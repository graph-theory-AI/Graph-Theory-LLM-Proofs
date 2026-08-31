```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full characterization is not obtained, but there are exact decomposition, high-attachment, sparse-case, and polynomial-recognition results for the three exceptional lengths.",
  "would_publish": false,
  "caveats": "Components attaching to a hole through zero, one, or two consecutive rim vertices remain unclassified, and the prime 4-holed case is still broad."
}
```

# 1. Statement of the partial results

All graphs below are finite and simple. A graph with no holes is regarded as \(\ell\)-holed vacuously.

I do not obtain the requested complete description. I prove the following partial structural results.

1. **The class of \(4\)-holed graphs is closed under arbitrary substitution**, and in fact a substitution is \(4\)-holed if and only if its quotient and all substituted graphs are \(4\)-holed. This helps explain why the case \(\ell=4\) is much broader than the cases treated for large \(\ell\).

2. For \(\ell\in\{5,6\}\), I give a **complete description relative to a fixed \(\ell\)-hole \(C\)** under the hypothesis that every vertex outside \(C\) has at least three neighbors in \(C\). The resulting graphs are aligned cyclic arrangements of cliques, together with a universal clique.

3. For bipartite graphs having one side of maximum degree at most two, I give exact descriptions for all three values \(\ell=4,5,6\).

4. Recognition of \(\ell\)-holed graphs is polynomial for each fixed \(\ell\), with a direct self-contained algorithm running in
\[
O\bigl(n^\ell(n+m)\bigr).
\]

The unresolved part is made precise in Section 8.

---

# 2. Basic decomposition facts

## 2.1 Clique cutsets and universal vertices

Let \(S\) be a clique cutset of \(G\), and let \(D_1,\dots,D_t\) be the components of \(G-S\). Then
\[
G\text{ is }\ell\text{-holed}
\quad\Longleftrightarrow\quad
G[S\cup D_i]\text{ is }\ell\text{-holed for every }i.
\]

Indeed, a hole cannot meet two components of \(G-S\). A hole contains at most two vertices of the clique \(S\), and if it contains two then they must be consecutive. Removing one vertex, or two consecutive vertices, from a cycle leaves a connected path, which must lie in a single component of \(G-S\).

Similarly, if \(u\) is universal, then no hole contains \(u\), and hence
\[
G\text{ is }\ell\text{-holed}
\quad\Longleftrightarrow\quad
G-u\text{ is }\ell\text{-holed}.
\]

Thus clique-cutset decomposition and deletion of universal vertices are valid for all three exceptional lengths.

## 2.2 Holes and modules

Recall that \(M\subseteq V(G)\) is a module if every vertex outside \(M\) is either complete or anticomplete to \(M\).

### Lemma 2.1
Let \(M\) be a module and let \(Q\) be a hole not contained in \(M\). Then either

- \(|V(Q)\cap M|\leq 1\), or
- \(Q\) is a \(4\)-hole and \(V(Q)\cap M\) consists of two nonadjacent vertices.

#### Proof
No two vertices of \(M\cap V(Q)\) can be consecutive on \(Q\). Otherwise, let \(p\notin M\) precede a maximal nonempty segment of \(Q\cap M\). Since \(p\) has a neighbor in \(M\), it is complete to \(M\), and hence is adjacent to the second vertex of the segment, giving a chord.

Suppose now that \(u,v\in M\cap V(Q)\) are distinct. Let \(a,b\) be the two neighbors of \(u\) on \(Q\). Both are complete to \(M\), so both are adjacent to \(v\). Since \(Q\) is induced, \(a,b\) must also be the two cycle-neighbors of \(v\). It follows that
\[
Q=a-u-b-v-a
\]
is a \(4\)-hole. Moreover \(uv\notin E(G)\), since \(u,v\) are nonconsecutive on \(Q\). ∎

For \(\ell=5,6\), this gives a useful primeness reduction.

### Corollary 2.2
Let \(G\) be connected and \(C_4\)-free. If \(G\) has neither a clique cutset nor a universal vertex, then every proper module of \(G\) is a clique.

