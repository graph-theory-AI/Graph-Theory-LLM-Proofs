```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the recolouring interpretation stated in the catalog, a midpoint-splicing and approximate-convexity argument improves the Hamilton-cycle upper bound from O(k^2) to O(k log k) in both complete and complete bipartite graphs.",
  "would_publish": false,
  "caveats": "The exact formal definition of f_h was not supplied, and optimality or literature novelty has not been checked."
}
```

## 1. Precise statement proved

For a \(k\)-edge-colouring \(\gamma\) and a subgraph \(F\), write
\[
\mathbf m_\gamma(F)
   =(m_1(F),\ldots,m_k(F)),
\]
where \(m_j(F)\) is the number of edges of \(F\) of colour \(j\).

If \(|E(F)|=kq\), the minimum number of edges of \(F\) that must be recoloured to make \(F\) colour-balanced is
\[
\rho_\gamma(F)
   =\sum_{j=1}^k (m_j(F)-q)_+
   =\frac12\left\|\mathbf m_\gamma(F)-q\mathbf 1\right\|_1.
\tag{1}
\]

I prove the following.

### Theorem 1

Let \(k\ge2\).

1. Suppose \(K_{n,n}\) is \(k\)-edge-coloured with all colour classes of size \(n^2/k\), and suppose \(k\mid 2n\). Then it contains a Hamilton cycle \(C\) satisfying
   \[
   \rho_\gamma(C)
      \le 8k\bigl(\lceil\log_2 k\rceil+2\bigr).
   \tag{2}
   \]

2. Suppose \(K_N\) is \(k\)-edge-coloured with all colour classes of size \(\binom N2/k\), and suppose \(k\mid N\). Then it contains a Hamilton cycle \(C\) satisfying
   \[
   \rho_\gamma(C)
      \le 8k\bigl(\lceil\log_2 k\rceil+2\bigr)+4k+1.
   \tag{3}
   \]

Consequently, under the recolouring definition described in the catalog,
\[
f_h(C)=O(k\log k)
\]
for Hamilton cycles in both complete and complete bipartite hosts. This is \(o(k^2)\).

The argument is based on a stronger vector-labelled perfect-matching statement.

---

## 2. A vector matching theorem

Let \(X\) be a real \(d\)-dimensional normed space. For an edge-labelling
\[
\lambda:E(K_{r,r})\longrightarrow X,
\]
write
\[
\lambda(M)=\sum_{e\in M}\lambda(e)
\]
for a perfect matching \(M\).

### Theorem 2

If \(\|\lambda(e)\|\le L\) for every edge of \(K_{r,r}\), then there is a perfect matching \(M\) such that
\[
\left\|
 \lambda(M)-\frac1r\sum_{e\in E(K_{r,r})}\lambda(e)
\right\|
 \le
 8Ld\bigl(\lceil\log_2 d\rceil+2\bigr).
\tag{4}
\]

The crucial point is the logarithm. A sequential rounding of a Carathéodory representation would pay an \(O(d)\) error \(d\) times and give \(O(d^2)\). A balanced dyadic rounding tree pays only \(O(\log d)\) weighted levels.

### 2.1. Continuous halving with few cuts

We need the following standard necklace-halving fact.

#### Lemma 3

Let \(f:[0,r]\to\mathbb R^d\) be integrable. There is a measurable set \(A\subseteq[0,r]\), constant on the intervals of a partition with at most \(d\) cut points, such that
\[
\int_A f(x)\,dx=\frac12\int_0^r f(x)\,dx.
\tag{5}
\]

#### Proof

Choose coordinates in \(\mathbb R^d\). For \(x=(x_0,\ldots,x_d)\in S^d\), partition \([0,r]\) into \(d+1\) intervals of respective lengths \(r x_i^2\), and assign the \(i\)-th interval the sign \(\operatorname{sgn}(x_i)\). The signed integral defines a continuous odd map
\[
S^d\longrightarrow\mathbb R^d.
\]
Continuity at \(x_i=0\) follows because the corresponding interval has vanishing length. By the Borsuk–Ulam theorem this map has a zero. Taking \(A\) to be the union of the positively signed intervals gives (5). ∎

### 2.2. Approximate midpoint closure for matching profiles

#### Lemma 4

For any two perfect matchings \(P,Q\) of a vector-labelled \(K_{r,r}\), there is a perfect matching \(R\) such that
\[
\left\|
\lambda(R)-\frac{\lambda(P)+\lambda(Q)}2
\right\|
\le 8Ld.
\tag{6}
\]

