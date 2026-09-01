```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "A clean four-vertex switching proves non-reconstructibility up to a small constant times n^{-3/4}(log n)^{1/4}, but the reconstructible side remains open.",
  "would_publish": false,
  "caveats": "This is one-sided, assumes induced radius-two balls and np/log n tending to infinity, and may overlap the source paper's unstated logarithmic lower bound."
}
```

# 1. Setup

For a graph \(G\) and \(v\in V(G)\), let
\[
B_2^G(v)=G[\{x:\operatorname{dist}_G(v,x)\le 2\}]
\]
with \(v\) distinguished as the root. The radius-two deck is the multiset
\[
\mathcal D_2(G)=\{[B_2^G(v),v]:v\in V(G)\}.
\]
A graph is 2-reconstructible if every graph with the same radius-two deck is isomorphic to it.

Write
\[
d=np,\qquad \Lambda=n^3p^4=\frac{d^4}{n}.
\]
For a fixed pair \(u,v\), \(\Lambda\) is asymptotically the expected number of length-four \(u\)-\(v\) paths. Conditional on \(uv\in E(G)\), these are the potential 5-cycles containing \(uv\). Thus \(\Lambda\) is the natural parameter at the proposed \(n^{-3/4}\) scale.

I prove the following one-sided result.

## Theorem

Let \(G\sim G(n,p)\). Suppose
\[
\frac{np}{\log n}\longrightarrow\infty
\qquad\text{and}\qquad
n^3p^4\le \frac1{100}\log n.
\]
Then, with probability tending to one, \(G\) is not 2-reconstructible.

Consequently, for every fixed
\[
0<c<10^{-1/2},
\]
if
\[
p=c\,n^{-3/4}(\log n)^{1/4},
\]
then \(G(n,p)\) is not 2-reconstructible with high probability.

The numerical constant is not optimized.

# 2. A deterministic deck-preserving switch

The main mechanism is a two-edge switch whose four endpoints are mutually invisible to radius two after the switched edges are removed.

## Lemma 2.1

Let \(H\) be a graph and let \(a,b,c,d\) be distinct vertices satisfying:

1. \(\operatorname{dist}_H(x,y)>4\) for all distinct \(x,y\in\{a,b,c,d\}\);
2. the four rooted one-balls
   \[
   (H[B_1^H(a)],a),\ (H[B_1^H(b)],b),\
   (H[B_1^H(c)],c),\ (H[B_1^H(d)],d)
   \]
   are mutually isomorphic.

