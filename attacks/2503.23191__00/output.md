```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For every even k at least 4, the balanced blow-up of a directed triangle omits a non-antidirected k-edge path.",
  "would_publish": false,
  "caveats": "This uses the standard definition that an antidirected path has alternating arc directions, equivalently no directed two-edge subpath."
}
```

## Statement

Under the standard terminology, an antidirected path is an oriented path in which every internal vertex is a source or a sink. Equivalently, the directions of consecutive edges alternate.

The proposed statement is false, already for \(k=4\).

## Smallest counterexample

Let \(G\) be the balanced blow-up of the directed triangle with parts
\[
A_0,A_1,A_2,\qquad |A_0|=|A_1|=|A_2|=2,
\]
with all arcs
\[
A_0\to A_1,\qquad A_1\to A_2,\qquad A_2\to A_0,
\]
and no arcs within a part.

Every vertex has exactly two inneighbors and two outneighbors, so
\[
\delta^0(G)=2=\frac{k}{2}
\]
for \(k=4\).

Consider the oriented path
\[
P:\qquad x_0\to x_1\leftarrow x_2\leftarrow x_3\to x_4.
\]
This is not antidirected: it contains the directed two-edge subpath
\[
x_3\to x_2\to x_1.
\]

Suppose that \(G\) contained \(P\). Since \(x_0\) and \(x_2\) are both inneighbors of \(x_1\), they must belong to the same part of the blow-up: all inneighbors of any vertex of \(G\) lie in one part. Likewise, \(x_2\) and \(x_4\) are both outneighbors of \(x_3\), so they must belong to the same part. Consequently
\[
x_0,x_2,x_4
\]
would all lie in one part. They are distinct, whereas every part has only two vertices, a contradiction.

Thus \(G\) has minimum semidegree \(k/2\) but does not contain the non-antidirected \(4\)-edge path \(P\).

## Infinite family

The same obstruction works for every even \(k\ge4\). Write \(k=2m\), where \(m\ge2\), and let \(G_m\) be the cyclic blow-up
\[
A_0\to A_1\to A_2\to A_0,
\qquad |A_0|=|A_1|=|A_2|=m.
\]
Then
\[
\delta^0(G_m)=m=\frac{k}{2}.
\]

Let \(P_m\) have vertices \(v_0,\ldots,v_{2m}\). Orient
\[
v_0\to v_1\leftarrow v_2,
\]
and, for every \(2\le j\le m\), orient both edges incident with \(v_{2j-1}\) away from that vertex:
\[
v_{2j-1}\to v_{2j-2},
\qquad
v_{2j-1}\to v_{2j}.
\]
In particular,
\[
v_3\to v_2\to v_1,
\]
so \(P_m\) is not antidirected.

In any embedding into \(G_m\), for each \(j\), the vertices \(v_{2j-2}\) and \(v_{2j}\) are either both inneighbors or both outneighbors of \(v_{2j-1}\). Hence they must lie in the same blow-up part. Induction gives
\[
v_0,v_2,\ldots,v_{2m}
\]
all in one part. These are \(m+1\) distinct vertices, but every part has size \(m\), which is impossible.

More generally, this blow-up excludes every orientation in which all vertices in the smaller bipartition class
\[
\{v_1,v_3,\ldots,v_{2m-1}\}
\]
are sources or sinks. Only two of these orientations are antidirected; choosing different source/sink types at two consecutive odd vertices produces a directed two-edge subpath. Thus the exact-threshold obstruction is substantially broader than the antidirected orientations alone.

There are no remaining cases or computational assumptions needed for the disproof.