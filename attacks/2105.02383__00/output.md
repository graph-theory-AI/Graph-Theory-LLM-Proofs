```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The known lower bound rules out a degree-uniform polynomial exponent but not polynomial growth at any fixed degree; below I give a self-contained polynomial bound for total maximum degree at most two and a separator-based sufficient condition.",
  "would_publish": false,
  "caveats": "The broad request for 'natural parameters' is non-formal, no fixed-degree counterexample or general polynomial bound is obtained, and the cited 2025 preprint is not used or independently checked."
}
```

## 1. Precise formulation and a quantifier correction

For an integer \(\Delta\), define
\[
R_\Delta(n)=\max\left\{\overrightarrow r_1(H):
  |V(H)|=n,\ H\text{ acyclic},\ \Delta(H)\leq \Delta\right\},
\]
where \(\Delta(H)\) is the maximum degree of the underlying undirected graph.

There are two substantially different meanings of “polynomial for bounded degree”:

\[
\tag{U}
\exists C\ \exists A(\Delta)\quad
R_\Delta(n)\leq A(\Delta)n^C
\quad\text{for all fixed }\Delta\text{ and large }n,
\]
where the exponent is independent of \(\Delta\); and
\[
\tag{P}
\forall\Delta\ \exists C_\Delta,A_\Delta\quad
R_\Delta(n)\leq A_\Delta n^{C_\Delta}.
\]

The first is a degree-uniform, fixed-exponent polynomial bound. The second merely asks for polynomial growth for each fixed degree cap.

Under the standard uniform interpretation of the \(\Omega\)-notation, the quoted Fox–He–Wigderson theorem says that for an absolute \(c>0\),
\[
\tag{1}
R_\Delta(n)\geq
n^{c\,\Delta^{2/3}/(\log\Delta)^{5/3}}
\]
for appropriate \(\Delta\) and all sufficiently large \(n\), with the threshold allowed to depend on \(\Delta\).

Since
\[
\frac{\Delta^{2/3}}{(\log\Delta)^{5/3}}\longrightarrow\infty,
\]
(1) has the following consequences.

### Proposition 1

The lower bound (1):

1. disproves (U), even if the multiplicative factor \(A(\Delta)\) is arbitrary;
2. disproves the directed Burr–Erdős-type assertion \(R_\Delta(n)=O_\Delta(n)\);
3. does **not** disprove (P).

#### Proof

Given an absolute exponent \(C\), choose a fixed \(\Delta\) such that
\[
c\,\frac{\Delta^{2/3}}{(\log\Delta)^{5/3}}>C.
\]
If \(R_\Delta(n)\leq A(\Delta)n^C\), then for large \(n\), (1) would give
\[
n^{c\Delta^{2/3}/(\log\Delta)^{5/3}}
\leq A(\Delta)n^C,
\]
which is impossible as \(n\to\infty\). Taking \(C=1\) also rules out a linear bound for a suitable fixed \(\Delta\).

On the other hand, after \(\Delta\) is fixed, the exponent in (1) is a fixed constant. Thus (1) is itself only a polynomial lower bound in \(n\), and is consistent with an upper bound \(n^{C_\Delta}\). ∎

Consequently, the catalog sentence that the source provides “super-polynomial examples” for \(\overrightarrow r_1\) is correct only if “polynomial” means an exponent uniform in \(\Delta\). Under the usual fixed-degree interpretation, it overstates the result.

A convenient numerical formulation is
\[
\rho(\Delta)=\limsup_{n\to\infty}
 \frac{\log R_\Delta(n)}{\log n}.
\]
The actual fixed-degree question is whether \(\rho(\Delta)<\infty\) for every fixed \(\Delta\). The source lower bound only proves
\[
\rho(\Delta)\geq
c\,\frac{\Delta^{2/3}}{(\log\Delta)^{5/3}}.
\]

The quoted quasi-polynomial upper bound gives, for every fixed degree cap,
\[
\tag{2}
R_\Delta(n)\leq
2^{(\log n)^{C_\Delta}}
\]
for some constant \(C_\Delta\). Thus (1) and (2) leave a genuine polynomial versus super-polynomial gap.

