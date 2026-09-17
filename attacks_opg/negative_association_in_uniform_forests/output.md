```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture for sufficiently long subdivisions of every finite simple graph, using an explicit small-activity negative-correlation bound.",
  "would_publish": false,
  "caveats": "The general uniform-forest conjecture remains untreated; novelty and current literature status are not asserted."
}
```

# A partial result: sufficiently subdivided graphs

I use the intended formulation with **distinct edges** \(e\ne f\). Forests are acyclic edge subsets, with isolated vertices allowed. The results below are stated for finite simple graphs.

The main partial result is:

**Theorem 1.** Let \(G\) have \(m\ge 3\) edges. Replace each edge \(g\) by a path of length \(k_g\), with all new internal vertices distinct, obtaining \(H\). If
\[
k_g\ge m-1\qquad\text{for every }g\in E(G),
\]
then the uniform forest of \(H\) has pairwise negatively correlated edge indicators.

Thus the original graph \(G\) can be arbitrary; the restriction is on the subdivision lengths. The proof also establishes the following weighted result.

**Theorem 2.** For a graph \(G\) with \(m\ge2\) edges, give a forest \(F\) probability proportional to
\[
\prod_{g\in F}x_g,
\]
where the activities satisfy
\[
0<x_g\le 2^{\,2-m}\qquad(g\in E(G)).
\]
Then all distinct edge indicators are negatively correlated.

The bound is very crude. Its advantage is that it is explicit and applies to every graph.

## 1. Forest polynomials and the desired inequality

Define
\[
Z_G(\mathbf x)=\sum_{\substack{F\subseteq E(G)\\F\text{ acyclic}}}
\prod_{g\in F}x_g.
\]
For distinct \(e,f\), write
\[
Z_G=A+x_eB+x_fC+x_ex_fD,
\]
where \(A,B,C,D\) involve only the other \(m-2\) variables. Set
\[
\Delta_{ef}=Z_eZ_f-Z_GZ_{ef}=BC-AD.
\]
In particular, \(\Delta_{ef}\) is independent of \(x_e,x_f\).

Under the weighted forest measure, with \(X_g=\mathbf 1_{\{g\in F\}}\),
\[
\operatorname{Cov}(X_e,X_f)
=-\frac{x_ex_f}{Z_G(\mathbf x)^2}\Delta_{ef}(\mathbf x).
\tag{1}
\]
Consequently, negative correlation is equivalent to \(\Delta_{ef}\ge0\).

We will control the negative coefficients of \(\Delta_{ef}\) by positive coefficients coming from cycles through \(e\) and \(f\).

## 2. Three elementary facts about coefficient supports

### 2.1 Edges on no common cycle are independent

The forest polynomial factors over the blocks of a graph: every cycle lies in a single block, so choices of forests in different blocks are independent.

Also, two distinct edges belong to a common nontrivial block if and only if they lie on a common cycle. The nontrivial direction follows, for example, by subdividing the two edges in a 2-connected block and finding two internally vertex-disjoint paths between the subdivision vertices.

It follows that
\[
e,f\text{ lie on no common cycle}
\quad\Longrightarrow\quad
\Delta_{ef}\equiv0.
\tag{2}
\]

Specializing some edge variables to zero simply deletes those edges.

### 2.2 Each cycle supplies a positive coefficient

Suppose the graph is just a cycle \(\gamma\) containing \(e,f\). Put
\[
P=\prod_{g\in\gamma\setminus\{e,f\}}(1+x_g),
\qquad
Q=\prod_{g\in\gamma\setminus\{e,f\}}x_g.
\]
Then
\[
Z_\gamma=P(1+x_e)(1+x_f)-Qx_ex_f,
\]
and hence
\[
\Delta_{ef}^{\gamma}=PQ
=\prod_{g\in\gamma\setminus\{e,f\}}x_g(1+x_g).
\tag{3}
\]

Therefore, in an arbitrary graph, the coefficient in \(\Delta_{ef}\) of the squarefree monomial
\[
\prod_{g\in\gamma\setminus\{e,f\}}x_g
\]
is exactly \(1\). Indeed, set all variables outside \(\gamma\) to zero and apply (3).

### 2.3 A cycle plus at most one extra edge has no negative coefficients

We need the following slightly stronger observation.

**Lemma.** Suppose \(J\) consists of a cycle \(\gamma\) containing \(e,f\), together with at most one additional edge. Then every coefficient of \(\Delta_{ef}^{J}\) is nonnegative.

**Proof.** The cycle case is (3). If the extra edge is not a chord of \(\gamma\), it is a bridge, possibly in a separate component. Its activity \(t\) multiplies the forest polynomial by \(1+t\), and therefore multiplies \(\Delta_{ef}\) by \((1+t)^2\).

It remains to consider a chord of activity \(t\). Its endpoints split \(\gamma\) into two paths \(P,Q\). Write
\[
P_0=\prod_{g\in P}(1+x_g),\qquad P_1=\prod_{g\in P}x_g,
\]
and similarly \(Q_0,Q_1\). A direct classification according to whether the chord is present gives
\[
Z_J=P_0Q_0-P_1Q_1+t(P_0-P_1)(Q_0-Q_1).
\tag{4}
\]

