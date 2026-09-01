```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured logarithmic improvement is proved for broad structural classes via new spanning-tree and Kempe-orbit bounds, but the universal regime with many true twins and large block escape degrees remains open.",
  "would_publish": false,
  "caveats": "The catalog statement is informal and omits at least the complete-graph exception; novelty relative to unindexed literature has not been checked."
}
```

# 1. Precise formulation

Put
\[
q=\Delta+1,\qquad P(G,q)=\#\{\text{proper \(q\)-colourings of \(G\)}\},
\]
and let \(F(G,q)\) denote the number of frozen \(q\)-colourings.

A natural precise version of the proposed improvement is that, for some absolute \(c>0\),
\[
\frac{F(G,q)}{P(G,q)}
   \le q^{-c(m-1)},\qquad m=\frac nq,
\tag{1}
\]
whenever \(G\) is connected, \(G\ne K_q\), and \(G\) has a frozen \(q\)-colouring. Since
\[
q^{-c(m-1)}
 =\exp\left(-\Theta\left(\frac nq\log q\right)\right),
\]
this has the order suggested by Proposition 4.

The \(m-1\) is necessary: for \(G=K_q\), one has \(m=1\) and every proper \(q\)-colouring is frozen. In particular, the bound \((6/7)^{n/q}\), as quoted in the catalog, cannot literally include \(K_q\); the original theorem must contain an omitted exception or hypothesis.

I do not prove (1) universally. I prove it in two broad structural regimes and give a reduction of the remaining case.

Throughout, graphs are finite and simple.

# 2. Structure forced by one frozen colouring

Let \(\alpha\) be a frozen \(q\)-colouring of a graph of maximum degree at most \(q-1\).

For every vertex \(v\), all \(q-1\) colours different from \(\alpha(v)\) must occur in \(N(v)\). Consequently:

1. \(G\) is \((q-1)\)-regular.
2. Every colour occurs equally often. Write
   \[
   |\alpha^{-1}(i)|=m,\qquad n=qm.
   \]
3. Between every two colour classes there is a perfect matching.
4. Equivalently, \(\alpha\) is a covering projection \(G\to K_q\).

Fix a colour, say \(0\), and put
\[
S=\alpha^{-1}(0).
\]
The \(m\) closed neighbourhoods
\[
B_s=N[s],\qquad s\in S,
\]
partition \(V(G)\). Indeed, every vertex has exactly one colour-\(0\) vertex in its closed neighbourhood.

Moreover, every frozen colouring \(\beta\), not just \(\alpha\), uses all \(q\) colours exactly once on each \(B_s\). Thus, after denoting by \(v_{s,i}\) the unique vertex of \(\alpha\)-colour \(i\) in \(B_s\), every frozen \(\beta\) determines permutations
\[
\pi_s\in S_q,\qquad \pi_s(i)=\beta(v_{s,i}).
\tag{2}
\]

In particular,
\[
F(G,q)\le (q!)^m.
\tag{3}
\]

We shall compare this with the following elementary lower bound.

## Lemma 2.1: universal lower bound on the number of colourings

If \(\Delta(G)\le q-1\), then
\[
P(G,q)\ge (q!)^{n/q}.
\tag{4}
\]

### Proof

For a vertex ordering \(\sigma\), let \(d^-_\sigma(v)\) be the number of neighbours of \(v\) preceding it. Greedy colouring in this order gives
\[
P(G,q)\ge \prod_v\bigl(q-d^-_\sigma(v)\bigr).
\tag{5}
\]

Choose \(\sigma\) uniformly at random. If \(d(v)=d\), then the rank of \(v\) within \(\{v\}\cup N(v)\) is uniform, so \(d^-_\sigma(v)\) is uniform on \(\{0,\dots,d\}\). Hence
\[
\mathbb E\log\bigl(q-d^-_\sigma(v)\bigr)
 =\frac1{d+1}\sum_{j=0}^d\log(q-j)
 \ge \frac1q\log(q!),
\]
because \(d\le q-1\) and the sequence \(\log q,\log(q-1),\ldots,\log1\) is decreasing. Summing over \(v\), some ordering satisfies
\[
\sum_v\log(q-d^-_\sigma(v))\ge \frac nq\log(q!).
\]
Applying (5) proves (4). ∎

# 3. A weighted spanning-tree bound

For \(v\in B_s\), define its escape degree from the block \(B_s\) by
\[
d_s(v)=|N[v]\setminus B_s|.
\tag{6}
\]
Since \(|N[v]|=|B_s|=q\),
\[
d_s(v)=|B_s\setminus N[v]|.
\tag{7}
\]
A cross-block edge has both endpoint escape degrees between \(1\) and \(q-2\).

