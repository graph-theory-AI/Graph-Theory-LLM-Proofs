```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture reduces exactly to asymmetric bigraph forcing, and it holds for complete bipartite graphs, a broad reflection-unicyclic family, suitable disjoint unions, and in particular every case with at most five arcs.",
  "would_publish": false,
  "caveats": "Only special cases and a radial local result are proved; the unrestricted conjecture and the novelty of these elementary cases remain open."
}
```

## 1. Graphon formulation

An oriented graphon is a measurable kernel \(W:[0,1]^2\to[0,1]\) satisfying
\[
W(x,y)+W(y,x)\le 1
\quad\text{a.e.}
\]
For an oriented graph \(B\),
\[
t(B,W)=\int_{[0,1]^{V(B)}}\prod_{uv\in E(B)}W(x_u,x_v)\,d\mathbf x,
\qquad
p(W)=\int_{[0,1]^2}W.
\]
At the graph-limit level, the directed forcing property says that
\[
t(B,W)=p(W)^{e(B)}
\quad\Longrightarrow\quad
W=p(W)\ \text{a.e.}                                      \tag{1}
\]
The usual finite-sequence formulation is equivalent by compactness and sampling.

Suppose \(B\) admits a homomorphism to the directed edge. Its vertices then admit a bipartition \(L\cup R\) such that every arc is directed from \(L\) to \(R\). Let \(H=(L,R;E)\) be the resulting bigraph. For any nonnegative kernel \(U\), write
\[
t_H(U)=
\int\prod_{uv\in E(H)}U(x_u,y_v)\,d\mathbf x\,d\mathbf y.
\]
Then
\[
t(B,W)=t_H(W).
\]

### Exact reduction

The directed forcing property of \(B\) is equivalent to
\[
t_H(U)=\left(\int U\right)^{e(H)}
\quad\Longrightarrow\quad
U\text{ is constant a.e.}                                \tag{AF}
\]
for every bounded nonnegative kernel \(U\).

Indeed, one implication is immediate. Conversely, if a nonconstant bounded \(U\ge0\) violated (AF), choose
\[
0<\lambda\le \frac{1}{2\|U\|_\infty}.
\]
Then \(W=\lambda U\) is an oriented graphon and
\[
t_H(W)=\lambda^{e(H)}t_H(U)
      =\left(\int W\right)^{e(H)},
\]
while \(W\) remains nonconstant.

Thus the orientation constraint does not make the equality problem easier: the conjecture is precisely the asymmetric/bigraph forcing assertion for every bipartite graph containing a cycle.

## 2. A hardness observation

Property (AF) for a cyclic \(H\) already implies the asymmetric Sidorenko inequality
\[
t_H(U)\ge \left(\int U\right)^{e(H)}.                      \tag{2}
\]

To see this, normalize \(\int U_-=1\) and suppose \(t_H(U_-)<1\). Choose a bounded positive nonconstant \(a\) with \(\int a=1\), and put
\[
U_+(x,y)=a(x).
\]
Since the \(L\)-side of a cyclic bipartite graph contains a vertex of degree at least two,
\[
t_H(U_+)=\prod_{u\in L}\int a(x)^{d_H(u)}\,dx>1.
\]
Choose \(a\) so that \(U_+-1\) is not proportional to \(U_--1\). Along
\[
U_s=(1-s)U_-+sU_+,
\]
continuity gives an \(s\in(0,1)\) with \(t_H(U_s)=1\), and the non-proportionality ensures \(U_s\) is not constant. This contradicts (AF).

In particular, the full directed conjecture would imply the ordinary forcing conjecture by restricting to symmetric kernels, and it would also imply the ordinary Sidorenko conjecture. This is only a hardness implication, not a resolution.

## 3. The tree inequality with equality information

The following standard entropy form of Sidorenko's inequality for trees will be used repeatedly.

### Lemma 1

