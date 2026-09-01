Attack the following open graph-theory problem.

Catalog id: 1901.01797__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1901.01797__00/
Source paper: Baker game and polynomial-time approximation schemes (arXiv:1901.01797)

=== Extracted statement (catalog JSON) ===
Title: Open Problem (Section 1.1)
It is an open problem whether some variation on the local search approach can give PTAS for all monotone FO optimization problems.

Context:
Cabello–Gajser and Har-Peled–Quanrud showed that the trivial local search algorithm (performing bounded-size changes on an initial solution as long as it can be improved) gives PTASes for maximum independent set and minimum dominating set, as well as many related problems, on classes with strongly sublinear separators. The question is whether this approach, or a variation thereof, can be extended to cover all monotone first-order optimization problems on such classes.

=== Catalog page (statement + literature review) ===
PTAS for monotone FO optimization via local search — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The open problem asks whether a local search variation yields PTAS for all monotone first-order optimization problems on classes with strongly sublinear separators. Dvořák's follow-up work (arXiv:2103.08698, SWAT 2022) obtains PTAS for fractionally treewidth-fragile classes (which include all common strongly sublinear separator classes) and a QPTAS for all strongly sublinear separator classes, via Baker-style decomposition techniques rather than local search. The specific question about the local search approach remains unresolved, and PTAS for the full generality of strongly sublinear separator classes (beyond fractionally treewidth-fragile ones) is still open.

 Cited literature (1)

 
 
 
partial Approximation metatheorems for classes with bounded expansion
 (2021)
 

 
 Zdeněk Dvořák · SWAT 2022 (LIPIcs vol. 227) · arXiv:2103.08698 · doi:10.4230/LIPIcs.SWAT.2022.22

Proves PTAS for monotone FO maximization in fractionally treewidth-fragile classes and QPTAS in all strongly sublinear separator classes, via Baker-style techniques rather than local search; the local search question and full PTAS for all strongly sublinear separator classes remain open.
 

 

 Reviewer notes. The follow-up paper 2103.08698 makes substantial progress by obtaining PTAS for many of the target classes, but does so via Baker-style decompositions rather than local search. Whether a local search variation specifically achieves PTAS for all monotone FO problems on all strongly sublinear separator classes remains an open question.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. It is an open problem whether some variation on the local search approach can give PTAS for all monotone FO optimization problems.

Context

Cabello–Gajser and Har-Peled–Quanrud showed that the trivial local search algorithm (performing bounded-size changes on an initial solution as long as it can be improved) gives PTASes for maximum independent set and minimum dominating set, as well as many related problems, on classes with strongly sublinear separators. The question is whether this approach, or a variation thereof, can be extended to cover all monotone first-order optimization problems on such classes.

Notes. Stated as prose ('It is an open problem whether…') in Section 1.1 without a labelled theorem environment; no prior attribution given. PDF source — remainder of paper text is cut off, so additional items later in the paper may be missing.

Source paper

 Baker game and polynomial-time approximation schemes
 Zdeněk Dvořák · 2019-01-07
 https://arxiv.org/abs/1901.01797
 PDF source

=== Source paper abstract / header ===
Abstract:Baker devised a technique to obtain approximation schemes for many optimization problems restricted to planar graphs; her technique was later extended to more general graph classes. In particular, using the Baker's technique and the minor structure theorem, Dawar et al. gave Polynomial-Time Approximation Schemes (PTAS) for all monotone optimization problems expressible in the first-order logic when restricted to a proper minor-closed class of graphs. We define a Baker game formalizing the notion of repeated application of Baker's technique interspersed with vertex removal, prove that monotone optimization problems expressible in the first-order logic admit PTAS when restricted to graph classes in which the Baker game can be won in a constant number of rounds, and prove without use of the minor structure theorem that all proper minor-closed classes of graphs have this property.
 

 
 
 
 Comments:
 27 pages, no figures
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C85 (Primary) 05C83 (Secondary)
 

 
 ACM classes:
 G.2.2; F.2.2
 

 Cite as:
 arXiv:1901.01797 [cs.DM]
 

 
  
 (or 
 arXiv:1901.01797v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1901.01797
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Mon, 7 Jan 2019 13:35:30 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Baker game and polynomial-time approximation schemes, by Zden\v{e}k Dvo\v{r}\'ak
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
 | 2019-01
 

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

 
Zdenek Dvorák 

 

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
