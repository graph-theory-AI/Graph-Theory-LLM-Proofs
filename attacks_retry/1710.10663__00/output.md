```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured constant for L=4 in the fractional-radius formulation, and for discrete-centre codes with blocklength n at least |C|²; higher even L remain unresolved.",
  "would_publish": false,
  "caveats": "Uses the corrected source coefficient. No literature-novelty claim; unrestricted finite-blocklength discrete-centre effects are not covered."
}
```

## 1. The intended constant and the scope of the result

I discard the previous attempt’s claimed disproof. The source coefficient quoted in the supplied source-check is
\[
c_L=2^{-L}\left\lfloor\frac L2\right\rfloor
       \binom{L-1}{\lfloor L/2\rfloor}.
\]
For \(L=2m\), this is
\[
c_{2m}=\frac{m}{2^{2m+1}}\binom{2m}{m}.
\]
In particular,
\[
\tau_4=\frac5{16},\qquad c_4=\frac38.
\]

The main result below is a sharp four-word theorem. I state the radius convention explicitly, rather than silently identifying fractional radii with finite-blocklength integer radii.

For \(x\in\{0,1\}^n\) and \(y\in[0,1]^n\), let
\[
d(x,y)=\frac1n\sum_{j=1}^n |x_j-y_j|.
\]
For a finite set \(S\) of binary words, define its **fractional radius**
\[
r(S)=\min_{y\in[0,1]^n}\max_{x\in S}d(x,y).
\]
For a code \(C\), put
\[
r_4(C)=\min_{\substack{S\subseteq C\\ |S|=4}}r(S),
\qquad
R_4(M)=\sup_{\substack{n,\ C\subseteq\{0,1\}^n\\ |C|=M}}r_4(C).
\]

This is also the limiting-blocklength radius obtained using binary centres. The rounding bound, and a precise discrete-centre consequence, appear in §8.

## 2. Main theorem

**Theorem.** There is an absolute integer \(M_0\) such that, for every \(M\ge M_0\),
\[
R_4(M)=B_4(M),
\]
where
\[
B_4(M)=
\begin{cases}
\displaystyle
\frac5{16}+\frac{3}{8(M-1)}
+\frac{3}{16(M-1)(M-3)},&M\text{ even},\\[8pt]
\displaystyle
\frac5{16}+\frac{3}{8M}
+\frac{3}{16M(M-2)},&M\text{ odd}.
\end{cases}
\tag{1}
\]

One possible, very unoptimized, choice is
\[
M_0=100000\binom{133}{4}.
\tag{2}
\]

Consequently, defining \(\mathrm{maxcode}^{\mathrm{frac}}_4(\varepsilon)\) using fractional radius and the condition
\[
r_4(C)>\frac5{16}+\varepsilon,
\]
we have
\[
\boxed{\displaystyle
\mathrm{maxcode}^{\mathrm{frac}}_4(\varepsilon)
=\frac{3}{8\varepsilon}+O(1).}
\tag{3}
\]

The proof is elementary but uses a feature specific to four words: their fractional radius has only two kinds of obstruction.

## 3. An exact formula for the radius of four binary words

For four words indexed by \(S\), define the average radius
\[
A(S)=\min_y\frac14\sum_{i\in S}d(x_i,y).
\]
The centre in this definition may be binary or fractional; coordinatewise majority attains the minimum.

### Lemma 1
For every four-word set \(S\),
\[
r(S)=\max\left\{A(S),\ \frac12\max_{i,j\in S}d(x_i,x_j)\right\}.
\tag{4}
\]

**Proof.**
Linear-programming duality gives
\[
r(S)=\max_{\lambda\in\Delta_4}
\frac1n\sum_{j=1}^n
\min\left\{
\sum_{i:x_{ij}=0}\lambda_i,\
\sum_{i:x_{ij}=1}\lambda_i
\right\},
\tag{5}
\]
where \(\Delta_4=\{\lambda_i\ge0:\sum_i\lambda_i=1\}\).

The objective is affine on every cell cut out by the hyperplanes
\[
\sum_{i\in T}\lambda_i=\frac12.
\]
Its maximum is therefore attained at a vertex of this subdivision.

Those vertices are precisely:

* the unit vectors;
* the vectors having two entries \(1/2\) and two entries \(0\);
* \((1/4,1/4,1/4,1/4)\).

Here is a complete check. On a face with support at most three, the cutting hyperplanes reduce to \(\lambda_i=1/2\), producing only unit vectors and half-pairs. A full-support vertex cannot have \(\lambda_i=1/2\), since then no other independent cutting hyperplane passes through it. Otherwise the only possible cutting hyperplanes are the three complementary pair-sum hyperplanes. Their common intersection is the uniform vector.

The objective values at these vertices are respectively \(0\), \(d(x_i,x_j)/2\), and \(A(S)\). This proves (4). ∎

