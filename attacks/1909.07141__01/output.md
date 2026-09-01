```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An extremal common-arc lemma proves the conjecture for equal demands, more generally for n−1 equal demands, and settles n=3 when two demands coincide or one demand is 1/2.",
  "would_publish": false,
  "caveats": "The case n=3 with three distinct positive demands, none equal to 1/2, remains unresolved; no counterexample is constructed."
}
```

## 1. Reformulation

Write
\[
\alpha(P)=\sum_{i\in P}\alpha_i.
\]
Since all measures are probability measures,
\[
\min_{j\in Q}\mu_j(X^c)
 =1-\max_{j\in Q}\mu_j(X).
\]
Thus the desired conclusion is equivalent to finding a proper nonempty \(P\subset[n]\), an arc \(X\), and \(a=\alpha(P)\) such that
\[
\mu_i(X)\ge a\quad(i\in P),\qquad
\mu_j(X)\le a\quad(j\notin P),
\]
with equality attained by at least one index on each side.

Endpoints of arcs are immaterial because the measures are nonatomic.

## 2. An extremal common-arc lemma

### Lemma 2.1
Let \(\mu_1,\dots,\mu_m\) be nonatomic probability measures on \(S^1\), where \(m\ge2\), and let \(0<t<1\). Then there are distinct indices \(r,s\) and an arc \(X\) such that
\[
\mu_r(X)=\mu_s(X)=t
\quad\text{and}\quad
\mu_k(X)\le t\qquad\text{for every }k.
\tag{2.1}
\]
Dually, there are distinct \(r,s\) and an arc \(Y\) such that
\[
\mu_r(Y)=\mu_s(Y)=t
\quad\text{and}\quad
\mu_k(Y)\ge t\qquad\text{for every }k.
\tag{2.2}
\]

### Proof

First suppose every \(\mu_i\) has full support. Identify \(S^1\) with \(\mathbb R/\mathbb Z\), with a fixed orientation. Each \(\mu_i\) has a continuous strictly increasing cumulative lift
\[
H_i:\mathbb R\longrightarrow\mathbb R,\qquad
H_i(x+1)=H_i(x)+1,
\]
such that
\[
\mu_i([x,y])=H_i(y)-H_i(x)
\qquad (x\le y\le x+1).
\]

For \(0<t<1\), define
\[
T_i^t(x)=H_i^{-1}(H_i(x)+t).
\]
Thus \(T_i^t(x)\in(x,x+1)\) is the unique endpoint for which
\[
\mu_i([x,T_i^t(x)])=t.
\]

