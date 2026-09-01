```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted threshold problem remains unresolved, but exact fixed excess is polynomial-time, and the threshold problem is polynomial on graphs with bounded geodesic multiplicity, bounded induced-cycle length, or cactus structure.",
  "would_publish": false,
  "caveats": "No polynomial algorithm or NP-hardness proof is obtained for unrestricted graphs, and the literature novelty of the partial results has not been checked."
}
```

# 1. Statement and notation

All graphs are finite, simple, and undirected, and path length means number of edges. Let \(s,t\in V(G)\), with \(t\) reachable from \(s\), and put
\[
d=\operatorname{dist}_G(s,t).
\]
The problem is to decide whether there is an induced \(s\)-\(t\) path \(P\) satisfying
\[
|E(P)|\ge d+3.
\]

I do not resolve the unrestricted problem. I give:

1. a polynomial algorithm for every fixed **exact** excess;
2. an exact structural reformulation using an extendable prefix of excess \(3\) or \(4\);
3. an output-sensitive polynomial algorithm for the threshold problem when the number of shortest paths from one endpoint is bounded;
4. a polynomial algorithm on graphs with bounded maximum induced-cycle length, including an \(O(nm)\)-type algorithm on chordal graphs;
5. a linear-time solution on cactus graphs.

The first item also clarifies that “excess \(=3\)” and “excess at least \(3\)” are quite different problems.

# 2. The defect of a path

Let
\[
\lambda(v)=\operatorname{dist}_G(s,v).
\]
For an oriented traversal of an edge \(uv\), define
\[
c(u,v)=1+\lambda(u)-\lambda(v).
\]
Because adjacent vertices lie in the same or consecutive BFS layers,
\[
c(u,v)\in\{0,1,2\}.
\]
Thus an edge going one layer away from \(s\) has cost \(0\), an edge within one layer has cost \(1\), and an edge going one layer toward \(s\) has cost \(2\).

For a walk
\[
W=(v_0=s,v_1,\ldots,v_r)
\]
define its defect by
\[
\delta(W)=\sum_{i=1}^r c(v_{i-1},v_i).
\]
The sum telescopes:
\[
\delta(W)=r-\lambda(v_r).
\]
In particular, if \(v_r=t\), then
\[
\delta(W)=r-d,
\]
so defect is exactly excess over the shortest \(s\)-\(t\) path.

# 3. Exact fixed excess is polynomial-time

## Theorem 3.1

For every fixed \(K\), there is an \(O(Kn^{K+2})\)-time algorithm deciding whether \(G\) contains an induced \(s\)-\(t\) path whose excess belongs to any prescribed subset of \(\{0,\ldots,K\}\).

In particular:

- exact excess \(2\) is decidable in \(O(n^4)\);
- exact excess \(3\) is decidable in \(O(n^5)\);
- existence of a path with excess in \(\{3,4\}\) is decidable in \(O(n^6)\).

## Proof

Consider a walk \(W=(v_0,\ldots,v_r)\) of total defect at most \(K\). For positions \(i<j\), the defect of the corresponding subwalk is
\[
\delta(i,j)=(j-i)+\lambda(v_i)-\lambda(v_j)\le K.
\]

If \(v_iv_j\in E(G)\), then \(\lambda(v_j)-\lambda(v_i)\le1\), and hence
\[
j-i=\delta(i,j)+\lambda(v_j)-\lambda(v_i)\le K+1.
\]
Thus every possible chord joins vertices whose positions differ by at most \(K+1\).

Likewise, if \(v_i=v_j\), then
\[
j-i=\delta(i,j)\le K.
\]
Therefore, for walks of defect at most \(K\), simplicity and inducedness can be checked using only the last \(K+1\) vertices.

Construct a state graph whose states consist of:

- the current total defect \(e\in\{0,\ldots,K\}\);
- the ordered tuple of the last at most \(K+1\) vertices of the current prefix.

From a state ending in \(v\), append a neighbor \(w\) if:

1. \(e+c(v,w)\le K\);
2. \(w\) is distinct from every stored vertex;
3. \(w\) is nonadjacent to every stored vertex except \(v\).

A vertex omitted from the stored tuple is at positional distance at least \(K+2\) from \(w\), and the preceding inequalities show that it can neither equal nor be adjacent to \(w\). Hence merging prefixes with the same state is safe.

There are \(O(Kn^{K+1})\) states and at most \(n\) possible transitions per state. Reachability of a state ending in \(t\) with an accepted defect gives the result. ∎

Thus, if the catalog phrase “excess \(=3\)” is interpreted literally as equality, that problem is polynomial. The difficulty is the unbounded threshold problem: a yes-instance may have no path of excess \(3\), or indeed of any bounded excess.

For example, let \(G=C_N\), and let \(s,t\) be at distance \(2\) on the cycle. The two \(s\)-\(t\) paths have lengths \(2\) and \(N-2\), and both are induced. The only positive excess is \(N-4\), which is arbitrarily large.

# 4. An exact extendable-prefix characterization

The preceding defect calculus gives a useful reformulation of the full problem.

