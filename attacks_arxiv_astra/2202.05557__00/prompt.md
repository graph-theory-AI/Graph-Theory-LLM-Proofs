Attack the following open graph-theory problem.

Catalog id: 2202.05557__00
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2202.05557__00/
Source paper: Polynomial bounds for chromatic number. V. Excluding a tree of radius t… (arXiv:2202.05557)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.3
For every forest $H$, there is a polynomial $f$ such that $\chi(G) \leq f(\omega(G))$ for every $H$-free graph $G$.

Context:
This conjecture is presented as what the Gyárfás-Sumner conjecture (1.1) and Esperet's conjecture (that every $\chi$-bounded hereditary class has a polynomial bounding function) would jointly imply for forest-free graph classes. Esperet's conjecture has been disproved in full generality but remains open for classes excluding a forest, and Conjecture 1.3 is known only for a few special families of trees.

=== Catalog page (statement + literature review) ===
Polynomial χ-boundedness for forest-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 1.3 — polynomial chi-boundedness for every forest-free graph class — remains open in full generality as of May 2026. Significant partial progress has been made: Nguyen (arXiv:2512.24907, 2025) proved the conjecture for H = P_5, the five-vertex path, resolving a case open since 1985; Davies and Yuditsky (arXiv:2407.16882, 2024) proved it for all forests H when the host graphs have bounded boxicity. The ongoing Scott–Seymour series establishes polynomial bounds for several additional tree families, but no uniform proof for all forests exists.

 Cited literature (2)

 
 
 
partial Polynomial χ-boundedness for excluding P₅
 (2025)
 

 
 Tung H. Nguyen · arXiv preprint · arXiv:2512.24907

Proves that every P₅-free graph G satisfies χ(G) ≤ f(ω(G)) for a polynomial f, establishing Conjecture 1.3 for the specific forest H = P₅ (the five-vertex path).
 

 
 
partial Polynomial Gyárfás-Sumner conjecture for graphs of bounded boxicity
 (2024)
 

 
 James Davies, Yelena Yuditsky · arXiv preprint · arXiv:2407.16882

Proves Conjecture 1.3 for every forest H when restricted to intersection graphs of axis-aligned boxes in ℝ^d (graphs of bounded boxicity).
 

 

 Reviewer notes. Conjecture 1.3 is closely related to Esperet's conjecture (polynomial chi-boundedness for hereditary classes, now disproved in general) and to the Gyárfás-Sumner conjecture (which concerns bounded chromatic number, not polynomial bounds). The P5 case (arXiv:2512.24907) and the bounded-boxicity case (arXiv:2407.16882) are the most notable post-2023 advances. Internal reference 2508.14332 appears unrelated.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every forest $H$, there is a polynomial $f$ such that $\chi(G) \leq f(\omega(G))$ for every $H$-free graph $G$.

Context

This conjecture is presented as what the Gyárfás-Sumner conjecture (1.1) and Esperet's conjecture (that every $\chi$-bounded hereditary class has a polynomial bounding function) would jointly imply for forest-free graph classes. Esperet's conjecture has been disproved in full generality but remains open for classes excluding a forest, and Conjecture 1.3 is known only for a few special families of trees.

Notes. Stated in the paper without a parenthesised attribution; it is a natural combination of Conjecture 1.1 and Esperet's conjecture restricted to forest-free classes.

Source paper

 Polynomial bounds for chromatic number. V. Excluding a tree of radius two and a complete multipartite graph
 Alex Scott, Paul Seymour · 2023-01-10
 https://arxiv.org/abs/2202.05557
 PDF source

