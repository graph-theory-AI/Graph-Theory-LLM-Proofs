```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for k≤3 or n≤k+4, and its bound is attained by every directed power of a cycle.",
  "would_publish": false,
  "caveats": "Standard loopless convention; no general resolution or claim that these special cases are new."
}
```

# Partial results

Throughout, digraphs are finite, nonempty and loopless, with no parallel arcs. Opposite arcs are allowed. A \(k\)-regular digraph has
\[
d^+(v)=d^-(v)=k
\]
at every vertex.

Write \(\nu(D)\) for the maximum number of arc-disjoint directed cycles in \(D\), and put
\[
T(k)=\binom{k+1}{2}.
\]

I establish the following special cases, without claiming novelty.

**Theorem.**
1. Every \(k\)-regular digraph satisfies \(\nu(G)\ge T(k)\) when \(k\le3\).
2. The same conclusion holds whenever \(G\) has \(n\le k+4\) vertices.
3. Let \(P(n,k)\), where \(0\le k<n\), have vertex set \(\mathbb Z_n\) and arcs
   \[
   x\longrightarrow x+j,\qquad 1\le j\le k.
   \]
   Then
   \[
   \nu(P(n,k))=T(k).
   \]
   Thus the proposed bound is attained by directed powers of cycles of every permissible order, not just by the complete symmetric digraph.

The proof uses an exact complementation identity and a degree-three splitting argument.

## 1. Elementary packing facts

Call a digraph **balanced** if every vertex has equal indegree and outdegree. Every finite balanced digraph decomposes into directed cycles: repeatedly remove a directed cycle; balance is preserved, and a nonempty balanced digraph cannot be acyclic.

Consequently,
\[
\nu(D)\ge \max_v d^+(v)
\tag{1}
\]
for every balanced digraph \(D\).

Also, every digraph of minimum outdegree at least \(d\) has \(d\) arc-disjoint directed cycles. Indeed, after removing fewer than \(d\) directed cycles, the minimum outdegree remains positive.

These facts give an elementary bound useful below:
\[
\nu(G)\ge 2k-1
\qquad(k\ge1)
\tag{2}
\]
for every \(k\)-regular \(G\).

To prove (2), choose \(v\). The digraph \(G-v\) has minimum outdegree at least \(k-1\), so it contains \(k-1\) arc-disjoint cycles. Delete their arcs from \(G\). The remaining digraph is balanced, and \(v\) still has outdegree \(k\); by (1), it has at least \(k\) further arc-disjoint cycles.

In particular, the conjecture holds for \(k=0,1,2\).

## 2. An exact complementation identity

A pair of opposite arcs will be called a **digon**.

### Lemma 1
If \(u\to v\) and \(v\to u\) are arcs of \(D\), then
\[
\nu(D)=1+\nu\bigl(D-\{u\to v,v\to u\}\bigr).
\tag{3}
\]

**Proof.**
The lower bound follows by adding the digon to a packing in the remaining graph.

For the upper bound, take a maximum packing in \(D\).

- If the digon itself is a member, delete it.
- If only one of its arcs is used, discard the cycle containing that arc.
- If its two arcs belong to distinct cycles, delete these arcs from those cycles. The two remaining directed paths concatenate into a closed directed trail, which contains a directed cycle avoiding both deleted arcs. Replace the original two cycles by this cycle.
- If neither arc is used, retain the packing.

In every case, deleting the two arcs leaves a packing with at least \(\nu(D)-1\) cycles. ∎

Let \(b(D)\) count the digons, and let \(R(D)\) be obtained by deleting all their arcs. Repeated application of (3) gives
\[
\nu(D)=b(D)+\nu(R(D)).
\tag{4}
\]

Let \(\overline D\) denote the directed complement: it contains \(x\to y\), for \(x\ne y\), precisely when \(D\) does not.

For each unordered vertex pair:

- a digon of \(D\) becomes an empty pair in \(\overline D\);
- an empty pair becomes a digon;
- a single arc becomes its reverse.

