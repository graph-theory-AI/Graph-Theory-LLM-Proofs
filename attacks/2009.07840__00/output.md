```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained packing argument places the isolated-state threshold between asymptotically sqrt(log n/(2n)) and sqrt(2 log n/n), but it does not show that absence of isolated states implies connectivity.",
  "would_publish": false,
  "caveats": "The conjecture is informal, and the packing lower bound may overlap the cited follow-up literature; no sharp connectivity result is obtained."
}
```

# 1. Formalization

For a bijection \(\sigma:V(X)\to V(Y)\), its degree in the friends-and-strangers graph is

\[
d_{\mathsf{FS}(X,Y)}(\sigma)
 =
 \bigl|\{uv\in E(X):\sigma(u)\sigma(v)\in E(Y)\}\bigr|.
\]

Thus \(\sigma\) is isolated precisely when it is a **packing** of \(X\) and \(Y\): no edge of \(X\) is mapped to an edge of \(Y\).

Let \(Z=Z(X,Y)\) denote the number of such packings. A natural precise version of the informal conjecture would be the following. Define median thresholds

\[
p_I(n)=\inf\{p:\Pr(Z=0)\ge 1/2\}
\]

and

\[
p_C(n)=\inf\{p:\Pr(\mathsf{FS}(X,Y)\text{ is connected})\ge 1/2\}.
\]

Both events are monotone increasing under addition of edges, and connectivity implies \(Z=0\), so \(p_I(n)\le p_C(n)\). The strong interpretation of the conjecture is

\[
p_C(n)=(1+o(1))p_I(n),
\]

or, more ambitiously, equality of the two critical windows. I do not prove this.

I establish the following self-contained partial result. All logarithms are natural.

## Theorem

Let \(X,Y\) be independent copies of \(G(n,p)\).

1. For every fixed \(\gamma>0\), if
   \[
   np^2\le \frac12\log n-\left(\frac52+\gamma\right)\log\log n,
   \tag{1}
   \]
   then with high probability \(\mathsf{FS}(X,Y)\) has an isolated vertex.

2. If
   \[
   np^2\ge 2\log n-1,
   \tag{2}
   \]
   then with high probability \(\mathsf{FS}(X,Y)\) has no isolated vertex.

Consequently,

\[
(1-o(1))\sqrt{\frac{\log n}{2n}}
\ \le\
p_I(n)
\ \le\
(1+o(1))\sqrt{\frac{2\log n}{n}}.
\tag{3}
\]

In particular, the isolated-state threshold is determined to within a factor \(2+o(1)\) in \(p\). The lower half of the theorem also yields the same lower bound for the connectivity threshold.

I have not verified whether this packing bound is already contained in the cited follow-up literature, so no novelty claim is made.

# 2. First-moment upper bound for isolated states

Put \(N=\binom n2\). For a fixed bijection \(\sigma\), the \(N\) events

\[
\{uv\in E(X)\text{ and }\sigma(u)\sigma(v)\in E(Y)\}
\]

are mutually independent, each with probability \(p^2\). Hence

\[
\Pr(\sigma\text{ is isolated})=(1-p^2)^N
\]

and therefore

\[
\mathbb E Z=n!(1-p^2)^N.
\tag{4}
\]

If \(np^2\ge 2\log n-1\), then

\[
\begin{aligned}
\log \mathbb E Z
&\le \log(n!)-p^2N\\
&\le n\log n-n+O(\log n)
   -\frac{(2\log n-1)(n-1)}2\\
&=-\frac n2+O(\log n),
\end{aligned}
\]

so \(\mathbb E Z=o(1)\). Markov's inequality gives \(Z=0\) with high probability.

The exact point where the expectation equals one is

\[
p_{\mathrm{FM}}^2
 =
1-\exp\left(-\frac{\log(n!)}{\binom n2}\right)
 =
\frac{2(\log n-1)}n
 +O\left(\frac{(\log n)^2}{n^2}\right).
\tag{5}
\]

Expectation alone does not show that this is the actual packing threshold.

# 3. A matching lemma with read-bounded dependencies

The lower bound uses a sequential packing construction.

## Lemma 1: read-\(L\) inequality

Let \((\xi_u)_{u\in U}\) be independent random variables. Suppose events \(E_x\), \(x\in A\), depend respectively on coordinate sets \(D_x\subseteq U\), and every coordinate belongs to at most \(L\) of the sets \(D_x\). If \(\Pr(E_x)\ge q\) for every \(x\), then

\[
\Pr\left(\bigcap_{x\in A}E_x^c\right)
 \le (1-q)^{|A|/L}
 \le \exp\left(-\frac{|A|q}{L}\right).
\tag{6}
\]

### Proof

The generalized Hölder inequality for a read-\(L\) family states that for nonnegative functions \(f_x\), with \(f_x\) depending only on \(D_x\),

