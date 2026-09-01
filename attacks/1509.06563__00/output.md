```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains unresolved, but the case ν=1 is exact, bounded triangle-incidence admits a general extension of the triangle-free theorem, and any putative threshold has explicit and probabilistic lower bounds.",
  "would_publish": false,
  "caveats": "The essential case k≥4, ν≥2 with unbounded triangle incidence remains open."
}
```

## 1. Statement and notation

Call a set of holes with lengths
\[
a,a+1,\ldots,a+\nu-1 \qquad (a\ge 4)
\]
a **\(\nu\)-run**. Define
\[
F_{\nu,k}=\sup\{\chi(G):\omega(G)<k,\;G\text{ has no }\nu\text{-run}\}.
\]
The conjecture is precisely that \(F_{\nu,k}<\infty\) for all \(\nu>0\) and \(k\ge3\). If finite, the least threshold in the question is \(F_{\nu,k}+1\).

Let \(m_\nu\ge3\) be any threshold supplied by the Scott–Seymour triangle-free theorem: every triangle-free graph of chromatic number at least \(m_\nu\) has a \(\nu\)-run.

I do not prove that \(F_{\nu,k}\) is finite for \(k\ge4,\nu\ge2\). The results below isolate some tractable cases and a structural obstacle.

---

## 2. The case \(\nu=1\) is exact

### Proposition 2.1
For every \(k\ge3\),
\[
F_{1,k}=k-1.
\]
Equivalently, the optimal threshold is \(n(1,k)=k\).

### Proof
A graph with no hole is chordal. Every chordal graph has a perfect elimination ordering: every nonempty induced subgraph has a simplicial vertex. Inductively coloring along such an ordering gives
\[
\chi(G)=\omega(G).
\]
Thus, if \(\omega(G)<k\) and \(G\) has no hole, then \(\chi(G)\le k-1\). Consequently, \(\chi(G)\ge k\) forces a hole.

Conversely, \(K_{k-1}\) has chromatic number \(k-1\) and no hole. Hence the threshold \(k\) is best possible. ∎

Thus only \(\nu\ge2\) is genuinely open.

---

## 3. A positive extension when triangles are sufficiently sparse

For a graph \(G\), let \(\mathcal T(G)\) be the 3-uniform hypergraph whose hyperedges are the vertex sets of triangles of \(G\). Let
\[
\tau_\triangle(G)
\]
denote the weak chromatic number of \(\mathcal T(G)\), i.e. the least number of parts in a partition of \(V(G)\) into triangle-free induced subgraphs.

### Proposition 3.1
If \(G\) has no \(\nu\)-run, then
\[
\chi(G)\le (m_\nu-1)\tau_\triangle(G).
\]

### Proof
Let \(V(G)=X_1\cup\cdots\cup X_r\), where \(r=\tau_\triangle(G)\) and every \(G[X_i]\) is triangle-free. Since \(G\) has no \(\nu\)-run, neither does any induced subgraph \(G[X_i]\). The triangle-free theorem therefore gives
\[
\chi(G[X_i])\le m_\nu-1.
\]
Using disjoint color palettes on the parts gives
\[
\chi(G)\le \sum_{i=1}^r\chi(G[X_i])
   \le r(m_\nu-1).
\]
∎

This yields a concrete theorem in terms of the number of triangles through a vertex.

Let
\[
\Delta_\triangle(G)=
\max_{v\in V(G)}
|\{T:T\text{ is a triangle of }G,\ v\in T\}|.
\]

### Proposition 3.2
Define
\[
r(D)=
\begin{cases}
1,&D=0,\\[2mm]
\left\lceil\sqrt{3eD}\right\rceil,&D\ge1.
\end{cases}
\]
If \(\Delta_\triangle(G)\le D\) and
\[
\chi(G)>(m_\nu-1)r(D),
\]
then \(G\) contains a \(\nu\)-run. No hypothesis on \(\omega(G)\) is needed.

### Proof
For \(D=0\), the graph is triangle-free, so this is the supplied theorem.

Suppose \(D\ge1\). Color the vertices independently and uniformly with \(r=r(D)\) colors. For every triangle \(T\), let \(A_T\) be the event that \(T\) is monochromatic. Then
\[
\Pr(A_T)=\frac1{r^2}.
\]
The event \(A_T\) is independent of all events corresponding to vertex-disjoint triangles. Since every vertex belongs to at most \(D\) triangles, \(A_T\) is dependent on at most \(3(D-1)\) other events. Thus
\[
e\Pr(A_T)\bigl(3(D-1)+1\bigr)
 \le \frac{3eD}{r^2}\le1.
\]
The symmetric Lovász local lemma supplies a coloring with no monochromatic triangle. Its color classes are triangle-free, so
\[
\tau_\triangle(G)\le r(D).
\]
Proposition 3.1 now proves the assertion. ∎

