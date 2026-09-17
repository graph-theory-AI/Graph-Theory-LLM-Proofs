```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for at most 2k+3 odd-degree nonterminals, and for at most 4k+1 if the nonterminals are independent.",
  "would_publish": false,
  "caveats": "The full conjecture is unresolved here; novelty and the latest literature have not been checked."
}
```

# Two parity-sensitive special cases

I checked and retain the splitting-off reduction from the previous attempt. The new ingredient is a branching-aware augmentation argument: a shortage of one in the auxiliary hypergraph’s spanning-tree partition inequalities can always be repaired. When the nonterminals are independent, this augmentation can be repeated more substantially.

All graphs below are finite and undirected. Parallel edges are allowed, and loops are discarded. We work in the nontrivial setting \(k\ge 1\) and \(|T|\ge 2\).

Write
\[
q(G,T)=|\{v\in V(G)\setminus T:\deg_G(v)\text{ is odd}\}|.
\]
A **\(T\)-cut** is an edge cut with terminals on both sides. By edge-Menger, the hypothesis of Kriesell’s conjecture is equivalent to every \(T\)-cut having size at least \(2k\).

## 1. Results

**Theorem A.** Suppose every \(T\)-cut of \(G\) has size at least \(\lambda\), where
\[
\lambda\ge 2k,
\qquad
q(G,T)\le 2\lambda-2k+3.
\]
Then \(G\) contains \(k\) edge-disjoint trees containing \(T\).

Equivalently, the sufficient cut bound is
\[
\boxed{\max\left\{2k,\ k+\left\lfloor\frac{q(G,T)}2\right\rfloor-1\right\}.}
\]
In particular, the original \(2k\)-cut hypothesis suffices whenever
\[
\boxed{q(G,T)\le 2k+3.}
\]

This improves the previous attempt’s proposed cutoff \(2k+1\) by two.

**Theorem B.** Suppose \(V(G)\setminus T\) is independent and every \(T\)-cut has size at least \(2k\). If
\[
\boxed{q(G,T)\le 4k+1,}
\]
then \(G\) contains \(k\) edge-disjoint trees containing \(T\).

The proof of Theorem B also establishes the case in which \(V(G)\setminus T\) is independent and \(|T|\le 6\), without a restriction on \(q(G,T)\).

These are partial results only. I do not claim novelty or an improvement to the general constant-factor bounds quoted in the question.

---

## 2. Verified reduction and its counting inequality

### 2.1 Reduction to cubic nonterminals

We use the following standard form of Mader’s local splitting-off theorem:

> If a vertex \(v\) has degree at least two, has degree different from three, and is incident with no bridge, then two edges at \(v\) can be split off without decreasing the local edge-connectivity between any two vertices other than \(v\).

Splitting \(vx,vy\) means deleting these two edges and adding \(xy\). The new edge remains individually labelled.

**Reduction lemma.** If every \(T\)-cut of \(G\) has size at least \(\lambda\ge2\), then there is a connected loopless multigraph \(H\), with the same terminal set, such that:

1. every \(T\)-cut of \(H\) has size at least \(\lambda\);
2. every nonterminal of \(H\) is cubic;
3. \(|V(H)\setminus T|\le q(G,T)\);
4. every packing of \(T\)-trees in \(H\) lifts to a packing of the same size in \(G\).

If \(V(G)\setminus T\) is independent, then \(V(H)\setminus T\) is also independent.

**Proof.** First retain only the connected component containing \(T\).

There is a useful pruning operation. Delete all bridges, and let \(B\) be the resulting component containing \(T\). All terminals lie in \(B\), since a bridge cannot separate terminals. Every component \(D\) of the original graph outside \(B\) is attached to \(B\) by exactly one bridge.

Pruning to \(B\) preserves terminal connectivity: a simple path between terminals cannot enter such a component \(D\).

It also cannot increase the number of odd nonterminals. Indeed,
\[
\sum_{v\in D}\deg(v)=2|E(D)|+1,
\]
so each deleted component contains an odd-degree vertex, necessarily a nonterminal. If there are \(b\) deleted components, they remove at least \(b\) odd nonterminals. Deleting their attachment edges can create at most \(b\) new odd nonterminals inside \(B\).

