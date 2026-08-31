# Graph-Theory-Auto

Systematic Sol attacks on the open graph-theory conjectures catalogued at
[mlelarge.github.io/graph-conjectures](https://mlelarge.github.io/graph-conjectures).

Hard budget: **€250** of OpenAI API credit (started at €150, +€100 on
2026-08-31). Every call is priced, logged, and refused if it would breach
the remaining budget plus a €5 safety margin. The sweep wall-clock is a
soft cap; raise `--hours` rather than stopping while usable credit remains.

## Setup

```bash
uv venv
uv pip install -r requirements.txt
# .env must contain OPENAI_API_KEY (gitignored)
```

## Commands

```bash
python attack.py spend            # remaining budget
python attack.py queue            # easiest-first attack queue
python attack.py run --next       # next unattacked conjecture (budget-checked)
python attack.py run --id ID      # one specific record, e.g. 2402.10782__01
python attack.py run --limit N    # up to N new attacks, stopping on budget
python attack.py catalog-issues   # catalog defects to share with Marc Lelarge
python attack.py sweep --jobs 24 --hours 5   # spend the remaining budget in parallel
```

Each attack writes `attacks/<id>/` (prompt, model output, verdict, usage) and
appends `attacks/ledger.jsonl`. Running totals live in `attacks/spend.json`.

## Pricing (GPT-5.6 Sol, promo through 2026-11-21)

|             | per 1M tokens |
| ----------- | ------------: |
| input       |         $4.00 |
| cached input|         $0.40 |
| output (incl. reasoning) | $20.00 |

A single Responses call is capped at 128k output tokens, so the **hard
ceiling** of one max-effort request is about **$2.56 of output** plus a few
cents of input — unless `reasoning.mode=pro` internally aggregates extra work,
which is why the pre-flight reserve is a conservative **$15** per call.

Do **not** enable Ultra / 64-subagent runs: that is a different cost scale
(OpenAI's Cycle Double Cover experiment was ~$200/breakthrough).

## Catalog defects

Incomplete statements (empty official block, placeholder, truncated formula)
are logged rather than silently skipped:

- `CATALOG_ISSUES.md` — shareable list for Marc Lelarge
- `catalog/issues_severe.json` — machine-readable scan of all 762 arXiv records
- `catalog/issues.jsonl` — defects actually hit during an attack

`run --next` will not spend API credit on a placeholder statement.
