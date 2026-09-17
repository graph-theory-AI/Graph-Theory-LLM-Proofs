Attack the following open graph-theory problem.

Catalog id: 2006.00534__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/2006.00534__00/
Source paper: Inverse problems for minimal complements and maximal supplements (arXiv:2006.00534)

=== Catalog page (statement + literature review) ===
Minimal complement count T(n) square-root growth — Graph-theory open problems (arXiv)

 
 Status
 open
 medium confidence
 

 No verified follow-up resolving Conjecture 7 was found. At the time of the paper, the known bounds were T(n) \geq n^{1/3}/\mathrm{polylog} (Theorem 1) and T(n) = O(n^{3/4+\varepsilon}) (Theorem 3), with the conjecture proposing the true growth rate is \widetilde{\Theta}(\sqrt{n}). Web searches returned related papers on minimal additive complements published in 2023 and 2025, but none could be verified via WebFetch to specifically address this conjecture. The conjecture appears to remain open as of May 2026.

 Reviewer notes. Searches returned related papers including 'On minimal additive complements' (Ramanujan Journal, 2025, doi:10.1007/s11139-025-01281-6) and 'Sets arising as minimal additive complements in the integers' (Journal of Number Theory, 2023), but WebFetch of the Ramanujan Journal page was blocked by authentication redirect and thus these papers could not be verified to address Conjecture 7 on T(n). Noah Kravitz's arXiv author page shows no additional follow-up paper co-authored on this topic. The gap between the n^{1/3} lower bound and n^{3/4+\varepsilon} upper bound remains unresolved in the verified literature.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Conjecture. We have that $T(n) = \widetilde{\Theta}(\sqrt{n})$. More generally, we have that $T(G) = \widetilde{\Theta}(\sqrt{|G|})$.

Context

The paper defines $\widetilde{\Theta}(g(n))$ to mean $f = \Omega(g(n)(\log n)^a)$ and $f(n) = O(g(n)(\log n)^b)$ for some integers $a,b$ (i.e., equality up to polylogarithmic factors). Theorem 1 gives a lower bound $T(n) \geq n^{1/3}/(2(\log n/\log 2)^{2/3})$ and Theorem 3 gives $T(n) = O(n^{3/4+\varepsilon})$; the conjecture proposes the true growth rate is $\widetilde{\Theta}(\sqrt{n})$.

Notes. PDF source — the tilde in $\widetilde{\Theta}$ is garbled in extraction (appears as bare 'e' or dropped); the argument of the second $\widetilde{\Theta}$ (presumably $\sqrt{|G|}$) is also lost in the PDF rendering. Statement reconstructed from context.

Source paper

 Inverse problems for minimal complements and maximal supplements
 Noga Alon, Noah Kravitz, Matt Larson · 2020-12-30
 https://arxiv.org/abs/2006.00534
 PDF source

