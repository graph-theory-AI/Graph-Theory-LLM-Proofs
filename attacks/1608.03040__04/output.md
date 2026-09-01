```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general conjecture remains open, but every Eulerian tournament and every Eulerian digraph satisfying an explicit high-degree Lovász-local-lemma condition has a majority 3-colouring.",
  "would_publish": false,
  "caveats": "Assumes finite loopless simple digraphs; the tournament special case may already be known, and the general mixed-degree case remains untouched."
}
```

# Majority 3-colourings of Eulerian digraphs

## 1. Statement and conventions

For a colouring \(c:V(D)\to\{1,2,3\}\), put
\[
m_c^+(v)=|\{w\in N^+(v):c(w)=c(v)\}|.
\]
A majority 3-colouring satisfies
\[
m_c^+(v)\le \frac{d^+(v)}2
\qquad\text{for every }v.
\]

Throughout, digraphs are finite, loopless, and have no parallel arcs, although opposite arcs are allowed. The loopless convention is essential: if loops are admitted and counted, the one-vertex one-loop digraph is Eulerian and has no majority colouring with any number of colours.

I do not resolve the general problem. I prove a nontrivial complete special case—Eulerian tournaments—and give two quantitative partial results for general Eulerian digraphs.

---

## 2. Eulerian tournaments

### Theorem 2.1
Every Eulerian tournament has a majority 3-colouring.

Since an Eulerian tournament is necessarily regular, it has \(n=2d+1\) vertices and every vertex has outdegree and indegree \(d\).

### Proof

Choose uniformly at random an equitable partition
\[
V(T)=C_1\mathbin{\dot\cup} C_2\mathbin{\dot\cup} C_3,
\]
meaning that the three class sizes \(s_1,s_2,s_3\) differ by at most one. Use the classes as the three colours.

Fix a vertex \(v\), condition on \(v\in C_i\), and put \(r=s_i-1\). The other \(r\) vertices of \(C_i\) form a uniformly random \(r\)-subset of \(V(T)\setminus\{v\}\). Exactly \(d\) of the \(2d\) available vertices are outneighbours of \(v\). Hence
\[
X_v:=|N^+(v)\cap C_i|
\]
has the hypergeometric distribution
\[
\Pr(X_v=k)
 =\frac{\binom dk\binom d{r-k}}{\binom{2d}{r}}.
\]
The vertex \(v\) is bad precisely when
\[
X_v\ge \left\lfloor\frac d2\right\rfloor+1.
\]

For later use, define
\[
p(d,s)=
\frac{\displaystyle
 \sum_{k=\lfloor d/2\rfloor+1}^{s-1}
 \binom dk\binom d{s-1-k}}
 {\binom{2d}{s-1}},
\]
with binomial coefficients outside their natural range interpreted as zero. If \(B\) denotes the number of bad vertices, then
\[
\mathbb E B=\sum_{i=1}^3 s_i\,p(d,s_i). \tag{2.1}
\]
Indeed, a given vertex lies in \(C_i\) with probability \(s_i/(2d+1)\), and there are \(2d+1\) choices of the vertex.

We show that the right side of (2.1) is always less than \(1\).

### A hypergeometric tail estimate

If \(X\) counts the ones in a uniformly random \(r\)-subset of a population consisting of \(d\) ones and \(d\) zeros, then
\[
\Pr(X-r/2\ge t)\le \exp\left(-\frac{2t^2}{r}\right). \tag{2.2}
\]

For completeness, let the population values be \(z_1,\dots,z_{2d}\in\{0,1\}\), with \(d\) of each value. By Maclaurin's inequality for elementary symmetric means, for \(\lambda\ge0\),
\[
\begin{aligned}
\mathbb E e^{\lambda X}
&=
\frac{e_r(e^{\lambda z_1},\dots,e^{\lambda z_{2d}})}
     {\binom{2d}{r}}\\
&\le
\left(\frac{1+e^\lambda}{2}\right)^r.
\end{aligned}
\]
Consequently,
\[
\mathbb E e^{\lambda(X-r/2)}
 \le \cosh(\lambda/2)^r
 \le e^{r\lambda^2/8}.
\]
Markov's inequality and optimization at \(\lambda=4t/r\) give (2.2).

For an equitable partition of \(2d+1\) vertices,
\[
r=s_i-1\le \left\lfloor\frac{2d}{3}\right\rfloor.
\]
Writing \(k_0=\lfloor d/2\rfloor+1\), we therefore have
\[
k_0-\frac r2\ge \frac d6+\frac12=\frac{d+3}{6}.
\]
Thus (2.2) gives
\[
p(d,s_i)
 \le \exp\left(-\frac{(d+3)^2}{12d}\right). \tag{2.3}
\]
It follows that
\[
\mathbb E B
 \le (2d+1)\exp\left(-\frac{(d+3)^2}{12d}\right)<1
 \qquad(d\ge50). \tag{2.4}
\]
At \(d=50\), the exponent is
\[
\frac{53^2}{600}=4.681\ldots>\log 101=4.615\ldots,
\]
and the difference
\[
\frac{(d+3)^2}{12d}-\log(2d+1)
\]
is increasing for \(d\ge50\).

