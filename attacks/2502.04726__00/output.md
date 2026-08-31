```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The universal upper bound remains open, but the proposed order is necessary and holds for Hamiltonian graphs whose chords mix short cyclic intervals, including a natural planted-random model.",
  "would_publish": false,
  "caveats": "No universal improvement over the source paper's O(ell^2) upper bound is obtained."
}
```

## 1. Definitions and results obtained

Write \(\operatorname{ch}(G)\) for the largest \(r\) such that \(G\) contains \(K_r\) as a cyclic minor. I use the following equivalent formulation of the source paper's definition:

A cyclic \(K_r\)-model consists of a cycle \(C\) and a partition
\[
V(C)=I_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}I_r
\]
into nonempty consecutive intervals of \(C\), such that every two distinct intervals \(I_i,I_j\) are joined by an edge of \(G\). Contracting the cycle edges inside each \(I_i\) then gives a \(K_r\).

Every cyclic \(K_r\)-minor is an ordinary \(K_r\)-minor. Hence, denoting the ordinary Hadwiger number by \(h(G)\),
\[
\operatorname{ch}(G)\le h(G).
\]

I prove the following partial results.

1. A self-contained lower bound
   \[
   f(r)\ge (\beta-o(1))r\sqrt{\ln r},
   \qquad
   \beta=\max_{0<p<1}\frac{p}{\sqrt{-\ln(1-p)}}=0.638\ldots .
   \]
   The witnessing graphs can moreover be chosen Hamiltonian and without even an ordinary \(K_r\)-minor.

2. A deterministic sufficient condition on a Hamilton cycle under which the conjectured upper scale holds.

3. For a fixed Hamilton cycle with independent random chords, the cyclic Hadwiger number is
   \[
   \Theta\!\left(\frac{\delta(G)}{\sqrt{\ln\delta(G)}}\right)
   \]
   with high probability.

These do not prove the universal upper bound.

---

## 2. An interval-mixing criterion

Let \(C\) be a Hamilton cycle of an \(n\)-vertex graph \(G\). Define \(J_C(G)\) to be the least positive integer \(s\) such that every two disjoint \(C\)-intervals, each containing at least \(s\) vertices, are joined by an edge of \(G\).

### Lemma 2.1
\[
\operatorname{ch}(G)\ge \left\lfloor\frac{n}{J_C(G)}\right\rfloor.
\]

#### Proof
Put \(s=J_C(G)\) and \(k=\lfloor n/s\rfloor\). Partition \(C\) into \(k\) consecutive intervals, each of size at least \(s\), distributing the fewer than \(s\) remaining vertices arbitrarily among the intervals. Every two intervals are adjacent by the definition of \(J_C(G)\). Contracting each interval therefore gives a cyclic \(K_k\)-minor. \(\square\)

This gives a degree-scale version.

### Corollary 2.2
Let \(G\) be an \(n\)-vertex Hamiltonian graph of minimum degree \(d\ge 3\). Suppose that, for some constant \(A\),
\[
J_C(G)\le A\sqrt{\frac{n\ln n}{d}}
\tag{2.1}
\]
for a Hamilton cycle \(C\). Then
\[
\operatorname{ch}(G)
 \ge \frac1A\sqrt{\frac{nd}{\ln n}}-1
 \ge \frac1A\frac{d}{\sqrt{\ln d}}-1.
\tag{2.2}
\]

#### Proof
The first inequality follows directly from Lemma 2.1. Since \(n\ge d+1\) and \(x/\ln x\) is increasing for \(x>e\),
\[
\frac{n}{\ln n}\ge \frac{d}{\ln d}.
\]
Thus
\[
\sqrt{\frac{nd}{\ln n}}
 \ge \frac{d}{\sqrt{\ln d}}.
\]
\(\square\)

Consequently, the conjectured \(O(r\sqrt{\ln r})\) bound holds for any class of Hamiltonian graphs satisfying (2.1) with an absolute constant \(A\).

---

## 3. A planted-random Hamiltonian model

Fix a labelled \(n\)-cycle \(C_n\). Let \(G^\circ_{n,p}\) be obtained by taking all edges of \(C_n\) and then independently adding every edge of
\[
K_n-E(C_n)
\]
with probability \(p\), where \(p\in(0,1)\) is fixed. Put
\[
q=1-p,\qquad \rho=-\ln q.
\]

### Theorem 3.1
With probability tending to one,
\[
\delta(G^\circ_{n,p})=(p+o(1))n
\tag{3.1}
\]
and
\[
\left(\sqrt{\frac p2}-o(1)\right)\frac{n}{\sqrt{\ln n}}
\le
\operatorname{ch}(G^\circ_{n,p})
\le
h(G^\circ_{n,p})
\le
\left(\sqrt{\rho}+o(1)\right)\frac{n}{\sqrt{\ln n}}.
\tag{3.2}
\]

