Attack the following open graph-theory problem.

Catalog id: minimal_graphs_with_a_prescribed_number_of_spanning_trees
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/minimal_graphs_with_a_prescribed_number_of_spanning_trees/
Original entry: http://www.openproblemgarden.org/op/minimal_graphs_with_a_prescribed_number_of_spanning_trees
Problem attributed to: Azarija, Jernej, Skrekovski, Riste (posted 2012-04-22)

=== Problem statement (OpenProblemGarden) ===
Title: Minimal graphs with a prescribed number of spanning trees
Conjecture Let $ n \geq 3 $ be an integer and let $ \alpha(n) $ denote the least integer $ k $ such that there exists a simple graph on $ k $ vertices having precisely $ n $ spanning trees. Then $ \alpha(n) = o(\log{n}). $

=== Discussion / context (OpenProblemGarden) ===
Observe that $ \alpha(n) $ is well defined for $ n \geq 3 $ since $ C_n $ has $ n $ spanning trees. The function was introduced by Sedlacek [S] who has shown that for large enough $ n $ $ \alpha(n) \leq \frac{n+6}{3} \mbox{if } n \equiv 0 \pmod{3} $ and $ \alpha(n) \leq \frac{n+4}{3} \mbox{if } n \equiv 2 \pmod{3}. $ Using the fact that almost all positive integers $ n $ are expressible as $ n = ab+ac+bc $ for integers $ 0 < a < b < c $ it can be shown [A] that for large enough $ n $ $ \alpha(n) \leq \frac{n+4}{3} \mbox{if } n \equiv 2 \pmod{3} $ and $ \alpha(n) \leq \frac{n+9}{4} $ otherwise. Moreover, the only fixed points of $ \alpha $ are 3, 4, 5, 6, 7, 10, 13 and 22. The conjecture is motivated by the following graph (ploted for a very small sample of vertices) The conjecture [C] is justifiable for highly composite numbers $ n $ since in this case one can construct the graph obtained after taking cycles $ C_{p_1}, \ldots,C_{p_k} $ for every odd prime factor $ p_i $ of $ n $ .

=== References listed by OpenProblemGarden ===
- [S] J. Sedlacek, On the minimal graph with a given number of spanning trees, Canad. Math. Bull. 13 (1970) 515-517.
- [A] J. Azarija, R. Skrekovski, Euler's idoneal numbers and an inequality concerning minimal graphs with a prescribed number of spanning trees, IMFM preprints 49 (2011) Link to paper
- * [C] Minimal graphs with a prescribed number of spanning trees

=== Catalog page (statement + literature review) ===
Minimal graphs with a prescribed number of spanning trees — Graph-theory open problems

 
 Status
 partial
 high confidence
 

 The conjecture $\alpha(n) = o(\log n)$ remains open, but significant progress has been made. Stong (2022) proved a weak version: $\alpha(n) = O((\log n)^{3/2} / \log\log n)$, the current state of the art. More recently, Alon, Bucć, and Gishboliner (2025) proved a modular analogue: for any $N$ and $u < N$, there exists a planar graph on $O(\log N)$ vertices whose spanning tree count is $\equiv u \pmod{N}$.

 Cited literature (2)

 
 
 
partial Minimal graphs with a prescribed number of spanning trees
 (2022)
 

 
 Richard Stong · Australasian Journal of Combinatorics

Proves $\alpha(n) = O((\log n)^{3/2} / \log\log n)$, a weak version of the conjecture $\alpha(n) = o(\log n)$, using algebraic number theory.
 

 
 
partial The spanning tree spectrum: improved bounds and simple proofs
 (2025)
 

 
 Noga Alon, Matija Bucć, Lior Gishboliner · arXiv preprint · arXiv:2503.23648

Proves a modular analogue of the conjecture: for any $N$ and $u < N$, there exists a planar graph on $O(\log N)$ vertices with spanning tree count $\equiv u \pmod{N}$; the full conjecture $\alpha(t) = O(\log t)$ is explicitly noted as still open.
 

 

 Reviewer notes. The Stong (2022) AJC paper PDF could not be directly extracted by WebFetch (binary content), but title/author/year were confirmed via the AJC volume 82 table-of-contents page and corroborated by multiple search results; the main result is also cited as state-of-the-art by the Alon et al. (2025) paper. No arXiv preprint was found for Stong's paper. The Alon et al. paper (arXiv:2503.23648, submitted March 2025) was independently verified via both the abstract and HTML pages.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 07) (web search enabled).
 

