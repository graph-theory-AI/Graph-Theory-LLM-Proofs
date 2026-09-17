Attack the following open graph-theory problem.

Catalog id: 2004.12166__01
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2004.12166__01/
Source paper: An algorithmic weakening of the Erdős-Hajnal conjecture (arXiv:2004.12166)

=== Catalog page (statement + literature review) ===
MIS approximation exponent in H-free graphs — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The question of determining the largest ε > 0 such that MIS admits an O(n^{1-ε})-approximation in H-free graphs remains open for most choices of H. The source paper itself proved tight bounds for specific classes: a √OPT-approximation for C_4-free graphs (from local search applied to K_{t,t}-free), and matching upper and lower bounds for triangle-free and high-girth graphs (tight up to constants in the exponent c/γ). No subsequent paper has been found that resolves the meta-question of characterising the optimal exponent as a function of H in full generality.

 Reviewer notes. No follow-up paper directly addressing the optimal approximation exponent as a function of H was found. Related nearby work exists: (1) arXiv:2006.10444 (Bonnet, Giannopoulos, Kim, Rzążewski, Sikora, Algorithmica 2022) studies parameterised inapproximability of independent set in H-free graphs — this is FPT inapproximability rather than the polynomial-time exponent question and was not fetched to verify; (2) a STACS 2023 paper on approximating inapproximable problems on bounded-twin-width graphs was noted but not verified. The question is a fine-grained open problem within a line of work that remains very active.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. For a given $H$, what is the largest $\varepsilon > 0$ such that MIS admits an $O(n^{1-\varepsilon})$-approximation algorithm in $H$-free graphs?

Context

After establishing that many graphs $H$ satisfy the improved approximation property, the authors ask how to optimise the approximation ratio. They investigate this in Sections 3 and 4, proving e.g. a $\sqrt{OPT}$-approximation in $C_4$-free graphs and a tight inapproximability bound in triangle-free and high-girth graphs.

Notes. Posed as an open research direction in running prose in the 'Results and organization' section; partially investigated within the paper but not fully resolved.

Source paper

 An algorithmic weakening of the Erdős-Hajnal conjecture
 Édouard Bonnet, Stéphan Thomassé, Xuan Thang Tran, Rémi Watrigant · 2020-04-25
 https://arxiv.org/abs/2004.12166
 PDF source

