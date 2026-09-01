```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Pair constructions of complexity O(n^4 alpha^(-n)) attain every biased first-moment Ramsey lower bound, while diagonal cliques show that an arbitrary growing subpolynomial complexity does not suffice.",
  "would_publish": false,
  "caveats": "The phrase p > r(G,H)^{o(1)} needs a uniform threshold quantifier; under the likely intended interpretation the conjecture remains open."
}
```

# 1. Setup and quantifier issue

I use the standard definition from the pair-construction framework. A pair construction of complexity at most \(p\) consists of
\[
f:\binom{[N]}2\longrightarrow [p]
\]
and a palette
\[
g:[p]^3\longrightarrow \{\mathrm{red},\mathrm{blue}\},
\]
with
\[
\chi_{f,g}(x,y,z)
 =g\bigl(f(x,y),f(x,z),f(y,z)\bigr),
 \qquad x<y<z.
\]
The same arguments work if \(g\) is presented as a symmetric function on multisets of three labels.

Write \(r^p(G,H)\) for the least \(N\) such that every such coloring on \(N\) vertices contains a red \(G\) or a blue \(H\). If the source instead uses the largest admissible order, all statements below change by at most one.

There is a formal issue with the extracted conjecture: for fixed finite \(G,H\), the expression
\[
p>r(G,H)^{o(1)}
\]
is not a well-defined predicate. A plausible uniform formulation is:

> There exist \(a>0\) and a function \(q(R)=R^{o(1)}\) such that, for all \(G,H\), writing \(R=r(G,H)\), one has
> \[
> r^p(G,H)\ge R^a
> \qquad\text{whenever }p\ge q(R).
> \tag{\(*\)}
> \]

The results below do not settle \((*)\). They do, however, refute the weaker interpretation that every unbounded subpolynomial sequence of complexities should suffice.

# 2. Two elementary baseline bounds

Let
\[
u=|V(G)|,\qquad v=|V(H)|,\qquad n=\max\{u,v\}.
\]

## Proposition 2.1: Constant-complexity baseline

For every \(p\ge1\),
\[
r^p(G,H)\ge n.
\]

### Proof

With one pair label, the resulting triple coloring may be chosen entirely red or entirely blue. For every \(N<n\), at least one of these two constant colorings avoids the relevant forbidden hypergraph: if \(N<u\), use all red, and if \(N<v\), use all blue. Hence \(r^1(G,H)=n\), and monotonicity in \(p\) gives the assertion. \(\square\)

Consequently, for every family satisfying an upper bound
\[
r(G,H)\le n^C
\]
with a fixed absolute \(C\), the conjectural conclusion already holds with no condition on \(p\):
\[
r^p(G,H)\ge n\ge r(G,H)^{1/C}.
\]

For example, if \(G=M_s^{(3)}\) and \(H=M_t^{(3)}\) are 3-uniform matchings, a maximal-red-matching argument gives
\[
r(G,H)\le 3(s+t-1)\le 2n.
\]
Thus \(r^p(G,H)\ge n\ge r(G,H)/2\), and in particular \(r^p(G,H)\ge r(G,H)^{1/2}\) apart from finitely many small cases.

## Proposition 2.2: Every coloring has linear pair complexity

For all \(G,H,p\),
\[
r^p(G,H)\ge
\min\left\{r(G,H),\,\left\lfloor\frac p2\right\rfloor+1\right\}.
\tag{2.1}
\]

### Proof

It is enough to show that every triple coloring on \(N\) vertices is a pair construction with fewer than \(2N\) labels.

Choose an odd prime \(q\) with \(N<q<2N\), and identify the vertices with distinct elements of \(\mathbb F_q\). Put
\[
f(\{i,j\})=i+j.
\]
For a triple \(i,j,k\), its three labels
\[
x=i+j,\qquad y=i+k,\qquad z=j+k
\]
determine the vertices because
\[
i=\frac{x+y-z}{2},\qquad
j=\frac{x+z-y}{2},\qquad
k=\frac{y+z-x}{2}.
\]
Thus the signature of a triple determines that triple, and the palette \(g\) can be defined to reproduce any prescribed triple coloring.

