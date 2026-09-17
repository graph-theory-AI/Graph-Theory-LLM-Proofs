Attack the following open graph-theory problem.

Catalog id: subdivision_of_a_transitive_tournament_in_digraphs_with_large_outdegree
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Directed Graphs
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/subdivision_of_a_transitive_tournament_in_digraphs_with_large_outdegree/
Original entry: http://www.openproblemgarden.org/op/subdivision_of_a_transitive_tournament_in_digraphs_with_large_outdegree
Problem attributed to: Mader, W. (posted 2013-03-04)

=== Problem statement (OpenProblemGarden) ===
Title: Subdivision of a transitive tournament in digraphs with large outdegree.
Conjecture For all $ k $ there is an integer  $ f(k) $ such that every digraph of minimum outdegree at least  $ f(k) $ contains a subdivision of a transitive tournament of order $ k $ .

=== Discussion / context (OpenProblemGarden) ===
A fundamental result of Mader [M1] states that for every integer $ k $ there is a smallest $ g(k) $ so that every graph of average degree at least $ g(k) $ contains a subdivision of a complete graph on $ k $ vertices. Bollobás and Thomason [BT] as well as Komlós and Szemerédi [KS] showed that $ g $ is quadratic in $ k $ . The above conjecture is a digraph analogue of this result. However one cannot replace the minimum outdegree in this conjecture by the average degree as in Mader's analogue for graphs: consider the complete bipartite graph $ K_{n,n} $ and orient all edges from the first to the second class. The resulting digraph has average degree $ n $ but not even a transitive tournament on 3 vertices. One might be tempted to conjecture that large minimum outdegree would even force the existence of a subdivision of a large complete digraph. However, for all $ n $ Thomassen [T] constructed a digraph on $ n $ vertices whose minimum outdegree is at least $ \frac{1}{2} \log_2 n $ but which does not contain an even directed cycle (and thus no complete digraph on 3 vertices). A simpler construction was found by DeVos et al. [DMMS]. It is easy to see that  $ f(1)=0 $ and $ f(2)=1 $ . Mader [M3] showed that $ f(4) = 3 $ . Even the existence of  $ f(5) $ is not known.

=== References listed by OpenProblemGarden ===
- [BT] B. Bollobás and A. Thomason, Proof of a conjecture of Mader, Erdös and Hajnal on topological complete subgraphs, European Journal of Combinatorics 19 (1998), 883–887.
- [DMMS] M. DeVos, J. McDonald, B. Mohar, and D. Scheide, Immersing complete digraphs, European Journal of Combinatorics, 33 (2012), no 6, 1294-1302.
- [KS] J. Komlós and E. Szemerédi, Topological Cliques in Graphs II, Combinatorics, Probability and Computing 5 (1996), 70–90.
- [M1] W. Mader, Homomorphieeigenschaften und mittlere Kantendichte von Graphen, Math. Annalen 174 (1967), 265–268.
- * [M2] W. Mader, Degree and Local Connectivity in Digraphs, Combinatorica 5 (1985), 161–165.
- [M3] W. Mader, On Topological Tournaments of order 4 in Digraphs of Outdegree 3, Journal of Graph Theory 21 (1996), 371–376.
- [T] C. Thomassen, Even Cycles in Directed Graphs, European Journal of Combinatorics 6 (1985), 85–89.

=== Catalog page (statement + literature review) ===
Subdivision of a transitive tournament in digraphs with large outdegree. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 Mader's conjecture remains open in full generality — even the existence of $f(5)$ is unknown as of the most recent sources found. Meaningful partial progress has been made: Lochet (2017) proved the immersion analogue of the conjecture (immersion being a weaker embedding notion than subdivision), and Aboulker et al. (2019) proved the conjecture for special sub-structures (oriented paths, in-arborescences) and connected it to the dichromatic number. Kim, Lee, and Seo (2022) established Ramsey-type bounds $O(k^2 \log\log k)$ for 1-subdivisions of transitive tournaments inside arbitrary tournaments.

 Cited literature (4)

 
 
 
partial Subdivisions in Digraphs of Large Out-Degree or Large Dichromatic Number
 (2019)
 

 
 Pierre Aboulker, Nathann Cohen, Frédéric Havet, William Lochet, Phablo F. S. Moura, Stéphan Thomassé · The Electronic Journal of Combinatorics · arXiv:1610.00876

Proves Mader's conjecture for special cases including oriented paths and in-arborescences, and shows digraphs with dichromatic number greater than $4^m(n-1)$ contain every $n$-vertex $m$-arc digraph as a subdivision; the general conjecture remains open with $f(5)$ still unknown.
 

 
 
