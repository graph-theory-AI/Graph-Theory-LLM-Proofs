```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There is a linear-time output algorithm for bounded-precoloring extension in bipartite toroidal quadrangulations, including instances with forced nonzero winding.",
  "would_publish": false,
  "caveats": "This does not resolve the general surface problem; novelty of the special case and subsequent literature have not been established."
}
```

# A partial result in the quadrangulation regime

I do not resolve the catalogued problem. The following is an independent approach to a class not covered by the previous attempt’s sparse-core argument.

## Partial theorem

Let \(k\) be fixed. Given

- a finite simple bipartite graph \(G\), cellularly embedded in the torus with every face of length four, and
- a prescribed coloring \(\psi:P\to\mathbb Z_3\), where \(|P|\le k\),

one can decide whether \(\psi\) extends to a proper 3-coloring of \(G\), and output an extension if one exists, in linear time.

More explicitly, with \(k\) variable, the algorithm below runs in
\[
2^{O(k)}\bigl(|V(G)|+|E(G)|\bigr)
\]
time.

The prescribed vertices may be anywhere, not necessarily on one face. The proof also gives a linear-time reconstruction algorithm for quadrangulated annuli with bounded, fully precolored boundary.

The argument does not use the earlier attempt’s subcubic list-coloring lemma or its claimed linear-time cycle-shortening routine.

---

# 1. Recoloring within a fixed planar winding class

Write colors as elements of \(\mathbb Z_3\). For a proper 3-coloring \(c\), define
\[
w_c(u,v)=
\begin{cases}
1,&c(v)-c(u)=1\pmod 3,\\
-1,&c(v)-c(u)=-1\pmod 3.
\end{cases}
\]
Thus \(w_c(v,u)=-w_c(u,v)\).

For an oriented walk \(W\), its **integer circulation** is the sum of \(w_c\) along \(W\). This is an integer, not just a residue modulo three.

In a plane graph, orient each facial boundary walk with the face on its left. Denote its circulation by \(\sigma_c(f)\).

## Lemma 1: fixed-circulation reconstruction

Let \(F\) be a connected plane graph, let \(c_0\) be a proper 3-coloring of \(F\), and let \(\eta\) prescribe colors on \(q\) vertices.

One can decide whether there is an extension \(c\) of \(\eta\) satisfying
\[
\sigma_c(f)=\sigma_{c_0}(f)
\qquad\text{for every face }f,
\tag{1}
\]
and output one if it exists, in
\[
O\!\left((q+1)(|V(F)|+|E(F)|)+q^3\right)
\tag{2}
\]
time.

### Proof

Put \(w_0=w_{c_0}\). If \(c\) satisfies (1), then
\[
\frac{w_c-w_0}{2}
\]
is an integer-valued antisymmetric edge function with zero circulation around every face.

In a connected plane graph, such an edge function is a gradient. Indeed, integrate it along a spanning tree; consistency on each non-tree edge follows because a fundamental cycle is an integer sum of facial boundary walks. Consequently, there is an integer function \(p\) on vertices such that
\[
w_c(u,v)=w_0(u,v)+2\bigl(p(v)-p(u)\bigr).
\tag{3}
\]

Conversely, whenever the right-hand side of (3) belongs to \(\{-1,1\}\) on every edge, the coloring
\[
c_p(v)=c_0(v)+2p(v)\pmod 3
\tag{4}
\]
is proper and has the same facial circulations as \(c_0\).

These formulas describe every coloring satisfying (1). Initially they may reproduce \(c\) only up to a constant color shift, but adding a constant to \(p\) absorbs that shift.

For each edge, name its endpoints so that \(w_0(u,v)=1\). Then (3) has value \(\pm1\) precisely when
\[
-1\le p(v)-p(u)\le0.
\tag{5}
\]
Represent these inequalities by a directed graph having

- an arc \(u\to v\) of weight \(0\);
- an arc \(v\to u\) of weight \(1\).

An arc \(x\to y\) of weight \(a\) means
\[
p(y)\le p(x)+a.
\]

