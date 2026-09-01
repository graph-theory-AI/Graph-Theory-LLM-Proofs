```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "A 2019 theorem of Cames van Batenburg, Huynh, Joret, and Raymond gives an O_H(k log(k+1)) vertex Erdős–Pósa bound for every fixed planar H, and taking H to be a grid proves the conjecture.",
  "would_publish": false,
  "caveats": "The deduction is complete but relies on the published planar-minor Erdős–Pósa theorem rather than reproving it; the catalog appears to have missed arXiv:1807.04969."
}
```

# Mathematical writeup

## 1. Relevant later theorem

The conjecture is a consequence of the main result of:

> W. Cames van Batenburg, T. Huynh, G. Joret, and J.-F. Raymond,  
> **A tight Erdős–Pósa function for planar minors**,  
> *Advances in Combinatorics* (2019), arXiv:1807.04969.

Their theorem states, in the form needed here:

**Planar-minor Erdős–Pósa theorem.**  
For every fixed connected planar graph \(H\), there is a constant \(c_H\) such that, for every graph \(G\) and integer \(k\geq 1\), either

1. \(G\) contains \(k\) pairwise vertex-disjoint subgraphs, each containing \(H\) as a minor; or
2. there is \(X\subseteq V(G)\) with
   \[
   |X|\leq c_H k\log(k+1)
   \]
   such that \(G-X\) is \(H\)-minor-free.

Changing the base of the logarithm only changes \(c_H\).

This is the broader planar-\(H\) statement from which the source paper already observed that Conjecture 1.4 would follow.

## 2. Choosing the planar minor

Fix \(r\geq 1\), and let \(H_r\) be the \((r+1)\times(r+1)\) square grid. It is planar and connected, and
\[
\operatorname{tw}(H_r)\geq r.
\]

For completeness, this lower bound follows from the standard grid bramble. If \(n=r+1\), let \(R_i\) and \(C_j\) denote the rows and columns, and consider
\[
\mathcal B=\{R_i\cup C_j:1\leq i,j\leq n\}.
\]
These are connected and pairwise intersecting. Any set of fewer than \(n\) vertices misses some row and some column, hence misses the corresponding member of \(\mathcal B\). Thus \(\mathcal B\) has order at least \(n\), and the bramble characterization of treewidth gives
\[
\operatorname{tw}(H_r)\geq n-1=r.
\]

By the excluded-grid theorem, there is an integer \(b_r\), depending only on \(r\), such that every \(H_r\)-minor-free graph has treewidth at most \(b_r\).

## 3. Treewidth after adding back a vertex set

We use the elementary inequality
\[
\operatorname{tw}(G)\leq \operatorname{tw}(G-X)+|X|.
\]
Indeed, take a tree decomposition of \(G-X\) and add every vertex of \(X\) to every bag. This covers all edges involving \(X\) and increases the width by at most \(|X|\).

## 4. Deduction of the conjecture

Normalize logarithms to base \(2\), and let \(c_r:=c_{H_r}\) be the constant from the planar-minor Erdős–Pósa theorem. Define
\[
f(r):=\left\lceil c_r+b_r+1\right\rceil .
\]

Let \(k\geq1\), and suppose
\[
\operatorname{tw}(G)\geq f(r)\,k\log_2(k+1).
\]

Apply the planar-minor Erdős–Pósa theorem to \(H_r\). If its second outcome holds, then there is a set \(X\) with
\[
|X|\leq c_r k\log_2(k+1)
\]
such that \(G-X\) is \(H_r\)-minor-free. Consequently,
\[
\begin{aligned}
\operatorname{tw}(G)
&\leq \operatorname{tw}(G-X)+|X|\\
&\leq b_r+c_r k\log_2(k+1).
\end{aligned}
\]
Since \(k\log_2(k+1)\geq1\), the definition of \(f(r)\) gives
\[
b_r+c_r k\log_2(k+1)
<
f(r)k\log_2(k+1),
\]
contradicting the assumed lower bound on \(\operatorname{tw}(G)\).

Therefore the first outcome holds: \(G\) has \(k\) pairwise vertex-disjoint subgraphs \(G_1,\dots,G_k\), each containing \(H_r\) as a minor. Treewidth is minor-monotone, so
\[
\operatorname{tw}(G_i)\geq\operatorname{tw}(H_r)\geq r
\qquad (1\leq i\leq k).
\]

This proves the stated conjecture for every \(r,k\geq1\).

## 5. Status and gaps

There is no gap in the deduction from the cited planar-minor Erdős–Pósa theorem. The deep proof of that theorem is not reproduced here. Thus Conjecture 1.4 was open when the 2017/2018 wheel-minor paper was written, but it was subsequently resolved by the 2019 planar-minor result; the supplied catalog status is outdated or incomplete.