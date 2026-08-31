```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A fourth-moment sum-of-squares certificate proves the outerplanar bound for several explicit degree regimes and the planar bound for a bounded-degree regime, while the natural high-degree extremal families are verified separately.",
  "would_publish": false,
  "caveats": "Neither conjecture is proved in full; no exhaustive computation of the remaining cases was performed."
}
```

# 1. Statement and scope

For a graph \(G\) with adjacency matrix \(A\), write

\[
s^+(G)=\sum_{\lambda_i>0}\lambda_i^2,\qquad
s^-(G)=\sum_{\lambda_i<0}\lambda_i^2.
\]

Since \(s^+(G)+s^-(G)=\operatorname{tr}A^2=2m\), the two conjectured inequalities are equivalent to

\[
s^+(G)-s^-(G)\ge 12
\]

for maximal planar graphs, and

\[
s^+(G)-s^-(G)\ge 6
\]

for maximal outerplanar graphs.

I do not prove either assertion in full. I prove:

1. a general fourth-moment lower bound for \(s^+\);
2. the maximal outerplanar conjecture whenever
   \[
   \sum_v d(v)^2\le 39n-267+\frac{324}{n};
   \]
   in particular, for every maximal outerplanar graph with \(n\ge10\) and \(\Delta\le6\);
3. an explicit extension covering every fixed \(\Delta\le17\) for sufficiently large \(n\);
4. a high-degree maximal outerplanar regime;
5. the maximal planar conjecture whenever
   \[
   \operatorname{tr}A^4\le219n-2136+\frac{3072}{n};
   \]
   in particular, when \(n\ge482\) and \(\Delta\le6\);
6. the conjectured inequalities for the natural fan, double-fan, and bipyramid constructions.

No counterexample was found.

# 2. A variational sum-of-squares bound

Let \(A_+\) be the positive part of a real symmetric matrix \(A\).

## Lemma 2.1

For every real symmetric \(A\),

\[
\operatorname{tr}(A_+^2)
 =\max_{X\succeq0}\left(2\operatorname{tr}(AX)-\operatorname{tr}(X^2)\right).
\]

### Proof

Completing the square gives

\[
2\operatorname{tr}(AX)-\operatorname{tr}(X^2)
 =\operatorname{tr}(A^2)-\|A-X\|_F^2.
\]

The orthogonal projection of \(A\) onto the cone of positive semidefinite matrices is \(A_+\). Hence the maximum is

\[
\operatorname{tr}(A^2)-\|A-A_+\|_F^2
 =\operatorname{tr}(A_+^2).
\qquad\square
\]

Let

- \(m=|E(G)|\),
- \(\tau=\tau(G)\) be the number of triangles,
- \(W_4=\operatorname{tr}A^4\).

Taking \(X=t(A+aI)^2\succeq0\), where \(a,t\ge0\), gives the following.

## Lemma 2.2

For every graph \(G\) and every \(a\ge0\),

\[
\boxed{
s^+(G)\ge
\frac{(6\tau+4am)^2}
{W_4+24a\tau+12a^2m+a^4n}.
}
\tag{2.1}
\]

### Proof

We have

\[
\operatorname{tr}\bigl(A(A+aI)^2\bigr)
 =\operatorname{tr}A^3+2a\operatorname{tr}A^2
 =6\tau+4am,
\]

and

\[
\operatorname{tr}(A+aI)^4
 =W_4+24a\tau+12a^2m+a^4n.
\]

Lemma 2.1 therefore gives

\[
s^+(G)\ge
2t(6\tau+4am)
-t^2\bigl(W_4+24a\tau+12a^2m+a^4n\bigr).
\]

Optimizing over \(t\ge0\) proves (2.1). \(\square\)

We shall also use the standard closed-walk identity

\[
\boxed{
W_4=2\sum_{v}d(v)^2-2m+8c_4(G),
}
\tag{2.2}
\]

where \(c_4(G)\) counts not necessarily induced \(4\)-cycles.

# 3. Maximal outerplanar graphs

Let \(G\) be maximal outerplanar of order \(n\ge4\). Then

\[
m=2n-3,\qquad \tau=n-2.
\]

