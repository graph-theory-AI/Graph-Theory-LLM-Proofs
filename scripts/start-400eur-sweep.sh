#!/usr/bin/env bash
# Wait until 03:00 Europe/Paris on 2026-09-01, reset the wallet to a fresh
# €400 prepaid campaign, then sweep unattacked records until that budget
# (or the wall-clock cap) is gone. Do not enable Ultra.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p "$ROOT/attacks"

LOCK="$ROOT/attacks/night-sweep.lock"
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "another start-400eur-sweep.sh already holds $LOCK" >&2
  exit 0
fi

echo "=== start-400eur-sweep $(date -Is) ==="

"$ROOT/.venv/bin/python" - <<'PY'
from datetime import datetime
from zoneinfo import ZoneInfo
import time

target = datetime(2026, 9, 1, 3, 0, 0, tzinfo=ZoneInfo("Europe/Paris"))
now = datetime.now(ZoneInfo("Europe/Paris"))
sleep_s = (target - now).total_seconds()
print(f"now={now.isoformat()} target={target.isoformat()} sleep_s={max(0, int(sleep_s))}", flush=True)
if sleep_s > 0:
    time.sleep(sleep_s)
print(f"wake {datetime.now(ZoneInfo('Europe/Paris')).isoformat()}", flush=True)
PY

"$ROOT/.venv/bin/python" - <<'PY'
import json
from datetime import datetime, timezone
from pathlib import Path

path = Path("attacks/spend.json")
spend = json.loads(path.read_text())
# First prepaid wallet: €250 credit billed as $241.360548 on the promo ledger.
usd_per_eur = 241.360548 / 250.0
eur_per_usd = 250.0 / 241.360548
history = list(spend.get("budget_history") or [])
history.append(
    {
        "when": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "from_eur": spend.get("budget_eur"),
        "to_eur": 400.0,
        "note": (
            "new €400 prepaid wallet at 03:00 Europe/Paris 2026-09-01; "
            "campaign spend reset; FX from first-wallet prepaid (€250 ≈ $241.36)"
        ),
    }
)
spend.update(
    {
        "budget_eur": 400.0,
        "usd_per_eur": usd_per_eur,
        "eur_per_usd": eur_per_usd,
        "fx_as_of": "2026-08-31-openai-prepaid",
        "safety_margin_eur": 5.0,
        "conservative_max_usd_per_call": 3.5,
        "spent_usd": 0.0,
        "spent_eur": 0.0,
        "reserved_usd": 0.0,
        "in_flight": 0,
        "stopped": False,
        "stop_reason": None,
        "budget_history": history,
    }
)
path.write_text(json.dumps(spend, indent=2) + "\n")
print(
    f"wallet reset budget_eur=400 usable=395 "
    f"usd_per_eur={usd_per_eur:.6f} n_attacks={spend.get('n_attacks')}",
    flush=True,
)
PY

if pgrep -f '[a]ttack.py sweep' >/dev/null; then
  echo "attack.py sweep already running; not launching another" >&2
  exit 0
fi

if ! pgrep -f '[c]ommit-loop.sh' >/dev/null; then
  nohup env INTERVAL=600 "$ROOT/scripts/commit-loop.sh" >>"$ROOT/attacks/commit-loop.log" 2>&1 &
  echo "commit-loop pid $!"
fi

echo "launching sweep jobs=24 hours=16 $(date -Is)"
exec "$ROOT/.venv/bin/python" -u "$ROOT/attack.py" sweep --jobs 24 --hours 16
