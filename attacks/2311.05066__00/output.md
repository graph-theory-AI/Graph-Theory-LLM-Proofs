```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Finite languages admit an exact linear-time return-path criterion, and two-word languages have a closed-form classification, but arbitrary unbounded languages are not classified.",
  "would_publish": false,
  "caveats": "Assumes the standard binary definition of c-padding: at least c zeroes at each end and at least one 1; novelty has not been independently literature-checked."
}
```

# Mathematical writeup

## 1. Formulation

Let \(\Sigma=\{0,1\}\). I use the following definition, which is forced by the quoted classification of singleton languages:

- a \(c\)-padded word is a finite binary word containing at least one \(1\), whose first and last \(c\) symbols are \(0\);
- factors are consecutive substrings;
- \(\mathcal S\) is \(c\)-unavoidable if every \(c\)-padded word contains some \(s\in\mathcal S\) or \(s^{\mathrm{rev}}\).

Set
\[
\mathcal F=\mathcal S\cup\{s^{\mathrm{rev}}:s\in\mathcal S\}.
\]
Call a word \(\mathcal F\)-clean if it contains no member of \(\mathcal F\).

A useful normalization is the following. Let
\[
\mathcal I=\{1\}\cup 1\Sigma^*1.
\]

**Observation.** For fixed \(c\), \(\mathcal S\) is \(c\)-unavoidable if and only if
\[
0^c x0^c
\]
contains a member of \(\mathcal F\) for every \(x\in\mathcal I\).

Indeed, after deleting all initial and terminal zeroes from any padded word, one obtains such an \(x\), and \(0^cx0^c\) is a factor of the original word.

The results below give:

1. an exact finite-state characterization of every finite language;
2. the bound \(c\leq \max_{s\in\mathcal S}|s|\);
3. a linear-time decision algorithm;
4. a complete closed-form classification when \(|\mathcal S|\leq2\);
5. an analogous finite-state criterion for regular, possibly infinite, languages.

The unrestricted nonregular case remains open here.

---

## 2. Finite languages

### 2.1 A universal bound on the padding constant

Let \(\mathcal S\neq\varnothing\) be finite and put
\[
\ell=\max_{s\in\mathcal S}|s|.
\]

**Lemma 2.1.** If \(\mathcal S\) is \(c\)-unavoidable for some \(c\), then it is already \(\ell\)-unavoidable.

**Proof.**
We prove the contrapositive. Suppose \(W\) is an \(\ell\)-padded \(\mathcal F\)-clean word.

For \(c\leq\ell\), the same \(W\) is \(c\)-padded. For \(c>\ell\), let
\[
W_c=0^{c-\ell}W0^{c-\ell}.
\]
Any newly created factor of length at most \(\ell\) that meets one of the added zero-blocks is all-zero, because \(W\) already begins and ends with \(\ell\) zeroes. But no all-zero member of \(\mathcal F\) can exist: such a word would already occur in the initial zero-block of \(W\). Hence \(W_c\) is still \(\mathcal F\)-clean.

Thus there is a clean \(c\)-padded word for every \(c\), so \(\mathcal S\) is not unavoidable. ∎

The bound is sharp: for \(\mathcal S=\{0^\ell\}\), padding \(\ell\) is necessary.

---

### 2.2 A de Bruijn graph characterization

Define a directed graph \(D_\ell(\mathcal F)\) as follows.

- Its vertices are the words \(u\in\Sigma^\ell\) containing no member of \(\mathcal F\).
- There is an arc
  \[
  u_1u_2\cdots u_\ell\longrightarrow u_2\cdots u_\ell b
  \]
  for each \(b\in\Sigma\), provided the target is also a vertex.

Let
\[
z=0^\ell,\qquad r=0^{\ell-1}1.
\]

Here a path \(r\leadsto z\) is understood not to exist if \(r\) or \(z\) is absent.

**Theorem 2.2.** A finite nonempty language \(\mathcal S\) is unavoidable if and only if either

1. \(z\notin V(D_\ell(\mathcal F))\), or
2. there is no directed path \(r\leadsto z\) in \(D_\ell(\mathcal F)\).

Equivalently, if no all-zero word belongs to \(\mathcal F\), then \(\mathcal S\) is avoidable for every padding constant precisely when
\[
0^{\ell-1}1\leadsto 0^\ell
\]
in the clean part of the order-\(\ell\) binary de Bruijn graph.

**Proof.**

If \(z\) is not a vertex, then some member of \(\mathcal F\) is a factor of \(0^\ell\), hence is all-zero. Every \(\ell\)-padded word contains it.

Now suppose \(z\) is a vertex. It has a zero-labelled loop. An \(\ell\)-padded clean word \(W\) starts and ends in state \(z\) when its consecutive length-\(\ell\) windows are read. Before its first \(1\), the walk remains at \(z\); the first \(1\) takes it from \(z\) to \(r\). The remaining windows give a path from \(r\) back to \(z\).

