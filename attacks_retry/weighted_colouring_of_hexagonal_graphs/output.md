```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured coefficient, with an explicit additive constant, for triangle-free hexagonal graphs that are odd subdivisions of K4, and prove that these graphs are (9,4)-colourable.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not settled; novelty of the special-case results is not claimed, and the additive constant is not optimized."
}
```

## 1. Result and scope

All graphs below are finite. An **odd subdivision of \(K_4\)** is obtained by replacing each of its six edges by an internally vertex-disjoint path of positive odd length.

I prove the following.

**Theorem 1.** Let \(G\) be a triangle-free hexagonal graph that is an odd subdivision of \(K_4\). Then
\[
\chi(G,\mathbf4)\le 9.
\]
Furthermore, for every integer demand function \(p\ge 0\), writing \(W=\omega(G,p)\), we have
\[
\boxed{\quad
\chi(G,p)\le \left\lceil\frac98W\right\rceil+14
\le \frac98W+15.
\quad}
\]

In particular,
\[
\alpha(G)\ge \frac49|V(G)|.
\]

These graphs have a \(K_4\) minor, so this result is outside the series-parallel class considered in the previous attempt. The main geometric point is that the lattice excludes exactly the small obstruction arising in the following classification.

**Theorem 2.** Let \(H\) be an odd subdivision of \(K_4\). Then
\[
\boxed{\quad
\chi(H,\mathbf4)\le9
\quad\Longleftrightarrow\quad
\text{\(H\) has odd girth at least \(9\) and }|V(H)|\ge18.
\quad}
\]

The proofs are self-contained. I independently verify the turning observation from the previous attempt and prove the path-overlap fact used here; I do not assume its general series-parallel multicolouring lemma.

---

## 2. Multicolouring a path with prescribed endpoint sets

We first need an exact elementary extension criterion.

**Lemma 3.** Let
\[
P=v_0v_1\cdots v_\ell
\]
be a path, with integer demands satisfying
\[
p(v_i)\le K,\qquad p(v_i)+p(v_{i+1})\le K.
\]
Put
\[
a=p(v_0),\qquad c=p(v_\ell),\qquad S=p(V(P)).
\]
For a \(K\)-colouring, let \(z\) be the intersection size of the endpoint colour sets.

If \(\ell=2r\), the possible values of \(z\) are exactly the integers in
\[
\left[
\max(0,a+c-K,S-rK),\ \min(a,c)
\right].
\tag{1}
\]
If \(\ell=2r+1\), they are exactly the integers in
\[
\left[
\max(0,a+c-K),\
\min(a,c,rK-S+a+c)
\right].
\tag{2}
\]
Moreover, any prescribed pair of endpoint sets having an admissible intersection size can be extended.

**Proof.**
A single edge gives the interval \(\{0\}\).

For the induction step, suppose a path ends at a vertex of demand \(b\), and its attainable overlap with its first endpoint is the integer interval \([L,U]\). Append a vertex of demand \(c\).

For a fixed old overlap \(x\), the new endpoint must receive \(c\) colours outside the old endpoint's \(b\)-element set. Consequently its overlap with the first endpoint ranges over all integers between
\[
\max(0,a+b+c-K-x)
\quad\text{and}\quad
\min(a-x,c).
\tag{3}
\]
These are elementary subset-intersection bounds, and every intermediate integer is attainable.

As \(x\) increases by one, both endpoints in (3) decrease by at most one. Thus the union has no integer gaps and is exactly
\[
\left[
\max(0,a+b+c-K-U),\
\min(c,a-L)
\right].
\tag{4}
\]
It is nonempty: any colouring of the old path can be extended to its new final vertex because \(b+c\le K\).

Substituting the two induction formulas into (4) gives (1) and (2). In the simplification, terms \(b+c-K\) are nonpositive and terms \(K-b\) are redundant upper bounds because \(c\le K-b\).

Finally, two ordered pairs of subsets of a \(K\)-element palette with the same sizes and intersection size are related by a permutation of that palette. Hence attainability of an overlap implies extension for any prescribed endpoint sets with that overlap. ∎

For uniform demand \(4\), palette size \(9\), and a path of odd length \(2r+1\), the criterion simplifies to
\[
|C(v_0)\cap C(v_{2r+1})|\le r.
\tag{5}
\]

