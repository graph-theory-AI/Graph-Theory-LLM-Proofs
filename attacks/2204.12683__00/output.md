```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains unresolved, but the stronger 8/3 bound holds when the degree-three vertices induce a matching, and the 19/7 bound holds whenever the maximum average degree is at most 9/4.",
  "would_publish": false,
  "caveats": "The dense and cubic cases remain untreated, and the four specific forbidden graphs are not used; novelty of the partial lemmas has not been checked."
}
```

## 1. Statement and partial results

Let  
\[
V_3(G)=\{v\in V(G):d_G(v)=3\}.
\]
All graphs below are finite and simple.

I do not prove or disprove the catalog conjecture. I prove the following special cases, none of which require excluding \(F_{14}^{(1)},F_{14}^{(2)},F_{11},F_{22}\).

### Theorem 1

Let \(G\) be a subcubic triangle-free graph.

1. If \(V_3(G)\) is independent, then \(G\) has a \((5:2)\)-coloring. In particular,
   \[
   \chi_f(G)\le \frac52.
   \]

2. If \(\Delta(G[V_3(G)])\le 1\), equivalently the degree-three vertices induce a matching together with isolated vertices, then \(G\) has an \((8:3)\)-coloring. In particular,
   \[
   \chi_f(G)\le \frac83<\frac{19}{7}.
   \]

3. If
   \[
   \operatorname{mad}(G):=\max_{\varnothing\ne H\subseteq G}\frac{2|E(H)|}{|V(H)|}\le\frac94,
   \]
   then
   \[
   \chi_f(G)\le \frac{19}{7}.
   \]

Consequently, a vertex-minimal counterexample to the catalog conjecture must have a degree-three vertex with at least two degree-three neighbors, has no thread with three degree-two internal vertices, and has average degree strictly greater than \(9/4\).

The proof is constructive.

---

## 2. A path-extension lemma

An \((a:b)\)-coloring assigns to every vertex a \(b\)-subset of \([a]\), with adjacent vertices receiving disjoint subsets. Equivalently, it is a homomorphism to the Kneser graph \(KG(a,b)\).

For a finite graph and integers \(p,q>0\),
\[
\chi_f(G)\le \frac pq
\]
implies that \(G\) has a \((pt:qt)\)-coloring for some positive integer \(t\). This follows by clearing denominators in the fractional-coloring LP, adding empty color classes if necessary, and deleting surplus incidences.

### Lemma 2

Let \(a,b\) be integers satisfying
\[
\frac52\le \frac ab<3,
\]
and put
\[
r=3b-a,\qquad s=a-2b.
\]
For \(b\)-subsets \(A,B\subseteq[a]\):

1. There is a walk of length \(2\) in \(KG(a,b)\) from \(A\) to \(B\) if and only if
   \[
   |A\cap B|\ge r.
   \]

2. There is a walk of length \(3\) from \(A\) to \(B\) if and only if
   \[
   |A\cap B|\le s.
   \]

3. For every \(L\ge4\), there is a walk of length \(L\) from \(A\) to \(B\), without any condition on \(A\cap B\).

#### Proof

For a length-two walk \(A-X-B\), a \(b\)-set \(X\) must lie in the complement of \(A\cup B\). Such an \(X\) exists exactly when
\[
a-|A\cup B|=a-2b+|A\cap B|\ge b,
\]
equivalently \(|A\cap B|\ge3b-a=r\).

For a length-three walk \(A-X-Y-B\), choose \(X\) disjoint from \(A\). A suitable \(Y\), disjoint from both \(X\) and \(B\), exists exactly when
\[
|X\cap B|\ge r.
\]
Since \(X\cap B\subseteq B\setminus A\), this is possible exactly when
\[
b-|A\cap B|\ge r,
\]
or \(|A\cap B|\le b-r=a-2b=s\).

For length four, note that \(2r\le b\), because \(a/b\ge5/2\). Choose a \(b\)-set \(C\) such that
\[
|C\cap A|\ge r,\qquad |C\cap B|\ge r.
\]
Indeed, choose \(r\) elements from each of \(A\) and \(B\), whose union has size at most \(2r\le b\), and fill to a \(b\)-set. Part 1 supplies sets \(X,Y\) giving
\[
A-X-C-Y-B.
\]

For length five, choose disjoint \(r\)-sets \(S\subseteq A\) and \(T\subseteq B\). This is possible since \(2r\le b\). Extend them to disjoint \(b\)-sets \(C,D\); there is enough room because \(a\ge2b\). Part 1 then gives
\[
A-X-C-D-Y-B.
\]

Finally, inserting a two-edge backtrack into a walk increases its length by two. Thus the length-four and length-five constructions give every length \(L\ge4\). ∎

