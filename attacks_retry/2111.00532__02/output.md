```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Graph-power obstructions exclude an infinite family missed by the quoted degree bound, including a nine-vertex tree that passes every multicoloring test from the previous attempt.",
  "would_publish": false,
  "caveats": "No characterization or sufficiency theorem is obtained; novelty relative to the full source paper and subsequent literature is unverified."
}
```

# 1. Scope and conventions

I do not resolve the characterization. I prove stronger necessary conditions and use them to exclude an infinite family of trees.

A transversal copy is **induced**. A blockade of width \(W\) is \((\alpha W,\alpha W)\)-cohesive if no two distinct blocks contain anticomplete subsets both of size at least \(\alpha W\). All counterexample blockades constructed below have blocks of exactly \(W\) vertices.

The triangle-forcing construction in the supplied attempt checks out. The strengthening here is to use graph powers, which force closure along longer paths, not just paths of length two.

The results include:

* a necessary weighted-path condition;
* a strictly stronger version of the previous multicoloring condition;
* a necessary inequality involving several high-degree vertices;
* an infinite family \(T_d\), \(d\ge4\), with
  \[
  |T_d|=2^{d-1}+1,\qquad \Delta(T_d)=d,
  \]
  that does not have the strong transversal property.

Every \(T_d\) passes the matching-cut spectrum test from the previous attempt. The nine-vertex member also passes that attempt’s entire multicoloring test.

# 2. A graph-power obstruction

## Theorem 1: weighted-path necessary condition

Let \(H\) be a forest of order \(h\ge2\) with the strong transversal property. Assign a positive integer \(a_{ij}=a_{ji}\) to every pair of distinct elements of \([h]\).

Then there is a bijection
\[
\phi:V(H)\longrightarrow [h]
\]
such that, whenever \(u,v\) are distinct, nonadjacent vertices in the same component of \(H\),
\[
a_{\phi(u)\phi(v)}
<
\sum_{xy\in E(P_H(u,v))}a_{\phi(x)\phi(y)}.
\tag{1}
\]
Here \(P_H(u,v)\) denotes the unique \(u\)-\(v\) path.

### Sparse base graph

Fix \(0<\alpha<1/2\), and put
\[
L=\max_{i\ne j}a_{ij}.
\]
For a large integer \(m\), let
\[
W=m^{L+2},
\]
and take a random graph \(R\) on a set \(U\) of size \(W\), with edge probability \(m/W\).

With probability tending to one as \(m\to\infty\), the following hold:

1. \(\Delta(R)\le 2m\);
2. every two disjoint subsets of \(U\), each of size at least \(\alpha W\), have an edge between them.

Indeed, a Chernoff bound gives
\[
\Pr(\Delta(R)>2m)\le W e^{-m/3}=o(1).
\]
For the second assertion, put \(s=\lceil\alpha W\rceil\). For fixed disjoint \(s\)-element sets \(X,Y\),
\[
\Pr(E_R(X,Y)=\varnothing)
\le \exp(-\alpha^2mW).
\]
There are at most \(4^W\) ordered pairs of subsets, so the probability of any such empty pair is at most
\[
\exp\big((\log4-\alpha^2m)W\big)=o(1).
\]

Choose a realization with both properties. Every radius-\(L\) ball has size at most
\[
1+(2m)+\cdots +(2m)^L
\le 2(2m)^L
<\alpha W
\tag{2}
\]
for sufficiently large \(m\).

### The blockade graph

Make \(h\) disjoint copies \(B_1,\ldots,B_h\) of \(U\). Write \(\lambda(x)\in U\) for the label of a vertex in a block. Between distinct blocks, set
\[
xy\in E(G)
\quad\Longleftrightarrow\quad
\operatorname{dist}_R(\lambda(x),\lambda(y))\le a_{ij},
\qquad x\in B_i,\ y\in B_j.
\tag{3}
\]
Distance zero is allowed here: two copies of the same label are adjacent. Put no edges within blocks.

By (2), the local degree is less than \(\alpha W\).

To check cohesion, take \(X\subseteq B_i\) and \(Y\subseteq B_j\), each of size at least \(\alpha W\). If their label sets intersect, a pair of equal labels gives an edge. Otherwise, the base-graph property gives an \(R\)-edge between their label sets, which also gives a \(G\)-edge since \(a_{ij}\ge1\).

Thus this is an \((\alpha W,\alpha W)\)-cohesive blockade of local degree less than \(\alpha W\).

