```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A closed-neighborhood deficit inequality proves the conjecture for all claw-free graphs, bounded-degree or bounded-average-degree graphs, and graphs with clique-cover number sufficiently close to their independence number, with exact bounds for perfect graphs.",
  "would_publish": false,
  "caveats": "The argument does not cover dense, highly imperfect graphs with unbounded induced stars; throughout, 'maximal' is interpreted as maximum-cardinality."
}
```

# 1. Statement and notation

Write \(\alpha_0(G)\) for the independence number, to distinguish it from the independence ratio. Let

\[
r=\alpha_0(G),\qquad a=\frac rn\in(0,1/2),
\]

and let \(W\subseteq V(G)\) contain each vertex independently with probability \(1/2\). Set

\[
F(G)=\mathbb E\,\alpha_0(G[W]),\qquad
D(G)=r-F(G).
\]

Thus the conjecture asks whether, for every fixed \(a\in(0,1/2)\),

\[
D(G)\ge \varepsilon^{**}(a)n
\]

for every graph with \(\alpha_0(G)=an\), for some \(\varepsilon^{**}(a)>0\).

I interpret “the maximal independent set contained in \(W\)” as a maximum-cardinality independent set of \(G[W]\). If “maximal” is meant only inclusionwise, the random variable is not canonical; all the upper bounds below remain valid for an arbitrary maximal independent set because its size is at most \(\alpha_0(G[W])\).

The general conjecture remains unresolved below the ranges stated in the question. The main new ingredient here is the following elementary but useful graph-dependent certificate.

# 2. A closed-neighborhood deficit inequality

## Proposition 2.1

Let \(I\) be any maximum independent set of \(G\). Then

\[
\boxed{\quad
D(G)\ge \sum_{v\in I}2^{-|N_G[v]|}.
\quad} \tag{2.1}
\]

### Proof

For a realization of \(W\), define

\[
X_W=\{v\in I:W\cap N_G[v]=\varnothing\}.
\]

Let \(J\) be a maximum independent set in \(G[W]\). Since \(W\cap N[X_W]=\varnothing\), no vertex of \(J\) lies in or is adjacent to \(X_W\). Hence \(J\cup X_W\) is independent in \(G\). The maximality of \(I\) in cardinality gives

\[
|J|+|X_W|\le r.
\]

Consequently,

\[
r-\alpha_0(G[W])\ge |X_W|.
\]

Taking expectations and using linearity,

\[
D(G)\ge \sum_{v\in I}\Pr(W\cap N[v]=\varnothing)
       =\sum_{v\in I}2^{-|N[v]|}.
\]

This proves (2.1). \(\square\)

By convexity of \(x\mapsto 2^{-x}\), (2.1) gives the convenient consequence

\[
\frac{D(G)}n
 \ge a\,2^{-\frac1r\sum_{v\in I}|N[v]|}. \tag{2.2}
\]

This estimate is exact for a disjoint union of equal-sized cliques: choose one vertex of \(I\) in each component, and \(v\in X_W\) exactly when its entire clique is absent from \(W\).

# 3. Consequences for graph classes

## 3.1 \(K_{1,t}\)-free graphs

## Theorem 3.1

Let \(t\ge2\) be fixed. If \(G\) is induced-\(K_{1,t}\)-free and \(\alpha_0(G)=an\), then

\[
\boxed{\quad
\frac{F(G)}n
\le
a-
a\,2^{-((t-1)/a-(t-2))}.
\quad} \tag{3.1}
\]

In particular, the conjecture holds for every fixed induced-star-free class, for all \(a\in(0,1/2)\).

### Proof

Fix a maximum independent set \(I\), \(|I|=r\). Every vertex \(x\notin I\) has at most \(t-1\) neighbors in \(I\), since \(t\) such neighbors, being pairwise nonadjacent, together with \(x\) would induce \(K_{1,t}\). Therefore

\[
\sum_{v\in I}|N[v]|
 =r+e(I,V\setminus I)
 \le r+(t-1)(n-r).
\]

Dividing by \(r=an\),

\[
\frac1r\sum_{v\in I}|N[v]|
\le
1+(t-1)\frac{1-a}{a}
=
\frac{t-1}{a}-(t-2).
\]

Now apply (2.2). \(\square\)

The function

\[
\varepsilon_t(a)
=
a\,2^{-((t-1)/a-(t-2))}
\]

is strictly increasing in \(a\), because

