Attack the following open graph-theory problem.

Catalog id: 2310.04265__05
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2310.04265__05/
Source paper: Clique number of tournaments (arXiv:2310.04265)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 4.3 (Gyárfás-Sumner for Tournaments)
A tournament $H$ is $\operatorname{\overrightarrow{\chi}}$-binding if and only if $H$ has a backedge graph which is a forest.

Context:
The authors propose this as the directed analogue of the celebrated Gyárfás-Sumner Conjecture, where a tournament $H$ is $\operatorname{\overrightarrow{\chi}}$-binding if the class of tournaments not containing $H$ as a subtournament is $\operatorname{\overrightarrow{\chi}}$-bounded. The 'only if' direction is proved as Theorem 4.4, and it is shown that it suffices to prove the 'if' direction for trees.

=== Catalog page (statement + literature review) ===
χ⃗-binding tournaments with forest backedge graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The 'only if' direction of this biconditional conjecture was established in the source paper itself (Theorem 4.4), and the open 'if' direction was further reduced to the case of trees. No subsequent work proving the remaining implication has been found. A closely related follow-up by three of the four original authors (arXiv:2402.10782, revised January 2026) proves that deciding whether a tournament admits a forest-ordering — the right-hand-side structural condition — is NP-complete, indicating computational hardness around that condition but leaving the χ̄-binding implication open.

 Cited literature (1)

 
 
 
partial Finding forest-orderings of tournaments is NP-complete
 (2024)
 

 
 Pierre Aboulker, Guillaume Aubian, Raul Lopes · arXiv preprint · arXiv:2402.10782

Proves that deciding whether a tournament admits an ordering whose backedge graph is a forest (the right-hand-side condition of Conjecture 4.3) is NP-complete, and connects this to dichromatic number and Erdős-Hajnal properties, but does not resolve the χ̄-binding implication.
 

 

 Reviewer notes. The conjecture as stated already has the 'only if' direction proved in the source paper (Theorem 4.4), so the genuinely open part is the 'if' direction, further reduced to trees. arXiv:2402.10782 establishes NP-completeness of detecting the forest-ordering condition but does not prove the χ̄-binding implication. The conjecture is the directed analogue of the undirected Gyárfás-Sumner conjecture, which is itself still open in general.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. A tournament $H$ is $\operatorname{\overrightarrow{\chi}}$-binding if and only if $H$ has a backedge graph which is a forest.

Context

The authors propose this as the directed analogue of the celebrated Gyárfás-Sumner Conjecture, where a tournament $H$ is $\operatorname{\overrightarrow{\chi}}$-binding if the class of tournaments not containing $H$ as a subtournament is $\operatorname{\overrightarrow{\chi}}$-bounded. The 'only if' direction is proved as Theorem 4.4, and it is shown that it suffices to prove the 'if' direction for trees.

Source paper

 Clique number of tournaments
 Pierre Aboulker, Guillaume Aubian, Pierre Charbit, Raul Lopes · 2023-10-06
 https://arxiv.org/abs/2310.04265

=== Source paper abstract / header ===
Abstract:Given a digraph $D$ together with an ordering $\prec$ of its vertices, the \emph{backedge graph} of $D$ with respect to $\prec$ is the undirected graph $D^{\prec}$ with the same vertex set as $D$, where $xy \in E(D^{\prec})$ if $xy \in A(D)$ and $y \prec x$. We introduce the notion of the \emph{clique number of a digraph} $D$, defined as the minimum clique number over all backedge graphs of $D$. We investigate its relationship with the dichromatic number. In particular, this concept allows us to define $\dic$-bounded classes of digraphs, which constitute the main topic of this paper, with a primary focus on tournaments. A class of tournaments is $\dic$-bounded if, for every tournament in the class, its dichromatic number is bounded by a function of its clique number. We study for which tournaments $H$ the class of $H$-free tournaments is $\dic$-bounded, and prove in particular that $H$ must have a backedge graph that is a forest. We prove that if a class of tournaments is $\dic$-bounded, then so is its closure under substitution. We also explore the relationship between $\dic$-bounded classes of tournaments and certain conjectures on tournaments. We prove that a $\dic$-bounded class of tournaments satisfies the $BIG \Rightarrow BIG$ Conjecture, and that a polynomially $\dic$-bounded class of tournaments satisfies the (tournament) Erdős-Hajnal Conjecture.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C20
 

 Cite as:
 arXiv:2310.04265 [math.CO]
 

 
  
 (or 
 arXiv:2310.04265v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2310.04265
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Pierre Aboulker [view email] 
 [v1]
 Fri, 6 Oct 2023 14:11:26 UTC (31 KB)

 [v2]
 Mon, 22 Jun 2026 10:06:06 UTC (31 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Clique number of tournaments, by Pierre Aboulker and 3 other authors
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
 | 2023-10
 

 Change to browse by:
 
 cs
 cs.DM
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
