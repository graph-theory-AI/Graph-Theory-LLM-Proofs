# Results

Auto-generated from `attacks_arxiv_astra/*/verdict.json` by `python attack.py summary`.
**These are unrefereed model self-reports.** A `proved` / `disproved` label is
not a theorem. `would_publish` is the model's own claim that it would submit
the writeup to a journal.

Catalog: [mlelarge/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures).
Model: `gpt-5.6-sol`, reasoning effort `max`, `mode=pro`. Ultra / 64-subagent
runs were not used.

## Counts

Finished attacks with a verdict: **56**.
Spend (promo ledger × prepaid FX): **€258.27** billed USD
**$249.35** / budget €600
(safety margin €5).

| verdict | n | would_publish |
| --- | ---: | ---: |
| disproved | 6 | 1 |
| already_resolved | 1 | 0 |
| partial | 49 | 0 |

## Claimed proofs (0)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |

## Claimed counterexamples (6)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |
| [`1611.03196__01`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__01/) · [artifact](attacks_arxiv_astra/1611.03196__01/) | high | no | The displayed conjecture fails for an explicit partition of E(K_{12,12}) into nine parts, with j=9. |
| [`1611.03196__02`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__02/) · [artifact](attacks_arxiv_astra/1611.03196__02/) | high | no | The stated conjecture fails at maximum degree 4: seven edge classes of size 6 need not admit a matching meeting every class, even in a tree. |
| [`1810.00058__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1810.00058__00/) · [artifact](attacks_arxiv_astra/1810.00058__00/) | high | no | The displayed linear-linear statement is false already for H = K_3, by a sparse random-graph construction followed by vertex deletion. |
| [`1912.01570__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1912.01570__00/) · [artifact](attacks_arxiv_astra/1912.01570__00/) | high | yes | A 12-vertex planar graph has fvs = 5 and fp = 2; a related family has fvs/fp tending to 3. |
| [`2009.13319__01`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2009.13319__01/) · [artifact](attacks_arxiv_astra/2009.13319__01/) | high | no | Randomly ordered line graphs of complete bipartite graphs refute the conjecture with H the directed triangle and F any orientation of the claw. |
| [`2009.13319__02`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2009.13319__02/) · [artifact](attacks_arxiv_astra/2009.13319__02/) | high | no | With K_k edgeless as explicitly stipulated, iterated cyclic-triangle tournaments disprove the statement already for k=2 and a directed three-vertex path. |

## Already resolved (model says the literature already closed it) (1)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |
| [`1701.03366__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1701.03366__00/) · [artifact](attacks_arxiv_astra/1701.03366__00/) | high | no | The list-flow theorem stated in the supplied source abstract proves the claim by assigning the list {1,2} to every arc over Z_5. |

## Ill-posed / no determinate statement as supplied (0)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |

## Coverage

The sweep queue is the easiest-first open/partial arXiv ranking (692
records, including a handful of questions restored after catalog extraction
fixes). Open Problem Garden entries were **not** attacked.

Queue records not yet attacked: **2** (plus 0 skipped without a model call).

| id | tier | score | paper |
| --- | ---: | ---: | --- |
| [`1907.12999__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1907.12999__00/) | 5 | 5.0 | Independence number in triangle-free graphs avoiding a minor |
| [`2110.00278__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2110.00278__00/) | 5 | 5.0 | Polynomial bounds for chromatic number. IV. A near-polynomial bound for… |

Generated 2026-09-16T20:43:02Z.
