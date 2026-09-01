```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For fixed c the exponent is already determined by maximal cliques of order at most c; in particular, the c=3 case reduces exactly to counting maximal triangles, for which a sharp n^{3/2} special case and a structural derivation of the n^{7/4} barrier are proved.",
  "would_publish": false,
  "caveats": "The worst-case exponent is not improved; the remaining obstruction is maximal triangles with moderately large, globally compatible edge books."
}
```

# Mathematical writeup

## 1. Statement and notation

Fix an integer \(c\ge 2\). A graph \(G\) is \(c\)-closed if every nonedge has at most \(c-1\) common neighbors.

Let

\[
F_c(n)=\max\{\text{number of maximal cliques of }G:
 |V(G)|=n,\ G\text{ is }c\text{-closed}\}.
\]

The supplied bounds are

\[
\Omega_c(n^{3/2})\le F_c(n)
 \le O_c\!\left(n^{\,2-2^{1-c}}\right).
\]

I do not close this gap. I prove a reduction showing that cliques larger than \(c\) do not affect the exponent, and then analyze the first open case \(c=3\).

---

## 2. Two elementary structural facts

### Lemma 2.1: external vertices see fewer than \(c\) vertices of a maximal clique

If \(K\) is a maximal clique in a \(c\)-closed graph and \(x\notin K\), then

\[
|N(x)\cap K|\le c-1.
\]

### Proof

Since \(K\) is maximal, \(x\) has a nonneighbor \(y\in K\). Every vertex of \(N(x)\cap K\) is adjacent to both \(x\) and \(y\), because \(K\) is a clique. Thus \(x,y\) have at least \(|N(x)\cap K|\) common neighbors. Since \(xy\) is a nonedge, this number is at most \(c-1\). ∎

### Lemma 2.2: distinct maximal cliques have small intersection

If \(K,L\) are distinct maximal cliques, then

\[
|K\cap L|\le c-1.
\]

### Proof

Choose \(x\in L\setminus K\). Maximality of \(K\) gives a vertex \(y\in K\) nonadjacent to \(x\). Necessarily \(y\notin L\). Every member of \(K\cap L\) is a common neighbor of \(x,y\), so \(c\)-closure gives \(|K\cap L|<c\). ∎

In particular, every \(c\)-set is contained in at most one maximal clique.

---

## 3. A bounded-rank reduction

Let

\[
B_c(n)=\max\{\text{number of maximal cliques of order at most }c
  \text{ in an }n\text{-vertex }c\text{-closed graph}\}.
\]

### Theorem 3.1

Fix \(c\ge2\) and \(\beta\ge1\). If

\[
B_c(m)\le A(m+1)^\beta
\qquad\text{for every }m,
\]

then

\[
F_c(n)\le C_{c,\beta}A(n+1)^\beta .
\]

Consequently, \(F_c(n)\) and \(B_c(n)\) have the same upper polynomial exponent.

### Proof

Partition the maximal cliques of order at least \(c\) into dyadic classes

\[
\mathcal K_s=\{K:s\le |K|<2s\},
\qquad s=c,2c,4c,\ldots.
\]

For a fixed class, retain every vertex independently with probability

\[
p=\frac{c}{2s},
\]

and let \(R\) be the retained set.

For every \(K\in\mathcal K_s\), the probability that exactly \(c\) vertices of \(K\) are retained is bounded below by a positive constant \(\delta_c\) depending only on \(c\). Indeed, \(p|K|\in[c/2,c]\), and a direct binomial estimate gives a uniform positive lower bound.

Suppose exactly a \(c\)-set \(C\subseteq K\) is retained from \(K\). Then \(C\) is a maximal clique in \(G[R]\). To see this, a retained vertex of \(K\setminus C\) does not exist, while Lemma 2.1 says that a vertex outside \(K\) is adjacent to at most \(c-1\) members of \(K\), and hence cannot be adjacent to all of \(C\).

Moreover, distinct maximal cliques \(K\) give distinct retained \(c\)-sets, by Lemma 2.2. Therefore, for every realization of \(R\),

\[
\#\{K\in\mathcal K_s:|K\cap R|=c\}
   \le B_c(|R|).
\]

Taking expectations,

\[
\delta_c|\mathcal K_s|
 \le \mathbb E B_c(|R|)
 \le A\,\mathbb E(|R|+1)^\beta.
\]

For a binomial random variable, with fixed \(\beta\),

\[
\mathbb E(|R|+1)^\beta
 \le C_\beta(np+1)^\beta
 \le C_{c,\beta}\left(\frac ns+1\right)^\beta.
\]

Thus

\[
|\mathcal K_s|
 \le C_{c,\beta}A\left(\frac ns+1\right)^\beta .
\]

Summing over dyadic \(s\) gives

\[
\sum_s |\mathcal K_s|=O_{c,\beta}(A n^\beta);
\]

