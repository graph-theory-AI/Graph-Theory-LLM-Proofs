```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A connected simple bridgeless cubic graph on 30 vertices has every 2-factor of type 5+5+5+15, and therefore has oddness 4.",
  "would_publish": false,
  "caveats": "The counterexample has cyclic 3-edge cuts; no novelty claim or resolution of a cyclically 4-edge-connected variant is made."
}
```

# A counterexample to the statement as written

The conjecture is false even when the graph is required to be **connected and simple**. In fact, under the stated hypotheses, oddness is unbounded.

## 1. The Petersen gadget

Use the following explicit model of the Petersen graph \(P\):
\[
V(P)=\{a_i,b_i:i\in\mathbb Z/5\mathbb Z\},
\]
with edges
\[
a_i a_{i+1},\qquad a_i b_i,\qquad b_i b_{i+2}
\quad(i\in\mathbb Z/5\mathbb Z).
\]

Delete \(a_0\), and put
\[
Q=P-a_0.
\]
The three degree-two vertices of \(Q\), called its terminals, are
\[
p=a_1,\qquad q=a_4,\qquad r=b_0.
\]
All other vertices of \(Q\) have degree three.

We use two elementary facts about this gadget.

**Fact 1.** Every 2-factor of \(P\) consists of two 5-cycles. Moreover, each edge incident with \(a_0\) belongs to a perfect matching of \(P\).

Here is a direct verification. A perfect matching contains an odd number of spokes \(a_i b_i\), hence one, three, or five. Three spokes are impossible: the two remaining indices would have to be adjacent both in the outer pentagon and in the inner pentagon, requiring their difference to be both \(\pm1\) and \(\pm2\) modulo five.

Five spokes give the two pentagons as the complementary 2-factor. If the only spoke is \(a_0b_0\), the matching is uniquely determined:
\[
\{a_0b_0,\ a_1a_2,\ a_3a_4,\ b_2b_4,\ b_1b_3\},
\]
and its complementary cycles are
\[
a_0a_1b_1b_4a_4a_0,
\qquad
a_2a_3b_3b_0b_2a_2.
\]
Rotating the indices handles every one-spoke matching. This enumerates all six perfect matchings; each edge incident with \(a_0\) occurs in exactly two.

**Fact 2.** The graph \(Q\) is connected and bridgeless.

Indeed, it has the Hamiltonian cycle
\[
a_1a_2a_3a_4b_4b_2b_0b_3b_1a_1.
\]
Every edge of a graph with a Hamiltonian cycle lies on a cycle: an edge outside that Hamiltonian cycle is a chord and can be combined with a path along the cycle.

## 2. Construction of the 30-vertex graph

Take three disjoint copies \(Q_1,Q_2,Q_3\), with terminals \(p_i,q_i,r_i\). Add three new vertices \(x,y,z\), and add the nine edges
\[
xp_i,\qquad yq_i,\qquad zr_i
\quad (i=1,2,3).
\]
Call the resulting graph \(G\).

Thus \(G\) has
\[
3\cdot9+3=30
\]
vertices. It is plainly simple, connected, and cubic.

It is also bridgeless. Every edge internal to a copy \(Q_i\) lies on a cycle by Fact 2. Contracting each \(Q_i\) to a single vertex produces \(K_{3,3}\), with bipartition
\[
\{Q_1,Q_2,Q_3\},\qquad \{x,y,z\}.
\]
Every attachment edge belongs to a cycle in this quotient. Such a cycle lifts to a cycle in \(G\), using a path between the appropriate terminals in each visited copy of \(Q\). Consequently, no attachment edge is a bridge either.

## 3. Every 2-factor has cycle lengths \(5,5,5,15\)

Let \(M\) be any perfect matching of \(G\). For \(i=1,2,3\), let
\[
s_i=|M\cap\delta(V(Q_i))|.
\]
Since \(Q_i\) has nine vertices,
\[
9=2|M\cap E(Q_i)|+s_i.
\]
Thus \(s_i\) is odd, so \(s_i\in\{1,3\}\).

On the other hand, every matching edge incident with \(x,y,z\) is an attachment edge, and each of these three vertices is matched exactly once. Therefore
\[
s_1+s_2+s_3=3.
\]
It follows that
\[
s_1=s_2=s_3=1. \tag{1}
\]

Set
\[
F=E(G)\setminus M.
\]
This is the 2-factor complementary to \(M\).

For each \(Q_i\), restore its deleted vertex \(a_0\). Extend \(M\cap E(Q_i)\) by matching this restored vertex to the terminal whose attachment edge belongs to \(M\). By (1), this gives a perfect matching of the Petersen graph.

