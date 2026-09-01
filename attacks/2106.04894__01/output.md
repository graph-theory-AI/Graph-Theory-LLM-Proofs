```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The optimal bound holds for every segment-free o-minimal set of dimension at most one in arbitrary ambient dimension, and hence for the full conjecture when d is at most two.",
  "would_publish": false,
  "caveats": "Higher-dimensional non-semialgebraic targets with coefficient span at least three remain untreated; the reported 2025 semialgebraic resolution is not used."
}
```

# 1. Statement of the partial result

Let \(\mathcal R\) be an o-minimal expansion of the real field. For nonzero vectors
\[
a_1,\dots,a_n\in\mathbb R^d
\]
and independent uniform signs \(\xi_i\in\{-1,1\}\), write
\[
X=\sum_{i=1}^n \xi_i a_i .
\]

I prove the following.

**Theorem.** Let \(S\subseteq\mathbb R^d\) be \(\mathcal R\)-definable and contain no nondegenerate line segment.

1. If \(\dim S\leq 1\), then there is \(C_S\) such that
   \[
   \Pr(X\in S)\leq \frac{C_S}{\sqrt n}.
   \]
2. The same conclusion holds for arbitrary-dimensional \(S\) whenever
   \[
   \dim \operatorname{span}\{a_1,\dots,a_n\}\leq 2,
   \]
   with a constant uniform over the choice of that two-dimensional span.
3. Consequently, Conjecture 1.2 holds completely in ambient dimensions \(d\leq 2\).

The proof is independent of the reported 2025 semialgebraic result.

# 2. A compatible symmetric-chain decomposition

Write
\[
w_n=\binom{n}{\lfloor n/2\rfloor}.
\]

We need a slightly strengthened form of the usual symmetric-chain decomposition.

**Lemma 2.1.** Given any prescribed ordering \(1,\dots,n\) of the coordinates, the Boolean lattice \(2^{[n]}\) can be partitioned into \(w_n\) saturated symmetric chains such that, along every chain, coordinates are added in increasing order.

**Proof.** Induct on \(n\). Suppose a symmetric chain in \(2^{[n-1]}\) is
\[
A_k\subset A_{k+1}\subset\cdots\subset A_{n-1-k},
\qquad |A_j|=j,
\]
with coordinates added in increasing order. Replace its product with the new coordinate \(n\) by the two chains
\[
A_k\subset\cdots\subset A_{n-1-k}
  \subset A_{n-1-k}\cup\{n\},
\]
and, when nonempty,
\[
A_k\cup\{n\}\subset A_{k+1}\cup\{n\}
  \subset\cdots\subset A_{n-2-k}\cup\{n\}.
\]
Both chains are symmetric in \(2^{[n]}\), they partition the two copies of the old chain, and all newly added coordinates occur in increasing order. Induction gives the decomposition. Every symmetric chain contains exactly one set of cardinality \(\lfloor n/2\rfloor\), so the number of chains is \(w_n\). \(\square\)

# 3. Strictly convex planar graphs

The main combinatorial observation is the following.

**Lemma 3.1.** Let \(I\subseteq\mathbb R\) be an interval and let \(f:I\to\mathbb R\) be strictly convex or strictly concave. Put
\[
\Gamma_f=\{(x,f(x)):x\in I\}.
\]
For arbitrary nonzero \(b_1,\dots,b_n\in\mathbb R^2\),
\[
\bigl|\{\varepsilon\in\{-1,1\}^n:
          \textstyle\sum_i\varepsilon_i b_i\in\Gamma_f\}\bigr|
 \leq 2w_n,
\]
provided, after a linear change of coordinates, every \(b_i\) has nonzero first coordinate.

**Proof.** Independently change the sign of each \(b_i\), which merely relabels the random sign \(\varepsilon_i\), so that
\[
b_i=(u_i,v_i),\qquad u_i>0.
\]
For \(A\subseteq[n]\), the corresponding signed sum is
\[
z_A=-\sum_{i=1}^n b_i+2\sum_{i\in A}b_i.
\]

