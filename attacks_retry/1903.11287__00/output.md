```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "For the subset-incidence model in the previous attempt, I prove faithful convex unit-distance realizability of G_3 and realizability of G_4 with one core edge deleted.",
  "would_publish": false,
  "caveats": "The excerpt omits G_k's adjacency definition, so identification with that model remains conditional; the full k>=4 question is unresolved."
}
```

# 1. Scope and result

There is an important input issue: the supplied source excerpt gives the vertex and edge counts, but not the construction defining \(G_k\). Those counts do **not** uniquely determine a graph. Thus I cannot accept the previous attempt’s assertion that its adjacency rule follows uniquely from them.

I will denote its proposed graph by \(H_k\):
\[
A_k=\{a_S:S\subseteq[k]\},\qquad
B_k=\{b_T:T\subseteq[k]\},
\]
with
\[
a_Sb_T\in E(H_k)
\quad\Longleftrightarrow\quad
T=S\quad\text{or}\quad T=S\cup\{i\},\ i\notin S.
\tag{1}
\]
Equivalently, \(H_{k+1}\) consists of two copies of \(H_k\), together with the edges
\[
a_S^{(0)}b_S^{(1)}\qquad(S\subseteq[k]).
\]
It has the stated counts
\[
|V(H_k)|=2^{k+1},\qquad |E(H_k)|=(k+2)2^{k-1}.
\]

All results below are unconditional for the explicitly defined \(H_k\). Their application to the paper’s \(G_k\) requires checking \(G_k\cong H_k\) against the full source construction.

Here is the improvement over the previous attempt.

## Theorem

For the graphs defined by (1):

1. Every **2-degenerate subgraph** of \(H_k\) has a strictly convex unit-distance realization.
2. In particular, \(H_3\) has a **faithful** strictly convex unit-distance realization: two represented vertices are at distance \(1\) exactly when they are adjacent. The same follows for \(H_1,H_2\).
3. Let
   \[
   C=H_4\bigl[
   \{a_S:|S|\in\{1,2\}\}
   \cup
   \{b_T:|T|\in\{2,3\}\}
   \bigr].
   \]
   This is a connected cubic graph with \(20\) vertices and \(30\) edges. For every \(e\in E(C)\), the graph \(H_4-e\) has a strictly convex realization satisfying every required unit-distance constraint. Moreover, every nonedge of \(H_4\) is nonunit in this realization. Only the distance corresponding to \(e\) is uncontrolled.

These are exact unit-distance realizations, not approximate ones. The proof uses a nonsingular perturbation of an explicit parabolic incidence configuration.

# 2. A unit-distance perturbation lemma

The following is the main tool.

## Lemma 2.1

Let \(F=(A,B;E)\) be a bipartite 2-degenerate graph. Suppose we have real parameters
\[
(x_a,\alpha_a)\quad(a\in A),\qquad
(y_b,\beta_b)\quad(b\in B)
\]
such that:

- the \(x_a\)'s are pairwise distinct, and the \(y_b\)'s are pairwise distinct;
- the points \((x_a,\alpha_a)\), ordered by increasing \(x_a\), form a strictly convex graph: their consecutive secant slopes are strictly increasing;
- the points \((y_b,\beta_b)\), ordered by increasing \(y_b\), form a strictly concave graph;
- for every edge \(ab\),
  \[
  2(\beta_b-\alpha_a)+(y_b-x_a)^2=0.
  \tag{2}
  \]

Then \(F\) has a strictly convex unit-distance realization.

If, additionally, the expression in (2) is nonzero for every cross-part nonedge, then the realization can be chosen faithful.

### Proof

For a small positive \(\varepsilon\), seek a realization of the form
\[
p(a)=(\varepsilon^2\alpha_a,\varepsilon x_a),\qquad
p(b)=(1+\varepsilon^2\beta_b,\varepsilon y_b),
\tag{3}
\]
allowing all the parameters to vary slightly from their specified values.

The squared length of \(ab\) is
\[
\|p(b)-p(a)\|^2
=
1+\varepsilon^2
\left[
2(\beta_b-\alpha_a)+(y_b-x_a)^2
+\varepsilon^2(\beta_b-\alpha_a)^2
\right].
\]
Put \(\eta=\varepsilon^2\), and define
\[
\Phi_{ab}(z,\eta)
=
2(\beta_b-\alpha_a)+(y_b-x_a)^2
+\eta(\beta_b-\alpha_a)^2,
\tag{4}
\]
where \(z\) denotes all vertex parameters. We have
\[
\Phi(z_0,0)=0
\]
by (2).

### Full row rank