Conjecture. Let $ n \geq 3 $ be an integer and let $ \alpha(n) $ denote the least integer $ k $ such that there exists a simple graph on $ k $ vertices having precisely $ n $ spanning trees. Then $ \alpha(n) = o(\log{n}). $

Keywords:
number of spanning trees, asymptotics

Discussion

Observe that $ \alpha(n) $ is well defined for $ n \geq 3 $ since $ C_n $ has $ n $ spanning trees. The function was introduced by Sedlacek [S] who has shown that for large enough $ n $ $ \alpha(n) \leq \frac{n+6}{3} \mbox{if } n \equiv 0 \pmod{3} $ and $ \alpha(n) \leq \frac{n+4}{3} \mbox{if } n \equiv 2 \pmod{3}. $ Using the fact that almost all positive integers $ n $ are expressible as $ n = ab+ac+bc $ for integers $ 0 < a < b < c $ it can be shown [A] that for large enough $ n $ $ \alpha(n) \leq \frac{n+4}{3} \mbox{if } n \equiv 2 \pmod{3} $ and $ \alpha(n) \leq \frac{n+9}{4} $ otherwise. Moreover, the only fixed points of $ \alpha $ are 3, 4, 5, 6, 7, 10, 13 and 22. The conjecture is motivated by the following graph (ploted for a very small sample of vertices) The conjecture [C] is justifiable for highly composite numbers $ n $ since in this case one can construct the graph obtained after taking cycles $ C_{p_1}, \ldots,C_{p_k} $ for every odd prime factor $ p_i $ of $ n $ .

Bibliography

 [S]
 J. Sedlacek, On the minimal graph with a given number of spanning trees, Canad. Math. Bull. 13 (1970) 515-517.

 [A]
 J. Azarija, R. Skrekovski, Euler's idoneal numbers and an inequality concerning minimal graphs with a prescribed number of spanning trees, IMFM preprints 49 (2011) Link to paper
 Link to paper

