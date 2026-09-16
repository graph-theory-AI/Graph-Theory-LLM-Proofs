```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured lower bound holds for drawings with at most four rotation types left after reverse-rotation cancellation, but the unrestricted conjecture is not resolved.",
  "would_publish": false,
  "caveats": "Structural special case only; no novelty claim or improvement of the unrestricted bounds."
}
```

## 1. A structural partial result

Write
\[
f(t)=\left\lfloor\frac t2\right\rfloor
     \left\lfloor\frac{t-1}2\right\rfloor,
\qquad
Z(m,n)=f(m)f(n),
\]
with \(f(0)=0\). Let \(C(D)\) denote the number of crossings in a good drawing \(D\), as defined in the question.

Fix an orientation of the plane and label the two vertex classes \(U,V\), where \(|U|=m\) and \(|V|=n\). The **rotation** at \(v\in V\) is the cyclic order of its \(m\) incident edges, identified with a cyclic order of \(U\). For a rotation \(\sigma\), write \(\bar\sigma\) for its reversal.

Consider the following cancellation operation on the multiset of rotations at \(V\): cancel one occurrence of \(\sigma\) against one occurrence of \(\bar\sigma\), repeatedly.

**Partial theorem.** Suppose that, after these cancellations, at most four distinct rotations remain. Then
\[
C(D)\ge Z(m,n).
\]

Thus the conclusion holds, in particular, if:

- there are at most four rotation types on one side; or
- the rotation multiplicities are invariant under reversal, apart from at most four reversal pairs.

By symmetry, the hypothesis may be imposed on either vertex class. Consequently, any drawing contradicting the conjecture must have **at least five reversal pairs with unequal multiplicities on each side**.

I give a self-contained proof. I do not claim that this structural result is new.

## 2. Equal rotations force many crossings

For distinct \(x,y\in V\), let \(c(x,y)\) be the number of crossings between an edge incident with \(x\) and an edge incident with \(y\). Every crossing has exactly two distinct endpoints in \(V\), so
\[
C(D)=\sum_{\{x,y\}\subseteq V}c(x,y).
\tag{1}
\]

We use the identities
\[
f(t)=\binom t2-\left\lfloor\frac{t^2}{4}\right\rfloor
=\min_{a+b=t}\left(\binom a2+\binom b2\right).
\tag{2}
\]

### Equal-rotation lemma

Suppose \(m\) simple curves join two points on an oriented sphere, are in general position away from their endpoints, and have the same cyclic order at both endpoints. Then they have at least \(f(m)\) crossings.

**Proof.** Form a graph \(H\) whose vertices are the \(m\) curves, with two vertices adjacent when the corresponding curves have disjoint interiors.

The graph \(H\) is triangle-free. Indeed, three pairwise internally disjoint curves would form an embedded theta graph. In an oriented sphere, the three paths of an embedded theta graph have opposite cyclic orders at its two branch vertices. This follows immediately by considering the two regions bounded by the first two paths and locating the third path. It contradicts the assumed equal orders.

Therefore
\[
|E(H)|\le \left\lfloor\frac{m^2}{4}\right\rfloor.
\]
For completeness, the usual triangle-free bound follows from
\[
\frac{4|E(H)|^2}{m}
\le \sum_v d(v)^2
=\sum_{uv\in E(H)}(d(u)+d(v))
\le m|E(H)|.
\]

Each nonedge of \(H\) accounts for at least one crossing, and different nonedges account for different pairs of curves. Thus the total is at least
\[
\binom m2-\left\lfloor\frac{m^2}{4}\right\rfloor=f(m).
\qquad\square
\]

Apply the lemma to the \(m\) paths
\[
x-u-y,\qquad u\in U.
\]
These paths are simple because adjacent edges do not cross. Hence
\[
\sigma(x)=\sigma(y)
\quad\Longrightarrow\quad
c(x,y)\ge f(m).
\tag{3}
\]

## 3. Opposite rotations can be cancelled

The following stronger local fact makes cancellation possible.

### Opposite-rotation lemma

If \(y,z\in V\) have opposite rotations, then for every \(x\in V\setminus\{y,z\}\),
\[
c(x,y)+c(x,z)\ge f(m).
\tag{4}
\]

**Proof.** Take independent copies of the two restricted drawings on \(U\cup\{x,y\}\) and \(U\cup\{x,z\}\), viewed on oriented spheres.

