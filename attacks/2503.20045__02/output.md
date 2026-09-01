```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any affirmative H must have zero undirected chromatic threshold and a source-forest grading; an explicit acyclic orientation of K_{3,3} fails, while every strictly leveled digraph is affirmative.",
  "would_publish": false,
  "caveats": "Assumes χ(D) is the chromatic number of the underlying graph; sufficiency and literature novelty are unresolved."
}
```

# Mathematical writeup

## 1. Definitions and statement of the partial result

Write \(U(D)\) for the simple underlying graph of a digraph \(D\), and interpret
\[
\chi(D)=\chi(U(D)).
\]
Containment is non-induced subdigraph containment.

Call a fixed digraph \(H\) **affirmative** if for every \(\varepsilon>0\) there is \(c_\varepsilon\) such that every \(n\)-vertex digraph \(D\) with
\[
\chi(D)\ge c_\varepsilon,\qquad \delta^+(D)\ge \varepsilon n
\]
contains \(H\).

We obtain the following partial classification.

### Partial theorem

1. If \(H\) is affirmative, then every weak component \(Q\) of \(H\) has a **source-forest grading**: there are \(S\subseteq V(Q)\) and a map
   \[
   \ell:V(Q)\longrightarrow \mathbb Z_{\ge 0}
   \]
   such that:
   - \(\ell^{-1}(0)=S\), possibly with \(S=\varnothing\);
   - \(Q[S]\) is an orientation of a forest;
   - for every arc \(u\to v\) not having both ends in \(S\),
     \[
     \ell(v)=\ell(u)+1.
     \]

   Consequently, every affirmative \(H\) is acyclic.

2. If \(H\) is affirmative, then \(U(H)\) has zero undirected chromatic threshold. By the known classification of undirected chromatic thresholds, this implies that \(U(H)\) is either bipartite or is a near-acyclic \(3\)-chromatic graph.

3. For every \(r\ge3\), a particular acyclic orientation \(H_r\) of \(K_{r,r}\), defined below, is not affirmative. Thus being acyclic with bipartite underlying graph is not sufficient.

4. Every **strictly leveled** digraph \(H\), meaning that there is \(g:V(H)\to\mathbb Z\) such that
   \[
   g(v)=g(u)+1\qquad\text{for every arc }u\to v,
   \]
   is affirmative. In fact, for every \(\varepsilon>0\), all sufficiently large digraphs with minimum out-degree at least \(\varepsilon n\) contain \(H\), without any chromatic-number hypothesis.

The first and third assertions are the main orientation-specific negative results.

---

## 2. A high-girth blow-up obstruction

We use the classical fact that for every \(g,M\) there exists a graph of girth greater than \(g\) and chromatic number greater than \(M\). For completeness, this follows by taking \(G(N,p)\) with
\[
p=N^{-1+1/(2g)}:
\]
the expected number of cycles of length at most \(g\) is \(O(N^{1/2})\), while with high probability there is no independent set of linear size. Deleting one vertex from every short cycle leaves a graph of the required type.

### Proposition 2.1

If a weakly connected digraph \(Q\) is affirmative, then \(Q\) has a source-forest grading.

#### Proof

Let \(h=|V(Q)|\). Define a finite oriented graph \(F\) consisting of

- a directed path
  \[
  p_0\to p_1\to\cdots\to p_h\to c_0,
  \]
- followed by a directed cycle
  \[
  c_0\to c_1\to\cdots\to c_h\to c_0.
  \]

Thus every vertex of \(F\) has out-degree at least one, while \(p_0\) has in-degree zero.

Choose a graph \(G\) of girth greater than \(h\) and arbitrarily large chromatic number, and orient its edges according to a total ordering. Construct \(D=D(F,G)\) as follows.

- Replace \(p_0\) by a copy \(V_{p_0}\) of the oriented graph \(G\).
- Replace every other vertex \(x\in V(F)\setminus\{p_0\}\) by an independent set \(V_x\) of size \(|V(G)|\).
- For every arc \(x\to y\) of \(F\), add all arcs from \(V_x\) to \(V_y\).
- Add no other arcs.

If \(q=|V(F)|=2h+2\) and \(m=|V(G)|\), then
\[
|V(D)|=qm,\qquad \delta^+(D)\ge m=\frac{|V(D)|}{q},
\]
and
\[
\chi(D)\ge \chi(G).
\]
The host \(D\) is an oriented graph, so it satisfies even the stronger prohibition on antiparallel arcs.

