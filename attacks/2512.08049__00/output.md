```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There is an explicit spectrally symmetric orientation of density 90/121, and a stability-plus-graphon argument shows that the upper bound 10/11 is not asymptotically attainable.",
  "would_publish": false,
  "caveats": "The exact value remains open and the improved upper bound is non-effective: it proves only that some absolute epsilon>0 exists."
}
```

# Statement of the partial result

Let
\[
\zeta=e^{\pi i/3}=\frac{1+i\sqrt3}{2}.
\]
For an orientation \(D\), write \(H(D)\) for its Hermitian adjacency matrix, with \(H_{uv}=\zeta\) or \(\bar\zeta\) according to the direction of the edge \(uv\). Reversing this convention conjugates \(H\) and does not affect any argument below.

I prove the following two improvements to the supplied bounds.

**Theorem.**
There is an absolute constant \(\varepsilon>0\) such that
\[
\boxed{\frac{90}{121}\leq \widehat\rho\leq \frac{10}{11}-\varepsilon.}
\]
The lower bound is explicit. The existence of \(\varepsilon\) is non-effective.

Numerically,
\[
\frac{90}{121}\approx0.743802,
\qquad
\frac{13}{18}\approx0.722222.
\]

The proof of the strict upper inequality uses only
\[
\operatorname{tr}H^3=\operatorname{tr}H^5=0,
\]
so it applies to a somewhat larger class than the spectrally symmetric orientations.

---

# 1. An improved construction

## 1.1 The orientation

For any positive integer \(k\), take four independent vertex classes
\[
A_1,A_2,A_3,B
\]
of respective sizes
\[
3k,3k,3k,2k.
\]
Put in every edge between distinct classes. Orient the edges by
\[
A_1\longrightarrow A_2\longrightarrow A_3\longrightarrow A_1
\]
and let
\[
B\longrightarrow A_i\qquad (i=1,2,3).
\]

Thus the underlying graph is the complete multipartite graph
\[
K_{3k,3k,3k,2k}.
\]

## 1.2 Spectral calculation

Let \(e_i\) be the normalized characteristic vector of the \(i\)-th class. Every vector whose coordinate sum is zero on each class lies in the kernel of \(H\). Consequently, all nonzero eigenvalues of \(H\) are those of the \(4\times4\) compression
\[
M=\bigl(\sqrt{n_i n_j}\,h_{ij}\bigr)_{i,j=1}^4,
\]
where \(n_1=n_2=n_3=3k,n_4=2k\) and \(h_{ij}\in\{\zeta,\bar\zeta\}\) is the gain between the corresponding classes.

For any triangle of classes, its contribution to \(\operatorname{tr}M^3/6\) is its class-size product multiplied by

- \(-1\) if the triangle is cyclic, because \(\Re(\zeta^3)=-1\);
- \(1/2\) if it is transitive.

The triangle \(A_1A_2A_3\) is cyclic and has weight
\[
(3k)^3=27k^3.
\]
The other three class-triangles are transitive, each with weight
\[
(3k)(3k)(2k)=18k^3.
\]
Hence
\[
\frac{\operatorname{tr}M^3}{6}
=-27k^3+3\cdot\frac{18k^3}{2}=0.
\]

Since \(M\) is a \(4\times4\) Hermitian matrix with zero trace, Newton's identities give
\[
\det(xI-M)
=x^4-\frac{\operatorname{tr}M^2}{2}x^2
-\frac{\operatorname{tr}M^3}{3}x+\det M.
\]
Thus \(\operatorname{tr}M^3=0\) makes the characteristic polynomial even, so the spectrum of \(M\), and therefore that of \(H\), is symmetric.

For completeness, one can calculate the spectrum explicitly. For \(k=1\),
\[
\operatorname{tr}M^2=90,\qquad \det M=324,
\]
and therefore
\[
\det(xI-M)=x^4-45x^2+324
=(x^2-36)(x^2-9).
\]
For general \(k\), the nonzero spectrum is
\[
\{6k,3k,-3k,-6k\},
\]
with \(11k-4\) additional zero eigenvalues.

## 1.3 Density

