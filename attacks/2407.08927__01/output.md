```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full polynomial-time question remains open; I prove a sharp separator-parity lemma for even-hole-free graphs and show that exact Coloring is NP-hard even when tree-independence number is at most three.",
  "would_publish": false,
  "caveats": "The hardness family is not contained in the even-hole-free class, and parity does not bound the number of coloring states on a large separator."
}
```

## 1. Statement and outcome

A **hole** is an induced cycle of length at least four. A graph is **even-hole-free** if all its holes have odd length. The question is whether, on this hereditary class, the exact value of \(\chi(G)\) can be computed in polynomial time.

I do not resolve this question. The main rigorous progress below is:

1. exact Coloring is NP-hard already on graphs of tree-independence number at most \(3\), so the polylogarithmic tree-independence bound from the source paper cannot by itself yield an exact-coloring algorithm;
2. nonadjacent vertices in a separator of an even-hole-free graph can be simultaneously attached to at most two components, with opposite path parities;
3. consequently, every nonclique minimal separator of an even-hole-free graph has exactly two full components;
4. an exact separator-profile formula identifies precisely why star-cutset decompositions do not combine by simply taking a maximum;
5. the slice \(\alpha(G)\le 3\) of the problem has a concrete equivalent formulation as a triangle-packing-plus-matching problem in a restricted complement class.

## 2. Tree-independence number alone is insufficient

Write
\[
\operatorname{tin}(G)=
 \min_{(T,\mathcal B)}
 \max_{t\in V(T)}\alpha(G[B_t])
\]
for the tree-independence number.

### Proposition 2.1

The decision problem \(\chi(G)\le k\) is NP-complete on graphs satisfying
\[
\alpha(G)\le 3.
\]
Consequently it is NP-hard on graphs with \(\operatorname{tin}(G)\le 3\), even when a witnessing tree decomposition is supplied.

#### Proof

Use the standard NP-complete problem **Tripartite Triangle Partition**:

- the input is a tripartite graph \(H\) on \(3q\) vertices;
- the question is whether \(V(H)\) can be partitioned into \(q\) triangles.

Let
\[
G=\overline H.
\]
Since \(H\) is tripartite, \(\omega(H)\le 3\), and hence
\[
\alpha(G)=\omega(H)\le 3.
\]

A color class in \(G\) is a clique in \(H\), so every color class has at most three vertices. Therefore, if \(G\) has a coloring with at most \(q\) colors, its \(3q\) vertices must be partitioned into exactly \(q\) color classes of size three. Each such class is a triangle of \(H\). Conversely, a partition of \(H\) into \(q\) triangles gives a \(q\)-coloring of \(G\). Thus
\[
\chi(G)\le q
\quad\Longleftrightarrow\quad
H\text{ has a triangle partition}.
\]

Finally, the one-bag tree decomposition \(B=V(G)\) witnesses
\[
\operatorname{tin}(G)\le\alpha(G)\le 3.
\]
Membership in NP is immediate. \(\square\)

Thus Coloring is para-NP-hard when parameterized by tree-independence number. Unless \(P=NP\), there is no general algorithm with running time \(n^{f(\operatorname{tin}(G))}\), even if the decomposition is part of the input.

This does **not** prove hardness on even-hole-free graphs: complements of arbitrary tripartite graphs are not necessarily even-hole-free. It does prove that the source paper’s bound
\[
\operatorname{tin}(G)=O(\log^{10} n)
\]
cannot be inserted into a generic fixed-parameter dynamic program for exact Coloring. Any successful algorithm must exploit additional even-hole-free structure.

### Proposition 2.2: the preceding threshold is sharp for global independence number

If \(\alpha(G)\le 2\), then
\[
\chi(G)=|V(G)|-\nu(\overline G),
\]
where \(\nu\) denotes maximum matching size.

#### Proof

Every color class has size one or two. A pair of vertices can receive the same color exactly when it is an edge of \(\overline G\). Hence the two-vertex color classes form a matching in \(\overline G\).

