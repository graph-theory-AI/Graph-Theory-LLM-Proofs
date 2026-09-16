Attack the following open graph-theory problem.

Catalog id: 2211.01032__00
Catalog status: open (triage tier 3, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2211.01032__00/
Source paper: Random Embeddings of Graphs: The Expected Number of Faces in Most Graph… (arXiv:2211.01032)

=== Catalog page (statement + literature review) ===
Expected faces in G(n,p) random embedding logarithmic — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 1.13 from arXiv:2211.01032 asserts that the expected number of faces in a random embedding of G(n,p) is (1+o(1))ln(pn^2). The authors prove a weaker log-squared upper bound E[F(G(n,p))] <= ln^2(n) + 1/p (Theorem 1.10), and obtain tight Theta(log n) results for bounded-degree random graph models, but the full conjecture for arbitrary G(n,p) remains open. No subsequent paper resolving the conjecture was found in a search of the literature through May 2026.

 Reviewer notes. The paper was submitted to arXiv in November 2022 and revised to its current form in April 2025 (SODA 2024 extended abstract). The authors explicitly note that extending their proof technique from complete graphs and bounded-degree models to general G(n,p) 'requires further ideas' and list this as an open problem in Section 9. No follow-up paper resolving the conjecture was found in four web searches; the conjecture is recent and open with high confidence.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. Let $p = p(n)$ be the probability of edges in $G(n,p)$. The expected number of faces in a random embedding of a random graph $G \in G(n,p)$ is $(1 + o(1))\ln(pn^{2})$.

Context

In light of the paper's theorems for specific graph families and Monte Carlo experiments, the authors conjecture that a logarithmic bound holds for any usual model of random graphs. Extending the proof of Theorem 1.5 to arbitrary random graphs requires further ideas; Section 9 provides additional discussion.

Also stated in

 
Random Embeddings of Graphs: The Expected Number of Faces in Most Graphs is Logarithmic (2025-04-09) 

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
  "one_line": "For the unconditioned model as stated, taking p=(log n)/(3n) makes isolated K2 components alone contribute asymptotically n^(1/3)log(n)/6 faces, far more than log(pn^2).",
  "would_publish": false,
  "caveats": "This refutes the unrestricted catalog wording, not a version conditioned on connectivity or restricted to the connected regime."
}
```

## 1. Statement and convention

For a graph \(G\), let \(D(G)\) be its set of directed edges. A rotation system is a product \(\rho=\prod_v\rho_v\), where \(\rho_v\) is a cyclic permutation of the darts with tail \(v\). If
\[
\alpha(u,v)=(v,u)
\]
is edge reversal, then the faces are the cycles of the facial permutation
\[
\phi=\rho\alpha.
\]

For disconnected graphs, the standard permutation definition is componentwise: the dart set of every edge-containing component is invariant under \(\phi\), and the total number of faces is the sum of the numbers of facial cycles on those components.

Under this interpretation, the conjecture as supplied—without a connectivity condition or a lower bound on \(p\)—is false, even when
\[
\log(pn^2)\longrightarrow\infty
\quad\text{and}\quad
np\longrightarrow\infty.
\]

## 2. Isolated-edge obstruction

Let \(X_2(G)\) denote the number of components of \(G\) isomorphic to \(K_2\).

An isolated \(K_2\) has two darts. Both local rotations are identities, so its facial permutation is the transposition of the two darts and hence has exactly one cycle. Consequently, for every rotation system,
\[
F(G,\rho)\ge X_2(G).
\]
Averaging over both \(G\) and the rotations gives
\[
\mathbb E F(G(n,p))\ge \mathbb E X_2(G(n,p)).
\]

For a fixed unordered pair \(\{u,v\}\), it is an isolated \(K_2\) precisely when \(uv\) is present and all \(2(n-2)\) other edges incident with \(u\) or \(v\) are absent. Hence
\[
\mathbb E X_2
 =\binom n2 p(1-p)^{2n-4}.
\tag{1}
\]

Now take
\[
p=\frac{\log n}{3n}.
\]
Since \(np^2=o(1)\),
\[
(1-p)^{2n-4}
 =\exp\!\left(-(2n-4)p+O(np^2)\right)
 =(1+o(1))n^{-2/3}.
\]
Substitution into (1) yields
\[
\mathbb E X_2
 =(1+o(1))
 \frac{n^2}{2}\frac{\log n}{3n}n^{-2/3}
 =(1+o(1))\frac{n^{1/3}\log n}{6}.
\]
Therefore
\[
\mathbb E F(G(n,p))
 \ge (1+o(1))\frac{n^{1/3}\log n}{6}.
\tag{2}
\]

On the other hand,
\[
\log(pn^2)
 =\log\!\left(\frac{n\log n}{3}\right)
 =\log n+\log\log n-\log 3
 =(1+o(1))\log n.
\]
Thus (2) gives
\[
\frac{\mathbb E F(G(n,p))}{\log(pn^2)}
 \longrightarrow\infty,
\]
rather than \(1\). This disproves the unrestricted statement.

More generally, writing \(p=d/n\), whenever \(d=o(\sqrt n)\),
\[
\mathbb E F(G(n,p))
 \ge (1+o(1))\frac{nd}{2}e^{-2d}.
\tag{3}
\]
For example, if \(d=(\tfrac12-\varepsilon)\log n\), the lower bound in (3) is of order
\[
n^{2\varepsilon}\log n,
\]
again much larger than \(\log(pn^2)\).

## 3. A separate dense-case partial result

The counterexample above does not address a version restricted to connected graphs or, for example, to
\[
p\ge \frac{\log n+\omega(1)}n.
\]
For that intended version, one can nevertheless improve the quoted lower bound for the endpoint case \(p=1\).

### Proposition
For a random rotation system of \(K_n\),
\[
\mathbb E F(K_n)\ge \log n-O(1).
\tag{4}
\]

This remains a factor \(2\) below the conjectured value
\[
\log(n^2)=2\log n.
\]

### Proof

Write the darts of \(K_n\) as ordered pairs \((u,v)\), \(u\ne v\). Let \(C_k\) be the number of facial cycles of length \(k\).

Consider a cyclic word
\[
w=(v_0,v_1,\ldots,v_{k-1}),
\]
with indices modulo \(k\), and set
\[
e_i=(v_i,v_{i+1}).
\]
Call the word good if:

1. \(v_i\ne v_{i+1}\) for every \(i\);
2. the darts \(e_i\) are pairwise distinct;
3. no two of the \(e_i\) are reversals of one another.

If the \(v_i\) are chosen independently and uniformly from \([n]\), then, for \(k\ge5\),

- a loop occurs with probability at most \(k/n\);
- two darts coincide with probability at most \(\binom{k}{2}/n^2\);
- reversed darts occur with probability at most
  \[
  \frac{k}{n}+\frac{\binom{k}{2}}{n^2};
  \]
  the \(k/n\) term accounts for consecutive immediate reversals.

Thus the number \(\lvert\mathcal W_k\rvert\) of good words satisfies
\[
\lvert\mathcal W_k\rvert
 \ge n^k\left(1-\frac{2k}{n}-\frac{k^2}{n^2}\right).
\tag{5}
\]

For a fixed good word, the condition that it be a facial cycle is
\[
\rho_{v_{i+1}}(v_i)=v_{i+2}
\qquad(0\le i<k).
\tag{6}
\]
At a vertex \(x\), suppose (6) imposes \(t_x\) prescribed directed adjacencies in the cyclic order on the \(n-1\) neighbors of \(x\). Goodness ensures that these \(t_x\) prescribed adjacencies have pairwise disjoint endpoints: a common endpoint would give either a repeated dart or both orientations of an edge.

There are \((n-2)!\) cyclic permutations of the \(n-1\) neighbors of \(x\). Contracting the \(t_x\) prescribed directed adjacencies shows that exactly
\[
(n-t_x-2)!
\]
of them satisfy all the constraints. Therefore
\[
\Pr(\text{constraints at }x)
 =\frac{(n-t_x-2)!}{(n-2)!}
 \ge (n-1)^{-t_x}.
\]
The rotations at distinct vertices are independent and \(\sum_x t_x=k\), so
\[
\Pr(w\text{ is facial})\ge (n-1)^{-k}.
\tag{7}
\]

Each facial \(k\)-cycle gives exactly \(k\) cyclic words, one for every choice of starting dart. From (5) and (7),
\[
\mathbb E C_k
 \ge \frac{\lvert\mathcal W_k\rvert}{k(n-1)^k}
 \ge \frac1k\left(1-\frac{2k}{n}-\frac{k^2}{n^2}\right),
\tag{8}
\]
where we used \((n/(n-1))^k\ge1\).

Summing (8) for \(5\le k\le n/10\) gives
\[
\begin{aligned}
\mathbb E F(K_n)
&\ge
 \sum_{k=5}^{\lfloor n/10\rfloor}
 \left(\frac1k-\frac2n-\frac{k}{n^2}\right)\\
&=\log n-O(1),
\end{aligned}
\]
proving (4).

## 4. Scope and remaining gap

- The isolated-\(K_2\) calculation is a complete counterexample to the unconditioned statement supplied in the prompt.
- If the source intended \(G(n,p)\) conditioned on being connected, or assumed \(p\) above the connectivity threshold, that hypothesis is essential and the counterexample does not apply.
- Under such a corrected interpretation, the conjectured coefficient remains open. The additional \(K_n\) argument gives only
  \[
  \mathbb E F(K_n)\ge \log n-O(1),
  \]
  versus the desired \(2\log n+o(\log n)\), and supplies no matching upper bound.

--- referee report on that attempt ---
---
id: 2211.01032__00
claimed_verdict: disproved
review_verdict: FATAL_ERROR
confidence: high
interpretation_ok: false
references_ok: true
computation_run: true
one_line: The isolated-K2 "counterexample" is arithmetically correct but counts faces with a componentwise convention that the source paper explicitly rejects — arXiv:2211.01032 defines F(n,p) = F(M) - c(M) + 1, under which every tree component (isolated K2 included) contributes exactly zero, so Conjecture 1.13 is not disproved.
---

## Interpretation

The writeup claims to **disprove** Conjecture 1.13 of arXiv:2211.01032 ("The expected
number of faces in a random embedding of a random graph G ∈ G(n,p) is
(1+o(1)) ln(pn²)") by taking p = (log n)/(3n) and observing that isolated-K2
components alone then contribute Θ(n^{1/3} log n) faces.

The entire argument stands or falls on how the number of faces of a **disconnected**
embedding is counted. The writeup asserts (its Section 1):

> "For disconnected graphs, the standard permutation definition is componentwise:
> ... the total number of faces is the sum of the numbers of facial cycles on those
> components."

This is **not** the source paper's definition. I fetched arXiv:2211.01032v3 and
Section 7 (the section that defines and proves Theorem 1.10, the paper's only
G(n,p) result, and hence fixes what "number of faces of G(n,p)" means throughout the
paper) states verbatim:

> "Note that the underlying graph of the embedding outputted by this process may not
> be connected. To allow for that case, we define the number of faces for maps that
> are not connected as the sum of the number of faces in each connected component
> **minus the number of connected components plus one**. This corresponds to the fact
> that one can always pick an arbitrary face f₁ in one connected component H₁ and an
> arbitrary face f₂ in another connected component H₂ and insert the whole embedding
> of H₂ inside f₁ using f₂ as a boundary. **Note that each isolated vertex (in fact
> any tree) always contributes zero towards the number of faces.** ... We define
> F(n,p) as the random variable F(M) − c(M) + 1."

Under the paper's convention, an isolated K2 (a tree) contributes 1 − 1 = 0 faces —
the authors explicitly anticipated exactly the objection the writeup raises and
normalized it away. The correction needed is not "conditioning on connectivity"
(the writeup's own hedge in its caveats field and Section 4): the paper's definition
applies for **all** p with no connectivity assumption, and Conjecture 9.1 of the
paper ("For any p(n) : ℕ → [0,1], almost all graphs in G(n,p) satisfy
E[F] = O(log n)") only makes sense under it. My Monte Carlo (check [4] below)
confirms that at p = (log n)/(3n) the paper's F(n,p) stays near ln(pn²) while the
writeup's componentwise count blows up — the discrepancy is purely the convention.

No reasonable author of arXiv:2211.01032 would consider Conjecture 1.13 resolved by
this writeup. This is textbook interpretation gaming: the refuted statement is a
strawman reading whose defect the source paper explicitly repaired in print. Even
outside this paper, "faces of an embedding of a disconnected graph" has no unique
standard meaning (a 2-cell embedding requires a connected graph; per-component
surfaces vs. nesting into one surface differ by exactly c − 1), so the verdict
cannot rest on the writeup's chosen reading.

## Step-by-step findings

| step | label | note |
|------|-------|------|
| S1. Facial permutation setup φ = ρα (writeup §1) | VALID | Standard combinatorial-map formalism; matches the paper's (D,R,L) maps. |
| S1'. "For disconnected graphs, the standard permutation definition is componentwise" (writeup §1) | ERROR | Directly contradicts the source paper's explicit definition F(M) − c(M) + 1 (Section 7, quoted above), under which trees contribute zero. This is the load-bearing error. |
| S2. Isolated K2 has exactly 1 facial cycle; F(G,ρ) ≥ X₂(G) (writeup §2) | VALID (under writeup's convention only) | Verified by code: the 2-dart transposition has 1 cycle (check [1]). Under the paper's convention the same component contributes 1 − 1 = 0, and the inequality E F(n,p) ≥ E X₂ fails. |
| S3. E X₂ = C(n,2) p (1−p)^{2n−4}, eq. (1) | VALID | Verified exactly by full enumeration for n = 5 (three values of p, agreement to 1e−9) and by Monte Carlo for n = 8 (0.2208 vs 0.2217, T = 200000). |
| S4. At p = (log n)/(3n): (1−p)^{2n−4} = (1+o(1)) n^{−2/3}, E X₂ = (1+o(1)) n^{1/3} log n / 6, eq. (2) | VALID | Re-derived: (2n−4)p = (2/3)log n − o(1), np² = O(log²n / n) = o(1). Numerics: ratio E X₂ / (n^{1/3} ln n / 6) = 1.0000 at n = 10⁶…10¹⁰. |
| S5. log(pn²) = (1+o(1)) log n, hence ratio → ∞ (writeup §2) | VALID | Correct arithmetic. |
| S6. "This disproves the unrestricted statement" (writeup §2) | ERROR | The quantity bounded is not the paper's E[F(n,p)]. Under the paper's definition the K2 contribution is identically zero for every rotation system, so nothing about Conjecture 1.13 is disproved. Irreparable: no variant of the tree/K2-component argument survives F − c + 1 (unicyclic components contribute at most 1 each and there are only O(1) of them below the connectivity threshold). |
| S7. Generalization (3): d = o(√n) ⇒ E F ≥ (1+o(1)) (nd/2) e^{−2d} (writeup §2) | VALID (under writeup's convention only) | E X₂ = C(n,2)(d/n)(1−d/n)^{2n−4} ~ (nd/2)e^{−2d} needs d²/n = o(1), i.e. d = o(√n): correct. Same fatal convention problem as S6. |
| S8a. Good-word count, eq. (5): |W_k| ≥ n^k(1 − 2k/n − k²/n²) (writeup §3) | VALID | Loops ≤ k/n; coincident darts ≤ C(k,2)/n²; reversals ≤ k/n + C(k,2)/n² (the k/n term covers immediate reversals v_{i+2} = v_i). Union bound gives 2k/n + 2·C(k,2)/n² ≤ 2k/n + k²/n². |
| S8b. Facial condition (6): ρ_{v_{i+1}}(v_i) = v_{i+2} | VALID | With φ = ρα this is exactly φ(e_i) = e_{i+1}; goodness (distinct darts) makes the orbit of e₀ have length exactly k. Orientation convention immaterial by symmetry of the uniform rotation. |
| S8c. Endpoint-disjointness of the t_x constraints at each vertex | VALID | Re-derived all four coincidence cases (a=a′, b=b′, a=b′, b=a′, and a=b within one constraint): each forces a repeated dart or a reversal pair, excluded by goodness. Verified computationally on random good words with repeated vertices (check [2], 6/6 words OK). |
| S8d. Per-vertex count (n−t_x−2)!/(n−2)!, and ≥ (n−1)^{−t_x} | VALID | Contraction argument correct for disjoint prescribed adjacencies; verified by exhaustive enumeration of cyclic permutations (m = 6,7, t = 1,2,3) and, for actual word-derived constraint systems on K₈, per-vertex satisfaction counts equal (n−t_x−2)! in all tested cases. (n−t−2)!/(n−2)! = 1/((n−2)⋯(n−t−1)) ≥ (n−1)^{−t}: correct. |
| S8e. Independence over vertices ⇒ Pr(w facial) ≥ (n−1)^{−k}, eq. (7) | VALID | Rotations at distinct vertices independent; Σ_x t_x = k. |
| S8f. Each good facial k-cycle ↔ exactly k good words; E C_k bound (8) | VALID | Good faces have no periodicity (distinct darts), so exactly k pointed words each; faces repeating darts or containing reversal pairs are simply not counted — harmless for a lower bound. MC check on K₁₀₀: E[#good facial 5-cycles] = 0.2052 ≥ bound 0.1795 (check [3]). |
| S8g. Summation over 5 ≤ k ≤ n/10 gives E F(K_n) ≥ log n − O(1), eq. (4) | VALID | Σ 1/k = ln n − O(1); Σ 2/n ≤ 1/5; Σ k/n² ≤ 1/200. MC values E F(K₂₀) ≈ 5.09, E F(K₅₀) ≈ 6.85, E F(K₁₀₀) ≈ 8.39 track ≈ 2 ln n, consistent with the bound. |
| S9. Scope discussion (writeup §4) | ERROR (diagnosis) | Correctly concedes the K_n result leaves the conjecture open, but wrongly asserts the isolated-K2 calculation is "a complete counterexample to the unconditioned statement supplied in the prompt" and misidentifies the fix as a connectivity hypothesis; the actual fix — the paper's stated F − c + 1 definition — needs no hypothesis at all. |

## Reference check

- **Conjecture 1.13** (arXiv:2211.01032v3, Section 1.3): fetched and quoted verbatim —
  "Let p = p(n) be the probabillity of edges in G(n,p). The expected number of faces
  in a random embedding of a random graph G ∈ G(n,p) is (1+o(1)) ln(pn²)." Matches
  the catalog/prompt wording. No explicit hypothesis on p — but the paper's own
  definition of "number of faces" for possibly-disconnected maps (Section 7) governs.
- **Theorem 1.10**: "Let n be a positive integer and p ∈ (0,1] (p = p(n)). Then
  E[F(n,p)] ≤ H_n² + 1/p", with F(n,p) := F(M) − c(M) + 1 defined in Section 7.
  Confirms the paper's G(n,p) face count is the normalized one. (The catalog's
  "ln²n + 1/p" is a harmless paraphrase of H_n².)
- **Theorem 1.6** (the "quoted lower bound" the writeup's Proposition improves):
  "For all positive integers n, E[F(n)] > (1/2)ln(n) − 2." Confirmed verbatim.
- **Conjectured value 2 ln n for K_n**: Conjecture 9.4 of the paper ("2 ln n + O(1)",
  attributed to [36, p. 289]) and Conjecture 1.13 at p = 1 both give ln(n²) = 2 ln n.
  Confirmed.
- **Section 9**: Conjecture 9.1 ("For any p(n): ℕ → [0,1], almost all graphs in
  G(n,p) satisfy E[F] = O(log n)") confirms the authors intend their statement to
  cover all p under their normalized face count — a.a.s. G(n, (log n)/(3n)) has
  ≫ log n tree components, so 9.1 is only coherent with the F − c + 1 convention,
  independently corroborating the interpretation finding.
- The writeup cites no other external results. references_ok: true (everything it
  quotes exists and is quoted accurately; what it gets wrong is the paper's
  definition, which it never checked).

## Computational check

Scripts in `verification/scripts/2211.01032__00/`:

`check_counterexample.py`:
1. Isolated K2 facial permutation has exactly **1** cycle (componentwise): confirmed.
2. E X₂ = C(n,2)p(1−p)^{2n−4}: exact for n = 5 at p = 0.1/0.3/0.5 (e.g. 0.531441 =
   0.531441); MC n = 8, p = 0.25: 0.2208 vs 0.2217 (T = 200000).
3. At p = (log n)/(3n): E X₂ / (n^{1/3} ln n / 6) = 1.0002, 1.0000, 1.0000, 1.0000
   for n = 10⁴, 10⁶, 10⁸, 10¹⁰; ln(pn²) = 10.3, 15.3, 20.2, 25.1. The writeup's
   asymptotics are exactly right — under its convention.
4. **The decisive check**: G(300, ln(300)/900), T = 30 random (graph, rotation)
   samples: mean componentwise face count over edge-containing components = **14.17**
   (mean X₂ alone = 5.90), while the paper's F(n,p) = F(M) − c(M) + 1 = **5.03**,
   versus ln(pn²) = 6.35. The paper-convention count is entirely consistent with
   Conjecture 1.13; only the writeup's convention diverges.

`check_proposition.py` (the side result, writeup §3):
1. Uniform cyclic permutation of m elements, t disjoint prescribed adjacencies:
   satisfying count = (m−1−t)! exactly, verified exhaustively (m = 6,7; t = 1,2,3).
2. Six random good words on K₈ (including words with 1–2 repeated vertices): the
   claimed endpoint-disjointness of per-vertex constraints holds, and exhaustive
   per-vertex enumeration gives exactly (n−t_x−2)! satisfying rotations, every time.
3. K₁₀₀, T = 4000: E[#good facial 5-cycles] = 0.2052 ≥ bound (8) value 0.1795
   (and ≈ n⁵/(5(n−1)⁵) = 0.2103, as the proof predicts). E F(K_n) MC: 5.09, 6.85,
   8.39 for n = 20, 50, 100 — tracking ≈ 2 ln n, consistent with the Proposition's
   E F(K_n) ≥ ln n − O(1).

No computational check failed; the writeup's finite/asymptotic arithmetic is sound.
The fatal problem is not arithmetic but which quantity is being bounded.

## Caveats

- The whole verdict is convention-dependent and the writeup bet on the wrong
  convention: the source paper defines F for disconnected maps as
  Σ(component faces) − c(M) + 1, with trees (hence isolated K2's and isolated
  vertices) contributing zero. The writeup never fetched or checked this definition,
  despite hedging that a "conditioned on connectivity" variant would escape — the
  actual escape needs no conditioning at all.
- Even as a refutation of the "literal catalog wording", the claim is shaky: the
  catalog sentence is copied from the paper, whose own definitions resolve the
  ambiguity; and "number of faces of a random embedding" of a disconnected graph has
  no convention-free meaning (2-cell embeddings are defined for connected graphs).
- Under the paper's convention the writeup's approach is unrepairable below the
  connectivity threshold: tree components give 0, unicyclic components give at most
  1 each and only O(1) many exist outside the giant component, so no
  component-counting argument can beat Θ(log n).
- The Section 3 Proposition (E F(K_n) ≥ ln n − O(1)) survived all my checks and, if
  new, would improve the paper's Theorem 1.6 lower bound (1/2)ln n − 2 by a factor
  of 2 — a legitimate but modest partial result that resolves nothing (the
  conjectured value at p = 1 is 2 ln n). I did not certify its novelty against the
  literature (Stahl's random-embedding work and follow-ups on E F(K_n) should be
  searched before publicizing it).
- Minor: the writeup's k ≥ 5 restriction and the k ≤ n/10 cutoff are safe but
  unexplained; both only cost O(1). Its use of "log" vs the conjecture's "ln" is
  consistent (natural log throughout).

## Referee summary

The writeup's claimed disproof of Conjecture 1.13 is arithmetically flawless and
completely beside the point. It shows that at p = (log n)/(3n) the expected number
of isolated-K2 components of G(n,p) is (1+o(1)) n^{1/3} log n / 6 — verified exactly
and numerically — and concludes E F ≫ ln(pn²) by counting one face per isolated
edge. But arXiv:2211.01032 explicitly defines the face count of a disconnected map
as F(M) − c(M) + 1 and states in Section 7 that "each isolated vertex (in fact any
tree) always contributes zero towards the number of faces"; the authors built their
G(n,p) theorem (1.10) and their all-p Conjecture 9.1 on precisely this convention.
Under it the counterexample contributes exactly zero and Conjecture 1.13 is
untouched, for every p, with no connectivity hypothesis needed. This is
interpretation gaming — a strawman literal reading whose defect the source paper
repaired in print — and it is irreparable, so the claimed verdict "disproved" is a
FATAL_ERROR. The accompanying K_n side result (E F(K_n) ≥ ln n − O(1)) checked out
computationally and analytically but is only a partial lower bound, a factor 2 below
the conjectured 2 ln n.

