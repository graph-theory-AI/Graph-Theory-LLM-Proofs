```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every cycle of length at most nine in a 3-edge-colorable cubic graph contains a removable edge, so any counterexample must have girth at least ten and at least 62 vertices.",
  "would_publish": false,
  "caveats": "The general high-girth case is not settled, and no novelty claim is made for this partial result."
}
```

## 1. A local partial result

Parallel edges must be allowed in the suppressed graph, as in the problem’s flow formulation. For example, suppressing the two degree-two vertices of \(K_4-e\) produces three parallel edges.

Call an edge \(e\) **removable** if suppressing the degree-two vertices of \(G-e\) produces a 3-edge-colorable cubic multigraph.

I prove the following.

**Theorem.** Let \(G\) be a connected, loopless, 3-edge-colorable cubic multigraph with \(|V(G)|>2\). If \(C\) is a cycle of length at most nine, then some edge of \(C\) is removable. Here two parallel edges are regarded as a cycle of length two.

In particular:

- the conjecture holds for every such graph of girth at most nine;
- every counterexample is simple and has at least \(62\) vertices;
- consequently, the conjecture holds for every eligible graph with at most \(60\) vertices.

The proof is constructive and uses only Kempe interchanges.

## 2. A certificate for removability

Fix a proper edge coloring with colors \(a,b,c\). The edges of any two colors form a disjoint union of alternating even cycles.

**Lemma 1.** Suppose \(e=uv\) has color \(a\), and \(u,v\) belong to the same component of the subgraph formed by colors \(b,c\). Then \(e\) is removable.

**Proof.** Choose a \(u\)-\(v\) path \(P\) in that alternating \(b,c\)-cycle. Delete \(e\), and interchange \(b,c\) along \(P\).

At each internal vertex of \(P\), both incident path edges change color, so the coloring remains proper there. At each of \(u,v\), the two remaining incident edges now have the same color. Thus, on suppressing \(u,v\), each new edge can be given the common color of the path it replaces. At every remaining vertex the coloring is proper. ∎

In particular:

> **Singleton-color certificate.** If some color occurs exactly once on a cycle \(C\), the edge carrying that color is removable.

Indeed, deleting that edge from \(C\) leaves a path in the other two colors.

Every edge of a 3-edge-colored cubic graph lies on a two-color cycle, so \(G\) has no bridges. Hence \(G-e\) is connected. Since \(|V(G)|>2\), it has cubic vertices, and suppressing its degree-two vertices gives the cubic graph required in the statement.

### Independent interchanges between occurrences of one color

A **Kempe interchange** swaps two colors on one component of their two-color subgraph.

For the rest of the proof, suppose for a contradiction that **no edge of a fixed cycle \(C\) is removable**. This assumption concerns the graph, not a particular coloring, so it remains in force after every Kempe interchange.

Suppose color \(a\) occurs \(r\) times on \(C\). Removing those \(a\)-edges splits \(C\) into \(r\) nonempty alternating \(b,c\)-paths, which I call the **\(a\)-gaps**.

**Lemma 2.** Under the above assumption:

1. Two cyclically consecutive \(a\)-gaps cannot belong to the same \(b,c\)-component of \(G\).
2. If \(r=2\) or \(r=3\), all the \(a\)-gaps belong to different \(b,c\)-components. Consequently, the colors on any one gap can be interchanged without changing any other edge of \(C\).

**Proof.** Consecutive gaps are separated by an \(a\)-edge. If they belonged to the same \(b,c\)-component, both ends of that edge would lie in that component, contradicting Lemma 1.

When there are two or three gaps, every pair is cyclically consecutive. Hence their components are distinct. Swapping colors on the component containing one gap affects precisely that gap among the edges of \(C\). ∎

Thus, when a color occurs two or three times, we can independently choose either alternating phase on every gap between its occurrences.

All cyclic words below are considered up to rotation, reversal, and permutation of the colors.

## 3. Proof of the theorem

