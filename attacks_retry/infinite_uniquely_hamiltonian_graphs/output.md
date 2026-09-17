```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For one-ended cubic graphs of end-degree four and eventual cutwidth at most five, the number of Hamilton circles is finite and even or continuum, and therefore is never one.",
  "would_publish": false,
  "caveats": "This strengthens a restricted case of the previous attempt, not the unrestricted existence problem; literature novelty is not claimed."
}
```

# A counting refinement of the four-rail obstruction

I do not resolve the general existence question. I prove the following more precise partial result.

**Theorem 1.** Let \(G\) be a connected, simple, one-ended cubic graph whose end has degree four. Suppose that \(V(G)\) has an enumeration \(v_1,v_2,\ldots\) such that
\[
\left|\delta(\{v_1,\ldots,v_n\})\right|\leq 5
\]
for all sufficiently large \(n\). Then
\[
|\mathcal H(G)|\in \{0,2,4,6,\ldots\}\cup\{2^{\aleph_0}\},
\]
where \(\mathcal H(G)\) denotes the set of Hamilton circles.

In particular, such a graph is not uniquely Hamiltonian. It also cannot have a countably infinite number of Hamilton circles.

The relevant ingredients from the previous attempt—the spanning-double-ray reduction and the four-rail transition table—are rederived below. The additional steps are a branching argument giving continuum many Hamilton circles from a two-path frontier state, and a parity argument handling the remaining, finite case. I do not use the previous attempt’s cofinal three-cut argument or any unverified literature assertion.

## 1. Hamilton circles in a one-ended graph

In a connected, locally finite, one-ended graph, Hamilton circles correspond exactly to spanning double rays.

Indeed, deleting the unique end \(\omega\) from a Hamilton circle leaves an open arc containing all vertices. Its graph edges form a connected, spanning, 2-regular graph, hence a double ray. Conversely, both tails of a spanning double ray converge to \(\omega\); adjoining \(\omega\) gives its one-point compactification, which is a circle.

We therefore count spanning double rays.

If \(D\) is a double ray and \(S\) is finite and nonempty, then \(D[S]\) is a disjoint union of finite paths and
\[
|\delta_D(S)|=2c(D[S]).
\tag{1}
\]
Thus, across a four-edge boundary, the restriction of \(D\) consists of either one spanning path or two spanning paths.

## 2. The four-rail model

Start with a finite simple graph \(F\) with four distinct labelled ports
\[
p_1,p_2,p_3,p_4.
\]
Each port has degree two in \(F\), and every other vertex has degree three.

A construction step selects two different labels \(a,b\), adds vertices \(x_a,x_b\), and adds the three edges
\[
p_ax_a,\qquad p_bx_b,\qquad x_ax_b.
\]
The new ports with labels \(a,b\) are \(x_a,x_b\); the other two ports remain unchanged. Call \(x_ax_b\) a **rung**.

Assume every label is selected infinitely often. The limit is cubic. The non-rung edges outside \(F\) form four disjoint rail rays, and every construction prefix has exactly four outgoing edges.

Assume also that the resulting graph is connected and one-ended.

We shall prove the following core statement.

**Theorem 2.** A one-ended graph in this four-rail model has a finite even number of Hamilton circles, or \(2^{\aleph_0}\) Hamilton circles.

More specifically, if an admissible two-path frontier state occurs at any finite construction prefix, then the graph has \(2^{\aleph_0}\) Hamilton circles extending that state.

One-endedness supplies the following property:
\[
\begin{gathered}
\text{For every partition of the four labels into two nonempty classes,}\\
\text{arbitrarily late rungs join the two classes.}
\end{gathered}
\tag{2}
\]
Otherwise, deleting a prefix beyond all cross-rungs would separate infinite rail tails belonging to the two classes, giving at least two ends.

The end of a graph in this model has degree exactly four: the rails give four disjoint rays, and the cofinal four-edge boundaries exclude five disjoint rays.

## 3. Frontier states and their transitions

An admissible state consists of a spanning path forest in the current prefix, together with its selected outgoing edges. Every vertex is to have degree two after those outgoing edges are included.

There are two types:

