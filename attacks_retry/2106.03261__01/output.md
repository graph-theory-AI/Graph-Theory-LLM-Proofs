```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit asymptotically regular C4-free construction disproves Petersen countability; the dodecahedral case remains unresolved here.",
  "would_publish": true,
  "caveats": "The dodecahedral case is not settled, and literature priority for the Petersen construction has not been checked."
}
```

# A counterexample for Petersen countability

The Petersen closure pattern in the previous attempt is correct. However, it leads to a counterexample rather than a counting argument: in a three-dimensional polarity model, its last edge is algebraically forced by the other fourteen edges. One can change the equation defining that last pair while preserving both global \(C_4\)-freeness and asymptotic regularity.

The construction below rules out **all Petersen homomorphisms**, not merely canonical copies. Thus the distinction between unrestricted and vertex-restricted counting does not affect the counterexample.

## 1. The counting conclusion that will fail

For a graph \(G\) on \(N\) vertices, write \(A_G\) for its adjacency matrix. For a weighted graph \(h\) on the same vertex set, put
\[
t_F(h)=\frac{1}{N^{v(F)}}\sum_{\phi:V(F)\to V(G)}
       \prod_{uv\in E(F)}h(\phi(u),\phi(v)).
\]
Then
\[
t_F(\sqrt N A_G)
=\frac{\operatorname{hom}(F,G)}
       {N^{v(F)-e(F)/2}}.
\]

Use the normalized cut norm
\[
\|K\|_\square
=\frac1{N^2}\max_{X,Y\subseteq V(G)}
 \left|\sum_{x\in X,\ y\in Y}K(x,y)\right|.
\]

A necessary consequence of countability is the following: if \(G_N\) is \(C_4\)-free, has the required \(O(\sqrt N)\) maximum-degree bound, and \(h_N\in[0,1]\) satisfies
\[
\|\sqrt N A_{G_N}-h_N\|_\square\longrightarrow0,
\]
then the normalized \(F\)-count in \(G_N\) cannot stay zero while \(t_F(h_N)\) stays bounded away from zero.

We will construct, for infinitely many \(N\),
\[
\begin{aligned}
&G_N\text{ is }C_4\text{-free},\qquad
  \Delta(G_N)<\sqrt N,\\
&\|\sqrt N A_{G_N}-h_N\|_\square\le 3N^{-1/4},\\
&\operatorname{hom}(P,G_N)=0,\qquad
  \liminf_{N\to\infty}t_P(h_N)\ge 10^{-10},
\end{aligned}
\tag{1.1}
\]
where \(P\) is the Petersen graph. Moreover,
\[
e(G_N)=\left(\frac{3}{20}+o(1)\right)N^{3/2}.
\]
Thus these are genuinely critical-density hosts.

---

## 2. An exact polarity identity for Petersen minus one edge

Represent \(P\) as the graph of disjoint two-element subsets of \(\{1,2,3,4,5\}\), and label its vertices
\[
\begin{array}{lllll}
a=12,&b=13,&c=14,&d=45,&e=35,\\
f=25,&g=23,&h=24,&i=34,&j=15.
\end{array}
\]

The fourteen edges other than \(ij\) are specified by
\[
\begin{array}{c|c}
\text{vertex}&\text{two prescribed neighbors}\\ \hline
d&a,b\\
e&a,c\\
f&b,c\\
g&c,d\\
h&b,e\\
i&a,f\\
j&g,h
\end{array}
\tag{2.1}
\]

### Lemma 2.1 — Forced final orthogonality

Let \(V\) be a three-dimensional vector space over a field, equipped with a nondegenerate symmetric bilinear form \(\langle\cdot,\cdot\rangle\). Assign ten pairwise distinct projective points
\[
A,B,C,D,E,F,G,H,I,J
\]
to the vertices in (2.1). Suppose every edge in (2.1) joins orthogonal points. Then
\[
\langle I,J\rangle=0.
\]

#### Proof

First, \(A,B,C\) are linearly independent. Otherwise their pairwise spans would coincide, and their orthogonal complements would force \(D,E,F\) to represent the same projective point.

Set
\[
\alpha=\langle A,B\rangle,\qquad
\beta=\langle A,C\rangle,\qquad
\gamma=\langle B,C\rangle.
\]

Because \(D\) is orthogonal to \(A,B\),
\[
D^\perp=\operatorname{span}(A,B).
\]
The conditions \(G\perp D,C\) therefore give
\[
G\ \sim\ \gamma A-\beta B,
\tag{2.2}
\]
where \(\sim\) denotes equality up to a nonzero scalar.

The vector on the right is nonzero: if \(\beta=\gamma=0\), then \(C\) and \(D\) both span \(\operatorname{span}(A,B)^\perp\), contradicting projective distinctness.

Similarly,
\[
H\ \sim\ \gamma A-\alpha C,\qquad
I\ \sim\ \beta B-\alpha C.
\tag{2.3}
\]
The corresponding exceptional cases would respectively give \(B\sim E\) and \(A\sim F\), so both displayed vectors are nonzero.

