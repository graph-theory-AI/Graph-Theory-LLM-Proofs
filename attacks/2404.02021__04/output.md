```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds for every fixed 3-uniform H having a vertex set that meets every edge in exactly one vertex.",
  "would_publish": false,
  "caveats": "The tetrahedron K_4^(3) has no such transversal and remains open; the elementary lemma may already be known."
}
```

## 1. Formal setting and reduction

Write
\[
T_n:=K_{n,n,n}^{(3)}.
\]
Thus \(r_3(H,T_n)\) is the least \(N\) such that every red-blue coloring of \(\binom{[N]}3\) contains either a red copy of \(H\) or disjoint \(n\)-sets \(A,B,C\) for which every triple in \(A\times B\times C\) is blue.

A useful normalization is that the full conjecture is equivalent to its restriction to complete red hypergraphs. Indeed, if \(h=|V(H)|\), then \(H\subseteq K_h^{(3)}\), so
\[
r_3(H,T_n)\le r_3(K_h^{(3)},T_n).
\]
Consequently, proving the conjecture for every fixed \(K_h^{(3)}\) would prove it for every fixed \(H\). The first nontrivial complete case is \(K_4^{(3)}\).

The partial result below covers a substantial class not containing \(K_4^{(3)}\).

---

## 2. A common-link extraction lemma

For a vertex \(x\), let \(L_R(x)\) be its red link graph: its vertex set is \(V\setminus\{x\}\), and \(yz\) is an edge of \(L_R(x)\) precisely when \(xyz\) is red.

### Lemma 2.1

Let \(q\le R<N\), and suppose that for every \(x\in V\), every \(R\)-subset of \(V\setminus\{x\}\) contains a \(q\)-set \(I\) such that
\[
xyz\ \text{is blue for all distinct }y,z\in I.
\]
If
\[
N-q\ge a\binom Rq,
\]
then there are disjoint sets \(A,I\) with \(|A|=a\), \(|I|=q\), such that every triple \(xyz\), with \(x\in A\) and distinct \(y,z\in I\), is blue.

#### Proof

For \(x\in V\), let \(\mathcal I_x\) be the family of such \(q\)-sets \(I\subseteq V\setminus\{x\}\).

Double-count pairs \((S,I)\) where \(S\in\binom{V\setminus\{x\}}R\), \(I\in\mathcal I_x\), and \(I\subseteq S\). Every \(S\) contains at least one suitable \(I\), while any fixed \(I\) lies in exactly
\[
\binom{N-1-q}{R-q}
\]
such \(R\)-sets. Hence
\[
|\mathcal I_x|
 \ge
\frac{\binom{N-1}{R}}{\binom{N-1-q}{R-q}}
 =
\frac{\binom{N-1}{q}}{\binom Rq}.
\]

For \(I\in\binom Vq\), let
\[
d(I):=\bigl|\{x\notin I:I\in\mathcal I_x\}\bigr|.
\]
Averaging gives
\[
\frac{1}{\binom Nq}\sum_I d(I)
 =
\frac{1}{\binom Nq}\sum_x|\mathcal I_x|
 \ge
\frac{N-q}{\binom Rq}.
\]
Thus some \(I\) has \(d(I)\ge a\), and any \(a\) corresponding vertices form the desired set \(A\). ∎

For \(q=2n\) and \(a=n\), partitioning \(I\) into two \(n\)-sets produces a blue \(T_n\).

---

## 3. Multi-suspensions

Let \(F\) be a graph and \(t\ge1\). Define the 3-uniform multi-suspension \(\Sigma_tF\) by
\[
V(\Sigma_tF)=\{a_1,\dots,a_t\}\sqcup V(F)
\]
and
\[
E(\Sigma_tF)
 =
\bigl\{\{a_i,u,v\}:i\in[t],\ uv\in E(F)\bigr\}.
\]
For \(t=1\), this is the usual suspension or cone over \(F\).

### Theorem 3.1

For every fixed graph \(F\) and fixed \(t\),
\[
r_3(\Sigma_tF,T_n)\le 2^{O_{F,t}(n\log n)}.
\]

More quantitatively, put \(f=|V(F)|\), \(q=2n\), and
\[
R=\max\{f,r_2(F,K_q^{(2)})\}.
\]
Then
\[
r_3(\Sigma_tF,T_n)
 =
O_{F,t}\left(R^f+n\binom R{2n}\right).
\]

#### Proof

Consider a red-blue coloring on \(N\) vertices with no red \(\Sigma_tF\).

For every injection
\[
\phi:V(F)\longrightarrow V,
\]
define its red support
\[
C_\phi=
\left\{
x\notin\phi(V(F)):
x\phi(u)\phi(v)\text{ is red for every }uv\in E(F)
\right\}.
\]
If \(|C_\phi|\ge t\), then \(\phi(V(F))\), together with any \(t\) vertices of \(C_\phi\), gives a red \(\Sigma_tF\). Therefore
\[
|C_\phi|\le t-1. \tag{3.1}
\]

