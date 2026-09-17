Attack the following open graph-theory problem.

Catalog id: list_hadwiger_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/list_hadwiger_conjecture/
Original entry: http://www.openproblemgarden.org/op/list_hadwiger_conjecture
Problem attributed to: Kawarabayashi, Ken-ichi, Mohar, Bojan (posted 2014-07-07)

=== Problem statement (OpenProblemGarden) ===
Title: List Hadwiger Conjecture
Conjecture Every $ K_t $ -minor-free graph is $ c t $ -list-colourable for some constant $ c\geq1 $ .

=== Discussion / context (OpenProblemGarden) ===
Hadwiger's conjecture asserts that every $ K_t $ - minor -free graph is $ (t − 1) $ -colourable. Robertson, Seymour and Thomas [RST] proved Hadwiger's conjecture for $ t \leq 6 $ . It remains open for $ t \geq 7 $ . In fact, it is open whether every $ K_t $ -minor-free graph is $ ct $ -colourable for some constant $ c\geq 1 $ . It is natural to consider analogous problems for list colourings . First, consider planar graphs. While every planar graph is 4-colourable, Erdös, Rubin and Taylor. [ERT] conjectured that some planar graph is not 4-list-colourable, and that every planar graph is 5-list-colourable. The first conjecture was verified by Voigt [V] and the second by Thomassen [T]. More generally, Borowiecki [B] asked whether every $ K_t $ -minor-free graph is $ (t − 1) $ -list-colourable, which is true for $ t \leq 4 $ but false for $ t = 5 $ by Voigt’s example. Kawarabayashi and Mohar [KM] proposed the stated conjecture, and suggested it might be true with $ c=\frac{3}{2} $ . Barát, Joret and Wood [BJW] proved that $ c\geq\frac{4}{3} $ . In particular, they constructed a $ K_{3t+2} $ -minor-free graph that is not $ 4t $ -list-colourable.

=== References listed by OpenProblemGarden ===
- [B] Mieczyslaw Borowiecki. Research problem 172. Discrete Math., 121:235–236, 1993. .
- [BJW] Janos Barát, Gwenael Joret, David R. Wood. Disproof of the List Hadwiger Conjecture, Electronic J. Combinatorics 18:P232, 2011.
- [ERT] Paul Erdo ̋s, Arthur L. Rubin, and Herbert Taylor. Choosability in graphs. In Proc. West Coast Conference on Combinatorics, Graph Theory and Computing, vol. XXVI of Congress. Numer., pp. 125–157. Utilitas Math., 1980. MathSciNet.
- *[KM] Ken-ichi Kawarabayashi and Bojan Mohar. A relaxed Hadwiger’s conjecture for list colorings. J. Combin. Theory Ser. B, 97(4):647–651, 2007. MathSciNet.
- [RST] Neil Robertson, Paul D. Seymour, and Robin Thomas. Hadwiger’s conjecture for -free graphs. Combinatorica, 13(3):279–361, 1993. MathSciNet.
- [T] Carsten Thomassen. Every planar graph is 5-choosable. J. Combin. Theory Ser. B, 62(1):180–181, 1994. MathSciNet.

=== Catalog page (statement + literature review) ===
List Hadwiger Conjecture — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that every $K_t$-minor-free graph is $ct$-list-colourable for some absolute constant $c$ remains open. Norin and Postle (2020) established the best current upper bound of $O(t(\log t)^\beta)$-list-colorability for every $\beta > 1/4$, falling short of the conjectured linear bound. Steiner (2022) improved the lower bound to $(2-o(1))t$, refuting the specific sub-conjecture $c = 3/2$ of Kawarabayashi and Mohar and showing $c \geq 2$ is necessary.

 Cited literature (4)

 
 
 
partial Connectivity and choosability of graphs with no $K_t$ minor
 (2020)
 

 
 Sergey Norin, Luke Postle · arXiv preprint · arXiv:2004.10367

Every $K_t$-minor-free graph is $O(t(\log t)^\beta)$-list-colorable for every $\beta > 1/4$, improving the previous $O(t\sqrt{\log t})$ upper bound and providing the best known bound for list coloring.
 

 
 
partial Improved lower bound for the list chromatic number of graphs with no $K_t$ minor
 (2022)
 

 
 Raphael Steiner · Combinatorics, Probability and Computing · arXiv:2110.09403 · doi:10.1017/S0963548322000116

The maximum list chromatic number of $K_t$-minor-free graphs is at least $(2-o(1))t$, showing $c \geq 2$ is necessary and disproving the specific conjecture of Kawarabayashi–Mohar that $c = 3/2$ suffices.
 

 
 
