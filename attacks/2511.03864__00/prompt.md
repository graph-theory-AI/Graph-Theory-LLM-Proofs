Attack the following open graph-theory problem.

Catalog id: 2511.03864__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2511.03864__00/
Source paper: Induced matching treewidth and tree-independence number, revisited (arXiv:2511.03864)

=== Catalog page (statement + literature review) ===
Polynomial tree-α bound in K_{t,t}-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Question 5.2 is left open in the source paper arXiv:2511.03864. The paper's main result (Theorem 1.2) establishes tree-α(G) = O_t(μ^{3t²+1}) for K_{t,t}-free graphs with tree-μ(G) ≤ μ, giving a polynomial bound in μ for fixed t; however, Question 5.2 asks for the reverse direction: a polynomial bound in t for fixed μ. Lemma 5.1 of the paper shows the existing bound involves N(s,s,2) which is exponential in s, motivating the question, but does not rule out a polynomial in t for fixed μ. No follow-up paper resolving this question was found in the indexed literature in the six months since posting.

 Reviewer notes. The paper was posted November 2025 and Question 5.2 is explicitly left open. The main theorem gives tree-α(G) = O_t(μ^{3t²+1}), a polynomial in μ (for fixed t) but with t-dependent exponent, so it does not answer Question 5.2. No follow-up resolving this specific question was found after 5 web calls; the conjecture is open with high confidence given its recency.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. Is is true that for every positive integer $\mu$ there exists a polynomial $\mathsf{p}_{\mu}$ such that every $K_{t,t}$-free graph $G$ with $\operatorname{tree\textnormal{-}\mu}(G)\leqslant\mu$ satisfies $\operatorname{tree\textnormal{-}\alpha}(G)\leqslant\mathsf{p}_{\mu}(t)$?

Context

Lemma 5.1 shows that the smallest integer $\mathsf{N}(s,s,2)$ appearing in the bound from Abrishami et al. is not bounded by any polynomial in both parameters, motivating the question of whether a polynomial bound in $t$ alone (for fixed $\mu$) is achievable. The question asks specifically whether tree-independence number can be bounded polynomially in the induced biclique exclusion parameter $t$ for graphs of bounded induced matching treewidth.

Also stated in

 
Induced matching treewidth and tree-independence number, revisited (2025-11-05) 

Source paper

 Induced matching treewidth and tree-independence number, revisited
 Noga Alon, Martin Milanič, Paweł Rzążewski · 2025-11-05
 https://arxiv.org/abs/2511.03864

=== Source paper abstract / header ===
Abstract:We study two graph parameters defined via tree decompositions: tree-independence number and induced matching treewidth. Both parameters are defined similarly as treewidth, but with respect to different measures of a tree decomposition $\mathcal{T}$ of a graph $G$: for tree-independence number, the measure is the maximum size of an independent set in $G$ included in some bag of $\mathcal{T}$, while for the induced matching treewidth, the measure is the maximum size of an induced matching in $G$ such that some bag of $\mathcal{T}$ contains at least one endpoint of every edge of the matching.
While the induced matching treewidth of any graph is bounded from above by its tree-independence number, the family of complete bipartite graphs shows that small induced matching treewidth does not imply small tree-independence number. On the other hand, Abrishami, Briański, Czyżewska, McCarty, Milanič, Rzążewski, and Walczak~[SIAM Journal on Discrete Mathematics, 2025] showed that, if a fixed biclique $K_{t,t}$ is excluded as an induced subgraph, then the tree-independence number is bounded from above by some function of the induced matching treewidth. The function resulting from their proof is exponential even for fixed $t$, as it relies on multiple applications of Ramsey's theorem. In this note we show, using the Kövári-Sós-Turán theorem, that for any class of $K_{t,t}$-free graphs, the two parameters are in fact polynomially related.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2511.03864 [cs.DM]
 

 
  
 (or 
 arXiv:2511.03864v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2511.03864
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Paweł Rzążewski [view email] 
 [v1]
 Wed, 5 Nov 2025 21:09:44 UTC (15 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Induced matching treewidth and tree-independence number, revisited, by Noga Alon and Martin Milani\v{c} and Pawe{\l} Rz\k{a}\.zewski
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
 | 2025-11
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
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
