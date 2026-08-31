```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sparse-incidence construction gives a new necessary multicoloring condition and shows that a nine-vertex subdivided double star does not have the strong transversal property.",
  "would_publish": false,
  "caveats": "This is only a necessary condition; sufficiency and exact overlap with the full source paper remain unchecked."
}
```

# 1. Statement and conventions

I use the standard interpretation that a \(\mathcal B\)-transversal copy is induced, and that an \((a,b)\)-cohesive blockade has no anticomplete pair \(X\subseteq B_i\), \(Y\subseteq B_j\) in distinct blocks with \(|X|\ge a\), \(|Y|\ge b\). All blocks below are equicardinal of width \(W\).

The main partial result is a finite coloring obstruction.

For a coloring \(c:V(H)\to[q]\), say that \(c\) is **externally locally injective** if

\[
\left|N_H(v)\cap c^{-1}(j)\right|\le 1
\qquad
\text{for every }v\in V(H)\text{ and every }j\ne c(v).
\tag{1}
\]

## Theorem 1: incidence-color obstruction

Let \(H\) be a forest of order \(h\). If \(H\) has the strong transversal property, then for every \(q\in\{2,\ldots,h\}\) and every positive composition

\[
n_1+\cdots+n_q=h,
\]

there is an externally locally injective coloring \(c:V(H)\to[q]\) satisfying

\[
|c^{-1}(i)|=n_i\qquad (1\le i\le q).
\tag{2}
\]

For \(q=2\), this has a particularly simple interpretation. If \(S=c^{-1}(1)\), then (1) says exactly that the edge boundary

\[
\partial_H(S)=\{xy\in E(H):x\in S,\ y\notin S\}
\]

is a matching. Consequently:

> **Corollary 2.** If a forest \(H\) has the strong transversal property, then for every \(p\in\{1,\ldots,h-1\}\), there is a set \(S\subseteq V(H)\) with \(|S|=p\) such that \(\partial_H(S)\) is a matching.

The proof is by a sparse incidence construction.

# 2. Sparse incidence systems

## Lemma 3

Fix \(q\ge2\) and \(0<\alpha<1/2\). There are sets \(U_1,\ldots,U_q\), each of size \(W\), and, for every \(1\le i<j\le q\), a bipartite graph \(R_{ij}\) between \(U_i\) and \(U_j\), such that:

1. every vertex has degree at most \(2m\) in each \(R_{ij}\);
2. every \(X\subseteq U_i\) and \(Y\subseteq U_j\) with
   \[
   |X|,|Y|\ge \alpha W
   \]
   have at least one edge between them;
3. \(W=m^5\), where \(m\) can be chosen arbitrarily large.

### Proof

Let \(W=m^5\), and construct each \(R_{ij}\) independently by putting every possible edge in with probability

\[
\rho=m^{-4}.
\]

Every degree has distribution \(\operatorname{Bin}(W,\rho)\), with mean

\[
\rho W=m.
\]

By a Chernoff bound,

\[
\Pr(\deg>2m)\le e^{-m/3}.
\]

There are only \(2\binom q2 W\) relevant degrees, so the probability that any degree exceeds \(2m\) tends to zero as \(m\to\infty\).

Now put \(s=\lceil\alpha W\rceil\). For fixed \(X,Y\) of size \(s\),

\[
\Pr(E_{R_{ij}}(X,Y)=\varnothing)
=(1-\rho)^{s^2}
\le \exp(-\rho s^2)
\le \exp(-\alpha^2m^6).
\]

There are at most \(4^W\) choices for the ordered pair \((X,Y)\). Hence

\[
\Pr(\text{some empty }s\times s\text{ pair})
\le
\binom q2
\exp\big((\log 4)m^5-\alpha^2m^6\big),
\]

which also tends to zero. Thus, for all sufficiently large \(m\), a realization satisfying both assertions exists. \(\square\)

# 3. Construction of the counterexample blockades

Fix a positive composition \(n_1+\cdots+n_q=h\). Make \(n_i\) blocks of type \(i\). Every block of type \(i\) is a disjoint copy of \(U_i\); write \(\lambda(x)\in U_i\) for the label of a vertex \(x\) in such a block.

For vertices \(x,y\) in distinct blocks, define adjacency as follows.

* If \(x\) has type \(i\) and \(y\) has type \(j\ne i\), then
  \[
  xy\in E(G)
  \quad\Longleftrightarrow\quad
  \lambda(x)\lambda(y)\in E(R_{ij}).
  \tag{3}
  \]

* If \(x,y\) both have type \(i\), then
  \[
  xy\in E(G)
  \]
  if and only if there are some \(j\ne i\) and \(z\in U_j\) such that both
  \[
  \lambda(x)z,\lambda(y)z\in E(R_{ij}).
  \tag{4}
  \]

Thus, between two blocks of the same type we use the union of the half-squares of the incidence graphs \(R_{ij}\).

## Local degree

Between blocks of different types, the local degree is at most \(2m\).

Between two blocks of type \(i\), a fixed label \(x\in U_i\) has, for each \(j\ne i\), at most \(2m\) choices for the common neighbor \(z\), and each such \(z\) has at most \(2m\) neighbors in \(U_i\). Hence the degree into any same-type block is at most

\[
4(q-1)m^2.
\]

Since \(W=m^5\), for sufficiently large \(m\),

\[
\max\{2m,4(q-1)m^2\}<\alpha W.
\tag{5}
\]

Thus the local degree is less than \(\alpha W\).

## Cohesion

For two blocks of different types, cohesion follows directly from Lemma 3.

