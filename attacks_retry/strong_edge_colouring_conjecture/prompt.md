Attack the following open graph-theory problem.

Catalog id: strong_edge_colouring_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/strong_edge_colouring_conjecture/
Original entry: http://www.openproblemgarden.org/op/strong_edge_colouring_conjecture
Problem attributed to: Erdos, Paul, Nesetril, Jaroslav (posted 2013-03-01)

=== Problem statement (OpenProblemGarden) ===
Title: Strong edge colouring conjecture
A strong edge-colouring of a graph $ G $ is a edge-colouring in which every colour class is an induced matching; that is, any two vertices belonging to distinct edges with the same colour are not adjacent. The strong chromatic index $ s\chi'(G) $ is the minimum number of colours in a strong edge-colouring of $ G $ . Conjecture $$s\chi'(G) \leq \frac{5\Delta^2}{4}, \text{if $\Delta$ is even,}$$ $$s\chi'(G) \leq \frac{5\Delta^2-2\Delta +1}{4},&\text{if $\Delta$ is odd.}$$

=== Discussion / context (OpenProblemGarden) ===
The conjectured bounds would be sharp. When $ D $ is even, expanding each vertex of a $ 5 $ -cycle into a stable set of size $ \Delta/2 $ yields such a graph with $ 5\Delta^2/4 $ edges in which the largest induced matching has size $ 1 $ . A similar construction achieves the bound when $ \Delta $ is odd. Greedy colouring the edges yields $ s\chi'(G) \leq 2\Delta(\Delta-1)+1 $ . Using probabilistic methods, Molloy and Reed~[MoRe97] proved that there is a positive constant $ \epsilon $ such that, for sufficiently large $ \Delta $ , every graph with maximum degree $ \Delta $ has strong chromatic index at most $ (2-\epsilon)\Delta^2 $ . The greedy bound proves the conjecture for $ \Delta \leq 2 $ . For $ \Delta =3 $ , the conjectured bound of 10 was proved independently by Hor\'ak, He, and Trotter[HHT] and by Andersen [A]. For $ \Delta=4 $ , the conjectured bound is 20, and Cranston [C] proved that 22 colours suffice. For a bipartite graph $ G $ , Faudree et al. [FGST] conjectured that $ s\chi'(G)\leq \Delta^2(G) $ . This is implied by the stronger conjecture due to Kaiser. Conjecture Let $ G=((A_1,A_2),E) $ be a bipartite graph such that every vertex in $ A_1 $ has degree at most $ \Delta_1 $ and every vertex in $ A_2 $ has degree at most $ \Delta_2 $ . Then $ s\chi'(G)\leq \Delta_1\Delta_2 $ .

=== References listed by OpenProblemGarden ===
- [A] L. D. Andersen. The strong chromatic index of a cubic graph is at most 10. Discrete Math., 108(1-3):231--252, 1992.
- [C] D. W. Cranston. Strong edge-coloring of graphs with maximum degree 4 using 22 colors. Discrete Math., 306(21):2772--2778, 2006.
- [FGST] R. J. Faudree, A. Gyárfás, R. H. Schelp, and Zs. Tuza. Induced matchings in bipartite graphs. Discrete Math., 78(1-2):83--87, 1989.
- [HHT] P. Horák, Q. He, and W. T. Trotter. Induced matchings in cubic graphs. J. Graph Theory, 17(2):151--160, 1993.

