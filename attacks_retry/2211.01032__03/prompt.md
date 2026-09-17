Attack the following open graph-theory problem.

Catalog id: 2211.01032__03
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2211.01032__03/
Source paper: Random Embeddings of Graphs: The Expected Number of Faces in Most Graph… (arXiv:2211.01032)

=== Catalog page (statement + literature review) ===
Non-orientable random embedding faces of Kₙ — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 9.5 from arXiv:2211.01032 posits that the expected number of faces in a non-orientable random embedding of $K_n$ (defined via a random rotation system combined with a random signature assigning each edge a sign independently with probability $1/2$) is at most $\ln(n) + O(1)$. This is the non-orientable analogue of the paper's main theorem for orientable embeddings. The conjecture is supported only by computer simulations reported by the authors; no subsequent work resolving or making partial progress on it has been found in the literature. The conjecture first appeared in the April 2025 (v3) version of the paper, so it is very recent.

 Reviewer notes. No follow-up found. The conjecture was introduced in the v3 (April 2025) of the paper, making it at most one year old at review time. All web searches returned only the source paper and its orientable predecessors; no citing paper addressing the non-orientable case was found.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. The expected number of faces in a non-orientable random embedding of the complete graph $K_{n}$ is at most $\ln(n) + O(1)$.

Context