Start with any proper 3-edge coloring of \(G\). If a color occurs exactly once on \(C\), Lemma 1 already gives a contradiction. We therefore assume this never happens in the colorings constructed below.

### 3.1. Cycles initially using only two colors

Such a cycle has even length. Length two already has a singleton color, so consider lengths \(4,6,8\).

Write \(C\) as alternating colors \(a,b\), and let its length be \(2k\), where \(k\in\{2,3,4\}\). Consider the \(a,c\)-components containing its \(k\) edges of color \(a\).

No component can contain two cyclically consecutive \(a\)-edges: the intervening \(b\)-edge would then satisfy Lemma 1. Consequently:

- for \(k=2,3\), each such component contains only one \(a\)-edge of \(C\);
- for \(k=4\), each contains at most two.

If a component contains exactly one \(a\)-edge of \(C\), interchange \(a,c\) on that component. Color \(c\) now occurs exactly once on \(C\), a contradiction.

The only remaining possibility has \(|C|=8\), and a component contains two \(a\)-edges of \(C\). Interchanging \(a,c\) on it gives color counts
\[
(4,2,2).
\]
This is handled below.

### 3.2. The possible three-color count patterns

If all three colors occur and none occurs once, the cycle has length at least six. Each color class is a matching on \(C\), so each color occurs at most \(\lfloor |C|/2\rfloor\) times. The possibilities, up to permutation, are therefore exactly
\[
\begin{array}{c|c}
|C|&\text{color counts}\\ \hline
6&(2,2,2)\\
7&(3,2,2)\\
8&(4,2,2),\ (3,3,2)\\
9&(4,3,2),\ (3,3,3).
\end{array}
\]

We first eliminate the two patterns containing a color four times and another color twice.

Suppose
\[
\#a=4,\qquad \#c=2,\qquad \#b=r\in\{2,3\}.
\]
The \(r\) gaps between the \(b\)-edges are alternating \(a,c\)-paths. On each gap, the difference between the numbers of \(a\)- and \(c\)-edges belongs to \(\{-1,0,1\}\). The sum of these differences is \(2\), so some gap has one more \(a\)-edge than \(c\)-edge.

By Lemma 2, interchange \(a,c\) on this gap alone, as far as \(C\) is concerned. The new counts are
\[
\#a=\#c=3,\qquad \#b=r.
\]
Thus it suffices to handle
\[
(2,2,2),\quad (3,2,2),\quad (3,3,2),\quad (3,3,3).
\]

### 3.3. Length six: counts \((2,2,2)\)

Choose \(a\) as the distinguished color. Its two gap lengths are either
\[
(1,3)\quad\text{or}\quad(2,2).
\]

If they are \((1,3)\), independently choose their phases to be
\[
b,\qquad bcb.
\]
Then \(c\) occurs exactly once.

If they are \((2,2)\), choose their phases so that the cyclic word is
\[
a\,b\,c\,a\,c\,b.
\]
Now the two \(b\)-gaps have lengths \(1,3\), reducing to the preceding case.

### 3.4. Length seven: counts \((3,2,2)\)

Choose \(a\) to be the color occurring three times. Its gap lengths are necessarily
\[
(2,1,1).
\]
By Lemma 2, choose their phases to be
\[
bc,\qquad b,\qquad b.
\]
Again, \(c\) occurs exactly once.

### 3.5. Length eight: counts \((3,3,2)\)

Choose \(a\) to occur three times. Its gap lengths are either
\[
(3,1,1)\quad\text{or}\quad(2,2,1).
\]

For \((3,1,1)\), choose the phases
\[
bcb,\qquad b,\qquad b,
\]
giving a unique \(c\)-edge.

For \((2,2,1)\), choose phases giving the cyclic word
\[
a\,b\,c\,a\,c\,b\,a\,b.
\]
The three \(b\)-gaps now have lengths \(3,1,1\), so the preceding case applies with \(b\) distinguished.

This also finishes the count pattern \((4,2,2)\) produced earlier.

