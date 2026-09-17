```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The conjecture is false: an explicit two-ended highly arc-transitive digraph has connected, noncomplete bipartite tiles.",
  "would_publish": false,
  "caveats": "The supplied catalog already records a disproof; the construction below is verified directly, with no claim of novelty."
}
```

## A self-contained counterexample

The supplied catalog attributes the negative resolution to DeVos, Mohar, and Šámal. Rather than relying on that literature report, we can verify an explicit counterexample directly.

Let \(S=\{0,1,2\}\). Define a digraph \(D\) by
\[
V(D)=\mathbb Z\times S\times S,
\]
with arcs
\[
(i,a,b)\longrightarrow(i+1,c,d)
\quad\Longleftrightarrow\quad a\ne d.
\tag{1}
\]
Put
\[
X_i=\{i\}\times S\times S,
\qquad
T_i=D[X_i\cup X_{i+1}].
\]

We will prove that:

1. \(D\) is connected and locally finite;
2. \(D\) is highly arc-transitive;
3. \(\{X_i:i\in\mathbb Z\}\) is an invariant finite-block system for the full digraph automorphism group;
4. the underlying undirected graph has exactly two ends;
5. every \(T_i\) is connected but not complete bipartite.

Thus the \(T_i\) are genuine tiles violating the conjecture.

### 1. Local finiteness and connectivity

Every vertex has outdegree \(6\): in (1), there are three choices for \(c\) and two choices for \(d\). Similarly, every vertex has indegree \(6\).

