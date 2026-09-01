```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A standard induced-topological extremal theorem reduces the conjecture to an induced-biclique obstruction, proving it for complete-bipartite targets and certain disconnected mixtures.",
  "would_publish": false,
  "caveats": "This uses the standard closed radius-two definition and the Kühn–Osthus extremal theorem; arbitrary targets remain open because induced bicliques have bounded χ₂."
}
```

## 1. Interpretation

Write
\[
B_G^r(v)=\{x\in V(G):d_G(x,v)\le r\},\qquad
\chi_r(G)=\max_{v\in V(G)}\chi\bigl(G[B_G^r(v)]\bigr).
\]
This is the standard meaning of the parameter denoted \(\chi_2\) in the statement. Define \(\chi_1\) analogously. Then
\[
\omega(G)\le \chi_1(G)\le \chi_2(G).
\]

The cases \(\tau\le1\) are immediate for every \(J\). If \(\chi_2(G)\le0\), then \(G\) is null. If \(\chi_2(G)\le1\), then \(G\) has no edge, since the radius-two ball around an endpoint of an edge has chromatic number at least two. Thus one may take \(c=0\) for \(\tau=0\) and \(c=1\) for \(\tau=1\).

Below, all graphs are finite and simple.

## 2. Extremal input

I use the following theorem of Kühn and Osthus, from *Induced subdivisions in \(K_{s,s}\)-free graphs of large average degree*, Combinatorica 24 (2004).

> **Kühn–Osthus theorem.**  
> For all positive integers \(s,t\), there is \(d(s,t)\) such that every graph of average degree at least \(d(s,t)\) contains either \(K_{s,s}\) as a not necessarily induced subgraph or an induced subdivision of \(K_t\).

The following standard corollary will be the useful form.

> **Extremal induced-subdivision lemma.**  
> For every finite graph \(H\) and every positive integer \(s\), there is \(D(H,s)\) such that every graph of average degree at least \(D(H,s)\) contains either a \(K_{s,s}\) subgraph or an induced subdivision of \(H\).

### Proof

Let \(n=|V(H)|\), and choose \(t\) large enough that every graph on \(t\) vertices has either a clique of order \(2s\) or a stable set of order \(n\). Apply the Kühn–Osthus theorem with \(s,t\).

Suppose that the graph contains no \(K_{s,s}\) subgraph. We obtain an induced subdivision \(S\) of \(K_t\). Consider the graph induced by the \(t\) branch vertices of \(S\). It has no clique of order \(2s\), since such a clique contains a \(K_{s,s}\) subgraph. Hence it has a stable set \(X\) of order \(n\).

Index \(X\) by \(V(H)\). For every edge \(uv\in E(H)\), retain the corresponding branch-to-branch path of the \(K_t\)-subdivision, and omit the paths corresponding to nonedges of \(H\). Since \(X\) is stable, none of the omitted pairs is joined by an unsubdivided edge. Since \(S\) is induced, there are no edges between interiors of different retained paths or other unwanted edges. The retained graph is therefore an induced subdivision of \(H\). ∎

## 3. The induced-biclique obstruction

The main partial result is stronger than needed in that it only assumes bounded \(\chi_1\).

> **Theorem 1.**  
> For every graph \(H\) and positive integers \(\kappa,r\), there is
> \(C=C(H,\kappa,r)\) such that every graph \(G\) with
> \[
> \chi_1(G)\le\kappa\quad\text{and}\quad \chi(G)>C
> \]
> contains either an induced subdivision of \(H\) or an induced \(K_{r,r}\).

### Proof

Set
\[
s=\kappa(r-1)+1,
\]
and let \(D=D(H,s)\) be supplied by the extremal induced-subdivision lemma. Take
\[
C=\lceil D\rceil+1.
\]

