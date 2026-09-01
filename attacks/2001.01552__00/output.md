```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every chordal graph of clique number at most K has a (K, sqsubseteq_{2^K})-tame ball representation in R^K, which completely answers the question when p(1)<3.",
  "would_publish": false,
  "caveats": "The construction relies on a perfect-elimination order and does not cover the nonchordal graphs permitted when col_1 is at least 3."
}
```

# Statement of the partial result

Write \(\lambda_d\) for \(d\)-dimensional Lebesgue measure. For convex bodies \(A,B\subseteq\mathbb R^d\), the relation from the source is

\[
 A\sqsubseteq_s B
 \quad\Longleftrightarrow\quad
 \lambda_d(A)\le s\,\lambda_d(A\cap B).
\]

Thus at least a \(1/s\)-fraction of \(A\) lies in \(B\). In the tame condition, intersecting bodies must be comparable under this relation, and each body has only boundedly many \(\sqsubseteq_s\)-successors. Whether the body itself is counted only changes the constant by one. The construction below also has bounded ply, so it satisfies the multiplicity part of the definition as well.

The main partial result is the following.

## Theorem

For every positive integer \(K\), every finite chordal graph \(G\) with

\[
\omega(G)\le K
\]

has an intersection representation by closed Euclidean balls \(\{B_v:v\in V(G)\}\) in \(\mathbb R^K\) such that:

1. \(B_u\cap B_v\neq\varnothing\) if and only if \(uv\in E(G)\);
2. every edge \(uv\) has exactly one orientation, say \(u\to v\), for which
   \[
   B_u\sqsubseteq_{2^K}B_v
   \quad\text{and}\quad
   B_v\not\sqsubseteq_{2^K}B_u;
   \]
3. every \(B_v\) has at most \(K\) \(\sqsubseteq_{2^K}\)-successors, counting \(B_v\) itself;
4. every point of \(\mathbb R^K\) belongs to at most \(K\) balls.

Consequently, \(G\) has a \((K,\sqsubseteq_{2^K})\)-tame representation in \(\mathbb R^K\).

This yields two consequences for Question 6.

- The answer is affirmative after restricting to chordal graphs: if \(G\) is chordal and \(\operatorname{col}_r(G)\le p(r)\) for every \(r\), take
  \[
  K=\max\{1,\lfloor p(1)\rfloor\},\qquad
  c=K,\qquad s=2^K,\qquad d=K.
  \]
- If \(p(1)<3\), then the unrestricted question has an affirmative answer, with
  \[
  c=2,\qquad s=4,\qquad d=2.
  \]

The constants are not optimized.

# The ball-port construction

For a ball \(B=\overline{B}(a,R)\) and \(x\in\partial B\), let

\[
n_B(x)=\frac{x-a}{R}
\]

be its outward unit normal.

Suppose a graph \(H\) of clique number at most \(K\) has already been represented by balls in \(\mathbb R^K\). For each clique \(Q\) of \(H\) with \(|Q|\le K-1\), maintain a **private transverse port**: a nonempty relatively open patch

\[
P_Q\subseteq \bigcap_{v\in Q}\partial B_v
\]

such that:

- every point of \(P_Q\) is outside \(B_w\) for \(w\notin Q\);
- the normals \(\{n_{B_v}(x):v\in Q\}\) are linearly independent at every \(x\in P_Q\).

For \(Q=\varnothing\), a port is simply an open set outside all existing balls. Since \(|Q|\le K-1\), the common boundary has local dimension at least one, so ports can be used while leaving another portion available for later use.

## Insertion lemma

Let \(S\) be a clique of the currently represented graph with \(|S|\le K-1\). One can add an arbitrarily small ball \(C\) which intersects exactly the balls indexed by \(S\), while preserving private transverse ports for all old cliques and creating them for all new cliques of size at most \(K-1\).

### Proof

Choose \(x\in P_S\). Enumerate \(S=\{1,\ldots,t\}\), and write

\[
B_i=\overline B(a_i,R_i),\qquad
n_i=\frac{x-a_i}{R_i}.
\]