partial Refined list version of Hadwiger's conjecture
 (2022)
 

 
 Yangyan Gu, Yiting Jiang, David R. Wood, Xuding Zhu · SIAM Journal on Discrete Mathematics · arXiv:2209.07013 · doi:10.1137/22M1522413

Introduces a λ-choosability framework and proves that for any $\varepsilon > 0$ and sufficiently large $t$, for any partition $\lambda$ of $\lfloor(2-\varepsilon)t\rfloor$, there exists a $K_t$-minor-free graph that is not λ-choosable, showing fundamental limitations on list colorability below the $2t$ threshold.
 

 
 
partial Improved lower bound for the list chromatic number of graphs with no $K_t$ minor
 (2021)
 

 
 Raphael Steiner · arXiv preprint · arXiv:2110.09403

Disproves this conjecture by showing that the maximum list chromatic number of $K_t$-minor free graphs is at least $(2-o(1))t$, which strictly exceeds $\frac{3}{2}t$ for all sufficiently large $t$.
 

 

 Reviewer notes. The SIAM page for the Gu–Jiang–Wood–Zhu paper returned 403 Forbidden; verified via the arXiv preprint 2209.07013 instead, using DOI from earlier confirmed search results. The Norin–Postle arXiv preprint (2004.10367) may not yet have a published journal version; cited as arXiv. The Delcourt–Postle O(t log log t) result (arXiv:2108.01633) addresses standard chromatic number only, not list coloring. The gap between the upper bound O(t(log t)^beta) and the linear conjectured bound remains open.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 06) (web search enabled).
 

Conjecture. Every $ K_t $ -minor-free graph is $ c t $ -list-colourable for some constant $ c\geq1 $ .

Keywords:
Hadwiger conjecture · list colouring · minors

Discussion

Hadwiger's conjecture asserts that every $ K_t $ - minor -free graph is $ (t − 1) $ -colourable. Robertson, Seymour and Thomas [RST] proved Hadwiger's conjecture for $ t \leq 6 $ . It remains open for $ t \geq 7 $ . In fact, it is open whether every $ K_t $ -minor-free graph is $ ct $ -colourable for some constant $ c\geq 1 $ . It is natural to consider analogous problems for list colourings . First, consider planar graphs. While every planar graph is 4-colourable, Erdös, Rubin and Taylor. [ERT] conjectured that some planar graph is not 4-list-colourable, and that every planar graph is 5-list-colourable. The first conjecture was verified by Voigt [V] and the second by Thomassen [T]. More generally, Borowiecki [B] asked whether every $ K_t $ -minor-free graph is $ (t − 1) $ -list-colourable, which is true for $ t \leq 4 $ but false for $ t = 5 $ by Voigt’s example. Kawarabayashi and Mohar [KM] proposed the stated conjecture, and suggested it might be true with $ c=\frac{3}{2} $ . Barát, Joret and Wood [BJW] proved that $ c\geq\frac{4}{3} $ . In particular, they constructed a $ K_{3t+2} $ -minor-free graph that is not $ 4t $ -list-colourable.

Bibliography

 [B]
 Mieczyslaw Borowiecki. Research problem 172 . Discrete Math., 121:235–236, 1993. .
 Research problem 172

 [BJW]
 Janos Barát, Gwenael Joret, David R. Wood. Disproof of the List Hadwiger Conjecture , Electronic J. Combinatorics 18:P232, 2011.
 Disproof of the List Hadwiger Conjecture

 [ERT]
 Paul Erdo ̋s, Arthur L. Rubin, and Herbert Taylor. Choosability in graphs . In Proc. West Coast Conference on Combinatorics, Graph Theory and Computing, vol. XXVI of Congress. Numer., pp. 125–157. Utilitas Math., 1980. MathSciNet .
 Choosability in graphs · MathSciNet

★ [KM]
 Ken-ichi Kawarabayashi and Bojan Mohar. A relaxed Hadwiger’s conjecture for list colorings . J. Combin. Theory Ser. B, 97(4):647–651, 2007. MathSciNet .
 A relaxed Hadwiger’s conjecture for list colorings · MathSciNet

 [RST]
 Neil Robertson, Paul D. Seymour, and Robin Thomas. Hadwiger’s conjecture for $ K_6 $ -free graphs . Combinatorica, 13(3):279–361, 1993. MathSciNet .
 Hadwiger’s conjecture for -free graphs · MathSciNet

 [T]
 Carsten Thomassen. Every planar graph is 5-choosable . J. Combin. Theory Ser. B, 62(1):180–181, 1994. MathSciNet .
 Every planar graph is 5-choosable · MathSciNet

