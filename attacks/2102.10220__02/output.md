```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "With the displayed minimum over all n-vertex graphs, m(n,k)=0 identically, while replacing the minimum by a maximum gives a meaningful problem for which only partial results are established below.",
  "would_publish": false,
  "caveats": "This assumes open neighborhoods and induced edges on their union; the catalog may have transcribed max as min."
}
```

# Mathematical writeup

## 1. Precise interpretation and the quantifier problem

For a finite simple graph \(G\) and \(S\subseteq V(G)\), write

\[
D_G(S):=\bigcup_{v\in S}N_G(v),
\]

where neighborhoods are open, and interpret an edge as covered when both endpoints belong to \(D_G(S)\). Thus

\[
u(G,k):=\max_{|S|\le k}e\bigl(G[D_G(S)]\bigr).
\]

Adding vertices to \(S\) cannot decrease the covered edge set, so using \(|S|=k\) instead of \(|S|\le k\) makes no difference when \(k\le |V(G)|\).

Under the definition displayed in the prompt,

\[
m_{\min}(n,k):=\min_{|V(G)|=n}\bigl(e(G)-u(G,k)\bigr),
\]

the answer is immediate:

\[
\boxed{m_{\min}(n,k)=0.}
\]

Indeed, \(u(G,k)\le e(G)\) for every graph, while the empty \(n\)-vertex graph has \(e(G)=u(G,k)=0\).

Consequently, the displayed minimization cannot be the intended open extremal problem unless an additional constraint on \(G\) has been omitted. The natural worst-case version is

\[
M(n,k):=\max_{|V(G)|=n}\bigl(e(G)-u(G,k)\bigr).
\]

The remainder addresses this corrected version.

---

## 2. A universal upper bound and an exact case

Define

\[
r_k(G):=e(G)-u(G,k)
       =\min_{|S|\le k}\left(e(G)-e(G[D_G(S)])\right).
\]

### Proposition 2.1

For every \(n\)-vertex graph and every \(k\ge1\),

\[
r_k(G)\le
\frac{k^k}{(k+1)^{k+1}}\,n^2.
\]

Consequently,

\[
M(n,k)\le
\frac{k^k}{(k+1)^{k+1}}\,n^2.
\]

#### Proof

Choose \(v_1,\dots,v_k\) independently and uniformly from \(V(G)\), allowing repetitions, and put

\[
D=\bigcup_{i=1}^kN(v_i).
\]

For a vertex \(x\) of degree \(d(x)\),

\[
\Pr(x\notin D)=\left(1-\frac{d(x)}n\right)^k.
\]

Every edge not contained in \(G[D]\) has at least one endpoint outside \(D\). Hence, writing \(R=e(G)-e(G[D])\),

\[
R\le \sum_{x\in V(G)}d(x)\mathbf 1_{\{x\notin D\}}.
\]

Taking expectations gives

\[
\mathbb E R
\le
\sum_x d(x)\left(1-\frac{d(x)}n\right)^k.
\]

For \(0\le t\le n\), the function \(t(1-t/n)^k\) is maximized at
\(t=n/(k+1)\), with maximum

\[
\frac{n}{k+1}\left(\frac{k}{k+1}\right)^k.
\]

Therefore

\[
\mathbb E R
\le
n^2\frac{k^k}{(k+1)^{k+1}}.
\]

Some realization of the random tuple gives at most this many uncovered edges. Repetitions merely yield a set of at most \(k\) vertices. ∎

This bound has asymptotic constant

\[
\frac{k^k}{(k+1)^{k+1}}
=
\left(\frac1e+o(1)\right)\frac1k.
\]

### Corollary 2.2: the case \(k=1\)

\[
\boxed{M(n,1)=\left\lfloor\frac{n^2}{4}\right\rfloor.}
\]

#### Proof

Proposition 2.1 gives \(M(n,1)\le n^2/4\), and the residual is integral.

For the reverse inequality, take the balanced complete bipartite graph

\[
G=K_{\lfloor n/2\rfloor,\lceil n/2\rceil}.
\]

For every vertex \(v\), \(N(v)\) is one independent shore, so

\[
e(G[N(v)])=0.
\]

Thus \(u(G,1)=0\) and

\[
r_1(G)=e(G)=\left\lfloor\frac{n^2}{4}\right\rfloor.
\qquad\Box
\]

---

## 3. Another exact endpoint

The corrected problem can also be solved when \(k=n-1\).

### Proposition 3.1

For \(n\ge2\),

\[
M(n,n-1)=
\begin{cases}
1,&n\text{ even},\\
0,&n\text{ odd}.
\end{cases}
\]

Also \(M(n,n)=0\).

#### Proof

For \(v\in V(G)\), let

\[
\lambda(v):=\bigl|\{x\in N(v):d(x)=1\}\bigr|
\]

