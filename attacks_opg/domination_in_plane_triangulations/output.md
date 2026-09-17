```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove gamma(G) <= floor(n/4+b/8), where b counts vertices with bipartite open neighborhoods, establishing the conjectured bound when b=0.",
  "would_publish": false,
  "caveats": "The general conjecture is not settled; novelty of this structural bound has not been checked."
}
```

## 1. A structural partial result

Let \(G\) be a finite simple plane triangulation with \(n\ge 4\) vertices. Write
\[
B(G)=\{v\in V(G):G[N(v)]\text{ is bipartite}\},
\qquad b=|B(G)|,
\]
where \(N(v)\) is the **open** neighborhood of \(v\).

I prove the following parameterized bound. I am not claiming that it is new.

**Theorem.**
\[
\boxed{\displaystyle
\gamma(G)\le \left\lfloor\frac n4+\frac b8\right\rfloor.}
\tag{1}
\]
More generally, if vertices have nonnegative costs \(w(v)\), then \(G\) has a dominating set \(D\) satisfying
\[
\boxed{\displaystyle
w(D)\le \frac{w(V(G))}{4}+\frac{w(B(G))}{8}.}
\tag{2}
\]

In particular, the conjectured bound holds whenever every open neighborhood is non-bipartite. An easily checked sufficient condition is:

> Every vertex either has odd degree or belongs to a copy of \(K_4\).

Thus the result includes all odd-degree plane triangulations and all stacked triangulations, as well as mixtures of these local conditions.

The proof uses the Four Color Theorem and a counting argument based on Kempe switches.

## 2. A switching lemma for proper four-colorings

Let \(\Omega\) be the set of all proper colorings
\[
f:V(G)\longrightarrow \{1,2,3,4\}.
\]
The Four Color Theorem guarantees that \(\Omega\ne\varnothing\).

Call a vertex \(v\) **colorful** in \(f\) if its closed neighborhood \(N[v]\) contains all four colors, and **deficient** otherwise.

The neighbors of every vertex of a plane triangulation occur in a cyclic order in which consecutive neighbors are adjacent. Consequently, every closed neighborhood contains at least three colors. A deficient vertex therefore sees exactly two colors on its open neighborhood. In particular,
\[
\{v:v\text{ is deficient in }f\}\subseteq B(G).
\tag{3}
\]

The useful point is that deficiency cannot occur in more than half of all proper four-colorings, at any fixed vertex.

**Lemma.** For every \(v\in V(G)\),
\[
|\{f\in\Omega:v\text{ is deficient}\}|
\le
|\{f\in\Omega:v\text{ is colorful}\}|.
\tag{4}
\]

### Proof

There is nothing to prove if \(v\) is never deficient. Otherwise, its degree is even, say \(2k\), with \(k\ge2\). Fix the cyclic ordering
\[
x_1,y_1,x_2,y_2,\ldots,x_k,y_k
\]
of its neighbors, and put
\[
A=\{x_1,\ldots,x_k\},\qquad B=\{y_1,\ldots,y_k\}.
\]

In any coloring in which \(v\) is deficient, the neighbor cycle alternates between two colors. Write these colors as \(a\) on \(A\) and \(b\) on \(B\), write \(c=f(v)\), and let \(d\) be the missing fourth color.

We construct an injection from deficient colorings to colorful colorings. Let \(H=G-v\).

A Kempe switch means interchanging two colors on a connected component of the subgraph induced by those colors.

### Case I: the \(a,d\)-component through \(x_1\) does not contain all of \(A\)

Let \(X\) be that component in \(H\), and interchange \(a\) and \(d\) on \(X\).

This preserves properness: \(v\) has color \(c\), which is neither switched color. Some vertices of \(A\), including \(x_1\), now have color \(d\), while other vertices of \(A\) retain color \(a\). The vertices of \(B\) retain color \(b\).

Thus \(N(v)\) contains \(a,b,d\), and \(v\), still colored \(c\), is colorful.

### Case II: the \(a,d\)-component through \(x_1\) contains all of \(A\)

Let \(Y\) be the \(b,c\)-component of \(H\) containing \(y_1\). I first claim that \(Y\) does not contain all of \(B\).

There is a simple \(a,d\)-colored path \(P\) in \(H\) joining \(x_1\) to \(x_2\). Together with \(vx_1\) and \(vx_2\), it forms a simple cycle. The cyclic ordering at \(v\) places \(y_1\) and \(y_2\) on opposite sides of this cycle: the edges \(vy_1\) and \(vy_2\) leave \(v\) on opposite sides and cannot meet the cycle elsewhere.

A \(b,c\)-colored path in \(H\) cannot meet this cycle. Its vertices cannot belong to \(P\), whose colors are \(a,d\), and it cannot use \(v\), which has been deleted. Planarity therefore excludes a \(b,c\)-colored path from \(y_1\) to \(y_2\). Hence \(y_2\notin Y\), proving the claim.

Now recolor \(v\) from \(c\) to \(d\), which is legal because \(d\) is absent from \(N(v)\). Interchange \(b\) and \(c\) on \(Y\). This is a legal Kempe switch after the recoloring of \(v\).

The set \(A\) remains monochromatic in color \(a\), while \(B\) now contains both \(b\) and \(c\). Since \(v\) has color \(d\), it is colorful.

### Injectivity

The two types of output are distinguishable:

- Case I produces an output in which \(A\) uses two colors and \(B\) is monochromatic.
- Case II produces an output in which \(A\) is monochromatic and \(B\) uses two colors.

For a Case I output, the original coloring is recovered by switching the two colors occurring on \(A\), on their component in \(H\) containing \(x_1\). A Kempe switch does not change the vertex set or connectivity of the corresponding two-color induced subgraph, so this uniquely reverses the operation.

For a Case II output, first switch the two colors occurring on \(B\), on their component in \(H\) containing \(y_1\). After this reversal, \(N(v)\) is again two-colored. Recolor \(v\) to the unique color absent from its current closed neighborhood. This uniquely recovers the original coloring.

Thus the map is injective, proving (4). \(\square\)

## 3. From colorings to dominating sets

Choose \(f\) uniformly from \(\Omega\), and let \(X(f)\) be its set of deficient vertices. By the lemma and (3),
\[
\mathbb P(v\in X(f))\le
\begin{cases}
1/2,&v\in B(G),\\
0,&v\notin B(G).
\end{cases}
\]
Therefore, for any nonnegative vertex costs,
\[
\mathbb E\,w(X(f))
\le \frac12 w(B(G)).
\tag{5}
\]
There exists a proper four-coloring \(f\) for which
\[
w(X(f))\le \frac12 w(B(G)).
\tag{6}
\]

Fix such a coloring and let
\[
C_i=f^{-1}(i),\qquad i=1,2,3,4.
\]
Define
\[
X_i=\{v:N[v]\cap C_i=\varnothing\},
\qquad
D_i=C_i\cup X_i.
\]
Each \(D_i\) is a dominating set: vertices not dominated by \(C_i\) are included in \(X_i\).

Every deficient vertex misses exactly one color, while every colorful vertex misses none. Thus the sets \(X_i\) partition \(X(f)\). Also \(C_i\cap X_i=\varnothing\). Consequently,
\[
\sum_{i=1}^4 w(D_i)
=
w(V(G))+w(X(f))
\le
w(V(G))+\frac12w(B(G)).
\]
At least one of these four dominating sets has cost at most one quarter of the right-hand side. This proves (2).

Taking \(w(v)=1\) for every vertex and using integrality proves (1). \(\square\)

## 4. Consequences for the conjecture

### 4.1. An exact \(n/4\) special case

The neighbors of a vertex \(v\) contain a cycle of length \(\deg(v)\). Hence odd degree implies that \(G[N(v)]\) is non-bipartite.

If \(v\) belongs to a \(K_4\), its neighborhood contains the triangle formed by the other three vertices, so again \(G[N(v)]\) is non-bipartite.

Therefore:

**Corollary.** If every vertex of a plane triangulation either has odd degree or belongs to a \(K_4\), then
\[
\gamma(G)\le \left\lfloor\frac n4\right\rfloor.
\]

In this case there is an especially direct interpretation: **every** proper four-coloring partitions \(V(G)\) into four dominating sets.

### 4.2. A small-exception extension

Write \(n=4q+r\), where \(0\le r\le3\). Bound (1) gives the conjectured inequality whenever
\[
b+2r\le7.
\tag{7}
\]
In particular, it holds if at most one vertex has a bipartite open neighborhood.

Conversely, any counterexample to \(\gamma(G)\le n/4\) must satisfy
\[
b\ge 8-2r.
\tag{8}
\]
This is only a local obstruction requirement, not a resolution of the conjecture.

For comparison with the general estimate quoted in the question, the unrounded bound in (1) is smaller than \(2n/7\) whenever
\[
b<\frac{2n}{7}.
\]

### 4.3. The coefficient \(1/4\) is sharp within the special case

The disjoint-\(K_4\) construction in the question already lies in the class \(b=0\).

For completeness, take \(m\) vertex-disjoint plane copies \(Q_1,\ldots,Q_m\) of \(K_4\), each with a vertex \(z_i\) inside the triangle formed by its other three vertices. Place the copies in disjoint regions and add noncrossing edges until the graph is a triangulation, without adding vertices.

No added edge can join \(z_i\) to a vertex outside \(Q_i\), because the enclosing triangle separates them. Thus
\[
N[z_i]=V(Q_i).
\]
These \(m\) closed neighborhoods are disjoint, so every dominating set contains at least \(m\) vertices.

Conversely, choosing one arbitrary vertex from each \(Q_i\) dominates all \(4m\) vertices. Hence
\[
\gamma(G)=m=\frac{|V(G)|}{4}.
\]
Every vertex belongs to one of the original \(K_4\)'s, so \(b=0\).

## 5. What remains unresolved

The error term \(b/8\) can be linear in \(n\); planarity does not force \(b\) to be small.

For an explicit example, take an even cycle \(C_{2k}\), \(k\ge2\), and add two nonadjacent poles, each adjacent to every cycle vertex, embedded on opposite sides of the cycle. This is a plane triangulation. Each pole has an even cycle as its induced neighborhood, while each cycle vertex has a \(4\)-cycle as its induced neighborhood. Therefore
\[
b=n.
\]
On this family, (1) gives only \(\gamma(G)\le\lfloor3n/8\rfloor\), although the two poles themselves form a dominating set.

Thus the argument proves the desired bound for a definite structural class and supplies a quantitative extension, but it does not address the conjecture adequately when a large proportion of vertices have bipartite open neighborhoods. No removal of that linear error term is established here.