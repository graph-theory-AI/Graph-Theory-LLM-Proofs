```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Ear-incidence and common-neighbor estimates extend the fourth-moment approach to maximum degrees 23 and 7, respectively, and give stronger results for 5-connected triangulations.",
  "would_publish": false,
  "caveats": "Neither conjecture is settled in full; no exhaustive computation or independent literature-status verification was performed."
}
```

# 1. Results obtained

Write
\[
s^+(G)=\sum_{\lambda_i(G)>0}\lambda_i(G)^2.
\]

I prove the following special cases.

### Theorem A — maximal outerplanar graphs

Let \(G\) be maximal outerplanar of order \(n\). Then \(s^+(G)\ge 2n\) in each of these regimes:
\[
\boxed{\Delta(G)\le22,\qquad n\ge159;}
\]
\[
\boxed{\Delta(G)\le23,\qquad n\ge60000.}
\]

The main new ingredient is the degree-square estimate
\[
\boxed{
\sum_v d(v)^2
\le
\frac{(4D^2+22D-116)n-18D^2+192}{3D-10}
}
\tag{1}
\]
for maximal outerplanar graphs of order at least \(5\) and maximum degree at most \(D\ge4\).

### Theorem B — maximal planar graphs

Let \(G\) be maximal planar of order \(n\). Then \(s^+(G)\ge3n\) whenever
\[
\boxed{\Delta(G)\le6,\qquad n\ge27,}
\]
or
\[
\boxed{\Delta(G)\le7,\qquad n\ge152.}
\]

These improve the supplied attempt’s bounded-degree planar result.

### Theorem C — 5-connected maximal planar graphs

If \(G\) is 5-connected and maximal planar, with \(\Delta(G)\le D\), then
\[
\boxed{
(141-2D)n+24D-1980+\frac{3072}{n}\ge0
\quad\Longrightarrow\quad s^+(G)\ge3n.
}
\tag{2}
\]

Consequently, the conjecture holds for:

* every such graph with \(\Delta(G)\le70\) and \(n\ge290\);
* every such graph with \(\Delta(G)\le6\), at every possible order;
* every 5-connected maximal planar graph with
  \[
  \boxed{12\le n\le139,}
  \]
  without a maximum-degree restriction.

I independently rederive the variational certificate from the supplied attempt. The advances below are the ear-incidence estimate (1), a sharper common-neighbor bound for triangulations, and the 5-connected analysis. The supplied family computations are not used.

---

# 2. The spectral certificate

For a real symmetric matrix \(A\), let \(A_+\) denote its positive part.

## Lemma 2.1

\[
\operatorname{tr}(A_+^2)
=
\max_{X\succeq0}
\left(2\operatorname{tr}(AX)-\operatorname{tr}(X^2)\right).
\tag{3}
\]

### Proof

Completing the square,
\[
2\operatorname{tr}(AX)-\operatorname{tr}(X^2)
=
\operatorname{tr}(A^2)-\|A-X\|_F^2.
\]
The nearest positive semidefinite matrix to \(A\) in Frobenius norm is \(A_+\), as follows directly by diagonalizing \(A\). Substitution proves (3). ∎

For a graph, write
\[
m=|E(G)|,\qquad \tau=\#\{\text{triangles}\},\qquad
W_4=\operatorname{tr}(A^4).
\]

## Lemma 2.2

For every \(a\ge0\),
\[
\boxed{
s^+(G)\ge
\frac{(6\tau+4am)^2}
{W_4+24a\tau+12a^2m+a^4n}.
}
\tag{4}
\]

### Proof

Use \(X=t(A+aI)^2\succeq0\) in (3). Since
\[
\operatorname{tr}\bigl(A(A+aI)^2\bigr)=6\tau+4am
\]
and
\[
\operatorname{tr}(A+aI)^4
=W_4+24a\tau+12a^2m+a^4n,
\]
optimization over \(t\ge0\) gives (4). ∎

We also use
\[
\boxed{
W_4=2\sum_v d(v)^2-2m+8c_4(G),
}
\tag{5}
\]
where \(c_4(G)\) counts all, not necessarily induced, 4-cycles.

---

# 3. An ear-incidence bound for maximal outerplanar graphs

Fix a maximal outerplanar graph \(G\) of order \(n\ge5\), and put
\[
S=\sum_vd(v)^2.
\]
Let \(t\) and \(u\) be the numbers of vertices of degree \(2\) and \(3\), respectively.

## Lemma 3.1

\[
\boxed{4t+u\le2n.}
\tag{6}
\]

### Proof

