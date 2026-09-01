```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture reduces exactly to the directed-clique-number-two case, and the binding implication holds for interval unions of ordered stars, in particular for every tournament with a star backedge tree.",
  "would_publish": false,
  "caveats": "Uses the established induced triangle-free extraction theorem of Rödl; non-star backedge trees remain untreated and novelty of the special case was not checked."
}
```

# Mathematical writeup

## 1. Statement and scope

For a tournament \(T\), write

\[
\vec\chi(T)
\]

for its dichromatic number, equivalently the minimum number of transitive subtournaments partitioning \(V(T)\), and write

\[
\vec\omega(T)=\min_{\prec}\omega(T^\prec),
\]

where \(T^\prec\) is the backedge graph with respect to \(\prec\).

A tournament \(H\) is \(\vec\chi\)-binding if there is a function \(f_H\) such that every \(H\)-free tournament \(T\) satisfies

\[
\vec\chi(T)\le f_H(\vec\omega(T)).
\]

I do not prove the conjecture for arbitrary forest-orderable \(H\). I prove:

1. an exact reduction of binding to the case \(\vec\omega\le 2\);
2. an exact ordered-graph reformulation;
3. the binding implication when \(H\) has a star backedge tree;
4. more generally, when \(H\) has a forest-ordering whose components are interval stars.

The external input is the following established induced-subgraph theorem, usually called Rödl's theorem.

> **Rödl extraction theorem.** For all integers \(k,q\), there is an integer \(\rho(k,q)\) such that every graph \(G\) with
> \[
> \omega(G)\le k,\qquad \chi(G)>\rho(k,q)
> \]
> has an induced triangle-free subgraph \(J\) with \(\chi(J)>q\).

No unproved conjecture is used.

---

## 2. The ordered-graph dictionary

Given an ordered graph \(G=(V,<)\), define a tournament \(T(G)\) by, for \(x<y\),

\[
y\to x\quad\Longleftrightarrow\quad xy\in E(G).
\]

Thus \(G\) is exactly the backedge graph of \(T(G)\) in the given order.

### Lemma 2.1

For every ordered graph \(G\),

\[
\frac{\chi(G)}{\omega(G)}
\le \vec\chi(T(G))
\le \chi(G).
\tag{2.1}
\]

#### Proof

A proper coloring of \(G\) partitions \(V(G)\) into sets with no backedges. Each such set induces a transitive tournament in the inherited order. Hence

\[
\vec\chi(T(G))\le \chi(G).
\]

Conversely, let \(S\) induce a transitive subtournament of \(T(G)\). List \(S\) in the ambient order, and record the ranks of these vertices in the transitive order of \(T(G)[S]\). Two vertices are adjacent in \(G[S]\) exactly when their two orders are reversed. Thus \(G[S]\) is an inversion graph of a permutation.

An inversion graph can be colored with as many colors as its clique number: cliques are decreasing subsequences, while a proper coloring is a partition into increasing subsequences, and the equality follows from the standard chain-antichain theorem. Consequently,

\[
\chi(G[S])=\omega(G[S])\le \omega(G).
\]

If \(T(G)\) is partitioned into \(r=\vec\chi(T(G))\) transitive sets, color the corresponding \(r\) induced subgraphs of \(G\) with disjoint palettes. This gives

\[
\chi(G)\le r\,\omega(G),
\]

which is the other inequality. \(\square\)

---

## 3. Exact ordered forbidden-pattern formulation

Let \(H\) have \(h\) vertices. For every ordering

\[
\sigma=(v_1,\dots,v_h)
\]

of \(V(H)\), let \(B_\sigma(H)\) be the ordered graph on \(1<\cdots<h\) in which, for \(i<j\),

\[
ij\in E(B_\sigma(H))
\quad\Longleftrightarrow\quad
v_j\to v_i \text{ in }H.
\]

Let

\[
\mathcal B(H)=\{B_\sigma(H):\sigma \text{ is an ordering of }V(H)\}.
\]

Occurrences below are induced and order-preserving.

### Proposition 3.1

For an ordered graph \(G\),

\[
T(G)\text{ is }H\text{-free}
\quad\Longleftrightarrow\quad
G\text{ contains no member of }\mathcal B(H).
\]

#### Proof

If \(x_1<\cdots<x_h\) induce \(H\) in \(T(G)\), pull their order back through an isomorphism from \(H\). For \(i<j\), the edge \(x_ix_j\) belongs to \(G\) exactly when \(x_j\to x_i\), so these vertices induce the corresponding \(B_\sigma(H)\).

The converse is the same argument reversed. \(\square\)

### Proposition 3.2

