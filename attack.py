#!/usr/bin/env python3
"""Sol-max attacks on graph-theory conjectures, with a hard €150 budget."""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CATALOG = ROOT / "catalog"
ATTACKS = ROOT / "attacks"
SPEND_PATH = ATTACKS / "spend.json"
LEDGER_PATH = ATTACKS / "ledger.jsonl"
LOCK_PATH = ATTACKS / "spend.lock"
QUEUE_PATH = CATALOG / "queue.json"
RANKING_PATH = CATALOG / "ARXIV_OPEN_DIFFICULTY_RANKING.md"

_THREAD_LOCK = threading.Lock()
_PRINT_LOCK = threading.Lock()

MODEL = "gpt-5.6-sol"
SITE_ARXIV = "https://mlelarge.github.io/graph-conjectures/arxiv/{id}/"
SITE_OPG = "https://mlelarge.github.io/graph-conjectures/op/{slug}/"
ARXIV_ABS = "https://arxiv.org/abs/{arxiv_id}"
ARXIV_HTML = "https://arxiv.org/html/{arxiv_id}"

# Promo rates through 2026-11-21 (OpenAI). Reasoning tokens bill as output.
PRICE = {
    "input": 4.00 / 1_000_000,
    "cached_input": 0.40 / 1_000_000,
    "output": 20.00 / 1_000_000,
    "long_input": 8.00 / 1_000_000,
    "long_cached": 0.80 / 1_000_000,
    "long_output": 30.00 / 1_000_000,
    "long_threshold": 272_000,
}

INSTRUCTIONS = """\
You are a research mathematician attacking an open graph-theory conjecture.

Rules:
- Work at the level of a careful Combinatorica / JCTB referee.
- A complete proof or an explicit counterexample is the goal. A precise
  partial result (special case, complexity classification, tighter bound)
  is an acceptable fallback. "I tried and here is why it is hard" is also
  acceptable — do not invent a proof.
- Do not reduce the claim to another unproven conjecture.
- Do not cite papers you have not verified exist. If literature status is
  uncertain, say so.
- Computational checks of small cases are welcome if they are fully specified.
- Never claim a theorem is proved unless every case is covered and you would
  be willing to submit the argument to a journal.

Output format, in this order:
1. A single fenced JSON block with exactly these keys:
   {
     "verdict": "proved" | "disproved" | "partial" | "no_progress" | "already_resolved" | "ill_posed",
     "confidence": "low" | "medium" | "high",
     "one_line": "<one sentence>",
     "would_publish": false,
     "caveats": "<short>"
   }
   `would_publish` is true only if you would actually submit this as a paper.
2. Then a full mathematical writeup (statement, argument, gaps).
"""


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_dotenv() -> None:
    path = ROOT / ".env"
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, val = line.split("=", 1)
        os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))


