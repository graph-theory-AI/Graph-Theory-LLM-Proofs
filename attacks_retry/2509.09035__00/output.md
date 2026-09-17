```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The uniform conjecture holds for every finite tree with at most three leaves, including every subdivision of the claw, without any local-finiteness assumption on the ambient graph.",
  "would_publish": false,
  "caveats": "The general tree and planar cases are not resolved; novelty of these special cases has not been checked."
}
```

# A uniform result for paths and subdivided claws

I can strengthen the claw result in the supplied attempt: the quasi-isometry constants can be made uniform, local finiteness is unnecessary, and bounded graphs are handled uniformly as well. This also settles every subdivision of the claw.

The geodesic-tube observation from the previous attempt is retained and verified below. The ends argument is replaced by a two-ball contraction argument and a compactness argument.

## 1. Statement and conventions

All graphs have unit-length edges, and distances are vertex distances. I work with connected graphs. For the connected patterns considered here, disconnected ambient graphs can be treated componentwise.

A map \(f:X\to Y\) is a \((1,C)\)-quasi-isometry if
\[
\left|d_Y(f(x),f(y))-d_X(x,y)\right|\le C
\]
for all \(x,y\in V(X)\), and every vertex of \(Y\) is within distance \(C\) of \(f(V(X))\).

For definiteness, a \(c\)-fat \(H\)-model consists of connected branch sets \(B_v\), \(v\in V(H)\), and connecting paths \(P_e\), \(e\in E(H)\), such that:

* distinct branch sets are at distance at least \(c\);
* each \(P_{uv}\) meets the branch sets only at its endpoints, one in \(B_u\) and one in \(B_v\);
* distinct connecting paths, including their endpoints, are at distance at least \(c\);
* \(P_e\) is at distance at least \(c\) from every branch set not incident with \(e\).

This is a relatively strong separation convention. All obstruction models constructed below satisfy it, so the conclusions also apply to versions of fat minors that relax separation between incident edge-paths.

### Theorem A: uniform claw theorem

Let \(c>0\), and put
\[
C(c)=200(\lceil c\rceil+1)+1.
\]
Every connected graph with no \(c\)-fat \(K_{1,3}\)-minor admits a \((1,C(c))\)-quasi-isometry to a connected graph of maximum degree at most two.

More specifically:

* if the ambient graph has bounded diameter, the target can be a point, a finite path, or a finite cycle;
* if it has unbounded diameter, the target can be a ray or a double ray.

### Corollary B: trees with at most three leaves

For every finite tree \(H\) with at most three leaves and every \(c>0\), there is \(C=C(H,c)\) such that every connected graph with no \(c\)-fat \(H\)-minor admits a \((1,C)\)-quasi-isometry to an \(H\)-minor-free graph.

Thus these cases satisfy even the uniform, additive-error version of the conjecture.

The rest of the writeup proves these statements.

---

## 2. Three elementary lemmas

### Lemma 2.1: fat models lift through contractions

Let \(Q\) be a contraction quotient of \(G\): its vertices are pairwise disjoint connected vertex sets partitioning \(V(G)\), and two quotient vertices are adjacent whenever an edge of \(G\) joins the corresponding sets. If \(Q\) contains a \(c\)-fat \(H\)-model, then so does \(G\).

#### Proof

Let \(q:G\to Q\) be the quotient map. It is nonexpanding:
\[
d_Q(q(x),q(y))\le d_G(x,y).
\]

Lift a branch set to its full preimage; this is connected. Lift a connecting path through the connected fibers of its vertices, and trim it so that it meets its incident branch sets only at its endpoints.

Each lifted object has image contained in the corresponding object of the quotient model. Consequently every required distance lower bound in \(Q\) remains a distance lower bound in \(G\).

If finite branch sets are required, retain finite connected subgraphs joining the finitely many attachment points. Shrinking branch sets does not impair the separation conditions. ∎

### Lemma 2.2: geodesic-tube lemma

Set
\[
s=\lceil c\rceil+1,\qquad T=10s.
\]
Suppose \(P\) is a geodesic path in \(G\), and \(x\in V(G)\) has a nearest point \(p\in P\) such that

1. \(d(x,P)\ge T\);
2. \(P\) extends at least \(T\) in each direction from \(p\).

