```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I derive necessary conditions for a smallest counterexample and give a self-contained reproof for n <= 8, but obtain no improvement on the catalog's known bounds.",
  "would_publish": false,
  "caveats": "The small cases are already known; no novelty is claimed, and the K13 application uses the catalog's value cr(K11)=100 as an input."
}
```

# Partial attack: deletion excesses and vertex duplication

Write
\[
H(n)=\frac14
\left\lfloor\frac n2\right\rfloor
\left\lfloor\frac{n-1}2\right\rfloor
\left\lfloor\frac{n-2}2\right\rfloor
\left\lfloor\frac{n-3}2\right\rfloor .
\]
I use the upper bound \(\operatorname{cr}(K_n)\le H(n)\) supplied in the question.

The main result below is a system of necessary integer constraints on a smallest counterexample. A Jordan-curve obstruction makes these constraints sufficient at order seven. They remain insufficient at order thirteen: I give explicit integer data satisfying them for the still-listed candidate \(219\). **These data are not a drawing or a counterexample.**

Throughout, \(c(D)\) denotes the number of crossings in a particular good drawing \(D\), not the crossing number of its underlying graph.

## 1. Deletion counting and parity

### Deletion identity

For a drawing \(D\) of \(K_r\),
\[
\sum_{v\in V(D)}c(D-v)=(r-4)c(D).
\tag{1}
\]
Indeed, each crossing has four distinct endpoints and survives deletion of precisely the other \(r-4\) vertices.

Consequently,
\[
\operatorname{cr}(K_{2m})
\ge \frac{2m}{2m-4}\operatorname{cr}(K_{2m-1}).
\]
Since
\[
H(2m)=\frac{2m}{2m-4}H(2m-1),
\]
truth at an odd order implies truth at the next even order. Thus a smallest counterexample must have odd order.

For clarity, **odd-to-even is the implication supplied by this deletion calculation**; the reverse-direction sentence in the original discussion does not follow from it.

### Odd-order parity lemma

For every good drawing \(D\) of \(K_r\), with \(r\) odd,
\[
c(D)\equiv \binom r4\pmod 2.
\tag{2}
\]

Here is a proof that does not require a classification of drawings. Fix the vertex positions and replace one edge \(uv\) by another \(uv\)-arc. The old and new arcs together form a closed curve \(C\), interpreted modulo two. For an edge \(ab\) independent of \(uv\), the change in crossing parity is
\[
\lambda_C(a)+\lambda_C(b),
\]
where \(\lambda_C\) is the mod-two winding number. Summing over all edges on the remaining \(r-2\) vertices gives
\[
(r-3)\sum_{w\ne u,v}\lambda_C(w)=0\pmod2.
\]
Thus replacing an edge preserves the parity of the total number of independent-edge crossings. Intermediate drawings need not be good; general position suffices for this parity comparison.

After applying a plane homeomorphism to put the vertices in convex position, replace the edges one at a time by straight segments. The resulting drawing has \(\binom r4\) crossings, proving (2).

In particular,
\[
c(D)\equiv H(2m+1)\pmod2
\qquad\text{when }D\text{ draws }K_{2m+1}.
\tag{3}
\]
Indeed,
\[
H(2m+1)=\binom m2^{\,2},
\qquad
\binom{2m+1}{4}\equiv\binom m2\pmod2.
\]
The latter congruence follows by comparing coefficients of \(x^4\) in
\[
(1+x)^{2m+1}\equiv(1+x)(1+x^2)^m\pmod2.
\]

## 2. A vertex-duplication inequality

Let \(D\) be a crossing-minimal drawing of \(K_n\). Define
\[
d_v=\#\{\text{crossings having }v\text{ among their endpoints}\},
\]
and, for distinct \(u,v\),
\[
p_{uv}=\#\{\text{crossings having both }u,v
\text{ among their endpoints}\}.
\]
Thus \(p_{uv}\) counts more than just crossings of the edge \(uv\).

Then
\[
p_{uv}+|d_u-d_v|
\le
L_n:=
\left\lfloor\frac{n-2}{2}\right\rfloor
\left\lfloor\frac{n-3}{2}\right\rfloor .
\tag{4}
\]

### Proof

Delete \(u\), place a new copy of \(u\) sufficiently close to \(v\), and route its edges alongside the corresponding edges incident with \(v\).

Away from a small disk around \(v\), the copied edges introduce exactly
\[
d_v-p_{uv}
\]
crossings: these are the crossings involving \(v\) that survived deletion of \(u\).

