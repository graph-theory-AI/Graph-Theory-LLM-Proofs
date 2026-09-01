Attack the following open graph-theory problem.

Catalog id: 1510.06964__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1510.06964__00/
Source paper: On a conjecture of Mohar concerning Kempe equivalence of regular graphs (arXiv:1510.06964)

=== Extracted statement (catalog JSON) ===
Title: Open case: WSK algorithm on the triangular lattice for q=5
Determine whether the Wang-Swendsen-Koteck\'{y} algorithm for $q = 5$ colourings of the triangular lattice (with periodic boundary conditions) is valid (i.e., whether the set of $5$-colourings of the triangular lattice is a Kempe class).

Context:
Theorem 2.2 establishes that the WSK algorithm on the triangular lattice is valid for $q \geq 6$ (via Theorem 1.1 and a degeneracy lemma) and invalid for $q \leq 4$ (Mohar and Salas). The authors explicitly note that $q = 5$ is the single remaining open case.

=== Catalog page (statement + literature review) ===
WSK validity for 5-colorings of triangular lattice — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The question of whether all 5-colourings of the triangular lattice (with periodic boundary conditions) form a single Kempe class — equivalently whether the WSK algorithm is ergodic for q=5 — was explicitly left open in arXiv:1510.06964. A 2022 preprint by Salas and Sokal (arXiv:2206.13126) proves WSK ergodicity for q≥5 on Eulerian triangulations of the torus satisfying certain structural conditions; since the triangular lattice is a 6-regular Eulerian triangulation of the torus, this is a significant adjacent result, but the abstract does not explicitly confirm that the standard triangular lattice satisfies the paper's conditions for q=5. No paper was found that unambiguously and completely settles the conjecture.

 Cited literature (1)

 
 
 
partial Ergodicity of the Wang--Swendsen--Kotecký algorithm on several classes of lattices on the torus
 (2022)
 

 
 Jesús Salas, Alan D. Sokal · arXiv preprint · arXiv:2206.13126

Proves WSK ergodicity for q≥5 on Eulerian triangulations of the torus meeting certain structural conditions, an adjacent result that may encompass the standard triangular lattice but does not explicitly confirm it.
 

 

 Reviewer notes. arXiv:2206.13126 (Salas--Sokal 2022) is the most relevant post-2016 paper found; it establishes WSK ergodicity for q≥5 on Eulerian triangulations under certain conditions. The triangular lattice is 6-regular and Eulerian, making it a natural candidate, but the WebFetch of the abstract indicated the triangular lattice is not explicitly mentioned as a covered case. No separate paper resolving the q=5 triangular lattice case was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Determine whether the Wang-Swendsen-Koteck\'{y} algorithm for $q = 5$ colourings of the triangular lattice (with periodic boundary conditions) is valid (i.e., whether the set of $5$-colourings of the triangular lattice is a Kempe class).

Context

Theorem 2.2 establishes that the WSK algorithm on the triangular lattice is valid for $q \geq 6$ (via Theorem 1.1 and a degeneracy lemma) and invalid for $q \leq 4$ (Mohar and Salas). The authors explicitly note that $q = 5$ is the single remaining open case.

Notes. Stated as an observation ('We observe that this leaves the single open case of a triangular lattice with q = 5') rather than in a formal labelled environment.

Source paper

 On a conjecture of Mohar concerning Kempe equivalence of regular graphs
 Marthe Bonamy, Nicolas Bousquet, Carl Feghali, Matthew Johnson · 2016-09-22
 https://arxiv.org/abs/1510.06964
 PDF source

=== Source paper abstract / header ===
Abstract:Let $G$ be a graph with a vertex colouring $\alpha$. Let $a$ and $b$ be two colours. Then a connected component of the subgraph induced by those vertices coloured either $a$ or $b$ is known as a Kempe chain. A colouring of $G$ obtained from $\alpha$ by swapping the colours on the vertices of a Kempe chain is said to have been obtained by a Kempe change. Two colourings of $G$ are Kempe equivalent if one can be obtained from the other by a sequence of Kempe changes.
A conjecture of Mohar (2007) asserts that, for $k \geq 3$, all $k$-colourings of a $k$-regular graph that is not complete are Kempe equivalent. It was later shown that all $3$-colourings of a cubic graph that is neither $K_4$ nor the triangular prism are Kempe equivalent. In this paper, we prove that the conjecture holds for each $k\geq 4$. We also report the implications of this result on the validity of the Wang-Swendsen-Kotecký algorithm for the antiferromagnetic Potts model at zero-temperature.
 

 
 
 
 Comments:
 corrected typos, tidied references, added figures; added section on Wang-Swendsen-Kotecky algorithm
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1510.06964 [cs.DM]
 

 
  
 (or 
 arXiv:1510.06964v3 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1510.06964
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Matthew Johnson [view email] 
 [v1]
 Fri, 23 Oct 2015 15:06:51 UTC (17 KB)

 [v2]
 Thu, 3 Dec 2015 19:40:48 UTC (18 KB)

 [v3]
 Thu, 22 Sep 2016 16:24:28 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On a conjecture of Mohar concerning Kempe equivalence of regular graphs, by Marthe Bonamy and Nicolas Bousquet and Carl Feghali and Matthew Johnson
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
 | 2015-10
 

 Change to browse by:
 
 cs
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Marthe Bonamy
Nicolas Bousquet
Carl Feghali
Matthew Johnson 

 

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