Moreover,

\[
c_4(G)=n-3.
\tag{3.1}
\]

Indeed, a triangulated polygon is chordal and \(K_4\)-free. Thus every \(4\)-cycle has exactly one chord and is the union of the two triangular faces incident with an internal diagonal. Conversely, each of the \(n-3\) internal diagonals produces one \(4\)-cycle.

Consequently,

\[
\boxed{
W_4=2\sum_v d(v)^2+4n-18.
}
\tag{3.2}
\]

Substitution into Lemma 2.2 gives, for every \(a\ge0\),

\[
s^+(G)\ge
\frac{\bigl((6+8a)n-12(1+a)\bigr)^2}
{W_4+(24a+24a^2+a^4)n-(48a+36a^2)}.
\tag{3.3}
\]

## Theorem 3.1

Let \(G\) be maximal outerplanar of order \(n\). If

\[
\boxed{
\sum_vd(v)^2\le 39n-267+\frac{324}{n},
}
\tag{3.4}
\]

then \(s^+(G)\ge2n\).

### Proof

Put \(a=2\) in (3.3). Then

\[
s^+(G)\ge
\frac{(22n-36)^2}{W_4+160n-240}.
\tag{3.5}
\]

The right side is at least \(2n\) whenever

\[
W_4\le82n-552+\frac{648}{n}.
\tag{3.6}
\]

Using (3.2), condition (3.6) is exactly (3.4). \(\square\)

## Corollary 3.2

If \(G\) is maximal outerplanar, \(n\ge10\), and \(\Delta(G)\le6\), then

\[
s^+(G)\ge2n.
\]

### Proof

For \(2\le d\le6\),

\[
d^2\le8d-12.
\]

Since \(\sum_vd(v)=4n-6\),

\[
\sum_vd(v)^2\le8(4n-6)-12n=20n-48.
\]

For \(n\ge10\),

\[
20n-48
\le39n-267+\frac{324}{n},
\]

because after multiplying by \(n\) this is

\[
19n^2-219n+324\ge0,
\]

which holds at \(n=10\) and is increasing thereafter. Apply Theorem 3.1. \(\square\)

More generally, if \(\Delta(G)\le D\), then convexity of \(d^2\) on \([2,D]\) gives

\[
d^2\le(D+2)d-2D,
\]

and hence

\[
\sum_vd(v)^2\le(2D+8)n-6D-12.
\tag{3.7}
\]

Combining this with Theorem 3.1 yields:

## Corollary 3.3

A maximal outerplanar graph of order \(n\) and maximum degree \(D\) satisfies \(s^+(G)\ge2n\) whenever

\[
\boxed{
(62-4D)n+12D-510+\frac{648}{n}\ge0.
}
\tag{3.8}
\]

For example, this proves the conjecture in the following regimes:

\[
\begin{array}{c|c}
\Delta(G)\le & \text{sufficient order}\\ \hline
6&n\ge10\\
7&n\ge11\\
8&n\ge12\\
9&n\ge14\\
10&n\ge16\\
11&n\ge20\\
12&n\ge25\\
13&n\ge34\\
14&n\ge56.
\end{array}
\]

A slightly better asymptotic range follows by choosing \(a=5/2\). In that case it is sufficient that

\[
W_4\le\frac{1423}{16}n-747+\frac{882}{n}.
\]

Using (3.7), this is implied by

\[
\boxed{
\frac{1103-64D}{16}\,n+12D-705+\frac{882}{n}\ge0.
}
\tag{3.9}
\]

Thus every fixed maximum degree \(D\le17\) is covered for all sufficiently large \(n\).

# 4. A high-degree maximal outerplanar regime

For every vertex \(v\) of degree \(d\) in a maximal outerplanar graph,

\[
G[N[v]]\cong K_1\vee P_d.
\tag{4.1}
\]

Indeed, in the outerplane embedding the \(d\) neighbors of \(v\), in order, contain a path with \(d-1\) edges. Together with the \(d\) edges incident with \(v\), this already gives \(2d-1\) edges on \(d+1\) vertices, the outerplanar maximum; hence there can be no further neighbor-neighbor edge.

