```json
{
  "verdict": "proved",
  "confidence": "medium",
  "one_line": "Under the standard LOCAL-model formulation of Corollary 2.1, a randomized algorithm finds a Δ-list-coloring in O(log^2 n) rounds, with no polynomial dependence on Δ.",
  "would_publish": false,
  "caveats": "The proof assumes Δ≥3, no uncolorable K_{Δ+1} component, unique IDs, and unbounded LOCAL messages; it does not apply to CONGEST, and novelty has not been literature-checked."
}
```

# Mathematical writeup

## 1. Formal statement

The extracted prose omits necessary hypotheses: \(K_{\Delta+1}\), with every list equal to \(\{1,\dots,\Delta\}\), is not \(\Delta\)-list-colorable. I therefore use the standard Brooks-type formulation underlying Corollary 2.1.

### Theorem
Let \(G\) be a simple \(n\)-vertex graph of maximum degree \(\Delta\ge 3\), with no connected component isomorphic to \(K_{\Delta+1}\). Suppose each vertex \(v\) is given a finite list \(L(v)\) satisfying
\[
|L(v)|\ge \Delta .
\]
In the randomized LOCAL model with unique identifiers, there is a private-coin algorithm producing a proper \(L\)-coloring, with high probability, in
\[
O(\log ^2 n)
\]
rounds.

Since \(\Delta\le n-1\),
\[
O(\log ^2 n)
 =O\!\left(\frac{\log ^3 n}{\log \Delta}\right)
\qquad(\Delta\ge3),
\]
so this removes every multiplicative polynomial dependence on \(\Delta\).

The proof uses unbounded LOCAL messages and unbounded local computation.

---

## 2. Degree-choosable graphs

A connected graph is a **Gallai tree** if every block is either a complete graph or an odd cycle; bridges count as \(K_2\)-blocks.

We use the standard degree-choosability characterization:

### Degree-choosability theorem
If a connected graph \(H\) is not a Gallai tree, then for every list assignment \(A\) satisfying
\[
|A(v)|\ge d_H(v)\qquad(v\in V(H)),
\]
the graph \(H\) has a proper \(A\)-coloring.

Only this forward implication is needed. Once all data of \(H\) are held by one processor, a coloring can be found by the constructive proof of the theorem, or simply by exhaustive search; local computation is free in the LOCAL model.

---

## 3. A randomized slack-list-coloring lemma

We first isolate an elementary subroutine.

### Lemma 1
Let \(J\) be any graph, and suppose every vertex \(v\) has a current list \(A(v)\) with
\[
|A(v)|\ge d_J(v)+1.
\]
Then \(J\) can be list-colored in \(O(\log n)\) randomized LOCAL rounds with probability at least \(1-n^{-c}\), for any fixed \(c\), by adjusting the constant.

### Proof
In each round, every currently uncolored vertex independently:

1. activates with probability \(p=1/2\);
2. if active, chooses a uniformly random color from its current list;
3. commits to that color if no active uncolored neighbor chose the same color.

When a neighbor commits, its color is deleted from the current list. If \(U\) is the current uncolored graph, the invariant
\[
|A(v)|\ge d_U(v)+1
\]
is preserved: each newly colored neighbor decreases \(d_U(v)\) by one and deletes at most one color.

Condition on the entire previous history and on \(v\) still being uncolored. Given that \(v\) activates, the union bound gives
\[
\begin{aligned}
\Pr(\text{\(v\) has a conflict}\mid v\text{ active})
&\le
\frac{p}{|A(v)|}
 \sum_{u\in N_U(v)}
 \frac{|A(v)\cap A(u)|}{|A(u)|}  \\
&\le
p\,\frac{d_U(v)}{|A(v)|}
\le p .
\end{aligned}
\]
Thus
\[
\Pr(v\text{ commits in this round}\mid\text{history})
\ge p(1-p)=\frac14.
\]
Consequently, after \(T\) rounds,
\[
\Pr(v\text{ is still uncolored})\le (3/4)^T.
\]
Taking \(T=C\log n\) and applying the union bound proves the lemma. ∎

---

## 4. The local Gallai-tree growth lemma

The main structural point is that every vertex is within logarithmic distance of either a vertex with degree below \(\Delta\), or a connected induced subgraph which is degree-choosable.

Let
\[
k=\left\lceil\log_2(n+1)\right\rceil,
\qquad
R=2k+3.
\]

### Lemma 2
Let \(x\in V(G)\), and assume that the connected component of \(x\) is not \(K_{\Delta+1}\). Then at least one of the following holds:

