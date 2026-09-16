```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A constructive forest-completion criterion proves Hamiltonicity whenever one face-color class contains at most two nonquadrilateral faces.",
  "would_publish": false,
  "caveats": "This does not settle the general conjecture; novelty is not claimed, and the argument does not rely on the supplied literature review."
}
```

# A constructive partial result

I do not obtain a proof or counterexample to Barnette’s conjecture. I obtain a self-contained sufficient condition, an exact algorithm for a restricted kind of Hamiltonian cycle, and an explicit obstruction to extending that method directly to all Barnette graphs.

Throughout, graphs are finite and simple, and embeddings are on the sphere. Call a 3-connected cubic planar bipartite graph a **Barnette graph**.

## Theorem: forest completion

Let \(G\) be a Barnette graph, and let \(T=G^*\) be its plane dual. Choose a proper vertex 3-coloring of \(T\), with color classes \(R,B,Z\). Such a coloring always exists.

Put
\[
Q=\{z\in Z:\deg_T(z)=4\},\qquad L=Z\setminus Q.
\]
Thus \(L\) represents the nonquadrilateral faces of \(G\) in the face-color class \(Z\).

The following are equivalent:

1. \(G\) has a Hamiltonian cycle placing every \(R\)-face on one side and every \(B\)-face on the other.
2. There is a partition
   \[
   L=X\mathbin{\dot\cup}Y
   \]
   such that both
   \[
   T[R\cup X]\quad\text{and}\quad T[B\cup Y]
   \]
   are forests.

Given such a partition, a Hamiltonian cycle can be constructed in linear time.

In particular:

- **If one face-color class contains at most two nonquadrilateral faces, then \(G\) is Hamiltonian.**
- Consequently, **every Barnette graph with at most eight nonquadrilateral faces is Hamiltonian.**

The other two face-color classes may contain arbitrarily many faces of arbitrarily large sizes.

---

## 1. A planar cycle-rank identity

Because \(G\) is cubic and 3-connected, \(T\) is a simple plane triangulation. Because \(G\) is bipartite, every vertex of \(T\) has even degree.

An even plane triangulation has a proper vertex 3-coloring: color one triangle and propagate across adjacent triangles. Propagation is consistent around a vertex precisely because its degree is even. These local closed walks generate the closed walks on the sphere, so propagation is globally consistent. This also shows uniqueness up to permuting the three colors.

Consider the embedded bipartite graph
\[
H=T[R\cup Z].
\]
It is connected, and its faces correspond naturally to the vertices of \(B\). Indeed, deleting a vertex \(b\in B\) merges its incident triangular faces into the disk bounded by its neighbor cycle; every triangle contains exactly one vertex of \(B\).

For \(z\in Z\), its neighbors alternate between \(R\) and \(B\), so
\[
\deg_H(z)=\frac{\deg_T(z)}2.
\]

For a graph \(J\), including its isolated vertices, write
\[
\beta(J)=|E(J)|-|V(J)|+c(J),
\]
where \(c(J)\) is its number of components. Thus \(\beta(J)=0\) exactly when \(J\) is a forest.

### Lemma
For every \(Y\subseteq Z\),
\[
c(H-Y)-1=\beta\bigl(T[B\cup Y]\bigr). \tag{1}
\]

### Proof
Set
\[
F=T[B\cup Y],\qquad
d=\sum_{y\in Y}\deg_H(y).
\]
Deleting \(Y\) from \(H\) removes \(|Y|\) vertices and \(d\) edges, since \(Z\) is independent.

The faces of \(H\) are indexed by \(B\). Removing a vertex \(y\in Y\), together with its incident edges, merges precisely the faces incident with \(y\). Taking the transitive closure of these mergers gives exactly the components of \(F\). Consequently, \(H-Y\) has \(c(F)\) faces.

Let \(v_H,e_H\) denote the numbers of vertices and edges of \(H\). Euler’s formula gives
\[
v_H-e_H+|B|=2
\]
and
\[
(v_H-|Y|)-(e_H-d)+c(F)=1+c(H-Y).
\]
Subtracting,
\[
c(H-Y)-1=d-|B|-|Y|+c(F).
\]
The right-hand side is \(\beta(F)\), since \(F\) has \(d\) edges. ∎

