```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured implication holds, without the excluded-subcontraction hypothesis, for graphs with at most four odd-degree vertices.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; novelty of this special case has not been checked."
}
```

## Partial result

I prove the following special case independently of the forbidden-subcontraction condition.

**Theorem.** Every universally cell \(3\)-colorable finite multigraph with at most four odd-degree vertices admits a nowhere-zero \(3\)-flow.

Consequently, any counterexample to Conjecture 11 must have a connected component containing at least six odd-degree vertices.

The argument uses prescribed orientations, three small cuts, and a planar quotient resembling a tetrahedron with vertices inserted in its faces. I do not assert that this special case is new relative to the full source paper or subsequent literature.

## 1. Orientation and drawing preliminaries

For an orientation \(D\), write
\[
b_D(v)=d_D^+(v)-d_D^-(v).
\]
A **modulo-\(3\) orientation** is one satisfying
\[
b_D(v)\equiv 0\pmod 3
\qquad\text{for every }v.
\]

Existence of such an orientation is equivalent to existence of a nowhere-zero \(3\)-flow. Indeed, reduction modulo \(3\), followed by reversing edges whose value is \(-1\), proves one direction. For completeness, the converse follows from integral circulation: if \(D\) is a modulo-\(3\) orientation, the fractional vector \(x_e=1/3\) satisfies
\[
\operatorname{div}x(v)=b_D(v)/3,\qquad 0\le x_e\le1.
\]
These integral-demand, integral-capacity constraints have an integral solution \(x_e\in\{0,1\}\). Then \(f(e)=1-3x_e\in\{1,-2\}\) is an integer circulation.

We will use two further elementary facts.

### Prescribed-orientation criterion

Given integers \(b(v)\), there is an orientation with imbalance \(b(v)\) at every vertex if and only if
\[
\sum_v b(v)=0,\qquad b(v)\equiv d(v)\pmod2,
\]
and
\[
|b(X)|\le |\delta(X)|\qquad\text{for every }X\subseteq V,
\tag{1}
\]
where \(b(X)=\sum_{v\in X}b(v)\).

For sufficiency, prescribe outdegrees
\[
r(v)=\frac{d(v)+b(v)}2.
\]
Assigning every edge to its tail is a bipartite matching problem with vertex capacities \(r(v)\). Its feasibility conditions are
\[
\sum_{v\in X}r(v)\ge |E(X)|
\]
for all \(X\), together with \(\sum_vr(v)=|E|\). These follow from (1).

In particular:

**Lemma 1.** Every bridgeless graph with at most two odd-degree vertices is \(3\)-flowable.

**Proof.** If there are no odd-degree vertices, use an Eulerian orientation. Otherwise, assign imbalance \(+3\) to one odd vertex, \(-3\) to the other, and zero elsewhere. A cut separating the two odd vertices has odd size and, by bridgelessness, has size at least three. Thus (1) holds. ∎

### Plane duality and quotient closure

For a drawing \(\Gamma\), let \(P(\Gamma)\) denote its planarization. Elementary plane flow–color duality gives
\[
\Gamma\text{ has a cell }3\text{-coloring}
\quad\Longleftrightarrow\quad
P(\Gamma)\text{ has a modulo-}3\text{ orientation}.
\tag{2}
\]
For example, in the forward direction, regard colors as elements of \(\mathbb Z_3\) and use their differences across edges as flow values. Conservation follows by telescoping around each vertex. Conversely, a plane \(\mathbb Z_3\)-flow gives well-defined face-color differences.

Two consequences are important.

* A universally cell \(3\)-colorable graph is bridgeless: a bridge can be drawn without crossings between drawings of its two sides, and remains a bridge of the planarization.
* Universal cell \(3\)-colorability is preserved by identifying the vertices in each part of an arbitrary vertex partition and discarding the resulting loops.

Here is a justification of the second assertion, including when parts are disconnected. Given a drawing of the quotient, replace each quotient vertex by a small disk. Inside it, draw the corresponding original vertices and internal edges, routing incident edges to their prescribed boundary points. Allow crossings inside the disks. A modulo-\(3\) orientation of this drawing’s planarization induces one on the quotient drawing’s planarization by summing conservation over each disk. Equation (2) finishes the argument.

This also permits deletion of loops. Loops do not affect degree parity or \(3\)-flowability, so henceforth graphs are loopless.

## 2. Two flow-extension reductions

The following reductions will be applied to a smallest counterexample.

### Even patches with at most four boundary edges

