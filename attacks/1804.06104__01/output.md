```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "Without a formal definition of “probabilistic methods” and “on their own,” the stated methodological forecast has no determinate mathematical truth value.",
  "would_publish": false,
  "caveats": "This does not settle the Δ+2 conjecture; only a narrow obstruction to the canonical direct LLL setup is proved below."
}
```

## 1. The mathematical conjecture behind the statement

For an edge-colouring \(\varphi:E(G)\to[q]\), write
\[
S_\varphi(v)=\{\varphi(e):e\ni v\}.
\]
The colouring is proper if incident edges receive different colours, and it is adjacent vertex distinguishing if
\[
S_\varphi(u)\ne S_\varphi(v)
\qquad\text{for every }uv\in E(G).
\]
An isolated-edge component must be excluded, since its two endpoints necessarily see the same singleton colour set.

The underlying Zhang–Liu–Wang conjecture, in the version relevant here, is the well-defined assertion
\[
\chi'_a(G)\le \Delta(G)+2
\]
for finite simple graphs without isolated edges and with \(\Delta(G)\ge 3\).

The catalog item is not this conjecture. It is the methodological prediction that, assuming the conjecture is true, “probabilistic methods such as the Local Lemma or entropy compression will probably not be enough on their own” to prove it.

## 2. Why the catalog statement is not a proposition

At least four expressions have no formal definition:

1. “probabilistic methods”;
2. “such as,” which leaves the class of methods open-ended;
3. “on their own,” especially for proofs combining random choices with structural reductions;
4. “probably,” for which no probability space on future proofs or methods is specified.

The distinction between probabilistic and deterministic proofs is also not invariant under reformulation. For a fixed graph \(G\) and palette size \(q\), let \(N_q(G)\) be the number of valid adjacent-distinguishing proper edge-colourings. If \(\Phi\) is a uniformly random map \(E(G)\to[q]\), then
\[
\Pr(\Phi\text{ is valid})=\frac{N_q(G)}{q^{|E(G)|}}.
\]
Consequently,
\[
N_q(G)>0
\quad\Longleftrightarrow\quad
\Pr(\Phi\text{ is valid})>0.
\]
Thus every finite colouring-existence statement has an equivalent positive-probability formulation. This equivalence does not prove that the probability is positive—it merely shows that “probabilistic” cannot be a semantic property of the conclusion. Likewise, a deterministic construction can be viewed as a randomized algorithm with a degenerate distribution.

To turn the authors’ suspicion into a theorem one would need, for example, to specify:

- a particular distribution on partial or complete colourings;
- a fixed collection of bad events and dependency graph;
- a particular Local Lemma criterion;
- or a formally defined class of bounded-radius resampling/entropy-compression algorithms.

No such model is present. Hence there is no statement here that can be proved or refuted in the ordinary graph-theoretic sense.

## 3. A rigorous barrier for one canonical LLL formulation

There is nevertheless an elementary obstruction to the most direct independent-colouring application of the standard asymmetric Local Lemma.

### Proposition

Let \(G\) be a finite simple \(\Delta\)-regular graph with \(\Delta\ge3\), and put \(q=\Delta+2\). Independently and uniformly assign each edge a colour in \([q]\). For each pair of incident edges \(e,f\), let
\[
B_{e,f}=\{X_e=X_f\}.
\]
Give these events their natural variable-dependency graph: two events are adjacent when their defining pairs share an edge-colour variable.

Then there are no numbers \(x_B\in(0,1)\) satisfying the standard asymmetric Local Lemma inequalities
\[
\Pr(B)\le x_B\prod_{C\in\Gamma(B)}(1-x_C)
\]
for all conflict events \(B\). Thus this canonical product-form LLL cannot prove even properness with \(\Delta+2\) colours.

### Proof

Fix an edge \(e=uv\). There are
\[
m=(d(u)-1)+(d(v)-1)=2\Delta-2
\]
edges \(f\ne e\) incident with \(u\) or \(v\). The corresponding events
\[
\mathcal K_e=\{B_{e,f}:f\text{ is incident with }e\}
\]
form a clique in the variable-dependency graph, since all involve \(X_e\). Each has probability
\[
p=\frac1q=\frac1{\Delta+2}.
\]

If the global LLL inequalities held, then, after discarding factors corresponding to neighbours outside this clique, there would be \(x_1,\dots,x_m\in(0,1)\) such that
\[
p\le x_i\prod_{j\ne i}(1-x_j)
\qquad (1\le i\le m).
\]
Multiplying these inequalities gives
\[
p^m
 \le \prod_{i=1}^m x_i(1-x_i)^{m-1}.
\]
For \(0<x<1\),
\[
x(1-x)^{m-1}\le \frac{(m-1)^{m-1}}{m^m},
\]
with equality at \(x=1/m\). Hence a necessary condition is
\[
p\le \frac{(m-1)^{m-1}}{m^m}
 =\frac1m\left(1-\frac1m\right)^{m-1}.
\]

For \(\Delta=3\), this would require
\[
\frac15\le \frac{27}{256},
\]
which is false. For \(\Delta\ge4\), we have
\[
q=\Delta+2\le 2\Delta-2=m,
\]
so
\[
p=\frac1q\ge\frac1m>
\frac1m\left(1-\frac1m\right)^{m-1}.
\]
Again the necessary condition fails. This covers every \(\Delta\ge3\). \(\square\)

For \(\Delta\ge4\), there is an even stronger dependency-data obstruction. The clique above has \(m\ge q\) events of probability \(1/q\). On a \(q\)-point probability space, \(q\) singleton events of probability \(1/q\) can cover the whole space; any remaining clique events may duplicate one of them. Therefore probabilities and the complete dependency graph alone cannot guarantee a common avoiding outcome. Any successful argument in this formulation must exploit additional structure of the equality events, a different distribution, or a different event encoding.

## 4. Scope of the partial result

The proposition is deliberately narrow. It does not rule out:

- a lopsided or otherwise refined dependency relation;
- sampling from proper edge-colourings rather than independent edge colours;
- random alterations starting from a deterministic proper colouring;
- different bad events or event splitting;
- adaptive resampling or entropy compression;
- a proof mixing probabilistic and structural arguments.

Indeed, for a \(\Delta\)-regular graph properly coloured from a \((\Delta+2)\)-palette, every vertex misses exactly two colours. If
\[
M_\varphi(v)=[\Delta+2]\setminus S_\varphi(v),
\]
then the remaining distinguishing condition is simply
\[
M_\varphi(u)\ne M_\varphi(v)
\qquad\text{for every }uv\in E(G).
\]
A random process operating directly on proper colourings therefore bypasses the conflict-event obstruction above.

## 5. Conclusion and gaps

The catalog item should be classified as an informal research heuristic, not an open graph-theoretic conjecture. A precise restricted statement about the direct independent-colouring/product-LLL formulation is proved above, but it gives no lower bound for all Local Lemma arguments and no limitation theorem for entropy compression.

The actual \(\Delta+2\) adjacent vertex distinguishing edge-colouring conjecture remains untouched by this analysis.