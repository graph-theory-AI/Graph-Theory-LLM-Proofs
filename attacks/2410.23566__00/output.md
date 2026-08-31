```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The literal statement fails for a directed triangle, while for the intended acyclic formulation there is a linear bound when mad(D)≤2 and a polynomial bound for a height-two one-sided bounded-degree subclass.",
  "would_publish": false,
  "caveats": "Acyclicity is evidently implicit in the source problem; the general acyclic case for fixed alpha>2 remains open."
}
```

## 1. Interpretation

Write \(\underline D\) for the underlying simple graph of an oriented graph \(D\), and use the standard convention
\[
\operatorname{mad}(D)
 =\max_{\varnothing\ne H\subseteq \underline D}
 \frac{2|E(H)|}{|V(H)|}.
\]
Also, \(\operatorname{unvd}(D)\) is the least \(N\) such that every tournament of order \(N\) contains \(D\) as a subdigraph.

A necessary condition for finite unavoidability is that \(D\) be acyclic: a transitive tournament contains no directed cycle.

### Literal formulation

As written, without an acyclicity hypothesis, the statement is false. Let \(D\) be the directed triangle. Then
\[
\operatorname{mad}(D)=2,
\]
but transitive tournaments of arbitrary order avoid \(D\), so
\[
\operatorname{unvd}(D)=\infty.
\]
Thus no polynomial \(P_2\) can satisfy the displayed assertion for every digraph of maximum average degree at most \(2\).

In the source context, however, \(\operatorname{unvd}\) is evidently intended only for acyclic digraphs. I address that corrected formulation below.

---

## 2. A linear bound when \(\operatorname{mad}(D)\le 2\)

I use the following theorem stated in the supplied source paper:

> If an acyclic digraph \(D^\ast\) is obtained from an oriented tree \(F\) by adding \(k\) universal vertices, then
> \[
> \operatorname{unvd}(D^\ast)
> \le 2\cdot 3^{(k+1)(2k+1)}|V(F)|.
> \]

Here “universal” means adjacent to every other vertex, with directions chosen so that the resulting digraph is acyclic.

We first record a slightly more general consequence.

### Proposition 2.1

Fix \(k\ge 0\). Let \(D\) be an acyclic digraph such that every connected component \(H\) of \(\underline D\) has cyclomatic number
\[
\mu(H):=|E(H)|-|V(H)|+1\le k.
\]
Then
\[
\operatorname{unvd}(D)\le C_k|V(D)|
\]
for a constant \(C_k\) depending only on \(k\). One may take, apart from irrelevant components of order at most \(k\),
\[
C_k=2\cdot 3^{(k+1)(2k+1)}.
\]

#### Proof

It suffices first to consider a connected component \(D_0\), with underlying graph \(H\).

Choose a spanning tree \(Q\) of \(H\). There are exactly \(\mu(H)\le k\) edges of \(H\setminus Q\). Choose one endpoint of each such edge and let \(S\) be the set of chosen vertices. Then
\[
|S|\le k
\]
and \(H-S\) is a forest.

Fix a topological ordering \(\prec\) of \(D_0\). Connect the components of \(H-S\) by additional edges to obtain a tree \(F\) on \(V(D_0)\setminus S\), orienting every added edge forward according to \(\prec\). Now add every missing adjacency incident with \(S\), including adjacencies inside \(S\), again orienting each new edge forward according to \(\prec\). The resulting digraph \(D^\ast\)

1. is acyclic;
2. contains \(D_0\);
3. is obtained from the oriented tree \(F\) by adding at most \(k\) universal vertices.

The source theorem therefore gives
\[
\operatorname{unvd}(D_0)\le \operatorname{unvd}(D^\ast)
 \le C_k |V(D_0)|.
\]

For a disconnected \(D\), partition an arbitrary tournament of order \(C_k|V(D)|\) into blocks of orders \(C_k|V(D_i)|\), one for each component \(D_i\), and embed each component in its corresponding block. The embeddings are disjoint. ∎

### Corollary 2.2

For every acyclic digraph \(D\) satisfying
\[
\operatorname{mad}(D)\le 2,
\]
we have the explicit linear estimate
\[
\operatorname{unvd}(D)\le 1458\,|V(D)|.
\]

#### Proof

Let \(H\) be a connected component of \(\underline D\). Since \(H\) itself is among the subgraphs considered in the maximum average degree,
\[
\frac{2|E(H)|}{|V(H)|}\le 2,
\]
and hence \(|E(H)|\le |V(H)|\). Therefore
\[
\mu(H)=|E(H)|-|V(H)|+1\le 1.
\]
Apply Proposition 2.1 with \(k=1\). The constant from the source theorem is
\[
2\cdot 3^{(1+1)(2\cdot1+1)}
 =2\cdot 3^6
 =1458.
\]
∎

Thus the intended conjecture has an affirmative, indeed linear, answer throughout the full range \(\alpha\le 2\).

