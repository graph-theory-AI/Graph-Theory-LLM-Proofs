```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds with explicit bounds for chordal graphs, cactus graphs, and more generally graphs whose blocks are chordal or cycles, and it is equivalent to the existence of growth-preserving chordal completions.",
  "would_publish": false,
  "caveats": "The general growth-preserving completion step remains open; the argument assumes finite simple graphs and the source paper's hereditary radius-growth definition."
}
```

# Mathematical writeup

## 1. Statement and conventions

For a graph \(G\), write
\[
f_G(r)=\max\bigl\{|V(H)|:H\subseteq G,\ \operatorname{rad}(H)\le r\bigr\}.
\]
This is the hereditary radius-growth function used in the source paper. Two consequences used repeatedly are:

1. If \(H\subseteq G\), then
   \[
   f_H(r)\le f_G(r).
   \]
2. Every ambient ball \(B_G(v,r)\) has at most \(f_G(r)\) vertices.

An embedding \(G\subseteq T\boxtimes K_k\) is equivalent to a partition
\[
V(G)=\bigsqcup_{t\in V(T)} B_t
\]
such that \(|B_t|\le k\) and every edge of \(G\) has its endpoints either in the same bag or in bags indexed by adjacent vertices of \(T\). I use this tree-partition formulation below.

The full conjecture is not proved. I establish several nontrivial special cases and an exact reformulation.

---

## 2. A normal-spanning-tree criterion

### Lemma 2.1
Let \(G\) be connected, and let \(F\subseteq G\) be a rooted spanning tree. Suppose:

- \(\Delta(F)\le D\);
- \(f_F(r)\le ar\);
- for every edge \(xy\in E(G)\), one endpoint is an ancestor of the other in \(F\), and
  \[
  d_F(x,y)\le L.
  \]

Then there is a tree \(R\) such that
\[
G\subseteq R\boxtimes K_M,
\qquad
M\le 1+D+\cdots+D^{L-1},
\]
and
\[
f_R(r)\le aLr.
\]

#### Proof
Partition \(V(F)\) into the connected components of the depth slabs
\[
\{qL,qL+1,\dots,(q+1)L-1\},\qquad q\ge0.
\]
Each part is a connected subtree of height at most \(L-1\), so it has at most
\[
1+D+\cdots+D^{L-1}
\]
vertices.

Contract each part to one vertex. Since \(F\) is a tree, the quotient \(R\) is a tree. If \(xy\in E(G)\), then \(x,y\) are ancestor-related and their depths differ by at most \(L\). Hence their slab-parts are equal or adjacent in \(R\). Thus these parts form a tree-partition of \(G\) of width at most \(M\).

For every part \(A\), choose its unique vertex \(\rho(A)\) of minimum depth. If \(A,B\) are adjacent in \(R\), then
\[
d_F(\rho(A),\rho(B))\le L.
\]
Consequently,
\[
d_F(\rho(A),\rho(B))\le L\,d_R(A,B)
\]
for arbitrary \(A,B\in V(R)\). The chosen representatives of an \(R\)-ball of radius \(r\) therefore lie in an \(F\)-ball of radius \(Lr\). They are distinct, so
\[
|B_R(A,r)|\le f_F(Lr)\le aLr.
\]
Any radius-\(r\) subgraph of a tree is contained in a radius-\(r\) ball, proving the growth bound. ∎

---

## 3. The conjecture for chordal graphs

### Theorem 3.1
Let \(c>1\), set \(D=\lceil c\rceil\), and let \(G\) be a connected chordal graph satisfying
\[
f_G(r)\le cr.
\]
Then
\[
G\subseteq T\boxtimes K_{D^D}
\]
for some tree \(T\) with
\[
f_T(r)\le cDr.
\]

#### Proof
First,
\[
\deg_G(v)+1\le f_G(1)\le c,
\]
so \(\Delta(G)\le D\).

Take a perfect elimination ordering
\[
v_1,v_2,\dots,v_n.
\]
For every \(v_i\) having a later neighbor, let \(p(v_i)\) be its later neighbor of smallest index. The edges \(v_ip(v_i)\) form a forest \(F\), called the elimination forest. Since these are edges of \(G\), \(F\subseteq G\).

We need two standard properties, for which a short proof is included. Suppose \(v_iv_j\in E(G)\) with \(i<j\). Starting at \(x_0=v_i\), repeatedly put \(x_{s+1}=p(x_s)\). As long as \(x_s\ne v_j\), the vertex \(v_j\) is a later neighbor of \(x_s\), so the index of \(p(x_s)\) is at most \(j\). Moreover \(p(x_s)\) and \(v_j\) are both later neighbors of \(x_s\), and hence are adjacent by the perfect-elimination property. Thus the process eventually reaches \(v_j\). Therefore:

- \(v_j\) is an ancestor of \(v_i\) in \(F\);
- every vertex before \(v_j\) on this parent path is adjacent to \(v_j\).

It follows that
\[
d_F(v_i,v_j)\le \deg_G(v_j)\le D.
\]
Also, every edge of \(G\) has both endpoints in one component of \(F\). Since \(G\) is connected, \(F\) is a spanning tree.

Finally, \(F\subseteq G\), so
\[
f_F(r)\le f_G(r)\le cr.
\]
Apply Lemma 2.1 with \(a=c\), \(L=D\), and maximum degree at most \(D\). The resulting bag size is at most
\[
1+D+\cdots+D^{D-1}\le D^D,
\]
and the quotient tree has growth at most \(cDr\). ∎

Thus Conjecture 14 is true for the entire class of chordal linear-growth graphs, with explicit functions
\[
g(c)=\lceil c\rceil^{\lceil c\rceil},
\qquad
h(c)=c\lceil c\rceil
\]
in the connected case.

---

## 4. A rooted lifting criterion

The next lemma is useful for graphs assembled from blocks.

### Lemma 4.1
Let \(G\) have a tree-partition \((T,\{B_t\})\) of width \(k\), and root \(T\). Suppose there is \(A\ge1\) such that whenever \(y\) is a descendant of \(x\), there are vertices
\[
u\in B_x,\qquad v\in B_y
\]
with
\[
d_G(u,v)\le A\,d_T(x,y).
\]
If \(f_G(r)\le cr\), then
\[
f_T(r)\le 2kcAr.
\]

#### Proof
For \(x\in V(T)\), let \(T_x\) be the descendant subtree rooted at \(x\). If \(y\in T_x\) and \(d_T(x,y)\le R\), choose a corresponding vertex \(v_y\in B_y\) lying within distance \(AR\) in \(G\) of one of the at most \(k\) vertices of \(B_x\). Distinct tree nodes have disjoint bags, so the chosen \(v_y\)'s are distinct. Hence
\[
|B_{T_x}(x,R)|
 \le \sum_{u\in B_x}|B_G(u,AR)|
 \le kcAR.
\]

Now consider an arbitrary \(T\)-ball \(B_T(z,r)\). Let \(x\) be the ancestor of \(z\) at distance \(\min\{r,\operatorname{depth}(z)\}\). Every vertex of \(B_T(z,r)\) is a descendant of \(x\) and is at distance at most \(2r\) from \(x\). Therefore
\[
|B_T(z,r)|\le kcA(2r)=2kcAr.
\]
This bounds \(f_T(r)\). ∎

---

## 5. The conjecture for cactus graphs

Recall that a cactus is a graph whose blocks are edges or cycles.

### Theorem 5.1
Let \(G\) be a connected cactus satisfying \(f_G(r)\le cr\). Then
\[
G\subseteq T\boxtimes K_2
\]
for a tree \(T\) satisfying
\[
f_T(r)\le 4cr.
\]

#### Construction
Root the block-cut tree of \(G\) at an arbitrary vertex \(o\).

For a bridge \(av\), where \(a\) is the articulation on the root side, create one new host-tree node adjacent to the node containing \(a\), and put \(v\) in its bag.

For a cycle block
\[
C=a v_1v_2\cdots v_{\ell-1}a,
\]
where \(a=v_0\) is the articulation on the root side, let
\[
m=\left\lfloor\frac{\ell}{2}\right\rfloor.
\]
Create a host path
\[
w_0w_1\cdots w_m,
\]
identifying \(w_0\) with the already existing node containing \(a\), and put
\[
v_i,\ v_{\ell-i}\in B_{w_i}\qquad(1\le i\le m),
\]
with only one vertex at \(w_m\) when \(\ell\) is even.

Child blocks rooted at either vertex in a two-vertex bag are attached as separate branches at that host node. Inductively replacing every block in this way produces a tree \(T\). Every bag has at most two vertices.

For a cycle edge, the sequence of host coordinates is
\[
w_0,w_1,\dots,w_m,\dots,w_1,w_0,
\]
so consecutive cycle vertices map to equal or adjacent host nodes. Bridges are also represented by host edges. Hence this is a tree-partition of width two.

#### Growth of the host tree
Root \(T\) at the node containing \(o\). The construction has the following path-lifting property:

> If \(y\) is a descendant of \(x\), then there are \(u\in B_x\) and \(v\in B_y\) with
> \[
> d_G(u,v)\le d_T(x,y).
> \]

