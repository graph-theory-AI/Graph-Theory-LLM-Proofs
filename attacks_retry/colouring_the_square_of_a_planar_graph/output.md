```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the sharp conjectured list-colouring bound for planar graphs with vertex cover at most five and maximum degree at least 20.",
  "would_publish": false,
  "caveats": "The unrestricted planar conjecture remains unresolved; novelty of this restricted-class result is not claimed."
}
```

# 1. Result and scope

Write \(\tau(G)\) for the minimum size of a vertex cover of \(G\). The following extends the vertex-cover range treated in the supplied previous attempt.

**Theorem 1.** Let \(D\ge 3\), and let \(G\) be a finite simple planar graph with maximum degree at most \(D\) and \(\tau(G)\le 5\). Then
\[
\chi_\ell(G^2)\le
\max\left\{D+11,\left\lfloor\frac{3D}{2}\right\rfloor+1\right\}.
\tag{1}
\]
In particular, if \(D\ge20\), then
\[
\chi_\ell(G^2)\le \left\lfloor\frac{3D}{2}\right\rfloor+1.
\tag{2}
\]

The bound in (2) is sharp, even when \(\tau(G)\le3\).

There is also an ordinary-colouring extension:

**Corollary 2.** If every block of a planar graph \(G\) has a vertex cover of size at most five, and \(\Delta(G)\ge20\), then
\[
\chi(G^2)\le \left\lfloor\frac{3\Delta(G)}2\right\rfloor+1.
\]

Thus the partial result also covers graphs with arbitrarily large vertex-cover number.

The proof is self-contained apart from Hall’s theorem and the Tutte–Berge matching formula. I reprove the complement-matching list-colouring certificate from the supplied lead; its asserted four-cover theorem is not assumed.

# 2. Two matching certificates

## 2.1. Turning nonedges into a list-colouring bound

**Lemma 3.** If \(H\) has \(n\) vertices and \(\overline H\) has a matching of size \(r\), then
\[
\chi_\ell(H)\le n-r.
\]

**Proof.** Add edges to \(H\) until its only nonedges are the \(r\) matched pairs. The resulting supergraph is complete multipartite, with \(k=n-r\) parts, each of size one or two. It suffices to show that this graph is \(k\)-choosable.

Proceed by induction on \(k\). If the two lists in some two-vertex part have a common colour, give that colour to both vertices, delete the part, and remove the colour from all remaining lists. Induction applies.

Otherwise, the two lists in every two-vertex part are disjoint. Hall’s condition now holds for the family of vertex lists. A nonempty set of at most \(k\) vertices has at least \(k\) colours in its union. A larger set contains both vertices of some two-vertex part, so its list union has size at least \(2k\), which is at least the total number of vertices. Distinct representatives therefore give a proper colouring. ∎

## 2.2. Pairing disjoint edges of a multigraph

For a loopless multigraph \(M\), let \(J(M)\) be the graph whose vertices are the edge copies of \(M\), with two vertices adjacent precisely when the corresponding edges are disjoint.

**Lemma 4.** If \(M\) has \(m\) edges, counted with multiplicity, then
\[
m-\nu(J(M))
=
\max\left\{
\left\lceil\frac m2\right\rceil,\,
\max_v d_M(v),\,
\max_{|T|=3}|E(M[T])|
\right\}.
\tag{3}
\]

**Proof.** Put \(J=J(M)\). First, every pairwise-intersecting family of edges of a loopless multigraph is contained in a star or a triangle. Indeed, if such a family has no common endpoint, it contains edges \(ab,ac,bc\); every edge meeting all three lies in that triangle. Hence
\[
\alpha(J)=
\max\left\{\max_v d_M(v),\ \max_{|T|=3}|E(M[T])|\right\}.
\tag{4}
\]

We prove
\[
m-\nu(J)=\max\{\alpha(J),\lceil m/2\rceil\}.
\tag{5}
\]

The lower bound is immediate. For the upper bound, consider \(J-X\), where \(X\subseteq V(J)\).

If \(J-X\) has a nonbipartite component, that component contains every vertex of \(J-X\). To see this, suppose an edge \(ab\) of \(M\) represents a vertex in another component. Every edge represented in the nonbipartite component must meet \(ab\). But the disjointness graph of edges all meeting \(ab\) is bipartite: split them according to whether they meet \(a\) or \(b\), assigning parallel copies of \(ab\), which are isolated in this disjointness graph, arbitrarily. This is a contradiction.

Thus \(J-X\) is either bipartite or connected. Let \(o(J-X)\) denote its number of odd components.

* If \(J-X\) is bipartite, choosing the larger side of each component gives
  \[
  \frac{|V(J-X)|+o(J-X)}2\le \alpha(J).
  \]
