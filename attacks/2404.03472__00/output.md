```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A polynomial-evaluation construction attains the target when the family size is at most r^A for fixed A, while typical equal-density Bernoulli matrices fail at the conjectured scale.",
  "would_publish": false,
  "caveats": "No uniform bound is obtained for superpolynomial family size; the random obstruction is distributional, not a deterministic lower bound."
}
```

## 1. Intended formulation

Let \(\tau(n,r)\) be the minimum \(t\) for which there is a family
\(\mathcal F=\{F_1,\dots,F_n\}\subseteq 2^{[t]}\) such that, for every \(j\) and every \(R\subseteq[n]\setminus\{j\}\) with \(|R|\le r\),
\[
F_j\not\subseteq \bigcup_{i\in R}F_i.
\]
Equivalently, the incidence matrix is \(r\)-disjunct: for every \(j\) and every \(r\)-set \(R\) of other columns, there is a row containing a \(1\) in column \(j\) and \(0\)'s in all columns indexed by \(R\).

The intended question is whether there is an absolute constant \(C\) such that
\[
\tau(n,r)\le C\,\frac{r^2\log n}{\log r}
\tag{1}
\]
for all \(2\le r<n\).

Without the universal quantifier over \(n\), the literal wording “are there families” is trivial: for example, \(r+1\) singleton sets use \(t=r+1\). The context in terms of \(t(n,1,r)\) makes (1) the meaningful interpretation.

## 2. An algebraic partial result

### Theorem 1

For all \(2\le r<n\),
\[
\tau(n,r)\le
\min\left\{
n,\;
4r^2\left\lceil\log_r n\right\rceil^2,\;
\left\lceil e(r+1)\bigl((r+1)\log n+1\bigr)\right\rceil
\right\}.
\tag{2}
\]

Consequently, for every fixed \(A>1\),
\[
n\le r^A
\quad\Longrightarrow\quad
\tau(n,r)=O_A\!\left(\frac{r^2\log n}{\log r}\right).
\tag{3}
\]
Thus the conjectured order is attained whenever \(n\) is bounded by a fixed power of \(r\). The dependence of the implicit constant on \(A\) is essential in this argument and prevents (3) from resolving the full problem.

### Proof of the algebraic bound

Put
\[
k=\left\lceil \log_r n\right\rceil.
\]
Since \(n>r\), we have \(k\ge2\). Let \(q\) be the smallest power of \(2\) strictly larger than \(r(k-1)\). Then
\[
r(k-1)<q\le 2r(k-1).
\tag{4}
\]

Use the ground set
\[
X=\mathbb F_q\times\mathbb F_q,
\qquad |X|=q^2.
\]
For every polynomial \(f\in\mathbb F_q[x]\) of degree less than \(k\), define its graph
\[
G_f=\{(x,f(x)):x\in\mathbb F_q\}.
\]
There are \(q^k\) such polynomials. Moreover,
\[
q^k\ge r^k\ge n,
\]
so it is enough to prove that the whole family of polynomial graphs is \((1,r)\)-cover-free.

Fix distinct polynomials \(f,g_1,\dots,g_s\), where \(s\le r\). For every \(i\), the nonzero polynomial \(f-g_i\) has at most \(k-1\) roots. Hence
\[
\left|\left\{x\in\mathbb F_q:
f(x)=g_i(x)\text{ for some }i\le s\right\}\right|
\le s(k-1)
\le r(k-1)<q.
\]
There is therefore an \(x\in\mathbb F_q\) such that
\[
f(x)\ne g_i(x)\qquad\text{for every }i.
\]
The point \((x,f(x))\) belongs to \(G_f\) but to none of the \(G_{g_i}\). Thus
\[
G_f\not\subseteq G_{g_1}\cup\cdots\cup G_{g_s}.
\]

Taking any \(n\) of the \(q^k\) graphs gives
\[
\tau(n,r)\le q^2
\le 4r^2(k-1)^2
\le 4r^2\left\lceil\log_r n\right\rceil^2.
\]