Indeed, along a folded cycle path \(w_i,\dots,w_j\), a prescribed endpoint in
\[
B_{w_j}=\{v_j,v_{\ell-j}\}
\]
determines one of the two corresponding cycle arcs, beginning at the matching vertex in \(B_{w_i}\). On entering a child block at a cutvertex, the same argument restarts. Thus a directed host-tree path can be lifted, after choosing the appropriate one of the at most two starting vertices, to a graph path of the same length.

Lemma 4.1 with \(k=2\) and \(A=1\) gives
\[
f_T(r)\le 4cr.
\]
∎

This handles arbitrarily many cycles; in particular, the number of cycles is not required to be bounded.

---

## 6. A somewhat broader blockwise result

The preceding construction extends to graphs whose blocks are either cycles or chordal graphs.

### Theorem 6.1
Let \(G\) be connected, every block of \(G\) be either chordal or a cycle, and \(f_G(r)\le cr\). Put \(D=\lceil c\rceil\). Then
\[
G\subseteq T\boxtimes K_{D^D}
\]
for a tree \(T\) with
\[
f_T(r)\le 4cD^{D+1}r.
\]

#### Argument
For every chordal block \(B\) and any prescribed articulation \(a\in V(B)\), one can choose a perfect elimination ordering ending at \(a\). This follows inductively from the elementary fact that a noncomplete chordal graph has two nonadjacent simplicial vertices.

Construct the elimination tree rooted at \(a\), but partition it into:

- the singleton root bag \(\{a\}\);
- connected components of depth slabs \(1,\dots,D\), then \(D+1,\dots,2D\), and so on.

As in Theorem 3.1, these bags have size at most \(D^D\), and they form a tree-partition of the block.

Moreover, if \(X\) is an ancestor of \(Y\) in this block-host and \(v\in B_Y\) is prescribed, then for \(X\ne Y\) there is \(u\in B_X\) such that
\[
d_B(u,v)\le 2D\,d_T(X,Y).
\]
To see this, use the minimum-depth representative of \(X\), move in the elimination tree to the minimum-depth representative of \(Y\), at cost at most \(D\,d_T(X,Y)\), and then move inside the final depth slab to \(v\), at additional cost at most \(D-1\).

For a cycle block rooted at an articulation, the folded construction from Theorem 5.1 has the same prescribed-endpoint property with constant \(1\).

Now root the block-cut tree of \(G\). Identify the singleton root node of each child-block host with the existing host node containing its parent articulation. No new vertex is added to that bag. The resulting host remains a tree and has bag size at most \(D^D\).

A directed host path passes successively through local block hosts. At every intermediate block, prescribe the articulation through which the path enters the next block. The root bag of a child block is the singleton containing that articulation, so the local paths concatenate in \(G\). Hence the global tree-partition satisfies Lemma 4.1 with
\[
k=D^D,\qquad A=2D.
\]
Therefore
\[
f_T(r)\le 2(D^D)c(2D)r
       =4cD^{D+1}r.
\]
∎

For pure cactus graphs, Theorem 5.1 gives much better constants.

---

## 7. Disconnected graphs

The preceding theorems were stated for connected graphs. The extension to finite disconnected graphs costs only a constant factor in the host growth.

### Lemma 7.1
Suppose \(T_1,\dots,T_s\) are finite trees with
\[
f_{T_i}(r)\le ar.
\]
There is a tree \(T\) containing disjoint copies of all \(T_i\) such that
\[
f_T(r)\le (3a+4)r.
\]

#### Proof sketch
Let \(n_i=|V(T_i)|\), choose a root \(\rho_i\in V(T_i)\), and take a path with marked vertices \(p_i\) in order satisfying
\[
d(p_i,p_{i+1})=n_i+n_{i+1}+1.
\]
Attach \(\rho_i\) to \(p_i\).

For a ball of radius \(r\) centered on the connecting path, the marked points it meets are consecutive. Except for the first and last attached trees, the sum of the orders of all fully encountered trees is at most \(r\), by the spacing rule. Each of the two endpoint trees contributes at most \(ar\), and the connecting path contributes at most \(3r\). Thus such a ball has at most \((2a+4)r\) vertices.

If the center lies inside some \(T_i\), its intersection with that tree has at most \(ar\) vertices, and the part beyond the connecting path is bounded as above. This gives \((3a+4)r\). ∎

Consequently:

- for arbitrary finite chordal \(G\), one may take
  \[
  g(c)=D^D,\qquad h(c)=3cD+4;
  \]
