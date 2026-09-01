```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general question remains open, but for every t >= 5 it is equivalent to its restriction to prime, clique-cutset-free diameter-two graphs, while logarithmic prime-quotient degree is polynomial-time solvable.",
  "would_publish": false,
  "caveats": "No general polynomial-time algorithm is obtained, and the novelty of the reduction lemmas has not been checked against the complete literature."
}
```

# Mathematical writeup

## 1. Problem and outcome

For fixed \(t\ge 7\), the problem asks whether Maximum Independent Set is polynomial-time solvable on graphs with no induced \(P_t\).

I do not obtain such an algorithm. I prove two partial results:

1. The problem remains polynomial-time equivalent even after restricting to \(P_t\)-free graphs that are simultaneously:
   - prime with respect to modular decomposition,
   - free of clique cutsets,
   - connected and co-connected,
   - of diameter two.

   Thus modular decomposition, clique-cutset decomposition, connectivity, and bounded diameter cannot by themselves resolve the conjecture.

2. Using the pathwidth-versus-maximum-degree theorem from the supplied source, one obtains a polynomial-time algorithm when every prime quotient in the modular decomposition has maximum degree \(O(\log n)\). A parameterized strengthening using deletion to bounded degree is also given.

The first result is valid for every \(t\ge 5\), hence in particular for all cases in the question.

---

## 2. Reduction to prime, clique-cutset-free diameter-two graphs

A set \(M\subseteq V(G)\) is a **module** if every vertex outside \(M\) is either complete or anticomplete to \(M\). A graph is **prime** if its only modules are the singletons and the whole vertex set.

### Theorem 2.1

Fix \(t\ge 5\). Given any nonempty \(P_t\)-free graph \(G\), one can construct in polynomial time a graph \(H\) such that

\[
\alpha(H)=\alpha(G)+1,
\]

and \(H\) is:

- \(P_t\)-free,
- prime,
- without a clique cutset,
- of diameter two.

Moreover, \(H\) has \(2|V(G)|+6\) vertices.

Consequently, for every fixed \(t\ge5\), MIS on \(P_t\)-free graphs is polynomial-time equivalent to MIS on the above restricted subclass.

### 2.1. First extension

Let \(G\) be nonempty. Form a graph \(A\) by adding three vertices \(p,q,r\) such that

- \(p\) is complete to \(V(G)\);
- \(q\) and \(r\) are anticomplete to \(V(G)\);
- among \(p,q,r\), the only edges are \(pq\) and \(qr\).

Thus, after contracting \(G\) to one vertex, the quotient is the path

\[
G-p-q-r.
\]

The set \(V(G)\) is a module of \(A\).

#### Claim 2.2

The graph \(A\) is connected and co-connected, and

\[
\alpha(A)=\alpha(G)+1.
\]

#### Proof

Connectivity is immediate from the path \(G-p-q-r\).

For co-connectivity, in \(\overline A\), the vertex \(r\) is adjacent to \(p\) and every vertex of \(G\), while \(q\) is adjacent to every vertex of \(G\). Hence \(\overline A\) is connected.

A maximum independent set of \(G\), together with \(q\), is independent in \(A\), so

\[
\alpha(A)\ge \alpha(G)+1.
\]

Conversely, if an independent set meets \(V(G)\), it cannot contain \(p\), and it contains at most one of \(q,r\). It therefore has size at most \(\alpha(G)+1\). If it avoids \(V(G)\), then it lies in the \(P_3\) induced by \(p,q,r\), and has size at most \(2\le\alpha(G)+1\). ∎

We use the following elementary module observation.

#### Lemma 2.3

Let \(M\) be a module of a graph \(X\). If an induced path \(P\) has at least four vertices and meets both \(M\) and \(V(X)\setminus M\), then \(P\) contains at most one vertex of \(M\).

#### Proof

Suppose an edge of \(P\) crosses from \(M\) to \(V(X)\setminus M\), say \(uv\) with \(u\in M\) and \(v\notin M\). Since \(M\) is a module and \(v\) has a neighbor in \(M\), \(v\) is complete to \(M\).

