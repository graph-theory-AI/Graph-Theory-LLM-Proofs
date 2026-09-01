```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For the joint regime 2 <= r <= s I prove Q(s,r) = (1+o(1))s uniformly, with exact equality when s is a prime power, and give explicit general two-parameter bounds.",
  "would_publish": false,
  "caveats": "The bounds do not match once r substantially exceeds s; even r=s^2 remains open up to an asymptotic factor of two."
}
```

## 1. Statement of the partial result

Let \(s,r\ge 2\). Write the vertices as \((i,a)\in [r]\times [s]\), where the sets
\[
C_i=\{(i,a):a\in[s]\}
\]
are the \(r\) cliques. A family of \(q\) proper colorings \(c_1,\dots,c_q\) is admissible if every two vertices in different cliques receive the same color in at least one coloring.

The following bounds hold:

\[
\boxed{
\max\left\{
s,\,
\left\lceil\log _2\!\left(r\left\lfloor\frac{s}{2}\right\rfloor\right)\right\rceil
\right\}
\le Q(s,r)
}
\tag{1}
\]

and, for every prime power \(n\ge s\),

\[
\boxed{
Q(s,r)\le
1+(n-1)\left\lceil\log_n r\right\rceil .
}
\tag{2}
\]

There is also an exact characterization of the minimum possible value:

\[
\boxed{
Q(s,r)=s
\quad\Longleftrightarrow\quad
\text{there exists an index-one }OA(s^2,r+1,s,2).
}
\tag{3}
\]

Consequently \(Q(s,r)=s\) implies \(r\le s\), while if \(s\) is a prime power then

\[
\boxed{Q(s,r)=s\qquad(2\le r\le s).}
\tag{4}
\]

For arbitrary \(s\), let \(p_s\) be the least prime at least \(s\). Since \(p_s=(1+o(1))s\), (1) and (2) give the uniform joint-growth asymptotic

\[
\boxed{
Q(s,r)=(1+o(1))s
\quad\text{uniformly for }2\le r\le s,\quad s\to\infty.
}
\tag{5}
\]

Thus (5) applies in particular whenever both \(r\) and \(s\) tend to infinity with \(r\le s\).

---

## 2. Lower bounds

### 2.1 The matching bound \(Q(s,r)\ge s\)

Fix two distinct cliques \(C_i,C_j\). In any one proper coloring, equality of colors between \(C_i\) and \(C_j\) defines a matching in the complete bipartite graph \(C_i\times C_j\), because no two vertices in either clique can have the same color.

Thus one coloring covers at most \(s\) of the \(s^2\) ordered cross-pairs. Since all \(s^2\) pairs must be covered,

\[
q s\ge s^2,
\]
and hence \(q\ge s\).

### 2.2 A rank bound

Let \(q\) admissible colorings be given and put
\[
m=\left\lfloor\frac{s}{2}\right\rfloor.
\]
In every clique \(C_i\), choose disjoint sets of vertices
\[
u_{i,1},\ldots,u_{i,m},
\qquad
v_{i,1},\ldots,v_{i,m}.
\]

For every coloring \(\ell\) and every color \(\gamma\) used in that coloring, introduce an indeterminate \(X_{\ell,\gamma}\). Over the corresponding rational-function field, define an \(rm\times rm\) matrix \(M\) by

\[
M_{(i,a),(j,b)}
 =
\prod_{\ell=1}^{q}
\left(
X_{\ell,c_\ell(u_{i,a})}
-
X_{\ell,c_\ell(v_{j,b})}
\right).
\tag{6}
\]

If \(i\ne j\), the vertices \(u_{i,a}\) and \(v_{j,b}\) are nonadjacent, so they receive the same color in at least one coloring. Therefore the corresponding factor in (6) is zero. Hence \(M\) is block diagonal, with one \(m\times m\) block \(B_i\) for each clique.

Each \(B_i\) is nonsingular as a polynomial matrix. Indeed, because all \(2m\) selected vertices in \(C_i\) receive distinct colors in every coloring, one may specialize their color variables so that

\[
(B_i)_{a,b}=(x_a-y_b)^q.
\]

