```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a neighborhood criterion that settles the conjecture whenever a vertex has at most one nonneighbor.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; novelty of the special case and criterion is not claimed."
}
```

## 1. A sufficient neighborhood condition

All graphs below are finite and simple. Write \(N(v)\) for the open neighborhood of \(v\), and \(N[v]=N(v)\cup\{v\}\).

I prove the following statement. It does **not** require \(G\) itself to be 6-connected.

**Theorem.** Let \(G\) have no \(K_6\) minor, and let \(v\in V(G)\). Suppose that

1. \(G[N(v)]\) is 4-connected; and
2. every \(u\in V(G)\setminus N[v]\) has at least four neighbors in \(N(v)\).

Then \(G-v\) is planar.

In particular:

**Corollary.** If \(G\) is 6-connected, has no \(K_6\) minor, and
\[
d(v)\ge |V(G)|-2,
\]
then \(G-v\) is planar.

Thus any counterexample to Jørgensen’s conjecture must satisfy
\[
\Delta(G)\le |V(G)|-3,
\qquad\text{equivalently}\qquad
\delta(\overline G)\ge 2.
\]

The proof uses established theorems, not additional conjectures.

## 2. A cofaciality lemma

We use the following classical facts.

- **Wagner’s theorem, 4-connected case:** every 4-connected graph with no \(K_5\) minor is planar. This follows from Wagner’s decomposition by clique-sums of order at most three into planar graphs and the cubic Wagner graph.
- A 3-connected planar graph has a unique embedding on the sphere, up to homeomorphism. Consequently, if \(P+ab\) is planar, then \(a,b\) are cofacial in any fixed planar embedding of \(P\).
- Distinct faces of a 3-connected plane graph cannot have three boundary vertices in common.

Here is the geometric ingredient.

**Lemma.** Let \(P\) be a 4-connected plane graph, and let \(W\subseteq V(P)\), with \(|W|\ge4\). If every two vertices of \(W\) are cofacial, then all vertices of \(W\) lie on the boundary of one face.

**Proof.** First, a 4-connected planar graph cannot contain a \(K_4\) subgraph. Indeed, an embedded \(K_4\) has four triangular faces. Any additional vertex lies inside one of them, and its boundary triangle separates that vertex from the fourth vertex of the \(K_4\). This contradicts 4-connectivity.

Take any four-element subset \(T\subseteq W\). Suppose no face contains all four vertices of \(T\). For each missing edge between vertices of \(T\), choose a face containing its endpoints and draw the edge inside that face.

These additions can be made simultaneously without crossings: each face contains at most three vertices of \(T\), and chords among at most three boundary vertices can be drawn without crossings. We thereby obtain a planar supergraph of \(P\), on the same vertex set, containing \(K_4\). Adding edges preserves 4-connectivity, contradicting the preceding paragraph.

Therefore every four vertices of \(W\) lie on a common face.

Fix three distinct vertices \(a,b,c\in W\). They lie on a face \(F\), and this face is unique because distinct faces cannot have three boundary vertices in common. For every other \(d\in W\), the four vertices \(a,b,c,d\) lie on one face, necessarily \(F\). Hence \(W\subseteq V(\partial F)\). \(\square\)

## 3. Proof of the neighborhood criterion

Let
\[
N=N_G(v),\qquad U=V(G)\setminus N[v],\qquad P=G[N].
\]
We induct on \(|U|\).

### Base case: \(U=\varnothing\)

Here \(v\) is adjacent to every vertex of \(P=G-v\). If \(P\) had a \(K_5\) minor, its five branch sets together with the singleton branch set \(\{v\}\) would give a \(K_6\) minor in \(G\).

Thus \(P\) has no \(K_5\) minor. It is 4-connected, so Wagner’s theorem implies that \(P=G-v\) is planar.

### Inductive step

Choose \(w\in U\), and put
\[
H=G-v,\qquad Q=H-w.
\]

The graph \(G-w\), with distinguished vertex \(v\), satisfies the same two hypotheses and has fewer vertices outside \(N[v]\). Hence the induction hypothesis says that \(Q\) is planar.

Moreover, \(Q\) is 4-connected. To see this, delete any set \(S\) of at most three vertices. The graph \(P-S\) remains connected. Every remaining vertex of \(Q-V(P)\) has at least four neighbors in \(P\), so it retains a neighbor in \(P-S\). Thus \(Q-S\) is connected.

We next prove that
\[
H/ws\ \text{is planar for every }s\in N_H(w).
\tag{1}
\]

Consider \(G/ws\), retaining the label \(s\) for the contracted vertex. This graph has no \(K_6\) minor. There are two cases.

- **If \(s\in N\):** the neighborhood of \(v\) has the same vertex set \(N\), and its induced graph is a spanning supergraph of \(P\), hence is 4-connected. Each remaining nonneighbor of \(v\) retains its four distinct neighbors in \(N\).
- **If \(s\in U\setminus\{w\}\):** the neighborhood graph of \(v\) remains \(P\). The contracted vertex has as its neighbors in \(N\) the union of the former neighbors of \(w\) and \(s\), so it has at least four. The other nonneighbors retain their required neighbors.

In both cases the number of nonneighbors of \(v\) decreases by one. The induction hypothesis therefore applies to \(G/ws\), proving (1).

