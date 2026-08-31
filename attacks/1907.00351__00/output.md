```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact class remains open, but a 12-vertex K3,3-minor-free graph is an explicit excluded minor and treewidth 3 is the sharp threshold guaranteeing membership.",
  "would_publish": false,
  "caveats": "The remaining excluded minors and the planar case are unresolved; no novelty claim is made relative to the source paper's construction."
}
```

# Mathematical writeup

## 1. Precise interpretation of the question

For an undirected graph \(G\), let

\[
\mathcal U_2=\{G:\text{every orientation of }G\text{ has dichromatic number at most }2\}.
\]

This class is not minor-closed. For example, the graph obtained by subdividing every edge of \(K_7\) once is bipartite, hence belongs to \(\mathcal U_2\), but it has \(K_7\) as a minor.

Consequently, the unique largest minor-closed class contained in \(\mathcal U_2\) is

\[
\boxed{\mathcal G_2
 =\{G:\text{every minor }H\preccurlyeq_m G\text{ belongs to }\mathcal U_2\}.}
\tag{1}
\]

Indeed, the right-hand side is minor-closed and contained in \(\mathcal U_2\), and every minor-closed subclass of \(\mathcal U_2\) is contained in it. By the Graph Minor Theorem, \(\mathcal G_2\) has a finite excluded-minor set, but that set is not presently determined.

Below I prove the following partial result.

### Main partial theorem

1. Every graph of treewidth at most \(3\) belongs to \(\mathcal G_2\).
2. There is a chordal, \(K_{3,3}\)-minor-free graph \(F\) on \(12\) vertices with
   \[
   \operatorname{tw}(F)=4
   \]
   such that \(F\notin\mathcal U_2\), while every proper minor of \(F\) belongs to \(\mathcal U_2\). Thus
   \[
   F\in \operatorname{Ex}_m(\mathcal G_2).
   \]
3. Consequently, \(3\) is the largest integer \(t\) for which every graph of treewidth at most \(t\) lies in \(\mathcal G_2\).
4. A natural family obtained by thickening every edge of a graph \(H\) to a \(K_5\) admits an exact characterization:
   \[
   \Theta(H)\in\mathcal U_2\iff H\text{ is bipartite},
   \qquad
   \Theta(H)\in\mathcal G_2\iff H\text{ is a forest}.
   \]

The graph \(F\) is likely closely related, and possibly identical, to the \(K_{3,3}\)-minor-free example underlying the source paper's observation. The excluded-minimality argument is given here in full.

---

## 2. Three elementary lemmas

A coloring of an oriented graph is called acyclic if each color class induces an acyclic digraph.

### Lemma 2.1: Subgraph heredity

If \(G\in\mathcal U_2\), then every subgraph of \(G\) lies in \(\mathcal U_2\).

#### Proof

Given an orientation of a subgraph \(H\subseteq G\), orient the remaining edges of \(G\) arbitrarily. An acyclic 2-coloring of the resulting orientation of \(G\) restricts to one of \(H\). ∎

### Lemma 2.2: Gluing over a clique of order at most two

Suppose oriented graphs \(D_1,D_2\) have no arcs between
\(V(D_1)\setminus V(D_2)\) and \(V(D_2)\setminus V(D_1)\), and their intersection is a clique of order at most two. If they have acyclic 2-colorings agreeing on the intersection, then the common coloring is acyclic on \(D_1\cup D_2\).

#### Proof

For an intersection of order at most one, every directed cycle lies in one piece.

Suppose the intersection is the edge \(uv\). A monochromatic directed cycle meeting both pieces would decompose into a directed \(u\)-to-\(v\) path in one piece and a directed \(v\)-to-\(u\) path in the other. If the shared arc is oriented \(u\to v\), then the latter path together with \(u\to v\) is already a monochromatic directed cycle in one piece, a contradiction. The case \(v\to u\) is symmetric. ∎

### Lemma 2.3: Prescribed colors in small cliques

Let \(x,y\) be two specified vertices.

1. Every orientation of \(K_r\), \(2\le r\le5\), has an acyclic 2-coloring in which \(x\) and \(y\) have different colors.
2. Every orientation of \(K_r\), \(2\le r\le4\), has an acyclic 2-coloring in which \(x\) and \(y\) have the same color.
3. Every orientation of \(K_5-e\) has an acyclic 2-coloring in which any specified pair \(x,y\) has the same color.

#### Proof

For (1), the assertion is immediate for \(r\le4\), since the vertices can be split into two sets of size at most two with \(x,y\) separated.

