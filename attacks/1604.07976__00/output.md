```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A linear-size incidence-matching formulation is exact when one vertex meets every noncontractible cycle, while an explicit torus embedding shows why the same formulation fails in general.",
  "would_publish": false,
  "caveats": "The full conjecture remains open; the intended simple-graph convention and cellular embeddings are assumed."
}
```

# Mathematical writeup

## 1. Statement and conventions

For a connected graph \(G=(V,E)\), let

\[
P_{\mathrm{st}}(G)=\operatorname{conv}\{\chi^T:T\subseteq E\text{ is a spanning tree of }G\}.
\]

The conjecture is that, for every fixed surface \(\Sigma\), every connected \(n\)-vertex graph embedded in \(\Sigma\) satisfies

\[
\operatorname{xc}(P_{\mathrm{st}}(G))=O_\Sigma(n).
\]

The simple-graph convention is essential. If parallel edges are allowed, two vertices joined by \(q\) parallel edges give

\[
P_{\mathrm{st}}(G)=\operatorname{conv}\{e_1,\dots,e_q\},
\]

a \((q-1)\)-simplex of extension complexity \(q\), while \(|V|=2\). Thus the literal statement without a simplicity or \(|E|=O(|V|)\) assumption is false.

Below, \(\gamma\) denotes Euler genus, so a cellular embedding satisfies

\[
|V|-|E|+|F|=2-\gamma.
\]

For a simple graph on a fixed surface, \(|E|=O_\Sigma(|V|)\).

---

## 2. A linear formulation with a precise topological hypothesis

### Theorem

Let \(G\) be a connected simple graph cellularly embedded in a closed surface \(\Sigma\). Suppose there is a vertex \(r\in V(G)\) such that every noncontractible cycle of the embedded graph contains \(r\). Then

\[
\operatorname{xc}(P_{\mathrm{st}}(G))=O(|E|).
\]

Consequently, for every fixed \(\Sigma\),

\[
\operatorname{xc}(P_{\mathrm{st}}(G))=O_\Sigma(|V|).
\]

In particular, this applies when \(G-r\) is contained in a topological disk.

### Construction

Choose a face \(f_0\) incident with \(r\). Define a bipartite incidence graph \(B\) as follows:

- its left side has one node \(p_e\) for each \(e\in E\);
- its right side is
  \[
  (V\setminus\{r\})\ \dot\cup\ (F\setminus\{f_0\});
  \]
- \(p_e\) is adjacent to each nonroot endpoint of \(e\), and to each nonroot face incident with \(e\).

Use separate links for separate incidences if an edge has the same face on both sides. Let \(w_\ell\) be the variable associated with a link \(\ell\) of \(B\), and consider

\[
\begin{aligned}
w_\ell&\ge 0 &&\text{for every link }\ell,\\
w(\delta_B(s))&=1 &&\text{for every right-side node }s,\\
w(\delta_B(p_e))&\le 1 &&\text{for every }e\in E.
\end{aligned}
\tag{1}
\]

This is a face of a bipartite matching polytope and is therefore integral. There are at most \(4|E|\) link variables.

Define the projection

\[
x_e=\sum_{\substack{\ell=p_ev\\v\in V\setminus\{r\}}}w_\ell.
\tag{2}
\]

Thus \(x_e=1\) at an integral point precisely when the edge-node \(p_e\) is matched to a vertex rather than to a face.

Euler's formula gives

\[
(|V|-1)+(|F|-1)=|E|-\gamma,
\]

so an integral matching satisfying (1) leaves exactly \(\gamma\) edge-nodes unmatched.

---

## 3. Every spanning tree has a lift

Let \(T\) be a spanning tree.

1. Root \(T\) at \(r\), and match every \(v\neq r\) to its parent edge in \(T\).
2. The dual subgraph formed by \(E\setminus T\) is connected.

For the second assertion, suppose otherwise and take a nontrivial union of components of the dual complement. The primal edges dual to its boundary all belong to \(T\). At every primal vertex this boundary has even degree, so it is a nonempty even subgraph and therefore contains a cycle, contradicting that \(T\) is a tree.

Hence \(E\setminus T\) contains a dual spanning tree. Root such a dual tree at \(f_0\) and match every face \(f\neq f_0\) to its parent dual edge. These two matchings are edge-disjoint, so they define a feasible integral point of (1) projecting to \(\chi^T\).

This part holds on every surface.

---

## 4. Structure of the unwanted integral points

Let \(w\) be an integral point of (1), and let \(A\subseteq E\) be the edges matched to vertices. Then \(|A|=|V|-1\).

Consider a connected component \(K\) of \((V,A)\).

- If \(r\in V(K)\), every vertex of \(K\) except \(r\) owns exactly one edge of \(K\), so
  \[
  |A(K)|=|V(K)|-1.
  \]
  Thus \(K\) is a tree.
