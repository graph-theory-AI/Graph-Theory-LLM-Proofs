```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general growth remains open, but I prove the exact first nontrivial value gr(G_{2x2},K_3)=9 and obtain essentially cubic bounds when all blue fibers have bounded chromatic number.",
  "would_publish": false,
  "caveats": "No improvement of the quoted general-n asymptotic bounds; the literature novelty of these finite and restricted results was not independently checked."
}
```

# 1. Statement and conventions

Write the row set and column set as \(R=C=[N]\). For \(r\in R\), let \(H_r\) be the graph on \(C\) whose blue edges are the blue horizontal edges in row \(r\). For \(x\in C\), let \(V_x\) be the graph on \(R\) whose blue edges are the blue vertical edges in column \(x\).

Thus rows \(r,s\) and columns \(x,y\) form a red rectangle precisely when
\[
xy\notin E(H_r)\cup E(H_s)
\quad\text{and}\quad
rs\notin E(V_x)\cup E(V_y).
\]

Every clique of order at least \(3\) in \(K_N\square K_N\) lies entirely in one row or one column. Consequently, avoiding a blue \(K_3\) is equivalent to requiring every \(H_r\) and every \(V_x\) to be triangle-free.

The main partial result is:

\[
\boxed{\operatorname{gr}(G_{2\times2},K_3)=9.}
\]

I also prove a structural result for colorings whose blue fiber graphs have bounded chromatic number.

---

# 2. Two elementary fiber lemmas

For distinct columns \(x,y\), define
\[
S_{xy}=\{r\in R:xy\notin E(H_r)\},\qquad s_{xy}=|S_{xy}|.
\]
Thus \(S_{xy}\) consists of the rows in which the horizontal edge \(xy\) is red. Define \(T_{rs}\) and \(t_{rs}\) symmetrically for vertical red edges.

## Lemma 2.1

In a red-rectangle-free coloring with no blue \(K_3\),
\[
s_{xy}\le 5,\qquad t_{rs}\le 5.
\]
Moreover, if \(s_{xy}=5\), then
\[
V_x[S_{xy}]\quad\text{and}\quad V_y[S_{xy}]
\]
are complementary \(5\)-cycles. The analogous statement holds when \(t_{rs}=5\).

### Proof

For any two vertices \(r,s\in S_{xy}\), the horizontal edge \(xy\) is red in both rows. Hence, to avoid a red rectangle, \(rs\) must be blue in at least one of \(V_x,V_y\). Therefore
\[
V_x[S_{xy}]\cup V_y[S_{xy}]=K_{S_{xy}}.
\]
Both graphs are triangle-free. If \(|S_{xy}|\ge6\), assign every edge of \(K_6\) to one of the two graphs containing it. This would give a two-coloring of \(K_6\) with no monochromatic triangle, contradicting \(R(3,3)=6\). Thus \(s_{xy}\le5\).

If \(|S_{xy}|=5\), the same assignment gives a triangle-free two-coloring of \(K_5\). In such a coloring every vertex has degree exactly \(2\) in each color: degree at least \(3\) in one color immediately gives either a triangle in that color or a triangle in the other color. Hence both color classes are \(5\)-cycles. Neither \(V_x[S_{xy}]\) nor \(V_y[S_{xy}]\) can have an additional edge, since every chord of a \(5\)-cycle creates a triangle. Thus they are exactly complementary \(5\)-cycles. ∎

---

# 3. Dense non-bipartite triangle-free graphs on nine vertices

The following small extremal lemma is the structural ingredient needed for \(N=9\).

## Lemma 3.1

Let \(G\) be a non-bipartite triangle-free graph on nine vertices.

1. \(e(G)\le17\).
2. If \(e(G)=17\), some edge belongs to every \(5\)-cycle of \(G\).
3. If \(e(G)=16\), then either some vertex belongs to every \(5\)-cycle of \(G\), or some edge belongs to every \(5\)-cycle of \(G\).

### Proof