For \(r=5\), let the other vertices be \(a,b,c\), and prescribe \(x\) color \(0\) and \(y\) color \(1\). Among \(a,b,c\), two, say \(a,b\), are either both out-neighbors of \(y\) or both in-neighbors of \(y\). Hence the tournament on \(\{y,a,b\}\) is transitive. Color \(y,a,b\) with \(1\) and \(x,c\) with \(0\).

Part (2) follows by putting \(x,y\) in one class and the at most two remaining vertices in the other.

For (3), write \(Z=V(K_5-e)\setminus\{x,y\}\).

- If the missing edge has both endpoints in \(Z\), color \(x,y\) with \(0\) and all of \(Z\) with \(1\). The second class induces \(K_3-e\), hence a forest.
- If the missing edge joins \(x\) or \(y\) to some \(z\in Z\), color \(x,y,z\) with \(0\) and the remaining two vertices with \(1\). The first class induces a path.
- If the missing edge is \(xy\), put any \(z\in Z\) with \(x,y\); again the first class induces a path.

These partitions work for every orientation because both color classes induce forests. ∎

---

## 3. All graphs of treewidth at most three belong to \(\mathcal G_2\)

A \(3\)-degenerate graph admits a partition into two induced forests.

Take a degeneracy ordering \(v_1,\dots,v_n\) in which every \(v_i\) has at most three neighbors among \(v_{i+1},\dots,v_n\). Color in reverse order. When \(v_i\) is colored, one of the two colors occurs on at most one of its later neighbors; give \(v_i\) that color.

If one color class contained an undirected cycle, let \(v_i\) be the first vertex of that cycle in the ordering. Both its neighbors on the cycle would be later neighbors of the same color, contradicting the coloring rule. Thus both color classes induce forests and are acyclic under every orientation.

Every graph of treewidth at most \(3\), and every minor of it, is \(3\)-degenerate. Therefore

\[
\boxed{\operatorname{tw}(G)\le3\implies G\in\mathcal G_2.}
\tag{2}
\]

---

## 4. A \(K_5\) inequality gadget

Let \(Q(x,y)\) be the tournament on

\[
\{x,y,a,b,c\}
\]

with arcs

\[
x\to y,\qquad
y\to a,b,c,\qquad
a,b,c\to x,
\]

and

\[
a\to b\to c\to a.
\]

### Gadget property

In every acyclic 2-coloring of \(Q(x,y)\), the vertices \(x\) and \(y\) have different colors.

Indeed, if \(x,y\) had the same color, then each of

\[
x\to y\to a\to x,\qquad
x\to y\to b\to x,\qquad
x\to y\to c\to x
\]

would force \(a,b,c\) to receive the other color. But then
\(a\to b\to c\to a\) would be monochromatic.

Conversely, Lemma 2.3 shows that every orientation of \(K_5\), including this one, has a coloring separating any prescribed pair. Thus this gadget realizes exactly the binary constraint \(x\ne y\).

---

## 5. The explicit excluded minor \(F\)

Let the central vertices be

\[
X=\{x_0,x_1,x_2\},
\]

with indices modulo \(3\). For each \(i\), introduce three private vertices

\[
P_i=\{a_i,b_i,c_i\},
\]

and let

\[
B_i=\{x_i,x_{i+1},a_i,b_i,c_i\}
\]

induce a \(K_5\). There are no further edges. Thus \(F\) has \(12\) vertices and consists of a central triangle with a \(K_5\) attached along each of its three edges.

Orient each \(B_i\) as the gadget \(Q(x_i,x_{i+1})\). These orientations are consistent because different \(B_i\)'s share no edge.

Every acyclic 2-coloring would have to satisfy

\[
x_0\ne x_1,\qquad
x_1\ne x_2,\qquad
x_2\ne x_0,
\]

which is impossible with two colors. Hence

\[
F\notin\mathcal U_2.
\tag{3}
\]

### Structural properties of \(F\)

- \(F\) contains \(K_5\), so \(\operatorname{tw}(F)\ge4\).
- A tree decomposition consists of the central bag
  \(\{x_0,x_1,x_2\}\) and the three leaf bags \(B_0,B_1,B_2\). Its largest bags have size \(5\), so
  \[
  \operatorname{tw}(F)=4.
  \]