Inside the disk, split the \(n-2\) old incident edges into two consecutive blocks of sizes \(a,b\), with \(|a-b|\le1\). Route the copied edges in nested fans on the two sides of the short new edge \(uv\). The local crossing count is
\[
\binom a2+\binom b2=L_n.
\]
For example, on a side containing \(a\) old rays, the successive copied edges cross \(0,1,\ldots,a-1\) old rays. The copied edges can be kept mutually disjoint. Thin strips around the old edges, and small disks at their other endpoints, introduce no further crossings.

The resulting drawing therefore has at most
\[
c(D)-d_u+d_v-p_{uv}+L_n
\]
crossings. Minimality gives
\[
p_{uv}\le L_n+d_v-d_u.
\]
Interchanging \(u,v\) proves (4). \(\square\)

## 3. Necessary conditions for a smallest counterexample

Suppose \(m\ge3\) and
\[
\operatorname{cr}(K_{2m-1})=H(2m-1).
\]
Deletion counting and the upper bound then give
\(\operatorname{cr}(K_{2m})=H(2m)\).

Assume that a crossing-minimal drawing \(D\) of \(K_{2m+1}\) violates the conjecture. By parity, write
\[
c(D)=H(2m+1)-2q,\qquad q\ge1.
\]

Define the deletion excesses
\[
e_v=c(D-v)-H(2m)
\]
and the two-vertex deletion excesses
\[
b_{uv}
=\frac{c(D-\{u,v\})-H(2m-1)}2.
\]
These are nonnegative integers. Put \(b_{vv}=0\), and set
\[
A_m=\frac{m(m-1)^2}{2},
\qquad
E=\sum_v e_v.
\]

### Proposition

The following conditions are necessary:
\[
\boxed{
\begin{aligned}
E&=A_m-2q(2m-3),\\
\sum_{w\ne v}b_{vw}&=(m-2)e_v
&&\text{for every }v,\\
b_{uv}&\le \min(e_u,e_v)+q
&&\text{for every }u\ne v,\\
p_{uv}&=(m-1)^2-2q-e_u-e_v+2b_{uv}\ge0.
\end{aligned}}
\tag{5}
\]
In particular,
\[
q\le
\left\lfloor
\frac{m(m-1)^2}{4(2m-3)}
\right\rfloor,
\qquad
e_v\le\frac E2.
\tag{6}
\]

### Proof

Applying (1) to \(D\),
\[
\begin{aligned}
E
&=(2m-3)\bigl(H(2m+1)-2q\bigr)
 -(2m+1)H(2m)\\
&=A_m-2q(2m-3).
\end{aligned}
\]

Apply (1) within \(D-v\). This gives
\[
\begin{aligned}
2\sum_{w\ne v}b_{vw}
&=(2m-4)\bigl(H(2m)+e_v\bigr)
 -2mH(2m-1)\\
&=(2m-4)e_v,
\end{aligned}
\]
proving the second condition.

Inclusion-exclusion for crossings gives
\[
p_{uv}
=c(D)-c(D-u)-c(D-v)+c(D-\{u,v\}).
\]
Using
\[
H(2m+1)-2H(2m)+H(2m-1)=(m-1)^2
\]
yields the displayed expression for \(p_{uv}\).

Also,
\[
|d_u-d_v|=|e_u-e_v|.
\]
For \(n=2m+1\), inequality (4) has \(L_n=(m-1)^2\). Substitution therefore gives
\[
-2q-e_u-e_v+2b_{uv}+|e_u-e_v|\le0,
\]
equivalently
\[
b_{uv}\le \min(e_u,e_v)+q.
\]

The bound on \(q\) follows from \(E\ge0\). Finally, regard the \(b_{uv}\) as edge weights of a loopless multigraph. Its weighted degree at \(v\) is \((m-2)e_v\), while its total edge weight is \((m-2)E/2\). A weighted degree cannot exceed the total edge weight, proving \(e_v\le E/2\). \(\square\)

These conditions apply, in particular, to every smallest counterexample.

## 4. A complete topological obstruction at order seven

The following recovers only known small cases, but illustrates how topology can strengthen the numerical constraints.

Parity and the supplied upper bound give
\[
\operatorname{cr}(K_5)=1.
\]
Deletion counting then gives
\[
\operatorname{cr}(K_6)=3.
\]

Suppose \(\operatorname{cr}(K_7)<9\), and take a crossing-minimal drawing \(D\). In the proposition, \(m=3\), and (6) forces \(q=1\). Thus
\[
c(D)=7,\qquad E=6-2\cdot1\cdot3=0.
\]
All \(e_v\) and \(b_{uv}\) vanish. In particular, **every induced \(K_5\) has exactly one crossing**.

### The forced triple system

Let \(V\) be the seven-vertex set. For each crossing, let \(Q\) be its four endpoints and form the complementary triple
\[
L=V\setminus Q.
\]
These seven triples have the following property:

> Every pair of vertices belongs to exactly one triple.