* If \(J-X\) is connected and nonbipartite, then
  \[
  \frac{|V(J-X)|+o(J-X)}2
  =\left\lceil\frac{|V(J-X)|}{2}\right\rceil
  \le\left\lceil\frac m2\right\rceil.
  \]

The Tutte–Berge formula gives
\[
m-\nu(J)
=\max_{X\subseteq V(J)}
\frac{m-|X|+o(J-X)}2.
\]
This proves (5), and then (3) follows from (4). ∎

# 3. Proof of Theorem 1

Set
\[
Q=\left\lfloor\frac{3D}{2}\right\rfloor,
\qquad
K=\max\{D+11,Q+1\}.
\]

Graphs on fewer than five vertices are immediate. Otherwise, enlarge a vertex cover to a set \(C\) of exactly five vertices.

Delete all vertices outside \(C\) having degree at most one, obtaining \(G_0\). Such a deleted vertex cannot be internal to a path of length two between retained vertices, so
\[
G_0^2=G^2[V(G_0)].
\]
Moreover, a deleted leaf has at most \(D\) neighbours in \(G^2\). Since \(K\ge D+1\), a \(K\)-list colouring of \(G_0^2\) extends greedily to all deleted vertices.

It remains to colour \(G_0^2\).

## 3.1. The bounded exceptional set

Partition
\[
V(G_0)=C\mathbin{\dot\cup} X\mathbin{\dot\cup} P,
\]
where vertices of \(X\) have degree two and vertices of \(P\) have degree at least three. All their neighbours lie in \(C\).

Write
\[
m=|X|,\qquad p=|P|,\qquad F=G_0[C],\qquad f=|E(F)|.
\]

The bipartite planar graph consisting of the edges between \(C\) and \(P\) has at least \(3p\) edges and at most \(2(5+p)-4\) edges. Consequently,
\[
p\le6.
\tag{6}
\]
Counting degrees in \(C\) also gives
\[
2m+3p+2f\le5D.
\tag{7}
\]

Two vertices outside \(C\) are adjacent in \(G_0^2\) exactly when their neighbourhoods in \(C\) intersect.

Construct a multigraph \(M\) on \(C\), putting one edge \(ij\) for each vertex of \(X\) with neighbourhood \(\{i,j\}\). By Lemma 4, the complement of \(G_0^2[X]\) has a matching of size \(m-q_0\), where
\[
q_0=
\max\left\{
\left\lceil\frac m2\right\rceil,\,
\max_i d_M(i),\,
\max_{|T|=3}|E(M[T])|
\right\}.
\tag{8}
\]
Leaving \(C\cup P\) unmatched, Lemma 3 gives
\[
\chi_\ell(G_0^2)\le q_0+p+5.
\tag{9}
\]

Assume from now on that
\[
q_0+p+5>K.
\tag{10}
\]

We treat the alternatives in (8).

## 3.2. Star and half-order alternatives

The star alternative cannot cause (10), because
\[
d_M(i)+p+5\le D+11\le K.
\]

Suppose next that \(q_0=\lceil m/2\rceil\). From (7),
\[
q_0+p+5
\le
\left\lfloor\frac{5D+p-2f+2}{4}\right\rfloor+5
\le
\left\lfloor\frac{5D}{4}\right\rfloor+7.
\tag{11}
\]
For \(D\le19\), the last expression is at most \(D+11\). For \(D\ge22\), it is at most \(Q+1\): check \(D=22,23\) directly, while for \(D\ge24\) the difference between \(3D/2\) and \(5D/4\) is at least six.

Thus only \(D=20,21\) remain. In both cases \(K=D+11\), and (11) is at most \(K+1\).

If \(f\ge1\), the first bound in (11), using \(p\le6\), is already at most \(K\). Hence (10) forces \(F\) to be edgeless.

If every vertex of \(P\) has degree five, including the possibility \(P=\varnothing\), then
\[
2m+5p\le5D,
\]
so
\[
q_0+p+5
\le
\left\lfloor\frac{5D-p+2}{4}\right\rfloor+5
\le K.
\]
Therefore some \(u\in P\) has degree three or four. Choose \(i\in C\setminus N(u)\). Since \(F\) is edgeless, \(i\) and \(u\) are nonadjacent in \(G_0^2\). This nonedge is disjoint from the matching within \(X\), so it increases that matching by one. Lemma 3 now gives
\[
\chi_\ell(G_0^2)\le q_0+p+4\le K.
\]

This completes the half-order alternative.

## 3.3. The triangle alternative