Thus every vertex of \(P\cap M\) must be a path-neighbor of \(v\), or else \(v\) gives a chord. There can be at most two such vertices. If there are two, they are the two path-neighbors of \(v\), producing a subpath \(x-v-y\). This subpath cannot be extended: any vertex adjacent to \(x\) outside \(M\) is also adjacent to \(y\), while another vertex of \(M\) is adjacent to \(v\). Either possibility gives a chord. Hence a crossing path with two vertices of \(M\) has at most three vertices. ∎

#### Claim 2.4

If \(G\) is \(P_t\)-free for \(t\ge5\), then \(A\) is \(P_t\)-free.

#### Proof

An induced \(P_t\) contained in \(V(G)\) is impossible. If it meets both \(V(G)\) and \(\{p,q,r\}\), Lemma 2.3 says it contains at most one vertex of \(G\). It would then have at most four vertices in total. ∎

### 2.2. Co-matching extension

For every \(a\in V(A)\), introduce a new vertex \(b_a\). Let

\[
B=\{b_a:a\in V(A)\}.
\]

Construct \(H\) as follows:

- \(H[A]=A\);
- \(B\) is a clique;
- \(b_a\) is adjacent to every vertex of \(A\) except \(a\).

Thus the nonedges between \(A\) and \(B\) form a perfect matching.

#### Claim 2.5

\[
\alpha(H)=\max\{\alpha(A),2\}=\alpha(G)+1.
\]

#### Proof

An independent set contains at most one vertex of the clique \(B\). If it contains \(b_a\), the only vertex of \(A\) that it may also contain is \(a\). Hence such an independent set has size at most two. Independent sets avoiding \(B\) are precisely independent sets of \(A\). Since \(\alpha(A)=\alpha(G)+1\ge2\), the result follows. ∎

#### Claim 2.6

Every induced path of \(H\) that meets \(B\) has at most four vertices.

#### Proof

An induced path contains at most two vertices of the clique \(B\), and if it contains two, they are consecutive.

Suppose first that the path contains exactly one vertex \(b_a\). This vertex is adjacent to every vertex of \(A\) except \(a\). All vertices of the path adjacent to \(b_a\) must be its path-neighbors, of which there are at most two; in addition, the path may contain \(a\). Hence the path has at most four vertices.

Now suppose it contains consecutive vertices \(b_a,b_c\). A vertex \(x\in A\setminus\{a,c\}\) is adjacent to both of them and therefore cannot occur on the induced path. The vertex \(a\) can occur only on the \(b_c\)-side, and \(c\) only on the \(b_a\)-side. Again the path has at most four vertices. ∎

Combining Claims 2.4 and 2.6 gives:

#### Corollary 2.7

If \(G\) is \(P_t\)-free for \(t\ge5\), then \(H\) is \(P_t\)-free.

### 2.3. Primeness

#### Claim 2.8

If \(\overline A\) is connected, then \(H\) is prime.

#### Proof

Let \(M\) be a nontrivial module of \(H\).

If \(M\subseteq A\) contains distinct \(a,c\), then \(b_a\) is nonadjacent to \(a\) and adjacent to \(c\), so \(b_a\) distinguishes two vertices of \(M\). Thus no nontrivial module lies entirely in \(A\). The symmetric argument shows that none lies entirely in \(B\).

Suppose therefore that \(M\) meets both \(A\) and \(B\). Set

\[
S=M\cap A,\qquad
T=\{a\in A:b_a\in M\}.
\]

If \(a\in S\setminus T\), then \(b_a\notin M\). The vertex \(b_a\) is adjacent to every member of \(M\cap B\) but is nonadjacent to \(a\), contradicting the module condition. Thus \(S\subseteq T\).

If \(a\in T\setminus S\), then \(a\notin M\) and is nonadjacent to \(b_a\). If \(T\) contains another element \(c\), then \(a\) is adjacent to \(b_c\), again contradicting the module condition. If \(T=\{a\}\), then the nonempty set \(S\subseteq T\) equals \(T\), also a contradiction. Hence \(T\subseteq S\).

Therefore \(S=T\), and

\[
M=S\cup\{b_a:a\in S\}.
\]

For every \(x\in A\setminus S\), the vertex \(x\) is adjacent to every \(b_a\) with \(a\in S\). Since \(M\) is a module, \(x\) must consequently be complete to all of \(M\), and in particular complete to \(S\) inside \(A\). Thus every edge between \(S\) and \(A\setminus S\) is present in \(A\).

