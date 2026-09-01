```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains open, but a maximum-clique decomposition shows that goodness is preserved when an isolated vertex or isolated edge is adjoined, yielding explicit polynomial bounds for matchings and for a star together with any number of isolated vertices and edges.",
  "would_publish": false,
  "caveats": "This is an elementary special-case reduction; it does not address P5 or the general problem of combining nontrivial tree components, and novelty was not checked."
}
```

## Statement and conventions

All graphs are finite and simple, and “\(H\)-free” means having no induced subgraph isomorphic to \(H\). Write \(\sqcup\) for disjoint union. For a fixed graph \(H\), set
\[
b_H(w)=\sup\{\chi(G):G\text{ is induced-}H\text{-free and }\omega(G)\leq w\}.
\]
The conjecture asks whether \(b_H(w)\) is bounded by a polynomial in \(w\) for every forest \(H\).

The following closure lemma gives a limited but completely rigorous reduction.

## 1. Adjoining isolated vertices and isolated edges

### Theorem 1

Let \(F\) be a fixed graph, and suppose every induced-\(F\)-free graph \(G\) satisfies
\[
\chi(G)\leq p(\omega(G)),
\]
where \(p\geq 1\) is nondecreasing. Then:

1. Every induced-\((F\sqcup K_1)\)-free graph \(G\) satisfies
   \[
   \chi(G)\leq \omega(G)\,p(\omega(G)).
   \]

2. Every induced-\((F\sqcup K_2)\)-free graph \(G\) satisfies
   \[
   \chi(G)\leq \omega(G)+\binom{\omega(G)}2p(\omega(G)).
   \]

Consequently, goodness is preserved by adjoining any number of components isomorphic to \(K_1\) or \(K_2\).

Here there is no loss in assuming \(p\) nondecreasing and at least one: any polynomial bound can be enlarged to \(C(1+w)^d\).

### Proof for \(F\sqcup K_1\)

Let \(G\) be \((F\sqcup K_1)\)-free, let \(w=\omega(G)\), and choose a maximum clique
\[
Q=\{q_1,\dots,q_w\}.
\]
Every vertex \(x\notin Q\) is nonadjacent to at least one member of \(Q\), since otherwise \(Q\cup\{x\}\) would be a larger clique. Choose one such index \(i(x)\), and put
\[
X_i=\{x\notin Q:i(x)=i\}.
\]

The vertex \(q_i\) is anticomplete to \(X_i\). Moreover, \(G[X_i]\) is \(F\)-free: an induced copy of \(F\) in \(X_i\), together with \(q_i\), would induce \(F\sqcup K_1\). Therefore
\[
\chi(G[X_i])\leq p(w).
\]
Since \(q_i\) is anticomplete to \(X_i\), it can be included without increasing the chromatic number:
\[
\chi(G[X_i\cup\{q_i\}])\leq p(w).
\]
Using disjoint palettes for the \(w\) sets gives
\[
\chi(G)\leq wp(w).
\]

### Proof for \(F\sqcup K_2\)

Again choose a maximum clique \(Q=\{q_1,\dots,q_w\}\). For \(x\notin Q\), let
\[
D(x)=\{i:xq_i\notin E(G)\}.
\]
This set is nonempty.

For vertices with \(D(x)=\{i\}\), put \(x\) in \(A_i\). The set
\[
A_i\cup\{q_i\}
\]
is stable. Indeed, every member of \(A_i\) is adjacent to all of \(Q\setminus\{q_i\}\). If two vertices \(x,y\in A_i\) were adjacent, then
\[
(Q\setminus\{q_i\})\cup\{x,y\}
\]
would be a clique of size \(w+1\).

For every \(x\) with \(|D(x)|\geq2\), choose a pair \(\{i,j\}\subseteq D(x)\), and put \(x\) in \(B_{ij}\). Every vertex of \(B_{ij}\) is anticomplete to the edge \(q_iq_j\). Thus \(G[B_{ij}]\) is \(F\)-free: otherwise an induced \(F\) in \(B_{ij}\), together with \(q_iq_j\), would induce \(F\sqcup K_2\). Hence
\[
\chi(G[B_{ij}])\leq p(w).
\]

The \(w\) stable sets \(A_i\cup\{q_i\}\) use \(w\) colors, and the at most \(\binom w2\) sets \(B_{ij}\) use at most \(\binom w2p(w)\) further colors. Therefore
\[
\chi(G)\leq w+\binom w2p(w).
\]
This proves the theorem. \(\square\)

