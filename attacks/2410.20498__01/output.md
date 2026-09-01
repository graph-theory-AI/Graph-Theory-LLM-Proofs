```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For s = 2^(d-r) and 2^d-2^(d-r) with r = o(d), the deficit 1-lambda(d,s) has an exact exponential rate, although the general problem remains open.",
  "would_publish": false,
  "caveats": "Only a special power-of-two family is covered; multiplicative constants and general s remain open, and novelty against the full literature was not checked."
}
```

## 1. Statement of the partial result

Write \(Q_n=\{0,1\}^n\), and let a random \(d\)-face mean that a \(d\)-element set of varying coordinates and an assignment to the other coordinates are chosen uniformly.

For \(d\ge r\ge2\), define
\[
s_{d,r}=2^{d-r},\qquad
q_r=2^r-1,\qquad
\rho_r=\frac{2^{r-1}-1}{2^r-1}.
\]
Thus \(s_{d,r}/2^d=2^{-r}\).

### Theorem

Let \(r=r(d)\) satisfy \(2\le r=o(d)\). Then, as \(d\to\infty\),
\[
(1-o(1))\,\frac{\rho_r^d}{q_r}
\ \le\
1-\lambda\bigl(d,2^{d-r}\bigr)
\ \le\
(1+o(1))\,q_r\rho_r^d.
\tag{1}
\]
The same bounds hold for \(s=2^d-2^{d-r}\).

Consequently,
\[
\frac{\bigl(1-\lambda(d,2^{d-r})\bigr)^{1/d}}{\rho_r}
\longrightarrow 1.
\tag{2}
\]
In particular, for every fixed \(r\ge2\),
\[
1-\lambda(d,2^{d-r})
=\Theta_r(\rho_r^d).
\tag{3}
\]

Thus the exponential rate of convergence to \(1\) is determined for every fixed reciprocal dyadic density \(2^{-r}\), and more generally for \(r=o(d)\).

For example, when \(r=2\),
\[
\rho_2=\frac13,
\]
and hence
\[
(1-o(1))3^{-(d+1)}
\le 1-\lambda(d,2^{d-2})
\le 3^{1-d}.
\tag{4}
\]
In particular,
\[
\lim_{d\to\infty}
\bigl(1-\lambda(d,2^{d-2})\bigr)^{1/d}
=\frac13.
\]

The proof consists of a linear-code blow-up construction and a Fourier-analytic obstruction.

---

## 2. The lower bound on \(\lambda\): a linear construction

Let \(V=\mathbb F_2^r\setminus\{0\}\), so \(|V|=q_r\). Partition the \(n\) coordinates as equally as possible into classes indexed by \(V\), and assign to coordinate \(i\) the label \(v_i\in V\). Define
\[
\Phi:\mathbb F_2^n\longrightarrow\mathbb F_2^r,
\qquad
\Phi(x)=\sum_{i=1}^n x_i v_i,
\]
and take
\[
A=\ker\Phi.
\]

Consider a \(d\)-face whose varying-coordinate set is \(I\). Let
\[
k=\dim\langle v_i:i\in I\rangle.
\]
After fixing all coordinates outside \(I\), membership in \(A\) is an affine linear system in the \(d\) free variables. It therefore has either no solutions or exactly \(2^{d-k}\) solutions.

Hence the face contains exactly \(2^{d-r}\) points of \(A\) if and only if \(k=r\):

- if \(k=r\), the system is surjective and has exactly \(2^{d-r}\) solutions;
- if \(k<r\), the number of solutions is either \(0\) or \(2^{d-k}>2^{d-r}\).

As \(n\to\infty\), the labels on a uniformly chosen \(d\)-set of coordinates converge in distribution to \(d\) independent uniformly chosen elements of \(V\). Let
\[
F_{d,r}
=
\Pr(v_1,\dots,v_d\text{ do not span }\mathbb F_2^r),
\tag{5}
\]
where the \(v_i\) are independent and uniform on \(V\). The construction gives
\[
\lambda(d,2^{d-r})\ge 1-F_{d,r},
\qquad\text{so}\qquad
1-\lambda(d,2^{d-r})\le F_{d,r}.
\tag{6}
\]

### Estimating \(F_{d,r}\)

