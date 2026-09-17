Attack the following open graph-theory problem.

Catalog id: odd_cycle_transversal_in_triangle_free_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/odd_cycle_transversal_in_triangle_free_graphs/
Original entry: http://www.openproblemgarden.org/op/odd_cycle_transversal_in_triangle_free_graphs
Problem attributed to: Erdos, Paul, Faudree, Ralph, Pach, János, Spencer, Joel (posted 2013-03-06)

=== Problem statement (OpenProblemGarden) ===
Title: Odd-cycle transversal in triangle-free graphs
Conjecture If $ G $ is a simple triangle-free graph, then there is a set of at most $ n^2/25 $ edges whose deletion destroys every odd cycle.

=== References listed by OpenProblemGarden ===
- *[EFPS] P. Erdös, R. Faudree, J. Pach and J. Spencer, How to make a graph bipartite. J. Combin. Theory Ser. B 45 (1988), 86--98.

=== Catalog page (statement + literature review) ===
Odd-cycle transversal in triangle-free graphs — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that every triangle-free graph on $n$ vertices can be made bipartite by deleting at most $n^2/25$ edges remains open. Balogh, Clemen, and Lidický (2021) proved it for triangle-free graphs with edge density at most $0.2486$ or at least $0.3197$, and improved the best general upper bound from $n^2/18$ to $n^2/23.5$. A related spectral approach by the same group and coauthors (2022) further investigated structural properties of triangle-free graphs, but the full conjecture is unresolved.

 Cited literature (2)

 
 
 
partial Max Cuts in Triangle-free Graphs
 (2021)
 

 
 József Balogh, Felix Christian Clemen, Bernard Lidický · arXiv preprint · arXiv:2103.14179

Proves the Erdős–Faudree–Pach–Spencer conjecture for triangle-free graphs with edge density at most 0.2486 or at least 0.3197, and improves the general upper bound on edges to delete to achieve bipartiteness from $n^2/18$ to $n^2/23.5$.
 

 
 
partial The Spectrum of Triangle-free Graphs
 (2022)
 

 
 József Balogh, Felix Christian Clemen, Bernard Lidický, Sergey Norin, Jan Volec · SIAM Journal on Discrete Mathematics · arXiv:2204.00093 · doi:10.1137/22M150767X

Via flag algebra and spectral methods, proves bounds on the smallest eigenvalue of the signless Laplacian of triangle-free graphs, with progress toward structural results related to the bipartization conjecture.
 

 

 Reviewer notes. The ScienceDirect page for '10 problems for partitions of triangle-free graphs' (2023) returned HTTP 403 and could not be verified; it may contain additional partial results. The UCSD Erdős problems page (mathweb.ucsd.edu) returned a certificate error and could not be fetched. The extremal bound n²/25 is tight, realized by the balanced blow-up of C₅. The 2022 spectral paper (arXiv:2204.00093) is published in SIAM J. Discrete Math. (doi confirmed in search results) but the exact contribution to the n²/25 bound could not be fully characterized from the abstract alone.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. If $ G $ is a simple triangle-free graph, then there is a set of at most $ n^2/25 $ edges whose deletion destroys every odd cycle.

Bibliography

