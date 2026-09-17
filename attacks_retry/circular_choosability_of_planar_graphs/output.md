```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain cch(K_{2,n}) = 4 - 8/sqrt(n) + O(1/n) and a sharp bound for bipartite planar graphs, but do not improve the general planar upper bound.",
  "would_publish": false,
  "caveats": "The general 6–8 gap is unchanged; novelty of the auxiliary results and current literature status have not been independently verified."
}
```

# Partial results

Let
\[
\tau=\sup\{\operatorname{cch}(G):G\text{ is planar}\}.
\]
I do not determine \(\tau\). The supplied bounds \(6\le \tau\le8\) remain unchanged.

The main quantitative result below sharpens the preceding attempt’s estimates for \(K_{2,n}\) to an exact first-order asymptotic.

**Theorem 1.** For every \(n\ge1\), put \(k=\lfloor\sqrt n\rfloor\). Then
\[
\boxed{
\frac{4k}{k+2}
\le \operatorname{cch}(K_{2,n})
\le
4-\frac{8}{\sqrt{n+16}+6}.
}
\tag{1}
\]
Consequently,
\[
\boxed{
\operatorname{cch}(K_{2,n})
=4-\frac8{\sqrt n}+O\!\left(\frac1n\right).
}
\tag{2}
\]

The lower construction in (1) is the construction suggested in the previous attempt; I have checked it independently and reproduce its proof. The additional step is a different counting lemma giving the matching leading constant \(8\).

I also give a self-contained density bound for bipartite graphs.

**Theorem 2.** Define
\[
\operatorname{mad}(H)
=\max_{\varnothing\ne S\subseteq V(H)}
\frac{2|E(H[S])|}{|S|}.
\]
Every finite bipartite graph \(H\) is circularly
\[
\max\{2,\operatorname{mad}(H)\}\text{-choosable}.
\tag{3}
\]

In particular:

- the sharp supremum of circular choosability over **bipartite planar graphs** is \(4\);
- if a finite planar graph becomes bipartite after deletion of one vertex, its circular choosability is **strictly less than \(6\)**.

I do not claim that these auxiliary results are new.

## 1. Preliminaries

Graphs are finite and simple, and \(p,q\) are positive integers. Write
\[
\mathbb Z_p=\{0,\ldots,p-1\}.
\]
When \(p\ge2q\), the colors forbidden by a neighbor colored \(a\) form the cyclic interval
\[
F(a)=\{a-q+1,\ldots,a+q-1\}\pmod p,
\]
of size
\[
r=2q-1.
\]
Thus an edge is properly \((p,q)\)-colored exactly when neither endpoint’s color belongs to the other’s forbidden interval.

We use two elementary observations.

1. Lists can be trimmed to a specified common size without making a coloring problem harder to obstruct.
2. An uncolorable assignment with every list of size \(m\) gives
   \[
   \operatorname{cch}(G)\ge \frac mq.
   \tag{4}
   \]
   Indeed, it disproves circular \(t\)-choosability for every \(t\le m/q\). No assumption about attainment of the defining infimum is involved.

## 2. A density bound for bipartite graphs

We first prove Theorem 2.

### 2.1. A polynomial with controlled coefficient signs

Suppose \(p\ge2q\), let \(\omega=e^{2\pi i/p}\), and put \(r=2q-1\). Define
\[
f(x,y)=\prod_{j=-q+1}^{q-1}(x-\omega^j y).
\]
Its coefficients have the form
\[
f(x,y)=\sum_{a=0}^{r}(-1)^a\alpha_a x^{r-a}y^a,
\qquad \alpha_a>0.
\tag{5}
\]
More precisely,
\[
\alpha_a=
\prod_{j=1}^{a}
\frac{\sin((r-j+1)\pi/p)}{\sin(j\pi/p)}.
\tag{6}
\]
Every sine appearing here is positive because \(1\le j,r-j+1\le r<p\).

For completeness, formula (6) follows from the elementary identity
\[
\prod_{j=0}^{r-1}(1+u^j z)
=
\sum_{a=0}^{r}
u^{a(a-1)/2}
\left(\prod_{j=1}^{a}\frac{1-u^{r-j+1}}{1-u^j}\right)z^a.
\]
This identity follows by induction on \(r\). Set \(u=\omega\), replace \(z\) by \(\omega^{-q+1}z\), and use
\[
1-e^{2i\theta}=-2ie^{i\theta}\sin\theta.
\]
The phase factors cancel, giving (6).