class _TextExtractor(HTMLParser):
    skip = {"script", "style", "nav", "footer", "header"}

    def __init__(self) -> None:
        super().__init__()
        self._skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.skip:
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in self.skip and self._skip:
            self._skip -= 1
        if tag in {"p", "div", "li", "h1", "h2", "h3", "h4", "tr", "br"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def html_to_text(html: str) -> str:
    p = _TextExtractor()
    p.feed(html)
    text = re.sub(r"[ \t]+", " ", "".join(p.parts))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def http_get(url: str, timeout: int = 60) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Graph-Theory-Auto/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


class SpendLock:
    """Process + thread exclusive lock around spend.json and claim files."""

    def __enter__(self):
        _THREAD_LOCK.acquire()
        LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.fh = open(LOCK_PATH, "a+")
        fcntl.flock(self.fh.fileno(), fcntl.LOCK_EX)
        return self

    def __exit__(self, exc_type, exc, tb):
        try:
            fcntl.flock(self.fh.fileno(), fcntl.LOCK_UN)
            self.fh.close()
        finally:
            _THREAD_LOCK.release()
        return False


def log(msg: str) -> None:
    with _PRINT_LOCK:
        print(msg, flush=True)


def load_spend() -> dict:
    data = json.loads(SPEND_PATH.read_text())
    data.setdefault("budget_eur", 250.0)
    data.setdefault("usd_per_eur", 1.158)
    data.setdefault("eur_per_usd", 1.0 / data["usd_per_eur"])
    data.setdefault("safety_margin_eur", 5.0)
    data.setdefault("conservative_max_usd_per_call", 3.5)
    data.setdefault("spent_usd", 0.0)
    data.setdefault("spent_eur", 0.0)
    data.setdefault("reserved_usd", 0.0)
    data.setdefault("in_flight", 0)
    data.setdefault("n_calls", 0)
    data.setdefault("n_attacks", 0)
    data.setdefault("stopped", False)
    return data


def save_spend(data: dict) -> None:
    SPEND_PATH.parent.mkdir(parents=True, exist_ok=True)
    SPEND_PATH.write_text(json.dumps(data, indent=2) + "\n")


def usd_to_eur(usd: float, spend: dict) -> float:
    return usd * spend["eur_per_usd"]


def remaining(spend: dict) -> dict:
    spent_eur = spend["spent_usd"] * spend["eur_per_usd"]
    reserved_usd = spend.get("reserved_usd", 0.0)
    reserved_eur = reserved_usd * spend["eur_per_usd"]
    usable = spend["budget_eur"] - spend["safety_margin_eur"]
    committed_eur = spent_eur + reserved_eur
    return {
        "budget_eur": spend["budget_eur"],
        "spent_usd": round(spend["spent_usd"], 6),
        "spent_eur": round(spent_eur, 6),
        "reserved_usd": round(reserved_usd, 6),
        "reserved_eur": round(reserved_eur, 6),
        "in_flight": spend.get("in_flight", 0),
        "safety_margin_eur": spend["safety_margin_eur"],
        "usable_eur": usable,
        "remaining_eur": round(spend["budget_eur"] - spent_eur, 6),
        "remaining_usable_eur": round(usable - committed_eur, 6),
        "stopped": bool(spend.get("stopped")),
        "stop_reason": spend.get("stop_reason"),
        "n_calls": spend.get("n_calls", 0),
        "n_attacks": spend.get("n_attacks", 0),
    }


def price_usd(input_tokens: int, output_tokens: int, cached_tokens: int = 0) -> float:
    long_ctx = input_tokens > PRICE["long_threshold"]
    if long_ctx:
        uncached = max(input_tokens - cached_tokens, 0)
        return (
            uncached * PRICE["long_input"]
            + cached_tokens * PRICE["long_cached"]
            + output_tokens * PRICE["long_output"]
        )
    uncached = max(input_tokens - cached_tokens, 0)
    return (
        uncached * PRICE["input"]
        + cached_tokens * PRICE["cached_input"]
        + output_tokens * PRICE["output"]
    )


def hard_ceiling_usd(max_output_tokens: int, assumed_input: int = 30_000) -> float:
    """Worst-case bill if the call fills max_output_tokens (short-context rates)."""
    return price_usd(assumed_input, max_output_tokens)


def reserve_amount(max_output_tokens: int, spend: dict) -> float:
    return max(
        spend.get("conservative_max_usd_per_call", 3.5),
        hard_ceiling_usd(max_output_tokens) * 1.15,
    )


def try_reserve(max_output_tokens: int) -> tuple[bool, float, dict]:
    """Atomically reserve worst-case USD for one in-flight call."""
    with SpendLock():
        spend = load_spend()
        amount = reserve_amount(max_output_tokens, spend)
        rem = remaining(spend)
        if spend.get("stopped"):
            return False, amount, rem
        need_eur = usd_to_eur(amount, spend)
        if rem["remaining_usable_eur"] < need_eur:
            spend["stopped"] = True
            spend["stop_reason"] = (
                f"preflight refused: remaining usable €{rem['remaining_usable_eur']:.2f} "
                f"< reserve €{need_eur:.2f} (${amount:.2f})"
            )
            save_spend(spend)
            return False, amount, remaining(spend)
        spend["reserved_usd"] = round(spend.get("reserved_usd", 0.0) + amount, 6)
        spend["in_flight"] = int(spend.get("in_flight", 0)) + 1
        save_spend(spend)
        return True, amount, remaining(spend)


def release_reserve(amount: float) -> dict:
    with SpendLock():
        spend = load_spend()
        spend["reserved_usd"] = round(max(spend.get("reserved_usd", 0.0) - amount, 0.0), 6)
        spend["in_flight"] = max(int(spend.get("in_flight", 0)) - 1, 0)
        save_spend(spend)
        return remaining(spend)


def record_call(record: dict, reserved: float) -> dict:
    with SpendLock():
        spend = load_spend()
        spend["spent_usd"] = round(spend["spent_usd"] + record["usd"], 6)
        spend["spent_eur"] = round(spend["spent_usd"] * spend["eur_per_usd"], 6)
        spend["reserved_usd"] = round(max(spend.get("reserved_usd", 0.0) - reserved, 0.0), 6)
        spend["in_flight"] = max(int(spend.get("in_flight", 0)) - 1, 0)
        spend["n_calls"] = spend.get("n_calls", 0) + 1
        spend["n_attacks"] = spend.get("n_attacks", 0) + 1
        rem = remaining(spend)
        if rem["remaining_usable_eur"] <= 0:
            spend["stopped"] = True
            spend["stop_reason"] = (
                f"usable budget exhausted: spent €{rem['spent_eur']:.4f} "
                f"/ €{spend['budget_eur']:.2f} (margin €{spend['safety_margin_eur']:.2f})"
            )
            rem = remaining(spend)
        save_spend(spend)
        LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
        with LEDGER_PATH.open("a") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        return rem


def parse_ranking() -> list[dict]:
    rows: list[dict] = []
    for line in RANKING_PATH.read_text().splitlines():
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        # Complete Ranking columns: Rank | Score | Tier | Lean | Status | Review | Record | Paper | …
        if not parts or not parts[0].isdigit() or len(parts) < 8:
            continue
        if not parts[2].isdigit():
            continue
        rec_id = parts[5].strip().strip("`")
        rows.append(
            {
                "rank_hardest": int(parts[0]),
                "score": float(parts[1]),
                "tier": int(parts[2]),
                "lean": parts[3],
                "status": parts[4],
                "id": rec_id,
                "title_md": parts[6],
                "paper": parts[7],
                "source": "arxiv",
                "url": SITE_ARXIV.format(id=rec_id),
            }
        )
    # Attack easiest first (lowest score / highest rank_hardest).
    rows.sort(key=lambda r: (r["tier"], r["score"], -r["rank_hardest"]))
    return [r for r in rows if r["status"] in {"open", "partial"}]


def attacked_ids() -> set[str]:
    done = set()
    if not ATTACKS.exists():
        return done
    for p in ATTACKS.iterdir():
        if p.is_dir() and (
            (p / "verdict.json").exists() or (p / "skipped.json").exists()
        ):
            done.add(p.name)
    return done


def pid_alive(pid: int) -> bool:
    if not pid:
        return False
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def is_busy(path: Path) -> bool:
    if (path / "verdict.json").exists() or (path / "skipped.json").exists():
        return True
    claimed = path / "claimed.json"
    if not claimed.exists():
        return False
    try:
        data = json.loads(claimed.read_text())
    except Exception:
        return False
    return pid_alive(int(data.get("pid") or 0))


def claim_next() -> dict | None:
    """Pick the next easiest complete record and mark it claimed."""
    with SpendLock():
        for rec in parse_ranking():
            dest = ATTACKS / rec["id"]
            if dest.exists() and is_busy(dest):
                continue
            dest.mkdir(parents=True, exist_ok=True)
            (dest / "claimed.json").write_text(
                json.dumps({"id": rec["id"], "pid": os.getpid(), "when": utc_now()}, indent=2)
                + "\n"
            )
            return rec
        return None


def cmd_queue(args: argparse.Namespace) -> None:
    rows = parse_ranking()
    QUEUE_PATH.write_text(json.dumps(rows, indent=2) + "\n")
    done = attacked_ids()
    pending = [r for r in rows if r["id"] not in done]
    n = args.n or 15
    print(f"{len(rows)} open/partial arXiv records; {len(done)} attacked; {len(pending)} pending")
    print(f"easiest {n}:")
    for r in pending[:n]:
        print(
            f"  tier {r['tier']}  {r['score']:.2f}  {r['status']:8}  {r['id']:22}  {r['paper'][:60]}"
        )


def fetch_dossier(rec: dict) -> dict:
    page_url = rec["url"]
    try:
        page_html = http_get(page_url)
        page_text = html_to_text(page_html)
    except Exception as exc:  # noqa: BLE001
        page_text = f"(failed to fetch {page_url}: {exc})"
    m = re.search(r"(\d{4}\.\d{4,5})", rec["id"])
    arxiv_id = m.group(1) if m else None
    abstract = ""
    if arxiv_id:
        try:
            abs_html = http_get(ARXIV_ABS.format(arxiv_id=arxiv_id))
            abstract = html_to_text(abs_html)
            # keep the abstract block, not the whole arxiv chrome
            if "Abstract:" in abstract:
                abstract = "Abstract:" + abstract.split("Abstract:", 1)[1]
            abstract = abstract[:6000]
        except Exception as exc:  # noqa: BLE001
            abstract = f"(failed to fetch arXiv abs: {exc})"
    return {
        "id": rec["id"],
        "url": page_url,
        "arxiv_id": arxiv_id,
        "page_text": page_text[:20000],
        "abstract": abstract,
        "tier": rec.get("tier"),
        "score": rec.get("score"),
        "lean": rec.get("lean"),
        "status": rec.get("status"),
        "paper": rec.get("paper"),
    }


def build_prompt(dossier: dict) -> str:
    return f"""Attack the following open graph-theory problem.

Catalog id: {dossier['id']}
Catalog status: {dossier.get('status')} (triage tier {dossier.get('tier')}, lean {dossier.get('lean')})
Catalog page: {dossier['url']}
Source paper: {dossier.get('paper')} (arXiv:{dossier.get('arxiv_id')})

=== Catalog page (statement + literature review) ===
{dossier['page_text']}

=== Source paper abstract / header ===
{dossier['abstract']}
"""


def parse_verdict(text: str) -> dict:
    default = {
        "verdict": "unknown",
        "confidence": "low",
        "one_line": "",
        "would_publish": False,
        "caveats": "no JSON block parsed",
    }
    if not text:
        return default
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.S)
    if not blocks:
        m = re.search(r"\{[^{}]*\"verdict\"[^{}]*\}", text, flags=re.S)
        raw = m.group(0) if m else None
    else:
        raw = blocks[0]
    if not raw:
        return default
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return default
    default.update({k: data.get(k, default.get(k)) for k in default})
    return default


