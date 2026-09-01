```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A deterministic p-exchange local search gives an O(OPT^{1-1/p}) approximation on induced K_{p,q}-free graphs for p≤q, yielding the conjectured property with every ε<1/p, but it does not extend to arbitrary H.",
  "would_publish": false,
  "caveats": "Complete bipartite H are already covered abstractly by substitution, and this asymmetric quantitative extension may be implicit in the source; general prime forbidden graphs remain untouched."
}
```

# Mathematical writeup

## 1. Statement and outcome

Throughout, \(H\)-free means induced-\(H\)-free. Write \(\alpha(G)\) for the maximum independent-set size.

The full conjecture asks whether, for every fixed graph \(H\), there is an \(\varepsilon>0\) and a polynomial-time algorithm returning an independent set \(I\) in every \(H\)-free \(n\)-vertex graph \(G\) such that
\[
|I|\ge \frac{\alpha(G)}{n^{1-\varepsilon}}.
\]

I do not prove this in general. The following gives a direct deterministic result, with an explicit exponent, for asymmetric complete bipartite forbidden induced subgraphs.

## 2. Asymmetric induced-biclique theorem

### Theorem

Fix integers \(1\le p\le q\). There is a deterministic polynomial-time algorithm which, on every induced-\(K_{p,q}\)-free graph \(G\), returns an independent set \(I\) satisfying
\[
\alpha(G)
 \le |I|+\sum_{i=1}^{p-1}i\binom{|I|}{i}
       +(q-1)\binom{|I|}{p}.
\tag{1}
\]
Consequently, with
\[
C_{p,q}=q+\frac{p(p-1)}2,
\]
the output satisfies
\[
|I|\ge \left(\frac{\alpha(G)}{C_{p,q}}\right)^{1/p},
\]
and hence has approximation ratio at most
\[
C_{p,q}^{1/p}\alpha(G)^{1-1/p}
 \le C_{p,q}^{1/p}n^{1-1/p}.
\tag{2}
\]

In particular, induced-\(K_{p,q}\)-free graphs satisfy the improved approximation property for every fixed
\[
0<\varepsilon<\frac1p.
\]
For example, one may take \(\varepsilon=1/(2p)\).

### Algorithm

Maintain an independent set \(I\), initially empty. As long as there is an independent set
\[
X\subseteq V(G)\setminus I,\qquad 1\le |X|\le p,
\]
such that
\[
|N_G(X)\cap I|<|X|,
\]
replace
\[
I\leftarrow \bigl(I\setminus N_G(X)\bigr)\cup X.
\]

The new set is independent, and its cardinality strictly increases. Thus there are at most \(n\) iterations. Since \(p\) is fixed, all candidate sets \(X\) can be enumerated in \(O(n^p)\) time per scan; a naive implementation is polynomial, for example \(O(n^{p+2})\).

At termination we have the local optimality condition
\[
|N_G(X)\cap I|\ge |X|
\tag{3}
\]
for every independent \(X\subseteq V(G)\setminus I\) of size at most \(p\).

## 3. Proof of the bound

Let \(S\) be a maximum independent set, let
\[
a=|I|,\qquad Y=S\setminus I.
\]
Because \(Y\) is independent, condition (3) applies to every subset of \(Y\) of size at most \(p\).

Partition \(Y\) according to its degree into \(I\).

### Vertices with fewer than \(p\) neighbors in \(I\)

For \(Z\subseteq I\), define
\[
Y_Z=\{y\in Y:N_G(y)\cap I=Z\}.
\]
Suppose \(|Z|=i<p\). If \(|Y_Z|\ge i+1\), choose \(X\subseteq Y_Z\) of size \(i+1\). Then
\[
|X|=i+1\le p,\qquad N_G(X)\cap I=Z,
\]
and therefore
\[
|N_G(X)\cap I|=i< i+1=|X|,
\]
contradicting (3). Hence
\[
|Y_Z|\le |Z|.
\]
It follows that
\[
|\{y\in Y:|N_G(y)\cap I|<p\}|
 \le \sum_{i=1}^{p-1}i\binom ai.
\tag{4}
\]

### Vertices with at least \(p\) neighbors in \(I\)

For every \(p\)-set \(P\subseteq I\), there are at most \(q-1\) vertices of \(Y\) adjacent to every vertex of \(P\). Indeed, \(q\) such vertices, together with \(P\), would induce a \(K_{p,q}\): both \(I\) and \(Y\) are independent, and all cross edges between the selected sets would be present.

Double-count pairs \((P,y)\) where \(y\in Y\), \(P\subseteq N_G(y)\cap I\), and \(|P|=p\). This gives
\[
\sum_{\substack{y\in Y\\ |N_G(y)\cap I|\ge p}}
 \binom{|N_G(y)\cap I|}{p}
 \le (q-1)\binom ap.
\]
Every summand on the left is at least one, so
\[
|\{y\in Y:|N_G(y)\cap I|\ge p\}|
 \le (q-1)\binom ap.
\tag{5}
\]