be the number of leaves adjacent to \(v\). Take \(S=V(G)\setminus\{v\}\).

Every nonisolated vertex other than a leaf whose unique neighbor is \(v\) belongs to \(D_G(S)\). The vertex \(v\), if nonisolated, is also dominated by one of its neighbors in \(S\). It follows that the uncovered edges are exactly the \(\lambda(v)\) leaf edges at \(v\). Hence

\[
r_{n-1}(G)=\min_{v\in V(G)}\lambda(v).
\]

If \(\min_v\lambda(v)\ge1\), then every vertex \(v\) has a leaf neighbor \(x\). Applying the same condition to \(x\), whose only neighbor is \(v\), forces \(d(v)=1\). Thus every vertex has degree one, so \(G\) is a perfect matching and \(n\) is even. In a perfect matching every \(\lambda(v)=1\).

Moreover, \(\min_v\lambda(v)\ge2\) is impossible, since a leaf has only one neighbor. This proves the asserted formula. Finally, taking \(S=V(G)\) dominates every nonisolated vertex, so all edges are covered and \(M(n,n)=0\). ∎

---

## 4. A probabilistic lower bound for the corrected maximum

For fixed \(k\), random graphs give a considerably stronger lower bound than disjoint elementary constructions.

Define

\[
L_k:=
\max_{0\le p\le1}
p\left((1-p)^k-\frac12(1-p)^{2k}\right).
\]

### Proposition 4.1

For each fixed \(k\),

\[
\liminf_{n\to\infty}\frac{M(n,k)}{n^2}\ge L_k.
\]

#### Proof

Fix \(p\in(0,1)\) and take \(G\sim G(n,p)\). For a fixed \(k\)-set \(S\), let

\[
T_S:=\{x\in V(G)\setminus S:N(x)\cap S=\varnothing\}.
\]

Put \(a=(1-p)^k\). Since membership in \(T_S\) is determined by the edges between \(S\) and \(V(G)\setminus S\),

\[
|T_S|\sim\operatorname{Bin}(n-k,a).
\]

For fixed \(k\), Chernoff bounds and a union bound over at most \(n^k\) choices of \(S\) show that, with probability tending to one,

\[
|T_S|=(a+o(1))n
\]

simultaneously for every \(k\)-set \(S\).

Every edge within \(V(G)\setminus S\) having at least one endpoint in \(T_S\) is uncovered by \(S\). Conditional on \(T_S\), these edges remain mutually independent Bernoulli-\(p\) variables, because \(T_S\) depends only on edges incident with \(S\). The number of possible such edges is

\[
\binom{n-k}{2}-\binom{n-k-|T_S|}{2}
=
\left(a-\frac{a^2}{2}+o(1)\right)n^2.
\]

A second Chernoff bound, again uniformly over the \(O(n^k)\) sets \(S\), therefore gives

\[
e(G)-e(G[D_G(S)])
\ge
\left[p\left(a-\frac{a^2}{2}\right)-o(1)\right]n^2
\]

for every \(S\). Thus, with positive probability,

\[
r_k(G)\ge
\left[
p\left((1-p)^k-\frac12(1-p)^{2k}\right)-o(1)
\right]n^2.
\]

Optimizing over \(p\) proves the result. ∎

### Large-\(k\) constants

Let

\[
\Phi(c):=c\left(e^{-c}-\frac12e^{-2c}\right).
\]

Setting \(p=c/k\) shows

\[
kL_k\longrightarrow C_0:=\max_{c\ge0}\Phi(c).
\]

The unique maximizer \(c_0>0\) satisfies

\[
2e^{c_0}(1-c_0)=1-2c_0,
\]

or equivalently

\[
2e^{c_0}(c_0-1)=2c_0-1.
\]

Numerically,

\[
c_0\approx1.2119,\qquad C_0\approx0.3070.
\]

Thus, in the iterated limit \(n\to\infty\) followed by \(k\to\infty\), the corrected problem currently has the elementary constant gap

\[
0.3070\ldots
\ \le\
k\,\frac{M(n,k)}{n^2}
\ \le\
\frac1e+o(1)
=
0.367879\ldots+o(1).
\]

The lower assertion here is meant in the precise form

\[
\liminf_{k\to\infty}
k\left(\liminf_{n\to\infty}\frac{M(n,k)}{n^2}\right)
\ge C_0.
\]

---

## 5. A sharper bound for regular graphs

The preceding universal upper bound double-counts edges whose two endpoints are both undominated. Inclusion–exclusion removes this loss for regular graphs.

For a random ordered \(k\)-tuple as above and an edge \(xy\), let \(A_x\) be the event \(x\notin D\). Then

\[
\Pr(A_x)=\left(1-\frac{d(x)}n\right)^k
\]

and

