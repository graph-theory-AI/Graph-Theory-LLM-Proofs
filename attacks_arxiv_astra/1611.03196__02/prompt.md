Attack the following open graph-theory problem.

Catalog id: 1611.03196__02
Catalog status: open (triage tier 4, lean disprove)
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/arxiv/1611.03196__02/
Source paper: Fair representation by independent sets (arXiv:1611.03196)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.14
If the edge set of a graph $H$ is partitioned into sets $E_1, \ldots, E_m$ then there exists a matching $M$ satisfying $|M \cap E_i| \geq \left\lfloor \frac{|E_i|}{\Delta(H)+2} \right\rfloor$ for all $i \leq m$.

Context:
Proposed as a stronger version of Conjecture 1.12 (the rainbow matching conjecture), extending almost fair representation to arbitrary graphs via the parameter $\Delta(H)+2$, which mirrors the connectivity bound for independence complexes of line graphs.

=== Catalog page (statement + literature review) ===
Fair matching representation via edge partition — Graph-theory open problems (arXiv)

 
 Status
 open
 low confidence
 

 Conjecture 1.14 from arXiv:1611.03196 asserts a fair-representation guarantee for matchings in edge-partitioned graphs: for any partition E_1,...,E_m of E(H) there exists a matching M with |M cap E_i| >= floor(|E_i|/(Delta(H)+2)) for all i. Proposed as a strengthening of the rainbow matching conjecture (Conjecture 1.12) via the connectivity bound for independence complexes of line graphs, the conjecture targets general graphs with no bipartiteness assumption. Multiple searches found no subsequent paper that resolves, refutes, or substantially advances this specific conjecture; the broader rainbow-matching program remains active, but this edge-partition variant appears unaddressed in the indexed literature. Given that the conjecture is nearly a decade old, the absence of any visible resolution warrants low confidence.

 Reviewer notes. No follow-up paper found that directly addresses Conjecture 1.14. The sole internal reference (arXiv:2212.11969) is a false match verified by WebFetch. The conjecture is a strict strengthening of Conjecture 1.12 (rainbow matching conjecture for general graphs), and since 1.12 itself remains open in full generality, 1.14 is almost certainly open. Low confidence reflects the conjecture's age (~9 years) making the absence of a resolution somewhat suspicious, though the niche nature of the exact Delta(H)+2 bound may explain limited follow-up.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. If the edge set of a graph $H$ is partitioned into sets $E_1, \ldots, E_m$ then there exists a matching $M$ satisfying $|M \cap E_i| \geq \left\lfloor \frac{|E_i|}{\Delta(H)+2} \right\rfloor$ for all $i \leq m$.

Context

Proposed as a stronger version of Conjecture 1.12 (the rainbow matching conjecture), extending almost fair representation to arbitrary graphs via the parameter $\Delta(H)+2$, which mirrors the connectivity bound for independence complexes of line graphs.

Notes. PDF source — floor bracket symbol garbled as (cid:107); LaTeX reconstructed from context.

Source paper

 Fair representation by independent sets
 Ron Aharoni, Noga Alon, Eli Berger, Maria Chudnovsky, Dani Kotlar, Martin Loebl, Ran Ziv · 2016-11-10
 https://arxiv.org/abs/1611.03196
 PDF source

=== Source paper abstract / header ===
Abstract:For a hypergraph $H$ let $\beta(H)$ denote the minimal number of edges from $H$ covering $V(H)$. An edge $S$ of $H$ is said to represent {\em fairly} (resp. {\em almost fairly}) a partition $(V_1,V_2, \ldots, V_m)$ of $V(H)$ if $|S\cap V_i|\ge \lfloor\frac{|V_i|}{\beta(H)}\rfloor$ (resp. $|S\cap V_i|\ge \lfloor\frac{|V_i|}{\beta(H)}\rfloor-1$) for all $i \le m$.
In matroids any partition of $V(H)$ can be represented fairly by some independent set. We look for classes of hypergraphs $H$ in which any partition of $V(H)$ can be represented almost fairly by some edge.
We show that this is true when $H$ is the set of independent sets in a path, and conjecture that it is true when $H$ is the set of matchings in $K_{n,n}$. We prove that partitions of $E(K_{n,n})$ into three sets can be represented almost fairly. The methods of proofs are topological.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1611.03196 [math.CO]
 

 
  
 (or 
 arXiv:1611.03196v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1611.03196
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Daniel Kotlar [view email] 
 [v1]
 Thu, 10 Nov 2016 06:31:33 UTC (276 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Fair representation by independent sets, by Ron Aharoni and 6 other authors
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
 | 2016-11
 

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
