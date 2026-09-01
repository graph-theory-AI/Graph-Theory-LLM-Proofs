Attack the following open graph-theory problem.

Catalog id: 1812.09752__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1812.09752__00/
Source paper: The hat guessing number of graphs (arXiv:1812.09752)

=== Extracted statement (catalog JSON) ===
Title: Problem 1.4
Do there exist functions $f_i : \mathbb{N} \to \mathbb{N}$, $1 \leq i \leq 3$ such that (i) if the maximum degree of $G$ is $\Delta$, then $HG(G) \leq f_1(\Delta)$; (ii) if $G$ is $d$-degenerate, then $HG(G) \leq f_2(d)$; (iii) if the minimum degree of $G$ is $\delta$, then $HG(G) \geq f_3(\delta)$, and $f_3(\delta)$ tends to infinity when $\delta$ tends to infinity.

Context:
The authors seek to understand how basic graph parameters control the hat guessing number. The existence of $f_1$ is already known via the Lovász Local Lemma ($HG(G) < e^\Delta$), but whether $f_2$ (degeneracy bound) or $f_3$ (minimum-degree lower bound) exist is unclear. Theorems 1.6 and 1.8 provide partial progress toward part (ii).

=== Catalog page (statement + literature review) ===
Hat guessing number graph parameter bounds — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Problem 1.4 remains largely open. Part (i) (HG(G) bounded by a function of maximum degree) was already settled before the problem was stated via the Lovász Local Lemma. Parts (ii) and (iii) are unresolved: for part (ii), several papers have studied hat guessing numbers of degenerate and strongly degenerate graphs and shown that HG can grow at least as fast as $2^{2^{d-1}}$ for $d$-degenerate graphs, but whether an upper bound $f_2(d)$ exists is still open; for part (iii), no evidence of a minimum-degree lower bound was found.

 Cited literature (1)

 
 
 
partial On the Hat Guessing Number of Graphs
 (2021)
 

 
 Noga Alon, Jeremy Chizewer · arXiv preprint · arXiv:2107.05995

Restates Problem 1.4 and notes a positive answer seems plausible but does not prove it; constructs a planar graph with HG(G)=12 and analyzes random and complete multipartite graphs.
 

 

 Reviewer notes. Web search found two further highly relevant papers not verified by WebFetch due to the 5-call cap: arXiv:2003.04990 (Xiaoyu He, 'Hat Guessing Numbers of Degenerate Graphs', Electronic Journal of Combinatorics 2020) showing HG(G) >= 2^{2^{d-1}} for some d-degenerate G and giving new upper-bound methods, and arXiv:2112.09619 ('Hat guessing numbers of strongly degenerate graphs', SIAM J. Discrete Math. ~2023); search summaries indicate that the general degeneracy-bound question of part (ii) remains open as of those papers. Part (iii) (minimum-degree lower bound) has no follow-up evidence in indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Do there exist functions $f_i : \mathbb{N} \to \mathbb{N}$, $1 \leq i \leq 3$ such that (i) if the maximum degree of $G$ is $\Delta$, then $HG(G) \leq f_1(\Delta)$; (ii) if $G$ is $d$-degenerate, then $HG(G) \leq f_2(d)$; (iii) if the minimum degree of $G$ is $\delta$, then $HG(G) \geq f_3(\delta)$, and $f_3(\delta)$ tends to infinity when $\delta$ tends to infinity.

Context

The authors seek to understand how basic graph parameters control the hat guessing number. The existence of $f_1$ is already known via the Lovász Local Lemma ($HG(G) < e^\Delta$), but whether $f_2$ (degeneracy bound) or $f_3$ (minimum-degree lower bound) exist is unclear. Theorems 1.6 and 1.8 provide partial progress toward part (ii).

Source paper

 The hat guessing number of graphs
 Noga Alon, Omri Ben-Eliezer, Chong Shangguan, Itzhak Tamo · 2020-01-15
 https://arxiv.org/abs/1812.09752
 PDF source

=== Source paper abstract / header ===
Abstract:Consider the following hat guessing game: $n$ players are placed on $n$ vertices of a graph, each wearing a hat whose color is arbitrarily chosen from a set of $q$ possible colors. Each player can see the hat colors of his neighbors, but not his own hat color. All of the players are asked to guess their own hat colors simultaneously, according to a predetermined guessing strategy and the hat colors they see, where no communication between them is allowed. Given a graph $G$, its hat guessing number ${\rm{HG}}(G)$ is the largest integer $q$ such that there exists a guessing strategy guaranteeing at least one correct guess for any hat assignment of $q$ possible colors.
In 2008, Butler et al. asked whether the hat guessing number of the complete bipartite graph $K_{n,n}$ is at least some fixed positive (fractional) power of $n$. We answer this question affirmatively, showing that for sufficiently large $n$, the complete $r$-partite graph $K_{n,\ldots,n}$ satisfies ${\rm{HG}}(K_{n,\ldots,n})=\Omega(n^{\frac{r-1}{r}-o(1)})$. Our guessing strategy is based on a probabilistic construction and other combinatorial ideas, and can be extended to show that ${\rm{HG}}(\vec{C}_{n,\ldots,n})=\Omega(n^{\frac{1}{r}-o(1)})$, where $\vec{C}_{n,\ldots,n}$ is the blow-up of a directed $r$-cycle, and where for directed graphs each player sees only the hat colors of his outneighbors.
 

 
 
 
 Comments:
 25 pages, minor revision, to appear in JCTB
 

 Subjects:
 
 Combinatorics (math.CO); Information Theory (cs.IT)
 

 Cite as:
 arXiv:1812.09752 [math.CO]
 

 
  
 (or 
 arXiv:1812.09752v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1812.09752
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Chong Shangguan [view email] 
 [v1]
 Sun, 23 Dec 2018 18:27:26 UTC (28 KB)

 [v2]
 Wed, 8 Jan 2020 13:22:04 UTC (28 KB)

 [v3]
 Wed, 15 Jan 2020 13:22:18 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The hat guessing number of graphs, by Noga Alon and Omri Ben-Eliezer and Chong Shangguan and Itzhak Tamo
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
 | 2018-12
 

 Change to browse by:
 
 cs
 cs.IT
 math
 math.IT
 

 

 

 
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
