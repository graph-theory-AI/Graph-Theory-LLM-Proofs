```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The L=1 conclusion holds for bounded-geometry graphs and for bounded-diameter blow-ups of bounded-tree-width quotients with uniformly bounded interfaces, but arbitrary ball-covered decompositions remain unresolved.",
  "would_publish": false,
  "caveats": "The arguments require extra uniform geometry or a global coherent partition, neither of which follows from the stated hypothesis."
}
```

# Mathematical writeup

## 1. Formulation

I use the following standard quantitative formulation. A connected graph \(G\) has a \((k,r)\)-centred tree-decomposition if it has a tree-decomposition
\[
(T,(B_t)_{t\in V(T)})
\]
such that for every \(t\) there are vertices \(c_{t,1},\dots,c_{t,k}\) with
\[
B_t\subseteq \bigcup_{i=1}^k B_G(c_{t,i},r).
\]

The question is whether there are constants \(w=w(k,r)\) and \(C=C(k,r)\) such that \(G\) admits a map \(f\) to a graph \(H\) of tree-width at most \(w\) satisfying
\[
d_G(x,y)-C\le d_H(f(x),f(y))\le d_G(x,y)+C
\]
for all \(x,y\in V(G)\), with every vertex of \(H\) at distance at most \(C\) from \(f(V(G))\).

I do not prove this in full. The principal partial result below handles graphs obtained from a bounded-tree-width quotient by replacing each quotient vertex by a bounded-diameter graph having only boundedly many attachment vertices.

---

## 2. A bounded-interface theorem

### Theorem 2.1

Let \(G\) be a connected graph, and let
\[
\mathcal F=\{F_q:q\in V(Q)\}
\]
be a partition of \(V(G)\). Let \(Q\) be the quotient graph: distinct \(q,q'\) are adjacent in \(Q\) precisely when \(G\) has an edge between \(F_q\) and \(F_{q'}\).

Assume:

1. \(\operatorname{tw}(Q)\le a\);
2. every induced graph \(G[F_q]\) is connected and has diameter at most \(D\);
3. for every \(q\), at most \(s\) vertices of \(F_q\) have a neighbour outside \(F_q\).

Then \(G\) admits a \((1,2D)\)-quasi-isometry to an ordinary graph \(H\) satisfying
\[
\operatorname{tw}(H)\le (a+1)(s+1)-1.
\]

Thus the desired \(L=1\) conclusion holds in this globally partitioned, bounded-interface case.

### Proof

For each \(q\), let
\[
\partial F_q=\{x\in F_q:N_G(x)\not\subseteq F_q\},
\]
and choose an anchor \(a_q\in F_q\). Put
\[
P_q=\partial F_q\cup\{a_q\};
\qquad |P_q|\le s+1.
\]

Construct an integer-weighted graph \(K\) as follows.

- Its vertex set is \(\bigcup_q P_q\).
- For every \(q\), make \(P_q\) a complete weighted graph, assigning to \(u,v\in P_q\) the weight
  \[
  \ell(uv)=d_{G[F_q]}(u,v)\le D.
  \]
- Retain every edge of \(G\) joining two different parts; its endpoints belong to the corresponding boundary sets, and it receives weight \(1\).

We first record that \(K\) exactly preserves the metric of \(G\) on its retained vertices:
\[
d_K(u,v)=d_G(u,v)
\qquad\text{for all }u,v\in V(K). \tag{2.1}
\]

Indeed, every weighted edge inside \(P_q\) can be replaced by a path of the same length inside \(G[F_q]\), and every cross-edge of \(K\) is an edge of \(G\). Hence
\[
d_G(u,v)\le d_K(u,v).
\]
Conversely, take a \(G\)-path between two vertices of \(K\), and divide it into maximal subpaths lying in individual parts \(F_q\), separated by cross-edges. The endpoints of each such internal subpath lie in \(P_q\). Replacing it by the corresponding weighted edge of \(K\) does not increase its length. Thus
\[
d_K(u,v)\le d_G(u,v),
\]
proving (2.1).

