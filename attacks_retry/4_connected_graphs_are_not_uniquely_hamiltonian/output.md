```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any counterexample satisfies n ≥ 13 and 5n ≥ 18δ − 21, and an even-order counterexample satisfies n ≥ 4δ − 2.",
  "would_publish": false,
  "caveats": "The conjecture is not resolved here; the bounds are self-contained but are not claimed to be new or best known."
}
```

# A strengthened necessary-condition theorem

All graphs below are finite, undirected, and simple. Hamilton cycles are distinguished by their edge sets.

I obtain the following partial result. It uses minimum degree rather than the full force of 4-connectivity.

**Theorem.** Let \(G\) be uniquely Hamiltonian, of order \(n\) and minimum degree \(\delta\ge 4\). Then
\[
n\ge 13,
\tag{1}
\]
\[
n\text{ even}\quad\Longrightarrow\quad n\ge 4\delta-2,
\tag{2}
\]
and
\[
5n\ge
\begin{cases}
18\delta-15,&\delta\text{ odd},\\[2mm]
18\delta-21,&\delta\text{ even}.
\end{cases}
\tag{3}
\]
Furthermore, if \(C\) is its unique Hamilton cycle and
\[
n<4\delta-4,
\]
then \(G-E(C)\) has exactly three connected components, all of odd order.

Thus the proposed conjecture holds on at most twelve vertices, and it holds for 4-connected Hamiltonian graphs violating any of the applicable inequalities above.

The parity ingredients from the supplied attempt are valid; I checked them and include proofs. The additional ingredient is a counting restriction on pairs of cycle edges that would permit a two-edge switch. I do not assume the supplied attempt’s claimed order bound.

## 1. Parity tools

### 1.1. A fixed-edge parity lemma

**Lemma 1.** Let \(uv\in E(J)\). If every vertex outside \(\{u,v\}\) has odd degree in \(J\), then the number of Hamilton cycles containing \(uv\) is even.

**Proof.** Form an auxiliary graph on the oriented Hamilton paths
\[
P=(p_1,\ldots,p_n),\qquad p_1=u,\quad p_2=v.
\]
For every edge \(p_np_i\), where \(2\le i\le n-2\), join \(P\) to
\[
(p_1,\ldots,p_i,p_n,p_{n-1},\ldots,p_{i+1}).
\]
These rotations are reversible and give distinct neighbors. Hence
\[
d_{\rm aux}(P)
=d_J(p_n)-1-\mathbf 1_{\{up_n\in E(J)\}}.
\]
Since \(p_n\notin\{u,v\}\), this auxiliary degree is odd precisely when \(up_n\in E(J)\).

Such paths correspond bijectively to Hamilton cycles containing \(uv\): orient the cycle to begin with \(u,v\), then delete its closing edge. The handshaking lemma proves the assertion. \(\square\)

We also use the elementary fact that, in a connected graph \(Q\), every even-cardinality set \(T\subseteq V(Q)\) is the set of odd-degree vertices of some spanning subgraph. For example, root a spanning tree and include a parent–child edge exactly when the child’s subtree contains an odd number of vertices of \(T\).

### 1.2. Components after deleting the Hamilton cycle

Fix a Hamilton cycle \(C\), and write
\[
H=G-E(C).
\]

**Lemma 2.** The graph \(G\) has a second Hamilton cycle if any of the following holds:

1. \(H\) has no odd-order component;
2. \(H\) has exactly one odd-order component;
3. \(H\) has exactly two odd-order components and a \(C\)-edge joins them.

**Proof.** Choose an exceptional set \(S\) as follows:

- \(S=\varnothing\) in the first case;
- \(S=\{x\}\), with \(x\) in the odd component, in the second;
- \(S=\{x,y\}\), where \(xy\in E(C)\) joins the odd components, in the third.

In each component \(Q\) of \(H\), the set \(V(Q)\setminus S\) has even cardinality. The parity-subgraph fact therefore supplies \(F\subseteq H\) whose odd-degree vertices are exactly \(V(G)\setminus S\).

In \(J=C\cup F\), all vertices outside \(S\) have odd degree. Apply Lemma 1 to a \(C\)-edge whose endpoints contain \(S\), choosing an arbitrary edge if \(S=\varnothing\). Since \(C\) is counted, another Hamilton cycle exists. \(\square\)

Consequently, in a uniquely Hamiltonian graph:

- \(H\) has at least three components;
- if \(H\) has exactly two odd-order components, there is no \(C\)-edge between them.

The first assertion follows because, if \(H\) had two odd-order components and no others, the spanning cycle would necessarily have an edge between them.

