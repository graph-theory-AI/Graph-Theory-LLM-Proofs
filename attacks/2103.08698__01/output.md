```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full metatheorem remains open, but weighted vertex cover has a PTAS on every efficiently fractionally treewidth-fragile class via a half-integral LP core.",
  "would_publish": false,
  "caveats": "Only weighted vertex cover and a bounded-rank syntactic fragment are covered; the general monotone FO claims remain open."
}
```

## 1. Statement of the partial result

I use the following standard formulation of efficient fractional treewidth fragility. For every fixed integer \(k\), an algorithm produces a polynomial-size multiset
\[
Z_1,\ldots,Z_m\subseteq V(G)
\]
such that

1. \(\operatorname{tw}(G-Z_i)\le t(k)\) for every \(i\), where \(t(k)\) is independent of \(|G|\); and
2. every vertex belongs to at most \(m/k\) of the sets \(Z_i\).

The equivalent probabilistic formulation is that \(Z\) is sampled from a finite distribution with
\[
\Pr(v\in Z)\le \frac1k
\]
for every vertex, and \(G-Z\) always has treewidth at most \(t(k)\).

The following settles the concrete weighted-vertex-cover case highlighted in the question.

### Theorem 1

Let \(\mathcal C\) be an efficiently fractionally treewidth-fragile graph class. Then minimum-weight vertex cover, with nonnegative rational vertex weights, has a deterministic PTAS on \(\mathcal C\) under the explicit-support definition above.

More precisely, for every integer \(k\), the algorithm returns a vertex cover of weight at most
\[
\left(1+\frac{2}{k}\right)\operatorname{OPT}.
\]

No hereditary assumption on \(\mathcal C\) is needed.

The proof consists of applying the fractional treewidth deletion only after a weighted Nemhauser–Trotter reduction. The resulting residual graph has total vertex weight at most twice its optimum vertex-cover weight, exactly eliminating the “error relative to total weight” obstruction.

---

## 2. A weighted half-integral core lemma

For a weighted graph \((G,w)\), consider the vertex-cover LP
\[
\begin{aligned}
\min\quad &\sum_{v\in V(G)}w(v)x_v,\\
\text{subject to}\quad &x_u+x_v\ge 1 &&(uv\in E(G)),\\
&0\le x_v\le 1 &&(v\in V(G)).
\end{aligned}
\tag{VC-LP}
\]

An optimal basic solution can be chosen half-integral:
\[
x_v\in\left\{0,\frac12,1\right\}.
\]
For completeness, this follows by considering the graph of tight edge constraints on the strictly fractional variables. A bipartite component admits a nonzero alternating perturbation in both directions, contradicting extremality, while an odd cycle of tight equations \(x_u+x_v=1\) forces all values in its component to equal \(1/2\).

Set
\[
V_0=\{v:x_v=0\},\qquad
R=\{v:x_v=1/2\},\qquad
V_1=\{v:x_v=1\},
\]
and let \(H=G[R]\).

### Lemma 2

The partition above satisfies

\[
\tau_w(G)=w(V_1)+\tau_w(H)
\tag{1}
\]
and
\[
w(R)\le 2\tau_w(H),
\tag{2}
\]
where \(\tau_w\) denotes minimum vertex-cover weight.

#### Proof

First, there is no edge from \(V_0\) to \(V_0\cup R\), since such an edge would violate its LP constraint. Thus every neighbor of a vertex in \(V_0\) belongs to \(V_1\).

We prove the persistence assertion underlying (1). Let \(C\) be a minimum-weight vertex cover of \(G\), and put
\[
A=V_1\setminus C,\qquad B=V_0\cap C.
\]
Let
\[
N_0(A)=N(A)\cap V_0.
\]
Since \(C\) omits every vertex of \(A\), it must contain every vertex of \(N_0(A)\), so
\[
N_0(A)\subseteq B.
\tag{3}
\]

Modify \(x\) by lowering every variable in \(A\) from \(1\) to \(1/2\), and raising every variable in \(N_0(A)\) from \(0\) to \(1/2\). This remains LP-feasible:

- an edge from \(A\) to \(V_0\) has both endpoint values \(1/2\);
- an edge from \(A\) to \(R\) has both endpoint values \(1/2\);
- an edge with both endpoints in \(A\) also has sum \(1\);
- all other affected constraints remain satisfied.

Optimality of \(x\) therefore gives
\[
\frac12 w(N_0(A))-\frac12 w(A)\ge 0,
\]
and hence, using (3),
\[
w(A)\le w(N_0(A))\le w(B).
\tag{4}
\]

