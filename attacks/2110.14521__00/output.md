```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "In the universal certificate model, the clique algorithm is optimal for all n when k=2 and p1=p2, asymptotically optimal for arbitrary binary probabilities, optimal for n at most 4, and optimal within all incremental algorithms.",
  "would_publish": false,
  "caveats": "The exact finite conjecture remains open for n at least 5 and also for unequal binary probabilities."
}
```

# 1. Model and conclusions

I use the source paper’s apparent notion of an AC algorithm: the algorithm must be correct for every set partition, not merely for partitions in the support of \((p_1,\dots,p_k)\). Thus, at termination, positive answers must connect each output block, and every two output blocks must be joined by at least one negative answer. This interpretation is consistent with the stated clique-algorithm asymptotic
\[
\left(\sum_{i=1}^k i p_i\right)n.
\]

Under this interpretation I prove the following partial results.

### Theorem 1
Let \(p_1\ge\cdots\ge p_k\).

1. Among all incremental algorithms—algorithms which completely place one fresh vertex before touching the next—the clique algorithm is exactly optimal for every \(n\).
2. Among all AC algorithms, the clique algorithm is optimal for \(n\le 4\).
3. For \(k=2\), writing \(p_1=p\ge q=p_2\), every AC algorithm \(A\) satisfies
   \[
   \mathbb E Q_A\ge n-2+p^n+q^n+nq-\beta_n,
   \]
   where
   \[
   \beta_n=
   \Pr\!\left(\operatorname{Bin}(n,q)>\frac n2\right)
   +\frac12\Pr\!\left(\operatorname{Bin}(n,q)=\frac n2\right).
   \]
   Consequently, for fixed \(p>q\),
   \[
   \inf_A\mathbb E Q_A=(1+q)n+O_p(1),
   \]
   and the clique algorithm is asymptotically optimal.
4. If \(k=2\) and \(p=q=1/2\), the clique algorithm is exactly optimal for every \(n\), with
   \[
   \min_A\mathbb E Q_A
   =\frac32n-\frac52+2^{1-n}.
   \]

The full finite conjecture remains unresolved.

---

# 2. Certificates and a dynamic-programming formulation

Collapse every connected component of positive answers into one weighted vertex, whose weight is its number of original items. Put an edge between two such vertices when a negative answer between the components is known.

A transcript uniquely certifies a partition exactly when this quotient graph is complete. If its weighted vertices are \(V(G)\), with weights \(w_v\), define
\[
Z(G,w)=
\sum_{\substack{c:V(G)\to[k]\\c\text{ proper}}}
\prod_{v\in V(G)}p_{c(v)}^{w_v}.
\]
This is the probability mass of assignments consistent with the transcript.