### 1.3. Deleting an interval of the cycle

**Lemma 3.** Suppose \(S\) is a nonempty proper interval of consecutive vertices on \(C\), with at least two vertices outside \(S\). If every component of \(H-S\) has even order, then \(G\) has a second Hamilton cycle.

**Proof.** Choose \(F\subseteq H-S\) with odd degree at every vertex outside \(S\), and put \(J=C\cup F\). Every vertex in \(S\) has degree two in \(J\), and every vertex outside \(S\) has odd degree.

Write the corresponding cycle segment as
\[
a,s_1,\ldots,s_t,b.
\]
Replace it by \(a,x,y,b\), where \(x,y\) are new vertices. In the resulting graph, all vertices outside \(\{x,y\}\) have odd degree. Lemma 1 gives an even, positive number of Hamilton cycles through \(xy\).

Because \(x,y\) have degree two, replacing their forced path by the original segment gives a bijection with the Hamilton cycles of \(J\). Hence \(J\), and therefore \(G\), has a second Hamilton cycle. \(\square\)

Here is a useful consequence.

**Lemma 4.** If \(G\) is uniquely Hamiltonian and \(H\) is a disjoint union of \(k\) cliques, then
\[
n\le 2^{k-1}.
\]

**Proof.** If all clique orders are even, Lemma 2 already gives a contradiction. Otherwise let
\[
v\in\mathbb F_2^k\setminus\{0\}
\]
record their order parities.

List the vertices around \(C\). For \(0\le j<n\), let \(p_j\in\mathbb F_2^k\) record the component-membership parities of the first \(j\) vertices. The quotient
\[
\mathbb F_2^k/\langle v\rangle
\]
has \(2^{k-1}\) elements.

If \(n>2^{k-1}\), two of these prefix vectors have the same quotient image. The interval between them has parity vector either \(0\) or \(v\). In the latter case, its complementary cyclic interval has parity vector \(0\).

Thus there is a nonempty proper cyclic interval \(T\) containing an even number of vertices from every clique. In particular, \(|T|\ge2\), and every component of \(H[T]\) has even order. Apply Lemma 3 with \(S=V(G)\setminus T\). \(\square\)

## 2. Restrictions from two-edge switches

Orient \(C\) cyclically. For two distinct oriented cycle edges \(xy\) and \(zw\), the simultaneous presence of
\[
xz,\ yw\in E(H)
\tag{4}
\]
would give a second Hamilton cycle: delete \(xy,zw\) and insert \(xz,yw\). If both proposed chords lie in \(H\), the four endpoints are automatically distinct.

Put
\[
r=\delta-1.
\]
Every component \(Q_i\) of \(H\) has order
\[
m_i=r+q_i,\qquad q_i\ge0,
\]
because \(\delta(H)=\delta-2=r-1\). Each vertex of \(Q_i\) has at most \(q_i\) nonneighbors within \(H[Q_i]\).

Let \(x_{ij}\) count the oriented \(C\)-edges from \(Q_i\) to \(Q_j\). In particular,
\[
\sum_j x_{ij}=m_i.
\tag{5}
\]

**Lemma 5.** If \(G\) is uniquely Hamiltonian, then, for \(i\ne j\),
\[
x_{ij}\le q_i+q_j+1.
\tag{6}
\]
If both \(q_i,q_j\) are odd, this improves to
\[
x_{ij}\le q_i+q_j.
\tag{7}
\]
Also,
\[
x_{ii}\le
\begin{cases}
0,&q_i=0,\\
2q_i-1,&q_i>0.
\end{cases}
\tag{8}
\]

**Proof of (6)–(7).** Consider the \(t=x_{ij}\) cycle edges from \(Q_i\) to \(Q_j\). On these \(t\) occurrences, form two graphs:

- join two occurrences in \(R\) if their origins are nonadjacent in \(H[Q_i]\);
- join them in \(S\) if their destinations are nonadjacent in \(H[Q_j]\).

The switch obstruction (4) says
\[
R\cup S=K_t.
\]
Moreover,
\[
\Delta(R)\le q_i,\qquad \Delta(S)\le q_j.
\]
Thus \(t-1\le q_i+q_j\), proving (6).

If \(q_i,q_j\) are odd and equality \(t=q_i+q_j+1\) holds, then \(t\) is odd. Covering every edge of \(K_t\) forces every degree of \(R\) to equal \(q_i\). This would be an odd-regular graph on an odd number of vertices, which is impossible. This proves (7).

**Proof of (8).** If \(q_i=0\), then \(H[Q_i]\) is complete, so it contains every possible internal edge and \(C\) has none.

