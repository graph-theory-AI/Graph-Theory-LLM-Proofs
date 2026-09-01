```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for k at most 2 and, more generally, for every class with log |T| = O(gamma(T)); a quantitative local-to-global bound is proved, but the unrestricted case k at least 3 remains open.",
  "would_publish": false,
  "caveats": "The general bound still depends logarithmically on the order of the tournament, and no unrestricted proof or counterexample is obtained."
}
```

## 1. Statement and notation

A set \(D\subseteq V(T)\) dominates a tournament \(T\) if every vertex in \(V(T)\setminus D\) is the head of an arc from some vertex of \(D\). Write \(\gamma(T)\) for the minimum size of such a set.

For \(S\subseteq V(T)\), define its common predecessor set by
\[
C_T(S)=\{v\in V(T)\setminus S: v\to s\text{ for every }s\in S\}.
\]
Thus \(S\) fails to dominate \(T\) precisely when \(C_T(S)\neq\varnothing\).

The problem asks whether, for every fixed \(k\), there are \(K,\ell\) such that
\[
\gamma(T)\ge K
\]
forces an \(\ell\)-vertex induced subtournament \(H\) with \(\gamma(H)\ge k\).

I do not resolve the unrestricted problem. The main partial result below shows that it holds whenever the order of the tournament is at most exponential, with fixed base, in its domination number.

---

## 2. Common predecessor sets retain large domination number

### Lemma 2.1
For every tournament \(T\) and every \(S\subseteq V(T)\),
\[
\gamma\bigl(T[C_T(S)]\bigr)\ge \gamma(T)-|S|.
\]

### Proof
Put \(A=C_T(S)\), and let \(D\) dominate \(T[A]\). Every vertex
\[
x\in V(T)\setminus(S\cup A)
\]
fails to beat all vertices of \(S\), so some \(s\in S\) satisfies \(s\to x\). Hence \(S\) dominates \(V(T)\setminus(S\cup A)\), while \(D\) dominates \(A\). Therefore \(S\cup D\) dominates \(T\), and
\[
\gamma(T)\le |S|+\gamma(T[A]).
\]
Rearranging proves the lemma. \(\square\)

This is stronger than the elementary cardinality bound
\[
|C_T(S)|\ge \gamma(T)-|S|.
\]

We will also use the standard greedy estimate.

### Lemma 2.2
Every tournament \(R\) on \(m\) vertices satisfies
\[
\gamma(R)\le \left\lceil\log_2(m+1)\right\rceil.
\]
Consequently, if \(\gamma(R)\ge q\), then
\[
|R|\ge 2^{q-1}.
\]

### Proof
In any \(a\)-vertex tournament there is a vertex of outdegree at least \((a-1)/2\). Selecting it leaves at most \((a-1)/2\) undominated vertices. If \(a_i\) is the number left after \(i\) selections, then
\[
a_{i+1}+1\le \frac{a_i+1}{2}.
\]
Thus after \(\lceil\log_2(m+1)\rceil\) selections none remain. The second assertion follows by contraposition. \(\square\)

Combining the two lemmas, if \(d=\gamma(T)\) and \(|S|=r<d\), then
\[
|C_T(S)|\ge 2^{d-r-1}. \tag{2.1}
\]

---

## 3. The cases \(k=1,2\)

### Proposition 3.1
The conjecture holds for \(k=1\) and \(k=2\).

### Proof

- For \(k=1\), take \(K=\ell=1\).
- For \(k=2\), take \(K=2\) and \(\ell=3\). If \(\gamma(T)\ge2\), then \(T\) has no vertex dominating all other vertices. A tournament with no directed triangle is transitive and therefore has such a vertex. Hence \(T\) contains a directed triangle. A directed triangle has domination number \(2\). \(\square\)

---

## 4. The smallest obstruction for \(k=3\)

Although this does not settle \(k=3\), the first possible local witness can be identified exactly.

