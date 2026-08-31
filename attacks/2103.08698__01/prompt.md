Attack the following open graph-theory problem.

Catalog id: 2103.08698__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2103.08698__01/
Source paper: Approximation metatheorems for classes with bounded expansion (arXiv:2103.08698)

=== Catalog page (statement + literature review) ===
FO minimization PTAS in treewidth-fragile classes — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 6 of arXiv:2103.08698 asks whether monotone minimization problems expressible in first-order logic admit constant-factor approximations in bounded-expansion classes and PTASes in efficiently fractionally treewidth-fragile classes. The source paper itself establishes these results only for maximization problems; the paper explicitly notes that for minimization the error is bounded only by a fraction of the total vertex weight rather than the optimum, leaving both parts of the problem open. No subsequent paper resolving either part was found in a targeted literature search spanning arXiv and conference proceedings through May 2026.

 Reviewer notes. No follow-up paper addressing the minimization side of Problem 6 was found. The source paper's own discussion identifies weighted vertex cover in fractionally treewidth-fragile classes as the simplest concrete open case. The related literature on PTAS for sparse general-valued CSPs (e.g. arXiv:2012.12607) works with Max-CSP frameworks and does not resolve the FO-minimization question in bounded-expansion classes.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Do monotone minimization problems expressible in the first order logic admit constant factor approximation in all classes with bounded expansion? And PTASes in all efficiently fractionally treewidth-fragile graph classes?

Context

The paper's techniques apply to minimization problems only with error bounded by a fraction of the total vertex weight rather than the optimal, so constant-factor approximation in bounded-expansion classes and PTASes in fractionally treewidth-fragile classes for minimization remain open. As a concrete simplest case, it is unknown whether a PTAS exists for weighted vertex cover in fractionally treewidth-fragile graph classes.

Source paper

 Approximation metatheorems for classes with bounded expansion
 Zdeněk Dvořák · 2021-10-09
 https://arxiv.org/abs/2103.08698
 PDF source

=== Source paper abstract / header ===
Abstract:We give a number of approximation metatheorems for monotone maximization problems expressible in the first-order logic, in substantially more general settings than the previously known. We obtain * constant-factor approximation algorithm in any class of graphs with bounded expansion, * a QPTAS in any class with strongly sublinear separators, and * a PTAS in any fractionally treewidth-fragile class (which includes all common classes with strongly sublinear separators. Moreover, our tools also give an exact subexponential-time algorithm in any class with strongly sublinear separators.
 

 
 
 
 Comments:
 35 pages, no figures; revised the presentation
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C85
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2103.08698 [cs.DM]
 

 
  
 (or 
 arXiv:2103.08698v3 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2103.08698
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdeněk Dvořák [view email] 
 [v1]
 Mon, 15 Mar 2021 20:26:05 UTC (16 KB)

 [v2]
 Sat, 11 Sep 2021 16:12:58 UTC (17 KB)

 [v3]
 Sat, 9 Oct 2021 23:06:38 UTC (24 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Approximation metatheorems for classes with bounded expansion, by Zden\v{e}k Dvo\v{r}\'ak
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
 | 2021-03
 

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
