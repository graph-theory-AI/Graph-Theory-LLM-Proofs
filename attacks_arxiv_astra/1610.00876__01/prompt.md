Attack the following open graph-theory problem.

Catalog id: 1610.00876__01
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1610.00876__01/
Source paper: Subdivisions in digraphs of large out-degree or large dichromatic number (arXiv:1610.00876)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 4
Every oriented tree is $\delta^+$-maderian.

Context:
Oriented trees are known to be $\delta^0$-maderian with $\mathrm{mader}_{\delta^0}(T) = |T|-1$ via a greedy procedure, but whether they are $\delta^+$-maderian is open. This is posed as a natural weaker step towards Mader's Conjecture 2. The paper provides evidence by proving in-arborescences are $\delta^+$-maderian (Theorem 23) and all oriented paths are $\delta^+$-maderian (Corollary 20).

=== Catalog page (statement + literature review) ===
δ⁺-Maderian property for oriented trees — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 Subdivision of a transitive tournament in digraphs with large outdegree.
 (fuzzy-match score 74).

 
 Status
 open
 high confidence
 

 Conjecture 4 from arXiv:1610.00876, that every oriented tree is $\delta^+$-maderian, remains open as of 2026. The source paper itself established special cases: in-arborescences are $\delta^+$-maderian (Theorem 23) and all oriented paths are $\delta^+$-maderian (Corollary 20), but the general statement is unresolved. A 2024 survey (Stein, arXiv:2310.18719) explicitly notes that minimum-outdegree conditions for oriented trees and paths 'appear to be very difficult' and that related problems 'seem wide open', confirming no resolution has appeared. The most-cited follow-up papers in this area (arXiv:2008.13224 and arXiv:2008.09888, both 2020) resolve Conjecture 5 from the same source paper (oriented cycles), not Conjecture 4.

 Cited literature (1)

 
 
 
survey Oriented trees and paths in digraphs
 (2024)
 

 
 Maya Stein · arXiv preprint · arXiv:2310.18719

This survey of the area explicitly states that minimum-outdegree conditions for oriented paths and trees 'appear to be very difficult' and highlights the Thomassé-type conjectures as 'wide open', with the Aboulker et al. paper cited as related work, confirming Conjecture 4 remains unresolved.
 

 

 Reviewer notes. The internal reference corpus contains inconsistent entries for arXiv:2008.13224: some claim it proves Conjecture 4 in full generality while others say no direct progress is made; WebFetch confirms the paper is exclusively about oriented cycles (Conjecture 5). The 2024 survey arXiv:2310.18719 (Stein) treats minimum-outdegree conditions for trees as a wide-open research direction and explicitly calls related problems 'very difficult', providing strong corroboration that Conjecture 4 is open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Every oriented tree is $\delta^+$-maderian.

Context

Oriented trees are known to be $\delta^0$-maderian with $\mathrm{mader}_{\delta^0}(T) = |T|-1$ via a greedy procedure, but whether they are $\delta^+$-maderian is open. This is posed as a natural weaker step towards Mader's Conjecture 2. The paper provides evidence by proving in-arborescences are $\delta^+$-maderian (Theorem 23) and all oriented paths are $\delta^+$-maderian (Corollary 20).

Notes. PDF source.

Source paper

 Subdivisions in digraphs of large out-degree or large dichromatic number
 Pierre Aboulker, Nathann Cohen, Fréderic Havet, William Lochet, Phablo F. S. Moura, Stéphan Thomassé · 2016-10-04
 https://arxiv.org/abs/1610.00876
 PDF source

Related conjectures

 
 implied by
 Subdivision of a transitive tournament in digraphs with large outdegree.
 partial
 Every oriented tree T on k vertices is an acyclic digraph, so ordering its vertices along a topological order embeds T as a subdigraph of the transitive tournament TT_k (TT_k contains all forward arcs). A subdivision of TT_k contains a subdivision of every subdigraph H of TT_k: keep the branch vertices of H and the directed paths corresponding to H's arcs. Hence if min out-degree >= f(k) forces a TT_k-subdivision (source), it forces a subdivision of every oriented tree of order k, i.e., every oriented tree is delta+-maderian with mader_{delta+}(T) <= f(|T|) (target). Direction is correct: source is the stronger statement, and the target's context confirms it is 'posed as a natural weaker step towards Mader's Conjecture'.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

=== Source paper abstract / header ===
Abstract:In 1985, Mader conjectured the existence of a function $f$ such that every digraph with minimum out-degree at least $f(k)$ contains a subdivision of the transitive tournament of order $k$. This conjecture is still completely open, as the existence of $f(5)$ remains unknown. In this paper, we show that if $D$ is an oriented path, or an in-arborescence (i.e., a tree with all edges oriented towards the root) or the union of two directed paths from $x$ to $y$ and a directed path from $y$ to $x$, then every digraph with minimum out-degree large enough contains a subdivision of $D$. Additionally, we study Mader's conjecture considering another graph parameter. The dichromatic number of a digraph $D$ is the smallest integer $k$ such that $D$ can be partitioned into $k$ acyclic subdigraphs. We show that any digraph with dichromatic number greater than $4^m (n-1)$ contains every digraph with $n$ vertices and $m$ arcs as a subdivision.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1610.00876 [math.CO]
 

 
  
 (or 
 arXiv:1610.00876v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1610.00876
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: William Lochet [view email] 
 [v1]
 Tue, 4 Oct 2016 07:25:24 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Subdivisions in digraphs of large out-degree or large dichromatic number, by Pierre Aboulker and 4 other authors
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
 | 2016-10
 

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
