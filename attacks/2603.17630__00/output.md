```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The optimal exponent is proved for graphs with vertex-cover number o(log n), including all joins H ∨ overline(K)_{n-d}, and for a further minimum-degree-d matching-join family.",
  "would_publish": false,
  "caveats": "General graphs need not contain a large false-twin class, and the uniformity intended by the supplied o_n(1) is not formally specified."
}
```

## 1. Interpretation and summary of the partial result

I interpret the conjecture in the usual fixed-\(d\) sense, or in a growing-\(d\) regime in which the displayed \(o_n(1)\) is uniform. The latter dependence is not specified in the supplied statement, so the bounds below are explicit.

The main observation is an exact factorization for the spanning-tree degree enumerator of a large class of false twins. It yields the following.

### Theorem 1: bounded vertex cover

Let \(G\) be an \(n\)-vertex connected graph with minimum degree at least \(d\ge 2\), and suppose \(G\) has a vertex cover \(A\) of size \(r\). Then there is a set \(S\subseteq A\), with
\[
s:=|S|\ge d,
\]
and a class \(U\subseteq V(G)\setminus A\) of vertices having common neighborhood \(S\), of size
\[
m:=|U|\ge \frac{n-r}{2^r}.
\]
If \(N=m-1\ge 2rs\), then for every \(n\)-vertex tree \(R\),
\[
\mathbb P(\mathcal T\cong R)
 \le
 3r^s(2s)^{s/2}N^{-(s-1)/2}
 +s\exp\!\left(-\frac{N}{8s}\right).
\tag{1}
\]

Consequently:

1. For every fixed \(r\),
   \[
   \sup_R\mathbb P(\mathcal T\cong R)
   =O_r\!\left(n^{-(d-1)/2}\right).
   \tag{2}
   \]
2. More generally, if \(r=o(\log n)\), then
   \[
   \sup_R\mathbb P(\mathcal T\cong R)
   \le n^{-(1/2-o(1))(d-1)}.
   \tag{3}
   \]

A particularly relevant special case is \(\operatorname{vc}(G)=d\). Then necessarily
\[
G=H\vee \overline{K}_{n-d}
\]
for some graph \(H\) on \(d\) vertices. In this case, writing \(N=n-d-1\), one obtains the more explicit bound
\[
\mathbb P(\mathcal T\cong R)
 \le
 3d!(2d)^{d/2}N^{-(d-1)/2}
 +d\exp\!\left(-\frac{N}{8d}\right),
\tag{4}
\]
provided \(N\ge 2d^2\). Thus the conjectured exponent holds throughout this whole extremal-looking family, not only for \(K_{d,n-d}\). The estimate is also uniform, for example, when \(d=n^{o(1)}\).

I also prove the conjectured exponent for one family with vertex-cover number linear in \(n\): take \(d-1\) hubs, join them to all remaining vertices, and put a perfect matching on the remaining vertices.

The general conjecture remains unresolved.

---

## 2. A weighted complete-bipartite identity

We use the following standard identity, included with its proof.

Let the two sides of \(K_{p,q}\) have weights
\[
\alpha_1,\dots,\alpha_p,\qquad \beta_1,\dots,\beta_q,
\]
and give edge \(ij\) weight \(\alpha_i\beta_j\). Then
\[
\sum_{T\in\mathsf{ST}(K_{p,q})}\prod_{e\in T}w(e)
 =
 \left(\sum_{i=1}^p\alpha_i\right)^{q-1}
 \left(\sum_{j=1}^q\beta_j\right)^{p-1}
 \prod_{i=1}^p\alpha_i\prod_{j=1}^q\beta_j.
\tag{5}
\]

Indeed, put \(A=\sum_i\alpha_i\) and \(B=\sum_j\beta_j\), delete one vertex on the \(q\)-side in the weighted Laplacian, and take the Schur complement of the resulting diagonal block. The remaining determinant is
\[
A^{q-1}\prod_{j<q}\beta_j\,
\det\left(B\operatorname{diag}(\alpha_i)
-\frac{B-\beta_q}{A}\alpha\alpha^{\mathsf T}\right).
\]
The matrix determinant lemma gives
\[
\det\left(B\operatorname{diag}(\alpha_i)
-\frac{B-\beta_q}{A}\alpha\alpha^{\mathsf T}\right)
 =
 B^{p-1}\beta_q\prod_i\alpha_i,
\]
which proves (5).

---

## 3. The false-twin factorization

### Lemma 2

Let \(G\) be connected. Suppose \(U\) is an independent set of \(m\) vertices such that every \(u\in U\) has the same neighborhood \(S\), where \(|S|=s\). Let
\[
D_i=\deg_{\mathcal T}(i),\qquad i\in S,
\]
for a uniformly random spanning tree \(\mathcal T\) of \(G\).

