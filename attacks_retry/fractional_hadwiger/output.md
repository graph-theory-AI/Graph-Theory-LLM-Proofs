```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "All three inequalities hold for induced-2K2-free graphs; in fact, these graphs satisfy the ordinary Hadwiger inequality with branch sets of size at most two.",
  "would_publish": false,
  "caveats": "The unrestricted conjectures remain unresolved here; the restricted result uses Gallai's classical critical-graph theorem, and novelty is not claimed."
}
```

## 1. Restricted theorem

I can remove the independence-number restriction from the previous attempt, and prove a stronger integral statement for that entire graph class.

All graphs below are finite and simple. A graph is **induced-\(2K_2\)-free** if no four vertices induce exactly two disjoint edges.

**Theorem.** Every induced-\(2K_2\)-free graph \(G\) has a \(K_{\chi(G)}\) minor whose branch sets each have at most two vertices. In particular,
\[
\boxed{\chi(G)\le \operatorname{had}(G).}
\]
Consequently, all three fractional Hadwiger inequalities hold for induced-\(2K_2\)-free graphs, with no restriction on their independence number.

I do not claim this restricted theorem is new. The proof below verifies the matching facts reused from the previous attempt and does not use the small-order Hadwiger cases.

Besides Hall’s theorem, the structural input is the following classical theorem.

> **Gallai’s critical-graph theorem.** If \(G\) is vertex-\(k\)-critical and \(|V(G)|\le 2k-2\), then \(\overline G\) is disconnected.

Here vertex-\(k\)-critical means \(\chi(G)=k\) and \(\chi(G-v)<k\) for every vertex \(v\). If one uses the usual formulation for graphs critical under all proper subgraphs, the stated version follows by taking an edge-minimal spanning \(k\)-chromatic subgraph. Vertex-criticality ensures every vertex is still necessary; adding edges back cannot connect its complement.

## 2. Matchings and complete minors

Two vertex sets *touch* if they intersect or an edge joins them.

The defining property of induced-\(2K_2\)-free graphs gives the following useful observation:

\[
\boxed{\text{The edges of every matching are branch sets of a complete minor.}} \tag{1}
\]

Indeed, two matching edges are disjoint, and the absence of an edge between their endpoints would give an induced \(2K_2\). Thus, writing \(\nu(G)\) for the matching number,
\[
\operatorname{had}(G)\ge \nu(G),                            \tag{2}
\]
with every branch set in this model having two vertices.

We need a little more control over matchings.

### Lemma 1: fractional perfect matchings

A graph \(F\) has a fractional perfect matching if and only if
\[
|N_F(I)|\ge |I|
\qquad\text{for every independent set }I\subseteq V(F).     \tag{3}
\]
When these conditions hold, \(F\) has a spanning subgraph whose components are edges or cycles.

**Proof.**
A fractional perfect matching consists of weights \(x_e\ge0\) satisfying
\[
\sum_{e\ni v}x_e=1
\qquad(v\in V(F)).
\]
Summing these equations over an independent set \(I\) gives (3): the weight incident with \(I\) also uses capacity in \(N_F(I)\).

Conversely, suppose (3) holds. Form the bipartite double cover, with left and right copies of \(V(F)\), and edge \(u_Lv_R\) whenever \(uv\in E(F)\).

For \(X\subseteq V(F)\), write
\[
\Gamma(X)=\bigcup_{x\in X}N_F(x),
\qquad I=X\setminus\Gamma(X).
\]
The set \(I\) consists of the isolated vertices of \(F[X]\), so it is independent and
\[
N_F(I)\subseteq \Gamma(X)\setminus X.
\]
Hence
\[
|\Gamma(X)|
\ge |X|-|I|+|N_F(I)|
\ge |X|.
\]
Hall’s theorem gives a perfect matching in the double cover.

That perfect matching defines a permutation \(\pi\) of \(V(F)\), with \(v\pi(v)\in E(F)\). Its permutation cycles give a spanning collection of edges and cycles in \(F\): a permutation cycle of length two gives one edge. Assign weight \(1\) to these edge components and weight \(1/2\) to each edge of the cycle components. This is a fractional perfect matching. ∎

### Lemma 2: rounding in the induced-\(2K_2\)-free class

If an induced-\(2K_2\)-free graph \(F\) has a fractional perfect matching, then
\[
\nu(F)=\left\lfloor\frac{|V(F)|}{2}\right\rfloor.            \tag{4}
\]

**Proof.**
Use the spanning collection of edges and cycles from Lemma 1. Match each even cycle perfectly.

