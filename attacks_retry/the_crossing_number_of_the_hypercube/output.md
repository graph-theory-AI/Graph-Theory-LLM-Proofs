```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A strengthened doubling inequality proves convergence and makes a drawing of Q_7 with at most 1687 crossings a finite certificate against the proposed limit, but no qualifying drawing is constructed.",
  "would_publish": false,
  "caveats": "No improvement to the quoted asymptotic interval; novelty and the full formulas in the later literature have not been checked."
}
```

# A strengthened amplification bound

I do **not** determine whether the limit is \(5/32\).

I independently checked the vertex-splitting construction in the supplied attempt, including its strand-order obstruction. There is an additional optimization: at a vertex, one may choose not only which new vertex receives label \(0\), but also **which consecutive half of the incident ports lies on each side of the split**. Exploiting this improves the universal doubling inequality.

The resulting partial conclusions are:

1. The normalized crossing numbers converge.
2. Their limit has an explicit upper envelope defined by finite sign-word optimizations.
3. A drawing of \(Q_7\) with at most **1687 crossings** would disprove the proposed value. This improves the sufficient target of 1657 in the supplied attempt.

No drawing meeting the new target is produced here.

## 1. The local optimization

Let
\[
\epsilon_d=
\begin{cases}
0,&d\text{ even},\\
1,&d\text{ odd},
\end{cases}
\qquad
f(d)=
\binom{\lfloor d/2\rfloor}{2}
+\binom{\lceil d/2\rceil}{2}
=\frac{d^2-2d+\epsilon_d}{4}.
\]

Index \(d\) positions cyclically. Let \(\mathcal P_d\subseteq\{-1,1\}^d\) consist of the sign words whose positive positions form a cyclic interval of length \(\lfloor d/2\rfloor\), together with the negatives of all these words. Thus, for odd \(d\), both possible balanced interval lengths are allowed.

For independent uniform signs \(X_1,\dots,X_d\), define
\[
M_d=
\mathbb E\left[
\max_{p\in\mathcal P_d}\sum_{i=1}^d p_iX_i
\right].                                                   \tag{1}
\]
Equivalently, if
\[
D_d(x)=\min_{p\in\mathcal P_d}
\bigl|\{i:x_i\ne p_i\}\bigr|,
\]
then
\[
M_d=d-2\mathbb E D_d(X).                                   \tag{2}
\]

These are explicitly computable rational numbers. Because \(\mathcal P_d\) contains a word and its negative,
\[
d\ge M_d\ge \mu_d,
\qquad
\mu_d:=\mathbb E|X_1+\cdots+X_d|\ge1.                       \tag{3}
\]

## 2. A doubling lemma for regular bipartite graphs

**Lemma.** Let \(G\) be a finite simple \(d\)-regular bipartite graph, with \(N\) vertices and \(d\ge1\). Then
\[
\boxed{
\operatorname{cr}(G\square K_2)
\le
4\operatorname{cr}(G)
+\frac N4\bigl(d^2-d+\epsilon_d-M_d\bigr).
}                                                          \tag{4}
\]

### Proof

Take a crossing-minimal drawing of \(G\) in general position. Choose small, disjoint vertex disks and crossing disks, with narrow corridors following the remaining edge segments.

#### The construction inside a vertex disk

Replace an old vertex \(v\) by two nearby vertices \(v^0,v^1\), and replace each incident edge by one strand from each new vertex. Also draw the new edge \(v^0v^1\).

The local strands can be arranged with exactly \(f(d)\) crossings, while leaving \(v^0v^1\) uncrossed. To see this, put the two new vertices at \((-\eta,0)\) and \((\eta,0)\). Choose \(\lfloor d/2\rfloor\) ray directions in the upper half-plane and the remaining directions in the lower half-plane, and draw a ray in every chosen direction from each new vertex.

For two distinct directions in the same half-plane, exactly one cross-pair of rays intersects. Directions in opposite half-planes produce no intersection, and the two rays in the same direction are parallel. Taking \(\eta\) sufficiently small puts all these intersections inside the disk. Their number is \(f(d)\).

The two strands for each old edge exit as an adjacent pair. The old cyclic order of the edge ports can be preserved by connecting these pairs through an annulus.

Crucially, the choice of the consecutive upper group is arbitrary. Around the boundary of the disk, the order of labels within a strand pair is one way on this group and the opposite way on its complement. Exchanging \(v^0,v^1\) reverses every pair order. Consequently, every pattern in \(\mathcal P_d\) is available, always at the same local cost \(f(d)\).

#### Old crossings and corridor twists

