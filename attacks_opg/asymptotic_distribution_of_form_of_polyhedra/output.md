```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For a uniformly chosen unlabelled polyhedral graph with k edges, β converges to 1/2 and √k(β−1/2) converges to a normal law of variance 1/32.",
  "would_publish": false,
  "caveats": "Uses the classical exact enumeration of rooted 3-connected planar maps; no claim of novelty or literature priority is made."
}
```

# The limiting distribution

Let \(\mathcal P_k\) be the set of isomorphism classes of simple, 3-connected planar graphs with \(k\) edges. Choose \(G_k\) uniformly from \(\mathcal P_k\), and write
\[
V_k=|V(G_k)|,\qquad \beta_k=\frac{V_k}{k+2}.
\]
Thus dual polyhedra are not identified unless their graphs are isomorphic.

The answer is
\[
\boxed{\quad
\beta_k\xrightarrow{\mathrm P}\frac12,
\qquad
\sqrt{k}\left(\beta_k-\frac12\right)
\xrightarrow{\mathrm d}N\!\left(0,\frac1{32}\right).
\quad}
\]
Equivalently,
\[
\sqrt{32k}\left(\beta_k-\frac12\right)
\xrightarrow{\mathrm d}N(0,1).
\]

Moreover,
\[
\mathbb E\beta_k=\frac12,
\qquad
\operatorname{Var}(\beta_k)=\frac1{32k}+O(k^{-2}).
\]

The principal issue is not the Gaussian calculation for rooted maps. It is justifying its passage to the **uniform distribution on unlabelled graphs**. Rooting weights a graph inversely by its number of automorphisms. A proof of the required exponential asymmetry estimate is included below, covering orientation-reversing as well as orientation-preserving automorphisms.

## 1. Rooted enumeration

A rooted map here is a map on an oriented sphere with a distinguished directed edge, considered up to orientation-preserving homeomorphism.

For a polyhedral graph \(G\) with \(k\) edges, the number of distinct rooted maps having underlying graph \(G\) is
\[
\frac{4k}{|\operatorname{Aut}G|}.                                      \tag{1}
\]
Indeed, Whitney’s uniqueness of the spherical embedding identifies these rooted maps with automorphism orbits on the \(4k\) flags consisting of a directed edge and a choice of incident face. The action on flags is free.

We use the classical exact bivariate enumeration identity for rooted 3-connected planar maps. Let
\[
M(x,z)=\sum_M x^{v(M)}z^{e(M)}.
\]
Then
\[
M(x,z)=x^2z^2\left(
\frac1{1+xz}+\frac1{1+z}-1
-\frac{(1+U)^2(1+V)^2}{(1+U+V)^3}
\right),                                                          \tag{2}
\]
where the formal power series \(U,V\), with zero constant terms, satisfy
\[
U=xz(1+V)^2,\qquad V=z(1+U)^2.                                      \tag{3}
\]
This is the standard rooted-map enumeration input. Its normalization gives one rooted tetrahedral map.

Put
\[
m_k(x)=[z^k]M(x,z),\qquad R_k=m_k(1).
\]

### The dominant singularity

The characteristic equation of (3) is
\[
4UV=(1+U)(1+V),
\]
or
\[
3UV-U-V-1=0.                                                       \tag{4}
\]
Parameterize the critical point by \(U=u\). Then
\[
V=\frac{u+1}{3u-1},
\]
and substitution into (3) gives
\[
x=\frac{(u+1)(3u-1)^3}{16u},
\qquad
\rho(x)=\frac1{(u+1)(3u-1)}.                                       \tag{5}
\]
At \(x=1\), these equations give
\[
u=1,\qquad V=1,\qquad \rho(1)=\frac14.
\]

For \(x\) in a complex neighborhood of \(1\), singularity analysis of (2)–(3) yields
\[
m_k(x)=c(x)\,k^{-5/2}\rho(x)^{-k}\bigl(1+O(k^{-1})\bigr),            \tag{6}
\]
uniformly there, with \(c(x)\) analytic and nonzero.

Here are details checking the singularity type and the cancellation needed in this assertion. The implicit system has a simple square-root singularity. At its critical point, a null direction is
\[
(1+U,\,2V).
\]
For
\[
T(U,V)=\frac{(1+U)^2(1+V)^2}{(1+U+V)^3},
\]
direct differentiation gives
\[
\bigl((1+U)\partial_U+2V\partial_V\bigr)\log T
=
\frac{3UV-U-V-1}{(1+V)(1+U+V)}.
\]
Thus the square-root term in \(M\) vanishes along the entire critical curve.

