```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an explicit nondecreasing initial segment for every simple surface triangulation and stronger coefficient bounds in the orientably triangulating case, but do not settle log-concavity.",
  "would_publish": false,
  "caveats": "The results use fixed-graph rotation-system counts; later coefficient ratios remain uncontrolled, and literature novelty of the partial bounds is not claimed."
}
```

# Partial results

I do not obtain a proof or counterexample to the conjecture. The main progress beyond the supplied attempt is a switching argument that controls **more than the first step**, and applies also to graphs triangulating nonorientable surfaces.

Here is one consequence. If \(G\) is a simple planar triangulation on \(n\) vertices, then
\[
\boxed{\quad
a_0(G)\le a_1(G)\le\cdots\le
a_{\left\lfloor(4n+11)/24\right\rfloor}(G).
\quad} \tag{1}
\]
There is an analogous bound for every closed surface, stated below. I also obtain a coefficientwise lower bound from independent sets and substantially strengthen the first-coefficient bound from the previous attempt.

These are partial results toward the distribution problem, not proofs of log-concavity.

## 1. Conventions and face excess

Throughout, graphs are connected and simple, and surfaces are closed. Embeddings are counted by orientable rotation systems on a fixed graph: graph automorphisms are not factored out. Write
\[
\Gamma_G(x)=\sum_{g\ge0}a_g(G)x^g.
\]

If global mirror images are identified instead, all counts for the nontrivial triangulations considered here are divided uniformly by two, and the inequalities remain valid.

Let \(n=|V(G)|\) and \(m=|E(G)|\). A simple graph of minimum degree at least two has no face of length one or two in an orientable cellular embedding. Consequently, for a genus-\(g\) rotation system \(R\),
\[
E_g:=\sum_{F\in\mathcal F(R)}(|F|-3)
      =3n-m-6+6g\ge0. \tag{2}
\]
In particular, \(E_g\) depends only on \(G\) and \(g\), not on \(R\).

If \(G\) triangulates a surface of Euler characteristic \(\chi\), then
\[
m=3(n-\chi). \tag{3}
\]
Except for the possible \(K_3\) convention, such a simple graph has minimum degree at least three.

When the triangular embedding is orientable of genus \(h\), equations (2)–(3) give
\[
m=3n-6+6h,\qquad E_g=6(g-h). \tag{4}
\]
Thus \(h\) is the minimum orientable genus, and its embeddings are exactly the triangular embeddings.

---

# 2. A nondecreasing initial segment for every surface triangulation

The switching argument below gives a result for a somewhat larger class of graphs.

### Theorem 2.1

Let \(G\) be a connected simple graph of minimum degree at least two. Then
\[
\boxed{\qquad
a_{g+1}(G)\ge a_g(G)
\quad\text{whenever}\quad
24g\le 6m-14n+23.
\qquad} \tag{5}
\]

Consequently, if \(G\) triangulates a closed surface of Euler characteristic \(\chi\), then
\[
\boxed{\quad
a_0(G)\le a_1(G)\le\cdots\le
a_{\left\lfloor(4n-18\chi+47)/24\right\rfloor}(G).
\quad} \tag{6}
\]

For example:

* For a sphere triangulation, this is (1).
* If \(G\) has an orientable triangular embedding of genus \(h\), then
  \[
  \boxed{\quad
  a_h(G)\le\cdots\le
  a_{h+\left\lfloor(4n+12h+11)/24\right\rfloor}(G).
  \quad} \tag{7}
  \]
* If \(G\) triangulates the nonorientable surface of crosscap number \(k\), then
  \[
  a_0(G)\le\cdots\le
  a_{\left\lfloor(4n+18k+11)/24\right\rfloor}(G). \tag{8}
  \]
  Some initial terms in (8) can be zero. This statement does not assume that the orientable Euler lower bound is attained.

## 2.1. A three-corner switch with a uniquely identifiable inverse face

Let \(R\) be an arbitrary orientable rotation system. At a vertex \(v\), choose three darts that belong to three triangular faces.

There is exactly one way to multiply the rotation at \(v\) by a 3-cycle on those darts while retaining a single cyclic rotation at \(v\). To see this, suppress the unchosen portions of the vertex rotation. On the three selected positions, the original cyclic order is a 3-cycle; of the two possible multiplying 3-cycles, one leaves a single cycle and the other produces three cycles.

Write the face permutation as
\[
\varphi=\sigma\alpha,
\]
where \(\sigma\) is the vertex-rotation permutation and \(\alpha\) reverses darts. The switch replaces \(\varphi\) by \(\pi\varphi\), where the three points in the support of \(\pi\) belong to distinct triangular face cycles. It therefore merges these three faces into one 9-face. All other face cycles are unchanged. The genus increases by one.

Crucially, the new 9-face identifies the switched vertex:

* \(v\) occurs exactly three times on its boundary;
* every other vertex occurs at most twice.

Indeed, another vertex \(u\) can occur in at most two of the three original triangles: every triangle containing both \(u\) and \(v\) uses the edge \(uv\), which has only two sides.

Thus, given a particular 9-face in a target embedding, there is **at most one** inverse switch of this type. Its center must be the unique vertex occurring three times, and the original three triangles, if they can be recovered at all, are obtained uniquely by cutting at those occurrences.

This inverse bound is considerably sharper than counting arbitrary triples of repeated vertices.

## 2.2. Counting by the number of 9-faces

For a genus-\(g\) rotation system \(R\), let

* \(e(R)\) be its number of 9-faces;
* \(t_v(R)\) be the number of triangular faces incident with \(v\);
* \(T(R)=\sum_v t_v(R)\), the total number of triangular corners.

The number of available switches from \(R\) is exactly
\[
M(R)=\sum_v\binom{t_v(R)}3. \tag{9}
\]

Fix \(e=e(R)\). Let \(L_{\mathrm{nt}}(R)\) be the total boundary length of all nontriangular faces. For every length \(\ell\ge4\),
\[
\ell\le4(\ell-3).
\]
Treating the 9-faces separately therefore gives
\[
L_{\mathrm{nt}}(R)
\le 9e+4(E_g-6e)
=4E_g-15e.
\]
Hence
\[
T(R)=2m-L_{\mathrm{nt}}(R)
\ge 2m-4E_g+15e. \tag{10}
\]

For every nonnegative integer \(t\),
\[
\binom t3\ge t-2.
\]
Combining this with (9)–(10), we obtain
\[
M(R)\ge 2m-2n-4E_g+15e.
\]
Put
\[
C_g:=2m-2n-4E_g
     =6m-14n+24-24g. \tag{11}
\]
Then
\[
M(R)\ge \max\{0,C_g+15e\}. \tag{12}
\]

Let \(a_{g,e}\) count the genus-\(g\) rotation systems having exactly \(e\) 9-faces. Every switch just described goes from class \((g,e)\) to class \((g+1,e+1)\). Each target has at most \(e+1\) inverse switches. Double counting gives
\[
\boxed{\quad
(e+1)a_{g+1,e+1}
\ge \max\{0,C_g+15e\}\,a_{g,e}.
\quad} \tag{13}
\]

If \(C_g\ge1\), then
\[
C_g+15e\ge e+1,
\]
so \(a_{g+1,e+1}\ge a_{g,e}\). Summing over \(e\) proves
\[
a_{g+1}\ge a_g.
\]
If \(E_g<0\), equation (2) already implies \(a_g=0\), so the same conclusion is automatic.

Condition \(C_g\ge1\) is precisely (5). Substitution of (3) proves (6), and the stated specializations follow. ∎

## 2.3. A quantitative version

For an orientable triangular embedding of genus \(h\), set
\[
A=2m-2n=4n-12+12h.
\]
At genus \(h+r\), we have \(E_{h+r}=6r\), so \(0\le e\le r\). Equation (13) implies
\[
a_{h+r+1}\ge
\min_{0\le e\le r}
\frac{\max\{0,A-24r+15e\}}{e+1}\,a_{h+r}.
\]
The expression before taking the positive part is monotone in \(e\), since
\[
\frac{A-24r+15e}{e+1}
=15+\frac{A-24r-15}{e+1}.
\]
Therefore
\[
\boxed{\quad
a_{h+r+1}\ge
\left[
\min\left\{
A-24r,\,
\frac{A-9r}{r+1}
\right\}
\right]_+a_{h+r},
\quad} \tag{14}
\]
where \([z]_+=\max\{z,0\}\).

This controls an initial range of successive ratios from below. It does not show that the actual ratios decrease.

---

# 3. A coefficientwise bound from independent sets

There is a different, complementary construction when an orientable triangular embedding exists.

For \(d\ge2\), fix a \(d\)-cycle \(\rho\), and define
\[
B_d(x)=
\sum_{\substack{\tau\in S_d\\ \tau\text{ is a }d\text{-cycle}}}
x^{(d-c(\tau\rho^{-1}))/2}, \tag{15}
\]
where \(c(\pi)\) denotes the number of cycles of a permutation.

The exponent is a nonnegative integer: \(\tau\rho^{-1}\) is even, so \(d-c(\tau\rho^{-1})\) is even. The polynomial is independent of the chosen \(\rho\). Write
\[
B_d(x)=1+\sum_{j\ge1}b_{d,j}x^j.
\]

For example,
\[
\begin{aligned}
B_3(x)&=1+x,\\
B_4(x)&=1+5x,\\
B_5(x)&=1+15x+8x^2,\\
B_6(x)&=1+35x+84x^2.
\end{aligned}
\]
In particular,
\[
\boxed{\quad b_{d,1}=\binom{d+1}{4}.\quad} \tag{16}
\]
A direct proof of (16) is given below.

