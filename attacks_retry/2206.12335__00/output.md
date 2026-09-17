```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for all cut-valued 1-independent laws and all independent equality-colour models, and the unrestricted minimum has the signs model's quadratic expansion at p=1.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains open; the partial results below do not justify restricting to either special class, and their literature novelty has not been checked."
}
```

# 1. Results and benchmark

Let
\[
f(p)=\inf_{\mu\in\mathcal D_{\ge p}(Q_3)}
 \mathbb P_\mu(Q_3\text{ is connected}).
\]
For \(1/2<p\le1\), write
\[
t=2p-1,\qquad r=1-p,\qquad
\theta=\frac{1+\sqrt t}{2}.
\]
The signs model has connectivity probability
\[
\begin{aligned}
S(p)
&=\theta^8+(1-\theta)^8\\
&=\frac{1+28t+70t^2+28t^3+t^4}{128}\\
&=1-4r+5r^2-2r^3+\frac{r^4}{8}.
\end{aligned}
\]
Indeed, its open graph is connected exactly when all eight vertex signs agree.

I obtain three partial results.

1. **Arbitrary 1-independent laws, asymptotically:**
   \[
   \boxed{f(p)=1-4(1-p)+5(1-p)^2+O((1-p)^3)\qquad(p\uparrow1).}
   \]
   Thus the signs model is optimal through the quadratic term, improving the linear-order estimate in the supplied attempt.

2. **All cut-valued 1-independent laws:** suppose that almost surely the closed-edge set is a cut \(\delta(U)\), where \(U\) may have an arbitrary distribution. Then the conjectured inequality holds whenever
   \[
   p>p_*:=\frac{1+\tan^2(\pi/16)}2
   \approx0.519783065.
   \]
   No independence assumption on the vertex memberships of \(U\) is needed.

3. **All independent equality-colour models:** vertex colours may have arbitrary, vertex-dependent distributions on a common finite or countable colour space. If an edge is open exactly when its endpoint colours agree, then the conjectured inequality holds for every \(p>1/2\).

The benchmark and thinning reduction from the previous attempt are correct; the arguments below are otherwise self-contained.

## Exact marginals for the unrestricted problem

For unrestricted lower bounds, it suffices to assume that every edge has marginal exactly \(p\). If edge \(e\) has marginal \(q_e\ge p\), retain it, independently, with probability \(p/q_e\). This preserves 1-independence and cannot increase connectivity.

I do **not** use this reduction inside either special class below: thinning need not preserve those classes.

---

# 2. Arbitrary independent equality-colour models

## Theorem 2.1

Let the vertices of \(Q_3\) receive independent colours, with possibly different distributions at different vertices. Open an edge exactly when its endpoint colours agree. If every edge has open probability at least \(p>1/2\), then
\[
\mathbb P(Q_3\text{ is connected})\ge S(p).
\]
For \(1/2<p<1\), equality forces the ordinary signs model, up to renaming colours and adding zero-probability colours.

### Proof

We first identify a common dominant colour.

If probability vectors \(x,y\) satisfy
\[
\sum_i x_i y_i>\frac12,
\]
then they have the same colour with mass greater than \(1/2\). To see this, let \(m=x_c=\max_i x_i\). Necessarily \(m>1/2\). If \(y_c\le1/2\), then
\[
\sum_i x_i y_i
\le my_c+(1-m)(1-y_c)
\le\frac12,
\]
a contradiction.

Applying this along the edges of the connected cube, there is one colour, denoted \(0\), whose probability at every vertex exceeds \(1/2\).

Write
\[
a_v=\mathbb P(\text{colour at }v=0),\qquad
b_v=1-a_v,\qquad c_v=2a_v-1>0.
\]
For an edge \(uv\), define
\[
d_{uv}
=b_ub_v-\sum_{i\ne0}
 \mathbb P(\text{colour at }u=i)\mathbb P(\text{colour at }v=i).
\]
Thus \(d_{uv}\ge0\) is the probability that both endpoint colours are nonzero but different. The edge-marginal assumption gives
\[
\frac{1+c_uc_v}{2}-d_{uv}\ge p,
\]
and consequently
\[
c_uc_v\ge t+2d_{uv}. \tag{2.1}
\]

