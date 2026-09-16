```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the stronger bound h(G) >= chi(G) when deleting at most one vertex makes the complement C4-free.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved here; novelty of this special case has not been checked."
}
```

## A structural special case

Write \(h(G)\) for the largest order of a complete minor of \(G\), and write \(2K_2\) for the graph consisting of two disjoint edges.

I prove the following partial result.

**Theorem.** Let \(G\) be a nonempty finite simple graph with \(\alpha(G)\le 2\). Suppose that there is a vertex \(x\) such that \(G-x\) has no induced \(2K_2\). Then
\[
h(G)\ge \chi(G)\ge \left\lceil\frac{|V(G)|}{2}\right\rceil.
\]
Moreover, the \(K_{\chi(G)}\)-minor can be chosen with every branch set having at most three vertices.

In complement language, the additional hypothesis says that **one vertex meets every \(4\)-cycle of \(\overline G\)**. Indeed, \(\overline G\) is triangle-free, so every \(4\)-cycle in it is induced, and its complement is an induced \(2K_2\).

The proof is self-contained apart from the standard perfect-matching theorem of Tutte and the Tutte–Berge formula.

## 1. Two useful observations

A clique-minor model is a collection of disjoint connected vertex sets, called branch sets, with an edge between every two branch sets.

Two elementary facts will be used repeatedly.

1. **A seagull is dominating.** If \(p-q-r\) is an induced three-vertex path in a graph with independence number at most two, every vertex outside the path is adjacent to \(p\) or \(r\). Otherwise it forms an independent triple with \(p,r\).

   Consequently, a seagull disjoint from a clique of order \(k\) gives a \(K_{k+1}\)-minor.

2. **Matching edges are mutually adjacent in a \(2K_2\)-free graph.** If two disjoint edges had no edge between their endpoint sets, those four vertices would induce \(2K_2\).

Thus, in a \(2K_2\)-free graph, any matching is already a clique-minor model. The difficulty for an odd-order graph is supplying one additional branch set.

## 2. A component lemma

**Lemma.** Suppose that \(H\) satisfies \(\alpha(H)\le2\) and has no induced \(2K_2\). Let
\[
V(H)=A\mathbin{\dot\cup}B,
\]
where \(A\) is a clique. Form \(J\) by deleting all edges within \(A\). If \(S\subseteq V(J)\) and \(|B\setminus S|\ge2\), then \(J-S\) has at most two components.

**Proof.** Suppose that \(J-S\) has at least three components.

There cannot be two components containing vertices of \(B\setminus S\): choosing one such vertex from each and a vertex from a third component gives an independent triple in \(H\). Here we use that every edge incident with \(B\) was retained in \(J\).

Therefore all of \(B\setminus S\) lies in one component. Every other component lies in \(A\), and hence is a singleton, since \(J[A]\) is edgeless. Choose two such isolated vertices \(a_1,a_2\), and distinct \(b_1,b_2\in B\setminus S\).

In \(H\), the vertices \(a_1,a_2\) are adjacent and are anticomplete to \(\{b_1,b_2\}\). Also \(b_1b_2\) is an edge, since otherwise \(a_1,b_1,b_2\) would be independent. These four vertices induce \(2K_2\), a contradiction. \(\square\)

## 3. The half-order bound

First prove
\[
h(G)\ge \left\lceil\frac{|V(G)|}{2}\right\rceil
\tag{1}
\]
under the theorem’s hypothesis.

### Odd order

Let
\[
|V(G)|=2m+1.
\]
Orders one and three are immediate, so assume \(m\ge2\).

Choose \(v\) such that \(H=G-v\) has no induced \(2K_2\). Set
\[
A=V(G)\setminus N_G[v],\qquad B=N_G(v),
\]
and write \(a=|A|\), \(b=|B|=2m-a\).

The set \(A\) is a clique: two nonadjacent vertices of \(A\), together with \(v\), would be independent.

#### Case 1: \(a\ge m+1\)

The clique \(A\) contains the required \(K_{m+1}\).

#### Case 2: \(a=m\)

Then \(b=m\).

If \(B\) is a clique, \(B\cup\{v\}\) is a clique of order \(m+1\).

Otherwise choose nonadjacent \(p,q\in B\). The path \(p-v-q\) is a seagull disjoint from the \(m\)-clique \(A\), so it gives a \(K_{m+1}\)-minor together with \(A\).

#### Case 3: \(a\le m-1\)

In particular,
\[
b\ge m+1\ge3,\qquad b\ge a+2.
\tag{2}
\]

Form \(J\) from \(H\) by deleting all edges within \(A\). I will show that either \(G\) already contains a clique of order \(m+1\), or \(J\) has a perfect matching.

**First suppose that \(J\) is disconnected.** By the lemma, it has exactly two components.

If a component contains no vertex of \(B\), it is a singleton \(u\in A\). The vertex \(u\) is anticomplete in \(H\) to \(B\), so \(\alpha(H)\le2\) forces \(B\) to be a clique. Its size is at least \(m+1\).

Otherwise both components contain vertices of \(B\). Each component induces a clique in \(H\): a vertex of \(B\) in the other component is anticomplete to it, so any nonadjacent pair within it would give an independent triple.

