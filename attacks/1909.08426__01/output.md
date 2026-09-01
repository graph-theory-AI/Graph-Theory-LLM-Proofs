```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Adding isolated vertices to the forbidden pattern does not change randomized FPT solvability, and gives full parameterized many-one equivalence when the core has connected complement.",
  "would_publish": false,
  "caveats": "The reductions are elementary and do not decide the isolate-free cases P7, S_{1,1,3}, or S_{1,2,2}."
}
```

# Mathematical writeup

## 1. Formalization

For a fixed graph \(H\), let

\[
\textsc{IS}_H=\{(G,k):G\text{ is }H\text{-free and }\alpha(G)\ge k\},
\]

where “\(H\)-free” means having no induced copy of \(H\). The parameter is \(k\). This is the decision version of parameterized Maximum Independent Set.

I do not resolve the full dichotomy. I give:

1. an exact reduction eliminating isolated vertices from the forbidden pattern;
2. a many-one strengthening when the remaining pattern is co-connected;
3. an equivalence showing that the named open cases remain open even on graphs of diameter at most two with a universal vertex;
4. an explicit bounded-clique-number kernel for these cases.

The first result reduces the full dichotomy to forbidden patterns without isolated vertices.

---

## 2. Eliminating isolated vertices from the forbidden pattern

Write \(H+sK_1\) for the disjoint union of \(H\) and \(s\) isolated vertices.

### Theorem 1

Let \(H\) be a fixed nonempty graph and \(s\ge 0\) a fixed integer.

1. There is a nonadaptive FPT Turing reduction
   \[
   \textsc{IS}_{H+sK_1}\leq^{\mathrm{fpt}}_T \textsc{IS}_H
   \]
   using at most \(\binom ns\) oracle calls, each with parameter \(k-s\).

2. Consequently, \(\textsc{IS}_{H+sK_1}\) is deterministic FPT if and only if \(\textsc{IS}_H\) is deterministic FPT. The same equivalence holds for bounded-error randomized FPT.

3. If \(\textsc{IS}_H\) is \(W[1]\)-hard, then \(\textsc{IS}_{H+sK_1}\) is \(W[1]\)-hard.

4. If \(\overline H\) is connected, then the Turing reduction can be replaced by a parameterized many-one reduction. In that case the two problems are parameterized many-one equivalent, and hence one is \(W[1]\)-hard if and only if the other is.

### Proof

For \(X\subseteq V(G)\), define

\[
N_G[X]=X\cup\{v\in V(G): vx\in E(G)\text{ for some }x\in X\},
\]
and let
\[
G_X=G-N_G[X].
\]

The essential observation is the following.

#### Residual lemma

If \(G\) is \((H+sK_1)\)-free and \(X\) is an independent set of size \(s\), then \(G_X\) is \(H\)-free.

Indeed, if \(G_X\) contained an induced copy \(Q\) of \(H\), then:

- \(X\) is an independent set of size \(s\);
- by the definition of \(G_X\), there are no edges between \(X\) and \(Q\).

Thus \(G[X\cup V(Q)]\cong H+sK_1\), a contradiction.

Now suppose \(k\ge s\). For every graph \(G\),

\[
\alpha(G)\ge k
\quad\Longleftrightarrow\quad
\exists X\subseteq V(G),\ |X|=s,\ X\text{ independent},\
\alpha(G_X)\ge k-s.
\tag{1}
\]

The forward implication follows by taking any \(s\) vertices from an independent \(k\)-set. Conversely, an independent set in \(G_X\) is anticomplete to \(X\), so its union with \(X\) is independent.

If \(G\) is \((H+sK_1)\)-free, every graph \(G_X\) occurring in (1) is \(H\)-free by the residual lemma. We therefore enumerate the at most \(\binom ns\) independent \(s\)-subsets \(X\) and query \(\textsc{IS}_H\) on \((G_X,k-s)\).

If \(k<s\), one may simply enumerate all \(k\)-subsets. Since \(s\) is fixed as part of the forbidden pattern, this takes \(O(n^s)\) time.

If an algorithm for \(\textsc{IS}_H\) takes \(f(k)n^c\) time, the resulting running time is at most

\[
f(k)n^{c+s+O(1)},
\]

which is FPT because \(s\) is fixed.

