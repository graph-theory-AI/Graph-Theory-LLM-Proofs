Attack the following open graph-theory problem.

Catalog id: 1812.02420__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1812.02420__00/
Source paper: On the Complexity of Digraph Colourings and Vertex Arboricity (arXiv:1812.02420)

=== Extracted statement (catalog JSON) ===
Title: Problem 2.15
Let $F$ be a fixed (multi-)digraph. Instance: A (multi-)digraph $D$. Decide whether $D$ is circularly $F$-colourable.

Context:
A digraph $D$ is circularly $F$-colourable if there exists a circular homomorphism from $D$ to $F$. This problem generalises Problem 1 and serves as a directed analogue of the $H$-colouring problem for graphs. Conjecture 2.16 asserts that NP-completeness holds whenever $F$ contains a directed cycle, and Theorem 2.17 establishes this for almost all such cases.

=== Catalog page (statement + literature review) ===
Circular F-colourability complexity dichotomy — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Problem 2.15 asks for the complexity of deciding circular F-colourability for a fixed digraph F. Conjecture 2.16 (stated in the same paper) asserts this problem is NP-complete whenever F contains a directed cycle. Theorem 2.17 of the source paper already establishes NP-completeness for almost all such F: specifically for digon-free digraphs with directed cycles, digraphs whose symmetric part contains an odd cycle, and 2-colourable digraphs. The remaining open case is digraphs F that contain a directed cycle whose symmetric part is non-empty and bipartite. No external follow-up paper resolving the full conjecture was found in the literature.

 Reviewer notes. The source paper (arXiv:1812.02420, published DMTCS 2020) itself partially resolves the conjecture via Theorem 2.17, proving NP-completeness for three broad families of F. The open subcase involves digraphs F with a directed cycle and a non-empty bipartite symmetric part. No follow-up paper fully resolving Problem 2.15 / Conjecture 2.16 was found after 4 web searches and targeted fetches.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Let $F$ be a fixed (multi-)digraph. Instance: A (multi-)digraph $D$. Decide whether $D$ is circularly $F$-colourable.

Context

A digraph $D$ is circularly $F$-colourable if there exists a circular homomorphism from $D$ to $F$. This problem generalises Problem 1 and serves as a directed analogue of the $H$-colouring problem for graphs. Conjecture 2.16 asserts that NP-completeness holds whenever $F$ contains a directed cycle, and Theorem 2.17 establishes this for almost all such cases.

Notes. The complete dichotomy (all F with a directed cycle) is conjectured but not fully proved within the paper.

Source paper

 On the Complexity of Digraph Colourings and Vertex Arboricity
 Winfried Hochstättler, Felix Schröder, Raphael Steiner · 2020-01-09
 https://arxiv.org/abs/1812.02420

=== Source paper abstract / header ===
Abstract:It has been shown by Bokal et al. that deciding 2-colourability of digraphs is an NP-complete problem. This result was later on extended by Feder et al. to prove that deciding whether a digraph has a circular $p$-colouring is NP-complete for all rational $p>1$. In this paper, we consider the complexity of corresponding decision problems for related notions of fractional colourings for digraphs and graphs, including the star dichromatic number, the fractional dichromatic number and the circular vertex arboricity. We prove the following results:
Deciding if the star dichromatic number of a digraph is at most $p$ is NP-complete for every rational $p>1$.
Deciding if the fractional dichromatic number of a digraph is at most $p$ is NP-complete for every $p>1, p \neq 2$.
Deciding if the circular vertex arboricity of a graph is at most $p$ is NP-complete for every rational $p>1$.
To show these results, different techniques are required in each case. In order to prove the first result, we relate the star dichromatic number to a new notion of homomorphisms between digraphs, called circular homomorphisms, which might be of independent interest. We provide a classification of the computational complexities of the corresponding homomorphism colouring problems similar to the one derived by Feder et al. for acyclic homomorphisms.
 

 
 
 
 Comments:
 21 pages, 1 figure
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1812.02420 [math.CO]
 

 
  
 (or 
 arXiv:1812.02420v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1812.02420
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Mathematics & Theoretical Computer Science, vol. 22 no. 1, Graph Theory (January 21, 2020) dmtcs:5140
 

 
 
 Related DOI:
 
 https://doi.org/10.23638/DMTCS-22-1-4

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Thu, 6 Dec 2018 09:33:41 UTC (21 KB)

 [v2]
 Mon, 28 Jan 2019 21:17:07 UTC (27 KB)

 [v3]
 Wed, 11 Dec 2019 21:54:34 UTC (32 KB)

 [v4]
 Thu, 9 Jan 2020 13:07:09 UTC (32 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On the Complexity of Digraph Colourings and Vertex Arboricity, by Winfried Hochst\"attler and 2 other authors
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
 | 2018-12
 

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
