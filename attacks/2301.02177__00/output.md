```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "A weak finite-Grassmannian interpretation is trivially true, whereas a faithful stable interpretation requires an unspecified compatible family and already encounters a concrete obstruction for the graph K2.",
  "would_publish": false,
  "caveats": "The sign convention, ambient Grassmannian, stabilization, and meaning of subvariety are unspecified; the likely intended scheme-theoretic stable problem remains open."
}
```

# Mathematical writeup

## 1. Statement and conventions

Let \(G\) have \(n\) vertices. Its Kromatic symmetric function is, in the signless convention,

\[
\overline X_G=\sum_{\kappa} \prod_{v\in V(G)}\prod_{i\in\kappa(v)}x_i,
\]

where each \(\kappa(v)\) is a nonempty finite set of colors and adjacent vertices receive disjoint sets.

There are several inequivalent meanings of saying that a symmetric function “represents” a class in a Grassmannian. For the finite Grassmannian

\[
\operatorname{Gr}(k,k+w),
\]

the standard cohomological specialization is

\[
\rho^H_{k,w}(s_\lambda)=
\begin{cases}
[\Omega_\lambda],&\lambda\subseteq (w^k),\\
0,&\text{otherwise}.
\end{cases}
\]

Likewise, after choosing a Grothendieck-function convention, one has

\[
\rho^K_{k,w}(G_\lambda)=
\begin{cases}
[\mathcal O_{\Omega_\lambda}],&\lambda\subseteq (w^k),\\
0,&\text{otherwise}.
\end{cases}
\]

These maps have large kernels. Thus equality after applying \(\rho^H_{k,w}\) and \(\rho^K_{k,w}\) is much weaker than equality of stable symmetric functions.

There is also a sign issue. If \(\overline s_\lambda\) denotes the signless generating function of set-valued tableaux, then already

\[
\overline s_{(1)}=\sum_{m\geq 1}e_m,
\]

whereas the usual stable Grothendieck polynomial representing a Schubert structure sheaf is

\[
G_{(1)}=\sum_{m\geq 1}(-1)^{m-1}e_m.
\]

One normally passes from the signless series to algebraic \(K\)-theory by inserting the excess sign, equivalently by applying an appropriate \(x\mapsto -x\) transformation. The catalog statement does not specify this.

Finally, “subvariety” may mean:

- an integral reduced variety;
- a reduced but reducible closed subset;
- an arbitrary closed subscheme;
- an ind-subvariety or a compatible family of finite-stage subschemes.

These distinctions change the answer.

## 2. The leading-term compatibility is automatic

Every set-valued coloring has total degree at least \(n\). Equality occurs precisely when each vertex receives one color, in which case it is an ordinary proper coloring. Hence

\[
\bigl(\overline X_G\bigr)_{\deg n}=X_G. \tag{2.1}
\]

Suppose the source theorem gives

\[
\overline X_G=\sum_\lambda c_\lambda\,\overline s_\lambda,
\qquad c_\lambda\geq 0,
\]

where

\[
\overline s_\lambda=s_\lambda+\text{terms of degree \(>|\lambda|\)}.
\]

It follows inductively from (2.1) that

\[
c_\lambda=0\quad\text{for }|\lambda|<n,
\]

and

\[
c_\lambda=[s_\lambda]X_G\quad\text{for }|\lambda|=n. \tag{2.2}
\]

This is also the geometric compatibility one expects from the codimension filtration on \(K^0\): if \(Y\) is pure of codimension \(n\), then the leading associated-graded term of \([\mathcal O_Y]\) is the fundamental cycle \([Y]\). Thus, once the \(K\)-class is realized by a structure sheaf, the cohomological condition is essentially forced by (2.1).

The real problem is therefore structure-sheaf representability, not compatibility of the two leading classes.

## 3. The graph \(K_2\) shows that no finite Grassmannian can retain the full stable class

The edge \(K_2\) is claw-free and is the incomparability graph of a two-element antichain.