First suppose \(f\) is strictly convex. Relabel the coordinates so that
\[
\frac{v_1}{u_1}\geq \frac{v_2}{u_2}\geq\cdots\geq\frac{v_n}{u_n}.
\]
Use Lemma 2.1 with this ordering. Along one of its chains, join consecutive points \(z_A\) by straight segments. The first coordinates strictly increase, while the slopes of the successive segments are nonincreasing. Thus this polygonal chain is the graph of a concave piecewise-linear function \(g\).

On the common domain of \(g\) and \(f\), the function
\[
g-f
\]
is strictly concave. A strictly concave function cannot have three distinct zeros: if \(x_1<x_2<x_3\) were zeros, strict concavity applied to \(x_2\) and the outer pair would give \((g-f)(x_2)>0\). Hence at most two vertices on this chain belong to \(\Gamma_f\).

There are \(w_n\) chains, giving the claimed \(2w_n\) bound. If \(f\) is strictly concave, order the slopes increasingly; the polygonal function is then convex and \(g-f\) is strictly convex, with the same conclusion. \(\square\)

For a single point \(p\in\mathbb R^2\), the analogous bound is \(w_n\): after orienting all first coordinates positively, two subsets mapping to \(p\) cannot be comparable, and Sperner's theorem applies.

Since
\[
\frac{w_n}{2^n}\leq \frac{c_0}{\sqrt n}
\]
for an absolute constant \(c_0\), every fixed finite union of strictly convex or strictly concave graphs and points satisfies the desired estimate.

# 4. A uniform planar o-minimal theorem

Uniformity is essential because later the planar coordinates will depend on the vectors \(a_i\).

**Proposition 4.1.** Let \(Q\) be definable and let
\[
\mathcal T\subseteq Q\times\mathbb R^2
\]
be a definable family such that every fiber
\[
T_q=\{x:(q,x)\in\mathcal T\}
\]
contains no nondegenerate line segment. Then there is a constant \(C_{\mathcal T}\) such that, for every \(q\in Q\), every \(n\), and all nonzero \(b_1,\dots,b_n\in\mathbb R^2\),
\[
\Pr\left(\sum_{i=1}^n\xi_i b_i\in T_q\right)
 \leq \frac{C_{\mathcal T}}{\sqrt n}.
\]

**Proof.**

First enlarge the parameter space by \(L\in\operatorname{GL}_2(\mathbb R)\) and consider the family
\[
L(T_q).
\]
This is still a definable family of segment-free sets.

By uniform \(C^2\) cell decomposition, there is a uniform finite bound on the number of pieces needed to cover each \(L(T_q)\) by:

- singleton sets; and
- graphs \(y=f(x)\) of definable \(C^2\) functions on intervals.

There can be no two-dimensional cell, since a two-dimensional definable planar set has interior and therefore contains a segment. Likewise, a one-dimensional vertical cell would itself contain a vertical segment.

For each graph cell, consider the zero set of \(f''\). In a fixed fiber this zero set is finite: if it were infinite, o-minimality would give an interval on which \(f''=0\), making \(f\) affine there and producing a line segment in the target. By uniform finiteness in o-minimal structures, the number of these zeros is bounded uniformly in all parameters \(q,L\).

Splitting at these zeros, there is therefore an integer \(M\), depending only on the family, such that every \(L(T_q)\) is covered by at most \(M\) pieces, each of which is either:

- a point;
- the graph of a \(C^2\) function with \(f''>0\); or
- the graph of a \(C^2\) function with \(f''<0\).

Now choose \(L\) so that the first coordinate of every \(Lb_i\) is nonzero. This is possible because the first row of \(L\) need only avoid finitely many one-dimensional orthogonal subspaces. For every graph piece, Lemma 3.1 gives at most \(2w_n\) sign vectors, and for every point piece at most \(w_n\). Thus
\[
\bigl|\{\varepsilon:\textstyle\sum_i\varepsilon_i Lb_i\in L(T_q)\}\bigr|
 \leq 2M w_n.
\]
Since applying \(L\) does not change the event,
\[
\Pr\left(\sum_i\xi_i b_i\in T_q\right)
 \leq 2M\frac{w_n}{2^n}
 \leq \frac{2Mc_0}{\sqrt n}.
\]
This is uniform in \(q\). \(\square\)