#### Proof
Let \(M\) be a proper nonclique module, and put
\[
A=N(M)\setminus M,\qquad
R=V(G)\setminus(M\cup A).
\]
Choose nonadjacent \(x,y\in M\). If \(A\) contained nonadjacent \(a,b\), then
\[
x-a-y-b-x
\]
would be an induced \(C_4\). Thus \(A\) is a clique.

If \(R\neq\varnothing\), then \(A\) is a clique cutset separating \(M\) from \(R\). If \(R=\varnothing\), every vertex of \(A\) is universal. Both alternatives contradict the hypotheses. ∎

Since \(5\)- and \(6\)-holed graphs are \(C_4\)-free, their clique-cutset atoms with no universal vertex are prime after contracting true-twin cliques.

---

# 3. The \(4\)-holed case and arbitrary substitution

Let \(F\) be a graph, and for every \(v\in V(F)\) let \(H_v\) be a nonempty graph. The substitution
\[
F[H_v:v\in V(F)]
\]
is obtained by replacing \(v\) with \(H_v\), making \(H_u\) complete to \(H_v\) when \(uv\in E(F)\), and anticomplete otherwise.

### Theorem 3.1
The substitution \(F[H_v:v\in V(F)]\) is \(4\)-holed if and only if \(F\) and every \(H_v\) are \(4\)-holed.

#### Proof
Necessity is immediate: every \(H_v\) is induced, and choosing one representative from each bag gives an induced copy of \(F\).

For sufficiency, let \(Q\) be a hole in the substitution. Each bag \(V(H_v)\) is a module. By Lemma 2.1, if \(Q\) uses more than one vertex of some bag, then \(Q\) is a \(4\)-hole.

Otherwise, \(Q\) uses at most one vertex from each bag. Projecting its vertices to \(F\) gives a hole of the same length in \(F\), and hence that length is four. ∎

This closure is substantially stronger than clique blowup closure. For example, every complete multipartite graph is \(4\)-holed: substitute independent sets into a complete graph.

Thus modular decomposition reduces the \(4\)-holed problem to prime \(4\)-holed graphs, but does not itself describe those prime graphs. In standard terminology, \(4\)-holed graphs are precisely graphs of chordality at most four, so this case already contains the broad class of chordal bipartite graphs and their nonbipartite analogues.

---

# 4. Attachments to a hole

Let
\[
C=c_0-c_1-\cdots-c_{\ell-1}-c_0
\]
be a hole, with indices modulo \(\ell\), and let \(x\notin V(C)\).

### Lemma 4.1
Suppose \(G\) is \(\ell\)-holed.

1. If \(\ell=4\), there is no restriction on a set \(N_C(x)\) of size at least two.

2. If \(\ell\in\{5,6\}\) and \(|N_C(x)|\geq2\), then exactly one of the following holds:
   - \(N_C(x)\) consists of two consecutive vertices of \(C\);
   - \(N_C(x)\) consists of three consecutive vertices of \(C\);
   - \(x\) is complete to \(C\).

#### Proof
List the neighbors of \(x\) cyclically as \(a_1,\dots,a_r\), and let \(d_i\) be the number of edges in the \(a_i\)-to-\(a_{i+1}\) sector of \(C\) containing no other neighbor of \(x\).

First suppose \(r\geq3\). If \(d_i\geq2\), the complementary sector contains at least two edges, so \(a_i,a_{i+1}\) are nonadjacent. Consequently the sector together with \(x\) is an induced cycle of length \(d_i+2\), and therefore
\[
d_i+2=\ell.
\]
Thus every gap has length \(1\) or \(\ell-2\).

For \(\ell=5,6\), either all gaps have length one, giving \(r=\ell\), or exactly one gap has length \(\ell-2\) and the other two have length one, giving three consecutive neighbors.

