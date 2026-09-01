```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when the high-minimum-degree core has maximum degree O(sqrt(g)), and the canonical bipartite obstruction is ruled out below density 1/2 when one bipartition class is sufficiently small.",
  "would_publish": false,
  "caveats": "The uncontrolled case is a nonempty core with maximum degree much larger than k and no sufficiently small bipartition side."
}
```

## 1. Formulation

For an edge \(uv\), write \(R_{uv}\subseteq [k]\times [k]\) for its set of conflicts, after fixing an ordering of its endpoints. A coloring \(\varphi:V(G)\to[k]\) is valid if
\[
(\varphi(u),\varphi(v))\notin R_{uv}
\qquad\text{for every }uv\in E(G).
\]
Throughout, suppose
\[
|R_{uv}|\le \gamma k
\]
for every edge, where \(\gamma>0\) is the proposed absolute conflict-density constant.

I do not obtain a proof or counterexample to the full conjecture. I give two rigorous partial results and isolate the remaining high-degree regime.

---

## 2. The obstruction at \(\gamma=1/2\)

The restriction \(\gamma<1/2\) is indeed necessary.

### Proposition 2.1

For every even \(k\), there is a planar simple graph with exactly \(k/2\) conflicts on every edge which is not conflict \(k\)-colorable.

### Proof

Let \(A,B\) partition \([k]\), with \(|A|=|B|=k/2\). Take two vertices \(x,y\), and for every \((a,b)\in[k]^2\), add a vertex \(z_{a,b}\) adjacent to both \(x\) and \(y\). The underlying graph is \(K_{2,k^2}\), hence planar.

Assign conflicts
\[
R_{xz_{a,b}}=\{(a,c):c\in A\},
\qquad
R_{yz_{a,b}}=\{(b,c):c\in B\}.
\]
Each relation has \(k/2\) pairs.

If \(\varphi(x)=a\) and \(\varphi(y)=b\), then the vertex \(z_{a,b}\) cannot receive a color in \(A\), because of its edge to \(x\), and cannot receive a color in \(B\), because of its edge to \(y\). Thus it has no available color. ∎

More generally, if \(q\mid k\), the same construction with \(q\) left vertices, \(k^q\) right vertices, and \(q\) blocks of size \(k/q\), gives a noncolorable instance on \(K_{q,k^q}\) with \(k/q\) conflicts per edge. For \(q\ge3\), however, the Euler genus is at least
\[
\frac{(q-2)k^q-2q+4}{2},
\]
by the bipartite Euler inequality. Hence these higher-order examples do not satisfy \(k=\Omega(\sqrt g)\).

---

## 3. A core reduction and a maximum-degree case

The following elementary reduction allows arbitrary high degrees outside a fixed core.

### Proposition 3.1

Let \(d\) be a nonnegative integer satisfying
\[
d\gamma<1.
\]
Starting from \(G\), repeatedly delete a vertex of current degree at most \(d\), and let \(H\) be the remaining \((d+1)\)-core. If \(H\) is empty, or if
\[
e\frac{\gamma}{k}\bigl(2\Delta(H)-1\bigr)\le1,
\tag{3.1}
\]
then \(G\) is conflict \(k\)-colorable.

### Proof

First color \(H\). Choose every vertex color independently and uniformly from \([k]\). For \(uv\in E(H)\), let
\[
E_{uv}=\{(\varphi(u),\varphi(v))\in R_{uv}\}.
\]
Then
\[
\Pr(E_{uv})=\frac{|R_{uv}|}{k^2}\le\frac{\gamma}{k}.
\]
The event \(E_{uv}\) is independent of all edge-events whose edges are disjoint from \(uv\). It is therefore dependent on at most
\[
\deg_H(u)+\deg_H(v)-2\le 2\Delta(H)-2
\]
other events. Condition (3.1) is exactly the standard symmetric Lovász local lemma condition, so \(H\) has a valid coloring.

Now restore the deleted vertices in reverse deletion order. When a deleted vertex \(v\) is restored, at most \(d\) of its neighbors have already been colored. A fixed color at one neighbor forbids at most \(|R_{uv}|\le\gamma k\) colors at \(v\). Hence fewer than
\[
d\gamma k<k
\]
colors are forbidden at \(v\), and the coloring extends. ∎

