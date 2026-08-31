```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A star construction strengthens the general lower bound to f(k) at least k+1, while a common-neighborhood reduction gives exponent k+O(s^2) when the forest vertices occupy extension types of span s.",
  "would_publish": false,
  "caveats": "The unrestricted case can have span s=k, so the linear-versus-quadratic gap remains; the catalog and abstract also use inconsistent numerical normalizations."
}
```

# Mathematical writeup

## 1. Definitions and statement of the partial results

Write \(r(D)\) for the least \(N\) such that every tournament on \(N\) vertices contains \(D\) as a not-necessarily-induced subdigraph.

Let \(D\) be an acyclic \(k\)-extension of an oriented forest \(F\). Thus
\[
V(D)=V(F)\mathbin{\dot\cup}Q,\qquad |Q|=k,
\]
and every vertex of \(Q\) is adjacent to every other vertex of \(D\). Since \(D\) is acyclic, after relabelling,
\[
Q=\{q_1,\ldots,q_k\},\qquad q_i\to q_j\quad\text{for }i<j.
\]

For each \(x\in V(F)\), there is a unique type
\[
\tau(x)\in\{0,\ldots,k\}
\]
such that
\[
q_j\to x\quad\Longleftrightarrow\quad j\leq \tau(x).
\]
Indeed, the set of \(q_j\) which dominate \(x\) must be an initial segment: otherwise \(i<j\), \(x\to q_i\), and \(q_j\to x\) would give the directed triangle
\[
q_i\to q_j\to x\to q_i.
\]

The following are the main partial conclusions.

### Theorem A: improved general lower bound

For every fixed \(k\),
\[
\sup_{\substack{F\text{ forest}\\ |F|=n}}\ 
\sup_{\substack{D\text{ a }k\text{-extension of }F}}r(D)
\geq 2^{k+1}n-o(n).
\]
Consequently, under the binary normalization in the question,
\[
\boxed{f(k)\geq k+1.}
\]

This strengthens the lower bound obtained directly from \(k\)-extensions of an arcless graph by one in the exponent.

### Theorem B: stripping extension vertices outside the occupied type interval

Let
\[
a=\min_{x\in V(F)}\tau(x),\qquad
b=\max_{x\in V(F)}\tau(x),\qquad
s=b-a.
\]
Let
\[
D_0=D\big[V(F)\cup\{q_{a+1},\ldots,q_b\}\big].
\]
Then \(D_0\) is an \(s\)-extension of \(F\), and
\[
\boxed{r(D)\leq 2^{k-s}\bigl(r(D_0)+1\bigr)-1.}
\]

In particular, if all forest vertices have the same type, so \(s=0\), then
\[
\boxed{r(D)\leq 2^k\bigl(r(F)+1\bigr)-1.}
\]
Thus the dependence on \(k\) is optimal up to an absolute multiplicative constant for this subclass.

More generally, if the quoted \(s\)-extension upper bound has the form
\[
r(D_0)\leq A_s n,
\]
then
\[
r(D)\leq 2^{k-s}(A_s+1)n.
\]
Using a quadratic-exponent estimate \(A_s=2^{O(s^2)}\), this becomes
\[
r(D)\leq 2^{k+O(s^2)}n.
\]
Hence the conjectured \(2^{O(k)}n\) bound holds whenever \(s=O(\sqrt{k})\), and in particular whenever \(s\) is fixed.

---

## 2. A common-neighborhood lemma

Define
\[
\Phi_t(M)=2^t(M+1)-1.
\]

### Lemma 1

Every tournament on at least \(\Phi_t(M)\) vertices contains a transitive \(t\)-vertex subtournament \(A\) and a set \(U\) of \(M\) further vertices such that
\[
A\to U.
\]

By reversing every arc, the analogous assertion with \(U\to A\) also holds.

#### Proof

We induct on \(t\). For \(t=0\), take any \(M\) vertices.