The authors extend their investigation to non-orientable surfaces, where a random embedding is defined by choosing a random rotation system together with a random signature assigning each edge a sign independently with probability $1/2$. Computer simulations support a logarithmic behaviour analogous to the orientable case.

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
The problem above was already attacked by `gpt-5.6-sol`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but vertex-simple faces contribute exactly one quarter of a logarithm and all faces of length at most any fixed multiple of n contribute at most one half of a logarithm.",
  "would_publish": false,
  "caveats": "Faces of length greater than a fixed fraction of n remain uncontrolled."
}
```

## 1. Statement of the partial results

Let \(F_n\) be the number of faces in the random non-orientable embedding of \(K_n\). Face length is counted in edge-sides, so the sum of all face lengths is \(n(n-1)\).

Write \(F_{n,k}\) for the number of faces of length \(k\), and let \(S_{n,k}\) count those length-\(k\) faces whose projected boundary visits \(k\) distinct vertices.

I prove the following.

### Theorem

1. For \(3\le k\le n\),
   \[
   \mathbb E S_{n,k}
   =\frac{(n)_k}{2k(n-2)^k},
   \]
   where \((n)_k=n(n-1)\cdots(n-k+1)\).

2. Consequently,
   \[
   \sum_{k=3}^n \mathbb E S_{n,k}
   =\frac14\ln n+O(1),
   \]
   and hence
   \[
   \boxed{\mathbb E F_n\ge \frac14\ln n-O(1).}
   \]

3. For every fixed \(0<\alpha<1\),
   \[
   \boxed{\mathbb E\!\left[\sum_{k\le \alpha n}F_{n,k}\right]
   \le \frac12\ln n+O_\alpha(1).}
   \]

4. More precisely, for every fixed \(c>0\),
   \[
   \boxed{\mathbb E\!\left[\sum_{k\le c\sqrt n}F_{n,k}\right]
   =\frac14\ln n+O_c(1).}
   \]
   Thus, up to length \(O(\sqrt n)\), all but \(O(1)\) expected faces are vertex-simple.

These statements do not control faces longer than \(\alpha n\), so they do not prove the conjectured global upper bound.

---

## 2. A matching model for the random embedding

Put \(d=n-1\). At each incidence \((v,e)\), introduce two side-flags. Thus vertex \(v\) has \(2d\) flags.

There are three relevant matchings.

- \(J_v\) pairs the two flags belonging to the same incidence at \(v\).
- The boundary arcs of the vertex disc define another matching \(V_v\) on the \(2d\) flags at \(v\).
- The two sides of every edge-band define an edge matching \(A\) between flags at opposite endpoints.

The union \(A\cup \bigcup_v V_v\) is 2-regular, and its connected components are exactly the facial boundary components.

The signatures can be absorbed into random endpoint flips. More explicitly, choose independent bits \(b_{v,e}\), and define the signature of \(e=uv\) as
\[
\varepsilon_e=b_{u,e}+b_{v,e}\pmod 2.
\]
These signatures are independent and uniform. Relabelling the two flags at incidence \((v,e)\) according to \(b_{v,e}\) makes every edge matching canonical. After this relabelling, the matchings \(V_v\) are independent and uniform in the following family:
\[
\mathcal H_d=\{V:\ J_v\cup V\text{ is one }2d\text{-cycle}\}.
\]

A direct cyclic-order count gives
\[
|\mathcal H_d|=h_d=2^{d-1}(d-1)!.
\]

In this representation, \(A\) has exactly two matching edges between every pair of distinct vertex-blocks.

---

## 3. Local completion probability

Suppose \(Q\) is a prescribed matching of \(r\) pairs of flags at a vertex, where \(J_v\cup Q\) contains no cycle. Then \(J_v\cup Q\) consists of \(d-r\) alternating paths. Contracting these paths shows that the number of elements of \(\mathcal H_d\) containing \(Q\) is \(h_{d-r}\). Therefore, for \(0\le r\le d-1\),
\[
\Pr(Q\subseteq V_v)
=\frac{h_{d-r}}{h_d}
=\frac{1}{2^r(d-1)_r},
\tag{3.1}
\]
where
\[
(a)_r=a(a-1)\cdots(a-r+1).
\]

If \(J_v\cup Q\) already contains a proper cycle, the probability is zero. Thus (3.1) is also a valid upper bound for arbitrary prescribed \(Q\).

---

## 4. Exact enumeration of vertex-simple faces

Fix an undirected simple \(k\)-cycle \(C\) in \(K_n\). It has \(2^k\) choices of edge-sides, one for each edge of \(C\). For any such choice, exactly one local pair must be present in \(V_v\) at each vertex of \(C\).

By (3.1), the probability that all \(k\) required local pairs occur is
\[
\left(\frac1{2(d-1)}\right)^k
=\left(\frac1{2(n-2)}\right)^k.
\]

The number of undirected simple \(k\)-cycles in \(K_n\) is
\[
\frac{(n)_k}{2k}.
\]
Consequently,
\[
\mathbb E S_{n,k}
=\frac{(n)_k}{2k}\,2^k
  \left(\frac1{2(n-2)}\right)^k
=\frac{(n)_k}{2k(n-2)^k}.
\tag{4.1}
\]

Set
\[
R_{n,k}=\frac{(n)_k}{(n-2)^k}.
\]
For \(k=O(\sqrt n)\),
\[
\log R_{n,k}
=\sum_{j=0}^{k-1}
 \left(\log\left(1-\frac jn\right)
       -\log\left(1-\frac2n\right)\right)
=-\frac{k^2}{2n}+O\!\left(\frac{k}{n}+\frac{k^3}{n^2}\right).
\tag{4.2}
\]
Hence
\[
\sum_{k\le c\sqrt n}\frac{R_{n,k}}{2k}
=\frac12\sum_{k\le c\sqrt n}\frac{e^{-k^2/(2n)}}{k}+O_c(1)
=\frac14\ln n+O_c(1).
\tag{4.3}
\]

For \(k\ge 10\) and \(k\le n/2\), elementary logarithmic estimates give
\[
R_{n,k}\le C e^{-c k^2/n}.
\]
For \(k>n/2\), it is already exponentially small in \(n\). Thus the tail beyond \(c\sqrt n\) is \(O_c(1)\), and
\[
\sum_{k=3}^n\mathbb E S_{n,k}
=\frac14\ln n+O(1).
\]

This proves the lower bound in the theorem.

---

## 5. Counting all short potential faces

Fix integers \(r_1,\dots,r_n\ge0\) with
\[
r_1+\cdots+r_n=k.
\]
Here \(r_v\) is the number of vertex-matching edges used by a potential face at \(v\).

Let \(N(r_1,\dots,r_n)\) denote the number of possible alternating cycles using \(r_v\) local pairs at \(v\). I claim
\[
N(r_1,\dots,r_n)
\le
\frac{2^{k-1}(k-1)!}{\prod_v r_v!}.
\tag{5.1}
\]

To see this, replace the selected flags at \(v\) by \(2r_v\) labelled abstract stubs.

- There are \((2r_v-1)!!\) ways to pair the stubs locally.
- For any fixed local matching on all \(2k\) stubs, the number of second perfect matchings whose union with it is one alternating \(2k\)-cycle is
  \[
  2^{k-1}(k-1)!.
  \]
- An abstract matching edge between two vertex-blocks has at most two available channels in the actual graph. The number of channel assignments is at most \(2^k\).
- Every actual candidate has \(\prod_v(2r_v)!\) labellings by the abstract stubs.

Therefore
\[
N(r_1,\dots,r_n)
\le
\frac{
2^k\,2^{k-1}(k-1)!\prod_v(2r_v-1)!!
}{
\prod_v(2r_v)!
}.
\]
Using
\[
\frac{(2r-1)!!}{(2r)!}=\frac1{2^r r!}
\]
and \(\sum_vr_v=k\) gives (5.1).

If \(k<d\), then every \(r_v\le d-1\), and (3.1), independence over vertices, and (5.1) yield
\[
\mathbb E F_{n,k}
\le
\frac{(k-1)!}{2}
\sum_{\substack{r_1+\cdots+r_n=k\\r_i\ge0}}
\prod_{i=1}^n
\frac1{r_i!(n-2)_{r_i}}.
\tag{5.2}
\]

Define
\[
U_{n,k}
=
k!\sum_{r_1+\cdots+r_n=k}
\prod_{i=1}^n
\frac1{r_i!(n-2)_{r_i}}.
\]
Then
\[
\mathbb E F_{n,k}\le \frac{U_{n,k}}{2k}.
\tag{5.3}
\]

---

## 6. Bounding \(U_{n,k}\) for \(k\le\alpha n\)

Let \(a=n-2\), and let
\[
(R_1,\dots,R_n)\sim\operatorname{Multinomial}
 \left(k;\frac1n,\dots,\frac1n\right).
\]
Then
\[
U_{n,k}
=\left(\frac na\right)^k
\mathbb E\prod_{i=1}^n q_a(R_i),
\qquad
q_a(r)=\frac{a^r}{(a)_r}.
\tag{6.1}
\]

Fix \(\alpha<1\) and suppose \(k\le\alpha n\). Uniformly for \(r\le k\),
\[
\log q_a(r)
=\sum_{j=0}^{r-1}-\log\left(1-\frac ja\right)
\le \frac{C_\alpha}{n}\binom r2.
\tag{6.2}
\]
Put
\[
X=\sum_{i=1}^n\binom{R_i}{2}.
\]
This is the number of colliding pairs when \(k\) balls are independently placed into \(n\) boxes. Equation (6.2) gives
\[
\prod_iq_a(R_i)\le e^{tX},
\qquad t=\frac{C_\alpha}{n}.
\]

Place the balls sequentially. When ball \(i\) is placed, let \(Y_i\) be the number of previous balls in its chosen box, so \(X=\sum_iY_i\). Conditional on the current occupancies \(s_1,\dots,s_n\), convexity gives
\[
\frac1n\sum_{v=1}^n e^{t s_v}
\le
1+\frac{e^{t(i-1)}-1}{n}.
\]
Iterating,
\[
\mathbb E e^{tX}
\le
\exp\left(
 \frac1n\sum_{j=1}^{k-1}(e^{tj}-1)
\right)
\le
\exp\left(C_\alpha\frac{k^2}{n^2}\right).
\]
Together with (6.1),
\[
U_{n,k}
\le
\exp\left(
 C_\alpha\left(\frac kn+\frac{k^2}{n^2}\right)
\right).
\tag{6.3}
\]

Since the exponent is bounded for \(k\le\alpha n\),
\[
U_{n,k}-1
\le
C_\alpha\left(\frac kn+\frac{k^2}{n^2}\right).
\tag{6.4}
\]

Summing (5.3) and using (6.4),
\[
\begin{aligned}
\mathbb E\sum_{k\le\alpha n}F_{n,k}
&\le
\frac12\sum_{k\le\alpha n}\frac1k
+\frac12\sum_{k\le\alpha n}\frac{U_{n,k}-1}{k}\\
&\le
\frac12\ln n+O_\alpha(1).
\end{aligned}
\]
This proves the third assertion.

---

## 7. Faces of length \(O(\sqrt n)\)

For \(k\le c\sqrt n\), (6.3) gives
\[
U_{n,k}=1+O_c(k/n).
\]
On the other hand, (4.2) gives
\[
|R_{n,k}-1|
\le
O_c\left(\frac kn+\frac{k^2}{n}\right).
\]

Since the vertex-simple candidates are a subset of all candidates,
\[
0\le
\mathbb E(F_{n,k}-S_{n,k})
\le
\frac{U_{n,k}-R_{n,k}}{2k}.
\]
Therefore
\[
\sum_{k\le c\sqrt n}
\mathbb E(F_{n,k}-S_{n,k})
=O_c(1).
\]
Combining this with (4.3) gives
\[
\mathbb E\sum_{k\le c\sqrt n}F_{n,k}
=\frac14\ln n+O_c(1).
\]

---

## 8. Exact small cases

The matching model gives
\[
\mathbb E F_2=1,
\qquad
\mathbb E F_3=\frac32.
\]
For \(K_3\), the unique cycle is two-sided with probability \(1/2\), producing two faces, and one-sided with probability \(1/2\), producing one face.

There is also a short exact check for \(K_4\). Contract a spanning-tree star. The resulting bouquet has three loops. Its boundary count is
\[
F=1+\operatorname{null}_{\mathbb F_2}M,
\]
where the diagonal of \(M\) records the three residual twist bits and the off-diagonal entries record chord interlacements. For \(K_4\), the three off-diagonal entries are independent fair bits, each determined by the random order at one of the three non-root vertices. Thus \(M\) is a uniformly random symmetric \(3\times3\) matrix over \(\mathbb F_2\).

Among the \(64\) such matrices, the rank counts are
\[
28,\ 28,\ 7,\ 1
\]
for ranks \(3,2,1,0\), respectively. Hence
\[
\mathbb E F_4
=1+\frac{28+2\cdot7+3}{64}
=\frac{109}{64}.
\]

---

## 9. Remaining gap

The proof of the short-face bound uses \(k<d=n-1\), ensuring that no face exhausts all local transitions at a vertex. More importantly, the abstract-stub relaxation in (5.1) ignores the restriction that only two edge-sides are available between any fixed pair of vertices. This relaxation is harmless for \(k=O(n)\), but becomes exponentially loose for long, repeatedly visiting facial walks.

Thus the unresolved term is
\[
\mathbb E\!\left[\sum_{k>\alpha n}F_{n,k}\right].
\]
The conjecture would follow from, for example,
\[
\mathbb E\!\left[\sum_{k>\alpha n}F_{n,k}\right]
\le \frac12\ln n+O_\alpha(1)
\]
for one fixed \(\alpha<1\). The present argument gives only the deterministic \(O(n)\) bound for that range. Hence this is genuine partial progress, not a proof of the conjecture.
