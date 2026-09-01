```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A full regularity-free proof is not obtained, but exact reductions to ordinary clique removal work for interval-transversal and common-safe-color patterns, while monotone ordered stars and order-spined graphs admit regularity-free bounds.",
  "would_publish": false,
  "caveats": "The arbitrary induced colored case with no unused color, particularly for unbounded forbidden families, remains unresolved."
}
```

## 1. Precise interpretation

Let \(\Sigma\) be a finite palette. An ordered \(\Sigma\)-graph \(G\) consists of a linearly ordered vertex set and a coloring
\[
c_G:\binom{V(G)}2\to \Sigma.
\]
For an ordered \(\Sigma\)-graph \(F\) on \([h]\), write \(N_F(G)\) for the number of increasing tuples
\[
x_1<\cdots <x_h
\]
such that
\[
c_G(x_i,x_j)=c_F(i,j)\qquad(1\le i<j\le h).
\]

All distances below are normalized by \(n^2\), rather than \(\binom n2\); this changes only constants.

The source theorem is already proved. The open request concerns the method and quantitative dependence, so it is not literally a yes/no conjecture. Here “regularity-free” will mean that the only non-elementary input is the ordinary graph removal lemma in the form admitting Fox’s regularity-free proof.

Let \(r_h(\alpha)>0\) be an ordinary \(K_h\)-removal function: every \(N\)-vertex graph requiring at least \(\alpha N^2\) edge deletions to become \(K_h\)-free contains at least
\[
r_h(\alpha)N^h
\]
copies of \(K_h\).

## 2. Exact reduction for interval-transversal copies

This is the cleanest place where the ordered problem reduces exactly to ordinary clique removal.

### Proposition 2.1

Let \(F\) be an ordered \(\Sigma\)-graph on \([h]\), with \(|\Sigma|\ge2\). Let
\[
V_1<V_2<\cdots <V_h
\]
be disjoint consecutive vertex sets in an ordered \(\Sigma\)-graph \(G\). A transversal copy of \(F\) is a copy \(x_1<\cdots <x_h\) with \(x_i\in V_i\).

Construct an ordinary graph \(A\) on \(V_1\sqcup\cdots\sqcup V_h\) by putting no edges inside the parts and, for \(i<j\), putting
\[
xy\in E(A)
\quad\Longleftrightarrow\quad
x\in V_i,\ y\in V_j,\ c_G(x,y)=c_F(i,j).
\]
Then:

1. \(K_h\)'s in \(A\) are in bijection with transversal copies of \(F\) in \(G\).
2. The minimum number of pair recolorings needed to eliminate all transversal copies of \(F\) equals the minimum number of edge deletions needed to make \(A\) \(K_h\)-free.

Consequently, if \(N=\sum_i|V_i|\) and at least \(\alpha N^2\) recolorings are necessary, then
\[
N_F^{\mathrm{tr}}(G)\ge r_h(\alpha)N^h.
\]

### Proof

An \(h\)-clique in the \(h\)-partite graph \(A\) contains exactly one vertex \(x_i\) from each \(V_i\). Since the blocks occur consecutively, \(x_1<\cdots <x_h\), and the clique conditions say precisely that all pair colors agree with \(F\).

Now let \(D\subseteq E(A)\) meet every \(K_h\). For every \(xy\in D\), where \(x\in V_i\), \(y\in V_j\), recolor \(xy\) to any color different from \(c_F(i,j)\). Since a pair between \(V_i\) and \(V_j\) has a unique possible role \((i,j)\), this operation only deletes the corresponding edge of \(A\); it cannot create a new one. Thus the resulting colored graph has no transversal \(F\).

Conversely, from any successful recoloring, take the originally matching pairs that cease to match their prescribed colors. They meet every original transversal copy and hence form a \(K_h\)-hitting set in \(A\). ∎

The missing global step is to find a bounded interval partition on which a positive proportion of the original edit distance survives. In the induced colored setting, repairs for different choices of blocks need not be compatible.

## 3. A global safe-color theorem

There is one situation in which the incompatibility disappears completely.

### Theorem 3.1

