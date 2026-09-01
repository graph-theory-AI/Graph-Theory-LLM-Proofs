```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The fixed-density question remains open, but G(n,p) is a.a.s. normal when np=o(1) or n(1-p)=o(1), whereas p asymptotic to c/n has a Poisson isolated-C5 obstruction and is not a.a.s. normal.",
  "would_publish": false,
  "caveats": "If p may vary arbitrarily with n, p=c/n disproves a universal affirmative statement; the intended fixed p in (0,1), including p=1/2, is not resolved."
}
```

# 1. Statement and interpretation

A graph \(G\) is normal if there are a clique cover \(\mathcal C\) and a stable-set cover \(\mathcal S\) of \(V(G)\) such that
\[
C\cap S\neq\varnothing
\qquad\text{for every }C\in\mathcal C,\ S\in\mathcal S.
\]

There are two possible readings of the question.

1. **Fixed-density reading:** \(p\in(0,1)\) is fixed as \(n\to\infty\). This includes \(p=1/2\), equivalently almost all labeled graphs.
2. **Uniform \(p(n)\) reading:** the assertion is meant for arbitrary functions \(p=p(n)\).

The second reading is false: \(p\sim c/n\) gives a positive limiting probability of an isolated \(C_5\), which is an obstruction to normality. The fixed-density problem is not resolved below.

# 2. Deterministic facts about normal covers

## 2.1 Every member of a normal cover is maximal

**Lemma 2.1.**  
If \((\mathcal C,\mathcal S)\) is a normal cover, then every \(C\in\mathcal C\) is a maximal clique and every \(S\in\mathcal S\) is a maximal stable set.

**Proof.**
Suppose \(C\in\mathcal C\) is not maximal. Then some \(x\notin C\) is adjacent to every vertex of \(C\). Choose \(S\in\mathcal S\) containing \(x\). By normality, \(C\cap S\) contains a vertex \(y\). Then \(x,y\in S\), but \(xy\in E(G)\), a contradiction.

The stable-set assertion follows by the complementary argument. \(\square\)

This observation is useful because one cannot use small nonmaximal cliques or stable sets in a normal certificate.

## 2.2 Complementation and components

**Lemma 2.2.**
A graph \(G\) is normal if and only if \(\overline G\) is normal.

**Proof.**
Swap the clique and stable-set families. \(\square\)

**Lemma 2.3.**
A graph is normal if and only if each of its connected components is normal.

**Proof.**

For the forward implication, let \(H\) be a component of a normal graph \(G\). Every clique lies in one component. Let
\[
\mathcal C_H=\{C\in\mathcal C:C\subseteq V(H)\},\qquad
\mathcal S_H=\{S\cap V(H):S\in\mathcal S\}.
\]
The first family covers \(V(H)\). Every \(S\in\mathcal S\) intersects every member of \(\mathcal C_H\), so \(S\cap V(H)\) is nonempty and the two restricted families are cross-intersecting. They therefore form a normal cover of \(H\).

Conversely, suppose the components \(H_1,\dots,H_m\) have normal covers
\((\mathcal C_i,\mathcal S_i)\). Use
\[
\mathcal C=\bigcup_i\mathcal C_i
\]
and take as stable sets all unions
\[
S_1\cup\cdots\cup S_m,\qquad S_i\in\mathcal S_i.
\]
There are no edges between components, and each such union intersects every clique in the appropriate component. \(\square\)

## 2.3 \(C_5\) is not normal

**Lemma 2.4.**
The cycle \(C_5\) is not normal.

**Proof.**
Index vertices modulo \(5\). By Lemma 2.1, the clique members must be maximal cliques, hence edges
\[
E_i=\{i,i+1\},
\]
and the stable-set members must be maximal stable sets
\[
I_j=\{j,j+2\}.
\]
One checks that
\[
E_i\cap I_j=\varnothing\quad\Longleftrightarrow\quad j=i+2\pmod 5.
\]
Thus disjointness gives a perfect matching between the five possible clique members and the five possible stable-set members.

