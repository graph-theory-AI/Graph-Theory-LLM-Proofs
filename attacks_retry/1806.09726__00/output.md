```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained argument gives the sharp special-case estimate r̃_rand(5,n) = Θ((n/log n)^(8/3)), but does not resolve the diagonal or large-m asymptotics.",
  "would_publish": false,
  "caveats": "This is consistent with the intended large-m interpretation of part (b); the small-clique query exponent is already known, and no novelty is claimed."
}
```

# A sharp special case and localization of the difficult Painter bias

I follow the quantifier clarification in the supplied referee report: the intended content of part (b) concerns the leading coefficient of the off-diagonal exponent as \(m\) grows. I therefore do **not** regard an exceptional fixed-\(m\) exponent as a disproof.

Here is an unconditional special-case result, including the logarithmic factor.

## Theorem
As \(n\to\infty\),
\[
\boxed{\displaystyle
\widetilde r_{\mathrm{rand}}(5,n)
=\Theta\!\left(\left(\frac{n}{\log n}\right)^{8/3}\right).
}
\]
Moreover, any Painter biases giving a fixed positive fraction of this maximum must satisfy
\[
p=\Theta\!\left(\frac{\log n}{n}\right).
\]

Throughout, \(\log\) is the natural logarithm. I use the probability-\(1/2\) convention: \(\widetilde r(m,n;p)\) is the least deterministic query budget with which Builder can win with probability at least \(1/2\). Expected query counts will only be used to obtain upper bounds by Markov's inequality.

The sparse \(K_5\) query exponent used here is already reported in the supplied source material. Both its upper and lower bounds are proved below, so the argument does not depend on an unverified literature assertion or on another conjecture.

---

## 1. A quantitative lower bound for finding a red \(K_5\)

### Lemma 1
For every adaptive Builder strategy, every \(p\in(0,1)\), and every integer \(T\geq 0\),
\[
\Pr(\text{a red }K_5\text{ is found within }T\text{ queries})
\leq \binom{T}{3}p^8.
\tag{1}
\]

The main point is that this bound permits arbitrary adaptivity.

### An ordering observation

Consider any ordering of the ten edges of a \(K_5\). There are three edges, called **anchors**, such that:

1. their endpoints together comprise all five vertices; and
2. with at most two exceptions, every edge either is an anchor or occurs after both its endpoints have appeared in anchors.

To prove this, distinguish two cases.

**Case 1: the first five edges involve all five vertices.**  
Their graph has five edges and no isolated vertex. It has a matching of size two: a simple graph whose edges are pairwise intersecting is a star or a triangle, and on five vertices such a graph has at most four edges. Take two disjoint edges and add an edge incident to the remaining vertex. These three anchors occur among the first five edges and cover all vertices. Only the other two edges among the first five might be exceptions.

**Case 2: the first five edges omit a vertex.**  
They lie on the other four vertices. The first four edges have a matching of size two, since a four-vertex graph with four edges cannot have all its edges pairwise intersecting. Use these two matching edges as anchors, and use the first edge incident to the fifth vertex as the third anchor. Only the two non-anchor edges among the first four might be exceptions.

This proves the observation.

### Applying the observation to an adaptive strategy

Fix three query indices
\[
J=\{t_1,t_2,t_3\}\subseteq\{1,\ldots,T\}.
\]
As the strategy runs, maintain the set \(S\) of endpoints of anchor queries that have already occurred. Mark a query if:

- its index belongs to \(J\); or
- both its endpoints already belong to \(S\).

At an anchor query, add its endpoints to \(S\).

Whether a query is marked is determined before its color is revealed. Consequently, successive conditioning gives
\[
\Pr(\text{at least eight marked queries occur and the first eight are red})
\leq p^8.
\tag{2}
\]
This remains true if Builder is randomized, by first conditioning on Builder's private randomness.

Now suppose the strategy finds a red \(K_5\). Apply the ordering observation to the order in which its ten edges were queried. For the resulting three anchor indices \(J\), at least eight of those edges are marked. Furthermore, every marked query has both endpoints in this \(K_5\), so every marked query is red.

Thus the event of finding a red \(K_5\) is covered by the events in (2), one for each of the \(\binom{T}{3}\) choices of \(J\). The union bound proves (1). \(\square\)

In particular, finding a red \(K_5\) with constant probability requires
\[
\Omega(p^{-8/3})
\]
queries.

---

## 2. Finding a red \(K_5\) in \(O(p^{-8/3})\) expected queries

### Lemma 2
There is an absolute constant \(C\) such that, for every \(p\in(0,1)\), Builder can find a red \(K_5\) in expected at most
\[
C p^{-8/3}
\tag{3}
\]
queries.

### Construction

Put
\[
a=\lceil p^{-1}\rceil,
\qquad
b=\lceil p^{-5/3}\rceil.
\]

One trial proceeds as follows.