Coarsen all nonzero colours into one colour. The connectivity probability of this binary model is
\[
B=\prod_v a_v+\prod_v b_v
  =\frac1{128}\sum_{\substack{0\le k\le8\\k\text{ even}}}e_k(c),
\]
where \(e_k\) is the \(k\)-th elementary symmetric polynomial.

Multiplication of (2.1) over a perfect matching gives
\[
\prod_v c_v\ge t^4.
\]
AM–GM over the \(k\)-element subsets therefore yields
\[
e_k(c)\ge\binom8k t^{k/2}. \tag{2.2}
\]

We need a refinement for \(e_2\). The complement of \(Q_3\) is 4-regular and has 16 edges. Hence
\[
\prod_{\{u,v\}\notin E(Q_3)}c_uc_v
=\left(\prod_v c_v\right)^4\ge t^{16}.
\]
Another application of AM–GM gives
\[
\sum_{\{u,v\}\notin E(Q_3)}c_uc_v\ge16t.
\]
Together with (2.1),
\[
e_2(c)\ge28t+2\sum_{uv\in E(Q_3)}d_{uv}.
\]
Using this and (2.2),
\[
B\ge S(p)+\frac1{64}\sum_{uv\in E(Q_3)}d_{uv}. \tag{2.3}
\]

The original colour model is connected exactly when all eight colours agree. Its connectivity probability is \(B-L\), where
\[
L=\mathbb P(\text{all colours are nonzero, but not all agree}).
\]
Since the cube is connected, on this event some edge has different endpoint colours. Independence of the vertex colours and a union bound give
\[
\begin{aligned}
L
&\le\sum_{uv\in E(Q_3)}
 d_{uv}\prod_{w\notin\{u,v\}}b_w\\
&\le\frac1{64}\sum_{uv\in E(Q_3)}d_{uv},
\end{aligned}
\]
because \(b_w<1/2\). Combining with (2.3) proves the inequality.

If some \(d_{uv}>0\), the last bound is strict. Thus equality requires all \(d_{uv}=0\), and equality in the symmetric-polynomial bounds forces \(c_v=\sqrt t\) for every vertex. The nonzero-colour distributions at the endpoints of each edge must then be concentrated on the same single colour. Connectivity of \(Q_3\) makes that colour common to every vertex. This is precisely the signs model. ∎

This theorem simultaneously removes the identical-distribution restriction from the multicolour result and the binary-colour restriction from the vertex-dependent result in the previous attempt.

---

# 3. All cut-valued 1-independent laws

Call a law **cut-valued** if its closed-edge set is almost surely
\[
\delta(U)=\{uv:|\{u,v\}\cap U|=1\}
\]
for some random vertex set \(U\). Equivalently, its edge signs
\[
Y_e=\begin{cases}
+1,&e\text{ open},\\
-1,&e\text{ closed}
\end{cases}
\]
can be written
\[
Y_{uv}=\sigma_u\sigma_v
\]
for vertex spins \(\sigma_v\in\{-1,+1\}\).

The spins need not be independent. By applying an independent global sign flip, we may and do make their law invariant under \(\sigma\mapsto-\sigma\).

## Theorem 3.1

Every cut-valued 1-independent law on \(Q_3\) with edge marginals at least
\[
p>p_*=\frac{1+\tan^2(\pi/16)}2
\]
satisfies
\[
\mathbb P(Q_3\text{ is connected})\ge S(p).
\]
For \(p<1\), equality forces the signs edge law.

The main ingredient is a classification of the even spin moments.

## 3.1. A product representation for the even moments

Identify
\[
Q_3=K_{4,4}-M,
\]
with bipartition
\[
A_1,\ldots,A_4,\qquad B_1,\ldots,B_4,
\]
where \(A_iB_j\) is an edge exactly when \(i\ne j\).

Set
\[
t_{ij}=\mathbb E(\sigma_{A_i}\sigma_{B_j})>0
\qquad(i\ne j).
\]

