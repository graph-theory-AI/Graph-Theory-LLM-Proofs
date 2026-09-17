```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Optimal play is polynomial-time computable for every fixed number k of gold-bearing vertices, using an exact n^{O(k)}-state compression on arbitrary trees.",
  "would_publish": false,
  "caveats": "This does not give a polynomial-time algorithm for unrestricted k; novelty and the current literature status of this parameterized result have not been verified."
}
```

# An exact algorithm for sparse gold support

Let
\[
n=|V(T)|,\qquad M=\{v:g(v)>0\},\qquad k=|M|,\qquad
G=\sum_{v\in V(T)}g(v).
\]

I prove the following partial result.

## Theorem

For every fixed \(k\), the gold-grabbing game on arbitrary trees with \(k\) gold-bearing vertices can be solved in polynomial time.

More explicitly, for \(k\ge 2\), there is an exact algorithm using at most
\[
2^k(n+1)^{6k-5}
\]
states, with polynomial work per state. It computes the minimax score and an optimal first move. Reapplying it to the actual remaining tree supplies optimal strategies for both players, including against deviations from the strategies used in the computation.

The arithmetic-operation bound is
\[
2^k n^{6k+O(1)}.
\]
All score arithmetic involves integers between \(0\) and \(G\), so the bit-cost contributes only a polynomial factor in the encoding length of the weights.

Thus this is an \(n^{O(k)}\)-time, or XP, result—not a fixed-parameter tractability claim.

The main issue is not the weighted part of the game: there are only \(k\) scoring moves. It is compressing the potentially very numerous zero-weight branches without losing their strategic effect. The proof below does that.

I use the single-target observation from the supplied lead, but prove it independently. None of the lead’s other assertions is needed.

---

## 1. Fixed parity roles and the one-prize endgame

Throughout a play, one player always moves when the remaining tree has even order, and the other always moves when it has odd order. Call them \(E\) and \(O\), respectively. A singleton is a legal leaf.

Let \(F(P)\) denote the maximum remaining gold that \(E\) can guarantee from a position \(P\). If the current order is even, \(E\) maximizes; if it is odd, \(O\) minimizes. This is legitimate because the total remaining gold is fixed.

At the initial position, the first player’s optimal score is therefore
\[
A(T,g)=
\begin{cases}
F(T,g),&n\text{ even},\\
G-F(T,g),&n\text{ odd}.
\end{cases} \tag{1}
\]

### Lemma 1: one designated vertex

On an even-order tree, the player to move can force the capture of any designated vertex \(r\).

On an odd-order tree, the player to move can force the capture of \(r\) if and only if \(r\) is already a leaf.

#### Proof

In an even-order position, take \(r\) if it is a leaf. Otherwise choose a leaf whose deletion leaves \(r\) a nonleaf.

Such a choice always exists. If \(\deg(r)\ge 3\), any leaf deletion works. If \(\deg(r)=2\), the two components of \(T-r\) cannot both have order one, because that would give \(|T|=3\). Delete a leaf in a component of order at least two; that component remains nonempty.

The opponent now moves on an odd-order tree in which \(r\) is unavailable. After the opponent’s move, repeat. The process must eventually capture \(r\).

For an odd-order starting position, an available \(r\) can be taken immediately. If \(r\) is unavailable, every legal move leaves an even-order position containing \(r\), and the opponent applies the preceding strategy. ∎

Consequently, if \(r\) is the only remaining positive vertex, of weight \(w\), then
\[
F(P)=
\begin{cases}
0,& |P|\text{ odd and }r\text{ is a leaf},\\
w,&\text{otherwise}.
\end{cases} \tag{2}
\]

The algorithm will stop its recursion at this endgame. This is important: with one prize, the shapes of the remaining zero-weight branches need not be solved recursively.

---

## 2. A small fixed skeleton

Assume \(k\ge 2\).

Let \(S\) be the minimal subtree containing \(M\). Form a tree \(K\) by retaining:

- every vertex of \(M\);
- every unmarked vertex whose degree in \(S\) is at least three;

