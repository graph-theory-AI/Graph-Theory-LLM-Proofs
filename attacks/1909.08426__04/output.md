```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "The catalog item is an informal research expectation rather than a proposition, because neither “very few” nor “will end up” specifies a mathematical quantifier or asymptotic notion.",
  "would_publish": false,
  "caveats": "Universal, finite-exception, and density-one reformulations are distinct genuine conjectures and remain unresolved."
}
```

## 1. Statement

For a fixed graph \(H\), let \(\operatorname{IS}(H)\) denote the parameterized decision problem

\[
(G,k)\longmapsto [\,G\text{ is }H\text{-free and }\alpha(G)\ge k\,],
\]

parameterized by \(k\), where \(H\)-free means excluding \(H\) as an induced subgraph.

Let \(\mathcal C\) be the class of connected “FPT candidates” specified by the structural conditions in Figure 1 of arXiv:1909.08426. After fixing a precise bounded-error model for randomized FPT, define

\[
\mathcal T=\{H\in\mathcal C:\operatorname{IS}(H)\text{ is in randomized FPT}\}.
\]

The extracted assertion is that \(\mathcal C\setminus\mathcal T\) will be “very few.”

## 2. Why the assertion has no definite truth value

Even granting that Figure 1 defines \(\mathcal C\) unambiguously, “very few” has no specified mathematical meaning. Several natural formalizations are inequivalent:

1. **Universal tractability**
   \[
   \mathcal C\setminus\mathcal T=\varnothing.
   \]

2. **Finitely many exceptions**
   \[
   |\mathcal C\setminus\mathcal T|<\infty.
   \]

3. **A bounded number of exceptions**
   \[
   |\mathcal C\setminus\mathcal T|\leq M
   \]
   for some specified small constant \(M\).

4. **Asymptotic density zero by order**
   \[
   \lim_{N\to\infty}
   \frac{|\{H\in\mathcal C\setminus\mathcal T:|V(H)|\le N\}|}
        {|\{H\in\mathcal C:|V(H)|\le N\}|}=0.
   \]

5. A corresponding density among labeled graphs, or an order-by-order rather than cumulative density.

These notions differ substantially. An infinite exceptional set can have density zero, and a set can have different labeled and unlabeled densities. Moreover, “few” might refer to exceptional individual graphs, exceptional induced-subgraph antichains, or exceptional parametric families. None is selected in the source sentence.

The future-tense phrase “will not end up in FPT” is also epistemic rather than mathematical. The objective property is existence of an algorithm with a specified running time and error guarantee; whether such an algorithm has already been discovered is a different matter.

Consequently:

- one exceptional candidate would refute universal tractability, but not a finite-exception or density-one interpretation;
- infinitely many exceptional candidates would still not refute a density-one interpretation;
- the present lack of algorithms for \(P_7\), \(S_{1,1,3}\), and \(S_{1,2,2}\) does not show that these graphs lie outside \(\mathcal T\).

Thus the catalog item admits no proof or counterexample until a quantifier is supplied.

## 3. A useful monotonicity fact

There is nevertheless a simple rigorous structural principle.

### Lemma

If \(H_1\) is an induced subgraph of \(H_2\), then:

1. randomized FPT for \(\operatorname{IS}(H_2)\) implies randomized FPT for \(\operatorname{IS}(H_1)\);
2. \(W[1]\)-hardness of \(\operatorname{IS}(H_1)\) implies \(W[1]\)-hardness of \(\operatorname{IS}(H_2)\).

### Proof

If a graph \(G\) contains an induced \(H_2\), then that copy contains an induced \(H_1\). Hence

\[
\{H_1\text{-free graphs}\}\subseteq \{H_2\text{-free graphs}\}.
\]

An algorithm valid for all \(H_2\)-free graphs can therefore be restricted to \(H_1\)-free inputs. Conversely, the identity map embeds the problem on the \(H_1\)-free subclass into the problem on the larger \(H_2\)-free class, preserving the parameter. ∎

Thus tractable forbidden patterns form a down-set in the induced-subgraph order, while patterns for which hardness is established form an up-set. This suggests that a precise conjecture could instead concern the minimal hard candidates or maximal unresolved candidates.

## 4. A precise tractable subfamily following from the source theorem

Let \(P(a,b,c,d)\) denote the graph obtained from a four-vertex path by replacing its four vertices by cliques of orders \(a,b,c,d\), with complete adjacency between consecutive bags and no adjacency between nonconsecutive bags.

The source abstract states that, for every fixed \(t\ge1\),

\[
\operatorname{IS}\bigl(P(1,t,t,t)\bigr)
\]

is FPT. This immediately yields the following slightly more general formulation.

### Corollary

For every fixed positive integers \(a,b,c\), Maximum Independent Set parameterized by solution size is FPT on \(P(1,a,b,c)\)-free graphs.

### Proof

Set \(t=\max\{a,b,c\}\). By retaining \(a,b,c\) vertices from the three \(t\)-vertex bags,

\[
P(1,a,b,c)\le_{\mathrm{ind}}P(1,t,t,t).
\]

Therefore every \(P(1,a,b,c)\)-free graph is also \(P(1,t,t,t)\)-free. Apply the source theorem and the lemma. ∎

More generally, the same conclusion holds for every induced subgraph of some \(P(1,t,t,t)\). Likewise, the advertised randomized algorithms for dart-free and cricket-free graphs apply to the classes excluding any induced subgraph of the dart or cricket. These are exact consequences of the supplied source theorem, not a resolution of the informal belief.

The reported five-vertex dichotomy also establishes that there are no exceptional candidate graphs through order five. A finite initial segment, however, gives no conclusion under any unspecified asymptotic interpretation of “very few.”

## 5. Possible well-posed replacements

The cleanest strong replacement would be:

> **Universal candidate conjecture.** For every connected graph \(H\) satisfying the candidate conditions of Figure 1, \(\operatorname{IS}(H)\) is in randomized FPT.

This is stronger than the authors’ wording and, according to the supplied review, includes the unresolved \(P_7\)-free, \(S_{1,1,3}\)-free, and \(S_{1,2,2}\)-free cases.

A weaker alternative is:

> **Finite-exception conjecture.** Only finitely many connected candidates \(H\) fail to give randomized-FPT \(H\)-free MIS.

A density formulation would additionally have to specify labeled versus unlabeled graphs, exact-order versus cumulative counting, and how orders containing no candidates are treated.

No argument given here settles any of these formal replacements. The only definitive conclusion is that the catalog sentence itself is not a falsifiable mathematical conjecture.