Attack the following open graph-theory problem.

Catalog id: 2211.01032__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2211.01032__01/
Source paper: Random Embeddings of Graphs: The Expected Number of Faces in Most Graph… (arXiv:2211.01032)

=== Catalog page (statement + literature review) ===
Expected faces logarithmic for all G(n,p) — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 9.1 from arXiv:2211.01032 asserts that for any density function p(n), almost all graphs in G(n,p) have E[F] = O(log n). The paper itself proves this for dense graphs (p >= 1/polylog n, Corollary 7.3, polylogarithmic bound) and for sparse random graphs (Section 8, logarithmic bound), leaving the general case open. The conjecture would follow from the stronger Conjecture 1.13. No subsequent work resolving the full conjecture was found in the literature.

 Reviewer notes. No follow-up paper resolving Conjecture 9.1 was found. The paper's latest revision (v3, April 2025) still lists the conjecture as open. Conjecture 9.1 is a consequence of the stronger Conjecture 1.13 (also open), which predicts E[F] = (1+o(1)) ln(pn^2) for G(n,p).

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For any $p(n) : \mathbb{N} \rightarrow [0,1]$, almost all graphs in $G(n,p)$ satisfy $\mathbb{E}[F] = O(\log(n))$.

Context

Corollary 7.3 establishes a polylogarithmic bound for almost all dense graphs (when $p \geq 1/\mathrm{polylog}\, n$), and Section 8 gives a logarithmic bound for random sparse graphs. The authors conjecture that the logarithmic property holds without any density condition on edges. This conjecture would follow from the stronger Conjecture 1.13.

Source paper

 Random Embeddings of Graphs: The Expected Number of Faces in Most Graphs is Logarithmic
 Jesse Campion Loth, Kevin Halasz, Tomáš Masařík, Bojan Mohar, Robert Šámal · 2025-04-09
 https://arxiv.org/abs/2211.01032