If \(x=\log_r n\ge1\), then \(\lceil x\rceil\le2x\), so
\[
\tau(n,r)\le16r^2x^2
=16x\,\frac{r^2\log n}{\log r}.
\]
When \(x\le A\), this proves (3).

### Proof of the probabilistic bound in (2)

Construct a random \(t\times n\) binary matrix with independent entries, each equal to \(1\) with probability
\[
p=\frac1{r+1}.
\]
For a fixed distinguished column \(j\) and fixed \(r\)-set \(R\) of other columns, a row witnesses \(j\) against \(R\) with probability
\[
p(1-p)^r
=
\frac1{r+1}\left(\frac r{r+1}\right)^r
>
\frac1{e(r+1)}.
\]
Thus the probability that no row witnesses this pair is at most
\[
\exp\left(-\frac{t}{e(r+1)}\right).
\]
There are at most
\[
n\binom{n-1}{r}\le n^{r+1}
\]
choices of \((j,R)\). Hence the expected number of unwitnessed pairs is less than \(1\) whenever
\[
t\ge e(r+1)\bigl((r+1)\log n+1\bigr).
\]
A matrix with no bad pair therefore exists. Checking \(r\)-sets suffices for all sets of size at most \(r\), since a smaller set can be extended to an \(r\)-set.

Finally, the singleton family gives \(\tau(n,r)\le n\). This proves (2). \(\square\)

### Quantified remaining factor

Writing
\[
x=\frac{\log n}{\log r},
\]
the two nontrivial bounds in (2) imply
\[
\tau(n,r)
=
O\left(
\frac{r^2\log n}{\log r}
\min\{x,\log r\}
\right).
\tag{5}
\]
Thus the algebraic construction loses a factor \(O(\log_r n)\), while the independent random construction loses \(O(\log r)\). The multiplier in (5) is bounded for \(n\le r^A\), but not uniformly for superpolynomial \(n\).

## 3. A barrier for the most direct random model

The missing logarithmic improvement cannot be obtained by taking a typical binary matrix with one common independent entry density.

### Proposition 2

Fix constants \(C,\varepsilon>0\). Let \(r\to\infty\), let
\[
n=n(r)\ge r^{2+\varepsilon},
\]
and let \(M\) be a \(t\times n\) matrix whose entries are mutually independent Bernoulli random variables with a common, arbitrary parameter \(p=p(r,n)\). If
\[
t\le C\frac{r^2\log n}{\log r},
\tag{6}
\]
then
\[
\Pr(M\text{ is }r\text{-disjunct})\longrightarrow0,
\]
uniformly in \(p\).

This is only a statement about typical equal-density product matrices. It is not a deterministic lower bound and does not rule out highly structured or correlated random constructions.

### Proof

Write
\[
L=\log n,\qquad h=\log r,\qquad \mu=pt.
\]

The cases \(p=0,1\) are immediate, so assume \(0<p<1\).

#### Case 1: \(\mu<h\)

If \(p\le1/2\), a fixed column is empty with probability
\[
(1-p)^t
\ge \exp(-2pt)
>\frac1{r^2}.
\]
The column-empty events are independent, so
\[
\Pr(\text{no empty column})
\le \exp(-n/r^2)
\le \exp(-r^\varepsilon).
\]
An empty column violates disjunctness.

If \(p>1/2\), then \(t<2h\). Therefore
\[
2^t<2^{2\log r}=r^{2\log 2}<r^{2+\varepsilon}\le n.
\]
Every \(t\times n\) binary matrix then has two identical columns, which also violates \(r\)-disjunctness.

#### Case 2: \(\mu\ge h\)

Fix the first column, and let \(S\) be its support, with \(s=|S|\). Chernoff's inequality gives
\[
\Pr(s>2\mu)\le e^{-\mu/3}\le r^{-1/3}.
\tag{7}
\]

Condition on a support \(S\) with \(s\le2\mu\). Let \(N=n-1\), and let \(X\) count the \(r\)-subsets of the other \(N\) columns whose union covers \(S\).

