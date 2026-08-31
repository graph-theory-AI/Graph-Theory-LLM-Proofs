```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for s=1 and for s=2 in every uniformity, while for s>=3 there is a universal stretched-exponential lower bound and an exp(Omega(n^{s-1})) bound for a structural subclass.",
  "would_publish": false,
  "caveats": "The required tower height remains open for s>=3, and I have not checked whether the s=2 construction already appears elsewhere."
}
```

# 1. Results

All hypergraphs are simple. For a \(k\)-graph \(G\), write \(\alpha(G)\) for its independence number. Two edges are \(s\)-adjacent if they intersect in at least \(s\) vertices; the \(s\)-tight components are the components of this edge-adjacency graph.

The main partial result is the following.

### Theorem 1
Fix \(2\le s<k\), and put
\[
b=\binom{k}{s}.
\]
For every
\[
0<\delta<\frac{s-1}{b}
\]
and all sufficiently large \(n\), there is a \(k\)-graph \(G\) on
\[
N=\left\lfloor 2^{n^\delta}\right\rfloor
\]
vertices such that:

1. \(\alpha(G)<n\);
2. every \(s\)-tight component of \(G\) is \(k\)-partite.

Consequently, for every fixed \(s\)-tightly connected non-\(k\)-partite \(k\)-graph \(H\),
\[
r(H,K_n^{(k)})>2^{n^\delta}
\qquad
\text{for every }\delta<\frac{s-1}{\binom{k}{s}}
\]
and all sufficiently large \(n\).

For \(s=2\), this is exactly a bound of the conjectured tower height:
\[
r(H,K_n^{(k)})\ge t_2(n^c)=2^{n^c}
\]
for, for example,
\[
c=\frac1{k(k-1)}.
\]

Thus the conjecture is proved for \(s=2\) in every uniformity \(k\ge3\), albeit with a much weaker exponent than the \(k=3\) result from the source paper.

For \(s=1\), the conjecture is trivial: the all-blue coloring on \(n-1\) vertices gives
\[
r(H,K_n^{(k)})\ge n=t_1(n).
\]

For \(s\ge3\), Theorem 1 has only tower height \(2\), so it does not prove the stated conjecture.

A second construction gives a stronger one-exponential bound for a structural subclass.

### Theorem 2
Let \(2\le s<k\). Suppose a \(k\)-graph \(H\) admits no family of bijections
\[
\rho_e:e\longrightarrow [k],\qquad e\in E(H),
\]
such that
\[
\rho_e(v)=\rho_f(v)
\quad\text{whenever }v\in e\cap f\text{ and }|e\cap f|\ge s.
\tag{1}
\]
Then there is \(c=c(k,s)>0\) such that
\[
r(H,K_n^{(k)})\ge \exp\!\bigl(cn^{s-1}\bigr).
\tag{2}
\]

A convenient sufficient condition for (1) to be impossible is the following: for every nonisolated vertex \(v\), the graph whose vertices are the edges of \(H\) containing \(v\), with two such edges adjacent when their intersection has size at least \(s\), is connected, and \(H\) is not \(k\)-partite.

# 2. Proof of Theorem 1

## 2.1. A perfect-hash family of \(k\)-partitions

We first need a small collection of \(k\)-colorings such that every \(k\)-set is rainbow in many of them.

Let
\[
\eta=\frac{k!}{k^k}.
\]

### Lemma 3
For every sufficiently large \(N\), there are
\[
m\le C_k\log N
\]
maps
\[
\pi_i:[N]\longrightarrow[k],\qquad i\in[m],
\]
such that every \(k\)-set \(E\subseteq[N]\) satisfies
\[
\bigl|\{i\in[m]:\pi_i|_E\text{ is a bijection}\}\bigr|
   \ge \frac{\eta m}{2}.
\tag{3}
\]

#### Proof
Choose the maps independently and uniformly at random. For a fixed \(k\)-set \(E\), the probability that \(\pi_i|_E\) is bijective is \(\eta\). Thus the number of good indices for \(E\) is \(\operatorname{Bin}(m,\eta)\), and Chernoff's inequality gives
\[
\Pr\left(Z_E<\frac{\eta m}{2}\right)
 \le \exp\left(-\frac{\eta m}{8}\right).
\]
Taking, for example,
\[
m=\left\lceil \frac{16k}{\eta}\log N\right\rceil
\]
makes this probability at most \(N^{-2k}\). There are at most \(N^k\) choices for \(E\), so a union bound proves the lemma. \(\square\)

Fix such maps \(\pi_1,\ldots,\pi_m\). We regard \(\pi_i\) as a global \(k\)-partition of the vertex set.

## 2.2. Random labels on \(s\)-sets

Independently for every \(s\)-set \(S\subseteq[N]\), choose
\[
\lambda(S)\in[m]
\]
uniformly at random.

Define a \(k\)-graph \(G\) as follows. A \(k\)-set \(E\) is an edge of \(G\) if there is an index \(i\in[m]\) such that

