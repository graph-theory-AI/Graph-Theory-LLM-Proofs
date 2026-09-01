Attack the following open graph-theory problem.

Catalog id: 1505.05637__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1505.05637__00/
Source paper: Distributed Corruption Detection in Networks (arXiv:1505.05637)

=== Extracted statement (catalog JSON) ===
Title: Open Problem: Expansion vs. Corruption Detection
There is still a significant gap between the expansion properties that suffice for solving the detection problem (Theorem 1.4) and the conditions in Proposition 1.6 that are necessary for such a solution. It will be interesting to obtain tighter relations between expansion and corruption detection.

Context:
Theorem 1.4 shows that strong spectral expansion (Ramanujan-type $(n,d,\lambda)$-graphs with $\lambda \leq 2\sqrt{d-1}$) suffices for identifying most truthful and corrupt vertices. Proposition 1.6 shows that if removing at most $\epsilon n$ vertices splits the graph into components of size at most $\epsilon n$, then no corruption detection is possible. The gap between these two regimes is noted by the authors as an open research direction.

=== Catalog page (statement + literature review) ===
Expansion-corruption detection gap in networks — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The open problem asks for a tight characterization of which graph expansion properties are necessary and sufficient for corruption detection, closing the gap between the Ramanujan-type spectral sufficiency (Theorem 1.4, requiring \lambda \leq 2\sqrt{d-1}) and the vertex-separator impossibility (Proposition 1.6). Two directly related papers appeared before the 2020 journal publication: Jin, Mossel, and Ramnarayan (arXiv:1809.10325, ITCS 2019) characterize corruption detection on arbitrary graphs via a vertex separability parameter but do not close the spectral expansion gap; Alweiss (arXiv:1908.07493, 2019) addresses a noisy variant of the model. No post-2020 paper resolving the specific expansion gap was found in a broad web search.

 Reviewer notes. Two pre-2020 follow-up papers address related but distinct questions: arXiv:1809.10325 (Jin, Mossel, Ramnarayan, 2018; ITCS 2019) characterizes detectable corruption on general graphs via a vertex-separability parameter m(G) and proves that finding an optimal corruption strategy is NP-hard under the Small Set Expansion Hypothesis; arXiv:1908.07493 (Alweiss, 2019) extends the model to a noisy setting and claims to answer a question of the original authors, but in the noisy (not expansion-gap) sense. Neither directly closes the gap between Ramanujan-type spectral conditions (sufficient) and vertex-separator conditions (necessary for impossibility). No post-2020 literature resolving this specific open problem was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. There is still a significant gap between the expansion properties that suffice for solving the detection problem (Theorem 1.4) and the conditions in Proposition 1.6 that are necessary for such a solution. It will be interesting to obtain tighter relations between expansion and corruption detection.

Context

Theorem 1.4 shows that strong spectral expansion (Ramanujan-type $(n,d,\lambda)$-graphs with $\lambda \leq 2\sqrt{d-1}$) suffices for identifying most truthful and corrupt vertices. Proposition 1.6 shows that if removing at most $\epsilon n$ vertices splits the graph into components of size at most $\epsilon n$, then no corruption detection is possible. The gap between these two regimes is noted by the authors as an open research direction.

Notes. No labelled theorem environment; stated as a research direction at the end of Section 1.1. Section 4, where this is said to be 'further discussed', is not present in the extracted text (PDF extraction appears truncated).

Source paper

 Distributed Corruption Detection in Networks
 Noga Alon, Elchanan Mossel, Robin Pemantle · 2020-03-12
 https://arxiv.org/abs/1505.05637
 PDF source

=== Source paper abstract / header ===
Abstract:We consider the problem of distributed corruption detection in networks. In this model, each vertex of a directed graph is either truthful or corrupt. Each vertex reports the type (truthful or corrupt) of each of its outneighbors. If it is truthful, it reports the truth, whereas if it is corrupt, it reports adversarially. This model, first considered by Preparata, Metze, and Chien in 1967, motivated by the desire to identify the faulty components of a digital system by having the other components checking them, became known as the PMC model. The main known results for this model characterize networks in which \emph{all} corrupt (that is, faulty) vertices can be identified, when there is a known upper bound on their number.
We are interested in networks in which the identity of a \emph{large fraction} of the vertices can be identified.
It is known that in the PMC model, in order to identify all corrupt vertices when their number is $t$, all indegrees have to be at least $t$. In contrast, we show that in $d$ regular-graphs with strong expansion properties, a $1-O(1/d)$ fraction of the corrupt vertices, and a $1-O(1/d)$ fraction of the truthful vertices can be identified, whenever there is a majority of truthful vertices. We also observe that if the graph is very far from being a good expander, namely, if the deletion of a small set of vertices splits the graph into small components, then no corruption detection is possible even if most of the vertices are truthful. Finally, we discuss the algorithmic aspects and the computational hardness of the problem.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Data Structures and Algorithms (cs.DS); Multiagent Systems (cs.MA)
 

 Cite as:
 arXiv:1505.05637 [math.CO]
 

 
  
 (or 
 arXiv:1505.05637v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1505.05637
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Elchanan Mossel [view email] 
 [v1]
 Thu, 21 May 2015 08:01:38 UTC (14 KB)

 [v2]
 Sat, 31 Oct 2015 09:07:02 UTC (16 KB)

 [v3]
 Thu, 12 Mar 2020 16:13:39 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Distributed Corruption Detection in Networks, by Noga Alon and Elchanan Mossel and Robin Pemantle
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
 | 2015-05
 

 Change to browse by:
 
 cs
 cs.DS
 cs.MA
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
