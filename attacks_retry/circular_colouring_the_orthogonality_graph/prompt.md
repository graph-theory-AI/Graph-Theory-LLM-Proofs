Attack the following open graph-theory problem.

Catalog id: circular_colouring_the_orthogonality_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/circular_colouring_the_orthogonality_graph/
Original entry: http://www.openproblemgarden.org/op/circular_colouring_the_orthogonality_graph
Problem attributed to: DeVos, Matt, Ghebleh, Mohammad, Goddyn, Luis A., Mohar, Bojan, Naserasr, Reza (posted 2008-09-23)

=== Problem statement (OpenProblemGarden) ===
Title: Circular colouring the orthogonality graph
Let $ {\mathcal O} $ denote the graph with vertex set consisting of all lines through the origin in $ {\mathbb R}^3 $ and two vertices adjacent in $ {\mathcal O} $ if they are perpendicular. Problem Is $ \chi_c({\mathcal O}) = 4 $ ?

=== Discussion / context (OpenProblemGarden) ===
In the problem statement, $ \chi_c $ denotes the circular chromatic number . Coloring properties of $ {\mathcal O} $ are, rather surprisingly, of interest in quantum mechanics. If the spins of certain particles are measured in three orthogonal directions, then these measurements always return one $ 0 $ and two values which are $ \pm 1 $ . If such a particle has "decided" in advance how it will respond to any possible measurement, then the set of directions in which it will respond $ 0 $ must be an independent set in the orthogonality graph $ {\mathcal O} $ which meets every triangle. Kochen and Specker have shown that $ {\mathcal O} $ (even certain finite subgraphs of it) does not have any independent set meeting every triangle, thus exhibiting a rather mysterious property of these particles. In some sense, if the person doing the measurement has the free will to decide in which directions to measure, then the particle must have some free will to decide how it will respond. The property that $ {\mathcal O} $ has no independent set which meets every triangle shows that $ \chi({\mathcal O}) \ge 4 $ . On the other hand, if we center a regular octahedron at the origin, and assign a color to each line $ L $ depending on which pair of opposite faces it passes through (if $ L $ meets more than one pair of opposite faces, just choose one) we get a proper 4-coloring of $ {\mathcal O} $ . Therefore, $ \chi({\mathcal O}) = 4 $ . These bounds prove that $ 3 \le \chi_c({\mathcal O}) \le 4 $ . By investigating certain finite subgraphs of $ {\mathcal O} $ , DeVos, Ghebleh, Goddyn, Mohar, and Naserasr have shown that $ \chi_c({\mathcal O}) \ge 3.5 $ .

=== Catalog page (statement + literature review) ===
Circular colouring the orthogonality graph — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 The problem asks whether the circular chromatic number of the orthogonality graph $\mathcal{O}$ (vertices = lines through the origin in $\mathbb{R}^3$, edges = orthogonal pairs) equals 4. The bounds $3.5 \le \chi_c(\mathcal{O}) \le 4$ established by DeVos, Ghebleh, Goddyn, Mohar, and Naserasr remain the state of the art; no subsequent paper improving either bound was found in any of the searched sources.

 Reviewer notes. The SIAM Journal paper 'Coloring an Orthogonality Graph' (DOI: 10.1137/050639715) appears to be the source of the lower bound χ_c(O) ≥ 3.5, but the SIAM server returned HTTP 403 on both direct and DOI-redirect fetches, so its full content could not be verified. An arXiv full-text search for 'circular chromatic orthogonality graph' returned zero results. Naserasr's DBLP bibliography (post-2008) contains no paper on this specific problem. The 2025 arXiv paper (2512.01195) on 'Quantum Chromatic Number of Subgraphs of Orthogonality Graphs' concerns quantum chromatic number, not circular chromatic number, and is thus unrelated. The problem remains open as of the search date.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 168s.
 

Problem. Is $ \chi_c({\mathcal O}) = 4 $ ?

Keywords:
circular coloring · geometric graph · orthogonality

Discussion