In particular, this proves Conjecture 1.2 for every planar o-minimal set containing no segment.

# 5. Generic planar projections of definable curves

We next show that a one-dimensional segment-free definable set in arbitrary ambient dimension has a uniformly segment-free family of generic planar projections.

## 5.1 Persistent local affine hulls

Use cell decomposition to write the one-dimensional part of \(S\) as finitely many definable arcs
\[
\gamma:I\longrightarrow \mathbb R^d
\]
together with finitely many points.

For \(t\in I\), define \(r(t)\) to be the least dimension of an affine subspace containing \(\gamma(J)\) for some neighborhood \(J\) of \(t\). This is a definable, integer-valued function: the condition that a neighborhood lie in an affine \(k\)-plane is first-order definable using the definable Grassmannian of affine \(k\)-planes.

After deleting finitely many parameter values, \(r(t)\) is constant on each remaining interval. On such an interval, let \(A_t\) be the affine hull of a sufficiently small neighborhood of \(\gamma(t)\). The map \(t\mapsto A_t\) is locally constant. Indeed, if \(\gamma(U)\) spans \(A_t\) and \(s\) is sufficiently close to \(t\), a sufficiently small neighborhood of \(s\) lies in \(U\); its affine hull has the same dimension as \(A_t\), and hence equals \(A_t\). Thus \(A_t\) is constant on the interval; call it \(A\).

Moreover, every nonempty open subinterval of the parameter interval affinely spans \(A\).

The direction space
\[
V=A-A
\]
has dimension at least two. If it had dimension one, a small subarc would be a connected nonconstant definable subset of an affine line and would therefore contain a nondegenerate line segment, contrary to the hypothesis on \(S\).

We have consequently partitioned \(S\), apart from finitely many points, into finitely many arcs \(C_j\) with affine spaces \(A_j\) such that:

1. \(V_j=A_j-A_j\) has dimension at least two;
2. every open subarc of \(C_j\) affinely spans \(A_j\).

## 5.2 The good projections

Let \(G\) be the set of linear maps
\[
\pi:\mathbb R^d\longrightarrow\mathbb R^2
\]
such that
\[
\operatorname{rank}(\pi|_{V_j})=2
\]
for every arc \(C_j\). This is a nonempty open definable subset of the space of \(2\times d\) matrices: each rank condition is open and dense, and there are only finitely many of them.

**Claim.** For every \(\pi\in G\), the planar set \(\pi(S)\) contains no nondegenerate line segment.

Suppose first that \(\pi(C_j)\) contained a segment. Parameterize a subsegment by \(y(s)\). By definable choice there is a definable function \(\sigma(s)\) such that
\[
\pi(\gamma(\sigma(s)))=y(s).
\]
After restricting to a subinterval, o-minimal monotonicity makes \(\sigma\) continuous and strictly monotone. Its image is then an interval \(J\), and \(\pi\gamma(J)\) lies in a line.

Let \(c\in(\mathbb R^2)^*\setminus\{0\}\) be normal to that line. Then
\[
c\circ\pi\circ\gamma
\]
is constant on \(J\). Since \(\gamma(J)\) affinely spans \(A_j\), the functional \(c\circ\pi\) vanishes on \(V_j\). This contradicts
\[
\operatorname{rank}(\pi|_{V_j})=2,
\]
whose dual formulation says that \(c\circ\pi|_{V_j}=0\) implies \(c=0\).

Thus no individual \(\pi(C_j)\) contains a segment. A finite union of these images and finitely many points cannot contain a segment either: intersecting with a purported segment gives finitely many definable subsets of an interval, one of which would have to contain a subinterval. This proves the claim.

# 6. Proof for all one-dimensional targets

