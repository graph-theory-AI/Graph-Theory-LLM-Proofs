```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "A clean switching obstruction proves radius-2 nonreconstructibility throughout log(n)/n << p << n^{-3/4}(log n)^{1/4}, but does not establish the high-density reconstruction half.",
  "would_publish": false,
  "caveats": "This assumes rooted induced balls; only lower bounds are proved, and overlap with the full arXiv v3 lower-bound argument has not been checked line by line."
}
```

# Mathematical writeup

## 1. Interpretation and partial result

For a graph \(G\) and \(v\in V(G)\), write
\[
B_r^G(v)=G[\{x:\operatorname{dist}_G(v,x)\le r\}],
\]
rooted at \(v\). The radius-\(r\) deck is the multiset of rooted isomorphism classes of the \(B_r^G(v)\). A graph is \(r\)-reconstructible if no nonisomorphic graph has the same radius-\(r\) deck.

The extracted conjecture is informal because it does not specify \(t(n)\), but the intended open cases are \(r=1,2\). The following gives a self-contained lower bound for \(r=2\).

### Theorem 1: a radius-two nonreconstruction regime

Let \(G\sim G(n,p)\), and put
\[
d=np,\qquad \theta=n^3p^4=\frac{d^4}{n}.
\]
Suppose
\[
\frac{d}{\log n}\longrightarrow\infty
\qquad\text{and}\qquad
n^2d\,e^{-6\theta}\longrightarrow\infty.
\tag{1}
\]
Then, with high probability, \(G\) is not reconstructible from its rooted radius-two neighborhoods.

In particular,
\[
\frac{\log n}{n}\ll p\ll n^{-3/4}(\log n)^{1/4}
\tag{2}
\]
implies nonreconstructibility with high probability.

More quantitatively, if
\[
p=n^{-3/4}f,\qquad f\ge 1,\qquad
f^4\le \left(\frac38-\varepsilon\right)\log n
\]
for fixed \(\varepsilon>0\), then \(G\) is not radius-two reconstructible with high probability.

Thus, in the literal \(\omega/o\) formulation, \(t_2(n)=n^{-3/4}\) cannot be the second threshold: for example,
\[
p=n^{-3/4}(\log n)^{1/8}
\]
is \(\omega(n^{-3/4})\), but Theorem 1 still gives nonreconstructibility. The result is consistent with a threshold of order
\[
n^{-3/4}(\log n)^{1/4}.
\]

The proof uses a two-edge switch whose radius-two neighborhoods are unchanged.

---

## 2. A deterministic radius-two switch

### Lemma 2

Let \(H\) be a graph containing distinct vertices \(a,b,c,d\) such that

1. every two of \(a,b,c,d\) have \(H\)-distance greater than \(4\);
2. the rooted graphs satisfy
   \[
   B_1^H(a)\cong B_1^H(d),
   \qquad
   B_1^H(b)\cong B_1^H(c).
   \tag{3}
   \]