Since \(G\) is non-bipartite, it contains an odd cycle. If its shortest odd cycle had length at least \(7\), every outside vertex would have at most two neighbors on that cycle: with three neighbors, the arcs between consecutive neighbors include a shorter odd arc, producing a shorter odd cycle. On nine vertices this gives at most
\[
7+2\cdot2+1=12
\]
edges when the shortest odd cycle has length \(7\), and fewer for length \(9\). Thus a graph with at least \(16\) edges contains a \(5\)-cycle.

Fix a \(5\)-cycle
\[
C=v_0v_1v_2v_3v_4v_0
\]
and let \(X=V(G)\setminus V(C)\), so \(|X|=4\). Every vertex of \(X\) has at most two neighbors on \(C\), because its neighborhood on \(C\) is independent. Also \(e(G[X])\le4\). Hence
\[
e(G)\le 5+8+4=17.
\]

If \(x\in X\) has two neighbors on \(C\), they have the form
\[
N_C(x)=\{v_{i-1},v_{i+1}\}
\]
for a unique \(i\in\mathbb Z_5\); call \(i\) the type of \(x\). If two such outside vertices are adjacent, their types are adjacent in the cycle \(\mathbb Z_5\), because their neighborhoods on \(C\) must be disjoint.

### The case \(e(G)=17\)

Equality forces every vertex of \(X\) to have two neighbors on \(C\), and \(G[X]\cong C_4\). Reading the types around this \(C_4\) gives a closed walk of length four in \(C_5\), so the set of types used has size at most three. Consequently, two consecutive type classes contain only their original vertices from \(C\).

All edges of \(G\) lie between consecutive type classes, so \(G\) is a subgraph of a blow-up of \(C_5\). Every \(5\)-cycle in such a blow-up uses exactly one vertex from each class: its sequence of classes is a closed walk of length five in \(C_5\), and hence goes once around the cycle. Therefore the edge joining the two consecutive singleton classes belongs to every \(5\)-cycle.

### The case \(e(G)=16\)

There are two possibilities:
\[
e(G[X])=3,\ e(C,X)=8,
\]
or
\[
e(G[X])=4,\ e(C,X)=7.
\]

In the first case every outside vertex has a type, and again \(G\) is a subgraph of a blow-up of \(C_5\). Four outside vertices distributed among five classes leave a singleton class, whose unique vertex belongs to every \(5\)-cycle.

In the second case \(G[X]\cong C_4\), and the four cross-degrees are \(2,2,2,1\). Label the outside cycle \(x_1x_2x_3x_4x_1\), with \(x_4\) having one neighbor on \(C\). Up to cyclic symmetry and reversal, the types of \(x_1,x_2,x_3\) are either
\[
0,1,0
\quad\text{or}\quad
0,1,2.
\]

In the first case the sole neighbor of \(x_4\) is one of \(v_0,v_2,v_3\). Deleting \(v_2v_3\) makes the graph bipartite, with one possible bipartition
\[
\{v_0,v_2,v_3,x_1,x_3\},
\qquad
\{v_1,v_4,x_2,x_4\}.
\]
Thus every \(5\)-cycle contains \(v_2v_3\).

In the second case the sole neighbor of \(x_4\) is one of \(v_0,v_2\). Deleting \(v_3v_4\) makes the graph bipartite, with bipartition
\[
\{v_1,v_3,v_4,x_2,x_4\},
\qquad
\{v_0,v_2,x_1,x_3\}.
\]
Thus every \(5\)-cycle contains \(v_3v_4\). ∎

---

# 4. No avoiding coloring exists for \(N=9\)

Assume, for contradiction, that \(K_9\square K_9\) has a coloring with neither a red rectangle nor a blue \(K_3\).

By Mantel's theorem,
\[
e(H_r),e(V_x)\le20.
\]
Define the total deficits
\[
D_H=\sum_{r=1}^9(20-e(H_r)),
\qquad
D_V=\sum_{x=1}^9(20-e(V_x)).
\]
Since each row contains \(36-e(H_r)\) red horizontal edges,
\[
\sum_{\{x,y\}}s_{xy}
=\sum_r(36-e(H_r))
=144+D_H.
\]
Let
\[
q_H=\#\{\{x,y\}:s_{xy}=5\}.
\]
Since every other \(s_{xy}\le4\),
\[
144+D_H
\le 5q_H+4(36-q_H)
=144+q_H,
\]
and hence
\[
q_H\ge D_H. \tag{4.1}
\]
Define \(q_V\) symmetrically; then
\[
q_V\ge D_V. \tag{4.2}
\]

