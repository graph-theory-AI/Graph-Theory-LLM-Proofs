```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Weighted Vertex Cover has a PTAS on every effectively fractionally treewidth-fragile class via a half-integral LP core and thin bounded-treewidth deletions, but the PTAS extension to all hereditary sublinear-separator classes remains open.",
  "would_publish": false,
  "caveats": "The algorithm requires efficiently obtainable fragility distributions; the argument is specific to Vertex Cover and transfers only a QPTAS in the broader separator setting."
}
```

# Mathematical writeup

## 1. Result established

All vertex weights below are nonnegative rationals.

### Theorem
Let \(\mathcal C\) be an effectively fractionally treewidth-fragile graph class, in the following standard algorithmic sense: for every integer \(a\ge 1\), there is a constant \(t(a)\) and a polynomial-time algorithm, for fixed \(a\), which on \(G\in\mathcal C\) produces a finite distribution
\[
\{(X_i,p_i):i\in[m]\}
\]
and tree decompositions of \(G-X_i\), such that

\[
\operatorname{tw}(G-X_i)\le t(a)
\]
for every \(i\), and
\[
\sum_{i:v\in X_i}p_i\le \frac1a
\]
for every \(v\in V(G)\).

Then weighted Minimum Vertex Cover has a PTAS on \(\mathcal C\).

The proof is based on the half-integral vertex-cover LP. The preprocessing is essential: it removes precisely the part of the graph on which approximating a complementary independent set would give no relative control on the cover cost.

---

## 2. The half-integral LP core

For a weighted graph \((G,w)\), write
\[
\tau_w(G)=\min\{w(C):C\text{ is a vertex cover of }G\}
\]
and
\[
\alpha_w(G)=\max\{w(I):I\text{ is an independent set of }G\}.
\]
Since complementation is a bijection between vertex covers and independent sets,
\[
\tau_w(G)+\alpha_w(G)=w(V(G)).
\tag{1}
\]

Consider the standard LP
\[
\begin{aligned}
\min \quad &\sum_{v\in V(G)}w(v)x_v,\\
\text{subject to}\quad &x_u+x_v\ge 1 &&(uv\in E(G)),\\
&0\le x_v\le 1 &&(v\in V(G)).
\end{aligned}
\tag{VC-LP}
\]

The upper bounds are harmless because weights are nonnegative.

### Lemma 1: LP kernel
There is an optimal half-integral solution \(x\in\{0,\tfrac12,1\}^{V(G)}\). Define
\[
P=\{v:x_v=1\},\qquad
R=\{v:x_v=\tfrac12\},\qquad
Z=\{v:x_v=0\},
\]
and let \(H=G[R]\). Then:

1. every neighbor of a vertex in \(Z\) lies in \(P\);
2. \[
   \tau_w(G)=w(P)+\tau_w(H);
   \tag{2}
   \]
3. the all-\(\tfrac12\) vector is an optimum of (VC-LP) on \(H\), and consequently
   \[
   \alpha_w(H)\le \tau_w(H).
   \tag{3}
   \]

#### Proof

First choose an optimal extreme point \(x\) of (VC-LP). For completeness, half-integrality follows by the usual perturbation argument. Let \(F=\{v:0<x_v<1\}\), and form the graph on \(F\) consisting of the tight edges \(uv\) with \(x_u+x_v=1\). If a component of this graph were bipartite, increasing \(x\) slightly on one side and decreasing it on the other, or vice versa, would preserve all tight constraints and, for sufficiently small perturbation, all remaining constraints. This contradicts extremality. Thus every component contains an odd cycle; the equations \(x_u+x_v=1\) around an odd cycle force every coordinate in the component to equal \(\tfrac12\). Hence \(x\) is half-integral.

Assertion 1 follows immediately from feasibility: if \(x_z=0\) and \(zu\in E(G)\), then \(x_u\ge1\), hence \(u\in P\).

We next prove the weighted persistency statement needed for (2). Let \(C\) be any integral vertex cover. Define another fractional vector \(y\) from \(x\) by changing

- \(x_v=1\) to \(y_v=\tfrac12\) when \(v\notin C\);
- \(x_v=0\) to \(y_v=\tfrac12\) when \(v\in C\);

and leaving every other coordinate unchanged.

This vector is feasible. Indeed, the only decreases occur at vertices in \(P\setminus C\). Since \(C\) is a vertex cover, every neighbor \(u\) of such a vertex belongs to \(C\). If \(u\in Z\), its coordinate was increased to \(\tfrac12\); if \(u\in R\), its coordinate is already \(\tfrac12\); and if \(u\in P\), its coordinate remains \(1\). Thus every edge incident with a decreased coordinate still has endpoint sum at least \(1\).

Since \(x\) is LP-optimal,
\[
0\le w(y)-w(x)
 =\frac12\bigl(w(Z\cap C)-w(P\setminus C)\bigr),
\]
and therefore
\[
w(P\setminus C)\le w(Z\cap C).
\tag{4}
\]

