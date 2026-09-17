```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an explicit O(1/m) small-activity bound, yielding the conjecture for logarithmic-length subdivisions of arbitrary m-edge graphs.",
  "would_publish": false,
  "caveats": "The unrestricted uniform-forest conjecture remains unresolved; novelty and current literature status of the partial bound are not asserted."
}
```

# A logarithmic subdivision bound

I use the intended formulation with **distinct edges** \(e\ne f\). Forests are arbitrary acyclic edge subsets, with isolated vertices allowed. Graphs are loopless; auxiliary contractions may produce loops and parallel edges, which are treated in the usual way.

The full conjecture is not proved here. The partial result improves asymptotically on the supplied lead: the sufficient subdivision length is logarithmic in the number of original edges, rather than linear.

The forest-measure and subdivision identities used in that lead are rederived below. Its small-activity coefficient estimate is not used.

## 1. Results

For positive activities \(\mathbf x=(x_g:g\in E(G))\), let
\[
\mu_{\mathbf x}(F)=\frac{1}{Z_G(\mathbf x)}
 \prod_{g\in F}x_g,
\qquad
Z_G(\mathbf x)=\sum_{F\text{ forest}}\prod_{g\in F}x_g.
\]

All logarithms without a subscript are natural.

**Theorem 1 — small-activity negative correlation.**  
For distinct edges \(e,f\), if
\[
\sum_{g\in E(G)\setminus\{e,f\}}\frac{x_g}{1+x_g}
\le \frac{\log 2}{121},
\tag{1}
\]
then
\[
\operatorname{Cov}_{\mu_{\mathbf x}}
   \bigl(\mathbf1_{\{e\in F\}},\mathbf1_{\{f\in F\}}\bigr)\le0.
\]

In particular, for a graph with \(m\ge3\) edges, all pairs are negatively correlated whenever
\[
0<x_g\le
\frac{\log 2}{121(m-2)-\log 2}
\qquad(g\in E(G)).
\tag{2}
\]
Thus the sufficient activity scale is \(O(1/m)\), rather than exponentially small in \(m\).

**Theorem 2 — uniform forests on subdivisions.**  
Let \(G\) have \(m\ge3\) edges. Replace each edge \(g\) by a path of length \(k_g\), with distinct new internal vertices, obtaining \(H\). If
\[
k_g\ge
K_m:=
\left\lceil
\log_2\!\left(\frac{121(m-2)}{\log 2}\right)
\right\rceil
\qquad(g\in E(G)),
\tag{3}
\]
then all distinct edge indicators in the uniform forest of \(H\) are negatively correlated.

A simpler sufficient condition is
\[
k_g\ge 8+\left\lceil\log_2(m-2)\right\rceil.
\tag{4}
\]

The constants are deliberately crude. The substantive point is the logarithmic dependence.

## 2. A useful normalization

Put
\[
p_g=\frac{x_g}{1+x_g}.
\]
Define the acyclicity probability polynomial
\[
Q_G(\mathbf p)
=
\sum_{F\text{ forest}}
 \prod_{g\in F}p_g
 \prod_{g\notin F}(1-p_g).
\tag{5}
\]
Thus \(Q_G(\mathbf p)\) is the probability that independent Bernoulli edges with parameters \(\mathbf p\) form a forest, and
\[
Z_G(\mathbf x)=\prod_g(1+x_g)\,Q_G(\mathbf p).
\tag{6}
\]

For distinct \(e,f\), define
\[
\Phi_{ef}^G=Q_eQ_f-Q_GQ_{ef},
\tag{7}
\]
where derivatives are with respect to the \(p\)-variables. Because \(Q_G\) is multiaffine, writing
\[
Q_G=A+p_eB+p_fC+p_ep_fD
\]
gives
\[
\Phi_{ef}^G=BC-AD.
\tag{8}
\]
In particular, \(\Phi_{ef}^G\) is independent of \(p_e,p_f\).

Differentiating (6) gives the exact covariance identity
\[
\operatorname{Cov}_{\mu_{\mathbf x}}(X_e,X_f)
=
-\frac{p_e(1-p_e)p_f(1-p_f)}{Q_G(\mathbf p)^2}
  \Phi_{ef}^G(\mathbf p),
\tag{9}
\]
where \(X_g=\mathbf1_{\{g\in F\}}\). Consequently, it suffices to prove \(\Phi_{ef}^G\ge0\).