At \(\eta=0\), the block of the row \(D\Phi_{ab}\) in the coordinates \((\alpha_a,x_a)\) is
\[
(-2,\;2(x_a-y_b)).
\]
For two edges incident with \(a\), these two-component row vectors are linearly independent because their other endpoints have distinct \(y\)-coordinates.

Similarly, the block in \((\beta_b,y_b)\) is
\[
(2,\;2(y_b-x_a)),
\]
and two such rows are independent when their other endpoints have distinct \(x\)-coordinates.

Suppose a linear combination of the rows of \(D_z\Phi(z_0,0)\) is zero. Choose a vertex of degree at most \(2\). Its coordinate block forces the coefficients of all incident rows to vanish. Delete that vertex and repeat. Since \(F\) is 2-degenerate, all row coefficients vanish.

Thus
\[
\operatorname{rank}D_z\Phi(z_0,0)=|E|.
\tag{5}
\]

The implicit function theorem now gives parameters \(z(\eta)\), for all sufficiently small \(\eta\), with
\[
z(\eta)\longrightarrow z_0,\qquad
\Phi(z(\eta),\eta)=0.
\]
Substituting them into (3) makes every required edge have length exactly \(1\).

### Strict convexity

The two strict secant-slope conditions are open conditions, so they persist under the small parameter perturbation.

For an \(A\)-vertex, choose a supporting slope \(s_a\) for the lower convex chain:
\[
\alpha_{a'}-\alpha_a>s_a(x_{a'}-x_a)
\qquad(a'\ne a).
\]
Then the vector
\[
n_a=(-1,\varepsilon s_a)
\]
strictly exposes \(p(a)\) among the \(A\)-vertices. It also separates \(p(a)\) from every \(B\)-vertex for sufficiently small \(\varepsilon\), since the corresponding scalar products with differences to \(B\)-vertices equal
\[
-1+O(\varepsilon^2).
\]

Likewise, a supporting slope for the upper concave \(B\)-chain gives an exposing vector
\[
n_b=(1,-\varepsilon s_b)
\]
for each \(p(b)\). Thus every represented vertex is extreme.

Finally, same-part distances tend to zero. For a cross-part nonedge whose expression in (2) is nonzero,
\[
\|p(b)-p(a)\|^2-1
=
\varepsilon^2\bigl(\Phi_{ab}(z_0,0)+o(1)\bigr)\ne0
\]
for sufficiently small \(\varepsilon\). This proves the faithful version. \(\square\)

# 3. Explicit parabolic data for every \(H_k\)

Choose positive integers
\[
w_1=1,\qquad
w_j=4\sum_{i<j}w_i\quad(j\ge2).
\tag{6}
\]
Thus
\[
(w_1,w_2,w_3,w_4,\ldots)=(1,4,20,100,\ldots).
\]
For \(S\subseteq[k]\), put
\[
t_S=\sum_{i\in S}w_i,\qquad
q_S=\sum_{i\in S}w_i^2.
\]
Define
\[
\boxed{
x_S=t_S,\quad
\alpha_S=t_S^2+\frac{q_S}{2},\quad
y_S=-t_S,\quad
\beta_S=-t_S^2+\frac{q_S}{2}.
}
\tag{7}
\]

The subset sums \(t_S\) are distinct. Moreover,
\[
\begin{aligned}
2(\beta_T-\alpha_S)+(y_T-x_S)^2
&=q_T-q_S-(t_T-t_S)^2.
\end{aligned}
\tag{8}
\]
This vanishes whenever \(T=S\), and whenever \(T=S\cup\{i\}\). Thus every edge of \(H_k\) satisfies the limiting equation (2).

It remains to verify the two convex-chain conditions.

## Lemma 3.1

For the parameters in (7), the \(A\)-chain is strictly convex and the \(B\)-chain is strictly concave.

### Proof

Order all subset sums \(t_S\) increasingly. Regard \(q_S\) as data \(q(t_S)\). For three consecutive abscissas
\[
u<v<z,
\]
let \(r_1,r_2\) be the corresponding consecutive secant slopes of \(q\).

The increase in secant slopes of
\[
\alpha(t)=t^2+\frac{q(t)}2
\]
is
\[
z-u+\frac{r_2-r_1}{2}.
\]
The increase in secant slopes of
\[
\beta(t)=-t^2+\frac{q(t)}2
\]
is
\[
-(z-u)+\frac{r_2-r_1}{2}.
\]
Consequently, both required conclusions follow from
\[
|r_2-r_1|<2(z-u).
\tag{9}
\]
Concavity is unchanged by replacing the abscissa \(t\) by \(y=-t\).

We prove (9) inductively. It is vacuous for \(k=1\).

Suppose the previous largest subset sum and sum of squares are
\[
L=\sum_{i<k}w_i,\qquad Q=\sum_{i<k}w_i^2.
\]
The new weight is \(w=4L\). The new ordered data consist of the old block followed by its translate:
\[
(t,q)\quad\text{and}\quad(w+t,w^2+q).
\]
Within either block, (9) is unchanged.