Let the prescribed vertices be \(p_1,\ldots,p_q\). Choose
\[
a_i\in\{0,1,2\}
\quad\text{such that}\quad
c_0(p_i)+2a_i=\eta(p_i)\pmod3.
\]
The required potential values have the form
\[
p(p_i)=a_i+3z_i,\qquad z_i\in\mathbb Z.
\]

Let \(d(i,j)\) be the directed shortest-path distance from \(p_i\) to \(p_j\) in the constraint graph. Specified terminal potentials extend to all vertices if and only if
\[
p(p_j)-p(p_i)\le d(i,j)
\qquad\text{for all }i,j.
\tag{6}
\]
Necessity follows by summing arc inequalities. For sufficiency, set
\[
p(v)=\min_i\bigl(p(p_i)+d(p_i,v)\bigr).
\tag{7}
\]
The pairwise inequalities ensure that (7) gives the prescribed value at every terminal, and the shortest-path inequalities ensure every arc constraint.

Substituting \(p(p_i)=a_i+3z_i\), condition (6) becomes
\[
z_j-z_i
\le
\left\lfloor\frac{d(i,j)+a_i-a_j}{3}\right\rfloor.
\tag{8}
\]
This is a system of integer difference constraints on \(q\) variables. Bellman–Ford, with a new source having zero-weight arcs to every variable, either detects infeasibility or supplies integer values \(z_i\). Its running time is \(O(q^3)\).

The distances are obtained by \(q\) runs of the deque shortest-path algorithm for weights zero and one. After solving (8), a second collection of such runs evaluates (7). Thus the running time is (2). If \(q=0\), simply return \(c_0\). ∎

The important point is that matching prescribed colors *within one planar winding class* is a shortest-path problem, not a repeated call to a coloring decision algorithm.

---

# 2. Linear reconstruction in a quadrangulated annulus

The next lemma supplies the winding class needed after cutting the torus.

## Lemma 2: annular reconstruction

Let \(F\) be a connected graph embedded in an annulus, with both boundary components traced by cycles \(R_1,R_2\), and with every other face of length four.

Suppose all boundary vertices are precolored, along with possibly some additional vertices. Write
\[
b=|R_1|+|R_2|,
\qquad q=|\operatorname{dom}\eta|.
\]
There is an extension-and-output algorithm running in
\[
O\!\left((b+q+1)(|V(F)|+|E(F)|)+q^3\right).
\tag{9}
\]

No bipartiteness assumption is needed in this lemma.

### Proof

First reject an improper prescribed coloring.

Cap both boundary components by disks, obtaining a plane embedding with two distinguished faces \(f_1,f_2\). Their required integer circulations \(t_1,t_2\) are determined by the prescribed boundary colors, using the facial orientations.

For every other face, the required circulation is zero. Indeed, a sum of four numbers in \(\{-1,1\}\) is even and lies between \(-4\) and \(4\); if it is zero modulo three, it must be zero as an integer.

Since each edge contributes oppositely to its two incident facial walks, necessarily
\[
t_1+t_2=0.
\tag{10}
\]
Reject if (10) fails. Put \(t(f_i)=t_i\) and \(t(f)=0\) on all other faces.

We first construct some proper 3-coloring having these facial circulations, without yet requiring its individual boundary colors to match.

## 2.1 Orienting the dual

Choose the convention that a dual edge directed into a face contributes \(+1\) to that face’s circulation. We seek an orientation of the plane dual \(D\) satisfying
\[
\operatorname{indeg}_D(f)-\operatorname{outdeg}_D(f)=t(f).
\tag{11}
\]

Every dual vertex except possibly \(f_1,f_2\) has degree four. Hence there are either zero or two odd-degree dual vertices.

If there are two, join them by one artificial edge. Orient an Euler tour of the resulting even-degree multigraph and delete the artificial edge. This gives an initial orientation whose imbalance
\[
a(f)=\operatorname{indeg}(f)-\operatorname{outdeg}(f)
\]
is zero except possibly at \(f_1,f_2\), where it is \(1\) or \(-1\).

