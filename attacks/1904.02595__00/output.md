```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for all products of at most three factors, for every product having a bipartite factor, and under a general weight-gap condition, but the higher-dimensional small-gap unbalanced cases remain open.",
  "would_publish": false,
  "caveats": "The case n >= 4 with every factor at least tripartite and with small quotient-weight gap is not settled; overlap with cases already implicit in the source paper has not been checked."
}
```

# 1. Statement of the partial result

All graphs below are finite and simple, and \(IR(G)\) denotes upper irredundance.

I prove the following.

### Theorem A
Let
\[
G=\prod_{i=1}^n H_i,
\]
where every \(H_i\) is complete multipartite.

1. If \(n\le 3\), then
   \[
   IR(G)=\alpha(G),
   \]
   with no balance assumption.

2. If one factor \(H_i\) has at most two parts, then
   \[
   IR(G)=\alpha(G)
   \]
   for arbitrary \(n\).

3. More generally, let \(s_{i,a}\) be the sizes of the parts of \(H_i\), and put
   \[
   g_i=\gcd_a s_{i,a}.
   \]
   If
   \[
   \prod_{i=1}^n g_i\ge 2^n,
   \]
   then
   \[
   IR(G)=\alpha(G).
   \]

The third assertion follows from a more flexible “second-best weight gap” criterion proved below.

The unresolved case is therefore \(n\ge4\), every factor having at least three parts, and with small arithmetic/weight gap.

---

# 2. The weighted quotient

Write the parts of \(H_i\) as
\[
P_{i,1},\dots,P_{i,q_i},\qquad |P_{i,a}|=s_{i,a}.
\]
For
\[
x=(x_1,\dots,x_n)\in\Omega:=\prod_{i=1}^n [q_i],
\]
let
\[
C_x=P_{1,x_1}\times\cdots\times P_{n,x_n},
\qquad
w(x)=|C_x|=\prod_{i=1}^n s_{i,x_i}.
\]

Each \(C_x\) is an independent false-twin class. Two distinct classes \(C_x,C_y\) are completely joined precisely when
\[
x_i\ne y_i\qquad\text{for every }i.
\]

Thus the quotient graph is
\[
Q=\prod_{i=1}^n K_{q_i}.
\]
A family \(\mathcal F\subseteq\Omega\) is independent in \(Q\) exactly when every two members agree in at least one coordinate.

Any independent set in \(G\) can be completed by taking all vertices from each occupied class. Consequently,
\[
\alpha(G)
=
\alpha_w(Q)
:=
\max_{\mathcal F\text{ independent in }Q}
W(\mathcal F),
\qquad
W(\mathcal F):=\sum_{x\in\mathcal F}w(x).
\tag{2.1}
\]

---

# 3. Two general lemmas on irredundant sets

Let \(S\) be irredundant. Call \(v\in S\) **lonely** if it has no neighbor in \(S\), and **social** otherwise. Write
\[
L=\{v\in S:v\text{ is lonely}\},\qquad
R=S\setminus L,
\]
and
\[
\ell=|L|,\qquad t=|R|.
\]

Every social vertex \(v\) has an external private neighbor \(p_v\), adjacent to \(v\) and to no other member of \(S\).

Two elementary observations will be used repeatedly.

* A false-twin class contains at most one social vertex of \(S\). Indeed, a private neighbor of one such vertex would also be adjacent to the other.
* A false-twin class cannot contain both a lonely and a social vertex: any neighbor of the social vertex would also be a neighbor of the lonely one.

## Lemma 3.1: The number of social vertices is at most \(2^n\)

For every irredundant \(S\subseteq V(G)\),
\[
t\le 2^n.
\tag{3.1}
\]

### Proof

Let the part-label of the \(j\)-th social vertex be \(x^{(j)}\), and the part-label of its private neighbor be \(y^{(j)}\). Then
\[
y^{(j)}_i\ne x^{(j)}_i
\quad\text{for all }i,
\tag{3.2}
\]
while for \(k\ne j\), the private-neighbor property implies that \(y^{(j)}\) and \(x^{(k)}\) agree in at least one coordinate.

