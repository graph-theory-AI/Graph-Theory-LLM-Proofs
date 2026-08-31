```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "No infinite exceptional family is obtained, but I prove a prime-core reduction, exhibit a broad infinite class with finite saturators, and show that any saturator for P4 plus r isolated vertices has at least |H|+2 vertices.",
  "would_publish": false,
  "caveats": "No graph other than P4 is proved to lack a finite induced-saturated graph, so the main problem remains open."
}
```

# 1. Statement of the partial results

All graphs below are finite and simple. For a pair \(xy\), write \(G\triangle xy\) for the graph obtained by toggling \(xy\).

I obtain the following self-contained results.

### Theorem A: prime-core reduction

Let \(H\) be a prime graph. If a finite \(H\)-induced-saturated graph exists, then one exists that is prime. More precisely, if \(M\) is a nontrivial module of an \(H\)-induced-saturated graph \(G\), then \(G[M]\) is itself \(H\)-induced-saturated.

Moreover, \(P_4\) is the only graph \(H\) on at least four vertices for which every sufficiently large \(H\)-free graph is nonprime. For every \(H\neq P_4\), either arbitrarily long paths or their complements form an infinite family of prime \(H\)-free graphs.

Thus the standard modular-decomposition proof for \(P_4\) cannot by itself produce an infinite exceptional family.

### Theorem B: an infinite positive family

Let \(C=K_{a_1}\dot\cup\cdots\dot\cup K_{a_r}\) be an arbitrary cluster graph, possibly empty. Then
\[
H=P_3\dot\cup C
\]
has a finite \(H\)-induced-saturated graph. The same holds for \(\overline H\).

### Theorem C: the first natural extensions of \(P_4\)

For
\[
H_r=P_4\dot\cup rK_1,\qquad r\geq 1,
\]
every finite \(H_r\)-induced-saturated graph \(G\), if one exists, satisfies
\[
|V(G)|\geq r+6=|V(H_r)|+2.
\]
By complementation, the same lower bound holds for
\[
\overline{H_r}=P_4\vee K_r.
\]

For the first case \(H_1=P_4\dot\cup K_1\), any finite induced-saturated graph would additionally have to be prime, connected and co-connected, twin-free, and of order at least seven.

These statements do not settle whether any \(H_r\) is genuinely exceptional.

---

# 2. Local witnesses

The following elementary observation will be used repeatedly.

## Lemma 2.1

Suppose \(G\) is \(H\)-free and \(G\triangle xy\) contains an induced copy of \(H\) on a set \(S\). Then \(x,y\in S\).

If \(xy\in E(G)\), then \(G[S]\) is obtained from \(H\) by adding one edge corresponding to a nonedge of \(H\). If \(xy\notin E(G)\), then \(G[S]\) is obtained from \(H\) by deleting one edge of \(H\).

### Proof

If \(S\) did not contain both \(x\) and \(y\), then the induced graph on \(S\) would be unchanged by the toggle, contradicting that \(G\) is \(H\)-free. The final assertions follow because \(xy\) is the only adjacency changed. \(\square\)

A useful immediate consequence is that if \(H\) is twin-free, then every \(H\)-induced-saturated graph is twin-free: toggling a pair of twins leaves them twins, whereas any newly created copy of \(H\) would have to contain that twin pair.

---

# 3. Prime forbidden graphs and modular decomposition

Recall that \(M\subseteq V(G)\) is a module if every vertex outside \(M\) is either complete or anticomplete to \(M\). A graph is prime if its only modules are the singletons and the whole vertex set.

## Proposition 3.1

Let \(H\) be prime, and let \(G\) be \(H\)-induced-saturated. If \(M\) is a nontrivial module of \(G\), then \(G[M]\) is \(H\)-induced-saturated.

### Proof

Certainly \(G[M]\) is \(H\)-free.

Take distinct \(x,y\in M\). Toggling \(xy\) in \(G\) creates an induced copy of \(H\) on some set \(S\) containing \(x,y\). The set \(M\) remains a module after toggling \(xy\), since only an adjacency internal to \(M\) changed. Consequently \(M\cap S\) is a module in the induced copy \(H\).

