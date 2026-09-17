Attack the following open graph-theory problem.

Catalog id: universal_steiner_triple_systems
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Edge coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/universal_steiner_triple_systems/
Original entry: http://www.openproblemgarden.org/op/universal_steiner_triple_systems
Problem attributed to: Grannell, Mike, Griggs, Terry, Knor, Martin, Skoviera, Martin (posted 2007-10-05)

=== Problem statement (OpenProblemGarden) ===
Title: Universal Steiner triple systems
Problem Which Steiner triple systems are universal?

=== Discussion / context (OpenProblemGarden) ===
A cubic graph $ G $ is $ S $ -edge-colorable for a Steiner triple system $ S $ if its edges can be colored with the points of $ S $ in such a way that the points assigned to three edges sharing a vertex form a triple in $ S $ . A Steiner triple system $ S $ is called universal if any (simple) cubic graph is $ S $ -colorable. It is easy to see that if $ S_3 $ denotes the trivial Steiner triple system with three points and one triple, then $ S_3 $ -colorable graphs are precisely (cubic) edge-3-colorable graphs. For the same reason, any cubic edge-3-colorable graph is $ S $ -colorable for any Steiner triple system (with at least one edge). Thus, the study of $ S $ -colorings may be viewed as an attempt to understand snarks . It is not hard to see, that a graph is Fano-colorable iff it has a nowhere-zero 8-flow. Thus (by Jaeger's result) Fano plane is "almost universal": it is possible to use it to color any bridgeless cubic graph (but it doesn't work for any graph with a bridge). Grannell et al. [GGKS] constructed a universal Steiner triple system of order 381. Holroyd, Skoviera [HS] proved that neither projective nor affine Steiner triple systems are universal. Kral et al. [KMPS] proved that any non-affine non-projective non-trivial point-transitive Steiner triple system is universal.

=== References listed by OpenProblemGarden ===
- *[GGKS] M.J. Grannell, T.S. Griggs, M. Knor, M. Skoviera, A Steiner triple system which colours all cubic graphs, J. Graph Theory 46 (2004), 15--24. MathSciNet
- [HS] F. Holroyd and M. Skoviera, Colouring of cubic graphs by Steiner triple systems, J.~Combin. Theory Ser. B 91 (2004), 57--66.
- [KMPS] D. Kral, E. Macajova, A. Por, J.-S. Sereni, Characterization results for Steiner triple systems and their application to edge-colorings of cubic graphs, preprint.

=== Catalog page (statement + literature review) ===
Universal Steiner triple systems — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 The preprint [KMPS] cited on the OPG page was published in 2010 in the Canadian Journal of Mathematics, formally establishing that every non-projective, non-affine, non-trivial point-transitive Steiner triple system is universal. A 2013 paper by Grannell, Griggs, Máčajová, and Škoviera addressed point-intransitive systems, constructing both an infinite family of universal point-intransitive STS containing no proper universal subsystem and an infinite family of non-universal STS that are neither projective nor affine; however, a complete characterization of all universal Steiner triple systems remains open.

 Cited literature (1)

 
 
 
partial Characterisation Results for Steiner Triple Systems and Their Application to Edge-Colourings of Cubic Graphs
 (2010)
 

 
 Daniel Král', Edita Máčajová, Attila Pór, Jean-Sébastien Sereni · Canadian Journal of Mathematics · doi:10.4153/CJM-2010-021-9

Proves that all cubic graphs are $S$-edge-colourable for every non-projective non-affine point-transitive Steiner triple system $S$, completing the characterization of universality within the class of point-transitive STS.
 

 

 Reviewer notes. Multiple search results consistently report a 2013 paper by Grannell, Griggs, Máčajová, Škoviera ('Coloring cubic graphs by point-intransitive Steiner triple systems', J. Graph Theory 74, 163–181, DOI 10.1002/jgt.21696) that extends results to point-intransitive STS; however, all attempts to fetch this paper's URL returned HTTP 403, so it is not included in since_posted per the verification rule. The Kral et al. result appeared as a preprint when the OPG was posted but only the published (2010) journal version is cited here. No arXiv preprints on this topic were found. The full classification of which Steiner triple systems are universal (including non-point-transitive ones) appears to remain open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Problem. Which Steiner triple systems are universal?

Keywords:
cubic graph · Steiner triple system

Discussion