- for arbitrary finite cactus \(G\), one may take
  \[
  g(c)=2,\qquad h(c)=12c+4.
  \]

The unused connector nodes cause no difficulty for a subgraph embedding.

---

## 8. Another special case: bounded cyclomatic number

There is also a useful folding operation.

Suppose \(G_0\subseteq T\boxtimes K_k\), and add one edge \(xy\), where \(x,y\) currently lie over \(a,b\in V(T)\). Fold the path
\[
a=p_0,p_1,\dots,p_\ell=b
\]
by identifying
\[
p_i\quad\text{with}\quad p_{\ell-i}.
\]
Keep all components attached off this path distinct, attaching both sides to the corresponding folded path node. The resulting graph \(T'\) is still a tree, every fiber of \(T\to T'\) has size at most two, and the images of \(a,b\) coincide. Thus the new graph embeds in
\[
T'\boxtimes K_{2k}.
\]

Moreover,
\[
f_{T'}(r)\le 2f_T(r).
\]
Indeed, \(T'\) is the union of two subtrees, each isomorphic to a subtree of \(T\), corresponding to the two halves of the folded path. The intersection of any \(T'\)-ball with either half is contained in a radius-\(r\) ball of that half.

Starting with a spanning tree of a connected graph and folding once for every non-tree edge gives:

### Proposition 8.1
If a connected graph \(G\) has cyclomatic number
\[
q=|E(G)|-|V(G)|+1
\]
and \(f_G(r)\le cr\), then
\[
G\subseteq T\boxtimes K_{2^q}
\]
for a tree \(T\) with
\[
f_T(r)\le 2^qcr.
\]

This is not enough for the full conjecture, since \(q\) is not bounded in terms of \(c\); for example, a chain of triangles has bounded linear growth but unbounded cyclomatic number.

---

## 9. Exact reformulation by chordal completions

The chordal special case yields a useful equivalence.

### Proposition 9.1
Conjecture 14 is equivalent, up to composition of the bounding functions, to the following assertion:

> There exists a function \(A\) such that every graph \(G\) with \(f_G(r)\le cr\) has a chordal supergraph \(H\) on the same vertex set satisfying
> \[
> f_H(r)\le A(c)r.
> \]

#### Proof

**Conjecture \(\Rightarrow\) chordal completion.**  
Suppose
\[
G\subseteq T\boxtimes K_{g(c)}
\]
and \(f_T(r)\le h(c)r\). On the image of \(V(G)\), add every edge supplied by the ambient product, obtaining an induced subgraph \(H\) of \(T\boxtimes K_{g(c)}\).

The graph \(T\boxtimes K_k\) is a tree with each vertex replaced by a clique and every tree edge replaced by a complete join. It is chordal: the vertices in a leaf fiber are simplicial, and induction on the tree proves chordality. Hence \(H\) is chordal.

If \(Q\subseteq H\) has radius at most \(r\), then its projection lies in a radius-\(r\) ball of \(T\), with at most \(g(c)\) vertices above each tree node. Thus
\[
|V(Q)|\le g(c)f_T(r)\le g(c)h(c)r.
\]

**Chordal completion \(\Rightarrow\) conjecture.**  
If \(H\supseteq G\) is chordal and \(f_H(r)\le A(c)r\), apply Theorem 3.1, and Lemma 7.1 if necessary, to \(H\). Then \(H\), and hence \(G\), embeds in a bounded clique blow-up of a linear-growth tree. ∎

Thus the unresolved core can be phrased as constructing a chordal completion without destroying hereditary linear growth.

---

## 10. Why the general case is still open

One cannot simply take the tree from the existing bounded tree-partition theorem and infer that it has linear growth.

For example, let \(U\) be a finite complete binary tree and list the vertices encountered by an Euler tour of \(U\). Consecutive terms form a path \(P\), and each vertex of \(U\) occurs at most three times. Hence
\[
P\subseteq U\boxtimes K_3.
\]
The path \(P\) has uniformly linear growth, while \(U\) has exponential balls. Every edge of \(U\) is supported by an edge of \(P\), so merely deleting unused host edges also does not fix the problem.

The chordal and cactus arguments avoid this artificial branching in different ways:

- chordal graphs admit an elimination tree whose every graph edge has bounded span;
- cactus cycles can be folded with only two coherent “sheets”, giving a rooted path-lifting property.

For a general bounded-treewidth linear-growth graph, overlapping long cycles can create neither a bounded-span elimination tree nor an evident bounded-sheet block folding. Equivalently, I do not have a construction of the growth-preserving chordal completion in Proposition 9.1. That is the remaining gap.