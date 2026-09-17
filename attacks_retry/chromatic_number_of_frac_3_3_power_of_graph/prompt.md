Attack the following open graph-theory problem.

Catalog id: chromatic_number_of_frac_3_3_power_of_graph
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/chromatic_number_of_frac_3_3_power_of_graph/
Original entry: http://www.openproblemgarden.org/op/chromatic_number_of_frac_3_3_power_of_graph

=== Problem statement (OpenProblemGarden) ===
Title: Chromatic number of $\frac{3}{3}$-power of graph
Let $ G $ be a graph and $ m,n\in \mathbb{N} $ . The graph $ G^{\frac{m}{n}} $ is defined to be the $ m $ -power of the $ n $ -subdivision of $ G $ . In other words, $ G^{\frac{m}{n}}=(G^{\frac{1}{n}})^m $ . Conjecture Let $ G $ be a graph with $ \Delta(G)\geq 2 $ . Then $ \chi(G^{\frac{3}{3}})\leq 2\Delta(G)+1 $ .

=== References listed by OpenProblemGarden ===
- [1] Mahsa Mozafari-Nia and M. N. Iradmusa, Simultaneous coloring of vertices and incidences of graphs, Australasian Journal of Combinatorics, Vol. 85, Mo. 3, pp. 287-307, 2023.
- [2] Mahsa Mozafari-Nia and M. N. Iradmusa, Simultaneous coloring of vertices and incidences of outerplanar graphs, Electronic Journal of Graph Theory and Applications, Vol.11, No.1, pp.245-262, 2023.
- [3] Mahsa Mozafari-Nia and M. N. Iradmusa, A note on coloring of 3/3-power of subquartic graphs, Australasian Journal of Combinatorics, Vol. 79, No. 3, pp. 454-460, 2021.
- [4] M. N. Iradmusa, A short proof of 7-colorability of 3/3-power of subcubic graphs, Iranian Journal of Science and Technology, Transactions A: Science, Vol. 44, No. 1, pp. 225-226, 2020.

=== Catalog page (statement + literature review) ===
Chromatic number of $\frac{3}{3}$-power of graph — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture $\chi(G^{3/3}) \leq 2\Delta(G)+1$ remains open in general. Anastos, Boyadzhiyska, Rathke, and Rué (2024) proved the asymptotically tight bound $\chi(G^{3/3}) \leq \Delta + C\log\Delta$ for all graphs $G$ (with $C=28$ for sufficiently large $\Delta$), which confirms the conjecture for all sufficiently large $\Delta$ and is in fact stronger than $2\Delta+1$ in that regime, but leaves the exact conjecture open for small-to-moderate values of $\Delta \geq 5$ not already handled by pre-posting results. Lower bounds show $\chi(G^{3/3}) \geq \Delta + \Omega(\log\Delta)$ for infinitely many $\Delta$, making the new upper bound essentially tight.

 Cited literature (1)

 
 
 
partial On the chromatic number of powers of subdivisions of graphs
 (2024)
 

 
 Michael Anastos, Simona Boyadzhiyska, Silas Rathke, Juanjo Rué · Discrete Applied Mathematics · arXiv:2404.05542 · doi:10.1016/j.dam.2024.10.002

Proves $\chi(G^{3/3}) \leq \Delta + C\log\Delta$ for all graphs $G$ with maximum degree $\Delta$ (with $C=28$ for large $\Delta$), confirming the Mozafari-Nia–Iradmusa conjecture asymptotically for large $\Delta$ and establishing a matching $\Omega(\log\Delta)$ lower bound.
 

 

 Reviewer notes. The DOI 10.1016/j.dam.2024.10.002 (Discrete Applied Mathematics, Vol. 360, pp. 506–511) was found in web search results and is consistent with the ISTA research-explorer metadata, but ScienceDirect returned HTTP 403 so the journal page could not be independently verified via WebFetch; the arXiv preprint is fully verified. A 2024 paper by Mozafari-Nia and Iradmusa on simultaneous coloring of hypercubes (Communications in Combinatorics and Optimization, Vol. 9(1), pp. 67–77) was mentioned in search results but the publisher's website was unreachable (ECONNREFUSED), so it was not cited. The Opuscula Mathematica paper on incidence coloring of graph fractional powers (vol. 43, no. 1) was also found but its PDF was binary-encoded and could not be read; it appears to predate the posting date in any case.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (web search enabled) · 235s.
 