Let \(k_H\) and \(k_V\) be the numbers of non-bipartite graphs among the \(H_r\)'s and \(V_x\)'s. Lemma 3.1 gives
\[
D_H\ge3k_H,\qquad D_V\ge3k_V. \tag{4.3}
\]

Form a graph \(Q_H\) on the columns, joining \(x,y\) when \(s_{xy}=5\). By Lemma 2.1, both \(V_x,V_y\) are non-bipartite whenever \(xy\in E(Q_H)\). Thus
\[
q_H\le \binom{k_V}{2}. \tag{4.4}
\]
Symmetrically,
\[
q_V\le \binom{k_H}{2}. \tag{4.5}
\]

## 4.1. Starting the bootstrap

We first note that \(q_H\ge1\). This follows from (4.1) unless \(D_H=0\). If \(D_H=0\), every \(H_r\) is an extremal triangle-free graph \(K_{4,5}\). Choose a binary label for its two parts. Each column \(x\) then gives a binary word \(a_x\in\{0,1\}^9\), and \(s_{xy}\) is the number of coordinates in which \(a_x,a_y\) agree.

If also \(q_H=0\), then all \(s_{xy}\le4\), while their sum is \(144=36\cdot4\). Hence every \(s_{xy}=4\), so every pair of words has Hamming distance \(5\). This is impossible for three binary words: the parity of their Hamming distance is the parity difference of their weights, and among three words two have weights of the same parity.

Thus \(q_H\ge1\). Iterating (4.1)–(4.5) now gives
\[
\begin{aligned}
q_H\ge1&\Longrightarrow k_V\ge2
\Longrightarrow D_V\ge6
\Longrightarrow q_V\ge6\\
&\Longrightarrow k_H\ge4
\Longrightarrow D_H\ge12
\Longrightarrow q_H\ge12\\
&\Longrightarrow k_V\ge6
\Longrightarrow D_V\ge18
\Longrightarrow q_V\ge18\\
&\Longrightarrow k_H\ge7
\Longrightarrow D_H\ge21
\Longrightarrow k_V\ge7.
\end{aligned}
\]
Therefore
\[
k_H,k_V\ge7. \tag{4.6}
\]

## 4.2. A degree refinement

Suppose a vertex \(x\) has degree at least \(6\) in \(Q_H\). If \(e(V_x)=17\), Lemma 3.1 supplies an edge \(ab\) lying in every \(5\)-cycle of \(V_x\). For every neighbor \(y\) of \(x\) in \(Q_H\), the graph \(V_x[S_{xy}]\) is a \(5\)-cycle and \(V_y[S_{xy}]\) is its complement. Hence \(ab\) is red in every such column \(y\). It would therefore be vertically red in at least six columns, contradicting \(t_{ab}\le5\).

Consequently, every degree-at-least-six vertex of \(Q_H\) corresponds to a vertical graph with at most \(16\) edges. If \(h_H\) denotes the number of such vertices, then
\[
D_V\ge3k_V+h_H. \tag{4.7}
\]
Symmetrically, if \(h_V\) is the number of degree-at-least-six vertices of \(Q_V\), then
\[
D_H\ge3k_H+h_V. \tag{4.8}
\]

For a graph \(Q\) on \(k\in\{7,8,9\}\) vertices with \(q\) edges, if \(h\) vertices have degree at least \(6\), then
\[
2q\le 5(k-h)+(k-1)h
=5k+(k-6)h. \tag{4.9}
\]

## 4.3. Forcing the equality case

The possibilities \(k_H,k_V\in\{7,8,9\}\) can now be eliminated except for \((9,9)\).

- If, say, \(k_V=7\), then
  \[
  q_H\ge D_H\ge3k_H\ge21=\binom72.
  \]
  This forces \(k_H=7\) and \(Q_H=K_7\), so \(h_H=7\). Equation (4.7) gives \(D_V\ge28\), hence \(q_V\ge28>\binom72\), impossible.