* \(P(I)\): one spanning path, with outgoing labels given by a two-element set \(I\);
* \(Q(\Pi)\): two spanning paths, using all four outgoing edges, with \(\Pi\) the pairing of their endpoint labels.

If the next rung uses \(A=\{a,b\}\), the complete transition table is
\[
\begin{array}{c|c|c}
\text{State}&\text{Condition}&\text{Next state}\\ \hline
P(I)&A=I&P(I)\\
P(I)&|A\cap I|=1&P(I\triangle A)\\
P(I)&A=I^c&Q(\{I,I^c\})\\
Q(\Pi)&\text{omit the rung}&Q(\Pi)\\
Q(\Pi)&A\notin\Pi,\ \text{use the rung}&P(A^c).
\end{array}
\tag{3}
\]

Here \(A\notin\Pi\) means that the two labels of \(A\) belong to different pairs of \(\Pi\).

To check the table, inspect the two new vertices. If an incoming rail edge is unselected, its new vertex must use both the rung and its outgoing rail edge. If both incoming edges are selected, one may omit the rung and continue along both rails. Using the rung instead joins the two incoming path ends; it is allowed precisely when they belong to different path components. Joining the two ends of the same component would create a finite cycle.

In particular, a \(P\)-state has a **forced** evolution until it first reaches a \(Q\)-state.

There is a useful algebraic description of the \(P\)-transitions. Let \(\tau_A\) be the transposition of labels \(a,b\). Unless \(I=A^c\),
\[
P(I)\longmapsto P(\tau_A(I)).
\tag{4}
\]
This map is injective on the five allowed \(P\)-states, and its image omits \(P(A^c)\).

## 4. A two-path state has continuum many Hamiltonian extensions

**Lemma 3.** Every admissible \(Q\)-state in a one-ended four-rail graph has \(2^{\aleph_0}\) spanning-double-ray extensions.

**Proof.** Start in \(Q(\Pi)\). If we keep omitting rungs, the pairing \(\Pi\) remains unchanged. By (2), there are infinitely many future rungs joining the two pairs of \(\Pi\). At any such rung, we may merge into a \(P\)-state.

For each possible merge time, perform that merge and then follow the forced \(P\)-evolution. Call the merge time:

* **returning**, if this evolution eventually reaches \(Q\) again;
* **terminal**, if it remains in \(P\) forever.

There are at most six terminal merge times.

To see this, consider terminal merges in chronological order. At a later merge rung \(A\), the newly created \(P\)-state is \(P(A^c)\). Every earlier terminal continuation is still in a \(P\)-state. By (4), its state after this rung cannot be \(P(A^c)\). Moreover, distinct earlier \(P\)-states remain distinct, because their updates are injective. Consequently, \(k\) terminal merge times give \(k\) distinct \(P\)-states at the latest of those times. There are only six \(P\)-states.

It follows that infinitely many merge times are returning.

We can now construct a binary tree of finite extensions. At each \(Q\)-state:

1. choose two different returning merge times;
2. for each choice, wait until that merge, perform it, and follow the forced \(P\)-evolution until the next \(Q\)-state;
3. repeat from each resulting \(Q\)-state.

The two extensions chosen at a branch differ on a rung: the earlier-merge extension uses it, while the later-merge extension omits it.

Every infinite branch yields nested spanning path forests. Every vertex eventually has degree two in their union. Furthermore, each stage contains a \(P\)-state, and these \(P\)-states occur at unbounded construction times. Hence any two vertices eventually lie in one selected finite path. The union is therefore connected, spanning, and 2-regular: it is a double ray.

Different binary branches give different edge sets. Thus there are at least \(2^{\aleph_0}\) extensions. There are at most that many, because the graph has countably many edges. ∎

This strengthens the extension argument in the previous attempt: a two-path state does not merely have two extensions—it has continuum many.

## 5. The safe one-path states form a forest

Fix a construction prefix. Call a two-element set \(I\) **safe** if the forced evolution from \(P(I)\) never reaches \(Q\).

Regard the safe pairs as the edges of a simple graph \(S\) on the four labels.

**Lemma 4.** The graph \(S\) is a forest.

**Proof.** A cycle on four vertices contains either a triangle or a four-cycle.

