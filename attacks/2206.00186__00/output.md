```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The global guarantee is known to improve asymptotically to density sqrt(2)-1, and the argument below proves the 0.9 target in several structural regimes, but gives neither a proof nor a counterexample in general.",
  "would_publish": false,
  "caveats": "The 0.9 target remains open; the structural corollaries use the quoted Hendrey–Norin–Steiner–Turcotte theorem and Gallai's classical critical-graph lemma."
}
```

# 1. Formal statement

For a graph \(G\), let
\[
m_t(G)=\max\{e(H): |V(H)|=t,\ H\preccurlyeq G\},
\]
where \(\preccurlyeq\) denotes the minor relation. Then
\[
g(t)=\min_{\chi(G)\ge t}m_t(G).
\]

The concrete \(0.9\)-density target is

\[
\tag{\(\mathcal P_{0.9}\)}
g(t)\ge \frac9{10}\binom t2.
\]

The weaker informal assertion that the asymptotic density \(1/4\) can be significantly improved is already resolved. The specific assertion \(\mathcal P_{0.9}\) is not.

# 2. The established global improvement

Every graph \(G\) with \(\chi(G)\ge t\) contains a \(t\)-critical subgraph \(F\): choose a subgraph minimal subject to having chromatic number at least \(t\). Then \(\chi(F)=t\), and
\[
\delta(F)\ge t-1.
\]
Indeed, \(F-v\) is \((t-1)\)-colorable for every \(v\), and a vertex of degree at most \(t-2\) could be assigned a missing color.

The theorem of Hendrey, Norin, Steiner, and Turcotte quoted in the prompt says that every graph of average degree at least \(t-1\) has a \(t\)-vertex minor with at least
\[
\left(\sqrt2-1-o(1)\right)\binom t2
\]
edges. Applying it to \(F\) gives
\[
\boxed{g(t)\ge \left(\sqrt2-1-o(1)\right)\binom t2.}
\]
Thus the guaranteed density is at least approximately \(0.414213\), rather than \(1/4\).

This does not approach \(0.9\).

# 3. Why the \(3/4\) average-degree upper bound is not a counterexample

There is a simple extremal construction showing that average degree alone cannot force density exceeding \(3/4+o(1)\).

Let
\[
a=\left\lceil\frac t2\right\rceil
\]
and choose \(b\ge t\) sufficiently large that
\[
\frac{2ab}{a+b}\ge t-1.
\]
For example, it is enough to take
\[
b\ge \frac{a(t-1)}{2a-t+1}.
\]
Consider \(K_{a,b}\), with bipartition \(A,B\).

In a minor model in \(K_{a,b}\), every branch set is one of:

1. a singleton contained in \(A\);
2. a singleton contained in \(B\);
3. a mixed branch set meeting both sides.

A mixed branch set is adjacent to every other branch set. If there are \(p\) \(A\)-singletons, \(q\) \(B\)-singletons and \(r\) mixed branch sets, then
\[
p+r\le a,\qquad p+q+r=t,
\]
and hence \(q\ge t-a\). The only necessarily missing edges are between two \(A\)-singletons or two \(B\)-singletons. Therefore
\[
e(H)\le \binom t2-\binom p2-\binom q2
   \le \binom t2-\binom{t-a}{2}.
\]
This bound is attained when \(b\ge t\): take \(a\) mixed branch sets and \(t-a\) additional \(B\)-singletons. Consequently,
\[
m_t(K_{a,b})
 =\binom t2-\binom{\lfloor t/2\rfloor}{2}
 =\left(\frac34+o(1)\right)\binom t2.
\]

However,
\[
\chi(K_{a,b})=2.
\]
Thus this is an upper bound for the average-degree analogue, not for \(g(t)\). Any proof of \(\mathcal P_{0.9}\) must use genuinely chromatic or critical-graph structure beyond \(\delta(F)\ge t-1\).

# 4. An exact elementary small-core result

The following gives the \(0.9\) target whenever a \(t\)-critical core has order close enough to \(t\).

## Proposition 4.1

Let \(G\) contain a \(t\)-critical subgraph \(F\) on \(n\) vertices. Then \(G\) has a \(t\)-vertex subgraph, hence a \(t\)-vertex minor, with at least
\[
\binom t2\frac{t-1}{n-1}
\]
edges.

### Proof

Since \(\delta(F)\ge t-1\),
\[
e(F)\ge \frac{n(t-1)}2.
\]
Choose a uniformly random \(t\)-element subset \(X\subseteq V(F)\). Then
\[
\mathbb E[e(F[X])]
 =e(F)\frac{\binom t2}{\binom n2}
 \ge \binom t2\frac{t-1}{n-1}.
\]
Some choice of \(X\) attains at least this expectation. ∎