Let \(k=\chi(G)>C\), and choose an inclusion-minimal induced subgraph \(F\) with \(\chi(F)=k\). Then \(F\) is vertex-critical and hence
\[
\delta(F)\ge k-1>D.
\]
In particular, its average degree exceeds \(D\). Also \(\chi_1(F)\le\kappa\).

The extremal lemma gives either an induced subdivision of \(H\) in \(F\), which remains induced in \(G\), or a \(K_{s,s}\) subgraph with parts \(A,B\).

In the latter case, fix \(b\in B\). Since \(A\subseteq N_F(b)\),
\[
\chi(F[A])\le\chi_1(F)\le\kappa.
\]
Thus \(A\) has a stable set \(A'\) of size at least
\[
\left\lceil\frac{s}{\kappa}\right\rceil
=\left\lceil r-1+\frac1\kappa\right\rceil=r.
\]
Similarly, \(B\) has a stable set \(B'\) of size \(r\). All edges between \(A'\) and \(B'\) are present, so
\[
F[A'\cup B']\cong K_{r,r}.
\]
This \(K_{r,r}\) is induced in \(G\). ∎

Since \(\chi_1(G)\le\chi_2(G)\), this gives the following trichotomy in the notation of the conjecture:

> For every \(H,\tau,r\), sufficiently large chromatic number forces an induced subdivision of \(H\), or \(\chi_2(G)>\tau\), or an induced \(K_{r,r}\).

Equivalently, for fixed \(H,\tau,r\), the class of graphs satisfying
\[
\chi_2(G)\le\tau,
\quad
G\text{ has no induced subdivision of }H,
\quad
G\text{ has no induced }K_{r,r}
\]
has bounded chromatic number.

Thus any counterexample family to Conjecture 1.10 must contain induced bicliques of unbounded order.

## 4. Complete-bipartite targets

> **Corollary 2.**  
> Conjecture 1.10 holds when \(J=K_{p,q}\), for all positive \(p,q\).

### Proof

Fix \(\tau\), and put \(r=\max\{p,q\}\). Apply Theorem 1 with \(H=K_{p,q}\) and \(\kappa=\tau\).

If \(\chi_2(G)\le\tau\) and \(\chi(G)\) exceeds the resulting constant, then either \(G\) contains an induced subdivision of \(K_{p,q}\), or it contains an induced \(K_{r,r}\). In the second case, selecting \(p\) vertices from one side and \(q\) from the other gives an induced \(K_{p,q}\), which is itself a subdivision of \(J\). ∎

In fact this special case needs only bounded clique number. Given \(\omega(G)\le\kappa\), choose \(s\) sufficiently large by Ramsey's theorem that each side of any \(K_{s,s}\) subgraph contains a stable set of size \(r\). The same critical-subgraph and extremal argument then gives an induced \(K_{r,r}\). Consequently:

> For every \(p,q,\kappa\), graphs of clique number at most \(\kappa\) and sufficiently large chromatic number contain an induced subdivision of \(K_{p,q}\).

This is stronger than the assertion required by Conjecture 1.10 for complete-bipartite \(J\).

More generally, the same proof works whenever some complete bipartite graph \(K_{p,q}\) is itself a subdivision of \(J\).

## 5. Many pairwise anticomplete bicliques

The biclique obstruction can be iterated.

> **Theorem 3.**  
> For all \(H,\kappa,r,m\), there is \(C_m\) such that if
> \[
> \chi_1(G)\le\kappa,\qquad \chi(G)>C_m,
> \]
> then \(G\) contains either an induced subdivision of \(H\), or an induced copy of
> \[
> mK_{r,r},
> \]
> that is, \(m\) pairwise anticomplete induced copies of \(K_{r,r}\).

### Proof

Let \(C_1=C(H,\kappa,r)\) from Theorem 1. If \(B\cong K_{r,r}\) is induced, then
\[
N_G[B]=\bigcup_{v\in V(B)}N_G[v].
\]
By subadditivity of chromatic number over a union,
\[
\chi\bigl(G[N_G[B]]\bigr)
 \le \sum_{v\in V(B)}\chi(G[N_G[v]])
 \le 2r\kappa.
\]
Consequently,
\[
\chi(G-N_G[B])\ge\chi(G)-2r\kappa.
\]

Taking
\[
C_m=C_1+(m-1)2r\kappa
\]
and inducting on \(m\) proves the claim. At each step delete the closed neighborhood of the biclique obtained; all subsequently found bicliques are therefore anticomplete to it. ∎

One consequence is that Conjecture 1.10 holds for every disjoint union of complete bipartite graphs. Indeed, if
\[
J=K_{p_1,q_1}\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}K_{p_m,q_m},
\]
choose \(r\ge\max_i\{p_i,q_i\}\), apply Theorem 3 with target \(H=J\), and select the required \(K_{p_i,q_i}\) from the \(i\)-th induced \(K_{r,r}\).

## 6. Linear forests and mixed disconnected targets

For completeness, bounded local chromatic number also gives a simple explicit induced-path bound.

> **Induced-path lemma.**  
> If \(\ell\ge3\), \(\chi_1(G)\le\kappa\), and
> \[
> \chi(G)>(\ell-2)\kappa,
> \]
> then \(G\) contains an induced \(P_\ell\).

### Proof

Take a connected component of maximum chromatic number and a vertex \(v_1\) in it. Deleting \(N[v_1]\) costs at most \(\kappa\) colors. Choose a component \(D\) of the remainder with maximum chromatic number. Connectivity gives a vertex \(v_2\in N(v_1)\) with a neighbor in \(D\).

Maintain an induced path \(v_1,\ldots,v_i\) and a connected set \(D\) such that \(D\) is anticomplete to \(v_1,\ldots,v_{i-1}\), while \(v_i\) has a neighbor in \(D\). Delete \(N_D(v_i)\), which costs at most \(\kappa\) colors, choose a maximum-chromatic component \(D'\) of the remainder, and choose \(v_{i+1}\in N_D(v_i)\) adjacent to \(D'\). This preserves the invariant and the path is induced. The strict inequality leaves a nonempty reservoir after \(\ell-2\) such losses, allowing the final vertex to be chosen. ∎

If \(L\) is a linear forest with component orders \(n_1,\ldots,n_a\), an induced path on
\[
n_1+\cdots+n_a+(a-1)
\]
vertices contains an induced copy of \(L\): use consecutive blocks of orders \(n_i\), leaving one omitted vertex between successive blocks.

Combining this observation with Theorem 3 and retaining a high-chromatic remainder after deleting the closed neighborhoods of the bicliques proves the following.

> **Corollary 4.**  
> Conjecture 1.10 holds whenever every component of \(J\) is either:
> 1. a path; or
> 2. a graph \(J_i\) for which some complete bipartite graph \(K_{a_i,b_i}\) is a subdivision of \(J_i\).

Indeed, construct pairwise anticomplete induced bicliques for the components of the second type, deleting their closed neighborhoods at bounded chromatic cost, and then find the required linear forest in the remaining high-chromatic induced subgraph.

## 7. Remaining gap

The reduction does not settle arbitrary \(J\). Its obstruction is genuine:
\[
\chi_2(K_{r,r})=2
\]
for every \(r\), so bounded \(\chi_2\) does not bound the size of an induced biclique. For targets such as \(K_4\), an induced \(K_{r,r}\) does not itself contain an induced subdivision of the target. Iterating the argument only produces pairwise anticomplete bicliques and therefore does not create the required connected topology.

Thus a proof for general \(J\) would need an additional mechanism exploiting how large induced bicliques attach to the remaining high-chromatic part, rather than merely extracting and isolating them.

The supplied source already proves the conjectural conclusion, in the stronger bounded-clique setting, for banana trees and some related multigraphs. The results above are complementary reductions and exact special cases; they do not resolve Conjecture 1.10 in full.