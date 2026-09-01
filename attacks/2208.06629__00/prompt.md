Attack the following open graph-theory problem.

Catalog id: 2208.06629__00
Catalog status: partial (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2208.06629__00/
Source paper: Perfect shuffling with fewer lazy transpositions (arXiv:2208.06629)

=== Extracted statement (catalog JSON) ===
Title: Problem 3
Does $U_t(n) = tn - \binom{t+1}{2}$?

Context:
This generalises Problem 1 to the setting of shuffling $t$ distinguishable counters across $n$ positions using the fewest lazy transpositions. The upper bound $U_t(n)\leq tn-\binom{t+1}{2}$ is achieved by existing sweeping/divide-and-conquer constructions. When $t=n$ the problem reduces to Problem 1, which Theorem 2 answers negatively; the paper asks whether the trivial bound is tight for other values of $t$.

=== Catalog page (statement + literature review) ===
Exact formula for U_t(n) lazy transpositions — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Problem 3 asks whether U_t(n) = tn - C(t+1,2) holds for all t, where the upper bound is already established by sweeping/divide-and-conquer constructions and the t=n case is answered negatively by Theorem 2 of the source paper. A follow-up by Janzer, Johnson, and Leader (arXiv:2210.13286, October 2022) proves that U_2(n) = 2n-3, confirming the formula for t=2 and settling the corresponding conjecture of Groenland et al. Whether the formula holds for intermediate values of t remains open.

 Cited literature (1)

 
 
 
partial Partial Shuffles by Lazy Swaps
 (2022)
 

 
 Barnabas Janzer, Robert Johnson, Imre Leader · arXiv preprint · arXiv:2210.13286

Proves U_2(n) = 2n-3, confirming the t=2 case of Problem 3 (since 2n-3 = 2n - C(3,2)) and explicitly settling a conjecture of Groenland, Johnston, Radcliffe, and Scott.
 

 

 Reviewer notes. The formula U_t(n) = tn - C(t+1,2) is confirmed for t=2 by Janzer et al. (arXiv:2210.13286); the case t=n is answered negatively in the source paper itself (Theorem 2). The general problem for intermediate t remains open. Confidence is medium because the Janzer et al. abstract was verified but the full paper was not read to confirm exact scope.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Does $U_t(n) = tn - \binom{t+1}{2}$?

Context

This generalises Problem 1 to the setting of shuffling $t$ distinguishable counters across $n$ positions using the fewest lazy transpositions. The upper bound $U_t(n)\leq tn-\binom{t+1}{2}$ is achieved by existing sweeping/divide-and-conquer constructions. When $t=n$ the problem reduces to Problem 1, which Theorem 2 answers negatively; the paper asks whether the trivial bound is tight for other values of $t$.

Notes. PDF source — binomial-coefficient notation garbled in raw extraction; LaTeX reconstructed from context. The paper also proves (Theorem 4) that for $3\leq t\leq n$ the bound can likewise be beaten by a constant factor, so the answer is negative for all $t\geq 3$.

Source paper

 Perfect shuffling with fewer lazy transpositions
 Carla Groenland, Tom Johnston, Jamie Radcliffe, Alex Scott · 2022-08-13
 https://arxiv.org/abs/2208.06629
 PDF source

=== Source paper abstract / header ===
Abstract:A lazy transposition $(a,b,p)$ is the random permutation that equals the identity with probability $1-p$ and the transposition $(a,b)\in S_n$ with probability $p$. How long must a sequence of independent lazy transpositions be if their composition is uniformly distributed? It is known that there are sequences of length $\binom{n}2$, but are there shorter sequences? This was raised by Fitzsimons in 2011, and independently by Angel and Holroyd in 2018. We answer this question negatively by giving a construction of length $\frac23 \binom{n}2+O(n\log n)$, and consider some related questions.
 

 
 
 
 Comments:
 23 pages, 5 figures, 1 table
 

 Subjects:
 
 Combinatorics (math.CO); Probability (math.PR)
 

 Cite as:
 arXiv:2208.06629 [math.CO]
 

 
  
 (or 
 arXiv:2208.06629v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2208.06629
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Tom Johnston [view email] 
 [v1]
 Sat, 13 Aug 2022 11:24:27 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Perfect shuffling with fewer lazy transpositions, by Carla Groenland and 3 other authors
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
 | 2022-08
 

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