The advantage of \(Q_G\) over \(Z_G\) is that suppressing a degree-two path simply replaces its edge parameters by their product. No additional prefactor appears.

## 3. A coefficient-norm lemma

For a polynomial \(R=\sum_\alpha r_\alpha\mathbf p^\alpha\), write
\[
\|R\|_1=\sum_\alpha |r_\alpha|.
\]
We use the elementary inequalities
\[
\|R+S\|_1\le\|R\|_1+\|S\|_1,
\qquad
\|RS\|_1\le\|R\|_1\|S\|_1.
\]

The key bound depends on the number of edges **outside a cycle**, not on the cycle’s length.

**Lemma 3.**  
Suppose \(J\) consists of a cycle \(\gamma\) and an additional edge set \(T\), with \(|T|=k\). Then
\[
\|Q_J\|_1\le 2\cdot11^k.
\tag{10}
\]
Consequently, for any two distinct marked edges of \(J\),
\[
\|\Phi_{ef}^J\|_1\le121^k.
\tag{11}
\]

### Proof of (10)

Condition on the Bernoulli edges selected from \(T\). Only forests \(A\subseteq T\) can contribute. Contracting such a forest gives
\[
Q_J(\mathbf p)
=
\sum_{\substack{A\subseteq T\\A\text{ forest}}}
 \left(\prod_{g\in A}p_g\right)
 \left(\prod_{g\in T\setminus A}(1-p_g)\right)
 Q_{\gamma/A}(\mathbf p_\gamma).
\tag{12}
\]
Here \(\gamma/A\) means the graph of the cycle edges after contracting \(A\); isolated vertices are irrelevant. The identity follows because
\[
A\cup B\text{ is a forest}
\quad\Longleftrightarrow\quad
B\text{ is a forest after contracting }A
\]
when \(A\) is a forest.

Let \(t=|A|\). The non-isolated part of \(\gamma/A\) is connected and Eulerian: it is obtained by identifying vertices of a cycle. Its cycle rank \(\rho\) satisfies
\[
\rho\le t+1,
\tag{13}
\]
because contracting \(t\) edges can make at most \(t\) identifications among the cycle vertices.

If every vertex has degree two, this graph is a cycle, and its acyclicity polynomial has coefficient norm \(2\).

Otherwise, suppress all degree-two vertices. The resulting connected multigraph has minimum degree at least four. If it has \(v\) vertices and \(h\) edges, then
\[
h\ge2v,
\qquad
\rho=h-v+1,
\]
and therefore
\[
h\le2(\rho-1)\le2t.
\tag{14}
\]

Suppression preserves the coefficient norm of the acyclicity polynomial: each new edge variable is replaced by the product of the variables along its path, and these paths have disjoint edge sets. This substitution is injective on monomials.

For any multigraph \(L\) with \(h\) edges, (5) gives
\[
\|Q_L\|_1
\le
\sum_{F\text{ forest}}2^{h-|F|}
\le
\sum_{F\subseteq E(L)}2^{h-|F|}
=3^h.
\tag{15}
\]
This remains valid when loops are present.

Combining the cycle case with (14)–(15), we obtain the uniform bound
\[
\|Q_{\gamma/A}\|_1\le2\cdot9^t.
\tag{16}
\]
Taking norms in (12) now gives
\[
\begin{aligned}
\|Q_J\|_1
&\le
\sum_{t=0}^k
 \binom kt\,2^{k-t}\,2\cdot9^t\\
&=2(2+9)^k
=2\cdot11^k.
\end{aligned}
\]

### Proof of (11)

Write \(Q_J=A+p_eB+p_fC+p_ep_fD\). These four parts have disjoint coefficient supports, so
\[
\|Q_J\|_1=\|A\|_1+\|B\|_1+\|C\|_1+\|D\|_1.
\]
Using (8),
\[
\begin{aligned}
\|\Phi_{ef}^J\|_1
&\le \|B\|_1\|C\|_1+\|A\|_1\|D\|_1\\
&\le \frac14\|Q_J\|_1^2\\
&\le121^k.
\end{aligned}
\]
For the middle inequality, use \(bc+ad\le(a+b)(c+d)\le(a+b+c+d)^2/4\) for nonnegative \(a,b,c,d\). ∎

## 4. Proof of the small-activity theorem

We first record two support facts.

### 4.1 A nonzero coefficient requires a common cycle

Acyclicity factors over the blocks of a graph, so \(Q_G\) is the product of the corresponding block polynomials. A bridge contributes the factor \(1\).

