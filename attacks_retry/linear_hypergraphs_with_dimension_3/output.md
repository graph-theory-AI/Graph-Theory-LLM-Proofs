```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds whenever every vertex-node has degree at most three in the 2-core of the incidence graph, even when total incidence degrees are unbounded.",
  "would_publish": false,
  "caveats": "The unrestricted high-core-degree case remains unresolved; novelty is unchecked, and the intended finite Sperner convention is used."
}
```

# A core-sensitive partial result

I verify and reuse the bounded-incidence construction from the previous attempt, and extend it using a private-boundary lemma and a carefully chosen subhypergraph.

The extension is needed because simply representing the incidence graph’s 2-core and reattaching everything is not justified: a deleted tree can attach at a **hyperedge-node**, where there need not be an available geometric attachment point.

## 1. Statement and conventions

Work with finite Sperner hypergraphs whose nonempty edges cover the vertex set, as required by the maximal-intersection convention in the question. Singleton components are harmless. All geometric objects below are closed and filled.

For \(H=(V,\mathcal E)\), a representation means
\[
\bigcap_{v\in S}T_v\ne\varnothing
\quad\Longleftrightarrow\quad
S\subseteq e\text{ for some }e\in\mathcal E
\tag{1}
\]
for every nonempty \(S\subseteq V\). Since \(H\) is Sperner, this says precisely that its edges are the maximal intersecting subfamilies.

Let \(B(H)\) be the incidence graph, and let \(C\) be its **2-core**: the maximal induced subgraph of minimum degree at least two. Set
\[
d_C(v)=
\begin{cases}
\deg_C(v),&v\in V(C)\cap V,\\
0,&v\notin V(C).
\end{cases}
\]

### Theorem

Let \(H\) be a finite linear Sperner hypergraph with incidence-poset dimension at most three. Then \(H\) has a representation by nondegenerate convex polygons \(T_v\) satisfying
\[
\#\{\text{corners of }T_v\}\le \max\{3,d_C(v)\}
\qquad(v\in V).
\tag{2}
\]

Consequently, the conjecture holds if
\[
d_C(v)\le 3\qquad\text{for every original vertex }v.
\tag{3}
\]
In this case, nondegenerate triangles alone suffice.

Thus a counterexample, if one exists, must have an original vertex incident with at least four hyperedges **within the incidence graph’s 2-core**, not merely in the full hypergraph.

---

## 2. The convex-hull construction, checked

I first establish the geometric ingredient independently of the other claims in the previous attempt.

### Lemma 1

Let \(H\) be a finite Sperner hypergraph of incidence dimension at most three, and let \(d_H(v)\) denote its vertex-incidence degrees. There is a representation satisfying (1) in which \(T_v\) is a nondegenerate convex polygon with at most
\[
\max\{3,d_H(v)\}
\]
corners.

Linearity is not needed for this lemma.

### Proof

Put \(N=|V|+|\mathcal E|\). Choose three linear extensions \(L_1,L_2,L_3\) realizing the incidence poset, repeating an extension if necessary. Let \(r_i(x)\) be the position of \(x\) in \(L_i\).

For \(e\in\mathcal E\), define
\[
q_e=\left(
4^{N-r_1(e)},\,
4^{N-r_2(e)},\,
4^{N-r_3(e)}
\right).
\]
Use the projection
\[
\pi(x_1,x_2,x_3)=(x_1-x_3,x_2-x_3),
\]
and set
\[
p_e=\pi(q_e),\qquad
K_v=\operatorname{conv}\{p_e:v\in e\}.
\]

Write \(D=[-1,1]^2\). I claim that
\[
\bigcap_{v\in S}(K_v+D)\ne\varnothing
\quad\Longleftrightarrow\quad
S\subseteq e\text{ for some }e\in\mathcal E.
\tag{4}
\]

The reverse implication follows from the common point \(p_e\).

For the other direction, suppose that no edge contains \(S\), but that \(z\) belongs to the intersection on the left. For each \(v\in S\), choose
\[
x^v\in\operatorname{conv}\{q_e:v\in e\},
\qquad \delta^v\in D,
\]
such that
\[
z=\pi(x^v)+\delta^v.
\]

