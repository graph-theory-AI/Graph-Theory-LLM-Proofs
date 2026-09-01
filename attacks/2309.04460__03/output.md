```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I derive an embedding obstruction for identity products, determine t(k) exactly for 2≤k≤7, and prove asymptotic bounds showing t(k)=k^{1+o(1)}.",
  "would_publish": false,
  "caveats": "The exact value remains open from k=8 onward; the asymptotic upper bound uses the rainbow-cycle theorem from the source paper, and t(2),t(3) use the usual vacuous-threshold convention."
}
```

# Mathematical writeup

## 1. Reformulation

Identify the transposition \((ij)\in S_k\) with the edge \(ij\) of \(K_k\). Call a graph \(G\) **product-one-free** if no nonempty subset \(F\subseteq E(G)\) can be ordered as
\[
\tau_1\tau_2\cdots \tau_m=1.
\]
If \(M(k)\) is the maximum number of edges in a product-one-free graph on \(k\) labeled vertices, then
\[
t(k)=M(k)+1.
\]

The main results established below are
\[
\boxed{t(2)=2,\quad t(3)=4,\quad t(4)=6,\quad
t(5)=8,\quad t(6)=11,\quad t(7)=14}
\]
and
\[
\boxed{\left(\frac12-o(1)\right)\frac{k\log k}{\log\log k}
\le t(k)\le (k\log k)^{1+o(1)}}.
\]
In particular,
\[
t(k)=k^{1+o(1)}.
\]

For \(k=8\), the arguments also give
\[
16\le t(8)\le18.
\]

---

## 2. The ribbon-surface obstruction

The following is the main structural observation.

### Lemma 2.1
Let
\[
\tau_1\tau_2\cdots\tau_m=\pi
\]
be a product of distinct transpositions, and let \(H\) be their graph on its \(v\) support vertices. If \(H\) is connected, there is an orientable cellular embedding of \(H\) whose number of faces is the number \(c(\pi)\) of cycles of \(\pi\) on those \(v\) vertices.

#### Proof
At every vertex of \(H\), cyclically order the incident edges by their indices in the word \(\tau_1,\ldots,\tau_m\). This defines an orientable ribbon graph.

One can see the face-permutation correspondence either by tracing darts or by attaching the edge-bands successively. Start with \(v\) oriented vertex-discs, one for each support vertex. Attach the band corresponding to \(\tau_i=(a_i b_i)\) at the next available slots of the discs \(a_i,b_i\). On the boundary components, this surgery interchanges the two boundary successors corresponding to \(a_i,b_i\). Thus, after the first \(j\) bands have been attached, the boundary-component permutation is
\[
\tau_1\cdots\tau_j.
\]
Consequently, after all bands are attached, the boundary components are indexed by the cycles of \(\pi\). Capping these boundary components gives the required cellular embedding. ∎

### Corollary 2.2
If the transpositions corresponding to a connected simple graph \(H\) can be ordered to have product \(1\), then
\[
|E(H)|=2|V(H)|-2+2g
\]
for some integer \(g\ge0\). In particular,
\[
|E(H)|\ge 2|V(H)|-2,
\]
and if equality holds, then \(H\) is planar.

#### Proof
In Lemma 2.1, \(\pi=1\), so the ribbon surface has
\[
f=c(\pi)=|V(H)|
\]
faces. Euler's formula gives
\[
|V(H)|-|E(H)|+|V(H)|=2-2g.
\]
Rearranging gives the result. ∎

Thus an identity product using the minimum possible number \(2v-2\) of transpositions must have a planar support graph. This already rules out the tempting guess \(t(k)=2k-2\).

### Lemma 2.3
The support graph of a connected identity product has no bridge.

#### Proof
Suppose \(e=xy\) is the unique edge crossing a partition \(V(H)=A\cup B\), with \(x\in A\), \(y\in B\). Every factor other than \((xy)\) preserves \(A\) setwise. Writing the word as
\[
P_1(xy)P_2,
\]
both \(P_1\) and \(P_2\) preserve \(A\), while \((xy)\) replaces one member of \(A\) by one member of \(B\). Hence the whole product does not preserve \(A\), and therefore cannot be the identity. ∎

