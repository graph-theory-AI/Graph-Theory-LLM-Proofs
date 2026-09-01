Attack the following open graph-theory problem.

Catalog id: 2107.05995__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2107.05995__01/
Source paper: On the Hat Guessing Number of Graphs (arXiv:2107.05995)

=== Extracted statement (catalog JSON) ===
Title: Question on Typical Hat Guessing Number of G(n,1/2)
What is the typical asymptotic behavior of the hat guessing number of the random graph $G(n,1/2)$? In particular, is $\mathrm{HG}(G(n,1/2))$ equal to $o(n)$ with high probability?

Context:
The paper improves the known lower bound from $(2-o(1))\log_2 n$ to $n^{1-o(1)}$ with high probability, but the true order of growth remains unknown. The upper bound is $n$ trivially.

=== Catalog page (statement + literature review) ===
Hat guessing number growth in G(n,1/2) — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 A direct follow-up, arXiv:2302.04122 (2023), extends the n^{1-o(1)} lower bound from G(n,1/2) to all random graphs G(n,p) with constant edge probability p \in (0,1), and also establishes an upper bound of (1-o(1))n with high probability. These bounds narrow the gap but do not definitively resolve whether HG(G(n,1/2)) = o(n) holds with high probability, so the precise asymptotic order remains open.

 Cited literature (1)

 
 
 
partial The hat guessing number of random graphs with constant edge-chosen probability
 (2023)
 

 
 unknown (arXiv ID 2302.04122) · arXiv preprint · arXiv:2302.04122

Generalises the n^{1-o(1)} lower bound on HG(G(n,p)) to all constant p \in (0,1) and establishes a matching upper bound of (1-o(1))n with high probability, extending the results of Alon-Chizewer but leaving the question of whether HG = o(n) open.
 

 

 Reviewer notes. The follow-up paper 2302.04122 makes meaningful progress by generalising to all constant edge-probability p and tightening both bounds to n^{1-o(1)} <= HG(G(n,p)) <= (1-o(1))n. However, since n^{1-o(1)} is not necessarily o(n) (depending on the rate), and the upper bound is (1-o(1))n = Theta(n), the specific question 'is HG(G(n,1/2)) = o(n) with high probability?' remains unanswered. Authors of 2302.04122 could not be verified from available fetches.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. What is the typical asymptotic behavior of the hat guessing number of the random graph $G(n,1/2)$? In particular, is $\mathrm{HG}(G(n,1/2))$ equal to $o(n)$ with high probability?

Context

The paper improves the known lower bound from $(2-o(1))\log_2 n$ to $n^{1-o(1)}$ with high probability, but the true order of growth remains unknown. The upper bound is $n$ trivially.

Source paper

 On the Hat Guessing Number of Graphs
 Noga Alon, Jeremy Chizewer · 2021-07-21
 https://arxiv.org/abs/2107.05995
 PDF source

=== Source paper abstract / header ===
Abstract:The hat guessing number $HG(G)$ of a graph $G$ on $n$ vertices is defined in terms of the following game: $n$ players are placed on the $n$ vertices of $G$, each wearing a hat whose color is arbitrarily chosen from a set of $q$ possible colors. Each player can see the hat colors of his neighbors, but not his own hat color. All of the players are asked to guess their own hat colors simultaneously, according to a predetermined guessing strategy and the hat colors they see, where no communication between them is allowed. The hat guessing number $HG(G)$ is the largest integer $q$ such that there exists a guessing strategy guaranteeing at least one correct guess for any hat assignment of $q$ possible colors.
In this note we construct a planar graph $G$ satisfying $HG(G)=12$, settling a problem raised in \cite{BDFGM}. We also improve the known lower bound of $(2-o(1))\log_2 n$ for the typical hat guessing number of the random graph $G=G(n,1/2)$, showing that it is at least $n^{1-o(1)}$ with probability tending to $1$ as $n$ tends to infinity. Finally, we consider the linear hat guessing number of complete multipartite graphs.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C57
 

 Cite as:
 arXiv:2107.05995 [math.CO]
 

 
  
 (or 
 arXiv:2107.05995v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2107.05995
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Jeremy Chizewer [view email] 
 [v1]
 Tue, 13 Jul 2021 11:24:14 UTC (9 KB)

 [v2]
 Wed, 21 Jul 2021 17:28:03 UTC (9 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On the Hat Guessing Number of Graphs, by Noga Alon and Jeremy Chizewer
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
 | 2021-07
 

 Change to browse by:
 
 cs
 cs.DM
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