#### Proof

Let the bipartition be \(U\cup V\). For \(v\in V\), let \(P(v),Q(v)\in U\) be its neighbours in \(P,Q\). Define a permutation \(\sigma\) of \(V\) by
\[
Q(v)=P(\sigma(v)).
\]
Order the elements of each cycle of \(\sigma\) cyclically, and concatenate these cycle orders.

For the position corresponding to \(v_i\), let \(P_i\) and \(Q_i\) denote its \(P\)- and \(Q\)-edges. On the unit interval \(I_i=[i-1,i]\), put
\[
f(x)=\lambda(P_i)-\lambda(Q_i).
\]
Apply Lemma 3. Let
\[
\alpha_i=|A\cap I_i|.
\]
Then
\[
\sum_i \alpha_i\bigl(\lambda(P_i)-\lambda(Q_i)\bigr)
 =
\frac12\sum_i\bigl(\lambda(P_i)-\lambda(Q_i)\bigr).
\tag{7}
\]

At most \(d\) of the unit intervals contain a cut point. Call these intervals exceptional and let their number be \(F\le d\). On every nonexceptional interval let \(s_i\in\{0,1\}\) be its membership value in \(A\); choose \(s_i\) arbitrarily on exceptional intervals.

Consider the preliminary edge set that chooses \(P_i\) when \(s_i=1\) and \(Q_i\) when \(s_i=0\). Its label sum \(\lambda_0\) satisfies, by (7),
\[
\begin{aligned}
\left\|\lambda_0-\frac{\lambda(P)+\lambda(Q)}2\right\|
&=
\left\|
 \sum_i(s_i-\alpha_i)
 \bigl(\lambda(P_i)-\lambda(Q_i)\bigr)
\right\|  \\
&\le 2LF
 \le 2Ld.
\end{aligned}
\tag{8}
\]

The preliminary edge set has degree one at every vertex of \(V\), but may have degrees zero or two in \(U\). On each cycle of \(\sigma\), such defects occur exactly where the cyclic binary sequence \((s_i)\) changes value.

Away from exceptional positions, changes can only occur at one of the at most \(d\) continuous cut points. Rounding an exceptional position creates at most two further linear changes. Thus there are at most \(d+2F\) changes inside the concatenated cycle blocks. Closing each block cyclically at most doubles this number. Hence the number \(b\) of cyclic changes satisfies
\[
b\le 2(d+2F)\le 6d.
\tag{9}
\]

There are exactly \(b/2\) vertices of \(U\) of degree two and \(b/2\) of degree zero. Delete one selected edge at every degree-two vertex. This frees \(b/2\) vertices of \(V\), which can be matched arbitrarily to the degree-zero vertices of \(U\), since the host is complete bipartite. Thus only \(b/2\) edges are replaced. Their total effect on the label sum has norm at most
\[
2L\cdot\frac b2=Lb\le6Ld.
\tag{10}
\]
Combining (8) and (10) gives (6). ∎

### 2.3. Approximate convexification

#### Lemma 5

Let \(S\) be a finite subset of a normed space. Suppose that for every \(x,y\in S\), there is \(z\in S\) with
\[
\left\|z-\frac{x+y}{2}\right\|\le D.
\tag{11}
\]
If \(x\in\operatorname{conv}(S)\) is a convex combination of at most \(m\) points of \(S\), then
\[
\operatorname{dist}(x,S)
 \le
D\bigl(\lceil\log_2(m-1)\rceil+2\bigr)
\tag{12}
\]
for \(m\ge2\).

#### Proof

First suppose all coefficients are dyadic with denominator \(2^s\). Form \(2^s\) leaves of a complete binary tree, arranging equal points in contiguous blocks. At every internal node apply (11) to the representatives of its two children. If all leaves below a node are equal, use that common point and incur no error.

At depth \(j\), every heterogeneous node contains a boundary between two contiguous blocks. Therefore the number \(H_j\) of heterogeneous nodes satisfies
\[
H_j\le \min(2^j,m-1).
\]
An error made at depth \(j\) reaches the root with coefficient \(2^{-j}\). Hence the total error is at most
\[
D\sum_{j\ge0}2^{-j}H_j
 \le
D\sum_{j\ge0}\min\bigl(1,(m-1)2^{-j}\bigr)
 \le
D\bigl(\lceil\log_2(m-1)\rceil+2\bigr).
\]

