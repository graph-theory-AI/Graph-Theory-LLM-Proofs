```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the target if either hypergraph has sublinear pair-codegree, and for 3-uniform pairs with a common vertex cover of size o(min(m_1,m_2)^(1/3)).",
  "would_publish": false,
  "caveats": "The unrestricted problem is not resolved; literature novelty of these sufficient conditions has not been checked."
}
```

## 1. Statements of the partial results

Hypergraphs are finite and simple, and \(r\) is fixed. Write
\[
p_r=\frac{r!}{r^r},\qquad
\Delta_2(H)=\max_{\{u,v\}\subseteq V}|\{e\in E(H):\{u,v\}\subseteq e\}|.
\]
For a coloring \(\phi:V\to[r]\), let \(X_H(\phi)\) count the rainbow edges of \(H\).

I prove three sufficient conditions.

**Theorem A — only one small pair-codegree is needed.**  
For \(r\ge2\) and \(m_1,m_2>0\), put
\[
\delta=\min_{i=1,2}\frac{\Delta_2(H_i)}{m_i},
\qquad
\eta=\left[\binom r2 p_r(1-p_r)^2\delta\right]^{1/3}.
\]
There is an \(r\)-partition satisfying
\[
X_{H_i}\ge (p_r-\eta)m_i\qquad(i=1,2).
\]
Consequently, the conjectured conclusion holds whenever **either** hypergraph has \(\Delta_2(H_i)=o(m_i)\); no codegree restriction is imposed on the other one.

This weakens the hypotheses of the sufficient condition stated in the supplied catalog, though I do not claim literature novelty.

**Theorem B — a common exact transversal.**  
Suppose there is a set \(U\subseteq V\) such that every edge of both hypergraphs contains exactly one vertex of \(U\). Then there is an \(r\)-partition satisfying
\[
X_{H_i}\ge
\frac{p_{r-1}}{2-p_{r-1}}\,m_i
>p_rm_i
\qquad(i=1,2).
\]
Here \(p_1=1\). There is no asymptotic error, and both pair-codegrees may be linear in their edge counts.

**Theorem C — small common vertex cover for triples.**  
Suppose \(r=3\), let \(M=\min(m_1,m_2)\), and suppose \(H_1\cup H_2\) has a vertex cover of size \(k\). There is a partition into three classes satisfying
\[
X_{H_i}\ge
\left(\frac29-O\!\left(\frac{k^3}{M}+M^{-1/7}\right)\right)m_i
\qquad(i=1,2),
\]
with an absolute implied constant.

Thus the conjecture holds for \(r=3\) if
\[
k=o(M^{1/3}).
\]
In particular, it holds when each hypergraph has bounded vertex-cover number, even if both have linear maximum pair-codegree.

The case \(r=1\) is trivial, and zero-edge objectives can simply be omitted.

## 2. Rainbow moments

Color vertices independently and uniformly from \([r]\). For an edge \(e\), let \(I_e\) be its rainbow indicator. Then
\[
\mathbb E I_e=p_r.
\]
If \(e,f\) are \(r\)-sets with \(|e\cap f|=t\), then
\[
\mathbb E(I_eI_f)
=p_r\frac{(r-t)!}{r^{r-t}}
=\frac{r!(r-t)!}{r^{2r-t}}. \tag{1}
\]
Indeed, after \(e\) is rainbow, the \(r-t\) remaining vertices of \(f\) must receive the \(r-t\) colors absent from \(e\cap f\), in some order.

Two consequences will be useful:

* When \(t=0\) or \(t=1\), the covariance is zero.
* For every \(t\), the covariance is nonnegative, since
  \[
  \frac{(r-t)!/r^{r-t}}{p_r}
  =\frac{r^t}{r(r-1)\cdots(r-t+1)}\ge1.
  \]

For an \(r\)-uniform hypergraph \(H\) with \(m\) edges,
\[
\begin{aligned}
\operatorname{Var}X_H
&\le p_r(1-p_r)
 \big|\{(e,f)\in E(H)^2:|e\cap f|\ge2\}\big|\\
&\le p_r(1-p_r)
 \sum_{e\in E(H)}\sum_{\substack{P\subseteq e\\|P|=2}}d_H(P)\\
&\le \binom r2p_r(1-p_r)m\Delta_2(H). \tag{2}
\end{aligned}
\]
The pairs in the first line are ordered, and the diagonal is included.

## 3. Proof of Theorem A

