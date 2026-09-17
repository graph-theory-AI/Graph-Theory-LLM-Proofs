```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Positivity holds for every bridgeless graph of cycle rank at most 8 and for every projective-planar graph, but the general conjecture is not settled here.",
  "would_publish": false,
  "caveats": "These are restricted-class results; no claim of novelty or exhaustive computational verification is made."
}
```

# Partial results on positivity at \(11/2\)

I do not obtain a proof or a counterexample in full generality. The following partial results have self-contained proofs.

Write
\[
r(G)=|E(G)|-|V(G)|+c(G)
\]
for the cycle rank. Allowing loops and parallel edges is useful for the reductions below.

## Theorem

For every real \(q>5\):

1. If \(G\) is bridgeless and \(r(G)\le 8\), then
   \[
   \Phi(G,q)>0.
   \]
2. If \(G\) is bridgeless and embeddable in the projective plane, then
   \[
   \Phi(G,q)>0.
   \]

Moreover, if positivity fails at a fixed real \(q>5\), a counterexample of minimum cycle rank can be chosen to be a connected cubic simple graph of girth at least \(6\), with at least \(16\) vertices.

Thus both asserted special cases include \(q=11/2\). The proof uses positive reductions on cycles of length at most five, followed by an exact treatment of the fourteen-vertex endpoint.

---

## 1. Nonvanishing at \(11/2\) is automatic

The inclusion–exclusion formula is
\[
\Phi(G,q)=
\sum_{A\subseteq E(G)}
(-1)^{|E(G)|-|A|}
q^{\,|A|-|V(G)|+c(V(G),A)}.
\tag{1}
\]

For a bridgeless graph, this is a monic integer polynomial of degree \(r(G)\). Indeed, deleting any edge first decreases the cycle rank, so only \(A=E(G)\) contributes to the leading term.

Consequently,
\[
2^{r(G)}\Phi(G,11/2)
\]
is an odd integer: the leading term contributes \(11^{r(G)}\), and every lower-degree term contributes an even integer. In particular,
\[
\Phi(G,11/2)\ne 0
\]
for every bridgeless graph.

The conjecture is therefore purely a **sign problem**. A counterexample would have a strictly negative value, not a zero.

---

## 2. Reduction to cubic graphs

We use the following elementary identities:

- A graph with a bridge has flow polynomial zero.
- Removing a loop contributes a factor \(q-1\).
- Suppressing a degree-two vertex preserves the flow polynomial.
- Flow polynomials multiply over connected components.
- For a nonloop edge \(e\),
  \[
  \Phi(H,q)=\Phi(H/e,q)-\Phi(H-e,q).
  \tag{2}
  \]

Suppose a vertex \(v\) has degree \(d\ge4\). Partition its incident half-edges into sets of sizes \(2\) and \(d-2\). Split \(v\) into two vertices carrying these sets, and join the new vertices by a new edge \(e\). Call the resulting graph \(H\). Then \(H/e=G\), so
\[
\Phi(G,q)=\Phi(H,q)+\Phi(H-e,q).
\tag{3}
\]

Both resulting graphs have cycle rank at most \(r(G)\). Furthermore, if \(G\) is connected and bridgeless, at least one of \(H\) and \(H-e\) is bridgeless:

- Any bridge of \(H\) other than \(e\) would remain a bridge after contracting \(e\), contradicting bridgelessness of \(G\).
- If \(e\) is a bridge, deleting it leaves bridgeless components.

The splitting process terminates. For example, use the excess
\[
\mu(G)=\sum_{v\in V(G)}\max\{\deg(v)-3,0\}.
\]
Both terms on the right of (3) have smaller excess at the split vertex. Loop removal and degree-two suppression handle the remaining noncubic vertices.

Since \(q-1>0\) when \(q>1\), we obtain:

### Cubic reduction lemma

Fix \(q>1\). If a bridgeless graph fails to have positive flow-polynomial value at \(q\), then some connected bridgeless cubic multigraph of no greater cycle rank also fails.

This reduction also works within graphs embedded in a fixed surface: choose the two half-edges consecutively in the rotation at \(v\), and perform the split inside a small disc.

---

## 3. Positive short-cycle identities

Let \(G\) be cubic, and let
\[
C=v_1v_2\cdots v_\ell v_1
\]
be a cycle of length \(2\le\ell\le5\).

Form \(H\) by deleting the edges of \(C\) and identifying all its vertices to one vertex \(w\). The \(\ell\) remaining incident half-edges are labelled \(1,\ldots,\ell\).

