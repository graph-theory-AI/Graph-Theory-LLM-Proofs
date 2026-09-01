Attack the following open graph-theory problem.

Catalog id: 2201.08204__01
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2201.08204__01/
Source paper: A counterexample to a conjecture about triangle-free induced subgraphs … (arXiv:2201.08204)

=== Extracted statement (catalog JSON) ===
Title: Question 3.2
Is there a function $f : \mathbb{N} \to \mathbb{N}$ such that for every digraph $D$ with no induced directed cycle of odd length, we have $\vec{\chi}(D) \leq f(\omega(D))$?

Context:
Motivated by Theorem 1.5, which shows that the digraph analogue of the Scott–Seymour theorem on odd holes fails, the authors ask whether banning all odd-length induced directed cycles forces the dichromatic number to be bounded by a function of the clique number.

=== Catalog page (statement + literature review) ===
χ-boundedness for odd-cycle-free digraphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No paper has been found that resolves Question 3.2 either positively or negatively. The closely related questions about t-chordal digraphs (all induced directed cycles of the same length t) have been answered negatively — for each t ≥ 3 there exist t-chordal digraphs with clique number at most 3 and arbitrarily large dichromatic number (arXiv:2203.15575, arXiv:2202.01006) — but these results concern digraphs where induced cycles are restricted to a fixed length, not digraphs where all odd-length induced directed cycles are absent. The distinction is material: banning every odd-length induced directed cycle is a much stronger condition, and the question of whether it forces χ⃗(D) ≤ f(ω(D)) remains open to the best of available search results.

 Cited literature (2)

 
 
 
partial Digraphs with all induced directed cycles of the same length are not $\vec{\chi}$-bounded
 (2022)
 

 
 Carbonero, Hompe, Moore, Spirkl · The Electronic Journal of Combinatorics, v29i4p4 · arXiv:2203.15575

For each t ≥ 3, there exist t-chordal digraphs (all induced directed cycles have length t) with clique number at most 3 and arbitrarily large dichromatic number, showing that t-chordal digraph classes are not χ⃗-bounded; this is a related but distinct condition from the one in Question 3.2.
 

 
 
partial Chordal directed graphs are not $\vec{\chi}$-bounded
 (2022)
 

 
 Aboulker, Bousquet, de Verclos · The Electronic Journal of Combinatorics, v29i2p17 · arXiv:2202.01006

Digraphs with no transitive tournament on 3 vertices in which every induced directed cycle has length 3 can have arbitrarily large dichromatic number, negatively answering a related question from the same source paper but not Question 3.2 directly.
 

 

 Reviewer notes. The construction in arXiv:2201.08204 itself is a digraph with bounded clique number, large dichromatic number, and no induced directed cycles of odd length at least 5 (i.e., it avoids odd cycles of length ≥ 5, but may have odd cycles of length 3). Question 3.2 asks whether banning ALL odd-length induced directed cycles (including length 3) suffices to bound the dichromatic number. No resolution of this stronger question was found in the indexed literature within the cap of 5 web calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Is there a function $f : \mathbb{N} \to \mathbb{N}$ such that for every digraph $D$ with no induced directed cycle of odd length, we have $\vec{\chi}(D) \leq f(\omega(D))$?

Context

Motivated by Theorem 1.5, which shows that the digraph analogue of the Scott–Seymour theorem on odd holes fails, the authors ask whether banning all odd-length induced directed cycles forces the dichromatic number to be bounded by a function of the clique number.

Notes. The paper states that Questions 3.2 and 3.4 were subsequently answered in the negative by the same authors in arXiv:2203.15575.

Source paper

 A counterexample to a conjecture about triangle-free induced subgraphs of graphs with large chromatic number
 Alvaro Carbonero, Patrick Hompe, Benjamin Moore, Sophie Spirkl · 2022-09-15
 https://arxiv.org/abs/2201.08204
 PDF source

=== Source paper abstract / header ===
Abstract:We prove that for every $n$, there is a graph $G$ with $\chi(G) \geq n$ and $\omega(G) \leq 3$ such that every induced subgraph $H$ of $G$ with $\omega(H) \leq 2$ satisfies $\chi(H) \leq 4$.
This disproves a well-known conjecture. Our construction is a digraph with bounded clique number, large dichromatic number, and no induced directed cycles of odd length at least 5.
 

 
 
 
 Comments:
 Accepted manuscript, see DOI for journal version
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2201.08204 [math.CO]
 

 
  
 (or 
 arXiv:2201.08204v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2201.08204
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Journal of Combinatorial Theory, Series B, Volume 158, Part 2, 2023, Pages 63-69
 

 
 
 Related DOI:
 
 https://doi.org/10.1016/j.jctb.2022.09.001

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Sophie Spirkl [view email] 
 [v1]
 Thu, 20 Jan 2022 14:35:42 UTC (6 KB)

 [v2]
 Wed, 9 Feb 2022 17:54:19 UTC (8 KB)

 [v3]
 Tue, 29 Mar 2022 13:54:11 UTC (7 KB)

 [v4]
 Thu, 15 Sep 2022 14:17:40 UTC (7 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A counterexample to a conjecture about triangle-free induced subgraphs of graphs with large chromatic number, by Alvaro Carbonero and 3 other authors
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
 | 2022-01
 

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