Conjecture. Let $ G $ be a graph with $ \Delta(G)\geq 2 $ . Then $ \chi(G^{\frac{3}{3}})\leq 2\Delta(G)+1 $ .

Bibliography

 [1]
 Mahsa Mozafari-Nia and M. N. Iradmusa, Simultaneous coloring of vertices and incidences of graphs, Australasian Journal of Combinatorics, Vol. 85, Mo. 3, pp. 287-307, 2023.

 [2]
 Mahsa Mozafari-Nia and M. N. Iradmusa, Simultaneous coloring of vertices and incidences of outerplanar graphs, Electronic Journal of Graph Theory and Applications, Vol.11, No.1, pp.245-262, 2023.

 [3]
 Mahsa Mozafari-Nia and M. N. Iradmusa, A note on coloring of 3/3-power of subquartic graphs, Australasian Journal of Combinatorics, Vol. 79, No. 3, pp. 454-460, 2021.

 [4]
 M. N. Iradmusa, A short proof of 7-colorability of 3/3-power of subcubic graphs, Iranian Journal of Science and Technology, Transactions A: Science, Vol. 44, No. 1, pp. 225-226, 2020.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds for every finite simple graph of maximum degree at least 9, by a self-contained local-lemma argument.",
  "would_publish": false,
  "caveats": "Degrees 5–8 are not resolved here; the novelty of this threshold and the supplied literature have not been independently verified."
}
```

# A degree-threshold result

Throughout, graphs are finite and simple.

**Theorem.** Let \(D\ge 9\). If \(\Delta(G)\le D\), then
\[
\chi(G^{3/3})\le 2D+1.
\]

In particular, the conjecture holds whenever \(\Delta(G)\ge 9\). The proof below is independent of the asymptotic result quoted in the question.

## 1. A set-system sufficient condition

For each edge \(uv\), write its subdivided path as
\[
u-x_{uv}-x_{vu}-v.
\]
Thus \(x_{uv}\) is the internal vertex nearest \(u\).

The adjacency rules in \(G^{3/3}\) are:

- Original vertices \(u,v\) are adjacent exactly when \(uv\in E(G)\).
- An original vertex \(w\) is adjacent to \(x_{uv}\) exactly when \(w\in\{u,v\}\).
- Distinct internal vertices \(x_{uv},x_{ab}\) are adjacent exactly when
  \[
  u=a,\qquad v=a,\qquad\text{or}\qquad b=u.
  \]

Let \(\mathcal C\) be a color palette. For every vertex \(u\), choose a set
\[
S(u)\subseteq\mathcal C,\qquad T(u)=\mathcal C\setminus S(u).
\]

We will arrange that
\[
|T(u)|\ge D+1                                                     \tag{1}
\]
and, for every nonempty \(X\subseteq N(u)\),
\[
\left|\bigcup_{v\in X}\bigl(S(v)\cap T(u)\bigr)\right|
   \ge |X|+1.                                                     \tag{2}
\]

These conditions suffice to color \(G^{3/3}\) from \(\mathcal C\).

Indeed, first greedily color the original graph, choosing
\[
c(u)\in T(u).
\]
Condition (1) guarantees a proper choice. At each \(u\), consider the lists
\[
L_u(v)=\bigl(S(v)\cap T(u)\bigr)\setminus\{c(u)\},
\qquad v\in N(u).
\]
By (2), these lists satisfy Hall’s condition. Choose distinct representatives, and use the representative of \(L_u(v)\) as the color of \(x_{uv}\).

This is a proper coloring:

- Internal vertices with the same first coordinate receive distinct colors.
- The colors on \(x_{uv}\) and \(x_{vw}\) lie respectively in \(S(v)\) and \(T(v)\).
- The colors on \(x_{uv}\) and \(x_{wu}\) lie respectively in \(T(u)\) and \(S(u)\).
- The color of \(x_{uv}\) avoids \(c(u)\) by construction and avoids \(c(v)\) because it belongs to \(S(v)\), whereas \(c(v)\in T(v)\).

It remains to construct the sets satisfying (2).

## 2. Random sets and bad events

Fix \(D\ge9\), and put
\[
q=2D+1,\qquad s=D-2,\qquad t=D+3,\qquad
M_D=\binom{2D+1}{D-2}.
\]
Independently at every vertex, choose \(S(u)\) uniformly among the \(s\)-subsets of \([q]\). Then \(|T(u)|=t\), so (1) holds.

There are two types of bad events.

### Edge events

For \(uv\in E(G)\), let
\[
A_{uv}=\{|S(v)\setminus S(u)|\le1\}.
\]
Because all sets have the same size, this event is symmetric in \(u,v\). It covers the failures of (2) with \(|X|=1\).

Conditioning on \(S(u)\), there is one choice of \(S(v)\) with no element outside \(S(u)\), and \(st\) choices with exactly one element outside. Consequently
\[
\Pr(A_{uv})=\alpha_D
 :=\frac{1+st}{M_D}
 =\frac{D^2+D-5}{M_D}.                                           \tag{3}
\]

### Vertex events

Let \(B_u\) be the event that (2) fails for some \(X\subseteq N(u)\) with \(|X|\ge2\).

For fixed \(X\), \(|X|=k\), a failure implies that some \(k\)-subset \(Y\subseteq T(u)\) contains every set \(S(v)\cap T(u)\), \(v\in X\). Conditional on \(S(u)\), the probability for fixed \(X,Y\) is
\[
\left(\frac{\binom{s+k}{s}}{M_D}\right)^k.
\]
Therefore
\[
\Pr(B_u)\le \beta_D
 :=\sum_{k=2}^{D}F_{D,k},                                        \tag{4}
\]
where
\[
F_{D,k}
 =\binom Dk\binom{D+3}k
  \left(
    \frac{\binom{D+k-2}{D-2}}{\binom{2D+1}{D-2}}
  \right)^k.                                                     \tag{5}
\]

The numerical estimates needed below are
\[
\boxed{\quad
\alpha_D<\frac1{6D^2},
\qquad
\beta_D<\frac1{4(D^2+1)}
\quad(D\ge9).
\quad}                                                           \tag{6}
\]
A full verification, including the uniformity in \(D\), appears in Section 4.

## 3. Applying the asymmetric local lemma

Use the dependency graph in which two bad events are joined whenever their sets of underlying random variables overlap. The following bounds hold:

\[
\begin{array}{c|cc}
\text{event type}&\text{adjacent edge events}&\text{adjacent vertex events}\\ \hline
A_{uv}&2D-2&2D\\
B_u&D^2&D^2
\end{array}                                                       \tag{7}
\]

Here:

- \(A_{uv}\) depends only on \(S(u),S(v)\).
- \(B_u\) depends only on the variables indexed by \(N[u]\).
- The centers of vertex events adjacent to \(A_{uv}\) lie in
  \(N[u]\cup N[v]\), which has size at most \(2D\).
- There are at most \(D^2\) other vertices within distance two of \(u\).
- The number of edges incident with \(N[u]\) is at most \(D\,d(u)\le D^2\): summing degrees over \(N[u]\) gives at most \(d(u)(D+1)\), and the \(d(u)\) edges from \(u\) to its neighbors have been counted twice.

Assign local-lemma parameters
\[
x=\frac1{4D^2}\quad\text{to edge events},\qquad
y=\frac1{D^2+1}\quad\text{to vertex events}.
\]

For an edge event, Bernoulli’s inequality gives
\[
\begin{aligned}
(1-x)^{2D-2}(1-y)^{2D}
&\ge
\left(1-\frac1{2D}\right)
\left(1-\frac2D\right)\\
&>\frac23
\qquad(D\ge9).
\end{aligned}
\]
Thus
\[
x(1-x)^{2D-2}(1-y)^{2D}
>\frac1{6D^2}>\alpha_D.                                          \tag{8}
\]

For a vertex event,
\[
(1-x)^{D^2}\ge\frac34
\]
and
\[
(1-y)^{D^2}
=\left(1+\frac1{D^2}\right)^{-D^2}
>e^{-1}>\frac13.
\]
Hence
\[
y(1-x)^{D^2}(1-y)^{D^2}
>\frac1{4(D^2+1)}>\beta_D.                                       \tag{9}
\]

Equations (7)–(9) are precisely sufficient conditions for the asymmetric Lovász local lemma. With positive probability, no bad event occurs.

Absence of edge events gives (2) for singleton \(X\), and absence of vertex events gives it for all larger \(X\). Section 1 now provides a proper coloring using \(q=2D+1\) colors. This proves the theorem, subject only to the estimates established next.

## 4. Verification of the probability estimates

### 4.1. The edge-event estimate

At \(D=9\),
\[
M_9=\binom{19}{7}=50388,\qquad
\alpha_9=\frac{85}{50388}<\frac1{486}.
\]

Moreover,
\[
\frac{(D+1)^2\alpha_{D+1}}{D^2\alpha_D}
=
\frac{(D+1)^2}{D^2}
\frac{D^2+3D-3}{D^2+D-5}
\frac{(D-1)(D+4)}{(2D+3)(2D+2)}.
\]
For \(D\ge9\), the first two factors are each less than \(5/4\), and the third is less than \(1/3\). The ratio is therefore less than \(25/48<1\). This proves
\[
\alpha_D<\frac1{6D^2}
\qquad(D\ge9).
\]

### 4.2. The initial vertex-event estimate

For \(D=9\), the summands in (5) have denominator \(50388^k\). The following are deliberately rounded-up rational bounds:

\[
\begin{array}{c|r|r|r}
k&
\binom9k\binom{12}k&
\binom{7+k}{7}&
\text{upper bound on }10^6F_{9,k}\\ \hline
2&2376&36&1300\\
3&18480&120&260\\
4&62370&330&120\\
5&99792&792&100\\
6&77616&1716&130\\
7&28512&3432&210\\
8&4455&6435&330\\
9&220&11440&380
\end{array}
\]

Each entry in the final column means the exact integer-checkable inequality
\[
10^6\binom9k\binom{12}k\binom{7+k}{7}^{\,k}
<
(\text{displayed bound})\,50388^k.
\]
Summing gives
\[
\beta_9<0.002830<\frac3{1000}.                                   \tag{10}
\]

### 4.3. A uniform contraction estimate

We prove
\[
\beta_{D+1}\le\frac45\beta_D
\qquad(D\ge9).                                                   \tag{11}
\]

Put
\[
h=\left\lfloor\frac{D+3}{2}\right\rfloor.
\]
We will show
\[
F_{D+1,k}\le\frac25F_{D,k}
\quad(2\le k\le h),                                              \tag{12}
\]
and
\[
F_{D+1,k+1}\le\frac25F_{D,k}
\quad(h\le k\le D).                                              \tag{13}
\]

#### Lower half: fixed \(k\)

Directly from (5),
\[
\frac{F_{D+1,k}}{F_{D,k}}
=
\frac{(D+1)(D+4)}
     {(D+1-k)(D+4-k)}
\left(
\frac{(D+k-1)(D+4)}
     {(2D+3)(2D+2)}
\right)^k.                                                       \tag{14}
\]

For \(k\le h\), the expression inside parentheses is at most \(1/2\). The prefactor is at most \(5\), since
\[
\frac{(D+1)(D+4)}
     {(D+1-k)(D+4-k)}
\le
\frac{4(D+1)(D+4)}{(D-1)(D+5)}
\le5.
\]
For \(k=2\), the prefactor is less than \(3/2\); for \(k=3\), it is less than \(2\). Consequently (14) is at most, respectively,
\[
\frac38,\qquad \frac14,\qquad \frac5{16}\quad(k\ge4).
\]
All three bounds are below \(2/5\), proving (12).

#### Upper half: fixed complementary parameter

Set
\[
r=D+3-k.
\]
In the range of (13),
\[
3\le r\le\frac{D+4}{2}.
\]
Using falling factorials,
\[
F_{D,D+3-r}
=
\binom D{r-3}\binom{D+3}r
\left(\frac{(D+3)_r}{(2D+1)_r}\right)^{D+3-r}.                    \tag{15}
\]

For fixed \(r\), define
\[
L_r(z)
=(z+3-r)\sum_{j=0}^{r-1}
  \log\frac{z+3-j}{2z+1-j}.
\]
The derivative of its \(j\)-th summand is
\[
\log\frac{z+3-j}{2z+1-j}
+
\frac{(z+3-r)(j-5)}
     {(z+3-j)(2z+1-j)}.                                         \tag{16}
\]

For \(z\ge D\ge9\):

- If \(j<5\), (16) is at most \(\log(2/3)\).
- If \(j\ge5\), put
  \[
  a=\frac{j-5}{2z+1-j}.
  \]
  Since \(j\le r-1\), expression (16) is at most
  \[
  \log\frac{1-a}{2}+a\le-\log2.
  \]

Integrating from \(D\) to \(D+1\) yields
\[
\exp\bigl(L_r(D+1)-L_r(D)\bigr)
\le
\left(\frac23\right)^{\min(r,5)}
2^{-\max(r-5,0)}.                                                \tag{17}
\]

The ratio of the binomial prefactors in (15) is
\[
\frac{(D+1)(D+4)}{(D+4-r)^2}.
\]
For \(r=3,4,5\), this is at most \(4/3,2,3\), respectively. For \(r\ge6\), it is at most \(4\), using \(r\le(D+4)/2\).

Multiplying these bounds by (17), the resulting ratio is at most
\[
\frac{32}{81}<\frac25
\]
for \(r=3,4,5\), and at most
\[
\frac{64}{243}<\frac25
\]
for \(r\ge6\). This proves (13).

Finally, split the sum for \(\beta_{D+1}\) at \(h\), applying (12) below the split and (13) above it:
\[
\begin{aligned}
\beta_{D+1}
&\le
\frac25\sum_{k=2}^{h}F_{D,k}
+
\frac25\sum_{k=h}^{D}F_{D,k}\\
&=\frac25\bigl(\beta_D+F_{D,h}\bigr)
\le\frac45\beta_D.
\end{aligned}
\]
Thus (11) holds.

### 4.4. Finishing the vertex-event estimate

For \(D\ge9\),
\[
\frac45\bigl((D+1)^2+1\bigr)\le D^2+1.
\]
Combining this with (10)–(11), we obtain
\[
(D^2+1)\beta_D
\le82\beta_9
<82\cdot\frac3{1000}
<\frac14.
\]
Therefore
\[
\beta_D<\frac1{4(D^2+1)}
\qquad(D\ge9),
\]
completing the proof of (6) and of the theorem.

## 5. Scope and remaining gap

The unconditional result proved here is
\[
\boxed{\chi(G^{3/3})\le2\Delta(G)+1
       \quad\text{whenever }\Delta(G)\ge9.}
\]

For completeness, the case \(\Delta=2\) is elementary. Components are paths and cycles. Cubes of subdivided paths are \(4\)-colorable. A subdivided cycle has length \(3n\), \(n\ge3\); this length is expressible as \(4a+5b\). Concatenating blocks \(1234\) and \(12345\) cyclically gives a proper \(5\)-coloring of its cube, since every four cyclically consecutive entries are distinct.

Taking the degree-\(3\) and degree-\(4\) results reported in the question as established, the remaining degree values are therefore
\[
\boxed{\Delta\in\{5,6,7,8\}.}
\]

I do not resolve these four cases, and I make no claim that the degree-\(9\) threshold has not appeared elsewhere.