Let
\[
\mathcal F=\{F_1,\dots,F_s\}
\]
be a finite family of ordered \(\Sigma\)-graphs, with \(h_j=|V(F_j)|\ge2\). Suppose there is a color \(\sigma\in\Sigma\) which does not occur on any pair of any \(F_j\):
\[
c_{F_j}(u,v)\ne \sigma
\qquad\text{for all }j\text{ and }u<v.
\]
If an ordered \(\Sigma\)-graph \(G\) on \(n\) vertices is \(\varepsilon\)-far from being \(\mathcal F\)-free, then for some \(j\),
\[
N_{F_j}(G)
 \ge
 r_{h_j}\!\left(\frac{\varepsilon}{s h_j^2}\right)
 (h_jn)^{h_j}.
\]

In particular one may take
\[
\delta=
\min_{1\le j\le s}
h_j^{h_j}\,
r_{h_j}\!\left(\frac{\varepsilon}{s h_j^2}\right).
\]

### Proof

For each \(F_j\), form an \(h_j\)-partite ordinary graph \(A_j\) whose \(i\)-th part is a copy of \(V(G)\). For \(i<k\), put an edge between \((i,x)\) and \((k,y)\) precisely when
\[
x<y
\quad\text{and}\quad
c_G(x,y)=c_{F_j}(i,k).
\]
There are no edges inside parts.

Every \(K_{h_j}\) in \(A_j\) uses one vertex from every part. Its defining inequalities imply
\[
x_1<\cdots <x_{h_j},
\]
so these cliques are in bijection with ordered copies of \(F_j\).

Let \(\tau_j\) be the minimum number of edges that must be deleted from \(A_j\) to destroy all \(K_{h_j}\)'s, and choose a corresponding deletion set \(D_j\). Project \(D_j\) to a set \(S_j\) of pairs of \(V(G)\): put \(xy\in S_j\) if one of the role-copies of \(xy\) belongs to \(D_j\). Then
\[
|S_j|\le |D_j|=\tau_j.
\]

If \(\sum_j\tau_j<\varepsilon n^2\), recolor every pair in \(\bigcup_jS_j\) to \(\sigma\). This destroys every old \(F_j\)-copy because its corresponding clique was hit by \(D_j\). It creates no new forbidden copy, since \(\sigma\) occurs in none of the \(F_j\). Thus fewer than \(\varepsilon n^2\) recolorings would make \(G\) \(\mathcal F\)-free, a contradiction. Therefore
\[
\sum_{j=1}^s\tau_j\ge\varepsilon n^2,
\]
and some \(j\) satisfies \(\tau_j\ge\varepsilon n^2/s\).

Since \(A_j\) has \(h_jn\) vertices, it is
\[
\frac{\varepsilon}{s h_j^2}
\]
-far from \(K_{h_j}\)-free. Ordinary clique removal gives the asserted number of cliques, hence ordered copies of \(F_j\). ∎

This proof inherits the ordinary tower-type bound rather than the generic ordered wowzer-type bound. It also applies to any uniformly bounded family, since only finitely many ordered colored patterns of bounded size exist.

For binary simple graphs, the condition covers monochromatic patterns—complete and empty ordered graphs—but not a pattern using both edges and nonedges. For palettes with at least three colors, it is substantially broader.

## 4. Monotone ordered graphs with an order-spanning path

We next consider ordinary, non-induced ordered containment: a copy of an ordered simple graph \(F\) is only required to contain the edges of \(F\). This is a special case of the source theorem by forbidding all induced completions of \(F\).

We use the standard partite form of ordinary graph removal:

> For every graph \(H\) on \([h]\) and every \(\alpha>0\), there is \(p_H(\alpha)>0\) such that if an \(h\)-partite graph with equal parts of size \(m\) requires at least \(\alpha m^2\) edge deletions to eliminate all canonical copies of \(H\), then it contains at least \(p_H(\alpha)m^h\) canonical copies.

This is the vertex-labelled form of ordinary graph removal. Fox’s proof can be run while retaining the fixed vertex labels, so no induced or strong regularity lemma is needed.

### Theorem 4.1

