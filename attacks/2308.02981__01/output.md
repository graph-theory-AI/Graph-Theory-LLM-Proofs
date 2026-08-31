```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The main FPT and constant-approximation questions remain open, but separable index is exactly max-compatible with substitution, reduces to simple permutations, lies in para-NP, and is FPT for bounded substitution-node arity.",
  "would_publish": false,
  "caveats": "No FPT algorithm in sep, fixed-k hardness result, or constant-factor approximation is obtained; overlap with observations in the full source paper was not checked."
}
```

# 1. Statement and conventions

Let \(\mathcal S_n=\operatorname{Av}_n(2413,3142)\) be the separable permutations of length \(n\). Composition is from right to left. Write
\[
\operatorname{sep}(\pi)=\min\{k:\pi=\alpha_k\circ\cdots\circ\alpha_1,\ \alpha_i\in\mathcal S_n\}.
\]
If empty products are allowed, then \(\operatorname{sep}(\mathrm{id})=0\); otherwise it is \(1\). This convention affects only trivial cases.

I do not resolve whether deciding \(\operatorname{sep}(\pi)\le k\) is FPT, XP, or para-NP-hard, nor whether a constant-factor FPT approximation exists. I prove the following partial results.

### Partial theorem

1. **Inflation formula.** For every inflation
   \[
   \pi=\theta[\rho_1,\ldots,\rho_m],
   \]
   one has
   \[
   \boxed{\operatorname{sep}(\pi)=
   \max\bigl(\operatorname{sep}(\theta),
             \operatorname{sep}(\rho_1),\ldots,
             \operatorname{sep}(\rho_m)\bigr).}
   \]

2. Consequently, if \(T_\pi\) is the substitution decomposition tree of \(\pi\), then
   \[
   \boxed{\operatorname{sep}(\pi)
   =\max_{v\in V(T_\pi)}\operatorname{sep}(\theta_v),}
   \]
   where \(\theta_v\) is the simple, \(12\), or \(21\) quotient labelling \(v\).

   Thus exact computation and constant-factor approximation reduce, under parameter-preserving polynomial-time truth-table reductions, to the same problems restricted to simple permutations.

3. The decision problem has an explicit CNF formulation with
   \[
   O(kn^2)\text{ variables and }O(kn^4)\text{ clauses}.
   \]
   In particular it is in para-NP and, classically, in NP.

4. Every \(n\)-permutation admits a factorization into at most
   \[
   \lceil\log_2 n\rceil
   \]
   separable permutations, constructible in \(O(n\log n)\) time. Hence the exact value can be found with \(O(\log\log n)\) adaptive NP-oracle calls.

5. If \(D(n)=\max_{\pi\in S_n}\operatorname{sep}(\pi)\), then
   \[
   D(n)=\Theta(\log n).
   \]

6. Exact separable index is FPT when parameterized by the maximum arity of a simple node in the substitution decomposition tree. This does not imply FPT parameterized by \(\operatorname{sep}\): there are arbitrarily long simple permutations of separable index exactly \(2\).

# 2. Orders, products, and pattern monotonicity

Represent a permutation \(\pi\) on a ground set \(V\) by two total orders \(L_0,L_\pi\), where \(L_0\) is the position order and
\[
x<_{L_\pi}y\quad\Longleftrightarrow\quad \pi(x)<\pi(y).
\]

A factorization into \(k\) separable permutations is equivalently a chain
\[
L_0,L_1,\ldots,L_k=L_\pi
\]
such that the relative permutation of \(L_{i-1}\) and \(L_i\) is separable for every \(i\).

This immediately gives pattern monotonicity.

### Lemma 2.1
If \(\tau\) is a pattern of \(\pi\), then
\[
\operatorname{sep}(\tau)\le \operatorname{sep}(\pi).
\]