Then \(G\) contains a \(c\)-fat claw.

#### Proof

Let \(Q\) be a geodesic from \(p\) to \(x\). If \(z\in Q\) is at distance \(t\) from \(p\), then
\[
d(z,P)=t. \tag{2.1}
\]
Indeed, a shorter route from \(z\) to \(P\), followed by the \(x\)-\(z\) subpath of \(Q\), would contradict the choice of \(p\).

Choose \(a,b\in P\) at distance \(T\) from \(p\), on opposite sides, and \(q\in Q\) at distance \(T\) from \(p\). Take as the central branch set the first \(3s\) units of each of the three arms from \(p\). The three leaf branch sets are
\[
\{a\},\quad \{b\},\quad \{q\},
\]
and the remaining arm segments are the connecting paths.

Here are the separation checks.

* The left and right connecting paths are at distance at least \(6s\), by geodesicity of \(P\).
* The connecting path in \(Q\) is at distance at least \(3s\) from \(P\), by (2.1).
* Every leaf is at distance at least \(7s\) from the central branch set along its own arm.
* For \(z\in Q\) at distance \(t\) from \(p\),
  \[
  d(a,z)\ge T-t,\qquad d(a,z)\ge t.
  \]
  Hence
  \[
  d(a,z)\ge \max\{T-t,t\}\ge T/2=5s,
  \]
  and the same holds for \(b\).
* Finally, \(q\) is at distance \(T\) from all of \(P\).

These inequalities cover all distinct branch-set pairs, all distinct connecting-path pairs, and all nonincident branch-set/path pairs. Thus the model is \(c\)-fat. ∎

A useful consequence is the following.

### Corollary 2.3: a long isometric cycle is dominating

If \(G\) has no \(c\)-fat claw and contains an isometric cycle \(Z\) of length at least \(4T\), then
\[
V(G)\subseteq N_T(Z).
\]

#### Proof

Suppose \(d(x,Z)\ge T\), and let \(p\) be nearest to \(x\) on \(Z\). The arc of \(Z\) extending distance \(T\) in each direction from \(p\) is a geodesic: its length is \(2T\), at most half the length of \(Z\). Lemma 2.2 gives a fat claw. ∎

### Lemma 2.4: two shortest bridges give an isometric cycle

Let \(a,b\) be nonadjacent vertices of a connected graph \(Y\). Suppose at least two components of \(Y-\{a,b\}\) have neighbors in both \(a\) and \(b\).

For such a component \(D\), let \(\ell(D)\) be the length of a shortest \(a\)-\(b\) path with interior in \(D\). Choose two distinct components \(D_0,D_1\) with the two smallest values of \(\ell(D)\), and corresponding shortest paths \(P_0,P_1\). Then
\[
Z=P_0\cup P_1
\]
is an isometric cycle in \(Y\).

#### Proof

Write \(\ell_i=|E(P_i)|\), with \(\ell_0\le \ell_1\). We construct a nonexpanding retraction \(Y\to Z\).

On \(Y[D_i\cup\{a,b\}]\), use distance from \(a\), clipped at \(\ell_i\), as a coordinate on \(P_i\). Since \(P_i\) is a shortest \(a\)-\(b\) path in this subgraph, this map fixes \(P_i\), maps \(a,b\) to the corresponding endpoints, and changes by at most one across an edge.

For every other component having neighbors in both endpoints, use the same construction but clip at \(\ell_0\) and map along \(P_0\). This is consistent at \(b\), because that component's intrinsic \(a\)-\(b\) distance is at least \(\ell_0\). A component having neighbors in only one endpoint is mapped constantly to that endpoint.

The resulting map fixes \(Z\) and maps every edge to an edge or a vertex of \(Z\). It is therefore nonexpanding. Since \(Z\) is also a subgraph of \(Y\), its intrinsic and ambient distances agree. ∎

---

## 3. Uniform classification in bounded diameter

### Proposition 3.1

Every connected bounded-diameter graph \(G\) with no \(c\)-fat claw has an onto map \(f\) to a point, a finite path, or a finite cycle satisfying
\[
\left|d(f(x),f(y))-d_G(x,y)\right|\le 20T. \tag{3.1}
\]

