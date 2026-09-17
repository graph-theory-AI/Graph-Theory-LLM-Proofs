Attack the following open graph-theory problem.

Catalog id: the_bermond_thomassen_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/the_bermond_thomassen_conjecture/
Original entry: http://www.openproblemgarden.org/op/the_bermond_thomassen_conjecture
Problem attributed to: Bermond, Jean-Claude, Thomassen, Carsten (posted 2007-10-01)

=== Problem statement (OpenProblemGarden) ===
Title: The Bermond-Thomassen Conjecture
Conjecture For every positive integer $ k $ , every digraph with minimum out-degree at least $ 2k-1 $ contains $ k $ disjoint cycles.

=== Discussion / context (OpenProblemGarden) ===
This conjecture is a simple observation when $ k=1 $ . It was proved by Thomassen~[Tho83] in 1983 when $ k=2 $ , and more recently the case $ k=3 $ was settled~[LPS07]. The bound offered would be optimal — just consider a symmetric complete graph on $ 2k-1 $ vertices. In 1996, Alon~[Alo96] proved that the statement is true with $ 2k-1 $ replaced by $ 64k $ . The conjecture was also verified for tournaments of minimum in-degree at least $ 2k-1 $ ~[BLS07]. Bang-Jensen et al. [BBT] made a stronger conjecture for digraph with sufficiently large girth. Conjecture For every integer $ g >1 $ , every digraph $ D $ with girth at least $ g $ and with minimum out-degree at least $ \frac{g}{g-1}k $ contains $ k $ disjoint cycles. The constant $ \frac{g}{g-1} $ is best possible. Indeed, for every integers $ p $ and $ g $ , consider the digraph $ D(g,p) $ on $ n = p(g − 1) + 1 $ vertices with vertex set $ \{x_1, \dots , x_n\} $ and arc set $ \{x_ix_j : j − i \mod n \in \{1,\dots p\}\} $ . It has girth $ g $ and out-degree $ p = \left \lfloor \frac{g}{g−1} k \right \rfloor $ . Moreover, for $ n = 0 \mod g $ , the digraph $ D(g,p) $ admits a partition into $ k $ vertex disjoint 3-cycles and no more. For g = 3, the first case of this conjecture which differs from Bermond-Thomassen Conjecture and which is not already known corresponds to the following question: Question Does every digraph D without 2-cycles and out-degree at least 6 admit four vertex disjoint cycles?

=== References listed by OpenProblemGarden ===
- [Alo96] N. Alon: Disjoint directed cycles, J. Combin. Theory Ser. B, 68(2):167--178, 1996. PDF
- [BBT] J. Bang-Jensen, S. Bessy and S. Thomassé, Disjoint 3-cycles in tournaments: a proof of the Bermond-Thomassen conjecture for tournaments, J. Graph Theory, to appear.
- *[BeTh81] J.-C. Bermond and C.~Thomassen: Cycles in digraphs---a survey, J. Graph Theory, 5(1):1--43, 1981. MathSciNet
- [BLS07] S.~Bessy, N.~Lichiardopol, and J.-S. Sereni: Two proofs of the {B}ermond-{T}homassen conjecture for tournaments with bounded minimum in-degree, Discrete Math., Special Issue dedicated to CS06, to appear.
- [LPS07] N.~Lichiardopol, A.~ P\'or, and J.-S. Sereni: A step towards the Bermond-Thomassen conjecture about disjoint cycles in digraphs, Submitted, 2007.
- [Tho83] C.~Thomassen, Disjoint cycles in digraphs, Combinatorica, 3(3-4):393--396, 1983. MathSciNet

=== Catalog page (statement + literature review) ===
The Bermond-Thomassen Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The Bermond-Thomassen conjecture ($\delta^+(D) \geq 2k-1 \Rightarrow k$ disjoint cycles) remains open for general digraphs with $k \geq 4$. Significant post-2007 advances include a new shorter proof for $k=3$ (Bai and Manoussakis, 2018) and verification for triangle-free multipartite and 3-partite tournaments (Gutin et al., 2023). Notably, the stronger conjecture of Bang-Jensen, Bessy, and Thomassé on girth conditions (listed in the OPG discussion) was disproved by Bai and Manoussakis (2018).

 Cited literature (4)

 
 
 
partial On the number of vertex-disjoint cycles in digraphs
 (2018)
 

 
 Yandong Bai, Yannis Manoussakis · arXiv preprint · arXiv:1805.02999

Provides a new shorter proof of the Bermond-Thomassen conjecture for $k=3$, and disproves the stronger Bang-Jensen--Bessy--Thomassé conjecture on girth-conditioned vertex-disjoint cycles.
 

 
 
