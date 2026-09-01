```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A fixed monotone FO problem has arbitrarily bad bounded-exchange local optima even on subcubic trees, ruling out the unmodified local-search paradigm but not unrestricted variations.",
  "would_publish": false,
  "caveats": "Only strictly improving bounded-support neighborhoods are ruled out; the phrase “some variation” has no formal definition."
}
```

## 1. Precise scope

The stated problem is not literally a yes/no mathematical proposition because “some variation on the local search approach” does not specify the permitted initialization, neighborhoods, auxiliary state, or temporary worsening moves. Under the standard interpretation—repeatedly replace the current feasible set by a better feasible set differing on at most \(k=k(\varepsilon)\) vertices—there is a simple obstruction.

The result below applies under the usual definition in which a monotone FO maximization problem has a fixed FO feasibility formula whose feasible sets are downward closed, while a monotone FO minimization problem has upward-closed feasible sets.

## 2. Bounded-exchange local search

For feasible vertex sets \(S,S'\), call \(S'\) a \(k\)-exchange from \(S\) if
\[
|S\setminus S'|\leq k
\qquad\text{and}\qquad
|S'\setminus S|\leq k.
\]
The argument also applies when the stronger condition \(|S\triangle S'|\leq k\) is imposed.

A feasible set is a \(k\)-local optimum if no improving feasible \(k\)-exchange exists.

## 3. Fixed FO problems

Let
\[
\lambda(x):=\exists y\bigl(E(x,y)\land
     \forall z\,(E(x,z)\rightarrow z=y)\bigr),
\]
so that \(\lambda(x)\) says that \(x\) is a leaf. Let \(X\) be the unary predicate representing the solution.

### Maximization formula

Define
\[
\varphi_{\max}(X):=
\neg\exists x\exists y\,
 \bigl(X(x)\land X(y)\land \lambda(x)\land\neg\lambda(y)\bigr).
\]

Thus a feasible set cannot contain both a leaf and a nonleaf. If \(L\) and \(U\) denote the sets of leaves and nonleaves, respectively, then
\[
\mathcal F_{\max}(G)=\{S:S\subseteq L\}\cup\{S:S\subseteq U\}.
\]

This family is downward closed. In negation normal form all occurrences of \(X\) are negative:
\[
\forall x\forall y\,
\bigl(\neg X(x)\lor\neg X(y)\lor\neg\lambda(x)\lor\lambda(y)\bigr).
\]

The objective is to maximize \(|X|\).

### Minimization formula

Define
\[
\varphi_{\min}(X):=
 \left[\forall x\,(\lambda(x)\rightarrow X(x))\right]
 \lor
 \left[\forall x\,(\neg\lambda(x)\rightarrow X(x))\right].
\]

A set is feasible precisely when it contains every leaf or contains every nonleaf:
\[
\mathcal F_{\min}(G)
 =\{S:L\subseteq S\}\cup\{S:U\subseteq S\}.
\]
This family is upward closed, and all occurrences of \(X\) are positive in negation normal form. The objective is to minimize \(|X|\).

Both formulas are fixed and independent of the exchange radius.

## 4. The graph class

Let \(\mathcal C\) be the class of subcubic forests. This class has constant-size balanced separators. Indeed, if every component of an \(n\)-vertex forest has at most \(2n/3\) vertices, the empty set is a balanced separator. Otherwise, take a centroid of the unique component having more than \(2n/3\) vertices. Deleting that vertex leaves components of size at most \(n/2\), while all other original components have size below \(n/3\).

Consequently \(\mathcal C\) has strongly sublinear separators, for example separators of size at most \(1=O(n^{1/2})\).

## 5. Arbitrarily bad local optima

### Proposition

For every integer \(k\geq 0\) and every \(A>0\), there is a subcubic tree \(G\) such that:

1. the maximization problem defined by \(\varphi_{\max}\) has a \(k\)-local optimum \(S\) with
   \[
   \frac{\operatorname{OPT}(G)}{|S|}>A;
   \]
2. the minimization problem defined by \(\varphi_{\min}\) has a \(k\)-local optimum \(T\) with
   \[
   \frac{|T|}{\operatorname{OPT}(G)}>A.
   \]

### Construction

Put \(m=k+2\). Take a subcubic tree \(H_m\) having exactly \(m\) leaves. Such a tree exists for every \(m\geq2\): for \(m=2\) take an edge, for \(m=3\) take \(K_{1,3}\), and for larger \(m\) take any unrooted binary tree with \(m\) leaves.

Subdivide edges sufficiently many times to obtain a tree \(G\) with
\[
|L|=m,\qquad |U|=N,
\]
where
\[
N>Am
\quad\text{and}\quad
N>m.
\]
Subdividing edges creates only degree-two vertices, so the number of leaves remains \(m\), and the tree remains subcubic.

### Maximization

Take \(S=L\), the set of all leaves. It is feasible and has size \(m\).

Because every feasible set is contained either in \(L\) or in \(U\), and \(N>m\),
\[
\operatorname{OPT}(G)=N,
\]
attained by \(U\).

Suppose \(S'\) is a better feasible solution. Since \(S\) already contains every leaf, \(S'\) cannot be a subset of \(L\). It must therefore be contained in \(U\). Hence every leaf is deleted:
\[
|S\setminus S'|=m=k+2>k.
\]
Thus no improving \(k\)-exchange exists, so \(S\) is a \(k\)-local optimum. Nevertheless,
\[
\frac{|S|}{\operatorname{OPT}(G)}
 =\frac{m}{N}<\frac1A.
\]

### Minimization

Take \(T=U\), the set of all nonleaves. It is feasible and has size \(N\). Since \(m<N\), the optimum is \(L\), with
\[
\operatorname{OPT}(G)=m.
\]

Let \(T'\) be any better feasible solution, so \(|T'|<N\). It cannot contain all of \(U\), since that alone would give it size at least \(N\). Therefore, by \(\varphi_{\min}\), it must contain every leaf. As \(T\cap L=\varnothing\),
\[
|T'\setminus T|\geq |L|=m=k+2>k.
\]
Hence \(T\) is a \(k\)-local optimum, while
\[
\frac{|T|}{\operatorname{OPT}(G)}
 =\frac{N}{m}>A.
\]

This proves the proposition.

## 6. Strengthening to sublinear-size exchanges

The same construction rules out any guarantee based on all local optima for neighborhoods of support \(b(n)=o(n)\).

For sufficiently large \(n\), let
\[
m=\max\{b(n)+1,2\}.
\]
Choose an \(n\)-vertex subcubic tree with exactly \(m\) leaves, obtained by starting with a subcubic tree on \(2m-2\) vertices having \(m\) leaves and subdividing edges. Then there are \(n-m\) nonleaves.

The leaf solution for maximization cannot be improved without deleting all \(m>b(n)\) leaves, while the nonleaf solution for minimization cannot be improved without adding all \(m>b(n)\) leaves. Since \(m=o(n)\),
\[
\frac{m}{n-m}\longrightarrow 0
\quad\text{and}\quad
\frac{n-m}{m}\longrightarrow\infty.
\]

Thus even allowing \(o(n)\)-vertex exchanges does not make every local optimum a constant-factor approximation for these fixed problems.

## 7. Consequences and remaining gap

This disproves the following natural strengthening of the known local-search results:

> For every monotone FO optimization problem and every accuracy parameter, every sufficiently large bounded-exchange local optimum is near-optimal on classes with strongly sublinear separators.

The obstruction is a global FO-definable choice between two modes. In the maximization example, moving from the leaf mode to the nonleaf mode requires first abandoning every selected leaf; any strictly improving bounded-change trajectory is trapped. The graph itself has excellent separators, but the feasibility relation creates a complete global incompatibility between two FO-definable vertex types.

This does **not** resolve the catalogued question as phrased. A variation could, for example:

- recognize and enumerate the two global modes;
- use structured moves changing linearly many vertices;
- use multiple initial solutions;
- permit temporary objective deterioration;
- decompose the FO formula before invoking local search.

Indeed, the two displayed example problems are themselves exactly solvable by simply comparing the numbers of leaves and nonleaves. Therefore the argument is a barrier to the trivial bounded-change local-search paradigm, not a counterexample to the existence of every conceivable local-search-based PTAS.