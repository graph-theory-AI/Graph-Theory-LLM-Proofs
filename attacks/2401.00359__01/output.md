```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is verified for block expansions of arbitrary bipartite graphs and is shown to be stable under cone and private-leaf extensions.",
  "would_publish": false,
  "caveats": "The general common-neighborhood problem for vertices shared by an intermediate family of edges remains unresolved."
}
```

# 1. Statement and notation

For a \(k\)-uniform hypergraph \(H\), write
\[
\mathcal S_i(H)
 =\{S\subseteq V(H): |S|=i+1,\ S\subseteq e
 \text{ for some }e\in E(H)\},
 \qquad 1\le i<k.
\]
Thus \(\mathcal S_1(H)\) is the usual graph \(1\)-skeleton. For a uniform hypergraph \(F\), let
\[
\operatorname{degen}(F)
 =\max_{\varnothing\ne U\subseteq V(F)}
   \min_{v\in U}\deg_{F[U]}(v).
\]
I use the source paper's convention
\[
d_i(H)=\operatorname{degen}(\mathcal S_i(H)),
\qquad
d_{\max}(H)=\max_{1\le i<k}d_i(H).
\]

I do not prove the full conjecture. I prove several closure and special-case results.

# 2. Simultaneously synchronizing all skeletal degeneracies

The separate definitions of \(d_i(H)\) allow different optimal peeling orders. Nevertheless, this is not itself an obstruction.

## Lemma 2.1
There is an ordering \(v_1,\dots,v_h\) of \(V(H)\) such that, putting
\[
U_j=\{v_j,\dots,v_h\},
\]
for every \(j\) and every \(1\le i<k\),
\[
\deg_{\mathcal S_i(H)[U_j]}(v_j)
 \le 2(k-1)(i+1)d_i(H).
\]

### Proof
If \(F\) is a hypergraph of degeneracy at most \(d\), then
\[
e(F[U])\le d|U|
\]
for every \(U\): peel vertices of degree at most \(d\), assigning each edge to its first removed vertex.

Consequently, for every \(U\subseteq V(H)\),
\[
\sum_{v\in U}\deg_{\mathcal S_i(H)[U]}(v)
 =(i+1)e(\mathcal S_i(H)[U])
 \le(i+1)d_i(H)|U|.
\]
Hence fewer than \(|U|/(2(k-1))\) vertices have \(i\)-degree exceeding
\[
2(k-1)(i+1)d_i(H).
\]
Taking the union over \(i=1,\dots,k-1\), fewer than \(|U|/2\) vertices are bad for at least one \(i\). Thus some vertex is simultaneously good for every \(i\). Remove it and iterate. ∎

Thus there is a common elimination order with every forward skeletal degree \(O_k(d_{\max}(H))\). What remains missing in the general conjecture is a host-hypergraph embedding lemma that exploits this order without paying for all combinations of lower-dimensional faces.

# 3. Block expansions

This gives a sizable class for which the desired exponent follows from a lower-uniformity problem.

Let \(J\) be an \(r\)-uniform \(r\)-partite hypergraph with parts \(Y_1,\dots,Y_r\). Fix positive integers
\[
p_1+\cdots+p_r=k.
\]
The block expansion \(J^{\mathbf p}\), where \(\mathbf p=(p_1,\dots,p_r)\), is obtained as follows. Replace every \(y\in Y_j\) by a block
\[
B_y=\{y^{(1)},\dots,y^{(p_j)}\},
\]
with these clones placed in \(p_j\) separate vertex classes. Every edge
\[
\{y_1,\dots,y_r\}\in E(J)
\]
is replaced by the \(k\)-edge
\[
B_{y_1}\cup\cdots\cup B_{y_r}.
\]

Write \(\operatorname{ex}^{\square}_r(n,J)\) for the part-respecting extremal number in an \(r\)-partite host with each part of size at most \(n\).

## Theorem 3.1
For every \(J\) and \(\mathbf p\) as above,
\[
\operatorname{ex}^{\square}_k(n,J^{\mathbf p})
 \le n^{k-r}\operatorname{ex}^{\square}_r(n,J).
\]