- The private vertices can be successively eliminated as simplicial vertices, leaving the central triangle. Thus \(F\) is chordal.
- \(F\) is obtained from \(K_3\) and three copies of \(K_5\) by clique-sums of order two. Since \(K_{3,3}\) is \(3\)-connected, a \(K_{3,3}\)-minor cannot straddle a separation of order at most two: any such minor would be contained in one summand. Neither \(K_3\) nor \(K_5\) has a \(K_{3,3}\)-minor. Hence
  \[
  K_{3,3}\not\preccurlyeq_m F.
  \]
- Since \(\operatorname{tw}(F)=4\), \(F\) has no \(K_6\)-minor.

Thus this is already a bad graph well below the complete-minor obstruction \(K_7\).

---

## 6. Minor-minimality of \(F\)

I now show that every proper minor of \(F\) belongs to \(\mathcal U_2\).

### 6.1. Every single-edge deletion is universally 2-colorable

Fix \(e\in E(F)\). It belongs to a unique block \(B_i\). Relabel so that its terminal vertices are \(p,q\), and let \(r\) be the third central vertex.

Prescribe

\[
c(p)=c(q)=0,\qquad c(r)=1.
\tag{4}
\]

The damaged block \(B_i-e\) extends this coloring by Lemma 2.3(3). The other two \(K_5\)'s have differently colored terminals, so their colorings extend by Lemma 2.3(1).

If \(e\ne pq\), the central triangle is colored \(0,0,1\), and all pieces meet along intact edges. Lemma 2.2 combines the local colorings into an acyclic coloring of \(F-e\).

Suppose \(e=pq\). First combine the central path \(p-r-q\) with the two intact \(K_5\)'s. In color \(0\), the vertices \(p\) and \(q\) lie in different underlying components of this union because their only connection outside \(B_i\) passes through \(r\), which has color \(1\). The damaged block \(B_i-pq\) is itself acyclically colored with \(p,q\) both color \(0\).

A monochromatic cycle crossing between \(B_i-pq\) and the rest would have to use both \(p,q\). This is impossible in color \(1\), since neither belongs to that color, and impossible in color \(0\), since there is no \(p\)-to-\(q\) path of color \(0\) in the rest. Hence \(F-pq\in\mathcal U_2\).

Thus

\[
F-e\in\mathcal U_2\qquad\text{for every }e\in E(F).
\tag{5}
\]

By subgraph heredity, every proper subgraph of \(F\) belongs to \(\mathcal U_2\).

### 6.2. Every nontrivial contraction quotient is universally 2-colorable

Let \(R\) be obtained from \(F\) by contracting a nonempty set of edges, with no deletions yet. Let \(y_i\) be the image of \(x_i\).

The image of every \(B_i\) is a clique of order at most five. Since private vertices have no neighbors outside their own \(B_i\), the intersections of these image cliques are controlled entirely by the images of the central vertices.

#### Case 1: \(y_0,y_1,y_2\) are distinct

The quotient still consists of a central triangle and three cliques of order at most five attached along its edges. Since at least one edge was contracted, at least one of these cliques, say the one on \(y_0y_1\), has order at most four.

Color

\[
c(y_0)=c(y_1)\ne c(y_2).
\]

The smaller clique on \(y_0y_1\) extends the equal terminal colors by Lemma 2.3(2). The other two cliques extend their unequal terminal colors by Lemma 2.3(1). Lemma 2.2 glues the colorings.

#### Case 2: exactly two central images are distinct

Suppose \(y_0=y_1=u\) and \(y_2=v\). The image of \(B_0\) is a clique of order at most four attached only at \(u\). The images of \(B_1\) and \(B_2\) are cliques of order at most five sharing the edge \(uv\).

Color \(u,v\) differently. Lemma 2.3(1) extends this coloring to both cliques containing \(uv\). The remaining clique has order at most four and meets the rest only at \(u\), so it can be colored and its color labels swapped to agree at \(u\). Gluing gives an acyclic coloring.

#### Case 3: all central vertices have the same image

Each image of \(B_i\) then has order at most four, and the pieces meet only at the common central image. Color each separately into classes of size at most two and swap color names so that they agree at the common vertex.

Therefore every nontrivial pure contraction quotient of \(F\) belongs to \(\mathcal U_2\).

### 6.3. Arbitrary proper minors

Every minor \(H\) of \(F\) can be obtained by first contracting the connected branch sets and then deleting unwanted edges and vertices.

- If at least one contraction is made, \(H\) is a subgraph of a nontrivial contraction quotient, which belongs to \(\mathcal U_2\).
- If no contraction is made and \(H\ne F\), then \(H\) is a proper subgraph of \(F\), and hence belongs to \(\mathcal U_2\) by (5).