### Surface corollary

Let \(H\) denote the \(7\)-core of \(G\). Fix \(A>0\). If
\[
\gamma<\frac16,\qquad \Delta(H)\le A\sqrt g,
\]
then \(G\) is conflict \(k\)-colorable whenever
\[
k\ge 2e\gamma A\sqrt g.
\tag{3.2}
\]

Indeed, apply Proposition 3.1 with \(d=6\). For example, one may take
\[
\gamma=\frac1{12},
\qquad
C'=\frac{eA}{6}.
\]
This proves the conjectured conclusion for the class of surface graphs whose \(7\)-core has maximum degree \(O(\sqrt g)\). Degrees outside the core are unrestricted.

For \(g=0\), the \(7\)-core is empty by Euler's formula, so the argument also covers the planar case.

---

## 4. Necessary structure of a counterexample

Proposition 3.1 gives a useful reduction of the unresolved case.

### Proposition 4.1

Suppose \(d\ge6\), \(d\gamma<1\), and \(G\) is vertex-minimal among non-conflict-\(k\)-colorable instances embeddable in Euler genus \(g\). Then

\[
\delta(G)\ge d+1,
\tag{4.1}
\]
\[
|V(G)|\le \frac{6g-12}{d-5}\le \frac{6g}{d-5},
\tag{4.2}
\]
and
\[
\Delta(G)>\frac12\left(1+\frac{k}{e\gamma}\right).
\tag{4.3}
\]

### Proof

If \(v\) had degree at most \(d\), a coloring of \(G-v\), which exists by minimality, would extend to \(v\) because \(d\gamma<1\). This proves (4.1).

Writing \(n=|V(G)|\) and \(m=|E(G)|\), Euler's inequality gives
\[
m\le3n-6+3g.
\]
Together with \(2m\ge(d+1)n\), this yields
\[
(d-5)n\le6g-12,
\]
proving (4.2).

Finally, if (4.3) failed, the local lemma condition (3.1) would hold directly on \(G\), contradicting noncolorability. ∎

Thus, after choosing for example \(d=6\) and \(\gamma<1/6\), every counterexample must have:

- minimum degree at least \(7\);
- at most \(6g\) vertices;
- a vertex of degree \(\Omega(k/\gamma)\).

