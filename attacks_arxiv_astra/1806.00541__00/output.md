```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a clique-minor special case and a sharp rank obstruction to extending the usual unique-disjointness witness to sparse graphs of linear treewidth, but do not resolve the conjecture.",
  "would_publish": false,
  "caveats": "The positive bound is a standard special case; the obstruction is method-specific, and no novelty or literature-resolution claim is made."
}
```

# Partial result and an obstruction to the standard approach

Throughout, graphs are finite and simple, \(n\ge 1\), and logarithms are base \(2\). Write
\[
\operatorname{COR}(G)
=
\operatorname{conv}\left\{
\left((a_v)_{v\in V(G)},(a_u a_v)_{uv\in E(G)}\right):
a\in\{0,1\}^{V(G)}
\right\}.
\]
Extension complexity counts inequalities; equations are free.

I do **not** prove or disprove the proposed bound
\[
\operatorname{xc}(\operatorname{COR}(G))
\ge 2^{\Omega(\operatorname{tw}(G)+\log n)}.
\]

The rigorous outcomes below are:

1. If \(m=|E(G)|\) and \(h(G)\) is the largest order of a complete minor of \(G\), then
   \[
   \boxed{\operatorname{xc}(\operatorname{COR}(G))
   \ge \max\left\{n+m+1,\ (3/2)^{h(G)}\right\}.}
   \tag{1}
   \]
   Consequently, the conjectured bound holds on every class satisfying
   \[
   \operatorname{tw}(G)\le C\bigl(h(G)+\log n\bigr)
   \tag{2}
   \]
   for a fixed constant \(C\).

2. A normalized unique-disjointness witness with parameter \(k\), even with arbitrary nonnegative entries at intersections of size at least two, requires ambient polytope dimension at least
   \[
   \boxed{\binom{k+1}{2}.}
   \tag{3}
   \]
   This rank bound is sharp.

The second point is the main limitation uncovered by this attack. It shows that the familiar clique-style witness cannot simply be transplanted with parameter proportional to treewidth into sparse graphs of linear treewidth. I give a self-contained construction of that regime below.

## 1. Slack-matrix facts used

For a polytope \(P\), valid affine functions \(q_i\ge 0\) on \(P\), and points \(p_j\in P\), form the nonnegative matrix
\[
S_{ij}=q_i(p_j).
\]
Two facts will be used:
\[
\operatorname{rank}(S)\le \dim(P)+1,
\qquad
\operatorname{rank}_+(S)\le \operatorname{xc}(P)
\tag{4}
\]
when \(P\) is not a singleton. Here \(\operatorname{rank}_+\) denotes nonnegative rank.

The ordinary-rank inequality follows by factoring affine evaluation through augmented coordinates \((1,p_j)\).

For completeness, the extension-complexity inequality follows from linear-programming duality. Suppose
\[
Q=\{y:Ay\le b,\ Ey=f\},\qquad \pi(Q)=P,
\]
uses \(r\) inequalities, and choose a lift \(y_j\) of each \(p_j\). If \(q_i\) attains zero on \(P\), duality gives, on the affine space \(Ey=f\),
\[
q_i(\pi(y))=\lambda_i^\top(b-Ay)
\]
for some \(\lambda_i\ge 0\). Evaluating at the lifts gives a nonnegative factorization through \(r\) coordinates.

This also works for valid functions with positive minimum. Indeed, subtract their minimum, and represent the remaining nonnegative constant using
\[
1=\ell+(1-\ell),
\]
where \(\ell\) is a nonconstant affine function normalized to have minimum \(0\) and maximum \(1\) on \(P\). Both summands attain zero.

## 2. The positive partial bound

### 2.1 Dimension and the \(\log n\) term

Put \(d=n+m\). Consider the affine functions
\[
1,\qquad x_v\ (v\in V(G)),\qquad x_e\ (e\in E(G)).
\]
Evaluate them at the correlation points whose supports are respectively
\[
\varnothing,\qquad \{v\}\ (v\in V(G)),\qquad
\{u,v\}\ (uv\in E(G)).
\]
In this order, the resulting matrix has block form
\[
\begin{pmatrix}
1&\mathbf 1^\top&\mathbf 1^\top\\
0&I_n&B\\
0&0&I_m
\end{pmatrix},
\]
where \(B\) is the vertex-edge incidence matrix. It is invertible.

