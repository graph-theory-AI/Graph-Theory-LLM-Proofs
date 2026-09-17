```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under binary end-padding, I classify all unavoidable one-run languages and prove that unavoidability for context-free input languages is Σ⁰₂-complete.",
  "would_publish": false,
  "caveats": "The padding definition is made explicit but has not been independently checked in the source; the unrestricted structural characterization and novelty remain unsettled."
}
```

# 1. Convention and scope

The supplied excerpt does not give the formal definition of “\(c\)-padded.” I use the convention from the previous attempt:

> A \(c\)-padded word is a finite binary word containing at least one \(1\), with at least \(c\) zeroes at each end.

Here \(c\geq 1\). The singleton examples alone do not logically force this definition, so the results below are conditional on it being the intended definition.

Write \(\Sigma=\{0,1\}\), and put
\[
\mathcal F=\mathcal S\cup\mathcal S^{\mathrm{rev}}.
\]
Thus \(\mathcal S\) is unavoidable if some padding constant \(c\) forces a factor belonging to \(\mathcal F\).

I obtain two results beyond the finite-state approach:

1. A complete structural classification for languages whose words have at most one maximal block of \(1\)'s, including all their inclusion-minimal unavoidable languages.
2. A sharp computability classification: with a context-free grammar as input, deciding whether any padding constant works is \(\Sigma^0_2\)-complete.

All words below are nonempty. If the empty word is permitted, a language containing it is trivially unavoidable.

# 2. Complete classification of one-run languages

Call a word **one-run** if it has at most one maximal block of \(1\)'s. Such a word is either all-zero or has the form
\[
0^a1^r0^b,\qquad a,b\geq 0,\quad r\geq 1.
\]

## Theorem 1

Let \(\mathcal S\) consist of one-run words. Then \(\mathcal S\) is unavoidable if and only if it contains, up to independently reversing individual words, one of the following families.

### Type I: an all-zero singleton
\[
\{0^a\},\qquad a\geq 1.
\]

### Type II: a finite initial-run cover
\[
\{0^a1^r\}\ \cup\
\{0^{b_n}1^n0:1\leq n<r\},
\]
where
\[
r\geq 1,\qquad a\geq 0,\qquad b_n\geq 1.
\]

### Type III: a bounded infinite run cover
\[
\mathcal S_f=\{0^{f(n)}1^n0:n\geq 1\},
\]
where \(f:\mathbb N_{\geq1}\to\mathbb N_{\geq1}\) is bounded.

Moreover:

- these are precisely the inclusion-minimal unavoidable languages within the one-run class;
- their least positive padding constants are, respectively,
  \[
  a,\qquad
  \max\bigl(\{1,a\}\cup\{b_n:1\leq n<r\}\bigr),
  \qquad
  \max_{n\geq1}f(n).
  \]

### Proof: sufficiency

Type I is immediate.

For Type II, take
\[
c=\max\bigl(\{1,a\}\cup\{b_n:1\leq n<r\}\bigr).
\]
In a \(c\)-padded word, let the first maximal run of \(1\)'s have length \(n\).

- If \(n\geq r\), the word contains \(0^a1^r\).
- If \(n<r\), that first run is preceded by at least \(b_n\) zeroes and followed by a zero, so the word contains \(0^{b_n}1^n0\).

For Type III, take \(c=\max_n f(n)\). If the first maximal run of \(1\)'s has length \(n\), it gives a factor \(0^{f(n)}1^n0\).

Independent reversal of the listed forbidden words does not affect these arguments, since the avoidance condition already includes reversals.

### Proof: necessity

Suppose that \(\mathcal S\) is \(c\)-unavoidable.

If \(\mathcal S\) contains an all-zero word, it contains a Type I family. Assume henceforth that it does not.

For each \(n\geq1\), consider the palindrome
\[
B_{c,n}=0^c1^n0\,1^n0^c.
\]
Some word of \(\mathcal F\) occurs in \(B_{c,n}\).

Because forbidden words are one-run and are not all-zero, any such occurrence has one of the following two forms, after reversal if necessary:

1. A word
   \[
   0^a1^r,\qquad 0\leq a\leq c,\quad 1\leq r\leq n.
   \]
2. A word
   \[
   0^a1^n0,\qquad 1\leq a\leq c.
   \]

Indeed, a factor having zeroes on both sides of its \(1\)-run must use an entire run \(1^n\). One side of that run is the single zero separating the two runs, so one of its two zero-blocks has length exactly one.

Now split into two cases.

**There is a one-sided word in \(\mathcal F\).**  
Choose the least \(r\) for which
\[
0^a1^r\in\mathcal F
\]
for some \(a\geq0\), and choose one such word.

