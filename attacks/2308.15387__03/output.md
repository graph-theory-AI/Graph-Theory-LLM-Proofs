```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the natural parallel-edge interpretation, I prove a sharp universal lower bound, characterize equality, and determine several nontrivial exact cases, but not the general minimum.",
  "would_publish": false,
  "caveats": "The extracted statement does not specify parallel edges; I count them and interpret containment as E subseteq M."
}
```

## 1. Precise formulation

The formulation in the catalog omits an important convention. I use the interpretation natural for the coloring application:

- \(V\) is a set of \(r\) vertices.
- \(\mathcal H=(E_1,\ldots,E_N)\) is a multihypergraph: equal nonempty edges are allowed and counted with multiplicity.
- Intersecting means \(E_i\cap E_j\neq\varnothing\) whenever \(i\neq j\).
- An \(m\)-set \(M\) contains an edge when \(E_i\subseteq M\).

Define
\[
h(r,m,t)=\min |\mathcal H|
\]
over such hypergraphs satisfying
\[
|\{i:E_i\subseteq M\}|\ge t
\qquad\text{for every }M\in\binom Vm.
\]
Put
\[
q=r-m.
\]

If “hypergraph” is intended to be simple, the answer can differ drastically. For example, under the convention above,
\[
h(3,2,2)=6,
\]
whereas no simple intersecting hypergraph on three vertices has two distinct edges contained in every two-set.

Throughout, \(t\ge1\) and \(1\le m\le r\).

---

## 2. Normal form and feasibility

### Proposition 2.1

The following hold.

1. If \(m=r\), then \(h(r,r,t)=t\).
2. If \(r\ge 2m\), then \(h(r,m,t)=\infty\).
3. If \(r<2m\), then \(h(r,m,t)<\infty\), with the elementary upper bound
   \[
   h(r,m,t)\le t\binom rm.
   \]

### Proof

When \(m=r\), the sole \(m\)-set is \(V\), so \(t\) copies of any fixed nonempty edge are optimal.

Now suppose \(m<r\). In a minimum hypergraph, no edge has size greater than \(m\), since such an edge is contained in no \(m\)-set and may be deleted.

Moreover, every edge satisfies
\[
|E_i|\ge q+1=r-m+1. \tag{2.1}
\]
Indeed, if \(|E_i|\le q\), there is an \(m\)-set \(M\subseteq V\setminus E_i\). By hypothesis, \(M\) contains some edge \(E_j\), which is then disjoint from \(E_i\), a contradiction.

Thus a minimum hypergraph has
\[
q+1\le |E_i|\le m. \tag{2.2}
\]
If \(r\ge2m\), then \(q+1>m\), so no such hypergraph exists.

If \(r<2m\), take \(t\) copies of every \(m\)-subset of \(V\). Any two \(m\)-subsets intersect because \(2m>r\), and every \(m\)-set contains its own \(t\) copies. ∎

It is often useful to take complements
\[
D_i=V\setminus E_i.
\]
For a minimum hypergraph, (2.2) becomes
\[
q\le |D_i|\le m-1, \tag{2.3}
\]
and the conditions become

\[
\begin{aligned}
&\text{every }Q\in\binom Vq\text{ is contained in at least }t\text{ of the }D_i,\\
&D_i\cup D_j\neq V\qquad(i\neq j).
\end{aligned} \tag{2.4}
\]

Thus the problem is a covering-design problem with the additional prohibition \(D_i\cup D_j=V\).

---

## 3. A sharp universal lower bound

### Theorem 3.1

Suppose \(1\le q=r-m\) and \(h(r,m,t)<\infty\). Then
\[
h(r,m,t)\ge t+2q. \tag{3.1}
\]

Moreover, equality holds precisely when
\[
r\ge \binom{t+2q}{2}. \tag{3.2}
\]

### Proof of the lower bound

For every \(q\)-set \(Q\subseteq V\), its complement \(V\setminus Q\) is an \(m\)-set. Hence at least \(t\) edges are disjoint from \(Q\).

Any pairwise intersecting family of \(N\) nonempty edges has a transversal of size at most \(\lceil N/2\rceil\): pair the edges, choose one point from the intersection of each pair, and choose one point from a possible unpaired edge.

Consequently, \(N\le2q\) is impossible, since a set of at most \(q\) vertices would meet every edge and could be enlarged to a \(q\)-set.

Thus \(N\ge2q+1\). Choose \(2q\) distinct edges, pair them, and choose one vertex from the intersection of each pair. These at most \(q\) vertices meet all \(2q\) selected edges. Enlarge them to a \(q\)-set \(Q\). At least \(t\) further edges must be disjoint from \(Q\), giving
\[
N\ge 2q+t.
\]
This proves (3.1). ∎

For equality, we need a local degree lemma.

### Lemma 3.2

