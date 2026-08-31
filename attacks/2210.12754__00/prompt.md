Attack the following open graph-theory problem.

Catalog id: 2210.12754__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2210.12754__00/
Source paper: Largest subgraph from a hereditary property in a random graph (arXiv:2210.12754)

=== Catalog page (statement + literature review) ===
p(n) range for hereditary subgraph concentration — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The source paper proves Theorem 1.1 for fixed p ∈ (0,1) and for p = p(n) satisfying n^{−c} ≤ p ≤ 1−n^{−c}, but the full characterization of all p = p(n) for which the conclusion holds remains open. A 2024 follow-up (arXiv:2405.09486) explicitly addresses a question of Alon, Krivelevich and Samotij in the hereditary setting but still restricts its main results to fixed p ∈ (0,1), leaving the variable-probability regime unresolved.

 Cited literature (1)

 
 
 
partial Subgraphs of random graphs in hereditary families
 (2024)
 

 
 not verified from abstract · arXiv preprint · arXiv:2405.09486

Explicitly addresses a question of Alon, Krivelevich and Samotij about subgraphs in hereditary families, but its stated results remain in the regime of fixed p ∈ (0,1) rather than characterizing all p = p(n).
 

 

 Reviewer notes. No paper found that resolves the full characterization of all p = p(n). arXiv:2405.09486 (2024) is the closest follow-up, explicitly citing the question of Alon-Krivelevich-Samotij, but its results are for fixed p. A related paper arXiv:2405.05902 (Fox, Nenadov, Pham; Combinatorica 2025, 'The Largest Subgraph Without A Forbidden Induced Subgraph') generalizes the framework to pseudorandom/quasirandom host graphs, but it was found via search only and not fully verified via WebFetch so is excluded from since_posted. The conjecture is open with medium confidence because active follow-up work exists but the specific p = p(n) characterization problem appears unaddressed.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Characterize all edge probabilities $p = p(n)$ for which the assertion of Theorem 1.1 holds.

Context

Theorem 1.1 is proved for fixed $p \in (0,1)$ and (via Proposition 2.1) for $p = p(n)$ satisfying $n^{-c} \leq p \leq 1-n^{-c}$. The authors note that hereditary (even monotone) properties exist for which the fraction of edges of $G(n,p)$ lying in a maximum in-$\mathcal{P}$ subgraph changes, whp, several times as $p$ increases from 0 to 1.

Notes. PDF source; stated as an informal open problem in the concluding remarks without a labelled environment.

Source paper

 Largest subgraph from a hereditary property in a random graph
 Noga Alon, Michael Krivelevich, Wojciech Samotij · 2022-10-23
 https://arxiv.org/abs/2210.12754
 PDF source

=== Source paper abstract / header ===
Abstract:We prove that for every non-trivial hereditary family of graphs ${\cal P}$ and for every fixed $p \in (0,1)$, the maximum possible number of edges in a subgraph of the random graph $G(n,p)$ which belongs to ${\cal P}$ is, with high probability, $$ \left(1-\frac{1}{k-1}+o(1)\right)p{n \choose 2}, $$ where $k$ is the minimum chromatic number of a graph that does not belong to ${\cal P}$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C80, 05C35
 

 Cite as:
 arXiv:2210.12754 [math.CO]
 

 
  
 (or 
 arXiv:2210.12754v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2210.12754
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Michael Krivelevich [view email] 
 [v1]
 Sun, 23 Oct 2022 15:39:53 UTC (7 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Largest subgraph from a hereditary property in a random graph, by Noga Alon and 2 other authors
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
 | 2022-10
 

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