Now repeatedly:

* retain the terminal-containing component and prune its bridges;
* split off an admissible pair at a nonterminal of degree different from three;
* discard loops and isolated vertices.

After pruning, the connected graph is bridgeless and has at least two vertices, so every vertex has degree at least two. Thus Mader’s theorem applies whenever a nonterminal is not cubic.

Splitting preserves all degree parities; discarding a loop changes a degree by two. The pruning argument shows that the odd-nonterminal count never increases. Each splitting decreases the edge count, so eventually all remaining nonterminals are cubic. Their number is at most \(q(G,T)\).

For lifting, track each retained edge by its set of original predecessor edges. These sets remain pairwise edge-disjoint. Reversing splittings expands a connected subgraph into a connected subgraph, possibly with cycles. Expand each packed tree, and then take a spanning tree of each expansion.

Finally, if the nonterminals are independent, every split at a nonterminal adds an edge between terminals. Independence is therefore preserved. ∎

### 2.2 The component hypergraph

For a connected graph \(H\) containing \(T\), form a labelled hypergraph \(\mathcal H\) on \(T\):

* every edge of \(H[T]\) gives a two-element hyperedge;
* every component \(C\) of \(H-T\) with at least two distinct terminal neighbors gives one hyperedge
  \[
  e_C=N_T(C).
  \]

A selected pair from \(e_C\) can be realized by a path with internal vertices in \(C\). Different component-hyperedges have disjoint edge resources.

There is also a second permissible use of \(e_C\): reserve the entire component for one tree, allowing it to connect all vertices of \(N_T(C)\). This is the branching operation absent from the previous attempt.

For a partition \(\mathcal P\) of \(T\), let \(d_{\mathcal H}(\mathcal P)\) count hyperedges meeting at least two parts.

Suppose now that \(H\) is the cubic reduction, with at most \(q=q(G,T)\) nonterminals. For a component \(C\) of \(H-T\), put
\[
n_C=|V(C)|,\quad m_C=|E(C)|,\quad b_C=|\delta_H(C)|.
\]
Then
\[
b_C=3n_C-2m_C\le n_C+2.                 \tag{1}
\]

Fix a partition \(\mathcal P=\{P_1,\ldots,P_r\}\), \(r\ge2\). Let \(a\) count crossing terminal-terminal edges, and let \(\mathcal C_\times\) be the components whose terminal neighborhoods cross \(\mathcal P\).

For each \(i\), take \(P_i\) together with all components whose terminal neighborhoods are contained in \(P_i\). This is one side of a \(T\)-cut. Summing these cut inequalities gives
\[
\lambda r
\le 2a+\sum_{C\in\mathcal C_\times}b_C.
\]
Consequently,
\[
\begin{aligned}
\lambda r
&\le
2\bigl(a+|\mathcal C_\times|\bigr)
+\sum_{C\in\mathcal C_\times}(b_C-2)\\
&\le 2d_{\mathcal H}(\mathcal P)+q.
\end{aligned}
\]
Thus
\[
\boxed{
d_{\mathcal H}(\mathcal P)\ge
\left\lceil\frac{\lambda r-q}{2}\right\rceil.
}                                                        \tag{2}
\]

The previous attempt required this to reach \(k(r-1)\). We will repair a deficit of one.

---

## 3. A branching-aware hypergraph packing lemma

Here is the precise min–max tool needed.

**Packing lemma.** Let \(\mathcal H=(X,\mathcal E)\) be a finite labelled hypergraph, every hyperedge having size at least two. Distinguish \(m\le k\) hyperedges
\[
e_1,\ldots,e_m.
\]
For a partition \(\mathcal P\), let \(t_i(\mathcal P)\) be the number of its parts met by \(e_i\).

Suppose every partition satisfies
\[
d_{\mathcal H-\{e_1,\ldots,e_m\}}(\mathcal P)
+\sum_{i=1}^m\bigl(t_i(\mathcal P)-1\bigr)
\ge k(|\mathcal P|-1).                                  \tag{3}
\]