For arbitrary coefficients, approximate them by dyadic coefficients. Since \(S\) is finite, a subsequence of the resulting root representatives is constant, and passage to the limit gives the same bound. ∎

### 2.4. Proof of Theorem 2

Let
\[
\mathcal P=\{\lambda(M):M\text{ is a perfect matching of }K_{r,r}\}.
\]
Lemma 4 says that \(\mathcal P\) satisfies Lemma 5 with \(D=8Ld\).

For a uniformly random perfect matching, every edge is selected with probability \(1/r\). Consequently,
\[
\mu:=\frac1r\sum_{e\in E(K_{r,r})}\lambda(e)
   =\mathbb E[\lambda(M)]
   \in\operatorname{conv}(\mathcal P).
\]
By Carathéodory's theorem, \(\mu\) is a convex combination of at most \(d+1\) elements of \(\mathcal P\). Lemma 5 therefore gives
\[
\operatorname{dist}(\mu,\mathcal P)
 \le 8Ld\bigl(\lceil\log_2d\rceil+2\bigr),
\]
which is (4). ∎

---

## 3. Complete bipartite Hamilton cycles

Let the parts of \(K_{n,n}\) be
\[
A=\{a_1,\ldots,a_n\},\qquad B,
\]
where the \(a_i\) are cyclically ordered and \(a_{n+1}=a_1\).

Construct an auxiliary \(K_{n,n}\) whose left vertices are the \(n\) gaps
\[
g_i=(a_i,a_{i+1})
\]
and whose right vertices are \(B\). Give the auxiliary edge \(g_i b\) the vector label
\[
\lambda(g_i b)
 =
e_{\gamma(a_i b)}+e_{\gamma(a_{i+1}b)}
 \in(\mathbb R^k,\|\cdot\|_1).
\tag{13}
\]
Every such label has \(\ell_1\)-norm at most \(2\).

A perfect matching of the auxiliary graph assigns a distinct vertex \(b_i\in B\) to every gap and produces the Hamilton cycle
\[
a_1b_1a_2b_2\cdots a_nb_na_1.
\tag{14}
\]
Its colour-count vector is exactly the sum of the corresponding auxiliary labels.

Every original edge \(a_i b\) appears in exactly two labels in (13), one for each gap incident with \(a_i\). Therefore
\[
\frac1n\sum_{i,b}\lambda(g_i b)
 =
\frac2n\bigl(|E_1|,\ldots,|E_k|\bigr).
\tag{15}
\]
For a globally colour-balanced colouring, \(|E_j|=n^2/k\), so the right-hand side is
\[
\frac{2n}{k}\mathbf1,
\]
the desired Hamilton-cycle profile.

Apply Theorem 2 with \(d=k\) and \(L=2\). We obtain a Hamilton cycle \(C\) with
\[
\left\|
\mathbf m_\gamma(C)-\frac{2n}{k}\mathbf1
\right\|_1
\le
16k\bigl(\lceil\log_2k\rceil+2\bigr).
\]
Equation (1) gives (2).

---

## 4. Complete graphs

The only additional issue is to find a nearly colour-balanced near-bisection.

### Lemma 6

Let the edges of \(K_N\) be partitioned into \(k\) classes of equal size. Put
\[
a=\left\lceil\frac N2\right\rceil,
\qquad
b=\left\lfloor\frac N2\right\rfloor.
\]
There is a partition \(V(K_N)=A\cup B\), with \(|A|=a\), \(|B|=b\), such that, if \(x_j\) is the number of colour-\(j\) edges between \(A\) and \(B\), then
\[
\left\|
(x_1,\ldots,x_k)-\frac{ab}{k}\mathbf1
\right\|_1
\le 2kN.
\tag{16}
\]

#### Proof

Choose \(A\) uniformly among the \(a\)-subsets. For an edge \(e\), let \(I_e\) be its crossing indicator. Then
\[
p:=\mathbb P(I_e=1)=\frac{2ab}{N(N-1)}.
\]

For two adjacent edges,
\[
\mathbb P(I_e=I_f=1)=\frac p2,
\]
so
\[
\operatorname{Cov}(I_e,I_f)=p(1/2-p)\le0,
\]
because \(p\ge1/2\).