For subsequent calculations, choose a coordinate uniformly at random and write the corresponding codeword signs as
\[
U_i\in\{-1,1\},\qquad q_{ij}=\mathbb E[U_iU_j]=1-2d(x_i,x_j).
\]
The identity
\[
|u_1+u_2+u_3+u_4|
=\frac32+\frac12\sum_{i<j}u_iu_j-\frac12u_1u_2u_3u_4
\]
gives
\[
A(\{i,j,k,\ell\})
=\frac5{16}
+\frac1{16}\left(
\mathbb E[U_iU_jU_kU_\ell]
-\sum_{\{a,b\}\subseteq\{i,j,k,\ell\}}q_{ab}
\right).
\tag{6}
\]

The same algebraic identity is valid when some indices repeat.

## 4. Two average-radius bounds

Write
\[
\tau=\frac5{16},
\qquad
\overline A=\binom M4^{-1}\sum_{|S|=4}A(S),
\]
and define the coordinate imbalance
\[
\Theta=\frac1M\sum_{i=1}^M U_i,\qquad v=\mathbb E\Theta^2.
\]

### A coarse bound detecting imbalance

Sample four codeword indices independently, with replacement. By (6), their expected average radius is
\[
\tau-\frac38v+\frac1{16}\mathbb E\Theta^4
\le \tau-\frac5{16}v,
\]
because \(\Theta^4\le\Theta^2\).

The probability of a repeated index is at most \(6/M\). Since an average radius lies in \([0,1/2]\), conditioning on distinct indices changes its expectation by at most \(3/M\). Hence
\[
\boxed{\displaystyle
\overline A\le \tau-\frac5{16}v+\frac3M.}
\tag{7}
\]

### The exact average-radius bound

For one coordinate, put
\[
s=\sum_{i=1}^M U_i.
\]
Its contribution to \(\overline A\), obtained by averaging (6) over four distinct indices, is
\[
F_M(s)=\tau+
\frac{s^4-(6M^2-24M+28)s^2+
3M(M-2)(2M-5)}
{16M(M-1)(M-2)(M-3)}.
\tag{8}
\]

For completeness, the identities used here are
\[
\sum_{i<j}U_iU_j=\frac{s^2-M}{2}
\]
and
\[
\sum_{i<j<k<\ell}U_iU_jU_kU_\ell
=\frac{s^4-(6M-8)s^2+3M(M-2)}{24}.
\]

For \(M\ge5\), the numerator in (8) is strictly decreasing as a function of \(s^2\) throughout \(0\le s^2\le M^2\). Indeed, its derivative with respect to \(s^2\) is at most
\[
2M^2-(6M^2-24M+28)
=-4(M^2-6M+7)<0.
\]
Thus a coordinate contributes most when its number of \(1\)'s is as close as possible to \(M/2\). Substitution of \(s=0\) or \(s^2=1\) gives (1), proving
\[
\boxed{\overline A\le B_4(M).}
\tag{9}
\]

The remaining issue is that \(r(S)\) can exceed \(A(S)\). We now control those exceptions sharply enough not to lose the leading constant.

## 5. Far pairs have bounded degree

Assume henceforth that
\[
r=r_4(C)>\tau.
\]
Define a graph \(G\) on the codewords by
\[
ij\in E(G)\quad\Longleftrightarrow\quad d(x_i,x_j)>\frac58.
\tag{10}
\]

If a four-set is independent in \(G\), all its pairwise half-distances are at most \(\tau\). Lemma 1 therefore implies
\[
A(S)\ge r>\tau
\quad\text{for every independent four-set }S.
\tag{11}
\]

### Lemma 2
The graph \(G\) has maximum degree at most
\[
D=\binom{133}{4}-1.
\tag{12}
\]

**Proof.**
First, \(G\) is \(K_5\)-free. For any five binary words, the sum of their ten normalized pairwise distances is at most \(6\): each coordinate contributes at most \(2\cdot3=6\). Ten distances all exceeding \(5/8\) would instead have sum exceeding \(25/4>6\).

We also need a bound for words lying in a biased Hamming cap. For four independent Bernoulli-\(p\) bits, the expected average radius is
\[
\Phi(p)=\frac5{16}
-\frac38(2p-1)^2+\frac1{16}(2p-1)^4.
\tag{13}
\]
This function is concave on \([0,1]\), since
\[
\Phi''(p)=-3+3(2p-1)^2\le0,
\]
and is decreasing on \([1/2,1]\).

