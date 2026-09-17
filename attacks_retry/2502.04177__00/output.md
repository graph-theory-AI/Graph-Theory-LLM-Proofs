```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a delayed-treewidth subdivision case and construct explicit classes of expansion Θ(s^{2a}) containing graphs with bn_r=2 and scol_r=r^a+2.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; the constructed classes themselves have polynomial strong coloring numbers."
}
```

# 1. Scope of the result

I do not prove or disprove the full conjecture. I establish two self-contained partial results:

1. **A positive subdivision case.** The conjecture holds when the graphs arise by subdividing cores whose treewidth is polynomially bounded by the minimum subdivision length.
2. **A sharper explicit stress test.** For every integer \(a\ge 1\), there is an explicit monotone class \(\mathcal C_a\) whose expansion function has growth exactly
   \[
   \Theta_a(s^{2a}),
   \]
   and which contains, for every \(r=2^j\ge2\), a graph \(G_r\) satisfying
   \[
   \operatorname{bn}_r(G_r)=2,
   \qquad
   \operatorname{scol}_r(G_r)=r^a+2.
   \]
   Thus, even at bramble number \(2\), the required degree in \(r\) can be at least half the optimal expansion degree of the class.

The large-girth and subdivision mechanisms from the supplied attempt are checked below. The improvements are an exact characterization of \(\operatorname{bn}_r\le2\), an exact subdivision identity, and an algebraic construction with matching upper and lower expansion bounds.

All graphs are finite and simple. Strong reachability includes the starting vertex. Bramble members are nonempty connected subgraphs, with radius measured within the member. Minors are made simple after contraction. Empty graphs satisfy all upper bounds below trivially.

# 2. Ordering subdivision graphs

Write \(S_L(H)\) for the graph obtained by replacing every edge of \(H\) by a path of length exactly \(L\). Vertices inherited from \(H\) are called **original vertices**.

## Lemma 2.1 — Subdivision ordering

Suppose \(G\) is obtained from a nonempty graph \(H\) by replacing each edge by a path of length at least \(L\ge1\). Then, for every integer \(r\ge0\),
\[
\operatorname{scol}_r(G)
\le
\max\left\{3,\operatorname{scol}_{\lfloor r/L\rfloor}(H)\right\}.
\tag{2.1}
\]

In particular,
\[
\operatorname{scol}_r(G)\le3\qquad(r<L).
\tag{2.2}
\]

### Proof

Choose an order of \(V(H)\) witnessing the strong \(\lfloor r/L\rfloor\)-coloring number. Put all original vertices first in this order, followed by all subdivision vertices in any order.

Consider an original vertex \(v\). Every earlier vertex is original. A path between original vertices projects to a path in \(H\); a path of length at most \(r\) uses at most \(\lfloor r/L\rfloor\) subdivided edges. If the path witnesses strong reachability from \(v\), all its internal original vertices are later than \(v\). Consequently its endpoint is strongly \(\lfloor r/L\rfloor\)-reachable in the chosen order of \(H\).

Now consider an internal subdivision vertex \(v\). A witnessing strong path cannot have an original vertex internally, since every original vertex is earlier than \(v\). Hence it stays on the subdivided edge containing \(v\), possibly ending at an original endpoint. In each of the two directions, only the first earlier vertex can be strongly reachable: such a vertex blocks every further earlier endpoint in that direction. Including \(v\), there are at most three strongly reachable vertices. \(\square\)

For a graph \(H\), let \(\operatorname{dgn}(H)\) denote its degeneracy.

## Lemma 2.2 — An exact identity

For every nonempty graph \(H\) and integer \(L\ge1\),
\[
\boxed{\operatorname{scol}_L(S_L(H))
=\operatorname{dgn}(H)+1.}
\tag{2.3}
\]

### Proof

Put \(k=\operatorname{dgn}(H)\). Choose a nonempty subgraph \(H'\subseteq H\) of minimum degree at least \(k\).

Fix any order of \(S_L(H)\), and let \(v\) be the latest original vertex belonging to \(H'\). For every edge \(vw\in E(H')\), the other endpoint \(w\) is earlier than \(v\). Walking from \(v\) along its length-\(L\) replacement path, let \(x_{vw}\) be the first earlier vertex. Then \(x_{vw}\) is strongly \(L\)-reachable from \(v\). Distinct edges incident with \(v\) give distinct such vertices. Therefore
\[
\operatorname{scol}_L(S_L(H))\ge k+1.
\]

