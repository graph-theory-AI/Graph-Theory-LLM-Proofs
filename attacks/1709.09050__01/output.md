```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "A finite connected outerplanar graph is 1-cop-win exactly when it is chordal—equivalently, when every block on at least three vertices is maximal outerplanar—and otherwise its cop number is 2.",
  "would_publish": false,
  "caveats": "This uses the standard finite visible game with passing and the given two-cop upper bound; publication priority was not independently checked."
}
```

## Statement

Let \(G\) be a finite, simple, connected outerplanar graph. Then

\[
c(G)=
\begin{cases}
1,&\text{if \(G\) is chordal},\\[2mm]
2,&\text{if \(G\) contains an induced cycle of length at least \(4\)}.
\end{cases}
\]

Equivalently, \(G\) is \(1\)-cop-win if and only if every block of \(G\) having at least three vertices is a maximal outerplanar graph. Thus the \(1\)-cop-win outerplanar graphs are precisely trees of maximal outerplanar blocks, with bridges allowed.

The nontrivial point is proving that a cop-win outerplanar graph cannot contain an induced cycle of length at least four.

## 1. The dismantling characterization

For a graph \(H\), write \(N_H[v]\) for the closed neighborhood of \(v\). A vertex \(v\) is a **corner**, dominated by \(u\neq v\), if

\[
N_H[v]\subseteq N_H[u].
\]

A **dismantling order** is an ordering \(v_1,\dots,v_n\) such that, for every \(i<n\), the vertex \(v_i\) is a corner in

\[
H_i=H[\{v_i,v_{i+1},\dots,v_n\}].
\]

### Lemma 1
A finite connected graph is \(1\)-cop-win if and only if it has a dismantling order.

### Proof

First suppose a graph \(H\), with at least two vertices, has no corner. A robber can evade one cop as follows. After the cop chooses \(c\), there is a vertex \(r\notin N_H[c]\): otherwise \(N_H[c]=V(H)\), and every other vertex would be dominated by \(c\).

Maintain the invariant that, after each robber move, \(r\notin N_H[c]\). If the cop moves from \(c\) to \(c'\in N_H[c]\), then \(c'\neq r\). Since \(r\) is not dominated by \(c'\), there exists

\[
r'\in N_H[r]\setminus N_H[c'].
\]

