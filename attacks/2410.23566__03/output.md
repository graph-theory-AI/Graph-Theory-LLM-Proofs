```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but C=4 suffices when no weak component of D-v contains both an in-neighbor and an out-neighbor of v, and an explicit constant exists when the underlying graph of D-v has bounded feedback-vertex number.",
  "would_publish": false,
  "caveats": "The arguments do not control a mixed component of D-v with unbounded feedback complexity."
}
```

# Mathematical writeup

## 1. Statement and notation

Write
\[
r(F):=\operatorname{unvd}(F).
\]
Containment is as a not necessarily induced subdigraph. Thus, if \(F\subseteq G\), then
\[
r(F)\le r(G).
\]
Also \(r(F)\ge |V(F)|\) for every nonempty \(F\).

Let \(D\) be an acyclic digraph, let \(v\in V(D)\), and put
\[
H=D-v,\qquad m=r(H).
\]
I assume \(H\neq\varnothing\), which is the intended nontrivial range. The one-vertex case depends only on the convention for \(r(\varnothing)\).

I do not prove or disprove the conjecture. I give several rigorous special cases and a useful reduction.

---

## 2. It suffices to consider universal \(v\)

### Lemma 2.1
For every acyclic \(D\) and \(v\in V(D)\), there is an acyclic superdigraph \(\widehat D\) on the same vertex set such that

1. \(D\subseteq \widehat D\);
2. \(\widehat D-v=D-v\);
3. \(v\) is adjacent to every other vertex of \(\widehat D\).

#### Proof
Fix a topological ordering of \(D\). For every vertex \(u\) nonadjacent to \(v\), add the arc between \(u\) and \(v\) in the forward direction of this ordering. Every old and new arc is forward, so the resulting digraph remains acyclic. Only arcs incident with \(v\) were added. ∎

Consequently, a uniform bound for the case in which \(v\) is universal would prove the full conjecture.

For such a universal \(v\), a topological ordering can be chosen in the form
\[
L,\ v,\ R,
\]
where every vertex of \(L\) dominates \(v\) and \(v\) dominates every vertex of \(R\). Every arc of \(H\) between \(L\) and \(R\) points from \(L\) to \(R\). The unresolved issue is therefore a rooted embedding problem: find a copy of \(H\) respecting the in/out partition of some tournament vertex.

---

## 3. A balanced-vertex lemma

### Lemma 3.1
Let \(p,q\ge1\). Every tournament on
\[
2p+2q-1
\]
vertices has a vertex \(x\) satisfying
\[
d^-(x)\ge p,\qquad d^+(x)\ge q.
\]

#### Proof
Choose an ordering
\[
x_1,\ldots,x_N,\qquad N=2p+2q-1,
\]
maximizing the number of forward arcs.

For every \(i\), among \(x_1,\ldots,x_{i-1}\), the vertex \(x_i\) has at least as many in-neighbors as out-neighbors. Otherwise, moving \(x_i\) immediately before \(x_1\) would increase the number of forward arcs.

Likewise, among \(x_{i+1},\ldots,x_N\), the vertex \(x_i\) has at least as many out-neighbors as in-neighbors; otherwise moving \(x_i\) to the end would improve the ordering.

Take \(i=2p\). There are \(2p-1\) earlier vertices and \(2q-1\) later vertices. Hence
\[
d^-(x_{2p})\ge p,\qquad d^+(x_{2p})\ge q.
\]
∎

The order of magnitude is best possible for a statement depending only on the two semidegrees: two regular tournaments of order \(2p-1\), with every arc directed from one block to the other, show the obstruction when \(p=q\).

---

## 4. A \(C=4\) component-separation theorem

Let
\[
B=N_D^-(v),\qquad A=N_D^+(v).
\]

### Theorem 4.1
Suppose \(V(H)\) has a partition
\[
V(H)=P\mathbin{\dot\cup}Q
\]
such that

1. there is no arc of \(H\) between \(P\) and \(Q\);
2. \(B\subseteq P\);
3. \(A\subseteq Q\).

If \(P,Q\neq\varnothing\), then
\[
r(D)\le 2r(H[P])+2r(H[Q])-1.
\]
In particular,
\[
r(D)\le 4r(H)-1.
\]

#### Proof
Put
\[
p=r(H[P]),\qquad q=r(H[Q]).
\]
Let \(T\) be a tournament on \(2p+2q-1\) vertices. By Lemma 3.1, \(T\) has a vertex \(x\) with
\[
|N_T^-(x)|\ge p,\qquad |N_T^+(x)|\ge q.
\]
Thus \(N_T^-(x)\) contains a copy of \(H[P]\), while \(N_T^+(x)\) contains a copy of \(H[Q]\).