The probabilistic point is that concentration of just one objective suffices if an \(o(1)\) relative loss is permitted in the other.

### A two-variable lemma

Let \(Y_1,Y_2\in[0,1]\) satisfy
\[
\mathbb EY_1=\mathbb EY_2=p,\qquad \operatorname{Var}Y_1=v.
\]
For every \(a>0\), some outcome satisfies
\[
Y_1\ge p-a,\qquad
Y_2\ge p-(1-p)\frac{v}{a^2}. \tag{3}
\]

To prove this, let \(G=\{Y_1\ge p-a\}\) and \(q=\mathbb P(G^c)\). The one-sided Chebyshev inequality gives
\[
q\le \frac{v}{v+a^2}<1.
\]
Since \(Y_2\le1\),
\[
\begin{aligned}
\mathbb E(Y_2\mid G)
&\ge \frac{p-q}{1-q}\\
&=p-(1-p)\frac{q}{1-q}\\
&\ge p-(1-p)\frac{v}{a^2}.
\end{aligned}
\]
Choose an outcome in \(G\) at which \(Y_2\) is at least its conditional mean. If \(v=0\), the assertion follows directly.

### Application to hypergraphs

Swap the indices if necessary so that
\[
\frac{\Delta_2(H_1)}{m_1}=\delta.
\]
Set \(Y_i=X_{H_i}/m_i\). By (2),
\[
v=\operatorname{Var}Y_1
\le \binom r2p_r(1-p_r)\delta.
\]
Take
\[
a=\eta=
\left[\binom r2p_r(1-p_r)^2\delta\right]^{1/3}.
\]
Then
\[
(1-p_r)\frac{v}{a^2}\le a.
\]
Equation (3) proves Theorem A.

No independence between the two objectives was used.

## 4. A weighted simultaneous bound

The next lemma supplies the structured high-codegree cases.

**Lemma.** Let \(F_1,F_2\) be two nonnegatively weighted \(s\)-uniform hypergraphs, with total weights \(W_1,W_2\). There is an \(s\)-coloring retaining rainbow weight at least
\[
c_sW_i,\qquad
c_s:=\frac{p_s}{2-p_s},
\]
for both \(i=1,2\).

**Proof.** First suppose both total weights are positive. Under a uniformly random \(s\)-coloring, let \(A_i\in[0,1]\) be the rainbow fraction of \(F_i\). Equation (1), applied termwise to the weighted sums, gives
\[
\mathbb EA_i=p_s,\qquad
\mathbb E(A_1A_2)\ge p_s^2. \tag{4}
\]

Let
\[
t=\max_{\phi}\min(A_1(\phi),A_2(\phi)).
\]
Whenever \(a,b\in[0,1]\) and \(\min(a,b)\le t\),
\[
ab\le \frac{t}{1+t}(a+b). \tag{5}
\]
For example, if \(a\le b\), then
\[
\frac{ab}{a+b}\le \frac{a}{1+a}\le\frac{t}{1+t},
\]
with the zero case interpreted directly.

Taking expectations in (5) and using (4),
\[
p_s^2\le \frac{t}{1+t}\,2p_s.
\]
Hence \(t\ge p_s/(2-p_s)\).

If one total weight is zero, only the other objective matters; its expected rainbow weight is \(p_sW_i\ge c_sW_i\). ∎

In particular, two weighted graphs always have a common bipartition cutting at least one third of the weight of each.

### Proof of Theorem B

Put \(S=V\setminus U\). Project every edge \(e\) onto its \((r-1)\)-set \(e\setminus U\), retaining multiplicities as weights. This gives two weighted \((r-1)\)-uniform hypergraphs on \(S\), each with total weight \(m_i\).

Apply the lemma to partition \(S\) into \(r-1\) classes, and use \(U\) as the last class. An original edge is rainbow exactly when its projection is rainbow. Thus
\[
X_{H_i}\ge c_{r-1}m_i.
\]

Finally, for \(s\ge1\),
\[
\frac{p_{s+1}}{p_s}
=\left(\frac{s}{s+1}\right)^s\le\frac12,
\]
because \((1+1/s)^s\ge2\). Therefore
\[
c_s=\frac{p_s}{2-p_s}>\frac{p_s}{2}\ge p_{s+1},
\]
as required. ∎

## 5. Proof of Theorem C

I prove an explicit finite estimate.