Indeed, the triples containing a pair \(\{u,v\}\) correspond exactly to the crossings surviving in \(D-\{u,v\}\), and that drawing has one crossing.

Choose one crossing, say between \(ab\) and \(cd\), and write its complementary triple as
\[
L=\{v,w,z\}.
\]
For each \(x\in L\), the two triples through \(x\) other than \(L\) partition
\[
Q=\{a,b,c,d\}
\]
into two pairs. Denote the resulting perfect matching of \(Q\) by \(M_x\).

The three matchings \(M_v,M_w,M_z\) are distinct: otherwise a pair from \(Q\) would occur in two triples. Since a four-element set has exactly three perfect matchings, one of them is
\[
\{\{a,b\},\{c,d\}\}.
\]
Relabel \(v,w,z\) so that this is \(M_v\). The three triples through \(v\) are consequently
\[
\{v,w,z\},\qquad \{v,a,b\},\qquad \{v,c,d\}.
\]

It follows that the three crossings in \(D-v\) have endpoint sets
\[
\{a,b,c,d\},\qquad
\{w,z,c,d\},\qquad
\{w,z,a,b\}.
\]

### Contradiction from two disjoint triangles

Consider the vertex-disjoint triangles
\[
wab\quad\text{and}\quad zcd.
\]
They are Jordan curves. Their boundaries therefore cross an even number of times.

But \(ab\) crosses \(cd\). Neither of the other two crossings can be between the triangles: each of its endpoint sets has three vertices in one triangle and one in the other. Thus the two boundaries cross exactly once, a contradiction.

Therefore
\[
\operatorname{cr}(K_7)=9.
\]
Deletion counting now gives
\[
\operatorname{cr}(K_8)\ge \frac8{8-4}\,9=18,
\]
and the upper bound gives equality. Together with the planar cases, this proves the conjectured values for \(n\le8\).

## 5. Why this does not settle the next open order

For this section, take the catalog’s quoted value
\[
\operatorname{cr}(K_{11})=100
\]
as an external input. Then deletion counting gives
\[
\operatorname{cr}(K_{12})=150.
\]

Our numerical deficit bound at order thirteen gives only \(c(D)\ge217\); it does **not** recover the catalog’s quoted exclusion of \(217\).

Consider instead a hypothetical optimum
\[
c(D)=219=225-6.
\]
Here \(m=6\), \(q=3\), and (5) becomes
\[
\begin{aligned}
\sum_v e_v&=21,\\
\sum_{w\ne v}b_{vw}&=4e_v,\\
b_{uv}&\le\min(e_u,e_v)+3,\\
p_{uv}&=19-e_u-e_v+2b_{uv}\ge0.
\end{aligned}
\tag{7}
\]
Also \(0\le e_v\le10\). Hence every vertex-deleted drawing would have between \(150\) and \(160\) crossings.

### Explicit feasible integer data

Partition thirteen abstract vertices into \(U\cup W\), where
\[
|U|=8,\qquad |W|=5.
\]
Set
\[
e_v=
\begin{cases}
2,&v\in U,\\
1,&v\in W.
\end{cases}
\]
Thus \(\sum_v e_v=21\).

Choose a perfect matching \(M\) on \(U\) and a five-cycle \(C\) on \(W\). Define
\[
b_{uv}=
\begin{cases}
2,&uv\in M\cup E(C),\\
1,&u,v\in U\text{ and }uv\notin M,\\
0,&\text{otherwise}.
\end{cases}
\]
A vertex in \(U\) has weighted degree \(7+1=8=4e_v\), and a vertex in \(W\) has weighted degree \(2+2=4=4e_v\). The upper bounds on \(b_{uv}\) hold immediately.

The resulting \(p_{uv}\) values are:
- \(17\) or \(19\) within \(U\);
- \(17\) or \(21\) within \(W\);
- \(16\) between \(U\) and \(W\).

Thus all conditions in (7), including the duplication inequality, are satisfied.

**This is only a solution of the necessary integer constraints.** It need not extend to crossing indicators on four-element subsets, much less to a realizable drawing. It shows that deletion counts, odd-order parity, and these vertex-duplication inequalities do not by themselves exclude \(219\).

## Remaining gap

At order seven, the numerical equalities force enough crossing information that a single disjoint-triangle parity obstruction finishes the argument. At order thirteen, the deletion-excess data leave substantial freedom. One would need further constraints expressing compatibility of the crossing pairs, rotations, and Jordan curves.

I have not supplied such constraints sufficient to exclude \(219,221,223\), or to handle arbitrary larger odd orders. Accordingly, this is a rigorous partial analysis and a reproof of known small cases—not a proof, counterexample, improved general bound, or new asymptotic result.