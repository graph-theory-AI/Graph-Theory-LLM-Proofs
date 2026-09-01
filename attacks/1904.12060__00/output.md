```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains open, but it holds for every bipartite or 2-degenerate graph and for every graph with Δ=D≥5 and maximum average degree at most 6D/(D+3).",
  "would_publish": false,
  "caveats": "These are rigorous special cases, not a full resolution, and I have not checked whether all of the elementary refinements below are already in the literature."
}
```

# Mathematical writeup

## 1. Statement and notation

For a simple graph \(G\), its total graph \(T(G)\) has vertex set \(V(G)\cup E(G)\), with two elements adjacent when they are adjacent or incident in \(G\). Thus
\[
\chi''_\ell(G)=\chi_\ell(T(G)).
\]

The conjecture is
\[
\chi''_\ell(G)\le \Delta(G)+2
\tag{C}
\]
for every finite simple graph \(G\).

I do not prove or disprove (C). I prove three partial results:

1. (C) holds for every bipartite graph, and the bound is sharp on \(K_{D,D}\).
2. (C) holds for every \(2\)-degenerate graph.
3. If \(D\ge5\), \(\Delta(G)\le D\), and
   \[
   \operatorname{mad}(G)\le \frac{6D}{D+3},
   \]
   then \(G\) is totally \((D+2)\)-choosable.

Here
\[
\operatorname{mad}(G)=\max_{\varnothing\ne H\subseteq G}\frac{2|E(H)|}{|V(H)|}.
\]

---

## 2. A general baseline bound

### Proposition 2.1
If \(\Delta(G)=D\ge2\), then
\[
\chi''_\ell(G)\le 2D.
\]

### Proof

For an original vertex \(v\),
\[
d_{T(G)}(v)=2d_G(v)\le2D.
\]
For an edge \(uv\),
\[
d_{T(G)}(uv)=2+(d_G(u)-1)+(d_G(v)-1)
=d_G(u)+d_G(v)\le2D.
\]
Thus \(\Delta(T(G))\le2D\).

Consider a connected component \(Q\) of \(T(G)\), and let \(M=\Delta(Q)\). If \(M\le2D-1\), greedy list coloring gives
\[
\chi_\ell(Q)\le M+1\le2D.
\]
If \(M=2D\), the list version of Brooks' theorem gives \(\chi_\ell(Q)\le M\), unless \(Q\) is a complete graph or an odd cycle. Here \(M\ge4\), so the odd-cycle exception is irrelevant. Moreover, if the corresponding component of \(G\) has at least three vertices, then an edge \(xy\) and any third original vertex are nonadjacent in \(T(G)\), so \(Q\) is not complete. Components with at most two original vertices are immediate.

Hence \(T(G)\) is \(2D\)-choosable. ∎

In particular, (C) holds for \(D=2\). For \(D=1\), every nontrivial component is \(K_2\), whose total graph is \(K_3\), so \(\chi''_\ell=3=D+2\).

---

## 3. Graphs with list chromatic index \(D\)

### Proposition 3.1
Let \(G\) have maximum degree at most \(D\). If
\[
\chi'_\ell(G)\le D,
\]
then
\[
\chi''_\ell(G)\le D+2.
\]

### Proof

Let every vertex and edge \(x\) have a list \(L(x)\) of size at least \(D+2\).

First greedily color the vertices properly from their lists. For an edge \(e=uv\), put
\[
L'(e)=L(e)\setminus\{c(u),c(v)\}.
\]
Then \(|L'(e)|\ge D\). Since \(G\) is \(D\)-edge-choosable, its edges have a proper coloring from the lists \(L'\). This edge coloring avoids the colors of both endpoints, and together with the vertex coloring is a proper total coloring. ∎

### Corollary 3.2
Every bipartite simple graph \(G\) satisfies
\[
\chi''_\ell(G)\le \Delta(G)+2.
\]