\[
\mathbb E\prod_x f_x
 \le
 \prod_x \bigl(\mathbb E f_x^L\bigr)^{1/L}.
\]

It follows by successively applying ordinary Hölder in each independent coordinate; the hypothesis that a coordinate occurs in at most \(L\) functions permits exponent \(L\), with dummy factors \(1\) if necessary.

Apply this with \(f_x=\mathbf 1_{E_x^c}\). Since \(f_x^L=f_x\),

\[
\Pr\left(\bigcap_xE_x^c\right)
\le
\prod_x\Pr(E_x^c)^{1/L}
\le
(1-q)^{|A|/L}.
\qedhere
\]

## Lemma 2: a random compatibility graph has a perfect matching

Let \(S,T\) be sets of common size \(s\), and let \(U\) be a third set. For each \(x\in S\), let \(A_x\subseteq U\), with

\[
|A_x|\le d
\quad\text{and}\quad
|\{x:u\in A_x\}|\le L
\quad\text{for every }u\in U.
\tag{7}
\]

Independently put each edge \(yu\), \(y\in T,u\in U\), into a random graph with probability \(p\). Define a bipartite compatibility graph \(H\) on \(S,T\) by declaring \(xy\in E(H)\) if \(y\) has no random edge to \(A_x\).

Put

\[
q=(1-p)^d,\qquad \rho=\frac{s q}{L}.
\]

If \(\rho/\log s\to\infty\), then \(H\) has a perfect matching with probability \(1-o(1)\), uniformly over all families satisfying (7).

### Proof

Fix \(A\subseteq S\), \(B\subseteq T\), with \(|A|=a\), \(|B|=b\). For a fixed \(y\in B\), let \(E_x\) be the event that \(y\) has no edge to \(A_x\). Then

\[
\Pr(E_x)=(1-p)^{|A_x|}\ge q.
\]

The coordinate corresponding to \(yu\) appears in at most \(L\) events \(E_x\). Lemma 1 therefore gives

\[
\Pr(y\text{ has no neighbor in }A)
\le e^{-aq/L}.
\]

Different vertices \(y\in B\) use disjoint collections of random edges, so

\[
\Pr(E_H(A,B)=\varnothing)
\le e^{-abq/L}.
\tag{8}
\]

If Hall's condition fails, there is an \(A\subseteq S\), \(|A|=a\), and a set \(C\subseteq T\), \(|C|=a-1\), such that \(N_H(A)\subseteq C\). Thus there are no edges between \(A\) and \(T\setminus C\), whose size is \(s-a+1\). By (8),

\[
\Pr(H\text{ has no perfect matching})
\le
\sum_{a=1}^s
\binom sa\binom{s}{a-1}
\exp\left(-\frac{a(s-a+1)q}{L}\right).
\tag{9}
\]

Let \(t=\min\{a,s-a+1\}\). Then

\[
a(s-a+1)\ge \frac{st}{2}
\]

and

\[
\binom sa\binom{s}{a-1}\le s^{2t}.
\]

If \(\rho=sq/L\ge 8\log s\), the summand is at most \(e^{-t\rho/4}\). Summing over \(t\) proves the claim. \(\square\)

# 4. Construction of an isolated state

It suffices by monotonicity to prove the lower assertion at the largest \(p=p_0\) satisfying

\[
np_0^2
 =
\frac12\log n-\left(\frac52+\gamma\right)\log\log n.
\tag{10}
\]

Indeed, a packing for graphs sampled at \(p_0\) remains a packing after edges are deleted.

We henceforth write \(p=p_0\).

## 4.1 Partitioning \(X\) into locally sparse independent classes

With high probability,

\[
\Delta(X)=np+O\bigl(\sqrt{np\log n}\bigr)=(1+o(1))np.
\tag{11}
\]

Set

\[
h=100\log n,\qquad
k=\left\lceil\frac{np}{h}\right\rceil.
\]

Independently assign the vertices of \(X\) to \(k\) bins \(B_1,\dots,B_k\).

Conditional on (11), for every vertex \(v\) and bin \(B_j\),

\[
|N_X(v)\cap B_j|
\]

is binomial with mean at most \((1+o(1))h\). Chernoff's inequality and a union bound over at most \(n^2\) pairs \((v,j)\) show that, with probability \(1-o(1)\),

\[
|N_X(v)\cap B_j|\le L:=\lceil 3h\rceil
\quad\text{for every }v,j.
\tag{12}
\]

The bin sizes are all

\[
|B_j|=\Theta\left(\frac hp\right)
\tag{13}
\]

with high probability.

By (12), each induced graph \(X[B_j]\) has maximum degree at most \(L\). The equitable coloring theorem gives a proper equitable \((L+1)\)-coloring of each \(X[B_j]\). Let