If \(k\ge2\), Lemma 2.1 and
\(\operatorname{scol}_1(H)=k+1\) give the reverse inequality.

If \(k=0\), the graph is edgeless. If \(k=1\), it is a forest with an edge, and so is its subdivision. Ordering each rooted tree with parents before children shows that its strong coloring numbers, at every positive radius, equal \(2\). These cover the remaining cases. \(\square\)

We will also use the standard elimination bound
\[
\operatorname{scol}_r(H)\le \operatorname{tw}(H)+1.
\tag{2.4}
\]
For completeness, make every bag of a width-\(k\) tree decomposition a clique and reverse a perfect elimination ordering of the resulting chordal graph. Any path whose internal vertices are later than its starting vertex can be shortcut in the chordal completion. Its earlier endpoint is consequently an earlier neighbor in the completion. Those neighbors, together with the starting vertex, form a clique contained in a bag, and hence number at most \(k+1\).

# 3. A positive case: polynomially delayed treewidth

The following shallow-minor observation will be used twice.

## Lemma 3.1 — Below the subdivision scale

Suppose every replacement path in a subdivision \(G\) of \(H\) has length at least \(L\). If
\[
4s+1<L,
\]
then every depth-\(s\) minor of \(G\) has average degree at most \(4\).

### Proof

Consider a depth-\(s\) minor model. Call a branch set **principal** if it contains an original vertex.

Two principal branch sets cannot be adjacent. Indeed, choosing an original vertex in each, their distance in \(G\) would be at most
\[
2s+1+2s=4s+1<L.
\]
But distinct original vertices in \(G\) have distance at least \(L\).

Every nonprincipal branch set is an interval inside one replacement path, so it has at most two neighboring branch sets. Every minor edge therefore has a nonprincipal endpoint, giving
\[
|E(J)|\le 2|V(J)|.
\]
Thus the average degree is at most \(4\). \(\square\)

## Theorem 3.2 — Delayed-treewidth special case

Fix \(A\ge1\) and an integer \(d\ge0\). Let \(\mathcal C\) be the subgraph closure of any collection of subdivisions \(G_i\) of graphs \(H_i\), where every replacement path in \(G_i\) has length at least \(L_i\ge1\), and
\[
\operatorname{tw}(H_i)+1\le A L_i^d.
\tag{3.1}
\]

Then:

1. \(\mathcal C\) has polynomial expansion;
2. for every \(G\in\mathcal C\) and \(r\ge1\),
   \[
   \operatorname{scol}_r(G)\le \max\{3,Ar^d\}.
   \tag{3.2}
   \]

Consequently the conjectured inequality holds on \(\mathcal C\), for example with
\[
f(r,b)=3+A(r+1)^d.
\]

### Proof

It suffices to prove the bounds for the graphs \(G_i\): restricting an order to a subgraph cannot increase strong reachability, and every depth-\(s\) minor of a subgraph is also a depth-\(s\) minor of its supergraph.

If \(r<L_i\), Lemma 2.1 gives \(\operatorname{scol}_r(G_i)\le3\). If \(r\ge L_i\), the same lemma and (2.4) give
\[
\operatorname{scol}_r(G_i)
\le \max\{3,\operatorname{tw}(H_i)+1\}
\le \max\{3,Ar^d\}.
\]

For expansion, consider a depth-\(s\) minor \(J\) of \(G_i\). If \(4s+1<L_i\), Lemma 3.1 applies.

Otherwise \(L_i\le4s+1\). Subdividing edges gives
\[
\operatorname{tw}(G_i)\le\max\{2,\operatorname{tw}(H_i)\};
\]
this follows directly by inserting bags of size at most three along each replacement path. Treewidth does not increase under taking minors, and a graph of treewidth \(k\) has average degree at most \(2k\). Hence
\[
\overline d(J)
\le 2\max\{2,\operatorname{tw}(H_i)\}
\le 4+2A(4s+1)^d.
\]
This is a uniform polynomial expansion bound. \(\square\)

