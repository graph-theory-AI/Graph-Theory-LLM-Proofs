Attack the following open graph-theory problem.

Catalog id: 2003.05185__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2003.05185__00/
Source paper: Induced subgraphs of bounded treewidth and the container method (arXiv:2003.05185)

=== Extracted statement (catalog JSON) ===
Title: Combinatorial polynomial-time algorithm for MWIS in perfect graphs
Design a combinatorial polynomial-time algorithm for the Maximum Weight Independent Set problem in perfect graphs.

Context:
The polynomial-time algorithm of Grötschel, Lovász, and Schrijver for MWIS in perfect graphs relies on the ellipsoid method. The authors explicitly note that designing a combinatorial polynomial-time algorithm for this problem remains an important open problem.

=== Catalog page (statement + literature review) ===
Combinatorial MWIS algorithm for perfect graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The problem of designing a combinatorial polynomial-time algorithm for MWIS in perfect graphs (bypassing the ellipsoid-method-based algorithm of Grötschel, Lovász, and Schrijver) remains open in full generality. A verified partial result was published in 2024: Abrishami, Chudnovsky, Dibek, and Vušković give a combinatorial polynomial-time algorithm for perfect graphs of bounded degree that exclude a prism or a hole of length four as an induced subgraph, using even-set balanced separators and submodular function minimization. No paper resolving the full problem for all perfect graphs was found.

 Cited literature (1)

 
 
 
partial Submodular Functions and Perfect Graphs
 (2024)
 

 
 Tara Abrishami, Maria Chudnovsky, Cemil Dibek, Kristina Vušković · Mathematics of Operations Research · arXiv:2110.00108 · doi:10.1287/moor.2021.0302

Gives a combinatorial polynomial-time algorithm for MWIS in perfect graphs of bounded degree that do not contain a prism or a hole of length four as an induced subgraph, by showing such graphs admit a balanced separator that is a union of boundedly many even sets.
 

 

 Reviewer notes. The full problem for all perfect graphs is open; the partial result (arXiv:2110.00108) handles only the bounded-degree prism-free C4-free case. The approach reduces to submodular function minimization, which the authors classify as combinatorial. No resolution of the general case was found in indexed literature up to May 2026.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Design a combinatorial polynomial-time algorithm for the Maximum Weight Independent Set problem in perfect graphs.

Context

The polynomial-time algorithm of Grötschel, Lovász, and Schrijver for MWIS in perfect graphs relies on the ellipsoid method. The authors explicitly note that designing a combinatorial polynomial-time algorithm for this problem remains an important open problem.

Notes. Stated in prose without a labelled environment: 'Designing a combinatorial polynomial-time algorithm for MWIS in perfect graphs remains an important open problem.' A classical community-wide open problem acknowledged by the authors as ongoing context.

Source paper

 Induced subgraphs of bounded treewidth and the container method
 Tara Abrishami, Maria Chudnovsky, Marcin Pilipczuk, Paweł Rzążewski, Paul Seymour · 2020-03-11
 https://arxiv.org/abs/2003.05185
 PDF source

Related conjectures

 
 same conjecture as
 Combinatorial MIS algorithm for perfect graphs
 partial
 The target's problem (combinatorial polynomial-time algorithm for MWIS in perfect graphs) appears verbatim in the source's list ('no combinatorial polynomial-time algorithm is known for any of MIS, MWIS, MC, and MWC in perfect graphs; finding one is a major open problem'). Both attribute the only known polynomial algorithm to the Grotschel-Lovasz-Schrijver ellipsoid method and ask for a combinatorial replacement. The extra variants in the source are equivalent forms (perfect graphs are closed under complementation, so MC/MWC reduce to MIS/MWIS in the complement), and the C_4-free remark is a subcase, not a different problem. Same classical open problem, with the source a slightly broader record of it.
 

 
 same conjecture as
 Combinatorial MIS algorithm on perfect graphs
 open
 Both are the standard folklore open problem stemming from Grötschel–Lovász–Schrijver: their ellipsoid-based polynomial algorithm for (weighted) stable set in perfect graphs is the only known one, and finding a combinatorial polynomial-time algorithm is open; both contexts cite exactly this. The only nuance is weighted (2003.05185, MWIS) vs unweighted (1907.01083, MIS): strictly a combinatorial MWIS algorithm implies a combinatorial MIS one, and for polynomially bounded integer weights the converse follows by substituting each vertex by a stable set of w_v copies (substitution preserves perfection), though arbitrary weights need scaling. In the literature these are treated as one and the same open problem, which is how both papers state it, so same_conjecture is the right classification.
 

 
 implies
 Combinatorial MIS algorithm on perfect graphs
 open
 Maximum Independent Set is the special case of Maximum Weight Independent Set with all weights equal to 1, on the same graph class (perfect graphs). Specializing weights to 1 preserves both polynomial running time and the combinatorial (non-ellipsoid) character of an algorithm, so a combinatorial polynomial-time MWIS algorithm for perfect graphs is in particular a combinatorial polynomial-time (hence also FPT) MIS algorithm for perfect graphs, answering the target. The converse specialization is not automatic (weighted is a priori harder), so 'implies' rather than 'equivalent_to' is the right relation, in the claimed direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:A hole in a graph is an induced cycle of length at least 4. A hole is long if its length is at least 5. By $P_t$ we denote a path on $t$ vertices. In this paper we give polynomial-time algorithms for the following problems: the Maximum Weight Independent Set problem in long-hole-free graphs, and the Feedback Vertex Set problem in $P_5$-free graphs. Each of the above results resolves a corresponding long-standing open problem.
An extended $C_5$ is a five-vertex hole with an additional vertex adjacent to one or two consecutive vertices of the hole. Let $\mathcal{C}$ be the class of graphs excluding an extended $C_5$ and holes of length at least $6$ as induced subgraphs; $\mathcal{C}$ contains all long-hole-free graphs and all $P_5$-free graphs. We show that, given an $n$-vertex graph $G \in \mathcal{C}$ with vertex weights and an integer $k$, one can in time $n^{\Oh(k)}$ find a maximum-weight induced subgraph of $G$ of treewidth less than $k$. This implies both aforementioned results.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2003.05185 [cs.DS]
 

 
  
 (or 
 arXiv:2003.05185v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2003.05185
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Marcin Pilipczuk [view email] 
 [v1]
 Wed, 11 Mar 2020 09:30:40 UTC (437 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Induced subgraphs of bounded treewidth and the container method, by Tara Abrishami and Maria Chudnovsky and Marcin Pilipczuk and Pawe{\l} Rz\k{a}\.zewski and Paul Seymour
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
 | 2020-03
 

 Change to browse by:
 
 cs
 cs.DM
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Maria Chudnovsky
Marcin Pilipczuk
Pawel Rzazewski
Paul D. Seymour 

 

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
