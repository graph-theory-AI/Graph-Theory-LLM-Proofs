#!/usr/bin/env python3
"""Extract per-referee token usage from Claude Code task transcripts.

Scans the session tasks directory (JSONL transcripts of the verifier
sub-agents), matches each transcript to its target conjecture id via the
"target id <ID>" phrase in the launch prompt, sums token usage, and merges
the result into verification/usage.json (persistent across sessions, since
the tasks directory is a temporary session-specific location).

Usage: python3 verification/collect_usage.py [tasks_dir]
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_TASKS_DIR = (
    "/private/tmp/claude-479130717/-Users-viennot-dev-graph-conjectures/"
    "f7574d3e-ea52-4764-99bc-eebef21edbdd/tasks"
)
ID_RE = re.compile(r"target id (\d{4}\.\d{4,5}__\d{2})")


def scan_file(path: Path) -> dict | None:
    target, model = None, None
    tally = {
        "input_tokens": 0,
        "output_tokens": 0,
        "cache_read_input_tokens": 0,
        "cache_creation_input_tokens": 0,
    }
    turns = 0
    with path.open() as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = d.get("message")
            if not isinstance(msg, dict):
                continue
            if target is None and d.get("type") == "user":
                content = msg.get("content")
                text = content if isinstance(content, str) else json.dumps(content)
                m = ID_RE.search(text)
                if m:
                    target = m.group(1)
            if d.get("type") == "assistant":
                model = msg.get("model") or model
                usage = msg.get("usage") or {}
                if usage:
                    turns += 1
                for key in tally:
                    tally[key] += usage.get(key) or 0
    if target is None:
        return None
    return {
        "id": target,
        "model": model,
        "assistant_turns": turns,
        "billed_tokens": {k: v for k, v in tally.items()},
        "total_output_tokens": tally["output_tokens"],
        "total_input_tokens_incl_cache": (
            tally["input_tokens"]
            + tally["cache_read_input_tokens"]
            + tally["cache_creation_input_tokens"]
        ),
    }


def main() -> None:
    tasks_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_TASKS_DIR)
    usage_path = HERE / "usage.json"
    usage = json.loads(usage_path.read_text()) if usage_path.exists() else {}
    found = 0
    for path in sorted(tasks_dir.glob("*.output")):
        entry = scan_file(path)
        if entry is None:
            continue
        found += 1
        prev = usage.get(entry["id"])
        if prev and prev.get("_file") != path.name:
            # A second transcript for the same id (retry/resume in a new task):
            # keep the larger run to avoid double counting a superseded attempt.
            if prev["total_output_tokens"] >= entry["total_output_tokens"]:
                continue
        entry["_file"] = path.name
        usage[entry["id"]] = entry
    usage_path.write_text(json.dumps(usage, indent=2, sort_keys=True) + "\n")
    print(f"matched {found} transcripts; usage.json now covers {len(usage)} ids")


if __name__ == "__main__":
    main()
