Attack the following open graph-theory problem.

Catalog id: partial_list_coloring
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/partial_list_coloring/
Original entry: http://www.openproblemgarden.org/op/partial_list_coloring
Problem attributed to: Albertson, Michael O., Grossman, Sara, Haas, Ruth (posted 2008-05-05)

=== Problem statement (OpenProblemGarden) ===
Title: Partial List Coloring
Conjecture Let $ G $ be a simple graph with $ n $ vertices and list chromatic number $ \chi_\ell(G) $ . Suppose that $ 0\leq t\leq \chi_\ell $ and each vertex of $ G $ is assigned a list of $ t $ colors. Then at least $ \frac{tn}{\chi_\ell(G)} $ vertices of $ G $ can be colored from these lists.

=== Discussion / context (OpenProblemGarden) ===
Albertson, Grossman, and Haas introduce this interesting question in [AGH], and prove some partial results. For instance, they show that under the above assumptions, at least $ (1 - (\frac{ \chi(G) - 1}{\chi(G)} )^t) \cdot n $ vertices of $ G $ can be colored from the lists.

=== References listed by OpenProblemGarden ===
- *[AGH] M. Albertson, S. Grossman and R. Haas, Partial list colouring, Discrete Math., 214(2000), pp. 235-240.

=== Catalog page (statement + literature review) ===
Partial List Coloring — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Partial List Coloring Conjecture of Albertson, Grossman, and Haas remains open for general graphs. Post-2008 progress includes a proof of the conjecture for claw-free graphs, chordless graphs, series-parallel graphs, and graphs with chromatic number at least $(|V(G)|-1)/2$. The DP-coloring analogue of the conjecture has been shown to fail, indicating the conjecture does not follow from a more general principle.

 Cited literature (2)

 
 
 
partial Partial List Colouring of Certain Graphs
 (2015)
 

 
 Jeannette Janssen, Rogers Mathew, Deepak Rajendraprasad · Electronic Journal of Combinatorics · arXiv:1403.2587 · doi:10.37236/4283

Proves the conjecture for claw-free graphs, chordless graphs, series-parallel graphs, and graphs with chromatic number at least $(|V(G)|-1)/2$; also constructs an infinite family of 3-choosable graphs showing a related variant fails.
 

 
 
partial Partial DP-Coloring
 (2020)
 

 
 Hemanshu Kaul, Jeffrey A. Mudrock, Michael J. Pelsmajer · arXiv preprint · arXiv:2003.02687

Initiates the study of partial DP-coloring; shows the DP-coloring analogue of the Partial List Coloring Conjecture does not hold, while several partial list coloring results do extend to the DP-coloring setting.
 

 

 Reviewer notes. The Chappell (1998) lower bound (arXiv:math/9805066) showing at least 6/7 of the conjectured number can be colored predates the OPG posting and is not included in since_posted. The Kaul et al. paper likely appeared in Discrete Mathematics in 2021 (ScienceDirect PII S0012365X21000194) but that page returned HTTP 403 and could not be verified directly; arXiv URL is cited instead. No post-2015 paper verifiably proving further new cases of the original conjecture was found. The conjecture is also known to hold for bipartite graphs (follows from t ≤ ch(G) − χ(G) + 1) and when t divides ch(G), though these results appear in the original or earlier literature.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. Let $ G $ be a simple graph with $ n $ vertices and list chromatic number $ \chi_\ell(G) $ . Suppose that $ 0\leq t\leq \chi_\ell $ and each vertex of $ G $ is assigned a list of $ t $ colors. Then at least $ \frac{tn}{\chi_\ell(G)} $ vertices of $ G $ can be colored from these lists.

Keywords:
list assignment · list coloring

Discussion

Albertson, Grossman, and Haas introduce this interesting question in [AGH], and prove some partial results. For instance, they show that under the above assumptions, at least $ (1 - (\frac{ \chi(G) - 1}{\chi(G)} )^t) \cdot n $ vertices of $ G $ can be colored from the lists.

Bibliography

★ [AGH]
 M. Albertson, S. Grossman and R. Haas, Partial list colouring , Discrete Math., 214 (2000), pp. 235-240.
 Partial list colouring

Related conjectures

 
 implied by
 Partial List Coloring
 partial
 Set s = χ_ℓ in Iradmusa's inequality λ_r/r ≥ λ_s/s. By definition of the list chromatic number, every list assignment with lists of size χ_ℓ colors all vertices, so λ_{χ_ℓ} = n. This yields λ_t ≥ tn/χ_ℓ for 1 ≤ t ≤ χ_ℓ (t = 0 is trivial), which is exactly the Albertson–Grossman–Haas conjecture. The source's OPG context states this specialization explicitly: 'this conjecture in the special case s=χ_ℓ, is the conjecture of Albertson, Grossman and Haas'. Direction is correct: the monotonicity conjecture is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
