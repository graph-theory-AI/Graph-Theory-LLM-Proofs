```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Dense strongly connected digraphs require Ω(n²) list probes to output a DFS tree even when both incoming and outgoing lists are sorted, but the minimally strong adjacency-list case remains unresolved.",
  "would_publish": false,
  "caveats": "This is an input-access lower bound, not a new algorithm or a superlinear lower bound for sparse minimally strong inputs."
}
```

# A stronger lower bound for the general case

The main sparse question remains unresolved here. However, the general-case lower bound can be strengthened substantially: **supplying sorted incoming lists as well as sorted outgoing lists does not permit subquadratic worst-case time**. The lower bound also holds for bounded-error randomized algorithms and when every vertex has the same, publicly known, indegree and outdegree.

I reuse the previous attempt’s elementary observation that a left-maximal DFS-tree is, in particular, a spanning out-arborescence. This observation is valid: a DFS starting anywhere in a strongly connected digraph visits every vertex. The construction below replaces the previous attempt’s dense hard instance and removes its outgoing-only and unsorted-storage restrictions.

## 1. Model and result

The vertices have labels \(1,\ldots,n\). The input provides, for every vertex,

- its outgoing-neighbor array, sorted by vertex label;
- its incoming-neighbor array, also sorted;
- the lengths of both arrays.

An algorithm may probe any array entry in constant time. All other computation can be free for purposes of the lower bound. The output tree is explicit, with vertex-labeled arcs; its root may be chosen by the algorithm.

This is at least as powerful an input-access model as ordinary adjacency lists. A list-entry-probe lower bound gives the same asymptotic running-time lower bound on a standard word RAM with \(\Theta(\log n)\)-bit words.

### Theorem

For every \(k\ge 3\), there is a family of strongly connected digraphs on
\[
n=2k,\qquad m=2k(k-1)
\]
vertices and arcs, respectively, such that:

1. every vertex has indegree and outdegree \(k-1\);
2. every deterministic algorithm outputting a spanning out-arborescence requires at least
   \[
   k(k-1)-1
   \]
   list-entry probes in the worst case;
3. every randomized algorithm that succeeds with probability at least \(2/3\) on every input and always makes at most \(q\) probes satisfies
   \[
   q\ge \frac23 k(k-1)-1.
   \]

The randomized worst-case expected probe complexity is also \(\Omega(k^2)\).

All conclusions therefore apply to computing a left-maximal DFS-tree.

## 2. The hard family

Let
\[
A=\{a_1,\ldots,a_k\},\qquad B=\{b_1,\ldots,b_k\},
\]
with interleaved numerical labels
\[
a_i=2i-1,\qquad b_i=2i.
\]

Let \(H\) consist of two disjoint complete bidirected graphs, one on \(A\) and one on \(B\). Thus its arcs are
\[
a_i a_j,\ b_i b_j \qquad (i\ne j).
\]

The unknown parameter is an ordered pair
\[
(p,q)\in\mathcal P:=\{(i,j)\in[k]^2:i\ne j\}.
\]
There are
\[
K:=|\mathcal P|=k(k-1)
\]
possible parameters.

Define \(D_{p,q}\) by a degree-preserving switch:
\[
D_{p,q}
=
H-\{a_p a_q,\ b_p b_q\}
+\{a_p b_q,\ b_p a_q\}.
\]

In words, delete one corresponding internal arc from each clique and exchange their heads.

### Strong connectivity

The subdigraph on \(A\) is a complete bidirected graph with only \(a_p a_q\) deleted. It remains strongly connected: the missing connection can be replaced by
\[
a_p\longrightarrow a_r\longrightarrow a_q
\]
for any \(r\notin\{p,q\}\), which exists because \(k\ge3\). The same holds on \(B\).

There is an arc from \(A\) to \(B\), namely \(a_p b_q\), and one from \(B\) to \(A\), namely \(b_p a_q\). Hence \(D_{p,q}\) is strongly connected.

### Degrees and input lengths reveal nothing

The switch preserves every indegree and outdegree. Consequently, in every member of the family,
\[
d^+(v)=d^-(v)=k-1
\quad\text{for every }v,
\]
and
\[
m=2k(k-1).
\]

Thus all list lengths—and indeed the entire degree sequence—are independent of the hidden pair.

## 3. Even the sorted arrays differ in only four cells

Give the algorithm the graph \(H\), its sorted arrays, and the promise describing this family for free. It must only determine enough about the unknown switch to output a tree.

Relative to \(H\), exactly four list entries change:

| Array | Entry replacement |
|---|---|
| \(\operatorname{out}(a_p)\) | \(a_q\mapsto b_q\) |
| \(\operatorname{out}(b_p)\) | \(b_q\mapsto a_q\) |
| \(\operatorname{in}(a_q)\) | \(a_p\mapsto b_p\) |
| \(\operatorname{in}(b_q)\) | \(b_p\mapsto a_p\) |

Crucially, **these replacements do not move any entries when the lists are sorted**.

For example, \(a_q\) and \(b_q\) have consecutive labels \(2q-1\) and \(2q\). Replacing \(a_q\) by \(b_q\) in an otherwise all-\(A\) list preserves the order. Replacing \(b_q\) by \(a_q\) in an otherwise all-\(B\) list does likewise. The incoming-list replacements have the same property.

