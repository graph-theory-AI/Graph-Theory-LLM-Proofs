```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted conjecture remains open, but the entire exceptional family is forced in sparse high-girth backedge models, and D5-free tournaments satisfy a useful nesting lemma relative to every transitive spine.",
  "would_publish": false,
  "caveats": "The host-order sparsity and girth hypotheses are not known to follow from H-freeness, so even the case H=D5 is not settled."
}
```

# 1. Statement and notation

Write \(x\to y\) when \(xy\) is an edge of a tournament directed from \(x\) to \(y\). For a numbering
\[
v_1,\ldots ,v_n
\]
of a tournament \(G\), its backedge graph \(B(G)\) is the undirected graph in which \(v_iv_j\) is an edge, for \(i<j\), exactly when \(v_j\to v_i\) in \(G\).

A pure pair is a pair of disjoint sets \(A,B\) such that \(A\to B\).

The exceptional tournament \(D_5\) can be numbered \(d_1,\ldots,d_5\) so that its backward pairs are
\[
d_1d_4,\qquad d_1d_5,\qquad d_2d_5. \tag{1}
\]
Thus its backedge graph is a four-vertex path
\[
d_4-d_1-d_5-d_2
\]
together with the isolated vertex \(d_3\). This is the regular five-vertex tournament.

The open question asks whether every tournament \(H\) admitting a numbering with at most three backedges has the strong Erdős–Hajnal property, including the case in which \(H\) contains \(D_5\).

I do not resolve the unrestricted question. I prove two partial results:

1. Every tournament in the omitted family has a precise ordered normal form: its backedge graph is the path in (1) plus isolated vertices.
2. Such an \(H\) is forced in every ordered host whose backedge graph is sufficiently sparse and has no triangle or four-cycle, unless the host already has a linear pure pair.

The second result rules out the most direct sparse high-girth backedge construction as a possible counterexample.

---

# 2. Normal form of the omitted family

## Lemma 2.1

Every numbering of \(D_5\) has at least three backedges. If it has exactly three, then, after denoting the vertices in numbered order by \(d_1,\ldots,d_5\), the backedges are exactly
\[
d_1d_4,\ d_1d_5,\ d_2d_5.
\]

### Proof

Every vertex of \(D_5\) has outdegree and indegree two.

In any numbering, the first vertex has two inneighbors, and both corresponding edges are backedges. Similarly, the last vertex has two outneighbors, and both corresponding edges are backedges. These two sets of backedges overlap in at most the edge joining the first and last vertices, so there are at least three backedges.

Suppose there are exactly three. Let \(\rho_i\) be the number of backedges from \(d_i\) to later vertices and \(\lambda_i\) the number of backedges from \(d_i\) to earlier vertices. Relative to the transitive orientation of the numbering, \(d_i\) would have outdegree \(5-i\). Since its actual outdegree is two,
\[
5-i-\rho_i+\lambda_i=2,
\]
or
\[
\rho_i-\lambda_i=3-i. \tag{2}
\]

The first vertex is incident with two backedges to later vertices and the last vertex with two backedges to earlier vertices. Since there are only three backedges, \(d_1d_5\) must be their common edge. Write the other two as \(d_1d_j\) and \(d_kd_5\). Equation (2) at \(i=2\) forces \(k=2\) and \(j\ne2\), while (2) at \(i=4\) forces \(j=4\). Hence the three edges are exactly those in (1). ∎

## Corollary 2.2

Let \(H\) have a numbering with at most three backedges, and suppose \(H\) contains \(D_5\). Then:

- \(H\) has exactly three backedges;
- all three lie in the copy of \(D_5\);
- relative to the five positions \(p_1<\cdots<p_5\) occupied by that copy, they are
  \[
  p_1p_4,\qquad p_1p_5,\qquad p_2p_5;
  \]
- every other vertex is isolated in the backedge graph.

Thus, as an unordered graph,
\[
B(H)\cong P_4\mathbin{\dot\cup} (|H|-4)K_1. \tag{3}
\]

This describes exactly the targets omitted by the \(D_5\)-free condition.

Notice also the following asymmetry. If \(D_5\) fails the strong EH-property, then every \(H\) in this omitted family fails it as well: every \(D_5\)-free tournament is automatically \(H\)-free. The converse is not valid, since an \(H\)-free tournament may contain \(D_5\).

---

# 3. A sparse high-girth backedge theorem

## Theorem 3.1

Let \(H\) be a tournament on \(h\ge5\) vertices with a numbering whose backedge graph has the form (3), in the positional form of Corollary 2.2.

Let \(G\) be a tournament on \(n>1\) vertices with a numbering such that its backedge graph \(B\):

