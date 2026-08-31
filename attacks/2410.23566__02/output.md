```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The general base remains open, but it is at least 2, and base 2 is sharp for blown-up out-/in-stars and for almost all host tournaments.",
  "would_publish": false,
  "caveats": "No worst-case upper bound improving the source paper's exponential base is proved."
}
```

# Mathematical writeup

## 1. Normalization

For an acyclic digraph \(D\), let \(u(D)\) be the least \(N\) such that every \(N\)-vertex tournament contains \(D\) as a non-induced subdigraph.

For fixed \(k\), define
\[
a_k:=\limsup_{n\to\infty}\ \max_{\substack{\vec T\text{ oriented tree}\\ |V(\vec T)|=n}}
\frac{u(\vec T[k])}{kn}.
\]
Thus the fixed-\(k\) version of the requested constant is \(a_k^{1/k}\). The exponential-rate interpretation is
\[
C_{\mathrm{rate}}:=\limsup_{k\to\infty}a_k^{1/k}.
\]

The theorem quoted in the question gives
\[
a_k\le 2^{10+18k},
\]
and hence
\[
C_{\mathrm{rate}}\le 2^{18}.
\]

I prove below that
\[
a_k\ge 2^k,
\]
and, more precisely, that equality holds when the maximum is restricted to consistently oriented stars.

---

## 2. Sharp asymptotics for blown-up out-stars

Let \(\vec S_n^+\) be the out-star on \(n\) vertices, with center \(c\) and all arcs directed from \(c\) to the leaves. Put
\[
L:=k(n-1).
\]
The digraph \(\vec S_n^+[k]\) is, for purposes of non-induced containment, exactly a consistently oriented complete bipartite graph
\[
\overrightarrow{K}_{k,L};
\]
an embedding consists of a \(k\)-set \(X\) and \(L\) vertices dominated by every vertex of \(X\).

For a \(k\)-set \(X\) in a tournament \(R\), write
\[
N_R^+(X)=\{v\notin X:xv\in A(R)\text{ for every }x\in X\}.
\]
Let \(r_k(L)\) be the least \(N\) such that every \(N\)-vertex tournament has a \(k\)-set \(X\) with \(|N^+(X)|\ge L\).

### Proposition 1

For every fixed \(k\), as \(L\to\infty\),
\[
r_k(L)=(2^k+o(1))L.
\]
More quantitatively, for all sufficiently large \(L\),
\[
2^k\left(L-\sqrt{3(k+1)L\log(2^kL)}\right)
<r_k(L)
\le 2^kL+k(k+3).
\]

Consequently,
\[
\lim_{n\to\infty}\frac{u(\vec S_n^+[k])}{kn}=2^k.
\]

### Deterministic upper bound

Let \(R\) be a tournament on \(N\) vertices. Double-counting pairs \((X,v)\) with \(|X|=k\) and \(X\to v\) gives
\[
\sum_{X\in\binom{V(R)}k}|N_R^+(X)|
=
\sum_{v\in V(R)}\binom{d_R^-(v)}k.
\tag{1}
\]

The integer-valued function \(t\mapsto \binom tk\) is discretely convex, since
\[
\binom{t+1}{k}-\binom tk=\binom t{k-1}
\]
is nondecreasing in \(t\). Since
\[
\sum_v d_R^-(v)=\binom N2,
\]
the right side of (1) is minimized, subject only to this sum, when the degrees are as equal as possible. In particular, with
\[
q=\left\lfloor\frac{N-1}{2}\right\rfloor,
\]
we obtain
\[
\max_{X\in\binom{V(R)}k}|N_R^+(X)|
\ge
\frac{N\binom qk}{\binom Nk}.
\tag{2}
\]

For fixed \(k\), the right side is
\[
\frac{N}{2^k}+O_k(1).
\]
An explicit estimate is also available. For sufficiently large \(N\),
\[
\begin{aligned}
\frac{N\binom qk}{\binom Nk}
&=N\prod_{i=0}^{k-1}\frac{q-i}{N-i}\\
&\ge \frac{N}{2^k}
 \prod_{i=0}^{k-1}\left(1-\frac{i+2}{N-i}\right)\\
&\ge \frac{N}{2^k}
\left(1-\frac{k(k+3)}{2(N-k+1)}\right)\\
&\ge \frac{N-k(k+3)}{2^k}.
\end{aligned}
\tag{3}
\]
Here the penultimate inequality uses
\[
\prod_i(1-a_i)\ge1-\sum_i a_i.
\]

