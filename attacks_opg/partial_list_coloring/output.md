```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds, even with nonnegative vertex weights, for graphs whose every block becomes bipartite after deleting at most one vertex.",
  "would_publish": false,
  "caveats": "The general conjecture remains unresolved here; novelty of this structural special case has not been checked."
}
```

## 1. A structural special case

Call a graph **apex-bipartite** if deleting at most one vertex makes it bipartite.

I prove the following special case. No claim of novelty is made.

**Theorem.** Let \(G\) be a finite nonempty graph whose every block is apex-bipartite. Put \(k=\chi_\ell(G)\), and assign nonnegative weights \(w(v)\) to its vertices. For every integer \(0\le t\le k\) and every \(t\)-list assignment \(L\), there is a proper partial \(L\)-coloring whose colored vertices have total weight at least
\[
\frac{t}{k}\sum_{v\in V(G)}w(v).
\]

Here bridges may be counted as two-vertex blocks and isolated vertices as one-vertex blocks. Taking \(w(v)=1\) gives the conjectured bound for this class.

The main ingredient is stronger than a weighted cardinality bound. Write \(\bot\) for “uncolored.”

**Distributional proposition.** Suppose every block of \(G\) is apex-bipartite. For every integer \(t\ge2\) and every \(t\)-list assignment \(L\), there is a probability distribution on proper partial \(L\)-colorings \(\sigma\) such that
\[
\Pr(\sigma(v)=c)=\frac1{t+1}
\qquad
\text{for every }v\text{ and every }c\in L(v)\cup\{\bot\}.
\tag{1}
\]
Consequently, every vertex is colored with probability \(t/(t+1)\).

The equal probabilities for individual colors—not merely equal probabilities of being colored—will allow us to join the constructions across cutvertices.

## 2. A random-selection lemma

We first record a finite fractional matching observation.

**Lemma.** Let \(C\) be a set of \(t\) colors, and let \(A\subseteq C\) be a random set on a finite probability space. Suppose
\[
\Pr(A\cap U\ne\varnothing)\ge \frac{|U|}{t+1}
\qquad\text{for every }U\subseteq C.
\tag{2}
\]
Then, using additional randomness if necessary, one can choose
\[
Y\in A\cup\{\bot\}
\]
so that every element of \(C\cup\{\bot\}\) has probability exactly \(1/(t+1)\).

**Proof.** Make a bipartite flow network between the \(t+1\) possible outputs and the outcomes of the probability space. Give each output demand \(1/(t+1)\), and give each outcome capacity equal to its probability. Join a color to precisely the outcomes where it belongs to \(A\); join \(\bot\) to every outcome.

For a set \(U\) of color outputs, the capacity of its neighborhood is the left side of (2). A set of outputs containing \(\bot\) has neighborhood capacity \(1\), which is sufficient. Thus all fractional Hall inequalities hold. The max-flow/min-cut theorem supplies a flow of total value \(1\), defining the required joint distribution of the outcome and \(Y\). \(\square\)

## 3. The construction on an apex-bipartite graph

Let \(x\in V(G)\) be such that \(G-x\) has a fixed bipartition
\[
V(G-x)=A\mathbin{\dot\cup}B.
\]
Set \(S=L(x)\), so \(|S|=t\).

Our random experiment will reserve a color for \(x\), when \(x\) is colored, and assign every other color to one of the sides \(A,B\). A vertex in \(A\) may use only colors assigned to \(A\), and similarly for \(B\).

This guarantees properness regardless of how vertices choose among their available colors:

- each side is independent;
- a color assigned to one side cannot appear on the other;
- a color reserved for \(x\) is unavailable everywhere else.

### 3.1. Lists of size \(t\ge3\)

Choose \(\sigma(x)\) uniformly from \(S\cup\{\bot\}\). If a color is chosen, reserve it for \(x\). Assign every remaining color independently and uniformly to \(A\) or \(B\).

For \(v\ne x\), let \(A_v\subseteq L(v)\) be its available colors. We verify the selection lemma for \(A_v\).

Take \(U\subseteq L(v)\), with
\[
u=|U|\ge1,\qquad s=|U\cap S|.
\]
The reserved color belongs to \(U\) with probability \(s/(t+1)\). In that event, the remaining \(u-1\) colors all miss \(v\)'s side with probability \(2^{-(u-1)}\). Otherwise all \(u\) colors miss its side with probability \(2^{-u}\). Hence
\[
\begin{aligned}
\Pr(A_v\cap U=\varnothing)
&=\frac{s}{t+1}2^{-(u-1)}
  +\left(1-\frac{s}{t+1}\right)2^{-u}\\
&=2^{-u}\left(1+\frac{s}{t+1}\right)\\
&\le 2^{-u}\left(1+\frac{u}{t+1}\right).
\end{aligned}
\tag{3}
\]