This follows from the theorem that every bipartite graph is \(\Delta\)-edge-choosable. For completeness, the relevant argument can be summarized as follows.

Take a fixed proper \(D\)-edge-coloring \(\varphi:E(G)\to\{1,\dots,D\}\), supplied by König's edge-coloring theorem. Let \(A,B\) be the bipartition. Orient the line graph \(L(G)\) by orienting, at vertices of \(A\), from smaller to larger \(\varphi\)-color, and at vertices of \(B\), from larger to smaller \(\varphi\)-color. An edge of \(\varphi\)-color \(i\) has outdegree at most
\[
(D-i)+(i-1)=D-1.
\]

This orientation is kernel-perfect. Indeed, for any subset \(F\subseteq E(G)\), let vertices of \(A\) prefer larger \(\varphi\)-colors and vertices of \(B\) prefer smaller ones. A stable matching \(M\) in the bipartite graph with edge set \(F\) is an independent set in \(L(G)[F]\). Stability says that every \(e\in F\setminus M\) has an endpoint matched to an edge preferred to \(e\); consequently, \(e\) has an outgoing arc to \(M\). Thus \(M\) is a kernel.

The kernel lemma now shows that \(L(G)\) is colorable from arbitrary edge lists of size \(D\).

### Sharpness

For every \(D\ge1\),
\[
\chi''_\ell(K_{D,D})=D+2.
\]

Only the lower bound needs proof. Suppose \(K_{D,D}\), with bipartition \(A,B\), had a total coloring with \(D+1\) colors. At each vertex, its \(D\) incident edges together with the vertex itself form a clique of size \(D+1\), so all colors occur exactly once there.

For a color \(c\), let \(m_A(c)\) and \(m_B(c)\) be the numbers of vertices of color \(c\) in \(A\) and \(B\). Counting the edges of color \(c\) from the two sides gives
\[
D-m_A(c)=D-m_B(c),
\]
and hence \(m_A(c)=m_B(c)\). But no color can occur on both sides, since every vertex in \(A\) is adjacent to every vertex in \(B\). Therefore \(m_A(c)=m_B(c)=0\) for every \(c\), contradicting \(\sum_c m_A(c)=D\).

Thus even ordinary total coloring sometimes needs \(D+2\) colors.

---

## 4. Degenerate graphs

### Proposition 4.1
Let \(G\) be \(k\)-degenerate with \(\Delta(G)\le D\), where \(D\ge k+1\). Then
\[
\chi''_\ell(G)\le D+k.
\]

### Proof

Use induction on \(|V(G)|\), with the parameter \(D\) fixed. Let \(v\) have degree \(r\le k\), with neighbors \(u_1,\dots,u_r\). By induction, totally color \(G-v\) from lists of size \(D+k\).

Now color the edges \(vu_1,\dots,vu_r\) in this order. When coloring \(vu_i\), the already colored conflicting elements consist of:

- \(u_i\) and the edges of \(G-v\) incident with \(u_i\), at most \(d_G(u_i)\le D\) elements;
- the previously colored edges \(vu_1,\dots,vu_{i-1}\).

Thus at most \(D+i-1\) colors are forbidden. Since
\[
D+k-(D+i-1)=k-i+1\ge1,
\]
a color remains.

Finally, \(v\) conflicts with at most \(r\) neighboring vertices and \(r\) incident edges, hence at most \(2k\) colors. Since
\[
D+k\ge2k+1,
\]
\(v\) can be colored. ∎

### Corollary 4.2
Every \(2\)-degenerate simple graph satisfies (C).

Indeed, for \(D\ge3\), take \(k=2\) in Proposition 4.1. The cases \(D\le2\) follow from Proposition 2.1 and the direct \(D=1\) observation.

This includes, for example, all outerplanar graphs and all graphs of treewidth at most two.

---

## 5. A maximum-average-degree criterion

The following gives a wider sparse-graph class.

