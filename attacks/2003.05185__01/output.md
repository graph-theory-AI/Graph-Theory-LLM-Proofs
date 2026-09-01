```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A balanced-neighborhood recursion gives an n^{O(r log n)}-time MWIS algorithm for P7-free graphs with no induced K_{1,r}, while the unrestricted case remains unresolved.",
  "would_publish": false,
  "caveats": "The bound is still quasi-polynomial for fixed r, and unrestricted P7-free graphs have unbounded neighborhood independence."
}
```

# 1. Outcome

I do not obtain either a polynomial-time algorithm or an NP-hardness proof for unrestricted \(P_7\)-free graphs.

I can, however, prove a sharper quasi-polynomial bound for an orthogonal special case. Write \(K_{1,r}\) for the induced star with \(r\) leaves.

## Theorem

For fixed integers \(t\ge 3\) and \(r\ge 2\), Maximum Weight Independent Set on \((P_t,K_{1,r})\)-free graphs can be solved in time
\[
n^{O(tr\log n)}.
\]
More explicitly, a direct implementation runs in
\[
n^{((t-1)(r-1)+2)\lceil\log_2 n\rceil+O_{t,r}(1)}.
\]

Consequently, for every fixed \(r\), MWIS on \(P_7\)-free, induced-\(K_{1,r}\)-free graphs is solvable in
\[
n^{O(r\log n)}=2^{O(r\log^2 n)}
\]
time.

For fixed \(r\), this improves the \(n^{O(\log^3 n)}\) general \(P_7\)-free bound reported in the catalog to \(n^{O(\log n)}\) on this subclass. The subclass still has unbounded clique number and unbounded independence number.

I do not claim literature novelty for this elementary separator argument.

# 2. A balanced closed-neighborhood lemma

For a graph \(H\) on \(m\) vertices, call \(X\subseteq V(H)\) balanced if every component of \(H-X\) has at most \(m/2\) vertices.

## Lemma 1

Every connected \(P_t\)-free graph \(H\) contains an induced path \(Q\) on at most \(t-1\) vertices such that \(N_H[Q]\) is balanced.

### Proof

Choose an arbitrary vertex \(q_1\), and put \(Q_i=q_1q_2\cdots q_i\).

Suppose inductively that \(Q_i\) is induced. If \(N[Q_i]\) is balanced, stop. Otherwise, there is a unique component
\[
C_i\quad\text{of}\quad H-N[Q_i]
\]
with more than \(m/2\) vertices.

For \(i=1\), connectedness of \(H\) implies that some vertex
\[
q_2\in N(q_1)
\]
has a neighbor in \(C_1\).

For \(i\ge 2\), the construction maintains that \(q_i\) has a neighbor in \(C_{i-1}\). Moreover, \(C_i\subseteq C_{i-1}\): after passing from \(H-N[Q_{i-1}]\) to \(H-N[Q_i]\), a component with more than \(m/2\) vertices cannot be contained in one of the former non-heavy components.

Inside the connected graph \(C_{i-1}\), the set
\[
A_i=N(q_i)\cap C_{i-1}
\]
is nonempty, and \(C_i\) is a component of \(C_{i-1}-A_i\). Hence \(C_i\) has a neighbor in \(A_i\). Choose
\[
q_{i+1}\in A_i
\]
having a neighbor in \(C_i\).

Now \(q_{i+1}\) is adjacent to \(q_i\). Since
\[
q_{i+1}\in C_{i-1}\subseteq H-N[Q_{i-1}],
\]
it is nonadjacent to \(q_1,\ldots,q_{i-1}\). Thus \(Q_{i+1}\) is again an induced path.

If this construction did not stop by \(i=t-1\), it would construct the induced path \(q_1\cdots q_t\), contradicting that \(H\) is \(P_t\)-free. Therefore some \(Q_i\), \(i\le t-1\), has balanced closed neighborhood. ∎

The path and its balanced neighborhood are constructible by repeated component searches, in polynomial time.

# 3. Bounding the independent traces on the separator

## Lemma 2

Let \(H\) be induced-\(K_{1,r}\)-free, and let \(Q\) be a path. Then
\[
\alpha\bigl(H[N[Q]]\bigr)\le |Q|(r-1).
\]

### Proof

For every vertex \(q\),
\[
\alpha(H[N[q]])\le r-1.
\]
Indeed, an independent set in \(N[q]\) either contains \(q\), in which case it has size one, or consists of pairwise nonadjacent neighbors of \(q\). The latter cannot have size \(r\), since together with \(q\) it would induce \(K_{1,r}\).

Since
\[
N[Q]=\bigcup_{q\in Q}N[q],
\]
partitioning an independent subset of \(N[Q]\) according to one closed neighborhood containing each of its vertices gives
\[
\alpha(H[N[Q]])\le \sum_{q\in Q}\alpha(H[N[q]])
\le |Q|(r-1).
\]
∎

Combining Lemmas 1 and 2, every connected \((P_t,K_{1,r})\)-free graph has a balanced separator
\[
X=N[Q]
\]
such that every independent subset of \(X\) has size at most
\[
c=(t-1)(r-1).
\]

