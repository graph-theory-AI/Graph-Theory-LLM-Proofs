```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain the desired approximation for arbitrary monotone FO objectives on subpolynomial-degree graphs, and for weighted fixed-distance packing on every nowhere-dense class.",
  "would_publish": false,
  "caveats": "The unrestricted nowhere-dense metatheorem remains unproved; no novelty claim is made for the special cases."
}
```

# 1. Formulation and results

Let \(\varphi(X)\) be a fixed first-order sentence in the graph language with an additional unary predicate \(X\). A set \(S\subseteq V(G)\) is feasible when
\[
(G,S)\models\varphi(X).
\]
Assume feasibility is downward closed:
\[
S\text{ feasible},\quad S'\subseteq S
\quad\Longrightarrow\quad S'\text{ feasible}.
\]
We maximize \(w(S)\), where the vertex weights are nonnegative rationals. This includes the unweighted problem.

I prove two quantitative partial results.

**Theorem A.** For every fixed \(\varphi\), there is a constant \(R=R(\varphi)\) such that monotone \(\varphi\)-maximization has a polynomial-time approximation with factor
\[
d(G^R)+1\le (\Delta(G)+1)^R.
\tag{1}
\]
Here \(G^R\) joins distinct vertices at distance at most \(R\), and \(d\) denotes degeneracy.

Consequently, the desired \(n^{o(1)}\) approximation holds for arbitrary monotone FO objectives on any class satisfying
\[
\Delta(G)+1=n^{o(1)}.
\]
A version allowing a fixed number of arbitrary-degree exceptional vertices also follows.

**Theorem B.** For every fixed \(r\ge 1\), maximum-weight distance-\(r\) independence has a polynomial-time approximation with factor
\[
4\bigl(1+r(\operatorname{wcol}_r(G)-1)\bigr)^r.
\tag{2}
\]
A distance-\(r\) independent set has pairwise distances greater than \(r\). Thus this factor is \(n^{o(1)}\) on every nowhere-dense class.

In particular, the ambient distance-two constraint highlighted in the previous attempt is covered by Theorem B. Its failure under ordinary proper coloring is an obstruction to that proof method, not an unresolved special case here.

The proofs use two established background facts: Gaifman normal form and the weak-coloring-number characterization of nowhere density. No extension of bounded-expansion quantifier elimination is assumed.

# 2. Exact FO optimization on separated candidate sets

The main logical observation is stronger than the monotone statement.

## Lemma 2.1

For every fixed FO sentence \(\varphi(X)\), there is an integer \(R\) and a polynomial-time algorithm with the following property.

