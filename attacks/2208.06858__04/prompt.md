Attack the following open graph-theory problem.

Catalog id: 2208.06858__04
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2208.06858__04/
Source paper: The success probability in Levine's hat problem, and independent sets i… (arXiv:2208.06858)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 2.9
$\varepsilon^{**}(\alpha) > 0$ for all $\alpha \in (0, 1/2)$. In other words, there exists a monotone non-decreasing function $\varepsilon^{**} : (0,1/2) \to (0,1/2)$ such that the following holds: if $G$ is a graph on $n$ vertices with maximum independent set of size $\alpha n$, $W$ is a binomial random subset of $V(G)$, and $I_W$ is the maximal independent set contained in $W$, then $$\alpha^{**}(G) = E_W\!\left[|I_W|/n\right] \leq \alpha - \varepsilon^{**}(\alpha).$$

Context:
This is the special case of Conjecture 2.8 where the random-subset distribution is simply binomial (each vertex included independently with probability $1/2$), which the authors describe as 'a fundamental problem in the study of independent sets in graphs'. The paper proves this for $\alpha > 1/4$ (Theorem 2.10) and for regular graphs with $\alpha > 1/8$ (Theorem 2.11).

=== Catalog page (statement + literature review) ===
Binomial sampling gap for independence ratio — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Conjecture 2.9 asserts that for every graph $G$ on $n$ vertices with independence number $\alpha n$ ($\alpha < 1/2$), the expected size of the maximal independent set in a binomial random half-subset satisfies $\alpha^{**}(G) \leq \alpha - \varepsilon^{**}(\alpha)$ for some positive $\varepsilon^{**}(\alpha)$ depending only on $\alpha$. The source paper itself establishes the conjecture for $\alpha > 1/4$ (Theorem 2.10) and for regular graphs when $\alpha > 1/8$ (Theorem 2.11), leaving the full range $(0, 1/4]$ for general graphs open. Semantic Scholar lists five citing papers (to May 2026), none of which could be verified to make further progress on this specific conjecture; the closest follow-ups concern the hat-puzzle side of the paper or the related Bollobás–Erdős–Tuza conjecture.

 Reviewer notes. Semantic Scholar returns five citing papers (arXiv:2503.09042, arXiv:2405.18264, arXiv:2404.01639, arXiv:2405.18264 duplicate, and one without an arXiv ID); WebFetch of 2503.09042 ('A Fourier approach to Levine's hat puzzle', Heilman–Tamuz 2025) confirmed it addresses the two-player hat puzzle via Boolean harmonic analysis, not Conjecture 2.9 on independent sets; WebFetch of 2405.18264 (Cheng–Xu 2024) confirmed it concerns the Bollobás–Erdős–Tuza conjecture for $K_{s,t}$-free graphs and does not address Conjecture 2.9 directly. No paper found that resolves the conjecture for $\alpha \in (0, 1/4]$ on general graphs.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. $\varepsilon^{**}(\alpha) > 0$ for all $\alpha \in (0, 1/2)$. In other words, there exists a monotone non-decreasing function $\varepsilon^{**} : (0,1/2) \to (0,1/2)$ such that the following holds: if $G$ is a graph on $n$ vertices with maximum independent set of size $\alpha n$, $W$ is a binomial random subset of $V(G)$, and $I_W$ is the maximal independent set contained in $W$, then $$\alpha^{**}(G) = E_W\!\left[|I_W|/n\right] \leq \alpha - \varepsilon^{**}(\alpha).$$

Context

This is the special case of Conjecture 2.8 where the random-subset distribution is simply binomial (each vertex included independently with probability $1/2$), which the authors describe as 'a fundamental problem in the study of independent sets in graphs'. The paper proves this for $\alpha > 1/4$ (Theorem 2.10) and for regular graphs with $\alpha > 1/8$ (Theorem 2.11).

Source paper

 The success probability in Levine's hat problem, and independent sets in graphs
 Noga Alon, Ehud Friedgut, Gil Kalai, Guy Kindler · 2023-08-21
 https://arxiv.org/abs/2208.06858
 PDF source

=== Source paper abstract / header ===
Abstract:Lionel Levine's hat challenge has $t$ players, each with a (very large, or infinite) stack of hats on their head, each hat independently colored at random black or white. The players are allowed to coordinate before the random colors are chosen, but not after. Each player sees all hats except for those on her own head. They then proceed to simultaneously try and each pick a black hat from their respective stacks. They are proclaimed successful only if they are all correct. Levine's conjecture is that the success probability tends to zero when the number of players grows. We prove that this success probability is strictly decreasing in the number of players, and present some connections to problems in graph theory: relating the size of the largest independent set in a graph and in a random induced subgraph of it, and bounding the size of a set of vertices intersecting every maximum-size independent set in a graph.
 

 
 
 
 Comments:
 arXiv admin note: substantial text overlap with arXiv:2103.01541, arXiv:2103.05998
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2208.06858 [math.CO]
 

 
  
 (or 
 arXiv:2208.06858v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2208.06858
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Ehud Friedgut [view email] 
 [v1]
 Sun, 14 Aug 2022 14:17:03 UTC (17 KB)

 [v2]
 Mon, 21 Aug 2023 06:50:23 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled The success probability in Levine's hat problem, and independent sets in graphs, by Noga Alon and 3 other authors
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
 | 2022-08
 

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