For two disjoint edges, direct calculation gives
\[
\operatorname{Cov}(I_e,I_f)=
\begin{cases}
\dfrac{N}{2(N-1)^2(N-3)},&N\ \text{even},\\[6pt]
\dfrac{N+1}{2N^2(N-2)},&N\ \text{odd}.
\end{cases}
\tag{17}
\]
For \(N\ge4\), these quantities are at most \(4/N^2\). If \(G\) is any graph on these \(N\) vertices and \(X\) is its number of crossing edges, then, writing \(m=|E(G)|\),
\[
\operatorname{Var}X
 \le \frac m4+m^2\frac4{N^2}
 <2N^2.
\tag{18}
\]
The small case \(N=3\) is immediate.

For the \(j\)-th colour graph,
\[
\mathbb E x_j
 =p\frac{\binom N2}{k}
 =\frac{ab}{k}.
\]
Thus
\[
\mathbb E\sum_{j=1}^k
 \left(x_j-\frac{ab}{k}\right)^2
 \le 2kN^2.
\]
Some partition therefore satisfies this inequality. By Cauchy–Schwarz,
\[
\sum_{j=1}^k
 \left|x_j-\frac{ab}{k}\right|
 \le
\sqrt{k}\sqrt{2kN^2}
 \le 2kN,
\]
which proves (16). ∎

### Construction of the Hamilton cycle

Choose the partition from Lemma 6 and cyclically order
\[
A=\{a_1,\ldots,a_a\}.
\]

If \(N\) is even, then \(a=b\). If \(N\) is odd, then \(a=b+1\); in this case adjoin a dummy symbol \(\ast\) to \(B\), so in either case
\[
|B^\ast|=a.
\]

Again form an auxiliary \(K_{a,a}\) between the gaps \(g_i=(a_i,a_{i+1})\) and \(B^\ast\). For \(v\in B\), put
\[
\lambda(g_i v)
 =
e_{\gamma(a_i v)}+e_{\gamma(a_{i+1}v)}.
\tag{19}
\]
If \(N\) is odd, put
\[
\lambda(g_i\ast)=e_{\gamma(a_i a_{i+1})}.
\tag{20}
\]
All labels have \(\ell_1\)-norm at most \(2\).

A perfect matching inserts each real vertex \(v\in B\) into its assigned gap and, in the odd case, leaves the dummy-assigned gap as the direct edge \(a_i a_{i+1}\). This always gives a Hamilton cycle of \(K_N\).

Let
\[
x=(x_1,\ldots,x_k)
\]
be the crossing-edge profile of \(A,B\). In the odd case let \(y\) be the colour profile of the \(a\) cyclic gap edges \(a_i a_{i+1}\). The average auxiliary matching profile is
\[
\mu=
\begin{cases}
\dfrac2a x,&N\text{ even},\\[8pt]
\dfrac2a x+\dfrac1a y,&N\text{ odd}.
\end{cases}
\tag{21}
\]

If \(N\) is even, \(2b=N\); if \(N\) is odd, \(2b=N-1\). Using (16) and \(a\ge N/2\), we obtain
\[
\left\|\mu-\frac Nk\mathbf1\right\|_1
 \le 8k+2.
\tag{22}
\]
For odd \(N\), the additional \(2\) follows because both \(y/a\) and \(k^{-1}\mathbf1\) are probability vectors, so their \(\ell_1\)-distance is at most \(2\).

Applying Theorem 2 to the auxiliary graph with \(d=k\) and \(L=2\) gives a matching, and hence a Hamilton cycle \(C\), satisfying
\[
\left\|\mathbf m_\gamma(C)-\mu\right\|_1
 \le
16k\bigl(\lceil\log_2k\rceil+2\bigr).
\]
Together with (22),
\[
\left\|
\mathbf m_\gamma(C)-\frac Nk\mathbf1
\right\|_1
\le
16k\bigl(\lceil\log_2k\rceil+2\bigr)+8k+2.
\]
Equation (1) now gives (3).

---

## 5. Status and remaining gaps

The argument above is self-contained for the following standard interpretation:

- the host colouring has equally large colour classes;
- \(f_h(C)\) is the worst-case minimum number of edges of a Hamilton cycle that must be recoloured to make its colour counts equal;
- divisibility conditions necessary for an exactly balanced cycle are imposed.

It establishes the strict asymptotic improvement
\[
O(k^2)\quad\longrightarrow\quad O(k\log k).
\]

It does **not** determine the correct order. In particular, nothing here rules out an \(O(k)\) bound. I also have not audited the exact notation and any stronger vector-label hypotheses in the source paper, nor checked whether its later version already contains this dyadic approximate-convexity observation.