The number of vertices is \(11k\), and
\[
2|E|
=(11k)^2-\bigl(3(3k)^2+(2k)^2\bigr)
=121k^2-31k^2=90k^2.
\]
Thus
\[
\frac{2|E|}{|V|^2}=\frac{90}{121}.
\]
This proves
\[
\widehat\rho\geq\frac{90}{121}.
\]

## 1.4 Optimality within this four-class construction

More generally, suppose the cyclic classes have positive sizes \(a,b,c\), and the fourth, dominating class has size \(d\). The same trace calculation shows that spectral symmetry of the \(4\times4\) compression is equivalent to
\[
-abc+\frac d2(ab+ac+bc)=0,
\]
or
\[
d=\frac{2abc}{ab+ac+bc}
=\frac{2}{1/a+1/b+1/c}.
\]

Let \(s=a+b+c\). The harmonic-mean inequality gives
\[
d\leq \frac{2s}{9},
\]
and
\[
a^2+b^2+c^2\geq \frac{s^2}{3}.
\]
Writing \(r=d/s\leq2/9\), the missing-edge density satisfies
\[
\frac{a^2+b^2+c^2+d^2}{(a+b+c+d)^2}
\geq
\frac{1/3+r^2}{(1+r)^2}.
\]
The right side is decreasing for \(0\leq r\leq2/9\), so it is at least
\[
\frac{1/3+(2/9)^2}{(1+2/9)^2}
=\frac{31}{121}.
\]
Hence the maximum density in this family is \(90/121\), attained exactly when
\[
a=b=c,\qquad d=\frac{2a}{3}.
\]

---

# 2. The finite \(10/11\) identity and its stability terms

Let \(D\) be an orientation with underlying graph \(G\). Write

- \(n=|V(G)|\), \(m=|E(G)|\);
- \(d_v,d_v^+,d_v^-\) for the undirected, out-, and indegrees;
- \(b_v=d_v^+-d_v^-\);
- \(t\) for the number of underlying triangles;
- \(c\) for the number of cyclically oriented triangles.

A transitive triangle contributes \(3\) to \(\operatorname{tr}H^3\), while a cyclic triangle contributes \(-6\). Therefore
\[
\operatorname{tr}H^3=3(t-3c).
\]
In particular,
\[
\operatorname{tr}H^3=0\quad\Longrightarrow\quad t=3c.
\]

Define \(p\) to be the number of directed two-paths
\[
x\longrightarrow v\longrightarrow y
\]
whose endpoints \(x,y\) are nonadjacent.

Also define
\[
\ell=\sum_{uv\in E(G)}
\left(n-|N(u)\cup N(v)|\right).
\]
Every summand is nonnegative.

Set
\[
X=\sum_v d_v^2,\qquad B=\sum_v b_v^2.
\]

## Lemma 2.1: Exact deficit identity

If \(\operatorname{tr}H^3=0\), then
\[
\boxed{20mn=11X+9B+36p+20\ell.}
\]

### Proof

First,
\[
\sum_v d_v^+d_v^-
\]
counts one contribution at each vertex of a cyclic triangle, one at the middle vertex of a transitive triangle, and one for every directed two-path with nonadjacent endpoints. Hence
\[
\sum_vd_v^+d_v^-
=3c+(t-c)+p.
\]
Since \(t=3c\),
\[
\sum_vd_v^+d_v^-=\frac{5t}{3}+p.
\]
On the other hand,
\[
d_v^+d_v^-=\frac{d_v^2-b_v^2}{4}.
\]
Thus
\[
\frac{X-B}{4}=\frac{5t}{3}+p,
\]
or
\[
20t=3X-3B-12p. \tag{2.1}
\]

Next,
\[
3t=\sum_{uv\in E(G)}|N(u)\cap N(v)|.
\]
For every edge \(uv\),
\[
|N(u)\cap N(v)|
=d_u+d_v-n+\bigl(n-|N(u)\cup N(v)|\bigr).
\]
Summing over the edges gives
\[
3t=X-mn+\ell. \tag{2.2}
\]
Substitution of (2.1) into (2.2) yields
\[
20mn=11X+9B+36p+20\ell.
\]
\(\square\)