Moreover, for every nonempty \(J\),
\[
d_{\max}(J)
 \le d_{\max}(J^{\mathbf p})
 \le C_k d_{\max}(J)
\]
for a constant \(C_k\) depending only on \(k\).

### Proof of the extremal inequality
Let the \(k\) host parts be grouped into \(r\) groups, with group \(j\) containing \(p_j\) parts. After padding, label every part by \(\mathbb Z_n\).

The Cartesian product of the \(p_j\) parts in group \(j\) decomposes into \(n^{p_j-1}\) perfect matchings:
\[
M_{\alpha_2,\dots,\alpha_{p_j}}
 =
 \{(x,x+\alpha_2,\dots,x+\alpha_{p_j}):x\in\mathbb Z_n\}.
\]
Distinct tuples in one such matching are vertex-disjoint in every coordinate.

Choose one matching in each of the \(r\) groups. These matchings form the vertex classes of an auxiliary \(r\)-partite \(r\)-graph: a collection of \(r\) tuple-nodes is an auxiliary edge precisely when the union of the corresponding blocks is an edge of the original \(k\)-graph.

There are
\[
\prod_{j=1}^r n^{p_j-1}=n^{k-r}
\]
such auxiliary hypergraphs, and their edge sets partition the edge set of the original host.

If one auxiliary hypergraph contains a part-respecting copy of \(J\), then its tuple-nodes lift to a copy of \(J^{\mathbf p}\). Injectivity follows because distinct tuple-nodes in each selected perfect matching are coordinatewise disjoint. Therefore every auxiliary hypergraph is \(J\)-free, proving
\[
e(G)\le n^{k-r}\operatorname{ex}^{\square}_r(n,J).
\]
∎

### Proof of the skeletal-degeneracy comparison
Choose one representative clone from every block. On these representatives, every \((i+1)\)-shadow of \(J\) appears as an induced shadow of \(J^{\mathbf p}\). Hence
\[
d_{\max}(J^{\mathbf p})\ge d_{\max}(J).
\]

For the reverse inequality, let \(U\subseteq V(J^{\mathbf p})\), and let \(W\subseteq V(J)\) consist of those original vertices whose blocks meet \(U\). Apply Lemma 2.1 to \(J[W]\), obtaining \(v\in W\) with all its skeletal degrees \(O_k(d_{\max}(J))\). Choose a clone \(x\in B_v\cap U\).

Every shadow face of \(J^{\mathbf p}[U]\) containing \(x\) has an underlying set \(T\subseteq W\), containing \(v\), which is itself contained in an edge of \(J\). For a fixed \(T\), there are at most \(2^k\) possible clone subsets. Therefore, for every \(i\),
\[
\deg_{\mathcal S_i(J^{\mathbf p})[U]}(x)
 \le
 2^k\left(
 1+\sum_{t=1}^{r-1}
 \deg_{\mathcal S_t(J)[W]}(v)
 \right)
 \le C_k d_{\max}(J).
\]
Taking the minimum over \(x\in U\) and then the maximum over \(U\) proves the upper bound. ∎

## Corollary 3.2: bipartite templates

Let \(B\) be any nonempty bipartite graph of graph degeneracy \(d\), and let \(p+q=k\). Replace every vertex in one side of \(B\) by a \(p\)-vertex block and every vertex in the other side by a \(q\)-vertex block; replace every graph edge by the union of its two blocks. Call the resulting \(k\)-graph \(B^{(p,q)}\).

The \(k=2\) case of the supplied Theorem 1.4 gives an absolute \(\gamma>0\) such that
\[
\operatorname{ex}^{\square}_2(n,B)
 =O_B\!\left(n^{2-\gamma/d}\right).
\]
A prescribed-side version follows either directly from the partite proof or by joining two oppositely oriented copies of \(B\) into one connected bipartite supergraph; this changes degeneracy by at most an absolute additive constant.