Conversely, suppose
\[
r=v_0\to v_1\to\cdots\to v_t=z
\]
is a path. Start with \(z\), append a \(1\) to reach \(r\), and then append the symbols defining the displayed path. The resulting word starts and ends with \(0^\ell\), contains a \(1\), and every length-\(\ell\) window is a vertex of \(D_\ell(\mathcal F)\). Since every forbidden word has length at most \(\ell\), the constructed word is \(\mathcal F\)-clean.

Thus an \(\ell\)-padded clean word exists exactly when \(r\leadsto z\). Lemma 2.1 finishes the proof. ∎

Hence, for finite languages, unavoidability is exactly a directed vertex-separation condition in a finite de Bruijn graph.

---

### 2.3 A linear-time algorithm

The graph above may have \(2^\ell\) vertices, but it need not be constructed explicitly.

Build the standard deterministic factor-avoidance automaton for \(\mathcal F\):

- its nondead states are proper prefixes of members of \(\mathcal F\), with transitions determined by the longest suffix that is such a prefix;
- the dead state \(\bot\) is entered exactly when a member of \(\mathcal F\) has appeared as a factor.

Let \(q\) be the state reached after reading \(0^\ell\). If \(q\neq\bot\), then \(q\) has a zero-loop: after \(\ell\) zeroes, all relevant suffix information has stabilized. Put
\[
q_1=\delta(q,1).
\]

Then:
\[
\boxed{\quad
\mathcal S\text{ is unavoidable}
\iff
q=\bot,\ \text{or }q_1=\bot,\ \text{or }q\text{ is not reachable from }q_1
\text{ among nondead states}.
\quad}
\]

Indeed, a safe path \(q_1\xrightarrow{y}q\) yields the clean padded word
\[
0^\ell 1y0^\ell.
\]
Conversely, reading any clean \(\ell\)-padded word from its first \(1\) to its final \(\ell\) zeroes gives such a path.

If
\[
N=\sum_{f\in\mathcal F}|f|,
\]
the automaton has \(O(N)\) states and transitions because the alphabet is binary. Its construction and the reachability test take \(O(N)\) time and space. Thus finite-language unavoidability is decidable in deterministic linear time, and an avoiding padded word is returned whenever one exists.

For the finite string sets arising from a finite graph family, this gives a complete effective criterion.

---

## 3. Complete classification of two-word languages

The finite-state criterion can be sharpened to a closed-form answer for \(|\mathcal S|=2\).

We first recall that a singleton word is unavoidable exactly when, up to reversal, it is
\[
0^k\quad(k\geq1)
\qquad\text{or}\qquad
0^k1\quad(k\geq0).
\]
This includes the word \(1\), corresponding to \(k=0\).

**Theorem 3.1.** Let \(\mathcal S=\{p,q\}\), with \(p,q\) nonempty binary words. Then \(\mathcal S\) is unavoidable if and only if at least one of the following holds.

1. One of \(p,q\) is singleton-unavoidable; that is, up to reversal it is \(0^k\) for \(k\geq1\), or \(0^k1\) for \(k\geq0\).

2. After possibly interchanging \(p,q\) and independently reversing either word,
   \[
   p=0^a10,\qquad q=0^b11
   \]
   for some \(a\geq1\) and \(b\geq0\).

In case 2, \(c=\max\{a,b,1\}\) suffices.

### Proof: necessity

Assume neither \(p\) nor \(q\) is singleton-unavoidable, but that \(\{p,q\}\) is \(c\)-unavoidable.

Consider
\[
0^c10^c.
\]
One of \(p,q\), up to reversal, occurs in this word. It cannot be all-zero, by the assumption excluding case 1. Thus, after choosing an orientation, say
\[
p=0^\alpha10^\beta.
\]
If \(\alpha=0\) or \(\beta=0\), then \(p\) is, up to reversal, \(0^k1\), again contrary to the exclusion of case 1. Therefore
\[
\alpha,\beta\geq1.
\]

Next consider
\[
0^c1^n0^c
\]
for every \(n\geq2\). Neither \(p\) nor \(p^{\mathrm{rev}}\) occurs, since the unique \(1\) in \(p\) would need zeroes immediately on both sides. Hence \(q\) or \(q^{\mathrm{rev}}\) occurs for every \(n\geq2\).

Any non-all-zero factor of \(0^\infty1^n0^\infty\) has the form
\[
0^u1^r0^v.
\]
Thus write
\[
q=0^u1^r0^v.
\]
If \(u,v\geq1\), then \(q\) occurs in \(0^\infty1^n0^\infty\) only when \(n=r\), which cannot hold for every \(n\geq2\). Therefore one of \(u,v\) is zero. Reversing \(q\) if necessary, assume \(v=0\), so
\[
q=0^u1^r.
\]
Since \(q\) occurs when \(n=2\), we have \(r\leq2\). The case \(r=1\) makes \(q=0^u1\) singleton-unavoidable. Hence
\[
q=0^u11.
\]