Let \(Q_\alpha\) be the multigraph whose vertices are the blocks \(B_s\), with one quotient edge for every edge of \(G\) joining distinct blocks. It is connected.

## Theorem 3.1: spanning-tree estimate

For every spanning tree \(\mathcal T\) of \(Q_\alpha\), where each tree edge is represented by a particular cross-block edge \(uv\) of \(G\), one has
\[
\boxed{
\frac{F(G,q)}{P(G,q)}
 \le
 \prod_{uv\in E(\mathcal T)}
 \frac{d(u)d(v)}{q(q-1)}.
}
\tag{8}
\]
Here \(d(u),d(v)\) are their escape degrees from their respective blocks.

### Proof

For a vertex \(u\in B_s\), write
\[
M_u=B_s\setminus N[u],\qquad
X_u=N[u]\setminus B_s.
\]
Both sets have size \(d_s(u)\).

If \(\beta\) is frozen, then both \(B_s\) and \(N[u]\) are rainbow. Therefore
\[
\beta(M_u)=\beta(X_u)
\tag{9}
\]
as sets of colours.

Root \(\mathcal T\) at an arbitrary block. Consider a tree edge represented by
\[
uv,\qquad u\in B_s,\quad v\in B_t,
\]
where \(B_s\) is the parent and \(B_t\) the child. Equation (9) gives the two necessary conditions
\[
\beta(v)\in\beta(M_u),
\qquad
\beta(u)\in\beta(M_v).
\tag{10}
\]

Suppose the parent permutation \(\pi_s\) is fixed. Set
\[
a=\beta(u),\qquad A=\beta(M_u).
\]
Then \(|A|=d_s(u)\), and \(a\notin A\), because \(u\notin M_u\) and \(\beta\) is injective on \(B_s\).

To choose the child permutation \(\pi_t\) subject to (10):

- the colour of \(v\) can be chosen in \(d_s(u)\) ways from \(A\);
- the preimage of \(a\) must be one of the \(d_t(v)\) vertices in \(M_v\);
- the remaining \(q-2\) colours can be assigned arbitrarily to the remaining vertices.

Thus there are exactly
\[
d_s(u)d_t(v)(q-2)!
\tag{11}
\]
possible child permutations satisfying these two necessary conditions.

Traversing the rooted tree therefore gives
\[
F(G,q)
 \le q!\prod_{uv\in E(\mathcal T)}
 d(u)d(v)(q-2)!.
\]
Using \(P(G,q)\ge(q!)^m\) and
\[
\frac{(q-2)!}{q!}=\frac1{q(q-1)}
\]
proves (8). ∎

## Corollary 3.2: bounded escape degree

If, for some frozen \(\alpha\) and some choice of its distinguished colour,
\[
d_s(v)\le D
\quad\text{for every }s\in S,\ v\in B_s,
\]
then
\[
\boxed{
\frac{F(G,q)}{P(G,q)}
 \le
 \left(\frac{D^2}{q(q-1)}\right)^{m-1}.
}
\tag{12}
\]

In particular, if \(D\le q^{1-\varepsilon}\), then for sufficiently large \(q\),
\[
\frac{F(G,q)}{P(G,q)}
 \le q^{-\varepsilon(m-1)}.
\tag{13}
\]
This has precisely the conjectured \(\exp[-\Theta((n/q)\log q)]\) exponent.

### The matching-rewired clique case

If every vertex has at most one neighbour outside its block, then \(D=1\), and (12) gives
\[
\boxed{
\frac{F(G,q)}{P(G,q)}
 \le [q(q-1)]^{-(m-1)}.
}
\tag{14}
\]

This includes graphs obtained from \(m\) copies of \(K_q\) by deleting a vertex-disjoint collection of internal edges and reconnecting the exposed endpoints between blocks in such a way that the original block colouring remains frozen.

One can also see (14) directly. For a cross edge joining the \(\alpha\)-colour-\(i\) vertex in one block to the \(\alpha\)-colour-\(j\) vertex in another, frozen colourings force the two block permutations to agree on coordinates \(i\) and \(j\). Along a spanning tree, the root permutation is arbitrary and each subsequent permutation has at most \((q-2)!\) choices.

# 4. A complementary Kempe-orbit bound

The preceding bound is strongest when the blocks are close to cliques. A different argument is much stronger when \(G\) has few adjacent true twins.

Call adjacent vertices \(x,y\) true twins if
\[
N[x]=N[y].
\]
Let
\[
T=T(G)
\]
be the number of edges whose endpoints are not true twins.

## Theorem 4.1: non-twin-edge estimate

Let
\[
L=
\begin{cases}
q-1,&q\text{ even},\\
q,&q\text{ odd}.
\end{cases}
\]
Then
\[
\boxed{
\frac{F(G,q)}{P(G,q)}
 \le
 \min\left\{1,\,
 L\,2^{-T/(2L)}
 \right\}
 \le
 \min\left\{1,\,
 q\,2^{-T/(2q)}
 \right\}.
}
\tag{15}
\]

