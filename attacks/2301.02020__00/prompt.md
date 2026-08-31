Attack the following open graph-theory problem.

Catalog id: 2301.02020__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2301.02020__00/
Source paper: Extremal Independent Set Reconfiguration (arXiv:2301.02020)

=== Catalog page (statement + literature review) ===
Super-cubic diameter of 4-configuration graph — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 4 from arXiv:2301.02020 asserts $D(n,4) = n^{3-o(1)}$, i.e., the maximum diameter of the 4-independent-set reconfiguration graph on $n$ vertices is nearly cubic. The source paper (published in Electronic Journal of Combinatorics 2023) establishes the upper bound $D(n,4) = o(n^3)$ and the general lower bound $n^{2\lfloor k/3\rfloor}/e^{O_k(\sqrt{\log n})}$, which for $k=4$ gives only $\Omega(n^2/e^{O(\sqrt{\log n})})$, leaving a large gap. A comprehensive web search found no follow-up paper proving or disproving the conjecture.

 Reviewer notes. No follow-up found. The conjecture asks whether the 4-configuration graph can have super-quadratic (nearly cubic) diameter; the gap between the $\Omega(n^2/e^{O(\sqrt{\log n})})$ lower bound and $o(n^3)$ upper bound remains open. The paper was also published as Electronic Journal of Combinatorics, Volume 30, Issue 3 (2023), article P3.8.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. $D(n, 4) = n^{3-o(1)}$.

Context

The authors prove $D(n,3) = \Omega(n^2/e^{O(\sqrt{\log n})})$ and a general lower bound $D(n,k) = n^{2\lfloor k/3\rfloor}/e^{O_k(\sqrt{\log n})}$, but were unable to show that lower and upper bounds almost match for $k \geq 4$. In particular, it is open whether the 4-configuration graph can have super-quadratic diameter, while the upper bound is $o(n^3)$.

Source paper

 Extremal Independent Set Reconfiguration
 Nicolas Bousquet, Bastien Durain, Théo Pierron, Stéphan Thomassé · 2023-01-05
 https://arxiv.org/abs/2301.02020
 PDF source

=== Source paper abstract / header ===
Abstract:The independent set reconfiguration problem asks whether one can transform one given independent set of a graph into another, by changing vertices one by one in such a way the intermediate sets remain independent. Extremal problems on independent sets are widely studied: for example, it is well known that an $n$-vertex graph has at most $3^{n/3}$ maximum independent sets (and this is tight). This paper investigates the asymptotic behavior of maximum possible length of a shortest reconfiguration sequence for independent sets of size $k$ among all $n$-vertex graphs. We give a tight bound for $k=2$. We also provide a subquadratic upper bound (using the hypergraph removal lemma) as well as an almost tight construction for $k=3$. We generalize our results for larger values of $k$ by proving an $n^{2\lfloor k/3 \rfloor}$ lower bound.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C35, 05C69
 

 Cite as:
 arXiv:2301.02020 [math.CO]
 

 
  
 (or 
 arXiv:2301.02020v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2301.02020
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Théo Pierron [view email] 
 [v1]
 Thu, 5 Jan 2023 11:38:30 UTC (51 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Extremal Independent Set Reconfiguration, by Nicolas Bousquet and 3 other authors
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
 | 2023-01
 

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
