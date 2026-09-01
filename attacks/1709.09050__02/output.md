```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The coefficient and greater-than-n questions remain open, but every connected outerplanar graph satisfies capt_2(G) <= n-1 and capt(G) <= n-1.",
  "would_publish": false,
  "caveats": "This uses the standard visible-robber timing convention and does not improve the bound for non-outerplanar planar blocks."
}
```

# Mathematical writeup

## 1. Conventions and status

All graphs are finite, simple, and connected. The cops choose their initial vertices, the robber then chooses an unoccupied vertex, and the cops move first. Staying put is allowed. Capture time counts cop moves; thus initial capture has time \(0\).

Write \(\operatorname{capt}_k(G)\) for the optimal capture time with \(k\) cops, and

\[
\operatorname{capt}(G)=\operatorname{capt}_{c(G)}(G).
\]

I do not resolve either intended question:

1. I do not prove that the coefficient \(2\) in
   \[
   \operatorname{capt}_3(G)\le 2n
   \]
   is best possible, nor do I improve it for all planar graphs.

2. I do not construct a planar graph with
   \[
   \operatorname{capt}(G)>n.
   \]

The main partial result is the following exclusion theorem.

## 2. Main partial theorem

### Theorem 1

Let \(G\) be a connected outerplanar graph of order \(n\). Then

\[
\operatorname{capt}_2(G)\le n-1.
\]

If \(G\) is 2-connected, then the stronger bound

\[
\operatorname{capt}_2(G)\le n-2
\]

holds. Consequently,

\[
\operatorname{capt}_3(G)\le n-1
\qquad\text{and}\qquad
\operatorname{capt}(G)\le n-1
\]

for every connected outerplanar graph.

Thus no outerplanar graph can answer the second question affirmatively.

The proof is a quantitative version of the usual two-cop sweep through an outerplane block.

---

## 3. Sweeping one 2-connected outerplane block

Let \(B\) be a 2-connected outerplane graph of order \(q\). Its outer-face boundary is a Hamilton cycle, and its weak dual—whose vertices are the bounded faces, with two faces adjacent when they share an edge—is a tree.

Indeed, if \(e(B)=m\), then the number of bounded faces is \(m-q+1\), while the number of non-outer edges is \(m-q\). Every non-outer edge gives one weak-dual edge, and the weak dual is connected, so it is a tree.

Choose an outer edge \(e_0\), and root the weak dual at the bounded face incident with \(e_0\). For every bounded face \(F\), let its parent edge be \(e_0\) if \(F\) is the root face, and otherwise the edge shared with its parent face.

Suppose the parent edge of \(F\) is \(v_0v_m\). Write the rest of the boundary of \(F\) as

\[
v_0v_1\cdots v_m.
\]

Thus \(\ell(F)=m+1\), and \(m\ge 2\).

For each edge \(v_iv_{i+1}\), there is either no child face across that edge, or there is a unique child weak-dual subtree attached through the two vertices \(v_i,v_{i+1}\). In a larger outerplanar graph, components outside \(B\) may also hang from a cut vertex \(v_j\); such a component meets \(B\) only at \(v_j\).

### Face-sweep lemma

Assume two cops occupy \(v_0\) and \(v_m\), and the robber is on the side of the parent edge containing \(F\) and its descendant regions. Then within at most

\[
m-1=\ell(F)-2
\]

cop moves, one of the following occurs:

1. the robber is captured;
2. the cops occupy \(v_i,v_{i+1}\), and the robber is confined to the child region across \(v_iv_{i+1}\);
3. both cops occupy some \(v_j\), and the robber is confined to a component hanging from \(v_j\).

#### Proof

Maintain indices \(a<b\), with the cops at \(v_a,v_b\), such that the robber is confined to:

- the subpath \(v_a,\ldots,v_b\);
- child regions attached across \(v_iv_{i+1}\) for \(a\le i<b\);
- as-yet-unsearched components hanging from \(v_j\) for \(a\le j\le b\).

Outerplanarity and the fact that the weak dual is a tree imply that \(\{v_a,v_b\}\) separates this interval from the already cleared portion.

Moving the left cop from \(v_a\) to \(v_{a+1}\) is safe unless the robber is in a component hanging from \(v_a\), or in the child region across \(v_av_{a+1}\). Symmetrically, moving the right cop from \(v_b\) to \(v_{b-1}\) is unsafe only when the robber lies in the corresponding rightmost region.

