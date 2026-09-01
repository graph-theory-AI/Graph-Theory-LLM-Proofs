```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "The bipartite logarithmic lower bound transfers to all graphs by combining an affine-function obstruction for high chromatic number with a dense induced bipartite core in the low-chromatic case.",
  "would_publish": true,
  "caveats": "This uses the standard edgewise definition of separation and the quoted bipartite Theorem 1.2; literature priority has not been independently checked."
}
```

# Statement

For a graph \(G\), call a \(k\)-list assignment \(L\) separated if
\[
|L(u)\cap L(v)|\le 1
\qquad\text{for every }uv\in E(G).
\]
Then \(\operatorname{ch}_{\mathrm{sep}}(G)\) is the least \(k\) for which every separated \(k\)-list assignment is colorable.

We prove the following stronger form of Conjecture 1.3.

**Theorem.** There is an absolute \(c>0\) such that every graph \(G\) of sufficiently large minimum degree \(d\) satisfies
\[
\operatorname{ch}_{\mathrm{sep}}(G)
 \ge c\,\frac{\log d}{\log\log d}.
\]

The only external input is the established bipartite case, Theorem 1.2 of the source paper.

## 1. Induced-subgraph monotonicity

**Lemma 1.** If \(H\) is an induced subgraph of \(G\), then
\[
\operatorname{ch}_{\mathrm{sep}}(H)
 \le \operatorname{ch}_{\mathrm{sep}}(G).
\]

**Proof.** Suppose \(H=G[S]\) has an uncolorable separated \(k\)-list assignment \(L\). For every \(v\notin S\), give \(v\) a set of \(k\) fresh colors, with these sets pairwise disjoint and disjoint from every list on \(S\).

The resulting assignment on \(G\) is separated: edges within \(S\) are handled because \(H\) is induced, while every edge having an endpoint outside \(S\) has lists with empty intersection. Any coloring of \(G\) would restrict to an \(L\)-coloring of \(H\), a contradiction. \(\square\)

## 2. High chromatic number directly forces high separation choosability

**Lemma 2.** For every positive integer \(k\), if
\[
\chi(G)>4k^{2},
\]
then \(G\) is not separation \(k\)-choosable. In particular,
\[
\operatorname{ch}_{\mathrm{sep}}(G)>k.
\]

**Proof.** Put \(r=\chi(G)\), and fix a proper \(r\)-coloring with independent color classes
\[
V_1,\dots,V_r.
\]

Let \(q\) be the least power of \(2\) satisfying \(q\ge\sqrt r\). Then
\[
\sqrt r\le q<2\sqrt r.
\]
Since \(r>4k^2\), we have \(q>k\). Let \(\mathbb F_q\) be the field of order \(q\), and choose a \(k\)-element subset \(X\subseteq\mathbb F_q\).

Use the palette
\[
P=X\times\mathbb F_q,
\qquad |P|=kq.
\]
For every pair \((a,b)\in\mathbb F_q^2\), define the \(k\)-set
\[
S_{a,b}=\{(x,ax+b):x\in X\}.
\]
Two distinct affine functions \(ax+b\) and \(a'x+b'\) agree at at most one field element, so
\[
|S_{a,b}\cap S_{a',b'}|\le1
\quad\text{whenever }(a,b)\ne(a',b').
\]

There are \(q^2\ge r\) parameter pairs. Assign distinct pairs \((a_i,b_i)\) to the \(r\) color classes, and give every vertex in \(V_i\) the list \(S_{a_i,b_i}\). Adjacent vertices belong to distinct color classes, so this is a separated \(k\)-list assignment.

On the other hand,
\[
|P|=kq<2k\sqrt r<r=\chi(G),
\]
where the last strict inequality follows from \(r>4k^2\). Any proper list coloring would be a proper coloring of \(G\) using at most \(|P|<\chi(G)\) colors, which is impossible. \(\square\)

Thus high chromatic number presents no obstruction to the conjecture; it already supplies the required bad list assignment.

## 3. Low chromatic number gives a dense induced bipartite core

**Lemma 3.** Let \(G\) have minimum degree \(d>0\) and chromatic number \(r\). Then \(G\) contains an induced bipartite subgraph \(B\) satisfying
\[
\delta(B)\ge \frac{d}{2(r-1)}.
\]

