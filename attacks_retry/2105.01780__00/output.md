```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The LP-core reduction yields a PTAS under effective fractional treewidth fragility, and a fully explicit PTAS also follows for bounded-degree hereditary classes with strongly sublinear separators.",
  "would_publish": false,
  "caveats": "Unrestricted separator classes and general distance-1 minimization remain unresolved; no claim of literature novelty."
}
```

# Partial resolution

The half-integral-core argument in the supplied attempt is correct. I reprove it below and make two additions:

1. The reduction from weighted Vertex Cover to weighted Independent Set can use **the original graph**, so it requires no hereditary assumption.
2. For bounded-degree hereditary classes with a separator bound \(cn^{1-\gamma}\), I give a PTAS that needs **neither a separator oracle nor a fractional-fragility oracle**.

I also give an explicit example showing that LP preprocessing does not, by itself, repair cardinality-bounded local search.

Throughout, graphs are finite and simple, and weights are nonnegative rationals encoded in binary. Approximation parameters satisfy \(0<\varepsilon<1\).

## 1. The weighted LP core

Write
\[
\tau_w(G)=\min\{w(C):C\text{ is a vertex cover of }G\},
\]
and
\[
\alpha_w(G)=\max\{w(I):I\text{ is an independent set of }G\}.
\]
Complementation gives
\[
\tau_w(G)+\alpha_w(G)=w(V(G)).
\tag{1}
\]

Consider the vertex-cover LP
\[
\min \sum_{v\in V(G)}w(v)x_v
\quad\text{subject to}\quad
x_u+x_v\ge1\ (uv\in E(G)),\qquad 0\le x_v\le1.
\tag{2}
\]

### Lemma 1 — Weighted persistency and the balanced core

An optimal half-integral solution of (2) can be computed in polynomial time. For such a solution, put
\[
P=\{v:x_v=1\},\qquad
R=\{v:x_v=\tfrac12\},\qquad
Z=\{v:x_v=0\},\qquad H=G[R].
\]
Then
\[
\tau_w(G)=w(P)+\tau_w(H),
\tag{3}
\]
and
\[
w(R)\le 2\tau_w(H),\qquad
\alpha_w(H)\le\tau_w(H).
\tag{4}
\]

#### Proof

Take an optimal extreme point of (2). On its strictly fractional coordinates, consider the graph formed by tight edge constraints. A bipartite component of this graph would permit a sufficiently small two-sided alternating perturbation, contradicting extremality. Tight edges cannot join a strictly fractional coordinate to an integral one. Thus every component of the tight-edge graph contains an odd cycle, and its tight equations force every coordinate in that component to be \(1/2\). This proves half-integrality. An optimal extreme point is obtainable by polynomial-time rational linear programming.

Feasibility implies
\[
N_G(Z)\subseteq P.
\tag{5}
\]

Let \(C\) be any vertex cover. Starting from \(x\), decrease the coordinates of \(P\setminus C\) from \(1\) to \(1/2\), and increase those of \(Z\cap C\) from \(0\) to \(1/2\). Call the resulting vector \(y\).

This vector is feasible: every neighbor of a vertex in \(P\setminus C\) belongs to \(C\), and after the changes its coordinate is at least \(1/2\). Optimality of \(x\) therefore gives
\[
0\le \sum_v w(v)(y_v-x_v)
 =\frac12\bigl(w(Z\cap C)-w(P\setminus C)\bigr).
\]
Consequently,
\[
w(P\setminus C)\le w(Z\cap C).
\tag{6}
\]