Consider ordered pairs \((x,S)\) where \(x\in V\) and
\[
S\in\binom{V\setminus\{x\}}R.
\]
Call \((x,S)\) bad if \(L_R(x)[S]\) contains a copy of \(F\). A bad pair is witnessed by an injection \(\phi:V(F)\to S\) with \(x\in C_\phi\). By (3.1), the number \(B\) of bad pairs satisfies
\[
B\le
(t-1)N^f\binom{N-f-1}{R-f}.
\]
The total number of pairs is
\[
P=N\binom{N-1}R.
\]
Consequently,
\[
\frac BP
\le
(t-1)N^{f-1}
\frac{(R)_f}{(N-1)_f}
\le
\frac{2^f(t-1)R^f}{N},
\]
provided \(N\ge2f+2\). Thus, if
\[
N\ge2^{f+1}(t-1)R^f, \tag{3.2}
\]
at least \(P/2\) of the pairs \((x,S)\) are not bad.

For every nonbad pair, \(L_R(x)[S]\) has no red \(F\). By the definition of \(R\), it therefore contains a blue graph clique \(I\) of size \(q=2n\). Let \(\mathcal I_x\) denote all such \(q\)-sets in \(L_R(x)\). Counting incidences between nonbad pairs \((x,S)\) and blue \(q\)-cliques \(I\subseteq S\) gives
\[
\sum_x|\mathcal I_x|
\binom{N-1-q}{R-q}
\ge
\frac12N\binom{N-1}R.
\]
Hence
\[
\sum_x|\mathcal I_x|
\ge
\frac12N
\frac{\binom{N-1}q}{\binom Rq}.
\]
Averaging over \(I\in\binom Vq\), some \(I\) is a blue clique in at least
\[
\frac{N-q}{2\binom Rq}
\]
red links. If
\[
N-q\ge 2n\binom Rq, \tag{3.3}
\]
we may choose \(n\) such link vertices as \(A\), and partition \(I=B\sqcup C\) with \(|B|=|C|=n\). Every triple in \(A\times B\times C\) is blue.

Conditions (3.2) and (3.3), together with \(N>R\), prove the quantitative assertion.

Finally, if \(F\) has \(f\) vertices, then the ordinary graph Ramsey recursion gives
\[
R\le r_2(K_f^{(2)},K_{2n}^{(2)})
   \le \binom{2n+f-2}{f-1}
   =O_F(n^{f-1}).
\]
Therefore
\[
\binom R{2n}
\le
\left(\frac{eR}{2n}\right)^{2n}
\le
\left(C_F n^{f-2}\right)^{2n}
=
2^{O_F(n\log n)}.
\]
The additional \(R^f\) term is only polynomial in \(n\). ∎

---

## 4. Exact transversals

Call \(A\subseteq V(H)\) an exact transversal if
\[
|e\cap A|=1\qquad\text{for every }e\in E(H).
\]

### Corollary 4.1

If a fixed 3-uniform hypergraph \(H\) has an exact transversal, then
\[
r_3(H,T_n)\le 2^{O_H(n\log n)}.
\]

#### Proof

Let \(A\) be an exact transversal, put \(t=|A|\), and let \(B=V(H)\setminus A\). Define a graph \(F\) on \(B\) by
\[
uv\in E(F)
\quad\Longleftrightarrow\quad
\{a,u,v\}\in E(H)\text{ for some }a\in A.
\]
Then \(H\) is a subhypergraph of \(\Sigma_tF\): the multi-suspension may have additional edges, but it contains every edge of \(H\). Hence
\[
r_3(H,T_n)
\le r_3(\Sigma_tF,T_n),
\]
and Theorem 3.1 applies. ∎

This class includes:

- every ordinary suspension \(\Sigma F\);
- multi-suspensions with no common vertex in all edges;
- every strongly 3-partite 3-graph, by taking one of its parts as the exact transversal;
- disjoint unions of such hypergraphs, after taking the union of their exact transversals.

A notable nonlinear example is
\[
K_4^{(3)}-e=\Sigma_1K_3^{(2)}.
\]
Here
\[
r_2(K_3^{(2)},K_{2n}^{(2)})
\le \binom{2n+1}{2}=O(n^2),
\]
so the proof gives explicitly
\[
r_3(K_4^{(3)}-e,T_n)
\le 2^{2n\log_2 n+O(n)}.
\]

Thus the conjectured scale holds one edge short of the tetrahedron.

---

## 5. A polynomial refinement for a single suspension

When \(t=1\), sparsity of \(F\)-free link graphs can give a polynomial bound.

### Proposition 5.1

Suppose that for some \(C>0\) and \(0<\delta\le1\),
\[
\operatorname{ex}(m,F)\le C m^{2-\delta}
\qquad\text{for all }m.
\]
Then
\[
r_3(\Sigma_1F,T_n)=O_{F,C,\delta}\bigl(n^{2/\delta}\bigr).
\]

#### Proof