For every square, its two opposite-edge pairs are vertex-disjoint. Therefore the four-spin moment can be computed using either pair, giving
\[
t_{ik}t_{jl}=t_{il}t_{jk}
\]
whenever \(i,j,k,l\) are distinct. These identities imply the existence of positive numbers \(\alpha_i,\beta_j\) such that
\[
t_{ij}=\alpha_i\beta_j\qquad(i\ne j). \tag{3.1}
\]

For completeness, one can take
\[
\begin{gathered}
\alpha_1=1,\quad
\beta_2=t_{12},\quad\beta_3=t_{13},\quad\beta_4=t_{14},\\
\alpha_2=t_{23}/t_{13},\quad
\alpha_3=t_{32}/t_{12},\quad
\alpha_4=t_{42}/t_{12},\quad
\beta_1=t_{21}/\alpha_2.
\end{gathered}
\]
The square identities verify the remaining entries.

We repeatedly use the following consequence of 1-independence: if paths \(P_1,\ldots,P_k\) have disjoint vertex sets, then their edge-sign products are independent. Since a path-sign product telescopes to the product of its endpoint spins, this factors the corresponding spin moment.

For a triple \(i,j,k\), let \(l\) be the remaining index. An edge from \(B_l\) to one member of the triple can be chosen vertex-disjoint from a length-two path joining the other two. Thus
\[
t_{kl}\mathbb E(\sigma_{A_i}\sigma_{A_j})
=t_{jl}\mathbb E(\sigma_{A_i}\sigma_{A_k})
=t_{il}\mathbb E(\sigma_{A_j}\sigma_{A_k}).
\]
Using (3.1), for some real \(\lambda\),
\[
\mathbb E(\sigma_{A_i}\sigma_{A_j})
=\lambda\alpha_i\alpha_j\qquad(i\ne j).
\]
Similarly, for some real \(\mu\),
\[
\mathbb E(\sigma_{B_i}\sigma_{B_j})
=\mu\beta_i\beta_j.
\]

The four-spin moment on
\[
\{A_1,A_2,B_1,B_3\}
\]
can be computed from the matching \(A_1B_3,A_2B_1\), or from the disjoint paths
\[
A_1B_4A_2,\qquad B_1A_4B_3.
\]
Consequently,
\[
\lambda\mu=1. \tag{3.2}
\]
In particular, neither parameter is zero.

The same four-spin set, using the disjoint path \(A_1B_2A_3B_1\) and edge \(A_2B_3\), gives
\[
\mathbb E(\sigma_{A_1}\sigma_{B_1})=\alpha_1\beta_1.
\]
Permuting indices proves this for every missing edge.

It follows that there are numbers \(z_v\) satisfying
\[
\mathbb E(\sigma_u\sigma_v)=z_uz_v
\qquad(u\ne v),
\]
of one of two forms:

- **Real branch:** if \(\lambda>0\),
  \[
  z_{A_i}=\sqrt\lambda\,\alpha_i>0,\qquad
  z_{B_j}=\beta_j/\sqrt\lambda>0.
  \]

- **Imaginary branch:** if \(\lambda<0\),
  \[
  z_{A_i}=i\sqrt{-\lambda}\,\alpha_i,\qquad
  z_{B_j}=-i\beta_j/\sqrt{-\lambda}.
  \]

Moreover,
\[
\boxed{\quad
\mathbb E\prod_{v\in T}\sigma_v=\prod_{v\in T}z_v
\quad\text{for every even }T\subseteq V(Q_3).
\quad} \tag{3.3}
\]
To prove this last assertion, use a Hamiltonian cycle of the cube. Pair consecutive members of \(T\) around that cycle, taking alternate intervening arcs. These are vertex-disjoint paths with endpoint set \(T\), so the disjoint-path factorization applies.

By Fourier inversion on \(\{-1,+1\}^8\), (3.3) determines the symmetrized spin law:
\[
\mathbb P(\sigma=s)
=\frac1{512}
\left[
\prod_v(1+z_vs_v)+\prod_v(1-z_vs_v)
\right]. \tag{3.4}
\]
This is a formal product representation. In the real branch, it is not necessary to assume \(z_v\le1\).

