```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain an exact all-gold capture criterion for arbitrary support and complete optimal strategies when at most two vertices carry gold.",
  "would_publish": false,
  "caveats": "General intermediate optimal scores are not characterized; novelty and current literature status have not been verified."
}
```

# Partial results

Write \(A(T,g)\) for the maximum amount of gold the first player can guarantee. Since the total gold is fixed, maximizing one’s own amount is equivalent to minimizing the opponent’s amount.

Below, “even” and “odd” refer to the **number of remaining vertices**. A singleton is considered a leaf.

I prove two results:

1. A structural characterization of when a player can force the capture of **every** gold-bearing vertex, with arbitrary support.
2. An exact formula and constructive optimal strategies whenever at most two vertices have positive weight.

These results are self-contained; I make no claim that they are new.

## 1. Two preliminary lemmas

### Lemma 1: targeting one vertex

Let \(r\) be a designated vertex of a nonempty tree \(T\).

- If \(|T|\) is even, the player to move can force the capture of \(r\).
- If \(|T|\) is odd, the player to move can force the capture of \(r\) exactly when \(r\) is already a leaf. Otherwise the other player can force its capture.

#### Proof

On an even-order position, take \(r\) immediately if it is a leaf. Otherwise, there is a leaf whose deletion leaves \(r\) a nonleaf:

- If \(\deg(r)\geq 3\), every leaf deletion has this property.
- If \(\deg(r)=2\), the two components of \(T-r\) cannot both be singletons, since that would give \(|T|=3\). In a component with at least two vertices, choose a leaf farthest from \(r\). Its deletion does not make \(r\) a leaf.

Make such a deletion. The opponent now faces an odd-order tree in which \(r\) is not a leaf, so cannot take \(r\) immediately. After the opponent’s move, repeat this policy on the next even-order position. Eventually it captures \(r\).

For an odd-order starting position, a leaf \(r\) can be taken immediately. If \(r\) is not a leaf, every first move leaves an even-order position containing \(r\), so the other player can use the strategy just proved. ∎

Thus, if \(r\) is the only positive-weight vertex, of weight \(w\),
\[
A(T,g)=
\begin{cases}
w,& |T|\text{ is even or }r\text{ is a leaf},\\
0,&\text{otherwise}.
\end{cases}
\]

### Lemma 2: the race for the first marked vertex

Let \(M\subseteq V(T)\), with \(|M|\geq 2\), and suppose every vertex of \(M\) is a nonleaf of \(T\). In an auxiliary game, the objective is to take the **first vertex of \(M\)**; weights are irrelevant.

Let \(S\) be the minimal subtree containing \(M\), and let \(\ell(S)\) be its number of leaves. Put
\[
r=|T|-|S|-\ell(S).
\]
Then \(r\geq 0\), and the player to move can force the first marked vertex **if and only if \(r\) is odd**.

#### Proof

Call a deletion *safe* if every marked vertex remains a nonleaf afterward.

Every leaf of \(S\) belongs to \(M\). Since it is a nonleaf of \(T\), it has at least one vertex outside \(S\) attached on its side. Consequently,
\[
|T|-|S|\geq \ell(S).
\]

Every component of \(T-V(S)\) attaches to exactly one vertex of \(S\). For \(z\in V(S)\), let \(b_z\) count the vertices in components attached to \(z\). For every leaf \(z\) of \(S\), we have \(b_z\geq 1\).

A safe deletion exists precisely when \(r>0\):

- If some nonleaf \(z\) of \(S\) has \(b_z>0\), delete a leaf in one of its attached components.
- If some leaf \(z\) of \(S\) has \(b_z\geq 2\), delete a leaf on that side. At least one outside vertex remains there, so \(z\) remains a nonleaf.
- These possibilities exhaust \(r>0\).
- If \(r=0\), the tree consists of \(S\) together with one additional leaf at each leaf of \(S\). Every legal deletion exposes a marked vertex.

A safe deletion leaves \(S\) unchanged and decreases \(r\) by exactly one. An unsafe deletion allows the opponent to take a marked vertex immediately.

Thus, while avoiding immediate defeat, each player must decrease \(r\) by one. At \(r=0\), the player to move loses the race. The claimed parity rule follows. ∎

In particular, when \(M=\{u,v\}\) and \(d=\operatorname{dist}(u,v)\),
\[
r=|T|-d-3. \tag{1}
\]

The strategies in this lemma are constructive: make any safe deletion until the opponent exposes a marked vertex, then take it.

## 2. An exact all-gold criterion

Throughout a play, one player always moves on even-order positions and the other on odd-order positions. Call them \(E\) and \(O\), respectively.

For a nonempty marked set \(M\), define condition \(\mathcal C(T,M)\) as follows:

> The vertices of \(M\) lie in one bipartition class \(X\) of \(T\), and every vertex of \(X\) has degree at most two in the minimal subtree \(S\) containing \(M\).

For \(|M|=1\), this condition is automatic.

### Theorem 3: all marked vertices initially internal

