```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove (i)–(ii) for graph classes with fixed biclique-cover load, and the k_B-bound in (iii) when the cover has load one on B.",
  "would_publish": false,
  "caveats": "These are structural special cases, not a resolution for general bipartite graphs; novelty is not asserted."
}
```

# A structural special case at the conjectured scale

I discard the previous proposed disproof: its small-degree example does not address the intended asymptotic conjecture.

The partial result below applies to graph classes with unbounded degrees and arbitrarily large connected components. In particular, it proves the bound in Conjecture 7(iii), with an absolute constant, for a family of regular bipartite graphs obtained by blowing up incidence graphs.

All logarithms are natural. Graphs are finite and simple.

## 1. Biclique covers and the main criterion

A **biclique cover** of a bipartite graph \(G=(A\cup B,E)\) is a family
\[
\mathcal K=\{(A_i,B_i):i\in I\}
\]
such that \(A_i\subseteq A\), \(B_i\subseteq B\), every pair in \(A_i\times B_i\) is an edge, and
\[
E=\bigcup_{i\in I}(A_i\times B_i).
\]
Overlaps are allowed.

The cover has **load at most \((r_A,r_B)\)** if every vertex of \(A\) belongs to at most \(r_A\) bicliques and every vertex of \(B\) belongs to at most \(r_B\) bicliques.

Here \(r_A,r_B\geq1\). Throughout the asymptotic corollaries, these load bounds are fixed constants.

### Theorem 1
Suppose \(G\) has maximum degrees at most \(\Delta_A,\Delta_B\) on its respective parts and has a biclique cover of load at most \((r_A,r_B)\).

If there exist \(p,x_A,x_B\in(0,1)\) such that
\[
(1-p^{r_A})^{k_A}
 \leq x_A(1-x_B)^{\Delta_A},
\tag{1}
\]
and
\[
\bigl(1-(1-p)^{r_B}\bigr)^{k_B}
 \leq x_B(1-x_A)^{\Delta_B},
\tag{2}
\]
then \(G\) is \((k_A,k_B)\)-choosable.

The important feature is that the dependency bounds in this criterion are the original graph degrees, not the number of vertices or the number of occurrences of a colour.

### Proof

Fix an arbitrary list assignment with list sizes \(k_A,k_B\) on the respective parts. Larger lists can first be trimmed.

For every biclique \(i\) and every colour \(c\) appearing in the lists, choose an independent Bernoulli variable
\[
\xi_{i,c},\qquad \Pr(\xi_{i,c}=1)=p.
\]

Declare a colour \(c\in L(a)\) **available** at \(a\in A\) if
\[
\xi_{i,c}=1\quad\text{for every biclique }i\text{ containing }a.
\]
Declare \(c\in L(b)\) available at \(b\in B\) if
\[
\xi_{i,c}=0\quad\text{for every biclique }i\text{ containing }b.
\]

If every vertex has an available colour, choosing any such colour at each vertex gives a proper colouring. Indeed, an edge \(ab\) belongs to some biclique \(i\). A colour available at both endpoints would require both \(\xi_{i,c}=1\) and \(\xi_{i,c}=0\).

Let \(F_v\) be the event that \(v\) has no available colour. If \(a\) belongs to \(t(a)\leq r_A\) bicliques, then different colours use disjoint sets of random variables, so
\[
\Pr(F_a)=(1-p^{t(a)})^{k_A}
 \leq (1-p^{r_A})^{k_A}.
\tag{3}
\]
Similarly,
\[
\Pr(F_b)\leq
\bigl(1-(1-p)^{r_B}\bigr)^{k_B}.
\tag{4}
\]
For an isolated vertex belonging to no biclique, every colour is available, so its bad event has probability zero.

#### The lopsided dependency graph

Each \(F_a\), \(a\in A\), is decreasing in the Bernoulli variables, while each \(F_b\), \(b\in B\), is increasing.

Moreover, if \(a\in A\) and \(b\in B\) are nonadjacent, their bad events use disjoint variables: a biclique containing both would imply \(ab\in E\).

These facts imply that \(G\) itself is a lopsided dependency graph for the events \(\{F_v\}\). Here is a direct verification, including the issue of conditioning on several events simultaneously.

