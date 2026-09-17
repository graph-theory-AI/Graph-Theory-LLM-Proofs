```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "At the natural q^n|S|^n scale, a polynomial removal lemma holds for coordinate-permutation-invariant colored sets whenever every nontrivial additive character takes at least three values on S.",
  "would_publish": false,
  "caveats": "Arbitrary colored sets remain untreated; the character condition is automatic under the stated size hypothesis in characteristic at least 5, but not always in characteristic 3."
}
```

# 1. Formulation and partial result

The quoted question does not specify the normalization. I use the following natural colored formulation.

Fix an odd prime power \(q\), a set \(S\subseteq\mathbb F_q\) containing \(0\), and put
\[
s=|S|,\qquad G=\mathbb F_q^n,\qquad N=q^n.
\]
For \(X,Y,Z\subseteq G\), let
\[
m_S(X,Y,Z)
=
\bigl|\{(x,d):d\in S^n,\ x\in X,\ x+d\in Y,\ x+2d\in Z\}\bigr|.
\]
Let \(\tau_S(X,Y,Z)\) be the minimum total number of vertices deleted from the three colored sets to eliminate all these triangles.

There are \(Ns^n\) triangles in the complete instance. Thus the desired relative removal statement is
\[
\tau_S(X,Y,Z)\ge \varepsilon N
\quad\Longrightarrow\quad
m_S(X,Y,Z)\ge \delta(q,S,\varepsilon)Ns^n,
\tag{RR}
\]
with \(\delta>0\) independent of \(n\).

The previous attempt’s objection to normalization by \(N^2\) is correct: for \(X=Y=Z=G\) and \(S\ne\mathbb F_q\),
\[
m_S=Ns^n=o(N^2),\qquad \tau_S=N,
\]
where the latter equality follows from the \(N\) disjoint zero-difference triangles. I do not use the previous slice-rank estimate below. Instead, I obtain a special case directly at the natural \(Ns^n\) scale.

A set in \(\mathbb F_q^n\) is **permutation-invariant** if it is invariant under every permutation of the coordinates.

## Theorem

Suppose
\[
\bigl|\{\chi(d):d\in S\}\bigr|\ge 3
\quad\text{for every nontrivial additive character }\chi
\text{ of }\mathbb F_q.
\tag{C}
\]
There are constants \(c>0\) and \(C>0\), depending only on \(q,S\), such that, for every \(n\) and every three permutation-invariant sets \(X,Y,Z\subseteq\mathbb F_q^n\),
\[
\boxed{\quad
\frac{m_S(X,Y,Z)}{Ns^n}
\ge
c\left(\frac{\tau_S(X,Y,Z)}{N}\right)^C.
\quad}
\tag{1}
\]

In particular, this is a polynomial relative removal lemma for this class of sets.

Condition (C) is automatic under the problem’s size hypothesis when the characteristic \(p\) is at least \(5\). Indeed, every fiber of a nontrivial additive character has size \(q/p\), so a set whose character image has at most two elements has size at most \(2q/p<q/2\).

For prime \(q\), condition (C) is simply \(|S|\ge3\). The proof below also gives an extension to sets invariant under permutations within any fixed number of coordinate blocks.

# 2. The lattice of possible joint types

For \(v\in\mathbb F_q^n\), its **type** records the number of occurrences of each field element. We omit the count of \(0\), since the counts sum to \(n\), and write
\[
t(v)\in\mathbb Z^{q-1}.
\]
Permutation-invariant sets are precisely unions of type classes.

Consider the one-coordinate restricted-triangle distribution
\[
(U,V,W)=(a,a+d,a+2d),
\]
where \(a\) is uniform in \(\mathbb F_q\) and \(d\) is independently uniform in \(S\). Each of \(U,V,W\) is uniform in \(\mathbb F_q\).

Encode its joint type contribution by
\[
\Psi(U,V,W)=
\left(
(\mathbf 1_{U=b})_{b\ne0},
(\mathbf 1_{V=b})_{b\ne0},
(\mathbf 1_{W=b})_{b\ne0}
\right)
\in\mathbb Z^{3(q-1)}.
\]
Let
\[
\Lambda=\operatorname{span}_{\mathbb Z}
\{\Psi(a,a+d,a+2d):a\in\mathbb F_q,\ d\in S\}.
\tag{2}
\]
The support contains the zero vector, from \(a=d=0\).

## Lemma 1: full rank

Under condition (C), \(\Lambda\) has full rank \(3(q-1)\).

### Proof