def usage_from_response(resp) -> dict:
    u = getattr(resp, "usage", None)
    if u is None:
        return {
            "input_tokens": 0,
            "output_tokens": 0,
            "cached_tokens": 0,
            "reasoning_tokens": 0,
            "total_tokens": 0,
        }
    if hasattr(u, "model_dump"):
        d = u.model_dump()
    elif isinstance(u, dict):
        d = u
    else:
        d = {
            "input_tokens": getattr(u, "input_tokens", 0) or 0,
            "output_tokens": getattr(u, "output_tokens", 0) or 0,
            "total_tokens": getattr(u, "total_tokens", 0) or 0,
            "input_tokens_details": getattr(u, "input_tokens_details", None),
            "output_tokens_details": getattr(u, "output_tokens_details", None),
        }
    cached = 0
    details_in = d.get("input_tokens_details") or {}
    if isinstance(details_in, dict):
        cached = details_in.get("cached_tokens") or 0
    reasoning = 0
    details_out = d.get("output_tokens_details") or {}
    if isinstance(details_out, dict):
        reasoning = details_out.get("reasoning_tokens") or 0
    return {
        "input_tokens": d.get("input_tokens") or 0,
        "output_tokens": d.get("output_tokens") or 0,
        "cached_tokens": cached,
        "reasoning_tokens": reasoning,
        "total_tokens": d.get("total_tokens") or 0,
    }