Define
\[
G=H+\{ab,cd\},\qquad G'=H+\{ac,bd\}.
\]
Then
\[
[B_2^G(v),v]\cong [B_2^{G'}(v),v]
\quad\text{for every }v\in V(H).
\]
In particular,
\[
\mathcal D_2(G)=\mathcal D_2(G').
\]

### Proof

If
\[
v\notin \bigcup_{x\in\{a,b,c,d\}} B_1^H(x),
\]
then no path of length at most two from \(v\) can use one of the four switched edges. Moreover, both endpoints of a switched edge cannot already lie in \(B_2^H(v)\), since that would give an \(H\)-path of length at most four between two of \(a,b,c,d\). Hence the rooted two-ball at \(v\) is unchanged.

Consider the root \(a\). Because \(\operatorname{dist}_H(a,b)>4\),
\[
B_2^G(a)
\]
is obtained from \(B_2^H(a)\) by adjoining a disjoint copy of \(B_1^H(b)\), with its root joined to \(a\). Similarly, \(B_2^{G'}(a)\) is obtained by adjoining \(B_1^H(c)\). The two resulting rooted graphs are isomorphic by condition 2. The same argument applies at \(b,c,d\).

Finally, let \(v\in N_H(a)\). In \(B_2^G(v)\), the only new vertex reached across \(ab\) is \(b\), appearing as a boundary vertex adjacent only to \(a\) inside that two-ball. No neighbor of \(b\) can already lie in \(B_2^H(v)\), since that would yield an \(H\)-path from \(a\) to \(b\) of length at most four. In \(B_2^{G'}(v)\), \(b\) is simply replaced by an anonymous boundary vertex \(c\). Thus the two rooted balls are isomorphic. The cases \(v\in N_H(b)\), \(N_H(c)\), or \(N_H(d)\) are identical. ∎

A convenient sufficient form of condition 2 is that the four vertices have the same degree in \(H\), and each has an independent neighborhood in \(H\). Their rooted one-balls are then all stars of the same size.

# 3. Existence of a switchable quadruple in \(G(n,p)\)

Call an ordered quadruple \((a,b,c,d)\) admissible if, on putting
\[
H=G-\{ab,cd\},
\]
the following hold:

- \(G[\{a,b,c,d\}]\) has exactly the two edges \(ab,cd\);
- the four vertices have the same degree in \(H\);
- each \(N_H(x)\), \(x\in\{a,b,c,d\}\), is independent;
- all six pairwise \(H\)-distances between \(a,b,c,d\) exceed four.

An admissible quadruple satisfies Lemma 2.1.

## Lemma 3.1

Under the assumptions of the theorem, \(G(n,p)\) contains an admissible quadruple with high probability.

### Probability for a fixed quadruple

Fix distinct \(a,b,c,d\), and require that \(ab,cd\) are present while the other four pairs inside this set are absent. This has probability
\[
p^2(1-p)^4.
\]

Let
\[
q_k=\Pr(\operatorname{Bin}(n-4,p)=k).
\]
The four external degrees are independent, so the probability that they are equal is
\[
\rho_4:=\sum_k q_k^4.
\]
An elementary local central limit estimate, obtainable directly from Stirling's formula, gives
\[
\rho_4=\Theta(d^{-3/2}).
\tag{3.1}
\]

Condition on all four external degrees being \(k\). In the range carrying all but a negligible fraction of the \(q_k^4\)-mass,
\[
k=d+O(\sqrt{d\log n}).
\tag{3.2}
\]
The four neighborhoods are independent uniformly random \(k\)-subsets of the remaining \(n-4\) vertices. Since
\[
\frac{d^2}{n}=\sqrt{\frac{\Lambda}{n}}=o(1),
\]
they are pairwise disjoint with probability \(1-o(1)\).

Write these neighborhoods as \(A_1,\dots,A_4\) and put \(U=A_1\cup\cdots\cup A_4\). The required independence and distance conditions are equivalent to:

1. \(U\) is independent;
2. every \(y\notin U\cup\{a,b,c,d\}\) has neighbors in at most one of the four sets \(A_i\).

Indeed, a common vertex in two \(A_i\)'s gives a path of length two, an edge between two \(A_i\)'s gives a path of length three, and a vertex touching two distinct \(A_i\)'s gives a path of length four.

The probability that \(U\) is independent is
\[
(1-p)^{\binom{4k}{2}}
   =\exp\!\left(-O(k^2p)\right)
   =1-o(1),
\]
because
\[
k^2p=(1+o(1))\frac{d^3}{n}
     =(1+o(1))\frac{\Lambda}{d}=o(1).
\]

For a fixed \(y\notin U\), let
\[
r=1-(1-p)^k.
\]
The events that \(y\) touches \(A_i\) are independent Bernoulli variables with parameter \(r\). Thus the probability that \(y\) touches at most one \(A_i\) is
\[
h=(1-r)^4+4r(1-r)^3.
\]
Since
\[
\log h=-6r^2+O(r^3),
\]
while
\[
r=(1+o(1))kp,\qquad
nr^2=(1+o(1))\Lambda,\qquad
nr^3=o(1),
\]
independence over the choices of \(y\) gives
\[
h^{\,n-O(d)}=\exp(-6\Lambda+o(1)).
\tag{3.3}
\]

Combining (3.1)–(3.3), the probability that a fixed ordered quadruple is admissible is
\[
(1+o(1))p^2(1-p)^4\rho_4 e^{-6\Lambda}
=\Theta\!\left(p^2d^{-3/2}e^{-6\Lambda}\right).
\tag{3.4}
\]

### First moment

Let \(X\) count admissible ordered quadruples. From (3.4),
\[
\mathbb E X
 =\Theta\!\left(n^4p^2d^{-3/2}e^{-6\Lambda}\right)
 =\Theta\!\left(n^2d^{1/2}e^{-6\Lambda}\right).
\tag{3.5}
\]
Since \(\Lambda\le \frac1{100}\log n\),
\[
\mathbb E X\ge n^{1.94+o(1)}d^{1/2}\longrightarrow\infty.
\]

### Second moment

For two disjoint ordered quadruples, the preceding neighborhood calculation can be made simultaneously. The probability of an intersection between any two of the eight exposed neighborhoods is
\[
O(d^2/n).
\]
Relative to the principal factor \(e^{-12\Lambda}\), its contribution is bounded by
\[
O\!\left(\frac{d^2}{n}e^{12\Lambda}\right)
=O\!\left(\sqrt{\frac{\Lambda}{n}}\,n^{0.12}\right)
=o(1).
\]
Conditioned on all eight neighborhoods being disjoint, the two cleanliness conditions use disjoint edge variables, apart from cross-edges whose expected number is
\[
O(d^3/n)=o(1).
\]
Consequently, uniformly over disjoint quadruples,
\[
\Pr(Q_1\cap Q_2)=(1+o(1))\Pr(Q_1)\Pr(Q_2),
\tag{3.6}
\]
where \(Q_i\) denotes admissibility.

It remains to bound overlapping pairs. Suppose two ordered quadruples share \(t\) vertices. If \(1\le t\le3\), admissibility of both quadruples forces all \(8-t\) vertices in their union to have the same degree. Given any bounded collection of prescribed internal edges, the local central limit estimate gives the upper bound
\[
O\!\left(d^{-(7-t)/2}\right)
\]
for this degree coincidence.

The relevant bounds are:

\[
\begin{array}{c|c|c|c}
t & \text{union size} & \text{minimum prescribed edges}
  & \text{joint-probability upper bound}\\ \hline
1&7&4&O(p^4d^{-3})\\
2&6&3&O(p^3d^{-5/2})\\
3&5&3&O(p^3d^{-2}).
\end{array}
\]

After summing over supports and dividing by \((\mathbb EX)^2\), these contribute respectively at most
\[
O(n^{-1}e^{12\Lambda}),
\qquad
O(n^{-1}d^{-1/2}e^{12\Lambda}),
\qquad
O(n^{-2}e^{12\Lambda}),
\]
all of which tend to zero because \(e^{12\Lambda}\le n^{0.12}\).

When \(t=4\), either the two edge matchings conflict, in which case the joint event is impossible, or the two ordered quadruples represent the same admissible configuration up to ordering. Their total contribution is \(O(\mathbb EX)=o((\mathbb EX)^2)\).

Together with (3.6), this proves
\[
\operatorname{Var}X=o((\mathbb EX)^2).
\]
Hence \(X>0\) with high probability. ∎

# 4. The switched graph is genuinely nonisomorphic

The preceding construction gives a distinct labelled graph with the same deck. To rule out the possibility that it is nevertheless isomorphic to \(G\), we use a robust asymmetry property.

## Lemma 4.1

If \(d=np\) satisfies \(d/\log n\to\infty\) and \(p=o(1)\), then with high probability every nonidentity permutation \(\pi\) of \([n]\) satisfies
\[
|E(G)\triangle E(\pi G)|>4.
\]

### Proof

Suppose \(\pi\) moves \(k\ge2\) vertices. Its action on the \(\binom n2\) unordered vertex pairs moves at least
\[
\frac{k(2n-k-2)}2\ge \frac{kn}{3}
\]
pair positions for large \(n\). From the nontrivial orbits of these pair positions one can select at least \(kn/10\) disjoint adjacent pairs \(\{e,\pi(e)\}\).

For each selected pair, the two edge indicators are independent Bernoulli\((p)\) variables and disagree with probability
\[
2p(1-p)\ge p.
\]
If \(|E(G)\triangle E(\pi G)|\le4\), at most four selected pairs can disagree. A binomial lower-tail bound therefore gives
\[
\Pr\bigl(|E(G)\triangle E(\pi G)|\le4\bigr)
 \le \exp(-c k np)
\]
for an absolute \(c>0\), after absorbing a polynomial factor.

There are at most \(n^k\) permutations moving \(k\) vertices. Hence
\[
\sum_{k=2}^n n^k e^{-cknp}=o(1)
\]
because \(np/\log n\to\infty\). ∎

# 5. Completion of the theorem

With high probability, choose an admissible quadruple \((a,b,c,d)\). Put
\[
H=G-\{ab,cd\},\qquad G'=H+\{ac,bd\}.
\]
By Lemma 2.1,
\[
\mathcal D_2(G')=\mathcal D_2(G).
\]
Moreover,
\[
|E(G)\triangle E(G')|=4.
\]

If \(G'\cong G\), there would be a permutation \(\pi\) with \(G'=\pi G\). The identity permutation is impossible because \(G'\ne G\), while Lemma 4.1 rules out every nonidentity permutation. Thus \(G'\not\cong G\), proving that \(G\) is not 2-reconstructible.

# 6. Interpretation and remaining gap

The argument identifies a concrete obstruction controlled by
\[
\Lambda=n^3p^4.
\]
A present edge with no alternative path of length at most four behaves, as far as radius-two balls are concerned, like a locally detachable edge. Four suitably matched endpoints allow two such edges to be re-paired without changing any rooted radius-two card.

There are about \(n^4p^2d^{-3/2}\asymp n^2\sqrt d\) degree-compatible candidate quadruples, while demanding six clean endpoint pairs costs approximately \(e^{-6\Lambda}\). This is why the obstruction survives into a logarithmic window:
\[
\Lambda=\Theta(\log n),
\qquad\text{equivalently}\qquad
p=\Theta\!\left(n^{-3/4}(\log n)^{1/4}\right).
\]

What is not proved is the difficult converse. Once \(\Lambda\gg\log n\), clean switches of this form disappear, but absence of this particular obstruction does not imply that the radius-two deck has a unique assembly. Establishing reconstructibility would require controlling all globally consistent re-pairings of local branches, not merely two-edge switches. Thus the threshold question remains open on the reconstructible side.