```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture is not resolved here, but it holds for every triangle-free graph of treewidth at most two, while every triangle-free outerplanar graph has fractional chromatic number at most 5/2.",
  "would_publish": false,
  "caveats": "The remaining planar case may have treewidth at least three and maximum degree at least five; no literature-priority claim is made for the special-case lemmas."
}
```

# 1. Statement and weighted formulation

Write
\[
F(n)=3-\frac{3}{n+1}=\frac{3n}{n+1}.
\]
The conjecture is that every \(n\)-vertex triangle-free planar graph \(G\) satisfies
\[
\chi_f(G)\le F(n).
\]

For a nonnegative vertex weight \(w\), let
\[
w(V)=\sum_{v\in V(G)}w(v),\qquad
\alpha_w(G)=\max\{w(I):I\subseteq V(G)\text{ independent}\}.
\]
LP duality gives
\[
\chi_f(G)=
 \max_{w\ge 0,\ w\ne0}\frac{w(V)}{\alpha_w(G)}.
\]
Consequently, the conjecture is equivalent to the following genuinely weighted assertion:

> For every nonnegative \(w\), there is an independent set \(I\) such that
> \[
> w(I)\ge \frac{n+1}{3n}\,w(V).
> \]

The Steinberg–Tovey bound only establishes this for uniform weights. Thus the independence-number theorem alone does not imply the fractional statement.

# 2. A bounded-treewidth partial result

## Theorem 2.1

Every triangle-free graph \(G\) of treewidth at most \(2\) satisfies
\[
\chi_f(G)\le \frac{3|V(G)|}{|V(G)|+1}.
\]

The main ingredient is a constant bound which does not use planarity.

## Lemma 2.2

Every triangle-free graph of treewidth at most \(2\) has an \(8\)-color \(3\)-fold coloring. In particular,
\[
\chi_f(G)\le \frac83.
\]

### Proof

A \(3\)-fold coloring with eight colors assigns to each vertex \(v\) a set
\[
S_v\in\binom{[8]}3
\]
such that \(S_u\cap S_v=\varnothing\) whenever \(uv\in E(G)\).

Complete \(G\) to a \(2\)-tree \(T\) on the same vertex set. View \(T\) as starting from one edge and repeatedly adding a new vertex adjacent to the two ends of an existing edge. We maintain the following stronger invariant for every edge \(xy\in E(T)\):
\[
\begin{cases}
S_x\cap S_y=\varnothing,&xy\in E(G),\\[2mm]
|S_x\cap S_y|=1,&xy\notin E(G).
\end{cases}
\tag{1}
\]

The initial edge is easily assigned two \(3\)-subsets satisfying the appropriate condition.

Suppose now that \(v\) is added on an existing edge \(xy\). The sets \(S_x,S_y\) have already been chosen.

* If both \(vx,vy\in E(G)\), then \(xy\notin E(G)\), since \(G\) is triangle-free. Thus \(|S_x\cap S_y|=1\), so \(|S_x\cup S_y|=5\). Set
  \[
  S_v=[8]\setminus(S_x\cup S_y).
  \]

* Suppose \(vx\in E(G)\) and \(vy\notin E(G)\).
  - If \(xy\in E(G)\), then \(S_x,S_y\) are disjoint. Choose one element of \(S_y\) and the two elements of \([8]\setminus(S_x\cup S_y)\).
  - If \(xy\notin E(G)\), choose one element of \(S_y\setminus S_x\) and two elements outside \(S_x\cup S_y\).

  In either case \(S_v\cap S_x=\varnothing\) and \(|S_v\cap S_y|=1\). The symmetric case is identical.

* If neither \(vx\) nor \(vy\) belongs to \(E(G)\):
  - If \(S_x,S_y\) are disjoint, choose one element from each and one element outside their union.
  - If \(|S_x\cap S_y|=1\), choose their common element and two elements outside their union.

  Then \(S_v\) meets each of \(S_x,S_y\) in exactly one element.

Thus (1) is preserved. At the end, adjacent vertices of \(G\) receive disjoint \(3\)-sets, proving the lemma. ∎

## Small orders

For completeness, the constant \(8/3\) is not sufficient when \(n<8\). The following elementary fact handles those cases.

### Lemma 2.3