It remains to determine \(\alpha,\beta\). If
\[
\min\{\alpha,\beta\}\geq2,
\]
then the padded word
\[
0^c1010^c
\]
contains neither \(p\) nor \(p^{\mathrm{rev}}\): each \(1\) has only one zero on one of its two sides. It also contains neither \(q\) nor \(q^{\mathrm{rev}}\), because it has no adjacent \(1\)'s. This contradicts unavoidability.

Consequently \(\min\{\alpha,\beta\}=1\). Reversing \(p\) if necessary gives
\[
p=0^a10,\qquad a\geq1,
\]
and \(q=0^b11\) with \(b=u\geq0\), as required.

### Proof: sufficiency

Suppose
\[
p=0^a10,\qquad q=0^b11
\]
and let \(c\geq\max\{a,b,1\}\). In a \(c\)-padded word, inspect the first maximal run of \(1\)'s.

- If this run has length \(1\), it is preceded by at least \(a\) zeroes and followed by a zero, so \(0^a10\) occurs.
- If it has length at least \(2\), it is preceded by at least \(b\) zeroes, so \(0^b11\) occurs.

Thus every such word is hit. ∎

For example,
\[
\{010,011\}
\]
is \(1\)-unavoidable, although neither member is unavoidable by itself. This is the smallest genuinely collective example.

---

## 4. Extension to regular languages

The finite criterion extends to infinite languages whenever the factor-avoidance language is regular.

Let
\[
A_{\mathcal F}
=
\{w\in\Sigma^*:w\text{ contains no member of }\mathcal F\}.
\]
Suppose \(A_{\mathcal F}\) is recognized by a finite deterministic automaton with one dead state \(\bot\), all other states being accepting. This applies in particular if \(\mathcal S\) is regular, since
\[
A_{\mathcal F}
=
\Sigma^*\setminus \Sigma^*\mathcal F\Sigma^*.
\]

Assume first that every all-zero word is accepted; otherwise some \(0^k\in\mathcal F\), and unavoidability is immediate.

Let \(q_0\) be the initial state and define:

- \(C_0\): the states occurring infinitely often in the sequence
  \[
  q_0,\delta(q_0,0),\delta(q_0,0^2),\ldots;
  \]
  equivalently, the eventual zero-cycle;
- \(T_0\): the states from which arbitrarily many zeroes can safely be read:
  \[
  T_0=\{q:\delta(q,0^j)\neq\bot\text{ for all }j\geq0\}.
  \]

**Proposition 4.1.** There is an \(\mathcal F\)-clean \(c\)-padded word for every \(c\) if and only if there exist \(p\in C_0\), \(q\in T_0\), and a safe directed path
\[
p\xrightarrow{y}q
\]
whose label \(y\) contains a \(1\).

**Proof.**

If such a path exists, choose arbitrarily large \(n\) with
\[
\delta(q_0,0^n)=p.
\]
For any required padding \(c\), take \(n\geq c\), traverse \(y\), and append at least \(c\) zeroes. Membership of \(q\) in \(T_0\) guarantees that the resulting word is clean.

Conversely, suppose clean \(c\)-padded words exist for every \(c\). Write such a word as
\[
0^{i_c}x_c0^{j_c},
\qquad i_c,j_c\geq c,
\]
where \(x_c\) begins and ends with \(1\). Along an infinite subsequence, the state after \(0^{i_c}\) is a fixed state \(p\in C_0\), and the state after subsequently reading \(x_c\) is a fixed state \(q\). Since \(j_c\to\infty\), the zero-orbit of \(q\) can never enter \(\bot\), so \(q\in T_0\). The path labelled \(x_c\) contains a \(1\). ∎

Thus regular-language unavoidability is also a finite graph reachability problem. If the automaton has \(n\) nondead states and the language is unavoidable, then \(c=n\) suffices by the same pumping argument.

---

## 5. Why the unrestricted case is not reduced to the finite one

There need not be a finite unavoidable sublanguage.

Consider
\[
\mathcal T=\{01^n0:n\geq1\}.
\]
Every \(1\)-padded word contains a maximal run \(1^n\), and the zero immediately before and after that run gives a factor \(01^n0\). Hence \(\mathcal T\) is \(1\)-unavoidable.

On the other hand, no finite \(\mathcal T_0\subseteq\mathcal T\) is unavoidable. Choose \(N\) not among its finitely many exponents. Then
\[
01^N0
\]
is \(1\)-padded and contains \(01^n0\) only for \(n=N\). Thus it avoids \(\mathcal T_0\).

Consequently, a compactness argument cannot reduce arbitrary languages to finite ones. Proposition 4.1 handles this particular example because \(\mathcal T=01^+0\) is regular, but no characterization of genuinely arbitrary nonregular, unbounded languages is supplied here.

## 6. Assessment

There are no gaps in the finite-language criterion or in the two-word classification under the stated definition of padding. Thus:

- if Question 8.3 was intended only for finite string sets arising from finite graph families, Theorem 2.2 gives a complete effective characterization, with a linear-time algorithm and the sharp bound \(c\leq\max |s|\);
- independently of that interpretation, Theorem 3.1 completely settles the two-word case;
- under the literal wording allowing arbitrary languages, the problem is only partially resolved.