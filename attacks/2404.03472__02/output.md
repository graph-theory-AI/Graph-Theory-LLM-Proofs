```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the standard adversarial MIS-oracle model, there is a deterministic O(nΔ log(en/Δ)) algorithm, yielding a genuine subcubic saving when 2Δ ≤ n = o(Δ²), and any bounded-degree transcript supergraph can be completed in O(D²) further queries.",
  "would_publish": false,
  "caveats": "This does not improve the general regime n much larger than Δ²; the elementary lemmas may be folklore, and the argument assumes queries return arbitrary MISs of induced subgraphs."
}
```

# Partial attack on the adaptive MIS-reconstruction problem

## 1. Model and scope

I use the standard model implicit in the source paper:

- The vertex set \(V\), \(|V|=n\), is known.
- The hidden graph \(G\) satisfies \(\Delta(G)\leq \Delta\).
- A query is a set \(S\subseteq V\).
- The answer is an arbitrary maximal independent set of \(G[S]\).
- The algorithm must succeed for every legal sequence of oracle answers.

I do not obtain an \(o(\Delta^3\log(n/\Delta))\) bound for all \(n,\Delta\). I prove:

1. A deterministic adaptive algorithm using
   \[
   O\!\left(n\Delta\log\frac{en}{\Delta}\right)
   \]
   queries.

2. Consequently, under the usual assumption \(n\geq 2\Delta\), this is
   \[
   o\!\left(\Delta^3\log\frac n\Delta\right)
   \qquad\text{whenever }n=o(\Delta^2).
   \]

3. If the transcript has already produced a known supergraph \(H\supseteq G\) of maximum degree \(D\), then \(G\) can be reconstructed in \(O(D^2)\) additional queries.

4. For the special case of a known bipartition in which one side has degree at most one, \(O(\Delta^2\log n)\) deterministic non-adaptive queries suffice.

Thus the unresolved regime is essentially \(n\gtrsim \Delta^2\), where the \(n\)-dependent algorithm ceases to improve the catalogued cubic bound.

The little-\(o\) notation in the original question should be read with \(\Delta\to\infty\); as a two-variable assertion allowing fixed \(\Delta\), it is ambiguous. Comparisons below use \(n/\Delta\geq 2\).

---

## 2. A group-testing primitive supplied by MIS queries

### Lemma 2.1

Let \(x\in V\), and let \(A\subseteq V\setminus\{x\}\) be a known independent set. For every \(B\subseteq A\), one MIS query on \(\{x\}\cup B\) determines whether
\[
N_G(x)\cap B=\varnothing.
\]
Moreover, if the returned MIS contains \(x\), it reveals \(N_G(x)\cap B\) exactly.

### Proof

The graph induced by \(\{x\}\cup B\) is a star centered at \(x\), together with isolated vertices in \(B\setminus N(x)\). Its maximal independent sets are of the following forms:

- \(B\), possible exactly when \(B\cap N(x)\neq\varnothing\);
- \(\{x\}\cup(B\setminus N(x))\).

In particular, the answer is the whole set \(\{x\}\cup B\) if and only if \(B\cap N(x)=\varnothing\). If \(x\) is returned, the omitted members of \(B\) are exactly the neighbors of \(x\) in \(B\). ∎

Consequently, on a known independent set \(A\), MIS queries simulate ordinary OR group tests for the unknown set \(N(x)\cap A\).

### Lemma 2.2

If \(|A|=m\) and \(d=|N(x)\cap A|\), then \(N(x)\cap A\) can be recovered using
\[
O\!\left(d\log\frac{em}{d}\right)
\]
MIS queries.

### Proof

Use the standard balanced binary-splitting group-testing procedure, with Lemma 2.1 supplying each OR test. In the balanced binary partition tree, at depth \(i\), at most \(\min(2^i,d)\) nodes can contain a neighbor. Testing the children of positive nodes therefore costs
\[
O\!\left(d+d\log\frac md\right).
\]
The extra information obtained when the oracle returns an MIS containing \(x\) can only reduce this number. ∎

