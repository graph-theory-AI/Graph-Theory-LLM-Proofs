Attack the following open graph-theory problem.

Catalog id: 2010.08988__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2010.08988__00/
Source paper: Even Circuits in Oriented Matroids (arXiv:2010.08988)

=== Extracted statement (catalog JSON) ===
Title: Problem 1.4
Given an oriented matroid $\vec{M}$, decide whether there exists a directed circuit of even size in $\vec{M}$.

Context:
This is the paper's straight-forward generalisation of the even dicycle problem from digraphs to oriented matroids, and constitutes the central algorithmic motivation of the work. The authors show in Theorem 1.6 that this problem is polynomially equivalent to recognising non-even oriented regular matroids.

=== Catalog page (statement + literature review) ===
Even directed circuit in oriented matroids — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 1.4 asks for a decision procedure for the existence of an even directed circuit in a general oriented matroid. The source paper (published in Combinatorial Theory 2022) shows via Theorem 1.6 that the problem is polynomially equivalent to recognising non-even oriented regular matroids, and provides a forbidden-minor characterisation for non-even oriented bond matroids; however, the general problem for arbitrary oriented matroids is shown to require super-polynomially many signed-circuit oracle calls, leaving its exact computational complexity open. No subsequent paper resolving Problem 1.4 in full generality was found in a targeted web search.

 Reviewer notes. The paper itself (Combinatorial Theory, vol. 2 no. 1, 2022) already provides partial resolution: for regular oriented matroids the problem reduces to non-even recognition, and odd directed circuits are detectable in polynomial time. For general oriented matroids the signed-circuit oracle lower bound rules out a polynomial oracle algorithm. The open question is whether a poly-time algorithm exists when the matroid is given by an explicit representation rather than an oracle. No follow-up found after five web calls.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Given an oriented matroid $\vec{M}$, decide whether there exists a directed circuit of even size in $\vec{M}$.

Context

This is the paper's straight-forward generalisation of the even dicycle problem from digraphs to oriented matroids, and constitutes the central algorithmic motivation of the work. The authors show in Theorem 1.6 that this problem is polynomially equivalent to recognising non-even oriented regular matroids.

Notes. PDF source; the statement is short and mathematically simple, so extraction is reliable.

Source paper

 Even Circuits in Oriented Matroids
 Karl Heuer, Raphael Steiner, Sebastian Wiederrecht · 2020-10-18
 https://arxiv.org/abs/2010.08988
 PDF source

=== Source paper abstract / header ===
Abstract:In this paper we generalise the even directed cycle problem, which asks whether a given digraph contains a directed cycle of even length, to orientations of regular matroids. We define non-even oriented matroids generalising non-even digraphs, which played a central role in resolving the computational complexity of the even dicycle problem. Then we show that the problem of detecting an even directed circuit in a regular matroid is polynomially equivalent to the recognition of non-even oriented matroids. Our main result is a precise characterisation of the class of non-even oriented bond matroids in terms of forbidden minors, which complements an existing characterisation of non-even oriented graphic matroids by Seymour and Thomassen.
 

 
 
 
 Comments:
 30 pages, no figures
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05B35, 05C20, 05C70, 05C75, 05C83, 05C85, 52C40
 

 Cite as:
 arXiv:2010.08988 [math.CO]
 

 
  
 (or 
 arXiv:2010.08988v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2010.08988
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Raphael Steiner [view email] 
 [v1]
 Sun, 18 Oct 2020 14:01:17 UTC (32 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Even Circuits in Oriented Matroids, by Karl Heuer and 2 other authors
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