To check that the next nonanalytic term does not vanish, set
\[
w=\sqrt{1-4z}
\]
at \(x=1\). Then
\[
U=V=\frac{1-w}{1+w},
\]
and (2) becomes
\[
M(1,z)
=
z^2\left(\frac2{1+z}-1\right)
-\frac{(1-w)^2(1+w)}{(3-w)^3}.
\]
The expansion of the second term shows that the coefficient of \(w^3\) in \(M(1,z)\) is \(8/729\). Consequently,
\[
R_k\sim \frac{2}{243\sqrt{\pi}}\,4^k k^{-5/2}.                       \tag{7}
\]

The uniform version (6) follows by analytic perturbation of this simple critical point. At \(x=1\), the relevant branch has only the Catalan singularity \(z=1/4\) on its circle of convergence; the implicit-function theorem away from that point and the local square-root expansion provide a uniform dented continuation domain for \(x\) near \(1\). The coefficient of the \(3/2\)-power remains nonzero.

## 2. Gaussian fluctuations for rooted maps

Choose a rooted map uniformly among the \(R_k\) rooted maps with \(k\) edges, and denote its vertex count by \(V_k^{\mathrm r}\). Equation (6) gives
\[
\mathbb E e^{sV_k^{\mathrm r}}
=
\frac{c(e^s)}{c(1)}
\left(\frac{\rho(1)}{\rho(e^s)}\right)^k
\bigl(1+O(k^{-1})\bigr).                                          \tag{8}
\]