and suppressing all other vertices of \(S\).

Let \(\beta\) be the number of retained unmarked vertices. Since every leaf of \(S\) is marked,
\[
\beta\le k-2,\qquad
|V(K)|=k+\beta,\qquad
|E(K)|=k+\beta-1\le 2k-3. \tag{3}
\]

An edge \(e\) of \(K\) represents a path in \(S\). Let \(q_e\) be the number of suppressed, necessarily zero-weight, vertices on that path.

Every component outside \(S\) is entirely zero-weight and attaches to exactly one vertex of \(S\). We initially record these components as follows.

1. **At a marked vertex \(v\):** retain the individual component sizes, forming a multiset \(P_v\).
2. **At a retained unmarked vertex \(b\):** pool their total order into a counter \(c_b\).
3. **At suppressed vertices on an edge \(e\):** pool their total order into a counter \(c_e\).

Why retain individual sizes only at marked vertices? Eventually a marked vertex can be the last prize, and then the number of its nonempty incident zero components determines whether it is a leaf. An unmarked vertex can never be that last prize.

### Basic zero-component observation

A nonempty zero-weight component attached to a retained subtree always contains a legal leaf of the whole tree. Deleting such a leaf decreases its order by exactly one; until the component disappears, it still attaches through the same edge.

Thus, while its attachment stays in the retained subtree, the component’s internal shape is irrelevant: its order can be decreased by one whenever a player chooses that component.

---

## 3. Exact quotient positions

Suppose the remaining positive set is \(M'\), with \(M'\ne\varnothing\). Let \(H\) be its minimal connecting subtree in \(K\).

Only reachable subsets are needed. In particular, a previously captured marked vertex cannot lie in \(H\): a marked vertex can be captured only after becoming a leaf of the current gold hull.

We maintain the following information:

- \(M'\), and hence \(H\);
- the individual residual sizes in each original multiset \(P_v\), for \(v\in M'\);
- a counter \(c_b\) for each unmarked skeleton vertex \(b\in H\);
- one counter \(c_e\) for each original skeleton edge.

The edge counters have two possible active meanings:

- If \(e\in E(H)\), then \(c_e\) counts the remaining zero vertices in components attached to the suppressed interior of \(e\).
- If \(e\notin E(H)\) and meets \(H\) at a marked vertex \(v\), then \(c_e\) counts the entire remaining zero component attached to \(v\) through that side.

A component outside \(H\) attached to an **unmarked** skeleton vertex is included in its vertex counter \(c_b\), rather than kept separately. All other, unused counters are zero.

Original components in \(P_v\) are never merged with the newly liberated components represented by incident edge counters.

### 3.1 Legal moves with at least two prizes

As long as \(|M'|\ge 2\), no zero vertex inside the expanded hull \(H\) is a leaf. Every leaf of a minimal connecting subtree is marked.

The legal zero moves are therefore exactly:

- decrease one positive entry of some \(P_v\);
- decrease a positive vertex counter \(c_b\);
- decrease a positive active edge counter \(c_e\).

A marked vertex \(v\) is available exactly when:

- \(v\) is a leaf of \(H\);
- its multiset \(P_v\) is empty;
- every outside component represented by an incident edge counter is empty.

These tests depend only on the recorded data.

### 3.2 Updating after a gold capture

Suppose the available marked leaf \(x\) is captured, and let
\[
H'=\operatorname{hull}_K(M'-\{x\}).
\]
The portion removed from the hull is a path from \(x\) to an attachment vertex \(a\in H'\).

Let \(P\) be its skeleton edges, and \(Q\) its internal skeleton vertices. All vertices of \(Q\) are unmarked. After deleting \(x\), the remaining zero vertices on this side form, if nonempty, one component attached to \(a\). Its order is
\[
R=
\sum_{e\in P}(q_e+c_e)
+
\sum_{b\in Q}(1+c_b). \tag{4}
\]

There are no omitted components at \(x\): all such components had to be empty for \(x\) to be a leaf.

Clear the counters on the removed path. Then:

- if \(a\) is unmarked, add \(R\) to \(c_a\);
- if \(a\) is marked, store \(R\) in the counter of the removed path’s edge incident with \(a\).

All other data are unchanged.

This operation changes the description, but does **not** delete the zero vertices counted by \(R\). They have merely moved from the mandatory hull into a prunable outside component.

### 3.3 The one-prize terminal test

When \(M'=\{r\}\), the hull is the single vertex \(r\). Its degree is exactly
\[
\#\{\text{nonempty original components in }P_r\}
+
\#\{\text{incident edge counters that are positive}\}. \tag{5}
\]
Hence the terminal value in (2) is determined by the quotient position.

### Exactness of the quotient

The preceding description preserves the minimax value.

Indeed, with at least two prizes, every real move induces one of the listed abstract moves, and every listed abstract move can be realized by choosing an appropriate actual leaf. Zero-component shapes do not affect the possible decrements or the update (4). With one prize, the recorded component counts give its exact leaf status, and Lemma 1 supplies the exact value.

Induction on the number of remaining vertices now proves equality of real and abstract game values.

At this point there are only \(O(k)\) numerical counters—but the multisets \(P_v\) might still be large and have exponentially many residual configurations. The next two sections remove that obstruction.

---

## 4. A dominance rule for branches at a marked vertex

Consider one original multiset \(P_v\), with all other quotient data fixed.

For nonnegative integer vectors of the same sum, use the usual majorization order: after sorting in decreasing order,
\[
p\succeq q
\quad\Longleftrightarrow\quad
\sum_{i=1}^j p_i\ge \sum_{i=1}^j q_i
\quad\text{for every }j.
\]
Zeros may be appended. Thus \(p\) is the more concentrated distribution of zero vertices.

Let:

- \(D_{\max}(p)\) decrease a largest positive entry by one;
- \(D_{\min}(p)\) decrease a smallest positive entry by one.

### Lemma 2: elementary partition facts

Among the vectors obtainable from \(p\) by a single decrement, \(D_{\max}(p)\) is least in majorization order, and \(D_{\min}(p)\) is greatest.

Moreover, both operations preserve majorization:
\[
p\succeq q
\implies
D_{\max}(p)\succeq D_{\max}(q),
\qquad
D_{\min}(p)\succeq D_{\min}(q). \tag{6}
\]

#### Proof

For a decreasing vector \(p\), decreasing an entry of value \(h\) subtracts one from precisely those prefix sums whose indices are at least the last occurrence of \(h\). This proves the first assertion.

For completeness, write \(m(p)\) for the multiplicity of the largest entry and \(\ell(p)\) for the number of positive entries. The prefix sums after \(D_{\max}\) are
\[
P_j-\mathbf 1_{\{j\ge m(p)\}},
\]
and those after \(D_{\min}\) are
\[
P_j-\mathbf 1_{\{j\ge \ell(p)\}}.
\]

Because the prefix sums are integers, a failure of order preservation could occur only at an index where the original prefix sums agree.

For \(D_{\min}\), a failure would require \(j\ge\ell(p)\) but \(j<\ell(q)\). Then \(P_j\) is the whole sum and \(Q_j\) is not, contradicting equality.

For \(D_{\max}\), a failure would require
\[
j\ge m(p),\qquad j<m(q).
\]
Put \(q_1=\cdots=q_{j+1}=h\). Equality at \(j\), together with dominance at \(j+1\), forces
\[
p_1=\cdots=p_{j+1}=h,
\]
contradicting \(j\ge m(p)\). ∎

### Lemma 3: concentration helps \(O\)

If two quotient positions differ only in the branch-size vector at one marked vertex, and
\[
p\succeq q,
\]
then
\[
F(p)\le F(q). \tag{7}
\]

In words, a more balanced distribution of the same zero mass helps \(E\), while a more concentrated distribution helps \(O\).

#### Proof

Induct on the common number of remaining vertices.

If there is only one remaining prize, it is at the marked vertex under consideration. Majorization implies
\[
\ell(p)\le \ell(q).
\]
The other incident components are unchanged. By (2), increasing the number of nonempty components cannot decrease \(E\)’s value: it can only turn an odd-order, available prize into an unavailable one. Thus (7) holds in the terminal case.

Now suppose there are at least two prizes.

All moves outside this particular branch group can be matched between the two positions. Their legality and updates depend on its total mass, not its distribution. Capturing its marked vertex is possible only when that total mass is zero.

If \(E\) moves, consider an optimal move from \(p\). If it decrements this group to \(p'\), reply in the \(q\)-position by using \(D_{\max}(q)\). Lemma 2 gives
\[
p'\succeq D_{\max}(p)\succeq D_{\max}(q).
\]
Induction says that the latter child has at least as large an \(E\)-value. All other moves can be matched directly. Hence \(F(q)\ge F(p)\).

If \(O\) moves, consider an optimal move from \(q\). For a decrement to \(q'\), use \(D_{\min}(p)\) in the \(p\)-position. Then
\[
D_{\min}(p)\succeq D_{\min}(q)\succeq q'.
\]
Induction gives an \(E\)-value no larger than the value of the \(q'\)-child. Again, other moves match directly. Since \(O\) minimizes, \(F(p)\le F(q)\). ∎

We obtain a useful restriction on optimal play.

### Corollary 4: extremal branch deletions

Whenever a player chooses to delete a vertex from an original branch group \(P_v\), it is sufficient to consider:

- for \(E\): a component of **largest** remaining order;
- for \(O\): a component of **smallest positive** remaining order.

Deleting a leaf anywhere within the selected component has the same abstract effect.

Thus both players have optimal strategies satisfying this rule. The choice **which branch group to play in** remains part of the minimax computation.

---

## 5. Three integers describe a large branch group

Fix a marked vertex \(v\). Sort the initial sizes in \(P_v\) as
\[
s_1\le s_2\le\cdots\le s_d.
\]
Fix these component identities in this order.

When decrementing a largest entry, break ties by choosing the first such entry. When decrementing a smallest positive entry, choose the first positive entry. These rules preserve the nondecreasing order of the residual sizes. In particular, empty components always form an initial segment.

Let \(j\) be the first nonempty component, and let its residual size be \(a\).

For a fixed original suffix
\[
(s_i,s_{i+1},\ldots,s_d),
\]
define \(W_i(t)\) as follows: repeatedly decrement a largest entry, with the same tie rule, until the total is \(t\). This gives a uniquely determined vector for every
\[
0\le t\le \sum_{h=i}^d s_h.
\]

### Lemma 5: compact branch-group description

Every branch-group configuration reachable under Corollary 4 is determined by
\[
(j,a,t), \tag{8}
\]
where \(t\) is the total residual order in components \(j+1,\ldots,d\). Their residual vector is exactly \(W_{j+1}(t)\).

#### Proof

All components after \(j\) are still nonempty. None of them has ever received a smallest-positive-entry deletion: at all earlier times, some positive component with index at most \(j\) preceded it.

Thus those components have received only largest-entry deletions. Whenever a largest-entry deletion acts on this suffix, it also acts on a largest entry of the suffix, with the prescribed tie rule.

Consequently, the suffix is the deterministic largest-decrement profile of its original sizes, and its current total \(t\) determines that profile. ∎

The empty group has a separate state. The number of possible records is at most
\[
(d+1)(n+1)^2\le (n+1)^3. \tag{9}
\]

### Explicit updates

The necessary minimum and maximum entries of every \(W_i(t)\) can be precomputed.

- A smallest-component deletion decreases \(a\).
- For a largest-component deletion, compare \(a\) with the maximum entry of \(W_{j+1}(t)\):
  - if that maximum is greater than \(a\), decrease \(t\);
  - otherwise decrease \(a\), as required by the tie rule.
- If \(a\) becomes zero, remove this initial entry. The new \(a\) is the first entry of \(W_{j+1}(t)\), and the new tail total is \(t-a\).
- If no component remains, enter the empty state.

Deleting an initial coordinate from a largest-decrement profile leaves the corresponding profile of the shorter original suffix; this also follows from the proof of Lemma 5.

A straightforward preprocessing method generates each \(W_i(t)\) by successive largest-entry decrements and stores its first and largest entries. Even scanning the suffix at every decrement gives polynomial preprocessing—\(O(n^3)\) work over all original branch groups is sufficient.

No residual branch multiset needs to be stored in the game-state table.

---

## 6. Dynamic program, state bound, and strategies

A compressed state consists of:

1. the remaining marked set \(M'\);
2. one record of the form (8) for each original marked vertex;
3. the \(\beta\) unmarked-vertex counters;
4. the \(|E(K)|\) edge counters.

Counters not currently in use are zero.

The number of remaining vertices is determined by this data:
\[
N=
|V(H)|+\sum_{e\in E(H)}q_e
+\sum_v \operatorname{mass}(P_v)
+\sum_b c_b+\sum_e c_e. \tag{10}
\]

Every move decreases \(N\) by one. In particular, the reclassification in (4) preserves all zero vertices rather than silently deleting them. The state graph is acyclic.

### Recurrence

Use (2) when one prize remains, and value zero when none remains.

Otherwise generate:

- one extremal zero move per nonempty original branch group;
- one zero move per positive numerical counter;
- every available marked-leaf move.

If \(N\) is even,
\[
F(P)=
\max_{P\to P'}
\left(
\text{gold captured by this move}+F(P')
\right). \tag{11}
\]
If \(N\) is odd,
\[
F(P)=\min_{P\to P'}F(P'). \tag{12}
\]

Gold captured in (12) belongs to \(O\), so is not added to \(F\).

The exact quotient argument proves that the unrestricted abstract game equals the real game. Corollary 4 proves that restricting branch-group deletions does not change its value. Lemma 5 then proves that every state reachable under the restricted rules has the stated compact representation. Therefore (11)–(12) compute the exact minimax value.

### State count

There are at most \(2^k\) marked subsets.

The original branch groups contribute at most \((n+1)^{3k}\) possibilities. The numerical counters contribute at most
\[
(n+1)^{\beta+|E(K)|}
\le (n+1)^{(k-2)+(2k-3)}.
\]
Thus the total number of states is at most
\[
2^k(n+1)^{3k+k-2+2k-3}
=
2^k(n+1)^{6k-5}. \tag{13}
\]

There are \(O(k)\) abstract moves per state. Computing hull changes and counter updates requires only polynomial work. This proves the stated running-time bound.

### Implementing the strategy on the actual tree

Store an optimizing move at each computed state.

- For a gold move, take its marked leaf.
- For a numerical-counter move, take any leaf in the represented zero region.
- For an original branch-group move, choose the prescribed largest or smallest component, then take any leaf in it.
- With one prize left, use Lemma 1.

There is one subtlety: the opponent need not follow the extremal-deletion restriction. After such a deviation, the old three-integer descriptions need not remain valid.

The solution is to **reinitialize the solver on the actual remaining tree**. Every remaining position is another instance with at most \(k\) gold-bearing vertices. The algorithm computes its true value and an optimal first move, irrespective of its history. Recomputing after every actual move therefore gives optimal strategies against arbitrary opposition, with only an additional factor of at most \(n\) along a complete play.

---

## 7. What this settles—and what it does not

This proves exact polynomial-time solvability for **every fixed support size**, not merely for one or two positive vertices. There is no bound on the number, degrees, or branching complexity of the zero-weight vertices, and the running time is not pseudopolynomial in the gold amounts.

The unrestricted problem is not resolved here. The exponent depends on \(k\), which may be as large as \(n\). In particular, the argument does not establish:

- a polynomial-time algorithm for arbitrary weighted trees;
- an \(f(k)n^{O(1)}\)-time algorithm;
- a hardness classification for unrestricted optimal play;
- a simple structural description of all intermediate optimal scores.

I have also not verified whether this sparse-support algorithm, or an equivalent one, is already in the literature. The claimed contribution here is the self-contained partial theorem above, not a claim of priority or a complete solution to the catalog problem.