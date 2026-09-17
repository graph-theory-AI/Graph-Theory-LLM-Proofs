```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds when |V(G)| ≤ 2Δ(G), improving the supplied attempt’s order cutoff by one vertex.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved; no novelty is claimed, and the proof uses Gallai's classical critical-graph theorem."
}
```

# A strengthened small-order result

All graphs are finite and simple. Write \(\alpha(G)\) for the independence number and
\[
\tau(G)=|V(G)|-\alpha(G)
\]
for the minimum vertex-cover size.

The supplied attempt’s small-order argument checks out. Below I include its necessary ingredients and strengthen its clique-extension lemma to obtain the following.

**Theorem 1.** If \(G\) has maximum degree \(\Delta\ge 9\) and
\[
|V(G)|\le 2\Delta,
\]
then
\[
\chi(G)\le \max\{\Delta-1,\omega(G)\}.
\]

Consequently, every counterexample to Borodin–Kostochka has at least \(2\Delta+1\) vertices.

There is also an unrestricted-order vertex-cover consequence.

**Corollary 2.** If
\[
\Delta(G)\ge10,\qquad \omega(G)\le\Delta(G)-2,
\qquad \tau(G)\le2\Delta(G)-2,
\]
then \(G\) is \((\Delta(G)-1)\)-colorable.

These are restricted results, not a resolution of the conjecture.

## 1. Critical graphs and Gallai decomposition

A graph \(H\) is **\(k\)-vertex-critical** if
\[
\chi(H)=k,\qquad \chi(H-v)=k-1
\]
for every vertex \(v\). Such a graph has minimum degree at least \(k-1\). If it is noncomplete, it contains no \(K_k\).

The only nontrivial imported theorem is the following standard form of Gallai’s small-order critical-graph theorem:

> If a vertex-critical graph \(J\) has connected complement, then
> \[
> |V(J)|\ge2\chi(J)-1.
> \]

The vertex-critical formulation also follows from the usual critical-graph formulation by taking a spanning edge-minimal subgraph of the same chromatic number.

Let \(J\) be \(r\)-vertex-critical. The components of \(\overline J\) give a complete-join decomposition
\[
J=J_1\vee\cdots\vee J_m.
\]
Each \(J_i\) is vertex-critical. Put
\[
r_i=\chi(J_i),\qquad n_i=|V(J_i)|,\qquad t_i=n_i-r_i.
\]
Thus \(r=\sum_i r_i\).

If \(J_i\) is nonsingleton, then \(r_i\ge3\): the only 2-vertex-critical graph is \(K_2\), whose complement is disconnected. Gallai’s theorem therefore gives
\[
t_i\ge r_i-1\ge2. \tag{1}
\]

For \(v\in V(J_i)\),
\[
d_J(v)\ge r_i-1+\sum_{j\ne i}n_j
       =r-1+\sum_{j\ne i}t_j.
\]
Hence, if \(\Delta(J)\le r+s\), then
\[
\sum_{j\ne i}t_j\le s+1
\quad\text{for every }i. \tag{2}
\]

We need two consequences.

**Lemma 3.**
1. If \(J\) is noncomplete, \(r\)-vertex-critical, and \(\Delta(J)\le r\), then \(\overline J\) is connected and
   \[
   |V(J)|\ge2r-1.
   \]
2. If \(r\ge7\), \(J\) is \(r\)-vertex-critical,
   \[
   \Delta(J)\le r+1,\qquad |V(J)|\le2r-2,
   \]
   then
   \[
   J=K_r\quad\text{or}\quad J=K_{r-3}\vee C_5.
   \]

**Proof.**

For part 1, if the complement had at least two components, any nonsingleton component would have \(t_j\ge2\), contradicting (2) with \(s=0\). Thus all components would be singletons, making \(J\) complete.

For part 2, Gallai’s theorem forces at least two complement components. Equations (1)–(2) imply that every nonsingleton component has \(t_i=2\), \(r_i=3\), and \(n_i=5\). It is therefore \(C_5\), since the 3-vertex-critical graphs are precisely the chordless odd cycles.

If there are two nonsingleton components, there can be no other component, giving \(r=6\), contrary to the hypothesis. Thus there is at most one \(C_5\) component; the others are singletons. ∎

## 2. Counterexamples cannot have independence number two

We will use an elementary triangle-free minimum-degree bound, including its equality case.

**Lemma 4.** If a triangle-free graph \(F\) on \(N\) vertices is nonbipartite, then
\[
\delta(F)\le\frac{2N}{5}.
\]
If equality holds, \(F\) is a balanced blow-up of \(C_5\) by independent sets.