Suppose \(q=q_i>0\) and fix an internal cycle edge \(e=(x,y)\). Among the other internal cycle edges \(f=(z,w)\), let
\[
A=\{f:xz\notin E(H)\},\qquad
B=\{f:yw\notin E(H)\}.
\]
Every other internal cycle edge belongs to \(A\cup B\), by (4).

Let \(\epsilon_+\) indicate whether the cycle edge leaving \(y\) is internal to \(Q_i\), and let \(\epsilon_-\) indicate whether the cycle edge entering \(x\) is internal.

Since \(xy\notin E(H)\),
\[
|A|\le q-1+\epsilon_+,\qquad
|B|\le q-1+\epsilon_-.
\]
When \(\epsilon_+=1\), the edge leaving \(y\) belongs to both \(A\) and \(B\). When \(\epsilon_-=1\), the edge entering \(x\) also belongs to both. These are distinct edges. Therefore
\[
x_{ii}-1
=|A\cup B|
\le 2q-2,
\]
proving (8). \(\square\)

## 3. The even-order bound

First consider the case where \(H\) has exactly three components, two odd and one even. Call the odd components \(A,B\), and the even component \(D\). Write
\[
|A|=r+q_A,\quad |B|=r+q_B,\quad |D|=r+q_D,
\qquad s=q_A+q_B+q_D.
\]

There are no \(C\)-edges between \(A\) and \(B\), by Lemma 2. The number of cycle edges leaving a component equals the number entering it, so
\[
x_{AD}=x_{DA},\qquad x_{BD}=x_{DB}.
\]
Let
\[
\epsilon_A=\mathbf1_{\{q_A>0\}},\qquad
\epsilon_B=\mathbf1_{\{q_B>0\}}.
\]
Using (8),
\[
x_{AD}=|A|-x_{AA}\ge r-q_A+\epsilon_A,
\]
and similarly
\[
x_{BD}\ge r-q_B+\epsilon_B.
\]
All these edges enter \(D\), giving
\[
r+q_D\ge 2r-q_A-q_B+\epsilon_A+\epsilon_B.
\]
Hence
\[
s\ge r+\epsilon_A+\epsilon_B.
\tag{9}
\]

### 3.1. Orders below \(4r\)

If \(n<4r\), then \(H\) has exactly three components: it has at least three, each of order at least \(r\).

Lemma 2 excludes zero or one odd component. Equation (9) excludes exactly two odd components, since that would give
\[
n=3r+s\ge4r.
\]
Thus all three components are odd, and in particular \(n\) is odd.

### 3.2. The boundary order \(n=4r\)

Suppose now that \(n=4r\).

If \(H\) has four components, all have order \(r\), and all are cliques. Lemma 4 would give
\[
4r=n\le 8,
\]
contrary to \(r\ge3\).

Thus \(H\) has three components. Since \(n\) is even, Lemma 2 forces exactly two odd components \(A,B\). Here \(s=r\), so (9) forces
\[
q_A=q_B=0.
\]
Consequently,
\[
H[A]=H[B]=K_r,\qquad |D|=2r,
\]
and \(r\) is odd.

There are no cycle edges inside \(A\), inside \(B\), or between \(A\) and \(B\). Counting cycle incidences therefore shows that \(C\) alternates between \(A\cup B\) and \(D\). Write
\[
C=(u_1,d_1,u_2,d_2,\ldots,u_{2r},d_{2r},u_1),
\]
where \(u_i\in A\cup B\) and \(d_i\in D\).

Give \(d_i\) the type
\[
\bigl(\operatorname{comp}(u_i),\operatorname{comp}(u_{i+1})\bigr)
\in\{AA,AB,BA,BB\}.
\]
If \(d_id_j\in E(H[D])\), the switch obstruction implies both
\[
\operatorname{comp}(u_i)\ne\operatorname{comp}(u_j)
\quad\text{and}\quad
\operatorname{comp}(u_{i+1})\ne\operatorname{comp}(u_{j+1}).
\]
Thus edges of \(H[D]\) can join only complementary types:
\[
AA\leftrightarrow BB,\qquad AB\leftrightarrow BA.
\]

Both \(A\) and \(B\) occur in the cyclic word \(u_1,\ldots,u_{2r}\), so types \(AB\) and \(BA\) occur. Since \(H[D]\) is connected, types \(AA,BB\) cannot occur. It follows that the \(u_i\)'s alternate between \(A\) and \(B\), and that \(H[D]\) is bipartite with parts of size \(r,r\) and minimum degree at least \(r-1\).

