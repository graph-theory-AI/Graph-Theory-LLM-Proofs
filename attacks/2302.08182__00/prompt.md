Attack the following open graph-theory problem.

Catalog id: 2302.08182__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2302.08182__00/
Source paper: Maximum Independent Set when excluding an induced minor: $K_1 + tK_2$ a… (arXiv:2302.08182)

=== Extracted statement (catalog JSON) ===
Title: Question 2
Is it true that for every planar graph $H$, Max Independent Set can be solved in quasipolynomial time in the class of graphs excluding $H$ as an induced minor?

Context:
Question 2 is the quasipolynomial-time relaxation of Question 1, for which substantially more positive evidence exists: quasipolynomial-time algorithms are known for $C_t$-induced-minor-free graphs and for $tC_3$-induced-minor-free graphs. The present paper contributes a quasipolynomial-time algorithm for $tC_3 \uplus C_4$-induced-minor-free graphs, running in $n^{O(t^{2}\log n)+f(t)}$.

=== Catalog page (statement + literature review) ===
MIS quasipolynomial time for planar induced-minor-free — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 What is the smallest number of disjoint spanning trees made a graph Hamiltonian
 (fuzzy-match score 100, not yet manually confirmed).

 
 Status
 open
 high confidence
 

 Question 2 — whether Max Independent Set is solvable in quasipolynomial time for every planar-H-induced-minor-free graph class — remains open. The source paper itself adds the $tC_3 \uplus C_4$ case to the growing list of positive instances (already including $C_t$- and $tC_3$-free cases). A February 2026 paper (arXiv:2602.18317) extends the family further to $sC_t$-induced-minor-free graphs but only achieves a QPTAS (approximation scheme), not an exact quasipolynomial-time algorithm, so the conjecture for all planar $H$ is unresolved.

 Cited literature (1)

 
 
 
partial QPTAS for MWIS and finding large sparse induced subgraphs in graphs with few independent long holes
 (2026)
 

 
 unknown (arXiv:2602.18317) · arXiv preprint · arXiv:2602.18317

Proves a quasipolynomial-time approximation scheme (QPTAS) for MWIS in graphs excluding $sC_t$ as an induced minor, generalising the $C_4 \uplus sC_3$ case, but achieves only approximate (not exact) computation and does not cover all planar $H$.
 

 

 Reviewer notes. No paper found that resolves Question 2 for all planar $H$. The Gartland–Lokshtanov conjecture (polynomial-time for all planar-H-induced-minor-free classes) is described in arXiv:2602.18317 as 'notoriously open', which subsumes Question 2. Progress is incremental: new planar forbidden graphs are handled one family at a time.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. Is it true that for every planar graph $H$, Max Independent Set can be solved in quasipolynomial time in the class of graphs excluding $H$ as an induced minor?

Context

Question 2 is the quasipolynomial-time relaxation of Question 1, for which substantially more positive evidence exists: quasipolynomial-time algorithms are known for $C_t$-induced-minor-free graphs and for $tC_3$-induced-minor-free graphs. The present paper contributes a quasipolynomial-time algorithm for $tC_3 \uplus C_4$-induced-minor-free graphs, running in $n^{O(t^{2}\log n)+f(t)}$.

Notes. No parenthetical attribution appears in the theorem header; treated as the paper authors' own question. It is the natural quasipolynomial companion to Question 1.

Source paper

 Maximum Independent Set when excluding an induced minor: $K_1 + tK_2$ and $tC_3 \uplus C_4$
 Édouard Bonnet, Julien Duron, Colin Geniet, Stéphan Thomassé, Alexandra Wesolek · 2025-12-31
 https://arxiv.org/abs/2302.08182

=== Source paper abstract / header ===
Abstract:Dallard, Milanič, and Štorgel [arXiv '22] ask if for every class excluding a fixed planar graph $H$ as an induced minor, Maximum Independent Set can be solved in polynomial time, and show that this is indeed the case when $H$ is any planar complete bipartite graph, or the 5-vertex clique minus one edge, or minus two disjoint edges. A positive answer would constitute a far-reaching generalization of the state-of-the-art, when we currently do not know if a polynomial-time algorithm exists when $H$ is the 7-vertex path. Relaxing tractability to the existence of a quasipolynomial-time algorithm, we know substantially more. Indeed, quasipolynomial-time algorithms were recently obtained for the $t$-vertex cycle, $C_t$ [Gartland et al., STOC '21] and the disjoint union of $t$ triangles, $tC_3$ [Bonamy et al., SODA '23].
We give, for every integer $t$, a polynomial-time algorithm running in $n^{O(t^5)}$ when $H$ is the friendship graph $K_1 + tK_2$ ($t$ disjoint edges plus a vertex fully adjacent to them), and a quasipolynomial-time algorithm running in $n^{O(t^2 \log n)+f(t)}$, with $f$ a single-exponential function, when $H$ is $tC_3 \uplus C_4$ (the disjoint union of $t$ triangles and a 4-vertex cycle). The former extends a classical result on graphs excluding $tK_2$ as an induced subgraph [Alekseev, DAM '07], while the latter extends Bonamy et al.'s result.
 

 
 
 
 Comments:
 16 pages, 2 figures
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C85
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2302.08182 [cs.DS]
 

 
  
 (or 
 arXiv:2302.08182v2 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2302.08182
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 
 Related DOI:
 
 https://doi.org/10.1007/s00453-025-01356-2

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Thu, 16 Feb 2023 10:09:30 UTC (110 KB)

 [v2]
 Wed, 31 Dec 2025 14:09:20 UTC (113 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Maximum Independent Set when excluding an induced minor: $K_1 + tK_2$ and $tC_3 \uplus C_4$, by \'Edouard Bonnet and 4 other authors
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
 | 2023-02
 

 Change to browse by:
 
 cs
 cs.DM
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

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
