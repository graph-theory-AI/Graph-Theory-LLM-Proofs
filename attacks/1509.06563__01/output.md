```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unresolved, but bounded-gap sets are proved constricting for graphs with tame neighborhood matchings, and any least counterexample is reduced to locally bounded-chromatic graphs whose every vertex neighborhood contains arbitrarily large matched triangle configurations.",
  "would_publish": false,
  "caveats": "The neighborhood restrictions are not consequences of bounded clique number, so the unrestricted k=4 case remains open."
}
```

## 1. Statement and notation

For a graph \(G\), let
\[
\mathcal L(G)=\{\ell\ge 4: G\text{ contains an induced cycle of length }\ell\}.
\]
Call \(G\) **\(F\)-clean** if \(\mathcal L(G)\cap F=\varnothing\).

Let \(F\) have bounded gaps. We may choose integers \(b\ge 1\) and \(L\ge 4\) such that
\[
F\cap\{\ell,\ell+1,\ldots,\ell+b-1\}\ne\varnothing
\qquad\text{for every }\ell\ge L. \tag{1}
\]
Consequently, every \(F\)-clean graph has no block of \(b\) consecutive hole lengths beginning at or above \(L\).

The theorem from the source paper implies the following uniform statement.

> **Triangle-free input.** For every \(b,L\), there is \(c_0=c_0(b,L)\) such that every triangle-free graph of chromatic number greater than \(c_0\) has \(b\) consecutive hole lengths, all at least \(L\).

Indeed, apply the source theorem with sufficiently many consecutive lengths, for instance \(b+L\), and take the last \(b\) of them.

The arguments below use only this input.

---

## 2. A triangle-partition bound

Let \(\tau_\triangle(G)\) denote the least number of parts in a partition
\[
V(G)=V_1\cup\cdots\cup V_q
\]
such that every \(G[V_i]\) is triangle-free. Equivalently, \(\tau_\triangle(G)\) is the weak chromatic number of the hypergraph whose hyperedges are the triangles of \(G\).

For a graph \(J\), write \(\nu(J)\) for its matching number, and set
\[
m(G)=\max_{v\in V(G)}\nu\bigl(G[N_G(v)]\bigr).
\]

### Lemma 2.1
For every graph \(G\),
\[
\tau_\triangle(G)\le m(G)+1. \tag{2}
\]

#### Proof

Let \(p=\tau_\triangle(G)\), and choose an induced subgraph \(H\subseteq G\), minimal by vertex inclusion, with \(\tau_\triangle(H)=p\). For every \(v\in V(H)\),
\[
\tau_\triangle(H-v)=p-1;
\]
the upper bound follows from minimality, and the lower bound from
\(\tau_\triangle(H)\le \tau_\triangle(H-v)+1\).

Take a partition of \(H-v\) into \(p-1\) triangle-free sets
\[
X_1,\ldots,X_{p-1}.
\]
For every \(i\), the set \(N_H(v)\cap X_i\) must contain an edge. Otherwise, \(v\) could be put into \(X_i\) without creating a triangle, contradicting \(\tau_\triangle(H)=p\).

Choose an edge \(x_i y_i\) in \(H[N_H(v)\cap X_i]\). The edges \(x_i y_i\), for \(1\le i\le p-1\), are vertex-disjoint because the sets \(X_i\) are disjoint. Hence
\[
\nu\bigl(H[N_H(v)]\bigr)\ge p-1.
\]
Since \(H\) is induced in \(G\), this gives \(m(G)\ge p-1\), proving (2). \(\square\)

### Proposition 2.2
If \(G\) has no block of \(b\) consecutive hole lengths beginning at or above \(L\), then
\[
\chi(G)\le c_0(b,L)\bigl(m(G)+1\bigr). \tag{3}
\]

#### Proof