For a bounded-error randomized oracle algorithm, amplify each of the at most \(n^s\) calls to error at most \(1/(3n^s)\). This needs only \(O(\log n)\) repetitions, and a union bound gives total error at most \(1/3\). Thus randomized FPT is also preserved.

For the reverse FPT implication, observe that every \(H\)-free graph is automatically \((H+sK_1)\)-free. Hence an algorithm for the latter class can simply be restricted to \(H\)-free inputs.

The same identity mapping proves the hardness direction:

\[
\textsc{IS}_H\leq_m^{\mathrm{fpt}}\textsc{IS}_{H+sK_1}.
\]

Thus \(W[1]\)-hardness of the core implies \(W[1]\)-hardness after adding isolated vertices.

It remains to prove the many-one strengthening when \(\overline H\) is connected. Assume \(k>s\), and put \(q=k-s\). For every independent \(s\)-set \(X\), take a disjoint copy of \(G_X\). Let \(J\) be the complete join of all these copies: vertices belonging to distinct copies are made pairwise adjacent. Then

\[
\alpha(J)=\max_X \alpha(G_X).
\]

Consequently, by (1),

\[
\alpha(G)\ge k \quad\Longleftrightarrow\quad \alpha(J)\ge q.
\tag{2}
\]

Each block \(G_X\) is \(H\)-free. We claim that their complete join \(J\) is also \(H\)-free. If an induced copy of \(H\) used vertices from at least two blocks, then all pairs belonging to different blocks would be adjacent. In the complement of this induced copy there would be no edges between the corresponding nonempty parts. This would disconnect \(\overline H\), contrary to the hypothesis. Hence every induced copy of \(H\) would have to lie in one block, which is impossible.

The graph \(J\) has at most

\[
\binom ns n=O(n^{s+1})
\]

vertices and can be constructed in polynomial time for fixed \(s\). Cases \(k\le s\) can be decided directly and mapped to fixed yes- or no-instances; equivalently, one may allow target parameter zero. This gives the claimed many-one reduction. Together with the identity reduction in the other direction, it proves parameterized many-one equivalence. ∎

---

## 3. Consequences for the dichotomy

Let \(H^\circ\) be obtained from \(H\) by deleting all isolated vertices.

### Corollary 2

If \(H^\circ\neq\varnothing\), then

\[
\textsc{IS}_H\text{ is randomized FPT}
\quad\Longleftrightarrow\quad
\textsc{IS}_{H^\circ}\text{ is randomized FPT}.
\]

Moreover:

- if \(\textsc{IS}_{H^\circ}\) is \(W[1]\)-hard, then so is \(\textsc{IS}_H\);
- if \(\overline{H^\circ}\) is connected, the two problems are parameterized many-one equivalent.

If \(H=sK_1\) is edgeless, then \(H\)-free graphs have independence number at most \(s-1\), and \(\textsc{IS}_H\) is polynomial-time solvable by enumerating subsets of size less than \(s\).

It follows that the full FPT/\(W[1]\)-hard dichotomy holds for all finite \(H\) if and only if it holds for all finite isolate-free \(H\). In particular, a hypothetical forbidden pattern witnessing failure of the proposed dichotomy can be chosen without isolated vertices.

This is stronger than mere monotonicity: tractability passes from the core to its isolated extensions through the explicit oracle reduction.

---

## 4. Application to the named open trees

A useful elementary fact is the following.

### Lemma 3

If \(T\) is a tree that is not a star, then \(\overline T\) is connected.

### Proof

Suppose \(\overline T\) is disconnected, and partition its vertices into two nonempty sets \(A,B\) with no complement edges between them. Then every pair in \(A\times B\) is an edge of \(T\). If both \(|A|\) and \(|B|\) are at least two, this gives a \(4\)-cycle in \(T\), impossible. Thus one part, say \(A\), consists of one vertex \(a\).

The vertex \(a\) is adjacent in \(T\) to every vertex of \(B\). There can be no edge inside \(B\), since such an edge together with \(a\) would form a triangle. Hence \(T\) is a star centered at \(a\). ∎

The graphs

\[
P_7,\qquad S_{1,1,3},\qquad S_{1,2,2}
\]

are non-star trees. Therefore their complements are connected. By Theorem 1, for every fixed \(s\),

