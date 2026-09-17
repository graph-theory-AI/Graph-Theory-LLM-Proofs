```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every k≥2, the sharp connectivity threshold is k+3 within proper circular-arc graphs, without any bound on induced-cycle length.",
  "would_publish": false,
  "caveats": "No unrestricted f(k) is obtained; novelty of the restricted-class result is not claimed."
}
```

## 1. A sharp restricted-class result

All graphs below are finite and simple. A \(k\)-connected graph has at least \(k+1\) vertices.

A **proper circular-arc graph** is the intersection graph of arcs on a circle, with no arc properly containing another. Equal arcs are allowed.

I prove the following.

**Theorem.** Let \(G\) be a proper circular-arc graph with
\[
t=\kappa(G)\ge 4.
\]
For any distinct vertices \(x,y\), there is an induced \(x\)-\(y\) path \(P\) such that
\[
\boxed{\kappa(G-V(P))\ge t-3.}
\]

Consequently, \((k+3)\)-connectivity suffices for the Lovász path-removal property in this class. For every \(k\ge2\), this threshold is optimal—even within unit circular-arc graphs.

This does not resolve the unrestricted conjecture. It does go beyond a bounded-induced-cycle-length hypothesis: proper circular-arc graphs can have arbitrarily long induced cycles even at arbitrarily large connectivity.

The positive argument below does not use the previous attempt’s bounded-hole theorem. I reuse its multipartite obstruction for sharpness, verifying both the obstruction and its circular-arc representation.

---

## 2. An ordered model and a separator lemma

Let \(G\) be a proper circular-arc graph on \(n\) vertices. Order its arcs by their starting points around the circle, and write the corresponding vertices as
\[
\ldots,v_{-1},v_0,v_1,\ldots,
\qquad v_{i+n}=v_i.
\]

There is an integer-valued function \(R\) satisfying
\[
i\le R(i)\le i+n-1,\qquad
R(i+n)=R(i)+n,\qquad
R(i)\le R(i+1),                                      \tag{1}
\]
such that, whenever \(i<j<i+n\),
\[
v_iv_j\in E(G)
\quad\Longleftrightarrow\quad
j\le R(i)\ \text{ or }\ i+n\le R(j).                 \tag{2}
\]

Here \(R(i)\) is the last starting-point index reached by the arc for \(v_i\), going clockwise.

For completeness, lift the starting and ending points to the real line, with one circle traversal corresponding to adding its circumference. The ending points are nondecreasing in starting-point order: otherwise an arc starting later and ending earlier would be properly contained in an earlier arc. Arcs with the same starting point must be equal and can be ordered arbitrarily. This proves the monotonicity in (1); the other assertions follow directly from the representation. Formula (2) expresses that two arcs intersect precisely when at least one contains the other’s starting point.

Define the **forward set**
\[
F(i)=\{v_j:i<j\le R(i)\}.
\]
Each \(F(i)\) is a clique. Indeed, if
\[
i<a<b\le R(i),
\]
then \(R(a)\ge R(i)\ge b\), so \(v_av_b\) is an edge.

All integer intervals below are interpreted modulo \(n\).

### Two-cut lemma

**Lemma.** Suppose
\[
a<b<a+n,\qquad R(a)<b,\qquad R(b)<a+n.               \tag{3}
\]
Then \(F(a)\) and \(F(b)\) are disjoint, and
\[
F(a)\cup F(b)
\]
is a vertex cut of \(G\).

**Proof.** After deleting these two sets, the remaining vertices partition into the nonempty sets
\[
U=\{v_j:R(a)<j\le b\},
\qquad
W=\{v_j:R(b)<j\le a+n\}.
\]
Take indices \(u,v\) representing vertices in \(U,W\), respectively. Then \(u<v<u+n\), and
\[
R(u)\le R(b)<v,
\]
while
\[
R(v)\le R(a+n)=R(a)+n<u+n.
\]
Neither condition for adjacency in (2) holds. Thus there are no edges between \(U\) and \(W\). \(\square\)

An immediate consequence is useful:

> If \(G\) is connected, at most one index modulo \(n\) satisfies \(R(i)=i\).

Indeed, two such indices would satisfy (3), while both forward sets would be empty.

---

## 3. Constructing the induced path

