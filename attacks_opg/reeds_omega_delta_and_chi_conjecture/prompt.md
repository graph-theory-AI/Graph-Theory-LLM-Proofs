Attack the following open graph-theory problem.

Catalog id: reeds_omega_delta_and_chi_conjecture
Source: OpenProblemGarden (importance: High ✭✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/reeds_omega_delta_and_chi_conjecture/
Original entry: http://www.openproblemgarden.org/op/reeds_omega_delta_and_chi_conjecture
Problem attributed to: Reed, Bruce A. (posted 2007-05-22)

=== Problem statement (OpenProblemGarden) ===
Title: Reed's omega, delta, and chi conjecture
For a graph $ G $ , we define $ \Delta(G) $ to be the maximum degree, $ \omega(G) $ to be the size of the largest clique subgraph, and $ \chi(G) $ to be the chromatic number of $ G $ . Conjecture $ \chi(G) \le \ceil{\frac{1}{2}(\Delta(G)+1) + \frac{1}{2}\omega(G)} $ for every graph $ G $ .

=== Discussion / context (OpenProblemGarden) ===
Perhaps the two most trivial bounds on $ \chi(G) $ are $ \chi(G) \ge \omega(G) $ and $ \chi(G) \le \Delta(G) + 1 $ . The above conjecture roughly asserts that the (rounded-up) average of $ \Delta(G)+1 $ and $ \omega(G) $ should again be an upper bound on $ \chi(G) $ . The conjecture is easy to verify when $ \omega(G) $ is very large. It is trivial when $ \omega(G) \ge \Delta(G) $ , and it follows from Brook's theorem if $ \omega(G) = \Delta(G)-1 $ . On the other hand, if $ \omega(G) = 2 $ , so $ G $ is triangle free, then the conjecture is also true for $ \Delta $ sufficiently large. Indeed, Johannsen proved the much stronger fact that there exists a fixed constant $ c $ so that $ \chi(G) \le \frac{c \Delta(G)}{\log \Delta(G)} $ for every triangle free graph $ G $ . Reed showed that the conjecture holds when $ \Delta(G) = |V(G)| - 1 $ by way of matching theory. More interestingly, he proved (using probabilistc methods) that the conjecture is true provided that $ \Delta $ is sufficiently large, and $ \omega $ is sufficiently close to $ \Delta $ . More precisely, he proves the following: Theorem There exists a fixed constant $ \Delta_0 $ such that for every $ \Delta \ge \Delta_0 $ , if $ G $ is a graph of maximum degree $ \Delta $ with no clique of size $ >k $ for some $ k \ge (1 - \frac{1}{70000000}) \Delta $ then $ \chi(G) \le \frac{\Delta + 1 + k}{2} $ . It is known that the conjecture is true fractionally (that is with $ \chi(G) $ replaced by $ \chi_f(G) $ , the fractional chromatic number of~ $ G $ ).

=== References listed by OpenProblemGarden ===
- *[R] B. Reed, , and , J. Graph Theory 27 (1998) 177-212.

=== Catalog page (statement + literature review) ===
Reed's omega, delta, and chi conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Reed's conjecture $\chi(G) \le \lceil \tfrac{1}{2}(\Delta(G)+1+\omega(G)) \rceil$ remains open for general graphs. Since the 2007 OPG posting, it has been established for quasi-line graphs and further structural classes, and the quantitative 'epsilon version' $\chi(G) \le (1-\varepsilon)(\Delta+1) + \varepsilon\,\omega$ has been progressively strengthened from $\varepsilon \approx 1/130{,}000$ to $\varepsilon = 1/26$ and reportedly further to $\varepsilon \approx 0.119$.

 Cited literature (5)

 
 
 
partial A local strengthening of Reed's ω, Δ, χ conjecture for quasi-line graphs
 (2011)
 

 
 Maria Chudnovsky, Andrew D. King, Matthieu Plumettaz, Paul Seymour · SIAM Journal on Discrete Mathematics · arXiv:1109.2112

Proves a local strengthening of Reed's conjecture for all quasi-line graphs (including line graphs), along with polytime colouring algorithms.
 

 
 
partial A note on Reed's Conjecture about ω, Δ and χ with respect to vertices of high degree
 (2016)
 

 
 Vera Weil · arXiv preprint · arXiv:1611.02063

Proves Reed's conjecture for graphs in which all vertices of degree ≥ 5 form a stable set, and for graphs in which every odd induced cycle contains a vertex of degree ≤ 3.
 

 
 
partial Colouring Graphs with Sparse Neighbourhoods: Bounds and Applications
 (2018)
 

 
 Marthe Bonamy, Thomas Perrett, Luke Postle · arXiv preprint · arXiv:1810.06704

Dramatically improves Reed's epsilon theorem by showing the bound χ(G) ≤ (1−ε)(Δ+1) + ε·ω holds for large Δ with ε = 1/26, up from the prior ε ≈ 1/130,000.
 

 
 
partial A local epsilon version of Reed's Conjecture
 (2019)
 

 
 Tom Kelly, Luke Postle · Journal of Combinatorial Theory, Series B · arXiv:1911.02672

Proves a local list-colouring epsilon version of Reed's conjecture, establishing the bound under mild local density conditions.
 

 
 
partial A Recolouring Version of a Conjecture of Reed
 (2025)
 

 
 Lucas De Meyer, Clément Legrand-Duchesne, Jared León, Tim Planken, Youri Tamitegama · arXiv preprint · arXiv:2502.10147

Studies a Kempe-recolouring variant of Reed's conjecture; proves the analogous bound with ε = 1/2 is achievable for odd-hole-free graphs (and tight up to one colour).
 

 

 Reviewer notes. The conjecture remains open for general graphs. An important unverified result: Hurley, de Verclos, and Kang (SODA 2021) reportedly improved the epsilon to ε ≈ 0.119 ('An improved procedure for colouring graphs of bounded local density'), but this paper was not fetched within the query budget and cannot be cited. The digraph analogue by Kawarabayashi–Picasarri-Arrieta (arXiv 2407.05827, 2024) is not included in since_posted as it concerns directed graphs. The SIAM journal publication of the Chudnovsky et al. paper (DOI 10.1137/110847585 per search results) is likely 2012–2013; only the 2011 arXiv submission was directly verified.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. $ \chi(G) \le \ceil{\frac{1}{2}(\Delta(G)+1) + \frac{1}{2}\omega(G)} $ for every graph $ G $ .

Keywords:
coloring

Discussion

Perhaps the two most trivial bounds on $ \chi(G) $ are $ \chi(G) \ge \omega(G) $ and $ \chi(G) \le \Delta(G) + 1 $ . The above conjecture roughly asserts that the (rounded-up) average of $ \Delta(G)+1 $ and $ \omega(G) $ should again be an upper bound on $ \chi(G) $ . The conjecture is easy to verify when $ \omega(G) $ is very large. It is trivial when $ \omega(G) \ge \Delta(G) $ , and it follows from Brook's theorem if $ \omega(G) = \Delta(G)-1 $ . On the other hand, if $ \omega(G) = 2 $ , so $ G $ is triangle free, then the conjecture is also true for $ \Delta $ sufficiently large. Indeed, Johannsen proved the much stronger fact that there exists a fixed constant $ c $ so that $ \chi(G) \le \frac{c \Delta(G)}{\log \Delta(G)} $ for every triangle free graph $ G $ . Reed showed that the conjecture holds when $ \Delta(G) = |V(G)| - 1 $ by way of matching theory. More interestingly, he proved (using probabilistc methods) that the conjecture is true provided that $ \Delta $ is sufficiently large, and $ \omega $ is sufficiently close to $ \Delta $ . More precisely, he proves the following: Theorem There exists a fixed constant $ \Delta_0 $ such that for every $ \Delta \ge \Delta_0 $ , if $ G $ is a graph of maximum degree $ \Delta $ with no clique of size $ >k $ for some $ k \ge (1 - \frac{1}{70000000}) \Delta $ then $ \chi(G) \le \frac{\Delta + 1 + k}{2} $ . It is known that the conjecture is true fractionally (that is with $ \chi(G) $ replaced by $ \chi_f(G) $ , the fractional chromatic number of~ $ G $ ).

Bibliography

★ [R]
 B. Reed, $ \omega, \Delta $ , and $ \chi $ , J. Graph Theory 27 (1998) 177-212.

Related conjectures

 
 implies
 Bounding the chromatic number of triangle-free graphs with fixed maximum degree
 open
 Triangle-free means omega(G) <= 2. Reed's conjectured bound then gives chi <= ceil((Delta+1)/2 + 1) = ceil((Delta+3)/2). For even Delta this equals Delta/2 + 2 = ceil(Delta/2)+2; for odd Delta it equals (Delta+3)/2 = ceil(Delta/2)+1 <= ceil(Delta/2)+2. So Reed's conjecture (source) implies the triangle-free conjecture (target) by restriction to omega <= 2, with the correct rounding check. The target's own Open Problem Garden context states explicitly: 'This conjecture is a special case of Reed's omega, Delta, and chi conjecture.' Direction as claimed.
 

 
 implied by
 List-chromatic Reed bound
 open
 For every graph, chi(G) <= chi_ell(G): the list chromatic number is defined over all list assignments, including the one giving every vertex the same list {1,...,k}, so a list-coloring bound is at least as strong as the corresponding chromatic-number bound. Hence chi_ell(G) <= ceil((Delta+1+omega)/2) for all G immediately gives chi(G) <= ceil((Delta+1+omega)/2), which is exactly Reed's conjecture. Hypothesis classes are identical (all graphs, same Delta and omega parameters); only the colouring parameter is weakened. Direction as claimed: the list version is the stronger statement.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.