Fix \(a\in A\), and let \(S\) be any set of vertices not containing \(a\) or a neighbour of \(a\). Let \(X\) be the variables used by \(F_a\), and \(Y\) all remaining variables.

- Every event \(F_b\) with \(b\in S\cap B\) depends only on \(Y\).
- After fixing \(Y\), the event
  \[
  \bigcap_{a'\in S\cap A}\overline{F_{a'}}
  \]
  is increasing in \(X\), whereas \(F_a\) is decreasing.

The decreasing/increasing form of the product-measure correlation inequality therefore gives, for each fixed \(Y\),
\[
\Pr_X\!\left(
 F_a\cap\bigcap_{a'\in S\cap A}\overline{F_{a'}}
 \right)
\leq
\Pr(F_a)\,
\Pr_X\!\left(
 \bigcap_{a'\in S\cap A}\overline{F_{a'}}
 \right).
\]
Multiplying by the indicator that the events indexed by \(S\cap B\) are avoided, and then averaging over \(Y\), yields
\[
\Pr\!\left(F_a\mid\bigcap_{v\in S}\overline{F_v}\right)
 \leq \Pr(F_a)
\]
whenever the conditioning event has positive probability. The argument for \(b\in B\) is the same with increasing and decreasing interchanged.

We now apply the asymmetric lopsided Lovász local lemma: if the bad-event probabilities are at most
\[
x_v\prod_{u\in N_G(v)}(1-x_u),
\]
then all bad events can simultaneously be avoided with positive probability. Set \(x_v=x_A\) on \(A\) and \(x_v=x_B\) on \(B\). Equations (1)–(4), together with the degree bounds, verify these inequalities.

Thus every vertex has an available colour for some outcome of the variables, completing the proof. \(\square\)

---

## 2. Consequence for clause (ii): logarithmic lists

A useful specialization of Theorem 1 is obtained by setting
\[
x_A=\frac1{2\Delta_B},
\qquad
x_B=\frac1{2\Delta_A}.
\]
Bernoulli’s inequality gives
\[
\left(1-\frac1{2d}\right)^d\geq\frac12
\qquad(d\geq1).
\]
Consequently, it suffices to find \(p\) for which
\[
(1-p^{r_A})^{k_A}\leq\frac1{4\Delta_B},
\qquad
\bigl(1-(1-p)^{r_B}\bigr)^{k_B}\leq\frac1{4\Delta_A}.
\tag{5}
\]

Taking \(p=1/2\), and using \(1-z\leq e^{-z}\), proves the following.

### Corollary 2
A graph with a biclique cover of load at most \((r_A,r_B)\) is \((k_A,k_B)\)-choosable whenever
\[
k_A\geq 2^{r_A}\log(4\Delta_B),
\qquad
k_B\geq 2^{r_B}\log(4\Delta_A).
\tag{6}
\]

In particular, fix \(r\) and restrict to graphs admitting a cover with both loads at most \(r\). For \(\Delta_A,\Delta_B\geq2\),
\[
\log(4\Delta)\leq3\log\Delta.
\]
Thus clause (ii) holds throughout this graph class with the absolute constant
\[
C=3\cdot2^r.
\]

For example, load at most two on each part permits \(C=12\), independently of the degrees, graph order, and list assignment.

---

## 3. Consequence for clause (i), including arbitrarily unbalanced degrees

The logarithmic corollary alone does not establish clause (i) when the two degree bounds are extremely different. A biased choice of \(p\) handles that case.

### Corollary 3
Fix \(\varepsilon>0\) and fixed positive integers \(r_A,r_B\). There is
\[
\Delta_0=\Delta_0(\varepsilon,r_A,r_B)
\]
such that every graph with a biclique cover of load at most \((r_A,r_B)\) satisfies the conclusion of clause (i), provided
\[
\Delta_A,\Delta_B\geq\Delta_0.
\]

### Proof

First suppose
\[
X:=\Delta_A\geq Y:=\Delta_B.
\]
Choose
\[
p=X^{-\varepsilon/(2r_A)}.
\]
If \(k_A\geq X^\varepsilon\), then
\[
(1-p^{r_A})^{k_A}
 \leq \exp(-k_Ap^{r_A})
 \leq \exp(-X^{\varepsilon/2}).
\tag{7}
\]