If \(\operatorname{dist}_G(x,y)\le2\), take a shortest \(x\)-\(y\) path. It has at most three vertices, so the standard deletion inequality gives
\[
\kappa(G-V(P))\ge t-|V(P)|\ge t-3.
\]
We may therefore assume
\[
\operatorname{dist}_G(x,y)\ge3.                     \tag{4}
\]

Interchange the names of the two ends if necessary, and rotate the indexing so that
\[
x=v_0,\qquad y=v_m,\qquad 0<m<n,
\]
and
\[
R(i)>i\qquad(0\le i<m).                             \tag{5}
\]
This is possible because at most one forward set is empty, and the two clockwise segments between the ends partition the indices modulo \(n\).

We first observe that
\[
R(j)<n\qquad(0\le j\le m).                          \tag{6}
\]
For \(j=0\), nonadjacency of \(x,y\) gives \(R(0)<m\). For \(j=m\), it gives \(R(m)<n\). If \(0<j<m\) and \(R(j)\ge n\), then \(v_j\) is adjacent to both \(v_0\) and \(v_m\), contradicting (4).

Now define
\[
p_0=0,\qquad
p_{i+1}=\min\{R(p_i),m\},
\]
stopping when \(p_q=m\). By (5), this sequence is strictly increasing, so it terminates. Consecutive vertices are adjacent.

The resulting path
\[
P=v_{p_0}v_{p_1}\cdots v_{p_q}
\]
is induced. To see this, suppose \(h\ge i+2\). Since the path did not terminate at \(p_{i+1}\),
\[
p_{i+1}=R(p_i),
\]
and hence
\[
p_h>R(p_i).
\]
Also, by (6),
\[
R(p_h)<n\le p_i+n.
\]
Thus (2) excludes an edge between \(v_{p_i}\) and \(v_{p_h}\).

The important additional feature is
\[
\boxed{p_{i+1}=R(p_i)\quad\text{for every edge except possibly the last.}} \tag{7}
\]

Put \(H=G-V(P)\). Since \(P\) is induced, its end \(x\) has exactly one neighbor on \(P\). Therefore
\[
|V(H)|\ge \deg_G(x)-1\ge t-1.                      \tag{8}
\]
In particular, \(H\) has enough vertices to be \((t-3)\)-connected.

---

## 4. Normalizing a hypothetical small separator

Suppose, for a contradiction, that \(H\) is not \((t-3)\)-connected. By (8), there exists
\[
S\subseteq V(H),\qquad |S|\le t-4,
\]
such that \(H-S\) is disconnected. Write
\[
D=V(P)\cup S.
\]

List the vertices of \(G-D\) in cyclic order, labeling each by its component in \(G-D\). There are at least two transitions between different component labels.

Choose two such transitions, and let \(v_a,v_b\) be their respective preceding vertices, with
\[
a<b<a+n.
\]
If \(v_{a^+}\) and \(v_{b^+}\) are the next surviving vertices after them, then the transition endpoints are nonadjacent. Hence
\[
R(a)<a^+\le b,\qquad
R(b)<b^+\le a+n.                                   \tag{9}
\]
Consequently,
\[
F(a),F(b)\subseteq D,
\]
the two sets are disjoint, and the two-cut lemma applies.

Each forward set is a clique, so it contains at most two vertices of the induced path \(P\). A direct count would give a loss of four. The greedy choice (7) reduces this to three.

### Normalizing one forward set

Suppose \(F(c)\) contains two vertices of \(P\). They must be consecutive on \(P\), say
\[
v_{p_i},v_{p_{i+1}}.
\]

Their order inside the forward interval \(F(c)\) agrees with their path order. Otherwise, after translating indices by a multiple of \(n\), \(F(c)\) would contain \(p_{i+1}\) followed by \(p_i+n\). Monotonicity would then imply
\[
R(p_{i+1})\ge p_i+n\ge n,
\]
contrary to (6).

Suppose this pair is not the final pair of \(P\). By (7),
\[
p_{i+1}=R(p_i).
\]
Using lifts with
\[
c<p_i<p_{i+1}\le R(c),
\]
monotonicity gives
\[
p_{i+1}\le R(c)\le R(p_i)=p_{i+1}.
\]
Thus
\[
R(c)=R(p_i)=p_{i+1}.                               \tag{10}
\]
We may replace \(F(c)\) by
\[
F(p_i)\subseteq F(c).
\]
The new forward set contains exactly one path vertex, namely \(v_{p_{i+1}}\), and its right boundary has not changed.

