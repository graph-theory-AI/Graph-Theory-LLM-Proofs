Attack the following open graph-theory problem.

Catalog id: 1812.02420__03
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1812.02420__03/
Source paper: On the Complexity of Digraph Colourings and Vertex Arboricity (arXiv:1812.02420)

=== Extracted statement (catalog JSON) ===
Title: Problem 5.40
For given $k,b\in\mathbb{N}$ with $k\geq b$, is there a directed graph $\vec{K}(k,b)$ with vertex set $\binom{[k]}{b}$ such that the following holds? The subdigraph of $\vec{K}(k,b)$ induced by any $\{B_{1},\ldots,B_{l}\}\subseteq\binom{[k]}{b}$ is acylic if and only if $\bigcap_{i=1}^{l}{B_{i}}\neq\emptyset$.

Context:
Such 'directed Kneser graphs' $\vec{K}(k,b)$ would allow $b$-tuple $k$-colourings of digraphs to be equivalent to the existence of circular homomorphisms to $\vec{K}(k,b)$, tying the fractional dichromatic number to circular homomorphism theory. Existence is confirmed for $k=b+1$ via the directed cycle of length $b+1$, but the general case is open.

=== Catalog page (statement + literature review) ===
Directed Kneser graph existence for b-tuple colourings — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 No paper has been found that constructs the directed Kneser graphs $\vec{K}(k,b)$ of Problem 5.40 for general $k\geq b$, or refutes their existence. Related work studies the dichromatic number of Kneser-type digraphs (arXiv:2309.16565, arXiv:2511.12553) and develops circular homomorphism theory, but none directly resolves whether the intersection-acyclicity equivalence required by Problem 5.40 can be achieved. The only confirmed case ($k=b+1$, the directed $(b+1)$-cycle) remains as stated in the source paper.

 Reviewer notes. Search surfaced two related papers: arXiv:2309.16565 ('Colouring Complete Multipartite and Kneser-type Digraphs', 2023) studies dichromatic numbers of Kneser digraphs with canonical orientations; arXiv:2511.12553 ('On the Dichromatic Number of Generalized Kneser and Johnson Digraphs', 2025) extends this to generalized Kneser and Johnson digraphs. Neither addresses the specific intersection-acyclicity construction of Problem 5.40. No follow-up resolving the problem was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. For given $k,b\in\mathbb{N}$ with $k\geq b$, is there a directed graph $\vec{K}(k,b)$ with vertex set $\binom{[k]}{b}$ such that the following holds? The subdigraph of $\vec{K}(k,b)$ induced by any $\{B_{1},\ldots,B_{l}\}\subseteq\binom{[k]}{b}$ is acylic if and only if $\bigcap_{i=1}^{l}{B_{i}}\neq\emptyset$.

Context

Such 'directed Kneser graphs' $\vec{K}(k,b)$ would allow $b$-tuple $k$-colourings of digraphs to be equivalent to the existence of circular homomorphisms to $\vec{K}(k,b)$, tying the fractional dichromatic number to circular homomorphism theory. Existence is confirmed for $k=b+1$ via the directed cycle of length $b+1$, but the general case is open.

Source paper

 On the Complexity of Digraph Colourings and Vertex Arboricity
 Winfried Hochstättler, Felix Schröder, Raphael Steiner · 2020-01-09
 https://arxiv.org/abs/1812.02420

=== Source paper abstract / header ===
Abstract:It has been shown by Bokal et al. that deciding 2-colourability of digraphs is an NP-complete problem. This result was later on extended by Feder et al. to prove that deciding whether a digraph has a circular $p$-colouring is NP-complete for all rational $p>1$. In this paper, we consider the complexity of corresponding decision problems for related notions of fractional colourings for digraphs and graphs, including the star dichromatic number, the fractional dichromatic number and the circular vertex arboricity. We prove the following results:
Deciding if the star dichromatic number of a digraph is at most $p$ is NP-complete for every rational $p>1$.
Deciding if the fractional dichromatic number of a digraph is at most $p$ is NP-complete for every $p>1, p \neq 2$.
Deciding if the circular vertex arboricity of a graph is at most $p$ is NP-complete for every rational $p>1$.
To show these results, different techniques are required in each case. In order to prove the first result, we relate the star dichromatic number to a new notion of homomorphisms between digraphs, called circular homomorphisms, which might be of independent interest. We provide a classification of the computational complexities of the corresponding homomorphism colouring problems similar to the one derived by Feder et al. for acyclic homomorphisms.
 

 
 
 
 Comments:
 21 pages, 1 figure
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1812.02420 [math.CO]
 

 
  
 (or 
 arXiv:1812.02420v4 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1812.02420
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Mathematics & Theoretical Computer Science, vol. 22 no. 1, Graph Theory (January 21, 2020) dmtcs:5140
 

 
 
 Related DOI:
 
 https://doi.org/10.23638/DMTCS-22-1-4

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Thu, 6 Dec 2018 09:33:41 UTC (21 KB)

 [v2]
 Mon, 28 Jan 2019 21:17:07 UTC (27 KB)

 [v3]
 Wed, 11 Dec 2019 21:54:34 UTC (32 KB)

 [v4]
 Thu, 9 Jan 2020 13:07:09 UTC (32 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On the Complexity of Digraph Colourings and Vertex Arboricity, by Winfried Hochst\"attler and 2 other authors
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