Now
\[
(\gamma A-\beta B)-(\gamma A-\alpha C)
       +(\beta B-\alpha C)=0.
\]
Consequently,
\[
I\in\operatorname{span}(G,H).
\]
Since \(J\perp G,H\), it follows that \(J\perp I\). ∎

This lemma is the obstruction: the final pair cannot independently behave like a regular sparse pair.

---

## 3. The finite-field construction

Let \(q>20\) be an odd prime, and set
\[
N=q^2.
\]
Partition \(\mathbb F_q\) into ten sets
\[
(T_r)_{r\in V(P)}
\]
whose sizes differ by at most one.

This can be completely explicit: identify \(\mathbb F_q\) with the residues \(0,\ldots,q-1\), order the labels as \(a,b,\ldots,j\), and assign residues according to their ordinary integer residue modulo \(10\).

Put
\[
V_r=T_r\times\mathbb F_q.
\]
These ten classes partition the vertex set \(\mathbb F_q^2\).

For every template edge \(rs\in E(P)\), define a symmetric constant
\[
c_{rs}=
\begin{cases}
1,&rs=ij,\\
0,&rs\ne ij.
\end{cases}
\tag{3.1}
\]

Define a simple graph \(G_q\) as follows. For
\[
(x,y)\in V_r,\qquad (x',y')\in V_s,
\]
put an edge precisely when
\[
rs\in E(P)
\quad\text{and}\quad
y+y'+xx'=c_{rs}.
\tag{3.2}
\]
There are no other edges.

Let \(H_q\) be the complete blow-up of \(P\) with these vertex classes, and let
\[
h_q=A_{H_q}.
\]

### Degrees and pair densities

For a fixed \((x,y)\in V_r\), and every \(x'\in T_s\) with \(rs\in E(P)\), equation (3.2) determines exactly one \(y'\). Hence
\[
d_{G_q}((x,y))
=\sum_{s\in N_P(r)}|T_s|
\le 3\left\lceil\frac q{10}\right\rceil<q=\sqrt N.
\tag{3.3}
\]

Every required pair has density exactly
\[
d_{G_q}(V_r,V_s)=\frac1q=N^{-1/2}.
\tag{3.4}
\]
Also,
\[
e(G_q)
=q\sum_{rs\in E(P)}|T_r||T_s|
=\left(\frac{15}{100}+o(1)\right)q^3.
\tag{3.5}
\]

---

## 4. Global \(C_4\)-freeness

We show that any two distinct vertices have at most one common neighbor.

Take
\[
u=(x,y)\in V_r,\qquad u'=(x',y')\in V_s.
\]

### Case 1: \(r=s\)

If \(w=(z,t)\in V_\ell\) is a common neighbor, subtracting its two edge equations gives
\[
(x-x')z+(y-y')=0.
\tag{4.1}
\]

If \(x=x'\), then \(y\ne y'\), so no common neighbor exists.

Otherwise, (4.1) determines \(z\) uniquely. Crucially, it does so **independently of \(\ell\)**: the constants \(c_{r\ell}\) cancel. Since the sets \(T_\ell\) partition \(\mathbb F_q\), this \(z\) belongs to at most one possible neighbor class. Once that class is known, the edge equation determines \(t\) uniquely.

### Case 2: \(r\ne s\)