Let \(d(x)\) denote the number of indexed edges containing a vertex \(x\). If \(|\mathcal H|=N\), then
\[
d(x)\le N-t-2q+2 \qquad\text{for every }x\in V. \tag{3.3}
\]

### Proof

For \(q=1\), the set \(\{x\}\) meets \(d(x)\) edges, while at least \(t\) edges must avoid it, so \(d(x)\le N-t\), which is (3.3).

Assume \(q\ge2\). Let \(a=N-d(x)\) be the number of edges not containing \(x\). If \(a\le2q-2\), those \(a\) edges can be met by at most \(\lceil a/2\rceil\le q-1\) vertices, by pairing them as above. Together with \(x\), this gives a set of at most \(q\) vertices meeting every edge, a contradiction. Hence \(a\ge2q-1\).

Choose \(2q-2\) edges not containing \(x\), pair them, and choose \(q-1\) intersection vertices. Together with \(x\), these vertices meet at least
\[
d(x)+2q-2
\]
distinct edges. After enlarging to a \(q\)-set, at most \(N-t\) edges may be met. Therefore
\[
d(x)+2q-2\le N-t,
\]
which is (3.3). ∎

### Proof of the equality characterization

Let
\[
N_0=t+2q.
\]
If \(N=N_0\), Lemma 3.2 gives \(d(x)\le2\) for every vertex. Every pair of indexed edges must have a common vertex, and a vertex of degree at most two can witness at most one pair of edges. Therefore
\[
r\ge\binom{N_0}{2}.
\]

Conversely, suppose \(r\ge\binom{N_0}{2}\). Introduce vertices
\[
x_{ij}\qquad(1\le i<j\le N_0)
\]
and add isolated vertices if necessary. Define
\[
E_i=\{x_{ij}:j\neq i\}.
\]
Then \(E_i\cap E_j=\{x_{ij}\}\), so the hypergraph is intersecting.

Every ground vertex belongs to at most two edges. Hence any \(q\)-set \(Q\) meets at most \(2q\) edges. At least
\[
N_0-2q=t
\]
edges are therefore disjoint from \(Q\), and hence are contained in \(V\setminus Q\). Thus \(h(r,m,t)\le N_0\), completing the proof. ∎

### Consequences

For \(q=r-m\ge1\),
\[
h(r,m,t)=t+2(r-m)
\]
whenever
\[
r\ge\binom{t+2(r-m)}2,
\]
and the minimum is strictly larger otherwise.

For example,
\[
h(r,r-1,1)=3\qquad(r\ge3).
\]

---

## 4. Stronger general lower bounds

Let \(N=h(r,m,t)\) and write
\[
N=t+2q+s,\qquad s\ge0.
\]
Lemma 3.2 gives \(d(x)\le s+2\).

Every edge has at least \(q+1\) vertices by (2.1), so counting incidences gives
\[
(q+1)N
 \le \sum_{x\in V}d(x)
 \le r(s+2). \tag{4.1}
\]

Every pair of edges has a common vertex, so
\[
\binom N2
 \le \sum_{x\in V}\binom{d(x)}2
 \le r\binom{s+2}{2}. \tag{4.2}
\]

Finally, using the complementary sets \(D_i\), each \(D_i\) contains at most
\[
\binom{m-1}{q}
\]
different \(q\)-subsets, while every \(q\)-subset must be covered at least \(t\) times. Hence
\[
N\binom{m-1}{q}\ge t\binom rq. \tag{4.3}
\]
In particular,
\[
h(r,m,t)\ge
\max\left\{
t+2q,\,
\left\lceil
\frac{t\binom rq}{\binom{m-1}{q}}
\right\rceil
\right\}. \tag{4.4}
\]

Equations (4.1) and (4.2) often force a positive excess \(s\). Explicitly, every feasible \(s\) must satisfy
\[
r(s+2)\ge(q+1)(t+2q+s)
\]
and
\[
r\binom{s+2}{2}\ge\binom{t+2q+s}{2}.
\]

---

## 5. Exact boundary case \(r=2m-1\)

### Proposition 5.1

For all \(m\ge1\),
\[
h(2m-1,m,t)=t\binom{2m-1}{m}. \tag{5.1}
\]

### Proof

Here \(q=m-1\). By (2.2), every edge in a minimum hypergraph has size exactly \(m\). Therefore an \(m\)-set \(M\) contains only copies of the edge \(M\) itself, so every \(m\)-set must occur with multiplicity at least \(t\).

Conversely, all \(m\)-sets on \(2m-1\) vertices are pairwise intersecting. Taking \(t\) copies of each gives equality. ∎

For instance,
\[
h(3,2,t)=3t,\qquad h(5,3,t)=10t.
\]

---

## 6. The case \(m=r-1\) and covering numbers

