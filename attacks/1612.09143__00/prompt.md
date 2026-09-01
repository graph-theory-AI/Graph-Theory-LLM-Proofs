Attack the following open graph-theory problem.

Catalog id: 1612.09143__00
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1612.09143__00/
Source paper: Many cliques in $H$-free subgraphs of random graphs (arXiv:1612.09143)

=== Extracted statement (catalog JSON) ===
Title: Motivating Question (Introduction)
For which values of $p$ is it true that $\mathrm{ex}(G(n,p), K_m, H) = (1+o(1))\binom{k-1}{m}\left(\frac{n}{k-1}\right)^m p^{\binom{m}{2}}$ w.h.p.?

Context:
For any fixed $H$ with $\chi(H)=k>m$ the deterministic extremal result gives $\mathrm{ex}(n,K_m,H)=(1+o(1))\binom{k-1}{m}(n/(k-1))^m$. Analogous to the edge case characterised by Theorem 1.1, the authors ask for which values of $p$ this extremal count is achieved with high probability in $G(n,p)$. The paper answers the question fully when $m_2(H)\geq m_2(K_m)$ (Theorem 1.2) and only partially when $m_2(H)<m_2(K_m)$ (Theorem 1.4), leaving the exact transition threshold in the latter case open; the paper closes with a dedicated Section 6 of open problems not included in the provided text.

=== Catalog page (statement + literature review) ===
Kₘ extremal threshold in H-free G(n,p) — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 The source paper resolves the question when $m_2(H) \geq m_2(K_m)$ (Theorem 1.2) but only partially when $m_2(H) < m_2(K_m)$ (Theorem 1.4), leaving the exact transition threshold in the harder regime open. Samotij and Shikhelman (arXiv:1806.06609, 2018) generalise the problem to arbitrary pattern graphs $T$ in place of $K_m$: for the case $m_2(H) \leq m_2(T)$ they identify that threshold locations are governed by densities of coverings of $H$ by copies of $T$, reducing the question to deterministic hypergraph Tur\'{a}n problems that remain unsolved in full generality. The full question --- in particular the exact threshold when $m_2(H) < m_2(K_m)$ --- remains open.

 Cited literature (1)

 
 
 
partial A generalized Turán problem in random graphs
 (2018)
 

 
 Wojciech Samotij, Clara Shikhelman · arXiv preprint · arXiv:1806.06609

Extends the threshold analysis to arbitrary pattern graph T (not just K_m) and, for the harder case m_2(H) ≤ m_2(T), reduces the exact threshold question to deterministic hypergraph Turán problems without resolving them in full generality.
 

 

 Reviewer notes. Samotij-Shikhelman (1806.06609) is the main verified post-paper follow-up; it makes structural progress on the threshold question but does not settle it in full generality, especially for the regime m_2(H) < m_2(K_m). Morris-Riordan (arXiv:2504.00964, 2025) studies clique distributions in G(n,p) but addresses K_r-factors, not the H-free Turán threshold question.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. For which values of $p$ is it true that $\mathrm{ex}(G(n,p), K_m, H) = (1+o(1))\binom{k-1}{m}\left(\frac{n}{k-1}\right)^m p^{\binom{m}{2}}$ w.h.p.?

Context

For any fixed $H$ with $\chi(H)=k>m$ the deterministic extremal result gives $\mathrm{ex}(n,K_m,H)=(1+o(1))\binom{k-1}{m}(n/(k-1))^m$. Analogous to the edge case characterised by Theorem 1.1, the authors ask for which values of $p$ this extremal count is achieved with high probability in $G(n,p)$. The paper answers the question fully when $m_2(H)\geq m_2(K_m)$ (Theorem 1.2) and only partially when $m_2(H)<m_2(K_m)$ (Theorem 1.4), leaving the exact transition threshold in the latter case open; the paper closes with a dedicated Section 6 of open problems not included in the provided text.

Notes. Posed in introductory prose without a labelled environment. Section 6 (open problems) is absent from the provided PDF extraction, so further explicit open-problem formulations may be missing. PDF source — math may be garbled.

Source paper

 Many cliques in $H$-free subgraphs of random graphs
 Noga Alon, Alexandr Kostochka, Clara Shikhelman · 2017-11-19
 https://arxiv.org/abs/1612.09143
 PDF source

=== Source paper abstract / header ===
Abstract:For two fixed graphs $T$ and $H$ let $ex(G(n,p),T,H)$ be the random variable counting the maximum number of copies of $T$ in an $H$-free subgraph of the random graph $G(n,p)$. We show that for the case $T=K_m$ and $\chi(H)> m$ the behavior of $ex(G(n,p),K_m,H)$ depends strongly on the relation between $p$ and $m_2(H)=\max_{H'\subset H, |V(H')|'\geq 3}\left\{ \frac{e(H')-1}{v(H')-2} \right\}$.
When $m_2(H)> m_2(K_m)$ we prove that with high probability, depending on the value of $p$, either one can maintain almost all copies of $K_m$, or it is asymptotically best to take a $\chi(H)-1$ partite subgraph of $G(n,p)$. The transition between these two behaviors occurs at $p=n^{-1/m_2(H)}$. When $m_2(H)< m_2(K_m)$ we show that the above cases still exist, however for $\delta>0$ small at $p=n^{-1/m_2(H)+\delta}$ one can typically still keep most of the copies of $K_m$ in an $H$-free subgraph of $G(n,p)$. Thus, the transition between the two behaviors in this case occurs at some $p$ significantly bigger than $n^{-1/m_2(H)}$.
To show that the second case is not redundant we present a construction which may be of independent interest. For each $k \geq 4$ we construct a family of $k$ chromatic graphs $G(k,\epsilon_i)$ where $m_2(G(k,\epsilon_i))$ tends to $\frac{(k+1)(k-2)}{2(k-1)} (< m_2(K_{k-1}))$ as $i$ tends to infinity. This is tight for all values of $k$
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1612.09143 [math.CO]
 

 
  
 (or 
 arXiv:1612.09143v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1612.09143
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Clara Shikhelman [view email] 
 [v1]
 Thu, 29 Dec 2016 13:49:27 UTC (28 KB)

 [v2]
 Sun, 19 Nov 2017 11:20:09 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Many cliques in $H$-free subgraphs of random graphs, by Noga Alon and 1 other authors
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
 | 2016-12
 

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
