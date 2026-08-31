```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I do not resolve the conjecture, but give exact algorithms controlled by neighborhood components, external component types, or an associated CSP's treewidth, together with a sharp radius-two hardness barrier.",
  "would_publish": false,
  "caveats": "No universal polylogarithmic bound is proved for these parameters, so the general diameter-2 case remains open."
}
```

## 1. Statement and outcome

The target is to decide whether an \(n\)-vertex graph \(G\) of diameter at most \(2\) admits a homomorphism to \(K_3\), in time
\[
\exp((\log n)^{O(1)}).
\]

I do not obtain such an algorithm in full. I give:

1. an exact \(O^*(2^{\kappa_v})\) algorithm, where \(\kappa_v\) is the number of connected components of \(G[N(v)]\);
2. an exact \(O^*(3^{\rho_v})\) algorithm, where \(\rho_v\) counts certain external types of those components;
3. an exact bounded-treewidth algorithm for the resulting Boolean/ternary CSP;
4. the standard domination argument, recovering the supplied
   \[
   2^{O(\sqrt{n\log n})}
   \]
   bound and identifying two degree regimes where quasi-polynomial time already follows;
5. a safe forced-equality contraction reducing the unresolved core to graphs in which every neighborhood induces a matching;
6. a self-contained NP-hardness reduction for graphs of radius \(2\) and diameter at most \(4\), showing that the all-pairs diameter-\(2\) condition—not merely the existence of a radius-\(2\) centre—must be used essentially.

Here \(O^*(\cdot)\) suppresses polynomial factors.

---

## 2. The neighborhood-orientation reduction

Fix \(v\in V(G)\), and put
\[
H_v=G[N(v)],\qquad S_v=V(G)\setminus N[v].
\]

In any proper \(3\)-coloring, after permuting the colors we may assume that \(v\) has color \(1\). Consequently, \(H_v\) must be bipartite, since its vertices can only receive colors \(2\) and \(3\).

If \(H_v\) is not bipartite, then \(G\) is not \(3\)-colorable. Otherwise, let
\[
C_1,\dots,C_k
\]
be the connected components of \(H_v\), with fixed bipartitions
\[
C_i=A_i\mathbin{\dot\cup}B_i.
\]
Write
\[
\kappa_v=k.
\]

Each \(C_i\) has exactly two possible colorings with colors \(2,3\): either \(A_i\) gets \(2\) and \(B_i\) gets \(3\), or vice versa.

### Proposition 2.1

For every vertex \(v\) of eccentricity at most \(2\), \(3\)-colorability can be decided in time
\[
O^*(2^{\kappa_v}).
\]

#### Proof

Enumerate the two orientations of every component \(C_i\).

Once these orientations are fixed, every \(x\in S_v\) receives the list
\[
L(x)=\{1,2,3\}\setminus
\{\text{colors appearing on }N(x)\cap N(v)\}.
\]
Since \(\operatorname{ecc}(v)\le 2\), every \(x\in S_v\) has a neighbor in \(N(v)\). Hence
\[
|L(x)|\le 2.
\]

It remains to solve list \(3\)-coloring on \(G[S_v]\) when every list has size at most \(2\). This is a \(2\)-SAT instance: represent a two-element list by one Boolean variable, and for every edge \(xy\) and every color \(c\in L(x)\cap L(y)\), add the clause forbidding \(x=y=c\). Singleton lists give unit clauses, and empty lists cause immediate rejection.

Every \(3\)-coloring of \(G\) appears under one orientation vector, and every satisfying list coloring extends the chosen coloring of \(N[v]\). Thus the algorithm is exact. ∎

In particular, if some \(v\) has
\[
\kappa_v=(\log n)^{O(1)},
\]
then the problem is quasi-polynomial. If \(G[N(v)]\) is connected, the algorithm is polynomial.

---

## 3. The exact local CSP and its treewidth

The preceding reduction can be retained as one CSP rather than enumerating all component orientations.

For each component \(C_i\), introduce a Boolean variable \(X_i\) specifying its orientation. For every \(x\in S_v\), introduce a variable \(Y_x\in\{1,2,3\}\).