1. \(\lambda(S)=i\) for every \(S\in\binom{E}{s}\);
2. \(\pi_i|_E\) is bijective.

The index \(i\), when it exists, is unique.

## 2.3. Structure of the \(s\)-tight components

Suppose \(E,F\in E(G)\) and \(|E\cap F|\ge s\). Let their respective indices be \(i_E\) and \(i_F\). Choose
\[
S\in\binom{E\cap F}{s}.
\]
Then
\[
i_E=\lambda(S)=i_F.
\]
It follows by propagation along an \(s\)-tight walk that every edge in an \(s\)-tight component has the same index \(i\).

Every edge in that component is rainbow under the same global map
\[
\pi_i:[N]\to[k].
\]
Thus the component is a subgraph of the complete \(k\)-partite \(k\)-graph induced by \(\pi_i\). In particular, every \(s\)-tight component of \(G\) is \(k\)-partite.

This part of the argument is deterministic.

## 2.4. A packing lemma

We use the following elementary packing estimate.

### Lemma 4
Every \(n\)-element set \(X\) contains a family
\[
\mathcal B\subseteq\binom{X}{k}
\]
such that distinct members of \(\mathcal B\) intersect in fewer than \(s\) vertices and
\[
|\mathcal B|\ge d_{k,s}n^s
\tag{4}
\]
for some constant \(d_{k,s}>0\).

#### Proof
Choose \(k\)-sets greedily. Once a \(k\)-set \(E\) is chosen, the number of \(k\)-sets intersecting \(E\) in at least \(s\) vertices is at most
\[
\binom{k}{s}\binom{n-s}{k-s}
=b\binom{n-s}{k-s}.
\]
Thus the greedy family has size at least
\[
\frac{\binom nk}{b\binom{n-s}{k-s}}
 =\frac{\binom ns}{b^2}
 =\Omega_{k,s}(n^s).
\]
\(\square\)

## 2.5. Bounding the independence number

Fix an \(n\)-set \(X\), and choose a packing \(\mathcal B\) as in Lemma 4.

For \(E\in\mathcal B\), let
\[
I_E=\{i\in[m]:\pi_i|_E\text{ is bijective}\}.
\]
By Lemma 3,
\[
|I_E|\ge \frac{\eta m}{2}.
\]
The probability that \(E\in E(G)\) is therefore
\[
\frac{|I_E|}{m^b}
 \ge \frac{\eta}{2m^{b-1}},
\tag{5}
\]
because the \(b=\binom{k}{s}\) labels on the \(s\)-subsets of \(E\) must all equal one common index from \(I_E\).

If \(E,F\in\mathcal B\) are distinct, then \(|E\cap F|<s\), so they have no common \(s\)-subset. Consequently, the events \(E\in E(G)\) and \(F\in E(G)\) depend on disjoint sets of random variables and are independent.

It follows that
\[
\Pr(X\text{ is independent in }G)
 \le
 \exp\left(
 -c_{k,s}\frac{n^s}{m^{b-1}}
 \right)
\tag{6}
\]
for some \(c_{k,s}>0\).

Now take
\[
N=\left\lfloor 2^{n^\delta}\right\rfloor,
\qquad
\delta<\frac{s-1}{b}.
\]
Since \(m=O_k(\log N)=O_k(n^\delta)\), the expected number of independent \(n\)-sets is at most
\[
\begin{aligned}
\binom Nn
\exp\left(
 -c_{k,s}\frac{n^s}{m^{b-1}}
 \right)
&\le
\exp\left(
 n\log N-c'_{k,s}n^{\,s-\delta(b-1)}
 \right)\\
&\le
\exp\left(
 O(n^{1+\delta})
 -c'_{k,s}n^{\,s-\delta(b-1)}
 \right).
\end{aligned}
\tag{7}
\]
The exponent tends to \(-\infty\), because
\[
s-\delta(b-1)>(1+\delta)
\iff
\delta b<s-1.
\]
Thus, with positive probability, \(\alpha(G)<n\).

Together with the component argument, this proves Theorem 1. \(\square\)

# 3. Ramsey consequence and the \(s=2\) case

Let \(H\) be \(s\)-tightly connected and non-\(k\)-partite. Color the edges of \(G\) red and its complement blue.

There is no blue \(K_n^{(k)}\), since \(\alpha(G)<n\). There is also no red copy of \(H\): all edges of such a copy would belong to one \(s\)-tight component of \(G\), but that component is \(k\)-partite, and every subhypergraph of a \(k\)-partite \(k\)-graph is \(k\)-partite.

Hence
\[
r(H,K_n^{(k)})>|V(G)|.
\]

When \(s=2\), \(b=\binom{k}{2}\), and we may choose
\[
\delta=\frac{1}{2b}=\frac1{k(k-1)}.
\]
This gives
\[
r(H,K_n^{(k)})
 >
 2^{\,n^{1/(k(k-1))}}
 =
 t_2\!\left(n^{1/(k(k-1))}\right),
\]
proving the conjecture for \(s=2\) and every \(k\ge3\).