Any two of the odd cycles have an edge between them: otherwise, one edge from each would induce a \(2K_2\). Given such an edge \(uv\) between two odd cycles, use \(uv\), together with perfect matchings of the two even paths obtained by deleting \(u\) and \(v\) from their respective cycles. Thus their union has a perfect matching.

Pair off the odd cycles in this way. At most one odd cycle remains, and it has a matching leaving exactly one vertex uncovered. The resulting matching covers all but at most one vertex of \(F\). ∎

## 3. The Hall-deficient case is not an obstruction

The next lemma is the main improvement over the earlier attempt.

### Lemma 3

Let \(G\) be an induced-\(2K_2\)-free, vertex-\(k\)-critical graph. If \(G\) has no fractional perfect matching, then it has a \(K_k\) minor with branch sets of size at most two.

**Proof.**
Vertex-criticality gives
\[
\delta(G)\ge k-1.                                         \tag{5}
\]

By Lemma 1, choose an independent set \(I\) maximizing
\[
d(I)=|I|-|N_G(I)|,
\]
where this maximum is positive. Put
\[
T=N_G(I),\qquad
R=V(G)\setminus(I\cup T),\qquad t=|T|.
\]

First, there is a matching between \(I\) and \(T\) saturating \(T\). Otherwise, Hall’s theorem gives \(U\subseteq T\) such that
\[
|A|<|U|,
\qquad A=N_G(U)\cap I.
\]
Since
\[
N_G(I\setminus A)\subseteq T\setminus U,
\]
we obtain
\[
d(I\setminus A)
\ge |I|-|A|-|T|+|U|
=d(I)+|U|-|A|
>d(I),
\]
a contradiction.

Thus \(G\) has a matching \(M\) of size \(t\), all of whose edges lie between \(I\) and \(T\). Also, for any \(v\in I\), (5) gives
\[
k\le d_G(v)+1\le t+1.                                    \tag{6}
\]

There are two cases.

**Case 1: \(R\ne\varnothing\).**  
The graph \(G[R]\) must contain an edge. Otherwise \(I\cup R\) is independent, and its neighborhood is contained in \(T\), giving
\[
d(I\cup R)\ge d(I)+|R|>d(I).
\]
An edge of \(G[R]\), together with \(M\), is a matching of size \(t+1\). By (1) and (6), its edges give a complete minor of order at least \(k\).

**Case 2: \(R=\varnothing\).**  
Here \(T\) is a vertex cover and \(I\) is independent.

If \(G[T]\) is not complete, color \(T\) with at most \(t-1\) colors and use one new color on \(I\). This gives \(k\le t\), and \(M\) gives the required minor.

If \(G[T]\) is complete but no vertex of \(I\) is complete to \(T\), give \(T\) distinct colors and give each vertex of \(I\) the color of one of its nonneighbors in \(T\). Again \(k\le t\).

In the remaining case, \(T\cup\{v\}\) is a clique of order \(t+1\) for some \(v\in I\). By (6), this clique contains a \(K_k\).

All the branch sets used are singletons or edges. ∎

Thus, in a smallest counterexample to the restricted theorem, a fractional perfect matching is compulsory. Lemma 2 then supplies an ordinary matching covering all but at most one vertex.

## 4. The remaining odd-order case

We next handle precisely the extra vertex that a near-perfect matching might leave uncovered.

### Lemma 4

Let \(G\) be induced-\(2K_2\)-free, with
\[
|V(G)|=2q-1,\qquad \delta(G)\ge q-1.
\]
Then \(G\) has a \(K_q\) minor consisting of one singleton branch set and \(q-1\) edge branch sets.

**Proof.**
The case \(q=1\) is immediate. Choose a minimum-degree vertex \(v\), and put
\[
d=d_G(v)=\delta(G),\qquad
A=N_G(v),\qquad
B=V(G)\setminus N_G[v].
\]
Then
\[
|A|=d,\qquad |B|=2q-2-d\le q-1\le d.                     \tag{7}
\]

Let \(J\) be obtained from \(G-v\) by deleting all edges with both endpoints in \(B\). We will show that \(J\) has a perfect matching.

#### A matching saturating \(B\)

Consider the bipartite graph of edges between \(B\) and \(A\). Suppose Hall’s condition fails, so some \(U\subseteq B\) satisfies
\[
|N_A(U)|<|U|.
\]
By (7), there is a vertex \(a\in A\setminus N_A(U)\).

The set \(U\) must be independent. Otherwise an edge of \(G[U]\), together with \(va\), would induce a \(2K_2\).

Consequently, for \(u\in U\),
\[
d_G(u)
\le |N_A(U)|+|B|-|U|
<|B|
\le q-1
\le\delta(G),
\]
a contradiction. Thus there is a matching between \(B\) and \(A\) saturating \(B\).

