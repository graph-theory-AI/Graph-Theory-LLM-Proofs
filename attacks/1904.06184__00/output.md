```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general recognition problem remains unresolved, but Switchable graphs admit exact polynomial-time recognition on split, co-bipartite, bipartite, chordal, and C4-free inputs.",
  "would_publish": false,
  "caveats": "The general case and its hardness remain open, and some subclass results may be implicit in known strong-chordality theory."
}
```

# 1. Definitions and scope

I interpret the catalogued class as follows. For a graph \(H\), let \(\mathcal R(H)\) have as vertices the perfect matchings of \(H\), with two perfect matchings adjacent when their symmetric difference is a cycle of length four. A graph \(G\) is **Switchable** if, for every induced subgraph \(H\subseteq G\), every two perfect matchings of \(H\) lie in the same component of \(\mathcal R(H)\). The condition is vacuous when \(H\) has at most one perfect matching.

I do not resolve recognition on arbitrary graphs. I prove exact polynomial recognition for two nontrivial classes—split and co-bipartite graphs—and record several further exact special cases.

# 2. A basic reduction to even cycles

For an even cycle
\[
C=v_0v_1\cdots v_{2k-1}v_0,
\]
write
\[
M_C^0=\{v_{2i}v_{2i+1}:0\le i<k\},\qquad
M_C^1=\{v_{2i+1}v_{2i+2}:0\le i<k\},
\]
with indices modulo \(2k\).

## Lemma 2.1: Cycle criterion

A graph \(G\) is Switchable if and only if, for every even cycle \(C\) of \(G\), the two rim matchings \(M_C^0,M_C^1\) are connected in
\(\mathcal R(G[V(C)])\).

### Proof

Necessity follows by taking the induced subgraph \(G[V(C)]\).

Conversely, let \(H\) be an induced subgraph of \(G\), and let \(M,N\) be perfect matchings of \(H\). Their symmetric difference is a disjoint union of even cycles
\[
M\mathbin{\triangle}N=C_1\dot\cup\cdots\dot\cup C_t.
\]
On each \(C_i\), the restrictions of \(M\) and \(N\) are the two rim matchings. By hypothesis these can be reconfigured inside \(G[V(C_i)]\). Extending each such flip sequence by the fixed matching edges outside \(V(C_i)\), and treating the cycles one at a time, transforms \(M\) into \(N\). ∎

A chord \(v_iv_j\) of \(C\) will be called a **splitting chord** if \(i-j\) is odd. Equivalently, each of the two cycles formed from the chord and one rim arc is even. This is sometimes called an odd chord, but terminology varies.

## Lemma 2.2: Splitting a cycle

Suppose \(C\) has a splitting chord \(uv\), forming two smaller even cycles \(C_1,C_2\). If the rim matchings of \(C_1\) and \(C_2\) are connected in their respective induced subgraphs, then \(M_C^0\) and \(M_C^1\) are connected in \(G[V(C)]\).

### Proof

Each rim \(u\)-\(v\) path has odd length. One rim matching of \(C\) consists of the matching covering all vertices of the first path, together with the unique matching covering the internal vertices of the second path. Reconfiguring on \(C_1\) produces the matching containing \(uv\) and the internal matchings of both paths. Reconfiguring on \(C_2\) then produces the other rim matching of \(C\). All matching edges outside the cycle currently being reconfigured remain fixed. ∎

Consequently:

> If every even cycle of length at least six has a splitting chord, then the graph is Switchable.

The converse is false; see Section 8.

# 3. Exact recognition on split graphs

Let \(G\) be split, with
\[
V(G)=K\dot\cup I,
\]
where \(K\) is a clique and \(I\) is independent. Let \(B_G\) be the bipartite graph with bipartition \((K,I)\) and precisely the \(K\)-\(I\) edges of \(G\).

Recall that a bipartite graph is chordal bipartite if it has no induced cycle of length at least six.

## Theorem 3.1

For a split graph \(G\), the following are equivalent:

1. \(G\) is Switchable.
2. \(B_G\) is chordal bipartite.
3. \(G\) contains no induced \(k\)-sun, for any \(k\ge3\).

Thus Switchability of split graphs is recognizable in polynomial time.

### Proof: \(B_G\) not chordal bipartite implies non-Switchable

Suppose \(B_G\) contains an induced cycle
\[
s_0c_0s_1c_1\cdots s_{k-1}c_{k-1}s_0,
\qquad k\ge3,
\]
where \(s_i\in I\) and \(c_i\in K\). In \(G\), the vertices \(c_i\) form a clique, the \(s_i\) form an independent set, and the only selected \(I\)-\(K\) edges are the cycle edges. This is an induced \(k\)-sun.

The cycle has two rim perfect matchings. Consider either one, say \(M\). Every edge of \(M\) is an \(I\)-\(K\) edge. An \(M\)-alternating \(4\)-cycle would therefore use two vertices of \(I\) and two of \(K\), and would give a \(K_{2,2}\) in \(B_G\) on the selected vertices. But an induced cycle of length at least six has no such \(K_{2,2}\). Hence \(M\) admits no flip and is isolated. The two rim matchings are disconnected, so \(G\) is not Switchable.

### Proof: \(B_G\) chordal bipartite implies Switchable

We first establish a small parity fact. Let \(C\) be an even cycle of length \(2k\ge6\) in \(G\), and suppose \(C\) has no splitting chord.

Let \(K_E\) and \(K_O\) be the clique vertices in the even and odd positions of \(C\). Every pair in \(K_E\times K_O\) is adjacent because \(K\) is a clique. Since there is no splitting chord, every such pair must be consecutive on \(C\).

If both \(K_E\) and \(K_O\) are nonempty, then the complete bipartite graph between them is contained in the cycle \(C_{2k}\). Since a cycle of length at least six contains no \(K_{2,2}\), one of \(K_E,K_O\) has size one and the other has size at most two. Thus \(C\) contains at most three clique vertices. On the other hand, \(I\) is independent, so at most \(k\) vertices of \(C\) belong to \(I\), and hence at least \(k\) belong to \(K\). This is impossible for \(k\ge4\). For \(k=3\), equality would force the three \(I\)-vertices to be one parity class of \(C_6\), so the clique vertices again occupy only the other parity.

It follows that, if \(C\) has no splitting chord, the cycle strictly alternates between \(K\) and \(I\). Moreover, any additional \(K\)-\(I\) edge among \(V(C)\) would itself be a splitting chord. Therefore \(B_G[V(C)]\) would be an induced cycle of length at least six, contradicting chordal bipartiteness.

Thus every even cycle of length at least six has a splitting chord. Lemmas 2.1 and 2.2 imply that \(G\) is Switchable. ∎

## Recognition algorithm

It remains only to recognize whether a bipartite graph \(B\) has an induced cycle of length at least six. The following explicit polynomial algorithm suffices.

For every vertex \(z\) and every unordered pair of distinct neighbors \(x,y\in N(z)\), form
\[
B_{zxy}
=
B-\Bigl(
\{z\}\cup
(N(z)\setminus\{x,y\})\cup
((N(x)\cap N(y))\setminus\{z\})
\Bigr).
\]
Search for an \(x\)-\(y\) path in \(B_{zxy}\).

- All common neighbors of \(x,y\), other than \(z\), have been removed, so any such path has length at least four.
- A shortest such path is induced.
- The deletion of \(N(z)\setminus\{x,y\}\) ensures that adding \(z\) produces an induced cycle.

Conversely, if \(B\) has an induced cycle of length at least six, take \(z\) and its two neighbors \(x,y\) on the cycle. The complementary \(x\)-\(y\) path survives these deletions.

There are \(O(n^3)\) triples \((z,x,y)\), and each search takes \(O(n+m)\) time. This gives an explicit \(O(n^3(n+m))\) algorithm.