The remaining cases are a finite exact calculation using (2.1). The following Python 3 code uses only integer arithmetic and rational numbers.

```python
from math import comb
from fractions import Fraction

def C(n, k):
    if k < 0 or k > n:
        return 0
    return comb(n, k)

def p_bad(d, s):
    r = s - 1
    h = d // 2
    numerator = sum(C(d, k) * C(d, r-k)
                    for k in range(h+1, r+1))
    denominator = C(2*d, r)
    return Fraction(numerator, denominator)

def expected_bad(d):
    n = 2*d + 1
    q, rem = divmod(n, 3)
    sizes = [q+1] * rem + [q] * (3-rem)
    return sum((s * p_bad(d, s) for s in sizes),
               Fraction(0, 1))

values = [(expected_bad(d), d) for d in range(1, 50)]
assert all(E < 1 for E, d in values)
assert max(values) == (Fraction(2, 3), 5)
print(max(values))
```

The output is

```text
(Fraction(2, 3), 5)
```

Thus \(\mathbb E B<1\) for every \(d\ge1\). Since \(B\) is a nonnegative integer, some equitable partition has \(B=0\). This partition is a majority 3-colouring. The one-vertex tournament is immediate. ∎

### Remarks

1. The calculation does not enumerate tournaments; it only evaluates the orientation-independent hypergeometric expression (2.1).
2. I have not independently checked whether this tournament special case already occurs in the literature.

---

## 3. General high-degree criteria

The next observations do not require the tournament structure.

Put
\[
\alpha=\frac12\log\frac98=0.0588915\ldots.
\]

### Proposition 3.1: union-bound criterion
Let \(D\) be a loopless simple digraph. If
\[
\sum_{v\in V(D)}
 \left(\frac89\right)^{d^+(v)/2}<1,
 \tag{3.1}
\]
then \(D\) has a majority 3-colouring.

#### Proof

Colour every vertex independently and uniformly from three colours. Conditional on \(c(v)\),
\[
m_c^+(v)\sim \operatorname{Bin}(d^+(v),1/3).
\]
The Chernoff relative-entropy estimate gives
\[
\begin{aligned}
\Pr\left(m_c^+(v)>\frac{d^+(v)}2\right)
&\le
\exp\left(
-d^+(v)D\left(\frac12\middle\|\frac13\right)
\right)\\
&=
\exp(-\alpha d^+(v))
=
\left(\frac89\right)^{d^+(v)/2}.
\end{aligned}
\]
The union bound and (3.1) finish the proof. ∎

In particular, an \(n\)-vertex digraph is covered whenever
\[
\delta^+(D)>
\frac{2\log n}{\log(9/8)}
=16.981\ldots\log n.
\]

### Proposition 3.2: local-lemma criterion
Let \(D\) be Eulerian, with isolated vertices deleted, and put
\[
\delta=\min_v d^+(v),
\qquad
\Delta=\max_v d^+(v).
\]
If
\[
e(\Delta+1)^2
 \left(\frac89\right)^{\delta/2}\le1, \tag{3.2}
\]
then \(D\) has a majority 3-colouring.

#### Proof

Let \(A_v\) be the event that \(v\) violates the majority condition. As above,
\[
\Pr(A_v)\le \left(\frac89\right)^{\delta/2}.
\]

The event \(A_v\) depends only on the colour variables indexed by
\[
\{v\}\cup N^+(v),
\]
a set of size at most \(\Delta+1\). A given colour variable \(c(x)\) occurs only in \(A_x\) and in the events \(A_u\) with \(u\to x\). Since \(D\) is Eulerian,
\[
d^-(x)=d^+(x)\le\Delta,
\]
so \(c(x)\) occurs in at most \(\Delta+1\) bad events. Thus \(A_v\) is dependent on at most
\[
(\Delta+1)^2-1
\]
other events. Condition (3.2) is exactly the standard symmetric Lovász local lemma condition \(ep(D+1)\le1\). ∎

### Corollary 3.3
Every \(d\)-regular Eulerian digraph with
\[
d\ge197
\]
has a majority 3-colouring.

Indeed,
\[
1+2\log(198)-197\alpha=-0.0250\ldots<0,
\]
and \(1+2\log(d+1)-\alpha d\) decreases for \(d\ge197\).

