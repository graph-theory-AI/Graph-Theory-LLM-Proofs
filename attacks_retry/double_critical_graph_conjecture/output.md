```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every noncomplete double-critical t-chromatic graph has at least t+7 vertices, one more than the bound in the supplied attempt.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved, and novelty of this partial result has not been checked."
}
```

# A strengthened order bound

All graphs below are finite and simple, and \(\chi(\varnothing)=0\).

I prove the following partial result.

**Theorem.** Let \(G\) be a connected double-critical graph with \(\chi(G)=t\).

1. If \(\Delta(\overline G)\le 3\), then \(G\cong K_t\).
2. If \(G\not\cong K_t\), then
   \[
   |V(G)|\ge t+7.
   \]

The second assertion improves the supplied attempt’s bound by one vertex. I checked and reuse its matching reduction, with a proof included below. The additional argument excludes the case \(|V(G)|=t+6\) by analyzing triangles in the complement.

No novelty claim is made. The only non-elementary ingredient is the classical Gallai–Edmonds matching decomposition.

## 1. Elementary consequences of double-criticality

The cases \(t=1,2\) give \(K_1,K_2\) immediately, so the arguments concerning a noncomplete graph may assume \(t\ge3\).

Write \(N_G(v)\) for an open neighborhood.

### 1.1. Vertex-criticality

For every vertex \(v\),
\[
\chi(G-v)=t-1.
\tag{1}
\]
Indeed, choose a neighbor \(w\). Then
\[
t-1\le \chi(G-v)
\le \chi(G-\{v,w\})+1=t-1.
\]

Consequently, if \(G\) contains a \(K_t\), then \(G=K_t\).

### 1.2. Common neighbors in every color class

For every edge \(uv\), each color class in every \((t-2)\)-coloring of \(G-\{u,v\}\) contains a common neighbor of \(u,v\).

To see this, suppose a color class \(I\) contains no common neighbor. The graph induced by \(I\cup\{u,v\}\) is bipartite: \(I\) is independent, and no vertex of \(I\) is adjacent to both \(u,v\). Replacing the color on \(I\) by a two-coloring of this induced graph produces a \((t-1)\)-coloring of \(G\), a contradiction.

In particular,
\[
|N_G(u)\cap N_G(v)|\ge t-2
\qquad(uv\in E(G)).
\tag{2}
\]

### 1.3. Minimum degree

If \(G\) is noncomplete, then
\[
\delta(G)\ge t+1.
\tag{3}
\]

First, (2) gives \(\delta(G)\ge t-1\). If \(d_G(v)=t-1\), then (2) forces \(N_G(v)\) to be a clique, giving a \(K_t\) and hence \(G=K_t\).

Suppose \(d_G(v)=t\). Every vertex of \(N_G(v)\) has at most one nonneighbor within \(N_G(v)\). The neighborhood cannot be complete, so choose nonadjacent \(a,b\in N_G(v)\). Then
\[
N_G(v)\cap N_G(a)=N_G(v)\setminus\{a,b\}
\]
has exactly \(t-2\) vertices. In a \((t-2)\)-coloring of \(G-\{v,a\}\), these vertices represent all colors by Section 1.2. But \(b\) is adjacent to every one of them, leaving no color for \(b\). This proves (3).

### 1.4. Two private neighbors

A useful strengthening of the prohibition on false twins is:
\[
|N_G(v)\setminus N_G(u)|\ge2
\qquad\text{whenever }u,v\text{ are nonadjacent}.
\tag{4}
\]

If \(N_G(v)\subseteq N_G(u)\), a coloring of \(G-v\) extends by giving \(v\) the color of \(u\), contradicting (1).

If
\[
N_G(v)\setminus N_G(u)=\{a\},
\]
color \(G-\{v,a\}\) with \(t-2\) colors. Give \(v\) the color of \(u\), which is permissible because every remaining neighbor of \(v\) is a neighbor of \(u\). Give \(a\) a new color. Again \(G\) is \((t-1)\)-colorable.