## Proposition 4.1

Let \(G\) be maximal outerplanar and let \(v\) have degree \(d\ge11\). If

\[
n\le d+\sqrt d-2,
\tag{4.2}
\]

then \(s^+(G)>2n\).

### Proof

Set \(F_d=K_1\vee P_d\). Since \(F_d\) is a principal induced subgraph of \(G\),

\[
s^+(G)\ge s^+(F_d).
\]

Let

\[
\mu_1=2\cos\frac{\pi}{d+1}
\]

be the largest eigenvalue of \(P_d\). Since \(P_d\) is bipartite,

\[
s^+(P_d)=d-1.
\]

Interlacing therefore gives

\[
s^+(F_d)\ge \lambda_1(F_d)^2+d-1-\mu_1^2.
\tag{4.3}
\]

Compressing \(A(F_d)\) to the span of the apex and the normalized all-ones vector on the path gives

\[
\begin{pmatrix}
0&\sqrt d\\
\sqrt d&c
\end{pmatrix},
\qquad
c=\frac{2(d-1)}d.
\]

Thus

\[
\lambda_1(F_d)\ge
R:=\frac{c+\sqrt{c^2+4d}}2.
\]

Since \(R\ge\sqrt d+c/2\) and \(R^2=d+cR\),

\[
R^2\ge d+c\sqrt d+\frac{c^2}{2}.
\]

Using \(\mu_1^2<4\) in (4.3),

\[
s^+(F_d)>
2d-5+c\sqrt d+\frac{c^2}{2}.
\]

The difference between the right side and \(2(d+\sqrt d-2)\) is

\[
1-\frac2{\sqrt d}-\frac4d+\frac2{d^2},
\]

which is positive for \(d\ge11\). Therefore

\[
s^+(G)\ge s^+(F_d)>2(d+\sqrt d-2)\ge2n.
\qquad\square
\]

Thus the difficult maximal outerplanar range is not the nearly dominating case, but rather graphs with one or more intermediate-sized hubs.

# 5. The fan family

The previous proposition handles sufficiently large fans. The small threshold cases can also be verified analytically.

## Proposition 5.1

For every \(q\ge7\),

\[
s^+(K_1\vee P_q)\ge2(q+1).
\]

Thus every maximal outerplanar graph with a dominating vertex satisfies the conjecture.

### Proof

Write

\[
c=\frac{2(q-1)}q,\qquad
R=\frac{c+\sqrt{c^2+4q}}2.
\]

As above,

\[
s^+(K_1\vee P_q)
\ge R^2+q-1-4\cos^2\frac{\pi}{q+1}.
\tag{5.1}
\]

Since \(R^2=q+cR\), it is enough to show

\[
cR\ge3+4\cos^2\frac{\pi}{q+1}.
\tag{5.2}
\]

For \(q\ge10\),

\[
cR\ge c\sqrt q+\frac{c^2}{2}
\ge\frac95\sqrt{10}+\frac{81}{50}>7,
\]

while the right side of (5.2) is less than \(7\).

For \(q=8\),

\[
cR=\frac{7(7+\sqrt{561})}{32}>\frac{105}{16}.
\]

Also \(\sin(\pi/9)>1/3\), and hence

\[
4\cos^2\frac{\pi}{9}<\frac{32}{9}.
\]

Therefore

\[
3+4\cos^2\frac{\pi}{9}<\frac{59}{9}<\frac{105}{16}.
\]

For \(q=9\),

\[
cR=\frac{16(8+\sqrt{793})}{81}>\frac{64}{9},
\]

whereas

\[
3+4\cos^2\frac{\pi}{10}
=\frac{11+\sqrt5}{2}<\frac{20}{3}<\frac{64}{9}.
\]

It remains to treat \(q=7\). On the path vertices use the trial vector

\[
x=\left(\frac7{10},1,1,1,1,1,\frac7{10}\right).
\]

After normalization, the compression to the apex and \(x\) is

\[
\begin{pmatrix}
0&b\\
b&r
\end{pmatrix},
\qquad
r=\frac{540}{299},\qquad b^2=\frac{2048}{299}.
\]

Let \(L\) be its positive eigenvalue. Then

