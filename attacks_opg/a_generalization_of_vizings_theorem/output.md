```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A probabilistic construction gives a simple 100-uniform hypergraph with maximum 99-codegree at most 200 that requires at least 451 colors, contradicting the proposed bound of 299.",
  "would_publish": true,
  "caveats": "Nonconstructive counterexamples of very large order; no claim of literature priority or resolution of the small-uniformity cases."
}
```

# A probabilistic counterexample

All logarithms below are natural. The edge-coloring condition in the question will be called **facet coloring**: two distinct \(d\)-edges must receive different colors whenever they have a common \((d-1)\)-subset.

I prove the following.

**Theorem.** There exists a finite, simple, \(100\)-partite, \(100\)-uniform hypergraph \(H\) such that:

1. every \(99\)-set is contained in at most \(200\) edges;
2. every facet coloring of \(H\) uses at least \(451\) colors.

The proposed upper bound is
\[
r+d-1=200+100-1=299,
\]
so this disproves the conjecture.

The proof uses an asymptotic upper bound on the number of matchings in a regular linear hypergraph. I give the counting argument in full, since it is the principal ingredient.

## 1. A matching-counting lemma

A hypergraph is **linear** if two distinct edges intersect in at most one vertex.

**Lemma.** Fix an integer \(s\ge 2\) and \(x\in(0,1)\). Let \(F\) be an \(s\)-uniform, \(D\)-regular, linear hypergraph on \(N\) vertices, and suppose
\[
m=\frac{xN}{s}
\]
is an integer. Write \(a_m(F)\) for the number of matchings of size \(m\). As \(D,N\to\infty\),
\[
\boxed{\quad
\log a_m(F)
\le
m\bigl(\log(D/x)-(s-1)\bigr)
-N(1-x)\log(1-x)+o(N).
\quad} \tag{1}
\]
The error is uniform over \(F\), with \(s,x\) fixed.

### 1.1 An entropy estimate for weighted perfect matchings

Consider an \(s\)-uniform hypergraph \(K\) on \(L\) vertices, with positive edge weights \(w(e)\). Let
\[
Z=\sum_{M\text{ perfect matching}}\prod_{e\in M}w(e).
\]

Suppose every vertex has weighted degree at most \(\Delta\). For a perfect matching \(M\), call an edge \(e\) **bad relative to \(M\)** if
\[
|e\cap f|\ge 2
\quad\text{for some }f\in M.
\]
Assume that, for every perfect matching \(M\) and every vertex \(v\),
\[
\sum_{\substack{e\ni v\\e\text{ bad relative to }M}}w(e)
\le \varepsilon\Delta. \tag{2}
\]

Then
\[
\log Z
\le
\frac{L}{s}\left[
\log\Delta+
\int_0^1\log\bigl(u^{s-1}+\varepsilon\bigr)\,du
\right]. \tag{3}
\]
In particular, if \(\varepsilon\to0\), then
\[
\log Z
\le
\frac{L}{s}\bigl(\log\Delta-(s-1)+o(1)\bigr). \tag{4}
\]

Here is a proof. The case \(Z=0\) is immediate. Otherwise choose a random perfect matching with
\[
\Pr(M)=\frac{\prod_{e\in M}w(e)}{Z}.
\]
Its entropy satisfies
\[
H(M)+\mathbb E\sum_{e\in M}\log w(e)=\log Z. \tag{5}
\]

Independently assign each vertex a uniform label in \([0,1]\), and process vertices in decreasing label order. At a vertex \(v\), reveal its matching edge \(M(v)\), unless that edge has already been revealed.

If \(v\) is still uncovered by revealed matching edges, let \(S_v\) be the sum of the weights of all edges containing \(v\) and avoiding those revealed matching edges. The elementary entropy inequality
\[
H(P)+\sum_i P_i\log w_i\le \log\sum_i w_i
\]
applied conditionally at each reveal, followed by the entropy chain rule, gives
\[
\log Z\le
\sum_v
\mathbb E\!\left[
\mathbf 1_{\{v\text{ first in }M(v)\}}\log S_v
\right]. \tag{6}
\]
Each matching-edge weight is counted exactly once, at its first vertex.

Fix \(M\), and condition on \(v\) having label \(t\). The probability that \(v\) is first in \(M(v)\) is \(t^{s-1}\). Conditional on that event, consider a nonbad edge \(e\ni v\). Its other \(s-1\) vertices lie in \(s-1\) different matching edges, all distinct from \(M(v)\). For \(e\) to remain available, all vertices of those \(s-1\) matching edges must have labels below \(t\). This has probability
\[
t^{s(s-1)}.
\]
The bad edges have total weight at most \(\varepsilon\Delta\). Thus
\[
\mathbb E[S_v\mid M,\ t,\ v\text{ first in }M(v)]
\le
\Delta t^{s(s-1)}+\varepsilon\Delta.
\]
Jensen's inequality in (6) now yields
\[
\log Z\le
L\int_0^1 t^{s-1}
\log\!\left(\Delta(t^{s(s-1)}+\varepsilon)\right)\,dt.
\]
Substituting \(u=t^s\) proves (3). Finally,
\[
\int_0^1\log(u^{s-1}+\varepsilon)\,du
\longrightarrow
\int_0^1(s-1)\log u\,du=-(s-1),
\]
which proves (4).