## 3.2. The real branch satisfies the conjectured bound

For each edge \(uv\),
\[
z_uz_v=\mathbb E Y_{uv}\ge t.
\]
Multiplication over a perfect matching yields
\[
\prod_v z_v\ge t^4.
\]
All \(z_v\) are positive in the real branch, so AM–GM gives
\[
e_k(z)\ge\binom8k t^{k/2}.
\]

A cut-valued graph is connected exactly when all spins agree. Hence, by (3.4),
\[
\begin{aligned}
\mathbb P(Q_3\text{ connected})
&=\frac1{256}
 \left[\prod_v(1+z_v)+\prod_v(1-z_v)\right]\\
&=\frac1{128}\sum_{k\text{ even}}e_k(z)\\
&\ge S(p).
\end{aligned}
\]
Equality forces \(z_v=\sqrt t\) for all \(v\). Equation (3.3) then determines exactly the signs edge law.

## 3.3. The imaginary branch cannot reach \(p>p_*\)

Write \(z_v=i\varepsilon_v a_v\), where \(a_v>0\), with \(\varepsilon_v=1\) on the \(A\)-part and \(-1\) on the \(B\)-part. Put
\[
\gamma_v=\arctan a_v\in(0,\pi/2),\qquad
T=\sum_v\gamma_v.
\]
Formula (3.4) becomes
\[
\mathbb P(\sigma=s)
=\frac1{256}\prod_v\sqrt{1+a_v^2}\,
 \cos\!\left(\sum_v\varepsilon_vs_v\gamma_v\right).
\]
Thus every signed sum of the angles must have nonnegative cosine.

This forces
\[
T\le\frac\pi2. \tag{3.5}
\]
Indeed, if \(T>\pi/2\), nonnegativity of \(\cos T\) first implies \(T\ge3\pi/2\). Starting with all minus signs and flipping signs one at a time produces an increasing sequence from \(-T\) to \(T\), with each increment strictly less than \(\pi\). Such a sequence cannot cross the interval \((\pi/2,3\pi/2)\) without entering it. At that signed sum the cosine would be negative.

For an edge \(uv\),
\[
a_ua_v=z_uz_v\ge t.
\]
Since (3.5) implies \(\gamma_u+\gamma_v<\pi/2\), the tangent addition formula and AM–GM give
\[
\gamma_u+\gamma_v\ge2\arctan\sqrt t.
\]
Summing over a perfect matching,
\[
T\ge8\arctan\sqrt t.
\]
Together with (3.5), this implies
\[
t\le\tan^2(\pi/16),
\]
or \(p\le p_*\). Therefore only the real branch is possible when \(p>p_*\), completing the proof of Theorem 3.1. ∎

## 3.4. The cut-valued threshold is sharp

There is an explicit imaginary-branch construction below this threshold. This is **not** a counterexample in the conjectured range \(p>0.55\).

Let
\[
0<t\le\tan^2(\pi/16),\qquad
p=\frac{1+t}{2},\qquad \phi=\arctan\sqrt t.
\]
Give the spins the distribution
\[
\mathbb P(\sigma=s)
=\frac{(1+t)^4}{256}
 \cos\!\left(
 \phi\left(\sum_{v\in A}s_v-\sum_{v\in B}s_v\right)
 \right). \tag{3.6}
\]
Every cosine is nonnegative because \(8\phi\le\pi/2\). The probabilities sum to one since
\[
(1+t)^4(\cos\phi)^8=1.
\]

This is (3.4) with
\[
z_v=i\sqrt t\quad(v\in A),\qquad
z_v=-i\sqrt t\quad(v\in B).
\]
Its even moments factor as in (3.3). This implies 1-independence of the cut-edge law: a product of edge signs is a product of the spins at its odd-degree vertices, and vertex-disjoint edge sets give disjoint such vertex sets. Factorization of all these sign moments implies independence of the edge-state vectors.