Two distinct edges lie in a common cyclic block exactly when they lie on a common cycle. For completeness, the nontrivial direction follows by subdividing the two marked edges in a 2-connected block and applying the existence of two internally vertex-disjoint paths between the new subdivision vertices.

It follows that
\[
e,f\text{ lie on no common cycle}
\quad\Longrightarrow\quad
\Phi_{ef}^G\equiv0.
\tag{17}
\]

Setting \(p_g=0\) deletes \(g\). Hence, if \(\mathbf p^\alpha\) has a nonzero coefficient in \(\Phi_{ef}^G\), then
\[
S_\alpha:=\{e,f\}\cup\{g:\alpha_g>0\}
\tag{18}
\]
contains a cycle through \(e,f\).

### 4.2 Every common cycle supplies a positive coefficient

For a graph consisting of a cycle \(\gamma\),
\[
Q_\gamma=1-\prod_{g\in\gamma}p_g.
\]
If \(e,f\in\gamma\), direct differentiation gives
\[
\Phi_{ef}^{\gamma}
=
\prod_{g\in\gamma\setminus\{e,f\}}p_g.
\tag{19}
\]
Therefore, in the full graph, the coefficient of this monomial is exactly \(1\): delete all edges outside \(\gamma\).

Let \(\mathscr C_{ef}\) denote the set of cycles containing \(e,f\), and set
\[
L_{ef}(\mathbf p)
=
\sum_{\gamma\in\mathscr C_{ef}}
 \prod_{g\in\gamma\setminus\{e,f\}}p_g.
\tag{20}
\]
At nonnegative parameters, the positive-coefficient part of \(\Phi_{ef}^G\) is at least \(L_{ef}\).

### 4.3 Bounding all negative coefficients

Expand
\[
\Phi_{ef}^G=\sum_\alpha a_\alpha\mathbf p^\alpha.
\]
For each negative coefficient, choose one cycle
\[
\gamma_\alpha\subseteq S_\alpha
\]
through \(e,f\), and put
\[
T_\alpha=S_\alpha\setminus\gamma_\alpha.
\]
Necessarily \(T_\alpha\ne\varnothing\), by (19).

For \(0\le p_g\le1\), every edge in \(S_\alpha\setminus\{e,f\}\) occurs with positive exponent, so
\[
\mathbf p^\alpha
\le
\left(\prod_{g\in\gamma_\alpha\setminus\{e,f\}}p_g\right)
\left(\prod_{g\in T_\alpha}p_g\right).
\tag{21}
\]

Fix a cycle \(\gamma\) and a nonempty set \(T\subseteq E(G)\setminus\gamma\). The total absolute coefficient mass of negative monomials assigned to this pair \((\gamma,T)\) is at most
\[
\|\Phi_{ef}^{G[\gamma\cup T]}\|_1
\le121^{|T|},
\tag{22}
\]
by Lemma 3. The first inequality holds because deleting all other edges leaves the relevant coefficients unchanged.

Combining (20)–(22), and enlarging the sum to all possible nonempty \(T\), gives
\[
\boxed{
\Phi_{ef}^G(\mathbf p)
\ge
\sum_{\gamma\in\mathscr C_{ef}}
\left(\prod_{g\in\gamma\setminus\{e,f\}}p_g\right)
\left[
2-\prod_{g\notin\gamma}(1+121p_g)
\right].
}
\tag{23}
\]

Indeed, the sum over nonempty \(T\subseteq E(G)\setminus\gamma\) is
\[
\sum_{\varnothing\ne T\subseteq E(G)\setminus\gamma}
 121^{|T|}\prod_{g\in T}p_g
=
\prod_{g\notin\gamma}(1+121p_g)-1.
\]

Put
\[
s=\sum_{g\ne e,f}p_g.
\]
For every common cycle,
\[
\prod_{g\notin\gamma}(1+121p_g)
\le \exp(121s).
\]
Thus (23) implies the quantitative estimate
\[
\boxed{
\Phi_{ef}^G(\mathbf p)
\ge
\bigl(2-e^{121s}\bigr)L_{ef}(\mathbf p).
}
\tag{24}
\]

If \(s\le(\log2)/121\), the right-hand side is nonnegative. If there is no common cycle, (17) applies instead. These cases cover every pair, and (9) proves Theorem 1. ∎

The estimate can also be applied just within the block containing \(e,f\); factors from other blocks do not change the sign.

## 5. Proof of the subdivision theorem