There are \(q_r=2^r-1\) hyperplanes in \(\mathbb F_2^r\). Each contains \(2^{r-1}-1\) nonzero vectors, so the probability that all \(d\) samples lie in a specified hyperplane is \(\rho_r^d\).

Two distinct hyperplanes intersect in an \((r-2)\)-dimensional subspace. Put
\[
\sigma_r=\frac{2^{r-2}-1}{2^r-1}.
\]
The union bound and the first Bonferroni inequality give
\[
q_r\rho_r^d-\binom{q_r}{2}\sigma_r^d
\le F_{d,r}\le q_r\rho_r^d.
\tag{7}
\]
Since
\[
\frac{\sigma_r}{\rho_r}
=
\frac{2^{r-2}-1}{2^{r-1}-1}<\frac12,
\]
if \(r=o(d)\), then
\[
\frac{\binom{q_r}{2}\sigma_r^d}{q_r\rho_r^d}
\le 2^{r-1}2^{-d}=o(1).
\]
Thus
\[
F_{d,r}=(1+o(1))q_r\rho_r^d.
\tag{8}
\]
This proves the right-hand inequality in (1).

For \(r=2\), failure to span means that all \(d\) labels are equal. Therefore
\[
F_{d,2}=3\left(\frac13\right)^d=3^{1-d}
\tag{9}
\]
exactly.

---

## 3. A Fourier variance lemma

Let \(f=1_A:\{0,1\}^n\to\{0,1\}\), and let
\[
p=\mathbb E f=\frac{|A|}{2^n}.
\]
For a random \(d\)-face \(C\), put
\[
Z=\frac{|A\cap C|}{2^d}.
\]
Thus \(\mathbb E Z=p\).

### Lemma

If \(p<1/2\), then
\[
\operatorname{Var}(Z)
\ge
p(1-p)
\left(
1-\frac{n}{2(1-p)(n-d+1)}
\right)_+^d.
\tag{10}
\]
Consequently, for fixed \(d\), as \(n\to\infty\),
\[
\operatorname{Var}(Z)
\ge
p(1-p)
\left(\frac{1-2p}{2(1-p)}\right)^d-o_n(1).
\tag{11}
\]

### Proof

Use the Fourier expansion
\[
f(x)=\sum_{S\subseteq[n]}\widehat f(S)\chi_S(x).
\]
Parseval gives
\[
\sum_{S\ne\varnothing}\widehat f(S)^2=p(1-p).
\tag{12}
\]

For coordinate \(i\), let \(\operatorname{Inf}_i(f)\) be its influence. Since each bichromatic \(i\)-edge has exactly one endpoint in \(A\),
\[
\operatorname{Inf}_i(f)\le 2p.
\tag{13}
\]
Moreover,
\[
\sum_{S\ni i}\widehat f(S)^2=\frac14\operatorname{Inf}_i(f).
\]
Therefore
\[
\sum_{S\ne\varnothing}|S|\widehat f(S)^2
=
\frac14\sum_{i=1}^n\operatorname{Inf}_i(f)
\le \frac{np}{2}.
\tag{14}
\]

Choose the varying-coordinate set \(I\) uniformly from \(\binom{[n]}d\). Averaging \(f\) over the coordinates in \(I\) kills exactly the Fourier coefficients whose support meets \(I\). Hence
\[
\operatorname{Var}(Z)
=
\sum_{S\ne\varnothing}\widehat f(S)^2
\frac{\binom{n-|S|}{d}}{\binom nd}.
\tag{15}
\]

For \(0\le k\le n\),
\[
\frac{\binom{n-k}{d}}{\binom nd}
=
\prod_{j=0}^{d-1}\left(1-\frac{k}{n-j}\right)
\ge
\left(1-\frac{k}{n-d+1}\right)_+^d.
\tag{16}
\]
The function
\[
k\longmapsto
\left(1-\frac{k}{n-d+1}\right)_+^d
\]
is convex. Normalize the nonconstant Fourier weights in (12) to a probability distribution and let \(K=|S|\) under this distribution. From (14),
\[
\mathbb E K
\le
\frac{n}{2(1-p)}.
\tag{17}
\]
Jensen's inequality, (15), and (16) now give (10). Taking \(n\to\infty\) gives (11). ∎

---

## 4. Applying the variance lemma