Thus, for fixed \(p\),
\[
\operatorname{ch}(G^\circ_{n,p})
=\Theta_p\!\left(\frac{\delta(G^\circ_{n,p})}
{\sqrt{\ln\delta(G^\circ_{n,p})}}\right).
\]

### Proof: minimum degree

For every vertex \(v\),
\[
d(v)=2+\operatorname{Bin}(n-3,p).
\]
A Chernoff bound followed by a union bound over all \(n\) vertices gives (3.1).

### Proof: cyclic-minor lower bound

Fix \(\eta>0\), and put
\[
s=\left\lceil\sqrt{\frac{(2+\eta)\ln n}{p}}\right\rceil .
\]

There are at most \(n^2\) pairs of \(C_n\)-intervals of exactly \(s\) vertices. If two such disjoint intervals are consecutive on \(C_n\), they are already joined by a cycle edge. Otherwise, all \(s^2\) possible edges between them are random, so the probability that they are anticomplete is at most
\[
(1-p)^{s^2}\le e^{-ps^2}\le n^{-(2+\eta)}.
\]
Hence
\[
\Pr\bigl(J_{C_n}(G^\circ_{n,p})>s\bigr)
 \le n^2n^{-(2+\eta)}
 =n^{-\eta}.
\]
Lemma 2.1 therefore gives, with high probability,
\[
\operatorname{ch}(G^\circ_{n,p})
 \ge \left\lfloor\frac ns\right\rfloor
 =
 \left(\sqrt{\frac{p}{2+\eta}}-o(1)\right)
 \frac{n}{\sqrt{\ln n}}.
\]
Letting \(\eta\downarrow0\) proves the first inequality in (3.2).

### Proof: ordinary-minor upper bound

Fix a constant \(A>\sqrt{\rho}\), and let
\[
t=\left\lceil A\frac{n}{\sqrt{\ln n}}\right\rceil.
\]
We show that, with high probability, there do not exist \(t\) pairwise disjoint nonempty sets
\[
B_1,\ldots,B_t
\]
such that every pair \(B_i,B_j\) is adjacent. This is stronger than excluding a \(K_t\)-minor, since connectivity of the \(B_i\) is not required.

Choose a sufficiently small fixed \(\alpha>0\) such that
\[
\lambda:=\frac{\rho}{A^2(1-\alpha)^2}<1.
\tag{3.3}
\]
For any such family \(B_1,\ldots,B_t\), at least \(\alpha t\) of the sets have size at most
\[
S:=\frac{n}{(1-\alpha)t}
 =
 (1+o(1))\frac{\sqrt{\ln n}}{A(1-\alpha)}.
\tag{3.4}
\]
Indeed, otherwise more than \((1-\alpha)t\) sets would each have more than \(S\) vertices, contradicting their disjointness.

Among the \(\binom{\alpha t}{2}\) pairs of small sets, at most \(n\) pairs are joined by an edge of the deterministic cycle \(C_n\). Since \(t^2\gg n\), there are \(\Omega(t^2)\) remaining pairs for which all possible joining edges are random.

For any such pair,
\[
\Pr(B_i\text{ and }B_j\text{ are adjacent})
 =1-q^{|B_i||B_j|}
 \le 1-q^{S^2}.
\]
The relevant edge sets for different unordered pairs \(\{i,j\}\) are disjoint, so these events are independent. From (3.3) and (3.4), after increasing \(\lambda\) slightly while retaining \(\lambda<1\),
\[
q^{S^2}=e^{-\rho S^2}\ge n^{-\lambda}
\]
for all sufficiently large \(n\). Thus the probability that a fixed family is pairwise adjacent is at most
\[
\exp\left(-\Omega\left(t^2n^{-\lambda}\right)\right)
=
\exp\left(-\Omega\left(\frac{n^{2-\lambda}}{\ln n}\right)\right).
\tag{3.5}
\]

There are at most
\[
(t+1)^n=\exp(O(n\ln n))
\]
ordered families of pairwise disjoint sets: assign each vertex one of the labels \(0,1,\ldots,t\), where label \(0\) means unused. Since \(\lambda<1\), the negative exponent in (3.5) dominates \(O(n\ln n)\). A union bound therefore shows that no such family exists with high probability.

Thus \(G^\circ_{n,p}\) has no \(K_t\)-minor with high probability. Since this holds for every fixed \(A>\sqrt{\rho}\), the upper bound in (3.2) follows. \(\square\)

