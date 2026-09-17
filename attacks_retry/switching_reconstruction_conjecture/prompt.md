Attack the following open graph-theory problem.

Catalog id: switching_reconstruction_conjecture
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/switching_reconstruction_conjecture/
Original entry: http://www.openproblemgarden.org/op/switching_reconstruction_conjecture
Problem attributed to: Stanley, Richard P. (posted 2013-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Switching reconstruction conjecture
Conjecture Every simple graph on five or more vertices is switching-reconstructible.

=== Discussion / context (OpenProblemGarden) ===
To switch a vertex of a simple graph is to exchange its sets of neighbours and non-neighbours. The graph so obtained is called a switching of the graph. The collection of switchings of a graph G is called the switching deck of $ G $ . A graph is switching-reconstructible if every graph with the same deck as $ G $ is isomorphic to $ G $ . There are four pairs of non-isomorphic graphs of order $ 4 $ with the same switching deck. One of them consists of the empty graph and the $ 4 $ -cycle. Stanley [S] proved that a graph on $ n $ vertices is switching-reconstructible if $ n \not\equiv 0 (\mod 4) $ . An analogous problem was posed for digraphs. Instead of complementing the edges at a vertex, one reverses each of its incident arc.

=== References listed by OpenProblemGarden ===
- *[S] R. P. Stanley Reconstruction from vertex-switching. J. Combin. Theory Ser. B, 38 (1985), 132--138.

=== Catalog page (statement + literature review) ===
Switching reconstruction conjecture — Graph-theory open problems

 
 Status
 open
 medium confidence
 

 Stanley proved in 1985 that every simple graph on $n$ vertices is switching-reconstructible when $n \not\equiv 0 \pmod{4}$, and this remains the best known result. The conjecture is still open for $n \equiv 0 \pmod{4}$, $n \geq 8$ (the case $n = 4$ is known to fail). No post-2013 papers establishing progress on this remaining open case were found.

 Reviewer notes. arxiv:2401.01582 ('The Stanley Conjecture Revisited') and arxiv:2309.13870 ('New cases of the Strong Stanley Conjecture') are both about Jack symmetric functions / Littlewood-Richardson coefficients, completely unrelated to graph reconstruction. arxiv:2601.04530 ('On identity Seidel switches', 2026) studies which vertex subsets yield automorphisms under Seidel switching, tangentially related but not addressing reconstruction. arxiv:2403.04263 ('Switching Classes: Characterization and Computation', 2024) studies hereditary class properties under switching, not reconstruction. arxiv:2604.16567 ('Shuffling the Deck', 2026) concerns the classical vertex-deletion reconstruction conjecture, not vertex-switching reconstruction. The OPG page was unreachable (ECONNREFUSED). The core open case—n ≡ 0 (mod 4), n ≥ 8—appears not to have attracted published resolution since Stanley's foundational 1985 paper.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 04) (web search enabled).
 

Conjecture. Every simple graph on five or more vertices is switching-reconstructible.

Keywords:
reconstruction

Discussion

To switch a vertex of a simple graph is to exchange its sets of neighbours and non-neighbours. The graph so obtained is called a switching of the graph. The collection of switchings of a graph G is called the switching deck of $ G $ . A graph is switching-reconstructible if every graph with the same deck as $ G $ is isomorphic to $ G $ . There are four pairs of non-isomorphic graphs of order $ 4 $ with the same switching deck. One of them consists of the empty graph and the $ 4 $ -cycle. Stanley [S] proved that a graph on $ n $ vertices is switching-reconstructible if $ n \not\equiv 0 (\mod 4) $ . An analogous problem was posed for digraphs. Instead of complementing the edges at a vertex, one reverses each of its incident arc.

Bibliography

★ [S]
 R. P. Stanley Reconstruction from vertex-switching. J. Combin. Theory Ser. B, 38 (1985), 132--138.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A local degree certificate settles several infinite families, and an exponential self-switching bound gives failure probability O(n^2 2^(-3n/2)) for G(n,1/2).",
  "would_publish": false,
  "caveats": "The general case n divisible by 4 remains unresolved; novelty of these partial results has not been verified."
}
```

# Partial results

I use the standard convention that the switching deck is a **multiset**, with one card for each vertex.

The results below are self-contained. They give:

1. An \(O(n^3)\)-time sufficient certificate for switching reconstruction, based only on degrees and common neighborhoods.
2. Reconstruction for, among other classes:
   - graphs whose degree set contains no two values differing by \(2\), including all regular and almost-regular graphs;
   - disconnected graphs and graphs with disconnected complement;
   - graphs satisfying \(\delta+\Delta<n-2\) or \(\delta+\Delta>n\).
3. An exponential lower bound on the number of switchings isomorphic to a putative counterexample.
4. Consequently, the quantitative probabilistic result
   \[
   \Pr\bigl(G(n,1/2)\text{ is not switching-reconstructible}\bigr)
   =O\!\left(n^2\,2^{-3n/2}\right).
   \]

These do not resolve the remaining deterministic case.

## 1. What the deck immediately determines

For \(S\subseteq V(G)\), write \(G^S\) for switching all vertices of \(S\). This toggles precisely the edges between \(S\) and \(V(G)\setminus S\). In particular,
\[
G^S=G^{V(G)\setminus S}.
\]

Suppose \(G\) has \(n\) vertices and \(m\) edges. Switching a vertex \(v\) gives
\[
e(G^{\{v\}})=m+n-1-2d_G(v).
\]
Summing over all vertices,
\[
\sum_{v\in V(G)}e(G^{\{v\}})
=(n-4)m+n(n-1).
\]
Thus, when \(n\ne4\), the switching deck determines \(m\), and then determines the degree multiset through
\[
d_G(v)=\frac{m+n-1-e(G^{\{v\}})}2. \tag{1}
\]

A second useful observation considerably restricts possible rivals.

**Lemma 1.** Suppose \(G\) and \(H\) have the same switching deck. For every \(v\in V(G)\), either \(H\cong G\), or there is some \(u\ne v\) such that
\[
H\cong G^{\{u,v\}}.
\]

**Proof.** The card \(G^{\{v\}}\) occurs in the deck of \(H\). Identify an isomorphic card \(H^{\{w\}}\) with \(G^{\{v\}}\), and let \(u\) be the image of \(w\). Undoing that switch gives
\[
H\cong (G^{\{v\}})^{\{u\}}=G^{\{u,v\}}.
\]
If \(u=v\), this is \(G\). ∎

For \(n\ge5\), equality of edge counts therefore forces every such nontrivial pair to satisfy
\[
d_G(u)+d_G(v)-2\mathbf 1_{uv\in E(G)}=n-2. \tag{2}
\]

## 2. An exact degree-sequence test for a double switch

For distinct vertices \(u,v\), define
\[
C_{uv}=N_G(u)\cap N_G(v)
\]
and
\[
Z_{uv}=V(G)\setminus\bigl(N_G(u)\cup N_G(v)\cup\{u,v\}\bigr).
\]
Thus \(C_{uv}\) consists of common neighbors and \(Z_{uv}\) of common nonneighbors.

Multiset notation is used in the following statement.

**Lemma 2.** The graphs \(G\) and \(G^{\{u,v\}}\) have the same degree multiset if and only if
\[
\boxed{\quad
\{d_G(x):x\in C_{uv}\}
=
\{d_G(y)+2:y\in Z_{uv}\}.
\quad} \tag{3}
\]

**Proof.** Put \(G'=G^{\{u,v\}}\) and \(\varepsilon=\mathbf 1_{uv\in E(G)}\).

If the degree multisets agree, the edge counts agree, so (2) holds. The two switched vertices consequently exchange degrees:
\[
d_{G'}(u)=n-2-d_G(u)+2\varepsilon=d_G(v),
\]
and similarly \(d_{G'}(v)=d_G(u)\).

Every vertex in \(C_{uv}\) loses two neighbors, every vertex in \(Z_{uv}\) gains two, and all other degrees are unchanged. Therefore, writing \(P_G(z)=\sum_xz^{d_G(x)}\),
\[
P_{G'}(z)-P_G(z)
=(z^2-1)\left(
\sum_{y\in Z_{uv}}z^{d_G(y)}
-\sum_{x\in C_{uv}}z^{d_G(x)-2}
\right).
\]
Equality of the degree polynomials is equivalent to (3).

Conversely, (3) implies \(|C_{uv}|=|Z_{uv}|\). Counting adjacencies from \(u,v\) to the remaining vertices shows that this is equivalent to (2). Hence the endpoint degrees exchange, and the same polynomial calculation proves equality of the complete degree multisets. ∎

There is also a simple case in which the double switch is certainly trivial up to isomorphism.

**Lemma 3.** If \(C_{uv}=Z_{uv}=\varnothing\), then
\[
G^{\{u,v\}}\cong G.
\]

**Proof.** Every other vertex is adjacent to exactly one of \(u,v\). Consequently, switching \(u,v\) has exactly the same effect as interchanging their names. ∎

### A polynomial-time reconstruction certificate

Call a pair \(u,v\) **degree-admissible** if (3) holds and \(C_{uv}\ne\varnothing\).

**Theorem 4.** Let \(G\) have \(n\ge5\) vertices. If some vertex \(v\) belongs to no degree-admissible pair, then \(G\) is switching-reconstructible.

**Proof.** Suppose \(H\) has the same deck. By Lemma 1, either \(H\cong G\), or
\[
H\cong G^{\{u,v\}}
\]
for some \(u\ne v\). Equation (1) shows that the degree multisets agree, so Lemma 2 applies.

By the hypothesis on \(v\), we must have \(C_{uv}=\varnothing\). Equation (3) then gives \(Z_{uv}=\varnothing\), and Lemma 3 yields \(H\cong G\). ∎

This certificate can be checked without graph-isomorphism tests. For each pair \(u,v\), scan the other vertices and compare the two degree histograms in (3). This takes \(O(n)\) time per pair, hence \(O(n^3)\) time overall.

In particular, **a counterexample must have a degree-admissible partner for every vertex**.

## 3. Concrete classes covered by the certificate

### 3.1 Degree sets with no difference of two

**Corollary 5.** Every graph on at least five vertices whose degree set contains no two values differing by \(2\) is switching-reconstructible.

**Proof.** A degree-admissible pair would, by (3), supply vertices whose degrees differ by \(2\). Thus no such pair exists. ∎

This includes every regular graph and every graph with
\[
\Delta-\delta\le1.
\]

### 3.2 A restriction involving the extreme degrees

**Corollary 6.** A graph on at least five vertices is switching-reconstructible if
\[
\delta+\Delta<n-2
\qquad\text{or}\qquad
\delta+\Delta>n.
\]

**Proof.** In the first case choose \(v\) of minimum degree. For every \(u\ne v\),
\[
d(u)+d(v)-2\mathbf 1_{uv\in E(G)}
\le\Delta+\delta<n-2,
\]
so (2) cannot hold.

In the second case choose \(v\) of maximum degree. Then the same expression is at least
\[
\Delta+\delta-2>n-2,
\]
again excluding (2). Apply Lemma 1 and edge-count reconstruction. ∎

Thus every counterexample must satisfy
\[
\delta+\Delta\in\{n-2,n-1,n\}. \tag{4}
\]

### 3.3 Disconnected and co-disconnected graphs

**Corollary 7.** Every disconnected graph on at least five vertices is switching-reconstructible. The same holds if its complement is disconnected.

**Proof.** Choose \(v\) in a smallest component, of order \(s\le n/2\).

If \(u\) is in that same component, then
\[
d(u)+d(v)-2\mathbf 1_{uv\in E(G)}
\le2(s-2)<n-2,
\]
so (2) is impossible.

If \(u\) is in another component, of order \(t\), then
\[
d(u)+d(v)\le s+t-2\le n-2.
\]
Equality requires \(s+t=n\), with \(u\) and \(v\) universal in their respective components. There are then exactly two components, and every other vertex is adjacent to exactly one of \(u,v\). Lemma 3 applies.

Thus the chosen vertex \(v\) cannot lead to a nonisomorphic rival.

Finally, complementation commutes with switching and preserves isomorphism, so reconstruction of a graph is equivalent to reconstruction of its complement. ∎

## 4. An exponential obstruction to a counterexample

Define
\[
\rho(G)=\frac12
\bigl|\{S\subseteq V(G):G^S\cong G\}\bigr|.
\]
This counts distinct **labeled** switchings isomorphic to \(G\), identifying \(S\) with its complement. The factor \(1/2\) is exact: two subsets produce the same labeled switched graph precisely when they are equal or complementary.

**Theorem 8.** Suppose nonisomorphic graphs \(G,H\) have the same switching deck. Then \(n\equiv0\pmod4\), and
\[
\boxed{\qquad
\rho(G),\rho(H)\ \ge\ 2^{\,n/2-2}.
\qquad} \tag{5}
\]

The divisibility assertion recovers the result stated in the question. The separate lower bounds on both switching orbits will be useful below.

### Proof

By Lemma 1, relabel \(H\) so that it belongs to the labeled switching class of \(G\).

Consider the full cube
\[
\mathcal Q=\{0,1\}^{V(G)},
\]
where \(x\) represents its support and hence the graph \(G^x\). Partition the cube according to the isomorphism type of \(G^x\). Let
\[
A=\{x:G^x\cong G\},\qquad
B=\{x:G^x\cong H\},
\]
and put \(a=|A|\), \(b=|B|\). Thus
\[
a=2\rho(G),\qquad b=2\rho(H).
\]

Let \(L\) be cube adjacency:
\[
(Lf)(x)=\sum_{i=1}^n f(x+e_i).
\]
Define
\[
f=\frac{\mathbf 1_A}{a}-\frac{\mathbf 1_B}{b}.
\]

We first prove
\[
Lf=0. \tag{6}
\]

The isomorphism-type partition is equitable: the number of neighbors in a class \(D\) of any point in a class \(C\) is a constant \(p_{C,D}\), namely the multiplicity of type \(D\) in the switching deck of type \(C\). Undirected edge counting gives
\[
|C|p_{C,D}=|D|p_{D,C}.
\]
Equality of the decks of \(G,H\) says \(p_{A,C}=p_{B,C}\) for every class \(C\). Consequently, for \(x\in C\),
\[
(Lf)(x)
=\frac{p_{C,A}}a-\frac{p_{C,B}}b
=\frac{p_{A,C}-p_{B,C}}{|C|}
=0.
\]

The cube characters
\[
\chi_U(x)=(-1)^{|U\cap x|}
\]
satisfy
\[
L\chi_U=(n-2|U|)\chi_U.
\]
Since \(f\ne0\), equation (6) requires \(n\) even, and all Fourier terms of \(f\) have degree
\[
q=n/2.
\]

Also \(f(x+\mathbf1)=f(x)\), because switching complementary subsets gives the same graph. But every degree-\(q\) character changes by \((-1)^q\) under \(x\mapsto x+\mathbf1\). Hence \(q\) is even, proving \(4\mid n\).

It remains to bound \(a,b\). For any \(x\), the sum of \(f\) over the Hamming sphere of radius \(j\) around \(x\) is
\[
\sum_{d(x,y)=j}f(y)=K_j(q)f(x),
\]
where
\[
\sum_{j=0}^nK_j(q)z^j
=(1-z)^q(1+z)^q=(1-z^2)^q.
\]
Therefore
\[
K_{2r}(q)=(-1)^r\binom qr,\qquad K_{2r+1}(q)=0.
\]

The triangle inequality now gives
\[
\begin{aligned}
\|f\|_1
&\ge
\sum_{j=0}^n
\left|\sum_{d(x,y)=j}f(y)\right|\\
&=|f(x)|\sum_{r=0}^q\binom qr
=2^q|f(x)|.
\end{aligned}
\]
Here \(\|f\|_1=2\). Taking \(x\in A\) yields
\[
2\ge\frac{2^q}{a},
\]
so \(a\ge2^{q-1}\). Taking \(x\in B\) gives the same bound for \(b\). Dividing by two proves (5). ∎

### Interpretation through switching symmetries

Let \(\mathcal T(G)\) be the collection of triples spanning an odd number of edges, and let
\[
\Gamma(G)=\operatorname{Aut}(\mathcal T(G)).
\]
Then
\[
\rho(G)=\frac{|\Gamma(G)|}{|\operatorname{Aut}(G)|}. \tag{7}
\]

Indeed, switching preserves every triple parity. Conversely, if two labeled graphs have the same triple parities, their edgewise symmetric difference has even parity on every triangle and is therefore a cut: fixing a vertex \(r\), its edge indicators satisfy
\[
c_{ij}=c_{ir}+c_{jr}\pmod2.
\]
Thus the \(\Gamma(G)\)-orbit of \(G\) is exactly the set counted by \(\rho(G)\), and (7) follows from orbit–stabilizer.

In particular, for \(n\ge8\) divisible by \(4\), the sufficient condition
\[
|\Gamma(G)|<
2^{n/2-2}|\operatorname{Aut}(G)|
\]
guarantees reconstruction.

## 5. A quantitative random-graph consequence

**Theorem 9.** For the usual labeled random graph \(G(n,1/2)\),
\[
\Pr(G\text{ is not switching-reconstructible})
=O\!\left(n^2\,2^{-3n/2}\right).
\]

More explicitly, when \(4\mid n\) and \(n\ge8\), define
\[
U_n=\sum_{m=2}^n
(2n)^m\,2^{-m(2n-m-2)/4}.
\]
Then
\[
\Pr(G\text{ is not switching-reconstructible})
\le
\min\left\{1,\frac{U_n}{2^{n/2-2}-1}\right\}. \tag{8}
\]

### Proof

We bound \(\mathbb E(\rho(G)-1)\).

Every nontrivial switching cut \(S\) with \(G^S\cong G\) has a witnessing nonidentity permutation \(\sigma\) satisfying
\[
\sigma(G)=G^S.
\]
Suppose \(\sigma\) moves exactly \(m\) vertices.

There are at most \(2^m\) potentially feasible cuts \(S\), modulo complementation. To see this, all fixed vertices of \(\sigma\), when there are at least two, must have the same switching bit: edges between fixed vertices cannot change. Normalize that bit to zero. The cases of one or no fixed vertices give the same upper bound.

Put \(N=\binom n2\), and let \(c(\sigma)\) be the number of orbits of \(\sigma\) on unordered vertex pairs. For a fixed \(\sigma,S\), the condition \(\sigma(G)=G^S\) is either inconsistent, or leaves exactly one free edge bit per orbit. Its probability is therefore at most
\[
2^{-(N-c(\sigma))}.
\]

The number of unordered pairs fixed by \(\sigma\) is at most
\[
\binom{n-m}{2}+\frac m2.
\]
Every other pair orbit has size at least two. Consequently,
\[
N-c(\sigma)\ge\frac{m(2n-m-2)}4.
\]
There are at most \(n^m\) permutations with support size \(m\). Counting witnesses, possibly repeatedly, gives
\[
\mathbb E(\rho(G)-1)\le U_n. \tag{9}
\]

For completeness, \(U_n=O(n^2 2^{-n})\). If
\[
b_m=(2n)^m2^{-m(2n-m-2)/4},
\]
then
\[
b_2=16n^2 2^{-n}.
\]
Moreover, \(\log_2 b_m\) is convex in \(m\), so
\[
\sum_{m=3}^n b_m\le n\max\{b_3,b_n\}=o(n^2 2^{-n}).
\]

By Theorem 8, failure of reconstruction requires
\[
\rho(G)-1\ge2^{n/2-2}-1.
\]
Markov's inequality and (9) prove (8), and hence
\[
\Pr(\text{failure})=O(n^2 2^{-3n/2}).
\]
When \(4\nmid n\), the probability is zero by the cube argument above. ∎

## 6. The remaining gap

A counterexample on \(n\ge8\) vertices would have to satisfy all of the following:

- \(4\mid n\);
- both the graph and its complement are connected;
- \(\delta+\Delta\in\{n-2,n-1,n\}\);
- every vertex has a degree-admissible partner satisfying (3);
- its self-isomorphic switching orbit has size at least \(2^{n/2-2}\).

These restrictions are substantial, but they do not contradict one another. The argument does not exclude sufficiently large switching-symmetry orbits with the requisite local degree structure. No counterexample or proof for that remaining situation is obtained here, and I do not claim that the partial results above are absent from the existing literature.