1. contains no \(C_3\) and no \(C_4\); and
2. satisfies
   \[
   e(B)\le \frac{n^2}{800h^3}. \tag{4}
   \]

Then either \(G\) contains \(H\), or \(G\) has a pure pair \((A,C)\) with
\[
|A|,|C|\ge \frac{n}{40h}. \tag{5}
\]

### Proof

Set
\[
s=\frac{n}{40h},
\qquad
\delta=\frac1{20h^2}.
\]

If \(n\le40h\), every arc gives a pure pair of two singleton sets, and \(1\ge s\). We may therefore assume \(n>40h\).

Partition the numbering of \(G\) into \(h\) consecutive intervals
\[
V_1,\ldots,V_h
\]
whose sizes differ by at most one. Hence
\[
|V_i|\ge \left\lfloor \frac nh\right\rfloor
  >\frac{39n}{40h}. \tag{6}
\]

Let
\[
Z=\{v\in V(G):\deg_B(v)>\delta n\}
\]
and put \(W_i=V_i\setminus Z\). By (4),
\[
|Z|\delta n
   <\sum_{z\in Z}\deg_B(z)
   \le 2e(B)
   \le \frac{n^2}{400h^3}.
\]
Consequently,
\[
|Z|<\frac{n}{20h}.
\]
Together with (6), this gives
\[
|W_i|>\frac{37n}{40h} \qquad (1\le i\le h). \tag{7}
\]

Assume that \(G\) has no pure pair satisfying (5). We shall embed \(H\).

### Expansion observation

If \(i<j\), and \(X\subseteq W_i\), \(Y\subseteq W_j\) satisfy
\[
|X|,|Y|\ge s,
\]
then there is a \(B\)-edge between \(X\) and \(Y\). Indeed, if there were none, every tournament edge between \(X\) and \(Y\) would point forward in the numbering, so \(X\to Y\), contrary to the assumption that no pure pair of size \(s\) exists.

Let
\[
p_1<p_2<p_3<p_4<p_5
\]
be the positions in the numbering of \(H\) of its \(D_5\)-core.

Define
\[
A=\{a\in W_{p_1}:N_B(a)\cap W_{p_4}\ne\varnothing\}.
\]
If \(|W_{p_1}\setminus A|\ge s\), then \(W_{p_1}\setminus A\) and \(W_{p_4}\) are \(B\)-anticomplete, giving a pure pair. Hence
\[
|A|>|W_{p_1}|-s>\frac{36n}{40h}>s. \tag{8}
\]

Similarly, define
\[
E=\{e\in W_{p_5}:N_B(e)\cap W_{p_2}\ne\varnothing\}.
\]
Again,
\[
|E|>s. \tag{9}
\]

By the expansion observation, there is a \(B\)-edge \(ae\) with \(a\in A\) and \(e\in E\). Choose
\[
d\in W_{p_4}\cap N_B(a),
\qquad
b\in W_{p_2}\cap N_B(e).
\]
Thus, among \(a,b,d,e\), the graph \(B\) contains the three edges
\[
ad,\qquad ae,\qquad be. \tag{10}
\]

There are no further edges among these four vertices:

- if \(ab\in E(B)\), then \(a,b,e\) form a triangle;
- if \(de\in E(B)\), then \(d,a,e\) form a triangle;
- if \(bd\in E(B)\), then
  \[
  b-e-a-d-b
  \]
  is a four-cycle.

All are excluded by hypothesis. Therefore
\[
B[\{a,b,d,e\}]
\]
is exactly the path \(d-a-e-b\).

It remains to choose one vertex from every still-unfilled block, including \(V_{p_3}\), so that these additional vertices are isolated in the backedge graph induced by all chosen vertices.

All four already chosen vertices lie in their respective \(W_i\), and every vertex in every \(W_i\) has \(B\)-degree at most \(\delta n\). Suppose fewer than \(h\) vertices have been chosen. In an unfilled block \(W_i\), the union of the \(B\)-neighborhoods of all previously chosen vertices has size at most
\[
h\delta n=\frac{n}{20h}.
\]
By (7), this is strictly smaller than \(|W_i|\). We may therefore choose a vertex in \(W_i\) having no \(B\)-neighbor among the previously chosen vertices. Continuing greedily fills all \(h\) blocks.

The backedge graph on the selected vertices now has exactly the three edges in (10), in positions
\[
p_1p_4,\qquad p_1p_5,\qquad p_2p_5,
\]
and no others. Consequently the selected tournament is an ordered copy of \(H\), a contradiction. ∎

## Corollary 3.2