Now suppose \(r=2\). If the two neighbors are adjacent, the only induced cycle through \(x\) in \(G[V(C)\cup\{x\}]\) is a triangle; the cycle using the other sector has the rim edge as a chord. If they are nonadjacent, both sectors together with \(x\) are holes. If their lengths are \(d\) and \(\ell-d\), then
\[
d+2=\ell,\qquad \ell-d+2=\ell.
\]
Hence \(d=2\) and \(\ell=4\). This proves the assertions. ∎

The legal two-consecutive-neighbor case is an important low-length phenomenon. For example, \(C_\ell\) plus a vertex adjacent precisely to the ends of one rim edge is still \(\ell\)-holed for \(\ell=5,6\).

---

# 5. Complete high-attachment characterization for \(\ell=5,6\)

We now characterize the case in which every vertex outside a fixed hole has at least three neighbors on the hole.

For disjoint cliques \(A,B\), say that their cross graph is a **chain graph** if it has no induced \(2K_2\): there do not exist \(a,a'\in A\) and \(b,b'\in B\) such that
\[
ab,a'b'\in E(G),\qquad ab',a'b\notin E(G).
\]

### Theorem 5.1
Let \(\ell\in\{5,6\}\), and let \(C=c_0\cdots c_{\ell-1}c_0\) be a hole of \(G\). Suppose every vertex of \(G-C\) has at least three neighbors in \(C\).

Then \(G\) is \(\ell\)-holed if and only if \(V(G)\) has a partition
\[
U,A_0,\dots,A_{\ell-1},
\qquad c_i\in A_i,
\]
satisfying the following conditions, with indices modulo \(\ell\).

1. \(U\) is a clique complete to \(V(G)\setminus U\).

2. Every \(A_i\) is a clique.

3. \(A_i\) is anticomplete to \(A_j\) whenever \(j\notin\{i-1,i,i+1\}\).

4. The distinguished vertex \(c_i\) is adjacent to every other vertex in
   \[
   A_{i-1}\cup A_i\cup A_{i+1}.
   \]

5. For every \(i\), the cross graph between \(A_i\) and \(A_{i+1}\) is a chain graph.

6. There do not exist
   \[
   x,y\in A_i,\quad p\in A_{i-1},\quad q\in A_{i+1}
   \]
   such that
   \[
   px,yq\in E(G),\qquad py,xq\notin E(G).
   \tag{A}
   \]
   In words, the inclusion orders of the neighborhoods of vertices of \(A_i\) into the two neighboring bags cannot run in opposite directions.

#### Proof: necessity

By Lemma 4.1, every vertex outside \(C\) is either complete to \(C\), or has neighborhood
\[
\{c_{i-1},c_i,c_{i+1}\}
\]
for a unique \(i\). Define
\[
U=\{u\notin C:N_C(u)=V(C)\}
\]
and
\[
A_i=\{c_i\}\cup
\{x\notin C:N_C(x)=\{c_{i-1},c_i,c_{i+1}\}\}.
\]

These sets partition \(V(G)\).

If \(x,y\in A_i\setminus\{c_i\}\) were nonadjacent, then
\[
x-c_{i-1}-y-c_{i+1}-x
\]
would be an induced \(C_4\). Hence every \(A_i\) is a clique.

Let \(x\in A_i\setminus\{c_i\}\). Replacing \(c_i\) by \(x\) in \(C\) gives another \(\ell\)-hole \(C_x\). If \(y\in A_j\setminus\{c_j\}\), where \(i,j\) are nonconsecutive, then \(y\) has three consecutive neighbors on \(C_x\), and an edge \(xy\) would give it four neighbors on \(C_x\). Four neighbors are not allowed by Lemma 4.1 for either \(\ell=5\) or \(\ell=6\). Thus nonconsecutive bags are anticomplete.

Now let \(u\in U\). If \(ux\notin E(G)\) for some \(x\in A_i\setminus\{c_i\}\), then \(u\) would have exactly \(\ell-1\) neighbors on \(C_x\), again contradicting Lemma 4.1. Thus \(U\) is complete to every \(A_i\). If \(u,v\in U\) were nonadjacent, then \(u,v\), together with two nonadjacent vertices of \(C\), would induce a \(C_4\). Therefore \(U\) is a clique.

