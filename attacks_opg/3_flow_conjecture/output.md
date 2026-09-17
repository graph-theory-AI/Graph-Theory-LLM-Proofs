```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every 4-edge-connected graph with at most ten odd-degree vertices has a nowhere-zero 3-flow, but the unrestricted conjecture is not resolved.",
  "would_publish": false,
  "caveats": "Uses the classical splitting-off theorem; no novelty or improvement over previously known special cases is claimed."
}
```

## A restricted theorem

I do not resolve Tutte’s conjecture. The following is a rigorous restricted result, with an analytic proof rather than an asserted computational check.

**Theorem.** Every finite 4-edge-connected graph with at most ten vertices of odd degree has a nowhere-zero \(3\)-flow.

Parallel edges are allowed. Loops can be deleted and subsequently assigned flow value \(1\), so they cause no difficulty.

The argument has three parts:

1. reduce a hypothetical counterexample to a simple \(5\)-regular graph without increasing the number of odd-degree vertices;
2. prove a suitable partition lemma for simple \(5\)-regular graphs on at most ten vertices;
3. use a prescribed-imbalance orientation criterion.

The only non-elementary graph-theoretic input is Mader’s established splitting-off theorem, stated below.

## 1. Orientations and cut inequalities

Write
\[
\delta_G(X)=E_G(X,V(G)\setminus X),\qquad
d_G(X)=|\delta_G(X)|,
\]
and let \(e_G(X)\) count edges with both ends in \(X\).

A **modulo \(3\) orientation** is an orientation satisfying
\[
d^+(v)-d^-(v)\equiv 0\pmod 3
\]
at every vertex.

### Modulo \(3\) orientations give integer \(3\)-flows

Here is a direct justification, so no group-flow lifting result needs to be assumed.

Suppose \(D\) is a modulo \(3\) orientation, and put
\[
b(v)=d_D^+(v)-d_D^-(v),\qquad q(v)=b(v)/3.
\]
On the directed edges of \(D\), the fractional assignment \(x(e)=1/3\) satisfies
\[
\operatorname{div}x(v)=q(v),\qquad 0\le x(e)\le 1.
\]
Integral network-flow feasibility therefore gives such an assignment with
\(x(e)\in\{0,1\}\). Define
\[
f(e)=1-3x(e)\in\{1,-2\}.
\]
Then
\[
\operatorname{div}f(v)=b(v)-3q(v)=0.
\]
Thus \(f\) is a nowhere-zero integer \(3\)-flow. Negative values can be made positive by reversing their edges.

Conversely, reducing an integer \(3\)-flow modulo \(3\), and reversing edges with residue \(-1\), gives a modulo \(3\) orientation.

### Prescribed-imbalance criterion

**Lemma 1.** Let \(G\) be loopless, and let \(b:V(G)\to\mathbb Z\) satisfy
\[
\sum_v b(v)=0,\qquad b(v)\equiv d_G(v)\pmod 2.
\]
There is an orientation with
\[
d^+(v)-d^-(v)=b(v)
\]
if and only if
\[
|b(X)|\le d_G(X)\qquad\text{for every }X\subseteq V(G), \tag{1}
\]
where \(b(X)=\sum_{v\in X}b(v)\).

**Proof.** Necessity follows by summing imbalances over \(X\).

For sufficiency, prescribe the outdegree
\[
p(v)=\frac{d_G(v)+b(v)}2.
\]
These are nonnegative integers, and \(\sum_vp(v)=|E(G)|\). Moreover,
\[
p(X)=e_G(X)+\frac{d_G(X)+b(X)}2\ge e_G(X). \tag{2}
\]
Assign each edge to one of its endpoints, with vertex \(v\) receiving exactly \(p(v)\) edges. The integral incidence-network flow criterion guarantees such an assignment from (2): for any set \(F\) of edge-nodes, its set \(X\) of incident vertices satisfies
\[
|F|\le e_G(X)\le p(X).
\]
Orient each edge away from its assigned endpoint. Its outdegrees are \(p(v)\), as required. \(\square\)

For a \(5\)-regular graph, we will use \(b(v)\in\{-3,3\}\), corresponding to outdegrees \(1\) and \(4\).

## 2. Two reductions

### 2.1 Splitting off to degree five

Splitting off \(vu,vw\) means deleting these two edges and adding \(uw\). The vertices \(u,w\) need not be distinct; any resulting loop may be discarded.

We use this standard form of **Mader’s splitting-off theorem**:

> If \(v\) has degree at least two, its degree is not three, and no bridge is incident with \(v\), then some pair of edges at \(v\) can be split off without decreasing the local edge-connectivity between any two vertices other than \(v\).

