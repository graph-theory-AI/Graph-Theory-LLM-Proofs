```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An exact K5-padding operation realizes every four-term sequence (a,b,c,0) with a >= b+c, in both surface categories, and yields further arbitrary-length families.",
  "would_publish": false,
  "caveats": "Uses the established three-term results quoted in the question; the general conjecture remains unresolved here, and no novelty claim is made."
}
```

# 1. Partial result

Write
\[
o_g(G)=\operatorname{cr}_{S_g}(G),\qquad
n_i(G)=\operatorname{cr}_{N_i}(G),
\]
where \(S_g\) is the orientable surface of genus \(g\), and \(N_i\) is the nonorientable surface with \(i\) crosscaps. We use \(N_0=S_0\).

I prove the following subfamily, using the established three-term existence results stated in the question.

**Partial theorem.** If
\[
a>b>c>0,\qquad a\ge b+c,
\]
then \((a,b,c,0)\) is realizable as an orientable crossing sequence and, by a possibly different graph, as a nonorientable crossing sequence.

The main ingredient is an exact padding operation. Its proof does **not** assume an additivity theorem for arbitrary disjoint unions on surfaces.

# 2. A protected \(K_5\) gadget

For a graph with positive integer edge weights, give a crossing of edges \(e,f\) the cost \(w(e)w(f)\).

Integer weights can be eliminated exactly: replace an edge of weight \(w\) by \(w\) parallel edges. Indeed:

- Thickening a weighted drawing gives an ordinary drawing with the same total crossing cost.
- Conversely, in a drawing of the parallel-edge graph, independently choose one representative from each bundle, uniformly at random. A crossing between distinct bundles of sizes \(w(e),w(f)\) survives with probability \(1/(w(e)w(f))\). Its expected weighted contribution is therefore \(1\). Crossings within one bundle do not survive.

Thus some selection has weighted cost at most the original number of crossings. This proves equality of the two minima on every surface. Subdividing the parallel edges makes the graph simple without changing its crossing numbers.

For an integer \(d\ge1\), let \(P_d\) be the ordinary graph obtained this way from the following weighted \(K_5\):

- one distinguished edge \(e=uv\) has weight \(1\);
- its other nine edges have weight \(d\).

We will freely use this weighted representation of \(P_d\).

Its elementary properties are
\[
o_0(P_d)=n_0(P_d)=d,\qquad o_1(P_d)=n_1(P_d)=0.
\]
For the planar lower bound, every crossing involves at least one edge of weight \(d\), and \(K_5\) is nonplanar. For the upper bound, use a one-crossing drawing of \(K_5\) in which \(e\) participates in the crossing.

Resolving that crossing with one handle, or with one crosscap, gives the asserted embeddings. Parallel copies can follow the embedded edges.

# 3. The separation fact

Put
\[
M=K_5-e.
\]

Consider a drawing of \(G\sqcup K_5\) on a closed surface \(S\), and suppose **no edge of \(M\) participates in any crossing**. The distinguished edge \(e\) may cross edges of \(G\).

Then:

- if \(S=S_g\), the drawing of \(G\) can be transferred, without increasing its crossings, to an orientable surface of genus at most \(g-1\);
- if \(S=N_i\), it can be transferred to some closed surface of Euler genus at most \(i-1\). That surface might be orientable.

Here is the topological justification.

Take a sufficiently small connected regular neighbourhood \(R\) of the embedded \(M\), disjoint from the drawing of \(G\). Let \(b\) be the number of boundary components of \(R\), and let
\[
C_1,\ldots,C_r
\]
be the components of its complement. Write \(\epsilon(X)\) for the Euler genus after capping all boundary components of a connected surface \(X\). Euler characteristic gives
\[
\epsilon(S)
=
\epsilon(R)+\sum_{j=1}^r\epsilon(C_j)+2(b-r).
\tag{1}
\]
Every \(C_j\) has boundary, so \(b\ge r\).

If \(\epsilon(R)>0\), equation (1) already accounts for at least one unit of Euler genus outside the capped complementary components. On an orientable surface, it accounts for at least two.

