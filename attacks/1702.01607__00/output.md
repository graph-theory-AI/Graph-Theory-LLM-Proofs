```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "There are S_i-free tournaments of domination number (1/3-o(1))2^i, and the conjecture reduces up to an additive one to prime tournaments.",
  "would_publish": false,
  "caveats": "No upper bound is obtained for i at least 4, and the literature novelty of the lower bound has not been checked."
}
```

# Mathematical writeup

## 1. Statement and conventions

Write \(x\to y\) when the arc is directed from \(x\) to \(y\). A set \(D\subseteq V(T)\) dominates \(T\) if every vertex outside \(D\) is beaten by some vertex of \(D\). Its minimum size is \(\gamma(T)\).

Fix the recursive orientation
\[
S_i=\Delta(A,B,c),\qquad
A,B\simeq S_{i-1},\qquad A\to B\to c\to A.
\]
Let
\[
F_i=1+\sup\{\gamma(T):T\text{ contains no }S_i\},
\]
with \(F_i=\infty\) if the supremum is unbounded. The conjecture is precisely that \(F_i<\infty\) for every \(i\).

I obtain two unconditional partial results:

1. For every \(i\ge 7\),
   \[
   F_i\ge
   \left\lfloor\frac{2^i-2}{3}\right\rfloor-3i+3
   =\left(\frac13-o(1)\right)2^i.
   \]
   Thus any possible forcing function must grow at least exponentially in \(i\).

2. Every tournament \(T\) with \(\gamma(T)\ge2\) contains a prime subtournament \(P\) satisfying
   \[
   \gamma(P)\ge\gamma(T)-1.
   \]
   Consequently, the conjecture is equivalent, up to an additive one in the threshold, to its restriction to prime tournaments.

Neither result supplies the required upper bound.

---

## 2. Coloring and transitive subsets of \(S_i\)

Recall that \(\vec\chi(T)\) is the minimum number of transitive subtournaments partitioning \(V(T)\).

### Lemma 2.1
For every \(i\ge1\),
\[
\vec\chi(S_i)=i.
\]

#### Proof

The upper bound follows inductively. Color the two copies \(A,B\simeq S_{i-1}\) with the same \(i-1\) colors. Since \(A\to B\), the union of corresponding color classes in \(A\) and \(B\) is transitive. Give \(c\) a new color.

For the lower bound, suppose \(S_i\) had an \((i-1)\)-coloring. Both \(A\) and \(B\) require all \(i-1\) colors by induction. Let \(c\) have color \(j\), and choose vertices \(a\in A\), \(b\in B\) of color \(j\). Then
\[
a\to b\to c\to a,
\]
contradicting transitivity of the color class. ∎

In particular, any tournament with \(\vec\chi(T)\le i-1\) is \(S_i\)-free.

We need a stronger quantitative property.

### Lemma 2.2
For \(0\le r\le i\), the largest order of a subtournament of \(S_i\) with chromatic number at most \(r\) is
\[
b_r(i)=2^i-2^{i-r}.
\]

#### Proof

The assertions for \(r=0\) and \(r=i\) are immediate. Induct on \(i\), and let \(1\le r\le i-1\).

Write \(S_i=\Delta(A,B,c)\). If an \(r\)-colorable set \(X\) does not contain \(c\), then
\[
|X|\le 2b_r(i-1)
   =2^i-2^{i-r}.
\]
This bound is attained: take maximum \(r\)-colorable subsets in \(A\) and \(B\), and use the same colors on both sides.

Suppose \(c\in X\). The color class containing \(c\) cannot meet both \(A\) and \(B\), since any \(a\in A,b\in B\) together with \(c\) induce a directed triangle. Thus one of \(X\cap A,X\cap B\) uses at most \(r-1\) colors, while the other uses at most \(r\) colors. Hence
\[
\begin{aligned}
|X|
&\le 1+b_{r-1}(i-1)+b_r(i-1)\\
&=2^i+1-2^{i-r}-2^{i-r-1}\\
&\le 2^i-2^{i-r},
\end{aligned}
\]
where the last inequality uses \(r\le i-1\). ∎

### Corollary 2.3: exact crossing-pair count

Let \(n=|S_i|=2^i-1\). Among all partitions
\[
V(S_i)=C_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}C_t
\]
into transitive sets, the minimum number of unordered pairs whose endpoints lie in different classes is
\[
\lambda_i=\frac{n(n-1)}3.
\]