the geometric terms \((n/s)^\beta\) sum to \(O(n^\beta)\), and the \(O(\log n)\) additive contribution is also \(O(n^\beta)\). Maximal cliques of order less than \(c\) contribute at most \(B_c(n)\). ∎

### Consequence

For the exponent problem, it is enough to count maximal cliques of bounded order, namely order at most \(c\). Large maximal cliques are not the source of a larger exponent.

For every \(c\), maximal edges already number only \(O_c(n^{3/2})\). Indeed, let \(H\) consist of the edges that are maximal cliques in \(G\). Every pair of vertices has at most \(c-1\) common neighbors in \(H\):

- for a nonedge of \(G\), this follows from \(c\)-closure;
- if \(uv\in E(G)\) and \(x\) were adjacent to both \(u,v\) in \(H\), then the maximal edge \(ux\) would have the common neighbor \(v\), a contradiction.

Hence

\[
\sum_x \binom{d_H(x)}2\le(c-1)\binom n2,
\]

and convexity gives \(|E(H)|=O(\sqrt c\,n^{3/2}+n)\).

---

## 4. Exact reduction of the \(c=3\) case to maximal triangles

Let \(T_3(n)\) be the maximum possible number of maximal triangles in a \(3\)-closed graph on \(n\) vertices.

Maximal cliques of order at most \(3\) consist of:

- at most \(n\) maximal singletons;
- \(O(n^{3/2})\) maximal edges;
- maximal triangles.

Therefore Theorem 3.1 gives, at the level of upper exponents,

\[
\operatorname{exp}(F_3)
  =\max\left\{\frac32,\operatorname{exp}(T_3)\right\}.
\]

Since the standard lower bound already has exponent \(3/2\), the first unresolved case is exactly:

> How many maximal triangles can a \(3\)-closed graph have?

Thus larger maximal cliques can be removed from the \(c=3\) exponent question.

---

## 5. Attachments to a maximal triangle

For an edge \(e=uv\), write

\[
\gamma(e)=|N(u)\cap N(v)|.
\]

For a maximal triangle \(T\), define its attachment number

\[
a(T)=
\bigl|\{x\notin T:|N(x)\cap T|=2\}\bigr|.
\]

Since \(T\) is maximal, no outside vertex is adjacent to all three vertices of \(T\).

### Lemma 5.1

For every maximal triangle \(T\),

\[
a(T)=\sum_{e\in E(T)}(\gamma(e)-1).
\]

### Proof

For an edge \(e\) of \(T\), one common neighbor of its endpoints is the third vertex of \(T\). Every other common neighbor is outside \(T\) and is adjacent to exactly the two endpoints of \(e\). These three classes, one for each edge of \(T\), are disjoint. ∎

### Lemma 5.2: global attachment budget

For the family \(\mathcal T\) of maximal triangles in a \(3\)-closed graph,

\[
\sum_{T\in\mathcal T}a(T)\le n(n-1).
\]

### Proof

For each pair \((T,x)\) counted by \(a(T)\), let \(y\) be the unique vertex of \(T\) not adjacent to \(x\), and map \((T,x)\) to the ordered nonedge \((x,y)\).

The other two vertices of \(T\) are common neighbors of \(x,y\). Since the graph is \(3\)-closed, \(x,y\) have at most two common neighbors, so the ordered pair \((x,y)\) determines \(T\) uniquely whenever it arises. The map is injective into the ordered nonedges. ∎

---

## 6. A low-edge-codegree lemma

For \(D\ge0\), let

\[
E_D=\{uv\in E(G):\gamma(uv)\le D\}
\]

and put \(H_D=(V(G),E_D)\), \(m_D=|E_D|\).

### Lemma 6.1

In every \(3\)-closed graph,

\[
m_D=O\!\left(n^{3/2}+(D+1)n\right).
\]

### Proof

Count wedges in \(H_D\):

\[
W=\sum_x\binom{d_{H_D}(x)}2.
\]

Split them according to whether their endpoints are adjacent in \(G\).

If the endpoints \(u,v\) are nonadjacent in \(G\), they have at most two common neighbors, so these wedges contribute at most

\[
2\binom n2.
\]

If the endpoints are adjacent, the wedge lies in a triangle of \(G\). A triangle containing \(r\) edges of \(E_D\) contributes \(0,0,1,3\) such wedges for \(r=0,1,2,3\), respectively, which is at most \(r\). Hence this part contributes at most

\[
\sum_{e\in E_D}\gamma(e)\le Dm_D.
\]

Thus

\[
W\le 2\binom n2+Dm_D.
\]

On the other hand, convexity gives

\[
W\ge n\binom{2m_D/n}{2}
   =\frac{2m_D^2}{n}-m_D.
\]

Solving the resulting quadratic inequality yields

\[
m_D=O(n^{3/2}+(D+1)n).
\]
∎

---

## 7. Recovering the \(n^{7/4}\) barrier and a sharp special case

Fix \(A\ge1\). Split maximal triangles according to whether \(a(T)\le A\).