For a graph \(G\), define
\[
Q_G(x)=
\sum_{\substack{S\subseteq V(G)\\ S\text{ independent}}}
\prod_{v\in S}\bigl(B_{d(v)}(x)-1\bigr). \tag{17}
\]

### Theorem 3.1

If \(G\) is simple and has an orientable triangular embedding of genus \(h\), then
\[
\boxed{\qquad
\Gamma_G(x)\succeq a_h(G)x^hQ_G(x),
\qquad} \tag{18}
\]
where \(\succeq\) means coefficientwise inequality.

In particular,
\[
\boxed{\quad
a_{h+1}(G)\ge
a_h(G)\sum_v\binom{d(v)+1}{4}.
\quad} \tag{19}
\]
Also,
\[
a_{h+2}(G)\ge a_h(G)
\left(
\sum_v b_{d(v),2}
+
\sum_{\substack{\{u,v\}\subseteq V(G)\\uv\notin E(G)}}
\binom{d(u)+1}{4}\binom{d(v)+1}{4}
\right). \tag{20}
\]

## 3.1. Rigidity of triangular rotations

We first need an injectivity fact.

### Lemma 3.2

Suppose two triangular rotation systems of a simple graph agree at every vertex outside a set \(U\). If \(G[U]\) is triangle-free, then the two rotation systems are identical.

**Proof.**
Every facial triangle of the first rotation system has a vertex outside \(U\). At that vertex its oriented corner is unchanged. In a simple graph, a specified oriented corner belonging to a triangular face determines the entire oriented facial triangle: the third edge is uniquely determined.

Thus every face of the first rotation system is also a face of the second. Their face permutations, and hence their vertex rotations, are equal. ∎

## 3.2. Independent changes have additive genus cost

Fix a triangular rotation system \(R\). At one vertex \(v\), replace its cyclic order \(\rho_v\) by another cyclic order \(\tau_v\), and put
\[
\pi_v=\tau_v\rho_v^{-1}.
\]
The \(d(v)\) original faces incident with \(v\) are distinct triangles. The cycles of \(\pi_v\) describe how these triangles merge. The resulting genus increase is exactly
\[
\frac{d(v)-c(\pi_v)}2. \tag{21}
\]

Now make such changes at an independent set \(S\). No facial triangle contains two vertices of \(S\), so the sets of original faces affected by the changes are disjoint. Their genus costs add.

If every vertex in \(S\) is actually changed, the generating polynomial for the resulting genus increments is consequently
\[
\prod_{v\in S}(B_{d(v)}(x)-1). \tag{22}
\]

## 3.3. No overcounting across different triangular embeddings

Suppose an output rotation system is obtained

* from a triangular system \(R\) by changes on an independent set \(S\), and
* from a triangular system \(R'\) by changes on an independent set \(S'\).