1. Choose a fresh root \(v\), and query edges from \(v\) to fresh vertices until \(a+3b\) red neighbors have been obtained.
2. Partition these neighbors into sets
   \[
   U,\ B_1,\ B_2,\ B_3,
   \qquad |U|=a,\quad |B_i|=b.
   \]
3. Query all edges between \(U\) and \(B_1\cup B_2\cup B_3\).
4. For each \(u\in U\), let
   \[
   B_i(u)=\{x\in B_i:ux\text{ is red}\}.
   \]
   Query every still-unqueried edge between \(B_i(u)\) and \(B_j(u)\), for \(i<j\).

If some \(u\in U\) and \(x_i\in B_i(u)\) have all three edges \(x_ix_j\) red, then
\[
\{v,u,x_1,x_2,x_3\}
\]
is a red \(K_5\).

### Expected cost of a trial

The expected cost of Step 1 is
\[
\frac{a+3b}{p}.
\]
Step 3 uses \(3ab\) queries.

Write \(d_{u,i}=|B_i(u)|\). Step 4 uses at most
\[
\sum_{u\in U}\sum_{i<j}d_{u,i}d_{u,j}
\]
queries, because repeated requests for the same edge need only be queried once. For fixed \(u\), the variables \(d_{u,i}\) are independent \(\operatorname{Bin}(b,p)\) variables. Hence the expected cost of this step is at most
\[
3ab^2p^2.
\]
Using \(a\leq 2p^{-1}\) and \(b\leq 2p^{-5/3}\), the expected total cost is
\[
\frac{a+3b}{p}+3ab+3ab^2p^2
=O(p^{-8/3}).
\tag{4}
\]

### Constant success probability

Conditional on Step 1, all unqueried edges among the selected neighbors remain independent with red probability \(p\).

Let \(X\) count tuples
\[
(u,x_1,x_2,x_3)\in U\times B_1\times B_2\times B_3
\]
for which the six edges on \(\{u,x_1,x_2,x_3\}\) are all red. Then
\[
\mu:=\mathbb E X=ab^3p^6\geq 1.
\]
If \(X>0\), Step 4 necessarily reveals a red \(K_5\).

For two configurations, let \(i\in\{0,1\}\) indicate whether their \(U\)-vertices agree, and let \(j\in\{0,1,2,3\}\) be the number of agreeing \(B\)-coordinates. The number of shared required edges is
\[
ij+\binom j2.
\]
The number of ordered pairs with this overlap pattern is at most
\[
\binom3j a^{2-i}b^{6-j}.
\]
It follows that
\[
\frac{\mathbb E X^2}{\mu^2}
\leq
\sum_{i=0}^1\sum_{j=0}^3
\binom3j a^{-i}b^{-j}p^{-ij-\binom j2}.
\tag{5}
\]
Since \(a\geq p^{-1}\) and \(b\geq p^{-5/3}\), each summand is at most
\[
\binom3j p^{\,i+\frac53j-ij-\binom j2}.
\]
All exponents here are nonnegative:
\[
\begin{array}{c|cccc}
 &j=0&j=1&j=2&j=3\\ \hline
i=0&0&5/3&7/3&2\\
i=1&1&5/3&4/3&0 .
\end{array}
\]
Thus (5) is at most \(16\). By the second-moment inequality,
\[
\Pr(X>0)\geq
\frac{(\mathbb E X)^2}{\mathbb E X^2}
\geq \frac1{16}.
\tag{6}
\]

Repeat trials on disjoint fresh vertex sets. Trials are independent, each has success probability at least \(1/16\), and each has expected cost \(O(p^{-8/3})\). Therefore the expected total cost until success is \(O(p^{-8/3})\). Correlation between a trial's cost and its success does not cause a problem: independence of different trials gives
\[
\mathbb E[\text{total cost}]
=\frac{\mathbb E[\text{cost of one trial}]}{\Pr(\text{one trial succeeds})}.
\]
This proves Lemma 2. \(\square\)

Together, Lemmas 1 and 2 give the constant-probability query estimate
\[
f(K_5,p)=\Theta(p^{-8/3}).
\]

---

## 3. The uniform upper bound for the random Ramsey number

Set
\[
S_n=\left(\frac{n}{\log n}\right)^{8/3},
\qquad
p_0=\frac{\log n}{4n}.
\]

We give an \(O(S_n)\)-query strategy for every \(p\).

### When \(p\geq p_0\)

Use Lemma 2 to find a red \(K_5\). Its expected cost is at most
\[
Cp^{-8/3}
\leq C\left(\frac{4n}{\log n}\right)^{8/3}
=O(S_n).
\tag{7}
\]

### When \(p<p_0\)

