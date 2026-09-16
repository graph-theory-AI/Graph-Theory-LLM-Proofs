```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured upper-bound order for covers supported by fixed bounded-degree conflict templates, even with arbitrary changes on a bounded-degeneracy edge set, but not for unrestricted covers.",
  "would_publish": false,
  "caveats": "The templates must be fixed before sampling the graph; the unrestricted conjecture remains unresolved, and novelty of this restricted-model result is not claimed."
}
```

## 1. Scope

I work with the intended range \(0<p<1\). The edgeless endpoint from the previous attempt does not address the substantive problem.

Write
\[
a=-\log p>0,
\]
with natural logarithms. The unresolved assertion is
\[
\chi_{\mathrm{DP}}(G(n,1-p))=O(n/\log n)
\qquad\text{a.a.s.},
\]
where the correspondence assignment may be chosen arbitrarily **after** the graph is known.

The partial result below allows substantial graph-dependent choice of the assignment, but within predetermined conflict templates. It also permits completely arbitrary correspondences on a graph-dependent exceptional edge set of bounded degeneracy.

## 2. A restricted-cover theorem

Give each vertex \(v\in[n]\) a palette \(L(v)\) of \(k\) colors. A correspondence assignment specifies, for every edge \(uv\), a matching
\[
M_{uv}\subseteq L(u)\times L(v).
\]
A coloring chooses \(c(v)\in L(v)\) and avoids every matched pair.

Before sampling the graph, fix, for every unordered pair \(uv\), a bipartite relation
\[
R_{uv}\subseteq L(u)\times L(v)
\]
of maximum degree at most \(r\). These relations need not themselves be matchings. For example, \(R_{uv}\) can be the union of a predetermined menu of \(r\) matchings.

Recall that a graph is \(d\)-degenerate if every nonempty subgraph has a vertex of degree at most \(d\).

### Theorem

Fix \(p\in(0,1)\) and integers \(r\ge1\), \(d\ge0\). There is an explicit sequence
\[
k_n=\bigl(r(d+1)a+o(1)\bigr)\frac{n}{\log n}
\]
with the following property.

For every predetermined system of relations \(R_{uv}\) of maximum degree at most \(r\) on palettes of size \(k_n\), the random graph \(G=G(n,1-p)\), with probability at least \(1-n^{-2}\) for all sufficiently large \(n\), satisfies:

> Every correspondence assignment for which
> \[
> F=\{uv\in E(G):M_{uv}\nsubseteq R_{uv}\}
> \]
> is \(d\)-degenerate is colorable.

The assignment and the exceptional graph \(F\) may be chosen after seeing \(G\).

In particular:

- For \(r=1,d=0\), any correspondence assignment fixed before sampling \(G\) is a.a.s. colorable with \((a+o(1))n/\log n\) colors.
- For fixed \(r\) and \(d=0\), the matching on each edge may be chosen adversarially from a fixed menu of \(r\) matchings, after seeing the entire graph.
- For fixed \(d>0\), arbitrary correspondences are additionally permitted on any graph-dependent \(d\)-degenerate exceptional graph.

The probability estimate is uniform in the predetermined templates. It is **not** a simultaneous assertion over all choices of those templates.

## 3. Constructing mutually compatible sublists

The theorem follows from a stronger intermediate property: sufficiently large palettes contain sublists that have no template conflicts across any edge of \(G\).

### Lemma

Fix \(n,k,r,s\), with \(r,s\ge1\) and \(k\ge s\), and predetermined relations \(R_{uv}\) as above. Put
\[
m=k-s+1.
\]
For \(G=G(n,1-p)\), there is a greedy algorithm producing sets
\[
S(v)\subseteq L(v),\qquad |S(v)|=s,
\]
such that
\[
R_{uv}\cap\bigl(S(u)\times S(v)\bigr)=\varnothing
\qquad\text{for every }uv\in E(G),
\tag{1}
\]
whose failure probability is at most
\[
n\binom{k}{s-1}
\exp\!\left[
-\frac{m}{rs}\,p^{rs(n-1)/m}
\right].
\tag{2}
\]

