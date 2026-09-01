```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but the desired exponential bound holds for families of bounded dual-laminarity and for shifted families, while bounded pairwise intersections give a stronger polynomial bound.",
  "would_publish": false,
  "caveats": "These structural hypotheses do not follow from bounded VC-dimension, and the unrestricted VC-dimension-2 case remains open."
}
```

# Partial results toward the bounded-VC sunflower conjecture

## 1. Statement and scope

For a family \(\mathcal F\) of distinct \(k\)-element subsets of a ground set \(X\), sets
\[
A_1,\ldots,A_r\in\mathcal F
\]
form an \(r\)-sunflower if all pairwise intersections \(A_i\cap A_j\), \(i\ne j\), are equal.

The conjecture asks whether, for fixed \(d\) and \(r\), every \(r\)-sunflower-free \(k\)-uniform family of VC-dimension at most \(d\) has cardinality at most \(C(d,r)^k\).

I do not resolve the conjecture for \(d\ge2\). Below are several self-contained partial results and a reduction identifying a remaining hard subclass. I do not claim novelty for the elementary special cases.

---

## 2. Families of bounded dual-laminarity

For each \(x\in X\), define its incidence support
\[
P_x:=\{A\in\mathcal F:x\in A\}\subseteq\mathcal F.
\]

Call a collection of subsets laminar if any two of its members are nested or disjoint. Define the **dual-laminarity number** \(\lambda(\mathcal F)\) to be the least \(q\) for which the support of \(\mathcal F\) can be partitioned as
\[
X=X_1\cup\cdots\cup X_q
\]
so that, for each \(a\in[q]\), the collection \(\{P_x:x\in X_a\}\) is laminar.

### Theorem 2.1

Let \(q\ge1\) and \(r\ge3\). If \(\mathcal F\) is \(k\)-uniform, \(r\)-sunflower-free, and
\(\lambda(\mathcal F)\le q\), then
\[
|\mathcal F|\le \bigl(2q(r-1)\bigr)^k.
\]
For \(q=1\), the sharper bound
\[
|\mathcal F|\le (r-1)^k
\]
holds.

Moreover,
\[
\lambda(\mathcal F)\le q\quad\Longrightarrow\quad
\operatorname{VCdim}(\mathcal F)\le q.
\]

### Proof

Let \(V=\mathcal F\), viewing the members of \(\mathcal F\) as vertices. A basic incidence observation is that distinct \(A_1,\ldots,A_r\) form a sunflower if and only if
\[
|P_x\cap\{A_1,\ldots,A_r\}|\in\{0,1,r\}
\qquad\text{for every }x\in X. \tag{2.1}
\]
Indeed, a ground point occurring in between \(2\) and \(r-1\) of the selected sets belongs to some pairwise intersections but not all of them. Conversely, points occurring zero, once, or \(r\) times contribute either to none or to all pairwise intersections.

Set
\[
L:=2q(r-1).
\]
We prove \(|\mathcal F|\le L^k\) by induction on \(k\).

The assertion is clear for \(k=0\), since a set family contains at most one empty set. If \(\bigcap\mathcal F\ne\varnothing\), delete the entire common intersection. This preserves cardinality, sunflower-freeness, and dual-laminarity, while decreasing the uniformity. Thus the induction hypothesis applies. We may consequently assume
\[
\bigcap\mathcal F=\varnothing. \tag{2.2}
\]

For each color \(a\in[q]\), let \(\mathcal M_a\) be the collection of distinct inclusion-maximal nonempty supports \(P_x\) with \(x\in X_a\). Members of \(\mathcal M_a\) are pairwise disjoint by laminarity, and every support of color \(a\) is contained in one of them.

Define a graph \(G\) on \(V\) by joining \(A,B\) if they lie together in some member of some \(\mathcal M_a\). If \(R\subseteq V\) is independent in \(G\), every incidence support \(P_x\) meets \(R\) in at most one vertex. Therefore an independent set of order \(r\) would satisfy (2.1), giving an \(r\)-sunflower. Hence
\[
\alpha(G)\le r-1. \tag{2.3}
\]

Let \(m=|V|\), and let
\[
M:=\max\{|B|:B\in\mathcal M_a,\ a\in[q]\}.
\]
If \(m\ge2(r-1)\), then the complement of \(G\) is \(K_r\)-free. The standard Turán estimate gives
\[
e(G)\ge
\binom m2-\left(1-\frac1{r-1}\right)\frac{m^2}{2}
\ge \frac{m^2}{4(r-1)}. \tag{2.4}
\]
On the other hand,
\[
\begin{aligned}
e(G)
&\le \sum_{a=1}^q\sum_{B\in\mathcal M_a}\binom{|B|}{2}\\
&\le \frac{M}{2}\sum_{a=1}^q\sum_{B\in\mathcal M_a}|B|
\le \frac{qMm}{2},
\end{aligned}
\]
because the maximal supports of a fixed color are disjoint. Comparing this with (2.4) yields
\[
M\ge \frac{m}{2q(r-1)}=\frac mL. \tag{2.5}
\]