The relevant parameters are
\[
\begin{array}{c|c|c}
(a,b)&r&s\\ \hline
(5,2)&1&1\\
(8,3)&1&2\\
(19t,7t)&2t&5t.
\end{array}
\]

---

## 3. Degree-three vertices inducing an independent set

We first prove Theorem 1(1).

Vertices of degree at most one can be removed inductively: after coloring the smaller graph, a vertex with at most one already colored neighbor can be assigned a \(b\)-set from the complement of that neighbor's \(b\)-set, since \(a\ge2b\). Thus it suffices to consider a connected graph of minimum degree two.

If \(V_3(G)=\varnothing\), then \(G\) is a cycle. Triangle-freeness gives length at least four, and Lemma 2, with \((a,b)=(5,2)\), provides a closed walk of that length in \(KG(5,2)\).

Otherwise suppress every maximal path whose internal vertices have degree two. This produces a subcubic pseudograph \(K\) on \(V_3(G)\). Ignore loops when properly coloring \(K\); the resulting loopless underlying graph has maximum degree at most three and therefore has a proper coloring with colors \(1,2,3,4\).

In the palette \(\{0,1,2,3,4\}\), define
\[
S_i=\{0,i\}\qquad (i=1,2,3,4).
\]
Distinct \(S_i,S_j\) satisfy
\[
|S_i\cap S_j|=1.
\]

Assign \(S_i\) to a branch vertex receiving color \(i\). Since \(V_3(G)\) is independent, every nonclosed thread has length at least two.

- A thread of length two extends because its endpoint sets intersect in one element, and \(r=1\).
- A thread of length three extends because the endpoint intersection is one, and \(s=1\).
- Threads of length at least four extend by Lemma 2.
- A closed thread has length at least four: lengths two are impossible in a simple graph, and length three would be a triangle.

The threads have disjoint interiors, so all extensions can be made independently. This gives a \((5:2)\)-coloring.

---

## 4. Degree-three vertices inducing a matching

We now prove Theorem 1(2).

As above, it suffices to consider a connected graph of minimum degree two with \(V_3(G)\ne\varnothing\). Suppress degree-two paths to obtain a pseudograph on \(V_3(G)\). Its length-one threads are precisely the edges of \(G[V_3(G)]\), and by hypothesis these form a matching \(M\).

Contract every edge of \(M\). Each resulting part is either:

- a singleton degree-three vertex, or
- the two endpoints of an edge of \(M\).

Construct an auxiliary simple graph \(Q\) on these parts. Join two distinct parts when there is a thread of length two or three between vertices in those parts.

A singleton part has at most three incident thread ends. A matched part has four remaining incident thread ends after the matching edge is removed. Hence
\[
\Delta(Q)\le4.
\]
Therefore \(Q\) has a proper coloring with five colors.

We need five pairs of disjoint \(3\)-subsets of an \(8\)-element palette, with controlled intersections between different pairs. Let the palette be
\[
\Omega=\{0,1,2,3,4,5,6,7\},
\]
and define
\[
\begin{array}{c|c|c}
i&A_i&B_i\\ \hline
1&\{1,2,3\}&\{4,5,6\}\\
2&\{1,4,5\}&\{2,3,6\}\\
3&\{2,4,6\}&\{1,3,5\}\\
4&\{3,5,6\}&\{1,2,4\}\\
5&\{1,6,7\}&\{3,4,5\}.
\end{array}
\]
These sets satisfy

\[
A_i\cap B_i=\varnothing
\]
for every \(i\), and, whenever \(i\ne j\),
\[
1\le |X\cap Y|\le2
\quad
\text{for all }X\in\{A_i,B_i\},\;Y\in\{A_j,B_j\}.
\]
This is a direct check from the displayed table.

If a singleton part has color \(i\), assign its vertex \(A_i\). If a matched part \(uv\) has color \(i\), assign \(A_i\) to \(u\) and \(B_i\) to \(v\), in either orientation. Thus every direct edge in \(M\) has disjoint endpoint sets.

Consider any other thread \(P\), of length \(L\).

- If \(L=2\), its endpoint parts must be distinct. Indeed, a length-two closed thread is impossible in a simple graph, while a length-two thread joining the endpoints of a matching edge would form a triangle with that edge. The endpoint profile indices are therefore distinct, and their intersection has size one or two. Since \(r=1\) for \((8,3)\), Lemma 2 extends the coloring over \(P\).

- If \(L=3\) and the endpoint parts are distinct, their intersection has size at most two, so Lemma 2 applies since \(s=2\).

- If \(L=3\) joins the two vertices in one matched part, its endpoint sets are disjoint, again satisfying the condition \(|A\cap B|\le2\).

