Attack the following open graph-theory problem.

Catalog id: 2201.04062__00
Catalog status: open (triage tier 4, lean balanced)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2201.04062__00/
Source paper: Pure pairs. VIII. Excluding a sparse graph (arXiv:2201.04062)

=== Extracted statement (catalog JSON) ===
Title: Possibility 1.6
For all $c > 0$, there exists $\xi > 0$ with the following property. For every graph $H$ with congestion at most $\xi$, there exists $\varepsilon > 0$ such that for every graph $G$ with $|G| > 1$ that is $H$-free and $\bar{H}$-free, there is a pure pair $A, B$ in $G$ with $|A| \geq \varepsilon|G|$ and $|B| \geq \varepsilon|G|^{1-c}$.

Context:
Theorem 1.3 (from an earlier paper) gives a pure pair where one set has linear size, and the authors ask whether an analogous strengthening of their main result 1.4 holds: can one of the two sets always be taken to have linear size rather than polynomial size $\varepsilon|G|^{1-c}$? The authors explicitly state they were unable to decide this. The proof technique for 1.4 cannot be directly extended to resolve 1.6 because a key inductive argument requires strictly increasing shrinkage parameters, leaving no room for the stronger conclusion.

=== Catalog page (statement + literature review) ===
Linear pure pair in sparse H-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Possibility 1.6 asks whether the polynomial pure-pair bound in Theorem 1.4 can be strengthened so that one of the two sets always has linear size, for every graph H with sufficiently small congestion. The source paper's authors explicitly state they were unable to decide this, and the inductive proof technique cannot be directly extended. No subsequent paper resolving or substantially advancing the full conjecture was found in the indexed literature as of May 2026.

 Reviewer notes. Both internal references are false positives — neither addresses Possibility 1.6 or the congestion parameter from Pure pairs VIII. A potentially related paper arXiv:2504.21127 ('On polynomially high-chromatic pure pairs') was found but its abstract concerns forest-free graphs and the polynomial Gyárfás-Sumner conjecture, not the specific claim about congestion and linear-vs-polynomial set sizes. No follow-up resolving Possibility 1.6 was found within the 5-call cap.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. For all $c > 0$, there exists $\xi > 0$ with the following property. For every graph $H$ with congestion at most $\xi$, there exists $\varepsilon > 0$ such that for every graph $G$ with $|G| > 1$ that is $H$-free and $\bar{H}$-free, there is a pure pair $A, B$ in $G$ with $|A| \geq \varepsilon|G|$ and $|B| \geq \varepsilon|G|^{1-c}$.

Context

Theorem 1.3 (from an earlier paper) gives a pure pair where one set has linear size, and the authors ask whether an analogous strengthening of their main result 1.4 holds: can one of the two sets always be taken to have linear size rather than polynomial size $\varepsilon|G|^{1-c}$? The authors explicitly state they were unable to decide this. The proof technique for 1.4 cannot be directly extended to resolve 1.6 because a key inductive argument requires strictly increasing shrinkage parameters, leaving no room for the stronger conclusion.

Notes. PDF source — labeled 'Possibility' rather than 'Conjecture' or 'Question' in the paper; math in 1.6 is readable but the congestion bound $c/(9+15c)$ in the nearby Theorem 1.4 appears garbled in the PDF extraction.

Source paper

 Pure pairs. VIII. Excluding a sparse graph
 Alex Scott, Paul Seymour, Sophie Spirkl · 2023-10-29
 https://arxiv.org/abs/2201.04062
 PDF source

=== Source paper abstract / header ===
Abstract:A pure pair of size $t$ in a graph $G$ is a pair $A,B$ of disjoint sets of $t$ vertices such that $A$ is either complete or anticomplete to $B$. It is known that, for every forest $H$, every graph on $n\ge2$ vertices that does not contain $H$ or its complement as an induced subgraph has a pure pair of size $\Omega(n)$; furthermore, this only holds when $H$ or its complement is a forest.
In this paper, we look at pure pairs of size $n^{1-c}$, where $0<c<1$. Let $H$ be a graph: does every graph on $n\ge2$ vertices that does not contain $H$ or its complement as an induced subgraph have a pure pair $A,B$ with $|A|,|B|\ge \Omega(|G|^{1-c})$,? The answer is related to the congestion of $H$, the maximum of $1-(|J|-1)/|E(J)|$ over all subgraphs $J$ of $H$ with an edge. (Congestion is nonnegative, and equals zero exactly when $H$ is a forest.) Let $d$ be the smaller of the congestions of $H$ and $\overline{H}$. We show that the answer to the question above is "yes" if $d\le c/(9+15c)$, and "no" if $d>c$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2201.04062 [math.CO]
 

 
  
 (or 
 arXiv:2201.04062v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2201.04062
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Tue, 11 Jan 2022 17:06:36 UTC (25 KB)

 [v2]
 Sun, 29 Oct 2023 17:03:02 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Pure pairs. VIII. Excluding a sparse graph, by Alex Scott and 2 other authors
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
 | 2022-01
 

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