Let \(H\) have bipartition \(X,Y\), and form
\[
P(\mathbf z)=\prod_{xy\in E(H),\,x\in X,\,y\in Y} f(z_x,z_y).
\tag{7}
\]
For a fixed exponent vector \(\mathbf d\), every contribution to the coefficient of
\[
\prod_v z_v^{d_v}
\]
has sign
\[
(-1)^{\sum_{y\in Y}d_y}.
\]
Consequently, **there is no cancellation**: whenever a monomial can be obtained by choosing one term from each edge factor, its coefficient is nonzero.

### 2.2. Allocating edge degree

Put
\[
D=\operatorname{mad}(H),\qquad T=\max\{2,D\},\qquad m=\lceil Tq\rceil.
\]
We claim that the \(r\) units of polynomial degree contributed by each edge can be allocated to its two endpoints so that no vertex receives more than \(m-1\) units.

Indeed,
\[
m-1\ge Tq-1\ge \frac{rD}{2}.
\tag{8}
\]
For \(D\ge2\), the last inequality is
\[
Dq-1\ge Dq-\frac D2.
\]
For \(D\le2\), it follows from \(2q-1\ge (2q-1)D/2\).

To obtain the allocation, replace each edge by \(r\) distinguishable copies and give each vertex capacity \(m-1\). Hall’s theorem applies to the incidence matching problem: a collection of edge copies whose endpoints lie in \(S\) has size at most
\[
r|E(H[S])|
\le \frac{rD}{2}|S|
\le (m-1)|S|.
\]
Thus every edge copy can be assigned to one endpoint without exceeding the capacities.

Let \(d_v\le m-1\) be the resulting allocation counts. By (5)–(7), the coefficient of
\[
\prod_v z_v^{d_v}
\]
in \(P\) is nonzero, and
\[
\sum_v d_v=\deg P.
\]

### 2.3. Grid nonvanishing gives a coloring

We use the following elementary polynomial principle:

> If a polynomial has total degree \(\sum_v d_v\) and has a nonzero coefficient of \(\prod_v z_v^{d_v}\), then it cannot vanish on every point of a product of sets whose \(v\)-th set has more than \(d_v\) elements.

This follows by restricting each coordinate to \(d_v+1\) points and applying the coefficient formula from univariate Lagrange interpolation successively.

Consider a nonvacuous \(T\)-\((p,q)\)-list assignment. Since \(T\ge2\), we have \(p\ge m\ge2q\). Associate to each vertex the set
\[
A_v=\{\omega^c:c\in L(v)\}.
\]
Its size is at least \(m>d_v\). Hence \(P\) is nonzero at some point of \(\prod_v A_v\).

For an edge \(xy\), its factor is nonzero precisely when
\[
c(x)-c(y)\not\equiv -q+1,\ldots,q-1\pmod p.
\]
This is exactly the required circular separation. The chosen point therefore gives a list coloring.

The empty graph is immediate, so this covers every case and proves Theorem 2. \(\square\)

### 2.4. Planar consequences

Every finite bipartite planar graph has maximum average degree strictly less than \(4\), by Euler’s formula. Thus Theorem 2 gives
\[
\operatorname{cch}(H)<4
\]
for every individual bipartite planar graph. The lower construction in Section 5 shows that their supremum is nevertheless \(4\).

There is also a useful extension. If \(G-v\) is bipartite, then
\[
\operatorname{cch}(G)
\le
2+\max\{2,\operatorname{mad}(G-v)\}.
\tag{9}
\]
To see this, let \(T=\max\{2,\operatorname{mad}(G-v)\}\), start with lists of size at least \((T+2)q\), and color \(v\) arbitrarily. Deleting its forbidden interval from neighboring lists leaves at least
\[
(T+2)q-(2q-1)=Tq+1
\]
colors at each neighbor. Apply Theorem 2 to \(G-v\).

When \(G\) is planar, the right side of (9) is strictly less than \(6\).

## 3. A separated-pair counting lemma

The next lemma is the quantitative step for \(K_{2,n}\).

For \(a,b\in\mathbb Z_p\), write
\[
d_p(a,b)=\min\{|a-b|,p-|a-b|\}.
\]