#### Proof

Let \(D=\operatorname{diam}(G)\). Since distances are integers, \(D\) is attained.

If \(D\le20T\), map \(G\) to a point. Hence assume \(D>20T\). Choose a diametral geodesic \(P\) with endpoints \(a,b\), and put
\[
R=3T,\qquad A=B_G(a,R),\qquad B=B_G(b,R).
\]
The balls \(A,B\) are disjoint, connected, and have intrinsic diameter at most \(2R\).

Define
\[
U=\{x:d(x,P)>T\}.
\]

We first locate all edges between \(U\) and its complement. Suppose \(xy\) is such an edge, with \(x\in U\). Then
\[
d(x,P)=T+1.
\]
By Lemma 2.2, a nearest point of \(x\) on \(P\) lies at distance less than \(T\) from \(a\) or \(b\). Consequently
\[
d(x,\{a,b\})\le 2T,\qquad d(y,\{a,b\})\le2T+1.
\]
Thus both ends of every such edge lie in \(A\cup B\).

It follows that every component of
\[
G-(A\cup B)
\]
is contained either in \(U\) or in \(N_T(P)\). The middle subpath of \(P\) belongs to a component \(D_0\subseteq N_T(P)\) having neighbors in both \(A\) and \(B\).

There are two cases.

### Case 1: no component contained in \(U\) has neighbors in both balls

Let \(x\in U\setminus(A\cup B)\), and let \(D_x\) be its component in \(G-(A\cup B)\). By connectedness, \(D_x\) has a neighbor in at least one ball. Suppose it has neighbors in \(A\) but not \(B\).

Every \(x\)-\(b\) path meets \(A\), so
\[
d(x,b)\ge d(x,A)+d(A,b)\ge d(x,A)+D-R.
\]
Since \(d(x,b)\le D\), this gives \(d(x,A)\le R\), and hence
\[
d(x,P)\le d(x,A)+R\le2R.
\]
The other case is symmetric. Vertices in \(A\cup B\) are within \(R\) of \(P\), and the remaining vertices are within \(T\) of \(P\). Therefore
\[
V(G)\subseteq N_{2R}(P).
\]

Nearest-point projection to the isometric path \(P\), fixing \(P\), is onto and has additive distortion at most
\[
4R=12T.
\]

### Case 2: a component contained in \(U\) has neighbors in both balls

Contract \(A\) and \(B\) to vertices \(a^\ast,b^\ast\), obtaining \(Y\). Let \(q:G\to Y\) be the quotient map.

A shortest path in \(Y\) visits each contracted vertex at most once. Traversing either fiber costs at most \(2R\) in \(G\). Hence
\[
d_Y(q(x),q(y))
\le d_G(x,y)
\le d_Y(q(x),q(y))+4R. \tag{3.2}
\]

By Lemma 2.1, \(Y\) has no \(c\)-fat claw. Moreover,
\[
d_Y(a^\ast,b^\ast)=d_G(A,B)\ge D-2R.
\]
There are at least two components of \(Y-\{a^\ast,b^\ast\}\) adjacent to both endpoints: the component coming from the middle of \(P\), and the component contained in \(U\).

Lemma 2.4 therefore gives an isometric cycle \(Z\) in \(Y\), with
\[
|E(Z)|\ge 2(D-2R)>28T.
\]
By Corollary 2.3, \(Y\subseteq N_T(Z)\). Nearest-point projection \(Y\to Z\), fixing \(Z\), is onto and has additive distortion at most \(2T\). Composing with \(q\), and using (3.2), gives additive distortion at most
\[
4R+2T=14T.
\]

Both cases satisfy (3.1). ∎

This includes bounded-diameter graphs with infinitely many vertices; no finiteness or local-finiteness hypothesis was used.

---

## 4. Removing boundedness and local finiteness

We now prove Theorem A for unbounded graphs.

Let
\[
E=20T.
\]
Fix \(o\in V(G)\). For each positive integer \(n\), form \(G_n\) by contracting every component of
\[
G-B_G(o,n)
\]
to a single vertex, leaving the ball itself uncontracted. Let \(q_n:G\to G_n\) be the quotient map.

