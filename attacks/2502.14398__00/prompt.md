Attack the following open graph-theory problem.

Catalog id: 2502.14398__00
Catalog status: partial (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2502.14398__00/
Source paper: Circular sorting (arXiv:2502.14398)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 3.4
$t(n)=n-2$ if and only if $n$ is prime.

Context:
The function $t(n)$ denotes the diameter of the swap graph on cyclic permutations when all swaps (not necessarily adjacent) are allowed. Observation 3.1 and Proposition 3.2 together establish that the condition holds whenever $n=2$ or $n$ is an odd prime, providing one direction of the biconditional.

=== Catalog page (statement + literature review) ===
Primality characterization of cyclic swap diameter — Graph-theory open problems (arXiv)

 
 Status
 partial
 high confidence
 

 Conjecture 3.4 asserts t(n)=n-2 iff n is prime; the source paper establishes the forward direction (n prime implies t(n)=n-2). A November 2025 follow-up (arXiv:2510.18529) proves the converse direction t(n)≤n-3 for all composite n divisible by 2 or 3, and for composite n whose permutations admit a polynomial representation over Z_n, giving a tight bound t(3p)=3p-3 for primes p. The conjecture remains open for composite n not divisible by 2 or 3 (e.g., n=25, 35, 49).

 Cited literature (1)

 
 
 
partial Circular sorting, strong complete mappings and wreath product constructions
 (2025)
 

 
 Paul Bastide, Anurag Bishnoi, Carla Groenland, Dion Gijswijt, Rohinee Joshi · arXiv preprint · arXiv:2510.18529

Proves t(n)≤n-3 for all composite n divisible by 2 or 3, and for composite n admitting permutation polynomials; establishes the tight bound t(3p)=3p-3 for primes p; the full conjecture remains open for composite n coprime to 6.
 

 

 Reviewer notes. Paper 2601.12597 (Adin, Bagno, Roichman, Jan 2026) concerns a Schreier graph under adjacent transpositions, not the all-swaps setting of Conjecture 3.4, and is not directly relevant. A secondary conjecture in the source paper (that t([pi])=n-2 forces pi to be affine) was disproved by 2510.18529 via non-affine quadratic orthomorphisms for n=23.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. $t(n)=n-2$ if and only if $n$ is prime.

Context

The function $t(n)$ denotes the diameter of the swap graph on cyclic permutations when all swaps (not necessarily adjacent) are allowed. Observation 3.1 and Proposition 3.2 together establish that the condition holds whenever $n=2$ or $n$ is an odd prime, providing one direction of the biconditional.

Source paper

 Circular sorting
 Ron M. Adin, Noga Alon, Yuval Roichman · 2025-08-06
 https://arxiv.org/abs/2502.14398

=== Source paper abstract / header ===
Abstract:We determine the maximal number of steps required to sort $n$ labeled points on a circle by adjacent swaps. Lower bounds for sorting by all swaps, not necessarily adjacent, are given as well.
 

 
 
 
 Comments:
 16 pages, minor changes, one reference added. To appear in the Israel Journal of Mathematics
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05A05, 68P10
 

 Cite as:
 arXiv:2502.14398 [math.CO]
 

 
  
 (or 
 arXiv:2502.14398v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2502.14398
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Ron M. Adin [view email] 
 [v1]
 Thu, 20 Feb 2025 09:35:54 UTC (19 KB)

 [v2]
 Wed, 6 Aug 2025 17:49:39 UTC (20 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Circular sorting, by Ron M. Adin and 1 other authors
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
 | 2025-02
 

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