Suppose first that \(S\) contains the triangle on a three-element set \(T\), with remaining label \(x\). A rung \(\{x,a\}\), where \(a\in T\), is the complement of an edge of that triangle. It would therefore send one of the three safe states to \(Q\), which is impossible.

Thus the next rung must lie entirely within \(T\). Its transposition preserves the triangle of safe states. Inductively, every future rung lies within \(T\), contradicting (2).

Now suppose \(S\) contains a four-cycle. Let \(X,Y\) be its bipartition, with \(|X|=|Y|=2\); its edge set is all four pairs joining \(X\) to \(Y\). The complement of each such pair is another edge of the same four-cycle. Hence no future rung may join \(X\) to \(Y\). The permitted transpositions, within \(X\) or within \(Y\), preserve that four-cycle of safe states. Again this contradicts (2).

Thus \(S\) contains no cycle. ∎

## 6. Finite parity and the counting dichotomy

We need a finite parity lemma, proved here to avoid relying on an external result.

**Lemma 5.** Let \(K\) be a finite simple graph and \(s\in V(K)\). Suppose every vertex other than \(s\) has odd degree. Every edge incident with \(s\) belongs to an even number of Hamilton cycles.

**Proof.** Fix an oriented edge \(e=sv_2\). Consider the finite set of Hamilton paths
\[
P=(s,v_2,\ldots,v_m=t)
\]
whose first edge is \(e\).

Form the usual rotation graph on these paths: an edge from the terminal vertex \(t\) to \(v_i\), with \(2\leq i\leq m-2\), permits reversal of the terminal segment. These operations are reversible and preserve the first edge.

The degree of \(P\) in the rotation graph is
\[
d_K(t)-1-\mathbf 1_{\{st\in E(K)\}}.
\]
Since \(t\ne s\), its degree in \(K\) is odd. Thus \(P\) has odd degree in the rotation graph exactly when \(st\) is an edge.

By handshaking, the number of such paths is even. They correspond bijectively to Hamilton cycles containing \(e\): orient the cycle to begin with \(e\), and delete its closing edge at \(s\). ∎

We can now prove Theorem 2.

If an admissible \(Q\)-state occurs at the cap, or is reachable from an admissible cap state, Lemma 3 gives continuum many Hamilton circles.

Otherwise:

* every admissible cap state is a \(P\)-state;
* every such state is safe;
* each such cap path has exactly one Hamiltonian extension, namely its forced \(P\)-evolution.

For each pair \(I\) of port labels, let
\[
h_I=\#\{\text{spanning paths of }F\text{ with endpoint labels }I\}.
\]
The number of Hamilton circles is now the finite number
\[
\sum_I h_I.
\tag{5}
\]

Add a new vertex \(s\) to \(F\), adjacent to all four ports. Every vertex other than \(s\) has degree three. Hamilton cycles in this finite graph correspond to the cap paths counted by the \(h_I\).

Applying Lemma 5 to \(sp_i\) gives
\[
\sum_{I\ni i}h_I\equiv 0\pmod 2
\qquad(i=1,2,3,4).
\tag{6}
\]
Therefore the pairs \(I\) for which \(h_I\) is odd form an even-degree subgraph on the four labels.

Every pair with \(h_I>0\) is safe. By Lemma 4, the odd-count subgraph is consequently a subgraph of a forest. The only even-degree subgraph of a finite forest is empty. Hence
\[
h_I\equiv 0\pmod 2
\qquad\text{for every }I.
\tag{7}
\]
Equation (5) is therefore even.

This covers all cases and proves Theorem 2. ∎

## 7. From eventual cutwidth five to four rails

We now prove Theorem 1 by establishing the required normal form.

Let
\[
S_n=\{v_1,\ldots,v_n\}.
\]
Choose four vertex-disjoint rays in the unique end. Once a finite set contains their four initial vertices, its edge boundary has size at least four: each ray supplies a distinct exiting edge.

Consequently, for all sufficiently large \(n\),
\[
4\leq |\delta(S_n)|\leq 5.
\tag{8}
\]
Since \(G\) is cubic,
\[
|\delta(S_n)|=3n-2|E(G[S_n])|\equiv n\pmod 2.
\]
Thus, eventually,
\[
|\delta(S_{2k})|=4,\qquad
|\delta(S_{2k+1})|=5.
\tag{9}
\]