Set
\[
\beta(f)=\frac{t(f)-a(f)}2.
\tag{12}
\]
These are integers: both \(t(f)\) and \(a(f)\) have the parity of the face length. Also \(\sum_f\beta(f)=0\).

If there is a directed path from a vertex with \(\beta>0\) to a vertex with \(\beta<0\), reverse that path. This increases the initial endpoint’s imbalance by two, decreases the final endpoint’s imbalance by two, and leaves all intermediate imbalances unchanged. Thus it reduces
\[
B=\sum_f\max\{\beta(f),0\}
\]
by one.

If no such path exists, let \(S\) be the vertices reachable from all vertices with positive \(\beta\). Then \(S\) contains a positive-\(\beta\) vertex and no negative-\(\beta\) vertex. No currently directed edge leaves \(S\), so
\[
a(S)=|\delta(S)|.
\]
But
\[
t(S)=a(S)+2\beta(S)>|\delta(S)|,
\]
which is impossible for the imbalance sum of any orientation. Thus failure to find a path correctly certifies infeasibility of (11).

Initially,
\[
B
=\frac14\sum_f|t(f)-a(f)|
\le \frac{|t_1|+|t_2|+2}{4}
=O(b+1).
\]
Consequently, only \(O(b+1)\) directed searches and path reversals are needed. Each takes linear time.

Dual loops, if present, cause no problem: they contribute zero imbalance and are handled by the Euler-tour construction.

## 2.2 Integrating and prescribing colors

A successful dual orientation defines an antisymmetric primal edge function \(w\in\{-1,1\}\) with facial circulations \(t(f)\).

Every \(t(f)\) is divisible by three. Therefore \(w\), reduced modulo three, has zero circulation around every plane cycle. Integrating along a spanning tree gives a proper 3-coloring \(c_0\) with
\[
\sigma_{c_0}(f)=t(f).
\]

Apply Lemma 1 to \(c_0\) and all prescribed vertices.

This is complete: every extension of the input precoloring has exactly the prescribed circulations on \(f_1,f_2\), and circulation zero on every quadrilateral face. Thus every possible extension belongs to the winding class being tested.

Combining the dual construction with Lemma 1 gives (9). ∎

---

# 3. A height algorithm and its short obstruction

Here is the mechanism that either colors a bipartite toroidal quadrangulation immediately or finds a bounded-length cycle along which it can be cut.

Let \(G\) be any connected bipartite graph. Fix its bipartition function
\[
\epsilon:V(G)\to\{0,1\}.
\]
An **integer height coloring** is a function \(h:V(G)\to\mathbb Z\) satisfying
\[
|h(u)-h(v)|=1
\qquad\text{for every edge }uv.
\tag{13}
\]
Its reduction modulo three is a proper 3-coloring.

We can require \(h(v)\equiv\epsilon(v)\pmod2\) without loss of generality: adding three to all heights changes their parity but not their colors.

## Lemma 3: heights or a short forced-circulation walk

Given a bipartite graph \(G\) and a prescribed coloring on \(k\ge1\) vertices, one can, in
\[
O\!\left(k(|V(G)|+|E(G)|)+k^3\right)
\tag{14}
\]
time, do one of the following:

1. output an integer height coloring extending the prescribed colors modulo three; or
2. output a closed walk \(W\) of length at most \(4k-6\) such that every proper 3-coloring extending the prescription would have nonzero integer circulation around \(W\).

### Proof

Let the prescribed vertices be \(p_1,\ldots,p_k\). Choose the unique
\[
a_i\in\{0,1,\ldots,5\}
\]
satisfying
\[
a_i=\psi(p_i)\pmod3,
\qquad
a_i=\epsilon(p_i)\pmod2.
\]
The terminal heights must have the form
\[
h_i=a_i+6z_i.
\]

Let \(d(i,j)\) be ordinary graph distance. There is a height extension with these terminal heights if and only if
\[
|h_i-h_j|\le d(i,j)
\qquad\text{for all }i,j.
\tag{15}
\]