This permits unbounded treewidth; the additional requirement is that the subdivision scale grows sufficiently quickly relative to the core treewidth.

# 4. Exactly when the shallow bramble number is at most two

We use \(\operatorname{girth}(G)=\infty\) for forests.

## Lemma 4.1

For every graph \(G\) and integer \(r\ge0\),
\[
\boxed{
\operatorname{bn}_r(G)\le2
\quad\Longleftrightarrow\quad
\operatorname{girth}(G)>6r+3.
}
\tag{4.1}
\]

If \(G\) has an edge and satisfies these conditions, then \(\operatorname{bn}_r(G)=2\).

### Proof

Suppose first that \(G\) has a cycle of length \(\ell\le6r+3\). Partition its vertices into three nonempty consecutive arcs, each containing at most \(2r+1\) vertices. Each arc induces a connected subgraph of radius at most \(r\). The three arcs are disjoint and pairwise touch, so they form a depth-\(r\) bramble of order \(3\).

Conversely, suppose the girth exceeds \(6r+3\), and let \(\mathcal B\) be a nonempty depth-\(r\) bramble. Choose \(B_0\in\mathcal B\) and a center \(c\) of \(B_0\). Because every member touches \(B_0\), every vertex of every member lies within distance
\[
r+1+2r=3r+1
\]
of \(c\).

The ball \(G[N_{3r+1}[c]]\) is a tree. Indeed, a non-tree edge in a breadth-first-search tree of this ball would yield a cycle of length at most
\[
2(3r+1)+1=6r+3.
\]

Every bramble in a tree has order at most \(2\). Here is a direct argument. Subdivide every tree edge once, and augment each bramble member by the midpoint of every edge incident with it. The resulting subtrees pairwise intersect. By the Helly property for subtrees of a tree, they share a vertex. If this is an original vertex, it hits every member. If it is the midpoint of an edge \(xy\), then \(\{x,y\}\) hits every member.

Finally, the two singleton endpoints of an edge form a bramble of order \(2\). \(\square\)

# 5. Explicit examples with a sharp expansion profile

For a class \(\mathcal C\), define its expansion profile using average degree:
\[
\mathsf E_{\mathcal C}(s)
=
\sup\bigl\{\overline d(J):
J\text{ is a nonempty depth-}s\text{ minor of some }G\in\mathcal C\bigr\}.
\]

## Theorem 5.1

For every integer \(a\ge1\), there is an explicit monotone graph class \(\mathcal C_a\) such that:

1. as \(s\to\infty\),
   \[
   \mathsf E_{\mathcal C_a}(s)=\Theta_a(s^{2a});
   \tag{5.1}
   \]
2. for every \(r=2^j\ge2\), the class contains a graph \(G_r\) satisfying
   \[
   \operatorname{bn}_r(G_r)=2,
   \qquad
   \operatorname{scol}_r(G_r)=r^a+2;
   \tag{5.2}
   \]
3. nevertheless, every \(F\in\mathcal C_a\) satisfies
   \[
   \operatorname{scol}_t(F)\le 8(t+1)^{3a}
   \qquad(t\ge0).
   \tag{5.3}
   \]

## 5.1. The finite-field cores

Let \(q\ge2\) be a power of \(2\). Put
\[
K=\mathbb F_{q^2},\qquad V=K^2,
\]
viewing \(V\) as a four-dimensional vector space over \(\mathbb F_q\). Define
\[
\ell(z)=z+z^q
\]
and
\[
\beta(x,y)=\ell(x_1y_2-x_2y_1).
\]
The map \(\ell:K\to\mathbb F_q\) is nonzero. The form \(\beta\) is alternating and nondegenerate: for nonzero \(x\), the map
\[
y\longmapsto x_1y_2-x_2y_1
\]
is onto \(K\).

Define the bipartite graph \(H_q\) as follows:

- its point vertices are the one-dimensional \(\mathbb F_q\)-subspaces of \(V\);
- its line vertices are the two-dimensional totally isotropic \(\mathbb F_q\)-subspaces of \(V\);
- adjacency is containment.

