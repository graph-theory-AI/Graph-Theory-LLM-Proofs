```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove z(G'_k) >= c(G)+1 for every odd k >= 2 diam(G)+3, establishing the intended conjecture whenever z(G)=c(G).",
  "would_publish": false,
  "caveats": "The case z(G)>c(G) and the proposed universal choice k=5 remain unresolved; novelty of the partial bound has not been checked."
}
```

## 1. Formulation and partial result

I address the genuine formulation identified in the supplied source check:
\[
z(G'_k)\ge z(G)+1,
\]
not the catalog’s garbled strict inequality. Thus the previous \(K_2\) argument is not a counterexample.

All graphs below are finite, simple, connected, and have at least one edge. Zombies choose their initial positions first, the survivor then chooses a position, and the zombies move first in each round. Each zombie must move to a neighbor strictly closer to the current survivor. The survivor may move to a neighbor or stay. Write \(c(G)\) for the ordinary cop number, where cops may stay and have no geodesic restriction.

The partial result is the following.

**Theorem.** Let \(D=\operatorname{diam}(G)\). For every integer \(q\ge D+2\),
\[
\boxed{z\bigl(G'_{2q-1}\bigr)\ge c(G)+1.}
\]

Consequently, whenever \(z(G)=c(G)\), the conjectured increase holds with
\[
k=2D+3.
\]
In fact, every odd \(k\ge 2D+3\) works for such a graph.

This covers, for example, all nontrivial trees and all cycles. For graphs with \(z(G)=1\), a simpler argument below shows that every \(k\ge2\) works.

The proof uses long added paths to turn a sufficiently compact zombie configuration into a permanently following convoy. Ordinary cop evasion supplies a safe position from which to initiate that convoy.

## 2. Geometry of the augmented subdivision

Fix \(q\), and put
\[
H=G'_{2q-1}.
\]
Thus every original edge \(uv\) has an additional, internally disjoint path
\[
P_{uv}: \quad u=x_0,x_1,\ldots,x_{2q}=v
\]
of length \(2q\), while the original edge \(uv\) remains. Together they form an odd cycle of length \(2q+1\).

Call vertices of \(G\) **base vertices**. Distances between base vertices are unchanged:
\[
d_H(u,v)=d_G(u,v)\qquad(u,v\in V(G)).
\]
Indeed, traversing an added path between its endpoints can always be shortened by using the corresponding original edge.

For a vertex \(x_i\) of \(P_{uv}\), define its **height** to be
\[
h(x_i)=\min\{i,2q-i\};
\]
base vertices have height zero. This is precisely its distance to the base graph.

### Lemma 1: escape into a convoy

Let \(P_{uv}\) be one of the added paths. Suppose all zombies are outside its interior. Let \(a\) be an integer with \(0\le a\le q-1\), and suppose every zombie position \(w\) satisfies
\[
2\le a+d_H(w,u)\le q. \tag{1}
\]
Then a survivor starting at \(x_a\) can evade forever by repeatedly walking in the direction
\[
u,x_1,\ldots,x_{2q}=v,u.
\]

**Proof.** For any \(w\) outside the interior of \(P_{uv}\), and any \(0\le j\le2q\),
\[
d_H(w,x_j)
=
\min\bigl\{d_H(w,u)+j,\ d_H(w,v)+2q-j\bigr\}.
\]
The edge \(uv\) gives
\[
|d_H(w,u)-d_H(w,v)|\le1.
\]
Consequently, when \(j\le q-1\), the first term is strictly smaller. Every shortest path to \(x_j\) therefore enters the added path through \(u\).

Consider one zombie initially at distance \(b=d_H(w,u)\) from \(u\). Until it reaches \(u\), it is forced to decrease its distance to \(u\) at every move. To see that the preceding observation remains applicable, after \(t<b\) rounds the survivor is at \(x_{a+t}\), and
\[
a+t\le a+b-1\le q-1.
\]
Thus the zombie reaches \(u\) after exactly \(b\) moves. At that time the survivor is at \(x_{a+b}\), at forward distance
\[
\delta=a+b\in[2,q]
\]
from the zombie.

Every geodesic between vertices of the cycle \(P_{uv}+uv\) stays in that cycle. A path leaving it would have to leave and re-enter through \(u,v\), and replacing the external portion by \(uv\) would shorten it. Since this cycle has odd length \(2q+1\), a forward distance \(\delta\le q\) determines a unique geodesic, in the forward direction.

Hence, once the zombie reaches \(u\), it is forced to follow the survivor forever at distance \(\delta\). Before reaching \(u\), its distance to the survivor at the end of each round is also \(\delta\). Since \(\delta\ge2\), capture never occurs. This applies independently to every zombie. ∎

### Lemma 2: zombies chasing a base survivor project to ordinary cops

Suppose the survivor stays in \(G\). A zombie of initial height \(h\) has height
\[
\max\{h-t,0\}
\]
after \(t\) completed rounds. Once it reaches \(G\), it remains in \(G\).

Moreover, its position can be projected to a base vertex so that these projected positions form a legal ordinary-cop walk.

**Proof.** If the survivor is at a base vertex \(s\), then
\[
d_H(x_i,s)
=
\min\bigl\{i+d_G(u,s),\ 2q-i+d_G(v,s)\bigr\}. \tag{2}
\]
Because
\[
|d_G(u,s)-d_G(v,s)|\le1,
\]
a zombie at \(x_i\) with \(i<q\) must move toward \(u\), and one with \(i>q\) must move toward \(v\). At the midpoint \(x_q\), either direction may be available, but after the first move its endpoint is fixed: all subsequent moves, until reaching the base, go toward that endpoint.

For the projection, use the nearer endpoint while the zombie is internal, and its actual position once it is in \(G\). At an initial midpoint choose either endpoint in advance. If the zombie’s first move selects the other endpoint, the projection moves across the original edge \(uv\). Otherwise the projection waits until the zombie reaches its endpoint. Subsequent actual moves in \(G\) project to ordinary edge moves.

These are all legal cop moves, including the waiting moves. ∎

We will also use the following distance inequality. If \(p\) is either allowed endpoint projection of a zombie at \(w\), and \(s\) is a base vertex, then
\[
d_G(p,s)\le d_H(w,s). \tag{3}
\]
For internal vertices this follows directly from (2); for base vertices it is equality.

## 3. Restricting ordinary cop evasion to the 2-core

Suppose \(c(G)\ge2\). Let \(K\) be the 2-core of \(G\), obtained by repeatedly deleting vertices of degree at most one. Then:

1. \(K\) is nonempty and has minimum degree at least two.
2. Each component outside \(K\) is a tree attached to \(K\) at a unique vertex.
3. Collapsing each such attached tree to its attachment vertex defines a retraction
   \[
   \rho:G\longrightarrow K
   \]
   that sends an edge to an edge or a single vertex.
4. We have
   \[
   c(K)=c(G).
   \]

For completeness, the cop-number equality has a short proof. Projecting a winning cop strategy in \(G\) under \(\rho\), against a survivor confined to \(K\), shows \(c(K)\le c(G)\). Conversely, cops can play a winning strategy in \(K\) against the projected survivor \(\rho(s)\). When a cop reaches \(\rho(s)\), either the actual survivor is captured or it is in a tree attached at that vertex. That cop then pursues it through the tree, blocking its only exit and eventually capturing it. Thus \(c(G)\le c(K)\).

In particular,
\[
d_K\bigl(\rho(p),s\bigr)\le d_G(p,s)
\qquad(s\in V(K)). \tag{4}
\]

With fewer than \(c(K)\) ordinary cops, every initial cop placement admits a survivor starting position and a strategy for perpetual evasion. Such a strategy necessarily maintains distance at least two from every cop at the end of each survivor turn: an adjacent cop could capture on the next move.

Combining Lemma 2 with \(\rho\), any selected zombies chasing a survivor in \(K\) can therefore be treated conservatively as ordinary cops on \(K\).

## 4. Proof of the theorem

Let
\[
c=c(G),\qquad q\ge D+2,
\]
and consider an arbitrary initial placement of \(c\) zombies in \(H\). We show that the survivor can evade.

### The case \(c=1\)

For any original edge \(uv\), its added path together with \(uv\) is a cycle \(C_{2q+1}\). This cycle is a cop retraction of \(H\): fix its vertices and map every other vertex to \(u\). This sends every edge to an edge or a single vertex, since the only cycle vertices with external neighbors are \(u,v\).

A cycle of length at least four cannot be won by one ordinary cop. The survivor starts at distance at least two and, whenever the cop becomes adjacent, moves to the other cycle-neighbor to restore distance two. Cop number is monotone under retractions, so
\[
z(H)\ge c(H)\ge2=c(G)+1.
\]

The same argument applies to \(G'_k\) for every \(k\ge2\), not just the odd values used in the theorem.

Henceforth suppose \(c\ge2\), and use the 2-core \(K\) above.

Let \(h\) be the maximum initial height of any zombie.

### Case A: \(h=0\)

All zombies start in \(G\). Choose any original edge \(uv\), and start the survivor at \(x_2\) on its added path.

For every zombie \(w\),
\[
2\le 2+d_H(w,u)=2+d_G(w,u)\le D+2\le q.
\]
The path interior is empty, so Lemma 1, with \(a=2\), gives perpetual evasion.

### Case B: \(h=1\)

Choose a zombie \(Z_*\) of height one. Project the other \(c-1\) zombies first to base vertices \(p_i\), and then to \(\rho(p_i)\in K\).

Since \(c(K)=c\), choose a cop-evading initial position \(s\in K\) against those \(c-1\) projected cops. In particular,
\[
d_K\bigl(s,\rho(p_i)\bigr)\ge2. \tag{5}
\]

Because \(s\) has at least two incident edges in \(K\), choose an edge \(sv\in E(K)\) whose added path does not contain \(Z_*\).

No other zombie lies in that added path’s interior. Indeed, any such zombie would project to \(s\) or \(v\), contradicting (5). Also, no zombie is at \(s\): this follows from (5) for the included zombies, while \(Z_*\) is internal.

All zombies have height at most one, so
\[
1\le d_H(w,s)\le D+1
\]
for every zombie \(w\). Start the survivor at \(x_1\) on the selected path, oriented from \(s\). Then
\[
2\le 1+d_H(w,s)\le D+2\le q.
\]
Lemma 1, with \(a=1\), again gives perpetual evasion.

### Case C: \(h\ge2\)

Choose a zombie \(Z_*\) whose initial height is \(h\). Treat the remaining \(c-1\) zombies as projected ordinary cops on \(K\), using Lemma 2 and \(\rho\).

The survivor starts in \(K\) and follows an ordinary-cop evasion strategy against these projected cops for
\[
T=h-2
\]
complete rounds.

This is safe against the included zombies: by (3) and (4), their actual distances to the survivor are at least their projected distances. It is also safe against \(Z_*\), whose height remains at least two throughout these rounds.

At time \(T\):

- \(Z_*\) has height exactly two;
- every zombie has height at most two;
- writing \(s\in K\) for the survivor’s current vertex, every included projected cop satisfies
  \[
  d_K\bigl(s,\rho(p_i(T))\bigr)\ge2. \tag{6}
  \]

Choose an edge \(sv\in E(K)\) whose added path does not contain \(Z_*\). Such an edge exists because \(s\) has at least two incident edges in \(K\).

As in Case B, (6) implies that no included zombie lies in this path’s interior: its endpoint projection would otherwise be \(s\) or \(v\). Thus the selected path’s interior is completely free of zombies.

Every included zombie is at actual distance at least two from \(s\), while \(Z_*\) is at distance at least two because of its height. On the other hand, every zombie is within two steps of some base vertex, so
\[
2\le d_H(w,s)\le D+2\le q
\]
for every zombie \(w\).

The survivor now switches to walking around the selected added-path cycle, starting from \(s=x_0\). Lemma 1 with \(a=0\) gives perpetual evasion.

All possible initial maximum heights have been covered. Thus no placement of \(c(G)\) zombies wins on \(H\), proving
\[
z\bigl(G'_{2q-1}\bigr)\ge c(G)+1.
\qquad\Box
\]

## 5. Consequences and the remaining gap

The theorem establishes the conjecture for every graph satisfying
\[
z(G)=c(G),
\]
with the explicit diameter-dependent choice
\[
k=2\operatorname{diam}(G)+3.
\]
For example, cycles \(C_n\), \(n\ge4\), have \(c(C_n)=z(C_n)=2\): one cop cannot win, while two near-antipodal zombies can close in along the survivor’s arc. Thus their augmented subdivisions have zombie number at least three for the values of \(k\) covered by the theorem.

For \(z(G)=1\), the cycle-retraction argument is stronger:
\[
z(G'_k)\ge2=z(G)+1\qquad(k\ge2).
\]
The original edge used for this retraction need not be a bridge.

The unresolved issue is precise. In Lemma 2, an internal zombie projects to a pursuer that can **wait at its endpoint** while the actual zombie travels down the added path. At an initial midpoint, the projection may also make a first move that is legal for an ordinary cop but not for a deterministic zombie. Therefore these projections are ordinary cops, not necessarily legal deterministic zombies. Evasion against \(z(G)-1\) deterministic zombies cannot simply be substituted for the cop-evasion argument.

Accordingly, this proof does **not** establish the desired increase when \(z(G)>c(G)\), and it neither proves nor disproves the proposed universal choice \(k=5\).