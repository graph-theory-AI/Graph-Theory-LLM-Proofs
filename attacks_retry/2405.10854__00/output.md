```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Unimodality holds for every connected graph with maximum orientable embedding genus at most two, so any counterexample must have cycle rank at least six.",
  "would_publish": false,
  "caveats": "The general conjecture is unresolved here; novelty of the partial results has not been checked, and counts use the fixed-graph rotation-system convention."
}
```

# 1. Results obtained

Write
\[
\Gamma_G(t)=\sum_{g\ge 0}a_g(G)t^g,
\qquad
\gamma_{\max}(G)=\max\{g:a_g(G)>0\}.
\]

I prove the following partial result.

**Theorem 1.** For every connected graph \(G\),
\[
\gamma_{\max}(G)\ge 2
\quad\Longrightarrow\quad
a_1(G)\ge a_0(G).
\]

Consequently:

**Corollary 2.** Every connected graph with maximum orientable embedding genus at most two has a unimodal genus distribution. In particular, the conjecture holds whenever
\[
\beta(G)=|E(G)|-|V(G)|+1\le 5.
\]

Thus a connected counterexample must satisfy
\[
\gamma_{\max}(G)\ge 3,\qquad \beta(G)\ge 6.
\]

I also prove an infinite-family result that extends the generalized-star calculation in the previous attempt.

**Theorem 3.** If \(G-v\) is a forest for some vertex \(v\), then \(\Gamma_G(t)\) has only negative real zeros, unless it is constant. In particular, its coefficients are log-concave.

The same conclusion holds for graphs obtained by joining such graphs with bridges.

These results do not settle the general conjecture. No computational verification is used below.

## Conventions

An orientable embedding of a fixed graph is counted by its rotation system: darts are distinguished, and graph automorphisms are not factored out. If global orientation reversal is also identified, it changes all coefficients by the same factor for a connected graph having a vertex of degree at least three, so the shape conclusions remain valid.

Subdividing edges preserves the genus polynomial. We may therefore subdivide loops and parallel edges when convenient and work with simple graphs in the structural argument.

For a connected rotation system with \(f\) faces, Euler’s formula gives
\[
f=\beta(G)+1-2g.
\]
Since \(f\ge 1\),
\[
\gamma_{\max}(G)\le \left\lfloor\frac{\beta(G)}2\right\rfloor. \tag{1}
\]

# 2. A local permutation calculation

Let
\[
\boldsymbol d=(d_1,\ldots,d_s),\qquad
N=\sum_i d_i,\qquad e=N-s.
\]
All \(d_i\) are positive.

Consider the graph consisting of a central vertex and \(s\) peripheral vertices, with \(d_i\) parallel edges to peripheral vertex \(i\). Fix the rotations at the peripheral vertices and vary only the central rotation.

The peripheral rotations determine a permutation \(\pi\in S_N\) with cycle lengths \(d_1,\ldots,d_s\). The central rotation is an \(N\)-cycle \(\sigma\), and the number of faces is \(c(\sigma\pi)\). Set
\[
F_{\boldsymbol d}(x)
=\sum_{\sigma\text{ an }N\text{-cycle}}x^{c(\sigma\pi)}
=\sum_{j\ge0}b_jx^{e+1-2j},
\]
and
\[
L_{\boldsymbol d}(t)=\sum_{j\ge0}b_jt^j.
\]
Conjugation shows that these polynomials depend only on \(\boldsymbol d\), not on the particular \(\pi\).

Define
\[
h(z)=\prod_{i=1}^s(1+z+\cdots+z^{d_i-1})
=\sum_{j=0}^{e}h_jz^j.
\]

**Lemma 4.**
\[
F_{\boldsymbol d}(x)
=(N-1)!\sum_{j=0}^{e}
h_j\binom{x+e-j}{e+1}. \tag{2}
\]
In particular,
\[
b_0=\frac{(N-1)!\prod_i d_i}{(e+1)!}, \tag{3}
\]
and, for \(e\ge2\),
\[
\boxed{\quad
\frac{b_1}{b_0}
=
\frac{e(e+1)}{24}
\left(\sum_i d_i(d_i-1)-2\right).
\quad} \tag{4}
\]