Set
\[
u=(1-p)^r,\qquad a=1-u.
\]
For a fixed \(r\)-subset \(R\), the probability that \(R\) covers \(S\) is \(a^s\).

For two \(r\)-subsets \(R,R'\) with \(|R\cap R'|=k\), the probability, at one row of \(S\), that both unions contain a \(1\) is
\[
b_k=1-2u+(1-p)^{2r-k}
=a^2+u^2\bigl(u^{-k/r}-1\bigr).
\]
By convexity of \(y\mapsto u^{-y}\) on \([0,1]\),
\[
u^{-k/r}-1
\le \frac{k}{r}(u^{-1}-1).
\]
Consequently,
\[
\frac{b_k}{a^2}
\le
1+\frac{k}{r}\frac{u}{1-u}
\le
\exp\left(\frac{k}{r}\frac{u}{1-u}\right).
\tag{8}
\]

Let \(K\) be the intersection size of two independent uniformly chosen \(r\)-subsets of an \(N\)-element set. From (8),
\[
\frac{\mathbb E X^2}{(\mathbb E X)^2}
\le \mathbb E e^{\lambda K},
\qquad
\lambda=\frac{s}{r}\frac{u}{1-u}.
\tag{9}
\]
For \(\lambda\ge0\),
\[
\begin{aligned}
\mathbb E e^{\lambda K}
&=
\sum_{j=0}^r
\binom rj(e^\lambda-1)^j
\frac{(r)_j}{(N)_j}\\
&\le
\left(1+\frac rN(e^\lambda-1)\right)^r\\
&\le
\exp\left(\frac{r^2}{N}(e^\lambda-1)\right).
\end{aligned}
\tag{10}
\]

It remains to bound \(\lambda\). Put \(x=pr\). Since
\[
u=(1-p)^r\le e^{-x},
\]
we have
\[
\frac{x u}{1-u}
\le \frac{x}{e^x-1}
\le1.
\]
Using \(s\le2pt\),
\[
\lambda
\le
\frac{2pt}{r}\frac{u}{1-u}
=
\frac{2t}{r^2}\frac{x u}{1-u}
\le \frac{2t}{r^2}
\le \frac{2CL}{h}.
\tag{11}
\]
Combining (9)--(11), and using \(N\ge n/2\),
\[
\frac{\mathbb E X^2}{(\mathbb E X)^2}
\le
\exp(\delta_r),
\qquad
\delta_r
\le
2r^2 n^{-1+2C/h}.
\]
Because \(n\ge r^{2+\varepsilon}\) and \(2C/h=o(1)\), we have \(\delta_r\to0\).

Paley--Zygmund now gives
\[
\Pr(X>0\mid S)
\ge
\frac{(\mathbb E X)^2}{\mathbb E X^2}
\ge e^{-\delta_r}
=1-o(1).
\]
Thus, with probability \(1-o(1)\), the first column is covered by \(r\) other columns. Together with (7), this proves that \(M\) is not \(r\)-disjunct with probability tending to \(1\). \(\square\)

The same calculation gives a coarse \(\Theta(r^2\log n)\) scale for this random model: for example, when \(n\ge r^4\), every common-density Bernoulli matrix with
\[
t\le \frac18 r^2\log n
\]
is \(r\)-disjunct with probability \(o(1)\), whereas the first-moment construction above succeeds with \(O(r^2\log n)\) rows.

## 4. Remaining gap

The algebraic construction proves the desired bound for every fixed polynomial regime \(n\le r^A\), but its constant grows with \(A\). The independent random construction works for arbitrary \(n\) but uses \(O(r^2\log n)\) rows, and Proposition 2 shows that a typical equal-density product matrix does not recover the missing \(\log r\).

What remains is precisely the regime
\[
r\to\infty,\qquad \log_r n\to\infty,
\]
where one needs a structured family with binary rate
\[
\frac{\log n}{t}=\Omega\left(\frac{\log r}{r^2}\right).
\]
No such construction, nor a counterexample to its existence, is provided here.