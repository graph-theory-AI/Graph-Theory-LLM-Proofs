Attack the following open graph-theory problem.

Catalog id: complexity_of_the_h_factor_problem
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Extremal Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/complexity_of_the_h_factor_problem/
Original entry: http://www.openproblemgarden.org/op/complexity_of_the_h_factor_problem
Problem attributed to: Kühn, Daniella, Osthus, Deryk (posted 2013-03-05)

=== Problem statement (OpenProblemGarden) ===
Title: Complexity of the H-factor problem.
An $ H $ -factor in a graph $ G $ is a set of vertex-disjoint copies of $ H $ covering all vertices of $ G $ . Problem Let $ c $ be a fixed positive real number and $ H $ a fixed graph. Is it NP-hard to determine whether a graph $ G $ on $ n $ vertices and minimum degree $ cn $ contains and $ H $ -factor?

=== Discussion / context (OpenProblemGarden) ===
The answer is positive for cliques and a few other graphs [KO06]. If we remove the minimum degree condition, the problem is NP-complete if and only if $ H $ has a component which contains at least 3 vertices, as shown by Hell and Kirkpatrick [HK].

=== References listed by OpenProblemGarden ===
- [HK] P. Hell and D.G. Kirkpatrick, On the complexity of general graph factor problems, SIAM J. Computing 12 (1983), 601-609.
- [KO06] D. Kühn and D. Osthus, Critical chromatic number and the complexity of perfect packings in graphs, Proceedings of the 17th ACM-SIAM Symposium on Discrete Algorithms (SODA), 2006.
- *[KO09] D. Kühn and D. Osthus, The minimum degree threshold for perfect graph packings, Combinatorica 29 (2009), 65-107.

=== Catalog page (statement + literature review) ===
Complexity of the H-factor problem. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Han and Treglown (JCTB 2020) provide a general tool that resolves much of the question: for any graph $H$ and any $\gamma>0$, deciding whether an $n$-vertex graph $G$ with $\delta(G)\ge(1-1/\chi_{cr}(H)+\gamma)n$ contains a perfect $H$-packing is polynomial-time solvable, while a complementary hardness result of Kühn and Osthus (TAMC 2017) shows that for many $H$ (including all complete multipartite $H$ whose second smallest color class has size at least 2) the problem becomes NP-complete just below this critical threshold, so that a sharp $P$/NP-hard dichotomy in the parameter $c$ holds for those $H$. A complete dichotomy at the critical threshold for all graphs $H$ is, however, still not fully established.

 Cited literature (2)

 
 
 
partial The complexity of perfect matchings and packings in dense hypergraphs
 (2020)
 

 
 Jie Han, Andrew Treglown · Journal of Combinatorial Theory, Series B · arXiv:1609.06147 · doi:10.1016/j.jctb.2019.06.004

Gives, for every graph $F$, a minimum degree condition under which deciding existence of a perfect $F$-packing is polynomial-time solvable, and shows the threshold is best possible in many cases (lowering it makes the decision problem NP-complete), thereby largely answering the Kühn–Osthus question.
 

 
 
partial The Complexity of Perfect Packings in Dense Graphs
 (2017)
 

 
 Daniela Kühn, Deryk Osthus · Theory and Applications of Models of Computation (TAMC 2017), LNCS 10185 · doi:10.1007/978-3-319-55911-7_21