If \(e\in P\) and \(f\in Q\), put
\[
R=\prod_{g\in P\setminus\{e\}}(1+x_g),\quad
r=\prod_{g\in P\setminus\{e\}}x_g,
\]
\[
S=\prod_{g\in Q\setminus\{f\}}(1+x_g),\quad
s=\prod_{g\in Q\setminus\{f\}}x_g.
\]
Substitution into (4), followed by \(BC-AD\), gives
\[
\Delta_{ef}^{J}=RrSs.
\tag{5}
\]

If both marked edges lie in \(P\), instead put
\[
R=\prod_{g\in P\setminus\{e,f\}}(1+x_g),\quad
r=\prod_{g\in P\setminus\{e,f\}}x_g,
\]
and let \(S=Q_0,\ s=Q_1\). Equation (4) becomes
\[
Z_J=U(1+x_e)(1+x_f)-Vx_ex_f,
\]
where
\[
U=R\bigl[S+t(S-s)\bigr],\qquad
V=r\bigl[s+t(S-s)\bigr].
\]
Thus
\[
\Delta_{ef}^{J}=UV.
\tag{6}
\]
Here \(S-s\) has nonnegative coefficients. Both (5) and (6) therefore have nonnegative coefficients. These cases exhaust the possibilities. \(\square\)

## 3. An explicit small-activity bound

Expand
\[
\Delta_{ef}=\sum_\alpha a_\alpha\mathbf x^\alpha
\]
in the variables other than \(x_e,x_f\). Each exponent is at most \(2\).

For a monomial, define its associated edge set
\[
S_\alpha=\{e,f\}\cup\{g:\alpha_g>0\}.
\]
If \(a_\alpha\ne0\), then \(G[S_\alpha]\) must contain a cycle through \(e,f\). Otherwise, specializing all variables outside \(S_\alpha\) to zero and applying (2) would give the zero polynomial.

Furthermore, if \(a_\alpha<0\), then for every cycle \(\gamma\subseteq S_\alpha\) through \(e,f\),
\[
|S_\alpha\setminus\gamma|\ge2.
\tag{7}
\]
Indeed, if there were at most one extra edge, the lemma would say that the specialized polynomial has no negative coefficients, contradicting \(a_\alpha<0\).

Let \(\mathscr C_{ef}\) be the set of cycles through \(e,f\), and define
\[
L_{ef}(\mathbf x)
=\sum_{\gamma\in\mathscr C_{ef}}
\prod_{g\in\gamma\setminus\{e,f\}}x_g.
\]
By §2.2, the positive-coefficient part of \(\Delta_{ef}\) is at least \(L_{ef}\) at nonnegative activities.

Let
\[
M_{ef}=\sum_{\alpha:a_\alpha<0}|a_\alpha|.
\]
Because \(\Delta_{ef}=BC-AD\), with both products having nonnegative coefficients,
\[
M_{ef}\le A(\mathbf1)D(\mathbf1)\le 4^{m-2}.
\tag{8}
\]
The last inequality holds because each of \(A,D\) counts a subfamily of the \(2^{m-2}\) subsets of the other edges.

Now suppose
\[
0\le x_g\le\varepsilon\le1
\qquad(g\ne e,f).
\]
For each negative monomial, select a cycle
\(\gamma_\alpha\subseteq S_\alpha\) through \(e,f\). By (7), the monomial has at least two distinct edge factors outside that cycle. Hence
\[
\mathbf x^\alpha
\le
\varepsilon^2
\prod_{g\in\gamma_\alpha\setminus\{e,f\}}x_g.
\]
Consequently,
\[
\begin{aligned}
\Delta_{ef}(\mathbf x)
&\ge L_{ef}(\mathbf x)
-\varepsilon^2
\sum_{\alpha:a_\alpha<0}|a_\alpha|
\prod_{g\in\gamma_\alpha\setminus\{e,f\}}x_g\\
&\ge
\bigl(1-\varepsilon^2M_{ef}\bigr)L_{ef}(\mathbf x).
\end{aligned}
\tag{9}
\]
Combining (8) and (9),
\[
\Delta_{ef}(\mathbf x)
\ge
\bigl(1-\varepsilon^2\,4^{m-2}\bigr)L_{ef}(\mathbf x).
\tag{10}
\]

Taking
\[
\varepsilon=2^{2-m}
\]
makes the right-hand side nonnegative. Equation (1) proves Theorem 2.

Notice that for a **specified pair** \(e,f\), their own activities need not satisfy the smallness bound: \(\Delta_{ef}\) does not depend on them.

### A local asymptotic consequence

