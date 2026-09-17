```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every triangle-free odd-regular graph of degree at least three whose 4-cycles are pairwise edge-disjoint has a friendly partition.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not settled; novelty of this stronger special case is not claimed."
}
```

## 1. Result and scope

Graphs below are finite, simple, undirected, and nonempty. Both classes of a friendly partition must be **nonempty**.

I do not resolve the full conjecture. I prove the following extension of the girth-five result in the supplied attempt.

**Theorem.** Let \(k\ge 2\). Suppose \(G\) is a \((2k-1)\)-regular triangle-free graph, and every edge of \(G\) belongs to at most one cycle of length four. Then \(G\) has a friendly partition.

Thus the theorem allows four-cycles, even four-cycles sharing vertices, provided that distinct four-cycles do not share an edge. In particular, it applies to this class of 5-regular graphs.

I checked the core-extension and extremal-degenerate-partition arguments from the previous attempt; they are valid and are proved again below. The additional argument uses a two-exchange operation to handle the permitted four-cycles. No literature result is needed, and I have not established whether a published theorem already subsumes this special case.

## 2. Two cores and an extremal partition

Call a nonempty vertex set \(X\) a **\(k\)-core set** if
\[
\delta(G[X])\ge k.
\]
A graph is \((k-1)\)-degenerate precisely when it contains no \(k\)-core set.

### Lemma 1: extending two cores

A \((2k-1)\)-regular graph has a friendly partition if and only if it contains two disjoint \(k\)-core sets.

**Proof.** The classes of a friendly partition are themselves \(k\)-core sets.

Conversely, let \(X,Y\) be disjoint \(k\)-core sets. Among partitions
\[
V(G)=A\mathbin{\dot\cup}B,\qquad X\subseteq A,\quad Y\subseteq B,
\]
choose one minimizing the number of crossing edges.

Vertices of \(X\cup Y\) already have at least \(k\) neighbours in their own classes. If any other vertex had more neighbours across the partition than within its class, transferring it would decrease the cut while retaining \(X\) and \(Y\) in their prescribed classes. This is impossible by minimality. The partition is therefore friendly. ∎

### Lemma 2: intersections of cores

If \(P,Q\) are \(k\)-core sets in a graph of maximum degree at most \(2k-1\), then either \(P\cap Q=\varnothing\), or
\[
\delta(G[P\cap Q])\ge1.
\]

**Proof.** For \(v\in P\cap Q\),
\[
d_{P\cap Q}(v)
=d_P(v)+d_Q(v)-d_{P\cup Q}(v)
\ge 2k-(2k-1)=1.
\]
∎

Now suppose, towards proving the theorem, that \(G\) has **no** friendly partition.

There is a partition into two \((k-1)\)-degenerate induced subgraphs: a maximum cut has internal degree at most \(k-1\) at every vertex. Among all such partitions, maximize
\[
F(A,B)=e(G[A])+e(G[B]).
\]
Call a partition achieving this maximum **extremal**. Both classes of an admissible partition are nonempty, since \(G\) itself is not \((k-1)\)-degenerate.

For an extremal partition define
\[
L_A=\{x\in A:d_A(x)\le k-1\},\qquad
L_B=\{y\in B:d_B(y)\le k-1\}.
\]
Both sets are nonempty.

### Lemma 3: the low-degree sets are completely joined

For every extremal partition:

1. every vertex of \(L_A\) has internal degree exactly \(k-1\);
2. every vertex of \(L_B\) has internal degree exactly \(k-1\);
3. every vertex of \(L_A\) is adjacent to every vertex of \(L_B\).

**Proof.** Fix \(x\in L_A\). Transferring \(x\) to \(B\) would increase \(F\) by
\[
(2k-1)-2d_A(x)\ge1.
\]
Deleting \(x\) preserves degeneracy of \(G[A]\), so extremality implies that \(G[B\cup\{x\}]\) contains a \(k\)-core set \(Q_x\). Necessarily \(x\in Q_x\).

Similarly, for every \(y\in L_B\), there is a \(k\)-core set
\[
P_y\subseteq A\cup\{y\},\qquad y\in P_y.
\]

By Lemma 1, \(P_y\) and \(Q_x\) cannot be disjoint. Their intersection is contained in \(\{x,y\}\); Lemma 2 therefore gives
\[
P_y\cap Q_x=\{x,y\},\qquad xy\in E(G).
\]
Moreover,
\[
k\le d_{P_y}(x)\le d_A(x)+1\le k,
\]
so \(d_A(x)=k-1\). The argument for \(y\) is symmetric. ∎

### Lemma 4: exchanging opposite low-degree vertices

If \(x\in L_A\) and \(y\in L_B\), then swapping \(x,y\) produces another extremal partition.