Thus \(R(\overline D)\) is the reversal of \(R(D)\), and these residual digraphs have the same packing number. If \(m=|A(D)|\), counting unordered pairs gives
\[
b(D)-b(\overline D)=m-\binom n2.
\]
Together with (4), this proves the exact identity
\[
\boxed{\nu(D)-\nu(\overline D)=|A(D)|-\binom n2.}
\tag{5}
\]

Now suppose \(G\) is \(k\)-regular and set
\[
t=n-1-k.
\]
Its complement is \(t\)-regular. Since \(n=k+t+1\), equation (5) becomes
\[
\boxed{\nu(G)-T(k)=\nu(\overline G)-T(t).}
\tag{6}
\]

In particular, the conjectured inequality for a regular digraph is equivalent to the inequality for its complement.

Since it is already proved for degrees at most two, (6) proves it whenever \(n\le k+3\). In particular, it settles all 3-regular digraphs on at most six vertices.

## 3. A safe vertex-splitting operation

Suppose \(v\) has distinct inneighbors \(a_1,\dots,a_k\) and distinct outneighbors \(b_1,\dots,b_k\). Choose a bijection pairing these incoming and outgoing arcs. Delete \(v\) and replace each paired two-arc path
\[
a_i\to v\to b_{\pi(i)}
\]
by the arc \(a_i\to b_{\pi(i)}\).

Call this split **admissible** if none of the new arcs is a loop or already present. An admissible split of a \(k\)-regular digraph produces a loopless simple \(k\)-regular digraph \(H\) on one fewer vertex.

Moreover,
\[
\nu(G)\ge \nu(H).
\tag{7}
\]
Indeed, lift every new arc used by a packing in \(H\) back to its two-arc path through \(v\). The resulting closed directed trails are arc-disjoint: the paired paths use distinct incoming and outgoing arcs at \(v\). Each trail contains a directed cycle, so selecting one from each trail proves (7).

Existence of an admissible split is a bipartite matching question. Its two vertex classes are \(N^-(v)\) and \(N^+(v)\); a pair \(a,b\) is allowed exactly when \(a\ne b\) and \(a\to b\) is absent.

## 4. The conjecture for degree three

The useful local fact is specific to degree three.

### Lemma 2
Let \(G\) be 3-regular. If some vertex \(v\) belongs to no digon, then \(G\) has a vertex admitting an admissible split.

**Proof.**
Put
\[
A=N^-(v),\qquad B=N^+(v).
\]
Because \(v\) belongs to no digon, \(A\cap B=\varnothing\).

In the bipartite graph of allowed pairs from \(A\) to \(B\), every vertex has degree at least one. Each \(a\in A\) already sends an arc to \(v\), so it cannot send arcs to all three vertices of \(B\). The corresponding indegree argument applies to each \(b\in B\).

If this bipartite graph has a perfect matching, split \(v\). Otherwise, Hall’s theorem implies that two vertices of \(A\) have only one allowed neighbor: singleton sets have a neighbor, and all three vertices of \(A\) collectively meet all of \(B\).

Relabel so that
\[
A=\{a_1,a_2,a_3\},\qquad B=\{b_1,b_2,b_3\},
\]
and \(b_3\) is the only allowed neighbor of \(\{a_1,a_2\}\). Hence all four arcs
\[
a_i\to b_j,\qquad i,j\in\{1,2\},
\]
are present. Regularity now forces
\[
N^+(a_1)=N^+(a_2)=\{v,b_1,b_2\},
\tag{8}
\]
and
\[
N^-(b_1)=N^-(b_2)=\{v,a_1,a_2\}.
\tag{9}
\]

Consider splitting \(a_1\). Its outneighbors are \(\{v,b_1,b_2\}\). Write \(U=N^-(a_1)\). We have
\[
U\cap\{a_1,a_2,v\}=\varnothing:
\]
loops exclude \(a_1\); equation (8) excludes \(a_2\); and the absence of a digon at \(v\) excludes \(v\).

By (9), no vertex of \(U\) sends an existing arc to \(b_1\) or \(b_2\). Thus the only possible forbidden pairs with these heads are the loops
\[
(b_1,b_1),\qquad (b_2,b_2).
\]
Since \(N^-(v)=\{a_1,a_2,a_3\}\), the only possible forbidden pair with head \(v\) is
\[
(a_3,v).
\]

