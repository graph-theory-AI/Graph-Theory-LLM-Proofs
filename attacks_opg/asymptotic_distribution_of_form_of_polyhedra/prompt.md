Attack the following open graph-theory problem.

Catalog id: asymptotic_distribution_of_form_of_polyhedra
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/asymptotic_distribution_of_form_of_polyhedra/
Original entry: http://www.openproblemgarden.org/op/asymptotic_distribution_of_form_of_polyhedra
Problem attributed to: Rüdinger, Andreas (posted 2009-05-09)

=== Problem statement (OpenProblemGarden) ===
Title: Asymptotic Distribution of Form of Polyhedra
Problem Consider the set of all topologically inequivalent polyhedra with $ k $ edges. Define a form parameter for a polyhedron as $ \beta:= v/(k+2) $ where $ v $ is the number of vertices. What is the distribution of $ \beta $ for $ k \to \infty $ ?

=== Discussion / context (OpenProblemGarden) ===
Consider the set of all topologically inequivalent polyhedra on a sphere with k edges (i.e. polyhedral graphs, Sloan Sequence A002840 ). Due to duality the distribution of the form parameter $ \beta:= v/(k+2) $ is symmetric about $ \beta=1/2 $ . Now a natural question is whether the distribution of beta tends to a limiting distribution when the number of edges tends to infinity. Is there any nontrivial limit theorem by means of rescaling? Some numerical values can be found on Counting Polyhedra suggesting that the distribution concentrates around $ \beta=1/2 $ .

=== Catalog page (statement + literature review) ===
Asymptotic Distribution of Form of Polyhedra — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem asks for the limiting distribution (after possible rescaling) of the form parameter $\beta = v/(k+2)$ over all topologically inequivalent polyhedral graphs with $k$ edges as $k \to \infty$. No paper directly resolving or significantly advancing this problem was found in the literature post-2009. The related asymptotic enumeration literature on 3-connected planar graphs/maps has grown (Giménez–Noy 2009 on labeled planar graphs; work on random cubic planar graphs; enumeration of 3-connected bipartite maps), but none of these works addresses the specific conditional distribution of $\beta$ given the edge count for unlabeled polyhedral graphs.

 Reviewer notes. The OPG problem page (openproblemgarden.org) was unreachable (ECONNREFUSED) during this review. The JAMS full PDF (Giménez–Noy 2009) returned HTTP 403. The specific question — the limiting distribution of $\beta = v/(k+2)$ over unlabeled polyhedral graphs with exactly $k$ edges — sits at the intersection of combinatorial enumeration and probability theory, but no paper in the accessible literature appears to treat it. The closest body of work concerns labeled random planar or 3-connected planar graphs with $n$ vertices (where the number of edges is shown to be asymptotically normal around $\approx 2.21n$), but fixing edges and studying the vertex count distribution for unlabeled polyhedral graphs is a distinct, apparently unstudied problem. Confidence is medium rather than high because some relevant work may exist in graph-enumeration venues (e.g., proceedings of GD, EuroComb, or German-language journals) that did not surface in English-language web searches.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 1354s.
 

Problem. Consider the set of all topologically inequivalent polyhedra with $ k $ edges. Define a form parameter for a polyhedron as $ \beta:= v/(k+2) $ where $ v $ is the number of vertices. What is the distribution of $ \beta $ for $ k \to \infty $ ?

Keywords:
polyhedral graphs, distribution

Discussion

Consider the set of all topologically inequivalent polyhedra on a sphere with k edges (i.e. polyhedral graphs, Sloan Sequence A002840 ). Due to duality the distribution of the form parameter $ \beta:= v/(k+2) $ is symmetric about $ \beta=1/2 $ . Now a natural question is whether the distribution of beta tends to a limiting distribution when the number of edges tends to infinity. Is there any nontrivial limit theorem by means of rescaling? Some numerical values can be found on Counting Polyhedra suggesting that the distribution concentrates around $ \beta=1/2 $ .
