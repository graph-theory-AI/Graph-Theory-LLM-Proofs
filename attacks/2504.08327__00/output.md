```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A hypothetical counterexample has a tightly constrained planar core; in particular, if that core is 3-colorable, then it is at least five edges below the extremal one-crossing bound.",
  "would_publish": false,
  "caveats": "The 4-chromatic-core case and the sparse 3-colorable-core case remain open, and some structural lemmas may overlap the source paper."
}
```

# Statement and scope

Let \(G\) be a finite simple \(5\)-critical graph drawable with at most one crossing. The conjecture asserts that \(G\) has a vertex of degree \(4\).

I do not resolve the conjecture. I prove a collection of structural restrictions on any counterexample. The strongest new reduction obtained here concerns the planar graph formed by deleting the two crossed edges.

## Partial theorem

Suppose, for contradiction, that \(G\) is \(5\)-critical, has crossing number at most one, and has no vertex of degree \(4\). Let

\[
n=|V(G)|,\qquad m=|E(G)|.
\]

Choose a good drawing with its unique crossing between independent edges

\[
e=a_1a_2,\qquad f=b_1b_2,
\]

and put

\[
J=G-\{e,f\},\qquad q=3n-5-m.
\]

Then:

1. \(q\ge 0\), and if
   \[
   h=\sum_{\substack{v\in V(G)\\d_G(v)\ge 7}}(d_G(v)-6),
   \]
   then the number \(n_5\) of degree-five vertices satisfies
   \[
   n_5=10+2q+h.
   \]
   In particular,
   \[
   n_5\ge 10+2q,\qquad
   0\le q\le \left\lfloor\frac{n-10}{2}\right\rfloor.
   \]

2. The planar graph \(J\) is \(2\)-edge-connected. Every triangle of \(J\) is facial, and \(J\) is \(K_4\)-free.

3. The graph \(G-e\) has at least
   \[
   \begin{cases}
   n+6,&n\text{ even},\\
   n+7,&n\text{ odd}
   \end{cases}
   \]
   distinct facial triangles. Thus \(G\) contains at least that many triangles.

4. The graph \(J\) has at least
   \[
   \begin{cases}
   n+4,&n\text{ even},\\
   n+5,&n\text{ odd}
   \end{cases}
   \]
   triangular faces. Moreover, at least
   \[
   \begin{cases}
   \dfrac n2+14,&n\text{ even},\\[2mm]
   \dfrac{n+33}{2},&n\text{ odd}
   \end{cases}
   \]
   edges of \(J\) are incident with two triangular faces. Each such pair of faces induces a diamond \(K_4-e\) in \(J\).

5. One has
   \[
   \chi(G-e)=\chi(G-f)=4,\qquad \chi(J)\in\{3,4\}.
   \]

6. If \(\chi(J)=3\), then:
   - the four crossing endpoints induce a \(K_4\) in \(G\);
   - the cycle
     \[
     a_1b_1a_2b_2a_1
     \]
     bounds a face of \(J\);
   - and
     \[
     q\ge 5+\left\lceil\frac h2\right\rceil.
     \]
     In particular,
     \[
     m\le 3n-10.
     \]

Thus any counterexample whose planar core \(J\) is \(3\)-colorable and has \(m\ge 3n-9\) is impossible. The remaining cases are:

- \(\chi(J)=4\), with no comparable density restriction obtained here; or
- \(\chi(J)=3\) and \(q\ge5\).

# Proof

## 1. Critical-graph preliminaries

A \(5\)-critical graph has minimum degree at least \(4\): after coloring \(G-v\) with four colors, a vertex of degree at most \(3\) could be assigned a missing color. Hence, under the assumption that there is no degree-four vertex,

\[
\delta(G)\ge5.
\]

A critical graph has no separating clique. Indeed, suppose that a clique \(S\), with \(|S|\le4\), separates two nonempty parts. Color each graph induced by \(S\) together with one component of \(G-S\). Since \(S\) is a clique, its vertices receive distinct colors, and color permutations make the colorings agree on \(S\). They then combine to a four-coloring of \(G\), a contradiction.

We also need an edge-connectivity observation.

### Lemma 1
Every \(5\)-critical graph is \(4\)-edge-connected.