### Normalizing the two-cut

Apply this replacement to \(F(a)\) and \(F(b)\) whenever they contain two path vertices other than the final pair. Let the resulting anchors be \(a',b'\).

They satisfy
\[
a\le a'\le R(a)<b\le b'\le R(b)<a+n\le a'+n,
\]
and
\[
R(a')=R(a),\qquad R(b')=R(b).
\]
Therefore the two-cut lemma still applies to \(a',b'\).

Set
\[
C=F(a')\cup F(b').
\]
Then \(C\subseteq D\) is a vertex cut of \(G\).

After normalization, a forward set can contain two path vertices only if they are the final pair of \(P\). Because the original forward sets were disjoint, at most one of them can contain that pair. Hence
\[
|C\cap V(P)|\le3.
\]
It follows that
\[
|C|\le |S|+3\le t-1,
\]
contradicting \(t\)-connectivity.

This proves
\[
\kappa(G-V(P))\ge t-3,
\]
and completes the theorem. \(\square\)

The proof is constructive: given the ordered arc model, the path is obtained by the displayed greedy rule. No search over separators is needed.

---

## 5. Sharpness: \(k+3\) is necessary

Fix \(k\ge2\), and consider the construction from the previous attempt:
\[
G_k=K_{k-2}\vee K_{2,2,2}.
\]
It is complete multipartite, with three parts of size two and \(k-2\) singleton parts.

A complete multipartite graph on \(N\) vertices whose largest part has size two has connectivity \(N-2\): deleting everything outside a size-two part disconnects it, while deleting fewer vertices leaves at least three vertices, necessarily in at least two parts, and therefore leaves a connected graph.

Thus
\[
|V(G_k)|=k+4,\qquad \kappa(G_k)=k+2.
\]

Choose \(x,y\) in one of its size-two parts. Every other vertex is adjacent to both ends. Consequently, every induced \(x\)-\(y\) path is
\[
xzy.
\]
Indeed, on a longer path the first internal vertex would have a chord to \(y\).

After deleting \(x,z,y\), the remaining graph has \(k+1\) vertices. At least one of the other two size-two parts remains intact, so
\[
\kappa(G_k-\{x,z,y\})=(k+1)-2=k-1.
\]
Thus no induced \(x\)-\(y\) path has the required removal property.

### A unit circular-arc representation

Use a circle of circumference \(12\), and arcs of common length \(11/2\).

For the six vertices of \(K_{2,2,2}\), use starting points
\[
0,2,4,6,8,10.
\]
Two of these arcs are disjoint precisely when their starting points differ by \(6\). These are exactly the three nonadjacent pairs.

For every vertex of \(K_{k-2}\), use the arc starting at \(1\). Its circular starting-point distance from each of the six original starting points is at most \(5\), so it intersects all six arcs. The additional arcs also intersect each other.

All arcs have the same length, so none properly contains another. Therefore \(G_k\) is a unit circular-arc graph.

Combining this obstruction with the theorem yields
\[
\boxed{
\text{For every }k\ge2,\text{ the optimal threshold in proper circular-arc graphs is }k+3.
}
\]
The same exact threshold holds in the subclass of unit circular-arc graphs.

---

## 6. Scope and the remaining gap

The result is not a consequence of imposing a fixed bound on induced-cycle length. For example, replace each vertex of a cycle \(C_\ell\), \(\ell\ge4\), by a clique of order \(m\), with complete joins between consecutive cliques. The resulting graph is proper circular-arc, contains an induced \(C_\ell\), and has connectivity \(2m\):

- deleting two nonconsecutive cliques disconnects it;
- deleting fewer than \(2m\) vertices cannot empty two cliques, so the remaining graph is connected.

Thus both connectivity and induced-cycle length can grow arbitrarily within the class covered here.

The unrestricted conjecture remains unresolved by this argument. Its essential extra structure is the cyclic order with monotone reach function \(R\). That structure produces two-clique cuts whose boundaries can be shifted past greedy path vertices. General graphs need not have either feature.

Accordingly, no unrestricted value of \(f(k)\) for any new \(k\ge3\) is established here, and no novelty claim is made for the restricted-class theorem.