### Corollary 2.4
If a connected simple graph \(H\) supports an identity product, then
\[
\frac{2|E(H)|}{|V(H)|}\ge \operatorname{girth}(H).
\]

#### Proof
Use the cellular embedding supplied by Lemma 2.1. By Lemma 2.3, \(H\) has no bridges, so every facial boundary is a cyclically reduced closed walk. It therefore has length at least \(\operatorname{girth}(H)\). There are \(|V(H)|\) faces and the sum of their boundary lengths is \(2|E(H)|\). Hence
\[
2|E(H)|\ge |V(H)|\operatorname{girth}(H).
\]
∎

In particular:

### Corollary 2.5
If \(G\) is a simple graph satisfying
\[
\Delta(G)<\operatorname{girth}(G),
\]
then \(G\) is product-one-free.

Indeed, every subgraph \(H\subseteq G\) has average degree at most \(\Delta(G)\), while any cyclic \(H\) has girth at least that of \(G\), contradicting Corollary 2.4. An acyclic \(H\) is excluded already by Corollary 2.2.

---

## 3. A useful family of explicit identities

For odd \(q\), label the vertices by \(\mathbb Z_q\), and define
\[
r_i(x)=2i-x.
\]
Then \(r_i\) is a reflection: it fixes \(i\) and is the product of \((q-1)/2\) pairwise disjoint transpositions. Write \(M_i\) for this matching.

Every edge \(xy\) belongs to exactly one \(M_i\), namely the one with
\[
i=\frac{x+y}{2}.
\]
Thus the \(M_i\) partition \(E(K_q)\).

Moreover,
\[
r_a r_b(x)=x+2(a-b),
\]
and consequently
\[
r_a r_b r_c r_d=1
\quad\text{whenever}\quad
a-b+c-d=0\pmod q.
\]
Expanding each \(r_i\) into its matching gives an identity product of distinct transpositions.

---

## 4. Exact values for \(2\le k\le7\)

### 4.1. The cases \(k=2,3,4\)

There is only one transposition in \(S_2\), and all three transpositions in \(S_3\) form a product-one-free set: an identity product must have even length, while two distinct transpositions cannot multiply to \(1\). Thus
\[
t(2)=2,\qquad t(3)=4.
\]
These use the usual convention that the threshold is one more than the largest product-one-free set, even if no set of that larger cardinality exists.

For \(k=4\), the five edges of \(K_4-e\) are product-one-free by Corollary 2.2. On the other hand, all six edges of \(K_4\) give
\[
\bigl((12)(34)\bigr)
\bigl((13)(24)\bigr)
\bigl((14)(23)\bigr)=1,
\]
because the three parenthesized permutations are the three nonidentity elements of the Klein four-group. Hence
\[
t(4)=6.
\]

### 4.2. The case \(k=5\)

A seven-edge product-one-free example is \(K_{2,3}\) together with the edge joining the two vertices in its part of size two. It has no \(K_4\), and Corollary 2.2 shows that an identity component on at most four vertices would have to be a \(K_4\), while one on five vertices would require at least eight edges.

Now let \(G\) have eight edges on five vertices. Its two missing edges are either adjacent or disjoint.

* If they are adjacent, the other four vertices span a \(K_4\).
* If they are disjoint, relabel them as the two edges of \(M_0\) in the reflection factorization of \(K_5\). The remaining edges are \(M_1,M_2,M_3,M_4\), and
  \[
  r_1r_2r_4r_3=1
  \]
  because \(1-2+4-3=0\pmod5\).

Therefore
\[
t(5)=8.
\]

### 4.3. The case \(k=6\)

For the lower bound, take
\[
G=K_{3,3}+e,
\]
where \(e\) is an edge inside one bipartition class. This graph has ten edges.

