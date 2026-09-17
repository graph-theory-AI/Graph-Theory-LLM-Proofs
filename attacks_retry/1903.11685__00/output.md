```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I verify the sufficient bound n >= d and prove that no fixed side length works in all dimensions, with [3]^52 already not L_3^52-list-colorable.",
  "would_publish": false,
  "caveats": "Exact thresholds remain undetermined in most dimensions; the lower bounds use unrestricted color palettes, and literature novelty has not been independently checked."
}
```

# 1. Statement of the partial results

For \(n\ge2\), let
\[
G_{d,n}=P_n^{\square d},\qquad
L_n^d(x)=2+\bigl|\{i:1<x_i<n\}\bigr|.
\]
Here, \(L_n^d\)-list-colorability means colorability from **every** assignment of lists of these sizes, with no restriction on the total palette.

I checked the previous attempt’s orientation argument; it is valid. The further progress below is a lower-bound construction.

## Theorem

1. If \(n\ge d\) and \(n\ge2\), then \(G_{d,n}\) is \(L_n^d\)-list-colorable.
2. For every fixed \(n\ge2\), there is a finite, explicitly bounded \(R_n\) such that
   \[
   G_{d,n}\text{ is not }L_n^d\text{-list-colorable whenever }d\ge R_n.
   \]
3. One can take
   \[
   R_2=3,\qquad R_3=52.
   \]

Consequently, define the smallest successful nondegenerate side length by
\[
t(d)=\min\{n\ge2:G_{d,n}\text{ is }L_n^d\text{-list-colorable}\}.
\]
Then
\[
t(2)=2,\qquad t(3)=3,
\]
and
\[
t(d)\longrightarrow\infty.
\]
The construction also gives the very weak quantitative bound
\[
\frac13\log_2^*d-O(1)\le t(d)\le \max\{2,d\}.
\]
In particular,
\[
4\le t(d)\le d\qquad(d\ge52).
\]

These conclusions also hold for the “eventual threshold,” requiring colorability at every larger side length. No monotonicity assertion in \(n\) is needed below.

The lower-bound constructions are probabilistic existence proofs, not displayed individual assignments on the enormous resulting boxes.

# 2. Verification of the sufficient bound

I include the proof because it is an essential part of the claimed progress.

## 2.1 A bipartite orientation criterion

**Lemma 2.1.** Let \(G\) be a finite bipartite graph and \(a:V(G)\to\mathbb Z_{\ge0}\). Suppose
\[
|E(G[X])|\le\sum_{v\in X}a(v)
\tag{2.1}
\]
for every \(X\subseteq V(G)\). Then \(G\) is \((a+1)\)-list-colorable.

**Proof.** First orient \(G\) with outdegrees at most \(a(v)\). To do this, give each vertex \(v\) exactly \(a(v)\) slots, and match every edge to a slot at one of its endpoints. Hall’s condition follows from (2.1): if \(\mathcal F\) is a set of edges and \(X\) is its set of endpoints, then
\[
|\mathcal F|\le |E(G[X])|\le\sum_{v\in X}a(v).
\]
Orient each edge away from the endpoint to whose slot it is matched.

Every orientation of a bipartite graph has a kernel, and the same holds in every induced subdigraph. Here is an elementary proof. With bipartition \(U,V\), begin with \(K=U\). Whenever a vertex \(y\in V\setminus K\) has no outgoing edge to \(K\cap U\), add \(y\) to \(K\) and remove all its neighbors from \(K\cap U\). Each removed vertex points to the newly added \(y\). Added vertices of \(V\) are never removed. At termination, \(K\) is independent, every removed vertex of \(U\) points into \(K\), and every vertex of \(V\setminus K\) points into \(K\). Thus \(K\) is a kernel.

Now take lists satisfying
\[
|A(v)|\ge d^+(v)+1.
\]
Choose a color \(\alpha\), and take a kernel \(K\) in the subdigraph induced by vertices whose lists contain \(\alpha\). Color \(K\) with \(\alpha\) and delete \(K\). Each remaining vertex losing \(\alpha\) also loses an outgoing neighbor, so the same list-size inequality is preserved. Induction completes the coloring. \(\square\)