\[
\frac{d}{da}\log \varepsilon_t(a)
=
\frac1a+\frac{(t-1)\log 2}{a^2}>0.
\]

Thus it also has the monotonicity requested in the conjecture.

### Claw-free graphs

Taking \(t=3\) gives:

\[
\boxed{\quad
\frac{F(G)}n
\le
a-a\,2^{-(2/a-1)}
\qquad\text{for every claw-free }G.
\quad} \tag{3.2}
\]

Hence Conjecture 2.9 holds for all claw-free graphs, including all line graphs, throughout the entire interval \(a\in(0,1/2)\).

This genuinely reaches the unresolved range \(a\le1/4\), although only for this graph class.

## 3.2 Bounded degree and bounded average degree

If \(\Delta(G)\le \Delta\), then \(|N[v]|\le \Delta+1\) for all \(v\), and Proposition 2.1 yields

\[
\boxed{\quad
\frac{F(G)}n
\le a-a\,2^{-(\Delta+1)}.
\quad} \tag{3.3}
\]

More generally, if \(e(G)\le Cn\), then for any maximum independent set \(I\),

\[
\sum_{v\in I}d(v)=e(I,V\setminus I)\le e(G)\le Cn.
\]

Hence

\[
\frac1r\sum_{v\in I}|N[v]|
\le 1+\frac Ca,
\]

and therefore

\[
\boxed{\quad
\frac{F(G)}n
\le
a-a\,2^{-(1+C/a)}.
\quad} \tag{3.4}
\]

Thus every class of uniformly bounded average degree satisfies the conjecture for all admissible independence ratios. This does not subsume the regular-graph result quoted in the question when the regular degree is allowed to grow with \(n\).

# 4. Clique partitions and the exact perfect-graph case

Let \(\theta(G)=\chi(\overline G)\), equivalently the minimum number of cliques whose vertex sets partition \(V(G)\).

## Proposition 4.1

Suppose \(V(G)\) is partitioned into \(q\) cliques. Write

\[
n=kq+b,\qquad 0\le b<q.
\]

Then

\[
\boxed{\quad
F(G)\le q-L(n,q),
\quad
L(n,q):=(q-b)2^{-k}+b2^{-(k+1)}.
\quad} \tag{4.1}
\]

Consequently,

\[
D(G)\ge \max\{0,r-q+L(n,q)\}. \tag{4.2}
\]

### Proof

Let the clique sizes be \(s_1,\dots,s_q\). Every independent set in \(G[W]\) contains at most one vertex from each clique, so

\[
\alpha_0(G[W])
\le \sum_{i=1}^q {\bf 1}_{W\cap C_i\ne\varnothing}.
\]

Taking expectations,

\[
F(G)\le q-\sum_{i=1}^q2^{-s_i}. \tag{4.3}
\]

Subject to \(s_i\ge1\) and \(\sum s_i=n\), the convex sum \(\sum 2^{-s_i}\) is minimized when the \(s_i\)'s differ by at most one. This gives exactly \(L(n,q)\). \(\square\)

A convenient real-valued version follows from Jensen's inequality. With \(\gamma=q/n\),

\[
\boxed{\quad
\frac{F(G)}n
\le
\phi(\gamma):=\gamma\bigl(1-2^{-1/\gamma}\bigr).
\quad} \tag{4.4}
\]

## Corollary 4.2: exact result when \(\theta(G)=\alpha_0(G)\)

If \(\theta(G)=r\), then

\[
F(G)\le r-L(n,r). \tag{4.5}
\]

Moreover, this is sharp: equality is attained by the disjoint union of \(r-b\) copies of \(K_k\) and \(b\) copies of \(K_{k+1}\), where \(n=kr+b\).

In particular,

\[
\boxed{\quad
\frac{F(G)}n
\le a-a\,2^{-1/a}.
\quad} \tag{4.6}
\]

Every perfect graph satisfies \(\theta(G)=\alpha_0(G)\): indeed, \(\overline G\) is perfect and hence

\[
\chi(\overline G)=\omega(\overline G)=\alpha_0(G).
\]

Therefore Conjecture 2.9 holds for all perfect graphs and all \(a\in(0,1/2)\).

The exact normalized gap in (4.5) is as follows. Set

\[
k=\left\lfloor\frac1a\right\rfloor,
\qquad
\lambda=\frac1a-k.
\]

Then

