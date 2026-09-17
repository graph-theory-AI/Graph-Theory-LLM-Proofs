```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain a complete two-cycle normal form for two digon components, including planarity and the sharp arc bound m <= 3n - 4.",
  "would_publish": false,
  "caveats": "This does not establish membership in H_2; the prescribed join decomposition and the case of three or more digon components remain unresolved, and novelty relative to the full paper is unverified."
}
```

# A two-digon-component classification

I do not resolve Conjecture 9.2. The main progress is an extension of the previous attempt from **one** digon component to **two**.

In particular, I prove the following.

> **Partial theorem.** Let \(D\) be a 2-extremal digraph, and let \(B(D)\) be its digon graph.
>
> 1. If \(B(D)\) has at most two components, then \(D\) is Eulerian and its underlying graph is planar.
> 2. If \(B(D)\) has exactly two components, then
>    \[
>    |A(D)|\le 3|V(D)|-4.
>    \]
>    This bound is attained for every order at least six.
> 3. Digraphs in the two-component case have the necessary-and-sufficient two-cycle normal form given in Section 3 below. Its connectivity condition is an explicit cyclic-interval test on two auxiliary trees.

The initial reductions from the previous attempt are independently verified below. One additional strengthening is useful: in the connected tree-plus-cycle normal form, local arc-connectivity two is equivalent to **every** tree edge inducing a cyclic interval—not merely the stated separation condition on heavy vertices.

## 1. Definitions and criticality reduction

Digraphs are finite and loopless, with no parallel arcs; opposite arcs are allowed. Auxiliary digraphs used in the proof may have parallel arcs, counted with multiplicity.

Write
\[
\lambda_D(u,v)
\]
for the maximum number of arc-disjoint directed \(u\)-to-\(v\) paths, and
\[
\lambda(D)=\max_{u\ne v}\lambda_D(u,v).
\]

The digon graph \(B(D)\) has vertex set \(V(D)\), with an undirected edge \(xy\) precisely when both arcs \(xy,yx\) belong to \(D\). For an undirected graph \(G\), write \(\overleftrightarrow G\) for its symmetric orientation.

The extremal-block hypotheses used here are
\[
D\text{ strong},\qquad U(D)\text{ 2-connected},\qquad
\vec\chi(D)=3,\qquad \lambda(D)=2.
\]
All the structural results can alternatively be read directly as statements about 3-dicritical digraphs with \(\lambda\le2\). Here, **3-dicritical** means that the dichromatic number is three and every proper subdigraph is 2-dicolorable.

### Lemma 1.1
A digraph satisfying the extremal-block hypotheses is 3-dicritical.

#### Proof

Choose an inclusion-minimal subdigraph \(Q\subseteq D\) with \(\vec\chi(Q)=3\). It is strong: otherwise one proper strong component already has dichromatic number three.

Every nontrivial outgoing cut of \(Q\) has size at least two. Indeed, if \(d_Q^+(X)\le1\), 2-dicolor \(Q[X]\) and \(Q[V(Q)\setminus X]\). If there is one outgoing arc, permute the colors on one side to make that arc bichromatic. The combined coloring has no monochromatic directed cycle crossing the cut, a contradiction. Thus directed Menger gives two arc-disjoint \(x\)-to-\(y\) paths in \(Q\) for every \(x\ne y\).

We need the following ear observation:

> If \(Q\) is a proper strong subdigraph of a strong digraph \(D\), and \(U(D)\) is 2-connected, then either there is an unused arc between vertices of \(Q\), or there is a directed path with distinct ends in \(Q\) and all internal vertices outside \(Q\).

Here is a verification. A weak component \(W\) of \(D-V(Q)\) has at least two distinct neighbors in \(Q\), by 2-connectivity. Condense \(D[W]\) into its strong components. Each condensation vertex is reachable through \(W\) from some vertex of \(Q\), and can reach some vertex of \(Q\). If there is no ear with distinct ends, all such entrance and exit vertices for a given component must be the same vertex of \(Q\). These labels agree along every condensation arc, and therefore throughout \(W\). All attachments of \(W\) would consequently use one vertex of \(Q\), a contradiction.

