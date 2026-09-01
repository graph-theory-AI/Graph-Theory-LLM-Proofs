```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exponent remains open, but the normalized extremal function has a genuine limit in n, the probabilistic upper prefactor can be slightly improved, and random tournaments admit a simple 2^{-k}-density construction.",
  "would_publish": false,
  "caveats": "There is no improvement to the worst-case exponential interval, and convergence of the exponent as k tends to infinity is not proved."
}
```

# 1. Formalization

I count the order of a path, i.e. its number of vertices; using edge-length changes only additive constants.

For a tournament \(T\), let \(p_k(T)\) be the largest \(\ell\) for which there are distinct vertices
\[
v_1,\dots,v_\ell
\]
such that
\[
v_i\to v_j\qquad\text{whenever }1\le j-i\le k.
\]
Define the extremal guarantee
\[
F_k(n)=\min_{\lvert T\rvert=n}p_k(T).
\]

The natural normalized parameter is
\[
\alpha_k=\lim_{n\to\infty}\frac{F_k(n)}n,
\]
provided this limit exists. The intended exponent would then be
\[
c=\lim_{k\to\infty}\frac{-\log_2\alpha_k}{k},
\]
again provided the latter limit exists.

The first limit does exist.

## Proposition 1: the limit in \(n\) exists

For every fixed \(k\),
\[
\alpha_k=\lim_{n\to\infty}\frac{F_k(n)}n
       =\inf_{n\ge1}\frac{F_k(n)}n.
\]

### Proof

For tournaments \(A,B\), let \(A\oplus B\) denote their transitive sum: all arcs between the two parts are directed from \(A\) to \(B\).

I claim that
\[
p_k(A\oplus B)=p_k(A)+p_k(B). \tag{1}
\]

The lower bound follows by concatenating maximum \(k\)-th power paths in \(A\) and \(B\). Every required arc crossing the join is directed forward.

For the upper bound, every \(k\)-th power path is in particular an ordinary directed path. Thus, in \(A\oplus B\), it cannot visit \(B\) and subsequently return to \(A\). Its vertices in \(A\) and \(B\) therefore form two consecutive subpaths, of orders at most \(p_k(A)\) and \(p_k(B)\), respectively. This proves (1).

Taking extremal \(n\)- and \(m\)-vertex tournaments gives
\[
F_k(n+m)\le F_k(n)+F_k(m).
\]
Thus \(F_k\) is subadditive, and Fekete's lemma yields the assertion. ∎

This removes one ambiguity in the open problem. It does not, however, prove that
\[
\frac{-\log_2\alpha_k}{k}
\]
converges as \(k\to\infty\). Without such a result, the formally safe quantities are its liminf and limsup.

A useful consequence of (1) is that every finite obstruction can be replicated without loss: if \(H\) is a tournament, then the transitive sum of \(q\) copies satisfies
\[
p_k(H^{\oplus q})=q\,p_k(H).
\]

# 2. A slight optimization of the probabilistic upper construction

The upper bound from the prompt can be recovered by a first-moment argument and its leading polynomial prefactor can be slightly improved.

## Proposition 2

As \(k\to\infty\),
\[
\alpha_k\le
\left(\frac{e\ln 2}{2}+o(1)\right)
\frac{k(k+1)}{2^k}.
\]
Numerically,
\[
\frac{e\ln2}{2}=0.94208\ldots.
\]

Thus this improves the displayed prefactor \(1\) in
\[
\alpha_k\le \frac{k(k+1)}{2^k}
\]
to approximately \(0.94208\). It does not alter the exponential constant.

### Proof

Let \(H\) be a uniformly random tournament on \(m\) vertices. For an ordered injective \(\ell\)-tuple to be a \(k\)-th power path, the number of prescribed arcs is, for \(\ell\ge k+1\),
\[
e_k(\ell)
 =\sum_{d=1}^k(\ell-d)
 =k\ell-\frac{k(k+1)}2.
\]
Put
\[
A=\frac{k(k+1)}2.
\]
The expected number \(X_\ell\) of \(k\)-th power paths of order \(\ell\) therefore satisfies
\[
\mathbb E X_\ell
=(m)_\ell\,2^{-k\ell+A}
\le 2^A\left(\frac{m}{2^k}\right)^\ell. \tag{2}
\]

Suppose \(m<2^k\), and write
\[
a=\log_2\frac{2^k}{m}>0.
\]
If
\[
\ell>\frac{A}{a},
\]
then (2) is less than \(1\). Hence some \(m\)-vertex tournament has no \(k\)-th power path of order \(\ell\), and consequently has
\[
p_k(H)\le \ell-1\le \frac{A}{a}.
\]
By Proposition 1 and transitive replication,
\[
\alpha_k\le \frac{A}{m\log_2(2^k/m)}+o(2^{-k}k^2). \tag{3}
\]

Write \(m=x2^k\), where \(0<x<1\). The denominator in (3), apart from \(2^k\), is
\[
x\log_2(1/x).
\]
This is maximized at \(x=e^{-1}\). Taking
\[
m=\left\lfloor\frac{2^k}{e}\right\rfloor
\]
gives
\[
\alpha_k
\le
\frac{A e\ln2+o(k^2)}{2^k}
=
\left(\frac{e\ln2}{2}+o(1)\right)
\frac{k(k+1)}{2^k}.
\]
∎

For comparison, taking \(m\sim 2^{k-1}\) gives exactly the coefficient \(1\) from the quoted upper bound.