It contains \(x,y\), so \(|M\cap S|\geq2\). Since \(H\) is prime, this forces
\[
M\cap S=S.
\]
Thus \(S\subseteq M\), and the same toggle creates \(H\) entirely inside \(G[M]\). This holds for every pair of vertices in \(M\), proving the assertion. \(\square\)

## Corollary 3.2

If a finite \(H\)-induced-saturated graph exists for prime \(H\), then a minimum-order one is prime.

This recovers the usual obstruction for \(P_4\): every finite \(P_4\)-free graph of order at least two has twins, and toggling a twin pair preserves \(P_4\)-freeness.

There is, however, no analogous universal modular obstruction for any larger \(H\).

## Proposition 3.3

Let \(H\) be a graph on at least four vertices. If \(H\neq P_4\), then there are arbitrarily large prime \(H\)-free graphs.

### Proof

An induced subgraph of a path is a linear forest, i.e. a disjoint union of paths. Conversely, every fixed linear forest occurs as an induced subgraph of all sufficiently long paths.

If \(H\) is not a linear forest, then every path \(P_n\) is \(H\)-free.

Suppose instead that \(H\) is a linear forest. If \(\overline H\) is not a linear forest, then \(\overline{P_n}\) is \(H\)-free: otherwise complementing an induced embedding of \(H\) into \(\overline{P_n}\) would embed \(\overline H\) into \(P_n\).

It remains to identify graphs \(H\) for which both \(H\) and \(\overline H\) are linear forests. If \(h=|V(H)|\geq6\), then
\[
\deg_H(v)\leq2
\quad\text{and}\quad
\deg_H(v)\geq h-3\geq3,
\]
a contradiction. For \(h=5\), every vertex would have degree exactly two, contradicting acyclicity. For \(h=4\), the only possibilities without isolated vertices are \(P_4\) and \(2K_2\), and \(\overline{2K_2}=C_4\) is not a forest. Hence only \(P_4\) remains.

Finally, \(P_n\) is prime for every \(n\geq4\). Indeed, if \(M\) were a nontrivial module, a vertex just outside \(M\) adjacent to \(M\) would have to be adjacent to all of \(M\), forcing \(|M|\leq2\); the two-neighbor case is then distinguished by the next vertex along the path. Modules are preserved under complementation, so \(\overline{P_n}\) is also prime. \(\square\)

This proposition is only a limitation on one proof strategy: prime \(H\)-free graphs need not be induced-saturated.

---

# 4. An infinite family that does have finite saturators

## Proposition 4.1

Let
\[
C=K_{a_1}\dot\cup\cdots\dot\cup K_{a_r}
\]
be a cluster graph. Set
\[
H=P_3\dot\cup C,
\qquad
s=\max\{3,a_1,\ldots,a_r\},
\qquad
G=(r+2)K_s.
\]
Then \(G\) is \(H\)-induced-saturated.

### Proof

Every induced subgraph of \(G\) is a cluster graph, while \(H\) has a noncomplete connected component \(P_3\). Hence \(G\) is \(H\)-free.

Let \(xy\in E(G)\). The vertices \(x,y\) lie in the same \(K_s\). Choose a third vertex \(z\) in that clique. After deleting \(xy\), the vertices
\[
x,z,y
\]
induce a \(P_3\). From \(r\) other clique components of \(G\), choose respectively \(a_1,\ldots,a_r\) vertices. These induce \(C\) and are anticomplete to the displayed \(P_3\). Thus deleting any edge creates \(H\).

Now let \(xy\notin E(G)\). Then \(x\) and \(y\) lie in distinct clique components. Choose \(z\neq x\) in the clique containing \(x\). After adding \(xy\), the vertices
\[
z,x,y
\]
induce a \(P_3\). Exactly \(r\) clique components remain untouched, and they supply the components \(K_{a_1},\ldots,K_{a_r}\). Thus adding any nonedge also creates \(H\). \(\square\)

Complementation exchanges edge additions and edge deletions, so \(\overline G\) is \(\overline H\)-induced-saturated.

---

# 5. The family \(P_4\dot\cup rK_1\)

Let
\[
H_r=P_4\dot\cup rK_1,\qquad h=|V(H_r)|=r+4.
\]
It has exactly three edges.