**Proof.** Let \(V_1,\dots,V_r\) be the color classes of a proper \(r\)-coloring. Write
\[
n_i=|V_i|,\qquad
e_{ij}=e_G(V_i,V_j).
\]
If \(n=|V(G)|\) and \(m=|E(G)|\), then
\[
\sum_{i<j}e_{ij}=m
\]
and
\[
\sum_{i<j}(n_i+n_j)=(r-1)n.
\]
Consequently, for some \(i<j\),
\[
\frac{e_{ij}}{n_i+n_j}
 \ge \frac{m}{(r-1)n}.
\]
The induced graph
\[
H=G[V_i\cup V_j]
\]
is bipartite, and its average degree satisfies
\[
\overline d(H)
 =\frac{2e_{ij}}{n_i+n_j}
 \ge\frac{2m}{(r-1)n}
 \ge\frac{d}{r-1}.
\]

Every graph of average degree \(a\) has an induced subgraph of minimum degree at least \(a/2\): repeatedly delete vertices whose current degree is less than \(a/2\). Not all vertices can be deleted, since otherwise the deletion degrees would count every original edge once and have total strictly less than
\[
|V(H)|\,\frac a2=|E(H)|.
\]
Applying this to \(H\) gives an induced subgraph \(B\subseteq H\), hence also an induced subgraph of \(G\), such that
\[
\delta(B)\ge \frac{\overline d(H)}2
 \ge\frac{d}{2(r-1)}.
\]
It remains bipartite. \(\square\)

## 4. Deduction of Conjecture 1.3

The bipartite Theorem 1.2 has the following qualitative consequence:

> For every integer \(k\), there is an integer \(D_k\) such that every bipartite graph \(B\) with \(\delta(B)\ge D_k\) satisfies
> \[
> \operatorname{ch}_{\mathrm{sep}}(B)>k.
> \]

Fix \(k\), and let \(G\) have minimum degree
\[
d\ge 8k^2D_k.
\]
Put \(r=\chi(G)\).

* If \(r>4k^2\), Lemma 2 gives
  \[
  \operatorname{ch}_{\mathrm{sep}}(G)>k.
  \]

* If \(r\le4k^2\), Lemma 3 gives an induced bipartite subgraph \(B\) with
  \[
  \delta(B)
  \ge\frac{d}{2(r-1)}
  >\frac{d}{8k^2}
  \ge D_k.
  \]
  Hence \(\operatorname{ch}_{\mathrm{sep}}(B)>k\) by Theorem 1.2, and therefore
  \[
  \operatorname{ch}_{\mathrm{sep}}(G)>k
  \]
  by Lemma 1.

Thus, for every fixed \(k\), minimum degree at least \(8k^2D_k\) forces separation choosability greater than \(k\). This is exactly the claimed uniform divergence.

For example, setting
\[
T_k=8k^2D_k,\qquad
x_1(d)=1+\max\bigl(\{0\}\cup\{k:T_k\le d\}\bigr)
\]
gives a function \(x_1(d)\to\infty\) for which
\[
\operatorname{ch}_{\mathrm{sep}}(G)\ge x_1(d)
\]
whenever \(\delta(G)\ge d\).

## 5. Quantitative bound

The quoted bipartite theorem gives an absolute \(c_0>0\) such that, for sufficiently large \(D\),
\[
\operatorname{ch}_{\mathrm{sep}}(B)
 \ge c_0\frac{\log D}{\log\log D}
\]
for every bipartite \(B\) of minimum degree at least \(D\).

Set
\[
k=\left\lfloor\frac{c_0}{4}\frac{\log d}{\log\log d}\right\rfloor.
\]
If \(\chi(G)>4k^2\), Lemma 2 applies. Otherwise Lemma 3 supplies an induced bipartite \(B\) with
\[
\delta(B)\ge\frac{d}{8k^2}.
\]
Since \(k=O(\log d/\log\log d)\),
\[
\frac{\log(d/(8k^2))}
     {\log\log(d/(8k^2))}
=(1-o(1))\frac{\log d}{\log\log d}.
\]
The bipartite lower bound is therefore greater than \(k\) for all sufficiently large \(d\). Hence
\[
\operatorname{ch}_{\mathrm{sep}}(G)
 =\Omega\!\left(\frac{\log d}{\log\log d}\right)
\]
for arbitrary graphs \(G\) of minimum degree \(d\).

# Gaps and scope

There is no reliance on the open Ramsey-type induced-bipartite-subgraph question. The extra-edge obstruction noted in the source paper is avoided because the selected bipartite graph is induced: it comes from two independent color classes and subsequent vertex deletions.

The proof depends essentially on separation being required only for adjacent vertices, as in the extracted statement and source abstract. Literature priority for this transfer argument has not been independently verified.