Consider
\[
a=v_{2k+1},\qquad b=v_{2k+2}.
\]
The identity
\[
|\delta(S\cup\{v\})|-|\delta(S)|
=3-2|N(v)\cap S|
\tag{10}
\]
shows that \(a\) has exactly one neighbour in \(S_{2k}\), while \(b\) has exactly two neighbours in \(S_{2k}\cup\{a\}\).

The vertices \(a,b\) must be adjacent. Otherwise \(b\) has two neighbours in \(S_{2k}\), giving
\[
|\delta(S_{2k}\cup\{b\})|=4+3-4=3.
\]
For sufficiently large \(k\), this finite set contains the initial vertices of the four disjoint rays, a contradiction.

After discarding a finite initial segment, therefore, every consecutive pair
\[
(v_{2k+1},v_{2k+2})
\]
is adjacent.

Temporarily delete the edge within each such pair. Every remaining tail vertex then has exactly one earlier neighbour and exactly one later neighbour. The four edges leaving an initial even prefix generate four disjoint forward rays, and these contain every later vertex:

* predecessor chains strictly decrease the vertex index and reach the finite prefix;
* successor chains continue indefinitely;
* distinct chains cannot merge, because each tail vertex has only one predecessor.

Enlarge the finite prefix through complete pairs until all four rails have been entered. Its outgoing edges then have four distinct inner endpoints, giving the required degree-two ports.

The two vertices in each later consecutive pair lie on different rails. If they lay on the same rail, their consecutive indices would force their connecting rail edge to be precisely the edge we deleted. Simplicity excludes a second parallel rail edge.

Restoring the deleted edges now gives exactly the four-rail construction: every consecutive pair adds the next vertex on each of two distinct rails, together with their rung. Each rail is infinite, so each label is selected infinitely often.

Theorem 2 applies, proving Theorem 1. ∎

## 8. An independent obstruction valid for every degree

There is also a short necessary condition for any counterexample to the original problem.

**Proposition 6.** A connected, locally finite, one-ended simple graph with a unique Hamilton circle has at most two automorphisms.

**Proof.** Its unique spanning double ray \(D\) must be preserved by every automorphism. Label \(D\) by \(\mathbb Z\) in its path order. Every automorphism therefore acts as a translation or reflection of \(\mathbb Z\).

There can be no nonzero translation \(i\mapsto i+k\). Indeed, local finiteness and translation invariance would give a uniform bound \(L\) on \(|i-j|\) for all edges \(ij\): it suffices to examine neighbours of representatives modulo \(|k|\). Deleting a sufficiently long central interval would then separate the two infinite tails of \(D\), contradicting one-endedness.

Finally, two distinct reflections compose to a nonzero translation. Hence the automorphism group consists of the identity and, possibly, one reflection. ∎

In particular, a counterexample cannot be quasitransitive. This observation is self-contained and does not depend on the literature summary supplied with the problem.

## 9. Scope and the remaining gap

The counting theorem treats a genuine end-degree-four class, but neither end-degree four nor eventual cutwidth five follows from the hypotheses of Mohar’s question. No conclusion for arbitrary \(r\geq 4\), or for arbitrary one-ended cubic graphs, is obtained here.

There is a concrete obstruction to extending the frontier argument naively to five rails. Take a cap \(C_5\), with all five vertices as ports. Delete the cap edges \(12\) and \(34\) from the selected subgraph. This gives two paths with active outgoing labels \(1,2,3,4\), leaving label \(5\) inactive. Now repeat the rung sequence
\[
(5,1),(1,2),(2,3),(3,4),(4,5).
\]
At every step the rung touches the unique inactive label. The transition is forced: the inactive label moves to the other endpoint, and the two path components never merge. Yet the resulting five-rail graph is one-ended, since the recurrent rung pairs connect all five rails in a cycle.

Thus one-endedness alone does **not** make arbitrary two-path frontier states extendible once unused channels are present.

The precise progress established here is:

> **In the end-degree-four, eventual-cutwidth-five cubic case, a Hamiltonian graph has either a finite even number of Hamilton circles or continuum many—not exactly one.**

The unrestricted existence problem remains unresolved by this argument.