```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A clique-plus-sparse-random-core construction gives k = Theta(sqrt(n)) and c(H) = Omega(n^(1/4) log n), exceeding sqrt(n/k) by a logarithmic factor.",
  "would_publish": false,
  "caveats": "This uses the standard vertex-move game, in which c(H) equals the cop number of the 2-section; any additional source-specific restriction would need checking."
}
```

# The conjecture is false

Throughout, players occupy vertices, a move is allowed between two vertices contained in a common hyperedge, and capture occurs when a cop occupies the robber's vertex.

## 1. Reduction to a graph with clique-covered edges

For a hypergraph \(H\), let \(\partial H\) be its 2-section: two distinct vertices are adjacent in \(\partial H\) precisely when they lie in a common hyperedge of \(H\). The legal moves in the two games are identical, so

\[
c(H)=c(\partial H).
\]

Conversely, suppose a graph \(G\) has the property that every edge of \(G\) lies in a copy of \(K_k\). For each edge \(e\in E(G)\), select one \(k\)-clique \(Q_e\) containing \(e\), and form the \(k\)-uniform hypergraph

\[
H=(V(G),\{V(Q_e):e\in E(G)\}).
\]

After removing duplicate hyperedges, this is a simple \(k\)-graph, and its 2-section is exactly \(G\). Thus it suffices to construct connected graphs of large cop number in which every edge lies in a large clique.

## 2. The random graph construction

Let \(N\) tend to infinity. Take disjoint sets \(P,R\), each of cardinality \(N\), and put

\[
\rho=N^{-1/4},
\qquad
k=\left\lfloor \frac{\sqrt N}{2}\right\rfloor.
\]

Construct a random graph \(G\) on \(P\cup R\) as follows:

1. \(P\) induces a clique.
2. Every pair having at least one endpoint in \(R\) is independently made an edge with probability \(\rho\).

Thus the \(R\)-\(R\) and \(P\)-\(R\) edges are independent Bernoulli variables with parameter \(\rho\).

For \(u\in R\), write

\[
A_u=N_G(u)\cap P.
\]

We first verify that, with high probability, every edge of \(G\) lies in a \(K_k\).

### Clique-covering event

For each \(u\in R\),

\[
|A_u|\sim \operatorname{Bin}(N,\rho),
\qquad
\mathbb E|A_u|=N^{3/4}.
\]

For distinct \(u,v\in R\),

\[
|A_u\cap A_v|\sim \operatorname{Bin}(N,\rho^2),
\qquad
\mathbb E|A_u\cap A_v|=\sqrt N.
\]

Let \(\mathcal A\) be the event that

\[
|A_u|\ge k-1 \quad\text{for every }u\in R,
\]
and
\[
|A_u\cap A_v|\ge k-2
   \quad\text{for every distinct }u,v\in R.
\]

For sufficiently large \(N\), \(k\le \frac12\sqrt N\le \frac12N^{3/4}\). Standard Chernoff estimates therefore give

\[
\Pr\bigl(|A_u|<k-1\bigr)
 \le \exp(-N^{3/4}/8)
\]

and

\[
\Pr\bigl(|A_u\cap A_v|<k-2\bigr)
 \le \exp(-\sqrt N/8).
\]

Consequently,

\[
\Pr(\mathcal A^c)
 \le N e^{-N^{3/4}/8}+N^2e^{-\sqrt N/8}
 =o(1).
\]

On \(\mathcal A\), every edge of \(G\) belongs to a \(K_k\):

- An edge inside \(P\) extends to a \(k\)-subset of the clique \(P\).
- If \(up\) is an edge with \(u\in R\) and \(p\in P\), choose \(k-1\) vertices of \(A_u\), including \(p\). Together with \(u\) they form a \(K_k\).
- If \(uv\) is an edge inside \(R\), choose \(k-2\) vertices of \(A_u\cap A_v\). Together with \(u,v\) they form a \(K_k\).

Moreover, every \(u\in R\) has a neighbor in \(P\), so \(G\) is connected.

## 3. A cop-number lower bound

We use the following elementary evasion criterion.

### Safe-neighbor lemma

Let \(G\) be a graph, \(R\subseteq V(G)\), and \(q\) a positive integer. Suppose that

