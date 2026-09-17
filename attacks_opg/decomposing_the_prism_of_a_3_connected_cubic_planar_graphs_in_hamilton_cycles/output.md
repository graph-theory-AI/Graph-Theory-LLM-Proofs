```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Replacing a cubic vertex by the cube with one vertex deleted preserves Hamilton decomposability of the prism, yielding an explicit infinite 3-connected planar family.",
  "would_publish": false,
  "caveats": "This is a local preservation result, not a resolution of the conjecture; its novelty has not been checked."
}
```

## 1. A proved local preservation theorem

Write \(\Pi(G)=G\square K_2\), with \(v_0,v_1\) denoting the two copies of a vertex \(v\). Call \(v_0v_1\) its **rung**.

The following result does not require planarity.

**Proposition (cube insertion).**  
Let \(G\) be a finite simple cubic graph, and suppose that \(\Pi(G)\) has a Hamilton decomposition. Let \(v\in V(G)\).

Delete \(v\), and replace it by a copy \(T\) of the cube with one vertex deleted, attaching the three former neighbours of \(v\) bijectively to the three degree-two vertices of \(T\). Denote the resulting cubic graph by \(G'\). Then \(\Pi(G')\) has a Hamilton decomposition.

Moreover, if \(G\) is planar and 3-connected, then so is \(G'\).

Thus Hamilton decomposability of the prism is preserved by taking a cubic 3-sum with the cube. I give explicit local certificates covering every possible way the original decomposition can meet the replaced vertex.

### The replacement graph

Label
\[
V(T)=\{a,b,c,d,e,f,g\}
\]
and
\[
E(T)=\{ad,ae,bd,bf,ce,cf,dg,eg,fg\}.
\]
The attachment vertices are \(a,b,c\). In a cube, these would all be adjacent to the deleted eighth vertex.

If
\[
N_G(v)=\{x_a,x_b,x_c\},
\]
then \(G'\) consists of \(G-v\), the graph \(T\), and the three edges
\[
x_aa,\qquad x_bb,\qquad x_cc.
\]
In particular,
\[
|V(G')|=|V(G)|+6.
\]

## 2. How a Hamilton decomposition meets the replaced vertex

Let \(R,B\) be a Hamilton decomposition of \(\Pi(G)\). Interchange their names if necessary so that \(v_0v_1\in E(R)\).

At each of \(v_0,v_1\), precisely one horizontal edge belongs to \(R\), and the other two belong to \(B\).

Deleting \(v_0,v_1\) has the following effects:

* Since they are adjacent in \(R\), what remains of \(R\) is one spanning path.
* Since they are not adjacent in \(B\), what remains of \(B\) consists of two vertex-disjoint paths spanning the remaining vertices.
* Each of these two blue paths joins a former neighbour of \(v_0\) to a former neighbour of \(v_1\). Indeed, they are the two arcs between \(v_0\) and \(v_1\) in the blue Hamilton cycle.

For bookkeeping, label an outside endpoint \((x_t)_i\) by the corresponding new attachment terminal \(t_i\).

There are only two types of red boundary condition.

1. **Aligned:** the red horizontal edge uses \(x_a\) in both layers. The new red path must have endpoints \(a_0,a_1\). The blue terminals are
   \[
   b_0,c_0,b_1,c_1.
   \]
2. **Skew:** after relabelling, the red horizontal edges use \(x_a\) in layer \(0\) and \(x_b\) in layer \(1\). The new red path must have endpoints \(a_0,b_1\). The blue terminals are
   \[
   b_0,c_0,a_1,c_1.
   \]

The labels \(a,b,c\) can be permuted arbitrarily by automorphisms of \(T\), so these cases exhaust all possibilities.

## 3. Explicit local certificates

The graph \(\Pi(T)\) has 14 vertices and
\[
2|E(T)|+|V(T)|=25
\]
edges.

Below, a word denotes the vertex sequence of a path. In each certificate:

* the red path contains all 14 vertices and hence has 13 edges;
* the two blue paths are vertex-disjoint and together contain all 14 vertices;
* their 12 edges are exactly the edges not in the red path.

These claims can be checked directly from the displayed edge set of \(T\). Thus each certificate partitions **all** edges of \(\Pi(T)\), with no additional cycle components.

### Certificate A: aligned red endpoints

The red endpoints are \(a_0,a_1\):
\[
\begin{aligned}
R_A={}&
a_0\,d_0\,g_0\,g_1\,d_1\,b_1\,b_0\,
f_0\,f_1\,c_1\,c_0\,e_0\,e_1\,a_1,\\[2mm]
B_A^{(1)}={}&
b_0\,d_0\,d_1\,a_1\,a_0\,e_0\,g_0\,f_0\,c_0,\\
B_A^{(2)}={}&
b_1\,f_1\,g_1\,e_1\,c_1.
\end{aligned}
\]
The blue endpoint pairing is
\[
\bigl\{\{b_0,c_0\},\{b_1,c_1\}\bigr\}.
\]
In particular, both blue paths pair terminals **within** a layer.

### Certificate S1: skew red endpoints, first blue pairing

The red endpoints are \(a_0,b_1\):
\[
\begin{aligned}
R_{S1}={}&
a_0\,d_0\,g_0\,g_1\,d_1\,a_1\,e_1\,
e_0\,c_0\,c_1\,f_1\,f_0\,b_0\,b_1,\\[2mm]
B_{S1}^{(1)}={}&
b_0\,d_0\,d_1\,b_1\,f_1\,g_1\,e_1\,c_1,\\
B_{S1}^{(2)}={}&
a_1\,a_0\,e_0\,g_0\,f_0\,c_0.
\end{aligned}
\]
The blue endpoint pairing is
\[
\mathcal M_1=
\bigl\{\{b_0,c_1\},\{c_0,a_1\}\bigr\}.
\]

### Certificate S2: skew red endpoints, second blue pairing

Again, the red endpoints are \(a_0,b_1\):
\[
\begin{aligned}
R_{S2}={}&
a_0\,d_0\,d_1\,a_1\,e_1\,e_0\,c_0\,
c_1\,f_1\,g_1\,g_0\,f_0\,b_0\,b_1,\\[2mm]
B_{S2}^{(1)}={}&
b_0\,d_0\,g_0\,e_0\,a_0\,a_1,\\
B_{S2}^{(2)}={}&
c_0\,f_0\,f_1\,b_1\,d_1\,g_1\,e_1\,c_1.
\end{aligned}
\]
The blue endpoint pairing is
\[
\mathcal M_2=
\bigl\{\{b_0,a_1\},\{c_0,c_1\}\bigr\}.
\]

The availability of both skew pairings is the essential feature of the replacement.

## 4. Gluing the certificates into Hamilton cycles

Retain all edge colours outside the replacement. Colour each of the six attachment edges as its corresponding old edge incident with \(v_0\) or \(v_1\).

The outside red path and any certificate with the required red endpoints join through the two red attachment edges to form a Hamilton cycle of \(\Pi(G')\).

It remains to choose the certificate so that blue also forms one cycle.

### Aligned case

The two outside blue paths induce one of the cross-layer pairings
\[
\bigl\{\{b_0,b_1\},\{c_0,c_1\}\bigr\},
\qquad
\bigl\{\{b_0,c_1\},\{c_0,b_1\}\bigr\}.
\]
Certificate A induces the within-layer pairing
\[
\bigl\{\{b_0,c_0\},\{b_1,c_1\}\bigr\}.
\]
It therefore differs from either possible outside pairing.

Two distinct perfect matchings on a four-element terminal set have union a 4-cycle. Consequently, after reinstating the four blue attachment edges, the two outside blue paths and the two inside blue paths join into one cycle. Since they collectively cover every vertex, this is a Hamilton cycle.

### Skew case

The outside blue paths induce exactly one of \(\mathcal M_1,\mathcal M_2\), since each joins layer \(0\) to layer \(1\).

* If the outside pairing is \(\mathcal M_1\), use Certificate S2.
* If the outside pairing is \(\mathcal M_2\), use Certificate S1.

Again the inside and outside pairings are distinct, so all four blue paths join into one Hamilton cycle.

All edges are accounted for: outside edges retain their old colours, attachment edges retain their corresponding old colours, and each certificate partitions the 25 internal edges. This proves the Hamilton-decomposition assertion of the proposition. \(\square\)

## 5. Preservation of planarity and 3-connectivity

### Planarity

The graph \(T\) has an embedding with outer cycle
\[
a\,d\,b\,f\,c\,e\,a
\]
and with \(g\) inside, adjacent to \(d,e,f\). Its three attachment vertices lie on the outer face.

Insert this drawing into a small disk formerly occupied by \(v\), choosing its orientation or reflection to match the cyclic order of the three incident edges. Hence \(G'\) is planar whenever \(G\) is planar.

### 3-connectivity

View \(G'\) as joining
\[
G-v \quad\text{and}\quad Q_3-q
\]
by three edges with distinct endpoints on both sides. Here \(Q_3\) is the cube and \(q\) is its deleted vertex.

Let \(X\subseteq V(G')\) with \(|X|\le 2\).

* **All deleted vertices lie on one side.**  
  The other side remains connected. Every component of the affected side contains a surviving attachment vertex: otherwise restoring its deleted gluing vertex would still leave a disconnected graph after deleting at most two vertices from \(G\), or from \(Q_3\), contradicting 3-connectivity. Thus all components attach to the unaffected side.

* **One deleted vertex lies on each side.**  
  Both sides remain connected, by 3-connectivity of \(G\) and \(Q_3\): in each original graph we have deleted its gluing vertex and at most one other vertex. At most two of the three joining edges are lost, so a joining edge survives.

Thus \(G'-X\) is connected in every case, and \(G'\) is 3-connected.

## 6. An explicit infinite family satisfying the conjecture

The prism of \(K_4\) has a particularly simple Hamilton decomposition. Partition its base edges into the two Hamilton paths
\[
A=1\,2\,3\,4,
\qquad
D=3\,1\,4\,2.
\]
Take both layer copies of \(A\) and add the rungs at its endpoints \(1,4\). This forms a Hamilton cycle. Do the same for \(D\), using the rungs at \(3,2\).

The two path edge sets partition \(E(K_4)\), and their endpoint sets partition \(V(K_4)\). Therefore the resulting Hamilton cycles partition \(E(\Pi(K_4))\).

Applying the proposition repeatedly proves:

**Corollary.** Every graph obtained from \(K_4\) by finitely many cube insertions is cubic, planar and 3-connected, and its prism has a Hamilton decomposition. After \(t\) insertions its order is
\[
4+6t.
\]

This is an infinite **nonbipartite** family. Indeed, the three attachment vertices of \(T\) belong to the same bipartition class. Consequently cube insertion preserves bipartiteness in both directions: a 2-colouring after insertion would give a 2-colouring before insertion by assigning the deleted vertex the common colour of the three attachment vertices. Starting from \(K_4\), all resulting graphs remain nonbipartite.

The proof is constructive. Given the original Hamilton decomposition, trace the two outside blue paths, choose the appropriate certificate, and substitute it.

## 7. Scope and the remaining gap

The proposition also gives a precise reducibility statement:

> A vertex-minimal counterexample to the conjecture cannot be a cube insertion into a smaller simple 3-connected cubic planar graph.

Equivalently, a cube-minus-a-vertex patch is reducible whenever contracting that patch to one cubic vertex leaves a graph in the conjectured class.

This does **not** supply a reduction for an arbitrary 3-connected cubic planar graph. In particular, it does not handle general cyclically 4-edge-connected graphs, nor does it establish closure under arbitrary cubic 3-sums. The full conjecture is therefore not resolved here.

The local preservation theorem and its corollaries are proved above without reliance on literature claims; I have not checked whether this preservation theorem is already known.