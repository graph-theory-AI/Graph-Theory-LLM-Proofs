```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "RFCPP is APX-complete already on bidirected stars, admits a deterministic constant approximation when requested directed distances are bounded, and has an O(log |R|)-approximation on symmetric digraphs.",
  "would_publish": false,
  "caveats": "These results neither give a constant approximation nor prove constant-factor hardness for unrestricted directed RFCPP."
}
```

# Mathematical writeup

## 1. Problem and an exact reformulation

Let \(D=(V,A)\) be strongly connected and let \(R\subseteq \binom V2\). For an enumeration \(\pi\), let

\[
A_\pi=\{uv\in A:\pi(u)<\pi(v)\}.
\]

A request \(\{x,y\}\) is realized if \(A_\pi\) contains an \(x\)-to-\(y\) path or a \(y\)-to-\(x\) path.

### Lemma 1
The RFCPP optimum is

\[
\max_{H\subseteq D\text{ acyclic}}
\left|\left\{\{x,y\}\in R:
x\leadsto_H y\text{ or }y\leadsto_H x\right\}\right|.
\]

#### Proof
For every enumeration \(\pi\), \(D_\pi=(V,A_\pi)\) is acyclic, and its requested comparable pairs are exactly those realized by \(\pi\).

Conversely, if \(H\subseteq D\) is acyclic, take a topological ordering of \(H\). Every arc of \(H\) is then forward, so every request connected in one direction in \(H\) is realized. ∎

This emphasizes the source of difficulty: the objective is a reachability objective on an acyclic subgraph, rather than an additive objective on its arcs.

---

## 2. Bounded request distance gives a constant approximation

For a request \(r=\{x,y\}\), write \(d(x,y)\) for directed distance in \(D\). Since \(D\) is strong, both directed distances are finite.

### Theorem 2
There is a deterministic polynomial-time algorithm producing an enumeration realizing at least

\[
\sum_{\{x,y\}\in R}
\left(
\frac{1}{(d(x,y)+1)!}
+
\frac{1}{(d(y,x)+1)!}
\right)
\tag{1}
\]

requests.

Consequently, if

\[
L=\max_{\{x,y\}\in R}\min\{d(x,y),d(y,x)\},
\]

then RFCPP has a deterministic \((L+1)!\)-approximation on this class of instances. In particular, RFCPP is in APX whenever \(L\) is bounded by a constant.

### Proof
For every request \(r=\{x,y\}\), choose shortest directed paths

\[
P_r^+=(x=v_0,v_1,\dots,v_a=y),
\qquad
P_r^-=(y=w_0,w_1,\dots,w_b=x).
\]

In a uniformly random enumeration, the vertices of \(P_r^+\) occur in their prescribed order with probability \(1/(a+1)!\). On that event, \(P_r^+\) is a forward path. Similarly, \(P_r^-\) is forward with probability \(1/(b+1)!\).

The two events are disjoint: the first requires \(x\) before \(y\), while the second requires \(y\) before \(x\). Hence the expected number of requests realized through one of these chosen paths is exactly the quantity in (1). Thus some enumeration attains at least (1).

This can be derandomized by conditional expectation. Given a prefix of the enumeration, the conditional probability that a prescribed sequence \(z_1,\dots,z_k\) will occur in order is:

- zero if the sequence vertices already chosen are not an initial segment \(z_1,\dots,z_j\) in the correct order;
- \(1/(k-j)!\) otherwise.

At each position, test every remaining vertex as the next choice and select one maximizing the resulting conditional expectation. All chosen paths have at most \(n\) vertices, so this is polynomial time.

Finally, if every request has one direction of distance at most \(L\), then each summand in (1) is at least \(1/(L+1)!\). Hence the algorithm realizes at least

\[
\frac{|R|}{(L+1)!}\geq \frac{\operatorname{OPT}}{(L+1)!}.
\]

∎

The factorial dependence is only a restricted-case result. For example, on a directed Hamiltonian cycle all requests can be realized by cutting the cycle into a Hamiltonian path, while a fixed long witness path is monotone in only a factorially small proportion of random orders.

---

## 3. Exact equivalence with MAX-CUT on bidirected stars

The following gives a sharp complexity classification for a very restricted class.

### Theorem 3
RFCPP restricted to bidirected stars, with all requests between leaves, is exactly unweighted MAX-CUT. Consequently this restricted RFCPP is APX-complete and has no PTAS unless \(P=NP\).

### Proof
Given a simple graph \(G=(U,E)\), construct a digraph \(D\) with vertex set \(U\cup\{c\}\), where for every \(u\in U\) both arcs \(uc\) and \(cu\) are present. Thus \(D\) is a strongly connected bidirected star. Set

\[
R=\{\{u,v\}:uv\in E\}.
\]

Consider an enumeration \(\pi\). The unique simple path in the underlying star between distinct leaves \(u,v\) is \(u,c,v\). Thus \(\{u,v\}\) is forward-connected exactly when

\[
\pi(u)<\pi(c)<\pi(v)
\quad\text{or}\quad
\pi(v)<\pi(c)<\pi(u).
\]

Let

\[
S=\{u\in U:\pi(u)<\pi(c)\}.
\]