Choose a maximal support \(B\) of size \(M\). It equals \(P_x\) for some ground point \(x\), so every member of \(B\) contains \(x\). Restrict the set family to the members indexed by \(B\) and delete their entire common intersection. The resulting family

* is uniform of size at most \(k-1\);
* remains \(r\)-sunflower-free;
* consists of distinct sets;
* still has dual-laminarity number at most \(q\), because the new incidence supports are restrictions \(P_y\cap B\) of the old ones.

By induction,
\[
M\le L^{k-1}.
\]
Together with (2.5), this gives \(m\le L^k\).

If \(m<2(r-1)\), then \(m\le L\le L^k\) for \(k\ge1\). This proves the general bound.

For \(q=1\), after deleting the common intersection, the inclusion-maximal supports are disjoint and cover \(V\). If there were at least \(r\) of them, choosing one member from each would produce an \(r\)-sunflower. Thus there are at most \(r-1\) maximal supports. Applying induction separately inside each support gives
\[
|\mathcal F|\le (r-1)(r-1)^{k-1}=(r-1)^k.
\]

Finally, suppose \(\lambda(\mathcal F)\le q\) and that \(q+1\) ground points are shattered. Two of them, say \(x,y\), have the same laminar color. Shattering would realize all four membership patterns \(00,01,10,11\) on \(x,y\). This is impossible when \(P_x,P_y\) are nested or disjoint. Hence \(\operatorname{VCdim}(\mathcal F)\le q\). ∎

### Limitation

Bounded VC-dimension does not bound \(\lambda(\mathcal F)\). An explicit VC-dimension-\(2\) example with arbitrarily large dual-laminarity appears in Section 6 below. Thus Theorem 2.1 is a genuine subclass result, not a proof of the conjecture.

---

## 3. Shifted families

Let the ground set be linearly ordered. A \(k\)-uniform family \(\mathcal F\) is **shifted** if whenever \(A\in\mathcal F\), \(j\in A\), \(i<j\), and \(i\notin A\), then
\[
(A\setminus\{j\})\cup\{i\}\in\mathcal F.
\]

### Theorem 3.1

Every shifted, \(k\)-uniform, \(r\)-sunflower-free family satisfies
\[
|\mathcal F|\le (r-1)^k.
\]

### Proof

Write
\[
A=\{a_1<a_2<\cdots<a_k\}\in\mathcal F,
\qquad a_0:=0.
\]
Suppose that
\[
a_i-a_{i-1}\ge r
\]
for some \(i\). Choose \(r\) distinct integers
\[
x_1,\ldots,x_r\in\{a_{i-1}+1,\ldots,a_i\}.
\]
By shiftedness, all sets
\[
A_j=(A\setminus\{a_i\})\cup\{x_j\},\qquad j\in[r],
\]
belong to \(\mathcal F\). They form an \(r\)-sunflower with core \(A\setminus\{a_i\}\), a contradiction.

Consequently,
\[
1\le a_i-a_{i-1}\le r-1
\qquad\text{for every }i.
\]
The set \(A\) is therefore determined by a vector of \(k\) increments, each chosen from \(\{1,\ldots,r-1\}\). There are at most \((r-1)^k\) such vectors. ∎

### Why shifting does not prove the conjecture

Ordinary shifts need not preserve sunflower-freeness, even for VC-dimension \(2\).

Let
\[
\mathcal C=\{12,23,34,45,15\},
\]
the edge family of the \(5\)-cycle. It contains no \(3\)-sunflower: it has neither three disjoint edges nor three edges through one vertex. Its VC-dimension is \(2\).

Apply the usual \((1,3)\)-shift. The edge \(34\) becomes \(14\), while \(23\) remains because its shifted image \(12\) was already present. The resulting family contains
\[
12,\ 14,\ 15,
\]
which is a \(3\)-sunflower with core \(\{1\}\). Thus compression cannot simply reduce the general conjecture to Theorem 3.1.

---

## 4. Families with bounded pairwise intersections

### Theorem 4.1

Let \(0\le s\le k-1\). Suppose that \(\mathcal F\) is \(k\)-uniform, \(r\)-sunflower-free, and
\[
|A\cap B|\le s
\qquad\text{for all distinct }A,B\in\mathcal F.
\]
Then
\[
|\mathcal F|
\le (r-1)^{s+1}(k)_s, \tag{4.1}
\]
where
\[
(k)_s=k(k-1)\cdots(k-s+1),\qquad (k)_0=1.
\]

