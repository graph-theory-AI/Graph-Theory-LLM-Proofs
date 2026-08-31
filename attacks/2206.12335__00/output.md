```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for two broad classes of independent vertex-colour models, and every general 1-independent model satisfies an explicit asymptotically sharp lower bound, but the unrestricted conjecture remains open.",
  "would_publish": false,
  "caveats": "The vertex-colour arguments do not represent all 1-independent edge laws, and the universal lower bound is strictly below the signs value."
}
```

# 1. Statement and notation

Write \(Q_3\) for the three-dimensional cube. For \(p>1/2\), put
\[
t=2p-1,\qquad
\theta=\frac{1+\sqrt t}{2},\qquad
\bar\theta=1-\theta.
\]
In the signs model, the vertices receive independent signs, with probability
\(\theta\) of \(+\), and an edge is open exactly when its endpoints have the
same sign. Its edge density is
\[
\theta^2+\bar\theta^2=p.
\]

Since \(Q_3\) is connected, its open subgraph in the signs model is connected
if and only if all eight signs agree. Thus the conjectured minimum is
\[
S(p):=\theta^8+\bar\theta^8
     =\frac{p^4+12p^3-2p^2-4p+1}{8}.
\]
Writing \(r=1-p\), this is equivalently
\[
S(p)=1-4r+5r^2-2r^3+\frac{r^4}{8}.
\]

I do not prove the conjecture for arbitrary 1-independent models. I prove it
for two substantial subclasses and obtain a general lower bound.

---

# 2. Reduction to exact edge marginals

It is enough to consider models in which every edge has marginal exactly
\(p\).

Indeed, suppose edge \(e\) is open with probability \(q_e\ge p\). Independently
for each edge, let \(B_e\) be Bernoulli with parameter \(p/q_e\), independent
of the original model, and retain \(e\) only when both its original state and
\(B_e\) are open. The resulting edge marginal is \(p\), the new graph is a
subgraph of the old one, and 1-independence is preserved: edge sets with
disjoint vertex supports depend on independent original vectors and
independent thinning variables.

Consequently, thinning cannot increase connectivity, and minimization over
\(\mathcal D_{\ge p}(Q_3)\) is equivalent to minimization over homogeneous
models with every edge marginal \(p\).

---

# 3. A universal lower bound for arbitrary 1-independent models

## Proposition 3.1

For every 1-independent model on \(Q_3\) with edge marginals at least \(p>1/2\),
\[
\boxed{\;
\mathbb P(Q_3\text{ is connected})
\ge
\max\left\{0,\,(2p-1)^2-(1-p)^4\right\}.
\;}
\]

In particular, the bound is positive for
\[
p>2-\sqrt2\approx 0.585786.
\]

### Proof

Fix one coordinate direction and regard \(Q_3\) as two opposite square faces
\(F_0,F_1\), joined by a perfect matching \(M\) of four edges.

For a spanning subgraph of a square \(C_4\), let \(N\) be its number of open
edges and let \(I\) be the indicator that it is connected. Pointwise,
\[
I\ge \frac{N-2}{2}.
\]
This holds because a disconnected spanning subgraph of \(C_4\) has at most
two edges, while the right-hand side is \(1/2\) or \(1\) when \(N=3\) or \(4\).

Hence each face satisfies
\[
\mathbb P(F_i\text{ is connected})
\ge \frac{4p-2}{2}=2p-1.
\]
The edge sets of \(F_0\) and \(F_1\) have disjoint vertex supports, so their
entire edge-state vectors are independent. Therefore
\[
\mathbb P(F_0,F_1\text{ both connected})\ge (2p-1)^2.
\]

If both faces are connected and at least one edge of \(M\) is open, then the
whole cube is connected. The four edges of \(M\) are mutually independent,
and each is closed with probability at most \(1-p\). Thus
\[
\mathbb P(M\text{ is entirely closed})\le (1-p)^4.
\]
A union bound now gives
\[
\mathbb P(Q_3\text{ connected})
\ge (2p-1)^2-(1-p)^4.
\]
Taking the maximum with zero proves the claim. ∎

## Comparison with the signs model

In terms of \(r=1-p\), the lower bound is
\[
1-4r+4r^2-r^4.
\]
Its gap from the conjectured value is exactly
\[
S(p)-\bigl((2p-1)^2-r^4\bigr)
=
r^2\left(1-2r+\frac{9r^2}{8}\right)>0
\]
for \(0<r<1\). Thus, for the unrestricted extremal value \(f(p)\),
\[
S(p)-r^2\left(1-2r+\frac{9r^2}{8}\right)
\le f(p)\le S(p)
\]
whenever the displayed lower bound is useful. In particular,
\[
f(p)=S(p)+O((1-p)^2)\qquad (p\uparrow1).
\]
So the signs model is asymptotically optimal through the linear term at
\(p=1\), but this does not prove exact optimality on any nontrivial interval.

### Sharpness of the face estimate