1. \(B_R(x)\) contains a vertex \(z\) with \(d_G(z)<\Delta\);
2. the induced graph \(G[B_R(x)]\) is not a Gallai tree.

### Proof
Suppose that every vertex of \(B_R(x)\) has degree exactly \(\Delta\), and put
\[
F=G[B_R(x)].
\]
Assume for contradiction that \(F\) is a Gallai tree.

Every vertex \(u\) satisfying
\[
\operatorname{dist}_G(x,u)\le R-1
\]
has all its neighbors in \(B_R(x)\), and hence
\[
d_F(u)=\Delta.
\]

No block of \(F\) is \(K_{\Delta+1}\). Indeed, every vertex of such a block already has \(\Delta\) neighbors inside it, so the block would be an entire connected component of \(G\), contrary to the hypothesis.

Root the block-cut tree of \(F\) at \(x\). For a vertex \(v\) reached through a parent block \(P\), write
\[
a=d_P(v),\qquad
r=\Delta-a.
\]
The incident edges of \(v\) are partitioned among its blocks, so \(r\) is exactly the total contribution of the child blocks of \(v\). Since no parent block is \(K_{\Delta+1}\), \(a\le\Delta-1\) and hence \(r\ge1\).

We claim that from such a state \((v,P)\), provided the relevant vertices still have degree \(\Delta\) in \(F\), one can reach two new states in distinct descendant parts of the block-cut tree at graph distance at most two from \(v\).

- If \(r\ge2\) and there are at least two child blocks, choose one neighbor of \(v\) in each of two different child blocks.
- If \(r\ge2\) and there is exactly one child block \(C\):
  - if \(C\) is complete, it contains \(r\ge2\) neighbors of \(v\);
  - if \(C\) is an odd cycle, then \(r=2\), and the two cycle-neighbors of \(v\) may be chosen.
  
  Each chosen vertex has fewer than \(\Delta\) neighbors in \(C\), and hence, because its total degree in \(F\) is \(\Delta\), it has a child block outside \(C\). The two resulting descendant portions are disjoint.
- If \(r=1\), the unique child block is a bridge \(vy\). At \(y\), the parent block contributes one edge, leaving \(\Delta-1\ge2\) child-edge contribution. Applying the preceding case at \(y\) yields two descendant states within distance two of \(v\).

At the root \(x\), there must be at least two incident blocks. Otherwise its unique block would contribute all \(\Delta\) incident edges; in a Gallai tree and for \(\Delta\ge3\), that block would be \(K_{\Delta+1}\), which was excluded.

We may therefore iterate the branching claim \(k\) times. Different branches remain in disjoint portions of the block-cut tree, so the \(k\)-th generation contains at least \(2^k\) distinct vertices. Every constructed path has length at most \(2k<R\), so all vertices at which branching is required indeed have degree \(\Delta\) in \(F\).

But
\[
2^k\ge n+1,
\]
contradicting \(|V(F)|\le n\). Thus \(F\) is not a Gallai tree. ∎

---

## 5. Constructing separated cores

For each vertex \(x\), define a connected candidate core \(C_x\subseteq B_R(x)\):

- if \(B_R(x)\) contains a vertex of degree below \(\Delta\), let \(C_x=\{z_x\}\), where \(z_x\) is a canonically chosen such vertex;
- otherwise let
  \[
  C_x=G[B_R(x)].
  \]

By Lemma 2, every nonsingleton candidate core is not a Gallai tree. Every candidate core is contained in \(B_R(x)\).

Set
\[
q=2R+1.
\]
Compute a maximal independent set \(X\) of the power graph \(G^q\). A standard randomized MIS algorithm uses \(O(\log n)\) rounds with high probability on any graph. One virtual round on \(G^q\) can be simulated in \(O(q)\) LOCAL rounds by flooding all relevant information to distance \(q\). Hence this step costs
\[
O(q\log n)=O(\log^2 n)
\]
rounds.

For completeness, one may use the usual marking algorithm: an active vertex \(v\) marks itself with probability inversely proportional to its current active degree, marked vertices with no marked neighbor enter the MIS, and they and their neighbors become inactive. The standard good-vertex estimate contracts the expected number of active edges by a fixed constant factor per round; \(O(\log n)\) rounds suffice with probability \(1-n^{-c}\).

Let
\[
S=\bigcup_{x\in X}V(C_x).
\]

Two properties are immediate.

### Separation
If \(x,y\in X\) are distinct, then
\[
\operatorname{dist}_G(x,y)\ge q+1=2R+2.
\]
Since \(C_x\subseteq B_R(x)\) and \(C_y\subseteq B_R(y)\),
\[
\operatorname{dist}_G(C_x,C_y)\ge2.
\]
Thus distinct selected cores are vertex-disjoint and have no edge between them.