By Cauchy–Schwarz,
\[
X\geq \frac{(2m)^2}{n}.
\]
Consequently,
\[
20mn\geq\frac{44m^2}{n},
\]
and therefore
\[
\frac{2m}{n^2}\leq\frac{10}{11}.
\]

More importantly, if
\[
\rho=\frac{2m}{n^2},
\]
then the exact identity can be rewritten as
\[
\boxed{
\rho(10-11\rho)n^3
=
11\left(X-\frac{4m^2}{n}\right)
+9B+36p+20\ell.
} \tag{2.3}
\]

Thus a sequence whose densities tend to \(10/11\) must simultaneously satisfy:

1. its underlying degrees are asymptotically constant;
2. every vertex is asymptotically balanced between in- and outdegree;
3. it has \(o(n^3)\) directed two-paths with nonadjacent endpoints;
4. it has \(o(n^3)\) triples consisting of an edge and a common nonneighbor.

These conditions determine the limiting structure.

---

# 3. Equality-limit classification

Suppose, for contradiction, that there is a sequence \(D_j\) of spectrally symmetric orientations with
\[
\frac{2|E(D_j)|}{|V(D_j)|^2}\longrightarrow\frac{10}{11}.
\]
If the orders are bounded, a fixed example of density \(10/11\) occurs; taking its uniform blow-ups gives an unbounded sequence of the same density. We may therefore assume \(n_j\to\infty\).

Represent each \(D_j\) as a three-coloured graphon:

- \(P_j(x,y)\) is the indicator of the arc \(x\to y\);
- \(P_j(y,x)\) is the reverse direction;
- \(U_j(x,y)\) is the indicator of a nonedge.

Thus, off a null set,
\[
P_j(x,y)+P_j(y,x)+U_j(x,y)=1.
\]

By compactness for finite-coloured graphons, after relabelling and passing to a subsequence these converge in the coloured cut metric to kernels \(P,P^\top,U\). Put
\[
W=P+P^\top=1-U.
\]

All pattern densities used below are continuous under this convergence.

Equation (2.3) implies the following limit properties.

### Regularity
The degree function of \(W\) is
\[
d_W(x)=\frac{10}{11}
\quad\text{for almost every }x.
\]
Equivalently,
\[
d_U(x)=\frac1{11}
\quad\text{a.e.} \tag{3.1}
\]

### Vanishing of \(\ell\)
We have
\[
\int W(x,y)U(x,z)U(y,z)\,dx\,dy\,dz=0. \tag{3.2}
\]

### Vanishing of \(p\)
We have
\[
\int U(x,z)P(x,y)P(y,z)\,dx\,dy\,dz=0. \tag{3.3}
\]

### Balance
For almost every \(x\),
\[
\int\bigl(P(x,y)-P(y,x)\bigr)\,dy=0. \tag{3.4}
\]

## 3.1 The underlying graphon

For almost every \(z\), let
\[
S_z=\{x:U(x,z)>0\}.
\]
By (3.1) and \(U\leq1\),
\[
\mu(S_z)\geq\frac1{11}.
\]
Equation (3.2) says that for almost every \(x,y\in S_z\),
\[
U(x,y)=1.
\]
Consequently, for almost every \(x\in S_z\),
\[
d_U(x)\geq\mu(S_z).
\]
Together with \(d_U(x)=1/11\), this gives
\[
\mu(S_z)=\frac1{11}.
\]
Moreover, since \(U(z,\cdot)\) has integral \(1/11\) and support of measure \(1/11\),
\[
U(z,x)=1
\quad\text{for almost every }x\in S_z.
\]

