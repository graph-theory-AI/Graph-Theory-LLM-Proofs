Attack the following open graph-theory problem.

Catalog id: 1610.00876__00
Catalog status: open (triage tier 5, lean prove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1610.00876__00/
Source paper: Subdivisions in digraphs of large out-degree or large dichromatic number (arXiv:1610.00876)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 3
There exists a least integer $\mathrm{mader}_{\delta^0}(TT_k)$ such that every digraph $D$ with $\delta^0(D) \geq \mathrm{mader}_{\delta^0}(TT_k)$ contains a subdivision of $TT_k$.

Context:
The paper shows Conjecture 3 is equivalent to Mader's Conjecture 2: if transitive tournaments are $\delta^0$-maderian, then $\mathrm{mader}_{\delta^+}(TT_k) \leq \mathrm{mader}_{\delta^0}(TT_{2k})$ for all $k$. It is stated separately to make this equivalence explicit.

=== Catalog page (statement + literature review) ===
TT_k Subdivision via Minimum Semidegree — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 Subdivision of a transitive tournament in digraphs with large outdegree.
 (fuzzy-match score 74).

 
 Status
 open
 high confidence
 

 Conjecture 3 from arXiv:1610.00876 — that a least integer $\mathrm{mader}_{\delta^0}(TT_k)$ exists forcing a $TT_k$ subdivision in every digraph of minimum semi-degree at least that threshold — remains open. It is shown in the source paper to be equivalent to Mader's 1985 conjecture (Conjecture 2) on minimum out-degree; the full conjecture is unresolved even for $k=5$. Related papers in the curated corpus (arXiv:2008.13224, arXiv:2008.09888) make progress on other conjectures from the same paper (oriented-cycle subdivisions and dichromatic-number thresholds, respectively) but do not settle the $TT_k$ semi-degree question.

 Reviewer notes. Mader's conjecture on TT_k subdivision with large out-degree (equivalently, large minimum semi-degree via Conjecture 3) remains a major open problem as of May 2026; even the existence of the threshold for TT_5 is unknown. Related positive results exist for immersions of transitive tournaments (Lochet, arXiv:1710.11482) and for 1-subdivisions, but the full vertex-disjoint subdivision conjecture is unresolved. The contradictory corpus contributions for arXiv:2008.13224 arise because different extracted snippets describe different conjectures from the source paper.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There exists a least integer $\mathrm{mader}_{\delta^0}(TT_k)$ such that every digraph $D$ with $\delta^0(D) \geq \mathrm{mader}_{\delta^0}(TT_k)$ contains a subdivision of $TT_k$.

Context

The paper shows Conjecture 3 is equivalent to Mader's Conjecture 2: if transitive tournaments are $\delta^0$-maderian, then $\mathrm{mader}_{\delta^+}(TT_k) \leq \mathrm{mader}_{\delta^0}(TT_{2k})$ for all $k$. It is stated separately to make this equivalence explicit.

Notes. PDF source.

Source paper

 Subdivisions in digraphs of large out-degree or large dichromatic number
 Pierre Aboulker, Nathann Cohen, Fréderic Havet, William Lochet, Phablo F. S. Moura, Stéphan Thomassé · 2016-10-04
 https://arxiv.org/abs/1610.00876
 PDF source

Related conjectures

 
 equivalent to
 Subdivision of a transitive tournament in digraphs with large outdegree.
 partial
 One direction is hypothesis-class containment: delta^0(D)=min(delta^+,delta^-)>=f forces delta^+(D)>=f, so any digraph satisfying the semidegree hypothesis satisfies the outdegree hypothesis, hence Mader's outdegree conjecture implies the semidegree version. The converse is proved in the source paper: it shows that if transitive tournaments are delta^0-maderian then mader_{delta^+}(TT_k) <= mader_{delta^0}(TT_{2k}) for all k, and the provided context explicitly states 'Conjecture 3 is equivalent to Mader's Conjecture 2', which is the OPG statement. Equivalence is thus both partly self-contained and explicitly asserted in the source text.
 

 
 implied by
 Subdivision of a transitive tournament in digraphs with large outdegree.
 partial
 Hypothesis-class containment: delta^0(D) = min(min-outdegree, min-indegree), so any digraph with delta^0(D) >= f(k) in particular has minimum outdegree >= f(k). If Mader's outdegree conjecture holds with f(k), every such digraph contains a TT_k subdivision, so mader_{delta^0}(TT_k) exists and is <= f(k). The semidegree hypothesis is the stronger assumption, making the outdegree conjecture the stronger statement; direction as claimed. The target's own context notes the paper proves the two are in fact equivalent (via mader_{delta^+}(TT_k) <= mader_{delta^0}(TT_{2k})), but the claimed one-way implication is immediate from the statements alone.
 

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
