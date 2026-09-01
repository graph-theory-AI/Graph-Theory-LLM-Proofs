Attack the following open graph-theory problem.

Catalog id: 2005.12861__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2005.12861__00/
Source paper: Finding an induced path that is not a shortest path (arXiv:2005.12861)

=== Extracted statement (catalog JSON) ===
Title: Question 1.5
For fixed $k > 1$, is there a polynomial-time algorithm that, given a graph $G$ and $u, v \in V(G)$, decides whether there is an induced $uv$-path $P$ in $G$ of length at least $d(u, v) + k$?

Context:
The paper's main result (Theorem 1.1) gives a polynomial-time algorithm for the case $k = 1$ (detecting any induced non-shortest path), and the authors note the algorithm can be adjusted for $k = 2$. The question remains open even for $k = 3$. Fixing $k$ is necessary, since Theorem 1.6 shows the problem is NP-hard when $k$ is part of the input (e.g., deciding whether there exists a $uv$-NSP of length at least $2d_G(u,v)$).

=== Catalog page (statement + literature review) ===
Polynomial algorithm for fixed-k induced detours — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Question 1.5 asks whether, for fixed k>1, there is a polynomial-time algorithm deciding if a graph G contains an induced uv-path of length at least d(u,v)+k. The source paper resolves k=1 (Theorem 1.1, running in O(n^18)) and notes the algorithm can be adjusted for k=2, leaving k≥3 explicitly open. A follow-up by Chiu and Lu (STACS 2022; Information and Computation 2024, arXiv:2109.15268) improves the k=1 algorithm to O(n^4.75) via Boolean matrix multiplication, but does not address the k≥3 case. No resolution of the k≥3 question was found in the indexed literature.

 Cited literature (1)

 
 
 
partial Blazing a Trail via Matrix Multiplications: A Faster Algorithm for Non-shortest Induced Paths
 (2024)
 

 
 Yung-Chung Chiu, Hsueh-I Lu · Information and Computation · arXiv:2109.15268

Improves the k=1 algorithm of Berger-Seymour-Spirkl from O(n^18) to O(n^4.75) using a poly-logarithmic number of n²×n² Boolean matrix multiplications; does not address Question 1.5 for k≥3.
 

 

 Reviewer notes. The k=1 case (any induced non-shortest uv-path) was settled by the source paper itself; k=2 is also handled by a minor adjustment of the same algorithm. The question is open for all k≥3. Chiu-Lu (2022/2024) is the only confirmed follow-up and concerns runtime improvement for k=1 only.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. For fixed $k > 1$, is there a polynomial-time algorithm that, given a graph $G$ and $u, v \in V(G)$, decides whether there is an induced $uv$-path $P$ in $G$ of length at least $d(u, v) + k$?

Context

The paper's main result (Theorem 1.1) gives a polynomial-time algorithm for the case $k = 1$ (detecting any induced non-shortest path), and the authors note the algorithm can be adjusted for $k = 2$. The question remains open even for $k = 3$. Fixing $k$ is necessary, since Theorem 1.6 shows the problem is NP-hard when $k$ is part of the input (e.g., deciding whether there exists a $uv$-NSP of length at least $2d_G(u,v)$).

Source paper

 Finding an induced path that is not a shortest path
 Eli Berger, Paul Seymour, Sophie Spirkl · 2020-05-26
 https://arxiv.org/abs/2005.12861
 PDF source

=== Source paper abstract / header ===
Abstract:We give a polynomial-time algorithm that, with input a graph $G$ and two vertices $u,v$ of $G$, decides whether there is an induced $uv$-path that is longer than the shortest $uv$-path.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2005.12861 [math.CO]
 

 
  
 (or 
 arXiv:2005.12861v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2005.12861
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Sophie Spirkl [view email] 
 [v1]
 Tue, 26 May 2020 16:44:28 UTC (9 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Finding an induced path that is not a shortest path, by Eli Berger and 2 other authors
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
 | 2020-05
 

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
