```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained entropy-compression argument proves the conjecture for every maximum degree at least 8 and gives a 16-color bound when the maximum degree is 7.",
  "would_publish": false,
  "caveats": "Degrees 5–7 are not settled here; novelty and the supplied literature have not been independently verified."
}
```

# A degree-8 threshold

Throughout, graphs are finite and simple.

**Theorem.**
1. If \(D\ge 8\) and \(\Delta(G)\le D\), then
   \[
   \chi(G^{3/3})\le 2D+1.
   \]
2. If \(\Delta(G)\le 7\), then
   \[
   \chi(G^{3/3})\le 16.
   \]

Thus the conjecture holds whenever \(\Delta(G)\ge 8\). The second assertion misses the conjectured bound for maximum degree \(7\) by one color.

The palette reduction in the previous attempt is valid and is retained below. Its uniform probability estimates for \(D\ge9\) also survive checking; their verification is included. The improvement at \(D=8\) comes from counting only a necessary feature of **minimal** Hall obstructions, and then using entropy compression with one retained variable.

## 1. The palette reduction

For each edge \(uv\), write its subdivided path as
\[
u-x_{uv}-x_{vu}-v.
\]
Here \(x_{uv}\) is the internal vertex nearest \(u\).

The adjacency rules in \(G^{3/3}\) are:

- Original vertices \(u,v\) are adjacent precisely when \(uv\in E(G)\).
- An original vertex \(w\) is adjacent to \(x_{uv}\) precisely when \(w\in\{u,v\}\).
- Distinct internal vertices \(x_{uv},x_{ab}\) are adjacent precisely when
  \[
  u=a,\qquad v=a,\qquad\text{or}\qquad b=u.
  \]

Let \(\mathcal C\) be a palette. Choose sets \(S(u)\subseteq\mathcal C\), and put
\[
T(u)=\mathcal C\setminus S(u),\qquad
A_u(v)=S(v)\cap T(u)\quad(v\in N(u)).
\]

We seek the following two conditions:
\[
|T(u)|\ge D+1,                                                    \tag{1}
\]
and
\[
\left|\bigcup_{v\in X}A_u(v)\right|\ge |X|+1
\quad
\text{for every }u\text{ and every nonempty }X\subseteq N(u).       \tag{2}
\]

These conditions imply \(\chi(G^{3/3})\le|\mathcal C|\).

Indeed, first greedily color the original graph using
\[
c(u)\in T(u).
\]
Condition (1) guarantees that this is possible. For each \(u\), the lists
\[
A_u(v)\setminus\{c(u)\},\qquad v\in N(u),
\]
satisfy Hall’s condition by (2). Choose distinct representatives, and give \(x_{uv}\) the representative chosen for \(v\).

Internal vertices with the same first coordinate receive distinct colors. Moreover, the colors of \(x_{uv}\) and \(x_{vw}\) lie in \(S(v)\) and \(T(v)\), respectively; the other cross-adjacency is handled similarly. Finally, \(x_{uv}\) avoids \(c(u)\) by construction and avoids \(c(v)\) because its color lies in \(S(v)\).

It therefore remains to construct sets satisfying (1)–(2).

## 2. An entropy-compression lemma

The following elementary form of entropy compression will be useful.

**Lemma 1.** Suppose each of finitely many variables takes values in an alphabet of size \(M\). There are bad events of types \(k=1,\ldots,K\), where a type-\(k\) event involves \(k+1\) variables. Assume:

1. Each variable belongs to at most \(m_k\) type-\(k\) events.
2. After fixing any one variable of a type-\(k\) event to any value, the proportion of assignments to its other \(k\) variables making the event true is at most \(p_k\).

If some \(y>0\) satisfies
\[
1+\sum_{k=1}^K m_kp_ky^k<y,                                     \tag{3}
\]
then there is an assignment avoiding all bad events.

**Proof.**
Order the variables and the bad events. Repeatedly assign the first unassigned variable a new alphabet symbol.

If this creates a fully assigned bad event of type \(k\), choose one deterministically. Retain one of its variables other than the newly assigned variable, and erase the other \(k\) variables. Thus the newly assigned variable is always erased after a failure.

Record:

- the type \(k\);
- the event’s index among the at most \(m_k\) relevant events;
- the rank of the erased assignment among the bad assignments compatible with the retained value.

The last rank has at most
\[
\lfloor p_kM^k\rfloor
\]
possibilities. A successful step has a single record symbol.

Given the record and the final partial assignment, all input symbols can be reconstructed backwards. The sets of assigned variables are recoverable forwards from the record. At a failed step, the retained value and the recorded rank recover all erased values.

Let there be \(N\) variables, and set
\[
a_k=m_k\lfloor p_kM^k\rfloor,\qquad
F(z)=1+\sum_{k=1}^K a_kz^k.
\]
After \(n\) steps, if \(r\) variables remain assigned, the sum of the erasure sizes is \(n-r\). Consequently, for every \(z>0\), the number of possible records is at most
\[
\sum_{r=0}^{N}[z^{\,n-r}]F(z)^n
\le
\left(\frac{F(z)}z\right)^n\sum_{r=0}^{N}z^r.
\]
There are at most \((M+1)^N\) final partial assignments.

If no complete good assignment existed, all \(M^n\) input words would give such records, injectively. This is impossible for arbitrarily large \(n\) when \(F(z)/z<M\).

Taking \(z=y/M\), condition (3) gives
\[
\frac{F(z)}z
\le
\frac M y\left(1+\sum_km_kp_ky^k\right)<M.
\]
This proves the lemma. \(\square\)

## 3. Minimal Hall obstructions

Choose each \(S(u)\) independently and uniformly from the \(s\)-subsets of a palette of size \(q\). Write
\[
t=q-s,\qquad M=\binom qs,
\]
and assume \(t\ge D+1\).

### Edge events

For each \(uv\in E(G)\), let
\[
E_{uv}=\{|S(v)\setminus S(u)|\le1\}.
\]
Since all sets have size \(s\), this event is symmetric in \(u,v\). Its probability is
\[
\alpha=\frac{1+st}{M}.                                           \tag{4}
\]

### Star events

For \(u\in V(G)\) and \(X\subseteq N(u)\), \(|X|=k\ge2\), let \(C_{u,X}\) be the event that

- \(\left|\bigcup_{v\in X}A_u(v)\right|=k\); and
- every color in this union belongs to at least two of the sets \(A_u(v)\).

These events suffice to catch all remaining failures of (2).

To see this, suppose (2) fails, and choose an inclusion-minimal nonempty violating set \(X\). If \(|X|=1\), an edge event occurs. Otherwise, putting \(k=|X|\), minimality gives
\[
\left|\bigcup_{w\in X\setminus\{v\}}A_u(w)\right|\ge k
\quad\text{for every }v\in X.
\]
The full union has size at most \(k\). Hence it has size exactly \(k\), and no color occurs in just one of the sets. Thus \(C_{u,X}\) occurs.

The condition that every union color occurs at least twice is the useful saving over the previous union bound.

### A probability bound

Define
\[
\rho_{s,k}
=
1-(s+1)\left(\frac{k}{s+k}\right)^k.                              \tag{5}
\]
Then
\[
\Pr(C_{u,X})
\le
p_k:=
\binom tk
\left(\frac{\binom{s+k}{s}}{M}\right)^k
\rho_{s,k}^{\,k}.                                                \tag{6}
\]

Here is a proof, including the dependence issue in the final factor.

Condition on \(S(u)\), and fix a \(k\)-set \(Y\subseteq T(u)\). The probability that
\[
S(v)\subseteq S(u)\cup Y
\quad\text{for all }v\in X
\]
is
\[
\left(\frac{\binom{s+k}{s}}{M}\right)^k.
\]
Conditional on this, the \(S(v)\) are independent uniform \(s\)-subsets of an \((s+k)\)-set.

For a fixed \(a\in Y\), the number of these sets containing \(a\) has distribution
\[
\operatorname{Bin}\left(k,\frac{s}{s+k}\right).
\]
Its probability of being at least two is
\[
1-\left(\frac{k}{s+k}\right)^k
-k\frac{s}{s+k}\left(\frac{k}{s+k}\right)^{k-1}
=\rho_{s,k}.
\]