\[
\frac{L(n,r)}n
=
a\left((1-\lambda)2^{-k}
+\lambda2^{-(k+1)}\right). \tag{4.7}
\]

When \(a=1/s\),

\[
\frac{L(n,r)}n=a\,2^{-s}=a\,2^{-1/a}. \tag{4.8}
\]

Thus the cluster graph consisting of copies of \(K_s\) also shows that no universal gap at \(a=1/s\) can exceed

\[
a\,2^{-1/a}.
\]

This illustrates that any general bound must be exponentially small in \(1/a\) in the small-\(a\) regime.

## 4.1 Clique-cover number close to \(r\)

The function \(\phi\) in (4.4) is strictly increasing and satisfies \(0<\phi'(\gamma)<1\). Indeed, writing \(c=\log2\),

\[
\phi'(\gamma)
=
1-e^{-c/\gamma}\left(1+\frac c\gamma\right),
\]

which lies in \((0,1)\).

Since

\[
\phi(a)=a-a2^{-1/a},
\]

if

\[
\frac{\theta(G)}n-a
\le \frac12a2^{-1/a},
\]

then

\[
\phi\!\left(\frac{\theta(G)}n\right)
\le
\phi(a)+\frac{\theta(G)}n-a
\le
a-\frac12a2^{-1/a}.
\]

Hence:

\[
\boxed{\quad
\theta(G)\le
\left(a+\frac12a2^{-1/a}\right)n
\ \Longrightarrow\
\frac{F(G)}n
\le
a-\frac12a2^{-1/a}.
\quad} \tag{4.9}
\]

Thus the perfect-graph argument is stable under a small linear clique-cover excess.

# 5. A second structural bound: induced bipartite subgraphs

Let

\[
b_2(G)
=
\max\{|A|+|B|:
A,B\text{ are disjoint independent sets in }G\}.
\]

Equivalently, \(b_2(G)\) is the maximum order of an induced bipartite subgraph of \(G\).

## Proposition 5.1

\[
\boxed{\quad
F(G)\le \frac12b_2(G),
\qquad
D(G)\ge r-\frac12b_2(G).
\quad} \tag{5.1}
\]

### Proof

For every \(W\), choose maximum independent sets \(I_W\subseteq W\) and \(I_{\overline W}\subseteq V\setminus W\). They are disjoint, and their union induces a bipartite graph with the displayed independent sets as its two parts. Therefore

\[
\alpha_0(G[W])+\alpha_0(G[V\setminus W])
\le b_2(G).
\]

Since \(W\) and \(V\setminus W\) have the same marginal distribution, taking expectations gives \(2F(G)\le b_2(G)\). \(\square\)

Since each side of an induced bipartite subgraph has size at most \(r\), one always has \(b_2(G)\le2r\). In particular, if

\[
b_2(G)\le(2a-\eta)n,
\]

then

\[
\frac{F(G)}n\le a-\frac{\eta}{2}. \tag{5.2}
\]

Thus only graphs possessing two almost-disjoint, almost-maximum independent sets can be extremal for the conjecture.

# 6. An exact replacement-set formulation

Fix a maximum independent set \(I\), and put \(O=V(G)\setminus I\). For an independent set \(S\subseteq O\), let

\[
N_I(S)=N_G(S)\cap I.
\]

The maximality of \(I\) implies the Hall-type inequality

\[
|N_I(S)|\ge |S| \tag{6.1}
\]

for every independent \(S\subseteq O\), since otherwise

\[
(I\setminus N_I(S))\cup S
\]

would be an independent set larger than \(I\).

For a fixed realization \(W\), once the \(O\)-part \(S\subseteq W\cap O\) of an independent set is chosen, all vertices of

\[
W\cap (I\setminus N_I(S))
\]

can be added. Consequently,

\[
\alpha_0(G[W])
=
\max_{\substack{S\subseteq W\cap O\\S\text{ independent}}}
\left(
|S|+|W\cap(I\setminus N_I(S))|
\right).
\]

Equivalently,

\[
\boxed{\quad
r-\alpha_0(G[W])
=
\min_{\substack{S\subseteq W\cap O\\S\text{ independent}}}
\left[
|N_I(S)|-|S|
+
|(I\setminus N_I(S))\setminus W|
\right].
\quad} \tag{6.2}
\]

Both terms are nonnegative by (6.1).

Formula (6.2) identifies the unresolved obstruction. To make the deficit small, \(W\cap O\) must contain an independent set \(S\) which is nearly Hall-tight,

\[
|N_I(S)|-|S|=o(n),
\]

and whose neighborhood \(N_I(S)\) tracks almost all deleted vertices of \(I\). For a union of cliques these replacements occur independently inside each component, producing the gap \(a2^{-1/a}\). In a general dense graph, controlling the number and geometry of these adaptive Hall-tight replacement sets appears to require an additional argument not supplied here.

# 7. Necessary properties of any counterexample sequence

Suppose, for a fixed \(a\in(0,1/2)\), there were graphs \(G_n\) with

\[
\alpha_0(G_n)=an,\qquad D(G_n)=o(n).
\]

The preceding inequalities force all of the following.

## 7.1 Diverging average degree

For any fixed \(L\) and any maximum independent set \(I_n\), Proposition 2.1 gives

\[
D(G_n)
\ge
2^{-(L+1)}
\bigl|\{v\in I_n:d(v)\le L\}\bigr|.
\]

Hence

\[
\bigl|\{v\in I_n:d(v)\le L\}\bigr|=o(n).
\]

It follows that the mean degree on every maximum independent set tends to infinity, and in particular

\[
\frac{e(G_n)}n\longrightarrow\infty. \tag{7.1}
\]

Thus no bounded-average-degree sequence can disprove the conjecture.

## 7.2 A linear complement chromatic gap

Let \(q_n=\theta(G_n)=\chi(\overline{G_n})\) and \(\gamma_n=q_n/n\). From (4.4),

\[
a-o(1)=\frac{F(G_n)}n\le\phi(\gamma_n).
\]

For each \(a\in(0,1/2)\), there is a unique \(\gamma_a\in(0,1)\) satisfying

\[
\gamma_a(1-2^{-1/\gamma_a})=a.
\]

Moreover, \(\gamma_a>a\), since \(\phi(a)<a\). Hence

\[
\liminf_{n\to\infty}\frac{\chi(\overline{G_n})}{n}
\ge\gamma_a>a. \tag{7.2}
\]

A counterexample must therefore be quantitatively far from the clique-partition-tight or perfect case.

## 7.3 Two almost-disjoint maximum independent sets

From Proposition 5.1,

\[
b_2(G_n)\ge2r_n-2D(G_n)=2an-o(n).
\]

Since \(b_2(G_n)\le2r_n\),

\[
b_2(G_n)=2an-o(n). \tag{7.3}
\]

## 7.4 Robustness in both halves of a random bipartition

Because

\[
r_n-\alpha_0(G_n[W])\ge0
\]

has expectation \(o(n)\), Markov's inequality gives

\[
\alpha_0(G_n[W])=r_n-o(n)
\]

with probability tending to one. The same holds simultaneously for \(V\setminus W\). Thus a random bipartition would, with high probability, contain an almost-maximum independent set on each side.

These conditions do not by themselves contradict one another, but they sharply delimit what a genuine counterexample would have to look like: it must be dense, highly imperfect, contain induced stars of unbounded order, and possess a very large family of almost-disjoint, adaptively replaceable near-maximum independent sets.

# 8. Conclusion and remaining gap

The general conjecture is not proved here. The established partial results are:

1. The graph-dependent bound
   \[
   \alpha_0(G)-\mathbb E\alpha_0(G[W])
   \ge\sum_{v\in I}2^{-|N[v]|}.
   \]

2. Conjecture 2.9 for all induced-\(K_{1,t}\)-free graphs, with
   \[
   \varepsilon_t(a)
   =
   a\,2^{-((t-1)/a-(t-2))}.
   \]

3. In particular, the full range for claw-free graphs and line graphs:
   \[
   \varepsilon_{\mathrm{clawfree}}(a)
   =
   a\,2^{-(2/a-1)}.
   \]

4. The full range for bounded-degree and bounded-average-degree classes.

5. An exact extremal result for graphs with
   \(\chi(\overline G)=\alpha_0(G)\), including perfect graphs; balanced disjoint unions of cliques are extremal in this class.

6. Structural necessary conditions for any sequence violating the conjecture.

The missing case consists of dense graphs with unbounded induced stars and a large gap between \(\chi(\overline G)\) and \(\omega(\overline G)\). Formula (6.2) reduces that case to controlling adaptive Hall-tight independent replacement sets, but no uniform positive lower bound for their random deficit is proved here.