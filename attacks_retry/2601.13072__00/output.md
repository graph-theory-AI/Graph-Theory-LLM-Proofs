```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A degree–codegree counting inequality gives a polynomial-time algorithm in a near-uniform regime, while explicit affine-plane graphs show that the previous small-parameter approach leaves a genuine middle-degree core.",
  "would_publish": false,
  "caveats": "The general quasi-polynomial question remains open; novelty of the special-case criterion has not been checked."
}
```

## 1. Statement of the partial result

I do not obtain a quasi-polynomial algorithm for all diameter-\(2\) graphs. The main additional result is a tractable regime defined by degrees and common-neighbor counts.

Throughout, graphs are finite and simple. For distinct vertices put
\[
\operatorname{codeg}(u,v)=|N(u)\cap N(v)|.
\]
For a noncomplete graph \(G\) of diameter at most \(2\), define
\[
\delta=\delta(G),\qquad \Delta=\Delta(G),
\]
and
\[
\mu=\min_{\substack{u\ne v\\uv\notin E(G)}}\operatorname{codeg}(u,v),
\qquad
\nu=\max_{\substack{u\ne v\\uv\notin E(G)}}\operatorname{codeg}(u,v).
\]
The diameter assumption gives \(\mu\ge1\). Write
\[
r=\frac{\Delta}{\delta},\qquad s=\frac{\nu}{\mu}.
\]

### Partial theorem

Let \(0<\varepsilon\le1\). On the class of diameter-\(2\) graphs satisfying
\[
r^2s\le 2-\varepsilon,
\tag{1}
\]
\(3\)-colourability can be decided deterministically in time
\[
n^{O(1/\varepsilon)}.
\]

Consequently:

* for every fixed positive \(\varepsilon\), this class admits a polynomial-time algorithm;
* for every fixed \(a\ge0\), the condition
  \[
  r^2s\le 2-\frac1{(\log n)^a}
  \]
  gives a quasi-polynomial-time algorithm;
* in particular, for regular graphs, a fixed gap below \(2\) in the ratio of maximum to minimum nonedge codegree suffices.

The proof uses the all-pairs diameter condition, not just a radius-\(2\) centre.

I independently reprove the neighborhood-enumeration and domination facts used from the previous attempt. Its other algorithmic and hardness assertions are not needed.

---

## 2. The counting inequality

The key observation is that a sparse, nearly regular, \(3\)-colourable diameter-\(2\) graph must have substantial variation in its nonedge codegrees.

### Lemma 2.1

Suppose \(G\) is \(3\)-colourable and
\[
n>3\Delta,\qquad \delta>2r.
\]
Then
\[
r^2\frac{\nu}{\mu}
\ \ge\
2\left(1-\frac{3\Delta}{n}\right)
 \left(1-\frac{2r}{\delta}\right).
\tag{2}
\]

### Proof

Choose three nonempty independent colour classes \(A,B,C\), ordered so that
\[
a=|A|\ge b=|B|\ge c=|C|.
\]
If necessary, a colouring using fewer colours can be refined into three nonempty classes. Here \(n>3\Delta\) and \(\delta>2r\) ensure \(n\ge3\).