When \(b-a\ge2\), the leftmost and rightmost forbidden regions are disjoint. Hence at least one end can be contracted. Whenever both contractions are safe, make both moves simultaneously. After the move, the new occupied endpoints again separate the robber from the discarded part. The robber therefore cannot undo a contraction on its subsequent move.

If the interval reaches \(b=a+1\), then either the robber has been captured or it lies in the child region across \(v_av_{a+1}\), giving outcome 2. If instead the robber is in a component hanging from an endpoint, the other cop moves across \(v_av_{a+1}\), giving outcome 3.

It remains to justify the bound \(m-1\) when the cops must coalesce at a vertex rather than finish on an edge. Reducing the initial interval length \(m\) to zero requires \(m\) endpoint contractions. Unless the target hanging component was attached at \(v_0\) or \(v_m\), at least one round contracts both ends simultaneously: before its attachment vertex first becomes an occupied endpoint, that vertex is strictly internal and neither end is blocked. Thus at most \(m-1\) rounds are used. If the target is attached at \(v_0\) or \(v_m\), the other cop moves directly across the parent edge \(v_0v_m\), using one round, again at most \(m-1\). ∎

### The face budget

For a 2-connected outerplane graph \(B\),

\[
\sum_{F\text{ bounded}}(\ell(F)-2)=q-2.
\]

To see this, the outer face has length \(q\), so

\[
\sum_{F\text{ bounded}}\ell(F)=2m-q.
\]

Euler's formula gives \(m-q+1\) bounded faces. Therefore

\[
\sum_F(\ell(F)-2)
 =2m-q-2(m-q+1)
 =q-2.
\]

The face-sweep strategy follows a downward path in the weak-dual tree and never revisits a face. Hence its total cost inside \(B\) is at most \(q-2\).

This proves immediately:

### Corollary 2

If \(B\) is a 2-connected outerplanar graph of order \(q\), then

\[
\operatorname{capt}_2(B)\le q-2.
\]

Place the two cops initially on the endpoints of an outer edge and apply the sweep.

---

## 4. Passing through cut vertices

We now prove the general outerplanar case.

Place both cops initially at an arbitrary vertex \(r\). The robber lies in one component of \(G-r\), and cannot change to another because \(r\) is occupied.

Suppose at some stage both cops occupy a cut vertex \(x\), and the robber is confined to one component beyond \(x\). In the block-cut tree, let \(B\) be the next block toward the robber.

- If \(B\) is a bridge \(xy\), both cops move to \(y\). This costs one move, equal to \(|V(B)|-1\).

- If \(B\) is a 2-connected block of order \(q\), choose an outer edge \(xy\) of \(B\) incident with \(x\). One cop remains at \(x\), while the other moves to \(y\). This costs one move and establishes the initial occupied edge for the face sweep. The sweep then costs at most \(q-2\) further moves. Thus the total cost within this block is at most
  \[
  1+(q-2)=q-1.
  \]

The sweep either captures the robber or brings both cops to a cut vertex through which the robber has left the block. In the latter case the procedure repeats. The robber cannot return through a processed block because the occupied frontier separates it from the cleared side.

The blocks encountered form a simple path in the block-cut tree. If these blocks are \(B_1,\ldots,B_s\), each new block shares only its entry cut vertex with the previously processed part. Consequently,

\[
\sum_{i=1}^s\bigl(|V(B_i)|-1\bigr)\le n-1.
\]

This proves

\[
\operatorname{capt}_2(G)\le n-1.
\]

---

## 5. Passing from two-cop time to \(\operatorname{capt}(G)\)

It remains to consider outerplanar graphs whose cop number is \(1\).

### Lemma 3

Every cop-win graph of order \(n\) satisfies

\[
\operatorname{capt}_1(G)\le n-1.
\]

#### Proof

Use the dismantling characterization of finite cop-win graphs. If \(v\) is dominated by \(u\), so that

\[
N[v]\subseteq N[u],
\]

let \(H=G-v\). Map \(v\) to \(u\) and fix every vertex of \(H\). A cop can simulate an optimal game on \(H\) against the image of the robber.

If the simulated robber is captured while the real robber is not, the real robber must be at \(v\), while the cop is at \(u\). After the robber's next move, it remains in \(N[v]\subseteq N[u]\), so it is captured on the next cop move. Hence

\[
\operatorname{capt}_1(G)\le \operatorname{capt}_1(H)+1.
\]

