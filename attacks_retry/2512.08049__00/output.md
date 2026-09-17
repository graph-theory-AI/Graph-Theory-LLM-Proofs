```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit eight-partite construction and a quantitative two-moment obstruction give 21274/25281 <= rho_hat <= 10/11 - 10^(-42).",
  "would_publish": false,
  "caveats": "The exact constant is not determined; the numerical upper improvement is tiny, and literature novelty has not been independently checked."
}
```

# An improved construction and an effective upper gap

Put
\[
\zeta=e^{\pi i/3}=\frac{1+i\sqrt3}{2}.
\]
For an orientation \(D\) of a finite simple graph, use the Hermitian adjacency convention
\[
H_{uv}=
\begin{cases}
\zeta,&u\to v,\\
\bar\zeta,&v\to u,\\
0,&uv\notin E(D).
\end{cases}
\]
Changing the convention conjugates the matrix and does not change its spectrum.

I establish the following bounds:
\[
\boxed{\frac{21274}{25281}\leq \widehat\rho
\leq \frac{10}{11}-10^{-42}.}
\tag{1}
\]
The new lower bound is approximately \(0.841502\).

The lower construction has full spectral symmetry, not merely vanishing third and fifth moments. The upper bound, in fact, holds for every orientation satisfying
\[
\operatorname{tr}H^3=\operatorname{tr}H^5=0.
\tag{2}
\]

I checked the previous attempt’s counting identity and its fifth-moment obstruction for regular tournaments on eleven vertices; both are valid. Below, I use a different construction and replace the compactness step with an elementary quantitative argument.

## 1. An eight-partite construction

### 1.1 Definition

Take eight independent classes
\[
A_1,A_2,A_3,\quad B_1,B_2,B_3,\quad C,D
\]
of sizes
\[
11,11,11,\quad 22,22,22,\quad 44,16,
\]
respectively. Include every edge between distinct classes.

Orient the \(A\)-classes cyclically, and do the same for the \(B\)-classes:
\[
A_1\to A_2\to A_3\to A_1,\qquad
B_1\to B_2\to B_3\to B_1.
\]
Writing \(A=A_1\cup A_2\cup A_3\) and \(B=B_1\cup B_2\cup B_3\), orient all remaining edges according to
\[
A\to B,\qquad B\to C,\qquad C\to A,
\qquad A\to D,\qquad B\to D,\qquad D\to C.
\tag{3}
\]

Thus the underlying graph is
\[
K_{11,11,11,22,22,22,44,16}.
\]

### 1.2 Spectral calculation

Vectors whose coordinate sum is zero on every one of the eight independent classes lie in \(\ker H\). The orthogonal complement of this kernel subspace is invariant, and the corresponding \(8\times8\) compression has entries
\[
\sqrt{n_i n_j}\,h_{ij}.
\]

Divide this compression by \(11\). Its class weights become
\[
1,1,1,\quad 2,2,2,\quad 4,\frac{16}{11}.
\]

The Hermitian adjacency matrix of a directed triangle has eigenvalues
\[
1,1,-2,
\]
with the constant vector having eigenvalue \(1\). Consequently, the two nonconstant modes on the three \(A\)-classes contribute
\[
1,-2,
\]
and those on the three \(B\)-classes contribute
\[
2,-4.
\]

It remains to examine the four-dimensional subspace constant on each of \(A,B,C,D\). More generally, if the last two weights are \(c,d\), its matrix is
\[
Q(c,d)=
\begin{pmatrix}
1&3\sqrt2\,\zeta&\sqrt{3c}\,\bar\zeta&\sqrt{3d}\,\zeta\\
3\sqrt2\,\bar\zeta&2&\sqrt{6c}\,\zeta&\sqrt{6d}\,\zeta\\
\sqrt{3c}\,\zeta&\sqrt{6c}\,\bar\zeta&0&\sqrt{cd}\,\bar\zeta\\
\sqrt{3d}\,\bar\zeta&\sqrt{6d}\,\bar\zeta&\sqrt{cd}\,\zeta&0
\end{pmatrix}.
\tag{4}
\]

Let \(e_j(Q)\) denote the sum of its principal \(j\times j\) minors. Direct calculation gives
\[
\begin{aligned}
e_1(Q)&=3,\\
e_2(Q)&=-16-9(c+d)-cd,\\
e_3(Q)&=-48c+6d-3cd,\\
e_4(Q)&=46cd.
\end{aligned}
\tag{5}
\]
For clarity, the four principal \(3\times3\) determinants are
\[
-48c,\qquad 6d,\qquad -7cd,\qquad 4cd.
\]
The determinant in (5) can also be checked by expanding in the two nonzero diagonal entries.