Suppose a connected subgraph \(H\subseteq G\) supports an identity product. If \(H\) has at most five vertices, its maximum possible numbers of edges are respectively
\[
1,3,5,7
\]
on \(2,3,4,5\) vertices, all strictly smaller than \(2v-2\). Thus \(H\) must use all six vertices and all ten edges. Equality holds in Corollary 2.2, so \(H\) would have to be planar. But it contains \(K_{3,3}\), a contradiction. Therefore \(G\) is product-one-free.

Conversely, let \(G\) have eleven edges on six vertices. Since its degree sum is \(22\), it has a vertex of degree at most three. Deleting that vertex leaves at least eight edges on five vertices, and the case \(k=5\) supplies an identity subset. Hence
\[
t(6)=11.
\]

### 4.4. The case \(k=7\)

For the lower bound, take \(G=K_{3,4}+e\), where \(e\) lies inside the part of size three. This graph has thirteen edges.

Let a connected identity-supporting subgraph use \(a\le3\) vertices from the first part and \(b\le4\) vertices from the second part. It has at most
\[
ab+1
\]
edges. The density condition \(|E|\ge2(a+b)-2\) leaves only the following possible equality cases:

* \(a=b=3\), using all edges of \(K_{3,3}+e\);
* \(a=3,b=4\), using twelve edges.

The first is nonplanar. In the second case, if the internal edge is omitted the graph is \(K_{3,4}\); if a cross-edge is omitted, the graph still contains a \(K_{3,3}\) obtained by avoiding the endpoint of that missing edge in the part of size four. Thus every possible twelve-edge support is nonplanar, contradicting Corollary 2.2. Since thirteen is odd, it cannot itself be the length of an identity product. Hence \(G\) is product-one-free.

Now let \(G\) have fourteen edges on seven vertices. If it has a vertex of degree at most three, deleting that vertex leaves at least eleven edges on six vertices, and the result for \(k=6\) applies.

Otherwise, \(G\) is 4-regular. Its complement in \(K_7\) is therefore a 2-regular graph, hence isomorphic either to \(C_7\) or to \(C_3\cup C_4\).

Use the matchings \(M_i\) on \(\mathbb Z_7\). Explicitly,
\[
\begin{aligned}
M_0&=\{16,25,34\},\\
M_1&=\{02,36,45\},\\
M_2&=\{04,13,56\}.
\end{aligned}
\]
Their union contains both

\[
4-0-2-5-6-1-3-4,
\]
a spanning \(C_7\), and
\[
(1-6-3-1)\ \cup\ (0-2-5-4-0),
\]
a spanning \(C_3\cup C_4\).

Thus, after relabeling, the complement of \(G\) is contained in
\[
M_0\cup M_1\cup M_2.
\]
Consequently \(G\) contains all twelve edges in
\[
M_3\cup M_4\cup M_5\cup M_6.
\]
Finally,
\[
r_3r_4r_6r_5=1
\]
because \(3-4+6-5=0\pmod7\). Expanding the four reflections gives the required identity product of twelve distinct transpositions. Therefore
\[
t(7)=14.
\]

---

## 5. The first unresolved case

The complete bipartite graph \(K_{3,5}\), with fifteen edges, is product-one-free.

Indeed, a connected subgraph meeting the two sides in \(a\le3\) and \(b\le5\) vertices has at most \(ab\) edges. Corollary 2.2 leaves only:

* \(a=3,b=4,m=12\), necessarily \(K_{3,4}\), which is nonplanar;
* \(a=3,b=5,m=14\), necessarily \(K_{3,5}\) minus one edge, which still contains \(K_{3,3}\), and is nonplanar;
* \(m=15\), which is odd.

Thus
\[
t(8)\ge16.
\]

On the other hand, any eighteen-edge graph on eight vertices has a vertex of degree at most four. Deleting it leaves at least fourteen edges on seven vertices, so \(t(7)=14\) gives
\[
t(8)\le18.
\]

I do not settle whether \(t(8)\) is \(16\), \(17\), or \(18\).

---

## 6. Asymptotic lower bound

We construct product-one-free graphs with maximum degree \(d\) and girth greater than \(d\).

