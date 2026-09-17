```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The Petersen graph is not countable: a twisted affine-polarity construction gives C4-free graphs with a positive Petersen prediction but no Petersen homomorphism.",
  "would_publish": true,
  "caveats": "The full characterization and the dodecahedral case remain unresolved here; novelty has not been independently checked."
}
```

# A negative answer for the Petersen graph

I obtain an explicit obstruction for the Petersen graph, one of the specific cases highlighted in the question. The argument is self-contained. The finite-geometric idea in the previous attempt provides motivation, but its asserted Heawood result is not used.

Write \(P\) for the Petersen graph, with vertices
\[
a_0,\ldots,a_4,\quad b_0,\ldots,b_4
\]
and edges
\[
a_i a_{i+1},\qquad a_i b_i,\qquad b_i b_{i+2},
\]
where subscripts are modulo \(5\).

## The result

**Theorem.** There are graphs \(G_q,D_q\) on the same \(n_q\)-vertex set, with \(n_q\to\infty\), such that:

1. \(G_q\) has girth at least \(5\), and
   \[
   \Delta(G_q)\le \frac{3}{10}\sqrt{n_q},
   \qquad
   e(G_q)=\left(\frac{3}{20}+o(1)\right)n_q^{3/2}.
   \]
2. \(D_q\) is a complete balanced blow-up of \(P\).
3. In the normalized cut discrepancy appropriate to this problem,
   \[
   \max_{S,T\subseteq V(G_q)}
   \left|
   \frac{e_{G_q}(S,T)}{n_q^{3/2}}
   -
   \frac{e_{D_q}(S,T)}{n_q^2}
   \right|\longrightarrow 0.
   \]
4. Nevertheless,
   \[
   \operatorname{hom}(P,G_q)=0,
   \qquad
   \frac{\operatorname{hom}(P,D_q)}{n_q^{10}}\ge 10^{-10}.
   \]

Here \(e(S,T)\) counts ordered adjacent pairs in \(S\times T\). In particular, this obstructs both canonical counting and unrestricted homomorphism counting. It also obstructs an injective-copy formulation.

Since
\[
v(P)-\frac{e(P)}2=10-\frac{15}{2}=\frac52,
\]
a Petersen counting lemma would require, for sufficiently small cut discrepancy,
\[
\frac{\operatorname{hom}(P,G_q)}{n_q^{5/2}}
\ge
\frac{\operatorname{hom}(P,D_q)}{n_q^{10}}-\varepsilon.
\]
Taking \(\varepsilon<10^{-10}\) contradicts item 4.

The construction rests on a projective completion identity and a way of twisting one regular pair without introducing \(C_4\)'s.

---

## 1. An orthogonality completion identity

Let \(K\) be a field of odd characteristic, and let \(B\) be a nondegenerate symmetric bilinear form on \(K^3\). Orthogonality of projective points means orthogonality of their representatives.

**Lemma 1.** Assign pairwise distinct projective points
\[
A_0,\ldots,A_4,\quad B_0,\ldots,B_4
\]
to the vertices of \(P\). Suppose:

- \(A_0\) and \(A_1\) are nonisotropic;
- every Petersen edge other than \(a_3b_3\) joins orthogonal points.

Then \(A_3\) and \(B_3\) are also orthogonal.

### Proof

Since \(A_0\perp A_1\) and both points are nonisotropic, their span is nondegenerate. Choose coordinates in which
\[
A_0=[1:0:0],\qquad A_1=[0:1:0],
\]
and
\[
B(X,Y)=\alpha X_1Y_1+\beta X_2Y_2+\gamma X_3Y_3,
\qquad \alpha\beta\gamma\ne0.
\]

The edges \(a_1a_2,a_0a_4,a_0b_0,a_1b_1\) allow us to write
\[
A_2=[x:0:z],\quad A_4=[0:y:w],\quad
B_0=[0:s:t],\quad B_1=[r:0:u].
\]

A projective point orthogonal to two distinct points is uniquely determined. Taking cross products of their polar-line coefficient vectors therefore gives the following representatives:
\[
\begin{array}{c|ccc}
 & X_1&X_2&X_3\\ \hline
 A_3&-\beta\gamma zy&-\alpha\gamma xw&\alpha\beta xy\\
 B_3& \beta\gamma su& \alpha\gamma tr&-\alpha\beta sr\\
 B_2& \beta\gamma sz& \alpha\gamma tx&-\alpha\beta sx\\
 B_4&-\beta\gamma uy&-\alpha\gamma rw& \alpha\beta ry.
\end{array}
\tag{1}
\]
For example, \(B_2\) is orthogonal to \(B_0,A_2\), while \(B_4\) is orthogonal to \(B_1,A_4\).

