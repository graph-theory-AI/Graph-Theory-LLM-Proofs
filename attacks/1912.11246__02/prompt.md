Attack the following open graph-theory problem.

Catalog id: 1912.11246__02
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1912.11246__02/
Source paper: Maximum independent sets in (pyramid, even hole)-free graphs (arXiv:1912.11246)

=== Extracted statement (catalog JSON) ===
Title: Open problem: polynomial separator property for (prism, pyramid, theta, even wheel)-free graphs
It is unknown whether (prism, pyramid, theta, even wheel)-free graphs have polynomially many minimal separators.

Context:
The authors note that a weakening of Conjecture 2.2 is obtained by restricting to (prism, pyramid, theta, even wheel)-free graphs (since prisms, thetas, and turtles all contain even holes). They explicitly state they 'were not able to prove that (prism, pyramid, theta, even wheel)-free graphs have polynomially many minimal separators,' which is why the main result (Theorem 2.3) additionally excludes squares.

=== Catalog page (statement + literature review) ===
Polynomial minimal separators in odd-hole-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The open problem of whether (prism, pyramid, theta, even wheel)-free graphs have polynomially many minimal separators remains unresolved as stated. Abrishami, Chudnovsky, Dibek, Thomassé, Trotignon, and Vušković (arXiv:2005.05042, 2020) proved the closely related result that (theta, pyramid, prism, turtle)-free graphs have at most $|V(G)|^{18}$ minimal separators constructible in polynomial time; this shares three of the four forbidden subgraphs with the open problem but uses turtle in place of even wheel. Whether this result implies the even-wheel-free case (via class inclusion) could not be determined from the abstract alone, leaving the exact conjecture from arXiv:1912.11246 open or at most partially addressed.

 Cited literature (1)

 
 
 
partial Graphs with polynomially many minimal separators
 (2021)
 

 
 Tara Abrishami, Maria Chudnovsky, Cemil Dibek, Stéphan Thomassé, Nicolas Trotignon, Kristina Vušković · Journal of Combinatorial Theory, Series B · arXiv:2005.05042

Proves that (theta, pyramid, prism, turtle)-free graphs have at most $|V(G)|^{18}$ minimal separators, a polynomial bound for a four-forbidden-subgraph class that shares prism, pyramid, and theta with the open problem but replaces even wheel with turtle.
 

 

 Reviewer notes. The fourth forbidden subgraph differs between the proved result (turtle, in 2005.05042) and the open problem (even wheel, in 1912.11246). Since turtles contain even holes but even wheels may not contain turtles (and vice versa), the two graph classes are likely incomparable, so 2005.05042 does not directly resolve the stated open problem. The published version of 2005.05042 appears in JCTB (ScienceDirect pii S0095895621000848); DOI not verified. No further follow-up specifically addressing the even-wheel-free case was found within the 5-call cap.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It is unknown whether (prism, pyramid, theta, even wheel)-free graphs have polynomially many minimal separators.

Context

The authors note that a weakening of Conjecture 2.2 is obtained by restricting to (prism, pyramid, theta, even wheel)-free graphs (since prisms, thetas, and turtles all contain even holes). They explicitly state they 'were not able to prove that (prism, pyramid, theta, even wheel)-free graphs have polynomially many minimal separators,' which is why the main result (Theorem 2.3) additionally excludes squares.

Notes. Implicit open problem arising from the gap between Conjecture 2.2 and Theorem 2.3; not labeled as a formal conjecture or problem in the paper.

Source paper

 Maximum independent sets in (pyramid, even hole)-free graphs
 Maria Chudnovsky, Stéphan Thomassé, Nicolas Trotignon, Kristina Vušković · 2019-12-24
 https://arxiv.org/abs/1912.11246
 PDF source

=== Source paper abstract / header ===
Abstract:A \emph{hole} in a graph is an induced cycle with at least 4 vertices. A graph is \emph{even-hole-free} if it does not contain a hole on an even number of vertices. A \emph{pyramid} is a graph made of three chordless paths $P_1 = a \dots b_1$,
$P_2 = a \dots b_2$, $P_3 = a \dots b_3$ of length at least~1, two of which have length at least 2, vertex-disjoint except at $a$, and such that $b_1b_2b_3$ is a triangle and no edges exist between the paths except those of the triangle and the three edges incident with $a$.
We give a polynomial time algorithm to compute a maximum weighted independent set in a even-hole-free graph that contains no pyramid as an induced subgraph. Our result is based on a decomposition theorem and on bounding the number of minimal separators. All our results hold for a slightly larger class of graphs, the class of (square, prism, pyramid, theta, even wheel)-free graphs.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:1912.11246 [cs.DM]
 

 
  
 (or 
 arXiv:1912.11246v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1912.11246
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Nicolas Trotignon [view email] 
 [v1]
 Tue, 24 Dec 2019 08:41:09 UTC (71 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Maximum independent sets in (pyramid, even hole)-free graphs, by Maria Chudnovsky and 2 other authors
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
 | 2019-12
 

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

 
Maria Chudnovsky
Stéphan Thomassé
Nicolas Trotignon
Kristina Vuskovic 

 

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
