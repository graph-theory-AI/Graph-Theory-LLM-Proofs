Attack the following open graph-theory problem.

Catalog id: weighted_colouring_of_hexagonal_graphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory » Coloring » Vertex coloring
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/weighted_colouring_of_hexagonal_graphs/
Original entry: http://www.openproblemgarden.org/op/weighted_colouring_of_hexagonal_graphs
Problem attributed to: McDiarmid, Colin, Reed, Bruce A. (posted 2013-03-13)

=== Problem statement (OpenProblemGarden) ===
Title: Weighted colouring of hexagonal graphs.
Conjecture There is an absolute constant $ c $ such that for every hexagonal graph $ G $ and vertex weighting $ p:V(G)\rightarrow \mathbb{N} $ , $$\chi(G,p) \leq \frac{9}{8}\omega(G,p) + c $$

=== Discussion / context (OpenProblemGarden) ===
A hexagonal graph is an induced subgraph of the triangular lattice. The triangular lattice $ TL $ may be described as follows. The vertices are all integer linear combinations $ a\mathbf{e_1} + b\mathbf{e_2} $ of the two vectors $ \mathbf{e_1}=(1,0) $ and $ \mathbf{e_2}=(\frac{1}{2}, \frac{\sqrt{3}}{2}) $ . Two vertices are adjacent when the Euclidean distance between them is 1. Let $ G $ be a graph and $ p $ a vertex weighting $ p:V(G)\rightarrow \mathbb{N} $ . The weighted clique number of $ (G,p) $ , denoted by $ \omega(G,p) $ , is the maximum weight of a clique, that is $ \max \{p(C) \tq C \mbox{ clique of } G\} $ , where $ p(C)=\sum_{v\in C} p(v) $ . A $ k $ -colouring of a $ (G,p) $ is a mapping $ C:V(G)\ra {\cal P}(\{1, \dots , k\}) $ such that for every vertex $ v\in V(G) $ , $ |C(v)|=p(v) $ and for all edge $ uv\in E(G) $ , $ C(u)\cap C(v)=\emptyset $ . The chromatic number of $ (G,p) $ , denoted by $ \chi(G,p) $ , is the least integer $ t $ such that $ (G,p) $ admits a $ t $ -colouring. The conjecture would be tight because of $ C_9 $ the cycle of length 9. The maximum size of stable set in $ C_9 $ is $ 4 $ . Thus $ \chi(C_9,\mathbf{k})\geq 9k/4 $ and $ \omega(G,\mathbf{k})=2k $ , where $ \mathbf{k} $ is the all $ k $ function. McDiarmid and Reed [MR] proved that $ \chi(G,p)\leq \frac{4\omega(G,p)+1}{3} $ for any hexagonal graph $ G $ and vertex weighting $ p $ . Havet [H] proved that if a hexagonal graph $ G $ is triangle-free, then $ \chi(G,p)\leq\frac{7}{6}\omega(G,p) + 5 $ (See also [SV]). The conjecture would be implied by the following one, where $ \mathbf{4} $ is the all $ 4 $ function. Conjecture $ \chi(G,\mathbf{4})\leq 9 $ for every hexagonal graph. Since $ \chi(G,\mathbf{4}) \geq 4|V(G)|/\alpha(G) $ , where $ \alpha(G) $ is the stability number (the maximum size of a stable set). A first step to this later conjecture would be to prove the following conjecture of McDiarmid. Conjecture Let $ G $ be a triangle-free hexagonal graph. $$\alpha(G)\geq \frac{4}{9}|V(G)|$$

=== References listed by OpenProblemGarden ===
- [H] F.Havet. Channel assignment and multicolouring of the induced subgraphs of the triangular lattice. Discrete Mathematics 233:219--231, 2001.
- *[MR] C. McDiarmid and B. Reed. Channel assignment and weighted coloring, Networks, 36:114--117, 2000.
- [SV] K. S. Sudeep and S. Vishwanathan. A technique for multicoloring triangle-free hexagonal graphs. Discrete Mathematics, 300(1-3), 256--259, 2005.