**Lemma 2.** Let \(G\) be a loopless 4-edge-connected graph with \(t>0\) odd-degree vertices. There is a loopless 4-edge-connected \(5\)-regular multigraph \(H\) on \(t\) vertices such that every modulo \(3\) orientation of \(H\) lifts to one of \(G\).

**Proof.** By the handshaking lemma, \(t\ge2\).

First completely split off every even-degree vertex \(v\), preserving local edge-connectivity between the other vertices. The splitting-off theorem can be applied repeatedly. Indeed, the other vertices remain pairwise 4-edge-connected. A bridge incident with \(v\) would consequently have to isolate \(v\), forcing its current loopless degree to be one. This is impossible while its degree is positive and even.

Delete \(v\) when its degree becomes zero. After all even-degree vertices have been removed, the remaining graph is 4-edge-connected, and its vertices are precisely the original odd-degree vertices. Their degrees remain odd and are therefore at least five.

Now, whenever a remaining vertex \(v\) has degree at least seven, split off an admissible pair at \(v\). Its degree after the operation is at least five. Cuts separating two vertices other than \(v\) retain size at least four; the only additional cut to consider isolates \(v\), and that cut has size at least five. Thus 4-edge-connectivity is maintained. Repeating produces the required \(5\)-regular multigraph \(H\).

To lift an orientation, replace an oriented split edge \(u\to w\) by the oriented path
\[
u\to v\to w.
\]
This preserves all old imbalances and contributes zero imbalance at \(v\). Deleted loops can first be restored arbitrarily. Reversing the entire sequence of operations proves the lifting assertion. \(\square\)

### 2.2 Contracting parallel edges

**Lemma 3.** Suppose \(u,v\) are joined by at least two parallel edges. Let \(G'\) be obtained by identifying \(u,v\) and deleting the resulting loops. Every modulo \(3\) orientation of \(G'\) extends to one of \(G\).

**Proof.** Restore \(u,v\), keeping the orientations of all external edges. Let their resulting external imbalances be \(a_u,a_v\). Conservation at the contracted vertex gives
\[
a_u+a_v\equiv0\pmod3.
\]

Orient the internal \(uv\)-edges so that their total contribution at \(u\) is \(-a_u\) modulo \(3\). This is always possible: the sums of two elements of \(\{1,-1\}\) cover all of \(\mathbb Z_3\). Any additional internal edges may be oriented first, after which the final two correct the residue.

Conservation then holds at both \(u\) and \(v\). \(\square\)

Contraction preserves 4-edge-connectivity, since each cut in the contracted graph corresponds to a cut of the original graph.

In particular, if \(G\) is \(5\)-regular and \(u,v\) have \(r\ge2\) parallel edges, their merged vertex has degree
\[
5+5-2r,
\]
which is even. Hence this contraction reduces the number of odd-degree vertices by exactly two.

## 3. Simple \(5\)-regular graphs on at most ten vertices

We next prove the finite-order ingredient completely.

### 3.1 A partition lemma

**Lemma 4.** Every simple \(5\)-regular graph \(H\) on at most ten vertices has a partition
\[
V(H)=A\sqcup B,\qquad |A|=|B|,
\]
such that
\[
e_H(A)=e_H(B)\le4. \tag{3}
\]

**Proof.** Its order is even and at least six, so it is \(6,8\), or \(10\). For any equal-size partition, regularity gives
\[
5|A|=2e_H(A)+d_H(A),\qquad
5|B|=2e_H(B)+d_H(A),
\]
and therefore \(e_H(A)=e_H(B)\).

- **Order six.** Here \(H=K_6\). Any partition into two triples has three edges in each part.

- **Order eight.** Choose \(A\) uniformly among the four-vertex subsets. Since \(H\) has twenty edges,
  \[
  \mathbb E[e_H(A)]
  =20\frac{\binom42}{\binom82}
  =\frac{30}{7}<5.
  \]
  Some choice therefore has \(e_H(A)\le4\).

