```json
{
  "verdict": "partial",
  "confidence": "medium",
  "one_line": "For the standard size-conditioned model, the noncrossing-Dyck-path encoding and each distinguished Schnyder tree have an explicit local limit given by a type-C2 Doob transform, but the required transfer to the full triangulation remains unproved.",
  "would_publish": false,
  "caveats": "The supplied statement omits the precise size/Boltzmann law and rooting, and the non-tree-edge closure has not been shown to be finitary."
}
```

# 1. Statement and scope

The catalog statement is not quite a formal probabilistic assertion. Fixing only a boundary length does not give a finite set of triangulations if arbitrary interior vertices are allowed, so “uniform” requires at least one of the following additional specifications:

- a fixed number of interior vertices;
- a fixed total number of edges;
- a critical Boltzmann law;
- or a specified joint limit of boundary length and volume.

The location of the root is also essential: a fixed boundary edge, a uniformly chosen boundary edge, and a uniformly chosen interior edge generally lead to different limits.

I therefore treat the standard size-conditioned model that is naturally associated with the tree-height comparison in the question:

\[
\mathcal W_n=\{(T,S):T\text{ is a rooted triangulation with }n
\text{ internal vertices, and }S\text{ is a Schnyder wood of }T\}.
\]

Under the usual encoding, \(\mathcal W_n\) is in bijection with pairs of weakly noncrossing Dyck paths of length \(2n\). I prove:

1. an explicit local limit of this path encoding;
2. joint convergence of its initial and terminal windows;
3. local convergence of each individual color tree;
4. exponential separation of a uniform Schnyder wood from the maximal wood.

The missing step for the full conjecture is a stabilization result for the non-tree edges created by the inverse path-to-map closure.

# 2. The noncrossing-path encoding

Let \((L^{(n)},U^{(n)})\) be uniformly chosen among pairs of Dyck paths of length \(2n\) satisfying

\[
0\leq L^{(n)}_j\leq U^{(n)}_j,\qquad 0\leq j\leq 2n.
\]

Both paths have increments in \(\{-1,+1\}\) and start and end at zero.

Set

\[
X^{(n)}_j=\bigl(L^{(n)}_j+1,U^{(n)}_j+3\bigr).
\]

Then \(X^{(n)}\) is a walk with increments \((\pm1,\pm1)\), starting and ending at

\[
a=(1,3),
\]

and constrained to the chamber

\[
C=\{(x_1,x_2)\in\mathbb Z^2:0<x_1<x_2\}.
\]

Conversely, every chamber walk in the parity class of \(a\) gives a unique noncrossing pair. Thus the uniform path pair is the walk with four equiprobable increments, conditioned to remain in \(C\) and return to \(a\) at time \(2n\).

Define

\[
h(x_1,x_2)=x_1x_2(x_2^2-x_1^2).
\]

This is positive in \(C\), zero on the two chamber walls, and harmonic for the unrestricted walk:

\[
\frac14\sum_{\varepsilon_1,\varepsilon_2\in\{-1,1\}}
h(x_1+\varepsilon_1,x_2+\varepsilon_2)=h(x_1,x_2).
\]

Indeed, writing \(h(x,y)=xy^3-x^3y\),

\[
\mathbb E[(x+\varepsilon_1)(y+\varepsilon_2)^3]
=x(y^3+3y)
\]

and

\[
\mathbb E[(x+\varepsilon_1)^3(y+\varepsilon_2)]
=(x^3+3x)y,
\]

so the extra terms cancel.

# 3. Killed-walk asymptotics

Let

\[
q_m(x,y)=\mathbb P_x(X_m=y,\ X_0,\ldots,X_m\in C)
\]

for the unconditioned diagonal walk.

For one-dimensional simple random walk, let

\[
k_m(r,s)
=
2^{-m}\left[
\binom{m}{(m+s-r)/2}
-
\binom{m}{(m+s+r)/2}
\right],
\]

with invalid binomial coefficients interpreted as zero. This is the transition kernel killed at zero. The reflection determinant gives

\[
q_m(x,y)=
\det\begin{pmatrix}
k_m(x_1,y_1)&k_m(x_1,y_2)\\
k_m(x_2,y_1)&k_m(x_2,y_2)
\end{pmatrix}.
\]

