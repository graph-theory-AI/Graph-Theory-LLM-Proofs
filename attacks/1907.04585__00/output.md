```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but for every fixed subcubic forest H, MWIS has an exact 2^{O_H(beta)} n^{O_H(1)} algorithm where beta is the vertex-cover number of the graph induced by vertices of degree at least three.",
  "would_publish": false,
  "caveats": "The parameter beta can be linear, so unrestricted cubic and dense instances remain uncovered; novelty of this elementary parameterized observation was not literature-checked."
}
```

## 1. Statement and outcome

For a fixed graph \(H\), let \(\mathcal C_H\) denote the class of graphs containing no induced subgraph isomorphic to a subdivision of \(H\).

The full conjecture is not proved here. I establish the following parameterized special case, valid for forests \(H\) with arbitrarily many degree-three vertices.

For a graph \(G\), define
\[
B(G):=\{v\in V(G):d_G(v)\ge 3\},
\qquad
\beta(G):=\tau(G[B(G)]),
\]
where \(\tau\) denotes minimum vertex-cover number.

### Partial theorem

For every fixed forest \(H\) with \(\Delta(H)\le 3\), there is a deterministic exact algorithm for MWIS on \(\mathcal C_H\) with running time
\[
2^{O_H(\beta(G))}\, |V(G)|^{O_H(1)}.
\]

Consequently:

1. if \(\beta(G)=O(1)\), MWIS is polynomial-time solvable;
2. if \(\beta(G)\le (\log n)^{O(1)}\), MWIS is exactly solvable in quasi-polynomial time, and hence both conclusions of the conjecture hold on this subclass;
3. if \(\beta(G)=o(n)\), MWIS is exactly solvable in \(2^{o(n)}\) time;
4. in particular, for every fixed \(H\), MWIS is polynomial-time solvable on graphs in \(\mathcal C_H\) whose vertices of degree at least three form an independent set.

The fourth case includes proper subdivisions of arbitrary graphs.

## 2. Two standard facts

We use two established graph-minor facts.

### Fact 2.1: Subcubic minors are topological minors

If \(\Delta(F)\le 3\) and \(F\) is a minor of \(J\), then \(J\) has a subgraph that is a subdivision of \(F\).

Indeed, take a minor model \((M_v:v\in V(F))\). For every edge incident with \(v\), mark the corresponding attachment vertex in \(M_v\). There are at most three marked vertices. Inside \(M_v\), choose a minimal tree connecting them. Such a tree consists of internally disjoint paths from at most one branching vertex. Taking these trees together with the chosen inter-branch-set edges gives a subdivision of \(F\).

This is precisely where the hypothesis \(\Delta(H)\le3\) is used.

### Fact 2.2: Excluding a fixed forest minor bounds treewidth

For every fixed forest \(F\), there is a constant \(c_F\) such that
\[
F\not\preceq_{\mathrm m} J
\quad\Longrightarrow\quad
\operatorname{tw}(J)\le c_F.
\]

One way to obtain this is to embed \(F\) as a minor of a sufficiently large square grid and then apply the excluded-grid theorem. The constant is computable and depends only on \(F\).

## 3. The structural lemma

We first assume that \(H\) has no isolated vertices.

### Lemma 3.1

Let \(H\) be a fixed subcubic forest with no isolated vertices. There is a constant \(c_H\) such that every \(G\in\mathcal C_H\) satisfies
\[
\operatorname{tw}(G)\le
\max\{2,c_H+\beta(G)\}.
\]

### Proof

Let \(X\) be a minimum vertex cover of \(G[B(G)]\), so \(|X|=\beta(G)\).

#### Step 1: Suppress degree-two paths

Consider a connected component of \(G\) that is not a cycle. Suppress all maximal paths whose internal vertices have degree two. This produces a possibly non-simple multigraph \(K\). Every edge \(e\in E(K)\) corresponds to a path \(P_e\) in \(G\), and the internal vertices of the paths \(P_e\) are pairwise disjoint.