Use \(x\) as the image of \(v\). Every image of a vertex of \(P\) dominates \(x\), and \(x\) dominates every image of a vertex of \(Q\). This preserves all arcs incident with \(v\), because \(B\subseteq P\) and \(A\subseteq Q\). There are no required arcs between \(P\) and \(Q\), so the two independently chosen copies combine to give a copy of \(D\).

Finally, \(H[P]\) and \(H[Q]\) are subdigraphs of \(H\), so \(p,q\le r(H)\). ∎

If one side is empty, then \(v\) is a source or sink, and the standard argument gives \(r(D)\le2r(H)\).

### Corollary 4.2
If no weak component of \(H=D-v\) contains both a vertex of \(N_D^-(v)\) and a vertex of \(N_D^+(v)\), then
\[
r(D)\le4r(D-v)-1.
\]

#### Proof
Put in \(P\) all weak components meeting \(N_D^-(v)\), and in \(Q\) all weak components meeting \(N_D^+(v)\); components meeting neither side can be assigned arbitrarily. Distinct weak components have no arcs between them. Apply Theorem 4.1. ∎

### Corollary 4.3
For every oriented forest \(D\) and every \(v\in V(D)\),
\[
r(D)\le4r(D-v)-1.
\]

Indeed, if two neighbors of \(v\) belonged to the same weak component of \(D-v\), the underlying undirected graph of \(D\) would contain a cycle. Thus every component of \(D-v\) contains at most one neighbor of \(v\), and Corollary 4.2 applies.

This gives an elementary ratio bound for arbitrary vertices of oriented trees, not merely for sources and sinks.

---

## 5. The complete case has \(C=2\)

Let \(\operatorname{TT}_h\) denote the transitive tournament on \(h\) vertices.

### Proposition 5.1
If \(H=D-v\) is a tournament, then
\[
r(D)\le2r(H).
\]

#### Proof
Since \(H\) is acyclic and complete, \(H=\operatorname{TT}_h\). By Lemma 2.1, \(D\) is contained in an acyclic tournament on \(h+1\) vertices, hence in \(\operatorname{TT}_{h+1}\).

If \(m=r(\operatorname{TT}_h)\), every tournament on \(2m\) vertices has a vertex with at least \(m\) out-neighbors. Those out-neighbors contain \(\operatorname{TT}_h\), and adjoining the chosen vertex as a source gives \(\operatorname{TT}_{h+1}\). Thus
\[
r(D)\le r(\operatorname{TT}_{h+1})\le2m.
\]
∎

This treats a dense class not covered by the bounded-feedback-vertex result below.

---

## 6. Bounded feedback-vertex number of \(D-v\)

I now use the theorem explicitly stated in the supplied source paper:

> If an acyclic digraph \(E\) is obtained from an oriented tree \(F\) of order \(n\) by adding \(q\) universal vertices, then
> \[
> r(E)\le 2\cdot 3^{(q+1)(2q+1)}\,n.
> \tag{6.1}
> \]

Here “universal” means adjacent to every other vertex.

Let \(\underline H\) denote the underlying undirected graph of \(H\).

### Theorem 6.1
Suppose \(S\subseteq V(H)\), \(|S|=k\), and \(\underline H-S\) is a forest. Then
\[
r(D)
 \le
2\cdot 3^{(k+2)(2k+3)}\bigl(|V(H)|-k\bigr)
 \le
2\cdot 3^{(k+2)(2k+3)}r(H).
\tag{6.2}
\]

Consequently, Conjecture 9 holds with an explicit constant on every class for which the undirected feedback-vertex number of \(D-v\) is bounded.

#### Proof
Let
\[
R=V(H)\setminus S,\qquad U=S\cup\{v\}.
\]
Thus \(|U|=k+1\). Fix a topological ordering of \(D\).

The underlying graph of \(H[R]\) is a forest. Add \(c-1\) arcs between its \(c\) components so that its underlying graph becomes a tree; orient every added arc forward in the fixed topological ordering. Call the resulting oriented tree \(F\). It has
\[
|V(F)|=|R|=|V(H)|-k.
\]

Next, for every nonadjacent pair with at least one endpoint in \(U\), add the forward arc in the topological ordering. This makes every vertex of \(U\) universal. Call the resulting digraph \(E\).

All arcs of \(E\) point forward in the fixed order, so \(E\) is acyclic. Moreover,

- \(D\subseteq E\);
- \(E-U=F\);
- the \(k+1\) vertices of \(U\) are universal.