---

## 3. A polynomial height-two result

The following independent lemma handles some bounded-average-degree examples with arbitrarily large maximum degree.

### Proposition 3.1

Let \(D\) be a height-two acyclic digraph with a partition
\[
V(D)=A\mathbin{\dot\cup} B
\]
such that every arc goes from \(A\) to \(B\). Suppose every \(b\in B\) has indegree at most \(d\), where \(d\ge1\) is fixed. Then, with \(n=|V(D)|\),
\[
\operatorname{unvd}(D)
 \le Q_d(n):=
 4^d\bigl(d(2n)^d+n\bigr).
\]
In particular, this is a polynomial of degree \(d\).

The reverse statement holds if every \(a\in A\) has outdegree at most \(d\).

#### Proof

Let \(T\) be a tournament on
\[
N\ge 4^d\bigl(d(2n)^d+n\bigr)
\]
vertices. For \(S\subseteq V(T)\), write
\[
\Gamma^+(S)=\{y\in V(T):x\to y\text{ for every }x\in S\}.
\]

We first find a set \(U\subseteq V(T)\) of size at least \(n\) such that
\[
|\Gamma^+(S)|\ge 2n
\qquad\text{for every }S\subseteq U,\quad 1\le |S|\le d.
\tag{1}
\]

Choose \(d\) vertices \(y_1,\dots,y_d\) independently and uniformly from \(V(T)\), with repetition, and let
\[
X=\bigcap_{i=1}^d N_T^-(y_i).
\]
Thus \(x\in X\) precisely when \(x\to y_i\) for every \(i\). By convexity and
\(\sum_x d_T^+(x)=\binom N2\),
\[
\begin{aligned}
\mathbb E|X|
 &=\sum_{x\in V(T)}
   \left(\frac{d_T^+(x)}N\right)^d\\
 &\ge
 N\left(\frac{N-1}{2N}\right)^d
 \ge \frac{N}{4^d}.
\end{aligned}
\tag{2}
\]

Call a set \(S\), with \(1\le |S|\le d\), bad if
\[
|\Gamma^+(S)|<2n.
\]
For a fixed bad \(S\),
\[
\Pr(S\subseteq X)
 =\left(\frac{|\Gamma^+(S)|}{N}\right)^d
 <\left(\frac{2n}{N}\right)^d.
\]
If \(Z\) denotes the number of bad subsets contained in \(X\), then
\[
\mathbb E Z
 \le \sum_{s=1}^d N^s\left(\frac{2n}{N}\right)^d
 \le d(2n)^d.
\tag{3}
\]
From (2) and (3), some choice of \(y_1,\dots,y_d\) satisfies
\[
|X|-Z\ge \frac{N}{4^d}-d(2n)^d\ge n.
\]
Delete one vertex from every bad subset of \(X\). The remaining set \(U\) has size at least \(n\) and contains no bad subset of order at most \(d\), proving (1).

Map \(A\) injectively into \(U\). For each \(b\in B\), its already prescribed candidate set is
\[
C_b=
\bigcap_{a\in N_D^-(b)}
N_T^+(\varphi(a)).
\]
Since \(|N_D^-(b)|\le d\), property (1) gives \(|C_b|\ge2n\); if \(b\) is isolated, \(C_b=V(T)\). After excluding the at most \(n\) vertices used for \(A\), at least \(n\) candidates remain for each \(b\). As \(|B|\le n\), the vertices of \(B\) can be assigned greedily and distinctly. Every required arc \(a\to b\) is then present in \(T\).

Reversing all arcs proves the symmetric assertion. ∎

If every \(b\in B\) has degree at most \(d\), then every subgraph \(J\) of the underlying graph satisfies
\[
|E(J)|\le d\,|B\cap V(J)|\le d|V(J)|,
\]
so \(\operatorname{mad}(D)\le2d\). Thus Proposition 3.1 gives polynomial unavoidability for a genuine bounded-maximum-average-degree class with unbounded maximum degree. In particular, the height-two orientation of an incidence graph in which every incidence vertex has degree two has quadratic unavoidability by this argument.

---

## 4. Remaining gap

These arguments do not settle the intended problem for \(\alpha>2\).

The obstruction is structural:

* For \(\operatorname{mad}(D)\le2\), each connected component has cyclomatic number at most one, so the source paper’s bounded-extension theorem applies componentwise.
* For any fixed \(\alpha>2\), a connected graph of maximum average degree at most \(\alpha\) may have cyclomatic number \(\Theta(n)\), so the number of universal vertices required by Proposition 2.1 is no longer bounded.
* Proposition 3.1 relies on all high degrees being confined to one level of a height-two orientation. Bounded maximum average degree alone does not provide such a one-sided degree bound.

Consequently, the literal formulation is false without “acyclic,” while the corrected conjecture remains unresolved beyond the special cases proved above.