For sufficiency, define
\[
h(v)=\min_i\bigl(h_i+d(p_i,v)\bigr).
\tag{16}
\]
The pairwise inequalities give the correct values at the terminals. Formula (16) is 1-Lipschitz on edges. Moreover, every term in the minimum has parity \(\epsilon(v)\). Hence adjacent values differ by an odd integer of absolute value at most one, and therefore differ by exactly one.

Condition (15) is the system
\[
z_j-z_i\le B_{ij},
\qquad
B_{ij}=
\left\lfloor
\frac{d(i,j)+a_i-a_j}{6}
\right\rfloor.
\tag{17}
\]
Distances are computed by \(k\) breadth-first searches, and Bellman–Ford solves (17) in \(O(k^3)\) time.

Suppose (17) is infeasible. Take a negative directed cycle in this terminal constraint graph, with \(r\le k\) vertices. Index its successive terminals cyclically by \(p_1,\ldots,p_r\), and write
\[
d_i=d(p_i,p_{i+1}),\qquad B_i=B_{i,i+1}.
\]
Let
\[
\rho_i=d_i+a_i-a_{i+1}-6B_i.
\]
The quantity before reduction modulo six is even, by bipartiteness. Thus
\[
\rho_i\in\{0,2,4\}.
\]
Since \(\sum_iB_i\le-1\),
\[
\sum_i d_i
=6\sum_iB_i+\sum_i\rho_i
\le 4r-6
\le4k-6.
\tag{18}
\]

Choose shortest paths between successive terminals and concatenate them to form \(W\).

Now suppose \(c\) is any proper 3-coloring extending the prescription. Let \(s_i\) be its integer circulation along the chosen path from \(p_i\) to \(p_{i+1}\). Then
\[
s_i\le d_i.
\]
Also,
\[
s_i=a_{i+1}-a_i+6u_i
\]
for an integer \(u_i\): the congruence modulo three follows from the endpoint colors, and the congruence modulo two follows from the path length and bipartition.

Consequently \(u_i\le B_i\), and
\[
\oint_W w_c
=\sum_i s_i
=6\sum_i u_i
\le6\sum_iB_i<0.
\tag{19}
\]
This proves the required obstruction property. The shortest paths can be reconstructed by additional breadth-first searches within the time bound (14). ∎

For \(k=0\), the bipartition itself supplies a coloring.

---

# 4. Completing the toroidal algorithm

We now prove the partial theorem.

Assume first that the prescribed coloring is proper on the prescribed vertices; otherwise reject immediately.

Run Lemma 3.

- If it outputs a height coloring, reduce it modulo three and return it.
- Otherwise, obtain the closed walk \(W\) from that lemma.

## 4.1 Contractible cycles have zero circulation

In any proper 3-coloring of a quadrangulation, each facial four-walk has integer circulation zero.

Therefore every contractible simple cycle has circulation zero: sum the facial circulations in the disk that it bounds, orienting that disk consistently. Contributions from interior edges cancel.

Decompose \(W\) into simple cycles and immediate edge reversals. This can be done by splitting at repeated vertices. The total length of the resulting walks is \(|W|\); immediate reversals have circulation zero.

If every resulting simple cycle is contractible, then \(W\) has circulation zero in every proper 3-coloring. This contradicts (19), so the prescribed coloring has no extension.

Otherwise, we have found a noncontractible simple cycle \(C\) of length
\[
\ell\le |W|\le4k-6.
\tag{20}
\]

### Finding the noncontractible cycle

No short-cycle search theorem is needed: all candidate cycles already occur in the explicitly constructed \(O(k)\)-length walk.

For a simple cycle in a cellular torus embedding, contractibility can be tested in linear time. Delete from the dual the edges crossing that cycle and test connectivity. The cycle is nonseparating exactly when the remaining dual is connected. On the torus, a simple cycle is noncontractible exactly when it is nonseparating.

There are only \(O(k)\) candidate cycles, so these tests take \(O(k(|V|+|E|))\) time.

## 4.2 Cut, enumerate, reconstruct, and glue

Cut the torus along \(C\). Since \(C\) is noncontractible and simple, the resulting surface is an annulus.

