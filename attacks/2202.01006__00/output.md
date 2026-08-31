```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The qualitative upper-bound gap remains open, but the high-girth auxiliary bound n^(4r) can be sharpened to (O(n log n))^r, n^(Theta(r)) is unavoidable for that template, and every q-dichromatic member of C3 has at least floor(q^2/2) vertices.",
  "would_publish": false,
  "caveats": "No smaller-scale C3 construction is produced, and application of the auxiliary estimate is conditional on Lemma 3 having the high-girth/high-chromatic role indicated by the catalog."
}
```

## 1. Formal interpretation and results

I use the definition from the supplied abstract: \(\mathcal C_3\) consists of finite simple oriented graphs \(D\) such that

1. \(D\) has no transitive tournament on three vertices, and
2. every induced directed cycle has length \(3\).

Write \(\vec\chi(D)\) for the dichromatic number. The catalog item is a research direction rather than a sharply quantified conjecture: neither the polynomial hidden in the exponent nor a target replacement bound is specified.

Two rigorous partial results follow.

### Theorem A: an intrinsic quadratic lower bound

If \(D\in\mathcal C_3\) has \(N\) vertices, then, for every positive integer \(t\),

\[
\vec\chi(D)\le
\left\lfloor\frac Nt\right\rfloor+\left\lceil\frac t2\right\rceil.
\tag{1}
\]

Consequently,

\[
\vec\chi(D)\le \left\lceil\sqrt{2N}\right\rceil.
\tag{2}
\]

More precisely, if \(\vec\chi(D)\ge q\), where \(q\ge2\), then

\[
N\ge \left\lfloor\frac{q^2}{2}\right\rfloor.
\tag{3}
\]

Thus any example of dichromatic number at least \(k+1\) in \(\mathcal C_3\) has at least

\[
\left\lfloor\frac{(k+1)^2}{2}\right\rfloor
\]

vertices.

### Theorem B: the high-girth auxiliary problem

Let \(h(q,g)\) be the minimum order of a simple graph \(H\) satisfying

\[
\chi(H)>q,\qquad \operatorname{girth}(H)>g.
\]

For \(q\ge3\) and \(g\ge3\),

\[
(q-1)^{\lfloor g/2\rfloor}
\le h(q,g)
\le
\left\lceil\bigl(64q\log(8q)\bigr)^g\right\rceil.
\tag{4}
\]

In particular,

\[
\log h(q,g)=\Theta(g\log q).
\tag{5}
\]

Therefore an auxiliary estimate of the form \(q^{4g}\) can be improved to

\[
(O(q\log q))^g=q^{(1+o(1))g},
\]

but the dependence \(q^{\Theta(g)}\) cannot be removed while retaining both the chromatic-number and girth requirements. If the source construction requires \(g=2^{\operatorname{poly}(n)}\), then this auxiliary graph alone necessarily has order

\[
n^{\Omega(2^{\operatorname{poly}(n)})}
\]

when \(q\) is comparable to \(n\). Thus a qualitative improvement to \(2^{\operatorname{poly}(n)}\) must reduce the required girth/state parameter or abandon this auxiliary-graph template.

---

## 2. Cycles in \(\mathcal C_3\) are exactly triangles

We first record the basic structural fact used below.

### Lemma 1

For \(D\in\mathcal C_3\) and \(X\subseteq V(D)\), the following are equivalent:

1. \(D[X]\) is acyclic;
2. \(D[X]\) contains no directed triangle;
3. the underlying graph of \(D[X]\) is triangle-free.

#### Proof

If \(D[X]\) contains a directed cycle, choose one of minimum length. Such a cycle is induced: a chord in either direction, together with one of the two directed portions of the cycle, produces a shorter directed cycle. By the defining property of \(\mathcal C_3\), the minimum cycle therefore has length \(3\).

Thus \(D[X]\) is cyclic if and only if it contains a directed triangle.

Every orientation of an underlying triangle is either a directed \(3\)-cycle or a transitive tournament. The latter is forbidden in \(\mathcal C_3\), so every underlying triangle of \(D\) is directed cyclically. This proves all three conditions equivalent. \(\square\)

