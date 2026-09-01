```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The converse remains open, but it holds against every host tournament having an ordering whose backedge graph has girth greater than |H|+1, forcing any asymptotic counterexample to have an almost spanning packing of short backedge cycles in every ordering.",
  "would_publish": false,
  "caveats": "The high-girth hypothesis concerns the host tournament and is unavailable for a general H-free tournament."
}
```

# 1. Statement and notation

For a tournament \(G\), write \(A\Rightarrow B\) when every arc between disjoint sets \(A,B\subseteq V(G)\) is directed from \(A\) to \(B\). Define
\[
p(G)=\max\{\min(|A|,|B|): A\Rightarrow B\}.
\]
Thus a fixed tournament \(H\) has the strong EH-property exactly when
\[
\inf\left\{\frac{p(G)}{|G|}:G\text{ is }H\text{-free},\ |G|>1\right\}>0.
\]

For a numbering \(v_1,\dots,v_n\) of a tournament \(G\), its backedge graph \(B\) is the graph on \(v_1,\dots,v_n\) in which
\[
v_iv_j\in E(B),\quad i<j,
\]
if and only if \(v_j\to v_i\) in \(G\).

Fix a numbering \(1,\dots,h\) of \(H\) whose backedge graph \(F\) is a forest. The known direction from the source paper is that existence of such a numbering is necessary. I do not prove the unrestricted converse.

# 2. A partite tree embedding lemma

The following elementary lemma is useful because a high-girth graph turns every copy of a small tree into an induced copy.

## Lemma 2.1

Let \(T\) be a tree on \(\{1,\dots,m\}\), and let \(Q\) be a graph with pairwise disjoint vertex sets
\[
V_1,\dots,V_m,\qquad |V_i|=N.
\]
Let \(s\ge 1\) satisfy
\[
N-(m-1)(s-1)\ge s.
\]
Suppose that for every \(ij\in E(T)\), there do not exist sets
\[
X\subseteq V_i,\qquad Y\subseteq V_j,\qquad |X|=|Y|=s
\]
with no edge of \(Q\) between \(X\) and \(Y\). Then \(Q\) contains a transversal copy of \(T\), with vertex \(i\) represented in \(V_i\).

### Proof

Root \(T\) arbitrarily. Define viable sets from the leaves upwards.

For a leaf \(i\), set \(S_i=V_i\). If \(i\) has children \(j_1,\dots,j_d\), define
\[
S_i=\left\{x\in V_i:
N_Q(x)\cap S_{j_\ell}\neq\varnothing\text{ for every }\ell\right\}.
\]

Inductively assume \(|S_j|\ge s\) for every child \(j\). For a fixed child \(j\), let
\[
D_{ij}=\{x\in V_i:N_Q(x)\cap S_j=\varnothing\}.
\]
If \(|D_{ij}|\ge s\), then an \(s\)-subset of \(D_{ij}\) and an \(s\)-subset of \(S_j\) are anticomplete, contrary to the hypothesis. Hence \(|D_{ij}|\le s-1\). Therefore
\[
|S_i|\ge N-d(s-1)\ge N-(m-1)(s-1)\ge s.
\]

Choose any vertex representing the root from its viable set. Recursively choose, for each child, a neighbor in the child's viable set. Distinct subtrees use distinct designated parts, so no collision occurs. This gives the desired transversal copy. \(\square\)

The copy supplied by this lemma need not be induced.

# 3. A restricted converse for high-girth host backedge graphs

## Theorem 3.1

Let \(H\) be a tournament on \(h\) vertices admitting a numbering whose backedge graph is a forest. Let \(G\) be a tournament with a numbering whose backedge graph \(B\) has girth greater than \(h+1\), with acyclic graphs regarded as having infinite girth. Then either \(G\) contains \(H\), or
\[
p(G)\ge \frac{|G|}{8(h+1)^2}.
\]

In particular, the conjectured converse holds on the subclass of host tournaments admitting such a high-girth backedge ordering.

