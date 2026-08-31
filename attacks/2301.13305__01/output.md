```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the universal nonlinear bound d_{K_4}(n) <= 5/12 for n >= 7, together with vanishing for unate codes and structural lower bounds on the influence and Fourier complexity of any putative dense code.",
  "would_publish": false,
  "caveats": "The bound is constant and does not imply d_{K_4}(n)=o(1); novelty relative to all follow-up literature was not verified."
}
```

# 1. Statement and reformulation

Let
\[
\Gamma_n=\mathbb F_2^{E(K_n)},\qquad N=\binom n2.
\]
We identify an element of \(\Gamma_n\) with a graph on \([n]\). For each \(X\in\binom{[n]}4\), let \(k_X\in\Gamma_n\) be the incidence vector of the six edges of the copy \(K_n[X]\).

Let \(\mathcal C_n\) be the Cayley graph
\[
\operatorname{Cay}\bigl(\Gamma_n,\{k_X:X\in \tbinom{[n]}4\}\bigr).
\]
Then a graph code avoiding \(K_4\)-differences is precisely an independent set in \(\mathcal C_n\). Thus
\[
D_{K_4}(n)=\alpha(\mathcal C_n),\qquad
d_{K_4}(n)=\frac{\alpha(\mathcal C_n)}{2^N}.
\]

The conjecture asks whether \(d_{K_4}(n)\to0\).

The results proved below are:

1. For every \(n\ge7\),
   \[
   d_{K_4}(n)\le \frac5{12}.
   \]
2. Every such code of density \(\delta\) has total edge-coordinate influence at least
   \[
   \frac{\delta}{18}\binom n2.
   \]
3. Every nonempty code depends essentially on at least
   \[
   \binom n2-\operatorname{ex}(n,K_4)
   \]
   edge coordinates.
4. If the code is unate—equivalently, a translate of a monotone family—then its density is \(\exp(-\Omega(n^2))\).
5. Codes whose indicators are controlled, even approximately, by bounded-dimensional collections of linear parity tests are impossible for Ramsey-large \(n\).

None of these settles the unrestricted conjecture.

---

# 2. Monotonicity of the density

For later reference, \(d_{K_4}(n)\) is nonincreasing.

## Lemma 2.1
If \(n\ge m\), then
\[
d_{K_4}(n)\le d_{K_4}(m).
\]

### Proof

Fix \(U\subseteq[n]\) with \(|U|=m\). Partition a \(K_4\)-difference-free family \(\mathcal A\subseteq\Gamma_n\) according to all edge coordinates outside \(E(K_n[U])\). Within each fiber, the varying graphs on \(U\) form a \(K_4\)-difference-free family on \(m\) vertices. Hence every fiber has size at most \(D_{K_4}(m)\). There are
\[
2^{\binom n2-\binom m2}
\]
fibers, so
\[
|\mathcal A|\le
2^{\binom n2-\binom m2}D_{K_4}(m).
\]
Dividing by \(2^{\binom n2}\) proves the assertion. \(\square\)

---

# 3. An exact seven-vertex parity lemma

For a graph \(F\) and \(X\in\binom{V(F)}4\), write
\[
q_F(X)=e(F[X])\pmod2.
\]
Let
\[
o_4(F)=|\{X\in\tbinom{V(F)}4:q_F(X)=1\}|.
\]

The key finite statement is the following.

## Lemma 3.1
Every graph \(F\) on seven vertices satisfies
\[
o_4(F)\le30.
\]
Equality is attained, for example, when \(F\) is a \(K_4\) together with three isolated vertices.

### Proof

Let \(V(F)=[7]\).

First,
\[
\sum_{X\in\binom{[7]}4}q_F(X)=0\pmod2,
\]
because every edge of \(F\) belongs to
\[
\binom52=10
\]
four-subsets. Hence \(o_4(F)\) is even.

