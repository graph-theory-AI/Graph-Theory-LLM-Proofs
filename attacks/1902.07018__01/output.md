```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The equality remains unsettled, but bad assignments are structurally constrained, and the case r=4 reduces exactly to a finite 16-colour ∃∀ Boolean instance.",
  "would_publish": false,
  "caveats": "No QBF computation was run, and some of the general lemmas may already be standard."
}
```

# 1. Statement and notation

For a two-element list assignment
\[
L:E(K_n)\longrightarrow \binom{\mathcal C}{2},
\]
an \(L\)-coloring chooses \(\phi(e)\in L(e)\) for every edge. It is valid for \(K_r\) if no copy of \(K_r\) has all its edges assigned the same actual color.

The list Ramsey number \(R_\ell(K_r,2)\) is the least \(n\) for which some two-list assignment on \(K_n\) has no valid coloring. Constant lists give
\[
R_\ell(K_r,2)\le R(K_r,2).
\]
The open question asks whether equality always holds.

I do not resolve this. The main concrete outcome below is an exact reduction of the first unknown case \(r=4\) to a finite search with at most sixteen colors.

# 2. Exact SAT formulation

Order every list as
\[
L(e)=\{a_e,b_e\},
\]
and let \(x_e=0\) mean that \(a_e\) is selected, while \(x_e=1\) means that \(b_e\) is selected.

Put \(m=\binom r2\). For \(S\in\binom{[n]}r\) and
\[
c\in\bigcap_{e\in E(S)}L(e),
\]
define the clause
\[
C(S,c)=\bigvee_{e\in E(S)}\ell_{e,c},
\]
where
\[
\ell_{e,c}=
\begin{cases}
x_e,&c=a_e,\\
\neg x_e,&c=b_e.
\end{cases}
\]
This clause says that at least one edge of \(S\) is not assigned \(c\).

Thus
\[
F_L=\bigwedge_{\substack{S\in\binom{[n]}r\\
c\in\cap_{e\in E(S)}L(e)}}C(S,c)
\]
is satisfiable if and only if \(L\) has a valid coloring. Every clause has width \(m\), and there are at most
\[
2\binom nr
\]
clauses.

This formulation will be used repeatedly below.

# 3. Deterministic positive cases

## 3.1. Bipartite color-pair graph

Define the color-pair graph \(P_L\) as follows: its vertices are the colors occurring in the lists, and \(cd\) is an edge whenever \(\{c,d\}=L(e)\) for at least one host edge \(e\).

### Proposition 3.1
If \(n<R(K_r,2)\) and \(P_L\) is bipartite, then \(L\) has a valid coloring.

### Proof
Let \(f:\mathcal C\to\{0,1\}\) be a proper bipartition of \(P_L\). Hence every list contains one color of each \(f\)-value.

Because \(n<R(K_r,2)\), there is a red-blue coloring
\[
\chi:E(K_n)\to\{0,1\}
\]
with neither color class containing \(K_r\). For each host edge \(e\), choose the unique \(c\in L(e)\) satisfying
\[
f(c)=\chi(e).
\]
If a \(K_r\) were monochromatic in an actual color \(c\), all its edges would have the same \(\chi\)-color \(f(c)\), a contradiction. ∎

Consequently, every counterexample must have an odd cycle in its color-pair graph.

A slightly more flexible version will sometimes be useful.

### Proposition 3.2
Suppose there are maps
\[
f:\mathcal C\to\{0,1\},\qquad
\chi:E(K_n)\to\{0,1\},
\]
such that both \(\chi\)-classes are \(K_r\)-free and
\[
f(a_e)=f(b_e)\quad\Longrightarrow\quad
\chi(e)=f(a_e)=f(b_e).
\]
Then \(L\) has a valid coloring.

### Proof
If \(f(a_e)\ne f(b_e)\), choose the candidate whose \(f\)-value is \(\chi(e)\). If the two values agree, the displayed compatibility condition allows either candidate. Every edge assigned an actual color \(c\) then lies in the \(\chi\)-class \(f(c)\), which is \(K_r\)-free. ∎

For example, if the palette is \(\{1,2,3\}\) and all three pair types occur, write \(H_{ij}\) for the host graph formed by edges with list \(\{i,j\}\). If one \(H_{ij}\) is contained in a color class of some ordinary \((K_r,K_r)\)-free coloring, then Proposition 3.2 solves that assignment. Hence a bad three-color assignment would require all three pair-type graphs to fail this precoloring-extension property.