The vectors \(n_1,\ldots,n_t\) are linearly independent. Put

\[
C=\overline B(x,\rho)
\]

for a sufficiently small \(\rho>0\).

Because \(x\) is outside every old nonmember of \(S\), choosing \(\rho\) small makes \(C\) disjoint from every old ball outside \(S\). It plainly intersects every \(B_i\), because its center lies on \(\partial B_i\).

It remains to construct ports for the new cliques. Every new clique containing the new vertex has the form

\[
\{C\}\cup I,\qquad I\subseteq S.
\]

A port is needed when \(|I|+1\le K-1\), equivalently \(|I|\le K-2\).

Seek a point on \(\partial C\) in the form

\[
y=x+\rho z,\qquad \lVert z\rVert=1.
\]

For \(i\in S\),

\[
\begin{aligned}
y\in\partial B_i
&\Longleftrightarrow
\lVert R_i n_i+\rho z\rVert^2=R_i^2\\
&\Longleftrightarrow
n_i\cdot z=-\frac{\rho}{2R_i}.
\end{aligned}
\]

Likewise,

\[
y\notin B_j
\quad\Longleftrightarrow\quad
n_j\cdot z>-\frac{\rho}{2R_j}.
\]

Choose first a unit vector \(z_0\) satisfying

\[
n_i\cdot z_0=0\quad(i\in I),\qquad
n_j\cdot z_0>0\quad(j\in S\setminus I).
\]

Such a vector exists because the map

\[
z\longmapsto (n_1\cdot z,\ldots,n_t\cdot z)
\]

has rank \(t\). If \(S\setminus I=\varnothing\), choose any unit vector orthogonal to all the \(n_i\); the assumption \(|I|\le K-2\) leaves dimension at least two before imposing the unit-sphere equation.

For small \(\rho\), perturb \(z_0\) to a unit vector \(z_\rho\) satisfying exactly

\[
n_i\cdot z_\rho=-\frac{\rho}{2R_i}\qquad(i\in I).
\]

For example, solve these equations by a vector \(h_\rho\in\operatorname{span}\{n_i:i\in I\}\), with \(h_\rho=O(\rho)\), and put

\[
z_\rho=h_\rho+
\sqrt{1-\lVert h_\rho\rVert^2}\,z_0.
\]

The strict inequalities for \(j\in S\setminus I\) persist for sufficiently small \(\rho\). Thus

\[
y_I=x+\rho z_\rho
\]

lies on the boundaries of \(C\) and the balls indexed by \(I\), and lies outside all other old balls.

At \(\rho=0\), the relevant normal vectors are

\[
\{n_i:i\in I\}\cup\{z_0\},
\]

which are linearly independent because \(z_0\) is orthogonal to every \(n_i\), \(i\in I\). Hence independence persists for small \(\rho\). The common boundary therefore has local dimension

\[
K-(|I|+1)\ge1,
\]

and a small relatively open neighborhood of \(y_I\) is the desired private transverse port.

Finally, there are only finitely many old cliques. Before choosing \(\rho\), select in each old port a witness point different from \(x\). Taking \(\rho\) smaller than all corresponding distances ensures that a portion of every old port remains outside \(C\). This proves the insertion lemma. \(\square\)

# Proof of the theorem

Let

\[
v_1,v_2,\ldots,v_n
\]

be a perfect-elimination ordering of the chordal graph \(G\). Thus

\[
S_i=N(v_i)\cap\{v_{i+1},\ldots,v_n\}
\]

is a clique. Since \(S_i\cup\{v_i\}\) is also a clique and \(\omega(G)\le K\),

\[
|S_i|\le K-1.
\]

Represent the vertices in reverse order \(v_n,v_{n-1},\ldots,v_1\). When \(v_i\) is inserted, use the insertion lemma with the parent clique \(S_i\). In addition to the lemma's requirements, choose its radius \(\rho_i\) so that

\[
\rho_i<\frac14 R_j
\qquad\text{for every }v_j\in S_i,
\]

where \(R_j\) is the radius of \(B_{v_j}\).