The bound \(\mathbb P(C_4\text{ connected})\ge 2p-1\) is sharp even among
1-independent models. Label the cyclic edges \(e_1,e_2,e_3,e_4\), put
\(r=1-p\) and \(t=2p-1\), and assign probabilities
\[
\begin{array}{c|ccccc}
(e_1,e_2,e_3,e_4)&1111&1010&0101&1100&0011\\ \hline
\mathbb P&t&r^2&r^2&pr&pr .
\end{array}
\]
Each edge has marginal \(p\), and each opposite pair has the product
Bernoulli-\(p\) law. Those are precisely the nontrivial 1-independence
requirements on \(C_4\). Only \(1111\) is connected, so the connectivity
probability is \(t=2p-1\).

Thus a proof of the cube conjecture cannot simply replace each face by a
stronger universal face-connectivity estimate.

---

# 4. The conjecture for i.i.d. equality-colour models

Consider the following broad generalization of the signs model. Give every
vertex an independent colour with common distribution
\[
(x_i)_{i\in I},\qquad x_i\ge0,\qquad \sum_i x_i=1,
\]
and declare an edge open exactly when its endpoint colours agree. The edge
density is
\[
s=\sum_i x_i^2,
\]
and, since \(Q_3\) is connected, its open graph is connected exactly when all
eight vertices have the same colour. Therefore
\[
\mathbb P(Q_3\text{ connected})=\sum_i x_i^8.
\]

## Theorem 4.1

If \(p>1/2\) and \(\sum_i x_i^2\ge p\), then
\[
\boxed{\;
\sum_i x_i^8\ge S(p).
\;}
\]
Equality, apart from zero-probability colours and interchange of the two
colours, occurs only for
\[
(x_i)=(\theta,1-\theta).
\]

Thus the signs model is the unique minimizer among all i.i.d.
equality-colour models, with an arbitrary finite or countable colour space.

### Proof

Let
\[
a=\theta=\frac{1+\sqrt{2p-1}}2,\qquad b=1-a,
\]
so that
\[
a+b=1,\qquad a^2+b^2=p.
\]
Let
\[
m=\max_i x_i,\qquad R=1-m,\qquad Q=\sum_{x_i\ne m}x_i^2.
\]

First, \(m>1/2\), because
\[
\sum_i x_i^2\le m\sum_i x_i=m
\]
and the left-hand side is greater than \(1/2\). Moreover,
\[
p\le \sum_i x_i^2
   \le m^2+(1-m)^2.
\]
Since \(u^2+(1-u)^2\) is increasing for \(u\ge1/2\), this implies
\[
m\ge a.
\]

For the remaining coordinates, Jensen's inequality in size-biased form gives
\[
\sum_{x_i\ne m}x_i^8\ge \frac{Q^7}{R^6}.
\]
Indeed, after writing \(x_i=Rz_i\), choose a random value \(Z=z_i\) with
probability \(z_i\). Then
\[
\sum_i z_i^8=\mathbb E Z^7\ge(\mathbb EZ)^7
 =\left(\sum_i z_i^2\right)^7.
\]

If \(m\ge\sqrt p\), then
\[
\sum_i x_i^8\ge m^8\ge p^4
=(a^2+b^2)^4\ge a^8+b^8.
\]

It remains to consider \(a\le m\le\sqrt p\). Since
\[
Q\ge p-m^2,
\]
we obtain
\[
\sum_i x_i^8
\ge F(m):=m^8+\frac{(p-m^2)^7}{(1-m)^6}.
\]
Set
\[
q=p-m^2,\qquad y=\frac{q}{1-m}.
\]
Because \(p=a^2+b^2\), for \(m\ge a\),
\[
q-b(1-m)=-(m-a)(m+a-b)\le0.
\]
Hence \(0\le y\le b\le m\). Differentiating,
\[
F'(m)=8m^7-14my^6+6y^7.
\]
Writing \(z=y/m\in[0,1]\),
\[
F'(m)
=2m^7\bigl(4-7z^6+3z^7\bigr).
\]
The function
\[
h(z)=4-7z^6+3z^7
\]
is nonnegative on \([0,1]\): it is decreasing there and \(h(1)=0\).
Consequently \(F\) is increasing on \([a,\sqrt p]\), and therefore
\[
\sum_i x_i^8\ge F(a)=a^8+b^8=S(p).
\]

For equality, one must have \(m=a\), total second moment exactly \(p\), and
the remaining mass \(b\) must have square sum \(b^2\). This forces it to be
concentrated in one further colour. ∎

---

# 5. The conjecture for non-identically distributed binary signs

There is another extension in which the vertex labels remain binary but need
not have the same distribution.

At vertex \(v\), let \(+\) have probability \(\theta_v\), independently over
vertices, and again open an edge exactly when its endpoint signs agree.

## Theorem 5.1