Hence \(\mathcal P_{0.9}\) holds whenever
\[
\frac{t-1}{n-1}\ge\frac9{10},
\]
or equivalently
\[
\boxed{n\le 1+\frac{10}{9}(t-1)=\frac{10t-1}{9}.}
\]

This is finite and exact, but it only handles critical cores of order at most approximately \(1.111t\).

# 5. Join decompositions and a stronger small-core bound

Write \(G_1\vee\cdots\vee G_r\) for the join of graphs: all edges between different factors are present.

## Join lemma

Suppose \(G_i\) has a \(k_i\)-vertex minor \(H_i\), and put \(t=\sum_i k_i\). Then
\[
G_1\vee\cdots\vee G_r
\]
has the \(t\)-vertex minor \(H_1\vee\cdots\vee H_r\). In particular, the number of missing edges is exactly the sum of the numbers missing inside the \(H_i\).

Let
\[
q=\sqrt2-1,\qquad \beta=1-q=2-\sqrt2.
\]
Using the established \(q-o(1)\) lower bound separately in the join factors gives the following. If their chromatic numbers are \(k_1,\dots,k_r\), with \(\sum k_i=t\), then the join has a \(t\)-vertex minor whose number \(D\) of missing edges satisfies
\[
\tag{1}
D\le \beta\sum_i\binom{k_i}{2}+o(t^2).
\]
The aggregation of the error terms is legitimate: for any fixed \(\eta>0\), all factors with \(k_i\) sufficiently large have missing density at most \(\beta+\eta\), while factors of bounded chromatic number contribute only \(O_\eta(t)\) missing edges in total.

Consequently, the \(0.9\) target follows whenever
\[
\frac{\sum_i\binom{k_i}{2}}{\binom t2}
<
\frac{1}{10(2-\sqrt2)}
=
\frac{2+\sqrt2}{20}
\approx 0.1707107
\]
with a fixed positive margin.

For example, six join factors whose chromatic numbers are each \((1/6+o(1))t\) suffice, since
\[
\frac{2-\sqrt2}{6}\approx 0.097631<0.1.
\]

## Corollary for critical cores of order at most \(1.413t\)

I use the classical Gallai critical-graph lemma:

> If \(Q\) is \(k\)-critical and \(\overline Q\) is connected, then
> \[
> |V(Q)|\ge 2k-1.
> \]

Let \(F\) be \(t\)-critical of order
\[
|V(F)|=t+s.
\]
Let \(F_1,\dots,F_r\) be the factors corresponding to the connected components of \(\overline F\). Then
\[
F=F_1\vee\cdots\vee F_r.
\]
Put
\[
k_i=\chi(F_i),\qquad n_i=|V(F_i)|.
\]
Criticality of \(F\) implies criticality of every \(F_i\), and
\[
\sum_i k_i=t,\qquad \sum_i(n_i-k_i)=s.
\]
Gallai's lemma gives
\[
n_i-k_i\ge k_i-1.
\]
Therefore
\[
\sum_i(k_i-1)\le s.
\]
Writing \(y_i=k_i-1\), we obtain
\[
\sum_i\binom{k_i}{2}
 =\frac12\sum_i y_i(y_i+1)
 \le \frac12\left(\left(\sum_i y_i\right)^2+\sum_i y_i\right)
 \le \binom{s+1}{2}.
\]
Substitution into (1) yields
\[
\boxed{
\binom t2-m_t(F)
\le
(2-\sqrt2)\binom{s+1}{2}+o(t^2).
}
\]

Define
\[
c_0=\sqrt{\frac{1}{10(2-\sqrt2)}}
    =\sqrt{\frac{2+\sqrt2}{20}}
    \approx 0.41317.
\]
It follows that, for every fixed \(\varepsilon>0\), the \(0.9\) target holds for all sufficiently large \(t\) whenever \(G\) contains a \(t\)-critical subgraph on at most
\[
\boxed{(1+c_0-\varepsilon)t\approx(1.41317-\varepsilon)t}
\]
vertices.

Thus any asymptotic counterexample to \(\mathcal P_{0.9}\) must have every \(t\)-critical core of order at least approximately \(1.41317t\). This improves the elementary \(1.111t\) threshold, but uses both the dense-minor theorem and Gallai's lemma.

# 6. An exact result when \(\alpha(G)\le 2\)

