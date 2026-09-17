```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds on the torus when one summand has plane crossing number at most 10; in fact, two connected components in an optimal torus drawing cannot cross between one and ten times.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved here, and the novelty of these special cases has not been checked."
}
```

# A torus partial result

Write \(\operatorname{cr}_0(H)\) for the plane crossing number of \(H\). All graphs are finite, and drawings satisfy the usual general-position restrictions. Auxiliary embedded graphs may have loops and parallel edges.

I prove the following.

**Theorem.**
1. In an optimal drawing on the torus, the number of crossings between two distinct connected components is not any of
   \[
   1,2,\ldots,10.
   \]
2. Consequently, if \(G=G_1\sqcup G_2\) and
   \[
   \min\{\operatorname{cr}_0(G_1),\operatorname{cr}_0(G_2)\}\le 10,
   \]
   then every optimal torus drawing draws \(G_1\) and \(G_2\) disjointly.

The torus cut-and-chord argument in the previous attempt can be verified. Its cutoff at seven is not the endpoint of that method: a structural lemma for a toroidal map and its dual handles the exceptional crossing counts eight and ten.

The argument below is self-contained. I have not checked its novelty against the torus work mentioned in the question.

## 1. The redrawing statement to be proved

Consider a drawing of two connected graphs \(A,B\) on the torus. Let
- \(c_A,c_B\) be their internal crossing counts;
- \(m\) be their mutual crossing count.

We will prove:

> **Redrawing claim.** If \(1\le m\le 10\), then, for at least one \(i\in\{A,B\}\),
> \[
> \operatorname{cr}_0(i)\le c_i+m-1.
> \tag{1}
> \]

Moving that graph into an empty disk removes all \(m\) mutual crossings and adds at most \(m-1\) internal crossings. The same operation works if other components are present: choose the disk disjoint from all the remaining components.

Thus (1) implies the first assertion of the theorem, including its “every optimal drawing” formulation.

## 2. From the drawing to two toroidal maps

### 2.1. Internal planarization

Replace each internal crossing of \(A\) by a degree-four vertex, obtaining an embedded connected graph \(H_A\); do the same for \(B\). Their \(m\) mutual intersections are retained.

A plane drawing of \(H_i\) with \(q\) crossings gives a plane drawing of \(i\) with at most \(c_i+q\) crossings: at each designated degree-four vertex, restore the prescribed pairing using at most one crossing. Subsequent removal of self-crossings or other violations of good-drawing conditions does not increase the count.

If a regular neighborhood of either \(H_i\) has genus zero, it can be reproduced in the plane, and
\[
\operatorname{cr}_0(i)\le c_i.
\tag{2}
\]
We may therefore assume that both neighborhoods have genus one.

A connected genus-one subsurface of the torus has only disks as complementary components. For completeness, if its boundary has \(b\) components, and its complement has \(s\) components of total genus \(h\), Euler characteristic gives
\[
0=-b+(2s-2h-b),
\]
so \(s=b+h\). Since \(s\le b\), we have \(h=0\) and \(s=b\), and each complementary component is a disk. Thus both \(H_A,H_B\) are cellularly embedded.

### 2.2. Cutting at the mutual crossings

For each \(H_i\), delete a small open edge interval around each of the \(m\) mutual crossings. Let \(n_i\) be the number of connected pieces remaining.

Each piece of \(H_A\) lies in a disk face of \(H_B\). Moreover, every cut end is exposed to the outer face of its piece: the deleted half-interval continues from that end to the boundary of the containing face without meeting the cut graph.

Consequently, the pieces can be enclosed in pairwise disjoint disks, with their attachment points on the disk boundaries. These disks avoid \(H_B\) and all the remaining connector arcs. Here is a justification for the only possible nesting issue. Thicken a piece and fill its bounded complementary regions inside its containing face. No other cut piece can be trapped in such a region, because every cut piece has an attachment end with an unobstructed continuation to the face boundary. For the same reason, no connector arc is trapped there.

Replace these disks by vertices and retain the \(m\) connector arcs as edges. This gives an embedded connected multigraph \(Q_A\). Define \(Q_B\) similarly. Their edge sets are indexed by the same \(m\) crossing labels.

