Attack the following open graph-theory problem.

Catalog id: 2206.00186__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2206.00186__00/
Source paper: Dense minors of graphs with independence number two (arXiv:2206.00186)

=== Extracted statement (catalog JSON) ===
Title: Informal conjecture on improving the $g(t)$ lower bound
The factor $1/4$ in $g(t) \geq t(t+2)/8$ can likely be significantly improved. However it appears to be quite challenging, for example, to show that every graph with chromatic number at least $t$ contains a minor on $t$ vertices with at most one tenth of all possible edges missing.

Context:
The authors define $g(t)$ as the maximum number of edges guaranteed in a $t$-vertex minor of any graph with chromatic number at least $t$. Mader's theorem yields $g(t) \geq t(t+2)/8$; the authors believe this is far from the true value, posing a density of $9/10$ as an example of a seemingly hard intermediate target for general graphs.

=== Catalog page (statement + literature review) ===
Dense minor edge density improvement — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture that the factor $1/4$ in $g(t) \geq t(t+2)/8$ can be significantly improved has seen partial progress. Hendrey, Norin, Steiner, and Turcotte (arXiv:2307.01184, J. Graph Theory 2025) proved that graphs of average degree at least $t-1$ contain a $t$-vertex minor with at least $(\sqrt{2}-1-o(1))\binom{t}{2}$ edges — improving the density from $1/4$ to approximately $0.414$ — with an upper bound of $3/4+o(1)$. Since every graph with chromatic number $\geq t$ contains a $t$-critical subgraph of minimum degree $\geq t-1$, this result improves $g(t)$ accordingly. The conjecture's harder target of density $9/10$ (at most one tenth of edges missing) remains open.

 Cited literature (1)

 
 
 
partial Finding dense minors using average degree
 (2023)
 

 
 Kevin Hendrey, Sergey Norin, Raphael Steiner, Jérémie Turcotte · Journal of Graph Theory · arXiv:2307.01184 · doi:10.1002/jgt.23169

Improves the density lower bound for $t$-vertex minors from $1/4$ to $(\sqrt{2}-1-o(1))$ under the average degree $\geq t-1$ condition (which applies to graphs with chromatic number $\geq t$ via $t$-critical subgraphs), and shows the bound cannot exceed $3/4+o(1)$; the target density $9/10$ remains open.
 

 

 Reviewer notes. The conjecture is informal and does not have a canonical name. The follow-up 2307.01184 (Hendrey–Norin–Steiner–Turcotte) explicitly states its motivation as improving the $1/4$ density lower bound and achieves $\sqrt{2}-1 \approx 0.414$ for the average degree condition; the connection to the chromatic number formulation of $g(t)$ holds via the standard reduction through $t$-critical subgraphs. The upper bound $3/4+o(1)$ in the same paper shows there is still a significant gap before any density close to $9/10$ could hold even under average degree conditions.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. The factor $1/4$ in $g(t) \geq t(t+2)/8$ can likely be significantly improved. However it appears to be quite challenging, for example, to show that every graph with chromatic number at least $t$ contains a minor on $t$ vertices with at most one tenth of all possible edges missing.

Context

The authors define $g(t)$ as the maximum number of edges guaranteed in a $t$-vertex minor of any graph with chromatic number at least $t$. Mader's theorem yields $g(t) \geq t(t+2)/8$; the authors believe this is far from the true value, posing a density of $9/10$ as an example of a seemingly hard intermediate target for general graphs.

Notes. Stated as a remark in the introduction without a labelled environment; language 'can likely' and 'appears to be quite challenging' signals authorial belief rather than a formal conjecture.

Source paper

 Dense minors of graphs with independence number two
 Sergey Norin, Paul Seymour · 2022-06-01
 https://arxiv.org/abs/2206.00186
 PDF source

=== Source paper abstract / header ===
Abstract:Motivated by Hadwiger's conjecture, we prove that every $n$-vertex graph $G$ with no independent set of size three contains an $\lceil n/2\rceil$-vertex simple minor $H$ with $$0.98688 \cdot \binom{|V(H)|}{2} - o(n^2)$$ edges.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2206.00186 [math.CO]
 

 
  
 (or 
 arXiv:2206.00186v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2206.00186
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Sergey Norin [view email] 
 [v1]
 Wed, 1 Jun 2022 02:15:41 UTC (8 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Dense minors of graphs with independence number two, by Sergey Norin and Paul Seymour
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
 | 2022-06
 

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