=== Catalog page (statement + literature review) ===
Weighted colouring of hexagonal graphs. — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture that $\chi(G,p) \leq \frac{9}{8}\omega(G,p) + c$ for every hexagonal graph remains open. Žerovnik (2016) improved the best-known upper bound on the asymptotic ratio from $\frac{4}{3}$ (McDiarmid–Reed 2000) to $\frac{5}{4}$, showing $\chi(G,p) \leq 15\lfloor\omega(G,p)/12\rfloor + 18$. Godin and Togni (2018) developed reducible-configuration techniques and provided computational evidence that the implied $(9,4)$-colorability sub-conjecture holds across millions of randomly generated triangle-free hexagonal graphs, though no complete proof has appeared.

 Cited literature (2)

 
 
 
partial Improved approximative multicoloring of hexagonal graphs
 (2016)
 

 
 Janez Žerovnik · arXiv preprint · arXiv:1606.01328 · doi:10.48550/arXiv.1606.01328

Improves the best-known asymptotic ratio from 4/3 to 5/4, establishing χ(G,p) ≤ 15⌊ω(G,p)/12⌋ + 18 for every hexagonal graph.
 

 
 
partial New reducible configurations for graph multicoloring with application to the experimental resolution of McDiarmid-Reed's Conjecture (extended version)
 (2018)
 

 
 Jean-Christophe Godin, Olivier Togni · arXiv preprint · arXiv:1812.01911

Develops reducible-configuration tools for (a,b)-colorings and provides computational evidence that all tested triangle-free induced subgraphs of the triangular lattice are (9,4)-colorable.
 

 

 Reviewer notes. The Žerovnik 2016 paper was listed as 'submitted to Information Processing Letters' but journal publication could not be confirmed; cited as arXiv preprint. The Godin–Togni paper (1812.01911) was last revised October 2023 but remains without a confirmed journal publication. A DMTCS 2013 paper by Witkowski–Žerovnik on a 33/24-competitive distributed algorithm is related but addresses a different competitive-ratio setting (not the conjecture directly). No proof or disproof of the full conjecture was found.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 01) (web search enabled).
 

Conjecture. There is an absolute constant $ c $ such that for every hexagonal graph $ G $ and vertex weighting $ p:V(G)\rightarrow \mathbb{N} $ , $$\chi(G,p) \leq \frac{9}{8}\omega(G,p) + c $$

Discussion

A hexagonal graph is an induced subgraph of the triangular lattice. The triangular lattice $ TL $ may be described as follows. The vertices are all integer linear combinations $ a\mathbf{e_1} + b\mathbf{e_2} $ of the two vectors $ \mathbf{e_1}=(1,0) $ and $ \mathbf{e_2}=(\frac{1}{2}, \frac{\sqrt{3}}{2}) $ . Two vertices are adjacent when the Euclidean distance between them is 1. Let $ G $ be a graph and $ p $ a vertex weighting $ p:V(G)\rightarrow \mathbb{N} $ . The weighted clique number of $ (G,p) $ , denoted by $ \omega(G,p) $ , is the maximum weight of a clique, that is $ \max \{p(C) \tq C \mbox{ clique of } G\} $ , where $ p(C)=\sum_{v\in C} p(v) $ . A $ k $ -colouring of a $ (G,p) $ is a mapping $ C:V(G)\ra {\cal P}(\{1, \dots , k\}) $ such that for every vertex $ v\in V(G) $ , $ |C(v)|=p(v) $ and for all edge $ uv\in E(G) $ , $ C(u)\cap C(v)=\emptyset $ . The chromatic number of $ (G,p) $ , denoted by $ \chi(G,p) $ , is the least integer $ t $ such that $ (G,p) $ admits a $ t $ -colouring. The conjecture would be tight because of $ C_9 $ the cycle of length 9. The maximum size of stable set in $ C_9 $ is $ 4 $ . Thus $ \chi(C_9,\mathbf{k})\geq 9k/4 $ and $ \omega(G,\mathbf{k})=2k $ , where $ \mathbf{k} $ is the all $ k $ function. McDiarmid and Reed [MR] proved that $ \chi(G,p)\leq \frac{4\omega(G,p)+1}{3} $ for any hexagonal graph $ G $ and vertex weighting $ p $ . Havet [H] proved that if a hexagonal graph $ G $ is triangle-free, then $ \chi(G,p)\leq\frac{7}{6}\omega(G,p) + 5 $ (See also [SV]). The conjecture would be implied by the following one, where $ \mathbf{4} $ is the all $ 4 $ function. Conjecture $ \chi(G,\mathbf{4})\leq 9 $ for every hexagonal graph. Since $ \chi(G,\mathbf{4}) \geq 4|V(G)|/\alpha(G) $ , where $ \alpha(G) $ is the stability number (the maximum size of a stable set). A first step to this later conjecture would be to prove the following conjecture of McDiarmid. Conjecture Let $ G $ be a triangle-free hexagonal graph. $$\alpha(G)\geq \frac{4}{9}|V(G)|$$