★ [C]
 Minimal graphs with a prescribed number of spanning trees
 Minimal graphs with a prescribed number of spanning trees

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An explicit construction gives alpha(n) ~ log n/log log n when P(n) = (log n)^{o(1)}, and proves the conjecture whenever sum_{p|n} p^2 = o(log n).",
  "would_publish": false,
  "caveats": "Only restricted families are covered; prime inputs remain untreated, and novelty of these partial results is not claimed."
}
```

## 1. Partial result

Write \(\tau(G)\) for the number of spanning trees of \(G\), and define
\[
L=\log n,\qquad
P(n)=\max\{p:p\mid n,\ p\text{ prime}\},\qquad
S(n)=\sum_{\substack{p\mid n\\p\text{ prime}}}p^2.
\]
The sum defining \(S(n)\) is over **distinct** prime divisors.

I do not settle the unrestricted conjecture. The following self-contained bounds give special cases.

**Theorem.**

1. As \(n\to\infty\), uniformly over integers \(n\ge3\),
   \[
   \boxed{\displaystyle
   \alpha(n)\le (2+o(1))\frac{\log n}{\log\log n}+8S(n).}
   \tag{1}
   \]
   Consequently, along every sequence satisfying
   \[
   S(n)=o(\log n),
   \]
   the conjectured conclusion \(\alpha(n)=o(\log n)\) holds.

2. Along every sequence satisfying
   \[
   \log P(n)=o(\log\log n),
   \]
   one has the asymptotically optimal estimate
   \[
   \boxed{\displaystyle
   \alpha(n)\sim\frac{\log n}{\log\log n}.}
   \tag{2}
   \]

For example, (1) gives
\[
\alpha(n)\le(2+o(1))\frac{\log n}{\log\log n}
\]
whenever \(P(n)\le(\log n)^{1/3-\varepsilon}\), for fixed \(0<\varepsilon<1/3\). Part 2 applies, in particular, to powers of every fixed integer \(b\ge2\):
\[
\alpha(b^m)\sim\frac{m\log b}{\log m}
\qquad(m\to\infty).
\tag{3}
\]

The construction uses complete graphs to encode large portions of prime exponents, and cycles only for controlled remainders.

## 2. Multiplication and prime-power blocks

If connected simple graphs \(G_1,\ldots,G_r\) are joined by identifying one chosen vertex from each into a common vertex, the resulting graph is simple and satisfies
\[
\tau(G)=\prod_{i=1}^r\tau(G_i),
\qquad
|V(G)|=1+\sum_{i=1}^r\bigl(|V(G_i)|-1\bigr).
\tag{4}
\]
Indeed, a spanning tree of the resulting graph restricts to a spanning tree in each block, and the choices are independent.

Accordingly, call \(|V(H)|-1\) the **cost** of a block \(H\).

For a prime \(p\), put
\[
A_{p,t}=t(p^t-2).
\]
Cayley’s formula gives
\[
\tau(K_{p^t})=(p^t)^{p^t-2}=p^{A_{p,t}},
\tag{5}
\]
at cost \(p^t-1\). We use \(t\ge1\) for odd \(p\), and \(t\ge2\) for \(p=2\), so all these exponents are positive.

For odd \(p\), a cycle \(C_p\) supplies one additional factor \(p\), at cost \(p-1\). The prime \(2\) requires separate bookkeeping because no simple graph has exactly two spanning trees.

## 3. Normalizing the exponent of \(2\)

Let \(e_2=v_2(n)\). Choose an initial block \(H\) as follows.

- If \(e_2\) is even, take \(H=K_1\).
- If \(e_2\ge3\) is odd, take \(H=C_8\).
- If \(e_2=1\), choose an odd prime \(p_0\mid n\) and take \(H=C_{2p_0}\).

The last choice is always possible because \(n\ge3\) and \(v_2(n)=1\).

Set
\[
n_0=\frac{n}{\tau(H)}.
\]
Then \(v_2(n_0)\) is even, and the cost of \(H\) is at most \(2S(n)\): the only nonzero costs are \(7\) and \(2p_0-1\).

Write
\[
n_0=\prod_p p^{e_p}.
\]

## 4. Greedy decomposition of each prime exponent

For each \(p\), greedily divide \(e_p\) by the sequence \(A_{p,t}\), working downward from the largest admissible \(t\) with \(A_{p,t}\le e_p\). This gives
\[
e_p=\sum_t q_{p,t}A_{p,t}+r_p.
\tag{6}
\]
The final remainder satisfies
\[
0\le r_p<p-2\quad(p\text{ odd}),
\qquad
r_2\in\{0,2\}.
\tag{7}
\]
For \(p=2\), this uses the fact that both the initial exponent and all \(A_{2,t}\) are even, while \(A_{2,2}=4\).

Realize (6) using \(q_{p,t}\) copies of \(K_{p^t}\), together with:

- \(r_p\) copies of \(C_p\) for odd \(p\);
- one \(C_4\) if \(r_2=2\).

After attaching all these blocks to \(H\), equation (4) shows that the spanning-tree count is **exactly \(n\)**. All blocks and their one-vertex union are simple.

We next bound the cost.

### Bounds on the greedy coefficients

Immediately before processing \(A_{p,t}\), the remaining exponent is less than \(A_{p,t+1}\). Thus
\[
q_{p,t}<\frac{A_{p,t+1}}{A_{p,t}}.
\tag{8}
\]

For \(t\ge2\),
\[
\begin{aligned}
\frac{A_{p,t+1}}{A_{p,t}}
&=\frac{t+1}{t}
  \left(p+\frac{2(p-1)}{p^t-2}\right)\\
&\le \frac32(p+1)<2p+1.
\end{aligned}
\]
Since \(q_{p,t}\) is integral,
\[
q_{p,t}\le2p\qquad(t\ge2).
\tag{9}
\]

For odd \(p\),
\[
\frac{A_{p,2}}{A_{p,1}}
=\frac{2(p^2-2)}{p-2}
=2p+4+\frac4{p-2}<5p.
\]
Hence all the \(t=1\) clique blocks for this prime have total cost at most \(5p^2\).

The residual cycles have total cost at most \(p^2\) for each prime: for odd \(p\), their cost is \(r_p(p-1)<p^2\), and for \(p=2\) it is at most \(3<4\).

Combining these charges with the initial block, we have paid at most
\[
2S(n)+5S(n)+S(n)=8S(n).
\tag{10}
\]
Only clique blocks with \(t\ge2\) remain to be estimated.

## 5. A parameterized vertex bound

For real \(B\ge4\), define
\[
\rho(B)=\frac{B-2}{B-1}\log B.
\]
I claim that the construction above gives
\[
\boxed{\displaystyle
\alpha(n)\le
1+8S(n)+4B\min\{B,P(n)^2\}+\frac{L}{\rho(B)}.}
\tag{11}
\]

Partition the remaining clique blocks into those of order below \(B\) and those of order at least \(B\).

### Small clique blocks

For a fixed prime \(p\), equation (9) gives
\[
\begin{aligned}
\sum_{\substack{t\ge2\\p^t<B}}
q_{p,t}(p^t-1)
&\le 2p\sum_{\substack{t\ge2\\p^t<B}}p^t\\
&\le4pB.
\end{aligned}
\tag{12}
\]
Such terms occur only if \(p<\sqrt B\). Also,
\[
\sum_{\substack{p\mid n\\p<\sqrt B}}p
\le \min\{B,P(n)^2\},
\tag{13}
\]
by bounding each prime sum by the corresponding sum over all positive integers. Thus the small clique blocks cost at most
\[
4B\min\{B,P(n)^2\}.
\]

### Large clique blocks

A clique of order \(k=p^t\ge B\) supplies logarithmic spanning-tree count
\[
\log\tau(K_k)=(k-2)\log k
\]
at cost \(k-1\). Its logarithmic count per unit cost is
\[
\frac{k-2}{k-1}\log k\ge\rho(B),
\tag{14}
\]
because both factors on the left are increasing for \(k>2\).

The sum of the logarithmic spanning-tree counts of these blocks is at most \(L\). Their total cost is therefore at most \(L/\rho(B)\).

Adding the common vertex and the charges in (10) proves (11).

## 6. Consequences

### 6.1 The \(S(n)\)-criterion

In (11), choose
\[
B=\frac{\sqrt L}{(\log L)^2}.
\]
For sufficiently large \(n\), this is at least \(4\), and
\[
\rho(B)\sim\frac12\log L,
\qquad
4B\min\{B,P(n)^2\}\le4B^2
=\frac{4L}{(\log L)^4}.
\]
Consequently,
\[
\alpha(n)\le(2+o(1))\frac{L}{\log L}+8S(n),
\]
which proves (1).

If \(S(n)=o(L)\), both terms on the right are \(o(L)\), proving the conjecture along that sequence.

For the stated smooth-number example, the elementary estimate
\[
S(n)\le P(n)^3
\tag{15}
\]
shows that \(P(n)\le L^{1/3-\varepsilon}\) implies
\[
S(n)\le L^{1-3\varepsilon}
=o\!\left(\frac{L}{\log L}\right).
\]

### 6.2 Optimal asymptotics for very smooth integers

Suppose now that
\[
\log P(n)=o(\log L).
\]
In (11), choose
\[
B=\frac{L}{P(n)^2(\log L)^2}.
\]
Then \(B\to\infty\) and
\[
\log B
=\log L-2\log P(n)-2\log\log L
\sim\log L.
\]
Moreover,
\[
4B\min\{B,P(n)^2\}
\le \frac{4L}{(\log L)^2},
\]
and, by (15),
\[
S(n)\le P(n)^3=L^{o(1)}
=o\!\left(\frac{L}{\log L}\right).
\]
Thus
\[
\alpha(n)\le(1+o(1))\frac{L}{\log L}.
\tag{16}
\]

For the matching lower bound, every simple graph on \(k\) vertices has at most
\[
\tau(K_k)=k^{k-2}
\]
spanning trees. Therefore
\[
L\le(k-2)\log k,
\]
which implies
\[
\alpha(n)\ge(1-o(1))\frac{L}{\log L}.
\tag{17}
\]
Together, (16) and (17) prove (2).

## 7. What remains unresolved

The argument covers every integer satisfying the stated asymptotic restrictions, including the otherwise troublesome cases with \(v_2(n)=1\). Its construction and estimates require no unproved number-theoretic assumptions.

It does **not** address the principal difficulty of the unrestricted conjecture. For prime input \(n=p\),
\[
P(n)=n,\qquad S(n)=n^2,
\]
so these bounds supply no sublogarithmic estimate. Thus they do not establish \(\alpha(n)=o(\log n)\) for all integers, or even a uniform \(O(\log n)\) bound.

The rigorous outcome is an optimal first-order asymptotic for very smooth integers and a broader sufficient condition for the conjecture. I make no claim that these elementary partial results are new.
