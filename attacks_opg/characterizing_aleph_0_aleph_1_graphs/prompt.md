Attack the following open graph-theory problem.

Catalog id: characterizing_aleph_0_aleph_1_graphs
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Infinite Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/characterizing_aleph_0_aleph_1_graphs/
Original entry: http://www.openproblemgarden.org/op/characterizing_aleph_0_aleph_1_graphs
Problem attributed to: Diestel, Reinhard, Leader, Imre (posted 2008-06-26)

=== Problem statement (OpenProblemGarden) ===
Title: Characterizing (aleph_0,aleph_1)-graphs
Call a graph an $ (\aleph_0,\aleph_1) $ - graph if it has a bipartition $ (A,B) $ so that every vertex in $ A $ has degree $ \aleph_0 $ and every vertex in $ B $ has degree $ \aleph_1 $ . Problem Characterize the $ (\aleph_0,\aleph_1) $ -graphs.

=== Discussion / context (OpenProblemGarden) ===
The motivation for this problem comes from a lovely paper of Diestel and Leader [DL] where they prove that an infinite graph has a normal spanning tree (the natural infinite analogue of a depth-first search tree) if and only if it has no minor isomorphic to either an $ (\aleph_0,\aleph_1) $ -graph or an Aronszajn tree. (An earlier conjecture of Halin asserted that only the first of these excluded minors was needed.) So, $ (\aleph_0,\aleph_1) $ -graphs appear as a forbidden minor obstruction to the existence of a kind of depth-first search tree for infinite graphs. The obvious example of an $ (\aleph_0,\aleph_1) $ -graph is $ K_{\aleph_0,\aleph_1} $ , but there are other natural families of such graphs. For instance, let $ T $ be an infinite binary tree with root $ r $ , and let $ X $ be the set of all rays (one way infinite paths) with endpoint $ r $ . Now, form a bipartite graph with vertex bipartition $ (X,V(T)) $ and adjacency given by the rule that $ v \in V(T) $ adjacent to $ x \in X $ if and only if $ v $ lies on the ray $ x $ (in $ G $ ). Any $ (\aleph_0,\aleph_1) $ -graph which is isomorphic to a subgraph of this graph is said to be of binary type . Say that a $ (\aleph_0,\aleph_1) $ -graph is divisible if there exist disjoint subsets $ A',A'' \subseteq A $ and disjoint subsets $ B',B'' \subseteq B $ so that the graphs induced by both $ A' \cup B' $ and $ A'' \cup B'' $ are $ (\aleph_0,\aleph_1) $ -graphs. It is not difficult to show that every binary type graph is divisible. Curiously, the existence of non-divisible $ (\aleph_0,\aleph_1) $ -graphs depends on the Continuum Hypothesis (see [DL]). Although it is not clear wether or not there is a nice characterization of $ (\aleph_0,\aleph_1) $ -graphs, it would certainly be interesting to find more natural families of these graphs. The following rather more concrete question is posed by Diestel and Leader who suspect the answer is 'no'. Problem Does every $ (\aleph_0,\aleph_1) $ -graph have an $ (\aleph_0,\aleph_1) $ -graph as a minor which is either indivisible or of binary type?

=== References listed by OpenProblemGarden ===
- [DL] R. Diestel and I. Leader, Normal spanning trees, Aronszajn trees and excluded minors, J. London Math. Soc. 63 (2001), 16-32;

=== Catalog page (statement + literature review) ===
Characterizing (aleph_0,aleph_1)-graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The specific sub-question posed by Diestel and Leader — whether every $(\aleph_0,\aleph_1)$-graph has an $(\aleph_0,\aleph_1)$-minor that is either indivisible or of binary type — was answered negatively under the Continuum Hypothesis by Bowler, Geschke, and Pitz (2018, Fundamenta Mathematicae): they construct $(\aleph_0,\aleph_1)$-graphs with no such minor under CH, while under Martin's Axiom with $\neg$CH the class of forbidden $(\aleph_0,\aleph_1)$-graphs in the Diestel–Leader normal-spanning-tree theorem collapses to a single instance up to minors. The broader problem of providing a combinatorial characterization of all $(\aleph_0,\aleph_1)$-graphs remains open.

 Cited literature (2)

 
 
 
