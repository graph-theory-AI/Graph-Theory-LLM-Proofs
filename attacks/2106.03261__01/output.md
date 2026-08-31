```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Neither graph is resolved, but exact closure formulations reduce Petersen countability to one sparse check and dodecahedral countability to two, and a natural family of critical C4-free Cayley lifts has the correct count for a positive proportion of its parameters.",
  "would_publish": false,
  "caveats": "The full closure-mixing estimates remain unproved, and no counterexample sequence is constructed."
}
```

## Mathematical writeup

### 1. Setup and status

Let \(F\) be a fixed graph with vertices indexed by pairwise disjoint classes \((V_x)_{x\in V(F)}\), each of size \(n\). A canonical copy of \(F\) maps each \(x\) into \(V_x\).

The critical regime is
\[
p=n^{-1/2}.
\]
If every required pair has density \(\Theta(p)\), the random benchmark for the number of canonical copies is
\[
n^{v(F)}p^{e(F)}.
\]
Thus the benchmarks are
\[
n^{10}p^{15}=n^{5/2}
\quad\text{for the Petersen graph,}
\]
and
\[
n^{20}p^{30}=n^5
\quad\text{for the dodecahedral graph.}
\]

The exact source definition has quantitative regularity and error parameters, but all arguments below apply to the standard core case in which every required pair is \((\varepsilon,p)\)-regular and has density at least \(\alpha p\), with fixed \(\alpha>0\).

I do not obtain the required universal lower bounds. The following reductions identify the precise remaining correlations.

---

## 2. Common-neighbor closure

The elementary fact driving the argument is the following.

### Lemma 2.1
If \(G\) is \(C_4\)-free, then any two distinct vertices of \(G\) have at most one common neighbor.

#### Proof
Two distinct common neighbors would form a \(4\)-cycle with the given pair. ∎

This gives a useful general closure lemma.

### Lemma 2.2
Let \(F\) be cubic, and let \(S\subseteq V(F)\) be such that \(F-S\) is a forest. In every \(C_4\)-free graph with disjoint canonical classes, a canonical copy of \(F\) is uniquely determined by the images of \(S\).

Consequently,
\[
N_F(G;\{V_x\})\leq \prod_{s\in S}|V_s|.
\]

#### Proof
Since \(F-S\) is a forest, its vertices admit an ordering
\[
x_1,\dots,x_t
\]
such that \(x_i\) has at most one neighbor among \(x_i,\dots,x_t\). Because \(F\) is cubic, \(x_i\) therefore has at least two neighbors in
\[
S\cup\{x_1,\dots,x_{i-1}\}.
\]
Fix two such earlier neighbors as the parents of \(x_i\).

Once the images of the earlier vertices are known, the image of \(x_i\) must be their common neighbor in \(V_{x_i}\). By Lemma 2.1 there is at most one choice. Induction proves uniqueness. ∎

When \(S\) is independent, choosing two parent edges for every vertex of \(F-S\) uses exactly \(2(v(F)-|S|)\) edges. The number of remaining “check edges” is therefore
\[
r=e(F)-2(v(F)-|S|)
  =2|S|-\frac{v(F)}2.
\]
At critical density, the heuristic count is then
\[
n^{|S|}p^r=n^{v(F)/4},
\]
which is exactly the random benchmark for a cubic graph. Thus the entire issue is whether the closure maps hit the remaining \(r\) sparse pairs with the expected frequency.

---

## 3. Exact Petersen reduction: three seeds and one check

Use the Kneser representation of the Petersen graph: its vertices are the \(2\)-subsets of \(\{1,2,3,4,5\}\), with disjoint pairs adjacent. Write
\[
\begin{aligned}
a&=12,& b&=13,& c&=14,\\
d&=45,& e&=35,& f&=25,\\
g&=23,& h&=24,& i&=34,& j&=15.
\end{aligned}
\]

The set
\[
S_P=\{a,b,c\}
\]
is independent, and the remaining seven vertices induce the tree with center \(j\) after an appropriate ordering. More explicitly, starting from images \(A,B,C\), perform the following closures:

\[
\begin{array}{c|c}
\text{new vertex}&\text{parents}\\ \hline
d&(a,b)\\
e&(a,c)\\
f&(b,c)\\
g&(c,d)\\
h&(b,e)\\
i&(a,f)\\
j&(g,h)
\end{array}
\]

All fourteen corresponding parent edges are Petersen edges. The only unused Petersen edge is
\[
ij.
\]

Writing \(\kappa_x(y,z)\) for the unique common neighbor of \(y,z\) in \(V_x\), when it exists, the recursion is
\[
\begin{aligned}
D&=\kappa_d(A,B),&
E&=\kappa_e(A,C),&
F&=\kappa_f(B,C),\\
G&=\kappa_g(C,D),&
H&=\kappa_h(B,E),&
I&=\kappa_i(A,F),\\
J&=\kappa_j(G,H).
\end{aligned}
\]

Let \(\Omega_P\subseteq V_a\times V_b\times V_c\) be the set of seed triples for which every displayed closure is defined. Then the following is an exact identity:
\[
N_P(G)
=
\sum_{(A,B,C)\in\Omega_P}
1_G\bigl(I(A,B,C),J(A,B,C)\bigr).
\tag{3.1}
\]

In particular,
\[
N_P(G)\leq n^3.
\tag{3.2}
\]

The benchmark is \(n^{5/2}=pn^3\). Hence Petersen countability is reduced to proving two statements:

1. \(|\Omega_P|=\Omega(n^3)\), with the appropriate density factors;
2. the closure endpoints \(I,J\) hit the final regular pair \(V_iV_j\) with frequency \(\Omega(p)\).

The second point is a genuinely weighted sparse-mixing assertion; ordinary pair regularity does not directly imply it.

---

## 4. Exact dodecahedral reduction: six seeds and two checks

Represent the dodecahedral graph as the generalized Petersen graph \(G(10,2)\). Its vertices are
\[
u_0,\dots,u_9,\qquad v_0,\dots,v_9,
\]
with edges
\[
u_i u_{i+1},\qquad u_iv_i,\qquad v_iv_{i+2},
\]
where indices are modulo \(10\).

Take
\[
S_D=\{v_0,v_1,u_2,u_4,u_6,u_8\}.
\]
This is independent. Deleting it leaves two trees:

- the path \(v_2-v_4-v_6-v_8\);
- the tree formed from the path \(v_3-v_5-v_7-v_9\), with leaves \(u_3,u_5,u_7\) and the attached path
  \[
  v_9-u_9-u_0-u_1.
  \]

An explicit closure order and parent choice is:

\[
\begin{array}{c|c}
\text{new vertex}&\text{parents}\\ \hline
v_2&(v_0,u_2)\\
v_4&(v_2,u_4)\\
v_6&(v_4,u_6)\\
v_8&(v_6,v_0)\\
u_3&(u_2,u_4)\\
u_5&(u_4,u_6)\\
u_7&(u_6,u_8)\\
u_1&(u_2,v_1)\\
u_0&(u_1,v_0)\\
u_9&(u_0,u_8)\\
v_3&(v_1,u_3)\\
v_5&(v_3,u_5)\\
v_7&(v_5,u_7)\\
v_9&(v_7,v_1)
\end{array}
\]

These use \(28\) of the \(30\) dodecahedral edges. The two unused check edges can be taken to be
\[
u_8v_8,\qquad u_9v_9.
\]

Let \(\Omega_D\) be the set of six seed assignments for which all fourteen closures are defined. If \(\Phi_x(\mathbf z)\) denotes the resulting image of \(x\), then
\[
N_D(G)
=
\sum_{\mathbf z\in\Omega_D}
1_G\bigl(\Phi_{u_8}(\mathbf z),\Phi_{v_8}(\mathbf z)\bigr)
1_G\bigl(\Phi_{u_9}(\mathbf z),\Phi_{v_9}(\mathbf z)\bigr).
\tag{4.1}
\]

Consequently,
\[
N_D(G)\leq n^6.
\tag{4.2}
\]

The desired benchmark is
\[
n^5=p^2n^6.
\]
Thus dodecahedral countability asks for two simultaneous sparse check-edge savings after a six-variable common-neighbor closure.

---

## 5. What regularity proves at the first closure layer