def call_sol(prompt: str, max_output_tokens: int, timeout_s: int):
    from openai import OpenAI

    client = OpenAI(timeout=timeout_s)
    kwargs = dict(
        model=MODEL,
        instructions=INSTRUCTIONS,
        input=[{"role": "user", "content": prompt}],
        max_output_tokens=max_output_tokens,
        reasoning={"effort": "max", "mode": "pro", "summary": "auto"},
        store=True,
    )
    last_exc: Exception | None = None
    for attempt in range(8):
        try:
            try:
                resp = client.responses.create(background=True, **kwargs)
                background = True
            except Exception as exc:  # noqa: BLE001
                log(f"background create failed ({exc}); retrying synchronously")
                resp = client.responses.create(**kwargs)
                background = False
            if background:
                rid = resp.id
                t0 = time.time()
                while resp.status in {"queued", "in_progress"}:
                    if time.time() - t0 > timeout_s:
                        raise TimeoutError(
                            f"Sol call {rid} exceeded {timeout_s}s (status={resp.status})"
                        )
                    time.sleep(8)
                    resp = client.responses.retrieve(rid)
                    log(f"  … {rid} status={resp.status}  {int(time.time()-t0)}s")
            return resp
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            msg = str(exc).lower()
            status = getattr(exc, "status_code", None)
            if status == 429 or "rate" in msg or "overloaded" in msg:
                delay = min(120, 15 * (2 ** attempt))
                log(f"rate limit ({exc}); sleep {delay}s then retry {attempt+1}/8")
                time.sleep(delay)
                continue
            raise
    raise last_exc or RuntimeError("Sol call failed")