=== Source paper abstract / header ===
Abstract:We study the approximability of the Maximum Independent Set (MIS) problem in $H$-free graphs (that is, graphs which do not admit $H$ as an induced subgraph). As one motivation we investigate the following conjecture: for every fixed graph $H$, there exists a constant $\delta > 0$ such that MIS can be $n^{1 - \delta}$-approximated in $H$-free graphs, where $n$ denotes the number of vertices of the input graph. We first prove that a constructive version of the celebrated Erdős-Hajnal conjecture implies ours. We then prove that the set of graphs $H$ satisfying our conjecture is closed under the so-called graph substitution. This, together with the known polynomial-time algorithms for MIS in $H$-free graphs (e.g. $P_6$-free and fork-free graphs), implies that our conjecture holds for many graphs $H$ for which the Erdős-Hajnal conjecture is still open. We then focus on improving the constant $\delta$ for some graph classes: we prove that the classical Local Search algorithm provides an $OPT^{1-\frac{1}{t}}$-approximation in $K_{t,t}$-free graphs (hence a $\sqrt{OPT}$-approximation in $C_4$-free graphs), and, while there is a simple $\sqrt{n}$-approximation in triangle-free graphs, it cannot be improved to $n^{\frac{1}{4}-\varepsilon}$ for any $\varepsilon > 0$ unless $NP \subseteq BPP$. More generally, we show that there is a constant $c$ such that MIS in graphs of girth $\gamma$ cannot be $n^{\frac{c}{\gamma}}$-approximated. Up to a constant factor in the exponent, this matches the ratio of a known approximation algorithm by Monien and Speckenmeyer, and by Murphy. To the best of our knowledge, this is the first strong (i.e., $\Omega(n^\delta)$ for some $\delta > 0$) inapproximability result for Maximum Independent Set in a proper hereditary class.
 

 
 
 
 Subjects:
 
 Data Structures and Algorithms (cs.DS); Computational Complexity (cs.CC); Discrete Mathematics (cs.DM)
 
 
 MSC classes:
 68Q25, 68Q17, 68R10
 

 
 ACM classes:
 F.2.2
 

 Cite as:
 arXiv:2004.12166 [cs.DS]
 

 
  
 (or 
 arXiv:2004.12166v1 [cs.DS] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2004.12166
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Édouard Bonnet [view email] 
 [v1]
 Sat, 25 Apr 2020 15:11:59 UTC (33 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled An algorithmic weakening of the Erd\H{o}s-Hajnal conjecture, by \'Edouard Bonnet and 3 other authors
View PDF
HTML (experimental)
TeX Source
 

 view license

 

 
 Current browse context:

 cs.DS

 

 < prev
 
   |   
 next >
 

 

 new
 | 
 recent
 | 2020-04
 

 Change to browse by:
 
 cs
 cs.CC
 cs.DM
 

 

 

 
 References & Citations

 
 NASA ADS
Google Scholar

 Semantic Scholar

 
 

 

 DBLP - CS Bibliography

 
 listing | bibtex 

 
Édouard Bonnet
Stéphan Thomassé
Rémi Watrigant 

 

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
  "one_line": "The full characterization remains open, but the exponent is invariant under adjoining isolated vertices to H, and induced-K_{s,t}-free graphs admit an O(OPT^{1-1/min(s,t)}) approximation, giving the exact value ε=1 for stars.",
  "would_publish": false,
  "caveats": "Optimality beyond stars is not shown; the quantitative extensions may be implicit in the source, and the upper bounds quoted below are conditional."
}
```

# Mathematical writeup

## 1. Precise formulation

The phrase “largest \(\varepsilon\)” should technically be replaced by a supremum: an \(O(\log n)\)-approximation, for example, would imply every \(\varepsilon<1\), but not necessarily \(\varepsilon=1\).

Fix deterministic polynomial time and, for a graph \(H\) with at least two vertices, define
\[
\mathcal E(H)=\left\{\varepsilon\in[0,1]:
 \begin{array}{l}
 \text{there is a constant }C_H\text{ and a polynomial-time algorithm}\\
 \text{returning an independent set }I\text{ with }
 \alpha(G)/|I|\le C_H n^{1-\varepsilon}\\
 \text{for every nonempty induced-}H\text{-free graph }G
 \end{array}
 \right\}.
\]
Set
\[
\varepsilon^*(H)=\sup\mathcal E(H).
\]

Restricting to \([0,1]\) loses nothing. For every \(H\) with at least two vertices, the class of \(H\)-free graphs contains arbitrarily large nonempty graphs: use complete graphs if \(H\) is not complete, and edgeless graphs if \(H\) is complete. Since every approximation ratio is at least one, no exponent \(\varepsilon>1\) is possible.

All lower bounds below are unconditional and deterministic.

---

## 2. Two quantitative operations on the forbidden graph

Write \(F\sqcup K_1\) for adding an isolated vertex to \(F\), and \(K_1\vee F\) for adding a universal vertex.

### Proposition 2.1: monotonicity

If \(F\) is an induced subgraph of \(H\), then
\[
\mathcal E(H)\subseteq \mathcal E(F),
\qquad\text{and hence}\qquad
\varepsilon^*(H)\le \varepsilon^*(F).
\]

Indeed, every \(F\)-free graph is \(H\)-free, so an algorithm for the broader \(H\)-free class applies to the \(F\)-free class.

### Proposition 2.2: isolated vertices do not change the exponent

For every nonempty \(F\),
\[
\boxed{\mathcal E(F\sqcup K_1)=\mathcal E(F)}
\]
and therefore
\[
\boxed{\varepsilon^*(F\sqcup K_1)=\varepsilon^*(F)}.
\]

#### Proof

One inclusion follows from Proposition 2.1, since \(F\) is an induced subgraph of \(F\sqcup K_1\).

For the converse, suppose MIS on \(F\)-free graphs has approximation factor
\[
C m^{1-\varepsilon}
\]
on \(m\)-vertex inputs. Let \(G\) be \((F\sqcup K_1)\)-free. For each \(v\in V(G)\), put
\[
A_v=V(G)\setminus N_G[v].
\]
Then \(G[A_v]\) is \(F\)-free: otherwise an induced copy of \(F\) in \(A_v\), together with \(v\), would induce \(F\sqcup K_1\).

Run the \(F\)-free approximation algorithm on every \(G[A_v]\), and add \(v\) to the independent set returned. Let \(O\) be a maximum independent set of \(G\), with \(|O|=\alpha\), and choose \(v\in O\). Then
\[
O\setminus\{v\}\subseteq A_v,
\]
so \(\alpha(G[A_v])\ge\alpha-1\). If \(\alpha\ge2\), the candidate corresponding to \(v\) has size at least
\[
\frac{\alpha-1}{C n^{1-\varepsilon}}
\ge
\frac{\alpha}{2C n^{1-\varepsilon}}.
\]
The case \(\alpha=1\) is immediate. Thus the resulting approximation factor is at most \(2C n^{1-\varepsilon}\). This proves the reverse inclusion. \(\square\)

Consequently, deleting all isolated vertices from \(H\) leaves \(\varepsilon^*(H)\) unchanged, unless \(H\) is itself edgeless. For \(H=I_t\), one has \(\alpha(G)<t\) on every \(H\)-free graph, so \(\varepsilon^*(I_t)=1\).

---

### Proposition 2.3: adding a universal vertex loses at most a factor two in \(\varepsilon\)

For every nonempty \(F\),
\[
\boxed{\frac12\varepsilon^*(F)\le
\varepsilon^*(K_1\vee F)\le\varepsilon^*(F)}.
\]

#### Proof of the lower bound

Suppose an \(m\)-vertex \(F\)-free graph can be approximated within
\[
C m^{1-\delta}.
\]
Let \(G\) be \((K_1\vee F)\)-free, let \(\alpha=\alpha(G)\), and compute a maximal independent set \(S\), of size \(s\). For every \(v\in S\), the graph \(G[N(v)]\) is \(F\)-free, so run the \(F\)-free algorithm on every such neighborhood. Return the largest set among \(S\) and all neighborhood solutions.

Let \(O\) be a maximum independent set. If \(s\ge\alpha/2\), then \(S\) is already a 2-approximation. Otherwise, maximality of \(S\) gives
\[
\sum_{v\in S}|O\cap N(v)|
   \ge |O\setminus S|
   \ge \alpha-s
   >\frac{\alpha}{2}.
\]
Hence some \(v\in S\) satisfies
\[
|O\cap N(v)|>\frac{\alpha}{2s}.
\]
The solution found in \(N(v)\) therefore has size at least
\[
\frac{\alpha}{2Cs\,n^{1-\delta}}.
\]
If \(M\) denotes the final output size, then
\[
M\ge
\max\left\{
s,\frac{\alpha}{2Cs\,n^{1-\delta}}
\right\}
\ge
\sqrt{\frac{\alpha}{2C n^{1-\delta}}}.
\]
Thus
\[
\frac{\alpha}{M}
 \le \sqrt{2C\alpha n^{1-\delta}}
 \le \sqrt{2C}\,n^{1-\delta/2}.
\]
Hence \(\delta/2\in\mathcal E(K_1\vee F)\).

The upper bound follows from monotonicity, since \(F\) is an induced subgraph of \(K_1\vee F\). \(\square\)

There is a stronger form useful below. Say that \(F\) has property \(P_\beta\) if some polynomial-time algorithm always returns an independent set of size at least
\[
c_F\alpha(G)^\beta
\]
on \(F\)-free graphs. Equivalently, it is an
\(O(\mathrm{OPT}^{\,1-\beta})\)-approximation.

If \(F\) has \(P_\beta\), then \(K_1\vee F\) has
\[
\boxed{P_{\beta/(1+\beta)}}.
\]
Indeed, in the preceding proof the two available solution sizes are
\[
s
\quad\text{and}\quad
c_F\left(\frac{\alpha}{2s}\right)^\beta.
\]
Their maximum is at least a constant times
\[
\alpha^{\beta/(1+\beta)}.
\]
Adding an isolated vertex preserves \(P_\beta\), by the proof of Proposition 2.2.

---

## 3. An asymmetric biclique extension of the local-search bound

The source proves an \(O(\mathrm{OPT}^{1-1/t})\)-approximation for induced-\(K_{t,t}\)-free graphs. The same argument admits the following asymmetric sharpening.

### Theorem 3.1

Let \(1\le s\le t\) be fixed. There is a deterministic polynomial-time algorithm for MIS on induced-\(K_{s,t}\)-free graphs with approximation factor
\[
\boxed{O_{s,t}\!\left(\mathrm{OPT}^{\,1-1/s}\right)}.
\]
In particular,
\[
\boxed{\varepsilon^*(K_{s,t})\ge\frac1s}.
\]

For \(s=1\), this is a constant-factor approximation.

### Algorithm

Start with \(S=\varnothing\). As long as there is an independent set
\[
X\subseteq V(G)\setminus S,\qquad 1\le |X|\le s,
\]
such that
\[
|N_G(X)\cap S|<|X|,
\]
replace
\[
S\leftarrow (S\setminus N_G(X))\cup X.
\]

Each move increases \(|S|\), so there are at most \(n\) moves. Since \(s\) is fixed, all candidate sets \(X\) can be enumerated in polynomial time.

### Analysis

Let \(O\) be a maximum independent set and put
\[
A=O\setminus S,\qquad
B=S\setminus O,\qquad
C=S\cap O,
\]
with \(a=|A|\), \(b=|B|\), \(c=|C|\).

Every vertex \(a\in A\) has a nonempty neighborhood in \(S\), since otherwise \(\{a\}\) would be an improving move. Moreover,
\[
N_S(a)\subseteq B,
\]
because \(O\) is independent and hence \(a\) has no neighbor in \(C\).

Partition \(A\) into vertices having fewer than \(s\) neighbors in \(B\), and those having at least \(s\).

#### Low-degree vertices

Fix \(D\subseteq B\) with \(|D|=d<s\). At most \(d\) vertices of \(A\) can have neighborhood in \(S\) exactly \(D\). Otherwise, choosing \(d+1\) such vertices gives an independent set \(X\) with
\[
|X|=d+1,\qquad N_S(X)=D,
\]
contradicting local optimality. Therefore the number of low-degree vertices is at most
\[
\sum_{d=1}^{s-1} d\binom bd.
\]

#### High-degree vertices

Count pairs
\[
(a,D),\qquad
a\in A,\quad D\in\binom{N_B(a)}s.
\]
Each high-degree \(a\) contributes at least one pair. On the other hand, a fixed \(s\)-set \(D\subseteq B\) has at most \(t-1\) common neighbors in \(A\). If it had \(t\), those \(s\) vertices of \(B\) and \(t\) vertices of \(A\) would induce \(K_{s,t}\), since both \(A\) and \(B\) are independent. Hence the number of high-degree vertices is at most
\[
(t-1)\binom bs.
\]

Combining the two estimates,
\[
a\le
\sum_{d=1}^{s-1}d\binom bd
 +(t-1)\binom bs.
\]
Writing \(x=|S|=b+c\), and using \(x\ge1\), gives
\[
\alpha(G)=a+c
 \le
\left(t+\frac{s(s-1)}2\right)x^s.
\]
Consequently
\[
|S|\ge
\left(t+\frac{s(s-1)}2\right)^{-1/s}
\alpha(G)^{1/s},
\]
and therefore
\[
\frac{\alpha(G)}{|S|}
 =
O_{s,t}\!\left(\alpha(G)^{1-1/s}\right).
\]
This proves the theorem. \(\square\)

### Tightness for this local-search analysis

For \(s\ge2\), let \(B\) be a set of \(b\) vertices. For every \(s\)-subset \(D\subseteq B\), introduce \(t-1\) independent vertices whose neighborhood is exactly \(D\); call the set of all these vertices \(A\). There are no edges inside \(A\) or \(B\).

This graph is induced-\(K_{s,t}\)-free: every \(s\)-subset of \(B\) has exactly \(t-1\) common neighbors in \(A\), while every vertex of \(A\) has degree \(s\). Moreover, \(B\) is an \(s\)-local optimum, since every nonempty \(X\subseteq A\) with \(|X|\le s\) satisfies
\[
|N(X)|\ge s\ge |X|.
\]
But
\[
|A|=(t-1)\binom bs=\Theta(b^s).
\]
Thus the estimate \(\alpha=O(|S|^s)\) is asymptotically tight for arbitrary \(s\)-local optima. This is not an inapproximability construction—the graph is bipartite and highly structured—but it shows that this local-search proof cannot yield a better exponent.

---

## 4. Consequences

### 4.1 Stars have exact exponent one

For every fixed \(t\ge1\),
\[
\boxed{\varepsilon^*(K_{1,t})=1}.
\]

Theorem 3.1 gives a constant-factor approximation. More directly, if \(S\) is any maximal independent set and \(O\) is optimum, assign every vertex of \(O\setminus S\) to a neighbor in \(S\setminus O\). Each \(s\in S\setminus O\) receives at most \(t-1\) vertices, since \(t\) independent neighbors together with \(s\) would induce \(K_{1,t}\). Hence
\[
|O|\le (t-1)|S|
\]
for \(t\ge2\). Since no exponent above one is possible, the value is exact.

By Proposition 2.2,
\[
\boxed{\varepsilon^*(K_{1,t}\sqcup I_r)=1}
\]
for every fixed \(r\).

### 4.2 Cones over bicliques

Starting with Theorem 3.1 and repeatedly using the strong universal-vertex reduction, if
\[
H=(K_k\vee K_{s,t})\sqcup I_r,
\qquad 1\le s\le t,
\]
then
\[
\boxed{\varepsilon^*(H)\ge\frac1{s+k}}.
\]
Indeed, if \(\beta_0=1/s\), then
\[
\beta_{j+1}=\frac{\beta_j}{1+\beta_j},
\qquad\text{so}\qquad
\frac1{\beta_{j+1}}=\frac1{\beta_j}+1.
\]

### 4.3 Cliques

Taking \(K_2=K_{1,1}\) as the base and adding \(q-2\) universal vertices yields
\[
\boxed{\varepsilon^*(K_q)\ge\frac1{q-1}}.
\]
Equivalently, the recursive algorithm gives an
\[
O\!\left(\mathrm{OPT}^{\,1-1/(q-1)}\right)
\]
approximation on \(K_q\)-free graphs.

In particular, for triangle-free graphs,
\[
\varepsilon^*(K_3)\ge\frac12.
\]

### 4.4 All forbidden graphs on at most three vertices

Apart from the degenerate \(H=K_1\), the only unresolved three-vertex case is \(K_3\):

- \(I_3\): \(\alpha(G)\le2\), so \(\varepsilon^*=1\);
- \(K_2\sqcup K_1\): isolated-vertex invariance from \(K_2\), so \(\varepsilon^*=1\);
- \(P_3=K_{1,2}\): star case, so \(\varepsilon^*=1\);
- \(K_3\): only the interval below is currently obtained.

---

## 5. Conditional upper bounds from the source paper

These use the hardness statements quoted in the prompt and are not reproved here.

### Triangle-free graphs

The source gives a \(\sqrt n\)-approximation and rules out an
\(n^{1/4-\eta}\)-approximation for every \(\eta>0\), unless
\(NP\subseteq BPP\). Translating into the present parameter gives
\[
\boxed{\frac12\le\varepsilon^*(K_3)\le\frac34}
\qquad\text{assuming }NP\nsubseteq BPP.
\]

Thus the statements quoted in the prompt do not determine the exact triangle exponent: the algorithmic exponent is \(1/2\), while the hardness only excludes exponents exceeding \(3/4\).

By monotonicity, under the same assumption,
\[
K_3\le_{\mathrm{ind}}H
\quad\Longrightarrow\quad
\varepsilon^*(H)\le\frac34.
\]

### Any cyclic forbidden graph

Let \(H\) contain a cycle and let \(h=|V(H)|\). A graph of girth
\(\gamma>h\) cannot contain \(H\), even as a non-induced subgraph, and is therefore \(H\)-free.

Taking the source's high-girth hardness theorem in the form quoted in the prompt—no \(n^{c/\gamma}\)-approximation for fixed \(\gamma\)—gives, for any admissible fixed \(\gamma>h\),
\[
\varepsilon^*(H)\le 1-\frac c\gamma
\]
under the complexity assumption attached to that theorem, up to its endpoint convention. In particular, that hardness rules out \(\varepsilon^*(H)=1\) for every cyclic \(H\).

---

## 6. Remaining gaps

This does not resolve the catalog problem.

1. Even \(H=K_3\) remains open: the bounds supplied by the source leave
   \[
   \frac12\le\varepsilon^*(K_3)\le\frac34.
   \]
2. For \(K_{s,t}\) with \(s\ge2\), the bound
   \(\varepsilon^*\ge1/s\) has no matching complexity lower bound here.
3. The isolated-vertex and universal-vertex reductions do not handle arbitrary substitutions or arbitrary forbidden graphs.
4. The supremum \(\varepsilon^*(H)\) need not a priori be attained.
5. I have not verified whether the asymmetric \(K_{s,t}\) formulation or the exact isolated-vertex invariance already appears implicitly in the source; the arguments above are self-contained but are not, by themselves, sufficient for a publishable resolution.