There is no requirement concerning conflicts within one sublist; ultimately only one color will be selected from each.

### A product-space inequality

We first establish the probabilistic inequality used in the proof.

Let \(Z_1,\dots,Z_N\) be independent random variables, and let \(f_1,\dots,f_\ell\) be indicator functions of these variables. Suppose each \(Z_j\) occurs in the arguments of at most \(\rho\) functions. Then
\[
\mathbb E\prod_{c=1}^{\ell}f_c
\le
\prod_{c=1}^{\ell}(\mathbb E f_c)^{1/\rho}.
\tag{3}
\]

Indeed, the more general inequality for nonnegative functions is
\[
\mathbb E\prod_c f_c
\le
\prod_c\bigl(\mathbb E f_c^\rho\bigr)^{1/\rho}.
\]
Integrate the independent coordinates one at a time. For each coordinate, apply Hölder to the at most \(\rho\) functions depending on it, padding with constant functions \(1\) when necessary. After a set of coordinates has been integrated, the corresponding factor is
\[
\bigl(\mathbb E_{\text{integrated coordinates}}f_c^\rho\bigr)^{1/\rho}.
\]
Iteration proves the inequality. For indicators, \(f_c^\rho=f_c\), giving (3).

### Proof of the lemma

Process the vertices in the fixed order \(1,\dots,n\). At stage \(i\), expose the edges from \(i\) to earlier vertices and choose \(s\) colors that have no template conflict with any previously chosen sublist.

Condition on a successful history through stage \(i-1\). This history uses only edges with both endpoints in \([i-1]\), so the indicators of edges \(ji\), \(j<i\), remain independent, each with probability \(1-p\).

For each earlier vertex \(j\), let
\[
B_j=N_{R_{ji}}(S(j))\subseteq L(i).
\]
Since \(R_{ji}\) has maximum degree at most \(r\),
\[
|B_j|\le rs.
\]

For \(c\in L(i)\), define
\[
D_c=\{j<i:c\in B_j\},
\qquad d_c=|D_c|.
\]
Color \(c\) is available precisely when every edge \(ji\) with \(j\in D_c\) is absent. Thus
\[
\Pr(c\text{ is available}\mid\text{history})=p^{d_c}.
\tag{4}
\]
Moreover,
\[
\sum_{c\in L(i)}d_c
=\sum_{j<i}|B_j|
\le rs(i-1).
\tag{5}
\]

The availability events need not be independent. However, each edge indicator \(ji\) affects at most \(rs\) of them.

Fix \(T\subseteq L(i)\) of size \(s-1\). Applying (3) to the indicators that colors outside \(T\) are unavailable gives
\[
\begin{aligned}
&\Pr(\text{every color outside }T\text{ is unavailable}
       \mid\text{history})\\
&\qquad\le
\prod_{c\notin T}(1-p^{d_c})^{1/(rs)}
\le
\exp\!\left[-\frac1{rs}\sum_{c\notin T}p^{d_c}\right].
\end{aligned}
\tag{6}
\]
There are \(m\) colors outside \(T\). By convexity of \(x\mapsto p^x\), its monotonic decrease, and (5),
\[
\sum_{c\notin T}p^{d_c}
\ge
m\,p^{(\sum_{c\notin T}d_c)/m}
\ge
m\,p^{rs(i-1)/m}.
\tag{7}
\]

If fewer than \(s\) colors are available, all available colors lie in some set \(T\) of size \(s-1\). Consequently, the conditional failure probability at stage \(i\) is at most
\[
\binom{k}{s-1}
\exp\!\left[-\frac{m}{rs}p^{rs(i-1)/m}\right].
\]
Bounding this by its value at \(i=n\) and summing over the stages proves (2). A successful run satisfies (1) by construction. \(\square\)

## 4. Palette size and adversarial exceptions

Set
\[
s=d+1.
\]
Choose a constant \(B\ge0\) such that
\[
ae^B\ge s+2.
\]
For sufficiently large \(n\), define
\[
D_n=\log n-2\log\log n-B>0
\]
and
\[
k_n=s-1+
\left\lceil\frac{rsa\,n}{D_n}\right\rceil.
\tag{8}
\]
Then
\[
k_n=\bigl(rsa+o(1)\bigr)\frac{n}{\log n}.
\]