Let \(\mathsf C(v,k,2)\) denote the minimum number of \(k\)-subsets of a \(v\)-set whose union of pair sets covers every two-subset.

### Proposition 6.1

For \(r\ge3\),
\[
h(r,r-1,t)
=
\min\left\{
N\ge t+2:
\mathsf C(N,N-t,2)\le r
\right\}. \tag{6.1}
\]

### Proof

Index the hyperedges by \([N]\), and for each ground vertex \(x\), put
\[
B_x=\{i:x\in E_i\}\subseteq[N].
\]

The original edges are pairwise intersecting exactly when the \(r\) blocks \(B_x\) cover every pair of \([N]\).

Moreover, \(V\setminus\{x\}\) contains precisely the edges with indices outside \(B_x\), so the local condition is
\[
N-|B_x|\ge t,
\]
or \(|B_x|\le N-t\).

Thus the \(B_x\) are \(r\) blocks of size at most \(N-t\) covering every pair. Blocks of smaller size can be enlarged, proving one direction. Conversely, any such pair covering defines
\[
E_i=\{x:i\in B_x\},
\]
which gives the required intersecting hypergraph. ∎

This is an exact reduction, though general covering numbers do not have a closed formula.

As a concrete consequence,
\[
h(4,3,t)=\left\lceil\frac{5t}{2}\right\rceil. \tag{6.2}
\]

### Proof of (6.2)

In a minimum hypergraph, every edge has size two or three. Let \(D_i=V\setminus E_i\), so every \(D_i\) has size one or two. Every vertex must belong to at least \(t\) of the \(D_i\).

Two two-element sets \(D_i,D_j\) are forbidden precisely when they are disjoint, since then \(D_i\cup D_j=V\). Hence the support of the two-element \(D_i\)'s is a pairwise-intersecting graph on four vertices, and is contained in either a star or a triangle.

- In the star case, the three leaves each require \(t\) incidences, and each selected set covers at most one leaf. Thus at least \(3t\) sets are needed.
- In the triangle case, the fourth vertex requires \(t\) singleton sets. Covering the other three vertices \(t\) times using sets of size at most two requires at least \(\lceil3t/2\rceil\) further sets.

Thus
\[
N\ge t+\left\lceil\frac{3t}{2}\right\rceil
=\left\lceil\frac{5t}{2}\right\rceil.
\]

For equality, take \(t\) copies of \(D=\{4\}\), and use the pairs
\[
\{1,2\},\quad \{1,3\},\quad \{2,3\}
\]
with balanced multiplicities totalling \(\lceil3t/2\rceil\). For \(t=2u\), use \(u,u,u\); for \(t=2u+1\), use \(u+1,u+1,u\). Taking complements produces the desired intersecting hypergraph. ∎

For example,
\[
h(4,3,2)=5.
\]

---

## 7. Another exact family: \(h(6,4,t)\)

### Proposition 7.1

For every \(t\ge1\),
\[
h(6,4,t)=
\begin{cases}
5t,&t\text{ even},\\
5t+1,&t\text{ odd}.
\end{cases} \tag{7.1}
\]

### Proof

Here \(q=2\). In a minimum hypergraph, every edge has size three or four, so every complement \(D_i\) has size two or three. Every pair of vertices must be contained in at least \(t\) of the \(D_i\)'s.

A \(D_i\) contains at most three pairs. Since there are \(15\) pairs,
\[
3N\ge15t,
\]
and hence \(N\ge5t\).

If equality \(N=5t\) holds, every \(D_i\) must be a triple and every pair must occur exactly \(t\) times. For any fixed vertex \(v\), the five pairs through \(v\) then have total multiplicity \(5t\). Every triple containing \(v\) accounts for exactly two of these incidences. Thus \(5t\) must be even. Hence, for odd \(t\),
\[
N\ge5t+1.
\]

For the constructions, consider the six triples
\[
\mathcal D_6=
\{123,124,345,346,156,256\}.
\]
They cover the pairs \(12,34,56\) twice and every other pair once.

Add the four triples
\[
135,\quad146,\quad236,\quad245
\]
to obtain a ten-triple family \(\mathcal D_{10}\) in which every pair occurs exactly twice. No two triples in \(\mathcal D_{10}\) are complementary.

If \(t=2a\), take \(a\) copies of every member of \(\mathcal D_{10}\). If \(t=2a+1\), take \(a\) copies of \(\mathcal D_{10}\) and one copy of \(\mathcal D_6\). Finally, replace every \(D\) by the edge \(V\setminus D\). The absence of complementary triples makes these edges intersecting, and the pair-covering property is exactly the required condition on four-sets. The numbers of edges are respectively \(5t\) and \(5t+1\). ∎

In particular,
\[
h(6,4,1)=6.
\]

---

## 8. General dual formulation and constructions