Moreover, each array cell belongs to the four-cell change set of exactly one candidate \((p,q)\). For instance, an outgoing-array cell in the row of \(a_p\), whose baseline value is \(a_q\), changes precisely for parameter \((p,q)\). An incoming-array cell in the row of \(a_q\), whose baseline value is \(a_p\), changes precisely for that same parameter.

Therefore a probe has exactly the information content of an equality test:
\[
\text{“Is the hidden parameter }(p,q)\text{?”}
\]
It returns the known baseline value unless the tested candidate is the hidden one.

The redundancy between incoming and outgoing lists gives four ways to test each candidate, not a way to test several candidates at once.

## 4. Any output spanning tree identifies the hidden pair

The only arcs of \(D_{p,q}\) crossing between \(A\) and \(B\) are
\[
a_p b_q,\qquad b_p a_q.
\]

Every spanning out-arborescence has a connected underlying undirected graph, so it must contain a crossing arc. Either crossing arc determines \((p,q)\).

Equivalently, for two distinct parameters \((p,q)\ne(p',q')\), the intersection
\[
D_{p,q}\cap D_{p',q'}
\]
has no arcs between \(A\) and \(B\). Thus **no single explicit spanning out-arborescence can be valid for two different members of the family**.

This remains true whether the root is prescribed or chosen freely. Adding the DFS and left-maximality requirements cannot make the task easier.

## 5. Deterministic lower bound

An adversary answers every probe with its value in the baseline graph \(H\).

Each distinct candidate tested this way is eliminated. After fewer than \(K-1\) candidate tests, at least two members of the family remain consistent with the entire transcript.

The algorithm cannot stop then: its fixed output cannot be a spanning out-arborescence for both remaining inputs.

Consequently, some valid input forces at least
\[
K-1=k(k-1)-1
=\frac{n^2}{4}-\frac n2-1
\]
probes.

The fact that \(H\) itself is not strong causes no difficulty. Until all but one candidates have been eliminated, the adversary’s answers remain consistent with at least one—and, before termination is possible, at least two—promised strongly connected inputs. \(\square\)

## 6. Bounded-error randomized lower bound

Choose the hidden pair uniformly from the \(K\) candidates.

First fix the algorithm’s random bits, making it deterministic, and suppose its probe count is capped at \(q\). Consider its transcript when every probe receives the baseline answer. Let \(S\) be the set of candidates tested on this transcript. Then
\[
|S|\le q.
\]

For every hidden parameter outside \(S\), the actual transcript is this same baseline transcript. Thus the output is the same for all such parameters, and it can be correct for at most one of them.

For parameters in \(S\), give the algorithm the benefit of assuming it always succeeds. Its success probability on a uniform hidden parameter is therefore at most
\[
\frac{|S|+1}{K}\le\frac{q+1}{K}.
\]

Averaging over the random bits preserves this inequality. If success probability is at least \(2/3\) on every input, it is at least \(2/3\) on the uniform distribution, so
\[
\frac23\le\frac{q+1}{K}.
\]
Hence
\[
q\ge\frac23K-1=\Omega(n^2).
\]

### Expected running time

Suppose instead that success probability is at least \(2/3\) on every input and the worst-case expected probe count is \(t\). Truncate execution after
\[
Q=\lceil6t\rceil
\]
probes, declaring failure if it has not stopped.

By Markov’s inequality, truncation reduces success probability by at most \(1/6\). The truncated algorithm therefore succeeds with probability at least \(1/2\) on every input. The preceding argument gives
\[
Q\ge K/2-1,
\]
and hence
\[
t\ge K/12-O(1)=\Omega(n^2).
\]
This includes zero-error randomized algorithms. \(\square\)

## 7. What this settles—and what it does not

### General strongly connected inputs

This rules out an \(o(n^2)\) worst-case algorithm, measured solely in terms of \(n\), in a strong ordinary adjacency-list model:

- both incoming and outgoing lists are available;
- both are sorted;
- all degrees are fixed and known;
- randomization with bounded error is allowed.

Since \(m=2K\), the bound is also \(\Omega(m)\) on this family. It is not merely an assertion that an algorithm must “read its input”: the proof shows why it must inspect a linear fraction of the entries even to output a spanning tree.

This does **not** itself establish a matching upper bound for left-maximal DFS-trees of general digraphs.

### Minimally strongly connected inputs

Here the input-size obstruction disappears. For completeness, the sparsity observation in the earlier attempt is correct.

Fix a root \(r\). A strong digraph contains a spanning out-arborescence \(T^+\) and a spanning in-arborescence \(T^-\), both rooted at \(r\). Their union is strongly connected, since every vertex can reach \(r\) and be reached from \(r\).

If the digraph is arc-minimal strongly connected, it cannot have any arc outside this union. Therefore
\[
m\le |A(T^+)|+|A(T^-)|=2n-2.
\]

Our dense hard family is consequently outside the minimally strong promise. Its lower bound provides no superlinear obstruction for minimally strong adjacency-list inputs.

## Remaining gap

The central question is still open in this attempt:

> Can a left-maximal DFS-tree of a minimally strongly connected digraph, represented by adjacency lists, be computed in \(o(n^2)\) time?

Likewise, the lower bound does not rule out an input-sensitive general algorithm of the form
\[
O\bigl(m+o(n^2)\bigr).
\]

The progress is a stronger, representation-robust obstruction for dense general inputs. It does not address the additional computational difficulty caused specifically by left-maximality.