Suppose a real linear functional vanishes on every vector in (2). It can be written as
\[
A(a)+B(a+d)+C(a+2d)=0
\qquad(a\in\mathbb F_q,\ d\in S),
\tag{3}
\]
where \(A,B,C:\mathbb F_q\to\mathbb R\) satisfy
\[
A(0)=B(0)=C(0)=0.
\]

Taking the Fourier coefficient in \(a\) at a nontrivial additive character \(\chi\), we obtain
\[
\widehat A(\chi)
+\chi(d)\widehat B(\chi)
+\chi(d)^2\widehat C(\chi)=0
\qquad(d\in S).
\]
By (C), this quadratic polynomial vanishes at at least three distinct complex numbers. Therefore
\[
\widehat A(\chi)=\widehat B(\chi)=\widehat C(\chi)=0.
\]
This holds for every nontrivial character. Hence \(A,B,C\) are constant, and their values at \(0\) show that they are all zero.

Thus the support spans \(\mathbb R^{3(q-1)}\). Since it consists of integer vectors, \(\Lambda\) has full rank. ∎

Consequently,
\[
Q:=\mathbb Z^{3(q-1)}/\Lambda
\]
is a finite abelian group. Write \(K=|Q|\).

For a type \(t\in\mathbb Z^{q-1}\), define the three color-dependent labels
\[
\lambda_1(t)=[(t,0,0)],\qquad
\lambda_2(t)=[(0,t,0)],\qquad
\lambda_3(t)=[(0,0,t)]
\]
in \(Q\). Every restricted triangle satisfies
\[
\lambda_1(t(x))+\lambda_2(t(y))+\lambda_3(t(z))=0.
\tag{4}
\]

The important point is that \(Q\) is fixed independently of \(n\).

# 3. A uniform counting estimate for central types

We need a lower bound, not merely an asymptotic central limit theorem. The following elementary lattice estimate supplies it.

## Lemma 2: lattice local lower bound

Let a random vector \(T\) have fixed finite support
\[
\{w_1,\ldots,w_r\}\subseteq\mathbb Z^d,
\]
with positive probabilities \(p_1,\ldots,p_r\). Suppose \(w_1=0\), and the support spans \(\mathbb R^d\). Set
\[
\Lambda_T=\operatorname{span}_{\mathbb Z}\{w_1,\ldots,w_r\},
\qquad \mu=\mathbb ET.
\]

There are constants \(a,b,C_0>0\), depending only on this distribution, such that, whenever
\[
R\ge1,\qquad n\ge C_0(1+R^2),\qquad
v\in\Lambda_T,\qquad
\|v-n\mu\|_\infty\le R\sqrt n,
\]
independent copies \(T_1,\ldots,T_n\) satisfy
\[
\Pr(T_1+\cdots+T_n=v)
\ge
a\,n^{-d/2}e^{-bR^2}.
\tag{5}
\]

### Proof

Let \(A\) be the \((d+1)\times r\) integer matrix with columns
\[
(1,w_i).
\]
Its rank is \(d+1\). Since \(w_1=0\), the condition \(v\in\Lambda_T\) ensures that
\[
Ak=(n,v)
\tag{6}
\]
has an integer solution, without any further condition involving \(n\).

Choose a fixed real right inverse of \(A\). Starting from the real count vector \(np=(np_i)_i\), it gives a real solution \(y\) of (6) satisfying
\[
\|y-np\|_\infty=O(R\sqrt n).
\tag{7}
\]

The integer kernel of \(A\) spans its real kernel. Rounding coordinates in a fixed lattice basis therefore gives an integer solution \(k^{(0)}\) of (6) within a bounded distance of \(y\). Hence
\[
\|k^{(0)}-np\|_\infty=O(R\sqrt n+1).
\]

Put \(h=r-d-1\), the kernel dimension. Perturbing \(k^{(0)}\) along a fixed integer kernel basis, with each coefficient in an interval of length a sufficiently small constant times \(\sqrt n\), produces at least
\[
c_1 n^{h/2}
\]
distinct integer solutions \(k\) of (6). On increasing \(C_0\), all these solutions satisfy
\[
k_i\ge \frac12 np_i,\qquad
\|k-np\|_\infty=O(R\sqrt n).
\tag{8}
\]

For each such count vector, Stirling’s inequalities give
\[
\Pr(\text{count vector}=k)
=
\frac{n!}{\prod_i k_i!}\prod_i p_i^{k_i}
\ge
c_2 n^{-(r-1)/2}e^{-bR^2}.
\tag{9}
\]
For completeness, the exponential term follows from
\[
D(u\|p)\le \sum_i\frac{(u_i-p_i)^2}{p_i},
\qquad u_i=k_i/n,
\]
and (8), which imply \(nD(u\|p)=O(R^2)\).