Since \(Q\) is affirmative, choosing \(\chi(G)\) sufficiently large forces an embedding of \(Q\) in \(D\). Project this embedding to a map
\[
\phi:V(Q)\to V(F).
\]

There are two cases.

### Case 1: the image avoids \(p_0\)

Every part other than \(V_{p_0}\) is independent. Hence every arc of \(Q\) projects to an arc of \(F\); no arc has both ends in one part.

We claim that there is \(g:V(Q)\to\mathbb Z\) satisfying
\[
g(v)=g(u)+1
\]
for every arc \(u\to v\).

Indeed, these equations are consistent around every undirected cycle of \(U(Q)\). The directed-path edges of \(F\) are bridges in \(U(F)\), so a projected closed walk has net contribution zero on them. Its possible winding around the directed \((h+1)\)-cycle is a multiple of \(h+1\). On the other hand, a simple cycle of \(U(Q)\) has length at most \(h\), so the absolute value of the corresponding signed sum is at most \(h\). It must therefore be zero. Integrating the equations along a spanning tree gives \(g\). After translating \(g\), all levels may be taken positive, and we use \(S=\varnothing\).

### Case 2: the image uses \(p_0\)

Put
\[
S=\phi^{-1}(p_0).
\]
Because \(Q\) is weakly connected and has \(h\) vertices, every projected vertex has undirected distance at most \(h-1\) from \(p_0\). But the distance from \(p_0\) to \(c_0\) in \(U(F)\) is \(h+1\). Hence the image of \(Q\) lies entirely on the path \(p_0,p_1,\dots,p_h\).

Set
\[
\ell(v)=j\quad\text{if }\phi(v)=p_j.
\]
Every arc not internal to \(S\) then goes from level \(j\) to level \(j+1\). Moreover, \(Q[S]\) embeds into the oriented graph \(G\). Since \(G\) has girth greater than \(h\), the underlying graph of \(Q[S]\) contains no cycle; and since \(G\) is oriented, \(Q[S]\) has no antiparallel pair. Thus \(Q[S]\) is an orientation of a forest.

This is the required source-forest grading. ∎

### Corollary 2.2

Every affirmative \(H\) is acyclic.

#### Proof

The property of being affirmative is inherited by subdigraphs, so Proposition 2.1 applies to every weak component.

In a source-forest grading, every arc outside the level-zero forest strictly increases the level. Thus a directed cycle would have to lie entirely in the level-zero part, which is an oriented forest and therefore has no directed cycle. ∎

This also rules out loops, antiparallel pairs, and every fixed consistently directed cycle.

---

## 3. Reduction to the undirected chromatic-threshold problem

Let \(J\) be a fixed undirected graph. Say that \(J\) has **zero undirected chromatic threshold** if for every \(\eta>0\) there is \(C_\eta\) such that every \(J\)-free graph \(G\) satisfying
\[
\delta(G)\ge \eta |V(G)|
\]
has \(\chi(G)\le C_\eta\).

### Proposition 3.1

If \(H\) is affirmative, then \(U(H)\) has zero undirected chromatic threshold.

#### Proof

Suppose otherwise. Then for some \(\eta>0\) there are \(U(H)\)-free graphs \(G_t\) with
\[
\delta(G_t)\ge \eta |V(G_t)|,\qquad \chi(G_t)\longrightarrow\infty.
\]

Orient every edge of \(G_t\) independently and uniformly. For a vertex \(v\),
\[
d^+(v)\sim \operatorname{Bin}(d(v),1/2).
\]
A Chernoff bound gives
\[
\Pr\bigl(d^+(v)<d(v)/3\bigr)\le \exp(-d(v)/36)
 \le \exp(-\eta |V(G_t)|/36).
\]
For sufficiently large \(t\), a union bound over all vertices is less than one. Thus \(G_t\) has an orientation \(D_t\) satisfying
\[
\delta^+(D_t)\ge \frac{\eta}{3}|V(D_t)|.
\]

Furthermore,
\[
\chi(D_t)=\chi(G_t)\longrightarrow\infty,
\]
and \(D_t\) cannot contain \(H\), because an embedding of \(H\) would give an embedding of \(U(H)\) into \(G_t\). This contradicts affirmativity at \(\varepsilon=\eta/3\). ∎

The established classification of zero undirected chromatic threshold says that a fixed graph has this property exactly when it is bipartite, or when it is \(3\)-chromatic and near-acyclic. Here a \(3\)-chromatic graph \(J\) is near-acyclic if there is an independent set \(S\) such that \(J-S\) is a forest and every odd cycle of \(J\) contains at least two vertices of \(S\).