\[
L^2-rL-b^2=0.
\]

A direct exact calculation gives

\[
L^2>12+\sqrt2.
\tag{5.3}
\]

For completeness, writing \(Y=12+\sqrt2\), inequality (5.3) follows from

\[
540\sqrt Y>299Y-2048=1540+299\sqrt2.
\]

After squaring, the difference between the two sides is

\[
948798-629320\sqrt2>0,
\]

using \(\sqrt2<3/2\). Finally,

\[
4\cos^2\frac{\pi}{8}=2+\sqrt2,
\]

so interlacing gives

\[
s^+(K_1\vee P_7)
>L^2+6-(2+\sqrt2)>16.
\]

This completes all \(q\ge7\). \(\square\)

A pinching observation modestly extends this result. If \(V(G)\) is partitioned into sets \(V_1,\dots,V_k\), then

\[
s^+(G)\ge\sum_i s^+(G[V_i]).
\tag{5.4}
\]

Indeed, block-diagonal pinching is an average of unitary conjugates, and \(A\mapsto\operatorname{tr}(A_+^2)\) is convex by Lemma 2.1. Consequently, any maximal outerplanar graph whose vertex set can be partitioned into induced fans of order at least \(8\) satisfies \(s^+(G)\ge2n\).

# 6. Maximal planar graphs: a fourth-moment criterion

Let \(G\) be maximal planar of order \(n\ge4\). Then

\[
m=3n-6,\qquad \tau\ge2n-4.
\]

For fixed \(W_4,m,a\), the right side of (2.1) is increasing in \(\tau\). Substituting \(\tau=2n-4\) therefore gives

\[
s^+(G)\ge
\frac{144(1+a)^2(n-2)^2}
{W_4+(48a+36a^2+a^4)n-(96a+72a^2)}.
\tag{6.1}
\]

Putting \(a=3\) yields

\[
s^+(G)\ge
\frac{(48n-96)^2}{W_4+549n-936}.
\tag{6.2}
\]

## Theorem 6.1

If a maximal planar graph \(G\) of order \(n\) satisfies

\[
\boxed{
W_4\le219n-2136+\frac{3072}{n},
}
\tag{6.3}
\]

then \(s^+(G)\ge3n\).

### Proof

Condition (6.3) is exactly the result of requiring the right side of (6.2) to be at least \(3n\). \(\square\)

Equivalently, using (2.2) and \(m=3n-6\), condition (6.3) is

\[
2\sum_vd(v)^2+8c_4(G)
\le225n-2148+\frac{3072}{n}.
\tag{6.4}
\]

## Corollary 6.2

If \(G\) is maximal planar, \(\Delta(G)\le6\), and \(n\ge482\), then

\[
s^+(G)\ge3n.
\]

### Proof

For \(3\le d\le6\),

\[
d^2\le9d-18.
\]

Thus

\[
\sum_vd(v)^2\le9(6n-12)-18n=36n-108.
\tag{6.5}
\]

For distinct \(u,v\), let \(c_{uv}=|N(u)\cap N(v)|\). Every \(4\)-cycle has two opposite pairs, so

\[
2c_4(G)=\sum_{\{u,v\}}\binom{c_{uv}}2.
\]

As \(c_{uv}\le6\),

\[
\binom{c_{uv}}2\le\frac52c_{uv}.
\]

Moreover,

\[
\sum_{\{u,v\}}c_{uv}=\sum_w\binom{d(w)}2.
\]

Consequently,

\[
c_4(G)\le\frac54\sum_w\binom{d(w)}2.
\]

Combining this with (2.2),

\[
\begin{aligned}
W_4
&\le2\sum d(v)^2-(6n-12)
 +10\sum_v\binom{d(v)}2\\
&=7\sum_vd(v)^2-6(6n-12)\\
&\le216n-684,
\end{aligned}
\]

where (6.5) was used in the last line. Now

\[
216n-684
\le219n-2136+\frac{3072}{n}
\]

is equivalent to

\[
n^2-484n+1024\ge0,
\]

which holds for every integer \(n\ge482\). Apply Theorem 6.1. \(\square\)