- If \(r\notin V(K)\), every vertex of \(K\) owns exactly one edge, so
  \[
  |A(K)|=|V(K)|.
  \]
  Thus \(K\) is unicyclic.

Therefore \(A\) is a spanning tree exactly when it has no nonroot unicyclic component.

For arbitrary cellular embeddings, one gets the exact reduction

\[
P_{\mathrm{st}}(G)
=
\operatorname{conv}\left\{
\pi(w):
w\text{ is an integral solution of (1) and }(V,A(w))\text{ is connected}
\right\}.
\tag{3}
\]

The difficulty is imposing this last connectivity condition without losing the linear size and integrality.

---

## 5. Why the topological hypothesis makes connectivity automatic

Suppose \(A\) has a nonroot component, and let \(C\) be its unique cycle. Then \(C\) avoids \(r\). By hypothesis, \(C\) is contractible.

We first claim that \(C\) bounds a disk \(D\) not containing \(r\).

- On the sphere, choose the disk side not containing \(r\).
- On a surface of positive Euler genus, suppose instead that the disk bounded by \(C\) contained \(r\). The part of the cellular embedding outside that disk is a cell decomposition of a punctured surface of positive genus, whose 1-skeleton avoids \(r\). Its mod-\(2\) cycle space maps onto a nonzero part of \(H_1(\Sigma;\mathbb F_2)\). Hence that 1-skeleton contains a graph-theoretic noncontractible cycle avoiding \(r\), contradicting the hypothesis.

Since \(f_0\) is incident with \(r\), it also lies outside \(D\).

Let:

- \(k=|E(C)|=|V(C)|\);
- \(v\) be the number of vertices strictly inside \(D\);
- \(e\) be the number of edges strictly inside \(D\), excluding \(C\);
- \(f\) be the number of faces inside \(D\).

Euler's formula for the cell decomposition of the disk gives

\[
(k+v)-(k+e)+f=1,
\]

hence

\[
e=v+f-1.
\tag{4}
\]

All \(k\) edges of \(C\) are vertex-matched. Since they can only be matched to the \(k\) vertices of \(C\), they exhaust all boundary-vertex slots.

The \(v\) interior vertex slots and \(f\) interior face slots must therefore be matched using only the \(e\) interior edge-nodes. But (4) says that there are \(v+f\) such slots and only \(v+f-1\) available edge-nodes, a contradiction.

Thus \(A\) has no nonroot component. It is connected and has \(|V|-1\) edges, hence is a spanning tree. Since the matching polytope (1) is integral and every spanning tree has a lift, its projection is exactly \(P_{\mathrm{st}}(G)\).

The formulation has \(O(|E|)\) variables and inequalities. This proves the theorem.

---

## 6. Explicit failure of the formulation on the torus

The topological condition cannot simply be omitted.

Let

\[
V=\{r,a,b,c\},\qquad
E=\{ra,rb,ab,bc,ca\}.
\]

Give this graph the orientable rotation system

\[
\begin{aligned}
r&:(ra,rb),\\
a&:(ar,ab,ac),\\
b&:(br,ba,bc),\\
c&:(cb,ca).
\end{aligned}
\]

With the convention that a face step reverses a dart and then takes the next dart in the cyclic order, the unique face walk is

\[
ra,ab,bc,ca,ar,rb,ba,ac,cb,br.
\]

Thus the embedding has one face, and

\[
|V|-|E|+|F|=4-5+1=0,
\]

so it is a cellular torus embedding, of Euler genus \(2\).

Choose root vertex \(r\) and the unique face as \(f_0\). There are no face slots. The matching

\[
ab\mapsto a,\qquad bc\mapsto b,\qquad ca\mapsto c
\]

saturates all nonroot vertex slots, leaving \(ra\) and \(rb\) unmatched. Its projection is the triangle \(abc\), not a spanning tree: for \(S=\{a,b,c\}\),

\[
x(E(S))=3>|S|-1=2.
\]

This graph is abstractly planar, so this is not a counterexample to the conjecture. It is, however, a fully explicit counterexample to the claim that the surface-incidence matching formulation is automatically exact beyond the planar case.

---

## 7. Remaining gap

For a general fixed-surface embedding, integral points of (1) may contain nonroot cycle-rooted components supported by essential topology. The conjecture would follow from an \(O(|E|)\)-size formulation for the connected sector in (3), but the matching formulation alone does not provide it. Adding ordinary flow or ordering constraints to (1) does not suffice without an integrality argument; intersections of integral polytopes with such constraints can acquire fractional vertices.

Thus the argument proves the conjectured linear bound for embeddings with a one-vertex transversal of all noncontractible cycles and gives an exact linear-size relaxation/reduction in general, but it does not improve the known \(O(n^{3/2})\) bound for high-face-width examples such as large toroidal grids.