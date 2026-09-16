```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained argument establishes the conjecture up to a factor 1+O(log log m/log m), uniformly in k, but does not prove the exact inequality.",
  "would_publish": false,
  "caveats": "No resolution for fixed m≥4; no novelty claim is made for the asymptotic result."
}
```

## 1. A uniform asymptotic version

Write
\[
M(m,k)=\max\{\operatorname{ch}(G):\chi(G)=k,\ |V(G)|\le mk\}.
\]
The conjecture is precisely
\[
M(m,k)=\operatorname{ch}(K_{m*k}).
\]

I obtain the following partial result. All logarithms below are natural.

**Theorem.** Let \(m\ge1\) and \(k\ge2\) be integers, and put
\[
\lambda_k=\log\frac{k}{k-1}.
\]
Then
\[
M(m,k)\le
\left\lceil\frac{\log m+3}{\lambda_k}\right\rceil. \tag{1}
\]
Moreover, if \(L=\log m\ge20\), then
\[
\operatorname{ch}(K_{m*k})
>
\frac{L-2\log L-\log\log L-8}{\lambda_k}. \tag{2}
\]

Consequently,
\[
1\le
\frac{M(m,k)}{\operatorname{ch}(K_{m*k})}
\le
\frac{L+4}{L-2\log L-\log\log L-8}
=
1+O\!\left(\frac{\log\log m}{\log m}\right), \tag{3}
\]
where the implicit constant is independent of \(k\).

Thus, for every \(\varepsilon>0\), the conjectured inequality holds with a multiplicative factor \(1+\varepsilon\) for all sufficiently large \(m\), **simultaneously for every \(k\)**. The case \(k=1\) holds exactly.

The proof is self-contained. I do not claim that this asymptotic statement is new.

## 2. The exact extremal reduction

Given a proper \(k\)-coloring of \(G\), add all edges between different color classes. If necessary, add vertices to the classes until the order is \(mk\). This produces a complete \(k\)-partite supergraph, without decreasing the choice number.

Hence
\[
M(m,k)=
\max_{\substack{n_1,\dots,n_k\ge1\\n_1+\cdots+n_k=mk}}
\operatorname{ch}(K_{n_1,\dots,n_k}).
\]
The unresolved issue is therefore genuinely one of balancing the part sizes. The upper bound below does not assume that the color classes are balanced.

## 3. Proof of the upper bound

Fix a \(k\)-chromatic graph \(G\) of order at most \(mk\), together with a proper coloring
\[
V(G)=V_1\cup\cdots\cup V_k.
\]
Set
\[
q=\left\lceil\frac{\log m+3}{\lambda_k}\right\rceil.
\]
Consider an arbitrary list assignment in which every list has exactly \(q\) colors.

We use
\[
k-1\le \frac1{\lambda_k}\le k. \tag{4}
\]
In particular, \(q\ge k\).

### The cases \(k=2,3\)

Independently assign every color appearing in the lists to one of \(k\) bins, uniformly. Call a vertex \(v\in V_i\) bad if its list contains no color from bin \(i\).

The expected number of bad vertices is at most
\[
mk\left(1-\frac1k\right)^q
\le k e^{-3}<1.
\]
Thus there is an assignment with no bad vertices. Color every vertex of \(V_i\) using a color from bin \(i\). This is proper.

### The cases \(k\ge4\)

Introduce a reserve bin. Independently assign each color to:

- the reserve bin with probability \(\rho=k/q\);
- each of the \(k\) ordinary bins with probability \((1-\rho)/k\).

Again, \(v\in V_i\) is bad if its list misses ordinary bin \(i\). Write
\[
\beta=1-\frac{1-\rho}{k}.
\]
If \(B\) is the number of bad vertices, then
\[
\mathbb E B\le mk\beta^q.
\]
Since
\[
\log\beta
=
-\lambda_k+\log\left(1+\frac{\rho}{k-1}\right)
\le-\lambda_k+\frac{\rho}{k-1},
\]
we have
\[
q\log\beta
\le-(\log m+3)+\frac{k}{k-1}
\le-\log m-\frac53.
\]
Therefore
\[
\mathbb E B\le k e^{-5/3}. \tag{5}
\]