Applying (6.1) with \(q=k+1\) gives
\[
r(D)\le r(E)
 \le
2\cdot3^{(k+2)(2k+3)}|R|.
\]
Since \(r(H)\ge |V(H)|\ge|R|\), the second inequality in (6.2) follows. ∎

### Corollary 6.2
If the underlying graph of \(D-v\) is a forest, then
\[
r(D)\le1458\,r(D-v).
\]

Indeed, take \(k=0\), for which
\[
2\cdot3^{(0+2)(2\cdot0+3)}=2\cdot3^6=1458.
\]

Unlike Corollary 4.3, this allows \(v\) to have both in- and out-neighbors in the same component of \(D-v\).

---

## 7. A further bounded-separator variant

The same source theorem also yields a result in which the components left after deleting a bounded set need not be forests.

### Proposition 7.1
Let \(S\subseteq V(H)\), \(|S|=k\). Suppose \(D\) has a topological ordering with the following property. If
\[
U=S\cup\{v\}=\{u_1,\ldots,u_{k+1}\}
\]
is listed in its induced order, then every weak component of \(H-S\) lies wholly in one of the \(k+2\) gaps
\[
(-\infty,u_1),\ (u_1,u_2),\ldots,(u_{k+1},+\infty).
\]
Then
\[
r(D)\le
2(k+2)\,3^{(k+2)(2k+3)}\,r(H).
\tag{7.1}
\]

#### Proof
Put \(t=k+1\). Let \(X_i\) be the union of the components lying in the \(i\)-th gap, \(0\le i\le t\), and put
\[
p_i=r(H[X_i])
\]
for nonempty \(X_i\). Since \(H[X_i]\subseteq H\),
\[
p_i\le m=r(H).
\]

Construct a directed path \(F\) whose vertices are partitioned consecutively into blocks \(Z_i\) of orders \(p_i\). Add \(t\) universal vertices \(u_1,\ldots,u_t\), and orient all their incident arcs according to the total order
\[
Z_0,\ u_1,\ Z_1,\ u_2,\ldots,u_t,\ Z_t.
\]
The resulting digraph is acyclic and is obtained from an oriented tree of order \(\sum_i p_i\) by adding \(t\) universal vertices. By (6.1), every tournament of order
\[
2\cdot3^{(t+1)(2t+1)}\sum_{i=0}^t p_i
\]
contains it.

In such a copy, let \(W_i\) be the image of \(Z_i\). The tournament induced by \(W_i\) has order \(p_i\), so it contains \(H[X_i]\). Re-embed \(H[X_i]\) inside \(W_i\). Every vertex of \(W_i\) has the same prescribed orientation toward each \(u_j\), exactly as dictated by the corresponding gap. There are no arcs between distinct \(X_i\)'s because no weak component was split between gaps. Hence these copies, together with the vertices \(u_j\), form a copy of \(D\).

Finally,
\[
\sum_i p_i\le(t+1)m=(k+2)m,
\]
which gives (7.1). ∎

This is orthogonal to Theorem 6.1: the components of \(H-S\) may have arbitrarily complicated underlying graphs, provided they do not straddle the bounded scaffold \(S\cup\{v\}\).

---

## 8. A necessary lower bound on the conjectural constant

Any universal constant must satisfy \(C\ge2\).

Take \(D=\operatorname{TT}_3\), with \(v\) its middle vertex. Then
\[
D-v=\operatorname{TT}_2,\qquad r(D-v)=2.
\]
The cyclic triangle avoids \(\operatorname{TT}_3\), while every tournament on four vertices contains a transitive triangle. Thus
\[
r(D)=4,
\]
and
\[
\frac{r(D)}{r(D-v)}=2.
\]

---

## 9. Remaining gap

After universalizing \(v\), the difficult case has a partition
\[
V(H)=L\mathbin{\dot\cup}R
\]
with
\[
L\to v\to R
\]
and all arcs of \(H\) between the parts directed from \(L\) to \(R\). Given a tournament vertex \(x\), one needs a copy of \(H\) with
\[
L\subseteq N^-(x),\qquad R\subseteq N^+(x).
\]

Lemma 3.1 provides large sets on both sides of \(x\), but independently embedding \(H[L]\) and \(H[R]\) gives no control over the required arcs from the first copy to the second. The component-separation theorem is exactly the case in which there are no such cross-arcs. The bounded-feedback and bounded-scaffold arguments avoid the problem by invoking the source paper's universal-extension theorem, but their constants depend on structural parameters that can grow with \(D\).

Thus no absolute constant for the general case has been obtained, and no counterexample is produced.