A Stirling expansion of this determinant yields, for fixed reachable \(x,y\in C\),

\[
q_m(x,y)
\sim
\frac{4}{3\pi}\,h(x)h(y)m^{-5}.
\tag{1}
\]

The exponent \(5\) comes from the cancellation of all lower-order terms in the determinant. More explicitly, after extracting the factors \(x_i y_jm^{-3/2}\), the first nonzero determinant term is proportional to

\[
(x_2^2-x_1^2)(y_2^2-y_1^2)m^{-2}.
\]

For later tightness estimates one also obtains, directly from the determinant and Gaussian bounds for binomial coefficients, the fixed-start estimate

\[
q_m(a,x)\leq
C\,h(a)h(x)m^{-5}
\exp\left(-c\frac{|x|^2}{m}\right).
\tag{2}
\]

Only the case of fixed \(a=(1,3)\) is needed here.

# 4. Explicit endpoint local limit

## Theorem 1

For every fixed \(k\), the first \(k\) steps of \(X^{(n)}\) converge in distribution to the Markov chain \(X^\uparrow\) on \(C\), started at \(a\), with transition probabilities

\[
P^\uparrow(x,y)
=
\frac14\frac{h(y)}{h(x)}
\tag{3}
\]

when \(y-x\in\{(\pm1,\pm1)\}\) and \(y\in C\), and zero otherwise.

Moreover, the initial window and the time-reversal of the terminal window converge jointly to two independent copies of \(X^\uparrow\).

### Proof

Fix an admissible path

\[
a=x_0,x_1,\ldots,x_k=x.
\]

Conditioning on the initial segment gives

\[
\begin{aligned}
&\mathbb P\bigl(
X^{(n)}_0=x_0,\ldots,X^{(n)}_k=x_k
\bigr)\\
&\qquad =
4^{-k}\frac{q_{2n-k}(x,a)}{q_{2n}(a,a)}.
\end{aligned}
\]

Using (1),

\[
4^{-k}\frac{q_{2n-k}(x,a)}{q_{2n}(a,a)}
\longrightarrow
4^{-k}\frac{h(x)}{h(a)}.
\]

This is exactly the product of the transitions in (3). Harmonicity of \(h\) shows that these transitions sum to one.

For the two-ended assertion, prescribe an initial segment of length \(k\), ending at \(x\), and a reversed terminal segment of length \(\ell\), ending at \(y\). Its probability is

\[
4^{-(k+\ell)}
\frac{q_{2n-k-\ell}(x,y)}{q_{2n}(a,a)}.
\]

Equation (1) gives the limit

\[
4^{-(k+\ell)}
\frac{h(x)h(y)}{h(a)^2},
\]

which factors into the probabilities of two independent \(h\)-transformed paths. ∎

For example, \(h(1,3)=24\). The first step is forced to \((2,4)\). From \((2,4)\), the possible second states and probabilities are

\[
\begin{array}{c|c}
\text{state}&P^\uparrow\\ \hline
(1,3)&1/16\\
(1,5)&5/16\\
(3,5)&10/16.
\end{array}
\]

# 5. Escape from the chamber walls

The \(h\)-transformed walk does more than leave every finite set.

## Lemma 2

Under \(P^\uparrow_a\),

\[
X^\uparrow_{1,m}\longrightarrow\infty
\quad\text{and}\quad
X^\uparrow_{2,m}-X^\uparrow_{1,m}\longrightarrow\infty
\]

almost surely.

### Proof

From the Doob-transform identity and (2),

\[
\mathbb P^\uparrow_a(X_m=x)
=
q_m(a,x)\frac{h(x)}{h(a)}
\leq
C h(x)^2m^{-5}e^{-c|x|^2/m}.
\tag{4}
\]

For fixed \(R\), if \(x_1\leq R\), then \(h(x)\leq C_Rx_2^3\). Hence

\[
\begin{aligned}
\mathbb P^\uparrow_a(X_{1,m}\leq R)
&\leq
C_Rm^{-5}\sum_{s\geq 1}s^6e^{-cs^2/m}\\
&\leq C_Rm^{-3/2}.
\end{aligned}
\]

This is summable in \(m\). Borel–Cantelli proves that \(X_{1,m}\leq R\) only finitely often. The same calculation, using