Partition \(V(G)\) into \(\tau_\triangle(G)\) triangle-free sets. Every resulting induced subgraph also has no such block of consecutive hole lengths, since its holes are holes of \(G\). The triangle-free input therefore bounds the chromatic number of each part by \(c_0(b,L)\). Using disjoint palettes,
\[
\chi(G)\le c_0(b,L)\tau_\triangle(G).
\]
Now apply Lemma 2.1. \(\square\)

Since every \(F\)-clean graph satisfies the hypothesis of Proposition 2.2, we obtain:

### Corollary 2.3
For every bounded-gap \(F\), there is a constant \(c=c(F)\) such that every \(F\)-clean graph satisfies
\[
\chi(G)\le c\left(1+\max_{v\in V(G)}
\nu\bigl(G[N_G(v)]\bigr)\right). \tag{4}
\]

In particular, the conjecture holds, without any clique-number assumption, in every class for which matching numbers of vertex neighborhoods are uniformly bounded.

For example, it holds in any class excluding, as a not necessarily induced subgraph, a fixed fan
\[
K_1\vee tK_2.
\]

This is a genuine extension of the triangle-free case: triangles are allowed, but a graph of unbounded chromatic number avoiding the prescribed holes must contain arbitrarily large matchings inside vertex neighborhoods.

---

## 3. A bounded-clique special case with induced neighborhood restrictions

The preceding bound can be combined with induction on the clique number.

Let \(R_4(t)\) denote the four-colour Ramsey number for \(K_t\). We need the following elementary extraction lemma.

### Lemma 3.1
Let \(J\) be a graph with \(\chi(J)\le a\), and suppose \(J\) contains a matching of size at least
\[
\binom a2 R_4(t).
\]
Then \(J\) contains, as an induced subgraph, at least one of:

1. \(tK_2\);
2. \(K_{t,t}\);
3. a half-graph \(H_t\), with bipartition
   \(\{x_1,\ldots,x_t\}\), \(\{y_1,\ldots,y_t\}\), and
   \[
   x_i y_j\in E(H_t)\quad\Longleftrightarrow\quad i\le j.
   \]

#### Proof

Properly colour \(J\) with \(a\) colours. Every edge of the given matching has endpoints of two different colours. By pigeonhole, at least \(R_4(t)\) matching edges use the same unordered pair of colours. Write them as
\[
x_i y_i,\qquad 1\le i\le R_4(t),
\]
where all \(x_i\) have one colour and all \(y_i\) another. Thus both \(\{x_i\}\) and \(\{y_i\}\) are stable.

For \(i<j\), colour the pair \(ij\) by
\[
\left(\mathbf 1_{x_i y_j\in E(J)},
      \mathbf 1_{x_j y_i\in E(J)}\right)\in\{0,1\}^2.
\]
Ramsey's theorem yields \(t\) indices for which this pair is constant. The four possibilities give respectively:

- \((0,0)\): an induced \(tK_2\);
- \((1,1)\): an induced \(K_{t,t}\);
- \((1,0)\) or \((0,1)\): one of the two orderings of an induced half-graph.

\(\square\)

For \(t\ge3\), define \(\mathcal Q_t\) to be the hereditary class of graphs \(G\) such that no vertex neighborhood \(G[N(v)]\) contains any of the three graphs in Lemma 3.1 as an induced subgraph.

### Theorem 3.2
For all integers \(b,L,t,k\), there is a constant \(C=C(b,L,t,k)\) such that every \(K_k\)-free graph \(G\in\mathcal Q_t\) with
\[
\chi(G)>C
\]
contains \(b\) consecutive hole lengths, all at least \(L\).

Consequently, every bounded-gap set \(F\) is constricting when restricted to \(\mathcal Q_t\).

#### Proof

We induct on \(k\). The case \(k=3\) is exactly the triangle-free input.

Suppose \(k\ge4\), and let \(A_{k-1}\) be a bound supplied by induction for \(K_{k-1}\)-free graphs in \(\mathcal Q_t\) having no required block of holes.