Any edge cover of \(C_5\) uses at least three edges, and any cover by the \(I_j\)'s uses at least three stable pairs. If \(A\) and \(B\) are the corresponding index sets, cross-intersection requires
\[
B\cap(A+2)=\varnothing.
\]
But \(|A|\ge3\), so the complement of \(A+2\) has size at most \(2\), contradicting \(|B|\ge3\). \(\square\)

## 2.4 Bipartite graphs are normal

**Lemma 2.5.**
Every bipartite graph is normal.

**Proof.**
Let \(I\) be the set of isolated vertices, and let \(A,B\) be a bipartition of \(G-I\). Take
\[
\mathcal C=E(G)\cup\bigl\{\{v\}:v\in I\bigr\}
\]
and
\[
\mathcal S=\{A\cup I,\ B\cup I\}.
\]
Every nontrivial clique in \(\mathcal C\) is an edge and meets both stable sets; every singleton \(\{v\}\), \(v\in I\), meets both at \(v\). These families cover all vertices. In the edgeless case one may instead take \(\mathcal S=\{V(G)\}\). \(\square\)

# 3. Sparse random graphs

## 3.1 A positive regime

**Theorem 3.1.**
If \(np=o(1)\), then \(G(n,p)\) is normal with high probability. By complementation, the same holds if \(n(1-p)=o(1)\).

**Proof.**
Let \(Z\) denote the number of simple cycles. Then
\[
\mathbb E Z
 \le \sum_{k=3}^n\frac{(np)^k}{2k}.
\]
When \(np=o(1)\), this tends to zero. Hence \(G(n,p)\) is a forest with high probability. Every forest is bipartite, hence normal by Lemma 2.5.

The dense statement follows by applying this to \(\overline{G(n,p)}\), which has distribution \(G(n,1-p)\), and using Lemma 2.2. \(\square\)

## 3.2 A Poisson obstruction at \(p\sim c/n\)

Let \(X\) be the number of connected components isomorphic to \(C_5\).

**Theorem 3.2.**
If \(p\sim c/n\), where \(c>0\) is fixed, then
\[
X\ \xrightarrow{d}\ \operatorname{Poisson}(\lambda_c),
\qquad
\lambda_c=\frac{c^5e^{-5c}}{10}.
\]
Consequently,
\[
\limsup_{n\to\infty}\Pr\bigl(G(n,p)\text{ is normal}\bigr)
 \le e^{-\lambda_c}<1.
\]

**Proof.**
For a fixed \(5\)-set there are \(12\) possible labeled \(5\)-cycles. Such a set is a \(C_5\)-component precisely when its five cycle edges occur, its five other internal pairs are absent, and all \(5(n-5)\) edges to the rest of the graph are absent. Therefore
\[
\mathbb E X
 =\binom n5\,12p^5(1-p)^{5+5(n-5)}
 =\binom n5\,12p^5(1-p)^{5n-20}
 \longrightarrow \frac{c^5e^{-5c}}{10}.
\]

For fixed \(r\), two distinct component events contributing to \((X)_r\) must be vertex-disjoint. Thus
\[
\mathbb E (X)_r
 =\frac{(n)_{5r}}{(5!)^r}\,12^r p^{5r}
   (1-p)^{5rn+O_r(1)}
 \longrightarrow
 \left(\frac{c^5e^{-5c}}{10}\right)^r.
\]
The factorial moments therefore converge to those of the stated Poisson distribution.

If \(X\ge1\), then \(G\) has a nonnormal component by Lemma 2.4, and hence is nonnormal by Lemma 2.3. Therefore
\[
\Pr(G\text{ normal})\le \Pr(X=0)\longrightarrow e^{-\lambda_c}.
\]
\(\square\)

Applying the theorem to the complement gives the same conclusion when
\[
1-p\sim \frac cn.
\]

Thus there cannot be a universal affirmative theorem covering every function \(p=p(n)\).

# 4. Exact reformulations of the fixed-density problem

## 4.1 Rectangle-partition formulation

