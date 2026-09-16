```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "Under the stated minimum-degree definition, two regular tournaments sharing one vertex give a counterexample on exactly 4d+1 vertices.",
  "would_publish": false,
  "caveats": "This disproves the explicitly stated at-least-d version, not the different conjecture requiring both degrees to equal d."
}
```

## Counterexample to the statement as written

The distinction between **minimum semidegree at least \(d\)** and **indegree and outdegree exactly \(d\)** is decisive here.

**Proposition.** For every integer \(d\ge 1\), there is a strongly connected oriented graph \(G_d\) on \(4d+1\) vertices such that
\[
d^+(u)\ge d,\qquad d^-(u)\ge d
\]
for every vertex \(u\), but \(G_d\) has no Hamilton cycle.

### Construction

Let \(T_d\) be the regular tournament on \(\mathbb Z/(2d+1)\mathbb Z\), with
\[
i\longrightarrow j
\quad\Longleftrightarrow\quad
j-i\pmod{2d+1}\in\{1,\ldots,d\}.
\]
Every vertex has indegree and outdegree exactly \(d\).

Take two disjoint copies of \(T_d\) and identify their vertices labelled \(0\) into a single vertex \(v\). Make no other identifications and add no arcs. Write \(A\) and \(B\) for the respective sets of nonidentified vertices. Thus
\[
|A|=|B|=2d,
\]
and there are no arcs between \(A\) and \(B\).

### Verification of the hypotheses

The resulting graph is oriented: each copy is a tournament, and sharing just one vertex cannot create parallel arcs or opposite arcs.

Its order is
\[
|V(G_d)|=2(2d+1)-1=4d+1.
\]
Every vertex other than \(v\) retains its original degrees, so
\[
d^+(u)=d^-(u)=d\qquad(u\ne v).
\]
At the shared vertex, the contributions from the two copies add:
\[
d^+(v)=d^-(v)=2d.
\]
Consequently \(G_d\) is \(d\)-diregular under the question’s explicit definition.

In fact, \(G_d\) is strongly connected. Each copy contains the directed cycle
\[
0\longrightarrow1\longrightarrow\cdots\longrightarrow2d\longrightarrow0,
\]
so vertices in either copy can reach the common vertex and can be reached from it.

### Nonexistence of a Hamilton cycle

Suppose \(G_d\) had a directed Hamilton cycle. Deleting \(v\) from that cycle would leave a directed Hamilton path in \(G_d-v\).

But \(G_d-v\) consists of the two nonempty sets \(A\) and \(B\), with no arcs between them in either direction. No directed path can visit vertices from both sets. This is a contradiction. \(\square\)

In particular, **\(d=3\) gives an explicit counterexample on \(13\) vertices**: two cyclic regular tournaments on seven vertices, sharing one vertex.

## Scope of the disproof

This resolves the displayed statement **with “at least \(d\)” as its definition**.

It does **not** refute the exact-regularity conjecture discussed in the supplied literature summary, whose hypothesis is
\[
d^+(u)=d^-(u)=d\qquad\text{for every }u.
\]
Our shared vertex has both degrees \(2d\), so that hypothesis fails. Likewise, the construction is not strongly \(2\)-connected and therefore does not address the Kühn–Osthus variant.

Thus the minimum-degree formulation is false; the exact-\(d\)-regular problem remains untouched by this argument.