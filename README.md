# Graph Theory LLM Proofs

[![DOI](https://zenodo.org/badge/1351775966.svg)](https://doi.org/10.5281/zenodo.22706596)

AI-assisted attempts at the open graph-theory problems catalogued by Marc
Lelarge and Laurent Viennot at
[graph-theory-ai.github.io/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures).

For each problem, [GPT-5.6 Sol](https://openai.com) is asked to look for a
proof, a counterexample, or a meaningful partial result. It may also report
that it could not make progress. These outputs are research artifacts, not
established mathematics: a `proved` or `disproved` label is the model's own
assessment.

[Claude Fable](https://www.anthropic.com/claude/fable) was asked to act as an adversarial reviewer: look for errors, check cited sources, and reproduce computational
claims where possible. This is not human peer review, but its classification
is the status used in this repository. The reports, methodology, and
reproducible checks are in [`verification/`](verification/).

For an overview of the campaign, see [RESULTS.md](RESULTS.md).

## Results

The model completed 633 attacks. Claude Fable reviewed the 77 cases in which GPT-5.6 Sol reported a proof or a counterexample; the remaining categories were not independently reviewed.

| GPT-5.6 Sol verdict | Records | Claude Fable review |
| --- | ---: | --- |
| proved | 31 | all 31 reviewed |
| disproved | 46 | all 46 reviewed |
| already_resolved | 25 | not reviewed |
| partial | 471 | not reviewed |
| ill_posed | 23 | not reviewed |
| unknown | 37 | not reviewed |

### PDFs for human review

These 16 notes survived the LLM referee pass with `CONFIRMED` or
`MINOR_GAPS`, but have not yet been reviewed by a human mathematician.
Independent review is welcome; full provenance and referee reports are included
in each PDF.

If you would like to review one of these notes, please
[contact us by opening an issue](https://github.com/graph-theory-AI/Graph-Theory-LLM-Proofs/issues/new) or by email at `emanuele.natale🐌inria.fr`.

| Problem | Claim | LLM referee | PDF |
|:--|:--|:--|:--|
| [Fair representation by matchings in bipartite graphs](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__03/) (`1611.03196__03`) | proved | CONFIRMED | [note](to_review/1611.03196__03__fair-representation-matchings-bipartite-c-of-m-bound__note.pdf) |
| [Stable-set covers with no privately covered induced path](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1702.01094__01/) (`1702.01094__01`) | disproved | CONFIRMED | [note](to_review/1702.01094__01__stable-set-covers-no-privately-covered-induced-path__note.pdf) |
| [NP-completeness of fractional dichromatic number at threshold 2](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.02420__02/) (`1812.02420__02`) | proved | CONFIRMED | [note](to_review/1812.02420__02__fractional-dichromatic-number-2-NP-complete__note.pdf) |
| [Directed Kneser graphs: acyclic sets versus intersecting families](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.02420__03/) (`1812.02420__03`) | disproved | CONFIRMED | [note](to_review/1812.02420__03__directed-Kneser-graphs-acyclic-iff-intersecting__note.pdf) |
| [Asymmetry of $\psi$ for biconstrained bipartite graphs](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1902.10878__01/) (`1902.10878__01`) | disproved | CONFIRMED | [note](to_review/1902.10878__01__concatenating-bipartite-graphs-psi-not-symmetric__note.pdf) |
| [Exact multicolour list-Ramsey number $R_\ell(\mathcal H_s,k)=s^k+1$](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2103.15175__00/) (`2103.15175__00`) | proved | CONFIRMED | [note](to_review/2103.15175__00__multicolor-list-Ramsey-number-equals-s-to-the-k-plus-1__note.pdf) |
| [Monotone strategies in Levine's hat problem attain probability $1/2$](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2208.06858__01/) (`2208.06858__01`) | disproved | CONFIRMED | [note](to_review/2208.06858__01__Levine-hat-problem-monotone-strategies-reach-one-half__note.pdf) |
| [Unbounded-order 3-critical tournaments](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2310.04265__09/) (`2310.04265__09`) | disproved | CONFIRMED | [note](to_review/2310.04265__09__3-critical-tournaments-clique-number-question-5.9__note.pdf) |
| [Asymptotics of hypercube partitions into squares](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2401.00299__02/) (`2401.00299__02`) | proved | CONFIRMED | [note](to_review/2401.00299__02__hypercube-partitions-into-squares-asymptotics__note.pdf) |
| [Erdős–Szekeres bounds linear in the collinearity parameter](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2405.03455__00/) (`2405.03455__00`) | proved | CONFIRMED | [note](to_review/2405.03455__00__Erdos-Szekeres-big-line-or-big-convex-polygon-linear-in-l__note.pdf) |
| [Chromatic–cochromatic gap three below clique number five](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2408.02400__00/) (`2408.02400__00`) | proved | CONFIRMED | [note](to_review/2408.02400__00__chromatic-minus-cochromatic-number-Mycielski-construction__note.pdf) |
| [A non-transitive six-colouring with short colour-avoiding paths](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2512.10438__00/) (`2512.10438__00`) | proved | CONFIRMED | [note](to_review/2512.10438__00__color-avoiding-paths-tournaments-q6-N9-example__note.pdf) |
| [Sharp expansion exponent for classes with sublinear separators](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2001.09679__00/) (`2001.09679__00`) | proved | MINOR_GAPS | [note](to_review/2001.09679__00__sublinear-separators-expansion-exponent-Dvorak-b-eps__note.pdf) |
| [Exponentially many nowhere-zero flows over $\mathbb Z_6$ and $\mathbb Z_7$](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2005.09767__00/) (`2005.09767__00`) | proved | MINOR_GAPS | [note](to_review/2005.09767__00__group-connectivity-exponentially-many-flows-Z6-Z7__note.pdf) |
| [Expected faces in random graph embeddings grow as $\Theta(\log n)$](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2211.01032__02/) (`2211.01032__02`) | proved | MINOR_GAPS | [note](to_review/2211.01032__02__random-embeddings-expected-faces-Theta-log-n__note.pdf) |
| [Induced saturation of even cycles via hypohamiltonian line graphs](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2505.24100__01/) (`2505.24100__01`) | proved | MINOR_GAPS | [note](to_review/2505.24100__01__induced-saturation-even-cycles-line-graphs-hypohamiltonian__note.pdf) |

See [`to_review/README.md`](to_review/README.md) for source-paper links,
generation details, and literature updates.


## Details

The sections below describe the methodology, repository structure, and setup
required to reproduce and inspect the campaign.

<details>
<summary><strong>Method</strong></summary>

- **Queue.** Easiest-first open/partial arXiv records from Lelarge's difficulty
  ranking, plus six questions restored after
  [catalog extraction fixes](https://github.com/mlelarge/graph-conjectures/pull/3).
  Open Problem Garden entries were not attacked.
- **Prompt.** Catalog page + extracted statement JSON + arXiv abstract.
- **Attack model.** [GPT-5.6 Sol](https://openai.com), one Responses API call
  per record with effort `max`, `reasoning.mode=pro`, and
  `max_output_tokens=128000`.
- **Review model.** The 77 claimed proofs/counterexamples were adversarially
  reviewed with [Claude Fable](https://www.anthropic.com/claude/fable); see
  [`verification/`](verification/) for the review protocol and reports.
- **Budget.** Hard euro cap in `attacks/spend.json`, with a per-call USD
  reserve so parallel jobs cannot overspend. Pricing is the Sol promo schedule
  through 2026-11-21 ($4 / $0.40 cached / $20 per 1M tokens; reasoning bills as
  output). Prepaid EUR→USD is taken from the first wallet (€250 credit ≈
  $241.36 API), not from a market FX rate.
- **Artifact.** `attacks/<id>/{prompt.md,output.md,verdict.json,usage.json}`.

A single call is capped at 128k output tokens (~$2.56 of output at promo
rates). The preflight reserve is a conservative **$3.50** because `mode=pro`
can do extra internal work.

</details>

<details>
<summary><strong>Layout</strong></summary>

```
attack.py          # queue / run / sweep / summary
catalog/           # snapshot of the Lelarge catalog (not authored here)
attacks/<id>/      # one directory per attempted record
RESULTS.md         # generated index of verdicts
verification/      # adversarial reviews of claimed proofs/counterexamples
scripts/           # commit loop and campaign ops
```

</details>

<details>
<summary><strong>Setup</strong></summary>

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

</details>

## How to cite

If you use these results, please cite this repository:

```bibtex
@dataset{lelarge2026aiassisted,
  author    = {Marc Lelarge and Emanuele Natale and Édouard Oyallon and
               Aurora Rossi and Laurent Viennot},
  title     = {AI-Assisted Proofs for Open Problems in Graph Theory},
  year      = {2026},
  version   = {1.0.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22706597},
  url       = {https://doi.org/10.5281/zenodo.22706597}
}
```

Machine-readable citation metadata are available in [`CITATION.cff`](CITATION.cff).

## Acknowledgements

The ChatGPT-based attack campaign used API access provided by the Lamarr
Institute for Machine Learning and Artificial Intelligence.

<p align="center">
  <img src="assets/lamarr-logo-2023-negative.svg" alt="Lamarr Institute for Machine Learning and Artificial Intelligence" width="300">
</p>

## License

Code is [MIT](LICENSE). Catalog JSON/Markdown under `catalog/` is copied from
[graph-theory-ai/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures/);
see that repository for its data license. Model outputs in `attacks/` are
provided as research artifacts, not as verified mathematics.
