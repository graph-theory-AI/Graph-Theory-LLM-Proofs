```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An exponential lower bound is proved for connected triangle-free planar graphs admitting an embedding with at most two odd faces.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not proved; novelty of this special case has not been checked."
}
```

## 1. A proved special case

Write \(P_3(G)\) for the number of proper colorings with the labeled colors \(\{0,1,2\}\), and put
\[
\alpha=\log_{9/2}3<1.
\]

Here is the partial result.

**Theorem.** Let \(G\) be a connected simple triangle-free plane graph on \(n\) vertices. If exactly two faces have odd length, then
\[
\boxed{P_3(G)\ge 30\,2^{(n-5)/4}.}
\]
Face lengths count boundary edges with multiplicity.

Consequently, if \(G\) has at most two odd faces, then
\[
P_3(G)\ge 2^{n/4}.
\]
Thus the conjectured inequality holds for this subclass with \(c=2^{1/4}\), and in fact with an exponential rather than subexponential lower bound.

The proof below is self-contained apart from standard max-flow/min-cut and planar flow–coloring duality, whose relevant use is explained. I do not claim that this special case is new.

## 2. A directed counting lemma

For a directed graph \(D\) and an edge set \(Y\), define
\[
\partial_Y(v)=d_Y^+(v)-d_Y^-(v).
\]

**Lemma.** Suppose a directed multigraph \(D\) has vertices \(s,t\) satisfying
\[
d^+(s)=5,\quad d^-(s)=0,\qquad
d^-(t)=5,\quad d^+(t)=0,
\]
and each of its other \(N\) vertices has indegree and outdegree two. Then there are at least
\[
5\,2^{N/4}
\]
edge sets \(Y\subseteq E(D)\) satisfying
\[
\partial_Y(s)=1,\qquad \partial_Y(t)=-1,\qquad
\partial_Y(v)=0\quad(v\ne s,t).
\]

### Proof

At each ordinary vertex, choose one of the two bijections from its incoming edges to its outgoing edges. Call the resulting collection of choices a *transition system* \(\tau\).

A transition system decomposes the edges into five directed \(s\)-\(t\) trails and some number \(q(\tau)\) of directed circuits. Components may revisit vertices, but do not repeat edges.

Choose \(\tau\) uniformly from the \(2^N\) possibilities. Then:

* choose one of its five \(s\)-\(t\) trails uniformly;
* independently choose each circuit with probability \(1/2\).

Let \(Y\) be the union of the chosen components. It has the required divergence.

We use Shannon entropy in bits. The entropy of the entire random experiment is
\[
N+\log_2 5+\mathbb E q(\tau).
\]

For a resulting edge set \(Y\), let \(M(Y)\) be the number of ordinary vertices having exactly one incoming and one outgoing edge in \(Y\).

At such a vertex, the transition pairing compatible with \(Y\) is forced. At every other ordinary vertex, there are at most two compatible pairings. Moreover, once \(Y\) and \(\tau\) are specified, all the component-selection choices are determined. Hence the number of outcomes of the experiment producing a given \(Y\) is at most
\[
2^{N-M(Y)}.
\]
The entropy chain rule therefore gives
\[
H(Y)\ge
\log_2 5+\mathbb E q(\tau)+\mathbb E M(Y).
\tag{1}
\]

We claim that
\[
\mathbb E M(Y)\ge N/4.
\tag{2}
\]

Fix an ordinary vertex \(v\), and fix all transition choices except the choice at \(v\). Switching that choice has one of two effects.

1. **Splitting or merging a circuit component.**  
   In one transition system, the two incoming edges at \(v\) belong to the same component. In the other, they belong to different components, at least one of which is a circuit.

   In the first system, \(v\) cannot be counted by \(M(Y)\). In the second, exactly one of the two components is selected with probability \(1/2\): this holds both for two circuits and for a circuit together with a trail. Averaging over the two transition choices gives probability \(1/4\).

