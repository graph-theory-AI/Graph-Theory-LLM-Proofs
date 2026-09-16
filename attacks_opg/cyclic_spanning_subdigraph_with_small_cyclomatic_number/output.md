```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "As formulated for possibly nonstrong digraphs, the claim has a ten-vertex oriented counterexample with stability number 2 and minimum cyclic-spanning cyclomatic number 3.",
  "would_publish": false,
  "caveats": "Uses the non-vacuous interpretation that every vertex must lie on a directed cycle; does not refute the version restricted to strong digraphs."
}
```

## 1. Scope and conventions

The distinction between **“strong”** and **“all strong components are nontrivial”** is decisive. The latter hypothesis allows one-way arcs between strong components. Such arcs can reduce the stability number without helping any directed cycle.

I interpret a cyclic spanning subdigraph as covering every vertex by directed cycles, with no arcs between its strong components. In particular, isolated vertices are not permitted. This is the non-vacuous interpretation required by the cycle-covering context; the alternative is discussed below.

Throughout, I use exactly the stated formula
\[
\nu(H)=|A(H)|-|V(H)|+1,
\]
even when \(H\) is disconnected.

## 2. An explicit family

For each \(i\in\{1,\ldots,k\}\), let \(B_i\) have vertices
\[
V_i=\{z_i,a_i,b_i,c_i,d_i\}
\]
and precisely the six arcs forming the two directed triangles
\[
z_i\to a_i\to b_i\to z_i,
\qquad
z_i\to c_i\to d_i\to z_i.
\]
Thus \(B_i\) consists of two directed triangles sharing only \(z_i\).

Construct \(D_k\) from the vertex-disjoint digraphs \(B_1,\ldots,B_k\) by adding **every** arc from \(V_i\) to \(V_j\) whenever \(i<j\). There are no other arcs. This is an oriented digraph: it has neither loops nor opposite pairs of arcs.

### Strong components

Each \(B_i\) is strong, since its two directed triangles share \(z_i\).

Along any directed walk in \(D_k\), the block index never decreases, and it strictly increases whenever an interblock arc is traversed. Consequently, no directed cycle uses an interblock arc, and the strong components of \(D_k\) are exactly
\[
B_1,\ldots,B_k.
\]
They are all nontrivial, as required by the stated hypothesis.

### Stability number

Vertices in distinct blocks are adjacent, so every stable set lies entirely within one \(V_i\).

Within \(B_i\), the vertex \(z_i\) is adjacent to all other vertices. Among the remaining vertices, the underlying graph consists of the two edges \(a_ib_i\) and \(c_id_i\). Hence a stable set has size at most two, and \(\{a_i,c_i\}\) attains that size. Therefore
\[
\boxed{\alpha(D_k)=2.}
\]

## 3. Every cyclic spanning subdigraph needs all six arcs in each block

Let \(H\) be a cyclic spanning subdigraph of \(D_k\).

Every vertex of \(H\) must lie on a directed cycle. As established above, every directed cycle of \(D_k\) lies entirely within one block.

Consider \(a_i\) and \(b_i\). Within \(B_i\), the only incoming and outgoing arcs available to these vertices force
\[
z_i\to a_i,\qquad a_i\to b_i,\qquad b_i\to z_i
\]
to belong to \(H\). Indeed, \(a_i\) needs its unique internal incoming and outgoing arcs, and \(b_i\) needs its unique internal outgoing arc.

Likewise, covering \(c_i\) and \(d_i\) by directed cycles forces
\[
z_i\to c_i,\qquad c_i\to d_i,\qquad d_i\to z_i.
\]
Thus all six arcs of every \(B_i\) are mandatory, giving
\[
|A(H)|\ge 6k.
\]

Conversely, the disjoint union
\[
H_0=B_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}B_k
\]
is a cyclic spanning subdigraph with exactly \(6k\) arcs. Since \(D_k\) has \(5k\) vertices,
\[
\boxed{\min_H \nu(H)=6k-5k+1=k+1.}
\]

The lower bound also holds under the weaker interpretation that every vertex, but not necessarily every arc, must lie on a directed cycle.

## 4. The counterexample

Take \(k=2\). Then \(D_2\) is a ten-vertex oriented digraph with two nontrivial strong components and
\[
\alpha(D_2)=2.
\]
Nevertheless, every cyclic spanning subdigraph \(H\) satisfies
\[
\nu(H)\ge 12-10+1=3>2=\alpha(D_2).
\]

This explicitly contradicts the conjecture as supplied.

In fact, the family proves more:

> Among digraphs whose strong components are all nontrivial, the minimum cyclomatic number of a cyclic spanning subdigraph is unbounded even when the stability number is fixed at \(2\).

## 5. What this does—and does not—resolve

The obstruction is that complete one-way joins keep the stability number at \(2\), while every block independently contributes a mandatory excess of one arc over its number of vertices.

This construction is **not strong**. It therefore does not refute the version restricted to nontrivial strong digraphs, nor does it challenge the small-stability results stated for strong digraphs. It also does not apply if the intended hypothesis was that \(D\) is a **disjoint union of nontrivial strong digraphs**. That condition is strictly stronger than requiring all strong components to be nontrivial.

There is a separate definitional issue: if “cyclic” means only that every arc lies on a directed cycle, while isolated vertices are allowed, then the edgeless spanning subdigraph qualifies and has
\[
\nu=1-|V(D)|\le \alpha(D).
\]
Under that literal interpretation, the assertion is trivial.

Thus the supplied formulation needs correction: under its meaningful cycle-covering interpretation it is false by the construction above; allowing isolated vertices instead makes it vacuous. The strong-digraph conjecture is left untouched.