### 1.2 Completing partial matchings with weighted auxiliary edges

We apply this estimate to prove (1). Put
\[
u=N-sm=N(1-x),\qquad b=(s-1)u.
\]
Adjoin a set \(B\) of \(b\) new vertices to \(F\). Construct a weighted \(s\)-uniform hypergraph \(K\) as follows:

- retain the edges of \(F\), each with weight \(1\);
- for every old vertex \(a\) and every \(C\in\binom{B}{s-1}\), add the edge \(\{a\}\cup C\), with weight
  \[
  w=\frac{(1-x)D/x}{\binom{b}{s-1}}.
  \]

Every old vertex has weighted degree
\[
D+\binom{b}{s-1}w=\frac D x.
\]
Every new vertex has weighted degree
\[
N\binom{b-1}{s-2}w
=
N\frac{s-1}{b}\frac{(1-x)D}{x}
=\frac D x.
\]
Thus \(K\) is weighted-regular with
\[
\Delta=\frac D x.
\]

We verify (2), uniformly over perfect matchings \(M\) of \(K\).

An original edge of \(F\) cannot meet an auxiliary matching edge in two vertices, because an auxiliary edge contains only one old vertex. By linearity, an original edge can meet an original matching edge in two vertices only if the two edges are equal. Consequently, through any vertex, the total weight of bad original edges is at most \(1\).

For auxiliary edges, choose one uniformly from those containing a fixed vertex \(v\). There are only \(\binom{s}{2}\) pairs of positions to consider. Each vertex has at most \(s-1\) partners in its matching edge, whereas the old and new vertex pools both have order \(N\). A union bound therefore gives
\[
\Pr(\text{the auxiliary edge is bad relative to }M)
=O_{s,x}(N^{-1}),
\]
uniformly in \(M,v\). More explicitly, for \(b>s\), each pair contributes at most
\[
\frac{s-1}{\min\{N,b-s\}}.
\]
All auxiliary edges through \(v\) have the same weight. Hence the total bad-edge weight through \(v\) is at most
\[
1+O_{s,x}(\Delta/N).
\]
We may therefore take
\[
\varepsilon=\Delta^{-1}+O_{s,x}(N^{-1})=o(1).
\]
The weighted perfect-matching estimate applies.

Every perfect matching of \(K\) uses exactly \(u\) auxiliary edges, because these must cover the \(b=(s-1)u\) new vertices. It consequently uses exactly \(m\) original edges.

Conversely, each \(m\)-edge matching in \(F\) has exactly
\[
\frac{b!}{((s-1)!)^u}
\]
completions: partition the new vertices into an \((s-1)\)-set for each of the \(u\) uncovered old vertices. Therefore
\[
Z=a_m(F)\,\frac{b!}{((s-1)!)^u}\,w^u. \tag{7}
\]

The number of vertices of \(K\) is
\[
N+b=s(m+u).
\]
By (4),
\[
\log Z\le
(m+u)\bigl(\log(D/x)-(s-1)\bigr)+o(N). \tag{8}
\]
Stirling's formula gives
\[
\log\!\left(\frac{b!}{((s-1)!)^u}w^u\right)
=
u\left(\log\frac{(1-x)D}{x}-(s-1)\right)+o(N). \tag{9}
\]
Subtracting (9) from (8), using (7), proves (1). \(\square\)

## 2. The random hypergraph

Fix
\[
d=100.
\]
Let \(n\) tend to infinity through multiples of \(5\), and take \(100\) disjoint vertex classes
\[
V_1,\ldots,V_{100},
\qquad |V_i|=n.
\]
Let \(H_0\) consist of all transversal edges: one vertex from each class. Thus
\[
|E(H_0)|=n^{100}.
\]
Put
\[
T=n^{99}.
\]

Construct an auxiliary hypergraph \(F\):

- its vertices are the \(99\)-element facets of edges of \(H_0\);
- each edge of \(H_0\) gives an edge of \(F\) consisting of its \(100\) facets.

There are
\[
N=100T
\]
vertices in \(F\). Moreover, \(F\) is \(100\)-uniform, \(n\)-regular, and linear. Indeed, two different transversal \(100\)-sets cannot have two common \(99\)-subsets.

A collection of edges of \(H_0\) can receive one color precisely when the corresponding edges of \(F\) form a matching.

Independently retain each edge of \(H_0\) with probability
\[
p=\frac{100}{n},
\]
obtaining a random hypergraph \(H_{\mathrm{rand}}\). The corresponding edge-subhypergraph of \(F\) is obtained by the same independent sampling.

### 2.1 With high probability, no color class can be large