Fix a planar embedding of \(Q\), and let
\[
W=N_H(w).
\]
For any distinct \(a,b\in W\), contracting \(wa\) creates the edge \(ab\), if it was not already present. Consequently,
\[
Q+ab\subseteq H/wa.
\]
By (1), \(Q+ab\) is planar. Since \(Q\) is 4-connected, uniqueness of its planar embedding implies that \(a,b\) are cofacial in our fixed embedding of \(Q\).

Thus the vertices of \(W\) are pairwise cofacial. Also \(|W|\ge4\), because \(w\) has at least four neighbors in \(N\). The cofaciality lemma gives a single face of \(Q\) containing all of \(W\).

Place \(w\) inside that face and join it to its neighbors there. This gives a planar embedding of \(H=G-v\), completing the induction. \(\square\)

The auxiliary theorem’s formulation is important: the local hypotheses survive these contractions, whereas 6-connectivity need not.

## 4. Consequences for 6-connected graphs

Let \(G\) be 6-connected and \(K_6\)-minor-free.

Suppose first that \(v\) has at most one nonneighbor.

- If \(v\) is universal, then \(G[N(v)]=G-v\) is 5-connected.
- Otherwise, let \(w\) be its unique nonneighbor. Then
  \[
  G[N(v)]=G-\{v,w\}
  \]
  is 4-connected. Since \(\delta(G)\ge6\), and \(w\) is not adjacent to \(v\), all of \(w\)’s at least six neighbors lie in \(N(v)\).

The theorem applies in either case, proving the corollary.

There is also a slightly broader high-degree consequence:

**Further corollary.** If \(G[N(v)]\) is 4-connected and
\[
d(v)\ge |V(G)|-4,
\]
then \(G-v\) is planar.

Indeed, writing \(r=|V(G)\setminus N[v]|\le3\), every nonneighbor \(u\) of \(v\) has at most \(r-1\) neighbors outside \(N(v)\). Therefore
\[
|N(u)\cap N(v)|
\ge 6-(r-1)=7-r\ge4.
\]

## 5. Why the connectivity threshold matters

The almost-universal-vertex corollary becomes false if “6-connected” is replaced by “5-connected.” The following explicit example also illustrates the obstruction to extending the cofaciality lemma to 3-connected graphs.

Let \(P\) be the triangular prism, with triangles
\[
A=\{a_1,a_2,a_3\},\qquad B=\{b_1,b_2,b_3\},
\]
and matching edges \(a_ib_i\). Form \(F\) by adding two nonadjacent vertices \(x,y\), each adjacent to every vertex of \(P\).

Then \(F\) has eight vertices, and \(d(x)=d(y)=6=|V(F)|-2\).

### \(F\) is 5-connected

After deleting at most four vertices, if a hub \(x\) or \(y\) remains, it connects all remaining prism vertices, and also connects to the other hub through a remaining prism vertex.

If both hubs are deleted, at most two prism vertices have been deleted. The triangular prism remains connected after any two vertex deletions: both triangles retain vertices, and at least one of the three matching edges remains intact.

Thus \(\kappa(F)\ge5\). Prism vertices have degree five, so \(\kappa(F)=5\).

### \(F\) is not apex

The graph has
\[
|E(F)|=9+12=21.
\]
Deleting a prism vertex leaves seven vertices and sixteen edges, exceeding the planar bound \(3\cdot7-6=15\).

Deleting a hub leaves the cone over the triangular prism. The prism has a \(K_4\) minor: contract \(a_1b_1\) and \(a_2b_2\). The remaining hub extends this to a \(K_5\) minor. Hence deleting either hub also leaves a nonplanar graph.

### \(F\) has no \(K_6\) minor

Its clique number is four. A \(K_6\)-minor model on at most eight vertices must have at least four singleton branch sets. Five singleton branch sets would form a \(K_5\), which is impossible. Therefore such a model would have exactly four singleton branch sets and two branch sets of size two, using all eight vertices.

The four singleton vertices form a \(K_4\). Every \(K_4\) in \(F\) consists of one hub and one of the prism triangles. By symmetry, suppose these singleton vertices are
\[
x,a_1,a_2,a_3.
\]
The remaining vertices are \(y,b_1,b_2,b_3\). Their partition into two connected pairs must have the form
\[
\{y,b_i\},\qquad \{b_j,b_k\},
\]
where \(\{i,j,k\}=\{1,2,3\}\). But \(\{b_j,b_k\}\) has no edge to the singleton \(\{a_i\}\), contradicting the required branch-set adjacency.

Thus \(F\) is a 5-connected, nonapex, \(K_6\)-minor-free graph with almost-universal vertices. It is **not** a counterexample to Jørgensen’s conjecture.

Geometrically, all six vertices of the triangular prism are pairwise cofacial, but no face contains all six. Its neighborhood connectivity is three, exactly where the lemma above ceases to hold.

## 6. Remaining gap

The argument does not establish that an arbitrary 6-connected \(K_6\)-minor-free graph has a vertex satisfying the neighborhood criterion.

In particular, when \(v\) has two or more nonneighbors, deleting \(v\) and all its nonneighbors need not leave a 4-connected graph. Neither the Wagner step nor the cofaciality step then applies as written.

Thus the proof settles the stated special classes, but leaves the unrestricted conjecture unresolved.