The set
\[
C'=P\cup(C\cap R)
\]
is a vertex cover by (5), and (6) implies \(w(C')\le w(C)\). Hence some optimum contains \(P\), avoids \(Z\), and restricts to a cover of \(H\). Conversely, \(P\) together with any cover of \(H\) covers \(G\). This proves (3).

Finally, the all-\(1/2\) vector is LP-optimal on \(H\): a cheaper solution on \(H\), extended by \(1\) on \(P\) and \(0\) on \(Z\), would improve \(x\). Thus
\[
\tau_w(H)\ge \operatorname{LP}_w(H)=\frac{w(R)}2.
\]
Equation (1) now yields
\[
\alpha_w(H)=w(R)-\tau_w(H)\le\tau_w(H).
\]
\(\square\)

## 2. A same-graph approximation transfer

### Theorem 2

On any graph class \(\mathcal C\), an algorithm returning a \((1-\delta)\)-approximation for maximum-weight Independent Set gives an algorithm returning a \((1+\delta)\)-approximation for weighted Vertex Cover.

The reduction uses one LP computation and one Independent Set call on the **same input graph**. The class need not be hereditary.

#### Proof

Compute the partition \(P,R,Z\) from Lemma 1. On the original graph \(G\), define new weights
\[
w'(v)=
\begin{cases}
w(v),&v\in R,\\
0,&v\notin R.
\end{cases}
\]
Then
\[
\alpha_{w'}(G)=\alpha_w(H).
\tag{7}
\]
Indeed, every independent set of \(H\) is an independent set of \(G\), and intersecting any independent set of \(G\) with \(R\) preserves its \(w'\)-weight.

Let \(J\) be the approximate independent set returned on \((G,w')\), and put \(I=J\cap R\). Thus
\[
w(I)\ge(1-\delta)\alpha_w(H).
\]
Return
\[
C=P\cup(R\setminus I).
\]
This is a vertex cover, and
\[
\begin{aligned}
w(C)
&\le w(P)+w(R)-(1-\delta)\alpha_w(H)\\
&=w(P)+\tau_w(H)+\delta\alpha_w(H)\\
&\le w(P)+(1+\delta)\tau_w(H)\\
&\le(1+\delta)\tau_w(G).
\end{aligned}
\]
The last two inequalities use Lemma 1 and nonnegativity of \(w(P)\). \(\square\)

In particular, this reduction preserves both PTAS and QPTAS running-time guarantees. It does not turn a QPTAS into a PTAS.

## 3. Application to effective fractional treewidth fragility

For precision, suppose that for each fixed integer \(a\), a polynomial-time algorithm supplies sets \(X_1,\ldots,X_m\), probabilities \(p_1,\ldots,p_m\), and tree decompositions such that
\[
\sum_i p_i=1,\qquad
\sum_{i:v\in X_i}p_i\le\frac1a
\quad(v\in V(G)),
\tag{8}
\]
and
\[
\operatorname{tw}(G-X_i)\le t(a),
\tag{9}
\]
where \(t(a)\) is independent of \(|V(G)|\). The output, including the support of the distribution, has polynomial size for fixed \(a\).

### Corollary 3

Weighted Vertex Cover has a PTAS under this effective fractional-fragility hypothesis.

#### Proof

Compute the LP core \(H=G[R]\), and take
\[
a=\left\lceil\frac1\varepsilon\right\rceil.
\]
For each \(i\), compute an exact maximum-weight independent set \(I_i\) in
\[
H-(X_i\cap R).
\]
The supplied decomposition of \(G-X_i\) restricts to a width-\(t(a)\) decomposition of this graph.

Let \(I^\star\) be an optimum independent set of \(H\). Thinness gives
\[
\begin{aligned}
\sum_i p_i\,w(I^\star\cap X_i)
&=\sum_{v\in I^\star}w(v)\sum_{i:v\in X_i}p_i\\
&\le \frac1a\alpha_w(H).
\end{aligned}
\]
For some \(i\),
\[
w(I_i)\ge w(I^\star\setminus X_i)
\ge\left(1-\frac1a\right)\alpha_w(H).
\]
Choose the heaviest \(I_i\) and apply Theorem 2’s reconstruction. Its cover has weight at most
\[
\left(1+\frac1a\right)\tau_w(G)
\le(1+\varepsilon)\tau_w(G).
\]

For fixed \(\varepsilon\), the number of instances and their treewidth are polynomially bounded and constant, respectively. Bounded-treewidth dynamic programming handles binary-encoded rational weights in polynomial time. \(\square\)

No hereditary assumption is needed here: the fragility witnesses are obtained for \(G\), and their decompositions are restricted to the core.

This proves the Vertex Cover assertion whenever effective witnesses are available—or whenever a weighted Independent Set PTAS is otherwise available. I do not silently identify existential fractional fragility with efficient access to its witnesses.

## 4. A witness-free PTAS for bounded-degree separator classes

Here is an additional constructive special case.

### Theorem 4

Fix constants \(\Delta,c>0\) and \(0<\gamma\le1\). Let \(\mathcal C\) be hereditary, with maximum degree at most \(\Delta\), such that every \(m\)-vertex graph in \(\mathcal C\) has a separator of size at most
\[
c m^{1-\gamma}
\]
whose removal leaves components of order at most \(2m/3\).

Then weighted Vertex Cover has a PTAS on \(\mathcal C\). Neither separators nor fractional-fragility witnesses need be supplied or computed by an oracle.

The polynomial exponent depends on \(\varepsilon,\Delta,c,\gamma\), but not on the magnitudes of the weights.

The proof has three steps.

### 4.1. Small unweighted deletions exist

Set
\[
A=\frac{c}{1-(2/3)^\gamma}.
\]
For every integer \(b\ge1\), every \(n\)-vertex \(F\in\mathcal C\) has a set \(X\) satisfying
\[
|X|\le A b^{-\gamma}n
\tag{10}
\]
such that all components of \(F-X\) have at most \(b\) vertices.

To see this, recursively remove balanced separators until every remaining piece has at most \(b\) vertices. At a recursive piece of order \(m>b\), charge \(c m^{-\gamma}\) to each vertex of the piece. This pays for its separator.

Along the pieces containing any particular vertex, sizes decrease by a factor at most \(2/3\). Reading the sequence backwards, that vertex receives total charge at most
\[
c b^{-\gamma}\sum_{j\ge0}(2/3)^{j\gamma}
=A b^{-\gamma}.
\]
Summing over all vertices proves (10).

This step is existential; the next step makes the decomposition algorithmic.

### 4.2. Small unweighted deletions can be found by enumeration

The case \(\Delta=0\) is trivial, so assume \(\Delta\ge1\).

Fix \(0<\rho<1\), put
\[
\eta=\frac{\rho}{\Delta+\rho},
\]
and choose a constant \(b\) with
\[
A b^{-\gamma}\le\eta.
\]

I claim that every nonempty induced subgraph \(F\) contains a set \(S\) such that
\[
1\le |S|\le b,\qquad |N_F(S)|\le\rho|S|,
\tag{11}
\]
where \(N_F(S)\) is the external neighborhood.

Take a set \(X\) from (10), and let \(S_1,\ldots,S_j\) be the components of \(F-X\). Since the maximum degree is at most \(\Delta\),
\[
\sum_{\ell=1}^j |N_F(S_\ell)|
\le \Delta |X|.
\]
Also,
\[
\sum_{\ell=1}^j |S_\ell|=|V(F)|-|X|.
\]
Therefore some component satisfies
\[
\frac{|N_F(S_\ell)|}{|S_\ell|}
\le\frac{\Delta\eta}{1-\eta}=\rho,
\]
proving (11).

One can find such an \(S\) simply by enumerating all subsets of size at most \(b\). Repeatedly:

* retain \(S\) as a piece;
* put \(N_F(S)\) into a deletion set \(D_0\);
* continue on \(F-(S\cup N_F(S))\).

There are no edges between different retained pieces. Moreover,
\[
|D_0|
\le \rho\sum_{\text{retained }S}|S|
\le \rho |V(F)|.
\tag{12}
\]
Thus, in time \(n^{b+O(1)}\), the algorithm finds a deletion set of size at most \(\rho n\) leaving components of order at most \(b\).

Heredity ensures that (11) remains valid at every iteration.

### 4.3. Arbitrary weights can be handled by separating weight scales

I next prove the following stronger intermediate statement:

> For every fixed \(0<\lambda<1\), one can find, in polynomial time, a set \(D\) with
> \[
> w(D)\le\lambda w(V(F))
> \tag{13}
> \]
> such that every component of \(F-D\) has bounded order, with the bound depending only on \(\lambda,\Delta,c,\gamma\).

Zero-weight vertices may be put into \(D\) for free, so assume all remaining weights are positive. Write \(W=w(V(F))\), and choose
\[
k=\left\lceil\frac3\lambda\right\rceil,\qquad
B=\max\left\{2,\left\lceil\frac{3\Delta}{\lambda}\right\rceil\right\}.
\]
Assign each vertex its integer weight level
\[
\ell(v)=\lfloor\log_B w(v)\rfloor.
\]
These levels can be computed by exact comparisons with integer powers of \(B\), including for weights below \(1\).

Among the \(k\) residue classes of levels modulo \(k\), delete one of minimum total weight. Its weight is at most
\[
W/k\le\lambda W/3.
\tag{14}
\]
The remaining levels split into blocks of \(k-1\) consecutive levels.

Consider an edge joining different blocks. Its endpoints’ levels differ by at least two. If \(u\) is its lighter endpoint and \(v\) its heavier endpoint, then
\[
w(u)\le \frac{w(v)}B.
\]
Delete the lighter endpoint of every such edge. The total weight deleted in this step is at most
\[
\sum_{\text{cross-block }uv}w(\text{lighter endpoint})
\le\frac{\Delta}{B}W
\le\lambda W/3.
\tag{15}
\]
The degree bound is used to charge each heavier endpoint at most \(\Delta\) times.

There are now no edges between different blocks. Within any one block, the ratio of the largest to the smallest weight is at most
\[
Q=B^{k-1}.
\]
Apply the algorithm of Section 4.2 to each block, using
\[
\rho=\frac{\lambda}{3Q}.
\]
If a block has \(m\) vertices and minimum weight \(w_{\min}\), its additional deletion has weight at most
\[
Qw_{\min}\rho m
\le Q\rho\,w(\text{block})
=\frac{\lambda}{3}w(\text{block}).
\tag{16}
\]
Summing (14)–(16) proves (13). The retained components have order at most the constant \(b\) associated with this \(\rho\).

All constants are independent of the numerical weight range. There are at most \(n\) occupied blocks, and the algorithm is polynomial in the binary input length for fixed parameters.

### 4.4. Completing the Vertex Cover PTAS

Apply Lemma 1 and work on the core \(H\). Use Section 4.3 with
\[
\lambda=\varepsilon/2
\]
to obtain \(D\subseteq V(H)\). Compute an exact minimum-weight cover of each bounded-order component of \(H-D\), and add all of \(D\).

The resulting cover \(C_H\) satisfies
\[
\begin{aligned}
w(C_H)
&=w(D)+\tau_w(H-D)\\
&\le\lambda w(V(H))+\tau_w(H)\\
&\le(1+2\lambda)\tau_w(H)\\
&=(1+\varepsilon)\tau_w(H).
\end{aligned}
\]
Adding \(P\) gives, by (3),
\[
w(P\cup C_H)\le(1+\varepsilon)\tau_w(G).
\]
This proves Theorem 4. \(\square\)

The theorem explicitly assumes a power-law separator bound. I have not inferred that bound from an arbitrary \(o(n)\) separator hypothesis.

## 5. Why LP preprocessing does not automatically fix local search

The following example rules out a tempting shortcut.

Fix a local-search removal budget \(r\ge1\). Let \(a=r+1\), and choose \(q>a\). Form \(q\) triangles sharing one vertex \(h\):
\[
\{h,u_i,v_i\},\qquad i=1,\ldots,q.
\]
Give \(h\) weight \(a\) and every other vertex weight \(1\).

Let
\[
C_0=\{u_i,v_i:1\le i\le q\}.
\]
This is a cover of weight \(2q\). Any different cover removing at least one vertex from \(C_0\) must add \(h\). Consequently, no move removing at most \(r\) vertices from \(C_0\) can improve its weight, even if additions are unrestricted: it saves at most \(r\) and costs \(a=r+1\).

On the other hand,
\[
\tau_w(G)=q+a,
\]
obtained by selecting \(h\) and one vertex from each pair \(\{u_i,v_i\}\). Thus
\[
\frac{w(C_0)}{\tau_w(G)}
=\frac{2q}{q+r+1}\longrightarrow 2.
\tag{17}
\]

Crucially, LP preprocessing does nothing here. Assign positive edge prices
\[
y_{hu_i}=y_{hv_i}=\frac{a}{2q},
\qquad
y_{u_iv_i}=1-\frac{a}{2q}.
\]
They satisfy
\[
w(v)=\sum_{e\ni v}y_e.
\]
For every feasible LP vector \(x\),
\[
\sum_v w(v)x_v
=\sum_{uv\in E(G)}y_{uv}(x_u+x_v)
\ge\sum_e y_e.
\]
The all-half vector attains equality. Because every edge price is positive, equality forces all triangle edge constraints to be tight, which forces every coordinate to equal \(1/2\). The LP optimum is therefore uniquely all-half.

These graphs have treewidth \(2\), so this is **not** a counterexample to a PTAS. It shows specifically that “apply the LP core, then use fixed-cardinality local search” is insufficient: even on the core, such local optima can approach approximation ratio \(2\).

## 6. Remaining gaps

The arguments above do **not** establish a PTAS in the following settings:

* arbitrary hereditary separator classes of unbounded degree;
* a purely existential fractional-fragility formulation without either efficiently obtainable witnesses or another weighted Independent Set PTAS;
* general distance-\(1\) minimization problems.

The bounded-degree proof uses its degree bound twice: to find small sets with small external neighborhoods, and to charge cross-scale edges. Neither estimate extends as written to unbounded degree.

Thus the concrete weighted Vertex Cover problem is resolved here under effective fractional fragility, with an additional witness-free bounded-degree separator result. The unrestricted separator question remains unresolved by this argument. I have not verified whether these reductions or special-case algorithms have already appeared in the literature, so I make no publication-priority claim.