=== Catalog page (statement + literature review) ===
Strong edge colouring conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Erdős–Nešetřil strong edge-colouring conjecture ($s\chi'(G) \leq \frac{5\Delta^2}{4}$ for even $\Delta$) remains open. The best asymptotic bound for large $\Delta$ is $1.93\Delta^2$ (Bruhn–Joos, 2018), improving the earlier $(2-\varepsilon)\Delta^2$ of Molloy–Reed. For $\Delta=4$ the conjectured bound of 20 is still unresolved; the current best is 21 colors (Huang–Santana–Yu, 2018).

 Cited literature (3)

 
 
 
partial A Stronger Bound for the Strong Chromatic Index
 (2018)
 

 
 Henning Bruhn, Felix Joos · Combinatorics, Probability and Computing · arXiv:1504.02583 · doi:10.1017/S0963548317000244

Proves $\chi'_s(G) \leq 1.93\Delta(G)^2$ for graphs with sufficiently large maximum degree, strictly improving the $(2-\varepsilon)\Delta^2$ bound of Molloy and Reed.
 

 
 
partial Strong chromatic index of graphs with maximum degree four
 (2018)
 

 
 Mingfang Huang, Michael Santana, Gexin Yu · arXiv preprint · arXiv:1806.07012

Proves $\chi'_s(G) \leq 21$ for graphs with maximum degree 4, improving Cranston's 2006 bound of 22; the conjectured bound of 20 remains open.
 

 
 
partial The strong chromatic index of $(3,\Delta)$-bipartite graphs
 (2018)
 

 
 Mingfang Huang, Gexin Yu, Xiangqian Zhou · arXiv preprint · arXiv:1806.07017

Proves that every bipartite graph with one part of maximum degree at most 3 and the other of maximum degree $\Delta$ admits a strong edge-colouring with at most $3\Delta$ colours, confirming the Brualdi–Quinn Massey conjecture for this class.
 

 

 Reviewer notes. The Bruhn–Joos paper was submitted to arXiv in April 2015 (after the 2013-03-01 posting date) and published in CPC in 2018; year listed as 2018. Huang–Santana–Yu (1806.07012) is listed as an arXiv preprint; journal publication not confirmed. For 1806.07017 the fetched content mentioned 'published in Discrete Mathematics, 2017', conflicting with the June 2018 arXiv submission date — possible extraction error; treated as 2018 arXiv preprint. Cames van Batenburg et al. (2019, arXiv:1905.06031) on K_4-minor-free graphs is a tangential partial result and was not included in since_posted. No complete proof or disproof was found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 08) (web search enabled).
 

Conjecture. $$s\chi'(G) \leq \frac{5\Delta^2}{4}, \text{if $\Delta$ is even,}$$ $$s\chi'(G) \leq \frac{5\Delta^2-2\Delta +1}{4},&\text{if $\Delta$ is odd.}$$

Discussion

The conjectured bounds would be sharp. When $ D $ is even, expanding each vertex of a $ 5 $ -cycle into a stable set of size $ \Delta/2 $ yields such a graph with $ 5\Delta^2/4 $ edges in which the largest induced matching has size $ 1 $ . A similar construction achieves the bound when $ \Delta $ is odd. Greedy colouring the edges yields $ s\chi'(G) \leq 2\Delta(\Delta-1)+1 $ . Using probabilistic methods, Molloy and Reed~[MoRe97] proved that there is a positive constant $ \epsilon $ such that, for sufficiently large $ \Delta $ , every graph with maximum degree $ \Delta $ has strong chromatic index at most $ (2-\epsilon)\Delta^2 $ . The greedy bound proves the conjecture for $ \Delta \leq 2 $ . For $ \Delta =3 $ , the conjectured bound of 10 was proved independently by Hor\'ak, He, and Trotter[HHT] and by Andersen [A]. For $ \Delta=4 $ , the conjectured bound is 20, and Cranston [C] proved that 22 colours suffice. For a bipartite graph $ G $ , Faudree et al. [FGST] conjectured that $ s\chi'(G)\leq \Delta^2(G) $ . This is implied by the stronger conjecture due to Kaiser. Conjecture Let $ G=((A_1,A_2),E) $ be a bipartite graph such that every vertex in $ A_1 $ has degree at most $ \Delta_1 $ and every vertex in $ A_2 $ has degree at most $ \Delta_2 $ . Then $ s\chi'(G)\leq \Delta_1\Delta_2 $ .