Define
\[
a_i(v)=4^{N-r_i(v)-1}.
\]
Since \(v<e\) in every realizing order whenever \(v\in e\),
\[
x_i^v\le a_i(v).
\tag{5}
\]
Now put
\[
R_i=\max_{v\in S}r_i(v),\qquad
a_i=\min_{v\in S}a_i(v)=4^{N-R_i-1}.
\]
Every vertex has an incident edge, so \(a_i\ge1\).

Let
\[
y^v=x^v+(\delta_1^v,\delta_2^v,0).
\]
All these points have projection \(z\); hence their differences are multiples of \((1,1,1)\). Choose \(v_0\) minimizing \(y_3^v\). Then
\[
y^{v_0}\le y^v
\]
coordinatewise for every \(v\in S\). Using (5),
\[
x_i^{v_0}\le a_i+2\quad(i=1,2),
\qquad x_3^{v_0}\le a_3.
\]
Therefore
\[
\sum_{i=1}^3\frac{x_i^{v_0}}{a_i}
\le 3+\frac2{a_1}+\frac2{a_2}
\le7.
\tag{6}
\]

On the other hand, for every edge \(e\), choose \(w\in S\setminus e\). The elements \(e,w\) are incomparable, so some realizing order has \(e<w\). For its index \(i\),
\[
r_i(e)\le r_i(w)-1\le R_i-1,
\]
and hence
\[
(q_e)_i\ge4^{N-R_i+1}=16a_i.
\]
It follows that
\[
\sum_{i=1}^3\frac{(q_e)_i}{a_i}\ge16
\]
for every edge \(e\), and therefore for every convex combination of the \(q_e\). This contradicts (6), proving (4).

Consequently, any choices satisfying
\[
K_v\subseteq T_v\subseteq K_v+D
\tag{7}
\]
preserve the required intersection pattern.

If \(K_v\) is two-dimensional, retain it. It has at most \(d_H(v)\) corners. If it is a segment \([a,b]\), choose a coordinate unit vector \(u\) not parallel to \(b-a\), and use
\[
T_v=\operatorname{conv}\{a,b,a+u\}.
\]
If \(K_v=\{p\}\), use
\[
T_v=\operatorname{conv}\{p,p+(1,0),p+(0,1)\}.
\]
These are nondegenerate triangles satisfying (7). This proves the lemma. \(\square\)

In particular, the previous attempt’s maximum-degree-three result is valid. The construction above also gives integer coordinates of \(O(N)\) bits for this initial representation.

---

## 3. Private boundary points and tree attachments

The next lemma is where linearity enters.

### Lemma 2: private boundary

Suppose a linear Sperner hypergraph is represented as in (1) by nondegenerate convex polygons. If \(v\) belongs to at least two hyperedges, then \(T_v\) has a boundary point belonging to no other polygon.

Moreover, such a point can be chosen in the relative interior of a side of \(T_v\).

### Proof

For each edge \(e\ni v\), define
\[
A_e=T_v\cap\bigcup_{u\in e\setminus\{v\}}T_u.
\]
Since \(v\) has degree at least two and the hypergraph is Sperner, every such \(e\) has another member.

The sets \(A_e\) have three useful properties:

1. They are nonempty and compact.
2. Each \(A_e\) is star-shaped with respect to any point
   \[
   p_e\in\bigcap_{u\in e}T_u.
   \]
   Indeed, it is a union of convex sets \(T_v\cap T_u\), all containing \(p_e\).
3. They are pairwise disjoint.

For the third property, if \(x\in A_e\cap A_f\) for distinct edges \(e,f\ni v\), then some
\[
u\in e\setminus\{v\},\qquad w\in f\setminus\{v\}
\]
satisfy \(x\in T_v\cap T_u\cap T_w\). By (1), an edge \(g\) contains \(v,u,w\). Since \(g\) and \(e\) share \(v,u\), linearity forces \(g=e\). Then \(e,f\) share \(v,w\), a contradiction.

Every point of \(T_v\) covered by another polygon belongs to one of the \(A_e\). Suppose the entire boundary \(\partial T_v\) were covered. Because \(\partial T_v\) is connected and the finitely many \(A_e\) are pairwise disjoint compact sets, one \(A_e\) would contain all of \(\partial T_v\).