Given a graph \(G\), weights, and a set \(A\subseteq V(G)\) satisfying
\[
\operatorname{dist}_G(a,a')>R
\qquad(a,a'\in A,\ a\ne a'),
\tag{3}
\]
the algorithm finds a maximum-weight set \(S\subseteq A\) satisfying \(\varphi(X)\), or reports that none exists.

Monotonicity is not needed for this lemma. Fixed additional unary input predicates are also allowed.

### Proof

Gaifman normal form expresses \(\varphi\) as a Boolean combination
\[
B(\sigma_1,\ldots,\sigma_t)
\]
of basic local sentences
\[
\sigma_i=
\exists y_1\cdots \exists y_{m_i}
\left[
 \bigwedge_{j<k}\operatorname{dist}(y_j,y_k)>2r_i
 \ \land\
 \bigwedge_{j=1}^{m_i}\psi_i(y_j)
\right],
\tag{4}
\]
where \(\psi_i(y)\) is \(r_i\)-local. All parameters here depend only on \(\varphi\).

Because \(X\) is unary, adding it does not change the Gaifman graph. In particular, the truth of \(\psi_i(v)\) depends on the selected set only through
\[
X\cap N_{r_i}[v].
\]

Set
\[
R=6\max(1,r_1,\ldots,r_t).
\]
By (3), each \(N_{r_i}[v]\) contains at most one candidate vertex. Thus, as \(S\subseteq A\) varies, \(\psi_i(v)\) is either constant or a function of one Boolean variable
\[
z_a=\mathbf 1[a\in S].
\tag{5}
\]

We now describe an exhaustive polynomial-time algorithm.

### Step 1: Guess the truth values of the basic local sentences

Enumerate all \(b=(b_1,\ldots,b_t)\in\{0,1\}^t\) for which \(B(b)\) is true.

For every \(i\) with \(b_i=1\), enumerate a witness tuple
\[
(y_1,\ldots,y_{m_i})
\]
with pairwise distances greater than \(2r_i\). Require \(\psi_i(y_j)\) to hold for each \(j\). By (5), each requirement is a constant test or a restriction on one variable \(z_a\).

### Step 2: Certify the false basic local sentences

Fix \(i\) with \(b_i=0\). For a prospective solution \(S\), write
\[
P_i(S)=\{v:\psi_i(v)\text{ holds in }(G,S)\}.
\]

If \(\sigma_i\) is false, a maximal subset \(W_i\subseteq P_i(S)\) whose vertices have pairwise distances greater than \(2r_i\) has size at most \(m_i-1\). Maximality implies
\[
P_i(S)\subseteq N_{2r_i}[W_i].
\tag{6}
\]

Accordingly, enumerate every set \(W_i\subseteq V(G)\) of size at most \(m_i-1\), including the empty set. Put
\[
B_i=N_{2r_i}[W_i],
\qquad
T_i=A\cap N_{3r_i}[W_i].
\]
Each ball \(N_{3r_i}[w]\) contains at most one candidate, so
\[
|T_i|\le |W_i|\le m_i-1.
\tag{7}
\]

Enumerate the values of all variables belonging to
\[
T=\bigcup_{i:b_i=0}T_i.
\]
The number of these variables is bounded by a constant depending only on \(\varphi\).

For \(v\in B_i\), any candidate that can affect \(\psi_i(v)\) belongs to \(T_i\). Hence, after this enumeration, \(\psi_i(v)\) is known for every \(v\in B_i\). Reject the branch if the true vertices in \(B_i\) contain \(m_i\) vertices at pairwise distances greater than \(2r_i\). This is testable by enumerating \(m_i\)-tuples.

For every \(v\notin B_i\), impose
\[
\neg\psi_i(v).
\tag{8}
\]
Again, each such condition is constant or unary in one \(z_a\).

Conditions (8), together with the check inside \(B_i\), ensure that \(\sigma_i\) is false. It is unnecessary to require the guessed \(W_i\) itself to be a packing: the two checks already suffice.

### Step 3: Optimize the remaining independent choices

All conditions accumulated in a branch are restrictions on individual Boolean variables, together with constant checks.

Reject a branch if a constant check fails or a variable has no allowed value. Otherwise choose, independently for each candidate, its maximum-weight allowed value.

Every resulting set has precisely the guessed truth vector for the \(\sigma_i\), and therefore satisfies \(\varphi\).

Conversely, every feasible \(S\subseteq A\) occurs in some branch: use its actual truth vector, actual positive witnesses, maximal packings \(W_i\) for the false sentences, and its actual assignments on \(T\). In that branch the algorithm returns a set of weight at least \(w(S)\).

There are only polynomially many branches: all tuple lengths, set-size bounds, and formulas are fixed. Direct evaluation of every fixed FO formula is polynomial. This proves the lemma. \(\square\)

# 3. Consequences for arbitrary monotone FO objectives

## Proof of Theorem A

Construct \(H=G^R\), and properly color \(H\) using
\[
k=d(H)+1
\]
colors. Let its color classes be \(A_1,\ldots,A_k\). Each \(A_i\) satisfies (3), so Lemma 2.1 optimizes \(\varphi\) exactly among solutions contained in \(A_i\).

Let \(S^\star\) be an optimum solution. Downward monotonicity gives feasibility of every
\[
S^\star\cap A_i.
\]
Since these sets partition \(S^\star\),
\[
\max_i w(S^\star\cap A_i)\ge \frac{w(S^\star)}k.
\]
Returning the best restricted optimum proves the first bound in (1).

Furthermore,
\[
\Delta(G^R)\le \sum_{j=1}^R\Delta(G)^j,
\]
and therefore
\[
d(G^R)+1
\le 1+\sum_{j=1}^R\Delta(G)^j
\le (\Delta(G)+1)^R.
\]
All algorithms are polynomial for fixed \(\varphi\).

If \(\varphi\) is downward monotone and the empty set is infeasible, there is no feasible solution; this is checked at the outset. Thus infeasible and zero-optimum instances cause no exception. \(\square\)

The monotonicity/intersection argument is the part retained from the previous attempt. The new ingredient is that sufficiently separated candidate sets, unlike merely independent ones, permit exact optimization for the full FO language.

## A fixed number of exceptional vertices

The degree condition can be weakened slightly.

**Corollary 3.1.** Fix \(b\). There is a constant \(R=R(\varphi,b)\) such that, given \(B\subseteq V(G)\) with \(|B|\le b\), monotone \(\varphi\)-maximization admits approximation factor
\[
1+(\Delta(G-B)+1)^R.
\tag{9}
\]

To see this, first optimize over subsets of \(B\) by exhaustive enumeration. For solutions avoiding \(B\), translate \(\varphi\) to \(G-B\): adjacency to each vertex of \(B\) becomes a unary predicate, and quantification over vertices of \(B\) becomes a finite disjunction or conjunction. Set \(X\) false on \(B\). Since \(b\) is fixed, this produces one of finitely many fixed formulas.

Apply the preceding coloring algorithm to \(G-B\). The partition consisting of \(B\) and the resulting color classes gives (9) by monotonicity. If \(B\) is not supplied, all sets of size at most \(b\) can be enumerated in polynomial time.

Thus arbitrary monotone FO objectives have the desired approximation whenever deletion of a fixed number of vertices leaves subpolynomial maximum degree.

The same arguments work for a fixed finite list of solution predicates with coordinatewise downward closure and additive weights: replace each candidate's Boolean variable in Lemma 2.1 by a constant-sized state.

# 4. Distance packing on every nowhere-dense class

Here high degree can be handled without coloring a graph power.

For a linear order \(L\), let
\[
\operatorname{WReach}_r(G,L,v)
\]
contain the vertices \(u\) for which there is a \(v\)-\(u\) path of length at most \(r\) on which \(u\) is the \(L\)-minimum. Include \(v\) itself. Write
\[
\operatorname{wcol}_r(G)
=
\min_L\max_v|\operatorname{WReach}_r(G,L,v)|.
\]

The established nowhere-density characterization needed below is:
\[
\forall r\ge1\ \forall\varepsilon>0\ \exists c:
\quad
\operatorname{wcol}_r(G)\le c|V(G)|^\varepsilon
\quad(G\in\mathcal C)
\tag{10}
\]
for every nowhere-dense class \(\mathcal C\).

To avoid any effectiveness assumption on \(\mathcal C\), I first give an explicit polynomial-time way to obtain a suitable order.

## 4.1. Computing a subpolynomial-width weak order

**Lemma 4.1.** For fixed \(r\), a polynomial-time algorithm finds an order \(L\) satisfying
\[
K:=\max_v|\operatorname{WReach}_r(G,L,v)|
\le
\bigl(1+r(\operatorname{wcol}_r(G)-1)\bigr)^r.
\tag{11}
\]

### Proof

Maintain the set \(S\) of unplaced vertices, and construct the order from last to first.

For each \(v\in S\), greedily find a maximal family \(\mathcal P(S,v)\) of paths satisfying:

* each starts at \(v\), ends in \(S\setminus\{v\}\), and has length at most \(r\);
* internal vertices lie outside \(S\);
* different paths are vertex-disjoint except at \(v\).

Such a family is found by repeatedly searching for another path avoiding all previously used vertices other than \(v\). Choose a vertex minimizing
\[
p(S,v)=|\mathcal P(S,v)|,
\]
place it last among \(S\), and remove it from \(S\).

Put \(k=\operatorname{wcol}_r(G)\), and fix an order \(L^\star\) attaining \(k\). For every nonempty \(S\), let \(v\) be its \(L^\star\)-largest vertex. Any family of paths of the above kind has at most \(k-1\) members: truncate each path at its first vertex smaller than \(v\) in \(L^\star\). The resulting endpoints are distinct members of
\[
\operatorname{WReach}_r(G,L^\star,v)\setminus\{v\}.
\]
Thus the vertex selected by the algorithm always has \(p(S,v)\le k-1\).

For each selected \(v\), let \(Z_v\) be the union of its chosen paths with \(v\) removed. Then
\[
|Z_v|\le r(k-1).
\tag{12}
\]
By maximality, \(Z_v\) meets every path of length at most \(r\) from \(v\) to an earlier vertex whose internal vertices are later than \(v\), in the final order \(L\).

For \(1\le \ell\le r\),
\[
\operatorname{WReach}_{\ell}(G,L,v)
\subseteq
\{v\}\cup
\bigcup_{z\in Z_v}
\operatorname{WReach}_{\ell-1}(G,L,z).
\tag{13}
\]
Indeed, take a witnessing path from \(v\) to \(u\ne v\), and truncate its beginning at the first vertex earlier than \(v\). This prefix meets \(Z_v\). If \(z\) is such an intersection, the remaining \(z\)-\(u\) path has length at most \(\ell-1\), and \(u\) remains its minimum.

Writing \(b=r(k-1)\), recurrence (13) gives
\[
K\le 1+b+\cdots+b^r\le (1+b)^r,
\]
as required. All path searches and greedy packings are polynomial-time operations. \(\square\)

## 4.2. A bounded-interval representation of \(G^r\)

Fix any order \(L\) of weak width \(K\).

For \(z\in\operatorname{WReach}_r(G,L,v)\), define
\[
\ell_z(v)
=
\operatorname{dist}_{G[\{u:z\le_L u\}]}(z,v).
\]
This is an integer between \(0\) and \(r\).

For distinct \(u,v\),
\[
\operatorname{dist}_G(u,v)\le r
\quad\Longleftrightarrow\quad
\exists z\ 
\bigl(\ell_z(u)+\ell_z(v)\le r\bigr),
\tag{14}
\]
where both distances on the right must be defined.

For the forward implication, take the minimum vertex \(z\) on a path of length at most \(r\). The reverse implication follows by concatenating the two paths.

For each fixed \(z\), the relation
\[
\ell_z(u)+\ell_z(v)\le r
\tag{15}
\]
has an interval representation. Here is an explicit one.

* Call \(v\) short if \(\ell_z(v)\le r/2\), and long otherwise.
* Place the long vertices at distinct points \(1,\ldots,m\), in nondecreasing order of \(\ell_z(v)\).
* For a short vertex \(s\), let \(m_s\) be the number of long vertices satisfying
  \[
  \ell_z(v)\le r-\ell_z(s),
  \]
  and give \(s\) the interval \([0,m_s+1/2]\).

All short intervals intersect, the long points are disjoint, and the short–long intersections are precisely (15).

Place the representations for different \(z\)'s in disjoint blocks of the real line. Associate to \(v\) the union \(J_v\) of its intervals over all
\[
z\in\operatorname{WReach}_r(G,L,v).
\]
Thus \(J_v\) consists of at most \(K\) intervals, and (14) yields
\[
J_u\cap J_v\ne\varnothing
\quad\Longleftrightarrow\quad
uv\in E(G^r).
\tag{16}
\]

The representation is constructible in polynomial time and has polynomial size.

## 4.3. Packing unions of at most \(K\) intervals

**Lemma 4.2.** Given weighted sets \(J_v\), each a union of at most \(K\) intervals, a maximum-weight pairwise disjoint subfamily has a deterministic polynomial-time \(4K\)-approximation.

### Proof

Let \(P\) be the set of all right endpoints of the constituent intervals. Solve the LP
\[
\begin{aligned}
\text{maximize }&\sum_v w(v)x_v,\\
\text{subject to }&
\sum_{v:p\in J_v}x_v\le1 &&(p\in P),\\
&0\le x_v\le1 &&(v\in V).
\end{aligned}
\tag{17}
\]
Every disjoint subfamily is feasible for this LP.

Orient each edge \(uv\) of the intersection graph as follows. Choose intersecting constituent intervals of \(J_u,J_v\); the smaller of their right endpoints lies in the other interval. Orient the edge from the owner of that endpoint to the other vertex.

Every out-neighbor of \(v\) contains one of at most \(K\) right endpoints belonging to \(v\). Hence an LP solution satisfies
\[
\sum_{u\in N^+(v)}x_u\le K.
\tag{18}
\]

Independently sample \(v\) with probability
\[
p_v=\frac{x_v}{2K}.
\]
Retain a sampled \(v\) only when none of its out-neighbors was sampled. The retained family is disjoint: a sampled edge deletes its tail.

By (18) and the union bound,
\[
\begin{aligned}
\Pr(v\text{ retained})
&=p_v\prod_{u\in N^+(v)}(1-p_u)\\
&\ge p_v\left(1-\sum_{u\in N^+(v)}p_u\right)\\
&\ge \frac{x_v}{4K}.
\end{aligned}
\]
Thus expected retained weight is at least \(1/(4K)\) times the LP optimum, and therefore at least \(1/(4K)\) times the integral optimum.

This is derandomized by conditional expectations. After any partial assignment of the sampling bits, the expected retained weight is a sum of explicitly computable products. Fix each next bit to a value that does not decrease that expectation. Rational arithmetic has polynomial bit complexity here. \(\square\)

Combining (16) with Lemma 4.2 gives a \(4K\)-approximation for distance-\(r\) independence. Lemma 4.1 proves (2), completing Theorem B.

Finally, (10) implies
\[
4\bigl(1+r(\operatorname{wcol}_r(G)-1)\bigr)^r=n^{o(1)}
\]
uniformly on a fixed nowhere-dense class. The algorithm itself does not require the class constants or an \(\varepsilon\) as input.

### A slightly larger FO fragment

The same argument covers, for fixed \(r,t\), maximizing \(w(S)\) subject to
\[
G^r[S]\text{ containing no }K_{t+1}.
\tag{19}
\]
Indeed, for an optimum \(S^\star\), the assignment
\[
x_v=\frac{\mathbf1[v\in S^\star]}t
\]
is feasible in (17), because every collection of sets containing a common point is a clique in \(G^r\). The rounded independent set satisfies (19) and has weight at least
\[
\frac{w(S^\star)}{4Kt}.
\]
These are downward-monotone FO constraints involving ambient distance witnesses.

# 5. The remaining gap

Theorem A does **not** give a subpolynomial factor on all nowhere-dense classes. For a star on \(n\) vertices and \(R\ge2\),
\[
G^R=K_n,
\qquad
d(G^R)+1=n.
\]
Thus sufficiently separated candidates cannot simply be obtained by a low-loss coloring, even on trees.

Theorem B avoids that loss because distance independence has a specific intersection-packing representation. Arbitrary monotone FO feasibility need not have that representation.

For example,
\[
\eta(X):=
\forall v\,\exists u\,
\bigl(E(v,u)\land\neg X(u)\bigr)
\tag{20}
\]
is downward monotone. On an \(n\)-vertex star, its optimum is \(n-2\): exclude the center and one leaf. In contrast, any distance-two independent set has size at most one. Thus restricting to separated solutions can lose a linear factor for a legitimate monotone FO objective, even though that particular objective is easy on stars.

A full proof still needs to retain many mutually close selected vertices while controlling arbitrary FO quantification through unselected vertices, with only subpolynomial loss. Neither the separated-candidate lemma nor the interval-packing argument supplies that step.

Therefore the general conjecture is not proved here.