The maximum-degree-three super-polynomial lower bound in the source is for \(k\geq2\) edge colors. It does not transfer to \(k=1\): one always has
\[
\overrightarrow r_1(H)\leq \overrightarrow r_k(H),
\]
so a lower bound for the larger, colored quantity says nothing about the smaller one. The underlying uncolored tournament of a colored witness may contain many copies of \(H\), none monochromatic.

---

## 2. Two elementary embedding lemmas

We will use the fact that copies are not required to be induced.

### Lemma 2: Subadditivity over weak components

If \(H=H_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}H_t\), then
\[
\overrightarrow r_1(H)
 \leq \sum_{i=1}^t \overrightarrow r_1(H_i).
\]

#### Proof

Partition an arbitrary tournament on the right-hand side into sets of orders \(\overrightarrow r_1(H_i)\). Embed \(H_i\) in the \(i\)-th part. There are no required arcs between distinct components. ∎

### Lemma 3: A balanced vertex in every tournament

Every tournament \(T\) on \(N\) vertices has a vertex \(x\) satisfying
\[
d_T^+(x),d_T^-(x)\geq\frac{N-2}{4}.
\]

In particular, if \(N=4S\), both semidegrees are at least \(S\).

#### Proof

Order the vertices \(v_1,\dots,v_N\) so that
\[
d^+(v_1)\leq\cdots\leq d^+(v_N),
\]
and put \(j=\lceil N/2\rceil\), \(x=v_j\).

For \(A=\{v_1,\dots,v_j\}\),
\[
j\,d^+(x)
 \geq \sum_{v\in A}d^+(v)
 \geq e(T[A])=\binom j2.
\]
Hence \(d^+(x)\geq(j-1)/2\).

Let \(B=\{v_j,\dots,v_N\}\) and \(s=|B|=N-j+1\). For every \(v\in B\),
\[
d^-(v)=N-1-d^+(v)\leq N-1-d^+(x)=d^-(x).
\]
Therefore
\[
s\,d^-(x)
 \geq \sum_{v\in B}d^-(v)
 \geq e(T[B])=\binom s2.
\]
Thus \(d^-(x)\geq(s-1)/2\). Checking even and odd \(N\) gives the stated lower bound. Since semidegrees are integers, when \(N=4S\) they are at least \(S\). ∎

---

## 3. A separator parameter giving polynomial growth

Here is one explicit, although far from necessary, structural parameter.

Fix \(0<\alpha<1\). A connected oriented graph \(H\) is **recursively \(\alpha\)-uniform-separable** if either \(|H|=1\), or there is a vertex \(z\) such that:

1. every weak component \(H_i\) of \(H-z\) has
   \[
   |H_i|\leq \alpha |H|;
   \]
2. each \(H_i\) is recursively \(\alpha\)-uniform-separable;
3. for each \(i\), all arcs between \(z\) and \(H_i\) have the same direction—either all go from \(z\) to \(H_i\), or all go from \(H_i\) to \(z\).

A disconnected graph has the property when all its weak components do.

### Theorem 4

Let
\[
p=1+\left\lceil\frac{\log 4}{\log(1/\alpha)}\right\rceil.
\]
Every acyclic, recursively \(\alpha\)-uniform-separable digraph \(H\) on \(n\) vertices satisfies
\[
\overrightarrow r_1(H)\leq n^p.
\]

#### Proof

It suffices first to handle connected \(H\), by induction on \(n\). Choose \(z\) and components \(H_1,\dots,H_t\) from the definition, and put \(n_i=|H_i|\). By induction,
\[
\overrightarrow r_1(H_i)\leq n_i^p.
\]
Set
\[
S=\sum_i n_i^p.
\]
Since \(n_i\leq\alpha n\) and \(\sum_i n_i=n-1\),
\[
S
 \leq (\max_i n_i)^{p-1}\sum_i n_i
 < \alpha^{p-1}n^p.
\]
The choice of \(p\) ensures \(4\alpha^{p-1}\leq1\), so
\[
4S\leq n^p.
\]

Take any tournament on \(n^p\) vertices and restrict to \(4S\) vertices. By Lemma 3, this subtournament has a vertex \(x\) with at least \(S\) inneighbors and at least \(S\) outneighbors.