Let \(F\) be an ordered graph on \([h]\) satisfying
\[
\{i,i+1\}\in E(F)
\qquad(1\le i<h).
\]
Then for every \(\varepsilon>0\) there is \(\delta_F(\varepsilon)>0\), obtainable from the ordinary partite removal function, such that every ordered graph \(G\) which is \(\varepsilon\)-far from ordered \(F\)-free contains at least
\[
\delta_F(\varepsilon)n^h
\]
order-preserving copies of \(F\).

The resulting bound is tower-type if one uses Fox’s ordinary removal bound.

### Proof

Set
\[
q=\max\left\{h,\left\lceil\frac4\varepsilon\right\rceil\right\}
\]
and partition \(V(G)\) into \(q\) consecutive intervals \(I_1<\cdots<I_q\), with sizes differing by at most one.

For sufficiently large \(n\),
\[
\sum_{a=1}^q\binom{|I_a|}{2}\le \frac{\varepsilon n^2}{4}.
\]
Delete all edges lying inside an interval, obtaining \(G_0\). Since \(G\) was \(\varepsilon\)-far from \(F\)-free, at least \(3\varepsilon n^2/4\) further deletions are needed to make \(G_0\) \(F\)-free.

In any ordered copy
\[
x_1<\cdots <x_h
\]
of \(F\) in \(G_0\), the edge \(x_ix_{i+1}\) exists for every \(i\). Hence \(x_i,x_{i+1}\) cannot lie in the same interval. Their interval indices are therefore strictly increasing, so every copy is transversal across some \(h\)-tuple
\[
I_{a_1}<\cdots<I_{a_h}.
\]

There are
\[
M=\binom qh
\]
such choices. Let \(\tau_{\mathbf a}\) be the minimum number of edges needed to destroy all copies with \(x_i\in I_{a_i}\). Since edge deletion cannot create a non-induced copy, the union of deletion sets for all \(\mathbf a\) destroys every copy in \(G_0\). Thus
\[
\sum_{\mathbf a}\tau_{\mathbf a}
 \ge \frac{3\varepsilon n^2}{4}.
\]
For some \(\mathbf a\),
\[
\tau_{\mathbf a}\ge \beta n^2,
\qquad
\beta=\frac{3\varepsilon}{4M}.
\]

Let \(m=\lceil n/q\rceil\), and pad the selected intervals with isolated vertices until every part has size \(m\). Because every vertex of \(F\) lies on the consecutive path, no padded isolated vertex can occur in a canonical copy. For \(n\ge q\), \(m\le 2n/q\), and therefore
\[
\tau_{\mathbf a}\ge
\frac{\beta q^2}{4}m^2.
\]
The partite removal lemma gives at least
\[
p_F\!\left(\frac{\beta q^2}{4}\right)m^h
 \ge
 q^{-h}p_F\!\left(\frac{\beta q^2}{4}\right)n^h
\]
copies. The finitely many smaller values of \(n\) are absorbed by decreasing \(\delta_F(\varepsilon)\). ∎

If \(\mathcal C(F)\) is the family of all ordered graphs on \([h]\) whose edge set contains \(E(F)\), then ordered \(F\)-subgraph-freeness is exactly induced \(\mathcal C(F)\)-freeness. Pigeonholing among the
\[
2^{\binom h2-e(F)}
\]
possible induced completions converts the theorem into a special case of the source removal lemma.

## 5. A polynomial bound for all ordered stars

The next result is entirely elementary and does not invoke any removal lemma.

Let \(S_{a,b}\) be the ordered star with \(a\) leaves before its center and \(b\) leaves after its center. Thus
\[
h=a+b+1,\qquad r=a+b=h-1,
\]
and all \(r\) required edges are incident with the center.

### Theorem 5.1

If an ordered graph \(G\) on \(n\) vertices is \(\varepsilon\)-far from containing no order-preserving, not-necessarily-induced copy of \(S_{a,b}\), then \(G\) contains at least
\[
\frac{\varepsilon^{\,h-1}}{a!\,b!}\,n^h
\]
such copies, with \(0!=1\).

### Proof