### Corollary 3.3
If a graph \(G\) with chromatic number \(q>m_\nu-1\) has no \(\nu\)-run, then
\[
\Delta_\triangle(G)\ge
\frac1{3e}
\left(\frac{q}{m_\nu-1}-1\right)^2.
\]

Thus any counterexample sequence with unbounded chromatic number must contain vertices lying in quadratically many triangles, measured in terms of \(\chi(G)\). This is a genuine extension of the triangle-free result, but bounded clique number does not bound \(\Delta_\triangle\).

---

## 4. Decomposition reductions

### 4.1 Clique cutsets

Suppose \(S\) is a clique cutset and \(A,B\) are nonempty unions of different components of \(G-S\). Put
\[
G_A=G[A\cup S],\qquad G_B=G[B\cup S].
\]

Then
\[
\chi(G)=\max\{\chi(G_A),\chi(G_B)\}.
\]
Indeed, color both pieces with the larger number of colors and permute the colors in one piece so that the two colorings agree on the clique \(S\).

Moreover, every hole of \(G\) is contained in one of the two pieces. A hole crossing both \(A\) and \(B\) would have to meet \(S\) at least twice. Three vertices of \(S\) create a chord, while with exactly two vertices \(x,y\in S\), the edge \(xy\) is a chord unless \(x,y\) are consecutive on the cycle; in the latter case the remaining \(x\)-\(y\) path cannot use both \(A\) and \(B\).

Consequently, to prove the conjecture it is enough to consider graphs with no clique cutset.

### 4.2 A \(K_4\)-free special case

Recall that \(G=G_1\vee\cdots\vee G_s\) denotes the join: all possible edges are added between distinct factors.

### Proposition 4.1
If \(G\) is \(K_4\)-free, \(\overline G\) is disconnected, and
\[
\chi(G)\ge m_\nu+1,
\]
then \(G\) contains a \(\nu\)-run.

### Proof
The components of \(\overline G\) give a nontrivial join decomposition
\[
G=G_1\vee\cdots\vee G_s.
\]
Clique number and chromatic number add under joins:
\[
\omega(G)=\sum_i\omega(G_i),\qquad
\chi(G)=\sum_i\chi(G_i).
\]
Since \(\omega(G)\le3\) and \(s\ge2\), every factor has clique number at most two. Thus every \(G_i\) is triangle-free.

If \(G\) has no \(\nu\)-run, neither does any induced factor, so every factor with clique number two has chromatic number at most \(m_\nu-1\). Since the positive integers \(\omega(G_i)\) sum to at most three, either:

- all factors are stable sets, in which case \(\chi(G)\le3\); or
- one factor has clique number two and there is at most one further factor, which is stable, giving
  \[
  \chi(G)\le (m_\nu-1)+1=m_\nu.
  \]

This contradicts \(\chi(G)\ge m_\nu+1\). ∎

Hence the first genuinely unresolved case can be restricted to \(K_4\)-free graphs that are both clique-cutset-free and anticonnected.

---

## 5. Explicit lower bounds on any threshold

The following elementary observation about joins will be used repeatedly.

### Lemma 5.1
If a hole in \(A\vee B\) meets both \(A\) and \(B\), then it is a 4-hole consisting of two nonadjacent vertices of \(A\) and two nonadjacent vertices of \(B\).

### Proof
Every vertex in \(A\) is adjacent to every vertex in \(B\). On an induced cycle, each vertex has only two neighbors among the cycle vertices, so the cycle contains at most two vertices from each side. Since it meets both sides and has length at least four, it has exactly two from each side and length four. The two vertices lying in either factor must be nonadjacent, or they form a chord. ∎

### 5.1 An explicit logarithmic lower bound in \(\nu\)

Let
\[
r=\left\lfloor\frac{k-1}{2}\right\rfloor,
\qquad
s=k-1-2r\in\{0,1\},
\]
and for \(\nu\ge2\) set
\[
Q_\nu=
\max\left\{
3,\,
2+\left\lfloor
\log_2\left(\frac{\nu+3}{3}\right)
\right\rfloor
\right\}.
\]

### Proposition 5.2
For all \(k\ge3\) and \(\nu\ge2\),
\[
F_{\nu,k}\ge rQ_\nu+s.
\]
Thus any conjectural threshold must satisfy
\[
n(\nu,k)\ge rQ_\nu+s+1.
\]

### Proof
For \(Q_\nu=3\), take \(H=C_7\).

