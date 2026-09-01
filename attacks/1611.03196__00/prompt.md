Attack the following open graph-theory problem.

Catalog id: 1611.03196__00
Catalog status: open (triage tier 3, lean disprove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1611.03196__00/
Source paper: Fair representation by independent sets (arXiv:1611.03196)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.6
Given a partition of the vertex set of a path into sets $V_1, \ldots, V_m$ there exists an independent set $S$ and integers $b_i$, $i \leq m$, such that $|S \cap V_i| \geq \frac{|V_i|}{2} - b_i$ for all $i$, and 1. $\sum_{i \leq m} b_i \leq \frac{m}{2}$ and 2. $b_i \leq 1$ for all $i \leq m$.

Context:
The paper proves (Theorem 1.7) that either condition alone holds for the independence complex of a path, but not necessarily both simultaneously. Conjecture 1.6 asserts both conditions can be satisfied at once. The matching complex of a path is the independence complex of a path one vertex shorter.

=== Catalog page (statement + literature review) ===
Simultaneous fair representation in path partitions — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No follow-up paper was found that resolves the full statement of Conjecture 1.6 from arXiv:1611.03196, which asks for an independent set in a partitioned path satisfying both the global budget condition (sum b_i ≤ m/2) and the per-part cap (b_i ≤ 1) simultaneously. Related work has appeared on fair representation in cycles (computational complexity, PPA-completeness) and sparse graphs, but these address different graph classes. Alishahi and Meunier (2017, arXiv:1704.02921) proved 'a conjecture of Ron Aharoni and coauthors' about colored paths, but this could not be confirmed to be specifically Conjecture 1.6; it may instead resolve a different conjecture from the same paper.

 Cited literature (1)

 
 
 
partial Fair splitting of colored paths
 (2017)
 

 
 Meysam Alishahi, Frédéric Meunier · arXiv preprint · arXiv:1704.02921

Proves 'a conjecture of Ron Aharoni and coauthors' about fair splitting of colored paths into two disjoint independent sets, but which specific conjecture from arXiv:1611.03196 this resolves could not be confirmed; it may be a different conjecture from the same paper rather than Conjecture 1.6.
 

 

 Reviewer notes. Conjecture 1.6 is a joint condition combining two separately-provable bounds (Theorem 1.7 of the source paper). Related literature has grown around cycles and sparse graphs (fair representation in cycles, PPA-completeness of finding such sets), but no paper explicitly claiming to prove or disprove Conjecture 1.6 for paths was found. The conjecture is 9 years old, so medium rather than high confidence in 'open' status.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Given a partition of the vertex set of a path into sets $V_1, \ldots, V_m$ there exists an independent set $S$ and integers $b_i$, $i \leq m$, such that $|S \cap V_i| \geq \frac{|V_i|}{2} - b_i$ for all $i$, and 1. $\sum_{i \leq m} b_i \leq \frac{m}{2}$ and 2. $b_i \leq 1$ for all $i \leq m$.

Context

The paper proves (Theorem 1.7) that either condition alone holds for the independence complex of a path, but not necessarily both simultaneously. Conjecture 1.6 asserts both conditions can be satisfied at once. The matching complex of a path is the independence complex of a path one vertex shorter.

Notes. PDF source — sum symbol garbled as (cid:80) and fractions may be garbled; LaTeX reconstructed from context.

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
