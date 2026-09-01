Attack the following open graph-theory problem.

Catalog id: 1803.10962__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1803.10962__00/
Source paper: Single-conflict colouring (arXiv:1803.10962)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 3
There exist $C, C' > 0$ such that, for any simple graph $G$ that is embeddable on a surface of Euler genus $g$, if every edge is assigned at most $Ck$ conflicts from $[k]^2$, then $G$ is conflict $k$-colourable, provided $k \geq C'\sqrt{g}$.

Context:
Theorem 1 gives an upper bound of the form $\chi_=(G) = O(\sqrt{g}\log g)$ in the $\mu = \Theta(\sqrt{g})$ regime, evocative of Heawood's bound. The authors note that $C < 1/2$ is forced by their second instructive example, and that a previous version of the manuscript incorrectly conjectured $C$ could be taken arbitrarily close to 1.

=== Catalog page (statement + literature review) ===
Conflict k-colouring on surfaces of genus g — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 3 from arXiv:1803.10962 asserts a Heawood-type threshold for single-conflict colouring on surfaces: conflict k-colourability holds for graphs on a surface of Euler genus g when k ≥ C'√g and each edge carries at most Ck conflicts. The source paper itself establishes an O(√g log g) upper bound in this regime, leaving a logarithmic gap. A follow-up by Bradshaw and Masařík (arXiv:2112.06333, JGT 2025) resolves a separate question from the same paper concerning degenerate graphs but does not address Conjecture 3 for surfaces. No resolution of Conjecture 3 was found in the indexed literature.

 Cited literature (1)

 
 
 
partial Single-conflict colorings of degenerate graphs
 (2025)
 

 
 Peter Bradshaw, Tomáš Masařík · Journal of Graph Theory · arXiv:2112.06333

Proves χ≠(G) = O(√d log n) for simple d-degenerate graphs, answering Question 1.5 of Dvořák–Esperet–Kang–Ozeki, but does not address Conjecture 3 about graphs embeddable on surfaces.
 

 

 Reviewer notes. Conjecture 3 was adjusted in v2 of the source paper (October 2020); the surrounding context specifies that C < 1/2 is forced by an instructive example, and a previous version incorrectly allowed C arbitrarily close to 1. The Bradshaw–Masařík paper (2112.06333) is the only confirmed post-2020 follow-up to the source paper, but it targets a different open problem (degenerate graphs). No paper resolving the surface-specific Conjecture 3 was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There exist $C, C' > 0$ such that, for any simple graph $G$ that is embeddable on a surface of Euler genus $g$, if every edge is assigned at most $Ck$ conflicts from $[k]^2$, then $G$ is conflict $k$-colourable, provided $k \geq C'\sqrt{g}$.

Context

Theorem 1 gives an upper bound of the form $\chi_=(G) = O(\sqrt{g}\log g)$ in the $\mu = \Theta(\sqrt{g})$ regime, evocative of Heawood's bound. The authors note that $C < 1/2$ is forced by their second instructive example, and that a previous version of the manuscript incorrectly conjectured $C$ could be taken arbitrarily close to 1.

Source paper

 Single-conflict colouring
 Zdeněk Dvořák, Louis Esperet, Ross J. Kang, Kenta Ozeki · 2020-10-09
 https://arxiv.org/abs/1803.10962
 PDF source

=== Source paper abstract / header ===
Abstract:Given a multigraph, suppose that each vertex is given a local assignment of $k$ colours to its incident edges. We are interested in whether there is a choice of one local colour per vertex such that no edge has both of its local colours chosen. The least $k$ for which this is always possible given any set of local assignments we call the {\em single-conflict chromatic number} of the graph. This parameter is closely related to separation choosability and adaptable choosability. We show that single-conflict chromatic number of simple graphs embeddable on a surface of Euler genus $g$ is $O(g^{1/4}\log g)$ as $g\to\infty$. This is sharp up to the logarithmic factor.
 

 
 
 
 Comments:
 15 pages; in v2, changed the main terminology, added one example, adjusted Conjecture 3; to appear in Journal of Graph Theory
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C15
 

 Cite as:
 arXiv:1803.10962 [math.CO]
 

 
  
 (or 
 arXiv:1803.10962v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1803.10962
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Ross J. Kang [view email] 
 [v1]
 Thu, 29 Mar 2018 08:45:12 UTC (13 KB)

 [v2]
 Fri, 9 Oct 2020 18:48:20 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Single-conflict colouring, by Zden\v{e}k Dvo\v{r}\'ak and 3 other authors
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
 | 2018-03
 

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
