```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound is proved and shown sharp for valuations whose pairwise likelihood ratios cross every level at most twice, but arbitrary valuations remain unresolved.",
  "would_publish": false,
  "caveats": "The upper proof relies essentially on the two-crossing hypothesis; likelihood ratios for general valuations may oscillate arbitrarily often."
}
```

# 1. Precise formulation

Let \(\mu_1,\ldots,\mu_n\) be nonatomic Borel probability measures on \([0,1]\), and let
\[
\alpha_1,\ldots,\alpha_n>0,\qquad \sum_{i=1}^n\alpha_i=1.
\]
An allocation is a measurable partition \(A_1,\ldots,A_n\) of the cake. It is fair if
\[
\mu_i(A_i)\geq \alpha_i\qquad (1\leq i\leq n).
\]
An allocation uses at most \(k\) cuts if there are
\[
0=x_0\leq x_1\leq\cdots\leq x_k\leq x_{k+1}=1
\]
such that every interval \([x_j,x_{j+1}]\) is assigned wholly to one agent, up to endpoints of measure zero.

The conjecture is that every instance has a fair allocation using at most \(2n-2\) cuts. The supplied source proves \(3n-4\).

I do not prove the general conjecture. I prove it, sharply, for a substantial class of smooth valuations.

# 2. A sharp two-crossing theorem

## Theorem 2.1

Suppose that every \(\mu_i\) has a strictly positive continuous density \(f_i\) on \([0,1]\), and that for every distinct \(i,j\) and every \(q>0\), the equation
\[
f_i(x)=qf_j(x)
\]
has at most two solutions \(x\in[0,1]\).

Then every demand vector \(\alpha\) admits a fair allocation with at most
\[
2n-2
\]
cuts.

The bound is sharp even within this class.

The hypothesis says that every pairwise likelihood ratio \(f_i/f_j\) crosses each horizontal level at most twice.

## 2.1. Supported approximately fair allocations

A fractional allocation is a tuple of measurable functions
\[
p_i:[0,1]\longrightarrow[0,1],\qquad \sum_i p_i(x)=1
\]
almost everywhere. Its utility vector is
\[
u_i(p)=\int_0^1p_i(x)f_i(x)\,dx.
\]
Let \(\mathcal V\subseteq\mathbb R^n\) be the set of all such utility vectors. This is compact and convex: convexity is immediate, while compactness follows from weak-* compactness of the fractional allocations and weak-* continuity of the displayed integrals.

The constant fractional allocation \(p_i(x)=\alpha_i\) has utility vector exactly \(\alpha\).

Fix \(0<\delta<1\), and maximize
\[
\sum_i u_i
\]
over
\[
\mathcal V_\delta
 =\{u\in\mathcal V:u_i\geq(1-\delta)\alpha_i\text{ for all }i\}.
\]
Let \(u^\delta\) be a maximizer. Since \(\alpha\in\mathcal V\) strictly satisfies all the constraints defining \(\mathcal V_\delta\), the finite-dimensional convex multiplier theorem gives numbers \(\lambda_i\geq0\) such that, with
\[
c_i=1+\lambda_i>0,
\]
the vector \(u^\delta\) maximizes
\[
\sum_i c_i u_i
\]
over all \(u\in\mathcal V\).

Equivalently, any fractional allocation attaining \(u^\delta\) maximizes
\[
\int_0^1\sum_i p_i(x)c_if_i(x)\,dx.
\]
Pointwise,
\[
\sum_i p_i(x)c_if_i(x)\leq \max_i c_if_i(x).
\]
Consequently, a maximizing allocation assigns almost every \(x\) to an index attaining
\[
\max_i c_if_i(x).
\]

Under the two-crossing hypothesis, pairwise ties occur at only finitely many points. Hence the maximizing allocation is, up to null sets, the pure allocation
\[
x\longmapsto \operatorname*{arg\,max}_i c_if_i(x).
\]
It satisfies
\[
\mu_i(A_i^\delta)\geq(1-\delta)\alpha_i.
\]

## 2.2. Counting the runs of an upper envelope

Let
\[
s_1s_2\cdots s_m
\]
be the reduced sequence of agents occurring from left to right in the upper envelope of the functions \(c_if_i\); adjacent terms are distinct.

This sequence contains no alternating subsequence
\[
i,j,i,j.
\]
Indeed, if there were points \(x_1<x_2<x_3<x_4\) in runs labeled \(i,j,i,j\), respectively, then the continuous function
\[
h(x)=c_if_i(x)-c_jf_j(x)
\]
would have signs
\[
+,-,+,-.
\]
It would therefore have at least three distinct zeros, contradicting the hypothesis.

The following elementary Davenport–Schinzel bound applies.

### Lemma 2.2

A sequence over \(n\) symbols, with no equal adjacent terms and no subsequence \(i,j,i,j\) for \(i\neq j\), has length at most \(2n-1\).

### Proof

