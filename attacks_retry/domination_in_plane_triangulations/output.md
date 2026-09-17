```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I establish a degree-sensitive domination bound and prove the n/4 inequality for triangulated augmentations of at least two vertex-disjoint octahedra.",
  "would_publish": false,
  "caveats": "The general conjecture is not settled; novelty and current literature status have not been independently checked."
}
```

## 1. Two partial results

I use the usual convention that a plane triangulation is finite and simple.

The first result strengthens the bound in the supplied attempt. Its Kempe-switching idea is valid, but one can count substantially more switches at vertices of larger degree. The second result handles an infinite family with linearly many degree-four vertices having bipartite neighborhoods—a situation in which the coloring bound retains a linear error term.

Neither result settles the conjecture for arbitrary plane triangulations.

### A degree-sensitive bound

For a plane triangulation \(G\), define
\[
B(G)=\{v\in V(G):G[N(v)]\text{ is bipartite}\}.
\]
Every vertex in \(B(G)\) has even degree at least four: its neighbors, in rotation order, contain a cycle of length \(\deg(v)\).

For \(k\ge2\), put
\[
p_k=
\frac{2}{
2^{\lfloor(k+1)/2\rfloor}
+
2^{\lceil(k+1)/2\rceil}
-2}.
\]
The first values are
\[
\begin{array}{c|ccccc}
\deg(v)=2k&4&6&8&10&12\\ \hline
p_k&1/2&1/3&1/5&1/7&1/11 .
\end{array}
\]
Define
\[
S(G)=\sum_{v\in B(G)}p_{\deg(v)/2}.
\]

**Theorem 1.** Every simple plane triangulation on \(n\ge4\) vertices satisfies
\[
\boxed{\displaystyle
\gamma(G)\le \left\lfloor\frac{n+S(G)}4\right\rfloor.}
\tag{1}
\]
More generally, for every nonnegative vertex-cost function \(w\), there is a dominating set \(D\) such that
\[
\boxed{\displaystyle
w(D)\le
\frac14\left(
w(V(G))+
\sum_{v\in B(G)}w(v)p_{\deg(v)/2}
\right).}
\tag{2}
\]

For example, writing \(b_d\) for the number of vertices in \(B(G)\) of degree \(d\), (1) becomes
\[
\gamma(G)\le
\left\lfloor
\frac n4+\frac{b_4}{8}+\frac{b_6}{12}
+\frac{b_8}{20}+\frac{b_{10}}{28}
+\frac{b_{12}}{44}+\cdots
\right\rfloor.
\tag{3}
\]

Since \(p_k\le 1/k\le1/2\), this implies both
\[
\gamma(G)\le
\left\lfloor\frac n4+
\frac12\sum_{v\in B(G)}\frac1{\deg(v)}\right\rfloor
\tag{4}
\]
and the supplied attempt’s bound
\[
\gamma(G)\le \left\lfloor\frac n4+\frac{|B(G)|}{8}\right\rfloor.
\]

## 2. A stronger Kempe-switching count

Let \(\Omega\) be the set of all proper colorings
\[
f:V(G)\longrightarrow\{1,2,3,4\},
\]
including colorings that do not use every color. The Four Color Theorem gives \(\Omega\ne\varnothing\).

Call \(v\) **deficient** in \(f\) if \(N[v]\) does not contain all four colors. Every closed neighborhood contains at least three colors, since \(v\) belongs to a triangle. Thus a deficient vertex sees exactly two colors on its open neighborhood, and consequently belongs to \(B(G)\).

The key improvement is the following.

**Lemma.** If \(f\) is chosen uniformly from \(\Omega\), then, for \(v\in B(G)\) of degree \(2k\),
\[
\mathbb P(v\text{ is deficient in }f)\le p_k.
\tag{5}
\]

### 2.1. A planarity inequality for the relevant components

Fix \(v\), and fix its cyclically ordered neighbors as
\[
x_1,y_1,x_2,y_2,\ldots,x_k,y_k.
\]
Write
\[
A=\{x_1,\ldots,x_k\},\qquad
B=\{y_1,\ldots,y_k\}.
\]
These two sets are fixed independently of the coloring.