partial Immersion of transitive tournaments in digraphs with large minimum outdegree
 (2017)
 

 
 William Lochet · arXiv preprint · arXiv:1710.11482

Proves the immersion analogue of Mader's conjecture: every simple digraph with minimum outdegree greater than $h(k)$ contains an immersion of the transitive tournament on $k$ vertices, resolving a conjecture of DeVos–McDonald–Mohar–Scheide.
 

 
 
partial On 1-subdivisions of transitive tournaments
 (2022)
 

 
 Jaehoon Kim, Hyunwoo Lee, Jaehyeon Seo · The Electronic Journal of Combinatorics · arXiv:2110.05002

Proves the oriented Ramsey number for the 1-subdivision of the $k$-vertex transitive tournament is $O(k^2 \log\log k)$, tight up to the logarithmic factor, and gives structural results for tournaments with bounded outdegree variation; applies to tournaments, not general digraphs.
 

 
 
partial Subdivisions in digraphs of large out-degree or large dichromatic number
 (2016)
 

 
 Pierre Aboulker, Nathann Cohen, Fréderic Havet, William Lochet, Phablo F. S. Moura, Stéphan Thomassé · arXiv preprint · arXiv:1610.00876

Proves the conjecture for all oriented paths (Corollary 20, with $\mathrm{mader}_{\delta^+}(P)=|V(P)|-1$), for all in-arborescences (Theorem 23), and for the union of two directed paths from $x$ to $y$ and one from $y$ to $x$ (Theorem 24); also studies an analogue via the dichromatic number parameter.
 

 

 Reviewer notes. The Lochet immersion paper (arXiv:1710.11482, 2017) resolves a related but weaker conjecture; its journal publication status was not fully confirmed but its content and authorship were verified. The Kim–Lee–Seo result applies to 1-subdivisions inside tournaments (not general digraphs with large minimum outdegree), so it does not directly resolve Mader's conjecture. No paper was found proving f(5) exists or resolving the general Mader conjecture. A 2023 survey (arXiv:2306.02364) was found but did not address this specific conjecture in its accessible content.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 02) (web search enabled).
 

Conjecture. For all $ k $ there is an integer  $ f(k) $ such that every digraph of minimum outdegree at least  $ f(k) $ contains a subdivision of a transitive tournament of order $ k $ .

Discussion

A fundamental result of Mader [M1] states that for every integer $ k $ there is a smallest $ g(k) $ so that every graph of average degree at least $ g(k) $ contains a subdivision of a complete graph on $ k $ vertices. Bollobás and Thomason [BT] as well as Komlós and Szemerédi [KS] showed that $ g $ is quadratic in $ k $ . The above conjecture is a digraph analogue of this result. However one cannot replace the minimum outdegree in this conjecture by the average degree as in Mader's analogue for graphs: consider the complete bipartite graph $ K_{n,n} $ and orient all edges from the first to the second class. The resulting digraph has average degree $ n $ but not even a transitive tournament on 3 vertices. One might be tempted to conjecture that large minimum outdegree would even force the existence of a subdivision of a large complete digraph. However, for all $ n $ Thomassen [T] constructed a digraph on $ n $ vertices whose minimum outdegree is at least $ \frac{1}{2} \log_2 n $ but which does not contain an even directed cycle (and thus no complete digraph on 3 vertices). A simpler construction was found by DeVos et al. [DMMS]. It is easy to see that  $ f(1)=0 $ and $ f(2)=1 $ . Mader [M3] showed that $ f(4) = 3 $ . Even the existence of  $ f(5) $ is not known.

Bibliography

 [BT]
 B. Bollobás and A. Thomason, Proof of a conjecture of Mader, Erdös and Hajnal on topological complete subgraphs, European Journal of Combinatorics 19 (1998), 883–887.

 [DMMS]
 M. DeVos, J. McDonald, B. Mohar, and D. Scheide, Immersing complete digraphs, European Journal of Combinatorics, 33 (2012), no 6, 1294-1302.

 [KS]
 J. Komlós and E. Szemerédi, Topological Cliques in Graphs II, Combinatorics, Probability and Computing 5 (1996), 70–90.

 [M1]
 W. Mader, Homomorphieeigenschaften und mittlere Kantendichte von Graphen, Math. Annalen 174 (1967), 265–268.

★ [M2]
 W. Mader, Degree and Local Connectivity in Digraphs, Combinatorica 5 (1985), 161–165.

 [M3]
 W. Mader, On Topological Tournaments of order 4 in Digraphs of Outdegree 3, Journal of Graph Theory 21 (1996), 371–376.

 [T]
 C. Thomassen, Even Cycles in Directed Graphs, European Journal of Combinatorics 6 (1985), 85–89.

