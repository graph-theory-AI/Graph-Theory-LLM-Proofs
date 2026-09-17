```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "A planted-matching and short-cycle argument gives the partial upper bound P_n = O(n^{-1/6} sqrt(log n)), but does not establish the conjectured exponent 1/4.",
  "would_publish": true,
  "caveats": "The argument below is independent of the cited literature; novelty and the recent bibliographic claims in the supplied catalog have not been independently verified."
}
```

# A quantitative partial result

Throughout, “random preferences” means that the \(n\) preference lists are independent, uniformly random permutations of the other \(n-1\) people.

I obtain the following bound.

**Theorem.** For even \(n\),
\[
\boxed{\displaystyle P_n=O\!\left(n^{-1/6}\sqrt{\log n}\right).}
\]

This is stronger than the upper bound reported in the supplied catalog, but it falls short of the conjecture. In particular, the argument does not give either \(P_n=O(n^{-1/4})\) or \(P_n=\Omega(n^{-1/4})\).

The proof uses a planted stable matching. Under that distribution, short directed cycles describe independent changes to the planted matching, except for explicitly controlled collision and blocking events. A quantitative factorial-moment calculation then bounds the reciprocal of the number of stable matchings.

All estimates below are proved directly; no literature result is needed.

## 1. Scores and the planted distribution

Generate the preference lists using independent random variables
\[
U_{vw}\sim\operatorname{Unif}[0,1],\qquad v\ne w,
\]
where smaller scores mean greater preference.

Let \(Z\) be the number of stable perfect matchings, and write
\[
m_n=\mathbb E Z,\qquad N_n=(n-1)!!.
\]

Define a planted distribution \(\mathbb Q\) as follows:

1. choose a perfect matching \(M\) uniformly;
2. sample the scores conditional on \(M\) being stable.

Its marginal distribution on preference profiles satisfies
\[
\frac{d\mathbb Q}{d\mathbb P}=\frac{Z}{m_n}.
\]
Consequently,
\[
\boxed{\displaystyle P_n=m_n\,\mathbb E_{\mathbb Q}\frac1Z.} \tag{1}
\]
Here \(Z\ge1\) under \(\mathbb Q\). By relabeling, we can fix \(M\) for the rest of the proof.

Put
\[
x_v=U_{v,M(v)},\qquad S=\sum_v x_v,\qquad a=\max_v x_v.
\]

Conditional on \(x=(x_v)\) and on stability of \(M\), the score pairs belonging to different unmatched unordered pairs are independent. For \(\{v,w\}\notin M\), the pair
\[
(U_{vw},U_{wv})
\]
is uniform on the unit square with the rectangle
\[
[0,x_v)\times[0,x_w)
\]
deleted. Its normalizing denominator is
\[
d_{vw}=1-x_vx_w. \tag{2}
\]

We first establish the threshold estimates needed later.

## 2. Threshold estimates and the first moment

For fixed \(M\), define
\[
f(x)=\prod_{\substack{v<w\\\{v,w\}\notin M}}(1-x_vx_w).
\]
Then
\[
m_n=N_n\int_{[0,1]^n}f(x)\,dx. \tag{3}
\]

Let \(\mu_n\) be the probability measure on \(\mathbb R_+^n\) having density
\[
N_n e^{-S^2/2}.
\]
It is normalized because, for even \(n\),
\[
\int_{\mathbb R_+^n}e^{-S^2/2}\,dx
=\frac{1}{(n-1)!}\int_0^\infty s^{n-1}e^{-s^2/2}\,ds
=\frac1{(n-1)!!}.
\]

Set
\[
W(x)=\mathbf 1_{\{x\in[0,1]^n\}}e^{S^2/2}f(x).
\]
Thus
\[
m_n=\mathbb E_{\mu_n}W,
\qquad
\frac{d\mathbb Q_x}{d\mu_n}=\frac{W}{m_n}, \tag{4}
\]
where \(\mathbb Q_x\) denotes the planted marginal distribution of the thresholds.

### 2.1. A uniform likelihood bound