For a nonedge \(uv\), a negative answer gives \(G+uv\), while a positive answer contracts \(u,v\) and gives the weight \(w_u+w_v\). If \(L(G,w)\) denotes the minimum unnormalized expected remaining cost, then
\[
L(G,w)
=
Z(G,w)+
\min_{uv\notin E(G)}
\bigl(
L(G+uv,w)+L(G/uv,w')
\bigr),
\]
with \(L(G,w)=0\) when \(G\) is complete or \(Z(G,w)=0\). This recurrence is an exact finite procedure for testing the conjecture; canonical graph isomorphism with vertex weights makes it computationally practical for small \(n\).

---

# 3. Optimality among incremental algorithms

Suppose the already processed vertices form certified blocks of sizes
\[
s_1,\dots,s_r.
\]
If block \(j\) corresponds to latent label \(\ell_j\), then, conditional on this unlabeled partition,
\[
\Pr((\ell_1,\dots,\ell_r))
\propto
\prod_{j=1}^r p_{\ell_j}^{s_j},
\]
where the \(\ell_j\) are distinct.

Let
\[
q_j=\mathbb E[p_{\ell_j}\mid s_1,\dots,s_r]
\]
be the predictive probability that the next vertex belongs to block \(j\).

## Lemma 2
If \(s_a\ge s_b\), then \(q_a\ge q_b\).

### Proof
Pair every injective label assignment with the assignment obtained by exchanging the labels on blocks \(a,b\). Holding all other labels fixed, the contribution to the numerator of \(q_a-q_b\) from labels \(i,j\) is
\[
(p_i-p_j)
\left(
p_i^{s_a}p_j^{s_b}
-
p_j^{s_a}p_i^{s_b}
\right)
\prod_{h\ne a,b}p_{\ell_h}^{s_h}.
\]
This is nonnegative after ordering \(p_i\ge p_j\), because \(s_a\ge s_b\). Summing proves the claim. \(\square\)

An incremental algorithm tests the new item against existing blocks until it obtains a positive answer, or tests all blocks and creates a new singleton. If the test order is \(\sigma\), its expected cost for this item is
\[
r\left(1-\sum_{j=1}^r q_j\right)
+
\sum_{m=1}^r m\,q_{\sigma(m)}.
\]
By the rearrangement inequality this is minimized by decreasing \(q_j\), hence by decreasing block size.

After the item has been completely placed, the resulting block sizes do not depend on the order in which its tests were made. Backward induction on the number of unprocessed items therefore proves exact optimality of the clique rule within the entire incremental class.

This does not settle the conjecture because a general algorithm may compare two unresolved items or maintain several partially processed components.

---

# 4. Exact verification for \(n\le4\)

The cases \(n\le3\) are immediate. For \(n=4\), let
\[
s_j=\sum_i p_i^j
\]
and introduce the probabilities of specified set partitions:
\[
a=s_3-s_4
   =\sum_{i\ne j}p_i^3p_j
   \qquad\text{(a specified \(3+1\) partition),}
\]
\[
b=s_2^2-s_4
   =\sum_{i\ne j}p_i^2p_j^2
   \qquad\text{(a specified \(2+2\) partition),}
\]
and let \(c,d\) be the probabilities of a specified \(2+1+1\) partition and the all-singleton partition, respectively.

The basic moment inequality
\[
a-b=s_3-s_2^2\ge0
\]
follows from Cauchy–Schwarz:
\[
\left(\sum_i p_i^2\right)^2
\le
\left(\sum_i p_i\right)\left(\sum_i p_i^3\right)
=s_3.
\]

By symmetry the first query may be \(12\).

## 4.1. The branch \(1=2\)

Write \(A=\{1,2\}\). The only two essentially different next queries are \(A3\) and \(34\).

If \(A3\) is queried first and, following a negative answer, \(A4\) is queried before \(34\), the conditional expected remaining cost is
\[
2+\Pr(X_3\ne X_A,\ X_4\ne X_A\mid X_1=X_2).
\]

If \(34\) is queried first, the cost is
\[
2+\Pr(X_A\ne X_3,\ X_3\ne X_4\mid X_1=X_2).
\]

Their difference, “fresh–fresh” minus “large block–fresh”, equals
\[
\frac1{s_2}
\sum_{i<j}p_ip_j(p_i-p_j)^2\ge0.
\]
Thus the clique query is optimal on this branch. The same calculation shows that, after learning \(A\ne3\), it is optimal to test vertex \(4\) against the size-two block before the singleton.

## 4.2. The branch \(1\ne2\)

The following finite-state calculation covers all possible continuations. Costs are unnormalized expected remaining path lengths.

Consider first the state \(H\) having negative edges \(12,13\) and isolated vertex \(4\). There are three kinds of next query:

\[
\begin{array}{c|c}
\text{query type}&\text{optimal weighted continuation cost}\\ \hline
23 &2a+3b+12c+4d\\
14 &3a+2b+12c+4d\\
24\text{ or }34&2a+3b+12c+4d
\end{array}
\]

The middle choice exceeds the clique choice by \(a-b\ge0\). The other choice ties it.

For completeness, the subsidiary state consisting of a negative path \(P_4\) has optimal value
\[
2b+7c+3d.
\]
Querying a distance-two nonedge gives this value; querying the two endpoints gives
\[
3b+7c+3d,
\]
so no omitted query is better.

The state consisting of two disjoint negative edges has value
\[
5b+12c+4d.
\]

Returning to the state with only the edge \(12\), querying \(13\) and continuing optimally has value
\[
5a+7b+19c+5d.
\]
Querying the two fresh vertices \(34\) instead gives exactly the same value:
\[
5a+7b+19c+5d.
\]
These are the only two query types up to symmetry. Hence the clique continuation is optimal after \(1\ne2\).

Combining the two first-query branches proves the conjecture for \(n=4\). The argument permits zero values among \(a,b,c,d\), so it covers every \(k\) and every probability vector.

---

# 5. The binary case

Let \(k=2\), with probabilities \(p\ge q\).

## 5.1. A potential for negative answers

On an input from the binary support, consider the graph of all queries made so far, retaining both positive and negative signs. In each connected component, binary labels are determined up to a global flip. Let the two parity sides of such a component have total sizes \(a,b\). Their two possible absolute orientations have likelihoods
\[
p^a q^b,\qquad p^b q^a.
\]
Define its orientation error
\[
\epsilon(a,b)=
\frac{\min(p^a q^b,p^b q^a)}
     {p^a q^b+p^b q^a}
\le\frac12.
\]
Let
\[
\Phi=\sum_C\epsilon(C),
\]
the sum over connected queried components.

Initially there are \(n\) isolated vertices, each with error \(q\), so
\[
\Phi_0=nq.
\]

Suppose a query joins two previously disconnected queried components having orientation errors \(\alpha,\beta\le1/2\). Their orientation bits are conditionally independent. Assume \(\alpha\le\beta\). If the queried parity sides have the same canonical predicted label, the probability of a negative answer is
\[
D=\alpha+\beta-2\alpha\beta.
\]
Choosing opposite canonical sides only replaces \(D\) by \(1-D\ge D\).

After the answer is observed, the expected orientation error of the merged component is
\[
\alpha\beta+\min\{\alpha(1-\beta),(1-\alpha)\beta\}
=\alpha.
\]
Consequently,
\[
\mathbb E\bigl[\mathbf 1_{\{\text{negative}\}}
+\epsilon_{\rm merged}\bigr]
\ge D+\alpha
=\alpha+\beta+\alpha(1-2\beta)
\ge\alpha+\beta.
\]
Queries internal to one connected queried component do not decrease \(\Phi\). Therefore
\[
N_-+\Phi
\]
is a submartingale, where \(N_-\) is the number of negative answers.

At termination the queried graph is connected: for one output block its positive graph is connected, while for two output blocks their positive graphs are connected and at least one negative edge joins them. Hence
\[
\mathbb E N_-\ge nq-\mathbb E\Phi_{\rm final}.
\]

The final orientation uncertainty depends only on the unlabeled binary partition. If \(B\sim\operatorname{Bin}(n,q)\), its expected Bayes error is
\[
\mathbb E\Phi_{\rm final}
=
\beta_n
=
\Pr(B>n/2)+\frac12\Pr(B=n/2).
\]
Thus
\[
\mathbb E N_-\ge nq-\beta_n.
\]

## 5.2. Positive answers

If both classes occur, each of the two blocks needs a positive spanning tree, requiring \(n-2\) positive answers. If only one class occurs, \(n-1\) are required. Hence every AC algorithm has
\[
\mathbb E N_+
\ge n-2+p^n+q^n.
\]
Combining the two estimates gives
\[
\boxed{
\mathbb E Q_A
\ge
n-2+p^n+q^n+nq-\beta_n.
}
\]

## 5.3. Consequences

If \(p>q\), then \(\beta_n\) decays exponentially. The binary clique algorithm tests each new vertex first against the currently larger observed block. Apart from a summable probability that this empirical majority is the \(q\)-class, a negative first answer occurs with probability \(q\). More precisely,
\[
\mathbb E N_-^{\rm clique}
\le q(n-1)
+(p-q)\sum_{m\ge1}
\Pr\!\left(\operatorname{Bin}(m,q)\ge \frac m2\right),
\]
and the series is finite. Therefore
\[
\mathbb E Q_{\rm clique}=(1+q)n+O_p(1).
\]
Together with the lower bound,
\[
\inf_A\mathbb E Q_A=(1+q)n+O_p(1).
\]

If \(p=q=1/2\), then every connected queried component has orientation error \(1/2\), so the potential inequality is exact. Moreover, every first comparison made by the clique algorithm fails with probability \(1/2\), giving
\[
\mathbb E N_-^{\rm clique}=\frac{n-1}{2}.
\]
Since
\[
\mathbb E N_+^{\rm clique}=n-2+2^{1-n},
\]
we obtain
\[
\boxed{
\min_A\mathbb E Q_A
=
\frac32n-\frac52+2^{1-n}.
}
\]
Thus the full finite conjecture holds for the symmetric binary distribution.

---

# 6. Important interpretation caveat

If algorithms are only required to be correct on the support of the \(k\)-class distribution, then the conjecture as extracted is false.

For example, let \(k=2\) and \(p_1,p_2>0\). Query every vertex against vertex \(1\). This uses exactly \(n-1\) queries. All vertices receiving a positive answer form one block; all vertices receiving a negative answer must form the other block because at most two classes are allowed. By contrast, the source’s clique-algorithm asymptotic is
\[
(p_1+2p_2)n=(1+p_2)n.
\]
Thus the universal-certificate requirement is essential.

---

# 7. Remaining gap

The unresolved step is to exclude algorithms that maintain several partially resolved components and compare them with one another. The incremental exchange argument does not address such policies. In the binary case the potential above determines the leading term but leaves a bounded “potential drift”; I do not have a proof that the clique algorithm minimizes that drift for unequal \(p,q\). For \(k\ge3\), even a connected signed query graph does not determine labels up to one global permutation, so the binary orientation potential has no immediate analogue.