The last secant slope of the old \(q\)-block and the first secant slope of the translated block are both \(1\), since \(w_1=1\). The bridge slope is
\[
D=\frac{w^2-Q}{w-L}.
\]
Since \(0<Q\le L^2\),
\[
5L\le D<\frac{16L}{3}.
\]
The two new triples have outer-abscissa difference
\[
w-L+1=3L+1.
\]
Hence
\[
|D-1|=D-1
<
\frac{16L}{3}-1
<
6L+2
=
2(3L+1).
\]
These are exactly the two remaining instances of (9). \(\square\)

Combining Lemmas 2.1 and 3.1 proves:

## Corollary 3.2

Every 2-degenerate subgraph of \(H_k\) has a strictly convex realization satisfying all its required unit-distance constraints.

Notice that the vertex set may be retained in full, including isolated vertices.

# 4. The \(k=3\) case is solved for this model

The graph \(H_3\) is 2-degenerate. One elimination order is:

1. delete \(b_\varnothing\) and \(a_{123}\);
2. delete \(b_1,b_2,b_3,a_{12},a_{13},a_{23}\), each of degree at most \(2\);
3. delete the now-isolated \(a_\varnothing,b_{123}\);
4. the remaining graph is the cycle
   \[
   a_1-b_{12}-a_2-b_{23}-a_3-b_{13}-a_1.
   \]

Therefore Corollary 3.2 applies.

For clarity, here are the complete limiting data. In every row, \(y_S=-x_S\).
\[
\begin{array}{c|r|r|r}
S&x_S&2\alpha_S&2\beta_S\\ \hline
\varnothing&0&0&0\\
1&1&3&-1\\
2&4&48&-16\\
12&5&67&-33\\
3&20&1200&-400\\
13&21&1283&-481\\
23&24&1568&-736\\
123&25&1667&-833
\end{array}
\tag{10}
\]
The increasing \(A\)-secant slopes are
\[
\frac32,\ \frac{15}2,\ \frac{19}2,\ 
\frac{1133}{30},\ \frac{83}2,\ \frac{95}2,\ \frac{99}2.
\]
The \(B\)-secant slopes, when viewed as a function of increasing \(t=-y\), are
\[
-\frac12,\ -\frac52,\ -\frac{17}2,\ 
-\frac{367}{30},\ -\frac{81}2,\ -\frac{85}2,\ -\frac{97}2.
\]
Thus the convexity margins are explicit and strict.

The construction is: use (10) as the initial parameter vector in (4), select any nonsingular \(20\times20\) Jacobian minor—which exists by the peeling argument—and hold the other \(12\) parameters fixed. The implicit function theorem supplies an analytic correction for sufficiently small positive \(\eta=\varepsilon^2\).

## Faithfulness

In fact, the limiting expression (8) vanishes **only** on the edges of \(H_k\), for every \(k\). Here is a verification.

Write
\[
\delta_i=\mathbf1_{i\in T}-\mathbf1_{i\in S}\in\{-1,0,1\}.
\]
Then
\[
q_T-q_S-(t_T-t_S)^2
=
\sum_i\delta_iw_i^2-\left(\sum_i\delta_iw_i\right)^2.
\tag{11}
\]

If the largest index \(m\) with \(\delta_m\ne0\) has \(\delta_m=-1\), the first sum in (11) is negative, so (11) cannot vanish.

Suppose \(\delta_m=1\). If all smaller \(\delta_i\)'s are zero, this is precisely a cover edge. Otherwise, let \(h<m\) be the largest smaller nonzero index and put
\[
a=\sum_{i<m}\delta_iw_i,\qquad
b=\sum_{i<m}\delta_iw_i^2.
\]
The growth rule gives
\[
\frac34w_h\le |a|\le\frac54w_h,
\qquad
|b|\le\frac{17}{16}w_h^2,
\qquad
w_m\ge4w_h.
\]
Therefore
\[
|b-a^2|\le\frac{21}{8}w_h^2,
\qquad
|2w_ma|\ge6w_h^2.
\]
Consequently,
\[
b-a^2-2w_ma\ne0,
\]
which is (11).

The remaining zero case is \(\delta_i=0\) for every \(i\), namely \(S=T\).

Thus Lemma 2.1 yields a faithful realization of \(H_3\). Its actual unit-distance framework has full row rank \(20\), so the resulting realizations form locally a \(9\)-dimensional family modulo Euclidean motions:
\[
2\cdot16-20-3=9.
\]

Restricting to subsets of \([2]\), or of \([1]\), gives faithful convex realizations of \(H_2,H_1\).