### Proof
Restrict every order in a factorization chain for \(\pi\) to the subset of elements inducing \(\tau\). The relative permutation between two consecutive restricted orders is a pattern of a separable permutation, and hence remains separable. The final restricted pair represents \(\tau\). \(\square\)

Thus
\[
\mathcal C_k:=\{\pi:\operatorname{sep}(\pi)\le k\}
\]
is a permutation class for every \(k\).

# 3. Exact behaviour under inflation

Recall that \(\theta[\rho_1,\ldots,\rho_m]\) is obtained by replacing the \(i\)-th point of \(\theta\) by an interval inducing \(\rho_i\).

Separable permutations are substitution-closed: if \(\alpha\) and all \(\beta_i\) are separable, then \(\alpha[\beta_1,\ldots,\beta_r]\) is separable. This follows by induction from the direct-sum/skew-sum definition of separability.

### Theorem 3.1
For every inflation
\[
\pi=\theta[\rho_1,\ldots,\rho_m],
\]
\[
\operatorname{sep}(\pi)=
\max\bigl(\operatorname{sep}(\theta),
          \operatorname{sep}(\rho_1),\ldots,
          \operatorname{sep}(\rho_m)\bigr).
\]

### Proof

Let
\[
q=\max\bigl(\operatorname{sep}(\theta),
          \operatorname{sep}(\rho_1),\ldots,
          \operatorname{sep}(\rho_m)\bigr).
\]

For the lower bound, \(\theta\) is obtained as a pattern of \(\pi\) by selecting one point from each inflated block. Each \(\rho_i\) is also a pattern of \(\pi\). Lemma 2.1 therefore gives
\[
\operatorname{sep}(\pi)\ge q.
\]

For the upper bound, take order chains of length \(q\)
\[
L^0_0,\ldots,L^0_q
\]
for \(\theta\), and
\[
L^i_0,\ldots,L^i_q
\]
for every \(\rho_i\), padding shorter factorizations by identity permutations.

For each \(t\), form a global order \(\widehat L_t\) by:

1. listing the blocks in order \(L^0_t\);
2. listing the elements inside block \(i\) in order \(L^i_t\).

The relative permutation from \(\widehat L_{t-1}\) to \(\widehat L_t\) is an inflation of the separable outer transition by the separable inner transitions. It is therefore separable. The initial global order is the position order of the inflation, and the final one is its value order. Thus
\[
\operatorname{sep}(\pi)\le q.
\]
\(\square\)

### Consequences

1. Direct and skew sums both satisfy
   \[
   \operatorname{sep}(\pi_1\oplus\cdots\oplus\pi_r)
   =\operatorname{sep}(\pi_1\ominus\cdots\ominus\pi_r)
   =\max_i\operatorname{sep}(\pi_i),
   \]
   with the obvious interpretation for iterated skew sums.

2. Each class \(\mathcal C_k\) is substitution-closed.

3. In the canonical substitution decomposition tree,
   \[
   \operatorname{sep}(\pi)
   =\max_v\operatorname{sep}(\theta_v).
   \]

4. Every minimal excluded permutation for \(\mathcal C_k\) is simple. Indeed, if a nonsimple minimal obstruction were
   \[
   \beta=\theta[\beta_1,\ldots,\beta_m],
   \]
   then \(\theta\) and all \(\beta_i\) would be proper patterns of \(\beta\), hence members of \(\mathcal C_k\). Theorem 3.1 would then imply \(\beta\in\mathcal C_k\), a contradiction.

This does not prove that \(\mathcal C_k\) is finitely based: its simple basis elements might have unbounded length.

# 4. Reduction to simple permutations

Let SIMPLE-SEP denote the decision problem restricted to simple input permutations.

Given a general \(\pi\), compute its substitution decomposition tree. This can be done in polynomial time without invoking sophisticated algorithms: enumerate all position intervals, test whether their values form an interval using range minima and maxima, retain the strong intervals, and form the quotient tree.