Suppose instead that \(R\) is planar. The ends of \(e\), viewed in their incident boundary corners of \(R\), must lie on **different** boundary components. Otherwise, after capping \(R\), one could add \(e\) within a single face and obtain a planar embedding of \(K_5\).

But the interior of \(e\) avoids \(M\), and hence can be taken outside the interior of \(R\). It connects those two boundary components through one complementary component. Consequently \(b-r\ge1\). Equation (1) now accounts for two units of Euler genus outside the capped complementary components.

The entire drawing of \(G\) lies in the complementary components. Cap them and take connected sums away from the drawing. The crossing count is unchanged, and the claimed genus bounds follow.

# 4. Exact padding identities

The preceding fact gives the following formulas for every graph \(G\) and integer \(d\ge1\):
\[
\boxed{
o_g(G\sqcup P_d)
=
\min\{o_g(G)+d,\ o_{g-1}(G)\}
\quad(g\ge1).
}
\tag{2}
\]
In the nonorientable case,
\[
\boxed{
n_i(G\sqcup P_d)
=
\min\left\{
n_i(G)+d,\;
n_{i-1}(G),\;
o_{\lfloor(i-1)/2\rfloor}(G)
\right\}
\quad(i\ge1).
}
\tag{3}
\]
On the sphere,
\[
o_0(G\sqcup P_d)=n_0(G\sqcup P_d)=o_0(G)+d.
\tag{4}
\]

## Upper bounds

For the first term in either formula, put a planar drawing of \(P_d\), with \(d\) crossings, in a small disk disjoint from a drawing of \(G\).

For the second term, embed \(P_d\) using one handle or one crosscap, respectively, and use the rest of the surface for \(G\).

For the third term in (3), put \(h=\lfloor(i-1)/2\rfloor\). A drawing of \(G\) on \(S_h\), together with a projective-plane embedding of \(P_d\), fits on
\[
S_h\#N_1\cong N_{2h+1}.
\]
Add an unused crosscap if necessary to reach \(N_i\).

## Lower bounds

Work in the equivalent weighted model. Suppose a drawing has total crossing cost \(C\) smaller than the proposed minimum. Let \(C_G\) be the cost of crossings internal to \(G\).

For the orientable formula,
\[
C_G\ge o_g(G),\qquad C<o_g(G)+d.
\]
Hence
\[
C-C_G<d.
\]
Every crossing involving an edge of \(M\) costs at least \(d\), and all such crossings are included in \(C-C_G\). Therefore no edge of \(M\) participates in a crossing.

The separation fact transfers the drawing of \(G\) to genus at most \(g-1\), giving
\[
o_{g-1}(G)\le C_G\le C,
\]
a contradiction.

The same argument on \(N_i\) transfers the drawing of \(G\) to a surface of Euler genus at most \(i-1\). If that surface is nonorientable, then
\[
n_{i-1}(G)\le C_G.
\]
If it is orientable, then
\[
o_{\lfloor(i-1)/2\rfloor}(G)\le C_G.
\]
Either conclusion contradicts the assumed bound on \(C\). This proves (3).

Equation (4) follows by restricting a spherical drawing to its two parts, and by drawing them in disjoint disks.

The orientable term in (3) is important: capping the complementary surface can remove all its nonorientability, so one cannot silently replace (3) by (2).

# 5. Realizing the four-term subfamily

Take a graph with crossing sequence
\[
(A,B,0),\qquad A>B>0,
\]
in the surface category under consideration.

Such graphs exist by the three-term results quoted in the question: DeVos–Mohar–Šámal orientably, and Archdeacon–Bonnington–Širáň nonorientably.

Equations (2)–(4) show that adjoining \(P_d\) gives the sequence
\[
\left(
A+d,\;
\min\{A,B+d\},\;
\min\{B,d\},\;
0
\right).
\tag{5}
\]
This formula holds in **both** categories. For the nonorientable calculation, the additional orientable term in (3) is just \(o_0(G)=A\) at indices \(1,2\), and the zero at index \(3\) follows from \(n_2(G)=0\).