**Proof.**

Let \(C\) be a shortest odd cycle, of length \(\ell\ge5\). It is chordless.

Every vertex outside \(C\) has at most two neighbors on \(C\). Indeed, if it had at least three, the cyclic gaps between consecutive neighbors would all have length at least two. Some gap would be odd, and its length would be at most \(\ell-4\); together with the outside vertex, it would form a shorter odd cycle.

Therefore
\[
\ell\delta(F)
 \le \sum_{u\in V(C)}d_F(u)
 =\sum_{v\in V(F)}|N_F(v)\cap V(C)|
 \le2N.
\]
This proves the bound.

If \(\delta(F)=2N/5\), equality forces \(\ell=5\) and every vertex to have exactly two neighbors on \(C\). Label \(C\) cyclically by \(c_0,\dots,c_4\), and put
\[
B_i=\{v:N_F(v)\cap V(C)=\{c_{i-1},c_{i+1}\}\}.
\]
These sets partition \(V(F)\), and \(c_i\in B_i\). Triangle-freeness permits edges only between consecutive parts.

Writing \(b_i=|B_i|\), we have
\[
b_{i-1}+b_{i+1}\ge\delta(F).
\]
Summing yields equality throughout, since \(2N=5\delta(F)\). The five cyclic equations force \(b_i=N/5\) for every \(i\). The degree condition then forces every edge between consecutive parts to be present. ∎

**Lemma 5.** Let \(k\ge8\), and let \(H\) be noncomplete and \(k\)-vertex-critical with \(\Delta(H)\le k\). If \(\alpha(H)\le2\), then
\[
k=8,\qquad H\cong C_5[K_3].
\]

**Proof.**

Put \(n=|V(H)|\). By Lemma 3,
\[
n\ge2k-1.
\]
The complement \(F=\overline H\) is triangle-free and
\[
\delta(F)\ge n-k-1.
\]
It cannot be bipartite: a bipartition would have a part of size at least \(k\), producing a \(K_k\) in \(H\).

Lemma 4 gives
\[
n-k-1\le\frac{2n}{5},
\qquad\text{so}\qquad
n\le\frac{5(k+1)}3.
\]
Together with \(n\ge2k-1\), this implies \(k\le8\). Thus \(k=8\), \(n=15\), and equality holds in Lemma 4. Since \(C_5\) is self-complementary, \(H\cong C_5[K_3]\). ∎

In particular, every noncomplete critical graph relevant to Borodin–Kostochka has independence number at least three.

## 3. Extending a coloring across a large clique

The following is the main improvement over the supplied attempt.

**Lemma 6 — clique extension.** Let \(J\) satisfy
\[
\Delta(J)\le q+1,\qquad \omega(J)\le q,
\]
and suppose \(J\) contains a clique \(Q\) of order \(q\). Then \(J\) is \(q\)-colorable in either of these situations:
1. \(q\ge7\) and \(|V(J)|\le2q+1\);
2. \(q\ge8\) and \(|V(J)|\le2q+2\).

### Common setup

Pad with isolated vertices to reach the asserted order, and put \(R=V(J)\setminus Q\). For \(x\in R\), define
\[
A_x=N_J(x)\cap Q,\qquad a_x=|A_x|,
\qquad F=\overline{J[R]}.
\]
Every vertex of \(Q\) has at most two neighbors in \(R\). Consequently,
\[
\sum_{x\in R}a_x\le2q, \tag{3}
\]
and every element of \(Q\) belongs to at most two sets \(A_x\). Also \(A_x\ne Q\), since otherwise \(Q\cup\{x\}\) would be a \(K_{q+1}\).

Call \(x\) **heavy** if \(a_x=q-1\). There are at most two heavy vertices, and each has at most two neighbors in \(J[R]\).

Suppose \(R\) is partitioned into \(q\) independent color classes. For a class \(D\), let
\[
B_D=\bigcup_{x\in D}A_x.
\]
This is exactly the set of vertices of \(Q\) at which the color of \(D\) is forbidden.

Each vertex of \(Q\) has at least \(q-2\) available colors. Hall’s theorem therefore gives an extension to \(Q\) provided that
\[
B_D\ne Q\quad\text{for every class }D, \tag{4}
\]
and
\[
|B_D\cap B_E|\le q-2\quad\text{for distinct classes }D,E. \tag{5}
\]
Indeed, subsets of \(Q\) of size at most \(q-2\) satisfy Hall automatically; failure on \(q-1\) vertices requires two colors forbidden throughout that set, and failure on all \(q\) vertices requires one color forbidden everywhere.