For an induced path
\[
Q=(q_0=s,q_1,\ldots,q_r=x),
\]
let
\[
F(Q)=N_G[V(Q)\setminus\{x\}]\setminus\{x\},
\qquad
H_Q=G-F(Q),
\]
where \(N_G[S]\) denotes the closed neighborhood of \(S\). Thus \(H_Q\) retains \(x\), but deletes every earlier vertex of \(Q\) and every vertex adjacent to one of them.

## Proposition 4.1

There is an induced \(s\)-\(t\) path of length at least \(d+3\) if and only if there are a vertex \(x\) and an induced \(s\)-\(x\) path \(Q\) such that

\[
|E(Q)|-\operatorname{dist}_G(s,x)\in\{3,4\}
\]
and \(x,t\) lie in the same component of \(H_Q\).

## Proof

Suppose first that
\[
P=(v_0=s,\ldots,v_\ell=t)
\]
is induced and \(\ell-d\ge3\). Define
\[
h_i=i-\lambda(v_i).
\]
Then \(h_0=0\), \(h_\ell=\ell-d\ge3\), and
\[
h_i-h_{i-1}=c(v_{i-1},v_i)\in\{0,1,2\}.
\]
Let \(j\) be the first index with \(h_j\ge3\). Then
\[
h_j\in\{3,4\}.
\]
Set \(x=v_j\) and \(Q=P[s,v_j]\). Since \(P\) is induced, every vertex of the suffix \(P[v_j,t]\), except \(x\), avoids the closed neighborhood of \(V(Q)\setminus\{x\}\). Hence this suffix survives in \(H_Q\), so \(x\) and \(t\) are connected there.

Conversely, suppose such \(Q\) exists. Let \(R\) be a shortest \(x\)-\(t\) path in \(H_Q\). Then \(R\) is induced. By construction, no vertex of \(R\setminus\{x\}\) is adjacent to a vertex of \(Q\setminus\{x\}\). Consequently \(Q\cup R\) is an induced \(s\)-\(t\) path.

Writing \(r=|E(Q)|-\lambda(x)\in\{3,4\}\), its length is at least
\[
\lambda(x)+r+\operatorname{dist}_G(x,t)
   \ge d+r
   \ge d+3.
\]
This proves the equivalence. ∎

The remaining obstruction is now precise: one must find an excess-\(3\) or excess-\(4\) prefix while retaining enough information about the closed neighborhood of its entire, possibly long, vertex set to test extendability. The bounded-defect dynamic program of Theorem 3.1 cannot discard that information once an arbitrary-defect suffix is allowed.

# 5. Polynomial time under bounded geodesic multiplicity

Let \(g_s(v)\) be the number of shortest \(s\)-\(v\) paths and define
\[
\mu_s=\max_{v\in V(G)}g_s(v).
\]

## Theorem 5.1

The original threshold problem can be solved in
\[
\mu_s^5\, n^{O(1)}
\]
time. More explicitly, a coarse bound is
\[
O\!\left(nm^4\mu_s^5(n+m)\right).
\]
The same holds with \(s\) and \(t\) interchanged, so one may use
\[
\min\{\mu_s,\mu_t\}.
\]

In particular, the problem is polynomial-time solvable whenever every vertex has a unique shortest path from \(s\), or from \(t\).

## Proof

Call an oriented edge \(uv\) upward if
\[
\lambda(v)=\lambda(u)+1.
\]
An upward path consists entirely of zero-defect edges.

For arbitrary vertices \(u,v\), the number of upward \(u\)-\(v\) paths is at most \(\mu_s\). Indeed, fix one shortest \(s\)-\(u\) path. Concatenating it with any upward \(u\)-\(v\) path gives a distinct shortest \(s\)-\(v\) path.

An \(s\)-\(x\) path of defect \(3\) or \(4\) contains at most four non-upward edges. Enumerate:

1. an ordered list
   \[
   (a_1,b_1),\ldots,(a_k,b_k),\qquad k\le4,
   \]
   of oriented non-upward edges;
2. with total cost
   \[
   \sum_{i=1}^k c(a_i,b_i)\in\{3,4\};
   \]
3. an endpoint \(x\);
4. all upward paths in the gaps
   \[
   s\leadsto a_1,\quad
   b_i\leadsto a_{i+1},\quad
   b_k\leadsto x.
   \]

There are at most five upward portions, each having at most \(\mu_s\) choices. Every defect-\(3\) or defect-\(4\) path is generated in this manner. For each concatenation, explicitly test whether it is a simple induced path \(Q\), and then run a connectivity search between \(x\) and \(t\) in \(H_Q\). Proposition 4.1 proves correctness.

There are \(O(m^4n)\) choices of the anomalous edges and endpoint, and at most \(\mu_s^5\) choices for the upward portions. ∎

When \(\mu_s=1\), the upward edges form a rooted BFS tree: each upward portion is uniquely determined by its endpoints. This class includes graphs with arbitrarily long induced cycles—for example, an odd cycle rooted at any vertex—so the result is not merely a bounded-hole result.

