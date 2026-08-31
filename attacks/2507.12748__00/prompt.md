Attack the following open graph-theory problem.

Catalog id: 2507.12748__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2507.12748__00/
Source paper: Improved Decomposition Bounds for Partition Polytopes and Odd-Covers (arXiv:2507.12748)

=== Catalog page (statement + literature review) ===
Partition polytope diameter ⌈4κ₁/3⌉ bound — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 1.3 from arXiv:2507.12748 posits that the diameter of the partition polytope PP(κ₁,…,κₙ) is at most ⌈4κ₁/3⌉ + c for some absolute constant c. The source paper itself establishes the upper bound ⌈3κ₁/2⌉ (Theorem 1.1) and notes the known lower bound is ⌈4κ₁/3⌉; the conjecture asserts the true diameter matches the lower bound up to a constant. No follow-up paper resolving or making further progress on this conjecture was found in the ~10 months since posting.

 Reviewer notes. No follow-up found. The paper is recent (posted 2025-07-28); the conjecture is open with high confidence. The source paper notes that even the special case κ₁=3 (diameter ≤ 4) is open, suggesting the conjecture requires substantially new techniques.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There exists a constant $c$ such that for any positive integers $n$ and $\kappa_1 \geq \cdots \geq \kappa_n$, the partition polytope $\mathrm{PP}(\kappa_1, \ldots, \kappa_n)$ has diameter at most $\lceil 4\kappa_1/3 \rceil + c$.

Context

Theorem 1.1 establishes an upper bound of $\lceil 3\kappa_1/2 \rceil$ on the diameter of $\mathrm{PP}(\kappa_1,\ldots,\kappa_n)$, while the known lower bound (generalizing a construction from [6]) is $\lceil 4\kappa_1/3 \rceil$. The authors suspect the true diameter is closer to the lower bound, motivating this conjecture. They also note that the natural proof strategy—showing diameter at most 4 when $\kappa_1 = 3$—fails, so new techniques will be required.

Source paper

 Improved Decomposition Bounds for Partition Polytopes and Odd-Covers
 Steffen Borgwardt, Zdeněk Dvořák, Bryce Frederickson, Abigail Nix, Youngho Yoo · 2025-07-28
 https://arxiv.org/abs/2507.12748
 PDF source

=== Source paper abstract / header ===
Abstract:The assignments of a set of $m$ items into $n$ clusters of prescribed sizes $k_1,\dots,k_n$ can be encoded as the vertices of the partition polytope $\mathrm{PP}(k_1,\dots,k_n)$. We prove that, if $K = \max\{k_1,\dots,k_n\}$, then the combinatorial diameter of $\mathrm{PP}(k_1,\dots,k_n)$ is at most $\lceil 3K/2\rceil$. This improves the previously known upper bound of $2K$.
A cycle (or path) odd-cover of a graph $G$ is a set of cycles (or paths) with symmetric difference $G$. We prove that every Eulerian graph $G$ with maximum degree $\Delta$ admits a cycle odd-cover and a path odd-cover, each of size at most $\lceil 3\Delta/4\rceil$. This improves the previously known upper bound of $\Delta$.
The two proofs share many similarities and are both based on the proof of Akiyama, Exoo, and Harary that every graph with maximum degree 4 has linear arboricity at most 3.
 

 
 
 
 Comments:
 27 pages, 12 figures; v2. corrected formatting of abstract and added funding information
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C38, 05C62, 05C70, 52B05
 

 Cite as:
 arXiv:2507.12748 [math.CO]
 

 
  
 (or 
 arXiv:2507.12748v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2507.12748
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Bryce Frederickson [view email] 
 [v1]
 Thu, 17 Jul 2025 03:05:23 UTC (36 KB)

 [v2]
 Mon, 28 Jul 2025 23:54:02 UTC (36 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Improved Decomposition Bounds for Partition Polytopes and Odd-Covers, by Steffen Borgwardt and 4 other authors
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
 | 2025-07
 

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