Write
\[
A=\sum_vx_v^2,\qquad
B=\sum_{\{v,w\}\in M}x_vx_w,\qquad
D=\sum_{\substack{v<w\\\{v,w\}\notin M}}x_v^2x_w^2.
\]
On the cube, using \(\log(1-z)\le-z-z^2/2\),
\[
\log W\le \frac A2+B-\frac D2.
\]
Also,
\[
B\le\frac A2
\]
and
\[
D
=\frac12\left(A^2-\sum_vx_v^4\right)
-\sum_{\{v,w\}\in M}x_v^2x_w^2
\ge\frac{A^2}{2}-A.
\]
Therefore
\[
\log W\le \frac{3A}{2}-\frac{A^2}{4}\le\frac94,
\]
so
\[
\boxed{0\le W\le e^{9/4}.} \tag{5}
\]

### 2.2. Typical thresholds

Under \(\mu_n\), \(S^2\) has the chi-square distribution with \(n\) degrees of freedom, independently of \((x_v/S)_v\), which is uniform on the simplex. Equivalently,
\[
x_v=S\frac{E_v}{T},\qquad
T=\sum_vE_v,
\]
where the \(E_v\) are independent exponential random variables of mean one, independent of \(S\).

The law of large numbers gives
\[
A\longrightarrow2,\qquad B\longrightarrow\frac12,
\qquad a\longrightarrow0
\]
in probability. Furthermore,
\[
D\longrightarrow2.
\]
Indeed, \(\sum_vx_v^4\le a^2A=o_{\mathbb P}(1)\), and the matching contribution to \(D\) is at most \(\frac12\sum_vx_v^4\).

Taylor expansion, with the remainder controlled by \(a^2D\), now yields
\[
\log W=\frac A2+B-\frac D2+o_{\mathbb P}(1)
\longrightarrow\frac12.
\]
The bound (5) gives
\[
\boxed{m_n\longrightarrow\sqrt e.} \tag{6}
\]

For quantitative purposes, define
\[
\mathcal R_n=
\left\{
\frac{\sqrt n}{2}\le S\le2\sqrt n,\quad
a\le\frac{40\log n}{\sqrt n}
\right\}.
\]
Exponential-moment bounds for \(S^2\) and \(T\), together with
\[
\Pr\!\left(\max_vE_v>10\log n\right)\le n^{-9},
\]
give
\[
\mu_n(\mathcal R_n^c)=O(n^{-9}).
\]
Equations (4)–(6) therefore imply
\[
\boxed{\mathbb Q(\mathcal R_n^c)=O(n^{-9}).} \tag{7}
\]

Thus we can work uniformly with deterministic thresholds \(x\in\mathcal R_n\), at a negligible probability cost.

## 3. Exchange cycles

Given a stable matching \(M\), let
\[
A(v)=\{w\notin\{v,M(v)\}:U_{wv}<x_w\}.
\]
These are the people who prefer \(v\) to their partners in \(M\).

If \(A(v)\ne\varnothing\), let \(f(v)\) be \(v\)'s most preferred member of \(A(v)\), and define
\[
F(v)=M(f(v)).
\]
Otherwise \(F(v)\) is undefined.

Stability of \(M\) ensures
\[
U_{v,f(v)}>x_v: \tag{8}
\]
moving from \(M(v)\) to \(f(v)\) makes \(v\) worse off.

Let \(\mathcal C\) be a collection of directed cycles of \(F\), each of length at least two. Distinct directed cycles of a partial function are vertex-disjoint. Write \(C\) for their union of vertices.

Call this collection **good** if:

1. \(C\cap M(C)=\varnothing\);
2. there is no pair \(u,v\in C\) such that
   \[
   U_{uv}<U_{u,f(u)}
   \quad\text{and}\quad
   U_{vu}<U_{v,f(v)}. \tag{9}
   \]

**Exchange lemma.** If \(\mathcal C\) is good and contains \(c\) cycles, then
\[
Z\ge2^c. \tag{10}
\]

**Proof.** Select any subcollection, with vertex union \(D\). For each \(v\in D\), replace its old matching edge by
\[
\{v,f(v)\}.
\]
Since \(F\) permutes \(D\), \(f\) maps \(D\) bijectively onto \(M(D)\). As \(D\cap M(D)=\varnothing\), this produces a perfect matching.

The vertices in \(D\) become worse off; those in \(M(D)\) become better off; all others are unchanged.

A blocking pair not joining two worse-off vertices is impossible. Indeed, suppose \(v\in D\), while \(w\) is not worse off, and \(w\) prefers \(v\) to its new partner. Then \(w\) prefers \(v\) to \(M(w)\). Unless \(w=M(v)\), this makes \(w\) a candidate in \(A(v)\), so \(v\) cannot prefer \(w\) to its best candidate \(f(v)\). If \(w=M(v)\), then \(w\)'s new partner is strictly better than \(v\), also excluding a block.

