Attack the following open graph-theory problem.

Catalog id: graceful_tree_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Labeling
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/graceful_tree_conjecture/
Original entry: http://www.openproblemgarden.org/op/graceful_tree_conjecture

=== Problem statement (OpenProblemGarden) ===
Title: Graceful Tree Conjecture
Conjecture All trees are graceful

=== Discussion / context (OpenProblemGarden) ===
Label the vertices of a simple undirected graph $ G(V,E) $ (where $ |V| = n $ and $ |E| = m $ ) with integers from $ 0 $ to $ m $ . Now label each edge with absolute difference of the labels of its incident vertices. The labeling is said to be graceful if the edges are labelled $ 1 $ through $ m $ inclusive (with no number repeated). A graph is called graceful if it has at least one such labeling. This labeling was originally introduced in 1967 by Rosa. The name graceful labeling was coined later by Golomb. Gracefully labeled graphs serve as models in a wide range of applications including coding theory and communication network addressing. The graceful labeling problem is to determine which graphs are graceful. It is conjectured (by Kotzig, Ringel and Rosa) that all trees are graceful. Despite numerous (more than 200) publications on graceful labeling for over three decades, only a very restricted classes of trees (and also of some other graphs) have been shown to be graceful. These restricted classes include paths, stars, complete bipartite graphs, prism graphs, wheel graphs, caterpillar graphs, olive trees, and symmetrical trees.

=== Catalog page (statement + literature review) ===
Graceful Tree Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Graceful Tree Conjecture remains open. The strongest progress since the OPG posting (2007) is asymptotic: Adamaszek, Allen, Grosu and Hladky (2016, arXiv:1608.01577) proved that almost all trees admit an 'almost graceful' labelling using vertex labels in $\{1,\dots,(1+c)n\}$, and Letzter, Pokrovskiy and Williams (2025, arXiv:2511.11331) showed that every sufficiently large tree on $n$ vertices has gracesize $\ge (1-\varepsilon)n$, i.e. an asymptotic version of the conjecture. A claimed full proof by Gnang (arXiv:2202.03178, 2022) is an unpublished preprint flagged by arXiv for text overlap and has not been verified by the community.

 Cited literature (3)

 
 
 
partial Almost all trees are almost graceful
 (2016)
 

 
 Anna Adamaszek, Peter Allen, Codrut Grosu, Jan Hladky · arXiv preprint · arXiv:1608.01577

Proves a relaxation of the conjecture: for any $c>0$, asymptotically almost all $n$-vertex trees admit an injective labelling into $\{1,\dots,(1+c)n\}$ with pairwise distinct edge differences (and all bounded-degree trees do).
 

 
 
partial On the gracesize of trees
 (2025)
 

 
 Shoham Letzter, Alexey Pokrovskiy, Ella Williams · arXiv preprint · arXiv:2511.11331

Proves an asymptotic version of the Graceful Tree Conjecture: for every $\varepsilon>0$, every sufficiently large tree on $n$ vertices admits a labelling whose gracesize is at least $(1-\varepsilon)n$, i.e. all but $\varepsilon n$ edge differences are distinct.
 

 
 
proof A proof of the Kotzig-Ringel-Rosa Conjecture
 (2022)
 

 
 Edinah K. Gnang · arXiv preprint · arXiv:2202.03178

Claims a complete proof of the Graceful Tree Conjecture via a functional reformulation and a composition lemma; remains an unpublished preprint, has been flagged by arXiv for text overlap with arXiv:2111.12812, and is not accepted by the community as a verified proof.
 

 

 Reviewer notes. Gallian's Dynamic Survey of Graph Labeling (DS6, version dated October 30, 2025) continues to list the Graceful Tree Conjecture as open. The Gnang preprint (arXiv:2202.03178) is included with kind 'proof' for completeness but should be regarded with scepticism: it has been on arXiv since 2022 with no journal publication, and arXiv flagged it for text overlap with another preprint. The status 'partial' reflects the verified asymptotic progress (Adamaszek et al. 2016, Letzter-Pokrovskiy-Williams 2025); the original conjecture that every tree is graceful is still open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. All trees are graceful

Keywords:
combinatorics · graceful labeling

Discussion

Label the vertices of a simple undirected graph $ G(V,E) $ (where $ |V| = n $ and $ |E| = m $ ) with integers from $ 0 $ to $ m $ . Now label each edge with absolute difference of the labels of its incident vertices. The labeling is said to be graceful if the edges are labelled $ 1 $ through $ m $ inclusive (with no number repeated). A graph is called graceful if it has at least one such labeling. This labeling was originally introduced in 1967 by Rosa. The name graceful labeling was coined later by Golomb. Gracefully labeled graphs serve as models in a wide range of applications including coding theory and communication network addressing. The graceful labeling problem is to determine which graphs are graceful. It is conjectured (by Kotzig, Ringel and Rosa) that all trees are graceful. Despite numerous (more than 200) publications on graceful labeling for over three decades, only a very restricted classes of trees (and also of some other graphs) have been shown to be graceful. These restricted classes include paths, stars, complete bipartite graphs, prism graphs, wheel graphs, caterpillar graphs, olive trees, and symmetrical trees.