---

## 3. Recovering one complete neighborhood

### Proposition 3.1

For a specified vertex \(v\), its entire neighborhood can be recovered deterministically in
\[
O\!\left(\Delta\log\frac{en}{\Delta}\right)
\]
adaptive MIS queries.

### Algorithm

Maintain a set \(U\subseteq V\setminus\{v\}\) of vertices whose adjacency to \(v\) is still unknown. Initially \(U=V\setminus\{v\}\).

While \(|U|>2\Delta\), query
\[
S=\{v\}\cup U
\]
and let \(I\) be the returned MIS.

- **Case 1: \(v\in I\).**  
  Every vertex of \(I\setminus\{v\}\) is a nonneighbor of \(v\). Remove those vertices from \(U\).

- **Case 2: \(v\notin I\).**  
  By maximality, \(I\cap N(v)\neq\varnothing\). The set \(I\) is independent. Apply Lemma 2.2 to recover all of \(I\cap N(v)\), thereby classifying every vertex in \(I\). Remove all of \(I\) from \(U\).

When \(|U|\leq 2\Delta\), query every pair \(\{v,u\}\), \(u\in U\). Such a query returns both vertices exactly when \(uv\notin E(G)\).

### Correctness

Every removed vertex is classified correctly:

- in Case 1 it co-occurs with \(v\) in an independent set;
- in Case 2 Lemma 2.2 exactly recovers its adjacency to \(v\);
- the final pair queries are exact.

Thus, on termination, every pair \(vu\) has been classified.

### Query bound

Let \(m=|U|>2\Delta\). Since \(I\) is a maximal independent set in a graph of maximum degree at most \(\Delta\),
\[
|I|\geq \frac{m+1}{\Delta+1}.
\]

If \(v\notin I\), all \(|I|\) vertices are removed. If \(v\in I\), then
\[
|I|-1\geq \frac{m-\Delta}{\Delta+1}
          \geq \frac{m}{2(\Delta+1)}.
\]
Hence every main iteration decreases \(m\) by at least a \(1/[2(\Delta+1)]\) fraction. The number of main iterations is therefore
\[
O\!\left(\Delta\log\frac{en}{\Delta}\right).
\]

It remains to sum the group-testing costs from Case 2. Let the independent sets handled in those rounds have sizes \(m_1,\dots,m_t\), and put
\[
d_i=|N(v)\cap I_i|.
\]
These sets are disjoint, each \(d_i\geq1\), and
\[
\sum_i m_i\leq n,\qquad \sum_i d_i\leq\Delta.
\]
By the log-sum inequality,
\[
\sum_i d_i\log\frac{e m_i}{d_i}
 \leq d\log\frac{e\sum_i m_i}{d}
 \leq \Delta\log\frac{en}{\Delta},
\]
where \(d=\sum_i d_i\). The final pair-testing phase costs at most \(2\Delta\) queries. This proves the proposition. ∎

---

## 4. Reconstructing the whole graph

### Theorem 4.1

Every \(n\)-vertex graph of maximum degree at most \(\Delta\) can be reconstructed by a deterministic adaptive algorithm using
\[
O\!\left(n\Delta\log\frac{en}{\Delta}\right)
\]
MIS queries.

### Proof

Process the vertices one at a time. When processing \(v\), apply Proposition 3.1 only inside the set of vertices not yet processed, thereby recovering every edge from \(v\) to a later vertex. Then delete \(v\) from further consideration.

If \(r\) vertices remain, the cost is
\[
O\!\left(\Delta\log\frac{er}{\Delta}\right)
\]
until \(r\leq2\Delta\), after which all remaining pairs may be queried directly. Therefore
\[
\sum_{r=2\Delta+1}^{n}
 O\!\left(\Delta\log\frac{er}{\Delta}\right)
 +O(\Delta^2)
 =
 O\!\left(n\Delta\log\frac{en}{\Delta}\right).
\]
Every edge is determined when its first endpoint is processed. ∎