The robber moves to \(r'\), restoring the invariant. Thus every cop-win graph with more than one vertex has a corner.

If \(v\) is dominated by \(u\), define the fold

\[
\rho(v)=u,\qquad \rho(x)=x\quad(x\neq v).
\]

The domination relation makes \(\rho\) a graph retraction onto \(H-v\): every move involving \(v\) projects to a legal move involving \(u\). Hence, if \(H\) is cop-win, then \(H-v\) is cop-win by projecting a winning cop strategy. Repeatedly choosing a corner therefore gives a dismantling order.

Conversely, suppose \(v\) is dominated by \(u\) and \(H-v\) is cop-win. The cop remains in \(H-v\) and plays against the shadow \(\rho(r)\) of the robber. If the shadow is captured while the actual robber is at \(v\), the cop is at \(u\). Since \(N_H[v]\subseteq N_H[u]\), wherever the robber moves next is immediately capturable. Thus adding a dominated vertex preserves the cop-win property. Induction along a dismantling order proves the converse. \(\square\)

## 2. An intact induced cycle has no removable vertex

A cycle of length at least four with no chord will be called a hole.

### Lemma 2
Let \(G\) be outerplanar, let \(C\) be a hole in \(G\), and let \(H\) be any induced subgraph of \(G\) containing all vertices of \(C\). No vertex of \(C\) is a corner of \(H\).

### Proof

Suppose, to the contrary, that \(z\in V(C)\) is dominated in \(H\) by \(x\). Let \(a,b\) be the two neighbors of \(z\) on \(C\). Domination gives

\[
xz,xa,xb\in E(H).
\]

The vertex \(x\) is not on \(C\). Indeed, inducedness of \(C\) implies that the only cycle vertices adjacent to \(z\) are \(a,b\). If, say, \(x=a\), then domination would also force \(ab\in E(G)\), which is a chord of \(C\).

Let \(Q\) be the \(a\)-\(b\) path on \(C\) avoiding \(z\). The three paths

\[
a-z-b,\qquad a-x-b,\qquad Q
\]

are internally vertex-disjoint, and each has length at least two. After deleting the extra edge \(xz\) and any other irrelevant edges, their union is a subdivision of \(K_{2,3}\).

An outerplanar graph cannot contain a subdivision of \(K_{2,3}\), since contracting its subdivided edges would give a \(K_{2,3}\) minor. This is a contradiction. \(\square\)

The proof only uses exclusion of a subdivision of \(K_{2,3}\), so Lemma 2 applies more generally to every graph with no such topological minor.

## 3. Main classification

### Chordal outerplanar graphs are cop-win

Every chordal graph has a perfect elimination ordering: in each remaining induced subgraph, the next vertex is simplicial. If a simplicial vertex \(v\) has a neighbor \(u\), then its neighbors form a clique, and hence

\[
N[v]\subseteq N[u].
\]

Moreover, deleting a simplicial vertex from a connected graph preserves connectedness: any path segment \(p-v-q\) can be replaced by the edge \(pq\). Thus every vertex except the last has a neighbor when it is deleted. A perfect elimination ordering is therefore a dismantling order. By Lemma 1, every connected chordal graph, and in particular every connected chordal outerplanar graph, is \(1\)-cop-win.

### Nonchordal outerplanar graphs are not cop-win

Suppose \(G\) contains a hole \(C\) and nevertheless is \(1\)-cop-win. By Lemma 1, let

\[
v_1,\dots,v_n
\]

be a dismantling order. Choose the smallest index \(i\) for which \(v_i\in V(C)\). Then the tail

\[
H_i=G[\{v_i,\dots,v_n\}]
\]

still contains every vertex of \(C\), and \(C\) remains induced there. Since at least the other vertices of \(C\) occur after \(v_i\), the vertex \(v_i\) must be a corner of \(H_i\). This contradicts Lemma 2.

Therefore an outerplanar graph with a hole is not \(1\)-cop-win. Using the given theorem that every connected outerplanar graph has cop number at most \(2\), its cop number is exactly \(2\).

This completes the dichotomy.

## 4. Equivalent block characterization

A graph is chordal if and only if each of its blocks is chordal, since every cycle lies in a single block.

Let \(B\) be a \(2\)-connected outerplanar graph on \(n\ge 3\) vertices. Then

\[
B\text{ is chordal}
\quad\Longleftrightarrow\quad
B\text{ is maximal outerplanar}
\quad\Longleftrightarrow\quad
|E(B)|=2n-3.
\]

For the forward implication, a \(2\)-connected outerplanar graph has a Hamilton cycle given by the outer boundary of an outerplane embedding. In a chordal graph, every cycle of length \(n\) has at least \(n-3\) chords. This follows inductively by choosing one chord, splitting the cycle into cycles of lengths \(p,q\) with \(p+q=n+2\), and counting

\[
1+(p-3)+(q-3)=n-3.
\]

Consequently,

\[
|E(B)|\ge n+(n-3)=2n-3.
\]

The outerplanar edge bound gives the reverse inequality, so equality holds and \(B\) is maximal outerplanar.

Conversely, if a maximal outerplanar graph contained an induced cycle of length at least four, then in an outerplane embedding the interior of that cycle would contain no vertices and no chord. A diagonal could therefore be added while preserving outerplanarity, contradicting maximality.

Hence the classification can be stated concretely as follows:

- \(c(G)=1\) exactly when every block with at least three vertices has \(2|V(B)|-3\) edges;
- otherwise \(c(G)=2\).

This yields a linear-time recognition algorithm for a promised outerplanar graph: compute its block decomposition and check the displayed edge count in every non-bridge block.

## 5. Scope and remaining caveats

There is no uncovered mathematical case under the standard assumptions. The only imported result is the stipulated upper bound \(c(G)\le 2\) for connected outerplanar graphs.

The connectedness assumption is necessary for the stated \(1/2\) dichotomy. Under the usual convention that cops choose their initial vertices before the robber, if \(G\) has connected components \(G_1,\dots,G_t\), then

\[
c(G)=\sum_{j=1}^t c(G_j),
\]

so the componentwise characterization above gives the corresponding classification for disconnected outerplanar graphs.

I have not independently established publication priority; the argument proves the extracted statement but does not show that the characterization has not previously appeared.