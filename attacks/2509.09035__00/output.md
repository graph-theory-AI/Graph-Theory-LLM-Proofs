```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds uniformly for paths and cycles, and qualitatively for the claw on connected locally finite graphs, but the general tree and planar cases remain open.",
  "would_publish": false,
  "caveats": "No general tree or planar proof or counterexample is obtained; the one-ended claw argument is non-uniform, and novelty of these elementary special cases was not literature-checked."
}
```

# 1. Statement and conventions

I use the following standard quantitative formulation. For a finite graph \(H\) and \(c>0\), ask whether every connected graph \(G\) with no \(c\)-fat \(H\)-minor is quasi-isometric to an \(H\)-minor-free graph, with quasi-isometry constants depending only on \(H\) and \(c\).

To avoid relying on the weakest possible definition of fatness, the arguments below work with the following relatively strict convention. A \(c\)-fat \(H\)-model consists of connected branch sets \(B_v\), \(v\in V(H)\), and connecting paths \(P_e\), \(e\in E(H)\), such that:

1. distinct branch sets are at distance at least \(c\);
2. the portions of distinct edge paths outside their incident branch sets are at distance at least \(c\);
3. a branch set and a nonincident edge path are at distance at least \(c\).

All paths are otherwise internally disjoint from the branch sets. If the source uses the weaker convention in which edge paths corresponding to incident edges need not be separated, the proofs remain valid. Integer-rounding and endpoint conventions are absorbed by setting
\[
s:=\lceil c\rceil+2.
\]

The broad conjecture is not resolved. I prove the following special cases.

---

## Theorem A: connected patterns of maximum degree at most two

Let \(c>0\).

1. For every \(n\ge 2\), every graph with no \(c\)-fat \(P_n\)-minor is uniformly quasi-isometric to a point, hence to a \(P_n\)-minor-free graph.
2. For every \(n\ge 3\), every graph with no \(c\)-fat \(C_n\)-minor is uniformly quasi-isometric to a tree, hence to a \(C_n\)-minor-free graph.

Thus the conjecture holds, quantitatively, whenever \(H\) is a path or a cycle.

---

## Theorem B: the claw in the locally finite case

Let \(G\) be connected and locally finite. If \(G\) has no \(c\)-fat \(K_{1,3}\)-minor, then \(G\) is quasi-isometric to one of:

- a point;
- a ray;
- a double ray.

Consequently \(G\) is quasi-isometric to a \(K_{1,3}\)-minor-free graph.

This is qualitative: in the one-ended case, the proof does not bound the quasi-isometry constants solely in terms of \(c\). In the two-ended case it does.

# 2. Paths

Let \(n\ge2\). Suppose \(G\) contains a geodesic of length at least \(10ns\). Along it place, in order,
\[
B_1,E_1,B_2,E_2,\ldots,E_{n-1},B_n,
\]
where every branch block \(B_i\) and every intervening edge corridor \(E_i\) has length at least \(3s\). The \(B_i\) are the branch sets of the vertices of \(P_n\), and the \(E_i\) are the edge paths.

Because the ambient path is geodesic, the distance in \(G\) between any two of its subpaths is their separation along the path. Therefore:

- distinct branch sets are at distance at least \(3s\);
- distinct edge corridors are separated by an intervening branch block of length at least \(3s\);
- every branch set is at distance at least \(3s\) from every nonincident edge corridor.

This is a \(c\)-fat \(P_n\)-model. Hence, if \(G\) has no such model,
\[
\operatorname{diam}(G)<10ns.
\]

The constant map \(G\to K_1\) is then a \((1,10ns)\)-quasi-isometry. Since \(K_1\) has no \(P_n\)-minor, this proves Theorem A(1). The case \(P_1\) is vacuous apart from the empty graph.

# 3. A bottleneck lemma

The cycle case uses the following elementary form of the bottleneck characterization of quasi-trees.

## Lemma 3.1

Let \(X\) be a connected graph. Suppose there is \(\delta\ge0\) such that, for every \(x,y\in V(X)\), every \(x\)-\(y\) path meets the \(\delta\)-ball about a midpoint of any geodesic from \(x\) to \(y\). Then \(X\) is quasi-isometric to a tree, with constants depending only on \(\delta\).

### Proof