For \(Q_\nu\ge4\), take the iterated Mycielski graph \(H=H_{Q_\nu}\), starting from \(H_2=K_2\). The Mycielski operation preserves triangle-freeness, raises chromatic number by one, and changes the number of vertices by
\[
|M(H)|=2|H|+1.
\]
Consequently,
\[
\chi(H_q)=q,\qquad
\omega(H_q)=2,\qquad
|H_q|=3\cdot2^{q-2}-1.
\]
The definition of \(Q_\nu\) gives
\[
|H_{Q_\nu}|
=3\cdot2^{Q_\nu-2}-1
\le \nu+2.
\]

Now form
\[
J=\underbrace{H\vee\cdots\vee H}_{r\text{ factors}}\vee K_s.
\]
Then
\[
\omega(J)=2r+s=k-1,\qquad
\chi(J)=rQ_\nu+s.
\]

If \(Q_\nu=3\), every hole of \(J\) has length in \(\{4,7\}\), by Lemma 5.1, so \(J\) has no two consecutive hole lengths.

If \(Q_\nu\ge4\), every hole is either a 4-hole crossing factors or lies in a copy of \(H\), and hence has length at most \(\nu+2\). But a \(\nu\)-run begins at a length at least four and therefore ends at a length at least \(\nu+3\). Thus \(J\) has no \(\nu\)-run. ∎

For \(\nu=2\), this gives the particularly simple bound
\[
n(2,k)\ge
3\left\lfloor\frac{k-1}{2}\right\rfloor
+\bigl((k-1)\bmod 2\bigr)+1
=
\left\lfloor\frac{3k-1}{2}\right\rfloor.
\]

### 5.2 A probabilistic polynomial lower bound in \(\nu\)

The order of a graph alone provides another obstruction: a graph on at most \(\nu+2\) vertices cannot have a \(\nu\)-run, because the largest length in such a run is at least \(\nu+3\).

### Proposition 5.3
For every fixed \(k\ge3\), there is a constant \(c_k>0\) such that, for all sufficiently large \(\nu\),
\[
F_{\nu,k}\ge
c_k\frac{\nu^{\,1-2/k}}{\log \nu}.
\]

### Proof
Put \(n=\nu+2\), \(b=\binom{k}{2}\), and choose
\[
c=\min\left\{\frac12,\left(\frac{k!}{16}\right)^{1/b}\right\},
\qquad
p=cn^{-2/k}.
\]
Let \(G\sim G(n,p)\).

The expected number \(X\) of copies of \(K_k\) satisfies
\[
\mathbb E X
\le \frac{n^kp^b}{k!}
=\frac{c^b}{k!}n
\le\frac n{16}.
\]
Hence
\[
\Pr(X>n/4)\le\frac14.
\]

Let
\[
a=\left\lceil8p^{-1}\log n\right\rceil.
\]
For sufficiently large \(n\), \(a<n\). The expected number of independent sets of order \(a\) is at most
\[
\binom na(1-p)^{\binom a2}
\le
\left(\frac{en}{a}\right)^a
\exp\left(-\frac{pa(a-1)}2\right)
<n^{-a}.
\]
Thus, with probability tending to one, \(\alpha(G)<a\). There is therefore a realization with \(X\le n/4\) and \(\alpha(G)<a\).

Delete at most one vertex for each \(K_k\) in this realization. The resulting graph \(H\) is \(K_k\)-free and satisfies
\[
|V(H)|\ge\frac{3n}{4},
\qquad
\alpha(H)<a.
\]
Therefore
\[
\chi(H)\ge\frac{|V(H)|}{\alpha(H)}
>
\frac{3n}{4a}
\ge
\frac{c}{12}\,
\frac{n^{1-2/k}}{\log n}
\]
for large \(n\).

Finally, \(H\) has at most \(n=\nu+2\) vertices, so it has no \(\nu\)-run. Taking \(c_k=c/13\), say, proves the assertion. ∎

This lower bound does not threaten the conjecture, but it shows that any threshold must grow at least polynomially in \(\nu\) for fixed \(k\), even before considering the much more delicate hole structure.

---

## 6. Why partitioning into triangle-free pieces does not settle \(k=4\)

For a \(K_4\)-free graph, every neighborhood is triangle-free. Moreover, if the graph has no \(\nu\)-run, the supplied theorem gives
\[
\chi(G[N(v)])\le m_\nu-1
\qquad\text{for every }v.
\]
It is therefore tempting to hope that bounded local chromatic number forces a bounded partition into triangle-free induced subgraphs. The following construction shows that no such statement follows merely from \(K_4\)-freeness or even from neighborhoods being matchings.

### Proposition 6.1
For every \(R\) and \(L\), there exists a \(K_4\)-free graph \(G\) such that:

1. \(\chi(G)>R\);
2. every neighborhood induces a matching;
3. \(G\) has no holes of lengths \(4,\ldots,L\);
4. \(\tau_\triangle(G)>R\).