For a fixed set of \(m\) colors, a set-valued proper coloring of \(K_2\) is an ordered partition of that set into two nonempty parts. There are \(2^m-2\) such partitions. Therefore

\[
\overline X_{K_2}
=\sum_{m\geq 2}(2^m-2)e_m. \tag{3.1}
\]

For a column of length \(r\), a set-valued tableau using a prescribed ordered \(m\)-element set is obtained by cutting that ordered set into \(r\) nonempty consecutive blocks. Hence

\[
\overline s_{(1^r)}
=\sum_{m\geq r}\binom{m-1}{r-1}e_m. \tag{3.2}
\]

Combining (3.1) and (3.2),

\[
\begin{aligned}
2\sum_{r\geq 2}\overline s_{(1^r)}
&=\sum_{m\geq 2}
2\left(\sum_{r=2}^{m}\binom{m-1}{r-1}\right)e_m\\
&=\sum_{m\geq 2}2(2^{m-1}-1)e_m\\
&=\overline X_{K_2}.
\end{aligned} \tag{3.3}
\]

Thus

\[
\boxed{\overline X_{K_2}=2\sum_{r\geq 2}\overline s_{(1^r)}}. \tag{3.4}
\]

In particular, its Grothendieck support contains columns of arbitrarily large length. No finite rectangle \((w^k)\) contains all of these partitions.

Consequently:

- If “represented” means equality after applying a finite-stage quotient \(\rho^K_{k,w}\), then all terms with \(r>k\) are simply discarded.
- If it means that one finite Grassmannian should retain the complete stable Schubert expansion, then the demand is impossible already for \(K_2\).
- A faithful interpretation must instead involve an ind-Grassmannian or a compatible family as \(k,w\to\infty\).

The catalog statement does not say which of these is intended.

## 4. Under the weakest quotient interpretation, the problem is trivial

There is a uniform point construction.

Let

\[
a_G=[s_{(1^n)}]X_G.
\]

The standard power-sum inclusion-exclusion formula is

\[
X_G=\sum_{A\subseteq E(G)}(-1)^{|A|}p_{\lambda(A)},
\]

where \(\lambda(A)\) is the partition of \(n\) formed by the component sizes of \((V,A)\). Since the sign character has value

\[
\chi^{(1^n)}(\lambda)=(-1)^{n-\ell(\lambda)},
\]

we obtain

\[
a_G
=\sum_{A\subseteq E(G)}(-1)^{|A|+n-c(A)}
=(-1)^n\chi_G(-1). \tag{4.1}
\]

This is the number of acyclic orientations of \(G\), and in particular \(a_G>0\).

Now take

\[
\operatorname{Gr}(n,n+1)\cong \mathbf P^n.
\]

Its Schubert rectangle is the column \((1^n)\). Since \(X_G\) is homogeneous of degree \(n\),

\[
\rho^H_{n,1}(X_G)=a_G[\mathrm{pt}]. \tag{4.2}
\]

By (2.2), every Grothendieck term of \(\overline X_G\) has size at least \(n\), and the only partition of size at least \(n\) fitting inside \((1^n)\) is \((1^n)\) itself. Hence, under either standard sign convention—the excess is zero for this term—

\[
\rho^K_{n,1}(\overline X_G)=a_G[\mathcal O_{\mathrm{pt}}]. \tag{4.3}
\]

Choose \(a_G\) distinct points \(Z\subset \mathbf P^n\). Then

\[
[Z]=a_G[\mathrm{pt}],
\qquad
[\mathcal O_Z]=a_G[\mathcal O_{\mathrm{pt}}].
\]

Thus the catalog statement is true for every graph, not merely claw-free incomparability graphs, if:

1. one may choose any finite Grassmannian quotient;
2. a reduced reducible zero-dimensional subvariety is allowed; and
3. “represented” means equality only after that quotient.

If irreducibility is required, a reduced zero-dimensional variety has length one, so this argument fails whenever \(a_G>1\). If arbitrary schemes are allowed, one may instead take a length-\(a_G\) curvilinear scheme supported at one point.