The tournament \(H\) is \(\vec\chi\)-binding if and only if the ordered graph class avoiding \(\mathcal B(H)\) is \(\chi\)-bounded as a function of ordinary clique number.

#### Proof

Suppose first that the ordered class has a bound \(g\). For an \(H\)-free tournament \(T\), choose an order \(\prec\) with

\[
\omega(T^\prec)=\vec\omega(T).
\]

By Proposition 3.1, \(T^\prec\) avoids \(\mathcal B(H)\), and hence

\[
\vec\chi(T)\le \chi(T^\prec)
\le g(\vec\omega(T)).
\]

Conversely, suppose \(H\) is binding by a monotone function \(f\). If \(G\) avoids \(\mathcal B(H)\), then \(T(G)\) is \(H\)-free and

\[
\vec\omega(T(G))\le \omega(G).
\]

By Lemma 2.1,

\[
\chi(G)
\le \omega(G)\vec\chi(T(G))
\le \omega(G)f(\omega(G)).
\]

Thus the ordered class is \(\chi\)-bounded. \(\square\)

---

## 4. Reduction to triangle-free backedge graphs

### Theorem 4.1

For every hereditary class \(\mathcal C\) of tournaments, the following are equivalent:

1. \(\mathcal C\) is \(\vec\chi\)-bounded as a function of \(\vec\omega\);
2. there is a constant \(M\) such that
   \[
   \vec\chi(T)\le M
   \]
   for every \(T\in\mathcal C\) with \(\vec\omega(T)\le2\).

#### Proof

Only \(2\Rightarrow1\) requires proof. Let \(T\in\mathcal C\), put \(k=\vec\omega(T)\), and choose an order whose backedge graph \(G\) satisfies \(\omega(G)=k\).

If

\[
\chi(G)>\rho(k,2M),
\]

Rödl's theorem gives \(S\subseteq V(G)\) such that \(G[S]\) is triangle-free and

\[
\chi(G[S])>2M.
\]

The inherited order shows

\[
\vec\omega(T[S])\le2.
\]

Moreover, by Lemma 2.1,

\[
\vec\chi(T[S])
\ge \frac{\chi(G[S])}{\omega(G[S])}
> M,
\]

contradicting the hypothesis since \(\mathcal C\) is hereditary. Therefore

\[
\vec\chi(T)\le\chi(G)\le\rho(k,2M).
\]

Thus \(\mathcal C\) is \(\vec\chi\)-bounded. \(\square\)

In particular:

> **Corollary 4.2.** A tournament \(H\) is binding if and only if the \(H\)-free tournaments with \(\vec\omega\le2\) have bounded dichromatic number.

Equivalently, by Propositions 3.1–3.2 and Rödl's theorem:

> **Corollary 4.3.** A tournament \(H\) is binding if and only if the triangle-free ordered graphs avoiding every member of \(\mathcal B(H)\) have bounded chromatic number.

This also transparently recovers the known “only if” direction. If \(H\) has no forest backedge graph, then every member of \(\mathcal B(H)\) contains a cycle. Ordered graphs of girth greater than \(|H|\) avoid the whole family. The standard existence of graphs of arbitrarily large girth and chromatic number then violates Corollary 4.3.

Thus the remaining conjecture can be stated exactly as follows:

> If \(\mathcal B(H)\) contains a forest, must the triangle-free ordered graphs avoiding all of \(\mathcal B(H)\) have bounded chromatic number?

---

## 5. Ordered stars

Let \(S_{a,b}\) be the ordered star with center \(z\), with \(a\) leaves preceding \(z\) and \(b\) leaves following \(z\).

### Lemma 5.1

Every triangle-free ordered graph with no induced ordered copy of \(S_{a,b}\) satisfies

\[
\chi(G)\le a+b.
\tag{5.1}
\]

Here \(S_{0,0}\) is a single vertex, in which case the assertion is interpreted in the evident way.

#### Proof

For \(v\in V(G)\), let

\[
\ell(v)=|\{u<v:uv\in E(G)\}|,\qquad
r(v)=|\{u>v:uv\in E(G)\}|.
\]

Since \(G\) is triangle-free, \(N_G(v)\) is a stable set. Therefore, if simultaneously

\[
\ell(v)\ge a,\qquad r(v)\ge b,
\]

then any \(a\) earlier neighbors and any \(b\) later neighbors, together with \(v\), induce \(S_{a,b}\). Hence every vertex satisfies

\[
\ell(v)<a\quad\text{or}\quad r(v)<b.
\]

Put

\[
X=\{v:\ell(v)<a\},\qquad Y=V(G)\setminus X.
\]

Greedy coloring \(G[X]\) in increasing order uses at most \(a\) colors. Every vertex of \(Y\) has \(r(v)<b\), so greedy coloring \(G[Y]\) in decreasing order uses at most \(b\) colors. Using disjoint palettes gives (5.1). \(\square\)