For each incidence \(x\)--\(C_i\), impose the binary relation saying that \(Y_x\) differs from the colors assigned, under \(X_i\), to all neighbors of \(x\) in \(C_i\). For every edge \(xy\in E(G[S_v])\), impose
\[
Y_x\ne Y_y.
\]

Define the primal graph \(P_v\) with vertex set
\[
\{X_1,\dots,X_k\}\cup S_v,
\]
where:

- \(X_i\) is adjacent to \(x\in S_v\) if \(x\) has a neighbor in \(C_i\);
- two vertices \(x,y\in S_v\) are adjacent if \(xy\in E(G)\).

### Proposition 3.1

Given a tree decomposition of \(P_v\) of width \(t\), \(3\)-colorability of \(G\) can be decided in time
\[
O^*(3^{t+1}).
\]

#### Proof

This is standard dynamic programming on a nice tree decomposition. Every variable has domain of size at most \(3\), and all constraints are binary. For each bag, store the assignments to the variables in that bag which extend to a satisfying assignment in the processed part. There are at most \(3^{t+1}\) assignments per bag. ∎

Thus the problem is quasi-polynomial whenever some \(P_v\) has treewidth \((\log n)^{O(1)}\). A suitable decomposition can also be found within quasi-polynomial time in this regime using standard fixed-parameter treewidth algorithms.

---

## 4. Compressing externally equivalent neighborhood components

The number \(\kappa_v\) can be large even when most component orientations have the same effect on \(S_v\). This permits a stronger exact compression.

For \(C_i=A_i\dot\cup B_i\), define
\[
P_i=\{x\in S_v:N(x)\cap A_i\ne\varnothing\},\qquad
Q_i=\{x\in S_v:N(x)\cap B_i\ne\varnothing\}.
\]
Two components have the same external type if their ordered pairs
\((P_i,Q_i)\) agree, up to interchanging the two coordinates. Let
\[
\rho_v
\]
be the number of external types.

Choose a consistent orientation of the two sides for all components of one type. For a type containing several components, only three aggregate states matter:

- all components use orientation \(0\);
- all components use orientation \(1\);
- both orientations occur.

The third state is available only when the type has multiplicity at least two.

Indeed, for any \(x\in S_v\), the set of colors contributed by one type is determined by the following table:

\[
\begin{array}{c|ccc}
\text{incidence of }x&\text{all }0&\text{all }1&\text{mixed}\\ \hline
x\notin P_i\cup Q_i&\varnothing&\varnothing&\varnothing\\
x\in P_i\setminus Q_i&\{2\}&\{3\}&\{2,3\}\\
x\in Q_i\setminus P_i&\{3\}&\{2\}&\{2,3\}\\
x\in P_i\cap Q_i&\{2,3\}&\{2,3\}&\{2,3\}.
\end{array}
\]

### Proposition 4.1

For every \(v\) of eccentricity at most \(2\), \(3\)-colorability can be decided in time
\[
O^*(3^{\rho_v}).
\]

#### Proof

Enumerate the at most three aggregate states of each external type. Every state vector is realizable by choosing component orientations independently; in a mixed type choose at least one component of each orientation.

The table determines exactly which colors appear in \(N(x)\cap N(v)\) for every \(x\in S_v\), and hence determines a list \(L(x)\) of size at most two. Solve the resulting list-coloring instance by \(2\)-SAT as in Proposition 2.1.

Conversely, every orientation vector induces one of the enumerated aggregate state vectors, so no coloring is omitted. ∎

Therefore diameter-\(2\) \(3\)-coloring is quasi-polynomial whenever
\[
\min_v \rho_v=(\log n)^{O(1)}.
\]

This compression can be substantial. For example, in the friendship graph consisting of \(k\) triangles sharing one common vertex \(v\), \(G[N(v)]\) has \(k\) components, but all have the same empty external signature, so \(\rho_v=1\).

---

## 5. Dominating sets and the known subexponential bound

The following standard observation is useful for identifying the remaining degree regime.

### Lemma 5.1

If \(D\) is a dominating set of \(G\), then \(3\)-colorability can be decided in time
\[
O^*(3^{|D|}).
\]

#### Proof

