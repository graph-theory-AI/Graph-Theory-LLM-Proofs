```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjectured hardness for all non-edgeless targets satisfying the blow-up hypothesis when the forbidden family's minimum chromatic and clique numbers coincide.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; novelty and subsequent literature have not been independently checked."
}
```

# A partial theorem for arbitrary targets

All graphs below are finite and simple. Copies are not required to be induced, and
\[
N_T(H)=\frac{\operatorname{inj}(T,H)}{|\operatorname{Aut}(T)|}
\]
denotes the number of copies of \(T\) in \(H\).

I do not use the edgeless-target loophole as a resolution. I independently checked the vertex-cover/cone construction in the supplied attempt and retain it below. The additional ingredient is a symmetric gadget construction that works for **arbitrary non-edgeless targets**, not just cliques.

## Theorem

Fix a graph \(T\) with \(e(T)>0\), and a nonempty finite forbidden family \(\mathcal F\). Suppose there is an integer \(k\ge 3\) such that
\[
\omega(T)<k,\qquad
K_k\subseteq F\quad\text{for every }F\in\mathcal F,
\qquad
\chi(F_0)=k\quad\text{for some }F_0\in\mathcal F.
\tag{1}
\]
Then, for every fixed \(\epsilon>0\), approximating
\[
\operatorname{ex}(G,T,\mathcal F)
\]
within additive error \(n^{v(T)-\epsilon}\) is NP-hard.

This remains true when the input graph \(G\) is restricted to be \(K_{k+1}\)-free.

In particular, this proves the conjecture for every non-edgeless target and every forbidden family satisfying
\[
\min_{F\in\mathcal F}\chi(F)
=
\min_{F\in\mathcal F}\omega(F).
\tag{2}
\]
Here the target must satisfy the conjecture’s blow-up hypothesis. Thus it includes every singleton forbidden graph \(F\) with \(\chi(F)=\omega(F)\), and in particular all admissible clique-forbidden cases, including
\[
(T,\mathcal F)=(K_m,\{K_{m+1}\}).
\]

### Relation to the conjecture’s hypothesis

A graph \(F\) is a subgraph of a blow-up of \(T\) if and only if there is a graph homomorphism \(F\to T\).

Under the family assumptions in (1), the absence of such a homomorphism for every \(F\in\mathcal F\) is equivalent to \(\omega(T)<k\):

* If \(\omega(T)<k\), no graph containing \(K_k\) can map to \(T\).
* If \(T\) contains \(K_k\), a proper \(k\)-coloring of \(F_0\) gives
  \[
  F_0\longrightarrow K_k\longrightarrow T.
  \]

Thus the theorem establishes the entire intended hard regime for the class of families in (2).

---

## 1. An exact NP-hard auxiliary problem

For fixed \(k\ge3\), write
\[
z_k(Q)=\operatorname{ex}(Q,K_2,\{K_k\}).
\]

We first prove that computing \(z_k(Q)\) exactly is NP-hard even when \(Q\) is \(K_{k+1}\)-free. Only the standard NP-completeness of Vertex Cover is used.

### 1.1 Triangle-free vertex-cover instances

For every graph \(Y\),
\[
\tau(Y)=\min_{S\subseteq V(Y)}\bigl(|S|+e(Y-S)\bigr).
\tag{3}
\]
A vertex cover gives the upper bound. Conversely, from any \(S\), adding one endpoint of each edge of \(Y-S\) produces a vertex cover of size at most \(|S|+e(Y-S)\).

Given \(Y\), replace each edge \(uv\) by a path
\[
u-a_{uv}-b_{uv}-v,
\]
using distinct new vertices for different edges. Call the resulting triangle-free graph \(X\), and put \(r=e(Y)\).

If \(S\subseteq V(Y)\) is the set of original vertices selected in a vertex cover of \(X\), then the path replacing \(uv\) requires:

* one internal vertex if at least one of \(u,v\) belongs to \(S\);
* both internal vertices otherwise.