The maps \(Q_i\) are cellular on the torus. Indeed, the disks and connector bands form a neighborhood containing \(H_i\), so their genus is one; the preceding Euler-characteristic argument applies again.

Put
\[
r_i=m-n_i+1,
\tag{3}
\]
the cycle-space dimension of \(Q_i\).

Every face of \(Q_A\) contains at least one cut piece of \(H_B\). To see this, take a boundary edge of the face; the \(B\)-arc crossing that edge enters the face and leads to a cut piece. Since \(Q_A\) has
\[
f_A=m-n_A
\]
faces, it follows that
\[
n_B\ge m-n_A.
\]
Equivalently,
\[
r_A+r_B\le m+2.
\tag{4}
\]

We will also need the equality case:

> If \(r_A+r_B=m+2\), then \(Q_A\) and \(Q_B\) can be taken to be geometric duals.

Indeed, equality says that each face of \(Q_A\) contains exactly one cut piece of \(H_B\). Replacing that piece by a vertex gives one vertex per face and one edge crossing each edge of \(Q_A\), which is precisely a geometric dual.

## 3. The chord-redrawing bound

Let \(Q_i\) be one of these maps and choose a spanning tree \(T\). Thicken the corresponding tree connectors together with the vertex disks. A tree of disks and bands is a single disk \(\Delta\).

There remain \(r_i\) pairwise internally disjoint arcs outside \(\Delta\), each with two endpoints on \(\partial\Delta\). Reproduce \(\Delta\), including all the original graph pieces it contains, on the sphere. Draw the remaining arcs as chords in the complementary disk.

Two chords cross exactly when their endpoint pairs alternate.

Close each original outside arc by an arc in \(\Delta\), and denote its class in
\[
H_1(\mathbb T^2;\mathbb F_2)\cong\mathbb F_2^2
\]
by \(u_j\). These are the homology classes of the fundamental cycles associated with \(T\). Since the outside arcs are disjoint, their endpoint pairs alternate exactly when the two classes have intersection number one.

The three nonzero classes of \(H_1(\mathbb T^2;\mathbb F_2)\) intersect pairwise in one. Equal classes, and the zero class, have intersection zero. If the multiplicities of the three nonzero classes are \(a,b,c\), the number of added crossings is therefore
\[
k(T)=ab+bc+ca.
\tag{5}
\]
In particular,
\[
k(T)\le \left\lfloor\frac{r_i^2}{3}\right\rfloor.
\tag{6}
\]

Two refinements will be useful:

- if one fundamental cycle has zero homology,
  \[
  k(T)\le \left\lfloor\frac{(r_i-1)^2}{3}\right\rfloor;
  \tag{7}
  \]
- if at most two nonzero classes occur,
  \[
  k(T)\le \left\lfloor\frac{r_i^2}{4}\right\rfloor.
  \tag{8}
  \]

Restoring the original internal crossings gives
\[
\operatorname{cr}_0(i)\le c_i+k(T).
\tag{9}
\]

Combining (4) and (6), one of the two graphs satisfies
\[
\operatorname{cr}_0(i)\le c_i+F(m),
\qquad
F(m)=
\left\lfloor
\frac{(\lfloor m/2\rfloor+1)^2}{3}
\right\rfloor.
\tag{10}
\]
The relevant values are
\[
\begin{array}{c|rrrrrrrrrr}
m&1&2&3&4&5&6&7&8&9&10\\ \hline
F(m)&0&1&1&3&3&5&5&8&8&12.
\end{array}
\tag{11}
\]
Thus (1) follows already for \(m=1,\ldots,7\) and \(m=9\). We must treat eight and ten.

## 4. A duality fact about three homology classes

A **theta graph** consists of three internally vertex-disjoint paths with the same two distinct endpoints.

**Lemma 1.** Let \(Q\) be a cellular toroidal map, \(T\) a spanning tree, and \(R=Q^*\) its geometric dual. Suppose the fundamental cycles associated with \(T\) have nonzero homology and represent all three nonzero classes.

Then
\[
P=R-E(T)^*
\]
is a spanning, one-face subdivision of a theta graph. It has \(r(Q)\) edges.

**Proof.**
Contract \(T\) to a disk. The remaining \(r(Q)\) edges are disjoint proper arcs in the once-punctured torus.

