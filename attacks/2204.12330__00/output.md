```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "The proposed group of finitely supported permutations is a witness, because it is elementwise tame under a coset-convex order while its alternating subgroups force arbitrarily large translation grids under every order.",
  "would_publish": true,
  "caveats": "This uses the source paper's proved equivalence between permutation-width boundedness and exclusion of interval grids; constants are nonoptimal and literature priority is unchecked."
}
```

# Statement

Let
\[
G=\operatorname{Sym}_{\mathrm{fin}}(\mathbb Z)
\]
be the group of finitely supported permutations of \(\mathbb Z\). Then, in the terminology of *Twin-width VII: groups*,

\[
\operatorname{tww}(G)<\infty
\qquad\text{but}\qquad
\operatorname{utww}(G)=\infty.
\]

Thus uniform twin-width is strictly stronger than ordinary twin-width. In fact, the same conclusion holds for the finitary alternating group.

The proof gives the following more general criterion.

> **Theorem.** Let \(G\) be a countable locally finite group. Suppose that \(G\) contains finite subgroups \(H_i\) whose least dimension \(D(H_i)\) of a nontrivial complex representation tends to infinity. Then \(G\) has finite ordinary twin-width and infinite uniform twin-width.

The alternating subgroups \(A_n\leq \operatorname{Sym}_{\mathrm{fin}}(\mathbb Z)\) satisfy \(D(A_n)\to\infty\).

---

# 1. Translation grids

Fix a linear order \(\prec\) on a group \(G\). For \(g\in G\), let \(L_g:x\mapsto gx\), and consider its permutation matrix, with both rows and columns ordered by \(\prec\).

An \(r\)-grid in \(L_g\) consists of ordered convex row sets
\[
I_1\prec I_2\prec\cdots\prec I_r
\]
and ordered convex column sets
\[
J_1\prec J_2\prec\cdots\prec J_r
\]
such that
\[
L_g(I_i)\cap J_j\neq\varnothing
\qquad\text{for every }i,j\in[r].
\]

The source paper's pattern characterization implies:

* ordinary finite twin-width is equivalent to the existence of an order for which every fixed translation has finite grid width, with the bound allowed to depend on the translating element;
* finite uniform twin-width requires one finite bound valid for all translations.

The lower bound below is stronger than merely producing a nonempty grid: every cell will contain many entries of the permutation matrix. Thus it also gives the mixed-grid or rank-grid obstruction in equivalent formulations of permutation width.

Left and right multiplication are interchangeable throughout.

---

# 2. Every countable locally finite group has finite ordinary twin-width

Let
\[
G_0<G_1<G_2<\cdots,\qquad G=\bigcup_mG_m,
\]
where every \(G_m\) is finite. Such a chain exists for every countable locally finite group.

We construct an order on \(G\) recursively. Having ordered \(G_m\), partition \(G_{m+1}\) into right cosets \(G_mt\). Put \(G_m\) first, order the other cosets arbitrarily, and transport the existing order on \(G_m\) to every \(G_mt\) by
\[
x\longmapsto xt.
\]
The resulting orders extend one another. In the union order, every right coset \(G_mx\) is convex.

Fix \(g\in G_m\). Left multiplication by \(g\) preserves every right coset \(G_mx\) setwise. Hence \(L_g\) is a direct sum, along convex blocks, of permutations of blocks of size
\[
s=|G_m|.
\]

We claim that \(L_g\) has no \((s+1)\)-grid. More generally, suppose it has an \(r\)-grid. Choose

* \(x\in I_1\) with \(gx\in J_r\), and
* \(y\in I_r\) with \(gy\in J_1\).

Then \(x\prec y\) but \(gy\prec gx\). Points in distinct convex \(G_m\)-cosets retain their relative block order under \(L_g\), so \(x\) and \(y\) must lie in the same \(G_m\)-coset \(B\). By convexity, \(B\) meets each of the ordered intervals
\[
I_1,I_2,\ldots,I_r.
\]
Consequently \(|B|\geq r\), and hence \(r\leq s\).

