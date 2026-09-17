```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact m=4 bound holds when the total shortfall of color classes smaller than four is sufficiently large compared with both the number of oversized classes and log k.",
  "would_publish": false,
  "caveats": "This is a sufficient condition on color-class sizes, not a resolution of m=4 or the full conjecture; no novelty claim is made."
}
```

## 1. A fixed-\(m\) partial result

I obtain an exact special case for \(m=4\), rather than another approximation as \(m\to\infty\).

Fix a proper \(k\)-coloring of \(G\), with nonempty color classes of sizes
\[
n_1,\ldots,n_k.
\]
Define
\[
r=\bigl|\{i:n_i\ge5\}\bigr|,
\qquad
D=\sum_{i:n_i\le3}(4-n_i).
\]
Thus \(r\) counts oversized classes, while \(D\) is the total deficit in the undersized classes.

**Partial theorem.** Suppose that \(|V(G)|\le4k\). If either \(r=0\), or
\[
D\ge64r
\qquad\text{and}\qquad
D\ge10^4\log(8k),                                      \tag{1}
\]
then
\[
\operatorname{ch}(G)\le
\left\lfloor\frac{3k}{2}\right\rfloor
=\operatorname{ch}(K_{4*k}).                            \tag{2}
\]
Here and below, logarithms are natural.

The constants are deliberately unoptimized. An immediate asymptotic consequence is:

> For a sequence of \(k\)-chromatic graphs of order at most \(4k\), the conjectured bound holds for all sufficiently large \(k\) if a chosen \(k\)-coloring satisfies
> \[
> r=o(D)
> \quad\text{and}\quad
> \log k=o(D).
> \]

The only external inputs are two theorems stated in the question:

1. the Noel–West–Wu–Zhu bound
   \[
   \operatorname{ch}(H)\le
   \max\left\{\chi(H),
   \left\lceil\frac{|V(H)|+\chi(H)-1}{3}\right\rceil\right\};
                                                               \tag{3}
   \]
2. \(\operatorname{ch}(K_{4*b})=\lfloor3b/2\rfloor\).

From the previous attempt, I reuse only the reserve-palette idea, reproving the estimate needed here. Its random hitting-set lower bound is not used.

## 2. Reduction to complete multipartite graphs

Add every edge between distinct color classes of the chosen coloring. The resulting graph is
\[
F=K_{n_1,\ldots,n_k},
\]
and
\[
\operatorname{ch}(G)\le\operatorname{ch}(F).
\]
It therefore suffices to prove the theorem for \(F\).

If \(r=0\), every part has size at most four, so \(F\) is a subgraph of \(K_{4*k}\). This case is immediate.

For the rest of the proof, assume \(r\ge1\). Notice that
\[
\sum_{i:n_i\ge5}(n_i-4)\le D,
\]
because \(\sum_i n_i\le4k\). In particular,
\[
D\ge r.                                                 \tag{4}
\]

## 3. A coarse multipartite choosability bound

The following estimate is sufficient for the block consisting of oversized parts.

**Lemma 1.** If a graph \(H\) has a proper \(s\)-coloring and \(N\ge s\) vertices, then
\[
\operatorname{ch}(H)\le
\left\lceil s\left(\log\frac Ns+3\right)\right\rceil.      \tag{5}
\]

**Proof.** Put
\[
q=\left\lceil s\left(\log\frac Ns+3\right)\right\rceil,
\]
and consider an arbitrary assignment of lists of exactly \(q\) colors. Write the color classes as \(V_1,\ldots,V_s\).

Independently assign every palette color to a reserve bin with probability
\[
\rho=\frac{s}{q},
\]
and to each of \(s\) ordinary bins with probability \((1-\rho)/s\).

Call \(v\in V_i\) bad if its list misses ordinary bin \(i\). With
\[
\beta=1-\frac1s+\frac1q,
\]
the number \(B\) of bad vertices satisfies
\[
\mathbb EB=N\beta^q.
\]
Since \(\log x\le x-1\),
\[
q\log\beta\le-\frac qs+1
\le-\log\frac Ns-2,
\]
and hence
\[
\mathbb EB\le se^{-2}.                                  \tag{6}
\]

