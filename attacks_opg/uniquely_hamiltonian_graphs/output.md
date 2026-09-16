```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A parity argument settles the case where the complementary 2-factor has at most two components and gives a local matching criterion whose limitations can be demonstrated explicitly.",
  "would_publish": false,
  "caveats": "The unrestricted 4-regular case remains unresolved; these classical-parity consequences are not claimed to be novel."
}
```

## 1. Scope of the result

Throughout, graphs are finite, simple, and undirected. Hamiltonian cycles are counted without distinguishing their starting points or orientations.

I do **not** resolve Sheehan’s conjecture. I prove the following special case.

**Proposition.** Let \(G\) be a \(4\)-regular graph with a Hamiltonian cycle \(C\), and put
\[
F=G-E(C).
\]
If the \(2\)-factor \(F\) has at most two components, then \(G\) has a Hamiltonian cycle different from \(C\).

The proof gives stronger sufficient conditions involving matchings on consecutive vertices of \(C\). I also exhibit a \(12\)-vertex pair \((G,C)\) for which this matching criterion fails everywhere, despite \(G\) having another Hamiltonian cycle. In fact, \(12\) is the smallest order at which this particular certificate can fail for a Hamiltonian \(4\)-regular graph.

The latter is a bound on the **certificate**, not a proposed best-known bound for Sheehan’s conjecture.

## 2. A self-contained rotation-parity lemma

**Lemma.** Let \(H\) be a simple graph on at least three vertices, and let \(s\ne t\). Suppose that \(t\) has even degree and every vertex outside \(\{s,t\}\) has odd degree. Then the number of Hamiltonian \(s\)-\(t\) paths in \(H\) is even.

No condition on \(d_H(s)\) is needed.

**Proof.** Form an auxiliary graph \(\mathcal R\) whose vertices are all oriented Hamiltonian paths of \(H\) starting at \(s\).

For a path
\[
P=(v_1=s,v_2,\ldots,v_m=z)
\]
and an edge \(zv_i\), where \(2\le i\le m-2\), join \(P\) to its rotation
\[
(v_1,\ldots,v_i,z,v_{m-1},\ldots,v_{i+1}).
\]
This operation is reversible, and different eligible neighbors of \(z\) give different rotations. Hence
\[
d_{\mathcal R}(P)
=d_H(z)-1-\mathbf 1_{\{sz\in E(H)\}}.
\]
The two excluded possibilities are the predecessor of \(z\) on \(P\) and the starting vertex \(s\).

Since \(z\ne s\), the degree hypotheses imply
\[
d_{\mathcal R}(P)
\equiv
\mathbf 1_{\{z=t\}}
+\mathbf 1_{\{sz\in E(H)\}}
\pmod 2.
\]
Summing over all vertices of \(\mathcal R\), the handshaking lemma gives
\[
0\equiv
N_{s,t}
+\sum_P\mathbf 1_{\{sz\in E(H)\}}
\pmod 2,
\]
where \(N_{s,t}\) is the number of Hamiltonian \(s\)-\(t\) paths.

The last sum is even: closing \(P\) with \(zs\) gives a Hamiltonian cycle of \(H\), and every such cycle produces exactly two oriented Hamiltonian paths starting at \(s\). Thus \(N_{s,t}\) is even. \(\square\)

For comparison, this immediately recovers the classical odd-degree case. If every vertex of \(G\) has odd degree and \(st\) lies on a Hamiltonian cycle, apply the lemma to \(H=G-st\). Hamiltonian \(s\)-\(t\) paths in \(H\) correspond bijectively to Hamiltonian cycles of \(G\) containing \(st\). There are therefore at least two.

## 3. A local off-cycle matching criterion

A *cyclic interval* of \(C\) is a nonempty set of consecutive vertices in its cyclic order. We allow the interval to be all of \(V(C)\).

**Theorem — interval-matching criterion.** Let \(C\) be a Hamiltonian cycle of a simple graph \(G\). Suppose some cyclic interval \(T\) of \(C\) has a perfect matching using only edges outside \(C\). Then \(G\) has a Hamiltonian cycle different from \(C\).

For a proper interval, the second cycle can retain the entire complementary arc of \(C\).