For a partition of these labels into two sets, let \(H_{S\mid\bar S}\) denote the graph obtained by splitting \(w\) into two vertices, with no edge inserted between them, distributing the half-edges according to that partition.

The identities are
\[
\Phi(G,q)=(q-2)\Phi(H,q),\qquad \ell=2,
\tag{4}
\]
\[
\Phi(G,q)=(q-3)\Phi(H,q),\qquad \ell=3,
\tag{5}
\]
\[
\Phi(G,q)
=(q-4)\Phi(H,q)
+\Phi(H_{12\mid34},q)
+\Phi(H_{23\mid41},q),
\qquad \ell=4,
\tag{6}
\]
and
\[
\Phi(G,q)
=(q-5)\Phi(H,q)
+\sum_{i=1}^{5}
 \Phi\!\left(H_{\{i,i+1\}\mid\overline{\{i,i+1\}}},q\right),
\qquad \ell=5,
\tag{7}
\]
where indices in (7) are taken modulo \(5\).

### Proof of the identities

First take \(q\) to be a positive integer and count flows in an abelian group of order \(q\).

Let \(a_i\ne0\) be the flow on the remaining half-edge at \(v_i\), directed away from the cycle. Necessarily
\[
a_1+\cdots+a_\ell=0.
\]
Set
\[
s_0=0,\qquad s_j=a_1+\cdots+a_j.
\]
Once the flow on one cycle edge is selected, all cycle-edge flows are determined. The number of choices making them all nonzero is
\[
q-\bigl|\{s_0,s_1,\ldots,s_{\ell-1}\}\bigr|.
\tag{8}
\]

Cyclically adjacent \(s_i\)'s are distinct because every \(a_i\) is nonzero.

- For \(\ell=2,3\), all the \(s_i\)'s are distinct.
- For \(\ell=4\), the only possible equalities are the two nonadjacent pairs. They correspond to \(a_1+a_2=0\) and \(a_2+a_3=0\).
- For \(\ell=5\), every equality class has size at most two: three positions in a \(5\)-cycle cannot be pairwise nonadjacent. Thus
  \[
  \bigl|\{s_0,\ldots,s_4\}\bigr|
  =5-\sum_{i=1}^5\mathbf 1_{\{a_i+a_{i+1}=0\}}.
  \]
  Each indicator imposes precisely the additional conservation condition defining the corresponding split graph in (7).

Summing (8) over the flows off the cycle gives (4)–(7). Since they hold for infinitely many integers, they are polynomial identities.

### Rank and bridgelessness

The graph \(H\) is bridgeless whenever \(G\) is bridgeless. It can be obtained by contracting a spanning path of \(C\), then deleting the remaining cycle edge, which has become a loop.

Also,
\[
r(H)=r(G)-1.
\tag{9}
\]
Splitting \(w\) without adding an edge increases the vertex count by one and the component count by at most one. Hence every split graph in (6) or (7) has cycle rank at most \(r(G)-1\).

Finally, all graphs appearing in these identities are minors of \(G\). For the split graphs, delete the two cycle edges separating the two consecutive blocks and contract the paths within the blocks.

### Consequence

Fix \(q>5\), and take a minimum-cycle-rank counterexample. By the cubic reduction lemma it can be chosen cubic.

If it had a cycle of length at most five, (4)–(7) would express its value as a sum of nonnegative terms, with the term
\[
(q-\ell)\Phi(H,q)
\]
strictly positive by minimality. This is impossible.

Therefore a minimum-rank cubic counterexample has girth at least six.

---

## 4. The order bound and the fourteen-vertex endpoint

A cubic graph of girth at least six has at least fourteen vertices. Indeed, growing a tree to depth two from both ends of an edge gives
\[
2(1+2+4)=14
\]
distinct vertices; an identification would create a cycle of length at most five.

For a connected cubic graph,
\[
r(G)=\frac{|V(G)|}{2}+1.
\tag{10}
\]
Thus the short-cycle argument alone proves positivity for \(r(G)\le7\).

To reach cycle rank eight, it remains to treat cubic graphs of girth at least six on fourteen vertices.

### Uniqueness of this endpoint

Let \(v\) be a vertex of such a graph. Its distance-zero, distance-one and distance-two layers have sizes
\[
1,\quad 3,\quad 6.
\]
The six distance-two vertices are independent; an edge between two of them would create a cycle of length at most five.

Their twelve remaining edge incidences must meet the four remaining vertices. These four vertices have exactly twelve incidences available. It follows that the graph is bipartite, with parts of size seven.

