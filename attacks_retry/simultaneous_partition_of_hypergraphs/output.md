```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an unconditional simultaneous fraction p_r/(2-rp_r), improve it to 0.1868886-o(1) for triples, and establish the conjectured bound under a clustered-codegree condition.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains unresolved; r is fixed, hypergraphs are simple, and novelty of these partial results is unverified."
}
```

# 1. Results and scope

Write
\[
p_r=\frac{r!}{r^r},
\qquad
X_i(\phi)=|\{e\in E(H_i):\phi|_e\text{ is injective}\}|,
\]
where \(\phi:V\to[r]\). Throughout, hypergraphs are finite and simple, \(r\) is fixed, and
\[
M=\min(m_1,m_2).
\]

I do **not** obtain \(X_i\ge p_rm_i-o(m_i)\) for unrestricted pairs. I obtain the following partial results.

### Theorem 1 — an unconditional bound

For every fixed \(r\ge2\), there is a constant \(C_r\) such that any two \(r\)-uniform hypergraphs with \(m_1,m_2>0\) have a common \(r\)-partition satisfying
\[
X_i\ge
\left(
\frac{p_r}{2-rp_r}
-C_rM^{-1/(2r+1)}
\right)m_i
\qquad(i=1,2).
\tag{1}
\]

For \(r=2\), the main term is \(m_i/2\), so this also gives an elementary, non-sharp proof of the asymptotic graph case. For \(r=3\), the main term in (1) is \(m_i/6\).

### Theorem 2 — a stronger unconditional bound for triples

Put
\[
\tau=\frac{15-\sqrt{41}}{46}=0.1868886035\ldots.
\]
There is an absolute constant \(C\) such that any two 3-uniform hypergraphs have a common 3-partition satisfying
\[
X_i\ge \bigl(\tau-CM^{-1/7}\bigr)m_i
\qquad(i=1,2).
\tag{2}
\]

The conjectured fraction is \(2/9=0.222222\ldots\), so (2) does not settle it.

### Theorem 3 — the target under clustered large codegrees

Let \(\mathcal B\) be a partition of \(V\) into blocks of size at most \(r\). Define
\[
D_{\mathcal B}(H)=
\max_{\substack{B,C\in\mathcal B\\B\ne C}}
|\{e\in E(H):e\cap B\ne\varnothing,\ e\cap C\ne\varnothing\}|,
\tag{3}
\]
with maximum zero if there are no two blocks.

Set
\[
\delta=\frac{D_{\mathcal B}(H_1)}{m_1},
\qquad
\eta=\left[\frac{1-p_r}{4}\binom r2\,\delta\right]^{1/3}.
\]
Then a common \(r\)-partition exists with
\[
X_i\ge(p_r-\eta)m_i
\qquad(i=1,2).
\tag{4}
\]

In particular, the conjecture holds if **either** hypergraph admits such block partitions with
\[
D_{\mathcal B}(H_i)=o(m_i);
\]
the other hypergraph is unrestricted.

This permits linear pair-codegrees inside the blocks. For example, it applies when \(H_1\) is a growing sunflower with a fixed core of size between \(2\) and \(r-1\), even if \(H_2\) has no small vertex cover and also has linear maximum pair-codegree.

The covariance and conditioning ideas from the supplied attempt are valid. I reprove the forms used below. No literature claim is needed for these arguments.

# 2. Two elementary probabilistic lemmas

## 2.1. Injectivity events have nonnegative covariance

Color vertices independently and uniformly from \([k]\). For a set \(A\), with \(|A|\le k\), let \(J_A\) indicate that its vertices receive distinct colors. Define
\[
\pi_{k,t}=\frac{(k)_t}{k^t},\qquad \pi_{k,0}=1.
\]

If \(|A|=a\), \(|B|=b\), and \(|A\cap B|=c\), then
\[
\mathbb E(J_AJ_B)
=\frac{\pi_{k,a}\pi_{k,b}}{\pi_{k,c}}
\ge \pi_{k,a}\pi_{k,b}.
\tag{5}
\]
Indeed, conditional on \(A\) being injectively colored, the \(b-c\) additional vertices of \(B\) must receive distinct colors avoiding the \(c\) colors on \(A\cap B\).