### Proof

Let \(F\) be the forest backedge graph of the fixed numbering \(1,\dots,h\) of \(H\).

Construct a tree \(T\) containing \(F\) as an induced subgraph as follows. Add one new vertex \(z\). In every component \(C\) of \(F\), choose one vertex \(a_C\), and add the edge \(za_C\). The resulting graph \(T\) is a tree on
\[
m=h+1
\]
vertices, and \(T[\{1,\dots,h\}]=F\). Order the vertices of \(T\) as
\[
1,2,\dots,h,z.
\]

Let \(n=|G|\), and put
\[
N=\left\lfloor\frac{n}{m}\right\rfloor.
\]

If \(N<4m\), then \(n<4m^2\). Every tournament with at least two vertices has a singleton pure pair, and
\[
1>\frac{n}{8m^2},
\]
so the asserted bound holds.

Assume therefore that \(N\ge4m\), and set
\[
s=\left\lfloor\frac{N}{2m}\right\rfloor.
\]
Partition the first \(mN\) vertices of the given numbering of \(G\) into consecutive blocks
\[
V_1,\dots,V_m,
\qquad |V_i|=N.
\]
Thus every vertex of \(V_i\) precedes every vertex of \(V_j\) whenever \(i<j\).

Consider an edge \(ij\in E(T)\). If there are \(s\)-sets
\[
X\subseteq V_i,\qquad Y\subseteq V_j
\]
with no backedge-graph edge between them, then, after interchanging \(i,j\) if necessary so that \(i<j\), every tournament arc between \(X\) and \(Y\) is directed from \(X\) to \(Y\). Hence \(p(G)\ge s\).

Suppose no such anticomplete pair exists for any edge of \(T\). Since \(s\le N/(2m)\),
\[
N-(m-1)(s-1)>N-\frac{m-1}{2m}N>\frac N2\ge s.
\]
Lemma 2.1 gives a transversal copy of \(T\) in \(B\).

This copy is induced. Indeed, an extra edge between two nonadjacent vertices of the selected copy, together with their unique path in \(T\), would form a cycle of length at most \(m=h+1\), contrary to the girth assumption on \(B\).

Discard the selected vertex representing \(z\). The remaining \(h\) selected vertices occur in the prescribed order and induce exactly \(F\) in the backedge graph. Consequently, their tournament orientations are exactly those of \(H\). Thus \(G\) contains \(H\).

We have proved that an \(H\)-free \(G\) must have \(p(G)\ge s\). Finally, since \(N\ge4m\),
\[
s\ge\frac{N}{4m}\ge\frac{n}{8m^2}
  =\frac{n}{8(h+1)^2}.
\]
This proves the theorem. \(\square\)

## Corollary 3.2

Let \(G_n\) be an \(H\)-free sequence. If each \(G_n\) has a numbering whose backedge graph has girth tending to infinity, then
\[
p(G_n)\ge \frac{|G_n|}{8(h+1)^2}
\]
for all sufficiently large \(n\).

Thus the usual sparse, high-girth backedge-graph mechanism used to construct obstructions when no forest ordering exists cannot produce a counterexample when \(H\) has a forest ordering.

# 4. Structure forced on any hypothetical counterexample

The previous theorem gives a reasonably strong necessary condition for a counterexample sequence.

## Corollary 4.1: almost spanning short-cycle packings

Let
\[
c_H=\frac1{8(h+1)^2}.
\]
Let \(G\) be an \(H\)-free tournament, and fix any numbering of \(G\), with backedge graph \(B\). Then \(B\) has a family of vertex-disjoint cycles, each of length at most \(h+1\), covering all but at most
\[
\max\left(1,\frac{p(G)}{c_H}\right)
\]
vertices.

### Proof

