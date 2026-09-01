```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "After replacing the literal minimum by an infimum, I determine the threshold for a broad class including all bidirected graphs, give general bounds, and prove that every oriented forest has threshold zero.",
  "would_publish": false,
  "caveats": "The general oriented cyclic case remains open; the literal minimum can fail to exist, and antiparallel arcs are assumed allowed."
}
```

## 1. Formulation and a necessary correction

Write \(\mathcal P_H(\varepsilon)\) for the assertion that there is a constant \(c\) such that every loopless digraph \(D\), with no repeated arcs, satisfying
\[
\chi(D)\ge c
\qquad\text{and}\qquad
\delta^+(D)\ge \varepsilon |V(D)|
\]
contains \(H\) as a not necessarily induced subdigraph. Here \(\chi(D)\) is the chromatic number of the underlying simple graph, and antiparallel pairs of arcs are allowed.

The definition consistent with the context of the source paper is
\[
\varepsilon_H:=\inf\{\varepsilon\in[0,1]:\mathcal P_H(\varepsilon)\}.
\tag{1}
\]
Indeed, the interpretation “\(\varepsilon_H=0\)” as forcing \(H\) for every fixed positive minimum-outdegree density only makes sense with an infimum.

The word “minimum” in the extracted statement cannot always be literal: in Section 7 below I give a fixed \(H\) for which
\[
\{\varepsilon:\mathcal P_H(\varepsilon)\}=(1/2,1],
\]
so that the infimum exists but no minimum does.

---

## 2. An exact class: bidirected graphs

For a simple graph \(F\), let \(\overleftrightarrow F\) be the digraph obtained by replacing every edge \(xy\in E(F)\) with both arcs \(xy\) and \(yx\).

### Theorem 1

Let \(F\) be a fixed simple graph with at least one edge, and let \(r=\chi(F)\). Then
\[
\boxed{\displaystyle
\varepsilon_{\overleftrightarrow F}
=
1-\frac{1}{2(r-1)}.}
\tag{2}
\]

Adding isolated vertices to \(F\) does not affect the value.

### Proof: upper bound

Given a digraph \(D\), define its **digon graph** \(B(D)\) on \(V(D)\) by
\[
xy\in E(B(D))
\quad\Longleftrightarrow\quad
xy,yx\in A(D).
\]

If \(D\) contains no \(\overleftrightarrow F\), then \(B(D)\) is \(F\)-free. For every unordered pair \(\{x,y\}\), there is at most one arc unless \(xy\in E(B(D))\). Consequently,
\[
|A(D)|\le \binom n2+e(B(D))
          \le \binom n2+\operatorname{ex}(n,F),
\tag{3}
\]
where \(n=|V(D)|\).

Also,
\[
n\delta^+(D)\le \sum_{v\in V(D)}d^+(v)=|A(D)|.
\tag{4}
\]
By the Erdős–Stone theorem,
\[
\operatorname{ex}(n,F)
=
\left(1-\frac1{r-1}+o(1)\right)\frac{n^2}{2}.
\tag{5}
\]
This includes the bipartite case \(r=2\), where \(\operatorname{ex}(n,F)=o(n^2)\).

Combining (3)–(5), every \(\overleftrightarrow F\)-free \(D\) satisfies
\[
\frac{\delta^+(D)}n
\le
1-\frac{1}{2(r-1)}+o(1).
\]
Thus, for every \(\eta>0\), all sufficiently large digraphs with
\[
\delta^+(D)\ge
\left(1-\frac{1}{2(r-1)}+\eta\right)n
\]
contain \(\overleftrightarrow F\). Since \(\chi(D)\le n\), choosing \(c\) sufficiently large gives
\[
\varepsilon_{\overleftrightarrow F}
\le 1-\frac{1}{2(r-1)}.
\]

### Proof: lower bound

Put \(q=r-1\). Let \(s\) be odd and \(n=qs\). Partition \(V(D)\) into \(q\) sets
\[
V_1,\dots,V_q,\qquad |V_i|=s.
\]

- Between distinct parts, put both arcs on every pair.
- Inside each part, put a regular tournament.

Then \(B(D)\) is the complete \(q\)-partite graph with equal parts, so it contains no \(F\), because \(\chi(F)=q+1\). Hence \(D\) contains no \(\overleftrightarrow F\).

The underlying graph of \(D\) is complete, so
\[
\chi(D)=n.
\]
Every vertex has
\[
d^+(v)
=(q-1)s+\frac{s-1}{2}
=
\left(1-\frac1{2q}\right)n-\frac12.
\tag{6}
\]
Therefore, for every
\[
\varepsilon<1-\frac1{2q},
\]
taking \(s\) sufficiently large gives arbitrarily high-chromatic \(\overleftrightarrow F\)-free digraphs with \(\delta^+(D)\ge\varepsilon n\). This proves the reverse inequality and hence (2). \(\square\)

---

## 3. A general chromatic sandwich

For a fixed digraph \(H\), define two simple graphs on \(V(H)\):