Condition 5 follows from the absence of \(C_4\)'s. Indeed, a \(2K_2\) in the cross graph between the two cliques \(A_i,A_{i+1}\), together with the clique edges inside the two bags, is an induced \(C_4\).

Finally, suppose (A) holds. Then
\[
p-x-y-q-c_{i+2}-c_{i+3}-\cdots-c_{i-2}-p
\]
is an induced cycle. It has \(\ell+1\) vertices. The only possible chords near \(A_i\) are precisely the two nonedges specified in (A), and all other possible chords are excluded by anticompleteness of nonconsecutive bags. This contradicts that \(G\) is \(\ell\)-holed.

#### Proof: sufficiency

Let \(Q\) be a hole. Since every vertex of \(U\) is universal, \(Q\cap U=\varnothing\).

A hole can use at most two vertices of a clique \(A_i\), and if it uses two, they must be consecutive on the hole. Suppose \(x,y\in A_i\) occur consecutively, with predecessor \(p\) and successor \(q\).

If \(p,q\) belong to the same neighboring bag, say \(A_{i-1}\), then either \(Q\) has length four, in which case its four vertices form a forbidden \(2K_2\) in the cross graph between \(A_i\) and \(A_{i-1}\), or \(pq\) is a chord of \(Q\).

Thus \(p,q\) lie on opposite sides, say
\[
p\in A_{i-1},\qquad q\in A_{i+1}.
\]
Since \(Q\) is induced,
\[
px,yq\in E(G),\qquad py,xq\notin E(G),
\]
contrary to condition 6. Therefore \(Q\) contains at most one vertex from each \(A_i\).

Projecting the vertices of \(Q\) to their bag indices now gives a simple closed walk in the cycle \(C_\ell\), with distinct indices. Such a walk must traverse the whole cycle once. Hence
\[
|V(Q)|=\ell.
\]
Thus every hole has length \(\ell\). ∎

This theorem includes ordinary clique blowups of \(C_\ell\), but allows some edges between consecutive bags to be absent. The chain and alignment conditions are exactly what prevents such missing edges from creating \(4\)-holes or \((\ell+1)\)-holes.

---

# 6. A complementary sparse special case