But \(A_e\) is star-shaped with respect to \(p_e\). Every point of \(T_v\) lies on a segment from \(p_e\) to a boundary point, so \(A_e=T_v\). This contradicts the existence of another nonempty, disjoint \(A_f\).

Thus a private boundary point exists. The set of private points is relatively open in \(\partial T_v\), so it contains a point in the relative interior of a polygon side. \(\square\)

### Lemma 3: attaching one hyperedge

Suppose \(T_v\) has a private boundary point. One can add a hyperedge
\[
e=\{v,u_1,\ldots,u_k\},\qquad k\ge1,
\]
where the \(u_j\) are new vertices, without changing any existing polygon, using nondegenerate triangles for the new vertices.

Each new triangle has private boundary points.

### Proof

Choose a private point \(q\) in the interior of a side of \(T_v\), and a sufficiently small disk about \(q\) disjoint from all other existing polygons.

In the open half-plane exterior to that side, choose \(k\) small triangular wedges with common apex \(q\), pairwise disjoint except at \(q\). Keep all of them inside the disk.

Each new triangle meets the old family exactly at \(q\in T_v\), and all new triangles meet there. Thus the only new maximal intersecting subfamily is \(e\). Every point of a new triangle’s boundary other than \(q\) is private at this stage. \(\square\)

This permits an arbitrary incidence tree to be attached at such a vertex. Process its hyperedge-nodes outwards: every new hyperedge has exactly one previously represented vertex, and all its other vertices are new.

The constructions can be made with rational coordinates.

---

## 4. Constructing a suitable skeleton

We now prove the theorem.

A standard elementary property of the 2-core is useful:

> Every component outside the 2-core is a tree and has at most one attachment to the core.

Indeed, every cycle lies in the 2-core. If an outside tree had two attachments, the path between them could be added to the core while preserving minimum degree at least two, contradicting maximality.

### 4.1. Components with empty 2-core

Such an incidence component is a tree.

Begin with one hyperedge. Represent all its vertices by small triangular wedges with a common apex and otherwise pairwise disjoint. All these triangles have private boundary points. Then process the rest of the incidence tree outwards using Lemma 3.

Thus all forest components have triangle representations.

### 4.2. Components with nonempty 2-core

The important step is to choose an **edge-induced subhypergraph**
\[
H_0=(V_0,\mathcal E_0)
\]
with these properties:

- every core hyperedge belongs to \(\mathcal E_0\);
- for a core vertex \(v\),
  \[
  d_{H_0}(v)=d_C(v);
  \tag{8}
  \]
- every selected vertex outside the core has degree at most two in \(H_0\);
- every omitted part is an incidence tree attached to \(H_0\) at an original vertex \(v\) with
  \[
  d_{H_0}(v)\ge2.
  \tag{9}
  \]

Here “edge-induced” means that every selected edge is retained with **all of its original members**.

Construct \(H_0\) as follows.

1. Select every hyperedge-node in the core, together with all its original member vertices.
2. Do not initially select any off-core hyperedge adjacent to a core vertex.
3. Root each off-core tree towards its attachment to the core.
4. Whenever an off-core original vertex \(v\) has been selected, inspect its child hyperedges:
   - if it has none, do nothing;
   - otherwise select exactly one child hyperedge, include all its child vertices, and continue recursively.

An off-core selected vertex has its parent hyperedge and at most one selected child hyperedge, so its degree is at most two.

If such a vertex has any omitted child hyperedges, it also has a selected child hyperedge, and therefore has degree exactly two in \(H_0\). A core vertex at which omitted trees attach has degree at least two by definition of the core.

Because every selected hyperedge retains all its members, an omitted component cannot attach to \(H_0\) at an edge-node. It attaches at an original vertex. The rooted-tree construction shows that this attachment is unique. Thus all four properties hold.

This is the step that avoids the edge-node attachment difficulty.

### 4.3. Representing and completing the skeleton

The incidence poset of \(H_0\) is an induced subposet of that of \(H\), so its dimension is at most three. Apply Lemma 1.

