```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A lexicographic exact-search construction yields a connected computable cubic graph with infinite twin-width, but it gives neither a natural family nor an explicit finitely generated group.",
  "would_publish": false,
  "caveats": "Termination still uses the known probabilistic existence theorem, and no concrete high-twin-width adjacency list or effective Osajda labeling is produced."
}
```

## Statement and scope

The word “explicit” is not formally defined in the question. In the weak recursion-theoretic sense, the known existential result can be effectivized:

> **Partial theorem.** There is a total algorithm which, on input \(k\), outputs a connected finite cubic graph \(F_k\) with
> \[
> \operatorname{tww}(F_k)>k,
> \]
> together with a finite exhaustive certificate of this inequality. Consequently, there is a connected computable infinite cubic graph whose finite induced subgraphs have unbounded twin-width.

This does not resolve the intended question. The construction searches directly on the predicate \(\operatorname{tww}>k\), and its termination uses the existing probabilistic existence theorem. It supplies neither a natural formula for \(F_k\) nor a finitely generated group.

Throughout, I use only the established input stated in the question:

\[
(\mathrm E_D)\qquad
\text{for some fixed }D,\text{ finite graphs of maximum degree }D
\text{ have unbounded twin-width.}
\]

## 1. Exact finite decision procedure

For a partition \(\mathcal P\) of \(V(G)\), color a pair of distinct parts \(A,B\in\mathcal P\) as follows:

- black if \(A\) is complete to \(B\);
- white if \(A\) is anticomplete to \(B\);
- red otherwise.

Let \(\rho_G(\mathcal P)\) be the maximum red degree of a part.

The trigraph obtained after a sequence of contractions depends only on the resulting partition: a pair of bags is red exactly when the original adjacency relation between them is mixed. This follows immediately by induction on the number of contractions. Therefore

\[
\operatorname{tww}(G)\le k
\]

if and only if there is a chain

\[
\mathcal P_0,\mathcal P_1,\ldots,\mathcal P_{n-1}
\]

such that:

1. \(\mathcal P_0\) is the singleton partition;
2. \(\mathcal P_{n-1}=\{V(G)\}\);
3. \(\mathcal P_{i+1}\) is obtained from \(\mathcal P_i\) by merging two parts;
4. \(\rho_G(\mathcal P_i)\le k\) for every \(i\).

This gives an exact dynamic program over the Bell-number many partitions:

1. Mark the singleton partition reachable.
2. Whenever a marked partition \(\mathcal P\) has a two-part merge \(\mathcal Q\) with \(\rho_G(\mathcal Q)\le k\), mark \(\mathcal Q\).
3. Accept if and only if \(\{V(G)\}\) is eventually marked.

Thus finite twin-width is decidable without an oracle.

If the algorithm rejects, it can output the set \(\mathcal R\) of all reachable \(k\)-safe partitions. A verifier checks:

- the singleton partition belongs to \(\mathcal R\);
- every partition in \(\mathcal R\) has red degree at most \(k\);
- every \(k\)-safe merge of a member of \(\mathcal R\) again belongs to \(\mathcal R\);
- the one-part partition does not belong to \(\mathcal R\).

This is a finite, although generally enormous, certificate that \(\operatorname{tww}(G)>k\).

Also,

\[
\operatorname{tww}(G_1\mathbin{\dot\cup}G_2)
 =\max\{\operatorname{tww}(G_1),\operatorname{tww}(G_2)\}.
\]

The upper bound is obtained by contracting the components separately; the lower bound follows by restricting a contraction sequence to an induced component. Hence the existential bounded-degree witnesses may be assumed connected.

## 2. A locality lemma

The following elementary estimate is useful both for reducing the degree and for understanding subdivisions.

For \(q\ge1\), set

\[
\beta_r(q)=q\sum_{j=0}^{r-1}(q-1)^j,
\]

and put \(\beta_r(0)=0\). This bounds the number of other vertices in a radius-\(r\) ball of a graph of maximum degree \(q\).

> **Lemma 1.** Let \(H\) and \(J\) be graphs on the same vertex set. Suppose
> \[
> E(J)\subseteq E(H^r),
> \]
> where \(H^r\) joins vertices at \(H\)-distance at most \(r\). If
> \(\Delta(H)\le \Delta\) and \(\operatorname{tww}(H)\le d\), then
> \[
> \operatorname{tww}(J)\le \beta_r(d+\Delta).
> \]

### Proof

Take a width-\(d\) contraction sequence for \(H\). At any partition \(\mathcal P\), form the support quotient \(Q_{\mathcal P}\), in which two parts are adjacent when at least one \(H\)-edge joins them.

For a fixed part \(A\):

