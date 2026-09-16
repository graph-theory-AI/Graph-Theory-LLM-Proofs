Attack the following open graph-theory problem.

Catalog id: jones_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Basic Graph Theory » Cycles
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/jones_conjecture/
Original entry: http://www.openproblemgarden.org/op/jones_conjecture
Problem attributed to: Kloks, Ton, Lee, Chuan-Min, Liu, Jiping (posted 2007-10-09)

=== Problem statement (OpenProblemGarden) ===
Title: Jones' conjecture
For a graph $ G $ , let $ cp(G) $ denote the cardinality of a maximum cycle packing (collection of vertex disjoint cycles) and let $ cc(G) $ denote the cardinality of a minimum feedback vertex set (set of vertices $ X $ so that $ G-X $ is acyclic). Conjecture For every planar graph $ G $ , $ cc(G)\leq 2cp(G) $ .

=== Discussion / context (OpenProblemGarden) ===
In [KLL], the authors mention that there exists a family of nonplanar graphs for which $ cc(G) = \Theta( cp(G) \log cp(G) ) $ , so no such result could hold for general graphs. They also point out that the conjecture is tight for wheels, and they prove it for the special case of outerplanar graphs.

=== References listed by OpenProblemGarden ===
- *[KLL] Ton Kloks, Chuan-Min Lee, and Jiping Liu, New Algorithms for -Face Cover, -Feedback Vertex Set, and -Disjoint Cycles on Plane and Planar Graphs, in Proceedings of the 28th International Workshop on Graph-Theoretic Concepts in Computer Science (WG2002), LNCS 2573, pp. 282--295, 2002.

=== Catalog page (statement + literature review) ===
Jones' conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Jones' conjecture — that $cc(G) \leq 2\,cp(G)$ for every planar graph $G$ — remains open for general planar graphs, but has seen substantial partial progress since 2007. The bound for all planar graphs was tightened from $5\,cp(G)$ to $3\,cp(G)$ by Chappell, Gimbel, and Hartman (2014), the conjecture was proved for subcubic planar graphs by Bonamy et al. (2021), and further confirmed for Halin graphs and 'based' planar graphs (those containing a face adjacent to every other face) by Bärnkopf and Győri (2024).

 Cited literature (4)

 
 
 
partial On cycle packings and feedback vertex sets
 (2014)
 

 
 Glenn G. Chappell, John Gimbel, Chris Hartman · Contributions to Discrete Mathematics · doi:10.55016/ojs/cdm.v9i2.62105

Proves $cc(G) \leq 3\,cp(G)$ for every planar graph (improving the previously known factor-5 bound from Kloks–Lee–Liu), and extends the factor-3 bound to all graphs embedded in surfaces of non-negative Euler characteristic.
 

 
 
partial Jones' Conjecture in subcubic graphs
 (2021)
 

 
 Marthe Bonamy, François Dross, Tomáš Masařík, Andrea Munaro, Wojciech Nadara, Marcin Pilipczuk, Michał Pilipczuk · The Electronic Journal of Combinatorics · arXiv:1912.01570 · doi:10.37236/9192

Proves Jones' conjecture in full for subcubic planar graphs: if such a graph has no $k+1$ vertex-disjoint cycles, then $2k$ vertices suffice to destroy all cycles.
 

 
 
partial Jones' conjecture for Halin graphs and a bit more
 (2024)
 

 
 Pál Bärnkopf, Ervin Győri · arXiv preprint · arXiv:2401.07376

Proves Jones' conjecture for Halin graphs and, more generally, for 'based planar graphs' — planar graphs that contain a face adjacent to every other face.
 

 
 
partial Jones' Conjecture in subcubic graphs
 (2019)
 

 
 Marthe Bonamy, François Dross, Tomáš Masařík, Wojciech Nadara, Marcin Pilipczuk, Michał Pilipczuk · arXiv preprint · arXiv:1912.01570

Proves Jones' Conjecture for all subcubic planar multigraphs, i.e., establishes $\mathrm{fvs}(G) \leq 2 \cdot \mathrm{cp}(G)$ when the maximum degree is at most 3.
 

 

 Reviewer notes. The Princeton DataSpace entry (dsp01tb09j840d) returned HTTP 401 and could not be verified; it appears to be a thesis on the subcubic case and was not cited. Schlomberg–Thiele–Vygen (arXiv:2207.00450) on packing cycles in planar/bounded-genus graphs was fetched but does not directly address Jones' conjecture and was excluded. The arXiv version of the Bonamy et al. paper (1912.01570, 2019) lists six authors; the published EJC version (2021) adds Andrea Munaro as a seventh — the published list is used here.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. For every planar graph $ G $ , $ cc(G)\leq 2cp(G) $ .

Keywords:
cycle packing · feedback vertex set · planar graph

Discussion

In [KLL], the authors mention that there exists a family of nonplanar graphs for which $ cc(G) = \Theta( cp(G) \log cp(G) ) $ , so no such result could hold for general graphs. They also point out that the conjecture is tight for wheels, and they prove it for the special case of outerplanar graphs.

Bibliography

★ [KLL]
 Ton Kloks, Chuan-Min Lee, and Jiping Liu, New Algorithms for $ k $ -Face Cover, $ k $ -Feedback Vertex Set, and $ k $ -Disjoint Cycles on Plane and Planar Graphs, in Proceedings of the 28th International Workshop on Graph-Theoretic Concepts in Computer Science (WG2002), LNCS 2573, pp. 282--295, 2002.