\[
\Pr(A_x\cap A_y)
=
\left(1-\frac{|N(x)\cup N(y)|}{n}\right)^k.
\]

Consequently, some \(S\) with \(|S|\le k\) satisfies

\[
\begin{aligned}
r_k(G)
\le \sum_{xy\in E(G)}
\bigg[
&\left(1-\frac{d(x)}n\right)^k
+\left(1-\frac{d(y)}n\right)^k\\
&-\left(1-\frac{d(x)+d(y)}n\right)_+^k
\bigg],
\end{aligned}
\tag{1}
\]

where \(z_+=\max\{z,0\}\). Here we used
\(|N(x)\cup N(y)|\le d(x)+d(y)\).

If \(G\) is \(d\)-regular, (1) becomes

\[
r_k(G)
\le
\frac{nd}{2}
\left[
2\left(1-\frac dn\right)^k
-
\left(1-\frac{2d}{n}\right)_+^k
\right].
\tag{2}
\]

Let

\[
B_k:=
\max_{0\le x\le1}
\frac{x}{2}
\left[2(1-x)^k-(1-2x)_+^k\right].
\]

Then every \(n\)-vertex regular graph satisfies \(r_k(G)\le B_kn^2\), and

\[
kB_k\longrightarrow C_0\approx0.3070.
\]

Indeed, putting \(x=c/k\) in the expression defining \(B_k\) gives \(\Phi(c)\), while choices with \(kx\to\infty\) contribute at most \(kx\,e^{-kx}=o(1)\).

Thus the random-graph lower-bound constant \(C_0\) is also the asymptotically correct upper-bound constant within the regular setting. Any example approaching the larger universal constant \(1/e\) would therefore have to exploit substantial degree irregularity, unless a better selection distribution than uniform random sampling closes the gap.

---

## 6. Computational complexity of the graph-specific problem

There is also a clean complexity classification when \(k\) is part of the input.

### Proposition 6.1

Under the interpretation above, deciding whether

\[
u(G,k)=e(G)
\]

is NP-complete, even for bipartite graphs with no isolated vertices.

#### Proof

If \(G\) has no isolated vertices, then

\[
e(G[D_G(S)])=e(G)
\quad\Longleftrightarrow\quad
D_G(S)=V(G).
\]

Thus full edge coverage is precisely the existence of a total dominating set \(S\): every vertex has a neighbor in \(S\).

For completeness, reduce from SET COVER. Let the universe be
\(X=\{x_1,\dots,x_q\}\), let the available sets be
\(F_1,\dots,F_m\), and assume \(X\neq\varnothing\) and every element lies in some \(F_i\). Construct a graph with vertices

\[
\{r,\ell\}\cup\{s_1,\dots,s_m\}\cup X
\]

and edges

\[
r\ell,\qquad rs_i\quad(1\le i\le m),
\qquad s_ix_j\quad\text{when }x_j\in F_i.
\]

This graph is bipartite, with parts
\(\{r\}\cup X\) and \(\{\ell\}\cup\{s_i\}\), and has no isolated vertices.

If \(F_{i_1},\dots,F_{i_t}\) cover \(X\), then

\[
S=\{r,s_{i_1},\dots,s_{i_t}\}
\]

is a total dominating set: \(r\) dominates every set vertex and \(\ell\), the chosen set vertices dominate \(r\), and they dominate all element vertices.

Conversely, any total dominating set must contain \(r\), because \(\ell\) has the unique neighbor \(r\). Every element vertex must have a selected set vertex as a neighbor, so the selected set vertices form a set cover. Therefore there is a set cover of size at most \(k\) if and only if the constructed graph has full neighborhood-union coverage using at most \(k+1\) vertices.

Membership in NP is immediate. ∎

For every fixed \(k\), direct enumeration of all \(O(n^k)\) sets gives a polynomial-time algorithm, but the exponent depends on \(k\).

---

## 7. Remaining gap

1. With the literal \(\min_G\), the quantity is zero and there is no open problem.
2. If \(\max_G\) was intended, the exact value is established above for \(k=1\), \(k=n-1\), and \(k=n\), but not for general \(2\le k\le n-2\).
3. For fixed \(k\),

   \[
   L_k
   \le
   \liminf_{n\to\infty}\frac{M(n,k)}{n^2}
   \le
   \limsup_{n\to\infty}\frac{M(n,k)}{n^2}
   \le
   \frac{k^k}{(k+1)^{k+1}}.
   \]

4. In the large-\(k\), large-\(n\) iterated regime, the unresolved leading-constant interval is approximately

   \[
   0.3070\le C\le0.3679.
   \]

5. I have not verified whether the source paper already contains the universal upper bound or the random lower construction, and I make no claim of novelty for them. The regular-graph refinement and complexity observation do not resolve the intended extremal question.