Theorem 3.1 gives
\[
\operatorname{sep}(\pi)\le k
\quad\Longleftrightarrow\quad
\operatorname{sep}(\theta_v)\le k
\text{ for every simple label }\theta_v.
\]

Hence:

- general exact decision polynomial-time truth-table reduces to SIMPLE-SEP with the same parameter \(k\);
- SIMPLE-SEP trivially reduces to the general problem;
- exact values are obtained by taking a maximum;
- a \(c\)-approximation on simple permutations extends to a \(c\)-approximation on all permutations by approximating every simple label and synchronizing the resulting factorizations using Theorem 3.1;
- the same statement holds for FPT running times parameterized by the optimum.

Thus the unresolved complexity is already present on simple permutations.

# 5. Arbitrarily large simple permutations of index two

The preceding reduction does not bound the size of the simple labels as a function of \(k\).

For \(n\ge4\), define
\[
A_n=(1\,2)(3\,4)(5\,6)\cdots
\]
and
\[
B_n=(2\,3)(4\,5)(6\,7)\cdots,
\]
with unmatched points fixed. In one-line notation, \(A_n\) is a direct sum of copies of \(21\) and perhaps one singleton; \(B_n\) is a singleton followed by copies of \(21\), and perhaps another singleton. Thus both are separable.

Set
\[
\pi_n=A_n\circ B_n.
\]
For example,
\[
\pi_4=2413,\qquad
\pi_5=24153,\qquad
\pi_6=241635.
\]

A direct parity calculation gives
\[
\pi_n(i)=
\begin{cases}
2,&i=1,\\
i-2,&i\ge3\text{ odd},\\
i+2,&i\le n-2\text{ even},\\
n,&n\text{ odd and }i=n-1,\\
n-1,&n\text{ even and }i=n.
\end{cases}
\]

Its inversion graph is a path, with vertices in path order
\[
1,3,2,5,4,7,6,9,8,\ldots,
\]
truncated to \([n]\). This follows directly by comparing the displayed values: each interior even position is inverted precisely with the next one or two odd positions, with the endpoint modifications shown above.

A path \(P_n\) is prime as a graph for \(n\ge4\). To see this, suppose \(M\) is a proper module with at least two vertices. Since the path is connected, there is an edge \(xy\) with \(x\in M\) and \(y\notin M\). Modulehood forces \(y\) to be adjacent to every member of \(M\), so \(|M|\le2\). If \(|M|=2\), then \(M\) consists of the two neighbours of an internal vertex \(y\); for \(n\ge4\), an outer neighbour distinguishes those two vertices, again contradicting modulehood.

Every nontrivial interval of a permutation is a module in its inversion graph. Therefore \(\pi_n\) is simple. A separable permutation of length at least \(4\) cannot be simple, because its top direct- or skew-sum decomposition supplies a nontrivial interval. Consequently
\[
\boxed{\operatorname{sep}(\pi_n)=2\quad\text{for every }n\ge4.}
\]

Thus simple yes-instances can have unbounded length even for \(k=2\).

# 6. A universal logarithmic factorization

The following elementary construction gives a useful global upper bound.

### Lemma 6.1: binary grouping
Let \(x_1,\ldots,x_m\) be in a current order, and color each \(x_i\) either \(0\) or \(1\). There is a separable transition to an order in which all \(0\)-colored elements precede all \(1\)-colored elements.

### Proof
For a binary word \(w=c_1\cdots c_m\), recursively define a permutation \(q_w\) by
\[
q_\varnothing=\varnothing,
\]
and
\[
q_w=
\begin{cases}
1\oplus q_{c_2\cdots c_m},&c_1=0,\\
1\ominus q_{c_2\cdots c_m},&c_1=1.
\end{cases}
\]
It is separable by construction. Its values on \(0\)-colored positions are precisely the lowest \(|w|_0\) ranks, while its values on \(1\)-colored positions are the highest \(|w|_1\) ranks. Hence increasing output rank lists all zeros before all ones. \(\square\)