#### Proof

Order the class sizes as \(s_1\ge s_2\ge\cdots\). The union of the \(r\) largest classes is \(r\)-colorable, so Lemma 2.2 gives
\[
\sum_{j=1}^r s_j\le 2^i-2^{i-r}\qquad(1\le r\le i).
\]
Thus the sequence \((s_j)\) is majorized by
\[
(2^{i-1},2^{i-2},\ldots,2,1).
\]
Convexity of \(x^2\) therefore yields
\[
\sum_j s_j^2\le
\sum_{r=0}^{i-1}4^r
=\frac{4^i-1}{3}.
\]
Consequently, the number of cross-class pairs is at least
\[
\frac{n^2-\sum_j s_j^2}{2}
\ge
\frac{n^2-(4^i-1)/3}{2}
=\frac{n(n-1)}3.
\]

Equality is attained by the canonical \(i\)-coloring from Lemma 2.1, whose class sizes are \(2^{i-1},2^{i-2},\ldots,1\). ∎

---

## 3. An exponential lower bound on any forcing function

We use a random tournament with a prescribed partition into transitive classes.

Fix integers \(k,m\). Partition the vertex set into \(k\) parts
\[
P_1,\ldots,P_k,\qquad |P_j|=m.
\]
Orient each \(P_j\) transitively, and orient all edges between different parts independently and uniformly at random. Let
\[
N=km.
\]

### Lemma 3.1
For fixed \(k\), and sufficiently large \(m\), this random tournament has domination number \(k\) with positive probability.

#### Proof

Choosing the source of each transitive part gives a dominating set of size \(k\), so always
\[
\gamma(T)\le k.
\]

Let \(D\) be any set of size \(r\le k-1\). Some part \(P_j\) is disjoint from \(D\). For a fixed \(v\in P_j\), all edges between \(v\) and \(D\) are independent random cross-edges, and
\[
\Pr(v\to D)=2^{-r}.
\]
These events are independent as \(v\) ranges over \(P_j\). Hence
\[
\Pr(D\text{ dominates }T)
\le (1-2^{-r})^m
\le \exp(-m/2^{k-1}).
\]
There are at most \(kN^{k-1}\) sets of order at most \(k-1\), so
\[
\Pr(\gamma(T)<k)
\le kN^{k-1}\exp(-m/2^{k-1}),
\]
which tends to zero as \(m\to\infty\). ∎

This already gives the elementary lower bound \(F_i\ge i\): take \(k=i-1\). The resulting tournament has
\[
\gamma(T)=\vec\chi(T)=i-1
\]
and hence is \(S_i\)-free by Lemma 2.1.

To obtain an exponential bound, \(k\) is allowed to be much larger than \(i\), and the absence of \(S_i\) is established probabilistically.

### Theorem 3.2
For every \(i\ge7\), there exists an \(S_i\)-free tournament \(T\) with
\[
\gamma(T)=
\left\lfloor\frac{2^i-2}{3}\right\rfloor-3i+2.
\]

#### Proof

Put
\[
n=2^i-1,\qquad
q=\frac{n-1}{3}=\frac{2^i-2}{3},
\]
and define
\[
k=\lfloor q\rfloor-3i+2.
\]
For \(i\ge7\), one has \(k\ge23\). Set
\[
m=2^k k^2,\qquad N=km=2^k k^3.
\]

First consider domination. By Lemma 3.1 and its displayed bound,
\[
\Pr(\gamma(T)<k)
\le kN^{k-1}e^{-2k^2},
\]
since \(m/2^{k-1}=2k^2\). For \(k\ge16\), using
\[
\ln k\le k/4,\qquad \ln2<0.7,
\]
we have
\[
\ln N=k\ln2+3\ln k<1.45k.
\]
Thus
\[
\ln\!\big(kN^{k-1}\big)<1.5k^2,
\]
and therefore
\[
\Pr(\gamma(T)<k)<e^{-k^2/2}<\frac14.
\]

