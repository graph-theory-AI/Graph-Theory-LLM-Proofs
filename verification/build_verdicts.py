#!/usr/bin/env python3
"""Aggregate verification/<id>.md YAML headers into verification/verdicts.json.

Run from the repo root or from verification/: `python3 verification/build_verdicts.py`
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOOLS = {"true": True, "false": False}
KEYS = [
    "id", "claimed_verdict", "review_verdict", "confidence",
    "interpretation_ok", "references_ok", "computation_run", "one_line",
]


def parse_header(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"\s*---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {"id": path.stem, "error": "no YAML header"}
    entry = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip().strip('"')
        if key in KEYS:
            entry[key] = BOOLS.get(value.lower(), value)
    entry.setdefault("id", path.stem)
    missing = [k for k in KEYS if k not in entry]
    if missing:
        entry["missing_fields"] = missing
    return entry


def main() -> None:
    targets = {t["id"]: t for t in json.loads((HERE / "targets.json").read_text())}
    usage_path = HERE / "usage.json"
    usage = json.loads(usage_path.read_text()) if usage_path.exists() else {}
    entries = []
    for path in sorted(HERE.glob("*.md")):
        if path.stem not in targets:
            continue  # skip PROGRESS.md, SUMMARY.md, REFEREE_PROMPT.md, ...
        entry = parse_header(path)
        claim = targets[path.stem]
        entry["claimed_confidence"] = claim.get("confidence")
        entry["claimed_would_publish"] = claim.get("would_publish")
        entry["claimed_one_line"] = claim.get("one_line")
        u = usage.get(path.stem)
        if u:
            entry["review_model"] = u.get("model")
            entry["review_tokens"] = {
                "output": u["billed_tokens"]["output_tokens"],
                "input_uncached": u["billed_tokens"]["input_tokens"],
                "cache_read": u["billed_tokens"]["cache_read_input_tokens"],
                "cache_creation": u["billed_tokens"]["cache_creation_input_tokens"],
            }
            entry["review_assistant_turns"] = u.get("assistant_turns")
        entries.append(entry)
    reviewed = {e["id"] for e in entries}
    pending = sorted(set(targets) - reviewed)
    out = {
        "reviewed": len(entries),
        "pending": pending,
        "counts": {},
        "verdicts": entries,
    }
    for e in entries:
        v = e.get("review_verdict", "?")
        out["counts"][v] = out["counts"].get(v, 0) + 1
    with_usage = [e for e in entries if "review_tokens" in e]
    if with_usage:
        out["usage_totals"] = {
            "reviews_with_usage": len(with_usage),
            "models": sorted({e["review_model"] for e in with_usage}),
            "output_tokens": sum(e["review_tokens"]["output"] for e in with_usage),
            "input_tokens_incl_cache": sum(
                e["review_tokens"]["input_uncached"]
                + e["review_tokens"]["cache_read"]
                + e["review_tokens"]["cache_creation"]
                for e in with_usage
            ),
        }
    (HERE / "verdicts.json").write_text(json.dumps(out, indent=2) + "\n")
    print(f"{len(entries)} reviewed, {len(pending)} pending; counts: {out['counts']}")


if __name__ == "__main__":
    main()