Construct a blue clique greedily. Given a blue clique of size \(i\), test fresh candidate vertices one at a time, rejecting a candidate upon the first red edge to the clique. A candidate succeeds with probability \((1-p)^i\), and testing it costs at most \(i\) queries. Hence the expected total cost is at most
\[
\sum_{i=0}^{n-1}i(1-p)^{-i}
\leq \binom n2(1-p)^{-(n-1)}.
\tag{8}
\]
Here \(p<p_0<1/2\), so \(-\log(1-p)\leq 2p\). Consequently,
\[
(1-p)^{-(n-1)}
\leq e^{2pn}
\leq n^{1/2}.
\]
The expected cost in (8) is therefore \(O(n^{5/2})\), and
\[
n^{5/2}
=o\!\left(\left(\frac{n}{\log n}\right)^{8/3}\right).
\tag{9}
\]

Equations (7)–(9) give a uniform \(O(S_n)\) expected winning time. Truncating at twice its upper bound yields success probability at least \(1/2\). Thus
\[
\widetilde r_{\mathrm{rand}}(5,n)=O(S_n).
\tag{10}
\]

---

## 4. A matching lower bound

We first record a useful way to handle adaptively selected vertices.

### Lemma 3
For any strategy making at most \(T\) queries,
\[
\Pr(\text{a blue }K_n\text{ is found})
\leq
\binom{2T}{n}(1-p)^{\binom n2}.
\tag{11}
\]

### Proof

At most \(2T\) vertices occur as query endpoints. Label vertices in order of their first appearance. The complete query process can be simulated using a pre-sampled random coloring of all pairs of \(\{1,\ldots,2T\}\), with independent red probability \(p\).

This simulation has the correct distribution: every previously unqueried pair has an independent color with red probability \(p\), regardless of how Builder chooses it. A blue \(K_n\) in the queried graph is also a blue \(K_n\) in this complete pre-sampled coloring. A union bound over its \(n\)-subsets proves (11). \(\square\)

The relabeling argument is important: one cannot simply assume that an adaptively chosen vertex set is independent of its revealed colors.

Now choose
\[
p=\frac{4\log n}{n},
\qquad
T=\left\lfloor p^{-8/3}\right\rfloor.
\tag{12}
\]
For sufficiently large \(n\), this is an admissible bias.

By Lemma 1, every strategy satisfies
\[
\Pr(\text{red }K_5\text{ by time }T)
\leq \binom T3p^8
\leq \frac{T^3p^8}{6}
\leq \frac16.
\tag{13}
\]

For the blue event, Lemma 3 and \(\binom Mn\leq(eM/n)^n\) give
\[
\begin{aligned}
\log\left[\binom{2T}{n}(1-p)^{\binom n2}\right]
&\leq n\log\frac{2eT}{n}-p\binom n2\\
&\leq n\left(\frac53\log n+\log(2e)\right)
       -2(n-1)\log n\\
&=-\frac13n\log n+O(n+\log n).
\end{aligned}
\]
Thus
\[
\Pr(\text{blue }K_n\text{ by time }T)=o(1).
\tag{14}
\]

Combining (13) and (14),
\[
\Pr(\text{Builder wins by time }T)
\leq \frac16+o(1)<\frac12.
\]
This holds for every adaptive strategy, so
\[
\widetilde r_{\mathrm{rand}}(5,n)
\geq \widetilde r(5,n;p)
>T
=\Omega\!\left(\left(\frac{n}{\log n}\right)^{8/3}\right).
\tag{15}
\]
Together with (10), this proves the theorem.

---

## 5. Where the maximizing bias lies

Fix \(\eta>0\), and suppose a sequence \(p_n\) satisfies
\[
\widetilde r(5,n;p_n)
\geq \eta\,\widetilde r_{\mathrm{rand}}(5,n).
\tag{16}
\]

If \(p_n\leq \log n/(4n)\), the blue strategy above gives complexity
\[
O(n^{5/2})=o(S_n),
\]
contradicting (16) for sufficiently large \(n\). Hence
\[
p_n>\frac{\log n}{4n}
\]
eventually.

On the other hand, the red strategy gives
\[
\widetilde r(5,n;p_n)\leq C p_n^{-8/3}.
\]
Using the theorem and (16),
\[
p_n\leq C_\eta\frac{\log n}{n}.
\]
Therefore every such near-maximizing sequence satisfies
\[
p_n=\Theta_\eta\!\left(\frac{\log n}{n}\right).
\]

---

## 6. What remains unresolved

This calculation does **not** settle either substantive asymptotic assertion in the problem:

- It provides no matching \(2^{(2/3+o(1))n}\) lower bound for the diagonal case.
- It determines one fixed off-diagonal case, but does not establish that the fixed-\(m\) exponents have leading coefficient \(2/3\) as \(m\to\infty\).

The \(K_5\) certificate argument is particularly efficient because three anchor queries suffice while losing at most two of the ten required red edges. No generalization yielding the conjectured large-clique coefficient is proved here.

Thus the result is a rigorous special case, with a matching logarithmic factor and bias localization—not a resolution or disproof of the intended conjecture.