=== Source paper abstract / header ===
Abstract:Given a subset $W$ of an abelian group $G$, a subset $C$ is called an additive complement for $W$ if $W+C=G$; if, moreover, no proper subset of $C$ has this property, then we say that $C$ is a minimal complement for $W$. It is natural to ask which subsets $C$ can arise as minimal complements for some $W$. We show that in a finite abelian group $G$, every non-empty subset $C$ of size $|C| \leq 2^{2/3}|G|^{1/3}/((3e \log |G|)^{2/3}$ is a minimal complement for some $W$. As a corollary, we deduce that every finite non-empty subset of an infinite abelian group is a minimal complement. We also derive several analogous results for ``dual'' problems about maximal supplements.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Number Theory (math.NT)
 

 Cite as:
 arXiv:2006.00534 [math.CO]
 

 
  
 (or 
 arXiv:2006.00534v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.2006.00534
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 

 

 

 
 Submission history
 From: Matt Larson [view email] 
 [v1]
 Sun, 31 May 2020 14:53:18 UTC (16 KB)

 [v2]
 Wed, 30 Dec 2020 03:17:56 UTC (17 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Inverse problems for minimal complements and maximal supplements, by Noga Alon and 2 other authors
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
 | 2020-06
 

 Change to browse by:
 
 math
 math.NT
 

 

 

 
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
  "one_line": "I give an exact witness certificate, prove the conjectured square-root lower scale for sets of bounded difference multiplicity, and obtain the conjectured-order upper bound for balanced direct products.",
  "would_publish": false,
  "caveats": "The argument does not handle high difference multiplicity or indecomposable groups such as cyclic groups of prime order, and some observations may overlap the source paper."
}
```

# Mathematical writeup

## 1. Setup and outcome

Let \(G\) be a finite abelian group of order \(n\). A set \(C\subseteq G\) is a minimal complement if there is \(W\subseteq G\) such that
\[
C+W=G
\]
but
\[
(C\setminus\{c\})+W\ne G
\qquad\text{for every }c\in C.
\]
Equivalently, every \(c\in C\) has a private sum: some
\[
g_c\in (c+W)\setminus ((C\setminus\{c\})+W).
\]

I do not prove the full conjecture. I prove:

1. An exact finite certificate for \(C\) to be a minimal complement.
2. A square-root-scale sufficient condition in terms of the largest nonzero difference multiplicity of \(C\). In particular, difference-Sidon sets of size at most \(\sqrt{n/8}\) are minimal complements.
3. A nonminimal set of size \(|G_1|+|G_2|-1\) in every nontrivial direct product \(G_1\times G_2\). Thus the conjectured \(O(\sqrt n)\) upper bound holds for groups admitting a balanced direct decomposition.

The unresolved cases are precisely not covered by these two mechanisms: sets with highly repeated differences, and groups without balanced direct factors.

---

## 2. An exact certificate

Write
\[
C=\{c_1,\dots,c_m\}.
\]

### Lemma 2.1

The set \(C\) is a minimal complement in \(G\) if and only if there are elements
\[
x_1,\dots,x_m\in G
\]
such that, on defining
\[
X=\{x_1,\dots,x_m\}
\]
and
\[
Y=\bigcup_{i=1}^m
   \{x_i+c_i-c_j:j\ne i\},
\]
the following hold:

1. \(X\cap Y=\varnothing\);
2. there is no \(z\in G\) such that
   \[
   z-C:=\{z-c:c\in C\}\subseteq Y.
   \]

#### Proof

Suppose first that such \(x_i\) exist. Put
\[
W=G\setminus Y.
\]
If some \(z\notin C+W\), then \(z-c_j\notin W\) for every \(j\), hence
\[
z-C\subseteq Y,
\]
contrary to condition 2. Therefore \(C+W=G\).

For each \(i\), let
\[
g_i=c_i+x_i.
\]
Since \(x_i\in X\) and \(X\cap Y=\varnothing\), we have \(x_i\in W\), and hence \(g_i\in c_i+W\). On the other hand, for \(j\ne i\),
\[
g_i-c_j=x_i+c_i-c_j\in Y,
\]
so \(g_i\notin c_j+W\). Thus \(g_i\) is private to \(c_i\), proving minimality.

Conversely, suppose that \(C\) is a minimal complement to \(W\), and put
\[
A=G\setminus W.
\]
For every \(i\), choose
\[
g_i\notin (C\setminus\{c_i\})+W.
\]
Since \(C+W=G\), necessarily \(g_i=c_i+x_i\) for some \(x_i\in W\). For \(j\ne i\),
\[
g_i-c_j=x_i+c_i-c_j\notin W,
\]
so all such elements lie in \(A\). Consequently,
\[
X\subseteq W,\qquad Y\subseteq A,
\]
and therefore \(X\cap Y=\varnothing\).

Finally, if \(z-C\subseteq Y\subseteq A\), then \(z-c\notin W\) for every \(c\in C\), contradicting \(C+W=G\). ∎

Thus the inverse problem is equivalent to constructing \(m\) “roots” \(x_i\) such that the union of the \(m\) punctured translates
\[
x_i+c_i-C\setminus\{x_i\}
\]
avoids all roots and contains no translate of \(-C\).

---

## 3. A bounded-difference-multiplicity theorem

Define the largest nonzero ordered difference multiplicity by
\[
\rho(C)=
\max_{d\ne 0}
\left|\{(a,b)\in C^2:a-b=d\}\right|.
\]

### Proposition 3.1

Let \(m=|C|\ge2\), let \(\lambda=\rho(C)\), and put
\[
r=\left\lceil\frac m\lambda\right\rceil,\qquad
b=(m-1)^2,\qquad
L=n-2(m-1)^2.
\]
If \(L>0\) and
\[
L^m>
n^{m-r+1}\binom mr (m-1)^{2r},
\tag{3.1}
\]
then \(C\) is a minimal complement.

#### Proof

We count choices of \(x_1,\dots,x_m\).

For each \(i\), put
\[
Y_i=\{x_i+c_i-c_j:j\ne i\}.
\]
Choose the \(x_i\) sequentially while requiring \(X\cap Y=\varnothing\). Once
\(x_1,\dots,x_{i-1}\) have been selected, the new \(x_i\) must avoid:

- the sets \(Y_h\), \(h<i\), contributing at most \((i-1)(m-1)\) forbidden values;
- all values for which an old root \(x_h\) belongs to \(Y_i\), contributing at most another \((i-1)(m-1)\) forbidden values.

Thus there are at least
\[
n-2(i-1)(m-1)\ge L
\]
choices at each step. Hence the number of tuples satisfying \(X\cap Y=\varnothing\) is at least
\[
L^m.
\tag{3.2}
\]

It remains to bound the tuples for which \(Y\) contains some \(z-C\). Fix such a \(z\), and set
\[
S=z-C.
\]
Since \(S\subseteq Y\) and \(X\cap Y=\varnothing\), no \(x_i\) lies in \(S\).

For fixed \(i\), an element of \(Y_i\cap S\) gives indices \(j\ne i\) and \(k\) satisfying
\[
x_i+c_i-c_j=z-c_k,
\]
or equivalently
\[
x_i+c_i-z=c_j-c_k.
\tag{3.3}
\]
The right side cannot be zero, since otherwise \(x_i=z-c_i\in S\). By the definition of \(\lambda\), equation (3.3) has at most \(\lambda\) ordered solutions \((j,k)\). Hence
\[
|Y_i\cap S|\le\lambda.
\]
Since the \(m\)-element set \(S\) is covered by the \(Y_i\), at least
\[
r=\left\lceil\frac m\lambda\right\rceil
\]
of the rows \(Y_i\) meet \(S\).

For fixed \(z\) and \(i\), if \(Y_i\cap S\ne\varnothing\), then
\[
x_i=z-c_i+c_j-c_k
\]
for some \(j\ne i\) and \(k\ne j\). Thus there are at most
\[
(m-1)^2=b
\]
possible values of \(x_i\).

Choose \(r\) rows which meet \(S\). There are at most
\[
\binom mr b^r n^{m-r}
\]
tuples for this choice of \(z\). Taking the union over all \(n\) choices of \(z\), the number of bad tuples is at most
\[
n^{m-r+1}\binom mr b^r.
\tag{3.4}
\]
By (3.1), this is smaller than the lower bound (3.2) for root-disjoint tuples. Therefore some tuple satisfies both conditions in Lemma 2.1. ∎

### A convenient consequence

Using natural logarithms, Proposition 3.1 implies the following simpler criterion.

### Corollary 3.2

If
\[
n\ge16\lambda m^2
\qquad\text{and}\qquad
m\ge\lambda\log n,
\tag{3.5}
\]
where \(\lambda=\rho(C)\), then \(C\) is a minimal complement.

#### Verification

Normalize (3.1) by \(n^m\). Its right-hand bad proportion is at most
\[
n\binom mr\left(\frac{(m-1)^2}{n}\right)^r.
\]
Under (3.5),
\[
\binom mr\le\left(\frac{em}{r}\right)^r\le(e\lambda)^r
\]
and
\[
\frac{(m-1)^2}{n}\le\frac1{16\lambda},
\]
so the bad proportion is at most
\[
n\left(\frac e{16}\right)^r
\le
\exp\left(\log n-(\log16-1)\frac m\lambda\right)
<
\exp\left(-\frac{m}{7\lambda}\right).
\]
Meanwhile
\[
\left(1-\frac{2(m-1)^2}{n}\right)^m
\ge
\exp\left(-\frac{m}{7\lambda}\right).
\]
Thus (3.1) holds.

Consequently, any nonminimal \(C\) with \(m\ge2\) must satisfy
\[
\rho(C)>
\min\left\{\frac{m}{\log n},\frac{n}{16m^2}\right\}.
\tag{3.6}
\]
In particular, a counterexample of size
\[
m=\frac{\sqrt n}{L}
\]
must, in the usual polylogarithmic regime, have a nonzero difference occurring more than approximately \(L^2/16\) times.

---

## 4. The square-root result for Sidon sets

Call \(C\) difference-Sidon if every nonzero ordered difference has at most one representation:
\[
a-b=c-d\ne0
\quad\Longrightarrow\quad
(a,b)=(c,d).
\]

### Theorem 4.1

If \(C\) is difference-Sidon and
\[
|G|\ge8|C|^2,
\]
then \(C\) is a minimal complement.

#### Proof

Let \(m=|C|\ge2\). Here \(\lambda=1\), so \(r=m\). Proposition 3.1 reduces to
\[
n\left(\frac{(m-1)^2}{n-2(m-1)^2}\right)^m<1.
\tag{4.1}
\]
For fixed \(m\), the left side is decreasing in \(n>2(m-1)^2\). At \(n=8m^2\),
\[
n-2(m-1)^2
=
6m^2+4m-2
>
6m^2,
\]
and hence the left side of (4.1) is less than
\[
\frac{8m^2}{6^m}<1
\]
for every \(m\ge2\). The case \(m=1\) is trivial. ∎

Thus the conjectured square-root lower scale holds, with no polylogarithmic loss, for this natural class of additively unstructured sets.

More generally, for every fixed \(\lambda\), Corollary 3.2 together with the source paper’s universal \(n^{1/3}/\operatorname{polylog}n\) theorem gives:

> For sufficiently large \(n\), every \(C\subseteq G\) satisfying
> \(\rho(C)\le\lambda\) and
> \[
> |C|\le \frac14\sqrt{\frac n\lambda}
> \]
> is a minimal complement.

For \(|C|<\lambda\log n\), the source theorem applies for sufficiently large \(n\); above that range, Corollary 3.2 applies.

---

## 5. A square-root upper bound for balanced direct products

The following obstruction is elementary but gives the conjectured upper order for a broad class of groups.

### Proposition 5.1

Let
\[
G=G_1\times G_2,
\qquad |G_i|\ge2.
\]
Put
\[
C=(G_1\times\{0\})\cup(\{0\}\times G_2).
\]
Then \(C\) is not a minimal complement to any \(W\subseteq G\).

#### Proof

Let
\[
P_i=\pi_i(W)
\]
be the coordinate projections. Set
\[
A=G_1\times\{0\},\qquad B=\{0\}\times G_2.
\]
Then
\[
A+W=G_1\times P_2
\]
and
\[
B+W=P_1\times G_2.
\]
Therefore
\[
C+W=(G_1\times P_2)\cup(P_1\times G_2).
\]
This equals \(G_1\times G_2\) if and only if
\[
P_1=G_1\quad\text{or}\quad P_2=G_2.
\]
Indeed, if both projections are proper, choose
\(g_1\notin P_1\) and \(g_2\notin P_2\); then \((g_1,g_2)\) is uncovered.

If \(P_1=G_1\), then already
\[
B+W=G,
\]
so the proper subset \(B\subsetneq C\) is a complement. If \(P_2=G_2\), then similarly \(A+W=G\). Thus \(C\) is never minimal. ∎

Since
\[
|C|=|G_1|+|G_2|-1,
\]
this gives
\[
T(G_1\times G_2)
\le |G_1|+|G_2|-2.
\tag{5.1}
\]

In particular:

- If \(|G_1|\) and \(|G_2|\) are both within polylogarithmic factors of \(\sqrt{|G|}\), then
  \[
  T(G)=\widetilde O(\sqrt{|G|}).
  \]
- If \(G=H\times H\), then
  \[
  T(G)\le2\sqrt{|G|}-2.
  \]
- If \(n=ab\), \(\gcd(a,b)=1\), and \(a,b\ge2\), the Chinese remainder theorem gives
  \[
  T(\mathbb Z/n\mathbb Z)\le a+b-2.
  \]
  Thus the conjectured upper order follows whenever \(n\) has a balanced coprime factorization.

This does not address cyclic groups of prime or prime-power order.

---

## 6. What remains open

The certificate and counting argument isolate a concrete obstruction to the square-root lower bound: a prospective counterexample near
\[
|C|=\frac{\sqrt n}{\operatorname{polylog}n}
\]
must have a nonzero difference with polylogarithmically large multiplicity. However, one repeated difference does not by itself imply enough periodic structure to complete the argument. Handling such structured sets is the main gap.

On the upper-bound side, the direct-product construction gives the correct order whenever \(G\) splits into balanced factors, but it has no analogue proved here for additively indecomposable groups, especially \(\mathbb Z/p\mathbb Z\). The supplied \(O(n^{3/4+\varepsilon})\) bound therefore remains the best verified general bound in those cases.

I have not verified whether the certificate formulation or the direct-product observation already appears implicitly in the source paper or subsequent work; no novelty claim is made.
