```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every r>=1, I construct a finite (P4 plus r isolated vertices)-induced-saturated graph on 2r+25 vertices, ruling out that entire candidate exceptional family.",
  "would_publish": false,
  "caveats": "The original existence question remains unresolved; novelty of these positive constructions has not been checked."
}
```

# Partial result: isolated-vertex extensions of \(P_4\) have finite saturators

The main question remains unresolved. However, the family investigated in the previous attempt can be settled in the **positive** direction.

## Theorem

For every integer \(r\geq 1\), the graph
\[
H_r=P_4\dot\cup rK_1
\]
has a finite induced-saturated graph on \(2r+25\) vertices.

Consequently, the same holds for
\[
\overline{H_r}=P_4\vee K_r.
\]

The construction and verification below are self-contained. They do not rely on the previous attempt’s unverified structural assertions or lower bound.

Here \(\dot\cup\) denotes disjoint union and \(\vee\) denotes join. Write
\[
J=K_1\vee P_4
\]
for the **gem**. The first step is an explicit 27-vertex \(J\)-induced-saturated graph.

---

# 1. A local criterion for gem-induced-saturation

## Lemma 1

Suppose a graph \(F\) has the following properties:

1. For every vertex \(v\), the induced graph \(F[N_F(v)]\) is a nonempty disjoint union of copies of \(C_4\).
2. For every nonedge \(xy\), there is a common neighbor \(z\) such that \(x\) and \(y\) lie in different components of \(F[N_F(z)]\).

Then \(F\) is \(J\)-induced-saturated.

### Proof

An induced gem consists of a vertex whose neighborhood contains an induced \(P_4\). A disjoint union of \(4\)-cycles is \(P_4\)-free, so property 1 implies that \(F\) is gem-free.

Let \(xy\) be an edge. In \(F[N_F(x)]\), the vertex \(y\) lies in a \(4\)-cycle, so it has a neighbor \(z\) there. Thus \(x,y\in N_F(z)\). Since \(xy\) is an edge, \(x\) and \(y\) lie in the same \(C_4\)-component of \(F[N_F(z)]\). Deleting \(xy\) turns that \(C_4\) into an induced \(P_4\). Together with \(z\), this is a gem.

Now let \(xy\) be a nonedge. Choose \(z\) as in property 2. Choose a neighbor \(a\) of \(x\) in its \(C_4\)-component of \(F[N_F(z)]\), and a neighbor \(b\) of \(y\) in the other component. Before adding \(xy\), the four vertices \(a,x,y,b\) induce \(2K_2\). After adding \(xy\), they induce the path
\[
a-x-y-b.
\]
The vertex \(z\) is adjacent to all four, giving a gem. \(\square\)

---

# 2. A 27-vertex graph satisfying the criterion

Let
\[
Q=K_{3,3,3}
\]
have parts
\[
A=\{a_0,a_1,a_2\},\qquad
B=\{b_0,b_1,b_2\},\qquad
C=\{c_0,c_1,c_2\}.
\]
All subscripts below are in \(\mathbb Z/3\mathbb Z\).

The vertices of \(F\) are the 27 edges of \(Q\). We start with the line graph of \(Q\), but at each vertex of \(Q\) declare three pairs of incident edges to be nonadjacent.

The pairs are:

- at \(a_i\),
  \[
  \{a_i b_j,\ a_i c_{-i-j}\},
  \qquad j\in\mathbb Z/3\mathbb Z;
  \]
- at \(b_j\),
  \[
  \{a_i b_j,\ b_j c_{1-i-j}\},
  \qquad i\in\mathbb Z/3\mathbb Z;
  \]
- at \(c_k\),
  \[
  \{a_i c_k,\ b_{2-i-k}c_k\},
  \qquad i\in\mathbb Z/3\mathbb Z.
  \]

Thus two distinct vertices of \(F\), viewed as edges of \(Q\), are adjacent precisely when they share an endpoint and are not one of the designated pairs.

For \(v\in V(Q)\), write \(S_v\) for the six edges of \(Q\) incident with \(v\). The three designated pairs partition \(S_v\), and
\[
F[S_v]\cong K_{2,2,2}.
\]

## 2.1. Every neighborhood is \(C_4\dot\cup C_4\)

Consider a triangle
\[
a_i b_j c_k
\]
in \(Q\), and put \(s=i+j+k\pmod 3\). Of its three pairs of incident edges:

- the pair at \(a_i\) is designated exactly when \(s=0\);
- the pair at \(b_j\) is designated exactly when \(s=1\);
- the pair at \(c_k\) is designated exactly when \(s=2\).

Therefore **exactly one** of these three adjacencies is absent in \(F\). In particular, the three edges of a triangle of \(Q\) never form a triangle in \(F\).

Three pairwise incident edges of a simple graph either have a common endpoint or form a triangle. It follows that every triangle in \(F\) is contained in some \(S_v\).

Now take a vertex \(e=uv\) of \(F\). Its neighbors split into:

- the four edges in \(S_u\) outside the designated pair containing \(e\);
- the four edges in \(S_v\) outside the designated pair containing \(e\).

Each group induces \(K_{2,2}=C_4\). There are no edges between the groups: such an edge, together with \(e\), would give a triangle in \(F\) not contained in a single \(S_v\).

Hence
\[
F[N_F(e)]\cong C_4\dot\cup C_4
\qquad\text{for every }e\in V(F).
\]

This proves property 1 of Lemma 1.

## 2.2. Every nonedge has a separating common neighbor

Let \(e,f\) be nonadjacent vertices of \(F\). We find a common neighbor \(g\) such that \(e,f\) belong to different \(C_4\)-components of \(F[N_F(g)]\).

### Case A: \(e,f\) share an endpoint in \(Q\)

They must be one of the designated pairs. Write
\[
e=uv,\qquad f=uw.
\]
The vertices \(u,v,w\) belong to the three different parts of \(Q\), so \(g=vw\) is an edge of \(Q\).

The triangle \(uvw\) has its unique designated pair at \(u\). Thus \(g\) is adjacent in \(F\) to both \(e\) and \(f\). In the neighborhood of \(g=vw\), they lie in the components corresponding to \(v\) and \(w\), respectively.

### Case B: \(e,f\) are disjoint edges of \(Q\) joining the same two parts

