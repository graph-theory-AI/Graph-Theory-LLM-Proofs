```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A block-tribes construction gives balanced monotone strategies with success probability arbitrarily close to 1/2 for every number of players, so in fact p_monotone(t)=1/2.",
  "would_publish": true,
  "caveats": "The construction uses an enormous but finite number of hats and applies to the standard supremum-over-n, fiber-containment definition; it does not apply to the intersecting variant."
}
```

# Statement

Write \(\Omega_n=\{0,1\}^n\), with the uniform probability measure. Let \(\mathcal M_n\) be the collection of all balanced monotone families
\[
\mathcal A\subseteq\Omega_n,\qquad
|\mathcal A|=2^{n-1},
\]
where monotone means upward closed under changing zeroes to ones.

In the monotone relaxation, player \(i\), after seeing \(x_{-i}\), chooses some
\[
\mathcal A_i(x_{-i})\in\mathcal M_n
\]
and succeeds when \(x_i\in\mathcal A_i(x_{-i})\). Equivalently, the common success set has every \(i\)-fiber contained in a balanced monotone family.

Under this definition:

> **Theorem.** For every finite \(t\ge1\),
> \[
> p_{\mathrm{monotone}}(t)=\frac12.
> \]
> Consequently, \(p_{\mathrm{monotone}}(t)\) does not tend to zero.

The upper bound \(p_{\mathrm{monotone}}(t)\le1/2\) is immediate, because each individual player succeeds with probability exactly \(1/2\). The substance is the matching lower bound as a supremum.

## 1. Balancing an arbitrary monotone family

We first record an elementary fact.

**Lemma 1.** Let \(\mathcal F\subseteq\Omega_n\) be upward closed. There is a balanced upward-closed family \(\mathcal A\) such that

- \(\mathcal F\subseteq\mathcal A\) if \(|\mathcal F|\le2^{n-1}\);
- \(\mathcal A\subseteq\mathcal F\) if \(|\mathcal F|\ge2^{n-1}\).

Moreover,
\[
\mu(\mathcal F\triangle\mathcal A)
 =\left|\mu(\mathcal F)-\frac12\right|.
\]

**Proof.** If \(\mathcal F\) is too small, repeatedly add an inclusion-maximal member of its complement. This preserves upward closure. If it is too large, repeatedly remove an inclusion-minimal member of \(\mathcal F\), again preserving upward closure. Stop at cardinality \(2^{n-1}\). \(\square\)

A fixed tie-breaking order makes this construction deterministic.

## 2. A general synchronization observation

Let \(C\subseteq\Omega_n^t\) be globally monotone. For each player \(i\) and observation \(x_{-i}\), let
\[
\mathcal F_i(x_{-i})
 =\{x_i:(x_1,\dots,x_t)\in C\}
\]
be the corresponding fiber, and put
\[
q_i(x_{-i})=\mu\bigl(\mathcal F_i(x_{-i})\bigr).
\]
Each \(\mathcal F_i(x_{-i})\) is monotone. By Lemma 1, choose a balanced monotone family \(\mathcal A_i(x_{-i})\) nested with this fiber in the appropriate direction.

Let
\[
E_i=\{x:x_i\in\mathcal A_i(x_{-i})\}.
\]
Conditionally on \(x_{-i}\),
\[
\mu\bigl(C\setminus E_i\mid x_{-i}\bigr)
   =\left(q_i(x_{-i})-\frac12\right)_+.
\]
It follows that
\[
\Pr\left(\bigcap_{i=1}^t E_i\right)
 \geq \Pr(C)-
 \sum_{i=1}^t
 \mathbb E\left|q_i(X_{-i})-\frac12\right|.
\tag{1}
\]

Thus it suffices to construct a monotone event \(C\) of probability about \(1/2\) whose conditional probability, after revealing any \(t-1\) blocks, is highly concentrated about \(1/2\).

## 3. The block-tribes event

Fix \(t\ge2\) and an integer \(m\ge1\). Put
\[
u=2^{-m},\qquad s=u^t=2^{-mt},
\]
and choose
\[
N=\left\lceil\frac{\log 2}{-\log(1-s)}\right\rceil.
\]
Each player has
\[
n=mN
\]
hats, partitioned into \(N\) disjoint tribes of \(m\) hats each.