Suppose instead that \(B,B'\) both have type \(i\), and let \(X\subseteq B\), \(Y\subseteq B'\) have size at least \(\alpha W\). Choose any \(j\ne i\). By Lemma 3,

\[
|U_j\setminus N_{R_{ij}}(\lambda(X))|<\alpha W
\]

and similarly

\[
|U_j\setminus N_{R_{ij}}(\lambda(Y))|<\alpha W.
\]

Because \(\alpha<1/2\), the two neighborhoods in \(U_j\) intersect. Thus some \(x\in X\) and \(y\in Y\) have a common \(R_{ij}\)-neighbor, and so \(xy\in E(G)\) by (4). The blockade is therefore \((\alpha W,\alpha W)\)-cohesive.

# 4. Proof of Theorem 1

Suppose a \(\mathcal B\)-transversal induced copy of the forest \(H\) exists in the graph just constructed. Color each vertex of \(H\) by the type of the block containing its image. This coloring has the prescribed class sizes \(n_1,\ldots,n_q\).

Let \(v\in V(H)\), and suppose it has two neighbors \(x,y\) of the same color \(j\ne c(v)=i\). By (3), the images of both \(x\) and \(y\) are \(R_{ij}\)-adjacent to the label of the image of \(v\). Therefore the images of \(x\) and \(y\) have a common \(R_{ij}\)-neighbor. By (4), they are adjacent in \(G\).

But \(H\) is a forest, so two neighbors of \(v\) cannot be adjacent. This contradicts that the copy is induced. Hence the induced coloring must satisfy (1).

Therefore, if no coloring satisfying (1)–(2) exists, the construction gives, for every \(\alpha>0\), a cohesive blockade of local degree less than \(\alpha W\) with no transversal copy of \(H\). Taking \(\alpha\le\varepsilon\) shows that no \(\varepsilon\) can witness the strong transversal property. This proves Theorem 1. \(\square\)

# 5. An explicit additional negative tree

Let \(T\) be the nine-vertex tree with vertices

\[
\{u,x,v,a_1,a_2,a_3,b_1,b_2,b_3\}
\]

and edges

\[
ux,\quad xv,\quad ua_i\ (1\le i\le3),\quad vb_i\ (1\le i\le3).
\]

Thus \(u\) and \(v\) have degree four, are at distance two, and each has three pendant leaves. Equivalently, \(T\) is obtained from the double star with three leaves at each center by subdividing its central edge once.

## Proposition 4

The tree \(T\) does not have the strong transversal property.

### Proof

I show that \(T\) has no three-vertex set \(S\) whose edge boundary is a matching.

Suppose \(|S|=3\) and \(\partial_T(S)\) is a matching.

* If \(u\in S\), then at most one edge incident with \(u\) can leave \(S\). Since \(d(u)=4\), at least three neighbors of \(u\) must also belong to \(S\), giving \(|S|\ge4\), a contradiction. Hence \(u\notin S\). Similarly, \(v\notin S\).

* If \(x\in S\), then both \(xu\) and \(xv\) belong to \(\partial_T(S)\), and they meet at \(x\), contradicting that the boundary is a matching. Hence \(x\notin S\).

Thus \(S\) consists only of leaves. At most one of \(a_1,a_2,a_3\) can belong to \(S\), since two such leaves would give two boundary edges meeting at \(u\). Similarly, at most one of \(b_1,b_2,b_3\) belongs to \(S\). Therefore \(|S|\le2\), again a contradiction.

Corollary 2, with \(p=3\), now implies that \(T\) does not have the strong transversal property. \(\square\)

This example is not detected by the degree obstruction quoted in the prompt:

\[
|T|=9,\qquad \Delta(T)=4,\qquad 2^{\Delta(T)-1}=8<9.
\]

In particular, the incidence-color obstruction strictly strengthens that quoted negative test. The tree \(T\) is also a caterpillar, with spine \(u-x-v\); thus any positive caterpillar result must impose additional restrictions excluding this configuration.

# 6. Effective test for the two-color obstruction

For a forest \(H\), define its matching-cut spectrum

\[
\mathcal M(H)=
\{|S|:S\subseteq V(H),\ \partial_H(S)\text{ is a matching}\}.
\]

Corollary 2 says that strong transversality requires

\[
\mathcal M(H)=\{0,1,\ldots,|H|\}.
\tag{6}
\]

This condition is polynomial-time testable on forests. Root each tree component. For a vertex \(v\), color \(c\in\{0,1\}\), and \(b\in\{0,1\}\), maintain the attainable numbers of color-\(1\) vertices in the rooted subtree of \(v\), where \(b\) records whether the edge from \(v\) to its parent is bichromatic. When combining the children \(w\) of \(v\), impose

\[
b+\big|\{w:c(w)\ne c(v)\}\big|\le1.
\]

For a child of different color, its parent-edge state is \(1\); otherwise it is \(0\). Standard tree-knapsack convolution computes all attainable cardinalities in \(O(n^3)\) time. Component spectra are then combined by another knapsack convolution.

This does not decide the strong transversal property, but it gives an explicit, efficiently checkable necessary condition.

# 7. Gaps and status

1. The coloring conditions above are only necessary. I do not prove that a forest satisfying all of them has the strong transversal property.
2. The \(q\)-color conditions are stronger than the matching-cut spectrum, but no finite subcollection is shown sufficient.
3. The result adds a concrete negative tree beyond the degree obstruction in the prompt, but it does not provide a complete characterization.
4. I have not independently verified whether an equivalent incidence construction appears in the full source paper or elsewhere; it is not mentioned in the supplied literature summary.
