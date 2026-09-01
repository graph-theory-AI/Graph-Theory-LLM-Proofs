Attack the following open graph-theory problem.

Catalog id: 2004.12166__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.12166__00/
Source paper: An algorithmic weakening of the Erdős-Hajnal conjecture (arXiv:2004.12166)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 5 (Improved Approximation Conjecture)
Every graph $H$ satisfies the improved approximation property, i.e., there exists a constant $\varepsilon > 0$ such that MIS admits a (randomized) $n^{1-\varepsilon}$-approximation polynomial algorithm on every $H$-free $n$-vertex graph $G$.

Context:
This conjecture is introduced as an algorithmic weakening of the Erdős-Hajnal conjecture. It states informally that the inapproximability of MIS in general graphs can always be beaten in any proper hereditary class. It is strictly weaker than the Erdős-Hajnal conjecture, since MIS is polynomial in $P_6$-free graphs while it is open whether $P_5$ satisfies the Erdős-Hajnal property.

=== Catalog page (statement + literature review) ===
MIS sub-polynomial approximation in H-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No follow-up paper resolving or disproving Conjecture 5 from arXiv:2004.12166 was found after targeted searches. The conjecture remains open: it is known to hold for all H whose H-free class admits a polynomial-time MIS algorithm (e.g., P_6-free, fork-free graphs) by closure under graph substitution, but the full statement for every graph H is unresolved. The internal candidate reference arXiv:2301.10147 addresses the classical Erdős-Hajnal conjecture (clique/stable-set size bounds) and does not bear on the algorithmic/approximation formulation.

 Reviewer notes. Searches returned only the source paper (ESA 2020), closely related prior work on quasi-PTAS for MIS in H-free graphs (Chudnovsky et al. 2020), and a parameterized inapproximability paper in H-free graphs (Algorithmica 2022) whose content could not be verified due to a paywall redirect. Confidence is medium rather than high because the conjecture is ~6 years old, making absence of indexed progress mildly suspicious, though no counterexample or proof was found.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Every graph $H$ satisfies the improved approximation property, i.e., there exists a constant $\varepsilon > 0$ such that MIS admits a (randomized) $n^{1-\varepsilon}$-approximation polynomial algorithm on every $H$-free $n$-vertex graph $G$.

Context

This conjecture is introduced as an algorithmic weakening of the Erdős-Hajnal conjecture. It states informally that the inapproximability of MIS in general graphs can always be beaten in any proper hereditary class. It is strictly weaker than the Erdős-Hajnal conjecture, since MIS is polynomial in $P_6$-free graphs while it is open whether $P_5$ satisfies the Erdős-Hajnal property.

Source paper

 An algorithmic weakening of the Erdős-Hajnal conjecture
 Édouard Bonnet, Stéphan Thomassé, Xuan Thang Tran, Rémi Watrigant · 2020-04-25
 https://arxiv.org/abs/2004.12166
 PDF source

=== Source paper abstract / header ===
Abstract:We study the approximability of the Maximum Independent Set (MIS) problem in $H$-free graphs (that is, graphs which do not admit $H$ as an induced subgraph). As one motivation we investigate the following conjecture: for every fixed graph $H$, there exists a constant $\delta > 0$ such that MIS can be $n^{1 - \delta}$-approximated in $H$-free graphs, where $n$ denotes the number of vertices of the input graph. We first prove that a constructive version of the celebrated Erdős-Hajnal conjecture implies ours. We then prove that the set of graphs $H$ satisfying our conjecture is closed under the so-called graph substitution. This, together with the known polynomial-time algorithms for MIS in $H$-free graphs (e.g. $P_6$-free and fork-free graphs), implies that our conjecture holds for many graphs $H$ for which the Erdős-Hajnal conjecture is still open. We then focus on improving the constant $\delta$ for some graph classes: we prove that the classical Local Search algorithm provides an $OPT^{1-\frac{1}{t}}$-approximation in $K_{t,t}$-free graphs (hence a $\sqrt{OPT}$-approximation in $C_4$-free graphs), and, while there is a simple $\sqrt{n}$-approximation in triangle-free graphs, it cannot be improved to $n^{\frac{1}{4}-\varepsilon}$ for any $\varepsilon > 0$ unless $NP \subseteq BPP$. More generally, we show that there is a constant $c$ such that MIS in graphs of girth $\gamma$ cannot be $n^{\frac{c}{\gamma}}$-approximated. Up to a constant factor in the exponent, this matches the ratio of a known approximation algorithm by Monien and Speckenmeyer, and by Murphy. To the best of our knowledge, this is the first strong (i.e., $\Omega(n^\delta)$ for some $\delta > 0$) inapproximability result for Maximum Independent Set in a proper hereditary class.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Computational Complexity (cs.CC); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 68Q25, 68Q17, 68R10
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2004.12166 [cs.DS]
 

 
  
 (or 
 arXiv:2004.12166v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2004.12166
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Sat, 25 Apr 2020 15:11:59 UTC (33 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled An algorithmic weakening of the Erd\H{o}s-Hajnal conjecture, by \'Edouard Bonnet and 3 other authors
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
 | 2020-04
 

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
