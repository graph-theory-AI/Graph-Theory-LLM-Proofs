```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Yes: an explicit construction from a biregular tree gives universal highly arc-transitive digraphs of every composite common indegree and outdegree.",
  "would_publish": false,
  "caveats": "The supplied catalog attributes the resolution to DeVos, Mohar, and Šámal; the proof below is self-contained, and no novelty is claimed."
}
```

## Statement

The supplied catalog records an affirmative resolution. Here is an explicit construction with a complete verification.

**Theorem.** For every pair of integers \(p,q\ge 3\), there exists an infinite, locally finite, highly arc-transitive digraph \(D_{p,q}\) whose alternating reachability relation is universal and whose indegree and outdegree are both
\[
(p-1)(q-1).
\]
In particular, \(D_{3,3}\) answers the question with indegree and outdegree \(4\).

## 1. Construction and local finiteness

Let \(T\) be an infinite bipartite tree with bipartition \(A\cup B\), in which every vertex of \(A\) has degree \(p\) and every vertex of \(B\) has degree \(q\). Such a tree is obtained by recursively attaching new neighbours to achieve the prescribed degrees.

The vertices of \(D=D_{p,q}\) are the edges of \(T\). Write these as
\[
(a,b),\qquad a\in A,\quad b\in B,\quad ab\in E(T).
\]
Define
\[
(a,b)\longrightarrow(a',b')
\]
if and only if
\[
ab'\in E(T),\qquad a'\ne a,\qquad b'\ne b.
\]
Thus an arc of \(D\) corresponds to a three-edge path
\[
b-a-b'-a'
\]
in \(T\), with its first and last edges serving as the two vertices of \(D\).

For a fixed vertex \((a,b)\), an outneighbour is obtained by choosing
\[
b'\in N_T(a)\setminus\{b\},
\qquad
a'\in N_T(b')\setminus\{a\}.
\]
There are exactly \((p-1)(q-1)\) choices, and distinct choices give distinct outneighbours.

Similarly, an inneighbour is obtained by choosing
\[
a'\in N_T(b)\setminus\{a\},
\qquad
b'\in N_T(a')\setminus\{b\},
\]
so
\[
d^+(D)=d^-(D)=(p-1)(q-1).
\]
Consequently, \(D\) is locally finite. It is infinite because \(T\) has infinitely many edges.

## 2. High arc transitivity

Every automorphism of \(T\) preserving \(A\) and \(B\) induces an automorphism of \(D\).

Let
\[
(e_0,e_1,\ldots,e_s),
\qquad e_i=(a_i,b_i),
\]
be a directed walk in \(D\). Its defining conditions give a walk in \(T\):
\[
b_0,a_0,b_1,a_1,\ldots,b_s,a_s. \tag{1}
\]
This tree walk has no immediate reversal. Indeed, the arc \(e_{i-1}\to e_i\) guarantees
\[
b_{i-1}\ne b_i
\quad\text{and}\quad
a_{i-1}\ne a_i.
\]
A nonbacktracking walk in a tree cannot repeat a vertex, so (1) is a simple path.

Conversely, every ordered path of length \(2s+1\) in \(T\) starting in \(B\) can be written in the form (1), and its alternate edges give a directed \(s\)-arc of \(D\). Thus directed \(s\)-arcs of \(D\) correspond exactly to these ordered tree paths. In particular, the construction introduces no directed cycles or backtracking directed walks.

Now any two ordered paths of the same length in \(T\), both starting in \(B\), are mapped to one another by a bipartition-preserving automorphism of \(T\). To see this explicitly, map their vertices in order. At corresponding path vertices, the numbers and types of neighbours outside the path agree. The components attached through those neighbours are isomorphic rooted biregular trees, so the path map extends over these components to an automorphism of all of \(T\).

The induced automorphism of \(D\) maps any prescribed \(s\)-arc to any other. This applies also to \(s=0\), when the corresponding tree paths are single edges. Therefore \(D\) is highly arc transitive.

## 3. Universal alternating reachability

We use a convenient reformulation of alternating walks.

For any digraph \(D\), form an undirected bipartite graph \(\mathcal B(D)\) with two copies
\[
\{x^+:x\in V(D)\},
\qquad
\{x^-:x\in V(D)\},
\]
of its vertex set, and put an edge \(x^+y^-\) whenever \(x\to y\) is an arc of \(D\).

A walk in \(\mathcal B(D)\) projects to an alternating walk in \(D\): at a \(+\)-vertex both incident arcs have that vertex as their tail, and at a \(-\)-vertex both have it as their head. Conversely, every alternating walk lifts in this way. Hence
\[
D\text{ is universal}
\quad\Longleftrightarrow\quad
\text{all edges of }\mathcal B(D)\text{ belong to one connected component}. \tag{2}
\]

We prove this connectivity for the constructed digraph.

### Complete bipartite pieces

For each tree edge \(g=ab\), with \(a\in A\) and \(b\in B\), define subsets of \(V(D)\):
\[
L_g=\{(a,\beta):\beta\in N_T(a)\setminus\{b\}\},
\]
\[
R_g=\{(\alpha,b):\alpha\in N_T(b)\setminus\{a\}\}.
\]
Every vertex of \(L_g\) has an arc to every vertex of \(R_g\). Thus \(\mathcal B(D)\) contains a complete bipartite subgraph
\[
C_g=K_{L_g^+,R_g^-}\cong K_{p-1,q-1}.
\]
In particular, \(C_g\) is connected.

Moreover, every edge of \(\mathcal B(D)\) belongs to exactly one such piece. Indeed, the arc
\[
(a,b)\to(a',b')
\]
belongs to the piece indexed by its unique middle tree edge \(ab'\).

### Pieces indexed by adjacent tree edges intersect

Suppose first that two distinct tree edges share their \(A\)-endpoint:
\[
g=ab,\qquad h=ab'.
\]
Since \(p\ge3\), choose a third neighbour
\[
b''\in N_T(a)\setminus\{b,b'\}.
\]
Then
\[
(a,b'')\in L_g\cap L_h,
\]
so \(C_g\) and \(C_h\) share the vertex \((a,b'')^+\).

Similarly, if
\[
g=ab,\qquad h=a'b
\]
share their \(B\)-endpoint, then \(q\ge3\) supplies
\[
a''\in N_T(b)\setminus\{a,a'\}.
\]
Now
\[
(a'',b)\in R_g\cap R_h,
\]
so \(C_g\) and \(C_h\) share the vertex \((a'',b)^-\).

Because \(T\) is connected, any two of its edges can be joined by a finite sequence of consecutively incident edges. The corresponding connected subgraphs \(C_g\) therefore form a connected union.

Every edge of \(\mathcal B(D)\) lies in this union. Thus all its edges belong to one connected component, and (2) proves that \(D\) is universal.

## 4. Conclusion and scope

Taking \(p=q=3\) gives an explicit infinite digraph with
\[
d^+=d^-=4
\]
that is locally finite, highly arc transitive, and universal.

More generally, for any composite integer \(d=rs\), where \(r,s\ge2\), taking
\[
p=r+1,\qquad q=s+1
\]
gives common indegree and outdegree \(d\).

All required properties have been verified directly. No conjectural input or computational check is needed; this is a self-contained exposition of the affirmative answer, not a claim of a new resolution.