Provides the matching NP-hardness side, closing a long-standing hardness gap for all complete multipartite graphs $H$ whose second smallest color class has size at least 2, so that the polynomial/NP-hard transition at the critical chromatic threshold is sharp for these $H$.
 

 

 Reviewer notes. Han–Treglown (arXiv:1609.06147, JCTB 2020) explicitly state that their minimum degree threshold for polynomial solvability is, in many cases, best possible: lowering it makes the decision problem NP-complete. Kühn–Osthus's TAMC 2017 chapter supplies the matching hardness for complete multipartite $H$ whose second-smallest color class has size at least 2, closing the gap for those $H$. Together these substantially answer the OPG question affirmatively in the regime $c<1-1/\chi_{cr}(H)$ for many $H$, and negatively (problem is in P) for $c>1-1/\chi_{cr}(H)$. The Springer page for the Kühn–Osthus chapter required login to inspect the abstract, but its existence, authors, year, and content (closing the hardness gap) are corroborated across multiple independent search results and the Han–Treglown abstract; no arXiv preprint located. A fully tight dichotomy at the critical threshold for every graph $H$ does not yet appear in the literature, so the original problem as stated is best classified as having strong partial progress rather than fully resolved.

 
 Auto-reviewed 2026-05-08 with claude-sonnet (subagent) (web search enabled).
 

Problem. Let $ c $ be a fixed positive real number and $ H $ a fixed graph. Is it NP-hard to determine whether a graph $ G $ on $ n $ vertices and minimum degree $ cn $ contains and $ H $ -factor?

Discussion

The answer is positive for cliques and a few other graphs [KO06]. If we remove the minimum degree condition, the problem is NP-complete if and only if $ H $ has a component which contains at least 3 vertices, as shown by Hell and Kirkpatrick [HK].

Bibliography

 [HK]
 P. Hell and D.G. Kirkpatrick, On the complexity of general graph factor problems, SIAM J. Computing 12 (1983), 601-609.

 [KO06]
 D. Kühn and D. Osthus, Critical chromatic number and the complexity of perfect packings in graphs, Proceedings of the 17th ACM-SIAM Symposium on Discrete Algorithms (SODA), 2006.

