```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the literal edge-incidence definition, the bound holds for all complete bipartite graphs and some perturbations, with the exact value tau(K_{a,b})=b when b is at least 2a+1, but the general case remains unresolved.",
  "would_publish": false,
  "caveats": "The quoted complete-bipartite lower bound is incompatible with the literal definition, so the source definition or catalog summary should be checked."
}
```

## 1. Interpretation

I use the following standard interpretation. Graphs are finite, simple, and undirected; a path is an ordinary simple path subgraph, not necessarily induced. For a path system \(\mathcal P\), put
\[
\sigma_{\mathcal P}(e)=\{P\in\mathcal P:e\in E(P)\}.
\]
Then \(\mathcal P\) strongly separates \(E(G)\) precisely when, for every distinct \(e,f\),
\[
\sigma_{\mathcal P}(e)\not\subseteq \sigma_{\mathcal P}(f)
\quad\text{and}\quad
\sigma_{\mathcal P}(f)\not\subseteq \sigma_{\mathcal P}(e).
\]
Thus the edge signatures must form an antichain. In particular, distinct signatures of the same cardinality suffice.

Write \(\tau(G)\) for the minimum size of such a system.

The general \(2|V(G)|\) conjecture is not proved below. I prove it for all complete bipartite graphs, exactly determine \(\tau(K_{a,b})\) in a substantial unbalanced range, and give a robust extension to nearly complete bipartite graphs.

---

## 2. Basic observations

### 2.1 Sparse graphs

If \(m=|E(G)|\le 2|V(G)|\), the \(m\) singleton-edge paths give distinct one-element signatures. Hence
\[
\tau(G)\le m\le 2|V(G)|.
\]
Consequently, any counterexample must have average degree greater than \(4\).

### 2.2 A local lower bound

We use the following set-system lemma.

**Lemma 2.1.**  
Let \(A_1,\dots,A_d\) be pairwise incomparable subsets of a \(t\)-element ground set. Suppose every ground-set element belongs to at most two of the \(A_i\). If \(d\ge2\), then \(t\ge d\).

**Proof.**
For each coordinate belonging to exactly two sets \(A_i,A_j\), put an ordinary edge \(ij\) in an auxiliary multigraph on \([d]\). A coordinate belonging only to \(A_i\) is a private mark at \(i\).

Let \(r\) be the number of vertices having at least one private mark, let \(s\) be the number of private coordinates, and let \(q\) be the number of coordinates belonging to two sets. Thus \(s\ge r\).

If \(i\) has no private mark, then it must be incident with at least two ordinary auxiliary edges. Indeed, if it has none, then \(A_i=\varnothing\); if it has exactly one, say the coordinate also belongs to \(A_j\), then \(A_i\subseteq A_j\). Both alternatives contradict incomparability. Therefore
\[
2q\ge 2(d-r),
\]
so
\[
t\ge s+q\ge r+(d-r)=d. \qedhere
\]

At a vertex \(v\) of a graph, every path contains at most two edges incident with \(v\). Applying Lemma 2.1 to the signatures of the \(d(v)\) incident edges gives:

**Corollary 2.2.**
If \(\Delta(G)\ge2\), then
\[
\tau(G)\ge\Delta(G).
\]

For comparison, the path \(P_{m+1}\) actually needs \(m\) paths. Its edges can be ordered \(e_1,\dots,e_m\), and every path in \(P_{m+1}\) is an interval. A witness containing \(e_j\) but not \(e_{j+1}\) must have rightmost edge \(e_j\). These give \(m-1\) distinct paths, and a further path ending at \(e_m\) is needed. Singleton paths attain the bound.

---

## 3. An exact construction for highly unbalanced complete bipartite graphs

**Theorem 3.1.**  
Let \(1\le a\le b\). If
\[
b\ge 2a+1,
\]
then
\[
\tau(K_{a,b})=b.
\]

