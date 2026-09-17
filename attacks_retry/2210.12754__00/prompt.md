Attack the following open graph-theory problem.

Catalog id: 2210.12754__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2210.12754__00/
Source paper: Largest subgraph from a hereditary property in a random graph (arXiv:2210.12754)

=== Catalog page (statement + literature review) ===
p(n) range for hereditary subgraph concentration — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 The source paper proves Theorem 1.1 for fixed p ∈ (0,1) and for p = p(n) satisfying n^{−c} ≤ p ≤ 1−n^{−c}, but the full characterization of all p = p(n) for which the conclusion holds remains open. A 2024 follow-up (arXiv:2405.09486) explicitly addresses a question of Alon, Krivelevich and Samotij in the hereditary setting but still restricts its main results to fixed p ∈ (0,1), leaving the variable-probability regime unresolved.

 Cited literature (1)

 
 
 
partial Subgraphs of random graphs in hereditary families
 (2024)
 

 
 not verified from abstract · arXiv preprint · arXiv:2405.09486

Explicitly addresses a question of Alon, Krivelevich and Samotij about subgraphs in hereditary families, but its stated results remain in the regime of fixed p ∈ (0,1) rather than characterizing all p = p(n).
 

 

 Reviewer notes. No paper found that resolves the full characterization of all p = p(n). arXiv:2405.09486 (2024) is the closest follow-up, explicitly citing the question of Alon-Krivelevich-Samotij, but its results are for fixed p. A related paper arXiv:2405.05902 (Fox, Nenadov, Pham; Combinatorica 2025, 'The Largest Subgraph Without A Forbidden Induced Subgraph') generalizes the framework to pseudorandom/quasirandom host graphs, but it was found via search only and not fully verified via WebFetch so is excluded from since_posted. The conjecture is open with medium confidence because active follow-up work exists but the specific p = p(n) characterization problem appears unaddressed.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Problem. Characterize all edge probabilities $p = p(n)$ for which the assertion of Theorem 1.1 holds.

Context

Theorem 1.1 is proved for fixed $p \in (0,1)$ and (via Proposition 2.1) for $p = p(n)$ satisfying $n^{-c} \leq p \leq 1-n^{-c}$. The authors note that hereditary (even monotone) properties exist for which the fraction of edges of $G(n,p)$ lying in a maximum in-$\mathcal{P}$ subgraph changes, whp, several times as $p$ increases from 0 to 1.

Notes. PDF source; stated as an informal open problem in the concluding remarks without a labelled environment.

Source paper

 Largest subgraph from a hereditary property in a random graph
 Noga Alon, Michael Krivelevich, Wojciech Samotij · 2022-10-23
 https://arxiv.org/abs/2210.12754
 PDF source