Taking
\[
N=2^kL+k(k+3)
\]
in (3) gives a \(k\)-set with at least \(L\) common out-neighbours. Hence
\[
r_k(L)\le 2^kL+k(k+3).
\tag{4}
\]

### Probabilistic lower bound

Let
\[
t=\sqrt{3(k+1)L\log(2^kL)}
\]
and take
\[
N=\left\lfloor 2^k(L-t)\right\rfloor.
\]
Orient every edge of \(K_N\) independently and uniformly.

For any fixed \(k\)-set \(X\),
\[
|N^+(X)|\sim\operatorname{Bin}(N-k,2^{-k}),
\]
because each outside vertex is dominated by all vertices of \(X\) with probability \(2^{-k}\), independently for different outside vertices. Its mean satisfies
\[
\mu=\frac{N-k}{2^k}\le L-t.
\]
For sufficiently large \(L\), a standard Chernoff bound gives
\[
\Pr\bigl(|N^+(X)|\ge L\bigr)
\le
\exp\left(-\frac{t^2}{3L}\right)
=(2^kL)^{-(k+1)}.
\]
There are at most \(N^k\le(2^kL)^k\) possible \(k\)-sets, so by the union bound,
\[
\Pr\bigl(\exists X:\ |N^+(X)|\ge L\bigr)
\le \frac1{2^kL}<1.
\]
Thus there exists an \(N\)-vertex tournament avoiding \(\overrightarrow K_{k,L}\). This proves the lower estimate in Proposition 1.

The same result holds for in-stars by reversing every arc.

### Consequence for the proposed base

Since \(L=k(n-1)\),
\[
u(\vec S_n^+[k])=(2^k+o(1))kn.
\]
Therefore every interpretation of the problem in which \(C^kkn\) must work for all oriented trees has
\[
\boxed{C\ge2}.
\]

Conversely, for the subclass of out-stars or in-stars, the infimum is exactly \(2\). In fact, the literal budget \(2^kkn\) itself suffices for all sufficiently large \(n\). For \(k\ge3\), this follows from (4) and
\[
2^kk\ge k(k+3).
\]
The cases \(k=1,2\) follow directly from (2); for example, for \(k=2\) and \(N=8n\),
\[
\max_X|N^+(X)|
\ge
\frac{(4n-1)(4n-2)}{8n-1}
>
2n-2=L.
\]

---

## 3. Base \(2\) is also sharp for random host tournaments

The star argument identifies the correct threshold not only for a special target, but also for simultaneous universality in a typical tournament.

Define the \(k\)-common semidegree of a tournament \(R\) by
\[
\delta_k^0(R):=
\min_{X\in\binom{V(R)}k}
\min\{|N_R^+(X)|,\ |N_R^-(X)|\}.
\]

### Lemma 2

Let \(\vec T\) be any oriented tree on \(n\) vertices and put \(m=kn\). If
\[
\delta_k^0(R)\ge m,
\]
then \(R\) contains \(\vec T[k]\).

#### Proof

Root the underlying tree arbitrarily and process its vertices with each parent before its children. Choose any \(k\)-set for the root bag.

Suppose the parent bag \(X\) of the next tree vertex has already been embedded. If the corresponding tree arc is directed from parent to child, choose the child bag inside \(N^+(X)\); if it is directed from child to parent, choose it inside \(N^-(X)\).

Before the last bag is chosen, at most \(m-k\) vertices have been used. Since the appropriate common neighbourhood has at least \(m\) vertices, at least \(k\) unused candidates remain. Choosing any \(k\) of them gives the next bag. Every prescribed arc lies between a parent and a child, so this greedy procedure embeds the whole blow-up. ∎

### Corollary 3

Fix \(k\) and \(\varepsilon>0\), and let \(m=kn\).

