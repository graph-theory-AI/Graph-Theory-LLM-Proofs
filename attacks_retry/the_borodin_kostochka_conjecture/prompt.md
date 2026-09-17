Attack the following open graph-theory problem.

Catalog id: the_borodin_kostochka_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_borodin_kostochka_conjecture/
Original entry: http://www.openproblemgarden.org/op/the_borodin_kostochka_conjecture
Problem attributed to: Borodin, Oleg V., Kostochka, Alexandr V. (posted 2012-09-10)

=== Problem statement (OpenProblemGarden) ===
Title: The Borodin-Kostochka Conjecture
Conjecture Every graph with maximum degree $ \Delta \geq 9 $ has chromatic number at most $ \max\{\Delta-1, \omega\} $ .

=== Discussion / context (OpenProblemGarden) ===
The Borodin-Kostochka conjecture proposes that for any graph $ G $ with maximum degree $ \Delta $ and clique number $ \omega < \Delta $ , $ G $ is $ \Delta-1 $ colourable so long as $ \Delta $ is sufficiently large (specifically, $ \Delta\geq 9 $ ). The requirement that $ \Delta \geq 9 $ is necessary, as one can see by looking at the strong product of $ C_5 $ and $ K_3 $ . Reed [R] proved that there exists a $ \Delta_0 $ for which the conjecture holds whenever $ \Delta \geq \Delta_0 $ . Specifically he proved that $ \Delta_0 \leq 10^{14} $ , but claims that more careful analysis could reduce $ \Delta_0 $ to 1000. The conjecture was recently proven by Cranston and Rabern for claw-free graphs [CR]. In their paper they mention an unpublished strengthening proposed by Borodin and Kostochka, namely that one can replace the chromatic number in the statement of the conjecture with the list chromatic number.

=== References listed by OpenProblemGarden ===
- [BK] O. V. Borodin and A. V. Kostochka. On an upper bound of a graph's chromatic number, depending on the graph's degree and density. JCTB 23 (1977), 247--250.
- [CR] D. W. Cranston and L. Rabern. Coloring claw-free graphs with colors, arXiv 1206.1269, 2012.
- [R] B. A. Reed. A strengthening of Brooks’ Theorem. J. Comb. Theory Ser. B, 76:136–149, 1999.

=== Catalog page (statement + literature review) ===
The Borodin-Kostochka Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Borodin–Kostochka conjecture remains open for general graphs with $\Delta \ge 9$. Since the problem was posted, the conjecture has been verified for several hereditary graph classes ($(P_5,\text{gem})$-free, $(P_6,\text{apple,torch})$-free, and others), and the unconditional degree threshold has been reduced from Reed's $\Delta_0 \le 10^{14}$ to $\Delta \ge 5.2\times10^9$ in 2026; a companion 2026 paper also establishes the analogue for correspondence (DP) coloring at $\Delta \ge 3\times10^9$.

 Cited literature (8)

 
 
 
partial Coloring $(P_5, \text{gem})$-free graphs with $\Delta-1$ colors
 (2022)
 

 
 Daniel W. Cranston, Hudson Lafayette, Landon Rabern · Journal of Graph Theory · arXiv:2006.02015

Proves the Borodin–Kostochka conjecture for $(P_5,\text{gem})$-free graphs: if $\Delta(G)\ge 9$ and $\omega(G)\le\Delta(G)-1$ then $\chi(G)\le\Delta(G)-1$.
 

 
 
partial Validity of Borodin and Kostochka Conjecture for classes of graphs without a single, forbidden subgraph on 5 vertices
 (2021)
 

 
 Medha Dhurandhar · arXiv preprint · arXiv:2101.01354

Verifies the conjecture for $(P_4\cup K_1)$-free, $P_5$-free, Chair-free, and graphs with dense neighborhoods.
 

 
 
partial Borodin-Kostochka conjecture for a family of $P_6$-free graphs
 (2023)
 

 
 Di Wu, Rong Wu · arXiv preprint · arXiv:2306.12062