With \(c=4\) and \(d=16/11\), equations (5) yield
\[
\begin{aligned}
\det(xI-Q)
&=x^4-3x^3-\frac{780}{11}x^2
+\frac{2208}{11}x+\frac{2944}{11}\\
&=(x-4)(x+1)\left(x^2-\frac{736}{11}\right).
\end{aligned}
\tag{6}
\]

Combining (6) with the four nonconstant modes, the scaled compression has spectrum
\[
\left\{\pm1,\ \pm2,\ \pm4,\ \pm\sqrt{\frac{736}{11}}\right\}.
\]
Thus the original \(159\times159\) matrix has characteristic polynomial
\[
\boxed{
\det(xI-H)
=x^{151}(x^2-121)(x^2-484)(x^2-1936)(x^2-8096).
}
\tag{7}
\]
This proves full spectral symmetry.

### 1.3 Density

The order is \(159\), and the sum of the squared class sizes is
\[
3(11^2)+3(22^2)+44^2+16^2=4007.
\]
Therefore
\[
2|E|=159^2-4007=21274,
\]
giving
\[
\frac{2|E|}{|V|^2}=\frac{21274}{25281}.
\]
Uniform blow-ups preserve this density and spectral symmetry, so this also gives an infinite family.

---

## 2. The third-moment deficit identity

Let \(D\) have \(n\) vertices and \(m\) edges. Write
\[
d_v=d_v^++d_v^-,
\qquad b_v=d_v^+-d_v^-,
\]
and set
\[
X=\sum_vd_v^2,\qquad B=\sum_vb_v^2.
\]
Let \(t\) be the number of underlying triangles and \(c\) the number oriented cyclically.

A transitive triangle contributes \(3\) to \(\operatorname{tr}H^3\), while a cyclic triangle contributes \(-6\). Hence
\[
\operatorname{tr}H^3=3(t-3c).
\]
Under the first condition in (2), \(t=3c\).

Let \(p\) count directed paths \(x\to v\to y\) whose endpoints are nonadjacent, and define
\[
\ell=\sum_{uv\in E(D)}
\bigl(n-|N(u)\cup N(v)|\bigr).
\]
Both are nonnegative. Counting directed two-paths and triangle-edge incidences gives
\[
\frac{X-B}{4}=\frac{5t}{3}+p,
\qquad
3t=X-mn+\ell.
\]
Eliminating \(t\),
\[
20mn=11X+9B+36p+20\ell.
\tag{8}
\]

Put
\[
\rho=\frac{2m}{n^2}.
\]
Then (8) becomes
\[
\rho(10-11\rho)n^3
=
11(X-\rho^2n^3)+9B+36p+20\ell.
\tag{9}
\]
All terms on the right are nonnegative. In particular, \(\rho\leq10/11\).

We will rule out
\[
0\leq\delta:=\frac{10}{11}-\rho\leq10^{-42}.
\tag{10}
\]
Since \(\rho(10-11\rho)=11\rho\delta\leq10\delta\), equation (9) implies
\[
\frac{X}{n^3}-\rho^2\leq\delta,\qquad
\frac{B}{n^3}\leq2\delta,\qquad
\frac p{n^3}\leq\delta,\qquad
\frac\ell{n^3}\leq\delta.
\tag{11}
\]

## 3. Quantitative stability of the underlying graph

### 3.1 An elementary cluster-editing lemma

**Lemma.** If an \(n\)-vertex graph has at most \(\lambda n^3\) induced copies of \(P_3\), it can be changed into a disjoint union of cliques by at most
\[
4\lambda^{1/3}n^2
\]
edge additions and deletions.

**Proof.** The case \(\lambda=0\) is immediate: a graph with no induced \(P_3\) is a disjoint union of cliques.

Otherwise put \(\alpha=\lambda^{1/3}\). Repeatedly remove any vertex of current degree at most \(\alpha n\), deleting its incident edges and making it a singleton cluster. This costs at most \(\alpha n^2\) edits in total.

Whenever vertices remain and the minimum degree exceeds \(\alpha n\), let their number be \(r\). Some vertex \(v\) belongs to at most \(3\lambda n^3/r\) induced \(P_3\)'s. Make \(N[v]\) a clique and delete all edges from it to the remaining vertices. The number of required edits equals the number of induced \(P_3\)'s containing \(v\): missing edges within \(N(v)\) correspond to paths centred at \(v\), and edges from \(N(v)\) to the outside correspond to paths having \(v\) as an endpoint.

