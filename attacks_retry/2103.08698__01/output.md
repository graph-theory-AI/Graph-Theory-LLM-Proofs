```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The weighted vertex-cover PTAS is valid and extends to every fixed FO-definable binary covering problem, but the unrestricted FO minimization conjecture is not resolved.",
  "would_publish": false,
  "caveats": "Explicit-support efficient fragility is assumed; only special cases are proved, and their novelty has not been independently checked."
}
```

# 1. Results obtained

I checked the half-integral core argument in the supplied attempt; it is correct. Its approximation guarantee can be improved from \(1+2/k\) to \(1+1/k\). More importantly, combining that core argument with the **maximization theorem stated in the question** gives the following extension.

### Theorem A — FO-definable binary covering

Fix an FO formula \(\theta(x,y)\) not using the solution predicate \(S\). On every efficiently fractionally treewidth-fragile class, the problem
\[
\min w(S)
\quad\text{subject to}\quad
G\models
\forall x\,\forall y\,
\bigl(\theta(x,y)\longrightarrow(S(x)\lor S(y))\bigr)
\tag{1}
\]
has a PTAS for nonnegative rational vertex weights.

The relation defined by \(\theta\) need not be adjacency, symmetric, or local. In particular, its associated conflict graph need not itself be sparse or fractionally treewidth-fragile.

I also obtain two other, separate fragments:

* On bounded-maximum-degree efficiently fractionally treewidth-fragile classes, **all bounded-radius monotone local covering problems** have a PTAS.
* Weighted dominating set has an elementary \((4d+2)\)-approximation on \(d\)-degenerate graphs, and hence a constant-factor approximation on every bounded-expansion class.

These statements do **not** establish either full metatheorem in the question. I give complete arguments for the stated fragments below and distinguish their limitations at the end.

---

# 2. Efficient fractional fragility

I use the following explicit-support formulation. For each fixed positive integer \(k\), a polynomial-time algorithm, given \(G\in\mathcal C\), produces a polynomial-size distribution
\[
\{(p_i,Z_i):1\le i\le m\}
\]
such that
\[
\sum_i p_i=1,\qquad
\sum_{i:v\in Z_i}p_i\le \frac1k
\quad(v\in V(G)),
\tag{2}
\]
and
\[
\operatorname{tw}(G-Z_i)\le t(k),
\tag{3}
\]
where \(t(k)\) is independent of \(G\).

All algorithms below using fragility are polynomial-time for fixed accuracy. No hereditary assumption on \(\mathcal C\) is needed: the fragility algorithm is always run on the original input graph.

Weights are nonnegative rationals, encoded in binary.

---

# 3. The weighted vertex-cover core

Write \(\tau_w(G)\) for minimum vertex-cover weight and \(w(A)=\sum_{v\in A}w(v)\).

Consider
\[
\begin{aligned}
\min\quad &\sum_v w(v)x_v,\\
\text{subject to}\quad
&x_u+x_v\ge 1 &&(uv\in E(G)),\\
&0\le x_v\le 1 &&(v\in V(G)).
\end{aligned}
\tag{VC-LP}
\]

An optimal basic solution is half-integral. Here is the usual short justification. Form the graph of tight edge constraints on strictly fractional variables. A bipartite component permits a sufficiently small alternating perturbation in both directions, contradicting extremality. Every nonbipartite component contains an odd cycle of equations \(x_u+x_v=1\), forcing all variables in that component to equal \(1/2\).

Thus, in polynomial time, we obtain an optimal solution with values in
\(\{0,\frac12,1\}\). Put
\[
V_0=\{v:x_v=0\},\qquad
R=\{v:x_v=1/2\},\qquad
V_1=\{v:x_v=1\},
\]
and let \(H=G[R]\).

### Lemma 1 — Exact persistence and weight balance

The partition satisfies
\[
\tau_w(G)=w(V_1)+\tau_w(H)
\tag{4}
\]
and
\[
w(R)\le 2\tau_w(H).
\tag{5}
\]

### Proof

LP feasibility implies that there is no edge from \(V_0\) to \(V_0\cup R\).

Let \(C\) be an optimal vertex cover, and define
\[
A=V_1\setminus C,\qquad
B=V_0\cap C,\qquad
N_0(A)=N(A)\cap V_0.
\]
Because \(C\) omits \(A\),
\[
N_0(A)\subseteq B.
\tag{6}
\]

