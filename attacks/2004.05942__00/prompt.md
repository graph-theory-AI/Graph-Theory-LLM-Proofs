Attack the following open graph-theory problem.

Catalog id: 2004.05942__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.05942__00/
Source paper: Pentagon contact representations (arXiv:2004.05942)

=== Catalog page (statement + literature review) ===
Pentagon contact representation algorithm termination — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that the algorithm for computing homothetic pentagon contact representations always terminates remains open as of 2026. No follow-up paper resolving or making partial progress on the termination question was found in the indexed literature. The analogous algorithms for homothetic triangle and square contact representations likewise lack termination proofs, suggesting this is a structurally difficult problem across the family.

 Reviewer notes. No follow-up found. Searches returned only the original paper and its published version in Electronic Journal of Combinatorics (v25i3p39). DBLP page for Schrezenmaier shows no subsequent work on pentagon contact representations or algorithm termination. Semantic Scholar API returned no citing papers.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. We conjecture that the algorithm always terminates.

Context

The paper proposes an algorithm for computing homothetic pentagon contact representations based on systems of linear equations derived from five color forests. When the solution is non-negative it encodes distances between pentagon corners and the representation is constructed; otherwise negative variables guide a local change of the five color forest and the procedure restarts. The authors note that a proof of this conjecture would yield an existence proof for pentagon contact representations independent of Schramm's Monster Packing Theorem. Analogous algorithms for homothetic triangle and square contact representations exist but also lack termination proofs.

Notes. Stated in running prose in the introduction without a labelled theorem environment. PDF extraction quality is adequate for this prose statement.

Source paper

 Pentagon contact representations
 Stefan Felsner, Hendrik Schrezenmaier, Raphael Steiner · 2020-04-13
 https://arxiv.org/abs/2004.05942
 PDF source

=== Source paper abstract / header ===
Abstract:Representations of planar triangulations as contact graphs of a set of internally disjoint homothetic triangles or of a set of internally disjoint homothetic squares have received quite some attention in recent years. In this paper we investigate representations of planar triangulations as contact graphs of a set of internally disjoint homothetic pentagons. Surprisingly such a representation exists for every triangulation whose outer face is a 5-gon. We relate these representations to five color forests. These combinatorial structures resemble Schnyder woods and transversal structures, respectively. In particular there is a bijection to certain alpha-orientations and consequently a lattice structure on the set of five color forests of a given graph. This lattice structure plays a role in an algorithm that is supposed to compute a contact representation with pentagons for a given graph. Based on a five color forest the algorithm builds a system of linear equations and solves it, if the solution is non-negative, it encodes distances between corners of a pentagon representation. In this case the representation is constructed and the algorithm terminates. Otherwise negative variables guide a change of the five color forest and the procedure is restarted with the new five color forest. Similar algorithms have been proposed for contact representations with homothetic triangles and with squares.
 

 
 
 
 Subjects:
 
 Computational Geometry (cs.CG); Combinatorics (math.CO)
 
 
 MSC classes:
 05C62, 68R10
 

 Cite as:
 arXiv:2004.05942 [cs.CG]
 

 
  
 (or 
 arXiv:2004.05942v1 [cs.CG] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2004.05942
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Electronic Journal of Combinatorics 25.3 (2018), P.3.39
 

 

 

 
 Submission history
 From: Hendrik Schrezenmaier [view email] 
 [v1]
 Mon, 13 Apr 2020 13:53:27 UTC (217 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Pentagon contact representations, by Stefan Felsner and 2 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.CG

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2020-04
 

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

 
Stefan Felsner
Hendrik Schrezenmaier
Raphael Steiner 

 

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