Here \(r>\alpha n\), so this step costs at most \(3\lambda n^2/\alpha\), and removes more than \(\alpha n\) vertices. There are at most \(1/\alpha\) such steps. The total cost is consequently at most
\[
\alpha n^2+\frac{3\lambda n^2}{\alpha^2}
=4\lambda^{1/3}n^2.
\]
The residual graph at every step is an induced subgraph of the original graph, so the original bound on induced \(P_3\)'s remains applicable. ∎

In the complement of the underlying graph of \(D\), the number of induced \(P_3\)'s is exactly \(\ell\).

### 3.2 Kernel bookkeeping

The remainder uses bounded kernels on \([0,1]^2\), only as bookkeeping for finite graphs and measurable partitions; no compactness theorem is needed.

Partition \([0,1]\) into \(n\) equal intervals and let \(P(x,y)\) be the indicator of the corresponding arc \(x\to y\). Set
\[
U=1-P-P^\top.
\]
Thus \(U\) records nonadjacency, including pairs in the same vertex interval. Write \(\|\cdot\|_1\) for the integral of the absolute value over \([0,1]^2\).

Let
\[
q=\frac1{11},\qquad \tau=\delta^{1/3}.
\]
From (11), the degree function \(d_U(x)=\int U(x,y)\,dy\) satisfies
\[
\int|d_U(x)-q|\,dx\leq\sqrt\delta+\delta\leq2\sqrt\delta.
\tag{12}
\]

Apply the cluster-editing lemma to the complement. It gives a partition with part measures \(s_i\) and a kernel \(U_0\), equal to one within its parts and zero between them, such that
\[
\|U-U_0\|_1\leq8\tau.
\tag{13}
\]
The assertion also holds when \(\delta=0\), since then \(\ell=0\).

Because the degree of \(U_0\) is \(s_i\) on its \(i\)-th part,
\[
e:=\sum_i s_i|s_i-q|
\leq8\tau+2\sqrt\delta
\leq10\tau.
\tag{14}
\]

Call a part large if \(s_i\geq1/22\). The total measure \(r_0\) of the small parts is at most \(22e\). Each large part satisfies
\[
|s_i-q|\leq22e,
\]
and there are at most \(22\) large parts. If their number is \(k\), then
\[
\left|\frac{k}{11}-1\right|
\leq 506e.
\]
Under (10), \(e\leq10^{-13}\), so this forces \(k=11\).

We can now rebalance these eleven parts to have measure exactly \(q\). Keep as much as possible of each large part and redistribute the remainder, including all the small parts. The measure of the redistributed set is at most
\[
\frac{r_0+\sum_{\text{large }i}|s_i-q|}{2}\leq132e.
\]
Let \(U_*\) be the resulting balanced eleven-part kernel. Pairs outside the redistributed set are unchanged, so
\[
\|U_0-U_*\|_1\leq264e.
\]
Consequently,
\[
\boxed{\kappa:=\|U-U_*\|_1\leq3000\tau.}
\tag{15}
\]

## 4. Quantitative stability of the orientation

For kernels \(R,V\), put
\[
F(R,V)=
\int V(x,z)R(x,y)R(y,z)\,dx\,dy\,dz.
\]
For the original orientation,
\[
F(P,U)=\frac p{n^3}\leq\delta.
\tag{16}
\]

Modify \(P\) to an orientation kernel \(Q\) whose underlying graph is exactly the balanced complete eleven-partite kernel \(1-U_*\): remove within-part edges and orient any missing cross-pairs arbitrarily. We can retain every original arc whose underlying adjacency remains unchanged. Thus
\[
\|P-Q\|_1\leq\kappa.
\tag{17}
\]
Telescoping the three factors in \(F\) gives
\[
F(Q,U_*)\leq\delta+3\kappa.
\tag{18}
\]

The next calculation rounds the orientation between each pair of parts.

### Orientation-rounding lemma

For two parts \(A_i,A_j\), each of measure \(q\), regard
\[
f=Q|_{A_i\times A_j}
\]
as a function on the product of their normalized probability spaces. Let \(\mu\) be its mean, and let \(g,h\) be its row and column means. Orthogonal decomposition on a product space gives
\[
\mathbb E g^2+\mathbb E h^2
\leq\mathbb E f^2+\mu^2
\leq\mu+\mu^2.
\]
Therefore
\[
\mu(1-\mu)
\leq \mathbb E[g(1-g)]+\mathbb E[h(1-h)].
\tag{19}
\]