Define
\[
G=H+\{ab,cd\},
\qquad
G'=H+\{ac,bd\}.
\]
Then \(G\) and \(G'\) have identical rooted radius-two decks. Indeed,
\[
B_2^G(x)\cong B_2^{G'}(x)
\]
for every \(x\in V(H)\).

#### Proof

Because the four marked vertices are pairwise at distance greater than \(4\) in \(H\), their radius-two \(H\)-balls are pairwise disjoint.

Consider first the card rooted at \(a\). In \(G\), adding \(ab\) attaches to \(a\) a copy of the rooted graph \(B_1^H(b)\): the vertices of \(N_H[b]\) all lie within distance two of \(a\). There are no additional edges between \(B_1^H(b)\) and \(B_2^H(a)\), since such an edge would produce an \(H\)-path of length at most \(4\) from \(a\) to \(b\). Thus
\[
B_2^G(a)
\]
is obtained from \(B_2^H(a)\) by attaching \(B_1^H(b)\) at its root \(b\) through the edge \(ab\).

Similarly, \(B_2^{G'}(a)\) is obtained by attaching \(B_1^H(c)\) through \(ac\). The second isomorphism in (3) therefore gives
\[
B_2^G(a)\cong B_2^{G'}(a).
\]
The cards rooted at \(b,c,d\) are handled in the same way, using respectively the two isomorphisms in (3).

Now suppose \(x\notin\{a,b,c,d\}\).

- If \(x\) is an \(H\)-neighbor of exactly one marked vertex, say \(a\), then in \(B_2^G(x)\) the added edge \(ab\) contributes only the boundary vertex \(b\), as a pendant vertex adjacent to \(a\). In \(B_2^{G'}(x)\), it contributes instead the boundary vertex \(c\). Pairwise distance greater than \(4\) guarantees that neither boundary vertex has any other edge inside the card. Hence the two rooted cards are isomorphic.
- If \(x\) has \(H\)-distance exactly \(2\) from a marked vertex, traversing an added edge would require a third step, so neither added matching changes its radius-two ball.
- If \(x\) is farther than \(2\) from all four marked vertices, neither matching affects its radius-two ball.

Because no vertex can be within distance two of two different marked vertices, these cases exhaust all \(x\). ∎

For the random-graph application, we shall choose the four rooted \(1\)-balls to be stars. Then (3) reduces to two degree equalities.

---

## 3. Random occurrence of the switch

Let \(\mathcal F\) be the set of ordered quadruples
\[
Q=(a,b,c,d)
\]
of distinct vertices. Call \(Q\) good if the following hold.

1. The graph induced by \(\{a,b,c,d\}\) has exactly the two edges
   \[
   ab,\quad cd.
   \tag{4}
   \]
2. In
   \[
   H_Q=G-\{ab,cd\},
   \]
   all six pairs among \(a,b,c,d\) have distance greater than \(4\).
3. For each \(u\in\{a,b,c,d\}\), the graph induced by \(N_{H_Q}(u)\) is edgeless.
4. The degrees in \(H_Q\) satisfy
   \[
   \deg_{H_Q}(a)=\deg_{H_Q}(d),
   \qquad
   \deg_{H_Q}(b)=\deg_{H_Q}(c).
   \tag{5}
   \]

Conditions 3 and 4 imply
\[
B_1^{H_Q}(a)\cong B_1^{H_Q}(d),
\qquad
B_1^{H_Q}(b)\cong B_1^{H_Q}(c),
\]
because all four rooted \(1\)-balls are stars. Thus every good quadruple gives the switch of Lemma 2.

We prove that a good quadruple exists with high probability.

### 3.1 Preliminary estimates

Under (1),
\[
e^{6\theta}=o(n^2d).
\]
Consequently \(\theta=O(\log n)\), and since \(\theta=d^4/n\),
\[
d=O\bigl((n\log n)^{1/4}\bigr).
\tag{6}
\]
In particular,
\[
p=o(1),\qquad
\frac{d^2}{n}=o(1),\qquad
\frac{d^3}{n}=o(1).
\tag{7}
\]

Fix \(Q=(a,b,c,d)\), and condition on (4). In \(H_Q\), the four external degrees are independent copies of
\[
D\sim \operatorname{Bin}(n-4,p).
\]
The elementary local central limit theorem gives, for independent copies \(D_1,D_2\),
\[
\Pr(D_1=D_2)
 =\sum_k\Pr(D=k)^2
 \sim \frac{1}{2\sqrt{\pi d}}.
\]
Hence
\[
\Pr(D_a=D_d,\ D_b=D_c)
 \sim \frac{1}{4\pi d}.
\tag{8}
\]

Conditional on typical values
\[
D_u=d+O(\sqrt d\log n),
\tag{9}
\]
the external neighbor sets are independent uniform subsets of the appropriate sizes.

The probability that two of the four neighbor sets intersect is
\[
O\left(\frac{d^2}{n}\right)=o(1).
\tag{10}
\]
Conditional on their being disjoint, the expected number of edges between two different marked neighbor sets is \(d^2p=d^3/n=o(1)\). Thus paths of lengths two and three between marked vertices can be excluded at multiplicative cost \(1-o(1)\).

The principal constraint is the absence of paths of length four. For a marked pair \(u,v\), such a path has the form
\[
u-x-y-z-v,
\qquad
x\in N_{H_Q}(u),\quad z\in N_{H_Q}(v).
\]
Restrict initially to middle vertices \(y\) outside all four marked neighbor sets. Over all six marked pairs, the number of potential triples \((x,y,z)\) is
\[
(6+o(1))d^2n.
\]
Each requires two independent edges and hence has probability \(p^2\). Its total mean is therefore
\[
(6+o(1))d^2np^2=6\theta+o(1).
\tag{11}
\]

Two such path events are dependent only if they share one of their two random edges. Each path event has \(O(d)\) possible partners sharing an edge, so the Janson dependency sum is
\[
O(d^2n\cdot d\cdot p^3)
 =O\left(\frac{d^6}{n^2}\right)
 =o(1)
\tag{12}
\]
by (6).

Janson's upper bound and Harris's inequality give matching estimates:
\[
\Pr(\text{no such length-four path})
   =\exp(-6\theta+o(1)).
\tag{13}
\]
Indeed, the Harris lower bound is
\[
(1-p^2)^{(6+o(1))d^2n}
 =\exp(-6\theta+o(1)).
\]
Length-four paths whose middle vertex lies in one of the marked neighbor sets have expected number
\[
O(d^3p^2)=O\left(\frac{d^5}{n^2}\right)=o(1).
\]
Their absence, and the absence of edges within any marked neighbor set, are decreasing events of probability \(1-o(1)\). Harris's inequality therefore shows that adding these conditions changes (13) only by a factor \(1-o(1)\).

The estimates are uniform for degree values satisfying (9). Atypical degree values have probability \(\exp[-\Omega(\log^2 n)]\), negligible relative to all the polynomially small probabilities above.

It follows that, for a fixed ordered quadruple,
\[
\Pr(Q\text{ is good})
 =\left(\frac{1}{4\pi}+o(1)\right)
   \frac{p^2}{d}\,e^{-6\theta}.
\tag{14}
\]

Let \(X\) be the number of good ordered quadruples. Then
\[
\mathbb E X
 =\left(\frac{1}{4\pi}+o(1)\right)
   n^4\frac{p^2}{d}e^{-6\theta}
 =\left(\frac{1}{4\pi}+o(1)\right)
   n^2d\,e^{-6\theta},
\tag{15}
\]
which tends to infinity by assumption.

### 3.2 Second moment

It remains to rule out excessive dependence between candidate quadruples.

Take two ordered quadruples \(Q,R\), and let
\[
k=|V(Q)\cap V(R)|.
\]
For \(k=0\), the same marked-vertex exposure as above, now with eight marked vertices, gives
\[
\Pr(Q,R\text{ both good})
 =(1+o(1))\Pr(Q\text{ good})\Pr(R\text{ good}).
\tag{16}
\]
The length-four path family has mean \(12\theta+o(1)\), and the cross-dependency contribution is still \(o(1)\).

For \(k\ge1\), we only need upper bounds. If the two internal matching prescriptions are compatible, let:

- \(m_k\) be a lower bound on the number of distinct prescribed present edges;
- \(r_k\) be a lower bound on the rank of the combined affine degree-equality system;
- \(L_k\) be the number of distinct marked pairs required to have no external path of length four.

The relevant worst-case bounds are
\[
\begin{array}{c|c|c|c}
k&m_k&r_k&L_k\\ \hline
1&4&4&12\\
2&3&3&11\\
3&3&3&9\\
4&2&2&6
\end{array}
\tag{17}
\]
because two four-sets sharing \(k\) vertices share exactly \(\binom{k}{2}\) unordered pairs.

The same exposure argument gives
\[
\Pr(Q,R\text{ both good})
 \le C\,p^{m_k}d^{-r_k/2}e^{-L_k\theta+o(1)}.
\tag{18}
\]
There are \(O(n^{8-k})\) ordered pairs with overlap \(k\). After normalizing by \((\mathbb EX)^2\), their total contributions are bounded respectively by
\[
\begin{array}{c|c}
k&\text{normalized contribution}\\ \hline
1&O(n^{-1})\\[2mm]
2&O\!\left(n^{-1}d^{-1/2}e^\theta\right)\\[2mm]
3&O\!\left(n^{-2}d^{-1/2}e^{3\theta}\right)\\[2mm]
4&O\!\left(n^{-2}d^{-1}e^{6\theta}\right).
\end{array}
\tag{19}
\]

Set
\[
A_n=\frac{e^{6\theta}}{n^2d}.
\]
By (1), \(A_n\to0\). The last three nontrivial quantities in (19) satisfy
\[
n^{-1}d^{-1/2}e^\theta
 =A_n^{1/6}n^{-2/3}d^{-1/3}=o(1),
\]
\[
n^{-2}d^{-1/2}e^{3\theta}
 =A_n^{1/2}n^{-1}=o(1),
\]
and
\[
n^{-2}d^{-1}e^{6\theta}=A_n=o(1).
\]
Together with (16), this proves
\[
\mathbb E X^2=(1+o(1))(\mathbb E X)^2.
\]
Therefore \(X>0\) with high probability.

---

## 4. The switched graph is nonisomorphic

Producing the same deck is insufficient if the switched graph happens to be isomorphic to the original graph. We use a simple edit-rigidity property of \(G(n,p)\).

### Lemma 3: four-edge edit rigidity

Suppose
\[
np/\log n\longrightarrow\infty
\quad\text{and}\quad p\le \tfrac12.
\]
Then, with high probability, every nonidentity permutation \(\pi\) of \(V(G)\) satisfies
\[
|E(G)\triangle E(\pi G)|>4.
\tag{20}
\]

#### Proof

Let \(\pi\) have support of size \(k\ge2\). The induced permutation on the \(\binom n2\) unordered vertex pairs moves at least
\[
k\left(n-\frac{k}{2}-1\right)\ge \frac{kn}{3}
\]
coordinates for large \(n\). From the cycles of this coordinate permutation, choose at least \(kn/9\) disjoint pairs of coordinates of the form
\[
\{e,\pi(e)\}.
\]
The corresponding edge indicators are independent in these selected pairs.

For a selected pair, the probability of a mismatch is
\[
2p(1-p)\ge p.
\]
If (20) fails, at most four of the selected pairs can mismatch. Thus, for fixed \(\pi\),
\[
\Pr\bigl(|E(G)\triangle E(\pi G)|\le4\bigr)
 \le n^8\exp(-c k np)
\]
for an absolute constant \(c>0\). There are at most \(n^k\) permutations with support \(k\), and therefore
\[
\Pr(\exists \pi\ne\mathrm{id}\text{ violating (20)})
 \le n^8\sum_{k=2}^n
       \exp(k\log n-c k np)
 =o(1).
\]
∎

Take a good quadruple and form
\[
G'=G-\{ab,cd\}+\{ac,bd\}.
\]
Lemma 2 gives equality of radius-two decks. Moreover,
\[
|E(G)\triangle E(G')|=4.
\]
If \(G'\cong G\), then \(G'=\pi G\) for some permutation \(\pi\). The identity permutation is impossible because \(G'\ne G\), while every nonidentity permutation is excluded by Lemma 3. Hence \(G'\not\cong G\).

This completes the proof of Theorem 1.

---

## 5. Radius one: an analogous explicit obstruction

The same switching idea gives a clean lower bound in the other unresolved radius.

### Proposition 4

Let \(G\sim G(n,p)\), put
\[
d=np,\qquad \lambda=np^2,
\]
and suppose
\[
\frac d{\log n}\longrightarrow\infty,
\qquad
n^4p^2e^{-4\lambda}\longrightarrow\infty.
\tag{21}
\]
Then \(G\) is not reconstructible from its rooted radius-one neighborhoods with high probability.

In particular, for every fixed \(\varepsilon>0\),
\[
1\le np^2\le
\left(\frac34-\varepsilon\right)\log n
\tag{22}
\]
implies nonreconstructibility with high probability.

#### Proof

For distinct \(a,b,c,d\), require:

1. \(G[\{a,b,c,d\}]\) has exactly the edges \(ab,cd\);
2. none of the four pairs
   \[
   ab,\ ac,\ cd,\ bd
   \tag{23}
   \]
   has a common neighbor outside \(\{a,b,c,d\}\).

Switch \(ab,cd\) to \(ac,bd\).

For each endpoint card, the removed neighbor is an isolated vertex in the graph induced by the root's neighbors, and the added neighbor is also isolated there. Thus each endpoint's rooted \(1\)-ball remains isomorphic.

For any other root \(x\), its neighbor set is unchanged. Its induced rooted card could change only if \(x\) were adjacent to both endpoints of one of the four changed pairs in (23), which is excluded. Hence all rooted radius-one cards are unchanged.

For a fixed ordered quadruple, an outside vertex may meet the marked four vertices only in an independent set of the cycle with edge set (23). The corresponding probability is
\[
q=(1-p)^4+4p(1-p)^3+2p^2(1-p)^2
  =1-4p^2+4p^3-p^4.
\]
Thus the probability of a clean quadruple is
\[
p^2(1-p)^4q^{n-4}
 =(1+o(1))p^2e^{-4np^2}.
\tag{24}
\]
The expected number is consequently
\[
(1+o(1))n^4p^2e^{-4\lambda},
\]
which tends to infinity by (21).

A second-moment calculation is similar to the one above. Two cycle constraints whose marked four-sets overlap in \(k\) vertices can share at most \(0,1,2,4\) constrained pairs for \(k=1,2,3,4\), respectively. Relative to the square of the first moment, the overlap contributions are bounded by
\[
O(n^{-1}),\quad
O(n^{-2}p^{-1}e^\lambda),\quad
O(n^{-3}p^{-1}e^{2\lambda}),\quad
O(n^{-4}p^{-2}e^{4\lambda}).
\]
Writing
\[
A_n=\frac{e^{4\lambda}}{n^4p^2}=o(1),
\]
these are, respectively,
\[
O(n^{-1}),\quad
O\left(\frac{A_n^{1/4}}{\sqrt{nd}}\right),\quad
O\left(\frac{A_n^{1/2}}n\right),\quad
O(A_n),
\]
and hence all tend to zero. A clean switch therefore exists with high probability. Lemma 3 again ensures that the switched graph is nonisomorphic.

For (22), write \(p^2=\lambda/n\). Then
\[
n^4p^2e^{-4\lambda}=n^3\lambda e^{-4\lambda}
 \ge n^{4\varepsilon+o(1)},
\]
at the upper endpoint, while \(d=\sqrt{n\lambda}\gg\log n\). ∎

This rules out a pure \(n^{-1/2}\) threshold in the literal \(\omega/o\) sense: there are values \(p=\Theta(\sqrt{\log n/n})=\omega(n^{-1/2})\) for which nonreconstructibility still holds.

---

## 6. What remains open

The argument proves only the nonreconstructibility side.

- For \(r=2\), it gives a robust obstruction up to the scale
  \[
  n^{-3/4}(\log n)^{1/4},
  \]
  including values \(p=\omega(n^{-3/4})\).
- For \(r=1\), it gives a clean obstruction at scale
  \[
  \sqrt{\frac{\log n}{n}}.
  \]

No reconstruction algorithm or uniqueness theorem is proved above those scales. In particular, absence of these clean switches does not imply reconstructibility; more complicated switches may remain. Therefore the proposed second phase transitions for \(r=1,2\) are not resolved.

I also have not verified whether these precise clean-switch estimates, especially the logarithmic \(r=2\) formulation, are already contained implicitly in the source paper's lower-bound machinery. Hence I do not claim novelty.