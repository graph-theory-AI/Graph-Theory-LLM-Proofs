```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any polynomial bound for a k-vertex tree must have degree at least floor(k/2) when k >= 5; I also give a sharp-exponent proof for the claw, but no general upper bound.",
  "would_publish": false,
  "caveats": "These are standard Ramsey-type partial results, not a claimed new resolution; the catalog's later references were not independently verified."
}
```

# Necessary exponents and a sharp special case

All graphs below are finite and simple. Write \(\omega(G)\), \(\alpha(G)\), and \(\chi(G)\) for the clique, independence, and chromatic numbers.

The question is whether, for every fixed tree \(T\), there are constants \(C_T,d_T\) such that
\[
\chi(G)\le C_T\omega(G)^{d_T}
\tag{1}
\]
for every graph \(G\) with no induced copy of \(T\).

I do not establish (1) for arbitrary \(T\). The rigorous outcomes below are:

* a general lower bound on any possible exponent \(d_T\);
* an elementary polynomial upper bound for stars, with the optimal exponent for the claw;
* an obstruction to extending the star proof by a degree or degeneracy argument.

No novelty is claimed for these partial results.

## 1. A necessary exponent for every tree

For a graph \(F\), define
\[
m_2(F)=
\max_{\substack{J\subseteq F\\ |V(J)|\ge3}}
\frac{|E(J)|-1}{|V(J)|-2},
\]
where \(J\subseteq F\) means an ordinary, not necessarily induced, subgraph. Set
\[
\lambda(T)=\max\{1,m_2(\overline T)\}.
\]

### Proposition 1
Let \(T\) be a tree with at least three vertices. There is a constant \(c_T>0\) such that, for every sufficiently large integer \(t\), some induced-\(T\)-free graph \(G\) satisfies
\[
\omega(G)<t,
\qquad
\chi(G)\ge c_T\left(\frac{t}{\log t}\right)^{\lambda(T)}.
\tag{2}
\]
Consequently, any exponent \(d_T\) satisfying (1) must obey
\[
d_T\ge \lambda(T).
\tag{3}
\]

The proof uses the following probabilistic lemma, whose details are included to make the lower bound independent of unverified literature.

### Lemma 2
Let \(F\) have \(h\ge3\) vertices and \(q\) edges, and suppose
\[
\rho=\frac{q-1}{h-2}>1.
\]
There is \(c_F>0\) such that, for every sufficiently large integer \(t\), there exists a graph \(R\) with
\[
|V(R)|\ge c_F\left(\frac{t}{\log t}\right)^\rho,
\]
containing neither an ordinary copy of \(F\) nor an independent set of size \(t\).

#### Proof
We use the asymmetric Lovász local lemma: if events \(E_i\), with a dependency graph, have weights \(z_i\in(0,1)\) satisfying
\[
\Pr(E_i)\le z_i\prod_{j\in\Gamma(i)}(1-z_j),
\]
then with positive probability none of the events occurs.

Put \(K=2q^2\), and choose a constant \(a>0\) sufficiently small that
\[
4Ka^{q-1}\le \frac1{16}.
\]
For large \(n\), set
\[
p=a n^{-1/\rho},
\qquad
r=\left\lceil 16p^{-1}\log n\right\rceil.
\]
Since \(\rho>1\), we have \(r<n\) for sufficiently large \(n\).

Consider the random graph \(R\sim G(n,p)\). The bad events are:

* \(A_\phi\): a specified injective map \(\phi:V(F)\to[n]\) maps every edge of \(F\) to an edge;
* \(B_S\): a specified \(r\)-element set \(S\) is independent.

Their probabilities are
\[
\Pr(A_\phi)=p^q,
\qquad
\Pr(B_S)=(1-p)^{\binom r2}.
\]

Two events are joined in the dependency graph when they use a common edge variable. A fixed edge variable occurs in at most \(2q n^{h-2}\) events of type \(A\). Thus:

* an \(A\)-event has at most \(Kn^{h-2}\) neighbours of type \(A\);
* a \(B\)-event has at most \(Kr^2n^{h-2}\) neighbours of type \(A\);
* every event has at most \(M=\binom nr\) neighbours of type \(B\).