Every contracted component has a neighbor in the ball, so
\[
\operatorname{diam}(G_n)\le2n+2.
\]
Since \(G\) is unbounded, it has a vertex at distance exactly \(n\) from \(o\), and this distance is unchanged in \(G_n\). Thus
\[
\operatorname{diam}(G_n)\ge n. \tag{4.1}
\]

Also, for every integer \(b\ge0\),
\[
d_{G_n}(q_n(x),q_n(y))=d_G(x,y)
\quad\text{if }x,y\in B_G(o,b)\text{ and }n\ge2b. \tag{4.2}
\]
Indeed, a path between such vertices that uses a contracted outside component has length at least
\[
2(n-b+1)>2b.
\]
But their distance is at most \(2b\). A shortest quotient path consequently stays inside the uncontracted ball and is an original path of \(G\).

By Lemma 2.1, each \(G_n\) has no \(c\)-fat claw. Proposition 3.1 gives an onto map
\[
f_n:G_n\to Z_n,
\]
where \(Z_n\) is a finite path or cycle, or a point, with additive distortion at most \(E\). From (4.1),
\[
\operatorname{diam}(Z_n)\ge n-E,
\]
so these diameters tend to infinity.

### Constructing a rough isometric embedding into the integer line

Let \(F\subseteq V(G)\) be finite and contain \(o\), and choose \(b\) with \(F\subseteq B_G(o,b)\). Take \(n\) sufficiently large.

By (4.2), the map \(f_nq_n\) preserves all distances on \(F\) up to additive error \(E\). Its images lie within distance \(b+E\) of \(f_nq_n(o)\).

If \(Z_n\) is a path, this neighborhood has its usual integer coordinate. If \(Z_n\) is a cycle, take \(n\) large enough that its length exceeds \(4(b+E)\). Then the same neighborhood is an interval also with respect to ambient distances in \(Z_n\).

After setting the coordinate of \(f_nq_n(o)\) equal to zero, we obtain a map
\[
h_F:F\to\mathbb Z
\]
such that
\[
h_F(o)=0,\qquad |h_F(x)|\le d_G(o,x)+E,
\]
and
\[
\left|\ |h_F(x)-h_F(y)|-d_G(x,y)\right|\le E
\quad(x,y\in F). \tag{4.3}
\]

For each \(x\), the allowed coordinate set
\[
\{-d_G(o,x)-E,\ldots,d_G(o,x)+E\}
\]
is finite. The constraints (4.3) are finitely satisfiable. Compactness of a product of finite discrete spaces therefore gives a single map
\[
h:V(G)\to\mathbb Z
\]
satisfying
\[
\left|\ |h(x)-h(y)|-d_G(x,y)\right|\le E
\quad\text{for all }x,y. \tag{4.4}
\]
For countable graphs, the same step is an ordinary diagonal argument.

Let \(I\) be the smallest integer interval containing \(h(V(G))\). Since \(G\) is unbounded, (4.4) implies that \(I\) is a ray or a double ray.

It remains to check coarse surjectivity. Adjacent vertices of \(G\) have images differing by at most \(E+1\). If an integer \(z\in I\) lies between two image values, take a path in \(G\) between corresponding vertices. Along its image sequence, some value lies within \(E+1\) of \(z\). Thus
\[
I\subseteq N_{E+1}(h(V(G))).
\]

Together with (4.4), this proves that \(h:G\to I\) is a \((1,E+1)\)-quasi-isometry. Since
\[
E+1=200(\lceil c\rceil+1)+1,
\]
Theorem A follows. ∎

Every connected graph of maximum degree at most two is claw-minor-free, so Theorem A proves the required conjectural conclusion for \(H=K_{1,3}\).

---

## 5. Passing from the claw to every subdivided claw

The next lemma supplies the needed quantitative subdivision argument; it does not assume that the original connecting paths are geodesic.

### Lemma 5.1

Let \(H\) be a subdivision of the claw whose three arms have \(a_1,a_2,a_3\) edges. Put
\[
m=\max_i a_i,\qquad s=\lceil c\rceil+1,\qquad S=6ms.
\]
If \(G\) contains an \(S\)-fat claw, then it contains a \(c\)-fat \(H\)-minor.

#### Proof

