Attack the following open graph-theory problem.

Catalog id: 2003.05185__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2003.05185__01/
Source paper: Induced subgraphs of bounded treewidth and the container method (arXiv:2003.05185)

=== Extracted statement (catalog JSON) ===
Title: MWIS in P7-free graphs
Determine the computational complexity of the Maximum Weight Independent Set problem in $P_7$-free graphs.

Context:
Polynomial-time algorithms for MWIS in $P_5$-free graphs (2014) and $P_6$-free graphs (2019) were previously known. This paper extends tractability to the class $\mathcal{C}$ (which contains all $P_5$-free graphs), but the authors note that the case of $P_7$-free graphs remains open.

=== Catalog page (statement + literature review) ===
MWIS complexity in P₇-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The full complexity of Maximum Weight Independent Set in P7-free graphs remains open. Gartland and Lokshtanov (FOCS 2020) established a quasi-polynomial time algorithm running in n^{O(k^2 log^3 n)} for all Pk-free graphs (including P7-free), the first super-polynomial upper bound beyond NP-hardness evidence. More recently, Chudnovsky, Czyzewska, Kluk, Pilipczuk, and Rzazewski (ISAAC 2025) extended polynomial-time tractability to P7-free graphs of bounded clique number. The full polynomial-time resolution for all P7-free graphs remains open as of 2026.

 Cited literature (2)

 
 
 
partial Independent Set on P_k-Free Graphs in Quasi-Polynomial Time
 (2020)
 

 
 Peter Gartland, Daniel Lokshtanov · FOCS 2020 · arXiv:2005.00690

Gives a quasi-polynomial time algorithm (n^{O(k^2 log^3 n)}) for Maximum Weight Independent Set on Pk-free graphs for any fixed k, directly applying to P7-free graphs but not achieving polynomial time.
 

 
 
partial Sparse Induced Subgraphs in P_7-Free Graphs of Bounded Clique Number
 (2025)
 

 
 Maria Chudnovsky, Jadwiga Czyzewska, Kacper Kluk, Marcin Pilipczuk, Pawel Rzazewski · ISAAC 2025 · doi:10.4230/LIPIcs.ISAAC.2025.20

Extends polynomial-time tractability of MWIS and related sparse induced subgraph problems to P7-free graphs of bounded clique number, but the general P7-free case remains open.
 

 

 Reviewer notes. General P7-free case still open (no polynomial-time algorithm known). Two verified partial advances since posting: quasi-polynomial time for all Pk-free graphs (Gartland-Lokshtanov, FOCS 2020, arXiv:2005.00690) and polynomial time for P7-free graphs restricted to bounded clique number (Chudnovsky et al., ISAAC 2025, LIPIcs). A polynomial-time algorithm for P6-free graphs was also achieved circa SODA 2024, but that is for a smaller graph class and was not directly verified here.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine the computational complexity of the Maximum Weight Independent Set problem in $P_7$-free graphs.

Context

Polynomial-time algorithms for MWIS in $P_5$-free graphs (2014) and $P_6$-free graphs (2019) were previously known. This paper extends tractability to the class $\mathcal{C}$ (which contains all $P_5$-free graphs), but the authors note that the case of $P_7$-free graphs remains open.

Notes. Stated in passing prose: 'the case of P7-free graphs remains open.' No labelled theorem environment.

Source paper

 Induced subgraphs of bounded treewidth and the container method
 Tara Abrishami, Maria Chudnovsky, Marcin Pilipczuk, Paweł Rzążewski, Paul Seymour · 2020-03-11
 https://arxiv.org/abs/2003.05185
 PDF source

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
