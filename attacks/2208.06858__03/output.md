```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "Under two-sided positive association there is a uniform gap for α>3/7 and, for every α, on perfect or bounded-average-degree graphs, while disjoint triangles refute any merely pairwise or one-sided interpretation of positive correlation.",
  "would_publish": false,
  "caveats": "The omitted partition definition must imply the two orthant inequalities below; arbitrary graphs with α≤3/7 remain unresolved."
}
```

# Mathematical writeup

## 1. Probabilistic interface and an important ambiguity

Let \(G\) be a finite simple graph, with
\[
n=|V(G)|,\qquad a=\alpha(G),\qquad \beta=\bar\alpha(G)=a/n.
\]

The extracted statement does not reproduce the full definition of \(\alpha^*(G)\). The distinction between pairwise positive correlation and positive association is essential here.

Call a random set \(W\subseteq V(G)\) **two-sided \(1/2\)-orthant-positive** if every vertex has marginal \(1/2\) and, for every \(A\subseteq V(G)\),
\[
\Pr(A\subseteq W)\ge 2^{-|A|}
\quad\text{and}\quad
\Pr(A\cap W=\varnothing)\ge 2^{-|A|}.
\tag{1}
\]
A positively associated family of Bernoulli\((1/2)\) indicators satisfies (1): the first inequality follows by iterating positive association for increasing events, and the second similarly for decreasing events.

Also, if \(V(G)\) is partitioned into cells and \(W\) is the union of independently chosen cells, each chosen with probability \(1/2\), then (1) holds. Indeed, if \(A\) meets \(c\le |A|\) cells, either event in (1) has probability \(2^{-c}\ge 2^{-|A|}\).

Define the broader relaxation
\[
\widehat\alpha_\pm(G)
   =\sup_{\mu}\frac{\mathbb E_\mu[\alpha(G[W])]}{n},
\tag{2}
\]
where the supremum is over all laws satisfying (1).

Thus, if every random set arising in the paper's partition definition satisfies (1), and if \(\alpha^*(G)\) is the corresponding supremum of normalized expected induced independence numbers, then
\[
\alpha^*(G)\le \widehat\alpha_\pm(G).
\tag{3}
\]
All bounds below would then apply to the source parameter. If the partition construction uses an auxiliary graph on \(V(G)^r\), one must additionally check that its normalization and independence ratio are the ones required in (3). This is the only definitional step not certified by the extracted statement.

---

## 2. A universal bound for \(\beta>3/7\)

### Proposition 2.1

For every graph \(G\),
\[
\beta-\widehat\alpha_\pm(G)
   \ge \max\left\{0,\frac{7\beta-3}{8}\right\}.
\tag{4}
\]

Consequently, under the transfer condition (3),
\[
\varepsilon^*(\alpha)\ge \frac{7\alpha-3}{8}>0
\qquad\text{for every }\alpha\in(3/7,1/2).
\tag{5}
\]

### Proof

Let \(M\) be a maximum matching of \(G\), of size \(\nu(G)\). For a realization of \(W\), let
\[
Z_M(W)=|\{uv\in M:u,v\in W\}|.
\]
Because the edges of \(M\) are vertex-disjoint, every independent set in \(G[W]\) must omit at least one endpoint of each edge counted by \(Z_M(W)\). Hence
\[
\alpha(G[W])\le |W|-Z_M(W).
\tag{6}
\]
By the marginal condition, \(\mathbb E|W|=n/2\). By the first inequality in (1),
\[
\Pr(u,v\in W)\ge \frac14
\]
for every \(uv\in M\). Therefore
\[
\mathbb E Z_M(W)\ge \frac{\nu(G)}4
\]
and
\[
\mathbb E\alpha(G[W])
   \le \frac n2-\frac{\nu(G)}4.
\tag{7}
\]

