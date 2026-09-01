Attack the following open graph-theory problem.

Catalog id: 2101.03537__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2101.03537__00/
Source paper: Pure pairs. VII. Homogeneous submatrices in 0/1-matrices with a forbidd… (arXiv:2101.03537)

=== Extracted statement (catalog JSON) ===
Title: Informal belief on Conjecture 1.7 and polylog bound
Our guess is that Conjecture 1.7 is false. Perhaps $n/\operatorname{polylog}(n)$ might be true?

Context:
After stating Conjecture 1.7, the authors remark that while it is a natural extension of the unordered theory, they do not believe it holds, and informally suggest that a bound of $n/\operatorname{polylog}(n)$ for the sizes of the pure pair might be the correct weaker conclusion.

=== Catalog page (statement + literature review) ===
n/polylog(n) bound for ordered pure pairs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 1.7 (due to Korándi, Pach, and Tomon) asserts that $f_H(n)$ is linear in $n$ for every acyclic matrix $H$. Scott, Seymour, and Spirkl informally believe this conjecture is false and suggest $n/\operatorname{polylog}(n)$ as a plausible correct bound; their paper establishes the weaker result $f_H(n) = n^{1-o(1)}$ for every acyclic $H$. No subsequent work found in the indexed literature has resolved either Conjecture 1.7 or the informal $n/\operatorname{polylog}(n)$ belief.

 Reviewer notes. Conjecture 1.7 is by Korándi, Pach, and Tomon (linear bound for $f_H(n)$ for every acyclic $H$). The informal belief reviewed here is the authors' meta-conjecture that 1.7 is false and $n/\operatorname{polylog}(n)$ is the right bound. The source paper itself proves $f_H(n)=n^{1-o(1)}$, which is an intermediate result. No follow-up paper was found in the indexed literature resolving either question. Confidence is medium rather than high because the conjecture is now 4+ years old and absence of follow-up may reflect difficulty rather than lack of activity.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Our guess is that Conjecture 1.7 is false. Perhaps $n/\operatorname{polylog}(n)$ might be true?

Context

After stating Conjecture 1.7, the authors remark that while it is a natural extension of the unordered theory, they do not believe it holds, and informally suggest that a bound of $n/\operatorname{polylog}(n)$ for the sizes of the pure pair might be the correct weaker conclusion.

Notes. Stated as an informal belief/guess in running prose; no labelled theorem environment.

Source paper

 Pure pairs. VII. Homogeneous submatrices in 0/1-matrices with a forbidden submatrix
 Alex Scott, Paul Seymour, Sophie Spirkl · 2021-01-10
 https://arxiv.org/abs/2101.03537
 PDF source

=== Source paper abstract / header ===
Abstract:For integer $n>0$, let $f(n)$ be the number of rows of the largest all-0 or all-1 square submatrix of $M$, minimized over all $n\times n$ $0/1$-matrices $M$. Thus $f(n)= O(\log n)$. But let us fix a matrix $H$, and define $f_H(n)$ to be the same, minimized over over all $n\times n$ $0/1$-matrices $M$ such that neither $M$ nor its complement (that is, change all $0$'s to $1$'s and vice versa) contains $H$ as a submatrix. It is known that $f_H(n)\ge \epsilon n^c$, where $c, \epsilon>0$ are constants depending on $H$. When can we take $c=1$? If so, then one of $H$ and its complement must be an acyclic matrix (that is, the corresponding bipartite graph is a forest). Korandi, Pach, and Tomon conjectured the converse, that $f_H(n)$ is linear in $n$ for every acyclic matrix $H$; and they proved it for certain matrices $H$ with only two rows.
Their conjecture remains open, but we show $f_H(n)=n^{1-o(1)}$ for every acyclic matrix $H$; and indeed there is a $0/1$-submatrix that is either $\Omega(n)\times n^{1-o(1)}$ or $n^{1-o(1)}\times \Omega(n)$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2101.03537 [math.CO]
 

 
  
 (or 
 arXiv:2101.03537v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2101.03537
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Alexander Scott [view email] 
 [v1]
 Sun, 10 Jan 2021 12:54:26 UTC (20 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Pure pairs. VII. Homogeneous submatrices in 0/1-matrices with a forbidden submatrix, by Alex Scott and 2 other authors
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
 | 2021-01
 

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