Then there is a random vector \(Y\in\mathbb Z_{\ge0}^S\) such that
\[
(D_i:i\in S)\ \stackrel{d}{=}\ M+Y,
\tag{6}
\]
where \(M\) and \(Y\) are independent and
\[
M\sim \operatorname{Mult}\left(m-1;\frac1s,\dots,\frac1s\right).
\tag{7}
\]

In particular,
\[
\sup_z\mathbb P\big((D_i)_{i\in S}=z\big)
\le
\sup_z\mathbb P(M=z).
\tag{8}
\]

### Proof

Put \(W=V(G)\setminus U\), and introduce variables \(x_i\), \(i\in S\). Give an edge \(uv\) weight
\[
w(uv)=x_u^{\mathbf 1_{\{u\in S\}}}
       x_v^{\mathbf 1_{\{v\in S\}}}.
\]
Thus
\[
Z(\mathbf x)
 :=\sum_{T\in\mathsf{ST}(G)}\prod_{e\in T}w(e)
 =\sum_T\prod_{i\in S}x_i^{\deg_T(i)}.
\]

For a spanning tree \(T\), let \(F=T[W]\). Then \(F\) is a spanning forest of \(G[W]\), and every component of \(F\) meets \(S\): otherwise that component has no possible edge of \(T\) to \(U\), hence cannot be joined to the rest of \(T\).

Let the components of \(F\) be \(C_1,\dots,C_c\), and write
\[
y_j=\sum_{i\in C_j\cap S}x_i,
\qquad
X=\sum_{i\in S}x_i.
\]
After contracting the components of \(F\), the remaining edges of \(T\) form a spanning tree of a complete bipartite multigraph between \(U\) and \(\{C_1,\dots,C_c\}\). The total weight of the parallel edges between a given \(u\in U\) and \(C_j\) is \(y_j\). By (5), their weighted spanning-tree enumerator is
\[
m^{c-1}X^{m-1}\prod_{j=1}^c y_j.
\]

Summing over all possible forests \(F\) gives
\[
Z(\mathbf x)=X^{m-1}Q(\mathbf x),
\tag{9}
\]
where
\[
Q(\mathbf x)
 =
 \sum_F
 m^{c(F)-1}
 \left(\prod_{e\in F}w(e)\right)
 \prod_{C\in\operatorname{comp}(F)}
 \left(\sum_{i\in C\cap S}x_i\right).
\tag{10}
\]
Crucially, \(Q\) has nonnegative coefficients.

Dividing (9) by \(Z(\mathbf 1)=s^{m-1}Q(\mathbf 1)\), we obtain
\[
\mathbb E\prod_{i\in S}x_i^{D_i}
 =
 \left(\frac{x_1+\cdots+x_s}{s}\right)^{m-1}
 \frac{Q(\mathbf x)}{Q(\mathbf 1)}.
\]
Both factors are probability generating functions. The first is that of the multinomial vector \(M\), and the second defines \(Y\). This proves (6). Finally, convolution with an arbitrary probability distribution cannot increase the largest atom, giving (8). ∎

---

## 4. A multinomial atom estimate

### Lemma 3

If
\[
M\sim\operatorname{Mult}\left(N;\frac1s,\dots,\frac1s\right)
\]
and \(N\ge2s\), then
\[
\sup_z\mathbb P(M=z)
 \le
 3(2s)^{s/2}N^{-(s-1)/2}.
\tag{11}
\]

### Proof

A mode has coordinates differing by at most one, so every coordinate \(k_i\) of a mode satisfies
\[
k_i\ge \frac{N}{2s}.
\]
Using the crude Stirling bounds
\[
N!\le 3\sqrt N(N/e)^N,
\qquad
k!\ge \sqrt k(k/e)^k,
\]
we get
\[
\frac{N!}{s^N\prod_i k_i!}
 \le
 \frac{3\sqrt N}{\prod_i\sqrt{k_i}}\,
 \frac{N^N}{s^N\prod_i k_i^{k_i}}.
\]
The last factor is
\[
\exp\left(N\left[H\left(\frac{k_1}{N},\dots,\frac{k_s}{N}\right)
-\log s\right]\right)\le1.
\]
Therefore
\[
\mathbb P(M=(k_i))
 \le
 3\sqrt N\left(\frac{2s}{N}\right)^{s/2},
\]
which is (11). ∎

---

## 5. Proof of Theorem 1

Let \(A\) be a vertex cover of size \(r\), and put \(B=V(G)\setminus A\). Then \(B\) is independent. Partition \(B\) according to exact neighborhood in \(A\). There are at most \(2^r\) classes, so some class \(U\) has common neighborhood \(S\subseteq A\) and
\[
m=|U|\ge\frac{n-r}{2^r}.
\]
Since every vertex in \(U\) has degree at least \(d\),
\[
s=|S|\ge d.
\]