Theorem 3.1 now gives
\[
\operatorname{ex}_k(n,B^{(p,q)})
 =O_{B,k}\!\left(n^{k-\gamma'/d}\right)
\]
for an absolute \(\gamma'>0\). Furthermore,
\[
d\le d_{\max}(B^{(p,q)})\le C_kd.
\]
Consequently,
\[
\operatorname{ex}_k(n,B^{(p,q)})
 =O_{B,k}\!\left(
 n^{\,k-\gamma'/d_{\max}(B^{(p,q)})}
 \right).
\]

Thus Conjecture 6.2 holds, with the conjectured order of dependence on \(d_{\max}\), for every block expansion of every bipartite graph.

Passing from partite to ordinary extremal numbers only costs a \(k\)-dependent factor: a random \(k\)-coloring retains an expected \(k!/k^k\) fraction of all edges as crossing edges.

# 4. Cone and private-leaf extensions

Two further operations preserve any exponent already known in lower uniformity.

## Cone extension
For an \(r\)-graph \(J\), let \(C(J)\) be obtained by adding a new vertex \(a\) to every edge. Then
\[
\operatorname{ex}^{\square}_{r+1}(n,C(J))
 \le n\,\operatorname{ex}^{\square}_r(n,J).
\]

Indeed, in an \((r+1)\)-partite host, every vertex \(z\) of the last part has an \(r\)-uniform link. If the host is \(C(J)\)-free, every such link is \(J\)-free, and summing their sizes gives the inequality.

## Private-leaf extension
For every \(e\in E(J)\), fix \(t_e\ge1\). Introduce \(t_e\) new vertices
\[
z_{e,1},\dots,z_{e,t_e},
\]
all mutually distinct and lying in a new part, and add the edges
\[
e\cup\{z_{e,s}\}.
\]
Call the resulting \((r+1)\)-graph \(P_{\mathbf t}(J)\), and put
\[
h=\sum_{e\in E(J)}t_e.
\]

Then
\[
\operatorname{ex}^{\square}_{r+1}(n,P_{\mathbf t}(J))
 \le
 n\,\operatorname{ex}^{\square}_r(n,J)+(h-1)n^r.
\]

To prove this, for every crossing \(r\)-tuple \(x\), let \(c(x)\) be its number of extensions in the last part, and let
\[
Q=\{x:c(x)\ge h\}.
\]
If \(Q\) contained \(J\), the required private leaves could be selected greedily: at most \(h-1\) last-part vertices have already been used, while each required core edge has at least \(h\) extensions. Hence \(Q\) is \(J\)-free. Therefore
\[
e(G)=\sum_xc(x)
 \le (h-1)n^r+n|Q|
 \le (h-1)n^r+n\operatorname{ex}^{\square}_r(n,J).
\]

In both constructions, the old shadows of \(J\) occur as induced shadows on the old vertices, so
\[
d_{\max}(C(J)),\ d_{\max}(P_{\mathbf t}(J))
 \ge d_{\max}(J).
\]
Thus, if
\[
\operatorname{ex}_r(n,J)
 =O_J(n^{r-\eta}),\qquad 0<\eta\le1,
\]
then both extensions have extremal number
\[
O_H(n^{r+1-\eta}).
\]
In particular, any hypergraph obtained from a bipartite block expansion by repeatedly taking cones or adding private-leaf parts satisfies Conjecture 6.2. Private \(k\)-expansions of bipartite graphs are included.

# 5. Remaining gap

Lemma 2.1 shows that all the target skeletal degeneracies can be controlled in a single vertex order at cost only \(O_k(1)\). This does not by itself give a greedy embedding. Even if a target vertex is incident with only \(O_k(d_{\max})\) relevant boundary faces, the corresponding neighborhoods in a sparse host may have empty intersection.

The block-expansion argument avoids this issue by decomposing Cartesian products into disjoint diagonal matchings. Cone extensions reduce to one link, while private-leaf extensions require only distinct representatives. A general \(k\)-partite \(H\) may have vertices shared by a nontrivial proper subfamily of edges; lifting a shadow copy then requires genuinely simultaneous, multilevel common-neighborhood control. No argument above establishes such a lemma with cost \(O_k(d_{\max}(H))\), so the full conjecture remains open.