### Proof

Induct on \(s\).

For \(s=0\), the members are pairwise disjoint, so sunflower-freeness gives
\[
|\mathcal F|\le r-1.
\]

Suppose \(s\ge1\). Because \(r\) pairwise disjoint members would be an \(r\)-sunflower with empty core, the matching number of \(\mathcal F\) is at most \(r-1\). Let \(A_1,\ldots,A_t\) be a maximal matching and put
\[
U=A_1\cup\cdots\cup A_t.
\]
Then
\[
|U|\le (r-1)k,
\]
and \(U\) meets every member of \(\mathcal F\).

For \(x\in U\), let
\[
\mathcal F_x=\{A\setminus\{x\}:A\in\mathcal F,\ x\in A\}.
\]
This is a \((k-1)\)-uniform, \(r\)-sunflower-free family, and any two of its members intersect in at most \(s-1\) points. By induction,
\[
|\mathcal F_x|
\le (r-1)^s(k-1)_{s-1}.
\]
Since every member of \(\mathcal F\) meets \(U\),
\[
\begin{aligned}
|\mathcal F|
&\le \sum_{x\in U}|\mathcal F_x|\\
&\le (r-1)k\,(r-1)^s(k-1)_{s-1}\\
&=(r-1)^{s+1}(k)_s.
\end{aligned}
\]
∎

### Consequences

1. For fixed \(s\), the bound is polynomial in \(k\), much stronger than the conjectured exponential bound.

2. Such a family automatically has
   \[
   \operatorname{VCdim}(\mathcal F)\le s+1.
   \]
   Indeed, if a set \(Y\) of size \(s+2\) were shattered, there would be members whose traces on \(Y\) are \(Y\) and \(Y\setminus\{y\}\). Their intersection would contain \(s+1\) points.

3. In particular, a linear hypergraph—one with pairwise intersections of order at most \(1\)—has VC-dimension at most \(2\), and a \(k\)-uniform \(r\)-sunflower-free linear hypergraph has
   \[
   |\mathcal F|\le (r-1)^2k.
   \]

4. More generally, if
   \[
   s\le \frac{\alpha k}{\log k},
   \]
   then (4.1) gives
   \[
   |\mathcal F|\le C(\alpha,r)^k.
   \]
   Indeed,
   \[
   \log|\mathcal F|
   \le \log(r-1)+s\log\bigl((r-1)k\bigr)
   =O_{\alpha,r}(k).
   \]

The limitation is that bounded VC-dimension does not bound pairwise intersection sizes; tree-like VC-dimension-\(1\) families may have intersections of size \(k-1\).

---

## 5. Reduction to low-matching residual families

There is a useful reduction which, for \(r=3\), isolates the intersecting case.

### Proposition 5.1

Let \(\mathcal F\) be \(k\)-uniform, \(r\)-sunflower-free, and let \(A\in\mathcal F\). For each trace \(T\subseteq A\), define
\[
\mathcal R_T
=
\{B\setminus A:B\in\mathcal F,\ B\cap A=T\}.
\]
Then:

1. \(\mathcal R_T\) is \((k-|T|)\)-uniform and \(r\)-sunflower-free;
2. \(\operatorname{VCdim}(\mathcal R_T)\le \operatorname{VCdim}(\mathcal F)\);
3. for \(T\ne A\),
   \[
   \nu(\mathcal R_T)\le r-2.
   \]

Moreover, if \(\operatorname{VCdim}(\mathcal F)\le d\), the number of nonempty trace cells is at most
\[
\sum_{i=0}^{\min(d,k)}\binom{k}{i}. \tag{5.1}
\]

### Proof

The first two assertions follow by restriction. If \(r\) residual sets formed a sunflower, adjoining the fixed trace \(T\) would give an \(r\)-sunflower in \(\mathcal F\).

For the matching assertion, suppose that
\[
R_1,\ldots,R_{r-1}\in\mathcal R_T
\]
are pairwise disjoint. Let the corresponding original sets be \(B_1,\ldots,B_{r-1}\). Then
\[
A\cap B_i=T
\quad\text{and}\quad
B_i\cap B_j=T
\]
for all \(i\ne j\). Thus
\[
A,B_1,\ldots,B_{r-1}
\]
form an \(r\)-sunflower, a contradiction.

Finally, (5.1) is the Sauer bound applied to the trace family \(\{B\cap A:B\in\mathcal F\}\). ∎