For \(x\notin A\), let \(d_A(x)=|N(x)\cap A|\). Counting ordered pairs of neighbors in \(A\),
\[
\begin{aligned}
\sum_{x\notin A}d_A(x)^2
&=\sum_{u\in A}d(u)
  +2\sum_{\{u,u'\}\subseteq A}\operatorname{codeg}(u,u')\\
&\le a\Delta+\nu a(a-1).
\end{aligned}
\]
On the other hand, Cauchy–Schwarz gives
\[
\sum_{x\notin A}d_A(x)^2
\ge
\frac{\left(\sum_{u\in A}d(u)\right)^2}{b+c}
\ge \frac{a^2\delta^2}{b+c}.
\]
It follows that
\[
\nu\ge \frac{\delta^2}{b+c}-\frac{\Delta}{a}.
\]
Since \((b+c)/a\le2\), this implies
\[
\nu\ge
\frac{\delta^2}{b+c}
\left(1-\frac{2r}{\delta}\right).
\tag{3}
\]

Next count length-\(2\) paths between \(A\) and \(B\). Every common neighbor of a vertex of \(A\) and a vertex of \(B\) lies in \(C\). Thus
\[
\mu\bigl(ab-e(A,B)\bigr)
\le
\sum_{x\in C}d_A(x)d_B(x).
\]
For \(x\in C\), we have \(d_A(x)+d_B(x)=d(x)\), so
\[
\sum_{x\in C}d_A(x)d_B(x)
\le \frac14\sum_{x\in C}d(x)^2
\le \frac{c\Delta^2}{4}.
\]
Also \(e(A,B)\le b\Delta\). Because \(a\ge n/3>\Delta\), we obtain
\[
\mu\le \frac{c\Delta^2}{4b(a-\Delta)}.
\tag{4}
\]

Combining (3) and (4),
\[
r^2\frac{\nu}{\mu}
\ge
\frac{4ab}{c(b+c)}
\left(1-\frac{\Delta}{a}\right)
\left(1-\frac{2r}{\delta}\right).
\]
All factors used here are positive. Finally,
\[
\frac{4ab}{c(b+c)}\ge2,
\qquad
1-\frac{\Delta}{a}\ge1-\frac{3\Delta}{n},
\]
where the first inequality follows from \(a\ge c\) and \(b\ge c\). This proves (2). ∎

### Corollary 2.2: a degree dichotomy

Suppose \(G\) is \(3\)-colourable and satisfies (1). Then
\[
\boxed{\quad
\delta<\frac{8r}{\varepsilon}
\quad\text{or}\quad
\delta\ge\frac{\varepsilon n}{12r}.
\quad}
\tag{5}
\]

#### Proof

Assume \(\delta\ge8r/\varepsilon\).

If \(n\le3\Delta\), then
\[
\delta=\frac{\Delta}{r}\ge\frac{n}{3r}
\ge\frac{\varepsilon n}{12r}.
\]

Otherwise Lemma 2.1 applies. Using \((1-x)(1-y)\ge1-x-y\), condition (1) yields
\[
\varepsilon
\le \frac{6\Delta}{n}+\frac{4r}{\delta}.
\]
Our assumption gives \(4r/\delta\le\varepsilon/2\), and hence
\[
\frac{\Delta}{n}\ge\frac{\varepsilon}{12}.
\]
Dividing by \(r\) proves the second alternative in (5). ∎

Thus, within the class (1), a \(3\)-colourable graph cannot occupy the difficult middle-degree range.

---

## 3. Turning the dichotomy into an exact algorithm

For completeness, the two extension algorithms needed here are elementary.

### Lemma 3.1: small degree

If \(v\) has eccentricity at most \(2\), then \(3\)-colourability can be decided in time
\[
O^*(2^{d(v)}).
\]

#### Proof

Fix the colour of \(v\) to be \(1\), and enumerate all assignments of colours \(2,3\) to \(N(v)\). Discard assignments improper on \(G[N(v)]\).

Every vertex outside \(N[v]\) has a neighbor in \(N(v)\), so deleting the colours of its already coloured neighbors leaves a list of size at most \(2\).

List colouring with lists of size at most \(2\) is a \(2\)-SAT problem: for each edge and each colour common to its endpoints’ lists, forbid the simultaneous choice of that colour. Singleton lists give unit constraints, and an empty list rejects the branch.

Every proper \(3\)-colouring occurs in one branch, up to a global permutation of colours. ∎

### Lemma 3.2: a small dominating set

Given a dominating set \(D\), \(3\)-colourability can be decided in time
\[
O^*(3^{|D|}).
\]

#### Proof

Enumerate the proper colourings of \(G[D]\). Each vertex outside \(D\) loses at least one colour because it has a neighbor in \(D\). The remaining extension problem again has lists of size at most \(2\). ∎

A dominating set of size at most
\[
\left\lceil\frac{n(\ln n+1)}{\delta+1}\right\rceil
\tag{6}
\]
can be found greedily. Indeed, if \(U\) is the currently undominated set, then
\[
\sum_{v\in V(G)}|N[v]\cap U|
=\sum_{u\in U}(d(u)+1)
\ge(\delta+1)|U|.
\]
Some closed neighborhood therefore covers at least a \((\delta+1)/n\) fraction of \(U\). Repeatedly choosing such a neighborhood proves (6).

### Proof of the partial theorem

Complete graphs are handled directly. Otherwise compute \(\delta,\Delta,\mu,\nu\), which takes polynomial time, and verify (1).

Notice that (1) implies
\[
r\le\sqrt{2-\varepsilon}<\sqrt2.
\]

1. **If \(\delta<8r/\varepsilon\):** apply Lemma 3.1 at a minimum-degree vertex. The running time is
   \[
   2^{O(1/\varepsilon)}n^{O(1)}.
   \]

2. **If \(\delta\ge8r/\varepsilon\) but \(\delta<\varepsilon n/(12r)\):** reject. Corollary 2.2 certifies that the graph is not \(3\)-colourable.

3. **Otherwise:** \(\delta\ge\varepsilon n/(12r)\). By (6), a dominating set of size
   \[
   O\!\left(\frac{\log n}{\varepsilon}\right)
   \]
   can be found in polynomial time. Lemma 3.2 then gives running time
   \[
   n^{O(1/\varepsilon)}.
   \]

These cases are exhaustive, and every rejection and acceptance is justified. ∎

---

## 4. The factor \(2\) is a real boundary for this degree argument

The degree dichotomy cannot be extended to equality \(s=2\), even for regular graphs. The following family demonstrates this; it does **not** demonstrate computational hardness.

Let \(q\) be a prime power, and let \(\mathcal P\) be the one-dimensional subspaces of \(\mathbb F_q^4\). Fix a nondegenerate alternating bilinear form, for example
\[
B(x,y)=x_1y_2-x_2y_1+x_3y_4-x_4y_3.
\]
Write \(p\perp p'\) when \(B(x,x')=0\) for representatives of the projective points.

