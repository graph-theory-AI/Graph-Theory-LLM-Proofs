#!/usr/bin/env bash
# Sweep the 227-problem OpenProblemGarden corpus with gpt-6-astra at maximum
# reasoning effort, against the separate EUR 600 wallet in attacks_opg/spend.json.
#
#   JOBS=16 HOURS=12 TIER=flex scripts/start-opg-astra-sweep.sh
#
# TIER=flex bills at half the standard rate and is the default here: the sweep
# is a batch job with no latency requirement. Use TIER=default to force the
# standard tier. The budget is enforced inside attack.py, not here.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p "$ROOT/attacks_opg"

JOBS="${JOBS:-16}"
HOURS="${HOURS:-12}"
TIER="${TIER:-flex}"

LOCK="$ROOT/attacks_opg/sweep.lock"
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "another start-opg-astra-sweep.sh already holds $LOCK" >&2
  exit 0
fi

if pgrep -f '[a]ttack.py sweep' >/dev/null; then
  echo "attack.py sweep already running; not launching another" >&2
  exit 0
fi

echo "=== start-opg-astra-sweep $(date -Is) jobs=$JOBS hours=$HOURS tier=$TIER ==="
"$ROOT/.venv/bin/python" "$ROOT/attack.py" spend --corpus opg
"$ROOT/.venv/bin/python" "$ROOT/attack.py" queue --corpus opg -n 5

if ! pgrep -f '[c]ommit-loop.sh' >/dev/null; then
  nohup env INTERVAL=900 COMMIT_SCRIPT="$ROOT/scripts/commit-opg-attacks.sh" \
    "$ROOT/scripts/commit-loop.sh" >>"$ROOT/attacks_opg/commit-loop.log" 2>&1 &
  echo "commit-loop pid $!"
fi

exec "$ROOT/.venv/bin/python" -u "$ROOT/attack.py" sweep \
  --corpus opg --service-tier "$TIER" --jobs "$JOBS" --hours "$HOURS"