For every \(n<r\), the first possibility above is excluded by the minimality of \(r\). Hence
\[
0^{b_n}1^n0\in\mathcal F
\]
for some \(1\leq b_n\leq c\). Together with the chosen one-sided word, these form a Type II family.

**There is no one-sided word in \(\mathcal F\).**  
For every \(n\), the second possibility must hold. Choose
\[
f(n)=\min\{a\geq1:0^a1^n0\in\mathcal F\}.
\]
Then \(f(n)\leq c\) for every \(n\). These words form a Type III family.

This proves necessity.

### Minimality and optimal padding

Each listed family is inclusion-minimal.

- This is immediate for Type I.
- In Type II, deleting \(0^{b_n}1^n0\) leaves every word
  \[
  0^c1^n0^c
  \]
  avoiding the remaining family. Deleting \(0^a1^r\) gives the same conclusion with run length \(r\).
- In Type III, deleting the word indexed by \(n\) leaves \(0^c1^n0^c\) avoiding the remaining family for every \(c\).

Conversely, the necessity argument extracts one of these unavoidable subfamilies from every unavoidable one-run language. Inclusion-minimality therefore forces equality with that extracted family.

The same single-run test words show that the displayed padding constants cannot be decreased. ∎

## Consequences

This settles arbitrary infinite, potentially nonregular languages in a substantial special class.

In particular:

- Within the one-run class, words \(0^a1^r0^b\) with \(a,b\geq2\) can be deleted without changing whether the language is unavoidable.
- Every bounded positive function \(f\), whether computable or not, gives an infinite inclusion-minimal unavoidable language \(\mathcal S_f\).
- Consequently, finite-subfamily compactness fails very strongly: every proper sublanguage of \(\mathcal S_f\) is avoidable.

The singleton cases are exactly \(0^a\) and, up to reversal, \(0^a1\), as quoted in the question.

# 3. Unavoidability for context-free languages

The next result concerns an effective presentation of an infinite language, rather than an unrestricted set of words.

## Theorem 2

Given a context-free grammar \(G\) over \(\{0,1\}\), the property
\[
\exists c\geq1\quad
\text{every \(c\)-padded word has a factor in }
L(G)\cup L(G)^{\mathrm{rev}}
\]
is \(\Sigma^0_2\)-complete under computable many-one reductions.

Hardness holds even when the input language is reversal-closed and every forbidden word:

- begins and ends with \(00\);
- contains at least one \(1\);
- has no occurrence of \(00\) between its first and last \(1\).

Here \(\Sigma^0_2\) is the arithmetical-hierarchy class of properties expressible as
\[
\exists b\,\forall t\,R(b,t)
\]
with \(R\) computable.

## 3.1 Upper bound

For a fixed grammar \(G\), padding \(c\), and finite word \(w\), one can decide whether:

- \(w\) is \(c\)-padded; and
- some factor \(u\) of \(w\) satisfies \(u\in L(G)\) or \(u^{\mathrm{rev}}\in L(G)\).

There are finitely many factors to check, and context-free membership is decidable. Thus unavoidability has the form
\[
\exists c\,\forall w\,P(G,c,w)
\]
with \(P\) computable. It belongs to \(\Sigma^0_2\).

The lower bound will use a padding construction that turns **cofiniteness** into **unavoidability**.

## 3.2 A padding construction with an exact criterion

Let
\[
\mathcal R
=
\{x:x\text{ begins and ends with }1
       \text{ and contains no }00\}.
\]
Equivalently,
\[
\mathcal R=1(1\mid01)^*.
\]

Define a fixed language
\[
\mathcal C
=
\{0^{|x|+2}x00:x\in\mathcal R\}.
\]
For any \(A\subseteq\mathcal R\), put
\[
\mathcal S_A
=
\{00x00:x\in A\}\ \cup\ \mathcal C.
\]

The first part supplies patterns requiring only two leading zeroes; the second supplies a pattern for every core \(x\), but requires \(|x|+2\) leading zeroes.

### Lemma 3

For every \(c\geq2\),
\[
\mathcal S_A\text{ is \(c\)-unavoidable}
\quad\Longleftrightarrow\quad
\mathcal R\setminus(A\cup A^{\mathrm{rev}})
\subseteq
\{x:|x|\leq c-2\}.
\]

Consequently,
\[
\boxed{\quad
\mathcal S_A\text{ is unavoidable}
\iff
\mathcal R\setminus(A\cup A^{\mathrm{rev}})
\text{ is finite}.
\quad}
\]

#### Proof

Suppose first that every missing core has length at most \(c-2\).

