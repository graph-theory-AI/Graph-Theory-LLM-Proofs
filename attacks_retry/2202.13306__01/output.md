```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The hypotheses force F to be an oriented linear forest, and the transfer holds under a bounded neighborhood clique-cover condition, but the general implication remains unresolved.",
  "would_publish": false,
  "caveats": "Uses the oriented-graph and disjoint-union conventions; no novelty claim is made for the auxiliary probabilistic construction."
}
```

# An admissibility restriction and a restricted transfer theorem

I do not prove the full conjecture. The main additional restriction obtained here is that **the underlying graph of \(F\) must be a linear forest, not merely a forest**.

The key is a self-contained construction of directed-triangle-free orientations of claw-free graphs with arbitrarily large dichromatic number. I also obtain a positive transfer theorem when a closed neighborhood can be covered by a bounded number of cliques.

## 1. Conventions and partial results

All graphs are finite, and digraphs are simple oriented graphs. The operation \(+\) denotes **disjoint union**, as required by the motivation
\[
K_1+\overline K_t=\overline K_{t+1}.
\]
Write
\[
J=\Delta(1,1,H).
\]
Thus \(J\) consists of vertices \(x,y\), an induced copy \(Q\) of \(H\), and the arcs
\[
x\to y,\qquad y\to Q,\qquad Q\to x.
\]

Assume that \(F,H\) are nonempty. If empty digraphs are allowed, the cases \(F=\varnothing\) and \(H=\varnothing\) have trivial conclusions: respectively, the target class is \(K_1\)-free, or \(J\) is a single arc.

Let \(a,b\) be bounds supplied by the two hypotheses:
\[
\begin{aligned}
\vec\chi(D)&\le a &&\text{for every induced-\(\{F,J\}\)-free \(D\)},\\
\vec\chi(D)&\le b &&\text{for every induced-\(\{K_1+F,H\}\)-free \(D\)}.
\end{aligned}
\]

Here are the partial conclusions.

### Theorem 1

Under the hypotheses of the question:

1. \(H\) is a tournament.
2. The underlying graph of \(F\) is a disjoint union of paths, with isolated vertices allowed.
3. Suppose additionally that \(F\) is not a tournament. If \(D\) is induced-\(\{K_1+F,J\}\)-free and some closed neighborhood of its underlying graph is covered by \(q\) cliques, then
   \[
   \vec\chi(D)\le (q+1)a.
   \tag{1.1}
   \]
   In particular, the transfer holds on oriented graphs whose underlying graphs are quasi-line graphs, with bound \(3a\).

Here a quasi-line graph means a graph in which every open neighborhood is the union of at most two cliques. This includes all line graphs.

For \(H=K_1\), conclusion (1.1) improves to
\[
\vec\chi(D)\le a+q,
\tag{1.2}
\]
without the assumption that \(F\) is not a tournament.

The first conclusion and the forest part of the second conclusion were present in the previous attempt. I checked those arguments independently. The additional obstruction below rules out branching in \(F\).

---

## 2. Two triangle-free, high-dichromatic constructions

Because \(H\ne\varnothing\), the graph \(J\) contains a directed triangle. Consequently, every directed-triangle-free oriented graph is \(J\)-free.

### 2.1. Large underlying girth

We first record the forest obstruction with a complete proof.

### Lemma 2

For every pair of positive integers \(r,g\), with \(g\ge4\), there is an oriented graph \(D\) whose underlying graph has girth at least \(g\) and for which
\[
\vec\chi(D)>r.
\]

#### Proof

Fix \(r,g\), set
\[
\varepsilon=\frac1{2g},\qquad p=n^{-1+\varepsilon},
\]
and generate an undirected graph \(G(n,p)\). Orient each present edge independently and uniformly.

Put \(s=\lfloor n/(3r)\rfloor\). For a fixed \(s\)-vertex set \(S\), an acyclic orientation of \(D[S]\) has a topological ordering. For any prescribed ordering, each unordered pair must avoid being a backward arc, an event of probability \(1-p/2\). Therefore
\[
\Pr(D[S]\text{ is acyclic})
 \le s!(1-p/2)^{\binom{s}{2}}.
\]
A union bound gives
\[
\Pr(\text{some acyclic }s\text{-set})
 \le
 \binom ns s!\exp\!\left(-\frac p2\binom{s}{2}\right)
 \le
 \exp\!\left(s\log n-\frac p2\binom{s}{2}\right)
 =o(1).
\]
Indeed, the positive term is \(O(n\log n)\), while \(ps^2=\Theta(n^{1+\varepsilon})\).

