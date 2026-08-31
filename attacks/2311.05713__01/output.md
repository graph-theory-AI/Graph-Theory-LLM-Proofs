```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every fixed k at least 5, k-Coloring is NP-complete on P10-free graphs and, more generally, whenever H contains P10, 3P4, 2P5, or 2P4+P2 as an induced subgraph.",
  "would_publish": false,
  "caveats": "This is an elementary consequence of the source paper's list-hardness theorem; it leaves k=3,4 and many linear forests untreated, and novelty has not been literature-checked."
}
```

## 1. Statement of the partial result

All occurrences of “subgraph” below mean induced subgraph. Write \(F_1+F_2\) for disjoint union.

### Theorem

Let \(k\geq 5\) be fixed. The \(k\)-Coloring Problem is NP-complete on \(H\)-free graphs whenever \(H\) contains at least one of

\[
P_{10},\qquad 3P_4,\qquad 2P_5,\qquad 2P_4+P_2
\]

as an induced subgraph.

In particular:

1. \(k\)-Coloring is NP-complete on \(P_t\)-free graphs for every \(t\geq 10\);
2. it is NP-complete on \(rP_4\)-free graphs for every \(r\geq 3\);
3. it is NP-complete on \(rP_5\)-free graphs for every \(r\geq 2\).

Combined with the polynomial side of the source theorem, this gives the following path bracket for every fixed \(k\geq5\):

\[
\begin{array}{c|c}
H=P_t & \text{complexity of \(k\)-Coloring on \(H\)-free graphs}\\ \hline
t\leq5 & \text{polynomial}\\
t\geq10 & \text{NP-complete}.
\end{array}
\]

The cases \(t=6,7,8,9\) are not decided by the argument below.

---

## 2. External input from the source paper

Let

\[
B:=P_4+P_2.
\]

The hardness half of the theorem of Chudnovsky, Hajebi and Spirkl gives, for every fixed \(k>4\),

\[
\text{List-\(k\)-Coloring is NP-complete on \(B\)-free graphs.}
\]

Indeed, \(B\) satisfies neither polynomial condition in their dichotomy:

- it has a \(P_4\)-component, so not every component has at most three vertices;
- it has six nonisolated vertices, so it is not an induced subgraph of \(P_5\).

This is the only external hardness theorem used below.

---

## 3. Palette reduction

### Lemma 1

Let \(F,J\) be fixed graphs and \(k\) a fixed positive integer. Suppose List-\(k\)-Coloring is NP-hard on \(F\)-free graphs. Assume that

\[
\tag{\(*\)}
J-X\text{ contains an induced }F
\]

for every clique \(X\subseteq V(J)\) with \(|X|\leq k\), including \(X=\varnothing\). Then \(k\)-Coloring is NP-hard on \(J\)-free graphs.

### Proof

Let \((G,L)\) be an \(F\)-free List-\(k\)-Coloring instance, with every list contained in \([k]=\{1,\dots,k\}\).

Construct \(G^\star\) by adding a clique

\[
C=\{c_1,\dots,c_k\},
\]

and, for every \(v\in V(G)\), adding the edge \(vc_i\) precisely when \(i\notin L(v)\).

We first verify equivalence.

- If \(G\) has an \(L\)-coloring, color \(c_i\) with \(i\). This extends to a proper \(k\)-coloring of \(G^\star\).
- Conversely, in every proper \(k\)-coloring of \(G^\star\), the \(K_k\) induced by \(C\) uses all \(k\) colors. Relabeling colors, we may assume \(c_i\) has color \(i\). Since \(v\) is adjacent to every \(c_i\) with \(i\notin L(v)\), its color belongs to \(L(v)\). Thus the restriction to \(G\) is an \(L\)-coloring.

It remains to prove that \(G^\star\) is \(J\)-free. Suppose it contained an induced copy of \(J\). The vertices of this copy lying in \(C\) correspond to a clique \(X\) of \(J\), with \(|X|\leq k\). All vertices corresponding to \(J-X\) lie in \(G\), and induce \(J-X\) there. By \((*)\), they contain an induced \(F\), contradicting the fact that \(G\) is \(F\)-free.

The reduction is polynomial, proving NP-hardness. ∎

---

## 4. Robust forbidden graphs

Call a graph \(J\) \(B\)-robust if \(J-X\) contains an induced \(B=P_4+P_2\) for every clique \(X\) of \(J\).

### Lemma 2

Each of

\[
P_{10},\qquad 3P_4,\qquad 2P_5,\qquad 2P_4+P_2
\]

is \(B\)-robust.

### Proof

Because these are linear forests, every clique has at most two vertices, and a two-vertex clique consists of adjacent vertices in one path component.

#### The graph \(P_{10}\)

After deleting a clique \(X\), the remaining graph has at most two path components and at least eight vertices. Write it as \(P_a+P_b\), allowing \(b=0\), where \(a+b\geq8\) and \(a\geq b\).

- If \(a\geq7\), then \(P_a\) contains an induced \(P_4+P_2\): take four consecutive vertices, omit the next vertex, and take the following two.
- If \(a\leq6\), then \(a+b\geq8\) implies \(a\geq4\) and \(b\geq2\). Take a \(P_4\) from the first component and a \(P_2\) from the second.

Thus \(P_{10}-X\) always contains \(B\).

#### The graph \(3P_4\)

A clique \(X\) meets at most one component. Hence at least two \(P_4\)-components remain intact. One supplies the \(P_4\), and an edge of the other supplies the disjoint \(P_2\).

#### The graph \(2P_5\)

Again \(X\) meets at most one component. The untouched \(P_5\) contains a \(P_4\). Deleting at most two adjacent vertices from the other \(P_5\) always leaves an edge, which supplies the \(P_2\).