We first record the two-measure coincidence property:
\[
\text{for every }i\ne j,\quad
T_i^t(x)=T_j^t(x)\text{ for some }x.
\tag{2.3}
\]
Indeed, otherwise their difference has constant sign. Suppose, for example,
\[
T_i^t(x)<T_j^t(x)\qquad\text{for all }x.
\]
Then
\[
\mu_j([x,T_i^t(x)])<t\qquad\text{for all }x.
\]
Put \(u=H_i(x)\), and let \(\nu=(H_i)_\#\mu_j\). The last inequality becomes
\[
\nu([u,u+t])<t\qquad\text{for every }u.
\]
But Fubini gives
\[
\int_0^1 \nu([u,u+t])\,du
 =\int_{S^1}\bigl|\{u:z\in[u,u+t]\}\bigr|\,d\nu(z)
 =t,
\]
a contradiction. This is a self-contained proof of the relevant two-measure Stromquist–Woodall statement.

Now consider the lower envelope
\[
L(x)=\min_{1\le i\le m}T_i^t(x).
\]
If two functions attain \(L(x)\) at some \(x\), say
\[
T_r^t(x)=T_s^t(x)=y=L(x),
\]
then \(X=[x,y]\) satisfies
\[
\mu_r(X)=\mu_s(X)=t.
\]
For every \(k\), \(T_k^t(x)\ge y\), hence
\[
\mu_k(X)\le t.
\]
This proves (2.1).

It remains only to see that a tie on the lower envelope must occur. If the minimizing index were unique for every \(x\), it would be locally constant and hence constant on the connected circle. Thus some \(r\) would satisfy
\[
T_r^t(x)<T_s^t(x)\qquad\text{for every }x
\]
for every \(s\ne r\), contradicting (2.3).

For arbitrary nonatomic measures, put
\[
\mu_i^\varepsilon=(1-\varepsilon)\mu_i+\varepsilon\lambda,
\]
where \(\lambda\) is normalized Lebesgue measure. Apply the full-support case to obtain arcs \(X_\varepsilon\) and tied indices \(r_\varepsilon,s_\varepsilon\). After passing to a subsequence, the two indices are fixed and the oriented arcs converge in the compact space \(S^1\times[0,1]\). Arc masses depend continuously on their endpoints for nonatomic measures. Since
\[
\left|\mu_i^\varepsilon(A)-\mu_i(A)\right|\le\varepsilon
\]
for every Borel set \(A\), the limiting arc satisfies (2.1).

Finally, (2.2) follows by applying (2.1) at level \(1-t\) and taking complements. ∎

## 3. Consequences for the conjecture

### Theorem 3.1: \(n-1\) equal demands

Suppose that at least \(n-1\) of the demands are equal to the same number \(t\). Then Conjecture 3.1 holds.

#### Proof

Apply Lemma 2.1 at level \(t\). We obtain distinct \(r,s\) and an arc \(X\) such that
\[
\mu_r(X)=\mu_s(X)=t,\qquad \mu_k(X)\le t\quad\forall k.
\]
Since there is at most one index whose demand is not \(t\), at least one of \(r,s\), say \(r\), satisfies \(\alpha_r=t\). Put
\[
P=\{r\},\qquad Q=[n]\setminus\{r\}.
\]
Then
\[
\min_{i\in P}\mu_i(X)=t=\alpha(P).
\]
Moreover \(s\in Q\), so
\[
\max_{j\in Q}\mu_j(X)=t.
\]
Consequently
\[
\min_{j\in Q}\mu_j(X^c)
 =1-t
 =\alpha(Q).
\]
∎

This includes:

- the equal-demand case \(\alpha_1=\cdots=\alpha_n=1/n\);
- the complete \(n=2\) case;
- for \(n=3\), every instance in which two demands coincide.

If some demand is zero, the conclusion follows under the standard convention that degenerate circular intervals are permitted: choose \(P=\{i\}\) with \(\alpha_i=0\) and let \(X\) be a singleton. Every nonatomic measure assigns \(X\) mass \(0\) and \(X^c\) mass \(1\).

### Theorem 3.2: a half-demand for \(n=3\)

For \(n=3\), the conjecture holds whenever one of the demands equals \(1/2\).

#### Proof

Suppose \(\alpha_i=1/2\), and let \(j,k\) be the other two indices. By the two-measure part of Lemma 2.1, there is an arc \(Y\) such that
\[
\mu_i(Y)=\mu_j(Y)=\frac12.
\]
Its complement also has mass \(1/2\) for both \(\mu_i\) and \(\mu_j\). Since
\[
\mu_k(Y)+\mu_k(Y^c)=1,
\]
one of \(Y,Y^c\), call it \(X\), satisfies \(\mu_k(X)\le1/2\). Hence
\[
\mu_i(X)=\mu_j(X)=\frac12,\qquad \mu_k(X)\le\frac12.
\]
Taking \(P=\{i\}\) and \(Q=\{j,k\}\) proves the assertion. ∎

### Theorem 3.3: affinely collinear measures

The conjecture holds for arbitrary \(n\) if the measures \(\mu_1,\dots,\mu_n\) have affine span of dimension at most one in the vector space of signed measures.

#### Proof

If all measures coincide, choose any arc of the required common mass. Otherwise, choose two distinct measures \(\mu_r,\mu_s\) spanning their affine line. Every measure has the form
\[
\mu_i=(1-c_i)\mu_r+c_i\mu_s
\]
for some real \(c_i\).

Choose a proper nonempty \(P\) with \(0<\alpha(P)<1\), and put \(t=\alpha(P)\). The two-measure coincidence theorem supplies an arc \(X\) with
\[
\mu_r(X)=\mu_s(X)=t.
\]
Therefore \(\mu_i(X)=t\) for every \(i\). It follows immediately that
\[
\min_{i\in P}\mu_i(X)=t=\alpha(P)
\]
and
\[
\min_{j\notin P}\mu_j(X^c)=1-t=\alpha([n]\setminus P).
\]
The degenerate demand cases are handled as above. ∎

## 4. An exact description of the remaining \(n=3\) obstruction

For three measures and \(0<t<1\), call an index \(i\) **good at level \(t\)** if there is an arc \(X\) such that
\[
\mu_i(X)=t,\qquad
\mu_j(X)\le t\quad(j\ne i),
\]
and equality holds for at least one \(j\ne i\).

Thus, if \(\alpha_i=t\), goodness of \(i\) at \(t\) gives the conjectured partition with \(P=\{i\}\).

Let
\[
G(t)=\{i:i\text{ is good at }t\},\qquad
B_i=\{t:i\notin G(t)\}.
\]

### Proposition 4.1

For any three nonatomic probability measures:

1. \(|G(t)|\ge2\) for every \(0<t<1\).
2. For each \(i\),
   \[
   t\in B_i\implies 1-t\notin B_i.
   \tag{4.1}
   \]
3. For positive demands \(\alpha_1,\alpha_2,\alpha_3\), the conjecture fails exactly when
   \[
   \alpha_i\in B_i\qquad(i=1,2,3).
   \tag{4.2}
   \]

#### Proof

Part 1 is exactly Lemma 2.1: the two tied indices \(r,s\) are both good.

For part 2, suppose \(i\) is bad at \(t\). Choose \(j\ne i\), and let \(k\) be the third index. There is an arc \(X\) with
\[
\mu_i(X)=\mu_j(X)=t.
\]
Since \(i\) is bad at \(t\), necessarily
\[
\mu_k(X)>t.
\]
Therefore
\[
\mu_i(X^c)=\mu_j(X^c)=1-t,\qquad
\mu_k(X^c)<1-t,
\]
so \(i\) is good at \(1-t\).

For part 3, every bipartition of a three-element set has a singleton side. If the singleton is \(Q\), replace \(X\) by \(X^c\) and interchange \(P,Q\). Hence every solution can be represented with \(P=\{i\}\) for some \(i\), and such a solution is exactly goodness of \(i\) at \(t=\alpha_i\). ∎

This proposition gives short alternative explanations for the preceding \(n=3\) cases:

- if \(\alpha_i=\alpha_j=t\), then \(i,j\) cannot both be bad at \(t\), since at most one label is bad at any fixed level;
- if \(\alpha_i=1/2\), then (4.1) prevents \(i\) from being bad.

It also gives the following “five out of six” result.

### Corollary 4.2

Fix three measures and three distinct positive demand values \(a,b,c\) summing to \(1\). Among the six ways to assign these demand values to the three measures, at most one assignment can fail the conjecture.

#### Proof

At each fixed level \(t\), there is at most one bad label. A failing assignment must assign each of \(a,b,c\) to its unique bad label at that level. This determines at most one bijection between demand values and labels. ∎

## 5. Quantile-map certificate for \(n=3\)

For full-support nonatomic measures, the obstruction has a particularly concrete form. Retain the maps
\[
T_i^t(x)=H_i^{-1}(H_i(x)+t).
\]

An index \(i\) is good at \(t\) if and only if its graph attains the lower envelope:
\[
\exists x\qquad
T_i^t(x)=\min_r T_r^t(x).
\tag{5.1}
\]

Indeed, if the minimum is tied, the corresponding arc immediately witnesses goodness. If \(i\) is the unique minimizer somewhere, the set where it is the unique minimizer is open. It cannot be the entire circle by the pairwise coincidence theorem. At a boundary point, \(i\) remains a minimizer and ties another map, again giving goodness.

Consequently,
\[
t\in B_i
\quad\Longleftrightarrow\quad
T_i^t(x)>\min_{j\ne i}T_j^t(x)
\quad\text{for every }x.
\tag{5.2}
\]

Thus a smooth or full-support counterexample for \(n=3\) is exactly a triple satisfying
\[
T_i^{\alpha_i}(x)>
\min_{j\ne i}T_j^{\alpha_i}(x)
\qquad\text{for all }x,\ i=1,2,3.
\tag{5.3}
\]

This is also an exact finite computational criterion for positive piecewise-constant densities on a common rational mesh:

1. Construct the piecewise-linear cumulative lifts \(H_i\).
2. For each target \(t=\alpha_i\), construct
   \[
   T_r^t=H_r^{-1}(H_r+t),\qquad r=1,2,3.
   \]
3. Refine the domain by all breakpoints of these maps and all intersections \(T_j^t=T_k^t\).
4. On each resulting interval, the lower envelope of \(T_j^t,T_k^t\) is affine. Check exactly whether
   \[
   T_i^t-\min(T_j^t,T_k^t)>0
   \]
   throughout the interval.
5. If all three strict inequalities are certified, the densities form an explicit \(n=3\) counterexample. If one fails, (5.1) yields a solution.

For rational data, every step can be carried out using exact rational arithmetic. I have not executed such a search here.

## 6. Remaining gap

The unresolved case is already:

\[
n=3,\qquad
0<\alpha_1,\alpha_2,\alpha_3<1,
\]
with the three demands distinct and none equal to \(1/2\), and with an affinely independent triple of measures.

A counterexample would require
\[
\alpha_i\in B_i\quad(i=1,2,3),\qquad
\alpha_1+\alpha_2+\alpha_3=1,
\]
where the bad-level sets satisfy:

- at most one \(B_i\) contains any fixed \(t\);
- \(B_i\cap(1-B_i)=\varnothing\);
- for full-support measures, each \(B_i\) is open.

These set-theoretic properties alone do not yield a contradiction: disjoint small intervals around, for example, \(0.17,0.29,0.54\) satisfy them abstractly. What is missing is an additional constraint coming from the fact that all three \(B_i\) arise from the same three quantile flows \(T_i^t\).

Accordingly, this is not a proof or disproof of the full conjecture. The main rigorous progress is Lemma 2.1, its general equal-demand consequences, and the exact reduction (5.3) of the remaining \(n=3\) problem.