---

## 3. A four-set intersection lemma

The following small lemma is the combinatorial core.

**Lemma 4.** Let \(r_{ij}\) be nonnegative integers for \(1\le i<j\le4\). There exist four \(4\)-element subsets \(A_1,\dots,A_4\) of a \(9\)-element set satisfying
\[
|A_i\cap A_j|\le r_{ij}
\tag{6}
\]
if and only if
\[
r_{ij}+r_{ik}+r_{jk}\ge3
\qquad\text{for every triple }\{i,j,k\},
\tag{7}
\]
and
\[
\sum_{i<j}r_{ij}\ge7.
\tag{8}
\]

**Necessity.**
For any collection of subsets,
\[
\sum_i |A_i|
\le \left|\bigcup_i A_i\right|+\sum_{i<j}|A_i\cap A_j|.
\]
Apply this to three sets, whose total size is \(12\), and to all four sets, whose total size is \(16\). Since the union has size at most \(9\), we obtain (7) and (8). ∎

Here is a complete constructive proof of sufficiency.

Let \(Z\) be the graph on \(\{1,2,3,4\}\) whose edges are the pairs with \(r_{ij}=0\). By (7), \(Z\) is triangle-free. We consider its possible isomorphism types.

A **colour supported on \(ij\)** means a fresh colour put in exactly \(A_i,A_j\); supports of size one or three have the analogous meaning. Repeated supports use distinct colours.

### No zero pairs

All six capacities are at least one, and (8) makes some capacity at least two. Use one colour on each pair, and a second colour on a pair whose capacity is at least two.

This gives seven colours and membership counts \(4,4,3,3\), up to permutation. Add two singleton-supported colours.

### Exactly one zero pair

Let it be \(12\). Start with one colour on each of the five other pairs.

Condition (7) provides a capacity at least two in each of
\[
\{13,23\},\qquad \{14,24\}.
\]
Add one extra pair-supported colour from each of those two choices. There are now seven colours, no set has size more than four, and the total membership count is fourteen. Add two singleton-supported colours.

### Two adjacent zero pairs

Let them be \(12,13\). Then
\[
r_{23}\ge3,\qquad
r_{14}+r_{24}\ge3,\qquad
r_{14}+r_{34}\ge3.
\]

If \(r_{14}\ge2\), use
\[
2[14]+3[23]+[24]+[34]+2[1].
\tag{9}
\]
Here, for example, \(2[14]\) denotes two fresh colours supported on \(14\).

If \(r_{14}=1\), then \(r_{24},r_{34}\ge2\), and we use
\[
[234]+[14]+2[23]+[24]+[34]+3[1].
\tag{10}
\]
Both constructions use nine colours, give every set size four, and respect all capacities.

### Two disjoint zero pairs

Let them be \(12,34\). The other four pairs form \(K_{2,2}\), with sides \(\{1,2\}\) and \(\{3,4\}\).

Start with one colour on each of these four pairs and put
\[
\delta_{ij}=r_{ij}-1
\]
on them. Conditions (7) imply that the sum of the \(\delta\)'s incident with each vertex is at least one; condition (8) gives
\[
\sum \delta_{ij}\ge3.
\]

We can select three additional pair-supported colours, respecting these residual capacities, with additional degree at most two at every vertex:

* If every \(\delta_{ij}\le1\), select any three positive residual edges.
* Otherwise, let an edge \(e\) have residual capacity at least two. If its opposite edge has positive residual capacity, take \(e\) twice and the opposite edge once.
* If the opposite edge has zero residual capacity, the other two edges both have positive residual capacity. Take those two and \(e\) once each.

Together with the original four colours, this gives seven pair-supported colours and set sizes at most four. Two singleton-supported colours finish the construction.

### Three or four zero pairs

A triangle-free graph on four vertices with three edges is a star or a path; with four edges it is a \(4\)-cycle. The following table covers these remaining cases.