Consequently:

### Corollary 3.2

If \(H\) is affirmative, then \(U(H)\) is bipartite or near-acyclic. In particular, \(U(H)\) is triangle-free and has chromatic number at most three.

This reduction is independent of Proposition 2.1. For example, a transitive triangle has a source-forest grading but is excluded by Corollary 3.2.

---

## 4. An explicit negative acyclic orientation of \(K_{3,3}\)

For \(r\ge2\), let
\[
A=\{a_1,\dots,a_r\},\qquad B=\{b_1,\dots,b_r\},
\]
and orient \(K_{r,r}\) according to the total order
\[
a_1,b_1,a_2,b_2,\dots,a_r,b_r.
\]
Equivalently,
\[
a_i\to b_j\quad\text{if }i\le j,\qquad
b_j\to a_i\quad\text{if }j<i.
\]
Call this digraph \(H_r\). It is acyclic.

### Proposition 4.1

For every \(r\ge3\), \(H_r\) is not affirmative.

#### Structural proof

Let
\[
z_{2i-1}=a_i,\qquad z_{2i}=b_i.
\]
Then
\[
z_1\to z_2\to\cdots\to z_{2r}
\]
is a directed path, and there is also the arc
\[
z_1\to z_{2r}.
\]

Suppose \(H_r\) had a source-forest grading with exceptional forest \(S\). Along the directed path, every edge either has both ends in \(S\), contributing zero to the level difference, or increases the level by exactly one.

If \(z_1,z_{2r}\in S\), then once the path left \(S\) it could never return to level zero. Therefore the whole path would lie in \(S\), but \(H_r[S]=K_{r,r}\) is not a forest.

Otherwise, the shortcut \(z_1\to z_{2r}\) gives
\[
\ell(z_{2r})-\ell(z_1)=1.
\]
Hence exactly one of the \(2r-1\) path edges is not internal to \(S\). It follows that
\[
z_1,\dots,z_{2r-1}\in S,\qquad z_{2r}\notin S.
\]
But \(H_r[S]\) has underlying graph \(K_{r,r-1}\), which contains a \(C_4\) when \(r\ge3\). This again contradicts that \(H_r[S]\) is a forest.

Thus \(H_r\) violates the necessary condition of Proposition 2.1. ∎

### Fully specified host family

The negative result also has a direct witness.

Fix \(r\ge3\), and put \(k=2r+1\). For each \(t\), choose a \(C_4\)-free graph \(G_t\) with \(\chi(G_t)\ge t\), and orient its edges arbitrarily. Construct \(D_t\) with equal parts
\[
V_0,V_1,\dots,V_{k-1},
\]
where \(V_0\) induces the oriented \(G_t\), every other \(V_i\) is independent, and all arcs from \(V_i\) to \(V_{i+1\bmod k}\) are present. There are no other arcs.

Writing \(m=|V(G_t)|\), we have
\[
|V(D_t)|=km,\qquad
\delta^+(D_t)\ge m=\frac{|V(D_t)|}{2r+1},
\qquad
\chi(D_t)\ge t.
\]

Suppose \(H_r\) embedded in \(D_t\). Along
\[
z_1\to z_2\to\cdots\to z_{2r},
\]
the part index either stays fixed or advances by one modulo \(k\). Let \(q\) be the number of advances. Since \(q\le2r-1<k\), and since the shortcut \(z_1\to z_{2r}\) requires the final part to equal the initial part or its successor, one has \(q\in\{0,1\}\).

- If \(q=0\), all vertices lie in one part. It must be \(V_0\), but this would put a \(C_4\) of \(K_{r,r}\) inside \(G_t\).
- If \(q=1\), the sequence splits into a prefix and suffix in two consecutive parts. At most one of those parts is \(V_0\). A block lying in an independent part has size at most one, because consecutive \(z_i\)'s are adjacent. The block in \(V_0\) therefore has at least \(2r-1\ge5\) vertices and contains at least two vertices from each side of \(K_{r,r}\), again forcing a \(C_4\) in \(G_t\).

Thus every \(D_t\) is \(H_r\)-free. In particular, \(H_3\), an acyclic orientation of \(K_{3,3}\), is a concrete negative instance at \(\varepsilon=1/7\).

This shows that the two elementary conditions

- \(H\) is acyclic;
- \(U(H)\) is bipartite,

are not sufficient.

---

## 5. A positive class: strictly leveled digraphs