**Proof.** By Lemma 3, \(xy\in E(G)\), and each of \(x,y\) has exactly \(k\) crossing neighbours. Thus, after the swap, each has internal degree \(k-1\).

Each new class is obtained from a degenerate graph by adding a vertex with at most \(k-1\) neighbours, so remains \((k-1)\)-degenerate. Each class loses \(k-1\) internal edges and gains \(k-1\), so \(F\) is unchanged. ∎

## 3. Consequences of the forbidden short-cycle configurations

From now on use the hypotheses that \(G\) is triangle-free and no edge belongs to two distinct four-cycles.

Two observations will be used repeatedly:

- \(L_A\) and \(L_B\) are independent, by triangle-freeness and Lemma 3.
- Any two vertices have at most two common neighbours. Three common neighbours would form a \(K_{2,3}\), in which an edge belongs to two distinct four-cycles.

For \(x\in L_A\), write
\[
D_A(x)=\{a\in N_A(x):d_A(a)=k\},
\]
and define \(D_B(y)\) symmetrically.

If \(x\in L_A,y\in L_B\) are swapped, producing \(A',B'\), then
\[
L_{A'}=\{y\}\cup D_A(x),\qquad
L_{B'}=\{x\}\cup D_B(y).                         \tag{1}
\]

Indeed, every old low-degree vertex of \(A\setminus\{x\}\) gains \(y\) as a neighbour and loses no neighbour, so its internal degree becomes \(k\). A vertex of internal degree \(k\) adjacent to \(x\) loses \(x\) and cannot gain \(y\), because \(xy\) is an edge and \(G\) is triangle-free. These are exactly the old vertices becoming low-degree in \(A'\). The argument for \(B'\) is identical.

### Lemma 5: one low-degree set is a singleton

For every extremal partition,
\[
\min\{|L_A|,|L_B|\}=1.
\]

**Proof.** Suppose both low-degree sets have size at least two. Since they are completely joined and \(G\) contains no \(K_{2,3}\), both have size exactly two.

Every vertex of \(A\) has at most one neighbour in \(L_A\): otherwise the two vertices of \(L_A\) would have that vertex and both vertices of \(L_B\) as three common neighbours.

There must consequently be
\[
x\in L_A,\qquad a\in D_A(x).
\]
Otherwise, deleting \(L_A\) would leave a nonempty graph of minimum degree at least \(k\): vertices of degree \(k\) would lose no neighbours, and vertices of larger degree would lose at most one. This contradicts degeneracy. Nonemptiness follows because vertices of \(L_A\) have \(k-1\ge1\) internal neighbours and \(L_A\) is independent.

Similarly choose
\[
y\in L_B,\qquad b\in D_B(y).
\]

The original low-degree sets give a four-cycle containing \(xy\). After swapping \(x,y\), equation (1) and Lemma 3 force \(ab\in E(G)\). Hence
\[
x,a,b,y,x
\]
is another four-cycle containing \(xy\). These cycles are distinct because \(a\notin L_A\) and \(b\notin L_B\), a contradiction. ∎

## 4. The structure around a singleton low-degree set

Consider any extremal partition with
\[
L_A=\{x\},\qquad Y=L_B.
\]

### Lemma 6: a square through the singleton

The following hold:

1. \(D_A(x)\ne\varnothing\);
2. \(D_B(y)=\varnothing\) for every \(y\in Y\);
3. there are distinct \(y,z\in Y\) and \(w\in B\setminus Y\) such that
   \[
   d_B(w)=k+1,\qquad wy,wz\in E(G).
   \]
   In particular,
   \[
   x,y,w,z,x                                             \tag{2}
   \]
   is a four-cycle.

**Proof.**

Since \(x\) is the only low-degree vertex in \(A\), deleting \(x\) must expose a vertex of degree at most \(k-1\). Such a vertex originally had degree \(k\) and was adjacent to \(x\). Thus \(D_A(x)\ne\varnothing\).

For any \(y\in Y\), swap \(x,y\). By (1), the new low-degree set on the \(A\)-side has at least two vertices. Lemma 5 forces the other low-degree set to be the singleton \(\{x\}\). Equation (1) therefore gives \(D_B(y)=\varnothing\).

Now \(B\setminus Y\) is nonempty: every vertex of \(Y\) has \(k-1\ge1\) internal neighbours, and \(Y\) is independent. Choose a vertex \(w\) having degree at most \(k-1\) in \(G[B\setminus Y]\).

Its original degree in \(B\) cannot be \(k\), because no degree-\(k\) vertex of \(B\) is adjacent to \(Y\). Hence
\[
d_B(w)\ge k+1.
\]
On the other hand, \(w\) has at most two neighbours in \(Y\), since all vertices of \(Y\) are neighbours of \(x\). Thus
\[
d_B(w)\le d_{B\setminus Y}(w)+2\le k+1.
\]
Equality holds throughout: \(d_B(w)=k+1\), and \(w\) has two neighbours \(y,z\in Y\). Lemma 3 supplies \(xy,xz\), giving (2). ∎

### Lemma 7: exactly one degree-\(k\) neighbour

Under the same hypotheses,
\[
|D_A(x)|=1.
\]

**Proof.** First note an additional permissible exchange. If
\[
a\in D_A(x),\qquad y\in Y,
\]
we may exchange \(a,y\), leaving \(x\) in \(A\), and obtain another extremal partition.

To see this, first swap \(x,y\). Equation (1) makes \(a\) low-degree, while \(x\) is low-degree in the other class. Swap \(a,x\). The composition exchanges precisely \(a,y\).

Suppose now that \(a_1,a_2\) are distinct vertices of \(D_A(x)\), and take the square
\[
x,y,w,z,x
\]
from Lemma 6.

Exchange \(a_1,y\), keeping \(x\) in \(A\). All of \(a_1,a_2,y,z\) are neighbours of \(x\), hence are pairwise nonadjacent by triangle-freeness. Consequently:

- \(x\) remains low-degree;
- \(a_2\) still has internal degree \(k\);
- \(z\) remains low-degree.

We may therefore exchange \(a_2,z\) as well. Both exchanges preserve extremality.

The resulting partition is
\[
A''=(A\setminus\{a_1,a_2\})\cup\{y,z\},\qquad
B''=(B\setminus\{y,z\})\cup\{a_1,a_2\}.
\]

The vertices \(x,w\) already have the two common neighbours \(y,z\), so \(w\) is adjacent to neither \(a_1\) nor \(a_2\). Thus \(w\) loses exactly two internal neighbours and gains none:
\[
d_{B''}(w)=k+1-2=k-1.
\]
Meanwhile \(x\) remains low-degree in \(A''\).

Lemma 3 forces \(xw\in E(G)\). But \(xw\) would form a triangle with \(y\), a contradiction. Hence \(|D_A(x)|\le1\), and Lemma 6 gives equality. ∎

## 5. Completion of the theorem

Choose an extremal partition. By Lemma 5, orient its classes so that
\[
L_A=\{x\}.
\]
By Lemmas 6–7, write
\[
D_A(x)=\{a\},
\]
and choose a four-cycle
\[
Q=x,y,w,z,x
\]
as in Lemma 6.

Swap \(x,y\). Equation (1) gives exactly
\[
L_{A'}=\{y,a\},\qquad L_{B'}=\{x\}.
\]

Apply Lemma 6 to this new extremal partition, with the roles of the classes reversed. Since its nonsingleton low-degree set is precisely \(\{y,a\}\), there is a vertex
\[
w'\in A'\setminus\{y,a\}
\]
adjacent to both \(y,a\). Therefore
\[
Q'=x,y,w',a,x
\]
is a four-cycle.

The cycles \(Q,Q'\) share the edge \(xy\). They are distinct because \(a\) is not a vertex of \(Q\). This contradicts the hypothesis on four-cycles and completes the proof. ∎

## 6. An even-degree consequence

The theorem also gives a special case for even degrees.

**Corollary.** Let \(k\ge2\). Suppose \(G\) is a \(2k\)-regular triangle-free graph whose four-cycles are pairwise edge-disjoint. If \(G\) has a perfect matching, then \(G\) has a friendly partition.

**Proof.** Delete a perfect matching \(M\). The graph \(G-M\) is \((2k-1)\)-regular and retains both short-cycle restrictions. The theorem gives a partition in which every vertex has at least \(k\) neighbours in its own class in \(G-M\). The same partition is friendly in the \(2k\)-regular graph \(G\). ∎

In particular, this covers every regular bipartite graph of degree at least three whose four-cycles are pairwise edge-disjoint: odd degrees use the theorem directly, while positive-degree regular bipartite graphs have perfect matchings by Hall’s theorem.

## 7. What remains unresolved

The result strengthens the necessary local structure of a possible odd-regular counterexample:

> A \((2k-1)\)-regular graph without a friendly partition must contain either a triangle or two distinct four-cycles sharing an edge.

The previous girth-five argument only forced a triangle or a four-cycle.

This is still not a bound on the order of counterexamples. The proof does not control graphs containing triangles or overlapping four-cycles, and these configurations can occur in graphs of arbitrarily large order. In particular, no threshold \(N(5)\), or threshold for any other unrestricted open degree, is obtained here.