The events corresponding to different count vectors are disjoint. Summing (9) over them proves (5), since
\[
\frac h2-\frac{r-1}{2}=-\frac d2.
\]
All constants used depend only on the fixed support and probabilities. ∎

## Applying the lemma to triangle types

Call a type \(t\) **\(R\)-central** if all its \(q\) counts, including the omitted count of \(0\), satisfy
\[
|t_a-n/q|\le R\sqrt n.
\tag{10}
\]
Let
\[
p_n(t)=\Pr(t(V)=t)
\]
for a uniform \(V\in\mathbb F_q^n\).

For \(n\ge C_0(1+R^2)\), with \(C_0\) enlarged if necessary, Stirling’s inequalities give
\[
p_n(t)\le C_1n^{-(q-1)/2}
\tag{11}
\]
for every \(R\)-central type. Indeed, all its counts are then at least \(n/(2q)\).

Generate a uniform restricted triangle in \(\mathbb F_q^n\) coordinatewise. Its joint type vector is a sum of \(n\) independent copies of \(\Psi(U,V,W)\). Lemmas 1 and 2 apply, and its mean is the vector all of whose entries are \(n/q\).

Combining (5) and (11), we obtain constants \(\kappa_0,\kappa_1,C_0>0\), depending only on \(q,S\), with the following property:

> If \(n\ge C_0(1+R^2)\), the three types \(t_1,t_2,t_3\) are \(R\)-central, and
> \[
> \lambda_1(t_1)+\lambda_2(t_2)+\lambda_3(t_3)=0,
> \]
> then
> \[
> \Pr\bigl(t(U)=t_1,t(V)=t_2,t(W)=t_3\bigr)
> \ge
> \kappa_0e^{-\kappa_1R^2}
> p_n(t_1)p_n(t_2)p_n(t_3).
> \tag{12}
> \]

Thus, among central types, the only obstruction to a uniform lower comparison with the product of the marginals is a constraint in the fixed finite group \(Q\).

# 4. Proof of the removal theorem

Suppose
\[
\tau_S(X,Y,Z)\ge\varepsilon N,
\qquad 0<\varepsilon\le1.
\]
Choose
\[
R^2=\frac12\log\frac{24q}{\varepsilon}.
\tag{13}
\]
This is at least \(1\).

For a uniform vector, the elementary binomial tail bound and a union bound over the \(q\) symbols give
\[
\Pr(\text{type is not \(R\)-central})
\le 2q e^{-2R^2}.
\]
Consequently, deleting all noncentral vertices from all three colors costs at most
\[
6q e^{-2R^2}N=\frac{\varepsilon N}{4}.
\tag{14}
\]

First suppose
\[
n\ge C_0(1+R^2).
\tag{15}
\]
Within each color, partition the remaining set according to its label \(\lambda_j(t)\in Q\). Delete every part of size less than
\[
\frac{\varepsilon N}{12K}.
\tag{16}
\]
There are at most \(K\) parts per color, so these further deletions cost less than \(\varepsilon N/4\).