In each copy, remove small disks around the two vertices outside \(U\). Each remaining surface is an annulus carrying \(m\) curves between its boundary components, labelled by \(U\). Its crossing count is respectively \(c(x,y)\) or \(c(x,z)\).

Because the rotations at \(y,z\) are reversed, their boundary circles can be glued by an orientation-reversing homeomorphism matching equally labelled curve endpoints. The result is an oriented annulus. Cap its two remaining boundaries, extending the curves to the centers of the caps.

We have obtained \(m\) simple curves between two points, with:

- the same rotation at the two endpoints, inherited from the two copies of \(x\);
- exactly \(c(x,y)+c(x,z)\) crossings.

The equal-rotation lemma proves (4). Notice that no assumption about \(c(y,z)\) was needed. \(\square\)

Deleting \(y,z\) consequently gives
\[
\begin{aligned}
C(D)-C(D-\{y,z\})
&=c(y,z)+
  \sum_{x\in V\setminus\{y,z\}}\bigl(c(x,y)+c(x,z)\bigr)\\
&\ge f(m)(n-2).
\end{aligned}
\tag{5}
\]

Deleting vertices of \(V\) does not change the rotations at the remaining vertices of \(V\). Thus (5) can be iterated.

If \(p\) opposite-rotation pairs are deleted, leaving a drawing \(D_0\) with \(r=n-2p\) vertices on that side, then
\[
C(D)\ge C(D_0)+f(m)p(n-p-1).
\tag{6}
\]
The exact identity
\[
f(n)-f(r)=p(n-p-1)
\tag{7}
\]
follows by iterating \(f(t)-f(t-2)=t-2\).

In particular,
\[
C(D)-Z(m,n)\ge C(D_0)-Z(m,r).
\tag{8}
\]

## 4. A universal inequality for three vertices

Put \(A=f(m)\). For every three distinct \(x,y,z\in V\),
\[
c(x,y)+c(x,z)+c(y,z)\ge A.
\tag{9}
\]

Here is a direct proof, avoiding any external crossing-number result. Restrict the drawing to \(K_{m,3}\) on \(U\cup\{x,y,z\}\). Each vertex of \(U\) now has degree three, so there are only two possible rotations. If their multiplicities are \(s,m-s\), then (3), applied with three paths, gives at least
\[
\binom s2+\binom{m-s}{2}\ge f(m)=A
\]
crossings. This is precisely (9).

This also proves the lower bound for \(K_{3,m}\).

## 5. Four rotation types suffice

Assume \(m\ge3\), so \(A>0\). Suppose the vertices of \(V\) have \(k\le4\) rotation classes, of sizes \(a_1,\ldots,a_k\).

Crossings between vertices in the same class contribute at least
\[
A\sum_i\binom{a_i}{2}.
\tag{10}
\]

For \(i\ne j\), let \(E_{ij}\) be the total crossing contribution between classes \(i,j\), and define
\[
q_{ij}=\frac{E_{ij}}{A a_i a_j}.
\]
Summing (9) over all triples with one vertex in each of three distinct classes gives
\[
q_{ij}+q_{i\ell}+q_{j\ell}\ge1.
\tag{11}
\]
Consequently,
\[
\frac{C(D)}A
\ge
\sum_i\binom{a_i}{2}
+\sum_{i<j}a_i a_jq_{ij}.
\tag{12}
\]

For one or two classes, (2) proves the desired bound immediately.

For three classes, order the sizes \(a\ge b\ge c\). Nonnegativity and (11) give
\[
abq_{12}+acq_{13}+bcq_{23}
\ge bc(q_{12}+q_{13}+q_{23})
\ge bc.
\]
Therefore
\[
\frac{C(D)}A
\ge \binom a2+\binom{b+c}{2}
\ge f(a+b+c).
\tag{13}
\]

The four-class case requires a small weighted inequality.

### Weighted four-class lemma

Let \(a\ge b\ge c\ge d>0\), and suppose \(q_{ij}\ge0\) satisfies (11) for every triple of \(\{1,2,3,4\}\). Then
\[
\begin{aligned}
W:={}&abq_{12}+acq_{13}+adq_{14}
      +bcq_{23}+bdq_{24}+cdq_{34}\\
\ge{}&\min\{ad+bc,\;bc+bd+cd\}.
\end{aligned}
\tag{14}
\]

**Proof.** Write \(T_{ijk}=q_{ij}+q_{ik}+q_{jk}\).

