```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Ordered orientations of rook graphs yield claw- and directed-triangle-free examples with dichromatic number Ω(√n), disproving forest-plus-hero sufficiency and giving an additional necessary obstruction class.",
  "would_publish": false,
  "caveats": "No full characterization; the host convention matters, and the core counterexample overlaps the unverified 2026 claim reported in the prompt."
}
```

## 1. Statement of the partial result

The prompt alternates between digraphs and oriented graphs. The construction below consists of oriented graphs and therefore applies under either convention. If all loopless digraphs, including digons, are allowed as hosts, the corresponding forbidden family should additionally contain a bidirected clique; this is addressed below.

Write \(\vec\alpha(D)\) for the maximum order of an induced acyclic subdigraph of \(D\). Thus
\[
\vec\chi(D)\geq \frac{|V(D)|}{\vec\alpha(D)}.
\]

The main result is the following.

### Theorem 1
For every integer \(n\geq 49\), there is an orientation \(D_n\) of the rook graph
\[
R_n=L(K_{n,n})
\]
with the following properties:

1. the underlying graph of \(D_n\) is claw-free;
2. \(D_n\) has no directed triangle \(\vec C_3\);
3. 
   \[
   \vec\alpha(D_n)<7n^{3/2},
   \qquad
   \vec\chi(D_n)>\frac{\sqrt n}{7}.
   \]

Consequently, for every orientation \(S\) of the claw \(K_{1,3}\),
\[
\operatorname{Forb}_{\mathrm{ind}}(S,\vec C_3)
\]
has unbounded dichromatic number.

More generally, the same conclusion holds whenever \(S\) is an oriented forest whose underlying forest has maximum degree at least \(3\), and \(\vec C_3\) may be replaced by any nontransitive tournament.

The proof is self-contained and probabilistic.

---

## 2. Counting acyclic orientations

We use the following elementary bound.

### Lemma 2
If \(G\) is a finite simple graph and \(a(G)\) is its number of acyclic orientations, then
\[
a(G)\leq \prod_{v\in V(G)}\bigl(d_G(v)+1\bigr).
\]

#### Proof
An acyclic orientation is uniquely determined by its labeled indegree sequence.