These three possible forbidden pairs have distinct tails and distinct heads, because \(A\cap B=\varnothing\). Therefore the allowed-pair graph for splitting \(a_1\) is \(K_{3,3}\) with a matching deleted. It has a perfect matching, giving an admissible split of \(a_1\). ∎

### Proposition
Every 3-regular digraph contains six arc-disjoint directed cycles.

**Proof.**
Suppose otherwise, and choose a counterexample \(G\) with the fewest vertices. Section 2 gives
\[
n=|V(G)|\ge7.
\]

Let \(b\) be its number of digons.

If \(b\ge6\), the digons themselves give the required packing.

If \(b=4\) or \(5\), delete all digons and call the remaining balanced digraph \(R\). It has
\[
|A(R)|=3n-2b\ge3n-10>n.
\]
Thus some vertex of \(R\) has outdegree at least two, and (1) gives two arc-disjoint cycles in \(R\). Together with the \(b\) digons, these give at least six cycles.

Consequently a counterexample must have \(b\le3\). At most \(2b\le6\) vertices belong to digons, so \(G\) has a vertex belonging to no digon. Lemma 2 supplies an admissible split, producing a 3-regular digraph \(H\) on \(n-1\) vertices.

By minimality, \(\nu(H)\ge6\). Equation (7) then gives \(\nu(G)\ge6\), a contradiction. ∎

This completes the proof for \(k\le3\). Applying (6) to complements also proves the conjecture whenever
\[
n-1-k\le3,
\]
equivalently \(n\le k+4\).

## 5. Exact packing numbers for directed cycle powers

Recall that \(P(n,k)\) has arcs
\[
x\to x+j\pmod n,\qquad 1\le j\le k.
\]

### Upper bound

Assign weight \(j\) to the arc \(x\to x+j\). Around every directed cycle, the sum of these positive increments is a positive multiple of \(n\), so every cycle has weight at least \(n\).

The total weight of all arcs is
\[
n\sum_{j=1}^k j=nT(k).
\]
An arc-disjoint packing therefore has at most \(T(k)\) cycles:
\[
\nu(P(n,k))\le T(k).
\tag{10}
\]

### Matching lower bound

The case \(k=0\) is immediate. For fixed \(k\ge1\), induct on \(n\ge k+1\).

When \(n=k+1\), the graph is the complete symmetric digraph, whose \(T(k)\) digons give the required packing.

Suppose \(n\ge k+2\). At vertex \(0\), pair the incoming and outgoing arcs as
\[
(n-j)\to0\to(k+1-j),
\qquad j=1,\dots,k.
\]
The new arcs would be
\[
(n-j)\to(k+1-j).
\tag{11}
\]
Their original clockwise distance is \(k+1<n\). They are therefore neither loops nor existing arcs, so this split is admissible.

After deleting \(0\), use the cyclic order
\[
1,2,\dots,n-1.
\]
Every surviving old arc has forward distance at most \(k\), and every new arc in (11) has forward distance exactly \(k\). The resulting graph is thus a subdigraph of \(P(n-1,k)\). It is also \(k\)-regular, so it is exactly \(P(n-1,k)\), up to relabeling.

By induction and (7),
\[
\nu(P(n,k))\ge \nu(P(n-1,k))\ge T(k).
\]
Combining this with (10) proves
\[
\boxed{\nu(P(n,k))=\binom{k+1}{2}.}
\]

In fact, a maximum packing here uses every arc: its cycles have total weight at least \(nT(k)\), equal to the weight of the entire graph.

## 6. What remains unresolved

The argument does not settle arbitrary degrees \(k\ge4\). The degree-three splitting lemma relies on a failed matching producing the saturated neighborhoods (8)–(9); the same conclusion does not follow in larger degree.

The complementation identity shows that any counterexample could be replaced by one satisfying
\[
4\le k\le\frac{n-1}{2}.
\]
Apart from the cycle-power family and the dense cases proved above, this regime remains untreated here.

No improvement of the quoted asymptotic constant for unrestricted regular digraphs is established, and no literature-status claim is made.