Thus \(\operatorname{COR}(G)\) has dimension \(n+m\). All the displayed functions are valid nonnegative slacks, so (4) also gives directly
\[
\operatorname{xc}(\operatorname{COR}(G))\ge n+m+1.
\tag{5}
\]

In particular, the \(\log n\) contribution is automatic. The difficult part is the exponential dependence on treewidth.

### 2.2 Minor monotonicity

If \(H\) is a minor of \(G\), then
\[
\operatorname{xc}(\operatorname{COR}(H))
\le \operatorname{xc}(\operatorname{COR}(G)).
\tag{6}
\]

Vertex and edge deletions correspond to coordinate projections. For contracting an edge \(uv\), use the valid inequality
\[
x_u+x_v-2x_{uv}\ge 0.
\]
At a correlation point its left-hand side equals
\[
(a_u-a_v)^2.
\]
Consequently, its zero face consists exactly of convex combinations of assignments satisfying \(a_u=a_v\).

Project this face by using \(x_u\) for the contracted vertex. For each edge incident with that vertex, choose an available corresponding edge coordinate of \(G\). The image is exactly \(\operatorname{COR}(G/uv)\): every assignment on the contracted graph lifts by setting \(a_u=a_v\). Parallel edges, if created, have identical coordinates on this face and can be discarded.

Taking a face adds only an equation to an extended formulation, and projection does not increase its number of inequalities. This proves (6).

### 2.3 A self-contained complete-graph lower bound

For \(A\subseteq[k]\), the following is valid for \(\operatorname{COR}(K_k)\):
\[
q_A(x)
=
1-\sum_{i\in A}x_i
+2\sum_{\{i,j\}\subseteq A}x_{ij}
\ge 0.
\]
At the correlation point corresponding to \(B\subseteq[k]\), its slack is
\[
M_{A,B}=(1-|A\cap B|)^2.
\tag{7}
\]

We prove
\[
\operatorname{rank}_+(M)\ge (3/2)^k.
\tag{8}
\]

#### Rectangle lemma

If \(\mathcal A,\mathcal B\subseteq 2^{[k]}\) satisfy
\[
|A\cap B|\ne 1
\qquad
(A\in\mathcal A,\ B\in\mathcal B),
\]
then \(\mathcal A\times\mathcal B\) contains at most \(2^k\) disjoint pairs.

**Proof.** Induct on \(k\), with the case \(k=0\) immediate. Split the families according to whether they contain \(k\), deleting \(k\) when present:
\[
\mathcal A_0,\mathcal A_1,\mathcal B_0,\mathcal B_1
\subseteq 2^{[k-1]}.
\]
Let \(D(\mathcal F,\mathcal H)\) count disjoint pairs, and abbreviate
\(D_{ij}=D(\mathcal A_i,\mathcal B_j)\). The desired count is
\[
D_{00}+D_{01}+D_{10}.
\]

Both rectangles
\[
(\mathcal A_0\cup\mathcal A_1)\times\mathcal B_0,
\qquad
\mathcal A_0\times(\mathcal B_0\cup\mathcal B_1)
\]
avoid intersections of size one. Their disjoint-pair counts sum to
\[
2D_{00}+D_{01}+D_{10}-a-b,
\]
where
\[
a=D(\mathcal A_0\cap\mathcal A_1,\mathcal B_0),
\qquad
b=D(\mathcal A_0,\mathcal B_0\cap\mathcal B_1).
\]
The pairs counted by \(a\) and \(b\) are disjoint subsets of those counted by \(D_{00}\). Indeed, a pair counted in both would give disjoint members of \(\mathcal A_1,\mathcal B_1\); restoring \(k\) would produce an intersection of size exactly one. Hence \(a+b\le D_{00}\).

The induction hypothesis therefore gives
\[
D_{00}+D_{01}+D_{10}
\le 2^{k-1}+2^{k-1}=2^k.
\]
\(\square\)

Every nonnegative rank-one summand of \(M\) has rectangular support avoiding intersections of size one. There are \(3^k\) disjoint pairs \((A,B)\), and each has slack \(1\). The rectangle lemma shows that one summand can cover at most \(2^k\) of them. Thus (8) follows.

Applying (4) to (7) yields
\[
\operatorname{xc}(\operatorname{COR}(K_k))\ge (3/2)^k.
\tag{9}
\]
Together with minor monotonicity and (5), this proves (1).

### 2.4 Consequence for treewidth

