Attack the following open graph-theory problem.

Catalog id: 1909.08426__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1909.08426__00/
Source paper: When Maximum Stable Set can be solved in FPT time (arXiv:1909.08426)

=== Extracted statement (catalog JSON) ===
Title: Classical MIS Dichotomy Conjecture
For every connected graph $H$, Maximum Independent Set in $H$-free graphs is in $\mathsf{P}$ if and only if $H \in \{P_\ell\}_{\ell} \cup \{S_{i,j,k}\}_{i \leq j \leq k}$.

Context:
The polynomial-time complexity of MIS in $H$-free graphs has been studied since the early 1980s. Alekseev showed that if $H$ is neither a path nor a subdivided claw then MIS is NP-complete on $H$-free graphs, motivating this conjecture about the full dichotomy. The authors note that an even stronger conjecture is postulated by Lozin [28].

=== Catalog page (statement + literature review) ===
MIS dichotomy for path- and claw-subdivision-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture that MIS in H-free graphs is in P if and only if H is a path or subdivided claw remains open at the polynomial-time level. The landmark post-2019 development is arXiv:2305.15738 (Gartland, Lokshtanov, Masařík, M. Pilipczuk, M. Pilipczuk, Rzążewski; STOC 2024), which proves MWIS is solvable in quasi-polynomial time for every H-free graph class where H is a path or subdivided claw, closing the gap between predicted-tractable cases and NP-hardness. Polynomial-time algorithms are established for specific subclasses (P_t-free for t ≤ 6, fork-free/S_{1,1,2}-free), but polynomial-time solvability for all S_{i,j,k}-free graphs remains open.

 Cited literature (1)

 
 
 
partial Maximum Weight Independent Set in Graphs with no Long Claws in Quasi-Polynomial Time
 (2023)
 

 
 Peter Gartland, Daniel Lokshtanov, Tomáš Masařík, Marcin Pilipczuk, Michał Pilipczuk, Paweł Rzążewski · Proceedings of the 56th Annual ACM Symposium on Theory of Computing (STOC 2024) · arXiv:2305.15738 · doi:10.1145/3618260.3649791

Proves that MWIS is solvable in quasi-polynomial time on H-free graphs whenever each connected component of H is a path or a subdivided claw, showing all conjectured-tractable cases are not NP-hard but stopping short of the conjectured polynomial-time bound.
 

 

 Reviewer notes. The quasi-polynomial result of arXiv:2305.15738 is the major post-2019 development: it shows all cases predicted tractable by the conjecture are at worst quasi-polynomial, confirming the NP-hard/tractable boundary but not yet establishing polynomial time for the full class S_{i,j,k}-free. No paper resolving the full polynomial-time dichotomy was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every connected graph $H$, Maximum Independent Set in $H$-free graphs is in $\mathsf{P}$ if and only if $H \in \{P_\ell\}_{\ell} \cup \{S_{i,j,k}\}_{i \leq j \leq k}$.

Context

The polynomial-time complexity of MIS in $H$-free graphs has been studied since the early 1980s. Alekseev showed that if $H$ is neither a path nor a subdivided claw then MIS is NP-complete on $H$-free graphs, motivating this conjecture about the full dichotomy. The authors note that an even stronger conjecture is postulated by Lozin [28].

Notes. PDF source — math may be garbled. $\{P_\ell\}_\ell$ denotes the family of paths and $\{S_{i,j,k}\}_{i \leq j \leq k}$ denotes the family of subdivided claws. Presented as a conjecture formalising a well-known open problem; no explicit citation in the header.

Source paper

 When Maximum Stable Set can be solved in FPT time
 Édouard Bonnet, Nicolas Bousquet, Stéphan Thomassé, Rémi Watrigant · 2019-09-18
 https://arxiv.org/abs/1909.08426
 PDF source