Every triangle-free graph on at most seven vertices admits a homomorphism to \(C_5\), unless it is bipartite—in which case it admits a homomorphism to an edge.

### Proof

Only the nonbipartite case needs consideration. A shortest odd cycle has length \(5\) or \(7\).

Suppose first that \(G\) contains a \(5\)-cycle \(C=c_0c_1\cdots c_4c_0\). There are at most two vertices outside \(C\). For such a vertex \(x\), the set \(N_C(x)\) is independent in \(C_5\), and hence has size at most two. Under the identity map on \(C\):

* if \(N_C(x)=\varnothing\), \(x\) may receive any image;
* if \(N_C(x)=\{c_i\}\), \(x\) may be sent to \(c_{i-1}\) or \(c_{i+1}\);
* if \(N_C(x)=\{c_{i-1},c_{i+1}\}\), \(x\) must be sent to \(c_i\).

If the two outside vertices are adjacent, their neighborhoods on \(C\) are disjoint. A direct check of the above three possibilities shows that their allowed image sets contain adjacent vertices of \(C_5\). For example, if both have two neighbors on \(C\), disjointness of those two independent pairs forces their unique allowed images to be adjacent. Thus the map extends.

If the shortest odd cycle has length \(7\) and there is a chord, triangle-freeness forces the chord to join vertices at cyclic distance three; that chord produces a \(5\)-cycle, reducing to the preceding case. With no chord, the graph is \(C_7\), which maps to the closed walk
\[
0,1,2,3,4,0,1,0
\]
in \(C_5\). ∎

Since \(\chi_f(C_5)=5/2\), Lemma 2.3 gives \(\chi_f(G)\le5/2\) for nonbipartite graphs of orders \(5,6,7\). For \(n\le4\), a triangle-free graph is bipartite.

### Completion of Theorem 2.1

For \(n\ge8\),
\[
\frac83\le\frac{3n}{n+1},
\]
with equality at \(n=8\), so Lemma 2.2 applies. The cases \(n\le7\) follow from Lemma 2.3 and the elementary bipartite cases. ∎

This covers all triangle-free series-parallel graphs and allows arbitrarily large maximum degree, so it is not contained in the quoted maximum-degree-four result.

# 3. Stronger outerplanar bound

## Theorem 3.1

Every triangle-free outerplanar graph admits a homomorphism to \(C_5\). Consequently,
\[
\chi_f(G)\le\frac52.
\]

### Proof

First suppose \(G\) is a \(2\)-connected outerplane graph. Its weak dual is a tree. If \(G\) is a cycle, then:

* an even cycle maps to an edge of \(C_5\);
* an odd cycle has length at least five and maps to a closed walk in \(C_5\), obtained by traversing \(C_5\) once and inserting backtracks.

Otherwise, choose a leaf face in the weak dual. This face meets the rest of the graph in one edge \(st\); its remaining boundary is an \(s\)-\(t\) path \(P\), whose internal vertices have degree two. Since \(G\) is triangle-free, \(P\) has at least three edges.

Inductively map the graph obtained by deleting the internal vertices of \(P\) to \(C_5\). The images of \(s,t\) are adjacent. For every \(\ell\ge3\), \(C_5\) has a walk of length \(\ell\) between any prescribed adjacent pair:

* lengths \(3\) and \(4\) are immediate;
* a backtrack increases the length by two.

Use such a walk to map \(P\). This completes the induction.

For a general outerplanar graph, apply the result separately to each \(2\)-connected block. At a cutvertex, postcompose the coloring of a new block with an automorphism of \(C_5\) so that the two images of the cutvertex agree. Bridges map to edges of \(C_5\). ∎

For \(n\ge5\),
\[
\frac52\le \frac{3n}{n+1},
\]
and the smaller orders are bipartite or trivial. Thus Theorem 3.1 gives another complete special case of the conjecture.

# 4. Necessary structure of a minimal counterexample

The LP formulation gives several reductions that any full attack should exploit.

Assume \(G\) is a counterexample of minimum order \(n\).

## 4.1 Fractional criticality and positive dual weights

Since \(F(n)\) is strictly increasing, every proper induced subgraph \(H\) satisfies
\[
\chi_f(H)\le F(|V(H)|)<F(n)<\chi_f(G).
\]
Thus \(G\) is vertex-critical with respect to \(\chi_f\).

