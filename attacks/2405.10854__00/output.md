```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is not resolved, but exact formulas prove log-concavity for bouquets, dipoles, and several infinite bridge-closed classes, while a bridge-power criterion gives a concrete route to a counterexample.",
  "would_publish": false,
  "caveats": "No graph satisfying the counterexample criterion is identified; formulas use the standard fixed-graph rotation-system convention."
}
```

# Mathematical writeup

## 1. Statement and convention

For a connected graph \(G\), let

\[
\Gamma_G(t)=\sum_{g\ge 0}a_g(G)t^g
\]

be its orientable genus polynomial. I use the standard convention that a combinatorial embedding of a fixed graph is a rotation system: the darts of \(G\) are distinguished, and equivalence fixes \(G\). If one instead quotients by \(\operatorname{Aut}(G)\), Burnside corrections are needed and several enumerative formulas below no longer hold literally.

Let \(D(G)\) be the dart set, let \(\alpha\) be the fixed-point-free involution pairing the two darts of every edge, and let \(\sigma\) be the product of the cyclic rotations at the vertices. The faces are the cycles of \(\sigma\alpha\). If

\[
\beta(G)=|E(G)|-|V(G)|+1
\]

is the cycle rank and an embedding has \(f\) faces, then Euler's formula gives

\[
f=\beta(G)+1-2g. \tag{1}
\]

In particular,

\[
g\le \left\lfloor \frac{\beta(G)}2\right\rfloor. \tag{2}
\]

I do not prove or disprove the conjecture. The results below isolate several classes where it holds, provide an exact character formula for a larger class, and give a sufficient condition under which bridge amalgamation would produce a counterexample.

---

## 2. Elementary reductions

### Proposition 2.1: Cycle rank at most three

Every connected graph with \(\beta(G)\le 3\) has a unimodal genus distribution.

#### Proof

By (2), only genera \(0\) and \(1\) can occur. Any finite nonnegative sequence supported on at most two consecutive positions is unimodal. ∎

Thus any counterexample must have cycle rank at least four. For \(\beta=4\) or \(5\), a counterexample would necessarily have the form

\[
a_0>a_1<a_2,
\]

so in particular it would have to admit both a planar and a genus-two embedding.

### Lemma 2.2: Leaves and subdivisions

1. Deleting a leaf changes the genus polynomial only by a positive scalar.
2. Suppressing a degree-two vertex preserves the genus polynomial exactly.

#### Proof

Suppose \(x\) is a leaf adjacent to \(y\), and let \(H=G-x\). If \(d=\deg_H(y)\ge1\), each rotation at \(y\) has exactly \(d\) positions in which the new dart \(yx\) can be inserted. The bridge \(xy\) does not change genus. Hence

\[
\Gamma_G(t)=d\,\Gamma_H(t).
\]

The degree-zero exceptional case has one extension and is harmless.

At a degree-two vertex there is a unique cyclic ordering. Replacing a subdivided edge by a single edge gives a bijection of rotation systems, preserves the number of faces, and changes \(v\) and \(e\) by the same amount. Hence genus is preserved. ∎

Consequently, all statements below extend to arbitrary subdivisions and tree attachments, up to multiplication of all coefficients by the same positive integer.

---

## 3. Bridge multiplication and a counterexample criterion