# 4. Stronger one-exponential bound under a role obstruction

We now prove Theorem 2.

For every \(s\)-set \(S\subseteq[N]\), independently choose a uniformly random injection
\[
\phi_S:S\longrightarrow[k].
\]
There are
\[
(k)_s=k(k-1)\cdots(k-s+1)
\]
possible injections.

Call a \(k\)-set \(E\) coherent if there is a bijection
\[
\rho_E:E\longrightarrow[k]
\]
such that
\[
\phi_S=\rho_E|_S
\qquad
\text{for every }S\in\binom Es.
\tag{8}
\]
Let \(G\) be the \(k\)-graph of coherent \(k\)-sets.

For a fixed \(E\), the events corresponding to different bijections \(\rho_E\) are disjoint. Therefore
\[
\Pr(E\in E(G))
 =
 \frac{k!}{((k)_s)^{\binom{k}{s}}}
 =:p_{k,s}>0.
\tag{9}
\]

Using Lemma 4, a fixed \(n\)-set contains \(\Omega(n^s)\) \(k\)-sets with pairwise intersections smaller than \(s\). Their coherence events are independent, so
\[
\Pr(X\text{ is independent})
 \le \exp(-c_{k,s}n^s).
\tag{10}
\]
Taking
\[
N=\left\lfloor\exp(a n^{s-1})\right\rfloor
\]
with \(a>0\) sufficiently small gives
\[
\binom Nn\exp(-c_{k,s}n^s)<1.
\]
Hence there is a choice of the injections with
\[
\alpha(G)<n.
\tag{11}
\]

It remains to check \(H\)-freeness. If a copy of \(H\) existed in \(G\), assign to each edge \(e\) its bijection \(\rho_e\) from (8). If \(|e\cap f|\ge s\) and \(v\in e\cap f\), choose an \(s\)-set
\[
S\subseteq e\cap f
\quad\text{with }v\in S.
\]
Then
\[
\rho_e(v)=\phi_S(v)=\rho_f(v).
\]
Thus the maps \(\rho_e\) satisfy (1), contrary to the hypothesis of Theorem 2. This proves (2). \(\square\)

## A readily checked sufficient condition

For a vertex \(v\), let \(J_v\) be the graph whose vertices are the edges of \(H\) containing \(v\), with adjacency defined by intersection of size at least \(s\).

Suppose every \(J_v\) is connected. If a compatible family \((\rho_e)\) existed, then connectivity of \(J_v\) would imply that \(\rho_e(v)\) is independent of the incident edge \(e\). We could therefore define
\[
\rho(v)=\rho_e(v).
\]
Every edge would receive all \(k\) distinct values, giving a \(k\)-partition of \(H\). Thus a non-\(k\)-partite \(H\) with all \(J_v\) connected satisfies the hypothesis of Theorem 2.

For example, let \(C_\ell^{(k)}\) be the tight \(k\)-uniform cycle on \(\mathbb Z/\ell\mathbb Z\), with edges
\[
\{i,i+1,\ldots,i+k-1\}.
\]
Consecutive edges intersect in \(k-1\) vertices, and every \(J_v\) is connected for every \(s\le k-1\). A \(k\)-partition would force the vertex colors to satisfy
\[
c(i+k)=c(i).
\]
It exists exactly when \(k\mid\ell\). Hence, if \(k\nmid\ell\),
\[
r(C_\ell^{(k)},K_n^{(k)})
 \ge \exp(cn^{s-1})
\]
for every \(2\le s\le k-1\).

The same argument applies to \(K_{k+1}^{(k)}\) with \(s=k-1\), giving
\[
r(K_{k+1}^{(k)},K_n^{(k)})
 \ge \exp(cn^{k-2}).
\]

# 5. Remaining gap

For \(s\ge3\), neither construction reaches the conjectured tower height.

For instance, for
\[
k=4,\qquad s=3,\qquad H=K_5^{(4)},
\]
Theorem 2 gives
\[
r(K_5^{(4)},K_n^{(4)})\ge \exp(cn^2),
\]
whereas the conjecture asks for
\[
r(K_5^{(4)},K_n^{(4)})
 \ge t_3(n^c)
 =2^{\,2^{n^c}}.
\]
Thus even this basic case remains far beyond the argument above.

The obstruction is quantitative rather than structural. In Theorem 1, \(m=\Theta(\log N)\) global partitions are needed, and a red edge requires all \(\binom{k}{s}\) labels to agree. The resulting edge probability is of order
\[
(\log N)^{1-\binom{k}{s}},
\]
which only supports a one-exponential vertex set under the packing/union-bound argument. An iterated construction preserving the property that every \(s\)-tight component uses one global \(k\)-partition would be needed to obtain tower height \(s\); no such iteration is supplied here.