## 2.2 Counting in a rectangular box

In fact, a rectangular version holds.

**Proposition 2.2.** Let
\[
B=[n_1]\times\cdots\times[n_d],\qquad n_i\ge2,
\]
and set
\[
L(x)=2+\bigl|\{i:1<x_i<n_i\}\bigr|.
\]
If
\[
\sum_{i=1}^d\frac1{n_i}\le1,
\tag{2.2}
\]
then \(B\) is \(L\)-list-colorable.

**Proof.** Write
\[
b(x)=|\{i:x_i\in\{1,n_i\}\}|,\qquad
a(x)=L(x)-1=d+1-b(x).
\]

Fix \(X\subseteq B\). On each coordinate-parallel line \(\lambda\), let:

- \(s_\lambda=|X\cap\lambda|\);
- \(r_\lambda\) be the number of nonempty consecutive runs of \(X\cap\lambda\);
- \(e_\lambda\) be the number of endpoints of \(\lambda\) belonging to \(X\).

Put
\[
R=\sum_\lambda r_\lambda,\qquad B_X=\sum_\lambda e_\lambda,
\]
where both sums run over lines in all directions. Then
\[
|E(B[X])|=d|X|-R,\qquad
\sum_{x\in X}b(x)=B_X.
\tag{2.3}
\]

On a non-full line, \(e_\lambda-r_\lambda\le0\). Indeed, if both endpoints occur but the line is not full, they lie in different runs. On a full line, \(e_\lambda-r_\lambda=1\).

If \(F_i\) is the number of full lines in direction \(i\), then
\[
n_iF_i\le |X|.
\]
Consequently,
\[
B_X-R\le\sum_iF_i
\le |X|\sum_i\frac1{n_i}
\le |X|.
\]
Using (2.3),
\[
|E(B[X])|
\le(d+1)|X|-B_X
=\sum_{x\in X}a(x).
\]
Lemma 2.1 applies. \(\square\)

Taking all \(n_i=n\) proves the sufficient bound \(n\ge d\).

# 3. The base obstruction at side length two

For \(n=2\), the list-size function is constantly \(2\), and the graph is the hypercube \(Q_d\).

Here is a bad assignment on \(Q_3\), using binary vertex labels. Put \(u=000\), \(v=111\), and assign
\[
A(u)=A(v)=A(100)=A(110)=\{1,2\},
\]
together with
\[
\begin{array}{c|c}
\text{vertex}&A(\text{vertex})\\ \hline
010&\{1,3\}\\
011&\{2,3\}\\
001&\{2,4\}\\
101&\{1,4\}.
\end{array}
\]

There are four possibilities for the colors of \(u,v\).

- If both receive \(1\), the adjacent vertices \(100,110\) are forced to \(2\).
- If both receive \(2\), those two vertices are forced to \(1\).
- If their colors are \(1,2\), respectively, the adjacent vertices \(010,011\) are forced to \(3\).
- If their colors are \(2,1\), respectively, the adjacent vertices \(001,101\) are forced to \(4\).

Thus \(Q_3\) is not 2-list-colorable.

A bad assignment in dimension \(r\) persists in every larger dimension: fix the extra coordinates at endpoints, so the list-size function on the resulting face is unchanged. Therefore
\[
G_{d,2}\text{ is not }L_2^d\text{-list-colorable for every }d\ge3.
\tag{3.1}
\]

Together with Section 2, this settles the threshold in dimensions two and three.

# 4. Amplifying an obstruction to a larger side length

The following construction is the main additional result. It increases the side length by one, at the cost of a very large increase in dimension.

## 4.1 The amplification lemma

**Lemma 4.1.** Suppose \(G_{r,m}\) is not \(L_m^r\)-list-colorable, where \(m\ge2\). Define
\[
P=P(m,r)
=\prod_{k=0}^{r-1}(k+2)^{\binom{r-1}{k}(m-1)^k},
\qquad Q=P^r.
\tag{4.1}
\]
If \(D\ge r\) satisfies
\[
D-r+1>
\frac{\log Q}{\log\bigl(Q/(Q-1)\bigr)},
\tag{4.2}
\]
then \(G_{D,m+1}\) is not \(L_{m+1}^D\)-list-colorable.