## Proof of the permutation identity

Here is a derivation, rather than an assumption of the formula in the previous attempt.

Let \(C_N\) be the conjugacy class of \(N\)-cycles. For positive integers \(x\), the class function \(\rho\mapsto x^{c(\rho)}\) is the character of the action of \(S_N\) on \((\mathbb C^x)^{\otimes N}\). Thus
\[
x^{c(\rho)}
=\sum_{\lambda\vdash N}s_\lambda(1^x)\chi^\lambda(\rho).
\]
Averaging over \(C_N\) gives
\[
F_{\boldsymbol d}(x)
=(N-1)!\sum_{\lambda\vdash N}
s_\lambda(1^x)
\frac{\chi^\lambda((N))\chi^\lambda(\pi)}{f^\lambda}.
\]

Only hooks \(\lambda_r=(N-r,1^r)\) contribute. For these,
\[
\chi^{\lambda_r}((N))=(-1)^r,
\qquad
\frac{s_{\lambda_r}(1^x)}{f^{\lambda_r}}
=\binom{x+N-r-1}{N}.
\]
The second identity follows directly from the hook-content and dimension formulas.

The hook representations are the exterior powers of the standard representation, so
\[
\sum_{r=0}^{N-1}\chi^{\lambda_r}(\pi)u^r
=\frac{\prod_i(1-(-u)^{d_i})}{1+u}.
\]
Consequently, if
\[
W(z)=\frac{\prod_i(1-z^{d_i})}{1-z}
=\sum_{r=0}^{N-1}w_rz^r,
\]
then
\[
F_{\boldsymbol d}(x)
=(N-1)!\sum_{r=0}^{N-1}
w_r\binom{x+N-r-1}{N}. \tag{5}
\]
These identities extend from positive integral \(x\) to polynomial identities.

For \(0\le r\le N-1\),
\[
\sum_{m\ge0}\binom{m+N-r-1}{N}z^m
=\frac{z^{r+1}}{(1-z)^{N+1}}.
\]
Hence
\[
\begin{aligned}
\frac1{(N-1)!}\sum_{m\ge0}F_{\boldsymbol d}(m)z^m
&=\frac{zW(z)}{(1-z)^{N+1}}\\
&=\frac{zh(z)}{(1-z)^{e+2}}.
\end{aligned}
\]
Coefficient extraction yields (2).

## Proof of the first-coefficient ratio

The leading coefficient in (2) immediately gives (3).

Normalize the coefficients \(h_j\) by \(h(1)=\prod_i d_i\). They are the distribution of
\[
J=U_1+\cdots+U_s,
\]
where the \(U_i\) are independent and uniform on
\(\{0,\ldots,d_i-1\}\). Thus
\[
\mathbb E J=\frac e2,\qquad
\operatorname{Var}J=\frac1{12}\sum_i(d_i^2-1).
\]

In
\[
\binom{x+e-j}{e+1}
=\frac1{(e+1)!}\prod_{k=0}^{e}(x+e-j-k),
\]
put \(u=e/2-j\). The coefficient of \(x^{e-1}\), divided by the leading coefficient, is
\[
\frac{e(e+1)}2u^2-\frac{e(e+1)(e+2)}{24}.
\]
Averaging over \(J\) gives
\[
\begin{aligned}
\frac{b_1}{b_0}
&=\frac{e(e+1)}{24}
\left(\sum_i(d_i^2-1)-e-2\right)\\
&=\frac{e(e+1)}{24}
\left(\sum_i d_i(d_i-1)-2\right),
\end{aligned}
\]
as claimed. ∎

Two useful consequences are:
\[
\begin{array}{ll}
\text{some }d_i\ge3
&\Longrightarrow b_1\ge b_0,\\[2mm]
e\ge3
&\Longrightarrow b_1\ge2b_0.
\end{array} \tag{6}
\]
For the first implication, \(e\ge2\) and the sum in (4) is at least \(6\). For the second,
\[
\sum_i d_i(d_i-1)\ge2\sum_i(d_i-1)=2e,
\]
so
\[
\frac{b_1}{b_0}
\ge\frac{e(e-1)(e+1)}{12}\ge2.
\]