### Proof
Suppose \(\delta_G(A)\) is an edge cut of size at most \(3\). Four-color \(G[A]\) and \(G[V(G)\setminus A]\). Permute the four colors on one side. Each cut edge forbids one equation of the form

\[
\pi(i)=j
\]

for the permutation \(\pi\). A single such equation is satisfied by \(3!=6\) of the \(24\) permutations. Thus at most \(3\cdot6=18<24\) permutations are forbidden. Some permutation makes every cut edge properly colored, giving a four-coloring of \(G\), a contradiction. \(\square\)

Since \(G\) is not planar by the Four Color Theorem, its crossing number is exactly one. A crossing-minimal drawing may be assumed good; in particular, the two crossed edges have four distinct endpoints.

Deleting one crossed edge gives a \(3\)-edge-connected plane graph, and deleting both gives a \(2\)-edge-connected plane graph.

## 2. Euler charge and the degree-five count

Let

\[
H=G-e.
\]

Then \(H\) is planar and has \(m-1\) edges. Therefore

\[
m-1\le3n-6,
\]

so

\[
q=3n-5-m\ge0.
\]

Equivalently,

\[
|E(H)|=3n-6-q.
\]

Because \(H\) is bridgeless, every face has length at least three, and its total face excess is

\[
\sum_{F\in \mathcal F(H)}(|F|-3)
  =3n-6-|E(H)|
  =q.
\]

Also,

\[
\sum_{v\in V(H)}(6-d_H(v))=12+2q.
\]

Only \(a_1,a_2\) lose degree when \(e\) is deleted. Hence

\[
\sum_{v\in V(G)}(6-d_G(v))=10+2q. \tag{1}
\]

Under \(\delta(G)\ge5\), the left side of (1) equals

\[
n_5-\sum_{d_G(v)\ge7}(d_G(v)-6)=n_5-h.
\]

Consequently,

\[
n_5=10+2q+h. \tag{2}
\]

In particular, \(n_5\ge10+2q\).

On the other hand, \(2m\ge5n\), while \(m=3n-5-q\). Thus

\[
6n-10-2q\ge5n,
\]

and therefore

\[
q\le \left\lfloor\frac{n-10}{2}\right\rfloor. \tag{3}
\]

This proves item 1.

## 3. Triangles and diamonds in the planar core

For \(H=G-e\), Euler's formula gives

\[
|F(H)|=2n-4-q.
\]

If \(s_H\) is the number of nontriangular faces, then \(s_H\le q\), since each such face contributes at least one unit of excess. Hence the number \(t_H\) of triangular faces satisfies

\[
t_H\ge2n-4-2q. \tag{4}
\]

Using (3), this yields

\[
t_H\ge
\begin{cases}
n+6,&n\text{ even},\\
n+7,&n\text{ odd}.
\end{cases}
\]

These facial triangles are distinct triangles of \(G\).

Now consider

\[
J=G-\{e,f\}.
\]

It has

\[
|E(J)|=3n-7-q.
\]

Its face excess is therefore

\[
3n-6-|E(J)|=q+1.
\]

It has

\[
|F(J)|=2n-5-q
\]

faces, of which at most \(q+1\) are nontriangular. Thus

\[
t_J\ge2n-6-2q, \tag{5}
\]

and hence

\[
t_J\ge
\begin{cases}
n+4,&n\text{ even},\\
n+5,&n\text{ odd}.
\end{cases}
\]

### Lemma 2
Every triangle of \(J\) is facial.

### Proof
Let \(C\) be a triangle of \(J\). Its drawing is a Jordan curve, and no edge of \(G\) crosses \(C\): the only crossing is between \(e\) and \(f\), while neither belongs to \(C\).

If \(J\) had vertices on both sides of \(C\), then \(G-V(C)\) would also have vertices on both sides, with no path between them: a path would have to meet \(C\), since the crossing of \(e\) and \(f\) is not a graph vertex. Thus \(C\) would be a separating clique of \(G\), impossible. Therefore one side of \(C\) is empty, so \(C\) bounds a face. \(\square\)