Then one can obtain \(k\) spanning trees on \(X\) in a labelled auxiliary multigraph so that:

* distinguished hyperedge \(e_i\) supplies a tree on all its vertices to tree \(i\);
* every other hyperedge supplies at most one selected pair, used at most once across the packing.

In a component hypergraph, these trees expand to edge-disjoint \(T\)-trees in the original graph.

### Proof

Put \(n=|X|\), \(s_i=|e_i|\), and choose a fixed virtual tree \(F_i\) on \(e_i\). All virtual edges receive fresh labels.

From each nondistinguished hyperedge, create all candidate pairs of its vertices, retaining its label. Let \(\Omega\) be the resulting candidate-edge set.

For \(i\le m\), take the graphic matroid contracted by \(F_i\), restricted to \(\Omega\). For the other \(k-m\) indices, take the ordinary graphic matroid on \(\Omega\). Let \(M\) be their matroid union. Let \(N\) be the partition matroid permitting at most one candidate with each nondistinguished hyperedge label.

We seek a common independent set of size
\[
D=k(n-1)-\sum_{i=1}^m(s_i-1).
\]

For \(B\subseteq\Omega\), let \(\mathcal P_B\) be its component partition. Adding \(F_i\) merges exactly \(t_i(\mathcal P_B)\) of those components. The sum of the \(k\) relevant graphic ranks on \(B\) is therefore
\[
k(n-|\mathcal P_B|)
+\sum_{i=1}^m\bigl(t_i(\mathcal P_B)-s_i\bigr).
\]
The matroid-union rank formula implies, for \(A\subseteq\Omega\),
\[
r_M(A)\ge
\min_{\mathcal P}
\left[
k(n-|\mathcal P|)
+\sum_i(t_i(\mathcal P)-s_i)
+|A\cap\delta(\mathcal P)|
\right],                                                \tag{4}
\]
where \(\delta(\mathcal P)\) is the set of candidate edges crossing the partition.

Every nondistinguished hyperedge crossing \(\mathcal P\) either has a candidate outside \(A\), or has a crossing candidate inside \(A\). Hence
\[
|A\cap\delta(\mathcal P)|+r_N(\Omega\setminus A)
\ge d_{\mathcal H-\{e_1,\ldots,e_m\}}(\mathcal P).
\]
Combining this with (3) and (4) yields
\[
r_M(A)+r_N(\Omega\setminus A)\ge D
\qquad(A\subseteq\Omega).
\]
The matroid-intersection theorem supplies a common independent set of size \(D\).

Decompose it according to the union matroid. In color \(i\le m\), append \(F_i\). Each resulting graph is a forest. The total edge count forces every one of the \(k\) forests to have \(n-1\) edges, so all are spanning trees.

For a component hypergraph, realize each ordinary selected pair by a path inside its component. For a distinguished component, realize its whole virtual tree within that component, assigning all of it to its designated color. Paths within that one color may overlap, which is harmless: their union is connected. Different colors have disjoint edge resources. Taking spanning trees of the expansions completes the lifting. ∎

The case \(m=0\) is the ordinary hypergraphic spanning-tree packing lemma used in the previous attempt.

---

## 4. Partition submodularity

We need a small fact about the lattice of partitions.

Write \(\mathcal P\wedge\mathcal Q\) for the common refinement and \(\mathcal P\vee\mathcal Q\) for the least common coarsening. A function \(f\) on partitions is submodular if
\[
f(\mathcal P)+f(\mathcal Q)
\ge
f(\mathcal P\wedge\mathcal Q)+f(\mathcal P\vee\mathcal Q).
\]

Two relevant functions are submodular:

1. \(d_{\mathcal H}(\mathcal P)\);
2. \(\rho(\mathcal P)=|X|-|\mathcal P|\).

For the first, check each hyperedge’s crossing indicator separately. If it crosses both partitions, it crosses their meet; if it is contained in a part of either partition, it is contained in a part of their join. These observations give the inequality in every case.