Modify the LP solution by lowering variables in \(A\) from \(1\) to \(1/2\), and raising variables in \(N_0(A)\) from \(0\) to \(1/2\). This remains feasible:

* edges from \(A\) to \(V_0\) now have both endpoint values \(1/2\);
* edges from \(A\) to \(R\), or within \(A\), have endpoint sum \(1\);
* edges from \(A\) to \(V_1\setminus A\) remain satisfied;
* increasing other variables cannot violate a covering constraint.

Optimality of the original LP solution gives
\[
w(A)\le w(N_0(A))\le w(B).
\tag{7}
\]

Consequently,
\[
C'=(C\setminus B)\cup A
\]
has weight at most \(w(C)\). It contains all of \(V_1\), avoids \(V_0\), and remains a vertex cover: every edge incident with \(V_0\) has its other endpoint in \(V_1\), and removing \(B\) affects no other edges.

There is therefore an optimum containing \(V_1\) and avoiding \(V_0\). Conversely, \(V_1\) together with any vertex cover of \(H\) covers \(G\). This proves (4).

Finally, the all-\(1/2\) assignment on \(H\) is LP-optimal. A better fractional assignment on \(H\), extended by \(0\) on \(V_0\) and \(1\) on \(V_1\), would improve the original LP solution. Hence
\[
\operatorname{LP}(H)=\frac12w(R)\le \tau_w(H),
\]
proving (5). ∎

The lemma includes zero-weight vertices. In particular, it does not require division by the optimum.

---

# 4. A direct vertex-cover PTAS, with factor \(1+1/k\)

### Theorem 2

Under (2)–(3), weighted vertex cover has a deterministic approximation algorithm with guarantee
\[
1+\frac1k.
\]

### Algorithm

1. Compute \(V_0,R,V_1\) and \(H=G[R]\) as above.
2. Obtain the fragility distribution for the original graph \(G\).
3. For each support member, put
   \[
   X_i=Z_i\cap R.
   \]
4. Compute an exact minimum-weight vertex cover \(D_i\) of \(H-X_i\).
5. Return the lightest set
   \[
   K_i=V_1\cup X_i\cup D_i.
   \tag{8}
   \]

Since \(H-X_i\) is an induced subgraph of \(G-Z_i\), its treewidth is at most \(t(k)\). The exact computation in step 4 is therefore polynomial-time for fixed \(k\), using a tree decomposition and standard weighted vertex-cover dynamic programming.

Every \(K_i\) is a vertex cover.

### Approximation analysis

Fix an optimal cover \(C_H^\star\) of \(H\). Its restriction to \(H-X_i\) is feasible, so
\[
w(D_i)\le w(C_H^\star\setminus X_i).
\]
Thus
\[
\begin{aligned}
w(K_i)
&\le w(V_1)+w(X_i)+w(C_H^\star\setminus X_i)\\
&=w(V_1)+\tau_w(H)+w(X_i\setminus C_H^\star).
\end{aligned}
\tag{9}
\]

Taking the average under the fragility distribution,
\[
\begin{aligned}
\sum_i p_iw(K_i)
&\le w(V_1)+\tau_w(H)
  +\frac{w(R\setminus C_H^\star)}{k}\\
&=w(V_1)+\tau_w(H)
  +\frac{w(R)-\tau_w(H)}{k}\\
&\le w(V_1)+\left(1+\frac1k\right)\tau_w(H)\\
&\le \left(1+\frac1k\right)\tau_w(G).
\end{aligned}
\tag{10}
\]
The third line uses (5), and the last uses (4) and nonnegative weights.

The minimum candidate is no heavier than this average. Choosing
\[
k=\left\lceil\frac1\varepsilon\right\rceil
\]
gives a PTAS. If the optimum is zero, (10) still proves that the returned solution has weight zero.

The improvement over the supplied attempt is that we minimize the **actual candidate cost**, rather than first minimizing \(w(X_i)\). Only deleted vertices outside a fixed optimum constitute overhead in (9).

### Sampler-only variant