Put \(H=\overline G\). In complementary language, (4) says that, for every edge \(uv\in E(H)\),
\[
|N_H(u)\setminus N_H[v]|\ge2.
\]
Equivalently,
\[
d_H(u)\ge 3+|N_H(u)\cap N_H(v)|.
\tag{5}
\]

Thus every nonisolated vertex of \(H\) has degree at least three. Moreover, every vertex in a triangle of \(H\) has degree at least four.

## 2. Neighborhoods of vertices of degree \(t+1\)

**Lemma 1.** If \(d_G(v)=t+1\), then
\[
\overline{G[N_G(v)]}
\]
is a disjoint union of isolated vertices and cycles of length at least five.

**Proof.** Let
\[
L=\overline{G[N_G(v)]}.
\]
By (2), every vertex of \(L\) has degree at most two.

Suppose \(ab\in E(L)\). Consider a \((t-2)\)-coloring of \(G-\{v,b\}\). The color of \(a\) must also occur on a common neighbor \(c\) of \(v,b\). Therefore \(ac\in E(L)\), while \(bc\notin E(L)\).

It follows that every nonisolated vertex of \(L\) has degree two, and that \(L\) has no triangle. Hence its nontrivial components are cycles of length at least four.

A four-cycle is also impossible. If
\[
b,a,c,d,b
\]
is such a component, then in a \((t-2)\)-coloring of \(G-\{v,b\}\), both \(a\) and \(d\) must have the color of \(c\): for each, \(c\) is the only possible common-neighbor representative of its color. But \(a,d\) are adjacent in \(G\), a contradiction. \(\square\)

## 3. The verified matching reduction

Here is the restricted theorem from the supplied attempt that will be used.

**Lemma 2.** If some edge \(xy\in E(G)\) satisfies
\[
\alpha(G-\{x,y\})\le2,
\]
then \(G\cong K_t\).

### 3.1. Clique-packing savings

For a graph \(J\), define
\[
p(J)=\max_{\mathcal P}\sum_{Q\in\mathcal P}(|Q|-1),
\]
where \(\mathcal P\) ranges over vertex-disjoint cliques of order at least two. Uncovered vertices are regarded as singleton cliques.

Then
\[
p(J)=|V(J)|-\chi(\overline J).
\tag{6}
\]
Also:

- \(p\) is additive over components;
- if \(\nu(J)\) is the maximum matching size, then \(\nu(J)\le p(J)\), with equality when \(J\) is triangle-free;
- for every \(X\subseteq V(J)\),
  \[
  p(J)\le p(J-X)+|X|.
  \tag{7}
  \]

Let
\[
n=|V(G)|,\qquad r=n-t,\qquad H=\overline G.
\]
Vertex-criticality and double-criticality give
\[
\begin{aligned}
p(H)&=r,\\
p(H-v)&=r &&(v\in V(H)),\\
p(H-\{u,v\})&=r &&(uv\notin E(H),\ u\ne v).
\end{aligned}
\tag{8}
\]

### 3.2. A Gallai–Edmonds consequence

For a graph \(J\), let \(D\) be the vertices exposed by some maximum matching, let
\[
A=N_J(D)\setminus D,
\qquad
C=V(J)\setminus(D\cup A).
\]
The Gallai–Edmonds theorem states that the components \(Q_1,\dots,Q_m\) of \(J[D]\) are factor-critical, \(J[C]\) has a perfect matching, and every maximum matching matches the vertices of \(A\) into distinct components \(Q_i\), with near-perfect matchings inside the \(Q_i\).

Write
\[
b_i=\frac{|Q_i|-1}{2}.
\]
In particular,
\[
\nu(J)=\sum_i b_i+|A|+\frac{|C|}{2}.
\tag{9}
\]

Suppose
\[
p(J)=\nu(J),
\qquad
p(J-v)=p(J)\quad\text{for every }v.
\tag{10}
\]
Then
\[
A=\varnothing,\qquad p(Q_i)=b_i,\qquad p(J[C])=\frac{|C|}{2}.
\tag{11}
\]