For each coordinate \(i\), choose distinct real numbers \(\lambda_{i,a}\), one for every part \(a\), and put
\[
u_{i,a}=(1,\lambda_{i,a})\in\mathbb R^2.
\]
Define the functional
\[
\phi_{i,b}(z_0,z_1)=z_1-\lambda_{i,b}z_0.
\]
Then
\[
\phi_{i,b}(u_{i,a})=\lambda_{i,a}-\lambda_{i,b},
\]
which is zero exactly when \(a=b\).

Set
\[
U_x=\bigotimes_{i=1}^n u_{i,x_i}
\in(\mathbb R^2)^{\otimes n},
\qquad
\Phi_y=\bigotimes_{i=1}^n\phi_{i,y_i}.
\]
Then
\[
\Phi_y(U_x)\ne0
\quad\Longleftrightarrow\quad
x_i\ne y_i\text{ for every }i.
\]
Hence
\[
\Phi_{y^{(j)}}(U_{x^{(k)}})
=
\begin{cases}
\ne0,&j=k,\\
0,&j\ne k.
\end{cases}
\]
The vectors \(U_{x^{(1)}},\dots,U_{x^{(t)}}\) are therefore linearly independent in a \(2^n\)-dimensional vector space. Thus \(t\le2^n\). ∎

## Lemma 3.2: Blocker inequality

Let \(\mathcal A\subseteq\Omega\) be the set of labels of classes meeting \(L\). Define
\[
B(\mathcal A)
=
\{y\in\Omega:\text{ for every }x\in\mathcal A,\ y
\text{ and }x\text{ agree in some coordinate}\}.
\tag{3.3}
\]
Thus \(B(\mathcal A)\) is the set of quotient vertices having no neighbor in \(\mathcal A\).

Then
\[
2t\le W(B(\mathcal A))-\ell.
\tag{3.4}
\]

### Proof

The social vertices are nonadjacent to every member of \(L\), since the members of \(L\) are isolated in \(G[S]\). Every private neighbor of a social vertex is also nonadjacent to every member of \(L\).

The \(t\) social vertices and their \(t\) private neighbors are pairwise distinct and lie outside \(L\). All \(2t\) therefore belong to the union of the classes indexed by \(B(\mathcal A)\), outside \(L\). This gives (3.4). ∎

In particular, if \(S\) were a counterexample, then
\[
t>\alpha(G)-\ell.
\]
Together with Lemmas 3.1 and 3.2 this would imply
\[
\ell>\alpha(G)-2^n
\tag{3.5}
\]
and
\[
W(B(\mathcal A))+\ell>2\alpha(G).
\tag{3.6}
\]

---

# 4. Bipartite graphs

The following elementary fact settles every product having a complete bipartite factor.

## Proposition 4.1
Every bipartite graph \(G\) satisfies
\[
IR(G)=\alpha(G).
\]

### Proof

Let \(V(G)=X\sqcup Y\), and let \(S\) be irredundant. Let \(L_Y\) be the lonely vertices of \(S\cap Y\). For every social \(y\in S\cap Y\), choose a private neighbor \(p_y\in X\setminus S\).

The set
\[
I=(S\cap X)\cup L_Y\cup
\{p_y:y\in S\cap Y\text{ is social}\}
\]
is independent:

* all vertices in \(S\cap X\) and all the \(p_y\)'s lie in \(X\);
* the vertices of \(L_Y\) have no neighbors in \(S\cap X\);
* privacy implies that every \(p_y\) is nonadjacent to every vertex of \(L_Y\);
* distinct social vertices have distinct private neighbors.

Moreover,
\[
|I|=|S\cap X|+|L_Y|+|S\cap Y\setminus L_Y|=|S|.
\]
Thus \(|S|\le\alpha(G)\). Since every independent set is irredundant, equality follows. ∎

If one factor \(H_i\) has two parts, the direct product is bipartite, colored by the two parts of that factor. If one factor has one part, the direct product is edgeless. This proves Theorem A(2).

---

# 5. A general quotient-weight gap criterion

