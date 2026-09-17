Attack the following open graph-theory problem.

Catalog id: 2208.06630__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2208.06630__00/
Source paper: Short reachability networks (arXiv:2208.06630)

=== Catalog page (statement + literature review) ===
Minimum transpositions in t-reachable networks — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Problem 1 from arXiv:2208.06630 asks for the minimum number of transpositions in a t-reachable network, including the special case of star transpositions of the form (1,·). The paper (published in DMTCS, November 2025) settles the t=2 case exactly and gives an upper bound of (2+o_t(1))n transpositions for fixed t>=3, but the true asymptotics for large t remain open; a gap between upper and lower bounds also persists in the star-transposition setting. No follow-up paper resolving either variant was found in the indexed literature.

 Reviewer notes. The paper appeared in Discrete Mathematics & Theoretical Computer Science, vol. 27:3, Combinatorics (DOI: 10.46298/dmtcs.12454), published 4 November 2025. A companion manuscript 'Perfect shuffling with fewer lazy transpositions' by Groenland and Johnston is hosted on Alex Scott's webpage but its arXiv preprint status and exact bearing on Problem 1 could not be confirmed within the 5-call budget. The sole verified citing paper (arXiv:2210.13286, Janzer–Johnson–Leader 2022) concerns lazy random transpositions and uniform mixing, not the deterministic t-reachable network problem. No resolution of the open asymptotics for t>=3 or the star-transposition gap was found.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Problem. What is the minimum number of transpositions needed in a $t$-reachable network? What if all transpositions are of the form $(1,\cdot)$?

Context

The authors determine the exact minimum for $t=2$ (Theorem 2) and give an upper bound of $(2+o_t(1))n$ transpositions for fixed $t\geq 3$, but the asymptotics remain open for large $t$. Lower bounds for star-transposition $t$-reachable networks are also given, but a gap between upper and lower bounds remains even in that restricted setting.

Source paper

 Short reachability networks
 Carla Groenland, Tom Johnston, Jamie Radcliffe, Alex Scott · 2025-10-23
 https://arxiv.org/abs/2208.06630