### Proof of part 1: one merger

Here \(|R|=q+1\), and the degree bound gives
\[
a_x\le d_F(x)+1. \tag{6}
\]
We merge one nonadjacent pair in \(J[R]\), leaving all other vertices singleton color classes.

If there are no heavy vertices, it suffices to find an edge \(xy\in E(F)\) with \(A_x\cup A_y\ne Q\).

Suppose every edge of \(F\) covers \(Q\) in this way. For each \(z\in Q\), the set \(N_J(z)\cap R\) is then a vertex cover of \(F\) of size at most two. A vertex of \(F\) of degree at least three would belong to every such cover and hence be adjacent in \(J\) to all of \(Q\), impossible. Thus \(\Delta(F)\le2\), and (6) gives \(a_x\le3\). But \(F\) has an edge, since \(|R|=q+1>\omega(J)\), and its endpoint labels cannot cover \(Q\), because \(6<q\). This is a contradiction.

The heavy cases are as follows.

- **One heavy vertex \(r\), missing \(a\in Q\).** Choose \(t\in R\setminus\{r\}\) adjacent to neither \(r\) nor \(a\). At most four candidates are excluded. Merge \(r,t\). Its label union misses \(a\), and no singleton heavy vertex remains.
- **Two heavy vertices with the same label \(Q\setminus\{a\}\).** They are nonadjacent, since otherwise they and their common neighbors form a \(K_{q+1}\). Merge them.
- **Two heavy vertices \(r,s\), missing distinct vertices \(a,b\).** Choose \(t\notin\{r,s\}\) adjacent to neither \(r\) nor \(a\), and merge \(r,t\). There are at most three excluded candidates: \(r\) has at most two neighbors in \(R\), and \(a\), already adjacent to \(s\), has at most one other neighbor there. The merged label misses \(a\), whereas \(A_s\) contains \(a\).

In each case (4)–(5) hold.

### Proof of part 2: two mergers

Now \(|R|=q+2\), and the stronger degree relation is
\[
a_x\le d_F(x). \tag{7}
\]
We will use either two independent pairs or one independent triple.

#### Two heavy vertices with different labels

Let their labels be \(Q\setminus\{a\}\) and \(Q\setminus\{b\}\), where \(a\ne b\).

Choose distinct \(x,y\in R\setminus\{r,s\}\) such that \(x\) is adjacent to neither \(r\) nor \(a\), and \(y\) is adjacent to neither \(s\) nor \(b\). Each choice has at least \(q-3\) candidates.

Merge \(r,x\) and \(s,y\). Their label unions are the two different \((q-1)\)-subsets of \(Q\), so (4)–(5) hold.

#### Two heavy vertices with the same label

Write the common label as \(A=Q\setminus\{a\}\). As above, \(r,s\) are nonadjacent.

Among the \(q\) other vertices of \(R\), choose \(x\) adjacent to none of \(r,s,a\). At most six candidates are excluded, and \(q\ge8\). The independent triple \(\{r,s,x\}\) has label union \(A\). All other classes are nonheavy singletons, so (4)–(5) hold.

#### Exactly one heavy vertex

Let \(r\) be heavy, with \(A_r=Q\setminus\{a\}\), and put \(F_0=F-r\).

We claim that \(F_0\) has an edge \(uv\) satisfying
\[
A_r\not\subseteq A_u\cup A_v. \tag{8}
\]
First, \(F_0\) has an edge, because \(J[R\setminus\{r\}]\) cannot be a \(K_{q+1}\).

Suppose every edge of \(F_0\) covers \(A_r\). For each \(z\in A_r\), the set
\[
N_J(z)\cap(R\setminus\{r\})
\]
is a vertex cover of \(F_0\) of size at most one, since \(z\) is already adjacent to \(r\).

If \(F_0\) has at least two edges, their common intersection must consequently be one vertex \(w\), and every \(z\in A_r\) is adjacent to \(w\). Thus \(A_w=A_r\), contradicting uniqueness of the heavy vertex.

If \(F_0\) has exactly one edge \(uv\), then \(d_F(u),d_F(v)\le2\), so (7) gives
\[
|A_u\cup A_v|\le4<q-1.
\]
This is also a contradiction, proving (8).

Choose \(x\notin\{r,u,v\}\) adjacent to neither \(r\) nor \(a\). Before excluding \(u,v\), there are at least \(q-3\) candidates. Merge \(r,x\) and \(u,v\). The first label union is \(A_r\), and the second misses some element of \(A_r\). Thus (4)–(5) hold.

