Attack the following open graph-theory problem.

Catalog id: 1709.09050__02
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1709.09050__02/
Source paper: Topological directions in Cops and Robbers (arXiv:1709.09050)

=== Extracted statement (catalog JSON) ===
Title: Tightness of linear capture time bound for planar graphs
Is the bound $\mathrm{capt}_3(G) \leq 2n$ tight for planar graphs of order $n$? Does there exist a planar graph $G$ of order $n$ with $\mathrm{capt}(G) > n$?

Context:
Theorem 5 establishes $\mathrm{capt}_3(G) \leq 2n$ for planar graphs of order $n$, improving the earlier $O(n^2)$ bound of Theorem 4. Whether this linear bound is tight is unknown; even finding a single planar graph with capture time exceeding $n$ remains open.

=== Catalog page (statement + literature review) ===
Tightness of 3-cop capture time bound for planar graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture from Bonato and Mohar (arXiv:1709.09050) asks whether the bound capt_3(G) ≤ 2n for planar graphs of order n is tight and, more specifically, whether any planar graph exists with capture time exceeding n. No follow-up paper resolving either question was found in the indexed literature as of May 2026. The most related general result — showing O(n^{k+1}) is asymptotically tight for k ≥ 2 cops in arbitrary graphs (Brandt et al., 2020) — does not apply to the planar setting with k = 3.

 Reviewer notes. No follow-up found. The Brandt-Emek-Uitto-Wattenhofer paper (Theoretical Computer Science, 2020; doi:10.1016/j.tcs.2020.07.016) shows O(n^{k+1}) capture-time is tight for k ≥ 2 cops in general graphs, but this does not address the planar restriction. The paper arXiv:2406.01068 (2024) studies guarding isometric subgraphs and proves c_2(G) ≤ 3 for planar graphs (cop-move number variant), which is unrelated to the capt_3 tightness question. The conjecture remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Is the bound $\mathrm{capt}_3(G) \leq 2n$ tight for planar graphs of order $n$? Does there exist a planar graph $G$ of order $n$ with $\mathrm{capt}(G) > n$?

Context

Theorem 5 establishes $\mathrm{capt}_3(G) \leq 2n$ for planar graphs of order $n$, improving the earlier $O(n^2)$ bound of Theorem 4. Whether this linear bound is tight is unknown; even finding a single planar graph with capture time exceeding $n$ remains open.

Notes. PDF source

Source paper

 Topological directions in Cops and Robbers
 Anthony Bonato, Bojan Mohar · 2018-04-22
 https://arxiv.org/abs/1709.09050
 PDF source

=== Source paper abstract / header ===
Abstract:We survey results at the intersection of topological graph theory and the game of Cops and Robbers, focusing on results, conjectures, and open problems for the cop number of a graph embedded on a surface. After a discussion on results for planar graphs, we consider graphs of higher genus. In 2001, Schroeder conjectured that if a graph has genus $g,$ then its cop number is at most $g + 3.$ While Schroeder's bound is known to hold for planar and toroidal graphs, the case for graphs with higher genus remains open. We consider the capture time of graphs on surfaces and examine results for embeddings of graphs on non-orientable surfaces. We present a conjecture by the second author, and in addition, we survey results for the lazy cop number, directed graphs, and Zombies and Survivors.
 

 
 
 
 Comments:
 arXiv admin note: text overlap with arXiv:1703.09616 by other authors
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C10, 05C57
 

 Cite as:
 arXiv:1709.09050 [math.CO]
 

 
  
 (or 
 arXiv:1709.09050v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1709.09050
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Anthony Bonato [view email] 
 [v1]
 Mon, 25 Sep 2017 14:08:10 UTC (14 KB)

 [v2]
 Sun, 22 Apr 2018 18:17:58 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Topological directions in Cops and Robbers, by Anthony Bonato and 1 other authors
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
 | 2017-09
 

 Change to browse by:
 
 cs
 cs.DM
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 
 
 1 blog link
 (what is this?)
 

 

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