Consequently, any two nonnegative weighted sums of such indicators have nonnegative covariance.

In particular, the normalized cut weights of two weighted graphs under a uniform \(k\)-coloring have common mean
\[
q=\frac{k-1}{k}
\]
and nonnegative covariance.

## 2.2. Simultaneous thresholds from a mixed moment

Suppose \(A,B\in[0,1]\) are random variables on a finite probability space and
\[
\mathbb EA=\mathbb EB=q,\qquad
\mathbb E(AB)\ge q^2.
\tag{6}
\]

Then some outcome satisfies
\[
A,B\ge\frac{q}{2-q}.
\tag{7}
\]

To see this, let \(t=\max\min(A,B)\). Pointwise,
\[
AB\le \frac{t}{1+t}(A+B).
\]
Taking expectations gives
\[
q^2\le\frac{2qt}{1+t},
\]
which proves (7).

We also need an asymmetric version. If \(0<q<1\), \(a,b\in[0,q]\), and
\[
q-a-b+(2-q)ab\ge0,
\tag{8}
\]
then some outcome satisfies
\[
A\ge a,\qquad B\ge b.
\tag{9}
\]

If one threshold is zero, this follows from the mean of the other variable. Otherwise, on the region \(x\le a\) or \(y\le b\),
\[
xy\le
\frac{b(1-a)}{1-ab}\,x+
\frac{a(1-b)}{1-ab}\,y.
\tag{10}
\]
This follows by checking the corners of the two rectangles. If (9) were impossible, taking expectations in (10) would give
\[
q^2\le q\,\frac{a+b-2ab}{1-ab}.
\]
This contradicts the strict version of (8). The non-strict case follows by decreasing the thresholds slightly and using finiteness of the probability space. Indeed, on \([0,q]^2\), decreasing a positive threshold strictly increases the left side of (8).

# 3. A small core and a concentrated extension

Fix \(0<\gamma\le1\). Let \(d_i(v)\) be the degree of \(v\) in \(H_i\), and put
\[
S=\{v:d_1(v)>\gamma m_1\text{ or }d_2(v)>\gamma m_2\},
\qquad W=V\setminus S.
\]
Then
\[
|S|\le \frac{2r}{\gamma},
\qquad d_i(v)\le\gamma m_i\quad(v\in W).
\tag{11}
\]

Delete the edges contained entirely in \(S\). Write
\[
D_i=|\{e\in E(H_i):e\subseteq S\}|,\qquad m_i'=m_i-D_i.
\]
Simplicity gives
\[
D_i\le \binom{\lceil2r/\gamma\rceil}{r}.
\tag{12}
\]

