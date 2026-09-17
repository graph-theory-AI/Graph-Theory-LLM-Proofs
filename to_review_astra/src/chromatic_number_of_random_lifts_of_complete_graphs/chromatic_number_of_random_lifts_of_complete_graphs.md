---
title: 'Chromatic number of random lifts of complete graphs'
subtitle: 'Unrefereed candidate proof by GPT-6 Astra'
author:
  - 'Writeup: `gpt-6-astra` (single model pass)'
date: 'Catalog id `chromatic_number_of_random_lifts_of_complete_graphs` — generated 2026-09-16'
---

::: {.warning}
**UNREFEREED MODEL OUTPUT.** This document was selected solely because GPT-6 Astra labelled its own result `would_publish: true` and returned `proved` or `disproved`. It has not passed the adversarial LLM referee used for the earlier Sol campaign, has not been checked by a human mathematician, and has not been checked for novelty. Treat every mathematical and bibliographic claim below as unverified.
:::

# Summary and provenance

| | |
|:--|:--|
| Catalog id | `chromatic_number_of_random_lifts_of_complete_graphs` |
| Catalog entry | [Chromatic number of random lifts of complete graphs](https://graph-theory-ai.github.io/graph-conjectures/op/chromatic_number_of_random_lifts_of_complete_graphs/) |
| Source corpus | opg |
| Campaign leg | OpenProblemGarden first pass (`attacks_opg`) |
| Source paper / entry | http://www.openproblemgarden.org/op/chromatic_number_of_random_lifts_of_complete_graphs |
| Model verdict | **proved** (confidence: high) |
| Model's one-line claim | A random h-lift of K_5 has chromatic number 3 asymptotically almost surely. |
| Model | `gpt-6-astra`, reasoning effort `max`, `mode=pro`, flex service tier |
| Original artifact | `attacks_opg/chromatic_number_of_random_lifts_of_complete_graphs/output.md` |
| Independent review | **None** |
| Model's caveats | Novelty relative to the full cited literature has not been independently checked. |

# Problem statement

Question Is the chromatic number of a random lift of $K_5$ concentrated on a single value?

## Catalog context

Let $G$ be a graph with vertex set $V$ and edge set $E$ . An $h$ -lift $H$ is a graph with vertex set $V\times\{1,\dots,h\}$ , such that $(u,k)$ and $(v,\ell)$ may only be adjacent in $H$ if $uv \in E$ , and for each $uv\in E$ , the edges between $\{u\}\times\{1,\dots,h\}$ and $\{v\}\times\{1,\dots,h\}$ form a perfect matching. A random $h$ -lift of $G$ is a graph drawn uniformly at random from the set of all $h$ -lifts of $G$ . This amounts to choosing, independently at random, a perfect matching for each edge of $G$ . One is generally interested in properties of random $h$ -lifts when $h\to\infty$ . Amit, Linial, and Matousek [ALM02] have studied the chromatic number of random lifts. They ask whether a the chromatic number of a random $h$ -lift of $K_5$ is asymptotically almost surely a single number. It is easy to see that this number may be either 3 or 4. Farzad and Theis [FT12] have shown that random lifts of $K_5\setminus e$ are asymptotically almost surely 3-colorable. A more general question is this. Question Is the chromatic number of a random lift of $K_n$ concentrated on a single value? Amit, Linial, and Matousek [ALM02] have shown that the chromatic number of a random lift of $K_n$ is in $\Theta(n/\log n)$ .

# Astra writeup

*The text below is the model output verbatim, apart from moving its machine-readable verdict block into the summary above and shifting Markdown heading levels for this document. Mechanical TeX defects and equation tags were normalized where needed for compilation.*

## Theorem

Let \(H_n\) be a random \(n\)-lift of \(K_5\). Then
\[
\Pr\bigl(\chi(H_n)=3\bigr)\longrightarrow 1.
\]

The main point is an entropy inequality that gives a unique global maximum for the second moment of fibre-balanced 3-colourings. The local second-moment calculation then matches the short-cycle contribution exactly, allowing small-subgraph conditioning.

All logarithms below are natural.

### 1. Balanced colourings and overlap matrices

Choose integers \(t_1,t_2,t_3\) summing to \(n\), each differing from \(n/3\) by at most \(1\), and put
\[
p=(t_1/n,t_2/n,t_3/n).
\]
Let \(Z_n\) count proper 3-colourings of \(H_n\) in which every fibre has exactly \(t_a\) vertices of colour \(a\).

Write
\[
M_n=\frac{n!}{t_1!t_2!t_3!}.
\]
If \(a_n\) is the probability that a uniform perfect matching between two such coloured fibres respects the colouring, then
\[
\mathbb E Z_n=M_n^5a_n^{10}.                                      \qquad\text{(1)}
\]

For two independently chosen balanced colourings, their overlap in fibre \(i\) is the matrix
\[
\rho_i(a,b)=\frac1n
 \bigl|\{x:\text{the two colours of }x\text{ are }a,b\}\bigr|.
\]
Its row and column sums are \(p\). Independently for the five fibres,
\[
\Pr(\rho_i=\rho)
 =\frac{\prod_{a=1}^3(t_a!)^2}
        {n!\prod_{a,b=1}^3(n\rho(a,b))!}.                         \qquad\text{(2)}
\]

Let \(q_n(\rho,\sigma)\) be the probability that a uniform matching between fibres with overlaps \(\rho,\sigma\) respects both colourings. Thus
\[
\frac{\mathbb E Z_n^2}{(\mathbb E Z_n)^2}
 =
 \mathbb E_{\rho_1,\ldots,\rho_5}
 \prod_{ij\in E(K_5)}\frac{q_n(\rho_i,\rho_j)}{a_n^2}.             \qquad\text{(3)}
\]

We first establish a global bound on this sum.

### 2. The entropy inequality

Let \(U\) be the \(3\times3\) matrix with all entries \(1/9\). For a nonnegative matrix \(\rho\) of total mass \(1\), define
\begin{equation*}
\begin{split}
H(\rho)&=-\sum_{a,b}\rho(a,b)\log\rho(a,b),\\
L(\rho)&=\sum_{a,b}\rho(a,b)\log\bigl(\tfrac13+\rho(a,b)\bigr),\\
F(\rho)&=H(\rho)+2L(\rho).
\end{split}
\end{equation*}
As usual, \(0\log0=0\).

#### Lemma 1
There is \(c>0\) such that, for every nonnegative \(3\times3\) matrix whose row sums are \(1/3\),
\[
F(\rho)\le F(U)-c\|\rho-U\|_F^2,
\qquad
F(U)=2\log(4/3).                                                  \qquad\text{(4)}
\]

##### Proof

Put
\[
g(x)=2x\log(1+x)-x\log x,\qquad 0\le x\le1.
\]
We claim that
\[
g(x_1)+g(x_2)+g(x_3)\le 3g(1/3)
\quad\text{if }x_1+x_2+x_3=1,                                   \qquad\text{(5)}
\]
with equality only at \(x_1=x_2=x_3=1/3\).

Indeed,
\[
g''(x)=\frac{x^2+2x-1}{x(1+x)^2}.
\]
Thus \(g\) is strictly concave below \(r=\sqrt2-1\), and strictly convex above \(r\). A maximizer in (5) is interior, since \(g'(0+)=+\infty\). At an interior maximizer, two coordinates cannot both exceed \(r\): varying those two coordinates with fixed sum would give a positive second derivative.

If all coordinates are at most \(r\), concavity proves (5). Otherwise, writing the exceptional coordinate as \(x>r\), concavity on the other two coordinates gives the upper bound
\[
\phi(x)=g(x)+2g((1-x)/2).
\]
For \(1/3\le x<1\),
\[
\phi''(x)=
\frac{x^4-10x^3-32x^2+34x-9}
{x(1+x)^2(1-x)(3-x)^2}<0.
\]
To verify the sign, the numerator is at most
\[
-\frac{103}{3}x^2+34x-9,
\]
whose discriminant is \(-80\). Since \(\phi'(1/3)=0\), we have
\(\phi(x)<\phi(1/3)\) for \(x>1/3\). This proves (5), including uniqueness.

Apply (5) to each row of \(x_{ab}=3\rho(a,b)\). Since
\[
F(\rho)=-\log3+\frac13\sum_{a,b}g(3\rho(a,b)),
\]
the unique maximum is \(U\).

Finally, the Hessian of \(F\) at \(U\) is
\[
-\frac98 I
\]
in the nine entry coordinates. Strict quadratic decrease near \(U\), together with compactness and uniqueness of the maximum, gives (4). \(\square\)

For the rounded row sums \(p\) used above, the following uniform version follows:
\[
F(\rho)\le F(U)-c'\|\rho-U\|_F^2
                    +O\!\left(\frac{\log n}{n}\right).           \qquad\text{(6)}
\]
Indeed, rescale row \(a\) by \(1/(3p_a)\). This changes the matrix by \(O(1/n)\) in total variation. The resulting change in entropy is \(O((\log n)/n)\), and the change in \(L\) is \(O(1/n)\).

#### A permanent bound

We shall use
\[
\operatorname{per}(A)\le \prod_{v}(r_v!)^{1/r_v}                  \qquad\text{(7)}
\]
for a zero-one matrix with row sums \(r_v>0\).

Here is the entropy proof, to specify the inequality being used. Take a uniform permitted permutation and expose its rows in a uniformly random order. The conditional entropy of the image of a row is at most the logarithm of its number of still-available permitted columns. For a fixed permitted permutation, these columns are occupied by \(r_v\) rows, including the given row. Its rank among those rows is uniform, so the expected logarithm of the number remaining is
\(\log(r_v!)/r_v\). Sum the entropy bounds over rows.

For the matching defining \(q_n(\rho,\sigma)\), a vertex of type \((a,b)\) has
\[
n\bigl(1-p_a-p_b+\sigma(a,b)\bigr)
\]
permitted partners. These numbers are uniformly at least \(n/4\) for large \(n\). Consequently, (7) and Stirling's formula give
\[
\log q_n(\rho,\sigma)
 \le n\sum_{a,b}\rho(a,b)
                \log\bigl(\tfrac13+\sigma(a,b)\bigr)+O(\log n),  \qquad\text{(8)}
\]
uniformly over all feasible overlaps.

The same bound holds with \(\rho,\sigma\) exchanged. Moreover,
\begin{equation*}
\begin{split}
&\sum_{a,b}\rho(a,b)\log(\tfrac13+\sigma(a,b))
 +\sum_{a,b}\sigma(a,b)\log(\tfrac13+\rho(a,b))\\
&\hspace{20mm}\le L(\rho)+L(\sigma),                              \qquad\text{(9)}
\end{split}
\end{equation*}
because each term in
\[
\sum_{a,b}(\rho(a,b)-\sigma(a,b))
 \bigl(\log(\tfrac13+\rho(a,b))-\log(\tfrac13+\sigma(a,b))\bigr)
\]
is nonnegative. Hence
\[
\log q_n(\rho,\sigma)
 \le \frac n2\bigl(L(\rho)+L(\sigma)\bigr)+O(\log n).              \qquad\text{(10)}
\]

This is the global estimate needed for the second moment.

### 3. A finite-type matching calculation

We record the local matching asymptotic, including the prefactor.

Let \(A\) be a symmetric zero-one matrix of order \(s\), with every row sum \(r\), and put \(P=A/r\). Write \(u=(1/s,\ldots,1/s)\). Assume:

* \(I-P^2\) is positive definite on \(\mathbf1^\perp\);
* the integer vectors \(e_j-e_k\), where columns \(j,k\) occur together in some row support of \(A\), generate the full zero-sum integer lattice.

For integer type counts \(n\alpha,n\beta\), let \(Q_A(n;\alpha,\beta)\) be the probability that a uniform matching respects the allowed type pairs \(A\).

#### Lemma 2
Uniformly when
\[
\|\alpha-u\|+\|\beta-u\|=O(n^{-2/5}),
\]
we have
\begin{equation*}
\begin{split}
Q_A(n;\alpha,\beta)
={}&\left(\frac rs\right)^n
 \det_{\mathbf1^\perp}(I-P^2)^{-1/2}\\
&\quad{}\times
 \exp\left\{\frac{ns}{2}
 \left[
 \|\beta-u\|^2
 -\left\langle w,(I-P^2)^{-1}w\right\rangle
 \right]\right\}(1+o(1)),                                      \qquad\text{(11)}\\
&w=\beta-u-P(\alpha-u).
\end{split}
\end{equation*}
The error is uniform on each such region with a fixed implied constant.

##### Proof

For every left vertex, independently choose one of its \(r\) permitted right types uniformly. Let \(S\) be the resulting vector of right-type counts. An exact counting identity is
\[
Q_A(n;\alpha,\beta)
 =
 \left(\frac rs\right)^n
 \frac{\Pr(S=n\beta)}
 {\Pr(\operatorname{Mult}(n,u)=n\beta)}.                         \qquad\text{(12)}
\]

The mean of \(S/n\) is \(P\alpha\). At \(\alpha=u\), its covariance divided by \(n\), restricted to \(\mathbf1^\perp\), is
\[
\Sigma_0=\frac1s(I-P^2).
\]

For completeness, exponential tilting gives the required uniform local estimate as follows. The normalized log moment-generating function of \(S\) is
\[
K_\alpha(t)
 =\sum_i\alpha_i\log\left(\sum_j P_{ij}e^{t_j}\right).
\]
On \(\mathbf1^\perp\),
\[
K_\alpha(t)
 =\langle P\alpha,t\rangle
  +\frac12\langle t,\Sigma_0t\rangle
  +O\bigl(\|\alpha-u\|\|t\|^2+\|t\|^3\bigr).
\]
The tilt giving mean \(n\beta\) is
\[
t=\Sigma_0^{-1}w+O\bigl((\|\alpha-u\|+\|\beta-u\|)^2\bigr).
\]
Thus its rate function is
\[
I_\alpha(\beta)
 =\frac12\langle w,\Sigma_0^{-1}w\rangle
  +O\bigl((\|\alpha-u\|+\|\beta-u\|)^3\bigr).                    \qquad\text{(13)}
\]

Fourier inversion under this tilt gives a Gaussian local prefactor. The lattice assumption ensures that the only maximum-modulus point on the dual torus is the trivial one. Away from its neighbourhood, the integrand decays exponentially, uniformly for the parameters in question; near it, the positive-definite covariance and the Taylor expansion give the Gaussian integral. The lattice constant is the same as for the multinomial distribution in the denominator of (12).

The determinant ratio is therefore
\(\det_{\mathbf1^\perp}(I-P^2)^{-1/2}\). The multinomial rate function is
\[
D(\beta\|u)=\frac s2\|\beta-u\|^2+O(\|\beta-u\|^3).
\]
Since \(n\,O(n^{-6/5})=o(1)\), substituting these estimates into (12) proves (11). \(\square\)

We use the lemma for two matrices:
\[
A_0=J_3-I_3,
\qquad
A_1=A_0\otimes A_0.
\]
For both, any two columns occur together in a row support, so the lattice hypothesis holds.

The eigenvalues of \(P_0=A_0/2\) are
\[
1,-\tfrac12,-\tfrac12.
\]
It follows that
\[
a_n=\frac43\left(\frac23\right)^n(1+o(1)).                       \qquad\text{(14)}
\]
In particular, (1) gives
\[
\mathbb E Z_n=\Theta(n^{-5})(4/3)^{5n}.                          \qquad\text{(15)}
\]

For \(P_1=A_1/4=P_0\otimes P_0\), the eigenvalues are
\[
1,\quad -\tfrac12\ \text{(multiplicity 4)},\quad
\tfrac14\ \text{(multiplicity 4)}.                              \qquad\text{(16)}
\]

### 4. The second moment

#### 4.1. All noncentral overlaps are negligible

By (2) and Stirling's formula, uniformly over feasible overlaps,
\[
\log\Pr(\rho_i=\rho)
 =n\bigl(H(\rho)-2H(p)\bigr)+O(\log n).                          \qquad\text{(17)}
\]
Also \(H(p)=\log3+O(n^{-2})\).

Combining (10), (14), and (17), the contribution to (3) of any specified five overlaps is at most
\[
\exp\left\{
 n\sum_{i=1}^5\bigl(F(\rho_i)-F(U)\bigr)+O(\log n)
\right\}.                                                       \qquad\text{(18)}
\]
Here the coefficient \(2L(\rho_i)\) is exactly where 4-regularity is used.

Put
\[
C_n=pp^{\mathsf T}.
\]
By (6), the sum in (3) over profiles for which some
\[
\|\rho_i-C_n\|_F>n^{-2/5}                                       \qquad\text{(19)}
\]
is \(o(1)\). Indeed, \(C_n-U=O(1/n)\), so (18) is at most a fixed polynomial in \(n\) times \(\exp(-c n^{1/5})\), and the number of overlap profiles is polynomial in \(n\).

Thus only the central region remains.

#### 4.2. The central Gaussian integral

Let
\[
\mathcal T=\{X\in\mathbb R^{3\times3}:
                  X\mathbf1=X^{\mathsf T}\mathbf1=0\},
\]
a four-dimensional Euclidean space, and write
\[
z_i=3\sqrt n\,(\rho_i-C_n)\in\mathcal T.
\]

Uniformly in the central region, Stirling's formula applied to (2) gives
\[
\Pr(\rho_i=\rho)
 =
 \frac{729}{(2\pi n)^2}
 \exp\bigl(-\|z_i\|_F^2/2\bigr)(1+o(1)).                        \qquad\text{(20)}
\]
There is no divisibility restriction here. The integer row-and-column-zero lattice in \(\mathcal T\) has covolume \(9\): the usual basis
\((e_a-e_3)(e_b-e_3)^{\mathsf T}\), \(a,b\in\{1,2\}\), has Gram determinant \(81\). Consequently, the \(z_i\)-lattice has covolume \(729/n^2\), as required by (20).

On \(\mathcal T\), \(P_1\) acts as multiplication by \(1/4\). Lemma 2, (14), and (16) therefore give
\[
\frac{q_n(\rho_i,\rho_j)}{a_n^2}
 =
 \left(\frac{16}{15}\right)^2
 \exp\left\{
 \frac4{15}\langle z_i,z_j\rangle
 -\frac1{30}\bigl(\|z_i\|^2+\|z_j\|^2\bigr)
 \right\}(1+o(1)).                                              \qquad\text{(21)}
\]
Replacing \(U\) by \(C_n\) in this expression changes the exponent by \(o(1)\), uniformly in the central region, because \(C_n-U=O(1/n)\).

Let \(A\) now denote the adjacency matrix of \(K_5\), and set
\[
M=\frac{19I_5-4A}{15}.                                         \qquad\text{(22)}
\]
Combining (20) and (21), the quadratic form for each of the four coordinates in \(\mathcal T\) is \(M\).

The eigenvalues of \(M\) are
\[
\frac15\quad\text{once},\qquad
\frac{23}{15}\quad\text{four times}.                            \qquad\text{(23)}
\]
In particular, it is positive definite. The lattice sums converge to Gaussian integrals; the central-region radius in \(z\)-coordinates tends to infinity. We obtain
\[
\frac{\mathbb E Z_n^2}{(\mathbb E Z_n)^2}
 \longrightarrow
 R:=\left(\frac{16}{15}\right)^{20}\det(M)^{-2}.                 \qquad\text{(24)}
\]
Explicitly,
\[
R=25\left(\frac{16}{15}\right)^{20}
       \left(\frac{15}{23}\right)^8<\infty.                     \qquad\text{(25)}
\]

The next step identifies all of this limiting variance with short cycles.

### 5. Short cycles

Let \(B\) be the nonbacktracking matrix of \(K_5\), indexed by its 20 directed edges:
\[
B_{(u,v),(v,w)}=1\quad\Longleftrightarrow\quad w\ne u.
\]
For \(\ell\ge3\), define
\[
\mu_\ell=\frac{\operatorname{tr}(B^\ell)}{2\ell},
\qquad
\delta_\ell=2(-1/2)^\ell.                                      \qquad\text{(26)}
\]
Let \(X_{\ell,n}\) count unoriented simple \(\ell\)-cycles in \(H_n\).

For each fixed finite list of lengths, the \(X_{\ell,n}\) converge jointly to independent Poisson variables of means \(\mu_\ell\). Here is the counting argument.

A cycle in the lift projects to a cyclically nonbacktracking closed walk in the base. For a specified projected walk, the number of choices of distinct lift vertices is \(n^\ell(1+O(1/n))\), and the probability of its required matching edges is \(n^{-\ell}(1+O(1/n))\). Dividing rooted oriented cycles by \(2\ell\) gives (26). In joint factorial moments, vertex-disjoint cycles give the product of these contributions. An overlapping union of distinct cycles has more edges than vertices, and contributes \(O(1/n)\). This proves the stated Poisson limits.

#### Size-biased cycle counts

Consider the probability measure with density \(Z_n/\mathbb E Z_n\). It has the following exact construction:

1. choose independently a uniform balanced colouring in each fibre;
2. independently for each base edge, choose a uniform matching that respects this colouring.

For any fixed collection of \(r\) disjoint, colour-compatible prescribed edges in one matching, the probability that all occur is
\[
\left(\frac{3}{2n}\right)^r(1+o(1)).                            \qquad\text{(27)}
\]
To verify this, remove their endpoints. The ratio of the remaining permissible matching count to the original one is
\[
\frac{(n-r)!}{n!}\,
\frac{Q_{A_0}(n-r;\alpha',\beta')}
     {Q_{A_0}(n;p,p)},
\]
where \(\alpha',\beta'=(1/3,1/3,1/3)+O(1/n)\). Lemma 2 and (14) give (27).

On a fixed set of vertices, the planted colours are asymptotically independent uniform colours. An \(\ell\)-cycle has
\[
2^\ell+2(-1)^\ell
\]
proper 3-colourings. Consequently, its relative probability under the size-biased measure is
\[
3^{-\ell}\bigl(2^\ell+2(-1)^\ell\bigr)
          \left(\frac32\right)^\ell
 =1+\delta_\ell.                                                \qquad\text{(28)}
\]

The same disjoint-cycle and overlapping-union enumeration now gives, for every fixed finitely supported sequence of nonnegative integers \(b_\ell\),
\[
\frac{
 \mathbb E\!\left[Z_n\prod_{\ell\ge3}(X_{\ell,n})_{b_\ell}\right]}
 {\mathbb E Z_n}
 \longrightarrow
 \prod_{\ell\ge3}
 \bigl(\mu_\ell(1+\delta_\ell)\bigr)^{b_\ell}.                    \qquad\text{(29)}
\]
Thus the finite-dimensional cycle limits under size bias are independent Poisson variables of means \(\mu_\ell(1+\delta_\ell)\).

### 6. Exact matching of the variance

Since \(B\) has row sum \(3\),
\[
\sum_{\ell\ge3}\mu_\ell\delta_\ell^2<\infty.
\]
Moreover, \(\operatorname{tr}B=\operatorname{tr}B^2=0\), and
\begin{equation*}
\begin{split}
\sum_{\ell\ge3}\mu_\ell\delta_\ell^2
 &=2\sum_{\ell\ge1}\frac{\operatorname{tr}(B^\ell)}{\ell\,4^\ell}\\
 &=-2\log\det(I-B/4).                                          \qquad\text{(30)}
\end{split}
\end{equation*}

For clarity, the determinant identity needed here is
\[
\det(I-uB)=(1-u^2)^5\det(I-uA+3u^2I).                          \qquad\text{(31)}
\]
It follows directly by writing \(B=XY-J\), where \(J\) reverses directed edges, \(X\) is head-incidence and \(Y\) is tail-incidence. Then
\[
J^2=I,\qquad YX=A,\qquad YJX=4I,
\]
and the determinant lemma applied to \(I+uJ-uXY\) gives (31).

At \(u=1/4\),
\[
I-uA+3u^2I=\frac{15}{16}M.
\]
Hence
\[
\det(I-B/4)=\left(\frac{15}{16}\right)^{10}\det M.
\]
Together with (24) and (30), this proves
\[
R=\exp\left(\sum_{\ell\ge3}\mu_\ell\delta_\ell^2\right).          \qquad\text{(32)}
\]

### 7. Small-subgraph conditioning, with the positivity step

We include the conditioning argument rather than merely invoking it.

Let \(P_\ell\), \(\ell\ge3\), be independent Poisson variables of means \(\mu_\ell\), and put
\[
W_L=\prod_{\ell=3}^L
       (1+\delta_\ell)^{P_\ell}e^{-\mu_\ell\delta_\ell}.
\]
These form a mean-one martingale, and
\[
\mathbb E W_L^2
 =\exp\left(\sum_{\ell=3}^L\mu_\ell\delta_\ell^2\right)\le R.
\]
Thus \(W_L\) converges in \(L^2\) to some \(W\).

Furthermore, \(W>0\) almost surely. Indeed,
\[
\log W_L
 =\sum_{\ell=3}^L
   (P_\ell-\mu_\ell)\log(1+\delta_\ell)
 +\sum_{\ell=3}^L
   \mu_\ell\bigl(\log(1+\delta_\ell)-\delta_\ell\bigr).
\]
The first series converges almost surely because its variances are summable; the second converges absolutely. Here we use \(\delta_\ell\to0\), \(\delta_\ell>-1\), and the finiteness of the sum in (32).

Now set \(Y_n=Z_n/\mathbb E Z_n\), and condition on
\((X_{3,n},\ldots,X_{L,n})\). The original and size-biased Poisson limits imply that, at each fixed count vector, the limiting conditional mean is the corresponding likelihood ratio \(W_L\). Therefore
\[
\mathbb E[Y_n\mid X_{3,n},\ldots,X_{L,n}]
 \ \xrightarrow{\mathrm d}\ W_L
\]
and, by summing over finite sets of count vectors,
\[
\liminf_{n\to\infty}
 \mathbb E\!\left[
   \mathbb E[Y_n\mid X_{3,n},\ldots,X_{L,n}]^2
 \right]
 \ge \mathbb E W_L^2.
\]
Using (24), the conditional-variance identity yields
\[
\limsup_{n\to\infty}
\mathbb E\!\left[
 \left(Y_n-\mathbb E[Y_n\mid X_{3,n},\ldots,X_{L,n}]\right)^2
\right]
\le R-\mathbb E W_L^2.
\]
The right side tends to zero as \(L\to\infty\), by (32). Consequently,
\[
Y_n\xrightarrow{\mathrm d}W.
\]
Since \(W>0\) almost surely and \(Y_n\ge0\),
\[
\Pr(Z_n=0)\longrightarrow0.                                    \qquad\text{(33)}
\]

This proves that \(H_n\) is a.a.s. 3-colourable. The rounded choices \(t_a=n/3+O(1)\) used throughout show that (33) holds along all integers \(n\), not merely multiples of \(3\).

### 8. Excluding chromatic number 2

Suppose a lift of \(K_5\) has a proper 2-colouring, and let \(s_i\) be the number of vertices of its first colour in fibre \(i\). Every base-edge matching forces
\[
s_i+s_j=n.
\]
Since the base contains triangles, all \(s_i=n/2\). Thus no such colouring exists when \(n\) is odd.

For even \(n\), the expected number of proper 2-colourings is exactly
\[
\binom{n}{n/2}^{5}
 \left(\frac{((n/2)!)^2}{n!}\right)^{10}
 =\binom{n}{n/2}^{-5}=o(1).
\]
Therefore \(H_n\) is a.a.s. nonbipartite. Combining this with (33) gives
\[
\boxed{\Pr\bigl(\chi(H_n)=3\bigr)\longrightarrow1.}
\]

### Scope and literature caveat

The argument also gives a.a.s. 3-colourability for random lifts of any fixed simple 4-regular base: the global entropy estimate is unchanged, and the corresponding Gaussian matrix
\[
(19I-4A)/15
\]
is positive definite because every adjacency eigenvalue is at most \(4\). The same determinant and cycle-conditioning calculation applies.

No unproved graph-theoretic conjecture is used above. I have not checked the full cited 2021 preprint or independently established whether this entropy/permanent argument already appears in the literature, so I am not asserting bibliographic novelty.