The total deletion cost is less than \(\varepsilon N\). A restricted triangle therefore remains. Let \(r_1,r_2,r_3\in Q\) be its three labels. They satisfy
\[
r_1+r_2+r_3=0.
\]
Let \(X',Y',Z'\) be the corresponding remaining parts. Each has size at least \(\varepsilon N/(12K)\).

Every type in these parts is central, and every triple of their types satisfies the compatibility condition in (12). Moreover, the parts are unions of complete type classes. Summing (12) over their types therefore gives
\[
\begin{aligned}
\frac{m_S(X,Y,Z)}{Ns^n}
&\ge
\Pr(U\in X',V\in Y',W\in Z')\\
&\ge
\kappa_0e^{-\kappa_1R^2}
\frac{|X'|}{N}\frac{|Y'|}{N}\frac{|Z'|}{N}\\
&\ge
\kappa_0e^{-\kappa_1R^2}
\left(\frac{\varepsilon}{12K}\right)^3.
\end{aligned}
\]
Using (13), this is
\[
\frac{m_S(X,Y,Z)}{Ns^n}
\ge
\frac{\kappa_0}{(12K)^3(24q)^{\kappa_1/2}}
\,\varepsilon^{\,3+\kappa_1/2}.
\tag{17}
\]

It remains to cover the dimensions in which (15) fails. Since \(\tau_S>0\), at least one triangle exists, so
\[
\frac{m_S(X,Y,Z)}{Ns^n}\ge(qs)^{-n}.
\]
But now
\[
n<C_0\left(1+\frac12\log\frac{24q}{\varepsilon}\right),
\]
and hence
\[
\frac{m_S(X,Y,Z)}{Ns^n}
\ge
(qs)^{-C_0(1+\frac12\log(24q))}
\varepsilon^{\,\frac{C_0}{2}\log(qs)}.
\tag{18}
\]

Taking the smaller constant and the larger exponent from (17) and (18) proves a bound \(c\varepsilon^C\) in every dimension. Substituting \(\varepsilon=\tau_S/N\), with the case \(\tau_S=0\) trivial, proves (1). ∎

# 5. Two extensions

## 5.1 A fixed number of coordinate blocks

For each fixed \(b\), the theorem remains true if there is a common partition of the coordinates into at most \(b\) blocks, and \(X,Y,Z\) are invariant under permutations within each block. The constants may depend on \(b\).

Here are the modifications, including the treatment of short blocks. Set
\[
R^2=\frac12\log\frac{24bq}{\varepsilon}.
\]
Call a block large if its length is at least \(C_0(1+R^2)\). The total length \(t\) of the other blocks is at most
\[
bC_0(1+R^2).
\]
After deleting vertices with a noncentral type in any large block, classify each remaining vertex by:

* its exact word on the short blocks;
* its lattice label on each large block.

The number of classes per color is at most
\[
M\le q^tK^b\le q^{bC_0(1+R^2)}K^b.
\]
Delete classes smaller than \(\varepsilon N/(12M)\). As before, a triangle remains.

For a compatible triple of surviving classes, (12) applies independently on each large block. On the short blocks, the ratio of the probability of a fixed compatible triangle to the product of its three marginal probabilities is
\[
\frac{(qs)^{-t}}{q^{-3t}}=(q^2/s)^t\ge1.
\]
Taking \(\kappa_0e^{-\kappa_1R^2}\le1\), the same summation argument therefore gives
\[
\frac{m_S}{Ns^n}
\ge
\bigl(\kappa_0e^{-\kappa_1R^2}\bigr)^b
\left(\frac{\varepsilon}{12M}\right)^3.
\]
Since \(R^2=O_{q,b}(\log(1/\varepsilon))\), this is again \(c_b\varepsilon^{C_b}\). This argument also covers the case in which every block is short.

The number of blocks must remain bounded independently of \(n\).

## 5.2 Excluding zero differences and the one-set version

Let \(m_S^{-}\) and \(\tau_S^{-}\) refer only to triangles with \(d\ne0\). Then
\[
\tau_S\ge\tau_S^{-},\qquad m_S\le m_S^{-}+N.
\]
Thus \(\tau_S^{-}\ge\varepsilon N\) implies
\[
\frac{m_S^{-}}{Ns^n}\ge c\varepsilon^C-s^{-n}.
\tag{19}
\]
If \(s^{-n}\le c\varepsilon^C/2\), this gives the desired polynomial bound directly. Otherwise
\[
n=O_{q,S}(\log(1/\varepsilon)),
\]
and the existence of at least one nonzero-difference triangle gives a polynomial bound exactly as in (18). Therefore the theorem also holds with zero differences excluded, after changing its constants.

For a permutation-invariant single set \(A\), let \(\rho(A)\) be the minimum number of elements deleted to eliminate its nonconstant restricted progressions. Any colored cover in three copies of \(A\), upon taking the union of its underlying points, gives such an uncolored deletion set. Hence
\[
\tau_S^{-}(A,A,A)\ge\rho(A).
\]
The preceding result consequently gives a natural-scale polynomial removal lemma for permutation-invariant single sets as well.

# 6. What remains unresolved

This proves a dimension-independent, polynomial removal statement at the requested sparse scale, but only under symmetry assumptions.

There are two genuine limitations.

1. **Arbitrary subsets of type classes are not covered.**  
   The crucial estimate (12) counts complete type classes. For arbitrary \(X,Y,Z\), their intersections with those classes may have additional structure, and the joint triangle distribution inside a type class is not a product distribution. Consequently, the summation step in the removal proof is unavailable. Symmetrizing the sets is not justified: it need not preserve either the triangle count or the deletion distance.

2. **Condition (C) is additional in characteristic \(3\).**  
   For example, in \(\mathbb F_9\), let
   \[
   S=\{x:\operatorname{Tr}_{\mathbb F_9/\mathbb F_3}(x)\in\{0,1\}\}.
   \]
   Then \(0\in S\) and \(|S|=6>(9+1)/2\), but a nontrivial additive character takes only two values on \(S\). The full-rank type argument does not apply. This is a limitation of the proof, not a counterexample to removal.

In particular, I have neither proved (RR) for arbitrary colored sets nor constructed a counterexample to it. The general restricted-differences removal problem remains unresolved by this argument.