It follows that \(J\) is \(K_4\)-free. Indeed, in a planar embedding of a proper \(K_4\) subgraph, any additional connected material must lie in one of its four triangular regions, making the boundary triangle of that region nonfacial. Since \(n\ge10\) by (3), \(J\) cannot itself be \(K_4\).

Let \(A\) denote the number of edges of \(J\) incident with two triangular faces. Counting edge incidences with triangular faces gives

\[
3t_J\le |E(J)|+A,
\]

and hence, by (5),

\[
A\ge3t_J-|E(J)|
 \ge 3n-11-5q. \tag{6}
\]

Using (3),

\[
A\ge
\begin{cases}
\dfrac n2+14,&n\text{ even},\\[2mm]
\dfrac{n+33}{2},&n\text{ odd}.
\end{cases}
\]

If two triangular faces \(xyu\) and \(xyv\) share the edge \(xy\), then \(u\ne v\). Since \(J\) is \(K_4\)-free, \(uv\notin E(J)\). Thus these four vertices induce a diamond \(K_4-uv\).

This proves items 2–4.

## 4. Chromatic possibilities for the core

The plane graph \(G-e\) is four-colorable. It cannot be three-colorable: given a three-coloring, either \(a_1\) and \(a_2\) already have different colors, or one of them can be recolored with a fourth, previously unused color. In either case \(G\) would be four-colorable. Therefore

\[
\chi(G-e)=4,
\]

and similarly \(\chi(G-f)=4\).

The core \(J\) is planar, so \(\chi(J)\le4\). It cannot be bipartite. Indeed, if \(J\) has bipartition \(L,R\), color \(L\) with colors \(1,2\) so as to distinguish the endpoints of any of \(e,f\) lying wholly in \(L\), and similarly color \(R\) with colors \(3,4\). Since at most two added edges occur, the graph they induce inside either part is bipartite. All edges between \(L\) and \(R\) automatically join disjoint color palettes. This gives a four-coloring of \(G\).

Hence

\[
\chi(J)\in\{3,4\}. \tag{7}
\]

## 5. The case \(\chi(J)=3\)

Fix a proper three-coloring \(\varphi\) of \(J\).

Both pairs \(a_1,a_2\) and \(b_1,b_2\) must be monochromatic under \(\varphi\). If, for example, \(a_1,a_2\) were differently colored, then either \(b_1,b_2\) were also differently colored, giving a three-coloring of \(G\), or one endpoint of \(f\) could be recolored with a fourth color.

Moreover, the two monochromatic pairs must have distinct colors. If all four crossing endpoints had the same color, recolor one endpoint of \(e\) and one endpoint of \(f\) with a fourth color. They are nonadjacent in \(J\), since they originally belonged to one color class. This again gives a four-coloring of \(G\).

Relabel the three colors so that

\[
\varphi(a_1)=\varphi(a_2)=1,\qquad
\varphi(b_1)=\varphi(b_2)=2.
\]

### Lemma 3
All four edges \(a_i b_j\), \(i,j\in\{1,2\}\), belong to \(G\). Thus the four crossing endpoints induce a \(K_4\).

### Proof
Fix \(a_i\) and \(b_j\). Starting from \(\varphi\), give \(a_i\) a new color \(4\) and \(b_j\) a new color \(5\). This is a proper five-coloring of \(G\), with \(\{a_i\}\) and \(\{b_j\}\) singleton color classes.

If \(a_i b_j\notin E(G)\), recolor \(a_i\) with color \(5\). Since \(b_j\) is the only vertex of color \(5\), the result is a proper four-coloring of \(G\), a contradiction. Thus \(a_i b_j\in E(G)\). \(\square\)

The planarization of this crossed \(K_4\) is the wheel with rim

\[
C=a_1b_1a_2b_2a_1
\]

and center equal to the crossing point. A component of \(G-\{a_1,a_2,b_1,b_2\}\) lying in one of the four regions incident with the crossing could attach to the crossed \(K_4\) only through the two adjacent rim vertices bounding that region. Those two vertices form a clique separator, impossible. Hence all four crossing-adjacent regions are empty. After deleting \(e\) and \(f\), the cycle \(C\) therefore bounds a quadrilateral face of \(J\).

## 6. The density bound for a three-colorable core

Let \(r=q+1\) be the total face excess of \(J\). Let \(s\) be the number of nontriangular faces and let