The expected number of underlying cycles of length less than \(g\) is at most
\[
\sum_{\ell=3}^{g-1}\frac{(np)^\ell}{2\ell}
 =O\!\left(n^{\varepsilon(g-1)}\right)
 =o(n).
\]
Thus, for sufficiently large \(n\), there is an outcome having no acyclic \(s\)-set and fewer than \(n/3\) short underlying cycles.

Delete one vertex from each short cycle. The resulting graph has at least \(2n/3\) vertices and underlying girth at least \(g\). An acyclic \(r\)-coloring would have a color class of size at least \(2n/(3r)>s\), contrary to the choice of the outcome. ∎

### 2.2. Claw-free underlying graphs

The following construction supplies the stronger obstruction.

### Lemma 3

For every positive integer \(r\), there is an oriented graph \(D_r\) such that:

- \(D_r\) has no directed triangle;
- its underlying graph is claw-free;
- \(\vec\chi(D_r)>r\).

One may take \(D_r\) to have \(10000r^6\) vertices.

#### Construction

Set
\[
n=100r^3.
\]
Let \(R_n\) be the rook graph on
\[
[n]\times[n],
\]
where two distinct vertices are adjacent exactly when they lie in the same row or the same column. Equivalently,
\[
R_n=L(K_{n,n}).
\]

Independently choose a uniformly random total order on each of the \(n\) rows and each of the \(n\) columns. Orient an edge from the earlier endpoint to the later endpoint in its row or column order.

This is well-defined: two distinct cells share at most one row or column.

Every triangle of \(R_n\) lies entirely in one row or entirely in one column. Thus every triangle is transitively oriented, and \(D_r\) has no directed triangle.

Also, the neighbors of a cell are the union of its row clique and its column clique. They cannot contain three pairwise nonadjacent vertices, so \(R_n\) is claw-free.

It remains to show that some outcome has dichromatic number greater than \(r\).

#### An acyclic-orientation counting bound

For any undirected graph \(G\), an acyclic orientation is uniquely determined by its indegree sequence.

To see this, suppose two orientations have the same indegrees. Orient their disagreement edges as in the first orientation. At every vertex this disagreement digraph has equal indegree and outdegree. If it has an edge, it contains a directed cycle. Hence the first orientation cannot be acyclic.

It follows that the number of acyclic orientations of \(G\) is at most
\[
\prod_{v\in V(G)}(d_G(v)+1).
\tag{2.1}
\]

#### Bounding the probability that a fixed set is acyclic

Fix \(S\subseteq V(R_n)\), with \(|S|=s\). Write
\[
r_i=|S\cap\text{row }i|,
\qquad
c_j=|S\cap\text{column }j|.
\]
The restrictions of the random orders to these sets are independent and uniform. They produce
\[
M(S)=\prod_{i=1}^n r_i!\prod_{j=1}^n c_j!
\]
equally likely orientations of \(R_n[S]\).

Since \(R_n[S]\) has maximum degree at most \(2n-2\), (2.1) gives
\[
\Pr(D_r[S]\text{ is acyclic})
 \le \frac{(2n)^s}{M(S)}.
\tag{2.2}
\]

Using \(m!\ge(m/e)^m\), with the usual convention at \(m=0\), and convexity of \(x\log x\),
\[
\begin{aligned}
\log\prod_{i=1}^n r_i!
&\ge \sum_{i=1}^n(r_i\log r_i-r_i)\\
&\ge s\log(s/n)-s.
\end{aligned}
\]
The same calculation applies to the columns. Consequently,
\[
M(S)\ge \left(\frac{s}{en}\right)^{2s}.
\]
Substituting in (2.2),
\[
\Pr(D_r[S]\text{ is acyclic})
 \le \left(\frac{2e^2n^3}{s^2}\right)^s.
\tag{2.3}
\]