- it has at most \(d\) red neighbors;
- it has at most \(\Delta\) black neighbors.

Indeed, if \(B\) is black-adjacent to \(A\), fix \(a\in A\). Every vertex of \(B\) is adjacent to \(a\), and distinct black-neighboring parts contain distinct neighbors of \(a\). Thus there are at most \(\Delta\) such parts.

Consequently,

\[
\Delta(Q_{\mathcal P})\le d+\Delta.
\]

If \(A,B\) have at least one \(J\)-edge between them, its endpoints are joined by an \(H\)-path of length at most \(r\). The bags met by that path give a walk of length at most \(r\) from \(A\) to \(B\) in \(Q_{\mathcal P}\). Hence every red neighbor of \(A\) in the quotient for \(J\) lies in the radius-\(r\) ball around \(A\) in \(Q_{\mathcal P}\). There are at most \(\beta_r(d+\Delta)\) such bags.

Using the same merge chain for \(J\) proves the assertion. ∎

## 3. Why cubic graphs suffice

Starting from \((\mathrm E_D)\), one can deduce that connected cubic graphs have unbounded twin-width.

Given a graph \(G\) of maximum degree at most \(D\), replace each vertex \(v\), with incident edges ordered as \(e_1,\ldots,e_{\deg(v)}\), by a path

\[
p_{v,1}p_{v,2}\cdots p_{v,\deg(v)}.
\]

For every original edge \(e_i e_j=uv\), join the corresponding ports \(p_{u,i}\) and \(p_{v,j}\). Call the resulting graph \(H(G)\). It has maximum degree at most \(3\).

Choose \(p_{v,1}\) as the representative of \(v\). Representatives of adjacent vertices of \(G\) are at \(H(G)\)-distance at most

\[
L=2D-1.
\]

Let \(J\) be the graph on \(V(H(G))\) whose only nonisolated vertices are the representatives and whose representative subgraph is \(G\). Then

\[
E(J)\subseteq E(H(G)^L).
\]

By Lemma 1,

\[
\operatorname{tww}(G)=\operatorname{tww}(J)
 \le \beta_L\bigl(\operatorname{tww}(H(G))+3\bigr).
\]

Thus, if the subcubic graphs \(H(G)\) had bounded twin-width, then the original degree-\(D\) graphs would also have bounded twin-width, contradicting \((\mathrm E_D)\). Hence finite subcubic graphs have unbounded twin-width.

Finally, every finite subcubic graph is an induced subgraph of a finite cubic graph. For each missing incidence at a vertex \(v\), take a fresh copy of \(K_4\) with one edge subdivided. Its subdivision vertex has degree \(2\); join it to \(v\). Repeating this until \(v\) has degree \(3\) produces a cubic supergraph, and the original subcubic graph remains induced. Therefore connected finite cubic graphs have unbounded twin-width.

## 4. Canonical computable witnesses

Order all finite labeled graphs first by number of vertices and then lexicographically by their upper-triangular adjacency words. Define \(F_k\) to be the first connected cubic graph in this order satisfying

\[
\operatorname{tww}(F_k)>k.
\]

The algorithm is:

1. Enumerate connected cubic graphs in the stated order.
2. Apply the exact partition dynamic program.
3. Stop at the first graph rejected by the test for twin-width at most \(k\).

The preceding section proves termination. Thus \(k\mapsto F_k\) is a total recursive function. The dynamic program can simultaneously output the exhaustive lower-bound certificate described in Section 1.

This is formally explicit in the computability sense, but not in the sense intended by the open problem: the definition refers directly to twin-width and gives no useful size or running-time estimate.

## 5. A connected computable cubic graph of infinite twin-width

A minor additional construction turns the family into one connected cubic graph.

First note that toggling one edge changes twin-width by at most one:

> **Lemma 2.** If \(G\) and \(G'\) differ in exactly one adjacency, then
> \[
> \left|\operatorname{tww}(G)-\operatorname{tww}(G')\right|\le1.
> \]

Indeed, at any partition only the relation between the two bags containing the endpoints can change, so every red degree changes by at most one. Apply the same contraction sequence in both directions.

For each \(k\), choose the canonical graph \(F_{k+1}\) and choose a nonbridge edge \(u_kv_k\). Such an edge exists because every finite connected cubic graph contains a cycle.

Take copies indexed by \(i\in\mathbb Z\), using \(F_{|i|+1}\) in copy \(i\). Delete \(u_iv_i\) from that copy, and add

\[
v_i u_{i+1}
\qquad\text{for every }i\in\mathbb Z.
\]

Call the resulting infinite graph \(X\).

- Each copy with its chosen edge deleted remains connected.
- Every endpoint loses one edge and gains one cross-edge.
- Hence \(X\) is connected and \(3\)-regular.
- The induced subgraph on the vertices of copy \(i\) is
  \(F_{|i|+1}-u_iv_i\).

By Lemma 2,

\[
\operatorname{tww}(F_{|i|+1}-u_iv_i)
 \ge \operatorname{tww}(F_{|i|+1})-1
 > |i|.
\]

Therefore the finite induced subgraphs of \(X\) have unbounded twin-width.

The adjacency relation of \(X\) is recursive: to decide adjacency in copy \(i\), compute the finite graph \(F_{|i|+1}\); cross-edges are prescribed explicitly. Thus \(X\) is a connected computable cubic graph with infinite twin-width in the finite-induced-subgraph sense.

Again, this is a diagonal search construction, not the natural explicit example sought in the literature.

## 6. A direct lower-bound target for future candidates

For a partition \(\mathcal P\), let \(Q_{\mathcal P}\) be its contact quotient: two parts are adjacent if at least one original edge joins them. Define

\[
\kappa_m(G)=
\min_{\substack{\mathcal P\text{ partition of }V(G)\\|\mathcal P|=m}}
\Delta(Q_{\mathcal P}).
\]

If \(\Delta(G)\le D\), each part has at most \(D\) black neighbors, as in Lemma 1. Therefore

\[
\rho_G(\mathcal P)\ge \Delta(Q_{\mathcal P})-D.
\]

Every contraction sequence passes through a partition with exactly \(m\) parts, so

\[
\boxed{\displaystyle
\operatorname{tww}(G)\ge
\max_{1\le m\le |V(G)|}\bigl(\kappa_m(G)-D\bigr).
}
\]

Thus a genuinely direct construction would follow from an explicit bounded-degree family for which \(\kappa_m(G)\) is unbounded at some scale.

Ordinary edge expansion alone does not provide this. If all parts have size at most \(s\), a contacted part can absorb up to \(Ds\) boundary edges. For a part \(A\) of size comparable to \(s\), a lower bound \(e(A,V\setminus A)\ge h|A|\) therefore yields only about \(h/D\) contacted parts. Stronger anti-clustering information, valid for all partitions occurring in a contraction sequence, is needed.

## 7. Why this does not yet produce a group

Lemma 1 also quantifies the subdivision issue. If \(S_r(G)\) is the uniform \(r\)-subdivision of \(G\), then, by putting the edges of \(G\) between its branch vertices and treating all other vertices as isolated,

\[
\operatorname{tww}(G)
 \le \beta_r\!\left(
 \operatorname{tww}(S_r(G))+\max\{\Delta(G),2\}
 \right).
\]

Consequently, uniformly bounded subdivisions preserve unbounded twin-width. More generally, if a bounded-degree Cayley graph \(C\) of twin-width \(d\) contains \(S_{r_i}(G_i)\) as induced subgraphs, then

\[
\operatorname{tww}(G_i)
 \le \beta_{r_i}\bigl(d+\Delta(C)\bigr).
\]

Thus induced embeddings at uniformly bounded scale would solve the group problem. Embeddings using paths of unbounded length do not automatically suffice.

There is also no immediate conversion of the computable cubic graph \(X\) into a Cayley graph. A proper finite edge-coloring of \(X\) turns each color class into an involution and realizes \(X\) as a Schreier graph of an action of a finitely generated free product. But free products of finite groups are hyperbolic and hence have finite twin-width by the source paper. High twin-width of an arbitrary Schreier graph therefore says nothing about the twin-width of the acting group.

Finally, applying Osajda's existential embedding theorem to the computable sequence does not by itself produce a computable group presentation. One would need an effective extension theorem choosing globally compatible labels or relators. Existence of compatible choices at every finite level is not automatically enough: an infinite computable finitely branching tree can have no computable branch. I have not verified the additional effectivity needed in the Osajda construction, so I do not claim a recursively presented infinite-twin-width group.

## Conclusion and remaining gap

The graph side is formally resolved only under the weakest meaning of “explicit”: exact exhaustive search gives a canonical computable cubic family and even a connected computable cubic graph with unbounded twin-width. This is not the intended resolution because:

1. the construction tests the desired conclusion directly;
2. termination rests on the original probabilistic existence theorem;
3. no concrete high-twin-width adjacency list is produced;
4. no natural invariant proves the lower bound;
5. no explicit finitely generated group presentation or effective compatible small-cancellation labeling is obtained.

A genuine resolution would still require either a natural bounded-degree family satisfying a partition-contact lower bound, or a concrete finitely generated group whose Cayley graph contains such witnesses at uniformly bounded scale.