\[
\tag{\(*\)}
\text{for every }u\in R
\text{ and every }C\subseteq V(G)\setminus\{u\},\ |C|\le q,
\]
there exists
\[
v\in N_G(u)\cap R
\quad\text{such that}\quad
v\notin N_G[C],
\]
where \(N_G[C]\) denotes the union of the closed neighborhoods of vertices in \(C\). Then \(c(G)>q\).

#### Proof

After the cops choose their initial set \(C_0\), choose any \(u\in R\setminus C_0\). By \((*)\), there is a vertex \(r\in R\setminus N[C_0]\), and the robber starts at \(r\).

Maintain the invariant that the robber is in \(R\) and is outside the closed neighborhood of every cop. At the next cops' move, no cop can move onto the robber, since before moving no cop is equal or adjacent to the robber. Let \(C'\) be the new set of cop positions. In particular, the current robber vertex is not in \(C'\). Applying \((*)\) with the current robber vertex and \(C'\), the robber can move along an edge to a vertex of \(R\setminus N[C']\). The invariant continues indefinitely. ∎

### The random graph satisfies the criterion

Set

\[
q=\left\lfloor \frac{N^{1/4}\ln N}{32}\right\rfloor.
\]

Fix \(u\in R\) and a set

\[
C\subseteq V(G)\setminus\{u\},
\qquad |C|=j\le q.
\]

For each

\[
v\in R\setminus(C\cup\{u\}),
\]

consider the event that

\[
uv\in E(G)
\quad\text{and}\quad
vx\notin E(G)\ \text{for every }x\in C.
\]

Because every edge incident with \(R\) is independently present with probability \(\rho\), this event has probability

\[
\rho(1-\rho)^j.
\]

These events are independent as \(v\) varies: their defining sets of random edges are disjoint.

For \(N\) large, \(\rho\le \frac12\), and hence

\[
\ln(1-\rho)\ge -2\rho.
\]

Therefore

\[
\rho(1-\rho)^j
 \ge \rho(1-\rho)^q
 \ge \rho e^{-2\rho q}
 \ge N^{-1/4}N^{-1/16}
 =N^{-5/16}.
\]

There are at least \(N-q-1\ge N/2\) possible vertices \(v\). Hence the probability that no suitable \(v\) exists is at most

\[
\exp\left(-\frac12N^{11/16}\right).
\]

The total number of choices of \(u\) and \(C\) is at most

\[
N\sum_{j=0}^{q}\binom{2N-1}{j}
 \le N(q+1)(2N)^q.
\]

Its logarithm is

\[
O\!\left(N^{1/4}(\ln N)^2\right)
   =o(N^{11/16}).
\]

A union bound therefore gives

\[
\Pr\bigl((*)\text{ fails}\bigr)
 \le N(q+1)(2N)^q
       \exp\left(-\frac12N^{11/16}\right)
 =o(1).
\]

Thus, with high probability, the safe-neighbor lemma applies and

\[
c(G)>q
 =\Omega(N^{1/4}\log N).
\]

## 4. Passage to a \(k\)-uniform hypergraph

Both the clique-covering event \(\mathcal A\) and the safe-neighbor event hold simultaneously with probability tending to one. Fix any realization satisfying both.

For each edge of \(G\), select a \(K_k\) containing it, and take these selected \(k\)-cliques as the hyperedges of \(H\). Then:

- \(H\) is a connected \(k\)-uniform hypergraph;
- its number of vertices is \(n=2N\);
- its 2-section is exactly \(G\);
- hence \(c(H)=c(G)\).

For large \(N\),

\[
k=\left\lfloor\frac{\sqrt N}{2}\right\rfloor
   =\Theta(\sqrt n),
\]

and

\[
\sqrt{\frac nk}
 =\Theta(N^{1/4}).
\]

On the other hand,

\[
c(H)
 =\Omega(N^{1/4}\log N).
\]

Consequently,

\[
\frac{c(H)}{\sqrt{n/k}}
 =\Omega(\log N)\longrightarrow\infty.
\]

Therefore no universal constant \(C\) can satisfy

\[
c(H)\le C\sqrt{\frac nk}
\]

for all connected \(k\)-uniform hypergraphs.

## Scope

The construction is probabilistic, but it proves the existence of such a hypergraph for every sufficiently large \(N\). If a deterministic specification is desired, one may take the lexicographically first labeled graph satisfying the two finite conditions above.

There is no remaining mathematical gap for the extracted statement under the standard definition of the hypergraph Cops and Robber game.