Take a maximal family of vertex-disjoint cycles of length at most \(h+1\), and let \(R\) be the uncovered vertices. By maximality, \(B[R]\) has girth greater than \(h+1\). The tournament \(G[R]\) remains \(H\)-free. If \(|R|>1\), Theorem 3.1 gives
\[
p(G)\ge p(G[R])\ge c_H|R|.
\]
The assertion follows. \(\square\)

Consequently, if the conjecture is false and \(G_n\) is an \(H\)-free sequence with
\[
p(G_n)=o(|G_n|),
\]
then for **every numbering** of \(G_n\), its backedge graph has a packing of cycles of length at most \(h+1\) covering all but \(o(|G_n|)\) vertices.

This isolates the unresolved regime: a counterexample cannot merely have occasional short cycles; short cycles must occupy asymptotically the whole backedge graph in every ordering.

# 5. Universal-source and universal-sink reduction

There is also a simple target-side closure property.

## Lemma 5.1

If a tournament \(K\) has the strong EH-property, then the tournament obtained by adjoining a universal source to \(K\) has the strong EH-property. The same holds for adjoining a universal sink.

### Proof

Let \(H\) be obtained from \(K\) by adding a source \(s\), and let \(c_K>0\) be a strong EH constant for \(K\).

Let \(G\) be \(H\)-free on \(n\ge4\) vertices. Choose a vertex \(v\) of maximum outdegree. Then
\[
|N^+(v)|\ge\frac{n-1}{2}\ge\frac n3,
\]
and \(|N^+(v)|\ge2\). Moreover, \(G[N^+(v)]\) is \(K\)-free: a copy of \(K\) there, together with \(v\), would induce \(H\). Hence \(G[N^+(v)]\) has a pure pair with both sides of size at least
\[
c_K|N^+(v)|\ge\frac{c_K}{3}n.
\]
For \(n\le3\), a singleton pair suffices. Thus \(\min(c_K/3,1/3)\) is a strong EH constant for \(H\). The sink case is obtained using a vertex of maximum indegree. \(\square\)

## Consequence for a minimal counterexample

If the conjecture is false and \(H\) is a minimum-order forest-orderable counterexample, then \(H\) has neither a universal source nor a universal sink. In particular, in every forest ordering of \(H\),

- the first vertex is incident with a backedge, and
- the last vertex is incident with a backedge.

Indeed, an isolated first vertex in the backedge forest is a source, while an isolated last vertex is a sink.

This does not allow arbitrary forest leaves to be stripped: an internal leaf of the backedge forest generally has many in- and out-neighbors on both sides of its position.

# 6. A general mixing condition in a counterexample

The following elementary fact is sometimes useful when attempting a leaf-by-leaf embedding.

## Lemma 6.1

Suppose \(G\) has no pure pair whose two sides have size \(q\). If \(X,Y\subseteq V(G)\) are disjoint and
\[
|X|,|Y|\ge2q,
\]
then the arcs from \(X\) to \(Y\) contain a matching of size \(q\), and the arcs from \(Y\) to \(X\) also contain a matching of size \(q\).

### Proof

