```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "An entropy-refined deck count shows that for every fixed c<0.3698, a random q~cn colouring is a.a.s. not 1-ball reconstructible, while the n^(2+ε) upper bound remains untouched.",
  "would_publish": false,
  "caveats": "This only sharpens the lower bound, assumes the standard rooted colour-preserving card convention and q>=2, and may be implicit in the source's unextracted counting discussion."
}
```

## 1. Setup and partial result

Let \(N=2^n\), and let \(\chi:V(Q_n)\to[q]\) be uniformly random. A rooted coloured \(1\)-ball is a coloured star with \(n\) leaves, so its isomorphism type is determined by

\[
\left(\chi(v),\,m_v(1),\ldots,m_v(q)\right),
\qquad
m_v(a)=|\{u\in N(v):\chi(u)=a\}|.
\]

Write \(p_{n,q}\) for the probability that \(\chi\) is reconstructible from the multiset of these cards, up to an automorphism of \(Q_n\).

Define \(H_\lambda\) to be the Shannon entropy, with natural logarithms, of a Poisson random variable of mean \(\lambda\):

\[
H_\lambda
 =\lambda(1-\log\lambda)
   +e^{-\lambda}\sum_{k=0}^{\infty}\frac{\lambda^k}{k!}\log(k!).
\]

Let \(\lambda_0\) be the unique positive solution of

\[
H_{\lambda_0}=\lambda_0\log 2
\]

and set

\[
c_{\mathrm{prof}}=\frac1{\lambda_0}.
\]

Numerically,

\[
\lambda_0=2.7041\ldots,
\qquad
c_{\mathrm{prof}}=0.3698\ldots .
\]

### Theorem

If \(q=q(n)\ge 2\) and

\[
\limsup_{n\to\infty}\frac{q(n)}n<c_{\mathrm{prof}},
\]

then

\[
p_{n,q}\longrightarrow 0.
\]

Consequently, in the usual nondegenerate interpretation of the high-colour transition,

\[
\boxed{\quad q^*(n)\ge (0.3698\ldots-o(1))\,n.\quad}
\]

This improves the constant obtainable by counting all possible \(1\)-ball types, which only gives \(0.293815\ldots\,n\).

---

## 2. Basic deck count

The number of possible leaf-colour multisets is

\[
B_{n,q}=\binom{n+q-1}{q-1}.
\]

Thus the total number of possible card types is

\[
K_{n,q}=qB_{n,q}.
\]

There are at most

\[
\binom{N+K_{n,q}-1}{N}
\]

possible decks.

Moreover,

\[
|\operatorname{Aut}(Q_n)|=2^n n!=Nn!.
\]

For any deck containing a reconstructible colouring, its entire fibre is contained in one automorphism orbit. Hence it contains at most \(Nn!\) reconstructible colourings. Therefore

\[
p_{n,q}
 \le
 \frac{Nn!}{q^N}
 \binom{N+K_{n,q}-1}{N}.
\tag{2.1}
\]

Counting all possible profiles in this way gives the following elementary constant. If \(q\sim cn\), then

\[
\log B_{n,q}
 =n h(c)+O(\log n),
\qquad
h(c)=(1+c)\log(1+c)-c\log c.
\]

Thus \(K_{n,q}\ll N\) exponentially whenever \(h(c)<\log2\). The root of \(h(c)=\log2\) is \(c=0.293815\ldots\).

The improvement below comes from observing that almost all actual neighbourhood profiles occupy a much smaller set than the set of all weak compositions.

---

## 3. Entropy of a random neighbourhood profile

Let \(Z_1,\ldots,Z_n\) be independent uniform elements of \([q]\), and let

\[
M=(M_1,\ldots,M_q),\qquad
M_a=|\{i:Z_i=a\}|.
\]

This is exactly the distribution of the leaf-colour multiset at any fixed vertex.

For \(\sum_a m_a=n\),

\[
\Pr(M=m)=\frac{n!}{q^n\prod_{a=1}^q m_a!}.
\]

Its self-information is therefore

\[
I(M):=-\log\Pr(M)
 =n\log q-\log(n!)+\sum_{a=1}^q\log(M_a!).
\tag{3.1}
\]

Assume \(q/n\to c>0\). Since \(M_1\sim\operatorname{Bin}(n,1/q)\),

\[
M_1\ \xrightarrow{d}\ \operatorname{Poisson}(1/c).
\]

