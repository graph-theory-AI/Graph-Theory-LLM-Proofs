#!/usr/bin/env python3
"""Harvest Sol background responses left running after the wrapper killed the sweep."""

from __future__ import annotations

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import attack as A  # noqa: E402


def parse_ts(s: str | None) -> float | None:
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def inflight_resp_ids() -> list[str]:
    last: dict[str, str] = {}
    log = ROOT / "attacks" / "night-sweep.log"
    if not log.exists():
        return []
    for m in re.finditer(r"(resp_[a-z0-9]+) status=(\S+)", log.read_text()):
        last[m.group(1)] = m.group(2)
    return [rid for rid, st in last.items() if st == "in_progress"]


def claimed_without_verdict() -> list[tuple[str, float]]:
    out = []
    for p in sorted((ROOT / "attacks").iterdir()):
        if not p.is_dir():
            continue
        if (p / "verdict.json").exists() or (p / "skipped.json").exists():
            continue
        if not (p / "claimed.json").exists():
            continue
        meta = {}
        if (p / "meta.json").exists():
            meta = json.loads((p / "meta.json").read_text())
        claimed = json.loads((p / "claimed.json").read_text())
        ts = parse_ts(meta.get("started") or claimed.get("when"))
        if ts is None:
            continue
        out.append((p.name, ts))
    return out


def match_ids(client) -> dict[str, str]:
    rows = []
    for rid in inflight_resp_ids():
        resp = client.responses.retrieve(rid)
        rows.append((resp.created_at, rid, resp.status))
    claimed = claimed_without_verdict()
    used: set[str] = set()
    mapping: dict[str, str] = {}
    for created, rid, _st in sorted(rows):
        best = None
        for cid, ts in claimed:
            if cid in used:
                continue
            dt = abs(created - ts)
            if best is None or dt < best[0]:
                best = (dt, cid)
        if best and best[0] <= 3.0:
            mapping[best[1]] = rid
            used.add(best[1])
            A.log(f"map {best[1]} -> {rid} dt={best[0]:.1f}s")
        else:
            A.log(f"no catalog match for {rid} created={created} best={best}")
    return mapping


def save_response(rec_id: str, resp, started: float) -> str:
    out_dir = A.ATTACKS / rec_id
    out_dir.mkdir(parents=True, exist_ok=True)
    usage = A.usage_from_response(resp)
    usd = A.price_usd(usage["input_tokens"], usage["output_tokens"], usage["cached_tokens"])
    spend = A.load_spend()
    text = getattr(resp, "output_text", None) or ""
    verdict = A.parse_verdict(text)
    elapsed = max(time.time() - started, 0.0)
    (out_dir / "output.md").write_text(text)
    (out_dir / "usage.json").write_text(json.dumps(usage, indent=2) + "\n")
    (out_dir / "verdict.json").write_text(
        json.dumps(
            {
                **verdict,
                "id": rec_id,
                "model": A.MODEL,
                "usd": round(usd, 6),
                "eur": round(A.usd_to_eur(usd, spend), 6),
                "elapsed_s": round(elapsed, 1),
                "status": getattr(resp, "status", None),
                "response_id": getattr(resp, "id", None),
                "when": A.utc_now(),
                "recovered": True,
            },
            indent=2,
        )
        + "\n"
    )
    try:
        (out_dir / "raw.json").write_text(json.dumps(A.dump_response(resp), default=str) + "\n")
    except Exception:
        pass
    call_rec = {
        "when": A.utc_now(),
        "id": rec_id,
        "model": A.MODEL,
        "response_id": getattr(resp, "id", None),
        "status": getattr(resp, "status", None),
        "usd": round(usd, 6),
        "eur": round(A.usd_to_eur(usd, spend), 6),
        "usage": usage,
        "verdict": verdict.get("verdict"),
        "elapsed_s": round(elapsed, 1),
        "recovered": True,
    }
    rem = A.record_call(call_rec, reserved=0.0, consume_inflight=False)
    A.log(
        f"  RECOVERED {rec_id}  verdict={verdict.get('verdict')}  "
        f"${usd:.4f} (€{call_rec['eur']:.4f})  "
        f"in={usage['input_tokens']} out={usage['output_tokens']}  "
        f"spent €{rem['spent_eur']:.4f} / €{rem['budget_eur']:.2f}"
    )
    return verdict.get("verdict") or "unknown"


def main() -> None:
    A.load_dotenv()
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY missing")
    from openai import OpenAI

    client = OpenAI(timeout=120)
    mapping = match_ids(client)
    pid = os.getpid()
    for rec_id in mapping:
        dest = A.ATTACKS / rec_id
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "claimed.json").write_text(
            json.dumps({"id": rec_id, "pid": pid, "when": A.utc_now(), "recover": True}, indent=2)
            + "\n"
        )
    (A.ATTACKS / "inflight-recover.json").write_text(
        json.dumps({"when": A.utc_now(), "pid": pid, "mapping": mapping}, indent=2)
        + "\n"
    )

    pending = dict(mapping)
    while pending:
        done = []
        for rec_id, rid in list(pending.items()):
            if (A.ATTACKS / rec_id / "verdict.json").exists():
                done.append(rec_id)
                continue
            resp = client.responses.retrieve(rid)
            started = resp.created_at or time.time()
            if resp.status in {"queued", "in_progress"}:
                A.log(f"  … recover {rec_id} {rid} status={resp.status}")
                continue
            save_response(rec_id, resp, started)
            done.append(rec_id)
        for rec_id in done:
            pending.pop(rec_id, None)
        if pending:
            time.sleep(8)
    A.log("recover-inflight done")


if __name__ == "__main__":
    main()