Let \(\ell_{ef}\) be the shortest length of a cycle containing \(e,f\), and let \(N_{ef}\) count such shortest cycles. The same support argument shows that, at equal activity \(\beta\),
\[
\Delta_{ef}(\beta,\ldots,\beta)
=N_{ef}\beta^{\ell_{ef}-2}
+O_G(\beta^{\ell_{ef}-1}).
\]
Thus
\[
\operatorname{Cov}_\beta(X_e,X_f)
=-N_{ef}\beta^{\ell_{ef}}
+O_G(\beta^{\ell_{ef}+1}).
\tag{11}
\]
If there is no common cycle, the covariance is identically zero instead.

## 4. Passing from small activities to uniform subdivisions

We now prove Theorem 1.

For each original edge \(g\), let \(P_g\) be its replacement path, of length \(k_g\). In a uniformly chosen forest of \(H\), define
\[
Y_g=\mathbf1_{\{\text{every edge of }P_g\text{ is present}\}}.
\]

A set of edges of \(H\) is acyclic exactly when its fully present replacement paths correspond to an acyclic edge set of \(G\). This follows because a cycle using an internal vertex of a replacement path must traverse that entire path.

For a fixed forest \(A\subseteq E(G)\), the number of forests of \(H\) with
\[
\{g:Y_g=1\}=A
\]
is
\[
\prod_{g\notin A}(2^{k_g}-1).
\]
Therefore \(Y\) has precisely the weighted forest distribution on \(G\) with activities
\[
\beta_g=\frac1{2^{k_g}-1}.
\tag{12}
\]

Since \(k_g\ge m-1\) and \(m\ge3\),
\[
2^{k_g}-1\ge2^{m-2},
\qquad
\beta_g\le2^{2-m}.
\]
Theorem 2 implies
\[
\operatorname{Cov}(Y_g,Y_h)\le0
\qquad(g\ne h).
\tag{13}
\]

It remains important to check **all individual edges of the subdivided graph**, not merely the full-path indicators.

### 4.1 Edges on different replacement paths

Conditionally on \(Y\), choices on different paths are independent. An active path is completely present; an inactive path has a uniformly chosen proper subset of its edges.

For any particular edge \(a\in P_g\), put
\[
q_g=\frac{2^{k_g-1}-1}{2^{k_g}-1}.
\]
Then
\[
\mathbb E[X_a\mid Y]=q_g+(1-q_g)Y_g.
\]
For \(a\in P_g,\ b\in P_h,\ g\ne h\), conditional independence therefore gives
\[
\operatorname{Cov}(X_a,X_b)
=(1-q_g)(1-q_h)\operatorname{Cov}(Y_g,Y_h)\le0.
\tag{14}
\]

### 4.2 Two edges on the same replacement path

Let \(a,b\) be distinct edges of a path of length \(k\ge2\), and write
\[
p=\mathbb P(Y_g=1).
\]
Conditioned on \(Y_g=0\),
\[
q:=\mathbb P(X_a=1\mid Y_g=0)
=\frac{2^{k-1}-1}{2^k-1},
\]
and
\[
r:=\mathbb P(X_a=X_b=1\mid Y_g=0)
=\frac{2^{k-2}-1}{2^k-1}.
\]

We also have
\[
p\le2^{-k}.
\tag{15}
\]
To see this, write the original weighted forest polynomial, with other activities fixed, as
\[
Z_G=A_g+\beta_gB_g.
\]
Every forest counted by \(B_g\)—one to which \(g\) can be added—is also counted by \(A_g\), with the same weight. Thus \(B_g\le A_g\), and
\[
p=\frac{\beta_gB_g}{A_g+\beta_gB_g}
\le\frac{\beta_g}{1+\beta_g}
=2^{-k}.
\]

By total covariance,
\[
\operatorname{Cov}(X_a,X_b)
=(1-p)(r-q^2)+p(1-p)(1-q)^2.
\]
Substituting the displayed values simplifies this to
\[
\operatorname{Cov}(X_a,X_b)
=
\frac{(1-p)2^{k-2}}{(2^k-1)^2}
\bigl(2^kp-1\bigr)
\le0,
\tag{16}
\]
using (15).

Equations (14) and (16) cover every pair of distinct edges of \(H\), proving Theorem 1. Graphs with at most two edges are forests themselves, so their subdivision cases are trivial.

## 5. What remains unresolved

The argument does **not** establish the original conjecture for arbitrary unsubdivided graphs.

Its mechanism is explicit: a negative monomial in a Rayleigh difference needs at least two edge factors beyond a cycle through the marked edges. Small activities suppress those factors. At activity \(1\), that suppression disappears, and estimate (10) generally says nothing.

Nor can one undo the subdivision argument by contracting the replacement paths. Pairwise negative correlation at one measure is not, by itself, preserved under conditioning; contracting edges corresponds to such conditioning.

Thus the proved conclusions are:

- a quantitative negative-correlation neighborhood of zero activity for every graph;
- the corresponding shortest-common-cycle asymptotic;
- the uniform-forest conjecture for sufficiently long subdivisions of arbitrary finite simple graphs.

No proof or counterexample for the general uniform-forest conjecture is obtained, and no novelty claim is made for these partial results.