A coloring with \(p\) paired classes uses
\[
p+(n-2p)=n-p
\]
colors, so \(p\le\nu(\overline G)\) gives the lower bound. A maximum matching in \(\overline G\), with every unmatched vertex made a singleton color class, attains it. \(\square\)

Thus global independence number two is polynomial, whereas global independence number three is already NP-hard.

## 3. A precise formulation of the \(\alpha(G)\le 3\) even-hole-free slice

Let \(G\) satisfy \(\alpha(G)\le 3\), and put \(H=\overline G\). Then \(H\) is \(K_4\)-free.

Moreover, under the assumption \(\alpha(G)\le 3\), an even hole in \(G\) can only have length four or six: an induced \(C_{2r}\) with \(r\ge4\) contains an independent set of size \(r\ge4\). Now
\[
\overline{C_4}=2K_2,
\]
and \(\overline{C_6}\) is the triangular prism, namely two disjoint triangles joined by a perfect matching. Therefore:

### Proposition 3.1

For a graph \(G\) with \(\alpha(G)\le3\), the following are equivalent:

1. \(G\) is even-hole-free;
2. \(H=\overline G\) is \(K_4\)-free, induced-\(2K_2\)-free, and induced-triangular-prism-free.

There is also an exact optimization formula. Let \(\mathcal T\) range over families of pairwise vertex-disjoint triangles of \(H\), and let \(\nu(H-V(\mathcal T))\) be the matching number after deleting all vertices of those triangles.

### Proposition 3.2

If \(H\) is \(K_4\)-free and \(G=\overline H\), then
\[
\boxed{
\chi(G)
=
|V(H)|
-
\max_{\mathcal T}
\left(
2|\mathcal T|+
\nu\bigl(H-V(\mathcal T)\bigr)
\right).
}
\]

#### Proof

A coloring of \(G\) is a partition of \(V(H)\) into cliques of \(H\). Since \(H\) is \(K_4\)-free, these cliques are triangles, edges, and singletons.

If a clique partition has \(t\) triangles, \(p\) edges, and \(s\) singletons, then
\[
n=3t+2p+s
\]
and its number of classes is
\[
t+p+s=n-(2t+p).
\]
After fixing the disjoint triangle classes \(\mathcal T\), the largest possible number of edge classes among the remaining vertices is exactly
\(\nu(H-V(\mathcal T))\). Maximizing \(2t+p\) proves the formula. \(\square\)

Consequently, the \(\alpha(G)\le3\) portion of the original problem is exactly the following packing problem:

> Given a \((K_4,2K_2,\text{triangular prism})\)-free graph \(H\), maximize
> \[
> 2|\mathcal T|+\nu(H-V(\mathcal T))
> \]
> over vertex-disjoint triangle families \(\mathcal T\).

The general version is NP-hard by Proposition 2.1. I do not know how to solve it under these three induced-subgraph exclusions, nor how to prove it NP-hard there. This is a concrete restricted frontier of the original problem.

## 4. Separator parity in even-hole-free graphs

For \(S\subseteq V(G)\) and a component \(C\) of \(G-S\), write
\[
A_C=N(C)\cap S
\]
for its attachment in \(S\).

### Lemma 4.1: two-component parity lemma

Let \(G\) be even-hole-free. Let \(C,D\) be distinct components of \(G-S\), and let \(x,y\in S\) be nonadjacent vertices such that
\[
x,y\in A_C\cap A_D.
\]
Then every induced \(x\)-\(y\) path with interior in \(C\) has parity opposite to every induced \(x\)-\(y\) path with interior in \(D\).

In particular, for a fixed nonedge \(xy\) of \(G[S]\), there are at most two components \(C\) of \(G-S\) with \(x,y\in A_C\).

#### Proof

Choose induced paths \(P_C\) and \(P_D\) from \(x\) to \(y\), with interiors respectively in \(C\) and \(D\). Such paths exist by connectedness of the components; shortest such paths are induced.

The interiors of \(P_C\) and \(P_D\) are anticomplete because \(C\) and \(D\) are distinct components of \(G-S\). Since \(xy\notin E(G)\), the union
\[
P_C\cup P_D
\]
is an induced cycle of length
\[
|E(P_C)|+|E(P_D)|\ge4.
\]
If the two paths had the same parity, this cycle would be even, contradicting that \(G\) is even-hole-free. Thus their parities are opposite.

