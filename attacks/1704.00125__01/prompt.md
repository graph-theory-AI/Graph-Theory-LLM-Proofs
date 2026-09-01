Attack the following open graph-theory problem.

Catalog id: 1704.00125__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1704.00125__01/
Source paper: Thin graph classes and polynomial-time approximation schemes (arXiv:1704.00125)

=== Extracted statement (catalog JSON) ===
Title: Open Problem (Section 1.2): APX-hardness on classes without sublinear separators
It would be interesting to see whether this intuition can be made precise and for example show that the maximum independent set problem is APX-hard on any subgraph-closed class of graphs that does not have sublinear separators (or at least has exponential expansion).

Context:
The paper notes that maximum independent set is APX-hard on bounded-degree graphs, so results cannot extend to classes containing all 3-regular graphs. Classes studied all have strongly sublinear separators; the authors ask whether APX-hardness can be proved for any subgraph-closed class lacking this property.

=== Catalog page (statement + literature review) ===
Independent set APX-hardness without sublinear separators — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Dvořák asks whether maximum independent set is APX-hard on every subgraph-closed graph class that lacks sublinear separators (or at least has exponential expansion). No follow-up paper proving or disproving this was found after an exhaustive search. Related positive results (PTAS, QPTAS for bounded-expansion and sublinear-separator classes) confirm the structural boundary the problem targets, but the hardness side remains unresolved as of 2026.

 Reviewer notes. No follow-up resolving the hardness question was found in 5 web calls. The conjecture sits at the boundary between tractability (PTAS on classes with strongly sublinear separators) and hardness (APX-hard on 3-regular graphs, which have no sublinear separators); the intermediate regime—subgraph-closed classes with exponential expansion but no 3-regular graphs—appears untouched in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. It would be interesting to see whether this intuition can be made precise and for example show that the maximum independent set problem is APX-hard on any subgraph-closed class of graphs that does not have sublinear separators (or at least has exponential expansion).

Context

The paper notes that maximum independent set is APX-hard on bounded-degree graphs, so results cannot extend to classes containing all 3-regular graphs. Classes studied all have strongly sublinear separators; the authors ask whether APX-hardness can be proved for any subgraph-closed class lacking this property.

Notes. Stated as an open research question in prose; no labelled theorem environment.

Source paper

 Thin graph classes and polynomial-time approximation schemes
 Zdeněk Dvořák · 2017-04-01
 https://arxiv.org/abs/1704.00125
 PDF source

=== Source paper abstract / header ===
Abstract:Baker devised a powerful technique to obtain approximation schemes for various problems restricted to planar graphs. Her technique can be directly extended to various other graph classes, among the most general ones the graphs avoiding a fixed apex graph as a minor. Further generalizations (e.g., to all proper minor closed graph classes) are known, but they use a combination of techniques and usually focus on somewhat restricted classes of problems. We present a new type of graph decompositions (thin systems of overlays) generalizing Baker's technique and leading to straightforward polynomial-time approximation schemes. We also show that many graph classes (all proper minor-closed classes, and all subgraph-closed classes with bounded maximum degree and strongly sublinear separators) admit such decompositions.
 

 
 
 
 Comments:
 30 pages, no figures
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 68W25 (Primary) 05C75 (Secondary)
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:1704.00125 [cs.DM]
 

 
  
 (or 
 arXiv:1704.00125v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1704.00125
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Sat, 1 Apr 2017 06:06:07 UTC (24 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Thin graph classes and polynomial-time approximation schemes, by Zden\v{e}k Dvo\v{r}\'ak
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
 | 2017-04
 

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
