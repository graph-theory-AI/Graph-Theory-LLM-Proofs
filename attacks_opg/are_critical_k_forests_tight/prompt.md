Attack the following open graph-theory problem.

Catalog id: are_critical_k_forests_tight
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Hypergraphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/are_critical_k_forests_tight/
Original entry: http://www.openproblemgarden.org/op/are_critical_k_forests_tight
Problem attributed to: Strausz, Ricardo (posted 2007-09-01)

=== Problem statement (OpenProblemGarden) ===
Title: ¿Are critical k-forests tight?
Conjecture Let $ H $ be a $ k $ - uniform hypergraph. If $ H $ is a critical $ k $ -forest, then it is a $ k $ -tree.

=== Discussion / context (OpenProblemGarden) ===
We say that a hypergraph $ H=(V,E) $ is a $ k $ -graph if it is $ k $ -uniform, and denote its order by $ n=|V| $ and its size by $ m=|E| $ . Laszlo Lovasz introduced the following concept: a $ k $ -graph $ H=(V,E) $ is said to be a $ k $ -forest if for every edge $ e\in E $ there exists a $ k $ -colouing $ \varsigma\colon V\to[k] $ such that $ \varsigma(e')=[k]\Leftrightarrow e'=e $ ; that is, such that only the edge $ e $ receives the $ k $ colours in its vertices. Clearly a $ 2 $ -forest is simply a forest in the usual sense (i.e., an acyclic graph). Lovasz proved that Theorem A $ k $ -forest has size at most $ m\leq{n-1\choose k-1} $ . On the other hand, Victor Neumann-Lara introduced the following invariant: the heterochromatic number of a $ k $ -graph $ H=(V,G) $ is the minimum number of colours $ c $ such that, in every colouring $ \varsigma\colon V\to[c] $ there is an edge wich receives different colours in each of its vertices; that is, there exists $ e\in E $ such that $ |\varsigma(e)|=k $ . If the heterochromatic number and the rank are equal, the hypergraph is said to be tight . Clearly a $ 2 $ -graph is tight if and only if it is connected . A tight $ k $ -forest is called a $ k $ -tree . I can prove the following Theorem If a $ k $ -forest has size $ m={n-1\choose k-1} $ then it is tight — and therefore a $ k $ -tree. Finally, we say that a $ k $ -forest is critical if no edge can be added to it without loosing the property of being a $ k $ -forest; it is maximal (in size) with such a property. Observe that there are critical $ k $ -forests of size $ m<{n-1\choose k-1} $ , whenever $ k>2 $ . So, the conjecture is to motivate the question: ¿are critical $ k $ -forests tight?

=== Catalog page (statement + literature review) ===
¿Are critical k-forests tight? — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 The conjecture that every critical (saturated, inclusion-maximal) $k$-forest is tight (i.e., a $k$-tree) was disproved for $k=3$. Gebauer, Gundert, Moser, and Okamoto (2011) constructed an explicit saturated 3-forest that is not tight, using the definition of $k$-forests due to Graham and Lovász and the tightness notion of Arocha, Bracho, and Neumann-Lara; their abstract explicitly states that this resolves the open problem posed by Strausz.

 Cited literature (1)

 
 
 
counterexample Not All Saturated 3-Forests Are Tight
 (2011)
 

 
 Heidi Gebauer, Anna Gundert, Robin A. Moser, Yoshio Okamoto · arXiv preprint · arXiv:1109.3390

Provides an explicit saturated (inclusion-maximal) 3-forest that is not tight, directly resolving Strausz's open problem in the negative for k=3.
 

 

 Reviewer notes. The paper appears to exist only as an arXiv preprint (no journal publication found). The counterexample is for k=3; the conjecture for k>3 may still be open, but the problem as stated ('critical k-forests') is disproved by this single case. The 2505.05339 paper disproves an unrelated Lovász conjecture about hypergraph matchings.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 95s.
 

Conjecture. Let $ H $ be a $ k $ - uniform hypergraph. If $ H $ is a critical $ k $ -forest, then it is a $ k $ -tree.

Keywords:
heterochromatic number

Discussion

We say that a hypergraph $ H=(V,E) $ is a $ k $ -graph if it is $ k $ -uniform, and denote its order by $ n=|V| $ and its size by $ m=|E| $ . Laszlo Lovasz introduced the following concept: a $ k $ -graph $ H=(V,E) $ is said to be a $ k $ -forest if for every edge $ e\in E $ there exists a $ k $ -colouing $ \varsigma\colon V\to[k] $ such that $ \varsigma(e')=[k]\Leftrightarrow e'=e $ ; that is, such that only the edge $ e $ receives the $ k $ colours in its vertices. Clearly a $ 2 $ -forest is simply a forest in the usual sense (i.e., an acyclic graph). Lovasz proved that Theorem A $ k $ -forest has size at most $ m\leq{n-1\choose k-1} $ . On the other hand, Victor Neumann-Lara introduced the following invariant: the heterochromatic number of a $ k $ -graph $ H=(V,G) $ is the minimum number of colours $ c $ such that, in every colouring $ \varsigma\colon V\to[c] $ there is an edge wich receives different colours in each of its vertices; that is, there exists $ e\in E $ such that $ |\varsigma(e)|=k $ . If the heterochromatic number and the rank are equal, the hypergraph is said to be tight . Clearly a $ 2 $ -graph is tight if and only if it is connected . A tight $ k $ -forest is called a $ k $ -tree . I can prove the following Theorem If a $ k $ -forest has size $ m={n-1\choose k-1} $ then it is tight — and therefore a $ k $ -tree. Finally, we say that a $ k $ -forest is critical if no edge can be added to it without loosing the property of being a $ k $ -forest; it is maximal (in size) with such a property. Observe that there are critical $ k $ -forests of size $ m<{n-1\choose k-1} $ , whenever $ k>2 $ . So, the conjecture is to motivate the question: ¿are critical $ k $ -forests tight?