2. **Exchanging the tails of two \(s\)-\(t\) trails.**  
   In both transition systems, the incoming edges belong to two different \(s\)-\(t\) trails. Exactly one of these trails is selected with probability \(2/5\), which is greater than \(1/4\).

These cases exhaust the effect of switching the two transitions. Thus every ordinary vertex is counted by \(M(Y)\) with probability at least \(1/4\), proving (2).

By (1),
\[
H(Y)\ge \log_2 5+N/4.
\]
Since entropy is at most the logarithm of the support size, the number of possible \(Y\) is at least \(5\,2^{N/4}\). ∎

## 3. Passing to the planar dual

Let \(G\) satisfy the theorem, let \(m=|E(G)|\), and let \(f\) be its number of faces. Let \(D=G^*\) be its plane dual, allowing parallel edges and loops. Denote its two odd-degree vertices by \(s,t\).

### 3.1. Five edge-disjoint paths between the odd faces

Every nonempty edge cut of \(D\) corresponds to a nonempty even-degree edge set in \(G\): it is the boundary, modulo two, of a collection of faces. Such an edge set contains a cycle. Since \(G\) is simple and triangle-free, that cycle has length at least four.

Therefore every nontrivial edge cut of \(D\) has size at least four.

An edge cut separating \(s\) from \(t\) has odd size. Indeed, the sum of the degrees on the side containing \(s\), but not \(t\), is odd. Consequently every such cut has size at least five.

By the edge version of Menger’s theorem, \(D\) contains five edge-disjoint \(s\)-\(t\) paths. Orient all five from \(s\) to \(t\). Removing their edges leaves a graph in which every degree is even, so orient the remaining edges along Euler tours.

The resulting orientation \(D_0\) satisfies
\[
d^+_{D_0}(s)-d^-_{D_0}(s)=5,\qquad
d^+_{D_0}(t)-d^-_{D_0}(t)=-5,
\]
and every other vertex is balanced.

### 3.2. Splitting vertices into degree-four vertices

We next replace vertices by directed tree gadgets, retaining every original edge.

* A balanced vertex of degree \(2d\), where \(d\ge2\), can be replaced by a tree of \(d-1\) vertices, each with indegree and outdegree two.
* A vertex with indegree \(a\) and outdegree \(a+5\) can be replaced by one vertex with five outgoing edges and no incoming edges, together with \(a\) balanced degree-four vertices.
* The reverse construction applies at a vertex with indegree \(a+5\) and outdegree \(a\).

Here are explicit splitting operations. At a balanced vertex with \(d>2\), split off two incoming and one outgoing half-edge, and add an edge directed from the new vertex to the remaining vertex. The new vertex is balanced of degree four, and the remaining vertex has indegree and outdegree \(d-1\). Repeat.

At a vertex with imbalance \(+5\), split off one incoming and two outgoing half-edges, adding an edge from the remaining vertex to the new vertex. This removes one incoming edge and one net outgoing edge from the remaining vertex, preserving imbalance \(+5\). Repeat until it is a pure source. Reverse this operation at the sink.

The newly introduced edges form a tree within each replacement gadget. These operations also work with loops by treating their two ends as separate half-edges.

Call the expanded directed graph \(\widehat D\). It now satisfies the hypotheses of the counting lemma. Let \(N\) be its number of balanced degree-four vertices.

Write \(\ell_x\) for the degree of a dual vertex, equivalently the corresponding face length in \(G\). Then
\[
\begin{aligned}
N
&=\sum_{x\notin\{s,t\}}\left(\frac{\ell_x}{2}-1\right)
  +\frac{\ell_s-5}{2}+\frac{\ell_t-5}{2}\\
&=m-(f-2)-5\\
&=m-f-3\\
&=n-5,
\end{aligned}
\tag{3}
\]
where the last equality is Euler’s formula.

All quantities used in the splitting operations are nonnegative: the cut bound gives even dual degrees at least four and odd dual degrees at least five.