Every vertex of \(K\) has degree \(0\), \(1\), or at least \(3\). Moreover, an edge \(e=uv\) of \(K\) corresponds to a path of length one exactly when \(uv\in E(G)\).

Components of \(G\) in which every vertex has degree two are cycles and have treewidth two; they can be treated separately.

#### Step 2: \(K-X\) cannot contain \(H\) as a minor

Suppose for a contradiction that \(K-X\) contains \(H\) as a minor. By Fact 2.1, \(K-X\) contains a subgraph \(L\) that is a subdivision of \(H\).

Lift \(L\) to \(G\): for every edge \(e\in E(L)\), include all vertices of the corresponding path \(P_e\). Let \(S\) be the union of these lifted paths.

We claim that \(G[S]\) is an induced subdivision of \(H\). It suffices to check that an unused edge of \(K\) cannot produce a chord in \(G[S]\).

Let \(e=uv\in E(K)\setminus E(L)\).

- If \(P_e\) has length at least two, every edge of \(P_e\) has an internal endpoint. No internal vertex of \(P_e\) belongs to \(S\), so \(P_e\) creates no edge inside \(G[S]\).

- Suppose \(P_e\) has length one, so \(uv\in E(G)\). If both \(u\) and \(v\) have degree at least three in \(G\), then \(uv\) is an edge of \(G[B(G)]\). Since \(X\) covers this graph and \(u,v\in V(K-X)\), this is impossible.

  Thus at least one endpoint, say \(u\), has degree one in \(K\). If \(u\in V(L)\), then, because \(H\) has no isolated vertices, \(u\) has positive degree in \(L\). Its unique incident edge in \(K\) must consequently belong to \(L\), contradicting \(e\notin E(L)\).

Thus no unused edge gives a chord. The same argument also rules out edges between distinct components of the lifted copy of \(H\). Therefore \(G[S]\) is an induced subdivision of \(H\), contrary to \(G\in\mathcal C_H\).

It follows that
\[
H\not\preceq_{\mathrm m} K-X.
\]

#### Step 3: Bound treewidth

By Fact 2.2,
\[
\operatorname{tw}(K-X)\le c_H.
\]
Adding \(X\) to every bag of a tree decomposition of \(K-X\) gives
\[
\operatorname{tw}(K)\le c_H+|X|.
\]

Subdividing edges does not raise treewidth above two or the original width. More explicitly, for an edge \(uv\) replaced by
\[
u=x_0,x_1,\ldots,x_r=v,
\]
one may attach to a bag containing \(u,v\) the chain of bags
\[
\{v,x_{i-1},x_i\},\qquad 1\le i<r.
\]
Loops produced by suppression and cycle components admit analogous width-two decompositions. Hence
\[
\operatorname{tw}(G)\le
\max\{2,\operatorname{tw}(K)\}
\le \max\{2,c_H+\beta(G)\}.
\]
This proves the lemma. \(\square\)

## 4. The algorithm when \(H\) has no isolated vertices

A minimum vertex cover \(X\) of \(G[B(G)]\) can be found in
\[
2^{O(\beta(G))}n^{O(1)}
\]
time by the standard bounded-search algorithm: for a chosen edge \(uv\), every vertex cover contains \(u\) or \(v\). Iterating the depth bound from \(0\) upward finds a minimum cover within the stated parameterized time.

Construct the suppressed multigraph \(K\). By the proof of Lemma 3.1, \(K-X\) is \(H\)-minor-free and therefore has treewidth at most the fixed constant \(c_H\). A width-\(c_H\) decomposition can be found in polynomial time for fixed \(c_H\). Add \(X\) to all bags and expand the suppressed paths as in the proof. This gives a decomposition of \(G\) of width at most
\[
\max\{2,c_H+\beta(G)\}.
\]