Enumerate all proper colorings of \(G[D]\). For every \(x\notin D\), remove from \(\{1,2,3\}\) all colors used by its neighbors in \(D\). Since \(D\) dominates \(x\), the resulting list has size at most two. The extension problem is therefore \(2\)-SAT. ∎

If \(G\) has minimum degree \(\delta\), it has a dominating set of size at most
\[
\frac{n(1+\ln(\delta+1))}{\delta+1}.
\]
For completeness, select every vertex independently with probability
\[
p=\frac{\ln(\delta+1)}{\delta+1}
\]
and then add every undominated vertex. The expected size is at most
\[
np+n(1-p)^{\delta+1}
 \le \frac{n\ln(\delta+1)}{\delta+1}+\frac{n}{\delta+1}.
\]
This can be derandomized by conditional expectations.

On the other hand, if \(v\) has minimum degree, then
\[
\kappa_v\le |N(v)|=\delta.
\]
Combining the two algorithms gives
\[
O^*\!\left(
 \exp\left(
 O\!\left(
 \min\left\{
 \delta,\,
 \frac{n(1+\log(\delta+1))}{\delta+1}
 \right\}
 \right)\right)\right).
\]
Optimizing over \(\delta\) recovers
\[
2^{O(\sqrt{n\log n})},
\]
rather than improving it.

It also gives quasi-polynomial time in each of the following regimes, for every fixed \(a\):

\[
\delta\le(\log n)^a,
\qquad\text{or}\qquad
\delta\ge\frac{n}{(\log n)^a}.
\]

Thus the unresolved degree range for these elementary methods is approximately
\[
(\log n)^{\omega(1)}
 \ll \delta
 \ll \frac{n}{(\log n)^{\omega(1)}}.
\]

---

## 6. A safe forced-equality contraction

There is a useful polynomial preprocessing rule.

### Lemma 6.1

Suppose \(ab\in E(G)\) and \(x,y\in N(a)\cap N(b)\). In every proper \(3\)-coloring,
\[
c(x)=c(y).
\]

#### Proof

The adjacent vertices \(a,b\) receive two different colors. Every common neighbor of \(a,b\) must receive the unique third color. ∎

Consequently, all common neighbors of an edge may be contracted into one forced-color class. If two vertices forced into one class are adjacent, the instance is not \(3\)-colorable. Otherwise, form the quotient graph by taking the union of their neighborhoods.

This operation preserves \(3\)-colorability in both directions. It also preserves diameter at most \(2\): if two quotient classes are nonadjacent, representatives in the original graph have a common neighbor, whose class is adjacent to both quotient classes.

Iterate until every edge has at most one common neighbor.

### Corollary 6.2

In the resulting quotient \(Q\), for every \(q\in V(Q)\),
\[
\Delta(Q[N(q)])\le 1.
\]

#### Proof

If \(x\in N(q)\) had two distinct neighbors \(y,z\in N(q)\), then \(y,z\) would be two common neighbors of the edge \(qx\), contradicting termination. ∎

Hence one may assume that every neighborhood induces a disjoint union of edges and isolated vertices. This is a useful normalization, but it does not settle the problem: triangle-free diameter-\(2\) graphs are already fixed points of this contraction.

---

## 7. Why a radius-\(2\) centre is insufficient

The local reduction above applies to any graph with a vertex of eccentricity \(2\). Without the additional requirement that every pair of vertices be at distance at most \(2\), the resulting orientation CSP is already NP-hard.

### Proposition 7.1

\(3\)-colorability is NP-complete for graphs having radius at most \(2\), and hence diameter at most \(4\), even when for a specified centre \(v\):

- \(G[N(v)]\) is independent;
- \(G[V\setminus N[v]]\) is a disjoint union of triangles;
- every vertex outside \(N[v]\) has exactly one neighbor in \(N(v)\), apart from possible repeated variables within one triangle.

#### Proof

Reduce from positive NAE-\(3\)-SAT, allowing repeated variables in a clause. This version is NP-complete: starting from ordinary NAE-\(3\)-SAT, replace every literal \(x\) and \(\neg x\) by separate positive variables \(x^+,x^-\), and add
\[
\operatorname{NAE}(x^+,x^-,x^-),
\]
which forces \(x^+\ne x^-\).

Create a vertex \(v\), and for every Boolean variable \(x_i\), create a vertex \(z_i\) adjacent to \(v\).