The realized requests are therefore exactly the edges of \(G\) crossing the cut \((S,U\setminus S)\).

Conversely, every cut \(S\subseteq U\) is represented by placing all vertices of \(S\) before \(c\) and all vertices of \(U\setminus S\) after \(c\). Hence

\[
\operatorname{OPT}_{\mathrm{RFCPP}}(D,R)
=
\operatorname{MAXCUT}(G).
\]

The transformations between solutions preserve objective values exactly. Since unweighted MAX-CUT is APX-hard, this restriction of RFCPP is APX-hard. It belongs to APX because a random cut, derandomized by conditional expectation, cuts at least \(|E|/2\) edges and hence is a \(2\)-approximation. ∎

Thus RFCPP is already NP-hard and APX-hard on symmetric strong digraphs of directed diameter two. This rules out a PTAS but does not rule out a constant approximation for general RFCPP.

---

## 4. An \(O(\log |R|)\)-approximation for symmetric digraphs

Call \(D\) symmetric if \(uv\in A(D)\) implies \(vu\in A(D)\). The proof actually only needs \(D\) to contain a bidirected spanning tree.

### Theorem 4
Let \(D\) contain a bidirected spanning tree, and let \(m=|R|\geq1\). There is a deterministic polynomial-time enumeration realizing at least

\[
\frac{m}{2(1+\lfloor\log_2 m\rfloor)}
\]

requests. Consequently this class has a deterministic

\[
2(1+\lfloor\log_2 m\rfloor)
\]

approximation.

### Proof

Fix a bidirected spanning tree \(T\).

#### Request-weighted centroid decomposition

For a connected subtree \(U\subseteq T\), let \(Q\) be the requests whose two endpoints are in \(U\) and which have not yet been assigned. Give each vertex \(v\in U\) weight equal to the number of endpoints of requests in \(Q\) located at \(v\). The total weight is \(2|Q|\).

Choose a weighted centroid \(c\), so that every component \(B\) of \(U-c\) has endpoint weight at most \(|Q|\). Assign to \(c\) all requests in \(Q\) whose \(T\)-path contains \(c\). Every remaining request has both endpoints in one component \(B\), and we recurse there.

If \(Q_B\) is the set passed to \(B\), then

\[
2|Q_B|
\leq \text{endpoint weight of }B
\leq |Q|,
\]

so \(|Q_B|\leq |Q|/2\). Thus the recursion has at most

\[
h=1+\lfloor\log_2 m\rfloor
\]

nonempty levels. Every request is assigned exactly once.

#### Satisfying half the requests assigned to one centroid

Fix a recursion node with subtree \(U\), centroid \(c\), and assigned request set \(Q_c\). The components of \(U-c\) will be called branches.

For each branch \(B\), choose one of two states:

- orient every edge of \(B\cup\{c\}\) toward \(c\);
- orient every such edge away from \(c\).

If a request has one endpoint equal to \(c\), its tree path is directed in one of the two directions regardless of the branch state.

Otherwise its endpoints lie in distinct branches \(B_1,B_2\). Its path is directed exactly when \(B_1\) and \(B_2\) receive opposite states. Therefore these requests define a multigraph on the branches, and choosing the branch states is precisely a cut problem. A random choice cuts half its edges in expectation, so a deterministic greedy conditional-expectation procedure satisfies at least half of \(Q_c\).

#### Combining one recursion level

At any fixed recursion depth, the corresponding subtrees \(U\) are vertex-disjoint. Hence their edge orientations can be chosen independently, satisfying at least half the requests assigned at that depth. Orient all remaining tree edges arbitrarily.

Every orientation of a tree is acyclic, so take a topological ordering of the oriented tree. Since both directed versions of every tree edge belong to \(D\), each consistently oriented request path is a forward path in \(D\).

Let \(m_i\) be the number of requests assigned at depth \(i\). Since

\[
\sum_{i=0}^{h-1}m_i=m,
\]

some depth has \(m_i\geq m/h\). The corresponding enumeration realizes at least \(m_i/2\geq m/(2h)\) requests. Since \(\operatorname{OPT}\leq m\), this is also a \(2h\)-approximation. ∎

The same argument works for nonnegative request weights, with the decomposition depth controlled by the number of positive-weight requests.

---

## 5. What remains open

The unrestricted directed problem is not resolved here.

1. The bounded-distance approximation deteriorates factorially with the maximum requested distance.
2. The symmetric-digraph algorithm has a logarithmic, not constant, approximation factor.
3. The MAX-CUT reduction proves only APX-hardness. It excludes a PTAS under \(P\neq NP\), but is fully compatible with the existence of a constant-factor approximation.
4. The bidirected-tree argument relies crucially on independently orienting tree edges and then topologically sorting. A general strong digraph need not contain a bidirected spanning tree, and replacing tree edges by directed paths can introduce incompatible overlaps and directed cycles.
5. Proposition 4 from the source, asserting that \(\operatorname{OPT}/|R|\) can tend to zero, is consistent with the \(O(\log |R|)\) symmetric guarantee and does not by itself imply hardness relative to \(\operatorname{OPT}\).

Thus the central dichotomy—constant approximation versus constant-factor inapproximability for unrestricted directed RFCPP—remains open.