Fix \(o\in V(X)\), and choose an integer
\[
R>10\delta+10.
\]
For \(k\ge1\), let
\[
X_k:=X[\{v:d(o,v)\ge kR\}],
\]
and let the level-\(k\) vertices of an auxiliary graph \(T\) be the components of \(X_k\). Every such component meets the annulus
\[
A_k:=\{v:kR\le d(o,v)<(k+1)R\},
\]
because a geodesic from any of its vertices to \(o\) meets this annulus while remaining in \(X_k\) after its first contact with level \(kR\).

Add a root at level zero. A component of \(X_k\) has as parent the unique component of \(X_{k-1}\) containing it. Thus every nonroot vertex has a unique parent, and \(T\) is a tree.

Define
\[
f(v)=
\begin{cases}
\text{root},&d(o,v)<R,\\
\text{the component of }X_k\text{ containing }v,
 &kR\le d(o,v)<(k+1)R.
\end{cases}
\]

We first bound the fibers. Let \(x,y\) belong to the same level-\(k\) fiber. They are connected by a path \(Q\) contained in \(X_k\), so every vertex of \(Q\) has distance at least \(kR\) from \(o\). Let \(m\) be a midpoint of a geodesic \([x,y]\). By the bottleneck hypothesis, \(Q\) meets \(B(m,\delta)\), whence
\[
d(o,m)\ge kR-\delta.
\]
The path from \(x\) to \(y\) obtained by going from \(x\) to \(o\) and then to \(y\) also meets \(B(m,\delta)\). Thus some point \(p\in[o,x]\cup[o,y]\) satisfies \(d(p,m)\le\delta\). Suppose \(p\in[o,x]\). Then
\[
d(o,p)\ge kR-2\delta,
\]
while \(d(o,x)<(k+1)R\). Hence
\[
d(x,p)<R+2\delta
\]
and
\[
d(x,m)<R+3\delta.
\]
Since \(m\) is a midpoint,
\[
d(x,y)\le 2R+6\delta+3=:D.
\]
The root fiber has diameter at most \(2R\), so all fibers have diameter at most \(D\).

If \(x,y\) are adjacent in \(X\), then \(f(x)=f(y)\) or their images are adjacent parent and child vertices of \(T\). Hence
\[
d_T(f(x),f(y))\le d_X(x,y).
\]

Conversely, fibers corresponding to a parent-child pair in \(T\) are at distance at most \(2R\): follow a geodesic toward \(o\) across the appropriate annulus. Along a path of length \(q\) in \(T\), one can therefore connect representatives of successive fibers at cost at most \(2R\), paying at most \(D\) inside each fiber. Thus
\[
d_X(x,y)\le (D+2R)d_T(f(x),f(y))+D.
\]
The map \(f\) is onto \(T\), and these inequalities prove that it is a quasi-isometry. ∎

# 4. Cycles

The key point is that a path avoiding a large ball around the midpoint of a geodesic produces a fat cycle of any prescribed finite length.

## Lemma 4.1

For every \(n\ge3\) and \(c>0\), there is
\[
\Delta=\Delta(n,c)
\]
with the following property. Let \(P\) be a geodesic from \(x\) to \(y\), let \(m\) be a midpoint of \(P\), and suppose there is an \(x\)-\(y\) path \(Q\) avoiding \(B(m,\Delta)\). Then \(G\) contains a \(c\)-fat \(C_n\)-minor.

### Proof

Take
\[
s=\lceil c\rceil+2,\qquad \Delta=100ns.
\]
If \(d(x,y)<2\Delta\), one endpoint belongs to \(B(m,\Delta)\), so no \(x\)-\(y\) path avoids that ball. Thus suppose both endpoints lie outside it.

List the intersections of \(Q\) with \(P\) in their order along \(Q\). They all lie on one of the two sides of \(B(m,\Delta)\) in \(P\). Since \(Q\) starts on the \(x\)-side and ends on the \(y\)-side, there are consecutive intersections \(a,b\) lying on opposite sides. Let \(Q_0\) be the corresponding subpath of \(Q\), simplified if necessary. Then:

- \(Q_0\) is internally disjoint from \(P\);
- \(d(m,Q_0)\ge\Delta\);
- \(a,m,b\) occur in this order on \(P\);
- \(d_P(a,m),d_P(m,b)\ge\Delta\).