Iterating through a dismantling order gives the claimed \(n-1\) bound. ∎

Theorem 1 gives a two-cop winning strategy on every outerplanar graph, so its cop number is at most two. If \(c(G)=1\), Lemma 3 applies; if \(c(G)=2\), Theorem 1 applies. Therefore

\[
\operatorname{capt}(G)\le n-1
\]

for every connected outerplanar graph.

More generally, Lemma 3 shows that any planar witness to \(\operatorname{capt}(G)>n\) must have cop number \(2\) or \(3\).

---

## 6. What “tight” can mean: a linear lower bound

If “tight” merely means the order of growth \(O(n)\), then linearity is already forced by very elementary planar examples.

Let \(T_{4,L}\) be the tree formed from a central vertex \(o\) by attaching four internally disjoint paths of length \(L\). It has

\[
n=4L+1
\]

vertices.

### Proposition 4

\[
\operatorname{capt}_3(T_{4,L})=L.
\]

#### Proof

For the upper bound, place a cop at \(o\). Once the robber chooses an arm, that cop moves down the arm. The robber cannot pass the cop and is caught by the time the cop reaches the leaf, in at most \(L\) moves.

For the lower bound, consider any placement of three cops.

- If no cop is at \(o\), at least one of the four arms contains no cop. The leaf of that arm is at distance at least \(L\) from every cop.
- If a cop is at \(o\), the other two cops occupy at most two arm interiors, so again some arm has no off-center cop. Its leaf is at distance \(L\) from the center cop and at least \(L\) from every other cop.

The robber chooses such a leaf and stays there. No cop can reach it in fewer than \(L\) moves. ∎

Thus

\[
\lim_{L\to\infty}
\frac{\operatorname{capt}_3(T_{4,L})}{|V(T_{4,L})|}
=\frac14.
\]

Therefore no \(o(n)\) upper bound is possible. The genuinely open interpretation is whether the leading constant \(2\) can be approached, or even whether the threshold \(n\) can be exceeded when capture time is measured using the minimum winning number of cops.

For comparison, on the path \(P_n\),

\[
\operatorname{capt}(P_n)
=\operatorname{capt}_1(P_n)
=\left\lfloor\frac n2\right\rfloor.
\]

---

## 7. Exact computational formulation

The following retrograde recurrence completely specifies an exhaustive search for small planar graphs.

For fixed \(k\), use ordered cop configurations \(C=(c_1,\ldots,c_k)\). Let

\[
M(C)=N[c_1]\times\cdots\times N[c_k]
\]

be the possible simultaneous cop moves. A state is \((C,r)\), taken immediately before a cop move.

Let \(W_0\) consist of the already captured states \(r\in C\). Recursively, put \((C,r)\in W_t\) if either it is in \(W_0\), or there is a cop move \(C'\in M(C)\) such that

\[
r\in C'
\]

or, for every legal robber reply

\[
r'\in N[r]\setminus C',
\]

one has

\[
(C',r')\in W_{t-1}.
\]

Then the least \(t\) with \((C,r)\in W_t\) is precisely the number of further cop moves required from that state. Consequently,

\[
\operatorname{capt}_k(G)
=
\min_C\;
\max_{r\notin C}
\min\{t:(C,r)\in W_t\}.
\]

The state space has at most \(n^{k+1}\) states. A direct implementation of one layer takes \(O(n^{2k+2})\) time, and stabilization occurs after at most \(n^{k+1}\) strict layers. Thus fixed-\(k\) capture time is computable by this unoptimized procedure in

\[
O(n^{3k+3})
\]

time. For \(k=3\), testing only whether \(\operatorname{capt}_3(G)\le n\) requires \(n\) layers and \(O(n^9)\) time. No computational enumeration is claimed here.

---

## 8. Remaining gap

The outerplanar proof depends crucially on the weak dual of each 2-connected block being a tree. In a general planar block, descendant regions can reconnect around interior vertices, so two occupied vertices no longer define the interval separator used in the sweep. A third cop can guard an additional path, leading to the known \(2n\) argument, but the accounting above does not reduce that cost to \(n\).

Accordingly, the two central issues remain open here:

- no planar graph with \(\operatorname{capt}(G)>n\) is produced;
- no universal improvement of \(\operatorname{capt}_3(G)\le2n\) is proved.

The established restriction is that any witness must have cop number \(2\) or \(3\) and must be non-outerplanar.