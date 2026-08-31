```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An M(K4) restriction forces a group coordinatization, so a prime alphabet forces an F_p coordinatization for all intersection-generated rank-three matroids, in particular for every p-entropic projective plane.",
  "would_publish": false,
  "caveats": "This does not handle arbitrary sparse rank-three matroids or higher rank, and novelty relative to the source paper has not been checked."
}
```

# Mathematical writeup

## 1. Setup and partial results

I use the standard normalization: a matroid \(M=(E,r)\) is \(q\)-entropic if there are random variables \((X_e:e\in E)\), each taking at most \(q\) values, such that

\[
\frac{H(X_S)}{\log q}=r(S)\qquad(S\subseteq E).
\]

Thus every nonloop variable is uniform on exactly \(q\) symbols. Loops may be represented by constants.

The conjecture asks whether, for prime \(p\), every \(p\)-entropic matroid is representable over \(\mathbb F_p\).

I prove the following partial results.

### Theorem A

1. Every rank-at-most-two \(p\)-entropic matroid is \(\mathbb F_p\)-representable.

2. A \(q\)-entropic representation of \(M(K_4)\) canonically induces a group of order \(q\). In particular, if \(q=p\) is prime, then, after independently relabeling the coordinate alphabets, the representation is the standard \(\mathbb F_p\)-linear representation of \(M(K_4)\).

3. The Fano matroid is \(q\)-entropic if and only if \(q\) is a power of \(2\). Consequently, an odd-prime-entropic matroid has no Fano minor.

4. Let \(p\) be prime. Every simple rank-three \(p\)-entropic matroid that is generated from an \(M(K_4)\) restriction by repeatedly intersecting two already generated rank-two flats is \(\mathbb F_p\)-representable.

5. In particular, if the matroid of a finite projective plane is \(p\)-entropic for prime \(p\), then the plane has order \(p\) and is isomorphic to \(\operatorname{PG}(2,p)\).

The fifth assertion rules out non-Desarguesian projective planes as a source of prime-alphabet counterexamples.

---

## 2. Uniform-code formulation and minors

Let \(B\) be a basis of a \(q\)-entropic matroid. Then

\[
H(X_B)=|B|\log q=\sum_{b\in B}H(X_b).
\]

Every \(X_b\) is therefore uniform on \(q\) symbols, and the variables in \(B\) are mutually independent. Moreover,

\[
H(X_E)=H(X_B),
\]

so every \(X_e\) is a deterministic function of \(X_B\).

More generally, if \(I\) is a basis of \(M|S\), then

\[
H(X_S)=H(X_I),
\]

and hence \(X_S\) is a deterministic function of \(X_I\). Since \(X_I\) is uniform on \(q^{r(S)}\) tuples and is itself part of \(X_S\), the projection \(X_S\) is uniform on exactly \(q^{r(S)}\) values.

Thus a \(q\)-entropic representation can equivalently be viewed as a uniform code \(C\subseteq Q^E\) satisfying

\[
|\pi_S(C)|=q^{r(S)}
\]

for every \(S\subseteq E\).

This also proves minor closure. Deletion is immediate. For contraction by a nonloop \(e\), condition on \(X_e=a\). For every \(S\subseteq E-\{e\}\), the uniform projection \(X_{S\cup\{e\}}\) has \(q^{r(S\cup e)}\) values, equally split among the \(q\) values of \(X_e\). Hence

\[
H(X_S\mid X_e=a)
 =\bigl(r(S\cup e)-1\bigr)\log q
 =r_{M/e}(S)\log q.
\]

So every minor of a \(q\)-entropic matroid is again \(q\)-entropic, after removing any loops that arise.

A three-element circuit is consequently represented by a binary quasigroup: if \(\{e,f,g\}\) is a circuit, then

\[
X_g=\mu(X_e,X_f),
\]

and each row and each column of \(\mu\) is a permutation of the alphabet.

---

## 3. Rank two

Let \(M\) be simple of rank two, with \(n\) elements. Pick a basis and identify its joint sample space with \(Q^2\), uniformly distributed.

For each \(e\in E\), let

\[
V_e=\{f(X_e):\mathbb E f(X_e)=0\}\subseteq L^2(Q^2).
\]

Because \(X_e\) is uniform on \(q\) symbols,

\[
\dim V_e=q-1.
\]