For each NAE clause
\[
C=(x_i,x_j,x_k),
\]
create three vertices
\[
y_{C,i},y_{C,j},y_{C,k}
\]
forming a triangle, and add the three edges
\[
z_i y_{C,i},\quad z_j y_{C,j},\quad z_k y_{C,k}.
\]
There are no other edges.

Every vertex \(z_i\) is at distance one from \(v\), and every clause vertex is at distance two from \(v\). Thus \(v\) has eccentricity at most \(2\), and the graph has diameter at most \(4\).

Fix \(c(v)=1\). Each \(z_i\) receives color \(2\) or \(3\), representing a Boolean value. A clause triangle must use all three colors. Its vertex attached to \(z_i\) cannot use \(c(z_i)\).

If the three variable colors are equal, then none of the triangle vertices can use that common color, so the triangle cannot be colored. Conversely, if both colors \(2\) and \(3\) occur among the three variables, choose a position attached to color \(3\) and color its triangle vertex \(2\), choose a position attached to color \(2\) and color its triangle vertex \(3\), and color the remaining triangle vertex \(1\).

Thus a clause triangle is colorable exactly when its three variables are not monochromatic. Different clause triangles interact only through the variable vertices, completing the reduction. ∎

This explains a central obstacle: merely fixing a vertex \(v\) and using the fact that all remaining lists have size at most two after orienting \(G[N(v)]\) does not lead to a tractable joint problem. Any successful quasi-polynomial algorithm must use the additional distance-\(2\) conditions between:

- a vertex of \(S_v\) and every component of \(N(v)\), and
- pairs of vertices within \(S_v\).

---

## 8. The local parameters are not automatically small

For completeness, \(\rho_v\) cannot be bounded by a polylogarithm from diameter \(2\) and \(3\)-colorability alone.

For \(k\ge2\), let \(A_k\) be the Cayley graph on
\[
\mathbb Z_{3k-1}
\]
with connection set
\[
\{k,k+1,\dots,2k-1\}.
\]
The connection set is closed under negation.

- The graph is triangle-free because the neighborhood of \(0\), namely the interval \(\{k,\dots,2k-1\}\), is independent.
- It has diameter \(2\): every \(d\in\{1,\dots,k-1\}\) satisfies
  \[
  d\equiv (k+d)+(2k-1)\pmod{3k-1},
  \]
  and the negative differences are analogous.
- It is \(3\)-colorable by the three consecutive intervals
  \[
  \{0,\dots,k-1\},\quad
  \{k,\dots,2k-1\},\quad
  \{2k,\dots,3k-2\}.
  \]

For \(v=0\), \(N(v)\) is independent and has \(k\) components. These components have distinct external signatures. Indeed, equal external signatures would make the corresponding vertices false twins, while distinct translates of the connection set cannot coincide: a nontrivial translation stabilizer would have orbit size dividing both \(k\) and \(3k-1\), whose gcd is \(1\).

Thus
\[
\kappa_v=\rho_v=k=\Theta(n)
\]
for every \(v\). This family is nevertheless covered by the high-minimum-degree dominating-set regime, since \(k\sim n/3\). It shows, however, that the local component parameters alone cannot prove the conjecture.

---

## 9. Remaining gap

The obtained algorithms yield quasi-polynomial time if at least one of the following holds:

1. \(\delta(G)=(\log n)^{O(1)}\);
2. \(\delta(G)\ge n/(\log n)^{O(1)}\);
3. some \(G[N(v)]\) has \((\log n)^{O(1)}\) connected components;
4. some \(v\) has \(\rho_v=(\log n)^{O(1)}\);
5. some associated CSP graph \(P_v\) has treewidth \((\log n)^{O(1)}\);
6. the forced-equality quotient becomes small enough to fall into one of these cases.

I do not prove that every \(3\)-colorable diameter-\(2\) graph satisfies one of these conditions. In particular, I have no argument excluding a middle-degree family whose diamond-closed quotient simultaneously has:

- many externally distinct neighborhood components for every choice of \(v\);
- large CSP treewidth;
- no polylogarithmic dominating set.

Therefore the general quasi-polynomial-time question remains unresolved.