For the second,
\[
|\mathcal P|+|\mathcal Q|
\le |\mathcal P\wedge\mathcal Q|+|\mathcal P\vee\mathcal Q|.
\]
One proof uses the bipartite incidence graph between the parts of \(\mathcal P\) and \(\mathcal Q\): its edges are the nonempty intersections and its components correspond to the join.

Also, for a fixed partition \(\mathcal R\),
\[
\mathcal P\longmapsto \rho(\mathcal P\vee\mathcal R)
\]
is submodular. This follows by applying submodularity of \(\rho\) to \(\mathcal P\vee\mathcal R,\mathcal Q\vee\mathcal R\), and using
\[
(\mathcal P\wedge\mathcal Q)\vee\mathcal R
\preceq
(\mathcal P\vee\mathcal R)\wedge(\mathcal Q\vee\mathcal R).
\]

Finally, the minimizing partitions of a submodular function are closed under meet and join. Thus there is a **coarsest minimizing partition**, and every minimizing partition refines it.

---

## 5. Repairing a one-unit deficit

The following is the main augmentation lemma. It does not require cubic nonterminals.

**One-defect lemma.** Let \(H\) be connected, with every \(T\)-cut of size at least \(2k\), and let \(\mathcal H\) be its component hypergraph. Suppose
\[
d_{\mathcal H}(\mathcal P)\ge k(|\mathcal P|-1)-1
\quad\text{for every partition }\mathcal P.               \tag{5}
\]
Then \(H\) contains \(k\) edge-disjoint \(T\)-trees.

### Proof

Define
\[
f(\mathcal P)=d_{\mathcal H}(\mathcal P)-k(|\mathcal P|-1).
\]
This is integer-valued and submodular.

If \(f\ge0\), the packing lemma with no distinguished hyperedges applies. Otherwise its minimum is \(-1\). Let \(\mathcal P_*\) be its coarsest minimizing partition.

There are two cases.

### Case 1: Some component meets at least three parts of \(\mathcal P_*\)

Let \(e_C=N_T(C)\) be such a hyperedge. Every partition with \(f=-1\) refines \(\mathcal P_*\), so \(e_C\) meets at least three parts of every such partition.

Reserve \(e_C\) for tree 1. Its contribution to the left side of (3), compared with its former one-pair contribution, increases by
\[
\max\{t_C(\mathcal P)-2,0\}.
\]
This is nonnegative everywhere and is at least one on every deficient partition. Therefore (3) holds, and the packing lemma applies.

### Case 2: Every component meets at most two parts of \(\mathcal P_*\)

Write \(r=|\mathcal P_*|\). Let \(a\) count crossing terminal-terminal edges and \(c\) count crossing component-hyperedges. Thus
\[
a+c=k(r-1)-1.
\]

For a crossing component \(C\), its terminal neighbors lie in two parts, say \(A_C,B_C\). Let \(\mu_C\) be the maximum number of edge-disjoint \(A_C\)-to-\(B_C\) paths whose internal vertices lie in \(C\).

By edge-Menger, \(\mu_C\) is the minimum contribution of \(C\) to a cut placing its neighbors in \(A_C\) on one side and those in \(B_C\) on the other. Optimizing each component separately for each part of \(\mathcal P_*\), and summing the resulting \(r\) terminal cuts, gives
\[
2kr\le 2a+2\sum_C\mu_C.                                 \tag{6}
\]
Each crossing component contributes \(\mu_C\) for each of its two incident parts.

Since \(a+c=k(r-1)-1<kr\), some component \(C\) has \(\mu_C\ge2\). Choose two edge-disjoint paths in it, with endpoint pairs
\[
p_1=x_1y_1,\qquad p_2=x_2y_2,
\]
both crossing the same two parts \(A,B\) of \(\mathcal P_*\).

