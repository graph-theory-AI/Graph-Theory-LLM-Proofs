Attack the following open graph-theory problem.

Catalog id: 1909.08426__04
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1909.08426__04/
Source paper: When Maximum Stable Set can be solved in FPT time (arXiv:1909.08426)

=== Extracted statement (catalog JSON) ===
Title: Informal belief on FPT candidates
There will be very few connected candidates $H$ (as described by the structural characterisation of FPT candidate graphs) which will not end up in (randomized) FPT.

Context:
After settling all four remaining five-vertex graph cases as (randomized) FPT, the authors express a broader belief that almost all graphs $H$ satisfying the structural conditions identified in Figure 1 will yield FPT algorithms for MIS in $H$-free graphs.

=== Catalog page (statement + literature review) ===
FPT candidates for H-free MIS nearly all tractable — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The informal belief that almost all connected graphs H satisfying the structural conditions of Figure 1 in arXiv:1909.08426 will yield (randomized) FPT algorithms for Maximum Independent Set in H-free graphs remains unresolved. Post-2019 searches confirm that the classical open cases—P7-free, S_{1,1,3}-free, and S_{1,2,2}-free graphs—still lack FPT algorithms, suggesting that at least some FPT candidates are genuinely difficult. Related work has expanded FPT/polynomial results to adjacent settings (e.g., induced-minor exclusion), but the core informal conjecture about induced-subgraph exclusion is not settled.

 Cited literature (1)

 
 
 
partial Maximum Independent Set when excluding an induced minor: K_1 + tK_2 and tC_3 ⊎ C_4
 (2023)
 

 
 Bonnet, Édouard; Duron, Julien; Geniet, Colin; Thomassé, Stéphan; Wesolek, Alexandra · ESA 2023 / Algorithmica 2025 · arXiv:2302.08182 · doi:10.4230/LIPIcs.ESA.2023.23

Extends MIS tractability to graphs excluding certain induced minors (K_1+tK_2 and tC_3⊎C_4), a related but distinct framework from induced-subgraph exclusion; does not directly resolve the open H-free cases from arXiv:1909.08426.
 

 

 Reviewer notes. The conjecture is deliberately informal ('there will be very few connected candidates ... which will not end up in (randomized) FPT'), making it hard to falsify definitively. Post-2019 literature confirms that P7-free, S_{1,1,3}-free, and S_{1,2,2}-free graphs remain major open cases within the FPT-candidate class, so the informal optimism has not been borne out for all candidates. No paper was found that explicitly claims to settle or refute this belief. The 2302.08182 paper (ESA 2023, Algorithmica 2025) by some of the same authors extends tractability results to excluded induced minors, but that is a separate framework.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. There will be very few connected candidates $H$ (as described by the structural characterisation of FPT candidate graphs) which will not end up in (randomized) FPT.

Context

After settling all four remaining five-vertex graph cases as (randomized) FPT, the authors express a broader belief that almost all graphs $H$ satisfying the structural conditions identified in Figure 1 will yield FPT algorithms for MIS in $H$-free graphs.

Notes. PDF source — informal belief stated in prose, not a formally labelled environment.

Source paper

 When Maximum Stable Set can be solved in FPT time
 Édouard Bonnet, Nicolas Bousquet, Stéphan Thomassé, Rémi Watrigant · 2019-09-18
 https://arxiv.org/abs/1909.08426
 PDF source

=== Source paper abstract / header ===
Abstract:Maximum Independent Set (MIS for short) is in general graphs the paradigmatic $W[1]$-hard problem. In stark contrast, polynomial-time algorithms are known when the inputs are restricted to structured graph classes such as, for instance, perfect graphs (which includes bipartite graphs, chordal graphs, co-graphs, etc.) or claw-free graphs. In this paper, we introduce some variants of co-graphs with parameterized noise, that is, graphs that can be made into disjoint unions or complete sums by the removal of a certain number of vertices and the addition/deletion of a certain number of edges per incident vertex, both controlled by the parameter. We give a series of FPT Turing-reductions on these classes and use them to make some progress on the parameterized complexity of MIS in $H$-free graphs. We show that for every fixed $t \geqslant 1$, MIS is FPT in $P(1,t,t,t)$-free graphs, where $P(1,t,t,t)$ is the graph obtained by substituting all the vertices of a four-vertex path but one end of the path by cliques of size $t$. We also provide randomized FPT algorithms in dart-free graphs and in cricket-free graphs. This settles the FPT/W[1]-hard dichotomy for five-vertex graphs $H$.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Computational Complexity (cs.CC); Discrete Mathematics (cs.DM)
 
 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:1909.08426 [cs.DS]
 

 
  
 (or 
 arXiv:1909.08426v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1909.08426
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Wed, 18 Sep 2019 13:04:39 UTC (115 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled When Maximum Stable Set can be solved in FPT time, by \'Edouard Bonnet and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2019-09
 

 Change to browse by:
 
 cs
 cs.CC
 cs.DM
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Édouard Bonnet
Nicolas Bousquet
Stéphan Thomassé
Rémi Watrigant 

 

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
