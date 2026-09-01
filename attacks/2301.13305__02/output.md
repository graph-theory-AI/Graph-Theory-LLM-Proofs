```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general case remains open, but I determine the linear maxima exactly for C4 and both two-edge graphs and up to constants for K1,4 and 4K2.",
  "would_publish": false,
  "caveats": "Only special cases are resolved; novelty was not literature-checked, and one displayed bound in the supplied catalog appears mistyped."
}
```

## 1. Statement and notation

Identify graphs on \([n]\) with the vector space
\[
V_n=\mathbb F_2^{E(K_n)},\qquad N=\binom n2.
\]
I interpret a linear graph-code as a vector subspace \(C\le V_n\). An affine subspace gives the same problem, since all pairwise differences lie in its translation subspace.

For a fixed graph \(H\), let
\[
L_H(n)=\max\{|C|:C\le V_n,\ C\text{ contains no copy of }H\}.
\]
This is equivalent to the original pairwise symmetric-difference condition because \(C\) is linear.

The results proved below include:

1. Exact formulas for \(H=P_3\), \(H=2K_2\), and \(H=C_4\).
2. \(L_{K_{1,4}}(n),L_{4K_2}(n)=\Theta(2^N/n^2)\).
3. \(L_{P_{\ell+1}}(n)=\Theta_\ell(2^N/n)\) for every fixed even \(\ell\).
4. General extremal-number and local-lemma bounds.

These do not settle arbitrary \(H\).

---

## 2. Syndrome-label reformulation

Let \(r_H(n)=N-\log_2 L_H(n)\), the minimum possible codimension.

### Lemma 2.1
The number \(r_H(n)\) is the minimum dimension of a binary vector space \(W\) admitting labels
\[
a_e\in W\qquad(e\in E(K_n))
\]
such that
\[
\sum_{e\in F}a_e\ne 0                                      \tag{2.1}
\]
for every copy \(F\) of \(H\).

#### Proof
If \(C\le V_n\) has codimension \(r\), take \(W=V_n/C\) and let \(a_e\) be the image of the basis vector corresponding to \(e\). Then
\[
\sum_{e\in F}a_e=F+C,
\]
which is nonzero exactly when \(F\notin C\).

Conversely, given such labels, define
\[
T:V_n\to W,\qquad T(x)=\sum_e x_ea_e.
\]
Then \(\ker T\) contains no \(H\)-copy. Replacing \(W\) by the span of the labels shows that its dimension is the codimension of \(\ker T\). ∎

Thus the problem asks for the fewest syndrome bits needed so that every \(H\)-copy has nonzero syndrome.

---

## 3. General quantitative bounds

Let \(h\) be the number of nonisolated vertices of \(H\), and let \(m=e(H)>0\).

### Proposition 3.1
For every fixed \(H\),
\[
L_H(n)\ge c_H\,\frac{2^N}{n^{h-2}}.                         \tag{3.1}
\]
If \(m\) is even, then
\[
L_H(n)\le 2^N\frac{\operatorname{ex}(n,H)}{N}.              \tag{3.2}
\]

#### Proof of the lower bound
Choose each edge label independently and uniformly from \(\mathbb F_2^r\). For every \(H\)-copy \(F\), let
\[
A_F=\left\{\sum_{e\in F}a_e=0\right\}.
\]
Then \(\Pr(A_F)=2^{-r}\).

An event \(A_F\) is independent of all events corresponding to edge-disjoint copies. A fixed edge belongs to at most
\[
2m\,n^{h-2}
\]
labelled embeddings of \(H\), so \(A_F\) is dependent on at most
\[
D\le 2m^2n^{h-2}
\]
other events. Taking
\[
r=\left\lceil\log_2\bigl(e(D+1)\bigr)\right\rceil,
\]
the symmetric Lovász local lemma gives a labeling with no bad event. Its kernel has size at least \(2^{N-r}\), which proves (3.1).

#### Proof of the upper bound
Let \(C\) have codimension \(r\), and use quotient labels \(a_e\in\mathbb F_2^r\). For each \(a\in\mathbb F_2^r\), consider the graph consisting of all edges with label \(a\).

Every such color class is \(H\)-free. Indeed, if all \(m\) edges of a copy of \(H\) had label \(a\), then, since \(m\) is even,
\[
\sum_{e\in H}a_e=ma=0,
\]
contrary to (2.1). Hence
\[
N\le 2^r\operatorname{ex}(n,H).
\]
Since \(|C|=2^{N-r}\), this gives (3.2). ∎

### Consequences