Consequently,
\[
\tau(X)
=r+\min_{S\subseteq V(Y)}\bigl(|S|+e(Y-S)\bigr)
=r+\tau(Y).
\tag{4}
\]

### 1.2 A cone encodes the cover number

Add an apex \(o\) adjacent to every vertex of \(X\), obtaining \(Q_0\). Since \(X\) is triangle-free, the triangles of \(Q_0\) are precisely
\[
ouv,\qquad uv\in E(X).
\]

Let \(\delta_3(Q_0)\) be the minimum number of edges whose deletion makes \(Q_0\) triangle-free. If
\[
S=\{v:ov\text{ is deleted}\},
\]
then every edge of \(X-S\) must also be deleted. Conversely, those deletions suffice. By (3),
\[
\delta_3(Q_0)
=\min_{S\subseteq V(X)}\bigl(|S|+e(X-S)\bigr)
=\tau(X).
\tag{5}
\]
Also, \(\omega(Q_0)\le3\).

### 1.3 Raising the forbidden clique size

Let \(q_0=v(Q_0)\). Form \(Q\) by joining \(Q_0\) to a complete \((k-3)\)-partite graph, with \(q_0\) vertices in each part. For \(k=3\), simply take \(Q=Q_0\).

Deleting a minimum triangle-deletion set inside \(Q_0\) makes the join \(K_k\)-free, so
\[
\delta_k(Q)\le\tau(X)<q_0.
\]

Conversely, let \(D\) be a minimum \(K_k\)-deletion set. Then \(|D|<q_0\). If a triangle survives in \(Q_0-D\), extend it greedily using one vertex from each of the \(k-3\) added parts. At each step, fewer than \(q_0\) candidates are excluded by deleted edges to previously selected vertices. Hence the extension exists and gives a \(K_k\), a contradiction.

Therefore \(Q_0-D\) is triangle-free, and (5) gives
\[
|D|\ge\tau(X).
\]
We have proved
\[
z_k(Q)=e(Q)-\tau(X)=e(Q)-r-\tau(Y).
\tag{6}
\]
The construction is polynomial, and
\[
\omega(Q)\le 3+(k-3)=k.
\]
This proves the claimed exact hardness on \(K_{k+1}\)-free graphs.

---

## 2. A quantitative bound on cliques in \(F_0\)-free graphs

Fix \(F_0\) from (1), and let
\[
a=\max\{2,v(F_0)\},\qquad
\delta=a^{-(k-1)},\qquad
C=(4a)^k.
\]
Since \(F_0\) is \(k\)-colorable, it is a subgraph of the balanced complete \(k\)-partite graph \(K_k^{(a)}\).

We will use the following explicit bound:
\[
N_{K_k}(H)\le C\,v(H)^{k-\delta}
\qquad\text{whenever }H\text{ is }F_0\text{-free}.
\tag{7}
\]
The positive power \(\delta\), rather than merely an \(o(v(H)^k)\) estimate, ensures that all subsequent amplification is polynomial-size.

### Proof of (7)

We prove the following elementary multipartite hypergraph bound. If an \(r\)-partite \(r\)-uniform hypergraph has at most \(h\) vertices in each part and contains no complete subhypergraph with \(a\) vertices in each part, then
\[
e(\mathcal H)\le (4a)^r h^{\,r-a^{-(r-1)}}.
\tag{8}
\]

For \(r=1\), there are at most \(a-1\) edges. Suppose \(r\ge2\), and write \(E=e(\mathcal H)\). For each tuple \(\mathbf x\) from the first \(r-1\) parts, let \(d(\mathbf x)\) be its number of extensions in the last part.

If \(E\le4a h^{r-1}\), (8) follows immediately. Otherwise, tuples with \(d(\mathbf x)\ge2a\) account for at least \(E/2\) extensions. Using
\[
\binom da\ge\left(\frac d{2a}\right)^a\qquad(d\ge2a)
\]
and the power-mean inequality gives
\[
\sum_{\mathbf x}\binom{d(\mathbf x)}a
\ge
\left(\frac{E}{4a}\right)^a
h^{-(r-1)(a-1)}.
\tag{9}
\]