A block joining two worse-off vertices is excluded by (9). Thus every selected subcollection gives a stable matching. Different subcollections give different matchings. ∎

We next estimate the number of short cycles and the probability that they fail to be good.

## 4. Probabilities of prescribed cycles

All probabilities in this section are conditional on the thresholds and on stability of \(M\). Write them as \(\mathbb Q_x\), and put
\[
q_v=\frac{x_{M(v)}}S.
\]
Then
\[
\sum_vq_v=1,\qquad \max_vq_v=\frac aS. \tag{11}
\]

Let \(C\) be a set of \(r\) vertices, and let \(\pi\) be a permutation of \(C\) without fixed points. We estimate
\[
E(C,\pi)=\{F(v)=\pi(v)\text{ for all }v\in C\}.
\]

### 4.1. An upper bound, including partner collisions

A required edge for \(v\) is
\[
\{v,M(\pi(v))\}.
\]
If a requirement asks \(f(v)=v\), it is impossible. If two required edges are the same unordered edge in opposite directions, the requirements are also impossible: each endpoint would have to prefer the other to its old partner, contradicting stability of \(M\).

In all remaining cases, the required score pairs are distinct. Write
\[
U_{v,M(\pi(v))}=x_v+t_v,\qquad t_v\ge0.
\]
The density contributed by this required edge is
\[
\frac{x_{M(\pi(v))}}{1-x_vx_{M(\pi(v))}}\,dt_v.
\]

For \(w\notin C\cup M(C)\), the condition that \(w\) does not beat this proposed choice is
\[
1-\frac{t_vx_w}{1-x_vx_w}
\le e^{-t_vx_w}.
\]
These external score pairs are independent. Dropping all other restrictions and extending the resulting exponential integrals to infinity gives, whenever \(S>2ra\),
\[
\boxed{
\mathbb Q_x(E(C,\pi))
\le
\left(\prod_{v\in C}q_v\right)
(1-a^2)^{-r}(1-2ra/S)^{-r}.
} \tag{12}
\]
Here we used
\[
\sum_{w\notin C\cup M(C)}x_w\ge S-2ra
\]
and \(\prod_{v\in C}x_{M(\pi(v))}=\prod_{v\in C}x_{M(v)}\).

In particular, when the displayed error terms are small,
\[
\mathbb Q_x(E(C,\pi))
\le
\left(1+O(ra^2+r^2a/S)\right)\prod_{v\in C}q_v. \tag{13}
\]

### 4.2. A lower bound for partner-free sets

Now suppose \(C\cap M(C)=\varnothing\). There are no conflicting required edges.

For \(u,v\in C\), the joint restriction that neither is an earlier eligible candidate for the other contributes exactly
\[
1-\frac{t_ux_v+t_vx_u}{1-x_ux_v}. \tag{14}
\]
For edges from \(C\) to its complement, excluding old and required partners, the factors are
\[
1-\frac{t_vx_w}{1-x_vx_w}. \tag{15}
\]
The required-edge densities together with (14)–(15) give the complete joint integral.

Restrict this integral to
\[
0\le t_v\le L/S,
\]
assuming \(L/S\le1-a\). Denote the quantities subtracted from one in (14)–(15) by \(b\). They satisfy
\[
\max b\le\frac{2aL}{S(1-a^2)}
\]
and
\[
\sum b\le\frac{S}{1-a^2}\sum_{v\in C}t_v. \tag{16}
\]
The latter follows by collecting the terms belonging to each row \(v\); the sum of the relevant thresholds is at most \(S\).

For \(\max b\le1/2\), use
\[
\log(1-b)\ge-b-2b^2.
\]
The full product of survival factors is therefore at least
\[
\exp\left(-(1+\eta)S\sum_vt_v\right),
\qquad
\eta=O(a^2+aL/S).
\]
The required-edge densities are at least \(\prod_vx_{M(\pi(v))}\). Integrating over the box gives
\[
\boxed{
\mathbb Q_x(E(C,\pi))
\ge
\left(1-O\!\left(r(a^2+aL/S+e^{-L})\right)\right)
\prod_{v\in C}q_v.
} \tag{17}
\]
All constants in (13) and (17) are absolute, subject to their error terms being sufficiently small.