Applying this to a \((G,H)\)-Ramsey coloring on every \(N<r(G,H)\) with \(2N\le p\) proves (2.1). \(\square\)

This bound alone only gives \(r^p\gg p\), so it does not approach \((*)\) for subpolynomial \(p\).

# 3. Pair constructions attain the ordinary biased first-moment bound

This is the main positive partial result.

Let
\[
e_G=|E(G)|,\qquad e_H=|E(H)|.
\]

## Lemma 3.1: Collision bound

Fix \(0<\theta<1\) and put
\[
\alpha=\min\{\theta,1-\theta\}.
\]
Choose \(f:\binom{[M]}2\to[p]\) by assigning independent uniform labels, and independently assign each possible signature red with probability \(\theta\).

Let \(S\subseteq[M]\), \(|S|=s\), and let
\(\mathcal E\subseteq\binom S3\) have \(m=|\mathcal E|\) edges. If
\[
p\ge \binom n2^2\alpha^{-(n-2)}
\qquad\text{and }s\le n,
\tag{3.1}
\]
then
\[
\Pr(\mathcal E\text{ is entirely red})
 \le \mathrm e\,\theta^m,
\tag{3.2}
\]
and
\[
\Pr(\mathcal E\text{ is entirely blue})
 \le \mathrm e\,(1-\theta)^m.
\tag{3.3}
\]

### Proof

There are
\[
b=\binom s2
\]
pair labels involved. Expose these labels in an arbitrary order. Let \(K\) be the number of labels which repeat a label already exposed; equivalently,
\[
K=b-\bigl|\operatorname{im}(f|_{\binom S2})\bigr|.
\]

Choose one representative pair for every used label. There are exactly \(K\) nonrepresentative pairs. A triangle containing no nonrepresentative pair will be called clean.

Two different clean triangles have different signatures: if their signatures agree, corresponding pair labels agree, and uniqueness of representatives forces the corresponding pairs, and hence the triangles, to be identical. Every nonrepresentative pair lies in at most \(s-2\) triangles. Therefore, if \(D\) is the number of distinct signatures among the triangles of \(\mathcal E\),
\[
D\ge m-K(s-2).
\tag{3.4}
\]

Conditional on \(f\), the probability that all edges of \(\mathcal E\) are red is \(\theta^D\), and hence by (3.4)
\[
\theta^D\le
\theta^m\left(\theta^{-(s-2)}\right)^K.
\tag{3.5}
\]

It remains to bound the exponential moment of \(K\). Let \(I_j\) indicate that the \(j\)-th exposed pair repeats an earlier label. Conditional on the previous labels,
\[
\Pr(I_j=1)\le \frac b p.
\]
Thus for every \(t\ge1\),
\[
\begin{aligned}
\mathbb E[t^K]
&=\mathbb E\left[t^{\sum_j I_j}\right]\\
&\le \left(1+\frac{b(t-1)}p\right)^b\\
&\le \exp\left(\frac{b^2(t-1)}p\right).
\end{aligned}
\tag{3.6}
\]

Taking \(t=\theta^{-(s-2)}\), equations (3.5), (3.6), and (3.1) give
\[
\Pr(\mathcal E\text{ all red})
\le
\theta^m
\exp\left(
\frac{\binom s2^2\theta^{-(s-2)}}p
\right)
\le \mathrm e\,\theta^m.
\]
The blue estimate is identical with \(\theta\) replaced by \(1-\theta\). \(\square\)

## Theorem 3.2: Pair version of the first-moment construction