**Proof.** Fix a bad assignment \(A(z)\) on \([m]^r\), with
\[
|A(z)|=L_m^r(z).
\]
Exact sizes may be assumed by trimming lists.

For \(x\in[m+1]^D\), define its support by
\[
S(x)=\{i:x_i\le m\}.
\]
We use only vertices with support size \(r-1\) or \(r\).

### Control vertices

Vertices with support size \(r-1\) will be called controls. Give every control vertex \(y\) a private list \(C(y)\): all these lists are pairwise disjoint, and
\[
|C(y)|=L_{m+1}^D(y)
=2+|\{i:2\le y_i\le m\}|.
\tag{4.3}
\]

For each fixed support of size \(r-1\), the product of the list sizes over its \(m^{r-1}\) control vertices equals \(P\). Hence the number of possible color assignments to all controls is
\[
P^{\binom D{r-1}}.
\tag{4.4}
\]

### Copies of the bad box

For every \(r\)-subset \(S\subseteq[D]\), let
\[
B_S=\{x:S(x)=S\}.
\]
These are pairwise disjoint copies of \([m]^r\).

A vertex \(x\in B_S\) has a neighboring control vertex in direction \(i\in S\) precisely when \(x_i=m\): replace that coordinate by \(m+1\). Thus the control boundary of \(B_S\) consists of \(r\) disjoint faces, each containing \(m^{r-1}\) controls.

Independently for each pair \((S,y)\), where \(y\) is a control adjacent to \(B_S\), choose
\[
\sigma_S(y)\in C(y)
\]
uniformly.

Give \(B_S\) a fresh-color copy \(A_S\) of the bad assignment \(A\), with all core colors disjoint from the control lists. At \(x\in B_S\), use the list
\[
A_S(x)\ \cup\
\{\sigma_S(y):y\text{ is a control adjacent to }x\}.
\tag{4.5}
\]

These lists have exactly the required size. Indeed,
\[
L_{m+1}^D(x)
=L_m^r(x)+|\{i\in S:x_i=m\}|,
\tag{4.6}
\]
and the added colors in (4.5) are distinct.

If a coloring of the controls agrees with \(\sigma_S\) on the entire control boundary of \(B_S\), then all the added colors in (4.5) are forbidden by colored neighbors. What remains is the bad assignment \(A_S\). Therefore such a control coloring cannot extend across \(B_S\).

### First-moment calculation

Fix any assignment of colors to all controls. For a given \(B_S\), the probability that it agrees with all its prescribed boundary colors is
\[
P^{-r}=Q^{-1}.
\]
For this fixed control assignment, these events are independent over the different \(r\)-sets \(S\).

Let \(Z\) be the number of control assignments which do not agree completely with the prescription of any block. Every proper coloring of the constructed graph must induce one of these assignments. By (4.4),
\[
\mathbb E Z
=P^{\binom D{r-1}}
(1-Q^{-1})^{\binom Dr}.
\tag{4.7}
\]
Taking logarithms and using
\[
\frac{\binom Dr}{\binom D{r-1}}=\frac{D-r+1}{r},
\]
condition (4.2) gives \(\mathbb E Z<1\).

Since \(Z\) is a nonnegative integer, some choice of the prescriptions has \(Z=0\). The corresponding lists are uncolorable. Give all unused vertices arbitrary private lists of the required sizes; this cannot repair the obstruction. \(\square\)

## 4.2 Explicit recursion and unboundedness

Start with \(R_2=3\). Given \(R_m=r\), calculate \(P,Q\) from (4.1) and take
\[
R_{m+1}=r-1+\left\lceil Q\log Q\right\rceil.
\tag{4.8}
\]
This satisfies (4.2), since
\[
\log\frac{Q}{Q-1}>Q^{-1}.
\]

Induction proves that
\[
G_{R_m,m}\text{ is not }L_m^{R_m}\text{-list-colorable}
\]
for every \(m\ge2\), and therefore the same is true in all dimensions \(d\ge R_m\).

Now fix \(M\). For
\[
d\ge\max_{2\le m\le M}R_m,
\]
every side length \(2,\ldots,M\) fails. Hence \(t(d)>M\). This proves
\[
\boxed{t(d)\to\infty.}
\]