Distinct elements of a simple rank-two matroid form an independent pair, so \(X_e\) and \(X_f\) are independent for \(e\neq f\). It follows that \(V_e\perp V_f\). All the \(V_e\) lie in the codimension-one space of mean-zero functions on \(Q^2\), of dimension \(q^2-1\). Therefore

\[
n(q-1)\le q^2-1,
\]

and hence

\[
n\le q+1.
\]

For \(q=p\) prime, \(U_{2,n}\) is represented by any \(n\) points of the projective line over \(\mathbb F_p\). Loops and parallel elements are represented by zero and repeated columns. This proves Theorem A(1).

---

## 4. Group rigidity of \(M(K_4)\)

Label the six elements of \(M(K_4)\) as

\[
x,y,z,a,b,c
\]

so that its four triangles are

\[
\{x,y,a\},\qquad
\{x,z,b\},\qquad
\{y,z,c\},\qquad
\{a,b,c\}.
\]

Choose \(x,y,z\) as a basis. Write the corresponding independent uniform variables as \(X,Y,Z\). There are binary quasigroups \(f,g,h,k\) such that

\[
A=f(X,Y),\qquad
B=g(X,Z),\qquad
C=h(Y,Z)=k(A,B).
\]

Fix one alphabet symbol \(x_0\). By relabeling the alphabets of \(A\) and \(B\), assume

\[
f(x_0,y)=y,\qquad g(x_0,z)=z.
\]

Then the equation at \(x=x_0\) gives \(k(y,z)=h(y,z)\). For every \(x\), define permutations

\[
\alpha_x(y)=f(x,y),\qquad \beta_x(z)=g(x,z).
\]

The circuit \(\{a,b,c\}\) gives

\[
h(\alpha_x(y),\beta_x(z))=h(y,z)
\tag{1}
\]

for all \(x,y,z\).

Define

\[
\Gamma=\{(\alpha,\beta)\in\operatorname{Sym}(Q)^2:
h(\alpha(y),\beta(z))=h(y,z)\text{ for all }y,z\}.
\]

This is a group under componentwise composition.

### Claim 4.1
The action of \(\Gamma\) through its first coordinate is free.

Indeed, suppose \(\alpha(y_0)=y_0\). Then

\[
h(y_0,\beta(z))=h(y_0,z)
\]

for every \(z\). Since a row of a quasigroup table is injective, \(\beta=\mathrm{id}\). Then

\[
h(\alpha(y),z)=h(y,z)
\]

for all \(y,z\), and injectivity of each column gives \(\alpha=\mathrm{id}\).

Thus every orbit has size \(|\Gamma|\), so \(|\Gamma|\le q\). On the other hand, the \(q\) pairs \((\alpha_x,\beta_x)\) are distinct: for fixed \(y\), the map \(x\mapsto f(x,y)\) is a permutation. Hence

\[
|\Gamma|=q,
\]

and the pairs \((\alpha_x,\beta_x)\) exhaust \(\Gamma\). Both coordinate actions are regular.

Identify the alphabets of \(Y\) and \(Z\) with \(\Gamma\), so that both actions are left multiplication. Relabel \(X\) by the corresponding element of \(\Gamma\). Then

\[
A=XY,\qquad B=XZ.
\]

Equation (1) says that \(h\) is invariant under simultaneous left multiplication. Its orbits on \(\Gamma^2\) are indexed by \(Y^{-1}Z\). Because \(h\) is a quasigroup, its value is a bijective relabeling of \(Y^{-1}Z\). Relabeling \(C\), we obtain

\[
\boxed{A=XY,\qquad B=XZ,\qquad C=Y^{-1}Z.}
\tag{2}
\]

This proves that every \(q\)-entropic representation of \(M(K_4)\) is isotopic to a group representation over some group of order \(q\).

If \(q=p\) is prime, that group is cyclic. Writing its operation additively and identifying it with \(\mathbb F_p\), (2) becomes

\[
A=X+Y,\qquad B=X+Z,\qquad C=-Y+Z.
\tag{3}
\]

Thus the entire six-coordinate code is, up to coordinate relabelings, \(\mathbb F_p\)-linear.

---

## 5. Exact alphabet obstruction for the Fano matroid

Add a seventh element \(d\) to the above \(M(K_4)\), with the remaining three Fano lines