Suppose
\[
p\ge \binom n2^2\alpha^{-(n-2)}.
\tag{3.7}
\]
If \(M\) satisfies
\[
\mathrm e\left(
M^u\theta^{e_G}
+
M^v(1-\theta)^{e_H}
\right)<1,
\tag{3.8}
\]
then
\[
r^p(G,H)>M.
\tag{3.9}
\]

### Proof

For each injection \(V(G)\to[M]\), Lemma 3.1 bounds the probability that all edges in that copy of \(G\) are red by
\(\mathrm e\theta^{e_G}\). There are at most \(M^u\) such injections. Similarly, the expected number of blue copies of \(H\) is at most
\[
\mathrm e M^v(1-\theta)^{e_H}.
\]
Under (3.8), the expected total number of forbidden copies is less than one. Some pair construction therefore has neither a red \(G\) nor a blue \(H\). \(\square\)

In particular, with
\[
A_\theta(G,H)=
\min\left\{
\theta^{-e_G/u},
(1-\theta)^{-e_H/v}
\right\},
\]
Theorem 3.2 gives
\[
r^p(G,H)
\ge
\left\lfloor\frac{A_\theta(G,H)}{4\mathrm e}\right\rfloor
\tag{3.10}
\]
whenever (3.7) holds.

Thus pair constructions reproduce, up to an absolute constant, the ordinary biased independent-coloring first-moment lower bound.

For \(\theta=1/2\), this becomes
\[
p\ge \binom n2^2 2^{n-2}=O(n^4 2^n)
\tag{3.11}
\]
and
\[
r^p(G,H)
\ge
c\,2^{\min\{e_G/u,e_H/v\}}.
\tag{3.12}
\]

For example,
\[
r^p\bigl(K_n^{(3)},K_n^{(3)}\bigr)
\ge
c\,2^{(n-1)(n-2)/6}
\]
already for \(p=O(n^4 2^n)\). Since the resulting order is \(2^{\Theta(n^2)}\), this complexity is subpolynomial in the constructed order.

## Consequence for first-moment-tight families

Consider a family \((G_i,H_i)\), and write
\[
R_i=r(G_i,H_i),\qquad n_i=\max\{|V(G_i)|,|V(H_i)|\}.
\]
Suppose that for suitable \(\theta_i\):

1. \(A_{\theta_i}(G_i,H_i)\ge R_i^b\) for some fixed \(b>0\); and
2. with \(\alpha_i=\min\{\theta_i,1-\theta_i\}\),
   \[
   \log\!\left(n_i^4\alpha_i^{-n_i}\right)
   =o(\log R_i).
   \]

Then there is a threshold \(p_i=R_i^{o(1)}\) such that
\[
r^{p_i}(G_i,H_i)\ge R_i^{b/2}
\]
for all sufficiently large \(i\). Hence the conjectural conclusion holds for every family whose ordinary Ramsey number is within a fixed power of its biased first-moment lower bound and for which the required complexity is subpolynomial.

The missing point is that no such comparison with the first-moment bound is available uniformly for all \(G,H\); indeed, the source paper is concerned precisely with cases where structured constructions substantially exceed elementary random bounds.

# 4. A necessary lower bound on the complexity threshold

Pair constructions also admit a simple universal upper bound in terms of ordinary multicolor graph Ramsey numbers.

Let \(\mathsf R_p(n)\) be the least \(N\) such that every \(p\)-coloring of the edges of \(K_N\) contains a monochromatic \(K_n\).

## Proposition 4.1

For all 3-graphs \(G,H\),
\[
r^p(G,H)\le
\mathsf R_p\bigl(\max\{|V(G)|,|V(H)|\}\bigr).
\tag{4.1}
\]

### Proof

If \(f\) has a monochromatic \(K_n\), say every pair in \(S\) has label \(c\), then every triple in \(S\) has the same signature \((c,c,c)\). Thus \(\chi_{f,g}\) is constant on \(\binom S3\). If that color is red, \(S\) contains a red \(G\); if it is blue, it contains a blue \(H\). \(\square\)