For any \(a\)-set \(A\) in the last part, its common link is an \((r-1)\)-partite hypergraph avoiding the corresponding complete \(a\)-by-\(\cdots\)-by-\(a\) subhypergraph. Induction and double-counting therefore give
\[
\sum_{\mathbf x}\binom{d(\mathbf x)}a
\le
(4a)^{r-1}h^{\,a+r-1-a^{-(r-2)}}.
\tag{10}
\]
Combining (9) and (10),
\[
E\le
(4a)^{1+(r-1)/a}h^{\,r-a^{-(r-1)}}
\le
(4a)^r h^{\,r-a^{-(r-1)}}.
\]

Now take \(k\) copies of \(V(H)\) as the parts of a \(k\)-uniform hypergraph. Declare a tuple to be an edge when its entries are distinct and form a \(K_k\) in \(H\). A complete \(a\)-by-\(\cdots\)-by-\(a\) subhypergraph yields a \(K_k^{(a)}\) in \(H\): its vertex sets in different parts must be disjoint, and all cross-edges are present. Such a subhypergraph is impossible when \(H\) is \(F_0\)-free.

Applying (8) proves (7).

### A random-transversal consequence

Let \(Q\) have \(q\) vertices, and let \(Q^{(s)}\) be its balanced blow-up with classes of size \(s\). If \(J\subseteq Q^{(s)}\) is \(F_0\)-free, then
\[
\frac{e(J)}{s^2}
\le z_k(Q)+Cq^{k+2}s^{-\delta}.
\tag{11}
\]