For each \(v\in[7]\), let \(o_v\) be the number of odd four-subsets contained in \([7]\setminus\{v\}\). Within a six-vertex set, every edge belongs to
\[
\binom42=6
\]
four-subsets. Thus \(o_v\) is even, and hence \(o_v\le14\). Every odd four-subset is counted for each of the three vertices outside it, so
\[
3o_4(F)=\sum_{v=1}^7 o_v\le 7\cdot14=98.
\]
Therefore \(o_4(F)\le32\). We now rule out equality.

Suppose \(o_4(F)=32\). There are then exactly three even four-subsets; call their collection \(\mathcal E\). Let
\[
e_v=|\{E\in\mathcal E:v\notin E\}|.
\]
Since \(o_v=15-e_v\) is even, each \(e_v\) is odd. Moreover,
\[
\sum_v e_v=3|\mathcal E|=9.
\]
Thus one vertex, say \(7\), has \(e_7=3\), and each of the other six vertices has \(e_v=1\). Consequently all three members of \(\mathcal E\) lie in \([6]\), and every vertex of \([6]\) lies in exactly two of them. Their complements in \([6]\) therefore form a perfect matching. Relabeling,
\[
\mathcal E=\{1234,1256,3456\};
\]
their complements in \([6]\) are \(56,34,12\).

Write \(a_{ij}\in\mathbb F_2\) for the edge indicator of \(F[\{1,\dots,6\}]\). Put
\[
T=\sum_{i<j}a_{ij},\qquad d_i=\sum_{j\ne i}a_{ij}.
\]
For \(i<j\), let
\[
y_{ij}=q_F([6]\setminus\{i,j\}).
\]
Thus \(y_{12}=y_{34}=y_{56}=0\), and all other \(y_{ij}\) equal \(1\).

The edges counted by \(y_{ij}\) are exactly those disjoint from \(\{i,j\}\), so over \(\mathbb F_2\),
\[
y_{ij}=T+d_i+d_j+a_{ij}. \tag{3.1}
\]
Let \(s_i=\sum_{j\ne i}y_{ij}\). Since each vertex is incident with four \(y\)-edges equal to \(1\), \(s_i=0\). Summing (3.1) over \(j\ne i\) gives
\[
s_i=T+d_i.
\]
Thus \(d_i=T\) for every \(i\), and (3.1) yields
\[
a_{ij}=y_{ij}+T.
\]
It follows that \(F[6]\) is either the perfect matching
\[
M=\{12,34,56\},
\]
or its complement \(K_6\setminus M\).

Let \(b_i=a_{i7}\). Every four-subset containing \(7\) is assumed odd. Hence for every triple \(\{i,j,k\}\subseteq[6]\),
\[
b_i+b_j+b_k
=
1+a_{ij}+a_{ik}+a_{jk}. \tag{3.2}
\]

Suppose first that \(F[6]=K_6\setminus M\). A triple containing one matching edge has two edges of \(F[6]\), while a transversal choosing one vertex from each matched pair has three. Therefore (3.2) says:

- the \(b\)-sum on every transversal is \(0\);
- the \(b\)-sum on a triple containing a matched pair is \(1\).

Comparing transversals differing only within one matched pair shows
\[
b_1=b_2,\quad b_3=b_4,\quad b_5=b_6.
\]
Write the common values as \(c_1,c_2,c_3\). The transversal equations give
\[
c_1+c_2+c_3=0.
\]
On the other hand, using a matched pair together with a vertex from another pair forces \(c_1=c_2=c_3=1\), a contradiction.

If \(F[6]=M\), the right sides are reversed: transversals have \(b\)-sum \(1\), while triples containing a matching edge have \(b\)-sum \(0\). Again the matched endpoints have equal \(b\)-values, but the latter equations force all three common values to be \(0\), contradicting the transversal sum \(1\).

Thus \(o_4(F)\ne32\). Since \(o_4(F)\) is even, it follows that \(o_4(F)\le30\).

For sharpness, let \(F\) be a \(K_4\) on a set \(A\), with three isolated vertices. For a four-set \(X\), if \(k=|X\cap A|\), then
\[
e(F[X])=\binom k2,
\]
which is odd exactly for \(k=2,3\). Hence
\[
o_4(F)=\binom42\binom32+\binom43\binom31=18+12=30.
\]
\(\square\)