Now take
\[
s=\frac{n^2}{r},
\]
which is an integer. A union bound over all \(s\)-sets yields
\[
\begin{aligned}
\Pr(\text{some acyclic }s\text{-set})
&\le
\binom{n^2}{s}
\left(\frac{2e^2n^3}{s^2}\right)^s\\
&\le
\left(\frac{2e^3n^5}{s^3}\right)^s\\
&=
\left(\frac{2e^3r^3}{n}\right)^s\\
&=
\left(\frac{e^3}{50}\right)^s
<1.
\end{aligned}
\]
Thus there is an outcome with no acyclic \(s\)-set. An acyclic \(r\)-coloring of its \(n^2\) vertices would have a color class of size at least \(n^2/r=s\), a contradiction. ∎

This is a fully specified probabilistic construction, not a report of a computational experiment. I make no claim that the construction is new.

---

## 3. Deducing the linear-forest restriction

In fact, the two preceding lemmas prove a statement somewhat more general than the restriction needed here.

### Proposition 4

Let \(J\) be any oriented graph containing a directed triangle. If \(J\) is a hero in \(\mathrm{Forb}_{\mathrm{ind}}(F)\), then the underlying graph of \(F\) is a linear forest.

#### Proof

Suppose first that the underlying graph of \(F\) contains a cycle. Apply Lemma 2 with
\[
g>\lvert V(F)\rvert,\qquad g\ge4.
\]
The resulting graphs are \(F\)-free and directed-triangle-free, hence \(J\)-free, and have arbitrarily large dichromatic number. This contradicts the hero assumption. Therefore the underlying graph of \(F\) is a forest.

Suppose now that this forest has a vertex of degree at least three. That vertex and any three of its neighbors induce an undirected claw. Thus every induced copy of \(F\) contains an induced claw in its underlying graph.

The graphs from Lemma 3 are therefore \(F\)-free. They are also \(J\)-free, since they have no directed triangle. Again their unbounded dichromatic number contradicts the hero assumption.

Hence the underlying graph of \(F\) is a forest of maximum degree at most two: a linear forest. ∎

Applying Proposition 4 to \(J=\Delta(1,1,H)\) proves Theorem 1(2).

### Why \(H\) must be a tournament

Since \(F\ne\varnothing\), the graph \(K_1+F\) has a nonadjacent pair. Thus every tournament belongs to \(\mathrm{Forb}_{\mathrm{ind}}(K_1+F)\).

If \(H\) were not a tournament, every tournament would also be \(H\)-free. This would contradict the second hypothesis, because tournaments have unbounded dichromatic number.

For completeness, the latter fact follows directly from random tournaments. For
\[
t=\lceil3\log_2 N\rceil,
\]
a random \(N\)-vertex tournament satisfies
\[
\Pr(\text{some acyclic }t\text{-set})
 \le \binom Nt t!\,2^{-\binom t2}
 \le N^t2^{-\binom t2}
 =o(1).
\]
Therefore some tournaments have dichromatic number at least \(N/(t-1)\), which tends to infinity.

This proves Theorem 1(1). The second hypothesis also directly implies that \(H\) is a hero in tournaments; no characterization theorem is needed for this observation.

---

## 4. The local bounds supplied by the hypotheses

Let \(D\) be induced-\(\{K_1+F,J\}\)-free. For \(v\in V(D)\), define
\[
A(v)=\{u\ne v:\text{\(u\) and \(v\) are nonadjacent}\}.
\]

The basic local reduction from the previous attempt is valid.

### Lemma 5

For every vertex \(v\),
\[
\vec\chi(D[A(v)])\le a.
\tag{4.1}
\]
For every arc \(x\to y\),
\[
\vec\chi\bigl(D[N^+(y)\cap N^-(x)]\bigr)\le b.
\tag{4.2}
\]

#### Proof

An induced \(F\) in \(A(v)\), together with \(v\), would give an induced \(K_1+F\). Hence \(D[A(v)]\) is \(F\)-free. It is also \(J\)-free, so the first hero bound proves (4.1).

For an arc \(x\to y\), an induced copy \(Q\) of \(H\) in \(N^+(y)\cap N^-(x)\) would satisfy
\[
x\to y,\qquad y\to Q,\qquad Q\to x,
\]
and would give an induced \(J\). Thus this common cyclic neighborhood is \(H\)-free. It remains \(K_1+F\)-free by heredity, so the second hero bound proves (4.2). ∎

I do not infer a general local-to-global coloring theorem from these two bounds.

---

## 5. A positive transfer under bounded neighborhood clique cover

Let \(G_D\) be the underlying graph of \(D\). For an undirected graph \(G\), write \(\theta(G)\) for the minimum number of cliques covering its vertices. Overlapping covers and clique partitions give the same minimum.

