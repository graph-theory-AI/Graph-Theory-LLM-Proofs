Attack the following open graph-theory problem.

Catalog id: 2005.09767__00
Catalog status: open (triage tier 3, lean balanced)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2005.09767__00/
Source paper: Many flows in the group connectivity setting (arXiv:2005.09767)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 1.10
There exists a fixed constant $c > 1$ so that the following holds. For every 3-edge-connected oriented graph $G = (V, E)$ of order $n$, every abelian group $\Gamma$ with $|\Gamma| \geq 6$, and every $f : E \to \Gamma$, there exist at least $c^n$ flows $\phi : E \to \Gamma$ with $\phi(e) \neq f(e)$ for every $e \in E$.

Context:
Theorem 1.9 establishes an explicit exponential lower bound on the number of $\Gamma$-connected flows for groups of size $k \geq 8$, but yields only the existence of a single flow for $k = 6, 7$. The authors attribute this gap to a shortcoming of their techniques and conjecture the exponential bound holds for all abelian groups of size at least 6. Theorem 1.9 confirms the conjecture for all groups except $\mathbb{Z}_6$ and $\mathbb{Z}_7$; Theorem 1.11 gives a superpolynomial (but not exponential) lower bound for $\mathbb{Z}_6$.

=== Catalog page (statement + literature review) ===
Exponential flows in 3-edge-connected oriented graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 1.10 from arXiv:2005.09767 asserts an exponential lower bound $c^n$ on the number of $\Gamma$-connected flows for every abelian group $\Gamma$ with $|\Gamma| \geq 6$. The source paper itself proves this for all groups of size $\geq 8$ (Theorem 1.9) and establishes only a superpolynomial (but sub-exponential) bound for $\mathbb{Z}_6$ (Theorem 1.11), leaving $\mathbb{Z}_6$ and $\mathbb{Z}_7$ open. No subsequent paper resolving the conjecture for these two groups was found in five targeted web searches across the literature through May 2026; the paper remains at a single arXiv version with no revision signalling a resolution.

 Reviewer notes. No follow-up paper resolving the conjecture for |Γ| = 6 or 7 was found. The conjecture is roughly 6 years old as of the review date, which is long enough that absence of evidence is somewhat suspicious but the two open cases (Z_6 and Z_7) are notoriously hard; confidence is set to medium rather than high. The sole internal reference candidate (2409.18220) was a false positive on the fuzz match.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. There exists a fixed constant $c > 1$ so that the following holds. For every 3-edge-connected oriented graph $G = (V, E)$ of order $n$, every abelian group $\Gamma$ with $|\Gamma| \geq 6$, and every $f : E \to \Gamma$, there exist at least $c^n$ flows $\phi : E \to \Gamma$ with $\phi(e) \neq f(e)$ for every $e \in E$.

Context

Theorem 1.9 establishes an explicit exponential lower bound on the number of $\Gamma$-connected flows for groups of size $k \geq 8$, but yields only the existence of a single flow for $k = 6, 7$. The authors attribute this gap to a shortcoming of their techniques and conjecture the exponential bound holds for all abelian groups of size at least 6. Theorem 1.9 confirms the conjecture for all groups except $\mathbb{Z}_6$ and $\mathbb{Z}_7$; Theorem 1.11 gives a superpolynomial (but not exponential) lower bound for $\mathbb{Z}_6$.

Source paper

 Many flows in the group connectivity setting
 Matt DeVos, Rikke Langhede, Bojan Mohar, Robert Šámal · 2020-05-19
 https://arxiv.org/abs/2005.09767
 PDF source

=== Source paper abstract / header ===
Abstract:Two well-known results in the world of nowhere-zero flows are Jaeger's 4-flow theorem asserting that every 4-edge-connected graph has a nowhere-zero $\mathbb{Z}_2 \times \mathbb{Z}_2$-flow and Seymour's 6-flow theorem asserting that every 2-edge-connected graph has a nowhere-zero $\mathbb{Z}_6$-flow. Dvořák and the last two authors of this paper extended these results by proving the existence of exponentially many nowhere-zero flows under the same assumptions. We revisit this setting and provide extensions and simpler proofs of these results.
The concept of a nowhere-zero flow was extended in a significant paper of Jaeger, Linial, Payan, and Tarsi to a choosability-type setting. For a fixed abelian group $\Gamma$, an oriented graph $G = (V,E)$ is called $\Gamma$-connected if for every function $f : E \rightarrow \Gamma$ there is a flow $\phi : E \rightarrow \Gamma$ with $\phi(e) \neq f(e)$ for every $e \in E$ (note that taking $f = 0$ forces $\phi$ to be nowhere-zero). Jaeger et al. proved that every oriented 3-edge-connected graph is $\Gamma$-connected whenever $|\Gamma| \ge 6$. We prove that there are exponentially many solutions whenever $|\Gamma| \ge 8$. For the group $\mathbb{Z}_6$ we prove that for every oriented 3-edge-connected $G = (V,E)$ with $\ell = |E| - |V| \ge 11$ and every $f: E \rightarrow \mathbb{Z}_6$, there are at least $2^{ \sqrt{\ell} / \log \ell}$ flows $\phi$ with $\phi(e) \neq f(e)$ for every $e \in E$.
 

 
 
 
 Comments:
 19 pages
 

 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C21, 05C30
 

 Cite as:
 arXiv:2005.09767 [math.CO]
 

 
  
 (or 
 arXiv:2005.09767v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2005.09767
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Robert Šámal [view email] 
 [v1]
 Tue, 19 May 2020 21:44:20 UTC (21 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Many flows in the group connectivity setting, by Matt DeVos and 3 other authors
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
 | 2020-05
 

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