Under \(k\ge C'\sqrt g\), the core has \(O(k^2)\) vertices, but it may still contain vertices of degree \(\Theta(k^2)\). This is exactly where the elementary edge-event local lemma fails.

---

## 5. A bipartite partial result

The natural attempted counterexamples generalizing \(K_{2,k^2}\) are bipartite graphs with a relatively small “control side.” The following rules out a substantial range of such examples.

### Lemma 5.1: blocking probability

Let \(X_1,\dots,X_s\) be independent uniform elements of \([k]\). For each \(i\), let
\[
R_i\subseteq[k]\times[k],\qquad |R_i|\le\gamma k,
\]
and put
\[
F_i(a)=\{b:(a,b)\in R_i\}.
\]
If \(k>\gamma s\), then
\[
\Pr\left(\bigcup_{i=1}^s F_i(X_i)=[k]\right)
\le
\left(\frac{e\gamma s}{k}\right)^{1/\gamma}.
\tag{5.1}
\]

### Proof

Let
\[
Y_i=|F_i(X_i)|,\qquad Z_i=\frac{Y_i}{\gamma k}.
\]
Then \(0\le Z_i\le1\), and
\[
\mathbb E Z_i
=
\frac{|R_i|}{\gamma k^2}
\le\frac1k.
\]
If the union in (5.1) covers \([k]\), then
\[
\sum_i Y_i\ge k,
\qquad\text{hence}\qquad
\sum_i Z_i\ge\frac1\gamma.
\]

For \(\lambda\ge0\), convexity gives
\[
e^{\lambda z}\le1+z(e^\lambda-1),\qquad 0\le z\le1.
\]
Consequently,
\[
\mathbb E\exp\left(\lambda\sum_iZ_i\right)
\le
\exp\left(\frac{s}{k}(e^\lambda-1)\right).
\]
Markov's inequality gives
\[
\Pr\left(\sum_iZ_i\ge\frac1\gamma\right)
\le
\exp\left(-\frac{\lambda}{\gamma}
+\frac{s}{k}(e^\lambda-1)\right).
\]
Taking \(e^\lambda=k/(\gamma s)\), which is permitted because \(k>\gamma s\), gives
\[
\Pr\left(\sum_iZ_i\ge\frac1\gamma\right)
\le
\exp\left(
-\frac1\gamma\log\frac{k}{\gamma s}
+\frac1\gamma-\frac{s}{k}
\right)
\le
\left(\frac{e\gamma s}{k}\right)^{1/\gamma}.
\]
∎

### Theorem 5.2

Let \(G=(S,T;E)\) be a simple bipartite graph embeddable in Euler genus \(g\), and let
\[
r=|S|.
\]
Suppose \(0<\gamma<1/2\), put
\[
q=\left\lceil\frac1\gamma\right\rceil,
\]
and assume \(k>\gamma r\). If
\[
\frac{2(r+g)}{q-2}
\left(\frac{e\gamma r}{k}\right)^{1/\gamma}<1,
\tag{5.2}
\]
then every assignment of at most \(\gamma k\) conflicts per edge is conflict \(k\)-colorable.

### Proof

Color all vertices of \(S\) independently and uniformly from \([k]\).

A vertex \(v\in T\) of degree \(d<q\) can never be blocked: regardless of the colors on its neighbors, at most
\[
d\gamma k<k
\]
colors are forbidden at \(v\).

Let
\[
T_q=\{v\in T:\deg(v)\ge q\},
\qquad t=|T_q|.
\]
Consider the bipartite subgraph consisting of \(S\cup T_q\) and all incident edges. It has at least \(qt\) edges. The bipartite Euler inequality gives
\[
qt\le2(r+t)-4+2g,
\]
and hence
\[
t\le\frac{2(r+g)}{q-2}.
\tag{5.3}
\]

For a fixed \(v\in T_q\), Lemma 5.1, applied to its at most \(r\) neighbors, shows that the probability that every color of \(v\) is forbidden is at most
\[
\left(\frac{e\gamma r}{k}\right)^{1/\gamma}.
\]
By (5.2), (5.3), and the union bound, with positive probability no vertex of \(T_q\) is blocked. Vertices of \(T\setminus T_q\) are never blocked. We can therefore choose an available color independently for every vertex of \(T\), completing the coloring. ∎

### Scaling consequence

Fix \(\gamma<1/2\) and \(C'>0\). There is an \(\eta=\eta(\gamma,C')>0\) such that the conjectured conclusion holds for every bipartite \(G=(S,T)\) satisfying
\[
|S|\le \eta k^{\,1-2\gamma}
\quad\text{and}\quad
k\ge C'\sqrt g.
\tag{5.4}
\]

Indeed, choose \(\eta>0\) sufficiently small that
\[
\gamma\eta<1
\quad\text{and}\quad
2(\eta+C'^{-2})(e\gamma\eta)^{1/\gamma}<1.
\]
Since \(g\le k^2/C'^2\), condition (5.4) gives
\[
r+g\le(\eta+C'^{-2})k^2
\]
and
\[
\left(\frac{e\gamma r}{k}\right)^{1/\gamma}
\le
(e\gamma\eta)^{1/\gamma}k^{-2}.
\]
Thus (5.2) follows.

In particular, when \(\gamma<1/2\), no family with one bipartition class of fixed order can generalize the planar \(K_{2,k^2}\) obstruction while still satisfying \(k=\Omega(\sqrt g)\).

---

## 6. Remaining gap

The arguments above cover:

1. arbitrary low-degree appendages, through core stripping;
2. cores with \(\Delta=O(\sqrt g)=O(k)\), through the local lemma;
3. bipartite instances with one side at most \(\eta k^{1-2\gamma}\).

They do not cover a core containing a small or mesoscopic collection of vertices of degree much larger than \(k\), with many overlapping neighborhoods. Such configurations are compatible with Euler genus \(g=\Theta(k^2)\). A direct edge-event local lemma sees dependency degree much larger than \(k\), while coloring the high-degree vertices first can leave correlated unary restrictions on their neighbors.

Thus the full conjecture remains unresolved here. The principal missing ingredient is a method exploiting the structure of these overlapping high-degree stars, rather than merely their maximum degree or total edge count.