### Proposition 6

Suppose \(F\) is not a tournament. Every induced-\(\{K_1+F,J\}\)-free oriented graph \(D\) satisfies
\[
\vec\chi(D)
\le
a\left(1+\min_{v\in V(D)}
\theta\bigl(G_D[N_{G_D}[v]]\bigr)\right).
\tag{5.1}
\]

#### Proof

Every tournament is \(F\)-free, because \(F\) has a nonadjacent pair. Consequently, the first hero hypothesis bounds the dichromatic number of every \(J\)-free tournament by \(a\).

Fix \(v\), and cover \(N_{G_D}[v]\) by \(q\) cliques. Partition this closed neighborhood into \(q\) sets, each contained in one of those cliques. Each set induces a \(J\)-free tournament and therefore has dichromatic number at most \(a\). Hence
\[
\vec\chi(D[N_{G_D}[v]])\le qa.
\]

The remaining vertices are exactly \(A(v)\), whose dichromatic number is at most \(a\) by Lemma 5. Using disjoint palettes gives
\[
\vec\chi(D)\le(q+1)a.
\]
Minimize over \(v\). ∎

In a quasi-line graph, every closed neighborhood is covered by at most two cliques: add the central vertex to the clique cover of its open neighborhood. Thus Proposition 6 gives
\[
\boxed{\vec\chi(D)\le3a}
\]
on that subclass.

This proves Theorem 1(3), and uses only the first hero hypothesis.

When \(H=K_1\), we have \(J=\vec C_3\). Every \(J\)-free tournament is acyclic, so each clique in the preceding proof needs only one color, regardless of \(F\). Consequently,
\[
\vec\chi(D)\le
a+\min_v\theta\bigl(G_D[N_{G_D}[v]]\bigr),
\]
which proves (1.2).

---

## 6. Why these results do not finish the conjecture

### 6.1. The rook-graph construction is not a counterexample

The construction in Lemma 3 has large antineighborhood dichromatic number as well as large global dichromatic number.

Indeed, use an outcome with no acyclic \(s\)-set, where \(s=n^2/r\). Every vertex has exactly \((n-1)^2\) nonneighbors. Moreover,
\[
(n-1)^2-(r-1)(s-1)
=\frac{(n-r)^2}{r}>0.
\]
Since every acyclic set has size at most \(s-1\), every antineighborhood requires at least \(r\) colors.

Thus, for a fixed admissible pair \(F,J\) with bound \(a\), these examples cannot be \(K_1+F\)-free once \(r>a\), by Lemma 5. They establish the branching obstruction on \(F\), but do not disprove the transfer.

### 6.2. Neighborhood clique-cover numbers need not be bounded

The hypotheses do not force the parameter in Proposition 6 to be bounded.

For example, take \(F=\overline K_2\) and \(H=K_1\). Let \(Q\) be a triangle-free undirected graph of large ordinary chromatic number, put \(G=\overline Q\), and orient \(G\) acyclically. The resulting \(D\) is \(J\)-free and has independence number at most two, so it is \(K_1+F\)-free.

Nevertheless, for every vertex \(v\),
\[
\begin{aligned}
\theta(G[N_G[v]])
&=\chi\bigl(Q[V(Q)\setminus N_Q(v)]\bigr)\\
&\ge \chi(Q)-1,
\end{aligned}
\]
because \(N_Q(v)\) is independent in the triangle-free graph \(Q\). Hence all these local clique-cover numbers can be arbitrarily large—even though this particular \(D\) is acyclic.

So Proposition 6 cannot itself supply the general bound.

---

## 7. Conclusion

The rigorous progress is:

- Any nonvacuous instance has \(H\) a tournament and \(F\) an **oriented linear forest**.
- The exclusion of branching in \(F\) follows from an explicit probabilistic construction of triangle-free, claw-free orientations with unbounded dichromatic number.
- For non-tournament \(F\), the transfer holds with bound \((q+1)a\) whenever some closed neighborhood is covered by \(q\) cliques; in particular, it holds with bound \(3a\) on quasi-line underlying graphs.
- For \(H=K_1\), the corresponding bound is \(a+q\).

The remaining cases include arbitrary orientations of linear forests \(F\), including edgeless \(F\), on unrestricted underlying graphs. I have not supplied the global coloring argument needed for those cases.