# 5. \(H_4\) is one edge away from the same argument

Consider \(H_4\). First delete:

- \(b_\varnothing,a_{1234}\);
- all four \(b_{\{i\}}\) and all four \(a_T\) with \(|T|=3\);
- the now-isolated \(a_\varnothing,b_{1234}\).

Every deletion has degree at most \(2\). What remains is exactly
\[
C=H_4\bigl[
\{a_S:|S|\in\{1,2\}\}
\cup
\{b_T:|T|\in\{2,3\}\}
\bigr].
\]
It has \(20\) vertices, and each has degree \(3\). It is connected: the singleton \(A\)-vertices are connected through the pair \(B\)-vertices; the remaining vertices attach through the diagonal and cover edges.

For any edge \(e\in E(C)\), the graph \(C-e\) is 2-degenerate. Indeed, if a nonempty subgraph of \(C-e\) had minimum degree \(3\), each of its vertices would have to retain all three of its neighbors in \(C\). Its vertex set would therefore be a union of connected components of \(C\), while avoiding the endpoints of \(e\). This contradicts connectedness.

Hence \(H_4-e\) is 2-degenerate, and Corollary 3.2 gives its convex unit-distance realization.

The faithfulness calculation above also shows that every nonedge of \(H_4\) stays nonunit. Thus the construction leaves exactly one possible extra unit edge: the deleted edge \(e\).

## The limiting obstruction is exactly one equation

The failure of the full-rank argument for \(H_4\) is not merely an artifact of the elimination order. At the limiting data (7), its \(48\)-row Jacobian has rank exactly \(47\).

Here is an explicit row dependence. Write \(w_i\) for the four weights. For distinct \(i,j\), let \(\ell,m\) be the complementary indices and define
\[
c_{ij}=\operatorname{sgn}(i,j,\ell,m)(w_m-w_\ell).
\]
This is independent of the order chosen for \(\ell,m\), and \(c_{ji}=-c_{ij}\). Direct expansion gives
\[
\sum_{j\ne i}c_{ij}=0,
\qquad
\sum_{j\ne i}w_jc_{ij}=0.
\tag{12}
\]

Assign coefficients to the core edges by
\[
\begin{aligned}
\lambda_{a_i b_{ij}}&=w_i c_{ij},\\
\lambda_{a_{ij}b_{ij}}&=-(w_i-w_j)c_{ij},\\
\lambda_{a_{ij}b_{ij\ell}}
&=\operatorname{sgn}(i,j,\ell,m)(w_i-w_j)w_m,
\end{aligned}
\tag{13}
\]
and assign zero to all other edges.

For the Jacobian in Lemma 2.1, a row dependence is equivalent to
\[
\sum_{e\ni a}\lambda_e=0,\qquad
\sum_{ab\in E}\lambda_{ab}y_b=0
\tag{14}
\]
at each \(A\)-vertex, and
\[
\sum_{e\ni b}\lambda_e=0,\qquad
\sum_{ab\in E}\lambda_{ab}x_a=0
\tag{15}
\]
at each \(B\)-vertex.

Equations (12) verify (14) at singleton \(A\)-vertices. At pair \(A\)-vertices and pair \(B\)-vertices, substitution into (13) gives cancellation directly. At a triple \(B\)-vertex, the two required cancellations reduce to
\[
(w_i-w_j)-(w_i-w_\ell)+(w_j-w_\ell)=0
\]
and
\[
(w_i+w_j)(w_i-w_j)
-(w_i+w_\ell)(w_i-w_\ell)
+(w_j+w_\ell)(w_j-w_\ell)=0.
\]
Thus (13) is a nonzero row dependence.

On the other hand, deleting any core-edge row leaves the full-rank system for the 2-degenerate graph \(H_4-e\). Its rank is \(47\). Therefore the full rank is exactly \(47\).

This isolates the next difficulty quite precisely: to realize all of \(H_4\), one must solve one additional nonlinear compatibility condition. The existence of this limiting dependence does **not** show that the compatibility condition is impossible.

# 6. What remains unresolved

For the explicitly defined model \(H_k\), the previous “first unresolved case is \(k=3\)” conclusion can be improved to:

\[
\boxed{\text{\(H_3\) is faithfully convexly unit-realizable; the first undecided member here is \(H_4\).}}
\]

For \(H_4\), all but one suitably chosen edge constraint can be satisfied while retaining strict convexity and excluding every nonedge of \(H_4\). I have not shown that the final distance can be made exactly \(1\), nor that it cannot.

Finally, the identification \(G_k\cong H_k\) must be verified from the source’s actual construction. The supplied counts alone do not justify it. Subject to that identification, the argument above is a genuine small-case advance on the catalog question, but not a resolution of the family.