The insertion lemma shows inductively that the resulting intersection graph is exactly \(G\).

## The overlap estimate

Suppose \(v_j\in S_i\). Let the parent ball be

\[
B_{v_j}=\overline B(a,R),
\]

and let the child ball be

\[
B_{v_i}=\overline B(x,\rho),
\]

where \(x\in\partial B_{v_j}\). Put \(n=(x-a)/R\). The ball

\[
D=\overline B\left(x-\frac{\rho}{2}n,\frac{\rho}{2}\right)
\]

is contained in both \(B_{v_i}\) and \(B_{v_j}\). Indeed,

\[
D\subseteq B_{v_i}
\]

by the triangle inequality, and, since \(\rho<2R\),

\[
\left\lVert x-\frac{\rho}{2}n-a\right\rVert+\frac{\rho}{2}
=R.
\]

Therefore

\[
\lambda_K(B_{v_i}\cap B_{v_j})
\ge 2^{-K}\lambda_K(B_{v_i}),
\]

and hence

\[
B_{v_i}\sqsubseteq_{2^K}B_{v_j}.
\]

On the other hand, \(\rho<R/4\), so

\[
\lambda_K(B_{v_i})
<4^{-K}\lambda_K(B_{v_j}).
\]

Consequently,

\[
2^K\lambda_K(B_{v_i}\cap B_{v_j})
\le 2^K\lambda_K(B_{v_i})
<\lambda_K(B_{v_j}),
\]

and therefore

\[
B_{v_j}\not\sqsubseteq_{2^K}B_{v_i}.
\]

Thus every edge is comparable in exactly the direction from the vertex being inserted to one of its later neighbors in the perfect-elimination ordering.

For a fixed \(v_i\), the only balls \(B_u\) satisfying

\[
B_{v_i}\sqsubseteq_{2^K}B_u
\]

are \(B_{v_i}\) itself and the balls corresponding to \(S_i\). Hence their number is at most

\[
1+|S_i|\le K.
\]

This verifies the tame bound.

Finally, if a point belonged to more than \(K\) balls, all corresponding vertices would be pairwise adjacent, giving a clique larger than \(K\). Thus the representation also has ply at most \(K\). This completes the proof. \(\square\)

# Consequences for the polynomial question

For strong coloring numbers,

\[
\operatorname{col}_1(G)=\operatorname{degeneracy}(G)+1.
\]

Hence every graph satisfying the hypothesis of Question 6 obeys

\[
\operatorname{degeneracy}(G)+1\le p(1).
\]

## Chordal graphs

If \(G\) is chordal, then

\[
\omega(G)\le \operatorname{col}_1(G)\le p(1).
\]

Taking \(K=\max\{1,\lfloor p(1)\rfloor\}\) in the theorem gives uniform constants

\[
c=K,\qquad s=2^K,\qquad d=K.
\]

No information about \(p(r)\) for \(r\ge2\) is needed in this restricted case.

## The range \(p(1)<3\)

If \(p(1)<3\), integrality gives

\[
\operatorname{col}_1(G)\le2,
\]

so \(G\) has degeneracy at most one. A finite simple graph has degeneracy at most one exactly when it is a forest. Forests are chordal and have clique number at most two. The theorem with \(K=2\) gives

\[
c=2,\qquad s=4,\qquad d=2.
\]

Thus Question 6 has an affirmative answer for every polynomial \(p\) satisfying \(p(1)<3\).

# Remaining gap

The proof uses the fact that, in a perfect-elimination ordering, the already represented neighborhood \(S_i\) is a clique. Its balls may therefore share a private common boundary port. For a general graph of degeneracy at least two, the corresponding neighborhood need not be a clique. Forcing several nonadjacent parent bodies through a common port would create forbidden intersections.

Passing to a chordal completion does not solve this: the fill edges would appear as genuine intersections, and there is no evident uniform way to delete them while retaining convexity and the fixed fractional-overlap bound. Polynomially bounded strong coloring numbers do not directly supply a perfect-elimination structure of the kind used above.

Accordingly, this argument gives neither a proof nor a counterexample for the full nonchordal case.