Then \(R\) and \(R'\) agree outside \(S\cup S'\). The union of two independent sets induces a bipartite graph, and in particular is triangle-free. Lemma 3.2 gives \(R=R'\).

Once the original rotation system and the output are fixed, the set of changed vertices and their new rotations are uniquely determined. Thus the construction is injective over all triangular starting systems and all independent changed sets.

Summing (22) proves (18). ∎

## 3.4. The first coefficient of \(B_d\)

For genus increase one, the permutation
\[
\pi=\tau\rho^{-1}
\]
has cycle deficit \(d-c(\pi)=2\). Its nontrivial cycle type is therefore either:

1. one 3-cycle; or
2. two disjoint transpositions.

For each three-element support, precisely one of the two 3-cycles leaves \(\pi\rho\) a single \(d\)-cycle. This contributes \(\binom d3\).

For four selected elements in cyclic order \(a,b,c,d\), precisely the crossing pairing
\[
(ac)(bd)
\]
leaves \(\pi\rho\) a single cycle. The other two pairings split it into three cycles. This contributes \(\binom d4\).

Hence
\[
b_{d,1}=\binom d3+\binom d4=\binom{d+1}{4},
\]
proving (16) and (19).

The displayed small polynomials follow from this coefficient, the total
\[
B_d(1)=(d-1)!,
\]
and the degree bound \(\deg B_d\le\lfloor(d-1)/2\rfloor\).

---

# 4. A further improvement of the first-coefficient bound

The first coefficient can also include suitable changes at two adjacent vertices.

### Theorem 4.1

Let \(G\) be a connected simple graph with an orientable triangular embedding of genus \(h\), and suppose \(G\notin\{K_3,K_4\}\). Then
\[
\boxed{
a_{h+1}(G)\ge a_h(G)
\left[
\sum_v\binom{d(v)+1}{4}
+
\sum_{uv\in E(G)}(d(u)-2)(d(v)-2)
\right].
} \tag{23}
\]

In particular,
\[
\boxed{\quad
a_{h+1}(G)\ge (n+m)a_h(G)
=(4n-6+6h)a_h(G).
\quad} \tag{24}
\]

The \(K_4\) exception is necessary for this particular bound:
\[
\Gamma_{K_4}(x)=2+14x,
\]
whereas the bracket in (23) would equal \(10\).

## 4.1. Distinct triangular rotations have distance at least five

Measure the distance between rotation systems by the number of vertices at which their rotations differ.

### Lemma 4.2

For \(G\notin\{K_3,K_4\}\), distinct triangular rotation systems differ at at least five vertices.

**Proof.**
Let \(U\) be their set of differing vertices, and suppose \(|U|\le4\).

At a changed vertex \(v\), at least three successor values change. Indeed, the quotient of two cyclic permutations is even, and a nonidentity even permutation moves at least three elements.

Every changed old corner belongs to a facial triangle contained entirely in \(U\): a triangle with an unchanged vertex would be fixed by the argument of Lemma 3.2.

Thus at least three corners at \(v\) have both neighboring vertices in \(U\setminus\{v\}\), a set of size at most three. In the cyclic link of \(v\), three selected vertices can span three link edges only when the entire link is a 3-cycle. Therefore \(d(v)=3\), and its three neighbors are precisely the other vertices of \(U\).

This holds for every \(v\in U\), forcing \(G[U]=K_4\), with no edges leaving \(U\). Connectedness gives \(G=K_4\), a contradiction. ∎

Therefore the sets of rotation systems at distance at most two from distinct triangular starting systems are disjoint.

## 4.2. Counting genus-one changes at an adjacent pair

Fix a triangular rotation system, and let \(uv\in E(G)\). The vertices \(u\) and \(v\) belong together to exactly two original faces, namely the two triangles incident with \(uv\).

At either endpoint, these two faces correspond to consecutive positions in the vertex rotation. Among the genus-one local changes counted by \(b_{d,1}\), exactly
\[
d-2 \tag{25}
\]
merge these two particular faces:

* the 3-cycle support must contain their two positions, and its third position has \(d-2\) choices;
* a valid double-transposition change pairs opposite, not consecutive, selected positions, so it contributes none.

For completeness, consider arbitrary nonidentity changes at \(u\) and \(v\), of individual genus costs \(k_u,k_v\). Their combined cost is
\[
k_u+k_v-\varepsilon, \tag{26}
\]
where \(\varepsilon=1\) exactly when both local changes merge the two shared faces, and otherwise \(\varepsilon=0\).

Here is the cut-and-join verification. After the change at \(u\), the relevant face-return permutation on the corners at \(v\) is either the identity or the transposition of the two shared-face corners. In the latter case, multiplication by that transposition increases the cycle count of the local change at \(v\) by one if the two corners lie in the same cycle, and decreases it by one otherwise. Euler's formula gives exactly (26).

Both individual costs are at least one. Thus a two-vertex change has total genus cost one precisely when
\[
k_u=k_v=1,\qquad \varepsilon=1.
\]
By (25), there are exactly
\[
(d(u)-2)(d(v)-2)
\]
such changes at the pair \(u,v\).

Changes at two nonadjacent vertices have additive costs and cannot have total cost one. Consequently, the bracket in (23) is exactly the number of genus-\((h+1)\) systems at distance at most two from a fixed triangular system.

Lemma 4.2 makes these sets disjoint for different triangular systems, proving (23). Finally, \(d(v)\ge3\), so every vertex summand and every edge summand in (23) is at least one. This gives (24). ∎

---

# 5. What this does and does not resolve

The arguments establish three precise facts:

1. **All simple surface triangulations have an explicitly bounded nondecreasing initial segment**, including graphs whose given triangulation is nonorientable.
2. **Orientable triangular embeddings admit an injective independent-set construction**, yielding lower bounds on every coefficient.
3. **The first rise is quantitatively large**: outside \(K_3,K_4\), inequality (23) improves substantially on the initial bound in the supplied attempt.

However, these remain lower-bound arguments. Log-concavity requires upper control on successive ratios. Even in the orientably triangulating case, I have not proved the general inequality
\[
a_{h+1}(G)^2\ge a_h(G)a_{h+2}(G).
\]

The switch in Section 2 accounts for embeddings obtained by merging three triangular faces into a recognizable 9-face. The packing constructions account for other specified families of embeddings. There is no sufficient control here on the remaining embeddings, particularly those with different nontriangular face patterns.

Thus the original conjecture is **not resolved by this attack**. The rigorous fallback is the initial-segment theorem (5)–(8), together with the coefficient bounds (18) and (23).