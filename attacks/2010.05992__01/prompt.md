Attack the following open graph-theory problem.

Catalog id: 2010.05992__01
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2010.05992__01/
Source paper: Near-sunflowers and focal families (arXiv:2010.05992)

=== Extracted statement (catalog JSON) ===
Title: Informal conjecture on non-tightness of upper bound for binary focal families
For $q = 2$ and large $n$, the upper bound $g^{q\text{-ff}}_r(n) \leq (r-1)\, q^{\lceil (r-2)n/(r-1) \rceil}$ of Theorem 1.3 is not tight.

Context:
Proposition 3.2 shows via Reed-Solomon codes that the upper bound is essentially tight when $q \geq n$ and $q$ is a prime power. The authors believe the binary case ($q = 2$) behaves differently, and support this belief by proving in Section 4 that the bound can be significantly improved when the family of binary vectors forms a linear code (closed under addition modulo 2).

=== Catalog page (statement + literature review) ===
Binary focal family upper bound non-tightness — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 A 2024 follow-up by Huang, Shangguan, Zhang, and Zhao (arXiv:2410.23611) establishes asymptotically optimal bounds on the maximum size of focal-free uniform hypergraphs and codes, proving that the Alon–Holzman multiplicative constant (r-1) in the upper bound is not tight in general (specifically showing the true constant is strictly smaller as q→∞). This supports the spirit of the conjecture that the binary (q=2) bound is not tight, but the paper's sharpest results are in the large-q regime; whether the full q=2 conjecture is resolved for all large n remains unclear from available abstracts.

 Cited literature (1)

 
 
 
partial Focal-free uniform hypergraphs and codes
 (2024)
 

 
 Xinqi Huang, Chong Shangguan, Xiande Zhang, Yuhao Zhao · arXiv preprint · arXiv:2410.23611

Proves asymptotically optimal bounds on focal-free codes, showing the Alon–Holzman multiplicative constant (r-1) is not tight (the true limit is strictly smaller), thereby confirming non-tightness of the upper bound; the sharpest explicit result concerns q→∞ rather than q=2 specifically.
 

 

 Reviewer notes. The 2024 paper arXiv:2410.23611 is the main follow-up and clearly improves the Alon–Holzman bound, establishing non-tightness in general via an asymptotic argument. However, the conjecture specifically targets q=2 (binary vectors) for large n; the most explicit result in the follow-up holds as q→∞, so it is not clear whether the binary case is fully settled. Status is therefore 'partial' rather than 'solved'.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. For $q = 2$ and large $n$, the upper bound $g^{q\text{-ff}}_r(n) \leq (r-1)\, q^{\lceil (r-2)n/(r-1) \rceil}$ of Theorem 1.3 is not tight.

Context

Proposition 3.2 shows via Reed-Solomon codes that the upper bound is essentially tight when $q \geq n$ and $q$ is a prime power. The authors believe the binary case ($q = 2$) behaves differently, and support this belief by proving in Section 4 that the bound can be significantly improved when the family of binary vectors forms a linear code (closed under addition modulo 2).

Notes. PDF source — math notation may be garbled.

Source paper

 Near-sunflowers and focal families
 Noga Alon, Ron Holzman · 2020-10-12
 https://arxiv.org/abs/2010.05992
 PDF source

=== Source paper abstract / header ===
Abstract:We present some problems and results about variants of sunflowers in families of sets. In particular, we improve an upper bound of the first author, Körner and Monti on the maximum number of binary vectors of length $n$ so that every four of them are split into two pairs by some coordinate. We also propose a weaker version of the Erdős-Rado sunflower conjecture.
 

 
 
 
 Comments:
 11 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05D05 (Primary), 05D40 (Secondary)
 

 Cite as:
 arXiv:2010.05992 [math.CO]
 

 
  
 (or 
 arXiv:2010.05992v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2010.05992
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Ron Holzman [view email] 
 [v1]
 Mon, 12 Oct 2020 19:41:05 UTC (11 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Near-sunflowers and focal families, by Noga Alon and Ron Holzman
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
 | 2020-10
 

 Change to browse by:
 
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 
 
 1 blog link
 (what is this?)
 

 

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