For the other part, Bernoulli’s inequality gives
\[
1-(1-p)^{r_B}\leq r_Bp.
\]
For sufficiently large \(X\), depending only on the fixed parameters,
\[
r_B\leq X^{\varepsilon/(4r_A)}.
\]
Hence, if \(k_B\geq Y^\varepsilon\),
\[
\begin{aligned}
\bigl(1-(1-p)^{r_B}\bigr)^{k_B}
&\leq (r_Bp)^{k_B}\\
&\leq X^{-\varepsilon k_B/(4r_A)}\\
&\leq X^{-\varepsilon Y^\varepsilon/(4r_A)}.
\end{aligned}
\tag{8}
\]

Choose \(\Delta_0\) sufficiently large that, whenever \(X\geq Y\geq\Delta_0\),
\[
Y^\varepsilon\geq\frac{8r_A}{\varepsilon},
\qquad X\geq4,
\qquad
e^{-X^{\varepsilon/2}}\leq\frac1{4X}.
\]
Then (7) is at most \(1/(4Y)\), and (8) is at most
\[
X^{-2}\leq\frac1{4X}.
\]
These are exactly the two bounds in (5).

If \(\Delta_B>\Delta_A\), interchange the parts and replace \(p\) by \(1-p\). Enlarging \(\Delta_0\) to cover both choices proves the assertion. \(\square\)

For any fixed cover-load class, the extra dependence of \(\Delta_0\) on the load is simply part of the constant defining that class. In particular, fixing load two gives a genuine special case with \(\Delta_0\) depending only on \(\varepsilon\).

---

## 4. Consequence for clause (iii): the conjectured semi-small-list scale

Here a stronger asymmetry in the cover is useful.

### Corollary 4
Suppose \(G\) has maximum degree at most \(\Delta\geq2\) and admits a biclique cover of load at most \((r,1)\). Then \(G\) is \((k_A,k_B)\)-choosable whenever
\[
k_B\geq
8r\left(\frac{\Delta}{\log\Delta}\right)^{1/k_A}\log\Delta.
\tag{9}
\]

Thus the \(k_B\)-bound in clause (iii) holds, with the conjectured power and logarithmic factor, for every fixed \(r\) in this class. Interchanging the parts gives the other branch for covers of load at most \((1,r)\).

### Proof

Write
\[
k=k_A,\qquad m=k_B,\qquad t=\log(2\Delta).
\]
Set
\[
x_A=\frac{t}{2\Delta},
\qquad
x_B=\frac1{2\Delta},
\qquad
q=\frac1r\left(\frac{t}{4\Delta}\right)^{1/k},
\qquad p=1-q.
\]
For \(\Delta\geq2\), we have \(t\leq\Delta\), so these parameters lie in the required intervals and \(x_A\leq1/2\).

On \(A\),
\[
\begin{aligned}
(1-p^r)^k
&=\bigl(1-(1-q)^r\bigr)^k\\
&\leq(rq)^k\\
&=\frac{t}{4\Delta}
=\frac{x_A}{2}\\
&\leq x_A(1-x_B)^\Delta.
\end{aligned}
\tag{10}
\]

Because the cover load on \(B\) is at most one, its bad-event bound is simply
\[
(1-q)^m\leq e^{-qm}.
\]
Also, \(\log(1-x)\geq-2x\) for \(0\leq x\leq1/2\), so
\[
\begin{aligned}
x_B(1-x_A)^\Delta
&\geq \frac1{2\Delta}e^{-2\Delta x_A}\\
&=\frac1{2\Delta}e^{-t}\\
&=e^{-2t}.
\end{aligned}
\tag{11}
\]
Thus Theorem 1 applies whenever \(qm\geq2t\), equivalently
\[
m\geq
2r\,4^{1/k}\Delta^{1/k}t^{\,1-1/k}.
\tag{12}
\]

Finally, \(t\leq2\log\Delta\), and \(k\geq1\), giving
\[
\begin{aligned}
2r\,4^{1/k}\Delta^{1/k}t^{1-1/k}
&\leq
4r\,2^{1/k}\Delta^{1/k}(\log\Delta)^{1-1/k}\\
&\leq
8r\,\Delta^{1/k}(\log\Delta)^{1-1/k}.
\end{aligned}
\]
Therefore (9) implies (12). This includes \(k_A=1\); no separate endpoint exception is needed. \(\square\)

