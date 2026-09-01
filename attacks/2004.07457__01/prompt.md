Attack the following open graph-theory problem.

Catalog id: 2004.07457__01
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.07457__01/
Source paper: Asymmetric list sizes in bipartite graphs (arXiv:2004.07457)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 7
Let the positive integers $\Delta_A, \Delta_B, k_A, k_B$ satisfy one of the following.
(i) Given $\varepsilon > 0$, we have $\Delta_A, \Delta_B \geq \Delta_0$ for some $\Delta_0 = \Delta_0(\varepsilon)$, and $k_A \geq \Delta_A^\varepsilon$ and $k_B \geq \Delta_B^\varepsilon$.
(ii) For some absolute constant $C > 1$, $k_A \geq C \log \Delta_B$ and $k_B \geq C \log \Delta_A$.
(iii) $\Delta_A = \Delta_B = \Delta$, and, for some absolute constant $C > 0$, $k_B \geq C(\Delta/\log\Delta)^{1/k_A} \log\Delta$ or $k_A \geq C(\Delta/\log\Delta)^{1/k_B} \log\Delta$.
Then any bipartite graph $G = (V = A \cup B, E)$ with parts $A$ and $B$ having maximum degrees at most $\Delta_A$ and $\Delta_B$, respectively, is $(k_A, k_B)$-choosable.

Context:
Motivated by the asymptotic behaviour of $(k_A, k_B)$-choosability for complete bipartite graphs (Theorem 6 and Theorem 16), the authors conjecture three concrete asymmetric analogues of the Krivelevich–Alon conjecture. Condition (i) is weaker than Conjecture 2; conditions (ii) and (iii) are stronger. The paper shows Conjecture 7 holds for complete bipartite graphs (Theorem 15) and provides partial progress in the general case via Theorem 4 and its corollaries.

=== Catalog page (statement + literature review) ===
Asymmetric Krivelevich–Alon choosability for bipartite graphs — Graph-theory open problems (arXiv)

 This appears to relate to an OPG problem:
 List chromatic number and maximum degree of bipartite graphs
 (fuzzy-match score 82).

 
 Status
 open
 medium confidence
 

 Conjecture 7 of Alon–Cambie–Kang posits (k_A,k_B)-choosability of bipartite graphs under three asymmetric degree/list-size regimes. Zhu (arXiv:2008.06040, Annals of Combinatorics 2022/2023) studied the problem in the semi-small list-size regime, strengthened bounds for k_A=2, and stated a unified framework conjecture on general bipartite graphs encompassing all three conditions; this constitutes partial progress but the full conjecture remains open. The improvement by Bradshaw–Mohar–Stacho (arXiv:2409.01513, 2024) on the symmetric Alon–Krivelevich bound does not directly address the asymmetric conditions of Conjecture 7.

 Cited literature (1)

 
 
 
partial Coloring bipartite graphs with semi-small list size
 (2020)
 

 
 Daniel G. Zhu · Annals of Combinatorics · arXiv:2008.06040 · doi:10.1007/s00026-022-00633-z

Studies asymmetric list coloring in the semi-small list size regime; proves improved bounds when one part has list size 2 and states a unified conjecture on general bipartite graphs encompassing all three conditions of Conjecture 7.
 

 

 Reviewer notes. Conjecture 7 unifies three asymmetric generalisations of the Krivelevich–Alon conjecture. Zhu (2008.06040) provides partial progress in the semi-small regime and a unified reformulation but does not resolve the conjecture. No full proof or counterexample found in the surveyed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let the positive integers $\Delta_A, \Delta_B, k_A, k_B$ satisfy one of the following.
(i) Given $\varepsilon > 0$, we have $\Delta_A, \Delta_B \geq \Delta_0$ for some $\Delta_0 = \Delta_0(\varepsilon)$, and $k_A \geq \Delta_A^\varepsilon$ and $k_B \geq \Delta_B^\varepsilon$.
(ii) For some absolute constant $C > 1$, $k_A \geq C \log \Delta_B$ and $k_B \geq C \log \Delta_A$.
(iii) $\Delta_A = \Delta_B = \Delta$, and, for some absolute constant $C > 0$, $k_B \geq C(\Delta/\log\Delta)^{1/k_A} \log\Delta$ or $k_A \geq C(\Delta/\log\Delta)^{1/k_B} \log\Delta$.
Then any bipartite graph $G = (V = A \cup B, E)$ with parts $A$ and $B$ having maximum degrees at most $\Delta_A$ and $\Delta_B$, respectively, is $(k_A, k_B)$-choosable.

Context

Motivated by the asymptotic behaviour of $(k_A, k_B)$-choosability for complete bipartite graphs (Theorem 6 and Theorem 16), the authors conjecture three concrete asymmetric analogues of the Krivelevich–Alon conjecture. Condition (i) is weaker than Conjecture 2; conditions (ii) and (iii) are stronger. The paper shows Conjecture 7 holds for complete bipartite graphs (Theorem 15) and provides partial progress in the general case via Theorem 4 and its corollaries.

Notes. PDF source — math notation verified readable. Three-part conjecture; each part is a separate asymmetric generalisation of Conjecture 2.

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