If \(H\) is bipartite with a bipartition having parts of sizes \(a\le b\), then \(H\subseteq K_{a,b}\). The standard common-neighborhood count
\[
\sum_{v}\binom{d(v)}a\le (b-1)\binom na
\]
in a \(K_{a,b}\)-free graph gives
\[
\operatorname{ex}(n,H)=O_H(n^{2-1/a}).
\]
Therefore
\[
L_H(n)=O_H\left(\frac{2^N}{n^{1/a}}\right).                 \tag{3.3}
\]

If \(H\) is a fixed forest on \(h\) nonisolated vertices, then
\[
\operatorname{ex}(n,H)\le (h-2)n.
\]
Indeed, a graph with more than \((h-2)n\) edges has a nonempty subgraph of minimum degree at least \(h-1\), into which every \(h\)-vertex forest embeds greedily. Consequently,
\[
L_H(n)=O_H\left(\frac{2^N}{n}\right)                        \tag{3.4}
\]
for every fixed forest with an even number of edges.

---

## 4. Exact solution for the two graphs with two edges

When \(H\) has exactly two edges, form the conflict graph \(X_H(n)\) whose vertices are the edges of \(K_n\), with two host edges adjacent when together they form a copy of \(H\).

Condition (2.1) becomes simply
\[
a_e+a_f\ne0,
\]
or \(a_e\ne a_f\), for every edge \(ef\) of \(X_H(n)\). Thus the labels are a proper coloring of \(X_H(n)\).

### Lemma 4.1
If \(e(H)=2\), then
\[
r_H(n)=\left\lceil\log_2\chi(X_H(n))\right\rceil.           \tag{4.1}
\]

Indeed, an \(r\)-dimensional binary space has at most \(2^r\) labels. Conversely, the colors of any proper \(\chi\)-coloring can be injected into \(\mathbb F_2^{\lceil\log_2\chi\rceil}\).

### Theorem 4.2: \(H=P_3\)

Here \(X_H(n)\) is the line graph of \(K_n\), so its chromatic number is the edge-chromatic number of \(K_n\):
\[
\chi'(K_n)=
\begin{cases}
n-1,&n\text{ even},\\
n,&n\text{ odd}.
\end{cases}
\]
Therefore, for \(n\ge3\),
\[
L_{P_3}(n)=
\begin{cases}
2^{N-\lceil\log_2(n-1)\rceil},&n\text{ even},\\[2mm]
2^{N-\lceil\log_2n\rceil},&n\text{ odd}.
\end{cases}                                                \tag{4.2}
\]

### Theorem 4.3: \(H=2K_2\)

Here \(X_H(n)\) is the Kneser graph \(KG(n,2)\), and
\[
\chi(KG(n,2))=n-2.
\]

For completeness, the upper bound is given by coloring \(\{i,j\}\), \(i<j\), by \(i\) when \(i\le n-2\), and coloring \(\{n-1,n\}\) by \(n-2\).

For the lower bound, every color class is an intersecting family of two-subsets. Such a family is either contained in a star or in a triangle. If \(q\le n-3\) colors sufficed, let \(s\) classes be star classes and delete one center from each. At least \(n-s\) vertices remain, and all their edges must be covered by the remaining \(q-s\) triangle classes. Hence
\[
\binom{n-s}{2}\le 3(q-s)\le3(n-3-s),
\]
contrary to
\[
\binom{k}{2}>3(k-3)\qquad(k\ge3).
\]
Thus
\[
L_{2K_2}(n)=2^{N-\lceil\log_2(n-2)\rceil},\qquad n\ge4.     \tag{4.3}
\]

---

## 5. Exact solution for \(C_4\)

### Theorem 5.1
For every \(n\ge4\),
\[
\boxed{L_{C_4}(n)=2^{N-\lceil\log_2n\rceil}.}               \tag{5.1}
\]

### Construction

Let \(r=\lceil\log_2n\rceil\), let \(Q=\mathbb F_{2^r}\), and choose distinct \(x_1,\dots,x_n\in Q\). Label
\[
a_{\{i,j\}}=x_ix_j\in Q,
\]
viewing \(Q\) as an \(r\)-dimensional binary vector space.

For a cycle \(i\,j\,k\,\ell\,i\),
\[
\begin{aligned}
a_{ij}+a_{jk}+a_{k\ell}+a_{\ell i}
 &=x_ix_j+x_jx_k+x_kx_\ell+x_\ell x_i\\
 &=(x_i+x_k)(x_j+x_\ell).
\end{aligned}
\]
The two factors are nonzero because the four vertices have distinct field labels. Hence every \(C_4\) has nonzero syndrome, proving
\[
r_{C_4}(n)\le\lceil\log_2n\rceil.
\]

### Lower bound

Suppose the edge labels lie in a binary space \(Q\) of order \(q=2^r\).

