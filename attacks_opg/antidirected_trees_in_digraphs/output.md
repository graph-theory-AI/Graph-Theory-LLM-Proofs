```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured threshold under a short almost-antidirected odd-cycle exclusion, and obtain an asymptotically sharp density bound for highly unbalanced trees.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; novelty of these elementary partial results is not claimed."
}
```

## 1. Results obtained

Throughout, digraphs are finite and loopless, with no parallel arcs; opposite arcs are allowed. Copies need not be induced. The case \(k=1\) is trivial, so assume \(k\ge 2\).

Let \(T\) be an antidirected tree, with source class \(S\) and sink class \(R\). Write
\[
s=|S|,\qquad t=|R|,\qquad s+t=k,
\]
and define
\[
\lambda(T)=\max\{\operatorname{dist}_T(x,y):x\in S,\ y\in R\}.
\]
Thus \(\lambda(T)\) is odd and at most \(\operatorname{diam}(T)\).

Call an orientation of an odd cycle **almost antidirected** if, within the chosen cycle, exactly one vertex has both positive indegree and positive outdegree, while every other vertex is a source or a sink. For length three this is precisely a transitive triangle. Extra arcs in the ambient digraph are irrelevant to this definition.

### Theorem 1: an explicit obstruction dichotomy

If
\[
|A(D)|>(k-2)|V(D)|,
\]
then \(D\) contains either

1. a copy of \(T\), or
2. an almost-antidirected odd cycle of some length \(\ell\) satisfying
   \[
   3\le \ell\le \lambda(T).
   \]

Consequently, the conjectured threshold is valid whenever the second possibility is excluded. In particular:

- **Bipartite hosts:** the conjecture holds if the underlying undirected graph of \(D\) is bipartite. Arcs in both directions across its bipartition are allowed.
- **Large odd girth:** it holds if the underlying graph has odd girth greater than \(\operatorname{diam}(T)\).
- **Small-diameter targets:** every transitive-triangle-free digraph satisfying the conjectured density contains every antidirected tree of order \(k\) and diameter at most \(4\).

I also obtain the following bound without any restriction on the host.

### Theorem 2: a leaf-sensitive density bound

Let
\[
\ell(T)=\max\bigl\{
|\{v\in S:\deg_T(v)=1\}|,
|\{v\in R:\deg_T(v)=1\}|
\bigr\},
\qquad h=k-\ell(T).
\]
Then
\[
|A(D)|>
\bigl(k-2+\max\{h-2,0\}\bigr)|V(D)|
\tag{1}
\]
guarantees a copy of \(T\).

In particular, if \(r=\min\{s,t\}\ge2\), then the simpler condition
\[
|A(D)|>(k+2r-5)|V(D)|
\tag{2}
\]
suffices. The ratio of this sufficient coefficient to \(k-2\) tends to \(1\) whenever \(r=o(k)\).

These are partial results only. Here are complete proofs.

## 2. A weighted bipartite embedding lemma