Related conjectures

 
 implied by
 List chromatic number bound for K_{s,t}-minor-free graphs
 open
 K_{t-1,t-1} contains a K_t minor: fix a perfect matching a_i b_i and contract the edges a_i b_i for i=1..t-2. The t-2 contracted vertices are pairwise adjacent (a_i is adjacent to b_j for i != j), and the two leftover vertices a_{t-1}, b_{t-1} are adjacent to each other and to every contracted vertex. Hence any K_t-minor-free graph is K_{t-1,t-1}-minor-free, and a positive answer to the source question with s = t' = t-1 gives chi_l(G) <= 2(t-1)+(t-1) = 3t-3 <= 3t for every K_t-minor-free G, which is exactly the List Hadwiger Conjecture with c = 3. Direction is correct: truth of the source forces truth of the target.
 

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
  "one_line": "The conjecture holds with asymptotically optimal coefficient 2 for graphs assembled by pure clique-sums of co-bipartite pieces, but the general case is not resolved.",
  "would_publish": false,
  "caveats": "Restricted-class result; the lower bound recovers the asymptotic obstruction supplied in the question, and no novelty is claimed."
}
```

## 1. Scope and result

I do not obtain a linear upper bound for arbitrary \(K_t\)-minor-free graphs. Instead, I give a sharp special case, together with a self-contained construction explaining the lower-bound constant \(2\).

Write \(\operatorname{ch}(G)\) for the list chromatic number, \(\omega(G)\) for the clique number, and \(h(G)\) for the largest order of a complete minor.

A graph is **co-bipartite** if its vertex set can be partitioned into two cliques. Let \(\mathcal C\) consist of graphs constructed by starting with a co-bipartite graph and repeatedly attaching another co-bipartite graph along a clique. All edges are retained, and there are no edges between the new vertices and the old vertices outside the identified clique. Thus these are pure clique-sums, without deletion of separator edges.

### Theorem
1. Every nonempty \(G\in\mathcal C\) satisfies
   \[
   \operatorname{ch}(G)\le 2\omega(G)-1.
   \]
   Consequently, every \(K_t\)-minor-free \(G\in\mathcal C\), for \(t\ge2\), is \((2t-3)\)-list-colourable.

2. For every sufficiently large integer \(t\), there exists a \(K_t\)-minor-free graph \(G_t\in\mathcal C\) such that
   \[
   \operatorname{ch}(G_t)\ge
   2t-\frac{(8\log\log t+2)t}{\log t}-3.
   \]

In particular, the optimal asymptotic coefficient for this class is exactly \(2\).

The unrestricted lower-bound conclusion is already present in the supplied background. The point here is a complete proof and a matching upper bound on the class containing the construction—not an improvement on the known general bounds.

## 2. Upper bound for the clique-sum class

Let \(G\in\mathcal C\) be nonempty, and put \(w=\omega(G)\). Each co-bipartite piece has at most \(2w\) vertices, since each of its two cliques has order at most \(w\).

I claim that \(G\) is \((2w-2)\)-degenerate.

Consider the last attached piece \(H\). Let \(S\) be its identified clique and let
\[
U=V(H)\setminus S
\]
be its new vertices. We may ignore an attachment with \(U=\varnothing\). Every vertex of \(U\) has all its current neighbours in \(H\).

If \(|V(H)|\le2w-1\), delete the vertices of \(U\) in any order: each has at most \(2w-2\) remaining neighbours.

If \(|V(H)|=2w\), then \(H\) is not complete, because its clique number is at most \(w<2w\). Choose a nonedge of \(H\). Since \(S\) is a clique, at least one endpoint \(v\) lies in \(U\). This vertex has degree at most \(2w-2\). Delete \(v\); the remaining part of \(H\) now has at most \(2w-1\) vertices, so the rest of \(U\) can be deleted in any order with the same degree bound.

After deleting \(U\), the preceding construction remains. Repeating this argument, including for the initial piece with \(S=\varnothing\), gives the claimed degeneracy ordering. Reverse greedy list colouring therefore yields
\[
\operatorname{ch}(G)\le2w-1.
\]

If \(G\) has no \(K_t\) minor, then \(w\le t-1\), proving the first assertion.

## 3. Two pasting lemmas

### Lemma 1: complete minors do not increase under pure clique-sums

Suppose \(G=G_1\cup G_2\), where \(V(G_1)\cap V(G_2)=S\) is a clique and there are no edges between \(V(G_1)\setminus S\) and \(V(G_2)\setminus S\). Then
\[
h(G)=\max\{h(G_1),h(G_2)\}.
\]

**Proof.**
Only the upper bound needs proof. Consider a model of \(K_k\) in \(G\).

If every branch set meets \(S\), then \(k\le |S|\), so \(K_k\) already occurs in each summand.

Otherwise, all branch sets disjoint from \(S\) lie in the same summand, say \(G_1\): each such branch set is contained in one side, and two lying on opposite sides would not be adjacent.

Restrict every branch set meeting \(S\) to \(V(G_1)\). Its restriction is connected. Indeed, every retained component off \(S\) attaches to a retained vertex of \(S\), and the retained vertices in \(S\) form a clique. Adjacencies to branch sets disjoint from \(S\) are retained. Adjacencies between two branch sets meeting \(S\) are supplied by the clique \(S\). Thus these restrictions give a \(K_k\) model in \(G_1\). ∎

### Lemma 2: turning an extension obstruction into a list obstruction

Let \(H\) have a partition \(V(H)=A\cup B\), where both \(A\) and \(B\) are \(n\)-vertex cliques. Suppose every vertex of \(B\) has at least \(d\) neighbours in \(A\), where \(1\le d\le n\).

Then there is a graph \(G\), obtained by pasting copies of \(H\) along \(A\), such that
\[
h(G)=h(H),
\qquad
\operatorname{ch}(G)\ge n+d.
\]

**Proof.**
Put
\[
\ell=n+d-1.
\]
Choose disjoint colour sets \(T,P\), with
\[
|T|=\ell,\qquad |P|=n-1.
\]
For each \(b\in B\), fix a set
\[
D_b\subseteq N_H(b)\cap A,\qquad |D_b|=d.
\]

For every injection \(f:A\to T\), attach a fresh copy \(B_f\) of \(B\), with its adjacency to the common clique \(A\) prescribed by \(H\). There are no edges between distinct \(B_f\)'s. Assign lists
\[
L(a)=T\quad(a\in A),
\]
and, for the copy \(b_f\) of \(b\),
\[
L(b_f)=P\cup f(D_b).
\]
Every list has exactly \(\ell\) colours.

Any proper list colouring of \(A\) is an injection \(f:A\to T\). In the corresponding copy \(B_f\), every colour in \(f(D_b)\) is forbidden at \(b_f\) by a neighbour in \(A\). Thus the entire \(n\)-vertex clique \(B_f\) would have to be coloured from the same \(n-1\) colours \(P\), which is impossible. Hence
\[
\operatorname{ch}(G)\ge\ell+1=n+d.
\]

Lemma 1 gives \(h(G)=h(H)\). The construction is finite: it has
\[
n\bigl(1+(\ell)_n\bigr)\le n\bigl(1+(2n)^n\bigr)
\]
vertices, where \((\ell)_n\) is the number of injections from an \(n\)-element set to an \(\ell\)-element set. ∎

The key feature is that pasting preserves the complete-minor bound while making every possible colouring of the common clique encounter a failed extension.

## 4. Dense co-bipartite blocks with small complete minors

The remaining ingredient is a co-bipartite graph with cross-degrees close to \(n\), but Hadwiger number close to \(n\), rather than \(2n\).

Fix
\[
0<q<\tfrac12,\qquad 0<\varepsilon<1.
\]
Take disjoint \(n\)-vertex cliques \(A,B\), and include each edge between \(A\) and \(B\) independently with probability \(1-q\). Set
\[
k=\left\lceil(1+\varepsilon)n\right\rceil,
\qquad
r=\left\lceil\frac2\varepsilon\right\rceil.
\]

I will prove that the probability that either

* some vertex has fewer than \((1-2q)n\) neighbours in the opposite clique, or
* the graph contains a \(K_k\) minor,

is at most
\[
2n e^{-qn/3}
+
\exp\!\left(
2n\log(2n+1)-\frac{\varepsilon^2q^r n^2}{2}
\right).
\tag{1}
\]

### Cross-degrees

For each vertex, the number \(X\) of missing cross-edges has distribution \(\operatorname{Bin}(n,q)\). The exponential-moment estimate gives
\[
\Pr(X>2qn)
\le \frac{(1+q)^n}{2^{2qn}}
\le e^{-(2\log2-1)qn}
\le e^{-qn/3}.
\]
A union bound over the \(2n\) vertices proves the first term of (1).

### Complete-minor models

Fix a candidate family of \(k\) pairwise disjoint, nonempty branch sets. At least
\[
2k-2n\ge2\varepsilon n
\]
of them are singletons: otherwise their total number of vertices would exceed \(2n\).

Consequently, one side, say \(A\), contains at least \(\varepsilon n\) singleton branch sets. Let \(X\subseteq A\) be their vertices.

At most \(n\) branch sets can meet \(A\), so at least
\[
k-n\ge\varepsilon n
\]
branch sets lie entirely in \(B\). At most \(n/(r+1)<\varepsilon n/2\) of these can have more than \(r\) vertices. Thus at least \(\varepsilon n/2\) of them have size at most \(r\). Denote these sets by
\[
Y_1,\ldots,Y_m,\qquad m\ge\varepsilon n/2.
\]

For the candidate family to be a complete-minor model, every \(x\in X\) must have a neighbour in every \(Y_i\). For each pair \((x,Y_i)\), this has probability
\[
1-q^{|Y_i|}\le1-q^r.
\]
The edge sets involved in these tests are pairwise disjoint, so the tests are independent. Therefore the probability that this fixed candidate family is a model is at most
\[
(1-q^r)^{|X|m}
\le
\exp\!\left(-\frac{\varepsilon^2q^r n^2}{2}\right).
\]

There are at most
\[
(k+1)^{2n}\le(2n+1)^{2n}
\]
candidate labelled families: assign each vertex either to one of \(k\) labelled branch sets or to an unused class. Invalid assignments only enlarge this count. A union bound proves the second term of (1).

This argument ignores the connectivity and other adjacency requirements of a model, which is legitimate for an upper bound on its probability.

## 5. Parameter choice and the near-\(2t\) obstruction

Let \(t\) tend to infinity through the integers, and set
\[
L=\log t,\qquad l=\log\log t,
\]
\[
q=\frac1L,\qquad
\varepsilon=\frac{4l}{L},\qquad
n=\left\lfloor\frac{t}{1+\varepsilon}\right\rfloor.
\]
For sufficiently large \(t\), these parameters are in the ranges used above, \(n\ge t/2\), and
\[
k=\left\lceil(1+\varepsilon)n\right\rceil\le t.
\]

Furthermore,
\[
r\le \frac{L}{2l}+1,
\]
so
\[
q^r
\ge L^{-L/(2l)-1}
=\frac{t^{-1/2}}{L}.
\]
It follows that
\[
\frac{\varepsilon^2q^r n^2}{2}
\ge
\frac{2t^{3/2}l^2}{L^3}.
\]
Thus the failure probability in (1) is at most
\[
2t\exp\!\left(-\frac{t}{6L}\right)
+
\exp\!\left(
2t\log(2t+1)-\frac{2t^{3/2}l^2}{L^3}
\right),
\]
which tends to zero. In particular, it is less than one for every sufficiently large \(t\).

Hence there exists a co-bipartite graph \(H\) with two \(n\)-vertex cliques such that

* \(H\) has no \(K_k\) minor;
* every vertex has at least \((1-2q)n\) neighbours in the opposite clique.

Put
\[
d=\lfloor(1-2q)n\rfloor.
\]
For sufficiently large \(t\), we have \(d\ge1\), so Lemma 2 applies. It produces \(G_t\in\mathcal C\) satisfying
\[
h(G_t)=h(H)<k\le t
\]
and
\[
\operatorname{ch}(G_t)\ge n+d.
\]
In particular, \(G_t\) is \(K_t\)-minor-free.

Finally,
\[
\begin{aligned}
\operatorname{ch}(G_t)
&\ge (2-2q)n-1\\
&\ge \frac{2-2q}{1+\varepsilon}\,t-3\\
&\ge \bigl(2-2\varepsilon-2q\bigr)t-3\\
&=
2t-\frac{(8\log\log t+2)t}{\log t}-3.
\end{aligned}
\]
This proves the second assertion of the theorem. The construction also has the finite order bound
\[
|V(G_t)|\le t\bigl(1+(2t)^t\bigr).
\]

Together with the upper bound, this gives
\[
\lim_{t\to\infty}
\frac{1}{t}
\sup\left\{
\operatorname{ch}(G):
G\in\mathcal C,\ h(G)<t
\right\}
=2.
\]

## 6. What remains unresolved

This establishes an asymptotically sharp special case, not the conjecture itself.

The upper-bound proof depends on every piece having at most twice the global clique number in vertices. Arbitrary \(K_t\)-minor-free graphs need not admit such a clique-sum construction, so the argument supplies no general linear upper bound.

The lower construction excludes every proposed constant \(c<2\), but it does **not** exclude any fixed \(c\ge2\). In particular, it neither disproves the quantified conjecture nor proves that \(c=2\) works in general. The unrestricted gap remains.
