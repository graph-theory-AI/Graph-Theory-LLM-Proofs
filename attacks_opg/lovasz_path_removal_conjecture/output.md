```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For graphs with no induced cycle longer than ell, connectivity at least k + floor(ell/2) + 1 guarantees that deleting any shortest x-y path leaves a k-connected graph.",
  "would_publish": false,
  "caveats": "No unrestricted bound f(k) is obtained; novelty of these restricted-class results is not claimed."
}
```

## 1. A bounded-induced-cycle-length theorem

I do not resolve the unrestricted conjecture. The following special case admits a self-contained proof, with optimal connectivity thresholds when the maximum allowed induced-cycle length is three, four, or five.

All graphs below are finite and simple. A \(k\)-connected graph has at least \(k+1\) vertices.

**Theorem.** Let \(k\ge 1\) and \(\ell\ge 3\). Suppose that \(G\) has no induced cycle longer than \(\ell\) and
\[
\kappa(G)\ge k+\left\lfloor\frac{\ell}{2}\right\rfloor+1.
\]
Then, for any distinct vertices \(x,y\), **every shortest \(x\)-\(y\) path** \(P\) satisfies
\[
\kappa(G-V(P))\ge k.
\]

Thus the conjectured property holds within every class with a fixed bound on induced-cycle length. In particular:

- \(k+2\) connectivity suffices for chordal graphs;
- \(k+3\) connectivity suffices for graphs with no induced cycle longer than five.

These classes need not have bounded diameter, so this is not simply a consequence of deleting a path of bounded length.

### A long-cycle certificate for a failed shortest path

The key observation applies without an induced-cycle restriction.

**Proposition.** Suppose \(G\) is \(t\)-connected, where \(t\ge k+2\), and \(P\) is a shortest path between distinct vertices \(x,y\). If \(G-V(P)\) is not \(k\)-connected, then \(G\) contains an induced cycle of length at least
\[
2(t-k).
\]

**Proof.** Put \(H=G-V(P)\). Since \(P\) is induced, \(x\) has exactly one neighbor on \(P\). Consequently,
\[
|V(H)|\ge \deg_G(x)-1\ge t-1\ge k+1.
\]
Thus failure of \(k\)-connectivity is not merely a shortage of vertices: there is a set
\[
S\subseteq V(H),\qquad |S|\le k-1,
\]
such that \(H-S\) is disconnected. Choose vertices \(a,b\) in different components of \(H-S\).

The set \(S\cup V(P)\) separates \(a\) from \(b\) in \(G\). Choose an inclusion-minimal \(a\)-\(b\) separator
\[
T\subseteq S\cup V(P).
\]
Since \(G\) is \(t\)-connected,
\[
|T|\ge t,
\]
and hence
\[
|T\cap V(P)|
\ge |T|-|S|
\ge t-k+1. \tag{1}
\]

Let \(A,B\) be the components of \(G-T\) containing \(a,b\), respectively. Minimality of \(T\) implies that every vertex of \(T\) has a neighbor in both \(A\) and \(B\). Indeed, restoring any one vertex \(z\in T\) must reconnect \(a\) to \(b\); such a connection must enter \(z\) from \(A\) and leave it toward \(B\).

Let \(u,v\) be the first and last vertices of \(T\cap V(P)\) in the order along \(P\). Because a subpath of a shortest path is shortest, (1) gives
\[
\operatorname{dist}_G(u,v)
=|E(P[u,v])|
\ge |T\cap V(P)|-1
\ge t-k
\ge 2. \tag{2}
\]
In particular, \(u,v\) are nonadjacent.

Choose a shortest \(u\)-\(v\) path \(Q_A\) in \(G[A\cup\{u,v\}]\), and similarly choose \(Q_B\) in \(G[B\cup\{u,v\}]\). These paths exist because \(A,B\) are connected and every vertex of \(T\) has a neighbor in each.