Thus every proper minor of \(F\) lies in \(\mathcal U_2\). Since every minor of a proper minor is again a proper minor of \(F\), every proper minor of \(F\) actually belongs to \(\mathcal G_2\). Combining this with (3),

\[
\boxed{F\in\operatorname{Ex}_m(\mathcal G_2).}
\tag{6}
\]

This also proves that the treewidth bound in (2) is sharp.

---

## 7. An exactly solvable family

For a simple graph \(H\), define \(\Theta(H)\) as follows. For every edge \(uv\in E(H)\), add three private vertices \(a_{uv},b_{uv},c_{uv}\) and make

\[
\{u,v,a_{uv},b_{uv},c_{uv}\}
\]

a \(K_5\). Distinct edge gadgets have disjoint private vertices.

### Proposition 7.1

\[
\boxed{\Theta(H)\in\mathcal U_2\iff H\text{ is bipartite}.}
\]

#### Proof

If \(H\) is bipartite, color its vertices by a bipartition. The endpoints of every edge receive different colors. For an arbitrary orientation of \(\Theta(H)\), Lemma 2.3(1) extends these prescribed endpoint colors across each \(K_5\) gadget. The base color classes are independent, and Lemma 2.2 glues the gadgets one at a time.

Conversely, if \(H\) is non-bipartite, orient every edge gadget as the inequality gadget \(Q(u,v)\). Any acyclic 2-coloring would give different colors to the ends of every edge of \(H\), producing a proper 2-coloring of \(H\), a contradiction. ∎

### Proposition 7.2

\[
\boxed{\Theta(H)\in\mathcal G_2\iff H\text{ is a forest}.}
\]

#### Proof

If \(H\) is a forest, the \(K_5\) gadgets form a tree of \(1\)-sums. Every \(K_5\) belongs to \(\mathcal G_2\), and \(\mathcal G_2\) is closed under \(1\)-sums: minors retain a \(0/1\)-sum decomposition, local colorings can be swapped to agree at a shared vertex, and every directed cycle lies in one summand.

If \(H\) contains a cycle, choose three edges on that cycle. Delete all other edge gadgets, and contract each of the three intervening paths to a single vertex. The three retained \(K_5\)'s become exactly the graph \(F\). Hence

\[
F\preccurlyeq_m\Theta(H),
\]

so \(\Theta(H)\notin\mathcal G_2\). ∎

This family also illustrates why \(\mathcal U_2\) itself is not minor-closed: \(\Theta(C_4)\in\mathcal U_2\), but it contains \(F=\Theta(C_3)\) as a minor.

For completeness, when \(H\) has an edge,

\[
\operatorname{tw}(\Theta(H))
  =\max\{4,\operatorname{tw}(H)\}.
\]

The upper bound follows by attaching each \(K_5\) bag to a bag of a tree decomposition of \(H\) containing the relevant edge; the reverse inequality follows because \(\Theta(H)\) contains both \(H\) and \(K_5\).

---

## 8. Another exact special case: block graphs

A block graph is a graph whose 2-connected blocks are cliques. Using the supplied fact that every orientation of \(K_6\) is 2-colorable, one obtains

\[
\boxed{
G\text{ a block graph}\quad\Longrightarrow\quad
G\in\mathcal G_2
\iff\text{ every block of }G\text{ has at most six vertices}.
}
\]

If every block has order at most six, each block and all its minors are universally 2-colorable, and the graph is an iterated \(1\)-sum. If a block has order at least seven, it contains \(K_7\), which has a non-2-colorable orientation.

---

## 9. Resulting bounds and unresolved gap

The proved information can be summarized as

\[
\boxed{
\{G:\operatorname{tw}(G)\le3\}
\subsetneq
\mathcal G_2
\subseteq
\operatorname{Forb}_m(F,K_7).
}
\]

The first inclusion is strict because \(K_5\in\mathcal G_2\) and
\(\operatorname{tw}(K_5)=4\). The right-hand containment is only necessary; I have not proved that excluding \(F\) and \(K_7\) is sufficient.

A complete determination still faces the planar two-color conjecture. Since minors of planar graphs are planar,

\[
\text{every planar orientation is 2-colorable}
\iff
\text{every planar graph belongs to }\mathcal G_2.
\]

Thus the work above identifies one genuine excluded minor and gives exact answers on several natural subfamilies, but it does not determine the full finite excluded-minor set or settle the planar case.