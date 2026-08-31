```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A third-moment inequality proves the conjecture for every regular graph of degree at least three and for broader bounded-irregularity and dense regimes.",
  "would_publish": false,
  "caveats": "The general sparse, highly irregular case, including arbitrary bicyclic graphs, remains open; novelty of the partial bounds was not independently checked."
}
```

# Partial resolution

## 1. Statement

Let \(G\) be a simple graph with adjacency eigenvalues
\[
\lambda_1\ge \cdots\ge \lambda_n,
\]
and put
\[
s^+(G)=\sum_{\lambda_i>0}\lambda_i^2,\qquad
s^-(G)=\sum_{\lambda_i<0}\lambda_i^2.
\]
The conjecture asks whether every connected graph of order \(n\) and size \(m\ge n+1\) satisfies
\[
s^+(G)\ge n.
\]

I do not obtain a proof in full. I prove a quantitative spectral inequality and deduce, in particular, the conjecture for all regular graphs of degree at least \(3\), including regular graphs of arbitrarily large diameter which contain induced claws.

---

## 2. A third-moment/rank inequality

Write
\[
P=s^+(G),\qquad N=s^-(G),\qquad \rho=\lambda_1(G),
\]
let \(\tau=\tau(G)\) be the number of triangles, and let
\[
r=\operatorname{rank} A(G).
\]

### Theorem 1

For every nonempty simple graph,
\[
\boxed{\quad
\bigl(\rho P-6\tau\bigr)^2
   \ge \frac{2m}{r}\,\frac{N^3}{P}.
\quad} \tag{1}
\]

Consequently, if
\[
\bar d=\frac{2m}{n},\qquad \eta=\frac rn,
\]
then
\[
\boxed{\quad
\frac{s^+(G)}n
\ge
\frac{\bar d^{4/3}}
{\bar d^{1/3}+\eta^{1/3}\rho^{2/3}}
\ge
\frac{\bar d^{4/3}}
{\bar d^{1/3}+\rho^{2/3}}.
\quad} \tag{2}
\]

A triangle-sensitive implicit version is the following. If
\[
y=\frac{P}{n},\qquad a=\frac{6\tau}{n},
\]
then
\[
\boxed{\quad
(\rho y-a)^2
\ge
\frac{\bar d}{\eta}\,
\frac{(\bar d-y)^3}{y}.
\quad} \tag{3}
\]

### Proof

Let the positive eigenvalues be \(a_1,\ldots,a_p>0\), and write the negative eigenvalues as \(-b_1,\ldots,-b_q\), where \(b_j>0\). Thus \(p+q=r\). Put
\[
S=\sum_i a_i=\sum_j b_j,
\]
where equality follows from \(\operatorname{tr}A=0\), and put
\[
T_+=\sum_i a_i^3,\qquad T_-=\sum_j b_j^3.
\]

Since \(\operatorname{tr}A^3=6\tau\),
\[
T_+-T_-=6\tau.
\]
Moreover \(a_i\le \rho\), so
\[
T_+\le \rho\sum_i a_i^2=\rho P.
\]
Therefore
\[
0<T_-\le \rho P-6\tau. \tag{4}
\]

Cauchy--Schwarz gives
\[
N^2
 =\left(\sum_j b_j^{1/2}b_j^{3/2}\right)^2
 \le \left(\sum_jb_j\right)\left(\sum_jb_j^3\right)
 =S T_-.
\]
Also \(S^2\le pP\), and hence
\[
N^4\le pP\,T_-^2. \tag{5}
\]

The power-mean inequality gives
\[
\left(\sum_jb_j^2\right)^{3/2}
 \le q^{1/2}\sum_jb_j^3,
\]
and therefore
\[
N^3\le qT_-^2. \tag{6}
\]

Dividing (5) by \(P\), adding (6), and using \(P+N=2m\), we obtain
\[
\frac{N^4}{P}+N^3
 =\frac{(P+N)N^3}{P}
 =\frac{2mN^3}{P}
 \le (p+q)T_-^2
 =rT_-^2.
\]
Together with (4), this proves (1).

For (3), substitute
\[
P=ny,\qquad N=n(\bar d-y),\qquad r=n\eta
\]
into (1), and divide by \(n^2\).