# 6. Graphs with bounded induced-cycle length

Fix \(q\ge3\), and suppose that \(G\) has no induced cycle on more than \(q\) vertices.

## Lemma 6.1: local inducedness

Let
\[
W=(v_0,v_1,\ldots,v_r)
\]
be generated as follows. Whenever \(v_j\) is appended, require:

1. \(v_{j-1}v_j\in E(G)\);
2. \(v_j\) is distinct from the last \(q-1\) previous vertices;
3. \(v_j\) is nonadjacent to all of those last \(q-1\) vertices except \(v_{j-1}\).

Then \(W\) is a simple induced path.

## Proof

Proceed by induction. Suppose the current prefix is induced and append \(w=v_j\).

If \(w\) repeats a vertex \(v_i\) earlier than the stored window, then the edge \(wv_{j-1}\) is an edge \(v_iv_{j-1}\) joining nonconsecutive vertices of the induced prefix, a contradiction.

Suppose instead that \(w\) is adjacent to an earlier vertex outside the stored window. Choose the largest such index \(i\). Then
\[
w,v_i,v_{i+1},\ldots,v_{j-1},w
\]
is an induced cycle: the old prefix has no chords, and maximality of \(i\) excludes further edges from \(w\) into its interior. Since \(i\le j-q\), this cycle has at least \(q+1\) vertices, contrary to the hypothesis. ∎

## Theorem 6.2

For each fixed \(q\), the longest induced \(s\)-\(t\) path can be found in \(O(n^q)\) time on graphs with no induced cycle longer than \(q\).

## Proof

Make a state from the ordered last at most \(q-1\) vertices. A transition shifts the tuple and appends a vertex satisfying the local conditions of Lemma 6.1.

The state digraph is acyclic. Otherwise, repeatedly traversing a directed state cycle would generate an arbitrarily long locally valid sequence, which by Lemma 6.1 would be a simple induced path, impossible in a finite graph.

There are \(O(n^{q-1})\) states and \(O(n)\) candidate extensions per state. A longest-path dynamic program in this acyclic state graph gives the maximum induced \(s\)-\(t\) path length. ∎

## Chordal graphs

For chordal graphs one may take \(q=3\). There is a particularly simple auxiliary digraph:

- its states are ordered edges \((u,v)\);
- there is an arc
  \[
  (u,v)\longrightarrow(v,w)
  \]
  exactly when \(w\ne u\) and \(uw\notin E(G)\).

In a chordal graph, every directed walk in this auxiliary graph projects to an induced path, and the auxiliary graph is acyclic. It has \(2m\) states and at most
\[
\sum_v \deg(v)^2=O(nm)
\]
arcs. Thus the maximum induced \(s\)-\(t\) path, and hence the excess-\(3\) decision problem, is computable in \(O(nm)\) time given constant-time adjacency tests.

For fixed \(q\), membership in the bounded-induced-cycle class can also be tested polynomially. To find an induced cycle of length at least \(q+1\), enumerate an induced path
\[
Q=(v_0,\ldots,v_{q-1})
\]
on \(q\) vertices, delete the closed neighborhood of its internal vertices while retaining \(v_0,v_{q-1}\), and test whether the endpoints remain connected. A shortest residual path closes \(Q\) to an induced cycle of length at least \(q+1\).

# 7. Cactus graphs

The problem is also easy on cactus graphs, even though their induced cycles can be arbitrarily long.

Use the block-cutvertex decomposition. Every simple \(s\)-\(t\) path traverses the unique sequence of blocks on the block-cut tree route from \(s\) to \(t\). Its restrictions to these blocks are independent, and concatenating locally induced paths produces a globally induced path. Consequently both shortest and maximum induced path lengths add over these blocks.

A cactus block is either:

- a bridge, contributing exactly one edge; or
- a chordless cycle.

For a cycle block with entry and exit vertices \(a,b\), let the two arc lengths be \(p\le q\).

- If \(p=1\), the other arc is not induced because the edge \(ab\) is a chord, so the local maximum is \(1\).
- If \(p,q\ge2\), both arcs are induced, so the local shortest and maximum lengths are \(p\) and \(q\), respectively.

Summing these quantities over the block route decides whether the total excess is at least \(3\). This gives a linear-time algorithm after standard block decomposition.

# 8. What remains open

The unrestricted problem is not settled by these arguments.

The exact characterization in Proposition 4.1 reduces the problem to finding an extendable near-geodesic prefix, but there may be exponentially many such prefixes. Different prefixes with the same endpoint, defect, and last few vertices can delete incomparable closed neighborhoods, so the finite-memory dynamic program for bounded total excess cannot safely merge them once the suffix is allowed arbitrary excess.

The cycle \(C_N\) with \(s,t\) at distance \(2\) also shows that no bounded-excess witness theorem is possible: the only positive excess can be \(N-4\).

Thus I obtain neither a general polynomial algorithm nor an NP-hardness reduction. The principal concrete advances are the exact fixed-excess algorithm, the extendable-prefix equivalence, and complete algorithms for the structural classes above.