Also \(\log(k!)\le k^2\), while the binomial variables here have uniformly bounded moments of every fixed order. Hence uniform integrability gives

\[
\mathbb E\log(M_1!)
 \longrightarrow
 \mathbb E\log(K!),
\qquad K\sim\operatorname{Poisson}(1/c).
\]

Using Stirling's formula in (3.1),

\[
\begin{aligned}
\frac1n\mathbb E I(M)
&=
\frac{n\log q-\log(n!)}n
 +\frac qn\,\mathbb E\log(M_1!)\\
&\longrightarrow
1+\log c+c\,\mathbb E\log(K!)\\
&=cH_{1/c}.
\end{aligned}
\tag{3.2}
\]

Define

\[
s(c):=cH_{1/c}.
\tag{3.3}
\]

### Typical-profile lemma

For every fixed \(\varepsilon>0\), there is a set \(\mathcal S_{n,q}\) of leaf-colour profiles such that

\[
|\mathcal S_{n,q}|
 \le \exp\!\bigl(n(s(c)+\varepsilon)\bigr)
\tag{3.4}
\]

and

\[
\Pr(M\notin\mathcal S_{n,q})
 \le \exp\!\left(-\Omega_\varepsilon
       \left(\frac n{\log^2 n}\right)\right).
\tag{3.5}
\]

#### Proof

Changing one of the \(Z_i\) changes

\[
\sum_a\log(M_a!)
\]

by

\[
-\log r+\log(s+1)
\]

for some \(1\le r\le n\) and \(0\le s<n\). Its absolute value is at most \(\log(n+1)\). McDiarmid's inequality therefore gives, for fixed \(\eta>0\),

\[
\Pr\bigl(|I(M)-\mathbb EI(M)|>\eta n\bigr)
 \le
2\exp\left(-\frac{2\eta^2n}{\log^2(n+1)}\right).
\]

By (3.2), take

\[
\mathcal S_{n,q}
 =\{m:I(m)\le n(s(c)+\varepsilon)\}.
\]

Every \(m\in\mathcal S_{n,q}\) has probability at least
\(\exp[-n(s(c)+\varepsilon)]\). Since the probabilities sum to at most one,

\[
|\mathcal S_{n,q}|
 \le \exp[n(s(c)+\varepsilon)].
\]

This proves the lemma. \(\square\)

---

## 4. Counting typical decks

Suppose now that \(c>0\) and

\[
s(c)<\log2.
\]

Choose \(\varepsilon>0\) sufficiently small that

\[
s(c)+3\varepsilon<\log2.
\tag{4.1}
\]

A card is called atypical when its leaf profile is outside \(\mathcal S_{n,q}\). Let \(X\) be the number of atypical cards in the deck. No independence between cards is needed: by the marginal estimate (3.5),

\[
\mathbb EX
 \le
N\exp\left(-\Omega\left(\frac n{\log^2n}\right)\right).
\]

Consequently, for some

\[
\delta_n=\exp\left(-\Omega\left(\frac n{\log^2n}\right)\right)
\quad\text{with}\quad
n\delta_n\to0,
\]

Markov's inequality gives

\[
\Pr(X>\delta_nN)=o(1).
\tag{4.2}
\]

There are at most

\[
T_n=q|\mathcal S_{n,q}|
 \le \exp[n(s(c)+2\varepsilon)]
\]

typical card types. By (4.1),

\[
\frac{T_n}{N}\le e^{-\Omega(n)}.
\tag{4.3}
\]

The total number \(K_{n,q}\) of all card types satisfies
\(\log K_{n,q}=O(n)\) when \(q\sim cn\).

Let \(J=\lceil\delta_nN\rceil\). The number of decks with at most \(J\) atypical cards is at most

\[
(J+1)
\binom{N+T_n}{T_n}
\binom{J+K_{n,q}}{J}.
\tag{4.4}
\]

By (4.3),

\[
\log\binom{N+T_n}{T_n}
 \le
T_n\log\frac{e(N+T_n)}{T_n}
=o(N).
\]

Also,

\[
\log\binom{J+K_{n,q}}J
 \le
J\log\!\left(e\left(1+\frac{K_{n,q}}J\right)\right)
=O(Jn)
=o(N),
\]

because \(J/N=\delta_n\) and \(n\delta_n\to0\). Thus the number of decks satisfying (4.2) is

\[
\exp(o(N)).
\tag{4.5}
\]