Set
\[
m=\frac T5,\qquad x=\frac{100m}{N}=\frac15.
\]
The expected number of \(m\)-edge matchings in the sampled auxiliary hypergraph is
\[
p^m a_m(F).
\]

More generally, substituting \(p=c/D\) into (1) gives
\[
\log\bigl(p^m a_m(F)\bigr)
\le
\frac Ns\left[
x\log(c/x)+x-sf(x)
\right]+o(N), \tag{10}
\]
where
\[
f(x)=x+(1-x)\log(1-x).
\]
Since \(f(0)=f'(0)=0\) and \(f''(x)=1/(1-x)\ge1\),
\[
f(x)\ge\frac{x^2}{2}. \tag{11}
\]

Here \(s=c=100\), \(x=1/5\), and \(N/s=T\). By (11),
\[
x\log(c/x)+x-sf(x)
\le
\frac{\log500+1}{5}-2
<
-\frac25,
\]
where the last inequality uses \(\log500<7\). Consequently, for all sufficiently large \(n\),
\[
\mathbb E[\text{number of \(m\)-edge matchings}]
\le e^{-T/5}. \tag{12}
\]

Let \(A\) be the event that \(H_{\mathrm{rand}}\) has no facet-disjoint family of \(m\) edges. The first-moment bound gives
\[
\Pr(A^c)\le e^{-T/5}. \tag{13}
\]

### 2.2 Enforcing maximum codegree \(200\)

From \(H_{\mathrm{rand}}\), delete every edge containing a facet whose degree in \(H_{\mathrm{rand}}\) exceeds \(200\). Denote the resulting hypergraph by \(H\), and put
\[
Z=|E(H)|.
\]
Every \(99\)-set now has degree at most \(200\). Nontransversal \(99\)-sets have degree zero.

We estimate the number of retained edges. Conditional on a particular edge being present, the number of other sampled edges through any one of its facets has distribution
\[
X\sim\operatorname{Bin}(n-1,100/n).
\]
Using Markov's inequality on \(2^X\),
\[
\Pr(X\ge200)
\le
2^{-200}(1+100/n)^{n-1}
\le
\frac{e^{100}}{2^{200}}
=
\left(\frac e4\right)^{100}.
\]
Write
\[
q=\left(\frac e4\right)^{100}.
\]
A union bound over the \(100\) facets of the edge shows that
\[
\mathbb E Z
\ge
100T(1-100q)>99T. \tag{14}
\]
The last inequality is very generous: \(q<10^{-10}\).

There is also the deterministic bound
\[
Z\le200T, \tag{15}
\]
obtained by summing facet degrees and dividing by \(100\).

Combining (13)–(15),
\[
\mathbb E[Z\mathbf 1_A]
\ge
\mathbb E Z-200T\Pr(A^c)
>
99T-200T e^{-T/5}
>
90T
\]
for sufficiently large \(n\). Hence some outcome satisfies both
\[
A
\qquad\text{and}\qquad
|E(H)|>90T. \tag{16}
\]

## 3. The coloring contradiction

Choose an outcome satisfying (16).

Deleting edges cannot create a larger facet-disjoint family. Since \(A\) holds, every color class in any facet coloring of \(H\) contains at most
\[
m-1<\frac T5
\]
edges.

If \(450\) colors sufficed, then
\[
|E(H)|
\le450(m-1)
<
450\frac T5
=
90T,
\]
contrary to (16). Thus \(H\) requires at least \(451\) colors.

It is simple, \(100\)-uniform, and has maximum \(99\)-codegree at most \(200\). This proves the theorem and disproves the conjecture. \(\square\)

## 4. The failure is asymptotically larger than an additive error

The same argument gives an unbounded-factor failure as \(d\) increases.

Take sampling probability \(p=d/n\), prune at codegree \(2d\), and choose
\[
a=\lceil5\log d\rceil,\qquad x=\frac ad.
\]
For sufficiently large \(d\), \(x<1\). The exponent in (10) is at most
\[
x\left(\log(d/x)+1-\frac{dx}{2}\right)
=
x\left(2\log d-\log a+1-\frac a2\right)<0.
\]
Choose \(n\) divisible by \(d\), so that the required matching size is integral.

Pruning retains \((1-o_d(1))dT\) edges in a suitable outcome, while every color class has fewer than \(xT\) edges. Consequently there are examples with maximum facet degree at most \(2d\) and
\[
\chi_{\mathrm{facet}}(H)
\ge
(1-o_d(1))\frac{d^2}{5\log d}.
\]
The conjectured bound in this regime is only \(3d-1\).

## Scope and limitations

This is a probabilistic existence proof, not a small explicit incidence list. All estimates concern finite hypergraphs; “sufficiently large \(n\)” is justified by the proved asymptotic counting lemma.

No unproved conjecture or literature assertion is used. I have not verified priority for this counterexample argument, and nothing here resolves the versions restricted to small uniformity, such as \(d=3\).