Define the positive gap
\[
\Delta(Q,w)
=
\min\{
\alpha_w(Q)-W(\mathcal F):
\mathcal F\text{ independent and }W(\mathcal F)<\alpha_w(Q)
\}.
\tag{5.1}
\]

## Proposition 5.1
If
\[
\Delta(Q,w)\ge2^n,
\tag{5.2}
\]
then \(IR(G)=\alpha(G)\).

### Proof

Suppose \(S\) is irredundant, with lonely-label support \(\mathcal A\).

If \(R=\varnothing\), then \(S\) is independent. Assume \(R\ne\varnothing\). I claim
\[
W(\mathcal A)<\alpha(G).
\tag{5.3}
\]
Indeed, if \(W(\mathcal A)=\alpha(G)\), then \(\mathcal A\) is a maximum-weight independent family. A social vertex has a label \(y\notin\mathcal A\), and it is nonadjacent to every class represented in \(\mathcal A\). Hence \(\mathcal A\cup\{y\}\) would be independent and have larger weight, a contradiction.

Therefore
\[
\alpha(G)-\ell
\ge
\alpha(G)-W(\mathcal A)
\ge\Delta(Q,w).
\]
If \(|S|>\alpha(G)\), then
\[
t>\alpha(G)-\ell\ge\Delta(Q,w)\ge2^n,
\]
contrary to Lemma 3.1. ∎

## Corollary 5.2
If
\[
\prod_{i=1}^n \gcd_a s_{i,a}\ge2^n,
\]
then \(IR(G)=\alpha(G)\).

### Proof

Put
\[
g=\prod_i\gcd_a s_{i,a}.
\]
Every cell weight \(w(x)\), hence every independent-family weight \(W(\mathcal F)\), is divisible by \(g\). Thus every positive difference between \(\alpha_w(Q)\) and a smaller independent-family weight is at least \(g\). Apply Proposition 5.1. ∎

For example, the conjecture holds if every part of every factor has even size. In the balanced case, with common part size \(u_i\) in \(H_i\), it holds whenever
\[
\prod_i u_i\ge2^n.
\]

---

# 6. Products of one or two factors

## 6.1 One factor

Let \(H\) be complete multipartite. Then
\[
\alpha(H)=\max\{\text{part size}\}.
\]

Let \(S\) be irredundant. If \(S\) has a lonely vertex, every member of \(S\) lies in that vertex's part, so \(S\) is independent.

Otherwise there is at most one selected vertex in each part. A private neighbor of \(v\in S\) must lie in the same part as every member of \(S\setminus\{v\}\). Hence \(|S|\le2\). If \(|S|=2\), each of the two occupied parts must have size at least two, because the private neighbor of either selected vertex is an unselected vertex in the other occupied part. Thus \(|S|\le\alpha(H)\).

Hence \(IR(H)=\alpha(H)\).

## 6.2 Two factors

Consider an arbitrary blow-up of
\[
K_r\times K_c.
\]
Its quotient cells are indexed by pairs \((i,j)\), and cell \((i,j)\) has a positive integer capacity \(w_{ij}\). Two cells are adjacent when both their row and column differ.

Every independent family of cells is contained in one row or one column. Therefore
\[
\alpha
=
\max\left\{
\max_i\sum_jw_{ij},
\max_j\sum_iw_{ij}
\right\}.
\tag{6.1}
\]

Let \(S\) be irredundant.

### Lonely cells

If lonely vertices occur in two distinct cells, those two cells lie in a common row or column. Suppose they lie in row \(i\), in distinct columns. Any occupied cell nonadjacent to both must also lie in row \(i\). Thus every selected vertex is lonely and \(S\) is independent.

Suppose instead that the lonely vertices occupy exactly one cell \(z=(i_0,j_0)\). Every social cell lies in row \(i_0\) or column \(j_0\). There must be a social cell on each arm of this cross.