| Zero pairs | Capacities forced by (7)–(8) | Nine colour supports |
|---|---|---|
| \(12,13,14\) | \(r_{23},r_{24},r_{34}\ge3\) | \(2[234]+[23]+[24]+[34]+4[1]\) |
| \(12,23,34\) | \(r_{13},r_{24}\ge3,\ r_{14}\ge1\) | \(3[13]+[14]+3[24]+[2]+[3]\) |
| \(12,23,34,14\) | \(r_{13},r_{24}\ge3\), one at least \(4\) | \(4[13]+3[24]+[2]+[4]\), after relabelling |

Every listed construction has all four set sizes equal to four. There are no other possible zero graphs. This proves sufficiency and Lemma 4. ∎

---

## 4. Exact classification for odd subdivisions of \(K_4\)

Let the four branch vertices of an odd subdivision \(H\) be \(1,2,3,4\), and write the length of its \(ij\)-path as
\[
\ell_{ij}=2r_{ij}+1.
\]

By Lemma 3, a choice of four branch-vertex colour sets extends to a \((9,4)\)-colouring precisely when
\[
|A_i\cap A_j|\le r_{ij}
\]
for all six pairs. The six extensions can be performed independently because their internal vertices are disjoint.

Lemma 4 therefore characterizes \((9,4)\)-colourability by
\[
r_{ij}+r_{ik}+r_{jk}\ge3
\quad\text{for every triple},
\qquad
\sum_{i<j}r_{ij}\ge7.
\tag{11}
\]

A cycle corresponding to a triangle \(ijk\) of \(K_4\) has length
\[
2(r_{ij}+r_{ik}+r_{jk})+3.
\]
These are exactly the odd cycles of \(H\): cycles corresponding to \(4\)-cycles of \(K_4\) have even length. Thus the first group of conditions in (11) is exactly odd girth at least \(9\).

Also,
\[
|V(H)|
=4+\sum_{i<j}(\ell_{ij}-1)
=4+2\sum_{i<j}r_{ij}.
\]
The last condition in (11) is therefore exactly \(|V(H)|\ge18\). This proves Theorem 2. ∎

One obstruction deserves emphasis. When the odd girth is at least \(9\) but \(|V(H)|=16\), the four branch sets would have total pairwise intersection capacity only six, whereas four \(4\)-sets in nine colours require at least seven. The lattice argument below rules this obstruction out.

---

## 5. Why the triangular lattice excludes the obstruction

We use the natural straight-line embedding of the triangular lattice.

### 5.1 Odd girth

**Lemma 5.** A triangle-free induced subgraph of the triangular lattice has odd girth at least \(9\).

**Proof.**
Orient a simple cycle counterclockwise. Its edge directions are multiples of \(60^\circ\).

A turn of \(120^\circ\) or \(-120^\circ\) makes the preceding and succeeding vertices lattice neighbours. Inducedness would then give a triangle. A \(180^\circ\) turn repeats the preceding vertex. Thus every turn is \(60^\circ\), \(0^\circ\), or \(-60^\circ\).

Let their respective counts be \(n_+,n_0,n_-\). The turning-angle theorem gives
\[
n_+-n_-=6.
\tag{12}
\]
Hence every cycle has length at least six.

For a \(7\)-cycle, (12) forces
\[
n_+=6,\qquad n_0=1,\qquad n_-=0.
\]
Its seven edge directions would consequently consist of all six lattice directions once, with one repeated. Their sum is the repeated unit vector, not zero, contradicting closure.

There are therefore no odd cycles shorter than nine. ∎

### 5.2 Boundary curvature at branch vertices

The neighbours of a lattice vertex induce a \(6\)-cycle. Consequently, in a triangle-free hexagonal graph, every vertex has degree at most three, and a degree-three vertex has its incident edges spaced at \(120^\circ\).

Now let \(G\) be an odd subdivision of \(K_4\). Suppressing its degree-two vertices yields a plane embedding of \(K_4\). Its four facial boundaries correspond to the four triangles of \(K_4\), so each facial boundary of \(G\) is odd.

The outer facial boundary contains exactly three branch vertices. At each such vertex, the third incident edge lies inside the outer boundary. Because the three incident directions are spaced at \(120^\circ\), the polygon's interior angle there is \(240^\circ\). Thus each of these three vertices contributes a turn of \(-60^\circ\).

