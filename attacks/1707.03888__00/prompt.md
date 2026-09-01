Attack the following open graph-theory problem.

Catalog id: 1707.03888__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1707.03888__00/
Source paper: Additive non-approximability of chromatic number in proper minor-closed… (arXiv:1707.03888)

=== Extracted statement (catalog JSON) ===
Title: Open question: additive approximation for triangle-free graphs
Does there exist $\alpha \geq 0$ such that for every proper minor-closed class $\mathcal{G}$, the chromatic number of triangle-free graphs in $\mathcal{G}$ can be approximated in polynomial time within additive error $\alpha$?

Context:
Forbidding triangles makes coloring more tractable for embedded graphs (all planar graphs are 3-colorable and 3-colorability in any fixed surface is linear-time decidable). The authors show forbidding cliques of size 4 is insufficient (Theorem 6), but explicitly state the triangle-free case remains open.

=== Catalog page (statement + literature review) ===
Triangle-free χ additive approximation in minor-closed — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The open question—whether a uniform additive approximation for the chromatic number of triangle-free graphs exists across all proper minor-closed classes—remains unresolved. The source paper (Dvořák and Kawarabayashi, ICALP 2018) establishes hardness for K_{4k+1}-minor-free graphs in general, and a weaker hardness bound for K_{4k+1}-minor-free graphs with no K_4 cliques (Theorem 6), but explicitly leaves the triangle-free case open. No follow-up paper resolving this question was found in a wide web search across the 2017–2026 period.

 Reviewer notes. No follow-up paper resolving the triangle-free open question was found. The published version of the source paper appeared at ICALP 2018 (LIPIcs vol. 107, article 47) and in Journal of Combinatorial Theory Series B (ScienceDirect, 2020). The known positive special case is that every triangle-free K_5-minor-free graph is 3-colorable (extending Grötzsch's theorem), but this does not address the uniform additive approximation across all proper minor-closed classes. Confidence is medium because the conjecture is roughly 9 years old, so absence of a resolution in the search is somewhat suspicious; the question may simply be very hard.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Does there exist $\alpha \geq 0$ such that for every proper minor-closed class $\mathcal{G}$, the chromatic number of triangle-free graphs in $\mathcal{G}$ can be approximated in polynomial time within additive error $\alpha$?

Context

Forbidding triangles makes coloring more tractable for embedded graphs (all planar graphs are 3-colorable and 3-colorability in any fixed surface is linear-time decidable). The authors show forbidding cliques of size 4 is insufficient (Theorem 6), but explicitly state the triangle-free case remains open.

Notes. PDF source; stated in prose as 'this question is still open'.

Source paper

 Additive non-approximability of chromatic number in proper minor-closed classes
 Zdeněk Dvořák, Ken-ichi Kawarabayashi · 2017-07-12
 https://arxiv.org/abs/1707.03888
 PDF source

=== Source paper abstract / header ===
Abstract:Robin Thomas asked whether for every proper minor-closed class C, there exists a polynomial-time algorithm approximating the chromatic number of graphs from C up to a constant additive error independent on the class C. We show this is not the case: unless P=NP, for every integer k>=1, there is no polynomial-time algorithm to color a K_{4k+1}-minor-free graph G using at most chi(G)+k-1 colors. More generally, for every k>=1 and 1<=\beta<=4/3, there is no polynomial-time algorithm to color a K_{4k+1}-minor-free graph G using less than this http URL(G)+(4-3beta)k colors. As far as we know, this is the first non-trivial non-approximability result regarding the chromatic number in proper minor-closed classes.
We also give somewhat weaker non-approximability bound for K_{4k+1}-minor-free graphs with no cliques of size 4. On the positive side, we present additive approximation algorithm whose error depends on the apex number of the forbidden minor, and an algorithm with additive error 6 under the additional assumption that the graph has no 4-cycles.
 

 
 
 
 Comments:
 22 pages, no figures
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 
 
 MSC classes:
 05C15
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:1707.03888 [cs.DM]
 

 
  
 (or 
 arXiv:1707.03888v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1707.03888
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Wed, 12 Jul 2017 19:55:03 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Additive non-approximability of chromatic number in proper minor-closed classes, by Zden\v{e}k Dvo\v{r}\'ak and Ken-ichi Kawarabayashi
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
 | 2017-07
 

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
Ken-ichi Kawarabayashi 

 

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