Each such deck can account for at most \(Nn!=\exp(o(N))\) reconstructible colourings. Therefore the fraction of all \(q^N\) colourings which are reconstructible and have such a deck is at most

\[
\frac{\exp(o(N))}{q^N}=o(1).
\]

Together with (4.2), this proves that \(p_{n,q}\to0\) whenever \(q/n\to c>0\) and \(s(c)<\log2\).

If \(q=o(n)\), then

\[
\log K_{n,q}
 \le
\log q+q\log\!\left(\frac{e(n+q)}q\right)
=o(n).
\]

Hence \(K_{n,q}=e^{o(n)}\ll N\), and the elementary count (2.1) already gives \(p_{n,q}\to0\) for \(q\ge2\). A subsequence argument now proves the theorem for every sequence with
\(\limsup q/n<c_{\mathrm{prof}}\).

---

## 5. Evaluation and uniqueness of the constant

Writing \(\lambda=1/c\), the condition \(s(c)=\log2\) becomes

\[
\frac{H_\lambda}{\lambda}=\log2.
\]

This equation has a unique positive solution. Indeed, using the Poisson differentiation identity

\[
\frac{d}{d\lambda}\mathbb Ef(K)
 =\mathbb E[f(K+1)-f(K)],
\]

one obtains

\[
H_\lambda'
 =\mathbb E\log(K+1)-\log\lambda
\]

and

\[
\begin{aligned}
H_\lambda''
&=\mathbb E\log\frac{K+2}{K+1}-\frac1\lambda\\
&\le \mathbb E\frac1{K+1}-\frac1\lambda\\
&=\frac{1-e^{-\lambda}}\lambda-\frac1\lambda<0.
\end{aligned}
\]

Thus \(H_\lambda\) is strictly concave with \(H_0=0\), so \(H_\lambda/\lambda\) is strictly decreasing. Moreover,

\[
\frac{H_\lambda}{\lambda}\to\infty
\quad(\lambda\downarrow0),
\qquad
\frac{H_\lambda}{\lambda}\to0
\quad(\lambda\to\infty).
\]

Direct evaluation of the absolutely convergent series gives

\[
\lambda_0=2.7041\ldots,
\qquad
c_{\mathrm{prof}}=\lambda_0^{-1}=0.3698\ldots .
\]

---

## 6. Exact algebraic formulation of the unresolved upper bound

Let \(A\) be the adjacency matrix of \(Q_n\), and let \(X\) be the \(N\times q\) one-hot matrix of the colouring:

\[
X_{v,a}=\mathbf 1_{\{\chi(v)=a\}}.
\]

The card at \(v\) is precisely row \(v\) of

\[
[X\mid AX].
\]

Thus another colouring \(X'\) has the same deck exactly when there is a permutation matrix \(P\) such that

\[
[X'\mid AX']=P[X\mid AX].
\]

Equivalently,

\[
X'=PX
\quad\text{and}\quad
(AP-PA)X=0.
\tag{6.1}
\]

Permutation matrices commuting with \(A\) are exactly automorphisms of \(Q_n\). Therefore the upper-bound problem is to prove that, for random one-hot \(X\), every solution \(P\) of (6.1) produces a colouring \(PX\) already in the automorphism orbit of \(X\).

For a fixed \(P\), one has the elementary anti-concentration bound

\[
\Pr\bigl((AP-PA)X=0\bigr)
 \le
q^{-\operatorname{rank}(AP-PA)}.
\]

Indeed, assign distinct real numbers to the \(q\) colours, obtaining an iid \(q\)-valued vector \(z\). Equation (6.1) implies \((AP-PA)z=0\), and an invertible rank-sized minor determines that many coordinates uniquely after the remaining coordinates are exposed.

This fixed-\(P\) estimate does not resolve the problem: there are \(N!\) permutations, and the corresponding events overlap heavily. A successful upper-bound argument would need substantial structural control of permutations satisfying (6.1), not merely a union bound.

## 7. Remaining gap

The result proves only the strengthened necessary condition

\[
q^*(n)\ge(0.3698\ldots-o(1))n.
\]

It gives no improvement to the known sufficient condition \(q\ge n^{2+\varepsilon}\), and it does not establish that the true transition is linear. Also, \(q=1\) is a trivial exceptional case, so a literal monotone threshold in \(q\) requires a nondegenerate convention. I have not verified whether the entropy-refined constant above is already implicit in the full counting discussion of the source paper.