Hence \(\vec\chi(D)\) is exactly the minimum number of parts into which the underlying graph can be partitioned so that every part induces a triangle-free graph.

---

## 3. Proof of the quadratic order bound

### Lemma 2

For every vertex \(v\) of a transitive-triangle-free oriented graph,

\[
N^+(v)\quad\text{and}\quad N^-(v)
\]

are stable sets in the underlying graph. Consequently the open neighborhood \(N(v)\) is bipartite.

#### Proof

If two out-neighbors \(x,y\) of \(v\) were adjacent, then \(v\), \(x\), and \(y\) would induce a transitive tournament with source \(v\), regardless of the direction of the edge \(xy\). The in-neighborhood case is symmetric. Therefore \(N(v)\) is bipartite with parts \(N^+(v)\) and \(N^-(v)\). \(\square\)

By Lemma 1, every open neighborhood in a member of \(\mathcal C_3\) induces an acyclic digraph.

### Proof of Theorem A

Fix \(t\ge1\). Repeatedly apply the following operation to the current induced subdigraph:

- if its underlying graph has a vertex \(v\) of degree at least \(t\), remove \(N(v)\) and give all vertices of \(N(v)\) one new color.

Each removed set is acyclic by Lemmas 1 and 2, and each operation removes at least \(t\) vertices. Hence at most

\[
\left\lfloor\frac Nt\right\rfloor
\]

colors are used in these operations.

When the process stops, the remaining underlying graph has maximum degree at most \(t-1\), so it has a proper coloring with at most \(t\) colors. Pair these proper color classes. The union of two stable sets is bipartite and hence triangle-free, so by Lemma 1 it is acyclic. The remainder therefore needs at most \(\lceil t/2\rceil\) dichromatic colors. This proves (1).

Taking \(t=\lceil\sqrt{2N}\rceil\), we have \(N/t\le t/2\), and hence

\[
\left\lfloor\frac Nt\right\rfloor+
\left\lceil\frac t2\right\rceil
\le
\left\lfloor\frac t2\right\rfloor+
\left\lceil\frac t2\right\rceil=t.
\]

This proves (2).

For the sharper inversion, first let \(q=2a\). Applying (1) with \(t=2a\), if \(N<2a^2\), then

\[
\vec\chi(D)
\le a+\left\lfloor\frac{N}{2a}\right\rfloor
\le a+(a-1)=q-1.
\]

Thus \(\vec\chi(D)\ge q\) implies \(N\ge2a^2=q^2/2\).

If \(q=2a+1\), then \(N<2a(a+1)\) would give

\[
\vec\chi(D)
\le a+\left\lfloor\frac{N}{2a}\right\rfloor
\le a+a=q-1.
\]

Therefore \(N\ge2a(a+1)=(q^2-1)/2\). These two cases give (3). \(\square\)

---

## 4. Sharpening the \(n^{4r}\) auxiliary estimate

The catalog attributes the large order partly to a Lemma 3 estimate \(n^{4r}\). The following addresses the standard form of that ingredient: constructing a graph of large chromatic number and large girth.

### Proposition 3: probabilistic upper bound

For integers \(q\ge2\) and \(g\ge3\), there exists a graph \(H\) such that

\[
\chi(H)>q,\qquad \operatorname{girth}(H)>g,
\]

and

\[
|V(H)|\le
\left\lceil\bigl(64q\log(8q)\bigr)^g\right\rceil.
\]

#### Proof

Put

\[
B=64q\log(8q),\qquad N=\lceil B^g\rceil,
\]

and consider \(G\sim G(N,p)\), where

\[
p=\frac14N^{-1+1/g}.
\]

Set \(d=Np=N^{1/g}/4\).

Let \(X\) be the number of cycles of length between \(3\) and \(g\). Then

\[
\mathbb E X
\le\sum_{i=3}^g (Np)^i
=\sum_{i=3}^g d^i.
\]

Since \(d\ge2\),

\[
\mathbb E X\le2d^g=\frac{2N}{4^g}\le\frac N{32}.
\]

Hence, by Markov's inequality,

\[
\Pr(X>N/4)\le\frac18.
\tag{6}
\]

Now let

\[
s=\left\lceil\frac{N}{2q}\right\rceil.
\]

