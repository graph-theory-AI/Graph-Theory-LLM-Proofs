```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The quoted Kwan–Sudakov–Tran theorem with t=3 immediately implies the conjecture, because girth at least 4 implies triangle-freeness and their lower bound eventually exceeds 3.",
  "would_publish": false,
  "caveats": "This uses the Kwan–Sudakov–Tran theorem exactly as quoted; even if their conclusion is stated in terms of average degree, a standard pruning argument still suffices."
}
```

## Statement

We consider finite simple graphs. The conjecture asks for constants \(d_0,g_0\) such that every graph \(G\) satisfying
\[
\delta(G)\ge d_0
\qquad\text{and}\qquad
\operatorname{girth}(G)\ge g_0
\]
contains an induced bipartite subgraph of minimum degree at least \(3\).

The catalog’s own literature review states that Kwan, Sudakov, and Tran proved the following stronger asymptotic result:

> For every fixed \(t\), every \(K_t\)-free graph of sufficiently large minimum degree \(d\) contains an induced bipartite subgraph whose minimum degree is
> \[
> \Omega_t\!\left(\frac{\log d}{\log\log d}\right).
> \]

Taking \(t=3\) resolves the conjecture.

## Proof

Fix \(t=3\). By the quoted theorem, there are constants \(c>0\) and \(D\) such that every triangle-free graph \(G\) with minimum degree \(d\ge D\) contains an induced bipartite subgraph \(H\) satisfying
\[
\delta(H)\ge c\frac{\log d}{\log\log d}.
\]

Since
\[
\frac{\log d}{\log\log d}\longrightarrow\infty
\qquad (d\to\infty),
\]
we may choose \(d_0\ge D\) sufficiently large that
\[
c\frac{\log d}{\log\log d}\ge 3
\]
for every \(d\ge d_0\).

Set
\[
g_0=4.
\]
If \(G\) has girth at least \(4\), then \(G\) contains no triangle and hence is \(K_3\)-free. Therefore, whenever additionally \(\delta(G)\ge d_0\), the \(t=3\) case of the quoted theorem supplies an induced bipartite subgraph \(H\) with
\[
\delta(H)\ge 3.
\]
This is precisely the desired conclusion.

## If the published theorem is stated with average degree

Some summaries of dense-induced-bipartite-subgraph results state the conclusion in terms of average rather than minimum degree. That formulation still suffices.

Indeed, suppose the theorem gives an induced bipartite \(B\) with
\[
\overline d(B)\ge c\frac{\log d}{\log\log d}.
\]
Choose \(d_0\) so that the right-hand side is at least \(6\). Repeatedly delete from \(B\) any vertex of degree at most \(2\). This process cannot delete every vertex: if it did, charging each edge when its first endpoint is deleted would give
\[
|E(B)|\le 2|V(B)|,
\]
contrary to \(\overline d(B)\ge6\), which gives
\[
|E(B)|\ge3|V(B)|.
\]
Thus the remaining nonempty induced subgraph has minimum degree at least \(3\). It remains bipartite and, being obtained only by deleting vertices from an induced subgraph of \(G\), remains induced in \(G\).

## Status assessment

The catalog’s sentence that the \(K_t\)-free result “does not imply the large-girth statement” is logically incorrect under the theorem statement it quotes. Graphs of girth at least \(4\) form a subclass of triangle-free graphs, so every universal result for triangle-free graphs applies to them. Thus the conjecture is already resolved, with \(g_0=4\) and some sufficiently large \(d_0\) supplied by the asymptotic theorem.

The deduction itself has no gap. The only external dependency is the precise Kwan–Sudakov–Tran theorem quoted in the supplied literature review.