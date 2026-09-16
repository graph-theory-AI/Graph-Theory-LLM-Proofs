```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "In the full complex-weighted model, I prove d ≤ n−2 for even n ≥ 6, classify existence for n ≤ 4, and establish rigidity for regular effective supports.",
  "would_publish": false,
  "caveats": "This argument does not decide, for example, (n,d)=(6,3); no claim of novelty or independently verified literature status."
}
```

# A degree obstruction and a rigidity theorem

I work directly with the complex-weighted, endpoint-bicolored multigraph formulation. In particular, I do **not** initially replace cancellation of nonmonochromatic colorings by the stronger assertion that every perfect matching is monochromatic.

Throughout, \(n,d\) are positive integers, and edges join distinct vertices, as in the endpoint-coloring definition.

## Results

The following existence statements and necessary conditions are proved below:

\[
\begin{array}{c|c}
n & \text{Conclusion}\\ \hline
n\text{ odd} & \text{No realization exists}\\
n=2 & \text{Every }d\ge1\text{ is realizable}\\
n=4 & \text{A realization exists exactly when }1\le d\le3\\
n\ge6\text{ even} &
d=1,2\text{ are realizable, and every realization satisfies }d\le n-2.
\end{array}
\]

There is also a structural result. Aggregate parallel edges having the same endpoint colors by summing their weights. Define the **effective support graph** \(\Gamma\) to have an edge \(ij\) when at least one resulting weight between \(i\) and \(j\) is nonzero.

For any realization with \(n\ge4\):

1. \(\delta(\Gamma)\ge d\).
2. If \(d\ge3\) and \(\deg_\Gamma(v)=d\), then all effective edges incident with \(v\) are monochromatic, with exactly one incident edge of each color.
3. If \(d\ge3\) and \(\Gamma\) is \(d\)-regular, then necessarily
   \[
   (n,d,\Gamma)=(4,3,K_4).
   \]

Thus any realization with \(n>4\) and \(d\ge3\) must have a vertex of effective degree at least \(d+1\).

---

## 1. Encoding the cancellation conditions

For distinct vertices \(i,j\), let \(A_{ij}\) be the \(d\times d\) matrix whose \((a,b)\)-entry is the sum of the weights of edges colored \(a\) at \(i\) and \(b\) at \(j\). Set
\[
A_{ji}=A_{ij}^{\mathsf T}.
\]

Summing parallel edges in this manner preserves every inherited-coloring weight: for a fixed pairing of the vertices, the sum over edge choices factors into a product of these matrix entries.

Introduce a vector of indeterminates
\[
x_i=(x_{i,1},\ldots,x_{i,d})^{\mathsf T}
\]
at each vertex. Define
\[
F_G(x_1,\ldots,x_n)
=
\sum_{M}
\prod_{\{i,j\}\in M}x_i^{\mathsf T}A_{ij}x_j,
\tag{1}
\]
where \(M\) ranges over all pairings of the vertices. Missing effective edges have zero matrices.

The coefficient of \(\prod_i x_{i,c_i}\) is precisely the weight of the inherited coloring \((c_1,\ldots,c_n)\). Consequently the required condition is exactly
\[
F_G(x_1,\ldots,x_n)
=
D_{n,d}(x_1,\ldots,x_n)
:=
\sum_{a=1}^d\prod_{i=1}^n x_{i,a}.
\tag{2}
\]

For a vertex subset \(S\), write \(H_S\) for the analogous matching polynomial of the induced matrix-weighted graph on \(S\), with \(H_\varnothing=1\). Expanding according to the partner of a fixed vertex \(i\) gives
\[
F_G
=
\sum_{j\ne i}
\bigl(x_i^{\mathsf T}A_{ij}x_j\bigr)
H_{V\setminus\{i,j\}}.
\tag{3}
\]

The key point is that after fixing \(x_i\), this is a sum with at most one linear “slice” at each remaining vertex.

---

## 2. An elementary slice lemma

**Lemma.** Let \(m\ge2\), \(d\ge3\), and \(\lambda_1,\ldots,\lambda_d\in\mathbb C^\times\). Suppose
\[
\sum_{a=1}^d\lambda_a\prod_{j=1}^m y_{j,a}
=
\sum_{j=1}^m L_j(y_j)\,Q_j(y_1,\ldots,\widehat{y_j},\ldots,y_m),
\tag{4}
\]
where each \(L_j\) is a linear form, possibly zero.

Then, for every color \(a\), some \(L_j\) is a nonzero scalar multiple of the coordinate form \(y_{j,a}\). In particular, at least \(d\) of the \(L_j\)'s are nonzero.

**Proof.** Put \(U_j=\ker L_j\). The left side of (4) vanishes on
\[
U_1\times\cdots\times U_m.
\tag{5}
\]

First suppose that no nonzero \(L_j\) is a coordinate form. Then no \(U_j\) is contained in a coordinate hyperplane. Because \(\mathbb C\) is infinite, each \(U_j\) therefore contains a vector all of whose coordinates are nonzero.