The indicators of membership in a uniform fixed-size subset are negatively associated. Independent products preserve this property. Applying it to the \(k\) increasing events “color \(a\) occurs at least twice,” whose indicator-coordinate sets are disjoint, gives an upper bound \(\rho_{s,k}^k\).

For completeness, the required negative association has a short proof. For increasing functions \(f,g\) on disjoint coordinate sets of one uniform subset, condition on the number \(R\) of selected coordinates in the support of \(f\). Then \(\mathbb E[f\mid R]\) is increasing in \(R\), while the conditional expectation of \(g\) is decreasing in \(R\). Both assertions follow by coupling uniform subsets of consecutive sizes by inclusion. Opposite monotonicity gives
\[
\mathbb E[fg]\le\mathbb E[f]\mathbb E[g].
\]
Closure under independent products follows by conditioning on the factors one at a time.

Finally, sum over the \(\binom tk\) choices of \(Y\). This proves (6).

### Conditioning on a retained variable

All these events are invariant under permutations of the palette. Such permutations act transitively on the possible values of each \(S(u)\). Therefore, for any variable belonging to an event, conditioning that variable to any particular \(s\)-set leaves the event probability unchanged.

Thus (4) and (6) satisfy the conditional-probability hypothesis of Lemma 1, regardless of which variable is retained.

Each variable belongs to at most \(D\) edge events. For \(k\ge2\), it belongs to at most
\[
\binom Dk+D\binom{D-1}{k-1}
=(k+1)\binom Dk                                                  \tag{7}
\]
star events of size \(k+1\).

We have proved the following sufficient numerical criterion.

**Proposition 2.** Put
\[
\begin{aligned}
\Psi_{D,q,s}(y)
={}&D\frac{1+st}{M}\,y\\
&+\sum_{k=2}^{D}(k+1)\binom Dk\binom tk
 \left(
 y\,\rho_{s,k}\frac{\binom{s+k}{s}}{M}
 \right)^k,
\end{aligned}                                                     \tag{8}
\]
where \(t=q-s\) and \(M=\binom qs\).

If \(t\ge D+1\) and
\[
\Psi_{D,q,s}(y)<y-1                                               \tag{9}
\]
for some \(y>0\), then every graph of maximum degree at most \(D\) satisfies
\[
\chi(G^{3/3})\le q.
\]

## 4. The certificates for degrees 8 and 7

For degree \(8\), take
\[
D=8,\qquad q=17,\qquad s=6,\qquad t=11,\qquad
M=12376,\qquad y=\frac54.
\]

For degree \(7\), take
\[
D=7,\qquad q=16,\qquad s=6,\qquad t=10,\qquad
M=8008,\qquad y=\frac43.
\]

The following table gives strict upper bounds on \(1000\) times the individual summands of (8). The first row is the edge-event contribution.

\[
\begin{array}{c|r|r}
\text{term}
& (D,q,s,y)=(8,17,6,5/4)
& (D,q,s,y)=(7,16,6,4/3)\\ \hline
\text{edge}&55&72\\
k=2&12&20\\
k=3&10&19\\
k=4&11&26\\
k=5&17&42\\
k=6&30&69\\
k=7&51&77\\
k=8&55&\text{--}\\ \hline
\text{sum}&241&325
\end{array}
\]

Consequently,
\[
\Psi_{8,17,6}(5/4)<\frac{241}{1000}<\frac14,
\]
and
\[
\Psi_{7,16,6}(4/3)<\frac{325}{1000}<\frac13.
\]
Proposition 2 proves
\[
\boxed{\Delta(G)\le8\ \Longrightarrow\ \chi(G^{3/3})\le17}
\]
and
\[
\boxed{\Delta(G)\le7\ \Longrightarrow\ \chi(G^{3/3})\le16.}
\]

These are rational inequalities, not floating-point estimates. A complete exact-arithmetic verifier is supplied in Section 6.

## 5. Uniform verification for all \(D\ge9\)

This section checks and reuses the probability estimates from the previous attempt. No asymptotic literature result is needed.

