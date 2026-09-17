```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Closure holds when one summand is an oriented tree with at most one vertex of in-degree at least two; for arbitrary summands, an explicit maximum-in-degree condition also suffices.",
  "would_publish": false,
  "caveats": "This does not resolve Conjecture 7; novelty of the partial results below has not been established."
}
```

# Partial results on closure under disjoint union

All digraphs below are finite and loopless, with no parallel arcs; opposite arcs are allowed. Subdivisions are ordinary, not induced, subdigraphs.

A **forcing threshold** for \(F\) is an integer \(m\) such that every digraph of minimum out-degree at least \(m\) contains an \(F\)-subdivision. Thus \(F\) is \(\delta^+\)-maderian precisely when it has a finite forcing threshold.

The general conjecture is not settled here. I prove:

1. an actual closure theorem when one summand belongs to a class of oriented trees;
2. a sufficient condition for arbitrary summands that implies an exponential lower bound on the maximum in-degree of any counterexample.

## 1. Adjoining a tree with at most one in-branching vertex

### Theorem 1

Let \(F\) have forcing threshold \(m\), and let \(T\) be an oriented tree on \(t\geq 1\) vertices with at most one vertex of in-degree at least two. Then
\[
F\mathbin{\dot\cup}T
\]
is \(\delta^+\)-maderian. More precisely, a forcing threshold is
\[
\boxed{\max\left\{m+t,\binom{t}{2}+1\right\}.}
\]

This includes out-arborescences and inward-directed spiders, with arbitrary outward-directed trees attached to their vertices.

The proof uses bounded-order copies rather than arbitrary subdivisions.

### 1.1. A bounded-copy deletion lemma

Suppose every digraph of minimum out-degree at least \(b\) contains \(H\) **as a subgraph**, where \(h=|V(H)|\). If \(F\) has forcing threshold \(m\), then
\[
\max\{b,m+h\}
\tag{1}
\]
is a forcing threshold for \(F\dot\cup H\).

Indeed, find an \(H\)-copy and delete its \(h\) vertices. Every remaining vertex loses at most \(h\) out-neighbours, so the remaining digraph has minimum out-degree at least \(m\). It contains an \(F\)-subdivision disjoint from the \(H\)-copy. The degree bound also guarantees that the remaining digraph is nonempty.

The substantive point is therefore to force the trees in Theorem 1 as actual subgraphs.

### 1.2. A bounded-copy lemma for inward spiders

An **inward spider** consists of a centre \(c\) and otherwise vertex-disjoint directed paths ending at \(c\).

#### Lemma 2

Every inward spider on \(s\geq 2\) vertices occurs as a subgraph of every digraph \(D\) satisfying
\[
\delta^+(D)\geq \binom{s}{2}+1.
\]

#### Proof

Put
\[
d=\binom{s}{2}+1.
\]
Retain exactly \(d\) outgoing arcs at each vertex of \(D\), and then take a sink strongly connected component. The resulting digraph \(G\) is strongly connected and \(d\)-out-regular.

Let \(P\) be the transition matrix of the uniform outgoing random walk on \(G\). Thus every nonzero entry of \(P\) is \(1/d\). For every \(j\geq 1\),
\[
P^j(x,y)
=\sum_z P^{j-1}(x,z)P(z,y)
\leq \frac1d.
\tag{2}
\]

Let \(\pi\) be a positive stationary distribution, and choose \(r\) with \(\pi_r\) maximum. Define the time-reversed transition matrix
\[
Q(x,y)=\frac{\pi_yP(y,x)}{\pi_x}.
\]
Stationarity makes \(Q\) stochastic, and
\[
Q^j(x,y)=\frac{\pi_yP^j(y,x)}{\pi_x}.
\]
Consequently, for every \(j\geq 1\),
\[
Q^j(r,y)\leq \frac1d,
\qquad
Q^j(x,x)=P^j(x,x)\leq \frac1d.
\tag{3}
\]

For completeness, existence of \(\pi\) follows by taking a limit point of Cesàro averages of a probability distribution under \(P\); strong connectivity makes every entry positive.

Write the leg lengths of the spider as \(\ell_1,\dots,\ell_k\). Independently run \(Q\)-walks of these lengths, all starting at \(r\). Map the centre to \(r\), and map the vertex at distance \(j\) from the centre on leg \(i\) to the \(j\)-th state of walk \(i\).

This is an arc-preserving map: a \(Q\)-transition from \(x\) to \(y\) means that \(y\to x\) is an arc of \(G\), as required for a leg directed towards its centre.

For every pair of distinct spider vertices, the probability that their images coincide is at most \(1/d\):

- For two vertices on the same leg, condition on the earlier walk state and use \(Q^j(x,x)\leq 1/d\).
- For the centre and another vertex, use \(Q^j(r,r)\leq 1/d\).
- For vertices on different legs, the walks are independent, and each relevant marginal distribution has every atom at most \(1/d\), by (3).

Thus the union bound gives
\[
\Pr(\text{the map is not injective})
\leq \frac{\binom{s}{2}}{d}<1.
\]
An injective arc-preserving map therefore exists. Its image is the required subgraph. \(\square\)

### 1.3. Proof of Theorem 1

First I show that \(T\) occurs as a subgraph whenever
\[
\delta^+(D)\geq \binom{t}{2}+1.
\tag{4}
\]

If every vertex of \(T\) has in-degree at most one, then \(T\) is an out-arborescence. It embeds greedily under the weaker condition \(\delta^+(D)\geq t-1\): process vertices in parent-before-child order, choosing an unused out-neighbour for each new child.