The polynomials \((x-y_b)^q\), \(1\le b\le m\), are linearly independent: comparing the coefficients of
\[
x^q,x^{q-1},\ldots,x^{q-m+1}
\]
gives a Vandermonde matrix in \(y_1,\ldots,y_m\). Here \(m\le q+1\), since the preceding matching argument gives \(q\ge s\). It follows that
\[
\det[(x_a-y_b)^q]_{a,b=1}^m
\]
is not the zero polynomial. Thus every \(B_i\) has rank \(m\), and

\[
\operatorname{rank}M=rm.
\tag{7}
\]

On the other hand, expanding (6) gives

\[
M_{x,y}
=
\sum_{S\subseteq[q]}
(-1)^{q-|S|}
\left(\prod_{\ell\in S}
X_{\ell,c_\ell(u_x)}\right)
\left(\prod_{\ell\notin S}
X_{\ell,c_\ell(v_y)}\right).
\]

This expresses \(M\) as a sum of at most \(2^q\) rank-one matrices. Therefore

\[
rm\le \operatorname{rank}M\le 2^q.
\]

Hence
\[
q\ge
\left\lceil
\log_2\!\left(r\left\lfloor\frac{s}{2}\right\rfloor\right)
\right\rceil,
\]
proving (1).

---

## 3. The exact threshold \(Q(s,r)=s\)

Suppose first that \(q=s\). For two cliques \(C_i,C_j\), each of the \(s\) colorings induces a matching of size at most \(s\) between them. These \(s\) matchings cover all \(s^2\) cross-pairs. Equality must therefore hold throughout:

1. every matching is perfect;
2. no cross-pair is covered twice.

In particular, in each coloring all cliques use the same set of \(s\) colors.

For every coloring \(\ell\) and every one of its \(s\) colors \(\gamma\), form a row \((\ell,\gamma)\). This gives \(s^2\) rows. Construct an array with \(r+1\) columns as follows:

- column \(0\) contains \(\ell\);
- column \(i\), \(1\le i\le r\), contains the label \(a\in[s]\) of the unique vertex \((i,a)\) having color \(\gamma\) in coloring \(\ell\).

For column \(0\) and a clique column \(i\), every ordered pair \((\ell,a)\) occurs exactly once. For two clique columns \(i,j\), every ordered pair \((a,b)\) occurs exactly once, by the perfect and edge-disjoint matching conclusion above. Thus this is an index-one orthogonal array

\[
OA(s^2,r+1,s,2).
\]

Conversely, given such an orthogonal array, designate one column as the coloring-coordinate column. For each symbol \(\ell\), its \(s\) rows are assigned \(s\) distinct color names. In clique column \(i\), the entry in a row specifies which vertex receives that row's color in coloring \(\ell\). Orthogonality with the coordinate column makes every coloring proper, while orthogonality between two clique columns ensures that every cross-pair receives a common color. This proves (3).

### The orthogonal-array bound

An index-one \(OA(s^2,k,s,2)\) has at most \(s+1\) columns. Here is the standard linear-algebra proof.

For column \(j\) and symbol \(a\), let \(v_{j,a}\in\mathbb R^{s^2}\) be the indicator vector of rows in which column \(j\) equals \(a\), and put

\[
w_{j,a}=v_{j,a}-\frac1s\mathbf 1.
\]

For a fixed \(j\), the vectors \(w_{j,a}\) span an \((s-1)\)-dimensional space. Orthogonality of the array implies that these spaces are mutually orthogonal for different columns. They all lie in \(\mathbf1^\perp\), which has dimension \(s^2-1\). Therefore

\[
k(s-1)\le s^2-1=(s-1)(s+1),
\]
so \(k\le s+1\).

Applying this with \(k=r+1\) gives \(r\le s\) whenever \(Q(s,r)=s\).

If \(s\) is a prime power, an \(OA(s^2,s+1,s,2)\) is obtained over \(\mathbb F_s\): index rows by \((x,y)\in\mathbb F_s^2\), and use the columns

\[
A_\infty(x,y)=x,
\qquad
A_t(x,y)=y+tx\quad(t\in\mathbb F_s).
\]

