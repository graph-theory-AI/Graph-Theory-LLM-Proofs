```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but a separator-preserving stretching construction proves it for every candidate with an exact or locally regular power-law separator profile and implies monotonicity of b_epsilon.",
  "would_publish": false,
  "caveats": "The unresolved case permits highly oscillatory separator profiles whose locally regular witnesses occur at multiplicatively sparse scales."
}
```

## 1. Statement and notation

For a graph \(G\), let \(\operatorname{sep}(G)\) denote the minimum order of a set \(S\subseteq V(G)\) such that every component of \(G-S\) has at most \(2|V(G)|/3\) vertices. For a hereditary class \(\mathcal C\), write

\[
s_{\mathcal C}(n)=
 \max\{\operatorname{sep}(G):G\in\mathcal C,\ |V(G)|\le n\}.
\]

Let

\[
\operatorname{pex}(\mathcal C)=
\limsup_{r\to\infty}
 \frac{\log \max\{2,\nabla_{\mathcal C}(r)\}}{\log r}
\]

be its polynomial expansion exponent. The parameter in the source can be written as

\[
b_\varepsilon=
\inf\{\operatorname{pex}(\mathcal C):
 \mathcal C\text{ hereditary and }
 s_{\mathcal C}(n)=\Theta(n^{1-\varepsilon})\},
\]