A digraph \(H\) is strictly leveled if there is \(g:V(H)\to\mathbb Z\) such that every arc \(u\to v\) satisfies
\[
g(v)=g(u)+1.
\]
Every orientation of a forest is strictly leveled: choose a root in each tree and integrate the equations along its unique paths. Uniformly oriented bipartite graphs are strictly leveled with two levels.

### Proposition 5.1

For every strictly leveled \(H\) and every \(\varepsilon>0\), there is \(n_0=n_0(H,\varepsilon)\) such that every \(n\)-vertex digraph \(D\) with
\[
n\ge n_0,\qquad \delta^+(D)\ge\varepsilon n
\]
contains \(H\).

#### Proof

This is a standard directed regularity argument; details of the reduction are included.

Choose constants
\[
0<\eta\ll d\ll \varepsilon,\frac1{|V(H)|},
\]
and apply a simultaneous directed regularity lemma to the two directional arc relations. We obtain an exceptional set \(V_0\) and equal clusters
\[
V_1,\dots,V_k
\]
of size \(m\), with \(k\) bounded and chosen initially large compared with \(1/\varepsilon\).

Discard the \(O(\sqrt\eta k)\) clusters incident with more than \(\sqrt\eta k\) irregular pairs. On the remaining clusters define a reduced digraph \(R\) by placing \(i\to j\) when the ordered pair \(V_i\to V_j\) is regular and has arc density at least \(d\).

Every remaining cluster has an out-neighbor in \(R\). Indeed, if \(V_i\) had none, its outgoing arcs would all lie in:

- the exceptional set;
- discarded clusters;
- its own cluster;
- irregular pairs;
- regular pairs of density less than \(d\).

The total number of these arcs is at most
\[
\bigl(O(\sqrt\eta)+\eta+d+1/k\bigr)mn<\varepsilon mn,
\]
contradicting
\[
\sum_{v\in V_i}d^+(v)\ge \varepsilon mn.
\]

Thus \(R\) has minimum out-degree at least one and consequently contains a directed cycle
\[
i_0\to i_1\to\cdots\to i_{s-1}\to i_0.
\]

Assign every vertex \(v\in V(H)\) to cluster \(V_{i_{g(v)\bmod s}}\). Since every arc increases \(g\) by one, every required arc is assigned to an ordered regular pair on this directed cycle. Split each cluster into a bounded number of subclusters, one for each level of \(g\) assigned to it. By the slicing lemma, every required ordered pair of subclusters remains regular with density at least \(d/2\), provided \(\eta\) was chosen sufficiently small.

There are no arcs of \(H\) within a level. The standard multipartite embedding lemma therefore embeds \(H\) into these subclusters once \(m\) is sufficiently large. ∎

Since \(\chi(D)\le |V(D)|\), taking \(c_\varepsilon=n_0(H,\varepsilon)\) gives the required catalog property.

### Elementary forest bound

For oriented trees one can avoid regularity entirely. If \(T\) has \(t\) vertices, then every \(T\)-free digraph satisfies
\[
\chi(D)\le (t-1)^2.
\]

Indeed, remove a leaf \(x\) of \(T\), with neighbor \(y\), and let \(T'=T-x\). Let \(S\) be the set of vertices that can be the image of \(y\) in a copy of \(T'\).

- If the leaf arc is \(y\to x\), then every \(v\in S\) has \(d^+(v)\le t-2\), since any out-neighbor outside a chosen copy of \(T'\) would extend it to \(T\).
- If the leaf arc is \(x\to y\), then every \(v\in S\) has \(d^-(v)\le t-2\).

Thus every induced subgraph of \(U(D[S])\) has at most \((t-2)|S|\) edges, and
\[
\chi(D[S])\le 2t-3.
\]
Also \(D-S\) is \(T'\)-free. Induction gives
\[
\chi(D)\le (2t-3)+(t-2)^2=(t-1)^2.
\]

Hence all oriented forests are affirmative even without using the minimum out-degree hypothesis.

---

## 6. What remains open

The following necessary package emerges:

1. every weak component of \(H\) has a source-forest grading;
2. \(U(H)\) is bipartite or near-acyclic.

These conditions are independent:

- a transitive triangle has a source-forest grading but fails the undirected condition;
- the acyclic \(K_{3,3}\) orientation \(H_3\) is bipartite but fails the source-forest grading.

Strictly leveled digraphs form a positive subclass, but the general source-forest-graded case with a nontrivial forest at level zero is not settled here. In particular, I do not prove that the two necessary conditions are sufficient. The cycle theorem in the source paper handles special instances of precisely this remaining interaction between the high-chromatic forest-bearing part and the dense out-neighborhood structure.