#### No heavy vertices

Here
\[
a_x\le q-2\quad\text{for every }x\in R. \tag{9}
\]

If \(F\) has no matching of size two, its edges either all have a common endpoint or form a triangle. The first possibility gives an independent set of size \(q+1\) in \(F\), contrary to \(\omega(J)\le q\). Thus \(F\) is a triangle together with isolated vertices. By (7), the triangle’s label union has size at most six. Merge its three vertices. Conditions (4)–(5) follow.

Assume now that \(F\) has a matching of size two. Call an edge \(xy\) **light** if
\[
|A_x\cup A_y|\le q-2.
\]

**Claim.** Some light edge belongs to a matching of size two.

Suppose not, and choose a matching whose four endpoints form \(U\). Its two edges each have label union of size at least \(q-1\), so
\[
\sum_{u\in U}a_u\ge2q-2.
\]
By (3), the vertices in \(W=R\setminus U\) have total label size at most two.

No edge can join \(U\) to a zero-label vertex of \(W\): by (9), it would be a light edge belonging to a matching of size two.

Let \(p\le2\) be the number of positive-label vertices in \(W\). For \(u\in U\), (7) now gives
\[
a_u\le3+p.
\]
For a positive-label vertex \(w\in W\), we have \(a_w\le3-p\). Hence
\[
|A_u\cup A_w|\le6\le q-2.
\]
So an edge from \(U\) to such a \(w\) would again be light and extendible to a matching of size two.

There are therefore no edges between \(U\) and \(W\). Equation (7) gives \(a_u\le3\) for all \(u\in U\), contradicting
\[
\sum_{u\in U}a_u\ge2q-2\ge14.
\]
This proves the claim.

Choose a light edge \(uv\) belonging to a matching of size two, and let \(F'=F-\{u,v\}\). If \(F'\) has an edge \(xy\) with \(A_x\cup A_y\ne Q\), use the pairs \(u,v\) and \(x,y\). One merged label has size at most \(q-2\), and the other is proper, so (4)–(5) hold.

