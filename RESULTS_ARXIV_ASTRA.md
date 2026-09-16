# Results

Auto-generated from `attacks_arxiv_astra/*/verdict.json` by `python attack.py summary`.
**These are unrefereed model self-reports.** A `proved` / `disproved` label is
not a theorem. `would_publish` is the model's own claim that it would submit
the writeup to a journal.

Catalog: [mlelarge/graph-conjectures](https://graph-theory-ai.github.io/graph-conjectures).
Model: `gpt-5.6-sol`, reasoning effort `max`, `mode=pro`. Ultra / 64-subagent
runs were not used.

## Counts

Finished attacks with a verdict: **39**.
Spend (promo ledger × prepaid FX): **€241.22** billed USD
**$232.89** / budget €600
(safety margin €5).

| verdict | n | would_publish |
| --- | ---: | ---: |
| disproved | 4 | 1 |
| already_resolved | 1 | 0 |
| partial | 34 | 0 |

## Claimed proofs (0)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |

## Claimed counterexamples (4)

| id | conf. | publish? | one line |
| --- | --- | --- | --- |
| [`1611.03196__02`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__02/) · [artifact](attacks_arxiv_astra/1611.03196__02/) | high | no | The stated conjecture fails at maximum degree 4: seven edge classes of size 6 need not admit a matching meeting every class, even in a tree. |
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

Queue records not yet attacked: **19** (plus 0 skipped without a model call).

| id | tier | score | paper |
| --- | ---: | ---: | --- |
| [`2008.09692__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2008.09692__00/) | 4 | 4.5 | Coloring Drawings of Graphs |
| [`1907.11429__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1907.11429__00/) | 5 | 4.6 | Revisiting a theorem by Folkman on graph colouring |
| [`1608.03040__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1608.03040__00/) | 5 | 4.65 | Majority Colourings of Digraphs |
| [`1808.01605__01`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1808.01605__01/) | 5 | 4.75 | Triangle-free subgraphs with large fractional chromatic number |
| [`1604.07976__01`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1604.07976__01/) | 5 | 4.75 | Smaller Extended Formulations for the Spanning Tree Polytope of Bounded… |
| [`1612.08698__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1612.08698__00/) | 5 | 4.75 | List coloring with requests |
| [`1610.00876__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1610.00876__00/) | 5 | 4.8 | Subdivisions in digraphs of large out-degree or large dichromatic number |
| [`1806.00541__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1806.00541__00/) | 5 | 4.8 | Extension Complexity of the Correlation Polytope |
| [`1611.03196__01`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__01/) | 5 | 4.8 | Fair representation by independent sets |
| [`1803.03588__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1803.03588__00/) | 5 | 4.8 | Towards Erdos-Hajnal for graphs with no 5-hole |
| [`1705.04609__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1705.04609__00/) | 5 | 5.0 | Induced subgraphs of graphs with large chromatic number. X. Holes of sp… |
| [`1907.12999__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1907.12999__00/) | 5 | 5.0 | Independence number in triangle-free graphs avoiding a minor |
| [`1605.07411__01`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1605.07411__01/) | 5 | 5.0 | $χ$-bounded families of oriented graphs |
| [`1605.07411__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1605.07411__00/) | 5 | 5.0 | $χ$-bounded families of oriented graphs |
| [`1810.00058__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/1810.00058__00/) | 5 | 5.0 | Sparse graphs with no polynomial-sized anticomplete pairs |
| [`2110.00278__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2110.00278__00/) | 5 | 5.0 | Polynomial bounds for chromatic number. IV. A near-polynomial bound for… |
| [`2202.05557__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2202.05557__00/) | 5 | 5.0 | Polynomial bounds for chromatic number. V. Excluding a tree of radius t… |
| [`2302.08922__01`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2302.08922__01/) | 5 | 5.0 | A note on the Gyárfás-Sumner conjecture |
| [`2402.08418__00`](https://graph-theory-ai.github.io/graph-conjectures/arxiv/2402.08418__00/) | 5 | 5.0 | Variations on Sidorenko's conjecture in tournaments |

Generated 2026-09-16T20:27:59Z.