Thus every \(g\) has finite grid width, bounded by \(|G_m|\) for any \(m\) containing \(g\). This proves finite ordinary twin-width.

Equivalently, for any finite set \(F\subseteq G\), choose \(m\) with \(F\subseteq G_m\); all translations by elements of \(F\) have a common finite bound depending on \(m\). In the Cayley-graph formulation, the Cayley graph associated with \(F\) has components of size at most \(|\langle F\rangle|\).

In particular,
\[
\operatorname{tww}\bigl(\operatorname{Sym}_{\mathrm{fin}}(\mathbb Z)\bigr)<\infty.
\]

---

# 3. A mixing lemma for finite quasirandom groups

For a finite group \(H\), let \(D(H)\) be the smallest dimension of a nontrivial irreducible complex representation of \(H\).

## Lemma

Let \(H\) be a finite group of order \(N\), and let \(D=D(H)\). Suppose
\[
A_1,\ldots,A_r,\qquad B_1,\ldots,B_r
\]
are two partitions of \(H\) such that
\[
|A_i|,|B_j|\geq \frac{N}{2r}
\]
for every \(i,j\). If
\[
D>16r^4,
\]
then there is \(h\in H\) such that, simultaneously for all \(i,j\),
\[
|hA_i\cap B_j|\geq \frac{N}{8r^2}.
\]

### Proof

Use normalized inner product on \(\ell^2(H)\):
\[
\langle f_1,f_2\rangle=\frac1N\sum_{x\in H}f_1(x)\overline{f_2(x)}.
\]

Let \(\lambda\) be the left regular representation. If \(u,v\) are orthogonal to the constant functions, Schur orthogonality gives
\[
\mathbb E_{h\in H}\left|\langle\lambda(h)u,v\rangle\right|^2
 \leq \frac{\|u\|_2^2\|v\|_2^2}{D}.
\tag{1}
\]
Indeed, decompose the mean-zero regular representation into nontrivial isotypic components. On a \(d\)-dimensional irreducible isotype, Schur orthogonality bounds the corresponding second moment by \(1/d\) times the product of the squared norms; every such \(d\) is at least \(D\).

For \(A,B\subseteq H\), put
\[
\alpha=\frac{|A|}{N},\qquad \beta=\frac{|B|}{N},
\]
and
\[
u_A=1_A-\alpha,\qquad u_B=1_B-\beta.
\]
Then
\[
\frac{|hA\cap B|}{N}-\alpha\beta
  =\langle\lambda(h)u_A,u_B\rangle.
\]
By (1),
\[
\mathbb E_h
\left(
\frac{|hA\cap B|}{N}-\alpha\beta
\right)^2
\leq \frac{\alpha(1-\alpha)\beta(1-\beta)}D
\leq \frac{\alpha\beta}{D}.
\]
Therefore Chebyshev's inequality gives
\[
\Pr_h\left[
|hA\cap B|<\frac12N\alpha\beta
\right]
\leq \frac4{D\alpha\beta}.
\tag{2}
\]

Apply (2) to \(A_i,B_j\). Since \(\alpha_i,\beta_j\geq 1/(2r)\),
\[
\Pr_h\left[
|hA_i\cap B_j|<\frac{N}{8r^2}
\right]
\leq \frac{16r^2}{D}.
\]
A union bound over the \(r^2\) pairs gives total failure probability at most
\[
\frac{16r^4}{D}<1.
\]
Hence some \(h\) satisfies all the desired inequalities. ∎

## Consequence for ordered regular actions

Give the row and column copies of \(H\) arbitrary linear orders, and divide each into \(r\) consecutive intervals of sizes differing by at most one. If \(N\geq2r\), these intervals satisfy the size hypothesis of the lemma. Therefore, when \(D(H)>16r^4\), some left translation has an \(r\times r\) grid.