Conditional on a vertex being bad, its number \(R_v\) of reserve colors is binomial with mean
\[
\frac{q\rho}{\beta}=\frac{s}{\beta}\ge s.
\]
The binomial lower-tail bound therefore gives
\[
\Pr(R_v<s/2\mid v\text{ is bad})\le e^{-s/8}.
\]
Consequently,
\[
\Pr(\text{some bad }v\text{ has }R_v<s/2)
\le se^{-2-s/8}.                                        \tag{7}
\]
Also, by Markov's inequality,
\[
\Pr(B>s/2)\le2e^{-2}.                                   \tag{8}
\]
The sum of the bounds in (7) and (8) is at most
\[
e^{-2}\left(2+\frac8e\right)<1.
\]

Choose an outcome avoiding both events. Color every nonbad vertex from its ordinary bin. There are at most \(\lfloor s/2\rfloor\) bad vertices, each with at least \(\lceil s/2\rceil\) reserve colors, so give them pairwise distinct reserve colors greedily.

The ordinary bins separate the original color classes, and reserve colors have not been used on nonbad vertices. This is a proper list coloring. \(\square\)

## 4. Joining a large block to two exceptional blocks

A direct palette split typically incurs an error of order
\(\sqrt{\operatorname{ch}(H)\log N}\). Here it is important that the error can depend only on the two exceptional blocks, not on the large block of four-vertex parts.

**Lemma 2.** Suppose
\[
V(H)=V_0\mathbin{\dot\cup}V_1\mathbin{\dot\cup}V_2,
\qquad |V(H)|=N\ge1,
\]
and
\[
\operatorname{ch}(H[V_i])\le h_i
\]
for nonnegative integers \(h_i\). Set
\[
S=h_1+h_2,\qquad h=h_0+h_1+h_2,\qquad t=\log(2N).
\]
Then
\[
\operatorname{ch}(H)\le
\left\lceil h+4\sqrt{St}+9t\right\rceil.                 \tag{9}
\]

**Proof.** Let the right side of (9) be \(q\), and consider arbitrary lists of size \(q\).

For \(i=1,2\), define
\[
d_i=\sqrt{2h_it}+2t,\qquad \mu_i=h_i+d_i,
\]
and put
\[
\mu=\mu_1+\mu_2,\qquad d_0=\sqrt{2\mu t}+2t.
\]
We first check that
\[
q\ge h_0+\mu+d_0.                                       \tag{10}
\]
Indeed,
\[
d_1+d_2\le2\sqrt{St}+4t,
\]
so
\[
\mu\le S+2\sqrt{St}+4t
\le(\sqrt S+2\sqrt t)^2.
\]
It follows that
\[
d_0\le\sqrt{2St}+(2\sqrt2+2)t.
\]
Thus
\[
h_0+\mu+d_0
\le h+(2+\sqrt2)\sqrt{St}+(6+2\sqrt2)t
\le h+4\sqrt{St}+9t,
\]
proving (10).

Assign each palette color independently to bin \(i\), for \(i=1,2\), with probability \(\mu_i/q\), and assign it to bin \(0\) otherwise. Equation (10) ensures these probabilities are valid.

For a vertex in \(V_i\), \(i=1,2\), the number of colors in bin \(i\) has mean \(\mu_i\). Since
\[
d_i^2\ge2t(h_i+d_i)=2t\mu_i,
\]
the probability that fewer than \(h_i\) colors remain is at most \(e^{-t}\).

For a vertex in \(V_0\), the number of colors outside bin \(0\) has mean \(\mu\). Failure requires more than \(q-h_0\ge\mu+d_0\) such colors. Using
\[
\Pr(X\ge\mathbb EX+u)
\le\exp\left(-\frac{u^2}{2(\mathbb EX+u)}\right)
\]
and \(d_0^2\ge2t(\mu+d_0)\), its failure probability is also at most \(e^{-t}\).

A union bound gives total failure probability at most
\[
Ne^{-t}=\frac12.
\]
For a successful outcome, color each \(H[V_i]\) using its bin. Distinct bins have disjoint palettes, so all edges between the blocks are respected. \(\square\)

## 5. Applying the two lemmas

Partition the parts of \(F\) into three blocks:

- \(a\) parts of size at most three;
- \(b\) parts of size exactly four;
- \(r\) parts of size at least five.

Thus
\[
a+b+r=k.
\]
The first block has exactly \(4a-D\) vertices, and
\[
a\le D\le3a.                                           \tag{11}
\]
The oversized block has at most \(4r+D\) vertices.