### Construction and proof
A Berge cycle of length \(\ell\) in a 3-uniform hypergraph consists of distinct vertices
\[
x_1,\ldots,x_\ell
\]
and distinct hyperedges \(e_1,\ldots,e_\ell\) such that
\[
\{x_i,x_{i+1}\}\subseteq e_i
\]
with indices modulo \(\ell\).

Fix \(R,L\), and choose \(d\) sufficiently large compared with \(R^3\). For large \(n\), take a random 3-uniform hypergraph \(\mathcal H_0\) on \(n\) vertices in which every triple is present independently with probability
\[
p=d/n^2.
\]

Let \(s=\lceil n/(4R)\rceil\). The expected number of independent \(s\)-sets is at most
\[
2^n(1-p)^{\binom s3}
\le
\exp\left(n\log2-p\binom s3\right),
\]
which tends to zero when \(d\) is chosen sufficiently large.

For every fixed \(\ell\), the expected number of Berge \(\ell\)-cycles is \(O(d^\ell)\): choose the \(\ell\) core vertices and at most one further vertex for each hyperedge, giving at most \(n^{2\ell}\) choices, each appearing with probability \(p^\ell\). Thus the expected total number of Berge cycles of lengths \(2,\ldots,L\) is bounded independently of \(n\).

Consequently, for sufficiently large \(n\), there is a realization with:

- independence number less than \(s\); and
- fewer than \(n/(4R)\) Berge cycles of lengths at most \(L\).

Delete one hyperedge from each such short Berge cycle. Let \(\mathcal H\) be the resulting hypergraph. If \(D\) is the set of deleted hyperedges, then
\[
|D|<n/(4R).
\]
Any independent set in \(\mathcal H\) can be made independent in \(\mathcal H_0\) by deleting at most one vertex for each hyperedge in \(D\). Hence
\[
\alpha(\mathcal H)
\le\alpha(\mathcal H_0)+|D|
<\frac nR
\]
for large \(n\). Thus the weak chromatic number of \(\mathcal H\) exceeds \(R\).

Because \(\mathcal H\) has no Berge 2-cycle, it is linear: distinct hyperedges meet in at most one vertex. Because it has no Berge 3-cycle, every triangle in its 2-shadow arises from one hyperedge.

Let \(G\) be the 2-shadow of \(\mathcal H\): two vertices are adjacent when they lie in a common hyperedge.

For any vertex \(v\), the hyperedges through \(v\) have the form
\[
\{v,a_i,b_i\}.
\]
Linearity makes the pairs \(\{a_i,b_i\}\) disjoint. There can be no edge between vertices belonging to different pairs, since this would create a Berge 3-cycle. Hence \(G[N(v)]\) is a matching.

Every triangle of \(G\) is exactly a hyperedge of \(\mathcal H\). A \(K_4\) in \(G\) would therefore give two hyperedges sharing two vertices, contrary to linearity. Thus \(G\) is \(K_4\)-free, and
\[
\tau_\triangle(G)=\chi_{\mathrm{weak}}(\mathcal H)>R.
\]
In particular, \(\chi(G)>R\).

Finally, every hole of length \(\ell\ge4\) in \(G\) yields a Berge \(\ell\)-cycle in \(\mathcal H\): consecutive cycle edges cannot come from the same hyperedge, since the third edge of that triangle would be a chord. Thus \(G\) has no holes of lengths at most \(L\). ∎

This proposition is not a counterexample to the conjecture: it gives no control over long hole lengths, and the graph may have a \(\nu\)-run above \(L\). It does show that bounded clique number, bounded neighborhood chromatic number, and avoidance of every bounded initial range of hole lengths are insufficient for a straightforward triangle-free partition argument.

---

## 7. Remaining gap

The first unresolved core is already:

- \(k=4\);
- \(\nu\ge2\);
- \(G\) has no clique cutset;
- \(\overline G\) is connected;
- every neighborhood has chromatic number at most \(m_\nu-1\);
- triangle incidence is necessarily unbounded in any high-chromatic counterexample.

The triangle-free theorem controls each neighborhood, but there is no established mechanism here for assembling those local bounds into a global coloring or for extracting a triangle-free induced subgraph of chromatic number at least \(m_\nu\). Proposition 6.1 shows why local boundedness alone cannot do this. A proof must exploit the absence of \(\nu\)-runs at arbitrarily large lengths, not merely the absence of bounded-length holes.

Accordingly, the full conjecture is neither proved nor disproved here. The rigorous gains are the exact \(\nu=1\) case, the bounded-triangle-incidence theorem, decomposition reductions, and quantitative lower bounds on any possible threshold.