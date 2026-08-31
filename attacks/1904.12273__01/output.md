```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For every fixed long-hole threshold at least seven, a four-vertex C-major set admits no bounded catching path, although C is the unique long odd hole.",
  "would_publish": false,
  "caveats": "This uses the standard definition of C-major and interprets bounded as depending only on the long-hole threshold; omitted source-paper hypotheses could alter the conclusion."
}
```

## Formal interpretation

Use the standard definition: a vertex \(v\notin V(C)\) is \(C\)-major if \(N(v)\cap V(C)\) is not contained in a three-vertex subpath of \(C\).

The natural formalization of “bounded length” is:

> For every fixed long-hole threshold \(t\), there is an integer \(b(t)\) such that, whenever \(C\) is a shortest odd hole of length at least \(t\) and \(M\) satisfies the stated hypothesis, some subpath \(Q\) of \(C\), with at most \(b(t)\) edges, contains a neighbor of every vertex of \(M\).

This statement is false, even with \(|M|=4\).

## Counterexample construction

Fix \(t=7\). Let \(q\ge 3\) be an arbitrary odd integer.

Construct an odd cycle \(C\) from three internally vertex-disjoint paths
\[
A_1:a_1\mathbin{-}\cdots\mathbin{-}a_2,\qquad
A_2:a_2\mathbin{-}\cdots\mathbin{-}a_3,\qquad
A_3:a_3\mathbin{-}\cdots\mathbin{-}a_1,
\]
each having exactly \(q\) edges. Thus
\[
|V(C)|=3q,
\]
which is odd.

Add vertices \(y_1,y_2,y_3,x\), with the following adjacencies:

1. \(y_1,y_2,y_3\) form a triangle;
2. for \(i=1,2,3\),
   \[
   N_C(y_i)=V(A_i);
   \]
3. \(x\) is complete to \(V(C)\);
4. \(x\) is anticomplete to \(\{y_1,y_2,y_3\}\);
5. there are no further edges.

Let
\[
M=\{x,y_1,y_2,y_3\}.
\]

## Verification of the premise

Since \(q\ge 3\), each \(N_C(y_i)=V(A_i)\) contains at least four consecutive vertices of \(C\), and hence is not contained in a three-vertex path of \(C\). Thus every \(y_i\) is \(C\)-major. The vertex \(x\), being complete to \(C\), is also \(C\)-major.

Moreover, \(x\) is nonadjacent to every other member of \(M\), exactly as required.

## Classification of the odd holes

We show that \(C\) is the unique odd hole of length at least seven.

### Holes not containing \(x\)

Let \(D\) be a hole in \(G-x\).

#### No \(y_i\) in \(D\)

Then \(D=C\), since the subgraph on \(V(C)\) is just a chordless cycle.

#### Exactly one \(y_i\) in \(D\)

The \(C\)-neighbors of \(y_i\) form the consecutive block \(V(A_i)\). The gaps between consecutive \(C\)-neighbors of \(y_i\) consist of:

- the \(q\) individual edges of \(A_i\), producing triangles with \(y_i\); and
- the complementary \(C\)-path \(A_j\cup A_k\), of length \(2q\).

Consequently, the only hole containing \(y_i\) and no other \(y\)-vertex has length
\[
2q+2,
\]
which is even.

#### Exactly two of \(y_1,y_2,y_3\) in \(D\)

Suppose they are \(y_i,y_j\), and let \(k\) be the remaining index. Since the \(y\)'s form a clique, \(y_i\) and \(y_j\) must be consecutive on the induced cycle \(D\).

The remaining vertices of \(D\) form a path in \(C\). Its internal vertices must be anticomplete to both \(y_i\) and \(y_j\); otherwise there is a chord. This forces the path to be precisely the remaining arc \(A_k\), joining the endpoint of \(A_i\) not shared with \(A_j\) to the endpoint of \(A_j\) not shared with \(A_i\).

Thus this hole has length
\[
q+3,
\]
which is even because \(q\) is odd.

#### All three \(y_i\) in \(D\)

This is impossible for an induced cycle of length at least four, since \(y_1,y_2,y_3\) form a triangle and one of their three edges would be a chord.

It follows that every hole in \(G-x\), other than \(C\), is even.

### Holes containing \(x\)

Let \(D\) be an induced cycle containing \(x\). The two neighbors of \(x\) on \(D\) must lie in \(C\), since \(x\) has no \(y_i\)-neighbors. As \(x\) is adjacent to every vertex of \(C\), these are the only two vertices of \(C\) that can belong to \(D\); any additional \(C\)-vertex would give a chord from \(x\).

The path between those two \(C\)-vertices avoiding \(x\) therefore has all its internal vertices in \(\{y_1,y_2,y_3\}\). Since these three vertices form a clique, an induced such path has at most two internal vertices. Hence
\[
|V(D)|\le 5.
\]

Therefore every odd hole containing \(x\) has length at most five.

Combining the two cases, \(C\) is the unique odd hole of length at least seven. In particular, \(C\) is a shortest long odd hole for threshold \(t=7\). The same construction works for every fixed threshold \(t\ge 6\), after choosing \(3q\ge t\).

## No bounded catching path

A path \(Q\subseteq C\) catches \(y_i\) exactly when
\[
V(Q)\cap V(A_i)\ne\varnothing.
\]
Every nonempty path catches \(x\), because \(x\) is complete to \(C\).

The three corner vertices \(a_1,a_2,a_3\) are pairwise at distance \(q\) in \(C\). Hence a subpath of \(C\) with fewer than \(q\) edges contains at most one corner.

- If it contains no corner, it lies in the interior of one \(A_i\), so it misses two of the \(y_j\).
- If it contains exactly one corner, it can meet only the two arcs incident with that corner, so it misses the third \(y_j\).

Thus every path catching all of \(M\) has at least \(q\) edges. Conversely, each \(A_i\) itself has \(q\) edges and catches all three \(y_j\), since its endpoints lie in the other two arcs. Therefore the minimum catching-path length is exactly \(q\).

Since \(q\) is arbitrarily large while the threshold remains fixed at \(t=7\), no bound depending only on \(t\) exists.

## Scope

This disproves the catalog statement under its standard reading. It does not address a possible version restricted to \(t=5\), to stable \(M\), or to additional “candidate graph” hypotheses that may have been present implicitly in the source discussion.