### Proposition 4.1
Every tournament on at most six vertices has domination number at most \(2\). Up to isomorphism, there is a unique seven-vertex tournament with domination number \(3\), namely the Paley tournament \(P_7\), defined on \(\mathbb Z_7\) by
\[
i\to j
\quad\Longleftrightarrow\quad
j-i\in\{1,2,4\}\pmod 7.
\]

### Proof
Let \(T\) have at most six vertices. Choose \(v\) of maximum outdegree. Then
\[
|N^-(v)|\le 2.
\]
A source of the tournament induced by \(N^-(v)\), together with \(v\), dominates \(T\). Thus \(\gamma(T)\le2\).

Now suppose \(|T|=7\) and \(\gamma(T)\ge3\). If some vertex had indegree at most two, the same argument would give a dominating pair. Hence every vertex has indegree at least three. Since the sum of all indegrees is \(21\), every vertex has indegree and outdegree exactly three.

For every \(v\), the tournament \(T[N^-(v)]\) must be a directed triangle: if it were transitive, its source together with \(v\) would dominate \(T\).

Consider an arc \(x\to y\). The set \(N^-(y)\) is a directed triangle containing \(x\), and exactly one of its other two vertices beats \(x\). Therefore every unordered pair of vertices has exactly one common predecessor.

Fix a vertex \(0\), and put
\[
A=N^+(0),\qquad B=N^-(0).
\]
Both \(A\) and \(B\) induce directed triangles. Each \(b\in B\) already has two outneighbors in \(B\cup\{0\}\), so it has exactly one outneighbor in \(A\). Uniqueness of common predecessors shows that these three arcs from \(B\) to \(A\) form a perfect matching. The requirement that each \(N^-(b)\) induce a directed triangle forces this matching to reverse the cyclic orders on \(A\) and \(B\). Up to relabelling this gives precisely the orientation
\[
i\to j\iff j-i\in\{1,2,4\}\pmod 7.
\]

Conversely, in this tournament every pair has a common predecessor, so no pair dominates it. Lemma 2.2 gives \(\gamma(P_7)\le3\), and hence \(\gamma(P_7)=3\). \(\square\)

A crucial caveat is that domination number is not hereditary under taking induced subtournaments. Thus Proposition 4.1 does not show that every tournament of domination number at least \(3\) contains \(P_7\).

---

## 5. A quantitative local-to-global estimate

The following is the main general partial result.

### Theorem 5.1
Let \(1\le r<\ell\), and define
\[
p_{\ell,r}=\binom{\ell}{r}^{-1/(\ell-r)},
\qquad
q_{\ell,r}=1-p_{\ell,r}.
\]
Suppose that every \(\ell\)-vertex subtournament of an \(n\)-vertex tournament \(T\) has domination number at most \(r\). Then
\[
\gamma(T)
\le
r\left\lceil
\frac{\log(n/\ell)}{\log(1/q_{\ell,r})}
\right\rceil+\ell
\qquad(n\ge\ell). \tag{5.1}
\]

For fixed \(r\) and \(\ell\to\infty\),
\[
q_{\ell,r}\sim \frac{r\log\ell}{\ell},
\]
so the leading term in (5.1) is approximately
\[
\frac{r\log n}{\log\ell}.
\]

### Proof
For an \(r\)-set \(D\), let
\[
M(D)=D\cup\bigcup_{d\in D}N^+(d),
\]
the set consisting of \(D\) and all vertices dominated by \(D\).

