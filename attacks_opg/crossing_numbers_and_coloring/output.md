```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture for triangle-free graphs and for graphs whose vertex-cover number is at most their chromatic number, but not for arbitrary graphs.",
  "would_publish": false,
  "caveats": "These are self-contained special-case arguments; novelty is not claimed, and the unrestricted conjecture remains unresolved."
}
```

# Two rigorous special cases

All graphs below are finite and simple. Write \(\tau(G)\) for the minimum size of a vertex cover.

The partial results are:

**Proposition 1.** Every triangle-free graph satisfies Albertson’s conjecture. More quantitatively, if \(G\) is triangle-free and \(k=\chi(G)\ge 7\), then
\[
\boxed{\operatorname{cr}(G)\ge
\frac{(k-1)^4(k+2)}{432}.}
\]

**Proposition 2.** If \(k=\chi(G)\) and \(\tau(G)\le k\), then \(G\) contains a subdivision of \(K_k\). Consequently, \(G\) satisfies Albertson’s conjecture.

These statements concern unbounded chromatic number, but are not offered as new results in the literature.

It suffices throughout to compare \(G\) with \(K_k\), where \(k=\chi(G)\): if \(t\le k\), then
\[
\operatorname{cr}(K_t)\le \operatorname{cr}(K_k).
\]

## 1. An elementary upper bound for complete graphs

We will only need
\[
\operatorname{cr}(K_k)\le \frac12\binom{k}{4}.
\tag{1}
\]

Here is a drawing argument. Place the vertices on the common boundary of two disks glued together to form a sphere. Independently assign each edge to either disk with probability \(1/2\), and draw edges within each disk as chords.

A pair of edges can cross precisely when their four endpoints alternate around the boundary and the edges receive the same disk. Every four-element vertex set contributes exactly one alternating pair, whose probability of crossing is \(1/2\). After a generic perturbation, the expected number of crossings is therefore \(\frac12\binom{k}{4}\). Some assignment attains at most this expectation. Removing a point of the sphere outside the drawing gives a plane drawing with the same crossings.

In particular, for \(k\ge4\),
\[
\operatorname{cr}(K_k)
\le \frac{k(k-1)(k-2)(k-3)}{48}
\le \frac{(k-1)^4}{48}.
\tag{2}
\]

No formula for the exact crossing number of \(K_k\) is being assumed.

## 2. Triangle-free graphs

### 2.1. A chromatic lower bound on the order

**Lemma 1.** If \(G\) is triangle-free and \(\chi(G)=k\ge2\), then
\[
|V(G)|\ge \frac{(k-1)(k+2)}2.
\tag{3}
\]

**Proof.** Induct on \(k\). For \(k=2\), at least two vertices are necessary.

For \(k\ge3\), choose a vertex-critical \(k\)-chromatic subgraph \(H\subseteq G\). Thus
\[
\delta(H)\ge k-1,
\]
and every proper induced subgraph of \(H\) is \((k-1)\)-colorable.

Fix \(v\in V(H)\). Since \(H\) is triangle-free, \(N_H(v)\) is independent. We claim that
\[
\chi\bigl(H-N_H[v]\bigr)=k-1.
\]
The upper bound follows from criticality. For the lower bound, suppose the remaining graph had a coloring with \(k-2\) colors. Give all vertices of \(N_H(v)\) one new color, and give \(v\) any of the original \(k-2\) colors. This would be a \((k-1)\)-coloring of \(H\), a contradiction.

Since \(|N_H[v]|\ge k\), induction gives
\[
|V(G)|\ge |V(H)|
\ge k+\frac{(k-2)(k+1)}2
=\frac{(k-1)(k+2)}2.
\]
\(\square\)

### 2.2. A triangle-free crossing inequality

For any drawing of a triangle-free graph with \(n\ge3\) vertices, \(m\) edges, and \(x\) crossings,
\[
x\ge m-2n+4.
\tag{4}
\]
Indeed, deleting at most one edge per crossing produces a planar triangle-free graph, which has at most \(2n-4\) edges.

The weakened inequality
\[
x\ge m-2n
\tag{5}
\]
holds for every order, including \(n=0,1,2\). This uniform version is convenient for random sampling.

**Lemma 2.** If \(G\) is triangle-free, with \(n>0\) vertices and \(m\ge3n\) edges, then
\[
\operatorname{cr}(G)\ge \frac{m^3}{27n^2}.
\tag{6}
\]

**Proof.** Take an optimal drawing in which adjacent edges do not cross; the usual local uncrossing operation permits this. Every crossing therefore involves four distinct endpoints.

Retain each vertex independently with probability \(p\), and inherit the drawing on the retained vertices. Its expected numbers of vertices, edges, and crossings are respectively
\[
pn,\qquad p^2m,\qquad p^4\operatorname{cr}(G).
\]
Applying (5) to every sampled drawing and taking expectations gives
\[
p^4\operatorname{cr}(G)\ge p^2m-2pn.
\]
Choose \(p=3n/m\le1\). Then
\[
\operatorname{cr}(G)
\ge \frac{m}{p^2}-\frac{2n}{p^3}
=\frac{m^3}{27n^2}.
\]
\(\square\)

### 2.3. Proof of Proposition 1

Let \(H\subseteq G\) be vertex-critical with \(\chi(H)=k\), and put
\[
n=|V(H)|,\qquad m=|E(H)|.
\]
Criticality and Lemma 1 give
\[
m\ge \frac{(k-1)n}{2},
\qquad
n\ge \frac{(k-1)(k+2)}2.
\tag{7}
\]

