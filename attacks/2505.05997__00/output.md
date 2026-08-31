```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "As written, the claim is vacuous via the K_1 solution, and uniform FPT testing in fact yields a polynomial-time approximation with ratio o(OPT) by a timeout construction.",
  "would_publish": false,
  "caveats": "The catalog omits the required restriction on f; no claim is made about a prescribed elementary, power-type, or certifying guarantee."
}
```

## 1. Statement and ambiguity

Let
\[
h(G):=\max\{t:K_t\preccurlyeq G\}
\]
denote the Hadwiger number of \(G\).

The phrase “an \(f(\mathrm{OPT})\)-approximation” is not meaningful without a restriction on \(f\). Under the usual multiplicative convention, an algorithm returning a \(K_s\)-minor has approximation ratio \(f(h(G))\) if
\[
\frac{h(G)}{s}\le f(h(G)).
\]
For every nonempty graph, returning the trivial \(K_1\)-minor gives
\[
\frac{h(G)}1=h(G).
\]
Thus \(f(t)=t\) immediately gives a polynomial-time \(f(\mathrm{OPT})\)-approximation. In particular, if \(f\) were triply exponential and interpreted as a multiplicative factor, the claim would be weaker still.

There is, however, a substantially stronger generic consequence of the FPT minor-testing result stated in the problem.

## 2. A generic timeout lemma

### Proposition

Suppose an integer-valued graph parameter \(p(G)\) satisfies \(1\le p(G)\le |V(G)|\) on nonempty graphs, and suppose deciding whether \(p(G)\ge k\) is uniformly fixed-parameter tractable: there are a constant \(c\) and a computable function \(A\) such that the decision algorithm runs in at most
\[
A(k)n^c
\]
steps on an \(n\)-vertex graph.

Then there is a polynomial-time algorithm returning \(s\le p(G)\) such that
\[
p(G)\le F(s)
\]
for a computable function \(F\) independent of \(n\). Moreover, under the multiplicative convention, the algorithm has approximation ratio \(\rho(p(G))\) for some computable
\[
\rho(t)=o(t).
\]

### Proof

Replace \(A\), if necessary, by a computable nondecreasing majorant satisfying \(A(k)\ge k\). Handle \(n\le1\) directly. For \(n\ge2\), execute the following algorithm.

1. Set \(s=1\).
2. For \(k=2,3,\dots,n\):
   - run the FPT tester for the question \(p(G)\ge k\), but interrupt it after \(n^{c+1}\) steps;
   - if it returns YES, set \(s=k\) and continue;
   - if it returns NO, return \(s=k-1\);
   - if it times out, return \(s=k-1\).
3. If all tests through \(k=n\) return YES, return \(s=n\).

There are at most \(n\) simulations, each lasting at most \(n^{c+1}\) steps, so the total running time is \(O(n^{c+2})\).

If the test at \(k\) returns NO, all preceding tests returned YES. Hence
\[
k-1\le p(G)<k,
\]
so \(p(G)=k-1=s\).

If the test at \(k\) times out, then
\[
n^{c+1}<\operatorname{time}(G,k)\le A(k)n^c,
\]
and consequently \(n<A(k)\). Again, all preceding tests returned YES, so \(s=k-1\le p(G)\); moreover,
\[
p(G)\le n<A(k)=A(s+1).
\]
Finally, if the loop ends, then \(p(G)=n=s\).

Thus, with
\[
F(s):=\max\{s,A(s+1)\},
\]
the returned value always satisfies
\[
s\le p(G)\le F(s).
\]
This already gives an \(F\)-approximation under the convention often used for gap approximations, namely that the output \(s\) must satisfy \(p(G)\le F(s)\).

For a multiplicative formulation, define
\[
q(t):=\max\Bigl(\{1\}\cup
 \{r\in\{1,\dots,t\}:A(r+1)\le t\}\Bigr).
\]
The function \(q\) is computable, nondecreasing, and unbounded: for every fixed \(R\), one has \(q(t)\ge R\) whenever
\[
t\ge \max\{R,A(R+1)\}.
\]