Bibliography

 [H]
 F.Havet. Channel assignment and multicolouring of the induced subgraphs of the triangular lattice . Discrete Mathematics 233:219--231, 2001.
 Channel assignment and multicolouring of the induced subgraphs of the triangular lattice

★ [MR]
 C. McDiarmid and B. Reed. Channel assignment and weighted coloring, Networks, 36:114--117, 2000.

 [SV]
 K. S. Sudeep and S. Vishwanathan. A technique for multicoloring triangle-free hexagonal graphs . Discrete Mathematics, 300(1-3), 256--259, 2005.
 A technique for multicoloring triangle-free hexagonal graphs

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For series-parallel hexagonal graphs, the sharp bound chi(G,p) <= floor((9 omega(G,p)+6)/8) holds.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture is not settled; novelty of this special case is not claimed."
}
```

# A sharp special case

I prove the conjectured coefficient, with the best possible additive constant, for **series-parallel hexagonal graphs**.

Here a graph is series-parallel if each block containing an edge admits a two-terminal construction from edges by series and parallel composition. This is the usual \(K_4\)-minor-free class; in particular, it includes all outerplanar graphs.

**Theorem.** Let \(G\) be a finite series-parallel hexagonal graph, let \(p:V(G)\to\mathbb Z_{\ge0}\), and put \(W=\omega(G,p)\). Then
\[
\boxed{\quad
\chi(G,p)\le
B(W):=
W+\left\lceil\frac{\lfloor W/2\rfloor}{4}\right\rceil
=
\left\lfloor\frac{9W+6}{8}\right\rfloor
\le \frac98W+\frac34.
\quad}
\]
For every positive integer \(W\), some series-parallel hexagonal graph with weighted clique number \(W\) attains \(B(W)\).

The proof is self-contained apart from the standard structural characterization of series-parallel graphs just mentioned. I do not claim novelty for the multicolouring lemma below or for this special case.

## 1. Odd holes in the triangular lattice

We first record the geometric fact responsible for the coefficient \(9/8\).

**Lemma 1.** Every induced odd cycle of the triangular lattice is either a triangle or has length at least \(9\).

**Proof.** Consider an induced cycle of length \(n\ge4\), oriented counterclockwise in the natural plane embedding.

Its edge directions are among the six unit lattice directions. A turn of \(120^\circ\) or \(-120^\circ\) would make the vertices immediately before and after the turn adjacent, giving a chord. A \(180^\circ\) turn would repeat a vertex. Consequently every turn is \(60^\circ\), \(0^\circ\), or \(-60^\circ\).

Let their respective numbers be \(n_+,n_0,n_-\). The total turning angle gives
\[
n_+-n_-=6.
\]
In particular, \(n\ge6\), excluding induced \(5\)-cycles.

If \(n=7\), necessarily
\[
n_+=6,\qquad n_-=0,\qquad n_0=1.
\]
Thus the seven edge directions consist of all six unit lattice directions once, with one direction repeated. Their vector sum is the repeated unit vector, not zero. This contradicts closure of the cycle. Hence there is no induced \(7\)-cycle. \(\square\)

Because a hexagonal graph is an **induced** lattice subgraph, the lemma also applies to its induced cycles.

## 2. Exact multicolouring feasibility for series-parallel graphs

The following lemma supplies the combinatorial part of the proof.

**Lemma 2.** Let \(H\) be series-parallel, let \(p\) be a nonnegative integer demand function, and let \(K\) be a nonnegative integer. Then \(H\) has a \(K\)-colouring of its demands if and only if
\[
\begin{aligned}
p(v)&\le K &&\text{for every vertex }v,\\
p(u)+p(v)&\le K &&\text{for every edge }uv,\\
p(C)&\le \frac{|C|-1}{2}K
&&\text{for every odd cycle }C.
\end{aligned}
\tag{1}
\]

The necessity is immediate: each colour appears on at most \((|C|-1)/2\) vertices of an odd cycle. We prove sufficiency, including the integrality assertion.

### 2.1 The terminal-overlap invariant

Let \(H\) be a two-terminal series-parallel graph with terminals \(s,t\), having demands
\[
a=p(s),\qquad c=p(t).
\]
Fix a palette of \(K\) colours. We characterize the possible values of
\[
z=|C(s)\cap C(t)|.
\]

For an \(s\)-\(t\) path \(P\), let \(\ell(P)\) denote its number of edges and let \(p(P)\) include both endpoint demands. Define
\[
E_H=\max_{\substack{P\text{ an }s\text{-}t\text{ path}\\ \ell(P)\text{ even}}}
\left(p(P)-\frac{\ell(P)}2K\right)
\]
and
\[
O_H=\min_{\substack{P\text{ an }s\text{-}t\text{ path}\\ \ell(P)\text{ odd}}}
\left(\frac{\ell(P)-1}{2}K-p(P)+a+c\right).
\]
An empty maximum is \(-\infty\), and an empty minimum is \(+\infty\).

We prove by induction on the construction that, under (1), the feasible overlaps are exactly the nonempty integer interval
\[
\boxed{\quad
\max(0,a+c-K,E_H)\ \le z\le\ \min(a,c,O_H).
\quad}
\tag{2}
\]

For a single edge, \(E_H=-\infty\), \(O_H=0\), and (1) makes this interval exactly \(\{0\}\).

We will repeatedly use the following elementary observation: two ordered pairs of subsets of a \(K\)-element palette, with the same two sizes and the same intersection size, are related by a permutation of the palette. Their four Venn-diagram regions have identical sizes.

### 2.2 Parallel composition

Suppose \(H\) is the parallel composition of \(H_1,H_2\), sharing only their terminals. Write their feasible intervals as \([L_1,U_1]\) and \([L_2,U_2]\).

An overlap is feasible in \(H\) exactly when it is feasible in both pieces: colour the pieces independently, then permute one palette to identify the two terminal colour sets. Thus the feasible interval is
\[
[\max(L_1,L_2),\ \min(U_1,U_2)].
\tag{3}
\]

It remains to show that this intersection is nonempty. Each child interval is nonempty. Their elementary bounds
\[
\max(0,a+c-K),\qquad \min(a,c)
\]
are the same. Therefore disjointness could occur only through an inequality
\[
E_{H_i}>O_{H_j},\qquad i\ne j.
\]
Choose an even terminal path in \(H_i\) of length \(2r\), and an odd terminal path in \(H_j\) of length \(2q+1\), witnessing this inequality. They form an odd cycle \(C\), and the inequality says precisely
\[
p(C)>(r+q)K,
\]
contrary to (1).

Every terminal path of a parallel composition belongs to one of its pieces. Hence (3) is exactly (2).

### 2.3 Series composition: the integer issue

Suppose \(H_1\), with terminals \(s,v\), and \(H_2\), with terminals \(v,t\), are composed in series. Write
\[
p(s)=a,\qquad p(v)=b,\qquad p(t)=c.
\]
Let the child overlap intervals be \([L_1,U_1]\) and \([L_2,U_2]\).

Choose overlaps
\[
x=|C(s)\cap C(v)|,\qquad
y=|C(v)\cap C(t)|.
\]
For fixed \(x,y\), elementary subset counting shows that the possible values of \(z=|C(s)\cap C(t)|\) are all the integers between
\[
\begin{aligned}
z_{\min}(x,y)
&=\max(0,x+y-b)
 +\max(0,a+c-x-y-(K-b)),\\
z_{\max}(x,y)
&=\min(x,y)+\min(a-x,c-y).
\end{aligned}
\tag{4}
\]
Indeed, choose the intersections inside \(C(v)\) and outside \(C(v)\) independently. Each of these two intersections ranges through an integer interval, and their sum does too. The palette-permutation observation then realizes the desired three terminal sets using colourings of the two entire pieces.

Equivalently,
\[
\begin{aligned}
z_{\min}(x,y)
&=\max(0,a+c-K,x+y-b,a+b+c-K-x-y),\\
z_{\max}(x,y)
&=\min(a,c,a-x+y,c+x-y).
\end{aligned}
\tag{5}
\]

As \(x,y\) range over their integer rectangle, the union of the intervals in (4) has no integer gaps. To see this, move between adjacent points of the rectangle: both endpoints in (5) change by at most one, so consecutive nonempty integer intervals overlap or are adjacent.

Minimizing the first expression in (5), which depends only on \(x+y\), and maximizing the second, which depends only on \(x-y\), therefore gives the exact feasible interval \([L,U]\), where
\[
\begin{aligned}
L=\max\bigl(&0,a+c-K,\,
L_1+L_2-b,\,
a+b+c-K-U_1-U_2\bigr),\\
U=\min\bigl(&a,c,\,
a-L_1+U_2,\,
c+U_1-L_2\bigr).
\end{aligned}
\tag{6}
\]
It is nonempty because the child intervals are nonempty and any pair of child colourings can be aligned at \(v\).

For completeness, the path bounds agree exactly with (6). Concatenating a path in \(H_1\) and a path in \(H_2\) gives the identities
\[
\begin{array}{c|c}
\text{parities of the two paths}&\text{bound for the concatenated path}\\ \hline
\text{even, even}&E=E_1+E_2-b\\
\text{odd, odd}&E=a+b+c-K-O_1-O_2\\
\text{even, odd}&O=a-E_1+O_2\\
\text{odd, even}&O=c+O_1-E_2 .
\end{array}
\tag{7}
\]
Here the symbols on the right denote the values for the individual paths.

Taking extrema in (7) and substituting the child formulas (2) into (6) yields
\[
L=\max(0,a+c-K,E_H),\qquad
U=\min(a,c,O_H).
\]
The elementary bounds introduce no additional terms: nonemptiness of the child intervals gives
\[
E_{H_1}\le\min(a,b),\qquad
O_{H_1}\ge\max(0,a+b-K),
\]
and the analogous inequalities for \(H_2\); these make all mixed elementary terms redundant in the expansion of (6).

This proves the invariant (2), and hence sufficiency for two-terminal series-parallel graphs.

Finally, colour the blocks of \(H\) successively. At each cutvertex, permute the new block’s palette to match its already assigned colour set. Different components reuse the same palette, and isolated vertices are handled by the first inequality in (1). This proves Lemma 2. \(\square\)

## 3. Applying the lemma to hexagonal graphs

Let
\[
d=\left\lceil\frac{\lfloor W/2\rfloor}{4}\right\rceil,
\qquad K=W+d=B(W).
\]
Vertex and edge inequalities in (1) hold because \(K\ge W\). We verify all odd-cycle inequalities.

### Induced odd cycles

For a triangle \(T\),
\[
p(T)\le W\le K.
\]

Now let \(C\) be an induced odd cycle of length \(2r+1\ge9\), so \(r\ge4\). Summing the edge inequalities around \(C\) gives
\[
2p(C)\le (2r+1)W.
\]
Since demands are integral,
\[
p(C)\le rW+\lfloor W/2\rfloor.
\]
By the definition of \(d\),
\[
\lfloor W/2\rfloor\le4d\le rd.
\]
Consequently
\[
p(C)\le r(W+d)=rK.
\tag{8}
\]

Lemma 1 shows that these are all induced odd-cycle cases.

### Odd cycles with chords

We use induction on the cycle length. Let an odd cycle \(C\) have a chord. The chord and one of the two paths along \(C\) form a shorter odd cycle \(C'\), say of length \(2s+1\).

If \(|C|=2r+1\), the vertices of \(C\) outside \(C'\) form a path with \(2(r-s)\) vertices. Pair its consecutive vertices into \(r-s\) edges. Thus
\[
p(C\setminus V(C'))\le(r-s)K.
\]
By induction,
\[
p(C')\le sK.
\]
Adding gives \(p(C)\le rK\), as required.

We have now checked every inequality in (1). Lemma 2 supplies the \(K\)-colouring and proves the theorem’s upper bound.

Notice that this odd-cycle verification works for **every** hexagonal graph. The series-parallel hypothesis is used precisely when turning these necessary inequalities into an integral multicolouring.

## 4. Sharpness, including the rounding term

In integer lattice coordinates \((a,b)\), the following vertices, in cyclic order, induce a \(9\)-cycle:
\[
\begin{split}
&(0,0),(1,0),(2,0),(2,1),(1,2),\\
&(0,3),(-1,3),(-1,2),(-1,1).
\end{split}
\tag{9}
\]
Consecutive differences are unit lattice directions, and no nonconsecutive pair has such a difference.

Every stable set of this cycle has size at most \(4\). Hence any demand function on it satisfies
\[
\chi(C_9,p)\ge \left\lceil\frac{p(V(C_9))}{4}\right\rceil.
\tag{10}
\]

If \(W=2h\ge2\), assign demand \(h\) everywhere. Then
\[
\omega(C_9,p)=2h,\qquad
\chi(C_9,p)\ge
\left\lceil\frac{9h}{4}\right\rceil
=2h+\left\lceil\frac h4\right\rceil
=B(W).
\]

If \(W=2h+1\ge3\), choose a stable set of four vertices, assign demand \(h+1\) on it, and demand \(h\) on the other five vertices. Then
\[
\omega(C_9,p)=2h+1,\qquad p(V(C_9))=9h+4,
\]
so
\[
\chi(C_9,p)\ge
\left\lceil\frac{9h+4}{4}\right\rceil
=2h+1+\left\lceil\frac h4\right\rceil
=B(W).
\]
The upper bound already proved makes these inequalities equalities. For \(W=1\), a single vertex attains \(B(1)=1\).

Thus \(B(W)\) is the exact best bound as a function of \(W\) within this class. In particular, taking uniform demand \(4q+1\) on \(C_9\) gives
\[
W=8q+2,\qquad
\chi=9q+3=\frac98W+\frac34.
\]
Neither the asymptotic coefficient \(9/8\) nor the additive constant \(3/4\) can be decreased in this special-case theorem.

## 5. Consequences and the remaining gap

If \(G\) is also triangle-free, then the all-\(4\) demand has weighted clique number at most \(8\). Therefore
\[
\chi(G,\mathbf4)\le B(8)=9.
\]
The nine colour classes are stable sets and contain altogether \(4|V(G)|\) vertex incidences, giving
\[
\alpha(G)\ge \frac49|V(G)|.
\]
Thus both auxiliary conjectures hold for triangle-free series-parallel hexagonal graphs.

The unrestricted problem is not resolved by this argument. Hexagonal graphs can have \(K_4\) minors—for example, the graph induced by a lattice vertex and its six neighbours does. The terminal-overlap induction above depends essentially on series and parallel composition; it does not establish that the clique and odd-cycle inequalities suffice for arbitrary hexagonal graphs, even with a universal additive error.

Finally, the contextual statement
\[
\chi(G,\mathbf4)\le9\quad\text{“for every hexagonal graph”}
\]
needs the **triangle-free** qualification: a lattice triangle has \(\chi(K_3,\mathbf4)=12\). This does not invalidate the main weighted conjecture.