★ [EFPS]
 P. Erdös, R. Faudree, J. Pach and J. Spencer, How to make a graph bipartite. J. Combin. Theory Ser. B 45 (1988), 86--98.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The sharp bound holds for every graph homomorphic to the Clebsch graph, with equality characterized, and a separate argument proves the stronger bound n^2/26 for odd girth at least 13.",
  "would_publish": false,
  "caveats": "Special cases only; novelty is not claimed, and no improved general upper bound is established."
}
```

# Partial results

Write
\[
b(G)=\min\{|F|:G-F\text{ is bipartite}\}.
\]
If \(m=e(G)\) and \(\operatorname{mc}(G)\) is the maximum number of edges in a cut, then
\[
b(G)=m-\operatorname{mc}(G).
\]
Thus the conjecture asks whether \(b(G)\le n^2/25\) for every triangle-free \(n\)-vertex graph.

I do not settle the unrestricted conjecture. Below are two self-contained special cases:

1. **Every graph homomorphic to the Clebsch graph satisfies the conjecture.** More generally, any triangle-free graph having a cut containing at least \(4m/5\) edges satisfies it. Within this class, equality occurs precisely for balanced blow-ups of \(C_5\).
2. **Every graph of odd girth at least \(13\) satisfies \(b(G)\le n^2/26\).**

The first result also gives a quantitative degree-stability estimate.

## 1. A neighborhood-cut inequality

Let \(G\) be triangle-free, with \(n\ge1\). For every vertex \(v\), its neighborhood \(N(v)\) is independent. Consequently, the cut with one side \(N(v)\) contains exactly
\[
\sum_{u\in N(v)}d(u)
\]
edges.

Averaging these \(n\) cuts gives
\[
\operatorname{mc}(G)
 \ge \frac1n\sum_{v\in V(G)}\sum_{u\in N(v)}d(u)
 =\frac1n\sum_{u\in V(G)}d(u)^2.
\]
In particular,
\[
\boxed{\quad
b(G)\le m-\frac1n\sum_v d(v)^2
       \le m-\frac{4m^2}{n^2}.
\quad} \tag{1}
\]
The second inequality is Cauchy–Schwarz.

This inequality is the mechanism that converts a relative \(4/5\)-cut guarantee into the conjectured absolute bound.

## 2. A sharp \(4/5\)-cut criterion

### Theorem 1
Let \(G\) be a triangle-free graph on \(n\ge1\) vertices. Suppose
\[
b(G)\le \frac{m}{5},
\]
equivalently, \(G\) has a cut containing at least \(4m/5\) edges. Then
\[
b(G)\le \frac{n^2}{25}.
\]
Moreover,
\[
\boxed{\quad
\sum_v\left(d(v)-\frac{2n}{5}\right)^2
\le 4n\left(\frac{n^2}{25}-b(G)\right).
\quad} \tag{2}
\]
Equality \(b(G)=n^2/25\) holds if and only if \(n=5q\) and \(G\) is the complete balanced blow-up of \(C_5\) with five parts of size \(q\).

### Proof of the bound and degree estimate

Using (1), we obtain
\[
\begin{aligned}
\frac1n\sum_v\left(d(v)-\frac{2n}{5}\right)^2
&=\frac1n\sum_v d(v)^2-\frac85m+\frac{4n^2}{25}\\
&\le (m-b(G))-\frac85m+\frac{4n^2}{25}\\
&=\frac{4n^2}{25}-\frac35m-b(G).
\end{aligned}
\]
Since \(m\ge5b(G)\), the last expression is at most
\[
4\left(\frac{n^2}{25}-b(G)\right).
\]
The left side is nonnegative, proving the asserted bound and (2).

In particular, if
\[
b(G)\ge \left(\frac1{25}-\varepsilon\right)n^2,
\]
then
\[
\sum_v\left(d(v)-\frac{2n}{5}\right)^2\le4\varepsilon n^3.
\]
Thus near equality, under the \(4/5\)-cut hypothesis, forces approximate \(2n/5\)-regularity.

### A shortest-odd-cycle observation

We will use the following fact twice.

**Lemma.** If \(C\) is a shortest odd cycle in a triangle-free graph, then \(C\) is induced and every vertex outside \(C\) has at most two neighbors on \(C\). Consequently,
\[
\sum_{v\in V(C)}d(v)\le2n. \tag{3}
\]

**Proof.** A chord of \(C\) would produce a shorter odd cycle, so \(C\) is induced.

Suppose an outside vertex \(x\) has at least three neighbors on \(C\). The cyclic gaps between consecutive such neighbors all have length at least two, since \(G\) is triangle-free. Their sum is odd, so some gap has odd length. Because at least two other gaps have length at least two, this odd gap has length at most \(|C|-4\). Together with its two edges to \(x\), it forms an odd cycle of length at most \(|C|-2\), a contradiction.

Every vertex, including vertices of \(C\), therefore has at most two neighbors on \(C\). Double-counting incidences with \(C\) proves (3). ∎

### Equality in Theorem 1

Suppose \(b(G)=n^2/25\). By (2),
\[
d(v)=\frac{2n}{5}\qquad\text{for every }v.
\]
Also, \(G\) is nonbipartite.

Let \(C\) be a shortest odd cycle of length \(\ell\). The lemma gives
\[
\ell\frac{2n}{5}\le2n,
\]
so \(\ell\le5\). Triangle-freeness forces \(\ell=5\). Write
\[
C=c_0c_1c_2c_3c_4c_0,
\]
with subscripts modulo five.

Now
\[
\sum_{i=0}^4d(c_i)=2n.
\]
Since every vertex has at most two neighbors on \(C\), every vertex must have exactly two.

The two neighbors cannot be consecutive on \(C\). Thus the sets
\[
V_i=\{x:N(x)\cap V(C)=\{c_{i-1},c_{i+1}\}\},
\qquad i\in\mathbb Z/5\mathbb Z,
\]
partition \(V(G)\).

Vertices in the same \(V_i\), or in \(V_i\) and \(V_{i+2}\), have a common neighbor on \(C\), so triangle-freeness forbids edges between them. Hence edges can occur only between consecutive parts.

Put \(a_i=|V_i|\). By the definition of the parts,
\[
a_{i-1}+a_{i+1}=d(c_i)=\frac{2n}{5}
\]
for every \(i\). Subtracting equations two indices apart shows that all \(a_i\) are equal. Hence
\[
a_i=\frac n5.
\]
Every vertex in \(V_i\) has degree \(2n/5\), and its possible neighbors are precisely the \(2n/5\) vertices in \(V_{i-1}\cup V_{i+1}\). All these edges must therefore be present. This is the complete balanced blow-up of \(C_5\).

Conversely, let all five parts have size \(q\). Deleting all \(q^2\) edges between one pair of consecutive parts makes the graph bipartite. For the matching lower bound, there are \(q^5\) five-cycles obtained by selecting one vertex from each part, and each edge belongs to exactly \(q^3\) of them. Any edge set meeting every odd cycle must therefore have size at least
\[
q^5/q^3=q^2.
\]
Thus
\[
b(G)=q^2=\frac{n^2}{25},
\]
as claimed. ∎

## 3. An explicit blow-up-closed class: Clebsch-homomorphic graphs

Define a graph \(H\) as follows:

- its vertices are the even-cardinality subsets of \([5]\);
- \(A,B\) are adjacent exactly when
  \[
  |A\triangle B|=4.
  \]

There are \(1+10+5=16\) vertices. This is a standard model of the **Clebsch graph**.

It is triangle-free: if \(A\) is adjacent to distinct \(B,C\), then \(A\triangle B\) and \(A\triangle C\) are distinct four-subsets of \([5]\). Their symmetric difference has size two, so \(|B\triangle C|=2\), and \(B,C\) are not adjacent.

### Corollary 2
If \(G\) admits a graph homomorphism \(f:G\to H\), then
\[
b(G)\le \frac{n^2}{25}.
\]
Equality occurs precisely for complete balanced blow-ups of \(C_5\).

**Proof.** For each \(i\in[5]\), form the cut
\[
S_i=\{v\in V(G):i\in f(v)\}.
\]
For every edge \(uv\), the labels \(f(u),f(v)\) differ in exactly four coordinates. Therefore \(uv\) crosses exactly four of these five cuts. Consequently,
\[
\sum_{i=1}^5 e(S_i,V(G)\setminus S_i)=4m.
\]
One of the cuts contains at least \(4m/5\) edges, so Theorem 1 applies. ∎

This proves the conjecture for **every subgraph of every independent-set blow-up of \(H\)**, with arbitrary part sizes.

In particular, it applies to all graphs homomorphic to the Petersen graph: the subgraph of \(H\) induced by its two-element subsets has adjacency given by disjointness and is the Petersen graph.

The constant is sharp within this class. For example,
\[
12,\ 34,\ 15,\ 23,\ 45
\]
are the labels of an induced \(C_5\) in \(H\), where \(ij\) abbreviates \(\{i,j\}\).

### Constructive aspect

When the homomorphism is supplied, no maximum-cut computation is required. Inspect:

- the five coordinate cuts above;
- the \(n\) neighborhood cuts from Section 1.

Let \(b_*\) be the smallest number of uncut edges among these \(n+5\) cuts. Then
\[
b_*\le \frac m5,
\qquad
b_*\le m-\frac1n\sum_v d(v)^2.
\]
The proof of Theorem 1 works unchanged with \(b_*\) in place of \(b(G)\), giving an explicit cut with at most \(n^2/25\) uncut edges.

## 4. A separate result for large odd girth

The odd girth is the length of a shortest odd cycle; bipartite graphs have infinite odd girth.

### Theorem 3
Let \(g\ge5\) be odd. If \(G\) has odd girth at least \(g\), then
\[
b(G)\le \frac{n^2}{2g}.
\]
In particular, odd girth at least \(13\) implies
\[
b(G)\le\frac{n^2}{26}<\frac{n^2}{25}
\qquad(n>0).
\]

### Proof

We induct on \(n\), with \(g\) fixed. A bipartite graph needs no deletions.

Otherwise, choose a shortest odd cycle \(C\), of length \(\ell\ge g\), and put
\[
R=V(G)\setminus V(C),\qquad r=|R|=n-\ell.
\]
By the shortest-odd-cycle lemma, \(C\) is induced and
\[
e(C,R)\le2r.
\]

By induction, \(G[R]\) has a cut with at most \(r^2/(2g)\) uncut edges. Cut the odd cycle \(C\) alternately, leaving exactly one of its edges uncut.

Keep the cut on \(R\) fixed and consider the two orientations of the cut on \(C\). Every edge between \(C\) and \(R\) is uncut in exactly one of these orientations. One orientation therefore leaves at most
\[
\frac{e(C,R)}2\le r
\]
such edges uncut. Hence
\[
b(G)\le \frac{r^2}{2g}+r+1.
\]
But
\[
\frac{(r+\ell)^2-r^2}{2g}
=\frac{r\ell}{g}+\frac{\ell^2}{2g}
\ge r+\frac g2
\ge r+1.
\]
Thus
\[
b(G)\le\frac{(r+\ell)^2}{2g}=\frac{n^2}{2g}.
\]
This completes the induction. ∎

## 5. The remaining gap

These arguments leave the general conjecture unresolved. They do imply that any counterexample must satisfy all of the following:

- \(\operatorname{mc}(G)<4m/5\), by Theorem 1;
- its odd girth belongs to \(\{5,7,9,11\}\), by Theorem 3;
- it is not homomorphic to the Clebsch graph;
- its number of edges satisfies
  \[
  \frac{2n^2}{25}<m<\frac{n^2}{5}.
  \]

For the last assertion, a random cut gives \(b(G)\le m/2\). At the other end, (1) gives
\[
b(G)\le m-\frac{4m^2}{n^2}\le\frac{n^2}{25}
\quad\text{whenever }m\ge\frac{n^2}{5}.
\]

These elementary restrictions are not asserted to improve the density results quoted in the question. The unresolved obstacle here is controlling graphs without a \(4/5\)-cut guarantee and with short odd cycles. No argument above covers that remaining class.