**Lemma 3.** Suppose
\[
3q\le m\le4q-2,\qquad p\ge2m.
\]
Put
\[
r=2q-1,\qquad \delta=2r-m.
\]
Let \(A,B\subseteq\mathbb Z_p\) be disjoint, and let \(S\subseteq\mathbb Z_p\) have \(m\) elements. Define
\[
\mathcal P=
\left\{(a,b)\in A\times B:
d_p(a,b)\notin[r-\delta,r+\delta]\right\}.
\]
Then
\[
\left|\{(a,b)\in\mathcal P:S\subseteq F(a)\cup F(b)\}\right|
\le
\left\lfloor\frac{(\delta+2)^2}{4}\right\rfloor.
\tag{10}
\]

**Proof.** Call a pair counted on the left a covering pair.

First, every covering pair has
\[
d_p(a,b)>r+\delta.
\tag{11}
\]
Indeed, if \(d=d_p(a,b)<r-\delta\), then \(p>2r\) and
\[
|F(a)\cup F(b)|=r+d<2r-\delta=m,
\]
which is impossible. Membership in \(\mathcal P\) now forces (11).

It follows that \(F(a)\) and \(F(b)\) are disjoint, and both gaps between them have more than \(\delta\) colors. Moreover,
\[
|F(a)\setminus S|+|F(b)\setminus S|
=2r-m=\delta.
\tag{12}
\]
In particular, neither interval can contain an entire gap of \(S\) having more than \(\delta\) colors.

Assume at least one covering pair exists. Its two forbidden intervals each meet \(S\), because \(m>r\). Their intervening gaps therefore lie in two distinct maximal gaps of \(S\), both longer than \(\delta\). There cannot be a third such gap: an interval covering points of \(S\) on both sides of that gap would contain more than \(\delta\) colors outside \(S\), contrary to (12).

Thus \(S\) has exactly two gaps longer than \(\delta\). They divide \(S\) into two nonempty clusters, say \(C_1,C_2\).

For every covering pair, one forbidden interval must contain all of \(C_1\), and the other all of \(C_2\). Neither interval can cross a long gap and meet both clusters.

Let \(h_j\) be the length, counting palette positions, of the arc from the first to the last point of \(C_j\) without crossing either long gap. Then
\[
h_j\le r,\qquad h_1+h_2\ge m.
\]
Since \(p>2r\), the number of cyclic intervals of length \(r\) containing this arc is
\[
r-h_j+1.
\]
Let their center sets be \(X_1,X_2\). Hence
\[
|X_1|+|X_2|
=2r+2-h_1-h_2
\le\delta+2.
\tag{13}
\]

A covering pair determines one center from \(X_1\) and one from \(X_2\). Conversely, a given ordered pair of cluster centers can correspond to at most one ordered pair in \(A\times B\): because \(A\cap B=\varnothing\), the roots cannot be interchanged in two different valid ways.

Therefore the number of covering pairs is at most
\[
|X_1||X_2|
\le
\left\lfloor\frac{(|X_1|+|X_2|)^2}{4}\right\rfloor
\le
\left\lfloor\frac{(\delta+2)^2}{4}\right\rfloor.
\]
This proves the lemma. \(\square\)

The reason for excluding the narrow distance range in the lemma is that, outside it, a leaf’s obstruction separates into two independently positioned clusters. The resulting product bound is asymptotically half the earlier triangular counting bound.

## 4. The upper bound for \(K_{2,n}\)

Set
\[
s=\sqrt{n+16},
\qquad
t=4-\frac8{s+6}
=\frac{4(s+4)}{s+6}.
\tag{14}
\]
Notice that \(3<t<4\).

Consider any \(t\)-\((p,q)\)-list assignment on \(K_{2,n}\). Trim all lists to size
\[
m=\lceil tq\rceil.
\]
Let \(A,B\) be the lists of the two vertices in its part of size two.

If \(A\cap B\ne\varnothing\), give both roots a common color. Each leaf then has at most \(r=2q-1<m\) forbidden colors, so the coloring extends.

Assume henceforth that \(A\cap B=\varnothing\). Then \(p\ge2m\). If \(m>2r\), any root-color pair extends to every leaf.

The remaining case is
\[
3q\le m\le2r.
\]
Put
\[
D=4q-m,\qquad \delta=D-2.
\]
Thus \(D\ge2\).

For each fixed \(a\in A\), at most \(4\delta+2\) colors \(b\) have circular distance from \(a\) in the integer interval
\[
[r-\delta,r+\delta].
\]
Consequently, the set \(\mathcal P\) from Lemma 3 satisfies
\[
|\mathcal P|
\ge m^2-m(4\delta+2)
=m^2-4mD+6m.
\tag{15}
\]