For the outer boundary, therefore,
\[
n_-\ge3.
\]
Using (12),
\[
|\partial_{\rm out}G|
=n_++n_0+n_-
=6+2n_-+n_0
\ge12.
\]
Since this boundary is odd,
\[
|\partial_{\rm out}G|\ge13.
\tag{13}
\]

Each of the other three facial cycles has length at least nine by Lemma 5. Summing facial lengths gives
\[
2|E(G)|\ge13+3\cdot9=40.
\]
As a subdivision of \(K_4\),
\[
|V(G)|=|E(G)|-2\ge18.
\]
Theorem 2 now supplies a \((9,4)\)-colouring.

Finally, its nine stable colour classes contain altogether \(4|V(G)|\) incidences, so one has size at least \(4|V(G)|/9\).

### A non-vacuous example

Here is an explicit member of the class. In integer lattice coordinates, let
\[
R(a,b)=(-a-b,a),
\]
the \(120^\circ\) rotation. Take the radial path
\[
(0,0),(1,0),(2,0),(3,0)
\]
and its two rotations, together with the path
\[
\begin{split}
&(3,0),(3,1),(3,2),(3,3),(2,4),(1,5),\\
&(0,5),(-1,5),(-2,5),(-3,5),(-3,4),(-3,3)
\end{split}
\]
and its two rotations.

Their forty vertices induce an odd subdivision of \(K_4\): the three radial paths have length three and the three outer paths have length eleven. This can be checked directly using the six allowable differences
\[
\pm(1,0),\quad \pm(0,1),\quad \pm(1,-1).
\]
There are no edges other than consecutive pairs on the stated paths.

---

## 6. From uniform \((9,4)\)-colourability to weighted fractional colouring

A **fractional colouring of length \(T\)** assigns to each vertex a measurable subset of \([0,T)\), of measure equal to its demand, with adjacent vertices receiving disjoint subsets. Only finite unions of intervals are needed below.

**Lemma 6.** If a graph \(F\) has a \((9,4)\)-colouring, then every integer demand function \(p\) admits a fractional colouring of length
\[
\frac98 W,
\qquad
W=\max\!\left(
\max_v p(v),\ \max_{uv\in E(F)}(p(u)+p(v))
\right).
\tag{14}
\]

**Proof.**
The case \(W=0\) is immediate. Consider the polytope
\[
Q(F)=
\left\{
x\in[0,1]^{V(F)}:
x_u+x_v\le1\text{ for every }uv\in E(F)
\right\}.
\]

Every vertex of \(Q(F)\) is half-integral. Here is the usual short proof. Among coordinates strictly between zero and one, consider the graph of tight equations \(x_u+x_v=1\). A bipartite component permits a sufficiently small alternating perturbation, contradicting extremality. Every remaining component contains an odd cycle, which forces all its coordinates to equal \(1/2\). Thus every coordinate of a vertex of \(Q(F)\) belongs to \(\{0,1/2,1\}\).

For such a half-integral point \(x\), put
\[
I=\{v:x_v=1\},\qquad J=\{v:x_v=1/2\}.
\]
The set \(I\) is stable and has no edges to \(J\). Restrict the given \((9,4)\)-colouring to \(J\), and give each of its nine colours an interval of length \(1/8\). This meets demand \(1/2\) at every vertex of \(J\) in a palette of length \(9/8\).

Vertices in \(I\) may all receive the same eight of these nine intervals, meeting demand one without conflict. Coordinates equal to zero require nothing.

Now \(p/W\in Q(F)\). Express it as a convex combination of vertices of \(Q(F)\), concatenate the correspondingly scaled fractional colourings, and multiply lengths by \(W\). The result has length \(9W/8\) and meets demands exactly. ∎

For the graph in Theorem 1, which is triangle-free, the quantity \(W\) in (14) is precisely \(\omega(G,p)\).

The remaining issue is integral rounding. The next lemma handles it with a constant independent of the subdivision lengths.

---

## 7. Rounding on a subdivision of \(K_4\)

**Lemma 7.** Let \(H\) be any subdivision of \(K_4\), with integer demands. If it has a fractional colouring of length \(T\), then
\[
\chi(H,p)\le \lceil T\rceil+14.
\tag{15}
\]