This conclusion is stronger than merely producing failures along a sequence of side lengths.

## 4.3 A quantitative, but extremely weak, consequence

The recursion is enormous. Nevertheless, it supplies an explicit asymptotic lower bound.

Since \(r=R_m\ge m\),
\[
\log Q
\le r\,m^{r-1}\log(r+1)
\le r^r\log(r+1).
\]
From (4.8), elementary estimates give, for \(r\ge3\),
\[
R_{m+1}
\le \exp\!\bigl(2r^r\log(r+1)\bigr)
\le 2^{\,2^{\,2^r}}.
\tag{4.9}
\]

Let \(T_0=1\) and \(T_{j+1}=2^{T_j}\). Starting from \(R_2=3\le T_2\), (4.9) yields
\[
R_m\le T_{3m-4}.
\]
Inverting this tower bound, and noting that the \(R_m\) increase, gives
\[
t(d)\ge \frac13\log_2^*d-O(1).
\]
The qualitative unboundedness is the more useful content.

# 5. A substantially smaller obstruction at \(n=3\)

The general recursion gives a poor bound even for side length three. A separate construction improves it to dimension \(52\).

## 5.1 A small finite count

Let \(a_4\) be the number of subsets of \(V(Q_4)\) which do not contain all four vertices of any two-dimensional face. Then
\[
a_4=27535.
\tag{5.1}
\]

Here is a hand-verifiable count.

Write \(Q_4=Q_3\square K_2\), and represent a vertex subset by \(A,B\subseteq V(Q_3)\). A two-face crossing the two layers is completely present exactly when \(A\cap B\) contains an edge of \(Q_3\). Thus the crossing-face condition is that \(A\cap B\) be independent.

The independence polynomial of \(Q_3\) is
\[
1+8z+16z^2+8z^3+2z^4.
\]
Consequently, the number of ordered pairs \((A,B)\) satisfying just the crossing-face condition is
\[
3^8+8\cdot3^7+16\cdot3^6+8\cdot3^5+2\cdot3^4
=37827.
\tag{5.2}
\]

Call \(A\) bad if it contains a two-face of \(Q_3\). For a fixed \(A\), the number of \(B\) with \(A\cap B\) independent is
\[
2^{8-|A|}\,i(Q_3[A]),
\]
where \(i(H)\) denotes the number of independent sets of \(H\), including the empty set.

All bad \(A\)'s are accounted for in this table. The last column counts bad \(B\)'s satisfying the crossing-face condition.

\[
\begin{array}{c|r|r|r|r}
\text{type of }A&\text{number}&|A|&i(Q_3[A])&
\#\text{ compatible bad }B\\ \hline
\text{a face}&6&4&7&7\\
\text{a face plus one vertex}&24&5&12&5\\
\text{complement of an adjacent pair}&12&6&17&0\\
\text{complement of a distance-two pair}&12&6&21&4\\
\text{seven vertices}&8&7&26&0\\
\text{all vertices}&1&8&35&0
\end{array}
\]

For example, when \(A\) is a face, a compatible bad \(B\) must contain the opposite face, and its additional vertices form an independent subset of \(A\), giving \(7\) possibilities. When \(A\) is a face plus one vertex, the same reasoning leaves an independent subset of a three-vertex path, giving \(5\). For a six-set missing a distance-two pair, the unique compatible face leaves two optional, nonadjacent vertices, giving \(4\).

Thus the number of pairs satisfying the crossing condition with \(A\) bad is
\[
5251,
\]
and the number with both \(A\) and \(B\) bad is
\[
6\cdot7+24\cdot5+12\cdot4=210.
\]
Inclusion–exclusion in (5.2) gives
\[
a_4=37827-2(5251)+210=27535,
\]
as claimed.

Set
\[
p=\frac{27535}{65536}.
\]
We will use
\[
p<2^{-5/4}.
\tag{5.3}
\]
This is an exact integer inequality: \(27535^4<2^{59}\).

## 5.2 The list construction

Consider \([3]^{52}\). Its corners are
\[
C=\{1,3\}^{52},\qquad N=|C|=2^{52}.
\]

