Attack the following open graph-theory problem.

Catalog id: 1909.08426__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1909.08426__01/
Source paper: When Maximum Stable Set can be solved in FPT time (arXiv:1909.08426)

=== Extracted statement (catalog JSON) ===
Title: Parameterized MIS Dichotomy
Is MIS (randomized) FPT or $W[1]$-hard in $H$-free graphs?

Context:
This is the parameterized counterpart of the classical MIS dichotomy question. Alekseev's NP-hardness reduction does not transfer to $W[1]$-hardness, leaving a priori more candidate graphs $H$ for which the parameterized status is open. Dabrowski et al. initiated a systematic study of this question.

=== Catalog page (statement + literature review) ===
MIS parameterized complexity in H-free graphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The full FPT vs W[1]-hard dichotomy for MIS in H-free graphs remains open as of 2026. Significant partial progress has been made: the dichotomy is completely resolved for all 4-vertex forbidden subgraphs, and many 5-vertex cases are settled, but cases such as P7-free, S_{1,1,3}-free, and S_{1,2,2}-free graphs remain open. A 2020 follow-up by Dvořák et al. strengthened hardness results by proving parameterized inapproximability lower bounds under ETH/Gap-ETH for graph classes where W[1]-hardness was already known, without resolving new FPT cases.

 Cited literature (1)

 
 
 
partial Parameterized Inapproximability of Independent Set in H-Free Graphs
 (2020)
 

 
 Pavel Dvořák, Andreas Emil Feldmann, Ashutosh Rai, Paweł Rzążewski · Algorithmica · arXiv:2006.10444 · doi:10.1007/s00453-022-01052-5

Under ETH and Gap-ETH, strengthens existing W[1]-hardness results for MIS in H-free graphs to parameterized inapproximability lower bounds, and extends inapproximability to K_{a,b}-free graphs, but does not settle new FPT cases or the full dichotomy.
 

 

 Reviewer notes. The precursor paper arXiv:1810.04620 (Bonnet, Bousquet, Charbit, Thomassé, Watrigant, 2018) initiated the systematic classification and predates the source paper; it is not listed in since_posted. The source paper itself (1909.08426) establishes additional FPT cases (disjoint unions of cliques, P(1,t,t,t)-free, dart-free, cricket-free). No paper found resolving the full dichotomy for all H as of the search date.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Is MIS (randomized) FPT or $W[1]$-hard in $H$-free graphs?

Context

This is the parameterized counterpart of the classical MIS dichotomy question. Alekseev's NP-hardness reduction does not transfer to $W[1]$-hardness, leaving a priori more candidate graphs $H$ for which the parameterized status is open. Dabrowski et al. initiated a systematic study of this question.

Notes. PDF source. Formally labelled with a bullet marker in the paper alongside the conjectures.

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