An elementary repeated-pigeonhole argument gives, for \(p\ge2\),
\[
\mathsf R_p(n)\le 2p^{p(n-1)+1}.
\tag{4.2}
\]
Indeed, from a sufficiently large vertex set one can successively select
\[
L=p(n-1)+1
\]
vertices \(x_i\) so that all edges from \(x_i\) to later selected vertices have one fixed color \(c_i\). Some color occurs among the \(c_i\) at least \(n\) times, yielding a monochromatic \(K_n\).

## Corollary 4.2: Not every subpolynomial \(p\) suffices

Let
\[
R_n=r\bigl(K_n^{(3)},K_n^{(3)}\bigr).
\]
A direct random-coloring argument gives
\[
R_n>
2^{(n-1)(n-2)/12}.
\tag{4.3}
\]
Indeed, for
\[
N=\left\lfloor2^{(n-1)(n-2)/12}\right\rfloor,
\]
the expected number of monochromatic \(K_n^{(3)}\)'s in a uniformly random coloring is at most
\[
2N^n2^{-\binom n3}<1.
\]

On the other hand, by (4.1) and (4.2),
\[
\log_2 r^p\bigl(K_n^{(3)},K_n^{(3)}\bigr)
\le O(pn\log p).
\tag{4.4}
\]
Consequently, whenever
\[
p\log p=o(n),
\tag{4.5}
\]
we have
\[
r^p\bigl(K_n^{(3)},K_n^{(3)}\bigr)
=
R_n^{o(1)}.
\tag{4.6}
\]

For example, take \(p_n=\lfloor\sqrt n\rfloor\). Then \(p_n\to\infty\) and
\[
p_n=R_n^{o(1)},
\]
but for every fixed \(a>0\),
\[
r^{p_n}\bigl(K_n^{(3)},K_n^{(3)}\bigr)
<
R_n^a
\]
for all sufficiently large \(n\).

Thus the interpretation

> “every unbounded subpolynomial complexity \(p=R^{o(1)}\) suffices”

is false. It also falsifies the reading “\(p\) is larger than some unspecified subpolynomial quantity”: here \(p_n>\log n\), and \(\log n=R_n^{o(1)}\).

Under the stronger uniform-threshold formulation \((*)\), this is only a restriction on the possible threshold. If \(q(R)\) is such a threshold and the conjectural exponent is \(a\), then along the diagonal clique sequence it is necessary that
\[
q(R_n)\log q(R_n)=\Omega_a(n).
\tag{4.7}
\]
In particular,
\[
q(R_n)=\Omega_a\!\left(\frac n{\log n}\right).
\tag{4.8}
\]
Indeed, otherwise taking \(p=\lceil q(R_n)\rceil\) in (4.4) would contradict (4.3) and \(r^p\ge R_n^a\).

# 5. What remains open

The arguments establish three points:

1. Every triple coloring has pair complexity \(O(N)\).
2. Complexity \(O(n^4\alpha^{-n})\) is enough to reproduce every biased first-moment Ramsey lower bound for forbidden 3-graphs on at most \(n\) vertices.
3. Complexity merely tending to infinity, or even an arbitrary \(R^{o(1)}\) sequence, is insufficient: for diagonal cliques one needs at least roughly \(n/\log n\) before a fixed-power conclusion is even possible by the elementary multicolor-Ramsey obstruction.

They do not prove the likely intended conjecture \((*)\). The unresolved step is to handle pairs \(G,H\) for which \(r(G,H)\) is much larger than all elementary first-moment lower bounds. Nothing above extracts a polynomial-size low-complexity subconstruction from an arbitrary near-extremal Ramsey coloring, nor does it provide a family requiring polynomial-in-\(R\) pair complexity. Thus there is no complete proof or counterexample to the intended uniform-threshold formulation.