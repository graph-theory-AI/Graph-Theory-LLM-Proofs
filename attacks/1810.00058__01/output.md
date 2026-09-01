```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The triangle case is not resolved, but a quantitative no-hole lemma proves it for polynomially sublinear-codegree families and for triangle-free strongly regular graphs.",
  "would_publish": false,
  "caveats": "The biclique-rich, near-linear common-neighborhood regime remains unresolved; these elementary partial results may already be known."
}
```

## 1. Formulation

For a graph \(G\) and \(X\subseteq V(G)\), write
\[
N(X)=\{v\in V(G)\setminus X: v\text{ has a neighbor in }X\}.
\]
Thus \(X\) and \(V(G)\setminus(X\cup N(X))\) are anticomplete.

The \(K_3\) case asks whether there is an absolute \(\varepsilon>0\) such that every triangle-free \(n\)-vertex graph satisfies at least one of

\[
\Delta(G)\ge \varepsilon n,
\]
or
\[
\exists\,A,B\subseteq V(G),\qquad
|A|\ge \varepsilon n^\varepsilon,\quad |B|\ge \varepsilon n,
\quad E(A,B)=\varnothing.
\tag{C}
\]

I do not prove or disprove (C). The main partial result below describes what a counterexample would have to contain and resolves several substantial special regimes.

---

## 2. A quantitative common-neighborhood hierarchy

Call \((A,B)\) an \((a,b)\)-hole if \(A,B\) are disjoint and anticomplete, with \(|A|\ge a\) and \(|B|\ge b\).

### Lemma 2.1

Let \(G\) be a triangle-free graph on \(n\ge 8\) vertices. Let \(a,b\) be positive integers with
\[
a+b\le \frac n4.
\]
Suppose that \(G\) has no \((a,b)\)-hole. Then:

1. Fewer than \(a\) vertices have degree at most
   \[
   \frac{n-a-b}{a}.
   \tag{2.1}
   \]

2. For every positive integer \(r\) satisfying
   \[
   (2a)^r\le n,
   \tag{2.2}
   \]
   the graph \(G\) contains a complete bipartite subgraph with parts \(Q_r,S_r\), where
   \[
   |Q_r|=r,\qquad |S_r|\ge \frac{n}{(2a)^r}.
   \tag{2.3}
   \]
   Both \(Q_r\) and \(S_r\) are stable sets.

#### Proof

Since there is no \((a,b)\)-hole, every \(a\)-vertex set \(X\) satisfies
\[
|N(X)|\ge n-a-b+1.
\tag{2.4}
\]

For part 1, suppose that \(a\) vertices all have degree at most \((n-a-b)/a\), and let \(X\) be this set. Then
\[
|N(X)|\le \sum_{x\in X}d(x)\le n-a-b,
\]
contradicting (2.4).

For part 2, choose \(q_1\) with
\[
d(q_1)>\frac{n-a-b}{a}\ge \frac{n}{2a},
\]
and put
\[
Q_1=\{q_1\},\qquad S_1=N(q_1).
\]
Because \(G\) is triangle-free, \(S_1\) is stable.

Suppose inductively that \(Q_i\) and \(S_i\) are stable, every vertex of \(Q_i\) is adjacent to every vertex of \(S_i\), and
\[
|Q_i|=i,\qquad m_i:=|S_i|\ge \frac{n}{(2a)^i}.
\tag{2.5}
\]
Assume \(i<r\). Condition (2.2) gives \(m_i\ge 2a\), so choose a uniformly random \(a\)-subset \(X\) of \(S_i\).

For \(z\notin Q_i\), put
\[
r_z=|N(z)\cap S_i|,
\qquad
R=\max_{z\notin Q_i}r_z.
\]
By the union bound,
\[
\Pr(z\in N(X))\le \frac{a r_z}{m_i}\le \frac{aR}{m_i}.
\]
All \(i\) vertices of \(Q_i\) lie in \(N(X)\). Hence
\[
\mathbb E|N(X)|
   \le i+(n-i)\frac{aR}{m_i}.
\tag{2.6}
\]
On the other hand, (2.4) gives \(|N(X)|\ge n-a-b+1\) for every choice of \(X\).

Because \(i\le r-1\le \log_2 n-1\le n/4\) and \(a+b\le n/4\), comparison with (2.6) yields
\[
R\ge \frac{m_i}{2a}.
\]
Choose \(q_{i+1}\notin Q_i\) attaining \(R\), and set
\[
Q_{i+1}=Q_i\cup\{q_{i+1}\},
\qquad
S_{i+1}=S_i\cap N(q_{i+1}).
\]
Then
\[
|S_{i+1}|\ge \frac{m_i}{2a}\ge \frac{n}{(2a)^{i+1}}.
\]