=== Source paper abstract / header ===
Abstract:We investigate the following generalisation of permutation networks. We say a sequence $T=(T_1,\dots,T_\ell)$ of transpositions in $S_n$ forms a $t$-reachability network if, for every choice of $t$ distinct points $x_1, \dots, x_t\in \{1,\dots,n\}$, there is a subsequence of $T$ whose composition maps $j$ to $x_j$ for every $1\leq j\leq t$. When $t=n$, any permutation in $S_n$ can be created and $T$ is a permutation network. Waksman [JACM, 1968] showed that the shortest permutation networks have length about $n \log_2(n)$. In this paper, we investigate the shortest $t$-reachability networks for other values of $t$. Our main result settles the case of $t=2$: the shortest $2$-reachability network has length $\lceil 3n/2\rceil-2 $. For fixed $t \geq 3$, we give a simple randomised construction which shows that there exist $t$-reachability networks with $(2+o_t(1))n$ transpositions. We also study the effect of restricting to star-transpositions, i.e. restricting all transpositions to have the form $(1, \cdot)$.
 

 
 
 
 Comments:
 12 pages, 1 figure
 

 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2208.06630 [math.CO]
 

 
  
 (or 
 arXiv:2208.06630v3 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2208.06630
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Mathematics & Theoretical Computer Science, vol. 27:3, Combinatorics (November 4, 2025) dmtcs:12454
 

 
 
 Related DOI:
 
 https://doi.org/10.46298/dmtcs.12454

 
 
 
 
 Focus to learn more
 
 
 
 
 DOI(s) linking to related resources
 

 

 
 

 

 

 
 Submission history
 From: Tom Johnston [view email] 
 [v1]
 Sat, 13 Aug 2022 11:25:54 UTC (13 KB)

 [v2]
 Thu, 19 Oct 2023 15:07:43 UTC (14 KB)

 [v3]
 Thu, 23 Oct 2025 17:22:21 UTC (19 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Short reachability networks, by Carla Groenland and 3 other authors
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
 | 2022-08
 

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
  "one_line": "A high-girth core construction gives a quantified star-transposition upper bound of 2n+O_t(n^{1-1/(2t)} log n), and networks with t=n-c are within O_c(1) of full permutation networks.",
  "would_publish": false,
  "caveats": "The leading constant 2 construction likely overlaps the source paper; no matching fixed-t lower bound is proved."
}
```

# 1. Statement and notation

Let \(L_t(n)\) be the minimum length of a \(t\)-reachability network on \([n]\), and let \(L_t^\star(n)\) be the corresponding minimum when every transposition has the form \((1,x)\).

I prove the following partial results.

### Theorem 1: quantified star upper bound

For every fixed \(t\ge 2\),
\[
L_t^\star(n)
 \le 2n+O_t\!\left(n^{1-\frac1{2t}}\log n\right).
\]
Consequently,
\[
\limsup_{n\to\infty}\frac{L_t^\star(n)}n\le 2.
\]

Together with monotonicity and the exact \(t=2\) result quoted in the question,
\[
\left\lceil\frac{3n}{2}\right\rceil-2
 \le L_t(n)\le L_t^\star(n)
 \le 2n+O_t\!\left(n^{1-\frac1{2t}}\log n\right)
\]
for every fixed \(t\ge2\).

The main point is that the usual high-girth core construction can be converted to star transpositions without multiplying its leading term by \(3\).

### Theorem 2: the near-permutation regime

Let \(P(n)=L_n(n)\) be the minimum length of a full permutation network, and let \(P^\star(n)=L_n^\star(n)\). If \(c=n-t\), then
\[
P(n)-P(c)\le L_{n-c}(n)\le P(n),
\]
and
\[
P^\star(n)-3P(c)\le L_{n-c}^\star(n)\le P^\star(n).
\]

In particular,
\[
L_{n-1}(n)=P(n),\qquad
L_{n-1}^\star(n)=P^\star(n),
\]
and for each fixed \(c\), an \((n-c)\)-reachability network is within \(O_c(1)\) switches of a full permutation network.

Neither theorem determines the fixed-\(t\) leading constant.

---

# 2. A sparse high-girth core

We need a standard graph lemma, included for completeness.

### Lemma 3

For every fixed \(t\ge2\) and all sufficiently large \(m\), there is a simple graph \(H\) on \(m\) vertices with girth greater than \(t\) and
\[
e(H)=\Omega_t\!\left(m^{1+1/t}\right).
\]

#### Proof

Take \(G\sim G(m,p)\) with
\[
p=m^{-1+1/t}.
\]
Then
\[
\mathbb E e(G)=\binom m2p=\Theta\!\left(m^{1+1/t}\right).
\]

For \(3\le r\le t\), the expected number \(C_r\) of \(r\)-cycles satisfies
\[
\mathbb E C_r
 \le \frac{m^r p^r}{2r}
 =\frac{m^{r/t}}{2r}
 =O_t(m).
\]
Thus the expected total number of cycles of length at most \(t\) is \(O_t(m)\). For sufficiently large \(m\),
\[
\mathbb E\!\left(e(G)-\sum_{r=3}^t C_r\right)
 =\Omega_t\!\left(m^{1+1/t}\right).
\]
Hence some realization has that many more edges than short cycles. Delete one edge from each remaining cycle of length at most \(t\). Deletion creates no new cycles, so the resulting graph has girth greater than \(t\) and still has
\[
\Omega_t\!\left(m^{1+1/t}\right)
\]
edges. ∎

An important consequence is the following matching property.

### Lemma 4

If \(H\) is simple and has girth greater than \(t\), then every family of at most \(t\) edges of \(H\) has a system of distinct representatives from its endpoints.

#### Proof

Regard every edge \(e\) as the two-element set of its endpoints. For any nonempty subfamily \(F\) with \(|F|\le t\), the graph formed by \(F\) is acyclic: otherwise it contains a cycle of length at most \(|F|\le t\). Hence
\[
\left|\bigcup_{e\in F}e\right|\ge |F|+1\ge |F|.
\]
Hall's condition holds. ∎

---

# 3. The core construction for arbitrary transpositions

Fix \(t\ge2\), and put
\[
m=\left\lceil n^{\,1-\frac1{2t}}\right\rceil.
\]
For large \(n\), choose a core \(C\subseteq[n]\) of size \(m\), containing \([t]\).

By Lemma 3,
\[
m^{1+1/t}
 =n^{(1-\frac1{2t})(1+\frac1t)+o(1)}
 =n^{1+\frac{t-1}{2t^2}+o(1)}
 \gg n.
\]
Thus there is a simple graph \(H\) on \(C\), of girth greater than \(t\), with at least \(n-m\) edges. Associate distinct edges
\[
e_x=\{a_x,b_x\}\in E(H)
\]
with the vertices \(x\in[n]\setminus C\).

Let \(Q_C\) be a full permutation network on the \(m\) core points. Write its length as \(p(m)\); the standard recursive permutation-network construction gives
\[
p(m)=O(m\log m).
\]

Consider the following network:

1. one copy of \(Q_C\);
2. all attachment transpositions
   \[
   (a_x,x),\quad (b_x,x)
   \qquad (x\in[n]\setminus C);
   \]
3. a second copy of \(Q_C\).

The attachment switches may be placed in any fixed order.

### Lemma 5

This is a \(t\)-reachability network.

#### Proof

Let \(f:[t]\to[n]\) be an injection. Let
\[
X=f([t])\setminus C
\]
be the set of prescribed targets outside the core.

The family \(\{e_x:x\in X\}\) has size at most \(t\). By Lemma 4, choose distinct core vertices
\[
\mu(x)\in e_x,\qquad x\in X.
\]

Use the first core permutation network to place the token destined for \(x\) at \(\mu(x)\), for every \(x\in X\). The other active tokens may be put in arbitrary distinct unused core positions. This partial assignment extends to a permutation of \(C\), so the full core network realizes it.

For every \(x\in X\), select the attachment transposition
\[
(\mu(x),x).
\]
These selected transpositions are pairwise disjoint, since both the \(x\)'s and the \(\mu(x)\)'s are distinct. They therefore deposit the correct tokens at all targets in \(X\).

All remaining active tokens are still in the core. Use the second core permutation network to send them to their prescribed targets in \(C\). Again, the required partial assignment extends to a permutation of \(C\). ∎

Its length is
\[
2p(m)+2(n-m)
 =2n+O_t\!\left(n^{1-\frac1{2t}}\log n\right).
\]

---

# 4. Conversion to star transpositions without losing the leading term

Write
\[
s_z=(1,z).
\]
For \(a,b\ne1\),
\[
(a,b)=s_a s_b s_a.
\]
Replacing every arbitrary switch separately by three star switches would give a factor \(3\). For the attachment stage, however, switches sharing a core endpoint can be bundled.

### Lemma 6: bundle simulation

Suppose a consecutive block of switches is
\[
(c,x_1),(c,x_2),\ldots,(c,x_d),
\qquad c,x_i\ne1.
\]
Then every subproduct of this block is realizable as a subproduct of the star word
\[
s_c,s_{x_1},s_{x_2},\ldots,s_{x_d},s_c.
\]

#### Proof

If no switch is selected, select nothing. If the selected indices are
\[
i_1<i_2<\cdots<i_k,
\]
select the first and last \(s_c\), together with
\[
s_{x_{i_1}},\ldots,s_{x_{i_k}}.
\]
Indeed, writing each selected \((c,x_i)\) as \(s_c s_{x_i}s_c\), all adjacent pairs \(s_cs_c\) cancel. The resulting product is exactly
\[
s_c s_{x_{i_1}}\cdots s_{x_{i_k}}s_c.
\]
∎

Group the attachment switches according to their core endpoint \(c\). For \(c\ne1\), replace the block
\[
(c,x_1),\ldots,(c,x_{d_c})
\]
by
\[
s_c,s_{x_1},\ldots,s_{x_{d_c}},s_c.
\]
For \(c=1\), the attachment switches are already star transpositions.

Since
\[
\sum_{c\in C}d_c=2(n-m),
\]
the star attachment word has length at most
\[
2(n-m)+2m\le2n.
\]

For each of the two core permutation networks, replace every switch not incident with \(1\) by its three-star simulation. Thus each core copy has star length at most \(3p(m)\). The complete star word has length at most
\[
2n+6p(m)
 =2n+O_t\!\left(n^{1-\frac1{2t}}\log n\right).
\]
Because every selected switch in the arbitrary-transposition construction is simulated exactly, Lemma 5 remains valid. This proves Theorem 1.

---

# 5. Why this construction does not yield a constant below \(2\)

The coefficient \(2\) is intrinsic to this particular one-core matching architecture.

Suppose \(q\) outside vertices have nonempty neighborhoods \(N(x)\subseteq C\), and routing any two outside targets is required to proceed by matching them to distinct core ports. Two different outside vertices cannot both have the same singleton neighborhood \(\{c\}\). Hence at most \(|C|\) outside vertices have degree one, and therefore
\[
\sum_x |N(x)|
 \ge 2q-|C|.
\]
If \(|C|=o(n)\) and \(q=n-o(n)\), the attachment stage necessarily has \(2n-o(n)\) incidences.

Thus beating \(2n\) requires a genuinely multistage temporal construction, not merely a sparser version of this high-girth core argument.

---

# 6. Networks with \(t\) close to \(n\)

We now prove Theorem 2.

Let \(t=n-c\), and let \(T\) be a \(t\)-reachability network of length \(L_t(n)\). Let \(U\) be a full permutation network on
\[
A=\{t+1,\ldots,n\},
\]
of length \(P(c)\).

Place \(U\) before \(T\). Given any \(\pi\in S_n\), use \(t\)-reachability to choose a subproduct \(\sigma\) of \(T\) satisfying
\[
\sigma(j)=\pi(j)\qquad(1\le j\le t).
\]
Then
\[
h=\sigma^{-1}\pi
\]
fixes every point of \([t]\), and hence \(h\) is a permutation of \(A\). Select a subword of \(U\) realizing \(h\). Applying \(h\) first and then \(\sigma\) realizes
\[
\sigma h=\pi.
\]
Therefore \(U,T\) is a full permutation network, and
\[
P(n)\le P(c)+L_t(n).
\]
The reverse inequality \(L_t(n)\le P(n)\) is immediate, proving
\[
P(n)-P(c)\le L_{n-c}(n)\le P(n).
\]

For the star version, simulate each switch of \(U\) by three star transpositions. This gives a star word of length at most \(3P(c)\) realizing every permutation of \(A\) while fixing \([t]\) in its total product. The same argument gives
\[
P^\star(n)-3P(c)\le L_{n-c}^\star(n)\le P^\star(n).
\]

For \(c=1\), \(P(1)=0\), so
\[
L_{n-1}(n)=P(n),\qquad
L_{n-1}^\star(n)=P^\star(n).
\]
This also follows directly: the images of the first \(n-1\) points determine the image of the last point.

---

# 7. General lower bounds and exact verification

Two elementary lower bounds apply to both variants.

First, a \(t\)-reachable network with \(t\ge2\) is also \(2\)-reachable: any prescribed pair of targets can be extended to an injective \(t\)-tuple. Hence the theorem quoted in the question gives
\[
L_t(n),L_t^\star(n)
 \ge \left\lceil\frac{3n}{2}\right\rceil-2.
\]

Second, a word of length \(\ell\) has at most \(2^\ell\) subwords, while there are
\[
(n)_t=n(n-1)\cdots(n-t+1)
\]
target injections. Therefore
\[
L_t(n),L_t^\star(n)
 \ge \left\lceil\log_2 (n)_t\right\rceil.
\]

For exact small-case verification, one can use the following recurrence. Let \(R_0=\{(1,\ldots,t)\}\), and for a word
\[
T=(\tau_1,\ldots,\tau_\ell)
\]
define
\[
R_i=R_{i-1}\cup
 \left\{(\tau_i(x_1),\ldots,\tau_i(x_t)):
       (x_1,\ldots,x_t)\in R_{i-1}\right\}.
\]
Induction on \(i\) shows that \(R_i\) is exactly the set of restrictions obtainable from subwords of the first \(i\) switches. Thus \(T\) is \(t\)-reachable exactly when
\[
|R_\ell|=(n)_t.
\]
Breadth-first search on these reachable-state sets, using all \(\binom n2\) transpositions or only the \(n-1\) star transpositions, returns the exact minimum for small \(n,t\).

---

# 8. Remaining gap

For fixed \(t\ge3\), the argument establishes only
\[
\frac32
 \le \liminf_{n\to\infty}\frac{L_t(n)}n
 \le \limsup_{n\to\infty}\frac{L_t^\star(n)}n
 \le2.
\]
No lower bound approaching \(2n\), and no construction below \(2n-o(n)\), is obtained here. The near-permutation result concerns the different regime \(n-t=O(1)\).

The high-girth core argument is close enough to the advertised randomized upper bound that it may already be implicit or explicit in the source paper; I have not verified the full 2025 text. The quantified error term and bundle simulation are therefore presented as rigorous partial deductions, not as a claim of literature novelty.
