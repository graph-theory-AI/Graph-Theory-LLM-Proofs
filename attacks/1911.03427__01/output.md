```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "The quoted conjecture has no determinate truth value, and the most direct uniform finite-group formulation is false.",
  "would_publish": false,
  "caveats": "The counterexamples exploit precisely the unspecified infinite-complexity and torsion/trivial-solution exclusions, so a suitably repaired formulation may remain open."
}
```

# Mathematical writeup

## 1. The statement is not presently a proposition

For an integer linear pattern
\[
L_i(x_1,\dots,x_k)=\sum_{j=1}^k a_{ij}x_j,\qquad a_{ij}\in\mathbb Z,
\]
and a coloring \(\phi:G\to[r]\), an all-tuples interpretation would count tuples \(\mathbf x\in G^k\) for which
\[
\phi(L_i(\mathbf x))=c_i\qquad(1\leq i\leq m).
\]

A direct uniform removal assertion would be:

> **(UR)** For every fixed finite family \(\mathcal H\) of colored integer-linear patterns and every \(\varepsilon>0\), there is \(\delta>0\) such that, for every sufficiently large finite abelian group \(G\), if every \(H\in\mathcal H\) has density at most \(\delta\), then the coloring can be changed on at most \(\varepsilon |G|\) elements so as to contain no member of \(\mathcal H\).

Several choices needed to turn the source sentence into a theorem are absent:

1. Whether “arbitrary abelian groups” means finite groups. Infinite discrete groups have no canonical normalized counting measure.
2. Whether \(\delta\) must be uniform over all groups, or may depend on their exponent or invariant factors. If it may depend on a fixed finite \(G\), the result is automatic by finiteness.
3. Whether complexity is computed over \(\mathbb Q\), modulo every prime dividing the group exponent, or in some group-relative module sense.
4. Which tuples are “generic” or “nontrivial.”
5. Whether the conclusion requires exact absence of every instance, or only absence of generic instances.
6. The quantifiers for infinite families of patterns.

These distinctions are substantive. The following two examples refute natural versions of (UR).

---

## 2. Infinite-complexity obstruction with no unavoidable solutions

Let the color set be \(\{R,B\}\), and consider the single pattern
\[
H=(x,2x;R,B).
\]
Thus an instance is a nonzero \(x\) such that
\[
\phi(x)=R,\qquad \phi(2x)=B.
\]

### Construction

There are primes \(p\) for which the multiplicative order
\[
d_p=\operatorname{ord}_p(2)
\]
is arbitrarily large. Indeed, for any \(D\), choose a prime not dividing
\[
2\prod_{j=1}^{D}(2^j-1);
\]
its order is larger than \(D\).

On \(G=\mathbb Z/p\mathbb Z\), multiplication by \(2\) partitions \(G\setminus\{0\}\) into
\[
\frac{p-1}{d_p}
\]
directed cycles of length \(d_p\). On every cycle
\[
x,2x,\dots,2^{d_p-1}x,
\]
color a consecutive block of \(\lfloor d_p/2\rfloor\) elements red and the remaining elements blue.

There is exactly one red-to-blue transition on each cycle. Consequently,
\[
\#H=\frac{p-1}{d_p},
\]
so the density of \(H\) in \(G\setminus\{0\}\) is exactly \(1/d_p\), tending to zero.

On the other hand, an \(H\)-free coloring of a directed cycle must be monochromatic. Indeed, if both colors occur, traversing the cycle from a red vertex eventually produces a red-to-blue transition. Therefore any \(H\)-free recoloring changes at least
\[
\frac{p-1}{d_p}\left\lfloor\frac{d_p}{2}\right\rfloor
\]
elements. As a fraction of \(G\setminus\{0\}\), this tends to \(1/2\).

Thus, for example, the coloring is \(1/3\)-far from \(H\)-freeness while the \(H\)-density tends to zero. Hence (UR) fails even for one fixed pattern and cyclic groups of prime order.

This is not a “trivial solution” obstruction: \(H\)-free colorings exist. Rather, the forms \(x\) and \(2x\) are proportional, so the system has infinite Cauchy–Schwarz complexity. It demonstrates that the unspecified infinite-complexity caveat is indispensable.

---

## 3. Torsion obstruction despite rational complexity zero

The next example shows that defining complexity only over \(\mathbb Q\) is insufficient.

For \(c\in\{R,B\}\), let \(H_c\) be the two-form pattern
\[
L_1(x,y)=x,\qquad L_2(x,y)=-x+4y,
\]
with both outputs required to have color \(c\).

The coefficient matrix is
\[
A=\begin{pmatrix}
1&0\\
-1&4
\end{pmatrix},
\qquad \det A=4.
\]
Thus the two forms are linearly independent over \(\mathbb Q\), and under the usual characteristic-zero linear-span definition this is a complexity-zero system.

Take
\[
G_n=(\mathbb Z/4\mathbb Z)^n,\qquad N=|G_n|=4^n,
\]
and color \(G_n\setminus\{0\}\). Since \(4y=0\),
\[
L_2(x,y)=-x.
\]