Let
\[
d
\]
be the largest even integer at most
\[
\frac{\log k}{\log\log k}.
\]
Consider the configuration model for a random \(d\)-regular multigraph on \(k\) vertices. Let \(C_\ell\) denote the number of cycles of length \(\ell\), counting loops as length one and pairs of parallel edges as length two.

For \(3\le\ell\le d\), a direct pairing count gives
\[
\mathbb E C_\ell
\le
\frac{(k)_\ell[d(d-1)]^\ell}
{2\ell\,(kd-1)(kd-3)\cdots(kd-2\ell+1)}
\le d^\ell
\]
for sufficiently large \(k\). The analogous bounds for \(\ell=1,2\) are also at most \(d^\ell\). Hence
\[
\mathbb E\sum_{\ell=1}^d C_\ell\le 2d^d.
\]
Now
\[
d\log d
=
\log k-\frac{\log k\,\log\log\log k}{\log\log k}
+o\!\left(\frac{\log k}{\log\log k}\right),
\]
so
\[
d^d=o(k).
\]
Therefore there is a configuration having only \(o(k)\) cycles of lengths at most \(d\). Delete one edge from every such cycle. The resulting graph is simple, has girth greater than \(d\), maximum degree at most \(d\), and
\[
|E(G)|=\frac{kd}{2}-o(k)
=
\left(\frac12-o(1)\right)
\frac{k\log k}{\log\log k}.
\]
By Corollary 2.5, this graph is product-one-free. Consequently
\[
t(k)\ge
\left(\frac12-o(1)\right)
\frac{k\log k}{\log\log k}.
\]

---

## 7. Asymptotic upper bound from the source theorem

Let \(A\) be a product-one-free set of transpositions in \(S_k\). Form the Cayley graph
\[
\Gamma=\operatorname{Cay}(S_k,A).
\]
It has \(k!\) vertices and is \(|A|\)-regular. Color the edge
\[
\{\sigma,\sigma\tau\}
\]
by \(\tau\). Because every \(\tau\) is an involution, each color class is a matching, so this is a proper edge-coloring.

A rainbow cycle with successive colors \(\tau_1,\ldots,\tau_r\) gives
\[
\tau_1\cdots\tau_r=1,
\]
with all \(\tau_i\) distinct. Thus \(\Gamma\) has no rainbow cycle.

The main theorem quoted in the source paper gives average degree at most
\[
(\log N)^{1+o(1)}
\]
for a properly edge-colored \(N\)-vertex graph with no rainbow cycle. Applying it with \(N=k!\) gives
\[
|A|
\le
(\log(k!))^{1+o(1)}
=
(k\log k)^{1+o(1)}.
\]
Therefore
\[
t(k)\le (k\log k)^{1+o(1)}.
\]

Together with the lower bound,
\[
t(k)=k^{1+o(1)}.
\]

---

## 8. Fully specified exact-search procedure

For a fixed edge set \(E=\{e_1,\ldots,e_m\}\), all orderable products can be tested by the following dynamic program. For every mask \(B\subseteq E\), define a set of permutations
\[
\mathcal P(\varnothing)=\{1\},
\qquad
\mathcal P(B)
=
\bigcup_{e\in B}
\{\sigma\tau_e:\sigma\in\mathcal P(B\setminus\{e\})\}.
\]
Then \(B\neq\varnothing\) is an identity subset exactly when
\[
1\in\mathcal P(B).
\]
Enumerating all labeled graphs on \(k\) vertices and applying this recurrence determines \(t(k)\) exactly. Odd masks can be omitted by the sign homomorphism. No computational output beyond the proved small cases is claimed here.

---

## 9. Remaining gaps

1. The embedding condition is necessary but not shown sufficient. In particular, the relevant rotation system must be induced by a single global ordering of the edges.
2. The exact value is not determined for \(k\ge8\).
3. The asymptotic gap is between
   \[
   \Theta\!\left(\frac{k\log k}{\log\log k}\right)
   \quad\text{and}\quad
   (k\log k)^{1+o(1)}.
   \]
4. The ribbon-surface and high-girth arguments are elementary and may be standard; I have not verified their novelty in the existing literature.