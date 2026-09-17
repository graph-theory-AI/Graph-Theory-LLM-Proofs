```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For flow-admissible bidirected graphs whose underlying graph is a simple cactus, I prove a sharp 5-flow bound, improving to a sharp 4-flow bound when bridgeless.",
  "would_publish": false,
  "caveats": "Only the cactus case is covered; no claim of novelty or resolution of the general conjecture is made."
}
```

# Partial result: sharp bounds for bidirected cacti

I do not obtain a proof or counterexample for Bouchet’s conjecture in general. The following is a self-contained special-case result. It also gives an exact flow-admissibility criterion and a linear-time construction for this class.

Throughout this writeup, graphs are finite and simple. A **cactus** is a connected graph in which every edge belongs to at most one cycle. Disconnected graphs whose components are cacti can be treated componentwise.

## 1. Statement

Write the bidirected incidence coefficient as
\[
\eta(v,e)=
\begin{cases}
+1,&\text{the end of }e\text{ points into }v,\\
-1,&\text{the end of }e\text{ points out of }v.
\end{cases}
\]
Thus an integer flow satisfies
\[
\sum_{e\ni v}\eta(v,e)f(e)=0
\qquad\text{for every }v.
\]

Call an edge **positive** when its two incidence coefficients are opposite, and **negative** when they are equal. A cycle is **balanced** if it contains an even number of negative edges, and **unbalanced** otherwise.

**Theorem.** Let \(G\) be a bidirected cactus, and let \(\mathcal U\) be its set of unbalanced cycles.

1. \(G\) is flow-admissible if and only if either:
   - \(\mathcal U=\varnothing\) and \(G\) has no bridges; or
   - \(|\mathcal U|\ge 2\), and each component of \(G-e\) contains an unbalanced cycle for every bridge \(e\).

2. Whenever \(G\) is flow-admissible, it has a nowhere-zero integer flow satisfying
   \[
   |f(e)|\le 3\quad\text{on cycle edges},
   \qquad
   |f(e)|\in\{2,4\}\quad\text{on bridges}.
   \]
   Consequently, \(G\) has a nowhere-zero \(5\)-flow, and if it is bridgeless it has a nowhere-zero \(4\)-flow.

3. Both bounds are sharp within this class.

The admissibility test and flow construction can be implemented in \(O(|V(G)|+|E(G)|)\) time.

## 2. Switching and necessary conditions

**Switching** a vertex means reversing all arrowheads at that vertex. This multiplies its flow equation by \(-1\), so it preserves the flow vectors. Reversing both arrowheads of an edge can be compensated by negating its flow value. Both operations preserve flow magnitudes.

There is a particularly useful normal form for cacti. Choose one edge \(h_C\) from each cycle \(C\). Deleting these chosen edges leaves a spanning tree. Switch vertices so that every spanning-tree edge is positive. Then:

- every bridge is positive;
- every balanced cycle is entirely positive;
- every unbalanced cycle has precisely one negative edge, namely its chosen edge \(h_C\).

In particular, the unique negative edge of each unbalanced cycle can be placed at any chosen location on that cycle.

### Bridges require unbalanced cycles on both sides

Suppose \(e\) is a bridge and one component \(H\) of \(G-e\) contains no unbalanced cycle. Switch within \(H\) so that all its internal edges are positive. Summing the flow equations over \(V(H)\), the internal contributions cancel, leaving
\[
\pm f(e)=0.
\]
Thus \(G\) cannot have a nowhere-zero flow.

### Exactly one unbalanced cycle is impossible

If \(|\mathcal U|=1\), the normal form has exactly one negative edge \(h\). Summing all vertex equations gives
\[
\pm 2f(h)=0,
\]
again contradicting nowhere-zeroness.

These prove the necessity in part 1.

If there are no unbalanced cycles and no bridges, normalize every cycle to be positive and give each cycle a unit circulation. Cycles are edge-disjoint, and each circulation has zero contribution at every vertex, including shared vertices. This gives a nowhere-zero \(2\)-flow.

It remains to handle \(|\mathcal U|\ge2\).

## 3. A bounded realization lemma for a cycle

For a cycle \(C\), define its contribution at a vertex \(v\in V(C)\) by
\[
p_C(v)=\sum_{\substack{e\in E(C)\\e\ni v}}\eta(v,e)f(e).
\]
This need not be zero: contributions from other cycles or bridges may cancel it.

Let
\[
D=\{-4,-2,2,4\}.
\]

**Cycle lemma.** Designate \(r\) distinct vertices of a cycle as ports, in cyclic order, with a distinguished first port. Suppose either:

- the cycle is balanced and \(r\ge2\); or
- the cycle is unbalanced and \(r\ge1\).