Suppose every edge of \(Q_3\) has open probability at least \(p>1/2\).
Then
\[
\boxed{\;
\mathbb P(Q_3\text{ connected})\ge S(p).
\;}
\]
Equality forces all \(\theta_v\) to equal \(\theta\), up to globally
interchanging \(+\) and \(-\).

### Proof

Put
\[
b_v=2\theta_v-1.
\]
For an edge \(uv\),
\[
\mathbb P(uv\text{ open})=\frac{1+b_ub_v}{2}.
\]
Thus
\[
b_ub_v\ge t:=2p-1>0.
\]
Because \(Q_3\) is connected, all \(b_v\) have the same sign. After globally
interchanging the signs, assume \(b_v>0\) for every \(v\).

Multiply the edge inequalities over any perfect matching of \(Q_3\). This
gives
\[
\prod_{v\in V(Q_3)}b_v\ge t^4.
\]

The cube is connected precisely when all eight vertex signs agree, so
\[
\begin{aligned}
\mathbb P(Q_3\text{ connected})
&=\prod_v\theta_v+\prod_v(1-\theta_v)\\
&=2^{-8}\left(\prod_v(1+b_v)+\prod_v(1-b_v)\right)\\
&=2^{-7}\sum_{\substack{0\le k\le8\\k\text{ even}}}e_k(b_1,\ldots,b_8),
\end{aligned}
\]
where \(e_k\) denotes the \(k\)-th elementary symmetric polynomial.

Maclaurin's inequalities give, for \(1\le k\le8\),
\[
\frac{e_k}{\binom8k}
\ge
\left(\prod_v b_v\right)^{k/8}.
\]
Therefore, for even \(k\),
\[
e_k\ge \binom8k t^{k/2}.
\]
It follows that
\[
\begin{aligned}
\mathbb P(Q_3\text{ connected})
&\ge
2^{-7}\sum_{k\text{ even}}\binom8k t^{k/2}\\
&=
2^{-8}\left((1+\sqrt t)^8+(1-\sqrt t)^8\right)\\
&=S(p).
\end{aligned}
\]

Equality in Maclaurin's inequalities forces all \(b_v\) equal, and equality
in the perfect-matching product requires \(b_v=\sqrt t\). Thus
\(\theta_v=\theta\) for all \(v\), up to global sign interchange. ∎

This theorem allows arbitrary vertex-dependent biases, while Theorem 4.1
allows arbitrarily many colours but requires a common colour distribution.
Neither covers all independent, non-identically distributed multicolour
models, much less all 1-independent edge laws.

---

# 6. Exact finite formulation of the remaining problem

The unrestricted problem is a finite polynomial optimization problem, but
not a linear program.

Enumerate the twelve edges of \(Q_3\). For each \(H\subseteq E(Q_3)\), let
\(x_H\) be the probability that the open edge set is exactly \(H\). Thus
there are \(2^{12}=4096\) variables satisfying
\[
x_H\ge0,\qquad \sum_Hx_H=1.
\]
For \(A\subseteq E(Q_3)\), define the all-open moment
\[
m_A=\sum_{H\supseteq A}x_H.
\]
After thinning, impose
\[
m_{\{e\}}=p\qquad(e\in E(Q_3)).
\]

The distribution is 1-independent exactly when
\[
m_{A\cup B}=m_A m_B
\]
for every two edge sets \(A,B\) with disjoint vertex supports. These
all-open moment factorizations imply factorization for arbitrary
zero-one patterns by inclusion-exclusion, and hence are equivalent to
independence of the two edge-state vectors.

The objective is the linear form
\[
\sum_{\substack{H\subseteq E(Q_3)\\(V(Q_3),H)\text{ connected}}}x_H.
\]
Thus the conjecture is the assertion that this objective is at least
\[
\frac{p^4+12p^3-2p^2-4p+1}{8}
\]
throughout the resulting compact semialgebraic set for \(11/20<p\le1\).

A rigorous computer proof could in principle consist of an exact
Positivstellensatz, cylindrical-algebraic-decomposition, or branch-and-bound
certificate for the infeasibility of the strict reverse inequality.
Floating-point optimization alone would not suffice.

One important obstruction is that the feasible set is nonconvex:
the equations \(m_{A\cup B}=m_A m_B\) are quadratic. Consequently, averaging
a model over cube automorphisms need not preserve 1-independence. A hidden
random automorphism can introduce dependence between vertex-disjoint edge
sets, so a symmetry reduction cannot be made without an additional argument.

---

# 7. Remaining gap

The two equality-colour theorems establish the conjecture for natural
vertex-generated models and identify the signs model uniquely there. The
universal face decomposition also shows that the unrestricted extremal value
is within \(O((1-p)^2)\) of the signs value as \(p\uparrow1\).

The unresolved step is structural: an arbitrary 1-independent edge law need
not admit a representation by independent vertex labels. The quadratic
independence constraints permit local correlations around a vertex and
potentially more complicated global interactions. None of the arguments
above excludes such a law from attaining connectivity strictly below
\(S(p)\), particularly in the difficult range near \(p=0.55\).