Both paths are induced. Their interiors are disjoint, there are no edges between their interiors, and \(uv\notin E(G)\). Therefore
\[
Q_A\cup Q_B
\]
is an induced cycle. By (2), its length is at least
\[
|E(Q_A)|+|E(Q_B)|
\ge 2\operatorname{dist}_G(u,v)
\ge 2(t-k).
\]
This proves the proposition. \(\square\)

### Proof of the theorem

Take
\[
t=k+\left\lfloor\frac{\ell}{2}\right\rfloor+1.
\]
If deleting a shortest \(x\)-\(y\) path failed to leave a \(k\)-connected graph, the proposition would produce an induced cycle of length at least
\[
2(t-k)
=2\left\lfloor\frac{\ell}{2}\right\rfloor+2
>\ell,
\]
contrary to the hypothesis. \(\square\)

If equal ends \(x=y\) are allowed, the one-vertex path suffices: deleting one vertex reduces connectivity by at most one.

## 2. Stronger conclusion and sharp threshold for chordal graphs

For chordal graphs, “shortest path” can be replaced by “induced path.”

**Corollary.** If \(G\) is chordal and \((k+2)\)-connected, then deleting **any induced path** leaves a \(k\)-connected graph.

**Proof.** First, every inclusion-minimal \(a\)-\(b\) separator \(T\) in a chordal graph is a clique. Otherwise two nonadjacent vertices \(u,v\in T\), together with paths through the two full components used in the preceding proof, would give an induced cycle of length at least four.

An induced path contains at most two vertices of a clique. Now suppose an induced path \(P\) leaves a graph that is not \(k\)-connected. The same order estimate and separator construction as above yield sets
\[
S\subseteq V(G)\setminus V(P),\quad |S|\le k-1,
\qquad
T\subseteq S\cup V(P),
\]
where \(T\) is an inclusion-minimal separator. Since \(T\) is a clique,
\[
|T|\le |S|+|T\cap V(P)|\le k-1+2=k+1,
\]
contradicting \((k+2)\)-connectivity. \(\square\)

### The threshold \(k+2\) cannot be decreased

Let
\[
G=K_{k+3}-uv,
\]
where just one edge \(uv\) is missing. This graph is chordal and has connectivity \(k+1\).

Choose distinct \(x,y\notin\{u,v\}\). They are adjacent, so their only induced connecting path is the edge \(xy\). Deleting its ends leaves
\[
K_{k+1}-uv,
\]
whose connectivity is \(k-1\).

Thus, for every \(k\ge1\), the optimal threshold within chordal graphs is exactly
\[
\boxed{k+2}.
\]
The obstruction is a genuine separator, not merely an insufficient number of remaining vertices.

## 3. Sharp threshold when induced cycles have length at most four or five

For \(k\ge2\), the theorem’s bound \(k+3\) is optimal in both of these classes.

Let
\[
G=K_{k-2}\vee K_{2,2,2},
\]
where \(\vee\) denotes the join; for \(k=2\), no additional clique vertices are present. Equivalently, \(G\) is complete multipartite with three parts of size two and \(k-2\) singleton parts.

A complete multipartite graph on \(n\) vertices with largest part of size \(a\) has connectivity \(n-a\): deleting all vertices outside a largest part gives the upper bound, while a smaller deletion leaves vertices in at least two parts and hence a connected graph. Therefore
\[
|V(G)|=k+4,\qquad \kappa(G)=k+2.
\]

Choose \(x,y\) to be the two vertices of one size-two part. Every other vertex is adjacent to both \(x\) and \(y\). Consequently, every induced \(x\)-\(y\) path has exactly the form
\[
xzy.
\]
A longer path would have a chord from \(x\) to its second internal vertex.

After deleting \(x,z,y\), the remaining graph has \(k+1\) vertices and still has a part of size two: at least one of the other two original size-two parts remains intact. Thus, for every possible induced \(x\)-\(y\) path,
\[
\kappa(G-\{x,z,y\})=(k+1)-2=k-1.
\]