For \(1\le u\le t\), we have
\[
2^{-u}\left(1+\frac{u}{t+1}\right)
\le 1-\frac{u}{t+1}.
\tag{4}
\]
Indeed, this is equivalent to
\[
(t+1-u)(2^u-1)\ge 2u.
\]
If \(u\le t-1\), use \(t+1-u\ge2\) and \(2^u-1\ge u\). If \(u=t\), use
\[
2^t\ge 2t+1,
\]
which holds for every \(t\ge3\).

Combining (3) and (4),
\[
\Pr(A_v\cap U\ne\varnothing)\ge \frac{u}{t+1}.
\]
The selection lemma therefore lets \(v\) choose an available color or remain uncolored, with each of its \(t+1\) states having probability \(1/(t+1)\).

Apply these choices simultaneously, conditional on the palette allocation. Any choices from the available sets are proper, so additional randomness at different vertices causes no problem. Together with the prescribed state of \(x\), this proves (1) for \(t\ge3\).

### 3.2. Lists of size \(t=2\)

The preceding independent allocation needs a small correction when \(t=2\).

Write \(S=\{a,b\}\). Choose the state of \(x\) uniformly from
\[
\{\bot,a,b\}.
\]

- If \(x\) receives \(a\) or \(b\), reserve that color and assign all remaining colors independently and fairly to the two sides.
- If \(x\) is uncolored, assign \(a\) and \(b\) to opposite sides, choosing their order uniformly. Assign all other colors independently and fairly.

Again let \(A_v\) be the available colors at \(v\ne x\).

For a singleton \(U=\{c\}\),
\[
\Pr(c\in A_v)=
\begin{cases}
1/3,&c\in\{a,b\},\\
1/2,&c\notin\{a,b\}.
\end{cases}
\]
Thus the selection inequality holds for singleton sets.

For \(U=L(v)\), classify according to \(s=|L(v)\cap\{a,b\}|\):
\[
\begin{array}{c|c}
s & \Pr(A_v\ne\varnothing)\\ \hline
0 & 3/4\\
1 & \frac13\cdot\frac12+\frac23\cdot\frac34=2/3\\
2 & \frac13\cdot1+\frac23\cdot\frac12=2/3.
\end{array}
\]
These are all the remaining nonempty subsets to check. The selection lemma now gives probability exactly \(1/3\) to each of the two colors and to \(\bot\).

This proves the distributional proposition for every apex-bipartite graph.

## 4. Joining the constructions across cutvertices

Suppose graphs \(G_1,G_2\) intersect in exactly one vertex \(z\), with no edges between their other vertices. Assume each has a distribution satisfying (1), for the restrictions of the same list assignment.

Couple the distributions as follows:

1. choose the state of \(z\) uniformly from \(L(z)\cup\{\bot\}\);
2. independently sample each graph’s distribution conditional on that state at \(z\).

Both conditional distributions exist because every state of \(z\) has positive probability \(1/(t+1)\). Each graph retains its original marginal distribution. The two partial colorings agree at \(z\), and their union is proper.

Thus property (1) is preserved under gluing along a single vertex. It is also preserved under disjoint unions. Applying this along the block-cutvertex trees proves the distributional proposition for every graph whose blocks are apex-bipartite.

## 5. Deduction of the partial-list-coloring bound

Let
\[
W=\sum_{v\in V(G)}w(v).
\]

For every \(t\ge2\), the distributional proposition gives
\[
\mathbb E\!\left[\sum_{\sigma(v)\ne\bot}w(v)\right]
=\frac{t}{t+1}W.
\]
Some proper partial coloring therefore has colored weight at least
\[
\frac{t}{t+1}W.
\tag{5}
\]

Now put \(k=\chi_\ell(G)\) and consider all cases in the conjecture.

- **\(t=0\):** the required weight is \(0\).
- **\(t=k\):** the entire graph can be colored, by the definition of \(k\).
- **\(t=1\):** take a proper ordinary \(k\)-coloring, which exists because \(\chi(G)\le k\). One of its independent color classes has weight at least \(W/k\). Color that independent set using its assigned singleton lists.
- **\(2\le t\le k-1\):** since \(k\ge t+1\), (5) gives
  \[
  \frac{t}{t+1}W\ge \frac{t}{k}W.
  \]

Every case is covered, proving the stated weighted special case. \(\square\)

## 6. Sharpness and the remaining gap

For \(t=2\), the stronger bound \(2W/3\) is sharp within this class: take a triangle with unit vertex weights and give every vertex the same two colors. At most two vertices can be colored.

The argument depends essentially on the stated block structure. It does **not** establish the distributional proposition for arbitrary graphs, nor does it settle \(t=2\) for arbitrary \(3\)-choosable graphs. In particular, no reduction from general \(k\)-choosable graphs to this structural class has been supplied.

Thus the outcome is a proved weighted special case, not a proof or disproof of the general conjecture.