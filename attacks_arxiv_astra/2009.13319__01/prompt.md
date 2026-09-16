Attack the following open graph-theory problem.

Catalog id: 2009.13319__01
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/2009.13319__01/
Source paper: Extension of Gyarfas-Sumner conjecture to digraphs (arXiv:2009.13319)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 4.2
Let $H$ be a hero and let $F$ be an oriented forest. The set $\{\overleftrightarrow{K_2}, H, F\}$ is heroic if and only if: either $F$ is the disjoint union of oriented stars, or $H$ is a transitive tournament.

Context:
This is the main conjecture of the paper, a digraph analog of the Gyárfás-Sumner conjecture for oriented graphs. The 'only if' direction is proved in Section 6.1. The case where both conditions hold simultaneously (H a transitive tournament and F a disjoint union of oriented stars) is already settled by Chudnovsky, Scott and Seymour [6].

=== Catalog page (statement + literature review) ===
Heroic triple characterization via transitive tournaments — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The 'only if' direction of Conjecture 4.2 is established in the source paper, and the case where both conditions hold simultaneously was resolved prior to posting by Chudnovsky–Scott–Seymour. Several special cases of the 'if' direction have since been proved: Aboulker, Aubian, and Charbit (2021) prove the case F = S₂⁺ with H = C₃; Aboulker, Aubian, Charbit, and Thomassé (2022) establish bounded dichromatic number for ⃗P₆-free triangle-free oriented graphs. A 2026 preprint by Aubian and Kuffner claims to disprove a conjecture of Aboulker, Charbit, and Naserasr via (claw, C₃)-free digraphs with unbounded dichromatic number, but the precise connection to Conjecture 4.2 was not confirmed from the abstract alone.

 Cited literature (3)

 
 
 
partial Decomposing and colouring some locally semicomplete digraphs
 (2021)
 

 
 Pierre Aboulker, Guillaume Aubian, Pierre Charbit · arXiv preprint · arXiv:2103.07886

Proves the first open special case of the 'if' direction with F = S₂⁺ and H = C₃ by showing every locally out-transitive oriented graph has dichromatic number at most 2.
 

 
 
partial (P6, triangle)-free digraphs have bounded dichromatic number
 (2022)
 

 
 Pierre Aboulker, Guillaume Aubian, Pierre Charbit, Stéphan Thomassé · arXiv preprint · arXiv:2212.02272

Establishes dichromatic number at most 382 for oriented graphs that are both ⃗P₆-free and triangle-free, verifying a special case of the conjecture in this restricted graph class.
 

 
 
counterexample (Claw, C⃗₃)-free digraphs with unbounded dichromatic number
 (2026)
 

 
 Guillaume Aubian, Luis Kuffner · arXiv preprint · arXiv:2602.08736

Constructs claw-free oriented digraphs with no directed C₃ but unbounded dichromatic number, claiming to disprove a conjecture of Aboulker, Charbit and Naserasr; the precise connection to Conjecture 4.2 specifically is not confirmed from the abstract alone.
 

 

 Reviewer notes. The 'only if' direction is fully proved in the source paper. The 'if' direction splits into two branches: (a) H is a transitive tournament (any oriented forest F), and (b) F is a disjoint union of oriented stars (any hero H). Special cases of branch (b) are addressed by arXiv:2103.07886 (F = S₂⁺, H = C₃) and arXiv:2212.02272 (⃗P₆-free, triangle-free case). The 2026 paper arXiv:2602.08736 by Aubian and Kuffner constructs digraphs disproving 'a conjecture of Aboulker, Charbit and Naserasr', but without access to the full text it cannot be determined whether this is Conjecture 4.2 specifically or a different conjecture from their body of work. The Steiner (2023) Journal of Graph Theory paper (arXiv:2103.04191) was identified in search results as proving the locally transitive tournament case, but was not fetched and is therefore not cited.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $H$ be a hero and let $F$ be an oriented forest. The set $\{\overleftrightarrow{K_2}, H, F\}$ is heroic if and only if: either $F$ is the disjoint union of oriented stars, or $H$ is a transitive tournament.

Context

This is the main conjecture of the paper, a digraph analog of the Gyárfás-Sumner conjecture for oriented graphs. The 'only if' direction is proved in Section 6.1. The case where both conditions hold simultaneously (H a transitive tournament and F a disjoint union of oriented stars) is already settled by Chudnovsky, Scott and Seymour [6].

Notes. PDF source — key symbols ($\overleftrightarrow{K_2}$, dichromatic number) inferred from context; the dichromatic number notation appears as '(cid:126)χ' in the raw PDF extraction.

Source paper

 Extension of Gyarfas-Sumner conjecture to digraphs
 Pierre Aboulker, Pierre Charbit, Reza Naserasr · 2020-09-28
 https://arxiv.org/abs/2009.13319
 PDF source

Related conjectures

 
 implied by
 Heroic sets for bounded dichromatic number
 partial
 Genuine restriction within the same paper. The general problem asks to characterize ALL heroic finite sets of digraphs; the conjecture proposes the exact characterization for the subfamily of triples of the form {bidirected K_2, H, F} with H a hero and F an oriented forest — these are finite sets, so any complete answer to the general problem determines, in particular, which such triples are heroic and thereby settles the conjecture. Caveat on typing: the source is a characterization Problem, not a truth-valued statement, so 'implies' here is resolution-implication (a solution to the source resolves the target), which is exactly the 'via restriction' convention; the general problem does not force the conjectured characterization to be the correct one.
 

 
 implies
 Heroic triple with oriented forest and K_k
 partial
 Instantiate the full characterization (Conjecture 4.2) with H = TT_k: TT_k is itself a transitive tournament, so the second disjunct of the 'if' condition holds trivially and the instance reduces to '{digon, TT_k, F} is heroic for every oriented forest F and every k'. The paper explicitly states (in the target's own context) that this special case is equivalent to the target conjecture about {digon, K_k, F}, via the Ramsey fact that every tournament on 2^k vertices contains TT_k, which makes forbidding the edgeless K_k interchangeable with forbidding TT_k in digon-free digraphs. Full conjecture implies its instance implies the target; direction as claimed (source is the general characterization, target a special case).
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:The dichromatic number of a digraph $D$ is the minimum number of colors needed to color its vertices in such a way that each color class induces an acyclic digraph. As it generalizes the notion of the chromatic number of graphs, it has been a recent center of study. In this work we look at possible extensions of Gyárfás-Sumner conjecture. More precisely, we propose as a conjecture a simple characterization of finite sets $\mathcal F$ of digraphs such that every oriented graph with sufficiently large dichromatic number must contain a member of $\mathcal F$ as an induce subdigraph.
Among notable results, we prove that oriented triangle-free graphs without a directed path of length $3$ are $2$-colorable. If condition of "triangle-free" is replaced with "$K_4$-free", then we have an upper bound of $414$. We also show that an orientation of complete multipartite graph with no directed triangle is 2-colorable. To prove these results we introduce the notion of \emph{nice sets} that might be of independent interest.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:2009.13319 [math.CO]
 

 
  
 (or 
 arXiv:2009.13319v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2009.13319
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Pierre Aboulker [view email] 
 [v1]
 Mon, 28 Sep 2020 13:41:38 UTC (41 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Extension of Gyarfas-Sumner conjecture to digraphs, by Pierre Aboulker and 2 other authors
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
 | 2020-09
 

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