Let \(a=\log_2(3/2)\). From (1),
\[
\log_2\operatorname{xc}(\operatorname{COR}(G))
\ge \max\{\log n,\ a h(G)\}
\ge \frac a2\bigl(h(G)+\log n\bigr).
\]
If (2) holds, then
\[
\operatorname{tw}(G)+\log n
\le (C+1)\bigl(h(G)+\log n\bigr).
\]
Therefore
\[
\operatorname{xc}(\operatorname{COR}(G))
\ge
2^{\frac{a}{2(C+1)}(\operatorname{tw}(G)+\log n)}.
\tag{10}
\]
This covers, for example, any class with \(h(G)=\Omega(\operatorname{tw}(G))\), as well as the regime \(\operatorname{tw}(G)=O(\log n)\).

## 3. A sharp rank obstruction

The preceding proof suggests looking for the matrix (7), or a nonnegative completion of its crucial entries, in slack matrices of arbitrary high-treewidth graphs. There is a dimensional obstruction to doing this with parameter proportional to treewidth.

### Proposition

Let \(U\) be a nonnegative matrix whose rows and columns are indexed by all subsets of \([k]\), satisfying
\[
U_{A,B}=
\begin{cases}
1,&A\cap B=\varnothing,\\
0,&|A\cap B|=1,
\end{cases}
\tag{11}
\]
with arbitrary nonnegative entries when \(|A\cap B|\ge 2\). Then
\[
\operatorname{rank}(U)\ge 1+k+\binom{k}{2}.
\tag{12}
\]
Moreover, equality is attainable.

**Proof.** Restrict to rows and columns indexed by
\[
\mathcal I=\{\varnothing\}
\cup\{\{i\}:i\in[k]\}
\cup\{\{i,j\}:1\le i<j\le k\}.
\]
Apply the following invertible row transformation, expressed using the original rows:
\[
R_{\varnothing}'=R_{\varnothing},
\]
\[
R_{\{i\}}'=R_{\{i\}}-R_{\varnothing},
\]
\[
R_{\{i,j\}}'
=
R_{\{i,j\}}-R_{\{i\}}-R_{\{j\}}+R_{\varnothing}.
\]
The transformed matrix has block form
\[
\begin{pmatrix}
1&*&*\\
0&-I_k&*\\
0&0&D+I_{\binom{k}{2}}
\end{pmatrix},
\tag{13}
\]
where
\[
D_{\{i,j\},\{i,j\}}=U_{\{i,j\},\{i,j\}}.
\]

To check the bottom-right block, two distinct two-element sets intersect in zero or one element, so their transformed entry is zero by (11). The diagonal entry is
\[
U_{\{i,j\},\{i,j\}}+1.
\]
Every such entry is positive because \(U\) is nonnegative. Thus (13) is invertible, proving (12).

For sharpness, the matrix
\[
M_{A,B}=(1-|A\cap B|)^2
\]
is a permitted completion. Writing \(a_i=\mathbf 1_{i\in A}\) and \(b_i=\mathbf 1_{i\in B}\),
\[
M_{A,B}
=
1-\sum_i a_i b_i
+2\sum_{i<j}a_i a_j b_i b_j.
\]
This is a sum of \(1+k+\binom{k}{2}\) real rank-one matrices, so its ordinary rank is at most that quantity. The lower bound gives equality. \(\square\)

Thus the minimum ordinary rank among all nonnegative completions satisfying (11) is exactly
\[
1+\binom{k+1}{2}.
\tag{14}
\]

Nonnegativity is essential here: the signed completion \(1-|A\cap B|\) has rank only \(k+1\), but is negative when the intersection has size at least two.

### Consequence for correlation polytopes

Suppose a matrix satisfying (11) occurs as a submatrix of a valid-inequality slack matrix of \(\operatorname{COR}(G)\). The ordinary-rank bound in (4) and (12) imply
\[
1+\binom{k+1}{2}
\le n+m+1,
\]
hence
\[
\boxed{\binom{k+1}{2}\le n+m.}
\tag{15}
\]
The conclusion is unchanged if the witness is obtained after positive row and column scalings, since these preserve rank.

In particular, when \(m=O(n)\), necessarily \(k=O(\sqrt n)\). Replacing the square in (7) by a clever nonnegative completion cannot remove this obstruction.

### Fixed-cardinality witnesses also face a quadratic barrier

The obstruction is not merely an artifact of explicitly including empty sets and singletons.

Suppose rows and columns are all \(\ell\)-subsets of a \(t\)-element ground set, with \(2\le\ell\le t/4\), and the matrix again has entries \(1\) for disjoint pairs and \(0\) for intersections of size one. Put \(k=t-2\ell\), and partition the ground set into
\[
W,\ F_R,\ F_C
\]
of sizes \(k,\ell,\ell\).