\[
\{x,c,d\},\qquad
\{y,b,d\},\qquad
\{z,a,d\}.
\]

There are quasigroups \(U,V,W\) such that

\[
D=U(X,C)=V(Y,B)=W(Z,A).
\tag{4}
\]

Use the group normal form (2). Put \(c=y^{-1}z\), so \(z=yc\). The first equality in (4) gives

\[
U(x,c)=V(y,xyc).
\tag{5}
\]

Setting \(y=1\), define the permutation

\[
\phi(t)=V(1,t).
\]

Then (5) yields

\[
U(x,c)=\phi(xc)
\]

and consequently

\[
V(y,xyc)=\phi(xc).
\tag{6}
\]

Fix \(y,t\), and in (6) impose \(xyc=t\), namely

\[
c=y^{-1}x^{-1}t.
\]

We obtain

\[
V(y,t)=\phi(xy^{-1}x^{-1}t)
\]

for every \(x\). Since \(\phi\) is injective, \(xy^{-1}x^{-1}\) is independent of \(x\). Taking \(x=1\) shows

\[
xy^{-1}x^{-1}=y^{-1}
\]

for all \(x,y\). Hence the group is abelian.

Now

\[
D=\phi(xy^{-1}z).
\]

The last equality in (4) gives

\[
W(z,xy)=\phi(xy^{-1}z).
\tag{7}
\]

Fix \(a=xy\) and \(z\). Since the group is abelian, \(x=ay^{-1}\), and the right side of (7) is

\[
\phi(ay^{-2}z).
\]

The left side is independent of \(y\). Injectivity of \(\phi\) therefore implies \(y^2=1\) for every \(y\). The group is an elementary abelian \(2\)-group, so

\[
q=2^m
\]

for some \(m\).

Conversely, for every \(q=2^m\), the usual representation of the Fano matroid over \(\mathbb F_q\) is \(q\)-entropic. Thus:

\[
\boxed{F_7\text{ is }q\text{-entropic if and only if }q\text{ is a power of }2.}
\]

By minor closure, no \(q\)-entropic matroid with \(q\) not a power of two can contain an \(F_7\) minor. In particular, no odd-prime-entropic matroid has an \(F_7\) minor.

---

## 6. Intersections of linear rank-two factors

The following elementary common-function lemma allows the \(M(K_4)\) normalization to propagate.

### Lemma 6.1
Let \(V\) be uniform on \(\mathbb F_p^3\). Let \(P,Q\) be distinct two-dimensional subspaces of \((\mathbb F_p^3)^*\). If a random variable \(T\) is simultaneously a function of the forms in \(P\) and a function of the forms in \(Q\), then \(T\) is a function of a nonzero form spanning \(P\cap Q\).

#### Proof

A function of the forms in \(P\) is invariant under translations by \(P^\perp\). Similarly, a function of the forms in \(Q\) is invariant under translations by \(Q^\perp\). Hence \(T\) is invariant under

\[
P^\perp+Q^\perp=(P\cap Q)^\perp.
\]

It therefore factors through the one-dimensional quotient defined by \(P\cap Q\). ∎

If additionally \(H(T)=\log p\), then \(T\) is a bijective relabeling of that common linear form.

### Definition
A simple rank-three matroid \(M\) is **quadrangle-generated** if it has a restriction \(N\cong M(K_4)\) and the remaining elements can be ordered \(e_1,\dots,e_m\) so that for every \(i\) there are earlier elements \(a,b,c,d\) with

\[
e_i\in\operatorname{cl}(a,b)\cap\operatorname{cl}(c,d),
\]

where \(\operatorname{cl}(a,b)\) and \(\operatorname{cl}(c,d)\) are distinct rank-two flats.

### Theorem 6.2
Every quadrangle-generated rank-three \(p\)-entropic matroid, for prime \(p\), is \(\mathbb F_p\)-representable.

#### Proof

Normalize the initial \(M(K_4)\) restriction using (3). Its six variables are now linear forms in three independent uniform variables

\[
V=(X,Y,Z)\in\mathbb F_p^3.
\]

Proceed inductively. Suppose all earlier elements have been relabeled as nonzero linear forms in \(V\). Let \(e_i\) lie on two distinct earlier-generated lines. Because

\[
r(e_i,a,b)=r(a,b)=2,
\]

