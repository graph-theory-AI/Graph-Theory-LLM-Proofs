Attack the following open graph-theory problem.

Catalog id: 2212.05133__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2212.05133__00/
Source paper: New bounds on the maximum number of neighborly boxes in R^d (arXiv:2212.05133)

=== Extracted statement (catalog JSON) ===
Title: Conjecture on the asymptotic of n(2,d)
A general conjecture is posed in the final section which, together with the lower bound $n(2,d) > (1-o(1))\frac{d^2}{2}$, would imply that $\lim_{d\to\infty} \frac{n(2,d)}{d^2} = \frac{1}{2}$.

Context:
The authors establish the lower bound $n(2,d) > (1-o(1))\frac{d^2}{2}$, improving the previous bound $n(2,d) > \frac{d^2}{4}$. They remark that determining the precise asymptotic order of $n(2,d)$ seems to be a hard task (as noted earlier by Alon and by Huang–Sudakov), and refer to a formal conjecture in the final section concerning lamination-based constructions.

=== Catalog page (statement + literature review) ===
n(2,d) asymptotic limit ½ — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 The conjecture that $\lim_{d\to\infty} n(2,d)/d^2 = 1/2$ remains open. A 2024 follow-up by Grytczuk, Kisielewicz, and Przesławski (arXiv:2402.02199) gives new recursive constructions of 2-neighborly families improving the lower bound on $n(2,d)$, and poses an explicit conjectured formula for $n(2,d)$ based on their construction being optimal — this is partial progress but does not resolve the asymptotic limit. A 2025 paper (arXiv:2508.20648) on 'strings with jokers' addresses the regime $k$ close to $d$ (proving $n(d-s,d) \sim \frac{2^s+1}{2^{s+1}} \cdot 2^d$) but does not directly resolve the $k=2$ question.

 Cited literature (2)

 
 
 
partial Neighborly boxes and bipartite coverings; constructions and conjectures
 (2024)
 

 
 Jarosław Grytczuk, Andrzej P. Kisielewicz, Krzysztof Przesławski · arXiv preprint · arXiv:2402.02199

Provides improved lower bounds on n(2,d) via a new recursive construction using 'algebra on ternary strings', conjectures that this construction is optimal and yields an explicit formula for n(2,d), but does not prove the asymptotic limit 1/2.
 

 
 
partial Neighborly boxes and strings with jokers; constructions and asymptotics
 (2025)
 

 
 authors not fully retrieved · arXiv preprint · arXiv:2508.20648

Proves n(d-s,d) ~ (2^s+1)/(2^(s+1)) * 2^d for fixed s, improving lower bounds when k is close to d; does not directly address the k=2 asymptotic conjecture.
 

 

 Reviewer notes. The conjecture from arXiv:2212.05133 that lim n(2,d)/d^2 = 1/2 is still open as of 2026. The follow-up arXiv:2402.02199 improves the lower bound and poses a more explicit conjecture about n(2,d), but does not settle the asymptotic constant. The 2025 paper arXiv:2508.20648 targets a different parameter regime (k near d). Full text of 2402.02199 was not retrievable (HTML 404), so the precise relationship between its conjecture and the 1/2 limit could not be verified; confidence is medium.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. A general conjecture is posed in the final section which, together with the lower bound $n(2,d) > (1-o(1))\frac{d^2}{2}$, would imply that $\lim_{d\to\infty} \frac{n(2,d)}{d^2} = \frac{1}{2}$.

Context

The authors establish the lower bound $n(2,d) > (1-o(1))\frac{d^2}{2}$, improving the previous bound $n(2,d) > \frac{d^2}{4}$. They remark that determining the precise asymptotic order of $n(2,d)$ seems to be a hard task (as noted earlier by Alon and by Huang–Sudakov), and refer to a formal conjecture in the final section concerning lamination-based constructions.

Notes. The formal conjecture appears in Section 3 (the final section on total laminations and computational experiments), which is not present in the provided PDF extract. Only the informal forward-reference in the introduction is available; math may be garbled due to PDF source.

Source paper

 New bounds on the maximum number of neighborly boxes in R^d
 Noga Alon, Jarosław Grytczuk, Andrzej P. Kisielewicz, Krzysztof Przesławski · 2023-03-03
 https://arxiv.org/abs/2212.05133
 PDF source

=== Source paper abstract / header ===
Abstract:A family of axis-aligned boxes in $\er^d$ is \emph{$k$-neighborly} if the intersection of every two of them has dimension at least $d-k$ and at most $d-1$. Let $n(k,d)$ denote the maximum size of such a family. It is known that $n(k,d)$ can be equivalently defined as the maximum number of vertices in a complete graph whose edges can be covered by $d$ complete bipartite graphs, with each edge covered at most $k$ times.
We derive a new upper bound on $n(k,d)$, which implies, in particular, that $n(k,d)\leqslant (2-\delta)^d$ if $k\leqslant (1-\varepsilon)d$, where $\delta>0$ depends on arbitrarily chosen $\varepsilon>0$. The proof applies a classical result of Kleitman, concerning the maximum size of sets with a given diameter in discrete hypercubes. By an explicit construction we obtain also a new lower bound for $n(k,d)$, which implies that $n(k,d)\geqslant (1-o(1))\frac{d^k}{k!}$. We also study $k$-neighborly families of boxes with additional structural properties. Families called \emph{total laminations}, that split in a tree-like fashion, turn out to be particularly useful for explicit constructions. We pose a few conjectures based on these constructions and some computational experiments.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2212.05133 [math.CO]
 

 
  
 (or 
 arXiv:2212.05133v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2212.05133
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Kisielewicz Andrzej [view email] 
 [v1]
 Fri, 9 Dec 2022 22:21:05 UTC (9 KB)

 [v2]
 Mon, 30 Jan 2023 08:52:10 UTC (25 KB)

 [v3]
 Thu, 2 Feb 2023 14:23:28 UTC (25 KB)

 [v4]
 Fri, 3 Mar 2023 07:14:40 UTC (23 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled New bounds on the maximum number of neighborly boxes in R^d, by Noga Alon and 2 other authors
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
 | 2022-12
 

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