Use an outerplane embedding whose outer boundary is the Hamiltonian cycle of \(G\).

A degree-2 vertex has precisely its two boundary neighbors as neighbors. Thus:

1. two degree-2 vertices cannot be adjacent when \(n\ge4\);
2. any vertex has at most two degree-2 neighbors.

Moreover, a degree-3 vertex has at most one degree-2 neighbor when \(n\ge5\). Indeed, suppose its two boundary neighbors \(x,y\) both have degree \(2\). Its third neighbor \(w\) lies between \(x,y\) in its neighborhood path, so both \(x\) and \(y\) are adjacent to \(w\). Since \(x,y\) have degree \(2\), the outer boundary is then the 4-cycle \(w,x,v,y,w\), contradicting \(n\ge5\).

Count incidences between degree-2 vertices and their neighbors. There are \(2t\) incidences. Degree-3 vertices receive at most one each, and vertices of degree at least \(4\) receive at most two each. Therefore
\[
2t\le u+2(n-t-u),
\]
which is (6). ∎

## Lemma 3.2

If \(\Delta(G)\le D\), where \(D\ge4\), then
\[
S\le
\frac{(4D^2+22D-116)n-18D^2+192}{3D-10}.
\tag{7}
\]

### Proof

Since \(G\) is maximal outerplanar,
\[
\sum_vd(v)=4n-6.
\]
For \(4\le d\le D\),
\[
d^2\le(D+4)d-4D.
\]
Accounting separately for degrees \(2,3\) gives
\[
S\le16n-6D-24+2(D-2)t+(D-3)u.
\tag{8}
\]

The degree sum also implies
\[
4n-6\le2t+3u+D(n-t-u),
\]
hence
\[
(D-2)t+(D-3)u\le(D-4)n+6.
\tag{9}
\]

Set
\[
\alpha=\frac{(D-2)(D-3)}{3D-10},
\qquad
\beta=\frac{2(D-4)}{3D-10}.
\]
Both are nonnegative, and
\[
\begin{aligned}
2(D-2)t+(D-3)u
&=\alpha(4t+u)
 +\beta\bigl((D-2)t+(D-3)u\bigr)\\
&\le2\alpha n+\beta((D-4)n+6),
\end{aligned}
\]
by (6) and (9). Substitution into (8) and simplification yield (7). ∎

The improvement over using only the minimum and maximum degrees is important: the latter allows far too many degree-2 vertices together with degree-3 vertices. Inequality (6) excludes that configuration.

---

# 4. Proof of Theorem A

For a maximal outerplanar graph,
\[
m=2n-3,\qquad \tau=n-2,\qquad c_4=n-3.
\tag{10}
\]

For completeness, every 4-cycle has exactly one chord: its interior must be triangulated, and two chords would give a \(K_4\), which is not outerplanar. Its two triangles are the faces incident with that chord. Thus 4-cycles correspond to the \(n-3\) internal diagonals.

By (5),
\[
W_4=2S+4n-18.
\tag{11}
\]

Substituting (10)–(11) into (4), and rearranging the condition that the resulting lower bound be at least \(2n\), gives the following sufficient condition:
\[
\boxed{
S\le R_a(n),
}
\tag{12}
\]
where
\[
R_a(n)=
\left(7+12a+4a^2-\frac{a^4}{2}\right)n
-27-60a-30a^2
+\frac{36(1+a)^2}{n}.
\tag{13}
\]

## 4.1 Maximum degree at most \(22\)

Taking \(D=22\) in (7),
\[
S\le\frac{288}{7}n-\frac{1065}{7}.
\tag{14}
\]
Taking \(a=5/2\) in (13),
\[
R_{5/2}(n)
=\frac{1359}{32}n-\frac{729}{2}+\frac{441}{n}.
\]
The difference between this expression and the right side of (14) is
\[
\frac{297}{224}n-\frac{2973}{14}+\frac{441}{n}.
\]
It is nonnegative exactly when
\[
99n^2-15856n+32928\ge0.
\tag{15}
\]
At \(n=159\), the left side of (15) is \(14643>0\), and its derivative is positive for all \(n\ge159\). Thus (12) holds whenever \(n\ge159\).

This proves the first assertion of Theorem A.

## 4.2 Maximum degree at most \(23\)