Choose the first symbol \(a\), and write the sequence as
\[
aW_1aW_2\cdots aW_{k-1}aW_k.
\]
No other symbol can occur in two distinct nonempty \(W_r\)'s, since that would create \(a,b,a,b\). Applying induction inside the nonempty \(W_r\)'s gives
\[
\sum_r |W_r|\leq 2(n-1)-t,
\]
where \(t\) is the number of nonempty \(W_r\)'s. Since \(t\geq k-1\),
\[
k+\sum_r|W_r|\leq k+2(n-1)-(k-1)=2n-1.
\]
\(\square\)

Thus \(A^\delta\) has at most \(2n-1\) runs and hence at most \(2n-2\) cuts.

Finally, let \(\delta\downarrow0\). There are only finitely many label words of length at most \(2n-1\). Passing to a subsequence, fix the word and let all cutpoints converge. Continuity of the measures on intervals gives a limiting allocation with
\[
\mu_i(A_i)\geq\alpha_i
\]
and still at most \(2n-2\) cuts. This proves Theorem 2.1.

## Remark 2.3: A parameterized version

More generally, if every equation \(f_i=qf_j\) has at most \(s\) solutions, the same argument bounds the number of runs by the maximum length of a sequence on \(n\) symbols with no alternating subsequence of length \(s+2\).

In particular, if every likelihood ratio crosses each level at most once, every agent occurs in at most one run, and \(n-1\) cuts suffice.

# 3. Sharpness within the two-crossing class

The lower bound can be realized with analytic, strictly positive densities satisfying the hypothesis of Theorem 2.1.

Fix \(n\geq2\). Let agent \(1\) have Lebesgue measure:
\[
f_1(x)=1.
\]
For agents \(i=2,\ldots,n\), choose distinct points
\[
x_i=\frac{i-1}{n}.
\]
Choose pairwise disjoint small intervals
\[
J_i=(x_i-\eta,x_i+\eta)
\]
so that every component of
\[
[0,1]\setminus\bigcup_{i=2}^nJ_i
\]
lying before, between, or after the \(J_i\)'s has length at least \(d>0\).

Choose
\[
0<\varepsilon<\frac d{n-1},
\qquad
\alpha_i=\varepsilon\quad(i\geq2),
\qquad
\alpha_1=1-(n-1)\varepsilon.
\]
For \(i\geq2\), let \(\mu_i\) have the normalized truncated Gaussian density
\[
f_i(x)=Z_i^{-1}
 \exp\left(-\frac{(x-x_i)^2}{2\sigma^2}\right)
\]
on \([0,1]\). Taking \(\sigma\) sufficiently small ensures
\[
\mu_i([0,1]\setminus J_i)<\varepsilon.
\]

Consider any fair finite-cut allocation \(A_1,\ldots,A_n\).

Since \(\mu_1\) is Lebesgue measure,
\[
\lvert [0,1]\setminus A_1\rvert
 \leq (n-1)\varepsilon<d.
\]
Hence every separator interval before, between, and after the \(J_i\)'s contains a point allocated to agent \(1\).

On the other hand,
\[
\mu_i(A_i)\geq\varepsilon
  >\mu_i([0,1]\setminus J_i),
\]
so \(A_i\cap J_i\) has positive \(\mu_i\)-measure. Thus the left-to-right allocation word contains, as a subsequence,
\[
1,2,1,3,1,\ldots,1,n,1.
\]
This has \(2n-1\) terms, so at least \(2n-2\) cuts are necessary.

It remains to check the two-crossing property. For two Gaussian agents with common variance, the logarithm of \(f_i/f_j\) is affine in \(x\), so each level is crossed at most once. For a Gaussian agent and the uniform agent, the logarithm of the ratio is quadratic, so each level is crossed at most twice.

Therefore:

## Corollary 3.1

Among instances satisfying the hypotheses of Theorem 2.1, the worst-case number of cuts is exactly
\[
2n-2.
\]

# 4. An aggregation result for repeated valuation types

There is another special case that follows from the established \(3r-4\) theorem.

## Proposition 4.1

Suppose the \(n\) agents use only \(r\) distinct valuation measures. Then
\[
\text{cuts}\leq f(r)+n-r.
\]

### Proof

Group agents with the same measure. If group \(t\) has common measure \(\nu_t\), let
\[
\beta_t=\sum_{i\in G_t}\alpha_i.
\]
First divide the cake among the \(r\) representative valuation types, with type \(t\) receiving a set \(P_t\) satisfying
\[
\nu_t(P_t)\geq\beta_t.
\]
This costs at most \(f(r)\) cuts.

Now subdivide \(P_t\) among its \(|G_t|\) agents. Traverse the components of \(P_t\) in their natural order and place cumulative \(\nu_t\)-measure thresholds at
\[
\alpha_{i_1},\quad
\alpha_{i_1}+\alpha_{i_2},\quad\ldots.
\]
There are at most \(|G_t|-1\) new cutpoints. The final agent receives any excess \(\nu_t\)-value. Summing over groups gives
\[
\sum_t(|G_t|-1)=n-r
\]
additional cuts. \(\square\)

