Attack the following open graph-theory problem.

Catalog id: 2301.02020__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2301.02020__01/
Source paper: Extremal Independent Set Reconfiguration (arXiv:2301.02020)

=== Extracted statement (catalog JSON) ===
Title: Question 8
What is the asymptotic behavior of $\max_k D(n, k)$?

Context:
The authors prove that for every $n$ and every $k$ with $3n/10 \leq k \leq 2n/5$, $D(n,k) = \Omega(2^{n/5})$, and remark that it is quite surprising that this exponential lower bound holds for such a wide range of values of $k$.

=== Catalog page (statement + literature review) ===
Maximum D(n,k) asymptotics in IS reconfiguration — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The source paper establishes D(n,k) = Ω(2^{n/5}) for the range 3n/10 ≤ k ≤ 2n/5, giving an exponential lower bound on max_k D(n,k), and leaves the precise asymptotics as Question 8. No follow-up paper resolving or improving this asymptotic question was found in searches covering arXiv and published literature through May 2026.

 Reviewer notes. No follow-up work addressing the asymptotic behavior of max_k D(n,k) was found. The source paper itself is the state of the art: it proves the exponential lower bound D(n,k) = Ω(2^{n/5}) for k in [3n/10, 2n/5], which implies max_k D(n,k) grows at least exponentially in n, but the exact asymptotic (upper and matching lower bound) remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. What is the asymptotic behavior of $\max_k D(n, k)$?

Context

The authors prove that for every $n$ and every $k$ with $3n/10 \leq k \leq 2n/5$, $D(n,k) = \Omega(2^{n/5})$, and remark that it is quite surprising that this exponential lower bound holds for such a wide range of values of $k$.

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
