```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The established uniform partition theorem gives an affirmative answer, with g(k_1,...,k_p) <= C p max_i k_i for an absolute constant C.",
  "would_publish": false,
  "caveats": "This applies a published theorem rather than providing a new proof; the optimal threshold for unequal k_i is not determined here."
}
```

## 1. Status and the theorem that resolves the question

The original Garden entry is outdated: the existence question, including the case \(g(2,2)\), has been resolved.

Kühn, Osthus and Townsend established the required uniform partition theorem in *Proof of a tournament partition conjecture and an application to 1-factors with prescribed cycle lengths*, arXiv:1309.7677. The later work of Girão and Letzter, *Partitioning a tournament into sub-tournaments of high connectivity*, arXiv:2210.17371, gives the following stronger quantitative form.

**Uniform partition theorem (Girão–Letzter).** There is an absolute positive integer \(C\) such that, for all positive integers \(k,t\), every strongly \(Ckt\)-connected tournament admits a partition
\[
V(T)=W_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}W_t
\]
such that each \(T[W_j]\) is strongly \(k\)-connected.

Here, a digraph is **strongly \(k\)-connected** if it has more than \(k\) vertices and remains strongly connected after deletion of any set of fewer than \(k\) vertices. Thus the parts supplied by the theorem are nontrivial.

The earlier Kühn–Osthus–Townsend existence theorem already suffices to answer the original problem. The linear theorem supplies the bound below.

## 2. Complete reduction to the non-uniform statement

**Corollary.** There is an absolute constant \(C\) such that one may take
\[
\boxed{\displaystyle
g(k_1,\ldots,k_p)=Cp\max_{1\le i\le p}k_i.}
\]

**Proof.** Set
\[
K=\max_{1\le i\le p}k_i.
\]
Apply the uniform partition theorem with \(k=K\) and \(t=p\). Every strongly \(CpK\)-connected tournament has a partition
\[
V(T)=V_1\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}V_p
\]
such that every \(T[V_i]\) is strongly \(K\)-connected.

Fix \(i\). We have
\[
|V_i|>K\ge k_i.
\]
For every \(X\subseteq V_i\) with \(|X|<k_i\), we also have \(|X|<K\). Consequently,
\[
T[V_i]-X
\]
is strongly connected. Therefore \(T[V_i]\) is strongly \(k_i\)-connected.

This holds for every \(i\), proving the required partition. For \(p=1\), the sharper choice \(g(k_1)=k_1\) is immediate. \(\square\)

In particular, the uniform theorem gives \(g(2,2)\le 4C\); its existence is no longer open.

## 3. Checking the lower bound

For completeness, the construction in the question indeed shows that no sufficient threshold can be smaller than
\[
S:=k_1+\cdots+k_p.
\]

Assume \(S\ge2\), and put \(s=S-1\). Choose \(n\ge3s\). Construct a tournament on
\[
R\mathbin{\dot\cup}Q,
\qquad |R|=s,\qquad
Q=\{v_1,\ldots,v_{n-s}\},
\]
as follows:

- \(v_a\to v_b\) whenever \(a<b\);
- every vertex of \(R\) dominates \(v_1,\ldots,v_s\);
- \(v_{n-2s+1},\ldots,v_{n-s}\) dominate every vertex of \(R\);
- all remaining edges are arbitrary.

### Connectivity of the construction

Let \(X\subseteq V(T)\) satisfy \(|X|<s\). There is a surviving vertex of \(R\), and there are surviving vertices in both the first and last blocks of \(s\) vertices of \(Q\).

Let \(a,b\) be, respectively, the first and last surviving vertices in the transitive order on \(Q\). Then every surviving \(r\in R\) satisfies
\[
r\to a,\qquad b\to r.
\]
Every surviving vertex of \(Q\) is reachable from \(a\) and can reach \(b\). Hence every surviving vertex of \(R\) can reach every surviving vertex of \(Q\), and conversely. The whole tournament \(T-X\) is strongly connected.

Thus \(T\) is strongly \(s\)-connected. Deleting \(R\) leaves a transitive tournament with at least two vertices, so its connectivity is exactly \(s\).

### Why the desired partition is impossible

Suppose \(T[W]\) is a nontrivial strongly \(k\)-connected subtournament. If
\[
|W\cap R|<k,
\]
delete \(W\cap R\) from \(T[W]\). The remaining tournament is transitive, and its order is at least
\[
|W|-|W\cap R|
\ge (k+1)-(k-1)=2.
\]
It is therefore not strongly connected, a contradiction. Consequently,
\[
|W\cap R|\ge k.
\]

A partition into the required subtournaments would therefore imply
\[
|R|
=\sum_{i=1}^p |V_i\cap R|
\ge\sum_{i=1}^p k_i
=S,
\]
contrary to \(|R|=S-1\).

The remaining case \(S=1\) is simply \(p=1,k_1=1\), whose least positive threshold is \(1\).

## 4. Conclusion and scope

Writing \(g_{\min}\) for the least sufficient threshold, the established results give
\[
\boxed{\displaystyle
\sum_{i=1}^p k_i
\;\le\;
g_{\min}(k_1,\ldots,k_p)
\;\le\;
Cp\max_i k_i.}
\]

For equal requirements this yields
\[
g_{\min}(\underbrace{k,\ldots,k}_{p\text{ times}})
=\Theta(pk).
\]
For unequal requirements, the maximum-based reduction does **not** by itself establish an \(O(\sum_i k_i)\) upper bound.

The deep input here is the published uniform partition theorem, which is cited rather than reproved. The non-uniform reduction is complete and uses no additional conjecture. This is an explanation of an existing resolution, not a new research result.