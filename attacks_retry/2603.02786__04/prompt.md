Attack the following open graph-theory problem.

Catalog id: 2603.02786__04
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2603.02786__04/
Source paper: Packing arithmetic progressions (arXiv:2603.02786)

=== Extracted statement (catalog JSON) ===
Title: Conjecture 7
For every fixed $n$ and $k$ tending to infinity, we have $M_{k}(n)=(1+o(1))nk$.

Context:
Concerns packing of $k$ arithmetic progressions of the form $B_d=\{d,2d,\ldots,nd\}$ for $d=1,2,\ldots,k$ with $n$ fixed. The authors suspect the trivial lower bound of $nk$ is asymptotically correct as $k\to\infty$.

=== Catalog page (statement + literature review) ===
Trivial lower bound tight for AP packing — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 Conjecture 7 of arXiv:2603.02786 asserts that for fixed n and k tending to infinity, the minimum interval length M_k(n) needed to pack the arithmetic progressions B_d = {d, 2d, ..., nd} for d = 1, ..., k satisfies M_k(n) = (1+o(1))nk, i.e., the trivial lower bound nk is asymptotically tight. The paper itself establishes Theorem 3, which proves M_k(n) < 3nk for sufficiently large k (beyond a threshold k_0(n)), confirming the right order of magnitude but with a constant factor of 3 instead of 1. No follow-up papers resolving the conjecture were found in the literature, consistent with the paper's very recent publication date of March 2026.

 Reviewer notes. No follow-up papers found. The paper is very recent (March 2026). The authors' own Theorem 3 provides a partial result: M_k(n) < 3nk for k > k_0(n), which establishes the correct order but leaves the asymptotic constant open. Conjecture 7 predicts the constant is 1.

 
 Auto-reviewed 2026-05-14 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. For every fixed $n$ and $k$ tending to infinity, we have $M_{k}(n)=(1+o(1))nk$.

Context

Concerns packing of $k$ arithmetic progressions of the form $B_d=\{d,2d,\ldots,nd\}$ for $d=1,2,\ldots,k$ with $n$ fixed. The authors suspect the trivial lower bound of $nk$ is asymptotically correct as $k\to\infty$.

Source paper

 Packing arithmetic progressions
 Noga Alon, Michał Dębski, Jarosław Grytczuk, Jakub Przybyło · 2026-03-03
 https://arxiv.org/abs/2603.02786