Double counting now gives an asymptotic version.

## Corollary 3.2
For every graph \(F\) on \(n\ge7\) vertices,
\[
o_4(F)\le \frac67\binom n4.
\]

### Proof

Sum \(o_4(F[U])\le30\) over all \(U\in\binom{[n]}7\). Every odd four-set is counted in \(\binom{n-4}{3}\) seven-subsets. Thus
\[
\binom{n-4}{3}o_4(F)
 \le 30\binom n7.
\]
Using
\[
35\binom n7=\binom n4\binom{n-4}{3}
\]
gives the claim. \(\square\)

---

# 4. Spectral consequence: \(d_{K_4}(n)\le5/12\)

## Theorem 4.1
For every \(n\ge7\),
\[
d_{K_4}(n)\le\frac5{12}.
\]

### Proof

The characters of \(\Gamma_n\) are indexed by graphs \(F\) on \([n]\):
\[
\chi_F(G)=(-1)^{|E(F)\cap E(G)|}.
\]
The corresponding adjacency eigenvalue of \(\mathcal C_n\) is
\[
\lambda_F
 =\sum_{X\in\binom{[n]}4}\chi_F(k_X)
 =\binom n4-2o_4(F).
\]
By Corollary 3.2,
\[
\lambda_F\ge
\binom n4-2\cdot\frac67\binom n4
=-\frac57\binom n4.
\]
Thus the least adjacency eigenvalue \(\tau\) satisfies
\[
\tau\ge-\frac57d,
\qquad d=\binom n4.
\]

Hoffman's ratio bound gives
\[
\frac{\alpha(\mathcal C_n)}{|\Gamma_n|}
 \le \frac{-\tau}{d-\tau}.
\]
Writing \(a=-\tau\le5d/7\), the right side is at most
\[
\frac{5d/7}{d+5d/7}=\frac5{12}.
\]
Therefore \(d_{K_4}(n)\le5/12\). \(\square\)

For \(n=7\), Lemma 3.1 shows that the least eigenvalue is exactly
\[
35-2\cdot30=-25.
\]
The theorem does not assert that the Hoffman bound is attained.

---

# 5. Every dense code has large total influence

Let \(f=1_{\mathcal A}\), where \(\mathcal A\subseteq\Gamma_n\) is a code of density
\[
\delta=\mathbb E f.
\]
For an edge coordinate \(e\), define
\[
I_e(f)=\mathbb P_G\bigl(f(G)\ne f(G+\{e\})\bigr)
      =\|f-\tau_e f\|_2^2.
\]

## Proposition 5.1
Every \(K_4\)-difference-free family satisfies
\[
\sum_{e\in E(K_n)}I_e(f)
 \ge \frac{\delta}{18}\binom n2.
\]

### Proof

For a four-set \(X\), independence gives
\[
\langle f,\tau_{k_X}f\rangle=0.
\]
Hence
\[
\|f-\tau_{k_X}f\|_2^2=2\delta.
\]
Order the six edges of \(K_n[X]\) arbitrarily and telescope the six single-coordinate translations. The triangle inequality followed by Cauchy–Schwarz gives
\[
2\delta
 \le 6\sum_{e\in E(K_n[X])}I_e(f).
\]
Thus
\[
\sum_{e\in E(K_n[X])}I_e(f)\ge\frac{\delta}{3}. \tag{5.1}
\]

Summing (5.1) over all \(X\in\binom{[n]}4\), and noting that each edge lies in \(\binom{n-2}{2}\) copies of \(K_4\), gives
\[
\binom{n-2}{2}\sum_e I_e(f)
 \ge \frac{\delta}{3}\binom n4.
\]
Since
\[
\frac{\binom n4}{\binom{n-2}{2}}
=\frac{n(n-1)}{12}
=\frac16\binom n2,
\]
the result follows. \(\square\)

