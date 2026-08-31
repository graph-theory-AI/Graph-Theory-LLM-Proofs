Attack the following open graph-theory problem.

Catalog id: 2001.03794__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2001.03794__00/
Source paper: Grundy Coloring & friends, Half-Graphs, Bicliques (arXiv:2001.03794)

=== Catalog page (statement + literature review) ===
FPT on H_{t,t}-free graphs for Grundy Coloring — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The question of whether Grundy Coloring and b-Chromatic Core are FPT on $H_{t,t}$-free graphs (parameterized by $k$) was explicitly left open in the source paper and remains unresolved as of 2026. A STACS 2025 paper (arXiv:2410.20629) establishes FPT for Grundy Coloring on $K_{i,j}$-free graphs and for Partial Grundy Coloring on general graphs, advancing the broader parameterized landscape for greedy coloring problems, but does not directly address the $H_{t,t}$-free case. No paper resolving or disproving the conjecture was found.

 Cited literature (1)

 
 
 
partial Parameterized Saga of First-Fit and Last-Fit Coloring
 (2025)
 

 
 not confirmed in fetch · STACS 2025 (LIPIcs, vol. 327) · arXiv:2410.20629 · doi:10.4230/LIPIcs.STACS.2025.5

Proves FPT algorithms for Partial Grundy Coloring on general graphs and for Grundy Coloring on $K_{i,j}$-free graphs, the closest known advance to the $H_{t,t}$-free question, but the $H_{t,t}$-free case is not settled.
 

 

 Reviewer notes. The source paper already achieves FPT on $K_{t,t}$-free graphs for b-Chromatic Core and Partial Grundy Coloring; the open question is whether excluding $H_{t,t}$ (the half-graph, which drives the W[1]-hardness construction) suffices to give FPT for the full Grundy Coloring and b-Chromatic Core. The key combinatorial lemma for $K_{t,t}$-free graphs was shown to collapse on $H_{t,t}$-free graphs. The STACS 2025 result on $K_{i,j}$-free graphs is the closest known related progress but does not directly resolve the conjecture. No follow-up resolving or disproving the $H_{t,t}$-free case was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Are \textsc{Grundy Coloring} and \textsc{b-Chromatic Core} fixed-parameter tractable on $H_{t,t}$-free graphs when parameterized by $k$?

Context

The W[1]-hardness constructions for both problems rely heavily on large half-graphs as color-propagation units; excluding large half-graphs may restore tractability. However, the key combinatorial lemma that gives FPT on $K_{t,t}$-free graphs collapses on $H_{t,t}$-free graphs, so the question is explicitly left open.

Notes. Stated as an explicit open problem in the 'Limits and further questions' section; no formal numbered theorem environment.

Source paper

 Grundy Coloring & friends, Half-Graphs, Bicliques
 Pierre Aboulker, Édouard Bonnet, Eun Jung Kim, Florian Sikora · 2020-01-11
 https://arxiv.org/abs/2001.03794
 PDF source

=== Source paper abstract / header ===
Abstract:The first-fit coloring is a heuristic that assigns to each vertex, arriving in a specified order $\sigma$, the smallest available color. The problem Grundy Coloring asks how many colors are needed for the most adversarial vertex ordering $\sigma$, i.e., the maximum number of colors that the first-fit coloring requires over all possible vertex orderings. Since its inception by Grundy in 1939, Grundy Coloring has been examined for its structural and algorithmic aspects. A brute-force $f(k)n^{2^{k-1}}$-time algorithm for Grundy Coloring on general graphs is not difficult to obtain, where $k$ is the number of colors required by the most adversarial vertex ordering. It was asked several times whether the dependency on $k$ in the exponent of $n$ can be avoided or reduced, and its answer seemed elusive until now. We prove that Grundy Coloring is W[1]-hard and the brute-force algorithm is essentially optimal under the Exponential Time Hypothesis, thus settling this question by the negative.
The key ingredient in our W[1]-hardness proof is to use so-called half-graphs as a building block to transmit a color from one vertex to another. Leveraging the half-graphs, we also prove that b-Chromatic Core is W[1]-hard, whose parameterized complexity was posed as an open question by Panolan et al. [JCSS '17]. A natural follow-up question is, how the parameterized complexity changes in the absence of (large) half-graphs. We establish fixed-parameter tractability on $K_{t,t}$-free graphs for b-Chromatic Core and Partial Grundy Coloring, making a step toward answering this question. The key combinatorial lemma underlying the tractability result might be of independent interest.
 

 
 
 
 Comments:
 25 pages, 5 figures
 

 Subjects:
 
 Computational Complexity (cs.CC); Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Combinatorics (math.CO)
 
 
 MSC classes:
 68W05
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2001.03794 [cs.CC]
 

 
  
 (or 
 arXiv:2001.03794v1 [cs.CC] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2001.03794
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Sat, 11 Jan 2020 20:17:11 UTC (104 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Grundy Coloring & friends, Half-Graphs, Bicliques, by Pierre Aboulker and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.CC

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2020-01
 

 Change to browse by:
 
 cs
 cs.DM
 cs.DS
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Pierre Aboulker
Édouard Bonnet
Eun Jung Kim
Florian Sikora 

 

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