Moreover, \(S_{i+1}\) is stable because it is a subset of \(S_i\). It is nonempty, and if \(q_{i+1}\) were adjacent to some \(q\in Q_i\), any vertex of \(S_{i+1}\) would complete a triangle with \(q,q_{i+1}\). Thus \(Q_{i+1}\) is stable. By construction all edges between \(Q_{i+1}\) and \(S_{i+1}\) are present. This completes the induction. ∎

---

## 3. Polynomially sublinear codegree

The hierarchy immediately gives a useful quantitative special case.

### Corollary 3.1

Let \(r\ge2\), \(t\ge1\), and \(n\ge 8^r t\). If an \(n\)-vertex triangle-free graph \(G\) contains no \(K_{r,t}\) as a subgraph, then it has anticomplete sets \(A,B\) satisfying
\[
|A|\ge \left\lfloor \frac14\left(\frac nt\right)^{1/r}\right\rfloor,
\qquad
|B|\ge \left\lfloor\frac n8\right\rfloor.
\tag{3.1}
\]

#### Proof

Set
\[
a=\left\lfloor \frac14\left(\frac nt\right)^{1/r}\right\rfloor,
\qquad
b=\left\lfloor\frac n8\right\rfloor.
\]
The numerical hypotheses ensure \(a+b\le n/4\). If there were no \((a,b)\)-hole, Lemma 2.1 would produce a \(K_{r,m}\) with
\[
m\ge \frac{n}{(2a)^r}\ge 2^r t\ge t,
\]
contrary to the \(K_{r,t}\)-free assumption. ∎

Let
\[
\mu(G)=\max_{x\ne y}|N(x)\cap N(y)|
\]
be the maximum codegree. Taking \(r=2\) and \(t=\mu(G)+1\) gives:

### Corollary 3.2

For every fixed \(\eta>0\), if \(G\) is triangle-free and
\[
\mu(G)\le n^{1-\eta},
\]
then, for all sufficiently large \(n\), \(G\) has anticomplete sets satisfying
\[
|A|=\Omega(n^{\eta/2}),
\qquad
|B|\ge \frac n9.
\tag{3.2}
\]

Thus the desired conjecture holds, with room to spare, for every family of triangle-free graphs with polynomially sublinear maximum codegree. In particular:

- triangle-free \(C_4\)-free graphs have \(|A|=\Omega(\sqrt n)\) and \(|B|=\Omega(n)\);
- more generally, the same conclusion is \(|A|=\Omega(\sqrt{n/t})\) when every pair has fewer than \(t\) common neighbors.

The condition allows \(t=t(n)\) to grow polynomially, so this is stronger than merely imposing one fixed forbidden biclique.

---

## 4. What a counterexample must look like

Fix \(0<\varepsilon<1/8\), and put
\[
a=\left\lceil \varepsilon n^\varepsilon\right\rceil,
\qquad
b=\left\lceil \varepsilon n\right\rceil.
\]
Suppose a triangle-free graph has neither outcome in (C). For sufficiently large \(n\), Lemma 2.1 implies:

1. All but \(O(n^\varepsilon)\) vertices have degree
   \[
   d(v)>
   \frac{n-a-b}{a}
   =
   \left(\frac{1-\varepsilon+o(1)}{\varepsilon}\right)n^{1-\varepsilon}.
   \tag{4.1}
   \]

2. For every fixed \(r\) with \(r\varepsilon<1\), there are stable sets \(Q_r,S_r\), complete to one another, such that
   \[
   |Q_r|=r,\qquad
   |S_r|=\Omega_{\varepsilon,r}\!\left(n^{1-r\varepsilon}\right).
   \tag{4.2}
   \]

3. In particular,
   \[
   \mu(G)=\Omega_\varepsilon(n^{1-2\varepsilon}).
   \tag{4.3}
   \]

4. Since every neighborhood in a triangle-free graph is stable,
   \[
   \alpha(G)=\Omega_\varepsilon(n^{1-\varepsilon}).
   \]
   On the other hand, an independent set of size at least \(a+b\) could be split into an \((a,b)\)-hole, so
   \[
   \alpha(G)<a+b=\varepsilon n+O(n^\varepsilon).
   \tag{4.4}
   \]