Now define
\[
C'=(C\setminus B)\cup A.
\]
The set \(C'\) contains all of \(V_1\) and none of \(V_0\). It is still a vertex cover: every edge incident with \(V_0\) has its other endpoint in \(V_1\), and no other edge can be uncovered by removing \(B\). By (4),
\[
w(C')\le w(C).
\]
Thus there is a minimum vertex cover containing \(V_1\) and avoiding \(V_0\).

Consequently, its intersection with \(R\) covers \(H\), proving
\[
\tau_w(G)\ge w(V_1)+\tau_w(H).
\]
Conversely, \(V_1\) together with any vertex cover of \(H\) covers all of \(G\), proving equality (1).

Finally, the all-\(1/2\) solution on \(H\) is optimal for the vertex-cover LP of \(H\). Otherwise, a better fractional solution on \(H\), combined with values \(0\) on \(V_0\) and \(1\) on \(V_1\), would improve the original LP solution. Therefore
\[
\operatorname{LP}(H)=\frac12 w(R).
\]
Since the LP is a lower bound on the integral optimum,
\[
\frac12 w(R)\le \tau_w(H),
\]
which is (2). ∎

---

## 3. PTAS algorithm

Fix \(\varepsilon>0\) and choose
\[
k=\left\lceil\frac{2}{\varepsilon}\right\rceil.
\]

Given \((G,w)\), perform the following steps.

1. Compute an optimal basic solution of (VC-LP), and obtain \(V_0,R,V_1\) and \(H=G[R]\).
2. Run the fractional treewidth-fragility algorithm on the original graph \(G\), obtaining \(Z_1,\ldots,Z_m\).
3. Put
   \[
   X_i=Z_i\cap R.
   \]
   Because every vertex lies in at most \(m/k\) deletion sets,
   \[
   \frac1m\sum_{i=1}^m w(X_i)
   \le \frac{w(R)}{k}.
   \]
   Hence an index \(i\) minimizing \(w(X_i)\) satisfies
   \[
   w(X_i)\le \frac{w(R)}{k}.
   \tag{5}
   \]
4. Since
   \[
   H-X_i=G[R\setminus Z_i]
   \]
   is an induced subgraph of \(G-Z_i\), it has treewidth at most \(t(k)\).
5. Compute an exact minimum-weight vertex cover \(D_i\) of \(H-X_i\) by dynamic programming on a bounded-width tree decomposition.
6. Return
   \[
   K=V_1\cup X_i\cup D_i.
   \]

### Feasibility

All edges incident with \(V_0\) have their other endpoint in \(V_1\). All other edges outside \(H\) are also covered by \(V_1\). Within \(H\), every edge incident with \(X_i\) is covered by \(X_i\), and every remaining edge is covered by \(D_i\). Thus \(K\) is a vertex cover of \(G\).

### Approximation guarantee

Let \(C_H^\star\) be a minimum-weight vertex cover of \(H\). Then
\[
C_H^\star\setminus X_i
\]
is a vertex cover of \(H-X_i\). Therefore
\[
w(D_i)\le w(C_H^\star\setminus X_i)\le \tau_w(H).
\]
Using (5) and Lemma 2,
\[
\begin{aligned}
w(X_i)+w(D_i)
&\le \frac{w(R)}{k}+\tau_w(H)\\
&\le \left(1+\frac{2}{k}\right)\tau_w(H).
\end{aligned}
\]
Together with the exact decomposition (1),
\[
\begin{aligned}
w(K)
&\le w(V_1)+\left(1+\frac{2}{k}\right)\tau_w(H)\\
&\le \left(1+\frac{2}{k}\right)
   \bigl(w(V_1)+\tau_w(H)\bigr)\\
&=\left(1+\frac{2}{k}\right)\tau_w(G)\\
&\le (1+\varepsilon)\tau_w(G).
\end{aligned}
\]

For fixed \(\varepsilon\), the number \(t(k)\) is constant. Weighted vertex cover on a graph of treewidth \(t(k)\) is solvable exactly in polynomial time, for example with \(2^{O(t(k))}\) states per bag. Thus the overall algorithm is a PTAS.

If efficient fractional fragility is supplied only by a sampler rather than an explicit polynomial-size support, the same proof gives a randomized PTAS by sampling repeatedly and taking the best candidate.

---

## 4. A constant-factor fragment of the first question

There is also a straightforward positive answer for a substantial syntactic subclass of monotone FO minimization formulas.

### Proposition 3

Suppose the feasibility formula is a fixed conjunction of formulas of the form
\[
\forall x_1\cdots x_q\,
\left(
\theta(x_1,\ldots,x_q)
\longrightarrow
\bigvee_{i\in I} S(x_i)
\right),
\tag{6}
\]
where \(\theta\) does not use the solution predicate \(S\), and every set \(I\) has size at most \(r\). Then the corresponding weighted minimization problem has an \(r\)-approximation on arbitrary graphs.

#### Proof

For every tuple satisfying \(\theta\), form the hyperedge
\[
e=\{x_i:i\in I\}.
\]
The feasible sets \(S\) are exactly the hitting sets of this rank-\(r\) hypergraph. There are polynomially many tuples because the formula and its arity are fixed.

Solve the standard hitting-set LP
\[
\min \sum_v w(v)x_v,\qquad
\sum_{v\in e}x_v\ge1\quad(e\in\mathcal E),\qquad x_v\ge0.
\]
Return
\[
S=\{v:x_v\ge1/r\}.
\]
Every hyperedge of size at most \(r\) contains such a vertex, and
\[
w(S)\le r\sum_v w(v)x_v\le r\,\operatorname{OPT}.
\]
∎

This covers vertex cover, fixed-pattern vertex transversals, and other bounded-rank universal covering formulas. It does not use bounded expansion.

---

## 5. What remains open

The proof does not establish either full metatheorem.

1. General semantically monotone FO formulas need not have the bounded-rank universal form (6). Dominating set, for example, has an existential selected witness ranging over an unbounded neighborhood.
2. The weighted vertex-cover PTAS relies crucially on the exact persistence identity
   \[
   \tau_w(G)=w(V_1)+\tau_w(H)
   \]
   and the balanced-core bound
   \[
   w(V(H))\le2\tau_w(H).
   \]
   No comparable lossless balanced-core theorem is proved here for arbitrary monotone FO minimization.
3. Fractional treewidth deletion by itself only yields an additive loss of order \(w(V)/k\). The LP core is precisely what converts that loss into \(O(\operatorname{OPT}/k)\); without such a core, the original obstruction remains.
4. Thus the constant-factor question for all monotone FO minimization problems on bounded-expansion classes, and the PTAS question for all such problems on efficiently fractionally treewidth-fragile classes, remain unresolved.

The argument is self-contained, but I have not independently verified whether this short weighted-vertex-cover observation has appeared elsewhere. Under the catalog's stated literature status, it would settle the highlighted concrete special case.