If \(k\ge7\), then \(m\ge3n\). Hence Lemma 2 implies
\[
\begin{aligned}
\operatorname{cr}(G)
&\ge \operatorname{cr}(H)\\
&\ge \frac{m^3}{27n^2}\\
&\ge \frac{(k-1)^3n}{216}\\
&\ge \frac{(k-1)^4(k+2)}{432}.
\end{aligned}
\tag{8}
\]
Since \(k+2\ge9\), equations (2) and (8) yield
\[
\operatorname{cr}(G)
\ge \frac{(k-1)^4}{48}
\ge \operatorname{cr}(K_k).
\]

It remains to cover smaller \(k\).

- **\(k\le4\):** \(K_k\) is planar, so the assertion is immediate.
- **\(k=5\):** We have \(m\ge2n\), and (4) gives
  \[
  \operatorname{cr}(G)\ge4>
  \frac12\binom54\ge\operatorname{cr}(K_5).
  \]
- **\(k=6\):** Lemma 1 gives \(n\ge20\), while \(m\ge5n/2\). Thus
  \[
  \operatorname{cr}(G)\ge \frac n2+4\ge14>
  \frac12\binom64\ge\operatorname{cr}(K_6).
  \]

This proves Proposition 1 for every chromatic number. \(\square\)

## 3. Graphs with a small vertex cover

We now prove the stronger, topological conclusion in Proposition 2.

The cases \(k\le2\) are immediate, so assume \(k\ge3\). Choose a vertex cover \(S\) with \(|S|\le k\), and let
\[
I=V(G)\setminus S.
\]
The set \(I\) is independent. Consequently,
\[
k=\chi(G)\le \chi(G[S])+1,
\]
so \(\chi(G[S])\ge k-1\).

### Case 1: \(|S|=k-1\)

Then \(S\) is a clique. If no vertex of \(I\) is adjacent to all of \(S\), color \(S\) with \(k-1\) distinct colors and give each vertex of \(I\) the color of one of its nonneighbors in \(S\). Independence of \(I\) makes this a valid \((k-1)\)-coloring of \(G\), a contradiction.

Thus some vertex of \(I\), together with \(S\), forms a \(K_k\).

The possibility \(|S|<k-1\) is excluded by \(\chi(G[S])\ge k-1\).

### Case 2: \(|S|=k\)

If \(\chi(G[S])=k\), then \(G[S]=K_k\), and we are done. We may therefore assume
\[
\chi(G[S])=k-1.
\tag{9}
\]

Consider the complement \(F=\overline{G[S]}\). It is nonempty. It contains neither:

- two vertex-disjoint edges, since their endpoints could be paired into two color classes, giving a \((k-2)\)-coloring of \(G[S]\); nor
- a triangle, since its three vertices could be placed in one color class, again saving two colors.

A nonempty graph with neither two disjoint edges nor a triangle is a star together with isolated vertices. To see this, if two edges are \(va\) and \(vb\), every edge not containing \(v\) would have to be \(ab\), which would create a triangle.

It follows that there is a vertex \(v\in S\) such that
\[
Q=S\setminus\{v\}
\]
is a \((k-1)\)-clique. Let
\[
A=Q\setminus N_G(v).
\]
The set \(A\) is nonempty.

If some vertex of \(I\) is adjacent to all of \(Q\), we already have a \(K_k\). Assume no such vertex exists.

For each \(a\in A\), give the vertices of \(Q\) distinct colors and give \(v\) the color of \(a\). This is a proper \((k-1)\)-coloring of \(G[S]\). It cannot extend to \(G\). Since \(I\) is independent, some vertex \(w_a\in I\) must have neighbors in every color class.

Our assumption that no vertex of \(I\) is complete to \(Q\) now forces
\[
N_G(w_a)\cap Q=Q\setminus\{a\},
\qquad
vw_a\in E(G).
\tag{10}
\]
Indeed, missing any vertex of \(Q\setminus\{a\}\) would leave its singleton color available; and, because \(w_a\) misses \(a\), it must be adjacent to \(v\) to block their shared color.

The vertices \(w_a\), for \(a\in A\), are distinct, because they have different unique nonneighbors in \(Q\).

If \(|A|=1\), say \(A=\{a\}\), then
\[
(Q\setminus\{a\})\cup\{v,w_a\}
\]
is a \(K_k\).

Finally, suppose \(|A|\ge2\). Choose a permutation \(\sigma\) of \(A\) with no fixed point, for example a cyclic shift. Take \(Q\cup\{v\}\) as the branch vertices of a subdivision of \(K_k\):

- retain all edges within \(Q\);
- retain the edges from \(v\) to \(Q\setminus A\);
- for each \(a\in A\), replace the missing edge \(va\) by
  \[
  v\,w_{\sigma(a)}\,a.
  \]

These are valid paths by (10) and \(\sigma(a)\ne a\). Their internal vertices are distinct and lie outside the branch set. They therefore form the required subdivision.

Crossing number cannot increase under taking subgraphs or suppressing subdivision vertices. Hence
\[
\operatorname{cr}(G)\ge\operatorname{cr}(K_k),
\]
proving Proposition 2. \(\square\)

## 4. What remains unresolved

These arguments imply that any counterexample must satisfy both
\[
G\text{ contains a triangle},
\qquad
\tau(G)\ge \chi(G)+1.
\]

The two mechanisms are different:

- Triangle-freeness forces a critical graph of chromatic number \(k\) to have quadratically many vertices. The crossing inequality then gives a lower bound of order \(k^5\), comfortably exceeding the order-\(k^4\) complete-graph benchmark.
- A vertex cover of size at most \(k\) forces a particularly rigid coloring obstruction, from which a complete-graph subdivision can be constructed.

Neither mechanism handles general critical graphs with triangles and larger vertex covers. Thus this does **not** extend the verified range for arbitrary graphs, and it does not settle Albertson’s conjecture.