partial Two disjoint cycles in digraphs
 (2022)
 

 
 Mikołaj Lewandowski, Joanna Polcyn, Christian Reiher · arXiv preprint · arXiv:2205.10826

Characterises all outdegree sequences forcing $k$ vertex-disjoint cycles for $k \leq 2$, giving a complete answer for the two-cycle case that strengthens the Bermond-Thomassen bound.
 

 
 
partial Note on Disjoint Cycles in Multipartite Tournaments
 (2023)
 

 
 Gregory Gutin, Wei Li, Shujing Wang, Anders Yeo, Yacong Zhou · arXiv preprint · arXiv:2311.13369

Verifies the Bermond-Thomassen conjecture for the special classes of triangle-free multipartite tournaments and 3-partite tournaments.
 

 
 
partial Vertex-disjoint cycles of different lengths in tournaments
 (2024)
 

 
 Yandong Bai, Wenpei Jia · arXiv preprint · arXiv:2403.03692

Proves that every tournament with minimum outdegree $\geq 2k-1$ ($k \geq 5$) contains $k$ disjoint cycles with at least three of different lengths, a variant of the Bermond-Thomassen problem in the tournament setting.
 

 

 Reviewer notes. The conjecture is open for $k \geq 4$ in general digraphs. The Bang-Jensen--Bessy--Thomassé stronger conjecture (mentioned in the OPG discussion) was disproved by Bai--Manoussakis 2018. Publication venue details for arXiv papers could not be verified from fetches alone; all are listed as preprints. The 2022 Lewandowski--Polcyn--Reiher and 2023 Gutin et al. papers may have appeared in journals by now but this was not confirmed.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 03) (web search enabled).
 

Conjecture. For every positive integer $ k $ , every digraph with minimum out-degree at least $ 2k-1 $ contains $ k $ disjoint cycles.

Keywords:
cycles

Discussion

This conjecture is a simple observation when $ k=1 $ . It was proved by Thomassen~[Tho83] in 1983 when $ k=2 $ , and more recently the case $ k=3 $ was settled~[LPS07]. The bound offered would be optimal — just consider a symmetric complete graph on $ 2k-1 $ vertices. In 1996, Alon~[Alo96] proved that the statement is true with $ 2k-1 $ replaced by $ 64k $ . The conjecture was also verified for tournaments of minimum in-degree at least $ 2k-1 $ ~[BLS07]. Bang-Jensen et al. [BBT] made a stronger conjecture for digraph with sufficiently large girth. Conjecture For every integer $ g >1 $ , every digraph $ D $ with girth at least $ g $ and with minimum out-degree at least $ \frac{g}{g-1}k $ contains $ k $ disjoint cycles. The constant $ \frac{g}{g-1} $ is best possible. Indeed, for every integers $ p $ and $ g $ , consider the digraph $ D(g,p) $ on $ n = p(g − 1) + 1 $ vertices with vertex set $ \{x_1, \dots , x_n\} $ and arc set $ \{x_ix_j : j − i \mod n \in \{1,\dots p\}\} $ . It has girth $ g $ and out-degree $ p = \left \lfloor \frac{g}{g−1} k \right \rfloor $ . Moreover, for $ n = 0 \mod g $ , the digraph $ D(g,p) $ admits a partition into $ k $ vertex disjoint 3-cycles and no more. For g = 3, the first case of this conjecture which differs from Bermond-Thomassen Conjecture and which is not already known corresponds to the following question: Question Does every digraph D without 2-cycles and out-degree at least 6 admit four vertex disjoint cycles?

Bibliography

 [Alo96]
 N. Alon: Disjoint directed cycles, J. Combin. Theory Ser. B, 68(2):167--178, 1996. PDF
 PDF

 [BBT]
 J. Bang-Jensen, S. Bessy and S. Thomassé, Disjoint 3-cycles in tournaments: a proof of the Bermond-Thomassen conjecture for tournaments, J. Graph Theory, to appear.

★ [BeTh81]
 J.-C. Bermond and C.~Thomassen: Cycles in digraphs---a survey, J. Graph Theory, 5(1):1--43, 1981. MathSciNet
 MathSciNet

 [BLS07]
 S.~Bessy, N.~Lichiardopol, and J.-S. Sereni: Two proofs of the {B}ermond-{T}homassen conjecture for tournaments with bounded minimum in-degree, Discrete Math., Special Issue dedicated to CS06, to appear.

 [LPS07]
 N.~Lichiardopol, A.~ P\'or, and J.-S. Sereni: A step towards the Bermond-Thomassen conjecture about disjoint cycles in digraphs, Submitted, 2007.

 [Tho83]
 C.~Thomassen, Disjoint cycles in digraphs, Combinatorica, 3(3-4):393--396, 1983. MathSciNet
 MathSciNet

