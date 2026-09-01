```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The quoted fixed-clique-number theorem implies the conjecture by a staircase diagonalization, even with x_2(d)=x_3(d).",
  "would_publish": false,
  "caveats": "This relies on the prompt's claim that the Kwan-Sudakov-Tran theorem holds for every fixed t; a triangle-free-only result would not suffice."
}
```

## Statement

Assume the following result attributed in the prompt to Kwan, Sudakov, and Tran:

> For every fixed integer \(r\ge 3\), there are constants \(c_r>0\) and \(d_r^0\) such that every \(K_r\)-free graph \(G\) with minimum degree at least \(d\ge d_r^0\) has an induced bipartite subgraph of minimum degree at least
> \[
> c_r\frac{\log d}{\log\log d}.
> \tag{1}
> \]

Then Conjecture 1.4 follows formally. No estimate uniform in \(r\) is needed.

## Diagonalization lemma

For each \(r\ge3\), since
\[
c_r\frac{\log d}{\log\log d}\longrightarrow\infty
\qquad(d\to\infty),
\]
there is an integer \(A_r\) such that every \(K_r\)-free graph of minimum degree at least \(A_r\) contains an induced bipartite subgraph of minimum degree at least \(r\).

Replace these thresholds by a strictly increasing sequence. Namely, let
\[
D_3=\max\{3,A_3\},
\]
and recursively, for \(r\ge4\), put
\[
D_r=\max\{A_r,D_{r-1}+1,r\}.
\]
Thus \(D_r\ge r\), and every \(K_r\)-free graph of minimum degree at least \(D_r\) contains an induced bipartite subgraph of minimum degree at least \(r\).

For a positive integer \(d\), define
\[
k(d)=
\begin{cases}
1,&d<D_3,\\[2mm]
\max\{r\ge3:D_r\le d\},&d\ge D_3.
\end{cases}
\]
The maximum is finite because \(D_r\ge r\). Moreover, for every fixed \(R\), if \(d\ge D_R\), then \(k(d)\ge R\). Hence
\[
k(d)\longrightarrow\infty.
\]

Set
\[
x_2(d)=x_3(d)=k(d).
\]

Now let \(G\) be any graph with \(\delta(G)\ge d\). For \(d<D_3\), the clique alternative with \(x_2(d)=1\) is automatic. Otherwise put \(k=k(d)\). There are two cases.

1. If \(G\) contains \(K_k\), then the first alternative holds.

2. If \(G\) does not contain \(K_k\), then \(G\) is \(K_k\)-free. Since
   \[
   \delta(G)\ge d\ge D_k\ge A_k,
   \]
   the fixed-\(k\) theorem gives an induced bipartite subgraph of minimum degree at least \(k=x_3(d)\).

This proves the conjectured dichotomy, with both functions equal and tending to infinity.

## If the cited theorem is stated using average degree

The same deduction works if the published result only guarantees an induced bipartite subgraph of average degree tending to infinity. Indeed, every graph of average degree at least \(2r\) has a nonempty induced subgraph of minimum degree at least \(r\): repeatedly delete vertices of degree less than \(r\); deleting every vertex would account for fewer than \(r|V|\) edges, contradicting average degree at least \(2r\). A further induced subgraph of an induced bipartite graph remains induced and bipartite. One therefore chooses \(A_r\) so that the average-degree conclusion is at least \(2r\).

## Quantifier diagnosis

More generally, the conjecture is qualitatively equivalent to the following family of assertions:

> For every fixed \(r\), the largest guaranteed minimum degree of an induced bipartite subgraph in a \(K_r\)-free graph tends to infinity with the minimum degree of the ambient graph.

The forward implication is immediate: once \(x_2(d)\ge r\), a \(K_r\)-free graph cannot satisfy the clique alternative, so it must satisfy the bipartite alternative. The reverse implication is exactly the diagonal construction above.

Consequently, the catalog's assertion that a theorem for every fixed \(K_t\)-free class “does not settle” Conjecture 1.4 is incompatible with the theorem summary given there. Dependence of the constants and thresholds on \(t\) is harmless, because \(x_2(d)\) may be chosen to grow arbitrarily slowly.

## Caveat

I have used the fixed-\(t\), \(K_t\)-free theorem exactly as stated in the prompt and have not independently checked the full text of the cited paper here. If that paper proves the structural assertion only for triangle-free graphs (\(t=3\)), then the diagonal argument does not apply. If it proves it for every fixed \(t\), in either minimum-degree or average-degree form, the conjecture is completely settled by the argument above.