Let \(T\) be a common vertex cover of size \(k\), and fix \(0<\gamma\le1\). For \(i=1,2\), write \(d_i(v)\) for the degree of \(v\) in \(H_i\). Set
\[
A=\{v:d_1(v)>\gamma m_1\text{ or }d_2(v)>\gamma m_2\},
\qquad S=T\cup A.
\]
Since each hypergraph is 3-uniform,
\[
|A|\le \frac6\gamma.
\]
Thus, with
\[
L=k+\left\lceil\frac6\gamma\right\rceil,
\]
we have
\[
|S|\le L,\qquad
d_i(v)\le\gamma m_i\quad(v\notin S). \tag{6}
\]

Every edge meets \(S\). Let \(m_{i,j}\) count the edges of \(H_i\) meeting \(S\) in exactly \(j\) vertices. In particular,
\[
m_{i,3}\le\binom L3. \tag{7}
\]

### Choosing the colors on \(S\)

For each \(i\), form a weighted graph \(G_i\) on \(S\): the weight of \(xy\) is the number of edges \(e\in H_i\) with
\[
e\cap S=\{x,y\}.
\]
Its total weight is \(m_{i,2}\).

By the weighted lemma with \(s=2\), choose a bipartition of \(S\) cutting at least \(m_{i,2}/3\) weight in each \(G_i\). Give these two parts colors 1 and 2.

Independently color each vertex outside \(S\) with probabilities
\[
\mathbb P(1)=\frac16,\qquad
\mathbb P(2)=\frac16,\qquad
\mathbb P(3)=\frac23. \tag{8}
\]

An edge meeting \(S\) once has rainbow probability
\[
2\cdot\frac16\cdot\frac23=\frac29,
\]
regardless of whether its vertex in \(S\) has color 1 or 2.

An edge meeting \(S\) twice has rainbow probability \(2/3\) if its two vertices in \(S\) lie on opposite sides, and zero otherwise. Consequently,
\[
\begin{aligned}
\mathbb EX_{H_i}
&\ge \frac29m_{i,1}
   +\frac23\cdot\frac13m_{i,2}\\
&=\frac29(m_i-m_{i,3}). \tag{9}
\end{aligned}
\]

### Concentration after fixing \(S\)

The colors on \(S\) are now fixed. Indicators of two edges are independent whenever their sets of vertices outside \(S\) are disjoint. Bounding every remaining covariance above by 1 gives
\[
\begin{aligned}
\operatorname{Var}X_{H_i}
&\le \sum_{v\notin S}d_i(v)^2\\
&\le \gamma m_i\sum_{v\notin S}d_i(v)\\
&\le 2\gamma m_i^2. \tag{10}
\end{aligned}
\]
The last inequality holds because every edge meets \(S\), so it has at most two vertices outside \(S\).

Chebyshev's inequality therefore yields
\[
\mathbb P\!\left(
X_{H_i}<\mathbb EX_{H_i}-3\sqrt{\gamma}\,m_i
\right)\le\frac29.
\]
The union of the two bad events has probability at most \(4/9\). Some coloring consequently satisfies, for both \(i\),
\[
X_{H_i}\ge
\frac29\left(m_i-\binom L3\right)
-3\sqrt{\gamma}\,m_i. \tag{11}
\]

This is the promised finite estimate.

Now set \(M=\min(m_1,m_2)\) and choose
\[
\gamma=M^{-2/7}.
\]
Then
\[
L\le k+6M^{2/7}+1,
\qquad
\binom L3=O(k^3+M^{6/7}).
\]
Dividing (11) by \(m_i\ge M\) gives
\[
\frac{X_{H_i}}{m_i}
\ge \frac29-
O\!\left(\frac{k^3}{M}+M^{-1/7}\right).
\]
This proves Theorem C. ∎

## 6. What remains unresolved

These arguments do not handle two unrestricted hypergraphs when both pair-codegrees are linear and neither of the structural hypotheses applies.

The weighted lemma alone gives only
\[
\frac{p_r}{2-p_r}<p_r,
\]
so it does not prove the conjecture. Nonnegative covariance also cannot simply be upgraded to simultaneous attainment of both expectations. For example, take two complementary 5-cycles on the same five vertices. Cutting at least \(5/2\) edges of each would require cutting at least four edges of each, since every cut of a cycle has even size. That would cut at least eight edges of \(K_5\), whereas a cut of \(K_5\) has at most six.

That finite example is **not** a counterexample to the asymptotic problem. It identifies the gap in a tempting moment-only proof. Theorems A–C avoid that gap through, respectively, concentration of one objective, an exact transversal structure, and a controlled treatment of a small vertex cover.