Set
\[
q=2D+1,\qquad s=D-2,\qquad t=D+3,\qquad
M_D=\binom{2D+1}{D-2},
\]
and define
\[
\alpha_D=\frac{D^2+D-5}{M_D},
\]
\[
F_{D,k}
=
\binom Dk\binom{D+3}k
\left(
\frac{\binom{D+k-2}{D-2}}{M_D}
\right)^k,
\qquad
\beta_D=\sum_{k=2}^{D}F_{D,k}.
\]

We will establish
\[
\alpha_D<\frac1{6D^2},
\qquad
\beta_D<\frac1{4(D^2+1)}
\quad(D\ge9).                                                    \tag{10}
\]

### 5.1. These estimates imply the coloring bound

Take
\[
y=1+\frac1D.
\]
Since \(0\le\rho_{s,k}\le1\), equation (8) gives
\[
\Psi_{D,2D+1,D-2}(y)
\le D\alpha_Dy+(D+1)y^D\beta_D.
\]
Using (10),
\[
D\Psi_{D,2D+1,D-2}(y)
<
\frac y6+
\frac{D(D+1)}{4(D^2+1)}y^D.
\]
For \(D\ge9\),
\[
y\le\frac{10}{9},\qquad
\frac{D(D+1)}{D^2+1}<\frac{10}{9},\qquad
y^D<e<\frac{11}{4}.
\]
Therefore
\[
D\Psi_{D,2D+1,D-2}(y)
<
\frac{10}{9}\left(\frac16+\frac{11}{16}\right)
=\frac{205}{216}<1.
\]
Thus \(\Psi(y)<1/D=y-1\), as required by Proposition 2.

### 5.2. The edge-event estimate

At \(D=9\),
\[
M_9=50388,\qquad
\alpha_9=\frac{85}{50388}<\frac1{486}.
\]
Moreover,
\[
\frac{(D+1)^2\alpha_{D+1}}{D^2\alpha_D}
=
\frac{(D+1)^2}{D^2}
\frac{D^2+3D-3}{D^2+D-5}
\frac{(D-1)(D+4)}{(2D+3)(2D+2)}.
\]
For \(D\ge9\), the first two factors are each less than \(5/4\), and the last is less than \(1/3\). The ratio is less than \(25/48<1\), proving the first inequality in (10).

### 5.3. The initial estimate for \(\beta_D\)

At \(D=9\), the following are strict upper bounds on \(10^6F_{9,k}\):
\[
\begin{array}{c|rrrrrrrr}
k&2&3&4&5&6&7&8&9\\ \hline
10^6F_{9,k}\text{ upper bound}
&1300&260&120&100&130&210&330&380.
\end{array}
\]
Thus
\[
\beta_9<\frac{2830}{10^6}<\frac3{1000}.                            \tag{11}
\]

### 5.4. A uniform contraction

We prove
\[
\beta_{D+1}\le\frac45\beta_D\qquad(D\ge9).                         \tag{12}
\]

Put \(h=\lfloor(D+3)/2\rfloor\). First, for \(2\le k\le h\),
\[
\frac{F_{D+1,k}}{F_{D,k}}
=
\frac{(D+1)(D+4)}
 {(D+1-k)(D+4-k)}
\left(
\frac{(D+k-1)(D+4)}
 {(2D+3)(2D+2)}
\right)^k.                                                       \tag{13}
\]
The factor inside parentheses is at most \(1/2\). The prefactor is at most \(5\); for \(k=2\) it is less than \(3/2\), and for \(k=3\) it is less than \(2\). Hence
\[
F_{D+1,k}\le\frac25F_{D,k}\qquad(2\le k\le h).                    \tag{14}
\]

For the other half, put \(r=D+3-k\). Then
\[
F_{D,D+3-r}
=
\binom D{r-3}\binom{D+3}r
\left(\frac{(D+3)_r}{(2D+1)_r}\right)^{D+3-r},                    \tag{15}
\]
where \((a)_r\) denotes a falling factorial.

For fixed \(r\), define
\[
L_r(z)
=(z+3-r)\sum_{j=0}^{r-1}
\log\frac{z+3-j}{2z+1-j}.
\]
The derivative of its \(j\)-th summand is
\[
\log\frac{z+3-j}{2z+1-j}
+
\frac{(z+3-r)(j-5)}
 {(z+3-j)(2z+1-j)}.                                              \tag{16}
\]

