Attack the following open graph-theory problem.

Catalog id: simultaneous_partition_of_hypergraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Hypergraphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/simultaneous_partition_of_hypergraphs/
Original entry: http://www.openproblemgarden.org/op/simultaneous_partition_of_hypergraphs
Problem attributed to: Kühn, Daniella, Osthus, Deryk (posted 2013-03-06)

=== Problem statement (OpenProblemGarden) ===
Title: Simultaneous partition of hypergraphs
Problem Let $ H_1 $ and $ H_2 $ be two $ r $ -uniform hypergraph on the same vertex set $ V $ . Does there always exist a partition of $ V $ into $ r $ classes $ V_1, \dots , V_r $ such that for both $ i=1,2 $ , at least $ r!m_i/r^r -o(m_i) $ hyperedges of $ H_i $ meet each of the classes $ V_1, \dots , V_r $ ?

=== Discussion / context (OpenProblemGarden) ===
The bound on the number of hyperedges is what one would expect for a random partition. For graphs, the question was answered in the affirmative in [KO]. Keevash and Sudakov observed that the answer is negative if we consider many hypergraphs instead of just 2 (see [KO] for the example).

=== References listed by OpenProblemGarden ===
- *[KO] D. Kühn and D. Osthus, Maximizing several cuts simultaneously, Combinatorics, Probability and Computing 16 (2007), 277-283.

=== Catalog page (statement + literature review) ===
Simultaneous partition of hypergraphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem asks whether two $r$-uniform hypergraphs on the same vertex set always admit a simultaneous $r$-partition in which at least $r!m_i/r^r - o(m_i)$ hyperedges of each cross all $r$ classes. Kühn and Osthus (2007) solved the analogous question for graphs and proved the hypergraph result conditionally when $\Delta_2(H_i) = o(m_i)$ for each $i$; the general case remains open. No post-2013 paper verifiably resolving or substantially advancing the unconditional hypergraph problem was found in the literature search.

 Reviewer notes. The Kühn-Osthus 2007 paper (CPC 16:277-283) is the key reference; its abstract (verified via Cambridge Core) confirms the simultaneous graph-cut result but does not reveal the full hypergraph content. Web-accessible PDFs were binary and unreadable. The arXiv paper 1701.05855 (Haslegrave, Combinatorica 2014) addresses a different problem: judicious partitions of a single r-uniform hypergraph (Bollobás-Thomason conjecture). No post-2013 paper specifically addressing the simultaneous two-hypergraph partition problem was found after four rounds of targeted searches covering arXiv, Combinatorica, and Semantic Scholar. The conditional result (Δ₂ = o(m_i) suffices) appears to originate in the Kühn-Osthus 2007 paper itself, predating the OPG posting.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Problem. Let $ H_1 $ and $ H_2 $ be two $ r $ -uniform hypergraph on the same vertex set $ V $ . Does there always exist a partition of $ V $ into $ r $ classes $ V_1, \dots , V_r $ such that for both $ i=1,2 $ , at least $ r!m_i/r^r -o(m_i) $ hyperedges of $ H_i $ meet each of the classes $ V_1, \dots , V_r $ ?

Discussion

The bound on the number of hyperedges is what one would expect for a random partition. For graphs, the question was answered in the affirmative in [KO]. Keevash and Sudakov observed that the answer is negative if we consider many hypergraphs instead of just 2 (see [KO] for the example).

Bibliography

★ [KO]
 D. Kühn and D. Osthus, Maximizing several cuts simultaneously, Combinatorics, Probability and Computing 16 (2007), 277-283.
