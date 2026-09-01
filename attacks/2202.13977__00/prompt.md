Attack the following open graph-theory problem.

Catalog id: 2202.13977__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2202.13977__00/
Source paper: Pure pairs. X. Tournaments and the strong Erdos-Hajnal property (arXiv:2202.13977)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.5
A tournament has the strong EH-property if and only if it admits a numbering for which the backedge graph is a forest.

Context:
The paper proves (Theorem 1.4) that the forward direction holds: every tournament with the strong EH-property admits a numbering for which the backedge graph is a forest. The authors initially thought the converse unlikely but failed to find a counterexample. This would be a tournament analogue of Theorem 1.3, which characterises graphs with the strong EH-property as those for which one of $H$ or $\bar{H}$ is a forest.

=== Catalog page (statement + literature review) ===
Strong EH-property via backedge forest tournaments — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 1.5 of arXiv:2202.13977 asserts that the strong EH-property for tournaments is characterised exactly by the existence of a numbering whose backedge graph is a forest. The necessary direction (strong EH-property implies forest numbering) was established as Theorem 1.4 in the source paper, but the converse remains open. A 2024 paper (arXiv:2402.10782) proved that deciding whether a tournament admits such a forest-ordering is NP-complete, which is computationally related to the conjecture but does not resolve it.

 Cited literature (1)

 
 
 
partial Finding forest-orderings of tournaments is NP-complete
 (2024)
 

 
 (not extracted from abstract page) · arXiv preprint · arXiv:2402.10782

Proves that the problem of deciding whether a tournament admits a forest-ordering (equivalently, a feedback arc set inducing a forest) is NP-complete; explicitly motivated by the connection to the strong Erdos-Hajnal property but does not resolve Conjecture 1.5.
 

 

 Reviewer notes. The conjecture is recent (posted 2022, published 2023). The only post-statement follow-up found is arXiv:2402.10782 (2024), which addresses the computational complexity of verifying the forest-ordering condition (NP-complete) rather than the logical equivalence itself. No counterexample or proof of the converse direction was found. Conjecture 1.5 remains fully open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. A tournament has the strong EH-property if and only if it admits a numbering for which the backedge graph is a forest.

Context

The paper proves (Theorem 1.4) that the forward direction holds: every tournament with the strong EH-property admits a numbering for which the backedge graph is a forest. The authors initially thought the converse unlikely but failed to find a counterexample. This would be a tournament analogue of Theorem 1.3, which characterises graphs with the strong EH-property as those for which one of $H$ or $\bar{H}$ is a forest.

Source paper

 Pure pairs. X. Tournaments and the strong Erdos-Hajnal property
 Maria Chudnovsky, Alex Scott, Paul Seymour, Sophie Spirkl · 2023-08-08
 https://arxiv.org/abs/2202.13977
 PDF source

=== Source paper abstract / header ===
Abstract:A pure pair in a tournament $G$ is an ordered pair $(A,B)$ of disjoint subsets of $V(G)$ such that every vertex in $B$ is adjacent from every vertex in $A$. Which tournaments $H$ have the property that if $G$ is a tournament not containing $H$ as a subtournament, and $|G|>1$, there is a pure pair $(A,B)$ in $G$ with $|A|,|B|\ge c|G|$, where $c>0$ is a constant independent of $G$? Let us say that such a tournament $H$ has the strong EH-property.
As far as we know, it might be that a tournament $H$ has this property if and only if its vertex set has a linear ordering in which its backedges form a forest. Certainly this condition is necessary, but we are far from proving sufficiency. We make a small step in this direction, showing that if a tournament can be ordered with at most three backedges then it has the strong EH-property (except for one case, that we could not decide). In particular, every tournament with at most six vertices has the property, except for three that we could not decide. We also give a seven-vertex tournament that does not have the strong EH-property.
This is related to the Erdos-Hajnal conjecture, which in one form says that for every tournament $H$ there exists $\tau>0$ such that every tournament $G$ not containing $H$ as a subtournament has a transitive subtournament of cardinality at least $|G|^\tau$. Let us say that a tournament $H$ satisfying this has the EH-property. It is known that every tournament with the strong EH-property also has the EH-property; so our result extends work by Berger, Choromanski and Chudnovsky, who proved that every tournament with at most six vertices has the EH-property, except for one that they did not decide.
 

 
 
 
 Comments:
 Accepted manuscript; see DOI for journal version
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2202.13977 [math.CO]
 

 
  
 (or 
 arXiv:2202.13977v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2202.13977
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 European Journal of Combinatorics, Volume 115, January 2024, 103786
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.ejc.2023.103786

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Sophie Spirkl [view email] 
 [v1]
 Mon, 28 Feb 2022 17:28:20 UTC (28 KB)

 [v2]
 Sun, 2 Oct 2022 15:04:43 UTC (29 KB)

 [v3]
 Tue, 8 Aug 2023 13:33:51 UTC (30 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Pure pairs. X. Tournaments and the strong Erdos-Hajnal property, by Maria Chudnovsky and 3 other authors
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