Partition the \(52\) coordinate directions into \(13\) groups of four. Each group, together with fixed endpoint values in the other coordinates, determines a four-dimensional corner cube. Call these cubes **blocks**. There are
\[
M=13\cdot2^{48}=\frac{13}{16}N
\tag{5.4}
\]
blocks.

Every corner-cube edge belongs to exactly one block.

Give each corner \(v\) a private two-element list
\[
A(v)=\{a_{v,0},a_{v,1}\},
\]
with all these colors distinct.

For every block \(B\), independently choose a uniformly random bit
\[
\sigma_B(v)\in\{0,1\}
\]
at each of its sixteen corners.

For every corner-cube edge \(e=uv\), let \(m_e\) be its midpoint in \([3]^{52}\), and introduce a fresh color \(b_e\). If \(e\) belongs to block \(B\), give \(m_e\) the list
\[
A(m_e)=
\{a_{u,\sigma_B(u)},a_{v,\sigma_B(v)},b_e\}.
\tag{5.5}
\]
This vertex has exactly one interior coordinate, so its required list size is \(3\).

For each two-face \(F\) lying inside a block, give its center \(z_F\) the list
\[
A(z_F)=\{b_e:e\in E(F)\}.
\tag{5.6}
\]
This has size \(4\), as required for a vertex with two interior coordinates.

All other vertices receive arbitrary private lists of the required sizes.

## 5.3 Why some choice is uncolorable

Fix a choice of colors at all corners, represented by bits
\[
\varepsilon(v)\in\{0,1\}.
\]
In a block \(B\), define its matching set
\[
S_B=\{v\in V(B):\varepsilon(v)=\sigma_B(v)\}.
\]

If both endpoints of an edge \(e=uv\) lie in \(S_B\), then the first two colors in (5.5) are forbidden by the colored endpoints. Thus \(m_e\) is forced to \(b_e\).

It follows that if \(S_B\) contains all four vertices of a two-face \(F\), all four colors in (5.6) are forbidden. Hence a necessary condition for extension is:

> Every matching set \(S_B\) contains no complete two-face.

For the fixed corner assignment \(\varepsilon\), the \(S_B\)'s are independent uniformly random subsets of their sixteen corners. The probability of satisfying the necessary condition in all blocks is therefore \(p^M\).

Let \(Z\) be the number of corner assignments satisfying this condition. By (5.3) and (5.4),
\[
\begin{aligned}
\mathbb E Z
&=2^N p^M\\
&<2^N\left(2^{-5/4}\right)^{13N/16}\\
&=2^{-N/64}<1.
\end{aligned}
\]
Some choice of the block prescriptions therefore has \(Z=0\). Its lists admit no proper coloring.

We have proved
\[
\boxed{[3]^{52}\text{ is not }L_3^{52}\text{-list-colorable}.}
\]
By taking faces, this remains true in every dimension \(d\ge52\).

This improved base case can replace the much larger value of \(R_3\) in the recursion of Section 4.

# 6. What remains unresolved

These results do **not** determine the optimal threshold in general.

For example, they do not decide whether
\[
[3]^4
\]
is \(L_3^4\)-list-colorable. More generally, the construction above leaves dimensions \(4,\ldots,51\) undecided at side length three.

There is also a genuine limitation to the verified orientation proof. For the entire box,
\[
|E(G_{d,n})|
-\sum_x\bigl(L_n^d(x)-1\bigr)
=n^d\left(\frac dn-1\right).
\]
Thus, when \(n<d\), no orientation can satisfy
\[
d^+(x)\le L_n^d(x)-1
\]
at every vertex. This explains why that particular method stops at \(n=d\); it is **not** a necessary condition for ordinary list-colorability.

Finally, the lower bounds deliberately use many private colors. They establish failure of unrestricted list-colorability, but do not automatically yield nonextendable boundary colorings using only \(d+2\) colors.

The defensible conclusion is therefore:

- the previous improvement to \(n\ge d\) is sound;
- the optimal side length cannot be bounded independently of dimension;
- side length three already fails in dimension \(52\);
- the exact threshold function remains substantially unresolved.