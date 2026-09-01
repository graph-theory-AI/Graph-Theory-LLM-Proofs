Attack the following open graph-theory problem.

Catalog id: 2009.07840__00
Catalog status: partial (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2009.07840__00/
Source paper: Typical and Extremal Aspects of Friends-and-Strangers Graphs (arXiv:2009.07840)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture (§1.2, Theorem 1.1 remarks)
The threshold for $\mathrm{FS}(X, Y)$ to be connected when $X, Y \sim G(n,p)$ is determined by the isolated-vertex threshold: ``it seems that (as in the usual case of a binomial random graph) this local obstruction to connectedness tells essentially the whole story.''

Context:
Theorem 1.1 establishes a lower bound $p \leq (2^{-1/2}-\varepsilon)/n^{1/2}$ arising from isolated vertices and an upper bound $p \geq \exp(2(\log n)^{2/3})/n^{1/2}$ for the high-probability connectivity threshold of $\mathrm{FS}(X,Y)$. The authors suggest the gap between these bounds is an artifact of the proof method and that the two thresholds should coincide up to lower-order factors.

=== Catalog page (statement + literature review) ===
Isolated-vertex threshold for FS(X,Y) connectivity — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Three follow-up papers have narrowed the gap in Theorem 1.1 of the source paper. Milojevic (arXiv:2210.03864, 2022) improved the isolated-vertex lower bound and disproved two formal conjectures from the source paper about threshold probabilities. Krishnan and Li (arXiv:2410.21334, 2024) established k-connectivity for p ≥ n^{-1/2+o(1)}, bringing the connectivity upper bound and isolated-vertex lower bound to the same asymptotic order n^{-1/2+o(1)}, broadly consistent with the informal conjecture. A sharp threshold matching an exact constant has not been proved.

 Cited literature (3)

 
 
 
partial Connectivity of friends-and-strangers graphs on random pairs
 (2022)
 

 
 Lanchao Wang, Yaojun Chen · Discrete Mathematics · arXiv:2208.00801

Extends the connectivity threshold analysis to the asymmetric case X ∈ G(n,p₁), Y ∈ G(n,p₂), showing FS(X,Y) is connected with high probability when p₁p₂ ≥ n^{-1+o(1)}, consistent with the isolated-vertex-threshold heuristic.
 

 
 
partial Connectivity of Old and New Models of Friends-and-Strangers Graphs
 (2022)
 

 
 Aleksa Milojevic · arXiv preprint · arXiv:2210.03864

Slightly improves the isolated-vertex lower bound on the disconnectedness threshold for FS(X,Y) when X,Y ∼ G(n,p), showing isolated vertices persist up to p = O(log n / n^{1/2}), and in doing so disproves two formal conjectures of Alon, Defant, and Kravitz about specific threshold probabilities.
 

 
 
partial On the Connectivity of Friends-and-strangers Graphs
 (2024)
 

 
 Neil Krishnan, Rupert Li · arXiv preprint · arXiv:2410.21334

Shows that for independent G(n,p₁) and G(n,p₂) with p₁p₂ ≥ p₀² where p₀ = n^{-1/2+o(1)}, FS(X,Y) is k-connected with high probability, improving the connectivity upper bound in the symmetric case to the same n^{-1/2+o(1)} order as the isolated-vertex threshold.
 

 

 Reviewer notes. The two formal conjectures disproved by Milojevic (arXiv:2210.03864) appear to be distinct formal conjectures in the source paper about specific threshold values, not the informal conjecture reviewed here; the full paper text could not be retrieved so the exact disproved statements are unconfirmed. The informal conjecture (connectivity threshold determined by isolated-vertex threshold) is broadly consistent with current bounds — both lower and upper bounds now sit at n^{-1/2+o(1)} — but the sharp threshold with an exact constant matching the isolated-vertex threshold has not been established.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. The threshold for $\mathrm{FS}(X, Y)$ to be connected when $X, Y \sim G(n,p)$ is determined by the isolated-vertex threshold: ``it seems that (as in the usual case of a binomial random graph) this local obstruction to connectedness tells essentially the whole story.''

Context

Theorem 1.1 establishes a lower bound $p \leq (2^{-1/2}-\varepsilon)/n^{1/2}$ arising from isolated vertices and an upper bound $p \geq \exp(2(\log n)^{2/3})/n^{1/2}$ for the high-probability connectivity threshold of $\mathrm{FS}(X,Y)$. The authors suggest the gap between these bounds is an artifact of the proof method and that the two thresholds should coincide up to lower-order factors.

Notes. PDF source; prose conjecture without a labelled environment. Section 7 (explicitly titled as containing open questions and conjectures) is absent from the supplied text, so further items from that section could not be extracted.

Source paper

 Typical and Extremal Aspects of Friends-and-Strangers Graphs
 Noga Alon, Colin Defant, Noah Kravitz · 2021-06-15
 https://arxiv.org/abs/2009.07840
 PDF source

=== Source paper abstract / header ===
Abstract:Given graphs $X$ and $Y$ with vertex sets $V(X)$ and $V(Y)$ of the same cardinality, the friends-and-strangers graph $\mathsf{FS}(X,Y)$ is the graph whose vertex set consists of all bijections $\sigma:V(X)\to V(Y)$, where two bijections $\sigma$ and $\sigma'$ are adjacent if they agree everywhere except for two adjacent vertices $a,b \in V(X)$ such that $\sigma(a)$ and $\sigma(b)$ are adjacent in $Y$. The most fundamental question that one can ask about these friends-and-strangers graphs is whether or not they are connected; we address this problem from two different perspectives. First, we address the case of "typical" $X$ and $Y$ by proving that if $X$ and $Y$ are independent Erdős-Rényi random graphs with $n$ vertices and edge probability $p$, then the threshold probability guaranteeing the connectedness of $\mathsf{FS}(X,Y)$ with high probability is $p=n^{-1/2+o(1)}$. Second, we address the case of "extremal" $X$ and $Y$ by proving that the smallest minimum degree of the $n$-vertex graphs $X$ and $Y$ that guarantees the connectedness of $\mathsf{FS}(X,Y)$ is between $3n/5+O(1)$ and $9n/14+O(1)$. When $X$ and $Y$ are bipartite, a parity obstruction forces $\mathsf{FS}(X,Y)$ to be disconnected. In this bipartite setting, we prove analogous "typical" and "extremal" results concerning when $\mathsf{FS}(X,Y)$ has exactly $2$ connected components; for the extremal question, we obtain a nearly exact result.
 

 
 
 
 Comments:
 31 pages, 4 figures
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C35, 05C40, 05C80
 

 Cite as:
 arXiv:2009.07840 [math.CO]
 

 
  
 (or 
 arXiv:2009.07840v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2009.07840
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Colin Defant [view email] 
 [v1]
 Wed, 16 Sep 2020 17:59:08 UTC (114 KB)

 [v2]
 Tue, 15 Jun 2021 13:52:38 UTC (115 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Typical and Extremal Aspects of Friends-and-Strangers Graphs, by Noga Alon and 2 other authors
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
 | 2020-09
 

 Change to browse by:
 
 cs
 cs.DM
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
