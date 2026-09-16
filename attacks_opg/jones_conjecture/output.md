```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained reduction argument proves cc(G) ≤ 2cp(G) for every graph of treewidth at most 3, without assuming planarity.",
  "would_publish": false,
  "caveats": "The general planar case is not resolved, and novelty of this special case has not been checked."
}
```

# A treewidth-three special case

Write
\[
\nu(G)=cp(G),\qquad \tau(G)=cc(G).
\]
I work with finite, simple, undirected graphs.

The following is a complete special-case result. I do **not** claim that it is new.

**Theorem.** Every graph \(G\) of treewidth at most \(3\) satisfies
\[
\tau(G)\le 2\nu(G).
\]
More constructively, given a tree decomposition of width at most \(3\), the proof produces a feedback vertex set \(X\) and a collection \(\mathcal P\) of vertex-disjoint cycles such that
\[
|X|\le 2|\mathcal P|.
\]

The constant is sharp already for \(K_4\), where \(\tau(K_4)=2\) and \(\nu(K_4)=1\). Planarity is not needed for this theorem.

## 1. Elementary reductions

We first record three reductions.

### Removing a vertex of degree at most one

If \(d_G(v)\le 1\), then no cycle contains \(v\). Consequently,
\[
\tau(G-v)=\tau(G),\qquad \nu(G-v)=\nu(G).
\]

### Suppressing a degree-two vertex

Suppose \(N_G(v)=\{a,b\}\) and \(ab\notin E(G)\). Set
\[
G'=G-v+ab.
\]
Then
\[
\tau(G')=\tau(G),\qquad \nu(G')=\nu(G).
\]