# 3. Transferring the local ratio to an arbitrary graph

Let \(G\) be connected and planar, and choose a vertex \(v\) of positive degree. Let
\[
H_1,\ldots,H_s
\]
be the components of \(G-v\), and let \(d_i\) be the number of edges from \(v\) to \(H_i\).

**Lemma 5.** With the notation of Lemma 4,
\[
\frac{a_1(G)}{a_0(G)}
\ge
\frac{b_1}{b_0}. \tag{7}
\]

### Proof

Fix all rotations except the rotation at \(v\). Call this partial rotation system *planar-compatible* if at least one rotation at \(v\) completes it to a planar embedding.

For a planar-compatible partial rotation system, replace \(v\) by separate degree-one ends on its incident edges. For each \(H_i\), all its \(d_i\) marked ends lie on one boundary component of its planar ribbon neighborhood. Indeed, in a planar completion, the deleted vertex lies in one face of \(H_i\), and every edge from \(v\) to \(H_i\) approaches through that face.

Thus the boundary permutation on the marked ends has one cycle of length \(d_i\) for each component \(H_i\). Its cycle type is exactly \(\boldsymbol d\). The other boundary components contain no marked ends.

Writing \(\beta_i=\beta(H_i)\), there are \(\beta_i\) such unmarked boundary components in \(H_i\). Since
\[
\beta(G)=\sum_i\beta_i+N-s=\sum_i\beta_i+e,
\]
Euler’s formula shows that varying the rotation at \(v\) gives precisely the genus polynomial
\[
L_{\boldsymbol d}(t),
\]
with no genus shift.

Let \(M\) be the number of planar-compatible partial rotation systems. Every planar embedding arises from one of them, so
\[
a_0(G)=Mb_0.
\]
They contribute \(Mb_1\) genus-one embeddings. Other partial rotation systems may contribute additional genus-one embeddings, but none of genus zero. Therefore
\[
a_1(G)\ge Mb_1,
\]
which proves (7). ∎

In particular, a planar graph satisfies \(a_1\ge a_0\) if it has a vertex \(v\) for which either:

* some component of \(G-v\) receives at least three edges from \(v\); or
* \(\deg(v)-c(G-v)\ge3\).

# 4. Proof of Theorem 1

If \(a_0(G)=0\), the assertion is immediate. Assume \(G\) is planar. By subdivision, assume it is simple.

## 4.1. Non-cycle blocks

Suppose \(G\) has a block \(B\) that is neither an edge nor a cycle. Since \(B\) is 2-connected and not a cycle, it has a vertex \(v\) with
\[
\deg_B(v)\ge3.
\]
The graph \(B-v\) is connected. Hence at least three edges from \(v\) lead into the same component of \(G-v\).

Lemmas 4 and 5 therefore give
\[
a_1(G)\ge a_0(G). \tag{8}
\]

## 4.2. Three cyclic blocks at one vertex

Suppose a vertex \(v\) belongs to at least three cyclic blocks. These blocks lead into distinct components of \(G-v\), and each contributes at least two edges incident with \(v\). Thus
\[
e=\deg(v)-c(G-v)\ge3.
\]
Again, Lemmas 4 and 5 give \(a_1(G)\ge a_0(G)\), in fact \(a_1(G)\ge2a_0(G)\).

## 4.3. The remaining cactus case

It remains to consider graphs whose blocks are edges or cycles and in which every vertex belongs to at most two cyclic blocks.

