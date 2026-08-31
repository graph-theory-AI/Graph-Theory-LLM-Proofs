Attack the following open graph-theory problem.

Catalog id: 2409.05039__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2409.05039__00/
Source paper: Distant digraph domination (arXiv:2409.05039)

=== Catalog page (statement + literature review) ===
Strong 2-kernel size bound in split digraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The source paper (Theorem 2.4) proves that every split digraph with no sources has a standard 2-kernel of size at most |G|/2, resolving the Erdős–Székely conjecture for this class. The open question asks whether the size bound survives when the 2-kernel is required to be strong — i.e., every vertex v in the tournament part T is either 1-covered by some vertex of K, or 2-covered by some vertex of K ∩ T. No follow-up work addressing this stronger variant was found in the indexed literature. The conjecture is recent (posted September 2024) and a targeted web search returns no evidence of resolution.

 Reviewer notes. No follow-up found on this specific open question. The source paper was published in The Electronic Journal of Combinatorics (v33i1p32, 2025). The main 2-kernel result (Theorem 2.4) is fully established; the strong 2-kernel variant asks whether the additional covering requirement for vertices in the tournament part T still allows a kernel of size at most |G|/2. The authors explicitly note they do not know the answer.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Does every split digraph $G$ with no sources admit a strong 2-kernel of size at most $|G|/2$?

Context

The paper proves (Theorem 2.4) that every split digraph with no sources has a 2-kernel of size at most $|G|/2$. A 2-kernel $K$ is called strong if for every vertex $v$ in the tournament part $T$, either some vertex of $K$ 1-covers $v$, or some vertex of $K \cap T$ 2-covers $v$. The authors note in passing that they do not know whether the size bound survives under this strengthening.

Notes. Stated as a parenthetical remark inside the proof section: 'We do not know whether 1.2 remains true if we ask for a strong 2-kernel of size at most |G|/2.' No labelled theorem environment.

Source paper

 Distant digraph domination
 Tung Nguyen, Alex Scott, Paul Seymour · 2024-09-08
 https://arxiv.org/abs/2409.05039
 PDF source

=== Source paper abstract / header ===
Abstract:A {\em $k$-kernel} in a digraph $G$ is a stable set $X$ of vertices such that every vertex of $G$ can be joined from $X$ by a directed path of length at most $k$. We prove three results about $k$-kernels. First, it was conjectured by Erdős and Székely in 1976 that every digraph $G$ with no source has a 2-kernel $|K|$ with $|K|\le |G|/2$. We prove this conjecture when $G$ is a ``split digraph'' (that is, its vertex set can be partitioned into a tournament and a stable set), improving a result of Langlois et al., who proved that every split digraph $G$ with no source has a 2-kernel of size at most $2|G|/3$. Second, the Erdős-Székely conjecture implies that in every digraph $G$ there is a 2-kernel $K$ such that the union of $K$ and its out-neighbours has size at least $|G|/2$. We prove that this is true if $V(G)$ can be partitioned into a tournament and an acyclic set. Third, in a recent paper, Spiro asked whether, for all $k\ge 3$, every strongly-connected digraph $G$ has a $k$-kernel of size at most about $|G|/(k+1)$. This remains open, but we prove that there is one of size at most about $|G|/(k-1)$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2409.05039 [math.CO]
 

 
  
 (or 
 arXiv:2409.05039v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2409.05039
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Sun, 8 Sep 2024 09:38:39 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Distant digraph domination, by Tung Nguyen and 2 other authors
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
 | 2024-09
 

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
