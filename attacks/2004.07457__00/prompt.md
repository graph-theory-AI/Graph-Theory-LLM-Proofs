Attack the following open graph-theory problem.

Catalog id: 2004.07457__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.07457__00/
Source paper: Asymmetric list sizes in bipartite graphs (arXiv:2004.07457)

=== Catalog page (statement + literature review) ===
Optimal asymmetric list sizes in bipartite graphs — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 List chromatic number and maximum degree of bipartite graphs
 (fuzzy-match score 82).

 
 Status
 open
 high confidence
 

 Problem 3 asks for the optimal list-size pairs $(k_A, k_B)$ (with $k_A \leq \Delta_A$, $k_B \leq \Delta_B$) guaranteeing $(k_A,k_B)$-choosability for all bipartite graphs with one-sided maximum degrees $\Delta_A, \Delta_B$. The source paper itself establishes several sufficient conditions (e.g., $(1+\varepsilon)\Delta/\log_4\Delta, 2$- and $((1+\varepsilon)\Delta/\log\Delta, \log\Delta)$-choosability in the symmetric case), but the full characterisation of optimal pairs remains open. A 2024 paper (arXiv:2409.01513) improves the symmetric choosability bound to $(\frac{4}{5}-\varepsilon)\Delta/\log\Delta$ but addresses the symmetric setting only and does not cite or directly engage with Problem 3.

 Reviewer notes. No follow-up paper resolving Problem 3 found after searching. The problem is inherently open-ended (asks for a full characterisation of optimal pairs), making partial progress hard to pin down. The paper 2409.01513 improves the symmetric upper bound but does not address the asymmetric question. The Springer paper 'Coloring Bipartite Graphs with Semi-small List Size' (doi:10.1007/s00026-022-00633-z) appeared in search results and could be relevant but could not be verified due to a paywall redirect; it was not included.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Given $\Delta_A$ and $\Delta_B$, what are optimal choices of $k_A \leq \Delta_A$ and $k_B \leq \Delta_B$ for which any bipartite graph $G = (V = A \cup B, E)$ with parts $A$ and $B$ having maximum degrees at most $\Delta_A$ and $\Delta_B$, respectively, is $(k_A, k_B)$-choosable?

Context

The authors introduce $(k_A, k_B)$-choosability as an asymmetric generalisation of ordinary list colouring of bipartite graphs, where vertices in part $A$ receive lists of size $k_A$ and vertices in part $B$ receive lists of size $k_B$. Problem 3 asks for the optimal list-size pairs in terms of the one-sided maximum degrees $\Delta_A$ and $\Delta_B$, and subsumes Conjecture 2 as its symmetric special case.

Notes. PDF source — math notation verified readable.

Source paper

 Asymmetric list sizes in bipartite graphs
 Noga Alon, Stijn Cambie, Ross J. Kang · 2021-08-30
 https://arxiv.org/abs/2004.07457
 PDF source

=== Source paper abstract / header ===
Abstract:Given a bipartite graph with parts $A$ and $B$ having maximum degrees at most $\Delta_A$ and $\Delta_B$, respectively, consider a list assignment such that every vertex in $A$ or $B$ is given a list of colours of size $k_A$ or $k_B$, respectively.
We prove some general sufficient conditions in terms of $\Delta_A$, $\Delta_B$, $k_A$, $k_B$ to be guaranteed a proper colouring such that each vertex is coloured using only a colour from its list. These are asymptotically nearly sharp in the very asymmetric cases. We establish one sufficient condition in particular, where $\Delta_A=\Delta_B=\Delta$, $k_A=\log \Delta$ and $k_B=(1+o(1))\Delta/\log\Delta$ as $\Delta\to\infty$. This amounts to partial progress towards a conjecture from 1998 of Krivelevich and the first author.
We also derive some necessary conditions through an intriguing connection between the complete case and the extremal size of approximate Steiner systems. We show that for complete bipartite graphs these conditions are asymptotically nearly sharp in a large part of the parameter space. This has provoked the following.
In the setup above, we conjecture that a proper list colouring is always guaranteed
* if $k_A \ge \Delta_A^\varepsilon$ and $k_B \ge \Delta_B^\varepsilon$ for any $\varepsilon>0$ provided $\Delta_A$ and $\Delta_B$ are large enough;
* if $k_A \ge C \log\Delta_B$ and $k_B \ge C \log\Delta_A$ for some absolute constant $C>1$; or
* if $\Delta_A=\Delta_B = \Delta$ and $ k_B \ge C (\Delta/\log\Delta)^{1/k_A}\log \Delta$ for some absolute constant $C>0$.
These are asymmetric generalisations of the above-mentioned conjecture of Krivelevich and the first author, and if true are close to best possible. Our general sufficient conditions provide partial progress towards these conjectures.
 

 
 
 
 Comments:
 20 pages; minor corrections in v2, to appear in Annals of Combinatorics
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15, 05C35, 05D05
 

 Cite as:
 arXiv:2004.07457 [math.CO]
 

 
  
 (or 
 arXiv:2004.07457v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2004.07457
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Ann. Comb. 25, 913-933 (2021)
 

 
 
 Related DOI:
 
 https://doi.org/10.1007/s00026-021-00552-5

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Ross J. Kang [view email] 
 [v1]
 Thu, 16 Apr 2020 04:52:04 UTC (26 KB)

 [v2]
 Mon, 30 Aug 2021 18:42:33 UTC (27 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Asymmetric list sizes in bipartite graphs, by Noga Alon and 2 other authors
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
 | 2020-04
 

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