The successful case is constructive: recursively split alternating cycles along splitting chords. A cycle of length \(2k\) requires at most \(k-1\) flips, so any two perfect matchings of an \(n\)-vertex induced subgraph can be connected using at most \(n/2\) flips.

# 4. Exact recognition on co-bipartite graphs

A graph is co-bipartite if
\[
V(G)=A\dot\cup B
\]
where both \(A\) and \(B\) are cliques.

## Theorem 4.1

For a co-bipartite graph \(G\), the following are equivalent:

1. \(G\) is Switchable.
2. For every six-element set \(S\subseteq V(G)\), the perfect-matching reconfiguration graph \(\mathcal R(G[S])\) is connected.

Consequently, Switchability of co-bipartite graphs can be recognized in \(O(n^6)\) time.

### A binary cyclic-word lemma

Let \(C=w_0\cdots w_{2k-1}w_0\) be an even cycle in a co-bipartite graph, and label \(w_i\) by \(A\) or \(B\).

Suppose \(C\) has no splitting chord. For \(X\in\{A,B\}\), let \(E_X\) and \(O_X\) be the even and odd positions carrying label \(X\). Because \(X\) is a clique, every pair in \(E_X\times O_X\) is an edge. The absence of splitting chords says all these pairs are consecutive on \(C\).

For \(k\ge3\), a cycle \(C_{2k}\) has no \(K_{2,2}\). Therefore, if \(E_X,O_X\) are both nonempty, then one has size one, the other size at most two, and \(X\) occurs at most three times.

It follows that:

- If \(k\ge4\), neither label can occur in both parities. Hence one clique occupies all even positions and the other all odd positions.
- If \(k=3\), either the same conclusion holds, or both labels occur in both parities. In the latter case each label occurs exactly three times, necessarily in the cyclic pattern
  \[
  AAABBB
  \]
  up to rotation and exchanging \(A,B\).

Thus a cycle without a splitting chord is either:

1. **aligned**, alternating globally between the two clique classes; or
2. a six-cycle with cyclic clique pattern \(AAABBB\).

### Aligned cycles are always reconfigurable

Write an aligned cycle as
\[
a_0b_0a_1b_1\cdots a_{k-1}b_{k-1}a_0,
\]
where \(a_i\in A\), \(b_i\in B\). Its rim matchings are
\[
M=\{a_ib_i:0\le i<k\},
\qquad
N=\{a_{i+1}b_i:0\le i<k\}.
\]

For \(k\ge3\), the following sequence transforms \(M\) into \(N\).

1. Flip
   \[
   a_0b_0,\ a_1b_1
   \quad\longrightarrow\quad
   a_0a_1,\ b_0b_1.
   \]

2. Flip
   \[
   a_0a_1,\ a_{k-1}b_{k-1}
   \quad\longrightarrow\quad
   a_0b_{k-1},\ a_1a_{k-1}.
   \]

3. For \(j=2,\ldots,k-2\), flip
   \[
   b_0b_{j-1},\ a_jb_j
   \quad\longrightarrow\quad
   a_jb_{j-1},\ b_0b_j.
   \]

4. Finally flip
   \[
   a_1a_{k-1},\ b_0b_{k-2}
   \quad\longrightarrow\quad
   a_1b_0,\ a_{k-1}b_{k-2}.
   \]

Every required same-clique edge exists. This uses \(k\) flips. For \(k=2\), the rim matchings differ by one flip.

### Proof of the theorem

Necessity of condition 2 is immediate from hereditary Switchability.

Conversely, assume condition 2. Consider any even cycle \(C\).

- If \(C\) has a splitting chord, use Lemma 2.2 and induction on its length.
- If it has no splitting chord and is aligned, use the explicit sequence above.
- The only remaining case is a six-cycle of pattern \(AAABBB\). Its two rim matchings lie in \(\mathcal R(G[V(C)])\), which is connected by condition 2.

Thus every even cycle satisfies the cycle criterion of Lemma 2.1, and \(G\) is Switchable. ∎

## Explicit algorithm

For every six-element set \(S\):