The algorithm always outputs \(s\ge q(p(G))\). This is immediate when \(s=p(G)\). In the timeout case, writing \(t=p(G)\), we have \(t<A(s+1)\). If \(q(t)>s\), monotonicity of \(A\) would give
\[
A(s+1)\le A(q(t)+1)\le t,
\]
a contradiction.

Therefore, setting
\[
\rho(t):=\frac{t}{q(t)},
\]
we obtain
\[
\frac{p(G)}s\le \frac{p(G)}{q(p(G))}=\rho(p(G)).
\]
Since \(q(t)\to\infty\),
\[
\frac{\rho(t)}t=\frac1{q(t)}\longrightarrow0.
\]
Thus \(\rho(t)=o(t)\).

If one insists that approximation ratios be nondecreasing, replace \(\rho\) by
\[
\widehat\rho(t):=\max_{1\le u\le t}\rho(u).
\]
It remains true that \(\widehat\rho(t)=o(t)\): once \(q(u)\ge M\) for all \(u\ge T_M\),
\[
\widehat\rho(t)\le
\max\left\{\max_{u<T_M}\rho(u),\,\frac{t}{M}\right\},
\]
and then let \(M\to\infty\). ∎

## 3. Application to complete minors

Apply the proposition with \(p(G)=h(G)\). The premise supplied in the problem is precisely that testing whether \(K_k\preccurlyeq G\) is uniformly FPT in \(k\). Also \(h(G)\le n\). Consequently there is, formally, a polynomial-time algorithm which returns \(s\le h(G)\) with all of the following equivalent qualitative guarantees:

1. \(h(G)\le F(s)\) for some computable \(F\) independent of \(n\);
2. \(s\ge q(h(G))\) for some computable unbounded \(q\);
3. the multiplicative approximation ratio is \(\rho(h(G))\) for some computable \(\rho(t)=o(t)\).

The algorithm need not evaluate \(A\), \(F\), or \(q\); it only runs the fixed FPT machine with a polynomial step counter.

### Constructing the minor model

The catalog asks for the size, so a decision tester suffices. If an actual \(K_s\)-model is required, decision can be made constructive without losing FPT running time.

Starting from a graph \(H\) known to contain \(K_k\):

- delete a vertex \(v\) whenever the tester says \(H-v\) still contains \(K_k\);
- contract an edge \(e\) whenever the tester says \(H/e\) still contains \(K_k\);
- repeat until neither operation is possible, recording the preimages of contracted vertices.

At termination, take any \(K_k\)-model in the remaining graph. No vertex can lie outside its branch sets, since such a vertex could be deleted. No branch set can contain more than one vertex, since an internal edge of that connected branch set could be contracted. Hence the remaining graph has exactly \(k\) vertices and contains all edges of \(K_k\). The recorded contraction preimages give a model in the original graph. Only polynomially many oracle calls are needed, so the tester remains FPT with a possibly larger fixed polynomial exponent.

## 4. What remains genuinely open

The timeout guarantee can be extraordinarily weak: \(q(t)\) may grow more slowly than any practically useful explicit function. It does not provide, for example,

\[
s\ge h(G)^\varepsilon,\qquad
s\ge \operatorname{polylog} h(G),
\]
a constant-factor approximation, or even a prescribed elementary relation between \(s\) and \(h(G)\).

Nor does a timeout furnish an independently verifiable structural certificate that no much larger complete minor exists.

Thus a meaningful open problem could ask for a prescribed power-type ratio, an explicit elementary gap function, or a certifying algorithm. None of those requirements appears in the catalog statement. As written, the statement is either trivial under the ordinary multiplicative interpretation or follows qualitatively from the already-stated FPT theorem under the unbounded-gap interpretation.