### Proof of the necessary condition

Suppose this graph contains an induced transversal copy of \(H\), and let \(\phi\) record its block assignment.

For a path \(u=v_0,v_1,\ldots,v_t=v\) in \(H\), the triangle inequality in \(R\) gives
\[
\operatorname{dist}_R(\lambda(u),\lambda(v))
\le
\sum_{r=1}^t a_{\phi(v_{r-1})\phi(v_r)}.
\]
If \(u,v\) are nonadjacent in the induced copy, (3) also gives
\[
\operatorname{dist}_R(\lambda(u),\lambda(v))
>a_{\phi(u)\phi(v)}.
\]
This proves (1).

The construction works for every sufficiently small positive \(\alpha\). In particular, if \(\varepsilon\) witnesses the strong transversal property, choose \(\alpha\le\varepsilon\). The constructed blockade then satisfies the conditions for \(\varepsilon\), and so must contain the required transversal. Hence some bijection satisfies (1). \(\square\)

# 3. A stronger multicoloring condition

For a coloring \(c:V(H)\to[q]\), let
\[
F_c=(V(H),\{uv\in E(H):c(u)\ne c(v)\})
\]
be the forest consisting of the cross-color edges.

## Corollary 2: rainbow-component condition

If a forest \(H\) of order \(h\) has the strong transversal property, then for every positive composition
\[
n_1+\cdots+n_q=h,
\]
there is a coloring \(c:V(H)\to[q]\) with
\[
|c^{-1}(i)|=n_i
\]
such that **every component of \(F_c\) is rainbow**: it contains at most one vertex of each color.

### Proof

Partition the block indices into groups of sizes \(n_1,\ldots,n_q\), and apply Theorem 1 with
\[
a_{ij}=
\begin{cases}
1,&i,j\text{ are in different groups},\\
h,&i,j\text{ are in the same group}.
\end{cases}
\]

Color each vertex by its assigned group. If a component of \(F_c\) contains distinct vertices \(u,v\) of the same color, their unique \(H\)-path consists entirely of cross-color edges. They cannot be adjacent in \(H\), since adding a monochromatic edge to this path would create a cycle.

The left side of (1) is therefore \(h\), while the right side is the path length, at most \(h-1\), a contradiction. \(\square\)

This implies the previous externally locally injective condition
\[
|N_H(v)\cap c^{-1}(j)|\le1
\qquad(j\ne c(v)).
\tag{4}
\]
Indeed, two such neighbors would give a component of \(F_c\) containing a repeated color.

For \(q=2\), the new condition is exactly the old matching-cut condition: every component of \(F_c\) has at most two vertices, so its edges form a matching. For \(q\ge3\), it is genuinely stronger; Section 6 gives an explicit certificate of strictness.

# 4. Hierarchical cuts and high-degree vertices

There is another useful consequence of Theorem 1.

## Lemma 3: hierarchical matching cuts

Let \(D\) be any rooted full binary tree with \(h\) leaves. If a forest \(H\) of order \(h\) has the strong transversal property, its vertices can be bijectively assigned to the leaves of \(D\) so that:

> At every internal node of \(D\), the edges of \(H\) between the leaf sets of its two children form a matching.

Consequently, the degree of a vertex of \(H\) is at most the depth of its assigned leaf.

### Proof

Index the leaves by \([h]\), give the root depth zero, and set
\[
a_{ij}=2^{\operatorname{depth}(\operatorname{lca}(i,j))}.
\]

Suppose a vertex \(v\) assigned to one child-subtree of a node \(z\) has two neighbors \(x,y\) assigned to the other. Then
\[
a_{\phi(v)\phi(x)}
=a_{\phi(v)\phi(y)}
=2^{\operatorname{depth}(z)},
\]
whereas
\[
a_{\phi(x)\phi(y)}
\ge2^{\operatorname{depth}(z)+1}.
\]
Since \(H\) is a forest, \(x,y\) are nonadjacent, contradicting (1).

Finally, the neighbors of a vertex are partitioned according to the ancestor that is their lowest common ancestor with its assigned leaf. At most one neighbor occurs at each ancestor. \(\square\)

In particular, if \(H\) has a vertex of degree \(d\), then
\[
h>2^{d-1}.
\tag{5}
\]
Otherwise, choose a full binary tree with \(h\) leaves and height at most \(d-1\). Such a tree is obtained from the complete height-\((d-1)\) binary tree by repeatedly replacing a sibling pair of leaves by its parent. Lemma 3 gives a contradiction.