The seven neighbourhoods on either side are triples on the opposite side. No pair occurs in two triples, because there are no \(4\)-cycles. Since
\[
7\binom32=\binom72,
\]
each pair occurs exactly once. This is the unique Steiner triple system on seven points.

For completeness, it can be labelled with triples
\[
012,\quad034,\quad056,\quad135,\quad146,\quad236,\quad245.
\tag{11}
\]
After selecting the three triples through \(0\), the remaining triples are forced up to relabelling.

Thus the only endpoint is the Heawood graph, the incidence graph of (11).

---

## 5. Exact evaluation of the Heawood graph

Let \(J\) denote the Heawood graph. Its flow polynomial is
\[
\boxed{
\Phi(J,q)
=(q-1)(q-2)
\left(
q^6-18q^5+140q^4-608q^3+1578q^2-2352q+1576
\right).
}
\tag{12}
\]

Here is a derivation, including the finite counting details.

### 5.1 Values at \(3\) and \(4\)

Orient every edge from one bipartition class to the other. Over \(\mathbb Z_3\), conservation at a cubic vertex forces its three incident nonzero values to be equal. Connectivity then gives
\[
\Phi(J,3)=2.
\tag{13}
\]

Next, the Heawood graph has exactly \(24\) perfect matchings. To see this, let \(A\) be the point-line incidence matrix of (11). For a set \(S\) of lines, write \(d_S(p)\) for the number of selected lines through point \(p\). Inclusion–exclusion gives
\[
\operatorname{per}(A)
=\sum_{S}(-1)^{7-|S|}\prod_p d_S(p).
\]
The sums of products, grouped by \(|S|\), are
\[
\begin{array}{c|rrrrr}
|S|&3&4&5&6&7\\ \hline
\displaystyle\sum_{|S|}\prod_p d_S(p)
&21&672&3024&4536&2187.
\end{array}
\]
Sets of at most two lines contribute zero. The entries follow as follows:

- Three lines cover all points only when concurrent: \(7\cdot3=21\).
- For four selected lines, their complement must be one of the \(28\) nonconcurrent triples; the product is \(24\).
- Deleting two lines gives product \(2^4 3^2=144\), for each of \(21\) choices.
- Deleting one line gives product \(2^3 3^4=648\), for each of \(7\) choices.
- Selecting all lines gives \(3^7=2187\).

Therefore
\[
\operatorname{per}(A)=21-672+3024-4536+2187=24.
\tag{14}
\]

Every \(2\)-factor of \(J\) is Hamiltonian. The only alternative, given bipartiteness and girth six, would be a \(6\)-cycle together with an \(8\)-cycle. But deleting any \(6\)-cycle leaves a theta graph with three paths of length three:

- Its six neighbours off the cycle are distinct, by the girth condition.
- The remaining graph has eight vertices, nine edges and minimum degree two.
- It is connected, since two components would each contain a cycle of length at least six.
- Its two degree-three vertices and six degree-two vertices form a theta graph; the three path lengths sum to nine, and every pair sums to at least six, so all three lengths are three.

Such a graph has no spanning \(8\)-cycle.

A nowhere-zero flow over \(\mathbb Z_2^2\) is a proper three-edge-colouring. Choosing one colour class gives a perfect matching, and its Hamiltonian complement has two alternating colourings. Hence
\[
\Phi(J,4)=2\cdot24=48.
\tag{15}
\]

### 5.2 The first five coefficients

Use the broken-circuit expansion for the cographic matroid:
\[
\Phi(J,q)=\sum_{k=0}^{8}(-1)^k b_k q^{8-k},
\tag{16}
\]
where \(b_k\) counts \(k\)-edge subsets containing no broken circuit. Here circuits are minimal edge cuts, and a broken circuit is obtained by deleting the largest edge from one. This expansion follows from sign-reversing cancellation in (1).

The bonds of sizes \(3,4,5\) in \(J\) are exactly the boundaries of a vertex, an adjacent pair of vertices, and a three-vertex path.

To justify completeness, take the smaller side \(S\) of a bond of size at most five, so \(|S|\le7\). A connected subcubic graph of girth six with two independent cycles needs at least eight vertices: a theta has total path length at least nine, and two disjoint cycles require still more vertices. If \(J[S]\) is unicyclic, its boundary has size \(|S|\ge6\). Thus \(J[S]\) must be a tree, and
\[
|\delta(S)|=|S|+2.
\]
This gives exactly the three types above. Their complements are connected, since otherwise two complement components would each have boundary at least three, exceeding the total boundary of at most five.

Fix a Hamiltonian cycle \(C_{14}\), and order the seven edges of its complementary matching after all cycle edges. The inclusion-minimal broken circuits of sizes at most four are then:

- **Fourteen pairs:** the two cycle edges incident with each vertex.
- **Fourteen triples:** one for each cycle edge, consisting of the two flanking cycle edges and one matching edge.
- **Fourteen quadruples:** one for each three-vertex path contained in the Hamiltonian cycle.

All other broken circuits arising from bonds of size at most five contain one of these pairs or triples.

This gives
\[
b_0=1,\qquad b_1=21,\qquad b_2=\binom{21}{2}-14=196.
\]
For triples, the fourteen forbidden pairs lie in \(14\cdot19\) triples, with fourteen double-counts. There are also the fourteen minimal forbidden triples. Therefore
\[
b_3=\binom{21}{3}-14\cdot19+14-14=1064.
\]

For \(b_4\), first avoid only the forbidden pairs. The selected cycle edges must form an independent set in a \(14\)-cycle. Its independent-set numbers through size four are
\[
1,\ 14,\ 77,\ 210,\ 294.
\]
Allowing arbitrary matching edges, the number of four-edge sets avoiding the pairs is
\[
\sum_{j=0}^{4} i_j(C_{14})\binom7{4-j}=3906.
\]
Each minimal forbidden triple has fifteen extensions avoiding forbidden pairs: nine cycle edges and six matching edges. No admissible four-set contains two such triples; an overlap would require a matching edge joining vertices at cyclic distance at most three, contrary to girth six. Finally exclude the fourteen minimal forbidden quadruples. Thus
\[
b_4=3906-14\cdot15-14=3682.
\]

Consequently,
\[
\Phi(J,q)
=q^8-21q^7+196q^6-1064q^5+3682q^4+\cdots.
\]
Also \(\Phi(J,1)=\Phi(J,2)=0\). Factoring these two roots and using (13) and (15) determines the remaining coefficients, giving (12).

### 5.3 Positivity

Set \(q=5+z\). The degree-six factor in (12) becomes
\[
z^6+12z^5+65z^4+192z^3+333z^2+328z+141.
\tag{17}
\]
Every coefficient is positive. Thus
\[
\Phi(J,q)>0\qquad(q\ge5).
\]

In particular, the exact half-integral value is
\[
\boxed{\Phi(J,11/2)=\frac{1\,680\,147}{256}>0.}
\tag{18}
\]

No graph search is being asserted here; the sole finite endpoint has been treated symbolically.

---

## 6. Conclusions of the reductions

### Cycle rank at most eight

Suppose positivity fails at some fixed \(q>5\) for a bridgeless graph with cycle rank at most eight. Choose a minimum-rank counterexample and apply the cubic reduction.

It has girth at least six. By (10), it has at most fourteen vertices; the Moore bound gives at least fourteen. Therefore it is the Heawood graph, contradicting (17).

This proves the first part of the theorem. It also shows that a minimum-rank cubic counterexample, if one exists, has at least sixteen vertices.

### Projective-planar graphs

Suppose a minimum-rank counterexample is embeddable in the projective plane. The surface-preserving cubic reduction again produces a cubic counterexample, and the minor-preserving short-cycle identities force girth at least six.

But a simple cubic graph of girth at least six cannot embed in a surface of positive Euler characteristic. In a cellular embedding,
\[
\chi=n-m+f,\qquad 6f\le2m.
\]
Hence
\[
\chi\le n-\frac23m=0,
\]
because \(m=3n/2\). A projective-planar graph has a cellular minimum-genus embedding in either the sphere or the projective plane, with Euler characteristic \(2\) or \(1\), respectively.

This contradiction proves the second part.

---

## 7. Where the general argument stops

The positive reduction is specific to cycles of length at most five. On a \(6\)-cycle, the analogous local extension count is
\[
\begin{aligned}
q-6
&+\sum_{\substack{\{i,j\}\subseteq\{0,\ldots,5\}\\
i,j\text{ nonadjacent cyclically}}}
 \mathbf1_{\{s_i=s_j\}}\\
&-\mathbf1_{\{s_0=s_2=s_4\}}
-\mathbf1_{\{s_1=s_3=s_5\}}.
\end{aligned}
\tag{19}
\]
At \(q=11/2\), the leading coefficient is \(-1/2\), and there are additional negative correction terms. Thus this is not an all-positive recursion.

The remaining class includes cubic graphs of girth at least six and arbitrarily large cycle rank, embedded only in surfaces of nonpositive Euler characteristic or with no fixed surface restriction. Nothing above establishes the required sign for that class. The general conjecture is therefore not resolved by this argument.