Proves the conjecture for $(P_6,\text{apple,torch})$-free graphs, extending the known result for $(P_5,C_4)$-free graphs.
 

 
 
partial Coloring some $(P_6,C_4)$-free graphs with $\Delta-1$ colors
 (2024)
 

 
 Ran Chen, Di Wu, Xiaowen Zhang · arXiv preprint · arXiv:2405.18455

Proves the conjecture for $(P_6,C_4,H)$-free graphs where $H\in\{K_7,C_5^+\}$.
 

 
 
partial On graphs with chromatic number and maximum degree both equal to nine
 (2024)
 

 
 Rachel Galindo, Jessica McDonald · arXiv preprint · arXiv:2408.12693

Proves structural results in support of the $\Delta=9$ base case of the conjecture, showing that vertex-critical graphs satisfying certain conditions must contain $K_3\vee\overline{K_6}$.
 

 
 
partial On the Borodin–Kostochka conjecture for graphs with large maximum degree
 (2026)
 

 
 Feng Liu, Shuang Sun, Yan Wang · arXiv preprint · arXiv:2603.16670

Reduces the unconditional threshold: every graph with $\Delta\ge 5.2\times10^9$ and $\omega(G)<\Delta$ satisfies $\chi(G)\le\Delta-1$, improving Reed's 1999 bound of $\Delta_0\le 10^{14}$.
 

 
 
partial On Borodin-Kostochka conjecture for correspondence coloring
 (2026)
 

 
 Zděněk Dvořák, Ross J. Kang, David Mikšaník · arXiv preprint · arXiv:2603.14427

Proves that for $\Delta\ge 3\times10^9$, every graph satisfies $\chi_{\mathrm{DP}}(G)\le\max(\omega(G),\Delta-1)$, establishing the correspondence-coloring analogue of the conjecture for large degree.
 

 
 
partial On Borodin-Kostochka conjecture for correspondence coloring
 (2026)
 

 
 Zdeněk Dvořák, Ross J. Kang, David Mikšaník · arXiv preprint · arXiv:2603.14427

Proves the conjecture for the stronger correspondence chromatic number $\chi_{DP}$, showing that for every graph $G$ with $\Delta(G)\geq 3\cdot 10^9$, $\chi_{DP}(G)\leq\max(\omega(G),\Delta(G)-1)$.
 

 

 Reviewer notes. The conjecture is definitively still open in general. A ScienceDirect paper on the list-chromatic version (S0012365X22005064) and a paper on K_{1,3}-bar-free graphs (S0166218X2400266X) returned HTTP 403 and could not be verified; they are not cited. The arXiv paper 2101.01354 by Dhurandhar is not peer-reviewed and should be treated with appropriate caution. The 2026 papers (2603.16670 and 2603.14427) are preprints not yet journal-published as of this review date.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. Every graph with maximum degree $ \Delta \geq 9 $ has chromatic number at most $ \max\{\Delta-1, \omega\} $ .

Discussion

The Borodin-Kostochka conjecture proposes that for any graph $ G $ with maximum degree $ \Delta $ and clique number $ \omega < \Delta $ , $ G $ is $ \Delta-1 $ colourable so long as $ \Delta $ is sufficiently large (specifically, $ \Delta\geq 9 $ ). The requirement that $ \Delta \geq 9 $ is necessary, as one can see by looking at the strong product of $ C_5 $ and $ K_3 $ . Reed [R] proved that there exists a $ \Delta_0 $ for which the conjecture holds whenever $ \Delta \geq \Delta_0 $ . Specifically he proved that $ \Delta_0 \leq 10^{14} $ , but claims that more careful analysis could reduce $ \Delta_0 $ to 1000. The conjecture was recently proven by Cranston and Rabern for claw-free graphs [CR]. In their paper they mention an unpublished strengthening proposed by Borodin and Kostochka, namely that one can replace the chromatic number in the statement of the conjecture with the list chromatic number.