Now let the requested sequence be \((a,b,c,0)\), and put
\[
x=a-b,\qquad y=b-c,\qquad z=c.
\]
Thus
\[
(a,b,c,0)=(x+y+z,\;y+z,\;z,\;0),
\]
and our hypothesis is \(x\ge z\).

There are two cases.

### Case 1: \(y\ge z\)

Choose
\[
A=x+y,\qquad B=y,\qquad d=z.
\]
Then (5) becomes
\[
\left(
x+y+z,\;
\min\{x+y,y+z\},\;
\min\{y,z\},\;
0
\right).
\]
Because \(x\ge z\) and \(y\ge z\), this is exactly the requested sequence.

### Case 2: \(y<z\)

Choose
\[
A=y+z,\qquad B=z,\qquad d=x.
\]
Now (5) becomes
\[
\left(
x+y+z,\;
\min\{y+z,z+x\},\;
\min\{z,x\},\;
0
\right).
\]
Since \(x\ge z>y\), this again is exactly the requested sequence.

This covers every case with \(a\ge b+c\).

For example, the construction realizes
\[
(2N+1,\;N+1,\;N,\;0)
\]
for every \(N\ge2\), in either category. Its successive decreases are
\[
N,\ 1,\ N,
\]
so the third handle or crosscap saves much more than the second.

# 6. An arbitrary-length consequence

Formula (2) immediately gives an extension rule.

Suppose an orientable sequence
\[
(a_0,\ldots,a_{r-1},0)
\]
has every successive decrease at least \(d\). Adjoining \(P_d\) realizes
\[
(a_0+d,\ldots,a_{r-1}+d,d,0).
\tag{6}
\]
Thus one can append a new final decrease \(d\) whenever \(d\) is no larger than any preceding decrease.

The same rule can be iterated for the nonorientable seeds used above. Here is the needed check.

Consider the property
\[
n_{2h}(G)\le o_h(G)\qquad(h\ge0).
\tag{7}
\]
It holds for every nonorientable three-term seed: equality holds at \(h=0\), while \(n_{2h}(G)=0\) for \(h\ge1\).

It is preserved by adjoining \(P_d\). Indeed, for \(h\ge1\), formulas (2)–(3) give
\[
\begin{aligned}
n_{2h}(G\sqcup P_d)
&\le \min\{n_{2h}(G)+d,\ o_{h-1}(G)\}\\
&\le \min\{o_h(G)+d,\ o_{h-1}(G)\}\\
&=o_h(G\sqcup P_d).
\end{aligned}
\]
The assertion at \(h=0\) follows from (4).

Under (7), the third term of (3) is redundant:

- for odd \(i\), this follows directly from (7);
- for even \(i\), it follows from
  \[
  n_{i-1}(G)\le o_{\lfloor(i-1)/2\rfloor}(G),
  \]
  obtained by adding one crosscap to the orientable surface.

Hence these nonorientable constructions obey the same extension rule (6).

Consequently, in either category, every sequence whose successive decreases are
\[
(p,q,u_1,\ldots,u_t),
\]
where
\[
p,q>0,\qquad
0<u_t\le\cdots\le u_1\le\min\{p,q\},
\]
is realizable.

In particular, for all integers \(a>b>0\) and \(t\ge1\), this realizes
\[
(a+t,\ b+t,\ t,\ t-1,\ldots,1,0)
\]
in both categories.

# 7. What remains unresolved

There is a precise limitation to the four-term construction. For the sequence in (5), the first decrease is
\[
A+d-\min\{A,B+d\}=\max\{A-B,d\},
\]
while the last decrease is
\[
\min\{B,d\}.
\]
Therefore the first decrease is always at least the last.

This is a limitation of this operation—not a proposed necessary condition for crossing sequences.

In particular, this argument does not realize the family
\[
(N+2,\;N+1,\;N,\;0),\qquad N\ge2.
\]
These have decreases \(1,1,N\), and
\[
\frac{a_0-a_2}{a_2-a_3}=\frac2N\longrightarrow0,
\]
matching the delayed-large-improvement phenomenon highlighted in the question.

Thus no proof or counterexample to the full conjecture is obtained. The padding lemma and the stated subfamilies are proved above, but I have not established that they are new to the literature.