Now let \((R,(X_t)_{t\in V(R)})\) be a tree-decomposition of \(Q\) of width at most \(a\). Define
\[
Y_t=\bigcup_{q\in X_t}P_q.
\]
These sets form a tree-decomposition of the underlying unweighted graph of \(K\):

- edges inside \(P_q\) are covered whenever \(q\in X_t\);
- an edge between \(P_q\) and \(P_{q'}\) is covered by a bag containing the quotient edge \(qq'\);
- the bags containing a fixed vertex of \(P_q\) are exactly the bags whose quotient bags contain \(q\), and hence form a connected subtree.

Moreover,
\[
|Y_t|\le (a+1)(s+1).
\]
Therefore
\[
\operatorname{tw}(K)\le (a+1)(s+1)-1. \tag{2.2}
\]

Replace every weighted edge of weight \(\ell\) by a path with \(\ell\) unit edges, obtaining an ordinary graph \(H\). Subdivision does not increase tree-width, so (2.2) also holds for \(H\).

Define
\[
f(x)=a_q\qquad\text{when }x\in F_q.
\]
By (2.1),
\[
d_H(f(x),f(y))=d_G(a_q,a_{q'})
\]
for \(x\in F_q\), \(y\in F_{q'}\). Since
\[
d_G(x,a_q)\le D,\qquad d_G(y,a_{q'})\le D,
\]
the triangle inequality gives
\[
\left|d_H(f(x),f(y))-d_G(x,y)\right|\le 2D. \tag{2.3}
\]

It remains to check coarse surjectivity. Every boundary vertex \(u\in P_q\) is at \(H\)-distance at most \(D\) from \(a_q\). Every subdivision vertex on an internal weighted edge has distance at most \(D\) from one endpoint and hence at most \(2D\) from an anchor. Cross-edges have weight \(1\), so introduce no internal subdivision vertices. Thus every vertex of \(H\) is within \(2D\) of \(f(V(G))\).

Together with (2.3), this proves that \(f\) is a \((1,2D)\)-quasi-isometry. ∎

### Relation to the open hypothesis

The graphs in Theorem 2.1 do satisfy the hypothesis in the question. Lift the tree-decomposition of \(Q\) by setting
\[
B_t=\bigcup_{q\in X_t}F_q.
\]
This is a tree-decomposition of \(G\). Since every \(F_q\) lies in the \(D\)-ball around its anchor,
\[
B_t\subseteq \bigcup_{q\in X_t}B_G(a_q,D),
\]
so each bag is covered by at most \(a+1\) balls of radius \(D\).

The theorem therefore verifies the \(L=1\) conclusion for a genuine subclass of the conjectured class, including examples of unbounded degree and unbounded ordinary tree-width inside the parts. The additional hypothesis is the uniform bound \(s\) on the number of attachment vertices.

---

## 3. Unbounded interfaces when the parts are fully interchangeable

The interface bound can be removed under a different coherence assumption.

### Proposition 3.1

Let \(Q\) have tree-width at most \(a\). Replace every \(q\in V(Q)\) by a nonempty graph \(F_q\) of \(G\)-diameter at most \(D\). For every edge \(qq'\in E(Q)\), put all possible edges between \(F_q\) and \(F_{q'}\), and put no cross-edges for nonedges of \(Q\).

Then the projection
\[
\pi:V(G)\longrightarrow V(Q),\qquad \pi(x)=q\ \text{for }x\in F_q,
\]
is a \((1,D)\)-quasi-isometry. In particular, \(G\) is additively quasi-isometric to a graph of tree-width at most \(a\), even if the parts and their interfaces are arbitrarily large.

### Proof

If \(x\in F_q\), \(y\in F_{q'}\), with \(q\ne q'\), projecting any \(G\)-path gives a \(Q\)-walk, and hence
\[
d_Q(q,q')\le d_G(x,y).
\]
Conversely, a shortest \(Q\)-path can be lifted edge-for-edge from \(x\) to \(y\), since every adjacent pair of fibres is completely joined. Thus
\[
d_G(x,y)=d_Q(q,q').
\]
If \(x,y\in F_q\), then \(d_Q(\pi(x),\pi(y))=0\) while \(d_G(x,y)\le D\). The projection is surjective, so it is a \((1,D)\)-quasi-isometry. ∎

This includes lexicographic blow-ups of bounded-tree-width graphs. It demonstrates that large balls and large interfaces are not themselves obstructions; the unresolved issue is their potentially incoherent external behaviour.

---

## 4. The bounded-geometry case collapses to ordinary tree-width

### Proposition 4.1

Suppose \(G\) has a \((k,r)\)-centred tree-decomposition and
\[
M_r:=\sup_{v\in V(G)}|B_G(v,r)|<\infty.
\]
Then
\[
\operatorname{tw}(G)\le kM_r-1.
\]
Consequently the identity \(G\to G\) is a \((1,0)\)-quasi-isometry to a bounded-tree-width graph.

### Proof

Every decomposition bag is contained in a union of at most \(k\) balls, each containing at most \(M_r\) vertices. Hence every bag has size at most \(kM_r\). ∎

In particular, if \(G\) has maximum degree at most \(\Delta<\infty\) and \(r\) is an integer, then
\[
M_r\le 1+\Delta\sum_{j=0}^{r-1}(\Delta-1)^j.
\]
Thus no bounded-degree graph can be a counterexample. More generally, a uniform counterexample family must have unbounded local geometry at the relevant radius. The case \(r=0\) is also immediate: the given decomposition already has width at most \(k-1\).

---

## 5. Why direct contraction of the balls is insufficient

A bounded-diameter partition does not by itself give an additive quasi-isometry to its quotient. Consider the path
\[
G_m=0\,1\,2\,\cdots\,(2m-1)
\]
and partition it into the adjacent pairs
\[
F_i=\{2i,2i+1\},\qquad 0\le i<m.
\]
Every part has diameter \(1\), and the quotient is the path on \(m\) vertices. Nevertheless, for the quotient projection,
\[
d_{G_m}(0,2m-1)=2m-1,\qquad
d_Q(F_0,F_{m-1})=m-1.
\]
The additive error is \(m\), so it is not uniformly bounded.

This is not a counterexample to the conjecture—\(G_m\) is itself a tree. It shows why the naïve proof strategy fails: collapsing one bounded-diameter set may save only \(O(r)\), but a long geodesic can pass through arbitrarily many such sets, causing linear accumulation.

Theorem 2.1 avoids this by retaining every interface vertex and preserving the exact intrinsic terminal metric of each part. In the general problem this approach encounters two serious obstacles:

1. the covering balls are specified separately for each decomposition bag and need not arise from a global partition;
2. one radius-\(r\) ball can have arbitrarily many externally inequivalent attachment vertices.

Retaining all such attachment states can destroy the tree-width bound, while identifying them risks precisely the accumulated distortion illustrated above. The complete-join case works because all attachment vertices are metrically interchangeable, but arbitrary ball-covered bags need not have this property.

## 6. Conclusion

The full \(L=1\) question is not resolved here, and no counterexample is produced. The main rigorous extension is Theorem 2.1: additive quasi-isometry holds for bounded-diameter blow-ups of bounded-tree-width quotients with bounded interfaces, with explicit constants
\[
C=2D,\qquad
\operatorname{tw}(H)\le (a+1)(s+1)-1.
\]
The unresolved core is the simultaneous treatment of unbounded, incoherent interfaces and the absence of a globally consistent partition behind the locally chosen ball covers.