For any indexed hypergraph \(E_1,\ldots,E_N\), define
\[
B_x=\{i:x\in E_i\}\subseteq[N]\qquad(x\in V).
\]
Then the original problem is exactly equivalent to finding \(r\) blocks \(B_x\subseteq[N]\) such that

\[
\binom{[N]}2\subseteq
\bigcup_{x\in V}\binom{B_x}{2}, \tag{8.1}
\]
and
\[
\left|\bigcup_{x\in Q}B_x\right|\le N-t
\qquad\text{for every }Q\in\binom Vq. \tag{8.2}
\]

Condition (8.1) says the blocks cover all pairs of edge indices. Condition (8.2) says every \(q\)-set of ground vertices meets at most \(N-t\) edges.

A general upper-bound mechanism follows. If \(r\) blocks of size at most \(k\) cover all pairs of \([N]\), and
\[
N\ge t+qk, \tag{8.3}
\]
then their union over any \(q\) ground vertices has size at most \(qk\), giving a valid hypergraph. Consequently,
\[
\mathsf C(N,k,2)\le r,\quad N\ge t+qk
\quad\Longrightarrow\quad
h(r,m,t)\le N. \tag{8.4}
\]

A completely explicit probabilistic bound is
\[
\mathsf C(N,k,2)
\le
\left\lceil
\frac{N(N-1)}{k(k-1)}
\left(\log\binom N2+1\right)
\right\rceil. \tag{8.5}
\]
Indeed, choose that many independent uniformly random \(k\)-sets. A fixed pair is missed with probability at most
\[
\exp\!\left(-R\frac{k(k-1)}{N(N-1)}\right),
\]
and the expected number of missed pairs is less than one.

---

## 9. Fixed-\((r,m)\) asymptotics in \(t\)

There is a finite linear-programming description of the leading constant.

Let
\[
\mathcal A=\{A\subseteq[r]:q+1\le |A|\le m\}.
\]
For an intersecting subfamily \(\mathcal F\subseteq\mathcal A\), define
\[
\rho(\mathcal F)=
\min\left\{
\sum_{A\in\mathcal F}z_A:
z_A\ge0,\ 
\sum_{\substack{A\in\mathcal F\\A\subseteq M}}z_A\ge1
\ \forall M\in\binom{[r]}m
\right\}.
\]
Let
\[
\rho_{r,m}=\min_{\mathcal F\text{ intersecting}}\rho(\mathcal F).
\]

Then
\[
\rho_{r,m}t
\le h(r,m,t)
\le \rho_{r,m}t+2^r. \tag{9.1}
\]

For the lower bound, divide the multiplicities in any integer solution by \(t\). For the upper bound, take an optimal fractional solution and replace each \(tz_A\) by \(\lceil tz_A\rceil\). Thus, for every fixed feasible pair \((r,m)\),
\[
h(r,m,t)=\rho_{r,m}t+O_{r,m}(1). \tag{9.2}
\]

This determines the exact asymptotic coefficient by a finite, rational optimization problem, although it does not give a closed expression for \(\rho_{r,m}\).

---

## 10. Exact integer programming formulation

For computational checks, in the feasible range \(r<2m\), let
\[
U=t\binom rm.
\]
For every \(A\in\mathcal A\), introduce an integer multiplicity \(x_A\ge0\) and a binary variable \(y_A\). Minimize
\[
\sum_{A\in\mathcal A}x_A
\]
subject to
\[
y_A\le x_A\le Uy_A,
\]
\[
y_A+y_B\le1\qquad(A\cap B=\varnothing),
\]
and
\[
\sum_{\substack{A\in\mathcal A\\A\subseteq M}}x_A\ge t
\qquad\text{for every }M\in\binom{[r]}m.
\]
The trivial construction with all \(m\)-sets shows that the cap \(U\) does not exclude an optimum. Thus this MILP computes \(h(r,m,t)\) exactly under the stated convention.

---

## 11. Remaining gap

The general problem is not resolved here. In the dual formulation, one must optimize a pair-covering family of \(r\) blocks under the strong condition that the union of every \(q\) blocks has size at most \(N-t\). The lower bounds above use degrees, pair counting, and covering counts, but these do not generally characterize such block systems.

The main established partial results are:

- complete feasibility classification;
- the sharp bound \(h\ge t+2(r-m)\) and exact characterization of equality;
- the covering lower bound (4.4) and the stronger degree inequalities (4.1)–(4.2);
- exact values on the boundary \(r=2m-1\);
- the exact covering-number reduction for \(m=r-1\);
- exact formulas for \((r,m)=(4,3)\) and \((6,4)\);
- an exact fixed-\((r,m)\) asymptotic coefficient via a finite LP.

I have not checked whether these elementary reductions or special cases already appear in the source paper or in the covering-design literature.