### Corollary 4.2: a genuine subcubic parameter range

Assume \(n\geq2\Delta\). Then
\[
\frac{n\Delta\log(en/\Delta)}
     {\Delta^3\log(n/\Delta)}
 =
 \frac{n}{\Delta^2}
 \frac{\log(en/\Delta)}{\log(n/\Delta)}.
\]
The logarithmic quotient is bounded when \(n/\Delta\geq2\). Hence, if
\[
2\Delta\leq n=o(\Delta^2),
\]
the algorithm uses
\[
o\!\left(\Delta^3\log\frac n\Delta\right)
\]
queries.

This is only a restricted parameter range, but it improves the trivial pair-query range \(n=o(\Delta^{3/2})\) to essentially \(n=o(\Delta^2)\).

---

## 5. Finishing from a bounded-degree transcript supergraph

Given a transcript, define the unresolved-pair graph \(K\) by
\[
uv\in E(K)
\quad\Longleftrightarrow\quad
u\text{ and }v\text{ have never co-occurred in a returned MIS}.
\]
Every true edge remains in \(K\), so
\[
E(G)\subseteq E(K).
\]

### Proposition 5.1

If \(\Delta(K)\leq D\), then \(G\) can be reconstructed using at most
\[
2D(D+1)=O(D^2)
\]
additional MIS queries.

### Proof

Properly color the square of the line graph \(L(K)^2\). Its vertices are the edges of \(K\); two edges conflict when they share an endpoint or when an endpoint of one is adjacent in \(K\) to an endpoint of the other.

For an edge \(uv\), every conflicting edge is incident to a vertex in
\[
N_K[u]\cup N_K[v],
\]
so the conflict degree is less than \(2D(D+1)\). A greedy coloring therefore uses at most \(2D(D+1)\) colors.

Every color class \(M\) is an induced matching in \(K\). Query the set \(S\) of all endpoints of \(M\). Since \(G\subseteq K\), the graph \(G[S]\) is a submatching of \(M\). Thus:

- if \(e=xy\in M\cap E(G)\), every returned MIS contains exactly one of \(x,y\);
- if \(e\in M\setminus E(G)\), both \(x,y\) are isolated in \(G[S]\), so every returned MIS contains both.

One query therefore determines every edge in \(M\). Processing all color classes determines every edge of \(K\), while pairs outside \(K\) are already certified nonedges. ∎

This gives a precise reduced target for the open problem:

> It would suffice to produce, with subcubic query cost, a transcript whose unresolved-pair graph has maximum degree \(O(\Delta)\).

I do not know how to achieve this deterministically when \(n\gg\Delta^2\).

---

## 6. A bounded-degree hypothesis can be tested efficiently

The following related primitive may be useful in a future adaptive strategy.

### Proposition 6.1

Given any known graph \(H\) of maximum degree \(D\), there is a deterministic adaptive procedure using \(O(D^2\log n)\) queries which either:

1. reconstructs \(G\), provided \(E(G)\subseteq E(H)\); or
2. returns an explicit edge in \(E(G)\setminus E(H)\).

### Proof

First construct a family \(\mathcal F\) of \(O(D^2\log n)\) independent sets of \(H\) such that every nonedge of \(H\) is contained in some member of \(\mathcal F\).

Such a family exists by the following probabilistic argument. Choose \(Z\subseteq V\) by independently retaining each vertex with probability \(p=1/(2D)\), and put
\[
I(Z)=\{v\in Z:N_H(v)\cap Z=\varnothing\}.
\]
Then \(I(Z)\) is \(H\)-independent. For a fixed nonedge \(uv\) of \(H\),
\[
\Pr(u,v\in I(Z))
 \geq p^2(1-p)^{2D}
 \geq \frac{1}{16D^2}.
\]
Thus \(O(D^2\log n)\) independent samples cover all at most \(n^2\) nonedges with positive probability. Since \(H\) is known, a suitable family can be found deterministically by exhaustive search; no efficiency claim is needed here.

