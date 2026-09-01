Attack the following open graph-theory problem.

Catalog id: 2511.03864__01
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2511.03864__01/
Source paper: Induced matching treewidth and tree-independence number, revisited (arXiv:2511.03864)

=== Extracted statement (catalog JSON) ===
Title: Question 5.3
Is it true that for classes of graphs with bounded induced matching treewidth, tree-independence number is bounded from above by a polynomial function of the induced biclique number?

Context:
The induced biclique number of $G$ is the largest nonnegative integer $t$ such that $G$ contains an induced subgraph isomorphic to $K_{t,t}$. This question is an equivalent restatement of Question 5.2 using the induced biclique number, and is noted as closely related to recent work bounding tree-independence number in terms of clique-like parameters.

=== Catalog page (statement + literature review) ===
Tree-independence number via induced biclique number — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The source paper (arXiv:2511.03864) itself establishes the main partial result: for any K_{t,t}-free graph class, tree-independence number and induced matching treewidth are polynomially related via the Kövári–Sós–Turán theorem, improving the exponential bound of Abrishami et al. (arXiv:2405.04617). Question 5.3 asks whether this polynomial relationship holds in full generality—bounding tree-independence number by a polynomial in both induced matching treewidth and the induced biclique number—without assuming K_{t,t}-freeness a priori. No follow-up paper resolving this question was found in the literature as of May 2026.

 Reviewer notes. No follow-up resolving Question 5.3 was found. The conjecture is equivalent to Question 5.2 (as stated in the paper) and was posted in November 2025; absence of resolution after a wide search gives high confidence it remains open. A related 2026 paper (arXiv:2604.01999) studies tree-independence number for graphs excluding a 6-vertex path and a (2,t)-biclique, but addresses a different conjecture. The paper arXiv:2405.04617 (Abrishami et al., SIAM JDM 2025) proved the qualitative boundedness result with an exponential bound, predating the source paper.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. Is it true that for classes of graphs with bounded induced matching treewidth, tree-independence number is bounded from above by a polynomial function of the induced biclique number?

Context

The induced biclique number of $G$ is the largest nonnegative integer $t$ such that $G$ contains an induced subgraph isomorphic to $K_{t,t}$. This question is an equivalent restatement of Question 5.2 using the induced biclique number, and is noted as closely related to recent work bounding tree-independence number in terms of clique-like parameters.

Notes. Explicitly stated by the authors to be equivalent to Question 5.2.

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
