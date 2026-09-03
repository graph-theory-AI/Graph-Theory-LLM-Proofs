#!/usr/bin/env python3
"""Generate verification/SUMMARY.md from verification/verdicts.json."""
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORDER = ["CONFIRMED", "MINOR_GAPS", "MAJOR_GAP", "FATAL_ERROR", "ALREADY_KNOWN", "UNVERIFIABLE"]

d = json.loads((HERE / "verdicts.json").read_text())
entries = d["verdicts"]
counts = Counter(e["review_verdict"] for e in entries)

lines = []
lines.append("# Adversarial verification of the 77 claimed proofs/disproofs")
lines.append("")
lines.append(f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} from the "
             "per-target reports in this directory (see `REFEREE_PROMPT.md` for the review "
             "protocol; `verdicts.json` for machine-readable verdicts; `scripts/<id>/` for "
             "reproducible computational checks).")
lines.append("")
lines.append("Each of the 77 `proved`/`disproved` self-reports in `../attacks/` was reviewed by an "
             "independent adversarial referee agent (model `claude-fable-5`) instructed to assume "
             "the writeup wrong, re-derive every step, verify every citation against fetched "
             "sources, and brute-force every finite construction.")
lines.append("")

lines.append("## Verdict counts")
lines.append("")
lines.append("| review verdict | n | share |")
lines.append("| --- | ---: | ---: |")
for v in ORDER:
    if counts.get(v):
        lines.append(f"| {v} | {counts[v]} | {counts[v]/len(entries):.0%} |")
lines.append(f"| **total** | **{len(entries)}** | |")
lines.append("")

# Cross-tabs
def crosstab(title, keyfn, keys):
    lines.append(f"## {title}")
    lines.append("")
    lines.append("| | " + " | ".join(ORDER[:5]) + " | total |")
    lines.append("| --- | " + " | ".join(["---:"] * 6))
    for k in keys:
        row = [e for e in entries if keyfn(e) == k]
        c = Counter(e["review_verdict"] for e in row)
        lines.append(f"| {k} | " + " | ".join(str(c.get(v, 0)) for v in ORDER[:5]) + f" | {len(row)} |")
    lines.append("")

crosstab("By model's claimed verdict", lambda e: e["claimed_verdict"], ["proved", "disproved"])
crosstab("By model's claimed confidence", lambda e: e["claimed_confidence"], ["high", "medium"])
crosstab("By model's would_publish flag", lambda e: e["claimed_would_publish"], [True, False])

lines.append("## Headline reading")
lines.append("")
conf = [e for e in entries if e["review_verdict"] == "CONFIRMED"]
near = [e for e in entries if e["review_verdict"] == "MINOR_GAPS"]
pub_conf = [e for e in conf if e["claimed_would_publish"]]
lines.append(f"- **{len(conf)} claims fully CONFIRMED** (correct, fairly interpreted, apparently new), "
             f"plus {len(near)} MINOR_GAPS (correct modulo routine repairs). "
             f"Of the model's {sum(1 for e in entries if e['claimed_would_publish'])} would_publish "
             f"claims, {len(pub_conf)} were fully confirmed.")
lines.append("- **Every FATAL_ERROR is an interpretation failure, not a computational error**: all 14 "
             "refute catalog transcription artifacts (lost overlines, > vs ≥, dropped hypotheses, "
             "inverted inequalities) or degenerate literal readings (p=1, p=2, K₁, tiny spheres); "
             "the internal mathematics was verified correct in every one.")
lines.append("- **The ALREADY_KNOWN pile (26) indicts catalog freshness more than the model**: most "
             "were scooped by 2024–2026 papers the 2026-05 auto-review missed or misjudged, several "
             "by mere weeks; a few statements were already settled inside the source papers themselves.")
lines.append("")

lines.append("## Confirmed claims (correct and apparently new)")
lines.append("")
for e in conf:
    tag = " **(would_publish)**" if e["claimed_would_publish"] else ""
    lines.append(f"- `{e['id']}` ({e['claimed_verdict']}){tag} — {e['one_line']}")
lines.append("")

lines.append("## Broken claims (FATAL_ERROR / MAJOR_GAP)")
lines.append("")
for e in entries:
    if e["review_verdict"] in ("FATAL_ERROR", "MAJOR_GAP"):
        lines.append(f"- `{e['id']}` ({e['claimed_verdict']}, {e['review_verdict']}) — {e['one_line']}")
lines.append("")

lines.append("## Correct but already known")
lines.append("")
for e in entries:
    if e["review_verdict"] == "ALREADY_KNOWN":
        lines.append(f"- `{e['id']}` ({e['claimed_verdict']}) — {e['one_line']}")
lines.append("")

lines.append("## Full table")
lines.append("")
lines.append("| id | claimed | conf. | publish? | review verdict | interp. ok | refs ok | code run |")
lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
for e in entries:
    lines.append(
        f"| [`{e['id']}`]({e['id']}.md) | {e['claimed_verdict']} | {e['claimed_confidence']} | "
        f"{'yes' if e['claimed_would_publish'] else 'no'} | {e['review_verdict']} | "
        f"{'y' if e['interpretation_ok'] else 'n'} | {'y' if e['references_ok'] else 'n'} | "
        f"{'y' if e['computation_run'] else 'n'} |")
lines.append("")

u = d.get("usage_totals", {})
toks = [e["review_tokens"]["output"] for e in entries if "review_tokens" in e]
lines.append("## Review cost")
lines.append("")
lines.append(f"- Model: `{', '.join(u.get('models', []))}` for all {u.get('reviews_with_usage')} reviews.")
lines.append(f"- Output tokens (incl. reasoning): {u.get('output_tokens'):,} total "
             f"(min {min(toks):,} / median {sorted(toks)[len(toks)//2]:,} / max {max(toks):,} per review).")
lines.append(f"- Input tokens incl. cache reads/writes: {u.get('input_tokens_incl_cache'):,}.")
lines.append("- Per-review token detail lives in `verdicts.json` (`review_tokens`) and `usage.json`.")
lines.append("")

(HERE / "SUMMARY.md").write_text("\n".join(lines) + "\n")
print(f"SUMMARY.md written: {len(entries)} entries, counts {dict(counts)}")
