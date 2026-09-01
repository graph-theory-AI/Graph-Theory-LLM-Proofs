```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact interior function remains open, but an extremal construction gives epsilon at most 1-sqrt(1-delta), exactly solves the perfect and dominating-vertex cases, and yields the correct first-order behavior as delta tends to zero.",
  "would_publish": false,
  "caveats": "The literal all-degree statement has answer zero; the substantive results use the intended large-Delta supremal interpretation and the source-paper normalization."
}
```

# 1. Precise formulation and a quantifier issue

I use the source-paper convention that a graph \(G\), of maximum degree \(\Delta\), is \(\delta\)-sparse if

\[
e(G[N(v)])\le (1-\delta)\binom{\Delta}{2}
\qquad\text{for every }v\in V(G).
\tag{1}
\]

This global normalization by \(\Delta(G)\), rather than by \(d(v)\), is essential below.

Taken literally, with no lower bound on \(\Delta\), the question has the trivial answer

\[
\varepsilon(\delta)=0
\qquad\text{for every }\delta\in[0,1].
\]

Indeed, \(K_2\) is \(\delta\)-sparse for every \(\delta\), since \(\Delta=1\) and both sides of (1) are zero, while

\[
\chi(K_2)=2=\Delta+1.
\]

Thus every positive \(\varepsilon\) fails. Conversely, \(\varepsilon=0\) is the greedy bound.

The intended question is plainly asymptotic in \(\Delta\). A convenient precise parameter is

\[
R(\delta):=
\limsup_{m\to\infty}
\sup\left\{
\frac{\chi(G)}{m+1}:
\Delta(G)=m,\ G\text{ is }\delta\text{-sparse}
\right\},
\]

and then

\[
\varepsilon_\infty(\delta):=1-R(\delta).
\tag{2}
\]

This is the supremal saving: every \(\varepsilon<\varepsilon_\infty(\delta)\) works for all sufficiently large \(\Delta\), while every \(\varepsilon>\varepsilon_\infty(\delta)\) fails infinitely often. Attainment at equality is a separate rounding issue.

# 2. Exact clique obstruction

For \(m\ge1\), define

\[
b_m(\delta):=
\left\lfloor
\frac{1+\sqrt{1+4(1-\delta)m(m-1)}}{2}
\right\rfloor.
\tag{3}
\]

Equivalently, \(b_m(\delta)\) is the largest integer \(b\le m\) satisfying

\[
b(b-1)\le (1-\delta)m(m-1).
\tag{4}
\]

## Proposition 1

Among all \(\delta\)-sparse graphs of maximum degree \(m\), the largest possible clique number is exactly

\[
b_m(\delta)+1.
\tag{5}
\]

Moreover, the same value is the largest possible chromatic number in either of the following two subclasses:

1. perfect \(\delta\)-sparse graphs of maximum degree \(m\);
2. \(\delta\)-sparse graphs having a dominating vertex.

### Proof: upper bound on the clique number

Suppose \(G\) contains a clique \(K_t\), and let \(v\) be a vertex of that clique. Then \(N(v)\) contains a \(K_{t-1}\), so

\[
\binom{t-1}{2}
\le e(G[N(v)])
\le (1-\delta)\binom{m}{2}.
\]

Thus \(t-1\le b_m(\delta)\), proving

\[
\omega(G)\le b_m(\delta)+1.
\tag{6}
\]

For perfect graphs, \(\chi(G)=\omega(G)\), giving the corresponding chromatic upper bound.

### Construction attaining equality

Let \(b=b_m(\delta)\), let \(B\) be a clique of order \(b\), let \(A\) be an independent set of order \(m-b\), and add a vertex \(u\) adjacent to every vertex of \(A\cup B\). There are no edges between \(A\) and \(B\). In symbols,

\[
G_{m,b}=K_1\vee\bigl(K_b\cup \overline K_{m-b}\bigr).
\tag{7}
\]

Then

\[
d(u)=m,\qquad d(x)=b\ (x\in B),\qquad d(y)=1\ (y\in A),
\]

so \(\Delta(G_{m,b})=m\). Its neighbourhood edge counts are

\[
e(G[N(u)])=\binom b2,
\]

\[
e(G[N(x)])=\binom b2\quad(x\in B),
\]

and

\[
e(G[N(y)])=0\quad(y\in A).
\]

Condition (4) therefore says exactly that \(G_{m,b}\) is \(\delta\)-sparse.

The set \(B\cup\{u\}\) is a clique of order \(b+1\), and all vertices of \(A\) can reuse a color appearing on \(B\). Hence

\[
\chi(G_{m,b})=\omega(G_{m,b})=b+1.
\tag{8}
\]

The graph is a clique with pendant vertices attached at \(u\), and is in particular perfect.

### Dominating-vertex upper bound

Now suppose \(G\) has a dominating vertex \(u\), so \(|V(G)|=m+1\). Put \(H=G-u\) and \(k=\chi(H)\). In any proper \(k\)-coloring of \(H\), every pair of color classes has an edge between them; otherwise those two classes could be merged. Consequently,