Use the four-vertex block as \(V_0\) in Lemma 2. Valid choosability bounds for the three blocks are
\[
h_0=\left\lfloor\frac{3b}{2}\right\rfloor,
\]
\[
h_1=
\max\left\{
a,\left\lceil\frac{5a-D-1}{3}\right\rceil
\right\},
\]
and
\[
h_2=
\left\lceil r\left(\log\left(4+\frac Dr\right)+3\right)\right\rceil.
\]
The bound on \(h_1\) follows from (3), and the bound on \(h_2\) follows from Lemma 1.

By (11),
\[
h_1\le\frac32a-\frac D6+1.
\]
Define
\[
\Gamma=
\frac D6-r\left(\log\left(4+\frac Dr\right)+\frac32\right). \tag{12}
\]
The preceding bounds imply
\[
h_0+h_1+h_2\le\frac32k-\Gamma+2,                         \tag{13}
\]
and
\[
S=h_1+h_2
\le\frac32(a+r)-\Gamma+2
\le\frac32(D+r)-\Gamma+2.                               \tag{14}
\]

These equations already give a profile-sensitive bound:
\[
\operatorname{ch}(F)\le
\left\lceil
\frac32k-\Gamma+2
+4\sqrt{\left(\frac32(D+r)-\Gamma+2\right)\log(8k)}
+9\log(8k)
\right\rceil.                                          \tag{15}
\]
The expression under the square root is positive; in particular, \(\Gamma\le D/6\).

### Verifying the sufficient conditions

Assume \(D\ge64r\), and put \(x=D/r\). The function
\[
f(x)=\frac{\log(4+x)+3/2}{x}
\]
is decreasing for \(x>0\). Consequently,
\[
\frac{\Gamma}{D}
=\frac16-f(x)
\ge\frac16-f(64)
>\frac16-\frac{13}{128}
>\frac1{16}.
\]
Here we used \(\log68<5\). Therefore
\[
\Gamma\ge\frac D{16}.                                  \tag{16}
\]
Moreover, \(D\ge64r\ge64\), so (14) yields
\[
S\le\frac32(D+r)+2
\le\frac{195}{128}D+2
<2D.                                                    \tag{17}
\]

Write \(L=\log(8k)\). Lemma 2, (13), (16), and (17) now give
\[
\operatorname{ch}(F)\le
\left\lceil
\frac32k-\frac D{16}+2+4\sqrt{2DL}+9L
\right\rceil.                                          \tag{18}
\]

If also \(D\ge10^4L\), then
\[
4\sqrt{2DL}+9L
\le\left(\frac{\sqrt2}{25}+\frac9{10^4}\right)D
<\frac{23}{400}D.
\]
Since \(1/16=25/400\), equation (18) implies
\[
\operatorname{ch}(F)
<\frac32k-\frac D{200}+3
<\frac32k.
\]
The last inequality follows from
\(D\ge10^4\log(8k)>20000\).

Because the choice number is an integer,
\[
\operatorname{ch}(F)\le\left\lfloor\frac32k\right\rfloor.
\]
This proves the partial theorem.

## 6. A concrete family covered by the theorem

For \(1\le s\le k-1\), consider
\[
F_{k,s}=
K_{\,s+4,\,
\underbrace{3,\ldots,3}_{s\text{ parts}},\,
\underbrace{4,\ldots,4}_{k-s-1\text{ parts}}}.
\]
It has \(k\) parts and exactly \(4k\) vertices. Its parameters are
\[
r=1,\qquad D=s.
\]
Thus
\[
s\ge\max\{64,10^4\log(8k)\}
\quad\Longrightarrow\quad
\operatorname{ch}(F_{k,s})
\le\operatorname{ch}(K_{4*k}).
\]
In particular, this holds eventually for every sequence \(s=s(k)\) satisfying
\[
\frac{s(k)}{\log k}\longrightarrow\infty.
\]

This includes graphs with one part of unbounded size, while almost all other parts can still have size four.

## 7. What remains unresolved

The partial theorem implies a necessary condition on any counterexample to the \(m=4\) case: **every** proper \(k\)-coloring must have \(r\ge1\) and must satisfy
\[
D<64r
\quad\text{or}\quad
D<10^4\log(8k).
\]

The argument does not cover profiles with many mildly oversized parts, such as equal numbers of parts of sizes three and five. It also does not handle bounded-size perturbations of the all-four profile by this method.

The remaining gap is therefore substantial. The proof exploits a linear saving from undersized parts when their deficit is concentrated into relatively few oversized parts; it supplies no general balancing principle. Consequently, it does not resolve \(m=4\), much less the full conjecture.