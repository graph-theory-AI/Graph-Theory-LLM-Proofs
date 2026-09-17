```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Hedetniemi’s conjecture was disproved by Shitov in 2019; below is a self-contained, nonoptimized counterexample construction.",
  "would_publish": false,
  "caveats": "This is not a new resolution, and no claim is made about the smallest possible colour threshold."
}
```

## 1. Status and statement of the construction

The original OpenProblemGarden discussion is outdated. The conjecture was disproved in:

Y. Shitov, **“Counterexamples to Hedetniemi’s conjecture,”** *Annals of Mathematics* **190** (2019), 663–667, DOI: **10.4007/annals.2019.190.2.6**.

For completeness, the following gives a self-contained, deliberately nonoptimized exponential-graph argument. It does not require the catalogue’s assertions about the latest small-colour thresholds.

Write \(\alpha(F)\) for the independence number of \(F\).

**Counterexample construction.** Let \(F\) be a finite simple graph on \(n\ge2\) vertices such that
\[
\operatorname{girth}(F)\ge6,
\qquad
\alpha(F)<\frac n5.
\]
Set
\[
q=n^3,\qquad c=5q,\qquad G=F[K_q],
\]
where \(F[K_q]\) is the lexicographic product, and let
\[
H=K_c^G.
\]
Then \(G,H\) are finite simple graphs satisfying
\[
\chi(G)>c,\qquad \chi(H)>c,\qquad \chi(G\times H)\le c.
\]

We prove this construction first and then prove that a suitable \(F\) exists, with fully specified finite parameters.

## 2. The first factor and the product colouring

The vertices of \(G=F[K_q]\) are pairs \((x,j)\), where \(x\in V(F)\) and \(j\in[q]\). Adjacency means either
\[
xy\in E(F),
\quad\text{or}\quad
x=y\ \text{and}\ j\ne k.
\]

An independent set in \(G\) contains at most one vertex from each \(K_q\)-fibre, and its projection is independent in \(F\). Conversely, every independent set of \(F\) lifts to one in \(G\). Hence
\[
\alpha(G)=\alpha(F),
\]
so
\[
\chi(G)\ge \frac{|V(G)|}{\alpha(G)}
=\frac{nq}{\alpha(F)}>5q=c. \tag{1}
\]

The vertices of \(H\) are all functions \(f:V(G)\to[c]\). Its adjacency condition is
\[
f\sim_H g
\quad\Longleftrightarrow\quad
f(u)\ne g(w)\text{ for every ordered edge }uw\text{ of }G.
\]
Both orientations of each undirected edge are included.

A loop at \(f\) would say precisely that \(f\) is a proper \(c\)-colouring of \(G\). By (1), there are no such loops. Thus \(H\) is finite and simple.

Moreover,
\[
(u,f)\longmapsto f(u)
\]
is a proper \(c\)-colouring of \(G\times H\): adjacency of \((u,f)\) and \((w,g)\) gives \(uw\in E(G)\) and \(f\sim_H g\), hence \(f(u)\ne g(w)\).

It remains to prove \(\chi(H)>c\).

## 3. A consequence of a hypothetical \(c\)-colouring of \(H\)

Suppose, for a contradiction, that
\[
\Psi:V(H)\to[c]
\]
is a proper colouring.

For each \(i\in[c]\), let \(\kappa_i\) be the constant function with value \(i\). These functions form a \(c\)-clique, so we may permute the colour names to arrange
\[
\Psi(\kappa_i)=i.
\]
Consequently,
\[
\Psi(f)\in\operatorname{im}(f)
\qquad\text{for every }f\in V(H). \tag{2}
\]
Indeed, if \(i\notin\operatorname{im}(f)\), then \(f\) is adjacent to \(\kappa_i\), so \(\Psi(f)\ne i\).