Let
\[
\mathcal C=\{C_1,\dots,C_r\},\qquad
\mathcal S=\{S_1,\dots,S_t\}
\]
be a normal cover. For every vertex \(v\), define
\[
A_v=\{i:v\in C_i\}\subseteq[r],\qquad
B_v=\{j:v\in S_j\}\subseteq[t].
\]

Because both families cover \(V(G)\), \(A_v,B_v\neq\varnothing\). Moreover, every clique \(C_i\) and stable set \(S_j\) intersect in exactly one vertex: they intersect by normality, and they cannot share two vertices.

It follows that the rectangles
\[
A_v\times B_v,\qquad v\in V(G),
\]
partition the whole grid \([r]\times[t]\).

Conversely, such a rectangle partition yields a normal cover provided
\[
A_u\cap A_v\neq\varnothing\ \Longrightarrow\ uv\in E(G),
\]
and
\[
B_u\cap B_v\neq\varnothing\ \Longrightarrow\ uv\notin E(G).
\]
Indeed, define \(C_i=\{v:i\in A_v\}\) and \(S_j=\{v:j\in B_v\}\).

Hence:

**Proposition 4.1.**
A graph is normal if and only if there is a partition
\[
[r]\times[t]=\mathop{\dot\bigcup}_{v\in V(G)} A_v\times B_v
\]
into nonempty combinatorial rectangles such that intersections among the \(A_v\)'s force edges and intersections among the \(B_v\)'s force nonedges.

This appears to be the core difficulty for random graphs: the partition may be chosen after observing the entire graph.

## 4.2 Irredundancy

Any normal cover can be reduced, by deleting redundant members, so that each family is an irredundant vertex cover. In such a family every member has a private vertex. Consequently,
\[
r\le n,\qquad t\le n.
\]
In the rectangle formulation, every row \(i\) has a vertex \(v\) with \(A_v=\{i\}\), and every column \(j\) has a vertex \(w\) with \(B_w=\{j\}\).

In particular, normality has certificates consisting of at most \(2n\) subsets of \(V(G)\), so deciding normality is in NP.

## 4.3 Exact SAT formulation

Let \(\mathfrak C(G)\) be the maximal cliques of \(G\), and let \(\mathfrak S(G)\) be the maximal stable sets. Introduce variables \(x_C\) and \(y_S\). By Lemma 2.1, \(G\) is normal if and only if the following formula is satisfiable:
\[
\begin{aligned}
&\bigwedge_{v\in V(G)}
  \left(\bigvee_{\substack{C\in\mathfrak C(G)\\v\in C}}x_C\right),\\
&\bigwedge_{v\in V(G)}
  \left(\bigvee_{\substack{S\in\mathfrak S(G)\\v\in S}}y_S\right),\\
&\bigwedge_{\substack{C\in\mathfrak C(G),\ S\in\mathfrak S(G)\\C\cap S=\varnothing}}
  (\neg x_C\vee\neg y_S).
\end{aligned}
\]
This gives an exact, fully specified method for exhaustive small-order computation: enumerate maximal cliques in \(G\) and \(\overline G\), construct the displayed CNF, and run a SAT solver. No numerical experiment is claimed here.

# 5. Necessary structure at fixed density

The following estimates show that every putative normal certificate in \(G(n,p)\), for fixed \(p\), is close to an entropy threshold.

Fix \(p\in(0,1)\), put \(q=1-p\), and write
\[
\gamma_p=\ln(1/p),\qquad \gamma_q=\ln(1/q).
\]
For fixed \(\varepsilon>0\), define
\[
L_p^-=\frac{\ln n-(2+\varepsilon)\ln\ln n}{\gamma_p},
\qquad
L_p^+=\frac{(2+\varepsilon)\ln n}{\gamma_p},
\]
and define \(L_q^-,L_q^+\) analogously.

**Proposition 5.1.**
With high probability:

1. every maximal clique has order between \(L_p^-\) and \(L_p^+\), up to integer rounding;
2. every maximal stable set has order between \(L_q^-\) and \(L_q^+\).

