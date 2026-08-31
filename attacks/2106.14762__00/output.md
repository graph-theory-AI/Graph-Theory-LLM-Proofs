```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "A direct size-biased run-profile calculation gives interior density e^(y-1) in every block of runs sorted by its first entry, hence no dependence on x.",
  "would_publish": false,
  "caveats": "The proof is probabilistic-combinatorial rather than bijective; novelty and the intended scope of “direct” have not been independently verified."
}
```

# Statement

Let \(\pi_n\) be uniform in \(S_n\), and let \(\sigma_n=\mathsf{runsort}(\pi_n)\). Write

\[
\mu_n=\frac1n\sum_{j=1}^n \delta_{(j/n,\sigma_n(j)/n)}
\]

for its empirical permuton.

The argument below derives directly from the statistics of a single ascending run that \(\mu_n\) converges in probability to the measure \(R\) satisfying

\[
\boxed{
\begin{aligned}
\int f\,dR
={}&\int_0^1\int_0^{y e^{1-y}}
      f(x,y)e^{y-1}\,dx\,dy\\
&+\int_0^1(1-y)f\!\left(y e^{1-y},y\right)\,dy
\end{aligned}}
\tag{1}
\]

for every continuous \(f\colon[0,1]^2\to\mathbb R\).

In particular, the absolutely continuous density is

\[
\boxed{\frac{dR_{\mathrm{ac}}}{dx\,dy}(x,y)=e^{y-1}
\quad\text{whenever }x<ye^{1-y},}
\]

which is independent of \(x\). The second term in (1) is singular and lies on the boundary \(x=ye^{1-y}\).

The key point is that the cancellation producing \(e^{y-1}\) occurs at the level of the expected profile of one run, before evaluating the boundary function \(ye^{1-y}\).

---

# 1. Mark each entry by the first entry of its run

For an entry \(\pi_n(i)\), let \(A_n(i)\) denote the first value in the ascending run containing \(\pi_n(i)\). Define the marked occupation measure

\[
\eta_n=\frac1n\sum_{i=1}^n
 \delta_{\left(A_n(i)/n,\ \pi_n(i)/n\right)}.
\tag{2}
\]

Its first marginal is the size-biased distribution of run starters:

\[
\rho_n=\frac1n\sum_{i=1}^n\delta_{A_n(i)/n}
      =\frac1n\sum_{\text{runs }B}|B|\,
          \delta_{a(B)/n},
\]

where \(a(B)\) is the first entry of \(B\). Let

\[
H_n(z)=\rho_n([0,z]).
\tag{3}
\]

Because distinct runs have distinct first entries, lexicographic sorting of the runs is simply sorting by \(a(B)\).

If \(p_n(i)\) is the position of \(\pi_n(i)\) after runsort and \(L_n\) is the maximum run length, then

\[
\left|\frac{p_n(i)}n-H_n\!\left(\frac{A_n(i)}n\right)\right|
\leq \frac{L_n}{n}.
\tag{4}
\]

Indeed, \(H_n(A_n(i)/n)\) is the right endpoint of the block occupied by the run containing \(\pi_n(i)\), and that block has length at most \(L_n/n\).

Moreover,

\[
\Pr(L_n\geq m)\leq \frac{n}{m!},
\tag{5}
\]

since an ascending run of length at least \(m\) contains an increasing block of \(m\) consecutive entries, and any specified block is increasing with probability \(1/m!\). Hence

\[
\frac{L_n}{n}\xrightarrow{\mathrm p}0.
\tag{6}
\]

Thus, asymptotically, runsort sends an entry with run starter \(z\) to horizontal coordinate \(H_n(z)\).

---

# 2. The local run-occupation measure

Consider a bi-infinite sequence of independent uniform random variables

\[
\ldots,U_{-2},U_{-1},U_0.
\]

Let \(Y=U_0\), and let \(Z\) be the first value in the increasing suffix ending at \(U_0\). Thus, if that suffix has \(k+1\) terms, then

\[
U_{-k}<U_{-k+1}<\cdots<U_0,
\qquad
U_{-k-1}>U_{-k},
\]

and \(Z=U_{-k}\).

For \(k=0\), the current entry is itself a run starter. Therefore the diagonal contribution to the joint law of \((Z,Y)\) is

\[
(1-y)\,dy\,\delta_y(dz).
\tag{7}
\]

For \(k\geq1\), fix \(Z=z<y=Y\). The \(k-1\) intermediate variables must lie in \((z,y)\) in increasing order, a region of volume

\[
\frac{(y-z)^{k-1}}{(k-1)!}.
\]

The variable preceding the run starter must exceed \(z\), contributing a factor \(1-z\). Summing over \(k\geq1\) gives

\[
(1-z)\sum_{k\geq1}\frac{(y-z)^{k-1}}{(k-1)!}
=(1-z)e^{y-z}.
\]

Consequently the limiting marked occupation measure is

\[
\boxed{
\eta(dz,dy)
=(1-z)\,dz\,\delta_z(dy)
+\mathbf 1_{\{z<y\}}(1-z)e^{y-z}\,dz\,dy.}
\tag{8}
\]

There is also a direct run interpretation. Runs with starter near \(z\) occur with intensity \((1-z)\,dz\). Conditional on such a starter, the expected occupation density of later run entries at height \(y>z\) is

\[
\sum_{j\geq1}\frac{(y-z)^{j-1}}{(j-1)!}\,dy
=e^{y-z}\,dy.
\]

Thus (8) is precisely the expected vertical profile of runs grouped according to their first entry.

---

# 3. Justification of the local limit

We record why (8) describes the empirical measure (2), rather than only the law around one position.