There are
\[
P=(q+1)(q^2+1)
\]
points. Each line contains \(q+1\) points. For a point \(p\), the isotropic lines through \(p\) correspond to the one-dimensional subspaces of \(p^\perp/p\), a two-dimensional space. Thus each point also lies on \(q+1\) lines.

Consequently \(H_q\) is \((q+1)\)-regular, with
\[
N_q=2(q+1)(q^2+1),
\qquad
m_q=(q+1)^2(q^2+1).
\tag{5.4}
\]

It has girth at least \(8\). Two distinct points lie on at most one line, excluding \(4\)-cycles. A \(6\)-cycle would give three pairwise orthogonal points on three distinct joining lines. If their span had dimension two, those joining lines would coincide. If their span had dimension three, it would be a three-dimensional totally isotropic subspace, impossible in a nondegenerate alternating space of dimension four.

## 5.2. The subdivision family and its coloring numbers

Fix \(a\ge1\). For
\[
L=2^j,\qquad j\ge1,
\]
put
\[
q=L^a,\qquad G_L=S_L(H_q).
\]
Let \(\mathcal C_a\) be the subgraph closure of these graphs.

Since \(H_q\) is \((q+1)\)-regular, Lemma 2.2 gives
\[
\operatorname{scol}_L(G_L)=q+2=L^a+2.
\tag{5.5}
\]
Also,
\[
\operatorname{girth}(G_L)\ge8L>6L+3,
\]
so Lemma 4.1 gives
\[
\operatorname{bn}_L(G_L)=2.
\tag{5.6}
\]

For the global upper bound, if \(t<L\), Lemma 2.1 gives \(\operatorname{scol}_t(G_L)\le3\). If \(t\ge L\), that lemma gives
\[
\operatorname{scol}_t(G_L)\le N_q
\le 8q^3
=8L^{3a}
\le8t^{3a}.
\]
Restriction to subgraphs proves (5.3), including \(t=0\).

## 5.3. Upper bound on expansion

We first record a useful bound that avoids counting all subdivision vertices.

### Cycle-rank bound

If \(G\) is a subdivision of a graph with \(m\) edges, every minor \(J\) of \(G\) satisfies
\[
\overline d(J)\le 2+\sqrt{2m}.
\tag{5.7}
\]

Indeed, the cycle rank
\[
\mu(X)=|E(X)|-|V(X)|+c(X)
\]
is invariant under subdivision and does not increase under taking minors. Thus, writing \(n=|V(J)|>0\),
\[
|E(J)|\le n+m.
\]
Simplicity also gives \(\overline d(J)\le n-1\). Therefore
\[
\overline d(J)
\le \min\left\{n-1,\ 2+\frac{2m}{n}\right\}
\le2+\sqrt{2m},
\]
by splitting at \(n=\sqrt{2m}\).

For the cores in (5.4),
\[
m_q\le8q^4.
\]
Thus every minor of \(G_L\) has average degree at most
\[
2+\sqrt{2m_q}\le6q^2.
\tag{5.8}
\]

Now consider a depth-\(s\) minor of \(G_L\).

- If \(4s+1<L\), its average degree is at most \(4\), by Lemma 3.1.
- Otherwise \(L\le4s+1\), and (5.8) bounds its average degree by
  \[
  6q^2=6L^{2a}
  \le6\cdot4^{2a}(s+1)^{2a}.
  \]

Hence
\[
\mathsf E_{\mathcal C_a}(s)
\le6\cdot4^{2a}(s+1)^{2a}.
\tag{5.9}
\]

## 5.4. A dense depth-two minor of the core

We next prove a matching lower bound.

The one-dimensional \(K\)-subspaces of \(K^2\) form a collection \(\mathcal S\) of \(q^2+1\) two-dimensional \(\mathbb F_q\)-subspaces. Each is totally isotropic for \(\beta\), and every point belongs to exactly one member of \(\mathcal S\). Thus \(\mathcal S\) is a collection of line vertices partitioning the point vertices by incidence.

A line \(M\notin\mathcal S\) meets exactly \(q+1\) distinct members of \(\mathcal S\), one at each of its points.