★ [KO09]
 D. Kühn and D. Osthus, The minimum degree threshold for perfect graph packings, Combinatorica 29 (2009), 65-107.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A uniform padding reduction preserves the unrestricted complexity dichotomy for 0 < c < 1/|H|, and an explicit expansion condition gives sharper hardness bounds.",
  "would_publish": false,
  "caveats": "The general higher-density regime and equality cases are not resolved here; literature novelty is not claimed."
}
```

## 1. Interpretation and partial result

I interpret the degree condition as the promise
\[
\delta(G)\ge c|V(G)|,
\]
as in the catalog’s discussion. Copies of \(H\) are **not required to be induced**.

The following gives a uniform low-density classification, including disconnected \(H\).

**Theorem 1.** Let \(H\) be a fixed nonempty graph, and put \(h=|V(H)|\). For every fixed
\[
0<c<\frac1h,
\]
the following hold.

* If every component of \(H\) has at most two vertices, the promised \(H\)-factor problem is polynomial-time solvable.
* If \(H\) has a component with at least three vertices, the promised \(H\)-factor problem is NP-hard.

For rational \(c\), the latter restricted language is NP-complete. For arbitrary fixed real \(c\), the construction gives NP-hardness under promise-preserving reductions.

I use the unrestricted factor NP-completeness theorem stated in the question as the starting hardness result. All the densification arguments below are proved explicitly.

### The polynomial-time side

Write
\[
H=aK_2\ \dot\cup\ bK_1,\qquad h=2a+b.
\]
If \(h\nmid n\), there is no \(H\)-factor. Otherwise, putting \(Q=n/h\), an \(H\)-factor exists exactly when \(G\) has a matching of size at least \(aQ\).

Necessity is immediate. Conversely, choose \(aQ\) matching edges and partition them into \(Q\) groups of \(a\) edges; distribute the remaining \(bQ\) vertices as \(b\) additional vertices per group. Because copies are non-induced, this gives an \(H\)-factor regardless of additional edges. Thus maximum matching solves this case, without any degree assumption.

The hardness side follows from a somewhat stronger padding theorem.

---

## 2. A general saturation-padding reduction

Here, \(F\)-free means containing no—not necessarily induced—copy of \(F\).

**Theorem 2.** Suppose
\[
H=tF\ \dot\cup\ J,
\]
where \(F\) is connected, \(f:=|V(F)|\ge3\), \(t\ge1\), and \(J\) is \(F\)-free. Put \(h=|V(H)|\). Then the \(H\)-factor problem is NP-hard under the promise
\[
\delta(G)\ge c|V(G)|
\]
for every fixed
\[
0<c<\frac{t}{h}.
\]

### Why this covers every \(H\) with a component of order at least three

Choose a component \(F\) of maximum order, and among components of that order choose one with the maximum number of edges. Remove all \(t\) components isomorphic to \(F\), leaving \(J\).

Then \(J\) is \(F\)-free. Indeed, because \(F\) is connected, a copy of \(F\) in \(J\) would lie in a single component. That component cannot have fewer vertices than \(F\); if it has the same number of vertices, the choice of \(F\) implies that containing \(F\) would force it to be isomorphic to \(F\).

Thus Theorem 2 always supplies a hardness range containing \(0<c<1/h\).

### Proof of Theorem 2

Reduce from the unrestricted \(F\)-factor problem, which is NP-complete by the theorem supplied in the question.

We may restrict the source to nonempty graphs \(X\) with
\[
|V(X)|=fk,\qquad k\ge1.
\]
Orders not divisible by \(f\) are immediately negative; they can be replaced by a fixed negative instance of order \(f\).

Write \(j=|V(J)|\), so \(h=tf+j\). Choose a fixed integer \(L\ge2\) sufficiently large that
\[
\frac{t}{h}-\frac{1}{hL}\ge c.
\]
Define
\[
Q=Lk,\qquad q=tQ-k=(tL-1)k.
\]

Construct \(G\) from three disjoint vertex sets:

1. \(X\), retaining all its original edges;
2. a clique \(B\) of order \(q\);
3. a graph \(A\) consisting of the disjoint union of
   * \(q\) copies of \(K_{f-1}\), and
   * \(Q\) copies of \(J\).

Join every vertex of \(B\) to every vertex of \(A\cup X\). Add no edges between \(A\) and \(X\).

The order of \(G\) is
\[
\begin{aligned}
n
&=fk+q+(f-1)q+jQ\\
&=f(k+q)+jQ\\
&=(ft+j)Q=hQ.
\end{aligned}
\]
Every vertex outside \(B\) has all \(q\) vertices of \(B\) as neighbours, and \(B\) is universal. Hence
\[
\delta(G)\ge q
\quad\text{and}\quad
\frac{\delta(G)}n
\ge
\frac{tL-1}{hL}
=
\frac th-\frac1{hL}
\ge c.
\]
The construction has \(O(|V(X)|)\) vertices and polynomially many edges.

We prove
\[
X\text{ has an }F\text{-factor}
\quad\Longleftrightarrow\quad
G\text{ has an }H\text{-factor}.
\]

#### Forward implication

An \(F\)-factor of \(X\) supplies \(k\) copies of \(F\).

Pair each of the \(q\) designated copies of \(K_{f-1}\) in \(A\) with a distinct vertex of \(B\). Each resulting \(K_f\) contains a copy of \(F\), supplying another \(q\) copies.

There are therefore
\[
k+q=tQ
\]
disjoint copies of \(F\), together with the \(Q\) designated copies of \(J\). Grouping \(t\) copies of \(F\) with one copy of \(J\) gives an \(H\)-factor. Additional edges between its components are irrelevant.

#### Reverse implication: the saturation argument

Suppose \(G\) has an \(H\)-factor. It consists of \(Q\) copies of \(H\), and thus contains \(tQ\) designated component copies of \(F\).

First, \(A\) is \(F\)-free: its components lie either in a \(K_{f-1}\) or in a copy of \(J\).

For each designated \(F\)-component copy \(C\), let
\[
a_C=|V(C)\cap A|,\qquad b_C=|V(C)\cap B|.
\]
If \(a_C>0\), then \(b_C>0\). Otherwise, connectedness and the absence of \(A\)-\(X\) edges would force \(C\) to lie entirely in \(A\), contradicting \(F\)-freeness.

Consequently,
\[
a_C\le(f-1)b_C
\tag{1}
\]
for every such \(C\).

There are only \(jQ\) vertices occupying \(J\)-component positions in the factor. Therefore
\[
\begin{aligned}
(f-1)q
&=|A|-jQ\\
&\le \sum_C a_C\\
&\le (f-1)\sum_C b_C\\
&\le (f-1)|B|\\
&=(f-1)q.
\end{aligned}
\tag{2}
\]
Every inequality is therefore an equality.

In particular:

* all vertices occupying \(J\)-component positions lie in \(A\);
* each \(F\)-component copy satisfies \(a_C=(f-1)b_C\).

If \(b_C=0\), then \(a_C=0\), so \(C\) lies entirely in \(X\). If \(b_C>0\), then
\[
f\ge a_C+b_C=fb_C,
\]
forcing
\[
b_C=1,\qquad a_C=f-1.
\]
Such a copy contains no vertex of \(X\).

Thus every vertex of \(X\) is covered by an \(F\)-copy lying entirely in \(X\). This is an \(F\)-factor of \(X\), completing the reduction. \(\square\)

For rational \(c\), checking the degree condition and verifying an \(H\)-factor certificate are polynomial-time operations, giving NP-completeness. For arbitrary fixed real \(c\), one fixes a suitable integer \(L\) once and for all; the reduction itself does not need to compute \(c\).

---

## 3. A sharper independent-neighbourhood criterion

The previous construction gives a uniform positive-density bound. An independent reservoir can do substantially better when the tile has suitable expansion.

For an independent set \(S\subseteq V(F)\), write \(N_F(S)\) for its open neighbourhood.

**Expansion condition.** Let \(F\) be connected, with
\[
f=|V(F)|\ge3,\qquad \alpha=\alpha(F).
\]
Assume that every nonempty independent set \(S\) of size less than \(\alpha\) satisfies
\[
\alpha\,|N_F(S)|>(f-\alpha)|S|.
\tag{E}
\]

Every maximum independent set is dominating, so for such a set
\[
|N_F(S)|=f-\alpha.
\]
Thus condition (E) says precisely that the minimum neighbourhood-to-size ratio is attained only by maximum independent sets. It is a finite, explicitly checkable condition: enumerate the subsets of the fixed graph \(F\).

**Theorem 3.** Suppose \(F\) satisfies (E), and let
\[
H=tF\ \dot\cup\ sK_1,\qquad t\ge1,\ s\ge0.
\]
Then the \(H\)-factor problem is NP-hard whenever
\[
0<c<
\frac{t(f-\alpha(F))}{tf+s}.
\tag{3}
\]
Equivalently, the upper endpoint in (3) is \(1-\alpha(H)/|V(H)|\).

In particular, for connected \(H=F\), the hardness range is
\[
0<c<1-\frac{\alpha(F)}f.
\]

### Proof

Put
\[
b=f-\alpha,\qquad h=tf+s.
\]
Again reduce from \(F\)-factor on an input \(X\) of order \(fk\).

Choose a fixed integer \(L\ge2\) such that
\[
\frac{b(tL-1)}{hL}\ge c,
\]
and set
\[
Q=Lk,\qquad q=tQ-k.
\]

Construct \(G\) from:

* the original graph \(X\);
* an independent set \(A\) of order \(sQ+\alpha q\);
* a clique \(B\) of order \(bq\).

Join \(B\) completely to \(A\cup X\), and add no \(A\)-\(X\) edges. Then
\[
|V(G)|
=fk+sQ+\alpha q+bq
=f(k+q)+sQ=hQ,
\]
and
\[
\delta(G)\ge bq\ge c|V(G)|.
\]

If \(X\) has an \(F\)-factor, form \(q\) further \(F\)-copies using \(\alpha\) vertices of \(A\) and \(b\) vertices of \(B\) per copy. A fixed maximum independent set of \(F\) specifies this embedding. Use the remaining \(sQ\) vertices of \(A\) for the isolated-vertex positions. Since \(k+q=tQ\), this gives an \(H\)-factor.

Conversely, suppose \(G\) has an \(H\)-factor. For each designated \(F\)-component copy \(C\), let \(a_C,b_C\) count its vertices in \(A,B\).

The preimage \(S_C\) of \(V(C)\cap A\) is independent in \(F\). Every vertex of \(N_F(S_C)\) must map into \(B\), because vertices of \(A\) have neighbours only in \(B\). Consequently,
\[
b_C\ge \frac b\alpha a_C.
\tag{4}
\]
For \(a_C>0\), equality in (4) is possible only when \(a_C=\alpha\).

At most \(sQ\) vertices of \(A\) can occupy isolated-vertex positions. Summing (4) therefore gives
\[
\begin{aligned}
bq=|B|
&\ge\sum_C b_C\\
&\ge\frac b\alpha\sum_C a_C\\
&\ge\frac b\alpha\bigl(|A|-sQ\bigr)\\
&=bq.
\end{aligned}
\]
Again all inequalities are equalities.

All isolated-vertex positions lie in \(A\). Each \(F\)-copy meeting \(A\) uses exactly \(\alpha\) vertices of \(A\) and \(b\) vertices of \(B\), hence no vertices of \(X\). Each other \(F\)-copy uses no vertices of \(B\), and therefore lies entirely in \(X\).

Thus \(X\) has an \(F\)-factor. \(\square\)

---

## 4. Families reaching the critical density from below

Here are concrete consequences of Theorem 3 with \(H=F\).

| Fixed graph \(F\) | Proven NP-hard range |
|---|---|
| \(K_r\), \(r\ge3\) | \(0<c<1-1/r\) |
| Connected biregular bipartite \(F\), with part sizes \(p\ge q\) and at least three vertices | \(0<c<q/(p+q)\) |
| \(P_{2k+1}\), \(k\ge1\) | \(0<c<k/(2k+1)\) |
| \(C_{2k+1}\), \(k\ge1\) | \(0<c<(k+1)/(2k+1)\) |

Even cycles are included in the biregular bipartite case. I verify the expansion condition rather than appeal to additional literature.

### Cliques

For \(K_r\), \(\alpha=1\), so (E) is vacuous. Theorem 3 gives \(c<(r-1)/r\).

### Connected biregular bipartite graphs

Let the bipartition be \(U\cup W\), where \(|U|=p\ge q=|W|\). Let the degrees on \(U,W\) be \(r,s\), respectively. Then
\[
pr=qs,\qquad \lambda:=\frac rs=\frac qp\le1.
\]

For an independent set \(S=U'\cup W'\), degree counting gives
\[
|N(U')|\ge\lambda |U'|,
\qquad
|N(W')|\ge\lambda^{-1}|W'|.
\]
These two neighbourhoods lie in different bipartition classes, so
\[
|N(S)|
\ge\lambda|U'|+\lambda^{-1}|W'|
\ge\lambda|S|.
\tag{5}
\]

If \(\lambda<1\), equality forces \(W'=\varnothing\) and equality in the first degree count. Every vertex of \(N(U')\) then has all its neighbours in \(U'\). Hence \(U'\cup N(U')\) has no edges to its complement. Connectedness forces \(U'=U\).

If \(\lambda=1\), the graph is regular. Equality in \(|N(S)|\ge|S|\) likewise forces \(S\cup N(S)=V(F)\), and hence \(|S|=p\).

Moreover, applying (5) to a maximum independent set—which is dominating—shows that \(\alpha(F)\le p\). Since \(U\) is independent, \(\alpha(F)=p\).

Thus equality in (5) occurs only for maximum independent sets, proving (E). The resulting density is \(q/(p+q)\).

### Odd-order paths

For \(F=P_{2k+1}\), we have \(\alpha=k+1\). Let \(S\) be independent with \(0<|S|<k+1\).

Some odd-indexed vertex \(v\) is outside \(S\). Deleting \(v\) leaves two even-order paths, and therefore a graph with a perfect matching. That matching matches every vertex of \(S\) to a distinct vertex of \(N(S)\), giving
\[
|N(S)|\ge |S|>
\frac{k}{k+1}|S|.
\]
This is (E), and yields \(c<k/(2k+1)\).

### Odd cycles

Let \(F=C_{2k+1}\), so \(\alpha=k\). For every nonempty independent set \(S\),
\[
|N(S)|\ge |S|+1.
\tag{6}
\]
Indeed, degree counting gives \(|N(S)|\ge|S|\). Equality would force every neighbour of \(N(S)\) to lie in \(S\); connectedness would then make the entire cycle bipartite, a contradiction.

For \(0<|S|<k\), equation (6) gives
\[
\frac{|N(S)|}{|S|}
\ge1+\frac1{|S|}
>
1+\frac1k
=\frac{k+1}{k}.
\]
Thus (E) holds, giving \(c<(k+1)/(2k+1)\).

### Comparison with the catalog’s parameter

Recall the numerical definition
\[
\chi_{\mathrm{cr}}(F)
=\frac{(\chi(F)-1)f}{f-\sigma(F)},
\]
where \(\sigma(F)\) is the smallest colour-class size achievable in a proper \(\chi(F)\)-colouring.

For every connected family in the table, its displayed endpoint equals
\[
1-\frac1{\chi_{\mathrm{cr}}(F)}.
\]
For connected bipartite graphs, \(\sigma(F)\) is the smaller bipartition size; for odd cycles it is \(1\); for cliques it is also \(1\).

Thus these reductions supply the hardness side **strictly below** that parameter for the stated families. This is a numerical comparison, not a claim that the bounds improve the published results for those families.

---

## 5. What remains missing—and a genuine obstruction

These arguments do not establish the general \(P\)/NP-hard classification requested in the problem. In particular, they make no assertion at the limiting density in Theorems 2 or 3, and the expansion condition is a real restriction.

The first simple obstruction is \(F=P_4\). Here \(\alpha=2\), but an endpoint \(S=\{v\}\) satisfies
\[
|N(S)|=1=\frac{4-2}{2}|S|.
\]
So (E) fails.

It would be incorrect merely to replace the strict inequality in (E) by a weak one. To see this, let
\[
X=2K_2
\]
with edges \(x_1y_1,x_2y_2\). It has no \(P_4\)-factor. Take independent
\[
A=\{a_1,a_2\},
\]
a clique
\[
B=\{b_1,b_2\},
\]
join \(B\) completely to \(A\cup X\), and add no \(A\)-\(X\) edges. The resulting graph nevertheless has the \(P_4\)-factor
\[
a_1b_1x_1y_1,\qquad a_2b_2x_2y_2.
\]
A saturated copy can use one reservoir vertex, one universal vertex, and only an **edge** of the source instance. The intended implication back to a \(P_4\)-factor therefore fails.

The uniform reduction still proves hardness for \(P_4\) whenever \(c<1/4\); this writeup does not classify its remaining densities.

**Conclusion.** The complete general question is not solved here. What is proved is:

1. the unrestricted polynomial/NP-complete division persists uniformly throughout \(0<c<1/|H|\), even for disconnected \(H\);
2. a sharper, finitely checkable neighbourhood-expansion condition yields stronger hardness ranges, reaching the catalog’s critical parameter from below for the families listed above.

These are complete reductions, but I have not established their literature novelty and would not present them as a new resolution of the catalog problem.
