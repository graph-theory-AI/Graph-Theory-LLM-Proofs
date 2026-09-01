Attack the following open graph-theory problem.

Catalog id: 2509.07174__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2509.07174__00/
Source paper: Asymptotic structure. VI. Distant paths across a disc (arXiv:2509.07174)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.2 (Coarse Menger conjecture for surfaces)
Let $\mathcal{S}$ be a fixed surface. For all integers $k,c\geq 0$ there exists $\ell>0$ with the following property. Let $G$ be a graph that embeds on $\mathcal{S}$ and let $S,T\subseteq V(G)$. Then either

$\bullet$ there are $k+1$ paths between $S,T$, pairwise $c$-distant; or

$\bullet$ there is a set $X\subseteq V(G)$ with $|X|\leq k$ such that every path between $S,T$ contains a vertex with distance at most $\ell$ from some member of $X$.

Context:
The original Coarse Menger conjecture (attributed to Albrechtsen, Huynh, Jacobs, Knappe and Wollan, and independently to Georgakopoulos and Papasoglu) was shown to be false for general graphs by the same authors (Nguyen–Scott–Seymour) in [11], with counterexamples that are highly non-planar (unbounded genus). Since the counterexamples rely on non-planarity, the authors propose that a surface-restricted version may still hold.

=== Catalog page (statement + literature review) ===
Coarse Menger for surface-embedded graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 1.2 (the strong Coarse Menger conjecture for surfaces) remains open but has partial progress. Blažej, Pilipczuk, and Protopapas (arXiv:2605.11112, 2026) prove the weak form for graphs embeddable on any fixed surface: if fewer than k pairwise d-apart S-T paths exist, then there is a vertex set X with |X| ≤ f(k,d) such that every S-T path is within distance d of some vertex of X. This weak form allows |X| to grow with d, whereas Conjecture 1.2 requires the stronger bound |X| ≤ k independent of the distance parameter; the full conjecture remains open.

 Cited literature (1)

 
 
 
partial A coarse Menger's Theorem for planar and bounded genus graphs
 (2026)
 

 
 Václav Blažej, Michał Pilipczuk, Evangelos Protopapas · arXiv preprint · arXiv:2605.11112

Proves the weak Coarse Menger conjecture for graphs embeddable on any fixed surface (Theorem 1.1): if fewer than k pairwise d-apart S-T paths exist, then there is a vertex set X with |X| ≤ f(k,d) such that every S-T path lies within distance d of X; the stronger bound |X| ≤ k required by Conjecture 1.2 is not established.
 

 

 Reviewer notes. The weak Coarse Menger conjecture for surfaces is settled by arXiv:2605.11112 (2026), which cites Nguyen–Scott–Seymour's counterexample paper (part IV) but not part VI (2509.07174), likely because 2605.11112 was largely written before part VI appeared. The strong form of Conjecture 1.2 (∣X∣ ≤ k with ℓ depending only on k and c) remains open. The internal reference 2412.13893 is a fuzz-match false positive.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $\mathcal{S}$ be a fixed surface. For all integers $k,c\geq 0$ there exists $\ell>0$ with the following property. Let $G$ be a graph that embeds on $\mathcal{S}$ and let $S,T\subseteq V(G)$. Then either

$\bullet$ there are $k+1$ paths between $S,T$, pairwise $c$-distant; or

$\bullet$ there is a set $X\subseteq V(G)$ with $|X|\leq k$ such that every path between $S,T$ contains a vertex with distance at most $\ell$ from some member of $X$.

Context

The original Coarse Menger conjecture (attributed to Albrechtsen, Huynh, Jacobs, Knappe and Wollan, and independently to Georgakopoulos and Papasoglu) was shown to be false for general graphs by the same authors (Nguyen–Scott–Seymour) in [11], with counterexamples that are highly non-planar (unbounded genus). Since the counterexamples rely on non-planarity, the authors propose that a surface-restricted version may still hold.

Notes. The paper proves a special case (Theorem 1.3): the conjecture holds when $G$ is planar and all vertices of $S\cup T$ lie on the infinite region, with the blocking structure being at most $k$ connected subgraphs whose diameters sum to at most $200k^3c$.

Source paper

 Asymptotic structure. VI. Distant paths across a disc
 Tung Nguyen, Alex Scott, Paul Seymour · 2025-09-08
 https://arxiv.org/abs/2509.07174

=== Source paper abstract / header ===
Abstract:Menger's theorem says that, for $k\ge0$, if $S, T$ are sets of vertices in a graph $G$, then either there are $k + 1$ vertex-disjoint paths between $S$ and $T$, or there is a set X of at most $k$ vertices such that every $S$-$T$ path passes through $X$. The ``coarse Menger conjecture'' proposed a generalization of Menger's theorem for paths that are far apart: for all $k, c$ there exists $\ell$, such that for every graph $G$ and subsets $S, T \subset V (G)$, either there are $k + 1$ paths between $S$ and $T$, pairwise with distance more than $c$, or there is a set $X \subset V (G)$ of at most $k$ vertices such that every $S$-$T$ path has distance at most $\ell$ from $X$. This is known to be false, but may be true if $G$ is planar. Here we show that it is true if $G$ is planar and all vertices in $S \cup T$ are on the infinite region. In this case, we also obtain a linear-time algorithm to test for the existence of $k+ 1$ paths between $S$ and $T$, pairwise with distance more than $c$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C10, 05C12, 05C40
 

 Cite as:
 arXiv:2509.07174 [math.CO]
 

 
  
 (or 
 arXiv:2509.07174v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2509.07174
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Tung H. Nguyen [view email] 
 [v1]
 Mon, 8 Sep 2025 19:43:17 UTC (16 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Asymptotic structure. VI. Distant paths across a disc, by Tung Nguyen and 2 other authors
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
 | 2025-09
 

 Change to browse by:
 
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
