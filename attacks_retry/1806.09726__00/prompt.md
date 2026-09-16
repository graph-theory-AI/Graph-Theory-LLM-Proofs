Attack the following open graph-theory problem.

Catalog id: 1806.09726__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1806.09726__00/
Source paper: Online Ramsey Numbers and the Subgraph Query Problem (arXiv:1806.09726)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 7
(a) The diagonal online random Ramsey numbers satisfy $$\tilde{r}_{rand}(n, n) = 2^{(1+o(1)) \frac{2}{3} n}.$$ (b) The off-diagonal online random Ramsey numbers ($m \geq 3$ fixed and $n \to \infty$) satisfy $$\tilde{r}_{rand}(m, n) = n^{(1+o(1)) \frac{2}{3} m}.$$

Context:
The authors define the online random Ramsey number $\tilde{r}_{rand}(m,n)$ as the maximum over $p \in (0,1)$ of $\tilde{r}(m,n;p)$, where Painter independently colors each edge red with probability $p$. These conjectures on the growth rate are motivated by a connection with the Subgraph Query Problem; Theorem 10 and Conjecture 9 together imply both parts of this conjecture.

=== Catalog page (statement + literature review) ===
Diagonal and off-diagonal online random Ramsey growth rates — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 Conjecture 7 from arXiv:1806.09726 posits that the diagonal online random Ramsey numbers grow as $2^{(1+o(1))\frac{2}{3}n}$ and the off-diagonal as $n^{(1+o(1))\frac{2}{3}m}$. The conjecture is tied to the Subgraph Query Problem via Theorem 10 and Conjecture 9 of the same paper. A 2019 follow-up (arXiv:1911.04413) makes progress on the Subgraph Query Problem itself, but a web search through 2026 found no paper that directly resolves either part of Conjecture 7. The conjecture remains open as far as indexed literature reveals.

 Cited literature (1)

 
 
 
partial On the subgraph query problem
 (2019)
 

 
 Ryan Alweiss, Chady Ben Hamida, Xiaoyu He, Alexander Moreira · arXiv preprint · arXiv:1911.04413

Improves bounds on the Subgraph Query Problem for cliques and degenerate graphs, directly related to the mechanism through which Conjecture 7 is expected to follow, but does not resolve the conjecture's stated growth-rate claims.
 

 

 Reviewer notes. Semantic Scholar citation list for arXiv:1806.09726 shows no citing paper that directly resolves Conjecture 7. The related paper arXiv:1911.04413 (with Xiaoyu He as co-author of both) works on the subgraph query problem but does not establish the conjectured exponents for r_rand. The conjecture is 8 years old; medium confidence rather than high is assigned because the conjecture's age and its tight connection to an active research topic leave room for a resolution in the literature that was not surfaced by the search.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. (a) The diagonal online random Ramsey numbers satisfy $$\tilde{r}_{rand}(n, n) = 2^{(1+o(1)) \frac{2}{3} n}.$$ (b) The off-diagonal online random Ramsey numbers ($m \geq 3$ fixed and $n \to \infty$) satisfy $$\tilde{r}_{rand}(m, n) = n^{(1+o(1)) \frac{2}{3} m}.$$

Context

The authors define the online random Ramsey number $\tilde{r}_{rand}(m,n)$ as the maximum over $p \in (0,1)$ of $\tilde{r}(m,n;p)$, where Painter independently colors each edge red with probability $p$. These conjectures on the growth rate are motivated by a connection with the Subgraph Query Problem; Theorem 10 and Conjecture 9 together imply both parts of this conjecture.

Source paper

 Online Ramsey Numbers and the Subgraph Query Problem
 David Conlon, Jacob Fox, Andrey Grinshpun, Xiaoyu He · 2018-11-04
 https://arxiv.org/abs/1806.09726
 PDF source