Choose three arcs representing distinct nonzero classes. Their endpoints alternate pairwise, so the cyclic order of their six ends is, up to relabeling and reversal,
\[
x,y,z,x,y,z.
\]
Cutting the once-punctured torus along these three arcs leaves two disks. Each has three boundary intervals from the puncture boundary, alternating with three sides from the chosen arcs.

Every other arc lies in one of these disks. Its endpoints cannot lie on the same puncture-boundary interval, since then its closed homology class would be zero. If they lie on different such intervals, the arc is parallel to one of the three chosen arcs.

Thus all arcs belong to three parallel families. The dual of the three chosen arcs is a theta graph; adding a parallel arc subdivides the corresponding dual edge. Hence the complete dual is a subdivision of a theta graph.

Contracting a primal tree deletes its dual edges and preserves the face set, so \(P\) is spanning in \(R\). Its embedding has one face. \(\square\)

In a one-face toroidal theta subdivision, its three cycles represent the three nonzero homology classes. This also follows directly from the cellular chain complex: its cycle space has dimension two, and its inclusion induces an isomorphism onto \(H_1(\mathbb T^2;\mathbb F_2)\).

## 5. A structural lemma for a map and its dual

For auxiliary multigraphs, a “simple cycle” includes a loop or a pair of parallel edges. Its embedded image is a simple closed curve. On the torus, such a cycle has zero mod-two homology exactly when it is contractible.

**Lemma 2 — Theta-extension lemma.**  
Let \(R\) be a cellular toroidal map. Suppose neither \(R\) nor \(R^*\) has a simple cycle of zero homology. Suppose \(R\) contains a spanning, one-face theta subdivision \(P\) with at least five edges.

Then \(R\) has a spanning tree for which the fundamental-cycle homology multiplicities are
\[
(r(R)-2,1,1)
\]
among the three nonzero classes, in some order. Consequently,
\[
k(T)=2r(R)-3.
\tag{12}
\]

### Proof

Write the three \(u\)-\(v\) paths of \(P\) as \(P_1,P_2,P_3\). Their three cycles have distinct nonzero homology classes. For \(\{i,j,k\}=\{1,2,3\}\), put
\[
\lambda_i=[P_j\cup P_k].
\tag{13}
\]
All homology calculations below are over \(\mathbb F_2\).

Call edges of \(R-E(P)\) **additional edges**. Since \(P\) is spanning, their endpoints are vertices of \(P\).

We first establish restrictions on additional non-loop edges.

#### 5.1. Additional non-loop edges lie along one branch

An additional edge cannot join internal vertices of different branches. Between two such vertices, \(P\) contains four simple paths whose relative homology classes exhaust \(\mathbb F_2^2\): use the paths through \(u\), through \(v\), and the two paths using the third branch. The additional edge would close one of them into a zero-homology simple cycle.

Thus both endpoints of an additional non-loop edge lie on some \(P_i\). Let \(I\) be the interval of \(P_i\) between its endpoints. The three simple paths in \(P\) between these endpoints have relative classes
\[
0,\quad [P_i\cup P_j],\quad [P_i\cup P_k].
\]
Avoiding a zero-homology cycle forces
\[
[e\cup I]=[P_j\cup P_k]=\lambda_i.
\tag{14}
\]

Two additional edges cannot lie on different branches. Indeed, shortcut each branch along its additional edge. For edges on \(P_i,P_j\), the resulting two \(u\)-\(v\) paths form a simple cycle of class
\[
[P_i\cup P_j]+\lambda_i+\lambda_j=0.
\]
An additional \(uv\)-edge likewise cannot coexist with any other additional non-loop edge: it and the corresponding shortcut \(u\)-\(v\) path have the same relative class.

Finally, intervals belonging to two additional edges on one branch cannot overlap in an edge. If they did, the symmetric difference of the two cycles in (14) would be a simple cycle of class
\[
\lambda_i+\lambda_i=0.
\]
Their intervals may share an endpoint, but have disjoint interiors.

Therefore, if there are at least two additional non-loop edges, they all lie on one branch, and their intervals have disjoint interiors.

#### 5.2. A degree-two obstruction from the dual

We record a consequence of the hypothesis on \(R^*\).