At every old crossing, the two strands replacing one edge cross the two strands replacing the other, giving four crossings.

Along an old edge, prescribed orders at its ends can be joined either without a crossing or with one crossing between the two strands. Call the latter a twist. If there are \(t\) twists, the total is at most
\[
4\operatorname{cr}(G)+Nf(d)+t.                             \tag{5}
\]

It remains to choose the local patterns to bound \(t\).

#### Choosing patterns using the bipartition

Write the bipartition as \(A\cup B\). Since \(G\) is \(d\)-regular and \(d>0\),
\[
|A|=|B|=N/2.
\]

At each vertex of \(A\), fix any balanced cyclic split and independently choose its overall label switch uniformly at random.

Now consider a vertex \(v\in B\). Transporting the chosen strand orders from its neighbors along the edge corridors determines a desired sign word
\[
X(v)\in\{-1,1\}^d
\]
at \(v\): matching this word would make all its incident corridors untwisted. Its entries are independent uniform signs, because \(G\) is simple and its \(d\) neighbors received independent switches.

Choose the local pattern at \(v\) from \(\mathcal P_d\) to minimize its number of mismatches with \(X(v)\). By (2), its expected number of incident twists is
\[
\frac{d-M_d}{2}.
\]
Each old edge is counted at exactly one vertex of \(B\). Linearity of expectation therefore gives a choice with
\[
t\le \frac N4(d-M_d).
\]
Substitution in (5) proves (4). All crossings are accounted for: local vertex crossings, four per old crossing, and corridor twists. ∎

The improvement over the supplied attempt is precisely the maximization over all balanced cyclic splits, rather than only a fixed split and its label reversal.

## 3. Convergence and the sharpened envelope

Write
\[
c_d=\operatorname{cr}(Q_d),
\qquad
a_d=\frac{c_d}{4^d}.
\]
Applying (4) to \(Q_d\) gives
\[
\boxed{
c_{d+1}\le
4c_d+2^{d-2}\bigl(d^2-d+\epsilon_d-M_d\bigr).
}                                                          \tag{6}
\]

Define
\[
e_d=\frac{d^2-d+\epsilon_d-M_d}{2^{d+4}},
\qquad
E_d=\sum_{k=d}^{\infty}e_k.                                \tag{7}
\]
The terms \(e_d\) are nonnegative: their numerators equal
\[
4f(d)+(d-M_d)\ge0.
\]
They are also summable, being \(O(d^2 2^{-d})\).

Dividing (6) by \(4^{d+1}\) gives
\[
a_{d+1}\le a_d+e_d.
\]
Since \(E_d=e_d+E_{d+1}\),
\[
a_{d+1}+E_{d+1}\le a_d+E_d.
\]
Thus \(a_d+E_d\) is nonnegative and nonincreasing. As \(E_d\to0\), this proves the following.

**Theorem.** The limit
\[
L=\lim_{d\to\infty}\frac{\operatorname{cr}(Q_d)}{4^d}
\]
exists, and
\[
\boxed{
L=\inf_{d\ge1}
\left(\frac{\operatorname{cr}(Q_d)}{4^d}+E_d\right).
}                                                          \tag{8}
\]
In particular, every drawing of \(Q_d\) with \(C\) crossings gives
\[
\boxed{L\le \frac{C}{4^d}+E_d.}                             \tag{9}
\]

For comparison, (3) implies
\[
E_d\le
\sum_{k=d}^{\infty}
\frac{k^2-k-1+\epsilon_k}{2^{k+4}}
=
\frac{d^2+d+(4+\epsilon_d)/3}{2^{d+3}}.                      \tag{10}
\]
Thus the closed-form envelope in the supplied attempt is recovered, while (7) strengthens it.

## 4. A concrete target: 1687 crossings for \(Q_7\)

Here are the finite constants needed:
\[
\begin{array}{c|c|c}
d&M_d&\mu_d\\ \hline
7&137/32&35/16\\
8&29/8&35/16\\
9&635/128&315/128\\
10&137/32&315/128
\end{array}                                                \tag{11}
\]

For completeness, the distributions of \(D_d(X)\), listed as counts rather than probabilities, are
\[
\begin{array}{c|rrrrrr}
d&D=0&D=1&D=2&D=3&D=4&D=5\\ \hline
7&14&56&56&2&0&0\\
8&8&48&104&80&16&0\\
9&18&108&234&150&2&0\\
10&10&80&260&400&242&32
\end{array}
\]
Each row sums to \(2^d\); equation (2) gives (11).

These are small sign-word enumerations, not searches for cube drawings. The following complete Python verifier checks every word involved:

```python
from fractions import Fraction

def cyclic_split_data(d):
    full = (1 << d) - 1
    p = d // 2
    patterns = set()

    for start in range(d):
        w = sum(1 << ((start + j) % d) for j in range(p))
        patterns.add(w)
        patterns.add(full ^ w)

    hist = [0] * (d + 1)
    for x in range(1 << d):
        distance = min((x ^ w).bit_count() for w in patterns)
        hist[distance] += 1

    M = Fraction(
        sum((d - 2*r) * hist[r] for r in range(d + 1)),
        1 << d
    )
    return hist, M

expected = {
    7:  ([14, 56, 56, 2, 0, 0, 0, 0], Fraction(137, 32)),
    8:  ([8, 48, 104, 80, 16, 0, 0, 0, 0], Fraction(29, 8)),
    9:  ([18, 108, 234, 150, 2, 0, 0, 0, 0, 0],
         Fraction(635, 128)),
    10: ([10, 80, 260, 400, 242, 32, 0, 0, 0, 0, 0],
         Fraction(137, 32)),
}

for d, answer in expected.items():
    assert cyclic_split_data(d) == answer
```

### Bounding the infinite tail

Set
\[
U_d=
\sum_{k=d}^{\infty}
\frac{k^2-k+\epsilon_k-\mu_k}{2^{k+4}}.
\]
By (3), \(E_d\le U_d\). We first evaluate \(U_7\), then subtract the improvements in (11).

For a simple symmetric random walk \(S_k\),
\[
\mu_k-\mu_{k-1}=\Pr(S_{k-1}=0).
\]
Therefore
\[
\sum_{k\ge1}\mu_k x^k
=\frac{x}{(1-x)\sqrt{1-x^2}}.
\]
In particular,
\[
\sum_{k\ge1}\frac{\mu_k}{2^k}=\frac2{\sqrt3},
\qquad
\sum_{k=1}^{6}\frac{\mu_k}{2^k}=\frac{573}{512}.
\]
Also, elementary geometric-series summation gives
\[
\sum_{k=7}^{\infty}\frac{k^2-k+\epsilon_k}{2^k}
=\frac{11}{12}.
\]
Consequently,
\[
4^7U_7
=
2^{10}\left(\frac{11}{12}
-\frac2{\sqrt3}+\frac{573}{512}\right)
=
\frac{6254}{3}-\frac{2048}{\sqrt3}.                         \tag{12}
\]

Using the improvements \(M_k-\mu_k\) for \(7\le k\le10\),
\[
\begin{aligned}
4^7E_7
&\le 4^7U_7-
\sum_{k=7}^{10}2^{10-k}(M_k-\mu_k)\\
&=
\frac{6254}{3}-\frac{2048}{\sqrt3}
-\left(\frac{67}{4}+\frac{23}{4}+5+\frac{233}{128}\right)\\
&=
\frac{6254}{3}-\frac{2048}{\sqrt3}-\frac{3753}{128}.
\end{aligned}                                             \tag{13}
\]

Since \((5/32)4^7=2560\), equation (9) proves \(L<5/32\) whenever a drawing of \(Q_7\) has
\[
C<
\frac{1426}{3}+\frac{2048}{\sqrt3}+\frac{3753}{128}
\approx1687.066997.                                        \tag{14}
\]

The strict comparison with 1687 does not depend on decimal rounding. Indeed, \(\sqrt3<97/56\), and
\[
\frac{1426}{3}+\frac{3753}{128}+\frac{114688}{97}
=
1687+\frac{155}{37248}>1687.
\]

We have therefore proved the finite certificate:

\[
\boxed{
\text{If \(Q_7\) has a drawing with at most \(1687\) crossings,
then \(L<5/32\).}
}                                                          \tag{15}
\]

## 5. What remains unresolved

The Erdős–Guy expression at dimension seven is
\[
\frac5{32}4^7-\left\lfloor\frac{7^2+1}{2}\right\rfloor2^5
=1760.
\]
A strict improvement over that expression, without its magnitude being specified, does not guarantee the threshold (15). I have not independently inspected the full later-paper constructions, so I make no claim about whether they meet this or another amplification threshold.

The argument establishes convergence and strengthens a universal finite-drawing bound. It supplies neither:

- a lower bound approaching \((5/32)4^d\), nor
- an actual drawing that forces a smaller limit.

Taking the asymptotic bounds quoted in the question as premises, the numerical interval remains
\[
\frac1{20}\le L\le\frac5{32}.
\]
The value of \(L\) is not settled here.