### Theorem 5.1
Let \(D\ge5\). If
\[
\Delta(G)\le D
\qquad\text{and}\qquad
\operatorname{mad}(G)\le \alpha_D:=\frac{6D}{D+3},
\]
then \(G\) is totally \((D+2)\)-choosable.

The proof uses a local extension lemma.

### Lemma 5.2
Let \(H\) have maximum degree at most \(D\), and suppose \(H-v\) has already been totally colored from lists of size \(D+2\). Put \(r=d_H(v)\). Assume

1. \(2r<D+2\); and
2. for every \(s\in\{3,\dots,r\}\), fewer than \(s\) neighbors \(u\) of \(v\) satisfy
   \[
   d_H(u)\ge D+3-s.
   \tag{1}
   \]

Then the coloring extends to \(H\).

#### Proof

For each edge \(vu\), after coloring \(H-v\), let
\[
A_u=L(vu)\setminus
\bigl(\{c(u)\}\cup\{c(e):e\in E(H-v),\, e\ni u\}\bigr).
\]
Exactly \(d_H(u)\) already colored elements conflict with \(vu\) at \(u\), so
\[
|A_u|\ge D+2-d_H(u)\ge2.
\tag{2}
\]

We verify Hall's condition for the family \(\{A_u:u\in N(v)\}\). For one or two sets it follows from (2). Let \(X\subseteq N(v)\) have size \(t\ge3\). By condition 2, some \(u\in X\) has
\[
d_H(u)\le D+2-t.
\]
Therefore \(|A_u|\ge t\), and hence
\[
\left|\bigcup_{x\in X} A_x\right|\ge t.
\]
Hall's theorem gives pairwise distinct colors for all edges incident with \(v\).

After these edges are colored, at most \(2r\) colors are forbidden at \(v\). Since \(D+2>2r\), a color remains for \(v\). ∎

### Proof of Theorem 5.1

Suppose the theorem is false, and fix a bad list assignment. Choose a vertex-minimal uncolorable subgraph \(H\). We may assume \(H\) is connected.

Lemma 5.2 first implies
\[
\delta(H)\ge3.
\tag{3}
\]
Moreover, whenever \(v\) has degree \(r\) with \(2r<D+2\), failure of the lemma implies that there is an integer
\[
s(v)\in\{3,\dots,r\}
\]
such that \(v\) has at least \(s(v)\) neighbors of degree at least
\[
D+3-s(v).
\tag{4}
\]

Set
\[
\alpha=\frac{6D}{D+3}.
\]
Notice that \(3<\alpha<6\). If \(r<\alpha\), then \(r\in\{3,4,5\}\), and \(2r<D+2\):

- \(r=3\) is allowed since \(D\ge5\);
- \(r=4<\alpha\) forces \(D\ge7\);
- \(r=5<\alpha\) forces \(D\ge16\).

Thus every vertex \(v\) with \(d(v)=r<\alpha\) has a witness \(s(v)\) satisfying (4). Select \(s(v)\) such high-degree neighbors.

Give each vertex \(x\) initial charge
\[
\mu(x)=d(x)-\alpha.
\]
For each low-degree vertex \(v\), each of its selected neighbors sends it
\[
\frac{\alpha-d(v)}{s(v)}.
\tag{5}
\]
Consequently, every low-degree vertex ends with charge zero.

It remains to check that no donor sends more than its initial charge. Suppose a vertex \(x\) of degree \(d\) is selected by a low vertex \(v\) with parameter \(s=s(v)\). Put
\[
p=\max\{3,D+3-d\}.
\]
Then \(p\le s\le d(v)<\alpha<6\), so \(p\in\{3,4,5\}\), and
\[
d\in\{D,D-1,D-2\}.
\]
The transfer along this edge is at most
\[
\frac{\alpha-s}{s}\le \frac{\alpha-p}{p}.
\tag{6}
\]
Thus \(x\) sends at most \(d(\alpha-p)/p\). We claim
\[
d\frac{\alpha-p}{p}\le d-\alpha.
\tag{7}
\]
Since \(d=D+3-p\), inequality (7) is equivalent to
\[
\alpha(D+3)\le2p(D+3-p).
\]
The left side is \(6D\). For \(p=3,4,5\), the right side is respectively
\[
6D,\qquad 8(D-1),\qquad 10(D-2),
\]
each at least \(6D\) for \(D\ge5\). Hence every donor finishes with nonnegative charge. All other vertices also have nonnegative charge.

