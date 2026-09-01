Attack the following open graph-theory problem.

Catalog id: 1905.12142__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1905.12142__00/
Source paper: Combinatorial anti-concentration inequalities, with applications (arXiv:1905.12142)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.12
Fix $p \in (0,1)$ and fix a graph $H$ with $h$ non-isolated vertices. Let $G \in G(n,p)$. Then for any $x \in \mathbb{N}$, $$\Pr(X_H = x) = O\!\left(1/\sqrt{\mathrm{Var}(X_H)}\right) = O\!\left(1/n^{h-1}\right).$$

Context:
The authors establish via Corollary 1.11 that $\Pr(X_H = x) = O(1/\sqrt{r})$ where $r$ is the number of edge-disjoint copies of $H$ in $G$, giving $O(1/n)$ in $G(n,p)$, but believe this is far from optimal. The conjectured bound matches the Gaussian scale and is best-possible given the known CLT for $X_H$. Theorem 1.14 confirms the conjecture for cliques $H = K_h$.

=== Catalog page (statement + literature review) ===
Local concentration of subgraph counts in G(n,p) — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 1.12 (that Pr(X_H = x) = O(1/sqrt(Var(X_H))) = O(1/n^{h-1}) for any fixed graph H with h non-isolated vertices in G(n,p)) has been resolved affirmatively for connected graphs H by Sah and Sawhney (arXiv:2006.11369, JLMS 2022), who established a local CLT for connected subgraph counts achieving the optimal scale. However, the same paper provides a counterexample showing the bound fails for certain disconnected graphs H, so the conjecture as stated for all graphs with non-isolated vertices is disproved. A companion paper (arXiv:1905.12749, Ann. Prob. 2021) by the same authors proved the near-optimal bound O(n^{1-h+o(1)}) for connected H, confirming the conjecture up to a subpolynomial factor.

 Cited literature (2)

 
 
 
partial Anti-concentration for subgraph counts in random graphs
 (2021)
 

 
 Jacob Fox, Matthew Kwan, Lisa Sauermann · Annals of Probability · arXiv:1905.12749 · doi:10.1214/20-AOP1490

Proves that for connected H with h vertices, Pr(X_H = x) <= n^{1-h+o(1)}, giving a near-optimal (but not tight) bound falling just short of the conjectured O(1/n^{h-1}); this is a companion paper submitted to arXiv concurrently in May 2019.
 

 
 
partial Local limit theorems for subgraph counts
 (2022)
 

 
 Ashwin Sah, Mehtaab Sawhney · Journal of the London Mathematical Society · arXiv:2006.11369 · doi:10.1112/jlms.12523

Proves a local CLT for connected subgraph counts in G(n,p) (establishing the optimal O(1/n^{h-1}) bound of Conjecture 1.12 for connected H), while also providing a counterexample showing the conjectured bound fails for certain disconnected graphs, resolving the conjecture negatively in full generality.
 

 

 Reviewer notes. Conjecture 1.12 is proved for connected H (full optimal bound O(1/n^{h-1}) via local CLT, Sah-Sawhney 2022) and disproved for disconnected H with no isolated vertices. The companion paper 1905.12749 achieves a near-optimal bound n^{1-h+o(1)} for connected H. The paper itself (Theorem 1.14) confirms the conjecture for cliques. Status 'partial' reflects that the positive case (connected H) is fully resolved at the optimal scale.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Fix $p \in (0,1)$ and fix a graph $H$ with $h$ non-isolated vertices. Let $G \in G(n,p)$. Then for any $x \in \mathbb{N}$, $$\Pr(X_H = x) = O\!\left(1/\sqrt{\mathrm{Var}(X_H)}\right) = O\!\left(1/n^{h-1}\right).$$

Context

The authors establish via Corollary 1.11 that $\Pr(X_H = x) = O(1/\sqrt{r})$ where $r$ is the number of edge-disjoint copies of $H$ in $G$, giving $O(1/n)$ in $G(n,p)$, but believe this is far from optimal. The conjectured bound matches the Gaussian scale and is best-possible given the known CLT for $X_H$. Theorem 1.14 confirms the conjecture for cliques $H = K_h$.

Source paper

 Combinatorial anti-concentration inequalities, with applications
 Jacob Fox, Matthew Kwan, Lisa Sauermann · 2020-11-18
 https://arxiv.org/abs/1905.12142
 PDF source

=== Source paper abstract / header ===
Abstract:We prove several different anti-concentration inequalities for functions of independent Bernoulli-distributed random variables. First, motivated by a conjecture of Alon, Hefetz, Krivelevich and Tyomkyn, we prove some "Poisson-type" anti-concentration theorems that give bounds of the form 1/e + o(1) for the point probabilities of certain polynomials. Second, we prove an anti-concentration inequality for polynomials with nonnegative coefficients which extends the classical Erdős-Littlewood-Offord theorem and improves a theorem of Meka, Nguyen and Vu for polynomials of this type. As an application, we prove some new anti-concentration bounds for subgraph counts in random graphs.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1905.12142 [math.CO]
 

 
  
 (or 
 arXiv:1905.12142v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1905.12142
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Math. Proc. Camb. Phil. Soc. 171 (2021) 227-248
 

 
 
 Related DOI:
 
 https://doi.org/10.1017/S0305004120000183

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Matthew Kwan [view email] 
 [v1]
 Wed, 29 May 2019 00:22:00 UTC (25 KB)

 [v2]
 Mon, 28 Oct 2019 02:11:54 UTC (25 KB)

 [v3]
 Wed, 18 Nov 2020 01:03:04 UTC (26 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Combinatorial anti-concentration inequalities, with applications, by Jacob Fox and 2 other authors
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
 | 2019-05
 

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