> If \(z\) is a degree-two vertex of \(R\), with two distinct incident edges, then no null-homologous mod-two cycle of \(R\) can contain those edges.

To prove this, every null-homologous cycle is a mod-two sum of facial boundaries, by the cellular chain complex. An edge incident with the same face on both sides has coefficient zero in every such sum. Thus, if a null-homologous cycle contains an edge incident with \(z\), that edge has distinct faces on its two sides.

At a degree-two vertex, the two incident edges then have the same two distinct incident faces. Their dual edges form a simple contractible 2-cycle—the boundary of the dual face corresponding to \(z\). This contradicts the hypothesis on \(R^*\).

The theta subdivision \(P\) has
\[
|E(P)|-3\ge 2
\tag{15}
\]
internal vertices.

#### 5.3. At least two additional non-loop edges

Suppose these edges lie on \(P_i\), and put \(\lambda=\lambda_i\). Every cycle consisting of an additional edge and its interval has class \(\lambda\). So does
\[
C_0=P_j\cup P_k.
\]

Suppose an additional loop has class \(\mu\ne\lambda\). Two such classes have intersection number one. Therefore the loop's base vertex must belong to \(C_0\) and to every additional-edge cycle; otherwise it would be disjoint from one of these cycles.

Its base must consequently be \(u\) or \(v\), and that endpoint must belong to every additional-edge interval. This is impossible for two positive-length intervals with disjoint interiors.

Thus every additional loop also has class \(\lambda\).

#### 5.4. No additional non-loop edges

Suppose two additional loops have different classes. They must have the same base vertex \(w\), since otherwise they would be disjoint despite having intersection number one.

Every other loop must also be based at \(w\): a nonzero class cannot be orthogonal to two distinct nonzero classes. Moreover, \(w\) must be \(u\) or \(v\). If it were internal to \(P_i\), the nonzero cycle \(P_j\cup P_k\) would be disjoint from both loops, again impossible.

Take an internal vertex \(z\) of \(P\). It still has degree two in \(R\). Choose a cycle of \(P\) through \(z\), and add a suitable mod-two combination of the two loops to cancel its homology. The resulting null-homologous cycle still contains the edges at \(z\), contradicting Section 5.2.

Hence all additional loops have one common class \(\lambda\). If there are none, choose any nonzero \(\lambda\).

#### 5.5. Exactly one additional non-loop edge

Let the edge be \(e\), let \(I\subseteq P_i\) be its interval, and put
\[
C_e=e\cup I,\qquad \lambda=[C_e]=[P_j\cup P_k].
\]

Suppose a loop \(L\) has class \(\mu\ne\lambda\). Its base must belong to both \(C_e\) and \(P_j\cup P_k\), hence must be \(u\) or \(v\). In particular, \(I\) meets an endpoint of \(P_i\), so \(e\) has at most one internal endpoint.

Every additional loop is based at \(u\) or \(v\). Indeed, loops of class different from \(\lambda\) satisfy the preceding argument, while a loop of class \(\lambda\) must share its base with \(L\), because its class intersects \(\mu\) in one.

By (15), there is an internal vertex \(z\) of \(P\) not incident with \(e\). It has degree two in \(R\).

Relabel \(j,k\) so that
\[
[C_1]=\mu,\qquad C_1=P_i\cup P_j,
\]
and put \(C_2=P_i\cup P_k\), whose class is \(\mu+\lambda\). Both
\[
Z_1=C_1+L,\qquad Z_2=C_2+C_e+L
\tag{16}
\]
are null-homologous.

The cycle \(Z_1\) contains every edge of \(P_i\) and \(P_j\), while \(Z_2\) contains every edge of \(P_k\). Thus one of them contains the edges at \(z\), contradicting Section 5.2.

So every additional loop has class \(\lambda\) in this case as well.

#### 5.6. Choosing the spanning tree

We have shown the following: there is a branch \(P_i\) and a nonzero class
\[
\lambda=[P_j\cup P_k]
\]
such that all additional non-loop edges have both endpoints on \(P_i\), their cycles with the corresponding intervals have class \(\lambda\), and all additional loops have class \(\lambda\).

When there are only loops, choose \(P_i\) to correspond to their common class.

