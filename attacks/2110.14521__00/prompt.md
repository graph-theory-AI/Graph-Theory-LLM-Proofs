Attack the following open graph-theory problem.

Catalog id: 2110.14521__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2110.14521__00/
Source paper: Active clustering for labeling training data (arXiv:2110.14521)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 5
For an $n$-set with a random partition with probabilities $p_1, p_2, \ldots, p_k$, the clique algorithm has minimal average complexity among all AC algorithms.

Context:
In the model where each of $n$ items independently belongs to class $C_i$ with probability $p_i$ (with $p_1 \geq p_2 \geq \cdots \geq p_k$), the authors argue that an optimal algorithm should compare each new element first to the largest identified class. The clique algorithm does exactly this, comparing each new item to blocks in decreasing order of size. The conjecture is stated directly before Theorem 6, which characterises the asymptotic expected query count of the clique algorithm as $\sum_{i=1}^k i p_i n$, offered as supporting evidence.

=== Catalog page (statement + literature review) ===
Clique algorithm optimality in active clustering — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 5 of arXiv:2110.14521 asserts that among all active clustering (AC) algorithms, the clique algorithm achieves minimal average query complexity when items are assigned to classes independently with fixed probabilities p_1 >= p_2 >= ... >= p_k. The paper itself provides Theorem 6 as supporting evidence, showing the clique algorithm's asymptotic expected query count equals sum_{i=1}^k i*p_i*n. A search of citing literature (via Semantic Scholar) yields six citing papers as of May 2026, none of which address this conjecture; the conjecture appears to remain open.

 Reviewer notes. Semantic Scholar lists 6 citing papers (as of May 2026): Bastide & Groenland 2025 (distance query reconstruction), A3S 2024 (arXiv:2407.10196, general active clustering), Bastide & Groenland 2023 (arXiv:2306.05979), a handwriting paper, a deep constrained clustering paper, and a lexicographic unranking paper. None of these appears to address Conjecture 5. The conjecture is recent (NeurIPS 2021) and highly specific to the probabilistic AC model; no follow-up was found in the indexed literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For an $n$-set with a random partition with probabilities $p_1, p_2, \ldots, p_k$, the clique algorithm has minimal average complexity among all AC algorithms.

Context

In the model where each of $n$ items independently belongs to class $C_i$ with probability $p_i$ (with $p_1 \geq p_2 \geq \cdots \geq p_k$), the authors argue that an optimal algorithm should compare each new element first to the largest identified class. The clique algorithm does exactly this, comparing each new item to blocks in decreasing order of size. The conjecture is stated directly before Theorem 6, which characterises the asymptotic expected query count of the clique algorithm as $\sum_{i=1}^k i p_i n$, offered as supporting evidence.

Source paper

 Active clustering for labeling training data
 Quentin Lutz, Élie de Panafieu, Alex Scott, Maya Stein · 2021-10-27
 https://arxiv.org/abs/2110.14521
 PDF source

=== Source paper abstract / header ===
Abstract:Gathering training data is a key step of any supervised learning task, and it is both critical and expensive. Critical, because the quantity and quality of the training data has a high impact on the performance of the learned function. Expensive, because most practical cases rely on humans-in-the-loop to label the data. The process of determining the correct labels is much more expensive than comparing two items to see whether they belong to the same class. Thus motivated, we propose a setting for training data gathering where the human experts perform the comparatively cheap task of answering pairwise queries, and the computer groups the items into classes (which can be labeled cheaply at the very end of the process). Given the items, we consider two random models for the classes: one where the set partition they form is drawn uniformly, the other one where each item chooses its class independently following a fixed distribution. In the first model, we characterize the algorithms that minimize the average number of queries required to cluster the items and analyze their complexity. In the second model, we analyze a specific algorithm family, propose as a conjecture that they reach the minimum average number of queries and compare their performance to a random approach. We also propose solutions to handle errors or inconsistencies in the experts' answers.
 

 
 
 
 Comments:
 Accepted at Neurips 2021. The main part is 14 pages long, the rest is an appendix containing the long version of the proofs
 

 Subjects:
 
 Data Structures and Algorithms (cs.DS); Artificial Intelligence (cs.AI); Discrete Mathematics (cs.DM); Combinatorics (math.CO)
 

 Cite as:
 arXiv:2110.14521 [cs.DS]
 

 
  
 (or 
 arXiv:2110.14521v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2110.14521
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 NeurIPS 2021
 

 

 

 
 Submission history
 From: Elie de Panafieu [view email] 
 [v1]
 Wed, 27 Oct 2021 15:35:58 UTC (114 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Active clustering for labeling training data, by Quentin Lutz and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 
 
 view license
 

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2021-10
 

 Change to browse by:
 
 cs
 cs.AI
 cs.DM
 math
 math.CO
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Alex Scott
Maya Stein 

 

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