## 3.2. A constructive polynomial lower bound

### Proposition 3.3
For every \(r\ge3\),
\[
R_\ell(K_r,2)\ge (r-1)^2+1.
\]

### Proof
Set \(q=r-1\), and suppose \(n\le q^2\). For every actual color \(c\), we will construct a vertex labeling
\[
\lambda_c:V(K_n)\to[q]
\]
such that for every host edge \(uv\) with list \(\{a,b\}\),
\[
\lambda_a(u)\ne\lambda_a(v)
\quad\text{or}\quad
\lambda_b(u)\ne\lambda_b(v). \tag{1}
\]

Order the host vertices \(v_1,\dots,v_n\). Assume the labels have already been chosen on \(v_1,\dots,v_{j-1}\). Choose all values \(\lambda_c(v_j)\) independently and uniformly from \([q]\). For a fixed \(i<j\), with
\[
L(v_iv_j)=\{a,b\},
\]
the probability that (1) fails is \(q^{-2}\). Since
\[
j-1\le n-1\le q^2-1,
\]
the union bound shows that some choice of the labels at \(v_j\) satisfies all \(j-1\) constraints. Continue inductively.

For every edge \(uv\), select a candidate \(c\in L(uv)\) for which
\[
\lambda_c(u)\ne\lambda_c(v).
\]
The edges assigned color \(c\) form a subgraph of the complete \(q\)-partite graph induced by the partition into the fibers of \(\lambda_c\). Since \(q=r-1\), this graph contains no \(K_r\). ∎

In particular,
\[
R_\ell(K_4,2)\ge10.
\]
This is far from the desired value \(18\), but the construction works for completely arbitrary palettes.

# 4. A lopsided local-lemma criterion

For a color \(c\), let
\[
G_c=\bigl(V(K_n),\{e:c\in L(e)\}\bigr)
\]
be its support graph. For \(e\in E(G_c)\), let
\[
\kappa_c(e)=
\#\left\{
S\in\binom{V(K_n)}r:
e\in E(S)\subseteq E(G_c)
\right\}.
\]
Thus \(\kappa_c(e)\) is the number of possible \(c\)-monochromatic \(K_r\)'s containing \(e\).

### Proposition 4.1
Let \(m=\binom r2\). If
\[
\kappa_c(e)\le K
\]
for every color-edge incidence and
\[
\mathrm e\,2^{-m}(mK+1)\le1, \tag{2}
\]
then \(L\) has a valid coloring.

### Proof
Under a uniformly random assignment of the binary variables \(x_e\), the probability that a fixed clause \(C(S,c)\) is false is \(2^{-m}\).

Use the standard lopsided dependency graph for CNF formulas: two clause-falsification events are adjacent only when the clauses contain complementary literals. For the clause \(C(S,c)\), consider an edge \(e\in E(S)\), and let \(d_e\) be the other color in \(L(e)\). Clauses containing the complementary literal on \(x_e\) are precisely clauses \(C(T,d_e)\) with \(e\in E(T)\subseteq E(G_{d_e})\). There are at most \(K\) of them.

Therefore every clause has at most \(mK\) lopsided neighbors. Condition (2) is the symmetric lopsided Lovász local lemma criterion. Hence with positive probability no clause is false, which is exactly a valid \(L\)-coloring. ∎

Since always
\[
\kappa_c(e)\le \binom{n-2}{r-2},
\]
we obtain the explicit sufficient condition
\[
\mathrm e\,2^{-m}
\left(
m\binom{n-2}{r-2}+1
\right)\le1. \tag{3}
\]

Using
\[
\binom{n-2}{r-2}
\le
\left(\frac{\mathrm e(n-2)}{r-2}\right)^{r-2},
\]
condition (3) holds whenever
\[
n-2\le
\frac{r-2}{\mathrm e}
\left(
\frac{2^m/\mathrm e-1}{m}
\right)^{1/(r-2)}.
\]
Consequently,
\[
R_\ell(K_r,2)
\ge
\left(\frac{\sqrt2}{\mathrm e}-o(1)\right)
r\,2^{r/2}.
\]
This is the classical local-lemma scale and does not approach the known upper bounds for ordinary diagonal Ramsey numbers.