Let \(E_{ij}\) count, as an integral, directed two-paths whose endpoints lie in \(A_i\) and whose middle vertex lies in \(A_j\). Then the right side of (19) is
\[
\frac{E_{ij}+E_{ji}}{q^3}.
\]
Rounding all edges between these two parts to the majority direction changes the arc kernel in \(L^1\) by
\[
2q^2\min(\mu,1-\mu)
\leq4q^2\mu(1-\mu)
\leq44(E_{ij}+E_{ji}).
\]
Summing over pairs of parts yields an eleven-vertex tournament \(T\), with balanced blow-up kernel \(P_T\), satisfying
\[
\|Q-P_T\|_1\leq44F(Q,U_*).
\tag{20}
\]

Combining (15), (17), (18), and (20),
\[
\begin{aligned}
L:=\|P-P_T\|_1
&\leq133\kappa+44\delta\\
&\leq400000\tau.
\end{aligned}
\tag{21}
\]

### The tournament is regular

Define the imbalance functions
\[
b_P(x)=\int(P(x,y)-P(y,x))\,dy
\]
and similarly \(b_T\). By (11),
\[
\int|b_P|\leq\sqrt{2\delta},
\]
while
\[
\int|b_P-b_T|\leq2L.
\]
Thus
\[
\int|b_T|
\leq2\tau+800000\tau.
\tag{22}
\]

If \(T\) were not regular, some vertex would have outdegree minus indegree of absolute value at least \(2\). On the corresponding part, \(|b_T|\geq2/11\), so
\[
\int|b_T|\geq\frac2{121}.
\]
But \(\tau\leq10^{-14}\), making (22) smaller than \(2/121\). Hence \(T\) is regular.

## 5. The fifth-moment contradiction

### 5.1 An arithmetic obstruction for regular tournaments of order eleven

Let \(S\) be the skew adjacency matrix of \(T\), and put \(R=iS\). Then
\[
H_T=\frac{J-I+\sqrt3R}{2}.
\]
Regularity gives \(R\mathbf1=0\), so \(H_T\mathbf1=5\mathbf1\), and on \(\mathbf1^\perp\),
\[
H_T=\frac{-I+\sqrt3R}{2}.
\]

The eigenvalues of \(R\) occur in opposite pairs. Also
\[
\operatorname{tr}R^2=110,\qquad
a:=\operatorname{tr}R^4=\operatorname{tr}S^4\in\mathbb Z.
\]
Expansion on the ten-dimensional space \(\mathbf1^\perp\) gives
\[
\begin{aligned}
\operatorname{tr}H_T^5
&=5^5-\frac{10+30\operatorname{tr}R^2
+45\operatorname{tr}R^4}{32}\\
&=\frac{96690-45a}{32}.
\end{aligned}
\tag{23}
\]
Since \(96690\equiv30\pmod{45}\),
\[
\boxed{|\operatorname{tr}H_T^5|\geq\frac{15}{32}.}
\tag{24}
\]

### 5.2 Transferring the obstruction back to \(D\)

Let
\[
K=\zeta P+\bar\zeta P^\top,\qquad
K_T=\zeta P_T+\bar\zeta P_T^\top.
\]
Both kernels have absolute value at most one, and
\[
\|K-K_T\|_1\leq2L.
\]
For the fifth-cycle integral
\[
t_5(K)=
\int K(x_1,x_2)K(x_2,x_3)\cdots K(x_5,x_1)
\,dx_1\cdots dx_5,
\]
telescoping the five factors gives
\[
|t_5(K)-t_5(K_T)|\leq5\|K-K_T\|_1\leq10L.
\tag{25}
\]

For the original finite orientation,
\[
t_5(K)=\frac{\operatorname{tr}H(D)^5}{n^5}=0.
\]
For the balanced blow-up of \(T\),
\[
t_5(K_T)=\frac{\operatorname{tr}H_T^5}{11^5}.
\]
Equations (21) and (25) therefore imply
\[
\frac{|\operatorname{tr}H_T^5|}{11^5}
\leq4\cdot10^6\tau
\leq4\cdot10^{-8}.
\]
This contradicts (24), because
\[
4\cdot10^{-8}
<
\frac{15}{32\cdot11^5}.
\]

Thus (10) is impossible. Every orientation satisfying (2) has density strictly below \(10/11-10^{-42}\), and taking the supremum proves the upper bound in (1).

# What remains unresolved

The construction proves the exact lower bound
\[
\widehat\rho\geq\frac{21274}{25281}
\]
with an explicitly factored characteristic polynomial. The upper argument makes the previous strict-gap strategy effective, although the resulting numerical improvement is deliberately very conservative.

There is no matching upper bound here, nor a proof that the eight-partite construction is optimal. In particular, these arguments do **not** determine the requested minimal constant.