Choose a spanning tree \(T\subseteq P\) containing all of \(P_i\), and delete one edge from each of \(P_j,P_k\). The two fundamental cycles from the deleted edges have the two nonzero classes other than \(\lambda\). Every additional edge has fundamental-cycle class \(\lambda\).

There are
\[
|E(R)|-|E(P)|=r(R)-2
\]
additional edges. The multiplicities are therefore \((r(R)-2,1,1)\), giving
\[
k(T)=(r(R)-2)+(r(R)-2)+1=2r(R)-3.
\]
This proves the lemma. \(\square\)

## 6. Excluding eight and ten mutual crossings

We treat these two cases together. Write
\[
m=2s-2,\qquad s\in\{5,6\}.
\]

Continue with the maps \(Q_A,Q_B\) from Section 2.

If
\[
\min(r_A,r_B)\le s-1,
\]
then (6) gives a plane-redrawing cost at most
\[
\left\lfloor\frac{(s-1)^2}{3}\right\rfloor
=
\begin{cases}
5,&s=5,\\
8,&s=6,
\end{cases}
\]
which is strictly less than \(m\).

Otherwise, (4) forces
\[
r_A=r_B=s.
\tag{17}
\]
Equality holds in (4), so \(Q_A,Q_B\) are geometric duals.

Suppose one map contains a zero-homology simple cycle \(C\). Choose an edge \(e\in E(C)\), and extend \(C-e\) to a spanning tree; then \(C\) is the fundamental cycle of \(e\). For a loop, any spanning tree suffices. Bound (7) again gives a cost at most \(5\) or \(8\), respectively.

We may therefore assume that neither map has a zero-homology simple cycle.

Choose any spanning tree \(T_A\) of \(Q_A\). Its \(s\) fundamental cycles all have nonzero homology. If they use at most two classes, (8) gives cost at most
\[
\left\lfloor\frac{s^2}{4}\right\rfloor
=
\begin{cases}
6,&s=5,\\
9,&s=6,
\end{cases}
\]
again strictly less than \(m\).

Otherwise all three classes occur. Lemma 1 gives a spanning, one-face theta subdivision in \(Q_B\), with \(s\ge5\) edges. Lemma 2 applies to \(Q_B\) and its dual \(Q_A\), and supplies a spanning tree with
\[
k(T_B)=2r_B-3=2s-3=m-1.
\tag{18}
\]

Restoring internal crossings proves (1) in both remaining cases.

Together with Section 3, this proves the redrawing claim for every \(1\le m\le10\).

## 7. Optimality consequences

The first assertion of the theorem now follows directly: if two connected components in an optimal torus drawing had between one and ten mutual crossings, (1) would let us move one into an empty disk and strictly decrease the total crossing number.

For the second assertion, let \(C\) be a connected component in an optimal drawing. Write \(c_C\) for its internal crossings and \(t_C\) for its crossings with all other components. Replacing \(C\) by an optimal plane drawing in an empty disk shows that
\[
c_C+t_C\le \operatorname{cr}_0(C).
\tag{19}
\]

If \(\operatorname{cr}_0(C)\le10\) and \(C\) meets another component \(D\), their mutual crossing count lies between \(1\) and \(t_C\le10\), contradicting the first assertion. Thus every component of plane crossing number at most ten is disjoint from every other component.

Finally, if \(\operatorname{cr}_0(G_1)\le10\), every connected component \(C\) of \(G_1\) satisfies
\[
\operatorname{cr}_0(C)\le\operatorname{cr}_0(G_1)\le10.
\]
Hence \(G_1\) is disjoint from \(G_2\) in every optimal torus drawing. \(\square\)

## 8. What remains unresolved

This does **not** prove the conjecture for arbitrary graphs on the torus, or for arbitrary surfaces.

The first mutual crossing count not covered here is eleven. At that count, the basic inequality permits unequal cycle ranks, or a failure of exact primal-dual correspondence. The strict numerical estimates used above no longer settle all cases.

The proved advance over the supplied attempt is therefore:
\[
\boxed{\text{the torus cutoff increases from plane crossing number }7\text{ to }10.}
\]
The structural theta-extension lemma is the additional ingredient; no unproved conjecture or external literature result is used.