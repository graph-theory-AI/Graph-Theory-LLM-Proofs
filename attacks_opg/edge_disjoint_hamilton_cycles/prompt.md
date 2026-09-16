Attack the following open graph-theory problem.

Catalog id: edge_disjoint_hamilton_cycles
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs » Tournaments
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/edge_disjoint_hamilton_cycles/
Original entry: http://www.openproblemgarden.org/op/edge_disjoint_hamilton_cycles
Problem attributed to: Thomassen, Carsten (posted 2013-03-08)

=== Problem statement (OpenProblemGarden) ===
Title: Edge-disjoint Hamilton cycles in highly strongly connected tournaments.
Conjecture For every $ k\geq 2 $ , there is an integer $ f(k) $ so that every strongly $ f(k) $ -connected tournament has $ k $ edge-disjoint Hamilton cycles.

=== Discussion / context (OpenProblemGarden) ===
Kelly made the following conjecture which replaces the assumption of high connectivity by regularity. Conjecture Every regular tournament of order $ n $ can be decomposed into $ (n-1)/2 $ Hamilton directed cycles. Kelly's conjecture has been proved for tournaments of sufficiently large order by Kühn and Osthus [KO].

=== References listed by OpenProblemGarden ===
- [KO] Daniela Kühn and Deryk Osthus, Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments, Advances in Mathematics 237 (2013), 62-146.
- *[T] C. Thomassen, Edge-disjoint Hamiltonian paths and cycles in tournaments, Proc. London Math. Soc. 45 (1982), 151-168.

=== Catalog page (statement + literature review) ===
Edge-disjoint Hamilton cycles in highly strongly connected tournaments. — Graph-theory open problems

 
 Status
 solved
 high confidence
 

 Thomassen's conjecture was proved by Kühn, Lapinskas, Osthus, and Patel (2014), who showed that every strongly $f(k)$-connected tournament with $f(k)=O(k^2\log^2 k)$ contains $k$ edge-disjoint Hamilton cycles. Pokrovskiy (2017) subsequently improved the bound to $f(k)\le Ck^2$, which is optimal up to the constant.

 Cited literature (2)

 
 
 
proof Proof of a conjecture of Thomassen on Hamilton cycles in highly connected tournaments
 (2014)
 

 
 Daniela Kühn, John Lapinskas, Deryk Osthus, Viresh Patel · Proceedings of the London Mathematical Society · doi:10.1112/plms/pdu019

Proves Thomassen's conjecture by establishing that every strongly $f(k)$-connected tournament with $f(k)=O(k^2\log^2 k)$ contains $k$ edge-disjoint Hamilton cycles, using a key lemma that strongly $10^4 k\log k$-connected tournaments are $k$-linked.
 

 
 
proof Edge disjoint Hamiltonian cycles in highly connected tournaments
 (2017)
 

 
 Alexey Pokrovskiy · International Mathematics Research Notices · arXiv:1406.7556 · doi:10.1093/imrn/rnw009

Improves the bound in Thomassen's conjecture to $f(k)\le Ck^2$ for an absolute constant $C$, which is optimal up to the constant factor, and resolves a related question of Thomassen on spanning linkages.
 

 

 Reviewer notes. The conjecture as stated (existence of $f(k)$) was proved by Kühn-Lapinskas-Osthus-Patel (PLMS 2014) with $f(k)=O(k^2\log^2 k)$, and the optimal-order bound $f(k)=O(k^2)$ was established by Pokrovskiy (IMRN 2017, arXiv:1406.7556 from 2014). Both papers postdate the OPG posting of 2013-03-08.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Conjecture. For every $ k\geq 2 $ , there is an integer $ f(k) $ so that every strongly $ f(k) $ -connected tournament has $ k $ edge-disjoint Hamilton cycles.

Discussion

Kelly made the following conjecture which replaces the assumption of high connectivity by regularity. Conjecture Every regular tournament of order $ n $ can be decomposed into $ (n-1)/2 $ Hamilton directed cycles. Kelly's conjecture has been proved for tournaments of sufficiently large order by Kühn and Osthus [KO].

Bibliography

 [KO]
 Daniela Kühn and Deryk Osthus, Hamilton decompositions of regular expanders: a proof of Kelly's conjecture for large tournaments, Advances in Mathematics 237 (2013), 62-146.

★ [T]
 C. Thomassen, Edge-disjoint Hamiltonian paths and cycles in tournaments, Proc. London Math. Soc. 45 (1982), 151-168.