Take an arbitrary \(n\)-set \(A\), and let \(U\) be the remaining \(M\) vertices. Assume there is no red \(\Sigma_1F\). Then, for each \(a\in A\), the red link \(L_R(a)[U]\) is \(F\)-free and has at most \(CM^{2-\delta}\) edges.

Let \(J\) be the union of these \(n\) red link graphs on \(U\). Then
\[
e(J)\le CnM^{2-\delta}.
\]
Every graph with \(M\) vertices and \(e\) edges has an independent set of size at least
\[
\frac{M^2}{2e+M};
\]
this follows, for example, by taking the expected number of vertices preceding all their neighbors in a random ordering and applying Cauchy–Schwarz. Hence
\[
\alpha(J)
\ge
\frac{M^2}{2CnM^{2-\delta}+M}
=
\frac{M^\delta}{2Cn+M^{\delta-1}}
\ge
\frac{M^\delta}{2Cn+1}.
\]
Choosing
\[
M^\delta\ge(4C+2)n^2
\]
ensures \(\alpha(J)\ge2n\). Let \(I\) be an independent \(2n\)-set in \(J\), and split it into \(B,C\) of size \(n\). By the definition of \(J\), every triple in \(A\times B\times C\) is blue. ∎

For example:

- If \(F\) is a forest, then every \(F\)-free graph has \(O_F(m)\) edges, so
  \[
  r_3(\Sigma_1F,T_n)=O_F(n^2).
  \]
  Indeed, a graph of minimum degree at least \(|V(F)|-1\) contains \(F\) greedily, so every \(F\)-free graph is \(O_F(1)\)-degenerate.

- If \(F\) is bipartite, choose \(s\) with \(F\subseteq K_{s,s}\). The elementary Kővári-type count
  \[
  \sum_v\binom{d(v)}s
   =\sum_{S\in\binom Vs}|N(S)|
   \le(s-1)\binom{|V|}s
  \]
  gives
  \[
  \operatorname{ex}(m,F)=O_F(m^{2-1/s}),
  \]
  and therefore
  \[
  r_3(\Sigma_1F,T_n)=O_F(n^{2s}).
  \]

---

## 6. Why this does not handle \(K_4^{(3)}\)

The exact-transversal condition excludes \(K_4^{(3)}\). Indeed, if \(x_i\in\{0,1\}\) indicated membership in an exact transversal, then the four equations
\[
\sum_{i\ne j}x_i=1,\qquad j=1,2,3,4,
\]
would force all \(x_i\) equal, which is impossible.

The link argument also identifies the quantitative obstruction.

Suppose a coloring contains neither a red \(K_4^{(3)}\) nor a blue \(T_n\). For every vertex \(x\), its red link graph \(L_R(x)\) contains no red \(K_{3n}^{(2)}\). Otherwise, if \(S\) were a \(3n\)-clique in \(L_R(x)\), then any red triple inside \(S\) would complete a red tetrahedron with \(x\). Thus every triple inside \(S\) would be blue, and \(S\) would contain a blue \(T_n\).

Let
\[
R_n=r_2(K_{3n}^{(2)},K_{2n}^{(2)}).
\]
Every \(R_n\)-set in every link therefore contains a blue graph clique of size \(2n\). Lemma 2.1 yields
\[
r_3(K_4^{(3)},T_n)
\le
\max\left\{
R_n+1,\,
2n+n\binom{R_n}{2n}
\right\}. \tag{6.1}
\]
The ordinary graph Ramsey bound
\[
R_n\le\binom{5n-2}{3n-1}=2^{O(n)}
\]
makes (6.1) only
\[
2^{O(n^2)}.
\]

This quadratic loss cannot be removed merely by sharpening the estimate for \(R_n\). A random red-blue graph on \(M=2^{n/4}\) vertices has expected number of red \(K_{3n}\)'s plus blue \(K_{2n}\)'s at most
\[
\binom M{3n}2^{-\binom{3n}{2}}
+
\binom M{2n}2^{-\binom{2n}{2}}
=o(1).
\]
Hence
\[
R_n\ge2^{\Omega(n)}.
\]
Consequently, the denominator \(\binom{R_n}{2n}\) in this particular common-link count is necessarily \(2^{\Omega(n^2)}\).

A proof of the conjectured \(2^{O(n\log n)}\) bound for \(K_4^{(3)}\) must therefore exploit compatibility among the different link graphs, rather than treating each link only through its ordinary graph Ramsey properties. The multi-suspension argument succeeds because every fixed red copy of \(F\) can be supported by at most \(t-1\) link vertices; no analogous fixed-support bound is available for the tetrahedron.

## 7. Remaining gap

The argument proves the conjectured bound for all 3-graphs with an exact transversal, including nonlinear and connected examples without a common apex. It does not address \(K_4^{(3)}\), and hence does not settle the universal conjecture. It also does not improve the reported best universal \(2^{O_H(n^{2-\varepsilon_H})}\) bound.

The observations are elementary enough that they may already be implicit in existing methods; I have not verified a literature claim of novelty, so I would not regard this alone as a publishable resolution.