Bibliography

 [BK]
 O. V. Borodin and A. V. Kostochka. On an upper bound of a graph's chromatic number, depending on the graph's degree and density. JCTB 23 (1977), 247--250.

 [CR]
 D. W. Cranston and L. Rabern. Coloring claw-free graphs with $ \Delta-1 $ colors , arXiv 1206.1269, 2012.
 Coloring claw-free graphs with colors

 [R]
 B. A. Reed. A strengthening of Brooks’ Theorem. J. Comb. Theory Ser. B, 76:136–149, 1999.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when |V(G)| ≤ 2Δ(G)−1; at Δ=8 and |V(G)|≤15, the only exception to the same bound is C5[K3].",
  "would_publish": false,
  "caveats": "This is an order-restricted result, not a resolution of the conjecture; no novelty is claimed, and the proof uses Gallai's classical decomposition theorem."
}
```

# A small-order partial result

All graphs below are finite and simple. Write \(C_5[K_3]\) for the graph obtained by replacing each vertex of a 5-cycle by a 3-clique, with complete adjacency between consecutive cliques.

I prove the following restricted version.

**Theorem 1.** Let \(G\) have maximum degree \(\Delta\).
1. If \(\Delta\ge 9\) and
   \[
   |V(G)|\le 2\Delta-1,
   \]
   then
   \[
   \chi(G)\le \max\{\Delta-1,\omega(G)\}.
   \]
2. If \(\Delta=8\) and \(|V(G)|\le15\), the only graph violating the same inequality is \(C_5[K_3]\).

Thus any counterexample to Borodin–Kostochka has at least \(2\Delta\) vertices. The unrestricted conjecture is not proved here.

The argument establishes the following more precise critical-graph statement.

**Theorem 2.** Suppose \(k\ge8\), and \(H\) is vertex-critical with
\[
\chi(H)=k,\qquad \Delta(H)\le k,\qquad |V(H)|\le2k-1.
\]
Then either \(H=K_k\), or \(k=8\) and \(H\cong C_5[K_3]\).

Here vertex-critical means that \(\chi(H-v)=k-1\) for every vertex \(v\).

## 1. Critical graphs and Gallai decomposition

I use the classical Gallai decomposition theorem in the following standard form:

> If a vertex-critical graph \(J\) has connected complement, then
> \[
> |V(J)|\ge2\chi(J)-1.
> \]

Recall also that an \(r\)-critical graph has minimum degree at least \(r-1\).

Let \(J\) be \(r\)-critical, and let \(J_1,\dots,J_m\) be the induced subgraphs corresponding to the components of \(\overline J\). Thus \(J\) is their complete join. Put
\[
r_i=\chi(J_i),\qquad n_i=|V(J_i)|,\qquad t_i=n_i-r_i.
\]
Join additivity of chromatic number gives
\[
r=\sum_i r_i,
\]
and each \(J_i\) is vertex-critical.

If \(J_i\) is not a singleton, then \(r_i\ge3\): the only 2-critical graph is \(K_2\), whose complement is disconnected. Gallai's theorem therefore gives
\[
t_i\ge r_i-1\ge2. \tag{1}
\]

For \(v\in V(J_i)\),
\[
d_J(v)\ge r_i-1+\sum_{j\ne i}n_j
=r-1+\sum_{j\ne i}t_j.
\]
Consequently, if \(\Delta(J)\le r+s\), then
\[
\sum_{j\ne i}t_j\le s+1
\qquad\text{for every }i. \tag{2}
\]

Two consequences will be useful.

**Lemma 3.**
1. If \(J\) is noncomplete, \(r\)-critical, and \(\Delta(J)\le r\), then \(\overline J\) is connected and \(|V(J)|\ge2r-1\).
2. If \(r\ge7\), \(J\) is \(r\)-critical, \(\Delta(J)\le r+1\), and \(|V(J)|\le2r-2\), then
   \[
   J=K_r
   \quad\text{or}\quad
   J=K_{r-3}\vee C_5.
   \]

**Proof.**

For part 1, suppose \(m\ge2\). If one complement component is nonsingleton, its \(t_j\ge2\), contradicting (2) with \(s=0\) and \(i\ne j\). Thus all components are singletons, making \(J\) complete. Gallai's theorem now gives the order bound.

For part 2, Gallai's theorem implies \(m\ge2\). By (2), the sum of the \(t_j\)'s outside any one component is at most 2.

If there is exactly one nonsingleton component, its \(t_i\) equals 2. Equation (1) then forces \(r_i=3\) and \(n_i=5\), so \(J_i=C_5\). Indeed, a 3-critical graph is a chordless odd cycle.

If there are at least two nonsingleton components, there can be exactly two components in total, and both must be \(C_5\). This gives \(r=6\), excluded by hypothesis. The remaining possibility is that every component is a singleton. ∎

## 2. Extending a coloring across a \((k-1)\)-clique

The following lemma is the main local ingredient.

**Lemma 4.** Let \(k\ge8\). Suppose
\[
|V(J)|\le2k-1,\qquad \Delta(J)\le k,\qquad \omega(J)\le k-1,
\]
and \(J\) contains a clique \(Q\) of order \(k-1\). Then \(J\) is \((k-1)\)-colorable.

**Proof.**

Add isolated vertices if necessary so that \(|V(J)|=2k-1\). Put \(R=V(J)\setminus Q\), so \(|R|=k\).

Each vertex of \(Q\) has at most two neighbors in \(R\). For \(x\in R\), write
\[
A_x=N_J(x)\cap Q.
\]
No \(A_x\) equals \(Q\), since that would give a \(K_k\).

Call \(x\) *heavy* if \(|A_x|=k-2\). Since
\[
\sum_{x\in R}|A_x|\le2(k-1)
\]
and \(3(k-2)>2(k-1)\), there are at most two heavy vertices.

We seek nonadjacent \(x,y\in R\) such that the following coloring extends to \(Q\): give \(x,y\) one common color and give the other \(k-2\) vertices of \(R\) distinct colors. This uses \(k-1\) colors.

Each vertex of \(Q\) then has a list of at least \(k-3\) available colors. Hall's theorem shows that extension can fail only in one of two ways:

* **Full-clique obstruction:** one color is forbidden at every vertex of \(Q\). A singleton color class cannot do this, so necessarily
  \[
  A_x\cup A_y=Q. \tag{3}
  \]
* **Almost-full-clique obstruction:** some \(k-2\) vertices of \(Q\) all forbid the same two colors. At least one of those color classes is a singleton heavy vertex. If both are singletons, they are heavy vertices with the same neighborhood in \(Q\).

Indeed, smaller subsets of \(Q\) automatically satisfy Hall's condition because every list has size at least \(k-3\).

We now choose \(x,y\), covering every possible number of heavy vertices.

### No heavy vertices

It suffices to find a nonedge \(xy\) in \(J[R]\) for which (3) fails.

Suppose no such nonedge exists, and put \(F=\overline{J[R]}\). Since \(\omega(J)\le k-1\), \(F\) has an edge. By supposition, every edge \(xy\) of \(F\) satisfies \(A_x\cup A_y=Q\). Hence, for every \(q\in Q\), the set \(N_J(q)\cap R\) is a vertex cover of \(F\) of size at most two.

If a vertex \(z\) had \(d_F(z)\ge3\), every such vertex cover would contain \(z\). Then \(z\) would be adjacent in \(J\) to every vertex of \(Q\), a contradiction. Thus \(\Delta(F)\le2\).

For every \(z\in R\),
\[
(k-1-d_F(z))+|A_z|=d_J(z)\le k,
\]
so \(|A_z|\le3\). But an edge \(xy\in E(F)\) would then give
\[
k-1=|Q|=|A_x\cup A_y|\le6,
\]
contrary to \(k\ge8\).

### Exactly one heavy vertex

Let the heavy vertex be \(r\), with \(A_r=Q\setminus\{a\}\). It has at most two neighbors in \(R\), and \(a\) also has at most two neighbors in \(R\). We may therefore choose
\[
t\in R\setminus\{r\}
\]
adjacent to neither \(r\) nor \(a\).

Pair \(r,t\). Their common color is not forbidden at \(a\), so (3) fails. There is no singleton heavy vertex, so the second obstruction also fails.

### Two heavy vertices with equal neighborhoods

Let \(A_r=A_s=Q\setminus\{a\}\). The vertices \(r,s\) are nonadjacent; otherwise their common \(k-2\) neighbors in \(Q\), together with \(r,s\), form a \(K_k\).

Pair \(r,s\). Again their union misses \(a\), and no singleton heavy vertex remains.

### Two heavy vertices with different neighborhoods

Write
\[
A_r=Q\setminus\{a\},\qquad
A_s=Q\setminus\{b\},\qquad a\ne b.
\]
Choose \(t\in R\setminus\{r,s\}\) adjacent to neither \(r\) nor \(a\). This is possible: \(r\) excludes at most two candidates, while \(a\), already adjacent to \(s\), excludes at most one further candidate.

Pair \(r,t\). Their union misses \(a\), so (3) fails. The only remaining singleton heavy vertex is \(s\), and \(a\in A_s\) is not adjacent to either member of the pair. Thus \(A_s\) is not contained in \(A_r\cup A_t\), excluding the second obstruction.

In every case Hall's condition holds, completing the coloring. ∎

## 3. A reducible joined 5-cycle

**Lemma 5.** Let \(k\ge7\), and let \(J\) have maximum degree at most \(k\). If \(J\) contains an induced subgraph
\[
X=K_{k-4}\vee C_5,
\]
then every \((k-1)\)-coloring of \(J-X\) extends to \(J\).

**Proof.**

Every vertex of the \(K_{k-4}\) already has degree \(k\) inside \(X\), so it has no neighbor outside \(X\). Each cycle vertex has degree \(k-2\) inside \(X\), and hence at most two outside neighbors.

After coloring \(J-X\), every cycle vertex has at least \(k-3\) available colors. Partition the cycle into two independent pairs and one singleton. Each pair has at least \(k-5\ge2\) common available colors; the singleton has at least \(k-3\ge4\) available colors. We can therefore assign three distinct colors to these three independent sets.

The \(K_{k-4}\) can use the remaining \(k-4\) colors. ∎

## 4. A dense triangle-free complement

Here is an elementary fact, including its equality case.

**Lemma 6.** If a triangle-free graph \(F\) on \(N\) vertices is nonbipartite, then
\[
\delta(F)\le\frac{2N}{5}.
\]
If equality holds, \(F\) is a balanced blow-up of \(C_5\) by independent sets.

**Proof.**

Let \(C\) be a shortest odd cycle, of length \(\ell\ge5\). It is chordless. Every vertex outside \(C\) has at most two neighbors on \(C\): otherwise the cyclic gaps between consecutive neighbors are all at least two, and one is odd. With at least three gaps, that odd gap has length at most \(\ell-4\), producing a shorter odd cycle through the outside vertex.

Consequently,
\[
\ell\delta(F)
\le \sum_{u\in V(C)}d_F(u)
=\sum_{v\in V(F)}|N_F(v)\cap V(C)|
\le2N.
\]
This proves the inequality.

Suppose \(\delta(F)=2N/5\). Equality forces \(\ell=5\) and every vertex to have exactly two neighbors on \(C\). Label the cycle cyclically \(c_0,\dots,c_4\), and set
\[
B_i=\{v:N_F(v)\cap V(C)=\{c_{i-1},c_{i+1}\}\}.
\]
These five sets partition \(V(F)\), and \(c_i\in B_i\).

Triangle-freeness permits edges only between consecutive sets \(B_i\). Writing \(b_i=|B_i|\), we obtain
\[
b_{i-1}+b_{i+1}\ge\delta(F).
\]
Summing gives equality throughout, because \(2N=5\delta(F)\). The five cyclic equations force every \(b_i=N/5\). Finally, the degree condition forces all edges between consecutive sets to be present. ∎

## 5. Proof of the critical-graph theorem

Let \(H\) satisfy the hypotheses of Theorem 2, and suppose \(H\ne K_k\).

A noncomplete \(k\)-critical graph contains no \(K_k\). By Lemma 3,
\[
|V(H)|=2k-1. \tag{4}
\]

### Case 1: \(\alpha(H)\le2\)

Then \(F=\overline H\) is triangle-free, and
\[
\delta(F)\ge (2k-2)-k=k-2.
\]
The graph \(F\) cannot be bipartite: a bipartition of its \(2k-1\) vertices has a part of size at least \(k\), giving a \(K_k\) in \(H\).

Lemma 6 therefore yields
\[
k-2\le \frac{2(2k-1)}5,
\]
which simplifies to \(k\le8\).

Thus \(k=8\), \(|V(F)|=15\), and \(\delta(F)=6=2|V(F)|/5\). The equality case of Lemma 6 makes \(F\) a balanced independent-set blow-up of \(C_5\), with three vertices in each part. Since \(C_5\) is self-complementary,
\[
H\cong C_5[K_3].
\]

### Case 2: \(\alpha(H)\ge3\)

Choose an independent triple \(T\). Since \(T\) can receive one color,
\[
\chi(H-T)\ge k-1.
\]
Criticality gives the reverse inequality, so \(\chi(H-T)=k-1\).

Choose a vertex-critical induced subgraph \(X\subseteq H-T\) with chromatic number \(r=k-1\). Then
\[
|V(X)|\le2k-4=2r-2,\qquad
\Delta(X)\le k=r+1.
\]
Since \(r\ge7\), Lemma 3 gives
\[
X=K_{k-1}
\quad\text{or}\quad
X=K_{k-4}\vee C_5.
\]

In the first case, Lemma 4 makes \(H\) \((k-1)\)-colorable.

In the second case, criticality provides a \((k-1)\)-coloring of \(H-X\), and Lemma 5 extends it to \(H\).

Both contradict \(\chi(H)=k\). This completes the proof of Theorem 2. ∎

## 6. Deduction for the conjecture and sharpness

Suppose \(G\) violates the conjectured inequality, and put \(k=\chi(G)\). Then
\[
k\ge\Delta,\qquad k>\omega(G).
\]
Choose a vertex-critical induced subgraph \(H\) with chromatic number \(k\). It is noncomplete and satisfies
\[
\Delta(H)\le\Delta\le k.
\]
If \(|V(G)|\le2\Delta-1\), then
\[
|V(H)|\le2\Delta-1\le2k-1.
\]
For \(\Delta\ge9\), Theorem 2 gives a contradiction.

If \(\Delta=8\) and \(|V(G)|\le15\), Theorem 2 instead forces \(k=8\) and \(H=C_5[K_3]\). Since \(H\) already has 15 vertices, \(G=H\).

Finally, \(C_5[K_3]\) really violates the degree-8 bound:
\[
\Delta=8,\qquad \omega=6,\qquad \chi=8.
\]
Its independence number is two, so its 15 vertices require at least eight colors. An eight-coloring assigns the following color sets to its five consecutive cliques:
\[
\{1,2,3\},\quad
\{4,5,6\},\quad
\{1,2,7\},\quad
\{3,4,8\},\quad
\{5,6,7\}.
\]
Consecutive sets are disjoint.

## What remains unresolved

The argument excludes the smallest order permitted by Gallai's theorem for a noncomplete critical graph with \(\Delta\le\chi\).

Its limitation is precise. At order \(2k-1\), deleting an independent triple leaves at most
\[
2(k-1)-2
\]
vertices, so Gallai decomposition forces the restricted structure used above. At order \(2k\), the corresponding bound becomes \(2(k-1)-1\), where that conclusion is unavailable.

Nothing here excludes larger critical counterexamples. Thus this is a complete proof of an order-restricted special case, not a proof of Borodin–Kostochka.