#### The graph \(2P_4+P_2\)

If \(X\) meets one of the \(P_4\)-components, the other \(P_4\) and the \(P_2\)-component remain intact. If \(X\) meets the \(P_2\)-component, both \(P_4\)'s remain intact; one supplies \(P_4\), and an edge of the other supplies \(P_2\). ∎

Applying Lemma 1 with \(F=B\) proves NP-hardness on the free classes of all four graphs. Membership in NP is immediate, so the problems are NP-complete.

If \(H\) contains one of these four graphs, every graph avoiding that smaller graph also avoids \(H\). The theorem follows.

---

## 5. Exact description of this robustness condition for linear forests

The four graphs above are not an arbitrary selection.

### Lemma 3

A linear forest \(J\) is \(B\)-robust if and only if it contains at least one of

\[
P_{10},\qquad 3P_4,\qquad 2P_5,\qquad 2P_4+P_2
\]

as an induced subgraph.

### Proof

The reverse implication follows from Lemma 2. Indeed, if \(S\) is an induced \(B\)-robust subgraph of \(J\), then for every clique \(X\) of \(J\), the set \(X\cap V(S)\) is a clique of \(S\), and

\[
S-(X\cap V(S))\subseteq J-X
\]

contains \(B\).

For the forward implication, ignore isolated vertices and list the path-component orders of \(J\). Let \(q\) be the number of components of order at least four.

- If some component has order at least ten, then \(J\) contains \(P_{10}\).
- If \(q\geq3\), then \(J\) contains \(3P_4\).
- Suppose \(q=2\), with component orders \(a\geq b\geq4\).
  - If \(b\geq5\), then \(J\) contains \(2P_5\).
  - If \(b=4\) and \(a\geq7\), then the \(P_a\)-component contains an induced \(P_4+P_2\); together with the other \(P_4\), this gives \(2P_4+P_2\).
  - If \(b=4\) and \(a\leq6\), robustness forces a third component of order at least two. Otherwise, deleting the middle edge of the \(P_4\)-component leaves only a path of order at most six and isolated vertices, which cannot contain \(P_4+P_2\). Such a third component yields \(2P_4+P_2\).
- Suppose \(q=1\), and let the unique component of order at least four have order \(a\).
  - If \(a\leq8\), one can delete two adjacent central vertices so that all remaining path components have order at most three. Then no \(P_4\) remains, contradicting robustness.
  - Since there is no \(P_{10}\), the only possibility is \(a=9\). Robustness then forces another component containing an edge: otherwise deleting the second and third vertices of the \(P_9\) leaves \(P_1+P_6\), which does not contain \(P_4+P_2\). But \(P_9\) contains \(2P_4\), and the additional edge gives \(2P_4+P_2\).
- If \(q=0\), \(J\) itself contains no \(P_4\), so it is not robust.

This exhausts all linear forests. ∎

Thus the theorem captures exactly what the elementary palette reduction can obtain from \(B\)-free list-coloring through this robustness criterion.

---

## 6. Polynomial side inherited from List-\(k\)-Coloring

Since ordinary \(k\)-Coloring is the special case in which every list is \([k]\), the polynomial algorithms from the source theorem apply directly.

For every fixed \(k\geq1\), \(k\)-Coloring on \(H\)-free graphs is polynomial-time solvable if either:

1. every component of \(H\) is a path on at most three vertices; or
2. deleting the isolated vertices of \(H\) leaves an induced subgraph of \(P_5\).

For example:

- \(P_t\)-free \(k\)-Coloring is polynomial for \(t\leq5\);
- \(P_4\)-free and \(P_5\)-free \(k\)-Coloring are polynomial;
- the same holds when arbitrary isolated vertices are added to \(P_4\) or \(P_5\).

Together with the hardness result, this leaves, within the path family for \(k\geq5\), only \(P_6,P_7,P_8,P_9\) untreated by this argument.

---

## 7. Why this particular method stops at \(P_9\)

The failure at \(P_9\) is structural, not merely a loose estimate.

Every linear forest \(F\) on the hard side of the source List-\(k\)-Coloring dichotomy contains either

\[
P_6\quad\text{or}\quad P_4+P_2.
\]

Indeed, if \(F\) has a component of order at least six, it contains \(P_6\). Otherwise, failure of both polynomial conditions requires a \(P_4\)- or \(P_5\)-component together with another nontrivial component, giving \(P_4+P_2\).

Label \(P_9=v_1\cdots v_9\). Consider the two edge-cliques

\[
X_1=\{v_2,v_3\},\qquad X_2=\{v_4,v_5\}.
\]

Then

\[
P_9-X_1=P_1+P_6,\qquad
P_9-X_2=P_3+P_4.
\]

The first graph contains no \(P_4+P_2\), while the second contains no \(P_6\). Consequently, there is no single linear forest \(F\) from the hard side of the source dichotomy that is contained in \(P_9-X\) for every clique \(X\).

Therefore Lemma 1, used as a black box with one forbidden graph \(F\), cannot establish hardness for \(P_9\)-free graphs. This does not rule out a different reduction, or list-coloring hardness under simultaneous forbidden-subgraph restrictions.

---

## 8. Gaps and status

This does not solve the catalog problem.

- It gives no new hardness conclusion for \(k=3\) or \(k=4\).
- For \(k\geq5\), it leaves many linear forests untreated, including \(P_6,\ldots,P_9\), \(2P_4\), and \(P_4+P_2\) itself.
- The obstruction above applies only to the basic palette reduction and a single forbidden graph used as a black-box list-hardness source.
- The \(P_{10}\) bound and the robust-core formulation are elementary enough that they may already be known; no claim of novelty is made without a dedicated literature search.