## 5. Quantitative factorial moments of short-cycle counts

Let \(C_K\) be the number of directed cycles of \(F\) whose lengths belong to \(\{2,\dots,K\}\), and put
\[
\lambda_K=\sum_{k=2}^K\frac1k=H_K-1.
\]

Fix an integer \(J\), and set \(R=KJ\). Take \(L>0\). Equations (13) and (17) imply, uniformly for \(0\le j\le J\),
\[
\boxed{
\left|\mathbb E_x(C_K)_j-\lambda_K^j\right|
\le \delta\,\lambda_K^j,
} \tag{18}
\]
where
\[
\delta=
O\!\left(
Ra^2+R^2a/S+RaL/S+Re^{-L}
\right), \tag{19}
\]
provided this expression tends to zero and the preceding integral conditions hold.

Here is the counting justification, including collisions.

The falling factorial \((C_K)_j\) counts ordered \(j\)-tuples of distinct cycles. In a partial function, such cycles must be vertex-disjoint. For prescribed lengths \(k_1,\dots,k_j\), write
\[
r=k_1+\cdots+k_j\le R.
\]
Represent the cycles by ordered vertex lists, dividing by
\[
k_1\cdots k_j
\]
to remove the choices of starting points.

For the upper bound, sum (13) over injective lists and then remove the injectivity restriction. The sum of \(\prod q_v\) over all lists is one.

For the lower bound, retain only lists with distinct vertices and without a pair of matching partners. If vertices are sampled independently with probabilities \(q_v\), the probability of a repeated vertex or a partner collision is at most
\[
\binom r2
\left(\sum_vq_v^2+\sum_vq_vq_{M(v)}\right)
\le r^2a/S. \tag{20}
\]
Apply (17) on the remaining lists. Finally,
\[
\sum_{k_1,\dots,k_j=2}^K\frac1{k_1\cdots k_j}
=\lambda_K^j,
\]
which proves (18).

### 5.1. Bounding the reciprocal switch count

For an even integer \(J\), the alternating binomial truncation gives, for every nonnegative integer \(c\),
\[
2^{-c}\le\sum_{j=0}^J\frac{(-1/2)^j}{j!}(c)_j.
\]
Consequently, (18) yields
\[
\mathbb E_x2^{-C_K}
\le
\sum_{j=0}^J\frac{(-\lambda_K/2)^j}{j!}
+\delta e^{\lambda_K/2}.
\]
Taylor's formula for the exponential gives
\[
\boxed{
\mathbb E_x2^{-C_K}
\le
e^{-\lambda_K/2}
+\delta e^{\lambda_K/2}
+\frac{(\lambda_K/2)^{J+1}}{(J+1)!}.
} \tag{21}
\]

The cancellation in this alternating expansion is the reason quantitative control of the factorial moments is needed.

## 6. Controlling failures of the exchange lemma

Let \(B_K\) be the event that the collection of all cycles counted by \(C_K\) is not good. I claim that, in the parameter range used below,
\[
\boxed{
\mathbb Q_x(B_K)
=O\!\left(K^2a/S+K^2/S^2\right).
} \tag{22}
\]

### 6.1. Matching-partner collisions

A partner collision is witnessed by either one cycle or two cycles of length at most \(K\). These witnesses involve at most \(2K\) vertices, so (12) is at most a constant times \(\prod q_v\) in our parameter range.

For a specified pair of list positions, the weighted sum imposing a partner collision is
\[
\sum_vq_vq_{M(v)}\le a/S.
\]

For a single cycle of length \(k\), the number of position pairs, divided by the \(k\) starting-point representations, is \(O(k)\). Summing over \(k\le K\) gives \(O(K^2)\).

For two cycles of lengths \(k,\ell\), the \(k\ell\) cross-position pairs cancel the \(k\ell\) starting-point representations. Summing over their lengths again gives \(O(K^2)\).

Thus the probability of any partner collision is
\[
O(K^2a/S). \tag{23}
\]

### 6.2. Blocking pairs among cycle vertices

Suppose a prescribed one- or two-cycle witness has partner-free vertex set \(C\), with \(|C|=r\le2K\). Fix \(u,v\in C\).

