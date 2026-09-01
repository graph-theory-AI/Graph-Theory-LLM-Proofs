Attack the following open graph-theory problem.

Catalog id: 2305.15585__03
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2305.15585__03/
Source paper: Chromatic number is not tournament-local (arXiv:2305.15585)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 13
There exists $f(N)$ satisfying $f(N)=o(\log N)$ such that for every $N$-vertex graph $G$ with $\chi(G)\geqslant f(N)$, and every tournament $T$ on the same vertex set, there is a vertex $v$ for which $\chi(G[N^{+}_{T}(v)])\geqslant 3$.

Context:
Theorem 2 shows a collection of at most $\lceil\log_2(N)/\lfloor\chi/2-1\rfloor\rceil$ out-neighbourhoods suffices to force chromatic number at least 3; the authors ask whether $o(\log(N)/\chi)$ out-neighbourhoods (or even a single vertex) suffice when the chromatic number threshold itself grows with $N$ as $o(\log N)$.

=== Catalog page (statement + literature review) ===
χ threshold for tournament out-neighbourhood 3-coloring — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 13 from arXiv:2305.15585 asks whether a function f(N)=o(log N) exists such that for every N-vertex graph G with \chi(G)\geq f(N) and every tournament T on the same vertex set, some vertex v satisfies \chi(G[N^+_T(v)])\geq 3. The paper itself (published in JCTB 168, 2024) establishes this only with a bound of \lceil\log_2(N)/\lfloor\chi/2-1\rfloor\rceil out-neighbourhoods rather than a single vertex. No follow-up paper resolving Conjecture 13 was found in the indexed literature as of May 2026.

 Reviewer notes. No follow-up found. Conjecture 13 is presented as an open question in the closing remarks of the source paper. The paper was published as JCTB 168 (2024) 86-95. The related paper arXiv:2306.02364 (Nguyen, Scott, Seymour on tournament structure problems) does not appear to address this conjecture. The conjecture is recent (2023) and the absence of evidence of resolution supports high-confidence open status.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There exists $f(N)$ satisfying $f(N)=o(\log N)$ such that for every $N$-vertex graph $G$ with $\chi(G)\geqslant f(N)$, and every tournament $T$ on the same vertex set, there is a vertex $v$ for which $\chi(G[N^{+}_{T}(v)])\geqslant 3$.

Context

Theorem 2 shows a collection of at most $\lceil\log_2(N)/\lfloor\chi/2-1\rfloor\rceil$ out-neighbourhoods suffices to force chromatic number at least 3; the authors ask whether $o(\log(N)/\chi)$ out-neighbourhoods (or even a single vertex) suffice when the chromatic number threshold itself grows with $N$ as $o(\log N)$.

Source paper

 Chromatic number is not tournament-local
 António Girão, Kevin Hendrey, Freddie Illingworth, Florian Lehner, Lukas Michel, Michael Savery, Raphael Steiner · 2023-12-04
 https://arxiv.org/abs/2305.15585

=== Source paper abstract / header ===
Abstract:Scott and Seymour conjectured the existence of a function $f \colon \mathbb{N} \to \mathbb{N}$ such that, for every graph $G$ and tournament $T$ on the same vertex set, $\chi(G) \geqslant f(k)$ implies that $\chi(G[N_T^+(v)]) \geqslant k$ for some vertex $v$. In this note we disprove this conjecture even if $v$ is replaced by a vertex set of size $\mathcal{O}(\log{\lvert V(G)\rvert})$. As a consequence, we answer in the negative a question of Harutyunyan, Le, Thomassé, and Wu concerning the corresponding statement where the graph $G$ is replaced by another tournament, and disprove a related conjecture of Nguyen, Scott, and Seymour. We also show that the setting where chromatic number is replaced by degeneracy exhibits a quite different behaviour.
 

 
 
 
 Comments:
 7 pages; funding information added
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15, 05C20
 

 Cite as:
 arXiv:2305.15585 [math.CO]
 

 
  
 (or 
 arXiv:2305.15585v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2305.15585
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Freddie Illingworth Dr [view email] 
 [v1]
 Wed, 24 May 2023 21:41:18 UTC (19 KB)

 [v2]
 Mon, 4 Dec 2023 15:19:50 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Chromatic number is not tournament-local, by Ant\'onio Gir\~ao and 6 other authors
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
 | 2023-05
 

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
