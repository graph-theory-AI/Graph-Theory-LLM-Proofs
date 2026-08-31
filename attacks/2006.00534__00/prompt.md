Attack the following open graph-theory problem.

Catalog id: 2006.00534__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2006.00534__00/
Source paper: Inverse problems for minimal complements and maximal supplements (arXiv:2006.00534)

=== Catalog page (statement + literature review) ===
Minimal complement count T(n) square-root growth — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No verified follow-up resolving Conjecture 7 was found. At the time of the paper, the known bounds were T(n) \geq n^{1/3}/\mathrm{polylog} (Theorem 1) and T(n) = O(n^{3/4+\varepsilon}) (Theorem 3), with the conjecture proposing the true growth rate is \widetilde{\Theta}(\sqrt{n}). Web searches returned related papers on minimal additive complements published in 2023 and 2025, but none could be verified via WebFetch to specifically address this conjecture. The conjecture appears to remain open as of May 2026.

 Reviewer notes. Searches returned related papers including 'On minimal additive complements' (Ramanujan Journal, 2025, doi:10.1007/s11139-025-01281-6) and 'Sets arising as minimal additive complements in the integers' (Journal of Number Theory, 2023), but WebFetch of the Ramanujan Journal page was blocked by authentication redirect and thus these papers could not be verified to address Conjecture 7 on T(n). Noah Kravitz's arXiv author page shows no additional follow-up paper co-authored on this topic. The gap between the n^{1/3} lower bound and n^{3/4+\varepsilon} upper bound remains unresolved in the verified literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. We have that $T(n) = \widetilde{\Theta}(\sqrt{n})$. More generally, we have that $T(G) = \widetilde{\Theta}(\sqrt{|G|})$.

Context

The paper defines $\widetilde{\Theta}(g(n))$ to mean $f = \Omega(g(n)(\log n)^a)$ and $f(n) = O(g(n)(\log n)^b)$ for some integers $a,b$ (i.e., equality up to polylogarithmic factors). Theorem 1 gives a lower bound $T(n) \geq n^{1/3}/(2(\log n/\log 2)^{2/3})$ and Theorem 3 gives $T(n) = O(n^{3/4+\varepsilon})$; the conjecture proposes the true growth rate is $\widetilde{\Theta}(\sqrt{n})$.

Notes. PDF source — the tilde in $\widetilde{\Theta}$ is garbled in extraction (appears as bare 'e' or dropped); the argument of the second $\widetilde{\Theta}$ (presumably $\sqrt{|G|}$) is also lost in the PDF rendering. Statement reconstructed from context.

Source paper

 Inverse problems for minimal complements and maximal supplements
 Noga Alon, Noah Kravitz, Matt Larson · 2020-12-30
 https://arxiv.org/abs/2006.00534
 PDF source

=== Source paper abstract / header ===
Abstract:Given a subset $W$ of an abelian group $G$, a subset $C$ is called an additive complement for $W$ if $W+C=G$; if, moreover, no proper subset of $C$ has this property, then we say that $C$ is a minimal complement for $W$. It is natural to ask which subsets $C$ can arise as minimal complements for some $W$. We show that in a finite abelian group $G$, every non-empty subset $C$ of size $|C| \leq 2^{2/3}|G|^{1/3}/((3e \log |G|)^{2/3}$ is a minimal complement for some $W$. As a corollary, we deduce that every finite non-empty subset of an infinite abelian group is a minimal complement. We also derive several analogous results for ``dual'' problems about maximal supplements.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Number Theory (math.NT)
 

 Cite as:
 arXiv:2006.00534 [math.CO]
 

 
  
 (or 
 arXiv:2006.00534v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2006.00534
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Matt Larson [view email] 
 [v1]
 Sun, 31 May 2020 14:53:18 UTC (16 KB)

 [v2]
 Wed, 30 Dec 2020 03:17:56 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Inverse problems for minimal complements and maximal supplements, by Noga Alon and 2 other authors
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
 | 2020-06
 

 Change to browse by:
 
 math
 math.NT
 

 

 

 
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