Every \(\ell\)-set \(U\) has a dominating set of size at most \(r\). Padding it inside \(U\), if necessary, gives an \(r\)-set \(D\subseteq U\) dominating \(T[U]\). Thus
\[
\binom n\ell
\le
\sum_{D\in\binom{V(T)}r}
\binom{|M(D)|-r}{\ell-r}.
\]
Consequently, some \(r\)-set \(D\) satisfies
\[
\binom{|M(D)|-r}{\ell-r}
\ge
\frac{\binom n\ell}{\binom nr}
=
\frac{\binom{n-r}{\ell-r}}{\binom\ell r}.
\]
Writing \(s=\ell-r\), and using
\[
\frac{\binom Ms}{\binom Ns}\le \left(\frac MN\right)^s,
\]
we obtain
\[
\frac{|M(D)|-r}{n-r}
\ge
\binom{\ell}{r}^{-1/(\ell-r)}
=p_{\ell,r}.
\]
Therefore the undominated set
\[
C_T(D)=V(T)\setminus M(D)
\]
has size at most
\[
q_{\ell,r}(n-r)\le q_{\ell,r}n. \tag{5.2}
\]

The hypothesis is hereditary: it remains true in every induced subtournament. We may therefore repeat the argument on the undominated set. After \(t\) repetitions, at most \(q_{\ell,r}^t n\) vertices remain. Taking
\[
t=
\left\lceil
\frac{\log(n/\ell)}{\log(1/q_{\ell,r})}
\right\rceil
\]
leaves at most \(\ell\) vertices. The union of the \(t\) selected \(r\)-sets and the final residual set dominates \(T\), proving (5.1). \(\square\)

This improves the universal \(O(\log n)\) domination bound by an arbitrarily small multiplicative constant when \(\ell\) is allowed to grow. It does not, however, remove the dependence on \(n\).

---

## 6. The conjecture for tournaments of exponentially bounded order

Theorem 5.1 yields a genuine special case of the conjecture.

### Theorem 6.1
Fix \(k\ge2\) and \(A>1\). There exist \(K\) and \(\ell\) such that every tournament \(T\) satisfying
\[
\gamma(T)\ge K
\qquad\text{and}\qquad
|T|\le A^{\gamma(T)}
\]
contains an \(\ell\)-vertex subtournament \(H\) with
\[
\gamma(H)\ge k.
\]

Equivalently, the conjecture holds uniformly on every class of tournaments satisfying
\[
\log |T|=O(\gamma(T)).
\]

### Proof
Put \(r=k-1\). Since \(q_{\ell,r}\to0\) as \(\ell\to\infty\), choose \(\ell>r\) so that
\[
L:=\log(1/q_{\ell,r})>r\log A.
\]
Set
\[
\lambda=\frac{r\log A}{L}<1
\]
and choose
\[
K>
\frac{\ell+r}{1-\lambda}.
\]

Suppose that \(d=\gamma(T)\ge K\), that \(|T|\le A^d\), and that every \(\ell\)-vertex subtournament has domination number at most \(r\). Theorem 5.1 gives
\[
d
\le
r\left\lceil\frac{\log(|T|/\ell)}L\right\rceil+\ell
\le
\frac{r d\log A}{L}+r+\ell
=
\lambda d+r+\ell.
\]
Hence
\[
d\le \frac{r+\ell}{1-\lambda},
\]
contrary to \(d\ge K\). Therefore some \(\ell\)-vertex subtournament has domination number at least \(r+1=k\). \(\square\)

Thus any counterexample sequence must have order growing faster than \(A^{\gamma(T)}\) for every fixed \(A\), after irrelevant vertices have been removed.

---

## 7. A direct sampling result

The common-predecessor lemma also gives a useful quantitative localization statement.

### Proposition 7.1
Let \(T\) have order \(n\) and domination number \(d\). Fix \(r<d\). If \(r<m\le n\) and
\[
\binom mr
\exp\left(
-\frac{2^{d-r-1}(m-r)}{n-r}
\right)<1, \tag{7.1}
\]
then \(T\) has an \(m\)-vertex subtournament of domination number at least \(r+1\).

### Proof
By (2.1), every \(r\)-set \(S\) has at least \(2^{d-r-1}\) common predecessors.