For every component joined outward from \(z\), allocate a disjoint set of \(n_i^p\) vertices inside \(N^+(x)\), and embed \(H_i\) there. Similarly, embed every component joined toward \(z\) in a disjoint subset of \(N^-(x)\). Mapping \(z\) to \(x\) now gives a copy of \(H\).

For disconnected \(H\), apply Lemma 2 and
\[
\sum_C |C|^p\leq\left(\sum_C|C|\right)^p=n^p.
\]
∎

This supplies a natural coarse parameter: the best balance \(\alpha\) obtainable by recursively deleting vertices whose attachments to each remaining component are directionally uniform.

### Corollary 5: Oriented forests

Every orientation \(F\) of a forest on \(n\) vertices satisfies
\[
\overrightarrow r_1(F)\leq n^3.
\]

#### Proof

Every tree has a centroid whose deletion leaves components of order at most half the original order. Since a tree has exactly one edge from the centroid to each resulting component, the directional-uniformity condition is automatic. Thus every oriented tree is recursively \(1/2\)-uniform-separable. Theorem 4 with \(\alpha=1/2\) gives exponent
\[
1+\frac{\log4}{\log2}=3.
\]
Use Lemma 2 for forests. ∎

The cubic estimate is intentionally crude; its role here is to give a completely self-contained parameter-based argument.

---

## 4. Polynomial growth for total maximum degree at most two

The separator idea can be sharpened for paths.

### Proposition 6: Oriented paths

Every oriented path \(P\) on \(m\) vertices satisfies
\[
\overrightarrow r_1(P)\leq m^2.
\]

#### Proof

Proceed by induction on \(m\). The assertion is immediate for \(m=1\). Choose a central vertex \(z\) of \(P\). The two components of \(P-z\), allowing one to be empty, have orders \(a,b\leq q=\lfloor m/2\rfloor\).

Consider a tournament \(T\) on
\[
N=4q^2
\]
vertices. Each component must be placed either in the outneighborhood of the image of \(z\) or in its inneighborhood, according to the orientation of its unique edge to \(z\).

If the two components require different semineighborhoods, Lemma 3 gives a vertex \(x\) with
\[
d^+(x),d^-(x)\geq q^2.
\]
By induction, the two components can be embedded in their respective semineighborhoods because
\[
a^2,b^2\leq q^2.
\]

If both components require the outneighborhood, choose a vertex \(x\) of maximum outdegree. Since the average outdegree is \((N-1)/2\),
\[
d^+(x)\geq 2q^2\geq a^2+b^2.
\]
Partition an appropriate subset of \(N^+(x)\) into parts of orders \(a^2\) and \(b^2\), and apply induction separately. The case where both require the inneighborhood is symmetric.

Thus every tournament on \(4q^2\) vertices contains \(P\). Finally,
\[
4q^2\leq m^2.
\]
∎

### Proposition 7: Acyclic orientations of cycles

If \(C\) is an acyclic orientation of a cycle on \(m\geq3\) vertices, then
\[
\overrightarrow r_1(C)\leq 2(m-1)^2.
\]

#### Proof

Since \(C\) is acyclic, it has a source \(z\). Both arcs incident with \(z\) point away from \(z\), and \(C-z\) is an oriented path on \(m-1\) vertices.

Every tournament on \(2(m-1)^2\) vertices has a vertex \(x\) with outdegree at least \((m-1)^2\). By Proposition 6, \(N^+(x)\) contains \(C-z\). Since \(x\) dominates all vertices in this copy, it in particular dominates the two former neighbors of \(z\), completing a copy of \(C\). ∎

### Theorem 8: The degree-two case

For total maximum degree at most two,
\[
\boxed{R_2(n)\leq 2n^2.}
\]

Moreover,
\[
\boxed{R_1(n)=n.}
\]

#### Proof

Every weak component of a graph of maximum degree at most two is a path, a cycle, or an isolated vertex. Since \(H\) is acyclic as a digraph, every cycle component has an acyclic orientation.

Let the component orders be \(s_1,\dots,s_t\). Propositions 6 and 7, followed by Lemma 2, give
\[
\overrightarrow r_1(H)
 \leq 2\sum_{i=1}^t s_i^2
 \leq 2\left(\sum_{i=1}^t s_i\right)^2
 =2n^2.
\]