=== Source paper abstract / header ===
Abstract:A random 2-cell embedding of a connected graph $G$ in some orientable surface is obtained by choosing a random local rotation around each vertex. Under this setup, the number of faces or the genus of the corresponding 2-cell embedding becomes a random variable. Random embeddings of two particular graph classes, those of a bouquet of $n$ loops and those of $n$ parallel edges connecting two vertices, have been extensively studied and are well-understood. However, little is known about more general graphs. The results of this paper explain why Monte Carlo methods cannot work for approximating the minimum genus of graphs.
In his breakthrough work [Permutation-partition pairs, JCTB 1991], Stahl developed the foundation of "random topological graph theory". Most of his results have been unsurpassed until today. In our work, we analyze the expected number of faces of random embeddings (equivalently, the average genus) of a graph $G$. It was very recently shown that for any graph $G$, the expected number of faces is at most linear. We show that the actual expected number of faces $F(G)$ is almost always much smaller. In particular, we prove:
1) $\frac{1}{2}\ln n - 2 < \mathbb{E}[F(K_n)] \le 3.65 \ln n +o(1)$.
2) For random graphs $G(n,p)$ ($p=p(n)$), we have $\mathbb{E}[F(G(n,p))] \le \ln^2 n+\frac{1}{p}$.
3) For random models $B(n,\Delta)$ containing only graphs, whose maximum degree is at most $\Delta$, we obtain stronger bounds by showing that the expected number of faces is $\Theta(\log n)$.
 

 
 
 
 Comments:
 Accepted at the 35th ACM-SIAM Symposium on Discrete Algorithms (SODA 2024). The submission also contains sources and data of the computation described in the paper. 55 pages, 11 figures
 

 Subjects:
 
 Combinatorics (math.CO); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 05C10
 

 
 ACM classes:
 G.2.2
 

 Cite as:
 arXiv:2211.01032 [math.CO]
 

 
  
 (or 
 arXiv:2211.01032v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2211.01032
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Proceedings: ACM-SIAM Symposium on Discrete Algorithms, SODA 2024
 

 
 
 Related DOI:
 
 https://doi.org/10.1137/1.9781611977912.46

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tomáš Masařík [view email] 
 [v1]
 Wed, 2 Nov 2022 10:58:31 UTC (500 KB)

 [v2]
 Thu, 28 Dec 2023 22:21:48 UTC (708 KB)

 [v3]
 Wed, 9 Apr 2025 18:37:40 UTC (1,123 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Random Embeddings of Graphs: The Expected Number of Faces in Most Graphs is Logarithmic, by Jesse Campion Loth and 4 other authors
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
 | 2022-11
 

 Change to browse by:
 
 cs
 cs.DM
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
  "one_line": "For p(n)=1/n, a graph in G(n,p) has linearly many isolated K_2 components a.a.s., each of which forces one face in every componentwise random embedding.",
  "would_publish": false,
  "caveats": "This refutes the catalog statement under the canonical componentwise definition; a version conditioned on connectedness or concerning one distinguished component is different."
}
```

## Statement and convention

For a graph \(G\), write
\[
f(G):=\mathbb E_{\rho}[F(G,\rho)],
\]
where \(\rho\) is the collection of independent uniform local rotations.

The source abstract initially defines this for connected graphs. There is a canonical extension to disconnected graphs: the face permutation acts separately on the darts of each connected component, equivalently each component is embedded in its own orientable surface. Under this extension, the number of faces is additive over components.

Under that standard interpretation, the catalog conjecture is false.

## Isolated edges force faces

Let \(uv\) be an isolated \(K_2\)-component of \(G\). Both \(u\) and \(v\) have degree one, so their local rotations are uniquely determined. On the two darts of \(uv\), the edge-reversal involution swaps the darts, while both vertex rotations are identities. Consequently, the face permutation has one \(2\)-cycle on these darts.

Thus every isolated \(K_2\)-component contributes exactly one face, independently of all rotation choices. If \(X(G)\) denotes the number of isolated \(K_2\)-components, then deterministically
\[
F(G,\rho)\ge X(G)
\quad\text{and hence}\quad
f(G)\ge X(G).
\]

## Isolated edges in \(G(n,1/n)\)

Set \(p=1/n\), and let
\[
X=\sum_{e\in\binom{[n]}2} I_e,
\]
where \(I_e\) indicates that \(e\) is an isolated \(K_2\)-component.

For a fixed edge \(e\),
\[
q:=\mathbb P(I_e=1)
=p(1-p)^{2(n-2)}.
\]
Therefore
\[
\mu:=\mathbb E X
=\binom n2\frac1n\left(1-\frac1n\right)^{2n-4}
=\left(\frac{e^{-2}}2+o(1)\right)n.
\]

We also have \(\operatorname{Var}X=O(n)\). Indeed:

- If two candidate edges share a vertex, they cannot both be isolated components, so their covariance is negative.
- If \(e,f\) are disjoint, then
  \[
  \mathbb P(I_e=I_f=1)
  =p^2(1-p)^{4n-12},
  \]
  whereas
  \[
  q^2=p^2(1-p)^{4n-8}.
  \]
  Hence
  \[
  \operatorname{Cov}(I_e,I_f)
  =q^2\bigl((1-p)^{-4}-1\bigr)
  =O(n^{-3})
  \]
  when \(p=1/n\). There are \(O(n^4)\) disjoint pairs, so their total covariance is \(O(n)\); the sum of individual variances is also \(O(n)\).

It follows from Chebyshev's inequality that
\[
\frac{X}{n}\xrightarrow{\mathrm p}\frac{e^{-2}}2.
\]
In particular, \(X=\Theta(n)\) asymptotically almost surely.

Consequently,
\[
f(G)\ge X(G)=\Theta(n)
\qquad\text{a.a.s. for }G\sim G(n,1/n).
\]
For every fixed \(C\),
\[
\mathbb P\bigl(f(G)\le C\log n\bigr)
\le
\mathbb P\bigl(X\le C\log n\bigr)
\longrightarrow 0.
\]
This is the opposite of the asserted conclusion.

The same obstruction persists even when \(np\to\infty\). For example, with
\[
p=\frac{\log n}{4n},
\]
the expected number of isolated edges is
\[
\binom n2p(1-p)^{2n-4}
=(1+o(1))\frac18 n^{1/2}\log n,
\]
and the same second-moment argument gives concentration.

## Connectedness caveat

If the paper defines \(F(G)\) only when \(G\) is connected, then the catalog formulation is not well-posed for arbitrary \(p(n)\): for \(p=1/n\), \(G(n,p)\) is disconnected asymptotically almost surely, so \(F(G)\) is undefined on almost every sample.

Possible corrected formulations include:

1. restrict to \(p\) for which \(G(n,p)\) is connected a.a.s.;
2. condition \(G(n,p)\) on being connected;
3. consider only the giant component or the \(2\)-core;
4. alter the face statistic by removing contributions from separate tree components.

These formulations are inequivalent. The isolated-\(K_2\) argument does not resolve a version conditioned on connectedness or restricted to a distinguished component; such a corrected conjecture may remain open.

--- referee report on that attempt ---
---
id: 2211.01032__01
claimed_verdict: disproved
review_verdict: FATAL_ERROR
confidence: high
interpretation_ok: false
references_ok: false
computation_run: true
one_line: The refutation works only under an additive-over-components face count, but the source paper explicitly defines the number of faces of a disconnected embedding as F(M) - c(M) + 1 (so every tree component, in particular every isolated K_2, contributes exactly zero), which annihilates the entire argument; Conjecture 9.1 remains open.
---

## Interpretation

The catalog statement matches Conjecture 9.1 of arXiv:2211.01032v3 verbatim ("For any
$p(n): \mathbb{N} \rightarrow [0,1]$, almost all graphs in $G(n,p)$ satisfy
$\E[F] = O(\log(n))$"). The entire question is what $F$ means for a disconnected graph,
since for $p = 1/n$ the sampled graph is a.a.s. disconnected.

The writeup asserts (its "Statement and convention" section) that "There is a canonical
extension to disconnected graphs: ... each component is embedded in its own orientable
surface. Under this extension, the number of faces is additive over components." It then
refutes the conjecture under that additive convention via isolated $K_2$ components.

This is exactly the failure mode of interpretation gaming, and here it is not even a
defensible literal reading, because the source paper **explicitly defines the opposite
convention**. In Section 7 (v3 TeX source, immediately before the proof of Theorem 1.10,
the $\E[F(n,p)] \le H_n^2 + 1/p$ bound), the paper states:

> "Note that the underlying graph of the embedding outputted by this process may not be
> connected. To allow for that case, we define the *number of faces* for maps that are
> not connected as the sum of the number of faces in each connected component minus the
> number of connected components plus one. This corresponds to the fact that one can
> always pick an arbitrary face $f_1$ in one connected component $H_1$ and an arbitrary
> face $f_2$ in another connected component $H_2$ and insert the whole embedding of $H_2$
> inside $f_1$ using $f_2$ as a boundary. **Note that each isolated vertex (in fact any
> tree) always contributes zero towards the number of faces.**"

and defines $F(n,p) := F(M) - c(M) + 1$. Corollary 7.3 (`cor:almostallpolylog`) defines
$X(G) := \E[F(G)]$ per sampled graph with $\E[X(G)] = \E[F(n,p)]$, i.e. the per-graph face
count in the "almost all graphs" statements uses this same disconnected-face convention.
Section 9 introduces Conjecture 9.1 directly from these results ("The same Markov's
inequality argument as in [Cor 7.3] gives that most sparse graphs have a logarithmic
average number of faces. This leads us to the conjecture..."). So the $\E[F]$ in
Conjecture 9.1 is unambiguously the paper's $F - c + 1$ statistic, under which every tree
component — in particular every isolated $K_2$ — contributes exactly zero, by the paper's
own remark quoted above.

Under the intended convention the writeup's obstruction vanishes identically: $X$ isolated
edges contribute $X$ faces and $X$ components, net $0$. My Monte Carlo run (Check 4 below)
confirms the paper-convention face count of a random embedding of $G(n,1/n)$ stays ~1.5-1.7
while the additive count grows linearly. No reasonable author of the original paper would
consider Conjecture 9.1 resolved by this argument; indeed, had the additive reading been
intended, the conjecture would be trivially false by counting components, and the authors
— who explicitly note that trees contribute zero — would never have posed it. The writeup
even concedes in its own caveats that a "corrected conjecture may remain open"; the
"correction" it gestures at (its option 4, "removing contributions from separate tree
components") is essentially the definition the paper already made, which the writeup
failed to check.

**Interpretation verdict: not the intended one; the refutation targets a strawman that the
source paper explicitly excludes.**

## Step-by-step findings

| step | label | note |
|---|---|---|
| S1. Convention: $F$ extends to disconnected graphs additively over components ("canonical", "standard") | **ERROR** | The source paper explicitly defines faces of disconnected maps as $F(M) - c(M) + 1$ (Section 7, v3), noting any tree component contributes zero. The additive convention is not the paper's, and the conjecture's $\E[F]$ inherits the paper's definition via Cor 7.3. This error is load-bearing for the whole verdict. |
| S2. An isolated $K_2$ component has exactly one face in every embedding (dart model: rotations trivial, face permutation one 2-cycle) | VALID | Verified by code: 100/100 random embeddings of $K_2$ give exactly 1 face (Euler: $2-1+F=2$). But under the paper's convention its net contribution is $1 - 1 = 0$. |
| S3. Hence $F(G,\rho) \ge X(G)$ deterministically ($X$ = number of isolated $K_2$ components) | VALID *given S1* | Correct under the additive convention only; false for the paper's statistic, where the contribution is 0. |
| S4. $q = \mathbb{P}(I_e{=}1) = p(1-p)^{2(n-2)}$ | VALID | Edge present ($p$); the $2(n-2)$ other potential edges at its two endpoints absent. Exponent $2n-4$ is right for the pair-isolation event in $G(n,p)$. |
| S5. $\mu = \binom{n}{2}\frac1n(1-\frac1n)^{2n-4} = (\frac{e^{-2}}{2}+o(1))n$ | VALID | Re-derived and checked numerically: $n=3000$ gives exact $\mu = 203.14$ vs $e^{-2}n/2 = 203.00$; Monte Carlo mean 201.8 over 40 trials. |
| S6. $\operatorname{Var} X = O(n)$: sharing pairs have negative covariance; disjoint pairs have $\mathbb{P}(I_e{=}I_f{=}1) = p^2(1-p)^{4n-12}$, so $\operatorname{Cov} = q^2((1-p)^{-4}-1) = O(n^{-3})$ | VALID | Re-derived: absent-edge count for two disjoint isolated edges is $4(n-4)+4 = 4n-12$; covariance identity checked symbolically and numerically ($2.72\times10^{-12}$ at $n=3000$, well within $O(n^{-3})$). $O(n^4)$ pairs $\times O(n^{-3}) + \sum\operatorname{Var}(I_e) \le \mu$ gives $O(n)$. Empirical sample variance $\approx 200 \approx 0.067n$. |
| S7. Chebyshev $\Rightarrow X/n \to e^{-2}/2$ in probability; $X = \Theta(n)$ a.a.s. | VALID | Standard second-moment argument; numbers confirm concentration. |
| S8. Therefore $f(G) \ge X = \Theta(n)$ a.a.s., so $\mathbb{P}(f(G) \le C\log n) \to 0$, refuting the conjecture | **ERROR** | Follows only under the additive convention of S1. Under the paper's actual definition the same graphs have paper-convention face count $O(\log n)$-compatible (Monte Carlo: mean $F - c + 1 \approx 1.5$-$1.7$ for $n = 200..1600$). The conjecture is not refuted. |
| S9. Persistence for $np \to \infty$: at $p = \frac{\log n}{4n}$, $\E[X] = (1+o(1))\frac18 n^{1/2}\log n$ | VALID (arithmetic) | Checked: at $n = 10^6$ the exact expectation and $\frac18\sqrt n\log n$ agree to 4 decimal places (ratio 1.0000). Same interpretation flaw applies. |
| S10. "Connectedness caveat": if $F$ is defined only for connected graphs the conjecture is ill-posed; lists four inequivalent corrected formulations | **ERROR** (as diligence) | The dichotomy "connected-only vs additive" is false: the paper defines a third thing, $F - c + 1$, explicitly and prominently, in the very section proving the theorem the conjecture generalizes. The writeup guesses at corrections instead of reading the source, and its guessed option 4 is roughly the paper's actual definition. |

## Reference check

- **Conjecture 9.1** (arXiv:2211.01032v3, Section 9 "Open Problems"): confirmed verbatim
  from the TeX source (`RE-arxiv3.tex`, downloaded from arXiv e-print, lines 2579-2581):
  "For any $p(n): \mathbb{N} \rightarrow [0,1]$, almost all graphs in $G(n,p)$ satisfy
  $\E[F] = O(\log(n))$." Matches the catalog statement.
- **Disconnected-face definition**: confirmed verbatim (lines 1791-1793): faces of a
  disconnected map $:=$ sum over components $-\ c + 1$; "each isolated vertex (in fact any
  tree) always contributes zero"; $F(n,p) := F(M) - c(M) + 1$.
- **Theorem 1.10 / `thm:randomgraphs`**: $\E[F(n,p)] \le H_n^2 + 1/p$ — confirmed; it is
  stated for the $F - c + 1$ statistic (which is why the bound can be polylog + $1/p$
  despite $\Theta(n)$ components at $p = 1/n$).
- **Corollary 7.3 / `cor:almostallpolylog`**: confirmed; $X(G) := \E[F(G)]$,
  $\Pr[X(G) \ge t(H_n^2 + 1/p)] \le 1/t$, with $\E[X(G)] = \E[F(n,p)]$ — this pins the
  per-graph convention used by the conjecture.
- **Conjecture 1.13 / `con:random`**: confirmed; $\E[F] = (1+o(1))\ln(pn^2)$ for
  $G \in G(n,p)$, matching the catalog's reviewer notes.
- **Writeup's sourcing**: the writeup cites only "the source abstract" and asserts the
  additive extension is "canonical"/"standard" without consulting the paper body. That
  assertion misrepresents the source, hence `references_ok: false`.

## Computational check

Script: `verification/scripts/2211.01032__01/check.py`
(pure Python stdlib; seeded). Results:

1. **$K_2$ face count**: 100/100 uniformly random rotation systems of an isolated edge
   yield exactly 1 face (and sanity checks: triangle always 2 faces, path $P_3$ always
   1 face). Writeup's S2 confirmed — and its net paper-convention contribution when added
   as an extra component is $1 - 1 = 0$.
2. **Isolated edges in $G(n, 1/n)$**, $n = 3000$, 40 trials: exact
   $\E X = 203.14$ vs asymptotic $e^{-2}n/2 = 203.00$; Monte Carlo mean $201.8$,
   sample variance $199.6 \approx 0.067n$ (consistent with $\operatorname{Var} = O(n)$);
   $X/n = 0.0673$ vs $e^{-2}/2 = 0.0677$. Writeup's S5-S7 confirmed. Disjoint-pair
   covariance identity checked numerically: $2.721\times10^{-12}$, matching the writeup's
   formula exactly and bounded by $n^{-3} = 3.7\times10^{-11}$.
3. **$p = \log n/(4n)$**, $n = 10^6$: exact $\E X = 1726.9$ vs claimed
   $\frac18\sqrt n \log n = 1726.9$ (ratio 1.0000). Writeup's S9 arithmetic confirmed.
4. **The decisive check — additive vs paper convention** on random embeddings of sampled
   $G(n,1/n)$ (12 graphs per $n$, one random rotation system each, isolated vertices
   counted as 1-face sphere components):

   | $n$ | mean additive $F$ | mean isolated $K_2$ | mean paper $F - c + 1$ |
   |---|---|---|---|
   | 200 | 101.4 | 13.9 | 1.58 |
   | 400 | 201.5 | 30.3 | 1.67 |
   | 800 | 408.6 | 54.2 | 1.67 |
   | 1600 | 807.9 | 103.0 | 1.50 |

   The additive count grows linearly exactly as the writeup computes, but the statistic
   the paper's conjecture is about stays bounded (indeed far below $\log n$) on the same
   samples. The writeup's mechanism has zero effect on the conjectured quantity.

## Caveats

- The writeup's probabilistic content (S4-S7, S9) is entirely correct; the failure is
  purely one of formalization. Nothing in it touches the actual open problem: for the
  paper's statistic, tree components contribute 0, unicyclic components contribute their
  face count minus 1 (and $G(n, c/n)$ has only $O(1)$ non-tree components outside the
  giant for fixed $c \ne 1$), so no easy component-counting refutation exists; the
  conjecture genuinely remains open.
- The writeup's own JSON caveat ("a version conditioned on connectedness or concerning
  one distinguished component is different") shows awareness that the verdict hinges on
  the convention — but it resolved the ambiguity by fiat ("canonical", "standard")
  instead of by checking the freely available source, where the answer is explicit.
- The catalog page itself quotes the conjecture without the disconnected-face definition;
  an attacker working only from the catalog could be misled. Future catalog entries for
  this problem should include the paper's $F(M) - c(M) + 1$ convention.
- Minor: the paper's Section 8 sparse results (Theorems 1.11/1.12) require degree
  sequences with all degrees $\ge 2$, so they never meet isolated edges; consistent with
  the above, not evidence for the additive reading.
- Convention robustness: the "one face per component" the writeup relies on is real under
  any convention (each component's surface has $\ge 1$ face); only the paper's explicit
  $-c+1$ normalization removes it, and that normalization is the paper's stated
  definition, not a post-hoc repair.

## Referee summary

The writeup "disproves" Conjecture 9.1 by taking $p = 1/n$, observing that $G(n,1/n)$
a.a.s. contains $\Theta(n)$ isolated $K_2$ components, and noting each contributes one
face when every component is embedded in its own surface and faces are summed. All of its
computations are correct (I re-derived them and verified them numerically), but the
argument refutes only a strawman: the source paper explicitly defines the number of faces
of a disconnected embedding as (sum over components) $- c + 1$ and remarks in so many
words that "any tree always contributes zero towards the number of faces" — precisely to
make its $G(n,p)$ results and the ensuing Conjecture 9.1 meaningful for disconnected
samples. Under the intended statistic the isolated-edge obstruction contributes exactly
zero (Monte Carlo: paper-convention face counts $\approx 1.5$ on graphs whose additive
counts are in the hundreds), and the conjecture is untouched. Claimed verdict "disproved"
is rejected: FATAL_ERROR, the open problem remains open.