Fix a coloring of \(S\), and color \(W\) independently and uniformly from \([r]\). Let \(X_i'\) count rainbow edges among the undeleted edges.

Two edge indicators are independent whenever their sets of vertices in \(W\) are disjoint. Thus
\[
\begin{aligned}
\operatorname{Var}(X_i'\mid \phi|_S)
&\le \sum_{v\in W}d_i(v)^2\\
&\le \gamma m_i\sum_{v\in W}d_i(v)\\
&\le r\gamma m_i^2.
\end{aligned}
\tag{13}
\]
Here the diagonal terms are included, since every undeleted edge meets \(W\).

By Chebyshev’s inequality and a union bound, some extension of the fixed coloring of \(S\) satisfies
\[
X_i'\ge
\mathbb E(X_i'\mid\phi|_S)-2\sqrt{r\gamma}\,m_i
\qquad(i=1,2).
\tag{14}
\]

The remaining task is therefore to choose colors on \(S\) that give good simultaneous conditional expectations.

# 4. Proof of Theorem 1

For a coloring \(\phi:S\to[r]\), define
\[
F_i(\phi)=\mathbb E(X_i'\mid\phi).
\]

For an undeleted edge \(e\), put \(t=|e\cap S|\le r-1\). Its contribution to \(F_i\) is
\[
\lambda_tJ_{e\cap S}(\phi),
\qquad
\lambda_t=\frac{(r-t)!}{r^{r-t}}.
\tag{15}
\]
Since \(r-t\ge1\),
\[
\lambda_t\le\frac1r.
\]
Consequently,
\[
0\le F_i\le\frac{m_i'}r.
\tag{16}
\]

Now color \(S\) uniformly at random. The resulting coloring of all vertices is uniform, so
\[
\mathbb EF_i=p_rm_i'.
\tag{17}
\]
Moreover, (5) and the nonnegative coefficients in (15) give
\[
\operatorname{Cov}(F_1,F_2)\ge0.
\tag{18}
\]

Suppose first that \(m_1',m_2'>0\). Apply (7) to
\[
A=\frac{rF_1}{m_1'},\qquad B=\frac{rF_2}{m_2'},
\]
whose common mean is \(q=rp_r\). There is a coloring of \(S\) with
\[
F_i\ge \frac{p_r}{2-rp_r}\,m_i'
\qquad(i=1,2).
\tag{19}
\]
If an \(m_i'\) is zero, its objective can be omitted; the other conditional expectation can be made at least its mean, which is enough for (19).

Combining (14), (19), and (12), with
\[
c_r=\frac{p_r}{2-rp_r},
\]
gives
\[
X_i\ge
c_rm_i-c_r\binom{\lceil2r/\gamma\rceil}{r}
-2\sqrt{r\gamma}\,m_i.
\tag{20}
\]

Choose
\[
\gamma=M^{-2/(2r+1)}.
\]
Then
\[
\frac{\gamma^{-r}}{M}=\sqrt{\gamma}=M^{-1/(2r+1)}.
\]
Equation (20) proves Theorem 1. \(\square\)

The improvement over applying (7) directly to \(X_i/m_i\) comes from (16): after removing the small core’s internal edges, every conditional edge contribution is at most \(1/r\), rather than at most \(1\).

# 5. Proof of Theorem 2

Here \(r=3\) and \(p=2/9\). Use the core \(S\) from Section 3. Assume first that both \(m_i'>0\); zero objectives are handled as above.

Let \(m_{i,j}\) count the edges meeting \(S\) in exactly \(j\) vertices. Thus
\[
m_i'=m_{i,0}+m_{i,1}+m_{i,2}.
\]
Put
\[
\beta_i=\frac{m_{i,2}}{m_i'}.
\tag{21}
\]

Form a weighted graph \(G_i\) on \(S\), assigning to \(xy\) the number of edges \(e\in H_i\) with \(e\cap S=\{x,y\}\). Its total weight is \(m_{i,2}\).

We compare two coloring procedures.

## 5.1. Procedure U: three colors on the core, uniform colors outside

Suppose a 3-coloring of \(S\) cuts a fraction \(A_i\) of the weight of \(G_i\). Then
\[
\frac{F_i}{m_i'}
=p(1-\beta_i)+\frac{\beta_i}{3}A_i.
\tag{22}
\]

Set
\[
\tau=\frac{15-\sqrt{41}}{46},\qquad d=p-\tau.
\]
To make (22) at least \(\tau\), it suffices that
\[
A_i\ge \frac23-\frac{3d}{\beta_i}.
\tag{23}
\]
A nonpositive threshold can simply be omitted.

Under a uniform 3-coloring, the cut fractions \(A_1,A_2\) have common mean \(2/3\) and nonnegative covariance. Applying (8) and substituting the thresholds (23), we find that Procedure U succeeds whenever
\[
2\beta_1\beta_2
\le 9d(\beta_1+\beta_2)+324d^2.
\tag{U}
\]

This includes the cases where a threshold is nonpositive: that objective is automatic, and the other can attain its mean.

## 5.2. Procedure B: two colors on the core, one color outside

Color \(S\) with colors 1 and 2, and give every vertex in \(W\) color 3.

An edge is rainbow precisely when it meets \(S\) twice and its two core vertices have different colors. Thus, if \(B_i\) is the fraction of \(G_i\)’s weight cut by the bipartition,
\[
\frac{X_i'}{m_i'}=\beta_iB_i.
\tag{24}
\]

Under a uniform bipartition, \(B_1,B_2\) have common mean \(1/2\) and nonnegative covariance. Provided \(\beta_i\ge2\tau\), the thresholds \(\tau/\beta_i\) lie in \([0,1/2]\). Applying (8), Procedure B succeeds if
\[
\beta_1\beta_2
\ge 2\tau(\beta_1+\beta_2)-3\tau^2.
\tag{B}
\]

## 5.3. One of the two procedures always succeeds

This is the reason for the choice of \(\tau\).

Write
\[
u=\frac{9d}{2},\qquad v=162d^2,\qquad z=13\tau-2.
\]
The equation
\[
23\tau^2-15\tau+2=0
\]
gives the identities
\[
u(1+z)+v=z,
\qquad
2\tau(1+z)-3\tau^2=z,
\tag{25}
\]
and the inequalities
\[
0<u<2\tau<z<1.
\tag{26}
\]

Put
\[
\sigma=\beta_1+\beta_2,\qquad \Pi=\beta_1\beta_2.
\]
Condition (U) is exactly
\[
\Pi\le u\sigma+v.
\tag{27}
\]

Suppose (27) fails. Let \(x=\min(\beta_1,\beta_2)\) and \(y=\max(\beta_1,\beta_2)\le1\). Then
\[
xy>u(x+y)+v,
\]
so
\[
(x-u)y>ux+v.
\]
It follows that
\[
x>\frac{u+v}{1-u}=z>2\tau.
\tag{28}
\]
Thus the thresholds needed for Procedure B are valid.

It remains to verify (B).

* If \(\sigma\le1+z\), equations (25) and \(u<2\tau\) give
  \[
  u\sigma+v\ge2\tau\sigma-3\tau^2.
  \]
  Since (27) fails, (B) holds.

* If \(\sigma\ge1+z\), then
  \[
  \Pi\ge\sigma-1
  \]
  because \((1-\beta_1)(1-\beta_2)\ge0\). Using (25) again,
  \[
  \sigma-1\ge2\tau\sigma-3\tau^2.
  \]
  Hence (B) holds in this case as well.

Therefore, either Procedure U or Procedure B gives at least \(\tau m_i'\) for both objectives—conditionally in Procedure U, and deterministically in Procedure B.

In Procedure U apply (14); in Procedure B no concentration estimate is needed. In either case,
\[
X_i\ge
\tau(m_i-D_i)-2\sqrt{3\gamma}\,m_i.
\tag{29}
\]
Taking \(\gamma=M^{-2/7}\) and using \(D_i=O(\gamma^{-3})\) proves (2). \(\square\)

# 6. Proof of Theorem 3

This uses a different random coloring: colors are independent between blocks, but injective within each block.

For every \(B\in\mathcal B\), choose a uniformly random injection \(B\to[r]\), independently for different blocks.

## 6.1. Every edge still has probability at least \(p_r\)

For an edge \(e\), let \(t_B=|e\cap B|\). Then
\[
\mathbb P(e\text{ is rainbow})
=\frac{r!}{\prod_{B\in\mathcal B}(r)_{t_B}}
\ge\frac{r!}{r^r}=p_r.
\tag{30}
\]
Indeed, the marginal coloring on \(e\cap B\) is a uniform injection, and
\[
(r)_{t_B}\le r^{t_B},\qquad \sum_Bt_B=r.
\]
Thus
\[
\mathbb EX_i\ge p_rm_i.
\tag{31}
\]

## 6.2. One common block creates no covariance

For an edge \(e\), let
\[
\mathcal B(e)=\{B\in\mathcal B:e\cap B\ne\varnothing\}.
\]

If \(\mathcal B(e)\) and \(\mathcal B(f)\) are disjoint, their indicators are independent.

Suppose they share exactly one block \(B\). Conditional on the coloring of \(B\), the two edge indicators depend on disjoint collections of other blocks, so they are conditionally independent. Moreover, the conditional rainbow probability of either edge does not depend on the particular injection chosen on \(B\): any two such injections are related by a permutation of the colors, and all other blocks have color-permutation-invariant distributions. Their covariance is therefore zero.

This also covers an edge lying entirely in one block: its rainbow indicator is constantly one.

Consequently, only edge pairs meeting at least two common blocks can contribute nonzero covariance.

Since the covariance of two Bernoulli variables is at most \(1/4\),
\[
\begin{aligned}
\operatorname{Var}X_H
&\le \frac14
|\{(e,f):|\mathcal B(e)\cap\mathcal B(f)|\ge2\}|\\
&\le \frac14
\sum_{e\in E(H)}
\sum_{\{B,C\}\subseteq\mathcal B(e)}
|\{f:f\cap B\ne\varnothing,\ f\cap C\ne\varnothing\}|\\
&\le \frac14\binom r2\,mD_{\mathcal B}(H).
\end{aligned}
\tag{32}
\]

## 6.3. Concentration of one objective suffices

We use the following bounded-variable observation, which also verifies the corresponding step in the supplied attempt.

Suppose \(Y_1,Y_2\in[0,1]\), both means are at least \(p\), and
\[
\operatorname{Var}Y_1=v.
\]
For every \(a>0\), some outcome satisfies
\[
Y_1\ge p-a,\qquad
Y_2\ge p-(1-p)\frac{v}{a^2}.
\tag{33}
\]

For proof, put \(G=\{Y_1\ge p-a\}\), and let \(h=\mathbb P(G^c)\). The one-sided Chebyshev inequality gives
\[
h\le\frac{v}{v+a^2}.
\]
Since \(Y_2\le1\),
\[
\begin{aligned}
\mathbb E(Y_2\mid G)
&\ge\frac{p-h}{1-h}\\
&=p-(1-p)\frac{h}{1-h}\\
&\ge p-(1-p)\frac{v}{a^2}.
\end{aligned}
\]
Choose an outcome in \(G\) attaining at least this conditional mean. The case \(v=0\) is immediate.

Apply (33) to \(Y_i=X_i/m_i\). From (32),
\[
v\le\frac14\binom r2\,\delta.
\]
Taking
\[
a=\left[\frac{1-p_r}{4}\binom r2\,\delta\right]^{1/3}
\]
proves (4), including \(\delta=0\) by the zero-variance case. \(\square\)

## 6.4. A pair-codegree formulation

For vertices in distinct blocks,
\[
D_{\mathcal B}(H)
\le
r^2\max_{\substack{u,v\\u,v\text{ in distinct blocks}}}d_H(u,v).
\tag{34}
\]

Thus it suffices that all linear pair-codegrees of one hypergraph be confined within disjoint blocks of size at most \(r\).

More explicitly, suppose there is a sequence \(\varepsilon\to0\) such that the graph
\[
uv\in E(G_\varepsilon)
\quad\Longleftrightarrow\quad
d_{H_1}(u,v)>\varepsilon m_1
\]
has every connected component of order at most \(r\). Use those components as blocks. Equation (34) gives
\[
D_{\mathcal B}(H_1)\le r^2\varepsilon m_1,
\]
and Theorem 3 reaches the conjectured asymptotic bound.

For the sunflower example, take its core as one block and each disjoint petal as another block. Then
\[
D_{\mathcal B}(H_1)=1,
\]
although every pair in the core has codegree \(m_1\).

# 7. What remains open in this attack

The unrestricted target is still
\[
X_i\ge p_rm_i-o(m_i).
\]

Theorem 1 gives a smaller constant when \(r\ge3\). Theorem 2 improves that constant for triples, but leaves the fixed gap
\[
\frac29-\tau=0.0353336187\ldots.
\]
Theorem 3 reaches the target only when one hypergraph’s large codegrees have the specified block structure.

The obstruction in these arguments is precise: after isolating a small high-degree core, the conditional expectations have the correct means and nonnegative covariance, but the moment lemmas do not generally give simultaneous attainment of both means. The two-palette argument for triples improves the guaranteed threshold without eliminating that loss.

None of this supplies a counterexample to the conjecture. The proofs above are self-contained, but I have not verified whether these partial bounds or the clustered-codegree formulation already occur in the literature.