Indeed, choose one uniformly random representative from each class. The resulting graph \(J'\) is a subgraph of \(Q\), and
\[
\mathbb E e(J')=\frac{e(J)}{s^2}.
\]
Every \(K_k\) in \(J\) uses distinct classes, so
\[
\Pr(J'\text{ contains }K_k)
\le\frac{N_{K_k}(J)}{s^k}.
\]
On the complementary event, \(e(J')\le z_k(Q)\); always \(e(J')\le\binom q2\). Thus (7) implies
\[
\frac{e(J)}{s^2}
\le
z_k(Q)+\binom q2\frac{N_{K_k}(J)}{s^k}
\le
z_k(Q)+Cq^{k+2}s^{-\delta}.
\]

This also applies to nonspanning \(J\). One first applies (7) on its actual vertex set and then adds isolated vertices for the random-transversal calculation; adding those vertices does not change its edges or \(K_k\)'s.

---

## 3. Symmetric edge gadgets for an arbitrary target

Put \(t=v(T)\ge2\), and fix an edge \(uv\in E(T)\).

Let \(Q\) be an auxiliary graph on \(q\ge2\) vertices. We construct an input graph with two kinds of vertices.

### Core vertices

For each \(i\in[q]\), make an independent class \(U_i\) of size \(s\). Their union is the core. Ultimately, the edges within the core will form \(Q^{(s)}\).

### Private gadget vertices

For **every ordered pair** \(i\ne j\), not merely for edges of \(Q\), and every
\[
w\in V(T)\setminus\{u,v\},
\]
make a private independent class \(V_{ij,w}\) of size \(M\).

For a fixed ordered pair \((i,j)\):

* join \(V_{ij,w}\) to \(V_{ij,w'}\) completely when \(ww'\in E(T)\);
* join \(V_{ij,w}\) to \(U_i\) completely when \(wu\in E(T)\);
* join \(V_{ij,w}\) to \(U_j\) completely when \(wv\in E(T)\).

There are no edges between private vertices belonging to different ordered pairs.

Let \(\mathsf B\) be this background graph, with **no core edges**. For any graph \(J\) on the core whose edges go between distinct core classes, write
\[
G(J)=\mathsf B\cup J.
\]
The actual input will be
\[
G=G(Q^{(s)}).
\]

The number of vertices is
\[
N=qs+(t-2)q(q-1)M.
\tag{12}
\]

### 3.1 All \(K_k\)'s lie in the core

Every clique containing a private vertex is contained in that vertex’s gadget together with its two root classes \(U_i,U_j\). The graph on those vertices is a subgraph of a blow-up of \(T\). Since \(\omega(T)<k\), it contains no \(K_k\).

Consequently,
\[
J\text{ is }K_k\text{-free}
\quad\Longrightarrow\quad
G(J)\text{ is }K_k\text{-free}.
\tag{13}
\]

### 3.2 Linearizing the number of \(T\)-copies

Set
\[
b=N_T(\mathsf B).
\]
Fix \(x\in U_1\) and \(y\in U_2\). Let \(c\) be the number of copies of \(T\) in \(\mathsf B+xy\) which:

1. use exactly two core vertices, namely \(x,y\);
2. include \(xy\) as an edge of the copy.

The use of every ordered pair in the construction makes the background symmetric under permutations of the core classes. It is also symmetric within each core class. Therefore the same \(c\) applies to every possible core edge between distinct classes.

Moreover,
\[
c\ge M^{t-2}.
\tag{14}
\]
To see this, map \(u\) to \(x\), \(v\) to \(y\), and choose one vertex from each private class of the gadget \((1,2)\). Different choices yield distinct vertex sets supporting copies that use \(xy\).

For every \(J\),
\[
N_T(G(J))=b+c\,e(J)+R(J),
\tag{15}
\]
where \(R(J)\ge0\) counts copies using at least one core edge and at least three core vertices.

Indeed:

* copies using no core edge are exactly the copies already in \(\mathsf B\);
* copies using core edges and exactly two core vertices contribute \(c\) for their unique core edge;
* all remaining copies contribute to \(R(J)\).

This classification uses ordinary, non-induced copies. Extra host edges not belonging to a particular copy do not affect it.

For \(t\ge3\), a simple embedding count gives
\[
R(J)\le \binom t3(qs)^3N^{t-3}.
\tag{16}
\]
Choose three target vertices whose images are in the core, then bound all remaining choices by \(N^{t-3}\). Counting labelled embeddings only enlarges the bound. For \(t=2\), \(R(J)=0\), \(b=0\), and \(c=1\).

Both \(b\) and \(c\) can be computed exactly in polynomial time: \(T\) is fixed, so enumerating its injective maps takes \(O(N^t)\) time.

---

## 4. Parameters and the approximation reduction

Fix \(\epsilon>0\), and put
\[
\eta=\min\{\epsilon,1\},
\qquad
d=\left\lceil\frac1\eta\right\rceil.
\]
Let
\[
A=q+(t-2)q(q-1).
\]
Choose
\[
L=
\begin{cases}
1,&t=2,\\[2mm]
1+16\binom t3q^3A^{t-3},&t\ge3.
\end{cases}
\tag{17}
\]
Then choose the integer
\[
s=
\max\left\{
(16Cq^{k+2})^{a^{k-1}},
\ (16A^tL^2)^d
\right\},
\qquad M=Ls.
\tag{18}
\]
All these quantities are polynomial in \(q\), since \(T,\mathcal F,k,\epsilon\) are fixed.

By (12),
\[
N\le ALs.
\]
Define the scale
\[
g=cs^2.
\]
Equation (14) implies
\[
g\ge L^{t-2}s^t.
\tag{19}
\]

The choices above give three useful bounds.

First, from (16), for \(t\ge3\),
\[
\frac{R(J)}g
\le
\frac{\binom t3q^3A^{t-3}}L
\le\frac1{16}.
\tag{20}
\]
This also holds for \(t=2\), because \(R(J)=0\).

Second, the first term in (18) ensures
\[
Cq^{k+2}s^{-\delta}\le\frac1{16}.
\tag{21}
\]

Third, since \(\eta\le\epsilon\), (19) gives
\[
\frac{N^{t-\epsilon}}g
\le
\frac{N^{t-\eta}}g
\le
A^{t-\eta}L^{2-\eta}s^{-\eta}
\le
A^tL^2s^{-\eta}
\le\frac1{16}.
\tag{22}
\]

### 4.1 Lower bound on the extremal value

Write
\[
z=z_k(Q).
\]
Take an optimal \(K_k\)-free subgraph \(J_0\subseteq Q\), and let
\[
J_*=J_0^{(s)}.
\]
Then \(J_*\) is \(K_k\)-free and has \(s^2z\) edges.

By (13), \(G(J_*)\) is \(K_k\)-free. Since every member of \(\mathcal F\) contains \(K_k\), it is also \(\mathcal F\)-free. Equation (15) therefore yields
\[
\operatorname{ex}(G,T,\mathcal F)\ge b+cs^2z=b+gz.
\tag{23}
\]

### 4.2 Upper bound on the extremal value

Let \(H\subseteq G\) be any \(\mathcal F\)-free subgraph, and let \(J\) be its core restriction. In particular, \(J\) is \(F_0\)-free. By (11) and (21),
\[
e(J)\le s^2\left(z+\frac1{16}\right).
\tag{24}
\]

Complete \(H\) by adding all missing background vertices and edges, obtaining \(G(J)\). This completion need not remain \(\mathcal F\)-free, and no such assertion is needed: monotonicity of non-induced copy counts gives
\[
N_T(H)\le N_T(G(J)).
\]
Using (15), (20), and (24),
\[
N_T(H)
\le
b+cs^2\left(z+\frac1{16}\right)+\frac g{16}
=
b+g\left(z+\frac18\right).
\]
Thus
\[
b+gz
\le
\operatorname{ex}(G,T,\mathcal F)
\le
b+g\left(z+\frac18\right).
\tag{25}
\]

This argument also covers nonspanning \(H\), including when forbidden graphs have isolated vertices: the clique-count estimate is applied before isolated vertices are added, and the completion is used only for an upper bound.

### 4.3 Recovering the exact NP-hard value

Suppose an approximation algorithm returns \(Z\) with
\[
\left|Z-\operatorname{ex}(G,T,\mathcal F)\right|
\le N^{t-\epsilon}.
\]
Equations (22) and (25) imply
\[
z-\frac1{16}
\le
\frac{Z-b}{g}
\le
z+\frac3{16}.
\]
Therefore rounding \((Z-b)/g\) to the nearest integer recovers \(z_k(Q)\) exactly.

The construction, computation of \(b,c\), and rounding are all polynomial-time. By Section 1, this would solve Vertex Cover in polynomial time.

Finally, the hard auxiliary graphs \(Q\) satisfy \(\omega(Q)\le k\). Their blow-ups have the same clique number, while every clique containing a private vertex lies in a blow-up of \(T\) and hence has size less than \(k\). Thus the constructed input satisfies
\[
\omega(G)\le k,
\]
proving the asserted \(K_{k+1}\)-free host restriction. This completes the proof of the partial theorem.

---

## 5. What remains unresolved

The theorem does **not** establish the full catalog conjecture.

Its essential additional assumption is that all forbidden graphs contain a common clique \(K_k\), while at least one forbidden graph is \(k\)-colorable. These two conditions play different roles:

* containing \(K_k\) makes every constructed \(K_k\)-free lower-bound graph feasible;
* \(k\)-colorability supplies the polynomial clique-count bound needed for the upper bound and amplification.

For forbidden graphs whose chromatic number exceeds their clique number, these mechanisms need not agree. For example, a \(K_3\)-free graph may still contain a forbidden odd cycle, so the lower-bound construction above is not automatically feasible.

The argument also deliberately avoids assuming an exact blow-up identity for a noncomplete target. Instead, the symmetric gadgets produce the identity
\[
N_T(G(J))=b+c\,e(J)+R(J),
\]
and the explicit parameter choices control \(R(J)\). This is what permits arbitrary targets in the proved subclass.

No claim of novelty or of a full resolution is made. The result is a self-contained positive partial result toward the conjecture, rather than the degenerate disproof claimed in the earlier attempt.