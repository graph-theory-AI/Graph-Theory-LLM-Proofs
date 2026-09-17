Attack the following open graph-theory problem.

Catalog id: 2302.08922__01
Catalog status: partial (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2302.08922__01/
Source paper: A note on the Gyárfás-Sumner conjecture (arXiv:2302.08922)

=== Extracted statement (catalog JSON) ===
Title: Polynomial bounds for the Gyárfás-Sumner conjecture
It is possible that the Gy\'{a}rf\'{a}s-Sumner conjecture holds with polynomial bounds; that is, 1.1 holds with a bound on the chromatic number that is polynomial in $t$.

Context:
The authors note that polynomial bounds on the $\chi$-bounding function have recently been established for trees not containing $P_5$ as an induced subgraph, and suggest that the full Gyárfás-Sumner conjecture may admit a polynomial $\chi$-bounding function in $t$ for every fixed tree $T$.

=== Catalog page (statement + literature review) ===
Polynomial χ-bounding in Gyárfás-Sumner — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The conjecture that the Gyárfás-Sumner conjecture holds with polynomial χ-bounding functions (chromatic number bounded by a polynomial in the clique number t) remains open in full generality. Significant partial progress has been made since 2023: polynomial χ-boundedness was established for P₅-free graphs (arXiv:2512.24907, Dec 2024), and the polynomial version of the conjecture was proved for intersection graphs of axis-aligned boxes of any fixed dimension (arXiv:2407.16882, Jul 2024). A further 2025 preprint (arXiv:2504.21127) improves bounds for P₅-free graphs and gives compositional results, but the full polynomial conjecture for all trees is still open.

 Cited literature (3)

 
 
 
partial Polynomial Gyárfás-Sumner conjecture for graphs of bounded boxicity
 (2024)
 

 
 not confirmed in fetch · arXiv preprint · arXiv:2407.16882

Proves the polynomial Gyárfás-Sumner conjecture for intersection graphs of axis-aligned boxes in ℝ^d (graphs of bounded boxicity): for every positive integer d and forest F, such graphs with no induced F are polynomially χ-bounded.
 

 
 
partial Polynomial χ-boundedness for excluding P₅
 (2024)
 

 
 not confirmed in fetch · arXiv preprint · arXiv:2512.24907

Proves that the chromatic number is polynomially bounded by the clique number for graphs with no induced five-vertex path P₅, resolving this case of the polynomial Gyárfás-Sumner conjecture via a chromatic density framework.
 

 
 
partial On polynomially high-chromatic pure pairs
 (2025)
 

 
 Tung H. Nguyen · arXiv preprint · arXiv:2504.21127

Improves the best known bound for P₅-free graphs from χ(G) ≤ ω^(log ω) to χ(G) ≤ ω^(O(log ω / log log ω)), and establishes that if T and a broom each satisfy the polynomial Gyárfás-Sumner conjecture then so does their disjoint union.
 

 

 Reviewer notes. Esperet's broader conjecture that every χ-bounded hereditary class is polynomially χ-bounded was disproved by Briański, Davies and Walczak, but that does not affect this specific conjecture about forest-free graphs. The most notable advance is arXiv:2512.24907 (Dec 2024) proving polynomial χ-boundedness for P₅-free graphs. Author names for arXiv:2407.16882 and arXiv:2512.24907 were not returned by WebFetch and are marked accordingly.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. It is possible that the Gy\'{a}rf\'{a}s-Sumner conjecture holds with polynomial bounds; that is, 1.1 holds with a bound on the chromatic number that is polynomial in $t$.

Context

The authors note that polynomial bounds on the $\chi$-bounding function have recently been established for trees not containing $P_5$ as an induced subgraph, and suggest that the full Gyárfás-Sumner conjecture may admit a polynomial $\chi$-bounding function in $t$ for every fixed tree $T$.

Notes. Stated in prose as 'it is possible that…' without a labelled conjecture environment.

Source paper

 A note on the Gyárfás-Sumner conjecture
 Tung Nguyen, Alex Scott, Paul Seymour · 2023-02-17
 https://arxiv.org/abs/2302.08922
 PDF source

Related conjectures

 
 same conjecture as
 Polynomial χ-boundedness for forest-free graphs
 partial
 Both statements are the polynomial Gyárfás–Sumner conjecture. In 2302.08922 (Nguyen–Scott–Seymour), t is the bound on clique size (verified from the abstract: 'no clique of size t'), so 'chromatic number polynomial in t' is exactly 'χ(G) ≤ poly(ω(G))', the same parameterization as the source. The only wording gap is forest (source) vs tree (target): a tree is a forest, and conversely any forest H is an induced subgraph of the tree T obtained by adding one new vertex adjacent to one vertex of each component, so H-free ⊆ T-free and the tree version transfers polynomial bounds to the forest version. Hence the two statements are polynomially equivalent formulations of one conjecture.
 

 
 implies
 Graphs with a forbidden induced tree are chi-bounded
 partial
 The source asserts that for every fixed tree T the class of T-free graphs admits a chi-bounding function polynomial in the clique number; a polynomial chi-bounding function is in particular a chi-bounding function, so the target (Gyárfás-Sumner: T-free graphs are chi-bounded) follows immediately. Strictly stronger statement, same hypothesis class (T-free graphs for every fixed tree T), monotone strengthening of the conclusion only. Direction as claimed. (The source is phrased informally as 'it is possible that...', but read as a conjecture the implication is trivial.)
 

 
 implies
 Polynomial χ-bound for path-induced rooted tree
 open
 Per the paper's definition (verified on arXiv:2302.08922), a copy H of T in G is path-induced if every path of H with one end at the distinguished root r is an induced path of G. If G contains T as an induced subgraph, then G[V(H)] = H is a tree, and every path of a tree is induced in it, hence induced in G; so any induced copy is a path-induced copy for any root. Therefore graphs with no path-induced copy of (T,r) form a subclass of T-(induced-)free graphs. Polynomial Gyarfas-Sumner (source) gives chi(G) <= poly(omega(G)) for all T-free graphs; on the subclass with omega <= t this yields chi <= poly(t), which is exactly an affirmative answer to Question __00 (polynomial strengthening of their Theorem 1.2). Hypothesis-class containment, direction as claimed.
 

 
 implied by
 Polynomial χ-boundedness for forest-free graphs
 partial
 Pure hypothesis-class containment. The source asserts polynomial chi-bounding of H-free graphs for every forest H; the target asserts it for every tree T (the Gyarfas-Sumner conjecture with polynomial bounds, with t the clique parameter, matching f(omega) polynomial in omega). Every tree is a forest, so the target is exactly the restriction of the source's universal quantifier to connected H. Parameterizations agree (both bound chi by a polynomial in the clique number). The converse (trees imply forests) may also hold via disjoint-union arguments but is not needed for the claimed direction.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:The Gyárfás-Sumner conjecture says that for every tree $T$ and every integer $t\ge 1$, if $G$ is a graph with no clique of size $t$ and with sufficiently large chromatic number, then $G$ contains an induced subgraph isomorphic to $T$. This remains open, but we prove that under the same hypotheses, $G$ contains a subgraph $H$ isomorphic to $T$ that is ``path-induced''; that is, for some distinguished vertex~$r$, every path of $H$ with one end $r$ is an induced path of $G$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2302.08922 [math.CO]
 

 
  
 (or 
 arXiv:2302.08922v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2302.08922
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Fri, 17 Feb 2023 14:52:52 UTC (7 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A note on the Gy\'arf\'as-Sumner conjecture, by Tung Nguyen and 2 other authors
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
 | 2023-02
 

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