If \(S\) is nonempty and proper, this means there is no edge between \(S\) and \(A\setminus S\) in \(\overline A\), contradicting connectivity of \(\overline A\). If \(S=A\), then \(M=V(H)\). Hence \(H\) has no proper nontrivial module. ∎

By Claim 2.2, \(\overline A\) is connected, so \(H\) is prime.

### 2.4. Absence of clique cutsets

#### Claim 2.9

If \(A\) is connected, then \(H\) has no clique cutset.

#### Proof

Let \(K\) be a clique of \(H\), and put \(R=B\setminus K\).

If \(|R|\ge2\), then every remaining vertex \(a\in A\setminus K\) is adjacent to at least one vertex of \(R\), because \(a\) has only one nonneighbor in \(B\). Since \(R\) is a clique, \(H-K\) is connected.

Suppose \(R=\varnothing\). Then \(B\subseteq K\). No vertex \(a\in A\) can belong to \(K\), because it is nonadjacent to \(b_a\in B\). Hence \(K=B\), and \(H-K=A\), which is connected.

Finally, suppose \(R=\{b_a\}\). Then \(B\setminus\{b_a\}\subseteq K\). If a vertex \(c\in A\) belongs to \(K\), then \(c\) must be adjacent to all of \(B\setminus\{b_a\}\). Since \(c\) is nonadjacent to \(b_c\), this forces \(c=a\). Thus \(K\cap A\subseteq\{a\}\).

If \(a\notin K\), the connected graph \(A\) remains, and \(b_a\) is adjacent to every vertex of \(A\setminus\{a\}\). If \(a\in K\), then \(b_a\) is adjacent to every remaining vertex of \(A-a\). In either case \(H-K\) is connected. ∎

### 2.5. Diameter

Since \(|A|\ge4\), any two nonadjacent vertices of \(A\) have a common neighbor in \(B\): choose \(b_c\) with \(c\) distinct from both. Also \(a\) and its matched nonneighbor \(b_a\) have a common neighbor \(b_c\), \(c\ne a\). Thus \(H\) has diameter two.

This proves Theorem 2.1.

### Consequence

For the decision version, map

\[
(G,k)\longmapsto (H,k+1).
\]

Then

\[
\alpha(G)\ge k
\quad\Longleftrightarrow\quad
\alpha(H)\ge k+1.
\]

The reverse reduction from the restricted class to general \(P_t\)-free graphs is the identity. Thus the two problems are polynomial-time equivalent.

This rules out an approach that merely decomposes along modules or clique cutsets: even the indecomposable atoms contain the full problem.

---

## 3. A polynomial special case from the pathwidth bound

The supplied source proves that, for each fixed \(t\), the pathwidth of a \(P_t\)-free graph is linear in its maximum degree. In the form needed here, there is an effective constant \(c_t\) such that

\[
\operatorname{tw}(F)\le \operatorname{pw}(F)
   \le c_t(\Delta(F)+1)
\]

for every \(P_t\)-free graph \(F\).

Using a standard single-exponential constant-factor treewidth approximation, a tree decomposition of width \(O_t(\Delta(F))\) can be found in time

\[
2^{O_t(\Delta(F))}|V(F)|^{O(1)}.
\]

Maximum Weight Independent Set can then be solved by the usual dynamic program over the decomposition. Therefore:

### Proposition 3.1

For fixed \(t\), Maximum Weight Independent Set on a \(P_t\)-free graph \(F\) of maximum degree \(d\) is solvable in time

\[
2^{O_t(d)}|V(F)|^{O(1)}.
\]

In particular, maximum degree \(O(\log n)\) gives polynomial time.

### 3.1. Prime quotients rather than the original maximum degree

Consider the modular decomposition tree of a graph \(G\). Each internal node has a quotient graph that is either complete, edgeless, or prime. Define

\[
D_{\mathrm{pr}}(G)
 =
 \max\{\Delta(Q):Q\text{ is a prime quotient in the modular decomposition of }G\},
\]

with the maximum equal to zero if there are no prime quotient nodes.

Each quotient \(Q\) of a \(P_t\)-free graph is itself \(P_t\)-free: choosing one representative from every child module produces an induced copy of \(Q\).

