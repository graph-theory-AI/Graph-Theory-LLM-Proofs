```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "A 13-vertex circulant-complement seed has (omega,zeta,chi)=(4,4,7), and iterated Mycielski constructions raise zeta and chi together by one while preserving clique number.",
  "would_publish": true,
  "caveats": "The proof is self-contained; only literature priority has not been independently checked."
}
```

# Theorem

For every integer \(k\ge 5\), there is a graph \(G_k\) satisfying
\[
\omega(G_k)=4,\qquad \zeta(G_k)=k,\qquad \chi(G_k)=k+3.
\]
In fact, the construction also gives such a graph for \(k=4\).

The proof consists of a 13-vertex seed and a lemma about the Mycielski construction.

## 1. A cochromatic lemma for Mycielski graphs

For a graph \(H\), let \(\mu(H)\) denote its Mycielskian. Thus, for every \(v\in V(H)\), there are vertices \(v^0,v^1\), together with a root \(r\). The edges are:

- \(u^0v^0\) whenever \(uv\in E(H)\);
- \(u^0v^1\) and \(u^1v^0\) whenever \(uv\in E(H)\);
- \(rv^1\) for every \(v\in V(H)\);

and there are no other edges. In particular, the first layer \(V^1=\{v^1\}\) is independent, and \(r\) is anticomplete to the old layer \(V^0=\{v^0\}\).

### Lemma 1

For every graph \(H\),
\[
\zeta(\mu(H))\ge \zeta(H)+1.
\]
If \(H\) has a minimum cochromatic partition containing an independent part, then
\[
\zeta(\mu(H))=\zeta(H)+1,
\]
and \(\mu(H)\) again has a minimum cochromatic partition containing an independent part.

#### Proof

Let \(\mathcal P\) be a cochromatic partition of \(\mu(H)\) into \(q\) parts, and let \(C\) be the part containing \(r\).

If \(C\) is a clique, then \(C\) contains no old-layer vertex and at most one first-layer vertex. Removing \(C\) and restricting the other \(q-1\) parts to \(V^0\) gives a cochromatic partition of \(H\). Hence
\[
\zeta(H)\le q-1.
\]

Suppose instead that \(C\) is independent. Since \(r\) is adjacent to every first-layer vertex, we have
\[
C=\{r\}\cup \{v^0:v\in S\}
\]
for some independent set \(S\subseteq V(H)\).

For every other part \(D\in\mathcal P\setminus\{C\}\), define
\[
D^*=
\{v:v^0\in D\}\ \cup\
\{v\in S:v^1\in D\}.
\]
These sets partition \(V(H)\):

- if \(v\notin S\), its old copy \(v^0\) occurs in exactly one \(D\ne C\);
- if \(v\in S\), its first-layer copy \(v^1\) occurs in exactly one \(D\ne C\).

Moreover, \(D^*\) is homogeneous.

- If \(D\) is independent, then its old-layer vertices are pairwise nonadjacent. A replacement \(v^1\mapsto v\), with \(v\in S\), preserves adjacency relations to old-layer vertices, while two such replacements are nonadjacent because \(S\) is independent.
- If \(D\) is a clique, then \(D\) contains at most one first-layer vertex. Replacing that vertex \(v^1\) by \(v\) preserves all adjacencies to old-layer vertices.

After discarding empty sets, the \(D^*\) give a cochromatic partition of \(H\) into at most \(q-1\) parts. Thus again
\[
\zeta(H)\le q-1.
\]
This proves \(\zeta(\mu(H))\ge \zeta(H)+1\).

Now suppose \(H\) has a minimum cochromatic partition
\[
I,P_2,\dots,P_{\zeta(H)}
\]
with \(I\) independent. Then
\[
\{r\}\cup I^0,\quad P_2^0,\dots,P_{\zeta(H)}^0,\quad V^1
\]
is a cochromatic partition of \(\mu(H)\) into \(\zeta(H)+1\) parts. Both \(\{r\}\cup I^0\) and \(V^1\) are independent. The lower bound proves optimality and also shows that the required property persists. \(\square\)

We will also use the standard Mycielski identities
\[
\chi(\mu(H))=\chi(H)+1,\qquad
\omega(\mu(H))=\max\{\omega(H),2\}.
\]

For completeness, the chromatic lower bound follows as follows. Given a proper \(q\)-coloring of \(\mu(H)\), rename the color of \(r\) as \(q\). No \(v^1\) receives color \(q\). Color \(v\in H\) by the color of \(v^0\), unless \(v^0\) has color \(q\), in which case use the color of \(v^1\). This is a proper \((q-1)\)-coloring of \(H\). The clique-number identity follows because a clique not containing \(r\) contains at most one first-layer vertex and projects injectively to a clique of \(H\).

