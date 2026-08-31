```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Consensus-type forbidden families are induced-removable for arbitrary finite abelian groups and for higher-complexity progressions in Z, while arbitrary-complexity finite-field families are removable when a safe color is available.",
  "would_publish": false,
  "caveats": "The general all-colors finite-complexity case remains open; the cyclic obstruction below uses proportional forms of infinite CS complexity."
}
```

# 1. Formal setting

The quoted problem is a research program rather than a single fully quantified statement, particularly over \(\mathbb Z\) and “general abelian groups.” I use the following standard formulations.

Let \(G\) be a finite abelian group and let
\[
\mathcal L=(L_1,\dots,L_m),\qquad
L_i:G^d\to G
\]
be fixed integer linear forms. An \(r\)-colored pattern is \((\mathcal L,\psi)\), where \(\psi:[m]\to[r]\). For a coloring \(\phi:G\to[r]\), an instance is a tuple \(\mathbf x\in G^d\) satisfying
\[
\phi(L_i(\mathbf x))=\psi(i)\quad(1\le i\le m).
\]
Instance counts are normalized by \(|G|^d\).

For \(V=\mathbb F_q^n\), the source paper colors \(V\setminus\{0\}\) and usually counts generic instances, meaning that the linear map
\[
\mathbb F_q^d\to V,\qquad e_j\mapsto x_j
\]
is injective. The number of non-generic parameter tuples is at most
\[
(q^d-1)|V|^{d-1},                                             \tag{1}
\]
since a non-injective tuple satisfies \(\sum_j a_jx_j=0\) for some nonzero \(a\in\mathbb F_q^d\).

The results below are genuine special cases, not a solution of the full conjecture.

---

# 2. A same-palette induced removal theorem over arbitrary finite abelian groups

The first result applies to systems of arbitrarily high Cauchy–Schwarz complexity, but to a particularly coercive forbidden family.

## Theorem 2.1: pair-consensus removal

Let \(G\) be a finite abelian group of order \(N\), and let
\[
\mathcal L=(L_1,\dots,L_m)
\]
be a system of forms in \(d\) variables. Suppose that for two indices \(a\ne b\), the homomorphism
\[
P=(L_a,L_b):G^d\longrightarrow G^2
\]
is surjective.

Let
\[
\mathcal F_{a,b}
 =\{\psi\in[r]^m:\psi(a)\ne\psi(b)\}.
\]
Set
\[
K=|\mathcal F_{a,b}|=(r-1)r^{m-1}.
\]

If every pattern \((\mathcal L,\psi)\), \(\psi\in\mathcal F_{a,b}\), has at most
\[
\delta N^d
\]
instances in \(\phi:G\to[r]\), then \(\phi\) can be made constant, and hence \(\mathcal F_{a,b}\)-free, by recoloring at most
\[
K\delta N
\]
points.

### Proof

Write
\[
A_c=\phi^{-1}(c),\qquad \alpha_c=\frac{|A_c|}{N}.
\]
Every parameter tuple for which
\[
\phi(L_a(\mathbf x))\ne\phi(L_b(\mathbf x))
\]
has exactly one color word belonging to \(\mathcal F_{a,b}\). Consequently,
\[
\begin{aligned}
&|\{\mathbf x\in G^d:
  \phi(L_a(\mathbf x))\ne\phi(L_b(\mathbf x))\}|\\
&\hspace{2cm}\le K\delta N^d.                                  \tag{2}
\end{aligned}
\]

Because \(P\) is a surjective homomorphism between finite groups, all its fibers have cardinality \(N^{d-2}\). Therefore the left-hand side of (2) is
\[
\begin{aligned}
N^{d-2}|\{(u,v)\in G^2:\phi(u)\ne\phi(v)\}|
  &=N^d\left(1-\sum_{c=1}^r\alpha_c^2\right).
\end{aligned}
\]
Thus
\[
1-\sum_c\alpha_c^2\le K\delta.                                 \tag{3}
\]
Let \(\alpha_*=\max_c\alpha_c\). Since
\[
\sum_c\alpha_c^2\le \alpha_*\sum_c\alpha_c=\alpha_*,
\]
equation (3) gives
\[
1-\alpha_*\le K\delta.
\]
Recolor every point outside the largest color class to that color. This changes at most \(K\delta N\) points. The resulting constant coloring has no pattern in \(\mathcal F_{a,b}\). \(\square\)

