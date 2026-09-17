```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For cographs, I prove the conjecture with C=4 and d=8, with optimal asymptotic powers for the set size and edit tolerance when multiplicative constants are allowed.",
  "would_publish": false,
  "caveats": "The arbitrary hereditary-family case remains unresolved; constants are not optimized, and novelty of this special-case result is not asserted."
}
```

# A sharp-power special case: cographs

I do not resolve Conjecture 10 for arbitrary proper hereditary families. I prove the following quantitative special case, including lower bounds on the powers of \(\varepsilon\).

An \(\varepsilon\)-homogeneous set means a vertex set whose induced edge density is at most \(\varepsilon\) or at least \(1-\varepsilon\). Sets of size at most one are declared homogeneous.

Let \(\mathcal C\) be the family of **cographs**, generated from one-vertex graphs by disjoint union and complete join. This family is hereditary. It is proper because every nontrivial cograph is disconnected or has disconnected complement, whereas \(P_4\) and its complement are both connected.

## 1. Quantitative result

**Theorem.** Let \(0<\varepsilon<1/2\). If an \(n\)-vertex graph \(G\) is
\[
\frac{\varepsilon^2}{64}\text{-close to }\mathcal C,
\]
then \(G\) contains an \(\varepsilon\)-homogeneous set of size at least
\[
\frac{\varepsilon n}{8}.
\tag{1}
\]

Consequently, Conjecture 10 holds for cographs, and for every hereditary subfamily of cographs, with
\[
C_{\mathcal F}=4,\qquad d_{\mathcal F}=8.
\]

Moreover:

* The size guarantee \(c\varepsilon n\) cannot be replaced uniformly by \(c\varepsilon^p n\) with \(p<1\), even without edits.
* The edit tolerance \(c\varepsilon^2\) cannot be replaced uniformly by \(c\varepsilon^p\) with \(p<2\), even if the required homogeneous-set size is allowed to be an arbitrarily small positive linear fraction depending on \(\varepsilon\).

Thus the powers \(1\) and \(2\) in the version with multiplicative constants are optimal. This does **not** assert that the normalized pair \(C=1,d=2\) works.

## 2. Almost-homogeneous sets in cographs

We first establish the structural ingredient.

**Lemma.** For every \(0<\delta<1\), every \(N\)-vertex cograph contains a \(\delta\)-homogeneous set of size at least
\[
\frac{\delta N}{2}.
\tag{2}
\]

### Proof

Fix a binary union/join decomposition tree of the cograph. Let \(t\ge 1\).

We construct two collections of disjoint vertex blocks:

* an **anticomplete collection**, with no edges between distinct blocks;
* a **complete collection**, with all possible edges between distinct blocks.

Each block has at most \(t\) vertices. Edges within a block are unrestricted.

For a decomposition node with at most \(t\) vertices, use its entire vertex set as a single block in either collection. At a larger node, let \(a_i,b_i\) be the total sizes of the two collections constructed in child \(i\). Define
\[
(a,b)=
\begin{cases}
(a_1+a_2,\ \max\{b_1,b_2\}),&\text{at a union node},\\[2mm]
(\max\{a_1,a_2\},\ b_1+b_2),&\text{at a join node}.
\end{cases}
\tag{3}
\]
These formulas correspond to taking unions of compatible collections or retaining the larger collection.

We claim that at every node with \(M>t\) vertices,
\[
a,b\ge \frac t2,
\qquad
ab\ge \frac{tM}{2}.
\tag{4}
\]

It suffices to check a union node; join nodes are symmetric.

* If both children have at most \(t\) vertices, of sizes \(x,y\), then
  \[
  a=x+y,\qquad b=\max\{x,y\}>t/2,
  \]
  giving (4).
* If both children have more than \(t\) vertices, induction gives
  \[
  ab=(a_1+a_2)\max\{b_1,b_2\}
  \ge a_1b_1+a_2b_2
  \ge \frac{tM}{2}.
  \]
  The individual lower bounds follow as well.
* If one child has more than \(t\) vertices and the other has \(y\le t\) vertices, then
  \[
  a=a_1+y,\qquad b=\max\{b_1,y\}\ge t/2.
  \]
  Hence
  \[
  ab\ge a_1b_1+\frac{ty}{2}\ge \frac{tM}{2},
  \]
  and \(a,b\ge t/2\).

Thus, whenever \(N>t\), one of the two collections has total size
\[
s\ge \sqrt{\frac{tN}{2}}.
\tag{5}
\]