With \(m=k_n-s+1\), the exponent in (2) satisfies
\[
\begin{aligned}
\frac{m}{rs}p^{rs(n-1)/m}
&=\frac{m}{rs}\exp\!\left[-\frac{ars(n-1)}m\right]\\
&\ge \frac{an}{D_n}e^{-D_n}\\
&=\frac{ae^B(\log n)^2}{D_n}\\
&\ge (s+2)\log n.
\end{aligned}
\tag{9}
\]
Also \(k_n\le n\) for all sufficiently large \(n\), since \(p,r,s\) are fixed. Therefore (2) is at most
\[
n\cdot n^{s-1}\cdot n^{-(s+2)}=n^{-2}.
\tag{10}
\]

On the resulting high-probability event, fix any correspondence assignment allowed by the theorem. Let \(F\) be its \(d\)-degenerate exceptional graph.

Restrict each vertex's palette to \(S(v)\), of size \(s=d+1\). A \(d\)-degenerate graph has an ordering in which every vertex has at most \(d\) earlier neighbors. Greedily color \(F\) in such an ordering. Each already colored neighbor forbids at most one color, because its correspondence relation is a matching. Hence at most \(d\) of the \(d+1\) available colors are forbidden, so this greedy coloring succeeds.

For every edge \(uv\in E(G)\setminus E(F)\),
\[
M_{uv}\subseteq R_{uv}.
\]
Property (1) therefore guarantees that any choices from \(S(u)\) and \(S(v)\) are compatible on that edge. The greedy coloring of \(F\) is consequently a coloring of the full correspondence assignment.

This proves the theorem. Notice that the sublists were constructed without knowing the eventual assignment or exceptional graph, so the conclusion is genuinely simultaneous over all allowed choices.

## 5. The lower-bound scale

The \(n/\log n\) scale cannot be improved uniformly over the template systems: they include ordinary coloring, obtained by taking every \(R_{uv}\) to be the identity matching.

For completeness, let
\[
t=\left\lceil\frac{2}{a}\log n\right\rceil
\]
and let \(X_t\) count independent \(t\)-sets in \(G(n,1-p)\). Then
\[
\mathbb E X_t
=\binom nt p^{\binom t2}
\le
\left(\frac{en}{t}\right)^t e^{-at(t-1)/2}
=
\exp\!\left[-\left(\frac2a+o(1)\right)
               \log n\log\log n\right],
\]
which tends to zero. Thus a.a.s.
\[
\chi_{\mathrm{DP}}(G)\ge\chi(G)
\ge\frac{n}{\alpha(G)}
\ge\left(\frac a2-o(1)\right)\frac{n}{\log n}.
\]
This is the standard lower-bound mechanism, not a new improvement.

## 6. The remaining gap

The restricted theorem has quantifiers of the form
\[
\boxed{\quad
\forall\text{ predetermined templates }R,\qquad
\Pr_G\!\left[
\text{every assignment compatible with }R
\text{ up to bounded-degeneracy exceptions is colorable}
\right]=1-o(1).
\quad}
\]

The conjecture requires
\[
\boxed{\quad
\Pr_G\!\left[
\text{every correspondence assignment on }G
\text{ is colorable}
\right]=1-o(1).
\quad}
\]

These are different assertions. In the proof, the sets \(D_c\) are determined before the current random star is exposed. If the templates themselves are chosen after seeing \(G\), this independence is lost. For a fixed greedy run, an adversary knowing the current star and earlier selected colors can use \(k\) earlier neighbors to forbid all \(k\) colors at the new vertex. That defeats the greedy run—not necessarily the existence of a coloring—but shows why the conditional calculation cannot simply be extended.

Accordingly, this establishes an \(O(n/\log n)\) upper bound for a restricted, partially adaptive class of covers. It does **not** improve the quoted \(O(n/\sqrt{\log n})\) bound for unrestricted correspondence chromatic number, and it supplies neither a proof nor an interior-density counterexample to the conjecture.