The unmatched vertices of a maximum matching form an independent set: otherwise an edge joining two unmatched vertices could be added to the matching. Thus
\[
n-2\nu(G)\le a,
\qquad\text{so}\qquad
\nu(G)\ge \frac{n-a}{2}.
\tag{8}
\]
Combining (7) and (8),
\[
\frac{\mathbb E\alpha(G[W])}{n}
 \le \frac12-\frac{1-\beta}{8}
 =\frac{3+\beta}{8}.
\]
Subtracting from \(\beta\) gives
\[
\beta-\frac{\mathbb E\alpha(G[W])}{n}
 \ge \frac{7\beta-3}{8}.
\]
The pointwise inequality \(\alpha(G[W])\le a\) supplies the additional lower bound \(0\). This proves (4). Since the right side is increasing in \(\beta\), (5) follows. ∎

This covers a nontrivial upper portion of the conjectured interval without any degree or structural assumption.

---

## 3. A vacant-neighborhood bound

The following estimate is useful when a maximum independent set contains many vertices of moderate degree.

### Proposition 3.1

For every maximum independent set \(I\) of \(G\),
\[
\beta-\widehat\alpha_\pm(G)
 \ge \frac1n\sum_{v\in I}2^{-(d(v)+1)}.
\tag{9}
\]

### Proof

For a realization of \(W\), define
\[
X(W)=\{v\in I:W\cap N[v]=\varnothing\}.
\]
Let \(J\) be any independent set of \(G[W]\). For every \(v\in X(W)\), no vertex of \(J\) is adjacent to \(v\), and \(v\notin J\). Since \(X(W)\subseteq I\), the set
\[
J\cup X(W)
\]
is independent in \(G\). Maximality of \(a=\alpha(G)\) therefore gives
\[
|J|+|X(W)|\le a.
\]
Taking \(J\) maximum in \(G[W]\),
\[
a-\alpha(G[W])\ge |X(W)|.
\]
After taking expectations and using the second inequality in (1),
\[
a-\mathbb E\alpha(G[W])
 \ge \sum_{v\in I}\Pr(W\cap N[v]=\varnothing)
 \ge \sum_{v\in I}2^{-|N[v]|},
\]
which is (9). ∎

### Corollary 3.2: bounded maximum degree

If \(\Delta(G)\le\Delta\), then
\[
\beta-\widehat\alpha_\pm(G)
 \ge \beta\,2^{-(\Delta+1)}.
\tag{10}
\]
Thus, for graphs with \(\bar\alpha(G)\ge\alpha\) and maximum degree at most \(\Delta\),
\[
\bar\alpha(G)-\alpha^*(G)
 \ge \alpha\,2^{-(\Delta+1)}
\]
under (3).

### Corollary 3.3: bounded average degree

Suppose the average degree of \(G\) is at most \(D\). Since \(I\) is independent,
\[
\sum_{v\in I}d(v)=e(I,V\setminus I)\le e(G)\le \frac{Dn}{2}.
\]
By convexity of \(x\mapsto2^{-x}\),
\[
\frac1a\sum_{v\in I}2^{-(d(v)+1)}
 \ge 2^{-1-\frac1a\sum_{v\in I}d(v)}
 \ge 2^{-1-D/(2\beta)}.
\]
Hence
\[
\beta-\widehat\alpha_\pm(G)
 \ge \beta\,2^{-1-D/(2\beta)}.
\tag{11}
\]
Uniformly over \(\beta\ge\alpha\),
\[
\beta-\widehat\alpha_\pm(G)
 \ge \alpha\,2^{-1-D/(2\alpha)}>0.
\tag{12}
\]

Thus the conjectured positivity holds for every fixed \(\alpha>0\) on any class of uniformly bounded average degree.

---

## 4. Graphs admitting an optimal clique partition

### Proposition 4.1

Suppose \(V(G)\) can be partitioned into exactly \(a=\alpha(G)\) nonempty cliques. Then
\[
\beta-\widehat\alpha_\pm(G)
 \ge \beta\,2^{-1/\beta}.
\tag{13}
\]