Suppose \(M\neq\varnothing\) and every vertex of \(M\) is a nonleaf of \(T\). Then
\[
E\text{ can force the capture of every vertex of }M
\quad\Longleftrightarrow\quad
\mathcal C(T,M).
\]

If the condition fails, \(O\) can force the capture of at least one vertex from a particular subset of \(M\) of size two or three.

#### Sufficiency

The case \(|M|=1\) is Lemma 1.

Suppose \(|M|\geq2\) and \(\mathcal C(T,M)\) holds. Every leaf of \(S\) belongs to \(M\), hence to \(X\). Write

- \(\ell=\ell(S)\);
- \(a\) for the number of degree-two vertices of \(S\) in \(X\);
- \(b\) for the number of vertices of \(S\) in the other bipartition class.

Counting edges through their endpoint in \(X\),
\[
|E(S)|=\ell+2a.
\]
Since \(S\) is a tree,
\[
|E(S)|=\ell+a+b-1.
\]
Therefore \(b=a+1\), and
\[
|S|+\ell
=2\ell+2a+1
\quad\text{is odd}. \tag{2}
\]

By Lemma 2, \(E\) can force the first marked capture: if \(E\) is to move then \(|T|\) is even and \(r\) is odd; if \(O\) is to move then \(|T|\) is odd and \(r\) is even.

Use that lemma’s strategy and take the newly exposed marked vertex \(x\). Before this capture, all other marked vertices are still nonleaves. Moreover, \(M\) is independent, so deleting \(x\) does not change their degrees.

The remaining marked set \(M-\{x\}\) still satisfies \(\mathcal C\): its minimal connecting subtree is a subtree of \(S\), so no degree in that subtree has increased. Induction on \(|M|\) now lets \(E\) capture all remaining marked vertices. ∎

#### Necessity

There are two possible failures.

**First, suppose two marked vertices \(u,v\) lie in opposite bipartition classes.** Their distance \(d\) is odd. For their connecting path \(P\),
\[
|P|+\ell(P)=d+3
\]
is even. Lemma 2 therefore lets \(O\) force the first capture from \(\{u,v\}\), preventing \(E\) from taking both.

**Now suppose \(M\subseteq X\), but some \(x\in X\) has degree at least three in \(S\).** Each component of \(S-x\) contains a marked vertex, by minimality of \(S\). Choose marked vertices \(u_1,u_2,u_3\) in three distinct components.

Their minimal connecting subtree \(R\) is a tripod centered at \(x\). Each arm has even length, because \(x,u_1,u_2,u_3\in X\). Hence
\[
|R|=1+\sum_{i=1}^3\operatorname{dist}(x,u_i)
\]
is odd, while \(\ell(R)=3\). Thus \(|R|+\ell(R)\) is even.

Lemma 2 again lets \(O\) force the first capture from this three-element marked set. So \(E\) cannot capture all of \(M\). ∎

### Gold-bearing leaves: the boundary cases

Taking \(M=\{v:g(v)>0\}\), Theorem 3 extends to a complete decision procedure for whether either player can force **all the gold**.

Assume \(M\neq\varnothing\), and let \(L=M\cap L(T)\).

#### Even-order starting tree

Here the first player is \(E\).

- If \(L=\varnothing\), she can force all the gold exactly when \(\mathcal C(T,M)\) holds.
- If \(|L|\geq2\), she cannot force all the gold: after her first move, the opponent can take a remaining gold-bearing leaf.
- If \(L=\{x\}\), she must take \(x\) immediately to have any chance of taking everything. This succeeds exactly when either:
  - \(M=\{x\}\); or
  - every remaining marked vertex is a nonleaf of \(T-x\), and
    \(\mathcal C(T-x,M-\{x\})\) holds.

The second player cannot force all the gold, since Lemma 1 lets the first player secure any preselected positive-weight vertex.

#### Odd-order starting tree

Here the second player is \(E\).

- The second player can force all the gold exactly when \(L=\varnothing\) and \(\mathcal C(T,M)\) holds.
- The first player can force all the gold exactly when \(M\) consists of a single leaf.

For the last assertion, if at least two positive vertices exist, at least one remains after the first move; Lemma 1 lets the second player capture a remaining one.

These tests require only a bipartition and the minimal subtree joining the positive vertices. That subtree can be found by repeatedly pruning unmarked leaves, so the structural computation is linear in \(|T|\).

## 3. Exact optimal play with two positive vertices

Suppose the only positive vertices are distinct vertices \(u,v\), with
\[
g(u)=a>0,\qquad g(v)=b>0.
\]
Set
\[
M_0=\max(a,b),\qquad m_0=\min(a,b),\qquad
d=\operatorname{dist}(u,v),
\]
and let
\[
L=\{u,v\}\cap L(T).
\]

### Theorem 4

If \(n=|T|\) is odd, then
\[
A(T,g)=
\begin{cases}
\displaystyle\max_{x\in L}g(x),&L\neq\varnothing,\\[2mm]
m_0,&L=\varnothing\text{ and }d\text{ is odd},\\
0,&L=\varnothing\text{ and }d\text{ is even}.
\end{cases} \tag{3}
\]