### Proof

#### Step 1: pair the colours

There is a family of \(L\) matchings of the colour set such that every unordered pair of colours occurs in exactly one matching:

- if \(q\) is even, a one-factorization of \(K_q\);
- if \(q\) is odd, a decomposition of \(E(K_q)\) into \(q\) near-perfect matchings.

For completeness, these are supplied by the standard round-robin construction. For odd \(q\), label colours by \(\mathbb Z_q\) and let
\[
M_t=\{\{t+i,t-i\}:1\le i\le(q-1)/2\};
\]
\(M_t\) leaves \(t\) unmatched. The analogous construction on
\(\mathbb Z_{q-1}\cup\{\infty\}\) gives the even case.

Fix one such matching \(M\), containing
\[
r=\lfloor q/2\rfloor
\]
colour-pairs.

#### Step 2: the Kempe hypercube around a frozen colouring

Let \(\alpha\) be frozen. For a paired pair \(P=\{a,b\}\), the subgraph induced by the \(a\)- and \(b\)-coloured vertices is a perfect matching with \(m\) edges. On each such edge we may either retain the two colours or swap them. Doing this independently for every edge and every pair \(P\in M\) gives
\[
2^{rm}
\]
proper colourings. Operations belonging to different colour-pairs concern disjoint colour sets, so they do not create conflicts.

For a fixed \(P=\{a,b\}\), put one binary variable \(x_e\) on each of its \(m\) bichromatic edges. For every vertex \(z\) whose \(\alpha\)-colour is outside \(P\), let \(e_a(z)\) be the \(P\)-edge containing its \(a\)-coloured neighbour and \(e_b(z)\) the \(P\)-edge containing its \(b\)-coloured neighbour.

After the swaps, these two neighbours have different colours exactly when
\[
x_{e_a(z)}=x_{e_b(z)}.
\tag{16}
\]
Let \(H_P\) be the graph on the \(m\) \(P\)-edges whose non-loop edges are the equations (16). Since the zero assignment is a solution, the equations are consistent, and their solution space has size
\[
2^{c(H_P)},
\]
where isolated vertices count as components.

Constraints for distinct pairs \(P\) involve disjoint sets of variables. Consequently, the number of frozen colourings in this Kempe hypercube is exactly
\[
2^{\sum_{P\in M}c(H_P)}.
\tag{17}
\]

#### Step 3: isolated variables are precisely true-twin edges

Let \(e=xy\) be a \(P\)-edge, with \(\alpha(x)=a\), \(\alpha(y)=b\).

If \(N[x]=N[y]\), then every outside-colour vertex adjacent to \(x\) is also adjacent to \(y\). All constraints involving \(e\) are loops, so \(e\) is isolated in \(H_P\).

Conversely, suppose \(N[x]\ne N[y]\). Since \(x\) and \(y\) are adjacent, there is a vertex
\[
z\in N[x]\setminus N[y].
\]
Its \(\alpha\)-colour is outside \(\{a,b\}\): it cannot have colour \(a\), and the unique \(b\)-neighbour of \(x\) is \(y\). At \(z\), the \(a\)-neighbour belongs to \(e\), while the \(b\)-neighbour belongs to a different \(P\)-edge. Hence \(e\) is incident with a non-loop edge of \(H_P\).

Thus the nonisolated vertices of \(H_P\) correspond exactly to the non-true-twin \(P\)-edges.

Let \(A_P\) be their number. A graph with \(A_P\) nonisolated vertices has at most
\[
m-A_P+\frac{A_P}{2}
\]
components. Hence
\[
m-c(H_P)\ge\frac{A_P}{2}.
\tag{18}
\]
Writing \(A_M=\sum_{P\in M}A_P\), equations (17) and (18) show that the frozen fraction in this hypercube is at most
\[
2^{-A_M/2}.
\tag{19}
\]

#### Step 4: choose a profitable matching and double-count

For each frozen \(\alpha\), the \(L\) colour matchings partition all unordered colour-pairs. Therefore
\[
\sum_M A_M=T.
\]
Choose one \(M=M(\alpha)\) for which
\[
A_M\ge \frac TL.
\tag{20}
\]

Now form pairs \((\alpha,\beta)\), where \(\alpha\) is frozen and \(\beta\) is any of the \(2^{rm}\) colourings in the chosen Kempe hypercube. There are
\[
F(G,q)\,2^{rm}
\tag{21}
\]
such pairs.

