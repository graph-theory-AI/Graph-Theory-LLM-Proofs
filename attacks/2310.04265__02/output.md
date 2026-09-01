```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is equivalent to ordinary χ-boundedness of all backedge graphs of width-k tournaments; an exact XOR normal form and a compatible-order special case for twin-width one are proved.",
  "would_publish": false,
  "caveats": "No bound is obtained for arbitrary optimal orders, and no counterexample family is constructed."
}
```

# Mathematical writeup

## 1. Statement and notation

For a tournament \(T\) and a linear order \(\sigma\) of \(V(T)\), let
\[
G_\sigma(T)=T^\sigma
\]
be its backedge graph: for \(x<_\sigma y\), the pair \(xy\) is an edge precisely when \(y\to x\) in \(T\).

Write
\[
\vec\omega(T)=\min_\sigma \omega(G_\sigma(T))
\]
for the clique number introduced in the source paper, and \(\vec\chi(T)\) for the dichromatic number of \(T\).

The conjecture asks whether, for every fixed \(k\), there is a function \(f_k\) such that
\[
\vec\chi(T)\le f_k(\vec\omega(T))
\qquad\text{whenever }\operatorname{tww}(T)\le k.
\]

I do not resolve this. I give an exact reformulation, an exact normal form, and a nontrivial special case for twin-width one.

---

## 2. Comparing dichromatic and ordinary chromatic number

### Lemma 2.1

For every tournament \(T\) and every order \(\sigma\), with \(G=G_\sigma(T)\),
\[
\frac{\chi(G)}{\omega(G)}
   \le \vec\chi(T)
   \le \chi(G).
\tag{2.1}
\]

### Proof

Every stable set of \(G\) induces a transitive subtournament of \(T\): all its arcs point forward in the order inherited from \(\sigma\). Thus any proper coloring of \(G\) is a dichromatic coloring of \(T\), proving
\[
\vec\chi(T)\le \chi(G).
\]

Conversely, let
\[
V(T)=X_1\cup\cdots\cup X_q,\qquad q=\vec\chi(T),
\]
where each \(T[X_i]\) is transitive. Let \(\rho_i\) be its unique transitive order. For \(x,y\in X_i\), the pair \(xy\) is an edge of \(G[X_i]\) exactly when \(\sigma|_{X_i}\) and \(\rho_i\) order \(x,y\) oppositely. Hence \(G[X_i]\) is a permutation graph.

Permutation graphs are perfect: equivalently, coloring an inversion graph amounts to partitioning a permutation into increasing subsequences, and by Dilworth's theorem the minimum number of such subsequences is the length of a longest decreasing subsequence, namely its clique number. Therefore
\[
\chi(G[X_i])=\omega(G[X_i])\le \omega(G).
\]
Using disjoint palettes on the \(q\) sets \(X_i\),
\[
\chi(G)\le q\,\omega(G),
\]
which is the other inequality. ∎

A useful consequence is that a high-chromatic bounded-clique backedge graph automatically gives a tournament with large dichromatic number.

---

## 3. Exact reformulation as an ordinary \(\chi\)-boundedness problem

For fixed \(k\), define
\[
\mathcal B_k=
 \{G_\sigma(T):\operatorname{tww}(T)\le k,\ \sigma\text{ any vertex order}\}.
\]

### Theorem 3.1

The tournament conjecture for twin-width at most \(k\) is equivalent to ordinary \(\chi\)-boundedness of \(\mathcal B_k\).

More precisely:

1. If \(\vec\chi(T)\le f_k(\vec\omega(T))\) for all \(T\) of twin-width at most \(k\), then
   \[
   \chi(G)\le \omega(G)f_k(\omega(G))
   \qquad(G\in\mathcal B_k),
   \]
   after replacing \(f_k\) by its monotone envelope if necessary.

2. If \(\chi(G)\le g_k(\omega(G))\) for every \(G\in\mathcal B_k\), then
   \[
   \vec\chi(T)\le g_k(\vec\omega(T))
   \qquad(\operatorname{tww}(T)\le k).
   \]

### Proof

For the first implication, write \(G=G_\sigma(T)\) and \(s=\omega(G)\). Since
\[
\vec\omega(T)\le s,
\]
Lemma 2.1 gives
\[
\chi(G)\le s\,\vec\chi(T)
 \le s f_k(s).
\]

For the converse, choose an order \(\sigma\) realizing
\[
\omega(G_\sigma(T))=\vec\omega(T).
\]
Then Lemma 2.1 gives
\[
\vec\chi(T)\le \chi(G_\sigma(T))
 \le g_k(\vec\omega(T)).
\]
∎

