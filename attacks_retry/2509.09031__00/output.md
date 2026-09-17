```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A finite counterexample is obtained from a contraction- and subdivision-closed class whose branch vertices are pairwise joined by internally degree-two paths.",
  "would_publish": true,
  "caveats": "Uses the standard coarsely onto definition of quasi-isometry; the class is not required to be closed under edge deletion."
}
```

# A finite counterexample

All graphs below are finite, connected, and simple. Edge contraction includes the usual suppression of loops and parallel edges.

An \((L,C)\)-quasi-isometry \(f:G\to H\) satisfies
\[
L^{-1}d_G(x,x')-C\le d_H(f(x),f(x'))\le Ld_G(x,x')+C
\]
and every vertex of \(H\) is within distance \(C\) of \(f(V(G))\).

We construct a fixed class \(\mathcal C\), closed under edge contraction and subdivision, and graphs \(G_g,H_g^+\) such that:

* \(H_g^+\in\mathcal C\);
* there is an onto \((2,1)\)-quasi-isometry \(G_g\to H_g^+\);
* every \((1,A)\)-quasi-isometry from \(G_g\) to any member of \(\mathcal C\) satisfies
  \[
  A+1>\frac{g}{10000}.
  \]

Thus the proposed uniform additive constant does not exist.

The red/blue turn-cost mechanism from the supplied attempt is useful, but its arbitrary-map/arbitrary-target gap must be closed. We do this by adding long complete-graph corridors and proving a rigidity lemma. The infinite-graph argument is not used.

---

## 1. The contraction- and subdivision-closed class

For a graph \(J\), put
\[
B(J)=\{v\in V(J):\deg_J(v)\ge 3\}.
\]
A **thread** between distinct vertices \(u,v\in B(J)\) is a \(u\)-\(v\) path all of whose internal vertices have degree two in \(J\).

Define
\[
\mathcal C=
\left\{
J:\text{every two distinct vertices of }B(J)
\text{ are joined by a thread}
\right\}.
\tag{1.1}
\]
In particular, every subdivision of a complete graph belongs to \(\mathcal C\).

### Lemma 1.1
The class \(\mathcal C\) is closed under edge subdivision and edge contraction.

#### Proof
Subdivision is immediate: the old branch vertices are unchanged, and threads remain threads.

For contraction, let \(J'\) be obtained from \(J\in\mathcal C\) by contracting \(xy\). Every branch vertex of \(J'\) is the image of a branch vertex of \(J\). Indeed, degrees of uncontracted vertices cannot increase, and contracting two vertices of degree at most two produces a vertex of degree at most two.