### 3.6. Length nine: counts \((3,3,3)\)

Choose \(a\) as the distinguished color. Its three gap lengths sum to six, so their multiset is one of
\[
(4,1,1),\qquad (3,2,1),\qquad (2,2,2).
\]

Independent phase choices give the following reductions:
\[
\begin{array}{c|c|c}
\text{\(a\)-gap lengths}
&\text{attainable cyclic word}
&\text{new distinguished color and gap lengths}\\ \hline
(4,1,1)
&a\,b\,c\,b\,c\,a\,b\,a\,c
&b:\ (3,2,1)\\
(3,2,1)
&a\,b\,c\,b\,a\,c\,b\,a\,c
&c:\ (2,2,2).
\end{array}
\]
Both displayed words still have three occurrences of every color. Hence we may reach the case in which one color, relabeled \(a\), has gap lengths \((2,2,2)\).

Choose phases giving
\[
a\,b\,c\,a\,b\,c\,a\,c\,b.
\]
There are three \(b\)-gaps. One is the path \(cac\). By Lemma 2, interchange \(a,c\) on its Kempe component without changing the other gaps of \(C\). The resulting cyclic word is
\[
a\,b\,c\,a\,b\,a\,c\,a\,b. \tag{1}
\]

In (1), the four \(a\)-gaps, in cyclic order, are
\[
bc,\qquad b,\qquad c,\qquad b.
\]
Let \(D\) be the \(b,c\)-component containing the singleton gap \(c\).

By Lemma 2(1), \(D\) cannot contain either neighboring singleton gap \(b\); otherwise the intervening \(a\)-edge would be removable. It may or may not contain the opposite gap \(bc\).

Interchange \(b,c\) on \(D\). The singleton \(c\)-gap becomes \(b\), the two singleton \(b\)-gaps stay unchanged, and the length-two gap remains a word with one occurrence of each color, whether or not it is interchanged. Therefore \(c\) now occurs **exactly once** on \(C\).

This is the final contradiction.

All possible cycle lengths and color-count patterns up to length nine have now been covered. The theorem follows. ∎

## 4. Consequences

### A counterexample must have at least 62 vertices

A counterexample cannot contain parallel edges, by the length-two case. It must therefore be simple, and the theorem gives girth at least ten.

The cubic Moore bound then gives
\[
|V(G)|\ge 2(1+2+4+8+16)=62.
\]

For completeness, root two breadth-first trees at the ends \(u,v\) of an edge, omitting \(uv\) from their branches, and grow both to depth four. Each is binary after its root and contains \(31\) vertices. Any repetition within one tree produces a cycle of length at most eight; any intersection between the trees produces a cycle of length at most nine. All \(62\) vertices are therefore distinct.

Since a cubic graph has even order, every eligible graph with at most \(60\) vertices satisfies the conjecture. This conclusion requires no computational enumeration.

### Constructive complexity

Given a 3-edge coloring and a cycle of length at most nine, the proof yields a linear-time procedure to find a removable edge and a coloring after suppression:

1. Trace the relevant two-color components.
2. If consecutive gaps belong to the same component, use Lemma 1.
3. Otherwise perform the prescribed Kempe interchange.

Only a bounded number of interchanges is used, and each component can be traced in \(O(|V(G)|)\) time.

### Another immediate class

Lemma 1 also covers every Hamiltonian cubic graph, without a girth restriction. Alternate \(b,c\) on a Hamiltonian cycle—its length is even—and color the complementary perfect matching \(a\). Every edge of that matching is removable.

## 5. What remains unresolved

This does **not** settle the conjecture for arbitrary 3-edge-colorable cubic graphs of girth at least ten. In longer cycles, several nonconsecutive gaps can lie in the same Kempe component, preventing the independent phase choices used above. I have not found a general way around that obstruction or an explicit counterexample.

The bounded-girth theorem above is self-contained. I have not checked whether it is already known, so I make no claim of novelty or of a publishable advance on the general conjecture.