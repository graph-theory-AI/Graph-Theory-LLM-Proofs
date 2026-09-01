```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The proposed linear-scale coherence is genuinely much weaker: there are arbitrarily large such coherent graphs of arbitrarily large girth, so no black-box reduction to the original hypothesis is possible.",
  "would_publish": false,
  "caveats": "The extracted question omits the full statement and auxiliary hypotheses of Theorem 3.3, so the construction below is an obstruction rather than a complete counterexample to that theorem."
}
```

## Statement and notation

I use the standard two-parameter coherence convention from the pure-pairs setting: an \(n\)-vertex graph is \((x,y)\)-coherent if

1. every vertex has degree less than \(x\); and
2. there are no two disjoint anticomplete sets \(A,B\) with
   \[
   |A|,|B|\ge y.
   \]

Thus replacing
\[
(\varepsilon n^{1-c},\varepsilon n^{1-c})
\quad\text{by}\quad
(\varepsilon n^{1-c},\varepsilon n)
\]
is a weakening of the hypothesis, despite occasionally being described as a “stronger coherence” version.

I do not obtain the proposed strengthening of Theorem 3.3. I prove, however, that the two hypotheses are separated even by graphs of arbitrarily large girth. Consequently, the original theorem cannot simply be invoked after changing constants or passing to a routine induced subgraph.

## A separation theorem

### Proposition

Let \(0<c<1\), \(0<\varepsilon<1/2\), and let \(g\) be a positive integer. There are arbitrarily large graphs \(G\), with \(n=|G|\), such that

1. \(G\) is \((\varepsilon n^{1-c},\varepsilon n)\)-coherent;
2. \(G\) has girth greater than \(g\);
3. \(G\) is not \((\varepsilon n^{1-c},\varepsilon n^{1-c})\)-coherent.

In particular, proposed-coherent graphs may have arbitrarily tree-like finite-radius structure.

### Proof

Choose a constant \(d\) so large that
\[
d\varepsilon ^2>2\log 3.
\]
Consider the binomial random graph
\[
G_n\sim G(n,d/n).
\]

#### No linear anticomplete pair

Set \(k=\lceil \varepsilon n\rceil\). If there are anticomplete disjoint sets of sizes at least \(k\), then there are such sets of size exactly \(k\). The number of ordered disjoint pairs \((A,B)\) is at most \(3^n\). For a fixed pair,
\[
\Pr(A\text{ is anticomplete to }B)
  =(1-d/n)^{k^2}
  \le \exp(-dk^2/n)
  \le \exp(-d\varepsilon ^2n).
\]
Therefore
\[
\Pr(\exists\text{ such }A,B)
 \le \exp\bigl((\log 3-d\varepsilon ^2)n\bigr)
 =o(1).
\]

#### Maximum degree

For a fixed vertex, its degree is binomial with bounded mean. The standard estimate
\[
\Pr(\deg(v)\ge t)\le \left(\frac{ed}{t}\right)^t
\]
with \(t=\log n\), followed by a union bound, gives
\[
\Pr(\Delta(G_n)>\log n)=o(1).
\]
Since \(c<1\),
\[
\log n<\varepsilon n^{1-c}
\]
for all sufficiently large \(n\).

#### Large girth

For fixed \(d\) and \(g\), the numbers of cycles of lengths \(3,\dots,g\) in \(G(n,d/n)\) converge jointly to independent Poisson random variables, with respective means
\[
\frac{d^r}{2r},\qquad 3\le r\le g.
\]
This follows directly from the factorial-moment calculation for finitely many fixed cycles. Hence
\[
\Pr(\operatorname{girth}(G_n)>g)
 \longrightarrow
 q(d,g):=\exp\left(-\sum_{r=3}^{g}\frac{d^r}{2r}\right)>0.
\]

The probabilities of having a linear anticomplete pair or maximum degree greater than \(\log n\) tend to zero, while the probability of girth greater than \(g\) tends to the positive constant \(q(d,g)\). Thus, for arbitrarily large \(n\), there is a realization \(G\) satisfying all three desired properties except possibly item 3.

For item 3, put
\[
s=\left\lceil \varepsilon n^{1-c}\right\rceil .
\]
Choose any set \(A\) of \(s\) vertices. Since \(\Delta(G)\le\log n\),
\[
|A\cup N(A)|\le (1+\log n)s=o(n).
\]
For large \(n\), at least \(s\) vertices lie outside \(A\cup N(A)\). Choosing \(B\) to be any \(s\) of them gives an anticomplete pair \(A,B\). Hence \(G\) is not
\((\varepsilon n^{1-c},\varepsilon n^{1-c})\)-coherent. ∎

## A deterministic indication of the scale gap

If an \(n\)-vertex graph is \((D,Y)\)-coherent, then necessarily
\[
D>\frac{n-2Y}{Y}.
\]
Indeed, choose any \(Y\)-vertex set \(A\). If \(\Delta(G)<D\), then
\[
|A\cup N(A)|<Y+DY.
\]
Unless \(Y+DY>n-Y\), there remain \(Y\) vertices anticomplete to \(A\).

For the original parameters \(D=Y=\varepsilon n^{1-c}\), this requires roughly
\[
\varepsilon n^{1-c}\gtrsim \varepsilon^{-1}n^c.
\]
In particular, for \(c>1/2\), the original coherence condition is eventually impossible, whereas the proposed condition with \(Y=\varepsilon n\) only forces \(D\) to exceed a constant. This is another reason that changing the second parameter cannot be treated as a harmless adjustment of constants.

## Consequences for cyclic targets

The proposition has the following immediate consequence. For every fixed graph \(H\) containing a cycle and every \(\varepsilon,c\), there are arbitrarily large
\[
(\varepsilon n^{1-c},\varepsilon n)\text{-coherent}
\]
graphs containing no copy of \(H\), even as a non-induced subgraph: take the girth larger than \(|H|\).

More concretely, for \(\ell\ge6\), a graph of girth greater than \(\ell\) contains neither \(C_\ell\) nor \(\overline{C_\ell}\) as an induced subgraph. The first exclusion follows from girth; the second follows because \(\overline{C_\ell}\) contains a triangle, while the graph is triangle-free. Also,
\[
\operatorname{cong}(C_\ell)=\frac1\ell,
\]
so these examples persist for cycles of arbitrarily small positive congestion.

Thus, if the desired version of Theorem 3.3, after all its hypotheses are unpacked, would force a prescribed cyclic graph using only the proposed coherence condition, the proposition supplies a counterexample. However, the extracted problem does not reproduce Theorem 3.3’s full conclusion or its additional structural hypotheses, so I cannot responsibly assert that these graphs satisfy every premise relevant to that technical theorem.

## Remaining gap

The construction proves that:

- proposed coherence does not imply original coherence after any fixed rescaling of \(\varepsilon\);
- passing to a generic random or large induced subset cannot bridge the gap;
- bounded-degree, high-girth expansion is a real obstruction that any affirmative proof must exclude using the other hypotheses of Theorem 3.3.

What remains is to analyze the exceptional step in Section 4 against those additional hypotheses. Without the full theorem statement in the supplied extract, I do not have a complete proof or a formally verified counterexample to the exact open question.