=== Source paper abstract / header ===
Abstract:The $(m,n)$-online Ramsey game is a combinatorial game between two players, Builder and Painter. Starting from an infinite set of isolated vertices, Builder draws an edge on each turn and Painter immediately paints it red or blue. Builder's goal is to force Painter to create either a red $K_m$ or a blue $K_n$ using as few turns as possible. The online Ramsey number $\tilde{r}(m,n)$ is the minimum number of edges Builder needs to guarantee a win in the $(m,n)$-online Ramsey game. By analyzing the special case where Painter plays randomly, we obtain an exponential improvement \[ \tilde{r}(n,n) \ge 2^{(2-\sqrt{2})n + O(1)} \] for the lower bound on the diagonal online Ramsey number, as well as a corresponding improvement \[ \tilde{r}(m,n) \ge n^{(2-\sqrt{2})m + O(1)} \] for the off-diagonal case, where $m\ge 3$ is fixed and $n\rightarrow\infty$. Using a different randomized Painter strategy, we prove that $\tilde{r}(3,n)=\tilde{\Theta}(n^3)$, determining this function up to a polylogarithmic factor. We also improve the upper bound in the off-diagonal case for $m \geq 4$.
In connection with the online Ramsey game with a random Painter, we study the problem of finding a copy of a target graph $H$ in a sufficiently large unknown Erdős--Rényi random graph $G(N,p)$ using as few queries as possible, where each query reveals whether or not a particular pair of vertices are adjacent. We call this problem the Subgraph Query Problem. We determine the order of the number of queries needed for complete graphs up to five vertices and prove general bounds for this problem.
 

 
 
 
 Comments:
 Corrected substantial error in the proof of Theorem 4
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:1806.09726 [math.CO]
 

 
  
 (or 
 arXiv:1806.09726v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1806.09726
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Xiaoyu He [view email] 
 [v1]
 Mon, 25 Jun 2018 23:26:16 UTC (25 KB)

 [v2]
 Sun, 4 Nov 2018 16:35:54 UTC (28 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Online Ramsey Numbers and the Subgraph Query Problem, by David Conlon and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 math.CO

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2018-06
 

 Change to browse by:
 
 math
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 export BibTeX citation
 Loading...

 
 
 BibTeX formatted citation

 ×
 

 
 loading...
 

 
 Data provided by: 
 
 

 

 Bookmark

 
 
 
 
 

 

 

 
 Bibliographic Tools
 
 Bibliographic and Citation Tools

 
 
 
 
 
 
 Bibliographic Explorer Toggle
 
 

 
 Bibliographic Explorer (What is the Explorer?)
 

 

 
 
 
 
 
 Connected Papers Toggle
 
 

 
 Connected Papers (What is Connected Papers?)
 

 

 
 
 
 
 Litmaps Toggle
 
 

 
 Litmaps (What is Litmaps?)
 

 

 
 
 
 
 
 scite.ai Toggle
 
 

 
 scite Smart Citations (What are Smart Citations?)
 

 

 

 

 

 

 

 

 
 Code, Data, Media
 
 Code, Data and Media Associated with this Article

 
 
 
 
 
 
 alphaXiv Toggle
 
 

 
 alphaXiv (What is alphaXiv?)
 

 

 
 
 
 
 
 Links to Code Toggle
 
 

 
 CatalyzeX Code Finder for Papers (What is CatalyzeX?)
 

 

 
 
 
 
 
 DagsHub Toggle
 
 

 
 DagsHub (What is DagsHub?)
 

 

 
 
 
 
 
 
 GotitPub Toggle
 
 

 
 Gotit.pub (What is GotitPub?)
 

 

 
 
 
 
 
 Huggingface Toggle
 
 

 
 Hugging Face (What is Huggingface?)
 

 

 
 
 
 
 
 ScienceCast Toggle
 
 

 
 ScienceCast (What is ScienceCast?)
 

 

 

 

 

 

 

 

 

 

 
 Demos
 
 Demos

 
 
 
 
 
 
 Replicate Toggle
 
 

 
 Replicate (What is Replicate?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 Hugging Face Spaces (What is Spaces?)
 

 

 
 
 
 
 
 Spaces Toggle
 
 

 
 TXYZ.AI (What is TXYZ.AI?)
 

 

 

 

 

 

 

 
 Related Papers
 
 Recommenders and Search Tools

 
 
 
 
 
 
 Link to Influence Flower
 
 

 
 Influence Flower (What are Influence Flowers?)
 

 

 
 
 
 
 
 Core recommender toggle
 
 

 
 CORE Recommender (What is CORE?)
 

 

 

 
 
 Author

 Venue

 Institution

 Topic

 
 
 

 

 

 

 

 

 

 

 

 
 
 About arXivLabs
 
 
 
 
 arXivLabs: experimental projects with community collaborators

 arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.

 Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.

 Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.

 

 
 

 

 

 

 

 
 Which authors of this paper are endorsers? |
 Disable MathJax (What is MathJax?)

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-5.6-sol`, which reported verdict `disproved` at high confidence. That attempt is reproduced below.
An adversarial referee then reviewed it and returned `FATAL_ERROR`, i.e. the claimed resolution did not stand, so the problem is still open.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "Part (b) is false as written: for fixed m=4 the online random Ramsey number is Theta(n^2), not n^(8/3+o(1)).",
  "would_publish": false,
  "caveats": "Part (a) is untouched; if the intended statement takes m to infinity and permits an additive O(1) in the exponent, this fixed-m counterexample does not apply."
}
```

## 1. Statement and convention

Take part (b) literally: \(m\ge 3\) is fixed, \(n\to\infty\), and the \(o(1)\) is with respect to \(n\).

For a Builder strategy \(\mathcal B\), let \(\tau_{m,n}(\mathcal B,p)\) be the first time that the queried graph contains either a red \(K_m\) or a blue \(K_n\), when every queried edge is independently red with probability \(p\). Under the expected-time convention, write
\[
R_p(m,n)=\inf_{\mathcal B}\mathbb E\tau_{m,n}(\mathcal B,p).
\]
The argument also applies, up to constant factors, if \(\widetilde r(m,n;p)\) is defined using probability at least \(1/2\) rather than expected stopping time: Markov's inequality converts the upper bounds, and the lower bound below directly controls the success probability.

I prove
\[
\widetilde r_{\mathrm{rand}}(4,n)=\Theta(n^2).
\]
This contradicts the asserted \(n^{8/3+o(1)}\).

---

## 2. Finding a red \(K_4\) in \(O(p^{-2})\) queries

### Lemma 1
There is an absolute constant \(C\) such that, for every \(p\in(0,1)\), Builder can find a red \(K_4\) in expected at most
\[
C p^{-2}
\]
queries.

### Proof

First suppose \(p\le 1/2\), and put
\[
L=\left\lceil \frac1p\right\rceil.
\]

One round of the strategy is as follows.

1. Choose a fresh vertex \(v\).
2. Query edges from \(v\) to fresh vertices until \(3L\) red neighbors have been obtained.
3. Partition these red neighbors into three sets \(A,B,C\), each of size \(L\).
4. Query all edges between each pair of parts \(A,B,C\).

If there are \(a\in A,b\in B,c\in C\) such that \(ab,bc,ca\) are all red, then
\[
\{v,a,b,c\}
\]
spans a red \(K_4\), since \(va,vb,vc\) were red by construction.

The expected number of queries in step 2 is
\[
\frac{3L}{p}=O(p^{-2}),
\]
and step 4 uses \(3L^2=O(p^{-2})\) queries.

It remains to show that a round succeeds with probability bounded below by an absolute positive constant. Let \(X\) count red tripartite triangles in \(A\cup B\cup C\). Then
\[
\mathbb E X=L^3p^3=(Lp)^3\ge 1.
\]
Two distinct tripartite triangles have dependent indicators only if they share an edge. There are at most \(3L^4\) ordered pairs sharing an edge, and each such pair has joint probability \(p^5\). Hence
\[
\operatorname{Var}X\le \mathbb E X+3L^4p^5.
\]
Since \(p\le1/2\) gives \(Lp\le 3/2\), the right-hand side is bounded by an absolute constant. The second-moment inequality therefore gives
\[
\Pr(X>0)\ge
\frac{(\mathbb E X)^2}{\mathbb E X^2}
\ge c_0
\]
for some absolute \(c_0>0\).

Repeating the round on disjoint fresh vertex sets consequently finds a red \(K_4\) after \(O(1)\) expected rounds, and hence after \(O(p^{-2})\) expected queries.

For \(p>1/2\), simply query all six edges on successive disjoint sets of four vertices. Each set is a red \(K_4\) with probability \(p^6\), so the expected number of queries is
\[
6p^{-6}\le 96p^{-2}.
\]
This proves the lemma. \(\square\)

---

## 3. Finding a blue \(K_n\) in \(O(n^2)\) queries when \(p\le 1/n\)

### Lemma 2
If \(p\le 1/n\), Builder can find a blue \(K_n\) in expected \(O(n^2)\) queries.

### Proof

Build a blue clique greedily. Suppose a blue clique \(S\) of size \(i\) has already been constructed. For each fresh candidate vertex \(w\), query the edges from \(w\) to all vertices of \(S\), stopping and rejecting \(w\) as soon as a red edge appears. Accept \(w\) if all \(i\) queried edges are blue.

A candidate succeeds with probability
\[
(1-p)^i\ge (1-1/n)^{n-1}\ge e^{-1}.
\]
Thus the expected number of candidates tested at stage \(i\) is at most \(e\), while each candidate costs at most \(i\) queries. The expected total cost is therefore at most
\[
e\sum_{i=0}^{n-1}i
= e\binom n2
=O(n^2).
\]
\(\square\)

---

## 4. Uniform upper bound for \(m=4\)

For every \(p\in(0,1)\), Builder chooses between the preceding strategies:

- If \(p\le 1/n\), Lemma 2 finds a blue \(K_n\) in expected \(O(n^2)\) queries.
- If \(p>1/n\), Lemma 1 finds a red \(K_4\) in expected
  \[
  O(p^{-2})=O(n^2)
  \]
  queries.

Consequently,
\[
\sup_{p\in(0,1)}R_p(4,n)=O(n^2).
\]

Under a constant-success-probability definition, Markov's inequality shows that Builder wins with probability at least \(1/2\) after \(O(n^2)\) queries. Any fixed higher success probability can likewise be obtained by a constant number of independent repetitions.

---

## 5. Matching lower bound

Choose
\[
p=n^{-3}
\]
and let
\[
q=\left\lfloor\frac{n(n-1)}4\right\rfloor.
\]
Since
\[
q<\binom n2,
\]
no queried graph with at most \(q\) edges can contain a blue \(K_n\), independently of how Builder chooses the edges.

For any adaptive Builder strategy, each newly queried edge is red with conditional probability \(p\). Thus, by a union bound,
\[
\Pr(\text{some queried edge among the first \(q\) is red})
\le qp=O(n^{-1}).
\]
A red \(K_4\) in particular requires at least one red edge, so
\[
\Pr\bigl(\tau_{4,n}\le q\bigr)=O(n^{-1}).
\]
Therefore every Builder strategy satisfies
\[
\mathbb E\tau_{4,n}
\ge q\,\Pr(\tau_{4,n}>q)
=(1-o(1))q
=\Omega(n^2).
\]
For the probability-\(1/2\) convention, the same calculation says that no strategy wins by time \(q\) with probability \(1/2\), for all sufficiently large \(n\).

Combining upper and lower bounds,
\[
\boxed{\widetilde r_{\mathrm{rand}}(4,n)=\Theta(n^2).}
\]

---

## 6. Contradiction to Conjecture 7(b)

The quoted conjecture predicts, for \(m=4\),
\[
\widetilde r_{\mathrm{rand}}(4,n)
=n^{(1+o(1))\frac83}
=n^{8/3+o(1)}.
\]
The proved estimate has logarithmic exponent \(2\), not \(8/3\). Hence part (b) is false under its stated fixed-\(m\), \(n\to\infty\) interpretation.

There is a second similar obstruction at \(m=5\). More generally, one can gather
\[
\Theta\!\left(p^{-(m-2)/2}\right)
\]
red neighbors of a vertex and expose all edges among them. The induced random graph contains a \(K_{m-1}\) with constant probability, by the usual fixed-clique second-moment calculation. This finds a red \(K_m\) using
\[
O_m\!\left(p^{-m/2}+p^{-(m-2)}\right)
\]
queries. For \(m=5\), this is \(O(p^{-3})\); combined with Lemma 2 it gives
\[
\widetilde r_{\mathrm{rand}}(5,n)=O(n^3),
\]
also smaller than the conjectured \(n^{10/3+o(1)}\).

## 7. Scope and possible transcription issue

Part (a), and any intended large-\(m\) version of part (b), remain unresolved here. The elementary \(m=4\) contradiction strongly suggests checking the original quantifiers. A formulation such as
\[
\widetilde r_{\mathrm{rand}}(m,n)
=n^{\frac23m+O(1)}
\]
with the emphasis on the coefficient as \(m\to\infty\) would allow exceptional fixed values such as \(m=4\) and is not refuted by this argument.

--- referee report on that attempt ---
---
id: 1806.09726__00
claimed_verdict: disproved
review_verdict: FATAL_ERROR
confidence: high
interpretation_ok: false
references_ok: true
computation_run: true
one_line: The writeup's mathematics (r̃_rand(4,n) = Θ(n²)) is correct but refutes only a mis-read literal statement; the source paper's own Theorem 13 and Conjecture 9 already give exponent 2 at m=4, so the intended Conjecture 7 (o(1) as m→∞) is untouched and remains open.
---

## Interpretation

The writeup reads Conjecture 7(b), "r̃_rand(m,n) = n^{(1+o(1))(2/3)m} (m ≥ 3 fixed and
n → ∞)", with the o(1) taken as n → ∞ at fixed m, so that m = 4 asserts
r̃_rand(4,n) = n^{8/3+o(1)}. It then proves r̃_rand(4,n) = Θ(n²) and declares the
conjecture disproved.

This literal reading is **not** the intended one, and the source paper itself proves it.
I fetched arXiv:1806.09726 (ar5iv full text) and confirmed:

- **Theorem 13** of the paper: f(K₄,p) = Θ(p⁻²) and f(K₅,p) = Θ(p^{-8/3}), where
  f(H,p) is the subgraph query complexity.
- **Theorem 10**: r̃(m,n;p) ≤ min{f(K_m,p), f(K_n,1−p)} ≤ 3·r̃(m,n;p).
- **Conjecture 9**: for m ≥ 4, f(K_m,p) = 2^{o(m)}·p^{−2m/3+c_m} with explicit
  corrections c_m (c₄ = 2/3 since 4 ≡ 1 mod 3; c₅ = (2·5+8)/(6·5−3) = 2/3).

Conjecture 9 at m = 4 predicts f(K₄,p) = p^{−8/3+2/3} = p^{−2}, exactly matching the
paper's proven Theorem 13; likewise m = 5 gives p^{−8/3}, matching. Combining
Theorem 13 with Theorem 10 (and the trivial/greedy bounds on f(K_n,1−p)), the paper's
own results already yield r̃_rand(4,n) = n^{2+o(1)} — precisely the writeup's
"counterexample" value. Under the writeup's literal reading, Conjecture 7(b) would be
refuted by Theorem 13 of the *same paper*: the authors would be contradicting
themselves three theorems apart. A reading that renders the source self-contradictory
cannot be the intended one. The paper states explicitly that "Theorem 10 and
Conjecture 9 together imply both parts of this conjecture," and Conjecture 9 carries
the per-m correction c_m ≈ 2/3, which the factor (1+o(1)) in Conjecture 7 can absorb
only as m → ∞. The intended statement is: for each fixed m, r̃_rand(m,n) is
polynomial in n with exponent e_m, and e_m = (2/3)m·(1+o(1)) as m → ∞ (equivalently
(2/3)m + O(1)); the parenthetical "m ≥ 3 fixed and n → ∞" only fixes the regime in
which the n-exponent is measured.

No reasonable author of the original paper would consider Conjecture 7 resolved by
this writeup. The writeup's own caveats field concedes the point ("if the intended
statement takes m to infinity and permits an additive O(1) in the exponent, this
fixed-m counterexample does not apply") — and that is exactly the intended statement.
This is interpretation gaming: a correct computation deployed against a transcription
artifact.

## Step-by-step findings

| step | label | note |
|---|---|---|
| §1 Conventions | VALID | Uses expected-stopping-time R_p; the paper's Definition 6 uses "win with probability ≥ 1/2". The conversions claimed are correct: Markov gives prob-1/2 upper bounds from expected-time upper bounds, and the §5 lower bound directly bounds the success probability (win prob by turn q is O(1/n) < 1/2). |
| Lemma 1 (red K₄ in O(p⁻²) expected queries) | VALID | For p ≤ 1/2, L = ⌈1/p⌉: Lp ∈ [1, 3/2], so EX = L³p³ ∈ [1, 3.375]. Step-2 cost 3L/p ≤ 6p⁻² (negative binomial), step-4 cost 3L² ≤ 12p⁻². Verified by simulation: E[queries]·p² ≈ 10, constant over p ∈ [0.02, 0.5]. |
| Lemma 1 second moment | VALID | Two tripartite triangles are dependent iff they share an edge (sharing one vertex leaves disjoint edge sets, covariance 0). Ordered pairs sharing an edge: 3 part-pairs × L² edges × L(L−1) third-vertex pairs ≤ 3L⁴, joint prob p⁵. Var X ≤ EX + 3L⁴p⁵ = EX + 3(Lp)⁴p ≤ 3.375 + 15.2p, bounded. Paley–Zygmund gives Pr(X>0) ≥ (EX)²/((EX)²+EX+3L⁴p⁵) ≥ 0.28 for all p ≤ 1/2 (exact computation in script); simulation observes 0.56–0.74. |
| Lemma 1 round iteration | VALID | Rounds use disjoint fresh vertices, hence i.i.d.; number of rounds geometric with success prob ≥ c₀; Wald's identity gives O(p⁻²) total expectation. |
| Lemma 1, p > 1/2 case | VALID | 6p⁻⁶ ≤ 6·16·p⁻² = 96p⁻² since p⁻⁴ ≤ 16. Arithmetic checks. |
| Lemma 2 (blue K_n in O(n²) for p ≤ 1/n) | VALID | (1−p)^i ≥ (1−1/n)^{n−1} ≥ e⁻¹ for i ≤ n−1 (standard). Expected candidates per stage ≤ e, cost per candidate ≤ i, total ≤ e·C(n,2). Simulation: E[queries]/C(n,2) ≈ 1.44–1.52 for n up to 160. |
| §4 uniform upper bound | VALID | p ≤ 1/n → Lemma 2 gives O(n²); p > 1/n → Lemma 1 gives O(p⁻²) = O(n²). Markov converts to the prob-1/2 convention. |
| §5 lower bound Ω(n²) | VALID | q = ⌊n(n−1)/4⌋ < C(n,2), so no blue K_n within q turns; against the i.i.d. Painter each newly queried edge is red with conditional probability p regardless of adaptivity, so Pr(any red edge in first q turns) ≤ qp = O(1/n) at p = n⁻³; a red K₄ needs a red edge. Hence win prob by turn q is O(1/n) < 1/2 and E[τ] ≥ (1−o(1))q. Arithmetic verified (qp ≤ 0.022 already at n = 10). |
| §6 contradiction to Conjecture 7(b) | ERROR | The Θ(n²) result contradicts only the strawman fixed-m reading. Under the paper's intended reading (o(1) as m → ∞, consistent with Conjecture 9's c_m and Theorem 13), there is no contradiction: the paper itself predicts and essentially proves exponent 2 at m = 4 (Theorems 10 + 13 give r̃_rand(4,n) = n^{2+o(1)}). The writeup's "new" value is already implicit in the source paper. |
| §6 m = 5 remark | GAP (and moot) | The O_m(p^{−m/2} + p^{−(m−2)}) sketch ("usual second-moment calculation" for K_{m−1} at its threshold) is plausible and routine for fixed m, but not written out. In any case the paper's Theorem 13 already gives the stronger r̃_rand(5,n) = n^{8/3+o(1)} < n³, so the remark adds nothing and again contradicts nothing intended. |
| §7 scope caveat | VALID | The writeup correctly flags the possible transcription issue — which is in fact the actual situation, undermining its own verdict. |

## Reference check

- **arXiv:1806.09726** (Conlon, Fox, Grinshpun, He, *Online Ramsey Numbers and the
  Subgraph Query Problem*): fetched full text via ar5iv. Definition 6 (r̃(m,n;p) =
  turns needed to win with probability ≥ 1/2 against the p-random Painter;
  r̃_rand = max over p), Conjecture 7, Conjecture 9 (with corrections c_m),
  Theorem 10 (r̃(m,n;p) ≤ min{f(K_m,p), f(K_n,1−p)} ≤ 3r̃(m,n;p)), and Theorem 13
  (f(K₄,p) = Θ(p⁻²), f(K₅,p) = Θ(p^{−8/3})) all confirmed verbatim. Internal
  consistency check: Conjecture 9's formula evaluated at m = 4 and m = 5 reproduces
  Theorem 13's exponents exactly (−8/3 + 2/3 = −2; −10/3 + 2/3 = −8/3), confirming
  both the fetched text and the m → ∞ reading of Conjecture 7.
- The writeup itself cites no external results; its proofs are self-contained and
  were checked directly.
- Literature status: a web search (September 2026) found no paper resolving
  Conjecture 7; the catalog's "open" status stands. The 2019 follow-up
  arXiv:1911.04413 works on the Subgraph Query Problem but does not settle the
  conjectured growth rates.

## Computational check

Script: `verification/scripts/1806.09726__00/verify_lemmas.py`
(Python 3, Monte Carlo + exact arithmetic; seed 12345). Results:

- **Lemma 1 second moment (exact):** for p ∈ {0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01,
  0.001}: EX = L³p³ ∈ [1, 1.73], Lp ≤ 1.2, and the Paley–Zygmund bound
  (EX)²/((EX)²+EX+3L⁴p⁵) ≥ 0.286 in every case.
- **Lemma 1 simulation:** per-round success probability 0.56–0.74 across p ∈
  [0.02, 0.5] (thousands of trials); full-strategy expected queries to a red K₄
  satisfy E[queries]·p² ≈ 9.6–10.7, i.e. a stable constant — confirming Θ(p⁻²).
- **Lemma 2 simulation:** at p = 1/n, E[queries to blue K_n]/C(n,2) = 1.52, 1.48,
  1.46, 1.44, 1.44 for n = 10, 20, 40, 80, 160 — below the claimed bound e ≈ 2.718
  and confirming O(n²).
- **Lower bound arithmetic:** q = ⌊n(n−1)/4⌋ < C(n,2) always; qp at p = n⁻³ equals
  0.022, 0.008, 0.0025, 0.00025 for n = 10, 30, 100, 1000 — confirming the O(1/n)
  union bound.
- **Exponent bookkeeping:** (2/3)·4 = 8/3; the paper's c₄ = 2/3 gives intended
  m = 4 exponent 2m/3 − c₄ = 2, equal to the writeup's Θ(n²) — the "counterexample"
  matches the paper's own prediction.

No computational check failed; the failure is not in the mathematics.

## Caveats

- The writeup addresses only part (b) at m = 4 (plus a sketched m = 5); part (a) and
  the genuine content of part (b) (the m → ∞ exponent (2/3)m + O(1)) are untouched,
  as the writeup itself admits.
- Convention dependence is handled: the paper's Definition 6 (probability ≥ 1/2) and
  the writeup's expected-time convention agree up to constant factors, which do not
  affect polynomial growth rates.
- The Θ(n²) upper bound needs an unbounded supply of fresh vertices; the game is
  defined on an infinite vertex set, so this is fine.
- The catalog transcription faithfully copies the paper's wording; the ambiguity in
  "(1+o(1))" is in the original text, but the surrounding paper (Conjecture 9's c_m,
  Theorem 13) disambiguates it decisively. The catalog's context line even reproduces
  the disambiguating sentence ("Theorem 10 and Conjecture 9 together imply both parts
  of this conjecture"), which the writeup did not act on.
- The writeup's own caveats field pre-emptively concedes the fatal objection.

## Referee summary

Every lemma and computation in the writeup is correct — I verified the second-moment
argument analytically and by simulation, the greedy clique bound, and the lower-bound
arithmetic, and the result r̃_rand(4,n) = Θ(n²) is true. But it is not a disproof of
Conjecture 7. The source paper proves f(K₄,p) = Θ(p⁻²) (Theorem 13) and shows
r̃(m,n;p) is determined by subgraph query complexities (Theorem 10), so
r̃_rand(4,n) = n^{2+o(1)} is already implicit in the very paper stating the
conjecture; the paper's Conjecture 9, which the authors say implies Conjecture 7,
explicitly predicts exponent 2m/3 − c_m = 2 at m = 4. The "(1+o(1))" in Conjecture 7
is therefore an m → ∞ asymptotic, and the writeup refutes only a transcription
artifact. The claimed verdict "disproved" is wrong; the conjecture remains open.