These representatives are nonzero because the points in each determining pair are distinct and \(B\) is nondegenerate. Direct multiplication in (1) gives
\[
\begin{aligned}
B(A_3,B_3)
&=-\alpha\beta^2\gamma^2zysu
  -\alpha^2\beta\gamma^2xwtr
  -\alpha^2\beta^2\gamma xysr\\
&=B(B_2,B_4).
\end{aligned}
\tag{2}
\]
The edge \(b_2b_4\) is present among the assumed fourteen orthogonalities, so the right-hand side is zero. Consequently \(A_3\perp B_3\).

No coordinate division was used after choosing the basis, so zero-coordinate cases are included. ∎

---

## 2. The twisted affine construction

Let
\[
q=11^r,\qquad k=\frac{q-1}{10}.
\]
Thus \(q\) has odd characteristic and \(k\) is an integer.

Partition the nonzero field elements into ten sets of equal size:
\[
\mathbb F_q^\times=\bigsqcup_{v\in V(P)} I_v,
\qquad |I_v|=k.
\]
For each Petersen vertex \(v\), define
\[
V_v=\{(x,y)\in\mathbb F_q^2:
             x\in I_v,\ 2y\ne x^2\}.
\]
These classes are disjoint, and
\[
|V_v|=k(q-1)=:m.
\]
The total number of vertices is therefore
\[
n=10m=(q-1)^2.
\tag{3}
\]

Assign constants to the Petersen edges by
\[
c_{uv}=
\begin{cases}
1,&\{u,v\}=\{a_3,b_3\},\\
0,&\text{otherwise}.
\end{cases}
\tag{4}
\]

Construct \(G_q\) as follows. Between classes \(V_u,V_v\) with \(uv\in E(P)\), join
\[
(x,y)\in V_u,\qquad (x',y')\in V_v
\]
exactly when
\[
y+y'=xx'+c_{uv}.
\tag{5}
\]
There are no other edges.

Let \(D_q\) be the complete blow-up of \(P\) on the same ten classes.

### Degree bounds