Now count embeddings of \(S_i\). Fix an injection
\[
\phi:V(S_i)\longrightarrow V(T).
\]
The inverse images of the parts \(P_j\) partition \(V(S_i)\). If \(\phi\) is an embedding, each nonempty inverse image must be transitive. By Corollary 2.3, at least
\[
\lambda_i=\frac{n(n-1)}3=nq
\]
pairs of vertices of \(S_i\) are mapped to different parts. The corresponding host edges are independent fair random bits. Hence
\[
\Pr(\phi\text{ is an embedding})\le 2^{-\lambda_i}.
\]
There are at most \(N^n\) injections, so the expected number \(X\) of labeled copies satisfies
\[
\mathbb E X\le N^n2^{-\lambda_i}.
\]

Because \(k<q<2^{i-1}\), we have \(\log_2 k<i-1\), and consequently
\[
\begin{aligned}
\log_2N
 &=k+3\log_2k\\
 &<\lfloor q\rfloor-3i+2+3(i-1)\\
 &=\lfloor q\rfloor-1\\
 &\le q-1.
\end{aligned}
\]
It follows that
\[
\mathbb E X
\le 2^{n(q-1)-nq}
=2^{-n}<\frac14.
\]
Therefore
\[
\Pr(T\text{ contains }S_i)<\frac14.
\]

With positive probability neither bad event occurs. For such a realization, \(T\) is \(S_i\)-free and has \(\gamma(T)\ge k\). The sources of the \(k\) transitive parts dominate \(T\), so \(\gamma(T)=k\). ∎

### Consequence

Any integer \(f(i)\) with the asserted forcing property must satisfy, for \(i\ge7\),
\[
\boxed{
f(i)\ge
\left\lfloor\frac{2^i-2}{3}\right\rfloor-3i+3.
}
\]

This is finite for each fixed \(i\), so it is not a counterexample to the conjecture.

### A small calibration at \(i=3\)

The quadratic-residue tournament \(P_7\) on \(\mathbb Z_7\), with
\[
x\to y\iff y-x\in\{1,2,4\},
\]
has \(\gamma(P_7)=3\). Indeed, every pair has a common vertex beating both; for \(\{0,1\}\), vertex \(6\) is such a vertex, and the automorphisms of \(P_7\) handle all pairs. On the other hand, \(\{0,1,2\}\) dominates \(P_7\).

The tournament \(P_7\) is regular, whereas \(S_3\) has outdegree sequence
\[
(4,4,4,3,2,2,2).
\]
Thus \(P_7\not\simeq S_3\), and since both have seven vertices, \(P_7\) is \(S_3\)-free. Hence \(F_3\ge4\).

---

## 4. Reduction to prime tournaments

A set \(M\subseteq V(T)\) is a module if every vertex outside \(M\) is either complete to \(M\) or complete from \(M\). A tournament is prime if its only modules are the singletons and the whole vertex set.

We use the standard modular-decomposition fact for tournaments:

> Every tournament of order at least two admits a partition into modules whose quotient is either transitive or prime. If the quotient is transitive, its source block is canonical; recursively decomposing that block either reaches a singleton or reaches a node with prime quotient.

This follows by taking maximal proper strong modules. They partition the vertex set, and contraction gives either a prime quotient or a transitive quotient. The usual proof uses the facts that overlapping modules have modular intersection, union and differences, and that a tournament with no nontrivial strong module is either prime or transitive.

We need one elementary domination observation.

### Lemma 4.1
Let \(Q\) be a tournament with no source. Then \(Q\) has a dominating set \(D^+\) of size at most \(\gamma(Q)+1\) such that every vertex of \(D^+\) is beaten by another vertex of \(D^+\).

#### Proof

Let \(D\) be a minimum dominating set.

If \(Q[D]\) has no source, take \(D^+=D\). Otherwise, let \(s\) be the source of \(Q[D]\). Since \(Q\) has no source, choose \(x\) with \(x\to s\). Necessarily \(x\notin D\). Since \(D\) dominates \(x\), some \(d\in D\) satisfies \(d\to x\), and \(d\ne s\).

Now in \(D\cup\{x\}\):

- \(x\to s\);
- \(d\to x\);
- \(s\to y\) for every \(y\in D\setminus\{s\}\).

Thus every selected vertex is beaten by another selected vertex. ∎

### Lemma 4.2
Suppose \(T\) is obtained by substituting nonempty tournaments \(T_v\) for the vertices \(v\) of a source-free quotient \(Q\). Then
\[
\gamma(T)\le\gamma(Q)+1.
\]

#### Proof

Take \(D^+\) from Lemma 4.1 and choose one arbitrary representative from each block \(T_v\), \(v\in D^+\).

