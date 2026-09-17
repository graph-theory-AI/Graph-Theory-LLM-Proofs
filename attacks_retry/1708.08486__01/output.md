```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained construction gives a tower-height lower bound for p=3 throughout α⁴≤β≤α³/2, including the advertised half-random specialization.",
  "would_publish": false,
  "caveats": "The other odd primes and the full parameter-by-parameter extension of Theorem 2 are not established here; novelty relative to the source is not claimed."
}
```

## 1. Scope and partial result

I use the intended **odd-prime** interpretation. The characteristic-two calculation in the previous attempt does not address that problem.

For \(A\subseteq\mathbb F_3^n\), put
\[
t_A(d)=3^{-n}\sum_x1_A(x)1_A(x+d)1_A(x+2d).
\]
Define towers by
\[
T_0=2,\qquad T_{h+1}=2^{T_h}.
\]
All logarithms below are natural unless a base is indicated.

The following is the partial result proved here.

### Theorem
Set
\[
\kappa=\frac{\log 3}{\log(4/3)}>1.
\]
There is an absolute constant \(C\) such that, whenever
\[
0<\alpha\le \frac14,\qquad
\alpha^4\le\beta\le\frac{\alpha^3}{2},
\]
we have
\[
n_3(\alpha,\beta)\ge T_h,
\]
where
\[
h=
\max\left\{
0,\left\lfloor
\frac{1}{\log\kappa}
\log\!\left(
\frac{\log(1/\alpha)}
     {\log(\alpha^3/\beta)}
\right)-C
\right\rfloor
\right\}.
\tag{1}
\]