For \(r=4\), \(m=6\). Proposition 4.1 gives the concrete structural statement:

> If every edge of every color-support graph lies in at most three \(K_4\)'s of that support graph, then the list assignment is colorable.

Thus any \(K_4\) counterexample must contain a color-support edge lying in at least four supported \(K_4\)'s.

# 5. Palette compression

Although the definition allows an arbitrary color set, a counterexample can always be compressed substantially.

### Proposition 5.1
If a bad list assignment exists on \(K_n\), then one exists using at most
\[
\min\left\{
n,\left\lfloor
\frac{2\binom n2}{\binom r2}
\right\rfloor
\right\}
\]
colors.

### Proof: chromatic compression
Let \(P_L\) be the color-pair graph and let
\[
t=\chi(P_L).
\]
Take a proper coloring
\[
\psi:V(P_L)\to[t]
\]
and replace every list \(\{a,b\}\) by
\[
\{\psi(a),\psi(b)\}.
\]
The two new entries remain distinct.

If the compressed assignment had a valid coloring, each selected meta-color would lift uniquely to one of \(a,b\). A monochromatic actual \(K_r\) in color \(c\) would give a monochromatic compressed \(K_r\) in color \(\psi(c)\). Hence badness is preserved.

Since \(P_L\) has at most \(\binom n2\) distinct edges, \(t\le n\): a \(t\)-critical subgraph has minimum degree at least \(t-1\), and hence at least \(\binom t2\) edges.

### Proof: minimal-unsatisfiable-core compression
Let \(F'\) be a clause-minimal unsatisfiable subformula of \(F_L\), and let \(U\) be its variables. Every variable in \(U\) occurs in both polarities. Indeed, if a variable occurred in only one polarity, assigning it to satisfy that polarity and satisfying the proper subformula obtained by deleting all clauses containing it would satisfy \(F'\).

Let \(\mathcal C'\) be the colors indexing clauses in \(F'\). Both candidates of every variable in \(U\) belong to \(\mathcal C'\). Moreover, every \(c\in\mathcal C'\) indexes a clause supported on \(m=\binom r2\) distinct variables. Therefore
\[
m|\mathcal C'|\le 2|U|\le2\binom n2.
\]
Keeping the original lists on \(U\) and filling all remaining host edges with arbitrary two-element lists from \(\mathcal C'\) preserves the unsatisfiable subformula \(F'\). This gives the second bound. Combining the two compressions gives the minimum displayed above. ∎

# 6. A sharper reduction for \(K_4\) on \(17\) vertices

The chromatic compression bound initially gives seventeen colors. The extremal seventeen-color case can be eliminated.

### Lemma 6.1
Every graph with sixteen edges contains at most sixteen copies of \(K_4\).

### Proof
For an edge \(uv\), copies of \(K_4\) containing \(uv\) correspond to edges in
\[
G[N(u)\cap N(v)].
\]
If \(uv\) belonged to at least seven \(K_4\)'s, then its common neighborhood would have at least five vertices and at least seven internal edges. The graph would then contain at least
\[
1+2\cdot5+7=18
\]
edges: \(uv\), the ten edges from \(u,v\) to the common neighborhood, and seven internal edges. This contradicts the assumption of sixteen edges.

Thus every edge belongs to at most six \(K_4\)'s. Double-counting incidences between edges and copies of \(K_4\) gives
\[
6\,N_{K_4}(G)\le16\cdot6,
\]
as required. ∎

### Proposition 6.2
Suppose the lists on \(E(K_{17})\) are in bijection with the \(\binom{17}{2}\) unordered pairs from a palette of seventeen colors. Then the assignment has a valid \(K_4\)-free coloring.

### Proof
For each palette color \(c\), let \(G_c\) be its support graph on the seventeen host vertices. Since every pair \(\{c,d\}\) occurs exactly once, \(G_c\) has exactly sixteen edges. By Lemma 6.1,
\[
N_{K_4}(G_c)\le16.
\]

Choose a uniformly random regular tournament \(T\) on the seventeen palette colors; every vertex has indegree eight. For a host edge whose list is \(\{c,d\}\), choose the head of the tournament edge \(cd\).