For a vertex \(v\), let \(R_v\) count the reserve colors in its list. Conditional on \(v\) being bad, its list colors remain independent, and
\[
R_v\sim\operatorname{Bin}\left(q,\frac{\rho}{\beta}\right).
\]
The conditional mean is
\[
\mu=\frac{q\rho}{\beta}=\frac{k}{\beta}\ge k.
\]
The elementary binomial lower-tail bound gives
\[
\Pr(R_v<k/2\mid v\text{ is bad})
\le e^{-k/8}.
\]
Consequently,
\[
\Pr(\exists\text{ bad }v\text{ with }R_v<k/2)
\le k e^{-5/3-k/8}. \tag{6}
\]
Also, by Markov's inequality,
\[
\Pr(B>k/2)\le2e^{-5/3}. \tag{7}
\]
Combining (6) and (7), the probability that either undesirable event occurs is at most
\[
e^{-5/3}\left(2+k e^{-k/8}\right)
\le
e^{-5/3}\left(2+\frac8e\right)
<1.
\]

Choose an outcome avoiding both events. Color all nonbad vertices from their respective ordinary bins. There are at most \(\lfloor k/2\rfloor\) bad vertices, and each has at least \(\lceil k/2\rceil\) reserve colors. They can therefore be given pairwise distinct reserve colors greedily.

Ordinary-bin colors do not conflict across color classes, and reserve colors were not used on nonbad vertices. This proves (1).

## 4. A list obstruction from hitting sets

We next construct lower bounds for the balanced graph.

Suppose that \(\mathcal F=(A_1,\dots,A_m)\) is a family of \(q\)-element subsets of a palette of \(N\) colors, and every set meeting all members of \(\mathcal F\) has size at least \(r\).

Assign the lists \(A_1,\dots,A_m\) to the \(m\) vertices in each part of \(K_{m*k}\). In any proper list coloring:

- the colors used in each part meet every member of \(\mathcal F\), so there are at least \(r\) of them;
- different parts use disjoint sets of colors.

It follows that this assignment is uncolorable whenever
\[
kr>N. \tag{8}
\]

We will also use a scaling observation. Replace each palette color by \(\ell\) distinct clones, and replace each list by all clones of its colors. List sizes and palette size are multiplied by \(\ell\), but the minimum size of a hitting set remains at least \(r\): projecting a hitting set onto the original colors gives a hitting set for \(\mathcal F\).

## 5. Constructing the obstruction

Assume \(L=\log m\ge20\), and define
\[
r=\lceil L^2\rceil,\qquad b=\lceil L\rceil,\qquad
T=L-2\log L-\log\log L-6.
\]
Here \(T>2\).

We first prove that, for every integer \(2\le j\le b^2\), there are \(m\) lists of size
\[
q=\left\lfloor\frac{T}{\lambda_j}\right\rfloor
\]
on a palette of
\[
N=jr-1
\]
colors, with no hitting set of size \(r-1\).

Choose the \(m\) lists independently and uniformly from the \(q\)-subsets of the palette. Repeated lists are allowed.

Fix an \((r-1)\)-subset \(S\). The probability that one random list avoids \(S\) is
\[
p=
\frac{\binom{(j-1)r}{q}}{\binom{jr-1}{q}}
=
\prod_{i=0}^{q-1}\frac{(j-1)r-i}{jr-1-i}. \tag{9}
\]
The binomial coefficients are well-defined: by (4),
\[
q\le jL\le (j-1)r.
\]

