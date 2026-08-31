Attack the following open graph-theory problem.

Catalog id: 2207.13651__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2207.13651__00/
Source paper: On random irregular subgraphs (arXiv:2207.13651)

=== Catalog page (statement + literature review) ===
Property (*) range extension to d = o(n/log n) — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Fox, Luo, and Pham prove Property (*) for the random irregular subgraph model when d = o(n/(log n)^{12}) (Theorem 1.3), and conjecture the result extends to the wider range d = o(n/log n). No subsequent paper resolving this conjecture was found in a web search; the conjecture remains open as of May 2026. The paper appeared in Random Structures & Algorithms (2024).

 Reviewer notes. The paper's main theorem (Theorem 1.3) covers d = o(n/(log n)^{12}); the informal conjecture asks to push this to d = o(n/log n). The authors also remark that for d = omega(n/log n) the model likely fails Property (*). No follow-up resolving or extending this conjecture was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. The irregular random subgraph $H = H(G)$ satisfies Property $(*)$ — that is, $m(H,k) = (1+o(1))n/(d+1)$ for all $0 \leq k \leq d$ — with high probability for all $d = o(n/\log n)$.

Context

After proving Theorem 1.3 for $d = o(n/(\log n)^{12})$, the authors conjecture the range extends to $d = o(n/\log n)$. They also remark that for $d = \omega(n/\log n)$ the random subgraph model likely fails to satisfy Property $(*)$, and that new ideas would be required to establish Conjecture 1.2 in the full range.

Notes. Stated in prose without a labelled theorem environment: 'We conjecture that with high probability for all d = o(n/log n), the irregular random subgraph H satisfies Property *'.

Source paper

 On random irregular subgraphs
 Jacob Fox, Sammy Luo, Huy Tuan Pham · 2022-07-27
 https://arxiv.org/abs/2207.13651
 PDF source

=== Source paper abstract / header ===
Abstract:Let $G$ be a $d$-regular graph on $n$ vertices. Frieze, Gould, Karoński and Pfender began the study of the following random spanning subgraph model $H=H(G)$. Assign independently to each vertex $v$ of $G$ a uniform random number $x(v) \in [0,1]$, and an edge $(u,v)$ of $G$ is an edge of $H$ if and only if $x(u)+x(v) \geq 1$. Addressing a problem of Alon and Wei, we prove that if $d = o(n/(\log n)^{12})$, then with high probability, for each nonnegative integer $k \leq d$, there are $(1+o(1))n/(d+1)$ vertices of degree $k$ in $H$.
 

 
 
 
 Comments:
 18 pages
 

 Subjects:
 
 Combinatorics (math.CO); Probability (math.PR)
 

 Cite as:
 arXiv:2207.13651 [math.CO]
 

 
  
 (or 
 arXiv:2207.13651v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2207.13651
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Huy Tuan Pham [view email] 
 [v1]
 Wed, 27 Jul 2022 17:15:18 UTC (16 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On random irregular subgraphs, by Jacob Fox and 2 other authors
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
 | 2022-07
 

 Change to browse by:
 
 math
 math.PR
 

 

 

 
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
