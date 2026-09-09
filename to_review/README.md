# Results to review

Claimed resolutions of open problems from the catalog that (a) the attacking model
itself flagged as `would_publish: true`, and (b) survived the adversarial referee pass
in `../verification/` with verdict **CONFIRMED** (12) or **MINOR_GAPS** (4,
correct modulo routine repairable details), and were not found to be already in the
literature. Total: 16.

Two kinds of PDF, distinguished by the file-name suffix:

- `__note.pdf` (16): a self-contained mathematical note rewritten from the model's
  writeup (statement, proof ideas, full proofs in Appendix A, the verbatim LLM referee
  report in Appendix B). Every deviation from the original writeup is declared in the
  provenance box on page 1. For the MINOR_GAPS items the gaps named by the referee were
  repaired in the rewrite, and each repair is marked where it occurs.
- `__writeup.pdf` (0): the model's writeup verbatim, with a summary
  table, the problem statement and the referee report appended (none at present; this is
  what an id without a `src/<id>/note.tex` produces).

Sources are in `src/<id>/` (`note.tex` where a note exists). Regenerate everything with
`python3 to_review/build.py`.

**Caveat.** Nothing here has been checked by a human mathematician. "CONFIRMED" is the
verdict of an LLM referee, and novelty was checked only against the indexed literature.