Form the bipartite graph on \(X,Y\) whose edges are arcs directed from \(X\) to \(Y\). If its maximum matching has size at most \(q-1\), König's theorem gives a vertex cover of size at most \(q-1\). Removing this cover leaves \(q\)-subsets \(X'\subseteq X\), \(Y'\subseteq Y\) with no arc from \(X'\) to \(Y'\). Hence \(Y'\Rightarrow X'\), a contradiction. Reverse the directions for the second assertion. \(\square\)

Thus an asymptotic counterexample is robustly mixed in both directions at every fixed linear scale. The difficulty is that such matching information does not control all the additional arcs required for an induced forest pattern.

# 7. Why the obvious partite forest argument fails

One might hope for the following false strengthening of Lemma 2.1:

> If every pair of designated parts is mixed on all linear-sized subsets, then every fixed labeled tree occurs as an induced transversal.

Already the labeled path \(P_3\) disproves this.

## Proposition 7.1

For every fixed \(\varepsilon>0\) and all sufficiently large \(N\), there is a tripartite graph \(Q\) with parts \(A,B,C\), each of size \(N\), such that:

1. there is no induced transversal path \(a-b-c\) with \(a\in A,b\in B,c\in C\);
2. between every two distinct parts, every pair of subsets of size at least \(\varepsilon N\) contains both an edge and a nonedge.

### Construction and proof

Let
\[
p=\frac1{\sqrt N\log N}.
\]
Choose independently random bipartite graphs
\[
R\subseteq A\times B,\qquad S\subseteq B\times C
\]
with edge probability \(p\). Put \(Q[A,B]=R\) and \(Q[B,C]=S\). Define
\[
ac\in E(Q)\quad\Longleftrightarrow\quad
\text{there exists }b\in B\text{ with }ab\in R,\ bc\in S.
\]

Property 1 is deterministic: every \(A\)-\(B\)-\(C\) two-edge path has its \(A\)-\(C\) chord.

For \(A,B\), the probability that fixed \(\varepsilon N\)-sets are anticomplete is at most
\[
(1-p)^{\varepsilon^2N^2}
 \le \exp\left(-\frac{\varepsilon^2N^{3/2}}{\log N}\right).
\]
A union bound over at most \(4^N\) pairs of subsets shows that no such anticomplete rectangle exists with high probability. The same applies to \(B,C\).

For fixed \(X\subseteq A\), \(Z\subseteq C\), each of size \(\varepsilon N\), there is no \(Q\)-edge between \(X\) and \(Z\) only if every \(b\in B\) fails to have both a neighbor in \(X\) through \(R\) and a neighbor in \(Z\) through \(S\). For a fixed \(b\), this failure probability is at most
\[
2(1-p)^{\varepsilon N}
 \le 2\exp\left(-\frac{\varepsilon\sqrt N}{\log N}\right).
\]
Independence over \(b\in B\) and another \(4^N\) union bound show that there is no anticomplete \(\varepsilon N\times\varepsilon N\) rectangle between \(A,C\).

Finally, the maximum degrees in \(R\) and \(S\) are \(o(N)\) with high probability. Conditional on
\[
d_R(a)\le \frac{2\sqrt N}{\log N}
\]
for every \(a\in A\), a fixed \(a\) has \(Q\)-adjacency probability to a fixed \(c\in C\) at most
\[
p\,d_R(a)\le \frac{2}{\log^2 N}.
\]
Thus
\[
\Pr\bigl(d_{Q[A,C]}(a)\ge\varepsilon N\bigr)
 \le
 \left(\frac{2e}{\varepsilon\log^2N}\right)^{\varepsilon N}.
\]
A union bound over \(a\) shows that all \(A\)-\(C\) degrees are below \(\varepsilon N\), so no complete \(\varepsilon N\times\varepsilon N\) rectangle exists. The same conclusion for \(A,B\) and \(B,C\) follows from their \(o(N)\) maximum degrees.

Hence a graph satisfying both properties exists. \(\square\)

This is not a tournament counterexample: the construction only controls cross-part behavior and does not avoid all backedge patterns arising from all numberings of a tournament \(H\). It does show that pairwise mixing and large two-way matchings do not by themselves force an induced labeled tree. In Theorem 3.1, high girth is precisely what prevents the forced chords seen in this construction.

# 8. Remaining gap

The unrestricted conjecture would follow if one could exploit all the additional backedge patterns arising from different numberings of \(H\) to control these chords. The present argument does not do this.

For a general ordering of an \(H\)-free host tournament, its backedge graph may contain many triangles and other short cycles. Lemma 2.1 then only produces a non-induced tree; extra backedges change the resulting subtournament. Corollary 4.1 shows that any genuine counterexample must lie entirely in this short-cycle-rich regime, but it does not rule that regime out.

Therefore there is no complete proof or counterexample here. The main concrete progress is the high-girth restricted converse and the consequent near-perfect short-cycle-packing condition on every hypothetical counterexample sequence.