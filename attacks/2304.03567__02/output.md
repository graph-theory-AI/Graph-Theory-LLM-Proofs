```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The intended sparse adjacency-list question remains open, but quadratic time is unavoidable in the adjacency-matrix model even for minimally strong digraphs and for dense general digraphs in an outgoing-adjacency-array model.",
  "would_publish": false,
  "caveats": "These are model-sensitive lower bounds and do not improve the source algorithm on sparse adjacency-list inputs."
}
```

# A model-sensitive partial answer

Throughout, “minimally strongly connected” means arc-minimal strongly connected. I use only the following consequence of the source definition: a left-maximal DFS-tree of a strong digraph is, in particular, a spanning out-arborescence consisting of arcs of the input digraph. Thus the lower bounds below apply independently of the additional left-maximality condition.

## 1. Sparsity of minimally strong digraphs

### Lemma 1
Every loopless minimally strongly connected digraph on \(n\ge 2\) vertices has at most \(2n-2\) arcs.

### Proof
Fix a vertex \(r\). Since \(D\) is strong, it contains

- a spanning out-arborescence \(T^+\) rooted at \(r\), and
- a spanning in-arborescence \(T^-\) rooted at \(r\).

Their union
\[
H=T^+\cup T^-
\]
is strongly connected: every vertex reaches \(r\) in \(T^-\), and \(r\) reaches every vertex in \(T^+\).

If an arc \(e\in A(D)\) did not belong to \(H\), then \(D-e\) would still contain the strongly connected spanning subdigraph \(H\), contradicting minimal strong connectivity. Hence
\[
A(D)=A(T^+)\cup A(T^-),
\]
and therefore
\[
|A(D)|\le (n-1)+(n-1)=2n-2.\qedhere
\]

Thus the source's \(O(n^2)\) bound is genuinely superlinear in the input size under an adjacency-list representation. On the other hand, an adjacency-matrix representation has size \(\Theta(n^2)\) even on these sparse inputs, and in that representation a subquadratic algorithm is impossible.

## 2. Quadratic lower bound in the adjacency-matrix model

### Theorem 2
For infinitely many \(n\), every deterministic adjacency-matrix query algorithm that outputs a left-maximal DFS-tree of a promised minimally strongly connected \(n\)-vertex digraph makes
\[
\Omega(n^2)
\]
queries in the worst case. This remains true if the algorithm is promised that the digraph is obtained by replacing every edge of a tree by its two orientations.

### Construction
Let \(n=2k\), with vertex sets
\[
A=\{a_1,\dots,a_k\},\qquad B=\{b_1,\dots,b_k\}.
\]
For each vector
\[
\sigma=(\sigma_1,\dots,\sigma_k)\in [k]^k,
\]
form the undirected graph \(H_\sigma\) with edges
\[
b_jb_{j+1}\quad(1\le j<k)
\]
and
\[
a_i b_{\sigma_i}\quad(1\le i\le k).
\]
Thus \(H_\sigma\) is a path on \(B\), with every \(a_i\) attached as a leaf to an independently chosen vertex of that path. In particular, \(H_\sigma\) is a tree.

Let \(D_\sigma\) be the bidirected version of \(H_\sigma\): every edge \(xy\) is replaced by the two arcs \(xy\) and \(yx\).

### Minimal strong connectivity
The digraph \(D_\sigma\) is strong because its underlying graph is connected and every edge is traversable in both directions. If one deletes an arc \(xy\), then deleting the underlying tree edge \(xy\) partitions the vertices into two sets \(X,Y\), with \(x\in X\) and \(y\in Y\). The deleted arc was the only arc directed from \(X\) to \(Y\). Hence \(D_\sigma-xy\) is not strong. Thus \(D_\sigma\) is minimally strongly connected.

### Why the output determines \(\sigma\)
Every spanning out-arborescence of \(D_\sigma\) has, as its underlying undirected graph, a connected spanning subgraph of the tree \(H_\sigma\). Consequently it must use every edge of \(H_\sigma\). In particular, it reveals the unique neighbor \(b_{\sigma_i}\) of every leaf \(a_i\).

This remains true if the root may be selected by the algorithm: if \(a_i\) is the root, its only possible first tree arc toward the rest of the graph is \(a_i b_{\sigma_i}\); otherwise its parent arc is \(b_{\sigma_i}a_i\).

### Query adversary
Grant the algorithm the path on \(B\) for free, and even let one query reveal both orientations of a pair. For each \(i\), the unknown \(\sigma_i\) is one marked item among the \(k\) candidates
\[
a_i b_1,\dots,a_i b_k.
\]

Maintain a candidate set \(C_i=[k]\). Whenever the algorithm queries \(a_i b_j\) with \(j\in C_i\) and \(|C_i|\ge2\), answer that it is absent and remove \(j\) from \(C_i\). Once \(C_i\) is a singleton, its remaining member can be chosen as \(\sigma_i\).