the variable \(X_{e_i}\) is a function of \(X_a,X_b\), and hence of the corresponding two-dimensional space \(P\) of linear forms. It is similarly a function of a distinct two-dimensional space \(Q\).

By Lemma 6.1, \(X_{e_i}\) is a function of the unique one-dimensional intersection \(P\cap Q\). Since \(X_{e_i}\) is uniform on \(p\) symbols, this function is a bijection. Relabel \(X_{e_i}\) to be the corresponding linear form.

At the end, every variable is literally a linear form in \(X,Y,Z\). For every subset \(S\), its entropy is therefore the dimension of the span of the corresponding coefficient vectors. Since the entropy was prescribed to be \(r_M(S)\log p\), those vectors represent \(M\) over \(\mathbb F_p\). ∎

Parallel extensions and loops can be added by duplicating columns and adding zero columns.

---

## 7. Application to projective planes

### Corollary 7.1
Let \(\Pi\) be a finite projective plane whose matroid is \(p\)-entropic for a prime \(p\). Then \(\Pi\cong\operatorname{PG}(2,p)\).

#### Proof

Let \(\Pi\) have order \(n\). Every line has \(n+1\) points. Restricting the matroid to one line gives \(U_{2,n+1}\). The rank-two bound gives

\[
n+1\le p+1,
\]

so

\[
n\le p.
\tag{8}
\]

Choose four lines of \(\Pi\) with no three concurrent. Their six pairwise intersections form an \(M(K_4)\) restriction. Normalize it over \(\mathbb F_p\) using Section 4.

Among these six points are four with no three collinear, hence a projective frame. The closure of a projective frame under joining two known points and intersecting two known lines is all of \(\operatorname{PG}(2,p)\). For completeness, this can be seen explicitly as follows.

After a projective coordinate change, take the frame to be

\[
O=(0,0),\quad E=(1,0),\quad N=(0,1),\quad I=(1,1).
\]

Intersections of opposite sides produce the horizontal and vertical points at infinity. If \((a,0)\) and \((b,0)\) are constructed, lift \((b,0)\) vertically to \((b,1)\), draw through \((a,0)\) the line parallel to \(O(b,1)\), and intersect it with \(y=1\). This gives \((a+b,1)\), and vertical projection returns \((a+b,0)\). Starting with \(1\), repeated addition constructs every element of the prime field \(\mathbb F_p\). The diagonal \(OI\) copies these coordinates to the \(y\)-axis, and horizontal and vertical intersections construct every affine point \((a,b)\). Finally, intersections of parallel affine lines give all points at infinity.

Perform the same sequence of joins and intersections inside \(\Pi\). At each step, the intersection point is a common function of two distinct linear rank-two factors. Lemma 6.1 therefore forces its variable to be the corresponding \(\mathbb F_p\)-linear form. Distinct points of \(\operatorname{PG}(2,p)\) cannot collapse to one point of \(\Pi\), since two nonproportional linear forms have joint entropy \(2\log p\).

Consequently \(\Pi\) contains at least

\[
p^2+p+1
\]

distinct points. Since \(\Pi\) has \(n^2+n+1\) points,

\[
n^2+n+1\ge p^2+p+1,
\]

and hence \(n\ge p\). Together with (8), this gives \(n=p\).

The construction has now accounted for every point of \(\Pi\), and every coordinate variable is an \(\mathbb F_p\)-linear form. Thus its matroid is \(\operatorname{PG}(2,p)\). ∎

---

## 8. Remaining gap

The crucial limitation is the requirement that the relevant rank-two flats have an actual ground-set intersection point. In an arbitrary rank-three matroid, two lines may have total rank three but no listed point in their intersection. Entropically, their two rank-two tuples have mutual information \(\log p\), but mutual information of this size does not in general produce a deterministic \(p\)-valued common variable.

Thus the argument does not cover sparse configurations such as non-Pappus-type matroids, nor does it align the possibly different cyclic group structures arising in different fibers after contractions. Having an \(M(K_4)\) minor, rather than an \(M(K_4)\) restriction from which all elements are obtained by intersections, is not enough for the proof above.

Accordingly, the general conjecture for \(p=5,7,\ldots\) remains unresolved here. The main concrete progress is the group-coordinatization lemma and its consequences for Fano minors, intersection-generated rank-three matroids, and projective planes.