### Theorem 5.2: star backedge trees

Suppose \(H\) has an ordering whose backedge graph is a spanning star. Then \(H\) is \(\vec\chi\)-binding.

More explicitly, if the center has \(a\) preceding leaves and \(b\) following leaves, then one may take

\[
f_H(k)=\rho(k,a+b).
\]

#### Proof

Let \(F=S_{a,b}\) be the given backedge representation of \(H\). If \(T\) is \(H\)-free and \(\prec\) minimizes the clique number of the backedge graph \(G=T^\prec\), then \(G\) contains no induced order-preserving copy of \(F\); otherwise those vertices induce \(H\).

If \(\chi(G)>\rho(\vec\omega(T),a+b)\), Rödl's theorem gives a triangle-free induced ordered subgraph \(J\) with

\[
\chi(J)>a+b.
\]

It remains \(F\)-free, contrary to Lemma 5.1. Therefore

\[
\vec\chi(T)\le\chi(G)
\le\rho(\vec\omega(T),a+b).
\]

Thus \(H\) is binding. \(\square\)

In tournament language, for \(a,b\ge1\), these are the tournaments with a vertex \(z\) and transitive sets \(A,B\), of orders \(a,b\), such that

\[
z\to A,\qquad A\to B,\qquad B\to z.
\]

If \(a=0\) or \(b=0\), the tournament is transitive, so binding is immediate anyway.

---

## 6. A somewhat broader forest subclass

For ordered graphs \(F_1,F_2\), write \(F_1\oplus F_2\) for their ordered disjoint union: every vertex of \(F_1\) precedes every vertex of \(F_2\), and there are no cross-edges.

### Lemma 6.1

Suppose every triangle-free ordered \(F_i\)-free graph has chromatic number at most \(c_i\), for \(i=1,2\). If \(n_2=|V(F_2)|\), then every triangle-free ordered \((F_1\oplus F_2)\)-free graph has chromatic number at most

\[
c_1+n_2+1+c_2.
\]

#### Proof

Suppose

\[
\chi(G)>c_1+n_2+1+c_2.
\]

Choose a minimal initial segment \(P\) of the vertex order with

\[
\chi(P)>c_1+n_2.
\]

Adding one vertex raises chromatic number by at most one, so

\[
\chi(P)\le c_1+n_2+1.
\]

Let \(S\) be the final segment after \(P\). Since

\[
\chi(G)\le\chi(P)+\chi(S),
\]

we have \(\chi(S)>c_2\), and hence \(S\) contains an ordered copy \(Q_2\) of \(F_2\).

Let \(U\subseteq P\) consist of vertices having a neighbor in \(Q_2\). For each \(q\in Q_2\), its neighborhood is stable because \(G\) is triangle-free. Therefore

\[
\chi(U)\le n_2.
\]

It follows that

\[
\chi(P\setminus U)
\ge \chi(P)-\chi(U)
>c_1.
\]

Thus \(P\setminus U\) contains an ordered copy \(Q_1\) of \(F_1\). By construction, \(Q_1\) is anticomplete to \(Q_2\), and all its vertices precede \(Q_2\). Hence \(Q_1\cup Q_2\) induces \(F_1\oplus F_2\), a contradiction. \(\square\)

Iterating Lemmas 5.1 and 6.1 gives:

### Theorem 6.2

Suppose \(H\) has an ordering \(\prec\) such that, in \(H^\prec\),

1. every connected component is a star, with isolated vertices allowed; and
2. every component is an interval of \(\prec\).

Then \(H\) is \(\vec\chi\)-binding.

Indeed, \(H^\prec\) is an ordered disjoint union of ordered stars. Lemmas 5.1 and 6.1 give a constant \(C_H\) bounding the chromatic number of triangle-free ordered \(H^\prec\)-free graphs, and then Rödl's theorem gives

\[
\vec\chi(T)\le \rho(\vec\omega(T),C_H)
\]

for every \(H\)-free tournament \(T\).

---

## 7. Remaining gap

For a non-star backedge tree, the local argument in Lemma 5.1 no longer embeds the required ordered tree: triangle-freeness makes a single neighborhood stable, but gives no comparable control over interactions between different branches or adjacent internal vertices.

The exact unresolved task is therefore to prove that, whenever some member of \(\mathcal B(H)\) is a forest, the triangle-free ordered graphs avoiding the entire finite family \(\mathcal B(H)\) have bounded chromatic number. The argument above establishes this only for ordered stars and interval concatenations of stars. It does not cover general paths, double-stars, caterpillars, or arbitrary trees, and it supplies no counterexample.