If fragility is supplied only by an efficient sampler, choose \(k\ge 2/\varepsilon\). The nonnegative excess \(w(K_Z)-\tau_w(G)\) has expectation at most \(\tau_w(G)/k\). For positive optimum, Markov's inequality gives success probability at least \(1/2\) for a \((1+\varepsilon)\)-approximation. Independent repetition amplifies this probability. Zero optimum is again handled exactly almost surely.

Thus the deterministic conclusion specifically uses explicit support.

---

# 5. Proof of Theorem A: transfer to FO-definable binary covering

The key point is that the LP core may be computed in a **dense conflict graph**, while the maximization algorithm still runs on the original sparse graph.

Fix \(\theta(x,y)\) as in (1). Define the forced set
\[
F=\{v\in V(G):G\models\theta(v,v)\}.
\]
Every feasible \(S\) must contain \(F\).

On \(U=V(G)\setminus F\), construct the simple graph \(Q\) whose edges are the unordered pairs of distinct vertices satisfying
\[
G\models\theta(u,v)\lor\theta(v,u).
\]
Then (1) is equivalent to
\[
F\subseteq S
\quad\text{and}\quad
S\cap U\text{ is a vertex cover of }Q.
\]
In particular,
\[
\operatorname{OPT}_\theta(G,w)=w(F)+\tau_w(Q).
\tag{11}
\]

Because \(\theta\) is fixed, evaluating it on all pairs and constructing \(Q\) takes polynomial time. No sparsity assertion about \(Q\) is being made.

Apply Lemma 1 to \((Q,w)\), obtaining \(V_0,R,V_1\) and \(H=Q[R]\). Thus
\[
\tau_w(Q)=w(V_1)+\tau_w(H),
\qquad
w(R)\le 2\tau_w(H).
\tag{12}
\]

Now consider, on the original graph \(G\), the fixed FO maximization formula
\[
\varphi(I)=
\forall x\,\forall y\,
\bigl((I(x)\land I(y))\longrightarrow\neg\theta(x,y)\bigr).
\tag{13}
\]
It is downward-monotone in \(I\).

Give \(G\) the modified weights
\[
\widehat w(v)=
\begin{cases}
w(v),&v\in R,\\
0,&v\notin R.
\end{cases}
\tag{14}
\]

The optimum weight for (13) with weights \(\widehat w\) equals
\[
\alpha_w(H),
\tag{15}
\]
the maximum independent-set weight in \(H\). Indeed:

* every feasible \(I\) has \(I\cap R\) independent in \(H\);
* every independent set contained in \(R\), selected alone, satisfies (13).

Apply the weighted monotone FO maximization PTAS stated in the question. For any fixed \(\delta>0\), it returns a feasible \(I\) satisfying
\[
w(I\cap R)\ge (1-\delta)\alpha_w(H).
\tag{16}
\]

Return
\[
S=F\cup V_1\cup\bigl(R\setminus(I\cap R)\bigr).
\tag{17}
\]
This is feasible by the vertex-cover core lemma.

Since the complement of a minimum-weight vertex cover is a maximum-weight independent set,
\[
\alpha_w(H)=w(R)-\tau_w(H)\le\tau_w(H).
\tag{18}
\]
Consequently,
\[
\begin{aligned}
w(S)
&\le w(F)+w(V_1)+w(R)-(1-\delta)\alpha_w(H)\\
&=w(F)+w(V_1)+\tau_w(H)+\delta\alpha_w(H)\\
&\le w(F)+w(V_1)+(1+\delta)\tau_w(H)\\
&\le (1+\delta)\operatorname{OPT}_\theta(G,w).
\end{aligned}
\]
This proves Theorem A.

### Examples and scope

Besides ordinary vertex cover, this covers, for every fixed \(r\), minimum-weight selection of \(S\) such that the vertices outside \(S\) are pairwise at distance greater than \(r\) **in the original graph**. Take
\[
\theta(x,y)\equiv x\ne y\land \operatorname{dist}_G(x,y)\le r.
\]

Finite conjunctions of universally quantified covering clauses with at most two selected vertices can likewise be folded into a fixed binary relation and unary forced constraints.

This is not a reduction to an unproved conjecture: the only metatheorem used in this section is the maximization theorem supplied in the question. The direct vertex-cover proof in Section 4 does not need that metatheorem.

---

# 6. A PTAS for bounded-radius local covering at bounded degree

