```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For finite graphs the conjecture remains unresolved here, but fixed-map straightening requires additive error linear in girth, while the literal infinite-graph version has a growth-entropy counterexample.",
  "would_publish": false,
  "caveats": "The entropy counterexample is out of scope if the source assumes finite graphs, and the finite construction does not exclude a different map or a different target in the class."
}
```

## 1. Statement and conventions

I use the standard convention that an \((L,C)\)-quasi-isometry \(f:X\to Y\) satisfies
\[
L^{-1}d_X(x,x')-C\le d_Y(f(x),f(x'))\le Ld_X(x,x')+C
\]
for all \(x,x'\in X\), and every point of \(Y\) is within distance \(C\) of \(f(X)\).

There are two distinct conclusions below.

1. If infinite bounded-degree graphs are allowed, and “closed under contracting edges” means closure under contraction of one edge, hence under finite sequences of contractions, then the displayed conjecture is false.
2. For the intended finite-graph version, I give a family showing that one cannot in general retain the original quasi-isometry and merely assign lengths to the edges of the original target. The necessary additive error is \(\Omega(\operatorname{girth}(H))\).

The second result does not exclude a different quasi-isometry to a different member of the class, which is exactly the unresolved issue in the stated finite conjecture.

---

## 2. A counterexample if infinite graphs are allowed

For a connected graph \(X\) of finite maximum degree, define its upper volume entropy by
\[
h(X)=\limsup_{r\to\infty}\frac{1}{r}\log |B_X(x,r)|.
\]
This is independent of the base vertex \(x\).

### Lemma 2.1
If bounded-degree graphs \(X,Y\) admit a \((1,A)\)-quasi-isometry, then
\[
h(X)=h(Y).
\]

#### Proof
Let \(f:X\to Y\) be a \((1,A)\)-quasi-isometry.

Every fiber \(f^{-1}(y)\) has diameter at most \(A\), and hence cardinality at most
\[
M_X(A):=\sup_x |B_X(x,A)|<\infty.
\]
Thus
\[
|B_X(x,r)|
 \le M_X(A)\,|B_Y(f(x),r+A)|.
\]
Consequently \(h(X)\le h(Y)\).

Conversely, for each \(y\in B_Y(f(x),r)\), choose \(z_y\in X\) with
\[
d_Y(y,f(z_y))\le A.
\]
Then
\[
d_X(x,z_y)\le r+2A.
\]
For a fixed \(z\), at most
\[
M_Y(A):=\sup_y |B_Y(y,A)|
\]
vertices \(y\) can be assigned to \(z\). Hence
\[
|B_Y(f(x),r)|
 \le M_Y(A)\,|B_X(x,r+2A)|.
\]
This gives \(h(Y)\le h(X)\). ∎

Let \(T\) be the infinite \(3\)-regular tree. Then
\[
h(T)=\log 2.
\]
Let \(G=T^2\), the graph on \(V(T)\) in which two vertices are adjacent whenever their \(T\)-distance is at most \(2\). Its metric is
\[
d_G(u,v)=\left\lceil \frac{d_T(u,v)}2\right\rceil.
\]
Therefore the identity map
\[
\operatorname{id}:G\longrightarrow T
\]
is a \((2,0)\)-quasi-isometry. Moreover,
\[
B_G(o,r)=B_T(o,2r),
\]
so
\[
h(G)=2\log 2=\log 4.
\]

Now define
\[
\mathcal C=\{X:\ X\text{ is connected, has finite maximum degree, and }h(X)\le \log2\}.
\]

Contracting one edge is a bounded additive change of metric and therefore preserves volume entropy. Subdividing one edge also preserves entropy. More generally, an arbitrary subdivision cannot increase entropy: a radius-\(r\) ball in the subdivision contains at most a polynomial factor in \(r\) times the number of original edges incident with an original radius-\(r+O(1)\) ball. Thus \(\mathcal C\) is closed under edge contraction and subdivision in the usual one-edge/finite-sequence sense.

We have \(T\in\mathcal C\), and \(G\) is \((2,0)\)-quasi-isometric to \(T\). If there were a \((1,A)\)-quasi-isometry from \(G\) to some \(K\in\mathcal C\), Lemma 2.1 would give
\[
h(K)=h(G)=\log4,
\]
contrary to \(K\in\mathcal C\).

Hence:

> **Conditional counterexample.** If infinite bounded-degree graphs are included, the conjecture as displayed is false.

This argument does not apply if all graphs are finite. It also does not apply if closure under contraction is intended to include simultaneous contraction of arbitrary infinite edge sets.

---

## 3. A finite fixed-map obstruction

The following proposition concerns only finite graphs.

### Proposition 3.1
For every integer \(g\ge100\), there are finite connected graphs \(G_g,H_g\) and an onto \((2,1)\)-quasi-isometry
\[
p_g:G_g\to H_g
\]
such that \(H_g\) has girth at least \(g\), with the following property.

For every assignment of nonnegative real edge lengths
\[
\ell:E(H_g)\to[0,\infty),
\]
write \(d_\ell\) for the induced shortest-path pseudometric on \(V(H_g)\). If
\[
\bigl|d_\ell(p_g(x),p_g(y))-d_{G_g}(x,y)\bigr|\le A
\tag{3.1}
\]
for all \(x,y\in V(G_g)\), then
\[
A\ge \frac g{100}.
\]

In particular, this holds for nonnegative integer lengths, which are precisely the lengths relevant to subdivisions and contractions.

### 3.1. The high-girth target

We use a finite connected \(4\)-regular graph \(H\) of girth at least \(g\), with an edge partition
\[
E(H)=E_R\sqcup E_B
\]
such that every vertex has two incident red edges and two incident blue edges.

Such graphs exist for arbitrarily large \(g\). For completeness, one construction starts with a finite quotient of the free group \(F(a,b)\) in which no nontrivial reduced word of length less than \(g\) becomes trivial and in which word-length parity survives. Its Cayley graph with generators \(a^{\pm1},b^{\pm1}\) is finite, connected, simple, bipartite, \(4\)-regular, and has girth at least \(g\). Color the \(a\)-edges red and the \(b\)-edges blue.

Existence of the required finite quotient follows from residual finiteness of the free group. An elementary proof separates a fixed reduced word by letting its letters act along the path of its successive prefixes and completing the resulting partial permutations; taking a finite product handles all reduced words of length less than \(g\).

Thus each monochromatic subgraph of \(H\) is a disjoint union of cycles, all of length at least \(g\).

### 3.2. The turn graph

Define \(G\) by
\[
V(G)=V(H)\times\{R,B\}.
\]
Its edges are:

- the switch edge \((v,R)(v,B)\) for every \(v\in V(H)\);
- the edge \((u,R)(v,R)\) for every red edge \(uv\in E_R\);
- the edge \((u,B)(v,B)\) for every blue edge \(uv\in E_B\).

Thus \(G\) is cubic. Define
\[
p(v,c)=v.
\]

Every path in \(G\) projects to a walk in \(H\), with switch edges projecting to stationary steps. Hence
\[
d_H(p(x),p(y))\le d_G(x,y).
\tag{3.2}
\]

Conversely, let a shortest \(H\)-path between \(p(x)\) and \(p(y)\) have \(k\) edges. Lift each edge in its color layer. There is at most one initial switch, at most \(k-1\) switches between successive edges, and at most one final switch. Therefore
\[
d_G(x,y)\le 2k+1=2d_H(p(x),p(y))+1.
\tag{3.3}
\]
Equations (3.2)–(3.3), together with surjectivity, show that \(p\) is a \((2,1)\)-quasi-isometry.

---

## 4. Proof of the lower bound

Assume that (3.1) holds for some \(A<g/100\). Put
\[
s=\left\lfloor\frac g{10}\right\rfloor,
\qquad
T=\left\lfloor\frac g3\right\rfloor.
\]
For \(g\ge100\), these choices satisfy
\[
T<\frac g2,\qquad T-A>s+A,\qquad s-1>2A.
\tag{4.1}
\]

### Lemma 4.1
If \(Q\) is an \(H\)-path of length \(t<g/2\), then
\[
\ell(Q)\ge t-A.
\tag{4.2}
\]

#### Proof
Because \(H\) has girth at least \(g\), every path of length less than \(g/2\) is geodesic. If \(u,v\) are the endpoints of \(Q\), then
\[
d_H(u,v)=t.
\]
For any lifts \(x\in p^{-1}(u)\), \(y\in p^{-1}(v)\), (3.2) gives
\[
d_G(x,y)\ge t.
\]
Thus (3.1) gives
\[
d_\ell(u,v)\ge t-A.
\]
Since \(Q\) is one particular \(u\)-\(v\) path,
\[
\ell(Q)\ge d_\ell(u,v)\ge t-A.
\]
∎

### Lemma 4.2
Every monochromatic \(H\)-path \(P\) of length \(s\) satisfies
\[
\ell(P)\le s+A.
\tag{4.3}
\]

#### Proof
Suppose \(P\) is red, with endpoints \(u,v\); the blue case is identical. In \(G\), the path in the red layer from \((u,R)\) to \((v,R)\) has length \(s\). Since \(P\) is geodesic in \(H\), (3.2) implies
\[
d_G((u,R),(v,R))=s.
\]
Hence
\[
d_\ell(u,v)\le s+A.
\tag{4.4}
\]

Choose a simple \(\ell\)-shortest \(u\)-\(v\) path \(Q\). If \(Q\ne P\), then \(P\cup Q\) contains a cycle, and therefore
\[
|Q|+s\ge g.
\]
In particular \(|Q|\ge g-s>T\). Thus \(Q\) contains a consecutive \(T\)-edge subpath \(R\). By Lemma 4.1,
\[
\ell(Q)\ge\ell(R)\ge T-A>s+A,
\]
contradicting (4.4). Therefore \(Q=P\), and (4.3) follows. ∎

Apply Lemma 4.2 to all cyclic windows of \(s\) consecutive edges around every monochromatic cycle. On a monochromatic cycle \(C\), every edge occurs in exactly \(s\) such windows. Therefore
\[
s\sum_{e\in E(C)}\ell(e)\le |E(C)|(s+A).
\]
Summing over all red and blue cycles yields
\[
\sum_{e\in E(H)}\ell(e)
   \le |E(H)|\left(1+\frac As\right).
\tag{4.5}
\]

Now choose a uniformly random directed edge of \(H\), and then construct a directed path of length \(s\) by alternating colors, at each step choosing uniformly one of the two outward edges of the required color. The distribution of the directed edge at every position is uniform: the transition between directed red and directed blue edges is doubly stochastic. Hence, by (4.5), the expected \(\ell\)-length of this alternating path is at most
\[
s\left(1+\frac As\right)=s+A.
\]
Consequently, there is an alternating nonbacktracking path
\[
P=v_0v_1\cdots v_s
\]
such that
\[
\ell(P)\le s+A.
\tag{4.6}
\]
Since \(s<g\), this path is simple.

Let \(c_i\) be the color of \(v_{i-1}v_i\), and put
\[
x=(v_0,c_1),\qquad y=(v_s,c_s).
\]
Following \(P\) in \(G\) uses \(s\) horizontal edges and one switch between each pair of consecutive, oppositely colored edges. Thus
\[
d_G(x,y)\le 2s-1.
\]

In fact equality holds. Any alternative projected simple \(v_0\)-\(v_s\) path has length at least \(g-s>2s-1\), since its union with \(P\) contains a cycle. A projected walk reducing to \(P\) must still traverse all \(s\) alternating edges in order and must switch modes at least \(s-1\) times. Therefore
\[
d_G(x,y)=2s-1.
\tag{4.7}
\]

Combining (3.1), (4.6), and (4.7),
\[
2s-1-A
 \le d_\ell(v_0,v_s)
 \le \ell(P)
 \le s+A.
\]
Thus \(s-1\le2A\), contradicting (4.1). This proves Proposition 3.1. ∎

---

## 5. Consequence for contraction/subdivision-closed classes

Choose \(g_i\to\infty\), and let \(\mathcal C\) be the closure under edge contractions and subdivisions of the graphs \(H_{g_i}\). Then each
\[
p_i:G_{g_i}\to H_{g_i}\in\mathcal C
\]
is a \((2,1)\)-quasi-isometry.

For an integer assignment \(\ell:E(H_{g_i})\to\mathbb Z_{\ge0}\), replacing an edge of length \(k\ge1\) by a \(k\)-edge path and interpreting length \(0\) as contraction gives a member of \(\mathcal C\). Proposition 3.1 shows that no constant independent of \(i\) can make the original map \(p_i\) a \((1,C')\)-quasi-isometry to such a weighted version of \(H_{g_i}\).

Notably, the proof allows arbitrary nonnegative real lengths. Thus the obstruction is not merely an integer-rounding obstruction: it comes from transition or “turn” costs that cannot be represented by assigning costs independently to edges.

---

## 6. Remaining gap

This does **not** disprove the intended finite conjecture. The conjecture allows:

1. a new map \(G_{g_i}\to K\), rather than the prescribed projection \(p_i\);
2. a target \(K\in\mathcal C\) not obtained as the particular weighted version of \(H_{g_i}\), possibly even arising from another generator \(H_{g_j}\).

The averaging proof constrains distances between the prescribed fibers \(p_i^{-1}(v)\). A different map could encode the two color states at unrelated locations in the target and thereby avoid those constraints. I do not have a valid rigidity argument ruling this out.

Thus the finite result is a sharp obstruction to the natural same-map strengthening proved in the bounded-path-width setting, but the full finite contraction/subdivision-closed-class conjecture remains open in this analysis.