There can be at most one social cell on the row arm. Indeed, let \(x=(i_0,j)\) be one such cell and let \((i',j')\) label a private neighbor of its selected vertex. Adjacency to \(x\) gives \(i'\ne i_0\), \(j'\ne j\). Nonadjacency to \(z\) forces \(j'=j_0\). Such a private neighbor would be adjacent to every other row-arm cell. The column-arm case is symmetric.

Thus there are exactly two social vertices, one in each arm. If there are at least three rows, column \(j_0\) contains at least two positive-capacity cells besides \(z\), and hence has weight at least \(w(z)+2\). If there are exactly two rows, the private neighbor of the row-arm vertex must be an unselected twin in the unique column-arm cell, forcing that cell to have capacity at least two. In either case
\[
|S|\le |S\cap C_z|+2\le\alpha.
\]

### No lonely vertices

Now every occupied cell contains exactly one selected vertex. Let \(\mathcal S\) be the set of occupied cells and \(m=|\mathcal S|\).

For each \(x=(i,j)\in\mathcal S\), if \((\rho,\kappa)\) labels a private neighbor, then
\[
\mathcal S\setminus\{x\}
\subseteq
(\{\rho\}\times[c])\cup([r]\times\{\kappa\}),
\qquad
\rho\ne i,\quad \kappa\ne j.
\tag{6.2}
\]

No row or column contains three members of \(\mathcal S\): applying (6.2) to one of three cells in the same row would force the other two, in distinct columns, both to lie in column \(\kappa\).

It follows from (6.2) that \(m\le5\). In fact \(m\ne5\). If \(m=5\), then for a chosen \(x\), the other four cells consist of two cells in row \(\rho\) and two cells in column \(\kappa\), with \((\rho,\kappa)\) unoccupied. Applying (6.2) to one of the two row cells forces a private-neighbor column equal to the other row cell's column; the two column cells would then force the private-neighbor row to be two distinct rows, impossible. Hence
\[
m\le4.
\tag{6.3}
\]

If \(m\le\max(r,c)\), then (6.1) gives \(m\le\alpha\), since every cell capacity is at least one. It remains to consider \(m>\max(r,c)\). By (6.3), either:

* \(m=3\) and \(r=c=2\), or
* \(m=4\) and \(r,c\le3\).

The first case is impossible without a lonely selected vertex: \(K_2\times K_2\) is a matching on four quotient cells, and any three cells include an endpoint whose mate is absent.

For \(m=4\), view the occupied cells as four edges of the bipartite incidence graph between rows and columns. Its maximum degree is two. Up to components, the possible four-edge graphs are
\[
C_4,\quad P_5,\quad P_4\sqcup P_2,\quad
P_3\sqcup P_3,\quad P_3\sqcup2P_2,\quad4P_2.
\]
Under \(r,c\le3\), condition (6.2) eliminates every type except \(C_4\) and \(P_5\):

* in \(P_4\sqcup P_2\), applying (6.2) to the middle edge of \(P_4\) fails on the isolated edge;
* two oppositely oriented \(P_3\)'s fail (6.2) at an edge of one component, while two equally oriented \(P_3\)'s require four rows or four columns;
* \(P_3\sqcup2P_2\) and \(4P_2\) require at least four rows or columns.

If the incidence graph is a \(C_4\), the unique possible private-neighbor label for each corner is the opposite corner. Since that corner is occupied, its cell must have an unselected vertex; all four cell capacities are at least two. Some row has weight at least four.

If the incidence graph is a \(P_5\), write its cells as
\[
(i_1,j_1),\ (i_2,j_1),\ (i_2,j_2),\ (i_3,j_2).
\]
The private neighbor of the first endpoint must lie in cell \((i_2,j_2)\), and that of the other endpoint must lie in \((i_2,j_1)\). Both middle cells therefore have capacity at least two, so row \(i_2\) has weight at least four.

Thus \(m\le\alpha\) in all cases. This proves
\[
IR(H_1\times H_2)=\alpha(H_1\times H_2)
\]
for arbitrary complete multipartite \(H_1,H_2\).

---

# 7. Three factors: a weighted blocker theorem

The key point is a three-dimensional statement valid for arbitrary product weights.

Let
\[
\Omega=X_1\times X_2\times X_3
\]
and assign positive weights \(s_i(x_i)\) to the coordinate labels, with product weight
\[
w(x_1,x_2,x_3)=s_1(x_1)s_2(x_2)s_3(x_3).
\]
Adjacency means differing in all three coordinates. Let \(\alpha_w\) be the maximum weight of an independent family.

## Lemma 7.1
If \(\mathcal A\subseteq\Omega\) is independent and \(|\mathcal A|\ge2\), then
\[
W(\mathcal A)+W(B(\mathcal A))\le2\alpha_w.
\tag{7.1}
\]

### Proof

Two distinct members of \(\mathcal A\) differ in one or two coordinates.

### Case 1: Every pair differs in one coordinate

Then \(\mathcal A\) lies on a single coordinate line. Suppose it varies in coordinate \(k\), while coordinates \(i,j\) have fixed values. Let \(D_i,D_j\) be the corresponding coordinate fibres.

Every blocker of two distinct points of that line lies in \(D_i\cup D_j\), while
\[
\mathcal A\subseteq D_i\cap D_j.
\]
Therefore
\[
W(\mathcal A)+W(B(\mathcal A))
\le
W(D_i\cap D_j)+W(D_i\cup D_j)
=
W(D_i)+W(D_j)
\le2\alpha_w.
\]

### Case 2: Some pair differs in two coordinates

Write such a pair, with coordinates ordered as \((k,i,j)\), as
\[
x=(c,a,b),\qquad y=(c,a',b'),
\]
where \(a\ne a'\) and \(b\ne b'\). Let
\[
D=\{(c,u,v):u\in X_i,\ v\in X_j\}.
\]

#### Case 2a: \(\mathcal A\not\subseteq D\)

Choose \(z\in\mathcal A\setminus D\). Since \(z\) is nonadjacent to both \(x\) and \(y\), after symmetry we may write
\[
z=(d,a,b'),\qquad d\ne c.
\]
Define
\[
\mathcal F=
\{(c,u,v):u=a\text{ or }v=b'\}
\cup
\{(e,a,b'):e\ne c\},
\]
and
\[
q=(d,a',b).
\]
A direct check gives
\[
B(\{x,y,z\})=\mathcal F\cup\{q\}.
\tag{7.2}
\]
The family \(\mathcal F\) is independent.

If \(q\in\mathcal A\), another direct check gives
\[
B(\{x,y,z,q\})=\{x,y,z,q\}.
\]
Since \(\mathcal A\) is independent, it must then equal these four points, and
\[
B(\mathcal A)=\mathcal A.
\]
Thus (7.1) follows.

Assume \(q\notin\mathcal A\). Put
\[
\mathcal F_0=B(\mathcal A)\cap\mathcal F.
\]
Then \(\mathcal F_0\) is independent. If \(q\in B(\mathcal A)\), then \(\mathcal A\cup\{q\}\) is independent; otherwise \(\mathcal A\) itself is independent. In either event, (7.2) decomposes the two weights in (7.1) as the sum of the weights of two independent families. Hence (7.1).

#### Case 2b: \(\mathcal A\subseteq D\)

Project \(\mathcal A\) to \(\overline{\mathcal A}\subseteq X_i\times X_j\), and define
\[
C=
\{(u,v):\text{ every }(r,s)\in\overline{\mathcal A}
\text{ has }r=u\text{ or }s=v\}.
\]
Then
\[
B(\mathcal A)
=
D\cup\bigl((X_k\setminus\{c\})\times C\bigr).
\tag{7.3}
\]

The two projected points \((a,b)\) and \((a',b')\) show that
\[
C\subseteq\{(a,b'),(a',b)\}.
\tag{7.4}
\]

If \(|C|\le1\), then
\[
\mathcal I
=
\mathcal A\cup\bigl((X_k\setminus\{c\})\times C\bigr)
\]
is independent. Equation (7.3) gives
\[
W(\mathcal A)+W(B(\mathcal A))
=
W(D)+W(\mathcal I)
\le2\alpha_w.
\]

It remains to consider
\[
C=\{(a,b'),(a',b)\}.
\]
The intersection of the two corresponding row-column crosses is exactly
\[
\{(a,b),(a',b')\}.
\]
Hence
\[
\mathcal A=\{x,y\}.
\]

Let
\[
T_h=\sum_{\xi\in X_h}s_h(\xi)
\]
be the total coordinate weights, and put
\[
p=s_k(c),\quad
r=s_i(a),\quad r'=s_i(a'),\quad
u=s_j(b),\quad u'=s_j(b').
\]
Let \(r_*=\max(r,r')\). From (7.3),
\[
\begin{aligned}
W(\mathcal A)+W(B(\mathcal A))
={}&pT_iT_j\\
&+p(ru+r'u')+(T_k-p)(ru'+r'u).
\end{aligned}
\]
Both
\[
ru+r'u'\le r_*(u+u')\le r_*T_j
\]
and
\[
ru'+r'u\le r_*(u+u')\le r_*T_j.
\]
Therefore
\[
W(\mathcal A)+W(B(\mathcal A))
\le
pT_iT_j+r_*T_kT_j.
\]
The two terms on the right are the weights of two coordinate fibres, each independent. Thus they are each at most \(\alpha_w\), proving (7.1). ∎

## Theorem 7.2
For arbitrary complete multipartite \(H_1,H_2,H_3\),
\[
IR(H_1\times H_2\times H_3)
=
\alpha(H_1\times H_2\times H_3).
\]

### Proof

If a factor has one part, the product is edgeless. If a factor has two parts, apply Proposition 4.1. Thus assume every factor has at least three parts.

Let \(S\) be irredundant, with lonely-label support \(\mathcal A\).

If \(|\mathcal A|\ge2\), then Lemmas 3.2 and 7.1 give
\[
\begin{aligned}
|S|
&=\ell+t\\
&\le \ell+\frac{W(B(\mathcal A))-\ell}{2}\\
&=\frac{\ell+W(B(\mathcal A))}{2}\\
&\le\frac{W(\mathcal A)+W(B(\mathcal A))}{2}\\
&\le\alpha(G).
\end{aligned}
\]

If \(\mathcal A=\varnothing\), Lemma 3.1 gives
\[
|S|=t\le8.
\]
A coordinate fibre contains at least \(3\cdot3=9\) positive-capacity quotient cells, so \(\alpha(G)\ge9\).

Finally, suppose \(\mathcal A=\{x\}\). Then
\[
\ell\le w(x),\qquad t\le8.
\]
Any coordinate fibre through \(x\) contains at least eight other positive-capacity cells. Hence
\[
\alpha(G)\ge w(x)+8\ge\ell+t.
\]

Thus every irredundant set has size at most \(\alpha(G)\). The reverse inequality is automatic because every independent set is irredundant. ∎

This completes the proof of Theorem A(1).

---

# 8. What remains

The argument leaves open the case

\[
n\ge4,\qquad q_i\ge3\ \text{for every }i,
\]
when the quotient weight gap from Proposition 5.1 is smaller than \(2^n\).

A counterexample in that range would have to yield a lonely-label family \(\mathcal A\) and lonely count \(\ell\) satisfying all of
\[
W(\mathcal A)<\alpha(G),
\qquad
\ell>\alpha(G)-2^n,
\qquad
W(B(\mathcal A))+\ell>2\alpha(G).
\tag{8.1}
\]
In particular,
\[
W(\mathcal A)+W(B(\mathcal A))>2\alpha(G).
\tag{8.2}
\]

The clean three-dimensional blocker inequality does not extend verbatim. For example, in the unweighted quotient \(K_3^4\), let
\[
\mathcal A=\{(0,0,0,0),(1,0,0,0)\}.
\]
Then
\[
|B(\mathcal A)|=3^4-3\cdot2^3=57,
\]
while \(\alpha(K_3^4)=27\). Thus
\[
|\mathcal A|+|B(\mathcal A)|=59>54=2\alpha(K_3^4).
\]
This is not a counterexample to the irredundance conjecture—the social bound \(t\le16\) rules out such a small lonely family—but it shows why the three-factor proof does not directly iterate.

Accordingly, the original conjecture is not resolved here. The remaining task is to control near-maximum weighted independent families and their blockers in dimensions at least four, specifically in the small-gap regime not covered by Proposition 5.1.