Thus a disproof is equivalent to constructing, for some fixed \(k,r\), graphs
\[
G_n=G_{\sigma_n}(T_n)
\]
such that
\[
\operatorname{tww}(T_n)\le k,\qquad
\omega(G_n)\le r,\qquad
\chi(G_n)\longrightarrow\infty.
\tag{3.1}
\]
For \(r=2\), these would be triangle-free graphs of unbounded chromatic number. Conversely, any such family gives
\[
\vec\omega(T_n)\le r,\qquad
\vec\chi(T_n)\ge \frac{\chi(G_n)}r\longrightarrow\infty.
\]

This explains why the supplied family \(S_j\) does not by itself disprove the conjecture: its unbounded dichromatic number is insufficient unless one also bounds \(\vec\omega(S_j)\).

---

## 4. An exact XOR normal form

Let \(P(\tau,\sigma)\) be the inversion graph of two orders \(\tau,\sigma\): a pair is an edge when the orders disagree on it. This is a permutation graph.

An order \(\tau\) is compatible with a contraction sequence if every bag appearing in the sequence is an interval of \(\tau\).

### Proposition 4.1

If \(T\) has twin-width at most \(k\), then there is an order \(\tau\) such that:

1. some width-\(k\) contraction sequence of \(T\) is compatible with \(\tau\);
2. the ordinary graph
   \[
   H=G_\tau(T)
   \]
   has an interval-compatible contraction sequence of width at most \(k\);
3. for every other order \(\sigma\),
   \[
   G_\sigma(T)=H\triangle P(\tau,\sigma),
   \tag{4.1}
   \]
   where \(\triangle\) denotes symmetric difference of edge sets.

### Proof

The bags created by a binary contraction sequence form a rooted binary merge tree. Choose a left-right ordering of this tree and let \(\tau\) be its leaf order. Every bag is then an interval of \(\tau\).

Consider two current bags \(A,B\). Since they are disjoint intervals, one lies entirely before the other in \(\tau\). If all arcs between \(A,B\) have the same direction, then \(H[A,B]\) is respectively complete or anticomplete. If both arc directions occur, then \(H[A,B]\) contains both edges and nonedges. Hence the same contractions give an ordinary graph contraction sequence with the same red pairs and therefore width at most \(k\).

For a pair \(x,y\), changing the reference order from \(\tau\) to \(\sigma\) toggles whether its tournament arc is a backedge exactly when \(\tau,\sigma\) order the pair oppositely. This proves (4.1). ∎

There is also a converse: if an ordered graph \(H\) has an interval-compatible width-\(k\) sequence, orient nonedges forward and edges backward in its order \(\tau\). The resulting tournament has twin-width at most \(k\), and changing to another order \(\sigma\) produces \(H\triangle P(\tau,\sigma)\).

Consequently, \(\mathcal B_k\) is exactly the class of graphs
\[
H\triangle P,
\]
where \(H\) admits an interval-compatible width-\(k\) contraction sequence and \(P\) is an inversion graph relative to the same underlying order.

The unresolved issue is cancellation between \(H\) and \(P\). Ordinary bounded twin-width of the compatible graph \(H\) does not imply bounded twin-width of \(H\triangle P\).

---

## 5. Width zero and ordinary graphs of twin-width one

### Proposition 5.1

A tournament has twin-width zero if and only if it is transitive.

### Proof

In a width-zero first contraction, the two merged vertices have identical orientations toward every other vertex. Contract them and argue inductively. The contracted tournament is transitive; replacing the contracted vertex by the two twins, placed consecutively in their mutual arc order, remains transitive.

Conversely, consecutive vertices in the transitive order are twins toward all remaining vertices and can be contracted with no red edge. ∎

Thus the width-zero case has
\[
\vec\chi(T)=\vec\omega(T)=1.
\]

The following elementary observation is useful for width one.

### Proposition 5.2

Every undirected graph of twin-width at most one is perfect.

### Proof

Twin-width is hereditary under induced subgraphs and invariant under complementation.

For every \(m\ge5\),
\[
\operatorname{tww}(C_m)\ge2.
\]
Indeed, in the initial partition into singletons, any two vertices \(u,v\) of \(C_m\) have at least two vertices that distinguish them:

- if \(u,v\) are adjacent, their other cycle-neighbors are distinct;
- if they are at distance two, each has one distinct external neighbor;
- at greater distance the symmetric difference is at least as large.

Thus any first contraction creates red degree at least two.

A graph of twin-width at most one therefore contains neither an induced odd cycle of length at least five nor the complement of one. By the Strong Perfect Graph Theorem it is perfect. ∎

### Corollary 5.3: compatible optimal orders

Suppose \(T\) has a width-one contraction sequence compatible with an order \(\sigma\), and suppose \(\sigma\) realizes \(\vec\omega(T)\). Then
\[
\vec\chi(T)\le\vec\omega(T).
\]