There is a useful densification fact.

### Lemma 5.1
Let \(A,B,X\) be disjoint sets of size \(n\) in a \(C_4\)-free graph. Suppose \((A,X)\) and \((B,X)\) are \((\varepsilon,p)\)-regular, in the relative additive sense, and have densities \(d_A,d_B\geq\alpha p\).

Define an auxiliary graph \(Q_X\) on \(A\cup B\) by
\[
ab\in E(Q_X)
\quad\Longleftrightarrow\quad
a,b\text{ have a common neighbor in }X.
\]
For all \(A'\subseteq A,B'\subseteq B\) with \(|A'|,|B'|\geq\varepsilon n\),
\[
e_{Q_X}(A',B')
\geq
(1-2\varepsilon)n(d_A-\varepsilon p)(d_B-\varepsilon p)
|A'||B'|.
\tag{5.1}
\]

In particular, when \(p=n^{-1/2}\), \(Q_X\) is a dense lower-regular graph of density bounded below by a positive constant depending only on \(\alpha\).

#### Proof
For fixed \(A'\), all but at most \(\varepsilon n\) vertices \(x\in X\) satisfy
\[
\deg_{A'}(x)\geq(d_A-\varepsilon p)|A'|;
\]
otherwise the exceptional vertices would contradict regularity. The analogous statement holds for \(B'\). Hence at least \((1-2\varepsilon)n\) vertices satisfy both inequalities.

By \(C_4\)-freeness, a pair \((a,b)\in A'\times B'\) has at most one common neighbor. Therefore
\[
e_{Q_X}(A',B')
=
\sum_{x\in X}\deg_{A'}(x)\deg_{B'}(x),
\]
and restricting the sum to the good vertices gives (5.1). ∎

### Consequences

For the Petersen closure, define auxiliary dense graphs:

- \(Q_d\) on \(V_a\times V_b\);
- \(Q_e\) on \(V_a\times V_c\);
- \(Q_f\) on \(V_b\times V_c\).

Lemma 5.1 makes all three dense and lower-regular. The ordinary dense triangle argument therefore gives
\[
\Omega(n^3)
\]
seed triples \((A,B,C)\) for which the first three closures \(D,E,F\) all exist.

For the dodecahedral closure, the first five immediately available operations give auxiliary constraints on the seed pairs
\[
(v_0,u_2),\ (u_2,u_4),\ (u_4,u_6),\ (u_6,u_8),\ (u_2,v_1).
\]
These form a tree on the six seed classes. Dense lower-regular tree counting therefore gives \(\Omega(n^6)\) seed tuples for which
\[
v_2,\ u_3,\ u_5,\ u_7,\ u_1
\]
are all defined.

The obstacle to iteration is that the output of one common-neighbor map is a highly structured “color” of an auxiliary dense edge. For example, the next Petersen condition asks that
\[
(C,D)\in Q_g,
\qquad D=\kappa_d(A,B).
\]
Lower-regularity of \(Q_g\) controls rectangles \(C'\times D'\), but not the correlated distribution of pairs \((C,\kappa_d(A,B))\). This is the first genuinely missing estimate.

---

## 6. A critical \(C_4\)-free Cayley model

The following shows that a natural algebraic family of globally \(C_4\)-free, macroscopically regular hosts has the correct number of copies for a positive proportion of its parameters.

### Proposition 6.1
For \(F\) equal to the Petersen or dodecahedral graph, there are infinitely many \(n\) and families of \(F\)-partite \(C_4\)-free graphs with all required pair densities \(\Theta(n^{-1/2})\) and relative discrepancy tending to zero, such that a positive proportion of the graphs in the family contain
\[
\Omega\!\left(n^{v(F)}\prod_{e\in E(F)}p_e\right)
=
\Omega\!\left(n^{v(F)-e(F)/2}\right)
\]
canonical copies of \(F\).

Thus the lower bounds are \(\Omega(n^{5/2})\) for Petersen and \(\Omega(n^5)\) for the dodecahedron.

#### Construction

Let \(q\) be an odd prime,
\[
\Gamma=\mathbb F_q^2,\qquad n=|\Gamma|=q^2,
\]
and let
\[
D=\{(t,t^2):t\in\mathbb F_q\}.
\]

The set \(D\) is Sidon in the ordered-difference sense: if
\[
(t,t^2)-(u,u^2)=(t',t'^2)-(u',u'^2)\neq0,
\]
then the first coordinate gives \(t-u=t'-u'\neq0\), and the second gives
\[
(t-u)(t+u)=(t'-u')(t'+u').
\]
Hence \(t+u=t'+u'\), and odd characteristic gives \(t=t'\), \(u=u'\).

Properly edge-color \(F\) with at most five colors; the elementary greedy bound suffices because every edge is adjacent to at most four others. Randomly partition \(D\) into five sets
\[
S_1,\dots,S_5.
\]
One can choose a partition satisfying
\[
|S_c|=(1+o(1))q/5
\tag{6.1}
\]
and
\[
\max_{\chi\neq1}\left|\sum_{s\in S_c}\chi(s)\right|
=O(\sqrt{q\log q})=o(q).
\tag{6.2}
\]
Indeed, the nontrivial character sums over \(D\) are linear or quadratic Gauss sums, of magnitude at most \(\sqrt q\), and concentration plus a union bound over the \(q^2\) characters proves existence of the partition.

Orient every template edge \(e=ij\). Give it the set \(S_{c(e)}\) corresponding to its color and an arbitrary translation \(\tau_e\in\Gamma\). Put an edge between \(x\in V_i=\Gamma\) and \(y\in V_j=\Gamma\) when
\[
y-x\in \tau_e+S_{c(e)}.
\tag{6.3}
\]

#### \(C_4\)-freeness

Within a single pair \(V_i,V_j\), two vertices of \(V_i\) cannot have two common neighbors because \(S_{c(e)}\) is Sidon.

If two vertices in \(V_i\) had common neighbors in two different adjacent classes corresponding to incident edges \(e,f\), their difference would lie in both
\[
\Delta S_{c(e)}
=\{s-s':s,s'\in S_{c(e)},\,s\neq s'\}
\]
and \(\Delta S_{c(f)}\). Distinct color classes are disjoint subsets of the Sidon set \(D\), so these difference sets are disjoint.

Finally, a \(4\)-cycle using four distinct classes would project to a \(4\)-cycle in \(F\), which neither Petersen nor the dodecahedron has. Thus the whole graph is \(C_4\)-free.

#### Relative regularity

The density in an edge pair is
\[
p_e=\frac{|S_{c(e)}|}{n}=(1+o(1))\frac1{5\sqrt n}.
\]
Fourier expansion of the bipartite Cayley graph gives, for \(X,Y\subseteq\Gamma\),
\[
\left|e(X,Y)-p_e|X||Y|\right|
\leq
\lambda_e\sqrt{|X||Y|},
\]
where
\[
\lambda_e=\max_{\chi\neq1}|\widehat{1_{S_{c(e)}}}(\chi)|
=o(\sqrt n).
\]
Since \(\lambda_e/|S_{c(e)}|\to0\), these pairs are \((\varepsilon,p_e)\)-regular for every fixed \(\varepsilon>0\) once \(q\) is sufficiently large.

#### Second moment over translations

Choose the \(\tau_e\) independently and uniformly from \(\Gamma\), and let \(N_F\) be the canonical \(F\)-count. For every vertex tuple,
\[
\Pr(\text{it is a copy})=\prod_ep_e,
\]
so
\[
\mu:=\mathbb E N_F=n^{v(F)}\prod_ep_e.
\tag{6.4}
\]

For two tuples \(x=(x_i)\) and \(y=(y_i)\), put \(z_i=y_i-x_i\). For an edge \(e=ij\), the two constraints on \(\tau_e\) differ by \(z_j-z_i\). If \(z_i=z_j\), their joint probability is \(p_e\). Otherwise it is at most \(1/n\), by the Sidon property.

Let
\[
m(z)=|\{ij\in E(F):z_i=z_j\}|.
\]
As all \(p_e=\Theta(n^{-1/2})\),
\[
\mathbb E(1_x1_y)
\leq
C_F\left(\prod_ep_e^2\right)n^{m(z)/2}.
\tag{6.5}
\]

Group \(z\) according to its equality partition \(\pi\), with \(k\) blocks. There are at most \(n^k\) assignments with a given partition. If \(m(\pi)\) denotes the number of edges internal to its blocks, then
\[
m(\pi)\leq 2(v(F)-k).
\tag{6.6}
\]
Indeed, for a block of size \(b\), its induced subgraph has at most \(2(b-1)\) edges: this is immediate for \(b\leq3\), while for \(b\geq4\), cubicity gives
\[
e(B)\leq \frac{3b}{2}\leq2(b-1).
\]
Summing over blocks proves (6.6).

Consequently,
\[
\sum_z n^{m(z)/2}=O_F(n^{v(F)}),
\]
and (6.5) yields
\[
\mathbb E N_F^2=O_F(\mu^2).
\]
Paley–Zygmund now gives a constant \(c_F>0\) such that
\[
\Pr(N_F\geq \mu/2)\geq c_F.
\]
This proves Proposition 6.1. ∎

This result is only generic in the translation parameters. It does not show that every translation has the required count.

---

## 7. The exact unresolved estimates

For Petersen, formula (3.1) requires
\[
\sum_{(A,B,C)\in\Omega_P}
1_G(I(A,B,C),J(A,B,C))
\geq cpn^3.
\tag{7.1}
\]
Neither \((\varepsilon,p)\)-regularity nor balanced one-coordinate marginals is enough abstractly. For example, if \(E\subseteq V_i\times V_j\) is a regular pair of density \(p\), the weight
\[
w(x,y)=n\,1_{(x,y)\notin E}
\]
has total mass \((1-o(1))n^3\) and balanced large marginals, yet
\[
\sum_{xy\in E}w(x,y)=0.
\]
Of course, it is not shown that such a weight can arise from the Petersen closure map. Proving that it cannot is essentially the missing structural theorem.

For the dodecahedron, the needed assertion is the still stronger two-edge correlation
\[
\sum_{\mathbf z\in\Omega_D}
1_{u_8v_8}(\mathbf z)\,1_{u_9v_9}(\mathbf z)
\geq cp^2n^6.
\tag{7.2}
\]

The supplied source-paper methods evidently control analogous expressions when the closure dependency graph decomposes into their “islands and bridges.” The above closure systems retain a cyclic dependence of common-neighbor colors, and I do not see a valid way to decorrelate the final checks.

---

## 8. A fully specified computational subproblem

The Cayley model gives a finite search space.

For fixed \(q\), a proper edge-coloring, and sets \(S_c\), orient \(F\) and search over translations \((\tau_e)\). Vertex coordinate changes
\[
x_i\mapsto x_i+a_i
\]
replace
\[
\tau_{ij}\mapsto \tau_{ij}+a_j-a_i.
\]
Thus translations on a spanning tree may be fixed to zero. Only
\[
e(F)-v(F)+1
\]
cycle voltages remain:

- \(6\) elements of \(\Gamma\) for Petersen;
- \(11\) elements of \(\Gamma\) for the dodecahedron.

For each voltage assignment one counts solutions of
\[
x_j-x_i\in \tau_{ij}+S_{c(ij)}
\]
with one vertex coordinate fixed to zero. A sequence of assignments with
\[
N_P=o(q^5)
\quad\text{or}\quad
N_D=o(q^{10})
\]
would produce a counterexample sequence inside this model. I have not run this computation and claim no small-\(q\) result.

---

## 9. Conclusion

The problem remains unresolved. The rigorous partial conclusions are:

1. Petersen copies are determined by three independent seed images and one final sparse edge check; hence \(N_P\leq n^3\).
2. Dodecahedral copies are determined by six independent seed images and two final sparse edge checks; hence \(N_D\leq n^6\).
3. Regularity and \(C_4\)-freeness make each individual common-neighbor domain dense and lower-regular, yielding the correct number of first-layer closures.
4. A natural critical \(C_4\)-free Cayley-lift family has the expected Petersen and dodecahedral counts for a positive proportion of translation parameters.
5. The unproved step is a weighted mixing theorem for recursively composed common-neighbor maps, specifically (7.1) and (7.2).