Every edge has marginal \(p\), while
\[
\mathbb P(Q_3\text{ connected})
=\frac{(1+t)^4}{128}=\frac{p^4}{8}.
\]
For \(t>0\),
\[
S(p)-\frac{p^4}{8}
=\frac{3t+8t^2+3t^3}{16}>0.
\]
Thus signs optimality fails within the cut-valued class at \(p=p_*\), although it holds throughout that class for every \(p>p_*\).

---

# 4. A universal quadratic-order bound

This section applies to **every** 1-independent law, with no cut or vertex-colour assumption.

## Theorem 4.1

For \(0<r<1/2\),
\[
1-4r+5r^2-3280r^3
\le f(1-r)
\le1-4r+5r^2-2r^3+\frac{r^4}{8}.
\]
In particular,
\[
f(p)=S(p)+O((1-p)^3)\qquad(p\uparrow1).
\]

The constant \(3280\) is deliberately unoptimized.

### Proof

By thinning, assume every edge is closed with probability exactly \(r\). Let \(K\) be the random closed-edge set, and let
\[
D(K)=\mathbf1\{Q_3-K\text{ is disconnected}\}.
\]
Define the nonnegative deficit
\[
d(K)=|K|-3D(K),\qquad \Delta=\mathbb E d(K).
\]
Then
\[
\Delta=3\left(\mathbb P(Q_3-K\text{ connected})-1+4r\right). \tag{4.1}
\]

The only configurations with \(d(K)=0\) are \(K=\varnothing\) and the eight vertex stars \(K=\delta(v)\). To check this, every cut has at least three edges, and the only three-edge cuts of the cube isolate one vertex. The latter follows from
\[
|\delta(U)|=3|U|-2e(U)
\]
by considering \(1\le |U|\le4\): the respective lower bounds are \(3,4,5,4\).

Put
\[
q_v=\mathbb P(K=\delta(v)).
\]
Call every other configuration bad. For an edge \(uv\),
\[
r=q_u+q_v+b_{uv},\qquad b_{uv}\ge0,
\]
where \(b_{uv}\) is the probability that \(uv\) is closed in a bad configuration. Let
\[
B=\sum_{uv\in E(Q_3)}b_{uv}.
\]
For every bad configuration, \(|K|\le4d(K)\): if it is connected, \(d(K)=|K|\), and if disconnected, \(|K|\ge4\). Therefore
\[
B\le4\Delta. \tag{4.2}
\]

### 4.1. Independent witnesses involving two centres

Define a nonnegative statistic \(W(K)\) as follows.

- **Adjacent centres \(u,v\):** add \(1\) if all four edges of \(\delta(\{u,v\})\) are closed. These four edges form two vertex-disjoint wedges, centred at \(u\) and \(v\).

- **Centres \(u,v\) at distance two:** let \(x,y\) be their common neighbours, and \(z,w\) their respective remaining neighbours. Add \(3/2\) for each of the two events
  \[
  \{ux,uz,vy,vw\}\subseteq K,\qquad
  \{uy,uz,vx,vw\}\subseteq K.
  \]
  Again, each event consists of two vertex-disjoint wedges.

- **Antipodal centres \(u,v\):** add \(3\) if both full stars are closed. Their vertex supports are disjoint.

Every local wedge or star event centred at \(v\) has probability at least \(q_v\). By 1-independence,
\[
\mathbb E W(K)\ge T(q),
\]
where
\[
T(q)=
\sum_{uv\in E(Q_3)}q_uq_v
+3\sum_{\{u,v\}\notin E(Q_3)}q_uq_v. \tag{4.3}
\]
There are 12 adjacent pairs, 12 distance-two pairs, and 4 antipodal pairs. Hence
\[
0\le W(K)\le12+36+12=60. \tag{4.4}
\]

### 4.2. A pointwise estimate when the closed graph has matching number at most two

I claim that
\[
d(K)\ge W(K)\qquad\text{if }\nu(K)\le2. \tag{4.5}
\]