Here is a different fragment that includes domination and is not restricted to binary covering clauses.

Fix constants \(\Delta,r\). Let the input graph have maximum degree at most \(\Delta\). For each vertex \(v\), let
\[
\mathcal F_v\subseteq 2^{B_r(v)}
\]
be an upward-closed family. Feasibility means
\[
S\cap B_r(v)\in\mathcal F_v
\qquad\text{for every }v.
\tag{19}
\]

Assume these families are given, or their membership can be evaluated in polynomial time. Since the balls have bounded size, this includes fixed FO predicates whose dependence on the selected set is confined to \(B_r(v)\) and is monotone there.

If some \(\mathcal F_v\) is empty, the instance is infeasible. Otherwise, upward closure implies that selecting all vertices is feasible.

### Theorem 3

On a bounded-maximum-degree efficiently fractionally treewidth-fragile class, every problem of the form (19) has a PTAS.

### Proof

Let \(b=b(\Delta,r)\) be an upper bound on the size of an \(r\)-ball.

For each \(v\), compute a minimum-weight set
\[
A_v\in\mathcal F_v,
\qquad c(v)=w(A_v).
\tag{20}
\]
This requires inspecting at most \(2^b\) subsets.

For a deletion set \(Z\), call \(v\) **good** if
\[
B_r^G(v)\cap Z=\varnothing,
\]
and bad otherwise.

Compute a minimum-weight set \(D_Z\subseteq V(G)\setminus Z\) satisfying all constraints belonging to good vertices. Return
\[
S_Z=D_Z\cup\bigcup_{\text{\(v\) bad}}A_v.
\tag{21}
\]

Good constraints remain satisfied because they are upward-closed. Each bad constraint is satisfied by its added set \(A_v\). Thus \(S_Z\) is feasible.

#### Exact optimization of the good constraints

For a good vertex \(v\),
\[
B_r^G(v)=B_r^{G-Z}(v).
\tag{22}
\]
Indeed, every vertex on a shortest path of length at most \(r\) from \(v\) lies in \(B_r^G(v)\), and hence avoids \(Z\).

Take a tree decomposition of \(G-Z\) of width at most \(t(k)\). Replace each bag \(B\) by
\[
B'=\bigcup_{u\in B}B_r^{G-Z}(u).
\tag{23}
\]
Its size is at most \(b(t(k)+1)\), and every good constraint scope lies in an expanded bag.

These expanded bags satisfy the running-intersection property. For a fixed vertex \(a\), its expanded-bag occurrences are the union of the original occurrence subtrees of the vertices in \(B_r^{G-Z}(a)\). That ball is connected, and occurrence subtrees of adjacent vertices intersect. Their union is therefore connected.

Consequently, the good constraints form a Boolean weighted constraint problem of bounded treewidth. Standard bag-assignment dynamic programming computes \(D_Z\) exactly in polynomial time for fixed \(k,\Delta,r\).

#### Approximation bound

Fix an optimum \(S^\star\). Its restriction \(S^\star\setminus Z\) satisfies every good constraint, so
\[
w(D_Z)\le w(S^\star\setminus Z)\le\operatorname{OPT}.
\tag{24}
\]

Moreover,
\[
c(v)\le w(S^\star\cap B_r(v)).
\]
Summing and using symmetry of graph distance,
\[
\begin{aligned}
\sum_v c(v)
&\le \sum_{u\in S^\star}w(u)
   \bigl|\{v:u\in B_r(v)\}\bigr|\\
&=\sum_{u\in S^\star}w(u)|B_r(u)|\\
&\le b\,\operatorname{OPT}.
\end{aligned}
\tag{25}
\]

The thinness condition and a union bound give
\[
\Pr(v\text{ is bad})
\le \sum_{u\in B_r(v)}\Pr(u\in Z)
\le \frac bk.
\tag{26}
\]

By (21), (24), and (25),
\[
\begin{aligned}
\mathbb E[w(S_Z)]
&\le \operatorname{OPT}
  +\sum_v c(v)\Pr(v\text{ is bad})\\
&\le \operatorname{OPT}+\frac bk\sum_v c(v)\\
&\le \left(1+\frac{b^2}{k}\right)\operatorname{OPT}.
\end{aligned}
\tag{27}
\]