Using the supplied upper bound \(f(r)\leq3r-4\), for \(r\geq2\) this gives
\[
\text{cuts}\leq n+2r-4.
\]
Consequently, the conjectured \(2n-2\) bound holds whenever
\[
r\leq\frac{n+2}{2}.
\]
For \(r=2\), the stronger bound \(n\) follows from \(f(2)=2\).

# 5. A useful but unresolved induction criterion

Viewing \([0,1]\) as a circle, suppose there are an agent \(j\) and a circular arc \(I\) such that
\[
\mu_j(I)=\alpha_j
\]
and
\[
\sum_{i\neq j}
 \frac{\alpha_i}{1-\mu_i(I)}
 \leq1.
\tag{5.1}
\]
Then agent \(j\) can receive \(I\). On the complementary arc, normalize the remaining measures. Their normalized demands are
\[
\beta_i=\frac{\alpha_i}{1-\mu_i(I)},
\]
whose sum is at most one by (5.1). They can be enlarged to demands summing to one, and induction on \(n-1\) would then add at most \(2n-4\) cuts. The two endpoints of \(I\) give a total of at most \(2n-2\).

For \(n=2\), such an arc always exists. Indeed, for any two nonatomic probability measures \(\mu,\nu\) on a circle and \(t\in(0,1)\), there is an arc \(I\) with
\[
\mu(I)=\nu(I)=t.
\]
For a measure with strictly increasing cumulative coordinate, slide a \(\mu\)-mass-\(t\) arc around the circle. Every point lies in such a random arc with probability \(t\), so the average \(\nu\)-mass of the arc is \(t\); continuity gives equality somewhere. General nonatomic measures follow by adding a vanishing positive Lebesgue component and taking a limit.

For \(n\geq3\), I cannot prove that an arc satisfying (5.1) exists. The obvious averaging argument has the wrong convexity:
if \(I\) is a random \(\mu_j\)-mass-\(\alpha_j\) arc, then heuristically
\[
\mathbb E\,\mu_i(I)=\alpha_j,
\]
but Jensen gives
\[
\mathbb E\left[
 \sum_{i\neq j}
 \frac{\alpha_i}{1-\mu_i(I)}
\right]\geq1,
\]
not the required upper bound. Thus this induction is only a sufficient criterion, not a resolution.

# 6. Exact finite search for step-function instances

For computational counterexample searches, the continuum can be reduced exactly to linear programming.

Suppose all densities are rational step functions on a common partition into \(M\) elementary intervals, and fix a cut budget \(K\).

For each:

1. label word \((\ell_0,\ldots,\ell_K)\in[n]^{K+1}\), and
2. nondecreasing list of elementary cells containing the cutpoints,

introduce cut variables
\[
0\leq x_1\leq\cdots\leq x_K\leq1.
\]
Once the containing cells are fixed, every utility
\[
\mu_i(A_i)
\]
is an affine function of the \(x_j\), because the densities are constant on each elementary cell. Fairness is therefore an ordinary rational linear feasibility problem.

At most
\[
n^{K+1}\binom{M+K-1}{K}
\]
linear programs need to be checked. Degenerate cutpoints include allocations using fewer than \(K\) cuts.

Thus, for fixed \(n\), feasibility with \(K=2n-2\) is decidable in polynomial time in \(M\), with a large constant depending on \(n\).

This discrete search is complete in the following sense: if a nonatomic instance is a counterexample for fixed \(n,K\), then a rational step-density counterexample also exists. Indeed, the space of \(K\)-cut allocations is a finite union of compact cutpoint simplices. Hence
\[
\Phi(\mu,\alpha)
 =\max_{\text{\(K\)-cut allocations}}
   \min_i\bigl(\mu_i(A_i)-\alpha_i\bigr)
\]
is attained. A counterexample has \(\Phi<0\), giving a strict margin. Continuous distribution functions can be approximated uniformly by rational step-density distribution functions, and the value of a union of at most \(K+1\) intervals changes uniformly by at most a constant times the CDF error. Hence the strict failure persists under a sufficiently close rational step approximation.

I did not execute an exhaustive search, so no computational evidence is claimed here.

# 7. Remaining gap

The proof of Theorem 2.1 selects a Pareto-supported allocation: points are assigned according to the upper envelope of weighted densities \(c_if_i\). Under the two-crossing condition, the resulting label word is a length-\((2n-1)\) Davenport–Schinzel sequence.

For arbitrary valuations, a likelihood ratio \(f_i/f_j\) can cross a level arbitrarily many times. A weighted upper envelope can consequently have arbitrarily many runs. I do not have an uncrossing argument that compresses such an allocation to \(2n-1\) runs while preserving all \(n\) utility inequalities. Nor do I have an explicit instance requiring more than \(2n-2\) cuts.

Thus the general gap
\[
2n-2\leq f(n)\leq3n-4
\]
remains open.