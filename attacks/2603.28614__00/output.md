```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A constructive pivot Gray code exists for every graph whose blocks are generalized theta graphs, and pivot codes lift through proper odd subdivisions of any base graph already admitting one.",
  "would_publish": false,
  "caveats": "Arbitrary 2-connected graphs, including general subdivisions of K4, remain unresolved, and the literature novelty of these partial results was not checked."
}
```

# Mathematical writeup

## 1. Definitions and partial results

All graphs below are finite, connected, loopless, and simple unless explicitly stated otherwise. Let \(\mathcal F(G)\) denote the graph whose vertices are the spanning trees of \(G\), with \(T,T'\) adjacent when
\[
T'=T-e+f
\]
and the two exchanged edges \(e,f\) have a common endpoint. The problem asks whether \(\mathcal F(G)\) always has a Hamiltonian path.

I prove the following two partial results.

### Theorem A: generalized theta blocks

Let \(G\) be a connected graph such that every nontrivial block of \(G\) is the union of internally vertex-disjoint paths with the same two endpoints. Then \(G\) has a pivot Gray code.

In particular, this covers:

- every generalized theta graph;
- every \(K_{2,r}\);
- every connected graph of cyclomatic number at most \(2\).

The \(K_{2,r}\) cases are not outerplanar for \(r\ge 3\), so this goes beyond the outerplanar class quoted in the question.

### Theorem B: lifting through proper odd subdivisions

Let \(H\) have cyclomatic number at least \(2\) and admit a pivot Gray code. Replace every edge \(e\) of \(H\) by an internally vertex-disjoint path of odd length \(\ell_e\ge 3\). Then the resulting subdivision also admits a pivot Gray code.

As a self-contained consequence, every subdivision of \(K_4\) in which each of the six edges is replaced by an odd path of length at least \(3\) admits a pivot Gray code.

Neither theorem settles the general conjecture.

---

## 2. Basic structure of the pivot flip graph

Let
\[
\beta(G)=|E(G)|-|V(G)|+1
\]
be the cyclomatic number.

### Proposition 2.1

If \(G\) is simple, then \(\mathcal F(G)\) is \(2\beta(G)\)-regular.

#### Proof

Fix a spanning tree \(T\) and a non-tree edge \(xy\). Let
\[
x=v_0,v_1,\ldots,v_q=y
\]
be the \(x\)-\(y\) path in \(T\). Since \(G\) is simple and \(xy\notin T\), one has \(q\ge 2\).

After adding \(xy\), an edge can be removed while preserving a spanning tree precisely when it lies on this path. For the removed edge to share an endpoint with \(xy\), it must be either
\[
v_0v_1\qquad\text{or}\qquad v_{q-1}v_q.
\]
Thus every non-tree edge gives exactly two pivot neighbors. Different non-tree edges give different resulting trees. Since every spanning tree has exactly \(\beta(G)\) non-tree edges, the degree is \(2\beta(G)\). ∎

The same cycle argument also proves connectivity. Indeed, an unrestricted exchange \(T\mapsto T-f+e\) can be simulated by moving the unique omitted edge one step at a time around the fundamental cycle \(T+e\). Thus the difficulty is Hamiltonicity, not connectivity.

---

## 3. Hamilton paths in rectangular grids

For \(a\ge 1\), let \(P_a\) denote the path with vertex set \(\{1,\ldots,a\}\). A corner of
\[
Q=P_{a_1}\square\cdots\square P_{a_d}
\]
is a vertex all of whose coordinates belong to \(\{1,a_i\}\).

### Lemma 3.1

Every rectangular grid \(Q\) has a Hamiltonian path starting at any prescribed corner and ending at some corner.

#### Proof

Reflecting coordinates reduces to the all-ones corner. Induct on \(d\). For \(d=0\), the grid is a single vertex.

Suppose \(A\) has a Hamiltonian path
\[
x_1,x_2,\ldots,x_M
\]
between corners. In \(A\square P_b\), traverse layer \(1\) in the order \(x_1,\ldots,x_M\), layer \(2\) in reverse order, and continue alternately. Consecutive layers join at the same \(A\)-coordinate. This visits every vertex once and ends at a corner. ∎

We will also need endpoint control in odd grids.

### Lemma 3.2

Let
\[
Q=P_{a_1}\square\cdots\square P_{a_d},
\qquad d\ge 2,
\]
where every \(a_i\) is odd and at least \(3\). Given a starting corner \(x\), a coordinate \(q\), and either terminal side of the \(q\)-th factor, there is a Hamiltonian path beginning at \(x\) and ending at a corner on the prescribed side in coordinate \(q\).

#### Proof

Reflect coordinates so that \(x=(1,\ldots,1)\).

If the prescribed \(q\)-coordinate is \(a_q\), begin with the path \(1,2,\ldots,a_q\) in the \(q\)-th factor and repeatedly apply the alternating-layer construction from Lemma 3.1. Because every newly added factor has odd order, the endpoint retains \(q\)-coordinate \(a_q\).

Suppose instead that the prescribed \(q\)-coordinate is \(1\). Choose \(r\ne q\). In the two-dimensional grid \(P_{a_q}\square P_{a_r}\), there is a Hamiltonian path from \((1,1)\) to \((1,a_r)\): first traverse the first column from top to bottom, and then traverse the remaining columns row by row, beginning with the bottom row and alternating direction. Since \(a_q\) is odd, this ends at \((1,a_r)\). Add the remaining odd factors by alternating layers. The \(q\)-coordinate of the endpoint remains \(1\). ∎

---

## 4. Generalized theta graphs

Let \(P_1,\ldots,P_r\) be internally vertex-disjoint \(s\)-\(t\) paths, with
\[
P_i=e_{i,1},e_{i,2},\ldots,e_{i,\ell_i}
\]
ordered from \(s\) to \(t\). Let
\[
\Theta(P_1,\ldots,P_r)=P_1\cup\cdots\cup P_r.
\]

### Lemma 4.1: description of its spanning trees

Every spanning tree of \(\Theta(P_1,\ldots,P_r)\) contains exactly one of the paths \(P_i\) in full and omits exactly one edge from each other path.

#### Proof

There are
\[
\sum_i\ell_i
\]
edges and
\[
2+\sum_i(\ell_i-1)=\sum_i\ell_i-r+2
\]
vertices. Hence a spanning tree omits exactly \(r-1\) edges.

A connected spanning subgraph cannot omit two edges of the same \(P_i\), because the internal segment between two omitted edges would be disconnected from both \(s\) and \(t\). Thus the \(r-1\) omitted edges lie on distinct paths. Exactly one path is intact. Conversely, every such choice is plainly connected and has the correct number of edges. ∎

For each \(i\), let \(\mathcal C_i\) be the set of spanning trees in which \(P_i\) is intact. A member of \(\mathcal C_i\) is specified by the omitted-edge positions
\[
(k_j)_{j\ne i},\qquad 1\le k_j\le \ell_j.
\]
Thus \(\mathcal C_i\) contains a spanning rectangular grid
\[
Q_i=\mathop{\square}_{j\ne i}P_{\ell_j}.
\]
Indeed, changing \(k_j\) from \(a\) to \(a+1\) exchanges the consecutive path edges \(e_{j,a}\) and \(e_{j,a+1}\), which share a vertex.

### Theorem 4.2

Every generalized theta graph has a pivot Gray code.

#### Proof

Order the chambers as
\[
\mathcal C_1,\mathcal C_2,\ldots,\mathcal C_r.
\]

Choose an arbitrary corner of \(Q_1\). By Lemma 3.1, list all of \(\mathcal C_1\) along a Hamiltonian path ending at another corner. At this endpoint, the omitted edge of \(P_2\) is terminal, hence incident with either \(s\) or \(t\); call that terminal \(x\).

Move to the tree in \(\mathcal C_2\) obtained by:

- restoring that terminal edge of \(P_2\);
- deleting from \(P_1\) its edge incident with \(x\);
- retaining all other omitted edges.

The two exchanged edges share \(x\), so this is a pivot. The resulting tree is a corner of \(Q_2\).

Repeat. At the endpoint of the Hamiltonian path through \(\mathcal C_i\), restore the omitted terminal edge of \(P_{i+1}\) and omit the corresponding terminal edge of \(P_i\). This gives a pivot to a corner of \(\mathcal C_{i+1}\).

The chambers are disjoint and exhaust all spanning trees by Lemma 4.1, so their concatenation is a pivot Gray code. ∎

### Corollary 4.3

Every \(K_{2,r}\) has a pivot Gray code.

This is Theorem 4.2 with all \(r\) paths of length \(2\).

---

## 5. Passing to blocks

If \(G\) is a one-vertex union of connected graphs \(G_1,\ldots,G_m\), then a spanning tree of \(G\) is exactly the union of independently chosen spanning trees of the \(G_i\).

Moreover, a pivot exchange cannot involve edges from two different blocks. If \(f\) is added to a tree, its fundamental cycle lies entirely in the block containing \(f\), and the removed edge must lie on this cycle. Consequently,
\[
\mathcal F(G)\cong
\mathcal F(G_1)\square\cdots\square\mathcal F(G_m).
\]

A Cartesian product of graphs with Hamiltonian paths again has a Hamiltonian path: traverse consecutive copies of one factor alternately forward and backward.

This proves Theorem A.

### Corollary 5.1

Every connected simple graph \(G\) with \(\beta(G)\le 2\) has a pivot Gray code.

#### Justification

The cyclomatic number is additive over blocks. A 2-connected block of cyclomatic number \(1\) is a cycle.

If a 2-connected block \(B\) has cyclomatic number \(2\), then
\[
\sum_{v\in V(B)}(\deg(v)-2)
  =2|E(B)|-2|V(B)|=2.
\]
Since \(B\) has minimum degree at least \(2\), it has exactly two degree-\(3\) vertices and all other vertices have degree \(2\). Suppressing degree-\(2\) vertices therefore exhibits \(B\) as three internally disjoint paths between the two degree-\(3\) vertices. Thus \(B\) is a theta graph, and Theorem A applies. ∎

---

## 6. Lifting a code through a proper odd subdivision

Let \(H\) be connected, and replace every edge \(e=uv\) with an internally vertex-disjoint \(u\)-\(v\) path \(P_e\) of length \(\ell_e\). Write \(H^\ell\) for the resulting subdivision.

### Lemma 6.1: chamber decomposition for subdivisions

A spanning tree of \(H^\ell\) is uniquely specified by:

1. a spanning tree \(S\) of \(H\);
2. for every edge \(e\notin S\), one omitted edge of \(P_e\).

All edges of \(P_e\) are present when \(e\in S\).

#### Proof

A connected spanning subgraph cannot omit two edges of a path \(P_e\), since an internal segment would then be isolated. Let \(S\) consist of those base edges whose paths are intact.

The branch vertices can be connected in the subdivided tree only through intact paths, so \(S\) is connected. It is acyclic because a cycle in \(S\) would lift to a cycle in the subdivided graph. Hence \(S\) is a spanning tree of \(H\).

Conversely, an intact copy of a spanning tree \(S\), together with all but one edge of every \(P_e\) for \(e\notin S\), is connected and has the correct number of edges. ∎

For fixed \(S\), the corresponding chamber is therefore the grid
\[
Q_S=\mathop{\square}_{e\notin S}P_{\ell_e}.
\]
Its dimension is \(\beta(H)\).

### Theorem 6.2

Suppose \(\beta(H)\ge 2\), \(H\) has a pivot Gray code, and every \(\ell_e\) is odd and at least \(3\). Then \(H^\ell\) has a pivot Gray code.

#### Proof

Let
\[
S_1,S_2,\ldots,S_N
\]
be a pivot Gray code for \(H\). Write
\[
S_{i+1}=S_i-f_i+e_i,
\]
where \(e_i\notin S_i\), \(f_i\in S_i\), and \(e_i,f_i\) share a base vertex \(v_i\).

Start at an arbitrary corner of the chamber \(Q_{S_1}\). By Lemma 3.2, traverse all of this chamber along a Hamiltonian path whose endpoint is a corner at which the omitted edge of \(P_{e_1}\) is the terminal edge incident with \(v_1\).

The next tree is obtained by:

- restoring this terminal edge of \(P_{e_1}\);
- deleting from \(P_{f_1}\) its terminal edge incident with \(v_1\);
- preserving every other omitted edge.

These two subdivided edges share \(v_1\). The resulting tree is a corner of \(Q_{S_2}\).

Inductively, upon entering \(Q_{S_i}\) at a corner, use Lemma 3.2 to traverse the entire chamber and finish with the omitted edge of \(P_{e_i}\) incident with \(v_i\). Then pivot to a corner of \(Q_{S_{i+1}}\). In the final chamber use Lemma 3.1 with no endpoint constraint.

By Lemma 6.1, the chambers are disjoint and exhaust all spanning trees of \(H^\ell\). Hence the concatenated order is a pivot Gray code. ∎

The oddness and lower bound \(\ell_e\ge 3\) are used only in Lemma 3.2. I do not claim that they are necessary.

---

## 7. A self-contained \(K_4\) application

Label the vertices of \(K_4\) by \(1,2,3,4\), writing \(ij\) for edge \(\{i,j\}\). The following is a pivot Gray code for its sixteen spanning trees; an arrow label \(a\to b\) means that \(a\) is removed and \(b\) added:
\[
\begin{aligned}
&\{12,13,14\}
 \xrightarrow{14\to24}
 \{12,13,24\}
 \xrightarrow{13\to23}
 \{12,23,24\}\\
&\xrightarrow{24\to14}
 \{12,14,23\}
 \xrightarrow{14\to34}
 \{12,23,34\}
 \xrightarrow{12\to13}
 \{13,23,34\}\\
&\xrightarrow{23\to12}
 \{12,13,34\}
 \xrightarrow{13\to14}
 \{12,14,34\}
 \xrightarrow{12\to24}
 \{14,24,34\}\\
&\xrightarrow{14\to12}
 \{12,24,34\}
 \xrightarrow{12\to13}
 \{13,24,34\}
 \xrightarrow{34\to23}
 \{13,23,24\}\\
&\xrightarrow{13\to14}
 \{14,23,24\}
 \xrightarrow{23\to13}
 \{13,14,24\}
 \xrightarrow{24\to23}
 \{13,14,23\}\\
&\xrightarrow{13\to34}
 \{14,23,34\}.
\end{aligned}
\]
Every displayed exchange uses incident edges. The list contains the four stars and all \(4!/2=12\) labeled paths, hence all spanning trees of \(K_4\).

Combining this list with Theorem 6.2 gives:

### Corollary 7.1

If every edge of \(K_4\) is replaced by an odd path of length at least \(3\), the resulting graph has a pivot Gray code.

Taking the complete-graph result quoted in the question as given, the same lifting argument applies to proper odd subdivisions of every \(K_n\).

---

## 8. Remaining gap

The argument does not cover:

- arbitrary 2-connected graphs;
- arbitrary series-parallel graphs;
- subdivisions with unrestricted path parities;
- even arbitrary subdivisions of \(K_4\).

The parity restriction in Theorem 6.2 arises from controlling the endpoint of a Hamiltonian path inside each chamber grid. Removing it would require a more flexible chamber traversal or an interleaving of chambers rather than visiting each chamber contiguously.

Thus no proof or counterexample to the full conjecture is obtained. I also have not independently checked whether the generalized-theta or odd-subdivision lifting results already occur in the literature.