Let
\[
I:=\{z\in P:d_P(z,m)\le 10ns\}.
\]
For \(z\in I\) and \(q\in Q_0\),
\[
d(z,q)\ge d(m,q)-d(m,z)\ge 90ns.
\]
Thus \(I\) is very far from \(Q_0\).

Along \(P[a,b]\), place the objects
\[
B_0,E_0,B_1,E_1,\ldots,B_{n-2},E_{n-2},B_{n-1}
\]
in this order, where:

- all edge corridors \(E_i\) have length at least \(3s\);
- all internal branch blocks \(B_1,\ldots,B_{n-2}\) have length at least \(3s\);
- all the \(E_i\) and all internal \(B_i\) lie inside \(I\);
- \(B_0\) contains the entire subpath from \(a\) to the left end of this alternating arrangement;
- \(B_{n-1}\) contains the corresponding subpath from the right end of the arrangement to \(b\).

There is ample room, since the finite alternating arrangement requires less than \(6ns\) length.

Use \(B_0,\ldots,B_{n-1}\) as the branch sets of \(C_n\), use \(E_0,\ldots,E_{n-2}\) as \(n-1\) consecutive edge paths, and use \(Q_0\) as the final edge path joining \(B_{n-1}\) to \(B_0\).

All separation conditions hold:

- Along \(P\), geodesicity converts the \(3s\) buffers into ambient separation.
- Distinct \(P\)-edge corridors are separated by internal branch blocks.
- \(Q_0\) is at distance at least \(90ns\) from every \(P\)-edge corridor and every internal branch set.
- \(Q_0\) may approach \(B_0\) and \(B_{n-1}\), but these are precisely its incident branch sets.

Thus this is a \(c\)-fat \(C_n\)-model. ∎

## Corollary 4.2

If \(G\) has no \(c\)-fat \(C_n\)-minor, then \(G\) satisfies the bottleneck hypothesis of Lemma 3.1 with \(\delta=\Delta(n,c)\).

Indeed, otherwise an avoiding path would give the model from Lemma 4.1.

Applying Lemma 3.1, \(G\) is uniformly quasi-isometric to a tree. Every minor of a tree is a forest, so the target tree has no \(C_n\)-minor. This proves Theorem A(2).

# 5. The claw in locally finite graphs

Here the relevant obstruction is a coarse geodesic tripod.

## Lemma 5.1: geodesic tube lemma

Let \(s=\lceil c\rceil+2\) and \(L=10s\). Let \(P\) be a geodesic path, ray, or double ray in \(G\). Suppose \(x\in V(G)\), \(p\in P\) is a nearest point to \(x\), and:

- \(d(x,P)\ge L\);
- \(P\) extends at least \(L\) in both directions from \(p\).

Then \(G\) contains a \(c\)-fat \(K_{1,3}\)-minor.

### Proof

Let \(Q\) be a shortest path from \(p\) to \(x\). For a point \(z\in Q\) at distance \(t\) from \(p\),
\[
d(z,P)=t.
\]
Otherwise a shorter path from \(z\) to \(P\) would combine with the \(x\)-\(z\) subpath of \(Q\) to contradict the choice of \(p\).

Choose points \(a,b\in P\) at distance \(L\) from \(p\) in opposite directions, and choose \(q\in Q\) at distance \(L\) from \(p\).

Let the central branch set consist of the first \(3s\) units of each of the three arms \(pa,pb,pq\). Use the remaining portions of the arms as the three edge paths, with leaf branch sets \(\{a\},\{b\},\{q\}\).

The left and right edge paths are separated by at least \(6s\). Every point of the \(Q\)-edge path lies at distance at least \(3s\) from \(P\), so it is separated from both \(P\)-edge paths.

For \(z\in Q\) with \(d(p,z)=t\), geodesicity of \(P\) gives
\[
d(a,z)\ge L-t,
\]
while \(d(a,z)\ge d(z,P)=t\). Hence
\[
d(a,z)\ge\max\{t,L-t\}\ge L/2=5s.
\]
The same holds for \(b\). This verifies the remaining nonincidence conditions. The resulting claw model is \(c\)-fat. ∎

In particular, if \(P\) is a geodesic double ray in a \(c\)-fat-claw-free graph, then every vertex lies at distance less than \(L\) from \(P\).

## Lemma 5.2: ends

If a connected locally finite graph has at least three ends, then it contains a \(c\)-fat \(K_{1,3}\)-minor for every \(c\).

### Proof

