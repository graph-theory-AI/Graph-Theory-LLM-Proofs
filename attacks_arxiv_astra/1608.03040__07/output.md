```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A directed triangle has fractional majority colouring weight exactly 3, refuting the quoted k<3 speculation but not determining the optimal universal constant.",
  "would_publish": false,
  "caveats": "The exact universal optimum remains unresolved here; the catalog's strict inequality needs checking against the source."
}
```

## 1. Definition and conclusion

In the majority-colouring setting, the relevant definition is that \(T\subseteq V(G)\) is **majority-stable** if
\[
|N_G^+(v)\cap T|\le \frac{d_G^+(v)}2
\qquad\text{for every }v\in T.
\]
These are precisely the permissible individual colour classes of a majority colouring. Write
\[
\chi_f^{\mathrm{maj}}(G)
=
\min\left\{
\sum_{T\in S(G)}x_T:
x_T\ge0,\quad
\sum_{\substack{T\in S(G)\\v\in T}}x_T\ge1
\text{ for every }v
\right\}.
\]

The following elementary obstruction contradicts the strict inequality quoted in the question.

**Proposition.** If \(\vec C_3\) is the directed triangle, then
\[
\chi_f^{\mathrm{maj}}(\vec C_3)=3.
\]
Consequently, every universal bound \(k\) satisfies \(k\ge3\).

## 2. Exact counterexample to \(k<3\)

Let
\[
V(\vec C_3)=\{a,b,c\},
\qquad
A(\vec C_3)=\{a\to b,\ b\to c,\ c\to a\}.
\]
This is a finite, loopless oriented graph, so the example does not depend on allowing loops or opposite arcs.

Every vertex has out-degree one. Thus, if \(v\in T\) and \(T\) is majority-stable, then
\[
|N^+(v)\cap T|\le \tfrac12.
\]
The left side is an integer, so it must be zero. In particular, a majority-stable set cannot contain both endpoints of any arc.

Every pair of distinct vertices of \(\vec C_3\) is joined by an arc. Hence
\[
S(\vec C_3)=\{\varnothing,\{a\},\{b\},\{c\}\}.
\]
The three covering constraints therefore give
\[
x_{\{a\}}\ge1,\qquad x_{\{b\}}\ge1,\qquad x_{\{c\}}\ge1,
\]
and consequently
\[
\sum_{T\in S(\vec C_3)}x_T\ge3.
\]
Conversely, assigning weight one to each singleton and zero to the empty set is feasible and has total weight three. This proves the proposition. \(\square\)

Thus even the weaker, nonuniform assertion
\[
\chi_f^{\mathrm{maj}}(G)<3
\quad\text{for every finite digraph }G
\]
is false.

## 3. A sharp special case

For completeness, the same obstruction gives the exact universal value for digraphs of maximum out-degree at most one.

**Proposition.**
\[
\sup_{\Delta^+(G)\le1}\chi_f^{\mathrm{maj}}(G)=3,
\]
where the supremum is over finite loopless digraphs.

**Proof.** Let \(H\) be the underlying simple undirected graph of \(G\). Since every out-degree is zero or one, a set is majority-stable in \(G\) exactly when it is independent in \(H\).

For each connected component \(H[U]\),
\[
|E(H[U])|
\le |A(G[U])|
\le |U|.
\]
A connected graph with at most as many edges as vertices is a tree or is unicyclic. Every such graph is properly 3-colourable: colour its cycle, if present, with at most three colours, and extend along the attached trees.

The resulting three independent colour classes, each given weight one, form a fractional majority colouring of total weight at most three. The directed triangle attains three. \(\square\)

## 4. What remains unresolved, and a wording issue

Let
\[
K_{\mathrm{maj}}=\sup_G\chi_f^{\mathrm{maj}}(G).
\]
The argument proves \(K_{\mathrm{maj}}\ge3\), but supplies no matching upper bound for unrestricted digraphs. **It does not decide whether \(K_{\mathrm{maj}}=3\) or \(K_{\mathrm{maj}}>3\).** Taking the upper bound reported in the question as given, the resulting interval is
\[
3\le K_{\mathrm{maj}}\le3.9602.
\]
That upper bound is not independently verified or reproved here.

Nevertheless, the catalog’s description of “\(k<3\) for every digraph” as an unresolved possibility cannot be correct under the majority-stable definition. The quoted inequality or its hypotheses should be checked against the source; I am not asserting that the source paper itself contains this error.

There is also a definitional omission in the extracted statement. If “stable set” means an ordinary independent set rather than a majority-stable set, then **no finite universal \(k\) exists**: orient the edges of \(K_n\) arbitrarily. Its only nonempty independent sets are singletons, so the displayed linear program has optimum \(n\). The majority-stable interpretation is therefore essential to the intended problem.