Let \(G\in\mathcal Q_t\) be \(K_k\)-free and suppose it has no block of \(b\) consecutive hole lengths at or above \(L\). For every \(v\),
\[
G[N(v)]
\]
is \(K_{k-1}\)-free, belongs to \(\mathcal Q_t\), and has no required block of holes. Hence
\[
\chi(G[N(v)])\le A_{k-1}. \tag{5}
\]

Set
\[
M=\binom{A_{k-1}}2 R_4(t).
\]
If some \(G[N(v)]\) had a matching of size at least \(M\), Lemma 3.1 would produce one of the three induced configurations prohibited by the definition of \(\mathcal Q_t\). Thus
\[
m(G)\le M-1.
\]
Proposition 2.2 now gives
\[
\chi(G)\le c_0(b,L)M.
\]
This completes the induction. \(\square\)

A more natural, but narrower, consequence is the following.

### Corollary 3.3
Fix \(t\ge3\). The conclusion of Theorem 3.2 holds for graphs \(G\) satisfying:

- \(G\) is induced-\(C_4\)-free; and
- every \(G[N(v)]\) has induced matching number less than \(t\).

Indeed, \(tK_2\) is excluded by the second condition, while \(K_{t,t}\) and \(H_t\) each contain an induced \(C_4\). In particular, if \(4\in F\), then \(F\) is constricting, for every clique bound, on the class of graphs with uniformly bounded induced matching number in every vertex neighborhood.

---

## 4. Necessary structure of any least counterexample

The preceding argument also gives a fairly rigid certificate that any counterexample must possess.

Assume the conjecture is false for a bounded-gap set \(F\), and choose the least \(k\) for which \(F\) is not \(k\)-constricting. Since the source paper proves that \(F\) is 3-constricting,
\[
k\ge4.
\]

For every \(r<k\), there is a constant \(d_r\) such that every \(F\)-clean, \(K_r\)-free graph has chromatic number at most \(d_r\).

There is a sequence \(G_i\) of \(F\)-clean, \(K_k\)-free graphs with
\[
\chi(G_i)\longrightarrow\infty.
\]
Let \(p_i=\tau_\triangle(G_i)\). By Proposition 2.2,
\[
p_i\ge \frac{\chi(G_i)}{c_0(b,L)},
\]
so \(p_i\to\infty\).

Choose an induced subgraph \(H_i\subseteq G_i\), minimal with
\[
\tau_\triangle(H_i)=p_i.
\]

Then the following all hold.

### (a) Every vertex neighborhood has bounded chromatic number

For every \(v\in V(H_i)\),
\[
\chi(H_i[N(v)])\le d_{k-1}, \tag{6}
\]
because \(H_i[N(v)]\) is \(F\)-clean and \(K_{k-1}\)-free.

More generally, if \(Q\) is a clique of size \(s\), \(1\le s\le k-2\), then
\[
\chi\bigl(H_i[N(Q)]\bigr)\le d_{k-s}. \tag{7}
\]

Thus a least counterexample is uniformly locally chromatically bounded in every nonempty clique link.

### (b) Every vertex neighborhood contains a huge matching

For every \(v\in V(H_i)\),
\[
\nu\bigl(H_i[N(v)]\bigr)\ge p_i-1. \tag{8}
\]
This is the matching constructed in the proof of Lemma 2.1. In fact, for every weak \((p_i-1)\)-colouring of \(H_i-v\), each colour class supplies one edge in \(N(v)\), and these edges form a matching.

Consequently,
\[
\delta(H_i)\ge 2(p_i-1),
\]
and every vertex belongs to at least \(p_i-1\) triangles with pairwise disjoint pairs of other vertices.

### (c) Every neighborhood contains a large canonical bipartite pattern