Thus a counterexample cannot resemble the usual low-codegree triangle-free Ramsey constructions. It must have successive large common neighborhoods on the scales
\[
n^{1-\varepsilon},\quad n^{1-2\varepsilon},\quad
n^{1-3\varepsilon},\ldots
\]
while still having maximum degree below \(\varepsilon n\). The lemma does not contradict such a configuration: complete bipartite structures are compatible with triangle-freeness. This is exactly where the argument stops.

---

## 5. Strongly regular triangle-free graphs

There is also a separate spectral special case covering graphs with very large and highly uniform codegrees.

### Proposition 5.1

Every triangle-free strongly regular graph on \(n\) vertices has anticomplete sets \(A,B\) with
\[
|A|=\Omega(n^{1/6}),\qquad |B|=\Omega(n).
\tag{5.1}
\]

#### Proof for the primitive case

Let the parameters be \((n,k,0,\mu)\). Counting edges from \(N(v)\) to the nonneighbors of \(v\) gives
\[
(n-k-1)\mu=k(k-1).
\tag{5.2}
\]

Let the two nonprincipal eigenvalues be
\[
\rho>0>\theta.
\]
They satisfy
\[
\rho+\theta=-\mu,\qquad
\rho\theta=\mu-k,
\]
or equivalently
\[
\rho(\rho+\mu)=k-\mu.
\tag{5.3}
\]
Let \(g\) be the multiplicity of \(\theta\). From the trace equations,
\[
g=\frac{k+(n-1)\rho}{\rho-\theta}
  =\frac{k+(n-1)\rho}{2\rho+\mu}.
\tag{5.4}
\]

We need the standard absolute bound, whose short proof is included. Project the coordinate vectors onto the \(\theta\)-eigenspace and normalize them. In a primitive strongly regular graph this gives \(n\) distinct unit vectors in \(\mathbb R^g\) having two possible inner products between distinct vectors. If these inner products are \(\alpha,\beta\), the polynomials
\[
p_i(x)=(\langle x,x_i\rangle-\alpha)
       (\langle x,x_i\rangle-\beta)
\]
are linearly independent when restricted to the \(n\) points. Restricted to the unit sphere, quadratic polynomials in \(g\) variables form a space of dimension at most
\[
\binom{g+2}{2}-1=\frac{g(g+3)}2.
\]
Consequently
\[
n\le \frac{g(g+3)}2.
\tag{5.5}
\]
In particular, for \(n\ge16\),
\[
g\ge \frac{\sqrt n}{2}.
\tag{5.6}
\]

From (5.2),
\[
\mu\ge \frac{k^2}{2n}
\]
when \(k\ge2\). Equation (5.3) gives \(\rho\le k/\mu\). Therefore (5.4) yields
\[
g
\le \frac{k+n\rho}{\mu}
\le \frac{k}{\mu}+\frac{nk}{\mu^2}
\le 2\frac nk+4\left(\frac nk\right)^3
\le 6\left(\frac nk\right)^3.
\]
Together with (5.6), this implies
\[
k\le 12^{1/3}n^{5/6}.
\tag{5.7}
\]

Now choose any set \(A\) of size
\[
\left\lfloor\frac{n}{4(k+1)}\right\rfloor.
\]
Its closed neighborhood has size at most \(|A|(k+1)\le n/4\). Thus
\[
B=V(G)\setminus(A\cup N(A))
\]
has size at least \(3n/4\), and (5.7) gives \(|A|=\Omega(n^{1/6})\).

The imprimitive strongly regular cases are direct. A disconnected strongly regular graph is a disjoint union of equal cliques; triangle-freeness restricts these cliques to size at most two. If the complement is disconnected, the graph is complete multipartite, and triangle-freeness permits at most two parts. In each case there is a stable set of size at least \(n/2\), which can be split into two linear anticomplete sets. ∎

Hence the triangle conjecture is valid on the entire class of strongly regular triangle-free graphs.

---

## 6. Remaining gap

The argument does not handle graphs in which:

- degrees are at least on the scale \(n^{1-\varepsilon}\) but below \(\varepsilon n\);
- codegrees are at least \(n^{1-2\varepsilon}\);
- higher common neighborhoods continue on the scales \(n^{1-r\varepsilon}\);
- these biclique structures do not coalesce into a linear stable set or a polynomial-by-linear anticomplete pair.

No contradiction with triangle-freeness is presently obtained from that hierarchy. Consequently this is a genuine partial result, not a proof of the catalogued conjecture.