Every witness in \(W\) contains two vertex-disjoint wedges. Suppose their centres are \(u,v\). If a closed edge is incident to neither centre, one can choose one edge from each wedge avoiding that edge, producing a three-edge matching. Here bipartiteness ensures that the extra edge cannot meet both leaves of one wedge. Thus, when \(\nu(K)\le2\), all closed edges are incident to \(u\) or \(v\).

Furthermore, this pair of centres is unique: a size-two vertex cover of two disjoint wedges must consist of their centres. Consequently, witnesses belonging to different centre pairs cannot coexist when \(\nu(K)\le2\).

It remains to check one pair.

- For adjacent centres, the witness has four closed edges, possibly with the centre edge also closed. Thus \(d(K)\ge1=W(K)\).
- For distance-two centres, four closed witness edges leave the open graph connected, so \(d(K)=4\). With five closed edges, one centre is isolated and \(d(K)=2\). With six, both witnesses occur and \(d(K)=3=W(K)\). In the four-edge case, connectivity follows because deleting the two centres leaves a connected graph and each centre retains an open edge.
- For antipodal centres, the witness consists of six closed edges, so \(d(K)=3=W(K)\).

This proves (4.5).

The cube has 44 three-edge matchings. One way to count them is to choose an edge and then a two-edge matching after deleting its endpoints: the remaining graph has seven edges and degrees \(3,3,2,2,2,2\), hence
\[
\binom72-\left(2\binom32+4\binom22\right)=11
\]
two-edge matchings. The answer is \(12\cdot11/3=44\).

Edges in a matching are mutually independent, so
\[
\mathbb P(\nu(K)\ge3)\le44r^3.
\]
Using (4.4), (4.5), and (4.3),
\[
\Delta\ge T(q)-2640r^3. \tag{4.6}
\]

### 4.3. The quadratic minimum of \(T(q)\)

Choose a vertex \(A_1\) in one bipartition class and write \(q_{A_1}=ar\), where \(0\le a\le1\). Define
\[
q_v^0=
\begin{cases}
ar,&v\in A,\\
(1-a)r,&v\in B.
\end{cases}
\]
Telescoping the relations
\[
q_u+q_v=r-b_{uv}
\]
along paths from \(A_1\) gives
\[
|q_v-q_v^0|\le B
\qquad\text{for every }v.
\]
Since \(q_v,q_v^0\le r\),
\[
|q_uq_v-q_u^0q_v^0|\le2rB.
\]
The sum of the weights in \(T\) is 60. Thus, by (4.2),
\[
T(q)\ge T(q^0)-120rB
      \ge T(q^0)-480r\Delta. \tag{4.7}
\]

A direct count gives
\[
\begin{aligned}
T(q^0)
&=\left(18-12a(1-a)\right)r^2\\
&=\left(15+12(a-\tfrac12)^2\right)r^2\\
&\ge15r^2.
\end{aligned}
\]
Combining (4.6) and (4.7),
\[
(1+480r)\Delta\ge15r^2-2640r^3.
\]
Using (4.1),
\[
\begin{aligned}
\mathbb P(Q_3-K\text{ connected})
&\ge1-4r+\frac{5r^2-880r^3}{1+480r}\\
&=1-4r+5r^2-\frac{3280r^3}{1+480r}\\
&\ge1-4r+5r^2-3280r^3.
\end{aligned}
\]
The signs model supplies the stated upper bound. ∎

---

# 5. What remains unresolved

The cut-valued theorem covers arbitrary dependence in the underlying vertex signs, not merely independent signs. The colour theorem covers arbitrary independent, non-identically distributed colour labels. The unrestricted estimate shows that no 1-independent law can improve on the signs model at quadratic order near \(p=1\).

However, none of these arguments permits restricting the original optimization to either special class. A general 1-independent law can assign positive probability to closed-edge configurations that are not cuts; even independent thinning of a signs model does this. The cut-law moment classification then no longer applies.

Accordingly, I have not proved
\[
f(p)\ge S(p)\qquad(0.55<p<1),
\]
nor produced a counterexample in that interval. In particular, the asymptotic result does **not** establish exact optimality on any nontrivial interval below \(p=1\).