Related conjectures

 
 related to
 Splitting a digraph with minimum outdegree constraints
 partial
 The OPG context explicitly states only a case-level equivalence: the d=1 case of the splitting problem (Thomassen's f(1)=3) is equivalent to the k=2 case of Bermond-Thomassen (min outdegree 3 gives 2 disjoint cycles); indeed a bipartition with both parts of min outdegree >=1 yields two disjoint cycles, and conversely per Thomassen. But the full statements do not imply each other: for general d, splitting into two parts of min outdegree d says nothing about packing k disjoint cycles under the specific 2k-1 bound, and k disjoint cycles do not yield an outdegree-preserving bipartition. The problems are thematically linked with one coinciding special case, so related_only.
 

 View in the relation graph
 — relations are AI-reviewed, not formally verified.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sharp digon-matching bound proves the conjecture for k≥4 when n=2k+s, s≤k+2, and s(s+1)<28(k−2), using the established k=3 case.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not resolved; novelty of this elementary order-restricted consequence has not been checked."
}
```

## 1. Results obtained

All digraphs below are finite, loopless, and have no parallel arcs. Cycles are directed and vertex-disjoint. A **digon** is a directed cycle of length two.

The main positive result of this attack is the following order-restricted case.

**Theorem 1.** Let \(k\ge 4\), and let \(D\) have
\[
|V(D)|=2k+s,\qquad \delta^+(D)\ge 2k-1,
\]
where \(s\ge0\) is an integer. If
\[
\boxed{\quad s\le k+2,\qquad s(s+1)<28(k-2),\quad}
\]
then \(D\) contains \(k\) vertex-disjoint directed cycles.

This uses the established \(k=3\) case stated in the question. Without using that result, the same method proves:

**Theorem 2.** For \(k\ge2\), the conclusion holds under the conditions
\[
\boxed{\quad s\le k,\qquad s(s+1)<12(k-1).\quad}
\]

The mechanism is to force sufficiently many disjoint digons, delete them, and apply the \(k=3\) or \(k=1\) case to the remainder. I give an exact extremal calculation for this mechanism.

I also give an explicit high-girth sharpness family. In particular, it supplies a 49-vertex negative answer to the auxiliary question about minimum outdegree six and four cycles. It is **not** a counterexample to Bermond–Thomassen.

## 2. A sharp bound for packing digons

For a digraph \(D\), define its **digon graph** \(G\): it has vertex set \(V(D)\), with
\[
uv\in E(G)\quad\Longleftrightarrow\quad uv,vu\in A(D).
\]
Matchings in \(G\) are precisely collections of vertex-disjoint digons in \(D\).

### Proposition 3

Let \(r\ge0\) and \(n\ge2r+2\). Put
\[
A(n,r)=\frac{(n-2r-1)(n+2r)}{2n},
\qquad
B(n,r)=\frac{n-r-1}{2}.
\]
Among all \(n\)-vertex digraphs having no \(r+1\) vertex-disjoint digons, the largest possible minimum outdegree is
\[
\boxed{
n-1-\left\lceil\min\{A(n,r),B(n,r)\}\right\rceil.
}
\tag{1}
\]

Consequently, if
\[
\delta^+(D)\ge n-1-s
\quad\text{and}\quad
s<\min\{A(n,r),B(n,r)\},
\tag{2}
\]
then \(D\) has \(r+1\) vertex-disjoint digons.

### Proof of the upper bound

Suppose that the digon graph \(G\) has matching number at most \(r\), and that every vertex of \(D\) is missing at most \(s\) outgoing arcs.

By the Tutte–Berge formula, there is a set \(S\subseteq V(G)\) such that, writing
\[
a=|S|,\qquad m=n-a,\qquad q=o(G-S),
\]
we have
\[
q\ge n-2r+a.
\tag{3}
\]
Here \(o(G-S)\) denotes the number of odd components of \(G-S\). Since \(q\le n-a\), equation (3) implies \(0\le a\le r\).

Every pair of vertices in different components of \(G-S\) is a nonedge of \(G\), so at least one of the two corresponding directed arcs is missing from \(D\).

The number of pairs in different components is at least
\[
(q-1)\left(m-\frac q2\right).
\tag{4}
\]
Indeed, merge any even components into one of the odd components. Among partitions of \(m\) vertices into \(q\) nonempty groups, the number of cross-pairs is minimized when \(q-1\) groups are singletons and the remaining group has size \(m-q+1\).

On the other hand, at most \(sm\) directed arcs with both endpoints in \(V(D)\setminus S\) are missing. Thus
\[
(q-1)\left(m-\frac q2\right)\le sm.
\tag{5}
\]
The expression on the left is increasing in the integer \(q\) for \(1\le q\le m\). Substituting the lower bound from (3) therefore yields
\[
\frac{(n-2r+a-1)(n+2r-3a)}2\le s(n-a).
\tag{6}
\]

Define
\[
F(a)=\frac{(n-2r+a-1)(n+2r-3a)}2-s(n-a).
\]
This is a concave quadratic in \(a\), with coefficient \(-3/2\) on \(a^2\). Its endpoint values are
\[
F(0)=n\bigl(A(n,r)-s\bigr),
\]
and
\[
F(r)=(n-r)\bigl(B(n,r)-s\bigr).
\]
If \(s<\min\{A(n,r),B(n,r)\}\), both endpoint values are positive. Concavity gives \(F(a)>0\) throughout \(0\le a\le r\), contradicting (6). This also covers \(r=0\), when the interval consists of one point.

Taking \(s=n-1-\delta^+(D)\), which is an integer, proves the upper bound in (1).

### Sharpness

I include the constructions because they identify exactly where the digon method stops.

We use the following elementary orientation fact:

> An undirected graph \(H\) has an orientation with maximum outdegree at most an integer \(p\ge0\) if and only if
> \[
> e(H[W])\le p|W|
> \quad\text{for every }W\subseteq V(H).
> \tag{7}
> \]

For sufficiency, assign each edge to one of its endpoints, with capacity \(p\) at each vertex, and orient the edge away from its assigned endpoint. Hall’s theorem gives such an assignment: any set \(F\) of edges satisfies
\[
|F|\le e(H[V(F)])\le p|V(F)|.
\]
Necessity follows by counting tails of edges inside \(W\).

Now choose an undirected graph \(G\), let \(H=\overline G\), and orient \(H\). Construct \(D\) by:

* putting both arcs on every edge of \(G\);
* for every oriented edge \(u\to v\) of \(H\), putting \(v\to u\), but not \(u\to v\), in \(D\).

Then \(G\) is exactly the digon graph of \(D\), and
\[
d_D^+(v)=n-1-d_{\vec H}^+(v).
\tag{8}
\]

There are two extremal choices.

**First construction.** Let \(G\) consist of \(K_{2r+1}\) and \(n-2r-1\) isolated vertices. Its matching number is \(r\).

Its complement \(H\) has a clique of size \(n-2r-1\), an independent set of size \(2r+1\), and all edges between them. Its maximum induced-subgraph density is
\[
\max_{\varnothing\ne W\subseteq V(H)}
\frac{e(H[W])}{|W|}=A(n,r).
\]
To check this, a subset containing \(t\) clique vertices and \(b\) independent vertices has density
\[
\frac{\binom t2+tb}{t+b},
\]
which is nondecreasing when either \(t\) or \(b\) increases. Thus (7) supplies an orientation with maximum outdegree at most \(\lceil A(n,r)\rceil\).

**Second construction.** Let
\[
G=K_r\vee \overline K_{n-r}.
\]
Its matching number is \(r\), since its \(K_r\) is a vertex cover and can be matched into the independent set.

Here \(H\) consists of \(K_{n-r}\) and \(r\) isolated vertices. Its maximum induced-subgraph density is \(B(n,r)\), so it has an orientation with maximum outdegree at most \(\lceil B(n,r)\rceil\).

Using whichever construction has the smaller density, equation (8) gives minimum outdegree at least the value in (1). Together with the upper bound, this proves the exact formula. \(\square\)

## 3. Deducing the order-restricted cases

Let
\[
n=2k+s,\qquad \delta^+(D)\ge2k-1=n-1-s.
\]

Take \(b\in\{1,3\}\), with \(k\ge b+1\), and set
\[
r=k-b-1.
\]
Proposition 3 forces \(k-b\) disjoint digons whenever
\[
s<A(n,r),\qquad s<B(n,r).
\]

The two inequalities simplify as follows:
\[
A(n,r)-s
=
\frac{2(2b+1)(2k-b-1)-s(s+1)}{2n},
\tag{9}
\]
and
\[
B(n,r)-s=\frac{k+b-s}{2}.
\tag{10}
\]
Thus it suffices that
\[
s\le k+b-1,
\qquad
s(s+1)<2(2b+1)(2k-b-1).
\tag{11}
\]

Delete the vertices of the resulting \(k-b\) digons. In the remaining induced digraph \(D'\),
\[
\delta^+(D')
\ge (2k-1)-2(k-b)
=2b-1.
\tag{12}
\]

* For \(b=1\), every finite digraph of positive minimum outdegree contains a directed cycle: follow outgoing arcs until a vertex repeats. This supplies the last cycle. Conditions (11) become
  \[
  s\le k,\qquad s(s+1)<12(k-1),
  \]
  proving Theorem 2.

* For \(b=3\), apply the established three-cycle theorem stated in the question to \(D'\), whose minimum outdegree is at least five. Conditions (11) become
  \[
  s\le k+2,\qquad s(s+1)<28(k-2),
  \]
  proving Theorem 1.

All cycles in \(D'\) avoid the previously deleted digons, so the resulting packing has exactly the required \(k\) members. \(\square\)

The sharper window allows an order surplus \(s\) of approximately \(\sqrt{28k}\). This is an order-restricted result, not an improvement to the general minimum-outdegree bound.

## 4. Explicit sharpness examples of arbitrarily large directed girth

The discussion’s girth strengthening cannot circumvent the obstruction at outdegree \(2k-2\). Here is a self-contained construction.

Fix \(k\ge2\) and \(L\ge2\), and put
\[
q=2k-1,\qquad d=2k-2.
\]
Take \(q\) distinguished vertices
\[
X=\{x_1,\ldots,x_q\}.
\]
For every \(i\), introduce \(L-1\) disjoint sets
\[
Y_{i,1},\ldots,Y_{i,L-1},
\]
each of size \(d\). Put in precisely these arcs:

1. \(x_i\to y\) for every \(y\in Y_{i,1}\);
2. all arcs from \(Y_{i,j}\) to \(Y_{i,j+1}\), for \(1\le j<L-1\);
3. \(y\to x_h\) for every \(y\in Y_{i,L-1}\) and every \(h\ne i\).

Call the resulting digraph \(D_{k,L}\).

### Degree and girth

Every vertex has outdegree exactly \(d=2k-2\).

Every directed cycle visits \(X\). Between consecutive visits to \(X\), it traverses exactly \(L\) arcs. A traversal beginning at \(x_i\) cannot return immediately to \(x_i\), so every cycle visits at least two vertices of \(X\). Conversely, any two distinct distinguished vertices support a cycle of length \(2L\). Therefore
\[
g(D_{k,L})=2L.
\tag{13}
\]

### Exact cycle-packing number

Every cycle consumes at least two vertices of the set \(X\), which has size \(2k-1\). Hence
\[
\nu_{\mathrm{cyc}}(D_{k,L})\le k-1.
\]
Pairing \(2k-2\) of the distinguished vertices and taking one \(2L\)-cycle for each pair attains this bound. Thus
\[
\boxed{
\delta^+(D_{k,L})=2k-2,\quad
g(D_{k,L})=2L,\quad
\nu_{\mathrm{cyc}}(D_{k,L})=k-1.
}
\tag{14}
\]

In particular, the necessary outdegree threshold cannot be lowered below \(2k-1\), even under an arbitrarily large prescribed lower bound on directed girth.

### The auxiliary four-cycle question

Take \(k=4\) and \(L=2\). There are seven distinguished vertices and six additional vertices for each distinguished vertex, for a total of
\[
7(1+6)=49
\]
vertices. Explicitly, its arcs are
\[
x_i\to y_{i,j},
\qquad
y_{i,j}\to x_h\quad(h\ne i),
\]
where \(1\le i,h\le7\) and \(1\le j\le6\).

This is an oriented bipartite digraph with minimum outdegree six and directed girth four. Every cycle uses at least two of the seven distinguished vertices, so it has no four vertex-disjoint cycles.

This answers the auxiliary question negatively. The supplied catalog already reports failure of the stronger girth conjecture; I make no novelty claim for this construction.

## 5. What remains unresolved

The exact calculation in Proposition 3 concerns **digons**, not arbitrary directed cycles. Outside the stated order windows, sufficiently many digons need not exist. In particular, oriented digraphs have no digons at all, so this mechanism does not address the central unrestricted difficulty.

The high-girth examples have minimum outdegree \(2k-2\), one below the conjectured threshold. They establish necessity, not a counterexample at \(2k-1\).

Thus the Bermond–Thomassen conjecture itself remains unresolved by this attack. The proved progress here is the order-restricted positive result and the exact auxiliary extremal calculation; their novelty has not been established.
