Attack the following open graph-theory problem.

Catalog id: 2402.10782__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2402.10782__00/
Source paper: Finding forest-orderings of tournaments is NP-complete (arXiv:2402.10782)

=== Catalog page (statement + literature review) ===
FPT approximation for tournament forest-ordering — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 4.2 asks for a function f and polynomial-time approximation scheme that, given a tournament T and integer k, either certifies the tournament clique number satisfies $\overrightarrow{\omega}(T)\geq k$ or finds an ordering $\prec$ with $\omega(T^{\prec})\leq f(k)$. The k=3 case was settled (with a constant bound) by Aboulker, Aubian, Charbit, and Thomassé (personal communication cited as [2] in the source paper), but the general case for all k remains open. No follow-up papers resolving or partially resolving the general conjecture were found in a broad web search conducted in May 2026, consistent with the conjecture being only ~4 months old.

 Reviewer notes. The conjecture was posed in the concluding section (Section 4) of arXiv:2402.10782 (last revised 2026-01-23). The k=3 base case is established by an unpublished personal communication (Aboulker, Aubian, Charbit, Thomassé), not a public paper. No published or arXiv follow-up addressing the general case was found within the 5-call web search budget. The closely related paper arXiv:2310.04265 ('Clique number of tournaments') introduces the $\overrightarrow{\omega}$ notation and its relation to dichromatic number, and arXiv:2401.07776 ('Computing the clique number of tournaments') addresses computational aspects, but neither appears to resolve Conjecture 4.2.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There is a function $f$ such that for every integer $k$, there is a polynomial-time algorithm that, given a tournament $T$, correctly concludes that $\operatorname{\overrightarrow{\omega}}(T)\geq k$, or finds an order $\prec$ of $V(T)$ such that $\omega(T^{\prec})\leq f(k)$

Context

Aboulker et al. [2] proved an approximation version for $k=3$: there is a constant $c$ and a polynomial-time algorithm that either certifies $\operatorname{\overrightarrow{\omega}}(T)\geq 3$ or finds an ordering $\prec$ with $\omega(T^{\prec})\leq c$. The conjecture asks whether such an approximation scheme extends to all $k$.

Source paper

 Finding forest-orderings of tournaments is NP-complete
 Pierre Aboulker, Guillaume Aubian, Raul Lopes · 2026-01-23
 https://arxiv.org/abs/2402.10782

=== Source paper abstract / header ===
Abstract:Given a class of (undirected) graphs $\mathcal{C}$, we say that a Feedback Arc Set (FAS for short) $F$ is a $\mathcal{C}$-FAS if the graph induced by the edges of $F$ (forgetting their orientations) belongs to $\mathcal{C}$. We show that deciding if a tournament has a $\mathcal{C}$-FAS is NP-complete when $\mathcal{C}$ is the class of all forests. We are motivated by connections between $\mathcal{C}$-FAS and structural parameters of tournaments, such as the dichromatic number, the clique number of tournaments, and the strong Erdős-Hajnal property.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2402.10782 [math.CO]
 

 
  
 (or 
 arXiv:2402.10782v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2402.10782
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Mathematics & Theoretical Computer Science, vol. 28:2, Graph Theory (July 21, 2026) dmtcs:14281
 

 
 
 Related DOI:
 
 https://doi.org/10.46298/dmtcs.14281

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Raul Lopes [view email] 
 [v1]
 Fri, 16 Feb 2024 16:05:22 UTC (18 KB)

 [v2]
 Wed, 11 Sep 2024 15:18:35 UTC (19 KB)

 [v3]
 Fri, 23 Jan 2026 14:21:14 UTC (20 KB)

 [v4]
 Fri, 17 Jul 2026 12:05:29 UTC (26 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Finding forest-orderings of tournaments is NP-complete, by Pierre Aboulker and 2 other authors
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
 | 2024-02
 

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
