Attack the following open graph-theory problem.

Catalog id: 2403.02298__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2403.02298__01/
Source paper: Minimum acyclic number and maximum dichromatic number of oriented trian… (arXiv:2403.02298)

=== Catalog page (statement + literature review) ===
Maximum dichromatic number of oriented triangle-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 4 from arXiv:2403.02298 asserts $\vec{t}(n)=\Theta\sqrt{n/\log n}$ for the maximum dichromatic number of oriented triangle-free graphs on $n$ vertices. The paper itself establishes an upper bound $\vec{t}(n)\leq(\sqrt{2}+o(1))\sqrt{n/\log n}$ and a lower bound $\vec{t}(n)\geq\frac{8}{107}\frac{\sqrt{n}}{\log n}$, leaving a $\sqrt{\log n}$ gap on the lower side. No follow-up paper closing this gap or otherwise resolving the conjecture was found in the indexed literature.

 Reviewer notes. No follow-up resolving Conjecture 4 was found. The conjecture follows from Conjecture 3 of the same paper (about $\vec{a}(n)$). The source paper has been published as Electronic Journal of Combinatorics vol. 32, issue 4, P4.27 (2025-11-03), URL https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i4p27. The paper arXiv:2511.20246 ('Acyclic dichromatic number of oriented graphs', Nov 2025) introduces a related but distinct parameter and does not address Conjecture 4.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. $\vec{t}(n)=\Theta\sqrt{\frac{n}{\log n}}$.

Context

Conjecture 4 follows from Conjecture 3, since $\vec{t}(n)\geq n/\vec{a}(n)$ and $\vec{t}(n)\leq t(n)$. The paper establishes $\frac{8}{107}\frac{\sqrt{n}}{\log n}\leq\vec{t}(n)\leq\left(\sqrt{2}+o(1)\right)\sqrt{\frac{n}{\log n}}$, leaving a logarithmic gap on the lower side.

Notes. The LaTeX in the source appears to be missing parentheses around the $\Theta$ argument; reproduced verbatim as given.

Source paper

 Minimum acyclic number and maximum dichromatic number of oriented triangle-free graphs of a given order
 Pierre Aboulker, Frédéric Havet, François Pirot, Juliette Schabanel · 2024-03-04
 https://arxiv.org/abs/2403.02298

=== Source paper abstract / header ===
Abstract:Let $D$ be a digraph. Its acyclic number $\vec{\alpha}(D)$ is the maximum order of an acyclic induced subdigraph and its dichromatic number $\vec{\chi}(D)$ is the least integer $k$ such that $V(D)$ can be partitioned into $k$ subsets inducing acyclic subdigraphs. We study ${\vec a}(n)$ and $\vec t(n)$ which are the minimum of $\vec\alpha(D)$ and the maximum of $\vec{\chi}(D)$, respectively, over all oriented triangle-free graphs of order $n$. For every $\epsilon>0$ and $n$ large enough, we show $(1/\sqrt{2} - \epsilon) \sqrt{n\log n} \leq \vec{a}(n) \leq \frac{107}{8} \sqrt n \log n$ and $\frac{8}{107} \sqrt n/\log n \leq \vec{t}(n) \leq (\sqrt 2 + \epsilon) \sqrt{n/\log n}$. We also construct an oriented triangle-free graph on 25 vertices with dichromatic number~3, and show that every oriented triangle-free graph of order at most 17 has dichromatic number at most 2.
 

 
 
 
 Comments:
 19 pages, 5 figures
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C20, 05C55
 

 Cite as:
 arXiv:2403.02298 [math.CO]
 

 
  
 (or 
 arXiv:2403.02298v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2403.02298
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Pierre Aboulker [view email] 
 [v1]
 Mon, 4 Mar 2024 18:29:12 UTC (1,276 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Minimum acyclic number and maximum dichromatic number of oriented triangle-free graphs of a given order, by Pierre Aboulker and 3 other authors
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
 | 2024-03
 

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