Assign weights
\[
x=2p^q\quad\text{to the \(A\)-events},\qquad
y=\exp(-pr^2/4)\quad\text{to the \(B\)-events}.
\]
For large \(n\), both weights are at most \(1/2\). Also,
\[
My
\le
\exp\left(r\log\frac{en}{r}-\frac{pr^2}{4}\right)
\le \exp(-2r\log n),
\tag{4}
\]
using \(pr\ge16\log n\) and \(\log(en/r)\le2\log n\).

The defining choice of \(\rho\) gives
\[
n^{h-2}p^{q-1}=a^{q-1}.
\tag{5}
\]
Using \(1-z\ge e^{-2z}\) for \(0\le z\le1/2\), the local-lemma right-hand side for an \(A\)-event is at least
\[
\begin{aligned}
x(1-x)^{Kn^{h-2}}(1-y)^M
&\ge 2p^q
   \exp\left(-4Kn^{h-2}p^q-2My\right)\\
&=2p^q
   \exp\left(-4Ka^{q-1}p-2My\right)\\
&\ge p^q
\end{aligned}
\]
for sufficiently large \(n\).

For a \(B\)-event, the right-hand side is at least
\[
\begin{aligned}
y(1-x)^{Kr^2n^{h-2}}(1-y)^M
&\ge
\exp\left(-\frac{pr^2}{4}
          -4Ka^{q-1}pr^2-2My\right)\\
&\ge \exp(-3pr^2/8)
\end{aligned}
\]
for sufficiently large \(n\), by (4) and the choice of \(a\). On the other hand, for \(r\ge4\),
\[
\Pr(B_S)
\le \exp\left(-\frac{pr(r-1)}2\right)
\le \exp(-3pr^2/8).
\]
All local-lemma inequalities therefore hold.

We obtain an \(n\)-vertex graph containing no copy of \(F\) and with
\[
\alpha(R)<r=O_F(n^{1/\rho}\log n).
\]
Taking \(n\) to be a sufficiently small constant multiple of
\((t/\log t)^\rho\) ensures \(r\le t\), proving the lemma. \(\square\)

### Proof of Proposition 1
First suppose \(\mu=m_2(\overline T)>1\). Choose \(J\subseteq\overline T\) attaining this maximum, and let \(h=|V(J)|\).

Apply Lemma 2 to \(J\), obtaining a \(J\)-free graph \(R\) with
\[
|V(R)|\ge c\left(\frac{t}{\log t}\right)^\mu,
\qquad
\alpha(R)<t.
\]
Let \(G=\overline R\).

An induced copy of \(T\) in \(G\) would give a copy of \(\overline T\), and hence an ordinary copy of \(J\), in \(R\). Thus \(G\) is induced-\(T\)-free. Moreover,
\[
\omega(G)=\alpha(R)<t.
\]
Since \(K_h\) contains \(J\) as an ordinary subgraph, \(R\) has no \(K_h\). Consequently,
\[
\alpha(G)=\omega(R)\le h-1,
\]
and hence
\[
\chi(G)\ge \frac{|V(G)|}{\alpha(G)}
\ge \frac{c}{h-1}\left(\frac{t}{\log t}\right)^\mu.
\]

If \(m_2(\overline T)\le1\), use \(G=K_{t-1}\). Every tree with at least three vertices has a nonedge, so this graph is induced-\(T\)-free and gives the required lower bound with exponent \(1\).

Finally, for \(d<\lambda(T)\), the graphs in (2) satisfy
\[
\frac{\chi(G)}{\omega(G)^d}
\ge
c_T\frac{t^{\lambda(T)-d}}{(\log t)^{\lambda(T)}}
\longrightarrow\infty.
\]
This proves (3). \(\square\)

## 2. Consequences in terms of the order of the tree

Let \(T\) have \(k\ge5\) vertices. Its complement has
\[
|E(\overline T)|
=\binom{k}{2}-(k-1)
=\frac{(k-1)(k-2)}2.
\]
Taking \(J=\overline T\) gives
\[
\lambda(T)\ge
\frac{|E(\overline T)|-1}{k-2}
=
\frac{k-1}{2}-\frac1{k-2}.
\tag{6}
\]