Related conjectures

 
 equivalent to
 TT_k Subdivision via Minimum Semidegree
 open
 One direction is hypothesis-class containment: delta^0(D)=min(delta^+,delta^-)>=f forces delta^+(D)>=f, so any digraph satisfying the semidegree hypothesis satisfies the outdegree hypothesis, hence Mader's outdegree conjecture implies the semidegree version. The converse is proved in the source paper: it shows that if transitive tournaments are delta^0-maderian then mader_{delta^+}(TT_k) <= mader_{delta^0}(TT_{2k}) for all k, and the provided context explicitly states 'Conjecture 3 is equivalent to Mader's Conjecture 2', which is the OPG statement. Equivalence is thus both partly self-contained and explicitly asserted in the source text.
 

 
 implies
 TT_k Subdivision via Minimum Semidegree
 open
 Hypothesis-class containment: delta^0(D) = min(min-outdegree, min-indegree), so any digraph with delta^0(D) >= f(k) in particular has minimum outdegree >= f(k). If Mader's outdegree conjecture holds with f(k), every such digraph contains a TT_k subdivision, so mader_{delta^0}(TT_k) exists and is <= f(k). The semidegree hypothesis is the stronger assumption, making the outdegree conjecture the stronger statement; direction as claimed. The target's own context notes the paper proves the two are in fact equivalent (via mader_{delta^+}(TT_k) <= mader_{delta^0}(TT_{2k})), but the claimed one-way implication is immediate from the statements alone.
 

 
 implies
 δ⁺-Maderian property for oriented trees
 open
 Every oriented tree T on k vertices is an acyclic digraph, so ordering its vertices along a topological order embeds T as a subdigraph of the transitive tournament TT_k (TT_k contains all forward arcs). A subdivision of TT_k contains a subdivision of every subdigraph H of TT_k: keep the branch vertices of H and the directed paths corresponding to H's arcs. Hence if min out-degree >= f(k) forces a TT_k-subdivision (source), it forces a subdivision of every oriented tree of order k, i.e., every oriented tree is delta+-maderian with mader_{delta+}(T) <= f(|T|) (target). Direction is correct: source is the stronger statement, and the target's context confirms it is 'posed as a natural weaker step towards Mader's Conjecture'.
 

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
  "one_line": "An explicit oriented four-cycle blow-up has subdivision threshold (19/128)k^2 + O(k), giving a quadratic lower bound on any possible forcing function f(k).",
  "would_publish": false,
  "caveats": "This gives no universal upper bound and does not establish that f(5) exists; novelty of the obstruction-family calculation has not been checked."
}
```

## 1. A quantitative partial result

I do not resolve the conjecture. I prove an asymptotically sharp threshold **within one explicit family of oriented digraphs**, and hence a necessary lower bound on the conjectured function.

All digraphs below are finite and loopless. A subdivision has distinct branch vertices, and its replacement directed paths are internally vertex-disjoint and avoid all branch vertices internally.

Let \(D_t\) have four independent vertex classes
\[
V_0,V_1,V_2,V_3,\qquad |V_i|=t,
\]
with all arcs from \(V_i\) to \(V_{i+1}\), indices modulo \(4\), and no other arcs. Thus
\[
|V(D_t)|=4t,\qquad \delta^+(D_t)=\delta^-(D_t)=t.
\]
In particular, \(D_t\) is an oriented graph.

Write
\[
\tau(k)=\min\{t\ge 1:D_t\text{ contains a subdivision of }TT_k\}.
\]

### Theorem
For every positive integer \(k\), putting \(r=\lceil k/8\rceil\),
\[
\boxed{\quad
\frac{19}{128}k^2-\frac{23}{160}k
\ \le\ \tau(k)\
\le\ \frac{19r^2+r}{2}.
\quad}
\]
Consequently,
\[
\boxed{\tau(k)=\frac{19}{128}k^2+O(k).}
\]

In particular, for \(k\ge4\), any finite forcing threshold in the original conjecture must satisfy
\[
\boxed{\quad
f(k)\ge
\left\lceil \frac{19}{128}k^2-\frac{23}{160}k\right\rceil .
\quad} \tag{1}
\]
Indeed, take \(t\) to be one less than the integer on the right. This is positive for \(k\ge4\), and the theorem says that \(D_t\) has no \(TT_k\)-subdivision.

The proof follows.

---

## 2. Three necessary capacity inequalities

Suppose a \(TT_k\)-subdivision occurs in \(D_t\). Order its branch vertices according to the transitive tournament. Let

- \(n_i\) be the number of branch vertices in \(V_i\);
- \(\ell_i\) be the total number of vertices of the subdivision in \(V_i\).

Thus
\[
\sum_i n_i=k,\qquad \ell_i\le t.
\]

Every directed path in \(D_t\) moves clockwise through the four classes. In particular:

- a path between distinct vertices of the same class has at least three internal vertices, one in each other class;
- a path between opposite classes has at least one internal vertex;
- a path between consecutive classes, but directed against their connecting arcs, has at least two internal vertices.

Normalize the branch counts by
\[
p_i=\frac{n_i}{k},\qquad
S_2=\sum_i p_i^2,\qquad S_3=\sum_i p_i^3,
\]
and put
\[
\mu=\min_i p_i,\qquad
m=\min_i p_i p_{i+1}.
\]
Define
\[
A=\frac{1-S_3}{6},
\qquad
B=\frac{S_2-\mu^2}{2},
\qquad
C=\frac{\frac32 S_2+p_0p_2+p_1p_3+2m}{4}.
\]

We will prove
\[
\begin{aligned}
t&\ge k^2A-\frac{k}{8}, \tag{2}\\
t&\ge k^2B-\frac{k}{2}, \tag{3}\\
t&\ge k^2C-\frac{k}{8}. \tag{4}
\end{aligned}
\]

### 2.1. Same-class pairs: inequality (3)

For every \(j\), each pair of branch vertices in another class requires a replacement path with an internal vertex in \(V_j\). These internal vertices are all distinct. Hence
\[
\ell_j\ge n_j+\sum_{i\ne j}\binom{n_i}{2}.
\]
Choosing \(j\) with \(n_j=k\mu\), this becomes
\[
t\ge
\frac{k^2}{2}(S_2-\mu^2)+\frac32n_j-\frac{k}{2}
\ge k^2B-\frac{k}{2}.
\]

### 2.2. Four-class tuples: inequality (4)

Let \(X_i\) count branch pairs in \(V_i,V_{i+1}\) whose tournament arc points against the clockwise direction, and let \(X=\sum_iX_i\).

Then
\[
X\ge \min_i n_i n_{i+1}. \tag{5}
\]
If some \(n_i=0\), this is immediate. Otherwise choose one branch vertex from each class. Among their four consecutive-class pairs, at least one points against the clockwise direction: all four pointing clockwise would form a directed cycle in a transitive tournament. Counting these choices gives
\[
1\le \sum_i\frac{X_i}{n_i n_{i+1}}
\le \frac{X}{\min_i n_i n_{i+1}},
\]
proving (5).

The path-length observations now give
\[
\begin{aligned}
4t
&\ge \sum_i\ell_i\\
&\ge k+3\sum_i\binom{n_i}{2}
       +n_0n_2+n_1n_3+2X\\
&\ge 4k^2C-\frac{k}{2}.
\end{aligned}
\]
This is (4).

### 2.3. A weighted triple count: inequality (2)

Consider the weighted occupancy
\[
\sum_i n_i\ell_i\le kt.
\]

The branch vertices contribute \(\sum_i n_i^2\). A replacement path whose two ends lie in \(V_i\) visits every other class internally, so all such paths contribute at least
\[
\sum_i\binom{n_i}{2}(k-n_i).
\]

There is also a useful contribution from triples of branch vertices in three distinct classes. For any such triple, at least one of its three replacement paths must pass internally through the class of the third vertex. To see this, arrange the three classes cyclically. Orienting all three pairs in their cyclic direction would give a directed triangle; the transitive tournament must reverse at least one, whose clockwise route passes through the third class.

Thus the cross-class paths contribute at least
\[
\sum_{i<j<h}n_i n_j n_h
\]
to the weighted occupancy. Consequently,
\[
kt\ge
\sum_i n_i^2+
\sum_i\binom{n_i}{2}(k-n_i)
+\sum_{i<j<h}n_i n_j n_h.
\]
Using the elementary-symmetric-polynomial identity for the final sum, the right side simplifies to
\[
\frac{k^3-\sum_i n_i^3}{6}
+\frac{3\sum_i n_i^2-k^2}{2}.
\]
After division by \(k\),
\[
t\ge k^2A+\frac{k}{2}(3S_2-1).
\]
Since \(S_2\ge1/4\), inequality (2) follows.

---

## 3. Optimizing the three inequalities

The key numerical fact is the following.

### Lemma
For every nonnegative \(p_0,p_1,p_2,p_3\) with sum \(1\), the quantities above satisfy
\[
\boxed{\frac{12A+7C+B}{20}\ge\frac{19}{128}.} \tag{6}
\]

### Proof

First suppose all coordinates are positive. Cyclically relabel them as \(a,b,c,d\) so that
\[
ad=\min\{ab,bc,cd,da\}.
\]
Then
\[
b\ge d,\qquad c\ge a.
\]

Write
\[
a=x+v,\quad d=x-v,\quad
b=y+u,\quad c=y-u.
\]
We have
\[
x+y=\frac12,\qquad
0<x\le\frac14,\qquad
|v|\le x,\qquad
|u+v|\le y-x\le\frac12.
\]
Also
\[
\mu=x-|v|,\qquad m=x^2-v^2.
\]

Set
\[
h=x-\frac18,\qquad z=u-v,\qquad w=u+v.
\]
Substitution into the definitions of \(A,B,C\) gives the identity
\[
\begin{aligned}
\frac{12A+7C+B}{20}-\frac{19}{128}
={}&\frac{3}{10}h^2+\frac{7}{80}z^2
+\frac35 hzw
+\frac1{20}|v|(x-|v|).
\end{aligned}
\]
The last term is nonnegative. Since \(|w|\le1/2\), the remaining terms are at least
\[
\begin{aligned}
\frac{3}{10}h^2+\frac{7}{80}z^2-\frac{3}{10}|hz|
&=
\frac{3}{10}\left(|h|-\frac{|z|}{2}\right)^2
+\frac1{80}z^2\\
&\ge0.
\end{aligned}
\]
This proves (6) for positive coordinates. All quantities in (6) are continuous on the closed simplex, so the result extends to zero coordinates. \(\square\)

Now take the weighted average of (2), (4), and (3), with weights \(12/20,7/20,1/20\), respectively. By the lemma,
\[
\begin{aligned}
t
&\ge k^2\frac{12A+7C+B}{20}
-\left(\frac{19}{20}\frac18+\frac1{20}\frac12\right)k\\
&\ge \frac{19}{128}k^2-\frac{23}{160}k.
\end{aligned}
\]
This proves the lower bound in the theorem.

---

## 4. An asymptotically matching subdivision

For the upper bound, first let \(k=8r\).

Choose branch vertices in the four classes in quantities
\[
(n_0,n_1,n_2,n_3)=(r,3r,3r,r),
\]
and order them in the transitive tournament class by class:
\[
V_0\ \text{first},\quad V_1,\quad V_2,\quad V_3\ \text{last}.
\]

For every tournament arc, prescribe the shortest clockwise class route between its ends. For ends in the same class, prescribe one complete circuit of the four classes.

The numbers of vertices required in each class, including branch vertices, are:

\[
\begin{array}{c|c|c}
\text{Class}&\text{Branch vertices}&\text{Total required vertices}\\ \hline
V_0&r&(19r^2-5r)/2\\
V_1&3r&(19r^2+r)/2\\
V_2&3r&(19r^2+r)/2\\
V_3&r&(19r^2-5r)/2
\end{array}
\]

For example, the demand in \(V_1\) is
\[
3r+\binom r2+\binom{3r}{2}+\binom r2
+r(3r+r)
=\frac{19r^2+r}{2}.
\]
The binomial terms come from same-class pairs elsewhere; the final term comes from paths from \(V_0\) to \(V_2\) or \(V_3\).

If
\[
t\ge\frac{19r^2+r}{2},
\]
assign a distinct nonbranch vertex to every prescribed internal occurrence in each class. This produces the required paths: all consecutive-class arcs exist, and the assignments ensure that no internal vertex is reused. Therefore
\[
\tau(8r)\le\frac{19r^2+r}{2}.
\]

For general \(k\), take \(r=\lceil k/8\rceil\) and retain any \(k\) branch vertices of the resulting \(TT_{8r}\)-subdivision together with their corresponding paths. Thus
\[
\tau(k)\le\frac{19r^2+r}{2}
=\frac{19}{128}k^2+O(k),
\]
completing the theorem.

---

## 5. What this does—and does not—settle

The result supplies explicit oriented digraphs showing that any universal threshold must be at least
\[
\frac{19}{128}k^2-O(k).
\]
The leading constant is sharp for this particular four-cycle blow-up family.

It does **not** supply counterexamples of arbitrarily large minimum outdegree for a fixed \(k\). Indeed, the matching construction proves that this family eventually contains the desired subdivision. Thus it obstructs a small forcing threshold, not the existence of a threshold.

The central missing assertion remains a universal upper bound for arbitrary digraphs; in particular, this argument gives no proof that \(f(5)\) exists. No claim is made that the family calculation or its constant is new in the literature.