The asymmetric local-lemma weights are important here. The choice \(x_A\asymp\log\Delta/\Delta\), rather than \(x_A\asymp1/\Delta\), produces the factor \((\log\Delta)^{1-1/k_A}\).

---

## 5. Nontrivial graph families covered

### 5.1 A description using twin classes

Partition \(B\) into classes of vertices having identical neighbourhoods. Suppose every \(a\in A\) is adjacent to vertices in at most \(r\) such classes.

For each class \(B_i\), take the biclique
\[
N(B_i)\times B_i.
\]
This is a cover of load at most \((r,1)\). Consequently, Corollary 4 applies.

The classes can be large, and their neighbourhoods can overlap in an arbitrary global pattern subject to the load bound.

### 5.2 Regular examples of arbitrary order

Let \(H\) be a loopless graph. Construct a bipartite graph as follows:

- for every edge \(e\in E(H)\), introduce a vertex \(a_e\in A\);
- for every vertex \(v\in V(H)\), introduce a nonempty independent set \(B_v\subseteq B\);
- join \(a_e\) to every vertex of \(B_v\) precisely when \(v\) is an endpoint of \(e\).

For each \(v\), the pair
\[
\bigl(\{a_e:e\ni v\},\,B_v\bigr)
\]
is a biclique. These bicliques give a cover of load at most \((2,1)\).

If \(\Delta\) is even, \(H\) is \(\Delta\)-regular, and every \(B_v\) has size \(\Delta/2\), then the constructed graph is itself \(\Delta\)-regular:
\[
d(a_{uv})=|B_u|+|B_v|=\Delta,
\qquad
d(b)=d_H(v)=\Delta\quad(b\in B_v).
\]
The order of \(H\), and hence the component order of the constructed graph, is unrestricted.

For all these graphs, Corollary 4 gives
\[
k_B\geq
16\left(\frac{\Delta}{\log\Delta}\right)^{1/k_A}\log\Delta.
\]
This is therefore not merely a bounded-order special case or a case where the small-list part has bounded degree.

### 5.3 Calibration of the power of \(\Delta\)

For comparison, the power \(\Delta^{1/k_A}\) cannot be reduced even within cover load \((1,1)\).

Fix \(k,m\geq2\). Take \(G=K_{m^k,k}\), with the part of size \(m^k\) called \(A\). Give the vertices \(b_1,\ldots,b_k\in B\) disjoint lists
\[
L(b_i)=\{c_{i,1},\ldots,c_{i,m}\}.
\]
Index \(A\) by tuples \(\mathbf j=(j_1,\ldots,j_k)\in[m]^k\), and set
\[
L(a_{\mathbf j})=\{c_{1,j_1},\ldots,c_{k,j_k}\}.
\]
Any choices of colours on \(B\) determine a tuple \(\mathbf j\); all colours of \(L(a_{\mathbf j})\) are then forbidden. Thus \(G\) is not \((k,m)\)-choosable.

Its maximum degree is \(\Delta=m^k\), so \(m=\Delta^{1/k}\). This verifies the necessary polynomial scale, but does not establish necessity of the logarithmic factor.

---

## 6. Remaining gap

The missing step is removal of the biclique-cover hypothesis. Nothing above does that.

The restriction is substantial. If a bipartite graph is \(C_4\)-free, every biclique is a star. If such a graph is \(\Delta\)-regular on \(n\) vertices and has a cover of load at most \(r\) at every vertex, then
\[
\frac{\Delta n}{2}
=|E(G)|
\leq\sum_i |E(K_i)|
\leq\sum_i |V(K_i)|
\leq rn.
\]
Hence
\[
r\geq\frac{\Delta}{2}.
\]
Our logarithmic-list constant \(3\cdot2^r\) consequently gives no useful conjectured-scale bound on this family.

Thus the conclusions established here are:

- clause **(i)** for every fixed-load biclique-cover class;
- clause **(ii)** for that class, with \(C=3\cdot2^r\);
- the \(k_B\)-branch of clause **(iii)** for load \((r,1)\), with \(C=8r\), and the exchanged version for load \((1,r)\).

The unrestricted Conjecture 7 is not settled here. The arguments are self-contained apart from standard probabilistic lemmas, but I have not verified novelty of these structural special cases and would not present them as a new publishable resolution.