| id | problem | source paper | claim | referee | format | pdf |
|:--|:--|:--|:--|:--|:--|:--|
| [`1611.03196__03`](https://mlelarge.github.io/graph-conjectures/arxiv/1611.03196__03/) | Conjecture 1.15 | *Fair representation by independent sets* ([arXiv:1611.03196](https://arxiv.org/abs/1611.03196)) | proved | CONFIRMED | rewritten note | [1611.03196__03__fair-representation-matchings-bipartite-c-of-m-bound__note.pdf](1611.03196__03__fair-representation-matchings-bipartite-c-of-m-bound__note.pdf) |
| [`1702.01094__01`](https://mlelarge.github.io/graph-conjectures/arxiv/1702.01094__01/) | Question (uniquely-covered vertices in an induced path) | *Induced subgraphs of graphs with large chromatic number. IX. Rainbow pa…* ([arXiv:1702.01094](https://arxiv.org/abs/1702.01094)) | disproved | CONFIRMED | rewritten note | [1702.01094__01__stable-set-covers-no-privately-covered-induced-path__note.pdf](1702.01094__01__stable-set-covers-no-privately-covered-induced-path__note.pdf) |
| [`1812.02420__02`](https://mlelarge.github.io/graph-conjectures/arxiv/1812.02420__02/) | Problem 3.21 | *On the Complexity of Digraph Colourings and Vertex Arboricity* ([arXiv:1812.02420](https://arxiv.org/abs/1812.02420)) | proved | CONFIRMED | rewritten note | [1812.02420__02__fractional-dichromatic-number-2-NP-complete__note.pdf](1812.02420__02__fractional-dichromatic-number-2-NP-complete__note.pdf) |
| [`1812.02420__03`](https://mlelarge.github.io/graph-conjectures/arxiv/1812.02420__03/) | Problem 5.40 | *On the Complexity of Digraph Colourings and Vertex Arboricity* ([arXiv:1812.02420](https://arxiv.org/abs/1812.02420)) | disproved | CONFIRMED | rewritten note | [1812.02420__03__directed-Kneser-graphs-acyclic-iff-intersecting__note.pdf](1812.02420__03__directed-Kneser-graphs-acyclic-iff-intersecting__note.pdf) |
| [`1902.10878__01`](https://mlelarge.github.io/graph-conjectures/arxiv/1902.10878__01/) | Open Question — symmetry of $\psi$ (biconstrained case) | *Concatenating bipartite graphs* ([arXiv:1902.10878](https://arxiv.org/abs/1902.10878)) | disproved | CONFIRMED | rewritten note | [1902.10878__01__concatenating-bipartite-graphs-psi-not-symmetric__note.pdf](1902.10878__01__concatenating-bipartite-graphs-psi-not-symmetric__note.pdf) |
| [`2103.15175__00`](https://mlelarge.github.io/graph-conjectures/arxiv/2103.15175__00/) | Conjecture on $R_\ell(\mathcal{H}_s, k)$ | *Multicolor list Ramsey numbers grow exponentially* ([arXiv:2103.15175](https://arxiv.org/abs/2103.15175)) | proved | CONFIRMED | rewritten note | [2103.15175__00__multicolor-list-Ramsey-number-equals-s-to-the-k-plus-1__note.pdf](2103.15175__00__multicolor-list-Ramsey-number-equals-s-to-the-k-plus-1__note.pdf) |
| [`2208.06858__01`](https://mlelarge.github.io/graph-conjectures/arxiv/2208.06858__01/) | Conjecture 2.2 | *The success probability in Levine's hat problem, and independent sets i…* ([arXiv:2208.06858](https://arxiv.org/abs/2208.06858)) | disproved | CONFIRMED | rewritten note | [2208.06858__01__Levine-hat-problem-monotone-strategies-reach-one-half__note.pdf](2208.06858__01__Levine-hat-problem-monotone-strategies-reach-one-half__note.pdf) |
| [`2310.04265__09`](https://mlelarge.github.io/graph-conjectures/arxiv/2310.04265__09/) | Question 5.9 | *Clique number of tournaments* ([arXiv:2310.04265](https://arxiv.org/abs/2310.04265)) | disproved | CONFIRMED | rewritten note | [2310.04265__09__3-critical-tournaments-clique-number-question-5.9__note.pdf](2310.04265__09__3-critical-tournaments-clique-number-question-5.9__note.pdf) |
| [`2401.00299__02`](https://mlelarge.github.io/graph-conjectures/arxiv/2401.00299__02/) | Problem 1.9 | *Partitioning the hypercube into smaller hypercubes* ([arXiv:2401.00299](https://arxiv.org/abs/2401.00299)) | proved | CONFIRMED | rewritten note | [2401.00299__02__hypercube-partitions-into-squares-asymptotics__note.pdf](2401.00299__02__hypercube-partitions-into-squares-asymptotics__note.pdf) |
| [`2405.03455__00`](https://mlelarge.github.io/graph-conjectures/arxiv/2405.03455__00/) | Open Problem (Introduction) | *Big line or big convex polygon* ([arXiv:2405.03455](https://arxiv.org/abs/2405.03455)) | proved | CONFIRMED | rewritten note | [2405.03455__00__Erdos-Szekeres-big-line-or-big-convex-polygon-linear-in-l__note.pdf](2405.03455__00__Erdos-Szekeres-big-line-or-big-convex-polygon-linear-in-l__note.pdf) |
| [`2408.02400__00`](https://mlelarge.github.io/graph-conjectures/arxiv/2408.02400__00/) | Problem 1.5 | *On the difference between the chromatic and cochromatic number* ([arXiv:2408.02400](https://arxiv.org/abs/2408.02400)) | proved | CONFIRMED | rewritten note | [2408.02400__00__chromatic-minus-cochromatic-number-Mycielski-construction__note.pdf](2408.02400__00__chromatic-minus-cochromatic-number-Mycielski-construction__note.pdf) |
| [`2512.10438__00`](https://mlelarge.github.io/graph-conjectures/arxiv/2512.10438__00/) | Problem 5.1 | *Color-avoiding directed paths in tournaments* ([arXiv:2512.10438](https://arxiv.org/abs/2512.10438)) | proved | CONFIRMED | rewritten note | [2512.10438__00__color-avoiding-paths-tournaments-q6-N9-example__note.pdf](2512.10438__00__color-avoiding-paths-tournaments-q6-N9-example__note.pdf) |
| [`2001.09679__00`](https://mlelarge.github.io/graph-conjectures/arxiv/2001.09679__00/) | Informal open question on the exact value of $b_\varepsilon$ | *A note on sublinear separators and expansion* ([arXiv:2001.09679](https://arxiv.org/abs/2001.09679)) | proved | MINOR_GAPS | rewritten note | [2001.09679__00__sublinear-separators-expansion-exponent-Dvorak-b-eps__note.pdf](2001.09679__00__sublinear-separators-expansion-exponent-Dvorak-b-eps__note.pdf) |
| [`2005.09767__00`](https://mlelarge.github.io/graph-conjectures/arxiv/2005.09767__00/) | Conjecture 1.10 | *Many flows in the group connectivity setting* ([arXiv:2005.09767](https://arxiv.org/abs/2005.09767)) | proved | MINOR_GAPS | rewritten note | [2005.09767__00__group-connectivity-exponentially-many-flows-Z6-Z7__note.pdf](2005.09767__00__group-connectivity-exponentially-many-flows-Z6-Z7__note.pdf) |
| [`2211.01032__02`](https://mlelarge.github.io/graph-conjectures/arxiv/2211.01032__02/) | Conjecture 9.3 | *Random Embeddings of Graphs: The Expected Number of Faces in Most Graph…* ([arXiv:2211.01032](https://arxiv.org/abs/2211.01032)) | proved | MINOR_GAPS | rewritten note | [2211.01032__02__random-embeddings-expected-faces-Theta-log-n__note.pdf](2211.01032__02__random-embeddings-expected-faces-Theta-log-n__note.pdf) |
| [`2505.24100__01`](https://mlelarge.github.io/graph-conjectures/arxiv/2505.24100__01/) | Question 1.8 | *Halfway to induced saturation for even cycles* ([arXiv:2505.24100](https://arxiv.org/abs/2505.24100)) | proved | MINOR_GAPS | rewritten note | [2505.24100__01__induced-saturation-even-cycles-line-graphs-hypohamiltonian__note.pdf](2505.24100__01__induced-saturation-even-cycles-line-graphs-hypohamiltonian__note.pdf) |