Let \(G\) and \(H\) be disjoint connected graphs, choose \(u\in V(G)\), \(v\in V(H)\), and add the bridge \(uv\). Denote the resulting graph by \(G\mathbin{\#}H\).

### Lemma 3.1: Bridge product formula

There is a positive integer \(c=c(G,u,H,v)\) such that

\[
\Gamma_{G\mathbin{\#}H}(t)=c\,\Gamma_G(t)\Gamma_H(t). \tag{3}
\]

If \(\deg_G(u),\deg_H(v)>0\), then \(c=\deg_G(u)\deg_H(v)\).

#### Proof

Given rotation systems of \(G\) and \(H\), insert the two darts of the new bridge into the cyclic orders at \(u\) and \(v\). There are \(\deg_G(u)\deg_H(v)\) choices.

The bridge splices one facial cycle of the first embedding to one facial cycle of the second, so

\[
f(G\mathbin{\#}H)=f(G)+f(H)-1.
\]

Using Euler's formula,

\[
g(G\mathbin{\#}H)=g(G)+g(H).
\]

Summing over all pairs of embeddings proves (3). ∎

This is relevant because convolution does **not** preserve unimodality for arbitrary unimodal sequences.

### Proposition 3.2: Bridge-power obstruction

Let \(H\) have maximum embedding genus \(h\ge2\), and put

\[
A=a_{h-2}(H),\qquad B=a_{h-1}(H),\qquad C=a_h(H).
\]

If there is an integer \(m\ge2\) such that

\[
C>mB \tag{4}
\]

and

\[
\frac AB+\frac{(m-1)B}{2C}>1, \tag{5}
\]

then a graph formed from \(m\) copies of \(H\) by joining them in a tree with bridges has a nonunimodal genus distribution.

#### Proof

By Lemma 3.1 its genus polynomial is a positive scalar multiple of \(\Gamma_H(t)^m\). Let \(b_j=[t^j]\Gamma_H(t)^m\). The top three coefficients are

\[
\begin{aligned}
b_{mh}&=C^m,\\
b_{mh-1}&=mBC^{m-1},\\
b_{mh-2}&=mAC^{m-1}+\binom m2 B^2C^{m-2}.
\end{aligned}
\]

Condition (4) gives

\[
b_{mh}>b_{mh-1},
\]

while (5) is exactly

\[
\frac{b_{mh-2}}{b_{mh-1}}
 =\frac AB+\frac{(m-1)B}{2C}>1.
\]

Thus

\[
b_{mh-2}>b_{mh-1}<b_{mh},
\]

a strict internal valley. ∎

For example, the abstract unimodal sequence

\[
(9,10,21)
\]

satisfies the criterion with \(m=2\), and

\[
(9+10t+21t^2)^2
 =81+180t+478t^2+420t^3+441t^4
\]

is nonunimodal. This is not claimed to be a graph genus polynomial, but it shows exactly what numerical pattern one should seek near the top of one of Mohar's examples.

There is a symmetric bottom-coefficient criterion: if

\[
a_0>m a_1,\qquad
\frac{a_2}{a_1}+\frac{(m-1)a_1}{2a_0}>1,
\]

then the coefficient at degree \(1\) of \(\Gamma_H(t)^m\) is a strict valley.

---

## 4. An exact formula for generalized dipole stars

Let

\[
S(d_1,\ldots,d_s)
\]

be the multigraph with a central vertex \(u\), peripheral vertices \(v_1,\ldots,v_s\), and \(d_i\) parallel edges between \(u\) and \(v_i\). Put

\[
N=\sum_{i=1}^s d_i,\qquad
\beta=N-s=\sum_i(d_i-1).
\]

Subdividing every parallel edge once gives a simple graph with the same genus polynomial.

For a rotation system, the central rotation is an \(N\)-cycle \(\sigma\). The peripheral rotations combine to a permutation \(\pi\) of cycle type

\[
(d_1,\ldots,d_s).
\]

The square of the face permutation, restricted to the central darts, is \(\sigma\pi\). Therefore the number of faces is

\[
c(\sigma\pi),
\]

where \(c(\rho)\) denotes the number of cycles of a permutation \(\rho\).

Define coefficients \(w_r\) by

\[
\sum_{r=0}^{N-1}w_r z^r
 =\frac{\prod_{i=1}^s(1-z^{d_i})}{1-z}. \tag{6}
\]

### Theorem 4.1: Exact face enumerator

The face enumerator of \(S(d_1,\ldots,d_s)\) is

\[
\boxed{
\sum_{\mathcal E}x^{f(\mathcal E)}
=
\left(\prod_{i=1}^s(d_i-1)!\right)
(N-1)!
\sum_{r=0}^{N-1}
w_r\binom{x+N-r-1}{N}.
} \tag{7}
\]

The genus coefficients are obtained by extracting the terms

\[
x^{\beta+1-2g}.
\]

#### Proof

Fix one peripheral permutation \(\pi\) of cycle type \((d_1,\ldots,d_s)\), and let \(C_N\) denote the conjugacy class of \(N\)-cycles. For positive integers \(x\), the class function

\[
\rho\longmapsto x^{c(\rho)}
\]

is the character of the action of \(S_N\) on \(x\)-colourings of \([N]\). Schur-Weyl duality gives the polynomial identity

\[
x^{c(\rho)}
 =\sum_{\lambda\vdash N}s_\lambda(1^x)\chi^\lambda(\rho).
\]

Averaging over \(\sigma\in C_N\),

\[
\sum_{\sigma\in C_N}x^{c(\sigma\pi)}
=(N-1)!\sum_{\lambda\vdash N}
s_\lambda(1^x)
\frac{\chi^\lambda((N))\chi^\lambda(\pi)}{f^\lambda}.
\]

The character of an \(N\)-cycle vanishes unless \(\lambda\) is a hook

\[
\lambda_r=(N-r,1^r),\qquad 0\le r\le N-1.
\]

For these hooks,

\[
\chi^{\lambda_r}((N))=(-1)^r,\qquad
f^{\lambda_r}=\binom{N-1}{r},
\]

and the hook-content formula gives

\[
\frac{s_{\lambda_r}(1^x)}{f^{\lambda_r}}
 =\binom{x+N-r-1}{N}. \tag{8}
\]

Moreover, since hook representations are exterior powers of the standard representation,

\[
\sum_{r=0}^{N-1}\chi^{\lambda_r}(\pi)t^r
 =\frac{\prod_i(1-(-t)^{d_i})}{1+t}.
\]

After substituting \(t=-z\), the coefficient of \(z^r\) is

\[
(-1)^r\chi^{\lambda_r}(\pi)=w_r.
\]

This proves (7) for a fixed peripheral rotation. There are exactly

\[
\prod_i(d_i-1)!
\]

peripheral rotation systems, and every resulting \(\pi\) has the same cycle type. ∎

Formula (7) is a finite exact reduction of the unimodality question for this class to an explicit coefficient problem. Its alternating coefficients \(w_r\) are the obstacle to a general total-positivity argument.

---

## 5. Dipoles are log-concave

Let \(D_n=S(n)\), the graph with two vertices and \(n\) parallel edges.

Here

\[
\frac{1-z^n}{1-z}=1+z+\cdots+z^{n-1}.
\]

Thus, for one fixed rotation at one vertex,

\[
\begin{aligned}
\sum_{\tau\text{ an }n\text{-cycle}}x^{c(\rho\tau)}
&=(n-1)!\sum_{r=0}^{n-1}\binom{x+n-r-1}{n}\\
&=(n-1)!\left(\binom{x+n}{n+1}-\binom{x}{n+1}\right)\\
&=\frac{x(x+1)\cdots(x+n)-x(x-1)\cdots(x-n)}
        {n(n+1)}.
\end{aligned} \tag{9}
\]

Let \(\left[{m\atop k}\right]\) denote an unsigned Stirling number of the first kind. Extracting the terms of the correct parity gives

\[
\boxed{
a_g(D_n)
=(n-1)!\frac{2}{n(n+1)}
\left[{n+1\atop n-2g}\right].
} \tag{10}
\]

The polynomial

\[
x(x+1)\cdots(x+n)
\]

has only real nonpositive roots, so its coefficient sequence

\[
\left(\left[{n+1\atop k}\right]\right)_k
\]

is log-concave by Newton's inequalities. A positive log-concave sequence has nonincreasing consecutive ratios, and hence each fixed-step subsequence is also log-concave. Therefore

\[
\left(\left[{n+1\atop n-2g}\right]\right)_g
\]

is log-concave.

### Corollary 5.1

The genus distribution of every dipole, and of every subdivision or tree extension of a dipole, is log-concave and hence unimodal.

---

## 6. Bouquets are log-concave

Let \(B_n\) be the bouquet of \(n\) loops. Its rotations are the \((2n)\)-cycles on a fixed paired dart set.

Fix a long cycle \(\sigma_0\) on \(2n\) darts, and let \(\varepsilon_g(n)\) be the number of fixed-point-free involutions \(\alpha\) such that

\[
c(\sigma_0\alpha)=n+1-2g.
\]

Simultaneous conjugation acts transitively on both long cycles and perfect matchings. Double-counting pairs \((\sigma,\alpha)\) gives

\[
a_g(B_n)=2^{n-1}(n-1)!\,\varepsilon_g(n). \tag{11}
\]

Let

\[
P_n(t)=\sum_g\varepsilon_g(n)t^g.
\]

Specializing Theorem 4.1 to \(S(2,\ldots,2)\), which suppresses to \(B_n\), gives the generating identity

\[
1+2\sum_{n\ge0}
\frac{E_n(x)}{(2n-1)!!}z^{n+1}
=\left(\frac{1+z}{1-z}\right)^x, \tag{12}
\]

where

\[
E_n(x)=\sum_g\varepsilon_g(n)x^{n+1-2g}.
\]

Since the right side satisfies

\[
(1-z^2)\frac{\partial}{\partial z}
\left(\frac{1+z}{1-z}\right)^x
=
2x\left(\frac{1+z}{1-z}\right)^x,
\]

coefficient comparison yields

\[
(n+1)P_n(t)
=
2(2n-1)P_{n-1}(t)
+
(2n-1)(n-1)(2n-3)tP_{n-2}(t). \tag{13}
\]

Normalize by positive constants so that \(Q_0=Q_1=1\) and

\[
Q_n(t)=Q_{n-1}(t)+\frac{n(n-1)}4\,tQ_{n-2}(t). \tag{14}
\]

Equation (14) is the matching recurrence for a path whose edge joining \(i-1\) to \(i\) has weight \(i(i-1)/4\). If \(A_n\) is the corresponding real symmetric weighted adjacency matrix, then

\[
\det(xI-A_n)=x^nQ_n(-x^{-2}).
\]

Because \(A_n\) is real symmetric, all its eigenvalues are real; because the path is bipartite, the nonzero eigenvalues occur in pairs \(\pm\lambda_j\). Hence

\[
Q_n(t)=\prod_j(1+\lambda_j^2t),
\]

so all zeros of \(Q_n\), and therefore of \(P_n\), are real and negative. Newton's inequalities now give log-concavity.

### Corollary 6.1

The genus distribution of every bouquet, and of every subdivision or tree extension of a bouquet, is log-concave.

---

## 7. Generalized stars of cycle rank at most six

Assume \(d_i\ge2\); entries \(d_i=1\) are removable leaf edges. Let

\[
F_{\mathbf d}(x)
=(N-1)!\sum_r w_r\binom{x+N-r-1}{N},
\]

so that the actual face enumerator is

\[
\left(\prod_i(d_i-1)!\right)F_{\mathbf d}(x).
\]

Write

\[
F_{\mathbf d}(x)
=\sum_g A_gx^{\beta+1-2g}.
\]

The scalar \(\prod_i(d_i-1)!\) does not affect shape.

For reference, if \(p\) is the number of \(d_i\)'s equal to \(2\), and \(q\) the number equal to \(3\), then (6) gives

\[
w_0=w_1=1,\qquad
w_2=1-p,\qquad
w_3=1-p-q.
\]

Consequently,

\[
\begin{aligned}
F_{\mathbf d}(1)&=(N-1)!,\\
F_{\mathbf d}(2)&=(N-1)!(N+2),\\
F_{\mathbf d}(3)&=(N-1)!
\left(\frac{(N+1)(N+4)}2+1-p\right),\\
F_{\mathbf d}(4)&=(N-1)!
\left(
\frac{(N+2)(N+3)(N+4)}6-p(N+2)-q
\right).
\end{aligned} \tag{15}
\]

For \(\beta\le6\), these evaluations determine all allowed parity coefficients. The resulting exact tables are as follows.

### Cycle rank \(4\)

\[
\begin{array}{c|c}
(d_i)&(A_0,A_1,A_2)\\ \hline
(5)&(1,15,8)\\
(4,2)&(8,80,32)\\
(3,3)&(9,75,36)\\
(3,2,2)&(72,480,168)\\
(2,2,2,2)&(672,3360,1008)
\end{array}
\]

### Cycle rank \(5\)

\[
\begin{array}{c|c}
(d_i)&(A_0,A_1,A_2)\\ \hline
(6)&(1,35,84)\\
(5,2)&(10,250,460)\\
(4,3)&(12,240,468)\\
(4,2,2)&(112,1960,2968)\\
(3,3,2)&(126,1890,3024)\\
(3,2,2,2)&(1344,16800,22176)\\
(2,2,2,2,2)&(16128,161280,185472)
\end{array}
\]

### Cycle rank \(6\)

\[
\begin{array}{c|c}
(d_i)&(A_0,A_1,A_2,A_3)\\ \hline
(7)&(1,70,469,180)\\
(6,2)&(12,630,3318,1080)\\
(5,3)&(15,630,3255,1140)\\
(4,4)&(16,616,3304,1104)\\
(5,2,2)&(160,6160,26320,7680)\\
(4,3,2)&(192,6048,26208,7872)\\
(3,3,3)&(216,6048,25704,8352)\\
(4,2,2,2)&(2304,64512,233856,62208)\\
(3,3,2,2)&(2592,63504,232848,63936)\\
(3,2,2,2,2)&(34560,725760,2298240,570240)\\
(2,2,2,2,2,2)&(506880,8870400,24837120,5702400)
\end{array}
\]

Every row is log-concave by direct cross multiplication.

### Theorem 7.1

Every generalized dipole star \(S(d_1,\ldots,d_s)\) of cycle rank at most six has a log-concave genus distribution.

This does not settle arbitrary graphs of cycle rank \(4,5,\) or \(6\); it only settles this structured family.

---

## 8. Bridge-closed infinite classes

A nonnegative sequence with no internal zeros is log-concave precisely when its Toeplitz matrix is totally positive of order two. Products of such Toeplitz matrices remain totally positive of order two by the Cauchy-Binet formula. Equivalently:

> Convolution preserves log-concavity for nonnegative log-concave sequences without internal zeros.

Combining this with Lemma 3.1 gives:

### Corollary 8.1

The genus distribution is log-concave for every graph formed, using bridges, subdivisions, and tree attachments, from pieces each of which is one of:

1. an arbitrary bouquet;
2. an arbitrary dipole;
3. a generalized dipole star of cycle rank at most six.

This is an infinite class of graphs with unbounded total cycle rank.

---

## 9. Fixed-parameter exact computation

There is also a straightforward fixed-parameter algorithm in the cycle rank.

### Proposition 9.1

The full orientable genus polynomial can be computed in fixed-parameter time parameterized by

\[
\beta=|E|-|V|+1.
\]

More precisely, after linear-time preprocessing, at most

\[
(6\beta-6)!
\]

rotation systems need be examined.

#### Proof

Repeatedly delete leaves, retaining the scalar factors from Lemma 2.2, and suppress degree-two vertices. Unless the remaining graph is a cycle, the resulting kernel \(K\) has minimum degree at least three.

Writing \(n=|V(K)|\), \(m=|E(K)|\), we have

\[
m=n+\beta-1
\]

and

\[
2m\ge3n.
\]

Therefore

\[
n\le2\beta-2,\qquad m\le3\beta-3. \tag{16}
\]

The number of rotation systems is

\[
\prod_{v\in V(K)}(\deg(v)-1)!
 \le (2m)!
 \le (6\beta-6)!.
\]

For each rotation system, construct \(\sigma\alpha\), count its cycles \(f\), and use

\[
g=\frac{2-|V(K)|+|E(K)|-f}{2}.
\]

Thus the exact polynomial, and hence unimodality, can be decided in

\[
O\!\left(|G|+\beta(6\beta-6)!\right)
\]

arithmetic operations, apart from standard big-integer costs. ∎

This makes exhaustive verification at any fixed cycle rank finite, but I have not performed or claimed an exhaustive verification over all kernels of rank \(4\) or higher.

---

## 10. What remains open

The main conjecture is not resolved here. The precise gaps are:

1. Formula (7) does not by itself imply unimodality for arbitrary tuples \((d_1,\ldots,d_s)\); the coefficients \(w_r\) have alternating signs.
2. The tables cover only generalized dipole stars of cycle rank at most six, not all graphs of those ranks.
3. Proposition 3.2 would turn a suitable top-coefficient pattern into an explicit counterexample, but no graph satisfying its inequalities has been found here.
4. The abstract sequence \((9,10,21)\) is only a numerical witness that bridge products can destroy unimodality; it is not asserted to be realizable as a genus distribution.
5. I have not verified the explicit coefficient lists of Mohar's counterexamples against Proposition 3.2 because those lists were not included in the supplied material.

Thus the most concrete next steps are:

- check the top and bottom three coefficients of Mohar's examples against Proposition 3.2;
- exhaustively enumerate reduced kernels beginning at cycle rank \(4\) using Proposition 9.1;
- search formula (7) over integer partitions of larger cycle rank for a nonunimodal generalized-star example.