The relevant counts are
\[
h=|\mathcal P|=q^3+q^2+q+1,
\]
\[
d_0=|p^\perp\cap\mathcal P|=q^2+q+1,
\]
and, for distinct \(p,p'\),
\[
|p^\perp\cap(p')^\perp\cap\mathcal P|=q+1=:\lambda.
\]
The last count follows because the intersection is a two-dimensional vector subspace.

Take three copies of \(\mathcal P\). Join vertices in different copies exactly when their underlying projective points are orthogonal.

This graph is \(3\)-colourable by its three copies and is \(2d_0\)-regular on \(3h\) vertices. Because the form is alternating, \(p\perp p\); corresponding points in different copies are therefore adjacent.

Its nonedges have exactly two types:

* distinct points in the same copy have \(2\lambda\) common neighbors;
* nonorthogonal points in different copies have \(\lambda\) common neighbors.

Thus the graph has diameter \(2\) and
\[
r=1,\qquad \mu=\lambda,\qquad \nu=2\lambda,\qquad s=2.
\]
But
\[
\delta=2(q^2+q+1)\longrightarrow\infty,
\qquad
\frac{\delta}{n}\longrightarrow0.
\]

Hence at ratio \(2\), regular \(3\)-colourable diameter-\(2\) graphs can have genuinely intermediate degree.

---

## 5. An explicit family realizing the previous attempt’s unresolved core

The previous attempt left open whether its troublesome combination of large local parameters actually occurs after forced-equality preprocessing. It does.

### Construction

Let \(q\ge3\) be a prime power. In the affine plane \(\operatorname{AG}(2,q)\), let

* \(A\) be the set of \(q^2\) points;
* \(B\) and \(C\) be two copies of its \(q(q+1)\) lines.

Define \(F_q\) as follows:

* a point is adjacent to each copy of every line containing it;
* \(\ell^B\) is adjacent to \(m^C\) exactly when \(\ell,m\) are distinct parallel lines;
* there are no other edges.

The three sets \(A,B,C\) are independent, so \(F_q\) is \(3\)-colourable.

A triangle would have to consist of a point and two line copies. But adjacent line copies represent disjoint lines, which cannot contain a common point. Thus \(F_q\) is triangle-free.

### Diameter and codegrees

The following table lists all nonedge types, including symmetric cases obtained by interchanging \(B,C\).

\[
\begin{array}{c|c}
\text{nonadjacent pair}&\text{number of common neighbors}\\ \hline
p,p'\in A,\ p\ne p'&2\\
p,\ell^B,\ p\notin\ell&1\\
\ell^B,m^B,\ \ell\ne m\text{ parallel}&q-2\\
\ell^B,m^B,\ \ell,m\text{ nonparallel}&1\\
\ell^B,\ell^C&q\\
\ell^B,m^C,\ \ell,m\text{ nonparallel}&1
\end{array}
\]

For example:

* two points share the two copies of their unique joining line;
* for a point \(p\notin\ell\), the copy in \(C\) of the line through \(p\) parallel to \(\ell\) is their unique common neighbor;
* two distinct parallel lines in \(B\) share the \(q-2\) other lines of that parallel class in \(C\).

Every table entry is positive because \(q\ge3\). Consequently,
\[
\operatorname{diam}(F_q)=2,\qquad \mu=1,\qquad \nu=q.
\]

The order and degrees are
\[
n=3q^2+2q,
\]
\[
d(p)=2q+2 \quad(p\in A),\qquad
d(\ell^B)=d(\ell^C)=2q-1.
\]
Thus
\[
\delta=\Theta(\sqrt n),\qquad
\Delta=\Theta(\sqrt n),\qquad
r\longrightarrow1,
\]
but the codegree ratio is \(s=q\). This is well outside the tractable regime above.

### All the earlier small parameters are large

**Domination.** Since a closed neighborhood has at most \(\Delta+1\) vertices,
\[
\gamma(F_q)
\ge \frac{3q^2+2q}{2q+3}
=\Omega(q)=\Omega(\sqrt n).
\tag{7}
\]

**Neighborhood components.** Triangle-freeness makes every neighborhood independent. Hence, for every vertex \(v\),
\[
\kappa_v=d(v)\ge2q-1.
\tag{8}
\]

**External types.** The graph has no false twins:

* distinct points lie on different sets of lines;
* distinct underlying lines have different sets of incident points;
* the two copies of one line have different neighbors among line vertices;
* point vertices and line vertices have different neighborhood intersections with \(A\).

For \(u\in N(v)\), triangle-freeness gives
\[
N(u)=\{v\}\cup\bigl(N(u)\cap(V\setminus N[v])\bigr).
\]
Therefore distinct neighbors of \(v\) have distinct external neighborhoods. The external-type parameter from the previous attempt satisfies
\[
\rho_v=d(v)\ge2q-1.
\tag{9}
\]

**CSP treewidth.** Because \(N(v)\) is independent, every neighborhood component is a singleton. Replacing those singleton vertices by their Boolean orientation variables leaves the primal graph isomorphic to
\[
F_q-v.
\]
Its minimum degree is at least \(2q-2\). Since every graph of treewidth \(t\) has a vertex of degree at most \(t\),
\[
\operatorname{tw}(P_v)\ge2q-2
\tag{10}
\]
for every \(v\).

**Forced-equality preprocessing.** The edge-common-neighbor contraction from the previous attempt does nothing: a triangle-free graph has no common neighbor of an edge.

Thus this is an explicit infinite family of \(3\)-colourable, triangle-free, twin-free, diameter-\(2\) graphs for which
\[
\gamma(F_q),\quad \min_v\kappa_v,\quad \min_v\rho_v,\quad
\min_v\operatorname{tw}(P_v)
\]
are all \(\Omega(\sqrt n)\), and the forced-equality quotient is unchanged.

This does not establish a running-time lower bound. It establishes that none of those parameters is universally polylogarithmic, even simultaneously after the indicated preprocessing.

---

## 6. What remains unresolved

The counting argument gives a recognizable polynomial-time class and a quasi-polynomial extension when the gap below \(2\) is inverse-polylogarithmic. It does not improve the worst-case bound supplied in the question.

The remaining issue is not merely whether the earlier middle-degree core exists: the affine-plane family shows that it does. A general algorithm must exploit more than:

* small degree or high minimum degree;
* few neighborhood components or external types;
* small treewidth of the local orientation CSP;
* a polylogarithmic dominating set;
* the stated forced-equality preprocessing.

In particular, the argument above provides no general way to exploit large variation in common-neighbor counts. No universal quasi-polynomial algorithm, explicit counterexample to its existence, or applicable hardness classification is obtained here.