Query each \(I\in\mathcal F\).

- If every answer is the whole set \(I\), then \(G[I]\) is edgeless for every \(I\). Since every nonedge of \(H\) is covered, \(E(G)\subseteq E(H)\). Proposition 5.1 then reconstructs \(G\).

- Otherwise, suppose the answer to \(I\) is \(J\subsetneq I\). Pick \(x\in I\setminus J\). By maximality, \(x\) has a neighbor in \(J\). Since \(J\) is independent, Lemma 2.1 and binary search find such a neighbor in \(O(\log n)\) queries. Because \(I\) was \(H\)-independent, this edge is not in \(H\).

This proves the proposition. ∎

The missing ingredient is a way to update the hypothesis after a counterexample while bounding the number of failed hypotheses independently of \(n\). Naively adding one counterexample at a time can require \(\Theta(n\Delta)\) iterations.

---

## 7. A subcubic special class: star forests

There is also a clean special case where the cubic dependence drops by one power.

### Proposition 7.1

Suppose a bipartition \(V=A\cup B\) is known, there are no edges inside \(A\) or \(B\), every \(a\in A\) has degree at most \(\Delta\), and every \(b\in B\) has degree at most one. Then \(G\) can be reconstructed deterministically and non-adaptively with
\[
O(\Delta^2\log n)
\]
MIS queries.

### Proof

Choose a random query \(S=X\cup Y\) by including each \(a\in A\) independently with probability \(1/2\), and each \(b\in B\) independently with probability
\[
p=\frac1{\Delta+1}.
\]

Fix a possible cross nonedge \(ab\). Let \(C=N(a)\), with \(|C|\leq\Delta\), and let \(c\) be the unique neighbor of \(b\), if one exists. Since \(ab\) is a nonedge, \(c\neq a\).

The event
\[
a,b\in S,\qquad C\cap S=\varnothing,\qquad c\notin S
\]
has probability at least
\[
\frac12\cdot p\cdot\frac12\cdot(1-p)^\Delta
 \geq \frac{c_0}{\Delta}
\]
for an absolute constant \(c_0>0\). On this event, both \(a\) and \(b\) are isolated in \(G[S]\), so every returned MIS contains both.

It is enough to require this property simultaneously for every tuple
\[
(a,b,C,c),
\qquad |C|\leq\Delta.
\]
There are at most \(n^{\Delta+4}\) such tuples. Therefore \(q=O(\Delta^2\log n)\) independent random queries satisfy all requirements with positive probability. As before, a deterministic family can be found by exhaustive search.

After all queries, declare \(ab\) an edge exactly when \(a,b\) never co-occurred in an answer. True edges never co-occur, and every nonedge is forced to co-occur by one of the queries. ∎

This does not extend directly to general bounded-degree bipartite graphs: for a nonedge \(ab\), one must then simultaneously exclude up to \(\Delta\) neighbors of each endpoint, restoring the usual cubic cover-free-family calculation.

---

## 8. Remaining gap

The results above leave the principal case unresolved:

\[
n\gtrsim \Delta^2,
\]
especially \(n/\Delta\to\infty\), where
\[
n\Delta\log(en/\Delta)
\]
is no better than the known \(O(\Delta^3\log(n/\Delta))\) bound.

The strongest concrete reduction obtained here is Proposition 5.1. Once the graph of unresolved pairs has maximum degree \(O(\Delta)\), only \(O(\Delta^2)\) further queries are needed. What remains is a deterministic adaptive “sparsification” phase producing such a bounded-degree supergraph in \(o(\Delta^3\log(n/\Delta))\) queries. Neither the single-vertex routine nor the bounded-degree hypothesis tester supplies that phase without an unwanted factor depending linearly on \(n\).

Accordingly, the full Problem 5.3 remains open under the stated model.