def dump_response(resp) -> dict:
    if hasattr(resp, "model_dump"):
        data = resp.model_dump()
    else:
        data = json.loads(resp.json()) if hasattr(resp, "json") else {"repr": str(resp)}
    # Drop bulky encrypted reasoning from the saved raw copy.
    out = []
    for item in data.get("output") or []:
        if isinstance(item, dict):
            item = dict(item)
            item.pop("encrypted_content", None)
        out.append(item)
    data["output"] = out
    return data


def cmd_spend(_: argparse.Namespace) -> None:
    rem = remaining(load_spend())
    print(json.dumps(rem, indent=2))


def select_records(args: argparse.Namespace) -> list[dict]:
    rows = parse_ranking()
    by_id = {r["id"]: r for r in rows}
    done = attacked_ids()
    if args.id:
        if args.id in by_id:
            return [by_id[args.id]]
        # allow attacking an id not in the ranking (manual)
        return [
            {
                "id": args.id,
                "tier": None,
                "score": None,
                "lean": None,
                "status": "open",
                "title_md": args.id,
                "paper": "",
                "source": "arxiv" if re.match(r"\d{4}\.\d+", args.id) else "opg",
                "url": SITE_ARXIV.format(id=args.id)
                if re.match(r"\d{4}\.\d+", args.id)
                else SITE_OPG.format(slug=args.id),
            }
        ]
    pending = [r for r in rows if r["id"] not in done]
    limit = args.limit if args.limit is not None else (1 if args.next else 0)
    if not limit:
        raise SystemExit("specify --id, --next, or --limit N")
    return pending[:limit]