This is a genuine but limited bounded-degree special case. The fourth moment can be quadratic in \(n\) for triangulations with hubs, so Theorem 6.1 cannot by itself address the general conjecture.

# 7. The principal high-degree planar families

Two natural maximal planar families satisfy the conjecture directly.

## 7.1 Double fans

Let

\[
D_q=K_2\vee P_q,
\qquad q\ge8.
\]

This is maximal planar of order \(n=q+2\).

Let

\[
\mu_1=2\cos\frac{\pi}{q+1}.
\]

Interlacing with the principal \(P_q\) gives

\[
s^+(D_q)\ge\lambda_1(D_q)^2+(q-1)-\mu_1^2.
\tag{7.1}
\]

Compressing to the normalized all-ones vectors on \(K_2\) and \(P_q\) gives

\[
\begin{pmatrix}
1&\sqrt{2q}\\
\sqrt{2q}&c
\end{pmatrix},
\qquad c=\frac{2(q-1)}q.
\]

Its larger eigenvalue is

\[
R=\frac{1+c+\sqrt{(1-c)^2+8q}}2.
\]

For \(q\ge8\),

\[
R\ge\sqrt{2q}+\frac{1+c}{2},
\]

and hence

\[
R^2>2q+11.
\]

Since \(\mu_1^2<4\), (7.1) gives

\[
s^+(D_q)>2q+11+q-1-4=3q+6=3n.
\]

Thus all double fans in the conjectured range satisfy the bound.

## 7.2 Bipyramids

Let

\[
B_q=\overline K_2\vee C_q,
\qquad q\ge8.
\]

This is the \(q\)-gonal bipyramid, maximal planar of order \(q+2\). Its spectrum consists of

\[
1+\sqrt{2q+1},\qquad
1-\sqrt{2q+1},\qquad
0,
\]

together with the nonprincipal eigenvalues of \(C_q\). Therefore

\[
s^+(B_q)
=(1+\sqrt{2q+1})^2+s^+(C_q)-4.
\tag{7.2}
\]

For completeness, the positive square energy of an odd cycle is

\[
s^+(C_q)=
\begin{cases}
q+1-\sec(\pi/q),&q\equiv1\pmod4,\\[2mm]
q-1+\sec(\pi/q),&q\equiv3\pmod4.
\end{cases}
\tag{7.3}
\]

For even \(q\), bipartiteness gives \(s^+(C_q)=q\). In all cases,

\[
s^+(C_q)\ge q-1.
\tag{7.4}
\]

For \(q\ge10\), equations (7.2) and (7.4) give

\[
s^+(B_q)
\ge3q-3+2\sqrt{2q+1}
>3q+6.
\]

For \(q=8\),

\[
s^+(B_8)=22+2\sqrt{17}>30.
\]

For \(q=9\), using (7.3),

\[
s^+(B_9)
=26+2\sqrt{19}-\sec(\pi/9)>33.
\]

Hence every bipyramid in the conjectured range satisfies the planar bound.

# 8. Remaining gaps

The arguments above do not cover all cases.

1. **Maximal outerplanar graphs.**  
   The fourth-moment argument covers a substantial low-degree range, while Proposition 4.1 covers a nearly dominating vertex. It does not cover arbitrary triangulated polygons with several intermediate or growing-degree hubs. In particular, the cases \(n=8,9\) outside the fan family have not been exhaustively checked here.

2. **Maximal planar graphs.**  
   The fourth-moment criterion is effective when both \(\sum d(v)^2\) and the number of \(4\)-cycles are controlled. General triangulations may have \(W_4=\Theta(n^2)\), as happens in bipyramid-type graphs. The explicit high-degree constructions can be analyzed, but I do not have a structural reduction showing that every graph with large \(W_4\) decomposes into such pieces.

3. **No induction inequality.**  
   A tempting claim would be that adding a simplicial degree-\(2\) vertex increases \(s^+\) by at least \(2\). I have not proved such an inequality, and analogous statements fail in unrestricted chordal graphs, so it should not be assumed.

Thus the conjecture remains open, but the sum-of-squares certificate gives explicit, journal-checkable sufficient conditions and settles several infinite subclasses.