In particular,
\[
n_3(\alpha,\alpha^3/2)
\ge
T_{\left\lfloor c\log\log(1/\alpha)-C'\right\rfloor}
\tag{2}
\]
for sufficiently small \(\alpha\), with absolute \(c>0,C'\).

Thus the lower-bound order in the advertised half-random specialization is obtained for \(p=3\). The source’s upper bound, stated in the question to hold for all odd primes, supplies the corresponding upper-bound order.

The proof has three ingredients:

1. a dense finite seed with a strictly subrandom progression count in every nonzero direction;
2. a fibre construction that increases dimension exponentially while preserving that relative deficit;
3. a Fourier-support argument that amplifies a small relative deficit to a large one.

The third step is important: simply iterating the fibre construction preserves the deficit but does not amplify it.

---

## 2. An elementary seed in characteristic three

Let
\[
m_0=101,\qquad Q=3^{m_0},
\]
and identify \(\mathbb F_Q\) additively with \(\mathbb F_3^{m_0}\). Let \(A_0\) be the nonzero squares in \(\mathbb F_Q\). Its density is
\[
a_0=\frac{Q-1}{2Q}.
\]

Write \(\chi\) for the quadratic character, with \(\chi(0)=0\). Since \(m_0\) is odd,
\[
\chi(-1)=-1.
\]
For every \(d\ne0\), I claim that
\[
t_{A_0}(d)=\frac{Q-3}{8Q}.
\tag{3}
\]

To verify this, let \(f=(1+\chi)/2\). The difference between \(f\) and \(1_{A_0}\) occurs only at zero. A characteristic-three progression containing zero has point set
\[
\{0,d,-d\},
\]
and exactly one of \(d,-d\) is a square. Consequently its product is zero both for \(f\) and for \(1_{A_0}\).

We may therefore expand the progression product using \(f\). The linear character sums vanish. Each of the three pair sums is \(-1\), using
\[
\sum_x\chi(x)\chi(x+d)=-1\qquad(d\ne0).
\]
For completeness, the corresponding identity with \(d=1\) follows by counting solutions to
\[
y^2=x(x+1):
\]
after the invertible change of variables
\[
u=2x+1-2y,\qquad v=2x+1+2y,
\]
the equation becomes \(uv=1\), giving \(Q-1\) solutions.

Finally, the cubic sum vanishes because
\[
x(x+d)(x-d)=x^3-d^2x
\]
is odd and \(\chi(-1)=-1\). This proves (3).

Define
\[
q_0=\frac{Q^2(Q-3)}{(Q-1)^3}
=1-\frac{3Q-1}{(Q-1)^3}.
\tag{4}
\]
Then
\[
\frac12<q_0<1,\qquad
t_{A_0}(d)=q_0a_0^3\quad(d\ne0).
\tag{5}
\]
The deficit is extremely small, but strictly positive and fixed.

---

## 3. A dimension-amplifying fibre construction

### Lemma 1
Suppose \(m\ge101\), and \(A\subseteq\mathbb F_3^m\) has density \(a\) satisfying
\[
a\ge3^{-m/100},
\qquad
t_A(h)\le q a^3\quad(h\ne0),
\]
where \(1/2\le q<1\).

Set
\[
r=\left\lceil
\frac{\log(16/a^2)}{\log(4/3)}
\right\rceil,\qquad
b=(2/3)^r,\qquad
\ell=\left\lfloor3^{m/2}\right\rfloor.
\tag{6}
\]
There exists \(A^+\subseteq\mathbb F_3^{m+\ell}\) with density \(a^+=ab\) such that
\[
t_{A^+}(d)\le q(a^+)^3\quad(d\ne0),
\qquad
a^+\ge3^{-(m+\ell)/100}.
\tag{7}
\]

Moreover, \(A^+\) has the form
\[
A^+=
\{(y,z):y\in A,\ L_yz\in\{0,1\}^r\},
\tag{8}
\]
where \(L_y:\mathbb F_3^\ell\to\mathbb F_3^r\) are linear maps.

### Proof

Choose the \(L_y\), independently, as uniformly random \(r\times\ell\) matrices. Put \(K=|A|\). We require two properties.

**First property.** For every three distinct \(y_1,y_2,y_3\in A\), the stacked map
\[
z\longmapsto(L_{y_1}z,L_{y_2}z,L_{y_3}z)
\]
is surjective.

A fixed stacked matrix fails to have full row rank with probability at most \(3^{3r-\ell}\), by a union bound over its nonzero row dependencies. Thus the probability that this property fails is at most
\[
3^{3m+3r-\ell}.
\tag{9}
\]

**Second property.** For every \(v\ne0\),
\[
|\{y\in A:L_yv=0\}|
<
\tau,\qquad
\tau=\frac12Ka^2b^2.
\tag{10}
\]

For fixed \(v\ne0\), the count on the left is binomial with mean
\[
\mu=K3^{-r}.
\]
The choice of \(r\) gives
\[
3^{-r}\le \frac{a^2b^2}{16},
\]
so \(\mu\le\tau/8\). The elementary binomial upper-tail estimate gives
\[
\Pr(X\ge\tau)\le(e\mu/\tau)^\tau
\le(e/8)^\tau<e^{-\tau}.
\]
The probability that (10) fails for some \(v\ne0\) is therefore at most
\[
\exp(\ell\log3-\tau).
\tag{11}
\]

Here are sufficient numerical checks for these two failure probabilities to have sum less than one. Write
\[
u=\log_3(1/a)\le m/100.
\]
From (6),
\[
r\le8u+11.
\tag{12}
\]
Since \(b^2=(4/9)^r\ge3^{-r}\),
\[
\tau
=\frac12\,3^ma^3b^2
\ge\frac12\,3^{m-3u-r}
\ge\frac12\,3^{89m/100-11}.
\tag{13}
\]
For \(m\ge101\), these bounds imply
\[
\tau\ge2\ell\log3,\qquad
\ell\ge4m+600.
\]
Together with (12), equations (9) and (11) have sum less than one. Hence maps with both required properties exist.

Fix such maps and define \(A^+\) by (8). The first property also implies that every individual \(L_y\) is surjective, so the density is \(ab\).

Consider a difference \(d=(h,v)\).

* If \(h\ne0\), the three outer coordinates \(y,y+h,y+2h\) are distinct. Whenever they all belong to \(A\), the three corresponding linear maps are jointly surjective. Therefore
  \[
  t_{A^+}(h,v)=b^3t_A(h)\le q(ab)^3.
  \tag{14}
  \]

* If \(h=0\) and \(v\ne0\), use that \(\{0,1\}^r\subseteq\mathbb F_3^r\) contains no nontrivial three-term progression. A fibre contributes precisely when \(L_yv=0\), and then its contribution is \(b\). Thus
  \[
  t_{A^+}(0,v)
  =b\,3^{-m}|\{y\in A:L_yv=0\}|
  <\frac12a^3b^3
  \le q(ab)^3.
  \tag{15}
  \]

Finally,
\[
\log_3(1/a^+)
=u+r\log_3(3/2)
\le5u+\frac{11}{2}
\le\frac{m+\ell}{100}.
\]
This proves the lemma. ∎

---

## 4. Iteration, growth, and Fourier sparsity

Starting with \(A_0\), apply Lemma 1 repeatedly. Denote the resulting sets, dimensions, and densities by \(A_j,m_j,a_j\). Then
\[
m_{j+1}=m_j+\left\lfloor3^{m_j/2}\right\rfloor,
\qquad
t_{A_j}(d)\le q_0a_j^3\quad(d\ne0).
\tag{16}
\]

Let
\[
\lambda_j=\log(1/a_j).
\]
The definition of \(r_j\) gives
\[
\lambda_{j+1}
=\kappa\lambda_j+O(1),
\tag{17}
\]
where the additive term is bounded above and below by positive constants. Hence
\[
\lambda_j=\Theta(\kappa^j).
\tag{18}
\]

The dimensions satisfy the useful explicit lower bound
\[
m_j\ge4T_j^2.
\tag{19}
\]
Indeed, it holds initially, and
\[
m_{j+1}\ge3^{m_j/2}.
\]
If \(m_j\ge4T_j^2\), then
\[
3^{m_j/2}\ge3^{2T_j^2}\ge4T_{j+1}^2.
\]

We also need a structural property of the constructed sets. For a function on \(\mathbb F_3^D\), let its Fourier support mean the set of characters with nonzero Fourier coefficient.

### Lemma 2
For every \(j\ge1\),
\[
|\operatorname{supp}\widehat{1_{A_j}}|\le m_j^6.
\tag{20}
\]

### Proof

Write the last fibre construction with outer dimension \(m=m_{j-1}\) and fibre rank \(r=r_{j-1}\). Its indicator is
\[
1_{A_j}(y,z)
=
\sum_{y_0\in A_{j-1}}
1_{\{y=y_0\}}\,1_{\{L_{y_0}z\in\{0,1\}^r\}}.
\]
Each summand depends on at most \(m+r\) linear coordinates. Its Fourier support therefore lies in a subspace of size at most \(3^{m+r}\). Taking the union over at most \(3^m\) summands gives
\[
|\operatorname{supp}\widehat{1_{A_j}}|
\le3^{2m+r}.
\]
By (12), \(r\le0.08m+11\), so \(2m+r\le3m\) for \(m\ge101\). Also \(m_j\ge3^{m/2}\). Consequently
\[
3^{2m+r}\le3^{3m}\le m_j^6.
\]
∎

---

## 5. Amplifying the deficit using Fourier support

This lemma is the step that turns the tiny deficit in (4) into an arbitrarily large relative deficit.

### Lemma 3
Let \(A\subseteq\mathbb F_3^D\) be nonempty, with density \(a\), and let
\[
S=\operatorname{supp}\widehat{1_A}.
\]
If
\[
|S|^{3k}<3^D-1,
\tag{21}
\]
then there are invertible linear maps \(g_1,\ldots,g_k\) such that
\[
B=\bigcap_{i=1}^k g_i^{-1}A
\]
satisfies
\[
|B|/3^D=a^k
\tag{22}
\]
and, for every \(d\),
\[
t_B(d)=\prod_{i=1}^k t_A(g_i d).
\tag{23}
\]

In particular, if \(t_A(d)\le qa^3\) for all \(d\ne0\), then
\[
t_B(d)\le q^k(a^k)^3\quad(d\ne0).
\tag{24}
\]

### Proof

Since \(A\) is nonempty, \(0\in S\). Put
\[
\Gamma=S+S+S,
\qquad |\Gamma|\le|S|^3.
\]
Choose \(g_1,\ldots,g_k\) independently and uniformly from the invertible linear maps.

We want the following property:
\[
\xi_i\in\Gamma,\quad
\sum_{i=1}^k g_i^{T}\xi_i=0
\quad\Longrightarrow\quad
\xi_1=\cdots=\xi_k=0.
\tag{25}
\]
For a fixed nonzero tuple \((\xi_1,\ldots,\xi_k)\), condition on all maps except one corresponding to a nonzero \(\xi_i\). Its image is uniform among the \(3^D-1\) nonzero vectors. Thus the probability of the displayed relation is at most \(1/(3^D-1)\). A union bound bounds the probability that (25) fails by
\[
\frac{|\Gamma|^k}{3^D-1}<1.
\]
Fix maps satisfying (25).

The Fourier support of
\[
x\longmapsto
1_A(g_i x)1_A(g_i x+g_i d)1_A(g_i x+2g_i d)
\]
lies in \(g_i^T\Gamma\). Property (25) says that a product of these \(k\) functions has a zero-frequency contribution only by selecting the zero frequency from every factor. Its average is consequently the product of their averages, which is (23).

Taking \(d=0\) gives (22). Invertibility of the \(g_i\) gives (24). ∎

Notice that this does **not** assert that arbitrary linear images of arbitrary sets behave independently. The small Fourier support in (21) is essential.

---

## 6. Choosing the parameters and obtaining a set of density at least \(\alpha\)

Write
\[
L=\log(1/\alpha),\qquad
t=\log(\alpha^3/\beta).
\]
The range in the theorem gives
\[
\log2\le t\le L.
\tag{26}
\]
Let
\[
\sigma=-\log q_0>0,\qquad
k=\left\lceil\frac{t+\log16}{\sigma}\right\rceil.
\tag{27}
\]
Then
\[
q_0^k\le e^{-t}/16,
\qquad
k=\Theta(t),
\tag{28}
\]
where the implied constants are fixed, although very large.

For \(L/t\) sufficiently large, choose \(j\) maximal subject to
\[
k\lambda_j\le L/2.
\tag{29}
\]
By (18) and (28),
\[
j=\frac{\log(L/t)}{\log\kappa}+O(1).
\tag{30}
\]

I show that, for sufficiently large \(j\),
\[
n_3(\alpha,\beta)\ge T_j.
\tag{31}
\]
There are two cases.

### Case 1: \(L\ge\sqrt{m_j}\)

Let
\[
s=\left\lfloor\frac{L}{\log(3/2)}\right\rfloor.
\]
The set \(\{0,1\}^s\subseteq\mathbb F_3^s\) is progression-free and has density
\[
(2/3)^s\ge e^{-L}=\alpha.
\]
By (19),
\[
L\ge\sqrt{m_j}\ge2T_j,
\]
and hence \(s\ge T_j\). This is already a counterexample in dimension at least \(T_j\), proving (31).

### Case 2: \(L<\sqrt{m_j}\)

Put \(D=m_j\). By (20),
\[
|\operatorname{supp}\widehat{1_{A_j}}|\le D^6.
\]
Equations (26)–(28) imply
\[
k=O(t)=O(L)=O(\sqrt D).
\]
Therefore
\[
|\operatorname{supp}\widehat{1_{A_j}}|^{3k}
\le D^{18k}<3^D-1
\]
for sufficiently large \(j\). Lemma 3 applies.

It produces a set \(B\subseteq\mathbb F_3^D\) with density
\[
b=a_j^k=e^{-k\lambda_j}\ge e^{-L/2}=\sqrt\alpha\ge2\alpha,
\tag{32}
\]
and
\[
t_B(d)\le \frac{e^{-t}}{16}b^3
\qquad(d\ne0).
\tag{33}
\]

Independently retain each point of \(B\) with probability
\[
\theta=\frac{2\alpha}{b}\le1,
\]
obtaining \(B'\). Then
\[
\mathbb E\,\operatorname{dens}(B')=2\alpha.
\]
Because a nonzero characteristic-three progression has three distinct points,
\[
\mathbb E\,t_{B'}(d)
=\theta^3t_B(d)
\le\frac12\alpha^3e^{-t}
=\frac{\beta}{2}.
\tag{34}
\]

Let \(N=3^D\). Changing one retention variable changes the density by at most \(1/N\), and changes \(t_{B'}(d)\) by at most \(3/N\). The bounded-differences inequality therefore gives
\[
\Pr(\operatorname{dens}(B')<\alpha)
\le e^{-2\alpha^2N}
\]
and, for fixed \(d\ne0\),
\[
\Pr(t_{B'}(d)\ge\beta)
\le e^{-\beta^2N/18}.
\]
A union bound bounds the total failure probability by
\[
e^{-2\alpha^2N}
+N e^{-\beta^2N/18}.
\tag{35}
\]

Here
\[
\alpha^2N
=\exp(D\log3-2L)
\ge\exp(D\log3-2\sqrt D)
\]
and
\[
\beta^2N
=\exp(D\log3-6L-2t)
\ge\exp(D\log3-8\sqrt D).
\]
Consequently (35) is less than one for sufficiently large \(j\), uniformly over the parameters in this case.

There is thus an outcome \(B'\) of density at least \(\alpha\) with
\[
t_{B'}(d)<\beta\qquad(d\ne0).
\]
It is a counterexample in dimension \(D=m_j\), proving (31).

### Completing the parameter range

Equation (30) now proves (1) after increasing the absolute constant \(C\) to absorb:

* the threshold for \(j\) in the preceding argument;
* bounded values of \(L/t\);
* integer rounding.

When the displayed height in (1) is zero, the assertion \(n_3(\alpha,\beta)\ge T_0=2\) follows from the progression-free set \(\{0,1\}\subseteq\mathbb F_3\). Thus no small-height parameter cases are omitted.

This completes the proof of the partial theorem.

---

## 7. What this does and does not establish

The argument establishes an unconditional lower bound for \(p=3\), using no progression-free-set construction beyond the binary cube \(\{0,1\}^r\).

In particular, setting \(\beta=\alpha^3/2\) in (1) gives tower height
\[
\Omega(\log\log(1/\alpha)).
\]
More generally, for \(\beta=\alpha^{3+\eta}\) in the stated range, it gives a tower-height lower bound of order
\[
\Omega(\log(1/\eta))-O(1).
\]

The key extra mechanism is Lemma 3: the fibre construction produces sets with Fourier support polynomial in their **dimension**, allowing intersections of suitably chosen linear images to multiply progression deficits exactly.

However, I have **not** established the complete conjecture:

* the primes \(5,7,11,13,17\) are not treated here;
* the regime \(\beta>\alpha^3/2\) is not analyzed here;
* I am not asserting that (1), together with the quoted results, matches every parameter dependence and tower convention in the full statement of Theorem 2.

Nor have I independently established whether the partial bound above is already implicit in the source’s arguments. It should therefore be regarded as a proved restricted construction, not as a claimed resolution of the catalog conjecture.