**Proof.** Let \(P\) be the path traversing the vertices of \(T\) in their order on \(C\), with endpoints \(s,t\). If \(T=V(C)\), choose \(P=C-st\), where \(st\) is any edge of \(C\).

Let \(M\) be the stipulated perfect matching, and consider the spanning graph on \(T\)
\[
H=(T,E(P)\cup M).
\]
Because \(M\cap E(C)=\varnothing\), the endpoints \(s,t\) have degree \(2\) in \(H\), while every internal vertex of \(P\) has degree \(3\).

The hypotheses force \(|T|\) to be even. Moreover, \(|T|=2\) is impossible, since the only possible matching edge would be an edge of \(C\). Thus \(|T|\ge4\), and the parity lemma applies.

Consequently, \(H\) has an even number of Hamiltonian \(s\)-\(t\) paths. One is \(P\), so there is another, say \(Q\).

Replace \(P\) in \(C\) by \(Q\). For a proper interval, the complementary arc has no internal vertex in \(T\); for \(T=V(C)\), it is the single edge \(st\). In either case the result is a Hamiltonian cycle different from \(C\). \(\square\)

This criterion applies to arbitrary Hamiltonian graphs, not just regular ones.

## 4. Consequences for a complementary \(2\)-factor

Now let \(G\) be \(4\)-regular and \(C\) Hamiltonian. Then
\[
F=G-E(C)
\]
is a spanning disjoint union of cycles.

### 4.1 At most one odd component

If all components of \(F\) are even cycles, \(F\) has a perfect matching. Apply the criterion with \(T=V(G)\).

If \(F\) has exactly one odd cycle, choose a vertex \(v\) on it. Then:

- that odd cycle minus \(v\) is an even-order path;
- every other component of \(F\) is an even cycle.

Thus \(F-v\) has a perfect matching. Since \(V(G)\setminus\{v\}\) is a cyclic interval of \(C\), the criterion again applies.

### 4.2 Two odd components joined by an edge of \(C\)

Suppose \(F\) has exactly two odd components, and \(uv\in E(C)\) joins them.

Deleting \(u,v\) from \(F\) leaves two even-order paths and any remaining even cycles. Therefore
\[
F-\{u,v\}
\]
has a perfect matching. Because \(u,v\) are consecutive on \(C\), their complement is a cyclic interval. Hence there is a second Hamiltonian cycle.

### 4.3 Proof of the stated proposition

If \(F\) has at most two components, the preceding cases cover everything except the possibility that its two components are both odd.

In that remaining case, the spanning cycle \(C\) must have an edge joining the two components. Section 4.2 applies. This proves the proposition. \(\square\)

More generally, suppose \(F\) has \(q\ge1\) odd components. If \(q\) consecutive vertices of \(C\) meet each odd component exactly once, deleting those vertices makes \(F\) perfectly matchable. The same argument gives a second Hamiltonian cycle.

### Necessary conditions for a counterexample

If a uniquely Hamiltonian \(4\)-regular graph existed, its unique cycle \(C\) and complementary factor \(F\) would therefore satisfy:

1. \(F\) has at least three components.
2. \(F\) has at least two odd components.
3. If \(|V(G)|\) is odd, \(F\) has at least three odd components.
4. If \(F\) has exactly two odd components, no edge of \(C\) joins them.
5. For every nonempty cyclic interval \(T\) of \(C\), the graph \(F[T]\) has no perfect matching.

The third assertion follows because the number of odd components of \(F\) has the same parity as \(|V(G)|\).

## 5. A sharp limitation of the interval criterion

The criterion does not apply to every Hamiltonian \(4\)-regular pair \((G,C)\). Here is an explicit obstruction, followed by a proof of its minimal order.

### 5.1 A \(12\)-vertex example

Take
\[
C=(0,1,2,\ldots,11,0)
\]
and let \(F\) consist of the three cycles
\[
(0,2,4),\qquad
(6,8,10),\qquad
(1,5,9,3,11,7).
\]
Set \(G=C\cup F\).

The cycles of \(F\) partition the vertices, and every edge of \(F\) joins indices of the same parity, whereas every edge of \(C\) joins opposite parities. Thus \(G\) is simple and \(4\)-regular.

