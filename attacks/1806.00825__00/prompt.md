Attack the following open graph-theory problem.

Catalog id: 1806.00825__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1806.00825__00/
Source paper: Short rainbow cycles in graphs and matroids (arXiv:1806.00825)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 4
Let $G$ be a simple $n$-vertex graph and $c$ be a colouring of $E(G)$ with $n$ colours, where each colour class has size at least $r$. Then $(G, c)$ contains a cycle $C$ of length at most $\lceil n/r \rceil$ such that no two incident edges of $C$ are the same colour.

Context:
Introduced by the authors as a weakening of Aharoni's Conjecture 3 (the rainbow condition on the whole cycle is replaced by a proper-edge-colouring condition on incident pairs). The authors prove that Conjecture 4 implies the Caccetta-Häggkvist conjecture via a direct colouring construction on the underlying undirected graph of a digraph.

=== Catalog page (statement + literature review) ===
Proper-incident short rainbow cycle bound — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 Caccetta-Häggkvist Conjecture
 (fuzzy-match score 83).

 
 Status
 open
 medium confidence
 

 Conjecture 4 from arXiv:1806.00825, which asks for a short proper cycle (no two incident edges share a color) of length at most \lceil n/r \rceil in an n-vertex graph with n color classes each of size at least r, remains open as a specific target. It is strictly weaker than Aharoni's rainbow cycle conjecture. Progress on Aharoni's conjecture — proven for color class size \Omega(k \log k) by Hompe et al. (2021) and advanced further in 2024 — is indirectly relevant but does not settle Conjecture 4. No paper directly addressing the proper-cycle variant was found in the searched literature.

 Cited literature (1)

 
 
 
partial On Aharoni's rainbow generalization of the Caccetta-Häggkvist conjecture
 (2021)
 

 
 Patrick Hompe, Petra Pelikanova, Aneta Pokorna, Sophie Spirkl · Discrete Mathematics, Volume 344, Issue 5 · arXiv:2101.04716

Proves Aharoni's rainbow conjecture (strictly stronger than Conjecture 4) when each color class has size at least \Omega(k \log k); only indirectly relevant to Conjecture 4 via the implication that a solved stronger conjecture would settle the weaker one.
 

 

 Reviewer notes. Conjecture 4 requires only that no two incident edges of the found cycle share a color (proper edge-coloring condition on the cycle), which is strictly weaker than Aharoni's rainbow condition (all edges distinct colors). No dedicated follow-up paper addressing this proper-cycle variant was found. A 2024 JCTB paper ('Aharoni's rainbow cycle conjecture holds up to an additive constant', doi:10.1016/j.jctb.2024.12.004) and a 2022 result showing Aharoni's conjecture holds for \Omega(k) color class size advance the stronger rainbow conjecture, but access to the 2024 paper was blocked (HTTP 403) and it cannot be cited as verified. Confidence is medium because the 2024 JCTB paper may implicitly cover Conjecture 4 but could not be confirmed.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $G$ be a simple $n$-vertex graph and $c$ be a colouring of $E(G)$ with $n$ colours, where each colour class has size at least $r$. Then $(G, c)$ contains a cycle $C$ of length at most $\lceil n/r \rceil$ such that no two incident edges of $C$ are the same colour.

Context

Introduced by the authors as a weakening of Aharoni's Conjecture 3 (the rainbow condition on the whole cycle is replaced by a proper-edge-colouring condition on incident pairs). The authors prove that Conjecture 4 implies the Caccetta-Häggkvist conjecture via a direct colouring construction on the underlying undirected graph of a digraph.

Notes. PDF source — ceiling notation garbled but mathematical content is unambiguous.

Source paper

 Short rainbow cycles in graphs and matroids
 Matt DeVos, Matthew Drescher, Daryl Funk, Sebastián González Hermosillo de la Maza, Krystal Guo, Tony Huynh, Bojan Mohar, Amanda Montejano · 2020-05-07
 https://arxiv.org/abs/1806.00825
 PDF source

=== Source paper abstract / header ===
Abstract:Let $G$ be a simple $n$-vertex graph and $c$ be a colouring of $E(G)$ with $n$ colours, where each colour class has size at least $2$. We prove that $(G,c)$ contains a rainbow cycle of length at most $\lceil \frac{n}{2} \rceil$, which is best possible. Our result settles a special case of a strengthening of the Caccetta-Häggkvist conjecture, due to Aharoni. We also show that the matroid generalization of our main result also holds for cographic matroids, but fails for binary matroids.
 

 
 
 
 Comments:
 9 pages, 2 figures. In this version we correct a slight inaccurancy in the proof of Theorem 14, found by the pilot project Mathpocalypse (this https URL) of Emanuele Natale and Édouard Oyallon
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C15, 05C20, 05C38
 

 Cite as:
 arXiv:1806.00825 [math.CO]
 

 
  
 (or 
 arXiv:1806.00825v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1806.00825
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Graph Theory. 2021; 96: 192-202
 

 
 
 Related DOI:
 
 https://doi.org/10.1002/jgt.22607

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tony Huynh [view email] 
 [v1]
 Sun, 3 Jun 2018 16:27:11 UTC (24 KB)

 [v2]
 Fri, 14 Sep 2018 16:03:53 UTC (26 KB)

 [v3]
 Thu, 7 May 2020 18:12:27 UTC (28 KB)

 [v4]
 Tue, 28 Jul 2026 13:46:27 UTC (29 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Short rainbow cycles in graphs and matroids, by Matt DeVos and 7 other authors
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
 | 2018-06
 

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