Any two distinct columns give a bijection from \(\mathbb F_s^2\) to \(\mathbb F_s^2\). Taking any \(r+1\) columns proves (4).

---

## 4. Finite-field upper construction

Let \(n\ge s\) be a prime power and set

\[
k=\left\lceil\log_n r\right\rceil.
\]

Choose \(r\) distinct vectors
\[
x_i\in\mathbb F_n^k,\qquad i\in[r],
\]
and choose a set \(A\subseteq\mathbb F_n\) of size \(s\) to label the vertices of each clique.

Use the following set of coloring coordinates:

\[
\mathcal V
=
\{0\}
\cup
\{t e_j:1\le j\le k,\ t\in\mathbb F_n^\ast\}.
\]

Thus
\[
|\mathcal V|=1+k(n-1).
\]

For \(v\in\mathcal V\), define the coloring

\[
c_v(i,a)=a+\langle v,x_i\rangle,
\qquad a\in A.
\tag{8}
\]

For fixed \(i,v\), the map \(a\mapsto c_v(i,a)\) is injective, so (8) is proper.

Now take \(i\ne j\) and \(a,b\in A\). Put \(\delta=x_i-x_j\ne0\), and choose a coordinate \(h\) with \(\delta_h\ne0\). Equality of colors requires

\[
\langle v,\delta\rangle=b-a.
\]

If \(a=b\), take \(v=0\). Otherwise take

\[
v=t e_h,\qquad
t=\frac{b-a}{\delta_h}\in\mathbb F_n^\ast.
\]

Thus every cross-pair is covered, proving (2).

---

## 5. The joint regime \(r\le s\)

Let \(p_s\) be the least prime at least \(s\). For \(2\le r\le s\), the construction above has \(k=1\), hence

\[
Q(s,r)\le p_s.
\]

Together with \(Q(s,r)\ge s\),

\[
s\le Q(s,r)\le p_s.
\]

The prime number theorem implies \(p_s/s\to1\), proving

\[
Q(s,r)=(1+o(1))s
\]
uniformly over \(2\le r\le s\).

This gives a genuine simultaneous-growth answer, complementary to the fixed-\(s\), \(r\to\infty\) result in the source paper.

---

## 6. An obstruction inside the additive subclass

For context, consider the restricted case \(s=n\), where \(n\) is a prime power and every coloring has the form

\[
c_\ell(i,a)=a+h_\ell(i),\qquad a\in\mathbb F_n.
\]

If \(q=n+t\), then for every \(i\ne j\) the multiset

\[
\{h_\ell(i)-h_\ell(j):1\le\ell\le q\}
\]
must contain every element of \(\mathbb F_n\).

Let \(\chi\) be a nontrivial additive character and define

\[
z_i=(\chi(h_1(i)),\ldots,\chi(h_q(i)))\in\mathbb C^q.
\]

For \(i\ne j\), subtracting one occurrence of every field element gives

\[
|\langle z_i,z_j\rangle|\le t,
\qquad
\|z_i\|^2=q.
\]

Applying the rank/Frobenius bound to their Gram matrix yields, whenever \(t^2<q\),

\[
r\le \frac{q^2-t^2}{q-t^2}.
\tag{9}
\]

In particular, additive constructions with \(q=n+o(\sqrt n)\) have only \(r\le(1+o(1))n\) rows. This does not apply to arbitrary coloring systems, but it indicates that improving the finite-field construction near \(q=s\) requires genuinely different structure.

---

## 7. Remaining gap

The full joint-growth problem is not resolved. Already for a prime-power \(s\),

\[
s+1\le Q(s,s^2)\le 2s-1.
\]

The lower bound \(s+1\) follows because \(r>s\) rules out \(Q=s\), while the upper bound is (2) with \(n=s\) and \(k=2\). Thus even the leading constant along \(r=s^2\) remains unknown.

For much larger \(r\), (1) and (2) can be separated by a factor of order \(s/\log s\). The fixed-\(s\) theorem from the source paper eventually gives \(Q(s,r)\sim\log_2 r\), but its dependence on \(s\) is precisely what is missing in the simultaneous-growth regime. No novelty claim is made for the elementary bounds above; they do not constitute a full solution.