```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Seymour’s r-graph conjecture is an immediate corollary of the proved Goldberg–Seymour edge-colouring theorem.",
  "would_publish": false,
  "caveats": "Uses the established Goldberg–Seymour theorem; graphs are finite loopless multigraphs, and this is not a new result."
}
```

## Statement and status

Under the intended convention, graphs are **finite loopless multigraphs**: parallel edges are allowed and counted with multiplicity. The assertion is:

> If \(G\) is \(r\)-regular and
> \[
> |\delta_G(X)|\ge r
> \qquad\text{for every odd-cardinality }X\subseteq V(G),
> \]
> then \(\chi'(G)\le r+1\).

This is already resolved by the Goldberg–Seymour theorem, as the supplied catalog reports. The historical OpenProblemGarden discussion predates that resolution. Below is the complete deduction.

## External theorem used

For a finite loopless multigraph \(H\), define its odd-set density by
\[
\Gamma(H)=
\max_{\substack{X\subseteq V(H)\\ |X|\ge3,\ |X|\text{ odd}}}
\frac{2|E(H[X])|}{|X|-1},
\]
with value \(0\) if the indexing family is empty.

The **Goldberg–Seymour theorem**, due to Chen, Jing, and Zang, states that
\[
\chi'(H)\le
\max\!\left\{\Delta(H)+1,\left\lceil\Gamma(H)\right\rceil\right\}.
\tag{GS}
\]

This is the established theorem identified in the supplied literature review, not an unproved conjecture being assumed. I do not reproduce its proof or claim an independent check of the supplied journal metadata.

## Proof of Seymour’s assertion

If \(G\) has no edges, the conclusion is immediate. Otherwise, \(r\)-regularity gives
\[
\Delta(G)=r.
\]

Let \(X\subseteq V(G)\) have odd cardinality at least \(3\). Counting the degrees of the vertices in \(X\), with every internal edge counted twice, gives
\[
r|X|=2|E(G[X])|+|\delta_G(X)|.
\]
The \(r\)-graph hypothesis therefore yields
\[
2|E(G[X])|
=r|X|-|\delta_G(X)|
\le r|X|-r
=r(|X|-1).
\]
Dividing by the positive number \(|X|-1\), we obtain
\[
\frac{2|E(G[X])|}{|X|-1}\le r.
\]
Taking the maximum over all eligible odd sets proves
\[
\Gamma(G)\le r.
\]
This also holds when there are no eligible sets, by the convention \(\Gamma(G)=0\).

Since \(r\) is an integer,
\[
\left\lceil\Gamma(G)\right\rceil\le r.
\]
Applying (GS), we conclude
\[
\chi'(G)
\le
\max\!\left\{r+1,\left\lceil\Gamma(G)\right\rceil\right\}
\le r+1.
\qquad\square
\]

## Scope and remaining gaps

The deduction covers disconnected graphs, parallel edges, and graphs with fewer than three vertices. It requires no connectivity assumption. For simple graphs, the same upper bound already follows from Vizing’s theorem without the odd-cut hypothesis; multigraphs are the substantive setting.

There is no remaining gap in this deduction. Its deep external input is the established Goldberg–Seymour theorem. Consequently, this is an already-known resolution, not a new proof warranting publication.