If \(n\) is even, then
\[
A(T,g)=
\begin{cases}
a+b,&L=\varnothing\text{ and }d\text{ is even},\\
a+b,&\text{some }x\in L\text{ leaves the other positive vertex}\\
&\qquad\text{a nonleaf in }T-x,\\
M_0,&\text{otherwise}.
\end{cases} \tag{4}
\]

#### Proof for even \(n\)

Lemma 1 guarantees \(M_0\), by targeting the heavier vertex.

The all-gold characterization above specializes exactly to the first two cases of (4):

- With both marked vertices internal, their minimal connecting subtree is a path, so \(\mathcal C\) simply means that their distance is even.
- With a marked leaf \(x\), taking it secures both precisely when the other marked vertex remains a nonleaf afterward.

In every other case, the opposing strategies proved above secure at least one of the two positive vertices. Thus the first player gets at most \(M_0\), proving (4). ∎

#### Proof for odd \(n\), with both positive vertices internal

If \(d\) is even, Theorem 3 lets the second player capture both, giving \(A(T,g)=0\).

If \(d\) is odd, equation (1) gives
\[
r=n-d-3\quad\text{odd}.
\]
Lemma 2 therefore lets the first player capture the first positive vertex, securing at least \(m_0\).

Conversely, Lemma 1 lets the second player target the heavier positive vertex, limiting the first player to at most \(m_0\). Hence \(A(T,g)=m_0\). ∎

#### Proof for odd \(n\), with a positive leaf

Let
\[
c=\max_{x\in L}g(x).
\]
Taking a leaf attaining \(c\) guarantees \(c\).

No first move can guarantee more:

- After taking a positive leaf \(x\), the remaining tree has even order. The opponent can target the other positive vertex, limiting the first player to \(g(x)\leq c\).
- After taking a zero-weight leaf, the opponent can target the heavier positive vertex, limiting the first player to \(m_0\leq c\).

Thus \(A(T,g)=c\). ∎

### Explicit optimal-move rules

The proofs yield the following succinct strategy. Apply these rules afresh to the remaining position.

- **One positive vertex:** use Lemma 1.
- **Even order, with a positive leaf whose deletion leaves the other positive vertex internal:** take that leaf.
- **Even order, both positive vertices internal at even distance:** make a deletion keeping both internal.
- **Every other even-order case:** use Lemma 1 to target the heavier vertex.
- **Odd order with a positive leaf:** take a heaviest positive leaf.
- **Odd order, both positive vertices internal at odd distance:** make a deletion keeping both internal.
- **Odd order, both positive vertices internal at even distance:** the guaranteed score is zero, so every legal first move has the same minimax value.

The safe deletions required by these rules exist by the lemmas. Applying the rules at every position gives optimal continuation strategies for **both** players.

The value is computable with \(O(n)\) graph operations: find the positive vertices, their degrees, and their distance. Scanning the current leaves whenever a move is required gives an explicit \(O(n^2)\)-time implementation of an entire play, without any game-tree search.

## 4. Why the all-gold criterion does not solve the weighted game

One must not infer that the optimal score is the maximum weight of a fixed vertex set that can be forced in its entirety. Adaptive play can do better.

Here is an explicit example. Take the ten-vertex tree with center \(x\) and four arms
\[
x-p-u-u',\qquad
x-q-v-v',\qquad
x-w-w',\qquad
x-z.
\]
Give \(u,v\) weight \(1\), give \(w\) weight \(10\), and give every other vertex weight zero.

All three positive vertices are internal. The distances satisfy
\[
\operatorname{dist}(u,v)=4,\qquad
\operatorname{dist}(u,w)=\operatorname{dist}(v,w)=3.
\]
Consequently:

- The first player can force the fixed set \(\{u,v\}\), of weight \(2\).
- She can force \(\{w\}\), of weight \(10\).
- She cannot force either pair containing \(w\).

Thus the maximum weight of a fixed set she can force is \(10\).

Nevertheless, her optimal score is **11**.

For the lower bound, first take \(z\). The opponent must then delete one of \(u',v',w'\). Take the exposed positive vertex.

- If it is \(w\), the two remaining positive vertices are internal at even distance; Theorem 4 gives the first player both of them.
- If it is \(u\) or \(v\), the remaining two positive vertices have weights \(1,10\), are internal, and have odd distance. Theorem 4 gives the original first player the weight-\(10\) vertex.

So she guarantees at least \(11\).

For the upper bound, the second player can force the first capture from \(\{u,w\}\), by Lemma 2. Hence the second player guarantees at least \(1\), and the first gets at most \(12-1=11\).

This exhibits a genuine obstacle to turning the all-gold characterization into a general weighted optimization algorithm.

## 5. Scope and remaining gap

The arguments above completely cover:

- the decision whether a player can force **all** the gold, for arbitrary support;
- the exact value and optimal strategies when at most two vertices carry gold.

They do **not** characterize general intermediate optimal scores with three or more positive vertices. In particular, the first-marked-vertex parity lemma controls a useful auxiliary objective, but not the full allocation of weighted prizes.

Thus this is a partial answer to the stated problem, not a claimed resolution of the unrestricted optimal-strategy problem.