Fix \(t\). For sufficiently large \(i\), (6), (8), and Lemma 3.1 imply that for every \(v\in V(H_i)\), the graph \(H_i[N(v)]\) contains as an induced subgraph one of
\[
tK_2,\qquad K_{t,t},\qquad H_t. \tag{9}
\]

Thus an unrestricted counterexample cannot merely have a few complicated neighborhoods. At every vertex and on every fixed scale, a large induced matching, complete bipartite graph, or half-graph must occur inside the bounded-chromatic neighborhood.

For \(k=4\), this becomes particularly concrete: every neighborhood is triangle-free and has bounded chromatic number, while still containing matchings of unbounded size. This is the first unresolved case.

---

## 5. Relation with the stronger consecutive-hole formulation

For fixed \(b,L,k\), let \(\mathscr S_{b,L}\) be the family of sets
\[
F\subseteq \{L,L+1,\ldots\}
\]
meeting every interval of \(b\) consecutive integers.

The following two uniform statements are equivalent:

1. Some \(N\) forces \(b\) consecutive hole lengths at least \(L\) in every \(K_k\)-free graph of chromatic number at least \(N\).
2. The same \(N\) works in the \(k\)-constricting definition simultaneously for every \(F\in\mathscr S_{b,L}\).

Only the reverse implication needs comment. If \(G\) has no such block of hole lengths, define
\[
F_G=\{n\ge L:n\notin\mathcal L(G)\}.
\]
Then \(F_G\in\mathscr S_{b,L}\), but \(G\) has no \(F_G\)-hole.

The original conjecture is pointwise in \(F\), so it does not formally provide this uniformity. Theorem 3.2 does establish the stronger, uniform consecutive-hole conclusion on the restricted class \(\mathcal Q_t\).

---

## 6. Arithmetic progressions do not cover the full problem

Using the residue-class theorem quoted in the prompt, any set \(F\) containing an infinite arithmetic progression is already constricting. Indeed, if
\[
\{a+jd:j\ge0\}\subseteq F,
\]
choose \(Q=md>a\). Then the full positive residue class
\[
\{a+jQ:j\ge0\}
\]
is contained in \(F\), and the fixed-residue theorem applies. Thus every eventually periodic infinite set is covered.

There are, however, very simple bounded-gap sets with no infinite arithmetic progression. For example, with
\[
\varphi=\frac{1+\sqrt5}{2},\qquad
F_\varphi=\{\lfloor n\varphi\rfloor:n\ge1\},
\]
successive elements differ by \(1\) or \(2\), so \(F_\varphi\) has gap bound \(2\). For an integer \(x\),
\[
\mathbf 1_{F_\varphi}(x)
=
\left\lfloor\frac{x+1}{\varphi}\right\rfloor
-
\left\lfloor\frac{x}{\varphi}\right\rfloor .
\]
Along any arithmetic progression \(x=a+md\), the phases
\[
\left\{\frac{a+md}{\varphi}\right\}
\]
are dense modulo one because \(d/\varphi\) is irrational. Both membership values therefore occur, so no infinite arithmetic progression is contained in \(F_\varphi\). This explicit gap-two set is not reached by the residue-class result.

---

## 7. Remaining gap

The full conjecture is not proved here. The obstruction is precise:

- bounded clique number gives bounded chromatic number in each neighborhood only after choosing a least failed clique size;
- high global chromatic number forces very large matchings in all neighborhoods of a triangle-partition-critical induced subgraph;
- bounded local chromatic number plus such a matching yields one of the three patterns in (9);
- none of these patterns is excluded by \(K_k\)-freeness. For example, \(K_{n,n,n}\) is \(K_4\)-free and has neighborhoods \(K_{n,n}\) with arbitrarily large matchings.

A complete proof would need to use the global interaction of these local induced matchings, bicliques, or half-graphs to manufacture holes whose lengths meet the particular aperiodic bounded-gap set \(F\). The arguments above do not provide that final step.