Choose a finite connected set \(S\) such that \(G-S\) has three infinite components \(C_1,C_2,C_3\). In each \(C_i\), choose a geodesic from \(S\) to a point at distance at least \(10s\) from \(S\).

Enlarge the central branch set by the first \(3s\) portions of these three geodesics. Use the next portions as edge paths and their distant endpoints as leaf branch sets. Different edge paths lie in different components of \(G-S\), and their first points outside the central branch set are at distance at least \(3s\) from \(S\). Thus different paths and nonincident leaf-path pairs are separated by more than \(c\). ∎

Hence a locally finite \(c\)-fat-claw-free graph has at most two ends.

## Theorem 5.3

Every connected locally finite \(c\)-fat-\(K_{1,3}\)-minor-free graph is quasi-isometric to a point, a ray, or a double ray.

### Proof

There are three cases.

### Finite \(G\)

Every finite connected graph is quasi-isometric to a point. This is only a qualitative statement, since the additive constant may depend on \(G\).

### Two-ended \(G\)

A connected locally finite two-ended graph contains a geodesic double ray. One way to see this is to take vertices tending to the two ends, choose geodesics between them through a fixed finite separator, and pass to a diagonal subsequential limit using local finiteness.

Let \(P\) be such a double ray. Lemma 5.1 shows that every vertex lies within \(L\) of \(P\). Since \(P\) is isometrically embedded, its inclusion into \(G\) is a \((1,L)\)-quasi-isometry. Thus this case is uniform in \(c\).

### One-ended \(G\)

Choose a geodesic ray
\[
P=p_0p_1p_2\cdots,
\]
which exists by local finiteness and König's lemma.

Let
\[
U:=\{x:d(x,P)>L\}.
\]
For every \(x\in U\), every nearest point \(p_i\in P\) has \(i<L\). Otherwise \(P\) would extend at least \(L\) in both directions from \(p_i\), and Lemma 5.1 would give a fat claw.

Suppose \(xy\) is an edge with \(x\in U\) and \(y\notin U\). Let \(p_i\) be nearest to \(x\) and \(p_j\) nearest to \(y\). Then
\[
i<L,\qquad d(x,p_i)\le L+1,\qquad d(y,p_j)\le L.
\]
Since \(P\) is geodesic,
\[
|i-j|=d(p_i,p_j)
 \le d(p_i,x)+1+d(y,p_j)
 \le 2L+2.
\]
Therefore \(j<3L+2\). Thus every edge leaving \(U\) enters the finite set
\[
B:=N_L(P[0,3L+2]).
\]

Every component of \(U\) is consequently a component of \(G-B\), apart from its attachment to \(B\). The tail of \(P\) lies in an infinite component of \(G-B\). Since \(G\) is one-ended, no component of \(U\) can be infinite. Since \(B\) is finite and \(G\) is locally finite, only finitely many components of \(U\) attach to \(B\). Hence \(U\) itself is finite.

It follows that
\[
\sup_{x\in V(G)}d(x,P)<\infty.
\]
Thus the inclusion \(P\hookrightarrow G\) is a quasi-isometry. The coarse-surjectivity constant obtained here can depend on the finite exceptional set \(U\), so this part is not uniform in \(c\). ∎

A point, ray, and double ray are all \(K_{1,3}\)-minor-free, completing the locally finite qualitative claw case.

# 6. What remains unresolved

The arguments above do not settle the catalog problem.

1. **General trees.**  
   Paths are covered, and the claw is covered qualitatively under local finiteness, but the method does not handle trees with several branching vertices or even give a uniform theorem for all locally finite claw-free-at-scale graphs.

2. **General planar graphs.**  
   The detour argument produces fat subdivisions of a cycle, not arbitrary planar patterns. In particular, exclusion of a fat planar graph \(H\) larger than a cycle does not imply exclusion of a fat cycle.

3. **Non-locally-finite claw case.**  
   Local finiteness is used to obtain geodesic rays or lines by compactness and to ensure that a finite separator has only finitely many attached components. A replacement for these steps in arbitrary graphs is not supplied.

4. **Uniformity for the one-ended claw case.**  
   The proof shows that the graph is quasi-isometric to a ray, but its coarse-surjectivity constant may depend on the particular graph. If Conjecture 1.2 is interpreted in a fully uniform fixed-\((H,c)\) sense, this is insufficient.

No counterexample to the tree or planar cases emerges from these arguments.