**Proof.**
Let
\[
A=\{x_1,\dots,x_a\},\qquad
B=\{y_s:s\in\mathbb Z_b\}.
\]
Define integers
\[
c_0=0,\qquad
c_r=(-1)^{r+1}\left\lceil\frac r2\right\rceil
\quad(1\le r\le a).
\]
Thus
\[
(c_0,c_1,c_2,c_3,c_4,\dots)=(0,1,-1,2,-2,\dots),
\]
and
\[
c_r-c_{r-1}=(-1)^{r+1}r.
\]

For each \(k\in\mathbb Z_b\), let
\[
P_k=
y_{k+c_0}\,x_1\,y_{k+c_1}\,x_2\cdots
x_a\,y_{k+c_a}.
\]
The \(c_r\) are distinct modulo \(b\): as integers they lie in an interval of length at most \(a<b\). Hence every \(P_k\) is a simple path.

For the edge \(x_r y_s\), one has
\[
\sigma(x_r y_s)
 =
 \{P_{\,s-c_{r-1}},P_{\,s-c_r}\}.
\]
Thus every edge has a two-element signature.

Suppose two edges \(x_r y_s\) and \(x_{r'}y_{s'}\) have the same signature. The difference, up to sign, between the two path labels in the first signature is
\[
\pm(c_r-c_{r-1})=\pm r,
\]
and similarly it is \(\pm r'\) for the second. Since
\[
1\le r,r'\le a,\qquad r+r'\le2a<b,
\]
the congruence \(\pm r\equiv\pm r'\pmod b\) forces \(r=r'\).

For this fixed \(r\), equality of the translated unordered pairs forces \(s=s'\). Indeed, a nonzero translation could preserve a two-element set only by interchanging its elements, which would give
\[
2r\equiv0\pmod b,
\]
impossible because \(2r\le2a<b\). Hence all \(ab\) signatures are distinct. Since all have cardinality two, they are pairwise incomparable.

This proves \(\tau(K_{a,b})\le b\). The reverse inequality follows from Corollary 2.2, since \(\Delta(K_{a,b})=b\). \(\square\)

The exceptional graph \(K_{1,2}\) also has \(\tau(K_{1,2})=2\), using its two singleton edges.

---

## 4. All complete bipartite graphs satisfy the conjecture

The preceding optimal construction does not cover the range \(a<b<2a+1\). The following two-family construction does.

**Theorem 4.1.**  
If \(1\le a<b\), then
\[
\tau(K_{a,b})\le2b.
\]

**Proof.**
The cases \(a=1\) are immediate from Theorem 3.1 or singleton paths, so assume \(a\ge2\). Again write
\[
A=\{x_0,\dots,x_{a-1}\},\qquad
B=\{y_s:s\in\mathbb Z_b\}.
\]

We require a permutation \(\pi\) of \(\{0,\dots,a-1\}\) for which the residues
\[
\pi(i)-i\pmod b
\]
are all distinct. Such a permutation can be given explicitly.

If \(a=2h+1\), define
\[
\pi(i)=
\begin{cases}
2i,&0\le i\le h,\\
2j-1,&i=h+j,\ 1\le j\le h.
\end{cases}
\]
Its displacement values are
\[
0,1,\dots,h,-h,\dots,-1.
\]

If \(a=2h\), define
\[
\pi(i)=
\begin{cases}
2i+1,&0\le i<h,\\
2j,&i=h+j,\ 0\le j<h.
\end{cases}
\]
Its displacement values are
\[
1,\dots,h,-h,\dots,-1.
\]
In either case the displacements are distinct modulo \(b\), because the difference between any two of the displayed integers has absolute value at most \(a<b\).

For a permutation \(p\) of \(\{0,\dots,a-1\}\) and \(k\in\mathbb Z_b\), define
\[
P_k^p=
y_k\,x_{p^{-1}(0)}\,y_{k+1}\,x_{p^{-1}(1)}
 \cdots
y_{k+a-1}\,x_{p^{-1}(a-1)}\,y_{k+a}.
\]
Since \(a<b\), the \(a+1\) displayed \(B\)-vertices are distinct, so this is a simple path.

Use the two families corresponding to \(p=\mathrm{id}\) and \(p=\pi\). For \(a\ge2\), these \(2b\) paths are distinct. Indeed, a path determines its traversal up to reversal; traversal in the displayed direction has successive \(B\)-subscripts increasing by one, whereas reversal has them decreasing by one. Equality with another displayed traversal in reverse would force \(1\equiv-1\pmod b\), impossible because \(b\ge3\).

If \(x_i\) occupies position \(p(i)\), then
\[
\sigma_p(x_i y_s)
 =
\{P^p_{\,s-p(i)},P^p_{\,s-p(i)-1}\}.
\]
The map
\[
d\longmapsto\{d,d-1\}
\]
on \(\mathbb Z_b\) is injective for \(b\ge3\).

Suppose \(x_i y_s\) and \(x_{i'}y_{s'}\) have equal signatures in the union of the two families. Equality in the identity block gives
\[
s-i\equiv s'-i'\pmod b,
\]
and equality in the \(\pi\)-block gives
\[
s-\pi(i)\equiv s'-\pi(i')\pmod b.
\]
Subtracting yields
\[
\pi(i)-i\equiv\pi(i')-i'\pmod b.
\]
The displacement property forces \(i=i'\), and then \(s=s'\). Thus all signatures are distinct. Every signature has exactly four elements, so the system strongly separates \(K_{a,b}\). \(\square\)

The balanced case follows by deleting one vertex.

**Corollary 4.2.**  
For every \(a\ge1\),
\[
\tau(K_{a,a})\le3a.
\]

**Proof.**
For \(a\ge2\), delete one vertex \(x\) in one bipartition class. The remaining \(K_{a-1,a}\) has a strongly separating system of at most \(2a\) paths by Theorem 4.1. Add the \(a\) singleton paths consisting of the edges incident with \(x\).

Edges in the two edge-disjoint parts are separated in both directions because every old edge lies on an old path, while every edge incident with \(x\) has its private singleton path. The case \(a=1\) is immediate. \(\square\)

Combining the results, for \(a\le b\),
\[
\tau(K_{a,b})\le
\begin{cases}
b,&b\ge2a+1,\\
2b,&a<b,\\
3a,&a=b.
\end{cases}
\]
In every case this is at most \(2(a+b)\). Thus the conjectured bound holds for all complete bipartite graphs.

---

## 5. Stability under a linear number of deleted edges

The constructions also apply to some incomplete bipartite graphs.

**Lemma 5.1.**  
Let \(H\) have a strongly separating path system \(\mathcal P\) of size \(q_0\), and suppose every edge of \(H\) lies in exactly \(r\) members of \(\mathcal P\). If \(G=H-F\), then
\[
\tau(G)\le q_0+r|F|.
\]

**Proof.**
For each \(P\in\mathcal P\), replace \(P\) by the nonempty path components of \(P-F\). If \(z_P=|E(P)\cap F|\), this creates at most \(z_P+1\) paths. Hence the total is at most
\[
q_0+\sum_{P\in\mathcal P}z_P
 =q_0+r|F|.
\]

For \(e,f\in E(G)\), choose an original witness \(P\) containing \(e\) but not \(f\). The component of \(P-F\) containing \(e\) remains a witness. The reverse direction is identical. \(\square\)

Consequently, let \(G\) be a bipartite graph with parts of sizes \(a<b\), obtained from \(K_{a,b}\) by deleting \(q\) edges.

- If \(b\ge2a+1\), the system of Theorem 3.1 has \(b\) paths and every edge occurs exactly twice. Therefore
  \[
  \tau(G)\le b+2q.
  \]
  In particular, the conjecture holds whenever
  \[
  2q\le2a+b.
  \]

- For arbitrary \(a<b\), the system of Theorem 4.1 has \(2b\) paths and every edge occurs exactly four times. Therefore
  \[
  \tau(G)\le2b+4q.
  \]
  Hence the conjecture holds whenever
  \[
  2q\le a.
  \]

These bounds may of course be combined with the singleton bound
\[
\tau(G)\le |E(G)|.
\]

---

## 6. Conflict with the quoted complete-bipartite lower bound

Under the literal definition in the prompt, Theorem 3.1 contradicts the contextual assertion that
\[
K_{\varepsilon n,(1-\varepsilon)n}
\]
requires at least \(2(1-2\varepsilon)n\) paths.

Indeed, put \(a=\varepsilon n\) and \(b=(1-\varepsilon)n\). For any fixed \(\varepsilon<1/3\) and sufficiently large admissible \(n\), one has \(b\ge2a+1\), and Theorem 3.1 gives
\[
\tau(K_{a,b})=b=(1-\varepsilon)n.
\]
The quoted lower bound is
\[
2(1-2\varepsilon)n=2(b-a),
\]
which exceeds \(b\) by
\[
b-2a=(1-3\varepsilon)n.
\]
This is a linear discrepancy, not an issue of rounding or lower-order terms.

A concrete example is \(K_{2,5}\). With indices modulo \(5\), the five paths
\[
P_k=y_k-x_1-y_{k+1}-x_2-y_{k-1},
\qquad k\in\mathbb Z_5,
\]
strongly separate all ten edges. Their signatures are
\[
\sigma(x_1y_s)=\{P_s,P_{s-1}\},
\qquad
\sigma(x_2y_s)=\{P_{s-1},P_{s+1}\}.
\]
These are exactly the ten distinct two-element subsets of a five-element set. Thus \(\tau(K_{2,5})=5\), the lower bound following from \(\Delta(K_{2,5})=5\).

Therefore, either:

1. the complete-bipartite lower-bound sentence in the catalog has been mistranscribed, or
2. the intended notion of “contains an edge” or “strongly separating path system” has an additional condition absent from the extracted statement.

All constructions above use ordinary, generally non-induced paths and regard only their traversed edges as contained in the path.

---

## 7. Necessary structure of a counterexample

For completeness, there is a simple reduction for any vertex-minimal counterexample \(G\) to the literal conjecture.

For \(S\subseteq V(G)\), let
\[
h_G(S)=|E(G[S])|+|E_G(S,V(G)\setminus S)|,
\]
the number of edges having at least one endpoint in \(S\).

If \(G\) is vertex-minimal among counterexamples, then:

1. \(G\) is connected;
2. \(|E(G)|>2|V(G)|\);
3. for every nonempty proper \(S\subset V(G)\),
   \[
   h_G(S)>2|S|.
   \]

For (3), apply minimality to \(G-S\), using at most \(2(|V(G)|-|S|)\) paths, and add every edge counted by \(h_G(S)\) as a singleton path. These two edge-disjoint systems strongly separate edges across the partition as well. If \(h_G(S)\le2|S|\), the total would be at most \(2|V(G)|\).

In particular, taking \(S=\{v\}\) gives
\[
\delta(G)\ge3.
\]
These conditions are weak but show that the unresolved case is necessarily a dense, irreducible core; neither the singleton argument nor the complete-bipartite constructions address such a general core.

## 8. Gap

No argument above handles an arbitrary graph with more than \(2n\) edges. The supergraph-restriction lemma is useful only when relatively few template-path edges are missing; for an arbitrary bipartite subgraph of \(K_{a,b}\), the number of missing edges may be quadratic, and splitting the template paths then gives no linear bound.

Thus the general \(2n\) conjecture remains open here. The principal concrete progress is the complete-bipartite construction—optimal for \(b\ge2a+1\)—together with its perturbative extension, and the identification of an apparent inconsistency in the supplied literature context.