The variance constant can be computed directly from (5). Define
\[
A(u)=\log\frac{(u+1)(3u-1)^3}{16u},
\qquad
B(u)=-\log\bigl((u+1)(3u-1)\bigr).
\]
Thus \(s=A(u)\) and \(\log\rho(e^s)=B(u)\). At \(u=1\),
\[
A'=4,\qquad A''=-6,\qquad
B'=-2,\qquad B''=\frac52.
\]
Therefore
\[
\left.\frac{d}{ds}\log\rho(e^s)\right|_{s=0}=-\frac12
\]
and
\[
\left.\frac{d^2}{ds^2}\log\rho(e^s)\right|_{s=0}
=
\frac{B''A'-B'A''}{(A')^3}
=-\frac1{32}.                                                     \tag{9}
\]

Writing
\[
h(s)=\log\frac{\rho(1)}{\rho(e^s)},
\]
we have
\[
h(s)=\frac{s}{2}+\frac{s^2}{64}+O(s^3).
\]
Substituting \(s=it/\sqrt{k}\) in (8) gives
\[
\mathbb E\exp\left(
it\,\frac{V_k^{\mathrm r}-(k+2)/2}{\sqrt{k}}
\right)
\longrightarrow
e^{-t^2/64}.
\]
Hence
\[
\frac{V_k^{\mathrm r}-(k+2)/2}{\sqrt{k}}
\xrightarrow{\mathrm d}N\!\left(0,\frac1{32}\right).                \tag{10}
\]

Duality is an exact bijection on rooted maps with \(k\) edges, and sends
\[
v\longmapsto k+2-v.
\]
Thus the mean is exactly
\[
\mathbb E V_k^{\mathrm r}=\frac{k+2}{2}.
\]
Differentiating (8), using its uniform analyticity, also gives
\[
\operatorname{Var}(V_k^{\mathrm r})=\frac{k}{32}+O(1).               \tag{11}
\]

## 3. Exponential asymmetry, including reflections

We now prove the ingredient needed for uniform unlabelled graphs.

### Lemma
There is a constant \(a>0\) such that the number \(R_k^{\mathrm{sym}}\) of rooted polyhedral maps whose underlying graph has a nonidentity automorphism satisfies
\[
R_k^{\mathrm{sym}}\le e^{-ak}R_k
\]
for all sufficiently large \(k\).

### Proof

We use a fixed rigid triangulated disk, show that almost every rooted map contains linearly many disjoint copies, and then count the possible fillings of their common exterior.

#### 3.1. A rigid triangular patch

Construct a triangulated disk \(Q\) with outer triangle \(abc\) as follows.

* Insert a vertex \(o\) adjacent to \(a,b,c\).
* Leave the sector \(abo\) empty.
* Insert one vertex into the sector \(bco\).
* Insert two vertices, successively into triangular faces, inside the sector \(cao\).

For definiteness, the latter two vertices can be \(q\), adjacent to \(c,a,o\), and then \(r\), adjacent to \(c,a,q\).

The disk \(Q\) has four internal vertices and twelve non-boundary edges. It has no nonidentity automorphism preserving its outer boundary setwise, even when reflections are allowed. To see this, \(o\) is the unique internal vertex adjacent to all three boundary vertices. The three sectors at \(o\) contain respectively zero, one and two internal vertices, so each sector, and therefore each boundary vertex, is fixed. The remaining vertices are then fixed as well.

An **occurrence** of \(Q\) is a triangular cycle together with one of its sides, on which the map is exactly this triangulated disk. Reflected copies count as occurrences.

For sufficiently large maps, distinct occurrences have disjoint interiors. Indeed, two triangular cycles in a simple planar graph cannot cross. Their chosen disks are disjoint or nested, unless their union is the whole sphere. The last possibility is excluded once the map has more than \(14\) vertices. Strict nesting is impossible because both disks have exactly four internal vertices.

Let \(q(M)\) denote the number of occurrences.

#### 3.2. Almost every map has linearly many occurrences

There are at least
\[
\sum_f\left\lfloor\frac{\deg f}{3}\right\rfloor
\ge \frac{2k}{5}
\]
pairwise compatible insertion locations in a map with \(k\) edges. To obtain them, partition each facial boundary into disjoint consecutive triples of vertices. Facial boundaries are simple cycles because the graph is 3-connected.

At a selected triple \(a,b,c\), introduce a vertex \(w\) inside the face, adjacent to \(a,b,c\), and insert \(Q\) into the resulting triangle \(abw\). This operation:

* preserves simplicity, planarity and 3-connectivity;
* adds five vertices and fifteen edges;
* creates a designated occurrence of \(Q\).

Insertions at the selected locations can be performed independently. A rooting supplies a canonical ordering if needed.

There is a constant \(C\) such that \(j\) insertions create at most \(Cj\) additional occurrences beyond those already present. Here one can take \(C=215\). Every new occurrence contains a new vertex. Every new vertex has degree at most \(7\), lies in the interior of at most one occurrence, and belongs to the boundary of at most
\[
2\binom72
\]
occurrences. There are five new vertices per insertion.

There is also a bounded inverse ambiguity. Given the resulting map and its \(j\) designated occurrences, there are at most \(6^j\) possible preimages: for each occurrence choose which boundary vertex was \(w\), and order the other two boundary vertices. The remaining neighbor of \(w\) outside the patch then identifies \(c\), and deletion recovers the original map.

Let \(B_k\) count rooted maps with \(q(M)\le\alpha k\), and put
\[
L_k=\left\lfloor\frac{2k}{5}\right\rfloor.
\]
For \(j\le L_k\), the insertion-and-deletion count gives
\[
B_k\binom{L_k}{j}
\le
6^j
\binom{\lfloor\alpha k\rfloor+Cj}{j}
R_{k+15j}.                                                       \tag{12}
\]
By (7),
\[
\frac{R_{k+15j}}{R_k}\le C_0\,4^{15j}
\]
for all sufficiently large \(k\), uniformly for \(j=O(k)\).

Choose \(j=\lfloor\delta k\rfloor\). Using
\[
\binom Nj\ge (N/j)^j,
\qquad
\binom Nj\le(eN/j)^j,
\]
equation (12) yields
\[
\frac{B_k}{R_k}
\le
C_0\left(
6e\,4^{15}
\frac{\alpha k+Cj}{L_k}
\right)^j.
\]
Choose positive \(\alpha,\delta\) sufficiently small that the quantity in parentheses is eventually less than \(1/2\). It follows that
\[
B_k\le e^{-bk}R_k                                                   \tag{13}
\]
for some \(b>0\).

Thus exponentially few rooted maps have fewer than \(\alpha k\) occurrences.

#### 3.3. Independent fillings break automorphisms

Delete the interiors of all occurrences of \(Q\), obtaining a core map \(S\) with \(m=q(M)\) marked triangular faces.

The core is still 3-connected for all sufficiently large maps. Indeed, a path through a deleted patch can be replaced by a path along its boundary triangle. Consequently, deleting at most two core vertices cannot disconnect the core. A core with only three vertices could accommodate at most two patches and hence occurs only among finitely many small maps.

If \(s=e(S)\), then
\[
k=s+12m.
\]
Since the marked faces are triangular faces of a simple planar map,
\[
m\le \frac{2s}{3},
\]
so
\[
s\ge \frac{k}{9}.                                                  \tag{14}
\]

At each marked face there are exactly six possible fillings by \(Q\): the six bijections from its boundary vertices to those of the face. These fillings are distinct because \(Q\) is rigid. Both orientations are included.

For a fixed rooted core with its marked faces, either all \(6^m\) fillings have precisely the designated occurrences of \(Q\), or none do. To justify this independence, any other triangular cycle either avoids an inserted patch or contains it. A different occurrence containing an entire inserted patch would have more than four internal vertices. A proper subdisk of an inserted patch has fewer than four. Thus changing the boundary assignments cannot create or destroy any additional occurrence.

Now suppose a nonidentity automorphism of a filled map exists. It induces an automorphism \(g\) of its core, preserving the marked faces. It cannot fix a marked face: that would preserve its copy of \(Q\), whose rigidity would force the automorphism to fix a flag, and hence to be the identity.

Therefore all cycles of \(g\) on the \(m\) marked faces have length at least two. For a given \(g\), the filling at one face of each cycle determines all the others, so at most
\[
6^{m/2}
\]
of the \(6^m\) fillings can admit \(g\).

The core has at most \(4s\le4k\) automorphisms, because its automorphism group acts freely on flags. Consequently, for each rooted core, the proportion of symmetric fillings is at most
\[
4k\,6^{-m/2}.                                                      \tag{15}
\]

This counts maps whose root edge remains in the core. By (14), at least \(1/9\) of the rootings of any underlying map have this property. Combining (13) and (15), we obtain
\[
R_k^{\mathrm{sym}}
\le
e^{-bk}R_k+36k\,6^{-\alpha k/2}R_k
\le e^{-ak}R_k
\]
after decreasing \(a>0\).

The argument allowed all core automorphisms, including orientation reversal. This proves the lemma. \(\square\)

## 4. Passing to uniform unlabelled polyhedra

Let
\[
A_k=|\mathcal P_k|,
\qquad
S_k=\#\{G\in\mathcal P_k:|\operatorname{Aut}G|>1\}.
\]
Equation (1) gives
\[
R_k=\sum_{G\in\mathcal P_k}\frac{4k}{|\operatorname{Aut}G|}.
\]
In particular,
\[
A_k\ge\frac{R_k}{4k},
\qquad
S_k\le R_k^{\mathrm{sym}},
\]
and hence
\[
\frac{S_k}{A_k}
\le 4k\,\frac{R_k^{\mathrm{sym}}}{R_k}
=O(e^{-a'k})                                                      \tag{16}
\]
for some \(a'>0\).

Conditional on asymmetry, both of the following distributions are uniform on the same set of graphs:

1. a uniformly chosen unlabelled graph;
2. the underlying graph of a uniformly chosen rooted map.

Their total-variation distance is therefore exponentially small, by the lemma and (16). In particular, the rooted central limit theorem (10) transfers to the desired uniform unlabelled model:
\[
\frac{V_k-(k+2)/2}{\sqrt{k}}
\xrightarrow{\mathrm d}N\!\left(0,\frac1{32}\right).                \tag{17}
\]

The exponential estimate also transfers moments. Since \(V_k=O(k)\), the difference between corresponding second moments is exponentially small times \(O(k^2)\). Thus (11) gives
\[
\operatorname{Var}(V_k)=\frac{k}{32}+O(1).
\]
Duality on unlabelled polyhedral graphs gives the exact identity
\[
\mathbb E V_k=\frac{k+2}{2}.
\]

Finally,
\[
\sqrt{k}\left(\beta_k-\frac12\right)
=
\frac{k}{k+2}\,
\frac{V_k-(k+2)/2}{\sqrt{k}},
\]
so (17) proves the stated normal limit. Dividing the variance by \((k+2)^2\) gives
\[
\operatorname{Var}(\beta_k)=\frac1{32k}+O(k^{-2}).
\]

As a normalization check, the same argument also gives
\[
A_k\sim \frac{R_k}{4k}
\sim \frac{1}{486\sqrt{\pi}}\,4^k k^{-7/2}.
\]

## Conclusion and dependencies

The unscaled limiting distribution is the point mass at \(1/2\), not a nondegenerate density. The nontrivial fluctuation scale is \(k^{-1/2}\), and its limiting law is Gaussian with variance constant \(1/32\).

The non-elementary enumeration input is the exact rooted-map identity (2)–(3), together with standard singularity coefficient extraction. Crucially, the uniform-unlabelled conclusion was not obtained by silently equating rooted and unrooted sampling: the required asymmetry estimate was proved above.

I have not established whether this particular Gaussian corollary has already appeared explicitly in the literature, and make no priority claim.