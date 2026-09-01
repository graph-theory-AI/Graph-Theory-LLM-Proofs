Attack the following open graph-theory problem.

Catalog id: 2311.05500__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2311.05500__00/
Source paper: Universality for graphs with bounded density (arXiv:2311.05500)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.1
For every $d\in\mathbb{Q}$, $d>1$, and $n\in\mathbb{N}$, there exists a graph $G$ with $$e(G)\leq Cn^{2-1/d}$$ edges which is $\mathcal{H}_{d}(n)$-universal, where $C=C(d)$.

Context:
The authors initiate the study of universality for graphs with bounded density, unifying earlier results on bounded-degree graphs, forests, and degenerate graphs. They note that a simple counting argument shows $e(G)=o(n^{2-1/d})$ is insufficient, making the conjectured bound tight up to the constant $C$. The paper proves constructions achieving $O_d(n^{2-1/(\lceil d\rceil+1)})$ edges, approaching but not yet matching this conjecture.

=== Catalog page (statement + literature review) ===
Universality for bounded-density graph families — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 1.1 of arXiv:2311.05500 asks for an $\mathcal{H}_d(n)$-universal graph with at most $Cn^{2-1/d}$ edges, which would be tight up to the constant $C$. The source paper itself proves a weaker construction with $O_d(n^{2-1/(\lceil d\rceil+1)})$ edges, achieving the bound only when $d\in\mathbb{N}$. A broad web search (5 calls) found no subsequent paper resolving or substantially advancing the general rational-$d$ case of this conjecture.

 Reviewer notes. No follow-up found that resolves Conjecture 1.1 for non-integer rational d. Related work on hypergraph universality (arXiv:2511.23341, arXiv:2411.19432) appeared in 2024-2025 but could not be verified to address this specific conjecture within the 5-call budget. The paper has been published in a journal (ScienceDirect link found, likely J. Combin. Theory Ser. B). The gap between the proved bound O_d(n^{2-1/(ceil(d)+1)}) and the conjectured O_d(n^{2-1/d}) remains open for rational non-integer d.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every $d\in\mathbb{Q}$, $d>1$, and $n\in\mathbb{N}$, there exists a graph $G$ with $$e(G)\leq Cn^{2-1/d}$$ edges which is $\mathcal{H}_{d}(n)$-universal, where $C=C(d)$.

Context

The authors initiate the study of universality for graphs with bounded density, unifying earlier results on bounded-degree graphs, forests, and degenerate graphs. They note that a simple counting argument shows $e(G)=o(n^{2-1/d})$ is insufficient, making the conjectured bound tight up to the constant $C$. The paper proves constructions achieving $O_d(n^{2-1/(\lceil d\rceil+1)})$ edges, approaching but not yet matching this conjecture.

Notes. The complete edge bound $e(G)\leq Cn^{2-1/d}$ appears in the introduction prose; the theorem-environment extraction was truncated. Statement reconstructed from the introduction.

Source paper

 Universality for graphs with bounded density
 Noga Alon, Natalie Dodson, Carmen Jackson, Rose McCarty, Rajko Nenadov, Lani Southern · 2024-01-11
 https://arxiv.org/abs/2311.05500

=== Source paper abstract / header ===
Abstract:A graph $G$ is $\textit{universal}$ for a (finite) family $\mathcal{H}$ of graphs if every $H \in \mathcal{H}$ is a subgraph of $G$. For a given family $\mathcal{H}$, the goal is to determine the smallest number of edges an $\mathcal{H}$-universal graph can have. With the aim of unifying a number of recent results, we consider a family of graphs with bounded density. In particular, we construct a graph with $O_d\left( n^{2 - 1/(\lceil d \rceil + 1)} \right)$ edges which contains every $n$-vertex graph with density at most $d \in \mathbb{Q}$ ($d \ge 1$), which is close to a lower bound $\Omega(n^{2 - 1/d - o(1)})$ obtained by counting lifts of a carefully chosen (small) graph. When restricting the maximum degree of such graphs to be constant, we obtain a near-optimal universality. If we further assume $d \in \mathbb{N}$, we get an asymptotically optimal construction.
 

 
 
 
 Comments:
 14 pages, updated version focusing on density, with new title and additional author
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C35
 

 Cite as:
 arXiv:2311.05500 [math.CO]
 

 
  
 (or 
 arXiv:2311.05500v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2311.05500
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Rose McCarty [view email] 
 [v1]
 Thu, 9 Nov 2023 16:38:31 UTC (120 KB)

 [v2]
 Thu, 11 Jan 2024 14:01:58 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Universality for graphs with bounded density, by Noga Alon and 5 other authors
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
 | 2023-11
 

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