---

## 4. A universal lower bound, with Hamiltonian witnesses

The upper half of Theorem 3.1 gives the usual random-graph lower-order obstruction, even after a Hamilton cycle is planted.

### Corollary 4.1
Let
\[
\beta=\max_{0<p<1}\frac{p}{\sqrt{-\ln(1-p)}}.
\]
Then
\[
f(r)\ge (\beta-o(1))r\sqrt{\ln r},
\tag{4.1}
\]
where
\[
\beta=0.638\ldots .
\]
Moreover, the witnessing graphs can be chosen Hamiltonian and without an ordinary \(K_r\)-minor.

#### Proof
Fix \(p\), write \(\rho=-\ln(1-p)\), and choose any
\[
c<\frac1{\sqrt{\rho}}.
\]
Set
\[
n=\left\lfloor c\,r\sqrt{\ln r}\right\rfloor.
\]
Choose \(A\) with
\[
\sqrt{\rho}<A<\frac1c.
\]
Then
\[
A\frac{n}{\sqrt{\ln n}}=(Ac+o(1))r<r.
\]
By the upper-bound argument in Theorem 3.1, with high probability \(G^\circ_{n,p}\) has no \(K_t\)-minor for
\[
t=\left\lceil A\frac{n}{\sqrt{\ln n}}\right\rceil.
\]
It consequently has no \(K_r\)-minor. On the other hand,
\[
\delta(G^\circ_{n,p})
=(p+o(1))n
=(pc+o(1))r\sqrt{\ln r}.
\]
Letting \(c\uparrow1/\sqrt{\rho}\) gives the coefficient
\[
\frac{p}{\sqrt{-\ln(1-p)}}.
\]
Finally optimize over \(p\).

The maximizing \(p\) is the nonzero solution of
\[
2(1-p)(-\ln(1-p))=p,
\]
numerically \(p=0.715\ldots\), yielding \(\beta=0.638\ldots\). The deterministic cycle makes every witness Hamiltonian. \(\square\)

This lower bound is not claimed as new relative to classical complete-minor extremal theory. Its relevance here is that it is self-contained and shows that Hamiltonicity alone does not permit a better order of magnitude.

---

## 5. Why the ordinary-minor theorem does not transfer automatically

There is no general conversion from an ordinary clique minor to a cyclic clique minor.

### Proposition 5.1
For every \(t\ge4\), the one-subdivision of \(K_t\) has an ordinary \(K_t\)-minor but no cyclic \(K_4\)-minor.

#### Proof
Let \(S_t\) be obtained by replacing every edge of \(K_t\) by a path of length two, using a distinct subdivision vertex for every edge. Suppressing the subdivision vertices gives an ordinary \(K_t\)-minor.

Every cycle in \(S_t\) is chordless. Indeed, every edge has a subdivision vertex as one endpoint. If a subdivision vertex \(x\) lies on a cycle, then both edges incident with \(x\) must be cycle edges because \(d(x)=2\). Hence every edge of \(S_t\) with both endpoints on the cycle is itself a cycle edge.

Contracting edges of a chordless cycle produces only another cycle, possibly with parallel edges in very small quotients. It cannot produce \(K_4\). Thus \(S_t\) has no cyclic \(K_4\)-minor. \(\square\)

The minimum degree of this example is only two, so it is not a counterexample to the conjecture. It does show that invoking the Kostochka–de la Vega ordinary-minor bound is insufficient without an additional high-minimum-degree argument.

Likewise, the interval-mixing condition is not automatic for an arbitrary Hamilton cycle. For example, take two copies of \(K_m\) and join them by two independent cross-edges. There is a Hamilton cycle consisting of a Hamilton path through each clique and the two cross-edges, but that cycle has two long anticomplete intervals. The graph nevertheless has a cyclic \(K_m\) inside either clique. Thus a universal proof would need a dichotomy: either find an interval-mixing cycle, or exploit the concentration of edges to find the cyclic clique locally.

## 6. Remaining gap

A proof of the conjecture would follow from a statement of roughly the following kind:

> Every graph of minimum degree \(d\) contains a Hamiltonian subgraph \(H\), with minimum degree comparable to \(d\), and a Hamilton cycle \(C\) satisfying
> \[
> J_C(H)=O\!\left(\sqrt{\frac{|V(H)|\ln |V(H)|}{d}}\right),
> \]
> or else already contains a cyclic clique of order \(\Omega(d/\sqrt{\ln d})\).

I have not proved such a structural dichotomy. In particular, the argument above gives no universal improvement over the source paper's \(O(r^2)\) upper bound.