Each \(T_i\) is connected as an undirected graph. Indeed, consider any two vertices
\[
(i,a,b),\quad(i,a',b')\in X_i.
\]
There exists \(d\in S\setminus\{a,a'\}\), since \(|S|=3\). Consequently, \((i+1,0,d)\) is adjacent to both vertices. Thus all vertices of \(X_i\) lie in the same component of \(T_i\). Every vertex of \(X_{i+1}\) has a neighbor in \(X_i\), so \(T_i\) is connected.

Consecutive such subgraphs overlap in an entire level. Their union is \(D\), so the underlying undirected graph of \(D\) is connected.

### 2. High arc-transitivity

The shift
\[
\tau(i,a,b)=(i+1,a,b)
\]
is an automorphism.

There is also a large family of level-preserving automorphisms. For an arbitrary sequence
\[
(\sigma_i)_{i\in\mathbb Z},
\qquad \sigma_i\in\operatorname{Sym}(S),
\]
define
\[
\Phi_\sigma(i,a,b)
   =\bigl(i,\sigma_i(a),\sigma_{i-1}(b)\bigr).
\tag{2}
\]
This map is bijective. Moreover, an arc in (1) is taken to the pair
\[
\bigl(i,\sigma_i(a),\sigma_{i-1}(b)\bigr),
\qquad
\bigl(i+1,\sigma_{i+1}(c),\sigma_i(d)\bigr).
\]
These form an arc exactly when
\[
\sigma_i(a)\ne \sigma_i(d),
\]
which is equivalent to \(a\ne d\). Hence every \(\Phi_\sigma\) is an automorphism.

Now fix \(k\ge 0\) and two directed \(k\)-arcs. Using shifts, it suffices to consider arcs
\[
v_0\to v_1\to\cdots\to v_k,
\qquad
w_0\to w_1\to\cdots\to w_k,
\]
where
\[
v_j=(j,a_j,b_j),
\qquad
w_j=(j,a'_j,b'_j).
\]
For \(0\le j<k\), the arc conditions give
\[
a_j\ne b_{j+1},
\qquad
a'_j\ne b'_{j+1}.
\]
Since \(\operatorname{Sym}(S)\) is transitive on ordered pairs of distinct elements, choose \(\sigma_j\) satisfying
\[
\sigma_j(a_j)=a'_j,
\qquad
\sigma_j(b_{j+1})=b'_{j+1}.
\tag{3}
\]
Independently choose
\[
\sigma_{-1}(b_0)=b'_0,
\qquad
\sigma_k(a_k)=a'_k.
\tag{4}
\]
Take all remaining permutations to be the identity. For \(k=0\), only the two endpoint choices in (4) are needed.

Equations (2)–(4) imply
\[
\Phi_\sigma(v_j)=w_j\qquad(0\le j\le k).
\]
Therefore \(D\) is \(k\)-arc-transitive for every \(k\), and hence highly arc-transitive.

### 3. The levels are genuine invariant blocks

It is important that the \(X_i\) are not merely an arbitrarily chosen slicing.

Define the height function
\[
h(i,a,b)=i.
\]
Every arc \(u\to v\) satisfies
\[
h(v)-h(u)=1.
\]
Let \(\alpha\in\operatorname{Aut}(D)\), and put
\[
\delta_\alpha(v)=h(\alpha(v))-h(v).
\]
For every arc \(u\to v\),
\[
\delta_\alpha(v)-\delta_\alpha(u)
=
\bigl(h(\alpha(v))-h(\alpha(u))\bigr)
-\bigl(h(v)-h(u)\bigr)
=1-1=0.
\]
Because the underlying graph is connected, \(\delta_\alpha\) is constant on all vertices. Thus, for some integer \(t=t(\alpha)\),
\[
\alpha(X_i)=X_{i+t}\qquad\text{for every }i.
\]

Consequently, the partition into the nine-vertex sets \(X_i\) is invariant under the full digraph automorphism group. Since \(D\) is vertex-transitive, this is a system of imprimitivity. All arcs go from \(X_i\) to \(X_{i+1}\), so the subgraphs \(T_i\) are tiles in the stated sense.

### 4. Exactly two ends

Here ends are those of the underlying undirected graph.

For \(N\ge0\), delete the finite set
\[
C_N=\bigcup_{i=-N}^{N}X_i.
\]
The remaining graph has exactly two components, on the vertex sets
\[
\bigcup_{i\le -N-1}X_i
\quad\text{and}\quad
\bigcup_{i\ge N+1}X_i.
\]
There are no edges between these sets because every edge joins consecutive levels. Both induced subgraphs are infinite and connected: each is a union of connected consecutive tiles with nonempty overlaps.

The sets \(C_N\) exhaust the vertex set, and every finite vertex set is contained in some \(C_N\). These deletions therefore show that the underlying graph has exactly two ends.

### 5. The tiles are not unions of complete bipartite graphs

Each \(T_i\) has nine vertices in each bipartition class. Every vertex has degree \(6\) within \(T_i\). By Section 1, \(T_i\) is connected.

If \(T_i\) were a disjoint union of complete bipartite graphs, its connectivity would force it to be a single complete bipartite graph. With its bipartition sizes, that graph would be \(K_{9,9}\), whose vertices have degree \(9\), not \(6\). This is impossible.

More explicitly, partition its two sides into
\[
L_a=\{(i,a,b):b\in S\},
\qquad
R_d=\{(i+1,c,d):c\in S\}.
\]
There are all possible edges between \(L_a\) and \(R_d\) precisely when \(a\ne d\). Hence each tile is obtained from
\[
K_{3,3}\setminus\text{a perfect matching}\cong C_6
\]
by replacing each vertex with an independent set of three vertices and each edge with a complete bipartite graph between the corresponding sets. It is therefore a connected, noncomplete bipartite graph on \(18\) vertices.

## Conclusion

The digraph
\[
(i,a,b)\to(i+1,c,d)\quad\Longleftrightarrow\quad a\ne d,
\qquad a,b,c,d\in\{0,1,2\},
\]
is locally finite, two-ended, and highly arc-transitive, while all its tiles are connected and noncomplete bipartite graphs. It is an explicit counterexample to the conjecture.

Every required property has been verified directly; no external theorem or unproved conjecture is needed.