Fix two vertices \(u,w\). For every \(x\notin\{u,w\}\), put
\[
d_x=a_{ux}+a_{xw}.
\]
If \(x\ne y\), then the \(C_4\) \(u\,x\,w\,y\,u\) has syndrome \(d_x+d_y\), so the \(d_x\)'s are distinct. Thus
\[
q\ge n-2.                                                   \tag{5.2}
\]

It remains to rule out \(n=q+1\) and \(n=q+2\).

Choose a vertex \(\infty\) and switch the labels by
\[
a'_{ij}=a_{ij}+a_{\infty i}+a_{\infty j}.
\]
Every \(C_4\)-sum is unchanged, while \(a'_{\infty i}=0\). We suppress the primes.

#### Case 1: \(n=q+2\)

On the remaining \(q+1\) vertices, the labels on edges incident with any fixed vertex are pairwise distinct: this follows from the \(C_4\)'s passing through \(\infty\). Thus they give a proper \(q\)-edge-coloring of \(K_{q+1}\).

But \(q\) is even, so \(q+1\) is odd, and every matching in \(K_{q+1}\) has at most \(q/2\) edges. Hence \(q\) colors cover at most \(q^2/2\) edges, fewer than
\[
\binom{q+1}{2}=\frac{q(q+1)}2.
\]
Contradiction.

#### Case 2: \(n=q+1\)

Let \(U\) be the remaining set of \(q\) vertices. At each \(i\in U\), its \(q-1\) incident edge labels are distinct, so there is a unique missing element \(\mu_i\in Q\).

Fix distinct \(i,k\in U\). The values
\[
a_{ij}+a_{kj}\qquad(j\in U\setminus\{i,k\}),
\]
together with the value \(0\) arising from the intermediate vertex \(\infty\), are \(q-1\) distinct elements of \(Q\). Thus the displayed values are all nonzero elements except one, say \(h_{ik}\).

Define a symmetric \(q\times q\) array
\[
L_{ij}=
\begin{cases}
a_{ij},&i\ne j,\\
\mu_i,&i=j.
\end{cases}
\]
Every row is a permutation of \(Q\). Since \(q\ge4\), the sum of all elements of \(Q\) is zero. Hence
\[
0=\sum_{j\in U}(L_{ij}+L_{kj})
  =h_{ik}+\mu_i+\mu_k,
\]
so
\[
h_{ik}=\mu_i+\mu_k.
\]
Because \(h_{ik}\ne0\), all \(\mu_i\)'s are distinct.

Thus \(L\) is a symmetric Latin square in which each symbol occurs exactly once on the diagonal. Every symbol occurs \(q\) times in total, leaving \(q-1\) off-diagonal occurrences. But off-diagonal occurrences in a symmetric array come in pairs, whereas \(q-1\) is odd. Contradiction.

Therefore \(q\ge n\), so \(r\ge\lceil\log_2n\rceil\). This matches the construction and proves (5.1). ∎

---

## 6. Even paths

### Proposition 6.1
For every fixed even \(\ell\ge2\),
\[
L_{P_{\ell+1}}(n)=\Theta_\ell\left(\frac{2^N}{n}\right).    \tag{6.1}
\]

#### Proof
Choose distinct vectors \(\alpha_1,\dots,\alpha_n\in\mathbb F_2^t\), where \(t=\lceil\log_2n\rceil\), and label
\[
a_{ij}=\alpha_i+\alpha_j.
\]
For any graph \(F\),
\[
\sum_{ij\in E(F)}a_{ij}
   =\sum_{\substack{v\in V(F)\\ \deg_F(v)\text{ odd}}}\alpha_v. \tag{6.2}
\]
A path has exactly two odd-degree vertices, its endpoints, so its syndrome is the sum of two distinct \(\alpha\)'s and is nonzero. Thus
\[
L_{P_{\ell+1}}(n)\ge2^{N-\lceil\log_2n\rceil}.
\]

The upper bound follows from (3.4), since \(P_{\ell+1}\) is a forest and \(\ell\) is even. ∎

---

## 7. Even stars and matchings

The following finite-field construction is useful.

### Lemma 7.1
Let \(k\ge1\), \(F=\mathbb F_{2^t}\), and
\[
B_{k,t}=\{(x,x^3,\dots,x^{2k-1}):x\in F^\times\}\subseteq F^k.
\]
No nonempty subset of at most \(2k\) distinct elements of \(B_{k,t}\) has sum zero.

#### Proof
Suppose distinct nonzero \(x_1,\dots,x_s\), \(s\le2k\), satisfy
\[
\sum_i x_i^j=0
\]
for every odd \(j\le2k-1\). By Frobenius, all power sums of degrees \(1,\dots,s\) vanish. Newton's identities then imply that every odd elementary symmetric function of the \(x_i\)'s vanishes.

If \(s\) is odd, this includes their product, impossible because all \(x_i\ne0\). If \(s\) is even, the polynomial
\[
\prod_{i=1}^s(z+x_i)
\]
contains only even powers of \(z\), so its derivative is identically zero. This is impossible for a polynomial with distinct roots. ∎

### Proposition 7.2
For each fixed \(k\ge2\),
\[
\Omega_k\left(\frac{2^N}{n^k}\right)
 \le L_{K_{1,2k}}(n),\,L_{2kK_2}(n)
 \le O_k\left(\frac{2^N}{n^2}\right).                       \tag{7.1}
\]

#### Lower bounds
Take \(t=\lceil\log_2(n+1)\rceil\) and choose \(n\) elements
\(\alpha_1,\dots,\alpha_n\in B_{k,t}\).

For \(K_{1,2k}\), label
\[
a_{ij}=\alpha_i+\alpha_j.
\]
The center contribution occurs \(2k\) times and cancels, leaving the sum of the \(2k\) distinct leaf labels.

For \(2kK_2\), order the vertices and label
\[
a_{\{i,j\}}=\alpha_{\min\{i,j\}}.
\]
In a matching, the smaller endpoints of its edges are distinct. Lemma 7.1 therefore gives nonzero syndrome in both cases. The label space has dimension at most \(kt\), proving the lower bounds.

#### Upper bounds
Let \(G\) be a binary group of order \(q\), and suppose
\[
b_1,\dots,b_M\in G
\]
have no \(2k\) distinct indices whose labels sum to zero. Each group element occurs at most \(2k-1\) times, so the support \(A\) of the sequence has size
\[
|A|\ge\frac{M}{2k-1}.
\]

Let \(T_{2k}(A)\) count ordered \(2k\)-tuples from \(A\) summing to zero. Fourier expansion gives
\[
T_{2k}(A)
 =\frac1q\sum_{\chi}\left(\sum_{a\in A}\chi(a)\right)^{2k}
 \ge\frac{|A|^{2k}}q.
\]
Every such tuple has a repeated coordinate. For any specified equal pair of positions there are at most \(|A|^{2k-2}\) possibilities, so
\[
T_{2k}(A)\le \binom{2k}{2}|A|^{2k-2}.
\]
Consequently
\[
q\ge \frac{|A|^2}{\binom{2k}{2}}=\Omega_k(M^2).             \tag{7.2}
\]

For the star, take the \(M=n-1\) labels on the edges incident with one center. For the matching, restrict to the edges of a fixed matching of size \(\lfloor n/2\rfloor\). Equation (7.2) gives \(q=\Omega_k(n^2)\), hence the upper bounds. ∎

For \(k=2\), the bounds match:

### Corollary 7.3
\[
L_{K_{1,4}}(n)=\Theta\left(\frac{2^N}{n^2}\right),\qquad
L_{4K_2}(n)=\Theta\left(\frac{2^N}{n^2}\right).              \tag{7.3}
\]

One can make the upper estimates explicit. If a sequence of \(M\) labels has no four distinct indices summing to zero, then at most one label is repeated, and it occurs at most three times. Hence the support has size at least \(M-2\). All sums of two distinct support elements are different, giving
\[
q\ge1+\binom{M-2}{2}.
\]
Thus
\[
L_{K_{1,4}}(n)
 \le \frac{2^N}{1+\binom{n-3}{2}},
\]
and, for \(n\ge8\),
\[
L_{4K_2}(n)
 \le \frac{2^N}{1+\binom{\lfloor n/2\rfloor-2}{2}}.
\]

---

## 8. Status, gaps, and a consistency issue

The arbitrary fixed-\(H\) problem remains open. In particular:

- For \(K_{1,2k}\) and \(2kK_2\) with \(k\ge3\), Proposition 7.2 leaves a gap between normalized sizes \(n^{-k}\) and \(n^{-2}\).
- For nonbipartite even-edge \(H\), the extremal-number bound (3.2) may only give a constant-factor loss.
- Eulerian graphs beyond \(C_4\) are not handled by the vertex-potential construction (6.2).

There is also a definite transcription issue in the supplied catalog review. The literal upper bound
\[
2^{\binom n2/n^{\varepsilon_H}}
\]
cannot hold for a fixed \(H\) under the standard definition of a linear code: Proposition 3.1 gives
\[
L_H(n)\ge 2^{N-O_H(\log n)}.
\]
The phrase “polynomial suppression” suggests that the intended bound was likely
\[
O\!\left(\frac{2^N}{n^{\varepsilon_H}}\right),
\]
but I have not independently checked the exact statement of the cited paper. I also have not verified whether the exact \(C_4\) formula above already appears in that paper or elsewhere.