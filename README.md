# Graph Theory LLM Proofs

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22706596.svg)](https://doi.org/10.5281/zenodo.22706596)

AI-assisted attempts at the open graph-theory problems catalogued by Marc
Lelarge and Laurent Viennot at
[graph-theory-ai.github.io/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures).

For each problem, [GPT-5.6 Sol and GPT-6 Astra](https://openai.com) are asked
to look for a proof, a counterexample, or a meaningful partial result. They may
also report that they could not make progress. These outputs are research
artifacts, not established mathematics: a `proved` or `disproved` label is the
model's own assessment.

[Claude Fable](https://www.anthropic.com/claude/fable) was asked to act as an
adversarial reviewer for the original GPT-5.6 Sol campaign: look for errors,
check cited sources, and reproduce computational claims where possible. This
is not human peer review, but its classification is the status used for that
campaign in this repository. The newer GPT-6 Astra results have not yet been
through this referee pass. The existing reports, methodology, and reproducible
checks are in [`verification/`](verification/).

For the complete generated indexes, see the
[original Sol results](RESULTS.md), [Astra OpenProblemGarden results](RESULTS_OPG.md),
[Astra arXiv additions](RESULTS_ARXIV_ASTRA.md), and
[Astra retry results](RESULTS_RETRY.md).

## Results

### Original GPT-5.6 Sol campaign

GPT-5.6 Sol completed 633 attacks. Claude Fable reviewed the 77 cases in which
the model reported a proof or a counterexample; the remaining categories were
not independently reviewed.

| GPT-5.6 Sol verdict | Records | Claude Fable review |
| --- | ---: | --- |
| proved | 31 | all 31 reviewed |
| disproved | 46 | all 46 reviewed |
| already_resolved | 25 | not reviewed |
| partial | 471 | not reviewed |
| ill_posed | 23 | not reviewed |
| unknown | 37 | not reviewed |

### New GPT-6 Astra campaign

GPT-6 Astra completed 563 attacks at reasoning effort `max` and `mode=pro` on
the flex service tier. These cover 466 distinct problems: all 227
OpenProblemGarden entries in the catalog and only 239 of the 692 arXiv records
in the ranked queue. Astra did **not** rerun the complete arXiv corpus: it
attacked 58 records that Sol had not reached and made a second attempt at 181
Sol outputs that remained open. The retry leg also revisited 97
OpenProblemGarden problems.

| Astra campaign leg | Progress | proved | disproved | already resolved | partial | unknown / no progress |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenProblemGarden first pass | 227 / 227 | 6 | 15 | 29 | 177 | 0 |
| Previously unattacked arXiv records | 58 / 58 | 0 | 6 | 1 | 51 | 0 |
| Second attempts (97 OPG + 181 arXiv) | 278 / 593 | 12 | 6 | 2 | 242 | 16 |

These verdicts are model self-reports and have not been independently
reviewed. Astra marked 31 outputs `would_publish`, including four partial
results; that flag is also the model's own assessment, not a validation or a
claim of literature priority. Full writeups, metadata, token usage, and
verdicts are stored under [`attacks_opg/`](attacks_opg/),
[`attacks_arxiv_astra/`](attacks_arxiv_astra/), and
[`attacks_retry/`](attacks_retry/).

PDF renderings are available for the 27 Astra outputs marked
`would_publish: true` with verdict `proved` or `disproved`; see
[`to_review_astra/`](to_review_astra/). These are unrefereed candidate
writeups, not validated notes. The four `would_publish` partial results are not
included.

### PDFs from the original Sol campaign

These 16 notes survived the LLM referee pass with `CONFIRMED` or
`MINOR_GAPS`, but have not yet been reviewed by a human mathematician.
Independent review is welcome; full provenance and referee reports are included
in each PDF. No Astra output has yet passed the referee stage; its separate PDF
collection consists of unverified renderings of the original model writeups.

Five of them now also have machine-checked Rocq/MathComp proofs in the
companion repository
[LLM4Rocq/graph-theory-rocq](https://github.com/LLM4Rocq/graph-theory-rocq),
linked in the last column below. Each is checked against a source-verified
formal statement and reports no added axioms. A formalization certifies the
formal proposition; whether that proposition faithfully renders the question
asked in the source paper is still a matter of source reading, so human review
of these notes remains wanted. One further confirmed claim that is not among
the 16 notes,
[2209.09107__00](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2209.09107__00/),
is formalized there as well.

If you would like to review one of these notes, please
[contact us by opening an issue](https://github.com/graph-theory-AI/Graph-Theory-LLM-Proofs/issues/new) or by email at `emanuele.natale🐌inria.fr`.

| Problem | Rocq formalization | PDF |
|:--|:--|:--|
| [Fair representation by matchings in bipartite graphs](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__03/) (`1611.03196__03`) | — | [note](to_review/1611.03196__03__fair-representation-matchings-bipartite-c-of-m-bound__note.pdf) |
| [Stable-set covers with no privately covered induced path](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1702.01094__01/) (`1702.01094__01`) | — | [note](to_review/1702.01094__01__stable-set-covers-no-privately-covered-induced-path__note.pdf) |
| [NP-completeness of fractional dichromatic number at threshold 2](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.02420__02/) (`1812.02420__02`) | — | [note](to_review/1812.02420__02__fractional-dichromatic-number-2-NP-complete__note.pdf) |
| [Directed Kneser graphs: acyclic sets versus intersecting families](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1812.02420__03/) (`1812.02420__03`) | [`directed_kneser_existence_disproved`](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/digraph-theory/theories/applications/directed_kneser_nonexistence.v) | [note](to_review/1812.02420__03__directed-Kneser-graphs-acyclic-iff-intersecting__note.pdf) |
| [Asymmetry of $\psi$ for biconstrained bipartite graphs](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1902.10878__01/) (`1902.10878__01`) | — | [note](to_review/1902.10878__01__concatenating-bipartite-graphs-psi-not-symmetric__note.pdf) |
| [Exact multicolour list-Ramsey number $R_\ell(\mathcal H_s,k)=s^k+1$](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2103.15175__00/) (`2103.15175__00`) | [`list_ramsey_chromatic_resolution`](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/extremal-graph-theory/theories/applications/list_ramsey_graph.v) | [note](to_review/2103.15175__00__multicolor-list-Ramsey-number-equals-s-to-the-k-plus-1__note.pdf) |
| [Monotone strategies in Levine's hat problem attain probability $1/2$](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2208.06858__01/) (`2208.06858__01`) | — | [note](to_review/2208.06858__01__Levine-hat-problem-monotone-strategies-reach-one-half__note.pdf) |
| [Unbounded-order 3-critical tournaments](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2310.04265__09/) (`2310.04265__09`) | [`question_5_9_disproved`](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/digraph-theory/theories/applications/question_5_9_resolution.v) | [note](to_review/2310.04265__09__3-critical-tournaments-clique-number-question-5.9__note.pdf) |
| [Asymptotics of hypercube partitions into squares](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2401.00299__02/) (`2401.00299__02`) | — | [note](to_review/2401.00299__02__hypercube-partitions-into-squares-asymptotics__note.pdf) |
| [Erdős–Szekeres bounds linear in the collinearity parameter](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2405.03455__00/) (`2405.03455__00`) | — | [note](to_review/2405.03455__00__Erdos-Szekeres-big-line-or-big-convex-polygon-linear-in-l__note.pdf) |
| [Chromatic–cochromatic gap three below clique number five](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2408.02400__00/) (`2408.02400__00`) | [`cochromatic_gap_three_proved`](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/chromatic-theory/theories/applications/cochromatic_gap/cochromatic_gap.v) | [note](to_review/2408.02400__00__chromatic-minus-cochromatic-number-Mycielski-construction__note.pdf) |
| [A non-transitive six-colouring with short colour-avoiding paths](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2512.10438__00/) (`2512.10438__00`) | [`problem_5_1_q6_n9`](https://github.com/LLM4Rocq/graph-theory-rocq/blob/main/digraph-theory/theories/applications/color_avoiding_tournament.v) | [note](to_review/2512.10438__00__color-avoiding-paths-tournaments-q6-N9-example__note.pdf) |
| [Sharp expansion exponent for classes with sublinear separators](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2001.09679__00/) (`2001.09679__00`) | — | [note](to_review/2001.09679__00__sublinear-separators-expansion-exponent-Dvorak-b-eps__note.pdf) |
| [Exponentially many nowhere-zero flows over $\mathbb Z_6$ and $\mathbb Z_7$](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2005.09767__00/) (`2005.09767__00`) | — | [note](to_review/2005.09767__00__group-connectivity-exponentially-many-flows-Z6-Z7__note.pdf) |
| [Expected faces in random graph embeddings grow as $\Theta(\log n)$](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2211.01032__02/) (`2211.01032__02`) | — | [note](to_review/2211.01032__02__random-embeddings-expected-faces-Theta-log-n__note.pdf) |
| [Induced saturation of even cycles via hypohamiltonian line graphs](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2505.24100__01/) (`2505.24100__01`) | — | [note](to_review/2505.24100__01__induced-saturation-even-cycles-line-graphs-hypohamiltonian__note.pdf) |

See [`to_review/README.md`](to_review/README.md) for source-paper links,
generation details, and literature updates.


## Details

The sections below describe the methodology, repository structure, and setup
required to reproduce and inspect the campaign.

<details>
<summary><strong>Method</strong></summary>

- **Queues.** The original Sol campaign attacked easiest-first open/partial
  arXiv records from Lelarge's difficulty ranking, plus six questions restored
  after
  [catalog extraction fixes](https://github.com/mlelarge/graph-conjectures/pull/3).
  The Astra campaign then covered all 227 OpenProblemGarden entries, but not
  the full arXiv queue: it attacked 58 arXiv records the first campaign had not
  reached and made 181 selected arXiv retries. A further 97 retries came from
  OpenProblemGarden, for 278 second attempts in total.
- **Prompt.** Catalog page + extracted statement JSON + arXiv abstract where
  applicable.
- **Attack models.** [GPT-5.6 Sol and GPT-6 Astra](https://openai.com), one
  Responses API call per attempt with effort `max`, `reasoning.mode=pro`, and
  `max_output_tokens=128000`. Astra ran on the flex service tier.
- **Review model.** The 77 claimed proofs/counterexamples were adversarially
  reviewed with [Claude Fable](https://www.anthropic.com/claude/fable); see
  [`verification/`](verification/) for the review protocol and reports. The
  Astra claims are not yet reviewed.
- **Budget.** Each campaign has a hard euro cap and a per-call USD reserve so
  parallel jobs cannot overspend. The Astra legs shared one €600 wallet and
  spent €584.88 ($564.66) across 563 calls. Prepaid EUR→USD accounting is
  taken from the API wallet rather than a market FX rate.
- **Artifact.** Each attempt stores `prompt.md`, `output.md`, `verdict.json`,
  `usage.json`, and `meta.json` in its campaign directory.

Each call is capped at 128k output tokens. The preflight reserve is $3.50 for
Sol and $8.00 for Astra because `mode=pro` can do extra internal work.

</details>

<details>
<summary><strong>Layout</strong></summary>

```
attack.py          # queue / run / sweep / summary
catalog/           # snapshot of the Lelarge catalog (not authored here)
attacks/<id>/      # one directory per attempted record
RESULTS.md         # generated index of verdicts
attacks_opg/        # Astra OpenProblemGarden first pass
attacks_arxiv_astra/# Astra arXiv records not reached by Sol
attacks_retry/      # Astra second attempts across both sources
RESULTS_*.md        # generated indexes for the Astra legs
to_review_astra/    # unrefereed Astra candidate-writeup PDFs
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