I claim that **no nonempty cyclic interval \(T\) of this specified \(C\) has a perfect matching in \(F[T]\)**.

Let
\[
U=\{0,2,4,6,8,10\},\qquad
W=\{1,3,5,7,9,11\}.
\]
A proper interval of even size \(2k\) contains \(k\) vertices from each set. Since \(F\) has no edges between \(U\) and \(W\), perfect matchability requires \(k\) even. Thus only interval sizes \(4\) and \(8\) need consideration.

- **Size \(4\).** Its two vertices in \(W\) are consecutive in the cyclic order
  \[
  1,3,5,7,9,11.
  \]
  No such pair is an edge of \(F[W]\). They cannot be matched.

- **Size \(8\).** Its four vertices in \(U\) must consist of two vertices from each triangle. The only possibilities, with their corresponding \(W\)-sets, are listed below. Each \(W\)-set contains an isolated vertex in its induced subgraph of \(F\).
  \[
  \begin{array}{c|c|c}
  T\cap U&T\cap W&\text{isolated vertex}\\ \hline
  \{2,4,6,8\}&\{1,3,5,7\}&3\\
  \{2,4,6,8\}&\{3,5,7,9\}&7\\
  \{8,10,0,2\}&\{7,9,11,1\}&9\\
  \{8,10,0,2\}&\{9,11,1,3\}&1
  \end{array}
  \]

Odd-sized intervals cannot have perfect matchings, and the whole vertex set cannot either because \(F\) contains odd components. This proves the claim.

Nevertheless, \(G\) is **not** uniquely Hamiltonian. An explicit second cycle is
\[
(0,2,4,5,9,3,11,10,8,6,7,1,0).
\]

Thus the example defeats the proposed stronger statement that every Hamiltonian \(4\)-regular pair possesses an interval-matching certificate. It does not defeat Sheehan’s conjecture.

### 5.2 Why \(12\) is the first possible failure of this certificate

Every Hamiltonian \(4\)-regular pair \((G,C)\) on at most \(11\) vertices satisfies the interval criterion.

For at most eight vertices, \(F\) has at most two components, so Section 4 supplies the certificate. For orders \(9,10,11\), only the following additional cases arise.

- **Order \(9\): \(F\) consists of three triangles.**  
  Label the vertices of \(C\) by their triangles. Adjacent labels differ. If no three consecutive labels were all distinct, every label would equal the label two positions later, so the cyclic word could use at most two labels. This is impossible. Three consecutive vertices therefore meet all three odd components.

- **Order \(10\): component lengths \(3,3,4\).**  
  If no edge of \(C\) joined the two triangles, their six vertices would be independent in \(C\): edges inside either triangle are already in \(F\). But a \(10\)-cycle has independence number \(5\). Hence Section 4.2 applies.

- **Order \(11\): component lengths \(3,4,4\) or \(3,3,5\).**  
  The first case has only one odd component.

  In the second case, call the triangle labels \(A,B\), and the remaining label \(D\). Suppose there were no three consecutive vertices with three different labels. If an \(A\)-\(B\) edge occurred on \(C\), the next label would have to be \(A\): it cannot be \(B\), because \(B\) is a triangle, and cannot be \(D\), by assumption. Repeating this reasoning forces the whole cycle to alternate \(A,B\), a contradiction.

  Thus no \(A\)-\(B\) edge occurs. The six triangle vertices would then be independent in an \(11\)-cycle, again impossible. Hence a consecutive transversal of the three odd components exists.

This covers every possible component-length partition. Together with the explicit example, it establishes the claimed sharp \(12\)-vertex limitation for this certificate.

## 6. The remaining gap

The parity argument proves the odd-degree case and the stated special cases for degree \(4\). As in the question, an even-regular counterexample would yield a \(4\)-regular one by retaining its unique Hamiltonian cycle and a \(2\)-factor of the remaining edges.

What is missing is an argument for arbitrary \(4\)-regular pairs whose complementary \(2\)-factor has several components and admits no matchable cyclic interval. The example above shows that the existence of such an interval cannot simply be asserted—even when there are only two odd components.

Accordingly, this is a proved special-case result and an explicit diagnosis of its limitation, not a proof or counterexample to the full conjecture.