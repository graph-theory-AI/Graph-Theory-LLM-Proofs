Attack the following open graph-theory problem.

Catalog id: 1811.08750__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1811.08750__00/
Source paper: Additive Approximation of Generalized Turán Questions (arXiv:1811.08750)

=== Catalog page (statement + literature review) ===
NP-hardness of generalized Turán approximation — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 1.8 from arXiv:1811.08750 posits that whenever no member of the forbidden family F is a subgraph of a blow-up of T, it is NP-hard to approximate ex(G,T,F) within additive error n^{v(T)-epsilon}. The paper proves the special case T=K_m, F={K_k} with k >= m+2 (Theorem 1.7), but the general conjecture remains open. The paper was published in Algorithmica in 2022, and a 2025 survey on generalized Turán problems (arXiv:2506.03418) exists, but no follow-up resolving the full conjecture was found in the indexed literature.

 Reviewer notes. The conjecture is from 2018 and no resolution was found after 5 web calls. The paper appeared in Algorithmica (2021, online; 2022 in print). A 2025 survey arXiv:2506.03418 covers generalized Turán counting problems but its full text was not accessible, so it may or may not discuss the conjecture's current status. Confidence is medium rather than high because the conjecture is 7+ years old, making absence of evidence somewhat less conclusive.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every graph $T$, family of graphs $\mathcal{F}$ such that no $F \in \mathcal{F}$ is a subgraph of a blow-up of $T$, and $\epsilon > 0$, it is NP-hard to approximate $\mathrm{ex}(G, T, \mathcal{F})$ up to additive error of $n^{v(T)-\epsilon}$ for a given input graph $G$ on $n$ vertices.

Context

The authors prove Theorem 1.7 as a special case (for $T = K_m$, $\mathcal{F} = \{K_k\}$ with $k \geq m+2$) and note that Proposition 1.5 covers the complementary easy regime (when some $F \in \mathcal{F}$ is a subgraph of a blow-up of $T$). They believe that excluding those easy cases no significantly better approximation than $\epsilon n^{v(T)}$ is achievable in polynomial time, leading to this conjecture. Section 6 of the paper contains further remarks on this conjecture and related open problems.

Source paper

 Additive Approximation of Generalized Turán Questions
 Noga Alon, Clara Shikhelman · 2018-11-21
 https://arxiv.org/abs/1811.08750
 PDF source

=== Source paper abstract / header ===
Abstract:For graphs $G$ and $T$, and a family of graphs $\mathcal{F}$ let $\mathrm{ex}(G,T,\mathcal{F})$ denote the maximum possible number of copies of $T$ in an $\mathcal{F}$-free subgraph of $G$. We investigate the algorithmic aspects of calculating and estimating this function. We show that for every graph $T$, finite family $\mathcal{F}$ and constant $\epsilon>0$ there is a polynomial time algorithm that approximates $\mathrm{ex}(G,T,\mathcal{F})$ for an input graph $G$ on $n$ vertices up to an additive error of $\epsilon n^{v(T)}$. We also consider the possibility of a better approximation, proving several positive and negative results, and suggesting a conjecture on the exact relation between $T$ and $\mathcal{F}$ for which no significantly better approximation can be found in polynomial time unless $P=NP$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1811.08750 [math.CO]
 

 
  
 (or 
 arXiv:1811.08750v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1811.08750
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Clara Shikhelman [view email] 
 [v1]
 Wed, 21 Nov 2018 14:28:44 UTC (23 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Additive Approximation of Generalized Tur\'an Questions, by Noga Alon and Clara Shikhelman
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
 | 2018-11
 

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