In particular, this applies to every perfect graph.

### Proof

Let
\[
V(G)=C_1\sqcup\cdots\sqcup C_a,
\qquad s_i=|C_i|.
\]
Every independent set meets each \(C_i\) in at most one vertex. Therefore
\[
\alpha(G[W])
 \le |\{i:W\cap C_i\ne\varnothing\}|.
\]
Consequently,
\[
a-\mathbb E\alpha(G[W])
 \ge \sum_{i=1}^a\Pr(W\cap C_i=\varnothing)
 \ge \sum_{i=1}^a2^{-s_i}.
\tag{14}
\]
Since \(\sum_i s_i=n\), convexity gives
\[
\sum_{i=1}^a2^{-s_i}
 \ge a\,2^{-n/a}.
\]
Dividing by \(n\) yields (13).

For a perfect graph,
\[
\chi(\overline G)=\omega(\overline G)=\alpha(G),
\]
so a proper coloring of \(\overline G\) partitions \(V(G)\) into \(\alpha(G)\) cliques of \(G\). ∎

The order of this bound is sharp in this class. If \(G\) is a disjoint union of equal cliques of size \(q\), then \(\beta=1/q\), and for independent vertex sampling,
\[
\frac{\mathbb E\alpha(G[W])}{n}
 =\frac1q(1-2^{-q}),
\]
so the normalized gap is exactly
\[
\frac{2^{-q}}q=\beta\,2^{-1/\beta}.
\]

---

## 5. A conditional counterexample under weak “positive correlation”

If the source uses only pairwise nonnegative correlations, or only the first inequality in (1), then the conjecture is false.

Let
\[
G=mK_3.
\]
Then \(n=3m\), \(\alpha(G)=m\), and \(\bar\alpha(G)=1/3\).

Independently in each triangle, choose \(W\) according to the four equiprobable states
\[
111,\qquad 100,\qquad 010,\qquad 001.
\tag{15}
\]
Then:

1. Every vertex has marginal \(1/2\).
2. Every pair of vertices in the same triangle is jointly present with probability \(1/4\), so the indicators are pairwise independent.
3. More strongly, for every set \(A\) of vertices,
   \[
   \Pr(A\subseteq W)\ge 2^{-|A|}.
   \]
   Within one triangle, the relevant probabilities for one, two, or three prescribed vertices are respectively
   \[
   \frac12,\quad\frac14,\quad\frac14,
   \]
   and different triangles are independent.
4. Every triangle contains at least one selected vertex. Hence
   \[
   \alpha(G[W])=m=\alpha(G)
   \]
   deterministically.

Thus, if the law (15) is admissible in the definition of \(\alpha^*(G)\), then
\[
\alpha^*(G)=\bar\alpha(G)=\frac13
\]
and therefore
\[
\varepsilon^*(\alpha)=0
\qquad\text{for every }0<\alpha\le\frac13.
\]

However, (15) is not positively associated in the full sense, since for each triangle
\[
\Pr(W\cap V(K_3)=\varnothing)=0<\frac18.
\]
It also cannot arise as a simple random union of independently activated partition cells. Consequently, this is not yet a counterexample to the source conjecture unless its partition-generated class permits such a law. It is, however, a decisive check on the exact meaning of “positively correlated.”

---

## 6. What remains open

Under the natural two-sided/full-association interpretation, the arguments prove:

- the conjectured uniform positivity for every \(\alpha>3/7\);
- positivity for every \(\alpha>0\) on perfect graphs;
- positivity for every \(\alpha>0\) on graph classes of bounded average degree.

They do not address arbitrary dense, imperfect graphs when
\[
0<\alpha\le\frac37.
\]
Moreover, because the extracted prompt suppresses the exact partition definition on \(V(G)^r\), one must verify that its admissible random subsets satisfy both inequalities in (1), and that the auxiliary normalization preserves the relevant independence ratio. Without that verification, the disjoint-triangle construction shows that the wording “positively correlated” alone is insufficient.