It follows that
\[
\sum_{x\in V(H)}(d(x)-\alpha)\ge0,
\]
so
\[
\frac{2|E(H)|}{|V(H)|}\ge\alpha.
\tag{8}
\]

It remains to exclude equality, since the theorem assumes \(\operatorname{mad}(G)\le\alpha\). Suppose equality holds in (8). Then every final charge in the discharging argument is zero.

If \(H\) contains a degree-\(D\) vertex, equality in (6) and (7) forces every one of its incident edges to lead to a degree-\(3\) vertex using \(s=3\). Conversely, every degree-\(3\) vertex has all three neighbors of degree \(D\). Connectivity then forces \(H\) to be bipartite, with degree classes \(3\) and \(D\). Corollary 3.2 colors \(H\), a contradiction.

Therefore \(H\) has no degree-\(D\) vertex. It then has no degree-\(3\) vertex. A low vertex of degree \(4\) or \(5\) would receive charge from a vertex of degree \(D-1\) or \(D-2\); the corresponding inequalities in (7) are strict in the cases where such a transfer is possible, leaving that donor with positive charge. Hence no vertex has degree below \(\alpha\).

Since the average degree equals \(\alpha\), every vertex must have degree exactly \(\alpha\). The only integers \(D\ge5\) for which \(6D/(D+3)\) is an integer are
\[
(D,\alpha)=(6,4)\quad\text{and}\quad(15,5).
\]
In the first case Proposition 2.1 colors \(H\) from lists of size \(8=D+2\); in the second, Proposition 2.1 needs only \(10<17=D+2\) colors. Both are contradictions.

Thus equality is also impossible, completing the proof. ∎

### Consequences

For a graph with actual maximum degree \(D\ge5\), Theorem 5.1 proves the conjectured bound whenever
\[
\operatorname{mad}(G)\le\frac{6D}{D+3}.
\]

Some concrete instances are:

- \(D=5\): threshold \(15/4\);
- \(D=6\): threshold \(4\);
- \(D=7\): threshold \(21/5\);
- the threshold tends to \(6\) as \(D\to\infty\).

For planar graphs this gives, for example:

- every triangle-free planar graph with \(\Delta\ge6\) is totally \((\Delta+2)\)-choosable, since its maximum average degree is \(<4\);
- every planar graph of girth at least \(5\) with \(\Delta\ge5\) is totally \((\Delta+2)\)-choosable;
- planar graphs of girth at least \(6\) are \(2\)-degenerate, so Corollary 4.2 handles all maximum degrees.

---

## 6. What remains unresolved

These arguments do not approach a proof for arbitrary dense nonbipartite graphs. The basic local obstruction appears already when deleting a degree-\(3\) vertex whose three neighbors all have degree \(D\): after coloring \(G-v\), each incident edge is guaranteed only two available colors, and all three residual lists may be the same two-element set. Hall's condition then fails, and a purely greedy extension is impossible.

Consequently, any proof of the full conjecture must use recoloring or more global structure beyond the local deletion arguments above. In particular, the methods here leave nonbipartite cubic graphs and many regular dense graphs untreated.

No counterexample is produced. A hypothetical counterexample can at least be assumed nonbipartite and not \(2\)-degenerate; if its maximum degree is \(D\ge5\), it must also satisfy
\[
\operatorname{mad}(G)>\frac{6D}{D+3}.
\]

Thus the full List Total Coloring Conjecture remains open.