Compute the candidates for every support member and return the lightest. Taking
\[
k=\left\lceil\frac{b^2}{\varepsilon}\right\rceil
\]
proves the PTAS. ∎

This includes weighted dominating set, fixed-distance domination, and bounded-radius monotone transversal constraints on bounded-degree classes.

---

# 7. A constant-factor result beyond bounded-rank clauses

For completeness, there is an elementary positive result for the bounded-expansion half that handles ordinary weighted domination, despite its unbounded-size covering constraints.

### Proposition 4

Weighted dominating set has a polynomial-time \((4d+2)\)-approximation on \(d\)-degenerate graphs.

### Proof

Orient the graph with outdegree at most \(d\). Solve the domination LP
\[
\begin{aligned}
\min\quad&\sum_u w(u)x_u,\\
\text{subject to}\quad&
\sum_{u\in N[v]}x_u\ge1\qquad(v\in V(G)),\\
&0\le x_u\le1.
\end{aligned}
\tag{28}
\]

For a vertex \(v\), put
\[
P_v=\{v\}\cup N^+(v),\qquad Q_v=N^-(v).
\]
Thus \(|P_v|\le d+1\).

First select
\[
T=\left\{u:x_u\ge\frac{1}{2(d+1)}\right\}.
\tag{29}
\]
Its weight is at most
\[
w(T)\le2(d+1)\operatorname{LP}.
\tag{30}
\]

Whenever
\[
\sum_{u\in P_v}x_u\ge\frac12,
\]
some vertex of \(P_v\) belongs to \(T\), so \(v\) is dominated.

For every remaining \(v\), the LP implies
\[
\sum_{u\in Q_v}x_u>\frac12.
\]
Choose a minimum-weight vertex \(a_v\in Q_v\). The weighted-average bound gives
\[
w(a_v)
\le
\frac{\sum_{u\in Q_v}w(u)x_u}
     {\sum_{u\in Q_v}x_u}
\le 2\sum_{u\in Q_v}w(u)x_u.
\tag{31}
\]

Each vertex \(u\) belongs to \(Q_v\) for at most \(d\) vertices \(v\), because those are precisely its outneighbors. Therefore
\[
w\bigl(\{a_v:v\text{ remaining}\}\bigr)
\le2d\,\operatorname{LP}.
\tag{32}
\]

Together, the selected vertices dominate the graph and have weight at most
\[
(4d+2)\operatorname{LP}
\le(4d+2)\operatorname{OPT}.
\]
∎

Every bounded-expansion class has uniformly bounded degeneracy, so this supplies a constant factor for this particular monotone FO minimization problem. It does not require bounded maximum degree.

---

# 8. What is still missing

The full problem remains unresolved by these arguments.

1. **Binary covering is a genuine restriction.**  
   Theorem A concerns clauses requiring one of at most two specified vertices. General monotone FO formulas can require selected witnesses from unbounded neighborhoods or involve more complicated quantifier interactions.

2. **The vertex-cover persistence lemma is special.**  
   The proof uses both
   \[
   \tau_w(G)=w(V_1)+\tau_w(H)
   \quad\text{and}\quad
   w(V(H))\le2\tau_w(H).
   \]
   No analogous lossless, weight-balanced reduction is established here for arbitrary monotone FO minimization.

3. **The local-covering PTAS genuinely uses bounded maximum degree.**  
   It uses bounded ball size both in (26) and in the charging bound (25). For example, in a star whose center has weight \(1\) and whose leaves have weight at least \(1\), domination has optimum \(1\), whereas the sum of the cheapest individual domination costs is the number of vertices. Thus this repair analysis does not extend uniformly to unbounded degree. The star itself is, of course, easy; this demonstrates a limitation of the analysis, not a hardness result.

4. **The general bounded-expansion claim is not proved.**  
   Proposition 4 handles domination, and bounded-rank universal covering clauses have the usual bounded-rank LP approximation. These do not cover all semantically monotone FO formulas.

Accordingly, the strongest conclusion here is a rigorous **partial resolution**, including the catalog’s highlighted weighted vertex-cover case under standard efficient fragility, and its extension to every fixed FO-definable binary covering relation. I have not independently checked whether these observations already occur in the literature, so I make no novelty claim.