Attack the following open graph-theory problem.

Catalog id: frankls_union_closed_sets_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Hypergraphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/frankls_union_closed_sets_conjecture/
Original entry: http://www.openproblemgarden.org/op/frankls_union_closed_sets_conjecture
Problem attributed to: Frankl, Peter (posted 2008-09-25)

=== Problem statement (OpenProblemGarden) ===
Title: Frankl's union-closed sets conjecture
Conjecture Let $ F $ be a finite family of finite sets, not all empty, that is closed under taking unions. Then there exists $ x $ such that $ x $ is an element of at least half the members of $ F $ .

=== Discussion / context (OpenProblemGarden) ===
This conjecture is notoriously difficult, even though (or should we say `because'?) it involves almost no mathematical structure whatsoever. It was posed by Frankl in the late 1970's. The recent paper of Morris [M] provides a good illustration of the kind of partial results known: Morris extends earlier work to show that the conjecture holds for families containing three 3-subsets of a 5-set, four 3-subsets of a 6-set, or eight 4-subsets of a 6-set. In a different direction, Czédli [C] has proved the conjecture in the case when $ |F| \ge 2^n - 2^{n/2} $ where $ n = |\bigcup F| \ge 3 $ .

=== References listed by OpenProblemGarden ===
- [C] G. Czédli, On averaging Frankl's conjecture for large union-closed-sets, J. Combin. Theory Ser. A, to appear.
- [M] R. Morris, FC-families and improved bounds for Frankl's conjecture, European J. Combin. 27 (2006), no. 2, 269–282.
- [P] B. Poonen, Union-closed families, J. Combin. Theory Ser. A 59 (1992), no. 2, 253–268.
- [V] T. P. Vaughan, Three-sets in a union-closed family, J. Combin. Math. Combin. Comput. 49 (2004), 73–84.
- [W] P. Wójcik, Union-closed families of sets, Discrete Math. 199 (1999), no. 1–3, 173–182.

=== Catalog page (statement + literature review) ===
Frankl's union-closed sets conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Frankl's union-closed conjecture remains open, but the period 2022–2023 brought a landmark breakthrough: Gilmer established the first constant lower bound (≥ 0.01) using an entropy method, and within days Alweiss–Huang–Sellke and Sawin independently improved this to $(3-\sqrt{5})/2 \approx 0.382$. Further refinements by Cambie and Liu raised the bound to approximately $0.38271$, but the conjectured threshold of $1/2$ has not been reached.

 Cited literature (6)

 
 
 
partial A constant lower bound for the union-closed sets conjecture
 (2022)
 

 
 Justin Gilmer · arXiv preprint · arXiv:2211.09055

Establishes the first constant lower bound for the union-closed conjecture, proving that some element appears in at least 0.01 fraction of the sets, via an information-theoretic entropy argument.
 

 
 
partial Improved Lower Bound for Frankl's Union-Closed Sets Conjecture
 (2024)
 

 
 Ryan Alweiss, Brice Huang, Mark Sellke · Electronic Journal of Combinatorics · arXiv:2211.11731

Proves that some element appears in at least $(3-\sqrt{5})/2 \approx 0.382$ fraction of the sets by verifying an explicit inequality conjectured by Gilmer.
 

 
 
partial An improved lower bound for the union-closed set conjecture
 (2022)
 

 
 Will Sawin · arXiv preprint · arXiv:2211.11504

Independently proves the lower bound $(3-\sqrt{5})/2 \approx 0.382$ using a different coupling approach, and outlines a strategy for further improvement.
 

 
 
partial Better bounds for the union-closed sets conjecture using the entropy approach
 (2022)
 

 
 Stijn Cambie · arXiv preprint · arXiv:2212.12500

Uses dependent samples (as suggested by Sawin) within the entropy framework to obtain bounds slightly exceeding $(3-\sqrt{5})/2$, and identifies limitations of the entropy method.
 

 
 
partial Improving the Lower Bound for the Union-closed Sets Conjecture via Conditionally IID Coupling
 (2023)
 

 
 Jingbo Liu · arXiv preprint · arXiv:2306.08824

Further improves the lower bound to approximately $0.38271$ by introducing a conditionally i.i.d. coupling technique beyond the convex-combination approach of Sawin.
 

 
 
survey Progress on the union-closed conjecture and offsprings in winter 2022-2023
 (2023)
 

 
 Stijn Cambie · arXiv preprint · arXiv:2306.12351

Surveys the Gilmer breakthrough and all subsequent improvements to the union-closed conjecture from winter 2022–2023, including extensions, limitations, and related open questions.
 

 

 Reviewer notes. The conjecture saw its most dramatic progress in November 2022 with Gilmer's entropy breakthrough. The bound (3-√5)/2 was achieved simultaneously by Alweiss–Huang–Sellke and Sawin (and independently by Chase–Lovett, whose paper arXiv:2211.11504 was attributed to Sawin when fetched — Chase–Lovett may be a separate paper I could not separately confirm). The Lu–Raz 2024 paper (arXiv:2405.10639) addresses a related question about Reimer's theorem and constructs counterexamples to a natural auxiliary conjecture, but does not improve the main bound. Wikipedia also credits Vuckovic–Zivkovic (2017) for verifying the conjecture for families whose union has ≤ 12 elements, but this paper was not separately fetched and verified. The conjecture is definitively still open; the gap between ~0.38271 and 0.5 is significant and the entropy method appears to have fundamental limitations below 0.5.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 161s.
 

Conjecture. Let $ F $ be a finite family of finite sets, not all empty, that is closed under taking unions. Then there exists $ x $ such that $ x $ is an element of at least half the members of $ F $ .

Discussion

This conjecture is notoriously difficult, even though (or should we say `because'?) it involves almost no mathematical structure whatsoever. It was posed by Frankl in the late 1970's. The recent paper of Morris [M] provides a good illustration of the kind of partial results known: Morris extends earlier work to show that the conjecture holds for families containing three 3-subsets of a 5-set, four 3-subsets of a 6-set, or eight 4-subsets of a 6-set. In a different direction, Czédli [C] has proved the conjecture in the case when $ |F| \ge 2^n - 2^{n/2} $ where $ n = |\bigcup F| \ge 3 $ .

Bibliography

 [C]
 G. Czédli, On averaging Frankl's conjecture for large union-closed-sets, J. Combin. Theory Ser. A, to appear.

 [M]
 R. Morris, FC-families and improved bounds for Frankl's conjecture, European J. Combin. 27 (2006), no. 2, 269–282.

 [P]
 B. Poonen, Union-closed families, J. Combin. Theory Ser. A 59 (1992), no. 2, 253–268.

 [V]
 T. P. Vaughan, Three-sets in a union-closed family, J. Combin. Math. Combin. Comput. 49 (2004), 73–84.

 [W]
 P. Wójcik, Union-closed families of sets, Discrete Math. 199 (1999), no. 1–3, 173–182.