Consider a coloring in which \(v\) is deficient. The neighbor cycle is two-colored, so write
\[
f(A)=a,\qquad f(B)=b,\qquad f(v)=c,
\]
with \(d\) the missing color. Let \(H=G-v\).

Let

- \(r\) be the number of components of \(H[\{a,d\}]\) meeting \(A\);
- \(s\) be the number of components of \(H[\{b,c\}]\) meeting \(B\).

Here, for example, \(H[\{a,d\}]\) means the subgraph induced by vertices colored \(a\) or \(d\).

I claim that
\[
\boxed{r+s\ge k+1.}
\tag{6}
\]

To prove this, view \(H\) in a closed disk whose boundary is the neighbor cycle \(C\). In each of the \(r+s\) components under consideration, choose a tree containing all its boundary vertices. These trees are pairwise vertex-disjoint, since the two color pairs are disjoint.

Let \(t\) be the number of their vertices not on \(C\), and let \(W\) be the union of these trees and \(C\). Then
\[
|V(W)|=2k+t,
\qquad
|E(W)|=2k+\bigl(2k+t-r-s\bigr).
\]
The graph \(W\) is connected, so Euler’s formula gives
\[
F_{\mathrm{bounded}}(W)=2k-r-s+1.
\]

Every bounded facial boundary contains a positive even number of edges of \(C\). Indeed, it cannot consist entirely of forest edges; and each traversal of an edge of \(C\) switches between an \(\{a,d\}\)-tree and a \(\{b,c\}\)-tree, whereas forest edges remain within one type. Thus every bounded face contains at least two boundary-cycle edges.

Each of the \(2k\) edges of \(C\) is incident with exactly one bounded face of \(W\). Therefore
\[
2F_{\mathrm{bounded}}(W)\le2k,
\]
which proves (6).

### 2.2. Many colorful outputs from each deficient coloring

A Kempe switch interchanges two colors on a component induced by those colors.

Starting from the deficient coloring above, perform either of the following operations.

**Type A.** Choose a nonempty proper subset of the \(r\) components of \(H[\{a,d\}]\) meeting \(A\), and switch \(a,d\) on those components. Keep \(v\) colored \(c\).

This gives \(2^r-2\) distinct proper colorings. In each, \(A\) uses both \(a,d\), while \(B\) remains monochromatic in \(b\); hence \(v\) is no longer deficient.

**Type B.** First recolor \(v\) from \(c\) to \(d\). Then choose a nonempty proper subset of the \(s\) components of \(H[\{b,c\}]\) meeting \(B\), and switch \(b,c\) on those components.

This gives \(2^s-2\) distinct proper colorings. Now \(A\) is monochromatic and \(B\) uses both \(b,c\), so again \(v\) is not deficient.

All these operations are legal: in Type A the center color is outside the switched pair, and in Type B it is moved outside the switched pair before switching. Outputs of the two types are distinguishable by which of \(A,B\) is monochromatic.

By (6) and the elementary minimization of \(2^r+2^s\) with fixed sum, every deficient coloring therefore gives at least
\[
m_k=
2^{\lfloor(k+1)/2\rfloor}
+
2^{\lceil(k+1)/2\rceil}
-4
\tag{7}
\]
distinct nondeficient outputs.

### 2.3. Each output has at most two preimages

For a Type A output, the original monochromatic color on \(A\) must be one of its two current colors. Once that choice is made, the inverse is unique: switch precisely those components meeting \(A\) whose boundary vertices have the other color.

The relevant two-color component partition is unchanged by a Kempe switch. Components not meeting \(A\) were never switched. Thus there are at most two preimages.

For a Type B output, the original monochromatic color on \(B\) must be one of its two current colors. For each choice, the switches are again uniquely determined, and the original color of \(v\) is the other color currently occurring on \(B\). Hence there are at most two preimages here as well.

Since the two output types are distinguishable, an output has at most two preimages in total.