For \(r=3\), every nontrivial \(\mathcal R_T\) is intersecting. Consequently, it would suffice to prove the exponential conjecture for intersecting, \(3\)-sunflower-free families of VC-dimension at most \(d\). Indeed, the polynomial number of trace cells in (5.1) can be absorbed into the exponential base.

This is a genuine narrowing, but the intersecting VC-dimension-\(2\) case remains nontrivial.

---

## 6. A barrier to constant-transversal arguments

For \(m\ge4\), let the ground set be the edges of \(K_m\):
\[
X=\binom{[m]}2.
\]
For each \(i\in[m]\), define the vertex-star
\[
F_i=\{\{i,j\}:j\ne i\}.
\]
Then \(\mathcal F_m=\{F_i:i\in[m]\}\) has the following properties:

* it is \(k\)-uniform with \(k=m-1\);
* it is intersecting;
* it is \(3\)-sunflower-free;
* its VC-dimension is exactly \(2\);
* its transversal number is \(\lceil m/2\rceil\), hence unbounded.

Indeed,
\[
F_i\cap F_j=\{\{i,j\}\}.
\]
For three distinct indices \(i,j,\ell\), the three pairwise intersections are the three distinct ground points
\[
\{i,j\},\quad \{i,\ell\},\quad \{j,\ell\},
\]
so there is no \(3\)-sunflower.

To see that the VC-dimension is at least \(2\), the two ground points \(\{1,2\},\{1,3\}\) are shattered by \(F_1,F_2,F_3,F_4\). Three ground points cannot be shattered: if no graph vertex is incident with all three corresponding edges, the full trace is missing; if all three form a graph star, no vertex is incident with exactly two of them.

A transversal of \(\mathcal F_m\) is precisely an edge cover of \(K_m\), and hence has size at least \(\lceil m/2\rceil\). Thus even an intersecting, \(3\)-sunflower-free VC-dimension-\(2\) family need not have a hitting set of size bounded solely in terms of \(d\) and \(r\).

This example also shows why Theorem 2.1 does not cover all VC-dimension-\(2\) families. Here
\[
P_{\{i,j\}}=\{F_i,F_j\}.
\]
For fixed \(i\), the \(m-1\) supports \(P_{\{i,j\}}\) pairwise cross, so they require distinct laminar colors. Hence
\[
\lambda(\mathcal F_m)\ge m-1.
\]

---

## 7. A popular-point diagnostic

Let \(\mathcal G\) be a \(k\)-uniform family of size \(M\), let
\[
C=\bigcap\mathcal G,\qquad \ell=k-|C|,
\]
and put \(b=\binom r2\).

### Lemma 7.1

If \(M\ge r\) and
\[
|\{A\in\mathcal G:x\in A\}|
\le \frac{M}{4b\ell}
\qquad\text{for every }x\notin C, \tag{7.1}
\]
then \(\mathcal G\) contains an \(r\)-sunflower.

### Proof

Choose \(r\) distinct members uniformly without replacement. For \(x\notin C\), let \(q_x\) be the fraction of members containing \(x\). Then
\[
\sum_{x\notin C}q_x=\ell.
\]
For any fixed pair of sampled sets, the probability that both contain \(x\) is at most \(2q_x^2\). Thus the probability that some selected pair meets outside \(C\) is at most
\[
2b\sum_{x\notin C}q_x^2
\le 2b\left(\max_xq_x\right)\sum_xq_x
\le \frac12
\]
by (7.1). Therefore there is a choice of \(r\) distinct members whose residuals outside \(C\) are pairwise disjoint. They form an \(r\)-sunflower with core \(C\). ∎

Consequently, every sunflower-free subfamily of size at least \(r\) has a noncore point lying in a proportion \(\Omega_r(1/\ell)\) of its members. Repeatedly conditioning on such a point decreases \(\ell\), but in the worst case incurs a product of losses comparable to
\[
k(k-1)\cdots1=k!.
\]
This recovers the source of the classical factorial bound. To prove the conjecture by this route, one needs to show that bounded VC-dimension amortizes these successive \(1/\ell\) losses down to a constant loss per element. The examples above show that neither a constant transversal nor bounded dual-laminarity is available in general.

---

## 8. Remaining gap

The partial results cover several natural extremes:

* nested/tree-like incidence structure: Theorem 2.1;
* fully shifted families: Theorem 3.1;
* uniformly small pairwise intersections: Theorem 4.1.

They do not control arbitrary mixtures of deep nested intersections and many crossing incidence supports. The first unresolved case remains \(d=2,r=3\), equivalently up to the trace reduction, the intersecting \(3\)-sunflower-free VC-dimension-\(2\) case.

Thus no proof or counterexample to Conjecture 1.1 is obtained. The global \(C(d,r)^k\) bound remains open under the literature status supplied in the question.