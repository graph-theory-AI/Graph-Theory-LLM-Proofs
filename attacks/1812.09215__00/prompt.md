Attack the following open graph-theory problem.

Catalog id: 1812.09215__00
Catalog status: open (triage tier 2, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1812.09215__00/
Source paper: Lipschitz bijections between boolean functions (arXiv:1812.09215)

=== Catalog page (statement + literature review) ===
Dictator-to-XOR Lipschitz inverse gap — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The informal question asks whether the gap between the general-map lower bound Ω(1/k)·log n and the linear-map upper bound O(1/log k)·log n (achieved by Rao–Shinkar) for the Lipschitz constant of φ⁻¹ can be closed for general maps. No follow-up paper resolving this gap was found in an extensive web search; the problem appears in an Oxford thesis/problems collection (Johnston) as still open. The conjecture is recent and narrowly specialised, so absence of a follow-up is credible.

 Reviewer notes. The paper was published in Combinatorics, Probability and Computing 30 (2021) 513–525 (DOI 10.1017/S0963548320000541). The earlier related paper arXiv:1501.03016 (Rao–Shinkar) gives the O(1/log k) linear-map construction that achieves the upper bound. An Oxford DPhil thesis/problems document (ORA uuid:970b5eb2) explicitly lists the Ω(1/k) vs O(1/log k) gap as an open problem. No follow-up resolving the informal question was found after five web calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Does there exist a map $\phi$ from Dictator to XOR which is $C$-Lipschitz, where each output bit depends on at most $k$ input bits, and such that $\phi^{-1}$ is $o(\log n / \log k)$-Lipschitz as $n, k \to \infty$?

Context

Theorem 1 shows that for general maps the inverse must be at least $\Omega(1/k)\cdot\log n$-Lipschitz, while for linear maps the bound is $\Omega(1/\log k)\cdot\log n$-Lipschitz. Rao and Shinkar's construction achieves $\delta(2,k)=O(1/\log k)$ for linear maps, matching the linear-map lower bound, but a gap remains for general maps between $\Omega(1/k)$ and $O(1/\log k)$.

Notes. Stated in running prose as 'This raises the following question:' without a labelled theorem environment.

Source paper

 Lipschitz bijections between boolean functions
 Tom Johnston, Alex Scott · 2021-12-10
 https://arxiv.org/abs/1812.09215
 PDF source

=== Source paper abstract / header ===
Abstract:We answer four questions from a recent paper of Rao and Shinkar on Lipschitz bijections between functions from $\{0,1\}^n$ to $\{0,1\}$. (1) We show that there is no $O(1)$-bi-Lipschitz bijection from $\mathrm{Dictator}$ to $\mathrm{XOR}$ such that each output bit depends on $O(1)$ input bits. (2) We give a construction for a mapping from $\mathrm{XOR}$ to $\mathrm{Majority}$ which has average stretch $O(\sqrt{n})$, matching a previously known lower bound. (3) We give a 3-Lipschitz embedding $\phi : \{0,1\}^n \to \{0,1\}^{2n+1}$ such that $\mathrm{XOR}(x) = \mathrm{Majority}(\phi(x))$ for all $x \in \{0,1\}^n$. (4) We show that with high probability there is a $O(1)$-bi-Lipschitz mapping from $\mathrm{Dictator}$ to a uniformly random balanced function.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:1812.09215 [math.CO]
 

 
  
 (or 
 arXiv:1812.09215v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1812.09215
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Combinator. Probab. Comp. 30 (2021) 513-525
 

 
 
 Related DOI:
 
 https://doi.org/10.1017/S0963548320000541

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tom Johnston [view email] 
 [v1]
 Fri, 21 Dec 2018 15:59:12 UTC (14 KB)

 [v2]
 Wed, 26 Feb 2020 15:52:43 UTC (16 KB)

 [v3]
 Fri, 10 Dec 2021 12:55:48 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Lipschitz bijections between boolean functions, by Tom Johnston and Alex Scott
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
 | 2018-12
 

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