### 3.3. Producing many nowhere-zero \(3\)-flows

Apply the lemma to \(\widehat D\). For each of its at least
\[
5\,2^{N/4}
\]
unit-flow edge sets \(Y\), reverse precisely the edges in \(Y\).

Reversing an edge set subtracts twice its divergence. Thus the resulting orientation has divergence
\[
3\text{ at }s,\qquad -3\text{ at }t,\qquad 0\text{ elsewhere}.
\]
Assigning value \(1\) to every edge in this orientation therefore gives a nowhere-zero flow over \(\mathbb F_3\).

These flows remain distinct after contracting the new tree edges. To see this, suppose two flows agree on every original edge. Their difference is then an \(\mathbb F_3\)-circulation supported entirely on the new edges. Those edges form a forest, and a circulation supported on a forest is zero, by repeatedly removing leaves. Hence the two flows were identical.

Globally reversing each of the constructed flows gives another equally large, disjoint family: its divergence at the distinguished source in \(\widehat D\) is \(-3\), rather than \(3\). The same forest argument shows that the two families stay disjoint after contraction.

Thus \(D\) has at least
\[
10\,2^{N/4}
=
10\,2^{(n-5)/4}
\tag{4}
\]
nowhere-zero \(\mathbb F_3\)-flows.

### 3.4. Flows give colorings

For a connected plane graph,
\[
P_3(G)=3\,F_3(G^*),
\tag{5}
\]
where \(F_3\) counts nowhere-zero \(\mathbb F_3\)-flows.

Briefly, a proper coloring determines nonzero differences across primal edges. Under planar duality, these differences satisfy flow conservation. Conversely, dual flow conservation says that the corresponding primal edge differences sum to zero around every facial boundary, hence around every cycle. They can therefore be integrated to a vertex coloring, with exactly three choices for the color of a fixed root.

Combining (4) and (5) proves
\[
P_3(G)\ge30\,2^{(n-5)/4}.
\]
This also covers graphs with bridges: primal bridges correspond to dual loops, and the flow–coloring correspondence remains valid. ∎

For \(G=C_5\), the bound is sharp: \(P_3(C_5)=30\).

## 4. Consequence for the requested exponent

The number of odd faces is even, so “at most two” means zero or two.

If there are no odd faces, every cycle is even and \(G\) is bipartite. Fix a bipartition with a part of size at least \(n/2\). Color the other part with color \(0\), and independently color every vertex of the larger part with \(1\) or \(2\). This gives
\[
P_3(G)\ge2^{n/2}.
\]

If there are exactly two odd faces, the theorem gives
\[
P_3(G)\ge30\,2^{(n-5)/4}\ge2^{n/4}.
\]

Hence throughout this subclass,
\[
P_3(G)\ge2^{n/4}
\ge \left(2^{1/4}\right)^{n^\alpha}.
\]
The same exponential bound holds for disconnected graphs when each connected component admits such an embedding, by multiplying the component bounds.

## 5. What remains unresolved

The proof does **not** extend as written to unrestricted numbers of odd faces. Its crucial step is obtaining an orientation with divergence \(+5\) at one odd dual vertex, \(-5\) at the other, and zero everywhere else.

Even the most direct proposed generalization of that step is false. Take \(K_4\) and double each edge of a four-cycle. This is a planar, nonbipartite, \(5\)-regular multigraph. An orientation with divergence \(+5\) or \(-5\) at every vertex would make every vertex a pure source or pure sink, forcing the graph to be bipartite. Its cuts have size at least five, so its planar dual is nevertheless simple and triangle-free.

Thus the two-odd-face argument cannot simply be applied simultaneously to all odd faces. No bound of the form
\[
P_3(G)\ge c^{n^\alpha}
\]
for arbitrary triangle-free planar \(G\) has been established here. The result above is a fully proved special case, not a resolution of Conjecture 1.