Bibliography

 [A]
 L. D. Andersen. The strong chromatic index of a cubic graph is at most 10. Discrete Math., 108(1-3):231--252, 1992.

 [C]
 D. W. Cranston. Strong edge-coloring of graphs with maximum degree 4 using 22 colors. Discrete Math., 306(21):2772--2778, 2006.

 [FGST]
 R. J. Faudree, A. Gyárfás, R. H. Schelp, and Zs. Tuza. Induced matchings in bipartite graphs. Discrete Math., 78(1-2):83--87, 1989.

 [HHT]
 P. Horák, Q. He, and W. T. Trotter. Induced matchings in cubic graphs. J. Graph Theory, 17(2):151--160, 1993.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds, even for strong list edge-colouring, for every independent-set blow-up of a pseudoforest.",
  "would_publish": false,
  "caveats": "This is a special-case result only; no novelty claim or improved bound for arbitrary graphs is made."
}
```

## 1. A sharp special-case theorem

Write
\[
B(\Delta)=\Delta^2+\left\lfloor\frac{\Delta}{2}\right\rfloor^2.
\]
This is precisely the conjectured bound, including its odd-degree correction.

A **pseudoforest** is a graph in which every connected component contains at most one cycle. An **independent-set blow-up** of a graph \(H\) is obtained by replacing each vertex \(v\) with a nonempty independent set \(A_v\), and replacing each edge \(uv\) with all edges between \(A_u\) and \(A_v\). No other edges are added.

The underlying pseudoforest and the part sizes below may be arbitrary.

**Theorem.** Let \(G\) be an independent-set blow-up of a finite simple pseudoforest, and let \(\Delta=\Delta(G)\ge 1\). Then
\[
L(G)^2\text{ is }(B(\Delta)-1)\text{-degenerate}.
\]
Consequently,
\[
s\chi'(G)\le B(\Delta).
\]
In fact, a strong edge-colouring exists whenever each edge is assigned its own list of at least \(B(\Delta)\) permissible colours.

If the underlying graph is a forest, the stronger bound \(\Delta^2\) holds, also for lists.

The theorem is sharp for every \(\Delta\). I give a self-contained proof; I do not claim this special-case result is new.

## 2. Conflict graphs and edge bundles

The **conflict graph** of \(G\) is
\[
J=L(G)^2.
\]
Its vertices are the edges of \(G\); two distinct vertices are adjacent when the corresponding edges share an endpoint or have adjacent endpoints. Thus strong edge-colouring is exactly proper vertex-colouring of \(J\).

Put
\[
a_v=|A_v|,
\qquad
d_v=\sum_{w\in N_H(v)}a_w.
\]
Every vertex of \(A_v\) has degree \(d_v\), so \(d_v\le\Delta\).

For \(uv\in E(H)\), let \(E_{uv}\) denote the **bundle** consisting of all \(a_ua_v\) edges between \(A_u\) and \(A_v\). Each bundle is a clique in \(J\). Moreover, the conflict relation between two bundles is uniform: either every edge of one conflicts with every edge of the other, or no such pair conflicts. The former occurs exactly when the corresponding edges of \(H\) have distance at most two in \(L(H)\).

We will delete vertices of the fixed conflict graph \(J\), bundle by bundle. At every deletion, the selected vertex will have at most \(B(\Delta)-1\) remaining neighbours. Reverse greedy colouring then proves the theorem, including its list version.

Importantly, deleting a bundle does **not** erase conflicts between other bundles that were mediated by it.

## 3. Removing leaf classes costs at most \(\Delta^2\)

Suppose that \(u\) is a leaf of the current underlying graph, with neighbour \(v\). Consider an edge \(e\in E_{uv}\).

Every edge in the closed conflict neighbourhood of \(e\) belongs either to a bundle incident with \(v\), or to a bundle incident with some
\[
w\in N_H(v)\setminus\{u\}.
\]
Therefore
\[
\begin{aligned}
|N_J[e]|
&\le
a_vd_v+
\sum_{w\in N_H(v)\setminus\{u\}}
a_w(d_w-a_v)\\
&\le
a_v\Delta+(\Delta-a_v)(d_v-a_u)\\
&\le \Delta^2.
\end{aligned}
\tag{1}
\]
Here the first expression may count an edge more than once, which is harmless. Also \(a_v=d_u\le\Delta\), so the coefficient \(\Delta-a_v\) is nonnegative.

Thus every edge of this leaf bundle has at most \(\Delta^2-1\) remaining conflicts. We may delete the entire bundle in any order, and then remove the now-isolated class \(A_u\).

After removing \(A_u\), conflicts among retained edges are exactly those in the induced graph \(G-A_u\): whether two retained edges conflict depends only on their endpoints and edges joining those endpoints. Hence we may apply (1) repeatedly, using the original \(\Delta\) throughout.

For a pseudoforest, this stripping process leaves only isolated vertices and cycle components. For a forest it removes every edge, already proving the \(\Delta^2\) assertion.

It remains to handle blow-ups of cycles.

## 4. Cycle blow-ups: a three-phase elimination order

Consider a cycle blow-up with classes
\[
A_0,\ldots,A_{n-1},
\qquad |A_i|=a_i,
\]
where indices are cyclic and
\[
a_{i-1}+a_{i+1}\le\Delta.
\tag{2}
\]
Set
\[
k=\left\lfloor\frac{\Delta}{2}\right\rfloor,
\qquad B=\Delta^2+k^2.
\]

### Short cycles

If \(n=3\) or \(4\), the number \(m\) of edges satisfies
\[
\begin{aligned}
m
&=\frac12\sum_i a_i(a_{i-1}+a_{i+1})\\
&\le \frac{\Delta}{2}\sum_i a_i
\le \frac{n\Delta^2}{4}
\le\Delta^2.
\end{aligned}
\]
The penultimate inequality follows by summing (2). Consequently the conflict graph has at most \(\Delta^2\) vertices, and any elimination order suffices.

Henceforth assume \(n\ge5\).

### The five-bundle neighbourhood

Let \(E_i\) be the bundle between \(A_i\) and \(A_{i+1}\). An edge in \(E_i\) conflicts exactly with the edges in
\[
E_{i-2},E_{i-1},E_i,E_{i+1},E_{i+2}.
\]

For a selected bundle \(E_i\), abbreviate
\[
(r,p,x,y,q,s)
=
(a_{i-2},a_{i-1},a_i,a_{i+1},a_{i+2},a_{i+3}).
\]
For \(n=5\), \(r=s\); all subsequent estimates remain valid. By (2),
\[
r+x\le\Delta,\quad
p+y\le\Delta,\quad
x+q\le\Delta,\quad
y+s\le\Delta.
\tag{3}
\]
Before any deletions, the closed conflict neighbourhood of an edge in this bundle has size
\[
S=rp+px+xy+yq+qs
  =p(r+x)+xy+q(y+s).
\tag{4}
\]

Call a class **large** if its size exceeds \(k\), and **small** otherwise. Delete bundles in the following three phases.

### Phase I: large–large bundles

Suppose \(x,y\ge k+1\). Equations (3)–(4) give
\[
\begin{aligned}
S
&\le \Delta(p+q)+xy\\
&\le \Delta(2\Delta-x-y)+xy\\
&=\Delta^2+(\Delta-x)(\Delta-y)\\
&\le\Delta^2+k^2=B.
\end{aligned}
\tag{5}
\]
Indeed, every nonisolated class has size at most \(\Delta\), and
\[
0\le \Delta-x,\Delta-y\le k.
\]

Thus all large–large bundles can be deleted, in arbitrary order, with closed remaining conflict neighbourhoods of size at most \(B\).

### Phase II: large–small bundles

Orient the selected bundle so that
\[
x\ge k+1,\qquad y\le k.
\]
There are two cases, according to the size \(p\) of the other class adjacent to \(A_i\).

**Case A: \(p\le k\).** Even the original closed conflict neighbourhood satisfies
\[
\begin{aligned}
S
&\le p\Delta+xy+q\Delta\\
&\le k\Delta+xk+(\Delta-x)\Delta\\
&=\Delta^2+k\Delta-x(\Delta-k)\\
&\le \Delta^2+k^2=B,
\end{aligned}
\tag{6}
\]
where the last inequality uses \(x\ge k\).

**Case B: \(p\ge k+1\).** The bundle of size \(px\) was deleted in Phase I. Hence the remaining closed conflict neighbourhood has size at most
\[
rp+xy+yq+qs.
\]
Using (3),
\[
\begin{aligned}
rp+xy+yq+qs
&\le p(\Delta-x)+xy+q\Delta\\
&\le(\Delta-x)(2\Delta-y)+xy\\
&=\Delta^2-(2x-\Delta)(\Delta-y)\\
&\le\Delta^2.
\end{aligned}
\tag{7}
\]
The last inequality holds because \(x\ge k+1\) implies \(2x\ge\Delta\).

Thus all large–small bundles can also be deleted in arbitrary order.

### Phase III: small–small bundles

Every remaining bundle has at most \(k^2\) edges. Each closed conflict neighbourhood meets at most five bundles, so its size is at most
\[
5k^2\le\Delta^2+k^2=B.
\tag{8}
\]

This completes the elimination order for every cycle blow-up.

### Completing the proof

First use the leaf-class deletions from Section 3. Then apply the cycle elimination order independently to each remaining component. Isolated classes have no edges to colour.

At every step the closed remaining conflict neighbourhood has size at most \(B\). Thus each deleted vertex has at most \(B-1\) remaining neighbours, proving that \(J\) is \((B-1)\)-degenerate.

Colouring in reverse order uses at most \(B\) colours. With individual lists of size \(B\), at most \(B-1\) colours are forbidden when an edge is coloured, so the same argument works without modification. ∎

## 5. Sharpness within this class

The standard extremal examples are already cycle blow-ups, so no better universal bound is possible for the class just treated.

Every two edges in a blow-up of \(C_5\) conflict. Its strong chromatic index therefore equals its number of edges.

If \(\Delta=2k\), take all five classes to have size \(k\). Then
\[
s\chi'(G)=5k^2=B(\Delta).
\]

If \(\Delta=2k+1\), where \(k\ge1\), use cyclic class sizes
\[
(k+1,k+1,k,k,k).
\]
The maximum degree is \(2k+1\), and
\[
\begin{aligned}
s\chi'(G)
&=(k+1)^2+2k(k+1)+2k^2\\
&=5k^2+4k+1\\
&=(2k+1)^2+k^2
=B(\Delta).
\end{aligned}
\]
For \(\Delta=1\), a single edge gives equality; the edgeless case is trivial.

## 6. What remains unresolved

This proves the conjecture for blow-ups of arbitrary pseudoforests, not for arbitrary graphs. The leaf-class argument stops when the underlying graph has a non-cyclic, branching \(2\)-core. There, a bundle can conflict with bundles along several branches, and the five-bundle calculation is unavailable.

Moreover, the stronger degeneracy conclusion cannot hold generally. If \(G\) is \(\Delta\)-regular with girth at least five, then every edge has
\[
2(\Delta-1)+2(\Delta-1)^2
=2\Delta(\Delta-1)
\]
neighbours in \(L(G)^2\). The girth condition prevents collisions in this count. Thus \(L(G)^2\) is regular of that degree, and its degeneracy is
\[
2\Delta(\Delta-1)>B(\Delta)-1
\qquad(\Delta\ge3).
\]
Such graphs include, for example, the cubic Petersen graph.

This is not a counterexample to the colouring conjecture: chromatic number can be much smaller than degeneracy. It shows precisely why the elimination method above, despite being sharp on the stated subclass, cannot by itself settle the general Erdős–Nešetřil conjecture.
