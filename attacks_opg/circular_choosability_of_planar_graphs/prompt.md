Attack the following open graph-theory problem.

Catalog id: circular_choosability_of_planar_graphs
Source: OpenProblemGarden (importance: Low ✭)
Subject: Graph Theory » Coloring » Homomorphisms
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/circular_choosability_of_planar_graphs/
Original entry: http://www.openproblemgarden.org/op/circular_choosability_of_planar_graphs
Problem attributed to: Mohar, Bojan (posted 2012-08-23)

=== Problem statement (OpenProblemGarden) ===
Title: Circular choosability of planar graphs
Let $ G = (V, E) $ be a graph. If $ p $ and $ q $ are two integers, a $ (p,q) $ -colouring of $ G $ is a function $ c $ from $ V $ to $ \{0,\dots,p-1\} $ such that $ q \le |c(u)-c(v)| \le p-q $ for each edge $ uv\in E $ . Given a list assignment $ L $ of $ G $ , i.e.~a mapping that assigns to every vertex $ v $ a set of non-negative integers, an $ L $ -colouring of $ G $ is a mapping $ c : V \to N $ such that $ c(v)\in L(v) $ for every $ v\in V $ . A list assignment $ L $ is a $ t $ - $ (p,q) $ -list-assignment if $ L(v) \subseteq \{0,\dots,p-1\} $ and $ |L(v)| \ge tq $ for each vertex $ v \in V $ . Given such a list assignment $ L $ , the graph G is $ (p,q) $ - $ L $ -colourable if there exists a $ (p,q) $ - $ L $ -colouring $ c $ , i.e. $ c $ is both a $ (p,q) $ -colouring and an $ L $ -colouring. For any real number $ t \ge 1 $ , the graph $ G $ is $ t $ - $ (p,q) $ -choosable if it is $ (p,q) $ - $ L $ -colourable for every $ t $ - $ (p,q) $ -list-assignment $ L $ . Last, $ G $ is circularly $ t $ -choosable if it is $ t $ - $ (p,q) $ -choosable for any $ p $ , $ q $ . The circular choosability (or circular list chromatic number or circular choice number) of G is $$cch(G) := \inf\{t \ge 1 : G \text{ is circularly $t$-choosable}\}.$$ Problem What is the best upper bound on circular choosability for planar graphs?

=== Discussion / context (OpenProblemGarden) ===
The problem was first posed in 2003 by Mohar (Problem 4 of link *) who suggested the answer should be between 4 and 5. Some time later, Havet, Kang, Müller, and Sereni [HKMS] showed that in fact the answer is somewhere between 6 and 8. The upper bound extends a celebrated planar choosability proof due to Thomassen [T]. The lower bound is by way of an elementary, though rather large, construction.

=== References listed by OpenProblemGarden ===
- [HKMS] F. Havet, R. J. Kang, T. Müller, and J.-S. Sereni. Circular choosability. J. Graph Theory 61 (2009), no. 4, 241--270.
- [T] C. Thomassen. Every planar graph is 5-choosable. J. Combinatorial Theory B 62 (1994) 180--181

=== Catalog page (statement + literature review) ===
Circular choosability of planar graphs — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 As of the posting date (August 2012), the best known bounds on $\tau = \sup\{\mathrm{cch}(G) : G \text{ planar}\}$ were $6 \le \tau \le 8$, established by Havet, Kang, Müller, and Sereni (2009). Exhaustive searching across arXiv, journal indices, and web resources found no verifiable post-2012 paper that narrows this gap or resolves the problem for general planar graphs.

 Reviewer notes. The Wang–Liu paper on circular choosability of planar graphs with large girth appeared on the Combinatorial Press page and ResearchGate, but its publication date is 2011, predating the OPG posting, so it is not included in since_posted. The HAL Inria page for the HKMS paper returned HTTP 403 and could not be verified; however, the 2009 HKMS result is pre-posting baseline knowledge and requires no citation here. No arXiv preprint or journal paper post-August 2012 specifically addressing the $6$–$8$ gap for circular choosability of general planar graphs was found through any of the six queries. Confidence is medium rather than high because the topic is niche enough that relevant papers could reside in journals (e.g., Ars Combinatoria, Australasian J. Combinatorics) not well indexed by the search engine.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 131s.
 

Problem. What is the best upper bound on circular choosability for planar graphs?

Keywords:
choosability · circular colouring · planar graphs

Discussion

The problem was first posed in 2003 by Mohar (Problem 4 of link *) who suggested the answer should be between 4 and 5. Some time later, Havet, Kang, Müller, and Sereni [HKMS] showed that in fact the answer is somewhere between 6 and 8. The upper bound extends a celebrated planar choosability proof due to Thomassen [T]. The lower bound is by way of an elementary, though rather large, construction.

Bibliography

 [HKMS]
 F. Havet, R. J. Kang, T. Müller, and J.-S. Sereni. Circular choosability. J. Graph Theory 61 (2009), no. 4, 241--270.

 [T]
 C. Thomassen. Every planar graph is 5-choosable. J. Combinatorial Theory B 62 (1994) 180--181