Apply Lemma 2. Write \(N=m-1\), and let \(M\) be the multinomial component of the vector of tree degrees on \(S\).

Every vertex of \(B\) has host-graph degree at most \(r\), and hence tree degree at most \(r\). Consider the event
\[
E=\{\deg_{\mathcal T}(i)>r\text{ for every }i\in S\}.
\]
Since \(D_i\ge M_i\), and \(M_i\sim\operatorname{Bin}(N,1/s)\), if \(N/s\ge2r\), the Chernoff bound gives
\[
\mathbb P(E^c)
 \le
 \sum_{i\in S}\mathbb P(M_i\le r)
 \le
 s\exp\left(-\frac{N}{8s}\right).
\tag{12}
\]

Now fix an abstract tree \(R\). On \(E\), every vertex of \(S\) has degree greater than \(r\). Moreover, every vertex of \(\mathcal T\) having degree greater than \(r\) belongs to \(A\). Thus, if \(\mathcal T\cong R\), the ordered degree vector on the labeled set \(S\) must be obtained by assigning the vertices of \(S\) to at most \(r\) intrinsically specified high-degree vertices of \(R\). There are at most \(r^s\) possible ordered degree vectors.

By Lemmas 2 and 3,
\[
\begin{aligned}
\mathbb P(\mathcal T\cong R,\ E)
&\le r^s\sup_z\mathbb P((D_i)_{i\in S}=z)\\
&\le 3r^s(2s)^{s/2}N^{-(s-1)/2}.
\end{aligned}
\]
Together with (12), this proves (1).

For fixed \(r\), one has \(m=\Omega_r(n)\) and \(s\ge d\), so (2) follows.

If \(r=o(\log n)\), then
\[
\log m\ge \log n-r\log2-o(1)=(1-o(1))\log n,
\]
while
\[
\log\big(r^s(2s)^{s/2}\big)=O(s\log(r+1)).
\]
Consequently the logarithm of the first term in (1) is at most
\[
-\frac{s-1}{2}\log n+O(sr+s\log(r+1))
 =
-\left(\frac12-o(1)\right)(s-1)\log n.
\]
Since \(s\ge d\), this is at most
\[
-\left(\frac12-o(1)\right)(d-1)\log n.
\]
The second term in (1) is exponentially smaller because \(m=n^{1-o(1)}\). This proves (3).

Finally, if \(r=d\), every vertex outside \(A\) has degree at least \(d\) and at most \(d\), hence is adjacent to every vertex of \(A\). Thus \(G=H\vee\overline K_{n-d}\). On \(E\), the high-degree set is exactly \(A\), so the factor \(r^s=d^d\) can be replaced by \(d!\), yielding (4).

---

## 6. A family with linear vertex-cover number

The previous theorem relies on a large independent twin class. The next family shows that the same exponent can also be obtained when the extra degree comes from edges among the large-side vertices.

### Theorem 4

Let \(a=d-1\), let \(B\) have \(m=2q\) vertices, and let \(A\) have \(a\) vertices. Form \(G\) by taking all edges between \(A\) and \(B\), putting a perfect matching on \(B\), and adding no other edges. For \(q\) sufficiently large relative to \(d\),
\[
\sup_R\mathbb P(\mathcal T\cong R)
 =O_d\!\left(n^{-(d-1)/2}\right).
\tag{13}
\]

Here every \(b\in B\) has degree \(a+1=d\), while vertices in \(A\) have degree \(2q\).

### Proof

Let \(D_i=\deg_{\mathcal T}(i)\) for \(i\in A\), and let
\[
K=|E(\mathcal T)\cap E(G[B])|
\]
be the number of matching edges used. Introduce variables \(x_i\) and \(z\), and put \(S=x_1+\cdots+x_a\).

If \(F\) is a \(k\)-edge subset of the perfect matching, then after contracting \(F\), the \(B\)-side consists of \(k\) components of size two and \(m-2k\) singleton components, hence \(m-k\) components in total. Applying (5), the weighted sum of the remaining cross-edge trees is
\[
S^{m-k-1}m^{a-1}\left(\prod_{i=1}^a x_i\right)2^k.
\]
Summing over the \(\binom qk\) choices of \(F\),
\[
\begin{aligned}
Z(\mathbf x,z)
&=\sum_Tz^{K(T)}\prod_{i\in A}x_i^{D_i(T)}\\
&=
m^{a-1}\left(\prod_{i=1}^a x_i\right)
\sum_{k=0}^q\binom qk(2z)^kS^{m-k-1}\\
&=
m^{a-1}\left(\prod_{i=1}^a x_i\right)
S^{q-1}(S+2z)^q.
\end{aligned}
\tag{14}
\]