- If \(k_H=k_V=8\), then \(q_H,q_V\ge24\). By (4.9), a graph on eight vertices with at least \(24\) edges has at least four vertices of degree at least six. Thus both deficits are at least \(28\). One of the \(Q\)'s is then complete, giving eight high-degree vertices and forcing the opposite deficit to be at least \(32>28\), impossible.

- If \((k_H,k_V)=(8,9)\), then
  \[
  q_V\ge D_V\ge27.
  \]
  On eight vertices this forces \(h_V\ge7\), so
  \[
  D_H\ge24+7=31,\qquad q_H\ge31.
  \]
  On nine vertices, (4.9) then gives \(h_H\ge6\), whence
  \[
  D_V\ge27+6=33,\qquad q_V\ge33>\binom82.
  \]
  The reversed case is symmetric.

Therefore
\[
k_H=k_V=9. \tag{4.10}
\]

Initially \(D_H,D_V,q_H,q_V\ge27\). For a graph on nine vertices, (4.9) gives
\[
h\ge \left\lceil\frac{2q-45}{3}\right\rceil.
\]
Applying (4.7) and (4.8) alternately yields
\[
27\longrightarrow30\longrightarrow32\longrightarrow34
\longrightarrow35\longrightarrow36.
\]
Thus
\[
D_H,D_V,q_H,q_V\ge36.
\]
But Lemma 2.1 also gives
\[
144+D_H=\sum s_{xy}\le36\cdot5=180,
\]
so \(D_H\le36\), and similarly \(D_V\le36\). Hence equality holds throughout:
\[
D_H=D_V=q_H=q_V=36. \tag{4.11}
\]

It follows that:

- every pair of columns has \(s_{xy}=5\);
- every pair of rows has \(t_{rs}=5\);
- every \(H_r\) and every \(V_x\) is non-bipartite with exactly \(16\) edges.

Fix a column \(x\). By Lemma 3.1, either an edge or a vertex belongs to every \(5\)-cycle of \(V_x\).

If an edge \(ab\) belongs to every such cycle, then for every \(y\ne x\), it belongs to the \(5\)-cycle \(V_x[S_{xy}]\) and hence is absent from the complementary cycle \(V_y[S_{xy}]\). Thus \(ab\) is vertically red in all eight columns \(y\ne x\), contradicting \(t_{ab}\le5\).

If instead a vertex \(r\) belongs to every \(5\)-cycle of \(V_x\), then \(r\in S_{xy}\) for every \(y\ne x\). Hence every horizontal edge \(xy\) is red in row \(r\), so \(x\) is isolated in the blue graph \(H_r\). Since \(e(H_r)=16\), the remaining eight vertices induce a triangle-free graph with \(16\) edges, necessarily \(K_{4,4}\). Thus \(H_r\) is bipartite, contradicting (4.10).

This contradiction proves that no avoiding coloring exists for \(N=9\).

---

# 5. An avoiding coloring for \(N=8\)

Let both rows and columns be indexed by
\[
\mathbb F_2^2\times\mathbb F_2.
\]
Write a row as \(r=(u,t)\) and a column as \(x=(i,\varepsilon)\), where \(u,i\in\mathbb F_2^2\) and \(t,\varepsilon\in\mathbb F_2\).

Choose the linear map
\[
L(a,b)=(b,a+b).
\]
For every nonzero \(d\in\mathbb F_2^2\), the vectors \(d,Ld\) are linearly independent.

At the cell \((r,x)\), define
\[
\alpha(r,x)=u\cdot i+\varepsilon,
\qquad
\beta(r,x)=t+u\cdot Li.
\]

Color a horizontal edge in row \(r\) blue exactly when its two \(\alpha\)-labels differ. Color a vertical edge in column \(x\) blue exactly when its two \(\beta\)-labels differ. Thus every blue fiber is complete bipartite and therefore triangle-free.

