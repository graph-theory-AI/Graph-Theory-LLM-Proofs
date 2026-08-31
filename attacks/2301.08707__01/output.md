```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but one obtains an O(n log n) rainbow path decomposition in general and linear covers for positive-codegree graphs, Dirac-dense graphs, and complete bipartite graphs.",
  "would_publish": false,
  "caveats": "Assumes finite simple graphs; the logarithmic factor remains for general graphs, and the dense-case constructions reuse connector edges."
}
```

# 1. Statement and conventions

Let \(\phi:E(G)\to\mathcal C\) be a proper edge-coloring of a finite simple graph \(G\). Write
\[
\rho(G,\phi)
\]
for the minimum number of rainbow simple paths whose union contains \(E(G)\). The paths need not be edge-disjoint.

The following partial results are proved below.

### Theorem A: general logarithmic bound
If \(G\) has \(n\) vertices and \(m\) edges, then
\[
\rho(G,\phi)\le
\min\left\{
m,\;
2n+\left\lceil 2n\log^+\!\left(\frac{m}{2n}\right)\right\rceil
\right\},
\]
where \(\log^+x=\max\{0,\log x\}\). In particular,
\[
\rho(G,\phi)=O(n\log n),
\]
and more precisely \(\rho(G,\phi)=O(n\log(\Delta(G)+1))\).

The proof actually partitions \(E(G)\) into rainbow paths.

### Theorem B: positive codegree
Suppose that some \(\gamma>0\) satisfies
\[
|N(x)\cap N(y)|\ge \gamma n
\qquad\text{for every distinct }x,y\in V(G).
\]
Then
\[
\rho(G,\phi)\le \frac{14n}{\gamma}.
\]

Consequently, for every fixed \(\varepsilon>0\),
\[
\delta(G)\ge \left(\frac12+\varepsilon\right)n
\quad\Longrightarrow\quad
\rho(G,\phi)\le \frac{7n}{\varepsilon}.
\]

Thus the conjecture holds for graphs uniformly above the Dirac threshold.

### Theorem C: complete bipartite graphs
Every properly edge-colored \(K_{p,q}\), with \(n=p+q\), has a rainbow path cover of size at most
\[
27n.
\]

This includes arbitrary Latin-square colorings of balanced complete bipartite graphs.

These estimates are not claimed to be new in the literature; the arguments are self-contained.

---

# 2. A longest-rainbow-path lemma

We begin with a standard extraction argument.

## Lemma 2.1
Let \(H\) be a nonempty properly edge-colored simple graph with at most \(n\) vertices and \(m\) edges. Then \(H\) contains a rainbow path of length at least
\[
\frac{m}{2n}.
\]

### Proof

