Attack the following open graph-theory problem.

Catalog id: 1704.00125__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1704.00125__00/
Source paper: Thin graph classes and polynomial-time approximation schemes (arXiv:1704.00125)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture (Section 1.2): dropping bounded-degree assumption
It seems plausible that this additional assumption [bounded maximum degree] could be dropped, leading to a much more general result strengthening majority of the algorithms mentioned in the previous subsection.

Context:
The paper proves that subgraph-closed graph classes with strongly sublinear separators admit thin systems of overlays under the additional assumption that their maximum degree is bounded. The authors conjecture this extra condition is unnecessary, which would subsume a much wider class of results.

=== Catalog page (statement + literature review) ===
Thin overlays without bounded-degree assumption — Graph-theory open problems (arXiv)

 
 Status
 open
 low confidence
 

 No verified follow-up paper has been found that resolves the conjecture that the bounded-maximum-degree assumption can be dropped from the result that subgraph-closed graph classes with strongly sublinear separators admit thin systems of overlays. The conjecture is from 2017 and is thus old enough that the absence of evidence in a web search is suspicious. A 2022 paper (arXiv:2208.10074) characterises hereditary graph classes with strongly sublinear separators structurally (as subgraphs of strong products of a star and a complete graph) but could not be confirmed to address the thin-overlay conjecture directly.

 Reviewer notes. Web search found two potentially related papers: arXiv:2208.10074 (Dujmović et al., 2022, 'Product structure of graph classes with strongly sublinear separators') and arXiv:2103.08698 (Dvořák, 2021, 'Approximation metatheorems for classes with bounded expansion'). The 2208.10074 abstract discusses hereditary classes with strongly sublinear separators but does not mention thin systems of overlays. The 2103.08698 paper generalises PTAS results to bounded-expansion classes (a stronger assumption than sublinear separators), so it does not settle the conjecture of dropping bounded degree. No paper directly proving or disproving the conjecture was found within the 5-call cap; status is open with low confidence given the 9-year age of the conjecture.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It seems plausible that this additional assumption [bounded maximum degree] could be dropped, leading to a much more general result strengthening majority of the algorithms mentioned in the previous subsection.

Context

The paper proves that subgraph-closed graph classes with strongly sublinear separators admit thin systems of overlays under the additional assumption that their maximum degree is bounded. The authors conjecture this extra condition is unnecessary, which would subsume a much wider class of results.

Notes. Stated informally in the 'Limitations of our technique' subsection; no labelled theorem environment.

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
