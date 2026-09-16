Attack the following open graph-theory problem.

Catalog id: grunbaums_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Topological Graph Theory » Coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/grunbaums_conjecture/
Original entry: http://www.openproblemgarden.org/op/grunbaums_conjecture
Problem attributed to: Grunbaum, Branko (posted 2007-04-04)

=== Problem statement (OpenProblemGarden) ===
Title: Grunbaum's Conjecture
Conjecture If $ G $ is a simple loopless triangulation of an orientable surface , then the dual of $ G $ is 3-edge-colorable.

=== Discussion / context (OpenProblemGarden) ===
The Four Color Theorem is equivalent to the statement that every cubic planar graph with no bridge is 3- edge-colorable . This is precisely equivalent to Grunbaum's conjecture restricted to the plane. Thus, Grunbaum's conjecture, if true, would imply the Four Color Theorem. Indeed, this conjecture suggests a deep generalization of the 4-color theorem. Definition: A cubic graph $ G $ is a snark if $ G $ is internally 4-edge-connected and $ G $ is not 3-edge-colorable. Grunbaum's conjecture states that no snark is the dual of a simple loopless triangulation of an orientable surface. In this light, the conjecture looks to be almost obviously false. To find a counterexample, it suffices to embed a snark in an orientable surface so that the dual has no loops or parallel edges. Of course, the difficulty is in satisfying this last constraint. All known embeddings of snarks in orientable surfaces give rise to either loops or parallel edges in the dual. It is striking to compare this conjecture with the Orientable cycle double cover conjecture . Both conjectures may be stated in terms of embedding snarks in orientable surfaces as follows: Conjecture (Grunbaum's conjecture (version 2)) Every embedding of a snark in an orientable surface has a cycle of length 1 or 2 (a loop or parallel edges) in the dual. Conjecture (Orientable cycle double cover conjecture) Every snark may be embedded in an orientable surface so that the dual graph has no cycle of length 1 (no loop). In this light it may look unlikely that both Grunbaum's conjecture and the orientable cycle double cover conjecture are true. I (M. DeVos) don't have a strong sense for or against either of these conjectures, and I don't believe there is a strong consensus among experts. Mohar and Robertson have suggested the following weak version of Grunbaum's conjecture: There exists a fixed constant $ k $ so that the dual of every loopless triangulation of an orientable surface of face-width $ >k $ is 3-edge-colorable. Robertson has suggested that this may still hold true even for nonorientable surfaces. The following conjecture is a further weakening of Grunbaum's conjecture which would allow the parameter $ k $ to depend on the surface. This is probably the weakest open problem in this vein. Conjecture (Weak Grunbaum conjecture) For every orientable surface $ \Sigma $ , there is a fixed constant $ k $ so that the dual of every loopless triangulation of $ \Sigma $ with face-width $ >k $ is 3-edge-colorable.

=== References listed by OpenProblemGarden ===
- [G] B. Grunbaum, Conjecture 6. In Recent progress in combinatorics, (W.T. Tutte Ed.), Academic Press (1969) 343.

=== Catalog page (statement + literature review) ===
Grunbaum's Conjecture — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 The conjecture in its full generality was disproved by Kochol (2009), who constructed snarks with polyhedral embeddings in orientable surfaces of genus $\geq 5$, showing that the dual of a simple loopless triangulation of such a surface need not be 3-edge-colorable. For the torus (genus 1), the conjecture was fully confirmed in 2025 by Inoue, Kawarabayashi, Miyashita, Mohar, and Sonobe, who characterized all non-3-edge-colorable toroidal cubic graphs as exactly the Petersen-like graphs. The conjecture remains open for orientable surfaces of genera 2, 3, and 4.

 Cited literature (3)

 
 
 
partial Grünbaum Colorings of Toroidal Triangulations
 (2008)
 

 
 Michael O. Albertson, Hannah Alpert, sarah-marie belcastro, Ruth Haas · arXiv preprint · arXiv:0805.0394

Proves Grünbaum's conjecture for toroidal triangulations G with chi(G) != 5: if G triangulates the torus and has chromatic number different from 5, then there exists a 3-edge-coloring of G such that every facial triangle receives all three colors.
 

 
 
counterexample Polyhedral embeddings of snarks in orientable surfaces
 (2009)
 

 
 Martin Kochol · Proceedings of the American Mathematical Society · doi:10.1090/S0002-9939-08-09698-6

Shows that snarks have polyhedral embeddings in orientable surfaces of sufficiently large genus, giving simple loopless triangulations of orientable surfaces whose duals are not 3-edge-colorable and thereby disproving Grünbaum's conjecture in full generality.
 

 
 
