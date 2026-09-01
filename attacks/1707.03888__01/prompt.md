Attack the following open graph-theory problem.

Catalog id: 1707.03888__01
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1707.03888__01/
Source paper: Additive non-approximability of chromatic number in proper minor-closed… (arXiv:1707.03888)

=== Extracted statement (catalog JSON) ===
Title: Open question: better additive approximation for $K_{4k_0+1}$-minor-free graphs
Is there a polynomial-time additive approximation algorithm for the chromatic number of $K_{4k_0+1}$-minor-free graphs with additive error strictly between $k_0/4$ (the lower bound of Corollary 4) and $k_0 - 2$ (the upper bound of Kawarabayashi et al.)?

Context:
Kawarabayashi et al. showed the chromatic number of $K_k$-minor-free graphs can be approximated additively up to $k-2$. Corollary 4 of this paper establishes that an additive error of $k_0 - 1$ is NP-hard to achieve, leaving a gap of roughly a factor of 4 between the best known algorithm and the hardness bound.

=== Catalog page (statement + literature review) ===
Additive chromatic approximation gap in K_k-minor-free — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The question of whether the additive approximation gap for chromatic number of $K_{4k_0+1}$-minor-free graphs can be tightened remains open. The source paper (arXiv:1707.03888, ICALP 2018, J. Combin. Theory Ser. B 2020) establishes a hardness lower bound showing no poly-time algorithm achieves additive error below $k_0/4$, while Kawarabayashi et al.'s prior algorithm achieves additive error $k_0-2$, leaving a gap of roughly a factor of 4. No subsequent work narrowing this gap was found in the indexed literature.

 Reviewer notes. No follow-up resolving the approximation gap between $k_0/4$ and $k_0-2$ was found in the indexed literature. The paper appeared as ICALP 2018 (LIPIcs) and was later published in J. Combin. Theory Ser. B (2020, doi:10.1016/j.jctb.2020.02.001); these are the same work and do not constitute follow-up. The conjecture is now approximately 8 years old with no known progress on closing the factor-of-4 gap.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Is there a polynomial-time additive approximation algorithm for the chromatic number of $K_{4k_0+1}$-minor-free graphs with additive error strictly between $k_0/4$ (the lower bound of Corollary 4) and $k_0 - 2$ (the upper bound of Kawarabayashi et al.)?

Context

Kawarabayashi et al. showed the chromatic number of $K_k$-minor-free graphs can be approximated additively up to $k-2$. Corollary 4 of this paper establishes that an additive error of $k_0 - 1$ is NP-hard to achieve, leaving a gap of roughly a factor of 4 between the best known algorithm and the hardness bound.

Notes. PDF source; stated in prose as 'We leave open the question whether a better additive approximation (of course above the bound ≈ k/4 given by Corollary 4) is possible'.

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
