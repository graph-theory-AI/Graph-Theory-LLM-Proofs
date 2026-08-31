Attack the following open graph-theory problem.

Catalog id: 2604.13700__00
Catalog status: open (triage tier 2, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2604.13700__00/
Source paper: Openly disjoint cycles and directed tree-width of regular digraphs (arXiv:2604.13700)

=== Catalog page (statement + literature review) ===
Limit of c_r/r in regular digraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The paper defines $c_r$ as the minimum, over all $r$-regular digraphs $D$, of the largest number of openly disjoint cycles through a common vertex, proves that $c_r/r$ converges to a limit $L \in [3/22, 1]$, and asks for the exact value of $L$. The paper was posted on 2026-04-26 and no follow-up work determining $L$ has appeared in the indexed literature as of 2026-05-14. The problem remains fully open.

 Reviewer notes. No follow-up found. The paper is very recent (posted 2026-04-26). The lower bound 3/22 comes from the main theorem of the paper; the upper bound 1 is trivial. The exact limit is unknown. Steiner's research page lists this paper as submitted but shows no companion or follow-up preprint.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine $\lim_{r\rightarrow\infty}\frac{c_{r}}{r}$.

Context

The paper proves that the sequence $(c_r/r)_{r\in\mathbb{N}}$ converges to some limit $L\in[\frac{3}{22},1]$; Problem 2 asks for the exact value of this limit. The problem is stated immediately after the proof of convergence.

Source paper

 Openly disjoint cycles and directed tree-width of regular digraphs
 Raphael Steiner · 2026-04-26
 https://arxiv.org/abs/2604.13700

=== Source paper abstract / header ===
Abstract:Given a digraph $D$, let $c(D)$ denote the largest integer $k$ such that there are $k$ openly disjoint cycles through a vertex, i.e., a collection of directed cycles $C_1,\ldots,C_k$ through a common vertex $v$ such that $C_1-v,\ldots,C_k-v$ are pairwise vertex-disjoint. The famous Caccetta-Häggkvist conjecture and its regular variant due to Behzad, Chartrand and Wall from 1970, have motivated the study of degree conditions forcing $c(D)$ to be large.
In 1985 Thomassen constructed digraphs of arbitrarily high minimum out- and in-degree such that $c(D)\le 2$. In 2005, Seymour asked whether in contrast every $r$-regular digraph satisfies $c(D)=r$, which would have implied the Behzad-Chartrand-Wall conjecture. In 2008, Mader answered this negatively for every $r\ge 8$, but conjectured that nevertheless the minimum value $c_r$ of $c(D)$ over all $r$-regular digraphs grows with $r$, i.e. $\lim_{r\rightarrow\infty}c_r=\infty$.
As the first main result of our paper, we prove Mader's conjecture in a strong form by showing $c_r\ge \lceil\frac{3}{22} r\rceil$ for every $r\in \mathbb{N}$. We also show $c_r\le 7\left\lceil \frac{r}{8}\right\rceil$, improving the previous best upper bound $c_r\le r-\Theta(\sqrt{r})$ due to Mader.
In our second main result we show that every $r$-regular digraph has directed tree-width $\Omega(r)$. This is tight up to the implied constant and cannot be extended to digraphs of minimum out- and in-degree at least $r$. As a corollary we obtain the existence of a function $f:\mathbb{N}\rightarrow \mathbb{N}$ such that every regular digraph with degree at least $f(k)$ contains a subdivision of the cylindrical wall of order $k$, and hence of a large class of planar digraphs. This makes progress on the notoriously difficult problem of finding degree conditions guaranteeing subdivisions of digraphs, related to a well-known conjecture of Mader from 1985.
 

 
 
 
 Comments:
 16 pages, added new result
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C07, 05C20, 05C38, 05C40
 

 Cite as:
 arXiv:2604.13700 [math.CO]
 

 
  
 (or 
 arXiv:2604.13700v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2604.13700
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Wed, 15 Apr 2026 10:28:27 UTC (13 KB)

 [v2]
 Sun, 26 Apr 2026 15:04:32 UTC (29 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Openly disjoint cycles and directed tree-width of regular digraphs, by Raphael Steiner
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
 | 2026-04
 

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
