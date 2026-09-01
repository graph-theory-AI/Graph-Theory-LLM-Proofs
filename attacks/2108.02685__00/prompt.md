Attack the following open graph-theory problem.

Catalog id: 2108.02685__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2108.02685__00/
Source paper: Irregular Subgraphs (arXiv:2108.02685)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.1
Every $d$-regular graph $G$ on $n$ vertices contains a spanning subgraph $H$ so that for every $k$, $0 \leq k \leq d$, $\left|m(H, k) - \frac{n}{d+1}\right| \leq 2$.

Context:
The paper introduces this conjecture as one of two central open problems on irregular spanning subgraphs. A small value of $m(H)$ measures the irregularity of $H$, and the conjecture asserts that every $d$-regular graph has a spanning subgraph nearly as irregular as its degree permits. The conjecture is tight: the vertex-disjoint union of two 4-cycles shows the additive 2 cannot be reduced to 1 in general.

=== Catalog page (statement + literature review) ===
Near-uniform degree distribution in regular spanning subgraphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 1.1 remains open for general d, but significant partial progress has been made. Fox, Luo, and Pham (2022) confirmed the asymptotic weaker version (Conjecture 1.2) for d = o(n/(log n)^12) via a probabilistic argument. Ma and Xie (2024) proved, via deterministic local adjustment techniques, that the conjecture holds exactly for d=3 (cubic graphs, in a strong form) and gave a general bound |m(H,k) - n/(d+1)| ≤ 2d² independent of n for all d-regular graphs — the first such n-independent bound.

 Cited literature (2)

 
 
 
partial On random irregular subgraphs
 (2022)
 

 
 Jacob Fox, Sammy Luo, Huy Tuan Pham · arXiv preprint (published in Random Structures & Algorithms, 2024) · arXiv:2207.13651

Confirms the asymptotic version of Conjecture 1.1 (Conjecture 1.2) for all d-regular graphs with d = o(n/(log n)^12) by showing the irregular random subgraph H satisfies m(H,k) = (1+o(1))n/(d+1) for all 0 ≤ k ≤ d with high probability; does not resolve Conjecture 1.1 itself.
 

 
 
partial Finding irregular subgraphs via local adjustments
 (2024)
 

 
 Jie Ma, Shengjie Xie · arXiv preprint · arXiv:2406.05675

Fully proves Conjecture 1.1 for d=3 (cubic graphs) in a strong form and establishes a general n-independent bound |m(H,k) - n/(d+1)| ≤ 2d² for all d-regular graphs, using deterministic local adjustment techniques.
 

 

 Reviewer notes. Conjecture 1.1 is open for d ≥ 4 in general. The Ma-Xie 2024 paper (arXiv:2406.05675) represents the strongest deterministic progress: it resolves d=3 completely and provides the first n-independent general bound. The Fox-Luo-Pham paper was published in Random Structures & Algorithms (2024) but the DOI link (Wiley) returned HTTP 402 and could not be verified directly.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Every $d$-regular graph $G$ on $n$ vertices contains a spanning subgraph $H$ so that for every $k$, $0 \leq k \leq d$, $\left|m(H, k) - \frac{n}{d+1}\right| \leq 2$.

Context

The paper introduces this conjecture as one of two central open problems on irregular spanning subgraphs. A small value of $m(H)$ measures the irregularity of $H$, and the conjecture asserts that every $d$-regular graph has a spanning subgraph nearly as irregular as its degree permits. The conjecture is tight: the vertex-disjoint union of two 4-cycles shows the additive 2 cannot be reduced to 1 in general.

Notes. Source is PDF extraction; mathematical notation appears clean for this statement.

Source paper

 Irregular Subgraphs
 Noga Alon, Fan Wei · 2021-08-06
 https://arxiv.org/abs/2108.02685
 PDF source

=== Source paper abstract / header ===
Abstract:We suggest two related conjectures dealing with the existence of spanning irregular subgraphs of graphs. The first asserts that any $d$-regular graph on $n$ vertices contains a spanning subgraph in which the number of vertices of each degree between $0$ and $d$ deviates from $\frac{n}{d+1}$ by at most $2$. The second is that every graph on $n$ vertices with minimum degree $\delta$ contains a spanning subgraph in which the number of vertices of each degree does not exceed $\frac{n}{\delta+1}+2$. Both conjectures remain open, but we prove several asymptotic relaxations for graphs with a large number of vertices $n$. In particular we show that if $d^3 \log n \leq o(n)$ then every $d$-regular graph with $n$ vertices contains a spanning subgraph in which the number of vertices of each degree between $0$ and $d$ is $(1+o(1))\frac{n}{d+1}$. We also prove that any graph with $n$ vertices and minimum degree $\delta$ contains a spanning subgraph in which no degree is repeated more than $(1+o(1))\frac{n}{\delta+1}+2$ times.
 

 
 
 
 Comments:
 The conjectures in the v1 was too strong. We updated the conjectures in this v2
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C35, 05C07
 

 Cite as:
 arXiv:2108.02685 [math.CO]
 

 
  
 (or 
 arXiv:2108.02685v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2108.02685
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Fan Wei [view email] 
 [v1]
 Thu, 5 Aug 2021 15:39:01 UTC (19 KB)

 [v2]
 Fri, 6 Aug 2021 14:57:22 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Irregular Subgraphs, by Noga Alon and Fan Wei
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
 | 2021-08
 

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