Replace the single hyperedge \(e_C\) by these two labelled pairs, obtaining \(\mathcal H'\). I claim
\[
d_{\mathcal H'}(\mathcal Q)\ge k(|\mathcal Q|-1)
\quad\text{for every }\mathcal Q.                         \tag{7}
\]

* If \(f(\mathcal Q)=-1\), then \(\mathcal Q\) refines \(\mathcal P_*\). Both new pairs cross \(\mathcal Q\), so its crossing count increases by one.
* If \(f(\mathcal Q)\ge1\), replacing one hyperedge can decrease its crossing count by at most one.
* It remains to consider \(f(\mathcal Q)=0\).

Suppose this last type of partition loses one crossing hyperedge. Then \(e_C\) crosses \(\mathcal Q\), but both new pairs are internal to its parts.

Set
\[
\mathcal R=\mathcal P_*\vee\mathcal Q,
\qquad
\mathcal M=\mathcal P_*\wedge\mathcal Q.
\]
Because a new pair joins \(A\) to \(B\) while lying within a part of \(\mathcal Q\), the join \(\mathcal R\) merges \(A,B\). It is strictly coarser than \(\mathcal P_*\), and \(e_C\) is internal to \(\mathcal R\).

Thus the crossing indicator of \(e_C\) contributes exactly one to the submodularity slack:
\[
1+1-1-0=1.
\]
All other hyperedge indicators and the partition-rank term have nonnegative slack. Consequently,
\[
f(\mathcal P_*)+f(\mathcal Q)
\ge f(\mathcal M)+f(\mathcal R)+1.
\]
But
\[
f(\mathcal P_*)=-1,\quad f(\mathcal Q)=0,\quad
f(\mathcal M)\ge-1,\quad f(\mathcal R)\ge0.
\]
The last inequality follows because \(\mathcal P_*\) is the coarsest minimizer. This would give \(-1\ge0\), a contradiction.

Therefore (7) holds. Apply the packing lemma without distinguished hyperedges. Realize the two replacement pairs by their chosen edge-disjoint paths, and every other component label by at most one path. The resulting \(T\)-trees are edge-disjoint. ∎

### Deduction of Theorem A

Apply the cubic reduction and inequality (2). For a partition with \(r\ge2\),
\[
\begin{aligned}
2d_{\mathcal H}(\mathcal P)-2k(r-1)
&\ge \lambda r-q-2k(r-1)\\
&=(\lambda-2k)(r-2)+(2\lambda-2k-q)\\
&\ge -3.
\end{aligned}
\]
The left side is even, so it is at least \(-2\). Hence
\[
d_{\mathcal H}(\mathcal P)\ge k(r-1)-1.
\]
The one-part partition causes no difficulty. The one-defect lemma gives the packing in \(H\), and the reduction lifts it to \(G\). This proves Theorem A. ∎

---

## 6. Independent nonterminals: repeated branching augmentation

Assume now that \(V(G)\setminus T\) is independent. The reduction preserves this property, so every nonterminal of \(H\) is an isolated cubic vertex in \(H-T\). The auxiliary hypergraph consequently has rank at most three.

For any terminal bipartition, a cubic nonterminal contributes either zero or one to a minimum extension cut. This remains true with parallel edges and repeated terminal neighbors. Therefore every bipartition cut of \(\mathcal H\) has size at least \(2k\).

For a partition \(\mathcal P\), let \(c(\mathcal P)\) count its hyperedges meeting three parts. Summing the hypergraph bipartition cuts associated with the individual parts gives, for \(r=|\mathcal P|\ge2\),
\[
2d_{\mathcal H}(\mathcal P)+c(\mathcal P)\ge2kr.           \tag{8}
\]

Put
\[
f_0(\mathcal P)=d_{\mathcal H}(\mathcal P)-k(r-1).
\]
By (2), for nontrivial partitions,
\[
f_0(\mathcal P)\ge k-\left\lfloor\frac q2\right\rfloor.
\]
Thus \(q\le4k+1\) implies
\[
\min_{\mathcal P}f_0(\mathcal P)\ge-k.                    \tag{9}
\]

We will reserve at most one full cubic star for each tree.

### 6.1 The partition function after reserving stars

Suppose \(m\le k\) distinct three-element hyperedges have been reserved, each for a different tree. Let \(b_m(\mathcal P)\) count the reserved hyperedges meeting three parts, and define
\[
f_m(\mathcal P)
=d_{\mathcal H}(\mathcal P)-k(r-1)+b_m(\mathcal P).        \tag{10}
\]
This is precisely the left side of packing condition (3), minus its right side.

The function \(f_m\) is submodular. To see this explicitly, let \(\mathcal R_i\) be the partition with the reserved triple \(e_i\) as one block and all other vertices singleton. Then
\[
t_i(\mathcal P)-1
=|\mathcal P|-|\mathcal P\vee\mathcal R_i|.
\]
Consequently,
\[
f_m(\mathcal P)
=
d_{\mathcal H-\{e_1,\ldots,e_m\}}(\mathcal P)
+(k-m)\rho(\mathcal P)
+\sum_{i=1}^m\rho(\mathcal P\vee\mathcal R_i)
-k(|T|-1).
\]
Every nonconstant term is submodular, and \(k-m\ge0\).

### 6.2 One more reserved star raises the minimum

Suppose \(f_m\) has negative minimum, and let \(\mathcal P_*\) be its coarsest minimizing partition. Its number of parts is at least two.

Let \(c_{\mathrm{un}}\) count the unreserved hyperedges meeting three parts of \(\mathcal P_*\), and put \(b=b_m(\mathcal P_*)\). From (8) and (10),
\[
c_{\mathrm{un}}
\ge 2k-2f_m(\mathcal P_*)+b>0.
\]
Thus there is an unreserved triple \(e\) meeting three parts of \(\mathcal P_*\).

Reserve it for a new tree. Then
\[
f_{m+1}(\mathcal P)
=
f_m(\mathcal P)
+\mathbf 1_{\{e\text{ meets three parts of }\mathcal P\}}.
\]
Every minimizing partition of \(f_m\) refines \(\mathcal P_*\), so every minimizer increases by one. Every nonminimizer was already at least one above the minimum, and no value decreases. Therefore
\[
\min f_{m+1}\ge \min f_m+1.                              \tag{11}
\]

By (9), at most \(k\) repetitions are needed. At termination, \(m\le k\) and \(f_m\ge0\), exactly condition (3). The packing lemma applies, and its expansion and the splitting-off lifting prove Theorem B. ∎

### An additional small-terminal consequence

The same proof only needs \(\min f_0\ge-k\), not the odd-degree bound itself.

Since \(c(\mathcal P)\le d_{\mathcal H}(\mathcal P)\), equation (8) gives
\[
f_0(\mathcal P)
\ge \frac{2kr}{3}-k(r-1)
=k\left(1-\frac r3\right).
\]
If \(|T|\le6\), this is at least \(-k\). Hence the conjecture also follows when the nonterminals are independent and \(|T|\le6\), without a bound on their number.

---

## 7. What remains outside the argument

The unrestricted conjecture does not follow. The general argument repairs only one unit of partition deficiency. The independent-nonterminal argument allows at most one fully used cubic star per tree.

That latter restriction genuinely limits the method. Here is a fully specified example.

Take \(k=3\), terminal set \(T=\{1,\ldots,7\}\), and the seven triples
\[
123,\quad145,\quad167,\quad246,\quad257,\quad347,\quad356.
\]
For each triple, add two nonterminals adjacent precisely to its three terminals. These are the two copies of each line of the Fano plane.

There are \(14=4k+2\) odd nonterminals. For terminal bipartitions whose smaller side has size \(1,2,3\), the minimum graph cuts have sizes respectively
\[
6,\quad10,\quad12.
\]
Thus the original \(2k=6\) hypothesis holds.

The auxiliary hypergraph has only fourteen labels. Three virtual spanning trees on seven terminals require eighteen edges. If each tree is allowed at most one full triple, the total supply is at most
\[
14+3=17.
\]
So the packing model used in Theorem B cannot certify this instance.

Nevertheless, the graph has three edge-disjoint \(T\)-trees. Use the three pencils of lines through terminals \(1,2,4\), respectively, assigning different copies whenever a line occurs in two pencils. Each pencil consists of three stars meeting only at its central terminal and covers all seven terminals; its union is a tree. Since \(1,2,4\) are noncollinear, no line is needed more than twice.

Thus the remaining obstacle is not a counterexample, but the need to handle several branching resources in the same tree—and, for general nonterminal components, several interacting internal linkages. The proofs above do not control those possibilities in general.