If \(d=q-1\), then \(|A|=|B|\), and this matching is already perfect in \(J\).

#### Completing the matching when \(d\ge q\)

We use the following elementary matching-closure fact.

> If \(L\) has even order \(N\), and nonadjacent vertices \(x,y\) satisfy
> \[
> d_L(x)+d_L(y)\ge N-1,
> \]
> then \(L\) has a perfect matching if and only if \(L+xy\) does.

To verify the nontrivial direction, take a perfect matching of \(L+xy\) using \(xy\). If some other matching edge \(ab\) permits replacing \(xy,ab\) by \(xa,yb\), or by \(xb,ya\), we obtain a perfect matching in \(L\). If no such replacement exists, each of the other matching edges receives at most two edges from \(\{x,y\}\). Hence
\[
d_L(x)+d_L(y)\le N-2,
\]
a contradiction.

Now \(J\) has order \(N=2q-2\), and for every \(a\in A\),
\[
d_J(a)=d_G(a)-1\ge d-1\ge q-1.
\]
Thus any two nonadjacent vertices of \(A\) have degree sum at least \(2q-2=N\). We may add all missing edges within \(A\), one at a time, without changing the existence of a perfect matching.

In the resulting graph, first use the matching saturating \(B\). The unused vertices of \(A\) form a clique of even order, so they can be matched perfectly. Reversing the closure steps shows that \(J\) itself has a perfect matching \(M\).

Finally, every edge of \(M\) has an endpoint in \(A\), and therefore touches \(\{v\}\). The edges of \(M\) pairwise touch by induced-\(2K_2\)-freeness. Hence
\[
\{\{v\}\}\cup\{V(e):e\in M\}
\]
is a \(K_q\)-minor model of the required form. ∎

## 5. Proof of the restricted theorem

The empty graph is harmless. Suppose the theorem fails, and choose a counterexample \(G\) of minimum order. Write
\[
k=\chi(G),\qquad n=|V(G)|.
\]

Here “counterexample” means that \(G\) has no \(K_k\)-minor model with branch sets of size at most two.

### Step 1: \(G\) is vertex-\(k\)-critical

If \(\chi(G-v)=k\) for some vertex \(v\), minimality supplies the required minor model in \(G-v\), hence in \(G\). Therefore
\[
\chi(G-v)<k\quad\text{for every }v,
\qquad\text{and so}\qquad
\delta(G)\ge k-1.                                         \tag{8}
\]

### Step 2: \(\overline G\) is connected

Otherwise, let \(V_1,\dots,V_s\) be its components, with \(s\ge2\), and put \(G_i=G[V_i]\). Every vertex of \(G_i\) is adjacent in \(G\) to every vertex of \(G_j\) for \(i\ne j\). Thus
\[
\chi(G)=\sum_{i=1}^s\chi(G_i).
\]
Each \(G_i\) is a smaller induced-\(2K_2\)-free graph. By minimality it has the required minor model of order \(\chi(G_i)\). Taking all these models together gives a complete minor of order \(\chi(G)\), still with branch sets of size at most two—a contradiction.

### Step 3: \(G\) has a fractional perfect matching

Otherwise Lemma 3 supplies the forbidden \(K_k\)-minor model.

### Step 4: finish by order

Gallai’s theorem, applied using Steps 1 and 2, gives
\[
n\ge2k-1.
\]

If \(n\ge2k\), Lemma 2 gives a matching of size
\[
\left\lfloor n/2\right\rfloor\ge k.
\]
Its edges are the required complete-minor branch sets by (1).

The only remaining possibility is \(n=2k-1\). Then (8) allows us to apply Lemma 4 with \(q=k\), again obtaining the required minor.

Every case contradicts the choice of \(G\). This proves the theorem. ∎

## 6. Consequences and remaining limitation

For every induced-\(2K_2\)-free graph,
\[
\chi_f(G)
\le \chi(G)
\le \operatorname{had}(G)
\le \operatorname{had}_f(G).
\]
The first and last inequalities follow by viewing ordinary colorings and ordinary clique-minor models as fractional solutions with unit weights. This chain proves **(a), (b), and (c)** on the stated class.

The argument does **not** prove any of the three inequalities for arbitrary graphs. Its essential special-class property is (1): arbitrary matching edges become pairwise adjacent branch sets. An induced \(2K_2\) already destroys that property.

Thus the independence-number restriction in the earlier partial result is unnecessary, and all three assertions hold on that entire class. The unrestricted problem remains unresolved by this argument.