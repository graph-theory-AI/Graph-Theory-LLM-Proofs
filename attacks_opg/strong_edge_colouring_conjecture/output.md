```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds, even for strong list edge-colouring, for every independent-set blow-up of a pseudoforest.",
  "would_publish": false,
  "caveats": "This is a special-case result only; no novelty claim or improved bound for arbitrary graphs is made."
}
```

## 1. A sharp special-case theorem

Write
\[
B(\Delta)=\Delta^2+\left\lfloor\frac{\Delta}{2}\right\rfloor^2.
\]
This is precisely the conjectured bound, including its odd-degree correction.

A **pseudoforest** is a graph in which every connected component contains at most one cycle. An **independent-set blow-up** of a graph \(H\) is obtained by replacing each vertex \(v\) with a nonempty independent set \(A_v\), and replacing each edge \(uv\) with all edges between \(A_u\) and \(A_v\). No other edges are added.

The underlying pseudoforest and the part sizes below may be arbitrary.

**Theorem.** Let \(G\) be an independent-set blow-up of a finite simple pseudoforest, and let \(\Delta=\Delta(G)\ge 1\). Then
\[
L(G)^2\text{ is }(B(\Delta)-1)\text{-degenerate}.
\]
Consequently,
\[
s\chi'(G)\le B(\Delta).
\]
In fact, a strong edge-colouring exists whenever each edge is assigned its own list of at least \(B(\Delta)\) permissible colours.

If the underlying graph is a forest, the stronger bound \(\Delta^2\) holds, also for lists.

The theorem is sharp for every \(\Delta\). I give a self-contained proof; I do not claim this special-case result is new.

## 2. Conflict graphs and edge bundles

The **conflict graph** of \(G\) is
\[
J=L(G)^2.
\]
Its vertices are the edges of \(G\); two distinct vertices are adjacent when the corresponding edges share an endpoint or have adjacent endpoints. Thus strong edge-colouring is exactly proper vertex-colouring of \(J\).

Put
\[
a_v=|A_v|,
\qquad
d_v=\sum_{w\in N_H(v)}a_w.
\]
Every vertex of \(A_v\) has degree \(d_v\), so \(d_v\le\Delta\).

For \(uv\in E(H)\), let \(E_{uv}\) denote the **bundle** consisting of all \(a_ua_v\) edges between \(A_u\) and \(A_v\). Each bundle is a clique in \(J\). Moreover, the conflict relation between two bundles is uniform: either every edge of one conflicts with every edge of the other, or no such pair conflicts. The former occurs exactly when the corresponding edges of \(H\) have distance at most two in \(L(H)\).

We will delete vertices of the fixed conflict graph \(J\), bundle by bundle. At every deletion, the selected vertex will have at most \(B(\Delta)-1\) remaining neighbours. Reverse greedy colouring then proves the theorem, including its list version.

Importantly, deleting a bundle does **not** erase conflicts between other bundles that were mediated by it.

## 3. Removing leaf classes costs at most \(\Delta^2\)

Suppose that \(u\) is a leaf of the current underlying graph, with neighbour \(v\). Consider an edge \(e\in E_{uv}\).

Every edge in the closed conflict neighbourhood of \(e\) belongs either to a bundle incident with \(v\), or to a bundle incident with some
\[
w\in N_H(v)\setminus\{u\}.
\]
Therefore
\[
\begin{aligned}
|N_J[e]|
&\le
a_vd_v+
\sum_{w\in N_H(v)\setminus\{u\}}
a_w(d_w-a_v)\\
&\le
a_v\Delta+(\Delta-a_v)(d_v-a_u)\\
&\le \Delta^2.
\end{aligned}
\tag{1}
\]
Here the first expression may count an edge more than once, which is harmless. Also \(a_v=d_u\le\Delta\), so the coefficient \(\Delta-a_v\) is nonnegative.

Thus every edge of this leaf bundle has at most \(\Delta^2-1\) remaining conflicts. We may delete the entire bundle in any order, and then remove the now-isolated class \(A_u\).

After removing \(A_u\), conflicts among retained edges are exactly those in the induced graph \(G-A_u\): whether two retained edges conflict depends only on their endpoints and edges joining those endpoints. Hence we may apply (1) repeatedly, using the original \(\Delta\) throughout.

For a pseudoforest, this stripping process leaves only isolated vertices and cycle components. For a forest it removes every edge, already proving the \(\Delta^2\) assertion.

It remains to handle blow-ups of cycles.

## 4. Cycle blow-ups: a three-phase elimination order

Consider a cycle blow-up with classes
\[
A_0,\ldots,A_{n-1},
\qquad |A_i|=a_i,
\]
where indices are cyclic and
\[
a_{i-1}+a_{i+1}\le\Delta.
\tag{2}
\]
Set
\[
k=\left\lfloor\frac{\Delta}{2}\right\rfloor,
\qquad B=\Delta^2+k^2.
\]

### Short cycles

If \(n=3\) or \(4\), the number \(m\) of edges satisfies
\[
\begin{aligned}
m
&=\frac12\sum_i a_i(a_{i-1}+a_{i+1})\\
&\le \frac{\Delta}{2}\sum_i a_i
\le \frac{n\Delta^2}{4}
\le\Delta^2.
\end{aligned}
\]
The penultimate inequality follows by summing (2). Consequently the conflict graph has at most \(\Delta^2\) vertices, and any elimination order suffices.

Henceforth assume \(n\ge5\).

### The five-bundle neighbourhood

Let \(E_i\) be the bundle between \(A_i\) and \(A_{i+1}\). An edge in \(E_i\) conflicts exactly with the edges in
\[
E_{i-2},E_{i-1},E_i,E_{i+1},E_{i+2}.
\]