### Domination
By maximality of \(X\), every vertex \(v\) is within distance \(q\) of some \(x\in X\). Since \(C_x\) contains a vertex within distance \(R\) of \(x\),
\[
\operatorname{dist}_G(v,S)\le q+R=3R+1=:D.
\]
In particular,
\[
D=O(\log n).
\]

---

## 6. Coloring toward the cores

For \(i=1,\dots,D\), define
\[
V_i=\{v\notin S:\operatorname{dist}_G(v,S)=i\}.
\]
Process these layers in decreasing order:
\[
V_D,V_{D-1},\dots,V_1.
\]

Suppose \(V_i\) is currently being processed. For \(v\in V_i\), let:

- \(d_+(v)\) be the number of neighbors in already colored layers \(V_j\), \(j>i\);
- \(d_0(v)\) be the number of neighbors in \(V_i\);
- \(d_-(v)\) be the number of neighbors in lower layers or in \(S\).

Because \(v\) has a shortest path to \(S\),
\[
d_-(v)\ge1.
\]
After deleting colors used by already colored neighbors, \(v\)'s current list \(A(v)\) satisfies
\[
|A(v)|\ge \Delta-d_+(v).
\]
Moreover,
\[
d_+(v)+d_0(v)+d_-(v)=d_G(v)\le\Delta.
\]
Therefore
\[
|A(v)|
\ge d_0(v)+d_-(v)+(\Delta-d_G(v))
\ge d_0(v)+1.
\]
Thus the induced graph \(G[V_i]\), with its current lists, satisfies the hypothesis of Lemma 1. We color \(V_i\) in \(O(\log n)\) rounds.

There are \(D=O(\log n)\) layers, so all vertices outside \(S\) are colored in
\[
O(\log^2 n)
\]
rounds with high probability.

---

## 7. Coloring the cores

Consider a selected nonsingleton core \(C=C_x\). After all vertices outside \(C\) have been colored, let \(A_C(v)\) be the colors of \(L(v)\) not used by outside neighbors. Since different selected cores have no edges between them,
\[
\begin{aligned}
|A_C(v)|
&\ge \Delta-d_G(v,V(G)\setminus C)\\
&=\Delta-\bigl(d_G(v)-d_C(v)\bigr)\\
&=d_C(v)+\Delta-d_G(v)\\
&\ge d_C(v).
\end{aligned}
\]
The core \(C\) is not a Gallai tree. The degree-choosability theorem therefore gives a proper coloring of \(C\) from the residual lists.

The diameter of \(C=G[B_R(x)]\) is at most \(2R\). Hence \(x\) can gather the entire core, its residual lists, compute a coloring centrally, and broadcast it in \(O(R)=O(\log n)\) LOCAL rounds. All cores do this simultaneously.

If \(C=\{z\}\) is a singleton core, then \(d_G(z)<\Delta\), and after its outside neighbors are colored,
\[
|A_C(z)|\ge\Delta-d_G(z)\ge1.
\]
So \(z\) can choose any remaining color.

This completes the coloring of \(G\).

---

## 8. Round complexity and probability

The costs are:

- collecting radius-\(R\) information: \(O(\log n)\);
- MIS in \(G^{2R+1}\): \(O(\log^2 n)\) with high probability;
- distance computation from \(S\): \(O(\log n)\);
- coloring \(O(\log n)\) layers, each in \(O(\log n)\): \(O(\log^2 n)\);
- centralized coloring of all cores: \(O(\log n)\).

Hence the total is
\[
O(\log^2 n)
\]
LOCAL rounds.

The only failure events are failure of the fixed-time randomized MIS computation and a vertex surviving the randomized slack-coloring phase of its layer. Choosing sufficiently large constants gives total failure probability \(n^{-c}\) for any prescribed fixed \(c\).

---

## 9. Scope and remaining caveats

1. **Literal obstruction.** Without excluding infeasible instances, the claim is false: \(K_{\Delta+1}\) with identical \(\Delta\)-element lists has no coloring.
2. **Model dependence.** Radius-\(\Theta(\log n)\) gathering may transmit exponentially much information. This is legitimate in LOCAL but not in CONGEST.
3. **Range of \(\Delta\).** The proof uses \(\Delta\ge3\). The case \(\Delta=2\) has different global behavior.
4. **Literature status.** I have not verified whether this particular argument or an equivalent \(O(\log^2 n)\) list-Brooks algorithm has already appeared. Under the stated LOCAL formulation, however, there is no mathematical gap in the argument above.