#!/usr/bin/env bash
# Third leg of the astra campaign. Waits for the OPG sweep and the arXiv leg to
# finish, then spends whatever is left of the same EUR 600 wallet on a second,
# stronger attempt at problems that are still open, most promising first:
#
#   1. claimed resolutions the adversarial referee pass rejected (FATAL_ERROR,
#      MAJOR_GAP) -- a full proof was within reach and the report says where it
#      broke;
#   2. `partial` at high confidence, easiest first;
#   3. everything else still open.
#
# Each retry gets the original prompt plus the earlier attempt and, when there
# is one, the referee report, framed as an unverified lead rather than an
# authority. Writes to attacks_retry/ so the first attempts stay intact.
#
#   MIN_EUR=20 JOBS=16 HOURS=10 TIER=flex scripts/continue-with-retry.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

MIN_EUR="${MIN_EUR:-20}"
JOBS="${JOBS:-16}"
HOURS="${HOURS:-10}"
TIER="${TIER:-flex}"
PY="$ROOT/.venv/bin/python"

echo "=== continue-with-retry: waiting for the earlier legs $(date -Is) ==="
while pgrep -f '[a]ttack.py sweep' >/dev/null || pgrep -f '[c]ontinue-with-arxiv.sh' >/dev/null; do
  sleep 60
done
echo "=== earlier legs finished $(date -Is) ==="

left=$("$PY" - <<'PY'
import json
d = json.load(open("attacks_opg/spend.json"))
print(f"{d['budget_eur'] - d['safety_margin_eur'] - d['spent_eur']:.2f}")
PY
)
echo "usable left on the shared wallet: EUR $left (minimum to start: EUR $MIN_EUR)"
if ! "$PY" -c "import sys; sys.exit(0 if float('$left') >= float('$MIN_EUR') else 1)"; then
  echo "not enough budget left; not starting the retry leg"
  exit 0
fi

"$PY" "$ROOT/attack.py" queue --corpus retry --wallet attacks_opg -n 8

if ! pgrep -f '[c]ommit-loop.sh' >/dev/null; then
  nohup env INTERVAL=900 COMMIT_SCRIPT="$ROOT/scripts/commit-opg-attacks.sh" \
    "$ROOT/scripts/commit-loop.sh" >>"$ROOT/attacks_opg/commit-loop.log" 2>&1 &
  echo "commit-loop pid $!"
fi

echo "launching retry leg jobs=$JOBS hours=$HOURS tier=$TIER $(date -Is)"
exec "$PY" -u "$ROOT/attack.py" sweep --corpus retry --model gpt-6-astra \
  --wallet attacks_opg --service-tier "$TIER" --jobs "$JOBS" --hours "$HOURS"
