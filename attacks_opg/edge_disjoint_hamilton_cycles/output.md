```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "Thomassen's conjecture is a published theorem, with the optimal-order connectivity bound f(k)=O(k^2).",
  "would_publish": false,
  "caveats": "The published upper-bound theorem is invoked, not reproved; no novelty is claimed."
}
```

## 1. Published resolution

The literature update in the question supersedes the original open-problem entry.

Recall that a tournament is **strongly \(r\)-connected** if it has more than \(r\) vertices and remains strongly connected after deleting any set of fewer than \(r\) vertices.

The relevant published theorem is:

> **Theorem (Pokrovskiy [2]).** There is an absolute constant \(C>0\) such that, for every integer \(k\ge 2\), every strongly \(\lceil Ck^2\rceil\)-connected tournament contains \(k\) pairwise edge-disjoint directed Hamilton cycles.

Consequently, the conjecture holds with
\[
f(k)=\lceil Ck^2\rceil .
\]
Its existential assertion had already been proved by Kühn, Lapinskas, Osthus, and Patel [1], with the bound \(f(k)=O(k^2\log^2 k)\).

For additional mathematical substance, below is a self-contained quadratic lower-bound construction. If \(F(k)\) denotes the smallest connectivity threshold that guarantees \(k\) edge-disjoint Hamilton cycles, it shows that
\[
\boxed{\binom{k+1}{2}\le F(k)\le \lceil Ck^2\rceil.}
\]
Thus the quadratic order is genuinely necessary, not merely a feature of the known proof.

## 2. A self-contained quadratic lower bound

Fix \(k\ge 2\), and put
\[
r=\binom{k+1}{2}-1.
\]
We construct a strongly \(r\)-connected tournament containing no \(k\) edge-disjoint Hamilton cycles. In fact, it will have no spanning subdigraph with every indegree and outdegree equal to \(k\).

### A robust tournament used in the construction

Let \(R_r\) have vertex set \(\mathbb Z/(2r+1)\mathbb Z\), with
\[
i\longrightarrow j
\quad\Longleftrightarrow\quad
j-i\pmod{2r+1}\in\{1,\ldots,r\}.
\]
This is a tournament.

It is strongly \(r\)-connected. Indeed, after deleting fewer than \(r\) vertices, list the surviving vertices in their original cyclic order. The forward cyclic distance between successive surviving vertices is at most \(r\), since at most \(r-1\) vertices were deleted. Thus the surviving vertices, in that order, form a directed Hamilton cycle.

### Construction of \(T\)

Take disjoint sets
\[
A=\{a_0,\ldots,a_{2r}\},\qquad
B=\{b_0,\ldots,b_{2r}\},\qquad
W=\{w_1,\ldots,w_k\}.
\]

Orient the edges as follows:

1. Both \(T[A]\) and \(T[B]\) are copies of \(R_r\).
2. Orient \(T[W]\) transitively.
3. Put every edge from \(B\) to \(W\), and every edge from \(W\) to \(A\):
   \[
   B\longrightarrow W\longrightarrow A.
   \]
4. Between \(A\) and \(B\), put all edges from \(B\) to \(A\), except for the \(r\) edges
   \[
   a_i\longrightarrow b_i,\qquad 0\le i<r.
   \]

This specifies a tournament on \(4r+k+2\) vertices.

### Connectivity

Let \(S\subseteq V(T)\) satisfy \(|S|<r\).

Both \(T[A\setminus S]\) and \(T[B\setminus S]\) are strongly connected by the property of \(R_r\). Moreover, the \(r\) exceptional edges
\[
a_i\longrightarrow b_i
\]
are vertex-disjoint. Deleting fewer than \(r\) vertices therefore leaves at least one of them intact. Hence there is an edge from \(A\setminus S\) to \(B\setminus S\).

There is also an edge in the opposite direction. Indeed, each vertex of \(B\) fails to send an edge to at most one vertex of \(A\), while
\[
|A\setminus S|\ge r+2>1.
\]
It follows that \(T[(A\cup B)\setminus S]\) is strongly connected.

Every surviving \(w\in W\setminus S\) receives edges from all of \(B\setminus S\) and sends edges to all of \(A\setminus S\). Adding these vertices preserves strong connectivity. Thus \(T-S\) is strongly connected, proving that \(T\) is strongly \(r\)-connected.

In fact, its connectivity is exactly \(r\): deleting \(a_0,\ldots,a_{r-1}\) leaves a nonempty set \(A\setminus S\) with no outgoing edge to its complement.

### The obstruction to \(k\) Hamilton cycles

Suppose that \(T\) contained \(k\) pairwise edge-disjoint Hamilton cycles, and let \(H\) be their union. Then
\[
d_H^+(v)=d_H^-(v)=k
\qquad\text{for every }v\in V(T).
\]

For vertex sets \(P,Q\), let \(e_H(P,Q)\) count the edges of \(H\) with tail in \(P\) and head in \(Q\). Set
\[
X=A\cup W,\qquad Y=B\cup W.
\]
Although \(X\) and \(Y\) overlap, the sets \(A\) and \(Y\) partition \(V(T)\). Consequently,
\[
e_H(X,Y)
 =k|X|-e_H(X,A)
 \ge k(|A|+k)-k|A|
 =k^2.
\]
Here \(e_H(X,A)\le k|A|\) because the total indegree of the vertices of \(A\) in \(H\) is \(k|A|\).

But the only edges of \(T\) with tail in \(X\) and head in \(Y\) are:

- the \(r\) exceptional edges from \(A\) to \(B\);
- the \(\binom{k}{2}\) edges inside \(W\).

There are no edges from \(A\) to \(W\) or from \(W\) to \(B\). Therefore
\[
e_T(X,Y)
 =r+\binom{k}{2}
 =\left(\binom{k+1}{2}-1\right)+\binom{k}{2}
 =k^2-1.
\]
This contradicts
\[
k^2\le e_H(X,Y)\le e_T(X,Y)=k^2-1.
\]

Thus the constructed strongly \(r\)-connected tournament has no \(k\) edge-disjoint Hamilton cycles. Since this works for every \(k\ge2\),
\[
F(k)\ge r+1=\binom{k+1}{2}.
\]

## 3. Scope and dependencies

The conjecture itself is settled by the published upper-bound theorem. The construction above independently verifies the quadratic lower bound, giving
\[
F(k)=\Theta(k^2).
\]

This writeup does **not** reproduce the substantial proof of the upper bound in [2], nor does it determine the sharp constant or the exact values of \(F(k)\). Its sole non-self-contained mathematical input is the established upper-bound theorem; no unproved conjecture is used.

### References

[1] Daniela Kühn, John Lapinskas, Deryk Osthus, and Viresh Patel, **Proof of a conjecture of Thomassen on Hamilton cycles in highly connected tournaments**, *Proceedings of the London Mathematical Society* (2014). DOI: **10.1112/plms/pdu019**.

[2] Alexey Pokrovskiy, **Edge disjoint Hamiltonian cycles in highly connected tournaments**, *International Mathematics Research Notices* (2017). DOI: **10.1093/imrn/rnw009**. arXiv: **1406.7556**.