Take distinct \(u',v'\in B(J')\), and choose branch vertices \(u,v\in B(J)\) mapping to them. Let \(P\) be a thread between \(u\) and \(v\) in \(J\).

The image of \(P\) contains a \(u'\)-\(v'\) path whose internal vertices have degree at most two in \(J'\). To see the only potentially problematic point, suppose the contracted vertex occurs internally on this image. If one endpoint of \(xy\) is internal on \(P\), its two neighbours already lie on \(P\). Hence the other endpoint of \(xy\) also lies on \(P\); unless the contracted vertex is an endpoint of the image, both contracted vertices have degree two. Their contraction therefore has degree at most two.

After choosing a simple path in the image, its internal vertices have degree exactly two. Thus \(u',v'\) are joined by a thread. ∎

---

## 2. Metric preliminaries

We use the geometric realization of a graph, giving every edge length one. Distances between original vertices are unchanged.

### Lemma 2.1 — Continuous coarse inverses
If there is a \((1,A)\)-quasi-isometry between graphs \(G\) and \(K\), then their geometric realizations \(X,Y\) admit continuous maps
\[
F:X\to Y,\qquad Q:Y\to X
\]
such that, with
\[
D=10(A+1),
\tag{2.1}
\]
we have
\[
\begin{aligned}
|d_Y(Fx,Fx')-d_X(x,x')|&\le D,\\
|d_X(Qy,Qy')-d_Y(y,y')|&\le D,\\
d_Y(FQy,y)&\le D.
\end{aligned}
\tag{2.2}
\]

#### Proof
Extend the given vertex map over each edge along a geodesic. The resulting continuous map \(F\) has distortion at most \(3A+4\): each point can be compared with an endpoint of its edge, and each image edge has length at most \(A+1\).

For every vertex \(w\) of \(K\), choose a vertex \(q(w)\) of \(G\) with
\[
d_K(f(q(w)),w)\le A.
\]
The vertex map \(q\) has distortion at most \(3A\). Extend it over edges along geodesics. The resulting \(Q\) has distortion at most \(9A+4\).

Finally, comparing \(y\) with an endpoint \(w\) of its edge gives
\[
d_Y(FQy,y)\le 7A+6.
\]
All three bounds are at most \(10(A+1)\). ∎

We also use the following elementary observation.

### Lemma 2.2 — Detecting a branch vertex
Let \(Z\) be a metric graph. Suppose \(z_1,z_2,z_3\) lie within distance \(r\) of \(z\), and
\[
d_Z(z_i,z_j)>r\qquad(i\ne j).
\]
Then \(B(Z)\) meets the closed radius-\(r\) ball about \(z\).

#### Proof
Otherwise, the union of shortest \(z\)-\(z_i\) paths has no branch vertex. It lies in a path, or forms a cycle of length at most \(2r\). In the path case, two of the three points lie on the same side of \(z\), at distance at most \(r\) from each other. In the cycle case, the diameter is at most \(r\). Both contradict the hypothesis. ∎

---

## 3. Rigidity of a complete system of long corridors

Here is the step that rules out changing either the quasi-isometry or the target.

### Lemma 3.1 — Long-corridor rigidity
Let \(n\ge4\), \(D\ge1\), and \(S\ge1000D\).

Construct a metric graph \(X\) as follows:

* replace each vertex \(v\) of \(K_n\) by a tree \(T_v\) of diameter at most one;
* choose \(r_v\in T_v\);
* for each pair \(u,v\), join a point of \(T_u\) to a point of \(T_v\) by one corridor \(I_{uv}\), of length
  \[
  L_{uv}\ge S;
  \]
* these corridors have disjoint interiors, and there are no other edges.

Let \(Y\) be the geometric realization of a graph in \(\mathcal C\). Suppose continuous maps \(F:X\to Y\), \(Q:Y\to X\) satisfy (2.2).

Then:

1. \(Y\) has exactly \(n\) branch vertices, labelled \(h_v\);
2. for each pair \(u,v\), there is exactly one thread between \(h_u,h_v\);
3. writing \(\lambda_{uv}\) for its length, the weighted complete-graph metric \(d_\lambda\) satisfies
   \[
   |d_\lambda(u,v)-d_X(r_u,r_v)|\le30D;
   \tag{3.1}
   \]
4. every such thread satisfies
   \[
   \lambda_{uv}\ge \frac{L_{uv}}2-D.
   \tag{3.2}
   \]

#### Proof

### Step 1: Find a branch vertex near each \(F(r_v)\)

Choose three different corridors incident with \(T_v\), and on each choose a point at corridor-distance \(10D\) from \(T_v\). Each point is within \(10D+1\) of \(r_v\), and each pair is at distance at least \(20D\).

Their images under \(F\) lie within \(12D\) of \(F(r_v)\), and have pairwise distances at least \(19D\). Lemma 2.2 therefore gives
\[
h_v\in B(Y),\qquad d_Y(h_v,F(r_v))\le12D.
\tag{3.3}
\]

For distinct \(u,v\), we have \(d_X(r_u,r_v)\ge S\), so
\[
d_Y(h_u,h_v)\ge S-25D.
\tag{3.4}
\]
In particular, these \(n\) branch vertices are distinct.

### Step 2: Every branch vertex of \(Y\) belongs to one of these clusters

Let \(h\in B(Y)\). By (3.4), at most one of the chosen \(h_v\) lies within distance \(S/3\) of \(h\). Since \(n\ge4\), choose three others, each at distance at least \(S/3\).

The defining property of \(\mathcal C\) supplies threads from \(h\) to these three vertices. The threads have disjoint interiors, and each has length at least \(S/3\). Points at thread-distance \(10D\) from \(h\) therefore have distance \(10D\) from \(h\) and pairwise distance \(20D\).

Their images under \(Q\), together with Lemma 2.2, show that \(Q(h)\) lies within \(11D\) of a branch vertex of \(X\). All branch vertices of \(X\) lie in the trees \(T_v\). Consequently,
\[
d_X(Q(h),r_v)\le12D
\tag{3.5}
\]
for some \(v\). Using (2.2),
\[
d_Y(h,F(r_v))\le14D.
\tag{3.6}
\]
This \(v\) is unique because distinct \(F(r_v)\) are at distance at least \(S-D>28D\).

Call it the cluster of \(h\). The initially chosen \(h_v\) belongs to cluster \(v\).

### Step 3: A thread between two clusters must follow the corresponding corridor

Consider any thread \(P\) between branch vertices \(h,h'\) in distinct clusters \(v,w\). Its length \(\lambda\) satisfies
\[
\lambda\ge d_Y(h,h')\ge S-29D>100D.
\]
Remove the first and last \(50D\) of \(P\), leaving a closed interval \(P^0\).

Every point \(y\in P^0\) has distance at least \(50D\) from \(B(Y)\), since the interior of a thread can be left only through its endpoints.

If \(d_X(Qy,r_z)\le20D\), then (2.2) and (3.3) give
\[
d_Y(y,h_z)
 \le D+(20D+D)+12D
 =34D,
\]
a contradiction. Thus
\[
Q(P^0)\cap\bigcup_z\overline B_X(r_z,20D)=\varnothing.
\tag{3.7}
\]

The components of the complement in (3.7) are precisely trimmed interiors of the individual corridors of \(X\). Since \(Q\) is continuous, \(Q(P^0)\) lies in one such component.

Let \(y_0,y_1\) be the two endpoints of \(P^0\). By (3.5),
\[
d_X(Qy_0,r_v)\le 50D+D+12D=63D,
\]
and similarly \(d_X(Qy_1,r_w)\le63D\). Since \(63D<S\), the corridor containing \(Q(P^0)\) must be incident with both \(v\) and \(w\). It is therefore \(I_{vw}\).

Moreover, measured from the respective ends of \(I_{vw}\), the points \(Qy_0,Qy_1\) lie within \(63D\). By continuity, \(Q(P^0)\) covers the whole central interval
\[
[63D,L_{vw}-63D]
\tag{3.8}
\]
of that corridor.

### Step 4: No two threads can join the same two clusters

If two distinct threads joined clusters \(v,w\), (3.8) would give interior points \(y,y'\), one on each trimmed thread, mapping under \(Q\) to the midpoint of \(I_{vw}\).

The distortion bound for \(Q\) would imply
\[
d_Y(y,y')\le D.
\]
But distinct threads have disjoint interiors, and leaving the first trimmed thread requires travelling at least \(50D\). This is impossible.

Every cluster is nonempty. If some cluster contained two branch vertices, threads from both of them to a branch vertex in any other cluster would contradict the preceding paragraph. Thus every cluster contains exactly one branch vertex.

The defining property of \(\mathcal C\) now gives exactly one thread between each pair \(h_u,h_v\).

### Step 5: The metric and thread-length conclusions

Any shortest path between branch vertices traverses a sequence of the threads just identified. Other components—pendant paths or cycles attached at a single branch vertex—cannot shorten such a path. Therefore their metric is exactly the weighted \(K_n\) metric with edge lengths \(\lambda_{uv}\).

Equation (3.3) and the distortion of \(F\) give
\[
|d_Y(h_u,h_v)-d_X(r_u,r_v)|\le25D,
\]
which implies (3.1).

Finally, (3.8) includes the quarter and three-quarter points of \(I_{uv}\). Their distance in \(X\) is \(L_{uv}/2\): the direct interval has that length, and a route through the two ends cannot be shorter. Choosing preimages on the thread and using the distortion of \(Q\) yields
\[
\lambda_{uv}\ge L_{uv}/2-D.
\]
This proves (3.2). ∎

---

## 4. High-girth graphs with two colours

For every integer \(g\ge5\), we need a finite connected simple graph \(H_g\) of girth at least \(g\), with
\[
E(H_g)=E_R\sqcup E_B,
\]
such that every vertex has two incident red edges and two incident blue edges.

Here is a self-contained construction.

Let \(W_g\) be the finite set of all nonempty freely reduced words of length less than \(g\) in
\[
a,a^{-1},b,b^{-1}.
\]
For a word \(w\) of length \(k\), take the set \(\{0,\ldots,k\}\), and prescribe partial permutations \(a_w,b_w\) so that following the letters of \(w\) sends
\[
0\to1\to\cdots\to k.
\]
For an inverse letter, prescribe the corresponding reversed permutation arrow. These partial permutations are well-defined and injective: a conflict at an intermediate index would require adjacent inverse letters. Complete each partial permutation to a permutation, for example by matching the remaining domain and range elements in increasing order.

In the product of these finite symmetric groups, let \(a,b\) be the tuples of the constructed permutations, and let \(Q_g\) be the subgroup they generate. No nonempty freely reduced word of length less than \(g\) is trivial in \(Q_g\), because its own coordinate sends \(0\) to \(k\).

The undirected Cayley graph of \(Q_g\) with generators \(a^{\pm1},b^{\pm1}\) is therefore simple, connected, 4-regular, and has girth at least \(g\). Colour \(a\)-edges red and \(b\)-edges blue.

Each monochromatic subgraph is a union of cycles, all of length at least \(g\).

---

## 5. The graphs and their uniform quasi-isometries

Fix an integer \(g\ge10000\), and write
\[
H=H_g,\qquad n=|V(H)|,\qquad S=g,\qquad M=100g^2.
\tag{5.1}
\]

Construct \(H_g^+\) from \(K_n\), on vertex set \(V(H)\), by replacing:

* every edge of \(H\) by a path of length \(S\);
* every edge not in \(H\) by a path of length \(M\).

Thus \(H_g^+\) is a subdivision of \(K_n\), so
\[
H_g^+\in\mathcal C.
\]

Construct \(G_g\) by splitting each original vertex \(v\) into two vertices \(v_R,v_B\), joined by a unit-length **switch edge**. Attach:

* the red \(H\)-corridors to the corresponding \(R\)-vertices;
* the blue \(H\)-corridors to the corresponding \(B\)-vertices;
* every length-\(M\) corridor to the corresponding \(R\)-vertices at both ends.

Define
\[
p:G_g\to H_g^+
\]
by collapsing each switch edge and mapping all corridor vertices to their corresponding vertices.

This map is onto. Every \(G_g\)-path projects to an \(H_g^+\)-walk of no greater length, so
\[
d_{H_g^+}(p(x),p(y))\le d_{G_g}(x,y).
\]
Conversely, a shortest \(H_g^+\)-path of length \(k\) lifts using at most \(k+1\) switches. Hence
\[
d_{G_g}(x,y)\le2d_{H_g^+}(p(x),p(y))+1.
\]
Therefore \(p\) is an onto \((2,1)\)-quasi-isometry.

---

## 6. No uniformly additive approximation exists

Suppose there is a \((1,A)\)-quasi-isometry
\[
G_g\to K,\qquad K\in\mathcal C,
\]
where
\[
A+1\le \frac{g}{10000}.
\tag{6.1}
\]
Put
\[
D=10(A+1),\qquad E=30D,\qquad
s=\left\lfloor\frac g{10}\right\rfloor.
\tag{6.2}
\]
Then \(S=g\ge1000D\), so Lemmas 2.1 and 3.1 apply to \(G_g\), with the switch edges as the trees \(T_v\) and \(r_v=v_R\).

We obtain positive lengths \(\lambda_{uv}\) on the edges of \(K_n\) such that
\[
|d_\lambda(u,v)-d_{G_g}(u_R,v_R)|\le E
\tag{6.3}
\]
for every \(u,v\), and
\[
\lambda_{uv}\ge M/2-D
\qquad\text{if }uv\notin E(H).
\tag{6.4}
\]

The following inequalities follow from \(g\ge10000\) and \(D\le g/1000\):
\[
\begin{gathered}
s-3>2E,\qquad Ss>2+2E,\qquad S>s+1,\\
M/2-D>Ss+2+E,\qquad 2s<g/2,\qquad g-s\ge2s.
\tag{6.5}
\]

We now show that (6.3)–(6.4) are impossible.

### 6.1. Lower bounds on short \(H\)-paths

If \(P\) is an \(H\)-path of length \(t<g/2\), then \(P\) is geodesic in \(H\). Let its endpoints be \(u,v\).

Any \(G_g\)-path from \(u_R\) to \(v_R\) that uses a long corridor has length at least \(M>St\). A path using only \(H\)-corridors has length at least \(St\). Thus
\[
d_{G_g}(u_R,v_R)\ge St.
\]
Consequently,
\[
\lambda(P)\ge d_\lambda(u,v)\ge St-E.
\tag{6.6}
\]

### 6.2. Upper bounds on monochromatic paths

Let \(P\) be a monochromatic \(H\)-path of length \(s\), with endpoints \(u,v\).

If \(P\) is red, it lifts from \(u_R\) to \(v_R\) with length \(Ss\). If it is blue, two endpoint switches suffice. Hence
\[
d_{G_g}(u_R,v_R)\le Ss+2,
\]
and so
\[
d_\lambda(u,v)\le Ss+2+E.
\tag{6.7}
\]

By (6.4)–(6.5), a \(\lambda\)-shortest path \(Q\) between \(u,v\) cannot use an edge outside \(H\). Choose \(Q\) simple.

If \(Q\ne P\), their union contains a cycle, giving
\[
|Q|+s\ge g.
\]
In particular, \(Q\) contains a \(2s\)-edge subpath. Applying (6.6) to that subpath gives
\[
\lambda(Q)\ge2Ss-E>Ss+2+E,
\]
contrary to (6.7). Thus \(P\) itself is shortest, and
\[
\lambda(P)\le Ss+2+E.
\tag{6.8}
\]

### 6.3. Average over the monochromatic cycles

Apply (6.8) to every cyclic window of \(s\) edges on every monochromatic cycle. Each edge of a cycle occurs in exactly \(s\) windows. Summing over both colours gives
\[
\sum_{e\in E(H)}\lambda_e
\le
|E(H)|\left(S+\frac{2+E}{s}\right).
\tag{6.9}
\]

Now choose a uniformly random directed edge of \(H\), and continue for \(s\) edges by alternating colours, choosing uniformly between the two available edges of the required colour.

At every position the directed edge is uniformly distributed: every directed edge has exactly two possible predecessor directed edges of the opposite colour, each transitioning to it with probability \(1/2\).

Thus (6.9) implies that the expected \(\lambda\)-length of this walk is at most
\[
Ss+2+E.
\]
There is therefore an alternating walk
\[
P=v_0v_1\cdots v_s
\]
with
\[
\lambda(P)\le Ss+2+E.
\tag{6.10}
\]
It is nonbacktracking. Since \(s<g\), it is a path; since \(2s<g\), it is the unique \(H\)-geodesic between its endpoints.

### 6.4. Alternating paths require accumulated switch costs

Following \(P\) in \(G_g\), from \((v_0)_R\) to \((v_s)_R\), costs at most
\[
Ss+s+1.
\]
A shortest path cannot use a long corridor, since \(M\) exceeds this quantity.

Nor can it use at least \(s+1\) short corridors, since
\[
S(s+1)>Ss+s+1.
\]
It must therefore use exactly \(s\) short corridors and project to the unique \(H\)-geodesic \(P\).

Because \(P\) alternates colours, a switch is necessary between every two successive corridors. Consequently,
\[
d_{G_g}((v_0)_R,(v_s)_R)\ge Ss+s-1.
\tag{6.11}
\]

Combining (6.3), (6.10), and (6.11),
\[
Ss+s-1-E
\le d_\lambda(v_0,v_s)
\le \lambda(P)
\le Ss+2+E.
\]
Therefore
\[
s-3\le2E,
\]
contradicting (6.5).

This proves that (6.1) is impossible.

---

## 7. Conclusion and scope

For the fixed class \(\mathcal C\) defined in (1.1), every \(g\ge10000\) gives an onto \((2,1)\)-quasi-isometry
\[
G_g\to H_g^+\in\mathcal C,
\]
but every \((1,A)\)-quasi-isometry from \(G_g\) to any member of \(\mathcal C\) satisfies
\[
A+1>\frac g{10000}.
\]

Hence the conjecture, with exactly the closure assumptions in the question, is **false for finite graphs**.

The crucial addition to the supplied attempt is Lemma 3.1: it turns an arbitrary additive quasi-isometry to an arbitrary member of \(\mathcal C\) into edge lengths on the prescribed complete-graph skeleton, with only a constant-factor increase in additive error. The long corridors enforce this rigidity; the red/blue averaging then supplies the contradiction.

No infinite-graph convention or external conjecture is needed. A version imposing the additional requirement of closure under edge deletion is not addressed by this counterexample.