- A length-three closed thread would be a triangle and hence does not occur.

- Every thread of length at least four extends without conditions on its endpoint sets.

Again, thread interiors are disjoint. Hence these extensions together give an \((8:3)\)-coloring of \(G\). ∎

---

## 5. Consequences for a minimal counterexample

Let \(\mathcal F=\{F_{14}^{(1)},F_{14}^{(2)},F_{11},F_{22}\}\), and suppose \(G\) is a vertex-minimal \(\mathcal F\)-free counterexample to the catalog conjecture.

### 5.1 Connectivity

The graph \(G\) is connected. It also has no cutvertex.

Indeed, fractional colorings can be glued over a cutvertex. After replacing all colorings by \((19t:7t)\)-colorings with a common \(t\), a permutation of the palette can make the \(7t\)-set assigned to the shared cutvertex agree in two blocks.

The same argument shows that \(G\) cannot be decomposed along an adjacent two-vertex separator: two ordered pairs of disjoint \(7t\)-sets are related by a palette permutation, since the three regions have sizes \(7t,7t,5t\).

In particular, \(G\) has minimum degree at least two.

### 5.2 No long degree-two thread

There is no path
\[
v_0v_1\cdots v_L
\]
with \(L\ge4\) whose internal vertices all have degree two.

Otherwise delete \(v_1,\ldots,v_{L-1}\). The resulting graph is smaller and remains subcubic, triangle-free and \(\mathcal F\)-free, so it has a \((19t:7t)\)-coloring for some \(t\). Lemma 2 with \((a,b)=(19t,7t)\) extends this coloring across the deleted path, since \(L\ge4\).

Thus every maximal degree-two thread has at most two internal vertices.

### 5.3 The degree-three vertices contain an adjacent pair of edges

By Theorem 1(2),
\[
\Delta(G[V_3(G)])\ge2.
\]
Thus some degree-three vertex has at least two degree-three neighbors. In particular,
\[
e_{33}:=|E(G[V_3(G)])|\ge2.
\]

This is a genuine restriction: merely having isolated direct edges between degree-three vertices is already enough for an \((8:3)\)-coloring.

### 5.4 Density

Let \(n_i\) be the number of degree-\(i\) vertices. Since \(G\) has minimum degree two, only \(n_2,n_3\) occur.

Suppressing all degree-two threads gives a cubic pseudograph on \(n_3\) vertices, with \(3n_3/2\) edges. Exactly \(e_{33}\) of these edges have no degree-two internal vertices; every other thread has at most two such vertices. Hence
\[
n_2\le 2\left(\frac{3n_3}{2}-e_{33}\right)
   =3n_3-2e_{33}
   \le3n_3-4.
\]
Therefore
\[
\frac{2|E(G)|}{|V(G)|}
 =\frac{2n_2+3n_3}{n_2+n_3}
 =2+\frac{n_3}{n_2+n_3}
 >2+\frac14
 =\frac94.
\]

Thus every vertex-minimal counterexample has average degree strictly greater than \(9/4\).

---

## 6. Maximum-average-degree special case

Suppose now that \(G\) is any subcubic triangle-free graph with
\[
\operatorname{mad}(G)\le\frac94
\]
and \(\chi_f(G)>19/7\). Choose a vertex-minimal subgraph \(H\) with
\[
\chi_f(H)>19/7.
\]
The preceding minimal-counterexample argument did not use the forbidden graphs, so it gives
\[
\frac{2|E(H)|}{|V(H)|}>\frac94,
\]
contrary to
\[
\frac{2|E(H)|}{|V(H)|}\le\operatorname{mad}(G)\le\frac94.
\]
This proves Theorem 1(3).

For example, the usual Euler calculation gives
\[
\operatorname{mad}(G)<\frac{2g}{g-2}
\]
for planar graphs of girth at least \(g\). Hence every planar subcubic graph of girth at least \(18\) satisfies
\[
\chi_f(G)\le\frac{19}{7},
\]
without any exceptional-subgraph hypothesis.

---

## 7. Remaining gap

The argument leaves precisely the dense branching case. In particular, it gives no useful control over cubic triangle-free graphs, for which \(V_3(G)=V(G)\) and there are no degree-two threads. Avoiding the four named graphs does not force the structural hypotheses of Theorem 1.

A complete proof still has to establish, for every nonnegative vertex weighting \(w\), an independent set \(I\) satisfying
\[
w(I)\ge \frac7{19}w(V(G)),
\]
or equivalently construct an appropriate fractional coloring, in those dense cores while exploiting the exact structures of \(F_{14}^{(1)},F_{14}^{(2)},F_{11},F_{22}\). The present argument does not do so and provides no counterexample.