Set
\[
\alpha=2^{-r}.
\]
For a given \(A\subseteq Q_n\), let
\[
\delta_A=\Pr(Z\ne\alpha),
\]
the fraction of bad \(d\)-faces.

Because \(Z=\alpha\) on every good face and \(0\le Z\le1\),
\[
|p-\alpha|
=
\left|\mathbb E\bigl[(Z-\alpha)1_{\{Z\ne\alpha\}}\bigr]\right|
\le (1-\alpha)\delta_A.
\tag{18}
\]
Also,
\[
\operatorname{Var}(Z)+(p-\alpha)^2
=
\mathbb E(Z-\alpha)^2
\le (1-\alpha)^2\delta_A.
\tag{19}
\]
In particular,
\[
\operatorname{Var}(Z)\le(1-\alpha)^2\delta_A.
\tag{20}
\]

Let
\[
\Delta_{d,r}=1-\lambda(d,2^{d-r}).
\]
By the construction,
\[
\Delta_{d,r}\le F_{d,r}.
\tag{21}
\]

For completeness, define
\[
p_-=\alpha-(1-\alpha)F_{d,r},
\qquad
p_+=\alpha+(1-\alpha)F_{d,r}.
\]
Whenever \(p_->0\) and \(p_+<1/2\), applying the variance lemma to maximizing sets in \(Q_n\), and then letting \(n\to\infty\), yields the explicit bound
\[
\Delta_{d,r}
\ge
\frac{p_-(1-p_-)}{(1-\alpha)^2}
\left(
\frac{1-2p_+}{2(1-p_+)}
\right)^d.
\tag{22}
\]
Indeed, (18) and (21) confine the density \(p\) to \([p_-,p_+]\); on this interval \(p(1-p)\) is increasing and
\[
\beta(p):=\frac{1-2p}{2(1-p)}
\]
is decreasing.

Now suppose \(r=o(d)\). Since \(\rho_r<1/2\),
\[
F_{d,r}\le q_r\rho_r^d\le 2^{r-d}.
\tag{23}
\]
Consequently,
\[
\frac{F_{d,r}}{\alpha}\le 2^{2r-d}=o(1),
\qquad
dF_{d,r}=o(1).
\tag{24}
\]
It follows that
\[
p_\pm=\alpha(1+o(1)),
\tag{25}
\]
and
\[
\frac{p_-(1-p_-)}{(1-\alpha)^2}
=
(1-o(1))\frac{\alpha}{1-\alpha}
=
(1-o(1))\frac1{q_r}.
\tag{26}
\]
Furthermore,
\[
\beta(\alpha)
=
\frac{1-2^{1-r}}{2(1-2^{-r})}
=
\frac{2^{r-1}-1}{2^r-1}
=
\rho_r.
\tag{27}
\]
Since \(\beta(p_+)=\rho_r+O(F_{d,r})\) and \(dF_{d,r}=o(1)\),
\[
\beta(p_+)^d=(1+o(1))\rho_r^d.
\tag{28}
\]
Substituting (26) and (28) into (22) proves
\[
\Delta_{d,r}\ge(1-o(1))q_r^{-1}\rho_r^d.
\tag{29}
\]
Together with (8), this proves (1).

Finally, complementation gives
\[
\lambda(d,s)=\lambda(d,2^d-s),
\]
so the same result holds for \(s=2^d-2^{d-r}\).

---

## 5. Scope and remaining gaps

This resolves the exponential order of the deficit for the infinite family
\[
s=2^{d-r}\quad\text{and}\quad s=2^d-2^{d-r},
\qquad r=o(d).
\]
For fixed \(r\), this is stronger than a bound of the form \(1-O(1/s)\), since
\[
\rho_r<\frac12
\]
and the true deficit is \(\Theta_r(\rho_r^d)\).

It does not settle the catalogued problem:

1. The two constants in (1) differ by a factor \(q_r^2\); even for \(r=2\), exact values for general \(d\) are not proved here.
2. Targets with a nontrivial odd factor, fixed \(s\), or \(r\) comparable to \(d\) are not covered.
3. In particular, this gives no improvement on the conjectured asymptotic value of \(\lambda(d,1)\).
4. I have not independently checked whether this Fourier argument or its conclusion already appears in the full versions of the source paper or the later cited preprint.