The family
\[
\mathcal P=\{(\pi,y):\pi\in G,\ y\in\pi(S)\}
\]
is definable, and by the preceding section every fiber \(\pi(S)\) is segment-free. Proposition 4.1 therefore supplies a constant \(C_S\), uniform over all \(\pi\in G\).

Given nonzero \(a_1,\dots,a_n\), choose \(\pi\in G\) such that
\[
\pi(a_i)\neq 0\qquad\text{for every }i.
\]
This is possible because each condition \(\pi(a_i)=0\) defines a proper linear subspace of the space of linear maps, and finitely many such subspaces cannot cover the nonempty open set \(G\).

Then
\[
\{X\in S\}\subseteq\{\pi(X)\in\pi(S)\},
\]
so Proposition 4.1 gives
\[
\Pr(X\in S)
 \leq
 \Pr\left(\sum_{i=1}^n\xi_i\pi(a_i)\in\pi(S)\right)
 \leq \frac{C_S}{\sqrt n}.
\]
This proves the theorem when \(\dim S\leq1\).

If \(d=2\), a definable set of dimension two has nonempty interior and hence contains a line segment. Thus every admissible planar \(S\) has dimension at most one, proving the full conjecture for \(d\leq2\).

# 7. Coefficients of linear rank at most two

There is a second consequence that does not restrict \(\dim S\).

Suppose
\[
W=\operatorname{span}\{a_1,\dots,a_n\}
\]
has dimension at most two. For \(d\geq2\), choose an injective linear map
\[
B:\mathbb R^2\longrightarrow\mathbb R^d
\]
whose image contains \(W\). Write \(a_i=Bb_i\), where every \(b_i\neq0\), and define
\[
T_B=\{x\in\mathbb R^2:Bx\in S\}.
\]
Because \(B\) is injective, \(T_B\) contains no line segment.

As \(B\) ranges over all full-rank \(d\times2\) matrices, the sets \(T_B\) form a definable family of segment-free planar sets. Proposition 4.1 is therefore uniform in \(B\), and
\[
\Pr\left(\sum_i\xi_i a_i\in S\right)
 =
\Pr\left(\sum_i\xi_i b_i\in T_B\right)
 \leq \frac{C_S}{\sqrt n}.
\]
For \(d=1\), an admissible definable \(S\) is finite, and the classical point version plus a union bound suffices.

# 8. A higher-dimensional class also covered

The same argument gives a limited higher-dimensional criterion. Suppose there are fixed linear maps
\[
L_1,\dots,L_m:\mathbb R^d\to\mathbb R^2
\]
such that

1. \(\bigcap_j\ker L_j=\{0\}\);
2. every \(L_j(S)\) contains no line segment.

For each \(j\), let
\[
I_j=\{i:L_j(a_i)\neq0\}.
\]
Since every \(a_i\neq0\), some \(j\) has \(|I_j|\geq n/m\). Condition on the signs outside \(I_j\). Membership in \(S\) then implies that the partial projected sum over \(I_j\) belongs to a translate of \(L_j(S)\). Translates form a uniform definable segment-free planar family, so Proposition 4.1 gives
\[
\Pr(X\in S)\leq O_{S,L_1,\dots,L_m}\left(\frac{\sqrt m}{\sqrt n}\right).
\]

For example, this covers products
\[
S=C_1\times\cdots\times C_m\subseteq(\mathbb R^2)^m
\]
where each \(C_j\) is an arbitrary segment-free o-minimal planar set, including non-semialgebraic examples.

# 9. Remaining gap

The proof does not address a general non-semialgebraic set \(S\) with
\[
\dim S\geq2
\quad\text{and}\quad
\dim\operatorname{span}\{a_i\}\geq3.
\]
A generic planar projection of such an \(S\) typically has two-dimensional image and therefore contains line segments, so the projection reduction loses the essential hypothesis.

The supplied catalog reports that Grebennikov and Kwan prove the full semialgebraic case in arXiv:2505.24699. I have not independently checked that preprint, and no part of the argument above depends on it or shows that its lattice-point method extends to arbitrary o-minimal structures.