Now suppose first that
\[
t=\frac{\delta^2N}{2}\ge1.
\]
Since \(t<N\), (5) gives \(s\ge\delta N/2\). Let \(S\) be the union of the selected blocks.

According to the collection’s type, either every edge or every nonedge of \(G[S]\) lies within a block. If the block sizes are \(s_1,\ldots,s_\ell\), the number of these exceptional pairs is at most
\[
\sum_i\binom{s_i}{2}
\le \frac{t-1}{2}\sum_i s_i
=\frac{(t-1)s}{2}.
\]
Here \(s\ge t/\delta>t\), so their density is at most
\[
\frac{t-1}{s-1}\le \frac ts\le\delta.
\]
This proves (2) in this case.

If \(\delta^2N/2<1\) and \(N\ge2\), use \(t=1\). Every block is a singleton, so the selected set is exactly homogeneous, and
\[
s\ge\sqrt{N/2}>\delta N/2.
\]
The case \(N=1\) is immediate. \(\square\)

## 3. Robustness under edits

Let \(H\in\mathcal C\) be obtained from \(G\) by changing at most
\[
\frac{\rho n^2}{2}
\]
edges, where \(0<\rho\le\varepsilon^2/64\).

Let \(D\) be the graph whose edges are precisely the changed pairs. Then
\[
\sum_{v\in V(G)}d_D(v)\le \rho n^2.
\]
Remove the vertices with \(D\)-degree greater than \(2\rho n\). The remaining set \(U\) satisfies
\[
|U|\ge n/2,\qquad \Delta(D[U])\le2\rho n.
\tag{6}
\]

The graph \(H[U]\) is a cograph. Applying the lemma with \(\delta=\varepsilon/2\), we obtain an \(\varepsilon/2\)-homogeneous set \(S\subseteq U\) with
\[
s:=|S|\ge \frac{\varepsilon|U|}{4}
\ge \frac{\varepsilon n}{8}.
\tag{7}
\]

If \(s=1\), there is nothing more to prove. Otherwise, the proportion of changed pairs inside \(S\) is at most
\[
\frac{e_D(S)}{\binom{s}{2}}
\le \frac{2\rho n}{s-1}
\le \frac{4\rho n}{s}
\le \frac{32\rho}{\varepsilon}
\le \frac{\varepsilon}{2}.
\]
Thus the density of \(G[S]\) differs from that of \(H[S]\) by at most \(\varepsilon/2\). Since \(H[S]\) is \(\varepsilon/2\)-homogeneous, \(G[S]\) is \(\varepsilon\)-homogeneous. This proves (1).

Finally, for \(0<\varepsilon<1/2\),
\[
\varepsilon^8\le \frac{\varepsilon^2}{64},
\qquad
\frac{\varepsilon}{8}\ge\varepsilon^4.
\]
Therefore the original normalized formulation holds with \(C=4,d=8\). Closeness to a subfamily of \(\mathcal C\) implies closeness to \(\mathcal C\), so the same constants apply to all hereditary subfamilies.

## 4. Why the size power \(1\) is necessary

Define cographs recursively by
\[
H_0=K_1,\qquad
H_{k+1}=(H_k\sqcup H_k)\vee(H_k\sqcup H_k),
\tag{8}
\]
where \(\vee\) denotes complete join. Induction gives
\[
|V(H_k)|=4^k,\qquad
\alpha(H_k)=\omega(H_k)=2^k.
\tag{9}
\]
Write
\[
a=2^k,\qquad n=a^2,\qquad \varepsilon=\frac1{4a}.
\]

We use the elementary bound that an \(s\)-vertex graph \(J\) with independence number at most \(a\) satisfies
\[
e(J)\ge \frac12\left(\frac{s^2}{a}-s\right).
\tag{10}
\]
For completeness, selecting vertices that precede all their neighbors in a uniformly random ordering gives
\[
a\ge\alpha(J)\ge\sum_v\frac1{d_J(v)+1}
\ge\frac{s^2}{2e(J)+s},
\]
which implies (10).

If \(S\subseteq V(H_k)\) is \(\varepsilon\)-sparse, then (10) yields
\[
\frac{s^2}{a}-s\le \varepsilon s(s-1),
\]
and hence
\[
s\le \frac{a(1-\varepsilon)}{1-a\varepsilon}
\le \frac{4a}{3}.
\tag{11}
\]
The same bound holds for an \(\varepsilon\)-dense set, by applying the argument to the complement and using \(\omega(H_k)=a\).