The complement formulation gives a somewhat stronger elementary bound in the class motivating the source paper.

## Proposition 6.1

Let \(F\) satisfy
\[
\alpha(F)\le2,\qquad \chi(F)=t,\qquad |V(F)|=t+s.
\]
Then \(F\) has a \(t\)-vertex induced subgraph with at most
\[
\left\lfloor\frac{s^2}{4}\right\rfloor
\]
missing edges. Equivalently,
\[
\boxed{
m_t(F)\ge \binom t2-\left\lfloor\frac{s^2}{4}\right\rfloor.
}
\]

### Proof

Let \(J=\overline F\). Since \(\alpha(F)\le2\), the graph \(J\) is triangle-free.

A proper coloring of \(F\) consists of singleton color classes and pairs that are edges of \(J\). Hence
\[
\chi(F)=|V(F)|-\nu(J),
\]
where \(\nu(J)\) is the matching number. Thus
\[
\nu(J)=s.
\]

Let
\[
M=\{x_i y_i:1\le i\le s\}
\]
be a maximum matching of \(J\), and let \(U\) be the unmatched vertices. Then
\[
|U|=|V(F)|-2s=t-s.
\]
The set \(U\) is independent in \(J\), since otherwise \(M\) would not be maximal.

For every matching edge \(x_i y_i\), at least one endpoint has no neighbor in \(U\). Otherwise, suppose
\[
x_i u,\ y_i v\in E(J),\qquad u,v\in U.
\]
If \(u=v\), then \(u,x_i,y_i\) form a triangle in \(J\). If \(u\ne v\), replacing \(x_i y_i\) by \(ux_i\) and \(y_iv\) augments \(M\). Both are impossible.

Choose from each \(x_i y_i\) an endpoint \(c_i\) having no neighbor in \(U\), and put
\[
C=\{c_1,\dots,c_s\},\qquad X=U\cup C.
\]
Then \(|X|=t\). Every edge of \(J[X]\) lies inside \(C\). Since \(J[C]\) is triangle-free, Mantel's theorem gives
\[
e(J[X])=e(J[C])\le\left\lfloor\frac{s^2}{4}\right\rfloor.
\]
These are precisely the missing edges of \(F[X]\). ∎

In particular, \(\mathcal P_{0.9}\) holds whenever
\[
\frac{s^2}{4}\le\frac1{10}\binom t2,
\]
and hence whenever
\[
\boxed{s^2\le\frac{t(t-1)}5.}
\]
Asymptotically this covers
\[
|V(F)|\le\left(1+\frac1{\sqrt5}-o(1)\right)t
 \approx1.44721t.
\]

If \(\overline F\) is bipartite, the conclusion is much stronger: by matching-cover duality, \(J\) has an independent set of size
\[
|V(F)|-\nu(J)=t,
\]
so \(F\) actually contains \(K_t\) as a subgraph.

## Using the \(0.98688\) source theorem near \(2t\)

A minor on \(h\le t\) vertices can always be padded to one on exactly \(t\) vertices without losing edges: add unused vertices as singleton branch sets, and if necessary split a connected branch set using a leaf of a spanning tree.

The Norin–Seymour theorem quoted in the prompt gives, for an \(n\)-vertex graph with \(\alpha\le2\), an
\[
h=\left\lceil\frac n2\right\rceil
\]
vertex minor with at least
\[
0.98688\binom h2-o(n^2)
\]
edges. If \(\chi(F)=t\), then \(n\le2t\), so this minor can be padded to \(t\) vertices. If \(n/t\to x\), its resulting density is at least
\[
0.98688\,\frac{x^2}{4}-o(1).
\]
This exceeds \(0.9\) when
\[
x>2\sqrt{\frac{0.9}{0.98688}}\approx1.90994.
\]

Thus, within the class \(\alpha\le2\), the arguments above establish the \(0.9\) target asymptotically in the two regimes
\[
\frac nt\le1.44721-o(1)
\qquad\text{or}\qquad
\frac nt\ge1.90994+\Omega(1).
\]
They leave a substantial middle interval.

# 7. Remaining gap

The general \(0.9\) assertion is not proved. In particular, the arguments give no adequate control over a dominant, complement-connected \(t\)-critical factor with order at least \(2t-1\), nor over large critical cores without special independence-number structure.

The complete-bipartite construction rules out obtaining \(0.9\) from average degree alone, but has chromatic number two and therefore is not a counterexample to the chromatic formulation. No graph with \(\chi(G)\ge t\) and all \(t\)-vertex minors below density \(0.9\) is produced here.