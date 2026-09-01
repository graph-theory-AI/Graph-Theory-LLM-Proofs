# Graph-Theory-Auto

Unrefereed [GPT-5.6 Sol](https://openai.com) attempts at the open graph-theory
problems catalogued by Marc Lelarge at
[mlelarge.github.io/graph-conjectures](https://mlelarge.github.io/graph-conjectures).

Each record gets one max-effort, `reasoning.mode=pro` Responses call. The
model must either prove the claim, give an explicit counterexample, record a
precise partial result, or say it failed. **Labels in this repository are the
model's own verdicts.** They are not refereed, and a `proved` / `disproved`
row is not a theorem. Ultra / 64-subagent runs were not used.

Headline numbers live in [RESULTS.md](RESULTS.md) (regenerated from
`attacks/*/verdict.json`).

## Method

- **Queue.** Easiest-first open/partial arXiv records from Lelarge's difficulty
  ranking, plus six questions restored after
  [catalog extraction fixes](https://github.com/mlelarge/graph-conjectures/pull/3).
  Open Problem Garden entries were not attacked.
- **Prompt.** Catalog page + extracted statement JSON + arXiv abstract.
- **Model.** `gpt-5.6-sol`, effort `max`, `mode=pro`, `max_output_tokens=128000`.
- **Budget.** Hard euro cap in `attacks/spend.json`, with a per-call USD
  reserve so parallel jobs cannot overspend. Pricing is the Sol promo schedule
  through 2026-11-21 ($4 / $0.40 cached / $20 per 1M tokens; reasoning bills as
  output). Prepaid EUR→USD is taken from the first wallet (€250 credit ≈
  $241.36 API), not from a market FX rate.
- **Artifact.** `attacks/<id>/{prompt.md,output.md,verdict.json,usage.json}`.

A single call is capped at 128k output tokens (~$2.56 of output at promo
rates). The preflight reserve is a conservative **$3.50** because `mode=pro`
can do extra internal work.

## Layout

```
attack.py          # queue / run / sweep / summary
catalog/           # snapshot of the Lelarge catalog (not authored here)
attacks/<id>/      # one directory per attempted record
RESULTS.md         # generated index of verdicts
scripts/           # commit loop and campaign ops
```

## Setup

```bash
uv venv
uv pip install -r requirements.txt
# .env must contain OPENAI_API_KEY (gitignored)
```

```bash
python attack.py summary          # rebuild RESULTS.md
python attack.py spend            # remaining budget
python attack.py queue            # easiest-first leftover queue
python attack.py run --id ID      # one record, e.g. 2402.10782__01
python attack.py sweep --jobs 24 --hours 16
```

## License

Code is [MIT](LICENSE). Catalog JSON/Markdown under `catalog/` is copied from
[mlelarge/graph-conjectures](https://github.com/mlelarge/graph-conjectures);
see that repository for its data license. Model outputs in `attacks/` are
provided as research artifacts, not as verified mathematics.