Indeed, choose a maximum matching exposing a vertex of \(Q_i\). There is no matching edge from \(Q_i\) to \(A\). If \(p(Q_i)>b_i\), replacing its internal matching by a better clique packing contradicts \(p(J)=\nu(J)\). The same replacement argument on \(C\) gives \(p(J[C])=|C|/2\). Thus
\[
p(J-A)=\nu(J)-|A|.
\]
If \(a\in A\), (7) gives
\[
p(J-a)\le p(J-A)+|A|-1=\nu(J)-1,
\]
contrary to (10).

### 3.3. Proof of Lemma 2

Let \(S=\{x,y\}\). The hypothesis says that \(H-S\) is triangle-free. Consequently,
\[
r=p(H-S)=\nu(H-S)\le\nu(H)\le p(H)=r.
\]
Apply (11) to \(H\). Its Gallai–Edmonds set \(A\) is empty.

A maximum matching of \(H-S\), viewed in \(H\), exposes \(x,y\). Hence \(S\subseteq D\), and its two vertices lie in distinct factor-critical components.

Because \(S\cap C=\varnothing\), the graph \(H[C]\) is triangle-free. If \(c\in C\), then
\[
p(H[C]-c)\le \frac{|C|}{2}-1.
\]
Additivity would give \(p(H-c)\le r-1\), contradicting (8). Thus \(C=\varnothing\).

Every component \(Q\) of \(H\) is now factor-critical, of order \(2b+1\), with
\[
p(Q)=b,
\]
and contains at most one vertex of \(S\).