\[
\textsc{IS}_{T+sK_1}
\quad\text{and}\quad
\textsc{IS}_T
\]

are parameterized many-one equivalent for each of these three choices of \(T\).

Thus adding any fixed number of isolated vertices to one of the listed open forbidden patterns creates no genuinely new case: it is exactly as hard, in the standard parameterized-reduction sense, as the isolate-free core.

This does not decide any of the three cores themselves.

---

## 5. The open cases remain open at diameter two

There is another exact restriction that is relevant to possible structural approaches.

### Theorem 4

Let \(H\) have no universal vertex. Then \(\textsc{IS}_H\) is parameterized many-one equivalent to its restriction to \(H\)-free graphs that have a universal vertex, and hence are connected and have diameter at most two.

### Proof

The restricted problem is trivially a subproblem of \(\textsc{IS}_H\). For the other direction, take an \(H\)-free graph \(G\) and add a new universal vertex \(u\), obtaining \(G'=G\vee K_1\).

The graph \(G'\) remains \(H\)-free. An induced copy of \(H\) avoiding \(u\) would already occur in \(G\). An induced copy containing \(u\) would make \(u\) correspond to a universal vertex of \(H\), contrary to the hypothesis.

Furthermore,

\[
\alpha(G')=\max\{\alpha(G),1\}.
\]

Thus, for \(k\ge2\),

\[
\alpha(G)\ge k \quad\Longleftrightarrow\quad \alpha(G')\ge k.
\]

The case \(k\le1\) is trivial and may be hard-coded. ∎

None of \(P_7,S_{1,1,3},S_{1,2,2}\) has a universal vertex. Consequently, solving any of their open cases merely for connected graphs, or even for graphs with a universal vertex and diameter at most two, would already solve the unrestricted case.

In particular, approaches based only on bounding the ordinary graph diameter cannot exploit the exclusion of a long induced path: adding an outside universal vertex reduces the diameter without destroying induced paths already present inside \(G\).

---

## 6. A bounded-clique-number tractable slice

For completeness, there is a standard explicit kernel when the clique number is bounded.

Fix \(r\ge2\), and define

\[
B(r,k)=\binom{r+k-2}{r-1}.
\]

The elementary Ramsey recurrence gives

\[
R(r,k)\le B(r,k).
\]

Hence every \(K_r\)-free graph on at least \(B(r,k)\) vertices contains an independent set of size \(k\). Therefore, on promised \(K_r\)-free inputs:

- if \(n\ge B(r,k)\), answer yes;
- otherwise retain the input, which has fewer than \(B(r,k)=O(k^{r-1})\) vertices.

For each fixed \(r\), this is a polynomial vertex kernel. In particular, for any of the three open patterns \(T\), the restriction to

\[
T\text{-free and }K_r\text{-free graphs}
\]

has a kernel with \(O(k^{r-1})\) vertices. A canonical yes-instance after the Ramsey threshold is the edgeless graph on \(k\) vertices, which is both \(T\)-free and \(K_r\)-free.

Combined with Theorem 1, this also gives a self-contained FPT proof for forbidden patterns \(K_r+sK_1\). The supplied source states stronger results for disjoint unions of cliques, so this corollary is not claimed as a literature advance.

---

## 7. What remains open

The reductions above do not address the essential isolate-free cases.

In particular, the isolate argument cannot be iterated along a pendant edge. For example, from \(P_7\)-freeness one cannot infer that \(G-N[v]\) is \(P_6\)-free: the graph \(P_6+K_1\) is \(P_7\)-free, but taking its isolated vertex \(v\) leaves \(G-N[v]\cong P_6\). Thus the known or conjectured tractability of shorter paths does not extend by the same argument.

Likewise, no algorithm or hardness reduction is obtained here for:

\[
P_7\text{-free},\qquad
S_{1,1,3}\text{-free},\qquad
S_{1,2,2}\text{-free}.
\]

For cores whose complements are disconnected, the oracle reduction still proves equivalence of deterministic and randomized FPT solvability, but I have not supplied a general many-one reduction in the reverse direction. One should therefore not infer standard \(W[1]\)-hardness of the core merely from hardness of an isolated extension in that case.

Accordingly, this is a structural reduction of the classification problem, not a proof of the full dichotomy or a counterexample to it.