This construction clearly destroys nearly all the information in \(X_G\) and \(\overline X_G\), so it is almost certainly not the intended answer. It demonstrates, however, that the informal statement is not a well-defined conjecture.

## 5. A concrete obstruction to natural integral realizations

The same graph \(K_2\) gives a nontrivial obstruction if one asks for an integral geometric representative.

After finite specialization to \(\operatorname{Gr}(k,N)\), (3.4) gives either

\[
\alpha_k^+
=2\sum_{r=2}^{k}[\mathcal O_{\Omega_{(1^r)}}] \tag{5.1}
\]

if the barred basis is declared directly to represent Schubert structure sheaves, or

\[
\alpha_k^-
=2\sum_{r=2}^{k}(-1)^{r-2}[\mathcal O_{\Omega_{(1^r)}}] \tag{5.2}
\]

after the usual excess-sign specialization to algebraic \(K\)-theory. Both have leading cohomology class \(2\sigma_{11}=X_{K_2}\).

### Proposition

Under either convention (5.1) or (5.2):

1. For \(k\geq 3\), no integral subvariety \(Y\subseteq\operatorname{Gr}(k,N)\) can have
   \[
   [Y]=2\sigma_{11},
   \qquad
   [\mathcal O_Y]=\alpha_k^\pm.
   \]
2. For \(k=2\), no normal integral such \(Y\) exists.

### Proof for \(k\geq 3\)

Let \(X=\operatorname{Gr}(k,N)\), of dimension \(D\). Choose subspaces

\[
A\subset B\subset \mathbf C^N,
\qquad
\dim A=k-3,\quad \dim B=k+1.
\]

Then

\[
Z=\{V:A\subseteq V\subseteq B\}
\cong \operatorname{Gr}(3,4)\cong\mathbf P^3.
\]

Take a general translate of \(Z\), and let \(C=Y\cap Z\).

An integral variety is Cohen–Macaulay at all codimension-one points, so the non-Cohen–Macaulay locus of \(Y\) has codimension at least two in \(Y\), hence dimension at most \(D-4\). A general three-dimensional translate \(Z\) avoids that locus. The intersection has expected dimension one. Along \(C\), the regular sequence defining \(Z\) is regular on \(\mathcal O_Y\), so the intersection is Tor-independent and Cohen–Macaulay. Generic transversality makes it generically reduced; a generically reduced Cohen–Macaulay curve is reduced.

Restriction to \(Z\cong\mathbf P^3\) sends

\[
[\mathcal O_{\Omega_{(1^2)}}]\longmapsto[\mathcal O_L],
\qquad
[\mathcal O_{\Omega_{(1^3)}}]\longmapsto[\mathcal O_p],
\]

where \(L\) is a line and \(p\) a point; all longer columns vanish. Therefore

\[
[\mathcal O_C]
=
\begin{cases}
2[\mathcal O_L]+2[\mathcal O_p],&\text{for (5.1)},\\
2[\mathcal O_L]-2[\mathcal O_p],&\text{for (5.2)}.
\end{cases}
\]

Hence

\[
\chi(\mathcal O_C)=4\quad\text{or}\quad 0. \tag{5.3}
\]

On the other hand, \([C]=2h^2\), so \(C\subset\mathbf P^3\) is a reduced curve of degree two. Every such curve is one of:

- an irreducible plane conic, with \(\chi(\mathcal O_C)=1\);
- two intersecting lines, with \(\chi(\mathcal O_C)=1\);
- two skew lines, with \(\chi(\mathcal O_C)=2\).

None has Euler characteristic \(0\) or \(4\), contradicting (5.3).

### Proof for \(k=2\)

If \(N=3\), then \(\operatorname{Gr}(2,3)\cong\mathbf P^2\), and an integral zero-dimensional subvariety has cycle class \([\mathrm{pt}]\), not \(2[\mathrm{pt}]\).

