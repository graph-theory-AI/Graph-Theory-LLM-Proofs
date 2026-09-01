Attack the following open graph-theory problem.

Catalog id: 2407.21360__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2407.21360__00/
Source paper: Clustered Colouring of Graph Products (arXiv:2407.21360)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 7
For any fixed integer $c \geq 2$, there exists an integer $t$ such that for infinitely many graphs $H$ with treewidth $t$ and paths $P$, every $c$-colouring of $H \boxtimes P$ has clustering $\Omega(|V(H \boxtimes P)|^{c/(c^2-c+1)})$.

Context:
The upper bound in Theorem 4 gives that $H_1 \boxtimes H_2$ is $c$-colourable with clustering $O(|V(H_1 \boxtimes H_2)|^{c/(c^2-c+1)})$ when one graph has bounded degree. The authors believe this upper bound is asymptotically tight, and furthermore conjecture that there exists a matching construction where the bounded-degree graph is a path.

=== Catalog page (statement + literature review) ===
Tight clustering bound in treewidth-path strong product — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 7 asserts that for every fixed integer c≥2 the optimal clustering exponent c/(c²−c+1) for c-colourings of H⊠P (with H of fixed treewidth and P a path) is achieved by a matching lower bound. The source paper itself establishes this lower bound for c=2 (Lemma 15, exponent 2/3) and c=3 (Theorem 2, exponent 3/7), confirming the conjecture for those two cases. For c≥4 only a weaker lower bound is known and the conjecture remains open. No follow-up paper resolving the general case was found in a search of arXiv and journal literature through May 2026.

 Reviewer notes. The c=2 and c=3 cases of Conjecture 7 are proved within the source paper (arXiv:2407.21360), which was subsequently published in the Electronic Journal of Combinatorics (accepted June 2025, published July 2025) as v32i3p15. For c≥4 the paper provides only the upper bound O(n^{c/(c²−c+1)}) and a weaker lower bound Ω(n^{1/(c−2/3)}); the conjecture that the tight exponent c/(c²−c+1) is achievable with a path construction remains open. No post-2024 follow-up paper addressing the general case was located.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any fixed integer $c \geq 2$, there exists an integer $t$ such that for infinitely many graphs $H$ with treewidth $t$ and paths $P$, every $c$-colouring of $H \boxtimes P$ has clustering $\Omega(|V(H \boxtimes P)|^{c/(c^2-c+1)})$.

Context

The upper bound in Theorem 4 gives that $H_1 \boxtimes H_2$ is $c$-colourable with clustering $O(|V(H_1 \boxtimes H_2)|^{c/(c^2-c+1)})$ when one graph has bounded degree. The authors believe this upper bound is asymptotically tight, and furthermore conjecture that there exists a matching construction where the bounded-degree graph is a path.

Notes. PDF source — exponents in the clustering bound appear inline without superscript formatting; LaTeX reconstructed from context.

Source paper

 Clustered Colouring of Graph Products
 Rutger Campbell, J. Pascal Gollin, Kevin Hendrey, Thomas Lesgourgues, Bojan Mohar, Youri Tamitegama, Jane Tan, David R. Wood · 2024-07-31
 https://arxiv.org/abs/2407.21360
 PDF source

=== Source paper abstract / header ===
Abstract:A colouring of a graph $G$ has clustering $k$ if the maximum number of vertices in a monochromatic component equals $k$. Motivated by recent results showing that many natural graph classes are subgraphs of the strong product of a graph with bounded treewidth and a path, this paper studies clustered colouring of strong products of two bounded treewidth graphs, where none, one, or both graphs have bounded degree. For example, in the case of two colours, if $n$ is the number of vertices in the product, then we show that clustering $\Theta(n^{2/3})$ is best possible, even if one of the graphs is a path. However, if both graphs have bounded degree, then clustering $\Theta(n^{1/2})$ is best possible. With three colours, if one of the graphs has bounded degree, then we show that clustering $\Theta(n^{3/7})$ is best possible. However, if neither graph has bounded degree, then clustering $\Omega(n^{1/2})$ is necessary. More general bounds for any given number of colours are also presented.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15
 

 Cite as:
 arXiv:2407.21360 [math.CO]
 

 
  
 (or 
 arXiv:2407.21360v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2407.21360
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Thomas Lesgourgues [view email] 
 [v1]
 Wed, 31 Jul 2024 06:06:25 UTC (170 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Clustered Colouring of Graph Products, by Rutger Campbell and 7 other authors
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
 | 2024-07
 

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