Let \(P_g\) be the path replacing \(g\), of length \(k_g\). For a uniformly chosen forest of \(H\), define
\[
Y_g=\mathbf1_{\{\text{all edges of }P_g\text{ are present}\}}.
\]

A cycle in \(H\) must traverse any replacement path it enters completely. Consequently, a subset of \(E(H)\) is acyclic exactly when the set of fully present replacement paths corresponds to a forest of \(G\).

For a fixed forest \(A\subseteq E(G)\), the number of forests of \(H\) with
\[
\{g:Y_g=1\}=A
\]
is
\[
\prod_{g\notin A}(2^{k_g}-1).
\]
Hence \(Y\) has the weighted forest distribution on \(G\) with activities
\[
x_g=\frac1{2^{k_g}-1},
\qquad
\frac{x_g}{1+x_g}=2^{-k_g}.
\tag{25}
\]

Under (3), for every distinct \(g,h\),
\[
\sum_{j\notin\{g,h\}}2^{-k_j}
\le(m-2)2^{-K_m}
\le\frac{\log2}{121}.
\]
Theorem 1 therefore gives
\[
\operatorname{Cov}(Y_g,Y_h)\le0.
\tag{26}
\]

It remains to check individual edges of \(H\), including pairs on the same path.

### 5.1 Edges on different replacement paths

Conditionally on \(Y\), choices on different paths are independent. An inactive path has a uniformly chosen proper subset of its edges.

For \(a\in P_g\), put
\[
q_g=\frac{2^{k_g-1}-1}{2^{k_g}-1}.
\]
Then
\[
\mathbb E[X_a\mid Y]=q_g+(1-q_g)Y_g.
\]
Thus, for \(a\in P_g\), \(b\in P_h\), \(g\ne h\),
\[
\operatorname{Cov}(X_a,X_b)
=
(1-q_g)(1-q_h)\operatorname{Cov}(Y_g,Y_h)
\le0.
\tag{27}
\]

### 5.2 Two edges on the same replacement path

Let \(a,b\) be distinct edges of a path of length \(k\ge2\), and write
\[
\theta=\mathbb P(Y_g=1).
\]
Conditioned on \(Y_g=0\),
\[
q=\mathbb P(X_a=1\mid Y_g=0)
=\frac{2^{k-1}-1}{2^k-1},
\]
and
\[
r=\mathbb P(X_a=X_b=1\mid Y_g=0)
=\frac{2^{k-2}-1}{2^k-1}.
\]

We have
\[
\theta\le2^{-k}.
\tag{28}
\]
Indeed, write the weighted forest polynomial on \(G\) as
\[
Z_G=A+x_gB.
\]
Every forest counted by \(B\) is also counted by \(A\), with the same weight, so \(B\le A\). Therefore
\[
\theta=\frac{x_gB}{A+x_gB}
\le\frac{x_g}{1+x_g}
=2^{-k}.
\]

The total covariance formula gives
\[
\begin{aligned}
\operatorname{Cov}(X_a,X_b)
&=(1-\theta)(r-q^2)
  +\theta(1-\theta)(1-q)^2\\
&=
\frac{(1-\theta)2^{k-2}}{(2^k-1)^2}
  \bigl(2^k\theta-1\bigr)
\le0,
\end{aligned}
\tag{29}
\]
using (28).

Equations (27) and (29) cover every pair of distinct edges of \(H\), proving Theorem 2. Graphs with at most two edges are handled directly by the forest or single-cycle calculation. ∎

## 6. What remains open

The substantive gain over the supplied lead is Lemma 3: after the Bernoulli normalization, a graph consisting of a cycle plus \(k\) extra edges has controlled coefficient norm **independently of the cycle length**. This yields an \(O(1/m)\) sufficient activity scale and hence \(O(\log m)\) sufficient subdivision lengths.

For an arbitrary unsubdivided graph under the uniform forest measure,
\[
x_g=1,\qquad p_g=\frac12.
\]
The hypothesis of Theorem 1 generally fails, and the lower bound (24) generally becomes uninformative. No unrestricted sign argument for \(\Phi_{ef}^G(1/2,\ldots,1/2)\) is obtained.

Nor can the subdivision result simply be contracted back to \(G\): that requires conditioning many edges to be present, and pairwise negative correlation alone does not justify preservation under such conditioning.

Thus the original conjecture remains unresolved by this argument. The proved partial result is the explicit small-activity theorem and its logarithmic subdivision consequence.