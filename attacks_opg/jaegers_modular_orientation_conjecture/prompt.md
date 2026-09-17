Attack the following open graph-theory problem.

Catalog id: jaegers_modular_orientation_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Nowhere-zero flows
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/jaegers_modular_orientation_conjecture/
Original entry: http://www.openproblemgarden.org/op/jaegers_modular_orientation_conjecture
Problem attributed to: Jaeger, Francois (posted 2007-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Jaeger's modular orientation conjecture
Conjecture Every $ 4k $ - edge-connected graph can be oriented so that $ {\mathit indegree}(v) - {\mathit outdegree}(v) \cong 0 $ (mod $ 2k+1 $ ) for every vertex $ v $ .

=== Discussion / context (OpenProblemGarden) ===
Jaeger called an orientation with the above property a modular $ (2k+1) $ - orientation , and observed that a graph has a modular $ (2k+1) $ -orientation if and only if it has a $ (2+\frac{1}{k}) $ -flow. Thus, this conjecture may be seen as a sharp form of the 2+epsilon flow conjecture . For k=1, this problem is precisely the 3-flow conjecture , and for k=2, Jaeger showed that this conjecture (if true) would imply the 5-flow conjecture . If true, this conjecture would be best possible for every value of k. The restriction of this conjecture to planar graphs is open, and has a dual formulation. See Mapping planar graphs to odd cycles .

=== References listed by OpenProblemGarden ===
- [J] F. Jaeger, On circular flows in graphs. Finite and infinite sets, Vol. I, II (Eger, 1981), 391--402, Colloq. Math. Soc. János Bolyai, 37, North-Holland, Amsterdam, 1984.. MathSciNet

=== Catalog page (statement + literature review) ===
Jaeger's modular orientation conjecture — Graph-theory open problems

 
 Status
 disproved
 high confidence
 

 Jaeger's modular orientation conjecture was refuted for $k \geq 3$: Han, Li, Wu, and Zhang (2018) constructed $4k$-edge-connected graphs admitting no modular $(2k+1)$-orientation for every $k \geq 3$, and even $(4k+1)$-edge-connected counterexamples for $k \geq 5$. The special cases $k=1$ (Tutte's 3-flow conjecture) and $k=2$ remain open; the $k=2$ instance was verified asymptotically almost surely for random 9-regular graphs by Delcourt, Huq, and Prałat (2022).

 Cited literature (2)

 
 
 
counterexample Counterexamples to Jaeger's Circular Flow Conjecture
 (2018)
 

 
 Miaomiao Han, Jiaao Li, Yezhou Wu, Cunquan Zhang · Journal of Combinatorial Theory, Series B

For every integer $k \geq 3$ constructs a $4k$-edge-connected graph that admits no modular $(2k+1)$-orientation, directly disproving Jaeger's conjecture; for $k \geq 5$ even $(4k+1)$-edge-connected counterexamples exist.
 

 
 
partial Almost all 9-regular graphs have a modulo-5 orientation
 (2022)
 

 
 Michelle Delcourt, Reaz Huq, Pawel Pralat · arXiv preprint · arXiv:2210.12103 · doi:10.48550/arXiv.2210.12103