Suppose \(T\) consists of \(K\) words, each of weight at least \(5/8\). Let \(p_j\) be the proportion of \(1\)'s in coordinate \(j\). Sampling four words with replacement, Jensen’s inequality gives expected average radius at most
\[
\frac1n\sum_j\Phi(p_j)
\le \Phi\left(\frac1n\sum_jp_j\right)
\le \Phi(5/8).
\]
Passing to sampling without replacement costs at most \(3/K\). Consequently,
\[
\binom K4^{-1}\sum_{\substack{S\subseteq T\\|S|=4}}A(S)
\le \Phi(5/8)+\frac3K.
\tag{14}
\]
Now
\[
\Phi(5/8)=\frac{1185}{4096},
\qquad
\frac{1185}{4096}+\frac3{130}<\frac5{16}.
\tag{15}
\]

Fix a vertex \(x\) of \(G\). After translating by \(x\), every word in its neighbourhood has weight greater than \(5/8\). The elementary Ramsey bound
\[
R(5,130)\le\binom{133}{4}
\]
shows that a neighbourhood of that size contains an independent set of \(130\) vertices, since \(G\) has no \(K_5\). Equation (11) says every four-set in this independent set has average radius greater than \(\tau\), contradicting (14)–(15). ∎

Only the elementary Ramsey recurrence is used here; the size of \(D\) is irrelevant to the asymptotic coefficient.

## 6. Exceptional four-sets do not increase the optimum

Let
\[
\mathcal B=\{S:|S|=4,\ E(G[S])\ne\varnothing\}
\]
be the exceptional four-sets, and put
\[
m=|E(G)|,\qquad
\eta=\frac{|\mathcal B|}{\binom M4}.
\]
Lemma 2 gives
\[
m\le\frac{DM}{2},
\qquad
\eta\le
\frac{m\binom{M-2}{2}}{\binom M4}
\le\frac{6D}{M-1}.
\tag{16}
\]

### 6.1 Global imbalance is small

Write \(a=r-\tau>0\). Nonexceptional four-sets have \(A(S)\ge r\), whereas all average radii are nonnegative. Also \(r\le1/2\), using the centre \((1/2,\ldots,1/2)\). Thus
\[
\overline A\ge(1-\eta)r\ge\tau+a-\frac{\eta}{2}.
\]
Combining this with (7) and (16), for \(M\ge2\),
\[
a+\frac5{16}v
\le\frac3M+\frac{3D}{M-1}
\le\frac{6(D+1)}M.
\tag{17}
\]

In particular, for the choice (2),
\[
M\ge M_0
\quad\Longrightarrow\quad
a<\frac1{256},
\qquad
v<\frac1{4096}.
\tag{18}
\]

### 6.2 A four-set containing a specified far pair has high average radius on average

Fix an edge \(ij\in E(G)\), so that
\[
q_{ij}<-\frac14.
\]
Let \(\overline A_{ij}\) be the average of \(A(\{i,j,k,\ell\})\) over distinct \(k,\ell\notin\{i,j\}\).

First sample \(k,\ell\) independently from all \(M\) indices. Applying (6),
\[
16\bigl(\mathbb EA(\{i,j,k,\ell\})-\tau\bigr)
=
-q_{ij}
+\mathbb E[(U_iU_j-1)\Theta^2]
-2\mathbb E[(U_i+U_j)\Theta].
\]
Therefore, by Cauchy–Schwarz,
\[
16\bigl(\mathbb EA-\tau\bigr)
\ge \frac14-2v-4\sqrt v.
\tag{19}
\]

The probability that \(k,\ell\) fail to be distinct and outside \(\{i,j\}\) is at most \(5/M\). Conditioning therefore changes the average radius by at most \(5/(2M)\). Hence
\[
16(\overline A_{ij}-\tau)
\ge \frac14-2v-4\sqrt v-\frac{40}{M}.
\tag{20}
\]
For \(M\ge M_0\), the right side exceeds \(1/8\). Thus, uniformly over all edges,
\[
\boxed{\overline A_{ij}\ge\tau+\delta,\qquad
\delta=\frac1{128}.}
\tag{21}
\]

### 6.3 Removing multiple counting costs only a lower-order term

For \(S\in\mathcal B\), let \(k(S)=|E(G[S])|\). Summing (21) over edges gives
\[
\sum_{S\in\mathcal B}k(S)(A(S)-\tau)
\ge
\delta\,m\binom{M-2}{2}.
\tag{22}
\]

Set
\[
T=\sum_{S\in\mathcal B}(k(S)-1).
\]
Since \(k-1\le\binom k2\), \(T\) is at most the number of pairs of edges contained in a common four-set, counted with their possible completions.

There are at most \((D-1)m\) adjacent pairs of edges, each with \(M-3\) completions. There are at most \(m^2/2\) disjoint pairs. Consequently,
\[
T\le (D-1)m(M-3)+\frac{m^2}{2}
\le\frac54DmM.
\tag{23}
\]