For a selected bundle \(E_i\), abbreviate
\[
(r,p,x,y,q,s)
=
(a_{i-2},a_{i-1},a_i,a_{i+1},a_{i+2},a_{i+3}).
\]
For \(n=5\), \(r=s\); all subsequent estimates remain valid. By (2),
\[
r+x\le\Delta,\quad
p+y\le\Delta,\quad
x+q\le\Delta,\quad
y+s\le\Delta.
\tag{3}
\]
Before any deletions, the closed conflict neighbourhood of an edge in this bundle has size
\[
S=rp+px+xy+yq+qs
  =p(r+x)+xy+q(y+s).
\tag{4}
\]

Call a class **large** if its size exceeds \(k\), and **small** otherwise. Delete bundles in the following three phases.

### Phase I: large–large bundles

Suppose \(x,y\ge k+1\). Equations (3)–(4) give
\[
\begin{aligned}
S
&\le \Delta(p+q)+xy\\
&\le \Delta(2\Delta-x-y)+xy\\
&=\Delta^2+(\Delta-x)(\Delta-y)\\
&\le\Delta^2+k^2=B.
\end{aligned}
\tag{5}
\]
Indeed, every nonisolated class has size at most \(\Delta\), and
\[
0\le \Delta-x,\Delta-y\le k.
\]

Thus all large–large bundles can be deleted, in arbitrary order, with closed remaining conflict neighbourhoods of size at most \(B\).

### Phase II: large–small bundles

Orient the selected bundle so that
\[
x\ge k+1,\qquad y\le k.
\]
There are two cases, according to the size \(p\) of the other class adjacent to \(A_i\).

**Case A: \(p\le k\).** Even the original closed conflict neighbourhood satisfies
\[
\begin{aligned}
S
&\le p\Delta+xy+q\Delta\\
&\le k\Delta+xk+(\Delta-x)\Delta\\
&=\Delta^2+k\Delta-x(\Delta-k)\\
&\le \Delta^2+k^2=B,
\end{aligned}
\tag{6}
\]
where the last inequality uses \(x\ge k\).

**Case B: \(p\ge k+1\).** The bundle of size \(px\) was deleted in Phase I. Hence the remaining closed conflict neighbourhood has size at most
\[
rp+xy+yq+qs.
\]
Using (3),
\[
\begin{aligned}
rp+xy+yq+qs
&\le p(\Delta-x)+xy+q\Delta\\
&\le(\Delta-x)(2\Delta-y)+xy\\
&=\Delta^2-(2x-\Delta)(\Delta-y)\\
&\le\Delta^2.
\end{aligned}
\tag{7}
\]
The last inequality holds because \(x\ge k+1\) implies \(2x\ge\Delta\).

Thus all large–small bundles can also be deleted in arbitrary order.

### Phase III: small–small bundles

Every remaining bundle has at most \(k^2\) edges. Each closed conflict neighbourhood meets at most five bundles, so its size is at most
\[
5k^2\le\Delta^2+k^2=B.
\tag{8}
\]

This completes the elimination order for every cycle blow-up.

### Completing the proof

First use the leaf-class deletions from Section 3. Then apply the cycle elimination order independently to each remaining component. Isolated classes have no edges to colour.

At every step the closed remaining conflict neighbourhood has size at most \(B\). Thus each deleted vertex has at most \(B-1\) remaining neighbours, proving that \(J\) is \((B-1)\)-degenerate.

Colouring in reverse order uses at most \(B\) colours. With individual lists of size \(B\), at most \(B-1\) colours are forbidden when an edge is coloured, so the same argument works without modification. ∎

## 5. Sharpness within this class

The standard extremal examples are already cycle blow-ups, so no better universal bound is possible for the class just treated.

Every two edges in a blow-up of \(C_5\) conflict. Its strong chromatic index therefore equals its number of edges.

If \(\Delta=2k\), take all five classes to have size \(k\). Then
\[
s\chi'(G)=5k^2=B(\Delta).
\]

If \(\Delta=2k+1\), where \(k\ge1\), use cyclic class sizes
\[
(k+1,k+1,k,k,k).
\]
The maximum degree is \(2k+1\), and
\[
\begin{aligned}
s\chi'(G)
&=(k+1)^2+2k(k+1)+2k^2\\
&=5k^2+4k+1\\
&=(2k+1)^2+k^2
=B(\Delta).
\end{aligned}
\]
For \(\Delta=1\), a single edge gives equality; the edgeless case is trivial.

## 6. What remains unresolved

This proves the conjecture for blow-ups of arbitrary pseudoforests, not for arbitrary graphs. The leaf-class argument stops when the underlying graph has a non-cyclic, branching \(2\)-core. There, a bundle can conflict with bundles along several branches, and the five-bundle calculation is unavailable.

Moreover, the stronger degeneracy conclusion cannot hold generally. If \(G\) is \(\Delta\)-regular with girth at least five, then every edge has
\[
2(\Delta-1)+2(\Delta-1)^2
=2\Delta(\Delta-1)
\]
neighbours in \(L(G)^2\). The girth condition prevents collisions in this count. Thus \(L(G)^2\) is regular of that degree, and its degeneracy is
\[
2\Delta(\Delta-1)>B(\Delta)-1
\qquad(\Delta\ge3).
\]
Such graphs include, for example, the cubic Petersen graph.

This is not a counterexample to the colouring conjecture: chromatic number can be much smaller than degeneracy. It shows precisely why the elimination method above, despite being sharp on the stated subclass, cannot by itself settle the general Erdős–Nešetřil conjecture.