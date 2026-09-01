Attack the following open graph-theory problem.

Catalog id: 1606.06810__00
Catalog status: open (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1606.06810__00/
Source paper: On the number of cliques in graphs with a forbidden subdivision or imme… (arXiv:1606.06810)

=== Extracted statement (catalog JSON) ===
Title: Conjecture on maximum cliques with no $K_t$-immersion
The maximum number of cliques in a graph on $n \geq t-2$ vertices with no $K_t$-immersion is $2^{t-2}(n-t+3)$.

Context:
The authors construct a graph on $n$ vertices with no weak $K_t$-immersion achieving $2^{t-2}(n-t+3)$ cliques: begin with a clique $K$ on $t-2$ vertices and attach $n-t+2$ additional vertices each with neighborhood $K$. Since every vertex outside $K$ has degree $t-2 < t-1$, no $K_t$-immersion exists. The authors conjecture this construction is optimal.

=== Catalog page (statement + literature review) ===
Clique count bound for Kₜ-immersion-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Fox and Wei construct a graph achieving $2^{t-2}(n-t+3)$ cliques with no $K_t$-immersion (take $K_{t-2}$ and attach $n-t+2$ universal vertices over it), and conjecture this is optimal. Their paper proves an upper bound of $2^{t+\log^2 t}n$, which falls short of the conjectured exact value by a factor of $2^{O(\log^2 t)}$. No follow-up paper proving or disproving the sharp bound was found in an exhaustive web search as of May 2026.

 Reviewer notes. The Fox-Wei paper proves an upper bound of $2^{t+\log^2 t}n$ cliques for $K_t$-immersion-free graphs (Theorem 1.3), which is sharp up to a $2^{O(\log^2 t)}$ factor. The conjecture asks for the exact extremal value $2^{t-2}(n-t+3)$, a linear function in $n$ with leading coefficient $2^{t-2}$. No published or arXiv paper resolving this sharp form was found in five web searches.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. The maximum number of cliques in a graph on $n \geq t-2$ vertices with no $K_t$-immersion is $2^{t-2}(n-t+3)$.

Context

The authors construct a graph on $n$ vertices with no weak $K_t$-immersion achieving $2^{t-2}(n-t+3)$ cliques: begin with a clique $K$ on $t-2$ vertices and attach $n-t+2$ additional vertices each with neighborhood $K$. Since every vertex outside $K$ has degree $t-2 < t-1$, no $K_t$-immersion exists. The authors conjecture this construction is optimal.

Notes. PDF source — stated in running prose in the introduction without a labeled conjecture environment; math notation garbled in extraction and reconstructed.

Source paper

 On the number of cliques in graphs with a forbidden subdivision or immersion
 Jacob Fox, Fan Wei · 2018-08-07
 https://arxiv.org/abs/1606.06810
 PDF source

=== Source paper abstract / header ===
Abstract:How many cliques can a graph on $n$ vertices have with a forbidden substructure? Extremal problems of this sort have been studied for a long time. This paper studies the maximum possible number of cliques in a graph on $n$ vertices with a forbidden clique subdivision or immersion. We prove for $t$ sufficiently large that every graph on $n \geq t$ vertices with no $K_t$-immersion has at most $2^{t+\log^2 t}n$ cliques, which is sharp apart from the $2^{O(\log^2 t)}$ factor. We also prove that the maximum number of cliques in an $n$-vertex graph with no $K_t$-subdivision is at most $2^{1.817t}n$. This improves on the best known exponential constant by Lee and Oum. We conjecture that the optimal bound is $3^{2t/3 +o(t)}n$, as we proved for minors in place of subdivision in earlier work.
 

 
 
 
 Comments:
 16 pages of main text, 6 pages of appendix
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1606.06810 [math.CO]
 

 
  
 (or 
 arXiv:1606.06810v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1606.06810
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Fan Wei [view email] 
 [v1]
 Wed, 22 Jun 2016 03:25:17 UTC (21 KB)

 [v2]
 Tue, 7 Aug 2018 18:24:14 UTC (79 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled On the number of cliques in graphs with a forbidden subdivision or immersion, by Jacob Fox and 1 other authors
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
 | 2016-06
 

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
