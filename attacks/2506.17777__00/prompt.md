Attack the following open graph-theory problem.

Catalog id: 2506.17777__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2506.17777__00/
Source paper: Extended VC-dimension, and Radon and Tverberg type theorems for unions … (arXiv:2506.17777)

=== Extracted statement (catalog JSON) ===
Title: Problem 1.4
Determine or estimate the least integer $f=f_{r}(d,s_{1},\ldots,s_{r})$ such that for any set $P$ of $f$ points in $\mathbb{R}^{d}$ there is a partition into $r$ pairwise disjoint sets $P=\bigcup_{i=1}^{r}P_{i}$ such that for any family of sets $C_{1},\ldots,C_{r}$ with $P_{i}\subset C_{i}$ where $C_{i}$ is an $s_{i}$-convex set for every $i\in[r]$ we have that $\bigcap_{i=1}^{r}C_{i}\neq\emptyset$.

Context:
This is a Tverberg-type generalization of Problem 1.3 to $r$ parts and $r$ families of $s_i$-convex sets. Radon's theorem is equivalent to $f(d,1,1)=d+2$ and Tverberg's theorem is equivalent to $f_{r}(d,1,\ldots,1)=(r-1)(d+1)+1$. The paper provides an upper bound via Theorem 1.6 but the exact determination remains open.

=== Catalog page (statement + literature review) ===
s-convex Tverberg partition number — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Problem 1.4 asks to determine or estimate f_r(d,s_1,...,s_r), the minimum number of points guaranteeing a Tverberg-type partition with s_i-convex containers. The source paper supplies an upper bound via Theorem 1.6. A follow-up by Chen, Wang, Ge, Shu, and Xu (arXiv:2510.20770, October 2025) answers two related questions of Alon and Smorodinsky negatively, proving f_r(d,s,...,s) > s^r for all r >= 2, s >= 1, d >= 2r-2, disproving polynomial boundedness in s and nearly matching the upper bound up to a log s factor. The exact determination of f_r(d,s_1,...,s_r) remains open.

 Cited literature (1)

 
 
 
partial A Tverberg-type problem of Kalai: Two negative answers to questions of Alon and Smorodinsky, and the power of disjointness
 (2025)
 

 
 Wenchong Chen, Zhouningxin Wang, Gennian Ge, Yang Shu, Zixiang Xu · arXiv preprint · arXiv:2510.20770

Proves f_r(d,s,...,s) > s^r for r >= 2, s >= 1, d >= 2r-2, nearly matching the upper bound up to a log s factor, and disproves polynomial boundedness; the exact value of f_r(d,s_1,...,s_r) remains open.
 

 

 Reviewer notes. arXiv:2510.20770 (posted October 2025, after the arXiv preprint of the source paper in June 2025) directly addresses two open questions from the Alon-Smorodinsky paper with near-tight exponential lower bounds; the exact determination of f_r(d,s_1,...,s_r) for general parameters remains open.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine or estimate the least integer $f=f_{r}(d,s_{1},\ldots,s_{r})$ such that for any set $P$ of $f$ points in $\mathbb{R}^{d}$ there is a partition into $r$ pairwise disjoint sets $P=\bigcup_{i=1}^{r}P_{i}$ such that for any family of sets $C_{1},\ldots,C_{r}$ with $P_{i}\subset C_{i}$ where $C_{i}$ is an $s_{i}$-convex set for every $i\in[r]$ we have that $\bigcap_{i=1}^{r}C_{i}\neq\emptyset$.

Context

This is a Tverberg-type generalization of Problem 1.3 to $r$ parts and $r$ families of $s_i$-convex sets. Radon's theorem is equivalent to $f(d,1,1)=d+2$ and Tverberg's theorem is equivalent to $f_{r}(d,1,\ldots,1)=(r-1)(d+1)+1$. The paper provides an upper bound via Theorem 1.6 but the exact determination remains open.

Notes. The paper proves the upper bound $f_{r}(d,s_{1},\ldots,s_{r})=O\left(dr^{2}\cdot\log r\cdot\prod_{i=1}^{r}s_{i}\cdot\ln(1+\prod_{i=1}^{r}s_{i})\right)$ via Theorem 1.6, partially addressing this problem. A 2025 paper by Chen et al. (reference [9]) is titled 'A Tverberg-type problem of Kalai: Two negative answers to questions of Alon and Smorodinsky', suggesting specific sub-questions of this problem are attributed to the paper authors.

Source paper

 Extended VC-dimension, and Radon and Tverberg type theorems for unions of convex sets
 Noga Alon, Shakhar Smorodinsky · 2026-02-27
 https://arxiv.org/abs/2506.17777

=== Source paper abstract / header ===
Abstract:We prove a new Radon type theorem for unions of convex sets, settling an open problem posed by Kalai in the 1970s. We also define
and study an extension of the notion of the VC-dimension of a
hypergraph and apply it to establish an extension of our
Radon type theorem to a Tverberg type theorem
for unions of convex sets.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Computational Geometry (cs.CG)
 
 
 MSC classes:
 52C10
 

 Cite as:
 arXiv:2506.17777 [math.CO]
 

 
  
 (or 
 arXiv:2506.17777v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2506.17777
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Shakhar Smorodinsky [view email] 
 [v1]
 Sat, 21 Jun 2025 18:13:42 UTC (16 KB)

 [v2]
 Sun, 29 Jun 2025 06:10:40 UTC (17 KB)

 [v3]
 Fri, 27 Feb 2026 19:30:26 UTC (20 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Extended VC-dimension, and Radon and Tverberg type theorems for unions of convex sets, by Noga Alon and 1 other authors
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
 | 2025-06
 

 Change to browse by:
 
 cs
 cs.CG
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