Take an \(S\)-fat claw model, with central branch set \(B\), leaf branch sets \(B_i\), and connecting paths \(P_i\). Let \(v_i\in B_i\) be the leaf endpoint of \(P_i\), and put
\[
R=2ms.
\]

Travel along \(P_i\) from \(B\) toward \(v_i\), and let \(p_i\) be the first vertex at distance \(R\) from \(v_i\). Such a vertex exists because \(d(v_i,B)\ge S>R\).

Let \(C\) consist of \(B\) together with these three initial path segments, up to and including \(p_i\). Then \(C\) is connected, and
\[
d(v_i,C)\ge R \quad(i=1,2,3). \tag{5.1}
\]
For the initial segment of \(P_i\), this follows from the first-entry choice of \(p_i\). For the other two segments, it follows from their \(S\)-separation from the nonincident leaf branch set \(B_i\).

Choose an ambient geodesic \(Q_i\) from \(p_i\) to \(v_i\), of length \(R\). If \(Q_i(t)\) denotes its vertex at distance \(t\) from \(p_i\), then (5.1) gives
\[
d(Q_i(t),C)\ge t. \tag{5.2}
\]
Also, since \(Q_i\subseteq B_G(v_i,R)\) and \(d(v_i,v_j)\ge S\),
\[
d(Q_i,Q_j)\ge S-2R=2ms\ge s
\quad(i\ne j). \tag{5.3}
\]

Use \(C\) as the central branch set of \(H\). On arm \(i\), measured along \(Q_i\) from \(p_i\):

* the \(j\)-th connecting path occupies
  \[
  [(2j-2)s,(2j-1)s],\qquad 1\le j\le a_i;
  \]
* for \(1\le j<a_i\), the \(j\)-th internal branch set occupies
  \[
  [(2j-1)s,2js];
  \]
* the terminal branch set is the vertex at position \((2a_i-1)s\).

These pieces fit because \((2a_i-1)s<R\).

Within one arm, all required separations follow from geodesicity and the intervening length-\(s\) blocks. Separation from the central branch set follows from (5.2), and separation between different arms follows from (5.3). This is a \(c\)-fat \(H\)-model. ∎

Consequently, if \(G\) has no \(c\)-fat \(H\)-minor, it has no \(S\)-fat claw. Theorem A gives a quasi-isometry to a claw-minor-free graph. Since every subdivision of the claw contains a claw minor, that target is also \(H\)-minor-free.

For example, the argument gives the explicit additive constant
\[
C(H,c)=1200m(\lceil c\rceil+1)+201.
\]

---

## 6. Paths and the conclusion for three-leaf trees

Let \(H=P_n\), with \(n\ge2\), and set \(s=\lceil c\rceil+1\).

A geodesic of length \((2n-3)s\) contains a \(c\)-fat \(P_n\)-model: use singleton endpoint branch sets, length-\(s\) connecting corridors, and length-\(s\) internal branch blocks, alternating along the geodesic. Geodesicity verifies all ambient separation requirements.

Hence
\[
G\text{ has no }c\text{-fat }P_n
\quad\Longrightarrow\quad
\operatorname{diam}(G)<(2n-3)s.
\]
The constant map to a point is then a uniform quasi-isometry, and a point is \(P_n\)-minor-free. The case \(P_1\) is vacuous for nonempty connected ambient graphs.

Every finite tree with at most two leaves is a path. Every finite tree with exactly three leaves has precisely one vertex of degree three and all other degrees at most two, so it is a subdivision of the claw. Lemma 5.1 and Theorem A therefore complete the proof of Corollary B. ∎

---

## 7. What remains unresolved

This is not a proof of the catalog conjecture for arbitrary trees or planar graphs.

The first uncovered trees include \(K_{1,4}\) and trees with two degree-three vertices. The reduction to fat-claw exclusion cannot simply be extended to them: an infinite tripod is \(K_{1,4}\)-minor-free but contains fat claws at every scale.

The argument's substantive additional conclusions over the supplied attempt are:

1. **Uniformity for the claw**, including bounded graphs and the one-ended case.
2. **No local-finiteness assumption.**
3. **All subdivisions of the claw**, via an explicit fat-model conversion.

No general counterexample is obtained, and no novelty claim is made for these special cases.