This is compatible with constant-density highly nonmonotone functions, so by itself it does not prove vanishing.

---

# 6. Exact and approximate junta obstructions

Call an edge coordinate relevant if changing that coordinate can change membership in \(\mathcal A\).

## Proposition 6.1
Every nonempty \(K_4\)-difference-free family has at least
\[
\binom n2-\operatorname{ex}(n,K_4)
\]
relevant edge coordinates.

### Proof

Let \(J\) be the set of relevant coordinates. If \(E(K_n)\setminus J\) contained all six edges of some \(K_4\), then toggling that \(K_4\) would not change \(f\). Thus every member \(G\in\mathcal A\) would have \(G+k_X\in\mathcal A\), a contradiction. Therefore the graph with edge set \(E(K_n)\setminus J\) is \(K_4\)-free, and
\[
|E(K_n)\setminus J|\le\operatorname{ex}(n,K_4).
\]
\(\square\)

By Turán's theorem,
\[
\operatorname{ex}(n,K_4)=e(T_3(n))=\left\lfloor\frac{n^2}{3}\right\rfloor,
\]
so asymptotically at least one third of all edge variables must be relevant.

There is also a robust version. If \(g\) is a \(J\)-junta and \(E(K_n)\setminus J\) contains a \(K_4\) with vector \(k_X\), then \(\tau_{k_X}g=g\). Consequently,
\[
\sqrt{2\delta}
=\|f-\tau_{k_X}f\|_2
\le 2\|f-g\|_2.
\]
Thus
\[
\|f-g\|_2^2\ge\frac{\delta}{2}. \tag{6.1}
\]
A positive-density code is therefore bounded away in \(L^2\) from every junta whose relevant coordinates fail to hit all copies of \(K_4\).

---

# 7. Unate codes have exponentially vanishing density

A family is unate if, after complementing a fixed collection of coordinates, it becomes monotone increasing. Translation by a fixed graph preserves symmetric differences, so it suffices to handle monotone families.

## Proposition 7.1
Let \(\mathcal A\) be an increasing or decreasing \(K_4\)-difference-free family. Then
\[
\frac{|\mathcal A|}{2^N}
\le
\left(\frac{63}{64}\right)^{p_4(n)},
\]
where \(p_4(n)\) is the maximum number of edge-disjoint copies of \(K_4\) in \(K_n\). In particular,
\[
\frac{|\mathcal A|}{2^N}=\exp(-\Omega(n^2)).
\]
The same holds for every unate code.

### Proof

Suppose first that \(\mathcal A\) is increasing. If \(G\in\mathcal A\) and \(G[X]\) is empty for some four-set \(X\), then
\[
G+k_X=G\cup K_n[X]
\]
is a supergraph of \(G\), hence is also in \(\mathcal A\), a contradiction. Therefore every \(G\in\mathcal A\) contains at least one edge in every copy of \(K_4\).

Fix \(p_4(n)\) edge-disjoint copies of \(K_4\). Under the uniform random graph measure, the six-edge restrictions on these copies are independent. The probability that each is nonempty is
\[
\left(\frac{63}{64}\right)^{p_4(n)}.
\]

If \(\mathcal A\) is decreasing, then no \(G\in\mathcal A\) can contain all six edges of a \(K_4\), since deleting those edges would produce another member of \(\mathcal A\). The same independent-block estimate applies.

For the packing size, greedily remove edge-disjoint copies of \(K_4\) until the residual graph is \(K_4\)-free. If \(t\) copies were removed, then
\[
\binom n2-6t\le \operatorname{ex}(n,K_4),
\]
and hence
\[
p_4(n)\ge
\frac{\binom n2-\operatorname{ex}(n,K_4)}6
=\Theta(n^2).
\]
Finally, translating a unate family to a monotone one preserves both density and the forbidden-difference property. \(\square\)

---

# 8. Bounded-dimensional Fourier factors

This extends the elementary linear-code obstruction to nonlinear unions of cosets.