Let \(T\) be a nontrivial bipartite tree with classes \(L_T,R_T\), and let \(W\ge0\) have mean \(p>0\). Define
\[
d(x)=\int W(x,y)\,dy,\qquad
c(y)=\int W(x,y)\,dx,
\]
and
\[
a(x)=\frac{d(x)}p,\qquad b(y)=\frac{c(y)}p.
\]
Then
\[
\log\frac{t_T(W)}{p^{e(T)}}
\ge
\left(\sum_{u\in L_T}(\deg_Tu-1)\right)\int a\log a
+
\left(\sum_{v\in R_T}(\deg_Tv-1)\right)\int b\log b.       \tag{3}
\]
Consequently \(t_T(W)\ge p^{e(T)}\). Moreover, equality forces \(d=p\) whenever the first coefficient in (3) is positive, and forces \(c=p\) whenever the second coefficient is positive.

#### Proof

After first assuming \(W>0\), define a probability density on \(T\)-labelings by
\[
q(\mathbf z)=
\frac{\displaystyle\prod_{uv\in E(T)}W(x_u,y_v)/p}
{\displaystyle
 \prod_{u\in L_T}a(x_u)^{\deg u-1}
 \prod_{v\in R_T}b(y_v)^{\deg v-1}}.
\]
Leaf elimination shows that \(q\) integrates to one and that every \(L_T\)-vertex has marginal density \(a\), while every \(R_T\)-vertex has marginal density \(b\).

Applying nonnegativity of relative entropy between \(q\) and the probability density proportional to \(\prod_{uv}W(x_u,y_v)\) gives (3). Finally,
\[
\int a\log a\ge0,\qquad \int b\log b\ge0,
\]
with equality only for the constant density \(1\). General \(W\ge0\) follows by approximation. \(\square\)

## 4. A broad forcing family obtained by doubling a tree

Here is the main concrete partial result.

### Theorem 2: reflection-unicyclic graphs are forcing

Let \(D\) be a bipartite tree with two distinguished vertices \(a,b\) at distance
\[
\ell=\operatorname{dist}_D(a,b)\ge2.
\]
Take two copies \(D_1,D_2\), identify their two copies of \(a\), and also identify their two copies of \(b\). Let \(R\) be any further rooted bipartite tree, whose root is identified with the common vertex \(a\). Denote the resulting bipartite graph by \(H(D,R)\).

Then \(H(D,R)\) satisfies
\[
t_{H(D,R)}(W)\ge p(W)^{e(H(D,R))}
\]
for every bounded nonnegative \(W\), with equality only when \(W\) is constant. Hence its canonical orientation has the directed forcing property.

The graph \(H(D,R)\) is unicyclic. Taking \(D\) to be a path gives, in particular:

- every canonically oriented even cycle;
- every even cycle with an arbitrary tree attached at a single cycle vertex.

#### Proof

Assume \(a\in L\); the other case follows by transposing \(W\). Let
\[
P_D(x,z)
\]
be the two-rooted homomorphism density of \(D\), with \(a\) fixed at \(x\) and \(b\) fixed at \(z\). Let \(h_R(x)\) be the rooted homomorphism density of \(R\).

Because the two copies of \(D\) share only \(a,b\),
\[
t_{H(D,R)}(W)
=
\int h_R(x)\int P_D(x,z)^2\,dz\,dx.
\]
Jensen's inequality gives
\[
t_{H(D,R)}(W)
\ge
\int h_R(x)\left(\int P_D(x,z)\,dz\right)^2dx.             \tag{4}
\]
The expression on the right is the homomorphism density of a tree \(S\): take two copies of \(D\), identify only their \(a\)-vertices, leave their \(b\)-vertices distinct, and attach \(R\) at \(a\). Moreover,
\[
e(S)=2e(D)+e(R)=e(H(D,R)).
\]
Lemma 1 therefore yields
\[
t_{H(D,R)}(W)\ge t_S(W)\ge p^{e(H(D,R))}.                  \tag{5}
\]