Taking \(D=23\) in (7),
\[
S\le\frac{2506n-9330}{59}.
\tag{16}
\]
Choose
\[
a=\frac{101}{40}.
\]
An exact subtraction gives
\[
R_a(n)-\frac{2506n-9330}{59}
=
\frac{1095541}{302080000}n
-\frac{1997817}{9440}
+\frac{178929}{400n}.
\]
Now
\[
\frac{1095541}{302080000}>\frac9{2500},
\qquad
\frac{1997817}{9440}<212.
\]
Consequently,
\[
R_a(n)-\frac{2506n-9330}{59}
>
\frac9{2500}n-212.
\]
For \(n\ge60000\), the last expression is at least \(4\). Applying (12) proves the second assertion. ∎

---

# 5. Sharper fourth-moment control for triangulations

Let \(G\) be maximal planar of order \(n\ge4\), with maximum degree at most \(D\). Again write
\[
S=\sum_vd(v)^2.
\]

For distinct vertices \(x,y\), put
\[
c_{xy}=|N(x)\cap N(y)|.
\]
Then
\[
2c_4(G)=\sum_{\{x,y\}}\binom{c_{xy}}2,
\qquad
\sum_{\{x,y\}}c_{xy}=\sum_v\binom{d(v)}2,
\tag{17}
\]
and
\[
\sum_{xy\in E(G)}c_{xy}=3\tau.
\tag{18}
\]

## Lemma 5.1

\[
\boxed{
W_4\le (D+1)S-(6D-4)m+6\tau.
}
\tag{19}
\]

### Proof

If \(xy\) is an edge, its two incident triangular faces show that \(c_{xy}\ge2\), while \(c_{xy}\le D-1\). Hence
\[
\binom{c_{xy}}2
\le\frac D2c_{xy}-(D-1).
\tag{20}
\]
For a nonedge,
\[
\binom{c_{xy}}2\le\frac{D-1}{2}c_{xy}.
\tag{21}
\]

Summing (20)–(21), and using (17)–(18), yields
\[
2c_4(G)
\le
\frac{D-1}{4}S-\frac32(D-1)m+\frac32\tau.
\]
Now apply (5). ∎

Because every vertex of a maximal planar graph has degree at least \(3\),
\[
d^2\le(D+3)d-3D.
\]
Therefore
\[
S\le(3D+18)n-12D-36.
\tag{22}
\]
Using \(m=3n-6\), Lemma 5.1 gives
\[
W_4\le U_D(n)+6\tau,
\tag{23}
\]
where
\[
U_D(n)=(3D^2+3D+30)n-12D^2-12D-60.
\tag{24}
\]

This bound keeps track of the triangle count rather than discarding its contribution.

---

# 6. Proof of Theorem B

Inserting (23) into (4) gives
\[
s^+(G)\ge
\frac{(6\tau+4am)^2}
{U_D(n)+(6+24a)\tau+12a^2m+a^4n}.
\tag{25}
\]

For \(a\ge1/2\), the right side is increasing in \(\tau\). Here is an explicit check. After removing a positive factor, the derivative has numerator
\[
12U_D(n)
+6(6+24a)\tau
+24a(2a-1)m
+12a^4n,
\]
which is positive: \(U_D(n)>0\) for \(n\ge4\).

Every maximal planar graph has at least \(2n-4\) triangles. Thus (25) implies
\[
s^+(G)\ge
\frac{144(1+a)^2(n-2)^2}
{
\begin{aligned}
&(3D^2+3D+42+48a+36a^2+a^4)n\\
&\qquad{}-12D^2-12D-84-96a-72a^2
\end{aligned}
}.
\tag{26}
\]

## 6.1 Maximum degree at most \(7\)

Set \(D=7\) and \(a=3\). Equation (26) becomes
\[
s^+(G)\ge
\frac{2304(n-2)^2}{759n-1692}.
\tag{27}
\]
The right side is at least \(3n\) precisely when
\[
9n^2-1380n+3072\ge0.
\tag{28}
\]
At \(n=152\), the left side is \(1248>0\), and it is increasing thereafter. This proves the second assertion of Theorem B.

## 6.2 Maximum degree at most \(6\)

Set \(D=6\) and \(a=11/4\) in (26). The condition that this lower bound be at least \(3n\) simplifies to
\[
\frac{11663}{256}n-\frac{2607}{2}+\frac{2700}{n}\ge0.
\tag{29}
\]
At \(n=27\), its left side is
\[
\frac{6805}{256}>0.
\]
Its derivative,
\[
\frac{11663}{256}-\frac{2700}{n^2},
\]
is positive for \(n\ge27\). Thus (29) holds throughout that range. ∎

---

# 7. The 5-connected case

Here the topology gives substantially sharper information.

## Lemma 7.1

If \(G\) is a 5-connected maximal planar graph, then
\[
\tau=2n-4,\qquad c_4(G)=3n-6.
\tag{30}
\]