By Fact 1, its complementary 2-factor consists of two 5-cycles. Deleting the restored vertex therefore leaves, inside \(Q_i\),

* one complete 5-cycle; and
* one path on four vertices, whose endpoints are the two terminals with attachment edges in \(F\).

Hence \(F\) contains three separate 5-cycles, one inside each gadget. Its remaining vertices lie on the three four-vertex paths and on \(x,y,z\).

The matching attachment edges project to a perfect matching of \(K_{3,3}\). Its complement in \(K_{3,3}\) is a single 6-cycle. Replacing the three gadget vertices on that cycle by their four-vertex paths produces a single cycle of length
\[
3+3\cdot4=15.
\]
Consequently, **every** 2-factor of \(G\) is isomorphic to
\[
C_5\;\dot\cup\;C_5\;\dot\cup\;C_5\;\dot\cup\;C_{15}. \tag{2}
\]

There is no existence issue: choose any perfect matching of the quotient \(K_{3,3}\), then independently choose a Petersen perfect matching containing the corresponding edge at each deleted vertex. These choices produce a perfect matching of \(G\). In fact, Fact 1 gives exactly
\[
3!\,2^3=48
\]
perfect matchings, and hence 48 2-factors, all of type (2).

All four cycles in (2) are odd. Therefore
\[
\boxed{\omega(G)=4>2.}
\]

# Stronger result: oddness is unbounded

The same construction gives an infinite family.

Let \(H\) be a simple bipartite cubic graph with bipartition \(A\cup B\), where
\[
|A|=|B|=m,
\]
and suppose every 2-factor of \(H\) is a Hamiltonian cycle. Replace every vertex of \(A\) by a copy of \(Q\), attaching its three terminals bijectively to the former neighbors of that vertex. Denote the resulting graph by \(G(H)\).

For any perfect matching of \(G(H)\), each of the \(m\) odd-order gadgets requires at least one matching attachment edge. The \(m\) vertices in \(B\) supply exactly \(m\) such edges altogether. Thus every gadget has exactly one matching attachment edge.

The preceding argument now shows that every 2-factor of \(G(H)\) consists of

* \(m\) separate 5-cycles; and
* one cycle containing the \(m\) vertices of \(B\) and four vertices from each gadget, hence of length \(5m\).

In symbols,
\[
F\cong mC_5\;\dot\cup\;C_{5m}.
\]
When \(m\) is odd, every cycle is odd and
\[
|V(G(H))|=10m,\qquad \omega(G(H))=m+1. \tag{3}
\]
The graph is connected and bridgeless by the same cycle-lifting argument.

For completeness, suitable graphs \(H\) exist with arbitrarily large odd \(m\), by the following elementary construction.

Start with \(H_0=K_{3,3}\). Given \(H_t\), replace a vertex in one bipartition class by \(K_{3,2}\), connecting its three former neighbors bijectively to the three vertices in the size-three class of the new gadget. This preserves simplicity, cubicity, and bipartiteness, and increases both bipartition sizes by two.

It also preserves the property that every 2-factor is Hamiltonian. To see this, consider any 2-factor in the new graph. Inside the \(K_{3,2}\) gadget, the difference between the sums of factor-degrees over its two bipartition classes is
\[
2\cdot3-2\cdot2=2.
\]
Since all attachment edges meet the size-three class, exactly two attachment edges belong to the factor. Restoring a vertex adjacent to the three terminals completes the gadget to \(K_{3,3}\); the induced 2-factor there is a 6-cycle. Thus the factor uses the gadget as a single spanning path. Contracting this path back to the replaced vertex gives a 2-factor of \(H_t\), which is Hamiltonian by induction.

Hamiltonian cycles exist throughout: a Hamiltonian cycle of \(H_t\) lifts using a spanning path of \(K_{3,2}\) between the two required terminals.

Therefore \(H_t\) has bipartition sizes
\[
m=3+2t.
\]
Applying (3) gives connected simple bridgeless cubic graphs with
\[
\boxed{|V(G(H_t))|=30+20t,\qquad \omega(G(H_t))=4+2t,}
\]
every one of whose 2-factors consists entirely of odd cycles.

## Scope and literature caveat

These constructions refute precisely the **bridgeless cubic** formulation supplied in the question. Each Petersen gadget is separated from the rest by a cyclic 3-edge cut, so they do **not** address a version requiring cyclically 4-edge-connected graphs.

I have not verified the original entry’s surrounding conventions or established whether this construction is already recorded in the literature. The mathematical counterexample to the displayed statement, however, is explicit and complete.