\[
e(H)\ge \binom{k}{2}.
\tag{9}
\]

Since \(H=G[N(u)]\), sparsity gives

\[
\binom{k}{2}\le (1-\delta)\binom m2,
\]

and hence \(k\le b_m(\delta)\). Because \(u\) is dominating,

\[
\chi(G)=k+1\le b_m(\delta)+1.
\]

Construction (7) attains equality. ∎

# 3. Consequence for the general asymptotic problem

Let

\[
q=\sqrt{1-\delta}.
\]

From (3),

\[
\frac{b_m(\delta)}m\longrightarrow q.
\]

Construction (7) therefore satisfies

\[
\frac{\chi(G_{m,b_m})}{m+1}
=
\frac{b_m(\delta)+1}{m+1}
\longrightarrow \sqrt{1-\delta}.
\]

Thus

\[
R(\delta)\ge \sqrt{1-\delta},
\]

or equivalently,

\[
\boxed{\;
\varepsilon_\infty(\delta)
\le 1-\sqrt{1-\delta}.
\;}
\tag{10}
\]

This obstruction is connected and perfect, and it exactly saturates the possible clique number. In particular, for perfect graphs and for graphs with a dominating vertex,

\[
\boxed{\;
\varepsilon_{\infty,\mathrm{perfect}}(\delta)
=
\varepsilon_{\infty,\mathrm{dominating}}(\delta)
=
1-\sqrt{1-\delta}.
\;}
\tag{11}
\]

As \(\delta\downarrow0\),

\[
1-\sqrt{1-\delta}
=
\frac{\delta}{2}+\frac{\delta^2}{8}+O(\delta^3).
\tag{12}
\]

Hence no general theorem can have a first-order saving larger than \(\delta/2\).

The Hurley–de Joannis de Verclos–Kang result cited in the prompt gives, after translating notation, the asymptotic lower bound

\[
\varepsilon_\infty(\delta)
\ge
\frac{\delta}{2}-\frac{\delta^{3/2}}6,
\tag{13}
\]

or at least the weaker consequence

\[
\varepsilon_\infty(\delta)\ge \frac{\delta}{2}-O(\delta^{3/2}).
\]

Combining (10) and (13) gives

\[
\frac{\delta}{2}-\frac{\delta^{3/2}}6
\le
\varepsilon_\infty(\delta)
\le
1-\sqrt{1-\delta},
\tag{14}
\]

and in particular the exact first-order asymptotic

\[
\boxed{\;
\lim_{\delta\downarrow0}
\frac{\varepsilon_\infty(\delta)}{\delta}
=
\frac12.
\;}
\tag{15}
\]

The lower bound (13) is an external literature input; its probabilistic proof is not reproduced here.

# 4. A different obstruction when \(\delta\) is close to \(1\)

The clique construction is not asymptotically the strongest obstruction near the triangle-free endpoint. A standard clique-blow-up construction gives a larger chromatic ratio.

## 4.1 Clique blow-ups of triangle-free graphs

Let \(F\) be a triangle-free graph with maximum degree \(D\), and let \(F[K_t]\) be the graph obtained by replacing every vertex of \(F\) by a clique of order \(t\), with complete joins between fibers corresponding to adjacent vertices of \(F\).

Then

\[
\Delta(F[K_t])=(D+1)t-1.
\tag{16}
\]

For a vertex lying in the fiber corresponding to a vertex of degree \(d\), its neighbourhood spans

\[
\binom{t-1}{2}
+d\binom t2
+d\,t(t-1)
=
\frac{(t-1)((3d+1)t-2)}2
\tag{17}
\]

edges. There are no edges between two different neighboring fibers because \(F\) is triangle-free.

Set

\[
\rho_D:=\frac{3D+1}{(D+1)^2}.
\tag{18}
\]

A direct cross-multiplication gives

\[
\frac{(t-1)((3D+1)t-2)}
{((D+1)t-1)((D+1)t-2)}
\le \rho_D.
\tag{19}
\]

Indeed, after clearing denominators, the difference between the right and left sides is

\[
D(D-1)\bigl(3(D+1)t-2\bigr)\ge0.
\]

Therefore \(F[K_t]\) is \((1-\rho_D)\)-sparse.

Let \(\chi_t(F)\) denote the \(t\)-fold chromatic number of \(F\). A proper coloring of \(F[K_t]\) is exactly a \(t\)-fold coloring of \(F\), so

\[
\chi(F[K_t])=\chi_t(F).
\]

By the standard characterization of fractional chromatic number,

\[
\frac{\chi_t(F)}t\longrightarrow\chi_f(F)
\]

along a suitable sequence, and hence

\[
\frac{\chi(F[K_t])}{\Delta(F[K_t])+1}
\longrightarrow
\frac{\chi_f(F)}{D+1}.
\tag{20}
\]

Thus any triangle-free \(F\) with large fractional chromatic number furnishes an obstruction.

## 4.2 Suitable triangle-free base graphs exist

### Lemma 2

There is an absolute constant \(c>0\) such that, for every sufficiently large integer \(D\), there is a triangle-free graph \(F\) with