A sufficient condition for pair-surjectivity uniformly over every abelian group is that the \(2\times d\) integer coefficient matrix of \((L_a,L_b)\) have an integer right inverse. In particular, a \(2\times2\) minor of determinant \(\pm1\) suffices.

## Corollary 2.2: higher-complexity progressions in every finite abelian group

Let
\[
\mathcal L_k=(x,x+d,\dots,x+(k-1)d).
\]
For every finite abelian group \(G\), the map
\[
(x,d)\mapsto (x,x+d)
\]
is a bijection \(G^2\to G^2\). Hence Theorem 2.1 applies to the family of all color words satisfying
\[
\psi(0)\ne\psi(1).
\]

In particular, for every \(\varepsilon>0\), taking
\[
\delta=\frac{\varepsilon}{(r-1)r^{k-1}}
\]
is sufficient to recolor at most \(\varepsilon|G|\) points and eliminate all these forbidden colored \(k\)-term progressions.

Over \(\mathbb Q\), the system
\[
x,x+d,\dots,x+(k-1)d
\]
has Cauchy–Schwarz complexity exactly \(k-2\). Indeed, for a fixed \(L_i=x+id\), any two other forms span the full two-dimensional dual space and hence span \(L_i\). Thus every class in a CS partition must contain at most one other form, requiring \(k-1\) classes and complexity at least \(k-2\); the singleton partition attains this value. Therefore \(k=4\) already gives a complexity-\(2\) special case.

The same calculation holds over fields of characteristic at least \(k\).

## Compatibility with generic finite-field instances

For \(V=\mathbb F_q^n\setminus\{0\}\), extend the coloring arbitrarily to \(0\). If only generic instances are counted, equation (1) contributes an error \(O_{q,d}(|V|^{d-1})\). Therefore the conclusion becomes
\[
\operatorname{dist}(\phi,\text{a constant coloring})
 \le \left(K\delta+O_{q,d}(|V|^{-1})\right)|V|.
\]
Thus this is also a genuine higher-complexity, same-palette special case in the precise finite-field model of the source paper.

The restrictive feature is that the forbidden family forces two independently distributed outputs to have the same color; consequently every permissible coloring is essentially constant.

---

# 3. An interval-\(\mathbb Z\) theorem for higher-complexity progressions

Here is a direct integer analogue which does not pass through cyclic groups.

## Theorem 3.1

Fix \(k\ge4\), \(r\ge2\), and \(\varepsilon>0\). There are \(\delta>0\) and \(N_0\) such that the following holds.

Let
\[
\phi:[N]\to[r],\qquad N\ge N_0.
\]
For every nonconstant word
\[
\psi\in[r]^k\setminus\{(c,\dots,c):c\in[r]\},
\]
suppose that the number of proper progressions
\[
(x,x+d,\dots,x+(k-1)d)\subseteq[N],\qquad d>0,
\]
having color word \(\psi\) is at most \(\delta N^2\).

Then \(\phi\) can be made constant, and hence free of all the forbidden nonconstant words, by recoloring at most \(\varepsilon N\) integers.

### Proof

It suffices to prove the sequential statement:

> If the total number \(T_N\) of nonmonochromatic \(k\)-term progressions is \(o(N^2)\), then \(\phi\) is \(o(N)\)-close to a constant coloring.

Let
\[
D=\left\lfloor\frac{N}{2k-3}\right\rfloor
\]
and let \(E_N\) be the number of unordered bichromatic pairs
\[
\{u,v\}\subseteq[N],\qquad 0<v-u\le D.
\]

We claim
\[
E_N\le 2T_N.                                                    \tag{4}
\]
Indeed, put \(d=v-u\).

* If \(u-(k-2)d\ge1\), then
  \[
  u-(k-2)d,\dots,u,v
  \]
  is a \(k\)-term progression in \([N]\), and it is nonmonochromatic.