Put \(a=(j-1)/j\). Each factor in (9) satisfies
\[
\frac{(j-1)r-i}{jr-1-i}
=
a\left(1+\frac{j-1-i}{(j-1)(N-i)}\right)
\ge
a\left(1-\frac{i}{(j-1)(N-i)}\right).
\]
Also,
\[
N-q\ge \frac{jL^2}{2},
\qquad
\frac{i}{(j-1)(N-i)}
\le\frac{2}{(j-1)L}\le\frac12.
\]
Using \(\log(1-x)\ge-2x\) for \(0\le x\le1/2\), we obtain
\[
\begin{aligned}
\log p
&\ge q\log a
-\frac{q(q-1)}{(j-1)(N-q)}\\
&\ge-q\lambda_j-4.
\end{aligned}
\]
Since \(q\lambda_j\le T\),
\[
mp\ge m e^{-T-4}=e^2L^2\log L. \tag{10}
\]

On the other hand, the number of candidate hitting sets satisfies
\[
\log\binom{N}{r-1}
\le r\log(2ej)
\le6L^2\log L. \tag{11}
\]
For the last inequality, use \(r\le2L^2\), \(j\le\lceil L\rceil^2\), and
\(\log(2e\lceil L\rceil^2)\le3\log L\) for \(L\ge20\).

A fixed \(S\) meets all \(m\) lists with probability
\[
(1-p)^m\le e^{-mp}.
\]
Thus (10), (11), and the union bound show that the probability of any hitting set of size \(r-1\) is at most
\[
\exp\left((6-e^2)L^2\log L\right)<1.
\]
The required family therefore exists.

By (8), this immediately yields
\[
\operatorname{ch}(K_{m*j})
\ge q+1
>
\frac{T}{\lambda_j},
\qquad 2\le j\le b^2. \tag{12}
\]

## 6. Extending the lower bound to every \(k\)

It remains to cover \(k>b^2\).

Use the family just constructed for \(j=b\). Its lists have size
\[
q_0=\left\lfloor\frac{T}{\lambda_b}\right\rfloor,
\]
its palette has \(br-1\) colors, and every hitting set has size at least \(r\).

Let
\[
\ell=\left\lfloor\frac{k}{b}\right\rfloor.
\]
Clone each color \(\ell\) times. The resulting lists have size \(\ell q_0\), and the palette has
\[
\ell(br-1)\le kr-1
\]
colors. The hitting-set obstruction gives
\[
\operatorname{ch}(K_{m*k})\ge\ell q_0+1. \tag{13}
\]

By (4),
\[
q_0\ge(b-1)T-1,
\qquad
\ell\ge k/b-1.
\]
Using \(k>b^2\), expansion of these inequalities gives
\[
\ell q_0+1
>
k\left(T-\frac{2T+1}{b}\right).
\]
Since \(T\le L-6\) and \(b\ge L\), we have \(2T+1<2b\). Hence
\[
\operatorname{ch}(K_{m*k})
>
k(T-2)
\ge\frac{T-2}{\lambda_k}.
\]
Together with (12), this proves, for every \(k\ge2\),
\[
\operatorname{ch}(K_{m*k})
>
\frac{L-2\log L-\log\log L-8}{\lambda_k},
\]
which is (2).

Finally, \(\lambda_k\le\log2<1\), so (1) implies
\[
M(m,k)\le\frac{L+4}{\lambda_k}.
\]
Dividing by (2) proves (3).

## 7. What remains unresolved

The partial result gives the explicit additive estimate
\[
0\le M(m,k)-\operatorname{ch}(K_{m*k})
<
\frac{2\log L+\log\log L+11}{\lambda_k}+1,
\qquad L=\log m\ge20.
\]
Since \(1/\lambda_k=\Theta(k)\), the possible gap here is still of order
\(k\log\log m\).

That gap cannot be discarded when the desired statement is an exact integer inequality. In particular, this argument provides **no resolution of the \(m=4\) case**. It establishes asymptotic extremality of the balanced graph, not the required exact balancing principle.