If \(a(T)\le A\), Lemma 5.1 implies that each edge of \(T\) has codegree at most \(A+1\). Hence, using Lemma 6.1,

\[
3|\{T:a(T)\le A\}|
 \le \sum_{e\in E_{A+1}}\gamma(e)
 \le (A+1)m_{A+1},
\]

and therefore

\[
|\{T:a(T)\le A\}|
 =O\!\left((A+1)n^{3/2}+(A+1)^2n\right).
\]

Lemma 5.2 gives

\[
|\{T:a(T)>A\}|\le \frac{n(n-1)}{A}.
\]

Combining,

\[
|\mathcal T|
 =O\!\left(
     A n^{3/2}+A^2n+\frac{n^2}{A}
   \right).
\]

Taking \(A=n^{1/4}\) gives

\[
|\mathcal T|=O(n^{7/4}),
\]

which is exactly the existing \(c=3\) exponent. Thus this argument does not improve the known worst-case bound, but it isolates the obstruction.

### Corollary 7.1: bounded attachment

If every maximal triangle satisfies \(a(T)\le B\), then

\[
|\mathcal T|
 =O\!\left((B+1)n^{3/2}+(B+1)^2n\right).
\]

In particular, for fixed \(B\),

\[
|\mathcal T|=O_B(n^{3/2}).
\]

If, additionally, \(G\) is \(K_4\)-free, all maximal cliques have order at most three, and hence

\[
\#\{\text{maximal cliques of }G\}=O_B(n^{3/2}).
\]

This exponent is sharp even for \(B=0\).

---

## 8. Sharpness of the bounded-attachment result

Let \(q\) be an odd prime power, let \(V=\mathbb F_q^3\), and fix a nondegenerate symmetric bilinear form \(B\). Define a graph \(G_q\) whose vertices are the one-dimensional subspaces of \(V\), with distinct \([x],[y]\) adjacent when

\[
B(x,y)=0.
\]

There are

\[
n=q^2+q+1
\]

vertices.

For any two distinct projective points \([x],[y]\),

\[
x^\perp\cap y^\perp
\]

is one-dimensional. Thus every pair has at most one common neighbor. In particular, \(G_q\) is \(2\)-closed and hence \(3\)-closed.

There are \(q^2\) nonisotropic projective points. For every nonisotropic \([x]\), the two-dimensional space \(x^\perp\) contains at least \(q-1\) nonisotropic projective points \([y]\). For each such ordered orthogonal pair, the one-dimensional space

\[
(\operatorname{span}\{x,y\})^\perp
\]

gives a third nonisotropic projective point \([z]\), and \([x],[y],[z]\) form a triangle. Every such triangle is counted six times by ordered pairs, so there are at least

\[
\frac{q^2(q-1)}6=\Theta(q^3)=\Theta(n^{3/2})
\]

triangles.

These triangles are maximal. Indeed, a vertex adjacent to both \([x]\) and \([y]\) must equal \([z]\). Consequently \(a(T)=0\) for every such triangle.

Thus the \(O_B(n^{3/2})\) special-case estimate cannot be improved in exponent.

---

## 9. A general bounded-edge-codegree special case

For completeness, there is also a simple all-\(c\) consequence.

Suppose \(G\) is \(c\)-closed and every edge has at most \(D\) common neighbors, where \(c,D\) are fixed. Then every pair of vertices has at most

\[
\max\{c-1,D\}
\]

common neighbors. Wedge counting gives

\[
|E(G)|=O_{c,D}(n^{3/2}).
\]

Every clique containing an edge \(uv\) lies inside

\[
\{u,v\}\cup (N(u)\cap N(v)),
\]

which has at most \(D+2\) vertices. Thus each edge is contained in at most \(2^D\) cliques, and

\[
\#\{\text{maximal cliques of }G\}=O_{c,D}(n^{3/2}).
\]

The exponent is again sharp by standard \(C_4\)-free incidence graphs.

---

## 10. Remaining gap

The unresolved \(c=3\) obstruction is now quite specific. To attain the known \(n^{7/4}\) upper scale, one would need roughly

- \(n^{3/2}\) relevant edges,
- each lying in about \(n^{1/4}\) maximal triangles,
- while the total attachment budget remains \(O(n^2)\).

Numerically this is consistent with all inequalities above. A roughly regular, \(K_4\)-free graph with degree \(\Theta(n^{1/2})\), adjacent-pair codegree \(\Theta(n^{1/4})\), and nonadjacent-pair codegree at most \(2\) would exhibit this behavior, but no such infinite family is constructed here.

Therefore the precise remaining question for \(c=3\) is whether the attachment systems of different maximal triangles can be simultaneously realized at that density. The present argument controls each triangle and each low-codegree edge separately, but supplies no further global compatibility inequality. For \(c>3\), Theorem 3.1 similarly reduces the problem to maximal cliques of orders \(3,\ldots,c\), but I do not obtain a better exponent for those bounded orders.