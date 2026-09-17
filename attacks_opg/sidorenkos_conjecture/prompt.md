Attack the following open graph-theory problem.

Catalog id: sidorenkos_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/sidorenkos_conjecture/
Original entry: http://www.openproblemgarden.org/op/sidorenkos_conjecture
Problem attributed to: Sidorenko, A. (posted 2019-10-10)

=== Problem statement (OpenProblemGarden) ===
Title: Sidorenko's Conjecture
Conjecture For any bipartite graph $ H $ and graph $ G $ , the number of homomorphisms from $ H $ to $ G $ is at least $ \left(\frac{2|E(G)|}{|V(G)|^2}\right)^{|E(H)|}|V(G)|^{|V(H)|} $ .

=== Discussion / context (OpenProblemGarden) ===
A homomorphism from a graph $ H $ to a graph $ G $ is a mapping $ f:V(H)\to V(G) $ which preserves edges. Given graphs $ H $ and $ G $ , the homomorphism density of $ H $ in $ G $ , denoted $ t(H,G) $ , is the probability that a random function $ f:V(H)\to V(G) $ is a homomorphism. That is, $$t(H,G)=\frac{\left|\left\{f: V(H)\to V(G): f\text{ is a homomorphism from }H\text{ to }G\right\}\right|}{|V(G)|^{|V(H)|}}.$$ In this language, Sidorenko's Conjecture says that, if $ H $ is bipartite, then every graph $ G $ satisfies $$t(H,G)\geq t(K_2,G)^{|E(H)|}.$$ There are lots of results on Sidorenko's Conjecture; rather than listing them all here, we encourage the reader to see the references of the recent paper [CL].

=== References listed by OpenProblemGarden ===
- [CL] David Conlon and Joonkyung Lee: Sidorenko's conjecture for blow-ups, submitted.

=== Catalog page (statement + literature review) ===
Sidorenko's Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Sidorenko's conjecture remains open in full generality for all bipartite graphs. Since the OPG posting, the key referenced paper by Conlon and Lee was formally published in *Discrete Analysis* (2021), proving that every bipartite graph $H$ has some blow-up satisfying the conjecture. Im, Li, and Liu (2024) further extended known cases to graphs obtained by replacing edges of a complete graph with generalized theta graphs. The conjecture is still open for many specific bipartite graphs, including $K_{5,5}$ minus a perfect matching.

 Cited literature (5)

 
 
 
partial Sidorenko's conjecture for blow-ups
 (2021)
 

 
 David Conlon, Joonkyung Lee · Discrete Analysis · arXiv:1809.01259 · doi:10.19086/da.21472

For every bipartite graph H there exists a positive integer p such that the p-blow-up of H satisfies Sidorenko's conjecture; also proves the conjecture for all bipartite graphs whose degree sequence satisfies a certain divisibility condition.
 

 
 
partial Sidorenko's conjecture for subdivisions and theta substitutions
 (2024)
 

 
 Seonghyuk Im, Ruonan Li, Hong Liu · arXiv preprint · arXiv:2408.03491

Proves Sidorenko's conjecture for bipartite graphs obtained by replacing each edge of a complete graph with a generalized theta graph (with divisibility conditions), extending earlier subdivision results by Conlon, Kim, Lee, and Lee.
 

 
 
reduction Extremal numbers and Sidorenko's conjecture
 (2023)
 

 
 David Conlon, Joonkyung Lee, Alexander Sidorenko · arXiv preprint · arXiv:2307.04588

Shows that failures of Sidorenko's conjecture for uniform hypergraphs yield improved lower bounds on extremal numbers; identifies new hypergraph counterexamples to the conjecture.
 

 
 
partial Variations on Sidorenko's conjecture in tournaments
 (2024)
 

 
 Jacob Fox, Zoe Himwich, Nitya Mani, Yunkun Zhou · arXiv preprint · arXiv:2402.08418

Develops tournament analogues of Sidorenko's conjecture: proves asymptotically tight bounds on the maximum number of edges in a tournament anti-Sidorenko digraph, gives novel constructions of tournament Sidorenko digraphs, and fully characterises which orientations of stars are tournament Sidorenko or tournament anti-Sidorenko.
 

 
 
partial A note on directed analogues of the Sidorenko and forcing conjectures
 (2022)
 

 
 Jacob Fox, Zoe Himwich, Nitya Mani, Yunkun Zhou · arXiv preprint · arXiv:2210.16971

Proves two necessary conditions for the directed forcing property (Theorem 1.6) and shows that an oriented graph $B$ with a homomorphism $B \to \vec{K}_2$ has the directed forcing property if and only if its underlying undirected bipartite graph has the asymmetric forcing property (Theorem 1.8).
 

 

 Reviewer notes. The Conlon–Lee blow-ups paper (arXiv:1809.01259) was already circulating as a preprint from September 2018 and explicitly cited in the OPG entry as [CL] 'submitted'; the journal publication in Discrete Analysis (March 30, 2021) postdates the OPG posting. The Conlon–Lee–Sidorenko 2023 paper focuses on hypergraph analogs where the conjecture fails and resulting extremal number consequences; it is listed as 'reduction' rather than a partial result for the bipartite graph case. A 2025 paper (arXiv:2512.11222) on Sidorenko-type inequalities in tournaments addresses a directed analog and does not contribute to the original conjecture. The conjecture remains open for all bipartite graphs in full generality.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. For any bipartite graph $ H $ and graph $ G $ , the number of homomorphisms from $ H $ to $ G $ is at least $ \left(\frac{2|E(G)|}{|V(G)|^2}\right)^{|E(H)|}|V(G)|^{|V(H)|} $ .

Keywords:
density problems · extremal combinatorics · homomorphism

Discussion

A homomorphism from a graph $ H $ to a graph $ G $ is a mapping $ f:V(H)\to V(G) $ which preserves edges. Given graphs $ H $ and $ G $ , the homomorphism density of $ H $ in $ G $ , denoted $ t(H,G) $ , is the probability that a random function $ f:V(H)\to V(G) $ is a homomorphism. That is, $$t(H,G)=\frac{\left|\left\{f: V(H)\to V(G): f\text{ is a homomorphism from }H\text{ to }G\right\}\right|}{|V(G)|^{|V(H)|}}.$$ In this language, Sidorenko's Conjecture says that, if $ H $ is bipartite, then every graph $ G $ satisfies $$t(H,G)\geq t(K_2,G)^{|E(H)|}.$$ There are lots of results on Sidorenko's Conjecture; rather than listing them all here, we encourage the reader to see the references of the recent paper [CL].

Bibliography

 [CL]
 David Conlon and Joonkyung Lee: Sidorenko's conjecture for blow-ups , submitted.
 Sidorenko's conjecture for blow-ups