For each fixed target \(H\) in the omitted family, no sequence of \(H\)-free tournaments \(G_n\) can witness failure of the strong EH-property if \(G_n\) has a numbering whose backedge graph \(B_n\) satisfies
\[
\operatorname{girth}(B_n)\ge5
\quad\text{and}\quad
e(B_n)=o(n^2).
\]
Indeed, for all sufficiently large \(n\), Theorem 3.1 gives a pure pair of size at least \(n/(40|H|)\).

This rules out the direct analogue of the usual sparse high-girth backedge construction used when every ordering of the forbidden tournament has a cyclic backedge graph.

A slightly simpler variant follows from the same proof: condition (4) can be replaced by
\[
\Delta(B)\le \frac{n}{20h^2},
\]
with the same conclusion.

---

# 4. A \(D_5\)-specific nesting lemma

The next observation applies to arbitrary \(D_5\)-free tournaments, without sparsity or girth assumptions.

## Lemma 4.1

Let \(G\) be \(D_5\)-free, and let
\[
T=(t_1,\ldots,t_m)
\]
be a transitive subtournament, numbered so that \(t_i\to t_j\) for \(i<j\).

For \(1\le k\le m-1\), define
\[
R_k=
\left\{
x\notin T:
x\to t_i\ \text{for }i\le k,\quad
t_i\to x\ \text{for }i>k
\right\}.
\]
Then, whenever \(i<j\),
\[
R_j\to R_i. \tag{11}
\]

### Proof

Take \(x\in R_i\) and \(y\in R_j\), with \(i<j\). Suppose for a contradiction that \(x\to y\). Set
\[
a=t_i,\qquad b=t_j,\qquad c=t_{j+1}.
\]
These vertices exist because \(i\ge1\) and \(j\le m-1\).

We have
\[
a\to b\to c,\qquad a\to c,
\]
and, from the definitions of \(R_i,R_j\),
\[
x\to a,\qquad b,c\to x,
\]
\[
y\to a,b,\qquad c\to y.
\]
Together with \(x\to y\), the order
\[
a,b,c,x,y
\]
has precisely the backedges
\[
xa,\qquad ya,\qquad yb.
\]
This is \(D_5\), a contradiction. Hence \(y\to x\), proving (11). ∎

Define
\[
p(G)=\max\{\min(|A|,|B|):A\to B\}.
\]
Let
\[
r=\sum_{k=1}^{m-1}|R_k|,
\qquad
M=\max_k |R_k|.
\]
Lemma 4.1 immediately yields
\[
p(G)\ge
\max\left\{
\left\lfloor\frac m2\right\rfloor,\,
\left\lfloor\frac{r-M}{2}\right\rfloor,\,
\max_k \min\bigl(|R_k|,\max\{k,m-k\}\bigr)
\right\}. \tag{12}
\]

Indeed:

- splitting \(T\) into two consecutive pieces gives the first term;
- the blocks
  \[
  R_{m-1},R_{m-2},\ldots,R_1
  \]
  form a transitive chain of pure blocks, and a weighted cut gives the second term;
- \(R_k\to\{t_1,\ldots,t_k\}\) and
  \[
  \{t_{k+1},\ldots,t_m\}\to R_k,
  \]
  giving the third term.

Thus, in a hypothetical \(D_5\)-free tournament with \(p(G)<\eta |G|\), every transitive spine \(T\) has length less than about \(2\eta |G|\), and all but about \(2\eta |G|\) of the reverse-threshold vertices lie in a single class \(R_k\).

The limitation is important: vertices whose adjacency word to \(T\) has several alternations, such as \(1010\), are not controlled by this lemma. Controlling those multi-switch patterns appears to be one of the missing ingredients.

---

# 5. What remains open

Theorem 3.1 covers all targets excluded by the \(D_5\)-free hypothesis, but only for hosts admitting an ordering whose backedge graph is sparse and has no triangle or four-cycle. There is currently no argument here showing that an arbitrary \(H\)-free tournament has such an ordering.

Short cycles are not a cosmetic issue in the proof: they are exactly what may add chords to the path
\[
d-a-e-b,
\]
preventing it from being the three-edge backedge graph of \(D_5\). Likewise, a dense backedge graph need not have enough low-degree vertices to add the isolated vertices required for a larger \(H\).

Consequently:

- the strong EH-property of \(D_5\) itself is not proved;
- proving it would still not automatically prove the property for every larger \(H\) containing \(D_5\);
- no counterexample is produced.

The rigorous progress is therefore a restricted-host theorem ruling out the natural sparse high-girth counterexample mechanism, together with the nesting constraint in Lemma 4.1.