# 4. The recursive MWIS algorithm

Weights may be arbitrary rational or integer weights; the empty independent set is allowed.

For a disconnected graph, solve the components independently and add their optimum values. Now suppose \(H\) is connected.

1. Use Lemma 1 to construct \(Q\) with \(|Q|\le t-1\) and balanced \(X=N[Q]\).
2. Enumerate every subset \(S\subseteq X\) with \(|S|\le c\), retaining only independent subsets.
3. For each such \(S\), form
   \[
   R_S=H-\bigl(X\cup N_H(S)\bigr),
   \]
   where \(N_H(S)\) denotes the open neighborhood of \(S\).
4. Recursively solve every component of \(R_S\), and return the maximum of
   \[
   w(S)+\sum_{D\in\operatorname{cc}(R_S)}\operatorname{mwis}(D).
   \]

## Correctness

For any independent set \(I\) of \(H\), let
\[
S=I\cap X.
\]
By Lemma 2, \(|S|\le c\), so this \(S\) is enumerated. Every vertex of \(I-S\) lies outside \(X\) and is nonadjacent to \(S\), hence
\[
I-S\subseteq V(R_S).
\]

Conversely, if \(J\) is an independent set of \(R_S\), then \(S\cup J\) is independent in \(H\). Therefore, for each fixed independent \(S\subseteq X\), the maximum weight of an independent set meeting \(X\) exactly in \(S\) is
\[
w(S)+\operatorname{mwis}(R_S).
\]
MWIS is additive over components, giving the displayed recursion. Taking the maximum over all enumerated \(S\) is therefore exact.

Every recursive component has at most \(|V(H)|/2\) vertices because it is contained in a component of \(H-X\).

# 5. Running time

There are at most
\[
\sum_{j=0}^{c}\binom{|X|}{j}\le (c+1)n^c
\]
candidate sets \(S\).

Let \(T(m)\) denote a worst-case running-time bound for a connected \(m\)-vertex recursive instance. For each \(S\), there are at most \(m\) recursive components, each of order at most \(m/2\). Allowing \(O(m^2)\) work to construct and decompose each \(R_S\), a crude recurrence is
\[
T(m)\le A_{t,r}m^{c+2}
  \bigl(1+T(\lfloor m/2\rfloor)\bigr).
\]
Iterating for at most \(\lceil\log_2m\rceil\) levels gives
\[
T(n)\le
n^{(c+2)\lceil\log_2 n\rceil+O_{t,r}(1)}
=n^{O(tr\log n)}.
\]

For \(t=7\), \(c=6(r-1)\), yielding \(n^{O(r\log n)}\).

For fixed \(r\), the promise can also be checked in polynomial time: enumerate ordered seven-vertex sets to test for an induced \(P_7\), and enumerate a center and \(r\) pairwise nonadjacent neighbors to test for an induced \(K_{1,r}\).

Equivalently, if
\[
\lambda(G)=\max_{v\in V(G)}\alpha(G[N(v)])
\]
is bounded by \(s\), then the algorithm runs in
\[
n^{O(s\log n)}
\]
on \(P_7\)-free graphs.

# 6. Scope and obstructions

The fixed-\(r\) class does not have bounded clique number. For example, take a clique \(c_1,\ldots,c_m\) and attach a private leaf \(p_i\) to each \(c_i\). This graph is claw-free and \(P_5\)-free, while both its clique number and independence number are \(m\).

On the other hand, the separator argument does not extend directly to unrestricted \(P_7\)-free graphs. Let \(S_m\) be the subdivided star with vertices
\[
\{c\}\cup\{a_i,b_i:1\le i\le m\}
\]
and edges \(ca_i,a_ib_i\). This tree has diameter four, hence is \(P_6\)-free. Nevertheless,
\[
N[c]=\{c,a_1,\ldots,a_m\},
\qquad
\alpha(S_m[N[c]])=m.
\]
Indeed, every subset \(A\subseteq\{a_1,\ldots,a_m\}\) occurs as the intersection with \(N[c]\) of the independent set
\[
A\cup\{b_i:a_i\notin A\}.
\]
Thus a balanced closed neighborhood in a \(P_7\)-free graph can have exponentially many independent traces.

There is also no gain merely from assuming connectedness, diameter two, or a dominating vertex. Given any weighted \(P_7\)-free graph \(G\), add a zero-weight universal vertex \(u\). The resulting graph is still \(P_7\)-free, is connected with diameter at most two, and has
\[
\operatorname{mwis}(G+u)=\operatorname{mwis}(G).
\]
Hence those restrictions are polynomially equivalent to the unrestricted problem.

# 7. Remaining gap

The recursion above incurs \(n^{O(r)}\) choices at each of \(\Theta(\log n)\) balanced levels, so even for fixed \(r\) it does not become polynomial. In unrestricted \(P_7\)-free graphs, \(r\) can be linear in \(n\), and Lemma 2 supplies no useful bound.

Thus the original complexity question remains unanswered: this argument proves neither polynomial-time solvability nor NP-hardness for general \(P_7\)-free graphs.