Fix such vectors in slots \(3,\ldots,m\). The resulting form in the first two slots is
\[
B(u,v)=
\sum_{a=1}^d
\left(\lambda_a\prod_{j=3}^m y_{j,a}\right)u_av_a.
\]
This is a nondegenerate bilinear form, and it vanishes on \(U_1\times U_2\). Hence
\[
\dim U_1+\dim U_2\le d.
\]
But each \(U_j\) has dimension at least \(d-1\), giving
\[
2d-2\le d,
\]
contrary to \(d\ge3\).

Thus some \(L_s\) is a nonzero multiple of \(y_{s,a_0}\). For any \(b\ne a_0\), the vector \(e_b\) belongs to \(U_s\). Substituting \(y_s=e_b\) in (5) gives
\[
\lambda_b\prod_{j\ne s}y_{j,b}=0
\qquad
\text{for all }y_j\in U_j.
\]
It follows that some \(U_j\) is contained in \(\{y_{j,b}=0\}\). Since \(U_j\) has codimension at most one, this means that \(L_j\) is a nonzero multiple of \(y_{j,b}\).

Every color is therefore represented. Distinct colors require distinct slots. \(\square\)

---

## 3. Minimum degree and rigidity at degree \(d\)

Fix a vertex \(i\). Choose \(t\in\mathbb C^d\) such that:

- every coordinate \(t_a\) is nonzero;
- for every nonzero column of every \(A_{ij}\), its scalar product with \(t\) is nonzero.

Such a choice exists because only finitely many proper hyperplanes are forbidden.

Set \(x_i=t\) in (2)–(3). We obtain
\[
\sum_{a=1}^d t_a\prod_{k\ne i}x_{k,a}
=
\sum_{j\ne i}
\bigl(t^{\mathsf T}A_{ij}x_j\bigr)
H_{V\setminus\{i,j\}}.
\tag{6}
\]

For \(d\ge3\), the lemma implies that for every \(a\), some linear form
\[
t^{\mathsf T}A_{ij}x_j
\]
is a nonzero multiple of \(x_{j,a}\). By the generic choice of \(t\), this can happen only if \(A_{ij}\) has exactly one nonzero column, namely column \(a\).

We have proved the useful endpoint-purity condition:

> For every vertex \(i\) and every color \(a\), there is a neighbor \(j\) such that all nonzero aggregated edges between \(i\) and \(j\) have color \(a\) at \(j\).

Different colors require different neighbors. Thus
\[
\deg_\Gamma(i)\ge d \qquad(d\ge3).
\tag{7}
\]

For completeness, the two smaller values of \(d\) also satisfy this bound. For \(d=1\), an isolated vertex would make \(F_G=0\). For \(d=2\), a vertex \(i\) of degree one, with neighbor \(j\), would give
\[
F_G=(x_i^{\mathsf T}A_{ij}x_j)H_{V\setminus\{i,j\}}.
\]
This is a product across the nonempty bipartition
\(\{i,j\}\mid V\setminus\{i,j\}\). Its coefficient-matrix flattening has rank at most one, whereas the corresponding flattening of \(D_{n,2}\) has rank two. Hence degree one is impossible.

This proves
\[
\boxed{\delta(\Gamma)\ge d\quad\text{for }n\ge4.}
\tag{8}
\]

### Equality at one vertex

Suppose now that \(d\ge3\) and \(\deg_\Gamma(i)=d\). The endpoint-purity condition exhausts all neighbors, so they can be denoted \(j_1,\ldots,j_d\) with
\[
A_{i j_a}=u_a e_a^{\mathsf T},
\qquad u_a\ne0.
\tag{9}
\]

Set \(x_k=e_a\) for every \(k\ne i\), leaving \(x_i\) arbitrary. Equation (2) becomes \(F_G=x_{i,a}\). In (3), all terms except the one indexed by \(j_a\) vanish. Therefore
\[
x_{i,a}=h_a\,x_i^{\mathsf T}u_a,
\qquad
h_a=
H_{V\setminus\{i,j_a\}}(e_a,\ldots,e_a).
\tag{10}
\]
Thus \(h_a\ne0\) and
\[
u_a=h_a^{-1}e_a.
\]
Consequently
\[
\boxed{A_{i j_a}=w_a e_ae_a^{\mathsf T},\qquad w_a\ne0.}
\tag{11}
\]

This is the claimed rigidity: every incident effective edge is genuinely monochromatic, with one edge of each color.

Comparing the coefficient of \(x_{i,a}\) in the full polynomial identity gives the additional restriction
\[
\boxed{
H_{V\setminus\{i,j_a\}}
=
w_a^{-1}\prod_{k\ne i,j_a}x_{k,a}.
}
\tag{12}
\]
Thus deleting a degree-\(d\) vertex and its color-\(a\) neighbor leaves a matching polynomial supported on just the all-\(a\) coloring.

---

## 4. The bound \(d\le n-2\) for \(n\ge6\)

Equation (8) immediately gives \(d\le n-1\).

Suppose \(d=n-1\). Then \(\Gamma=K_n\), and every vertex has degree \(d\). By (11), the aggregated graph is an ordinary monochromatically edge-colored \(K_n\), with exactly one incident edge of each color at every vertex.