Finally, complete multipartite graphs have no induced cycle longer than four. To see this, in an induced cycle of length at least five, the third and fourth vertices would both be nonneighbors of the first, and hence would lie in its part—contradicting their adjacency along the cycle.

Combining this obstruction with the theorem proves:

\[
\boxed{
\begin{array}{l}
\text{For every }k\ge2,\text{ the optimal threshold is }k+3\\
\text{both for graphs with induced-cycle length at most four}\\
\text{and for graphs with induced-cycle length at most five.}
\end{array}}
\]

For example, when \(k=3\), six-connectivity is sufficient and optimal within the class having no induced cycle of length at least six. This is a restricted-class result, not a determination of the unrestricted \(f(3)\).

## 4. A rigorous barrier to a shortest-path-only approach

The proof above works particularly cleanly for shortest paths. However, connectivity alone cannot guarantee that even one shortest path is removable. The following construction has arbitrarily large connectivity and a **unique** shortest path whose deletion disconnects the graph.

Fix \(r\ge3\). Construct \(G_r\) as follows.

- Take a path
  \[
  s_1s_2\cdots s_r.
  \]
- For each \(i\), take disjoint cliques \(A_i,B_i\), each of order \(r\).
- Join \(A_i\) completely to \(A_{i+1}\), and \(B_i\) completely to \(B_{i+1}\), for \(1\le i<r\).
- Join \(s_i\) to every vertex of \(A_i\cup B_i\).
- Add no other edges.

### Connectivity

Deleting all \(r\) vertices \(s_1,\ldots,s_r\) separates the \(A\)-cliques from the \(B\)-cliques, so
\[
\kappa(G_r)\le r.
\]

Conversely, delete fewer than \(r\) vertices. Every \(A_i\) and every \(B_i\) remains nonempty. The surviving \(A\)-vertices form a connected graph, as do the surviving \(B\)-vertices. At least one \(s_i\) survives and joins these two graphs. Every other surviving \(s_j\) attaches to them as well. Hence
\[
\kappa(G_r)=r.
\]

### Its unique shortest path is separating

Set \(x=s_1\) and \(y=s_r\), and assign column index \(i\) to \(s_i,A_i,B_i\). Every edge changes column index by at most one. Thus every \(x\)-\(y\) path has at least \(r-1\) edges.

The central path has exactly \(r-1\) edges. Any path of that length must increase its column index at every step. But the only neighbor of \(s_i\) in column \(i+1\) is \(s_{i+1}\). Therefore the unique shortest path is
\[
P=s_1s_2\cdots s_r.
\]
Its deletion separates the two rows of cliques.

This shows that no connectivity threshold—not even for \(k=1\)—can solve the unrestricted problem while insisting that the removable path be shortest.

### This is not a counterexample to Lovász’s conjecture

Choose \(a_i\in A_i\). The longer path
\[
Q=s_1a_1a_2\cdots a_rs_r
\]
is induced. After deleting it, the remaining central vertices are
\[
s_2,\ldots,s_{r-1},
\]
the \(A_i\) have order \(r-1\), and the \(B_i\) still have order \(r\).

The same connectivity calculation gives
\[
\kappa(G_r-V(Q))=r-2:
\]
deleting the remaining \(r-2\) central vertices separates the two rows, while any smaller deletion leaves every clique nonempty and at least one central vertex joining the rows.

Thus, for \(r\ge k+2\), this longer induced path does leave a \(k\)-connected graph.

## 5. What remains unresolved

The positive theorem depends on a uniform bound on induced-cycle length. The long-cycle certificate does not turn into a contradiction for arbitrary highly connected graphs, and the construction above shows that merely choosing a shortest path cannot overcome this issue.

The missing step is a controlled rerouting argument: one would need to replace a failed path by a longer induced path while protecting **all** potential separators of order less than \(k\). No such argument is established here.

Accordingly, the unrestricted existence of \(f(k)\) is neither proved nor disproved by this work. The established partial results are the bounded-induced-cycle-length theorem, the sharp restricted thresholds above, and the explicit obstruction to a shortest-path-only strategy.