If \(a\ge b+c\), coefficient comparison gives
\[
W\ge bcT_{123}+bdT_{124}+cdT_{134}
\ge bc+bd+cd.
\]
For example, the coefficient of \(q_{12}\) on the middle expression is
\(b(c+d)\le ab\); the other comparisons follow similarly.

Suppose instead that \(a\le b+c\). Set
\[
\begin{aligned}
\lambda_1&=\frac{d(b+c-a)}2,&
\lambda_2&=\frac{d(a+c-b)}2,\\
\lambda_3&=\frac{d(a+b-c)}2,&
\lambda_4&=bc-\frac{d(b+c-a)}2.
\end{aligned}
\]
All four numbers are nonnegative. Weight the four triangle inequalities by
\(\lambda_i\), where \(\lambda_i\) weights the triangle omitting \(i\).

The coefficients obtained for \(q_{14},q_{23},q_{24},q_{34}\) equal those in \(W\). The remaining coefficient slacks are
\[
ab-(\lambda_3+\lambda_4)=(a-c)(b-d)\ge0,
\]
and
\[
ac-(\lambda_2+\lambda_4)=(a-b)(c-d)\ge0.
\]
Hence
\[
W\ge \lambda_1T_{234}+\lambda_2T_{134}
       +\lambda_3T_{124}+\lambda_4T_{123}
\ge\sum_i\lambda_i=ad+bc.
\]
These two cases prove (14). \(\square\)

Using (14) in (12),
\[
\begin{aligned}
\frac{C(D)}A
&\ge
\min\left\{
\binom{a+d}{2}+\binom{b+c}{2},\;
\binom a2+\binom{b+c+d}{2}
\right\}\\
&\ge f(a+b+c+d),
\end{aligned}
\]
by (2). This proves
\[
C(D)\ge Z(m,n)
\tag{15}
\]
whenever there are at most four rotation types.

## 6. Completion of the partial theorem

Cancel opposite rotations by deleting corresponding vertex pairs. Under the theorem’s hypothesis, the remaining drawing \(D_0\) has at most four rotation types, so
\[
C(D_0)\ge f(m)f(r).
\]
Combining this with (6) and (7) yields
\[
C(D)\ge f(m)\bigl(f(r)+p(n-p-1)\bigr)
      =f(m)f(n).
\]

The cases \(m\le2\) have \(Z(m,n)=0\), so the claimed lower bound is immediate. All cases of the partial theorem are therefore covered.

There is also a quantitative consequence without the four-type hypothesis. If cancellation leaves \(r\) vertices, then \(C(D_0)\ge0\) gives
\[
C(D)\ge Z(m,n)-Z(m,r).
\tag{16}
\]
Thus rotation multisets whose total unmatched multiplicity is \(o(n)\) satisfy the conjectured lower bound asymptotically.

## 7. Sharpness and known special cases

The axis construction in the question gives the matching upper bound. With generic distances along the axes, its crossings number
\[
\left(
\binom{\lfloor m/2\rfloor}{2}
+\binom{\lceil m/2\rceil}{2}
\right)
\left(
\binom{\lfloor n/2\rfloor}{2}
+\binom{\lceil n/2\rceil}{2}
\right)
=Z(m,n).
\]
Generic choices avoid triple crossings. On either ray of the \(x\)-axis, the rotations are constant, and the two ray rotations are reversed. Hence this construction lies in the class covered above.

The argument also recovers the known exact cases \(\min\{m,n\}\le4\): for \(3\le m\le4\), the \((m-1)!\) cyclic orders form at most three reversal pairs, so the partial theorem applies to every drawing.

## 8. The remaining gap

Nothing above controls drawings with at least five uncancelled rotation types on both sides.

There is a concrete obstruction to extending the four-class calculation using only the inequalities already proved. Take five formal classes, each of size \(t\), assign normalized crossing weight \(1\) within a class and \(1/3\) between distinct classes. These weights satisfy all the equal-class and triangle inequalities used in Section 5. Nevertheless, when \(t\) is even,
\[
f(5t)-
\left(5\binom t2+\frac{10}{3}t^2\right)
=\frac{5}{12}t^2>0.
\]
Thus those local inequalities alone permit a total below the conjectured value.

This is **not a drawing or a counterexample**: no topological realizability is asserted. It identifies the missing ingredient—additional constraints among five or more surviving rotation types. The unrestricted Zarankiewicz conjecture is not proved or disproved by this argument.