A leaf with list \(S\) prevents extension of exactly those root pairs for which
\[
S\subseteq F(a)\cup F(b).
\]
By Lemma 3, it prevents at most
\[
\left\lfloor\frac{D^2}{4}\right\rfloor
\]
pairs in \(\mathcal P\).

It remains to check that all \(n\) leaves together cannot prevent every pair in \(\mathcal P\). Let
\[
x=\frac Dm.
\]
Since \(m\ge tq\), equation (14) gives
\[
x=\frac{4q}{m}-1
\le \frac4t-1
=\frac2{s+4}
=:x_0.
\]
A direct calculation using \(s^2=n+16\) yields
\[
\frac n4 x_0^2+4x_0=1.
\]
The left side is increasing for \(x\ge0\), so
\[
\frac n4D^2+4mD\le m^2.
\tag{16}
\]
Combining (15) and (16),
\[
|\mathcal P|
\ge \frac n4D^2+6m
>
n\left\lfloor\frac{D^2}{4}\right\rfloor.
\]
Thus some root pair is prevented by no leaf. Choose it, and then color all leaves independently.

This proves circular \(t\)-choosability, including the endpoint in (14), and establishes the upper bound in (1). \(\square\)

## 5. The explicit lower bound

Fix a positive integer \(k\), and put
\[
q=k+2,\qquad p=8kq.
\]
For \(0\le i<2k\), define
\[
C_i=\{4qi+q,\ldots,4qi+q+3\}.
\]
These are pairwise disjoint four-color blocks.

Their common forbidden intervals are
\[
D_i:=\bigcap_{c\in C_i}F(c)
=\{4qi+4,\ldots,4qi+2q-1\}.
\]
Hence
\[
|D_i|=2q-4=2k.
\tag{17}
\]
All intervals used here lie inside the palette without wrapping.

On \(K_{2,k^2}\), give the two roots the lists
\[
A=\bigcup_{i=0}^{k-1}C_i,
\qquad
B=\bigcup_{j=0}^{k-1}C_{k+j}.
\]
Each has \(4k\) colors. Index the leaves by pairs
\[
(i,j)\in\{0,\ldots,k-1\}^2,
\]
and give leaf \((i,j)\) the list
\[
D_i\cup D_{k+j}.
\]
By (17), each leaf list also has \(4k\) colors.

In any purported coloring, the first root chooses a color from some \(C_i\), and the second chooses a color from some \(C_{k+j}\). The entire list of leaf \((i,j)\) is then forbidden: its first block is forbidden by the first root, and its second block by the second root.

Thus the assignment is uncolorable, and (4) gives
\[
\operatorname{cch}(K_{2,k^2})
\ge\frac{4k}{k+2}.
\tag{18}
\]
If \(k^2\le n\), extend the obstruction to \(K_{2,n}\) by assigning the full palette to the additional leaves. Taking \(k=\lfloor\sqrt n\rfloor\) proves the lower bound in (1).

Finally, (1) gives
\[
\frac8{\sqrt{n+16}+6}
\le
4-\operatorname{cch}(K_{2,n})
\le
\frac8{\lfloor\sqrt n\rfloor+2}.
\]
Both endpoints equal \(8/\sqrt n+O(1/n)\), proving (2). \(\square\)

Since \(K_{2,n}\) is bipartite and planar, this also completes the assertion that the sharp supremum for bipartite planar graphs is \(4\).

## 6. What remains unresolved

These arguments do not settle the catalog problem.

The precise limitations are:

- The polynomial argument relies on the bipartition to ensure that all contributions to a coefficient have the same sign. In a non-bipartite graph, cancellation can occur; the balanced coefficient for a triangle already illustrates this obstruction.
- The separated-pair argument works because, after the two root colors in \(K_{2,n}\) are fixed, every remaining vertex can be colored independently.
- The one-vertex extension bound covers planar graphs with a one-vertex odd-cycle transversal, not arbitrary planar graphs.

Thus I obtain neither an upper bound below \(8\) for all planar graphs nor a planar graph with circular choosability greater than \(6\). The new conclusion relative to the supplied attempt is the sharp first-order estimate
\[
\operatorname{cch}(K_{2,n})
=4-\frac8{\sqrt n}+O(n^{-1}),
\]
together with the self-contained subclass bounds above.