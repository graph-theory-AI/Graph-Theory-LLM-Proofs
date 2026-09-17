```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit amplification gives a uniform iterated-logarithm lower bound and determines the asymptotic maximum when r - log* d tends to infinity, but does not settle fixed r >= 4.",
  "would_publish": false,
  "caveats": "No matching fixed-r upper bound is obtained; novelty relative to the full source paper has not been checked."
}
```

# A uniform lower-bound amplification

I do not resolve the principal fixed-\(r\) question. I replace the previous attempt’s upper-bound approach by an explicit construction. It gives:

- a quantitative lower bound with leading constant \(1\) for every fixed \(r\);
- a uniform statement when \(r\) grows with \(d\);
- in particular, an asymptotically sharp answer when
  \[
  r-\log^* d\longrightarrow\infty.
  \]

The argument is self-contained and uses no external coloring theorem. It may be a quantitative reformulation of the source paper’s lower-bound construction; I have not verified the full paper and make no novelty claim.

## 1. Statement

For integers \(d\ge 0\) and \(r\ge 2\), let
\[
F_r(d):=\sup\{\chi_f(G):G\text{ is a finite, nonempty, }d\text{-degenerate, }K_r\text{-free graph}\}.
\]
A supremum avoids assuming attainment.

Define, for \(x\ge1\),
\[
A_0(x)=x,\qquad A_{j+1}(x)=1+\log A_j(x),
\]
where logarithms are natural.

### Theorem 1
For all \(d\ge0\) and \(r\ge2\),
\[
\boxed{\frac{d+1}{A_{r-2}(d+1)}\le F_r(d)\le d+1.} \tag{1}
\]

The upper bound is greedy coloring. The lower bound is the substantive assertion.

For fixed \(r\ge3\), write \(L_j(x)=\log^{\circ j}x\) for the \(j\)-fold iterated logarithm. Then (1) gives
\[
\boxed{
F_r(d)\ge
\frac{d+1}{L_{r-2}(d)+1+o(1)}
=(1-o(1))\frac{d}{L_{r-2}(d)}.
} \tag{2}
\]

There is also a uniform consequence. Set
\[
k=\log^*(d+1)
:=\min\{j\ge0:L_j(d+1)\le1\},
\]
with \(L_0(x)=x\).

### Corollary 2
If \(r=k+2+m\), where \(m\ge0\) is an integer, then
\[
\boxed{
\frac{2m+3}{2m+9}(d+1)\le F_r(d)\le d+1.
} \tag{3}
\]
Consequently, if \(r=r(d)\) satisfies
\[
r(d)-\log^*(d+1)\longrightarrow\infty,
\]
then
\[
\boxed{F_{r(d)}(d)=(1-o(1))(d+1).} \tag{4}
\]

Thus a slowly growing clique bound already permits fractional chromatic number arbitrarily close, in relative terms, to the unrestricted degeneracy bound.

---

## 2. The amplification construction

We use the dual formulation
\[
\chi_f(G)=
\max\left\{
w(V(G)):
w\ge0,\quad w(I)\le1\text{ for every independent set }I
\right\}. \tag{5}
\]

### Lemma 3 — Block amplification
Let \(r\ge3\), let \(0\le\delta<d\), and put \(k=d-\delta\). Suppose:

- \(G\) is \(d\)-degenerate and \(K_r\)-free, with \(\chi_f(G)=t\);
- \(H\) is \(\delta\)-degenerate and \(K_{r-1}\)-free, with \(\chi_f(H)=h\).