- \(U(H)\), the underlying graph, where \(xy\in E(U(H))\) if at least one of \(xy,yx\) is an arc of \(H\);
- \(B(H)\), the digon graph, where \(xy\in E(B(H))\) if both \(xy\) and \(yx\) are arcs of \(H\).

Define
\[
\tau(1):=0,\qquad
\tau(r):=1-\frac1{2(r-1)}\quad(r\ge2).
\]

We have subdigraph inclusions
\[
\overleftrightarrow{B(H)}
\subseteq H
\subseteq
\overleftrightarrow{U(H)}.
\tag{7}
\]
Thresholds are monotone under subdigraph inclusion: if \(J\subseteq K\), then
\[
\varepsilon_J\le \varepsilon_K.
\]
Applying Theorem 1 to (7) gives:

### Corollary 2

For every fixed digraph \(H\),
\[
\boxed{\displaystyle
\tau\bigl(\chi(B(H))\bigr)
\le
\varepsilon_H
\le
\tau\bigl(\chi(U(H))\bigr).}
\tag{8}
\]

In particular, if
\[
\chi(B(H))=\chi(U(H))=r,
\]
then
\[
\boxed{\displaystyle
\varepsilon_H=1-\frac1{2(r-1)}.}
\tag{9}
\]

Concrete consequences include:

1. If \(H\) has at least one digon and \(U(H)\) is bipartite, then
   \[
   \varepsilon_H=\frac12.
   \]
2. For the complete bidirected graph,
   \[
   \varepsilon_{\overleftrightarrow{K_r}}
   =
   1-\frac1{2(r-1)}.
   \]
3. More generally, adding one-way arcs to a bidirected subgraph does not change the threshold whenever those one-way arcs do not increase the chromatic number of the underlying graph beyond that of the digon graph.

The upper bound in (8) has a direct interpretation: above the indicated density, the digon graph \(B(D)\) is dense enough to contain \(U(H)\), giving a completely bidirected copy of \(U(H)\), which certainly contains \(H\).

---

## 4. Two further general bounds

### 4.1 An arc-count upper bound

Let \(m=|A(H)|\ge1\). Then
\[
\boxed{\displaystyle
\varepsilon_H\le 1-\frac1m.}
\tag{10}
\]

For \(m\ge2\), this bound actually forces \(H\) at equality, for sufficiently large \(n\).

Indeed, suppose
\[
\delta^+(D)\ge \left(1-\frac1m\right)n.
\]
Choose a uniformly random injection
\[
\phi:V(H)\longrightarrow V(D).
\]
For each fixed arc \(uv\in A(H)\), the ordered pair
\((\phi(u),\phi(v))\) is uniform among the \(n(n-1)\) ordered pairs of distinct vertices. Since
\[
|A(D)|\ge n\delta^+(D),
\]
the probability that this arc is missing is at most
\[
1-\frac{|A(D)|}{n(n-1)}
\le
1-\frac{(m-1)n}{m(n-1)}.
\]
Thus the expected number of missing required arcs is at most
\[
m-\frac{(m-1)n}{n-1}
=
\frac{n-m}{n-1}<1
\]
when \(n>m\). Hence some injection misses no required arc and gives a copy of \(H\).

For \(m=1\), high chromatic number already guarantees an arc, so \(\varepsilon_H=0\).

Combining (8) and (10),
\[
\varepsilon_H
\le
\min\left\{
\tau(\chi(U(H))),
\,1-\frac1{|A(H)|}
\right\}.
\tag{11}
\]

### 4.2 A finite-template lower bound

Call a map \(f:V(H)\to V(Q)\) an **acyclic \(Q\)-model** if:

1. whenever \(uv\in A(H)\) and \(f(u)\ne f(v)\), the arc \(f(u)f(v)\) belongs to \(Q\);
2. each subdigraph \(H[f^{-1}(x)]\) is acyclic.

If \(H\) has no acyclic \(Q\)-model, then
\[
\boxed{\displaystyle
\varepsilon_H\ge \frac{\delta^+(Q)}{|V(Q)|}.}
\tag{12}
\]

To see this, replace every vertex of \(Q\) by a transitive tournament of order \(s\), and replace every arc \(xy\in A(Q)\) by all arcs from the \(x\)-class to the \(y\)-class. Each class is a clique in the underlying graph, so the resulting digraphs have chromatic number at least \(s\). Their minimum out-degree is exactly
\[
s\delta^+(Q),
\]
while any copy of \(H\) would induce an acyclic \(Q\)-model.

As one consequence, let \(\vec\chi(H)\) be the dichromatic number of \(H\), i.e. the minimum number of acyclic vertex classes. Taking
\[
Q=\overleftrightarrow{K_{\vec\chi(H)-1}}
\]
gives, for \(\vec\chi(H)\ge2\),
\[
\varepsilon_H\ge
1-\frac1{\vec\chi(H)-1}.
\tag{13}
\]
For \(\vec\chi(H)=2\), this is the trivial lower bound \(0\), but for large dichromatic number it is nontrivial.

---

## 5. Every oriented forest has threshold zero

Here “oriented forest” means that the underlying graph is a forest and no edge is a digon.

### Theorem 3