After normalization,
\[
\mathbb E\left[z^K\prod_{i=1}^a x_i^{D_i-1}\right]
 =
 \left(\frac{S}{a}\right)^{q-1}
 \left(\frac{S+2z}{a+2}\right)^q.
\tag{15}
\]

Thus
\[
K\sim\operatorname{Bin}\left(q,\frac{2}{a+2}\right),
\]
and, conditional on \(K=k\),
\[
(D_i-1:i\in A)
\sim
\operatorname{Mult}\left(2q-k-1;\frac1a,\dots,\frac1a\right).
\]
For fixed \(a\), the largest binomial atom is \(O_a(q^{-1/2})\), while Lemma 3 gives a conditional multinomial atom bound \(O_a(q^{-(a-1)/2})\). Hence
\[
\sup_{\mathbf v,k}
\mathbb P\big((D_i-1)_{i\in A}=\mathbf v,\ K=k\big)
 =
O_a(q^{-a/2}).
\tag{16}
\]

The first factor of (15) also shows that, with probability \(1-e^{-\Omega_a(q)}\), every vertex of \(A\) has tree degree greater than \(d=a+1\). Every vertex of \(B\), by contrast, has tree degree at most \(d\). On this high-probability event, \(A\) is therefore the intrinsic set of vertices of \(\mathcal T\) having degree greater than \(d\).

For a fixed abstract tree \(R\), its isomorphism type then determines:

- the multiset of degrees on \(A\), giving at most \(a!\) ordered vectors;
- the number \(K\), since this is exactly the number of tree edges with both endpoints outside the intrinsic high-degree set.

Using (16),
\[
\mathbb P(\mathcal T\cong R)
 \le a!\,O_a(q^{-a/2})+e^{-\Omega_a(q)}
 =O_d(n^{-(d-1)/2}),
\]
as claimed. ∎

---

## 7. Exact sharpness for \(K_{d,m}\)

For completeness, the exponent can be recovered sharply for the stated extremal example.

### Proposition 5

For fixed \(d\ge2\) and \(m\to\infty\),
\[
\max_R
\mathbb P_{K_{d,m}}(\mathcal T\cong R)
 =
\Theta_d\!\left(m^{-(d-1)/2}\right).
\tag{17}
\]

### Proof

Let \(A\) be the side of size \(d\). Formula (5) gives
\[
\sum_T\prod_{i\in A}x_i^{\deg_T(i)-1}
 =
m^{d-1}(x_1+\cdots+x_d)^{m-1}.
\]
Therefore
\[
(\deg_{\mathcal T}(i)-1:i\in A)
\sim
\operatorname{Mult}\left(m-1;\frac1d,\dots,\frac1d\right).
\tag{18}
\]

Since \(m>d\), the two color classes of an abstract spanning tree have different sizes, so its isomorphism type determines the multiset of degrees on \(A\). Lemma 3 and a union over at most \(d!\) orderings give the upper bound in (17).

For the lower bound, choose a modal vector in (18). Its probability is
\[
\Theta_d(m^{-(d-1)/2})
\]
by Stirling's formula. For every bipartite tree,
\[
\sum_{b\in B}(\deg_T(b)-1)=d-1,
\]
so at most \(d-1\) vertices of \(B\) are nonleaves. Deleting the \(B\)-leaves leaves a core on at most \(2d-1\) vertices. Once the ordered degree vector on \(A\) and this finite core are specified, all numbers of \(B\)-leaves attached to vertices of \(A\) are determined. Hence, for fixed \(d\), the modal degree-vector event is partitioned into only \(O_d(1)\) abstract tree types. One of them has probability \(\Omega_d(m^{-(d-1)/2})\). ∎

---

## 8. Remaining gap

The factorization lemma gives exactly the desired \((s-1)/2\) exponent whenever a large false-twin class with \(s\ge d\) can be found. The bounded-vertex-cover hypothesis then makes the common neighborhood \(S\) recognizable from the abstract sampled tree: its vertices acquire linearly large tree degree, while all vertices outside the cover have bounded degree.

Neither feature is available in a general minimum-degree graph. Such a graph may have:

- no large false-twin class;
- no bounded set of high-degree “hub” vertices;
- all tree degrees on the same scale, so a host-designated set \(S\) can have as many as \(\binom ns\) possible images under an abstract tree isomorphism.

Thus the degree-vector atom bound alone cannot be union-bounded in the unrestricted setting. The matching-join calculation indicates that edges within the large side can supply additional independent half-powers of \(n\), but no general invariant or decomposition yielding all \(d-1\) required fluctuation dimensions is established here. Consequently, this is a genuine special-case proof rather than a proof of the full conjecture.