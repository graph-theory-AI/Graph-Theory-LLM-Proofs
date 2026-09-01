Attack the following open graph-theory problem.

Catalog id: 2410.13008__01
Catalog status: partial (triage tier 4, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2410.13008__01/
Source paper: When all directed cycles have length three (arXiv:2410.13008)

=== Extracted statement (catalog JSON) ===
Title: Informal Question (NP-characterization of weightable digraphs)
Can we give a construction for all weightable digraphs (i.e., an NP-characterization)?

Context:
A digraph $G$ is weightable if one can assign a real weight $w(e)$ to each edge $e$ such that $\sum_{e\in E(C)}w(e)=1$ for each directed cycle $C$. The paper shows weightability is characterizable by excluded subdigraphs (giving a co-NP characterization), but an NP-characterization via explicit construction remains open. For strongly 2-connected digraphs, Conjecture 1.2 would provide such a construction.

=== Catalog page (statement + literature review) ===
NP-characterization of weightable digraphs — Graph-theory open problems (arXiv)

 
 Status
 partial
 medium confidence
 

 Berger, Carter, and Seymour (arXiv:2601.12746, 2026) provide two hierarchical constructions: one that builds every planar weightable digraph from circular digraphs, and one that builds every weightable digraph from planar ones. Together these yield a structural construction for all weightable digraphs, substantially addressing the informal question, alongside a poly-time algorithm to test weightability. Whether this constitutes a full NP-characterization in the formal complexity sense (a polynomial-time verifiable certificate) is not explicitly confirmed in the abstract.

 Cited literature (1)

 
 
 
partial When all directed cycles have the same weight
 (2026)
 

 
 Eli Berger, Daniel Carter, Paul Seymour · arXiv preprint · arXiv:2601.12746

Provides forbidden-subgraph characterization of weightable digraphs, a construction building every planar weightable digraph from circular digraphs, a construction building every weightable digraph from planar ones, and a poly-time algorithm to test weightability — collectively giving a structural construction for all weightable digraphs.
 

 

 Reviewer notes. The follow-up paper arXiv:2601.12746 is co-authored by Seymour himself (the author of 2410.13008), suggesting it directly continues this line of research. The two-step hierarchical construction (all weightable from planar, all planar from circular) provides the sought construction for all weightable digraphs. The poly-time algorithm for testing weightability further suggests the complexity question may be fully resolved (P membership). The formal NP-characterization framing of the original question may be moot given the polynomial-time decidability result.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Question. Can we give a construction for all weightable digraphs (i.e., an NP-characterization)?

Context

A digraph $G$ is weightable if one can assign a real weight $w(e)$ to each edge $e$ such that $\sum_{e\in E(C)}w(e)=1$ for each directed cycle $C$. The paper shows weightability is characterizable by excluded subdigraphs (giving a co-NP characterization), but an NP-characterization via explicit construction remains open. For strongly 2-connected digraphs, Conjecture 1.2 would provide such a construction.

Notes. Stated as prose question in the introduction without a labelled environment.

Source paper

 When all directed cycles have length three
 Paul Seymour · 2025-02-09
 https://arxiv.org/abs/2410.13008

=== Source paper abstract / header ===
Abstract:We give a construction to build all digraphs with the property that every directed cycle has length three.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C20
 

 Cite as:
 arXiv:2410.13008 [math.CO]
 

 
  
 (or 
 arXiv:2410.13008v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2410.13008
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Paul Seymour [view email] 
 [v1]
 Wed, 16 Oct 2024 20:07:30 UTC (14 KB)

 [v2]
 Sun, 9 Feb 2025 02:04:40 UTC (18 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled When all directed cycles have length three, by Paul Seymour
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
 | 2024-10
 

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
