Attack the following open graph-theory problem.

Catalog id: 2008.01616__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2008.01616__00/
Source paper: Automorphism groups of maps in linear time (arXiv:2008.01616)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.2
There is no $\varepsilon > 0$ for which there is an algorithm for testing isomorphism of maps of unrestricted genus in time $O(n^{2-\varepsilon})$.

Context:
The best known algorithm for the simultaneous conjugation problem runs in time $O(n^2 \log d / \log n + dn \log n)$, yielding an $O(n^2/\log n)$ algorithm for map isomorphism and automorphism problems of unrestricted genus. In complexity theory this is not considered 'truly subquadratic', which motivates the conjecture.

=== Catalog page (statement + literature review) ===
Quadratic lower bound for map isomorphism — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 1.2 asserts that map isomorphism for unrestricted genus admits no truly subquadratic algorithm (i.e., no $O(n^{2-\varepsilon})$ bound for any $\varepsilon>0$). The best known algorithm runs in $O(n^2/\log n)$ via a reduction to the simultaneous conjugacy problem in symmetric groups (Brodnik et al., arXiv:2007.05870), which predates the conjecture; the source paper's authors were already aware of it when formulating the conjecture. No follow-up paper resolving or refuting Conjecture 1.2 was found in the indexed literature as of May 2026.

 Reviewer notes. The $O(n^2\log d/\log n + dn\log n)$ simultaneous conjugacy algorithm (Brodnik et al., arXiv:2007.05870, Journal of Graph Theory 2022) achieves $o(n^2)$ but not a polynomial improvement; this is precisely why the authors conjectured no $O(n^{2-\varepsilon})$ algorithm exists. The SIAM paper 'Isomorphism Testing Parameterized by Genus and Beyond' (doi:10.1137/22M1514076) appeared in the search but could not be fetched (paywall); its title suggests it concerns bounded-genus parameterised algorithms rather than unrestricted-genus hardness. The published version of the source paper appeared in ACM Transactions on Algorithms (doi:10.1145/3686798, also paywalled) with no indication of conjecture resolution.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There is no $\varepsilon > 0$ for which there is an algorithm for testing isomorphism of maps of unrestricted genus in time $O(n^{2-\varepsilon})$.

Context

The best known algorithm for the simultaneous conjugation problem runs in time $O(n^2 \log d / \log n + dn \log n)$, yielding an $O(n^2/\log n)$ algorithm for map isomorphism and automorphism problems of unrestricted genus. In complexity theory this is not considered 'truly subquadratic', which motivates the conjecture.

Source paper

 Automorphism groups of maps in linear time
 Ken-ichi Kawarabayashi, Bojan Mohar, Roman Nedela, Peter Zeman · 2021-01-07
 https://arxiv.org/abs/2008.01616
 PDF source

=== Source paper abstract / header ===
Abstract:By a map we mean a $2$-cell decomposition of a closed compact surface, i.e., an embedding of a graph such that every face is homeomorphic to an open disc. Automorphism of a map can be thought of as a permutation of the vertices which preserves the vertex-edge-face incidences in the embedding. When the underlying surface is orientable, every automorphism of a map determines an angle-preserving homeomorphism of the surface. While it is conjectured that there is no "truly subquadratic" algorithm for testing map isomorphism for unconstrained genus, we present a linear-time algorithm for computing the generators of the automorphism group of a map, parametrized by the genus of the underlying surface. The algorithm applies a sequence of local reductions and produces a uniform map, while preserving the automorphism group. The automorphism group of the original map can be reconstructed from the automorphism group of the uniform map in linear time. We also extend the algorithm to non-orientable surfaces by making use of the antipodal double-cover.
 

 
 
 
 Comments:
 Added funding information
 

 Subjects:
 
 Combinatorics (math.CO); Data Structures and Algorithms (cs.DS)
 

 Cite as:
 arXiv:2008.01616 [math.CO]
 

 
  
 (or 
 arXiv:2008.01616v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2008.01616
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Peter Zeman [view email] 
 [v1]
 Tue, 4 Aug 2020 14:57:06 UTC (121 KB)

 [v2]
 Thu, 7 Jan 2021 17:29:05 UTC (121 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Automorphism groups of maps in linear time, by Ken-ichi Kawarabayashi and Bojan Mohar and Roman Nedela and Peter Zeman
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
 | 2020-08
 

 Change to browse by:
 
 cs
 cs.DS
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