For a vertex \(v\), let
\[
L_v=|N(v)\cap(-\infty,v)|,\qquad
R_v=|N(v)\cap(v,\infty)|.
\]

Assume first that \(a,b\ge1\), and define
\[
t_v=
\min\bigl\{(L_v-a+1)_+,\ (R_v-b+1)_+\bigr\}.
\]
At each \(v\), delete either \(L_v-a+1\) left edges or \(R_v-b+1\) right edges, choosing the cheaper positive option. The union of all these deletions has size at most \(\sum_vt_v\), and afterward every vertex \(v\) has either fewer than \(a\) left-neighbors or fewer than \(b\) right-neighbors. Hence the resulting graph is \(S_{a,b}\)-free. Farness gives
\[
\sum_vt_v\ge\varepsilon n^2.
\]

The number \(C\) of ordered star copies is
\[
C=\sum_v\binom{L_v}{a}\binom{R_v}{b}.
\]
If \(t_v>0\), then \(L_v\ge t_v+a-1\) and \(R_v\ge t_v+b-1\), so
\[
\binom{L_v}{a}\binom{R_v}{b}
 \ge \frac{t_v^{a+b}}{a!\,b!}.
\]
By the power-mean inequality,
\[
\begin{aligned}
C
&\ge \frac1{a!\,b!}\sum_v t_v^{r}\\
&\ge \frac1{a!\,b!}\,
 n^{1-r}\left(\sum_vt_v\right)^r\\
&\ge \frac{\varepsilon^r}{a!\,b!}n^{r+1}.
\end{aligned}
\]

If \(a=0\), use \(t_v=(R_v-b+1)_+\); if \(b=0\), use \(t_v=(L_v-a+1)_+\). The same calculation applies. ∎

### Induced-family consequence

Let \(\mathcal F_{a,b}\) consist of all binary ordered graphs on these \(h\) vertices which contain the required star edges, with every other pair arbitrary. There are
\[
2^s,\qquad
s=\binom h2-(h-1),
\]
such completions. Every non-induced star copy realizes exactly one member of \(\mathcal F_{a,b}\). Therefore, under the hypotheses of Theorem 5.1, some \(H\in\mathcal F_{a,b}\) has at least
\[
\frac{\varepsilon^{h-1}}
     {a!\,b!\,2^s}\,n^h
\]
induced ordered copies.

For \(a=b=1\), this says that an ordered graph \(\varepsilon\)-far from having no increasing two-edge path contains at least \(\varepsilon^2n^3\) such paths, and either the induced ordered path or the ordered triangle occurs at least \(\varepsilon^2n^3/2\) times.

## 6. Why the global induced reduction fails

The safe-color assumption is not a cosmetic convenience. Without it, recoloring a pair to destroy one role can make the same pair suitable for another role.

For a concrete example, let \(F\) be the ordered three-vertex binary graph whose only edge is \(12\); its color vector on \(12,13,23\) is \(100\). Let \(G\) on \(1<2<3<4\) have
\[
E(G)=\{12,13,24\}.
\]
The four ordered triples have color vectors
\[
123:110,\qquad
124:101,\qquad
134:100,\qquad
234:010.
\]
Thus \(134\) is the unique \(F\)-copy. Toggling the pair \(13\) destroys that copy, but the vectors become
\[
123:100,\qquad 134:000,
\]
so a new \(F\)-copy appears on \(123\).

In the auxiliary role graph, the pair \(13\) was used as the \(12\)-pair of the old copy; after recoloring, the same pair becomes suitable as the \(13\)-pair of another copy. This cannot happen in Proposition 2.1 because fixed interval blocks give every pair a unique role. It also cannot happen in Theorem 3.1 because the unused color blocks every role simultaneously.

Thus the unresolved tasks are:

1. selecting mutually compatible repairs when a pair can play several order roles;
2. handling copies with several vertices inside the same coarse interval without monotonicity or a safe color;
3. obtaining a bounded forbidden member for an unbounded family.

These are precisely the points at which the arguments above stop. They do not constitute a full regularity-free proof for arbitrary hereditary properties of ordered colored graphs. The star estimate and the reductions are elementary and are not claimed to be novel enough for publication.