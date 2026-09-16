Attack the following open graph-theory problem.

Catalog id: a_gold_grabbing_game
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Graph Algorithms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/a_gold_grabbing_game/
Original entry: http://www.openproblemgarden.org/op/a_gold_grabbing_game
Problem attributed to: Rosenfeld, Moshe (posted 2009-10-02)

=== Problem statement (OpenProblemGarden) ===
Title: A gold-grabbing game
Setup Fix a tree $ T $ and for every vertex $ v \in V(T) $ a non-negative integer $ g(v) $ which we think of as the amount of gold at $ v $ . 2-Player game Players alternate turns. On each turn, a player chooses a leaf vertex $ v $ of the tree, takes the gold at this vertex, and then deletes $ v $ . The game ends when the tree is empty, and the winner is the player who has accumulated the most gold. Problem Find optimal strategies for the players.

=== Discussion / context (OpenProblemGarden) ===
In the special case when $ T $ is a path of even length, the first player can ensure that she chooses either all of the even vertices, or all of the odd vertices. Thus, player 1 should never finish with less than player 2, and whenever the total gold on the odd vertices and the total gold on the even vertices are not equal, there is a winning strategy for player 1.

=== Catalog page (statement + literature review) ===
A gold-grabbing game — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The gold-grabbing game on trees attracted significant attention after 2009. Micek and Walczak (2011) formalised a graph version, proved that the first player can guarantee at least $1/4$ of the total weight on even trees, and conjectured the threshold is $1/2$; Seacrest and Seacrest (2012) proved this conjecture for trees (first player can always secure at least half the gold on any tree with an even number of vertices), resolving the main case of Rosenfeld's problem. Subsequent work extended the half-guarantee to larger graph families (even blow-ups of trees and cycles), while the full bipartite-graph generalisation and exact optimal-strategy characterisation for odd trees remain open.

 Cited literature (3)

 
 
 
partial A Graph-Grabbing Game
 (2011)
 

 
 Piotr Micek, Bartosz Walczak · Combinatorics, Probability and Computing · doi:10.1017/S0963548311000071

Proved the first player can guarantee at least 1/4 of the total weight on any even-vertex tree, conjectured the true threshold is 1/2, and verified the conjecture for subdivided stars.
 

 
 
partial The graph grabbing game on blow-ups of trees and cycles
 (2020)
 

 
 Sopon Boriboon, Teeradej Kittipassorn · arXiv preprint · arXiv:2007.11805 · doi:10.48550/arXiv.2007.11805

Extended the first-player half-guarantee to even blow-ups of trees and cycles, expanding the class of graphs for which the Seacrest–Seacrest conjecture is known to hold.
 

 
 
partial On conjectures concerning the graph grabbing game
 (2023)
 

 
 Lawrence Hollom · arXiv preprint · arXiv:2311.02109 · doi:10.48550/arXiv.2311.02109

Provided a family of counterexamples to the stronger Eoh–Choi conjecture, proposed a weaker replacement, and showed the Seacrest–Seacrest bipartite conjecture and the revised conjecture are equivalent when vertex weights are restricted to {0,1}.
 

 

 Reviewer notes. The key paper—Seacrest, D. E. and Seacrest, T., 'Grabbing the gold', Discrete Mathematics 312(10):1804–1806, 2012 (DOI: 10.1016/j.disc.2012.01.009)—is confirmed by multiple independent sources (algnotes blog, Hollom 2023, search snippets) to prove the first-player 1/2-guarantee for trees; however, ScienceDirect returned HTTP 403 so the paper could not be directly fetched and verified per the rules, and is therefore omitted from since_posted despite being the single most directly relevant post-2009 result. The bipartite generalisation (first player wins on any even-order bipartite graph) remains open as of 2023; no evidence of a resolution was found for 2024–2025.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 291s.
 

Problem. Find optimal strategies for the players.

Keywords:
game · tree

Discussion

In the special case when $ T $ is a path of even length, the first player can ensure that she chooses either all of the even vertices, or all of the odd vertices. Thus, player 1 should never finish with less than player 2, and whenever the total gold on the odd vertices and the total gold on the even vertices are not equal, there is a winning strategy for player 1.