partial Minimal obstructions for normal spanning trees
 (2018)
 

 
 Nathan Bowler, Stefan Geschke, Max Pitz · Fundamenta Mathematicae · arXiv:1609.01042

Under CH, constructs $(\aleph_0,\aleph_1)$-graphs with no minor that is either indivisible or of binary type, negatively answering Diestel–Leader's sub-question; under MA+$\neg$CH, shows the forbidden class reduces to a single $(\aleph_0,\aleph_1)$-graph up to minors.
 

 
 
partial A new obstruction for normal spanning trees
 (2021)
 

 
 Max Pitz · Bulletin of the London Mathematical Society · arXiv:2005.04150 · doi:10.1112/blms.12495

Identifies a gap in the Diestel–Leader proof and constructs a third type of excluded minor (an $\aleph_1$-sized graph without a normal spanning tree containing neither of the two Diestel–Leader obstructions as a minor), showing any forbidden-minor characterisation for normal spanning trees requires graphs of arbitrarily large cardinality.
 

 

 Reviewer notes. The Fundamenta Mathematicae journal DOI for the Bowler–Geschke–Pitz paper (vol. 241, 2018, pp. 245–263) could not be directly fetched (paywall), but its content was confirmed via the verified arXiv preprint 1609.01042 and the Hamburg research group page. The Pitz 2021 paper on Halin's conjecture (Israel J. Math., arXiv:2005.02833) proves that a graph has a normal spanning tree iff every minor has countable colouring number; this is tangentially related (characterises graphs with normal spanning trees rather than $(\aleph_0,\aleph_1)$-graphs themselves). No paper found after 2008 provides a full structural characterisation of $(\aleph_0,\aleph_1)$-graphs.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 132s.
 

Problem. Characterize the $ (\aleph_0,\aleph_1) $ -graphs.

Keywords:
binary tree · infinite graph · normal spanning tree · set theory

Discussion

The motivation for this problem comes from a lovely paper of Diestel and Leader [DL] where they prove that an infinite graph has a normal spanning tree (the natural infinite analogue of a depth-first search tree) if and only if it has no minor isomorphic to either an $ (\aleph_0,\aleph_1) $ -graph or an Aronszajn tree. (An earlier conjecture of Halin asserted that only the first of these excluded minors was needed.) So, $ (\aleph_0,\aleph_1) $ -graphs appear as a forbidden minor obstruction to the existence of a kind of depth-first search tree for infinite graphs. The obvious example of an $ (\aleph_0,\aleph_1) $ -graph is $ K_{\aleph_0,\aleph_1} $ , but there are other natural families of such graphs. For instance, let $ T $ be an infinite binary tree with root $ r $ , and let $ X $ be the set of all rays (one way infinite paths) with endpoint $ r $ . Now, form a bipartite graph with vertex bipartition $ (X,V(T)) $ and adjacency given by the rule that $ v \in V(T) $ adjacent to $ x \in X $ if and only if $ v $ lies on the ray $ x $ (in $ G $ ). Any $ (\aleph_0,\aleph_1) $ -graph which is isomorphic to a subgraph of this graph is said to be of binary type . Say that a $ (\aleph_0,\aleph_1) $ -graph is divisible if there exist disjoint subsets $ A',A'' \subseteq A $ and disjoint subsets $ B',B'' \subseteq B $ so that the graphs induced by both $ A' \cup B' $ and $ A'' \cup B'' $ are $ (\aleph_0,\aleph_1) $ -graphs. It is not difficult to show that every binary type graph is divisible. Curiously, the existence of non-divisible $ (\aleph_0,\aleph_1) $ -graphs depends on the Continuum Hypothesis (see [DL]). Although it is not clear wether or not there is a nice characterization of $ (\aleph_0,\aleph_1) $ -graphs, it would certainly be interesting to find more natural families of these graphs. The following rather more concrete question is posed by Diestel and Leader who suspect the answer is 'no'. Problem Does every $ (\aleph_0,\aleph_1) $ -graph have an $ (\aleph_0,\aleph_1) $ -graph as a minor which is either indivisible or of binary type?

Bibliography

 [DL]
 R. Diestel and I. Leader, Normal spanning trees, Aronszajn trees and excluded minors , J. London Math. Soc. 63 (2001), 16-32;
 Normal spanning trees, Aronszajn trees and excluded minors
