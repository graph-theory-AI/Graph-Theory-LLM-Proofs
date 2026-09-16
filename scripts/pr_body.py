#!/usr/bin/env python3
"""Render the astra campaign pull-request description from on-disk artifacts."""
import glob
import json
import os
from collections import Counter
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEGS = [
    ("attacks_opg", "OpenProblemGarden, all 227 problems", 227),
    ("attacks_arxiv_astra", "arXiv rows the first campaign never reached", 58),
    ("attacks_retry", "second attempt at problems still open", 593),
]
ORDER = ["proved", "disproved", "partial", "already_resolved", "ill_posed", "no_progress", "unknown"]


def load(d):
    rows = []
    for f in glob.glob(os.path.join(ROOT, d, "*", "verdict.json")):
        try:
            r = json.load(open(f))
        except Exception:
            continue
        r["_id"] = os.path.basename(os.path.dirname(f))
        rows.append(r)
    return rows


def main() -> None:
    spend = json.load(open(os.path.join(ROOT, "attacks_opg", "spend.json")))
    out = []
    out.append("Attacks on open graph-theory problems with `gpt-6-astra` at reasoning effort "
               "`max` and `mode=pro`, on the **flex** service tier, against a single "
               f"€{spend['budget_eur']:.0f} wallet.\n")
    out.append("Flex bills at half the standard rate for the same model and the same reasoning "
               "settings. That was decisive rather than cosmetic: at standard rates the "
               "OpenProblemGarden corpus alone would have cost about $595 against $574 of usable "
               "budget, so it would not have fit.\n")
    out.append("## Legs\n")
    out.append("All three bill the same wallet in `attacks_opg/spend.json`.\n")
    out.append("| leg | progress | spent | mean/attack | errors |")
    out.append("|:--|--:|--:|--:|--:|")
    all_rows = {}
    for d, label, total in LEGS:
        rows = load(d)
        all_rows[d] = rows
        errs = len(glob.glob(os.path.join(ROOT, d, "*", "error.txt")))
        if not rows:
            out.append(f"| {label} | not started | — | — | — |")
            continue
        usd = [r.get("usd", 0.0) for r in rows]
        out.append(f"| {label} | {len(rows)}/{total} | ${sum(usd):.2f} | "
                   f"${sum(usd)/len(usd):.2f} | {errs} |")
    usable = spend["budget_eur"] - spend["safety_margin_eur"] - spend["spent_eur"]
    out.append(f"\nWallet: €{spend['spent_eur']:.2f} of €{spend['budget_eur']:.0f} spent, "
               f"€{usable:.2f} usable left, {spend['n_attacks']} attacks.\n")

    out.append("## Verdicts\n")
    out.append("| leg | " + " | ".join(ORDER) + " |")
    out.append("|:--|" + "--:|" * len(ORDER))
    for d, label, _ in LEGS:
        rows = all_rows.get(d) or []
        if not rows:
            continue
        c = Counter(r.get("verdict") for r in rows)
        out.append(f"| {label} | " + " | ".join(str(c.get(k, 0)) for k in ORDER) + " |")

    pub = [(d, r) for d, _, _ in LEGS for r in (all_rows.get(d) or []) if r.get("would_publish")]
    out.append(f"\n## Claimed resolutions the model would submit ({len(pub)})\n")
    out.append("Self-reports, not results. In the first campaign the adversarial referee pass cut "
               "77 claimed resolutions to 25 confirmed and 26 already known, rejecting 17 outright. "
               "None of these has been through that pass yet.\n")
    out.append("| id | verdict | claim |")
    out.append("|:--|:--|:--|")
    for d, r in sorted(pub, key=lambda x: (x[0], x[1]["_id"])):
        one = (r.get("one_line") or "").replace("|", "\\|")[:150]
        out.append(f"| `{r['_id']}` | {r.get('verdict')} | {one} |")

    out.append("\n## What is in the diff\n")
    out.append("- `attack.py`: `--corpus {arxiv,opg,retry}`, `--model` with a per-model price "
               "table, `--service-tier` (flex by default), and `--attacks-dir` / `--wallet` / "
               "`--done-dir`, which separate where attacks are written, which wallet they bill, "
               "and which finished attacks count as done. The driver previously indexed only the "
               "arXiv catalogue, so the 227 OpenProblemGarden problems were unreachable.")
    out.append("- `scripts/`: one launcher per leg, chained; a campaign committer; and this "
               "description generator. No script starts a commit loop on its own.")
    out.append("- `attacks_opg/`, `attacks_arxiv_astra/`, `attacks_retry/`: artifacts, each with "
               "prompt, writeup, usage and verdict. The gpt-5.6-sol artifacts in `attacks/` are "
               "untouched.")
    out.append("- `RESULTS_OPG.md`, `RESULTS_ARXIV_ASTRA.md`, `RESULTS_RETRY.md`: generated "
               "summaries, one per leg.")

    out.append("\n## Notable\n")
    retry = all_rows.get("attacks_retry") or []
    if retry:
        try:
            rej = {e["id"] for e in json.load(open(os.path.join(ROOT, "verification", "verdicts.json")))["verdicts"]
                   if e["review_verdict"] in ("FATAL_ERROR", "MAJOR_GAP")}
        except Exception:
            rej = set()
        hit = [r for r in retry if r["_id"] in rej]
        if hit:
            saved = sum(1 for r in hit if r.get("would_publish"))
            out.append(f"- All {len(hit)} of the {len(rej)} claims the referee pass rejected have "
                       f"been retried, with the flawed proof and the referee report supplied as "
                       f"context. {saved or 'None'} produced a publishable resolution, which is "
                       "evidence the referee pass was catching real errors rather than being "
                       "over-strict.")
    opg = all_rows.get("attacks_opg") or []
    if opg:
        n_ar = sum(1 for r in opg if r.get("verdict") == "already_resolved")
        out.append(f"- {n_ar} of the {len(opg)} OpenProblemGarden problems came back "
                   "`already_resolved`. If those hold up they identify catalogue entries the "
                   "literature has since closed, which is plausible for entries dating to 2008.")
    out.append("\n---\n")
    out.append(f"_Generated by `scripts/update-pr.sh` from the artifacts on disk, "
               f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC._")
    print("\n".join(out))


if __name__ == "__main__":
    main()