Indeed, \(G_\sigma(T)\) has ordinary twin-width at most one, hence is perfect, and
\[
\vec\chi(T)\le\chi(G_\sigma(T))
 =\omega(G_\sigma(T))
 =\vec\omega(T).
\]

The missing point in the general conjecture is that an order realizing \(\vec\omega(T)\) need not be compatible with any bounded-width contraction sequence.

---

## 6. A stronger width-one special case

Let \(T\) have twin-width at most one. Choose a compatible order \(\tau\), and put
\[
H=G_\tau(T).
\]
Then \(H\) is perfect by Proposition 5.2. For another order \(\sigma\), let
\[
P=P(\tau,\sigma),\qquad G=G_\sigma(T)=H\triangle P.
\]

Let \(z(P)\) be the cochromatic number of \(P\), namely the minimum number of parts in a partition of \(V(P)\) into sets each inducing either a clique or a stable set.

### Theorem 6.1

With the notation above,
\[
\vec\chi(T)\le\chi(G)\le z(P)\,\omega(G).
\tag{6.1}
\]
In particular,
\[
\vec\chi(T)
 \le \omega(G)\min\{\omega(P),\alpha(P)\}.
\tag{6.2}
\]

### Proof

Partition \(V(P)\) into \(z(P)\) clique-or-stable parts.

If \(X\) is stable in \(P\), then
\[
G[X]=H[X].
\]
If \(X\) is a clique in \(P\), then, off the diagonal,
\[
G[X]=\overline{H[X]}.
\]
Both \(H[X]\) and its complement are perfect. Hence in either case \(G[X]\) is perfect and
\[
\chi(G[X])=\omega(G[X])\le\omega(G).
\]
Using disjoint palettes proves (6.1).

Since a permutation graph and its complement are perfect, \(P\) can be partitioned into \(\omega(P)\) stable sets or into \(\alpha(P)\) cliques. Thus
\[
z(P)\le\min\{\omega(P),\alpha(P)\},
\]
giving (6.2). ∎

Therefore the conjecture holds for twin-width-one tournaments whenever an order realizing \(\vec\omega(T)\) has bounded cochromatic distance, in the above sense, from a contraction-compatible order.

Any width-one counterexample must have both
\[
\omega(P)\to\infty
\quad\text{and}\quad
\alpha(P)\to\infty
\]
for every relevant compatible-order representation. No bound on \(z(P)\) in terms of \(\omega(G)\) is presently obtained here.

---

## 7. Why compatible perfectness does not settle width one

Consider the order
\[
1<2<3<4<5
\]
and let the backedge graph be the cycle
\[
12,23,34,45,15.
\]
Equivalently, define the tournament \(T\) by the arcs
\[
2\to1,\quad 3\to2,\quad 4\to3,\quad 5\to4,\quad 5\to1
\]
and orient every other pair forward in the displayed order.

Then \(G_\sigma(T)=C_5\), so this backedge graph is not perfect. Nevertheless \(T\) has twin-width one:

1. merge \(1,5\) into \(A\); its only red neighbor is \(3\);
2. merge \(A,2\) into \(B\); its only red neighbor is \(3\);
3. merge \(B,3\); the resulting bag has only \(4\) as a red neighbor;
4. merge the final two bags.

Moreover,
\[
\{1,2,5\}
\]
is transitive in the order \(2,5,1\), and \(\{3,4\}\) is transitive, so
\[
\vec\chi(T)=2.
\]
The tournament is not transitive because \(1\to3\to2\to1\), and the displayed order has backedge clique number two. Hence
\[
\vec\omega(T)=2.
\]

This example shows concretely that an arbitrary, even optimal, backedge order can turn a width-one tournament into a graph of twin-width at least two. Thus Proposition 5.2 cannot simply be applied to the optimal backedge graph.

---

## 8. Exact remaining gap

A counterexample is now reduced to the following explicit construction problem:

> Find fixed integers \(k,r\) and ordered graphs \(G_n\) with
> \[
> \omega(G_n)\le r,\qquad \chi(G_n)\to\infty,
> \]
> such that, after orienting nonedges forward and edges backward in the given order, the resulting tournaments have twin-width at most \(k\).

Equivalently, using Proposition 4.1, find
\[
G_n=H_n\triangle P_n,
\]
where \(H_n\) has an interval-compatible width-\(k\) sequence, \(P_n\) is a permutation graph relative to the same base order, \(\omega(G_n)\) is bounded, and \(\chi(G_n)\) is unbounded.

For \(k=1\), the graphs \(H_n\) are perfect, and Theorem 6.1 shows that the permutation graphs \(P_n\) would necessarily have unbounded cochromatic number. I have neither proved that such a family is impossible nor constructed one.

Accordingly, the original conjecture remains unresolved here.