Fix \(c\) and a \(K_4\) in \(G_c\). Its six host edges correspond to six distinct palette pairs \(\{c,d_i\}\), because every palette pair occurs once. The in-neighborhood of \(c\) in a uniformly random regular tournament is uniformly distributed over the \(\binom{16}{8}\) eight-subsets of the other colors. Hence the probability that all six corresponding tournament edges point into \(c\) is
\[
\frac{\binom{10}{2}}{\binom{16}{8}}
=
\frac{45}{12870}
=
\frac1{286}.
\]

There are at most
\[
17\cdot16=272
\]
possible bad pairs \((c,K_4)\). Therefore the expected number of monochromatic \(K_4\)'s is at most
\[
\frac{272}{286}<1.
\]
Some regular tournament consequently produces no monochromatic \(K_4\). ∎

### Corollary 6.3
If a bad two-list assignment exists on \(K_{17}\) for \(K_4\), then a bad assignment exists using at most sixteen colors.

### Proof
Let \(P_L\) be its color-pair graph. We know \(\chi(P_L)\le17\). Suppose equality holds. A \(17\)-critical subgraph has at least
\[
\binom{17}{2}=136
\]
edges. Since \(P_L\) has at most 136 distinct edges, equality holds throughout: the critical subgraph is \(K_{17}\), there are no additional used colors, and every palette pair occurs exactly once among the 136 host edges. Proposition 6.2 then shows that the assignment is colorable, a contradiction.

Thus \(\chi(P_L)\le16\), and chromatic compression gives a bad assignment with at most sixteen colors. ∎

This is an exact finite reduction, not a resolution of \(R_\ell(K_4,2)\).

# 7. Fully specified QBF for the \(K_4\) case

Because \(R(4,4)=18\), equality \(R_\ell(K_4,2)=18\) holds if and only if there is no bad assignment on \(K_{17}\). By Corollary 6.3 it suffices to search palettes of size sixteen.

For every host edge \(e\in E(K_{17})\) and \(1\le i<j\le16\), introduce an existential Boolean variable
\[
z_{e,ij},
\]
meaning \(L(e)=\{i,j\}\). Require exactly one \(z_{e,ij}\) for each \(e\). Introduce universal variables \(x_e\), where \(x_e=0\) selects the smaller list entry and \(x_e=1\) the larger.

Define
\[
\operatorname{Sel}_{e,c}=
\left(
\neg x_e\wedge\bigvee_{j>c}z_{e,cj}
\right)
\vee
\left(
x_e\wedge\bigvee_{i<c}z_{e,ic}
\right).
\]

The exact counterexample question is the truth of
\[
\begin{aligned}
\Phi_{17,16}:=
\exists (z_{e,ij})\ \forall(x_e)\quad
&\left[
\bigwedge_{e\in E(K_{17})}
\operatorname{ExactlyOne}\{z_{e,ij}:i<j\}
\right]\\
&{}\land
\left[
\bigvee_{\substack{S\in\binom{[17]}4\\c\in[16]}}
\ \bigwedge_{e\in E(S)}
\operatorname{Sel}_{e,c}
\right].
\end{aligned}
\]

It has:

- \(136\cdot\binom{16}{2}=16{,}320\) existential list variables;
- 136 universal choice variables;
- \(16\binom{17}{4}=38{,}080\) candidate monochromatic-color/copy conjunctions.

The interpretation is exact:

- If \(\Phi_{17,16}\) is true, its existential witness is a bad assignment on \(K_{17}\), so
  \[
  R_\ell(K_4,2)\le17<18.
  \]
- If \(\Phi_{17,16}\) is false, no bad assignment on \(K_{17}\) exists, and therefore
  \[
  R_\ell(K_4,2)=18.
  \]

For a proposed positive witness \(L\), one can independently validate badness by constructing the width-six CNF \(F_L\), with at most
\[
2\binom{17}{4}=4760
\]
clauses, and supplying an UNSAT certificate.

I have not run this computation.

# 8. Remaining gap

The reductions do not control assignments whose color-pair graph has an odd cycle and whose color-support graphs are sufficiently dense. In particular, the sixteen-color QBF remains completely unevaluated. The local-lemma estimate is asymptotic and much too weak to reach \(n=17\) when \(r=4\).

Thus there is presently neither a proof of
\[
R_\ell(K_r,2)=R(K_r,2)
\]
for any \(r>3\) here, nor an explicit counterexample.