Combining (4) and (5), and using \(|S\cap I|\le a\), yields (1):
\[
\alpha(G)=|S\cap I|+|Y|
 \le a+\sum_{i=1}^{p-1}i\binom ai+(q-1)\binom ap.
\]

For \(a\ge1\), each \(\binom ai\le a^i\le a^p\), and therefore
\[
\alpha(G)
 \le \left(1+\sum_{i=1}^{p-1}i+q-1\right)a^p
 =\left(q+\frac{p(p-1)}2\right)a^p.
\]
This proves (2).

## 4. Obtaining a literal \(n^{1-\varepsilon}\) factor

Equation (2) has a constant factor \(C_{p,q}^{1/p}\). Fix any \(\varepsilon<1/p\), and set
\[
N_0=\left\lceil C_{p,q}^{\,1/(1-p\varepsilon)}\right\rceil.
\]
For \(n\ge N_0\),
\[
C_{p,q}^{1/p}n^{1-1/p}\le n^{1-\varepsilon}.
\]
For \(n<N_0\), compute MIS exactly by exhaustive search. Since \(N_0\) depends only on the fixed forbidden graph, this branch contributes only a fixed constant to the running time. Thus the resulting algorithm is a literal \(n^{1-\varepsilon}\)-approximation.

Taking \(\varepsilon=1/(2p)\), it suffices to use the threshold \(N_0=\lceil C_{p,q}^2\rceil\).

The algorithm is deterministic; randomization is unnecessary.

## 5. Sharpness for this local-search analysis

The exponent \(1/p\) cannot be improved for arbitrary \(p\)-local optima by a stronger analysis of the same local condition.

Fix \(a\ge p\) and \(q\ge2\). Let \(A\) be an independent set of size \(a\). For every \(p\)-subset \(P\subseteq A\), introduce \(q-1\) independent vertices whose neighborhood is exactly \(P\). Let \(Y\) be the set of all introduced vertices, with no edges inside \(Y\).

This graph is induced-\(K_{p,q}\)-free:

- A fixed \(p\)-set in \(A\) has only \(q-1\) common neighbors in \(Y\).
- In the reverse orientation, if \(q>p\), every vertex of \(Y\) has degree only \(p<q\). If \(q=p\), \(p\) vertices of \(Y\) can have \(p\) common neighbors only if all have the same neighborhood, but there are only \(p-1\) copies of each neighborhood.

The independent set \(I=A\) is \(p\)-locally optimal: every nonempty \(X\subseteq Y\) with \(|X|\le p\) has
\[
|N_G(X)\cap A|\ge p\ge |X|.
\]
On the other hand,
\[
|Y|=(q-1)\binom ap=\Theta(a^p),
\]
so \(\alpha(G)\ge |Y|=\Theta(|I|^p)\). Thus a \(p\)-local optimum can have approximation ratio of order
\[
\alpha(G)^{1-1/p}.
\]

## 6. Why this does not approach arbitrary \(H\)

The proof depends on one very specific fact: for two independent sets \(I\) and \(S\), induced-\(K_{p,q}\)-freeness bounds the number of vertices of \(S\) having any prescribed \(p\)-set of common neighbors in \(I\). An arbitrary forbidden graph gives no analogous bound.

Indeed, fixed-radius exchange local search can be arbitrarily bad for almost every other forbidden graph. Let \(\ell\ge1\), and suppose \(H\) is not an induced subgraph of any complete bipartite graph. Take
\[
G=K_{\ell,N}
\]
with sides \(A,B\), where \(|A|=\ell\) and \(|B|=N\). Every induced subgraph of \(G\) is either edgeless or complete bipartite, so \(G\) is \(H\)-free. Nevertheless \(I=A\) is an \(\ell\)-local optimum: for every nonempty \(X\subseteq B\) with \(|X|\le\ell\),
\[
N_G(X)\cap I=A,\qquad |N_G(X)\cap I|=\ell\ge |X|.
\]
But
\[
\frac{\alpha(G)}{|I|}=\frac N\ell
\]
is unbounded.

This does not disprove the conjecture—one can plainly find the larger side of a complete bipartite graph. It shows only that an argument asserting that all bounded-radius exchange optima are good cannot handle general \(H\).

## 7. Relation to the source and remaining gap

For \(p=q=t\), the theorem recovers the \(OPT^{1-1/t}\) local-search bound mentioned in the source abstract. For \(p<q\), applying only the symmetric \(K_{t,t}\) statement with \(t=q\) gives an exponent governed by \(q\), whereas the direct asymmetric count is governed by the smaller side \(p\).

At the qualitative level, \(K_{p,q}\) is obtained from \(K_2\) by substituting independent sets, so this family was already covered by the source paper’s substitution closure. Thus the result is quantitative rather than a resolution for a genuinely new prime forbidden graph. The missing case remains arbitrary \(H\), particularly prime graphs for which no common-neighborhood counting statement like (5) is available.