For any prescribed contribution \(p_1\in D\) at the first port, one can assign nonzero integer values of magnitude at most \(3\) to all cycle edges so that:

- every other port also has contribution in \(D\);
- every nonport vertex has contribution zero.

For the proof, use the normal form above. In the unbalanced case, place the negative edge immediately before the first port.

### Proof

Orient the positive edges forward around the cycle. In the unbalanced case, orient the negative edge with both ends pointing inward.

The required assignment can be described by a sequence of nonzero states
\[
x_0,x_1,\ldots,x_r
\]
such that
\[
p_i=x_{i-1}-x_i,
\]
with the closing condition
\[
x_r=x_0 \quad\text{for a balanced cycle},
\qquad
x_r=-x_0 \quad\text{for an unbalanced cycle}.
\]

Indeed, values are constant along each positive path between consecutive ports. The negative closing edge, when present, has value \(x_0\), and the final positive segment has value \(x_r=-x_0\). These assignments give zero contribution at every nonport. All actual edge values are among the states, up to sign.

It therefore suffices to keep every state in
\[
\{-3,-2,-1,1,2,3\}
\]
and every consecutive difference in \(D\).

For positive prescribed \(p_1\), the following sequences handle the smallest port counts of each parity:

| Cycle type | Port-count parity | \(p_1=2\) | \(p_1=4\) |
|---|---:|---|---|
| Balanced | even, starting at \(r=2\) | \((1,-1,1)\) | \((2,-2,2)\) |
| Balanced | odd, starting at \(r=3\) | \((1,-1,-3,1)\) | \((1,-3,-1,1)\) |
| Unbalanced | odd, starting at \(r=1\) | \((1,-1)\) | \((2,-2)\) |
| Unbalanced | even, starting at \(r=2\) | \((3,1,-3)\) | \((3,-1,-3)\) |

Every listed consecutive difference belongs to \(D\), and the closing condition is correct.

To increase the port count by two, append a backtrack \(x,t,x\) at the endpoint. One may choose
\[
t=-x\quad\text{if }|x|\le2,
\qquad
t=x-2\operatorname{sgn}(x)\quad\text{if }|x|=3.
\]
Both added differences belong to \(D\), and the endpoint is unchanged. This handles every allowable \(r\).

For negative prescribed \(p_1\), negate the entire sequence. ∎

We also need a simple junction rule.

**Junction lemma.** If a vertex has \(r\ge2\) incident quantities, one of which is prescribed in \(D\), the others can be chosen in \(D\) so that their sum is zero.

**Proof.** Divide by two and, by negation if necessary, take the prescribed quantity to be \(a\in\{1,2\}\).

- If \(r\) is even, use \(a,-a\), followed by cancelling pairs \(1,-1\).
- If \(r\) is odd, start with
  \[
  (1,1,-2)\quad\text{if }a=1,
  \qquad
  (2,-1,-1)\quad\text{if }a=2,
  \]
  and append cancelling pairs.

Multiply by two. ∎

## 4. Assembly along a tree

Assume now that \(|\mathcal U|\ge2\) and every bridge has an unbalanced cycle on each side.

### The auxiliary tree

Construct a graph \(T\) as follows:

- retain every original vertex;
- replace each cycle \(C\) by a new node \(c_C\), joined to every original vertex of \(C\);
- retain every original bridge.

Then \(T\) is a tree. For example, if \(G\) has \(n\) vertices, \(m\) edges, and \(c\) cycles, then
\[
m=n-1+c,
\]
while \(T\) is connected with \(n+c\) vertices and \(m\) edges.

Let \(S\) be the minimal subtree of \(T\) containing all nodes \(c_C\) for \(C\in\mathcal U\). Then:

1. every leaf of \(S\) is an unbalanced-cycle node;
2. every original-vertex node in \(S\) has degree at least two;
3. every balanced-cycle node in \(S\) has degree at least two;
4. every original bridge belongs to \(S\);
5. every cycle whose node lies outside \(S\) is balanced.

For item 4, deleting an original bridge splits the marked unbalanced-cycle nodes into two nonempty sets, so that bridge lies on a path between two marked nodes.

An edge \(c_Cv\) of \(S\) is only a bookkeeping device: it represents the contribution of cycle \(C\) at \(v\). It is not an original edge whose flow value needs to satisfy the final bound.

### Rooting and normalization

Root \(S\) at any unbalanced-cycle node.

For each nonroot cycle node, designate its attachment to its parent as its first port. For the root cycle, choose any port as first. Ports are precisely the vertices \(v\) for which \(c_Cv\in E(S)\).

Use the spanning-tree normalization from Section 2, placing each unbalanced cycle’s negative edge immediately before its first port. Thus all bridges are positive, and the cycle lemma applies in its stated normal form.