**Lemma 2.** Let \(S\) induce a connected subgraph, suppose all vertices of \(S\) have even degree in \(G\), and suppose
\[
|\delta_G(S)|\le4.
\]
Every modulo-\(3\) orientation of \(G/S\) extends to one of \(G\).

**Proof.** The contracted vertex has even degree at most four, so its imbalance must be zero. Thus its boundary edges have equally many directions in and out, at most two each.

Let \(F=G[S]\). At each \(v\in S\), prescribe the internal imbalance needed to balance its already oriented boundary edges. Call this prescription \(q(v)\). Then
\[
q(S)=0,\qquad q(v)\equiv d_F(v)\pmod2.
\]
For every \(U\subseteq S\),
\[
|q(U)|\le2,
\qquad
|\delta_F(U)|\equiv q(U)\pmod2.
\]
If \(U\) is nonempty and proper, connectedness of \(F\) gives \(|\delta_F(U)|>0\). The parity condition therefore implies
\[
|\delta_F(U)|\ge |q(U)|.
\]
The prescribed-orientation criterion supplies an orientation balancing every vertex of \(S\). ∎

### One odd vertex behind a three-edge cut

**Lemma 3.** Suppose \(G\) is bridgeless, \(S\) contains exactly one odd-degree vertex, and
\[
|\delta_G(S)|=3.
\]
If \(G/S\) is \(3\)-flowable, then so is \(G\).

**Proof.** Contract the complement of \(S\) to one vertex. The resulting graph is bridgeless and has exactly two odd-degree vertices, so Lemma 1 applies.

In any modulo-\(3\) orientation, the three edges at a cubic vertex are all directed in or all directed out. Reverse one of the two quotient orientations if necessary, and glue their orientations across the three-edge cut. ∎

## 3. A smallest counterexample

Suppose the theorem is false. Choose a universally cell \(3\)-colorable, non-\(3\)-flowable graph \(G\) with at most four odd-degree vertices, minimizing its number of vertices.

We may assume \(G\) is connected. It is bridgeless, and Lemma 1 shows that it has exactly four odd-degree vertices.

Also,
\[
\delta(G)\ge3.
\tag{3}
\]
Indeed, a degree-two vertex can be suppressed by contracting one incident edge. Universal cell \(3\)-colorability is preserved, and the number of odd-degree vertices does not increase. A modulo-\(3\) orientation of the smaller graph lifts through the suppressed path. If both edges have the same other endpoint, restore them as a directed two-edge cycle.

Minimality and Lemmas 2–3 now give:

* If a connected vertex set \(S\) consists entirely of even-degree vertices and \(|\delta(S)|\le4\), then \(|S|=1\).
* If a connected vertex set \(S\) contains exactly one odd-degree vertex and \(|\delta(S)|=3\), then \(|S|=1\).

In particular, every nonempty connected set consisting entirely of even-degree vertices satisfies
\[
|\delta(S)|\ge4.
\tag{4}
\]
For a singleton this follows from (3) and parity; for a larger set, a smaller cut would contradict the first reduction.

## 4. Three cuts produce a planar quotient

Name the odd-degree vertices \(a_1,a_2,a_3,a_4\).

For each of the three bipartitions of these vertices into two pairs, prescribe imbalance \(+3\) on one pair, \(-3\) on the other, and zero elsewhere. Such an orientation would be a modulo-\(3\) orientation, so none exists.

By the prescribed-orientation criterion, each prescription has a violating cut. A cut with prescribed imbalance of absolute value three has odd size, hence size at least three. Therefore a violating cut must separate the two positive vertices from the two negative vertices and have size at most four.

Consequently there are sets \(X_1,X_2,X_3\) satisfying
\[
\begin{aligned}
X_1\cap\{a_1,a_2,a_3,a_4\}&=\{a_1,a_2\},\\
X_2\cap\{a_1,a_2,a_3,a_4\}&=\{a_1,a_3\},\\
X_3\cap\{a_1,a_2,a_3,a_4\}&=\{a_1,a_4\},
\end{aligned}
\qquad
|\delta(X_i)|\le4.
\tag{5}
\]

Partition \(V(G)\) according to its three membership bits in these sets, and identify each nonempty part to one vertex. Call the resulting loopless multigraph \(Q\).

The four parts containing the odd-degree vertices have labels
\[
111,\quad100,\quad010,\quad001.
\]
Call their quotient vertices \(t_1,t_2,t_3,t_4\). All other parts have even-parity labels.

