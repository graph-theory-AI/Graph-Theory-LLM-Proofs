```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "In ZFC, every graph omitting K_{n,n,(2^{aleph_0})^+} for some positive integer n is a countable union of triangle-free graphs.",
  "would_publish": false,
  "caveats": "This is a size-unrestricted special case, not a resolution of the original existence question; novelty is not claimed."
}
```

## 1. Reformulation and scope

All graphs below are simple and have set-sized vertex sets. Write
\[
\mathfrak c=2^{\aleph_0}.
\]

A graph is a union of countably many triangle-free graphs if and only if it has an edge-colouring
\[
c:E(G)\longrightarrow\omega
\]
with no monochromatic triangle. Indeed, from a cover one can assign each edge the least index of a covering graph containing it.

Thus the question asks for a \(K_4\)-free graph such that **every** countable edge-colouring has a monochromatic triangle.

I do not construct such a graph in ZFC. The result proved below excludes a substantial class of graphs of arbitrary cardinality and gives necessary subgraph configurations for any counterexample.

## 2. A basic cardinal obstruction

**Observation.** If \(\chi(G)\leq\mathfrak c\), then \(G\) is a union of countably many bipartite graphs.

Choose a proper vertex-colouring
\[
p:V(G)\longrightarrow 2^\omega.
\]
For an edge \(uv\), let
\[
c(uv)=\min\{i<\omega:p(u)(i)\ne p(v)(i)\}.
\]
Every edge of colour \(i\) joins the two sets determined by the \(i\)-th bit of \(p\), so that colour class is bipartite.

Consequently, any graph sought in the problem must satisfy
\[
\chi(G)>\mathfrak c,
\qquad\text{and hence}\qquad
|V(G)|\geq\mathfrak c^+.
\]

## 3. A forbidden-tripartite special case

Here \(K_{a,b,d}\) denotes the complete tripartite graph with part sizes \(a,b,d\).

**Theorem.** Fix a positive integer \(n\). If a graph \(G\) contains no subgraph isomorphic to
\[
K_{n,n,\mathfrak c^+},
\]
then \(G\) is a union of countably many triangle-free graphs.

The theorem does **not** require \(G\) to be \(K_4\)-free.

It follows that every graph sought in the problem must contain \(K_{n,n,\mathfrak c^+}\) for every positive integer \(n\). In a \(K_4\)-free graph, each such copy is automatically induced: an edge inside one part, together with one vertex from each of the other two parts, would give a \(K_4\).

In particular, any counterexample must:

- have an edge belonging to at least \(\mathfrak c^+\) triangles;
- contain induced \(K_{n,n,\mathfrak c^+}\) for every finite \(n\);
- contain every finite 3-colourable graph as a subgraph.

For example, the theorem settles the decomposition question affirmatively for every graph omitting a fixed finite complete tripartite graph, including \(K_{2,2,2}\).

### An auxiliary vertex-colouring lemma

For a nonempty set \(A\subseteq V(H)\), write
\[
N_H(A)=\bigcap_{a\in A}N_H(a).
\]

**Lemma.** Suppose that, for some positive integer \(n\), every \(n\)-element subset of \(V(H)\) has at most countably many common neighbours. Then \(H\) has a well-ordering in which every vertex has only finitely many earlier neighbours. In particular,
\[
\chi(H)\leq\aleph_0.
\]
This applies, in particular, to every \(K_{n,n}\)-free graph.

**Proof.** For \(S\subseteq V(H)\), define its closure by starting with \(S_0=S\), setting
\[
S_{j+1}
=
S_j\cup\bigcup_{A\in[S_j]^n}N_H(A),
\]
and taking
\[
\operatorname{cl}(S)=\bigcup_{j<\omega}S_j.
\]
Since the operation has finite arity,
\(\operatorname{cl}(S)\) is closed under the operation. Moreover,
\[
|\operatorname{cl}(S)|
\leq \max\{|S|,\aleph_0\}.
\]

If \(M\) is closed and \(v\notin M\), then
\[
|N_H(v)\cap M|\leq n-1. \tag{1}
\]
Otherwise an \(n\)-element set \(A\subseteq N_H(v)\cap M\) would imply
\(v\in N_H(A)\subseteq M\).

We now use induction on \(\lambda=|V(H)|\). Countable graphs have the required ordering simply by enumeration.

Suppose \(\lambda>\aleph_0\), and let \(\mu=\operatorname{cf}(\lambda)\). There is a continuous increasing sequence of closed sets
\[
(M_\alpha:\alpha\leq\mu)
\]
such that
\[
M_0=\varnothing,\qquad M_\mu=V(H),\qquad
|M_\alpha|<\lambda\quad(\alpha<\mu).
\]
To construct it, choose an increasing family of subsets of size less than \(\lambda\), indexed by \(\mu\), that covers \(V(H)\); close at successor stages and take unions at limit stages. The closure-size bound keeps all stages below \(\mu\) smaller than \(\lambda\). Increasing unions of closed sets are closed because the rule has finite arity. This construction works for both regular and singular \(\lambda\).