We first record an order-\((h+1)\) degree constraint.

## Lemma 5.1

Let \(H\) have \(h\) vertices and \(m\) edges, and suppose \(G\) is \(H\)-induced-saturated with \(h+1\) vertices and \(q\) edges.

For every edge \(xy\in E(G)\), there is a vertex \(z\notin\{x,y\}\) satisfying
\[
d_G(z)=q-m-1.
\]
For every nonedge \(xy\notin E(G)\), there is a vertex \(z\notin\{x,y\}\) satisfying
\[
d_G(z)=q-m+1.
\]

### Proof

A witness uses exactly \(h\) vertices, so it omits one vertex \(z\).

For an edge deletion, the induced graph before deletion has \(m+1\) edges. Hence
\[
q-d_G(z)=m+1.
\]
For a nonedge addition, the induced graph before addition has \(m-1\) edges, giving
\[
q-d_G(z)=m-1.
\]
\(\square\)

## Theorem 5.2

There is no \(H_r\)-induced-saturated graph on at most \(r+5\) vertices. Consequently, every such graph, if one exists, has at least \(r+6\) vertices.

### Proof

A graph on fewer than \(h\) vertices cannot create \(H_r\) after a toggle.

Suppose first that \(|V(G)|=h\). If \(G\) has both an edge and a nonedge, edge deletion would give
\[
e(G)-1=3,
\]
while nonedge addition would give
\[
e(G)+1=3,
\]
which is impossible. Complete and empty \(G\) also fail directly.

It remains to rule out
\[
|V(G)|=h+1=r+5.
\]
Write \(q=e(G)\). By Lemma 5.1, every edge has an omitted witness vertex of degree \(q-4\), and every nonedge has an omitted witness vertex of degree \(q-2\). Put
\[
L=\{v:d(v)=q-4\},
\qquad
U=\{v:d(v)=q-2\}.
\]

If \(q>4\), then vertices of \(L\) have positive degree. Consequently \(|L|\geq2\): if \(L=\{\ell\}\), an edge incident with \(\ell\) could not have an omitted \(L\)-vertex.

Unless \(q=r+6\), vertices of \(U\) are nonuniversal, so similarly \(|U|\geq2\). Hence
\[
2q=\sum_v d(v)
   \geq 2(q-4)+2(q-2)=4q-12,
\]
and therefore \(q\leq6\).

The exceptional possibility \(q=r+6\) makes a vertex of \(U\) universal. Together with two vertices of \(L\), the degree sum is at least
\[
(r+4)+(r+4)+2(r+1)=4r+10,
\]
whereas the actual degree sum is \(2r+12\). This is impossible for \(r\geq2\). For \(r=1\), equality would force degree sequence
\[
(5,3,3,1,1,1).
\]
After deleting the universal vertex, the two degree-three vertices would each need residual degree two while all other residual degrees were zero, which is impossible. Thus
\[
q\in\{4,5,6\}.
\]

### Case 1: \(q=6\)

Here \(L\) consists of degree-two vertices and \(U\) of degree-four vertices. The degree-sum inequality is an equality, so there are exactly two vertices of each type and every other vertex is isolated. A degree-four vertex would then have only three possible nonisolated neighbors, a contradiction.

### Case 2: \(q=4\)

For each edge \(e\), the omitted vertex has degree zero. Therefore
\[
G-e\cong P_4\dot\cup (r+1)K_1
\]
for every edge \(e\).

We claim this forces
\[
G\cong C_4\dot\cup (r+1)K_1.
\]
Indeed, the line graph \(L(G)-e\) is \(P_3\) for every vertex \(e\) of the four-vertex graph \(L(G)\). Thus every vertex-deleted subgraph of \(L(G)\) has two edges. Counting shows that every vertex of \(L(G)\) has degree two, so \(L(G)\cong C_4\), and hence the four edges of \(G\) form a \(C_4\).

Now add an edge between two of the \(r+1\) isolated vertices. The resulting graph is
\[
C_4\dot\cup K_2\dot\cup (r-1)K_1,
\]
which is \(P_4\)-free and therefore \(H_r\)-free. This contradicts saturation.