The standard tree-decomposition dynamic program for MWIS stores, for every bag and every independent subset of that bag, the maximum weight of a compatible partial independent set. Its running time is
\[
2^{O(c_H+\beta(G))}n^{O_H(1)}
=
2^{O_H(\beta(G))}n^{O_H(1)}.
\]

This algorithm is exact and accommodates arbitrary binary-encoded vertex weights.

## 5. Removing isolated vertices from \(H\)

Suppose now that
\[
H=H^\circ\;\dot\cup\; tK_1,
\]
where \(H^\circ\) has no isolated vertices.

If \(H^\circ\) is empty, then \(G\in\mathcal C_H\) implies
\[
\alpha(G)<t,
\]
so MWIS can be solved by enumerating all vertex subsets of size at most \(t-1\).

Assume \(H^\circ\neq\varnothing\). Enumerate every independent \(t\)-set \(Z\subseteq V(G)\), and put
\[
G_Z:=G-N_G[Z].
\]
Then \(G_Z\in\mathcal C_{H^\circ}\). Otherwise an induced subdivision of \(H^\circ\) in \(G_Z\), together with the mutually nonadjacent vertices of \(Z\), would induce a subdivision of \(H^\circ\dot\cup tK_1=H\).

Solve MWIS exactly in every \(G_Z\) using the preceding algorithm, and take the best set of the form
\[
Z\cup I_Z.
\]
Also enumerate independent sets of cardinality less than \(t\).

This recovers an optimum independent set. Indeed, if an optimum \(I\) has at least \(t\) vertices, choose any \(t\)-subset \(Z\subseteq I\). Then
\[
I\setminus Z\subseteq V(G_Z),
\]
so the optimum solution in \(G_Z\) has weight at least \(w(I\setminus Z)\).

Finally, \(\beta\) is monotone under taking induced subgraphs:
\[
J\subseteq_{\mathrm{ind}}G
\quad\Longrightarrow\quad
\beta(J)\le\beta(G),
\]
because every degree-at-least-three vertex of \(J\) already had degree at least three in \(G\). Since \(t\) is fixed with \(H\), the \(O(n^t)\) enumeration only changes the polynomial factor. This proves the stated running time for arbitrary forests \(H\).

## 6. Consequences for the conjecture

For every fixed \(d\), on the subclass satisfying
\[
\beta(G)\le O((\log n)^d),
\]
the exact running time is
\[
2^{O_H((\log n)^d)}n^{O_H(1)}
=
n^{(\log n)^{O_H(1)}}.
\]
Thus an exact quasi-polynomial algorithm exists, which in particular is a QPTAS, and the same running time is \(2^{o(n)}\).

Likewise, if for some fixed \(\delta>0\),
\[
\beta(G)=O(n^{1-\delta}),
\]
the exact running time is
\[
2^{O_H(n^{1-\delta})}n^{O_H(1)}.
\]

The particularly transparent case \(\beta(G)=0\) says that all vertices of degree at least three are pairwise nonadjacent. Then MWIS is polynomial-time solvable for every fixed subcubic forest \(H\), regardless of how many degree-three vertices \(H\) has.

## 7. Remaining gap

The result gives no subexponential bound when \(\beta(G)=\Theta(n)\). In particular, for a typical cubic graph,
\[
B(G)=V(G)
\quad\text{and}\quad
\beta(G)=\tau(G)=\Theta(n).
\]
Thus the unrestricted instances containing many adjacent degree-three vertices remain untouched.

The lifting argument identifies one concrete obstruction: after suppressing degree-two paths, unsubdivided edges between selected branch vertices can become chords of a minor model. Deleting a vertex cover of those edges eliminates the obstruction, but the conjectured exclusion condition alone does not presently give a sublinear such cover. Dense graphs such as complete graphs also show that large \(\beta\) need not correspond to algorithmic hardness, so a complete proof would require an additional dense-case mechanism rather than merely strengthening this treewidth argument.