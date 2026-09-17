```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds whenever one vertex meets every odd directed cycle, with the stronger bound 2d+2 for d>=2.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; no novelty claim is made for this elementary special case."
}
```

## 1. A special-case theorem

All digraphs below are finite and oriented: they have no loops or pairs of oppositely directed arcs. Write \(c(D)\) for the maximum length of a directed cycle and
\[
\delta^0(D)=\min\{\delta^+(D),\delta^-(D)\}.
\]

I do not resolve the unrestricted conjecture. The following result covers, in particular, oriented graphs whose underlying graph becomes bipartite after deleting one vertex.

**Theorem.** Let \(d\ge 2\), and let \(D\) be an oriented graph with \(\delta^0(D)\ge d\). Suppose there is a vertex \(z\) such that \(D-z\) contains no odd directed cycle. Then
\[
c(D)\ge 2d+2.
\]
Strong connectivity is not required.

The hypothesis concerns **directed** odd cycles; it is weaker than requiring the underlying graph of \(D-z\) to be bipartite.

For \(d=1\), the original conjecture is immediate: positive minimum outdegree guarantees a directed cycle, and an oriented graph has no cycle of length less than three. The strengthened bound above cannot include \(d=1\), as a directed triangle demonstrates.

## 2. Proof

Suppose, for a contradiction, that
\[
c(D)\le 2d+1.
\]
Put \(H=D-z\), and choose a directed path
\[
P=v_1v_2\cdots v_m
\]
with the maximum possible number of vertices in \(H\).

### Endpoint constraints

Every out-neighbor of \(v_m\) in \(H\) belongs to \(P\), since otherwise \(P\) could be extended. Each arc \(v_m\to v_i\) produces the directed cycle
\[
v_i v_{i+1}\cdots v_m v_i.
\]
Different out-neighbors produce different cycle lengths.

These cycles are even, because \(H\) has no odd directed cycles. They have length at least four, because \(H\) is oriented, and length at most \(2d\), because \(c(D)\le 2d+1\). Thus their lengths belong to
\[
\{4,6,\ldots,2d\},
\]
a set of \(d-1\) possibilities. Consequently,
\[
d_H^+(v_m)\le d-1.
\]
The corresponding argument at the initial vertex gives
\[
d_H^-(v_1)\le d-1.
\]

Deleting \(z\) removes at most one out-neighbor or in-neighbor from any vertex. Since \(\delta^0(D)\ge d\), both inequalities must be equalities, and
\[
d_H^+(v_m)=d_H^-(v_1)=d-1,
\qquad
v_m\to z,\quad z\to v_1. \tag{1}
\]

Importantly, these conclusions apply to **every** maximum-order directed path in \(H\).

### Closing and rotating the path

The \(d-1\) out-neighbors of \(v_m\) produce \(d-1\) distinct lengths from the set \(\{4,6,\ldots,2d\}\). Hence one of these cycles has length \(2d\), and therefore
\[
m\ge 2d.
\]

On the other hand, the two arcs in (1) close \(P\) through \(z\), producing a directed cycle of length \(m+1\). Our assumed circumference bound gives
\[
m+1\le 2d+1.
\]
Thus \(m=2d\). The cycle of length \(2d\) obtained from an out-neighbor of \(v_m\) must consequently use all of \(P\), so
\[
v_{2d}\to v_1.
\]

Now rotate this cycle to obtain another maximum-order path in \(H\):
\[
Q=v_2v_3\cdots v_{2d}v_1.
\]
Applying the terminal-vertex conclusion of (1) to \(Q\) forces \(v_1\to z\). But applying the initial-vertex conclusion to \(P\) already gave \(z\to v_1\). This is a forbidden pair of opposite arcs.

The contradiction proves \(c(D)\ge 2d+2\). \(\square\)

## 3. Consequences

### One-vertex deletion to bipartiteness

If the underlying graph of \(D-z\) is bipartite, then \(D-z\) has no odd directed cycle. Thus the conjecture holds for this class, with one additional vertex in the guaranteed cycle when \(d\ge2\).

For comparison, when \(D\) itself has no odd directed cycles, the endpoint-counting argument already gives \(c(D)\ge2d+2\) using minimum outdegree alone. The theorem shows that one exceptional vertex can be accommodated without losing that bound, provided minimum indegree is also available.

### A quantitative extension

Suppose a set \(S\) of \(t\ge1\) vertices meets every odd directed cycle of \(D\), and assume \(d\ge t+1\). Then
\[
\boxed{c(D)\ge 2d-2t+4.}
\]

Indeed, choose \(z\in S\) and delete \(S\setminus\{z\}\). The resulting oriented graph has minimum indegree and outdegree at least
\[
d-t+1\ge2,
\]
and deleting \(z\) eliminates all its odd directed cycles. Apply the theorem. Its lack of a connectivity assumption is useful here, since vertex deletion need not preserve strong connectivity.

### A necessary condition for a counterexample

For \(d\ge2\), any counterexample to the original conjecture must satisfy:

> For every vertex \(z\), there is an odd directed cycle avoiding \(z\).

Since such a counterexample would have circumference at most \(2d\), these odd cycles would all have length at most \(2d-1\).

## 4. Strong sharpness examples and a correction to the context

The disjoint union mentioned in the supplied discussion is not itself strong. There is, however, a straightforward strong sharpness construction.

Let \(T\) be the regular tournament on \(\mathbb Z_{2d+1}\) with
\[
i\to j
\quad\Longleftrightarrow\quad
j-i\pmod{2d+1}\in\{1,\ldots,d\}.
\]
It has indegree and outdegree \(d\) at every vertex and contains the directed Hamilton cycle
\[
0,1,\ldots,2d,0.
\]

Take \(q\ge2\) copies of \(T\), identify their vertices labelled \(0\) into one vertex \(z\), and add no other arcs.

The resulting graph:

- is strongly connected;
- has indegree and outdegree \(d\) at every vertex other than \(z\);
- has indegree and outdegree \(qd\) at \(z\);
- has order \(2dq+1\);
- has circumference exactly \(2d+1\).

For the last assertion, a simple directed cycle cannot pass between two different copies: doing so would require using \(z\) more than once.

Thus the proposed bound is sharp even among strong oriented graphs of arbitrarily large order. Taking \(q=2\) also shows that Hamiltonicity at order \(4d+1\) is false under minimum-semidegree assumptions alone. The related Hamilton-cycle statement must retain its **regularity** assumption.

## 5. What remains unproved

Without a parity restriction, the elementary longest-path argument only guarantees
\[
c(D)\ge d+2:
\]
the terminal vertex has at least \(d\) out-neighbors on the path, producing \(d\) distinct cycle lengths, all at least three. This is an elementary bound, not a claim about the best bound in the literature.

The special-case proof works because the absence of odd cycles in \(D-z\) leaves only \(d-1\) permissible closing-cycle lengths under the assumed circumference bound. This forces both endpoint attachments to \(z\), enabling the closing-and-rotation contradiction.

For a general strong oriented graph, odd and even closing cycles are both available, and those attachments are no longer forced. Nothing above establishes that an appropriate vertex \(z\) exists. Accordingly, the unrestricted conjecture remains unresolved by this argument.