If three components all had both \(x\) and \(y\) in their attachments, two of the corresponding paths would have the same parity, again producing an even hole. \(\square\)

An immediate useful formulation is
\[
A_{C_1}\cap A_{C_2}\cap A_{C_3}
\quad\text{is a clique}
\]
for any three distinct components of \(G-S\).

A component \(C\) of \(G-S\) is **full** if \(N(C)=S\). The standard characterization of a minimal separator says that it has at least two full components.

### Corollary 4.2

Every nonclique minimal separator \(S\) in an even-hole-free graph has exactly two full components.

Moreover, if \(C,D\) are these two full components and \(x,y\in S\) are nonadjacent, then:

- all induced \(x\)-\(y\) paths through \(C\) have the same parity;
- all induced \(x\)-\(y\) paths through \(D\) have the opposite parity.

#### Proof

There are at least two full components. Choose a nonedge \(xy\) in \(S\). Every full component contains both \(x\) and \(y\) in its attachment, so Lemma 4.1 gives at most two full components.

For parity uniqueness, fix an induced \(x\)-\(y\) path \(Q\) through \(D\). If \(C\) contained induced paths of both parities, one of them would have the same parity as \(Q\), contradicting Lemma 4.1. The argument is symmetric for \(D\). \(\square\)

This is a sharp structural restriction, but it does not bound \(|S|\).

## 5. Exact coloring across separators

The separator obstruction can be stated exactly in terms of color-equality profiles.

Let \(C_1,\ldots,C_r\) be the components of \(G-S\), and set
\[
G_i=G[S\cup C_i].
\]
A proper coloring of \(S\) induces a partition \(\pi\) of \(S\) into stable sets, where two vertices lie in the same block exactly when they receive the same color. Let \(\chi_\pi(G_i)\) be the minimum number of colors in a coloring of \(G_i\) inducing exactly \(\pi\) on \(S\).

### Proposition 5.1: separator profile formula

\[
\boxed{
\chi(G)
=
\min_{\pi}
\max_{1\le i\le r}\chi_\pi(G_i),
}
\]
where \(\pi\) ranges over all partitions of \(S\) into stable sets.

#### Proof

Any coloring of \(G\) induces some profile \(\pi\), and its restriction to each \(G_i\) proves the lower bound.

Conversely, fix \(\pi\) and put
\[
k=\max_i\chi_\pi(G_i).
\]
Choose for each \(i\) a \(k\)-coloring of \(G_i\) inducing \(\pi\), allowing unused colors. The blocks of \(\pi\) receive distinct color labels. By permuting the \(k\) labels separately inside each \(G_i\), all these colorings can be made identical on \(S\). They then combine because distinct components of \(G-S\) are anticomplete. \(\square\)

For \(|S|=2\) and \(S\) nonadjacent, there are only two states: the two separator vertices receive the same color or different colors. For large star cutsets, however, the number of stable partitions may be exponential.

### A sharp even-hole-free obstruction to naïve gluing

Let
\[
C=x-a-y-d-b-x
\]
be a \(5\)-cycle, and add a universal vertex \(u\). The resulting graph
\[
G=K_1\vee C_5
\]
is even-hole-free: every hole avoids \(u\), and the only hole is the original \(C_5\).

Let
\[
S=\{u,x,y\}.
\]
This is a minimal star cutset centered at \(u\). The components of \(G-S\) are
\[
C_1=\{a\},\qquad C_2=\{b,d\},
\]
and both are full.

Each block \(G[S\cup C_i]\) is \(3\)-colorable:

- \(G[S\cup C_1]\) is a universal vertex joined to the path \(x-a-y\);
- \(G[S\cup C_2]\) is a universal vertex joined to the path \(x-b-d-y\).

Nevertheless,
\[
\chi(G)=\chi(K_1\vee C_5)=1+\chi(C_5)=4.
\]