A cubic graph $ G $ is $ S $ -edge-colorable for a Steiner triple system $ S $ if its edges can be colored with the points of $ S $ in such a way that the points assigned to three edges sharing a vertex form a triple in $ S $ . A Steiner triple system $ S $ is called universal if any (simple) cubic graph is $ S $ -colorable. It is easy to see that if $ S_3 $ denotes the trivial Steiner triple system with three points and one triple, then $ S_3 $ -colorable graphs are precisely (cubic) edge-3-colorable graphs. For the same reason, any cubic edge-3-colorable graph is $ S $ -colorable for any Steiner triple system (with at least one edge). Thus, the study of $ S $ -colorings may be viewed as an attempt to understand snarks . It is not hard to see, that a graph is Fano-colorable iff it has a nowhere-zero 8-flow. Thus (by Jaeger's result) Fano plane is "almost universal": it is possible to use it to color any bridgeless cubic graph (but it doesn't work for any graph with a bridge). Grannell et al. [GGKS] constructed a universal Steiner triple system of order 381. Holroyd, Skoviera [HS] proved that neither projective nor affine Steiner triple systems are universal. Kral et al. [KMPS] proved that any non-affine non-projective non-trivial point-transitive Steiner triple system is universal.

Bibliography

★ [GGKS]
 M.J. Grannell, T.S. Griggs, M. Knor, M. Skoviera, A Steiner triple system which colours all cubic graphs , J. Graph Theory 46 (2004), 15--24. MathSciNet
 MathSciNet

 [HS]
 F. Holroyd and M. Skoviera, Colouring of cubic graphs by Steiner triple systems , J.~Combin. Theory Ser. B 91 (2004), 57--66.

 [KMPS]
 D. Kral, E. Macajova, A. Por, J.-S. Sereni, Characterization results for Steiner triple systems and their application to edge-colorings of cubic graphs , preprint.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit infinite family of non-projective, non-affine Steiner triple systems has maximal binary and ternary incidence ranks but fails to color a fixed 16-vertex simple cubic graph.",
  "would_publish": false,
  "caveats": "This does not characterize all universal systems, and novelty relative to the intransitive-system constructions mentioned in the question has not been verified."
}
```

## 1. Scope and partial result

I do not obtain a complete characterization. The following construction gives a self-contained obstruction that is invisible to the usual binary incidence-kernel test.

Throughout, Steiner triple systems are finite, and their triples consist of three distinct points.

**Theorem.** For every integer \(k\geq 1\), there is an explicitly specified Steiner triple system \(S_k\) of order
\[
v=64^k-1
\]
with the following properties.

1. A fixed simple cubic graph \(H\) on \(16\) vertices is not \(S_k\)-edge-colorable.
2. \(S_k\) is neither projective nor affine, and is point-intransitive.
3. If \(M_k\) is its triple-versus-point incidence matrix, then
   \[
   \operatorname{rank}_{\mathbb F_2} M_k=v,
   \qquad
   \operatorname{rank}_{\mathbb F_3} M_k=v-1.
   \]
   Both ranks are maximal: over \(\mathbb F_3\), the all-ones vector is always in the kernel.

The smallest member has \(63\) points. Its construction changes just \(24\) triples of the projective STS of order \(63\).

I also give an exact, polynomial-time criterion for colorability of a natural infinite family of cubic graphs built from copies of the same five-vertex balloon.

No literature results are needed for these assertions. I make no claim that the construction is new.

## 2. A five-vertex balloon and its palette

Let \(D\) be obtained from \(K_4\), with vertices \(u,v,r,s\), by subdividing \(uv\) with a vertex \(w\), and adding a dangling edge at \(w\). Thus \(D\) has five internal vertices, all of degree three when the dangling edge is counted.

For an STS \(S=(P,\mathcal B)\), define its **\(K_4\)-balloon palette**
\[
\beta(S)=\{p\in P:\text{\(D\) has an \(S\)-coloring with dangling-edge color \(p\)}\}.
\]

Now take three disjoint copies of the subdivided \(K_4\), and join their subdivision vertices to one new vertex. Call the resulting graph \(H\). It is simple and cubic, with \(3\cdot5+1=16\) vertices.

Directly from the definition,
\[
\boxed{\quad H\text{ is }S\text{-colorable}
\iff
\beta(S)\text{ contains a triple of }S.\quad}                 \tag{1}
\]
Indeed, the three edges at the new central vertex must receive a triple contained in \(\beta(S)\). Conversely, any such triple permits independent colorings of the three balloons.

### An algebraic formula

Write \(x*y\) for the third point of the triple containing distinct points \(x,y\), and set \(x*x=x\).

Assign colors
\[
c(rs)=z,\qquad c(ur)=x,\qquad c(us)=y.
\]
The remaining colors are forced:
\[
\begin{aligned}
c(vr)&=x*z,& c(vs)&=y*z,\\
c(uw)&=x*y,& c(vw)&=(x*z)*(y*z).
\end{aligned}
\]
Consequently,
\[
\beta(S)=
\left\{
(x*y)*\bigl((x*z)*(y*z)\bigr):
\begin{array}{l}
x,y,z\text{ pairwise distinct},\\
x*y\ne (x*z)*(y*z)
\end{array}
\right\}.                                                  \tag{2}
\]
These conditions are sufficient as well as necessary: multiplication by \(z\) is a permutation, so the two colors at \(v\) are distinct.

Thus, given the completion table of \(S\), the obstruction in (1) can be tested in \(O(|P|^3)\) time.

### An exact special-case characterization

Consider all graphs obtained from a finite tree whose vertex degrees are \(1\) or \(3\), by replacing each leaf with a copy of the balloon \(D\), using its dangling edge as the corresponding tree edge.

Then
\[
\boxed{\quad
\text{Every graph in this family is \(S\)-colorable}
\iff
\beta(S)\text{ contains a triple}.
\quad}                                                     \tag{3}
\]

Necessity follows from \(H\). For sufficiency, properly edge-color the underlying tree using a fixed triple contained in \(\beta(S)\), and extend independently into each balloon.

## 3. Disjoint switches inside a projective system

Let \(V\) be a vector space over \(\mathbb F_2\), of dimension \(d\geq4\). Start with the projective STS
\[
P=V\setminus\{0\},\qquad
\mathcal B_0=\{\{x,y,x+y\}:x,y\in P,\ x\ne y\}.
\]

Suppose
\[
U_1,\ldots,U_t\leq V
\]
are three-dimensional subspaces satisfying
\[
U_i\cap U_j=\{0\}\qquad(i\ne j).
\]
Choose a distinguished point \(a_i\in U_i\setminus\{0\}\) for each \(i\), and put
\[
P_i=U_i\setminus\{0,a_i\}.
\]

Within the Fano subsystem on \(U_i\setminus\{0\}\):

* remove its four triples not containing \(a_i\);
* insert the four triples
  \[
  \{x,y,z\}\subseteq P_i,\qquad x+y+z=a_i.
  \]

Call the resulting system \(S\).

### Verification that \(S\) is an STS

The sets \(P_i\) are pairwise disjoint, so different switches do not interfere.

For distinct \(x,y\in P_i\):

* if \(x+y=a_i\), their original triple \(\{x,y,a_i\}\) is retained;
* otherwise their old third point \(x+y\) is replaced by
  \[
  x+y+a_i.
  \]
  This is a point of \(P_i\), distinct from \(x,y\).

Pairs involving \(a_i\), and pairs not contained in any \(P_i\), retain their original triples. Every pair therefore belongs to exactly one triple.

An unchanged triple has vector sum \(0\); a newly inserted triple of switch \(i\) has vector sum \(a_i\).

## 4. The balloon palette is exactly the set of switch centers

The crucial fact is
\[
\boxed{\qquad \beta(S)=\{a_1,\ldots,a_t\}.\qquad}              \tag{4}
\]

### Every \(a_i\) occurs

Choose \(x,y\in P_i\) so that \(\{x,y,x+y\}\) is one of the removed triples, and choose \(z\notin U_i\).

The pairs \(\{x,z\}\) and \(\{y,z\}\) are unaffected by every switch. Also, the old triple
\[
\{x+z,y+z,x+y\}
\]
is unchanged: it contains the nonzero point \(x+y\in U_i\) and points outside \(U_i\), so cannot lie in any switching subspace.

Hence
\[
x*y=x+y+a_i,\qquad
x*z=x+z,\qquad
y*z=y+z,
\]
and
\[
(x*z)*(y*z)=x+y.
\]
The triple
\[
\{x+y+a_i,x+y,a_i\}
\]
is retained. Formula (2) therefore gives \(a_i\in\beta(S)\).

### No other point occurs

Consider an \(S\)-coloring of \(D\), and let \(q\) be its dangling-edge color.

Call an internal vertex **switched of type \(i\)** if its incident colors form a newly inserted triple from switch \(i\). At such a vertex, the vector sum of incident colors is \(a_i\); at every other vertex it is \(0\).

Summing over the five internal vertices cancels every internal edge twice, giving
\[
q=\sum_{i=1}^t n_i a_i,                                    \tag{5}
\]
where \(n_i\) is the number of type-\(i\) vertices, reduced modulo \(2\).

Adjacent switched vertices cannot have different types: their common edge color would have to lie in two disjoint sets \(P_i,P_j\).

The internal graph of \(D\) has independence number \(2\). Therefore at most two different switch types can occur.

If only one type has odd multiplicity, (5) already gives \(q=a_i\). The only remaining possibility is
\[
q=a_i+a_j,\qquad i\ne j,
\]
with both types occurring oddly.

Since \(U_i\cap U_j=\{0\}\), the point \(a_i+a_j\) belongs to neither \(U_i\) nor \(U_j\). Thus the subdivision vertex \(w\), incident with the dangling edge, cannot be switched. The two different types must consequently occur among the four original vertices of \(K_4-uv\).

Its only nonadjacent pair is \(u,v\). Hence \(u\) and \(v\) have types \(i,j\), respectively, while \(r,s\) are unswitched.

Let the colors on \(ur,us\) be \(x_1,x_2\in U_i\), and those on \(vr,vs\) be \(y_1,y_2\in U_j\). If \(c(rs)=z\), the unchanged triples at \(r,s\) give
\[
x_1+y_1+z=0,\qquad x_2+y_2+z=0.
\]
Thus
\[
x_1+x_2=y_1+y_2\in U_i\cap U_j=\{0\}.
\]
This forces \(x_1=x_2\), contradicting distinctness of the incident colors at \(u\).

The remaining possibility is impossible, proving (4).

Combining (1) and (4), this switching construction is non-universal whenever its set of distinguished points contains no triple.

## 5. An explicit 63-point example and the infinite family

Let
\[
\mathbb F_8=\mathbb F_2[\alpha]/(\alpha^3+\alpha+1).
\]
In \(\mathbb F_8^2\), take
\[
\begin{aligned}
a_1&=(1,0),&
a_2&=(0,1),\\
a_3&=(\alpha,1),&
a_4&=(\alpha^2,1),\\
a_5&=(1,\alpha),&
a_6&=(1,\alpha^2).
\end{aligned}                                               \tag{6}
\]
Set
\[
U_i=\mathbb F_8 a_i.
\]

Each \(U_i\) is three-dimensional over \(\mathbb F_2\). Their slopes are
\[
0,\ \infty,\ \alpha^{-1},\ \alpha^{-2},\ \alpha,\ \alpha^2,
\]
which are distinct, so they intersect pairwise only in \(0\).

Moreover, the six vectors in (6) form an \(\mathbb F_2\)-basis of \(\mathbb F_8^2\). Indeed, comparison of the coefficients of \(\alpha,\alpha^2\) in the two coordinates of a binary linear relation first annihilates the coefficients of \(a_3,a_4,a_5,a_6\), and then those of \(a_1,a_2\).

Perform the six switches from Section 3. This specifies an STS on
\[
|\mathbb F_8^2|-1=63
\]
points: begin with the \(651\) projective triples, remove the indicated \(24\), and insert the specified \(24\).

Its balloon palette is exactly
\[
\{a_1,\ldots,a_6\}.
\]
This set contains no unchanged triple, because it is linearly independent. It contains no new triple either: a new triple lies in \(P_i\), while none of the distinguished points lies in any \(P_i\). Hence \(H\) is not colorable.

For the infinite family, take
\[
V=(\mathbb F_8^2)^k
\]
and perform these six switches separately in each coordinate pair. All \(6k\) switching subspaces remain pairwise disjoint outside \(0\), and their \(6k\) distinguished points form an \(\mathbb F_2\)-basis of \(V\).

The resulting system has order \(64^k-1\), its palette is this basis, and the same graph \(H\) is an obstruction.

The palette is intrinsic and invariant under every automorphism of the STS. Since it is a nonempty proper subset of the point set, these systems are point-intransitive.

## 6. Incidence-rank calculations

These calculations show that the obstruction is not merely a surviving projective flow obstruction.

### Binary rank

More generally, for the switched system of Section 3,
\[
\dim_{\mathbb F_2}\ker M
=
d-\dim_{\mathbb F_2}\langle a_1,\ldots,a_t\rangle.             \tag{7}
\]

To prove this, let \(f:P\to\mathbb F_2\) satisfy
\[
f(x)+f(y)+f(z)=0
\]
on every triple of the switched system.

Take a removed old triple \(\{x,y,x+y\}\subset U_i\), and choose \(z\notin U_i\). The following three old triples are all unchanged:
\[
\{x,z,x+z\},\quad
\{y,z,y+z\},\quad
\{x+z,y+z,x+y\}.
\]
Summing their equations over \(\mathbb F_2\) gives
\[
f(x)+f(y)+f(x+y)=0.
\]
Thus \(f\) satisfies every original projective triple equation. Extending it by \(f(0)=0\), it is a linear functional on \(V\).

For such a functional, a new type-\(i\) triple satisfies its equation precisely when \(f(a_i)=0\). Conversely, every linear functional annihilating all the \(a_i\) satisfies every new and unchanged triple. This proves (7).

In our construction the \(a_i\) span \(V\), so the kernel is zero and
\[
\operatorname{rank}_{\mathbb F_2}M_k=v.
\]

### Ternary rank

For every switched system in Section 3,
\[
\dim_{\mathbb F_3}\ker M=1.                                 \tag{8}
\]

Let \(f:P\to\mathbb F_3\) satisfy its triple equations. Again take a removed old triple
\[
L=\{x,y,x+y\}\subset U_i
\]
and \(z\notin U_i\). Inside the Fano plane on
\[
\langle x,y,z\rangle\setminus\{0\},
\]
each of the six old lines other than \(L\) contains one nonzero point of \(U_i\) and two points outside \(U_i\). All six are therefore unchanged.

The sum of the seven Fano line-incidence vectors is zero over \(\mathbb F_3\), since every point lies on three lines. Consequently, the equation for \(L\) follows from those for the other six lines. Hence \(f\) satisfies every original projective triple equation.

On a Fano plane, if \(N\) is its incidence matrix, then
\[
N^{\mathsf T}N=2I+J.
\]
Over \(\mathbb F_3\), \(Nf=0\) implies
\[
-f+\left(\sum f\right)\mathbf1=0,
\]
so \(f\) is constant on that Fano plane. Any two points of \(V\setminus\{0\}\) lie in a three-dimensional subspace, so \(f\) is globally constant.

Conversely, every constant function satisfies every STS triple equation over \(\mathbb F_3\). This proves (8), and hence
\[
\operatorname{rank}_{\mathbb F_3}M_k=v-1.
\]

### Neither projective nor affine

A projective STS has nonzero binary-kernel functions given by its vector-space coordinates. Our systems have zero binary kernel, so are not projective.

An affine STS has order a power of \(3\). But
\[
64^k-1\equiv7\pmod8,
\]
whereas powers of \(3\) are congruent to \(1\) or \(3\pmod8\). Thus these systems are not affine.

This completes the proof of the stated partial theorem.

## 7. What this does—and does not—settle

The result gives:

* an explicit fixed-graph obstruction;
* an exact classification for the balloon-tree family in (3);
* infinitely many non-universal, point-intransitive STS for which both indicated incidence ranks are maximal.

The balloon-palette condition is **not** sufficient for universality. For example, in the affine STS on \(\mathbb F_3^2\), where
\[
x*y=-x-y,
\]
formula (2) gives \(\beta(S)=P\): for any \(z\), choose \(x,y,z\) distinct with \(x+y+z\ne0\); the resulting dangling-edge color is \(z\).

Nevertheless, this affine system fails on a different explicit graph. Take two copies of \(K_{3,3}\), subdivide one edge in each, and join the two subdivision vertices. This is a simple cubic graph on \(14\) vertices. In either copy, sum the affine triple equations over one original bipartition class and subtract those over the other. Internal edges cancel, forcing the two colors incident with the subdivision vertex from that copy to be equal—a contradiction.

Thus the construction isolates a genuine obstruction mechanism, but neither it nor the palette test answers which arbitrary STS are universal. A complete characterization remains unresolved here.