First obtain a nonempty subgraph \(H'\subseteq H\) with
\[
\delta(H')\ge \frac mn.
\]
Indeed, repeatedly delete a vertex of current degree less than \(m/n\). If all vertices were deleted, every edge would be counted exactly once, when its first endpoint was deleted, and hence
\[
m< |V(H)|\frac mn\le m,
\]
a contradiction.

Let
\[
P=v_0v_1\cdots v_\ell
\]
be a longest rainbow path in \(H'\). Consider the endpoint \(v_0\). If \(v_0x\) has \(x\notin V(P)\) and color not appearing on \(P\), then \(xv_0v_1\cdots v_\ell\) is a longer rainbow path. Therefore every edge incident with \(v_0\) either

1. has one of the \(\ell\) colors appearing on \(P\), or
2. has its other endpoint in \(V(P)\setminus\{v_0\}\).

Properness implies that at most \(\ell\) incident edges fall into the first category. Simplicity of \(H\) implies that at most \(\ell\) fall into the second. Hence
\[
d_{H'}(v_0)\le 2\ell.
\]
It follows that
\[
\ell\ge \frac{\delta(H')}{2}\ge \frac{m}{2n}.
\qedhere
\]

## Proof of Theorem A

Start with \(G\) and repeatedly remove all edges of a rainbow path supplied by Lemma 2.1. If \(m_t\) edges remain, the removed path has at least \(m_t/(2n)\) edges, so
\[
m_{t+1}\le \left(1-\frac1{2n}\right)m_t.
\]
After
\[
T=\left\lceil 2n\log\left(\frac m{2n}\right)\right\rceil
\]
steps, provided \(m>2n\), we have
\[
m_T
 \le m\exp\left(-\frac{T}{2n}\right)
 \le 2n.
\]
Cover the remaining edges individually. This gives
\[
\rho(G,\phi)\le
2n+\left\lceil 2n\log^+\left(\frac m{2n}\right)\right\rceil.
\]

Since \(G\) is simple,
\[
m\le \frac{n(n-1)}2,
\]
which yields \(O(n\log n)\). Also \(m\le n\Delta/2\), giving
\[
\rho(G,\phi)
 \le 2n+\left\lceil2n\log^+\left(\frac{\Delta}{4}\right)\right\rceil.
\]

---

# 3. Partition into linearly many rainbow matchings

The dense special cases use the following elementary observation.

## Lemma 3.1
Every properly edge-colored simple \(n\)-vertex graph has an edge-partition into at most \(3n\) rainbow matchings.

### Proof

Construct a conflict graph \(J\) whose vertices are the edges of \(G\), with two vertices adjacent when the corresponding edges of \(G\)

- share an endpoint, or
- have the same color.

An independent set in \(J\) is precisely a rainbow matching.

For an edge \(e=uv\) of color \(c\), write \(r_c\) for the size of its color class. Since the coloring is proper, a color class is a matching, so \(r_c\le\lfloor n/2\rfloor\). Therefore
\[
d_J(e)
 \le (d_G(u)-1)+(d_G(v)-1)+(r_c-1)
 < \frac{5n}{2}.
\]
A greedy coloring of \(J\) uses at most \(3n\) colors. Its color classes give the required rainbow matchings. \(\square\)

The difficulty is that a rainbow matching need not lie on one path. In graphs with many short connectors, however, every sufficiently small rainbow matching can be threaded into a rainbow path.

---

# 4. Positive-codegree graphs

## Lemma 4.1: threading through common neighbors
Suppose
\[
|N(x)\cap N(y)|\ge\gamma n
\]
for every distinct \(x,y\). If \(M\) is a rainbow matching of size
\[
k\le \frac{\gamma n}{10},
\]
then there is a rainbow path containing every edge of \(M\). The same is trivially true when \(k=1\).

### Proof

Order and orient the matching edges arbitrarily:
\[
M=\{a_1b_1,\ldots,a_kb_k\}.
\]
We construct a path
\[
a_1b_1w_1a_2b_2w_2\cdots w_{k-1}a_kb_k,
\]
where the \(w_i\) are distinct and outside \(V(M)\).

Suppose \(w_1,\ldots,w_{i-1}\) have been chosen. Let \(F\) consist of

- all \(k\) colors appearing on \(M\), and
- all \(2(i-1)\) connector colors already used.

Thus
\[
|F|=k+2(i-1).
\]

There are at least
\[
\gamma n-2k-(i-1)
\]
unused common neighbors of \(b_i\) and \(a_{i+1}\). For each forbidden color, properness implies that at most one such vertex \(w\) has
\(\phi(b_iw)\) equal to that color, and at most one has
\(\phi(wa_{i+1})\) equal to it. Thus at most \(2|F|\) candidates are forbidden.

The number of available candidates minus the number potentially forbidden is at least
\[
\gamma n-2k-(i-1)-2(k+2i-2)
 =\gamma n-4k-5i+5.
\]
Since \(i\le k-1\), this is at least
\[
\gamma n-9k+10>0.
\]
Choose such a \(w_i\). Both new colors avoid \(F\), and they differ from each other because the two new edges meet at \(w_i\) and the coloring is proper.

Continuing in this way produces a simple rainbow path containing \(M\). \(\square\)

## Proof of Theorem B

Partition \(E(G)\) into at most \(3n\) rainbow matchings by Lemma 3.1. Set
\[
s=\max\left\{1,\left\lfloor\frac{\gamma n}{10}\right\rfloor\right\}
\]
and split every matching into pieces of size at most \(s\).

For all \(\gamma n>0\),
\[
s\ge \frac{\gamma n}{20}.
\]
Hence the total number of pieces is at most
\[
3n+\frac{m}{s}
 \le 3n+\frac{n^2/2}{\gamma n/20}
 \le \frac{13n}{\gamma}.
\]
Allowing harmless rounding gives \(14n/\gamma\).

Each piece is a rainbow matching and, by Lemma 4.1, is contained in one rainbow path. Connector edges may be reused, which is permitted for a cover.

If
\[
\delta(G)\ge \left(\frac12+\varepsilon\right)n,
\]
then for distinct \(x,y\),
\[
|N(x)\cap N(y)|
 \ge d(x)+d(y)-n
 \ge 2\varepsilon n.
\]
Taking \(\gamma=2\varepsilon\) gives
\[
\rho(G,\phi)\le \frac{7n}{\varepsilon}.
\]

In particular, an arbitrary proper edge-coloring of \(K_n\) has a linear rainbow path cover; for example, \(28n\) paths suffice for \(n\ge4\).

---

# 5. Complete bipartite graphs

Complete bipartite graphs do not satisfy the positive-codegree hypothesis: vertices in opposite parts have no common neighbor. They nevertheless have plentiful three-edge connectors.

## Lemma 5.1
Let \(G=K_{p,q}\) with bipartition \(A\cup B\), and put \(h=\min\{p,q\}\). Every rainbow matching \(M\) of size
\[
k\le \frac{h}{12}
\]
is contained in a rainbow path.

### Proof

Write
\[
M=\{a_1b_1,\ldots,a_kb_k\},
\qquad a_i\in A,\ b_i\in B.
\]
We seek a path
\[
a_1b_1x_1y_1a_2b_2x_2y_2\cdots
x_{k-1}y_{k-1}a_kb_k,
\]
where \(x_i\in A\setminus V(M)\), \(y_i\in B\setminus V(M)\), and all introduced vertices are distinct.

At stage \(i\), let \(F\) contain all \(k\) matching colors and the \(3(i-1)\) connector colors already used:
\[
|F|=k+3(i-1).
\]

First choose an unused \(x_i\in A\setminus V(M)\) such that
\[
\phi(b_ix_i)\notin F.
\]
There are \(p-k-(i-1)\) candidates and at most \(|F|\) forbidden ones. At the last stage their difference is at least
\[
p-6k+8>0.
\]

Let \(\alpha=\phi(b_ix_i)\). Now choose an unused \(y_i\in B\setminus V(M)\) such that both
\[
\phi(x_iy_i),\ \phi(y_ia_{i+1})
\]
avoid \(F\cup\{\alpha\}\). Properness at \(x_i\) and \(a_{i+1}\) shows that at most \(2(|F|+1)\) candidates are forbidden. At the last stage, candidates minus forbidden choices is at least
\[
q-10k+12>0.
\]
The two latter colors are automatically distinct because their edges meet at \(y_i\).

Since \(k\le h/12\), all choices can be made. The resulting path is simple and rainbow. \(\square\)

## Proof of Theorem C

Use Lemma 3.1 to partition \(E(K_{p,q})\) into at most \(3n\) rainbow matchings. Let
\[
s=\max\left\{1,\left\lfloor\frac{h}{12}\right\rfloor\right\}.
\]
Split each matching into pieces of size at most \(s\). Since \(s\ge h/24\), the number of pieces is at most
\[
3n+\frac{pq}{s}
 \le 3n+\frac{24pq}{h}
 =3n+24\max\{p,q\}
 \le 27n.
\]
Every piece is covered by one rainbow path using Lemma 5.1. Thus
\[
\rho(K_{p,q},\phi)\le27(p+q).
\]

---

# 6. A further parameterized regime

Let \(q_\phi\) be the number of colors actually used and let
\[
s_\phi=m-q_\phi
\]
be the number of color repetitions beyond the first occurrence of each color.

The main \(19n\)-path separating theorem in the supplied source implies that every uncolored \(n\)-vertex graph has an edge-cover by at most \(19n\) ordinary paths. Choose one representative edge of each color. The representative subgraph has globally distinct edge colors, so every path in it is automatically rainbow. Cover the other \(s_\phi\) edges individually. Hence
\[
\rho(G,\phi)\le 19n+s_\phi.
\]
Thus the conjecture holds whenever \(m-q_\phi=O(n)\).

Similarly, if every color occurs at most \(\mu\) times, enumerate the occurrences of every color and put the \(i\)-th occurrence into layer \(i\). Every layer has globally distinct colors, giving
\[
\rho(G,\phi)\le 19\mu n.
\]
This settles the bounded-color-multiplicity subclass.

---

# 7. Lower bounds and the remaining gap

Two immediate lower bounds are
\[
\rho(G,\phi)\ge
\max\left\{
\left\lceil\frac{\Delta(G)}2\right\rceil,\,
\max_c |\phi^{-1}(c)|
\right\}.
\]
Indeed, a simple path contains at most two edges incident with a fixed vertex and at most one edge of a fixed color.

Both bounds can be asymptotically \(n/2\):

- A star \(K_{1,n-1}\), with its necessarily distinct incident colors, needs at least \(\lceil(n-1)/2\rceil\) paths.
- A matching of size \(n/2\) whose edges all have the same color is properly colored and needs \(n/2\) rainbow paths.

Thus a linear result would have the correct order.

The logarithmic extraction argument cannot by itself yield the conjecture. For example, a standard \(d\)-edge-coloring of \(K_{d,d}\) uses only \(d\) colors, so every rainbow path has at most \(d\) edges, of the same order as the average degree. Removing one longest path at a time therefore supplies only multiplicative progress. A linear proof needs a simultaneous packing or threading mechanism.

Lemma 3.1 reduces the problem to this topology issue: universally, \(E(G)\) can be partitioned into \(O(n)\) rainbow matchings. In complete, positive-codegree, and complete bipartite graphs, each sufficiently small such matching can be threaded into one rainbow path using fresh short connectors. In a general graph the matching may be distributed among many blocks or branches, and there may be no suitable connectors. Nothing above controls the total number of resulting path pieces in that situation.

The known \(O(n)\) rainbow-trail statement also does not directly close the gap. A single rainbow trail may have a dense edge set: for odd \(n\), a uniquely colored \(K_n\) has a rainbow Euler tour, but covering its edges by simple paths still requires at least
\[
\frac{\binom n2}{n-1}=\frac n2
\]
paths. Hence there is no constant-cost conversion from an individual rainbow trail to rainbow paths.

Finally, if “graph” were interpreted as allowing parallel edges, the conjecture would be false: two vertices joined by arbitrarily many parallel edges of distinct colors form a proper edge-coloring, while every simple path contains at most one of those edges. The source problem is therefore meaningful only under the usual simple-graph convention.