=== Source paper abstract / header ===
Abstract:We prove that for every non-trivial hereditary family of graphs ${\cal P}$ and for every fixed $p \in (0,1)$, the maximum possible number of edges in a subgraph of the random graph $G(n,p)$ which belongs to ${\cal P}$ is, with high probability, $$ \left(1-\frac{1}{k-1}+o(1)\right)p{n \choose 2}, $$ where $k$ is the minimum chromatic number of a graph that does not belong to ${\cal P}$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 
 
 MSC classes:
 05C80, 05C35
 

 Cite as:
 arXiv:2210.12754 [math.CO]
 

 
  
 (or 
 arXiv:2210.12754v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2210.12754
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Michael Krivelevich [view email] 
 [v1]
 Sun, 23 Oct 2022 15:39:53 UTC (7 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Largest subgraph from a hereditary property in a random graph, by Noga Alon and 2 other authors
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
 | 2022-10
 

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
The problem above was already attacked by `gpt-5.6-sol`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The property-independent range is exactly that both p and 1-p are n^{-o(1)}, and sharp wider ranges are obtained for s-colourable and 2-balanced F-free properties, while the arbitrary fixed hereditary property remains unresolved.",
  "would_publish": false,
  "caveats": "The universal quantifier is fully handled; the property-by-property problem remains open, and one special-case upper bound uses the established sparse random Turan theorem."
}
```

# Mathematical writeup

## 1. Formulation and the quantifier issue

Let \(\mathcal P\) be a nontrivial hereditary graph property, in the induced-subgraph sense used in the source paper, and define
\[
\operatorname{ex}_{\mathcal P}(G)
  :=\max\{e(H):H\subseteq G,\ H\in\mathcal P\}.
\]
Let
\[
k(\mathcal P):=\min\{\chi(F):F\notin\mathcal P\},
\qquad
\pi(\mathcal P):=1-\frac1{k(\mathcal P)-1},
\]
and write \(N=\binom n2\). The variable-\(p\) assertion is interpreted as
\[
\frac{\operatorname{ex}_{\mathcal P}(G(n,p))}{pN}
   \xrightarrow{\mathbb P}\pi(\mathcal P).
\tag{1}
\]

There are two possible readings of the open problem.

1. **Property-independent reading:** characterize those sequences \(p=p(n)\) for which (1) holds for every fixed nontrivial hereditary \(\mathcal P\).
2. **Property-by-property reading:** for each prescribed \(\mathcal P\), characterize its admissible \(p\)-range.

The first reading admits a complete answer. The second, which is likely what the concluding remarks intended, remains open. I also give two sharp property-specific results.

---

## 2. Exact maximal range valid for every hereditary property

### Theorem 2.1

Let \(0<p(n)<1\). The following are equivalent.

1. For every fixed nontrivial hereditary property \(\mathcal P\), assertion (1) holds.
2. For every fixed \(\varepsilon>0\), eventually
   \[
   n^{-\varepsilon}\le p(n)\le 1-n^{-\varepsilon}.
   \tag{2}
   \]
3. Equivalently,
   \[
   \frac{\log(1/p(n))}{\log n}\longrightarrow0,
   \qquad
   \frac{\log(1/(1-p(n)))}{\log n}\longrightarrow0.
   \tag{3}
   \]

Thus the maximal property-independent range is
\[
p=n^{-o(1)}
\quad\text{and}\quad
1-p=n^{-o(1)}.
\]

### Proof: sufficiency

The extension of Proposition 2.1 recorded in the question gives the following: for every fixed \(\mathcal P\) and every fixed accuracy \(\eta>0\), there is \(c=c(\mathcal P,\eta)>0\) such that the conclusion of Theorem 1.1, with error at most \(\eta pN\), holds whenever
\[
n^{-c}\le p\le1-n^{-c}.
\tag{4}
\]

If (2) holds, then for this particular \(c\), condition (4) holds for all sufficiently large \(n\). Since this is true for every fixed \(\eta>0\), (1) follows.

For completeness, the lower bound is transparent. By the definition of \(k=k(\mathcal P)\), every \((k-1)\)-colourable graph belongs to \(\mathcal P\). Taking all random edges across a fixed balanced \((k-1)\)-partition therefore gives
\[
\operatorname{ex}_{\mathcal P}(G(n,p))
 \ge \left(1-\frac1{k-1}-o(1)\right)pN
\]
with high probability. Under (2), \(pN\to\infty\), so ordinary Chernoff concentration applies.

### Proof: necessity at the sparse end

Suppose the first condition in (3) fails. Then there are \(c>0\) and an infinite subsequence \(\mathcal N\) such that
\[
p(n)\le n^{-c}\qquad(n\in\mathcal N).
\]

Choose \(r\ge3\) so large that
\[
c\binom r2>r.
\]
Let \(\mathcal P\) be the monotone hereditary property of being \(K_r\)-free. Then \(k(\mathcal P)=r\), while
\[
\mathbb E[\#K_r\text{ in }G(n,p)]
 \le n^r p^{\binom r2}
 \le n^{r-c\binom r2}=o(1)
\]
along \(\mathcal N\). Hence \(G(n,p)\) itself is \(K_r\)-free with high probability, and consequently
\[
\operatorname{ex}_{\mathcal P}(G(n,p))=e(G(n,p))
\qquad\text{with high probability.}
\tag{5}
\]

Let \(\mu=pN\) and
\[
\pi_r=1-\frac1{r-1}\in(0,1).
\]
The binomial variable \(e(G(n,p))\) cannot satisfy
\[
e(G(n,p))/\mu\longrightarrow \pi_r
\]
in probability:

- if \(\mu\to\infty\), then \(e(G)/\mu\to1\);
- if \(\mu\to0\), then \(e(G)/\mu\to0\) in probability;
- if \(\mu\to\lambda\in(0,\infty)\), then \(e(G)\) has a nondegenerate Poisson limit.

After passing to a further subsequence, one of these cases always occurs. Together with (5), this contradicts (1).

### Proof: necessity at the dense end

Suppose the second condition in (3) fails. Put \(q=1-p\). Then for some \(c>0\) and infinitely many \(n\),
\[
q\le n^{-c}.
\]

Choose \(t\) sufficiently large that
\[
c\,\frac{t(t+5)}2>t+3,
\]
and let
\[
F:=K_3\mathbin{\dot\cup} I_t.
\]
Here
\[
v(F)=t+3,\qquad e(F)=3,\qquad
\overline e(F)=\binom{t+3}{2}-3=\frac{t(t+5)}2.
\]

Let \(\mathcal P\) be the hereditary property of containing no induced copy of \(F\). Every graph outside \(\mathcal P\) contains a triangle, while \(F\notin\mathcal P\), so
\[
k(\mathcal P)=3.
\]

The expected number of induced copies of \(F\) in \(G(n,p)\) is at most
\[
n^{t+3}p^3q^{t(t+5)/2}
 \le n^{\,t+3-c t(t+5)/2}=o(1).
\]
Thus \(G(n,p)\in\mathcal P\) with high probability, and hence
\[
\operatorname{ex}_{\mathcal P}(G(n,p))=e(G(n,p))
 =(1+o(1))pN.
\]
But Theorem 1.1 would predict \((1/2+o(1))pN\). This is a contradiction.

This proves Theorem 2.1. \(\square\)

### Interpretation

If “the assertion of Theorem 1.1” retains its outer quantifier over all fixed hereditary properties, Theorem 2.1 is a complete characterization. It does not characterize the range for a given property \(\mathcal P\), since many individual properties have much wider ranges.

---

## 3. A sharp self-contained case: \(s\)-colourable subgraphs

Let
\[
\mathcal C_s:=\{H:\chi(H)\le s\},
\qquad s\ge2.
\]
Then \(k(\mathcal C_s)=s+1\), and
\[
\pi_s=1-\frac1s.
\]

### Theorem 3.1

For fixed \(s\ge2\),
\[
\operatorname{ex}_{\mathcal C_s}(G(n,p))
   =(\pi_s+o(1))pN
\quad\text{with high probability}
\tag{6}
\]
if and only if
\[
np\longrightarrow\infty.
\tag{7}
\]

No condition on \(1-p\) is needed.

### Proof: sufficiency

For a colouring \(\sigma:V(G)\to[s]\), let \(X_\sigma\) be the number of random edges whose endpoints receive different colours. Then
\[
\operatorname{ex}_{\mathcal C_s}(G)=\max_\sigma X_\sigma.
\tag{8}
\]
Indeed, every \(s\)-colourable subgraph has such a colouring and can be enlarged by adding all available cross-colour edges.

The number \(M_\sigma\) of potential cross-colour pairs satisfies
\[
M_\sigma\le t_s(n)=\pi_sN+O(n).
\]
For fixed \(\sigma\), \(X_\sigma\sim\operatorname{Bin}(M_\sigma,p)\). Bernstein's inequality, followed by a union bound over the \(s^n\) colourings, gives, with high probability,
\[
X_\sigma\le pM_\sigma+O_s\!\left(n\sqrt{np}+n\right)
\qquad\text{for every }\sigma.
\]
When \(np\to\infty\),
\[
n\sqrt{np}+n=o(pn^2)=o(pN).
\]
Therefore
\[
\max_\sigma X_\sigma\le \pi_s pN+o(pN).
\]
A fixed balanced \(s\)-colouring has \(\pi_sN+O(n)\) cross-pairs, so Chernoff's inequality gives the matching lower bound.

### Proof: necessity

Suppose \(np\not\to\infty\). Pass to a subsequence on which \(np\le C\), and put \(\mu=pN\).

First suppose \(\mu\to\infty\). Let \(I\) be the number of components of \(G(n,p)\) isomorphic to \(K_2\). Then
\[
\mathbb E I
 =Np(1-p)^{2n-4}
 \ge e^{-4C}\mu
 =:\delta\mu
\]
for all sufficiently large \(n\). Since \(I\le e(G)\),
\[
\mathbb E I^2\le \mathbb E e(G)^2=\mu^2+\mu(1-p).
\]
Paley–Zygmund therefore gives
\[
\mathbb P\left(I\ge\frac{\delta\mu}{2}\right)
 \ge \frac{\delta^2}{4}+o(1).
\tag{9}
\]

Every isolated edge can be made bichromatic. Colour all other vertices independently and uniformly from \([s]\). Averaging over these colourings shows that some colouring retains at least
\[
I+\pi_s(e(G)-I)
 =\pi_s e(G)+(1-\pi_s)I
\]
edges. Combining this with (9) and \(e(G)=(1+o(1))\mu\), with probability bounded away from zero,
\[
\operatorname{ex}_{\mathcal C_s}(G)
 \ge \left(\pi_s+\frac{(1-\pi_s)\delta}{3}\right)\mu.
\]
Thus (6) does not hold with high probability.

If \(\mu\) is bounded, then \(p=O(n^{-2})\), and
\[
\mathbb E[\text{number of adjacent pairs of present edges}]
 =O(n^3p^2)=o(1).
\]
Thus \(G(n,p)\) is a matching with high probability and belongs to \(\mathcal C_s\). Hence \(\operatorname{ex}_{\mathcal C_s}(G)=e(G)\), whose normalized value cannot converge to \(\pi_s\in(0,1)\), by the same binomial trichotomy used above. \(\square\)

---

## 4. A sharp range for one forbidden 2-balanced graph

Let \(F\) be fixed with \(r=\chi(F)\ge3\). Define
\[
m_2(F):=
\max_{\substack{J\subseteq F\\v(J)\ge3}}
\frac{e(J)-1}{v(J)-2}.
\]
Call \(F\) 2-balanced if
\[
m_2(F)=\frac{e(F)-1}{v(F)-2}.
\]
Let \(\operatorname{Forb}(F)\) denote the monotone property of containing no ordinary copy of \(F\).

### Theorem 4.1

If \(F\) is 2-balanced and \(\chi(F)=r\ge3\), then
\[
\operatorname{ex}(G(n,p),F)
 =\left(1-\frac1{r-1}+o(1)\right)pN
\tag{10}
\]
with high probability if and only if
\[
p\,n^{1/m_2(F)}\longrightarrow\infty.
\tag{11}
\]

### Sufficiency

The established sparse random Turán theorem states that, for fixed \(F\) and every \(\varepsilon>0\), there is \(C=C(F,\varepsilon)\) such that
\[
p\ge Cn^{-1/m_2(F)}
\]
implies, with high probability,
\[
\operatorname{ex}(G(n,p),F)
 \le \left(1-\frac1{r-1}+\varepsilon\right)e(G(n,p)).
\]
This is the standard theorem proved independently in the sparse random extremal framework of Conlon–Gowers and Schacht. Condition (11), followed by a diagonal argument in \(\varepsilon\), gives the upper bound in (10). The lower bound is obtained by keeping all edges across a fixed balanced \((r-1)\)-partition.

### Necessity

Suppose (11) fails. Pass to a subsequence on which
\[
p\,n^{1/m_2(F)}\le C.
\tag{12}
\]
Write \(v=v(F)\), \(e=e(F)\), \(\pi=1-1/(r-1)\), and \(\mu=pN\).

Call a present edge \(xy\) **safe** if no copy of \(F\) in \(G(n,p)\) contains \(xy\). Let \(S\) be the number of safe edges.

Condition on \(xy\in E(G)\). There are at most \(2e\,n^{v-2}\) labelled embeddings of \(F\) using \(xy\) as one of their edges. For each such embedding, all of its other \(e-1\) edges are present with probability \(p^{e-1}\). The events that a particular embedding is not completed are decreasing events, so Harris's inequality gives
\[
\mathbb P(xy\text{ is safe}\mid xy\in E(G))
 \ge (1-p^{e-1})^{2e n^{v-2}}.
\tag{13}
\]
Because \(F\) is 2-balanced,
\[
\frac1{m_2(F)}=\frac{v-2}{e-1}.
\]
Consequently, (12) implies
\[
n^{v-2}p^{e-1}=O_{F,C}(1).
\]
It follows from (13) that, for some constant \(\delta=\delta(F,C)>0\),
\[
\mathbb ES\ge\delta\mu.
\tag{14}
\]

Suppose first that \(\mu\to\infty\). Since \(S\le e(G)\),
\[
\mathbb ES^2\le \mu^2+\mu,
\]
and Paley–Zygmund applied to (14) yields
\[
\mathbb P\left(S\ge\frac{\delta\mu}{2}\right)
 \ge \frac{\delta^2}{4}+o(1).
\tag{15}
\]

Now colour the vertices independently with \(r-1\) colours and form a subgraph \(H\) consisting of

- every edge joining different colours, and
- every safe edge joining equal colours.

This graph is \(F\)-free. Indeed, any copy of \(F\), being \(r\)-chromatic, must contain a monochromatic edge; such an edge would be safe, contradicting its membership in that copy of \(F\) in the ambient graph.

Averaging over the colourings gives some \(F\)-free \(H\) with
\[
e(H)\ge \pi e(G)+(1-\pi)S.
\tag{16}
\]
By (15), (16), and \(e(G)=(1+o(1))\mu\), with probability bounded away from zero,
\[
\operatorname{ex}(G(n,p),F)
 \ge \left(\pi+\frac{(1-\pi)\delta}{3}\right)\mu.
\]
Hence (10) cannot hold with high probability.

If \(\mu\) is bounded, then \(p=O(n^{-2})\), and \(G(n,p)\) is a matching with high probability. Since \(\chi(F)\ge3\), the graph is \(F\)-free, and the same binomial argument again rules out convergence to \(\pi\). This proves necessity. \(\square\)

### Clique case

For \(F=K_r\),
\[
m_2(K_r)=\frac{r+1}{2}.
\]
Thus
\[
\operatorname{ex}(G(n,p),K_r)
 =\left(1-\frac1{r-1}+o(1)\right)pN
\]
holds exactly when
\[
p\,n^{2/(r+1)}\longrightarrow\infty.
\]

---

## 5. Two general obstruction tests

These elementary tests may be useful in any eventual property-specific characterization.

### 5.1 Monotone obstruction

Let \(F\) be fixed with \(v\) vertices, \(e\) edges and \(\chi(F)\ge3\). If \(pN\to\infty\) and
\[
n^{v-2}p^{e-1}\longrightarrow0,
\tag{17}
\]
then
\[
\operatorname{ex}(G(n,p),F)=(1-o(1))pN.
\]

Indeed, the expected number \(X_F\) of copies of \(F\) is
\[
\mathbb EX_F=O(n^vp^e)=o(pn^2).
\]
Delete one edge from each copy. At most \(X_F=o_{\mathbb P}(pN)\) edges are removed, and the resulting graph is \(F\)-free. Thus the Turán-density conclusion of Theorem 1.1 fails in the range (17).

### 5.2 Principal induced obstruction

For a fixed graph \(F\), let
\[
\mathcal I(F):=\{H:H\text{ has no induced copy of }F\}.
\]
If
\[
n^{v(F)}p^{e(F)}(1-p)^{\binom{v(F)}2-e(F)}
 \longrightarrow0,
\tag{18}
\]
then \(G(n,p)\in\mathcal I(F)\) with high probability. Consequently,
\[
\operatorname{ex}_{\mathcal I(F)}(G(n,p))=e(G(n,p)).
\]
Whenever \(\chi(F)\ge3\) and \(pN\to\infty\), this contradicts the predicted coefficient \(1-1/(\chi(F)-1)<1\).

---

## 6. What remains open

The results above do not characterize the range for an arbitrary prescribed hereditary property. They show, in particular, that the answer cannot depend only on \(k(\mathcal P)\):

- For the property of being bipartite, Theorem 3.1 gives the sharp condition \(np\to\infty\).
- For the property of being triangle-free, Theorem 4.1 gives the sharp condition \(pn^{1/2}\to\infty\).

Both properties have \(k=3\). For example, at \(p=n^{-3/4}\), the theorem holds for maximum bipartite subgraphs but fails for maximum triangle-free subgraphs.

Likewise, monotone properties need no dense-end restriction on \(1-p\), while principal induced properties can fail as soon as particular nonedges become too rare. An arbitrary hereditary property may have infinitely many forbidden induced graphs, and different forbidden configurations may govern different \(p\)-windows. That genuinely property-dependent synthesis is not supplied here.