\[
h(x)=x_1x_2(x_2-x_1)(x_2+x_1),
\]

works for a fixed-width strip \(x_2-x_1\leq R\). ∎

The corresponding conditioned bridges also avoid the walls away from their two endpoints. More precisely, for every fixed \(R\),

\[
\lim_{K\to\infty}\limsup_{n\to\infty}
\mathbb P\left(
\min_{K\leq j\leq 2n-K}X^{(n)}_{1,j}\leq R
\right)=0,
\tag{5}
\]

and similarly for \(X^{(n)}_{2,j}-X^{(n)}_{1,j}\).

To see this, for \(j\leq n\),

\[
\mathbb P(X^{(n)}_j=x)
=
\frac{q_j(a,x)q_{2n-j}(x,a)}{q_{2n}(a,a)}.
\]

Equations (1)–(2) imply

\[
\frac{q_{2n-j}(x,a)}{q_{2n}(a,a)}
\leq C\frac{h(x)}{h(a)}.
\]

Thus the probability of being in a fixed-width wall strip at time \(j\) is at most a constant times the corresponding probability under \(P^\uparrow\), hence \(O(j^{-3/2})\). Summing over \(K\leq j\leq n\), and treating the second half by time reversal, proves (5).

# 6. Consequence for one Schnyder tree

In the usual noncrossing-Dyck encoding of a wooded triangulation, the lower path \(L^{(n)}\) is the contour process of one distinguished color tree \(T^{(0)}_n\).

## Corollary 3

The rooted plane tree \(T^{(0)}_n\) has a local limit. The limit is an infinite, locally finite, one-ended plane tree obtained by gluing together the unmatched rays encoded by the lower coordinates of two independent copies of \(X^\uparrow\).

The same marginal conclusion holds for each of the three color trees by color symmetry.

### Argument

The first and reversed last portions of \(L^{(n)}\) converge to

\[
H^{\mathrm L}_j=X^{\uparrow,\mathrm L}_{1,j}-1,
\qquad
H^{\mathrm R}_j=X^{\uparrow,\mathrm R}_{1,j}-1,
\]

where the two joint chamber walks are independent. Lemma 2 says that both lower paths tend to infinity.

A nonnegative nearest-neighbor path tending to infinity encodes one side of a plane tree with an infinite spine: unmatched up-steps form the spine, while finite matched excursions encode finite bushes. Glue the two copies spine-level by spine-level, reversing the order on the right side. This gives a locally finite one-ended plane tree.

For a direct convergence argument, fix \(r\). By (5), with probability tending to one as \(K\to\infty\), uniformly in large \(n\), every contour visit to levels at most \(r\) occurs either during the first \(K\) steps or during the final \(K\) steps. On this event the radius-\(r\) tree ball is determined entirely by these two endpoint windows. Theorem 1 therefore gives convergence of every finite-radius tree ball.

This is a genuine graph-local result, but only for a spanning-tree projection, not for the union of all colored edges.

# 7. The exact remaining map-level lemma

Let \(\Phi_n(L,U)\) denote the inverse bijection producing the wooded triangulation. The path result would imply the full local limit if one proved the following finitary-closure statement.

For every radius \(r\), there should be functions \(F_{r,K}\), depending only on the first and last \(K\) path steps, such that

\[
\lim_{K\to\infty}\limsup_{n\to\infty}
\mathbb P\left(
B_r(\Phi_n(L^{(n)},U^{(n)}))
\neq
F_{r,K}(\text{endpoint windows})
\right)=0.
\tag{6}
\]

If (6) holds, Theorem 1 immediately gives convergence of all finite map balls. The candidate limit is obtained from two independent \(h\)-transformed chamber walks by an infinite version of the closure construction.

I have not proved (6). The obstruction is specific: non-tree colored edges are produced by parenthesis/stack matchings which can span a macroscopically long middle portion of the encoding. Avoidance of low contour levels proves stabilization for the lower spanning tree, but it does not by itself rule out a long matching edge entering a fixed map-distance neighborhood of the root. Establishing that no such edge does so is the central unresolved step.

# 8. Exact enumeration and separation from the maximal wood

For the standard rooted convention, the number of wooded triangulations is