For \(z\ge D\ge9\), the expression in (16) is at most \(\log(2/3)\) when \(j<5\). When \(j\ge5\), put
\[
a=\frac{j-5}{2z+1-j}.
\]
Since \(j\le r-1\), expression (16) is at most
\[
\log\frac{1-a}{2}+a\le-\log2.
\]
It follows that
\[
\exp(L_r(D+1)-L_r(D))
\le
\left(\frac23\right)^{\min(r,5)}
2^{-\max(r-5,0)}.                                                \tag{17}
\]

For \(h\le k\le D\), one has \(3\le r\le(D+4)/2\). The ratio of the binomial prefactors in (15) is
\[
\frac{(D+1)(D+4)}{(D+4-r)^2}.
\]
It is at most \(4/3,2,3\) for \(r=3,4,5\), respectively, and at most \(4\) for \(r\ge6\). Combining this with (17), the full ratio is at most \(32/81<2/5\) for \(r=3,4,5\), and at most \(64/243<2/5\) for \(r\ge6\). Therefore
\[
F_{D+1,k+1}\le\frac25F_{D,k}\qquad(h\le k\le D).                  \tag{18}
\]

Summing (14) and (18),
\[
\beta_{D+1}
\le\frac25\bigl(\beta_D+F_{D,h}\bigr)
\le\frac45\beta_D,
\]
proving (12).

Finally,
\[
\frac45\bigl((D+1)^2+1\bigr)\le D^2+1\qquad(D\ge9).
\]
Consequently, by (11)–(12),
\[
(D^2+1)\beta_D
\le82\beta_9
<82\cdot\frac3{1000}
<\frac14.
\]
This proves the second inequality in (10), and completes the proof for every \(D\ge9\).

Together with Section 4, the theorem is proved.

## 6. Exact verification of the numerical certificates

The following complete verifier checks both finite tables using rational arithmetic only. No search over graphs is involved.

```python
from math import comb
from fractions import Fraction as F

def entropy_terms(D, q, s, y):
    t = q - s
    M = comb(q, s)
    assert t >= D + 1

    terms = [F(D * (1 + s*t), M) * y]
    for k in range(2, D + 1):
        rho = F(1) - (s + 1) * F(k, s + k)**k
        term = (
            (k + 1) * comb(D, k) * comb(t, k)
            * (y * rho * F(comb(s + k, s), M))**k
        )
        terms.append(term)
    return terms

certificates = [
    (8, 17, 6, F(5, 4), [55, 12, 10, 11, 17, 30, 51, 55]),
    (7, 16, 6, F(4, 3), [72, 20, 19, 26, 42, 69, 77]),
]

for D, q, s, y, bounds in certificates:
    terms = entropy_terms(D, q, s, y)
    assert len(terms) == len(bounds)
    assert all(a < F(b, 1000) for a, b in zip(terms, bounds))
    assert sum(terms) < y - 1

# Base table for the uniform D >= 9 argument.
bounds9 = [1300, 260, 120, 100, 130, 210, 330, 380]
M9 = comb(19, 7)
beta9 = F(0)

for k, b in zip(range(2, 10), bounds9):
    term = F(
        comb(9, k) * comb(12, k) * comb(7 + k, 7)**k,
        M9**k
    )
    assert term < F(b, 10**6)
    beta9 += term

assert beta9 < F(3, 1000)
```

## 7. What remains unresolved

The unconditional conclusion proved here is
\[
\boxed{
\chi(G^{3/3})\le2\Delta(G)+1
\quad\text{whenever }\Delta(G)\ge8.
}
\]

For maximum degree \(7\), the argument gives \(16\), not the required \(15\). It does not settle maximum degrees \(5\) or \(6\).

Taking the degree-\(3\) and degree-\(4\) results reported in the question as given, and noting that degree \(2\) is elementary, the remaining degree values are therefore
\[
\boxed{\Delta\in\{5,6,7\}.}
\]

I make no claim that this threshold or the auxiliary 16-color bound is new in the literature. The improvement established here relative to the supplied attempt is the degree-\(8\) case.