If the algorithm stops while some \(|C_i|\ge2\), two inputs differing only in \(\sigma_i\) remain consistent with its transcript. The same output tree cannot be valid for both, since the unique edge incident with \(a_i\) differs. Hence at least \(k-1\) candidate pairs must be queried for every \(i\), giving
\[
k(k-1)=\frac{n^2}{4}-\frac n2
\]
queries.

This proves the theorem. \(\square\)

### Randomized zero-error algorithms
The same order of growth holds for Las Vegas algorithms. Choose the \(\sigma_i\) independently and uniformly. For one \(i\), identifying one marked candidate among \(k\) by equality queries takes expected
\[
\frac{1+2+\cdots +(k-1)+(k-1)}{k}
=\frac{(k-1)(k+2)}{2k}
\]
queries, where the final candidate may be inferred without querying it. Summing over the \(k\) independent leaves gives expected \(\Omega(k^2)=\Omega(n^2)\) queries on this distribution, and therefore on some input.

This argument does not address bounded-error algorithms.

## 3. Dense general digraphs require \(\Omega(m)\) outgoing-list probes

The usual objection to the preceding theorem is that the source problem intends adjacency lists. For minimally strong digraphs this is decisive, since Lemma 1 gives \(m=O(n)\). In the unrestricted strong case, however, even producing the underlying spanning out-tree can force inspection of \(\Theta(m)\) outgoing-list entries.

### Theorem 3
In the model where each vertex is represented by an arbitrarily ordered outgoing adjacency array and one probe returns one head vertex, there are strong digraphs with \(m=\Theta(n^2)\) on which every deterministic algorithm producing a spanning DFS-tree—and hence every algorithm producing a left-maximal DFS-tree—requires \(\Omega(m)\) probes.

### Construction
Again let
\[
A=\{a_1,\dots,a_k\},\qquad B=\{b_1,\dots,b_k\}.
\]
For a permutation \(\pi\in S_k\), define \(D_\pi\) by:

1. all arcs \(b_i b_j\) with \(i\ne j\);
2. the \(k\) arcs
   \[
   b_j a_{\pi(j)}\qquad(1\le j\le k);
   \]
3. the \(k\) arcs
   \[
   a_i b_1\qquad(1\le i\le k).
   \]

Then
\[
m=k(k-1)+2k=k^2+k=\Theta(n^2).
\]

The digraph is strong: every \(a_i\) reaches \(B\) through \(a_i b_1\), the subdigraph on \(B\) is complete, and every \(a_i\) is reached through its unique incoming arc from \(B\).

Each outgoing array of \(b_j\) has length \(k\): it consists of the \(k-1\) other vertices of \(B\) and one hidden vertex \(a_{\pi(j)}\). Each \(a_i\) has the known one-element array \((b_1)\).

Every nonroot \(a_i\) must receive its tree-parent arc through its unique incoming arc. Thus a spanning out-tree reveals all hidden arcs, except possibly the one entering the root if the algorithm chooses a vertex of \(A\) as root. The permutation constraint then still forces the algorithm to resolve all but at most one of the \(k\) rows.

An adversary answers the first \(k-1\) distinct probes in each \(b_j\)-row with the \(k-1\) vertices of \(B\), placing the unique \(A\)-entry in the last probed position. Hidden \(A\)-labels are assigned bijectively as rows are completed. Until all but at most one rows have exposed their \(A\)-entry, at least two permutations remain consistent and require different parent arcs for a nonroot leaf. Therefore at least \(k-1\) rows must be completely probed, at a cost of
\[
k(k-1)=\Omega(k^2)=\Omega(m).
\]
\(\square\)

This lower bound is specific to outgoing adjacency arrays. If singleton incoming lists are also supplied explicitly, this particular family becomes easy.

## 4. Consequences for the open problem

The conclusions are as follows.

1. **Adjacency-matrix formulation.**  
   The answer to “can it be done in \(o(n^2)\)?” is unconditionally negative, even for minimally strongly connected bidirected trees.

2. **Promised minimally strong adjacency-list formulation.**  
   Here \(m\le2n-2\), so the matrix lower bound is irrelevant. The only immediate lower bound is linear, and I do not obtain an improvement over the paper's \(O(n^2)\) algorithm.

3. **General strong digraphs.**  
   A complexity bound solely in terms of \(n\) cannot be subquadratic in standard explicit dense representations. The meaningful target is therefore an input-sensitive bound such as
   \[
   O(m+f(n)).
   \]
   The outgoing-array construction shows an \(\Omega(m)\) worst-case lower bound even before left-maximality is imposed.

4. **Sparsification does not automatically settle the general case.**  
   One can find a strong spanning subdigraph with at most \(2n-2\) arcs by taking the union of an in- and an out-arborescence. However, a tree that is left-maximal relative to that sparse subdigraph need not be left-maximal relative to the original digraph; such a transfer would require a separate monotonicity theorem.

## Remaining gap

The intended question—whether a left-maximal DFS-tree of an arc-minimal strong digraph given by outgoing adjacency lists can be found in \(o(n^2)\), ideally near-linear time—remains unresolved here. The lower bounds above use only the necessity of outputting a spanning out-arborescence and therefore give no obstruction beyond \(\Omega(n)\) on those sparse inputs.