INCOMPLETE_MARKERS = (
    "full statement not available",
    "statement unavailable",
    "[full statement not available",
    "verbatim statement not available",
    "statement not available:",
    "statement truncated in source",
    "mathematical conclusion truncated",
    "remainder of condition not captured",
)


def looks_incomplete(text: str) -> bool:
    low = (text or "").lower()
    return any(m in low for m in INCOMPLETE_MARKERS)


def attack_one(rec: dict, max_out: int, timeout_s: int, force: bool = False) -> str:
    """Attack one record. Returns a short status tag."""
    out_dir = ATTACKS / rec["id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    ok, reserved, rem = try_reserve(max_out)
    if not ok:
        log(f"STOP {rec['id']}: {rem.get('stop_reason')}")
        return "budget"
    log(
        f"attacking {rec['id']}  reserve ${reserved:.2f}  "
        f"spent €{rem['spent_eur']:.2f}  reserved €{rem['reserved_eur']:.2f}  "
        f"usable left €{rem['remaining_usable_eur']:.2f}"
    )
    try:
        dossier = fetch_dossier(rec)
        if (not force) and looks_incomplete(dossier["page_text"]):
            (out_dir / "skipped.json").write_text(
                json.dumps(
                    {
                        "id": rec["id"],
                        "reason": "catalog statement incomplete",
                        "when": utc_now(),
                    },
                    indent=2,
                )
                + "\n"
            )
            release_reserve(reserved)
            log(f"skip {rec['id']}: catalog statement incomplete (no API call)")
            return "skip"
        prompt = build_prompt(dossier)
        (out_dir / "prompt.md").write_text(prompt)
        (out_dir / "meta.json").write_text(
            json.dumps(
                {
                    "record": rec,
                    "dossier_meta": {
                        k: dossier[k]
                        for k in dossier
                        if k not in {"page_text", "abstract"}
                    },
                    "started": utc_now(),
                    "model": MODEL,
                    "reasoning": {"effort": "max", "mode": "pro"},
                },
                indent=2,
            )
            + "\n"
        )
        t0 = time.time()
        resp = call_sol(prompt, max_output_tokens=max_out, timeout_s=timeout_s)
        elapsed = time.time() - t0
        usage = usage_from_response(resp)
        usd = price_usd(usage["input_tokens"], usage["output_tokens"], usage["cached_tokens"])
        spend = load_spend()
        text = getattr(resp, "output_text", None) or ""
        verdict = parse_verdict(text)
        (out_dir / "output.md").write_text(text or "")
        (out_dir / "usage.json").write_text(json.dumps(usage, indent=2) + "\n")
        (out_dir / "verdict.json").write_text(
            json.dumps(
                {
                    **verdict,
                    "id": rec["id"],
                    "model": MODEL,
                    "usd": round(usd, 6),
                    "eur": round(usd_to_eur(usd, spend), 6),
                    "elapsed_s": round(elapsed, 1),
                    "status": getattr(resp, "status", None),
                    "response_id": getattr(resp, "id", None),
                    "when": utc_now(),
                },
                indent=2,
            )
            + "\n"
        )
        try:
            (out_dir / "raw.json").write_text(json.dumps(dump_response(resp), default=str) + "\n")
        except Exception:
            pass
        call_rec = {
            "when": utc_now(),
            "id": rec["id"],
            "model": MODEL,
            "response_id": getattr(resp, "id", None),
            "status": getattr(resp, "status", None),
            "usd": round(usd, 6),
            "eur": round(usd_to_eur(usd, spend), 6),
            "usage": usage,
            "verdict": verdict.get("verdict"),
            "elapsed_s": round(elapsed, 1),
        }
        rem = record_call(call_rec, reserved)
        log(
            f"  DONE {rec['id']}  verdict={verdict.get('verdict')}  "
            f"${usd:.4f} (€{call_rec['eur']:.4f})  "
            f"in={usage['input_tokens']} out={usage['output_tokens']} "
            f"(reasoning={usage['reasoning_tokens']})  "
            f"spent €{rem['spent_eur']:.4f} / €{rem['budget_eur']:.2f}  "
            f"in_flight={rem['in_flight']}"
        )
        return verdict.get("verdict") or "unknown"
    except Exception as exc:  # noqa: BLE001
        release_reserve(reserved)
        (out_dir / "error.txt").write_text(f"{utc_now()} {type(exc).__name__}: {exc}\n")
        log(f"ERROR {rec['id']}: {exc}")
        return "error"


def cmd_run(args: argparse.Namespace) -> None:
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY missing in environment / .env")
    recs = select_records(args)
    if not recs:
        print("nothing to attack")
        return
    for rec in recs:
        tag = attack_one(
            rec,
            max_out=args.max_output_tokens,
            timeout_s=args.timeout,
            force=bool(args.id),
        )
        if tag == "budget":
            break


def _sweep_worker(deadline: float, max_out: int, timeout_s: int) -> None:
    while time.time() < deadline:
        spend = load_spend()
        if spend.get("stopped"):
            return
        rec = claim_next()
        if rec is None:
            return
        tag = attack_one(rec, max_out=max_out, timeout_s=timeout_s, force=False)
        if tag == "budget":
            return


def cmd_sweep(args: argparse.Namespace) -> None:
    load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY missing in environment / .env")
    jobs = args.jobs
    hours = args.hours
    deadline = time.time() + hours * 3600
    rem = remaining(load_spend())
    log(
        f"SWEEP start jobs={jobs} hours={hours}  "
        f"spent €{rem['spent_eur']:.4f} / €{rem['budget_eur']:.2f}  "
        f"usable left €{rem['remaining_usable_eur']:.2f}"
    )
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        futs = [
            pool.submit(_sweep_worker, deadline, args.max_output_tokens, args.timeout)
            for _ in range(jobs)
        ]
        for fut in as_completed(futs):
            exc = fut.exception()
            if exc:
                log(f"worker crashed: {exc}")
    rem = remaining(load_spend())
    log(
        f"SWEEP done  spent €{rem['spent_eur']:.4f} / €{rem['budget_eur']:.2f}  "
        f"calls={rem['n_calls']} attacks={rem['n_attacks']}  "
        f"stop={rem.get('stop_reason')}"
    )
    if rem["spent_eur"] >= rem["budget_eur"] - rem["safety_margin_eur"]:
        print("DONE")
    else:
        print("DONE")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_spend = sub.add_parser("spend", help="print remaining budget")
    p_spend.set_defaults(func=cmd_spend)

    p_q = sub.add_parser("queue", help="rebuild easiest-first queue")
    p_q.add_argument("-n", type=int, default=15)
    p_q.set_defaults(func=cmd_queue)

    p_run = sub.add_parser("run", help="attack one or more conjectures")
    p_run.add_argument("--id", help="catalog id, e.g. 2402.10782__01")
    p_run.add_argument("--next", action="store_true", help="next unattacked easiest record")
    p_run.add_argument("--limit", type=int, help="max number of new attacks this invocation")
    p_run.add_argument("--max-output-tokens", type=int, default=128_000)
    p_run.add_argument("--timeout", type=int, default=10_800, help="seconds")
    p_run.set_defaults(func=cmd_run)

    p_sw = sub.add_parser("sweep", help="parallel attacks until budget or time is gone")
    p_sw.add_argument("--jobs", type=int, default=24, help="concurrent Sol calls")
    p_sw.add_argument("--hours", type=float, default=5.0, help="wall-clock cap")
    p_sw.add_argument("--max-output-tokens", type=int, default=128_000)
    p_sw.add_argument("--timeout", type=int, default=10_800, help="seconds per call")
    p_sw.set_defaults(func=cmd_sweep)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
