Attack the following open graph-theory problem.

Catalog id: 2004.14789__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.14789__00/
Source paper: Twin-width I: tractable FO model checking (arXiv:2004.14789)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture (polynomial expansion and bounded twin-width)
All classes of polynomial expansion may also have bounded twin-width.

Context:
The authors note that proper minor-closed classes have bounded twin-width, and observe that bounded twin-width is incomparable with bounded degree, bounded expansion, and nowhere denseness. They remark 'As far as we know, all classes of polynomial expansion may also have bounded twin-width,' suggesting this as an open direction. Figure 3 depicts this with a dash-dotted edge indicating possible inclusion.

=== Catalog page (statement + literature review) ===
Polynomial expansion implies bounded twin-width — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that all classes of polynomial expansion have bounded twin-width remains open as of 2026. Bonnet's TWIN-WIDTH ANR JCJC open-questions page explicitly lists this question and remarks 'If this is true, we are quite far from proving it.' No paper resolving or disproving the conjecture has been found in the indexed literature. The closely related question of whether every K_{t,t}-free string-graph class has twin-width bounded by a function of t is also listed as open.

 Reviewer notes. Bonnet's open-questions page (https://perso.ens-lyon.fr/edouard.bonnet/openQuestions.html) was verified via WebFetch and confirms the conjecture is still open with the remark 'If this is true, we are quite far from proving it.' No follow-up paper resolving it in either direction was found after four web calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. All classes of polynomial expansion may also have bounded twin-width.

Context

The authors note that proper minor-closed classes have bounded twin-width, and observe that bounded twin-width is incomparable with bounded degree, bounded expansion, and nowhere denseness. They remark 'As far as we know, all classes of polynomial expansion may also have bounded twin-width,' suggesting this as an open direction. Figure 3 depicts this with a dash-dotted edge indicating possible inclusion.

Notes. Stated in hedged prose ('as far as we know … may also'); clearly conjectural but no labelled environment.

Source paper

 Twin-width I: tractable FO model checking
 Édouard Bonnet, Eun Jung Kim, Stéphan Thomassé, Rémi Watrigant · 2021-10-25
 https://arxiv.org/abs/2004.14789
 PDF source

=== Source paper abstract / header ===
Abstract:Inspired by a width invariant defined on permutations by Guillemot and Marx [SODA '14], we introduce the notion of twin-width on graphs and on matrices. Proper minor-closed classes, bounded rank-width graphs, map graphs, $K_t$-free unit $d$-dimensional ball graphs, posets with antichains of bounded size, and proper subclasses of dimension-2 posets all have bounded twin-width. On all these classes (except map graphs without geometric embedding) we show how to compute in polynomial time a sequence of $d$-contractions, witness that the twin-width is at most $d$. We show that FO model checking, that is deciding if a given first-order formula $\phi$ evaluates to true for a given binary structure $G$ on a domain $D$, is FPT in $|\phi|$ on classes of bounded twin-width, provided the witness is given. More precisely, being given a $d$-contraction sequence for $G$, our algorithm runs in time $f(d,|\phi|) \cdot |D|$ where $f$ is a computable but non-elementary function. We also prove that bounded twin-width is preserved by FO interpretations and transductions (allowing operations such as squaring or complementing a graph). This unifies and significantly extends the knowledge on fixed-parameter tractability of FO model checking on non-monotone classes, such as the FPT algorithm on bounded-width posets by Gajarský et al. [FOCS '15].
 

 
 
 
 Comments:
 49 pages, 9 figures
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Discrete Mathematics (cs.DM); Logic in Computer Science (cs.LO)
 
 
 MSC classes:
 68Q25
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2004.14789 [cs.DS]
 

 
  
 (or 
 arXiv:2004.14789v3 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2004.14789
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Thu, 30 Apr 2020 14:05:41 UTC (89 KB)

 [v2]
 Wed, 23 Sep 2020 13:47:30 UTC (91 KB)

 [v3]
 Mon, 25 Oct 2021 15:10:57 UTC (93 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Twin-width I: tractable FO model checking, by \'Edouard Bonnet and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2020-04
 

 Change to browse by:
 
 cs
 cs.DM
 cs.LO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Édouard Bonnet
Eun Jung Kim
Stéphan Thomassé
Rémi Watrigant 

 

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