### Case 3: \(q=5\)

Now \(L\) consists of degree-one vertices and \(U\) of degree-three vertices. Both have size at least two. The degree sum is ten, so the only possible degree sequences, apart from isolated vertices, are
\[
(3,3,2,1,1)
\quad\text{or}\quad
(3,3,1,1,1,1).
\]

For every edge \(e\), choose the omitted degree-one vertex \(z\), and let \(f\) be its unique incident edge. Since \(z\) is not an endpoint of \(e\),
\[
E(G)\setminus\{e,f\}
\]
must be exactly the three-edge set of a \(P_4\).

In the first degree sequence there are exactly two degree-one vertices. Apply the preceding condition with \(e\) equal to one of their pendant edges. The other pendant edge must be \(f\), but after deleting both pendant edges only the three vertices of degrees \(3,3,2\) can remain nonisolated. Three edges on only three nonisolated vertices cannot form \(P_4\).

In the second degree sequence, the graph is forced to be the balanced double star: the two degree-three vertices are adjacent and each has two leaf neighbors. Taking their central edge as \(e\), deleting \(e\) and any pendant edge leaves a \(P_3\) and a disjoint \(K_2\), not a \(P_4\). This is again a contradiction.

All cases are excluded. \(\square\)

---

# 6. Further structure in the first case \(P_4\dot\cup K_1\)

Let
\[
H_1=P_4\dot\cup K_1.
\]

## Proposition 6.1

If a finite \(H_1\)-induced-saturated graph \(G\) exists, then:

1. \(G\) is twin-free;
2. \(G\) contains an induced \(P_4\);
3. \(G\) is connected and co-connected;
4. \(G\) is prime;
5. every nonedge of \(G\) has a common nonneighbor.

### Proof

The graph \(H_1\) is twin-free, so \(G\) is twin-free.

If \(G\) were \(P_4\)-free, then, being a finite cograph, it would have twins. Thus \(G\) contains a \(P_4\). If \(G\) were disconnected, any vertex outside the component containing this \(P_4\) would be isolated from it, producing \(H_1\). Hence \(G\) is connected.

Suppose \(\overline G\) is disconnected, so \(G=A\vee B\) for nonempty \(A,B\). Delete a cross-edge \(ab\). If a new \(H_1\) occurred, its five vertices would meet the two sides in sizes \(p\) and \(5-p\). All cross-edges except \(ab\) would be present. For \(p=2,3\), this already gives at least five edges, while \(H_1\) has only three. For \(p=1,4\), the singleton-side vertex would have degree three in the induced graph, while \(\Delta(H_1)=2\). Thus deleting \(ab\) remains \(H_1\)-free, a contradiction. Hence \(G\) is co-connected.

Now let \(M\) be a proper nontrivial module. If some vertex outside \(M\) is anticomplete to \(M\), then \(G[M]\) must be \(P_4\)-free, or that outside vertex together with a \(P_4\) in \(M\) would induce \(H_1\). Therefore \(G[M]\) has twins. Since \(M\) is a module, these are also twins in \(G\), a contradiction. Thus every vertex outside \(M\) is complete to \(M\), contradicting co-connectedness. Hence \(G\) is prime.

Finally, if \(xy\) is a nonedge, adding \(xy\) creates \(H_1\). The added edge lies in the \(P_4\)-component of the new copy, so its isolated vertex is a common nonneighbor of \(x\) and \(y\). \(\square\)

Equivalently, every edge of \(\overline G\) lies in a triangle. Also, \(H_1\)-freeness says that for every \(v\),
\[
G[\{x\neq v:xv\notin E(G)\}]
\]
is \(P_4\)-free.

---

# 7. Gap

The argument does **not** show that any \(H_r=P_4\dot\cup rK_1\) lacks a finite induced-saturated graph. It only rules out orders up to \(|H_r|+1\), and for \(r=1\) reduces any further search to prime, connected, co-connected, twin-free graphs on at least seven vertices.

The prime-core result also shows why the usual proof for \(P_4\) does not automatically extend: for every other \(H\) there are arbitrarily large prime \(H\)-free graphs. A genuinely new obstruction, beyond finite modular descent, appears necessary to resolve the catalog problem.