Write
\[
U_{u,f(u)}=x_u+t_u,\qquad U_{v,f(v)}=x_v+t_v.
\]
Under the requirements that these are the best eligible candidates, a block between \(u\) and \(v\) must lie in the rectangle
\[
[x_u,x_u+t_u)\times[x_v,x_v+t_v).
\]
Its conditional area is
\[
\frac{t_ut_v}{1-x_ux_v}. \tag{24}
\]
The portions below one of the old-partner thresholds are excluded by the candidate-minimality conditions.

Retain the external exponential factors used in (12), insert (24), and drop other restrictions. The resulting integral is at most
\[
\frac{\prod_{w\in C}x_{M(w)}}
{(1-a^2)^{r+1}(S-2ra)^{r+2}}
=O\!\left(\frac1{S^2}\prod_{w\in C}q_w\right). \tag{25}
\]
The two extra powers of \(S^{-1}\) come from integrating \(t_u\) and \(t_v\).

Sum (25) over witnesses and position pairs. The same one-cycle and two-cycle counting as above gives
\[
O(K^2/S^2). \tag{26}
\]
Together, (23) and (26) prove (22).

These witness arguments cover collections with arbitrarily many short cycles: a failure of goodness always has a witness using at most two of them.

## 7. Choice of parameters and conclusion

Take natural logarithms and set
\[
K=\left\lfloor\frac{n^{1/3}}{\log n}\right\rfloor,
\qquad
J=2\lceil10\log n\rceil,
\qquad
L=10\log n.
\]
Then
\[
R=KJ=O(n^{1/3}).
\]

Uniformly for \(x\in\mathcal R_n\), all conditions used in Sections 4–6 hold for sufficiently large \(n\). In particular,
\[
Ra^2+R^2a/S+RaL/S+Re^{-L}
=O(n^{-1/3}\log n),
\]
so
\[
\delta=O(n^{-1/3}\log n). \tag{27}
\]

Also,
\[
e^{-\lambda_K/2}=O(K^{-1/2}),
\qquad
e^{\lambda_K/2}\le K^{1/2}.
\]
The Taylor remainder in (21) is \(O(n^{-2})\), by
\[
(J+1)!\ge\left(\frac{J+1}{e}\right)^{J+1}
\]
and \(\lambda_K\le\log K\le\log n\). Hence
\[
\mathbb E_x2^{-C_K}
=
O\!\left(
K^{-1/2}
+n^{-1/3}(\log n)K^{1/2}
+n^{-2}
\right)
=
O\!\left(n^{-1/6}\sqrt{\log n}\right). \tag{28}
\]

Meanwhile, (22) gives
\[
\mathbb Q_x(B_K)
=O(K^2\log n/n)
=O(n^{-1/3}/\log n). \tag{29}
\]

The exchange lemma implies, pointwise under the planted distribution,
\[
\frac1Z\le 2^{-C_K}+\mathbf1_{B_K}.
\]
Average (28)–(29) over the thresholds and use (7) to discard \(\mathcal R_n^c\). We obtain
\[
\mathbb E_{\mathbb Q}\frac1Z
=O\!\left(n^{-1/6}\sqrt{\log n}\right).
\]
Finally, (1) and (6) establish
\[
\boxed{\displaystyle
P_n=O\!\left(n^{-1/6}\sqrt{\log n}\right).
}
\qquad\Box
\]

## 8. What remains unresolved

The argument supplies only an upper bound.

The short-cycle calculation explains why the exponent \(1/4\) is natural. For fixed cycle-length cutoff \(K\), the cycle counts have the factorial moments of independent Poisson variables of means \(1/k\). Independent switches would therefore contribute
\[
\mathbb E\,2^{-C_K}\approx
\exp\!\left(-\frac12\sum_{k=2}^K\frac1k\right)
\asymp K^{-1/2}.
\]
A cutoff on the order of \(\sqrt n\) would produce \(n^{-1/4}\).

The proof above does **not** justify that cutoff. Its quantitative factorial-moment error, after the alternating expansion, leads instead to \(K\) of order \(n^{1/3}/\log n\). Controlling the reciprocal switch count near the \(\sqrt n\) scale requires substantially sharper estimates, including treatment of interacting cycles.

There is a separate obstruction to a matching lower bound: constructing many stable matchings in the planted model bounds \(1/Z\) from above, not below. Even a successful extension of this construction to obtain the conjectured upper bound would not establish \(P_n=\Omega(n^{-1/4})\).

Thus the Mertens conjecture remains unresolved by this argument.