Finally, since \(0\le \rho P-6\tau\le \rho P\), (1) implies
\[
\rho^2P^3\ge \frac{2m}{r}N^3.
\]
Taking cube roots and substituting \(N=n\bar d-P\) gives
\[
\rho^{2/3}P
 \ge \left(\frac{\bar d}{\eta}\right)^{1/3}(n\bar d-P).
\]
Solving for \(P/n\) yields (2). ∎

---

## 3. A sufficient condition for the conjecture

### Corollary 2

Suppose \(m\ge n+1\), so \(\bar d>2\). If either
\[
\frac{6\tau}{n}\ge \rho, \tag{7}
\]
or
\[
\boxed{\quad
\eta\left(\rho-\frac{6\tau}{n}\right)^2
 \le \bar d(\bar d-1)^3,
\quad} \tag{8}
\]
then
\[
s^+(G)\ge n.
\]

In particular, either of the following more readily checkable conditions suffices:
\[
\eta\left(\Delta-\frac{6\tau}{n}\right)_+^2
 \le \bar d(\bar d-1)^3, \tag{9}
\]
or, more simply,
\[
\boxed{\quad
\eta\Delta^2\le \bar d(\bar d-1)^3.
\quad} \tag{10}
\]

Here \(\Delta\) is the maximum degree and \(x_+=\max\{x,0\}\).

### Proof

Condition (7) gives
\[
P\ge \frac{6\tau}{\rho}\ge n
\]
directly from (4).

Now suppose \(a=6\tau/n<\rho\), and assume for contradiction that \(y=P/n<1\). Since \(\rho y-a\ge0\), the left side of (3) is at most
\[
(\rho-a)^2.
\]
On the other hand, because \(\bar d>1\), the function
\[
z\longmapsto \frac{(\bar d-z)^3}{z}
\]
is strictly decreasing on \((0,\bar d)\). Thus
\[
\frac{\bar d}{\eta}\frac{(\bar d-y)^3}{y}
>
\frac{\bar d}{\eta}(\bar d-1)^3.
\]
This contradicts (3) and (8).

For (9), if \(a\ge\rho\) there is nothing to prove. Otherwise
\[
0<\rho-a\le\Delta-a.
\]
Condition (10) is the triangle-free weakening of (9). ∎

---

## 4. Regular graphs

### Corollary 3

Every connected \(d\)-regular graph with \(d\ge3\) satisfies
\[
\boxed{\quad
s^+(G)
\ge
\frac{d}{1+d^{1/3}}\,n
>n.
\quad} \tag{11}
\]

Hence the conjecture holds for every regular graph to which it applies.

### Proof

For a \(d\)-regular graph,
\[
\bar d=\rho=d.
\]
Equation (2) gives
\[
\frac{s^+(G)}n
\ge
\frac{d^{4/3}}{d^{1/3}+\eta^{1/3}d^{2/3}}
=
\frac{d}{1+(\eta d)^{1/3}}
\ge
\frac{d}{1+d^{1/3}}.
\]
For every integer \(d\ge3\),
\[
d>1+d^{1/3},
\]
equivalently \((d-1)^3>d\). Thus the last expression is greater than \(1\). ∎

For cubic graphs this gives the explicit estimate
\[
s^+(G)\ge \frac{3}{1+\sqrt[3]{3}}\,n
   \approx 1.228\,n.
\]

This is genuinely beyond the two classes listed in the source paper. For example, the odd prism graphs
\[
C_{2k+1}\square K_2,\qquad k\ge3,
\]
are cubic, nonbipartite, have diameter greater than \(2\), and contain induced claws.

---

## 5. Bounded irregularity and dense graphs

### Corollary 4

The conjecture holds whenever
\[
\Delta^2\le \bar d(\bar d-1)^3. \tag{12}
\]

In particular, it holds for:

1. every graph with minimum degree at least \(3\) and maximum degree at most \(4\);
2. every graph with minimum degree at least \(4\) and maximum degree at most \(10\).

Indeed, \(x(x-1)^3\) is increasing for \(x>1\), and
\[
4^2=16<3\cdot2^3=24,
\]
while
\[
10^2=100<4\cdot3^3=108.
\]

### Corollary 5

The conjecture holds if
\[
\bar d\ge 1+n^{1/3}. \tag{13}
\]
Equivalently, it holds in the density range
\[
m\ge \frac n2\bigl(1+n^{1/3}\bigr).
\]

