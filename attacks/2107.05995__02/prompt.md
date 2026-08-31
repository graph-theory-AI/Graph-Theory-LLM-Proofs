Attack the following open graph-theory problem.

Catalog id: 2107.05995__02
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2107.05995__02/
Source paper: On the Hat Guessing Number of Graphs (arXiv:2107.05995)

=== Catalog page (statement + literature review) ===
Hat guessing number under universal vertex addition — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No follow-up paper was found that establishes a general upper bound for HG(G') in terms of HG(G) when G' is obtained by adding a universal vertex to G, nor one that proves no such function exists. The source paper itself shows the gap can be large (HG(G') can reach q^2+q where q = HG(G)), so any bounding function must grow at least quadratically. Searches across arXiv and related literature on hat guessing numbers (including papers on degenerate graphs, random graphs, and proper colorings) found no subsequent resolution of this specific problem as of May 2026.

 Reviewer notes. No follow-up found in 5 web calls. The problem dates from 2021; absence of resolution after ~5 years lowers confidence slightly below high. Related active literature (degenerate graphs, random graphs, proper colorings) does not address the universal vertex addition problem. The lower bound q^2 <= HG(G') is implicit in the source paper via the G_d(N) construction.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Establish an upper bound for $\mathrm{HG}(G')$ as a function of $\mathrm{HG}(G)$, where $G'$ is obtained from $G$ by adding a single vertex connected to all vertices of $G$, or show that no such function exists.

Context

Using the graphs $G_d(N)$ from [10], the authors show that for arbitrarily large $q = \mathrm{HG}(G)$ the hat guessing number of $G'$ can exceed $q^2$ (specifically reaching $q^2+q$), so adding a universal vertex can dramatically increase the hat guessing number.

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