Suppose equality holds. Then equality holds throughout (4)–(5). In \(S\), the common \(a\)-vertex has degree at least two. Since \(\ell\ge2\), a neighbor of \(a\) on either \(a\)-\(b\) path has degree at least two and lies in the opposite bipartition class. Thus both coefficients in (3) are positive, and consequently
\[
d(x)=p,\qquad c(y)=p                                      \tag{6}
\]
almost everywhere.

For a biregular kernel satisfying (6), the rooted density of every tree with \(q\) edges is identically \(p^q\), by induction from the leaves. Hence
\[
h_R(x)=p^{e(R)}>0.
\]
Equality in Jensen now implies that \(P_D(x,z)\) is independent of \(z\) for almost every \(x\). Its \(z\)-integral is the rooted density of \(D\) at \(a\), hence
\[
P_D(x,z)=p^{e(D)}\quad\text{a.e.}                          \tag{7}
\]

Let \(P_\ell(x,z)\) be the kernel of the unique \(a\)-\(b\) path in \(D\). Removing that path leaves rooted trees attached to its vertices. Under (6), all such rooted-tree factors are constant, so (7) gives
\[
P_\ell(x,z)=p^\ell\quad\text{a.e.}                         \tag{8}
\]

Let \(T:L^2(R)\to L^2(L)\) be the integral operator with kernel \(W\).

- If \(\ell=2r\), then \(P_\ell\) is the kernel of \((TT^*)^r\).
- If \(\ell=2r+1\), then \(P_\ell\) is the kernel of \((TT^*)^rT\).

In either case the nonzero singular values are positive powers of the nonzero singular values of \(T\). Equation (8) says that the relevant operator has rank one, so \(T\) itself has rank one. Together with
\[
T1=p1,\qquad T^*1=p1,
\]
this forces \(T=pJ\), where \(Jf=(\int f)1\). Thus \(W=p\) almost everywhere. \(\square\)

## 5. Complete bipartite graphs

### Theorem 3

For every \(s,t\ge2\), the canonical orientation of \(K_{s,t}\) has the directed forcing property.

#### Proof

For
\[
F(x_1,\ldots,x_s)=\int\prod_{i=1}^sW(x_i,y)\,dy,
\]
one has
\[
t_{K_{s,t}}(W)=\int F(x_1,\ldots,x_s)^t\,d\mathbf x.
\]
Twice applying Jensen gives
\[
\begin{aligned}
t_{K_{s,t}}(W)
&\ge \left(\int F\right)^t\\
&=\left(\int c(y)^s\,dy\right)^t\\
&\ge p^{st}.                                               \tag{9}
\end{aligned}
\]