Suppose \(t\geq1\). Since
\[
\Phi_t(M)=2\Phi_{t-1}(M)+1,
\]
a tournament on \(\Phi_t(M)\) vertices has a vertex \(v\) with
\[
d^+(v)\geq \Phi_{t-1}(M).
\]
Apply the induction hypothesis inside \(N^+(v)\). We obtain a transitive \((t-1)\)-set \(A'\) and an \(M\)-set \(U\) such that
\[
A'\to U.
\]
As \(v\to A'\cup U\), the set
\[
A=\{v\}\cup A'
\]
is transitive and satisfies \(A\to U\). ∎

The useful composition identity is
\[
\Phi_p(\Phi_q(M))=\Phi_{p+q}(M).
\]

---

## 3. Proof of the type-span reduction

Recall that every forest vertex has type between \(a\) and \(b\). Therefore:

- \(q_1,\ldots,q_a\) dominate every vertex of \(D_0\);
- every vertex of \(D_0\) dominates \(q_{b+1},\ldots,q_k\).

Put
\[
p=a,\qquad q=k-b,
\]
so that
\[
p+q=k-(b-a)=k-s.
\]

Let \(M=r(D_0)\), and let \(T\) be a tournament on
\[
\Phi_{p+q}(M)
\]
vertices. Apply Lemma 1 first to obtain a transitive \(p\)-set \(P\) with a common outneighborhood \(W\) of size \(\Phi_q(M)\). Thus
\[
P\to W.
\]

Inside \(T[W]\), apply the reversed form of Lemma 1. We obtain a transitive \(q\)-set \(R\) and a set \(U\) of size \(M\) such that
\[
U\to R.
\]
Since \(P\to W\), we also have
\[
P\to U\cup R.
\]

By the definition of \(M\), the tournament \(T[U]\) contains \(D_0\). Together with \(P\) and \(R\), this gives a copy of \(D\). Hence
\[
r(D)\leq \Phi_{p+q}(M)
=2^{k-s}(M+1)-1.
\]
This proves Theorem B.

### Consequences

If every \(s\)-extension of an \(n\)-vertex forest is \(A_s n\)-unavoidable, then
\[
r(D)\leq 2^{k-s}(A_s n+1)-1
\leq 2^{k-s}(A_s+1)n.
\]

Under the catalog’s normalization
\[
A_s=2^{B(s)},\qquad
B(s)=\binom{2s+2}{2}=2s^2+3s+1,
\]
this gives the finite-size binary exponent
\[
k-s+\log_2(2^{B(s)}+1)
<k-s+B(s)+1
=k+2s^2+2s+2.
\]
Asymptotically in \(n\), the harmless \(+1\) disappears and the exponent is
\[
k-s+B(s)=k+2s^2+2s+1.
\]

The literal bound in the supplied abstract is instead
\[
A_s=2\cdot 3^{(s+1)(2s+1)}.
\]
With that normalization the same reduction gives exponent
\[
k-s+\log_2\!\left(2\cdot 3^{(s+1)(2s+1)}+1\right)
=k+O(s^2).
\]
The structural reduction is independent of this numerical discrepancy.

---

## 4. A star construction giving \(f(k)\geq k+1\)

Let \(F_n\) be the out-star on \(n\) vertices, with center \(c\), leaves
\[
L=\{\ell_1,\ldots,\ell_{n-1}\},
\]
and arcs
\[
c\to \ell_j.
\]

Add \(k\) universal vertices \(q_1,\ldots,q_k\) and orient all relevant arcs as
\[
q_1\to q_2\to\cdots\to q_k\to c,
\qquad
q_i\to \ell_j
\]
for every \(i,j\). Call the resulting \(k\)-extension \(D_{k,n}\).

The set
\[
A=\{q_1,\ldots,q_k,c\}
\]
induces a transitive tournament of order \(k+1\), and all its vertices dominate all \(n-1\) leaves. Consequently, a tournament contains \(D_{k,n}\) if and only if it contains a transitive \((k+1)\)-set with at least \(n-1\) common outneighbors.

### Upper bound for this family

Apply Lemma 1 with
\[
t=k+1,\qquad M=n-1.
\]
It gives
\[
r(D_{k,n})
\leq \Phi_{k+1}(n-1)
=2^{k+1}n-1.
\]

### Matching probabilistic lower bound

Fix \(r=k+1\) and put \(m=n-1\). Let
\[
N=\left\lfloor(2^r-\varepsilon)m\right\rfloor
\]
for fixed \(\varepsilon>0\), and take a uniformly random tournament on \(N\) vertices.

For any fixed ordered \(r\)-tuple \(\mathbf v\), the number \(X_{\mathbf v}\) of common outneighbors outside the tuple has distribution
\[
X_{\mathbf v}\sim \operatorname{Bin}(N-r,2^{-r}).
\]
For sufficiently large \(m\),
\[
\mathbb E X_{\mathbf v}
\leq \left(1-\frac{\varepsilon}{2^{r+1}}\right)m.
\]
A Chernoff bound therefore gives a constant \(c=c(r,\varepsilon)>0\) such that
\[
\Pr(X_{\mathbf v}\geq m)\leq e^{-cm}.
\]
There are at most \(N^r\) ordered \(r\)-tuples. Hence
\[
\Pr\bigl(\exists\mathbf v:X_{\mathbf v}\geq m\bigr)
\leq N^r e^{-cm}=o(1).
\]
In particular, with positive probability no transitive \(r\)-tuple has \(m\) common outneighbors. Such a tournament avoids \(D_{k,n}\). Letting \(\varepsilon\to0\) gives
\[
r(D_{k,n})\geq 2^{k+1}n-o(n).
\]

Together with the upper bound,
\[
\boxed{r(D_{k,n})=(2^{k+1}+o(1))n.}
\]

Therefore any function satisfying the requirement in the problem must obey
\[
2^{f(k)}\geq 2^{k+1},
\]
and hence
\[
\boxed{f(k)\geq k+1.}
\]

Equivalently, this can be viewed as moving one universal vertex from a hard \((k+1)\)-extension of an arcless graph into the forest: that vertex and the arcless vertices form an oriented star, while the remaining \(k\) vertices are still universal.

---

## 5. What this resolves and what remains open

For extensions whose forest vertices occupy types of bounded span \(s\), the lower and upper exponents are
\[
k+1\leq f_s(k)\leq k+O(s^2).
\]
Thus for every fixed \(s\),
\[
f_s(k)=k+O_s(1),
\]
and for \(s=O(\sqrt{k})\) the correct order is \(\Theta(k)\).

However, an unrestricted extension may use both types \(0\) and \(k\), in which case \(s=k\). The stripping argument then removes no extension vertices and reproduces only the existing quadratic estimate. Thus it does not settle the main problem:
\[
k+1\leq f(k)\leq O(k^2).
\]

The unresolved difficulty is precisely the case where the universal vertices are genuinely interleaved throughout the forest: no large prefix or suffix of the transitive universal set has a uniform orientation to all forest vertices. A new simultaneous embedding argument is needed there.