For example, write
\[
e=a_i b_j,\qquad f=a_{i'}b_{j'},
\qquad i\ne i',\quad j\ne j'.
\]
Take
\[
g=a_i b_{j'}.
\]
At \(a_i\), the edges \(e,g\) both go to \(B\), so they cannot be a designated pair. Similarly, \(f,g\) cannot be a designated pair at \(b_{j'}\).

Thus \(g\) is a common neighbor, and \(e,f\) lie in the two different neighborhood components of \(g\).

### Case C: \(e,f\) are disjoint edges of \(Q\) joining different pairs of parts

Suppose first that their common part-type is \(A\):
\[
e=a_i b_j,\qquad f=a_{i'}c_k,\qquad i\ne i'.
\]
Consider
\[
g_1=a_i c_k,\qquad g_2=a_{i'}b_j.
\]

The vertex \(g_1\) is adjacent to \(f\), since both corresponding edges go from \(c_k\) to \(A\). It fails to be adjacent to \(e\) only if
\[
i+j+k=0.
\]

Similarly, \(g_2\) is adjacent to \(e\), and fails to be adjacent to \(f\) only if
\[
i'+j+k=0.
\]

These two equalities cannot both hold because \(i\ne i'\). Therefore at least one of \(g_1,g_2\) is a common neighbor. For either choice, \(e\) and \(f\) meet different endpoints of the chosen edge of \(Q\), so they belong to different neighborhood components.

If the common part-type is \(B\) or \(C\), the same argument applies, with the exceptional residue \(0\) replaced by \(1\) or \(2\).

These cases exhaust all nonedges of \(F\), proving property 2 of Lemma 1.

We have therefore established:

## Proposition 2
The explicitly defined 27-vertex graph \(F\) is gem-induced-saturated. \(\square\)

---

# 3. Properties of the complementary base graph

Set
\[
B=\overline F.
\]
Since complementation preserves induced-saturation while complementing the forbidden graph, and \(P_4\) is self-complementary, \(B\) is
\[
(P_4\dot\cup K_1)\text{-induced-saturated}.
\]

We need three further elementary properties.

## 3.1. \(B\) contains an induced \(P_4\)

In \(F\), the four vertices
\[
a_0b_0,\quad a_1b_0,\quad a_1b_1,\quad a_2b_1
\]
induce a \(P_4\), in the displayed order.

Indeed, consecutive edges share an endpoint in \(Q\), and none is a designated pair because all four edges join \(A\) to \(B\). Nonconsecutive edges are disjoint.

Their induced graph in \(B\) is also a \(P_4\).

## 3.2. \(\alpha(B)=3\)

Every neighborhood in \(F\) is triangle-free, so \(F\) contains no \(K_4\). On the other hand, each \(F[S_v]\cong K_{2,2,2}\) contains a triangle. Thus
\[
\alpha(B)=\omega(F)=3.
\]

## 3.3. Every vertex of \(B\) can be an endpoint of the edge in an induced \(K_2\dot\cup 2K_1\)

More precisely, for every \(x\in V(B)\), there are distinct vertices \(w,a,b\) such that
\[
E\bigl(B[\{x,w,a,b\}]\bigr)=\{xw\}. \tag{*}
\]

To see this, regard \(x\) as an edge of \(Q\), and choose one of its endpoints \(v\). In
\[
F[S_v]\cong K_{2,2,2},
\]
let \(w\) be the other vertex in the part containing \(x\). Choose \(a,b\) from the other two parts, one from each.

Among these four vertices, \(xw\) is the only nonedge in \(F\). Hence it is the only edge in \(B\), proving \((*)\).

---

# 4. Padding by disjoint edges

For \(r\geq1\), define
\[
G_r=B\dot\cup (r-1)K_2.
\]
Then
\[
|V(G_r)|=27+2(r-1)=2r+25.
\]

We verify that \(G_r\) is \(H_r=P_4\dot\cup rK_1\)-induced-saturated.

## 4.1. \(G_r\) is \(H_r\)-free

Any induced \(P_4\) in \(G_r\) lies entirely in \(B\), since a \(P_4\) is connected and the other components have only two vertices.

Because \(B\) is \(P_4\dot\cup K_1\)-free, no vertex of \(B\) is anticomplete to such a \(P_4\). Consequently, all isolated vertices of a putative induced \(H_r\) would have to come from the \(r-1\) additional copies of \(K_2\).

An independent set can use at most one vertex from each of those copies, giving at most \(r-1\) isolated vertices. Thus \(G_r\) is \(H_r\)-free.

## 4.2. Toggling a pair inside \(B\)

By the induced-saturation of \(B\), the toggle creates an induced
\[
P_4\dot\cup K_1
\]
inside \(B\). Choose one vertex from each of the \(r-1\) additional copies of \(K_2\). These supply \(r-1\) more isolated vertices, giving \(H_r\).

## 4.3. Deleting an edge of an additional \(K_2\)

This case occurs when \(r\geq2\).

Use a fixed induced \(P_4\) in \(B\). The two endpoints of the deleted edge are now isolated from each other and from \(B\). Together with one vertex from each of the other \(r-2\) copies of \(K_2\), they give exactly \(r\) independent vertices anticomplete to the \(P_4\).

## 4.4. Adding an edge between two additional copies of \(K_2\)

This case occurs when \(r\geq3\).

The two copies of \(K_2\), together with the added edge, induce a \(P_4\). Choose an independent triple in \(B\), and choose one vertex from each of the other \(r-3\) copies of \(K_2\).

These
\[
3+(r-3)=r
\]
vertices are independent and anticomplete to the new \(P_4\).

## 4.5. Adding an edge between \(B\) and an additional \(K_2\)

Let the added edge be \(xy\), where \(x\in V(B)\), and let \(yz\) be the additional copy of \(K_2\).

By property \((*)\), choose \(w,a,b\in V(B)\) such that the only edge of
\[
B[\{x,w,a,b\}]
\]
is \(xw\).

After adding \(xy\), the vertices
\[
w-x-y-z
\]
induce a \(P_4\). The vertices \(a,b\), together with one vertex from each of the other \(r-2\) copies of \(K_2\), give
\[
2+(r-2)=r
\]
independent vertices anticomplete to this path.

These four toggle cases exhaust every pair of vertices of \(G_r\). Hence \(G_r\) is \(H_r\)-induced-saturated.

Finally, complementation gives a finite induced-saturated graph of the same order for \(P_4\vee K_r\). This proves the theorem. \(\square\)

The construction also has
\[
\alpha(G_r)=3+(r-1)=r+2=\alpha(H_r).
\]

---

# 5. What remains open

This settles the natural family
\[
P_4\dot\cup rK_1,\qquad r\geq1,
\]
which the previous attempt left undecided: **none of these graphs is an additional finite obstruction**.

It does not settle Problem 21. No infinite family lacking finite induced-saturated graphs is obtained, and no new individual obstruction beyond the given \(P_4\) is established.

The positive construction above is proved directly, but I have not verified whether it, or an equivalent construction, already appears in the literature.