If \(S_z\) and \(S_{z'}\) intersect in positive measure, the same argument shows that they agree modulo null sets. Hence the space is partitioned into exactly eleven sets
\[
A_1,\dots,A_{11}
\]
of measure \(1/11\), with
\[
U=1\quad\text{on }A_i\times A_i
\]
and
\[
U=0\quad\text{on }A_i\times A_j,\quad i\ne j.
\]

Thus \(W\) is the balanced complete \(11\)-partite graphon.

## 3.2 The orientation between the parts is uniform

Fix distinct \(i,j\). For \(y\in A_j\), put
\[
f_y(x)=P(x,y),\qquad x\in A_i.
\]
Since all cross-pairs are edges,
\[
P(y,z)=1-f_y(z)
\qquad(z\in A_i).
\]
Restricting (3.3) to \(x,z\in A_i\), \(y\in A_j\), gives
\[
\int_{A_j}
\left(\int_{A_i} f_y(x)\,dx\right)
\left(\frac1{11}-\int_{A_i}f_y(z)\,dz\right)
dy=0.
\]
Every integrand is nonnegative. Therefore, for almost every \(y\in A_j\), either

- \(f_y=0\) almost everywhere on \(A_i\), or
- \(f_y=1\) almost everywhere on \(A_i\).

Applying (3.3) with the nonadjacent endpoints in \(A_j\) shows that these two alternatives cannot both occur on sets of positive measure in \(A_j\). Hence every pair \(A_i,A_j\) is oriented uniformly in one direction.

The resulting orientation of the eleven parts is a tournament \(T\).

Finally, (3.4) says that every part has equal out- and indegree in \(T\). Hence \(T\) is a regular tournament:
\[
d_T^+(i)=d_T^-(i)=5
\qquad(i=1,\dots,11).
\]

Thus every hypothetical equality-limit is the balanced blow-up of a regular tournament on eleven vertices.

---

# 4. The fifth moment excludes the equality-limit

Let \(T\) be a regular tournament on eleven vertices, and let \(H_T\) be its sixth-root Hermitian adjacency matrix.

Let \(S\) be the real skew adjacency matrix,
\[
S_{ij}=
\begin{cases}
1,&i\to j,\\
-1,&j\to i.
\end{cases}
\]
Then
\[
H_T=\frac{J-I+i\sqrt3\,S}{2}.
\]
Set
\[
R=iS.
\]
The matrix \(R\) is Hermitian. Since \(T\) is regular,
\[
S\mathbf1=0.
\]
Therefore \(H_T\mathbf1=5\mathbf1\), while on \(\mathbf1^\perp\),
\[
H_T=\frac{-I+\sqrt3\,R}{2}.
\]

The eigenvalues of \(R\) occur in opposite pairs, so its odd traces vanish. Moreover,
\[
\operatorname{tr}R^2=110,
\]
because \(S\) has ten entries of modulus one in every row. Also,
\[
q:=\operatorname{tr}R^4=\operatorname{tr}S^4
\]
is an integer.

Expanding on \(\mathbf1^\perp\), which has dimension ten,
\[
\begin{aligned}
\operatorname{tr}H_T^5
&=5^5+\frac1{32}
\operatorname{tr}_{\mathbf1^\perp}(-I+\sqrt3R)^5\\
&=3125-\frac{10+30\operatorname{tr}R^2+45\operatorname{tr}R^4}{32}\\
&=3125-\frac{3310+45q}{32}.
\end{aligned}
\]
If this were zero, then
\[
45q=100000-3310=96690.
\]
But \(96690\) is not divisible by \(45\). Therefore
\[
\boxed{\operatorname{tr}H_T^5\ne0}
\]
for every regular tournament \(T\) on eleven vertices.

On the other hand, spectral symmetry of every \(D_j\) gives
\[
\operatorname{tr}H(D_j)^5=0.
\]
After normalization, this is the density of a complex-weighted directed \(5\)-cycle, and hence passes to the graphon limit. For the balanced blow-up of \(T\), that limit equals
\[
\frac{\operatorname{tr}H_T^5}{11^5},
\]
which is nonzero. This contradiction proves that no sequence of spectrally symmetric orientations can have densities tending to \(10/11\).

Consequently, there is an absolute \(\varepsilon>0\) such that
\[
\widehat\rho\leq\frac{10}{11}-\varepsilon.
\]

---

# Conclusion and remaining gap

The supplied interval can therefore be tightened to
\[
\boxed{\frac{90}{121}\leq\widehat\rho<\frac{10}{11}.}
\]

The lower construction is explicit and has spectrum
\[
\{6k,3k,0^{\,11k-4},-3k,-6k\}.
\]

The upper improvement is genuinely strict but non-effective: the graphon compactness argument does not produce a numerical value of \(\varepsilon\). Determining an explicit improved upper constant, or the exact value of \(\widehat\rho\), remains open.