It remains that \(q_0\) is attained by a triangle. Relabel
\[
C=\{1,2,3,4,5\},\qquad T=\{1,2,3\}.
\]

Let \(x_{ij}\) be the number of degree-two vertices with neighbourhood \(\{i,j\}\), and put
\[
r=x_{12}+x_{13}+x_{23}=q_0,
\]
\[
c_i=x_{i4}+x_{i5}\quad(i\in T),\qquad
c=c_1+c_2+c_3,\qquad z=x_{45}.
\]
Thus
\[
m=r+c+z.
\]

Partition \(P\) into \(P_1,P_2,P_3\), according to the number of neighbours in \(T\), and write \(p_j=|P_j|\). These sets exhaust \(P\): a vertex with at least three neighbours in a five-element set must meet \(T\).

For \(i\in T\), let
\[
y_i=\bigl|\{u\in P_1:N(u)\cap T=\{i\}\}\bigr|.
\]
Every such vertex has neighbourhood exactly \(\{i,4,5\}\), and
\[
y_1+y_2+y_3=p_1.
\]

### An initial matching

For \(\{i,j,k\}=T\), pair each of the following vertices with a distinct vertex of type \(\{j,k\}\):

* the \(c_i\) degree-two vertices of types \(\{i,4\}\) and \(\{i,5\}\);
* the \(y_i\) vertices of \(P_1\) whose sole neighbour in \(T\) is \(i\).

These are nonedges of \(G_0^2\), since the paired neighbourhoods are disjoint.

We must check that there are enough vertices of type \(\{j,k\}\). Write
\[
f_i=d_F(i),\qquad h_i=|N(i)\cap P|.
\]
The degree bound at \(i\) gives
\[
f_i+r-x_{jk}+c_i+h_i\le D.
\]
Hence the number left in type \(\{j,k\}\) after the proposed pairings is
\[
a_i:=x_{jk}-c_i-y_i
\ge r-D+f_i+h_i-y_i
\ge r-D.
\tag{12}
\]
By (10),
\[
r\ge K-p-4.
\]
Since \(K\ge D+11\) and \(p\le6\), (12) implies \(a_i\ge1\). Thus the initial matching exists and has size \(c+p_1\).

Put
\[
A=a_1+a_2+a_3=r-c-p_1,
\qquad
q=r+p_2+p_3.
\]

The \(z\) vertices of type \(\{4,5\}\) can each be paired with any remaining triangle-type vertex.

### Two useful bounds

First, define
\[
B=c+z+p+5=m-r+p+5.
\]
Using (7), \(r\ge K-p-4\), and \(p\le6\), we obtain
\[
\begin{aligned}
B
&\le
\left\lfloor\frac{5D+p}{2}\right\rfloor-K+9\\
&\le D+Q+12-K\\
&\le K.
\end{aligned}
\tag{13}
\]
The last inequality follows by adding \(K\ge D+11\) and \(K\ge Q+1\).

Second, let
\[
m_T=|E(F[T])|,
\qquad
g=|E_F(T,\{4,5\})|.
\]
Counting degrees at \(1,2,3\) gives the exact identity
\[
d_1+d_2+d_3
=
2r+c+p_1+2p_2+3p_3+2m_T+g.
\]
Therefore
\[
q\le Q.
\tag{14}
\]
Writing
\[
\delta=Q-q,\qquad \varepsilon=3D-2Q\in\{0,1\},
\]
we also have
\[
2m_T+g\le 2\delta+\varepsilon.
\tag{15}
\]

### When no cover vertices need pairing

After the initial matching, pair as many of the \(z\) vertices of type \(\{4,5\}\) as possible with free triangle-type vertices. The resulting matching certificate has value
\[
q+5+\max\{0,z-A\}
=
\max\{q+5,B\}.
\tag{16}
\]
Thus, if \(q+5\le K\), equations (13) and (16) finish the proof.

Assume instead that \(q+5>K\), and set
\[
s=q+5-K.
\]
By (14),
\[
1\le s\le4,\qquad s\le4-\delta.
\tag{17}
\]
We will obtain \(s\) additional matching edges using cover vertices.

### Enough free triangle vertices

For every \(i\in T\), equation (12) gives
\[
\begin{aligned}
a_i
&\ge r-D\\
&=q-p_2-p_3-D\\
&\ge q-6-D\\
&=s+(K-D-11)\\
&\ge s.
\end{aligned}
\tag{18}
\]
Moreover,
\[
A-z=q+5-B\ge q+5-K=s.
\tag{19}
\]

Thus each triangle type has at least \(s\) available vertices, and after reserving \(s\) of them there will still be enough to pair all \(z\) vertices of type \(\{4,5\}\).

### Enough eligible cover vertices