**Proof.**
Let \(B\) be the set of four branch vertices. Partition the fractional palette according to which branch vertices receive each point. For \(S\subseteq B\), let \(x_S\) be the measure of the region with branch-incidence pattern exactly \(S\). Thus
\[
\sum_{S\subseteq B}x_S=T,
\qquad
\sum_{S\ni i}x_S=p(i).
\]

For each nonempty \(S\), create \(\lceil x_S\rceil\) integer colours, initially assigned to exactly the branch vertices in \(S\). There are fifteen nonempty patterns, so the number \(N\) of created colours satisfies
\[
N<T+15,
\qquad\text{hence}\qquad
N\le\lceil T\rceil+14.
\tag{16}
\]

At branch vertex \(i\), the excess number of assigned colours is
\[
d_i=\sum_{S\ni i}(\lceil x_S\rceil-x_S).
\]
There are eight patterns containing \(i\). Since \(d_i\) is an integer,
\[
0\le d_i<8,\qquad d_i\le7.
\]
Delete any \(d_i\) assigned colours from vertex \(i\), leaving exactly its required demand.

Let \(z_{ij}\) be the original fractional overlap of branch vertices \(i,j\), and \(z'_{ij}\) their new integer overlap. Four patterns contain both vertices. Rounding up increases their overlap by less than four; the deletions reduce it by at most \(d_i+d_j\le14\). Therefore
\[
z_{ij}-14\le z'_{ij}<z_{ij}+4.
\tag{17}
\]

Set
\[
K=\lceil T\rceil+14,
\]
and regard the constructed colours as part of a \(K\)-element palette.

We check that every replacement path can be extended with these fixed endpoint sets. Let its endpoint demands be \(a,c\), and its total demand be \(S\).

The necessary path-overlap bounds also hold for fractional colourings. For an even path of length \(2r\), each colour appears on at most \(r\) vertices unless it appears at both endpoints, giving
\[
z_{ij}\ge S-rT.
\tag{18}
\]
For an odd path of length \(2r+1\), a colour occurring at both endpoints can occur on at most \(r-1\) internal vertices, giving
\[
z_{ij}\le rT-S+a+c.
\tag{19}
\]

For an even replacement path, \(r\ge1\), and (17)–(18) imply
\[
z'_{ij}
\ge S-rT-14
\ge S-rK.
\]
For an odd replacement path of length at least three, \(r\ge1\), and (17)–(19) imply
\[
z'_{ij}
<rT-S+a+c+4
\le rK-S+a+c.
\]

If a replacement path consists of a single edge, its original fractional endpoint overlap is zero. Every pattern containing both endpoints consequently has measure zero and creates no colour. Their new overlap is still zero.

All vertex and edge demand inequalities hold for palette size \(K\), since they already hold fractionally at length \(T\). The elementary endpoint-intersection bounds hold automatically for the actual endpoint sets. Lemma 3 therefore extends these sets along each path.

The six extensions coexist because the paths have disjoint interiors. This proves (15). ∎

Applying Lemma 6 with \(T=9W/8\), then Lemma 7, completes the weighted assertion of Theorem 1.

---

## 8. Extensions and the remaining gap

The weighted bound also survives gluing at cutvertices. Specifically, it holds for a hexagonal graph whose blocks are each:

* bipartite;
* a triangle; or
* triangle-free odd subdivisions of \(K_4\).

A bipartite block has weighted chromatic number equal to its weighted clique number: assign initial palette segments on one side and final segments on the other. A triangle also needs exactly its total demand. Colour each block within the common palette
\[
\left\lceil\frac98W\right\rceil+14,
\]
and permute a newly attached block's palette to match the colour set already assigned at its cutvertex. The additive term does not accumulate.

The unrestricted conjecture is **not** proved or disproved here. The limitations are substantive:

1. The four-set lemma controls one subdivided \(K_4\), not arbitrary interacting branching configurations.
2. The lattice curvature argument excludes the small obstruction for this topology; it does not establish \((9,4)\)-colourability for general triangle-free hexagonal graphs.
3. The rounding constant comes from having only four branch vertices. Applying the same method with an unbounded number of branch vertices would not yield an absolute constant.

Finally, the auxiliary assertion in the supplied discussion needs its triangle-free qualification: a lattice triangle with demand four requires twelve colours. That correction does not affect the main weighted conjecture.