Put
\[
D_\alpha=M_{\alpha+1}\setminus M_\alpha.
\]
Each \(H[D_\alpha]\) has smaller cardinality, so by induction it has a well-ordering with finitely many earlier neighbours. Concatenate these orderings in increasing order of \(\alpha\).

A vertex in \(D_\alpha\) has finitely many earlier neighbours within its own block and at most \(n-1\) neighbours in \(M_\alpha\), by (1). This gives the required ordering. Greedily choosing a natural-number colour not used by earlier neighbours gives a proper colouring.

Finally, in a \(K_{n,n}\)-free graph every \(n\)-element set has at most \(n-1\) common neighbours, so the lemma applies. \(\square\)

### Proof of the theorem

We use induction on \(|V(G)|\). If \(|V(G)|\leq\mathfrak c\), the binary-label construction in Section 2 gives the desired colouring.

Now suppose
\[
\lambda=|V(G)|>\mathfrak c
\]
and that the result holds for smaller graphs.

Whenever \(A,B\subseteq V(G)\) are disjoint \(n\)-element sets with every edge between \(A\) and \(B\) present, put
\[
C(A,B)=N_G(A\cup B).
\]
The hypothesis gives
\[
|C(A,B)|\leq\mathfrak c, \tag{2}
\]
since otherwise \(A,B\), and \(\mathfrak c^+\) common neighbours would form a \(K_{n,n,\mathfrak c^+}\).

Close a set \(S\) by repeatedly adjoining every \(C(A,B)\) for such pairs \(A,B\subseteq S\). By (2) and the finiteness of \(2n\), this closure satisfies
\[
|\operatorname{cl}(S)|\leq\max\{|S|,\mathfrak c\}. \tag{3}
\]

The crucial property is that, for every closed set \(M\) and every \(v\notin M\),
\[
G[N_G(v)\cap M]\text{ is }K_{n,n}\text{-free}. \tag{4}
\]
Indeed, if \(A,B\subseteq N_G(v)\cap M\) formed a \(K_{n,n}\), then
\[
v\in C(A,B)\subseteq M,
\]
a contradiction.

Using (3), construct a continuous closed filtration
\[
(M_\alpha:\alpha\leq\mu),
\qquad \mu=\operatorname{cf}(\lambda),
\]
with
\[
M_0=\varnothing,\quad M_\mu=V(G),\quad
|M_\alpha|<\lambda\quad(\alpha<\mu),
\]
exactly as in the lemma. Again let
\[
D_\alpha=M_{\alpha+1}\setminus M_\alpha.
\]

By induction, for each \(\alpha<\mu\) choose an edge-colouring
\[
c_\alpha:E(G[D_\alpha])\longrightarrow\omega
\]
with no monochromatic triangle.

For every \(v\in D_\alpha\), property (4) and the lemma give a proper vertex-colouring
\[
f_v:N_G(v)\cap M_\alpha\longrightarrow\omega
\]
of the graph induced by this set.

Define an edge-colouring \(c:E(G)\to\omega\) as follows:

- If \(u,v\in D_\alpha\), set
  \[
  c(uv)=2c_\alpha(uv).
  \]
- If \(v\in D_\alpha\) and \(u\in M_\alpha\), set
  \[
  c(uv)=2f_v(u)+1.
  \]

Thus edges within blocks receive even colours and edges between blocks receive odd colours.

Consider any triangle. There are exactly three cases.

1. **All three vertices lie in one block.**  
   It is not monochromatic by the choice of \(c_\alpha\).

2. **Exactly two vertices lie in the highest-indexed block occupied by the triangle.**  
   Their joining edge has an even colour, while the other two edges have odd colours.

3. **Exactly one vertex \(v\) lies in the highest-indexed block.**  
   The other vertices \(u,w\) belong to \(N_G(v)\cap M_\alpha\) and are adjacent. Since \(f_v\) is proper,
   \[
   f_v(u)\ne f_v(w).
   \]
   Hence \(c(vu)\ne c(vw)\).

Every triangle is therefore nonmonochromatic. This completes the induction and the proof. \(\square\)

## 4. What this does—and does not—settle

The special-case theorem is unconditional and applies at every cardinality. It shows that an obstruction cannot be obtained while forbidding even one of the configurations \(K_{n,n,\mathfrak c^+}\).

However, these configurations are compatible with very easy decompositions. For example, if \(\lambda\geq\mathfrak c^+\), then
\[
K_{\lambda,\lambda,\lambda}
\]
is \(K_4\)-free and contains all the required tripartite configurations, yet is a union of two bipartite graphs: with parts \(A,B,C\), put the \(A\)-\(B\) and \(A\)-\(C\) edges in one graph and the \(B\)-\(C\) edges in the other.

The gap to the original problem is therefore substantial. The closure argument succeeds when common neighbourhoods of some fixed finite biclique are bounded by the continuum. It supplies no decomposition once those common neighbourhoods can all be larger, and it supplies no ZFC construction for which every countable edge-colouring fails.

Thus this establishes a structural special case, but neither the requested ZFC existence result nor a consistency result for nonexistence.