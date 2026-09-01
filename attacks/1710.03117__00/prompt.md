Attack the following open graph-theory problem.

Catalog id: 1710.03117__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1710.03117__00/
Source paper: On classes of graphs with strongly sublinear separators (arXiv:1710.03117)

=== Extracted statement (catalog JSON) ===
Title: Informal Conjecture (constant-size M)
I conjecture that there actually always exists a balanced separator $C \cup M$ of $G$ with $q(C) \leq q(V(G))/\ell$ for some set $M$ of constant size (dependent on the class and $\ell$, but not on $|V(G)|$).

Context:
Theorem 5 guarantees a weighted balanced separator $C \cup M$ with $q(C) \leq q(V(G))/\ell$, but the bound on $|M|$ is only polylogarithmic in $n$ for graphs from a class with polynomial $\omega$-expansion. The author conjectures this polylogarithmic dependence on $n$ can be eliminated entirely, yielding a set $M$ of size depending only on the graph class and $\ell$.

=== Catalog page (statement + literature review) ===
Constant-size separator M in bounded expansion — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No published paper resolving this conjecture was found. Dvořák's 2022 Journal of Graph Theory paper 'On weighted sublinear separators' is a likely follow-up, but its full content is behind a paywall and could not be verified. The conjecture that the polylogarithmic-in-n bound on |M| in the weighted balanced separator C∪M can be replaced by a constant depending only on the graph class and ℓ remains, as far as can be determined from open-access sources, open.

 Reviewer notes. Dvořák published a follow-up paper 'On weighted sublinear separators' in J. Graph Theory 2022 (DOI 10.1002/jgt.22777) which may address this conjecture, but the paper is paywalled and the abstract does not explicitly mention the constant-size M conjecture. The 2022 paper 'Product Structure of Graph Classes with Strongly Sublinear Separators' (arXiv:2208.10074) and the 2026 paper 'Coarse Balanced Separators in Fat-Minor-Free Graphs' (arXiv:2604.11318) do not appear to reference this specific conjecture. Confidence is medium rather than high because the conjecture is ~8 years old and a relevant paywalled paper could not be fully verified.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. I conjecture that there actually always exists a balanced separator $C \cup M$ of $G$ with $q(C) \leq q(V(G))/\ell$ for some set $M$ of constant size (dependent on the class and $\ell$, but not on $|V(G)|$).

Context

Theorem 5 guarantees a weighted balanced separator $C \cup M$ with $q(C) \leq q(V(G))/\ell$, but the bound on $|M|$ is only polylogarithmic in $n$ for graphs from a class with polynomial $\omega$-expansion. The author conjectures this polylogarithmic dependence on $n$ can be eliminated entirely, yielding a set $M$ of size depending only on the graph class and $\ell$.

Notes. Stated as inline prose in the bullet-point remarks following Theorem 5; no labelled theorem environment.

Source paper

 On classes of graphs with strongly sublinear separators
 Zdeněk Dvořák · 2018-02-09
 https://arxiv.org/abs/1710.03117
 PDF source

=== Source paper abstract / header ===
Abstract:For real numbers c,epsilon>0, let G_{c,epsilon} denote the class of graphs G such that each subgraph H of G has a balanced separator of order at most c|V(H)|^{1-epsilon}. A class of graphs has strongly sublinear separators if it is a subclass of G_{c,epsilon} for some c,epsilon>0. We investigate properties of such graph classes, leading in particular to an approximate algorithm to determine membership in G_{c,epsilon}: there exist c'>0 such that for each input graph G, this algorithm in polynomial time determines either that G belongs to G_{c',epsilon^2/160}, or that G does not belong to G_{c,epsilon}.
 

 
 
 
 Comments:
 18 pages, no figures; updated according to reviewer comments
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C75 (Primary) 05C85 (Secondary)
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:1710.03117 [math.CO]
 

 
  
 (or 
 arXiv:1710.03117v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1710.03117
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Mon, 9 Oct 2017 14:35:09 UTC (13 KB)

 [v2]
 Fri, 9 Feb 2018 15:52:02 UTC (14 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On classes of graphs with strongly sublinear separators, by Zden\v{e}k Dvo\v{r}\'ak
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
 | 2017-10
 

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