Let
\[
T=G_n[2]=\{x\in G_n:2x=0\},
\qquad |T|=2^n.
\]
Color every element of \(T\setminus\{0\}\) red. The remaining elements form two-element inversion orbits \(\{x,-x\}\); color the two elements of each such orbit oppositely.

Then:

- If \(x\notin T\), the colors of \(x\) and \(-x\) differ.
- If \(x\in T\setminus\{0\}\), then \(-x=x\), and both evaluations are red.

Therefore
\[
\#H_R=(2^n-1)4^n,\qquad \#H_B=0.
\]
Normalized by \(N^2\),
\[
t_{H_R}=2^{-n}-4^{-n}\longrightarrow 0,
\qquad
t_{H_B}=0.
\]

Nevertheless, no \(\{H_R,H_B\}\)-free coloring exists. For any nonzero \(t\in T\) and every \(y\),
\[
L_1(t,y)=L_2(t,y)=t.
\]
Whichever color is assigned to \(t\) creates the corresponding pattern \(H_R\) or \(H_B\).

Consequently, the following precise formulation is false:

> Integer systems of Cauchy–Schwarz complexity at most \(1\) over \(\mathbb Q\) satisfy an all-tuples, exact induced removal lemma uniformly over all finite abelian groups.

The reason is that the matrix becomes degenerate on exponent-\(4\) groups. Modulo \(2\), its two rows coincide. A group-relative definition of complexity could exclude this system, but the catalog statement does not specify such a definition. Likewise, declaring the order-\(2\) collision tuples nongeneric would avoid the example, but no genericity notion is given.

---

## 4. A rigorous positive fragment: universally split complexity-zero systems

There is an elementary torsion-safe special case.

### Proposition

Let \(\mathcal H\) be a finite family of colored patterns. For \(H\in\mathcal H\), let its \(m_H\) forms in \(k_H\) variables have coefficient matrix
\[
A_H\in\mathbb Z^{m_H\times k_H}.
\]
Assume that \(A_H\) has an integer right inverse:
\[
A_HB_H=I_{m_H}
\]
for some integer matrix \(B_H\).

Then for every \(r\) and \(\varepsilon>0\), there is a \(\delta>0\), independent of the finite abelian group \(G\), such that any \(r\)-coloring of \(G\) with density at most \(\delta\) of every \(H\in\mathcal H\) can be recolored on at most \(\varepsilon |G|\) points to eliminate all patterns in \(\mathcal H\).

### Proof

For every abelian group \(G\), the map
\[
A_H:G^{k_H}\longrightarrow G^{m_H}
\]
is surjective, since \(A_HB_H=I\). For finite \(G\), all fibers have equal size.

Let
\[
\alpha_c=\frac{|\phi^{-1}(c)|}{|G|}.
\]
If \(H\) prescribes the color vector
\[
(c_{H,1},\dots,c_{H,m_H}),
\]
then surjectivity and equal fibers give the exact density
\[
t_H(\phi)=\prod_{i=1}^{m_H}\alpha_{c_{H,i}}.
\]

Put
\[
M=\max_{H\in\mathcal H}m_H,\qquad
\tau=\min\left\{\frac{\varepsilon}{2r},\frac1{2r}\right\},
\qquad
\delta=\tau^M.
\]
Let
\[
S=\{c\in[r]:\alpha_c>\tau\}.
\]
Because some color has density at least \(1/r>\tau\), the set \(S\) is nonempty.

For any \(H\), not all of its prescribed colors can lie in \(S\). Otherwise,
\[
t_H(\phi)
 =\prod_i\alpha_{c_{H,i}}
 >\tau^{m_H}
 \geq \tau^M
 =\delta,
\]
contrary to the hypothesis.

Choose \(c_0\in S\), and recolor every point whose color is outside \(S\) with color \(c_0\). The proportion changed is at most
\[
\sum_{c\notin S}\alpha_c\leq r\tau\leq\varepsilon.
\]
The new coloring uses only colors in \(S\), while every forbidden pattern requires at least one color outside \(S\). Hence no forbidden pattern remains. ∎

By Smith normal form, an integer matrix \(A_H\) has a right inverse exactly when its maximal minors generate the unit ideal. This is the natural universally nondegenerate version of complexity zero: the output forms remain jointly independent on every abelian group. The determinant-\(4\) matrix in the torsion counterexample fails precisely this condition.

---

## 5. Gaps and remaining open core

The examples do not disprove every possible intended conjecture. They show that at least the following must be fixed before there is a theorem to prove:

1. Restrict to finite abelian groups and specify uniformity in the group.
2. Give a torsion-sensitive complexity condition, likely requiring the relevant linear-span separations to remain valid modulo primes dividing the group exponent.
3. Define generic or admissible tuples uniformly across groups with different invariant factors.
4. Specify whether exact freeness is required when trivial torsion configurations make the property empty.
5. State the quantifiers for collections of patterns.

The positive proposition handles only universally split complexity-zero systems. It does not address genuine complexity-one systems. Thus the plausible torsion-safe, generic-instance complexity-one removal problem remains unresolved here, but the catalog’s current informal wording is not itself a well-posed conjecture.