1. A uniformly random tournament on
   \[
   N_+=\left\lceil(1+\varepsilon\right\rceil 2^km
   \]
   vertices—more precisely, on
   \[
   N_+=\left\lceil(1+\varepsilon)2^km\right\rceil
   \]
   vertices—a.a.s. contains \(\vec T[k]\) for every oriented tree \(\vec T\) of order \(n\), simultaneously.

2. A uniformly random tournament on
   \[
   N_-=\left\lfloor(1-\varepsilon)2^km\right\rfloor
   \]
   vertices a.a.s. avoids the \(k\)-blow-up of the out-star on \(n\) vertices.

For the first assertion, for any fixed \(k\)-set \(X\), each of \(|N^\pm(X)|\) has distribution
\[
\operatorname{Bin}(N_+-k,2^{-k})
\]
with mean at least \((1+\varepsilon/2)m\) for large \(n\). Chernoff bounds and a union bound over at most \(2N_+^k\) choices of \(X\) and sign give
\[
\Pr(\delta_k^0(R)<m)\le e^{-\Omega_{k,\varepsilon}(n)}.
\]
Lemma 2 then applies. The second assertion follows from the same upper-tail calculation used for Proposition 1, since the required leaf set has size \(m-k\), whereas the expected common out-neighbourhood has size approximately \((1-\varepsilon)m\).

Thus \(2^kkn\) is the sharp coarse threshold in the random-host model. This does not imply the corresponding worst-case theorem.

---

## 4. Check of the maximum-average-degree calculation

For completeness, the underlying graph of \(\vec T[k]\) indeed has maximum average degree
\[
2k\left(1-\frac1n\right).
\]

For a vertex subset of the blow-up, let \(x_v\in\{0,\dots,k\}\) be the number of selected vertices in the bag corresponding to \(v\in V(T)\), and put \(y_v=x_v/k\). Then
\[
|S|=k\sum_v y_v,\qquad
e(S)=k^2\sum_{uv\in E(T)}y_uy_v.
\]
Choose a random subset \(Z\subseteq V(T)\) by including \(v\) independently with probability \(y_v\). Since every induced subgraph of an \(n\)-vertex tree satisfies
\[
e(T[Z])\le \left(1-\frac1n\right)|Z|,
\]
taking expectations gives
\[
\sum_{uv\in E(T)}y_uy_v
\le
\left(1-\frac1n\right)\sum_v y_v.
\]
Consequently,
\[
\frac{2e(S)}{|S|}
\le 2k\left(1-\frac1n\right).
\]
Equality holds for the full vertex set.

---

## 5. Bounds on the unresolved constant

From the star calculation and the quoted theorem,
\[
2^k\le a_k\le 2^{10+18k},
\]
so for the fixed-\(k\) formulation,
\[
\boxed{2\le a_k^{1/k}\le 2^{18+10/k}}.
\]

If the intended quantity is the asymptotic exponential rate,
\[
\boxed{2\le C_{\mathrm{rate}}\le2^{18}}.
\]

If instead one literally requires one \(C\) satisfying \(a_k\le C^k\) for every \(k\), with no multiplicative prefactor, the supplied theorem directly gives only
\[
2\le C\le2^{28},
\]
because \(10+18k\le28k\) for \(k\ge1\). The catalog appears to use the exponential-rate interpretation, under which the upper base is \(2^{18}\).

---

## 6. Remaining gap

The deterministic greedy lemma explains why base \(2\) is natural: adding a new bag costs a factor \(2^{-k}\) in a quasirandom tournament, and each new bag has only its parent bag as a constraint.

However, an arbitrary tournament need not have large \(k\)-common semidegree. A transitive tournament, for example, has \(k\)-sets with empty common in-neighbourhood, although it trivially contains every acyclic digraph of the appropriate order through a topological ordering. Thus the expansion condition is sufficient but far from necessary.

What is missing is a deterministic argument combining the quasirandom/expanding regime with structured regimes such as nearly transitive tournaments, without losing an exponential factor larger than \(2^k\). No such argument, and no construction forcing a base strictly larger than \(2\), is obtained here.