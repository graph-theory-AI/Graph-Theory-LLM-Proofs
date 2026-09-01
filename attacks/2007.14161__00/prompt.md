Attack the following open graph-theory problem.

Catalog id: 2007.14161__00
Catalog status: partial (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2007.14161__00/
Source paper: Twin-width III: Max Independent Set, Min Dominating Set, and Coloring (arXiv:2007.14161)

=== Extracted statement (catalog JSON) ===
Title: Informal conjecture on MIS approximability vs. Min Dominating Set
Max Independent Set may have a very different approximability status than Min Dominating Set on bounded twin-width graphs.

Context:
Theorem 6 establishes $O(1)$-approximation algorithms for Min Dominating Set and Min $r$-Dominating Set on bounded twin-width graphs, but Max Independent Set (Distance-1 MIS) is explicitly excluded from that theorem. The authors note further that a constant approximation for Max Independent Set on bounded twin-width graphs with arbitrarily large clique number would imply a PTAS, and they give some evidence that MIS sits in a fundamentally different approximability regime.

=== Catalog page (statement + literature review) ===
MIS vs. Min Dominating Set approximability gap — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The 2022/2023 paper by Bergé, Bonnet, Déprés, and Watrigant (arXiv:2207.07708, STACS 2023) directly addresses MIS approximability on bounded twin-width graphs, establishing a polynomial-time n^ε-approximation algorithm and a time–approximation tradeoff (O(1)^{2^q-1}-approximation in time exp(O_q(n^{2^{-q}}))). This confirms that MIS sits in a strictly worse approximability regime than Min Dominating Set (which admits an O(1)-approximation) on bounded twin-width graphs, supporting the conjecture. However, no hardness result ruling out a constant-factor approximation for MIS on bounded twin-width has been established, so the precise approximability boundary remains open.

 Cited literature (1)

 
 
 
partial Approximating Highly Inapproximable Problems on Graphs of Bounded Twin-Width
 (2023)
 

 
 Pierre Bergé, Édouard Bonnet, Hugues Déprés, Rémi Watrigant · 40th International Symposium on Theoretical Aspects of Computer Science (STACS 2023), LIPIcs vol. 254 · arXiv:2207.07708 · doi:10.4230/LIPIcs.STACS.2023.10

Proves a polynomial-time n^ε-approximation and a time–approximation tradeoff for Max Independent Set on bounded twin-width graphs (given an O(1)-sequence), demonstrating that MIS is in a strictly worse approximability regime than Min Dominating Set (O(1) approximation), thereby providing the strongest published evidence that the two problems have fundamentally different approximability status on these graphs.
 

 

 Reviewer notes. The conjecture is informal and has no precise mathematical statement to be proved or disproved; rather it asserts that MIS 'may' have a different approximability regime from Min DS. The STACS 2023 paper (arXiv:2207.07708) confirms the different regime in the sense that MIS achieves only n^ε approximation while Min DS achieves O(1), and notes this is the 'first in-depth study of approximability on bounded twin-width.' No polynomial-time constant-factor approximation for MIS is known, and no APX-hardness for MIS on bounded twin-width has been established, leaving the precise complexity boundary open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Max Independent Set may have a very different approximability status than Min Dominating Set on bounded twin-width graphs.

Context

Theorem 6 establishes $O(1)$-approximation algorithms for Min Dominating Set and Min $r$-Dominating Set on bounded twin-width graphs, but Max Independent Set (Distance-1 MIS) is explicitly excluded from that theorem. The authors note further that a constant approximation for Max Independent Set on bounded twin-width graphs with arbitrarily large clique number would imply a PTAS, and they give some evidence that MIS sits in a fundamentally different approximability regime.

Notes. PDF source — the full paper text is truncated after the beginning of the Related Work section; additional labeled conjecture/problem/question environments present in later sections of the paper are not visible in the provided extract and cannot be extracted.

Source paper

 Twin-width III: Max Independent Set, Min Dominating Set, and Coloring
 Édouard Bonnet, Colin Geniet, Eun Jung Kim, Stéphan Thomassé, Rémi Watrigant · 2021-02-12
 https://arxiv.org/abs/2007.14161
 PDF source

=== Source paper abstract / header ===
Abstract:We recently introduced the graph invariant twin-width, and showed that first-order model checking can be solved in time $f(d,k)n$ for $n$-vertex graphs given with a witness that the twin-width is at most $d$, called $d$-contraction sequence or $d$-sequence, and formulas of size $k$ [Bonnet et al., FOCS '20]. The inevitable price to pay for such a general result is that $f$ is a tower of exponentials of height roughly $k$. In this paper, we show that algorithms based on twin-width need not be impractical. We present $2^{O(k)}n$-time algorithms for $k$-Independent Set, $r$-Scattered Set, $k$-Clique, and $k$-Dominating Set when an $O(1)$-sequence is provided. We further show how to solve weighted $k$-Independent Set, Subgraph Isomorphism, and Induced Subgraph Isomorphism, in time $2^{O(k \log k)}n$. These algorithms are based on a dynamic programming scheme following the sequence of contractions forward. We then show a second algorithmic use of the contraction sequence, by starting at its end and rewinding it. As an example, we establish that bounded twin-width classes are $\chi$-bounded. This significantly extends the $\chi$-boundedness of bounded rank-width classes, and does so with a very concise proof. The third algorithmic use of twin-width builds on the second one. Playing the contraction sequence backward, we show that bounded twin-width graphs can be edge-partitioned into a linear number of bicliques, such that both sides of the bicliques are on consecutive vertices, in a fixed vertex ordering. Given that biclique edge-partition, we show how to solve the unweighted Single-Source Shortest Paths and hence All-Pairs Shortest Paths in sublinear time $O(n \log n)$ and time $O(n^2 \log n)$, respectively. Finally we show that Min Dominating Set and related problems have constant integrality gaps on bounded twin-width classes, thereby getting constant approximations on these classes.
 

 
 
 
 Comments:
 38 pages, 6 figures. This version contains more results, notably the approximation for Min Dominating Set, and the title has been edited accordingly
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Computational Complexity (cs.CC); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C85
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2007.14161 [cs.DS]
 

 
  
 (or 
 arXiv:2007.14161v2 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2007.14161
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Tue, 28 Jul 2020 12:36:03 UTC (75 KB)

 [v2]
 Fri, 12 Feb 2021 12:32:34 UTC (84 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Twin-width III: Max Independent Set, Min Dominating Set, and Coloring, by \'Edouard Bonnet and 4 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2020-07
 

 Change to browse by:
 
 cs
 cs.CC
 cs.DM
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Édouard Bonnet
Eun Jung Kim
Stéphan Thomassé
Rémi Watrigant 

 

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