Indeed, suppose two acyclic orientations \(A,A'\) have the same indegree at every vertex. Consider the edges on which they differ, oriented as in \(A\). At every vertex, the number of these edges directed inwards equals the number directed outwards, because reversing all differing edges preserves the total indegree. Thus, if there is at least one differing edge, the resulting nonempty balanced digraph contains a directed cycle. This would be a directed cycle in \(A\), a contradiction.

Hence the map
\[
A\longmapsto (d^-_A(v):v\in V(G))
\]
is injective. Since \(d^-_A(v)\in\{0,\ldots,d_G(v)\}\), the stated bound follows. \(\square\)

---

## 3. Random ordered orientations of the rook graph

Identify \(V(R_n)\) with the cells \([n]\times[n]\). Two cells are adjacent exactly when they lie in a common row or a common column.

For every row \(i\), choose independently and uniformly a linear order of its \(n\) cells, and orient all row edges from earlier to later. Independently, do the same in every column. Denote the resulting random orientation by \(D_n\).

Fix a set \(X\subseteq[n]\times[n]\) of size \(m\). Let
\[
r_i=|\{j:(i,j)\in X\}|,\qquad
c_j=|\{i:(i,j)\in X\}|.
\]
Let \(G_X=R_n[X]\).

The restrictions of the random row and column orders to \(X\) are independent and uniform among
\[
Q_X=\prod_{i=1}^n r_i!\prod_{j=1}^n c_j!
\]
possibilities.

Every acyclic orientation of \(G_X\) restricts to an acyclic orientation of each row and column clique. An acyclic tournament is transitive, so these restrictions determine unique row and column orders. Conversely, every acyclic outcome of the restricted orders is an acyclic orientation of \(G_X\). Therefore
\[
\Pr(D_n[X]\text{ is acyclic})
   =\frac{a(G_X)}{\prod_i r_i!\prod_j c_j!}.
\]

For a cell \((i,j)\in X\),
\[
d_{G_X}(i,j)=(r_i-1)+(c_j-1),
\]
and Lemma 2 gives
\[
a(G_X)\leq
\prod_{(i,j)\in X}(r_i+c_j-1).
\]

Using \(d!\geq(d/e)^d\) for \(d\geq1\), and omitting zero-degree terms,
\[
\prod_i r_i!\prod_j c_j!
 \geq e^{-2m}\prod_i r_i^{r_i}\prod_j c_j^{c_j}.
\]
Moreover,
\[
\prod_i r_i^{r_i}\prod_j c_j^{c_j}
 =\prod_{(i,j)\in X}r_i c_j.
\]
It follows that
\[
\begin{aligned}
\Pr(D_n[X]\text{ is acyclic})
&\leq
e^{2m}\prod_{(i,j)\in X}
 \frac{r_i+c_j-1}{r_i c_j}\\
&\leq
e^{2m}\prod_{(i,j)\in X}
 \left(\frac1{r_i}+\frac1{c_j}\right).
\end{aligned}
\]

By the arithmetic-geometric mean inequality,
\[
\prod_{(i,j)\in X}
 \left(\frac1{r_i}+\frac1{c_j}\right)
\leq
\left[
\frac1m\sum_{(i,j)\in X}
 \left(\frac1{r_i}+\frac1{c_j}\right)
\right]^m.
\]
But
\[
\sum_{(i,j)\in X}\frac1{r_i}
 =|\{i:r_i>0\}|\leq n,
\]
and similarly
\[
\sum_{(i,j)\in X}\frac1{c_j}\leq n.
\]
Thus
\[
\boxed{\Pr(D_n[X]\text{ is acyclic})
 \leq \left(\frac{2e^2n}{m}\right)^m.}
\tag{1}
\]

Taking a union bound over all \(m\)-subsets,
\[
\begin{aligned}
\Pr(\exists X,\ |X|=m,\ D_n[X]\text{ acyclic})
&\leq \binom{n^2}{m}
 \left(\frac{2e^2n}{m}\right)^m\\
&\leq
\left(\frac{en^2}{m}\right)^m
\left(\frac{2e^2n}{m}\right)^m\\
&=
\left(\frac{2e^3n^3}{m^2}\right)^m.
\end{aligned}
\tag{2}
\]

Set
\[
m=\left\lceil 7n^{3/2}\right\rceil.
\]
For \(n\geq49\), \(m\leq n^2\), and
\[
\frac{2e^3n^3}{m^2}
\leq \frac{2e^3}{49}<1.
\]
Therefore the probability in (2) is strictly less than \(1\). Some outcome has no acyclic set of order \(m\). For that outcome,
\[
\vec\alpha(D_n)\leq m-1<7n^{3/2},
\]
and hence
\[
\vec\chi(D_n)
\geq \frac{n^2}{\vec\alpha(D_n)}
>\frac{\sqrt n}{7}.
\]

This proves the quantitative part of Theorem 1.

---

## 4. The forbidden induced subgraphs

The remaining assertions hold for every choice of the row and column orders.

### Claw-freeness
For a cell \(x=(i,j)\), its neighbors divide into:

- cells in row \(i\);
- cells in column \(j\).

Each of these two sets is a clique. Among any three neighbors of \(x\), two therefore lie in the same one of these cliques and are adjacent. Thus \(R_n\) has no induced claw.

Consequently, \(D_n\) avoids every orientation of \(K_{1,3}\). More generally, it avoids every oriented forest whose underlying forest has a vertex of degree at least \(3\), since such a forest contains an induced claw.

### No directed triangle
Every triangle of \(R_n\) lies completely in one row or completely in one column. Indeed, if two vertices of the triangle lie in the same row, any third vertex adjacent to both must also lie in that row; the column case is symmetric.

Every row and every column is transitively oriented by construction. Hence \(D_n\) contains no directed triangle \(\vec C_3\).

Every nontransitive tournament contains a directed triangle. Therefore \(D_n\) avoids every nontransitive tournament as an induced subdigraph.

This completes the proof of Theorem 1. \(\square\)

---

## 5. A new necessary obstruction class

The construction is naturally expressed as a hereditary class.

Let \(\mathcal L_{\mathrm{ord}}\) be the following class of oriented graphs. Start with a simple bipartite graph \(B\). For each \(v\in V(B)\), choose a linear order on the edges incident with \(v\). The vertices of the resulting oriented graph are \(E(B)\); two are adjacent when the corresponding edges of \(B\) share an endpoint, and their adjacency is oriented according to the order at that endpoint.

Thus the underlying graph is \(L(B)\). The class is hereditary: deleting vertices of \(L(B)\) corresponds to deleting edges of \(B\) and restricting the local orders.

The graphs \(D_n\) above belong to \(\mathcal L_{\mathrm{ord}}\), with \(B=K_{n,n}\). Hence:

### Corollary 3
The hereditary class \(\mathcal L_{\mathrm{ord}}\) has unbounded dichromatic number. Therefore every heroic finite family \(\mathcal F\) must satisfy
\[
\mathcal F\cap\mathcal L_{\mathrm{ord}}\neq\varnothing.
\]

#### Proof
If \(\mathcal F\cap\mathcal L_{\mathrm{ord}}=\varnothing\), then no member of \(\mathcal F\) can occur as an induced subdigraph of a member of \(\mathcal L_{\mathrm{ord}}\), because the latter class is hereditary. Thus all the \(D_n\) are \(\mathcal F\)-free, while their dichromatic numbers are unbounded. \(\square\)

This condition is genuinely additional to merely requiring an oriented forest and a tournament.

Two useful membership observations are exact:

- A tournament belongs to \(\mathcal L_{\mathrm{ord}}\) if and only if it is transitive.
- An oriented forest belongs to \(\mathcal L_{\mathrm{ord}}\) if and only if its underlying forest is a linear forest.

For the first assertion, every directed triangle in \(L(B)\), with \(B\) bipartite, would have to arise from three edges incident with one vertex of \(B\), and these are transitively ordered. Thus members of \(\mathcal L_{\mathrm{ord}}\) have no \(\vec C_3\). Conversely, a transitive tournament is obtained from an ordered star.

For the second, line graphs are claw-free, so a forest in the class must have maximum degree at most \(2\). Conversely, every orientation of a path is obtained as the ordered line graph of a slightly longer path, and disjoint unions are handled componentwise.

It follows that:

### Corollary 4
Let \(S\) be an oriented forest and \(H\) a tournament. If \(\{S,H\}\) is heroic in the oriented-host setting, then at least one of the following holds:

1. the underlying forest of \(S\) has maximum degree at most \(2\);
2. \(H\) is transitive.

This is only a necessary condition, not a converse.

Taking \(H=\vec C_3\) is particularly relevant. Since every \(\vec C_3\)-free tournament is transitive,
\(\vec C_3\) is a tournament hero with bound \(1\). Nevertheless, for every orientation \(S\) of the claw,
\[
\{S,\vec C_3\}
\]
is not heroic. Thus the assertion that an arbitrary oriented star forest together with an arbitrary tournament hero always forms a heroic pair is false.

---

## 6. Other necessary conditions

For completeness, two standard necessary conditions can also be proved without invoking any open conjecture.

### 6.1 A heroic family must contain a tournament

Tournaments have unbounded dichromatic number. Indeed, in a random tournament on \(N\) vertices, the probability that a fixed \(s\)-set is transitive is
\[
\frac{s!}{2^{\binom{s}{2}}}.
\]
Hence
\[
\Pr(\text{there is a transitive }s\text{-set})
\leq
\binom Ns\frac{s!}{2^{\binom{s}{2}}}
\leq
\frac{N^s}{2^{\binom{s}{2}}}.
\]
For \(s=\lceil3\log_2N\rceil\), this tends to \(0\). Since acyclic subtournaments are exactly transitive subtournaments, there are tournaments with dichromatic number at least
\[
\frac{N}{3\log_2N+1}.
\]

If \(\mathcal F\) contains no tournament, every tournament is automatically \(\mathcal F\)-free. Thus \(\mathcal F\) cannot be heroic.

### 6.2 A finite heroic family must contain an oriented forest

We use the following probabilistic fact.

#### Lemma 5
For every \(k\) and \(g\), there is an oriented graph \(D\) such that
\[
\vec\chi(D)>k
\]
and the underlying graph of \(D\) has girth greater than \(g\).

#### Proof
Fix \(k,g\), with \(g\geq3\), and let \(N\) tend to infinity. Set
\[
p=N^{-1+1/(2g)}.
\]
For each unordered pair of vertices, independently put no arc with probability \(1-p\), and either of the two possible arcs with probability \(p/2\) each.

Let
\[
s=\left\lceil\frac{N}{2k}\right\rceil.
\]
For a fixed \(s\)-set and a fixed linear ordering of it, the probability that every present arc goes forward in the ordering is
\[
(1-p/2)^{\binom{s}{2}}.
\]
Thus
\[
\Pr(\text{there is an acyclic }s\text{-set})
\leq
\binom Ns s!(1-p/2)^{\binom{s}{2}}
\leq
\exp\left(s\log N-\frac p2\binom{s}{2}\right),
\]
which tends to \(0\), since \(ps\gg\log N\).

The expected number of underlying cycles of lengths at most \(g\) is at most
\[
\sum_{\ell=3}^g\frac{N^\ell p^\ell}{2\ell}
\leq gN^{1/2}.
\]
With probability tending to \(1\), there are fewer than \(N/2\) such cycles. Choose one vertex from every such cycle and delete the union of the chosen vertices. The resulting oriented graph has more than \(N/2\) vertices, underlying girth greater than \(g\), and still has no acyclic set of order \(s\). Its dichromatic number is therefore greater than \(k\). \(\square\)

Now suppose a finite \(\mathcal F\) contains no oriented forest. Members of \(\mathcal F\) containing a digon cannot occur in an oriented host, while every oriented member has an underlying cycle. Taking
\[
g\geq \max_{H\in\mathcal F}|V(H)|
\]
in Lemma 5 gives arbitrarily high-dichromatic oriented graphs avoiding every member of \(\mathcal F\). Hence \(\mathcal F\) is not heroic.

Combining these observations with Corollary 3, a finite heroic family in the oriented-host setting must meet each of:

1. the oriented forests;
2. the tournaments;
3. \(\mathcal L_{\mathrm{ord}}\).

These conditions are not claimed to be sufficient.

---

## 7. If arbitrary digraphs with digons are hosts

Let \(\overleftrightarrow K_t\) denote the complete bidirected digraph on \(t\) vertices. Since
\[
\vec\chi(\overleftrightarrow K_N)=N
\]
and every induced subdigraph of \(\overleftrightarrow K_N\) is another complete bidirected digraph, a heroic family for unrestricted loopless digraphs must also contain some \(\overleftrightarrow K_t\).

The rook construction is oriented and therefore avoids every \(\overleftrightarrow K_t\) with \(t\geq2\). Consequently, for every orientation \(S\) of the claw and every \(t\geq2\),
\[
\{\overleftrightarrow K_t,S,\vec C_3\}
\]
is not heroic in the unrestricted-digraph setting. Thus even adjoining the standard bidirected-clique obstruction does not restore the naive “bidirected clique + oriented forest + tournament hero” sufficiency criterion.

---

## 8. What remains open

This does not characterize heroic finite families. In particular:

- Meeting the forest, tournament, and ordered-bipartite-line obstruction classes is only necessary.
- The argument gives no converse when the forbidden forest is a linear forest or the forbidden tournament is transitive.
- The exponent \(\Omega(\sqrt n)=\Omega(|V(D_n)|^{1/4})\) is not asserted to be optimal.
- The catalog attributes essentially the claw/\(\vec C_3\) rook-graph phenomenon to an unverified 2026 preprint. I have not verified that document, so no claim of novelty or priority is made; the proof above is independent of that attribution.