```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A switching argument proves BEC when G1 is k-degenerate and (k−1)Δ(G2)≤Δ(G1), and yields a stronger degree-sequence criterion.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved, and no novelty claim is made for these elementary sufficient conditions."
}
```

## 1. Partial result

All graphs below are finite, simple, and have the same order \(n\). Packing means finding a bijection under which no edge of one graph is an edge of the other.

Write
\[
d=\Delta(G),\qquad r=\Delta(H).
\]
Since the parameters are integers, the BEC hypothesis is exactly
\[
n\ge (d+1)(r+1).
\]

Recall that \(G\) is **\(k\)-degenerate** if every nonempty subgraph has a vertex of degree at most \(k\).

I prove the following restricted case.

**Corollary (BEC with a degeneracy hypothesis).**  
Suppose \(G\) is \(k\)-degenerate and
\[
(k-1)r\le d.
\]
Then the BEC hypothesis implies that \(G\) and \(H\) pack.

In particular, this proves BEC for:

- a forest paired with an arbitrary graph;
- a pair in which a graph of maximum degree at least that of the other is \(2\)-degenerate;
- any two \(2\)-degenerate graphs.

The proof gives a more general, degree-sequence-sensitive packing condition. These are self-contained partial results; I have not established their novelty.

## 2. A one-conflict switching lemma

Place two graphs \(R,B\) on the same vertex set, thinking of their edges as red and blue.

**Lemma.** Suppose
\[
E(R)\cap E(B)=\{uv\}.
\]
Define
\[
L(u)=
\sum_{a\in N_R(u)}d_B(a)
+
\sum_{b\in N_B(u)}d_R(b).
\]
If \(n>L(u)\), then exchanging the red labels of \(u\) and a suitable vertex produces a packing.

**Proof.** Set
\[
A=\bigcup_{a\in N_R(u)}N_B(a),
\qquad
C=\bigcup_{b\in N_B(u)}N_R(b).
\]
Because \(uv\) is both red and blue, \(u\in A\cap C\). Consequently,
\[
\begin{aligned}
|A\cup C\cup\{v\}|
&\le |A|+|C|\\
&\le
\sum_{a\in N_R(u)}d_B(a)
+
\sum_{b\in N_B(u)}d_R(b)
=L(u).
\end{aligned}
\]
Choose
\[
x\notin A\cup C\cup\{v\}.
\]
In particular, \(x\ne u,v\). Exchange \(u\) and \(x\) in the red graph, leaving the blue graph fixed.

We check every type of red edge.

1. A red edge incident with neither \(u\) nor \(x\) is unchanged and was not the unique conflict.
2. A red edge \(ua\), with \(a\ne x\), becomes \(xa\). This is not blue because \(x\notin A\).
3. A red edge \(xb\), with \(b\ne u\), becomes \(ub\). If \(ub\) were blue, then
   \[
   x\in N_R(b)\subseteq C,
   \]
   contrary to the choice of \(x\).
4. If \(ux\) is red, it remains the same edge. It was not blue, because \(x\ne v\).

Thus no conflict remains. \(\square\)

The exclusion of \(v\) matters: exchanging the endpoints of the conflicting edge would leave that edge in place. The common vertex \(u\in A\cap C\) pays exactly for this additional exclusion.

## 3. A degree-sequence packing theorem

For a graph \(J\), let
\[
s_t(J)=\text{the sum of its \(t\) largest vertex degrees},
\qquad s_0(J)=0.
\]

**Theorem.** Suppose \(G\) is \(k\)-degenerate and \(r=\Delta(H)\). If
\[
\boxed{\quad n>s_k(H)+s_r(G),\quad} \tag{1}
\]
then \(G\) and \(H\) pack.

In particular, since
\[
s_k(H)\le kr,\qquad s_r(G)\le rd,
\]
the simpler condition
\[
\boxed{\quad n>(d+k)r\quad} \tag{2}
\]
suffices.

**Proof.** Induct on \(|E(G)|\), keeping \(H\), \(n\), and \(k\) fixed.

If \(G\) is edgeless, there is nothing to prove. Otherwise, \(G\) has a vertex \(u\) with
\[
1\le d_G(u)\le k.
\]
Indeed, apply degeneracy to the subgraph induced by the non-isolated vertices.

Choose an edge \(uv\). Deleting this edge preserves \(k\)-degeneracy and cannot increase \(s_r(G)\). Therefore the induction hypothesis gives a packing of \(G-uv\) with \(H\).

Restore \(uv\). If it does not conflict, we are done. Otherwise, after identifying the vertex sets through the packing, \(uv\) is the unique common edge. At its endpoint \(u\),
\[
\begin{aligned}
L(u)
&=
\sum_{a\in N_G(u)}d_H(a)
+
\sum_{b\in N_H(u)}d_G(b)\\
&\le s_k(H)+s_r(G)
<n.
\end{aligned}
\]
The switching lemma repairs the conflict. This completes the induction. \(\square\)

This proof is constructive. Repeatedly delete an edge incident with a vertex of positive degree at most \(k\), then restore the edges in reverse order. Each restored edge requires at most one transposition. A straightforward adjacency-matrix implementation is polynomial-time.