**Lemma.** Let \(H\) be a bipartite graph with specified parts \(L,R'\). If
\[
e(H)>(t-1)|L|+(s-1)|R'|,
\tag{3}
\]
then \(H\) contains the underlying tree of \(T\), with \(S\) mapped into \(L\) and \(R\) mapped into \(R'\).

**Proof.** Repeatedly delete a vertex of \(L\) whose current degree is at most \(t-1\), or a vertex of \(R'\) whose current degree is at most \(s-1\).

If this procedure deleted every edge, charging each edge to the first of its endpoints deleted would give
\[
e(H)\le (t-1)|L|+(s-1)|R'|,
\]
contrary to (3). Thus a nonempty subgraph \(H_0\) remains, satisfying
\[
d_{H_0}(x)\ge t\quad(x\in L\cap V(H_0)),
\qquad
d_{H_0}(y)\ge s\quad(y\in R'\cap V(H_0)).
\]

Root \(T\) at a vertex of \(S\) and embed it greedily. When a new sink is required, at most \(t-1\) vertices of the right part have already been used, whereas its parent has at least \(t\) neighbors. When a new source is required, the corresponding bounds are \(s-1\) and \(s\). Hence the role-respecting embedding can be completed. \(\square\)

## 3. Proof of Theorem 1

### 3.1. Split each vertex into its two possible roles

Construct a bipartite graph \(B(D)\) with parts
\[
V^+=\{v^+:v\in V(D)\},\qquad
V^-=\{v^-:v\in V(D)\},
\]
putting an edge \(u^+v^-\) exactly when \(u\to v\) is an arc of \(D\).

Writing \(n=|V(D)|\), we have
\[
e(B(D))=|A(D)|>(k-2)n
=(t-1)|V^+|+(s-1)|V^-|.
\]
The lemma therefore gives an embedding of \(T\) into \(B(D)\), with sources in \(V^+\) and sinks in \(V^-\).

Project this embedding back to \(D\), identifying \(v^+\) and \(v^-\) with \(v\). The resulting map
\[
f:V(T)\longrightarrow V(D)
\]
preserves every arc and is injective separately on \(S\) and on \(R\).

The sole possible obstruction is a **cross-role collision**:
\[
f(x)=f(y),\qquad x\in S,\ y\in R.
\]

### 3.2. A shortest collision gives the claimed cycle

If there is no collision, \(f\) is a copy of \(T\).

Otherwise choose a colliding pair \(x,y\) minimizing
\[
\ell=\operatorname{dist}_T(x,y),
\]
and write its tree path as
\[
x=x_0,x_1,\ldots,x_\ell=y.
\]
Because \(x,y\) lie in opposite bipartition classes, \(\ell\) is odd. Also \(\ell\ne1\), since an adjacent colliding pair would map an arc to a loop.

By minimality, no two vertices of this path have the same image except its endpoints. Indeed, any other repetition would give a colliding pair at smaller tree distance. Hence
\[
f(x_0),f(x_1),\ldots,f(x_{\ell-1})
\]
are the distinct vertices of a cycle in \(D\).

Along the tree path, every internal vertex is a source or a sink. Identifying the source endpoint \(x_0\) with the sink endpoint \(x_\ell\) creates exactly one vertex having one incoming and one outgoing cycle arc. The resulting cycle is therefore almost antidirected.

Finally,
\[
3\le\ell\le\lambda(T),
\]
as required. \(\square\)

### Consequences

Every almost-antidirected odd cycle is, after forgetting orientations, an odd cycle. Thus underlying odd girth greater than \(\operatorname{diam}(T)\) excludes every obstruction from Theorem 1.

If \(\operatorname{diam}(T)\le4\), the only possible obstruction length is \(3\), namely a transitive triangle.

Notice that this last condition is weaker than requiring the underlying graph to be triangle-free: directed cyclic triangles are allowed.

## 4. Proof of Theorem 2

By reversing every arc of both \(D\) and \(T\), if necessary, assume that \(T\) has \(\ell(T)\) sink leaves. Remove all those leaves, obtaining a tree \(T_0\) of order
\[
h=k-\ell(T).
\]

Set
\[
p=k-1,\qquad q=\max\{1,h-1\}.
\]
The coefficient in (1) is exactly
\[
p+q-2=k-2+\max\{h-2,0\}.
\]

Apply the deletion argument from the preceding lemma to \(B(D)\), now deleting left vertices of degree at most \(p-1\) and right vertices of degree at most \(q-1\). The assumed density leaves a nonempty arc-subdigraph \(D_0\) such that
\[
d^+_{D_0}(v)>0\implies d^+_{D_0}(v)\ge k-1,
\tag{4}
\]
and
\[
d^-_{D_0}(v)>0\implies d^-_{D_0}(v)\ge \max\{1,h-1\}.
\tag{5}
\]

Here a vertex need not have both kinds of degree positive. This causes no problem because every vertex of an antidirected tree needs only one of the two roles.

### Embed \(T_0\)

If \(h=1\), its remaining vertex is a source; map it to the tail of any arc of \(D_0\).

If \(h\ge2\), first map an edge of \(T_0\) to an arc of \(D_0\), then extend greedily. Every newly embedded source has positive outdegree, and every newly embedded sink has positive indegree. Both relevant degree bounds are at least \(h-1\).

When adding another vertex of \(T_0\), at most \(h-1\) vertices have been used. Since the host is loopless, at most \(h-2\) of them can be neighbors of the parent in the required direction. Thus an unused neighbor is available.

This gives an injective copy of \(T_0\) in the original digraph, not merely in its split graph.

### Attach the removed leaves

All removed vertices are sink leaves. Add them one at a time.

Their parents are already embedded sources, each having outdegree at least \(k-1\) by (4). Before any addition, at most \(k-1\) vertices have been used; at most \(k-2\) of them can be outneighbors of the parent. Hence an unused outneighbor always exists.

This completes a copy of \(T\). \(\square\)

### Derivation of the unbalanced-tree bound

Let \(r=\min\{s,t\}\), and consider the larger bipartition class, of size \(k-r\). Since every edge has exactly one endpoint in that class,
\[
\sum_{v\text{ in the larger class}}(\deg_T(v)-1)
=(k-1)-(k-r)=r-1.
\]
Every nonleaf contributes at least one. Therefore the larger class has at most \(r-1\) nonleaves and at least
\[
(k-r)-(r-1)=k-2r+1
\]
leaves. Consequently,
\[
h=k-\ell(T)\le 2r-1.
\]
For \(r\ge2\), Theorem 2 now gives
\[
k-2+\max\{h-2,0\}\le k+2r-5,
\]
proving (2). When \(r=1\), the tree is a directed star, and Theorem 2 gives the exact coefficient \(k-2\).

## 5. A non-caterpillar illustration

Let \(T_r\) be the tree obtained by subdividing every edge of \(K_{1,r}\), with each subdivision vertex a source and the original center and leaves sinks. For \(r\ge3\), this is not a caterpillar.

It has
\[
k=2r+1,\qquad \operatorname{diam}(T_r)=4,\qquad \ell(T_r)=r.
\]
Thus the two results give:

- If \(D\) is transitive-triangle-free, then
  \[
  |A(D)|>(2r-1)|V(D)|
  \quad\Longrightarrow\quad T_r\subseteq D.
  \]
  This is the conjectured threshold.
- Without any host restriction,
  \[
  |A(D)|>(3r-2)|V(D)|
  \quad\Longrightarrow\quad T_r\subseteq D.
  \]

Both statements also hold for the reversed orientation.

## 6. Sharpness and the remaining gap

For any fixed tree \(T\) of order \(k\), disjoint unions of bidirected copies of \(K_{k-1}\) have
\[
|A(D)|=(k-2)|V(D)|
\]
and contain no copy of \(T\), because every connected component has only \(k-1\) vertices. Thus the coefficient in the unrestricted conjecture is necessary even for each individual target tree. In particular, the bound above is asymptotically sharp when \(\min\{s,t\}=o(k)\).

The exact coefficient is also necessary uniformly over all target trees even within bipartite hosts: the bidirected \(K_{k-2,k-2}\) has arc density \(k-2\) and contains no out-star of order \(k\).

The unresolved issue is precisely the projection collision. The split-graph argument always produces a role-injective homomorphic image at the conjectured density, but it need not produce an injective image in \(D\). For example, a bidirected triangle has a split graph of minimum degree \(2\), containing a role-correct four-vertex antidirected path, while the original digraph has only three vertices. This example is at equality, not above the conjectured threshold, so it is **not** a counterexample.

Theorem 1 excludes collisions by forbidding their short odd-cycle witnesses. Theorem 2 instead pays additional density to avoid used original vertices directly. Neither argument removes that additional assumption or density cost in general. No proof or counterexample to the unrestricted conjecture is obtained here.