The reason is profile incompatibility. In a \(3\)-coloring of the first block, \(x\) and \(y\) must receive the same color; in a \(3\)-coloring of the second block they must receive different colors. In the notation of Proposition 5.1,
\[
\begin{array}{c|cc}
 & x=y & x\ne y\\ \hline
G[S\cup C_1] & 3 & 4\\
G[S\cup C_2] & 4 & 3
\end{array}
\]
and therefore
\[
\chi(G)=\min\{\max(3,4),\max(4,3)\}=4.
\]

Thus even for an even-hole-free graph with a minimal star cutset and exactly two full components,
\[
\chi(G)\ne\max_i\chi(G[S\cup C_i])
\]
can occur. The opposite path parities from Lemma 4.1 explain the incompatibility but do not remove it.

### A positive gluing case

There is one useful situation in which profiles are unnecessary.

### Proposition 5.2

Suppose every component \(C_i\) of \(G-S\) has a clique attachment
\[
A_i=N(C_i)\cap S.
\]
Then
\[
\boxed{
\chi(G)=
\max\left(
\chi(G[S]),
\max_i\chi(G[C_i\cup A_i])
\right).
}
\]

#### Proof

Only the upper bound needs proof. Let the right-hand side be \(k\), and fix a \(k\)-coloring of \(G[S]\). Independently choose a \(k\)-coloring of each \(G[C_i\cup A_i]\).

Because \(A_i\) is a clique, its vertices receive distinct colors in both colorings. A permutation of the \(k\) colors in the \(i\)-th block can therefore make its coloring agree with the fixed coloring on \(A_i\). These adjusted colorings combine: there are no edges between distinct components, and vertices of \(S\setminus A_i\) have no neighbors in \(C_i\). \(\square\)

This extends the familiar clique-cutset formula, but Lemma 4.1 does not imply that all attachments are cliques.

## 6. Two easy exact slices of the even-hole-free class

Besides the \(\alpha(G)\le2\) matching formula, there is a complementary result for bounded clique number.

I use here the established bisimplicial-vertex theorem for even-hole-free graphs:

> Every nonempty even-hole-free graph has a vertex whose neighborhood is the union of two cliques.

Since the class is hereditary, this gives a bisimplicial elimination ordering. It can be found on a promised input by scanning vertices: \(N(v)\) is the union of two cliques exactly when the complement of \(G[N(v)]\) is bipartite.

If \(\omega(G)=\omega\), then at each elimination step each of the two neighborhood cliques has size at most \(\omega-1\). Reverse greedy coloring therefore uses at most
\[
2\omega-1
\]
colors. This is a polynomial-time constructive bound, but not an exact algorithm.

For \(\omega(G)\le2\), the graph is triangle-free. The neighborhood of a bisimplicial vertex is then simultaneously stable and covered by two cliques, so it has size at most two. Every induced subgraph therefore has a vertex of degree at most two, and the graph is \(2\)-degenerate. Hence it is \(3\)-colorable.

Thus exact coloring is easy for triangle-free even-hole-free graphs:
\[
\chi(G)=
\begin{cases}
0,&V(G)=\varnothing,\\
1,&E(G)=\varnothing,\ V(G)\ne\varnothing,\\
2,&G\text{ is bipartite and has an edge},\\
3,&G\text{ is not bipartite}.
\end{cases}
\]

## 7. Remaining gaps

The arguments above do not settle the catalog problem.

- Proposition 2.1 only shows that tree-independence number is an insufficient generic parameter. Its hardness outputs are not restricted to even-hole-free graphs.
- In the \(\alpha(G)\le3\) slice, the unresolved issue is the triangle-packing-plus-matching problem on \((K_4,2K_2,\text{triangular prism})\)-free graphs.
- Lemma 4.1 controls parity and the number of full components, but not the size of a nonclique separator.
- Proposition 5.1 may require exponentially many stable partitions of a large star cutset. The universal-\(C_5\) example shows that these profiles cannot simply be discarded.
- The bisimplicial ordering gives a polynomial \(2\omega-1\) coloring, not \(\chi(G)\).

Accordingly, no polynomial exact-coloring algorithm and no NP-hardness proof for the full even-hole-free class is established here.