Suppose rows \(r=(u,t)\), \(r'=(u',t')\) and columns
\(x=(i,\varepsilon)\), \(y=(j,\delta)\) formed a red rectangle. Horizontal redness gives
\[
(u-u')\cdot(i-j)=0.
\]
Vertical redness gives
\[
(u-u')\cdot L(i-j)=0.
\]
If \(i=j\), then \(x\ne y\) implies \(\varepsilon\ne\delta\), making a horizontal red edge impossible. Thus \(d=i-j\ne0\). Since \(d,Ld\) form a basis, the two displayed equations imply \(u=u'\). The vertical equality then gives \(t=t'\), contrary to the rows being distinct.

Hence this coloring has neither a red rectangle nor a blue \(K_3\). Combining this \(N=8\) construction with the preceding \(N=9\) upper bound gives
\[
\boxed{\operatorname{gr}(G_{2\times2},K_3)=9}.
\]

---

# 6. A bounded-chromatic structural theorem

The preceding construction extends to a useful restricted version of the general problem.

## Theorem 6.1

Suppose a coloring of \(K_N\square K_N\) has no red rectangle, and every blue row graph and every blue column graph is \(k\)-colorable. Then
\[
N\le k^3+k-1.
\]
For \(k=2\), the sharper bound
\[
N\le8
\]
holds, and it is attained by the construction above.

### Proof

Choose proper \(k\)-colorings
\[
a_{r,x}\in[k]
\]
of every blue row graph, and proper \(k\)-colorings
\[
b_{r,x}\in[k]
\]
of every blue column graph.

For columns \(x,y\), let
\[
S_{xy}=\{r:a_{r,x}=a_{r,y}\}.
\]
Equal row-colors guarantee that the horizontal edge \(xy\) is red. The map
\[
r\longmapsto (b_{r,x},b_{r,y})
\]
is injective on \(S_{xy}\): if two distinct rows had the same ordered pair, both vertical edges would also be red, producing a red rectangle. Hence
\[
|S_{xy}|\le k^2.
\]

In a row, if its \(k\) color classes have sizes \(n_1,\dots,n_k\), then
\[
\sum_i\binom{n_i}{2}
\ge \frac{N(N-k)}{2k}.
\]
Summing over rows gives
\[
\frac{N^2(N-k)}{2k}
\le \sum_{x<y}|S_{xy}|
\le k^2\binom N2.
\]
Therefore
\[
N(N-k)\le k^3(N-1).
\]
This is impossible when \(N\ge k^3+k\), proving
\[
N\le k^3+k-1.
\]

For \(k=2\) and \(N=9\), equality in the counting argument would force every pair of the nine binary column words to agree in exactly four coordinates, hence to have odd Hamming distance \(5\). As above, three binary words cannot be pairwise at odd distance. Thus \(N\le8\). ∎

## Finite-field lower construction

For every prime power \(q\), the \(N=8\) construction generalizes to \(N=q^3\). Index rows and columns by
\[
\mathbb F_q^2\times\mathbb F_q,
\]
choose a linear map \(L:\mathbb F_q^2\to\mathbb F_q^2\) with no eigenvalue in \(\mathbb F_q\), and use
\[
\alpha((u,t),(i,\varepsilon))=u\cdot i+\varepsilon,
\qquad
\beta((u,t),(i,\varepsilon))=t+u\cdot Li.
\]
Color a fiber edge blue when its corresponding labels differ.

Each blue fiber is complete \(q\)-partite, so it contains no \(K_{q+1}\). The same two-equation argument shows there is no red rectangle. Consequently,
\[
\operatorname{gr}(G_{2\times2},K_{q+1})\ge q^3+1.
\]
This polynomial lower bound is asymptotically weaker than the quoted quasi-polynomial lower bound, but together with Theorem 6.1 it shows that the bounded-chromatic variant has cubic order:
\[
q^3\le N_{\max}(q)\le q^3+q-1
\]
for prime-power \(q\), with \(N_{\max}(2)=8\).

---

# 7. Remaining gap

The argument does not improve
\[
2^{\Omega(\log^2 n)}
\le \operatorname{gr}(G_{2\times2},K_n)
\le 2^{O(n^{2/3}\log n)}
\]
for general \(n\). The bounded-chromatic theorem indicates why: any rectangle-free coloring on substantially more than \(k^3\) vertices must have at least one blue fiber of chromatic number greater than \(k\), even though that fiber remains \(K_n\)-free. Controlling such high-chromatic \(K_n\)-free fibers is precisely the aspect not addressed here.