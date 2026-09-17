Attack the following open graph-theory problem.

Catalog id: 1708.08486__00
Catalog status: open (triage tier 2, lean prove)
Catalog page: https://mlelarge.github.io/graph-conjectures/arxiv/1708.08486__00/
Source paper: Popular progression differences in vector spaces II (arXiv:1708.08486)

=== Catalog page (statement + literature review) ===
Exponential constant in r(n,m) for 𝔽₃ⁿ subspaces — Graph-theory open problems (arXiv)

 
 Status
 open
 high confidence
 

 The question asks whether the exponential base in the exponent of r(n,m) (the maximum size of a subset of F_3^n containing no affine m-dimensional subspace) is 3 (as in the random lower bound r(n,m) >= N^{1-(m+1)3^{-m}}) rather than C≈13.901 (as in the cap-set-supersaturation upper bound). Fox and Pham's paper itself provides evidence that the popular-differences approach cannot close this gap, and no subsequent work resolving or substantially narrowing it was found in the literature search.

 Reviewer notes. No follow-up paper resolving or substantially advancing the question was found in five web searches. The paper itself proves that the popular-differences/density-increment approach via Green's arithmetic regularity lemma cannot settle the correct exponential base, leaving the gap between 3 and C≈13.901 open. The question is closely tied to sharp bounds on n_3(alpha,beta) for beta=alpha^{3+o(1)}, which also remains open.

 
 Auto-reviewed 2026-05-15 with claude-sonnet-4-6 (web search enabled).
 

Informal. Is $3$, the lower bound on $r(n,m)$ given by considering a random set, the right exponential constant? That is, does $r(n,m) = N^{1-\varepsilon_m}$ hold with the same exponential base $3$ as in the random lower bound $r(n,m) \geq N^{1-(m+1)3^{-m}}$, rather than the base $C \approx 13.901$ appearing in the upper bound $r(n,m) \leq (1+o(1))N^{1-C^{-m}}$?

Context

The lower and upper bounds for $r(n,m)$ (the maximum size of a subset of $\mathbb{F}_3^n$ containing no affine $m$-dimensional subspace) both have the form $N^{1-\varepsilon_m}$ with $\varepsilon_m \to 0$ exponentially fast in $m$, but with different exponential constants: $3$ in the random lower bound and $C \approx 13.901$ in the upper bound derived from the cap set supersaturation result. The authors note that resolving this question is closely tied to whether $n_3(\alpha,\beta)$ is small enough for $\beta = \alpha^{3+o(1)}$, and their main result provides evidence that the approach via popular differences likely cannot resolve it.

Notes. Stated as an open question in running prose in the introduction without a formal labelled environment. PDF source — exponent notation in r(n,m) bounds may be garbled.

Source paper

 Popular progression differences in vector spaces II
 Jacob Fox, Huy Tuan Pham · 2019-11-21
 https://arxiv.org/abs/1708.08486
 PDF source

=== Source paper abstract / header ===
Abstract:Green used an arithmetic analogue of Szemerédi's celebrated regularity lemma to prove the following strengthening of Roth's theorem in vector spaces. For every $\alpha>0$, $\beta<\alpha^3$, and prime number $p$, there is a least positive integer $n_p(\alpha,\beta)$ such that if $n \geq n_p(\alpha,\beta)$, then for every subset of $\mathbb{F}_p^n$ of density at least $\alpha$ there is a nonzero $d$ for which the density of three-term arithmetic progressions with common difference $d$ is at least $\beta$. We determine for $p \geq 19$ the tower height of $n_p(\alpha,\beta)$ up to an absolute constant factor and an additive term depending only on $p$. In particular, if we want half the random bound (so $\beta=\alpha^3/2$), then the dimension $n$ required is a tower of twos of height $\Theta \left((\log p) \log \log (1/\alpha)\right)$. It turns out that the tower height in general takes on a different form in several different regions of $\alpha$ and $\beta$, and different arguments are used both in the upper and lower bounds to handle these cases.
 

 
 
 
 Subjects:
 
 Combinatorics (math.CO); Number Theory (math.NT)
 

 Cite as:
 arXiv:1708.08486 [math.CO]
 

 
  
 (or 
 arXiv:1708.08486v2 [math.CO] for this version)
 
 

 
  
 https://doi.org/10.48550/arXiv.1708.08486
 
 
 Focus to learn more
 
 
 
 arXiv-issued DOI via DataCite

 

 
 
 
 Journal reference:
 Discrete Analysis, 2019:16, 39 pp
 

 

 

 
 Submission history
 From: Huy Tuan Pham [view email] 
 [v1]
 Mon, 28 Aug 2017 19:01:31 UTC (43 KB)

 [v2]
 Thu, 21 Nov 2019 16:24:15 UTC (75 KB)

 

 
 
 
 Full-text links:
 Access Paper:

 
 