Take a \(c\)-padded word \(w\). Starting at its first \(1\), continue until just before the first subsequent zero-block of length at least two. Such a block exists because the terminal padding has length at least two. The resulting core \(x\) belongs to \(\mathcal R\), and \(w\) contains
\[
0^c x00.
\]

If \(x\in A\cup A^{\mathrm{rev}}\), this gives a forbidden factor \(00x00\), up to reversal. Otherwise \(|x|+2\leq c\), so it gives the forbidden factor
\[
0^{|x|+2}x00\in\mathcal C.
\]

Conversely, suppose
\[
x\in\mathcal R\setminus(A\cup A^{\mathrm{rev}})
\quad\text{and}\quad
|x|+2>c.
\]
Consider
\[
w=0^c x0^c.
\]

Every forbidden word has at least two zeroes on both sides of its core. Since \(x\) has no internal \(00\), any forbidden factor of \(w\) would have to use exactly \(x\) as its core.

It cannot come from the first part of \(\mathcal S_A\), even after reversal, because \(x\notin A\cup A^{\mathrm{rev}}\). It cannot come from \(\mathcal C\), or its reverse, because neither boundary has \(|x|+2\) zeroes. Thus \(w\) avoids the language.

Finally, no \(\mathcal S_A\) is \(1\)-unavoidable: the word \(010\) avoids it. Over a finite alphabet, bounded word length is equivalent to finiteness, proving the last assertion. ∎

### Preservation of context-freeness

If \(A\) is context-free, then \(\mathcal S_A\) is context-free.

Only the assertion about \(\mathcal C\) needs checking. The grammar
\[
T\longrightarrow 01\mid 0T0\mid 0T1
\]
generates
\[
L(T)=\{0^{|x|}x:x\in1\Sigma^*\}.
\]
Therefore
\[
\mathcal C
=
\bigl(00L(T)00\bigr)\cap\bigl(0^*\mathcal R00\bigr).
\]
The decomposition at the first \(1\) is unique, so this equality is exact. Context-free languages are effectively closed under concatenation with fixed words and intersection with regular languages.

## 3.3 Encoding cofiniteness while neutralizing reversal

Let \(L\subseteq\{a,b\}^*\) be a context-free language. Define
\[
\rho(a)=10,\qquad \rho(b)=110,
\]
and
\[
E(u)=1110\,\rho(u)\,1111.
\]
The code language
\[
K=E(\{a,b\}^*)
  =1110(10\mid110)^*1111
\]
is a regular subset of \(\mathcal R\), and \(E\) is injective.

Every word of \(K\) starts with a run of exactly three \(1\)'s and ends with a run of exactly four. Hence
\[
K\cap K^{\mathrm{rev}}=\varnothing.
\]

Set
\[
A_L=
\bigl(\mathcal R\setminus(K\cup K^{\mathrm{rev}})\bigr)
\ \cup\ E(L).
\]
This is context-free, effectively from a grammar for \(L\). Moreover,
\[
\mathcal R\setminus(A_L\cup A_L^{\mathrm{rev}})
=
E(\{a,b\}^*\setminus L)
\ \cup\
E(\{a,b\}^*\setminus L)^{\mathrm{rev}}.
\]
Thus Lemma 3 gives
\[
\boxed{\quad
\mathcal S_{A_L}\text{ is unavoidable}
\iff
\{a,b\}^*\setminus L\text{ is finite}.
\quad}
\]

This is an effective reduction from cofiniteness of context-free languages to padded unavoidability.

Replacing \(\mathcal S_{A_L}\) by its reversal closure changes neither the property nor context-freeness. Every resulting word has the additional properties asserted in Theorem 2.

For completeness, the required hardness of context-free cofiniteness is proved next.

## 3.4 Why context-free cofiniteness is \(\Sigma^0_2\)-complete

### Lemma 4

Given a context-free grammar \(G\) over a fixed binary alphabet, the property
\[
\Sigma^*\setminus L(G)\text{ is finite}
\]
is \(\Sigma^0_2\)-complete.

#### Upper bound

It is equivalent to
\[
\exists N\,\forall w\,
\bigl(|w|<N\ \text{or}\ w\in L(G)\bigr),
\]
whose matrix is computable.

#### Hardness source

Let
\[
\mathrm{FIN}=\{e:W_e\text{ is finite}\},
\]
where \(W_e\) is the computably enumerable set with index \(e\).

