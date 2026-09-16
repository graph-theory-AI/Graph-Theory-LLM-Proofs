Attack the following open graph-theory problem.

Catalog id: 1908.06300__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1908.06300__00/
Source paper: The stable set problem in graphs with bounded genus and bounded odd cyc… (arXiv:1908.06300)

=== Extracted statement (catalog JSON) ===
Title: Conjecture on polynomial-time solvability of bounded sub-determinant integer programs
Integer programs with bounded sub-determinants can be solved in polynomial time. In particular, the stable set problem on graphs with $\mathrm{ocp}(G) \leq k$ is polynomial for every fixed $k$.

Context:
The authors note that recent work links the complexity of integer programs to the magnitude of their sub-determinants, and that it is tempting to believe bounded sub-determinant integer programs are polynomial-time solvable. This would imply the stable set problem is polynomial for every fixed bound $k$ on the odd cycle packing number, which remains open for $k \geq 2$.

=== Catalog page (statement + literature review) ===
Polynomial-time bounded sub-determinant integer programs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture has two components: the general claim that all bounded sub-determinant integer programs are polynomial-time solvable, and the specific claim that the stable set problem is polynomial for every fixed odd cycle packing bound $k$. The latter was settled by arXiv:2106.05947 (FOCS 2021), which gives the first polynomial-time algorithm for the weighted stable set problem on graphs with at most $k$ vertex-disjoint odd cycles for any constant $k$, extending the previously known cases $k=0$ (bipartite) and $k=1$. The broader claim about all bounded sub-determinant IPs remains open in full generality; known positive results cover bimodular matrices and matrices with at most two nonzero entries per row.

 Cited literature (1)

 
 
 
partial Integer programs with bounded subdeterminants and two nonzeros per row
 (2021)
 

 
 authors unverified; see arXiv:2106.05947 · Proceedings of the 2021 IEEE 62nd Annual Symposium on Foundations of Computer Science (FOCS), pages 13-24 · arXiv:2106.05947

Proves the first polynomial-time algorithm for the weighted stable set problem on graphs with at most k vertex-disjoint odd cycles (any constant k), thereby resolving the graph-theoretic 'in particular' part of the conjecture; the general bounded sub-determinant IP claim is addressed only for coefficient matrices with at most two nonzero entries per row.
 

 

 Reviewer notes. The 'in particular' part of the conjecture (stable set polynomial for every fixed ocp bound k) is proved by arXiv:2106.05947 (FOCS 2021). The broader conjecture that all bounded sub-determinant IPs are polynomial remains open; partial progress includes bimodular matrices (Artmann-Weismantel-Zenklusen, STOC 2017) and matrices with two nonzeros per row (arXiv:2106.05947). Authors of 2106.05947 could not be confirmed from fetched abstract content; the URL was verified via two WebFetch calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Integer programs with bounded sub-determinants can be solved in polynomial time. In particular, the stable set problem on graphs with $\mathrm{ocp}(G) \leq k$ is polynomial for every fixed $k$.

Context

The authors note that recent work links the complexity of integer programs to the magnitude of their sub-determinants, and that it is tempting to believe bounded sub-determinant integer programs are polynomial-time solvable. This would imply the stable set problem is polynomial for every fixed bound $k$ on the odd cycle packing number, which remains open for $k \geq 2$.

Notes. Stated as 'it is tempting to believe'; the paper explicitly confirms the problem is open for $k \geq 2$. No labelled theorem environment.

Source paper

 The stable set problem in graphs with bounded genus and bounded odd cycle packing number
 Michele Conforti, Samuel Fiorin, Tony Huynh, Gwenaël Joret, Stefan Weltge · 2019-08-17
 https://arxiv.org/abs/1908.06300
 PDF source

Related conjectures

 
 implies
 Stable set for bounded ocp, unbounded genus
 open
 The source's explicit 'in particular' clause asserts polynomial-time stable set for ALL graphs with ocp(G) <= k, for every fixed k. Since every finite graph embeds in a surface of some Euler genus, 'graphs of arbitrary Euler genus with ocp <= k' is exactly the class of all graphs with ocp <= k; the target is therefore an instance (indeed a restatement) of the source's second clause, and the full source is strictly stronger since it also asserts polynomial solvability of all bounded sub-determinant IPs. Hypothesis-class containment is trivial and the direction is correct.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:Consider the family of graphs without $ k $ node-disjoint odd cycles, where $ k $ is a constant. Determining the complexity of the stable set problem for such graphs $ G $ is a long-standing problem. We give a polynomial-time algorithm for the case that $ G $ can be further embedded in a (possibly non-orientable) surface of bounded genus. Moreover, we obtain polynomial-size extended formulations for the respective stable set polytopes.
To this end, we show that $2$-sided odd cycles satisfy the Erdős-Pósa property in graphs embedded in a fixed surface. This extends the fact that odd cycles satisfy the Erdős-Pósa property in graphs embedded in a fixed orientable surface (Kawarabayashi & Nakamoto, 2007).
Eventually, our findings allow us to reduce the original problem to the problem of finding a minimum-cost non-negative integer circulation of a certain homology class, which turns out to be efficiently solvable in our case.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Combinatorics (math.CO); Optimization and Control (math.OC)
 

 Cite as:
 arXiv:1908.06300 [cs.DM]
 

 
  
 (or 
 arXiv:1908.06300v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1908.06300
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Stefan Weltge [view email] 
 [v1]
 Sat, 17 Aug 2019 13:10:18 UTC (46 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The stable set problem in graphs with bounded genus and bounded odd cycle packing number, by Michele Conforti and 4 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DM

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2019-08
 

 Change to browse by:
 
 cs
 cs.DS
 math
 math.CO
 math.OC
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Michele Conforti
Samuel Fiorini
Tony Huynh
Gwenaël Joret
Stefan Weltge 

 

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