\[
S_1,\dots,S_K
\]

be all resulting color classes. They have the following properties:

1. every \(S_i\) is independent in \(X\);
2. uniformly in \(i\),
   \[
   |S_i|=\Theta(1/p);
   \tag{14}
   \]
3. for every vertex \(z\in V(X)\) and every \(i\),
   \[
   |N_X(z)\cap S_i|\le L=O(\log n).
   \tag{15}
   \]

Moreover, \(K=O(np)\).

Partition \(V(Y)\), without exposing any edges of \(Y\), into sets

\[
T_1,\dots,T_K
\]

such that \(|T_i|=|S_i|\) for every \(i\).

## 4.2 Sequentially mapping the classes

We construct bijections \(f_i:S_i\to T_i\) in order.

Suppose \(f_1,\dots,f_{i-1}\) have already been chosen. For \(x\in S_i\), let

\[
A_x
 =
 f\bigl(N_X(x)\cap(S_1\cup\cdots\cup S_{i-1})\bigr)
 \subseteq T_1\cup\cdots\cup T_{i-1}.
\tag{16}
\]

A target \(y\in T_i\) is compatible with \(x\) if \(y\) has no \(Y\)-edge to \(A_x\).

The edges between \(T_i\) and the earlier target blocks have not been exposed at any previous stage. Conditional on the complete history, they are therefore still independent Bernoulli-\(p\) variables.

We have

\[
|A_x|\le\Delta(X).
\]

Furthermore, if \(u=f(z)\) is a previously used target, then by (15),

\[
|\{x\in S_i:u\in A_x\}|
 =
 |N_X(z)\cap S_i|
 \le L.
\tag{17}
\]

Thus Lemma 2 applies with

\[
d=\Delta(X),\qquad q=(1-p)^{\Delta(X)}.
\]

From (10) and (11),

\[
\begin{aligned}
\log q
&=\Delta(X)\log(1-p)\\
&=-p\Delta(X)+O(p^2\Delta(X))\\
&=-np^2+o(1).
\end{aligned}
\]

Indeed, in the present range both
\(p\sqrt{np\log n}=o(1)\) and \(np^3=o(1)\). Therefore

\[
q=(1+o(1))e^{-np^2}
 =
n^{-1/2}(\log n)^{5/2+\gamma+o(1)}.
\tag{18}
\]

Writing \(s_i=|S_i|\), (14) gives \(s_i\ge c/p\) for an absolute \(c>0\). Hence

\[
\frac{s_iq}{L}
\ge
c'\frac{q}{p\log n}.
\]

Using \(p=\Theta(n^{-1/2}\sqrt{\log n})\) and (18),

\[
\frac{s_iq}{L}
\ge
(\log n)^{1+\gamma+o(1)}
\gg \log s_i.
\tag{19}
\]

Lemma 2 therefore supplies a perfect matching between \(S_i\) and \(T_i\), except with probability

\[
\exp\bigl(-(\log n)^{1+\gamma+o(1)}\bigr).
\]

This estimate is uniform conditional on all previous choices. Since \(K=O(np)=n^{1/2+o(1)}\), a union bound shows that all stages succeed with probability \(1-o(1)\).

Let \(f=\bigcup_i f_i\). This is a bijection \(V(X)\to V(Y)\).

If \(xz\in E(X)\), then \(x,z\) lie in distinct independent classes. Suppose \(x\in S_i\), \(z\in S_j\), with \(i<j\). At stage \(j\), the point \(f(x)\) belongs to \(A_z\); compatibility of the selected image \(f(z)\) gives

\[
f(x)f(z)\notin E(Y).
\]

Thus no edge of \(X\) is mapped to an edge of \(Y\). Hence \(f\) is an isolated vertex of \(\mathsf{FS}(X,Y)\), completing the proof of the lower assertion.

# 5. Consequences and remaining gap

The theorem proves

\[
p_I(n)\in
\left[
(1-o(1))\sqrt{\frac{\log n}{2n}},
\,
(1+o(1))\sqrt{\frac{2\log n}{n}}
\right].
\]

Since a connected friends-and-strangers graph cannot have an isolated state,

\[
p_C(n)\ge
(1-o(1))\sqrt{\frac{\log n}{2n}}.
\]

What is not proved is any corresponding connectivity statement near the disappearance of the isolated states. In particular, the argument gives no way to rule out:

- components of size greater than one after \(Z\) becomes zero;
- a multiplicative gap between \(p_I(n)\) and \(p_C(n)\);
- different critical windows for the two monotone properties.

The quoted conjecture is therefore unresolved under the strong, natural interpretation \(p_C(n)/p_I(n)\to1\). Under the much weaker interpretation that both thresholds merely have exponent \(n^{-1/2+o(1)}\), the source theorem already essentially establishes that statement.