The cut graph \(G_C\) has two boundary copies \(C^+,C^-\) of \(C\), and all its other faces are quadrilaterals. Cutting duplicates each vertex and edge of \(C\), so
\[
|V(G_C)|=|V(G)|+\ell,
\qquad
|E(G_C)|=|E(G)|+\ell.
\]

Enumerate all \(3^\ell\) assignments
\[
\alpha:V(C)\to\mathbb Z_3.
\]
Discard assignments that are improper on \(C\) or disagree with already prescribed colors.

For each remaining assignment:

1. prescribe \(\alpha\) on both copies \(C^+,C^-\);
2. retain all other prescribed colors;
3. apply Lemma 2 to the resulting annular instance.

Here the total boundary length is \(2\ell\), and the number of prescribed vertices is at most
\[
k+2\ell=O(k).
\]

If an annular extension is found, identify the corresponding boundary copies. Their colors agree by construction, so this produces a proper coloring of \(G\) extending \(\psi\).

Conversely, any extension of \(\psi\) to \(G\) induces one enumerated assignment \(\alpha\), and cutting that coloring gives an extension of the corresponding annular instance. Thus rejection of every assignment correctly proves nonextendability.

By (20), the number of assignments is \(2^{O(k)}\). Lemma 2, the topological tests, and all reconstruction operations therefore take
\[
2^{O(k)}\bigl(|V(G)|+|E(G)|\bigr)
\]
time in total.

This proves the partial theorem. ∎

---

# 5. Why the winding step is genuinely needed

Bipartiteness alone does not make a bounded prescribed coloring easy to satisfy by a global height.

Consider the standard toroidal quadrangulation
\[
G=C_6\square C_{2r},\qquad r\ge2.
\]
Prescribe colors at
\[
(0,0),\ (2,0),\ (4,0)
\]
to be \(0,2,1\), respectively.

An extension exists, for example
\[
c(i,j)=i+(j\bmod2)\pmod3.
\]
But the prescribed colors force the horizontal six-cycle at \(j=0\) to have successive colors
\[
0,1,2,0,1,2.
\]
Its integer circulation is therefore six. No global integer height can induce this coloring, since a gradient has circulation zero on every closed walk.

Thus the height algorithm alone must fail on this family. The short-cycle-and-annulus reconstruction above handles it. Notice that these are arbitrarily large, 4-regular quadrangulations with only three prescribed vertices.

---

# 6. Further consequences and the remaining gap

Two immediate consequences help delimit the result.

### A supplied short planarizing cycle

For **any** toroidal quadrangulation, not necessarily bipartite, a supplied noncontractible cycle of bounded length permits linear-time reconstruction with boundedly many prescribed vertices: enumerate its colors, cut to an annulus, and apply Lemma 2.

The bipartite hypothesis in the main theorem is used to obtain either a coloring or such a bounded-length cycle.

### Large-edgewidth bipartite quadrangulations on other surfaces

For a bipartite quadrangulation of any fixed closed surface, if every noncontractible cycle has length at least \(4k\), the height algorithm by itself is complete.

Indeed, its obstruction walk has length at most \(4k-6\). All simple cycles in its decomposition would then be contractible, contradicting the required nonzero circulation. This gives another linear-time special case, including surfaces of higher genus.

## What remains unresolved

The argument does not provide the desired algorithm for general triangle-free graphs on a fixed surface.

In particular:

- **Nonbipartite toroidal quadrangulations of unbounded edgewidth:** there is no bipartition-based height construction, and the argument does not produce a bounded-length planarizing cycle.
- **Higher genus with short essential cycles:** cutting one such cycle need not produce a planar surface. Facial circulations alone then do not determine the remaining integer periods.
- **General triangle-free embeddings:** nonquadrilateral faces can have nonzero circulation, and there may be linearly many such faces. The bounded annular circulation construction does not choose these values globally.

These are genuine gaps, not implementation details concealed in the running-time analysis. The result above is consequently a rigorous special case rather than a solution of the catalogued conjecture.