\[
\Delta(F)=D
\qquad\text{and}\qquad
\chi_f(F)\ge c\,\frac D{\log D}.
\tag{21}
\]

### Proof

Put \(s=\lfloor D/4\rfloor\), \(n=s^4\), and take

\[
H\sim G(n,s^{-3}).
\]

The expected degree is asymptotic to \(s\).

Standard Chernoff bounds show that, with probability tending to one,

\[
\Delta(H)\le2s.
\tag{22}
\]

The expected number of triangles is at most \(s^3/6\), so by Markov's inequality, with probability tending to one the number of triangles is at most \(s^{7/2}\).

Let

\[
r=\left\lceil8s^3\log s\right\rceil.
\]

The expected number of independent sets of order \(r\) is at most

\[
\binom nr(1-s^{-3})^{\binom r2}
\le
\left(\frac{en}{r}\right)^r
\exp\left(-s^{-3}\binom r2\right).
\]

For large \(s\),

\[
\log\left(\frac{en}{r}\right)\le\log s,
\]

while

\[
s^{-3}\binom r2\ge 16s^3(\log s)^2.
\]

The logarithm of the preceding expectation is therefore at most

\[
9s^3(\log s)^2-16s^3(\log s)^2\to-\infty.
\]

Thus, with probability tending to one,

\[
\alpha(H)<r.
\tag{23}
\]

Choose an \(H\) satisfying these three properties, and delete one vertex from every triangle. At most \(s^{7/2}\) vertices are deleted. The resulting graph \(H_0\) is triangle-free and satisfies

\[
|V(H_0)|\ge \frac{s^4}{2},\qquad
\alpha(H_0)\le 9s^3\log s,\qquad
\Delta(H_0)\le2s.
\]

For every graph \(J\),

\[
\chi_f(J)\ge \frac{|V(J)|}{\alpha(J)},
\]

so

\[
\chi_f(H_0)\ge \frac{s}{18\log s}.
\tag{24}
\]

Finally, take the disjoint union of \(H_0\) and a star \(K_{1,D}\). Fractional chromatic number is the maximum over components, while the resulting graph has maximum degree exactly \(D\). Since \(s=\Theta(D)\), (21) follows. ∎

## 4.3 Endpoint asymptotics

Write

\[
p=1-\delta.
\]

For small \(p>0\), choose

\[
D=\left\lceil\frac3p\right\rceil.
\]

Since

\[
\rho_D=\frac{3D+1}{(D+1)^2}\le\frac3D\le p,
\]

the graphs \(F[K_t]\) constructed above are \((1-p)\)-sparse. Equations (20) and (21) yield

\[
R(1-p)\ge \frac{c'}{\log(1/p)}
\tag{25}
\]

for an absolute \(c'>0\).

In the opposite direction, the established sparse-neighbourhood theorem of Alon, Krivelevich and Sudakov states that if every neighbourhood spans at most \(\Delta^2/f\) edges, then

\[
\chi(G)\le C\frac{\Delta}{\log f}
\]

for an absolute \(C\), in the relevant range of \(f\). Taking \(f=2/p\) gives

\[
R(1-p)\le \frac{C'}{\log(1/p)}.
\tag{26}
\]

Consequently,

\[
\boxed{\;
1-\varepsilon_\infty(1-p)
=
\Theta\!\left(\frac1{\log(1/p)}\right)
\qquad(p\downarrow0).
\;}
\tag{27}
\]

Equivalently,

\[
\boxed{\;
1-\varepsilon_\infty(\delta)
=
\Theta\!\left(
\frac1{\log\!\frac1{1-\delta}}
\right)
\qquad(\delta\uparrow1).
\;}
\tag{28}
\]

The lower obstruction in (25) was proved above; the matching upper order in (26) uses the cited established coloring theorem.

In particular, under the supremal asymptotic convention,

\[
\varepsilon_\infty(0)=0,\qquad
\varepsilon_\infty(1)=1.
\]

At \(\delta=1\), the value \(1\) is a supremum and is not attained by the literal inequality, since nonempty graphs have positive chromatic number.

# 5. Remaining gap

The exact value of \(\varepsilon_\infty(\delta)\) for a fixed interior value \(0<\delta<1\) is not determined here.

The proven information is:

\[
\frac{\delta}{2}-\frac{\delta^{3/2}}6
\ \le\
\varepsilon_\infty(\delta)
\ \le\
1-\sqrt{1-\delta},
\]

together with:

- exact first-order behavior \(\varepsilon_\infty(\delta)\sim\delta/2\) as \(\delta\downarrow0\);
- exact order of \(1-\varepsilon_\infty(\delta)\) as \(\delta\uparrow1\);
- the exact finite and asymptotic answer for perfect graphs and for graphs with a dominating vertex.

The main unresolved issue is whether nonperfect graphs can force a larger chromatic ratio than the clique obstruction for fixed moderate \(\delta\), and by how much. The clique argument alone only controls \(\omega(G)\), not \(\chi(G)\), so it does not prove the general upper bound \(R(\delta)\le\sqrt{1-\delta}\).