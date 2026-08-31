Attack the following open graph-theory problem.

Catalog id: 2006.09877__01
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2006.09877__01/
Source paper: Twin-width II: small classes (arXiv:2006.09877)

=== Catalog page (statement + literature review) ===
Bounded twin-width for polynomial expansion classes — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The question of whether classes with polynomial expansion have bounded twin-width remains open as of 2026, confirmed by Bonnet's own open-problems page which lists it with the note 'we are quite far from proving it.' Twin-width IV (arXiv:2102.03117) gives a partial resolution for hereditary classes of ordered graphs, showing bounded twin-width and sub-exponential growth are equivalent in that setting. The related but strictly more general 'small conjecture' (every small class has bounded twin-width) was disproved by Twin-width VII (arXiv:2204.12330), which constructs via a Cayley-graph argument a small class with unbounded twin-width; however, that counterexample does not have polynomial expansion, so the polynomial-expansion question remains open and isolated.

 Cited literature (2)

 
 
 
partial Twin-width IV: ordered graphs and matrices
 (2021)
 

 
 Édouard Bonnet, Ugo Giocanti, Patrice Ossona de Mendez, Pierre Simon, Stéphan Thomassé, Rémi Watrigant · arXiv preprint · arXiv:2102.03117

Proves that for hereditary classes of ordered graphs, bounded twin-width is equivalent to sub-exponential (2^{O(n)}) growth, giving a partial resolution of the conjecture in the ordered setting.
 

 
 
partial Twin-width VII: groups
 (2022)
 

 
 Édouard Bonnet, Colin Geniet, Romain Tessera, Stéphan Thomassé · arXiv preprint · arXiv:2204.12330

Disproves the more general 'small conjecture' by constructing (via a finitely generated group with infinite twin-width, Theorem 1.1) a small hereditary class with unbounded twin-width (Corollary 1.4); the counterexample is not a class with polynomial expansion, so the polynomial-expansion question itself remains open.
 

 

 Reviewer notes. Bonnet's open-problems page (fetched 2026-05-15) explicitly lists this question as open with the remark 'we are quite far from proving it.' The small conjecture (small ⇒ bounded twin-width) was disproved by Twin-width VII; the polynomial expansion question is a strictly harder sub-question that survives the disproof because the Cayley-graph counterexample lacks polynomial expansion.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Do classes with polynomial expansion have bounded twin-width?

Context

Towards the small conjecture, the authors identify showing that small sparse classes have bounded (sparse) twin-width as a first, challenging step. Since classes with polynomial expansion are small, confirming bounded twin-width for them would constitute meaningful progress.

Notes. Stated as an explicit open question in the introduction without a labelled environment. PDF extraction is truncated; additional numbered questions may appear in later sections.

Source paper

 Twin-width II: small classes
 Édouard Bonnet, Colin Geniet, Eun Jung Kim, Stéphan Thomassé, Rémi Watrigant · 2020-06-17
 https://arxiv.org/abs/2006.09877
 PDF source

=== Source paper abstract / header ===
Abstract:The twin-width of a graph $G$ is the minimum integer $d$ such that $G$ has a $d$-contraction sequence, that is, a sequence of $|V(G)|-1$ iterated vertex identifications for which the overall maximum number of red edges incident to a single vertex is at most $d$, where a red edge appears between two sets of identified vertices if they are not homogeneous in $G$. We show that if a graph admits a $d$-contraction sequence, then it also has a linear-arity tree of $f(d)$-contractions, for some function $f$. First this permits to show that every bounded twin-width class is small, i.e., has at most $n!c^n$ graphs labeled by $[n]$, for some constant $c$. This unifies and extends the same result for bounded treewidth graphs [Beineke and Pippert, JCT '69], proper subclasses of permutations graphs [Marcus and Tardos, JCTA '04], and proper minor-free classes [Norine et al., JCTB '06]. The second consequence is an $O(\log n)$-adjacency labeling scheme for bounded twin-width graphs, confirming several cases of the implicit graph conjecture. We then explore the "small conjecture" that, conversely, every small hereditary class has bounded twin-width. Inspired by sorting networks of logarithmic depth, we show that $\log_{\Theta(\log \log d)}n$-subdivisions of $K_n$ (a small class when $d$ is constant) have twin-width at most $d$. We obtain a rather sharp converse with a surprisingly direct proof: the $\log_{d+1}n$-subdivision of $K_n$ has twin-width at least $d$. Secondly graphs with bounded stack or queue number (also small classes) have bounded twin-width. Thirdly we show that cubic expanders obtained by iterated random 2-lifts from $K_4$~[Bilu and Linial, Combinatorica '06] have bounded twin-width, too. We suggest a promising connection between the small conjecture and group theory. Finally we define a robust notion of sparse twin-width and discuss how it compares with other sparse classes.
 

 
 
 
 Comments:
 37 pages, 9 figures
 

 Subjects:
 
 Discrete Mathematics (cs.DM); Data Structures and Algorithms (cs.DS); Logic in Computer Science (cs.LO); Combinatorics (math.CO)
 
 
 MSC classes:
 68R10, 05C30, 05C48
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:2006.09877 [cs.DM]
 

 
  
 (or 
 arXiv:2006.09877v1 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2006.09877
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Wed, 17 Jun 2020 13:57:09 UTC (79 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Twin-width II: small classes, by \'Edouard Bonnet and 4 other authors
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
 | 2020-06
 

 Change to browse by:
 
 cs
 cs.DS
 cs.LO
 math
 math.CO
 

 

 

 
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