Let \(\mathcal L\) and \(\mathcal R\) be the deficient and nondeficient colorings at \(v\). Double-counting the transformations gives
\[
m_k|\mathcal L|\le2|\mathcal R|.
\]
Consequently,
\[
\frac{|\mathcal L|}{|\Omega|}
\le \frac{2}{m_k+2}=p_k,
\]
proving the lemma. \(\square\)

This re-proves the half-probability assertion from the previous attempt, while improving it strictly for every possible degree greater than four.

## 3. From the switching count to domination

For \(f\in\Omega\), let \(X(f)\) be its set of deficient vertices. By the lemma,
\[
\mathbb E\,w(X(f))
\le
\sum_{v\in B(G)}w(v)p_{\deg(v)/2}.
\]
Choose a coloring attaining at most this expectation.

Let
\[
C_i=f^{-1}(i),\qquad
X_i=\{v:N[v]\cap C_i=\varnothing\},
\qquad
D_i=C_i\cup X_i.
\]
Each \(D_i\) is a dominating set: any vertex not dominated by \(C_i\) has been included in \(X_i\).

Every deficient vertex misses exactly one color, so the four sets \(X_i\) partition \(X(f)\). Also \(C_i\cap X_i=\varnothing\). Therefore
\[
\sum_{i=1}^4 w(D_i)
=
w(V(G))+w(X(f))
\le
w(V(G))+
\sum_{v\in B(G)}w(v)p_{\deg(v)/2}.
\]
One of the four sets has at most one quarter of this total cost. This proves (2), and integrality gives (1). \(\square\)

For completeness, \(p_k\le1/k\) follows from \(2^j\ge2j\) for integers \(j\ge1\):
\[
2^{\lfloor(k+1)/2\rfloor}
+
2^{\lceil(k+1)/2\rceil}
-2\ge2k.
\]

## 4. Consequences for the conjectured bound

### 4.1. Exact bounds from small weighted defect

Write \(n=4q+r\), where \(0\le r\le3\). Theorem 1 proves
\[
\boxed{S(G)<4-r\quad\Longrightarrow\quad\gamma(G)\le q.}
\tag{8}
\]
Thus any counterexample to \(\gamma(G)\le n/4\) must satisfy
\[
S(G)\ge4-r.
\tag{9}
\]

There is a stronger conclusion when
\[
S(G)<1.
\tag{10}
\]
The expected number of deficient vertices is then less than one, so some proper four-coloring has no deficient vertices at all. Its four color classes are all dominating sets.

For instance, (10) holds if:

- \(B(G)\) has at most two vertices, both of degree at least six;
- \(B(G)\) has at most four vertices, all of degree at least eight.

More generally, if every vertex of \(B(G)\) has degree at least \(4t\), then
\[
S(G)\le \frac{2|B(G)|}{3\cdot2^t-2}.
\tag{11}
\]
In particular, the conjectured bound holds if every vertex with bipartite open neighborhood has degree at least
\[
4\lceil\log_2 n\rceil.
\]
Indeed, (11) then gives
\[
S(G)\le \frac{2n}{3n-2}<1.
\]

The case \(B(G)=\varnothing\) recovers the supplied special case. A sufficient condition is that every vertex either has odd degree or belongs to a \(K_4\).

### 4.2. A uniform bound for a structural class

Suppose every vertex of \(B(G)\) has degree at least eight, and put \(b=|B(G)|\). Then \(S(G)\le b/5\).

Since a simple plane triangulation has minimum degree at least three,
\[
6n-12=\sum_v\deg(v)\ge8b+3(n-b),
\]
so
\[
b\le\frac{3n-12}{5}.
\]
Theorem 1 therefore gives
\[
\boxed{\displaystyle
\gamma(G)\le
\left\lfloor\frac{7n-3}{25}\right\rfloor.}
\tag{12}
\]
Its asymptotic coefficient \(7/25=0.28\) is smaller than the \(2/7\) coefficient quoted in the question. This is a bound for the stated structural class, not a general improvement.

## 5. An exact \(n/4\) result with linearly many degree-four exceptions

The preceding method still leaves a linear error when many vertices have degree four. Here is a separate argument for one such family.