- **Order ten.** Let \(F=\overline H\), which is simple and \(4\)-regular. We claim that \(F\) has five vertices spanning at least six edges. Their set \(A\) then satisfies
  \[
  e_H(A)=\binom52-e_F(A)\le4.
  \]

  To prove the claim, first suppose \(F\) contains a triangle \(C\). If a vertex outside \(C\) has at least two neighbors in \(C\), those four vertices span at least five edges. Some edge leaves this four-vertex set, since \(F\) is simple and \(4\)-regular. Adding its external endpoint gives five vertices spanning at least six edges.

  Otherwise the six edges leaving \(C\) have six distinct external endpoints, forming a set \(P\). If two vertices of \(P\) are adjacent, they together with \(C\) span at least six edges. If \(P\) is independent, however, each vertex of \(P\) has at most two possible neighbors: its unique neighbor in \(C\) and the sole vertex outside \(C\cup P\). This contradicts \(4\)-regularity.

  It remains to consider triangle-free \(F\). It must contain a \(4\)-cycle: otherwise breadth-first search from any vertex exposes
  \[
  1+4+4\cdot3=17
  \]
  distinct vertices. A \(4\)-cycle has eight edges to the other six vertices, so some external vertex has at least two neighbors on the cycle. These five vertices span at least six edges.

This covers all three orders. \(\square\)

### 3.2 Verifying every cut inequality

**Lemma 5.** Every simple \(5\)-regular graph on at most ten vertices has a nowhere-zero \(3\)-flow.

**Proof.** Choose \(A,B\) as in Lemma 4 and put
\[
b(v)=
\begin{cases}
3,&v\in A,\\
-3,&v\in B.
\end{cases}
\]
The sum and parity conditions in Lemma 1 hold. We verify every cut inequality.

Because \(b(V(H))=0\), it suffices to consider sets \(X\) with
\[
s=|X|\le |V(H)|/2\le5.
\]
Simplicity and \(5\)-regularity give
\[
d_H(X)=5s-2e_H(X)\ge s(6-s). \tag{4}
\]

The nonempty possibilities are as follows.

| Size and distribution of \(X\) | Lower bound on \(d_H(X)\) | Required bound \(|b(X)|\) |
|---|---:|---:|
| \(1\le s\le3\), arbitrary | \(s(6-s)\ge3s\) | at most \(3s\) |
| \(s=4\), all in one part | \(20-2\cdot4=12\) | \(12\) |
| \(s=4\), meeting both parts | \(8\), by (4) | at most \(6\) |
| \(s=5\), all in one part | \(25-2\cdot4=17\) | \(15\) |
| \(s=5\), distribution \(4+1\) | \(9\) | \(9\) |
| \(s=5\), distribution \(3+2\) | \(5\), by (4) | \(3\) |

For the \(4+1\) row, the four vertices in one part span at most four edges by (3), and the remaining vertex has at most four edges to them. Hence
\[
e_H(X)\le8,\qquad d_H(X)\ge25-16=9.
\]
All other improved bounds in the table follow directly from (3).

Thus \(|b(X)|\le d_H(X)\) for every \(X\). Lemma 1 supplies an orientation with imbalances \(\pm3\), hence a modulo \(3\) orientation and a nowhere-zero integer \(3\)-flow. \(\square\)

## 4. Proof of the restricted theorem

Suppose the theorem is false, and choose a counterexample \(G\) having the smallest possible number \(t\le10\) of odd-degree vertices.

If \(t=0\), an Eulerian orientation with value \(1\) on every edge is already a nowhere-zero flow. Thus \(t>0\).

Apply Lemma 2 to obtain a loopless 4-edge-connected \(5\)-regular multigraph \(H\) on \(t\) vertices. It cannot have a modulo \(3\) orientation, since such an orientation would lift to \(G\).

If \(H\) has parallel edges between \(u,v\), contract these vertices and delete the resulting loops. The contracted graph is 4-edge-connected and has exactly \(t-2\) odd-degree vertices. By minimality of \(t\), it has a nowhere-zero \(3\)-flow. The single-vertex case is trivial. Lemma 3 then extends a modulo \(3\) orientation back to \(H\), a contradiction.

Consequently \(H\) is simple. A simple \(5\)-regular graph has at least six vertices, and its order is even. Therefore
\[
t\in\{6,8,10\}.
\]
Lemma 5 gives a nowhere-zero \(3\)-flow in every one of these cases, again a contradiction. This proves the theorem. \(\square\)

## 5. What remains unresolved

The proved conclusion is
\[
\boxed{\text{Any counterexample to Tutte’s \(3\)-flow conjecture has at least twelve odd-degree vertices.}}
\]

The restricted argument is constructive: admissible splitting pairs and prescribed-imbalance orientations can be found using max-flow computations. The small-order portion above is proved analytically; no computational enumeration is being claimed.

The gap is substantive. For a general residual simple \(5\)-regular graph, the small-order partition argument no longer supplies all the necessary cut inequalities. Nothing above establishes the conjecture for arbitrary numbers of odd-degree vertices or produces a counterexample. I have also not established that this restricted theorem is new.