partial Three-edge-coloring (Tait coloring) cubic graphs on the torus: A proof of Grünbaum's conjecture
 (2025)
 

 
 Yuta Inoue, Ken-ichi Kawarabayashi, Atsuyuki Miyashita, Bojan Mohar, Tomohiro Sonobe · arXiv preprint · arXiv:2505.07002

Proves that a 2-connected cubic multigraph embedded in the torus fails to be 3-edge-colorable if and only if it is Petersen-like (obtained from Petersen graph dot products), thereby fully confirming Grünbaum's conjecture for the torus: every polyhedral embedding in the torus yields a 3-edge-colorable dual.
 

 

 Reviewer notes. The primary disproof is Kochol (2009), 'Polyhedral embeddings of snarks in orientable surfaces,' Proc. AMS 137:1613-1619, DOI 10.1090/S0002-9939-08-09698-6; the AMS page is now directly verified and states that the paper gives counterexamples to Grünbaum's conjecture. A companion conference paper appeared in GD 2008, LNCS 5417, ch. 31. The 2024 projective-plane companion paper arXiv:2405.16586 (same author team as the torus paper) is related but concerns a non-orientable surface and is not included in since_posted. Status for genus 2, 3, 4 surfaces remains open per multiple search results.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. If $ G $ is a simple loopless triangulation of an orientable surface , then the dual of $ G $ is 3-edge-colorable.

Keywords:
coloring · surface

Discussion

The Four Color Theorem is equivalent to the statement that every cubic planar graph with no bridge is 3- edge-colorable . This is precisely equivalent to Grunbaum's conjecture restricted to the plane. Thus, Grunbaum's conjecture, if true, would imply the Four Color Theorem. Indeed, this conjecture suggests a deep generalization of the 4-color theorem. Definition: A cubic graph $ G $ is a snark if $ G $ is internally 4-edge-connected and $ G $ is not 3-edge-colorable. Grunbaum's conjecture states that no snark is the dual of a simple loopless triangulation of an orientable surface. In this light, the conjecture looks to be almost obviously false. To find a counterexample, it suffices to embed a snark in an orientable surface so that the dual has no loops or parallel edges. Of course, the difficulty is in satisfying this last constraint. All known embeddings of snarks in orientable surfaces give rise to either loops or parallel edges in the dual. It is striking to compare this conjecture with the Orientable cycle double cover conjecture . Both conjectures may be stated in terms of embedding snarks in orientable surfaces as follows: Conjecture (Grunbaum's conjecture (version 2)) Every embedding of a snark in an orientable surface has a cycle of length 1 or 2 (a loop or parallel edges) in the dual. Conjecture (Orientable cycle double cover conjecture) Every snark may be embedded in an orientable surface so that the dual graph has no cycle of length 1 (no loop). In this light it may look unlikely that both Grunbaum's conjecture and the orientable cycle double cover conjecture are true. I (M. DeVos) don't have a strong sense for or against either of these conjectures, and I don't believe there is a strong consensus among experts. Mohar and Robertson have suggested the following weak version of Grunbaum's conjecture: There exists a fixed constant $ k $ so that the dual of every loopless triangulation of an orientable surface of face-width $ >k $ is 3-edge-colorable. Robertson has suggested that this may still hold true even for nonorientable surfaces. The following conjecture is a further weakening of Grunbaum's conjecture which would allow the parameter $ k $ to depend on the surface. This is probably the weakest open problem in this vein. Conjecture (Weak Grunbaum conjecture) For every orientable surface $ \Sigma $ , there is a fixed constant $ k $ so that the dual of every loopless triangulation of $ \Sigma $ with face-width $ >k $ is 3-edge-colorable.

Bibliography

 [G]
 B. Grunbaum, Conjecture 6. In Recent progress in combinatorics, (W.T. Tutte Ed.), Academic Press (1969) 343.

Related conjectures

 
 related to
 Cycle double cover conjecture
 partial
 The source context compares Grunbaum's conjecture with the ORIENTABLE cycle double cover conjecture, and explicitly as a contrast, not an implication: Grunbaum's says every orientable embedding of a snark has a dual loop or parallel edge, while OCDC says some orientable embedding of every snark has no dual loop — near-opposite assertions about the same objects, neither implying the other. The target here is moreover the plain CDC, one step further removed (OCDC implies CDC, but Grunbaum's conjecture implies neither). Grunbaum's conjecture is in fact disproved (Kochol 2009: snarks with polyhedral embeddings in orientable surfaces) while CDC stands open, consistent only with the absence of implication in the other direction too. Twin conjectures about embedding snarks in orientable surfaces: related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
