```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For full Eichler-unit lattices one obtains the unconditional actual-diameter bound (64/25+o(1)) log V and coefficient 2 under a precise pointwise exceptional-spectrum hypothesis, whereas unrestricted arithmetic subgroups admit linear-diameter cyclic-cover counterexamples.",
  "would_publish": false,
  "caveats": "The conjecture is informal about its family and whether it asserts an upper bound or equality; the coefficient 2 remains open for the intended full-order family."
}
```

## 1. Precise interpretation

Let \(B/\mathbb Q\) be an indefinite division quaternion algebra, let \(\mathcal O\) be an Eichler order, and put
\[
\Gamma=P\mathcal O^1\subset \operatorname{PSL}_2(\mathbb R),\qquad
X_\Gamma=\Gamma\backslash\mathbb H.
\]
Write \(A_\Gamma=\operatorname{area}(X_\Gamma)\). The source's \(V_\Gamma\) differs from \(A_\Gamma\), if at all, by a fixed normalization, so
\[
\log A_\Gamma=\log(3V_\Gamma)+O(1).
\]

The natural difficult part of the speculation is the upper bound
\[
\operatorname{diam}(X_\Gamma)
   \le (2+o(1))\log(3V_\Gamma)
   \qquad (V_\Gamma\to\infty).
\tag{C}
\]
If “around” means an asymptotic equality, one must additionally specify and prove the corresponding lower bound. I address primarily (C).

There are two necessary quantifier warnings.

1. For a fixed compact \(X\) and \(w\in X\), the function \(z\mapsto d_X(z,w)\) is continuous. Consequently, if a fixed inequality \(d_X(z,w)\le R\) holds outside a null set, then it holds everywhere: a strict violation would persist on an open set of positive area. Thus “almost every” in the source cannot mean a literal null exceptional set on each fixed surface; it must mean a set of relative measure \(1-o(1)\) in a varying family.

2. If “arithmetic lattice” is interpreted in the usual broad sense of any lattice commensurable with an arithmetic one, then even an \(O(\log V_\Gamma)\) assertion is false. The restriction to full proper-unit groups of Eichler orders, or a similarly strong congruence restriction, is essential.

## 2. Counterexample to the unrestricted arithmetic-lattice reading

### Proposition 2.1

There is a sequence of cocompact arithmetic lattices \(\Gamma_n<\operatorname{PSL}_2(\mathbb R)\) such that
\[
\operatorname{area}(\Gamma_n\backslash\mathbb H)\asymp n,
\qquad
\operatorname{diam}(\Gamma_n\backslash\mathbb H)\gg n.
\]

### Proof

Start with any compact torsion-free arithmetic hyperbolic surface
\[
X_0=\Gamma_0\backslash\mathbb H.
\]
Such a surface is obtained, for example, by passing to a torsion-free finite-index subgroup of a norm-one group in an indefinite quaternion division algebra.

Choose a primitive class
\[
\phi\in H^1(X_0;\mathbb Z)
       =\operatorname{Hom}(\pi_1(X_0),\mathbb Z),
\]
and let \(X_n\to X_0\) be the cyclic cover corresponding to
\[
\ker\bigl(\pi_1(X_0)\xrightarrow{\phi}\mathbb Z\to\mathbb Z/n\mathbb Z\bigr).
\]
Then
\[
\operatorname{area}(X_n)=n\operatorname{area}(X_0).
\]

Represent \(\phi\) by a smooth closed one-form \(\omega\), and put
\[
M=\|\omega\|_\infty.
\]
Let \(T\) generate the deck group \(\mathbb Z/n\mathbb Z\), choose \(x\in X_n\), and set \(k=\lfloor n/2\rfloor\). Every path \(c\) from \(x\) to \(T^kx\) projects to a loop \(\bar c\) in \(X_0\) whose \(\phi\)-value is congruent to \(k\pmod n\). Hence
\[
|\phi([\bar c])|\ge \lfloor n/2\rfloor.
\]
On the other hand,
\[
|\phi([\bar c])|
 =\left|\int_{\bar c}\omega\right|
 \le M\,\operatorname{length}(c).
\]
Taking the infimum over \(c\) gives
\[
d_{X_n}(x,T^kx)\ge \frac{\lfloor n/2\rfloor}{M}.
\]
Thus \(\operatorname{diam}(X_n)\gg n\).

Each \(\pi_1(X_n)\) is a finite-index subgroup of the arithmetic lattice \(\Gamma_0\), hence arithmetic in the commensurability sense. These groups are generally not full unit groups of Eichler orders, so this does not disprove the intended narrow conjecture. ∎

## 3. An unconditional actual-diameter bound for the intended family

The standard spectral argument gives an explicit benchmark strictly weaker than coefficient \(2\).

### Theorem 3.1: spectral covering lemma

Let \(X\) be a compact hyperbolic orbifold of area \(A\). Assume:

1. there are constants \(\rho,v>0\), independent of \(X\), such that
   \[
   \operatorname{area} B_X(x,\rho)\ge v
   \quad\text{for every }x\in X;
   \]
2. every nonzero Laplace eigenvalue satisfies
   \[
   \lambda_j\ge \frac14-\vartheta^2
   \qquad\text{for some fixed }0\le\vartheta<\frac12.
   \]

Then, with \(\alpha=\frac12-\vartheta\),
\[
\operatorname{diam}(X)
 \le \frac{1}{\alpha}\log A+O_{\vartheta,\rho,v}(\log\log(A+2)).
\tag{3.1}
\]

#### Proof

Let \(b_R=2\pi(\cosh R-1)\) be the area of a radius-\(R\) ball in \(\mathbb H\). Define the universal-ball averaging operator
\[
(M_Rf)(x)=\frac1{b_R}\int_{B_{\mathbb H}(\widetilde x,R)}
                  f(\pi z)\,dz.
\]
It is self-adjoint, preserves constants, has nonnegative kernel, and its kernel is supported on pairs at quotient distance at most \(R\).

The spherical transform of the normalized ball satisfies, uniformly over all nonconstant spectral parameters allowed by the hypothesis,
\[
\left\|M_R\big|_{L^2_0(X)}\right\|
 \le C_\vartheta(1+R)e^{-\alpha R}.
\tag{3.2}
\]
Indeed, for tempered parameters the elementary spherical-function bound is
\[
|\varphi(r)|\ll (1+r)e^{-r/2},
\]
while for a complementary parameter \(0\le u\le\vartheta\),
\[
|\varphi_u(r)|\ll_\vartheta e^{-(1/2-u)r}.
\]
Integrating against \(2\pi\sinh r\,dr\) and dividing by \(b_R\asymp e^R\) gives (3.2).

For \(x\in X\), let
\[
f_x=\frac{\mathbf 1_{B_X(x,\rho)}}{\operatorname{area}B_X(x,\rho)}.
\]
Then \(\int_Xf_x=1\) and
\[
\|f_x\|_2\le v^{-1/2}.
\]
If \(d_X(x,y)>R+2\rho\), positivity and finite propagation give
\[
\langle M_Rf_x,f_y\rangle=0.
\tag{3.3}
\]
Writing \(f_x=A^{-1}+f_x^0\), spectral decomposition gives
\[
\langle M_Rf_x,f_y\rangle
 =\frac1A+\langle M_Rf_x^0,f_y^0\rangle.
\]
By (3.2),
\[
\left|\langle M_Rf_x^0,f_y^0\rangle\right|
 \le \frac{C_\vartheta(1+R)}v e^{-\alpha R}.
\]
Choose
\[
R=\frac1\alpha\left(\log A+2\log\log(A+2)+C_0\right)
\]
with \(C_0\) sufficiently large. Then the last error is strictly less than \(1/A\), contradicting (3.3). Therefore every pair satisfies \(d_X(x,y)\le R+2\rho\), proving (3.1). ∎

### Application to Eichler lattices

For \(\Gamma=P\mathcal O^1\), reduced traces are integers. Consequently:

- every hyperbolic element has
  \[
  |\operatorname{tr}\gamma|\ge3,
  \qquad
  \ell(\gamma)\ge 2\operatorname{arcosh}(3/2);
  \]
- a finite stabilizer has order at most \(3\), since an elliptic norm-one element has integral trace in \(\{-1,0,1\}\).

The hyperbolic Margulis lemma then supplies uniform \(\rho,v>0\): sufficiently small universal balls can overlap only through a finite cyclic stabilizer of order at most \(3\).

For the spectrum, Jacquet–Langlands transfer together with the established \(7/64\) bound toward Ramanujan for \(\mathrm{GL}_2/\mathbb Q\) gives
\[
\lambda_j\ge \frac14-\left(\frac7{64}\right)^2
            =\frac{975}{4096}
\]
for every nonconstant eigenfunction. Thus
\[
\vartheta=\frac7{64},\qquad
\alpha=\frac12-\frac7{64}=\frac{25}{64}.
\]
Theorem 3.1 yields the actual, not almost, diameter bound
\[
\boxed{\;
\operatorname{diam}(X_\Gamma)
 \le \frac{64}{25}\log A_\Gamma+O(\log\log A_\Gamma)
 =\left(\frac{64}{25}+o(1)\right)\log(3V_\Gamma).
\;}
\tag{3.4}
\]

This is likely implicit in the source's existing diameter bounds and is not claimed as a new publishable result.

### Special spectral case giving coefficient \(2\)

If a family satisfies
\[
\lambda_1(X_\Gamma)\ge \frac14-o(1),
\]
then \(\vartheta=o(1)\), so Theorem 3.1 gives
\[
\operatorname{diam}(X_\Gamma)
 \le (2+o(1))\log(3V_\Gamma).
\]
In particular, the desired upper bound holds for any family with entirely tempered nonconstant spectrum. This is only a sufficient special case; the diameter conjecture need not imply the full Ramanujan–Selberg assertion.

