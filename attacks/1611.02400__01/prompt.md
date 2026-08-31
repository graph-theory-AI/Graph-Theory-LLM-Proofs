Attack the following open graph-theory problem.

Catalog id: 1611.02400__01
Catalog status: open (triage tier 2, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1611.02400__01/
Source paper: A Graph-Theoretic Approach to Multitasking (arXiv:1611.02400)

=== Catalog page (statement + literature review) ===
Multitasker threshold at average degree log n — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No paper resolving the open problem has been found. The follow-up work arXiv:1809.02835 (Multitasking Capacity: Hardness Results and Improved Constructions, published in SIAM J. Discrete Math.) proves hardness of approximation results and provides improved constructions achieving $\alpha = 1/2 - \varepsilon$ for matchings of size $n/\mathrm{poly}(d)$, but does not construct multitaskers with $\alpha > 0$ independent of $n$ at average degree $\Theta(\log n)$. The specific threshold question — whether $\Theta(\log n)$ average degree suffices for constant $\alpha$ — remains open as of the search date.

 Cited literature (1)

 
 
 
partial Multitasking Capacity: Hardness Results and Improved Constructions
 (2018)
 

 
 Noga Alon, Jonathan D. Cohen, Biswadip Dey, Tom Griffiths, Sebastian Musslick, Kayhan Ozcimder, Daniel Reichman, Igor Shinkar, Tal Wagner · arXiv preprint (published in SIAM Journal on Discrete Mathematics) · arXiv:1809.02835

Proves computational hardness for approximating multitasking capacity and gives improved constructions achieving $\alpha = 1/2 - \varepsilon$ for matchings of size $n/\mathrm{poly}(d)$, but does not resolve the $\Theta(\log n)$ average-degree threshold question.
 

 

 Reviewer notes. The main follow-up paper arXiv:1809.02835 was verified via WebFetch; it improves constructions and proves hardness but does not address the specific open problem about $\Theta(\log n)$ average degree. No other paper specifically resolving this threshold question was found in the search.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. It is an interesting question whether there exists a multitasker with $\alpha > 0$ independent of $n$, for average degree $\Theta(\log n)$, which, if true is the largest average degree possible. This is left as an open problem.

Context

The paper shows there exist multitaskers of average degree $\Omega(\log\log n)$ with $\alpha > 1/3 - \varepsilon$, and that for the multitasking capacity to decay with average degree $d$ one must assume $d$ grows faster than $\log\log n$. The question is whether the threshold can be pushed up to $\Theta(\log n)$.

Notes. Statement appears in running prose without a labelled environment; PDF source.

Source paper

 A Graph-Theoretic Approach to Multitasking
 Noga Alon, Jonathan D. Cohen, Biswadip Dey, Tom Griffiths, Sebastian Musslick, Kayhan Ozcimder, Daniel Reichman, Igor Shinkar, Tal Wagner · 2017-06-09
 https://arxiv.org/abs/1611.02400
 PDF source

=== Source paper abstract / header ===
Abstract:A key feature of neural network architectures is their ability to support the simultaneous interaction among large numbers of units in the learning and processing of representations. However, how the richness of such interactions trades off against the ability of a network to simultaneously carry out multiple independent processes -- a salient limitation in many domains of human cognition -- remains largely unexplored. In this paper we use a graph-theoretic analysis of network architecture to address this question, where tasks are represented as edges in a bipartite graph $G=(A \cup B, E)$. We define a new measure of multitasking capacity of such networks, based on the assumptions that tasks that \emph{need} to be multitasked rely on independent resources, i.e., form a matching, and that tasks \emph{can} be multitasked without interference if they form an induced matching. Our main result is an inherent tradeoff between the multitasking capacity and the average degree of the network that holds \emph{regardless of the network architecture}. These results are also extended to networks of depth greater than $2$. On the positive side, we demonstrate that networks that are random-like (e.g., locally sparse) can have desirable multitasking properties. Our results shed light into the parallel-processing limitations of neural systems and provide insights that may be useful for the analysis and design of parallel architectures.
 

 
 
 
 Subjects:
 
 Discrete Mathematics (cs.DM)
 

 Cite as:
 arXiv:1611.02400 [cs.DM]
 

 
  
 (or 
 arXiv:1611.02400v2 [cs.DM] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1611.02400
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Daniel Reichman [view email] 
 [v1]
 Tue, 8 Nov 2016 06:06:36 UTC (35 KB)

 [v2]
 Fri, 9 Jun 2017 15:57:19 UTC (35 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled A Graph-Theoretic Approach to Multitasking, by Noga Alon and Jonathan D. Cohen and Biswadip Dey and Tom Griffiths and Sebastian Musslick and Kayhan Ozcimder and Daniel Reichman and Igor Shinkar and Tal Wagner
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DM

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2016-11
 

 Change to browse by:
 
 cs
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Jonathan D. Cohen
Biswadip Dey
Tom Griffiths
Sebastian Musslick
Kayhan Özcimder …

 

 

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