Related conjectures

 
 same conjecture as
 Polynomial χ-boundedness for H-free forest classes
 partial
 The target states 'perhaps every forest is good', where good is defined as: the class of H-free graphs is polynomially chi-bounded. Unfolding the definition gives exactly the source statement: for every forest H there is a polynomial f such that chi(G) <= f(omega(G)) for every H-free graph G. Both are the polynomial Gyarfas-Sumner conjecture, raised in the same 2022 line of work on polynomial chi-boundedness following the disproof of Esperet's conjecture (which both contexts cite). Identical quantification over forests, identical class (H-free graphs), identical polynomial bound; genuinely the same conjecture, not a name collision.
 

 
 same conjecture as
 Polynomial χ-boundedness for H-free forests
 partial
 Both statements are the polynomial strengthening of the Gyarfas-Sumner conjecture, with identical quantification and content: for every forest H, the class of H-free graphs is polynomially chi-bounded, i.e., there is a polynomial f with chi(G) <= f(omega(G)) for every H-free graph G. The target phrases it via the definition 'H is good' meaning exactly 'the class of H-free graphs is polynomially chi-bounded', and explicitly calls it the strengthening of Gyarfas-Sumner from chi-boundedness to polynomial chi-boundedness. Same forest quantifier, same graph class, same polynomial bound shape; not a fuzzy false match.
 

 
 same conjecture as
 Polynomial χ-bounding in Gyárfás-Sumner
 partial
 Both statements are the polynomial Gyárfás–Sumner conjecture. In 2302.08922 (Nguyen–Scott–Seymour), t is the bound on clique size (verified from the abstract: 'no clique of size t'), so 'chromatic number polynomial in t' is exactly 'χ(G) ≤ poly(ω(G))', the same parameterization as the source. The only wording gap is forest (source) vs tree (target): a tree is a forest, and conversely any forest H is an induced subgraph of the tree T obtained by adding one new vertex adjacent to one vertex of each component, so H-free ⊆ T-free and the tree version transfers polynomial bounds to the forest version. Hence the two statements are polynomially equivalent formulations of one conjecture.
 

 
 implies
 Forests are multibounding chromatic bound
 open
 Stated explicitly in the target's context: 'any forest satisfying the polynomial-bound Conjecture 1.2 is multibounding.' The self-contained argument: K_{dt} contains K_d(t) (complete d-partite with parts of size t) as a subgraph, so an H-free graph G with no K_d(t) subgraph has omega(G) < dt; the source's polynomial f then gives chi(G) <= f(omega(G)) <= f(dt), which for each fixed d is a polynomial in t, i.e. H is multibounding. This holds for every forest H, giving the target in full. Direction correct: the unconditional polynomial omega-bound is the stronger hypothesis.
 

 
 implies
 Graphs with a forbidden induced tree are chi-bounded
 partial
 Direct weakening in two independent ways: every tree T is a forest, so the source instantiated at H = T applies; and a polynomial χ-bounding function f is in particular a χ-bounding function. So if for every forest H there is a polynomial f with χ(G) ≤ f(ω(G)) for H-free G, then for every tree T the class of T-free graphs is χ-bounded, which is exactly the Gyárfás–Sumner conjecture as stated in the target. Hypothesis classes and parameterization (χ vs ω, induced-subgraph exclusion) match exactly. Direction is correct: source is strictly stronger (polynomial vs arbitrary bounding function, forests vs trees).
 

 
 implies
 Polynomial χ-bounding in Gyárfás-Sumner
 partial
 Pure hypothesis-class containment. The source asserts polynomial chi-bounding of H-free graphs for every forest H; the target asserts it for every tree T (the Gyarfas-Sumner conjecture with polynomial bounds, with t the clique parameter, matching f(omega) polynomial in omega). Every tree is a forest, so the target is exactly the restriction of the source's universal quantifier to connected H. Parameterizations agree (both bound chi by a polynomial in the clique number). The converse (trees imply forests) may also hold via disjoint-union arguments but is not needed for the claimed direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:The Gyárfás-Sumner conjecture says that for every forest $H$ and every integer $k$, if $G$ is $H$-free and does not contain a clique on $k$ vertices then it has bounded chromatic number. (A graph is $H$-free if it does not contain an induced copy of $H$.) Kierstead and Penrice proved it for trees of radius at most two, but otherwise the conjecture is known only for a few simple types of forest. More is known if we exclude a complete bipartite subgraph instead of a clique: Rödl showed that, for every forest $H$, if $G$ is $H$-free and does not contain $K_{t,t}$ as a subgraph then it has bounded chromatic number. In an earlier paper with Sophie Spirkl, we strengthened Rödl's result, showing that for every forest $H$, the bound on chromatic number can be taken to be polynomial in $t$. In this paper, we prove a related strengthening of the Kierstead-Penrice theorem, showing that for every tree $H$ of radius two and every integer $d\ge 2$, if $G$ is $H$-free and does not contain as a subgraph the complete $d$-partite graph with parts of cardinality $t$, then its chromatic number is at most polynomial in $t$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2202.05557 [math.CO]
 

 
  
 (or 
 arXiv:2202.05557v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2202.05557
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Fri, 11 Feb 2022 11:28:16 UTC (15 KB)

 [v2]
 Tue, 10 Jan 2023 08:39:10 UTC (15 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Polynomial bounds for chromatic number. V. Excluding a tree of radius two and a complete multipartite graph, by Alex Scott and 1 other authors
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
 | 2022-02
 

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