and \(b'_\varepsilon\) is obtained by replacing the condition \(\Theta(n^{1-\varepsilon})\) with \(\Omega(n^{1-\varepsilon})\).

Clearly \(b'_\varepsilon\le b_\varepsilon\). The question is whether equality holds for \(0<\varepsilon<1/2\).

I do not obtain the full equality. I prove a regularization theorem which rules out all exact-power and a wider class of locally regular candidates as possible sources of strict inequality.

---

## 2. The graphwise lower bound only uses the one-sided hypothesis

Put

\[
\alpha=1-\varepsilon>\frac12.
\]

The separator-or-shallow-clique argument used in the source already gives

\[
b'_\varepsilon\ge
\frac{\alpha-\frac12}{1-\alpha}
=\frac1{2\varepsilon}-1.
\]

Indeed, from a graph \(G\) on \(n\) vertices with
\(\operatorname{sep}(G)\ge c n^\alpha\), the Plotkin–Rao–Smith alternative, with

\[
\ell\asymp n^{1-\alpha}
\quad\text{and}\quad
h\asymp \frac{n^{\alpha-1/2}}{\operatorname{polylog} n},
\]

forces a \(K_h\)-model of depth

\[
r=O(n^{1-\alpha}\operatorname{polylog}n).
\]

Thus

\[
\nabla_{\mathcal C}(r)
 \ge \frac{r^{(\alpha-1/2)/(1-\alpha)}}
          {\operatorname{polylog}r}.
\]

Only the lower bound on \(s_{\mathcal C}\) is used here. The difficulty is that the presently unknown value \(b_\varepsilon\) may be strictly larger than this universal graphwise lower bound.

---

# 3. A regular-witness reduction

For a graph \(G\) of order \(m\), set \(t=\operatorname{sep}(G)\). The important local condition is

\[
\operatorname{sep}(F)
 \le A\,t\left(\frac{|V(F)|}{m}\right)^\alpha
 \tag{1}
\]

for every nonempty induced subgraph \(F\) of \(G\).

This says that \(G\) has no induced subgraph whose normalized separator
\(\operatorname{sep}(F)/|V(F)|^\alpha\) is much larger than that of \(G\).

### Theorem 1: locally regular witnesses can be normalized

Let \(0<\alpha<1\), and let \(\mathcal C\) be a hereditary class with
\(\nabla_{\mathcal C}(0)<\infty\). Suppose that \(\mathcal C\) contains graphs
\(G_i\) of orders \(m_i\), with

\[
t_i=\operatorname{sep}(G_i)\to\infty,
\]

such that:

1. \(t_i\ge c m_i^\alpha\) for a fixed \(c>0\);
2. the numbers \(t_i^{1/\alpha}\) have bounded multiplicative gaps;
3. every induced subgraph \(F\subseteq G_i\) satisfies
   \[
   \operatorname{sep}(F)
   \le A\,t_i\left(\frac{|V(F)|}{m_i}\right)^\alpha
   \tag{2}
   \]
   with fixed \(A\).

Then there exists a hereditary class \(\mathcal D\) such that

\[
s_{\mathcal D}(n)=\Theta(n^\alpha)
\]

and

\[
\nabla_{\mathcal D}(r)
 \le \max\{2,\nabla_{\mathcal C}(2r+1)\}.
 \tag{3}
\]

In particular,

\[
\operatorname{pex}(\mathcal D)
 \le \operatorname{pex}(\mathcal C).
 \tag{4}
\]

The proof is constructive.

---

## 4. Weighted separators from hereditary unweighted separators

We first record a standard recursive observation.

### Lemma 2

Suppose that for every nonempty \(U\subseteq V(G)\),

\[
\operatorname{sep}(G[U])
 \le B |U|^\gamma
\]

for some \(0<\gamma\le1\). Then for every nonnegative vertex-weighting of \(G\), there is a weighted \(2/3\)-balanced separator of order at most

\[
\frac{B}{1-(2/3)^\gamma}|V(G)|^\gamma.
\]

The same assertion holds if \(G\) is replaced by any spanning subgraph.

#### Proof

Apply an unweighted balanced separator to \(G\). If no component has more than \(2/3\) of the total weight, stop. Otherwise there is a unique overweight component; recurse inside it. At each step the number of vertices falls by a factor at most \(2/3\). The total number of selected vertices is therefore at most

\[
B n^\gamma
 \sum_{j\ge0}(2/3)^{j\gamma}
 =
\frac{B}{1-(2/3)^\gamma}n^\gamma.
\]

Deleting edges can only split components, so the same separator works in a spanning subgraph. ∎

The same argument applies to the scale-dependent bound (2): a graph on \(p\) relevant vertices has a weighted separator of order at most

\[
C_\alpha A\,t_i\left(\frac p{m_i}\right)^\alpha,
\qquad
C_\alpha=\frac1{1-(2/3)^\alpha}.
\tag{5}
\]

---

## 5. The stretching construction

Since \(\nabla_{\mathcal C}(0)<\infty\), there is an integer \(d\ge1\) such that every graph in \(\mathcal C\) has an orientation of maximum outdegree at most \(d\).

Fix \(G=G_i\), with \(m=|V(G)|\) and \(t=\operatorname{sep}(G)\), and orient \(G\) with outdegree at most \(d\). Define

\[
L=\left\lceil\frac{t^{1/\alpha}}m\right\rceil.
\tag{6}
\]

Construct \(T=T(G,L)\) as follows.

* Replace every directed edge \(u\to v\) by a path
  \[
  u,x_1,\ldots,x_L,v,
  \]
  with \(L\) new internal vertices.
* For each \(u\), add \(d-d^+(u)\) pendant paths, each having \(L\) new vertices and one end at \(u\).

For each original vertex \(u\), define its block \(B_u\) to consist of:

* \(u\);
* all internal vertices on edge-paths directed out of \(u\);
* all vertices on the added pendant paths rooted at \(u\).

The blocks form a partition of \(V(T)\), and every block has the same order

\[
W=1+dL.
\]

Consequently,

\[
|V(T)|=mW=m(1+dL)=\Theta(t^{1/\alpha}),
\tag{7}
\]

where the constants depend only on \(c,\alpha,d\).

### Lemma 3: stretching does not reduce the separator

\[
\operatorname{sep}(T)\ge \operatorname{sep}(G)=t.
\]

#### Proof

Let \(X\) be a balanced separator of \(T\), and define

\[
Y=\{u\in V(G):B_u\cap X\ne\varnothing\}.
\]

Since the blocks are disjoint,

\[
|Y|\le |X|.
\]

Suppose \(|X|<t\). Then \(Y\) is not a balanced separator of \(G\), so some component \(C\) of \(G-Y\) has more than \(2m/3\) vertices.

For every \(u\in C\), the block \(B_u\) is disjoint from \(X\). Moreover, if \(u,v\in C\) are adjacent in \(G\), then the entire subdivided \(uv\)-path survives in \(T-X\). Thus all blocks \(B_u\), \(u\in C\), lie in one component of \(T-X\). That component has more than

\[
\frac{2m}{3}W=\frac{2|V(T)|}{3}
\]

vertices, contradicting the assumption that \(X\) is balanced. ∎

Thus the stretched roots give the required lower separator bound.

---

## 6. Separators in every induced subgraph of a stretched graph

Let \(J\) be an induced subgraph of \(T\), of order \(k\). If every component of \(J\) has at most \(2k/3\) vertices, no separator is needed. Otherwise let \(K\) be the unique component with more than \(2k/3\) vertices.

If \(K\) contains at most one original vertex of \(G\), then it is a tree obtained from path segments meeting at at most one branch vertex. It has a balanced separator of order one.

Suppose now that \(K\) contains \(p\ge2\) original vertices. Form a skeleton \(F\) on those \(p\) vertices: an edge \(uv\) is present in \(F\) exactly when the whole subdivided \(uv\)-path lies in \(K\). Since \(K\) is connected, \(F\) is connected. Each edge of a spanning tree of \(F\) contributes \(L\) internally disjoint subdivision vertices, and hence

\[
L(p-1)\le k.
\tag{8}
\]

Thus

\[
p\le 1+\frac{k}{L}.
\tag{9}
\]

Assign all vertices of \(K\) to the branch vertices of \(F\):

* an original vertex is assigned to itself;
* all internal vertices of a complete directed edge-path are assigned to its tail;
* a partial path segment attached to one branch vertex is assigned to that vertex.

Using Lemma 2 and the local hypothesis (2), choose a weighted balanced separator \(S\subseteq V(F)\) with

\[
|S|
 \le C_\alpha A\,t\left(\frac p m\right)^\alpha.
\tag{10}
\]

Delete the branch vertices in \(S\). If a complete path corresponding to an edge directed from a vertex of \(S\) to a vertex outside \(S\) survives attached to its head, delete one internal vertex next to that head. There are at most \(d|S|\) such paths. All other vertices formerly assigned to \(S\) lie in branchless path components. If one such path component is too large, one additional vertex bisects it.

It follows that \(K\), and hence \(J\), has a balanced separator of order at most

\[
(d+1)|S|+1.
\tag{11}
\]

Using (8), if \(p\ge2\), then \(p\le 2k/L\). Consequently,

\[
t\left(\frac p m\right)^\alpha
 \le
2^\alpha t\left(\frac{k}{Lm}\right)^\alpha
 \le 2^\alpha k^\alpha,
\tag{12}
\]

because \(Lm\ge t^{1/\alpha}\) by the definition of \(L\). We have therefore proved

\[
\operatorname{sep}(J)=O(k^\alpha),
\tag{13}
\]

uniformly over all \(i\) and all induced subgraphs \(J\subseteq T(G_i,L_i)\).

Together with Lemma 3 and (7), and using the bounded-gap hypothesis, the hereditary closure \(\mathcal D\) of the stretched graphs satisfies

\[
s_{\mathcal D}(n)=\Theta(n^\alpha).
\]

---

## 7. Expansion does not increase

It remains to prove (3).

Consider an \(r\)-shallow minor \(M\) of a stretched graph \(T\), represented by pairwise disjoint connected branch sets. Divide the vertices of \(M\) into two types:

* \(Z\): branch sets containing at least one original vertex of \(G\);
* \(R\): branch sets containing no original vertex.

A branch set of the second type lies in the interior of one subdivided edge-path or one pendant path. It is therefore an interval of a path and has degree at most two in \(M\).

For a branch set of the first type, project it to the original vertices of \(G\) that it contains. The projection is connected in \(G\), different projections are disjoint, and each has radius at most \(2r+1\). Moreover, every edge of \(M[Z]\) projects to an edge between the corresponding projected branch sets. Hence \(M[Z]\) is a subgraph of a \((2r+1)\)-shallow minor of \(G\).

Therefore

\[
\begin{aligned}
|E(M)|
&\le |E(M[Z])|+2|R|\\
&\le \nabla_{\mathcal C}(2r+1)|Z|+2|R|\\
&\le
\max\{2,\nabla_{\mathcal C}(2r+1)\}|V(M)|.
\end{aligned}
\]

This proves (3), and hence Theorem 1. ∎

---

# 8. Exact power profiles can always be regularized

The preceding theorem applies particularly cleanly to exact power laws.

### Theorem 4

Let \(0<\alpha\le\beta\le1\), and let \(\mathcal C\) be hereditary with finite expansion at every depth and

\[
s_{\mathcal C}(n)=\Theta(n^\beta).
\]

Then there is a hereditary class \(\mathcal D\) satisfying

\[
s_{\mathcal D}(n)=\Theta(n^\alpha)
\]

and

\[
\operatorname{pex}(\mathcal D)
 \le \operatorname{pex}(\mathcal C).
\]

#### Proof

Choose geometrically increasing \(n_i\), and a graph \(G_i\in\mathcal C\) of order \(m_i\le n_i\) with

\[
\operatorname{sep}(G_i)\ge c n_i^\beta.
\]

The upper bound \(s_{\mathcal C}(m_i)\le C m_i^\beta\) implies \(m_i=\Theta(n_i)\). Hence, writing \(t_i=\operatorname{sep}(G_i)\),

\[
t_i=\Theta(m_i^\beta).
\tag{14}
\]

For every induced \(F\subseteq G_i\), with \(p=|V(F)|\),

\[
\operatorname{sep}(F)\le C p^\beta.
\]

Since \(\beta\ge\alpha\) and \(p\le m_i\),

\[
p^\beta
 =m_i^\beta\left(\frac p{m_i}\right)^\beta
 \le m_i^\beta\left(\frac p{m_i}\right)^\alpha
 =O\!\left(
 t_i\left(\frac p{m_i}\right)^\alpha
 \right).
\]

Thus the local condition (2) holds. Also \(t_i^{1/\alpha}\) has bounded multiplicative gaps by (14). Theorem 1 applies. ∎

---

# 9. Consequences for \(b_\varepsilon\)

Set

\[
\alpha=1-\varepsilon,\qquad \beta=1-\eta.
\]

If \(0<\eta\le\varepsilon<1\), then \(\beta\ge\alpha\). Theorem 4 gives

\[
\boxed{\,b_\varepsilon\le b_\eta\,}.
\tag{15}
\]

Thus \(b_\varepsilon\) is monotone nonincreasing as \(\varepsilon\) increases.

More directly, define a restricted one-sided parameter

\[
b^{\mathrm{pow}}_\varepsilon
=
\inf\left\{
\operatorname{pex}(\mathcal C):
s_{\mathcal C}(n)=\Theta(n^{1-\eta})
\text{ for some }0<\eta\le\varepsilon
\right\}.
\]

Then

\[
\boxed{\,b^{\mathrm{pow}}_\varepsilon=b_\varepsilon\,}.
\tag{16}
\]

Indeed, target-exponent classes show
\(b^{\mathrm{pow}}_\varepsilon\le b_\varepsilon\). Conversely, if
\(s_{\mathcal C}(n)=\Theta(n^{1-\eta})\) with \(\eta\le\varepsilon\), Theorem 4 constructs a class with separator exponent \(1-\varepsilon\) and no larger expansion exponent. Therefore
\(\operatorname{pex}(\mathcal C)\ge b_\varepsilon\).

Consequently, allowing a stronger but still exact power-law separator profile cannot decrease the extremal expansion exponent. Any strict inequality

\[
b'_\varepsilon<b_\varepsilon
\]

would have to arise from a class whose separator function is not comparable to any fixed power.

---

# 10. The precise remaining gap

For \(\alpha\in(0,1)\), define

\[
\rho_\alpha(G)=
\frac{\operatorname{sep}(G)}{|V(G)|^\alpha}.
\]

Every finite graph \(G\) contains an induced subgraph \(H\) maximizing
\(\rho_\alpha\) among its induced subgraphs. Such an \(H\) automatically satisfies

\[
\operatorname{sep}(F)
 \le
\operatorname{sep}(H)
 \left(\frac{|V(F)|}{|V(H)|}\right)^\alpha
\]

for every induced \(F\subseteq H\). Thus it is a perfect locally regular witness for Theorem 1.

The obstruction is scale control: when this maximizing \(H\) is extracted from a large graph witnessing

\[
s_{\mathcal C}(n)\ge c n^\alpha,
\]

its own separator may lie at a much smaller scale. I do not know how to prove that one can choose these maximizers so that their separator values have bounded multiplicative gaps. Nor do I have a graph class showing that such gaps can genuinely occur while maintaining low polynomial expansion.

Therefore:

* the conjecture holds for exact power profiles;
* it holds more generally whenever there is a geometrically cofinal family of locally \(\alpha\)-regular witnesses;
* a counterexample, if one exists, must exploit persistent oscillation or nesting of induced subgraphs with increasingly larger normalized separator ratios at multiplicatively sparse separator scales.

That extraction problem is the unresolved step, so the full equality \(b'_\varepsilon=b_\varepsilon\) is not proved here.