Use normalized Fourier coefficients
\[
\widehat f(F)=\mathbb E_G f(G)\chi_F(G).
\]
Let \(L\) be an \(r\)-dimensional linear subspace of the dual group, identified with an \(r\)-dimensional family of graphs.

Write \(R_q(m)\) for the \(q\)-color Ramsey number of \(K_m\).

## Proposition 8.1
If
\[
n\ge R_{2^r}(m),
\]
then for every \(K_4\)-difference-free \(f=1_{\mathcal A}\) of density \(\delta\),
\[
\sum_{F\in L}\widehat f(F)^2
\le d_{K_4}(m)\,\delta. \tag{8.1}
\]

### Proof

Choose a basis \(F_1,\dots,F_r\) of \(L\), and color every edge \(e\in E(K_n)\) by
\[
\bigl(1_{e\in F_1},\dots,1_{e\in F_r}\bigr)\in\mathbb F_2^r.
\]
There are at most \(2^r\) colors. By Ramsey's theorem, there is a set \(U\) of \(m\) vertices on which all edges receive the same color.

Consequently, for every four-set \(X\subseteq U\) and every \(F\in L\),
\[
|E(F)\cap E(K_n[X])|
\]
is either \(0\) or \(6\), modulo \(2\). Thus every \(F\in L\) annihilates every \(k_X\) with \(X\subseteq U\).

Let \(W\) be the span in \(\Gamma_n\) of these \(k_X\). Average \(f\) over \(W\):
\[
g(G)=\mathbb E_{w\in W} f(G+w).
\]
On each coset of \(W\), the restriction of \(\mathcal A\) is an independent set in a connected component of the \(m\)-vertex graph-code Cayley graph. All components are translates of one another, so their maximum independence ratio is \(d_{K_4}(m)\). Hence pointwise
\[
0\le g\le d_{K_4}(m).
\]
Also \(\mathbb E g=\delta\), and therefore
\[
\|g\|_2^2\le d_{K_4}(m)\delta.
\]

Fourier averaging over \(W\) retains exactly the characters in \(W^\perp\). Since \(L\subseteq W^\perp\), Parseval gives
\[
\sum_{F\in L}\widehat f(F)^2
\le
\sum_{F\in W^\perp}\widehat f(F)^2
=\|g\|_2^2
\le d_{K_4}(m)\delta.
\]
\(\square\)

### Consequences

- Taking \(m=4\), where \(d_{K_4}(4)=1/2\), shows that no bounded-dimensional Fourier factor can carry more than half the Fourier energy of a code once \(n\) is Ramsey-large.
- Taking \(m=7\) and Theorem 4.1 gives
  \[
  \sum_{F\in L}\widehat f(F)^2\le\frac5{12}\delta
  \]
  whenever \(n\ge R_{2^r}(7)\).
- If the entire Fourier support of \(f\) lies in a fixed \(r\)-dimensional subspace \(L\), then Parseval gives \(\delta\le d_{K_4}(m)\delta\), forcing \(\delta=0\). Thus no nonempty code can be an arbitrary union of cosets of a fixed-codimension subspace once \(n\) is sufficiently large.
- More quantitatively,
  \[
  \sum_{F\notin L}\widehat f(F)^2
  \ge \bigl(1-d_{K_4}(m)\bigr)\delta.
  \]
  Any hypothetical positive-density code must therefore have genuinely diffuse, high-dimensional Fourier spectrum.

---

# 9. Remaining gap

The central conjecture remains unresolved. The universal argument above stops at the constant
\[
d_{K_4}(n)\le\frac5{12}.
\]
The influence estimate only says that a dense code must be highly oscillatory, while arbitrary Boolean functions can indeed have total influence \(\Theta(n^2)\). Likewise, the Fourier result excludes bounded-dimensional or approximately bounded-dimensional parity structure, but it does not control a spectrum spread over exponentially many dense graph characters.

Thus a proof of \(d_{K_4}(n)=o(1)\) would need a new ingredient controlling highly nonmonotone, high-influence, Fourier-diffuse independent sets. The arguments here do not provide that step.