Suppose \(N\geq 4\) and \(Y\) is normal. Take a general

\[
Z\cong\operatorname{Gr}(2,4),
\]

which is a smooth four-dimensional quadric \(Q^4\subset\mathbf P^5\). Normality implies Serre's \(S_2\) condition, so the non-Cohen–Macaulay locus of \(Y\) has codimension at least three and is avoided by a general \(Z\). As above,

\[
C=Y\cap Z
\]

is a reduced Cohen–Macaulay surface satisfying

\[
[C]=2\sigma_{11},
\qquad
[\mathcal O_C]=2[\mathcal O_A],
\]

where \(A\cong\mathbf P^2\) is a maximal plane in one ruling of \(Q^4\).

The surface \(C\) has Plücker degree two.

- If \(C\) is irreducible, it is a quadric surface in its linear span \(\mathbf P^3\). Thus \(C=Q^4\cap\mathbf P^3\), whose class is
  \[
  h^2=\sigma_2+\sigma_{11},
  \]
  not \(2\sigma_{11}\).
- If \(C\) is reducible, it is a union of two planes. To have class \(2\sigma_{11}\), both planes lie in the same ruling. Two distinct such planes meet in one point, and therefore
  \[
  [\mathcal O_C]
  =2[\mathcal O_A]-[\mathcal O_p]
  \neq 2[\mathcal O_A].
  \]

This is again a contradiction. ∎

Thus a faithful stable construction for \(K_2\), if one exists in schemes, cannot consist of integral varieties at all ranks. At rank two it would have to be nonnormal or reducible/nonreduced, and at rank at least three integrality itself is impossible under the standard finite-stage interpretations.

## 6. A genuine positive special case: edgeless graphs

There is a natural construction for edgeless graphs that does not collapse everything to points.

Let \(E_n\) be the edgeless graph on \(n\) vertices. Then

\[
X_{E_n}=s_1^n
\]

and, because the set-valued choices at different vertices are independent,

\[
\overline X_{E_n}=\overline s_1^{\,n}.
\]

Choose a Grassmannian of dimension greater than \(n\), and let \(D_1,\dots,D_n\) be general Plücker hyperplane sections, equivalently general translates of the Schubert divisor. Their intersection

\[
Y=D_1\cap\cdots\cap D_n
\]

is a regular complete intersection; for a sufficiently large Grassmannian it may be chosen smooth and irreducible.

In cohomology,

\[
[Y]=[D_1]\cdots[D_n]=\sigma_1^n=\rho^H(X_{E_n}).
\]

The Koszul resolution gives

\[
[\mathcal O_Y]
=\prod_{i=1}^n[\mathcal O_{D_i}]
=\rho^K(\overline s_1^{\,n})
=\rho^K(\overline X_{E_n}),
\]

after the standard sign conversion if the barred functions are defined signlessly.

More generally, if suitable local-complete-intersection representatives are known for two graphs \(G_1,G_2\), then general translates intersect Tor-independently, and their intersection represents the product classes corresponding to \(G_1\sqcup G_2\), since both \(X_G\) and \(\overline X_G\) are multiplicative under disjoint union.

## 7. What remains open

A precise nontrivial version should specify at least:

1. the field, presumably \(\mathbf C\);
2. the exact sign or \(\beta=-1\) specialization from the signless Kromatic series to algebraic \(K\)-theory;
3. whether one asks for one finite-stage quotient, for every sufficiently large rectangle, or for a compatible ind-Grassmannian family;
4. whether the object must be integral, normal, Cohen–Macaulay, reduced, or merely a closed subscheme;
5. what compatibility under Grassmannian stabilization is required.

The weak single-quotient version has the point construction above. A faithful finite-stage version is impossible because of the unbounded expansion (3.4). A stable version using integral varieties is obstructed by \(K_2\). What remains genuinely open is a formulation permitting suitably singular, reducible, or nonreduced compatible schemes—or perhaps derived schemes—whose finite-stage structure-sheaf classes recover all truncations of \(\overline X_G\).