### Consequence for a possible minimal counterexample

Let \(F^\circ\) be obtained from a forest \(F\) by deleting all components of order one or two. If \(F^\circ\) is nonempty and good, then \(F\) is good by repeated application of Theorem 1. Forests all of whose components have order at most two are also good, starting from \(K_1\) or \(K_2\).

Thus the full conjecture is equivalent to its restriction to forests all of whose components have at least three vertices. Equivalently, any counterexample can be stripped of all isolated vertices and isolated edges while remaining a counterexample.

If \(p\) has degree \(d\), adjoining a \(K_1\) increases the displayed degree by at most one, and adjoining a \(K_2\) increases it by at most two.

## 2. Explicit bounds for stars and related forests

Let \(S_t=K_{1,t}\), where \(t\geq1\).

### Proposition 2

Every induced-\(S_t\)-free graph \(G\) satisfies
\[
\chi(G)\leq \binom{\omega(G)+t-2}{t-1}.
\]

### Proof

Set \(w=\omega(G)\). For every vertex \(v\), the neighborhood \(N(v)\) contains no stable set of size \(t\), since such a stable set together with \(v\) would induce \(K_{1,t}\). Also,
\[
\omega(G[N(v)])\leq w-1.
\]

The elementary Ramsey bound
\[
R(t,w)\leq \binom{t+w-2}{t-1}
\]
therefore gives
\[
\deg(v)<R(t,w)\leq \binom{t+w-2}{t-1}.
\]
Thus
\[
\Delta(G)+1\leq \binom{t+w-2}{t-1},
\]
and greedy coloring proves the assertion. \(\square\)

Combining this with Theorem 1 gives an explicit family of good forests.

### Corollary 3

Fix \(t\geq1\) and \(a,b\geq0\), and let
\[
H=S_t\sqcup aK_1\sqcup bK_2.
\]
Put
\[
c(w)=\binom w2,\qquad
P_{t,0}(w)=\binom{w+t-2}{t-1},
\]
and recursively define
\[
P_{t,j+1}(w)=w+c(w)P_{t,j}(w).
\]
Then every induced-\(H\)-free graph \(G\), with \(w=\omega(G)\), satisfies
\[
\chi(G)\leq w^aP_{t,b}(w).
\]
Equivalently,
\[
P_{t,b}(w)
=
c(w)^b\binom{w+t-2}{t-1}
+
w\sum_{j=0}^{b-1}c(w)^j.
\]
This has degree at most
\[
a+2b+t-1.
\]

In particular:

- every matching \(mK_2\) is good, with a bound of degree \(2m-2\);
- every forest consisting of isolated vertices and isolated edges is good;
- every forest with one star component and all other components of order at most two is good.

For example, for \(2K_2\) the argument gives the familiar explicit estimate
\[
\chi(G)\leq w+\binom w2=\binom{w+1}{2}.
\]

The same closure lemma can of course be applied to any other already-established good forest. For instance, using the elementary fact that \(P_4\)-free graphs are cographs and satisfy \(\chi=\omega\), it also gives polynomial bounds for
\[
P_4\sqcup aK_1\sqcup bK_2.
\]

## 3. Why this does not settle the conjecture

The maximum-clique argument works because the only complete connected forests are \(K_1\) and \(K_2\). Every vertex outside a maximum clique misses a clique vertex; if it misses two, those two vertices themselves supply an induced \(K_2\). There is no analogous way to obtain a component such as \(P_3\), \(P_5\), or a general tree from vertices of a clique.

More generally, suppose both \(F\) and \(T\) are already known to have polynomial bounds, and consider an \((F\sqcup T)\)-free graph containing an induced copy \(S\) of \(T\). The vertices anticomplete to \(S\) form an \(F\)-free graph, while all remaining vertices can be covered by the \(|T|\) neighborhoods of vertices of \(S\). This only yields a recurrence of the form
\[
b_{F\sqcup T}(w)
\leq
p_F(w)+|T|\,b_{F\sqcup T}(w-1)+O_T(1),
\]
together with the separate \(T\)-free case. Its direct solution is exponential in \(w\), not polynomial. Avoiding this multiplicative loss is precisely the missing issue for general disjoint unions.

Most importantly, the argument gives no information for connected nonstar trees such as \(P_5\), and it does not prove closure under adjoining a nontrivial tree component. Hence it is only a rigorous elementary partial result, not a proof of the polynomial Gyárfás–Sumner conjecture.