Indeed, \(G\) is obtained by subdividing the edge \(ab\) of \(G'\). Cycles correspond by replacing \(ab\) with \(avb\), and this correspondence preserves vertex-disjoint cycle collections.

For feedback vertex sets, a set in \(G'\) also meets every cycle of \(G\). Conversely, if a feedback vertex set of \(G\) contains \(v\), replace \(v\) by \(a\); every cycle containing \(v\) also contains \(a\). The resulting set, interpreted in \(G'\), is a feedback vertex set of no greater size.

The condition \(ab\notin E(G)\) is important: otherwise simply suppressing \(v\) would lose the triangle \(avb\).

### Reserving a cycle while deleting two vertices

Suppose a cycle \(C\) and a set \(A\subseteq V(C)\), with \(|A|\le 2\), have the following property:
\[
\text{every vertex of }V(C)\setminus A
\text{ has degree at most one in }G-A.
\tag{1}
\]
No cycle of \(G-A\) can then contain a vertex of \(C\). Thus
\[
\nu(G)\ge 1+\nu(G-A),
\qquad
\tau(G)\le |A|+\tau(G-A).
\tag{2}
\]
In particular, Jones’ inequality for \(G-A\) implies it for \(G\).

We will use two configurations satisfying (1):

* **Triangle configuration:** a triangle \(vab\) with \(d_G(v)\le 3\), taking \(A=\{a,b\}\).
* **Four-cycle configuration:** a cycle \(aubva\) with
  \[
  d_G(u),d_G(v)\le 3,
  \]
  taking \(A=\{a,b\}\).

In the second configuration, the two opposite vertices \(u,v\) each lose two neighbors and consequently have degree at most one. The cycle need not be induced.

## 2. A reducible configuration in every width-three graph

Recall that a tree decomposition consists of a tree \(T\) and bags \(B_t\subseteq V(G)\) such that:

1. the bags cover \(V(G)\);
2. each edge has both endpoints in a common bag;
3. the bags containing any fixed vertex induce a connected subtree.

Width at most \(3\) means that every bag has at most four vertices.

**Lemma.** Let \(G\) be a nonempty graph of treewidth at most \(3\) and minimum degree at least \(3\). Then \(G\) contains either:

1. a triangle containing a vertex of degree \(3\); or
2. a four-cycle whose two opposite vertices both have degree \(3\).

**Proof.**
Take a width-three tree decomposition. Whenever one of two adjacent bags is contained in the other, contract that tree edge and retain the larger bag. This preserves the decomposition axioms. We may therefore assume that neither of two adjacent bags contains the other.

If the decomposition has only one bag, then \(G\) has at most four vertices. Minimum degree at least three forces \(G=K_4\), giving the first configuration.

Root the decomposition tree. Choose a deepest node having at least one child. Write \(B\) for its bag. All its children are leaves.

Consider a child leaf bag \(L\), and put
\[
D=L\setminus B.
\]
The pruning condition gives \(D\ne\varnothing\). Every vertex \(x\in D\) occurs only in \(L\), so all its neighbors belong to \(L\). Since \(|L|\le4\) and \(d_G(x)\ge3\), necessarily
\[
|L|=4,\qquad d_G(x)=3,\qquad N_G(x)=L\setminus\{x\}.
\tag{3}
\]

If \(D\) contains distinct vertices \(x,y\), then \(x,y\) and any third vertex of \(L\) form a triangle containing a degree-three vertex. We may therefore assume, for every child leaf, that
\[
L=S\cup\{u\},\qquad S=L\cap B,\qquad |S|=3,
\]
where \(u\) has degree three and \(N_G(u)=S\).

If \(G[S]\) has an edge, that edge together with \(u\) gives the first configuration. Hence, assuming the first configuration is absent, every such \(S\) is independent.

If \(B\) has two child leaf bags, with private vertices \(u_1,u_2\) and corresponding three-element sets \(S_1,S_2\), then
\[
|S_1\cap S_2|\ge 3+3-|B|\ge2.
\]
Choose distinct \(a,b\in S_1\cap S_2\). The vertices
\[
a,u_1,b,u_2
\]
form a four-cycle, and \(u_1,u_2\) have degree three. This is the second configuration.

It remains to consider the case that \(B\) has exactly one child leaf
\[
L=S\cup\{u\}.
\]
Because \(B\not\subseteq L\), the bag-size bound implies
\[
B=S\cup\{w\}
\]
for a vertex \(w\notin L\).

If \(B\) is the root bag, then \(w\) occurs only in \(B\). Minimum degree three therefore gives \(N_G(w)=S\). The two degree-three vertices \(u,w\) have three common neighbors, yielding the required four-cycle.

Otherwise, let \(P\) be the parent bag of \(B\). Since \(B\not\subseteq P\), choose
\[
x\in B\setminus P.
\]
If \(x\in S\), the connectedness axiom implies that \(x\) occurs only in \(B\) and \(L\): it cannot occur above \(B\), and \(L\) is the only child. Since \(S\) is independent, its only possible neighbors are \(w\) and \(u\). This contradicts minimum degree three.

Thus \(B\setminus P=\{w\}\). The vertex \(w\) occurs neither in the parent bag nor in the child bag, so it occurs only in \(B\). Again,
\[
d_G(w)=3,\qquad N_G(w)=S.
\]
Together with \(u\), this gives the second configuration. All cases are covered. \(\square\)

## 3. Proof of the theorem

Proceed by induction on \(|V(G)|\). The empty graph is immediate.

Treewidth does not increase under vertex deletion or edge contraction. For contraction, one can replace the two endpoints by a single symbol in every bag; their occurrence subtrees intersect because an edge bag contains both endpoints.

* If \(G\) has a vertex of degree at most one, delete it and apply induction.
* If \(G\) has a degree-two vertex \(v\) with nonadjacent neighbors, suppress \(v\). This is an edge contraction, so the resulting graph still has treewidth at most three. Both parameters are unchanged.
* If a degree-two vertex has adjacent neighbors, use the triangle configuration and delete its two neighbors.
* Otherwise, \(G\) has minimum degree at least three. The lemma supplies either the triangle configuration or the four-cycle configuration.

In either of the last two cases, let \(A\) be the designated pair of vertices. The graph \(G-A\) still has treewidth at most three, so induction and (2) give
\[
\begin{aligned}
\tau(G)
&\le 2+\tau(G-A)\\
&\le 2+2\nu(G-A)\\
&\le 2\nu(G).
\end{aligned}
\]
This completes the proof. \(\square\)

### Constructive certificates

The same induction constructs \(X\) and \(\mathcal P\), without computing either optimum.

* When a triangle or four-cycle is reserved, add its designated pair \(A\) to the feedback vertex set and add the reserved cycle to the packing.
* The recursive packing avoids all vertices of the reserved cycle, by (1).
* When undoing a suppression, replace the suppressed edge by its original two-edge path in the packed cycle, if that edge is used. The feedback vertex set needs no enlargement.
* Removing or restoring a vertex of degree at most one changes neither certificate.

Thus each new packed cycle pays for at most two feedback vertices:
\[
|X|\le2|\mathcal P|.
\]
All decomposition modifications and configuration searches can be performed in polynomial time when a width-three decomposition is supplied.

## 4. Scope and sharpness

This proves Jones’ inequality for every **planar partial \(3\)-tree**, and in fact for every partial \(3\)-tree, planar or not.

For example, it covers planar \(3\)-trees—stacked triangulations—and all their subgraphs. Their width-three decompositions are obtained by starting with a bag for \(K_4\) and, for each inserted vertex, attaching a bag containing that vertex and its three earlier neighbors. This class permits arbitrarily large maximum degree.

The factor two is sharp within the class, as shown by \(K_4\), or by disjoint unions of copies of \(K_4\).

The treewidth threshold is also sharp **without planarity**: \(K_5\) has treewidth four and
\[
\tau(K_5)=3>2=2\nu(K_5).
\]
Of course, \(K_5\) is not a counterexample to the planar conjecture.

## 5. Restrictions on a smallest planar counterexample

The reductions also give some necessary conditions for a counterexample.

Suppose \(G\) is a planar counterexample of minimum order, and put \(k=\nu(G)\). For every nonempty set \(S\) with \(|S|\le2\),
\[
\nu(G-S)=k.
\tag{4}
\]
Otherwise, minimality would give
\[
\tau(G)
\le |S|+\tau(G-S)
\le 2+2(k-1)
=2k,
\]
a contradiction.

For any vertex \(v\), minimality and (4) imply
\[
\tau(G)\le1+\tau(G-v)\le2k+1.
\]
Since \(G\) violates the conjectured bound, integrality then yields
\[
\tau(G)=2k+1,\qquad
\tau(G-v)=2k\quad\text{for every }v.
\tag{5}
\]

Furthermore:

* \(G\) has minimum degree at least three. Vertices of degree at most one can be deleted; degree-two vertices can be suppressed or handled by the triangle reduction.
* No degree-three vertex lies on a triangle.
* No four-cycle has two opposite degree-three vertices.

The last two assertions follow directly from (4) and the cycle-reservation reduction. The structural lemma consequently forces
\[
\operatorname{tw}(G)\ge4.
\]

## 6. The remaining gap

Planarity does **not** force either configuration in the structural lemma. The planar octahedral graph, for instance, has minimum degree four and hence has neither configuration.

The proof therefore stops at a genuine boundary: width-three decompositions force the local configurations needed for a two-vertex reduction, whereas arbitrary planar graphs need not have such decompositions or configurations.

Thus this is a complete proof of the treewidth-three special case, but it supplies neither a proof nor a counterexample for unrestricted planar graphs.