It remains to handle the possibility that every edge of \(F'\) covers \(Q\). As in part 1, the sets \(N_J(z)\cap V(F')\), for \(z\in Q\), are vertex covers of \(F'\) of size at most two. Thus \(\Delta(F')\le2\). Equation (7) gives \(a_x\le4\) for every vertex incident with an edge of \(F'\). An edge covering \(Q\) is therefore impossible when \(q\ge9\).

For \(q=8\), each endpoint of each edge of \(F'\) has label size four, degree two in \(F'\), and is adjacent in \(F\) to both \(u,v\). The nonisolated part of \(F'\) is consequently a union of cycles on at most four vertices, by (3). Adjacent labels are disjoint 4-sets, so a triangle is impossible. Hence this part is \(C_4\).

Its four labels already have total size \(16=2q\), forcing \(A_u=A_v=\varnothing\). Choose two distinct cycle vertices \(x,y\), and instead use the pairs \(u,x\) and \(v,y\). Both label unions have size four, so (4)–(5) hold.

This completes both parts of the clique-extension lemma. ∎

## 4. The short-order critical classification

We first record the other reducible configuration used in the supplied attempt.

**Lemma 7.** Let \(k\ge7\), and let \(\Delta(J)\le k\). If \(J\) contains an induced subgraph
\[
X=K_{k-4}\vee C_5,
\]
then every \((k-1)\)-coloring of \(J-X\) extends to \(J\).

**Proof.**

Each vertex of the clique already has degree \(k\) inside \(X\), so it has no outside neighbor. Each cycle vertex has at most two outside neighbors and hence at least \(k-3\) available colors.

Partition the cycle into two independent pairs and one singleton. Each pair has at least
\[
(k-1)-4=k-5\ge2
\]
common available colors. Give the two pairs distinct colors, then give the singleton a third available color. The clique uses the remaining \(k-4\) colors. ∎

**Proposition 8.** Let \(k\ge8\), and suppose \(H\) is \(k\)-vertex-critical with
\[
\Delta(H)\le k,\qquad |V(H)|\le2k-1.
\]
Then
\[
H=K_k,
\]
unless \(k=8\) and \(H\cong C_5[K_3]\).

**Proof.**

Suppose \(H\ne K_k\). Lemma 3 gives \(|V(H)|=2k-1\). If \(\alpha(H)\le2\), Lemma 5 applies.

Otherwise choose an independent triple \(T\). Criticality and the ability to color \(T\) with one new color give
\[
\chi(H-T)=k-1.
\]
Choose an induced \((k-1)\)-vertex-critical subgraph \(X\subseteq H-T\). With \(r=k-1\),
\[
|V(X)|\le2r-2,\qquad \Delta(X)\le r+1.
\]
Lemma 3 gives
\[
X=K_{k-1}\quad\text{or}\quad X=K_{k-4}\vee C_5.
\]

In the first case, Lemma 6(1) makes \(H\) \((k-1)\)-colorable. In the second, criticality supplies a \((k-1)\)-coloring of \(H-X\), which Lemma 7 extends. Both are contradictions. ∎

## 5. Excluding order \(2k\)

We can now prove the strengthened critical-graph statement.

**Theorem 9.** Let \(k\ge9\), and suppose \(H\) is \(k\)-vertex-critical with
\[
\Delta(H)\le k,\qquad |V(H)|\le2k.
\]
Then \(H=K_k\).

**Proof.**

Suppose \(H\ne K_k\). By Lemma 5, \(\alpha(H)\ge3\). Extend an independent triple to a maximal independent set \(I\).

Every vertex outside \(I\) has a neighbor in \(I\). Therefore
\[
\Delta(H-I)\le k-1.
\]
Also
\[
\chi(H-I)=k-1,\qquad |V(H-I)|\le2k-3.
\]
Choose an induced \((k-1)\)-vertex-critical subgraph \(X\subseteq H-I\). Proposition 8, applied with \(r=k-1\), gives two possibilities.

### Case 1: \(X=K_{k-1}\)

Apply Lemma 6(2) to \(H\), with \(q=k-1\). Its hypotheses hold because
\[
q\ge8,\qquad |V(H)|\le2q+2,\qquad
\Delta(H)\le q+1,\qquad \omega(H)\le q.
\]
Thus \(H\) is \((k-1)\)-colorable, a contradiction.

### Case 2: \(k=9\) and \(X=C_5[K_3]\)

Here \(|V(X)|=15\), while \(|V(H)|\le18\) and \(|I|\ge3\). Hence
\[
H-I=X,\qquad |I|=3,\qquad |V(H)|=18.
\]

Every vertex of \(X\) has degree eight inside \(X\), so at most one neighbor in \(I\). Thus there are at most 15 edges between \(I\) and \(X\).

On the other hand, criticality gives \(\delta(H)\ge8\), and \(I\) is independent. The three vertices of \(I\) therefore send at least 24 edges to \(X\), a contradiction. ∎

### Deduction of Theorem 1

Suppose \(G\) violates the desired inequality, and put \(k=\chi(G)\). Then
\[
k\ge\Delta,\qquad k>\omega(G).
\]
Choose an induced \(k\)-vertex-critical subgraph \(H\). It is noncomplete and satisfies
\[
\Delta(H)\le\Delta\le k,\qquad
|V(H)|\le2\Delta\le2k.
\]
Since \(k\ge9\), Theorem 9 gives a contradiction.

### Proof of the vertex-cover corollary

Suppose the hypotheses of Corollary 2 hold but \(\chi(G)=k\ge\Delta\). Choose an induced \(k\)-vertex-critical subgraph \(H\), and let \(I\) be a maximum independent set in \(H\).

Vertex-cover number does not increase under taking induced subgraphs, so
\[
|V(H-I)|=\tau(H)\le\tau(G)\le2\Delta-2\le2(k-1).
\]
Maximality of \(I\) gives \(\Delta(H-I)\le k-1\), and criticality gives \(\chi(H-I)=k-1\).

An induced \((k-1)\)-vertex-critical subgraph of \(H-I\) is therefore \(K_{k-1}\), by Theorem 9, since \(k-1\ge9\). But then
\[
\omega(G)\ge k-1\ge\Delta-1,
\]
contrary to the hypothesis. ∎

## 6. What remains unresolved

The argument proves the conjecture through order \(2\Delta\), and Lemma 5 also proves it for all graphs with independence number at most two, without an order restriction.

It does **not** eliminate larger critical counterexamples. At order \(2k+1\), a \((k-1)\)-clique can have \(k+2\) vertices outside it: the clique-extension construction must then save three colors rather than the two controlled above. For the \(k=9\) reduction, 8-critical graphs on 16 vertices also enter, beyond Proposition 8.

Those cases are not settled here. No claim of novelty or of a new general degree threshold is made, and none of the catalog’s unverified recent literature claims is used.