According to the literature information supplied with the problem, the known sparse result covers maximum outdegree at most \(4\). Hence, for regular Eulerian digraphs, these two results leave the interval
\[
5\le d\le196
\]
unsettled in general. The tournament theorem covers the tournament members of that interval.

---

## 4. What the standard monochromatic-arc potential does prove

The following records precisely how far the most natural Eulerian potential argument goes.

### Proposition 4.1
Every Eulerian digraph has a 3-colouring \(c\) satisfying
\[
m_c^+(v)+m_c^-(v)\le\frac{2d(v)}3
\qquad\text{for every }v. \tag{4.1}
\]
Moreover, in such a colouring obtained by minimizing the number of monochromatic arcs, the vertices violating the desired outgoing majority condition have total degree-volume less than two-thirds of the total degree-volume.

#### Proof

Choose a 3-colouring minimizing the number of monochromatic arcs. For a vertex \(v\), let
\[
a_i^+(v)=|\{w\in N^+(v):c(w)=i\}|,
\qquad
a_i^-(v)=|\{w\in N^-(v):c(w)=i\}|.
\]
Suppose \(c(v)=i\). Recolouring \(v\) with either other colour \(j\) cannot decrease the objective, so
\[
a_i^+(v)+a_i^-(v)
 \le a_j^+(v)+a_j^-(v)
\]
for both \(j\ne i\). The three quantities sum to
\[
d^+(v)+d^-(v)=2d(v),
\]
and hence (4.1) follows.

Let
\[
B=\{v:m_c^+(v)>d(v)/2\}.
\]
For \(v\in B\), (4.1) gives
\[
m_c^-(v)<\frac{d(v)}6
\]
and therefore
\[
m_c^+(v)-m_c^-(v)>\frac{d(v)}3. \tag{4.2}
\]

Within each colour class, the total number of internal arcs counted at their tails equals the total counted at their heads. Consequently,
\[
\sum_v\bigl(m_c^+(v)-m_c^-(v)\bigr)=0.
\]
For a vertex outside \(B\),
\[
m_c^-(v)-m_c^+(v)
\le m_c^-(v)+m_c^+(v)
\le\frac{2d(v)}3.
\]
Writing \(\operatorname{vol}(S)=\sum_{v\in S}d(v)\), (4.2) now gives
\[
\frac13\operatorname{vol}(B)
<
\frac23\operatorname{vol}(V\setminus B).
\]
Thus
\[
\operatorname{vol}(B)<\frac23\operatorname{vol}(V).
\]
∎

This shows the exact obstruction to the naive potential argument: a bad vertex has very large monochromatic outdegree but very small monochromatic indegree. Eulerian balance cancels these imbalances only after summing over an entire colour class, not vertex by vertex.

---

## 5. A restriction on a minimal counterexample

### Proposition 5.1
Let \(D\) be an arc-minimal counterexample to the conjecture. Then the subdigraph induced by the vertices of even outdegree is acyclic.

#### Proof

Suppose the even-degree vertices contain a directed cycle \(C\). Delete all arcs of \(C\), obtaining an Eulerian digraph \(D'\) with fewer arcs. By minimality, \(D'\) has a majority 3-colouring.

For \(v\in V(C)\), write \(d_D(v)=2k\). In \(D'\), the degree is \(2k-1\), so the number of same-coloured outgoing arcs is at most
\[
\left\lfloor\frac{2k-1}{2}\right\rfloor=k-1.
\]
Restoring \(C\) adds exactly one outgoing arc at \(v\), increasing this number by at most one. It therefore remains at most \(k=d_D(v)/2\). Vertices outside \(C\) are unaffected, contradicting that \(D\) is a counterexample. ∎

Thus, in an arc-minimal obstruction, the odd-degree vertices meet every directed cycle; equivalently, they form a directed feedback vertex set.

Also, every weakly connected Eulerian digraph of positive degree is strongly connected: in the acyclic condensation, a source component has no entering arcs, and Eulerian balance then forces it to have no leaving arcs. Hence a minimal counterexample may be assumed strongly connected as well.

---

## 6. Remaining gap

The general conjecture is not proved here. The unresolved regime includes Eulerian digraphs having many vertices of small or moderate degree together with complicated overlap among their outneighbourhoods. The random-colouring argument is then too weak, while minimizing monochromatic arcs controls only
\[
m_c^+(v)+m_c^-(v),
\]
not the required outgoing term separately.

The concrete progress established above is:

- every Eulerian tournament has a majority 3-colouring;
- dense Eulerian digraphs satisfying (3.1) do;
- Eulerian digraphs satisfying the local degree condition (3.2) do, including all \(d\)-regular examples for \(d\ge197\);
- any arc-minimal counterexample has its even-degree vertices inducing an acyclic digraph.

No counterexample is produced, and no argument given here covers all Eulerian digraphs.