### Theorem 6.2
Every \(\pi\in S_n\), \(n\ge2\), satisfies
\[
\boxed{\operatorname{sep}(\pi)\le\lceil\log_2 n\rceil.}
\]

### Proof
Take a balanced binary tree whose leaves, from left to right, are the target ranks \(1,\ldots,n\), and whose height is \(\lceil\log_2n\rceil\).

Initially there is one block containing all elements. At each depth, every current block corresponds to an interval of target ranks. Color an element \(0\) or \(1\) according to whether its target rank lies in the left or right child interval. Apply Lemma 6.1 inside each current block. Since current blocks are contiguous, the direct sum of all these local transitions is separable.

After one layer, each target interval has been split into its two child intervals. After \(\lceil\log_2n\rceil\) layers, all blocks are singletons and occur in target order. \(\square\)

The construction requires \(O(n)\) work per layer and therefore \(O(n\log n)\) time.

Combining this with substitution decomposition gives the refined computable upper bound
\[
\operatorname{sep}(\pi)
\le
\max_v\left\lceil\log_2|\theta_v|\right\rceil,
\]
where \(12\) and \(21\) contribute \(1\). This can be much smaller than \(\lceil\log_2n\rceil\), but it is not a constant-factor approximation: the simple permutations \(\pi_n\) above have optimum \(2\) while this bound is \(\lceil\log_2n\rceil\).

# 7. Worst-case order of magnitude and obstruction sizes

Let
\[
D(n)=\max_{\pi\in S_n}\operatorname{sep}(\pi).
\]
Theorem 6.2 gives \(D(n)\le\lceil\log_2n\rceil\).

For the lower bound, every separable permutation admits a signed plane binary decomposition tree with \(n\) leaves. There are \(C_{n-1}<4^{n-1}\) plane full binary trees and \(2^{n-1}\) sign choices. Hence
\[
|\mathcal S_n|<8^{n-1}.
\]
The number of products of \(k\) separable permutations is therefore at most
\[
|\mathcal S_n|^k<8^{kn}.
\]
On the other hand,
\[
n!\ge (n/e)^n.
\]
Thus if \(n>e\,8^k\), then
\[
n!>8^{kn},
\]
so some \(n\)-permutation has separable index greater than \(k\). Therefore
\[
D(n)\ge \log_8(n/e)-O(1),
\]
and hence
\[
\boxed{D(n)=\Theta(\log n).}
\]

Using the exact enumeration of separable permutations by the large Schröder numbers gives the sharper asymptotic lower bound
\[
D(n)\ge
\frac{\log n-1-o(1)}{\log(3+2\sqrt2)}.
\]

If
\[
b(k)=\min\{|\pi|:\operatorname{sep}(\pi)>k\},
\]
then Theorem 6.2 and the counting argument give
\[
\boxed{2^k<b(k)\le \lfloor e\,8^k\rfloor+1.}
\]
A minimum-size such permutation is a minimal obstruction for \(\mathcal C_k\), hence is simple by Section 3. The existence of one exponentially bounded obstruction does not imply that all basis elements have bounded length.

# 8. Exact SAT formulation

For \(t=1,\ldots,k-1\) and unordered pairs \(\{u,v\}\subseteq[n]\), introduce a Boolean variable encoding whether
\[
u<_{L_t}v.
\]
Write \(X_t(u,v)\) for the corresponding literal, with
\[
X_t(v,u)=\neg X_t(u,v).
\]
For the fixed endpoint orders, let
\[
X_0(u,v)=[u<v],
\qquad
X_k(u,v)=[\pi(u)<\pi(v)]
\]
be constants.

For every intermediate \(t\) and every distinct \(a,b,c\), impose transitivity:
\[
\neg X_t(a,b)\vee \neg X_t(b,c)\vee X_t(a,c).
\]

