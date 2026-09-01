Attack the following open graph-theory problem.

Catalog id: 2202.07746__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2202.07746__00/
Source paper: Expected number of faces in a random embedding of any graph is at most … (arXiv:2202.07746)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 4
For any simple graph $G$ of order $n$, $E[F] \leq \frac{1}{3}n + 1$.

Context:
The paper proves $E[F] \leq \frac{\pi^2}{6}n$ for simple graphs (Theorem 8), but no examples approaching this constant are known. A chain of triangles connected by cut edges achieves $E[F] = \frac{1}{3}n+1$, which the authors conjecture is the true optimal bound.

=== Catalog page (statement + literature review) ===
Linear face bound in random graph embeddings — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 No follow-up paper proving or disproving Conjecture 4 (E[F] \leq \frac{1}{3}n + 1 for simple graphs) has been found. The source paper itself establishes E[F] \leq \frac{\pi^2}{6}n (Theorem 8) and notes that a chain of triangles connected by cut edges achieves E[F] = \frac{1}{3}n + 1, making this the conjectured tight constant. A related follow-up (arXiv:2211.01032, SODA 2024) by Campion Loth, Halasz, Masarik, Mohar, and Samal proves logarithmic expected face counts for many specific graph families (complete graphs, random graphs, degree-bounded models), but does not address the worst-case tight linear conjecture.

 Reviewer notes. The conjecture is recent (journal published 2023) and a wide search found no follow-up addressing the tight constant 1/3. The related paper arXiv:2211.01032 (SODA 2024, by partially overlapping authors) shows logarithmic bounds for most graphs but does not address this specific extremal conjecture. Absence of evidence is not suspicious given the difficulty of improving worst-case linear constants in random embedding theory.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any simple graph $G$ of order $n$, $E[F] \leq \frac{1}{3}n + 1$.

Context

The paper proves $E[F] \leq \frac{\pi^2}{6}n$ for simple graphs (Theorem 8), but no examples approaching this constant are known. A chain of triangles connected by cut edges achieves $E[F] = \frac{1}{3}n+1$, which the authors conjecture is the true optimal bound.

Notes. PDF source; fraction $\frac{1}{3}$ appears as '1\n3' in raw PDF text but context is unambiguous.

Source paper

 Expected number of faces in a random embedding of any graph is at most linear
 Jesse Campion Loth, Bojan Mohar · 2023-03-30
 https://arxiv.org/abs/2202.07746
 PDF source

=== Source paper abstract / header ===
Abstract:A random 2-cell embedding of a given graph $G$ is obtained by choosing a random local rotation around every vertex. We analyze the expected number of faces of such an embedding, which is equivalent to studying its average genus. In 1991, Stahl proved that the expected number of faces in a random embedding of an arbitrary graph of order $n$ is at most $n\log(n)$. While there are many families of graphs whose expected number of faces is $\Theta(n)$, none are known where the expected number would be super-linear. This lead to the conjecture that there is a linear upper bound. In this note we confirm the conjecture by proving that for any $n$-vertex multigraph, the expected number of faces in a random 2-cell embedding is at most $n(1+H_m)$, where $m$ is the maximum edge-multiplicity and $H_m$ denotes the $m$th harmonic number. This bound is best possible up to a constant factor.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C10, 05C80
 

 Cite as:
 arXiv:2202.07746 [math.CO]
 

 
  
 (or 
 arXiv:2202.07746v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2202.07746
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Jesse Campion Loth [view email] 
 [v1]
 Tue, 15 Feb 2022 21:57:10 UTC (32 KB)

 [v2]
 Thu, 30 Mar 2023 23:13:28 UTC (27 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Expected number of faces in a random embedding of any graph is at most linear, by Jesse Campion Loth and Bojan Mohar
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
 | 2022-02
 

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