For a core vertex \(v\), the resulting polygon has at most
\[
\max\{3,d_{H_0}(v)\}
=\max\{3,d_C(v)\}
\]
corners. Every selected off-core vertex receives a triangle.

Every vertex at which an omitted tree attaches has degree at least two in \(H_0\). By Lemma 2, its polygon has a private boundary point. Attach all the omitted incidence trees using Lemma 3.

No existing polygon is changed during these attachments, and every newly introduced object is a triangle. Consequently,
\[
\#\{\text{corners of }T_v\}\le\max\{3,d_C(v)\}
\]
for all vertices.

Finally, represent different connected components in disjoint regions of the plane. This proves the theorem. \(\square\)

---

## 5. A connected, nonplanar family with unbounded incidence degree

The condition genuinely allows unbounded degrees in connected nonplanar examples.

Start with the hypergraph from the question,
\[
\mathcal E_*=
\bigl\{
12,\ 23,\ 34,\ 14,\ 135,\ 245
\bigr\}.
\]
For \(t\ge0\), add vertices \(x_1,\ldots,x_t\) and edges
\[
\{2,x_j\}\qquad(1\le j\le t).
\]
Call the resulting hypergraph \(H_t\).

Its incidence graph remains nonplanar, since it contains the original subdivision of \(K_{3,3}\). Its 2-core is exactly the original incidence graph: each newly added path
\[
2-\{2,x_j\}-x_j
\]
is removed by leaf pruning. Thus all original vertex-nodes have core degree at most three, while
\[
d_{H_t}(2)=3+t.
\]

For completeness, the dimension bound also has an explicit certificate. Consider the following three permutations of the vertex set:
\[
\begin{aligned}
R_1&:\quad 3,4,1,5,2,x_1,\ldots,x_t,\\
R_2&:\quad 2,x_t,\ldots,x_1,3,1,5,4,\\
R_3&:\quad x_1,\ldots,x_t,2,4,5,1,3.
\end{aligned}
\tag{10}
\]

They satisfy:

- every two vertices occur in both relative orders;
- for every edge \(e\) and every \(w\notin e\), some \(R_i\) places \(w\) after all members of \(e\).

For the six original edges, the second condition on original vertices is certified by the following table; an entry \(w:i\) means that \(R_i\) places \(w\) after the edge:
\[
\begin{array}{c|l}
e&\text{certificates}\\ \hline
12&3:3,\ 4:2,\ 5:2\\
23&1:2,\ 4:2,\ 5:2\\
34&1:1,\ 2:1,\ 5:1\\
14&2:1,\ 3:3,\ 5:1\\
135&2:1,\ 4:2\\
245&1:3,\ 3:3
\end{array}
\]
Every new \(x_j\) is after every original edge in \(R_1\). For a new edge \(\{2,x_j\}\), all other original vertices come after it in \(R_2\). A distinct \(x_k\) comes after both \(2,x_j\) in \(R_1\) if \(k>j\), and in \(R_2\) if \(k<j\).

These conditions give a 3-realizer of the incidence poset: in each permutation insert every edge-element immediately after its last member. Nonincident vertex-edge pairs are reversed by the second condition. The opposite ordering follows from the vertex-antichain condition. For two distinct edges, the Sperner property supplies a member of each absent from the other, and the same separation condition reverses the two edge-elements in both directions.

Hence \(\dim P(H_t)\le3\), and the theorem gives triangle representations for every \(H_t\).

---

## 6. What remains unresolved

The result does **not** settle the original conjecture.

The construction leaves a core vertex \(v\) represented by a convex hull of up to \(d_C(v)\) witness points. When \(d_C(v)\ge4\), that hull may have more than three corners. The private-boundary argument handles tree attachments, but it does not simplify incidences lying in the 2-core: those incidences participate in cycles and cannot be reinserted independently by local fans.

In particular, there is still no justification for replacing such a polygon by an arbitrary enclosing triangle; doing so may create forbidden intersections.

The rigorous outcome is therefore:

- the bounded-incidence construction in the supplied attempt is verified;
- the polygon-complexity bound can be improved from total incidence degree to **2-core incidence degree**;
- the conjecture follows whenever every original vertex has core degree at most three;

but no proof or counterexample is obtained for the unrestricted high-core-degree case.