Call a cover vertex *eligible* if it is nonadjacent in \(G_0^2\) to every vertex of at least one triangle type.

For \(i\in T\), it is eligible whenever it is isolated in \(F[T]\): then it is nonadjacent to type \(T\setminus\{i\}\).

For \(v\in\{4,5\}\), it is eligible whenever it has at most one neighbour in \(T\) in \(F\): choose a pair in \(T\) avoiding that possible neighbour.

These assertions follow from the following exact criterion. If \(u\notin C\) has neighbourhood \(S\subseteq C\), then \(v\in C\) is nonadjacent to \(u\) in \(G_0^2\) precisely when
\[
v\notin S
\quad\text{and}\quad
N_F(v)\cap S=\varnothing.
\tag{20}
\]

At most \(m_T+1\) vertices of \(T\) are nonisolated in \(F[T]\). Also, at most \(\lfloor g/2\rfloor\) vertices of \(\{4,5\}\) have two or more neighbours in \(T\). Hence, by (15), the number of ineligible cover vertices is at most
\[
m_T+1+\left\lfloor\frac g2\right\rfloor
=
1+\left\lfloor\frac{2m_T+g}{2}\right\rfloor
\le \delta+1.
\]
There are therefore at least \(4-\delta\ge s\) eligible cover vertices.

Choose \(s\) of them. Pair each with a free vertex of a permissible triangle type. Equation (18) makes these choices possible even if all \(s\) cover vertices require the same type. Then use (19) to pair all \(z\) vertices of type \(\{4,5\}\) with remaining triangle-type vertices.

The resulting matching in \(\overline{G_0^2}\) has size
\[
c+p_1+z+s.
\]
Since \(|V(G_0)|=r+c+z+p+5\), Lemma 3 yields
\[
\chi_\ell(G_0^2)
\le r+p_2+p_3+5-s
=q+5-s
=K.
\]

This covers every alternative in (8). Extending to the deleted leaves proves Theorem 1. ∎

# 4. Block extension

Let \(D=\Delta(G)\ge20\) and \(K=\lfloor3D/2\rfloor+1\). By Theorem 1, the square of every block has an ordinary \(K\)-colouring, using the global degree bound \(D\).

Add blocks in a rooted block-tree order. Suppose a new block \(B\) meets the already coloured graph at the cutvertex \(v\). Take a \(K\)-colouring of \(B^2\). Its colours can be permuted so that:

* the colour at \(v\) agrees with its existing colour;
* the neighbours of \(v\) in \(B\) receive colours unused on its already coloured neighbours.

Indeed, the neighbours of \(v\) in \(B\) have distinct colours, and
\[
K-1\ge D
\]
provides enough available colours for the required permutation.

The only square-edges crossing between the old and new portions, apart from those involving \(v\), join old and new neighbours of \(v\). Thus the combined colouring is proper. Iterating proves Corollary 2.

This permutation argument does **not** establish the corresponding list-colouring block extension.

# 5. Sharpness

For \(D\ge20\), take vertices \(a,b,c\), with edges \(ab,bc\). Add independent sets of degree-two vertices as follows:
\[
\begin{array}{c|c}
\text{neighbourhood}&\text{number}\\ \hline
\{a,b\}&\lfloor D/2\rfloor-1\\
\{b,c\}&\lceil D/2\rceil-1\\
\{a,c\}&\lfloor D/2\rfloor.
\end{array}
\]

The graph is planar: draw the length-two paths in parallel bundles along the sides of a triangle, retaining the direct edges \(ab,bc\). Its maximum degree is \(D\), and \(\{a,b,c\}\) is a vertex cover.

Every two added vertices share a neighbour. The path \(a-b-c\) also puts every hub within distance two of every added vertex. Hence the graph has diameter two and order
\[
3+\left(\left\lfloor\frac D2\right\rfloor-1\right)
+\left(\left\lceil\frac D2\right\rceil-1\right)
+\left\lfloor\frac D2\right\rfloor
=
\left\lfloor\frac{3D}{2}\right\rfloor+1.
\]
Its square is therefore the complete graph of that order. This verifies sharpness of (2).

# 6. What remains open in this attack

The result does not cover arbitrary planar blocks, and it does not establish the conjectured small-degree bounds for five-cover graphs.

The essential restriction is structural, not merely numerical. With five cover vertices, every outside vertex of degree at least three meets any chosen cover triple. That fact drives the degree count and matching construction in the triangle case. It fails for a cover of size six, where a degree-three vertex may have its entire neighbourhood outside the chosen triple.

Accordingly, this is a proved restricted-class result—including list colouring and a sharp bound—but not a resolution of Wegner’s conjecture.