If \(Q\cap S=\varnothing\), then \(Q\) is triangle-free. If \(Q\) is nontrivial, it has nonadjacent vertices \(a,b'\). By (8) and additivity,
\[
p(Q-\{a,b'\})=p(Q)=b,
\]
whereas triangle-freeness and its order \(2b-1\) give
\[
p(Q-\{a,b'\})\le b-1.
\]
Thus \(Q\) is a singleton.

If \(Q\cap S=\{z\}\), then \(Q-z\) is triangle-free. The same argument shows that \(z\) cannot have a nonneighbor in \(Q\). Thus \(z\) is universal in \(Q\). If \(Q\) were nontrivial, any \(u\in Q-\{z\}\) would satisfy
\[
N_H(u)\setminus N_H[z]=\varnothing,
\]
contrary to (5). Hence this component is also a singleton.

Therefore \(H\) is edgeless, proving \(G=K_t\). \(\square\)

## 4. The subcubic-complement case

If \(\Delta(H)\le3\), equation (5) implies that \(H\) has no triangle. Thus \(\alpha(G)\le2\), and Lemma 2 applies to any edge of \(G\).

This proves the first assertion of the theorem.

For a noncomplete graph, (3) consequently excludes \(n\le t+5\), since
\[
\Delta(H)\le n-1-(t+1)\le3.
\]

It remains to exclude \(n=t+6\).

## 5. Structural properties when \(n=t+6\)

Assume for a contradiction that \(G\) is noncomplete and
\[
n=t+6.
\]
Then
\[
\Delta(H)\le4.
\tag{12}
\]

We will use four consequences.

1. **Every nonisolated vertex has degree three or four.**  
   This follows from (5).

2. **Every triangle vertex has degree four, and no edge belongs to two triangles.**  
   For an edge \(uv\) in a triangle, (5) and (12) force
   \[
   d_H(u)=d_H(v)=4,
   \qquad |N_H(u)\cap N_H(v)|=1.
   \tag{13}
   \]
   In particular, a vertex outside a triangle is adjacent to at most one vertex of that triangle.

3. **Nonadjacent degree-four vertices have at least two common neighbors in \(H\).**  
   If \(uv\notin E(H)\), then \(uv\in E(G)\). Equation (2) gives
   \[
   n-2-|N_H(u)\cup N_H(v)|\ge t-2.
   \]
   Thus
   \[
   |N_H(u)\cup N_H(v)|\le6.
   \]
   When both degrees are four,
   \[
   |N_H(u)\cap N_H(v)|\ge2.
   \tag{14}
   \]

4. **For every degree-four vertex \(v\),**
   \[
   H-N_H[v]
   \quad\text{is a union of isolated vertices and cycles of length at least five.}
   \tag{15}
   \]
   Indeed, \(d_G(v)=n-5=t+1\), and
   \[
   H-N_H[v]=\overline{G[N_G(v)]}.
   \]
   Apply Lemma 1.

The next two steps show that \(H\) has at most two triangles.

## 6. Triangles of \(H\) are vertex-disjoint

By (13), two triangles can share at most one vertex. Suppose that
\[
cab,\qquad cde
\]
are triangles sharing \(c\).

There are no edges between \(\{a,b\}\) and \(\{d,e\}\): any such edge would put an edge incident with \(c\) in two triangles. Put
\[
F=\{a,b,c,d,e\}.
\]
Every vertex of \(F\) has degree four, and \(N_H[c]=F\).

For \(s\in\{a,b,d,e\}\), let
\[
A_s=N_H(s)\setminus F.
\]
Each \(A_s\) has size two. Moreover,
\[
A_a\cap A_b=\varnothing,
\qquad
A_d\cap A_e=\varnothing,
\tag{16}
\]
because an outside common neighbor would put \(ab\) or \(de\) in a second triangle.

By (14), each cross-pair from \(\{a,b\}\times\{d,e\}\) has a common neighbor besides \(c\). Thus each cross-intersection of the corresponding \(A_s\)'s is nonempty. Together with (16) and their sizes, this forces four distinct vertices \(x,y,z,w\) such that
\[
A_a=\{x,y\},\quad
A_b=\{z,w\},\quad
A_d=\{x,z\},\quad
A_e=\{y,w\}.
\tag{17}
\]
Their neighborhoods within \(F\) are therefore
\[
\begin{array}{c|c}
\text{vertex}&\text{neighbors in }F\\ \hline
x& a,d\\
y& a,e\\
z& b,d\\
w& b,e .
\end{array}
\tag{18}
\]

Each of \(x,y,z,w\) has degree at least three. In \(H-F=H-N_H[c]\), its degree is its degree in \(H\) minus two. By (15), this cannot be one. Hence all four have degree four, and each has exactly two neighbors outside \(F\).

Now apply (15) at \(a\). The vertex \(z\) remains in \(H-N_H[a]\), as does its neighbor \(d\). Of the four neighbors of \(z\), the removed ones are \(b\) and any neighbors in \(\{x,y\}\). Its remaining degree must be two. Hence \(z\) has exactly one neighbor in \(\{x,y\}\). The same holds for \(w\). Applying the symmetric argument at \(b\), the edges between
\[
\{x,y\}\quad\text{and}\quad\{z,w\}
\]
form a perfect matching.

Likewise, applying (15) at \(d,e\), the edges between
\[
\{x,z\}\quad\text{and}\quad\{y,w\}
\]
form a perfect matching.

These two conditions leave exactly two possibilities for the edges among the four vertices:
\[
\{xy,xz,yw,zw\},
\qquad\text{or}\qquad
\{xw,yz\}.
\tag{19}
\]

The first possibility is a four-cycle component of \(H-F\): it uses both neighbors outside \(F\) of each of its vertices. This contradicts (15) at \(c\).

In the second possibility, write their remaining neighbors outside \(F\cup\{x,y,z,w\}\) as
\[
\rho_x,\rho_y,\rho_z,\rho_w.
\]
For example,
\[
N_H(x)=\{a,d,w,\rho_x\},
\qquad
N_H(y)=\{a,e,z,\rho_y\}.
\]
The nonadjacent degree-four vertices \(x,y\) have the common neighbor \(a\), and (14) forces
\[
\rho_x=\rho_y.
\]
Using \(x,z\) and \(y,w\) similarly gives
\[
\rho_x=\rho_y=\rho_z=\rho_w=\rho.
\]
But \(\rho\in H-F\) has all four of \(x,y,z,w\) as neighbors there, contradicting the maximum-degree-two assertion in (15).

Thus two triangles cannot share a vertex.

## 7. At most two triangles

Let \(P,Q\) be distinct triangles of \(H\). By the preceding section, they are disjoint. By (13), the edges between them form a matching.

I claim that this matching is perfect.

For \(v\in P\cup Q\), put
\[
R_v=N_H(v)\setminus(P\cup Q).
\]
The sets \(R_v\) belonging to distinct vertices of the same triangle are disjoint, since an outside vertex has at most one neighbor in that triangle.

Let \(m\) be the number of edges between \(P,Q\).

If \(m\le1\), choose two unmatched vertices \(a_1,a_2\in P\) and an unmatched vertex \(b\in Q\). For each \(i\), all common neighbors of \(a_i,b\) are outside \(P\cup Q\). Both relevant outside-neighbor sets have size two, so (14) forces
\[
R_{a_1}=R_b=R_{a_2},
\]
contrary to their disjointness.

If \(m=2\), let \(a_0\in P,b_0\in Q\) be the unmatched vertices. Again,
\[
R_{a_0}=R_{b_0}.
\tag{20}
\]
Choose a matched vertex \(a_1\in P\). It has exactly one neighbor outside \(P\cup Q\). The pair \(a_1,b_0\) has exactly one common neighbor within \(P\cup Q\), namely the vertex of \(Q\) matched to \(a_1\). Equation (14) forces its outside neighbor into
\[
R_{b_0}=R_{a_0},
\]
again contradicting the disjointness of outside-neighbor sets belonging to vertices of \(P\).

Therefore \(m=3\): every two triangles are joined by a perfect matching.

Suppose now that there are three triangles \(P,Q,R\). Each of their nine vertices has:

- two neighbors in its own triangle;
- one neighbor in each of the other two triangles.

Its degree is already four. Hence these nine vertices form a component \(H_0\) of \(H\).

The graph \(H\) has no \(K_4\), by (13). Therefore
\[
p(H_0)=6:
\]
the three triangles achieve six, and cliques of order at most three cannot achieve more on nine vertices. After deleting any vertex \(v\in H_0\), the remaining eight vertices have clique-packing savings at most
\[
\left\lfloor\frac{2\cdot8}{3}\right\rfloor=5.
\]
By additivity,
\[
p(H-v)<p(H),
\]
contradicting (8).

Thus \(H\) has at most two triangles.

## 8. Completing the order bound

We can now find two nonadjacent vertices of \(H\) whose deletion destroys all its triangles.

- If \(H\) has no triangle, take the endpoints of any edge of \(G\).
- If \(H\) has one triangle, take a vertex of that triangle and any of its neighbors in \(G\).
- If \(H\) has two triangles, the edges between them form a perfect matching. Choose one vertex from each triangle that are not matched to one another.

In every case, the chosen pair \(x,y\) is an edge of \(G\), and
\[
H-\{x,y\}
\]
is triangle-free. Equivalently,
\[
\alpha(G-\{x,y\})\le2.
\]
Lemma 2 forces \(G=K_t\), contrary to the assumption.

Hence \(n=t+6\) is impossible for a noncomplete double-critical graph. Together with Section 4,
\[
\boxed{|V(G)|\ge t+7.}
\]

## 9. What remains unresolved

This does not prove the double-critical graph conjecture.

The argument excludes complements of maximum degree at most three and, using the additional relation \(n-t=6\), excludes that entire order layer. Already when \(n-t=7\), the complement may have degree-five vertices and triangles sharing an edge; the triangle analysis above no longer applies.

In particular, no universal vertex has been established in an arbitrary double-critical graph. The general case remains unresolved by this argument.