1. Enumerate its at most \(15\) perfect matchings.
2. Join two matchings when their symmetric difference is a \(4\)-cycle.
3. Test connectivity of this constant-sized graph.

This takes \(O(n^6)\) time.

The proof is constructive. In a connected six-vertex matching graph, a path has length at most \(14\). Using the additive parameter
\[
\mu(C)=|C|/2-1
\]
under splitting, the preceding construction gives at most
\[
7\mu(C)
\]
flips for each symmetric-difference cycle. Hence any two perfect matchings of an \(n\)-vertex induced subgraph can be connected using at most \(7n/2\) flips.

# 5. Further exact special cases

## 5.1 Bipartite graphs

A bipartite graph \(G\) is Switchable if and only if it is chordal bipartite.

Indeed, every chord of an even cycle in a bipartite graph is a splitting chord. Conversely, an induced cycle of length at least six has two rim perfect matchings and no available flip.

## 5.2 Chordal graphs

Using the standard equivalent characterization
\[
\text{strongly chordal}
\iff
\text{chordal and sun-free}
\iff
\text{every even cycle of length at least six has a splitting chord},
\]
one obtains:

> A chordal graph is Switchable if and only if it is strongly chordal.

The forward implication follows because every induced sun is a non-Switchable witness, as in Theorem 3.1. The reverse implication follows from Lemma 2.2.

## 5.3 \(C_4\)-free graphs

Here \(C_4\)-free means containing no \(4\)-cycle, induced or otherwise.

> A \(C_4\)-free graph is Switchable if and only if it contains no even cycle.

If there is an even cycle \(C\), then \(G[V(C)]\) has two rim perfect matchings but admits no flips at all. Conversely, if two perfect matchings of any induced subgraph were distinct, their symmetric difference would contain an even cycle.

Graphs with no even cycle can be recognized by their blocks: every nontrivial 2-connected block must be an odd cycle. Otherwise an ear or theta subgraph supplies an even cycle.

# 6. General complexity upper bound

From the direct hereditary definition, recognition lies in PSPACE.

One can iterate over induced vertex sets and pairs of perfect matchings using polynomial space. Reachability in the implicitly represented perfect-matching reconfiguration graph is in PSPACE by the standard implicit-graph reachability algorithm, and PSPACE is closed under complement and polynomially many nested quantifiers. This does not give a polynomial algorithm or a useful certificate in the general case.

# 7. Why the splitting-chord argument does not solve the general case

The sufficient condition “every long even cycle has a splitting chord” is not necessary.

Let \(H_+\) have rim cycle \(0123450\) and additional edges
\[
02,\ 13,\ 24.
\]
There is no splitting chord of the rim cycle, but its two rim matchings are connected:
\[
\begin{aligned}
\{01,23,45\}
&\longrightarrow \{02,13,45\}\\
&\longrightarrow \{13,24,50\}\\
&\longrightarrow \{12,34,50\}.
\end{aligned}
\]
Every proper induced subgraph has at most four vertices relevant to a perfect matching pair, so \(H_+\) itself is Switchable.

In contrast, let \(H_-\) be the same \(6\)-cycle with additional edges
\[
02,\ 24,\ 40.
\]
Then
\[
M=\{01,23,45\}
\]
is frozen: none of its three pairs of matching edges belongs to an alternating \(4\)-cycle. Thus \(H_-\) is not Switchable.

Moreover, the rim \(6\)-cycle of \(H_-\) is the symmetric difference of the three \(4\)-cycles
\[
01240,\qquad 23402,\qquad 45024.
\]
Thus even generation of the cycle space, or of the corresponding integer circulation relation, by \(4\)-cycles is not sufficient: the required \(4\)-cycles need not be alternating at any currently available perfect matching.

This is the unresolved general obstruction. Same-parity chords can support long sequences of switches without giving a direct recursive decomposition, and I do not obtain either:

- a polynomial algorithm for deciding whether such a sequence exists for every induced cycle, or
- a hardness reduction for general Switchable recognition.

Accordingly, the catalogued general problem remains open in this analysis.