Thus this construction recovers the degree obstruction quoted in the question. It also gives the following strengthening.

## Theorem 4: high-degree set inequality

Suppose a forest \(H\) of order \(h\) has the strong transversal property. Let \(\ell\ge1\), with \(2^\ell<h\), and let \(U\subseteq V(H)\) be a nonempty set of vertices all having degree at least \(\ell+1\). Put \(k=|U|\), and let \(e_H(U)\) be the number of edges with both ends in \(U\).

Then
\[
\boxed{
h\ge
2^\ell+\sum_{u\in U}d_H(u)-e_H(U)
-\sum_{j=0}^{\ell-1}\min(k,2^j).
}
\tag{6}
\]

### Proof

Start with the complete binary tree of height \(\ell\). Replace one leaf by any full binary tree having
\[
s=h-2^\ell+1
\]
leaves. Apply Lemma 3 to this hierarchy.

Let \(S\subseteq V(H)\) be the vertices assigned to the replacement subtree. Every leaf outside that subtree has depth \(\ell\), so
\[
U\subseteq S.
\]

The sibling subtrees encountered above the replacement subtree have respectively
\[
1,2,4,\ldots,2^{\ell-1}
\]
leaves. At each of these cuts, the cross-edges form a matching. Therefore
\[
e_H(U,V(H)\setminus S)
\le\sum_{j=0}^{\ell-1}\min(k,2^j).
\tag{7}
\]

Inside \(S\),
\[
\begin{aligned}
\sum_{u\in U}d_{H[S]}(u)
&=e(H[S])+e_H(U)-e_H(S\setminus U)\\
&\le s-1+e_H(U),
\end{aligned}
\tag{8}
\]
because \(H[S]\) is a forest. Combining (7) and (8), and using \(s-1=h-2^\ell\), proves (6). \(\square\)

### Two high-degree vertices

If \(u,v\) both have degree at least \(d\ge2\), apply (6) with \(\ell=d-1\) and \(U=\{u,v\}\); condition \(2^{d-1}<h\) follows from (5). Since
\[
\sum_{j=0}^{d-2}\min(2,2^j)=2d-3,
\]
we obtain
\[
\boxed{h\ge2^{d-1}+3-e_H(\{u,v\}).}
\tag{9}
\]

Thus:

* two adjacent vertices of degree at least \(d\) require
  \[
  h\ge2^{d-1}+2;
  \]
* two nonadjacent vertices of degree at least \(d\) require
  \[
  h\ge2^{d-1}+3.
  \]

These are stronger than the single-vertex degree obstruction.

# 5. An infinite excluded family

For \(d\ge4\), start with the double star whose adjacent centers \(u,v\) both have degree \(d\). It has \(2d\) vertices. Subdivide one pendant edge exactly
\[
s_d=2^{d-1}+1-2d
\]
times, and call the resulting tree \(T_d\). Here \(s_d\ge0\).

Then
\[
|T_d|=2^{d-1}+1,\qquad \Delta(T_d)=d,
\]
and \(u,v\) remain adjacent vertices of degree \(d\).

By (9), \(T_d\) does not have the strong transversal property.

The quoted degree obstruction does not detect any of these trees, since
\[
2^{\Delta(T_d)-1}=|T_d|-1.
\]

## They all pass the matching-cut spectrum test

Let
\[
\mathcal M(T)=
\{|S|:S\subseteq V(T),\ \partial_T(S)\text{ is a matching}\}.
\]
I claim
\[
\mathcal M(T_d)=\{0,1,\ldots,|T_d|\}
\qquad(d\ge4).
\tag{10}
\]

For \(d\ge5\), the subdivided pendant arm has
\[
L_d=s_d+1=2^{d-1}-2d+2
\]
vertices other than its center. Moreover,
\[
L_d\ge2^{d-2}=\left\lfloor\frac{|T_d|}{2}\right\rfloor.
\]
For every \(p\) up to this floor, take the terminal \(p\) vertices of that arm. Their boundary has at most one edge. Taking complements gives every remaining cardinality.