At a modular decomposition node with child modules \(M_1,\ldots,M_r\), assign quotient vertex \(i\) the weight

\[
w_i=\alpha(G[M_i]).
\]

An independent set of the quotient specifies exactly which pairwise anticomplete modules are used, and inside each selected module one takes an optimum independent set. Thus

\[
\alpha(G)=\alpha_w(Q).
\]

Complete and edgeless quotient nodes are handled by a maximum and a sum, respectively. At a prime quotient, Proposition 3.1 applies.

Hence:

### Theorem 3.2

For every fixed \(t\), Maximum Independent Set on a \(P_t\)-free graph \(G\) can be solved in time

\[
2^{O_t(D_{\mathrm{pr}}(G))}\,|V(G)|^{O(1)}.
\]

Consequently, the problem is polynomial-time solvable on the subclass satisfying

\[
D_{\mathrm{pr}}(G)=O(\log |V(G)|).
\]

This includes arbitrary substitutions into low-degree prime skeletons, even when the original graph has very large maximum degree.

### 3.2. Deletion to bounded degree

A modest parameterized strengthening is possible. For a graph \(Q\), define

\[
\kappa(Q)=
 \min_{S\subseteq V(Q)}
 \bigl(|S|+\Delta(Q-S)\bigr),
\]

and let \(\kappa_{\mathrm{pr}}(G)\) be the maximum of \(\kappa(Q)\) over all prime modular quotients.

For fixed integers \(d,s\), a set \(S\) of size at most \(s\) with \(\Delta(Q-S)\le d\) can be found, if one exists, by the following branching algorithm. If a current graph has a vertex \(v\) with \(d+1\) selected neighbors \(u_1,\ldots,u_{d+1}\), every valid deletion set must contain one of

\[
\{v,u_1,\ldots,u_{d+1}\}.
\]

Branching on these \(d+2\) choices gives running time

\[
(d+2)^s |V(Q)|^{O(1)}.
\]

Once such an \(S\) is known, enumerate independent subsets \(J\subseteq S\). For each \(J\),

\[
w(J)+
\alpha_w\bigl(Q-(S\cup N_Q(J))\bigr)
\]

is the best solution whose intersection with \(S\) is exactly \(J\). The residual graph has maximum degree at most \(d\), so Proposition 3.1 applies.

Trying all \(d=0,\ldots,k\), with deletion budget \(k-d\), yields:

### Proposition 3.3

For fixed \(t\), Maximum Independent Set on \(P_t\)-free graphs is fixed-parameter tractable parameterized by \(\kappa_{\mathrm{pr}}(G)\), with running time

\[
2^{O_t(k\log(k+2))}|V(G)|^{O(1)},
\qquad
k=\kappa_{\mathrm{pr}}(G).
\]

Thus the problem is polynomial-time solvable whenever

\[
\kappa_{\mathrm{pr}}(G)
 =O\!\left(\frac{\log n}{\log\log n}\right).
\]

If the relevant deletion sets are supplied with the input, the search factor disappears, and the condition can be relaxed to size plus residual degree \(O(\log n)\).

---

## 4. Why this does not settle the conjecture

The graph \(H\) constructed in Theorem 2.1 has a clique \(B\) of order \(|A|\), and vertices of degree linear in \(|V(H)|\). It is nevertheless prime and has no clique cutset. Moreover, it encodes an arbitrary original \(P_t\)-free instance through

\[
\alpha(H)=\alpha(G)+1.
\]

Thus neither the modular-decomposition algorithm nor the bounded-degree pathwidth argument handles the dense prime atoms produced by the reduction. Any full polynomial-time algorithm must exploit substantially finer structure inside such atoms.

The quasi-polynomial algorithm quoted in the prompt remains the strongest supplied general upper bound. It does not unconditionally “rule out NP-completeness”: NP-hardness together with that algorithm would imply a quasi-polynomial algorithm for NP and, under ordinary polynomial reductions, would contradict ETH. Without a complexity assumption, NP-hardness and a quasi-polynomial algorithm are not logically incompatible.

Accordingly, the unrestricted polynomial-time problem for fixed \(t\ge7\) remains unresolved by the present argument.