An unused arc or an ear from \(x\) to \(y\), together with the two arc-disjoint \(x\)-to-\(y\) paths in \(Q\), gives three such paths in \(D\). Hence \(Q=D\). ∎

### Lemma 1.2
If \(D\) is 3-dicritical, then either \(D\) is a symmetric odd cycle or \(B(D)\) is a forest.

#### Proof

If \(B(D)\) contains an odd cycle, its symmetric orientation is a subdigraph of dichromatic number three. Criticality forces it to be all of \(D\).

Otherwise \(B(D)\) is bipartite. Suppose it contains a cycle and let \(xy\) be an edge of that cycle. Delete the arc \(xy\), retaining \(yx\). In any 2-dicoloring of \(D-xy\), the alternate \(x\)-to-\(y\) path around the even digon cycle forces \(x\) and \(y\) to have different colors. Restoring \(xy\) cannot create a monochromatic directed cycle, contrary to criticality. ∎

Consequently, Conjecture 9.2 holds when the digon graph contains a cycle: the digraph must be a defining symmetric odd cycle.

## 2. A strengthened tree-plus-cycle lemma

This section supplies the connectivity tool needed for the two-component case.

Let \(T\) be a tree, and let \(C\) be a directed cycle on a set \(S\subseteq V(T)\), where \(|S|\ge3\). Assume every leaf of \(T\) belongs to \(S\). Put
\[
M(T,C)=\overleftrightarrow T\cup C.
\]
For this auxiliary construction, tree arcs and cycle arcs are counted separately if they are parallel.

Call an edge \(e\in E(T)\) **interval-compatible** if the vertices of \(S\) on either side of \(T-e\) form a nonempty proper cyclic interval in the order prescribed by \(C\).

### Lemma 2.1
Under these assumptions,
\[
\lambda(M(T,C))=2
\quad\Longleftrightarrow\quad
\text{every edge of \(T\) is interval-compatible}. \tag{2.1}
\]

If these conditions hold, \(M(T,C)\) has planar underlying multigraph.

#### Proof: connectivity

For every vertex set \(Z\),
\[
d_M^+(Z)=|\delta_T(Z)|+\rho_C(Z), \tag{2.2}
\]
where \(\rho_C(Z)\) is the number of cycle arcs leaving \(Z\).

Every nontrivial outgoing cut has size at least two. If \(|\delta_T(Z)|\ge2\), this is immediate. If \(|\delta_T(Z)|=1\), both sides contain a leaf of \(T\), hence a vertex of \(S\), so \(\rho_C(Z)\ge1\).

The cuts of size exactly two have only the following forms.

* **Type I:** \(|\delta_T(Z)|=1\) and \(\rho_C(Z)=1\). These are exactly the cuts associated with interval-compatible edges.
* **Type II:** \(|\delta_T(Z)|=2\) and \(\rho_C(Z)=0\). One side \(W\) contains no vertex of \(S\).

In Type II, \(W\) is connected and every vertex of \(W\) has degree two in \(T\). To see this, each component \(K\) of \(T[W]\) has no leaf of \(T\), and thus
\[
|\delta_T(K)|
 =\sum_{v\in K}d_T(v)-2(|K|-1)\ge2.
\]
Since the total boundary has size two, there is only one component. Equality then forces every degree to be two.

Call a vertex **heavy** when
\[
d_T(v)+\mathbf 1_{v\in S}\ge3.
\]
A Type II cut cannot separate two heavy vertices.

Now suppress all degree-two vertices of \(T\) that are not in \(S\). Along each resulting unsubdivided edge, all original edges induce the same partition of \(S\). An edge incident with a leaf of the suppressed tree is automatically interval-compatible.

Therefore, if some original edge is not interval-compatible, it lies on a suppressed edge whose two ends \(u,v\) are heavy. No Type I cut of size two separates \(u,v\), because every edge on their connecting path is incompatible. No Type II cut does so either. By directed Menger,
\[
\lambda_M(u,v)\ge3.
\]

Conversely, if every tree edge is interval-compatible, every two distinct vertices are separated by a cut of size two arising from an edge on their tree path. Together with the lower bound on all cuts, this proves (2.1).

#### Proof: planarity