For every layer \(t=1,\ldots,k\) and every ordered quadruple of distinct elements \((a,b,c,d)\), forbid a \(2413\) transition by adding
\[
\begin{aligned}
&\neg X_{t-1}(a,b)\vee
\neg X_{t-1}(b,c)\vee
\neg X_{t-1}(c,d)\\
&\qquad\vee
\neg X_t(c,a)\vee
\neg X_t(a,d)\vee
\neg X_t(d,b),
\end{aligned}
\]
and forbid a \(3142\) transition by adding
\[
\begin{aligned}
&\neg X_{t-1}(a,b)\vee
\neg X_{t-1}(b,c)\vee
\neg X_{t-1}(c,d)\\
&\qquad\vee
\neg X_t(b,d)\vee
\neg X_t(d,a)\vee
\neg X_t(a,c).
\end{aligned}
\]

Indeed, if \(a<b<c<d\) in \(L_{t-1}\), then

- \(c<a<d<b\) in \(L_t\) gives relative pattern \(2413\);
- \(b<d<a<c\) in \(L_t\) gives relative pattern \(3142\).

Conversely, every forbidden occurrence is captured by one ordered quadruple.

Thus the formula is satisfiable exactly when
\[
\operatorname{sep}(\pi)\le k.
\]
It has
\[
(k-1)\binom n2=O(kn^2)
\]
variables and \(O(kn^4)\) clauses.

Consequences:

- The parameterized decision problem is in para-NP.
- The classical decision problem is in NP. If \(k\ge\lceil\log_2n\rceil\), Theorem 6.2 answers yes immediately; otherwise the certificate has polynomial size even when \(k\) is binary encoded.
- The exact value can be found by binary search over
  \[
  [0,\lceil\log_2n\rceil],
  \]
  using \(O(\log\log n)\) adaptive NP-oracle calls.

This SAT formulation does not establish XP or FPT: even the \(k=2\) slice asks whether there is a total order \(L_1\) with
\[
L_0\xrightarrow{\mathrm{separable}}L_1
\xrightarrow{\mathrm{separable}}L_\pi,
\]
and no polynomial-time algorithm or hardness proof for this slice is supplied here.

# 9. FPT for bounded substitution-node arity

Define
\[
r(\pi)=\max\bigl(2,\ |\theta_v|:v\text{ a simple node of }T_\pi\bigr).
\]

Exact separable index is FPT parameterized by \(r(\pi)\).

For every \(m\le r\), construct the Cayley graph with:

- vertex set \(S_m\);
- an edge from \(\gamma\) to \(\alpha\circ\gamma\) for every \(\alpha\in\mathcal S_m\).

Breadth-first search from the identity computes \(\operatorname{sep}(\gamma)\) for every \(\gamma\in S_m\). The preprocessing time is at most
\[
\sum_{m\le r} m!\,|\mathcal S_m|\,m^{O(1)},
\]
which is a function only of \(r\). Looking up all simple labels and taking their maximum then takes polynomial time in \(n\).

Hence exact computation has running time
\[
f(r(\pi))\,n^{O(1)}.
\]

The family \(\pi_n\) from Section 5 shows why this does not give an FPT algorithm parameterized by separable index: \(r(\pi_n)=n\) while \(\operatorname{sep}(\pi_n)=2\).

# 10. Remaining gaps

The principal questions remain unresolved:

1. It is not shown that deciding \(\operatorname{sep}(\pi)\le k\) is FPT or even in XP.
2. No fixed slice, including \(k=2\), is shown NP-hard.
3. No W-hierarchy or para-NP hardness classification is obtained.
4. No constant-factor approximation is obtained. The substitution theorem shows that it suffices to solve the approximation problem on simple permutations.
5. The basis of \(\mathcal C_k\) consists only of simple permutations, but it is not shown to be finite or to have bounded obstruction size as a function of \(k\).

Thus the exact parameterized complexity and constant-factor approximability asked in the catalog remain open.