Delete the four consecutive cycle vertices
\[
S=\{u_i,d_i,u_{i+1},d_{i+1}\}.
\]
The remaining portions of \(A\) and \(B\) are even-order cliques \(K_{r-1}\). In \(D\), one vertex was deleted from each bipartition class. The remaining bipartite graph has parts of size
\[
s_0=r-1\ge2
\]
and minimum degree at least \(s_0-1\).

Every component of this remaining graph has even order. Indeed, if \(s_0\ge3\), it is connected: two components would each require at least \(s_0-1\) vertices from each part. If \(s_0=2\), minimum degree at least one leaves either a connected four-vertex graph or two edges.

Thus every component of \(H-S\) has even order. Lemma 3 gives a contradiction.

We have proved that \(n=4r\) is impossible, and that any smaller order is odd. Therefore
\[
n\text{ even}\quad\Longrightarrow\quad n\ge4r+2=4\delta-2.
\]

## 4. The general density bounds

If \(n\ge4r\), then
\[
5n\ge20r\ge18r+3
\]
because \(r\ge3\), so both claimed density bounds hold.

Assume therefore that \(n<4r\). By Section 3.1, \(H\) has three odd-order components. Write
\[
|Q_i|=r+q_i,\qquad s=q_1+q_2+q_3,
\qquad n=3r+s.
\]

### Case 1: \(r\) is even

All three \(q_i\) are positive odd integers. Summing (7) over the six ordered pairs of distinct components gives at most \(4s\) cross-component cycle edges. Summing (8) gives at most \(2s-3\) internal cycle edges. Hence
\[
n\le6s-3.
\]
Together with \(n=3r+s\), this yields
\[
5s\ge3r+3,\qquad
5n\ge18r+3=18\delta-15.
\]

### Case 2: \(r\) is odd

All three \(q_i\) are even.

If all are positive, (6) and (8) give
\[
n\le(4s+6)+(2s-3)=6s+3.
\]
Thus
\[
5n\ge18r-3=18\delta-21.
\]

If, say, \(q_1=0\), there are no internal cycle edges in \(Q_1\). Equations (5) and (6) give
\[
r=x_{12}+x_{13}\le q_2+q_3+2=s+2.
\]
Since \(r\) is odd and \(s\) is even, this implies \(s\ge r-1\). Consequently,
\[
n\ge4r-1
\]
and
\[
5n\ge20r-5\ge18r-3.
\]
This completes the proof of (3).

## 5. Excluding orders at most twelve

Suppose \(n\le12\).

Since \(H\) has at least three components of order at least \(\delta-1\), a value \(\delta\ge5\) would force \(\delta=5,n=12\), contrary to the even-order bound. Thus \(\delta=4\).

The density bound gives
\[
5n\ge51,
\]
so \(n\ge11\). The even-order bound excludes \(n=12\). It remains to exclude \(n=11\).

Here \(r=3\) and \(n<4r\), so \(H\) has three odd-order components, necessarily of orders
\[
3,\ 3,\ 5.
\]
Call them \(A,B,D\). The first two are triangles.

There are no cycle edges inside \(A\) or \(B\). There must be a cycle edge between them: otherwise all twelve cycle-edge incidences at \(A\cup B\) would go to \(D\), which has only ten available incidences.

Take a maximal consecutive block of \(C\) contained in \(A\cup B\) and containing such an edge. Its labels alternate, and its two boundary vertices are distinct vertices of \(D\).

A connected five-vertex graph of minimum degree at least two has at most one cut vertex. To see this, if \(z\) is a cut vertex, every component after deleting \(z\) has at least two vertices. There must therefore be exactly two two-vertex components, forcing the graph to be two triangles sharing \(z\); that graph has only one cut vertex.

Thus at least one boundary vertex \(d\in D\) is not a cut vertex of \(H[D]\). At that end of the chosen block, there are three consecutive cycle vertices, one each in \(D,A,B\). Delete these three vertices as \(S\).

The components of \(H-S\) are two copies of \(K_2\) and a connected four-vertex graph. All have even order, contradicting Lemma 3.

Therefore \(n\ge13\), completing the partial theorem.

## 6. What remains unresolved

These arguments give stronger density and order restrictions, but they do not use 4-connectivity beyond its implication \(\delta\ge4\).

In particular, they do not show that a uniquely Hamiltonian graph has a vertex cut of size at most three. Large sparse graphs of minimum degree four remain outside the scope of the bounds, and the interval-parity criterion need not be applicable to their chord components.

Thus this is a proved necessary-condition theorem for a potential counterexample, not a resolution of the conjecture.