For a fixed vertex \((x,y)\) and a prescribed adjacent class \(V_v\), each \(x'\in I_v\) gives at most one candidate neighbor, namely
\[
y'=xx'-y+c_{uv}.
\]
Thus the degree into each required class is at most \(k\).

A candidate is excluded precisely when
\[
2(xx'-y+c_{uv})=(x')^2,
\]
a quadratic equation in \(x'\), with at most two solutions. Hence each required pair gives every vertex degree between \(k-2\) and \(k\). Consequently
\[
3k-6\le \deg_{G_q}(z)\le3k
\]
for every vertex \(z\). By (3),
\[
\Delta(G_q)\le3k=\frac3{10}\sqrt n,
\]
and
\[
e(G_q)=\left(\frac3{20}+o(1)\right)n^{3/2}.
\tag{6}
\]

---

## 3. Why the twist does not create a \(C_4\)

This is the purpose of partitioning the *first coordinates* into disjoint classes.

**Lemma 2.** The graph \(G_q\) is \(C_4\)-free.

### Proof

Suppose \(z_1z_2z_3z_4z_1\) were a \(4\)-cycle, with
\[
z_i=(x_i,y_i).
\]

Projecting each vertex to its Petersen class gives a closed walk of length four in \(P\). Since \(P\) is \(C_4\)-free, some pair of opposite vertices of the walk has the same class. Relabel so that \(z_1,z_3\in V_u\).

Subtracting the two edge equations involving \(z_2\) gives
\[
y_1-y_3=(x_1-x_3)x_2.
\tag{7}
\]
The edge-dependent constants cancel because \(z_1,z_3\) have the same class.

If \(x_1=x_3\), equation (7) gives \(y_1=y_3\), contrary to the distinctness of the cycle vertices. Thus \(x_1\ne x_3\). The equations involving \(z_4\) similarly give
\[
x_2=\frac{y_1-y_3}{x_1-x_3}=x_4.
\]
Since the sets \(I_v\) are disjoint, \(z_2,z_4\) must belong to the same class. Their equations with \(z_1\) now have the same constant and the same first coordinate, so \(y_2=y_4\). This again contradicts distinctness. ∎

Also, a triangle in \(G_q\) would project to a triangle in \(P\). Hence \(G_q\) is triangle-free as well.

---

## 4. There is no canonical Petersen copy

Associate the affine vertex \((x,y)\) with the projective point
\[
[1:x:y].
\]
Use the symmetric bilinear form
\[
B(X,Y)=X_0Y_2+X_2Y_0-X_1Y_1.
\tag{8}
\]
Its matrix is nonsingular. Moreover,
\[
B((1,x,y),(1,x,y))=2y-x^2,
\]
so every vertex retained in the construction is nonisotropic.

Suppose there were a canonical copy of \(P\), choosing one vertex from every \(V_v\).

The resulting ten projective points are pairwise distinct: their first affine coordinates lie in disjoint sets \(I_v\). On every Petersen edge except \(a_3b_3\), equations (4)–(5) give
\[
B((1,x,y),(1,x',y'))=0.
\]
Lemma 1 therefore forces orthogonality also on \(a_3b_3\).

But on that pair, the construction requires
\[
B((1,x,y),(1,x',y'))=1.
\]
This is impossible.

Thus \(G_q\) contains no canonical Petersen copy.

### In fact, there is no Petersen homomorphism at all

For completeness, the following verifies that noncanonical or collapsed maps cannot contribute.

**Lemma 3.** Every endomorphism of the Petersen graph is an automorphism.

### Proof

Use the equivalent description
\[
V(P)=\binom{[5]}2,
\]
with adjacency given by disjointness. The displayed outer/inner description is obtained by taking
\[
(a_0,\ldots,a_4)=(12,34,15,23,45),\qquad
(b_0,\ldots,b_4)=(35,25,24,14,13).
\]

An independent set is a pairwise intersecting family of edges of \(K_5\). Its size is at most four, and every independent set of size four is a star. Indeed, a pairwise intersecting family without a common endpoint has size at most three.

First, there is no homomorphism \(P\to C_5\). If its fibers have sizes \(s_0,\ldots,s_4\), the unions of nonadjacent fibers are independent, so
\[
s_i+s_{i+2}\le4.
\]
Summing gives equality in all five inequalities, because \(\sum s_i=10\). The resulting equations force \(s_i=2\) for every \(i\). Each union of two nonadjacent fibers is consequently a four-vertex star. Two such unions sharing one fiber intersect in two vertices, whereas two distinct four-vertex stars in \(P\) intersect in exactly one vertex. Contradiction.

Now choose an endomorphism of \(P\) with minimum image size. Taking a suitable power gives a retraction
\[
r:P\longrightarrow H,
\]
where every endomorphism of \(H\) is an automorphism.

Let \(\Gamma=S_5\) act transitively on \(V(P)\). For every \(\gamma\in\Gamma\), the map
\[
r\gamma|_H:H\longrightarrow H
\]
is an automorphism. Fix \(y\in V(H)\). Counting pairs \((\gamma,x)\) with \(x\in V(H)\) and \(r(\gamma x)=y\) gives
\[
|\Gamma|
=
|V(H)|\,\frac{|\Gamma|}{10}\,|r^{-1}(y)|.
\]
Thus \(|V(H)|\) divides \(10\).

The image of a \(5\)-cycle under \(r\) must contain a \(5\)-cycle, since \(H\subseteq P\) is triangle-free. Therefore \(|V(H)|\ge5\). If \(|V(H)|=5\), then \(H=C_5\), contradicting the preceding paragraph. Hence \(|V(H)|=10\), proving the lemma. ∎

The class projection
\[
\pi:G_q\longrightarrow P
\]
is a graph homomorphism. If \(\phi:P\to G_q\) existed, then \(\pi\phi\) would be an automorphism of \(P\). Reindexing \(\phi\) by its inverse would produce a canonical Petersen copy, already ruled out. Hence
\[
\operatorname{hom}(P,G_q)=0.
\tag{9}
\]

---

## 5. Uniform mixing of every required pair

For \(c\in\mathbb F_q\), let \(M_c\) be the \(q^2\times q^2\) matrix indexed by \(\mathbb F_q^2\), with
\[
M_c((x,y),(x',y'))=
\mathbf 1_{\{y+y'=xx'+c\}}.
\]

Every row and column has sum \(q\). Two distinct rows with different first coordinates have exactly one common \(1\)-entry, while distinct rows with the same first coordinate have none. Therefore
\[
M_cM_c^{\mathsf T}
=
qI+J-\bigoplus_{x\in\mathbb F_q}J_q.
\tag{10}
\]
It follows that the largest singular value is \(q\), and every singular value on the orthogonal complement of the constant vector is at most \(\sqrt q\).

Consequently, for arbitrary \(X,Y\subseteq\mathbb F_q^2\),
\[
\left|
\sum_{u\in X,v\in Y}M_c(u,v)
-\frac{|X||Y|}{q}
\right|
\le \sqrt q\,\sqrt{|X||Y|}.
\tag{11}
\]
This holds uniformly for both constants \(c=0\) and \(c=1\), and remains valid after restricting to the classes \(V_u,V_v\).

### Cut discrepancy

Let \(S,T\subseteq V(G_q)\). Sum (11) over the thirty oriented Petersen edge-pairs. Since every class has size \(m\),
\[
\left|
e_{G_q}(S,T)-\frac1q e_{D_q}(S,T)
\right|
\le30m\sqrt q.
\tag{12}
\]

Using \(n=10m=(q-1)^2\), we obtain
\[
\begin{aligned}
\left|
\frac{e_{G_q}(S,T)}{n^{3/2}}
-\frac{e_{D_q}(S,T)}{n^2}
\right|
&\le
\frac{30m\sqrt q}{n^{3/2}}
+
\left|\frac{\sqrt n}{q}-1\right|
\frac{e_{D_q}(S,T)}{n^2}\\
&\le
\frac{3\sqrt q}{q-1}+\frac1q.
\end{aligned}
\tag{13}
\]
The bound is independent of \(S,T\) and tends to zero.

### Regular-pair formulation

Put \(p=n^{-1/2}=1/(q-1)\). The degree bounds above imply that every required pair has density
\[
d(V_u,V_v)=(1+o(1))p.
\]

If \(X\subseteq V_u,Y\subseteq V_v\), with \(|X|,|Y|\ge\varepsilon m\), then (11) gives
\[
|d(X,Y)-d(V_u,V_v)|
\le
(\varepsilon^{-1}+1)\frac{\sqrt q}{m}
=o(p).
\]
Thus, for every fixed \(\varepsilon>0\), all fifteen required pairs are \((\varepsilon,p)\)-regular for sufficiently large \(q\). In fact, they are also asymptotically regular at the individual-vertex degree level.

So the example meets the regular-pair formulation directly, not merely an aggregate discrepancy condition.

---

## 6. Failure of the counting conclusion

Every choice of one vertex from each class gives a canonical homomorphism \(P\to D_q\). Hence
\[
\operatorname{hom}(P,D_q)\ge m^{10},
\]
and therefore
\[
\frac{\operatorname{hom}(P,D_q)}{n^{10}}
\ge
\left(\frac mn\right)^{10}
=10^{-10}.
\tag{14}
\]

On the other hand, (9) gives
\[
\frac{\operatorname{hom}(P,G_q)}{n^{5/2}}=0.
\tag{15}
\]

Fix, for example,
\[
\varepsilon=\frac12\,10^{-10}.
\]
The normalized cut discrepancy in (13) can be made smaller than any prescribed positive constant, while (14)–(15) violate the proposed lower counting conclusion by at least \(10^{-10}\).

This proves that **the Petersen graph is not countable**.

---

## Scope and remaining questions

This supplies a negative answer for the Petersen case singled out in the catalog. The obstruction is not caused by high degrees, vertex collisions, irregular pairs, or insufficient edge density:

- the host graphs are \(C_3\)- and \(C_4\)-free;
- their maximum degrees are below \(\sqrt n\);
- every required pair is asymptotically sparse-superregular;
- the dense approximation has a fixed positive normalized Petersen count;
- the sparse graph has no Petersen homomorphism whatsoever.

The full characterization of countable graphs is not obtained, and the dodecahedral graph is not decided here. The argument above is complete as a mathematical construction; whether this particular twisted-polarity obstruction has previously appeared in the literature has not been independently checked.