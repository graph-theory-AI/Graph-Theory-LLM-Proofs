Attack the following open graph-theory problem.

Catalog id: 2601.12746__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2601.12746__00/
Source paper: When all directed cycles have the same weight (arXiv:2601.12746)

=== Extracted statement (catalog JSON) ===
Title: Open Question on Circular Drawing Characterisation
Is there a theorem that says ``every appropriately connected digraph $G$ contains no thing of type $X$ if and only if $G$ admits a circular drawing''?

Context:
Thomassen's theorem gives a characterisation of circular drawings in the presence of a specific 2-vertex separator. The authors generalise this into a motivating question and, despite fully characterising weightable digraphs in the paper, explicitly state: ``We still have not come up with the characterization we hoped for of the digraphs with circular drawings.''

=== Catalog page (statement + literature review) ===
Circular drawing characterization via forbidden type — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The paper by Berger, Carter, and Seymour (arXiv:2601.12746, January 2026) fully characterises weightable digraphs and derives a polynomial-time algorithm for testing weightability, but explicitly leaves open the question of whether there is a forbidden-structure characterisation of digraphs that admit a circular drawing. No follow-up work addressing this specific open question was found in the four months since posting.

 Reviewer notes. The source paper is very recent (January 2026). The open question asks for a Thomassen-style forbidden-substructure theorem that characterises circular drawings of sufficiently connected digraphs. The authors explicitly state they could not find such a characterisation despite fully resolving the weightability question. No follow-up was found after three targeted web searches.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Informal. Is there a theorem that says ``every appropriately connected digraph $G$ contains no thing of type $X$ if and only if $G$ admits a circular drawing''?

Context

Thomassen's theorem gives a characterisation of circular drawings in the presence of a specific 2-vertex separator. The authors generalise this into a motivating question and, despite fully characterising weightable digraphs in the paper, explicitly state: ``We still have not come up with the characterization we hoped for of the digraphs with circular drawings.''

Notes. No labelled theorem environment; stated as a motivating open question in the introduction and explicitly left unresolved at the end of the introductory discussion.

Source paper

 When all directed cycles have the same weight
 Eli Berger, Daniel Carter, Paul Seymour · 2026-01-19
 https://arxiv.org/abs/2601.12746
 PDF source

=== Source paper abstract / header ===
Abstract:A digraph $G$ is weightable if its edges can be weighted with real numbers such that the total weight in each directed cycle equals 1. There are several equivalent conditions: that $G$ admits a 0/1-weighting with the same property, or that $G$ contains no subdivided "double-cycle" as a subdigraph, or that for every triple of vertices, all directed cycles containing all three pass through them in the same cyclic order. And there is quite a rich supply of such digraphs: for instance, any digraph drawn in the plane such that each of its directed cycles rotates clockwise around the origin is weightable (let us call such digraphs "circular"), and there are weightable planar digraphs with much more complicated structure than this.
Until now the general structure of weightable digraphs was not known, and that is our objective in this paper. We will show that:
- there is a construction that builds every planar weightable digraph from circular digraphs; and
- there is a (different) construction that builds every weightable digraph from planar ones.
We derive a poly-time algorithm to test if a digraph is weightable.
 

 
 
 
 Comments:
 43 pages, 23 figures
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C20 (Primary), 05C75, 05C22, 05C85 (Secondary)
 

 Cite as:
 arXiv:2601.12746 [math.CO]
 

 
  
 (or 
 arXiv:2601.12746v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2601.12746
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Daniel Carter [view email] 
 [v1]
 Mon, 19 Jan 2026 05:59:12 UTC (44 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled When all directed cycles have the same weight, by Eli Berger and 2 other authors
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
 | 2026-01
 

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
