Attack the following open graph-theory problem.

Catalog id: 2602.16333__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2602.16333__01/
Source paper: Long cycles in vertex transitive digraphs (arXiv:2602.16333)

=== Catalog page (statement + literature review) ===
Circumference equivalence vertex transitive digraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 4.2 from arXiv:2602.16333 proposes that the minimum circumference of connected vertex transitive digraphs and undirected graphs on n vertices are asymptotically equivalent: d(n) = Θ(c(n)). The source paper establishes the first nontrivial lower bound Ω(n^{1/3}) for the directed case, while the best undirected bound stands at Ω(n^{9/14}) (improved to Ω(n^{13/21}) by Groenland et al., arXiv:2408.04618, predating this conjecture). No follow-up paper resolving or making further progress on the conjecture has been found in the three months since posting.

 Reviewer notes. No follow-up found. The conjecture is very recent (posted 2026-02-18, reviewed 2026-05-14). The gap between the directed bound Omega(n^{1/3}) and the undirected bound Omega(n^{9/14}) is the main motivation. The related undirected paper arXiv:2408.04618 (Groenland et al., 2024) improves the undirected bound to Omega(n^{13/21}) but predates the conjecture.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $c(n)$ denote the minimum circumference of a connected vertex transitive graph on $n$ vertices. Let $d(n)$ denote the minimum circumference of a connected vertex transitive digraph on $n$ vertices. Then $d(n)=\Theta(c(n))$.

Context

The paper's bound of $\Omega(n^{1/3})$ on the circumference of connected vertex transitive digraphs is slightly weaker than the best known $\Omega(n^{9/14})$ undirected bound. This conjecture asserts that the directed and undirected cases are asymptotically the same, proposed as a natural intermediate target.

Source paper

 Long cycles in vertex transitive digraphs
 Matija Bucić, Kevin Hendrey, Bojan Mohar, Raphael Steiner, Liana Yepremyan · 2026-02-18
 https://arxiv.org/abs/2602.16333

=== Source paper abstract / header ===
Abstract:One of the most well-known conjectures concerning Hamiltonicity in graphs asserts that any sufficiently large connected vertex transitive graph contains a Hamilton cycle. In this form, it was first written down by Thomassen in 1978, inspired by a closely related conjecture due to Lovász from 1969. It has been attributed to several other authors in a survey on the topic by Witte and Gallian in 1984.
The analogous question for vertex transitive digraphs has an even longer history, having been first considered by Rankin in 1946. It is arguably more natural from the group-theoretic perspective underlying this problem in both settings. Trotter and Erdős proved in 1978 that there are infinitely many connected vertex transitive digraphs which are not Hamiltonian. This left open the very natural question of how long a directed cycle one can guarantee in a connected vertex transitive digraph on $n$ vertices.
In 1981, Alspach asked if the maximum perimeter gap (the gap between the circumference and the order of the digraph) is a growing function in $n$. We answer this question in the affirmative, showing that it grows at least as fast as $(1-o(1)) \ln n$. On the other hand, we prove that one can always find a directed cycle of length at least $\Omega(n^{1/3})$, establishing the first lower bound growing with $n$, providing a directed analogue of a famous result of Babai from 1979 in the undirected setting.
 

 
 
 
 Comments:
 14 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C20, 05C38, 05C25, 05C45, 05C48, 05E18
 

 Cite as:
 arXiv:2602.16333 [math.CO]
 

 
  
 (or 
 arXiv:2602.16333v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2602.16333
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Wed, 18 Feb 2026 10:13:14 UTC (50 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Long cycles in vertex transitive digraphs, by Matija Buci\'c and 4 other authors
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
 | 2026-02
 

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
