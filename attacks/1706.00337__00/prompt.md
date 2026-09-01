Attack the following open graph-theory problem.

Catalog id: 1706.00337__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1706.00337__00/
Source paper: Triangle-free graphs of tree-width t are ceil((t + 3)/2)-colorable (arXiv:1706.00337)

=== Extracted statement (catalog JSON) ===
Title: Problem 3
For integers $k \geq 4$ and $t \geq k - 1$, what is the maximum chromatic number of $K_k$-free graphs of tree-width at most $t$?

Context:
Theorem 2 establishes that $g(t,k) > \bigl(1 - \frac{1}{2^{k-2}}\bigr)t$ for all $t \geq 0$ and $k \geq 2$, providing a lower bound on the maximum chromatic number. The case $k = 3$ (triangle-free) is completely resolved by Theorem 1, which gives the tight bound $\lceil(t+3)/2\rceil$, but the question remains open for $k \geq 4$.

=== Catalog page (statement + literature review) ===
Chromatic number of Kₖ-free bounded treewidth graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Problem 3 of Dvořák–Kawarabayashi (arXiv:1706.00337) asks for the exact maximum chromatic number of K_k-free graphs of tree-width at most t for k≥4, generalising their tight answer ⌈(t+3)/2⌉ for k=3. No paper fully resolving the question for any fixed k≥4 was found. A 2025 paper (Discrete Mathematics, ScienceDirect pii/S0012365X25001037) explicitly addresses the fractional version of the same question—the maximum fractional chromatic number of K_r-free partial t-trees—and may constitute partial progress, but the URL could not be verified (HTTP 403) so it is recorded only in the notes.

 Reviewer notes. No verified follow-up paper that resolves Problem 3 (k≥4) was found. A 2025 paper titled 'Fractional colorings of partial t-trees with no large clique' (Discrete Mathematics, https://www.sciencedirect.com/science/article/pii/S0012365X25001037) was identified via web search as explicitly addressing the Dvořák–Kawarabayashi question for the fractional chromatic number, but ScienceDirect returned HTTP 403 and no arxiv preprint was located, so it cannot be cited with verified coordinates. If this paper proves tight bounds for the fractional chromatic number of K_r-free partial t-trees, the status might be upgraded to 'partial'. The lower bound g(t,k) > (1 − 1/2^{k−2})t from the source paper remains the best published lower bound known. The problem is open for k≥4 with high probability.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. For integers $k \geq 4$ and $t \geq k - 1$, what is the maximum chromatic number of $K_k$-free graphs of tree-width at most $t$?

Context

Theorem 2 establishes that $g(t,k) > \bigl(1 - \frac{1}{2^{k-2}}\bigr)t$ for all $t \geq 0$ and $k \geq 2$, providing a lower bound on the maximum chromatic number. The case $k = 3$ (triangle-free) is completely resolved by Theorem 1, which gives the tight bound $\lceil(t+3)/2\rceil$, but the question remains open for $k \geq 4$.

Notes. PDF source — references section is garbled with a list of arXiv IDs; the problem statement itself is clearly legible

Source paper

 Triangle-free graphs of tree-width t are ceil((t + 3)/2)-colorable
 Zdeněk Dvořák, Ken-ichi Kawarabayashi · 2017-06-09
 https://arxiv.org/abs/1706.00337
 PDF source

=== Source paper abstract / header ===
Abstract:We prove that every triangle-free graph of tree-width t has chromatic number at most ceil((t + 3)/2), and demonstrate that this bound is tight. The argument also establishes a connection between coloring graphs of tree-width t and on-line coloring of graphs of path-width t.
 

 
 
 
 Comments:
 10 pages, no figures; updated according to referee suggestions
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C15
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:1706.00337 [math.CO]
 

 
  
 (or 
 arXiv:1706.00337v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1706.00337
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Zdenek Dvorak [view email] 
 [v1]
 Thu, 1 Jun 2017 15:16:51 UTC (8 KB)

 [v2]
 Fri, 9 Jun 2017 11:07:49 UTC (8 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Triangle-free graphs of tree-width t are ceil((t + 3)/2)-colorable, by Zden\v{e}k Dvo\v{r}\'ak and Ken-ichi Kawarabayashi
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
 | 2017-06
 

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