Because \(A(S)-\tau\le3/16\), equations (22)–(23) imply
\[
\sum_{S\in\mathcal B}(A(S)-\tau)
\ge
\delta\,m\binom{M-2}{2}-\frac{15}{64}DmM.
\tag{24}
\]
For \(M\ge M_0\), the second term is at most half the first. Indeed,
\(\binom{M-2}{2}\ge M^2/4\) for \(M\ge9\), and \(M\ge240D\) suffices.

If \(m>0\), we obtain
\[
\frac1{|\mathcal B|}\sum_{S\in\mathcal B}A(S)
\ge\tau+\frac{\delta}{2}
=\tau+\frac1{256}.
\tag{25}
\]
By (18), this is greater than \(r\).

Every nonexceptional four-set has \(A(S)\ge r\). Thus (25), also allowing the case \(m=0\), proves
\[
r\le\overline A.
\tag{26}
\]
Finally, (9) yields
\[
r_4(C)\le B_4(M).
\]

If \(r_4(C)\le\tau\), this upper bound is immediate. Therefore every code of size \(M\ge M_0\) is covered.

## 7. Attainment and inversion

Let \(w=\lfloor M/2\rfloor\). Construct a code with one coordinate for each \(w\)-subset \(T\subseteq[M]\), and put
\[
x_i(T)=\mathbf1_{\{i\in T\}}.
\tag{27}
\]
Every column is maximally balanced.

For any fixed four codewords, the coordinate distribution is invariant under all permutations of those four words. The dual objective in (5) is concave and permutation-invariant in \(\lambda\). Averaging \(\lambda\) over permutations shows that its maximum occurs at the uniform vector. Thus the radius of every four-set equals its average radius.

All four-sets also have the same average radius. Since every column attains the maximum in (8), this common value is \(B_4(M)\). This proves attainment and completes the theorem.

For \(M\ge5\), formula (1) gives the useful bounds
\[
\frac{3}{8M}
<
B_4(M)-\tau
\le
\frac{3}{8(M-2)}.
\tag{28}
\]
Therefore, for sufficiently small \(\varepsilon>0\),
\[
\left\lfloor\frac{3}{8\varepsilon}\right\rfloor
\le
\mathrm{maxcode}^{\mathrm{frac}}_4(\varepsilon)
<
\frac{3}{8\varepsilon}+2.
\tag{29}
\]
In particular, the additive-\(O(1)\) assertion, not merely its leading-order version, follows for \(L=4\) in this formulation.

## 8. Binary centres and the remaining gap

### A rigorous discrete-centre consequence

Let \(r_{\mathrm{disc}}(S)\) use centres in \(\{0,1\}^n\). For four words,
\[
r(S)\le r_{\mathrm{disc}}(S)
\le r(S)+\frac{3}{2n}.
\tag{30}
\]
To see the upper bound, take an optimal basic solution of the fractional-radius linear program. It has at most three nonintegral centre coordinates: with \(f\) such coordinates and the radius variable, the \(f+1\) free variables must be determined by at most four distance constraints. Rounding these coordinates to nearest bits increases every normalized distance by at most \(3/(2n)\).

Consequently, the theorem proves, for every \(M\ge M_0\),
\[
\min_{|S|=4}r_{\mathrm{disc}}(S)
\le B_4(M)+\frac{3}{2n}.
\tag{31}
\]

In particular, consider the restricted maximum over discrete-centre codes satisfying
\[
n\ge |C|^2.
\]
For such codes, (28) and (31) imply, when \(M>6\),
\[
\varepsilon
<
\frac{3}{8(M-2)}+\frac{3}{2M^2}
\le\frac{3}{8(M-6)}.
\]
The balanced construction supplies the matching lower bound; coordinates may be repeated to satisfy the blocklength restriction. Hence this restricted discrete-centre maximum also satisfies
\[
\boxed{\displaystyle
\mathrm{maxcode}_{4,\ n\ge |C|^2}^{\mathrm{disc}}(\varepsilon)
=\frac{3}{8\varepsilon}+O(1).}
\tag{32}
\]

I do **not** use (30) to assert the same conclusion for arbitrary finite blocklength: its error is not uniformly \(O(M^{-2})\).

### What is unresolved

The argument does not prove the conjecture for even \(L\ge6\).

Its decisive step is the four-point identity (4). Already for six words, the dual subdivision has nonuniform full-support vertices, for example
\[
\left(\frac14,\frac14,
      \frac18,\frac18,\frac18,\frac18\right).
\]
Thus exceptional lists cannot be described solely by containing a far pair, and the bounded-degree graph argument above does not control all possible radius witnesses.

Accordingly:

* the corrected coefficient is supported, not refuted;
* a sharp \(L=4\) fractional-radius theorem is proved above;
* a long-blocklength discrete-centre special case follows;
* the full even-\(L\) conjecture remains unresolved here.

I have not independently checked whether the \(L=4\) theorem is already recorded in the literature, so I make no novelty claim.