View a PDF of the paper titled Popular progression differences in vector spaces II, by Jacob Fox and Huy Tuan Pham
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
 | 2017-08
 

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
  "one_line": "The base-3 conjecture remains open, but alteration strengthens the displayed random lower bound and the conjectured factor 3 is proved for a recursively Fourier-uniform special case.",
  "would_publish": false,
  "caveats": "No general upper bound with exponential base 3 is obtained, and no novelty is claimed for the elementary auxiliary results."
}
```

# Mathematical writeup

## 1. Precise formulation

Let \(V_n=\mathbb F_3^n\), \(N=3^n\), and let \(r(n,m)\) be the maximum size of \(A\subseteq V_n\) containing no affine \(m\)-dimensional subspace.

Since the notation \(r(n,m)=N^{1-\varepsilon_m}\) is only asymptotic shorthand, define
\[
\varepsilon_m^*
 :=
1-\limsup_{n\to\infty}\frac{\log_3 r(n,m)}{n}.
\]
The catalogued question can then be formulated as
\[
\varepsilon_m^*=3^{-m+o(m)}
\qquad(m\to\infty).
\]
The quoted upper bound gives \(\varepsilon_m^*\gtrsim C^{-m}\), where \(C\approx13.901\). The difficult missing direction is
\[
\varepsilon_m^*\ge 3^{-m-o(m)}.
\]

I do not prove that direction.

---

## 2. A stronger alteration lower bound

The displayed random lower bound can be improved in its polynomial-in-\(m\) factor.

### Proposition 2.1

For every fixed \(m\ge1\), with \(q=3^m\),
\[
r(n,m)\ge c_m N^{\,1-\frac{m}{q-1}}
\]
for some constant \(c_m>0\) and all sufficiently large \(n\). Consequently,
\[
\varepsilon_m^*\le \frac{m}{3^m-1}=3^{-m+o(m)}.
\]

### Proof

The number of affine \(m\)-flats in \(V_n\) is
\[
L_{n,m}
 =3^{n-m}{n\brack m}_3
 =\Theta_m(N^{m+1}),
\]
where
\[
{n\brack m}_3
 =\prod_{i=0}^{m-1}\frac{3^n-3^i}{3^m-3^i}.
\]

Choose each point independently with probability \(p\), obtaining \(R\). Let \(X\) be the number of affine \(m\)-flats contained in \(R\). Then
\[
\mathbb E|R|=Np,\qquad
\mathbb EX=L_{n,m}p^q.
\]
Choose
\[
p=\left(\frac{N}{qL_{n,m}}\right)^{1/(q-1)}.
\]
Then \(qL_{n,m}p^{q-1}=N\), and hence
\[
\mathbb E(|R|-X)
 =Np-L_{n,m}p^q
 =\left(1-\frac1q\right)Np.
\]

For any realization, remove one selected point from each \(m\)-flat contained in \(R\). At most \(X\) points are removed, and the remaining set is \(m\)-flat-free. Thus some realization gives an \(m\)-flat-free set of size at least
\[
\left(1-\frac1q\right)Np
 =\Theta_m\!\left(N^{1-\frac{m}{q-1}}\right),
\]
because \(L_{n,m}=\Theta_m(N^{m+1})\). ∎

This is strictly stronger than the catalogued exponent \(1-(m+1)/3^m\), since
\[
\frac{m}{3^m-1}<\frac{m+1}{3^m}.
\]
It does not change the exponential base \(3\).

---

## 3. Full lines and an exact induction inequality

For \(A\subseteq V_n\), let \(\ell(A)\) denote the number of unoriented affine lines contained in \(A\).

### Lemma 3.1

If \(A\) is \(m\)-flat-free, then
\[
\ell(A)\le \frac{N-1}{2}\,r(n-1,m-1).
\]

### Proof

Fix a one-dimensional linear subspace \(D\le V_n\). Let
\[
B_D=\{x+D:\ x+D\subseteq A\}\subseteq V_n/D.
\]
If \(B_D\) contained an affine \((m-1)\)-flat in \(V_n/D\), its inverse image would be an affine \(m\)-flat contained in \(A\). Therefore
\[
|B_D|\le r(n-1,m-1).
\]
There are \((N-1)/2\) possible directions \(D\), and every affine line has a unique direction, proving the claim. ∎

This is the elementary core of the usual induction through popular differences.

---

## 4. The Fourier-uniform case has the desired factor \(3\)

Let \(f=1_A\), \(\alpha=|A|/N\), and use normalized Fourier coefficients
\[
\widehat f(\xi)=\mathbb E_{x\in V_n}f(x)\overline{\chi_\xi(x)}.
\]

### Proposition 4.1

Suppose \(A\subseteq V_n\) is \(m\)-flat-free and satisfies
\[
\max_{\xi\ne0}|\widehat f(\xi)|\le \frac{\alpha^2}{2}.
\]
Then
\[
\alpha\le
\max\left\{
2N^{-1/2},
\left(\frac{12\,r(n-1,m-1)}{N}\right)^{1/3}
\right\}.
\]

### Proof

Let
\[
T(A)=\sum_{x,d\in V_n}f(x)f(x+d)f(x-d).
\]
Fourier inversion gives
\[
\frac{T(A)}{N^2}
 =\sum_{\xi}\widehat f(\xi)^3.
\]
By Parseval,
\[
\sum_{\xi\ne0}|\widehat f(\xi)|^2\le\alpha.
\]
Consequently,
\[
\left|\sum_{\xi\ne0}\widehat f(\xi)^3\right|
 \le
\max_{\xi\ne0}|\widehat f(\xi)|
\sum_{\xi\ne0}|\widehat f(\xi)|^2
 \le \frac{\alpha^3}{2}.
\]
Thus
\[
T(A)\ge \frac{\alpha^3}{2}N^2.
\]

The \(d=0\) terms contribute \(|A|=\alpha N\), while every affine line contained in \(A\) contributes six nonzero ordered pairs \((x,d)\). Hence
\[
T(A)=\alpha N+6\ell(A).
\]
Lemma 3.1 therefore gives
\[
\frac{\alpha^3}{2}N^2
 \le \alpha N+3(N-1)r(n-1,m-1),
\]
and hence
\[
\alpha^3\le \frac{2\alpha}{N}
             +\frac{6r(n-1,m-1)}{N}.
\]
If \(\alpha\le2N^{-1/2}\), the first alternative holds. Otherwise
\(2\alpha/N\le\alpha^3/2\), giving
\[
\alpha^3\le\frac{12r(n-1,m-1)}{N}.
\]
∎

Thus, if
\[
r(n-1,m-1)\le N^{1-\delta+o(1)},
\]
then every Fourier-uniform \(m\)-flat-free set has density
\[
\alpha\le N^{-\delta/3+o(1)}.
\]
This is exactly the desired factor \(3\) in one induction step.

If one assumes this Fourier-uniformity condition recursively for every set \(B_D\) arising in Lemma 3.1, then the base case \(m=1\) gives exponent deficit \(1/2\), and induction gives
\[
\delta_m=\frac{1}{2\cdot3^{m-1}}.
\]
Hence the base-\(3\) assertion is valid for this recursively Fourier-uniform class. The unresolved issue is that general extremal sets need not satisfy such uniformity.

---

## 5. Why ordinary line supersaturation cannot by itself give base \(3\)

Suppose one has a cap-set bound
\[
r(k,1)\le Kc^k,\qquad c<3,
\]
and put
\[
\eta=1-\log_3 c.
\]
A standard averaging argument gives, when the relevant \(k\le n\),
\[
\ell(A)\gg N^2\alpha^{\,1+1/\eta}.
\]

Indeed, choose a uniformly random affine \(k\)-flat \(W\). Inside \(W\),
\[
\ell(A\cap W)\ge |A\cap W|-r(k,1),
\]
because deleting at most one point for each contained line leaves a cap set. Choosing \(k\) so that
\[
K(c/3)^k\le\alpha/2
\]
gives
\[
\mathbb E\ell(A\cap W)\ge\frac{\alpha3^k}{2}.
\]
A fixed affine line lies in \(W\) with probability
\[
\frac{3^{k-1}(3^k-1)/2}{3^{n-1}(3^n-1)/2}
 <3^{2(k-n)}.
\]
It follows that
\[
\ell(A)\gg \frac{\alpha N^2}{3^k}
 \gg N^2\alpha^{\,1+1/\eta}.
\]

Combining this with Lemma 3.1 divides the exponent deficit by
\[
K_{\mathrm{sup}}=1+\frac1\eta.
\]
Substituting the cap-set exponent used in the source yields the quoted constant near \(13.901\).

There is a genuine obstruction to replacing this universal supersaturation exponent by \(3\). Let
\[
C_k=\{0,1\}^k\subseteq\mathbb F_3^k.
\]
This is a cap set: in any nonconstant affine line, some varying coordinate assumes all three values \(0,1,2\). For
\[
A=\mathbb F_3^h\times C_k
\]
we have
\[
\alpha=(2/3)^k.
\]
Every line contained in \(A\) must be constant in the \(C_k\)-coordinate, so
\[
\ell(A)
 =2^k\frac{3^{h-1}(3^h-1)}2.
\]
Writing \(\sigma=\log_3 2\), this is
\[
\ell(A)=\Theta\!\left(
 N^2\alpha^{K_0}
\right),
\qquad
K_0=\frac{2-\sigma}{1-\sigma}
   =1+\frac1{1-\sigma}
   \approx3.7095.
\]
Therefore no universal inequality
\[
\ell(A)\gg N^2\alpha^{3+o(1)}
\]
can hold, even when \(|A|=N^{1-\delta}\) with arbitrarily small fixed \(\delta>0\).

This is not a counterexample to the conjecture: \(A\) contains the \(h\)-flat
\(\mathbb F_3^h\times\{c\}\). It shows that a successful proof must exploit such concentration of line directions to construct the desired higher-dimensional flat, rather than merely count all lines.

---

## 6. A direct affine-map criterion

Define
\[
M_m(A)=
\#\left\{(x,d_1,\dots,d_m):
x+\sum_{i=1}^m t_id_i\in A
\text{ for every }t\in\mathbb F_3^m
\right\}.
\]
If \(A\) is \(m\)-flat-free, then \(d_1,\dots,d_m\) must be linearly dependent. The number of dependent ordered \(m\)-tuples is at most
\[
\sum_{j=1}^m 3^{j-1}N^{m-1}
 =\frac{3^m-1}{2}N^{m-1}.
\]
Thus
\[
M_m(A)\le \frac{3^m-1}{2}N^m.
\]

Consequently, any class of sets satisfying the random-count lower bound
\[
M_m(A)\ge c_m\alpha^{3^m}N^{m+1}
\]
also satisfies
\[
|A|\le
\left(\frac{3^m-1}{2c_m}\right)^{1/3^m}
N^{1-3^{-m}}.
\]
This has exactly the conjectured exponential base. The missing point is that such a random-count estimate is false for arbitrary structured sets; one needs a structure-versus-randomness argument that uses the structured outcome to build an \(m\)-flat.

---

## 7. An exact finite boundary case

There is also a simple exact answer when the forbidden flat is a hyperplane.

### Proposition 7.1

For \(d\ge1\),
\[
r(d,d-1)=3^d-(2d+1).
\]
Equivalently,
\[
r(m+1,m)=3^{m+1}-(2m+3).
\]

### Proof

Let \(B=V_d\setminus A\). Then \(A\) contains no affine hyperplane exactly when \(B\) meets every affine hyperplane.

The set
\[
B_0=\{0\}\cup\{\pm e_i:1\le i\le d\}
\]
has size \(2d+1\) and meets every affine hyperplane: for every nonzero linear functional \(y\), choose \(i\) with \(y(e_i)\ne0\); then
\[
y(0),\ y(e_i),\ y(-e_i)
\]
are the three elements of \(\mathbb F_3\).

For the lower bound, translate a blocking set \(B\) so that \(0\in B\). Consider
\[
P(y)=\prod_{b\in B}(\langle y,b\rangle-1).
\]
For every nonzero \(y\), the hyperplane
\(\{x:\langle y,x\rangle=1\}\) meets \(B\), so \(P(y)=0\). At \(y=0\), \(P(0)\ne0\). Hence, as a function on \(\mathbb F_3^d\), \(P\) is a nonzero scalar multiple of
\[
\prod_{i=1}^d(1-y_i^2),
\]
the delta function at \(0\). Its unique reduced polynomial representative has total degree \(2d\). Since the factor corresponding to \(b=0\) is constant, \(P\) has degree at most \(|B|-1\). Therefore
\[
|B|-1\ge2d,
\]
so \(|B|\ge2d+1\). ∎

This diagonal regime does not control the fixed-\(m\), \(n\to\infty\) exponent.

---

## 8. Remaining gap

The alteration argument establishes the easy side
\[
\varepsilon_m^*\le\frac{m}{3^m-1}=3^{-m+o(m)}.
\]
The unresolved task is the matching lower bound
\[
\varepsilon_m^*\ge3^{-m-o(m)}.
\]

The Fourier calculation shows that each genuinely pseudorandom induction step costs exactly a factor \(3\). The cap-product example shows why an unconditional cubic line-supersaturation estimate is impossible: lines may concentrate in a large subspace. What is missing is a quantitative dichotomy proving that either the line distribution is sufficiently uniform, or its concentration itself supplies enough independent directions to build the forbidden affine \(m\)-flat. No such dichotomy is proved here.