* Otherwise \(u\le(k-2)d\), and
  \[
  u+(k-1)d\le(2k-3)d\le N.
  \]
  Thus
  \[
  u,v,\dots,u+(k-1)d
  \]
  is a nonmonochromatic \(k\)-term progression in \([N]\).

A fixed progression can arise in this construction only from its first or its last consecutive pair, proving (4). Hence
\[
E_N=o(N^2).                                                     \tag{5}
\]

Now partition \([N]\) into
\[
B=8(2k-3)
\]
consecutive intervals \(I_1,\dots,I_B\) whose sizes differ by at most one. For sufficiently large \(N\), every two points in the same interval or in two consecutive intervals are at distance at most \(D\).

For \(c\in[r]\), write
\[
n_{j,c}=|\{x\in I_j:\phi(x)=c\}|.
\]
Let \(c_j\) be a color maximizing \(n_{j,c}\), and put
\[
s_j=|I_j|-n_{j,c_j}.
\]
All pairs inside \(I_j\) are short. In particular, the number of bichromatic pairs inside \(I_j\) is at least
\[
n_{j,c_j}s_j.
\]
Since
\[
n_{j,c_j}\ge \frac{|I_j|}{r}=\Theta_{k,r}(N)
\]
and \(E_N=o(N^2)\), it follows that
\[
s_j=o(N)                                                        \tag{6}
\]
for each of the finitely many blocks.

Moreover, adjacent dominant colors must agree. If \(c_j\ne c_{j+1}\), then the pairs between the \(c_j\)-colored majority of \(I_j\) and the \(c_{j+1}\)-colored majority of \(I_{j+1}\) are all short and bichromatic. Their number is \(\Theta_{k,r}(N^2)\), contradicting (5). Thus
\[
c_1=c_2=\cdots=c_B=:c.
\]
By (6), only
\[
\sum_{j=1}^B s_j=o(N)
\]
points fail to have color \(c\). Recoloring them produces a constant coloring.

Finally, the sequential statement implies the claimed \(\varepsilon\)-\(\delta\) formulation. Otherwise, for some fixed \(\varepsilon>0\), one could choose \(N_j\to\infty\) and colorings that are \(\varepsilon N_j\)-far from constant while every forbidden word occurs at most \(N_j^2/j\) times, contradicting the sequential conclusion. \(\square\)

Because the \(k\)-term progression system has complexity \(k-2\), this gives a genuine complexity-\(2\) result on \(\mathbb Z\) already for \(k=4\). It is nevertheless a very special forbidden family: all nonmonochromatic words are forbidden, forcing approximate consensus.

---

# 4. Arbitrary complexity when a safe color exists

The following reduction handles arbitrary finite-CS-complexity systems over a fixed finite field, but neutralizes the central induced difficulty.

## Theorem 4.1: safe-color removal

Fix \(q\), a finite family \(\mathcal H\) of \(r\)-colored systems of linear forms over \(\mathbb F_q\), and a color \(s\in[r]\) which does not occur in the prescribed color word of any member of \(\mathcal H\).

Then, without any restriction on the Cauchy–Schwarz complexity of the systems, the following holds. For every \(\varepsilon>0\), there are \(\delta>0\) and \(n_0\) such that if
\[
\phi:\mathbb F_q^n\setminus\{0\}\to[r],\qquad n\ge n_0,
\]
has at most
\[
\delta|\mathbb F_q^n|^{d_H}
\]
generic instances of each \(H\in\mathcal H\), then one can recolor at most
\[
\varepsilon|\mathbb F_q^n|
\]
points, all to color \(s\), so that no instance of any \(H\in\mathcal H\) remains.

### Proof

We use the standard coordinate-set finite-field arithmetic removal lemma:

> For a fixed system \(\mathcal L=(L_1,\dots,L_m)\) in \(d\) variables and every \(\eta>0\), there is \(\rho>0\) such that, whenever \(A_1,\dots,A_m\subseteq\mathbb F_q^n\) contain at most \(\rho|V|^d\) tuples \(\mathbf x\) with \(L_i(\mathbf x)\in A_i\) for all \(i\), one can delete sets \(E_i\subseteq A_i\), with total size at most \(\eta|V|\), so that no such tuple remains.