# 3. Random tournaments attain the candidate exponent by a simple greedy procedure

This does not address adversarial tournaments, but it identifies precisely where randomness gives the expected factor \(2^{-k}\).

## Proposition 3

Let \(R_n\) be a uniformly random tournament, and allow \(k=k(n)\). If
\[
\frac{n}{2^k}\longrightarrow\infty,
\]
then with probability tending to \(1\),
\[
p_k(R_n)\ge (1-o(1))\frac{n}{2^k}.
\]

### Proof

Expose the vertices in a fixed order. Maintain a sequence \(P\), initially empty. When a new vertex \(v\) is exposed, append it to \(P\) if every one of the last
\[
\min\{k,\lvert P\rvert\}
\]
vertices of \(P\) sends an arc to \(v\). Otherwise discard \(v\).

Each successful append preserves the \(k\)-th power property.

If currently \(\lvert P\rvert=r<k\), the relevant \(r\) arcs incident with the new vertex are fresh independent fair orientations. Thus the conditional probability of accepting the new vertex is \(2^{-r}\). The expected number of exposed vertices needed to obtain the first \(k\) accepted vertices is consequently
\[
\sum_{r=0}^{k-1}2^r=2^k-1. \tag{4}
\]

Once \(P\) has order at least \(k\), every subsequent vertex is accepted with conditional probability exactly
\[
2^{-k}.
\]
The relevant arcs are fresh, even though the last \(k\) accepted vertices are chosen adaptively. By iterated conditioning, the subsequent success indicators are independent Bernoulli variables with parameter \(2^{-k}\).

Let \(\tau\) be the exposure time at which the first \(k\) vertices have been accepted. From (4) and Markov's inequality,
\[
\tau=o(n)
\]
with high probability because \(2^k=o(n)\). Conditional on this event, the number of subsequent accepted vertices is binomial with mean
\[
(1-o(1))\frac{n}{2^k},
\]
which tends to infinity. Chernoff's inequality now gives the claimed lower bound. ∎

The proof fundamentally uses fresh independent orientations. In a deterministic tournament the common out-neighborhood of a current transitive \(k\)-tuple can be empty, so this argument cannot simply be averaged over vertex orderings.

# 4. A finite obstruction illustrating the difficulty

Let \(Q_7\) be the tournament on \(\mathbb Z_7\) in which
\[
i\to j
\quad\Longleftrightarrow\quad
j-i\pmod 7\in\{1,2,4\}.
\]

Every vertex has three out-neighbors. For example,
\[
N^+(0)=\{1,2,4\},
\]
and these form the directed triangle
\[
1\to2\to4\to1.
\]
By translation symmetry, every out-neighborhood induces a directed triangle.

Any transitive subtournament on four vertices would have a source dominating its other three vertices. Those other vertices would have to be precisely its out-neighborhood, which is cyclic. Hence \(Q_7\) has no transitive four-vertex subtournament.

On the other hand, \(\{0,1,2\}\) is transitive. Therefore
\[
p_3(Q_7)=3,
\]
since a third power path on four vertices is exactly a transitive four-vertex tournament. Transitive replication yields
\[
\alpha_3\le \frac37.
\]

The analogous construction from a directed triangle gives the sharp asymptotic upper bound \(2/3\) for squares.

This example also rules out a tempting local argument: a transitive \(k\)-tuple need not have even one common out-neighbor. For \(k=3\), every transitive triple in \(Q_7\) has zero common out-neighbors, since such a neighbor would create a transitive four-set.

# 5. Exact finite search formulation

The finite-base viewpoint from Proposition 1 makes SAT search potentially useful. For fixed \(n,k,L\), introduce one Boolean variable \(x_{uv}\) for every \(u<v\), with \(x_{uv}=1\) meaning \(u\to v\). For ordered distinct vertices \((v_1,\dots,v_L)\), add the clause
\[
\bigvee_{\substack{1\le i<j\le L\\j-i\le k}}
\neg E(v_i,v_j),
\]
where \(E(a,b)\) is the appropriate orientation literal.

The resulting formula is satisfiable exactly when there exists an \(n\)-vertex tournament with no \(k\)-th power path of order \(L\). Clauses can be generated lazily:

1. Solve the current orientation instance.
2. Search for a \(k\)-th power path of order \(L\) using DFS with state
   \[
   (\text{used vertex set},\ \text{ordered last at most }k\text{ vertices}).
   \]
3. If one is found, add its blocking clause and repeat.
4. If none is found, the current tournament is an explicit certificate.

No computational results from this formulation are claimed here.

# 6. Remaining gap

Let
\[
c_-=\liminf_{k\to\infty}\frac{-\log_2\alpha_k}{k},
\qquad
c_+=\limsup_{k\to\infty}\frac{-\log_2\alpha_k}{k}.
\]
The probabilistic upper construction gives
\[
c_-\ge1.
\]
The displayed theorem in the source gives \(c_+\le4\); the optimization reported in the prompt would give approximately
\[
c_+\le3.9.
\]

The central unresolved task is therefore still one of the following:

- prove the universal lower bound
  \[
  \alpha_k\ge 2^{-(1+o(1))k},
  \]
  which would establish the natural candidate \(c=1\); or
- construct tournaments with
  \[
  \alpha_k\le 2^{-(1+\varepsilon)k}
  \]
  for some fixed \(\varepsilon>0\), disproving that candidate.

The arguments above neither improve the worst-case exponent nor prove that \(c_-=c_+\).