Attach a new pendant vertex \(s'\) to each \(s\in S\). The leaves of the enlarged tree are now exactly the vertices \(s'\). Every edge induces an interval in their prescribed cyclic order.

Such a tree has a plane embedding with this leaf order: root it at one leaf, break the cyclic order there, and order each vertex’s child subtrees by their disjoint leaf intervals. Add a cycle through the leaves in the outer face. Finally contract every edge \(ss'\). This produces a planar embedding of \(T\cup C\). ∎

### Connected digon graphs

For completeness, the connected normal form follows immediately from criticality.

### Proposition 2.2
Let \(D\) be 3-dicritical with connected digon graph. Then either \(D\) is a symmetric odd cycle, or
\[
D=\overleftrightarrow T\cup C,
\]
where:

* \(T=B(D)\) is a tree;
* the vertices of \(C\) all lie in one bipartition class of \(T\);
* every leaf of \(T\) belongs to \(C\).

In the latter case, \(\lambda(D)=2\) exactly when every tree edge is interval-compatible.

#### Proof

By Lemma 1.2, the non-base case has \(B(D)=T\), a tree. The digons force its bipartition coloring, up to reversal. Since this is not a dicoloring, one bipartition class contains a directed cycle \(C\).

The subdigraph \(\overleftrightarrow T\cup C\) is already not 2-dicolorable, so criticality makes it all of \(D\). A leaf outside \(C\) could be deleted without removing the obstruction, again contradicting criticality. Apply Lemma 2.1. ∎

This both verifies and strengthens the corresponding connected-case result in the previous attempt.

## 3. The two-component normal form

The next theorem is the main structural result.

### Theorem 3.1
A digraph \(D\) is 2-extremal and has exactly two digon components if and only if it has the following form.

Take two vertex-disjoint nonempty trees \(T_1,T_2\), with bipartitions
\[
(X_1,Y_1),\qquad (X_2,Y_2),
\]
and two directed cycles \(C_0,C_1\), each of length at least three, satisfying:

1. **Opposite parity constraints**
   \[
   V(C_0)\subseteq X_1\cup X_2,\qquad
   V(C_1)\subseteq X_1\cup Y_2,
   \]
   and each cycle meets both trees.

2. **Small cycle intersection**
   \[
   |V(C_0)\cap V(C_1)|\le1.
   \]

3. **Minimal trees and separated hulls.**  
   Put
   \[
   S_{ij}=V(T_i)\cap V(C_j),
   \]
   and let \(H_{ij}\) be the minimal subtree of \(T_i\) spanning \(S_{ij}\). Then \(T_i\) is the minimal subtree spanning \(S_{i0}\cup S_{i1}\), and
   \[
   |V(H_{i0})\cap V(H_{i1})|\le1
   \qquad(i=1,2).
   \]

4. **Two interval tests.**  
   Let \(P_i\) be the path connecting \(H_{i0}\) and \(H_{i1}\), allowing a zero-length path when they meet. Write \(t_{ij}\) for its endpoint in \(H_{ij}\).

   For \(j=0,1\), form the auxiliary tree
   \[
   U_j=H_{1j}\cup H_{2j}+t_{1j}t_{2j}.
   \]
   Every edge of \(U_j\) must be interval-compatible with the cyclic order of \(C_j\).

The resulting digraph is
\[
D=\overleftrightarrow{T_1}\cup
  \overleftrightarrow{T_2}\cup C_0\cup C_1. \tag{3.1}
\]

The added edge of \(U_j\) is virtual. If its arcs are parallel to a cycle arc, the auxiliary digraph counts them separately.

### 3.1 Necessity of the two cycles

Let \(D\) be 2-extremal with two digon components. By Lemmas 1.1 and 1.2, it is 3-dicritical and
\[
B(D)=T_1\cup T_2
\]
for two trees.

A 2-coloring avoiding monochromatic digons is determined by the independent flips of these two trees. Up to a global reversal, there are only two possibilities.

There cannot be a directed cycle lying in one bipartition class of a single \(T_i\): that cycle together with \(\overleftrightarrow{T_i}\) would be a proper non-2-dicolorable subdigraph.

Choose a monochromatic directed cycle witnessing the failure of each of the two relative flips. Both cycles meet both trees. After exchanging the tree names and bipartition labels if necessary, they have precisely the parity pattern in condition 1.

Their two constraints contradict one another: one is monochromatic when the colors on \(X_1,X_2\) agree, and the other when they disagree. Thus the subdigraph in (3.1) is already not 2-dicolorable. Criticality proves equality with \(D\).

Every leaf of either tree must lie on one of the two cycles; otherwise deleting it preserves the obstruction. Equivalently, each \(T_i\) is the minimal subtree spanning \(S_{i0}\cup S_{i1}\).

### 3.2 The cycles meet in at most one vertex

Any common cycle vertex belongs to \(X_1\), because the cycles use opposite bipartition classes in \(T_2\).

Suppose they have at least two common vertices. Since \(C_1\) has vertices in \(T_2\) that are not on \(C_0\), it has a directed subpath \(R\) with distinct ends \(u,v\in V(C_0)\), all internal vertices outside \(C_0\).

There are then three arc-disjoint \(u\)-to-\(v\) paths:

1. \(R\);
2. the directed \(u\)-to-\(v\) segment of \(C_0\);
3. the bidirected tree path \(uT_1v\).

The third uses only digon arcs; the cycles use none. This contradicts \(\lambda(D)\le2\). Hence condition 2 holds. In particular, the two cycles are arc-disjoint.

### 3.3 The two hulls in a tree share no edge

Fix \(i\), and suppose
\[
K=H_{i0}\cap H_{i1}
\]
contains an edge. As an intersection of subtrees, \(K\) is a subtree. Choose two distinct leaves \(x,y\) of \(K\).

For each \(j\in\{0,1\}\), there is a path in \(H_{ij}\) from \(x\) to a terminal of \(S_{ij}\), meeting \(K\) only at \(x\). If \(x\) is itself a terminal, use a path of length zero. Otherwise minimality of \(H_{ij}\) implies that \(x\) has an incident edge of \(H_{ij}\) outside \(K\), leading to a terminal.

The paths selected for \(j=0,1\) are edge-disjoint: a common initial edge would belong to \(K\). Make the analogous choices at \(y\). The branches attached at \(x\) and \(y\) are also disjoint.

For each \(j\), travel:

* from \(x\) along its selected bidirected branch;
* along \(C_j\) to the terminal selected at \(y\);
* along that branch to \(y\).

These give two arc-disjoint directed walks, also arc-disjoint from the directed tree path \(xKy\). Extracting paths produces three arc-disjoint \(x\)-to-\(y\) paths, a contradiction.

Thus the hull intersection has at most one vertex, proving condition 3.

## 4. Why the two interval tests are exact

The remaining issue in Theorem 3.1 is condition 4 and its sufficiency. The following replacement lemma handles it.

### Lemma 4.1 — two-terminal replacement
Let \(N_0,N_1\) be strong Eulerian digraphs, arc-disjoint and with vertex intersection exactly \(\{a,b\}\). Let
\[
M_j=N_j+\{ab,ba\},
\]
where the two added arcs are distinguished virtual arcs. Suppose each \(M_j\) is 2-arc-strong. Then
\[
\lambda(N_0\cup N_1)=2
\quad\Longleftrightarrow\quad
\lambda(M_0)=\lambda(M_1)=2. \tag{4.1}
\]

#### Proof: necessity

In a strong Eulerian digraph there are arc-disjoint paths from \(a\) to \(b\) and from \(b\) to \(a\).

Indeed, choose an \(a\)-to-\(b\) path \(P\). After deleting its arcs, every cut containing \(b\) and excluding \(a\) has outgoing size minus incoming size equal to one. In particular, its outgoing size is positive, so a \(b\)-to-\(a\) path remains.

The virtual arcs of \(M_0\) can therefore be routed arc-disjointly through \(N_1\). Thus three arc-disjoint paths in \(M_0\) would yield three in \(N_0\cup N_1\). The same holds with the indices exchanged.

#### Proof: sufficiency

First, in any Eulerian 2-arc-strong digraph \(M\) with \(\lambda(M)=2\) and a distinguished digon \(ab\), every vertex \(z\notin\{a,b\}\) can be separated from both \(a,b\) by a cut of size two.

Choose minimum outgoing cuts \(A,B\), of size two, with
\[
a\in A,\ z\notin A,\qquad b\in B,\ z\notin B.
\]
If one already contains both \(a,b\), use it. Otherwise:

* If \(A\cap B\ne\varnothing\), cut submodularity and 2-arc-strength give
  \[
  d^+(A\cup B)\le2.
  \]
* If \(A\cap B=\varnothing\), the two distinguished opposite arcs cross between \(A,B\), so
  \[
  d^+(A\cup B)
  =d^+(A)+d^+(B)-e(A,B)-e(B,A)\le2.
  \]

In either case, \(A\cup B\) is a cut of size two containing \(a,b\) and excluding \(z\). Its complement also has outgoing size two, by Eulerianity.

Now consider two vertices in \(N_0\). Take a size-two separating cut in \(M_0\).

* If \(a,b\) are on the same side, put all of \(N_1-\{a,b\}\) on that side.
* If they are on opposite sides, combine it with an appropriately oriented size-two \(a,b\)-separating cut in \(M_1\). Each cut loses one virtual outgoing arc, leaving total outgoing size two.

Thus every ordered pair within either module has local connectivity at most two.

For a pair with one vertex in each module, neither a terminal, use the cut just established that separates the first vertex from both terminals, and put the other module outside it. This also has size two.

Finally, the union is 2-arc-strong. If a cut separates \(a,b\), each module contributes at least one outgoing arc. If not, any module meeting both sides contributes at least two. This proves (4.1). ∎

### Applying the replacement lemma

Use the data obtained in Section 3, and put
\[
a=t_{10},\qquad b=t_{20}.
\]
Define
\[
N_0=\overleftrightarrow{H_{10}}\cup
     \overleftrightarrow{H_{20}}\cup C_0,
\]
and
\[
N_1=
\overleftrightarrow{H_{11}\cup P_1}\cup
\overleftrightarrow{H_{21}\cup P_2}\cup C_1.
\]

The hull-intersection property shows that
\[
V(N_0)\cap V(N_1)=\{a,b\}.
\]
Both modules are strong and Eulerian.

Adding the virtual digon \(ab\) to \(N_0\) gives
\[
M(U_0,C_0).
\]
Adding it to \(N_1\) gives a tree-plus-cycle digraph whose tree is obtained from \(U_1\) by subdividing its virtual edge. The subdivision vertices are not on \(C_1\), so this changes none of the relevant partitions of \(V(C_1)\).

All leaves of both auxiliary trees lie on their respective cycles. Lemmas 2.1 and 4.1 now show that
\[
\lambda(D)=2
\]
is equivalent to precisely the two interval tests in condition 4.

### Converse: the data produce a 2-extremal digraph

Suppose conditions 1–4 of Theorem 3.1 hold.

The two cycles impose contradictory requirements on the relative bipartition flips, so \(D\) is not 2-dicolorable.

It is 3-dicolorable. Give \(X_1,X_2\) color 0 and \(Y_1,Y_2\) color 1, and recolor one vertex of \(C_0\cap X_1\) with color 2. All digons are bichromatic. Since the two directed cycles meet in at most one vertex, their union has no directed cycles other than \(C_0,C_1\); neither is monochromatic after this recoloring.

The digraph is strong because the trees are symmetric and each cycle meets both trees.

Its underlying graph is 2-connected. To verify this, delete a vertex \(v\in T_i\). The other tree remains connected and meets both \(C_0-v\) and \(C_1-v\). Every component of \(T_i-v\) contains an original leaf of \(T_i\), hence a vertex of one of the cycles. Consequently all vertices of \(D-v\) remain connected.

Finally, condition 4 and the replacement argument give \(\lambda(D)=2\). Thus \(D\) is 2-extremal, completing the proof of Theorem 3.1. ∎

## 5. Consequences

### 5.1 Planarity and Eulerianity

In the two-component normal form, the two cycles are arc-disjoint and use no digon arcs. Hence
\[
D=\overleftrightarrow{T_1}\cup\overleftrightarrow{T_2}\cup C_0\cup C_1
\]
is Eulerian.

By Lemma 2.1, both augmented modules in Section 4 are planar. Embed a distinguished virtual edge on the outer face of each, glue along that edge, and delete the virtual arcs. This gives a planar underlying graph for \(D\).

Together with Proposition 2.2, this proves:

> Every 2-extremal digraph whose digon graph has at most two components is Eulerian and planar.

### 5.2 The sharp arc bound

Let
\[
n=|V(D)|,\qquad q_j=|V(C_j)|.
\]
The two trees have \(n-2\) edges, and all displayed arc sets are disjoint. Therefore
\[
|A(D)|=2(n-2)+q_0+q_1. \tag{5.1}
\]

I claim that at least one vertex belongs to neither cycle.

Suppose instead that every vertex lies on \(C_0\cup C_1\). All vertices of \(T_1\) would then belong to \(X_1\), so \(T_1\) would consist of one vertex \(v\), common to both cycles.

Every vertex of \(T_2\) would belong either to \(C_0\cap X_2\) or to \(C_1\cap Y_2\). Both sets have size at least two, since both cycles have length at least three.

A tree with both bipartition classes of size at least two has an edge whose ends both have degree at least two. Such an edge belongs to the minimal subtree spanning each bipartition class: each side of the edge contains a vertex of each class. It would therefore belong to both \(H_{20}\) and \(H_{21}\), contradicting condition 3.

Thus, using also \(|V(C_0)\cap V(C_1)|\le1\),
\[
q_0+q_1
=
|V(C_0)\cup V(C_1)|+|V(C_0)\cap V(C_1)|
\le n.
\]
Equation (5.1) yields
\[
\boxed{|A(D)|\le3n-4.}
\]

If the two cycles are vertex-disjoint, the argument gives the stronger bound
\[
|A(D)|\le3n-5.
\]

### 5.3 Sharp examples for every \(n\ge6\)

Fix \(p\ge2\). Take vertices
\[
v,w,x,c,a_1,\ldots,a_p.
\]
Add the digons corresponding to the tree edges
\[
wa_i\quad(1\le i\le p),\qquad wx,\qquad xc,
\]
and add the directed cycles
\[
C_0=v\,a_1a_2\cdots a_p\,v,
\qquad
C_1=v\,w\,c\,v.
\]

The digon graph has exactly two components: the isolated vertex \(v\) and the displayed tree.

Its digons force all \(a_i,x\) to have one color and \(w,c\) the other. Whichever color is given to \(v\), one of \(C_0,C_1\) is monochromatic. Giving \(v\) a third color proves \(\vec\chi=3\).

Every vertex except \(w\) has indegree and outdegree two. Therefore every ordered pair has local connectivity at most two. There are two arc-disjoint \(v\)-to-\(w\) paths,
\[
v w,\qquad v a_1 w,
\]
so \(\lambda=2\). Strong connectivity and underlying 2-connectivity follow directly, or from the verification in the converse above.

Finally,
\[
n=p+4,\qquad
|A(D)|=2(p+2)+(p+1)+3=3p+8=3n-4.
\]

### 5.4 Recognition in this restricted case

The normal form gives a direct recognition procedure when \(B(D)\) has at most two components.

For two tree components, test the two relative bipartition flips. If both fail, extract a monochromatic cycle from each, then check:

* the union description;
* cycle intersection;
* minimal hulls and their intersections;
* the two auxiliary interval conditions.

These tests are linear-time once the digon graph is available. For the interval test, root an auxiliary tree at a marked vertex and number the other marked vertices in the linear order obtained by breaking the cycle there. A rooted subtree’s marked set is an interval exactly when
\[
\max-\min+1=\text{number of marked vertices}.
\]
All counts and extrema are obtained by one postorder traversal.

## 6. What remains unresolved

This is a classification by explicit tree-and-cycle data, **not** a proof of membership in \(\mathcal H_2\).

Two gaps remain relative to Conjecture 9.2:

1. I have not expressed every normal form above using the paper’s directed Hajós joins and 2-Hajós tree joins.
2. With three or more digon components, failure of all relative flips need not be witnessed by just two contradictory cycles. The argument forcing arc-disjoint cycles and edge-disjoint hulls therefore does not cover the general case.

Thus there is no complete proof or counterexample here. The concrete progress is the two-component normal form, its exact local-connectivity criterion, planarity, and the sharp bound \(3n-4\).