For each \(A\subseteq W\) with \(|A|\le2\), choose the row
\[
A\cup\{\text{the first }\ell-|A|\text{ elements of }F_R\},
\]
and choose columns analogously using \(F_C\). The intersection of the selected row and column is exactly \(A\cap B\). Consequently, the invertible block used in (13) appears here too.

The rank is therefore at least
\[
1+\binom{t-2\ell+1}{2}=\Omega(t^2).
\tag{16}
\]
Thus this common fixed-cardinality variant also cannot have a linear-size parameter in a slack matrix of dimension \(O(n)\).

## 4. Why this obstructs the missing sparse regime

Here is a self-contained construction showing that bounded degree and linear treewidth coexist.

### Lemma

For every positive multiple \(n\) of \(4\), there is a simple graph \(G_n\) satisfying
\[
\Delta(G_n)\le64,
\qquad
\operatorname{tw}(G_n)\ge n/4.
\tag{17}
\]

**Proof.** Choose \(64\) independent uniformly random perfect matchings on \([n]\), and let \(G_n\) be their simple union. Its maximum degree is at most \(64\).

Fix disjoint \(A,B\subseteq[n]\), with sizes \(a,b\ge n/4\). In one random perfect matching, expose partners of unmatched vertices of \(A\). At least \(a/2\) exposures are needed to exhaust \(A\). Conditional on having exposed no \(A\)-\(B\) edge, every vertex of \(B\) remains unmatched, so at each exposure the probability of hitting \(B\) is at least \(b/(n-1)\). Hence
\[
\Pr(\text{one matching has no }A\text{-}B\text{ edge})
\le
\exp\!\left(-\frac{ab}{2(n-1)}\right).
\]
For the union of \(64\) matchings, the probability is at most
\[
\exp\!\left(-\frac{32ab}{n-1}\right)
\le e^{-2n}.
\]
There are at most \(3^n\) ordered disjoint pairs \((A,B)\). Since \(3^n e^{-2n}<1\), some union satisfies
\[
\text{every disjoint }A,B\text{ with }|A|,|B|\ge n/4
\text{ have an edge between them.}
\tag{18}
\]

It remains to verify its treewidth. A graph of treewidth \(w\) has a set \(S\) of at most \(w+1\) vertices such that every component of \(G-S\) has at most \(n/2\) vertices. This follows directly from a tree decomposition: assign each vertex to one containing bag and choose a weighted centroid bag.

If \(w\le n/4-1\), then \(|S|\le n/4\). The components of \(G-S\) can be partitioned into two unions \(A,B\), each of size at least \(n/4\): choose a component of size between \(n/4\) and \(n/2\), if one exists; otherwise accumulate components until their total first reaches \(n/4\), remaining below \(n/2\). The remaining vertices outside \(S\) have size at least \(n/4\).

There are no edges between these unions, contradicting (18). Thus \(w\ge n/4\). \(\square\)

For a completely specified, though not efficient, deterministic choice, one may take the lexicographically first \(64\)-tuple of perfect matchings whose union satisfies (18).

For these graphs,
\[
|E(G_n)|\le32n,
\qquad
\dim\operatorname{COR}(G_n)\le33n.
\]
By (15), any normalized unique-disjointness witness in their slack matrices satisfies
\[
k\le\sqrt{66n}.
\]
Since such a witness has \(2^k\) rows,
\[
\operatorname{rank}_+(U)\le2^k\le2^{\sqrt{66n}}.
\tag{19}
\]
The conjecture, by contrast, demands \(2^{\Omega(n)}\) extension complexity for this family. The fixed-cardinality witnesses covered by (16) encounter the same asymptotic limitation.

## 5. Remaining gap

The positive argument proves the conjectured form under condition (2), but it does not handle general large-treewidth graphs.

The rank obstruction is **not** an upper bound on extension complexity and provides no counterexample. A slack matrix of dimension \(O(n)\) could still have nonnegative rank \(2^{\Omega(n)}\). What is ruled out is obtaining that conclusion solely by locating one normalized unique-disjointness completion of the forms above: its parameter is necessarily only \(O(\sqrt n)\) in the sparse regime.

Thus a proof for sparse graphs of linear treewidth needs substantially more than the direct clique-style witness used here. Establishing the required exponential lower bound for that regime remains an unresolved step in this attack.