Now \(x\ne x'\), because \(T_r\cap T_s=\varnothing\).

A common neighbor must have type
\[
\ell\in N_P(r)\cap N_P(s).
\]
The Petersen graph has at most one common neighbor for every pair of distinct vertices, so there is at most one possible \(\ell\).

For this fixed \(\ell\), subtracting the edge equations gives
\[
(x-x')z+(y-y')=c_{r\ell}-c_{s\ell},
\]
which determines \(z\), and then \(t\), uniquely.

Thus all pairs have codegree at most one, proving that \(G_q\) is \(C_4\)-free. In fact, it is also triangle-free, since its type graph \(P\) is triangle-free. ∎

The partition of the **first coordinate**, rather than an arbitrary partition of \(\mathbb F_q^2\), is essential here.

---

## 5. Asymptotic regularity and the cut approximation

For \(c\in\mathbb F_q\), consider the \(q^2\times q^2\) matrix
\[
M_c((x,y),(x',y'))=1_{\{y+y'+xx'=c\}}.
\]
Every row and column has sum \(q\).

Let \(J\) be the all-ones matrix, and let \(K\) be block diagonal with one all-ones \(q\times q\) block for each fixed first coordinate \(x\). A direct common-neighbor calculation gives
\[
M_cM_c^{\mathsf T}=qI+J-K.
\]
Consequently,
\[
\left(M_c-\frac Jq\right)
\left(M_c-\frac Jq\right)^{\mathsf T}
=qI-K,
\]
and hence
\[
\left\|M_c-\frac Jq\right\|_{\mathrm{op}}=\sqrt q.
\tag{5.1}
\]

In particular, for arbitrary \(X,Y\subseteq\mathbb F_q^2\),
\[
\left|
\sum_{u\in X,v\in Y}M_c(u,v)-\frac{|X||Y|}{q}
\right|
\le \sqrt q\,\sqrt{|X||Y|}.
\tag{5.2}
\]

Restricting to any required pair \(V_r,V_s\) preserves this bound. Thus every required pair is \((\varepsilon,N^{-1/2})\)-regular for every fixed \(\varepsilon>0\), once \(q\) is sufficiently large.

For completeness, we obtain the global cut bound directly. Write
\[
D=A_{G_q}-\frac1q A_{H_q}.
\]
For \(X,Y\subseteq V(G_q)\), put \(X_r=X\cap V_r\), \(Y_s=Y\cap V_s\). By (5.2),
\[
\left|\sum_{u\in X,v\in Y}D(u,v)\right|
\le \sqrt q
\sum_{\substack{(r,s)\\rs\in E(P)}}
\sqrt{|X_r||Y_s|},
\]
where the last sum uses ordered adjacent pairs.

Since \(P\) is cubic, Cauchy–Schwarz gives
\[
\sum_{\substack{(r,s)\\rs\in E(P)}}
\sqrt{|X_r||Y_s|}
\le 3\sqrt{|X||Y|}.
\]
Therefore
\[
\begin{aligned}
\|\sqrt N A_{G_q}-h_q\|_\square
&=\frac1{N^2}
 \max_{X,Y}\left|q\sum_{u\in X,v\in Y}D(u,v)\right|\\
&\le \frac{3q^{3/2}N}{N^2}
=3q^{-1/2}
=3N^{-1/4}.
\end{aligned}
\tag{5.3}
\]

Thus \(h_q\) is an asymptotically exact bounded cut approximation.

---

## 6. There are no canonical Petersen copies

Associate to a vertex \((x,y)\) the projective point represented by
\[
p(x,y)=(1,x,y)\in\mathbb F_q^3.
\]
Use the nondegenerate symmetric bilinear form
\[
\langle (z,x,y),(z',x',y')\rangle
=zy'+yz'+xx'.
\tag{6.1}
\]
In particular,
\[
\langle p(x,y),p(x',y')\rangle=y+y'+xx'.
\]

Suppose there were a canonical Petersen copy in \(G_q\), with one vertex in each \(V_r\).

Its ten first coordinates would be distinct, because they lie in different sets \(T_r\). Its ten associated projective points would therefore be pairwise distinct.

For all fourteen template edges other than \(ij\), equation (3.2) says that the corresponding points are orthogonal. Lemma 2.1 then gives
\[
\langle I,J\rangle=0.
\]
But the edge \(ij\) requires
\[
\langle I,J\rangle=1.
\]
This is impossible. Hence there is no canonical Petersen copy.

---

## 7. There are no Petersen homomorphisms at all

We need a small property of \(P\).

### Lemma 7.1

Every endomorphism \(P\to P\) is an automorphism.

#### Proof

Every pair of distinct Petersen vertices lies on a common \(5\)-cycle.

Indeed, permutations of \(\{1,\ldots,5\}\) act transitively on intersecting pairs of two-subsets and on disjoint pairs. Representative cycles are
\[
12,45,13,24,35,12
\]
for the intersecting pair \(12,13\), and
\[
12,34,15,23,45,12
\]
for the disjoint pair \(12,34\).

A homomorphism from a \(5\)-cycle into a graph of girth \(5\) is injective: a noninjective closed walk of length \(5\) would contain an odd cycle of length less than \(5\).

Therefore an endomorphism of \(P\) cannot identify any two vertices. It is consequently an automorphism. ∎

Now the type map
\[
\tau:V(G_q)\longrightarrow V(P)
\]
is a graph homomorphism. If \(\phi:P\to G_q\) were any graph homomorphism, then
\[
\tau\circ\phi:P\to P
\]
would be an automorphism. Relabeling the source by its inverse would produce a canonical Petersen copy, which Section 6 excludes.

Thus
\[
\operatorname{hom}(P,G_q)=0.
\tag{7.1}
\]

---

## 8. Contradiction to Petersen countability

The dense comparison graph \(H_q\) contains every canonical Petersen copy, so
\[
t_P(h_q)
\ge \frac{\prod_{r\in V(P)}|V_r|}{N^{10}}
=\prod_{r\in V(P)}\frac{|T_r|}{q}
\longrightarrow 10^{-10}.
\tag{8.1}
\]

On the other hand,
\[
t_P(\sqrt N A_{G_q})
=\frac{\operatorname{hom}(P,G_q)}{N^{5/2}}
=0.
\tag{8.2}
\]

Equations (3.3), (5.3), (8.1), and (8.2) give exactly the sequence asserted in (1.1). They violate the lower-counting conclusion with a fixed positive error gap, even though the cut discrepancy tends to zero.

Therefore:

\[
\boxed{\text{The Petersen graph is not countable in }C_4\text{-free graphs.}}
\]

No computational assumption or unproved mixing statement is used.

## 9. Scope and remaining gap

This settles the Petersen half of the question negatively.

It does **not** settle the dodecahedral half. Petersen-freeness of the constructed hosts does not imply dodecahedron-freeness, and I have not established a deficient dodecahedral count in these hosts. The forced-orthogonality identity above is specific to the displayed Petersen configuration; no corresponding obstruction for the dodecahedron has been proved here.