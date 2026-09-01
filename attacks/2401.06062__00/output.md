```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "For finite simple graphs, a nontrivial joined-union decomposition exists exactly when the graph has a proper nonsingleton module; this is polynomial-time decidable, while P4 shows that not every graph decomposes.",
  "would_publish": false,
  "caveats": "This uses the standard graph-substitution meaning of joined union; infinite graphs and more restrictive decomposition notions are not addressed."
}
```

## 1. Precise formulation

Let \(Q\) be a graph with vertex set \(\{1,\dots ,k\}\), and let \(G_1,\dots ,G_k\) be graphs on pairwise disjoint nonempty vertex sets. The **joined union**, also called graph substitution, is

\[
Q[G_1,\dots ,G_k],
\]

obtained by retaining all edges inside each \(G_i\), and, for \(i\neq j\), making \(V(G_i)\) complete to \(V(G_j)\) when \(ij\in E(Q)\), and anticomplete otherwise.

For an \(n\)-vertex graph, the decomposition is nontrivial if

\[
2\leq k<n.
\]

The condition \(k<n\) excludes the tautological representation
\[
G=G[K_1,\dots ,K_1].
\]

A set \(M\subseteq V(G)\) is a **module** or homogeneous set if every vertex outside \(M\) is either adjacent to every vertex of \(M\), or adjacent to none of them. It is nontrivial when

\[
2\leq |M|\leq |V(G)|-1.
\]

## 2. Exact characterization

### Theorem

For a finite simple graph \(G\), the following are equivalent:

1. \(G\) has a nontrivial joined-union decomposition.
2. \(G\) has a nontrivial module.

Thus the original question, under its standard interpretation, is precisely the modular-decomposition recognition problem.

### Proof

Suppose first that

\[
G=Q[G_1,\dots ,G_k]
\]

with \(2\leq k<n=|V(G)|\). Since \(k<n\), at least one block \(V(G_i)\) contains at least two vertices. It is a proper subset because \(k\geq 2\). Every vertex in another block \(V(G_j)\) is either adjacent to every vertex of \(V(G_i)\), if \(ij\in E(Q)\), or to none of them otherwise. Hence \(V(G_i)\) is a nontrivial module.

Conversely, let \(M\) be a nontrivial module of \(G\). Partition \(V(G)\) into

\[
\mathcal P=\{M\}\cup \{\{x\}:x\in V(G)\setminus M\}.
\]

Define a quotient graph \(Q\) whose vertices are the parts of \(\mathcal P\). Two distinct parts are adjacent in \(Q\) exactly when they are complete to one another in \(G\). This is well-defined: the only nonsingleton part is \(M\), and the module property says that each outside singleton is either complete or anticomplete to \(M\).

It follows directly that

\[
G=Q\bigl[G[M],(K_1)_{x\notin M}\bigr].
\]

Moreover,

\[
|V(Q)|=n-|M|+1,
\]

which lies between \(2\) and \(n-1\). All substituted graphs and the quotient are therefore smaller than \(G\), so this is a nontrivial joined-union decomposition. \(\square\)

## 3. A self-contained recognition algorithm

The characterization gives an elementary polynomial-time algorithm without invoking any external modular-decomposition machinery.

For \(X\subseteq V(G)\), call \(z\notin X\) a **splitter** of \(X\) if \(z\) has both a neighbor and a nonneighbor in \(X\), equivalently,

\[
0<|N(z)\cap X|<|X|.
\]

Thus \(X\) is a module exactly when it has no splitter.

For each unordered pair \(\{u,v\}\), perform the following closure process:

1. Set \(X=\{u,v\}\).
2. While there is a splitter \(z\notin X\), replace \(X\) by \(X\cup\{z\}\).
3. If \(X\neq V(G)\), output \(X\).

If every pair closes to \(V(G)\), report that \(G\) is prime.

### Closure lemma

The final set obtained from \(\{u,v\}\) is the unique smallest module containing \(u\) and \(v\).

#### Proof

Termination is immediate because \(X\) grows at every step. At termination, \(X\) has no splitter and hence is a module.

Let \(M\) be any module containing \(u\) and \(v\). We show inductively that every intermediate set \(X\) is contained in \(M\). This is initially true. Suppose \(X\subseteq M\), and let \(z\) split \(X\). If \(z\notin M\), then because \(M\) is a module, \(z\) must be either complete or anticomplete to \(M\), and therefore complete or anticomplete to \(X\). This contradicts that \(z\) splits \(X\). Hence \(z\in M\), preserving \(X\subseteq M\).

Consequently, the final set is contained in every module containing \(u,v\). Since the final set is itself such a module, it is the unique smallest one. \(\square\)

### Correctness of the recognition algorithm

If the algorithm outputs a proper set \(X\), the closure lemma says that \(X\) is a module. Since it contains the initial pair, it is nontrivial.

Conversely, suppose \(G\) has a nontrivial module \(M\). Choose distinct \(u,v\in M\). The closure lemma shows that the closure of \(\{u,v\}\) is contained in \(M\), and is therefore proper. Hence the algorithm will find a nontrivial module.

Thus the algorithm decides joined-union decomposability exactly.

### Complexity

Using an adjacency matrix, maintain

\[
d_X(z)=|N(z)\cap X|
\]

for vertices \(z\notin X\). When a new vertex is added to \(X\), all these counts can be updated in \(O(n)\) time. Locating a splitter by scanning the vertices also costs \(O(n)\). There are at most \(n-2\) additions for each pair, so one pair costs \(O(n^2)\). Trying all \(O(n^2)\) pairs gives an explicit bound of

\[
O(n^4)
\]

time and \(O(n^2)\) space. This bound is not claimed to be optimal.

Once a module \(M\) is returned, the quotient constructed in the theorem immediately gives the requested joined-union decomposition. Repeating the procedure on decomposable factors yields a recursive decomposition and terminates because every factor considered has fewer vertices.

## 4. Not every graph decomposes: the \(P_4\) obstruction

If the question is instead read as asking whether **every** graph has such a decomposition, the answer is no.

Let \(P_4\) have edges

\[
12,\quad 23,\quad 34.
\]

Any nontrivial module would have size two or three.

For the six pairs, a splitter is given by

\[
\begin{array}{c|c}
M&\text{splitter}\\ \hline
\{1,2\}&3\\
\{1,3\}&4\\
\{1,4\}&2\\
\{2,3\}&1\\
\{2,4\}&1\\
\{3,4\}&2
\end{array}
\]

For the four triples:

- \(4\) splits \(\{1,2,3\}\);
- \(3\) splits \(\{1,2,4\}\);
- \(2\) splits \(\{1,3,4\}\);
- \(1\) splits \(\{2,3,4\}\).

Therefore \(P_4\) has no nontrivial module and hence no nontrivial joined-union decomposition.

## 5. Relation to the source paper and remaining caveats

The Cayley-graph problem in the cited source is a specialization of this criterion: it seeks an algebraic description of when a Cayley graph has a nontrivial module. The broad finite graph-theoretic question itself is therefore not open; it is the standard modular-decomposition problem.

There is no gap in the argument for finite simple graphs under the definition above. Different questions would arise for infinite graphs, directed or weighted graphs, or decompositions imposing additional conditions such as isomorphic factors, prescribed quotients, or minimum-size representations.