Let \(B=(X,Y;E)\) be bipartite and suppose every \(y\in Y\) has degree at most two. Construct a loopless multigraph \(M\) on \(X\) by adding, for each degree-two vertex \(y\) with
\[
N_B(y)=\{x,x'\},
\]
one edge \(xx'\). Vertices of \(Y\) of degree zero or one are ignored.

Every cycle of \(B\) is induced: a vertex \(y\) on such a cycle already uses both of its possible neighbors as its two cycle-neighbors, so it cannot be incident with a chord. Moreover, cycles of \(B\) correspond to cycles of \(M\), with lengths doubled; a pair of parallel edges in \(M\) corresponds to a \(C_4\) in \(B\).

### Proposition 6.1
Under the preceding hypotheses:

1. \(B\) is \(4\)-holed if and only if the underlying simple graph of \(M\) is a forest. Parallel classes are allowed.

2. \(B\) is \(5\)-holed if and only if \(M\) is acyclic as a multigraph; equivalently, its underlying simple graph is a forest and it has no parallel edges.

3. \(B\) is \(6\)-holed if and only if \(M\) is simple and every block of \(M\) is either \(K_2\) or \(K_3\).

#### Proof
For (1), all cycles in \(B\) must have length four, so all cycles in \(M\) must be multigraph \(2\)-cycles. This is equivalent to the simple support of \(M\) being a forest.

For (2), a bipartite graph has no odd cycle. Since every cycle of \(B\) is induced, a \(5\)-holed \(B\) must be acyclic.

For (3), \(C_4\)'s are forbidden, so \(M\) must be simple. Every cycle in \(M\) must then have length three. A simple graph in which every cycle is a triangle has every nontrivial block equal to \(K_2\) or \(K_3\): if a \(2\)-connected block properly contained a triangle together with additional vertices, \(2\)-connectivity would give an external path between two vertices of the triangle, and combining that path with the two triangle arcs would produce a cycle longer than three. The converse is immediate. ∎

Related elementary consequences are:

- every triangle-free \(4\)-holed graph is bipartite and chordal bipartite;
- every bipartite \(5\)-holed graph is a forest;
- every triangle-free \(6\)-holed graph is bipartite, \(C_4\)-free, and has no induced even cycle of length at least eight.

For the first and third assertions, a shortest odd cycle in a triangle-free graph is an odd hole and hence cannot have even prescribed length.

---

# 7. Direct polynomial recognition

Although this does not provide the requested structure, recognition has a simple polynomial algorithm for each fixed \(\ell\).

### Lemma 7.1
For every fixed \(k\geq4\), one can decide in
\[
O\bigl(n^{k-1}(n+m)\bigr)
\]
time whether \(G\) contains a hole of length at least \(k\), and output such a hole if one exists.

#### Proof
Enumerate every ordered induced path
\[
P=v_0-v_1-\cdots-v_{k-2}
\]
on \(k-1\) vertices. Let
\[
I=\{v_1,\dots,v_{k-3}\},
\]
and define
\[
W_P=\{v_0,v_{k-2}\}
 \cup
 \{z\in V(G)\setminus V(P):N(z)\cap I=\varnothing\}.
\]

Test by breadth-first search whether \(v_0\) and \(v_{k-2}\) are connected in \(G[W_P]\). If they are, let \(Q\) be a shortest path between them. Since \(P\) is induced and has length at least two, its endpoints are nonadjacent, so \(Q\) has length at least two. The union \(P\cup Q\) is an induced cycle:

- \(P\) and \(Q\) are individually induced;
- the interior of \(Q\) is anticomplete to the interior of \(P\) by the definition of \(W_P\);
- shortestness of \(Q\) excludes chords from its interior to either endpoint.

Its length is at least
\[
(k-2)+2=k.
\]

Conversely, if \(C\) is a hole of length at least \(k\), take \(k-1\) consecutive vertices of \(C\) as \(P\). The complementary arc lies in \(G[W_P]\), so the corresponding breadth-first search succeeds.

There are \(O(n^{k-1})\) ordered tuples, and each search takes \(O(n+m)\) time. ∎

To recognize \(\ell\)-holed graphs:

1. enumerate and reject induced cycles of lengths \(4,\dots,\ell-1\);
2. apply Lemma 7.1 with \(k=\ell+1\).

Thus the running time is
\[
O\bigl(n^\ell(n+m)\bigr).
\]
In particular:

- \(4\)-holed recognition rejects holes of length at least five;
- \(5\)-holed recognition rejects \(C_4\)'s and holes of length at least six;
- \(6\)-holed recognition rejects \(C_4,C_5\), and holes of length at least seven.

Chordal graphs are accepted, as required by the vacuous definition.

---

# 8. What remains unresolved

Theorem 5.1 completely handles a fixed \(5\)- or \(6\)-hole \(C\) when every external vertex has at least three neighbors on \(C\). Lemma 4.1 shows exactly what remains locally:

- vertices anticomplete to \(C\);
- vertices with exactly one neighbor on \(C\);
- vertices adjacent precisely to the ends of one edge of \(C\).

A single vertex of the last type is harmless: \(C_\ell\) plus a vertex adjacent only to \(c_i,c_{i+1}\) is still \(\ell\)-holed. Such a vertex is separated by the clique \(\{c_i,c_{i+1}\}\), but connected collections of low-attachment vertices can attach at several places around \(C\) and need not reduce to this elementary clique-cutset situation. Those collections are the missing part of a full characterization.

For \(\ell=4\), arbitrary substitution closure demonstrates a different obstruction: even after clique-cutset decomposition, modular composition is far less rigid than for \(5\)- and \(6\)-holed graphs. The prime \(4\)-holed factors are not characterized here.

Accordingly, the catalog problem remains open in full generality.