This is the usual finite-field linear removal lemma, obtained from the finite hypergraph removal theorem; it applies to every fixed matrix system, not merely systems of CS complexity \(1\).

For \(H=(\mathcal L,\psi)\), put
\[
A_i=\{v\ne0:\phi(v)=\psi(i)\}.
\]
By (1), the number of non-generic parameter tuples is \(O_{q,d_H}(|V|^{d_H-1})\). Thus, after choosing \(n_0\) large and \(\delta\) sufficiently small, the total number of tuples satisfying
\[
L_i(\mathbf x)\in A_i\quad\text{for every }i
\]
is below the threshold required by the ordinary arithmetic removal lemma.

Apply that lemma separately to each \(H\), with the deletion budgets chosen so that their sum over all \(H\) is at most \(\varepsilon|V|\). Let \(E\) be the union of all resulting deletion sets, and recolor every point of \(E\) to \(s\).

This cannot create a forbidden instance, because no forbidden pattern requests color \(s\). If an \(H\)-instance survived, none of its outputs could lie in \(E\), and hence it would give a solution surviving the coordinate deletions for \(H\), a contradiction. \(\square\)

Equivalently, if the repair is allowed one new color not appearing in the forbidden patterns, induced removal at arbitrary complexity follows immediately from ordinary arithmetic removal. This special case bypasses the main issue: in the original conjecture, recoloring a deleted point to an existing requested color may create new forbidden patterns.

---

# 5. An obstruction to a literal unrestricted general-group statement

Without a finite-complexity or admissibility condition, a uniform theorem over all finite abelian groups is false.

## Proposition 5.1

There is no induced removal lemma, uniform over all cyclic groups, for the two forbidden patterns
\[
(x,2x)\text{ colored }(R,B)
\quad\text{and}\quad
(x,2x)\text{ colored }(B,R).
\]

### Proof

Choose primes \(p\) for which
\[
t_p=\operatorname{ord}_p(2)\longrightarrow\infty.
\]
Such a sequence exists: for fixed \(T\), every prime satisfying \(\operatorname{ord}_p(2)\le T\) divides one of the finitely many integers \(2^j-1\), \(1\le j\le T\).

Multiplication by \(2\) partitions \(\mathbb F_p^\times\) into
\[
\frac{p-1}{t_p}
\]
cycles of length \(t_p\). On each cycle
\[
u,2u,\dots,2^{t_p-1}u,
\]
color the first \(\lfloor t_p/2\rfloor\) points red and the remaining points blue.

Each cycle has exactly one directed \(R\to B\) transition and exactly one directed \(B\to R\) transition. Hence each forbidden pattern has exactly
\[
\frac{p-1}{t_p}=o(p)
\]
instances.

On the other hand, a coloring avoiding both patterns must satisfy
\[
\phi(x)=\phi(2x)\qquad\text{for every }x\ne0,
\]
and therefore must be constant on each doubling cycle. The constructed coloring has distance at least
\[
\frac{p-1}{t_p}\left\lfloor\frac{t_p}{2}\right\rfloor
 =\left(\frac12-o(1)\right)p
\]
from every such coloring.

Thus the coloring has \(o(p)\) forbidden instances but is bounded away from the property. \(\square\)

This does **not** disprove the intended higher finite-complexity conjecture. The forms \(x\) and \(2x\) are proportional, so the system has infinite Cauchy–Schwarz complexity. It also varies the group exponent, whereas a theorem over powers of one fixed finite group could have constants depending on that group. It does show that “general abelian groups” needs a precise uniformity and admissibility formulation.

---

# 6. Remaining gap

The unresolved core is still the following regime:

* fixed finite field, or a suitably admissible family of general groups;
* systems of finite complexity at least \(2\);
* an arbitrary finite forbidden family which may use every available color;
* recoloring must stay within the original palette;
* no consensus condition forcing an almost constant coloring.

The safe-color argument fails there because ordinary arithmetic removal only identifies small coordinate deletion sets. Recoloring those points to existing colors can create new forbidden configurations. The consensus results avoid this problem because few violations directly force one color class to have density \(1-o(1)\). Neither mechanism addresses a general induced family.

Accordingly, the catalogued conjecture remains open.