There is a finite \(d\)-degenerate \(K_r\)-free graph \(G'\) such that
\[
\chi_f(G')\ge
h+t\left(1-\left(1-\frac1t\right)^k\right). \tag{6}
\]

### Construction

Take \(k\) disjoint labeled copies \(G_1,\ldots,G_k\) of \(G\).

For every tuple
\[
\mathbf v=(v_1,\ldots,v_k)\in V(G_1)\times\cdots\times V(G_k),
\]
add a fresh copy \(H_{\mathbf v}\) of \(H\), and join every vertex of \(H_{\mathbf v}\) to all of \(v_1,\ldots,v_k\). Add no other edges.

This is completely finite: if \(G\) and \(H\) have \(n\) and \(N\) vertices, respectively, then \(G'\) has
\[
kn+n^kN
\]
vertices.

### Degeneracy and clique number

Order all the new \(H\)-copies before the old \(G\)-copies. Within each \(H\)-copy use a \(\delta\)-degeneracy ordering. Each new vertex has at most
\[
\delta+k=d
\]
later neighbors. After the new blocks have been removed, what remains is a disjoint union of \(d\)-degenerate graphs. Hence \(G'\) is \(d\)-degenerate.

The selected vertices \(v_1,\ldots,v_k\) are independent, since they belong to distinct old copies. A clique meeting \(H_{\mathbf v}\) therefore consists of a clique in \(H_{\mathbf v}\), together with at most one old vertex. Its order is at most
\[
(r-2)+1=r-1.
\]
Different new blocks have no edges between them. Cliques entirely in the old part are also smaller than \(r\). Thus \(G'\) is \(K_r\)-free.

### Fractional-chromatic lower bound

Choose optimal dual weights \(u\) on \(G\) and \(z\) on \(H\), so that
\[
u(V(G))=t,\qquad z(V(H))=h,
\]
and both weightings give every independent set weight at most \(1\).

Put
\[
q=1-\frac1t,\qquad a=\frac{1-q^k}{k}.
\]
Assign weight \(a\,u(v)\) to every old vertex \(v\).

For a tuple \(\mathbf v=(v_1,\ldots,v_k)\), define
\[
\pi_{\mathbf v}=\prod_{i=1}^k\frac{u(v_i)}{t},
\]
and assign weight \(\pi_{\mathbf v}z(x)\) to the vertex corresponding to \(x\in V(H)\) in \(H_{\mathbf v}\).

Let \(I\) be an independent set of \(G'\), and write
\[
x_i=u(I\cap V(G_i))\in[0,1].
\]
A new block can contribute to \(I\) only if none of its selected old vertices belongs to \(I\). Consequently, the total new weight in \(I\) is at most
\[
\sum_{\substack{\mathbf v\\v_i\notin I\ \forall i}}\pi_{\mathbf v}
=
\prod_{i=1}^k\left(1-\frac{x_i}{t}\right).
\]
The total weight of \(I\) is therefore at most
\[
a\sum_{i=1}^kx_i+
\prod_{i=1}^k\left(1-\frac{x_i}{t}\right). \tag{7}
\]

This is affine in each coordinate separately, so its maximum over \([0,1]^k\) occurs at a corner. At a corner with \(m\) coordinates equal to \(1\), its value is
\[
am+q^m.
\]
For \(0<q<1\), convexity gives
\[
q^m\le 1-\frac mk+\frac mkq^k,
\]
and hence
\[
am+q^m\le1.
\]
The case \(q=0\) follows directly: the value is \(1\) when \(m=0\), and \(m/k\) otherwise.

Thus the proposed weights are dual-feasible. Their total is
\[
kat+h\sum_{\mathbf v}\pi_{\mathbf v}
=t(1-q^k)+h,
\]
because \(\sum_{\mathbf v}\pi_{\mathbf v}=1\). This proves (6). ∎

---

## 3. A structural recursion for the extremal function

The preceding construction yields more than one particular asymptotic lower bound.

### Proposition 4
For \(r\ge3\) and \(0\le\delta\le d\),
\[
\boxed{
F_{r-1}(\delta)
\le
F_r(d)\left(1-\frac1{F_r(d)}\right)^{d-\delta}.
} \tag{8}
\]
When \(d=\delta\), the factor with exponent \(0\) is interpreted as \(1\).

### Proof

First suppose \(\delta<d\), and fix an admissible graph \(H\) with \(\chi_f(H)=h\). Choose admissible graphs \(G_j\) such that
\[
t_j:=\chi_f(G_j)\longrightarrow F_r(d).
\]
Lemma 3 and the definition of the supremum give
\[
F_r(d)\ge
h+t_j\left(1-\left(1-\frac1{t_j}\right)^{d-\delta}\right).
\]
Taking the limit and rearranging,
\[
h\le
F_r(d)\left(1-\frac1{F_r(d)}\right)^{d-\delta}.
\]
Now take the supremum over \(H\).

For \(\delta=d\), the assertion is just
\[
F_{r-1}(d)\le F_r(d).
\]
∎

For every integer \(k\ge0\), the function
\[
g_k(t)=t\left(1-\frac1t\right)^k,\qquad t\ge1,
\]
is strictly increasing, with the preceding convention for \(k=0\). Thus (8) can be used by finding any \(T\ge1\) for which
\[
T\left(1-\frac1T\right)^{d-\delta}\le F_{r-1}(\delta);
\]
such a \(T\) is necessarily a lower bound on \(F_r(d)\).

---

## 4. Proof of the uniform bound

The key quantitative step is the following.

### Lemma 5
Let \(s\ge2\), \(d\ge0\), and \(a\ge1\). Suppose
\[
F_s(e)\ge\frac{e+1}{a}
\qquad\text{for every }0\le e\le d.
\]
Then
\[
F_{s+1}(d)\ge\frac{d+1}{1+\log a}. \tag{9}
\]

### Proof

Put
\[
D=d+1,\qquad T=\frac{D}{1+\log a}.
\]
If \(T\le1\), there is nothing to prove. Assume \(T>1\). Since \(a\ge1\), we have \(T\le D\).

Let
\[
b=\lfloor T\rfloor,\qquad \delta=b-1,\qquad q=1-\frac1T.
\]
Then \(0\le\delta\le d\) and \(d-\delta=D-b\).

Write \(\theta=T-b\in[0,1)\). Convexity of \(q^x\) on \([0,1]\) gives
\[
q^\theta\le (1-\theta)+\theta q
=1-\frac{\theta}{T}
=\frac bT.
\]
Also, using \(\log(1-1/T)\le-1/T\),
\[
q^{D-T}
\le \exp\left(-\frac{D-T}{T}\right)
=\exp\left(1-\frac DT\right)
=\frac1a.
\]
It follows that
\[
Tq^{d-\delta}
=Tq^{D-T}q^{T-b}
\le\frac ba
\le F_s(b-1).
\]
Proposition 4 and monotonicity of \(g_{d-\delta}\) now imply
\[
F_{s+1}(d)\ge T.
\]
∎

### Proof of Theorem 1

Fix \(D=d+1\). We prove, by induction on \(j\ge0\), that
\[
F_{j+2}(e)\ge\frac{e+1}{A_j(D)}
\qquad\text{for every }0\le e\le d. \tag{10}
\]

For \(j=0\), this follows from
\[
F_2(e)=1\ge\frac{e+1}{D}.
\]
Given (10), apply Lemma 5 to each \(e\le d\), using \(a=A_j(D)\). This gives
\[
F_{j+3}(e)\ge
\frac{e+1}{1+\log A_j(D)}
=\frac{e+1}{A_{j+1}(D)}.
\]
Taking \(j=r-2\) and \(e=d\) proves the lower bound in (1). ∎

---

## 5. Consequences for fixed \(r\)

For each fixed \(j\ge1\),
\[
A_j(d+1)=L_j(d)+1+o(1).
\]
This follows immediately by induction, since all finitely many iterated logarithms involved tend to infinity. Equation (2) follows.

In particular,
\[
F_4(d)\ge(1-o(1))\frac{d}{\log\log d}. \tag{11}
\]
This independently rules out
\[
F_4(d)=O\left(\frac{d\log\log d}{\log d}\right),
\]
because the ratio of the lower-bound scale in (11) to that proposed scale is
\[
\frac{\log d}{(\log\log d)^2}\longrightarrow\infty.
\]
The same conclusion holds for every fixed \(r\ge4\).

### The logarithmic ambiguity in the supplied catalog

Under the standard convention,
\[
\log^{r-2}d=(\log d)^{r-2},
\]
the catalog’s displayed lower bound would not imply its stated separation from the maximum-degree analogy. The previous attempt’s warning on this point is correct.

The construction above instead proves a bound involving **iterated logarithms**, which does imply that separation. I have not checked whether this is the intended notation in the actual statement of Theorem 1.6.

### A stronger scalar bound for \(r=3\)

Taking \(\delta=0\) in (8) gives
\[
F_3(d)\left(1-\frac1{F_3(d)}\right)^d\ge1. \tag{12}
\]
Thus, for \(d\ge1\), \(F_3(d)\) is at least the unique \(T_d>1\) satisfying
\[
T_d\left(1-\frac1{T_d}\right)^d=1.
\]

For example, if \(s_d\log s_d=d\), then
\[
s_d\left(1-\frac1{s_d}\right)^d
\le s_de^{-d/s_d}=1,
\]
so \(F_3(d)\ge s_d\). This yields
\[
F_3(d)\ge
\frac{d}{\log d-\log\log d+o(1)}.
\]
No upper-bound conclusion is being inferred from this scalar recursion.

---

## 6. Proof of the growing-\(r\) consequence

We first show
\[
A_{\log^*D}(D)\le3
\qquad(D\ge1). \tag{13}
\]

The cases \(\log^*D=0,1\) are immediate. Otherwise let \(k=\log^*D\ge2\) and write \(L_j=L_j(D)\). For \(j\le k-2\), we have \(L_j>e\). Starting from \(A_0(D)=L_0\), induction gives
\[
A_j(D)\le L_j+2\qquad(0\le j\le k-1),
\]
because
\[
1+\log(L_j+2)
=L_{j+1}+1+\log\left(1+\frac2{L_j}\right)
\le L_{j+1}+2.
\]
Since \(L_{k-1}\le e\),
\[
A_k(D)\le1+\log(e+2)<3.
\]
This proves (13).

Now set
\[
x_m=A_{k+m}(D)-1.
\]
Then \(0\le x_0\le2\) and
\[
x_{m+1}=\log(1+x_m).
\]
For \(0\le x\le2\),
\[
\log(1+x)\le\frac{3x}{3+x}. \tag{14}
\]
Indeed, the difference between the right side and the left side vanishes at \(0\), and its derivative is
\[
\frac{9}{(3+x)^2}-\frac1{1+x}
=\frac{x(3-x)}{(3+x)^2(1+x)}\ge0.
\]
Whenever \(x_m>0\), (14) implies
\[
\frac1{x_{m+1}}\ge\frac1{x_m}+\frac13.
\]
The case \(x_m=0\) is trivial. Therefore
\[
x_m\le\frac1{1/2+m/3}
=\frac6{2m+3}.
\]
Combining this with Theorem 1,
\[
F_{k+2+m}(d)
\ge
\frac{d+1}{1+6/(2m+3)}
=
\frac{2m+3}{2m+9}(d+1),
\]
which proves Corollary 2.

For a concrete formulation, given \(0<\varepsilon<1\), if
\[
r\ge
2+\log^*(d+1)+\left\lceil\frac3\varepsilon\right\rceil,
\]
then
\[
F_r(d)\ge\frac{d+1}{1+\varepsilon}
>(1-\varepsilon)(d+1).
\]
Hence some finite admissible graph has fractional chromatic number greater than \((1-\varepsilon)(d+1)\). No attainment of the supremum is needed.

---

## 7. What remains unresolved

The full extremal function is not determined here. In particular, for fixed \(r\ge4\), the bounds established in this writeup leave
\[
(1-o(1))\frac{d}{\log^{\circ(r-2)}d}
\le F_r(d)\le d+1.
\]

The amplification recursion is one-sided: it forces lower bounds on \(F_r(d)\), but supplies no upper bound. It would be unjustified to reverse it or assume that the resulting constructions are extremal.

The complete partial result is the uniform lower bound (1), including the asymptotically sharp growing-\(r\) regime (4). The main missing ingredient remains a substantially stronger unrestricted upper bound for fixed \(r\ge4\), or a construction exceeding the iterated-logarithm scale.