For an edge of \(Q\), give it weight equal to the Hamming distance between its endpoint labels. Then
\[
W:=\sum_{e\in E(Q)}w(e)
=\sum_{i=1}^3|\delta_G(X_i)|
\le12.
\tag{6}
\]
Each part corresponding to \(t_i\) contains exactly one odd-degree vertex. Its boundary is therefore odd, and bridgelessness gives
\[
D:=\sum_{i=1}^4d_Q(t_i)\ge12.
\tag{7}
\]

An edge between two odd-parity labels contributes two to both \(W\) and \(D\). An edge between two even-parity labels contributes two to \(W\) and zero to \(D\). An edge between labels of opposite parity contributes one to \(D\), and either one or three to \(W\). Hence
\[
W-D
=
2\,|E_Q(\text{even labels})|
+
2\,|\{e:\text{opposite-parity endpoints at distance }3\}|.
\tag{8}
\]
Equations (6)–(8) force equality everywhere. Thus:

1. \(d_Q(t_i)=3\) for all \(i\);
2. all three cuts in (5) have size four;
3. no edge joins two even-label parts;
4. an even-label part is adjacent only to odd-label parts at Hamming distance one.

Each odd-label part is connected. Otherwise, its component containing the unique odd-degree vertex would have boundary at least three, and another component would have positive boundary, contradicting the total boundary size three. By the second minimality reduction, each such part is a singleton. Thus the four odd-degree vertices of \(G\) themselves have degree three.

Index the possible even-label vertices as \(e_1,e_2,e_3,e_4\), where the label of \(e_i\) is the bitwise complement of that of \(t_i\). Property 4 says
\[
N_Q(e_i)\subseteq\{t_j:j\ne i\}.
\tag{9}
\]
Absent even-label parts are simply omitted.

This makes \(Q\) planar: embed a \(K_4\) on \(t_1,t_2,t_3,t_4\), and put \(e_i\), when present, in the face opposite \(t_i\). Parallel edges cause no difficulty.

Moreover, every component of an even-label part has boundary at least four by (4). Thus every present \(e_i\) has degree at least four. Since there are no edges between even-label vertices,
\[
\sum_i d_Q(e_i)\le\sum_i d_Q(t_i)=12.
\tag{10}
\]
At most three of the \(e_i\) are present.

Finally, for each pair \(\{i,j\}\), with complementary pair \(\{k,l\}\), define
\[
U_{ij}=\{t_i,t_j,e_k,e_l\},
\]
omitting absent vertices. The three cuts in (5), together with their complements, give
\[
|\delta_Q(U_{ij})|=4
\qquad\text{for every pair }\{i,j\}.
\tag{11}
\]

## 5. The modulo-\(3\) orientations of \(Q\)

Quotient closure makes \(Q\) universally cell \(3\)-colorable. Since \(Q\) is planar, it has a modulo-\(3\) orientation.

Write
\[
b(t_i)=3s_i,\qquad s_i\in\{-1,1\},
\]
and
\[
b(e_i)=3k_i,
\]
taking \(k_i=0\) when \(e_i\) is absent.

Every four-edge cut in a modulo-\(3\) orientation is balanced: its imbalance is both even and divisible by three, and has absolute value at most four. Therefore (11) gives
\[
s_i+s_j+k_k+k_l=0
\tag{12}
\]
for every pair \(\{i,j\}\).

Put \(K=\sum_i k_i\). Equation (12) becomes
\[
(s_i-k_i)+(s_j-k_j)=-K.
\]
Hence
\[
s_i-k_i=r\quad\text{for all }i,
\qquad K=-2r.
\tag{13}
\]

At least one \(e_i\) is absent, so \(r=\pm1\). Reverse the orientation to arrange \(r=1\). Then
\[
k_i=s_i-1\in\{0,-2\},
\qquad \sum_i k_i=-2.
\]
Exactly one \(k_i\) equals \(-2\). Relabeling, we obtain
\[
\begin{array}{c|cccc}
 &t_1&t_2&t_3&t_4\\ \hline
b&-3&3&3&3
\end{array},
\qquad
b(e_1)=-6,\quad b(e_i)=0\ (i\ne1).
\tag{14}
\]

Thus \(t_1\) is a sink and the other three \(t_i\) are sources. By (9), all edges at \(e_1\) point into it, so
\[
d_Q(e_1)=6.
\tag{15}
\]

In fact, there are exactly two edges from \(e_1\) to each of \(t_2,t_3,t_4\). To see this, fix \(i\ne1\) and consider the four-edge cut of \(U_{1i}\). Its only outgoing edges are those from \(t_i\) to \(e_1\):

* \(t_1\) is a sink;
* no edge joins two of the three source vertices;
* the other even vertices in \(U_{1i}\) can send edges only to \(t_1\), which is inside \(U_{1i}\).