### Proof

We first prove the elementary spectral-radius estimate
\[
\rho^2\le 2m-n+1. \tag{14}
\]
Let \(x>0\) be a Perron eigenvector, and choose \(v\) with \(x_v=\max_wx_w\). Then
\[
\rho^2x_v
 =(A^2x)_v
 \le x_v\sum_{u\in N(v)}d(u).
\]
Since \(G\) is connected, every vertex outside \(N(v)\), apart from \(v\) itself, has degree at least \(1\). Hence
\[
\sum_{u\in N(v)}d(u)\le 2m-n+1,
\]
which proves (14).

Put \(x=\bar d-1\). Then
\[
2m-n+1=nx+1.
\]
If \(x^3\ge n\), then
\[
nx+1\le n(x+1)\le x^3(x+1)=\bar d(\bar d-1)^3.
\]
Thus
\[
\rho^2\le \bar d(\bar d-1)^3,
\]
and Corollary 2 applies. ∎

The \(O(n^{4/3})\) edge threshold improves the immediate spectral-radius argument \(s^+\ge\rho^2\ge\bar d^2\), which only proves the conjecture at density \(m=\Omega(n^{3/2})\).

---

## 6. A separate sparse structural case

The following pinching observation gives another class, relevant when the moment criterion is weak.

### Lemma 6

If \(V(G)=V_1\dot\cup\cdots\dot\cup V_k\), then
\[
s^+(G)\ge \sum_{i=1}^k s^+(G[V_i]). \tag{15}
\]

### Proof

For a real symmetric matrix \(M\), let
\[
F(M)=\operatorname{tr}(M_+^2).
\]
The variational formula
\[
F(M)=\max_{X\succeq0}
 \left(2\operatorname{tr}(MX)-\operatorname{tr}(X^2)\right)
\]
shows that \(F\) is convex and orthogonally invariant.

Let \(D_\varepsilon\) be a random diagonal matrix which is constant, with an independent sign \(\varepsilon_i\in\{\pm1\}\), on each \(V_i\). Then
\[
\mathbb E_\varepsilon[D_\varepsilon A D_\varepsilon]
 =\bigoplus_i A(G[V_i]).
\]
Convexity and orthogonal invariance give
\[
F\left(\bigoplus_iA(G[V_i])\right)
 \le \mathbb E_\varepsilon F(D_\varepsilon AD_\varepsilon)
 =F(A).
\]
This is (15). ∎

### Proposition 7

If \(G\) contains a triangle \(T\) such that
\[
H=G-V(T)
\]
is bipartite and
\[
e(H)\ge |V(H)|-1,
\]
then
\[
s^+(G)\ge n.
\]

In particular, it suffices that \(G-V(T)\) be connected and bipartite.

### Proof

The triangle has spectrum \(2,-1,-1\), so
\[
s^+(K_3)=4.
\]
For a bipartite graph \(H\), the adjacency spectrum is symmetric about \(0\), and hence
\[
s^+(H)=e(H).
\]
By Lemma 6,
\[
s^+(G)\ge 4+s^+(H)
 =4+e(H)
 \ge4+(n-3)-1=n.
\]
∎

This includes sparse graphs of arbitrarily large diameter and with induced claws, provided a suitable triangle has bipartite connected complement.

---

## 7. What remains open

The argument does not settle the conjecture in its most delicate range \(m=n+1\). In particular, it does not cover arbitrary bicyclic graphs with pendant trees or long bridge structures.

Any counterexample not already covered above would necessarily satisfy, with
\[
\bar d=\frac{2m}{n},\quad
\eta=\frac{\operatorname{rank}A}{n},\quad
a=\frac{6\tau}{n},
\]
all of
\[
a<\rho,\qquad
\eta(\rho-a)^2>\bar d(\bar d-1)^3,\qquad
\rho^2<n.
\]
It would therefore have to be both sparse and spectrally irregular. The moment inequality alone is insufficient for such graphs. For example, a star with two disjoint edges added among its leaves has \(m=n+1\), \(\bar d\to2\), and \(\rho^2\asymp n\), so condition (8) fails badly. That particular family has diameter \(2\) and is covered by the source paper, but it illustrates the obstruction to completing the proof by the present method.

No counterexample is produced, and no claim is made that Theorem 1 is new to the literature without a separate literature check.