For a function \(a:V(F)\to[c]\), define its fibre-constant extension by
\[
\bar a(x,j)=a(x),
\]
and put
\[
\psi(a)=\Psi(\bar a).
\]
Since \(q\ge2\),
\[
\bar a\sim_H\bar b
\quad\Longleftrightarrow\quad
a(x)\ne b(y)
\text{ whenever }y\in N_F[x], \tag{3}
\]
where \(N_F[x]\) is the closed neighbourhood. The condition with \(x=y\) comes from edges within a \(K_q\)-fibre.

### A robust colour

We claim that some \(v\in V(F)\) and \(r\in[c]\) satisfy
\[
\psi(a)=r
\quad\Longrightarrow\quad
r\in a(N_F[v])
\qquad\text{for every }a:V(F)\to[c]. \tag{4}
\]

For \(v\in V(F)\) and \(r\in[c]\), define
\[
\mathcal A_{v,r}
=\{a:V(F)\to[c]:\psi(a)=r,\ a(v)=r\}.
\]
By (2), every one of the \(c^n\) functions belongs to at least one such set. Therefore some pair \((v,r)\) satisfies
\[
|\mathcal A_{v,r}|
\ge \frac{c^{n-1}}n
> n^2c^{n-2}, \tag{5}
\]
where the strict inequality follows from \(c=5n^3>n^3\).

Suppose \(\psi(a)=r\), but \(r\notin a(N_F[v])\). For every \(b\in\mathcal A_{v,r}\), the functions \(\bar a,\bar b\) are distinct and have the same colour. Thus they are nonadjacent. By (3), some ordered pair \(x,y\), with \(y\in N_F[x]\), satisfies
\[
a(x)=b(y).
\]
Here \(y\ne v\), because \(b(v)=r\) whereas \(a\) avoids \(r\) on \(N_F[v]\).

For a fixed such pair \(x,y\), the conditions
\[
b(v)=r,\qquad b(y)=a(x)
\]
allow at most \(c^{n-2}\) functions \(b\). There are at most \(n^2\) possible pairs. Hence
\[
|\mathcal A_{v,r}|\le n^2c^{n-2},
\]
contradicting (5). This proves (4).

## 4. A clique forced into too few colours

Fix \(v,r\) satisfying (4).

The subgraph of \(F\) induced by vertices at distance at most two from \(v\) is bipartite, with parts
\[
\{v\}\cup\{x:d_F(v,x)=2\},
\qquad
N_F(v).
\]
To check this, an edge within \(N_F(v)\) would give a triangle. An edge between two distance-two vertices, together with chosen neighbours toward \(v\), would give either a triangle or a \(5\)-cycle. All are excluded.

Also, \(F\) is not bipartite because \(\alpha(F)<n/5\). Thus this radius-two ball is not all of \(V(F)\).

Choose disjoint sets
\[
A=\{a_1,\ldots,a_q\},\qquad
B=\{b_1,\ldots,b_q\}
\]
inside \([c]\setminus\{r\}\), and put
\[
T=[c]\setminus(A\cup B\cup\{r\}).
\]
Then
\[
|T|=3q-1>2q. \tag{6}
\]

For each \(t\in T\), define \(m_t:V(F)\to[c]\) by
\[
m_t(x)=
\begin{cases}
t,&x\in N_F[v],\\
r,&x\notin N_F[v].
\end{cases}
\]
Its colour belongs to \(\{t,r\}\) by (2). Property (4) excludes \(r\), so
\[
\Psi(\bar m_t)=t. \tag{7}
\]

Now define \(\phi_t:V(G)\to[c]\) by
\[
\phi_t(x,j)=
\begin{cases}
a_j,&d_F(v,x)\in\{0,2\},\\
b_j,&d_F(v,x)=1,\\
t,&d_F(v,x)>2.
\end{cases} \tag{8}
\]
Vertices in other components have distance infinity and fall into the last case.

### First adjacency check

For every \(t\in T\),
\[
\bar m_t\sim_H\phi_t. \tag{9}
\]