=== Source paper abstract / header ===
Abstract:Let $\mathcal{F}=\{A_1,A_2,\ldots,A_k\}$ be a collection of finite arithmetic progressions, where each $A_d$ is an initial segment of the set $D_d=\{d,2d,3d,\ldots\}$ of consecutive multiples of a positive integer $d$. Let $m(\mathcal{F})$ denote the minimum length of an interval containing pairwise disjoint \emph{shifted} copies of all members of the family $\mathcal{F}$.
We study this parameter in the following two cases: for a fixed positive integer $n$, (1) each progression in $\mathcal{F}$ has the form $A_d=D_d\cap\{1,2,\ldots,n\}$, and (2) all progressions $A_d$ of $\mathcal{F}$ have the same size $n$, that is, $A_d=D_d\cap \{1,2,\ldots, nd\}$. We in particular derive the following asymptotic estimates. In case (1), when $k=n$, we get $m(\mathcal{F})=\Theta(n^{3/2}/\ln n)$. In case (2), when $k=n$, we get $m(\mathcal{F})=\Theta(n^3/\ln n)$, while if $k>k_0(n)$, then $m(\mathcal{F}) < 3kn$. In both cases we additionally determine $m(\mathcal{F})$ asymptotically or settle its order of magnitude for all $k<n$.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO)
 

 Cite as:
 arXiv:2603.02786 [math.CO]
 

 
  
 (or 
 arXiv:2603.02786v1 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2603.02786
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Jarosław Grytczuk [view email] 
 [v1]
 Tue, 3 Mar 2026 09:25:43 UTC (18 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Packing arithmetic progressions, by Noga Alon and 3 other authors
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
 | 2026-03
 

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
  "one_line": "The conjecture is proved for n at most 2, and a hypergraph edge-colouring argument gives explicit general bounds with normalized constant tending to 4/e, substantially improving the quoted factor 3.",
  "would_publish": false,
  "caveats": "The asymptotic constant 1 remains open for n at least 3, and novelty relative to the full source paper has not been independently checked."
}
```

# 1. Formulation and partial result

Write a shifted copy of \(B_d\) as
\[
A(d,a)=\{a,a+d,\ldots,a+(n-1)d\}.
\]
Thus \(M_k(n)\) is the least \(m\) for which one can choose \(a_1,\ldots,a_k\) such that all \(A(d,a_d)\subseteq [m]\) are pairwise disjoint.

The trivial lower bound is
\[
M_k(n)\ge nk.
\]

I prove the following partial result.

## Theorem

1. \(M_k(1)=k\).

2. For every \(k\),
   \[
   2k\le M_k(2)\le 2k+1.
   \]
   Hence Conjecture 7 holds for \(n=2\).

3. For \(n=3\),
   \[
   \limsup_{k\to\infty}\frac{M_k(3)}{k}
   \le \frac{2}{1-e^{-2/3}}
   =4.110\ldots,
   \]
   or equivalently
   \[
   \limsup_{k\to\infty}\frac{M_k(3)}{3k}
   \le 1.3701\ldots.
   \]

4. For every \(n\ge4\), let \(\lambda_n\in(1,2)\) be the unique solution of
   \[
   \log\frac4{\lambda_n}
   +\frac1{n-1}\log\frac{\lambda_n}{\lambda_n-1}=1.
   \tag{1}
   \]
   Then
   \[
   \limsup_{k\to\infty}\frac{M_k(n)}{k}
   \le (n-1)\lambda_n,
   \tag{2}
   \]
   and therefore
   \[
   \limsup_{k\to\infty}\frac{M_k(n)}{nk}
   \le \frac{n-1}{n}\lambda_n.
   \tag{3}
   \]
   Moreover,
   \[
   \frac{n-1}{n}\lambda_n\longrightarrow \frac4e
   =1.4715\ldots
   \qquad (n\to\infty).
   \]

For example, \(\lambda_4\approx1.8910\), giving
\[
M_k(4)\le (5.6731\ldots+o(1))k
       =(1.4183\ldots+o(1))\,4k.
\]

The result does not prove the conjectured constant \(1\), but it improves the quoted general upper bound \(3nk\).

# 2. A hypergraph rounding criterion

The main ingredient is the standard fixed-rank asymptotic edge-colouring theorem:

> **Asymptotic edge-colouring theorem.**  
> Let \(r\) be fixed. If an \(r\)-uniform hypergraph \(H\) has maximum degree \(\Delta\to\infty\) and maximum pair-codegree \(o(\Delta)\), then its edges can be partitioned into at most
> \[
> (1+o(1))\Delta
> \]
> matchings.

This is the usual Pippenger–Spencer nibble theorem in its maximum-degree form. The commonly stated almost-regular form suffices as well, by embedding \(H\) in an almost \(\Delta\)-regular \(r\)-graph on auxiliary vertices while keeping codegrees \(o(\Delta)\), and then restricting the resulting colouring to \(H\).

We use the following consequence.

## Proposition 1: uniform-translate rounding

Fix \(n\). Let \(m=O(k)\), and put
\[
L_d=m-(n-1)d,
\]
the number of admissible starts for difference \(d\). Suppose that, for some fixed \(\alpha,\delta>0\),

\[
L_d\ge \alpha k\qquad(1\le d\le k)
\tag{4}
\]
and
\[
\Lambda_{k,m}:=
\max_{x\in[m]}
\sum_{d=1}^k
\frac{r_d(x)}{L_d}
\le 1-\delta,
\tag{5}
\]
where
\[
r_d(x)=
\left|\left\{j\in\{0,\ldots,n-1\}:
1\le x-jd\le L_d\right\}\right|.
\]
Then, for all sufficiently large \(k\),
\[
M_k(n)\le m.
\]

### Proof

Choose a constant \(\rho>0\) sufficiently small and write
\[
\sigma=1-\rho
\]
so that
\[
\frac{1-\delta}{\sigma}<1.
\tag{6}
\]

Independently place every point of \([m]\) into a reservoir \(R\) with probability \(\rho\), and put \(W=[m]\setminus R\).

Set
\[
D_0=\left\lfloor\frac{\alpha k}{2}\right\rfloor.
\]
For every admissible labelled progression \(A(d,a)\), independently retain it with probability
\[
p_d=\frac{D_0}{L_d}\le \frac12.
\]
Form an \((n+1)\)-uniform hypergraph \(H\) whose vertices are:

- one formal label vertex for each \(d\in[k]\);
- the point vertices of \(W\);

and whose edges are the retained progressions wholly contained in \(W\), together with their label vertex.

For a label \(d\), its expected degree is
\[
L_dp_d\sigma^n=D_0\sigma^n.
\]
For a point \(x\in W\), conditional on \(x\in W\), its expected degree is
\[
\sigma^{n-1}\sum_{d=1}^k r_d(x)p_d
=
\sigma^{n-1}D_0
\sum_{d=1}^k\frac{r_d(x)}{L_d}.
\]
By (5), this is at most
\[
\sigma^{n-1}D_0(1-\delta)
=
D_0\sigma^n\frac{1-\delta}{\sigma}.
\tag{7}
\]

All relevant random sums have dependency graphs of bounded degree, depending only on \(n\):

- two translates of a fixed \(d\)-progression intersect only if their starts differ by \((i-j)d\);
- after conditioning on \(x\in W\), two candidate edges containing \(x\) are dependent only when they share another point.

Standard bounded-dependency concentration therefore gives, simultaneously for all labels and point vertices,
\[
\deg_H(d)=(1+o(1))D,\qquad D=D_0\sigma^n,
\tag{8}
\]
and, by (6) and (7),
\[
\deg_H(x)\le (1-\gamma)D
\tag{9}
\]
for some fixed \(\gamma>0\).

The pair-codegrees of \(H\) are bounded solely in terms of \(n\). Indeed:

- a label \(d\) and a point \(x\) lie together in at most \(n\) edges;
- if \(x\ne y\) are point vertices, then an edge containing both gives
  \[
  y-x=(j-i)d
  \]
  for some \(i\ne j\), and for each ordered pair \((i,j)\) there is at most one possible \(d\).

Thus
\[
\Delta_2(H)=O_n(1)=o(D).
\]

The asymptotic edge-colouring theorem partitions \(E(H)\) into
\[
(1+o(1))D
\]
matchings. Since
\[
|E(H)|=\sum_{d=1}^k\deg_H(d)=(1+o(1))kD,
\]
one colour class is a matching containing
\[
(1-o(1))k
\]
edges, necessarily with distinct labels. Denote the set of omitted labels by \(T\), where
\[
|T|=o(k).
\]

It remains to cover \(T\) inside the reservoir. For each \(d\), the number of admissible \(d\)-progressions wholly contained in \(R\) has expectation
\[
\rho^n L_d=\Theta(k).
\]
The same bounded-dependency concentration shows that, simultaneously for every \(d\),
\[
\#\{a:A(d,a)\subseteq R\}
\ge \frac12\rho^nL_d
\ge c k
\tag{10}
\]
for some fixed \(c>0\).

Now greedily pack the labels in \(T\) inside \(R\). A previously selected \(n\)-term progression can intersect at most \(n^2\) candidate translates for a fixed new difference \(d\): choose one of its \(n\) points and one of the \(n\) possible positions in the new progression. Hence fewer than
\[
n^2|T|=o(k)
\]
of the \(ck\) choices from (10) are forbidden. The greedy completion succeeds.

The matching in \(W\) and the completion in \(R\) are disjoint, proving \(M_k(n)\le m\). ∎

# 3. Evaluation of the criterion

## 3.1 The case \(n=3\)

Take \(m=\lceil ck\rceil\), where \(c>2\). Then
\[
L_d=m-2d.
\]
Since \(r_d(x)\le3\),
\[
\Lambda_{k,m}
\le 3\sum_{d=1}^k\frac1{m-2d}.
\]
As \(k\to\infty\),
\[
3\sum_{d=1}^k\frac1{m-2d}
\longrightarrow
3\int_0^1\frac{dt}{c-2t}
=
\frac32\log\frac{c}{c-2}.
\]
Thus Proposition 1 applies whenever
\[
\frac32\log\frac{c}{c-2}<1.
\]
This is equivalent to
\[
c>\frac{2}{1-e^{-2/3}}.
\]
Letting \(c\) decrease to this threshold proves the asserted \(n=3\) bound.

## 3.2 The case \(n\ge4\)

Put
\[
A=n-1,\qquad m=\lceil \lambda A k\rceil,
\]
where \(1<\lambda<2\).

For fixed \(d,x\), the admissible values of \(j\) satisfy
\[
jd\in[x-L_d,x-1],
\]
an interval of length at most \(L_d\). Therefore
\[
r_d(x)\le \min\left(n,\frac{L_d}{d}+1\right).
\tag{11}
\]

Split the sum at \(d=\lambda k/2\). For \(d\le\lambda k/2\), use \(r_d(x)\le n\). For larger \(d\), use the second bound in (11). Uniformly in \(x\),
\[
\Lambda_{k,m}
\le
\sum_{d\le\lambda k/2}\frac{n}{m-Ad}
+
\sum_{\lambda k/2<d\le k}
\left(\frac1d+\frac1{m-Ad}\right).
\]
Passing to Riemann integrals gives
\[
\begin{aligned}
\limsup_{k\to\infty}\Lambda_{k,m}
&\le
\int_0^{\lambda/2}
\frac{n\,dt}{A(\lambda-t)}
+
\int_{\lambda/2}^1
\left(\frac1t+\frac1{A(\lambda-t)}\right)dt\\
&=
\frac nA\log2
+\log\frac2\lambda
+\frac1A\log\frac{\lambda}{2(\lambda-1)}\\
&=
\log\frac4\lambda
+\frac1{n-1}\log\frac{\lambda}{\lambda-1}\\
&=:B_n(\lambda).
\end{aligned}
\tag{12}
\]

The function \(B_n\) is strictly decreasing on \((1,2)\),
\[
B_n(\lambda)\to\infty\quad(\lambda\downarrow1),
\]
and
\[
B_n(2)=\frac{n}{n-1}\log2<1
\qquad(n\ge4).
\]
Consequently there is a unique \(\lambda_n\in(1,2)\) satisfying (1), and Proposition 1 applies to every \(\lambda>\lambda_n\). Letting \(\lambda\downarrow\lambda_n\) proves (2) and (3).

Finally, from (1),
\[
\log\frac4{\lambda_n}
=
1-\frac1{n-1}\log\frac{\lambda_n}{\lambda_n-1}.
\]
The second term tends to zero as \(n\to\infty\), so
\[
\lambda_n\longrightarrow \frac4e.
\]
Since \((n-1)/n\to1\), the normalized constant also tends to \(4/e\).

# 4. An explicit packing for \(n=2\)

Let
\[
O=\left\lceil\frac k2\right\rceil,
\qquad
E=\left\lfloor\frac k2\right\rfloor.
\]

For every odd difference \(d=2r-1\), \(1\le r\le O\), take
\[
P_{2r-1}=\{O-r+1,\ O+r\}.
\]
Its difference is \(2r-1\), and these pairs use exactly the positions
\[
1,2,\ldots,2O.
\]

For every even difference \(d=2r\), \(1\le r\le E\), take
\[
P_{2r}
=
\{2O+E-r+1,\ 2O+E+r+1\}.
\]
Its difference is \(2r\). These pairs use
\[
\{2O+1,\ldots,2O+E\}
\cup
\{2O+E+2,\ldots,2O+2E+1\}.
\]
They are disjoint from all odd-difference pairs and from each other. The single unused point is
\[
2O+E+1.
\]
Since \(2O+2E+1=2k+1\), this gives
\[
M_k(2)\le2k+1.
\]
Together with \(M_k(2)\ge2k\), this proves
\[
M_k(2)=(1+o(1))\,2k.
\]

As a side observation, if a packing exists in exactly \([2k]\), then all positions are used. Orient every pair from its smaller to its larger endpoint. A parity calculation from
\[
\sum(\text{larger}-\text{smaller})=\frac{k(k+1)}2
\]
shows that exact length \(2k\) is impossible when \(k\equiv2,3\pmod4\). Thus the above \(2k+1\) construction is exact in those two congruence classes.

# 5. Remaining gap

The rounding argument is not the obstruction. More generally, suppose that for \(m=(n+\varepsilon)k\) one could find weights \(w_{d,a}\) satisfying

\[
\sum_a w_{d,a}=1
\quad\text{for every }d,
\]
\[
\max_{d,a}w_{d,a}=O(1/k),
\]
and
\[
\sum_{\substack{d,a\\x\in A(d,a)}}w_{d,a}
\le1-\eta
\quad\text{for every }x
\]
for some \(\eta=\eta(n,\varepsilon)>0\). The same reservoir and edge-colouring proof would round these fractional choices to a genuine packing.

Thus a plausible route to the conjecture is a suitably spread fractional packing of the admissible translates with almost uniform point load. The present argument uses only the uniform distribution over all starts for each \(d\); near \(m=nk\), those loads are not flat enough, so condition (5) fails. No construction of the required non-uniform fractional weights is supplied here. Consequently the constant \(1\) remains unproved for every \(n\ge3\).