**Theorem 2.** Place \(m\ge2\) vertex-disjoint octahedra in pairwise disjoint disks, and add noncrossing edges, without adding vertices, to obtain a plane triangulation \(G\). Then
\[
\boxed{\displaystyle
\gamma(G)\le
\left\lfloor\frac{3m}{2}\right\rfloor
=
\left\lfloor\frac{|V(G)|}{4}\right\rfloor.}
\tag{13}
\]

### Proof

For each original octahedron \(O_i\), let \(T_i\) be its outer facial triangle and \(U_i\) its three inner vertices. Every edge added between different octahedra has its endpoints in their outer triangles.

An octahedron has three pairs of opposite vertices. For \(q\in T_i\), let \(q^*\in U_i\) be its opposite vertex. Then
\[
N_{O_i}[q^*]=V(O_i)\setminus\{q\}.
\tag{14}
\]
Also, any two distinct vertices dominate an octahedron.

Form the quotient graph \(Q\) whose vertices are the octahedra, with adjacency when an added edge joins them. It is connected and has at least two vertices.

The graph \(Q\) has a spanning star forest with no isolated vertices. To see this, take an inclusion-minimal spanning subgraph with no isolated vertices. Every edge has an endpoint of degree one, since otherwise it could be deleted; hence every component is a star.

Consider one star, with hub \(O_h\) and \(\ell\ge1\) leaves. For each leaf \(O_j\), choose an inter-octahedron edge
\[
p_jq_j,\qquad p_j\in T_h,\quad q_j\in T_j.
\]
Select \(q_j^*\) in every leaf. This dominates every vertex of the leaf except \(q_j\), which will be dominated if \(p_j\) is selected in the hub.

We complete the selection as follows.

- **If \(\ell=1\):** select \(p_1\) and one other hub vertex. The total is \(3\).
- **If \(\ell=2\):** select \(p_1,p_2\) if distinct; if they coincide, select that vertex and one other hub vertex. The total is \(4\).
- **If \(\ell\ge3\):** select all three vertices of \(T_h\). The total is \(\ell+3\).

In each case the hub is dominated, and all the remaining uncovered leaf vertices are dominated across the selected inter-octahedron edges. The costs satisfy
\[
3=\frac32(1+1),\qquad
4\le\frac32(2+1),
\]
and, for \(\ell\ge3\),
\[
\ell+3\le\frac32(\ell+1).
\]
Summing over the star forest gives a dominating set of size at most \(3m/2\). Integrality proves (13). \(\square\)

The restriction \(m\ge2\) is necessary: \(m=1\) is the original six-vertex octahedral obstruction.

This family genuinely goes beyond the small-\(B(G)\) situation. All three inner vertices of each octahedron retain degree four and an induced \(4\)-cycle as their neighborhood. Thus
\[
|B(G)|\ge3m=\frac{|V(G)|}{2}.
\]

## 6. What remains missing

There is a persistent obstruction to eliminating the coloring error merely by finding a proper four-coloring with no deficient vertices.

Consider an octahedral patch with outer triangle colored \(a,b,c\), and let \(d\) be the fourth color. Each inner vertex can receive either the color of its opposite outer vertex or \(d\). Since the inner vertices form a triangle, there are exactly four extensions:

1. no inner vertex receives \(d\);
2. one specified inner vertex receives \(d\), for each of the three choices.

In the first extension all three inner vertices are deficient. In each of the other extensions the vertex colored \(d\) is deficient. Consequently:

- every proper four-coloring of the patch has a deficient inner vertex;
- under the uniform distribution, each inner vertex is deficient in exactly half of the extensions.

So the degree-four probability \(1/2\) is sharp even inside arbitrarily large triangulations. In the family of Theorem 2, \(S(G)\ge n/4\), and Theorem 1 still carries a linear error term, even though Theorem 2 establishes the desired \(n/4\) bound.

The unresolved step is to replace the special octahedral-module argument by a method applicable to arbitrary triangulations, or to repair color deficiencies at no net cost above \(n/4\). Neither a general method of that kind nor an infinite counterexample family is established here.