Now set
\[
C' = P\cup(C\cap R).
\]
This is a vertex cover: edges incident with \(P\) are covered; every edge incident with \(Z\) has its other endpoint in \(P\); and an edge inside \(R\) is covered by \(C\cap R\). Moreover, by (4),
\[
w(C')-w(C)=w(P\setminus C)-w(Z\cap C)\le0.
\tag{5}
\]

Applying this to a minimum vertex cover shows that there is an optimum containing \(P\), avoiding \(Z\), and whose remaining part is a vertex cover of \(H\). Conversely, \(P\) together with any vertex cover of \(H\) covers \(G\). This proves (2).

Finally, the all-\(\tfrac12\) solution on \(H\) has value \(w(R)/2\). If \(H\) had a fractional vertex cover of smaller value, extending it by assigning \(1\) on \(P\) and \(0\) on \(Z\) would give an LP solution for \(G\) cheaper than \(x\). Thus
\[
\operatorname{LP}(H)=\frac{w(R)}2.
\]
Hence
\[
\tau_w(H)\ge\frac{w(R)}2.
\]
Using (1),
\[
\alpha_w(H)
 =w(R)-\tau_w(H)
 \le\frac{w(R)}2
 \le\tau_w(H),
\]
which proves (3). \(\square\)

---

## 3. Black-box transfer from independent set

Lemma 1 gives the following useful reduction.

### Proposition 2
Suppose that, on the induced graph \(H\) from Lemma 1, one can find an independent set \(I\) satisfying
\[
w(I)\ge(1-\delta)\alpha_w(H).
\]
Then
\[
C=P\cup(R\setminus I)
\]
is a vertex cover of \(G\) with
\[
w(C)\le(1+\delta)\tau_w(G).
\]

#### Proof
The set \(R\setminus I\) covers \(H\), so Lemma 1 shows that \(C\) covers \(G\). Moreover,
\[
\begin{aligned}
w(R\setminus I)
&\le w(R)-(1-\delta)\alpha_w(H)\\
&=\tau_w(H)+\delta\alpha_w(H)\\
&\le(1+\delta)\tau_w(H),
\end{aligned}
\]
where the last inequality is (3). Therefore
\[
\begin{aligned}
w(C)
&\le w(P)+(1+\delta)\tau_w(H)\\
&\le(1+\delta)\bigl(w(P)+\tau_w(H)\bigr)\\
&=(1+\delta)\tau_w(G).
\end{aligned}
\]
\(\square\)

Without the LP preprocessing, this argument would fail because \(\alpha_w(G)\) can be arbitrarily larger than \(\tau_w(G)\). The all-half LP core guarantees exactly the missing inequality \(\alpha_w(H)\le\tau_w(H)\).

---

## 4. Applying fractional treewidth fragility

Fix \(0<\varepsilon<1\), and set
\[
a=\left\lceil\frac1\varepsilon\right\rceil.
\]

Compute the LP core \(H=G[R]\). Obtain an \(a\)-thin distribution \((X_i,p_i)\) for \(G\). Put
\[
Y_i=X_i\cap R.
\]
Then
\[
H-Y_i=G[R\setminus X_i]
\]
is an induced subgraph of \(G-X_i\), so
\[
\operatorname{tw}(H-Y_i)\le t(a).
\]

For every \(i\), compute an exact maximum-weight independent set \(I_i\) in \(H-Y_i\) by bounded-treewidth dynamic programming, and let \(I\) be the heaviest among the \(I_i\).

Let \(I^\star\) be a maximum-weight independent set of \(H\). By thinness,
\[
\begin{aligned}
\mathbb E_i[w(I^\star\cap Y_i)]
&=\sum_{v\in I^\star}w(v)\Pr(v\in X_i)\\
&\le\frac1a w(I^\star)
 =\frac1a\alpha_w(H).
\end{aligned}
\]
Consequently, for some \(i\),
\[
w(I^\star\cap Y_i)\le\frac1a\alpha_w(H).
\]
For this \(i\), \(I^\star\setminus Y_i\) is an independent set of \(H-Y_i\), and hence
\[
\begin{aligned}
w(I_i)
&\ge w(I^\star\setminus Y_i)\\
&\ge\left(1-\frac1a\right)\alpha_w(H).
\end{aligned}
\]
The best computed set \(I\) satisfies the same bound. Proposition 2, with \(\delta=1/a\le\varepsilon\), now gives
\[
w\bigl(P\cup(R\setminus I)\bigr)
 \le(1+\varepsilon)\tau_w(G).
\]

For fixed \(\varepsilon\), the width \(t(a)\) is constant. If the support of the fragility distribution and the associated decompositions are obtainable in polynomial time, the total running time is polynomial. This is a PTAS.

Notice that heredity of the class is not needed here: the fragility witness is computed for \(G\), and \(H-Y_i\) is simply an induced subgraph of \(G-X_i\).

---

## 5. Consequence for hereditary classes with sublinear separators

Proposition 2 also gives the following unconditional algorithmic transfer.

### Corollary 3
Let \(\mathcal C\) be hereditary. If maximum-weight independent set has a PTAS, respectively a QPTAS, on \(\mathcal C\), then weighted Minimum Vertex Cover has a PTAS, respectively a QPTAS, on \(\mathcal C\).

Indeed, the LP core \(H\) is an induced subgraph of \(G\), hence \(H\in\mathcal C\), and Proposition 2 preserves the approximation parameter without asymptotic runtime loss.

Thus, under the weighted-objective hypotheses of the maximization metatheorem stated in the source paper, its QPTAS for hereditary classes with sublinear separators transfers to weighted Vertex Cover. It does not, however, turn that QPTAS into a PTAS.

---

## 6. What remains open

The argument settles the concrete weighted Vertex Cover question for effectively fractionally treewidth-fragile classes. It does not settle:

1. whether every hereditary class with sublinear separators admits a PTAS for weighted Vertex Cover;
2. whether fractional treewidth fragility suffices for arbitrary distance-\(1\) minimization problems;
3. the purely existential formulation in which fractional-fragility distributions are not algorithmically obtainable.

The broader separator setting lacks the per-vertex thinness used in the expectation argument: a separator of sublinear cardinality can still carry an arbitrarily large fraction of the total weight. The LP core controls the global relation \(\alpha_w(H)\le\tau_w(H)\), but by itself does not produce the weighted thin decompositions needed for a PTAS.

I have not verified whether this short LP reduction has already appeared elsewhere, so the argument establishes the mathematical implication but not a novelty claim suitable for publication.