Related conjectures

 
 implies
 MIS complexity for S_{i,j,k}-free graphs with P₇
 partial
 The dichotomy conjecture's 'if' direction asserts MIS is in P on H-free graphs for every H that is a path P_l or a subdivided claw S_{i,j,k}. Every H in the target (an S_{i,j,k} containing P7, S_{1,1,3}, or S_{1,2,2}) belongs to that family by hypothesis, so truth of the conjecture answers the target completely: MIS is polynomial for all such H-free classes. The direction is correct — the source is the stronger, universally quantified statement; the target asks only about a boundary subfamily of spiders. This is a direct instantiation, no subtle parameter mismatch.
 

 
 implies
 Polynomial-time MIS on Pₜ-free graphs
 partial
 The dichotomy conjecture asserts MIS on H-free graphs is in P iff H is a path P_ell or a spider S_{i,j,k}. Its 'if' direction instantiated at H = P_t for each t >= 7 gives a polynomial-time algorithm for MIS on P_t-free graphs, which settles the target's 'determine whether' question affirmatively. Only the open 'if' direction of the source is used (the 'only if' half is Alekseev's known NP-completeness result), so truth of the source forces resolution of the target. Direction as claimed is correct.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:Maximum Independent Set (MIS for short) is in general graphs the paradigmatic $W[1]$-hard problem. In stark contrast, polynomial-time algorithms are known when the inputs are restricted to structured graph classes such as, for instance, perfect graphs (which includes bipartite graphs, chordal graphs, co-graphs, etc.) or claw-free graphs. In this paper, we introduce some variants of co-graphs with parameterized noise, that is, graphs that can be made into disjoint unions or complete sums by the removal of a certain number of vertices and the addition/deletion of a certain number of edges per incident vertex, both controlled by the parameter. We give a series of FPT Turing-reductions on these classes and use them to make some progress on the parameterized complexity of MIS in $H$-free graphs. We show that for every fixed $t \geqslant 1$, MIS is FPT in $P(1,t,t,t)$-free graphs, where $P(1,t,t,t)$ is the graph obtained by substituting all the vertices of a four-vertex path but one end of the path by cliques of size $t$. We also provide randomized FPT algorithms in dart-free graphs and in cricket-free graphs. This settles the FPT/W[1]-hard dichotomy for five-vertex graphs $H$.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Computational Complexity (cs.CC); Discrete Mathematics (cs.DM)
 
 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:1909.08426 [cs.DS]
 

 
  
 (or 
 arXiv:1909.08426v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1909.08426
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Wed, 18 Sep 2019 13:04:39 UTC (115 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled When Maximum Stable Set can be solved in FPT time, by \'Edouard Bonnet and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2019-09
 

 Change to browse by:
 
 cs
 cs.CC
 cs.DM
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Édouard Bonnet
Nicolas Bousquet
Stéphan Thomassé
Rémi Watrigant 

 

 export BibTeX citation
 Loading...

 
 
 BibTeX formatted citation

 ×
 

 
 loading...
 

 
 Data provided by: 
 
 

 

 Bookmark

 
 
 
 
 

 

 

 
 Bibliographic Tools
 
 Bibliographic and Citation Tools

 
 
 
 
 
 
 Bibliographic Explorer Toggle
 
 

 
 Bibliographic Explorer (What is the Explorer?)
 

 

 
 
 
 
 
 Connected Papers Toggle
 
 

 
 Connected Papers (What is Connected Papers?)
 

 

 
 
 
 
 Litmaps Toggle
 
 

 
 Litmaps (What is Litmaps?)
 

 

 
 
 
 
 
 scite.ai Toggle
 
 

 
 scite Smart Citations (What are Smart Citations?)
 

 

 

 

 

 

 

 

 
 Code, Data, Media
 
 Code, Data and Media Associated with this Article

 
 
 
 
 
 
 alphaXiv Toggle
 
 

 
 alphaXiv (What is alphaXiv?)
 

 

 
 
 
 
 
 Links to Code Toggle
 
 

 
 CatalyzeX Code Finder for Papers (What is CatalyzeX?)
 

 

 
 
 
 
 
 DagsHub Toggle
 
 

 
 DagsHub (What is DagsHub?)
 

 

 
 
 
 
 
 
 GotitPub Toggle
 
 

 
 Gotit.pub (What is GotitPub?)
 

 

 
 
 
 
 
 Huggingface Toggle
 
 

 
 Hugging Face (What is Huggingface?)
 

 

 
 
 
 
 
 ScienceCast Toggle
 
 

 
 ScienceCast (What is ScienceCast?)
 

 

 

 

 

 

 

 

 

 

 
 Demos
 
 Demos

 
 
 
 
 
 
 Replicate Toggle
 
 

 
 Replicate (What is Replicate?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 Hugging Face Spaces (What is Spaces?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 TXYZ.AI (What is TXYZ.AI?)
 

 

 

 

 

 

 

 
 Related Papers
 
 Recommenders and Search Tools

 
 
 
 
 
 
 Link to Influence Flower
 
 

 
 Influence Flower (What are Influence Flowers?)
 

 

 
 
 
 
 
 Core recommender toggle
 
 

 
 CORE Recommender (What is CORE?)
 

 

 

 
 
 Author

 Venue

 Institution

 Topic

 
 
 

 

 

 

 

 

 

 

 

 
 
 About arXivLabs
 
 
 
 
 arXivLabs: experimental projects with community collaborators

 arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

 Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

 Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

 

 
 

 

 

 

 

 
 Which authors of this paper are endorsers? |
 Disable MathJax (What is MathJax?)