**Proof.**
For a fixed \(k\)-set, the probability that it is a maximal clique is
\[
p^{\binom k2}(1-p^k)^{n-k}.
\]
Thus the expected number of maximal \(k\)-cliques is
\[
\binom nk p^{\binom k2}(1-p^k)^{n-k}.
\]
For \(k\le L_p^-\),
\[
p^k\ge \frac{(\ln n)^{2+\varepsilon}}{n},
\]
and hence, uniformly over these \(k\),
\[
\binom nk p^{\binom k2}(1-p^k)^{n-k}
 \le
 \exp\left(O((\ln n)^2)-\tfrac12(\ln n)^{2+\varepsilon}\right).
\]
Summing over \(k\le L_p^-\) gives \(o(1)\).

For the upper bound, if \(k=\lceil L_p^+\rceil\), then
\[
\binom nk p^{\binom k2}
 =\exp\bigl(-\Omega((\ln n)^2)\bigr).
\]
Thus with high probability there is no \(k\)-clique, and hence no larger clique.

Apply the same argument to \(\overline G\sim G(n,q)\) for stable sets. \(\square\)

Now suppose \(G(n,p)\) is normal and use an irredundant normal cover with \(r\) cliques and \(t\) stable sets. Proposition 5.1 and Lemma 2.1 imply
\[
\frac{n}{L_p^+}\le r\le n,\qquad
\frac{n}{L_q^+}\le t\le n.
\]
Thus both sides of the rectangle partition have order at least \(n/\Theta(\log n)\).

Define the sets of pair constraints forced by the certificate:
\[
E^+=\bigcup_{C\in\mathcal C}\binom C2,
\qquad
E^-=\bigcup_{S\in\mathcal S}\binom S2.
\]
The pairs in \(E^+\) must be edges and those in \(E^-\) must be nonedges. They are disjoint.

Every vertex belongs to a clique of size at least \(L_p^-\), so the graph \((V,E^+)\) has minimum degree at least \(L_p^- -1\). Similarly, \((V,E^-)\) has minimum degree at least \(L_q^- -1\). Therefore
\[
|E^+|\ge \frac n2(L_p^--1),\qquad
|E^-|\ge \frac n2(L_q^--1).
\]
Consequently,
\[
\gamma_p|E^+|+\gamma_q|E^-|
 \ge n\ln n-(2+\varepsilon)n\ln\ln n-O_p(n).
\]

For a fixed incidence template, the probability that all these designated pairs have the required status is
\[
p^{|E^+|}q^{|E^-|}
 \le
 \exp\left(
   -n\ln n+(2+\varepsilon)n\ln\ln n+O_p(n)
 \right).
\]

For \(p=1/2\), this becomes
\[
|E^+|+|E^-|
 \ge n\log_2 n-(2+\varepsilon)n\log_2\ln n-O(n).
\]
Thus any normal certificate for a typical fixed-density random graph must force almost \(n\log_2 n\) pair statuses.

# 6. Why this does not settle fixed \(p\)

The preceding constraint count is near, but below, the entropy available from relabeling. For one fixed unlabeled template, multiplying the probability bound by \(n!\) gives only
\[
n!\exp\left(
-n\ln n+(2+\varepsilon)n\ln\ln n+O(n)
\right)
=
\exp\left((2+\varepsilon)n\ln\ln n+O(n)\right),
\]
which is not \(o(1)\). Moreover, there are many possible rectangle-partition templates, all chosen adaptively from the graph.

Accordingly, the argument proves neither existence nor nonexistence of a compatible rectangle partition for fixed \(p\). In particular, it does not resolve \(p=1/2\).

# 7. Conclusions and gaps

- If \(p=p(n)\) is unrestricted, a universal affirmative answer is false: \(p\sim c/n\) is not a.a.s. normal.
- If \(np=o(1)\), or symmetrically \(n(1-p)=o(1)\), normality holds with high probability.
- For fixed \(p\in(0,1)\), every possible certificate has a precise large rectangle-partition structure and forces nearly \(n\log n\) edge/nonedge decisions.
- The unresolved step is to prove that a fixed-density random graph a.a.s. does, or does not, admit one of these adaptive rectangle partitions.