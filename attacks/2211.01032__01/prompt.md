Attack the following open graph-theory problem.

Catalog id: 2211.01032__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2211.01032__01/
Source paper: Random Embeddings of Graphs: The Expected Number of Faces in Most Graph… (arXiv:2211.01032)

=== Catalog page (statement + literature review) ===
Expected faces logarithmic for all G(n,p) — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 9.1 from arXiv:2211.01032 asserts that for any density function p(n), almost all graphs in G(n,p) have E[F] = O(log n). The paper itself proves this for dense graphs (p >= 1/polylog n, Corollary 7.3, polylogarithmic bound) and for sparse random graphs (Section 8, logarithmic bound), leaving the general case open. The conjecture would follow from the stronger Conjecture 1.13. No subsequent work resolving the full conjecture was found in the literature.

 Reviewer notes. No follow-up paper resolving Conjecture 9.1 was found. The paper's latest revision (v3, April 2025) still lists the conjecture as open. Conjecture 9.1 is a consequence of the stronger Conjecture 1.13 (also open), which predicts E[F] = (1+o(1)) ln(pn^2) for G(n,p).

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any $p(n) : \mathbb{N} \rightarrow [0,1]$, almost all graphs in $G(n,p)$ satisfy $\mathbb{E}[F] = O(\log(n))$.

Context

Corollary 7.3 establishes a polylogarithmic bound for almost all dense graphs (when $p \geq 1/\mathrm{polylog}\, n$), and Section 8 gives a logarithmic bound for random sparse graphs. The authors conjecture that the logarithmic property holds without any density condition on edges. This conjecture would follow from the stronger Conjecture 1.13.

Source paper

 Random Embeddings of Graphs: The Expected Number of Faces in Most Graphs is Logarithmic
 Jesse Campion Loth, Kevin Halasz, Tomáš Masařík, Bojan Mohar, Robert Šámal · 2025-04-09
 https://arxiv.org/abs/2211.01032

=== Source paper abstract / header ===
Abstract:A random 2-cell embedding of a connected graph $G$ in some orientable surface is obtained by choosing a random local rotation around each vertex. Under this setup, the number of faces or the genus of the corresponding 2-cell embedding becomes a random variable. Random embeddings of two particular graph classes, those of a bouquet of $n$ loops and those of $n$ parallel edges connecting two vertices, have been extensively studied and are well-understood. However, little is known about more general graphs. The results of this paper explain why Monte Carlo methods cannot work for approximating the minimum genus of graphs.
In his breakthrough work [Permutation-partition pairs, JCTB 1991], Stahl developed the foundation of "random topological graph theory". Most of his results have been unsurpassed until today. In our work, we analyze the expected number of faces of random embeddings (equivalently, the average genus) of a graph $G$. It was very recently shown that for any graph $G$, the expected number of faces is at most linear. We show that the actual expected number of faces $F(G)$ is almost always much smaller. In particular, we prove:
1) $\frac{1}{2}\ln n - 2 < \mathbb{E}[F(K_n)] \le 3.65 \ln n +o(1)$.
2) For random graphs $G(n,p)$ ($p=p(n)$), we have $\mathbb{E}[F(G(n,p))] \le \ln^2 n+\frac{1}{p}$.
3) For random models $B(n,\Delta)$ containing only graphs, whose maximum degree is at most $\Delta$, we obtain stronger bounds by showing that the expected number of faces is $\Theta(\log n)$.
 

 
 
 
 Comments:
 Accepted at the 35th ACM-SIAM Symposium on Discrete Algorithms (SODA 2024). The submission also contains sources and data of the computation described in the paper. 55 pages, 11 figures
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C10
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:2211.01032 [math.CO]
 

 
  
 (or 
 arXiv:2211.01032v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2211.01032
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Proceedings: ACM-SIAM Symposium on Discrete Algorithms, SODA 2024
 

 
 
 Related DOI:
 
 https://doi.org/10.1137/1.9781611977912.46

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tomáš Masařík [view email] 
 [v1]
 Wed, 2 Nov 2022 10:58:31 UTC (500 KB)

 [v2]
 Thu, 28 Dec 2023 22:21:48 UTC (708 KB)

 [v3]
 Wed, 9 Apr 2025 18:37:40 UTC (1,123 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Random Embeddings of Graphs: The Expected Number of Faces in Most Graphs is Logarithmic, by Jesse Campion Loth and 4 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 math.CO

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2022-11
 

 Change to browse by:
 
 cs
 cs.DM
 math
 

 

 

 
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
