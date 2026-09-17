Attack the following open graph-theory problem.

Catalog id: partial_list_coloring_0
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/partial_list_coloring_0/
Original entry: http://www.openproblemgarden.org/op/partial_list_coloring_0
Problem attributed to: Iradmusa, Moharram (posted 2008-05-12)

=== Problem statement (OpenProblemGarden) ===
Title: Partial List Coloring
Let $ G $ be a simple graph, and for every list assignment $ \mathcal{L} $ let $ \lambda_{\mathcal{L}} $ be the maximum number of vertices of $ G $ which are colorable with respect to $ \mathcal{L} $ . Define $ \lambda_t = \min{ \lambda_{\mathcal{L}} } $ , where the minimum is taken over all list assignments $ \mathcal{L} $ with $ |\mathcal{L}| = t $ for all $ v \in V(G) $ . Conjecture [2] Let $ G $ be a graph with list chromatic number $ \chi_\ell $ and $ 1\leq r\leq s\leq \chi_\ell $ . Then \[\frac{\lambda_r}{r}\geq\frac{\lambda_s}{s}.\]

=== Discussion / context (OpenProblemGarden) ===
As you see this conjecture in the special case $ s=\chi_\ell $ , is the conjecture of Albertson, Grossman and Haas [1]: $ \lambda_t\geq\frac{tn}{\chi_\ell} $ for any $ 0\leq t\leq \chi_\ell $ .

=== References listed by OpenProblemGarden ===
- [1] M. Albertson, S. Grossman and R. Haas, Partial list colouring, Discrete Math., 214(2000), pp. 235-240.
- [2] Moharram N. Iradmusa, A Note on Partial List Colorings, Australasian Journal of Combinatorics, Vol.46, 2010, .

=== Catalog page (statement + literature review) ===
Partial List Coloring — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The Iradmusa conjecture that $\lambda_r/r \geq \lambda_s/s$ for $1 \leq r \leq s \leq \chi_\ell$ (which generalizes the Albertson–Grossman–Haas conjecture $\lambda_t \geq tn/\chi_\ell$) remains open in full generality. The special case $s = \chi_\ell$ has been verified for claw-free, chordless, and series-parallel graphs. The DP-coloring analogue of the partial list coloring conjecture does not hold in general.

 Cited literature (2)

 
 
 
partial Partial list colouring of certain graphs
 (2014)
 

 
 Jeannette Janssen, Rogers Mathew, Deepak Rajendraprasad · arXiv preprint · arXiv:1403.2587

Proves the Albertson–Grossman–Haas partial list coloring conjecture for claw-free graphs, chordless graphs, series-parallel graphs, and graphs with large chromatic number.
 

 
 
partial Partial DP-Coloring
 (2020)
 

 
 Hemanshu Kaul, Jeffrey A. Mudrock, Michael J. Pelsmajer · arXiv preprint · arXiv:2003.02687

Shows that the DP-coloring analogue of the partial list coloring conjecture does not hold, while extending several positive partial list coloring results to the DP-coloring setting.
 

 

 Reviewer notes. The Iradmusa conjecture (λ_r/r ≥ λ_s/s for all r ≤ s ≤ χ_ℓ) is strictly stronger than the AGH conjecture (the special case s = χ_ℓ). Most literature focuses on the weaker AGH special case; no papers directly addressing the more general Iradmusa ratio inequality were found. arXiv:2512.08020 concerns a different 'Albertson conjecture' about crossing numbers and is unrelated. The Kaul–Mudrock–Pelsmajer paper (2003.02687) was likely published in Discrete Mathematics but the journal DOI could not be verified (403 access). Chappell's 1998 bound (at least 6/7 of the conjectured vertices can be colored) predates the 2008 OPG posting and was not included in since_posted.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. [2] Let $ G $ be a graph with list chromatic number $ \chi_\ell $ and $ 1\leq r\leq s\leq \chi_\ell $ . Then \[\frac{\lambda_r}{r}\geq\frac{\lambda_s}{s}.\]

Keywords:
list assignment · list coloring

Discussion

As you see this conjecture in the special case $ s=\chi_\ell $ , is the conjecture of Albertson, Grossman and Haas [1]: $ \lambda_t\geq\frac{tn}{\chi_\ell} $ for any $ 0\leq t\leq \chi_\ell $ .

Bibliography

 [1]
 M. Albertson, S. Grossman and R. Haas, Partial list colouring , Discrete Math., 214 (2000), pp. 235-240.

 [2]
 Moharram N. Iradmusa, A Note on Partial List Colorings, Australasian Journal of Combinatorics , Vol.46, 2010, $ 19-24 $ .

Related conjectures

 
 implies
 Partial List Coloring
 partial
 Set s = χ_ℓ in Iradmusa's inequality λ_r/r ≥ λ_s/s. By definition of the list chromatic number, every list assignment with lists of size χ_ℓ colors all vertices, so λ_{χ_ℓ} = n. This yields λ_t ≥ tn/χ_ℓ for 1 ≤ t ≤ χ_ℓ (t = 0 is trivial), which is exactly the Albertson–Grossman–Haas conjecture. The source's OPG context states this specialization explicitly: 'this conjecture in the special case s=χ_ℓ, is the conjecture of Albertson, Grossman and Haas'. Direction is correct: the monotonicity conjecture is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