\[
W_n
=
\frac{6(2n)!(2n+2)!}
{n!(n+1)!(n+2)!(n+3)!}.
\tag{7}
\]

This follows directly from the reflection determinant above. Its asymptotics are

\[
W_n\sim \frac{24}{\pi}\,16^n n^{-5}.
\tag{8}
\]

The number of rooted triangulations with \(n\) internal vertices is

\[
T_n=
\frac{2(4n+1)!}{(n+1)!(3n+2)!},
\tag{9}
\]

and

\[
T_n\sim
\frac89\sqrt{\frac{2}{3\pi}}
\left(\frac{256}{27}\right)^n n^{-5/2}.
\tag{10}
\]

Since each triangulation has exactly one maximal Schnyder wood, a uniform wooded triangulation is maximal with probability

\[
\frac{T_n}{W_n}
\sim
\frac1{27}\sqrt{\frac{2\pi}{3}}\,
n^{5/2}\left(\frac{16}{27}\right)^n.
\tag{11}
\]

Thus maximal woods are exponentially rare in the uniform wooded ensemble.

There is also a positive-density Hamming separation. Under the usual convention, a non-boundary edge has at most twelve possible complete oriented/color states. Let \(d(S,S_{\max}(T))\) count edges whose state differs from the maximal wood of the same triangulation. The number of pairs with \(d\leq \delta n\) is at most

\[
T_n\sum_{k\leq\delta n}\binom{3n}{k}11^k.
\]

For \(\delta=0.07\), the exponential contribution of the sum is at most

\[
3H(0.07/3)+0.07\log 11
\approx 0.5001,
\]

whereas

\[
\log(27/16)\approx0.5232.
\]

Equations (8)–(10) therefore imply

\[
\mathbb P\left(
d(S_n,S_{\max}(T_n))\leq0.07n
\right)\longrightarrow0.
\tag{12}
\]

Consequently, under the natural coupling on the same underlying map and with a uniformly selected non-boundary edge, the uniform and maximal decorations disagree at that edge with limiting probability at least \(0.07/3\).

This does **not** prove that the two standalone local weak limits differ. The comparison with \(S_{\max}(T)\) uses a globally defined decoration, and global total-variation separation or different height exponents need not imply different local limits.

# 9. Reproducible finite checks

The path counts and the first nontrivial cylinder probability can be checked by the following exhaustive code.

```python
from itertools import product

def dycks(n):
    out = []
    for w in product((1, -1), repeat=2*n):
        h = 0
        hs = [0]
        good = True
        for s in w:
            h += s
            hs.append(h)
            if h < 0:
                good = False
                break
        if good and h == 0:
            out.append((w, hs))
    return out

for n in range(1, 7):
    D = dycks(n)
    total = 0
    initial_UD_UD = 0
    for lw, lh in D:
        for uw, uh in D:
            if all(x <= y for x, y in zip(lh, uh)):
                total += 1
                if lw[:2] == (1, -1) and uw[:2] == (1, -1):
                    initial_UD_UD += 1
    print(n, total, initial_UD_UD)
```

The output is

\[
\begin{array}{c|rrrrrr}
n&1&2&3&4&5&6\\ \hline
W_n&1&3&14&84&594&4719\\
\#(UD,UD\text{ prefix})&1&1&3&14&84&594.
\end{array}
\]

Indeed, the exact prefix probability is \(W_{n-1}/W_n\), namely

\[
\frac{n(n+1)(n+2)(n+3)}
{(2n-1)(2n)(2n+1)(2n+2)}
\longrightarrow \frac1{16},
\]

in agreement with the \(h\)-transform calculation.

# 10. Conclusion and gaps

The canonical path encoding has a completely explicit endpoint local limit, and every individual Schnyder tree has a locally finite one-ended local limit. This substantially narrows the map-level problem: it remains to prove the finitary closure estimate (6), or an equivalent tightness/stabilization statement for non-tree colored edges.

The following points are not proved here:

1. existence of the full wooded-triangulation local limit;
2. local finiteness of the candidate infinite closure;
3. identification of that closure as a half-plane triangulation;
4. inequality in law from the maximal-Schnyder-wood half-plane limit;
5. applicability to a boundary-Boltzmann model if that, rather than the size-\(n\) model, is the source paper’s intended ensemble.