Thus any real exponent in (1) must satisfy
\[
\boxed{\displaystyle
d_T\ge \frac{k-1}{2}-\frac1{k-2}.}
\]
In particular, the degree of an ordinary polynomial \(\chi\)-bound must be at least
\[
\boxed{\left\lfloor\frac{k}{2}\right\rfloor
\qquad(k\ge5).}
\]

For example, there are induced-\(P_6\)-free graphs with
\[
\omega(G)<t,
\qquad
\chi(G)\ge c\left(\frac{t}{\log t}\right)^{9/4}.
\]
Therefore a quadratic \(\chi\)-bound is impossible even for \(P_6\)-free graphs.

One can improve (6) for some trees by taking proper subgraphs of \(\overline T\). Explicitly,
\[
m_2(\overline T)
=
\max_{\substack{U\subseteq V(T)\\|U|\ge3}}
\left(
\frac{|U|+1}{2}
-\frac{|E(T[U])|}{|U|-2}
\right).
\tag{7}
\]
Indeed, for a fixed vertex set \(U\), taking every available edge of \(\overline T[U]\) maximizes the defining ratio.

These bounds do **not** contradict the conjecture: the permitted degree depends on \(T\), and the lower bound is finite for each fixed \(T\).

## 3. Polynomial upper bounds for stars

Here is a completely proved benchmark.

### Proposition 3
If \(G\) contains no induced \(K_{1,s}\), where \(s\ge2\), then
\[
\chi(G)\le
\binom{\omega(G)+s-2}{s-1}.
\tag{8}
\]

#### Proof
Assume \(G\) is nonempty and put \(w=\omega(G)\). For every vertex \(v\),

* \(G[N(v)]\) has no independent set of size \(s\), since such a set together with \(v\) would induce \(K_{1,s}\);
* \(G[N(v)]\) has no clique of size \(w\), since adding \(v\) would give a clique of size \(w+1\).

Let \(R(a,b)\) denote the least integer such that every graph of that order has an independent set of size \(a\) or a clique of size \(b\). The elementary Ramsey recurrence gives
\[
R(a,b)\le \binom{a+b-2}{a-1}.
\]
Therefore
\[
\deg(v)\le R(s,w)-1
\le \binom{s+w-2}{s-1}-1.
\]
Greedy colouring yields (8). \(\square\)

### The claw has optimal polynomial exponent \(2\)

For \(T=K_{1,3}\), Proposition 3 gives
\[
\chi(G)\le \binom{\omega(G)+1}{2}.
\tag{9}
\]
The complement of the claw contains \(K_3\), and
\[
m_2(K_3)=2.
\]
Proposition 1 therefore gives claw-free graphs with
\[
\omega(G)<t,
\qquad
\chi(G)\ge c\left(\frac{t}{\log t}\right)^2.
\tag{10}
\]
Together, (9) and (10) show that the optimal polynomial exponent for claw-free graphs is exactly \(2\): an exponent \(2\) works, and every exponent below \(2\) fails.

## 4. The gap in extending this approach

The star argument bounds maximum degree by applying Ramsey theory inside a neighbourhood. This strategy cannot extend to a degree or degeneracy bound for arbitrary forbidden trees.

Every non-star tree contains an induced \(P_4\). But \(K_{n,n}\) is \(P_4\)-free, and hence induced-\(T\)-free for every non-star tree \(T\), while
\[
\omega(K_{n,n})=\chi(K_{n,n})=2,
\qquad
\delta(K_{n,n})=n.
\]
Its degeneracy is also \(n\). Thus, for non-star trees, neither minimum degree nor degeneracy can be bounded by any function of the clique number in the entire induced-\(T\)-free class.

This does not obstruct a polynomial **chromatic** bound—complete bipartite graphs are easy to colour—but it rules out a direct extension of the elementary star proof.

The unresolved task is therefore genuinely an upper-bound problem: obtain structural control sufficient for colouring arbitrary induced-\(T\)-free graphs. The lower bounds above only specify how large a successful polynomial may need to be. No general polynomial upper bound, and no counterexample to its existence, is established here.