### Proof

Every triangle is facial: otherwise its three vertices separate vertices on its two sides.

There is no induced 4-cycle. In a triangulation, each side of a chordless 4-cycle must contain a vertex; otherwise that side would need a diagonal. Its four vertices would therefore be a vertex cut.

Also, \(G\) has no \(K_4\) subgraph. For \(n>4\), such a subgraph forces a separating triangle.

Consequently every 4-cycle has exactly one chord. Its two triangles are facial, so the 4-cycle is the union of the two faces incident with its unique chord. Conversely, every edge produces such a 4-cycle. This is a bijection between edges and 4-cycles, proving (30). ∎

By (5),
\[
W_4=2S+18n-36.
\tag{31}
\]
The minimum degree is at least \(5\). If \(\Delta(G)\le D\), then
\[
S\le(D+5)(6n-12)-5Dn
=(D+30)n-12D-60.
\]
Thus
\[
\boxed{
W_4\le(2D+78)n-24D-156.
}
\tag{32}
\]

For a triangulation with \(\tau=2n-4\), taking \(a=3\) in (4) proves \(s^+(G)\ge3n\) whenever
\[
W_4\le219n-2136+\frac{3072}{n}.
\tag{33}
\]
Combining (32)–(33) gives exactly (2), proving the main assertion of Theorem C.

### Consequence: \(\Delta\le70,\ n\ge290\)

Use \(D=70\) in (2). The condition is
\[
n-300+\frac{3072}{n}\ge0.
\]
Equivalently,
\[
n^2-300n+3072\ge0.
\]
Its value at \(290\) is \(172>0\), and it increases thereafter.

### Consequence: every order when \(\Delta\le6\)

Taking \(a=2\) in (4), rather than \(a=3\), gives the sufficient condition
\[
W_4\le176n-1248+\frac{1728}{n}.
\tag{34}
\]
With \(D=6\), (32) and (34) reduce this to
\[
86n-948+\frac{1728}{n}\ge0.
\]
A 5-connected planar graph has \(n\ge12\), and the last expression is positive and increasing for \(n\ge12\).

---

# 8. All 5-connected triangulations through order \(139\)

The degree restriction can be removed over a finite interval without enumerating graphs.

## Lemma 8.1

For a 5-connected maximal planar graph,
\[
\boxed{\Delta(G)\le\frac{n-1}{2}.}
\tag{35}
\]

### Proof

Fix a vertex \(v\) of degree \(d\). Its neighbors induce a chordless cycle: a chord would give a nonfacial triangle through \(v\).

Any vertex outside \(N[v]\) has at most two neighbors in \(N(v)\), and if it has two, they are consecutive on this cycle. Otherwise there is an induced 4-cycle through \(v\), contrary to Lemma 7.1.

For each of the \(d\) edges of the neighborhood cycle, consider the triangular face on the side opposite \(v\). Its third vertex lies outside \(N[v]\). These \(d\) third vertices are distinct, by the preceding paragraph. Hence
\[
n-d-1\ge d,
\]
which proves (35). ∎

Substitute \(D=(n-1)/2\) into (32):
\[
W_4\le n^2+65n-144.
\tag{36}
\]

For \(12\le n\le100\), conditions (34) and (36) are compatible because
\[
-n^2+111n-1104+\frac{1728}{n}>0.
\]
Indeed, \(n(111-n)\ge1100\) on this interval, so the expression is at least
\[
-4+\frac{1728}{100}>0.
\]

For \(101\le n\le139\), conditions (33) and (36) are compatible because
\[
-n^2+154n-1992+\frac{3072}{n}>0.
\]
Here \(n(154-n)\ge2085\), so the expression is greater than \(93\).

Thus every 5-connected maximal planar graph of order at most \(139\) satisfies the conjecture.

---

# 9. What remains unresolved

These arguments do **not** prove either full conjecture.

* For maximal outerplanar graphs, the ear-incidence estimate improves the bounded-degree range, but still permits a degree-square sum too large when the maximum degree grows with \(n\).
* For general maximal planar graphs, the common-neighbor estimate now handles maximum degree \(7\), but not arbitrary intermediate- or high-degree configurations.
* The particularly sharp 5-connected count \(c_4=m\) fails in the presence of separating 4-cycles. Even within the 5-connected class, the results above leave graphs of larger order and large maximum degree untreated.
* No ear-insertion or vertex-splitting inequality for \(s^+\) is assumed. Such an induction step would require a separate proof.

Accordingly, the verdict is **partial**: the displayed special cases are proved by explicit inequalities, but the two conjectures remain open within this attack.