Choose an \(m\)-set \(U\) uniformly at random. Conditional on \(S\subseteq U\), the probability that \(U\setminus S\) avoids \(C_T(S)\) is at most
\[
\exp\left(
-\frac{2^{d-r-1}(m-r)}{n-r}
\right).
\]
Hence the expected number of \(r\)-sets \(S\subseteq U\) with no common predecessor in \(U\) is at most the left side of (7.1). If this is less than one, some \(U\) has no such bad \(r\)-set.

Every \(r\)-set in that \(U\) therefore fails to dominate \(T[U]\). A smaller dominating set could be padded to an \(r\)-set, so
\[
\gamma(T[U])\ge r+1.
\]
\(\square\)

For example, if
\[
|T|\le C\,2^{\gamma(T)}
\]
for fixed \(C\), then the exponent in (7.1) is bounded below by
\[
\frac{m-r}{C2^{r+1}}.
\]
Thus one may choose
\[
m=O\!\left(C2^r r\log(C2^r r)\right),
\]
independent of \(T\).

---

## 8. Critical subtournaments and the remaining obstruction

Given \(K\), an inclusion-minimal induced subtournament \(H\) satisfying
\[
\gamma(H)\ge K
\]
has
\[
\gamma(H)=K.
\]
Indeed, \(\gamma(H-v)\le K-1\) for every \(v\), while a dominating set of \(H-v\), together with \(v\), dominates \(H\).

More precisely:

### Lemma 8.1
If \(H\) is inclusion-minimal with \(\gamma(H)\ge K\), then for every \(v\in V(H)\) there is a set \(D_v\) of size \(K-1\) such that

1. \(D_v\) dominates \(H-v\);
2. \(v\to d\) for every \(d\in D_v\);
3. \(C_H(D_v)=\{v\}\).

### Proof
Minimality gives \(\gamma(H-v)\le K-1\). It cannot be at most \(K-2\), since adjoining \(v\) would then give a dominating set of \(H\) of size at most \(K-1\). Hence \(\gamma(H-v)=K-1\); take \(D_v\) minimum.

If some \(d\in D_v\) satisfied \(d\to v\), then \(D_v\) would dominate all of \(H\), impossible. Thus \(v\to D_v\). Since \(D_v\) dominates every vertex other than \(v\), its only common predecessor is \(v\). \(\square\)

For \(K=3\), every vertex of a domination-critical tournament is therefore the unique common predecessor of some pair.

Theorem 6.1 shows that an unrestricted counterexample cannot have a critical core of order at most \(A^K\) for any fixed \(A\), once the parameters are chosen appropriately. What is missing is any general upper control on the order of such critical cores.

The order restriction cannot simply be imposed on the original tournament. If \(R\) is any tournament and a large transitive block \(B\) is placed below it, with every arc directed from \(R\) to \(B\), then
\[
\gamma(R\to B)=\gamma(R),
\]
while the order can be made arbitrarily large. Passing to an induced critical core removes this trivial inflation, but no adequate bound on critical core size is proved here.

---

## 9. Conclusion and gap

The unrestricted conjecture remains unresolved for \(k\ge3\). The proved partial results are:

1. \(k=1,2\) hold, with \((K,\ell)=(1,1)\) and \((2,3)\).
2. The unique smallest tournament of domination number \(3\) is \(P_7\).
3. If all \(\ell\)-vertex subtournaments have domination number at most \(k-1\), then the whole tournament has domination number
   \[
   O_{k,\ell}(\log |T|),
   \]
   with the explicit bound (5.1).
4. The conjecture holds on every class satisfying
   \[
   \log |T|=O(\gamma(T)).
   \]
5. Any hypothetical counterexample sequence must have domination-critical cores whose orders are superexponential in their domination numbers, in the fixed-base sense described above.

The unresolved point is precisely how to eliminate the residual dependence on \(|T|\) in Theorem 5.1, or else how to construct critical tournaments large enough and locally simple enough to show that such elimination is impossible.