A useful symmetric formulation follows. For \(P\subseteq Z\), put
\[
A=R\cup P,\qquad D=B\cup(Z\setminus P).
\]
Applying (1), and then interchanging \(R\) and \(B\), gives
\[
c(T[A])-1=\beta(T[D]),\qquad
c(T[D])-1=\beta(T[A]). \tag{2}
\]
In particular,
\[
T[A]\text{ is a tree}\quad\Longleftrightarrow\quad T[D]\text{ is a tree}. \tag{3}
\]

---

## 2. Completing the prescribed forests

Suppose
\[
L=X\mathbin{\dot\cup}Y
\]
satisfies the forest condition.

Since \(T[B\cup Y]\) is a forest, equation (1) says that \(H-Y\) is connected.

Every vertex \(q\in Q\) has degree two in \(H-Y\), with two distinct neighbors in \(R\). Suppress all these degree-two vertices, obtaining a connected plane multigraph \(K\) on
\[
V(K)=R\cup X.
\]
Each suppressed \(q\) gives a designated edge \(e_q\) of \(K\).

The edges of \(K\) not arising from suppression are precisely the edges of
\[
F_X=T[R\cup X].
\]
By hypothesis, \(F_X\) is a spanning forest of \(K\). Extend it to a spanning tree \(\mathcal T\) of \(K\).

Let
\[
Q_{\mathcal T}=\{q\in Q:e_q\in E(\mathcal T)\},
\qquad
A=R\cup X\cup Q_{\mathcal T}.
\]
Then \(T[A]\) is exactly the tree \(\mathcal T\) with its selected edges \(e_q\) subdivided. Hence \(T[A]\) is a tree.

By (3), the complementary induced graph
\[
T[V(T)\setminus A]
\]
is also a tree.

### Recovering a Hamiltonian cycle

Let \(\delta_T(A)\) be the edges of \(T\) with one endpoint in \(A\) and one outside it.

Both shores induce connected graphs, so \(\delta_T(A)\) is a bond—a minimal nonempty edge cut. Its dual edges therefore form a single cycle in \(G\).

Moreover, every triangular face of \(T\) contains an \(R\)-vertex in \(A\) and a \(B\)-vertex outside \(A\). It consequently has exactly two edges in \(\delta_T(A)\). The corresponding vertex of \(G\) has degree two in the dual cycle.

Thus the dual cycle passes through every vertex of \(G\): it is Hamiltonian.

For completeness, the bond-cycle assertion can also be seen directly here. The dual edges form a spanning 2-regular graph. If they had more than one cycle component, the Jordan curve theorem would make the edges dual to one component a proper nonempty cut contained in \(\delta_T(A)\), contradicting minimality.

This proves sufficiency.

### Necessity for the prescribed separation

Suppose a Hamiltonian cycle \(C\) separates all \(R\)-faces from all \(B\)-faces.

All vertices of \(G\) lie on \(C\). On either side, the remaining edges are noncrossing chords of a disk. The adjacency graph of the regions cut out by such chords is a tree: initially there is one region, and inserting each chord splits one region into two.

Therefore the vertices of \(T\) on either side of \(C\) induce trees. Let \(X\) be the vertices of \(L\) on the \(R\)-side and \(Y=L\setminus X\). Then
\[
T[R\cup X]\quad\text{and}\quad T[B\cup Y]
\]
are subgraphs of those trees, hence are forests.

This proves the stated equivalence.

---

## 3. Consequences and algorithm

### At most two exceptional faces in one color

If \(|L|\leq 2\), partition \(L\) so that
\[
|X|\leq 1,\qquad |Y|\leq 1.
\]
Each of \(T[R\cup X]\) and \(T[B\cup Y]\) is a star together with isolated vertices, or an edgeless graph. They are therefore forests.

The theorem gives a Hamiltonian cycle.