If either component has at least \(m+1\) vertices, we are done. The only remaining possibility is that both have exactly \(m\) vertices. Since \(b\ge3\), one component contains two vertices of \(B\). Their edge, together with any edge in the other component, induces \(2K_2\) in \(H\), a contradiction.

Thus, unless a sufficiently large clique has already been found, \(J\) is connected.

**Now suppose that \(J\) is connected.** Apply Tutte’s perfect-matching criterion. Let \(o(J-S)\) denote the number of odd components of \(J-S\). We check that
\[
o(J-S)\le |S|
\qquad\text{for every }S\subseteq V(J).
\tag{3}
\]

If \(|B\setminus S|\ge2\), the lemma gives at most two components.

- For \(S=\varnothing\), connectedness and the even order \(2m\) give \(o(J)=0\).
- For \(|S|=1\), the remaining graph has odd order, so its number of odd components is odd. Being at most two, it is one.
- For \(|S|\ge2\), the inequality is immediate.

If \(|B\setminus S|\le1\), then (2) gives
\[
|S|\ge b-1\ge a+1\ge |V(J-S)|,
\]
which also proves (3).

Therefore \(J\) has a perfect matching \(M\).

The \(m\) edges of \(M\) are mutually adjacent branch sets, because \(H\) has no induced \(2K_2\). Every edge of \(M\) has an endpoint in \(B\), since \(J[A]\) is edgeless. Hence every matching branch set is adjacent to the singleton branch set \(\{v\}\).

Together they give a \(K_{m+1}\)-minor.

This completes the odd-order proof.

### Even order

Suppose \(|V(G)|=2m\), and choose \(x\) as in the hypothesis. The graph \(G-x\) has odd order \(2m-1\) and is itself \(2K_2\)-free. It therefore satisfies the hypothesis of the odd-order result and contains a \(K_m\)-minor.

This proves (1). The construction used only singleton, edge, and seagull branch sets, so all branch sets have size at most three.

## 4. Upgrading the bound to \(\chi(G)\)

The class in the theorem is hereditary. Indeed, an induced subgraph containing \(x\) retains \(x\) as a possible exceptional vertex, while one not containing \(x\) is already \(2K_2\)-free.

The following matching argument therefore upgrades (1) to the claimed chromatic bound.

Let
\[
F=\overline G,\qquad n=|V(G)|,
\]
and let \(\nu(F)\) be the maximum matching size in \(F\). Because every color class of \(G\) has at most two vertices,
\[
\chi(G)=n-\nu(F).
\tag{4}
\]

By the Tutte–Berge formula, there is a set \(S\subseteq V(F)\) such that
\[
2\nu(F)=n+|S|-o(F-S).
\tag{5}
\]
Let \(C_1,\ldots,C_t\) be the vertex sets of the components of \(F-S\).

For each \(i\), the induced graph \(G[C_i]\) belongs to our hereditary class. The half-order result supplies a complete minor of order
\[
\left\lceil\frac{|C_i|}{2}\right\rceil
\]
in \(G[C_i]\), with branch sets of size at most three.

Different components of \(F-S\) are completely joined in \(G\). Thus all these minor models combine into one complete minor, of order
\[
\begin{aligned}
\sum_{i=1}^{t}\left\lceil\frac{|C_i|}{2}\right\rceil
&=\frac{n-|S|+o(F-S)}2\\
&=n-\nu(F)\\
&=\chi(G),
\end{aligned}
\]
using (5) and (4). This proves the theorem.

## 5. A quantitative consequence

Let \(\tau_4(F)\) be the minimum number of vertices whose deletion makes \(F\) \(C_4\)-free. For an arbitrary graph \(G\) with \(\alpha(G)\le2\), put
\[
r=\max\{0,\tau_4(\overline G)-1\}.
\]

Deleting \(r\) suitable vertices leaves a graph satisfying the theorem. Consequently,
\[
\boxed{
h(G)\ge
\max\left\{
\left\lceil\frac{n-r}{2}\right\rceil,\,
\chi(G)-r
\right\}.}
\]
The second bound uses the elementary inequality
\(\chi(G-X)\ge\chi(G)-|X|\).

In particular, the seagull conjecture holds for:

- graphs whose complement becomes \(C_4\)-free after deleting at most one vertex;
- even-order graphs whose complement becomes \(C_4\)-free after deleting at most two vertices.

## 6. What remains unresolved

The argument does not handle unrestricted triangle-free complements.

Its crucial use of the additional hypothesis is twofold: it controls the components of the auxiliary graph \(J-S\), and it guarantees that distinct matching edges are adjacent branch sets. Without it, two matching edges can induce \(2K_2\), preventing the matching from producing a complete minor.

For perspective, a minimum-order counterexample to the original conjecture would necessarily have odd order \(2m+1\). The first two odd-order cases above, which did not use the additional hypothesis, show that it would satisfy
\[
\delta(G)\ge m+1.
\]
It could also have no dominating edge: deleting the endpoints of such an edge, applying minimality, and adding that edge as a branch set would finish the minor. Equivalently, its triangle-free complement would have diameter two. The theorem adds that its complement’s \(4\)-cycles could not all meet one vertex.

These conditions do not exclude all possible counterexamples. Thus the result above is a proved structural special case, not a resolution of the seagull conjecture.