### Top-down construction

Process \(S\) from the root.

- **At the root cycle:** prescribe contribution \(2\) at its first port and apply the cycle lemma. This determines a contribution in \(D\) at every other port.

- **At a nonroot cycle:** its parent has already prescribed its contribution at the parent port. Apply the cycle lemma to determine all remaining port contributions.

- **At an original vertex \(v\):** the parent has already determined one contribution in \(D\) to the equation at \(v\). Apply the junction lemma to choose contributions in \(D\) for all child edges, with total sum zero.
  - If a child edge is an original bridge, choose its flow value to give the selected contribution at \(v\). Its contribution at the other endpoint is the opposite number, because the bridge is positive.
  - If the child is a cycle node \(c_C\), prescribe the selected number as \(p_C(v)\).

This never gets stuck:

- original-vertex nodes have degree at least two;
- balanced-cycle nodes have at least two ports;
- an unbalanced-cycle leaf can realize any prescribed single-port contribution in \(D\).

Because \(S\) is a tree, each node has at most one previously prescribed incident quantity. Thus there are no conflicting prescriptions.

Give every cycle outside \(S\) a unit circulation. Such cycles are balanced.

### Verification

Every original edge is now assigned:

- a cycle edge receives a nonzero value of magnitude at most \(3\);
- a bridge receives a value of magnitude \(2\) or \(4\).

At each original vertex in \(S\), the contributions sum to zero by the junction rule. At an original vertex outside \(S\), every incident cycle has contribution zero there, and there is no incident original bridge. Unit circulations outside \(S\) contribute zero everywhere.

Hence the assignment is a nowhere-zero integer flow. Undoing switching and edge reversals preserves its magnitudes.

This proves sufficiency and the claimed bounds.

All steps are linear-time: discover the cycles, build \(T\), obtain \(S\) by pruning unmarked leaves, and perform one rooted traversal using the two local lemmas. No initial flow is required.

## 5. Sharpness

### A cactus requiring a \(5\)-flow

Take three vertex-disjoint triangles \(C_1,C_2,C_3\), choose a vertex \(v_i\) in each, and add a new vertex \(z\) and bridges
\[
zv_1,\ zv_2,\ zv_3.
\]
Make each triangle unbalanced and all bridges positive.

This graph satisfies the admissibility criterion, so it has a nowhere-zero \(5\)-flow.

In every integer flow, the value on each bridge is even. More generally, this holds for every bridge in any bidirected graph: summing the vertex equations on one side of the bridge leaves its value plus an even sum from internal negative edges.

If a nowhere-zero \(4\)-flow existed, each of the three bridges would therefore have magnitude \(2\). But the equation at \(z\) would require three numbers from \(\{-2,2\}\) to sum to zero, which is impossible.

Thus the \(5\)-flow bound is sharp.

### A bridgeless cactus requiring a \(4\)-flow

Take a middle triangle with distinct vertices \(u,v,w\). Attach one triangle at \(u\) and another at \(v\), using otherwise disjoint vertices. Make all three triangles unbalanced.

This graph is bridgeless and satisfies the admissibility criterion, so it has a nowhere-zero \(4\)-flow.

Suppose it had a nowhere-zero \(3\)-flow. Normalize the middle triangle so that \(uw\) is negative and \(uv,vw\) are positive. With suitable orientations, write the middle-triangle edge values as
\[
f(uw)=x,\qquad f(uv)=y,\qquad f(vw)=-x,
\]
where the last equality follows from the equation at \(w\). Its contributions at \(u,v\) are then
\[
x-y,\qquad x+y.
\]

Each attached unbalanced triangle has only one attachment vertex. Its contribution there is twice a nonzero integer. Consequently,
\[
x-y\quad\text{and}\quad x+y
\]
must both be nonzero even integers.

But a \(3\)-flow requires
\[
x,y\in\{-2,-1,1,2\}.
\]
The evenness conditions force \(x,y\) to have the same parity. Within this set, that implies \(|x|=|y|\), so one of \(x-y,x+y\) is zero—a contradiction.

Thus the bridgeless bound \(4\) is sharp.

## 6. What remains unresolved

The essential feature is the tree structure: when a cycle is processed, only one port contribution has already been prescribed, and the cycle lemma can extend that prescription.

For a general signed graph, a block can contain overlapping cycles. The construction above provides no bounded realization theorem for such a block and no way to reconcile the multiple constraints that overlapping cycles can impose.

Therefore this argument verifies Bouchet’s conjecture, with stronger bounds, for cactus underlying graphs only. It neither proves the general \(6\)-flow conjecture nor produces a counterexample. No external literature claims or novelty claims are used.