```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Yes: the finite-state bound gives capt_k(G) <= n^{c(G)+1} for every k >= c(G), and hence Schroeder's conjecture immediately yields capt_k(G) <= n^{g+4}.",
  "would_publish": false,
  "caveats": "This does not prove Schroeder's conjecture or any sharper surface-specific capture-time bound."
}
```

## Statement

Consider the standard visible Cops and Robber game on a finite \(n\)-vertex graph \(G\), with passing allowed and the cops moving first after the initial placements. Set \(\operatorname{capt}_k(G)=\infty\) when \(k<c(G)\).

The relevant general fact is the following.

### Proposition

For every finite graph \(G\) and every \(k\ge c(G)\),
\[
\operatorname{capt}_k(G)\le n^{\,c(G)+1}.
\]
More generally, if \(h\) cops can win, then
\[
\operatorname{capt}_k(G)\le \operatorname{capt}_h(G)\le n^{h+1}
\qquad\text{for every }k\ge h.
\]

Consequently, if \(\gamma(G)=g\) and Schroeder's conjecture holds for \(G\), so that
\[
c(G)\le g+3,
\]
then for every \(k\ge g+3\),
\[
\operatorname{capt}_k(G)
 \le n^{c(G)+1}
 \le n^{g+4}.
\]
Thus the requested \(O(n^{g+4})\) estimate is valid, with constant \(1\) under the usual convention for counting rounds.

## Finite-state proof

Fix \(h\) cops. Label them temporarily. A position at the beginning of a cop move is
\[
(X,r)=((x_1,\dots,x_h),r)\in V(G)^h\times V(G).
\]
There are exactly
\[
|V(G)^h\times V(G)|=n^{h+1}
\]
such positions.

Let \(T\) be the set of captured positions, namely those for which
\[
r\in\{x_1,\dots,x_h\}.
\]
Define sets \(A_0,A_1,\ldots\) recursively. Put \(A_0=T\). Given \(A_t\), put a position \((X,r)\) in \(A_{t+1}\) if it is already in \(A_t\), or if the cops have a legal move
\[
X=(x_1,\dots,x_h)\longrightarrow Y=(y_1,\dots,y_h)
\]
such that either:

1. \(r\in\{y_1,\dots,y_h\}\), so the robber is captured on that cop move; or
2. every safe robber response \(s\in N[r]\setminus\{y_1,\dots,y_h\}\) satisfies
   \[
   (Y,s)\in A_t.
   \]

By induction, every position in \(A_t\) permits capture in at most \(t\) complete rounds.

Let
\[
A_\infty=\bigcup_{t\ge0}A_t.
\]
Because there are only \(n^{h+1}\) positions, this increasing sequence stabilizes after at most \(n^{h+1}\) iterations.

It remains to verify that \(A_\infty\) is exactly the set of winning positions. Suppose \((X,r)\notin A_\infty\). Since \(A_\infty\) is a fixed point of the above operation, after every legal cop move \(X\to Y\):

- the cops do not immediately capture \(r\), and
- there is a safe robber response \(s\in N[r]\setminus\{y_1,\dots,y_h\}\) such that
  \[
  (Y,s)\notin A_\infty.
  \]

The robber can therefore remain outside \(A_\infty\) after every round and evade forever. Hence a position is winning for the cops only if it lies in \(A_\infty\). It follows that every winning position has capture rank at most \(n^{h+1}\).

If \(h\) cops can win, they have an initial placement \(X_0\) from which every robber starting position is winning. Therefore
\[
\operatorname{capt}_h(G)\le n^{h+1}.
\]

Finally, capture time is nonincreasing in the number of cops: when \(k\ge h\), designate \(h\) cops to execute the \(h\)-cop strategy and leave the others unused. Thus
\[
\operatorname{capt}_k(G)\le\operatorname{capt}_h(G).
\]

If capture time is counted in individual plies rather than complete rounds, the same argument gives at most \(2n^{h+1}+O(1)\), which has the same asymptotic form.

## Application to genus

Take \(h=c(G)\). Under Schroeder's conjecture,
\[
h=c(G)\le g+3.
\]
For every \(k\ge g+3\), we have \(k\ge h\), and hence
\[
\operatorname{capt}_k(G)
 \le n^{h+1}
 \le n^{g+4}.
\]

No topological argument beyond the proposed cop-number bound is needed.

Indeed, for each fixed genus \(g\), the following assertions are equivalent:

1. Every genus-\(g\) graph satisfies \(c(G)\le g+3\).
2. Every genus-\(g\) graph has finite \(\operatorname{capt}_{g+3}(G)\).
3. Every genus-\(g\) graph satisfies
   \[
   \operatorname{capt}_{g+3}(G)\le n^{g+4}.
   \]

The implication \(1\Rightarrow3\) is the finite-state argument above; \(3\Rightarrow2\Rightarrow1\) follows directly from the definition of cop number. Thus an unconditional version at \(k=g+3\) is not a separate conjectural obstacle: it is equivalent to Schroeder's conjecture.

## Elementary lower-bound context

For completeness, define the \(k\)-center radius
\[
\rho_k(G)=\min_{\substack{S\subseteq V(G)\\ |S|\le k}}\max_{v\in V(G)}d(v,S).
\]
A robber may start at a vertex farthest from the initial cop set and remain there. Consequently,
\[
\operatorname{capt}_k(G)\ge \rho_k(G).
\]

This gives linear examples for every fixed genus and fixed \(k\). Fix a graph \(H\) of genus \(g\), and attach a pendant path of \(L\) edges at one vertex. The resulting graph still has genus exactly \(g\). A radius-\(R\) ball meets the pendant path in at most \(2R+1\) vertices, so \(k\) such balls cannot cover its \(L+1\) vertices unless
\[
k(2R+1)\ge L+1.
\]
Hence
\[
\operatorname{capt}_k(G)\ge \rho_k(G)
 \ge \left\lceil\frac{L+1-k}{2k}\right\rceil.
\]
For fixed \(g\) and \(k\), this is \(\Omega(n)\).

The gap between this elementary linear lower bound and the state-space upper bound \(n^{g+4}\) is not addressed here. In particular, no sharper exponent exploiting a surface embedding, and no proof of Schroeder's conjecture for higher genus, is obtained.