Otherwise let \(r\) be the unique vertex of \(T\) with in-degree at least two. Every component of \(T-r\) is an out-arborescence. In each component whose edge to \(r\) points towards \(r\), take the directed path from that component's root to \(r\). The union of these paths is an inward spider \(S\), with centre \(r\).

Everything outside \(S\) is a collection of out-arborescences attached to vertices of \(S\). By Lemma 2, condition (4) supplies a subgraph copy of \(S\). Extend it greedily through the attached out-arborescences. At each extension step, at most \(t-2\) used vertices can block out-neighbours of the parent, while
\[
\delta^+(D)\geq \binom{t}{2}+1\geq t-1.
\]
Hence every extension is possible, giving a subgraph copy of \(T\).

Apply the deletion lemma (1), with \(H=T\) and \(b=\binom{t}{2}+1\), to finish the proof. \(\square\)

In particular, this result can be iterated to adjoin any finite disjoint union of trees of the stated type to an arbitrary \(\delta^+\)-maderian digraph.

## 2. Arbitrary summands when maximum in-degree is controlled

For arbitrary \(F_1,F_2\), a local-lemma argument gives a quantitative host condition.

### Theorem 3

Let \(m_1,m_2\geq 1\) be forcing thresholds for \(F_1,F_2\), respectively. Let
\[
d=\delta^+(D),\qquad \Delta=\Delta^-(D),
\]
and suppose \(d\geq m_1+m_2\). Define
\[
A_d=
\sum_{j=0}^{m_1-1}\binom dj+
\sum_{j=0}^{m_2-1}\binom dj.
\]
If
\[
\boxed{e(d\Delta+1)A_d\leq 2^d,}
\tag{5}
\]
then \(D\) contains a subdivision of \(F_1\dot\cup F_2\).

#### Proof

For each vertex \(v\), choose a set \(N_v\subseteq N_D^+(v)\) of exactly \(d\) vertices. Independently colour every vertex red or blue, each with probability \(1/2\).

Let \(E_v\) be the event that \(N_v\) contains fewer than \(m_1\) red vertices or fewer than \(m_2\) blue vertices. Binomial tails give
\[
\Pr(E_v)\leq p:=2^{-d}A_d.
\tag{6}
\]

The event \(E_v\) depends only on the colours in \(N_v\). Each colour variable occurs in at most \(\Delta\) of these events. Therefore an event shares variables with at most \(d\Delta\) other events.

The symmetric Lovász local lemma guarantees a colouring avoiding every \(E_v\) when
\[
ep(d\Delta+1)\leq 1,
\]
which is exactly (5).

In such a colouring, every vertex has at least \(m_1\) red out-neighbours and at least \(m_2\) blue out-neighbours. Both colour classes are nonempty, and their induced digraphs have minimum out-degrees at least \(m_1\) and \(m_2\), respectively. They contain the required vertex-disjoint subdivisions. \(\square\)

### Consequences for a potential counterexample

Suppose \(D\) does **not** contain an \((F_1\dot\cup F_2)\)-subdivision and \(d\geq m_1+m_2\). Theorem 3 implies
\[
\boxed{\Delta^-(D)>
\frac{2^d}{e\,d\,A_d}-\frac1d.}
\tag{7}
\]

Writing \(m=\max\{m_1,m_2\}\), the elementary estimate
\[
A_d\leq 2m\,d^{m-1}
\]
yields the explicit weaker bound
\[
\boxed{\Delta^-(D)>
\frac{2^d}{2em\,d^m}-\frac1d.}
\tag{8}
\]

Thus, for fixed summands, any counterexample of sufficiently large minimum out-degree must have maximum in-degree exponential in that minimum out-degree, up to a polynomial factor.

In particular, the union conclusion holds for hosts satisfying
\[
\Delta^-(D)\leq C\bigl(\delta^+(D)\bigr)^a
\]
for fixed \(C,a\), once \(\delta^+(D)\) is sufficiently large. This includes regular digraphs of sufficiently large degree.

The same colouring calculation, using only the union bound, also shows that any obstruction must satisfy
\[
|V(D)|\geq \frac{2^d}{A_d}.
\tag{9}
\]

## 3. Why these arguments do not settle the conjecture

Theorem 1 relies on finding the first summand on a bounded number of vertices. That approach cannot simply be extended to all the in-arborescences in the source paper.

Here is an explicit obstruction to such a bounded-order argument.

Fix \(d\geq 3\) and \(L\geq 1\). Construct \(D_{d,L}\) as follows:

- take \(d\) distinct vertices called hubs;
- from each hub grow a disjoint full \(d\)-ary out-tree of depth \(L\);
- from every leaf add an arc to every hub.

Then
\[
\delta^+(D_{d,L})=d.
\]
Every non-hub has in-degree exactly one, while every hub has in-degree \(d^{L+1}\).

Let \(B\) be the binary in-arborescence of height two: its root has two children, and each child has two incoming leaves. In any \(B\)-subdivision in \(D_{d,L}\), the root and its two children must all be represented by hubs, since they have in-degree two in the subdivision.

But every directed path from one hub to a distinct hub has length at least \(L+1\). Consequently every \(B\)-subdivision has at least \(L+2\) vertices. Since \(L\) is arbitrary, no bounded-order version of the deletion argument is available for this pattern, even at arbitrarily large fixed minimum out-degree.

This construction also illustrates the limitation of Theorem 3:
\[
\Delta^-(D_{d,L})=d^{L+1}
\]
is unbounded with \(L\), while \(\delta^+=d\) stays fixed. A lower bound on minimum out-degree alone does not imply (5).

These examples are limitations of the methods, not proposed counterexamples to Conjecture 7. The unresolved task is to handle two arbitrary \(\delta^+\)-maderian summands without either a bounded-copy property or a maximum-in-degree restriction.