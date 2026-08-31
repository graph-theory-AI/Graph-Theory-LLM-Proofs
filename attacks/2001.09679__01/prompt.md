Attack the following open graph-theory problem.

Catalog id: 2001.09679__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2001.09679__01/
Source paper: A note on sublinear separators and expansion (arXiv:2001.09679)

=== Catalog page (statement + literature review) ===
One-sided sublinear separator expansion equality — Graph-theory open problems (arXiv)

 
 Status
 open
 low confidence
 

 No follow-up work resolving the conjecture $b'_\varepsilon = b_\varepsilon$ for $0 < \varepsilon < \frac{1}{2}$ was found in five web calls. Dvořák published related work on weighted sublinear separators (Journal of Graph Theory, 2022) and, with Wood, on product structure of graph classes with strongly sublinear separators (arXiv:2208.10074, 2022), but neither paper appears to address this specific parameter-equality question. The conjecture is now six years old; absence of a resolution in the indexed literature is somewhat surprising for a problem of this age, but the question is technically narrow and may simply not yet have attracted a focused attack.

 Reviewer notes. The Wiley page for Dvořák's 2022 JGT paper 'On weighted sublinear separators' (DOI 10.1002/jgt.22777) returned HTTP 402 (paywall) so its relevance to the conjecture could not be verified; it is not included in since_posted. The arXiv:2208.10074 paper by Dvořák–Wood works in an adjacent area but its abstract does not mention the b_epsilon/b'_epsilon parameters or the conjecture. No arXiv preprint for the 2022 JGT paper was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It seems likely that $b'_\varepsilon = b_\varepsilon$ when $0 < \varepsilon < \frac{1}{2}$ as well.

Context

The parameter $b'_\varepsilon$ is defined analogously to $b_\varepsilon$ but with the one-sided condition $s_\mathcal{G}(n)=\Omega(n^{1-\varepsilon})$ rather than $\Theta(n^{1-\varepsilon})$; equality $b'_\varepsilon=b_\varepsilon=0$ already holds for $\frac{1}{2}\leq\varepsilon\leq 1$, but extending this to $0<\varepsilon<\frac{1}{2}$ requires showing that a one-sided lower bound on separators alone forces the same expansion lower bound, which is not obvious.

Notes. Conjectural language 'It seems likely' appears in the final section. PDF source.

Source paper

 A note on sublinear separators and expansion
 Zdeněk Dvořák · 2020-07-07
 https://arxiv.org/abs/2001.09679
 PDF source

=== Source paper abstract / header ===
Abstract:For a hereditary class C of graphs, let s_C(n) be the minimum function such that each n-vertex graph in C has a balanced separator of order at most s_C(n), and let nabla_C(r) be the minimum function bounding the expansion of C, in the sense of bounded expansion theory of Nešetřil and Ossona de Mendez. The results of Plotkin, Rao, and Smith (1994) and Esperet and Raymond (2018) imply that if s_C(n)=Theta(n^{1-epsilon}) for some epsilon>0, then nabla_C(r)=Omega(r^{1/(this http URL)-1}/polylog r) and nabla_C(r)=O(r^{1/epsilon-1}polylog r). Answering a question of Esperet and Raymond, we show that neither of the exponents can be substantially improved.
 

 
 
 
 Comments:
 10 pages, no figures; updated according to the reviewer remarks
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C75
 

 Cite as:
 arXiv:2001.09679 [math.CO]
 

 
  
 (or 
 arXiv:2001.09679v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2001.09679
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Mon, 27 Jan 2020 10:48:05 UTC (8 KB)

 [v2]
 Tue, 7 Jul 2020 18:52:45 UTC (8 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A note on sublinear separators and expansion, by Zden\v{e}k Dvo\v{r}\'ak
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
 | 2020-01
 

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