### A systolic refinement

If \(X\) is torsion-free with systole \(s_X\), one may use embedded endpoint balls of radius \(r<s_X/2\), whose areas are \(\asymp e^r\). The same proof gives
\[
\operatorname{diam}(X)
 \le 2r+\frac{\log A-r}{\alpha}+O_\vartheta(\log\log A).
\]
Taking \(r=s_X/2-O(1)\) yields
\[
\operatorname{diam}(X)
 \le \frac1\alpha\log A
   -\left(\frac1\alpha-2\right)\frac{s_X}{2}
   +O_\vartheta(\log\log A).
\tag{3.5}
\]
With \(\alpha=25/64\),
\[
\operatorname{diam}(X)
 \le \frac{64}{25}\log A-\frac7{25}s_X+O(\log\log A).
\tag{3.6}
\]
Thus large-systole subfamilies improve quantitatively on \(64/25\), although this alone does not reach \(2\) for general Eichler-order surfaces.

## 4. A precise pointwise estimate sufficient for coefficient \(2\)

The spectral-gap argument is wasteful because it treats a possibly exceptional eigenfunction as if it could concentrate maximally at both endpoints. The almost-diameter result only requires averaged control. The missing all-points input can be isolated as follows.

For each exceptional eigenvalue write
\[
\lambda_j=\frac14-\theta_j^2,\qquad
0<\theta_j\le\frac7{64},
\]
and normalize \(\|\phi_j\|_2=1\). Consider the pointwise exceptional-spectrum estimate
\[
\sup_{x\in X}
 \sum_{\theta_j\ge u}|\phi_j(x)|^2
 \le A^{-2u+o(1)}
\tag{PD}
\]
uniformly for \(u\) bounded away from \(0\) by a quantity tending slowly to zero.

### Proposition 4.1

For a uniformly thick family with complementary parameters bounded by some \(\theta_0<1/2\), condition (PD) implies
\[
\operatorname{diam}(X)\le(2+o(1))\log A.
\]

### Argument

Use fixed-radius radial endpoint bumps and take
\[
R=(2+\delta_A)\log A,
\qquad \delta_A\to0,
\]
where \(\delta_A\log A\to\infty\) sufficiently rapidly.

The tempered contribution is
\[
O\!\left((1+R)e^{-R/2}\right)
 =o(A^{-1}).
\]
Group the exceptional parameters into intervals
\([u,u+o(\delta_A)]\). The ball multiplier on such an interval is at most
\[
A^{-(2+\delta_A)(1/2-u)+o(\delta_A)}.
\]
By Cauchy–Schwarz and (PD), the corresponding spectral projector between the two endpoint bumps is at most
\[
A^{-2u+o(\delta_A)}.
\]
Their product is
\[
A^{-1-\delta_A(1/2-u)+o(\delta_A)}
 =o(A^{-1})
\]
uniformly because \(u\le\theta_0<1/2\). Very small \(u\) are handled by the uniform local spectral-projector bound and the extra \(\delta_A\) in \(R\). Thus every nonconstant spectral contribution is \(o(A^{-1})\), while the constant eigenfunction contributes exactly \(A^{-1}\). Positivity then forces the two endpoint neighborhoods to be joined within distance \(R\).

Condition (PD) also explains the almost-versus-actual gap. Integrating its left side gives
\[
\int_X\sum_{\theta_j\ge u}|\phi_j(x)|^2\,dx
   =\#\{j:\theta_j\ge u\}.
\]
A global density estimate controls only the spatial average of this projector and hence all but a small set of points. The actual diameter requires a uniform pointwise estimate such as (PD), ruling out concentration at the exceptional points.

I do not prove (PD) here; it is the substantive remaining arithmetic-analytic obstacle in this approach.

## 5. Lower bounds and final gap

Every compact hyperbolic orbifold of area \(A\) satisfies the elementary volume lower bound
\[
A\le 2\pi(\cosh D-1),
\qquad D=\operatorname{diam}(X),
\]
because a radius-\(D\) ball in the universal cover projects onto \(X\). Hence
\[
D\ge \operatorname{arcosh}\left(1+\frac{A}{2\pi}\right)
  =\log A+O(1).
\]
This gives only coefficient \(1\). If the source's statement that the almost-diameter estimate is “sharp” includes a formal lower bound
\[
D\ge(2-o(1))\log(3V_\Gamma)
\]
under the same family quantifiers, then only the upper bound remains.

Thus:

- the unrestricted arithmetic-lattice interpretation is disproved by cyclic covers;
- for full Eichler-unit lattices, the unconditional actual-diameter coefficient is at most \(64/25\);
- coefficient \(2\) follows from asymptotic temperedness, and more generally from the pointwise exceptional-spectrum estimate (PD);
- no unconditional proof of the intended coefficient-\(2\) assertion is obtained.