First remove all bridges. Adding a bridge between two connected graphs multiplies their genus polynomials by a positive scalar and takes their product:
\[
\Gamma_{G_1\#G_2}(t)=c\,\Gamma_{G_1}(t)\Gamma_{G_2}(t). \tag{9}
\]
To see this, insert the two bridge darts into the rotations at its ends. The number of choices is independent of the rotation systems, and the bridge merges one face from each component; therefore genera add. At an endpoint of degree zero there is one insertion choice.

Consequently, deleting all bridges affects the remaining calculation only by a common positive scalar \(C\).

Every nontrivial remaining component is a cactus with vertex degrees two and four. Let \(m\) be the total number of degree-four vertices. At such a vertex, the two incident cycles partition the four darts into two pairs. Of the six cyclic orders:

* four are nonalternating;
* two alternate the two pairs.

The graph of cycle blocks, with adjacency when two cycles share a vertex, is a forest.

All choices of nonalternating rotations give planar embeddings. This follows by successively removing leaf cycles: their two darts are consecutive at the attachment vertex, and such a cycle can be added or removed without changing genus.

Conversely, an alternating pair of cycles cannot occur in a planar embedding. Two cycles meeting only at one vertex cannot alternate there in the sphere, by the Jordan curve theorem. Thus
\[
a_0(G)=C\,4^m. \tag{10}
\]

Every rotation system with exactly one alternating degree-four vertex has genus one. Remove nonalternating leaf cycles until only the two cycles meeting at that vertex remain. After suppressing degree-two vertices, these are two loops with alternating ends, whose ribbon neighborhood has genus one.

There are
\[
2m\,4^{m-1}
\]
such rotation systems when \(m\ge1\). Therefore
\[
a_1(G)\ge C\,2m\,4^{m-1},
\qquad
\frac{a_1(G)}{a_0(G)}\ge\frac m2. \tag{11}
\]

If \(m=0\), every embedding is planar. If \(m=1\), then
\[
\Gamma_G(t)=C(4+2t),
\]
so the maximum genus is one. Hence \(\gamma_{\max}(G)\ge2\) forces \(m\ge2\), and (11) gives \(a_1(G)\ge a_0(G)\).

This covers every case and proves Theorem 1. ∎

The argument actually yields the stronger classification
\[
a_1(G)<a_0(G)
\quad\Longrightarrow\quad
\Gamma_G(t)\text{ is constant or a positive multiple of }2+t. \tag{12}
\]

## Proof of Corollary 2

If the maximum genus is at most one, unimodality is automatic.

If it is two, Theorem 1 gives
\[
a_0\le a_1.
\]
Thus \((a_0,a_1,a_2)\) is either nondecreasing or has a peak at index one. It is unimodal.

Finally, \(\beta(G)\le5\) implies \(\gamma_{\max}(G)\le2\) by (1). ∎

# 5. Real-rootedness when all cycles meet one vertex

I next prove Theorem 3. The key point is that the polynomial transform in (2) has a useful zero-location property; its earlier alternating-coefficient form obscures this.

## 5.1. An elementary unit-circle transform lemma

**Lemma 6.** Suppose
\[
h(z)=\prod_{\ell=1}^{e}(1-\zeta_\ell z),
\qquad
|\zeta_\ell|=1,\quad \zeta_\ell\ne1,
\]
and let \(D\ge e\). Define
\[
U(x)=\sum_{j=0}^{e}h_j\binom{x+D-j}{D}.
\]
Then
\[
U(x)=\frac1{D!}
\left(\prod_{r=1}^{D-e}(x+r)\right)V(x),
\]
where every zero of \(V\) has real part
\[
-\frac{D-e+1}{2}.
\]

### Proof

Apply the factors \(1-\zeta_\ell z\) one at a time. Multiplication by \(1-\zeta z\) on the numerator corresponds to
\[
U_{\rm new}(x)=U_{\rm old}(x)-\zeta U_{\rm old}(x-1).
\]

Initially,
\[
U_0(x)=\binom{x+D}{D}.
\]
Suppose the \(j\)-th factor is being applied, and put \(k=D-j\). After extracting the common factors \(x+1,\ldots,x+k\), the new residual polynomial is
\[
V_{\rm new}(x)
=(x+k+1)V_{\rm old}(x)
-\zeta xV_{\rm old}(x-1). \tag{13}
\]
By induction, the zeros of \(V_{\rm old}\) have real part
\[
-\frac{k+2}{2}.
\]

Set \(y=x+(k+1)/2\). For suitable real numbers \(b_r\), the two products on the right of (13), up to the same nonzero constant, are
\[
\left(y+\frac{k+1}{2}\right)
\prod_r\left(y+\frac12-ib_r\right)
\]
and
\[
\zeta\left(y-\frac{k+1}{2}\right)
\prod_r\left(y-\frac12-ib_r\right).
\]

If \(\operatorname{Re}y>0\), every factor of the first product has strictly larger modulus than its counterpart in the second. If \(\operatorname{Re}y<0\), the reverse holds. Therefore their difference can vanish only when \(\operatorname{Re}y=0\).

The leading coefficient is multiplied by \(1-\zeta\ne0\), so the residual polynomial has the expected degree. This completes the induction. ∎

For the polynomial
\[
h(z)=\prod_i(1+z+\cdots+z^{d_i-1}),
\]
all zeros lie on the unit circle and none equals \(1\). Apply Lemma 6 with \(D=e+1\). All zeros of
\[
U(x)=\sum_jh_j\binom{x+e+1-j}{e+1}
\]
have real part \(-1\). Equation (2) says
\[
F_{\boldsymbol d}(x)=(N-1)!\,U(x-1).
\]
Thus every zero of \(F_{\boldsymbol d}\) lies on the imaginary axis.

Since \(F_{\boldsymbol d}\) has real coefficients and only powers of parity \(e+1\), it factors as
\[
F_{\boldsymbol d}(x)
=b_0x^r\prod_{\ell=1}^{q}(x^2+\lambda_\ell^2),
\qquad \lambda_\ell>0.
\]
Using
\[
F_{\boldsymbol d}(x)=x^{e+1}L_{\boldsymbol d}(x^{-2}),
\]
we obtain
\[
\boxed{\quad
L_{\boldsymbol d}(t)
=b_0\prod_{\ell=1}^{q}(1+\lambda_\ell^2t).
\quad} \tag{14}
\]
Hence all zeros of \(L_{\boldsymbol d}\) are negative real numbers.

## 5.2. Applying the lemma to \(G-v\) a forest

Suppose \(G-v\) is a forest with components \(H_1,\ldots,H_s\), and let \(d_i\) count edges from \(v\) to \(H_i\).

Fix arbitrary rotations away from \(v\). The ribbon neighborhood of each tree component is a disk, so its marked ends lie on one boundary component. There are no unmarked boundary components. Thus every fixed choice of rotations away from \(v\) gives the same central genus polynomial \(L_{\boldsymbol d}(t)\).

There are
\[
R=\prod_{w\ne v}(\deg_G(w)-1)!
\]
choices of those rotations, with the trivial one-vertex graph handled separately. Therefore
\[
\Gamma_G(t)=R\,L_{\boldsymbol d}(t). \tag{15}
\]
Equation (14) proves Theorem 3. Newton’s inequalities give log-concavity.

Bridge joining multiplies genus polynomials up to a positive scalar by (9), and products preserve negative real-rootedness. This proves the stated bridge-closed extension. ∎

# 6. Why this does not prove the full conjecture

The local calculation has a broader consequence. If all rotations except that at one vertex are fixed, the resulting genus polynomial is always a monomial times some \(L_{\boldsymbol d}(t)\).

Indeed, let \(\pi\) be the first-return permutation on darts at that vertex, and let \(f_0\) count facial cycles that never meet it. Then
\[
f=f_0+c(\sigma\pi).
\]
Euler’s formula gives the local genus polynomial as
\[
t^kL_{\boldsymbol d}(t)
\]
for a nonnegative integer \(k\). Consequently, every one-vertex conditional genus distribution is log-concave.

The obstacle is that the full genus polynomial is a **sum** of these conditional polynomials, whose shifts and cycle types may differ. Positive sums of negative-real-rooted polynomials need not even be unimodal. For example,
\[
(4+t)^2+(1+4t)^2=17+16t+17t^2.
\]
This is only an algebraic illustration of the obstruction, not a graph genus polynomial.

What is established here is therefore:

* unimodality for all connected graphs of maximum embedding genus at most two;
* the lower bound \(\beta\ge6\) for any connected counterexample;
* negative real-rootedness for graphs having a vertex whose deletion leaves a forest, and for their bridge combinations.

No inequality controlling \(a_2,a_3,\ldots\) strongly enough for arbitrary graphs is proved.

I independently rederived the previous attempt’s fixed-peripheral-rotation formula. Its finite tables and computational claims are not used. I have not checked whether the partial theorems above already occur in the literature, and I make no novelty claim for them.