In the problem statement, $ \chi_c $ denotes the circular chromatic number . Coloring properties of $ {\mathcal O} $ are, rather surprisingly, of interest in quantum mechanics. If the spins of certain particles are measured in three orthogonal directions, then these measurements always return one $ 0 $ and two values which are $ \pm 1 $ . If such a particle has "decided" in advance how it will respond to any possible measurement, then the set of directions in which it will respond $ 0 $ must be an independent set in the orthogonality graph $ {\mathcal O} $ which meets every triangle. Kochen and Specker have shown that $ {\mathcal O} $ (even certain finite subgraphs of it) does not have any independent set meeting every triangle, thus exhibiting a rather mysterious property of these particles. In some sense, if the person doing the measurement has the free will to decide in which directions to measure, then the particle must have some free will to decide how it will respond. The property that $ {\mathcal O} $ has no independent set which meets every triangle shows that $ \chi({\mathcal O}) \ge 4 $ . On the other hand, if we center a regular octahedron at the origin, and assign a color to each line $ L $ depending on which pair of opposite faces it passes through (if $ L $ meets more than one pair of opposite faces, just choose one) we get a proper 4-coloring of $ {\mathcal O} $ . Therefore, $ \chi({\mathcal O}) = 4 $ . These bounds prove that $ 3 \le \chi_c({\mathcal O}) \le 4 $ . By investigating certain finite subgraphs of $ {\mathcal O} $ , DeVos, Ghebleh, Goddyn, Mohar, and Naserasr have shown that $ \chi_c({\mathcal O}) \ge 3.5 $ .

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any value of χ_c(O) below 4 must be 4−1/k for an integer k≥2, while every finite subgraph of O has circular chromatic number strictly below 4.",
  "would_publish": false,
  "caveats": "This does not improve the supplied 7/2 lower bound or resolve the equality; novelty of these structural observations is not asserted."
}
```

## Partial results

I do not obtain either a proof that \(\chi_c(\mathcal O)=4\) or a circular colouring with ratio below \(4\). The following restrictions can, however, be proved rigorously.

**Proposition 1.**
\[
\boxed{\displaystyle
\chi_c(\mathcal O)\in
\left\{\frac72,\frac{11}{3},\frac{15}{4},\frac{19}{5},\ldots\right\}
\cup\{4\}.}
\]
Moreover, if \(\chi_c(\mathcal O)<4\), its value is attained by a colouring with a finite palette: for some integer \(k\ge2\),
\[
\mathcal O\longrightarrow K_{(4k-1)/k}.
\]

**Proposition 2.** Every finite subgraph \(F\subseteq\mathcal O\) satisfies
\[
\boxed{\chi_c(F)<4.}
\]
More quantitatively, if \(n=|V(F)|\ge3\), then
\[
\boxed{\displaystyle
\chi_c(F)\le
4-\frac{1}{\lfloor(n+1)/4\rfloor}.}
\]

Thus, if the conjectured equality holds, it cannot be witnessed by one finite subgraph having circular chromatic number \(4\). An unbounded family of finite subgraphs is necessary.

### Definitions

A circular \(r\)-colouring assigns each vertex a point of the circle
\(\mathbb R/r\mathbb Z\), with adjacent vertices at circular distance at least \(1\).

For integers \(p\ge2q>0\), the circular clique \(K_{p/q}\) has vertex set \(\mathbb Z_p\), with
\[
a\sim b
\quad\Longleftrightarrow\quad
q\le (b-a\bmod p)\le p-q.
\]
The usual equivalent definition is
\[
\chi_c(G)=\inf\{p/q:G\longrightarrow K_{p/q}\}.
\]

This equivalence also holds for infinite graphs. Indeed, first enlarge the circumference of a real-circle colouring slightly, creating uniform positive slack on every edge, and then round all colours to a sufficiently fine rational grid. The argument is uniform and does not depend on the number of vertices.

## 1. A finite optimal-colouring lemma

We need the following standard fact, including a little more information than rationality.

**Lemma 1.** Let \(H\) be a finite graph containing an edge. Write
\[
R=\chi_c(H).
\]
Then \(R=p/q\) in lowest terms, with \(p\le |V(H)|\). Furthermore, an optimal circular \(R\)-colouring contains all the points of some regular \(p\)-gon on its colour circle.

**Proof.** An optimal colouring exists by compactness, after normalizing the colour circle to circumference \(1\). If \(R=2\), the assertion follows from any edge, so assume \(R>2\).

Given an optimal colouring \(f\), form the directed graph of *tight edges*:
\[
u\longrightarrow v
\quad\Longleftrightarrow\quad
uv\in E(H),\qquad f(v)-f(u)=1\pmod R.
\]

This directed graph must contain a directed cycle. Otherwise, choose a function \(h:V(H)\to\mathbb R\) strictly increasing on its arcs and replace \(f(v)\) by
\[
f(v)+\varepsilon h(v)\pmod R.
\]
For sufficiently small \(\varepsilon>0\), every formerly tight edge has circular distance greater than \(1\), while every other edge retains distance greater than \(1\). Here the opposite arc of a tight edge initially has length \(R-1>1\), so it also retains positive slack. Since there are finitely many edges, the resulting colouring has a uniform positive slack and can be rescaled to circumference less than \(R\), a contradiction.

Take a simple directed tight cycle of length \(\ell\). Following it adds \(1\) to the colour at each step, so
\[
\ell=mR
\]
for some positive integer \(m\). Reducing \(\ell/m=p/q\) gives \(p\le\ell\le |V(H)|\).

Addition by \(1\) on the circle of circumference \(p/q\) has an orbit of exactly \(p\) points, equally spaced by \(1/q\). The tight cycle contains this entire orbit. ∎

We will also use that an optimal colouring with rational circumference \(p/q\) gives a homomorphism to \(K_{p/q}\). Multiply its colours by \(q\), obtaining a circle of integer circumference \(p\), and round down to integers. Forward edge separations in \([q,p-q]\) remain in that interval because both endpoints of the interval are integers.

## 2. Graphs in which every pair has a common neighbour

Say that a nonempty graph has the **common-neighbour property** if every pair of vertices, possibly equal, has a common neighbour.

The orthogonality graph has this property: two distinct lines have their common perpendicular, and a line has many perpendicular lines.

**Lemma 2.** If \(G\) has the common-neighbour property and \(\chi_c(G)<4\), then
\[
\chi_c(G)=4-\frac1k
\]
for some positive integer \(k\), and \(G\) admits a homomorphism to \(K_{(4k-1)/k}\).

### Finite case

Let \(H\) be finite with the common-neighbour property, and suppose
\[
R=\chi_c(H)<4.
\]

In any circular \(R\)-colouring, the colours of all neighbours of a vertex lie in an arc of length \(R-2\). Since every two vertices have a common neighbour, **every pair of colours used** has circular distance at most
\[
R-2. \tag{1}
\]

By Lemma 1, write \(R=p/q\) in lowest terms and find a regular \(p\)-gon among the used colours. Its largest circular distance is
\[
\frac{\lfloor p/2\rfloor}{q}.
\]
Applying (1),
\[
\frac{\lfloor p/2\rfloor}{q}
\le \frac pq-2,
\]
or equivalently,
\[
\left\lceil\frac p2\right\rceil\ge2q.
\]
Thus \(p\ge4q-1\). On the other hand, \(R<4\) gives \(p\le4q-1\). Consequently,
\[
p=4q-1,
\qquad
R=4-\frac1q. \tag{2}
\]

### Infinite case

Put \(R=\chi_c(G)<4\). For every sufficiently small \(\eta>0\), choose a finite-palette circular colouring
\[
G\longrightarrow K_{p/q},
\qquad
p/q<R+\eta<4.
\]
Let \(H\) be the subgraph of \(K_{p/q}\) induced by the colours actually used.

The graph \(H\) inherits the common-neighbour property. To see this, choose preimages in \(G\) of two colours; the colour of a common neighbour of those preimages is a common neighbour in \(H\).

Therefore the finite case gives
\[
R\le\chi_c(H)=4-\frac1k<R+\eta
\]
for some positive integer \(k\).

The set
\[
\{4-1/k:k\ge1\}
\]
has no accumulation point below \(4\). Letting \(\eta\) tend to zero proves that \(R\) itself belongs to this set. For sufficiently small \(\eta\), the corresponding \(H\) has \(\chi_c(H)=R\), so composing its optimal finite-palette colouring with \(G\to H\) proves the attainment assertion. ∎

### Application to \(\mathcal O\)

Applying Lemma 2, either \(\chi_c(\mathcal O)=4\), or
\[
\chi_c(\mathcal O)=4-\frac1k
\]
and \(\mathcal O\to K_{(4k-1)/k}\).

The case \(k=1\) would give a proper \(3\)-colouring of \(\mathcal O\), contrary to the non-\(3\)-colourability stated in the question. Thus \(k\ge2\), proving Proposition 1.

In particular, this argument rederives the stated lower bound \(7/2\) from non-\(3\)-colourability and the common-perpendicular property. It does not improve that bound.

## 3. Why every finite subgraph has circular chromatic number below \(4\)

Let \(F\subseteq\mathcal O\) be finite and contain an edge.

Choose a unit vector \(z\) neither parallel nor perpendicular to any line representing a vertex of \(F\). Such a choice avoids only finitely many great circles and finitely many points on the unit sphere.

For each vertex line \(L\), choose its unit representative \(u_L\) satisfying
\[
u_L\cdot z>0,
\]
and project onto \(z^\perp\):
\[
v_L=u_L-(u_L\cdot z)z.
\]
Our choice of \(z\) ensures \(v_L\ne0\).

If \(L\perp M\), then
\[
v_L\cdot v_M
=u_L\cdot u_M-(u_L\cdot z)(u_M\cdot z)
=-(u_L\cdot z)(u_M\cdot z)<0.
\]
Consequently, the smaller angle between \(v_L\) and \(v_M\) is strictly greater than \(\pi/2\).

Colour \(L\) by the argument of \(v_L\), measured on a circle of circumference \(4\). Every edge then has circular distance **strictly greater than \(1\)**. Finiteness gives
\[
\lambda:=\min_{LM\in E(F)}d_4(f(L),f(M))>1.
\]
Rescaling the circle by \(1/\lambda\) yields
\[
\chi_c(F)\le\frac4\lambda<4.
\]
An edgeless graph has circular chromatic number \(1\), so all finite cases are covered.

The same proof works for any finite graph possessing a real three-dimensional orthogonal representation, even when nonadjacent vertices are represented by the same line.

### A vertex-count bound

Let \(n\ge3\), and set
\[
k=\left\lfloor\frac{n+1}{4}\right\rfloor.
\]
For a graph containing an edge, Lemma 1 and the strict inequality just proved give
\[
\chi_c(F)=p/q<4,\qquad p\le n.
\]
In particular, \(p\le4q-1\).

If \(q\le k\), then
\[
\frac pq\le4-\frac1q\le4-\frac1k.
\]
If \(q\ge k+1\), use \(n\le4k+2\) to obtain
\[
\frac pq
\le\frac{n}{k+1}
\le\frac{4k+2}{k+1}
=4-\frac2{k+1}
\le4-\frac1k.
\]
The last inequality holds for every \(k\ge1\). Edgeless graphs satisfy the bound as well. This proves Proposition 2.

For example, any finite subgraph satisfying
\[
\chi_c(F)>4-\frac1k
\]
must have at least \(4k+3\) vertices.

## 4. A rigidity condition on any remaining candidate colouring

The discrete spectrum gives a useful algebraic constraint on a hypothetical colouring below \(4\).

Suppose
\[
c:\mathcal O\longrightarrow K_{(4k-1)/k},
\]
with colours in \(\mathbb Z_{4k-1}\). In this circular clique,
\[
N(a)\cap N(a+2k-1)=\{a+3k-1\}. \tag{3}
\]
Indeed, after translating \(a\) to \(0\),
\[
N(0)=\{k,\ldots,3k-1\},
\]
whereas
\[
N(2k-1)=
\{3k-1,\ldots,4k-2\}\cup\{0,\ldots,k-1\}.
\]

Thus, for nonzero vectors \(u,v\),
\[
\boxed{
\begin{aligned}
c([u])&=a,\\
c([v])&=a+2k-1
\end{aligned}
\quad\Longrightarrow\quad
c([u\times v])=a+3k-1
\pmod{4k-1}.}
\]
The different colours ensure that \([u]\ne[v]\), so \(u\times v\ne0\). Its line is a common neighbour of the two original lines, and (3) forces its colour.

For \(k=2\), this says that colours \(a\) and \(a+3\) force their common perpendicular to have colour \(a+5\pmod7\). I do not obtain a contradiction from these cross-product constraints.

## 5. The remaining gap

For the real-circle definition, compactness gives
\[
\chi_c(\mathcal O)
=
\sup\{\chi_c(F):F\subseteq\mathcal O,\ F\text{ finite}\}. \tag{4}
\]
For completeness, fix \(r\) strictly above the supremum on the right. Every finite collection of edge constraints has a circular \(r\)-colouring. These constraints are closed in the compact product
\[
(\mathbb R/r\mathbb Z)^{V(\mathcal O)},
\]
so they have a simultaneous solution. Letting \(r\) decrease proves (4).

Therefore, Proposition 2 does **not** disprove the conjecture: numbers strictly below \(4\) can have supremum \(4\). It instead shows why one finite extremal example cannot settle it.

The unresolved task is to exclude the remaining finite-palette possibilities
\[
\frac72,\quad \frac{11}{3},\quad \frac{15}{4},\quad\ldots
\]
—or to construct a colouring at one of them. Nothing above excludes even \(7/2\), so no stronger lower bound or resolution is claimed.
