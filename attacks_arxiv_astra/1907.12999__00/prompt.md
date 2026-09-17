Attack the following open graph-theory problem.

Catalog id: 1907.12999__00
Catalog status: open (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1907.12999__00/
Source paper: Independence number in triangle-free graphs avoiding a minor (arXiv:1907.12999)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1
For every positive integer $t$, if an $n$-vertex graph $G$ does not contain $K_{t+1}$ as a minor then $\alpha(G) \geq n/t$.

Context:
This conjecture is a natural weakening of Hadwiger's conjecture: since Hadwiger's conjecture would imply every $n$-vertex $K_{t+1}$-minor-free graph has chromatic number at most $t$ and thus an independent set of size at least $n/t$, this bound has attracted considerable attention (see Seymour's survey [31]). Duchet and Meyniel proved the bound holds within a factor of 2 in 1982, and subsequent improvements have been made by Fox, Balogh–Kostochka, and others. The present paper studies this conjecture restricted to triangle-free graphs.

=== Catalog page (statement + literature review) ===
Independence number lower bound in K_{t+1}-minor-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The conjecture that every n-vertex K_{t+1}-minor-free graph has independence number at least n/t remains open. The source paper itself proves a weaker result restricted to triangle-free graphs (independence number at least n/t^{1-ε} for all sufficiently large t), while the best known general bound without the triangle-free restriction is the Duchet–Meyniel bound α(G) ≥ n/(2t−1) from 1982. Recent breakthroughs on Hadwiger-type coloring (Norin–Postle–Song, Delcourt–Postle giving O(t log log t)-colorability) do not suffice to resolve this independence number conjecture, and no paper proving or disproving the full statement was found.

 Reviewer notes. The conjecture is a well-known weakening of Hadwiger's conjecture: Hadwiger would imply chromatic number ≤ t for K_{t+1}-minor-free graphs and thus α(G) ≥ n/t, but the conjecture may be provable independently. The best unconditional general bound remains Duchet–Meyniel (α ≥ n/(2t−1)). A related paper arXiv:2002.11100 extends the Dvořák–Yepremyan triangle-free result to arbitrary H-free graphs (clique minors given independence number), but this is a different direction and does not resolve Conjecture 1. No follow-up paper resolving the full conjecture was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every positive integer $t$, if an $n$-vertex graph $G$ does not contain $K_{t+1}$ as a minor then $\alpha(G) \geq n/t$.

Context

This conjecture is a natural weakening of Hadwiger's conjecture: since Hadwiger's conjecture would imply every $n$-vertex $K_{t+1}$-minor-free graph has chromatic number at most $t$ and thus an independent set of size at least $n/t$, this bound has attracted considerable attention (see Seymour's survey [31]). Duchet and Meyniel proved the bound holds within a factor of 2 in 1982, and subsequent improvements have been made by Fox, Balogh–Kostochka, and others. The present paper studies this conjecture restricted to triangle-free graphs.

Notes. No explicit attribution appears in the conjecture header; the paper describes it as having 'received quite a lot of attention' and directs the reader to Seymour's survey [31], indicating it is a community/folklore conjecture rather than one originated by the paper authors. Classified as 'states' per the no-attribution-in-header rule.

Source paper

 Independence number in triangle-free graphs avoiding a minor
 Zdeněk Dvořák, Liana Yepremyan · 2019-07-30
 https://arxiv.org/abs/1907.12999
 PDF source

Related conjectures

 
 implied by
 Fractional Hadwiger
 open
 If G is K_{t+1}-minor-free then its Hadwiger number satisfies had(G) ≤ t. Part (a) of the Fractional Hadwiger conjecture gives χ_f(G) ≤ had(G) ≤ t. The standard inequality χ_f(G) ≥ n/α(G) (every fractional coloring covers each vertex by independent sets of size ≤ α, LP duality) then gives α(G) ≥ n/χ_f(G) ≥ n/t, which is exactly the target. Only part (a) of the source is needed, and the source conjecture asserts (a), (b), (c) jointly, so truth of the source forces the target. The target's own context confirms this is a weakening along exactly this chain (via Hadwiger). Direction correct.
 

 
 implies
 Seagull problem
 partial
 Let G be an n-vertex graph with alpha(G) <= 2 and let h = had(G) be the largest k with a K_k minor. Then G has no K_{h+1} minor, so the source conjecture with t = h gives alpha(G) >= n/h, hence 2 >= n/h and h >= n/2; as h is an integer, G has a K_{ceil(n/2)} minor, which is exactly the Seagull statement. Equivalently, Seagull is the alpha = 2 special case of the conjecture that K_{t+1}-minor-free graphs satisfy alpha >= n/t (both are standard weakenings of Hadwiger's conjecture via chi >= n/alpha resp. chi >= n/2). Parameters are monotone and the specialization is exact; direction as claimed, and all three finder sketches agree with this derivation.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:The celebrated Hadwiger's conjecture states that if a graph contains no $K_{t+1}$ minor then it is $t$-colourable. If true, it would in particular imply that every $n$-vertex $K_{t+1}$-minor-free graph has an independent set of size at least $n/t$. In 1982, Duchet and Meyniel proved that this bound holds within a factor $2$. Their bound has been improved; most notably in an absolute factor by Fox, which was later improved by Balogh and Kostochka. Here we consider the same question for triangle-free graphs. By the results of Shearer and Kostochka and Thomason, it follows that any triangle-free graph with no $K_t$ minor has an independent set of size $\Omega(\tfrac{\sqrt{\log{t}}}{t}n)$. We show that a much larger independent set exists; for all sufficiently large $t$ every triangle-free graph on $n$ vertices with no $K_t$-minor has an independent set of size $ \tfrac{n}{t^{1-\varepsilon}}$. This answers a question of Sergey Norin.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1907.12999 [math.CO]
 

 
  
 (or 
 arXiv:1907.12999v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1907.12999
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Liana Yepremyan [view email] 
 [v1]
 Tue, 30 Jul 2019 15:06:41 UTC (13 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Independence number in triangle-free graphs avoiding a minor, by Zden\v{e}k Dvo\v{r}\'ak and Liana Yepremyan
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
 | 2019-07
 

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