A vertex coloring can now be inherited from at most one perfect matching: at each vertex, its prescribed color determines its incident matching edge uniquely. All effective edge weights are nonzero, so no existing perfect matching can cancel with another matching of the same inherited coloring.

Each color gives exactly one monochromatic perfect matching. There are therefore only \(d=n-1\) monochromatic perfect matchings. But for even \(n\ge6\),
\[
\#\operatorname{PM}(K_n)
=(n-1)!!>n-1.
\]
Some perfect matching is nonmonochromatic, and its inherited coloring has nonzero weight—a contradiction.

Hence
\[
\boxed{d\le n-2\qquad(n\ge6\text{ even}).}
\tag{13}
\]

For \(n=4,d=3\), the same argument instead yields a complete normal form. After permuting colors, the effective edges are
\[
\{12,34\}\text{ in color }1,\qquad
\{13,24\}\text{ in color }2,\qquad
\{14,23\}\text{ in color }3,
\]
and their weights satisfy
\[
w_{12}w_{34}=w_{13}w_{24}=w_{14}w_{23}=1.
\tag{14}
\]
Conversely, these conditions suffice.

---

## 5. Regular effective support: only the \(K_4\) example

The rigidity argument also resolves all \(d\)-regular effective supports.

We first need an elementary cancellation-free fact.

**Lemma.** Suppose a simple cubic graph has a proper edge-coloring with three colors, and every perfect matching is monochromatic. Then the graph is \(K_4\).

**Proof.** Let its three color classes be perfect matchings \(M_1,M_2,M_3\).

If \(M_1\cup M_2\) has more than one cycle, choosing \(M_1\) on one cycle and \(M_2\) on all the others produces a nonmonochromatic perfect matching. Hence \(M_1\cup M_2\) is a Hamiltonian cycle \(C\).

Assume \(n>4\), and label the vertices alternately even and odd around \(C\).

If an edge of \(M_3\) joins opposite parities, deleting its endpoints leaves two even-order paths in \(C\). Matching along those paths, together with that edge, produces a perfect matching using one \(M_3\)-edge and some edges of \(C\), a contradiction.

Thus every \(M_3\)-edge joins two even vertices or two odd vertices. Draw the vertices in convex position. There must be a crossing between an even-even \(M_3\)-chord and an odd-odd \(M_3\)-chord.

Here is a justification of that last assertion. If no opposite-type chords crossed, smooth all crossings between chords of the same type, allowing the endpoint pairings within each type to change. After discarding any closed curves, this would produce a noncrossing perfect matching of the boundary vertices in which every pair has the same parity. Such a matching is impossible: an arc joining same-parity boundary vertices separates off an odd number of boundary vertices, which cannot be matched internally.

Take such a crossing pair of \(M_3\)-edges. Their endpoints alternate in parity around \(C\). Deleting the four endpoints therefore leaves even-order paths, each matchable using edges of \(C\). Together with the two chosen \(M_3\)-edges, these give a perfect matching. Since \(n>4\), it also contains an edge of \(C\), again contradicting monochromaticity.

Thus \(n=4\), and simplicity and cubicity force \(K_4\). \(\square\)

Now suppose a realization has \(d\ge3\) and \(d\)-regular effective support. By (11), after aggregation it is properly edge-colored, with exactly one edge of each color incident with every vertex.

As above, each inherited coloring comes from at most one perfect matching. Therefore every perfect matching must be monochromatic.

Choose any three color classes. Their union is a spanning simple cubic graph, and all its perfect matchings must be monochromatic. The lemma forces \(n=4\). Since \(d\le n-1\) and \(d\ge3\), we obtain
\[
\boxed{(n,d,\Gamma)=(4,3,K_4).}
\tag{15}
\]

This step is where replacing cancellation by literal monochromaticity is justified; doing so before establishing rigidity would not be valid.

---

## 6. Constructions and the remaining gap

The positive constructions are straightforward and have unit weights throughout.

- **Odd \(n\):** no perfect matching exists, so no monochromatic coloring can have weight one.
- **\(n=2\), arbitrary \(d\):** put one weight-one monochromatic edge of each color between the two vertices.
- **Any even \(n\), \(d=1\):** use a single perfect matching.
- **Any even \(n\ge4\), \(d=2\):** use \(C_n\), with its two alternating perfect matchings colored differently. These are its only perfect matchings.
- **\(n=4,d=3\):** use the three-factor coloring of \(K_4\) described in (14), with all edge weights one.

Together with the obstructions above, these prove the existence table stated at the beginning.

### What is not proved

This does **not** exclude realizations with even \(n\ge6\) and
\[
3\le d\le n-2.
\]
For example, it does not decide \((n,d)=(6,3)\). It shows that any such realization must have irregular effective support in the specific sense that some vertex has degree greater than \(d\); vertices of degree exactly \(d\) obey the strong constraints (11)–(12).

No reduction of the remaining weighted-cancellation cases to an unproved ordinary edge-coloring assertion is being used.