The expected number \(Y\) of independent sets of size \(s\) satisfies

\[
\begin{aligned}
\mathbb E Y
&\le {N\choose s}(1-p)^{\binom s2}\\
&\le
\left(\frac{eN}{s}\right)^s
\exp\left(-p\binom s2\right).
\end{aligned}
\]

Since \(N/s\le2q\), we have

\[
\log(eN/s)\le\log(2eq)\le\log(8q).
\]

Also \(s-1\ge N/(4q)\), and therefore

\[
\frac{p(s-1)}2
\ge
\frac{N^{1/g}}{32q}
\ge2\log(8q).
\]

It follows that

\[
\mathbb E Y
\le
\exp\bigl(-s\log(8q)\bigr)<\frac18.
\tag{7}
\]

By (6) and (7), there is a realization of \(G\) with at most \(N/4\) cycles of length at most \(g\) and with no independent set of size \(s\).

Delete one vertex from each such short cycle. The resulting graph \(H\) has girth greater than \(g\) and at least \(3N/4\) vertices. Moreover,

\[
\alpha(H)\le\alpha(G)<s,
\]

so in fact \(\alpha(H)<N/(2q)\). Consequently,

\[
\chi(H)\ge\frac{|V(H)|}{\alpha(H)}
>
\frac{3N/4}{N/(2q)}
=\frac{3q}{2}>q.
\]

This proves the proposition. \(\square\)

---

## 5. A matching obstruction for the same template

### Proposition 4: Moore-type lower bound

If \(H\) satisfies

\[
\chi(H)>q,\qquad \operatorname{girth}(H)>g,
\]

where \(q\ge3\), then

\[
|V(H)|\ge(q-1)^{\lfloor g/2\rfloor}.
\]

#### Proof

Since \(\chi(H)>q\), \(H\) has a nonempty subgraph \(H_0\) of minimum degree at least \(q\). Otherwise one could successively delete vertices of degree at most \(q-1\), and the reverse deletion order would give a proper \(q\)-coloring.

Put \(r=\lfloor g/2\rfloor\) and expose a breadth-first-search tree in \(H_0\) to depth \(r\). Because \(H_0\) has no cycle of length at most \(g\), no two branches can meet within these first \(r\) levels, and there are no non-tree edges that reduce the branching count. The root has at least \(q\) children, and every subsequent non-leaf tree vertex has at least \(q-1\) new children. Therefore

\[
|V(H)|
\ge
1+q\sum_{i=0}^{r-1}(q-1)^i
\ge
(q-1)^r.
\]

This is the claimed bound. \(\square\)

Combining Propositions 3 and 4 proves (4) and (5). Thus the \(n^{4r}\) bound may be replaced at the auxiliary-graph level by

\[
(64n\log(8n))^r=n^{(1+o(1))r},
\]

while every such auxiliary graph requires at least approximately

\[
n^{r/2}
\]

vertices.

---

## 6. Consequences and remaining gap

1. **A genuine quantitative improvement.**  
   The exponent \(4r\) in the standard high-girth/high-chromatic lemma can be reduced to \((1+o(1))r\) as the chromatic parameter tends to infinity.

2. **No qualitative improvement from that lemma alone.**  
   The Moore bound shows that the dependence \(n^{\Theta(r)}\) is inherent. In particular, if the source proof needs an exponentially large girth parameter \(r\), then merely optimizing the random auxiliary graph cannot reduce the construction to \(2^{\operatorname{poly}(n)}\).

3. **An intrinsic lower bound for the desired examples.**  
   Independently of the source construction, a \((k+1)\)-dichromatic member of \(\mathcal C_3\) needs at least \(\lfloor (k+1)^2/2\rfloor\) vertices.

4. **What is not proved.**  
   I do not construct a member of \(\mathcal C_3\) smaller by a different asymptotic scale. Closing the catalogued gap requires a new mechanism that avoids the exponentially large girth/state parameter, or a substantially different recursion.

5. **Source-dependence caveat.**  
   The prompt does not reproduce the statement of Lemma 3 or the exact recurrence, and the catalog itself says the displayed tower was reconstructed. Thus the substitution into the paper's final numerical recurrence should be checked against the source TeX; the auxiliary propositions above are unconditional.