Define \(C\) to be the event that there is some tribe \(a\in[N]\) for which every one of the \(mt\) hats in that tribe, across all \(t\) players, is black. Thus
\[
C=\left\{\exists a\in[N]\ \forall i\in[t],\ \forall b\in[m]:
X_{i,a,b}=1\right\}.
\]
This event is monotone.

The \(N\) tribe events are independent, each of probability \(s\), so
\[
c:=\Pr(C)=1-(1-s)^N.
\]
By the choice of \(N\),
\[
\frac12\le c<\frac12+\frac{s}{2}.
\tag{2}
\]

## 4. Conditional probabilities concentrate

Fix player \(i\), and expose all other players' bits. A tribe is eligible for player \(i\) if all its \(m(t-1)\) exposed bits are black. Let \(M_i\) be the number of eligible tribes. Then
\[
M_i\sim\operatorname{Bin}(N,r),
\qquad r=u^{t-1}.
\]
Given the other players' stacks, the \(i\)-fiber of \(C\) is the monotone family saying that at least one of these \(M_i\) eligible tribes has all \(m\) of player \(i\)'s bits black. Its measure is therefore
\[
Q_i=1-(1-u)^{M_i}.
\tag{3}
\]
Moreover,
\[
\mathbb E Q_i
 =1-(1-ru)^N
 =1-(1-s)^N
 =c.
\tag{4}
\]

We need concentration of \(Q_i\). Set \(Z_i=1-Q_i=(1-u)^{M_i}\). Writing \(M_i\) as a sum of \(N\) independent Bernoulli variables and applying variance tensorization,
\[
\operatorname{Var}(Z_i)
 \le N r(1-r)u^2
 \le Nru^2
 =Nsu.
\]
The definition of \(N\) gives
\[
Ns\le \log 2+s<2,
\]
and hence
\[
\operatorname{Var}(Q_i)=\operatorname{Var}(Z_i)\le2u.
\tag{5}
\]
Combining (2), (4), and (5),
\[
\mathbb E\left|Q_i-\frac12\right|
 \le \sqrt{\operatorname{Var}(Q_i)}
       +\left|c-\frac12\right|
 \le \sqrt{2u}+\frac{s}{2}.
\tag{6}
\]

## 5. The balanced monotone strategy

For every player \(i\) and every realization \(x_{-i}\), apply Lemma 1 to the fiber \(\mathcal F_i(x_{-i})\) of \(C\):

- if \(Q_i(x_{-i})\le1/2\), enlarge it to a balanced monotone family;
- if \(Q_i(x_{-i})>1/2\), shrink it to a balanced monotone family.

This defines a deterministic valid monotone strategy. Using (1) and (6), its success probability is at least
\[
\begin{aligned}
\Pr\left(\bigcap_{i=1}^t E_i\right)
&\ge c-t\left(\sqrt{2u}+\frac{s}{2}\right)\\
&\ge \frac12
   -\sqrt2\,t\,2^{-m/2}
   -\frac t2\,2^{-mt}.
\end{aligned}
\tag{7}
\]

For each fixed \(t\), letting \(m\to\infty\) makes the right-hand side tend to \(1/2\). Therefore
\[
p_{\mathrm{monotone}}(t)\ge\frac12.
\]
The reverse inequality follows from the success probability \(1/2\) of any individual player. Hence
\[
\boxed{p_{\mathrm{monotone}}(t)=\frac12\quad\text{for every }t.}
\]

For an explicit sequence as \(t\to\infty\), one may take
\[
m=\left\lceil6\log_2(t+1)\right\rceil.
\]
Then (7) is \(1/2-O(t^{-2})\). The required number \(n=mN\) is enormous—roughly \(m(\log 2)2^{mt}\)—but it is finite, which is all the supremum over stack lengths requires.

## 6. Scope and remaining conjectures

The balanced families produced by Lemma 1 need not be intersecting. Thus this construction disproves the stated monotone conjecture but does not resolve either
\[
p_{\mathrm{intersecting}}(t)\to0
\quad\text{or}\quad
p_{\mathrm{dict}}(t)\to0.
\]

There is no mathematical gap in the argument under the standard definition above. The only definitional point to check against the source is that \(p_{\mathrm{monotone}}\) indeed permits an arbitrary balanced upward-closed family depending on the observed stacks, as indicated by the catalog and by the usual fiber formulation.