For distinct \(S,T\in\mathcal S\), there are exactly \(q+1\) isotropic lines meeting both. To see this, note that \(S\oplus T=V\), and the pairing between \(S\) and \(T\) is nondegenerate. For every point \(p\subseteq S\), the intersection
\[
T\cap p^\perp
\]
is a unique point \(p'\subseteq T\). The span of \(p,p'\) is an isotropic line. The \(q+1\) choices of \(p\) give distinct lines and exhaust the possibilities.

Independently assign each line \(M\notin\mathcal S\) uniformly to one of the \(q+1\) spread lines it meets. For \(S\in\mathcal S\), form a branch set \(X_S\) consisting of:

- the line vertex \(S\);
- all point vertices contained in \(S\);
- all line vertices assigned to \(S\).

These branch sets are pairwise disjoint and have radius at most \(2\), centered at \(S\).

For distinct \(S,T\), a connecting line produces an edge between \(X_S\) and \(X_T\) if it is assigned to either \(S\) or \(T\). There are \(q+1\) connecting lines, with independent assignments. Therefore
\[
\Pr(X_S\text{ and }X_T\text{ are adjacent})
=
1-\left(1-\frac2{q+1}\right)^{q+1}
\ge1-e^{-2}.
\]

Put \(\eta=1-e^{-2}\). By linearity of expectation, some assignment produces a depth-two minor \(J_q\) on \(q^2+1\) vertices with
\[
|E(J_q)|\ge \eta\binom{q^2+1}{2},
\]
and consequently
\[
\overline d(J_q)\ge\eta q^2.
\tag{5.10}
\]

This probabilistic argument only selects a minor model; the graphs \(H_q\) and \(G_L\) themselves are explicitly defined by finite-field arithmetic.

## 5.5. Lifting the minor through subdivisions

A depth-two minor of \(H_q\) lifts to a depth-\(3L\) minor of \(S_L(H_q)\).

To verify this, choose a radius-two spanning tree in each branch set and replace its edges by their length-\(L\) paths. The resulting tree has radius at most \(2L\). For every required adjacency, select one original edge between the corresponding branch sets and assign all \(L-1\) internal vertices of its replacement path to one endpoint branch set. Its radius increases to at most \(3L-1\). Replacement-path interiors are disjoint, so the branch sets remain disjoint.

It follows from (5.10) that
\[
\mathsf E_{\mathcal C_a}(3L)\ge\eta q^2=\eta L^{2a}.
\tag{5.11}
\]

For any integer \(s\ge6\), choose the largest power of two \(L\le s/3\). Then
\[
s/6<L\le s/3.
\]
By monotonicity in the depth,
\[
\mathsf E_{\mathcal C_a}(s)
\ge \eta L^{2a}
\ge \eta(s/6)^{2a}.
\tag{5.12}
\]
Together, (5.9) and (5.12) prove (5.1), completing Theorem 5.1. \(\square\)

# 6. Consequences and the remaining gap

Suppose a polynomial \(f_a(r,b)\) satisfies the conjectured inequality on \(\mathcal C_a\). At every dyadic \(L\ge2\),
\[
f_a(L,2)\ge L^a+2.
\]
Therefore the one-variable polynomial \(f_a(r,2)\) must have degree at least \(a\).

Thus:

- there is no class-independent polynomial valid for all polynomial-expansion classes;
- a class with optimal expansion degree \(2a\) can already require degree at least \(a\) in \(r\), even when \(\operatorname{bn}_r=2\);
- low shallow bramble number does not remove the need for substantial, class-dependent dependence on \(r\).

These statements do **not** contradict the original question. For each fixed \(a\), Theorem 5.1 supplies the polynomial upper bound
\[
\operatorname{scol}_r(F)\le8(r+1)^{3a}
\qquad(F\in\mathcal C_a).
\]
Nor does taking a union over all \(a\) yield a counterexample: such a union loses polynomial expansion.

The unresolved issue is the general upper bound. The delayed-treewidth hypothesis in Theorem 3.2 is an additional structural condition; nothing here shows that arbitrary polynomial-expansion classes satisfy it, or a suitable replacement for it. Consequently, these results sharpen the quantitative obstruction and prove a subdivision special case, but leave the stated conjecture unresolved.