Fix a proper colouring \(\beta\) and one matching \(M\). All frozen \(\alpha\) for which \(\beta\) belongs to the corresponding \(M\)-hypercube lie in one common pair-membership class. By (19) and (20), there are at most
\[
2^{rm-T/(2L)}
\]
such \(\alpha\). Summing over the \(L\) possible matchings, every \(\beta\) is counted at most
\[
L\,2^{rm-T/(2L)}
\]
times.

Double-counting (21) therefore yields
\[
F(G,q)2^{rm}
 \le
P(G,q)L2^{rm-T/(2L)},
\]
which is (15). ∎

# 5. Consequences

## 5.1 The conjectured scale when there are enough non-twin edges

If
\[
T\ge 2n\log_2 q,
\tag{22}
\]
then Theorem 4.1 gives
\[
\frac{F(G,q)}{P(G,q)}
 \le q\,2^{-n\log_2(q)/q}
 =q^{-(m-1)}.
\tag{23}
\]
Thus the desired exponent is proved whenever the number of non-true-twin edges is at least \(2n\log_2q\).

## 5.2 Twin-free and triangle-free graphs

If \(G\) has no adjacent true twins, then
\[
T=|E(G)|=\frac{n(q-1)}2.
\]
Consequently,
\[
\frac{F(G,q)}{P(G,q)}
 \le q\,2^{-n(q-1)/(4q)}.
\tag{24}
\]
This is exponentially small in \(n\), much stronger than the sought
\(\exp[-\Theta((n/q)\log q)]\) bound.

In particular, apart from the complete graph at very small parameters, triangle-free graphs have no adjacent true twins, so (24) applies.

## 5.3 Exact check for \(\Delta=2\)

Here \(q=3\). A connected graph admitting a frozen \(3\)-colouring must be a cycle \(C_{3m}\). There are exactly six frozen colourings: after the colours on one edge are chosen, the colouring is forced periodically.

The number of proper \(3\)-colourings is
\[
P(C_{3m},3)=2^{3m}+2(-1)^m.
\]
Hence, for \(m\ge2\),
\[
\mathbb P(\text{frozen})
 =\frac6{2^{3m}+2(-1)^m}.
\tag{25}
\]
This is exponentially small in \(n\).

The spanning-tree bound also gives the weaker but uniform estimate
\[
\mathbb P(\text{frozen})\le 6^{-(m-1)},
\]
because every cross-block endpoint has escape degree \(1\).

# 6. What remains

Equality of closed neighbourhoods is an equivalence relation. Each true-twin class \(C\) is a clique. If \(G\ne K_q\) is connected, then
\[
|C|\le q-2.
\tag{26}
\]
Indeed, a class of size \(q\) is a \(K_q\)-component. If \(|C|=q-1\), the common remaining neighbour is adjacent to all of \(C\), has no other neighbours, and therefore has the same closed neighbourhood, contradicting maximality of \(C\).

Every vertex in a true-twin class \(C\) has exactly \(q-|C|\) neighbours outside \(C\), all of which are non-twin edges. Thus
\[
2T=\sum_{v\in V(G)}\bigl(q-|C(v)|\bigr).
\tag{27}
\]

Consequently, if a graph were to violate the target estimate
\[
\frac{F(G,q)}{P(G,q)}\le q^{-(m-1)},
\]
Theorem 4.1 forces
\[
T<2n\log_2 q.
\tag{28}
\]
Equation (27) then implies that almost all vertices lie in very large true-twin cliques. More precisely, for every \(r>0\),
\[
\#\{v: |C(v)|\le q-r\}
 \le \frac{2T}{r}
 <\frac{4n\log_2q}{r}.
\tag{29}
\]

There is also a direct link with the escape parameter. If the centre \(s\) of a block \(B_s=N[s]\) lies in a true-twin class of size \(q-r\), then
\[
d_s(v)\le r-1
\quad\text{for every }v\in B_s.
\tag{30}
\]
Indeed, every \(v\in B_s\setminus C(s)\) is adjacent to all \(q-r\) vertices of \(C(s)\), and \(v\) itself also belongs to \(N[v]\cap B_s\).

Thus Theorem 3.1 settles the case in which one can choose a frozen colour class whose block centres all belong to twin classes of size at least \(q-q^{1-\varepsilon}\).

The unresolved configuration is therefore quite narrow:

- \(T=O(n\log q)\), so almost all vertices lie in large true-twin cliques;
- nevertheless, every useful block decomposition has a small number of badly damaged connector blocks with escape degree \(q^{1-o(1)}\);
- the weighted quotient graph has no spanning tree for which
  \[
  \sum_{uv\in E(\mathcal T)}
  \log\frac{q(q-1)}{d(u)d(v)}
  =\Omega(m\log q).
  \]

The arguments above do not rule out such a configuration and do not prove that it has sufficiently many nonfrozen colourings by another mechanism. That is the remaining gap, so the universal conjectured exponent is not proved here.