The cut is balanced, so it has two outgoing edges. Therefore
\[
|E_Q(e_1,t_i)|=2
\qquad(i=2,3,4).
\tag{16}
\]

Each of \(t_2,t_3,t_4\) consequently has just one incident edge outside \(e_1\). For any other even vertex \(e_j\), all incoming edges come from at most two of those source vertices, and all outgoing edges go to \(t_1\). Since \(e_j\) is balanced,
\[
d_Q(e_j)\le4.
\]
Its corresponding part is connected by (4), and the first minimality reduction says that this part is a singleton.

Let \(S\) be the part represented by \(e_1\). Since its boundary has size six and each of its components has boundary at least four, \(G[S]\) is connected.

We have proved that **the only possibly nonsingleton part of the quotient is \(S\)**, where
\[
|\delta_G(S)|=6
\quad\text{and every vertex of }S\text{ has even degree}.
\tag{17}
\]

## 6. A high-degree vertex inside \(S\) would give a flow

Suppose some \(v\in S\) has degree at least six.

Form \(H\) by contracting \(V(G)\setminus S\) to one vertex \(z\). Then \(d_H(z)=6\), and every vertex of \(H\) has even degree.

There are six edge-disjoint \(z\)-\(v\) paths in \(H\). Indeed, otherwise an edge cut separating them has size at most five. Every cut of the Eulerian graph \(H\) has even size, so there is a set \(A\subseteq S\), containing \(v\), with
\[
|\delta_H(A)|\le4.
\]
Take the component \(C\) of \(H[A]\) containing \(v\). It is a connected all-even vertex set in \(G\), and
\[
|\delta_G(C)|=|\delta_H(C)|\le4.
\]
The first minimality reduction makes \(C\) a singleton, contradicting \(d_G(v)\ge6\).

Orient six edge-disjoint \(z\)-\(v\) paths from \(z\) to \(v\). Their union has even degree at every vertex, so the remaining edges of \(H\) also form an even graph and can be oriented Eulerianly. This gives
\[
b_H(z)=6,\qquad b_H(v)=-6,
\]
with imbalance zero elsewhere.

All six edges at \(z\) point toward \(S\). This agrees with the orientation of \(Q\) in (14)–(16), where all six edges at \(e_1\) point inward. Replacing \(e_1\) by this oriented copy of \(H-z\) gives a modulo-\(3\) orientation of \(G\), a contradiction.

Therefore every vertex of \(S\) has degree four. All other even-degree vertices were already singleton parts of degree four. We have reached
\[
d_G(t_i)=3\quad(i=1,2,3,4),
\qquad d_G(v)=4\quad\text{for all other }v.
\tag{18}
\]

## 7. A drawing that cannot be cell \(3\)-colored

Take a plane embedding of \(Q\). Replace \(e_1\) by a small disk and draw \(G[S]\) and its incident edge portions inside the disk, allowing crossings there. Keep the remainder of the embedding unchanged. This produces a drawing \(\Gamma\) of \(G\) with all crossings inside that disk.

Suppose \(\Gamma\) had a cell \(3\)-coloring. Its planarization would have a modulo-\(3\) orientation.

Every vertex of the planarization other than the four \(t_i\) has degree four: this includes both original even-degree vertices and crossing vertices. Such a vertex necessarily has integer imbalance zero.

Collapsing the disk therefore gives an orientation of \(Q\) in which
\[
b(e_i)=0
\qquad\text{for every present even-label vertex}.
\tag{19}
\]
The four cubic vertices have imbalances \(\pm3\). Since total imbalance is zero, exactly two are sources and two are sinks.

Choose the pair of source vertices \(t_i,t_j\). The corresponding set \(U_{ij}\) has imbalance six by (19), but its boundary has size four by (11). This is impossible:
\[
6=|b(U_{ij})|>|\delta_Q(U_{ij})|=4.
\]

Thus \(\Gamma\) has no cell \(3\)-coloring, contradicting the universal cell \(3\)-colorability of \(G\). The theorem follows. ∎

## What remains open

The proof establishes the desired implication whenever there are at most four odd-degree vertices, with no forbidden-subcontraction assumption.

It does **not** address universally cell \(3\)-colorable non-\(3\)-flowable graphs having six or more odd-degree vertices. In particular, it does not show that such a graph must contain one of the specified \(K^+_{3,n-3}\) subcontractions, and it does not resolve Tutte’s \(3\)-Flow Conjecture.

The precise additional restriction obtained is:

\[
\boxed{\text{Any counterexample to Conjecture 11 has a component with at least six odd-degree vertices.}}
\]