Let \(g\in C([0,1]^2)\). Truncate the search for the beginning of the run after \(K\) positions to the left. The truncated mark is a function of a window of at most \(K+1\) consecutive entries.

For an index away from the left boundary, truncation can fail only if the last \(K+1\) entries are increasing. Hence

\[
\mathbb E\left[
\frac1n\#\{i:\text{truncation fails at }i\}
\right]
\leq \frac Kn+\frac1{(K+1)!}.
\tag{9}
\]

For fixed \(K\), the empirical average of the truncated local statistic converges in \(L^2\) to its i.i.d.-uniform expectation:

* only \(O(Kn)\) pairs of windows overlap;
* for two disjoint windows, their joint distribution differs from the product of their marginal distributions by \(O(K^2/n)\) in total variation—the only obstruction in independently sampling the two windows is reuse of one of the \(O(K)\) labels.

Thus the variance tends to zero for fixed \(K\). Letting first \(n\to\infty\), then \(K\to\infty\), and using (9), gives

\[
\int g\,d\eta_n
\xrightarrow{\mathrm p}
\int g\,d\eta.
\tag{10}
\]

Using a countable convergence-determining family of continuous functions yields

\[
\eta_n\Longrightarrow\eta
\qquad\text{in probability}.
\tag{11}
\]

This also proves concentration of the run-profile counts needed below.

---

# 4. Size-biased starters and the direct cancellation

The first marginal of \(\eta\) has density

\[
\begin{aligned}
r(z)
&=(1-z)\left(1+\int_z^1e^{y-z}\,dy\right)\\
&=(1-z)e^{1-z}.
\end{aligned}
\tag{12}
\]

Equivalently, a run beginning at \(z\) has expected length

\[
1+\int_z^1e^{y-z}\,dy=e^{1-z},
\]

and such runs occur with intensity \(1-z\).

Let

\[
H(z)=\int_0^z r(t)\,dt.
\tag{13}
\]

The decisive identity is

\[
\boxed{
(1-z)e^{y-z}=r(z)e^{y-1}\qquad(z<y).}
\tag{14}
\]

After sorting, runs whose starters lie in an infinitesimal interval \(dz\) occupy horizontal width

\[
dx=r(z)\,dz.
\]

Among those entries, the mass with vertical coordinate in \(dy\), away from the run-starter diagonal, is

\[
(1-z)e^{y-z}\,dz\,dy
=r(z)\,dz\,e^{y-1}dy
=dx\,e^{y-1}dy.
\]

Thus their interior vertical density is \(e^{y-1}\), independently of the starter \(z\), and hence independently of the horizontal position after sorting.

More formally, for \(0\leq a<b<c<d\leq1\),

\[
\begin{aligned}
\eta\big((a,b)\times(c,d)\big)
&=\int_a^b\int_c^d(1-z)e^{y-z}\,dy\,dz\\
&=\left(\int_a^br(z)\,dz\right)
  \left(\int_c^d e^{y-1}\,dy\right).
\end{aligned}
\tag{15}
\]

The runs with starters in \((a,b)\) occupy the horizontal interval
\((H(a),H(b))\). Hence

\[
R\big((H(a),H(b))\times(c,d)\big)
=
\big(H(b)-H(a)\big)
\int_c^d e^{y-1}\,dy.
\tag{16}
\]

Rectangles of this form constitute a basis for the open region below the boundary, proving horizontal uniformity directly.

Notice that this step does not require an explicit formula for \(H\).

---

# 5. Identification of the boundary

For completeness, (12) gives

\[
H(z)=\int_0^z(1-t)e^{1-t}\,dt
=z e^{1-z}.
\tag{17}
\]

Since the first marginal of \(\eta\) is continuous, (11) implies

\[
\sup_{z\in[0,1]}|H_n(z)-H(z)|
\xrightarrow{\mathrm p}0.
\tag{18}
\]

Combining (4), (6), (11), and (18), for every continuous \(f\),

\[
\int f\,d\mu_n
\xrightarrow{\mathrm p}
\int f(H(z),y)\,\eta(dz,dy).
\tag{19}
\]

Thus the runsort limit is the pushforward of \(\eta\) under

\[
(z,y)\longmapsto (H(z),y).
\]

On the off-diagonal part \(z<y\), set \(x=H(z)\). Since

\[
dx=H'(z)\,dz=(1-z)e^{1-z}\,dz,
\]

equation (14) gives

\[
(1-z)e^{y-z}\,dz\,dy=e^{y-1}\,dx\,dy.
\]

Furthermore,

\[
z<y\quad\Longleftrightarrow\quad
x=H(z)<H(y)=ye^{1-y}.
\]

The diagonal term of (8) maps to the boundary curve
\(x=H(y)=ye^{1-y}\), with mass \((1-y)\,dy\). This proves formula (1).

Equivalently, the conditional horizontal law at height \(y\) is

\[
\boxed{
R(dx\mid Y=y)
=
e^{y-1}\mathbf 1_{\{0<x<ye^{1-y}\}}\,dx
+(1-y)\delta_{ye^{1-y}}(dx).}
\tag{20}
\]

The continuous part has total mass

\[
e^{y-1}\,y e^{1-y}=y,
\]

and the boundary atom has mass \(1-y\), as expected.

---

# Gaps and scope

There is no unresolved mathematical step in the argument above. It proves convergence in probability to the stated measure; together with the already-established existence of the runsort permuton, this identifies that limit with \(R\).

The only interpretive caveat is the word “direct.” This proof does not invoke the known explicit formula for \(R\); it derives horizontal uniformity from the one-run profile identity (14), evaluating \(H(z)=ze^{1-z}\) only afterward to recover the boundary. It is, however, a probabilistic-combinatorial local-limit proof rather than a finite-\(n\) bijection.