### Deriving the stated BEC special case

Assume
\[
n\ge(d+1)(r+1)
\quad\text{and}\quad
(k-1)r\le d.
\]
Then
\[
\begin{aligned}
n-(d+k)r
&\ge (d+1)(r+1)-(d+k)r\\
&=d+1-(k-1)r\\
&\ge1.
\end{aligned}
\]
Thus (2) applies.

For a forest, take \(k=1\). For a \(2\)-degenerate graph with \(d\ge r\), take \(k=2\). If both graphs are \(2\)-degenerate, designate one with larger maximum degree as \(G\).

## 4. A stronger core-sensitive criterion

The preceding proof can be sharpened when the high-degeneracy portions of \(G\) have smaller degrees than \(G\) as a whole.

Let \(C_t(G)\) denote the \(t\)-core of \(G\): the graph obtained by repeatedly deleting vertices of degree less than \(t\). When taking degree sums, pad it with isolated vertices to order \(n\).

For nonempty \(G\), define
\[
P(G,H)=
\max_{\substack{t\ge1\\C_t(G)\ne\varnothing}}
\left\{s_t(H)+s_r(C_t(G))\right\},
\qquad r=\Delta(H).
\]

**Proposition.** If
\[
\boxed{\quad n>P(G,H),\quad} \tag{3}
\]
then \(G\) and \(H\) pack.

Moreover, if \(G\) is \(k\)-degenerate, then
\[
P(G,H)\le s_k(H)+s_r(G),
\]
so (3) is at least as strong as (1).

**Proof.** Suppose otherwise. Choose a spanning subgraph \(F\subseteq G\) with the fewest edges such that \(F\) does not pack with \(H\). It has an edge.

Let \(u\) have minimum positive degree in \(F\), and put
\[
t=d_F(u).
\]
The subgraph of \(F\) on its non-isolated vertices has minimum degree \(t\). Its vertices therefore all belong to \(C_t(G)\): none can be removed during the iterative deletion defining that core. In particular, after padding with isolates,
\[
F\subseteq C_t(G).
\]

Choose \(uv\in E(F)\). By minimality, \(F-uv\) packs with \(H\); restoring \(uv\) creates exactly one conflict. Since \(F\) does not pack, the switching lemma forces
\[
\begin{aligned}
n
&\le L(u)\\
&\le s_t(H)+s_r(F)\\
&\le s_t(H)+s_r(C_t(G))\\
&\le P(G,H),
\end{aligned}
\]
a contradiction.

Finally, nonempty cores have \(t\le k\), and \(C_t(G)\subseteq G\), giving the asserted comparison. \(\square\)

Thus the attack yields a computable sufficient condition involving the degree sequences of all nonempty cores, rather than only the two maximum degrees.

## 5. Boundary examples and the unresolved gap

### The strict inequality in the auxiliary bound is necessary

Let \(1\le k\le d\) be odd, and take
\[
G=K_{k,d},\qquad n=k+d,
\]
with \(H\) a perfect matching on the same number of vertices.

Here \(G\) is \(k\)-degenerate, \(\Delta(G)=d\), and \(r=1\), so
\[
s_k(H)+s_r(G)=k+d=n.
\]
Nevertheless, the graphs do not pack: the complement of \(G\) is
\[
K_k\;\dot\cup\;K_d,
\]
which has no perfect matching because both components have odd order.

These are **not** counterexamples to BEC. Indeed,
\[
n=k+d\le2d<2(d+1)=(d+1)(r+1).
\]
They only show that the strict inequality in the auxiliary theorem cannot generally be replaced by a non-strict one.

### What a minimal BEC counterexample must survive

The same switching lemma gives a useful obstruction restriction. Suppose a BEC counterexample exists, and delete edges from either graph until the pair is edge-minimal nonpackable. Continue to write its maximum degrees as \(d,r>0\).

For every non-isolated vertex \(u\in V(G)\), deleting an incident edge and restoring it after packing gives
\[
n\le r\bigl(d_G(u)+d\bigr).
\]
Hence
\[
d_G(u)
\ge \left\lceil\frac nr\right\rceil-d
\ge \left\lfloor\frac dr\right\rfloor+2.
\]
Symmetrically, every non-isolated \(v\in V(H)\) satisfies
\[
d_H(v)\ge \left\lfloor\frac rd\right\rfloor+2.
\]
In particular, when \(d=r\), an edge-minimal counterexample has no vertices of degree \(1\) or \(2\), apart from isolated vertices.

### The main gap remains

For two \(d\)-regular graphs, the degree-sequence criterion—and also its core-sensitive refinement—reduces to
\[
n>2d^2.
\]
BEC asks only for
\[
n\ge(d+1)^2.
\]
Thus, for \(d\ge3\), this argument leaves the central range
\[
(d+1)^2\le n\le2d^2
\]
untouched for regular pairs.

The proved result is therefore a genuine restricted packing theorem, not a proof of unrestricted BEC. The obstruction is explicit: the one-transposition count still pays for two essentially separate families of alternating two-edge paths in the high-degeneracy, near-regular regime.