\[
L=\sum_{\substack{F\in \mathcal F(J)\\|F|\ge4}} |F|
\]

be their total boundary length, with multiplicity. Since \(s\le r\),

\[
L=3s+r\le4r=4q+4. \tag{8}
\]

The central quadrilateral contributes four boundary incidences, one at each crossing endpoint.

Every degree-five vertex not among \(a_1,a_2,b_1,b_2\) must be incident with a nontriangular face. Otherwise its five neighbors occur cyclically around it, and every consecutive pair bounds a triangular face. In a three-coloring the neighbor colors would then have to alternate between the two colors different from the vertex's own color, which is impossible around a cycle of odd length five.

A degree-five crossing endpoint must be incident with a second nontriangular face in addition to the central quadrilateral. For example, suppose \(a_1\) had no other nontriangular incident face. In \(J\), it has degree four. Traversing from one central-face neighbor to the other through its other three face angles, all three angles are triangular, so the two neighbor colors must alternate three times and hence be different. But these two neighbors are \(b_1,b_2\), both of color \(2\), a contradiction.

Thus, beyond the four incidences of the central quadrilateral, every degree-five vertex contributes at least one further nontriangular-face incidence. Consequently,

\[
L\ge4+n_5.
\]

Using (2),

\[
L\ge14+2q+h. \tag{9}
\]

Combining (8) and (9) gives

\[
14+2q+h\le4q+4,
\]

or

\[
2q\ge10+h.
\]

Therefore

\[
q\ge 5+\left\lceil\frac h2\right\rceil.
\]

In particular,

\[
m=3n-5-q\le3n-10.
\]

This proves item 6.

# An extremal refinement

If \(\chi(J)=3\) and \(q=5\), equality must hold throughout the preceding count. Hence

\[
h=0,\qquad n_5=20,
\]

all remaining vertices have degree six, and the six nontriangular faces of \(J\) are quadrilaterals.

The case \(n=20\) is impossible. Indeed, then \(G\) is \(5\)-regular. Equality in the incidence count implies that every ordinary vertex is incident with exactly one quadrilateral, while every crossing endpoint is incident with exactly two, one being the central quadrilateral. A parity argument around each vertex shows that every quadrilateral is bichromatic in the three-coloring.

There are \(24\) triangular faces and six quadrilateral faces. Let \(q_{ij}\) be the number of quadrilaterals alternating colors \(i,j\), and let \(E_{ij}\) be the number of edges joining colors \(i,j\). Then

\[
2E_{ij}=24+4q_{ij},
\qquad
E_{ij}=12+2q_{ij}.
\]

Let \(n_i\) be the size of color class \(i\). The endpoints of \(e\) lie in class \(1\), the endpoints of \(f\) in class \(2\). Their degrees in \(J\) are four, while every other vertex has degree five. Thus, writing \(s_i=\sum_{j\ne i}q_{ij}\),

\[
5n_1-2=24+2s_1,\qquad
5n_2-2=24+2s_2,\qquad
5n_3=24+2s_3.
\]

Since \(0\le s_i\le6\), the congruences modulo five force

\[
s_1=s_2=2,\qquad s_3=3,
\]

and therefore

\[
n_1=n_2=n_3=6.
\]

This gives \(n=18\), contrary to \(n=20\). Thus the extremal possibility \(q=5\) with \(n=20\) does not occur.

# What remains open

The argument does not address the main apparent obstruction: the planar core \(J\) may itself be \(4\)-chromatic. In that case the alternating-neighbor parity used above is unavailable. Criticality only yields the following coloring constraint:

- every four-coloring of \(J\) identifies at least one of the pairs \(a_1,a_2\) and \(b_1,b_2\);
- there is a four-coloring identifying the first pair but not the second, and another identifying the second but not the first;
- after deleting any ordinary edge or vertex of \(J\), a four-coloring separating both pairs exists.

This is a nontrivial four-color precoloring-extension problem on a planar graph with one distinguished face. Resolving that locked-pair configuration, or finding a counterexample to it, appears to be the missing step.

No computational search beyond the one reported in the source paper was performed here, and I have not verified whether the elementary structural lemmas above already occur in the 51-page source.