Indeed, if \(m_t(x)=r\), then this value appears nowhere in \(\phi_t\). If \(m_t(x)=t\), then \(x\in N_F[v]\), and every neighbour in \(G\) of \((x,j)\) projects into the radius-two ball. On that ball, \(\phi_t\) takes values in \(A\cup B\), not \(t\).

By (7) and (9), \(\Psi(\phi_t)\ne t\). Since the image of \(\phi_t\) is contained in \(A\cup B\cup\{t\}\), (2) gives
\[
\Psi(\phi_t)\in A\cup B. \tag{10}
\]

### Second adjacency check

For distinct \(s,t\in T\),
\[
\phi_s\sim_H\phi_t. \tag{11}
\]

Every edge of \(G\) is covered by the following cases:

- Within a fibre over the radius-two ball, distinct indices receive distinct \(a_j\)'s or distinct \(b_j\)'s.
- Between adjacent base vertices inside that ball, the two palettes are \(A\) and \(B\), which are disjoint.
- If exactly one base vertex is outside the ball, its value is \(s\) or \(t\), outside both palettes.
- If both base vertices are outside the ball, the two functions give the distinct values \(s,t\).

The functions \(\phi_t\) are distinct because there is a vertex outside the ball. Thus (11) gives a clique of size \(3q-1\), while (10) colours that clique using only the \(2q\) colours in \(A\cup B\). This contradicts (6).

Therefore \(\chi(H)>c\), completing the proof of the construction.

## 5. Existence of the base graph, with explicit parameters

Here is an elementary probabilistic proof that the required \(F\) exists.

Set
\[
N=2^{100},\qquad p=2^{-90},
\]
and let \(J\) be a random graph on \([N]\), each edge chosen independently with probability \(p\).

Let \(X\) count its cycles of lengths \(3,4,5\). Since \(Np=2^{10}\),
\[
\mathbb E X
\le \sum_{\ell=3}^{5}\frac{(Np)^\ell}{2\ell}
\le 3\cdot2^{50}.
\]
Markov’s inequality gives
\[
\Pr(X\ge N/2)\le6\cdot2^{-50}<\frac12. \tag{12}
\]

Let \(k=\lceil N/12\rceil\). A union bound gives
\[
\Pr(\alpha(J)\ge k)
\le \binom Nk(1-p)^{\binom k2}
\le 2^N e^{-p\binom k2}.
\]
Since \(k\ge N/12\) and \(k-1\ge N/24\),
\[
p\binom k2\ge\frac{pN^2}{576}=\frac{16}{9}N.
\]
Consequently,
\[
\Pr(\alpha(J)\ge k)
\le \exp\!\left((\log2-16/9)N\right)<\frac12. \tag{13}
\]

By (12)–(13), there is a graph \(J\) with
\[
X<N/2,\qquad
\alpha(J)\le k-1<N/12.
\]
Delete one vertex from each of its cycles of lengths \(3,4,5\), taking the union of the selected vertices. The resulting induced graph \(F\) has
\[
n>N/2,\qquad \operatorname{girth}(F)\ge6,
\]
and
\[
\alpha(F)\le\alpha(J)<N/12<n/6<n/5.
\]
It therefore meets all requirements.

To make this a deterministic finite specification, choose the lexicographically first labelled graph \(J\) satisfying the two displayed conditions, and delete the union of the least-labelled vertices of all its \(3\)-, \(4\)-, and \(5\)-cycles. The preceding argument proves that this finite search has a successful outcome; no search is claimed to have been executed.

## 6. Conclusion and scope

The resulting finite simple graphs satisfy
\[
\boxed{\chi(G\times H)\le c<\min\{\chi(G),\chi(H)\}},
\]
so they violate Hedetniemi’s proposed equality.

All existence and colouring steps above have been supplied. The construction is astronomically large and serves only as a self-contained demonstration of the already known negative resolution, not as a claim about optimal counterexample sizes or colour thresholds.