If \(\Delta(H)\leq1\), every component is an isolated vertex or a single arc. Given any tournament on \(n\) vertices, partition its vertices into corresponding singletons and pairs; on each pair, map the tail of the required arc to the winner of the tournament edge. Hence every such \(H\) embeds in every \(n\)-vertex tournament. Since fewer than \(n\) vertices cannot contain \(H\),
\[
\overrightarrow r_1(H)=n.
\]
∎

Thus, under the standard total-degree convention, any fixed-degree super-polynomial one-color counterexample must have degree cap at least three.

---

## 5. A coarse component-size parameter

Let \(C_1,\dots,C_t\) be the weak components of an acyclic digraph \(H\), with \(s_i=|C_i|\). Every tournament on \(2^{s_i-1}\) vertices has a transitive subtournament on \(s_i\) vertices, and such a transitive tournament contains every acyclic digraph of order \(s_i\), via a topological ordering. Hence
\[
\tag{3}
\overrightarrow r_1(H)\leq\sum_{i=1}^t2^{s_i-1}.
\]

In particular, if every weak component has order at most \(b\), then
\[
\overrightarrow r_1(H)\leq n\,2^{b-1}.
\]
Consequently, largest weak-component order \(O(\log n)\) is another elementary sufficient parameter for polynomial growth. This does not address connected bounded-degree examples.

---

## 6. Exact ordered-pattern reformulation

There is also a useful exact reformulation explaining why degree alone does not record all relevant structure.

Fix a labeling of the host tournament by the ordered set \([N]\). Color a pair \(i<j\) by

- \(+\) if \(i\to j\);
- \(-\) if \(j\to i\).

For every total order \(\prec\) on \(V(H)\), define an ordered, partially two-colored graph \(P(H,\prec)\) on the underlying graph of \(H\): an arc \(u\to v\) receives color \(+\) if \(u\prec v\), and color \(-\) if \(v\prec u\). Nonedges impose no condition.

Let \(\mathcal P(H)\) be the family of these patterns over all total orders on \(V(H)\).

### Proposition 9

\(\overrightarrow r_1(H)\) is exactly the least \(N\) such that every two-coloring of the pairs of the ordered set \([N]\) contains an order-preserving copy of some member of \(\mathcal P(H)\).

#### Proof

The above construction is a bijection between tournaments on \([N]\) and \(+/-\) colorings of the pairs of \([N]\).

Given an injection \(\varphi:V(H)\to[N]\), pull back the natural order on \([N]\) to a total order \(\prec\) on \(V(H)\). For an arc \(u\to v\):

- if \(\varphi(u)<\varphi(v)\), the required tournament orientation is equivalent to color \(+\);
- if \(\varphi(v)<\varphi(u)\), it is equivalent to color \(-\).

Thus \(\varphi\) is a directed copy of \(H\) exactly when it is an order-preserving copy of \(P(H,\prec)\). Every injection determines one such \(\prec\), proving the equivalence. ∎

This is an exact characterization, but it is essentially a reformulation rather than the desired low-dimensional “natural parameter”: \(\mathcal P(H)\) may contain up to \(n!\) mixed ordered patterns. It does make precise that any successful parameter must control more than underlying sparsity—namely how orientation constraints behave across many possible vertex orders and scales.

---

## 7. Remaining gap

The following remain unresolved by the quoted results and by the arguments above:

1. Whether, for every fixed \(\Delta\geq3\), there is a constant \(C_\Delta\) such that
   \[
   R_\Delta(n)\leq n^{C_\Delta}.
   \]
2. Conversely, whether some fixed \(\Delta\geq3\) admits a bounded-degree family with
   \[
   \frac{\log \overrightarrow r_1(H_n)}{\log |H_n|}
   \longrightarrow\infty.
   \]
3. A necessary-and-sufficient structural parameter comparable in usefulness to degeneracy in the undirected setting.

The separator balance above is only a sufficient condition; it gives no matching lower bound and excludes bounded-degree expanders, which are natural candidates for the genuinely difficult regime. The principal catalog question therefore remains open, while the degree-uniform interpretation is already negatively resolved by the source lower bound.