Suppose equality holds. Strict convexity implies
\[
c(y)=p
\quad\text{and}\quad
F(x_1,\ldots,x_s)=p^s
\]
almost everywhere. Define
\[
K(x,x')=\int W(x,y)W(x',y)\,dy.
\]
Integrating the equality \(F=p^s\) over \(x_3,\ldots,x_s\) gives
\[
p^{s-2}K(x_1,x_2)=p^s,
\]
so \(K=p^2\) almost everywhere. Since \(c=p\),
\[
p\,d(x)=\int K(x,x')\,dx'=p^2,
\]
and hence \(d=p\).

Set \(G=W-p\). Then
\[
\int G(x,y)G(x',y)\,dy
=
K(x,x')-p\,d(x)-p\,d(x')+p^2=0.
\]
Thus the integral operator with kernel \(G\) satisfies \(GG^*=0\), so \(G=0\). Therefore \(W=p\) almost everywhere. \(\square\)

## 6. Disconnected closure and small graphs

If \(H=H_1\sqcup\cdots\sqcup H_r\), then
\[
t_H(W)=\prod_i t_{H_i}(W).
\]
Consequently, if each component is asymmetrically Sidorenko and at least one component is equality-rigid, then \(H\) is equality-rigid.

Combining Lemma 1 and Theorems 2–3 proves:

### Corollary 4

The conjecture holds whenever every component of the associated bigraph is one of:

1. a tree;
2. a reflection-unicyclic graph \(H(D,R)\) from Theorem 2;
3. a complete bipartite graph \(K_{s,t}\) with \(s,t\ge2\);

and at least one component contains a cycle.

### Corollary 5: all cases with at most five arcs

If \(B\) maps to an edge, has at most five arcs, and its underlying graph contains a cycle, then \(B\) has the directed forcing property.

Indeed, its underlying graph is bipartite. With at most five edges, its only possible cycle is a \(C_4\). A fifth edge is either in a separate tree component or is a pendant edge attached to the \(C_4\). The latter is Theorem 2 with \(D\) a two-edge path and \(R\) a rooted edge.

## 7. A general infinitesimal result

Although it does not prove global forcing, every conjectured graph is strictly forcing along each fixed perturbation direction around a constant kernel.

### Proposition 6

Let \(H\) be any bipartite graph containing a cycle, with \(m=e(H)\). Let \(p>0\), and let \(U\) be a nonzero bounded signed kernel with \(\int U=0\). Then, for every sufficiently small nonzero \(\varepsilon\) for which \(p+\varepsilon U\ge0\),
\[
t_H(p+\varepsilon U)>p^m.                                 \tag{10}
\]

#### Proof

Expand
\[
t_H(p+\varepsilon U)
=
\sum_{F\subseteq E(H)}
p^{m-|F|}\varepsilon^{|F|}t_F(U).                          \tag{11}
\]
The linear coefficient vanishes because \(\int U=0\).

Put
\[
\rho(x)=\int U(x,y)\,dy,\qquad
\gamma(y)=\int U(x,y)\,dx.
\]
The quadratic coefficient equals
\[
p^{m-2}\left(
 \sum_{u\in L}\binom{\deg_Hu}{2}\|\rho\|_2^2
 +
 \sum_{v\in R}\binom{\deg_Hv}{2}\|\gamma\|_2^2
\right).                                                   \tag{12}
\]
Both combinatorial coefficients are positive because \(H\) contains a cycle. Thus, if either marginal is nonzero, the first nonzero term is a positive multiple of \(\varepsilon^2\).

Now suppose \(\rho=\gamma=0\). If an edge-subgraph \(F\) has a leaf, integrating the leaf variable shows \(t_F(U)=0\). Let \(g\) be the girth of \(H\). Every nonempty \(F\) with fewer than \(g\) edges is a forest and hence has a leaf. At order \(g\), the only nonvanishing edge sets are \(g\)-cycles. Therefore the coefficient of \(\varepsilon^g\) is
\[
p^{m-g}N_g(H)\,t_{C_g}(U),
\]
where \(N_g(H)>0\). Since \(g=2k\),
\[
t_{C_g}(U)
=
\operatorname{Tr}\bigl((T_UT_U^*)^k\bigr)
=
\sum_i \sigma_i(U)^{2k}>0
\]
for \(U\ne0\). As \(g\) is even, this again gives (10) for both signs of sufficiently small \(\varepsilon\). \(\square\)

The size of the permitted neighborhood depends on the direction \(U\). Thus Proposition 6 is only a radial statement; it does not give a uniform local minimum in the infinite-dimensional kernel space and does not rule out global equality kernels.

## 8. Remaining gap

The argument does not cover arbitrary connected cyclic bipartite graphs. The reflection proof depends crucially on writing the cycle contribution as the square of two identical two-rooted tree densities. Decorations on the two sides of a cycle that are not matched destroy this structure. For example, a \(C_4\) with pendant edges attached at two adjacent cycle vertices is not covered by the arguments above.

Accordingly, no complete proof or counterexample is obtained. The exact reduction also shows that a full proof would resolve the corresponding asymmetric forcing problem, and in particular would imply the ordinary forcing and Sidorenko conjectures. I have not verified whether the elementary special families above have already appeared explicitly in the literature, so I do not claim publication-level novelty.