Attack the following open graph-theory problem.

Catalog id: 1904.12273__02
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1904.12273__02/
Source paper: Detecting a long odd hole (arXiv:1904.12273)

=== Extracted statement (catalog JSON) ===
Title: Open Question (running time improvement for long hole detection)
Can the running times of $O(|G|^{\ell+1})$ for detecting a long hole and $O(|G|^{20\ell+40})$ for detecting a long odd hole — both $|G|^{O(\ell)}$ — be substantially improved for fixed $\ell$?

Context:
The paper gives algorithms with running time $|G|^{O(\ell)}$ for both long hole and long odd hole detection. Both problems are NP-hard when $\ell$ is part of the input, but whether the dependence on $\ell$ in the exponent can be reduced for fixed $\ell$ is left as an open question.

=== Catalog page (statement + literature review) ===
Fixed-ℓ long odd hole detection complexity — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No paper has substantially improved the $|G|^{O(\ell)}$ exponent for detecting long holes or long odd holes for fixed $\ell$. The closely related problem of detecting long even holes was addressed by Cook and Seymour (arXiv:2009.05691), who gave an $O(|G|^{9\ell+3})$ algorithm — still $|G|^{O(\ell)}$. Hardness results show W[1]-hardness when $\ell$ is part of the input, suggesting that eliminating the $\ell$-dependence from the exponent entirely is likely impossible under standard complexity assumptions, but the question of a substantially smaller polynomial degree for fixed $\ell$ remains open.

 Cited literature (1)

 
 
 
partial Detecting a long even hole
 (2020)
 

 
 Linda Cook, Paul Seymour · European Journal of Combinatorics (2022) · arXiv:2009.05691

Provides an $O(|G|^{9\ell+3})$ algorithm for detecting long even holes for fixed $\ell \geq 4$; a closely related variant that still runs in $|G|^{O(\ell)}$ time and does not resolve the running-time question for long holes or long odd holes.
 

 

 Reviewer notes. The open question asks whether the $|G|^{O(\ell)}$ dependence can be substantially improved for fixed $\ell$. Cook and Seymour 2020 (arXiv:2009.05691) provides adjacent progress for even holes at $O(|G|^{9\ell+3})$, still polynomial in the same sense. W[1]-hardness when $\ell$ is part of the input (established in the FPT literature) implies that a uniform algorithm simultaneously polynomial in both $|G|$ and $\ell$ is unlikely, but does not rule out a smaller polynomial degree for each fixed $\ell$. No direct improvement to the $O(|G|^{\ell+1})$ or $O(|G|^{20\ell+40})$ bounds was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Question. Can the running times of $O(|G|^{\ell+1})$ for detecting a long hole and $O(|G|^{20\ell+40})$ for detecting a long odd hole — both $|G|^{O(\ell)}$ — be substantially improved for fixed $\ell$?

Context

The paper gives algorithms with running time $|G|^{O(\ell)}$ for both long hole and long odd hole detection. Both problems are NP-hard when $\ell$ is part of the input, but whether the dependence on $\ell$ in the exponent can be reduced for fixed $\ell$ is left as an open question.

Notes. Stated as 'We do not know if either can be substantially improved.' No formal labelled environment.

Source paper

 Detecting a long odd hole
 Maria Chudnovsky, Alex Scott, Paul Seymour · 2020-09-06
 https://arxiv.org/abs/1904.12273
 PDF source

=== Source paper abstract / header ===
Abstract:For each integer $t\ge 5$, we give a polynomial-time algorithm to test whether a graph contains an induced cycle with length at least $t$ and odd.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1904.12273 [math.CO]
 

 
  
 (or 
 arXiv:1904.12273v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1904.12273
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Sun, 28 Apr 2019 07:58:02 UTC (21 KB)

 [v2]
 Sun, 6 Sep 2020 18:22:39 UTC (23 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Detecting a long odd hole, by Maria Chudnovsky and 2 other authors
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
 | 2019-04
 

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