Moreover, if \(N/(8r^2)\geq r\), every cell contains at least \(r\) ones. Since these ones occupy distinct rows and columns, every cell has matrix rank at least \(r\) over any field. Thus this is also a rank-\(r\) division and, for \(r\geq2\), a mixed \(r\)-grid.

In particular, if
\[
U(H)=\min_{\prec}\max_{h\in H}\operatorname{grid}_{\prec}(L_h),
\]
then
\[
U(H)=\Omega\!\left(D(H)^{1/4}\right).
\tag{3}
\]

---

# 4. Alternating groups have unbounded \(D(H)\)

For \(n\geq5\), \(A_n\) is simple. Set
\[
q=\left\lfloor\frac n4\right\rfloor.
\]
Inside \(A_n\), consider the commuting double transpositions
\[
e_i=(4i-3\;\;4i-2)(4i-1\;\;4i),
\qquad 1\leq i\leq q.
\]
They generate
\[
E=\langle e_1,\ldots,e_q\rangle\cong (C_2)^q.
\]

Let \(\rho\) be a nontrivial irreducible complex representation of \(A_n\). Since \(A_n\) is simple, \(\ker\rho=1\), so \(\rho|_E\) is faithful. The commuting involutions \(\rho(e_i)\) are simultaneously diagonalizable with eigenvalues in \(\{\pm1\}\). Hence a \(d\)-dimensional faithful representation embeds \(E\) in \(\{\pm1\}^d\), forcing
\[
2^q\leq2^d.
\]
Thus
\[
D(A_n)\geq \left\lfloor\frac n4\right\rfloor.
\tag{4}
\]

Combining (3) and (4), the uniform translation-grid width of \(A_n\) grows at least on the order of \(n^{1/4}\).

---

# 5. Infinite uniform twin-width of the finitary symmetric group

Let
\[
G=\operatorname{Sym}_{\mathrm{fin}}(\mathbb Z).
\]
For every \(n\), \(G\) contains a subgroup \(H_n\cong A_n\), acting on an \(n\)-element subset of \(\mathbb Z\).

Fix an arbitrary candidate order \(\prec\) on \(G\), and fix \(r\). Choose \(n\) sufficiently large that
\[
\left\lfloor\frac n4\right\rfloor>16r^4
\]
and
\[
\frac{|A_n|}{8r^2}\geq r.
\]
Restrict \(\prec\) to \(H_n\). The preceding lemma supplies \(h\in H_n\) such that the permutation matrix of \(L_h|_{H_n}\) has an \(r\times r\) interval division with at least \(r\) ones in every cell.

This grid is also present in the full permutation \(L_h:G\to G\). Indeed, consecutive intervals in the induced order on the finite set \(H_n\) can be extended to convex intervals of \(G\) by placing cuts after the relevant elements of \(H_n\). The selected entries remain in the corresponding cells. Equivalently, the grid is a permutation pattern of the restriction, and permutation-grid width is hereditary under restriction.

Since \(r\) was arbitrary, for every order \(\prec\) on \(G\),
\[
\sup_{g\in G}\operatorname{grid}_{\prec}(L_g)=\infty.
\]
By the source paper's grid characterization,
\[
\operatorname{utww}(G)=\infty.
\]

Together with Section 2,
\[
\boxed{
\operatorname{tww}\bigl(\operatorname{Sym}_{\mathrm{fin}}(\mathbb Z)\bigr)<\infty
\quad\text{and}\quad
\operatorname{utww}\bigl(\operatorname{Sym}_{\mathrm{fin}}(\mathbb Z)\bigr)=\infty.
}
\]

Thus the conjecture is true, and the proposed candidate is indeed a witness.

# Gaps and scope

There is no remaining mathematical case under the source paper's permutation-grid characterization of ordinary and uniform twin-width. The conversion between grid size and the numerical twin-width parameter is not tracked, because only boundedness versus unboundedness is needed. The argument also works if orders are chosen afresh for finite sets of group elements: taking the finite set to be all of \(A_n\), the lower bound holds for every possible order.