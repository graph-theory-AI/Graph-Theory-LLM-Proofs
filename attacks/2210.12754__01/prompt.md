Attack the following open graph-theory problem.

Catalog id: 2210.12754__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2210.12754__01/
Source paper: Largest subgraph from a hereditary property in a random graph (arXiv:2210.12754)

=== Extracted statement (catalog JSON) ===
Title: Open Problem (accurate estimate in the bipartite case)
Provide a more accurate estimate for $\mathrm{ex}(G, \mathcal{P})$ when $\mathcal{P}$ misses a bipartite graph (i.e., when Theorem 1.1 gives only $\mathrm{ex}(G(n,p),\mathcal{P}) = o(n^2)$ whp).

Context:
When the minimum chromatic number $k$ of a graph not in $\mathcal{P}$ equals 2, Theorem 1.1 yields $\mathrm{ex}(G(n,p),\mathcal{P}) = o(n^2)$ whp but does not determine the precise order of magnitude. The authors ask for a sharper asymptotic in this regime.

=== Catalog page (statement + literature review) ===
Bipartite-missing hereditary ex(G(n,p), P) sharp asymptotics — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The open problem asks for a sharp asymptotic for ex(G(n,p),P) when the minimum chromatic number of a graph not in P is 2 (i.e., P misses a bipartite graph), a case where the main theorem of the source paper yields only o(n^2). Clifton, Liu, Mattos, and Zheng (arXiv:2405.09486, 2024) directly answer the explicit sub-question posed by Alon–Krivelevich–Samotij: they prove that ex(G(n,p),P) = O(n^{2-epsilon}) with high probability for some epsilon=epsilon(P)>0, establishing a polynomial improvement over the trivial o(n^2) bound. For excluded complete bipartite graphs K_{s,t} they obtain the more precise bound O(n^{2-1/s}(log n)^{1/s}). However, determining the precise order of magnitude for general hereditary properties missing an arbitrary bipartite graph remains open.

 Cited literature (1)

 
 
 
partial Subgraphs of random graphs in hereditary families
 (2024)
 

 
 Alexander Clifton, Hong Liu, Leticia Mattos, Michael Zheng · arXiv preprint · arXiv:2405.09486

Proves ex(G(n,p),P) = O(n^{2-epsilon}) whp for some epsilon>0 whenever P misses a bipartite graph, giving a polynomial improvement over the o(n^2) bound and directly answering one part of the open question; for K_{s,t}-free hereditary properties the bound is refined to O(n^{2-1/s}(log n)^{1/s}).
 

 

 Reviewer notes. arXiv:2405.09486 explicitly cites 2210.12754 and answers the polynomial sub-question (n^{2-epsilon} upper bound), but the precise order of magnitude for general bipartite-missing hereditary properties is still not determined, so the open problem is only partially resolved.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Provide a more accurate estimate for $\mathrm{ex}(G, \mathcal{P})$ when $\mathcal{P}$ misses a bipartite graph (i.e., when Theorem 1.1 gives only $\mathrm{ex}(G(n,p),\mathcal{P}) = o(n^2)$ whp).

Context

When the minimum chromatic number $k$ of a graph not in $\mathcal{P}$ equals 2, Theorem 1.1 yields $\mathrm{ex}(G(n,p),\mathcal{P}) = o(n^2)$ whp but does not determine the precise order of magnitude. The authors ask for a sharper asymptotic in this regime.

Notes. PDF source; stated as an open problem in the concluding remarks without a labelled environment.

Source paper

 Largest subgraph from a hereditary property in a random graph
 Noga Alon, Michael Krivelevich, Wojciech Samotij · 2022-10-23
 https://arxiv.org/abs/2210.12754
 PDF source

=== Source paper abstract / header ===
Abstract:We prove that for every non-trivial hereditary family of graphs ${\cal P}$ and for every fixed $p \in (0,1)$, the maximum possible number of edges in a subgraph of the random graph $G(n,p)$ which belongs to ${\cal P}$ is, with high probability, $$ \left(1-\frac{1}{k-1}+o(1)\right)p{n \choose 2}, $$ where $k$ is the minimum chromatic number of a graph that does not belong to ${\cal P}$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C80, 05C35
 

 Cite as:
 arXiv:2210.12754 [math.CO]
 

 
  
 (or 
 arXiv:2210.12754v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2210.12754
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Michael Krivelevich [view email] 
 [v1]
 Sun, 23 Oct 2022 15:39:53 UTC (7 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Largest subgraph from a hereditary property in a random graph, by Noga Alon and 2 other authors
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
 | 2022-10
 

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