For \(d=4\), label the nine-vertex tree as follows:
\[
V(T_4)=\{u,v,a,b,x,y,c,d,e\},
\]
\[
E(T_4)=\{uv,ua,ub,ux,xy,vc,vd,ve\}.
\tag{11}
\]
Matching-boundary sets of sizes \(0,1,2,3,4\) are respectively
\[
\varnothing,\quad
\{y\},\quad
\{x,y\},\quad
\{x,y,c\},\quad
\{v,c,d,e\}.
\]
Their complements supply the other sizes. This proves (10).

# 6. The nine-vertex example passes all the previous multicoloring tests

The tree in (11) differs from the previous attempt’s nine-vertex example: here the degree-four centers are adjacent, and a **pendant** edge is subdivided.

## A short exclusion using the new condition

Suppose \(T_4\) had a coloring with three classes of size three satisfying Corollary 2.

Every vertex has at most one neighbor in each other color. Therefore each degree-four center has at least two neighbors of its own color. Since its color class has size three, it is adjacent to both other vertices of that class.

The centers \(u,v\) cannot have the same color: they would then have a common neighbor, creating a triangle. Say they have colors \(1,2\).

Each center has exactly two same-color neighbors and exactly two cross-color neighbors. One cross-color neighbor is the other center, so its remaining cross-color neighbor must have color \(3\). Call these neighbors \(z_u,z_v\). They are distinct, since \(T_4\) is a tree.

But
\[
z_u-u-v-z_v
\]
is a path in \(F_c\) whose two ends have color \(3\), contradicting the rainbow-component condition.

Thus just the composition \((3,3,3)\) in Corollary 2 excludes \(T_4\).

## Exhaustive certificate for the old condition

Nevertheless, \(T_4\) satisfies the externally locally injective condition (4) for **every** prescribed composition of \(9\).

Here is a complete certificate. A string such as \(uvab\) denotes the set \(\{u,v,a,b\}\); vertical bars separate color classes. Class sizes are considered up to permutation.

| Class sizes | Color classes satisfying (4) |
|---|---|
| \(9\) | \(V(T_4)\) |
| \(7,2\) | \(uvabcde\mid xy\) |
| \(6,3\) | \(uvabde\mid xyc\) |
| \(5,4\) | \(uabxy\mid vcde\) |
| \(5,2,2\) | \(uvacx\mid bd\mid ey\) |
| \(4,3,2\) | \(vcde\mid uax\mid by\) |
| \(3,3,3\) | \(vcd\mid uax\mid eby\) |
| \(3,2,2,2\) | \(bey\mid ux\mid vc\mid ad\) |
| \(8,1\) | \(V(T_4)\setminus\{y\}\mid y\) |
| \(6,2,1\) | \(uvbcde\mid xy\mid a\) |
| \(5,3,1\) | \(uabxy\mid vcd\mid e\) |
| \(4,4,1\) | \(uabx\mid vcde\mid y\) |
| \(4,2,2,1\) | \(vcde\mid ux\mid ay\mid b\) |
| \(3,3,2,1\) | \(vcd\mid uax\mid be\mid y\) |
| \(2,2,2,2,1\) | \(ux\mid vc\mid ad\mid be\mid y\) |

Only \(u,v,x\) need checking, since every other vertex is a leaf.

These rows cover every integer partition of \(9\) having zero or one singleton part. To cover the rest, use the following elementary observation:

> Replacing an entire color class by distinct singleton colors preserves (4).

For vertices outside that class, there was at most one neighbor in the original class. For vertices inside it, their former same-color neighbors now all receive different colors.

Given a partition with at least two singleton parts, merge all those singleton parts into one part, use the corresponding row with no singleton parts, and then split that class into singletons. Permuting colors handles ordered compositions.

Consequently, Corollary 2 is **strictly stronger** than the complete collection of multicoloring conditions proved in the supplied attempt—not merely stronger than its two-color specialization.

# 7. What remains unresolved

The proved progress is entirely on the necessary-condition side:

1. The weighted-path condition (1) is necessary for strong transversality.
2. The rainbow-component coloring condition is a strict strengthening of the supplied multicoloring obstruction.
3. Inequality (6) provides higher-order degree obstructions.
4. The trees \(T_d\) are counterexamples for every positive proposed cohesion parameter, not merely small computational examples.

I have not proved a converse to any of these conditions, nor characterized the forests having the strong transversal property. In particular, passing all weighted-path tests is not shown sufficient.

The arguments above are self-contained. I have not verified whether equivalent graph-power constructions or the resulting exclusions already occur in the full source paper or later literature, so I make no priority claim.