Here is a direct verification of its \(\Sigma^0_2\)-hardness. Given
\[
e\in B\iff \exists b\,\forall t\,R(e,b,t)
\]
with \(R\) computable, define
\[
g_e(s)=
\min\{b\leq s:\forall t\leq s,\ R(e,b,t)\},
\]
using \(s+1\) when the set is empty. Enumerate all integers at most \(g_e(s)\) at stage \(s\).

If a witness \(b\) exists, \(g_e\) is bounded. If none exists, every finite collection of candidates is eventually refuted, so \(g_e(s)\to\infty\). The enumerated set is therefore finite exactly when \(e\in B\). The upper bound for \(\mathrm{FIN}\) is immediate from stagewise enumeration.

#### From finite enumeration to a cofinite context-free language

Given \(e\), construct a deterministic Turing machine \(M_e\) accepting precisely the unary encodings of elements of \(W_e\).

Use **canonical finite configurations**:

- the tape is one-sided;
- a configuration ends at the rightmost nonblank cell or the head position, whichever is farther right;
- no arbitrary trailing blanks are permitted;
- there is exactly one head/state marker.

Canonical configurations form a regular language. Each step changes their length by at most one. Arrange that acceptance halts the computation.

Encode accepting histories with alternating reversals:
\[
C_0\#C_1^{\mathrm{rev}}\#C_2\#C_3^{\mathrm{rev}}\#\cdots.
\]
Let \(H_e\) be the language of valid accepting histories. Determinism and canonical encoding give exactly one history for each accepted unary input. Consequently,
\[
|H_e|<\infty\iff |W_e|<\infty.
\]

The complement of \(H_e\) is context-free, effectively in \(e\). Here are the details needed for that assertion.

- Malformed configuration sequences, invalid initial configurations, and nonaccepting final configurations form regular languages.
- Otherwise, an invalid history has an incorrect adjacent transition. A pushdown automaton can nondeterministically select such a pair, push its first configuration, and compare it with the oppositely oriented second configuration.
- Legal one-step transitions have a regular padded-convolution description: away from the head and its neighboring cell, symbols must agree, and the local change is one of finitely many machine instructions.
- Length differences exceeding one are automatically illegal. For differences \(-1,0,1\), the pushdown automaton uses one of finitely many alignment cases, verifies the alignment at the pair's end, and runs finite control checking the complement of the legal-transition relation.

Both parities of adjacent pairs are handled by finite control. Thus the language containing an incorrect adjacent pair is context-free, and so is the union of all the invalid-history cases.

The canonical-configuration requirement matters: allowing arbitrary trailing blanks would introduce infinitely many encodings of a single computation and would destroy the finiteness equivalence.

Finally, encode the finite history alphabet by an injective fixed-length binary code \(h\). If \(B_e\) is the context-free language of invalid histories over that alphabet \(\Gamma_e\), then
\[
L_e=
h(B_e)\ \cup\
\bigl(\{a,b\}^*\setminus h(\Gamma_e^*)\bigr)
\]
is effectively context-free, and
\[
\{a,b\}^*\setminus L_e=h(H_e).
\]
Hence
\[
L_e\text{ is cofinite}\iff W_e\text{ is finite}.
\]
This proves the lemma. ∎

Lemma 4, the reduction in Section 3.3, and the upper bound in Section 3.1 complete the proof of Theorem 2. ∎

# 4. A further consequence for very simple decidable languages

The computability obstruction is already visible in the Type III languages of Theorem 1, without complicated individual patterns.

Let \(W_{e,n}\) be the finite set enumerated during the first \(n\) steps of program \(e\), and define
\[
f_e(n)=1+|W_{e,n}|.
\]
Membership in
\[
\mathcal S_{f_e}
=
\{0^{f_e(n)}1^n0:n\geq1\}
\]
is uniformly decidable by bounded simulation. Nevertheless,
\[
\mathcal S_{f_e}\text{ is unavoidable}
\iff
f_e\text{ is bounded}
\iff
W_e\text{ is finite}.
\]
Thus even this uniformly decidable family of one-run, factor-antichain languages has a \(\Sigma^0_2\)-complete unavoidability index set.

# 5. What remains unresolved

These results do **not** characterize arbitrary unavoidable languages.

The structural theorem covers all one-run languages, but not forbidden words having two or more separated \(1\)-runs. The context-free theorem is a complexity classification, not a substitute for a structural answer to Question 8.3.

It does establish a limitation on the previous finite-state direction:

> No algorithm can take an arbitrary context-free grammar and decide whether some padding constant works.

This does not rule out a noneffective structural characterization, and it does not conflict with algorithms for finite or regular languages.

Subject to the stated padding convention, the arguments above are complete. What remains unverified is the match with the source’s omitted definition and the novelty of these partial results; no claim is made to have resolved the original unrestricted question.