## 2. The 13-vertex seed

Let \(F\) be the circulant graph on \(\mathbb Z_{13}\) in which
\[
xy\in E(F)
\quad\Longleftrightarrow\quad
x-y\equiv \pm1,\pm5\pmod {13}.
\]
Let
\[
G=\overline F.
\]

We verify
\[
\omega(G)=4,\qquad \zeta(G)=4,\qquad \chi(G)=7,
\]
and that \(G\) has an optimal cochromatic partition containing an independent part.

### 2.1. The graph \(F\) is triangle-free

Let
\[
D=\{\pm1,\pm5\}\subseteq \mathbb Z_{13}.
\]
The differences between two distinct elements of \(D\) lie in
\[
\{\pm2,\pm3,\pm4,\pm6\},
\]
which is disjoint from \(D\). A triangle can be translated so that one vertex is \(0\); its other two vertices would then be distinct \(a,b\in D\) with \(a-b\in D\), which is impossible.

Thus
\[
\omega(F)=2.
\]

### 2.2. The independence number of \(F\) is four

The set
\[
\{0,2,4,6\}
\]
is independent in \(F\), so \(\alpha(F)\ge4\).

Suppose that \(F\) had an independent set of five vertices. List them cyclically around \(\mathbb Z_{13}\), and let their five cyclic gaps be \(g_1,\dots,g_5\). Since vertices at distance one are adjacent,
\[
g_i\ge2,\qquad \sum_{i=1}^5 g_i=13.
\]
Consequently, up to order, the gaps have one of the following forms:
\[
(5,2,2,2,2),\qquad
(4,3,2,2,2),\qquad
(3,3,3,2,2).
\]

- In the first case, a gap of five gives an edge of \(F\).
- In the second case, the gap of size three is cyclically adjacent to a gap of size two, since there is only one gap of size four. Their sum is five, again giving an edge.
- In the third case, some gap of size two is cyclically adjacent to a gap of size three, also giving two selected vertices at distance five.

All cases contradict independence. Therefore
\[
\alpha(F)=4.
\]

It follows that
\[
\omega(G)=\alpha(F)=4,\qquad
\alpha(G)=\omega(F)=2.
\]

### 2.3. Chromatic number of \(G\)

Since every independent set in \(G\) has size at most two,
\[
\chi(G)\ge \left\lceil\frac{13}{2}\right\rceil=7.
\]

On the other hand,
\[
\{0,1\},\{2,3\},\{4,5\},\{6,7\},\{8,9\},\{10,11\},\{12\}
\]
is a proper 7-coloring of \(G\), because each two-element class is an edge of \(F\), hence a nonedge of \(G\). Therefore
\[
\chi(G)=7.
\]

### 2.4. Cochromatic number of \(G\)

Every clique of \(G\) has size at most four, and every independent set has size at most two. Hence every homogeneous set has size at most four, so
\[
\zeta(G)\ge \left\lceil\frac{13}{4}\right\rceil=4.
\]

Now consider the following partition of \(\mathbb Z_{13}\):
\[
\begin{aligned}
A&=\{0,2,4,6\},\\
B&=\{1,5,7,11\},\\
C&=\{3,10,12\},\\
I&=\{8,9\}.
\end{aligned}
\]
The cyclic distances occurring inside \(A,B,C\) avoid \(1\) and \(5\), so these three sets are independent in \(F\), and hence cliques in \(G\). The vertices \(8,9\) are adjacent in \(F\), so \(I\) is independent in \(G\). Thus
\[
A,B,C,I
\]
is a cochromatic partition of \(G\) into four parts, one of which is independent. Consequently,
\[
\zeta(G)=4.
\]

We have therefore constructed a seed satisfying
\[
(\omega(G),\zeta(G),\chi(G))=(4,4,7).
\]

## 3. The infinite family

For \(k\ge5\), set
\[
G_k=\mu^{\,k-4}(G).
\]
Lemma 1 applies at every step because the seed has an optimal cochromatic partition containing an independent part, and that property persists under \(\mu\). Therefore
\[
\zeta(G_k)=4+(k-4)=k.
\]
The Mycielski chromatic identity gives
\[
\chi(G_k)=7+(k-4)=k+3.
\]
Finally, since \(\omega(G)=4\), repeated Mycielski constructions preserve the clique number:
\[
\omega(G_k)=4<5.
\]

Thus \(G_k\) has all the required properties for every \(k\ge5\). Its order is explicitly
\[
|V(G_k)|=14\cdot 2^{k-4}-1.
\]

# Gaps and caveats

There is no mathematical gap in the construction: all parameter values are established by explicit upper and lower bounds. The only remaining caveat is bibliographic priority; I have not independently checked whether this exact circulant seed and Mycielski argument have appeared subsequent to the supplied catalog review.