Attack the following open graph-theory problem.

Catalog id: 1912.11246__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1912.11246__01/
Source paper: Maximum independent sets in (pyramid, even hole)-free graphs (arXiv:1912.11246)

=== Extracted statement (catalog JSON) ===
Title: Open problem: MIS complexity in even-hole-free graphs
The complexity of computing a maximum independent set in an even-hole-free graph is not known.

Context:
Stated in the introduction as motivation for the paper's approach. The paper proves a polynomial-time algorithm for the strictly smaller class of (even hole, pyramid)-free graphs, with the hope that understanding the pyramid-free case may shed light on the full even-hole-free class.

=== Catalog page (statement + literature review) ===
MIS complexity in even-hole-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The complexity of maximum independent set in even-hole-free graphs (polynomial-time vs. NP-hard) remains open. Significant partial progress has been made: Abrishami et al. (arXiv:2005.05042, 2020) give a polynomial-time MWIS algorithm for (theta, pyramid, prism, turtle)-free graphs, subsuming the (pyramid, even hole)-free result. More decisively, Chudnovsky, Gartland, Hajebi, Lokshtanov, and Spirkl (arXiv:2407.08927, 2024) prove that every n-vertex even-hole-free graph has tree independence number at most c·log^{10}(n), yielding a quasi-polynomial time algorithm for MWIS across the full even-hole-free class—a major advance that nonetheless leaves the polynomial vs. NP-hard question unresolved.

 Cited literature (2)

 
 
 
partial Graphs with polynomially many minimal separators
 (2020)
 

 
 Tara Abrishami, Maria Chudnovsky, Cemil Dibek, Stéphan Thomassé, Nicolas Trotignon · arXiv preprint · arXiv:2005.05042

Proves that (theta, pyramid, prism, turtle)-free graphs have at most |V(G)|^{18} minimal separators, yielding a polynomial-time MWIS algorithm for this class (which implies polynomial time for (pyramid, even hole)-free graphs, a proper subclass of even-hole-free graphs).
 

 
 
partial Tree Independence Number IV. Even-hole-free Graphs
 (2024)
 

 
 Maria Chudnovsky, Peter Gartland, Sepehr Hajebi, Daniel Lokshtanov, Sophie Spirkl · arXiv preprint · arXiv:2407.08927

Proves that every n-vertex even-hole-free graph has tree independence number at most c·log^{10}(n), implying MWIS is solvable in quasi-polynomial time for the entire even-hole-free class.
 

 

 Reviewer notes. The open problem (polynomial vs. NP-hard for MIS in even-hole-free graphs) is still open as of May 2026. The quasi-polynomial algorithm of arXiv:2407.08927 is the strongest known result for the full class. Both since_posted URLs were verified via WebFetch.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. The complexity of computing a maximum independent set in an even-hole-free graph is not known.

Context

Stated in the introduction as motivation for the paper's approach. The paper proves a polynomial-time algorithm for the strictly smaller class of (even hole, pyramid)-free graphs, with the hope that understanding the pyramid-free case may shed light on the full even-hole-free class.

Notes. Stated as a known open problem in the field (referencing a survey [10]); no specific attribution to individual authors is given in the text.

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