If \(H\) is an oriented forest on \(h\) vertices, then
\[
\boxed{\varepsilon_H=0.}
\tag{14}
\]
In fact, every digraph \(D\) with
\[
\chi(D)\ge h^2
\]
contains \(H\), with no minimum-outdegree assumption.

### Proof

It suffices first to prove this for an oriented tree \(T\) on \(h\) vertices.

We use the following elementary observation. If \(S\subseteq V(D)\) and every \(v\in S\) has \(d_D^+(v)<h\), then for every \(X\subseteq S\),
\[
e(U(D[X]))
\le |A(D[X])|
\le (h-1)|X|.
\]
Thus \(U(D[S])\) is \((2h-2)\)-degenerate and
\[
\chi(D[S])\le 2h-1.
\tag{15}
\]
The same holds when “out-degree” is replaced by “in-degree”.

We induct on \(h\). The case \(h=1\) is immediate. Choose a leaf \(x\) of \(T\), with neighbour \(y\), and let \(T'=T-x\).

Suppose first that \(y\to x\) is the arc of \(T\). Let
\[
S=\{v:d_D^+(v)<h\},\qquad R=V(D)\setminus S.
\]
By (15),
\[
\chi(D[S])\le2h-1.
\]
Therefore
\[
\chi(D[R])
\ge h^2-(2h-1)
=(h-1)^2.
\]
By induction, \(D[R]\) contains \(T'\). The image of \(y\) lies in \(R\), so it has at least \(h\) out-neighbours in \(D\). At most \(h-2\) of these are other vertices already used by the copy of \(T'\), so there is an unused out-neighbour to serve as \(x\).

If the leaf arc is \(x\to y\), use in-degree instead. This completes the induction.

Finally, if \(H\) is a disconnected oriented forest, connect its components by arbitrarily oriented additional edges to obtain an oriented tree \(T\) on the same vertex set. Every copy of \(T\) contains \(H\) as a subdigraph. \(\square\)

As a small corollary, every fixed digraph with at most two arcs has threshold either:

- \(0\), if it has no digon; or
- \(1/2\), if its two arcs form a digon.

---

## 6. Consolidated bounds

For \(m=|A(H)|\ge1\), let \(k=\vec\chi(H)\) and define
\[
\rho(k)=
\begin{cases}
0,&k=1,\\[2mm]
1-\dfrac1{k-1},&k\ge2.
\end{cases}
\]
The results above give
\[
\boxed{
\max\left\{
\tau(\chi(B(H))),
\,\rho(\vec\chi(H))
\right\}
\le
\varepsilon_H
\le
\min\left\{
\tau(\chi(U(H))),
\,1-\frac1m
\right\}.
}
\tag{16}
\]

The bound is exact whenever \(\chi(B(H))=\chi(U(H))\), and Theorem 3 supplies another exact family not covered by that equality.

---

## 7. Why “minimum” cannot be literal

Let
\[
H=\overleftrightarrow{2K_2},
\]
the digraph consisting of two vertex-disjoint digons.

For every even \(n\), take a vertex \(z\) and a set \(L\) of \(n-1\) vertices.

- Put a regular tournament on \(L\).
- Put both arcs between \(z\) and every vertex of \(L\).

The underlying graph is \(K_n\), so \(\chi(D)=n\). The digon graph is the star with centre \(z\), so it has no matching of size two and \(D\) is \(H\)-free. Moreover,
\[
d^+(z)=n-1,
\]
while every \(v\in L\) has
\[
d^+(v)=1+\frac{n-2}{2}=\frac n2.
\]
Thus
\[
\delta^+(D)=\frac n2.
\]
Consequently, \(\mathcal P_H(1/2)\) fails.

On the other hand, if \(D\) is \(H\)-free, then \(B(D)\) has matching number at most one, so for \(n\ge4\),
\[
e(B(D))\le n-1.
\]
Therefore
\[
|A(D)|
\le \binom n2+n-1
=\frac{n^2}{2}+\frac n2-1.
\]
If \(\delta^+(D)\ge(1/2+\eta)n\), then
\[
|A(D)|\ge\left(\frac12+\eta\right)n^2,
\]
which is impossible for sufficiently large \(n\). Hence \(\mathcal P_H(1/2+\eta)\) holds for every \(\eta>0\).

It follows that
\[
\{\varepsilon\in[0,1]:\mathcal P_H(\varepsilon)\}
=(1/2,1].
\]
Thus the literal least admissible \(\varepsilon\) does not exist, although the intended infimum is
\[
\varepsilon_H=\frac12.
\]

---

## 8. Remaining gap

These arguments do not settle the general problem. In particular:

- When
  \[
  \chi(B(H))<\chi(U(H)),
  \]
  the chromatic sandwich can leave a substantial interval.
- For oriented graphs \(H\), \(B(H)\) is edgeless, so the principal lower bound in (8) is zero.
- Oriented cyclic graphs of small dichromatic number remain precisely the type of case where fine orientation structure, rather than only the underlying and digon graphs, matters.

Thus this is a complete solution for all symmetric \(H\), for all \(H\) with \(\chi(B(H))=\chi(U(H))\), and for all oriented forests, but not a general determination of \(\varepsilon_H\).