But, for any fixed \(c>0\) and \(p<1\),
\[
c\varepsilon^p n=c\,4^{-p}a^{2-p},
\]
which eventually exceeds \(4a/3\). Thus no uniform lower bound \(c\varepsilon^p n\) with \(p<1\) is possible, even for exact cographs.

## 5. Why the edit-tolerance power \(2\) is necessary

Here the obstruction is stronger: an exponent below \(2\) permits graphs with **no homogeneous set of any prescribed positive linear size**.

Fix \(0<d<2\). Choose \(k\) sufficiently large that, with
\[
a=2^k,\qquad m=a^2,\qquad \varepsilon=\frac1{4a},
\]
we have
\[
\frac1m\le\varepsilon^d.
\tag{12}
\]
This is possible because \(a^{2-d}\to\infty\).

Replace each vertex of \(H_k\) by a block of \(N\) vertices. Between distinct blocks, retain the complete-or-empty adjacency prescribed by \(H_k\). Inside each block, independently place a random graph \(G(N,1/2)\). Call the resulting graph \(G_N\), and write \(n=mN\).

Deleting all within-block edges leaves an independent blow-up of \(H_k\), which is a cograph. At most
\[
m\binom N2\le \frac{n^2}{2m}
\]
edges are deleted. Thus \(G_N\) is \(1/m\)-close, and by (12) it is \(\varepsilon^d\)-close, to cographs.

We show that, for every fixed \(\beta>0\), sufficiently large \(N\) admits a realization with no \(\varepsilon\)-homogeneous set of size at least \(\beta n\).

### A weighted density bound

For nonnegative weights \(x_1,\ldots,x_m\) summing to one, put
\[
Q(x)=\frac12\sum_i x_i^2+
2\sum_{ij\in E(H_k)}x_ix_j.
\tag{13}
\]
Then
\[
\frac1{2a}\le Q(x)\le 1-\frac1{2a}.
\tag{14}
\]

To prove the lower bound, suppose two adjacent vertices have positive weights. Keeping their sum fixed, \(Q\) is a concave quadratic in either weight. Moving all their combined weight to one endpoint can therefore be done without increasing \(Q\). Repeating this operation leaves weights supported on an independent set, of size at most \(a\). On that support,
\[
Q(x)=\frac12\sum_i x_i^2\ge\frac1{2a}.
\]
The upper bound follows by applying the lower bound to the complement, because \(1-Q(x)\) is the analogous expression for \(\overline{H_k}\) and \(\alpha(\overline{H_k})=a\).

### Uniform control of the random blocks

With probability tending to one, every subset \(T\) of every block satisfies
\[
\left|e(T)-\frac12\binom{|T|}{2}\right|\le N^{3/2}.
\tag{15}
\]
Indeed, the elementary Bernoulli tail bound gives failure probability at most \(2e^{-4N}\) for each \(T\). A union bound over the \(m2^N\) possible choices gives total failure probability at most
\[
2m\,2^N e^{-4N}=o(1).
\]

Choose a realization satisfying (15). For \(S\subseteq V(G_N)\), write
\[
s_i=|S\cap V_i|,\qquad s=|S|,\qquad x_i=s_i/s.
\]
The prescribed cross-edges and (15) imply
\[
\left|d_{G_N}(S)-Q(x)\right|
\le
\frac1{2(s-1)}
+\frac{2mN^{3/2}}{s(s-1)}.
\tag{16}
\]
For \(s\ge\beta mN\), the right-hand side tends uniformly to zero as \(N\to\infty\).

Since \(1/(2a)=2\varepsilon\), (14)–(16) give, for sufficiently large \(N\),
\[
\varepsilon<d_{G_N}(S)<1-\varepsilon
\]
for every \(S\) with \(|S|\ge\beta n\).

Taking \(\beta=\varepsilon^C\) disproves every proposed pair \((C,d)\) with \(d<2\) for the family of cographs. The same argument accommodates any fixed positive prefactor in the edit tolerance, because \(a^{-2}=o(\varepsilon^d)\) when \(d<2\).

This is a lower bound on possible exponents, not a counterexample to Conjecture 10.

## 6. What remains unresolved

The argument proves a quantitatively sharp-power special case without invoking any unproved conjecture.

Its essential structural input is the recursive decomposition into complete and anticomplete joins. An arbitrary proper hereditary family need not have such a decomposition, and no replacement for the capped-block lemma has been established here. Consequently, the assertion for arbitrary proper hereditary families remains unresolved by this argument.