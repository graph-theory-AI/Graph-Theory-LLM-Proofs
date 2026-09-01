#!/usr/bin/env bash
# Resume the €400 campaign after the grok wrapper killed the 03:00 sweep.
# Does NOT reset spend. Recovers in-flight OpenAI responses, then sweeps.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== resume-400eur-sweep $(date -Is) ==="

"$ROOT/.venv/bin/python" -u "$ROOT/scripts/recover-inflight.py" \
  >>"$ROOT/attacks/recover-inflight.log" 2>&1 &
recover_pid=$!
echo "recover-inflight pid $recover_pid"

for i in $(seq 1 90); do
  if [[ -f "$ROOT/attacks/inflight-recover.json" ]]; then
    echo "mapping ready after ${i}s"
    break
  fi
  sleep 1
done

"$ROOT/.venv/bin/python" - <<'PY'
import json
from pathlib import Path
from datetime import datetime, timezone

root = Path("attacks")
mapping = {}
mp = root / "inflight-recover.json"
if mp.exists():
    mapping = json.loads(mp.read_text()).get("mapping") or {}
now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
orphans = []
for p in sorted(root.iterdir()):
    if not p.is_dir():
        continue
    if (p / "verdict.json").exists() or (p / "skipped.json").exists():
        continue
    if not (p / "claimed.json").exists():
        continue
    if p.name in mapping:
        continue
    (p / "skipped.json").write_text(
        json.dumps(
            {
                "id": p.name,
                "reason": "orphaned after wrapper kill; OpenAI response id unknown",
                "when": now,
            },
            indent=2,
        )
        + "\n"
    )
    orphans.append(p.name)
print("orphaned", orphans)
print("recovering", sorted(mapping))
PY

echo "launching sweep jobs=24 hours=16 $(date -Is)"
exec "$ROOT/.venv/bin/python" -u "$ROOT/attack.py" sweep --jobs 24 --hours 16