If \(w\notin D^+\), some \(v\in D^+\) satisfies \(v\to w\), so the representative in \(T_v\) beats every vertex of \(T_w\). If \(w\in D^+\), the additional property of \(D^+\) again supplies some \(v\in D^+\) with \(v\to w\). Thus the chosen representatives dominate all of \(T\). ∎

If instead the quotient is transitive with source block \(T_s\), then
\[
\gamma(T)=\gamma(T_s).
\]
Indeed, a dominating set inside \(T_s\) dominates every other block, while no vertex outside \(T_s\) can dominate any vertex of \(T_s\).

### Theorem 4.3: prime-core lemma
Every tournament \(T\) with \(\gamma(T)\ge2\) contains a prime subtournament \(P\) such that
\[
\gamma(P)\ge\gamma(T)-1.
\]

#### Proof

Follow the source block whenever the modular quotient is transitive. Domination number is unchanged at each such step. Since \(\gamma(T)\ge2\), this process cannot terminate at a singleton; it eventually reaches a substitution whose quotient \(P\) is prime.

A prime tournament of order at least three has no source: if \(s\) were a source, then \(V(P)\setminus\{s\}\) would be a nontrivial module. Hence Lemma 4.2 applies:
\[
\gamma(T)\le\gamma(P)+1.
\]
Choosing one representative from each module realizes \(P\) as an induced subtournament of \(T\), proving the assertion. ∎

### Corollary 4.4
For every hereditary class \(\mathcal C\), let
\[
g(\mathcal C)=\sup\{\gamma(T):T\in\mathcal C\},
\]
and let \(p(\mathcal C)\) be the corresponding supremum over prime members. Then
\[
p(\mathcal C)\le g(\mathcal C)\le\max\{1,p(\mathcal C)+1\}.
\]

In particular, the original conjecture holds for \(S_i\) if and only if domination number is bounded among prime \(S_i\)-free tournaments.

Applying Theorem 4.3 to the probabilistic examples above also gives, for every \(i\ge7\), a prime \(S_i\)-free tournament \(P\) with
\[
\gamma(P)\ge
\left\lfloor\frac{2^i-2}{3}\right\rfloor-3i+1.
\]
Thus the exponential lower bound persists even in the prime case.

---

## 5. A structural fact about any hypothetical counterexample

For \(A\subseteq V(T)\), define its common in-neighborhood
\[
U(A)=\{x\in V(T)\setminus A:x\to A\}.
\]

### Lemma 5.1
\[
\gamma(T)\le |A|+\gamma(T[U(A)]).
\]

#### Proof

The set \(A\) dominates every vertex outside \(A\cup U(A)\). Add a dominating set of \(T[U(A)]\). ∎

Consequently,
\[
\gamma(T[U(A)])\ge\gamma(T)-|A|.
\]

Suppose a fixed tournament \(H\) is already known to be forced by domination number at least \(c\). Repeatedly applying Lemma 5.1 shows that sufficiently large domination number forces arbitrarily long sequences of disjoint copies
\[
H_r\to H_{r-1}\to\cdots\to H_1.
\]
For \(H=S_{i-1}\), an \(S_i\) would arise if, for some \(a<b\), there were a vertex \(v\) with
\[
H_a\to v\to H_b,
\]
because then
\[
H_b\to H_a\to v\to H_b.
\]

Thus, for \(i=4\), the known \(S_3\) case implies that any hypothetical sequence of \(S_4\)-free tournaments with unbounded domination number contains arbitrarily long chains of \(S_3\)-blocks, but every possible cyclic “middle” vertex between two blocks must fail at least one of the required uniform adjacency conditions.

This is the unresolved point: large domination naturally creates vertices and blocks that beat all previously chosen material, while \(S_i\) requires a cyclic return edge.

---

## 6. Conclusion and gap

The conjecture remains open for every \(i\ge4\). The results above establish:

- an unconditional exponential lower bound
  \[
  F_i\ge \frac{2^i}{3}-O(i);
  \]
- the exact transitive-partition crossing parameter
  \[
  \lambda(S_i)=\frac{(2^i-1)(2^i-2)}3;
  \]
- and a reduction of the conjecture to prime tournaments, losing at most one in domination number.

What is still missing is any bound on the domination number of prime \(S_i\)-free tournaments. The probabilistic construction shows that such a bound, if it exists, cannot be smaller than \((1/3-o(1))2^i\).