If \(G\) has at most eight nonquadrilateral faces in total, one of its three face-color classes contains at most two of them. This proves the second corollary.

Another immediate sufficient condition, allowing arbitrarily many exceptional faces, is
\[
T[R\cup L]\text{ is a forest}.
\]
Here one takes \(X=L\) and \(Y=\varnothing\).

Thus any counterexample to Barnette’s conjecture must have at least three nonquadrilateral faces in each face-color class. This is an elementary structural restriction, not a claimed improvement over known computational bounds.

### Exact search for color-separating cycles

For a fixed choice of \(R,B,Z\), let \(b=|L|\). Enumerate the \(2^b\) subsets \(X\subseteq L\), put \(Y=L\setminus X\), and test the two induced graphs for acyclicity.

If a partition succeeds, the construction above produces a Hamiltonian cycle. If none succeeds, the equivalence proves that no Hamiltonian cycle separates the prescribed classes \(R\) and \(B\).

For a supplied plane embedding, the running time is
\[
O(2^b n),
\]
where \(n=|V(G)|\). Once a successful partition is given, construction is linear: contract the components of the prescribed forest and find a spanning tree of the resulting connected graph.

**Rejection is not a certificate of non-Hamiltonicity.** It rules out only this restricted kind of Hamiltonian cycle.

---

## 4. An explicit obstruction to the method

The forest partition is not automatic, even with three exceptional faces in the chosen class.

Start with a plane \(K_{2,3}\), with bipartition
\[
\{r_+,r_-\},\qquad \{z_1,z_2,z_3\}.
\]
Its three faces correspond to the pairs \(12,23,31\). In the face corresponding to \(ij\), insert a path
\[
z_i-r_{ij}-z_j.
\]
Call the resulting plane graph \(H_0\). It has six quadrilateral faces.

Insert a new vertex into each face of \(H_0\), adjacent to all four boundary vertices. Let \(T_0\) be the resulting triangulation, colored by
\[
R=\{r_+,r_-,r_{12},r_{23},r_{31}\},\qquad
Z=\{z_1,z_2,z_3\},
\]
and with the six inserted face-centers forming \(B\).

The degrees are
\[
\deg_{T_0}(z_i)=8,\quad
\deg_{T_0}(r_\pm)=6,\quad
\deg_{T_0}(r_{ij})=4,\quad
\deg_{T_0}(b)=4.
\]
Thus \(T_0\) is a simple even triangulation, and its dual is a 24-vertex Barnette graph.

For every pair \(z_i,z_j\):

- they have the three common \(R\)-neighbors \(r_+,r_-,r_{ij}\), so
  \[
  T_0[R\cup\{z_i,z_j\}]
  \]
  contains a cycle;
- they have two common \(B\)-neighbors, namely the centers of the two faces created by the inserted path, so
  \[
  T_0[B\cup\{z_i,z_j\}]
  \]
  also contains a cycle.

Every partition of the three vertices of \(Z\) puts a pair on one side. Therefore no forest partition exists for this choice of \(Z\), and no Hamiltonian cycle separates the entire classes \(R\) and \(B\).

This is **not** a counterexample to Barnette: choosing \(B\) as the degree-four class makes the positive theorem apply immediately.

One can even force this obstruction in all three global colors. Glue three copies of \(T_0\) successively along triangular faces, assigning their obstructing triples to different global colors. Such gluing preserves simplicity and triangulation; an identified vertex has degree
\[
d_1+d_2-2,
\]
so evenness is preserved. Every cycle witnessing a pairwise obstruction survives. Hence all three choices of the distinguished class fail the forest test in the resulting even triangulation. Its dual has \(68\) vertices.

Again, this says nothing against its unrestricted Hamiltonicity. It shows that simply choosing the best of the three face-color classes cannot turn this criterion into a proof of Barnette’s conjecture.

## Remaining gap

The proved result is the forest-completion theorem and its stated special cases. General Hamiltonian cycles need not separate two entire face-color classes, and the explicit construction above shows that this restriction is a genuine limitation.

A resolution of the full conjecture therefore requires an additional mechanism beyond this spanning-tree completion argument.