Using the small subgraph conditioning method, proves Jaeger's conjecture for $k=2$ (modulo-5 orientation of 9-regular graphs) holds asymptotically almost surely for random 9-regular graphs, extending the $k=1$ result of Pralat-Wormald.
 

 

 Reviewer notes. Jaeger's circular flow conjecture (every $4k$-edge-connected graph has a circular flow of value at most $2+1/k$) is equivalent to the modular orientation conjecture by Jaeger's own observation, so the Han-Li-Wu-Zhang counterexamples apply directly. The partial positive result of Lovász, Thomassen, Wu, and Zhang (2013, JCTB) — that every $6k$-edge-connected graph has a modular $(2k+1)$-orientation — could not be verified via a readable URL (all WVU/ScienceDirect fetches returned binary or 403); it is mentioned in notes only. The conjecture survives only for $k=1$ (equivalent to Tutte's 3-flow conjecture, still open for 4-edge-connected graphs) and $k=2$ (still fully open). The Noga Alon paper on quasi-random regular graphs (Princeton preprint) was found but not successfully fetched.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. Every $ 4k $ - edge-connected graph can be oriented so that $ {\mathit indegree}(v) - {\mathit outdegree}(v) \cong 0 $ (mod $ 2k+1 $ ) for every vertex $ v $ .

Keywords:
nowhere-zero flow · orientation

Discussion

Jaeger called an orientation with the above property a modular $ (2k+1) $ - orientation , and observed that a graph has a modular $ (2k+1) $ -orientation if and only if it has a $ (2+\frac{1}{k}) $ -flow. Thus, this conjecture may be seen as a sharp form of the 2+epsilon flow conjecture . For k=1, this problem is precisely the 3-flow conjecture , and for k=2, Jaeger showed that this conjecture (if true) would imply the 5-flow conjecture . If true, this conjecture would be best possible for every value of k. The restriction of this conjecture to planar graphs is open, and has a dual formulation. See Mapping planar graphs to odd cycles .

Bibliography

 [J]
 F. Jaeger, On circular flows in graphs. Finite and infinite sets, Vol. I, II (Eger, 1981), 391--402, Colloq. Math. Soc. János Bolyai, 37, North-Holland, Amsterdam, 1984.. MathSciNet
 MathSciNet

Related conjectures

 
 implies
 3-flow conjecture
 partial
 The k=1 case of Jaeger's conjecture concerns 4-edge-connected graphs and asks for a modular 3-orientation (indegree-outdegree = 0 mod 3), which by Tutte's theorem is equivalent to a nowhere-zero Z3-flow and hence to a nowhere-zero 3-flow. So the target is precisely the k=1 instance of the source, and the universally quantified source implies it by restriction. The source's own OPG context states verbatim: 'For k=1, this problem is precisely the 3-flow conjecture.' The disproof of the general conjecture (for k>=3) does not affect this logical implication; the k=1 case remains open.
 

 
 implies
 5-flow conjecture
 partial
 The implication is explicitly stated in the source's own OPG context: 'for k=2, Jaeger showed that this conjecture (if true) would imply the 5-flow conjecture.' The full modular orientation conjecture (all k) contains the k=2 case (every 8-edge-connected graph has a modular 5-orientation, equivalently a 5/2-flow), and Jaeger's reduction derives nowhere-zero 5-flows for all bridgeless graphs from it, so truth of the source forces truth of the target. Direction correct. Note the source conjecture has since been disproved (for k >= 3, by Han, Li, Wu, Zhang), but that does not affect the validity of the conditional implication, and the k=2 case relevant to the reduction remains open.
 

 
 implied by
 Circular flow numbers of $r$-graphs
 disproved
(plausible) What is explicitly established (Steffen, arXiv:1310.8441 and the OPG context) is only: truth for even t=2t' implies Jaeger's conjecture restricted to (4t'+1)-REGULAR graphs (a 4t'-edge-connected (4t'+1)-regular graph is a (4t'+1)-graph, since its odd cuts are odd hence >= 4t'+1). The target as stated covers all 4k-edge-connected graphs, so the full implication needs the reduction of Jaeger's conjecture to its regular restriction. That equivalence is documented for k=1 (both equal the 3-flow conjecture) and is treated as folklore for general k (papers state Jaeger's conjecture in the regular form; the Han-Li-Wu-Zhang counterexamples are (4p+1)-regular and disprove both statements simultaneously), but I found no explicit general-k equivalence proof, so I stop short of confirming the full implication.
 

 
 implies
 Mapping planar graphs to odd cycles
 partial
 Let G be planar with girth >= 4k and let G* be its planar dual. Cycles of G correspond to minimal edge cuts of G*, so girth(G) >= 4k makes G* 4k-edge-connected. Jaeger's conjecture applied to G* gives a modular (2k+1)-orientation, which Jaeger showed is equivalent to a circular (2+1/k)-flow of G*; by planar flow/coloring duality this is a (2+1/k)-circular-coloring of G, i.e., a homomorphism G -> C_{2k+1}. The target's OPG page states this explicitly: 'This conjecture is Jaeger's modular orientation conjecture restricted to planar graphs and then dualized,' listing the chain of equivalences. Direction correct: the general-graph orientation conjecture is stronger. Note the source is now disproved for k >= 3 (Han-Li-Wu-Zhang), which does not affect the implication; the planar/dual case remains open.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