Let \(w\) be an optimal dual solution normalized by
\[
w(I)\le1\qquad\text{for every independent set }I.
\]
Then every \(w(v)\) is positive. Indeed, if \(S=\{v:w(v)>0\}\) were proper, the same dual solution would show
\[
\chi_f(G[S])\ge w(S)=\chi_f(G)>F(n)>F(|S|),
\]
contradicting minimality.

## 4.2 A small maximal independent set is forced

Let \(x_I\) be an optimal fractional coloring. Complementary slackness and positivity of every \(w(v)\) give
\[
\sum_{I\ni v}x_I=1\qquad(v\in V(G)).
\]
Hence
\[
\sum_I |I|x_I=n,
\qquad
\sum_I x_I=\chi_f(G).
\]
The average cardinality of an independent set used by this optimal coloring is therefore
\[
\frac{n}{\chi_f(G)}
<
\frac{n+1}{3}.
\]
Consequently, some \(I\) with \(x_I>0\) satisfies
\[
|I|<\frac{n+1}{3},
\qquad\text{hence}\qquad
|I|\le \left\lfloor\frac n3\right\rfloor.
\tag{2}
\]

Moreover, complementary slackness gives \(w(I)=1\). Since all vertex weights are positive, \(I\) must be maximal: otherwise \(I\cup\{v\}\) would be independent for some \(v\notin I\), and would have weight greater than one.

Thus:

> Every minimum counterexample contains an independent dominating set of size at most \(\lfloor n/3\rfloor\) which is tight for a full-support optimal dual weighting.

This is more restrictive than merely having a large maximum independent set, but I do not obtain a contradiction from it.

## 4.3 Connectivity, treewidth, and degrees

Fractional chromatic number is the maximum over components. It is also the maximum under a \(1\)-sum at a cutvertex: common \(b\)-fold colorings of the blocks can have the color set of the cutvertex aligned by permuting colors. Hence a minimum counterexample is \(2\)-connected.

The results above and the special case quoted in the question imply that such a counterexample must satisfy:

* \(n\ge8\);
* \(\operatorname{tw}(G)\ge3\), and hence \(G\) contains a \(K_4\)-minor;
* \(\Delta(G)\ge5\);
* \(\delta(G)\ge2\).

If \(n_i\) denotes the number of degree-\(i\) vertices, Euler's inequality \(m\le2n-4\) gives
\[
\sum_{v\in V(G)}(4-d(v))=4n-2m\ge8.
\]
Since there are no vertices of degree at most one,
\[
2n_2+n_3
\ge
8+\sum_{d\ge5}(d-4)n_d.
\tag{3}
\]
Thus every high-degree vertex forces additional degree-two or degree-three vertices. A successful full proof would likely need to combine (2), (3), and weighted reducibility around these low-degree vertices.

# 5. Exact computational test

For any fixed order, the conjecture can be checked exactly as follows.

1. Enumerate all simple graphs on \(n\) vertices, retaining only planar triangle-free graphs. One may additionally retain only \(2\)-connected graphs with \(\Delta\ge5\), treewidth at least three, and satisfying (3).
2. Enumerate all maximal independent sets \(I\). Constraints for nonmaximal independent sets are redundant for nonnegative weights.
3. Solve over exact rationals the LP
   \[
   \max \sum_{v}w_v
   \]
   subject to
   \[
   w_v\ge0,\qquad
   \sum_{v\in I}w_v\le1
   \quad\text{for every maximal independent set }I.
   \]
4. Compare the optimum with \(3n/(n+1)\).

An optimum larger than \(3n/(n+1)\), together with its rational weight vector and a planar embedding, would be an explicit counterexample. An upper-bound certificate is supplied by the dual fractional coloring. I have not executed this enumeration.

# 6. Remaining gap

The full weighted inequality remains unproved for planar triangle-free graphs of treewidth at least three and maximum degree at least five. The unweighted bound
\[
\alpha(G)\ge\frac{n+1}{3}
\]
only treats the uniform dual weighting, whereas a counterexample may be witnessed by a highly nonuniform positive weighting. The bounded-treewidth colorings above do not control this remaining case, and the existence of the small tight maximal independent set in (2) does not by itself contradict planarity.