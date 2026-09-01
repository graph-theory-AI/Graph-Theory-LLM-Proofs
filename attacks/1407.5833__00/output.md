```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The intended finite-VC-dimension implication is already refuted by the hereditary class of C4-free bipartite graphs in Theorem 4.3 of the cited source.",
  "would_publish": false,
  "caveats": "The inapproximability is conditional on the theorem's standard complexity assumption, and the extracted phrase 'logarithmic lower bound' is formally imprecise."
}
```

# Mathematical writeup

## 1. Statement under consideration

For a graph \(G\), let
\[
\mathcal N(G)=\{N_G[v]:v\in V(G)\}
\]
be its closed-neighborhood set system. An identifying code is a set \(C\subseteq V(G)\) such that the traces
\[
N_G[v]\cap C,\qquad v\in V(G),
\]
are all nonempty and pairwise distinct.

The intended algorithmic assertion is

\[
\sup_{G\in\mathcal C}\operatorname{VCdim}(\mathcal N(G))<\infty
\quad\Longrightarrow\quad
\text{Min Identifying Code has a constant-factor approximation on }\mathcal C
\]
for every hereditary class \(\mathcal C\).

This assertion is false in the usual complexity-theoretic sense.

## 2. Counterexample class

Let
\[
\mathcal B=\{G:G\text{ is bipartite and contains no }C_4\}.
\]

This class is hereditary: induced subgraphs preserve both bipartiteness and absence of a \(4\)-cycle.

### Proposition 2.1
Every graph in \(\mathcal B\) has closed-neighborhood VC-dimension at most \(2\).

#### Proof

Let \(G\in\mathcal B\), with bipartition \((L,R)\). Suppose, for a contradiction, that a three-element set
\[
X=\{x_1,x_2,x_3\}
\]
is shattered by \(\mathcal N(G)\). In particular, there is a vertex \(y\) such that
\[
N[y]\cap X=X.
\]

First suppose \(y\notin X\). Then all three vertices of \(X\) are neighbors of \(y\), hence lie in the same side of the bipartition. Since \(X\) is shattered, some vertex \(z\) realizes the trace \(\{x_1,x_2\}\). The vertex \(z\) cannot be one of the \(x_i\), because vertices in the same bipartition class are nonadjacent. Thus \(z\notin X\), and both \(y\) and \(z\) are adjacent to \(x_1,x_2\). Consequently
\[
y x_1 z x_2 y
\]
is a \(4\)-cycle, a contradiction.

Now suppose \(y\in X\), say \(y=x_1\). Then \(x_2,x_3\) lie in the opposite bipartition class and are both adjacent to \(x_1\). Let \(z\) realize the trace \(\{x_2,x_3\}\). It is not \(x_1\), whose trace is all of \(X\), and it cannot be \(x_2\) or \(x_3\): those vertices are adjacent to \(x_1\) and are not adjacent to each other. Hence \(z\notin X\), and \(x_1,z\) have the two common neighbors \(x_2,x_3\). Again this gives a \(4\)-cycle.

Thus no three-element set is shattered, proving
\[
\operatorname{VCdim}(\mathcal N(G))\le 2.
\]
\(\square\)

The bound is attained within the class: take a three-vertex path with endpoints \(x,y\), together with an isolated vertex. The set \(\{x,y\}\) is shattered by the closed neighborhoods of the two endpoints, the middle vertex, and the isolated vertex. Hence the class has VC-dimension exactly \(2\).

## 3. Polynomial lower bound on identifying-code size

The finite VC-dimension can also be used directly to verify that \(\mathcal B\) lies in the polynomial-size regime.

Let \(G\in\mathcal B\) have \(n\) vertices and let \(C\) be an identifying code of size \(k\). The \(n\) traces
\[
\{N[v]\cap C:v\in V(G)\}
\]
are pairwise distinct. Their set system on the ground set \(C\) has VC-dimension at most \(2\). By the Sauer–Shelah bound,
\[
n\le \binom{k}{0}+\binom{k}{1}+\binom{k}{2}
  =1+k+\frac{k(k-1)}2.
\]
Therefore
\[
k\ge \frac{\sqrt{8n-7}-1}{2}=\Omega(\sqrt n).
\]

Thus \(C_4\)-free bipartite graphs have the polynomial lower bound expected of a finite-VC-dimension class; in particular, they do not contain arbitrarily large graphs with identifying-code number \(O(\log n)\).

## 4. Approximation hardness

Theorem 4.3 of the cited source paper—Bousquet, Lagoutte, Li, Parreau and Thomassé, *SIAM Journal on Discrete Mathematics* 29 (2015), 2047–2064—establishes that there is an absolute constant \(c>0\) such that Min Identifying Code on \(C_4\)-free bipartite graphs cannot be approximated in polynomial time within
\[
c\log |V(G)|
\]
under the complexity assumption stated there. The hardness instances are identifiable graphs, as required for the optimization problem.

This immediately excludes a constant-factor approximation under the same assumption. Indeed, suppose an algorithm had approximation ratio \(A\), where \(A\) is constant. For all sufficiently large \(n\),
\[
A\le c\log n.
\]
For the finitely many smaller orders, one could solve the problem exactly by exhaustive enumeration, thereby obtaining a polynomial-time \(c\log n\)-approximation on every input. This contradicts Theorem 4.3.

Consequently, \(\mathcal B\) simultaneously has:

1. hereditary closure;
2. finite closed-neighborhood VC-dimension, in fact exactly \(2\);
3. the polynomial lower bound \(\gamma^{\mathrm{ID}}(G)=\Omega(\sqrt{|V(G)|})\);
4. no constant-factor approximation, subject to the source theorem’s standard complexity assumption.

This is precisely a counterexample to the proposed implication
\[
\text{finite VC-dimension}\Longrightarrow\text{constant-factor approximability}.
\]

## 5. Defect in the extracted wording

The phrase “the minimum identifying code size has a logarithmic lower bound” cannot define one side of a dichotomy. Every identifying code \(C\) of size \(k\) produces \(n\) distinct nonempty subsets of \(C\), so
\[
n\le 2^k-1
\quad\Longrightarrow\quad
k\ge \lceil\log_2(n+1)\rceil.
\]
Thus every identifiable graph has a logarithmic lower bound, and a polynomial lower bound implies a logarithmic one.

The size theorem from the source should instead be expressed as follows:

- infinite-VC-dimension hereditary classes contain arbitrarily large graphs with identifying-code number \(O(\log n)\);
- finite-VC-dimension classes have a uniform polynomial lower bound.

With that corrected interpretation, \(C_4\)-free bipartite graphs are unequivocally in the second size regime but have logarithmic approximation hardness.

## 6. Conclusion and remaining gap

The universal approximation dichotomy in the catalog entry is not open: its intended finite-VC algorithmic half is already refuted in the source paper itself. What may remain open is a structural characterization of those finite-VC-dimension hereditary classes that do admit constant-factor approximations.

The structural part above is self-contained. The algorithmic obstruction relies on the published reduction in Theorem 4.3 rather than reproducing that reduction, and is conditional on its stated complexity assumption. This is a correction of the catalog status, not a new publishable result.