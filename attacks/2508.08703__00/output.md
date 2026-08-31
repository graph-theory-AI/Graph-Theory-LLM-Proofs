```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Any 6-regular (4,1)-graph has at least 15 vertices, but existence from order 15 onward remains unresolved.",
  "would_publish": false,
  "caveats": "The lower bound is self-contained, but its novelty relative to details or computations in the full source paper has not been checked."
}
```

# Mathematical writeup

## 1. Statement of the partial result

A critical edge of a \(4\)-chromatic graph \(G\) is an edge \(e\) such that \(G-e\) is \(3\)-colorable. A \((4,1)\)-graph is a \(4\)-vertex-critical graph with no critical edge.

I prove:

> **Theorem.** If \(G\) is a \(6\)-regular \((4,1)\)-graph, then
> \[
> |V(G)|\ge 15.
> \]

The proof also gives the following necessary structure at the first surviving order.

> **Order-\(15\) reduction.** If such a graph has order \(15\), and \(H=\overline G\), then:
> 1. \(H\) is \(8\)-regular and \(\omega(H)=5\);
> 2. for every \(v\), \(H-v\) has a clique partition of sizes \(5,5,4\);
> 3. if \(Q\) is a \(K_5\) in \(H\), then each \(q\in Q\) has four neighbors outside \(Q\), and these external neighborhoods have pairwise intersection at most two.

This does not settle existence at order \(15\) or above.

---

## 2. The coloring-balance lemma

The key point is that degree \(6\) is the equality case of the elementary lower bound \(\delta(G)\ge 6\).

> **Lemma 2.1.** Let \(G\) be \(4\)-vertex-critical and \(v\in V(G)\). An edge \(vx\) is critical if and only if there is a proper \(3\)-coloring of \(G-v\) in which \(x\) is the unique neighbor of \(v\) receiving its color.
>
> Consequently, if \(G\) has no critical edge and \(d(v)=6\), then in every proper \(3\)-coloring of \(G-v\), each of the three colors occurs exactly twice on \(N_G(v)\).

**Proof.**

Suppose \(\varphi\) is a \(3\)-coloring of \(G-v\) and \(x\) is the unique neighbor of \(v\) colored \(\varphi(x)\). In \(G-vx\), give \(v\) color \(\varphi(x)\). This is proper, so \(vx\) is critical.

Conversely, suppose \(G-vx\) has a proper \(3\)-coloring. The vertices \(v\) and \(x\) must receive the same color; otherwise the coloring would also be proper for \(G\). No other neighbor of \(v\) can receive that color. Restricting to \(G-v\) therefore gives the claimed coloring.

In any \(3\)-coloring of \(G-v\), every color must occur on \(N(v)\), since otherwise \(v\) could receive a missing color. If there is no critical edge, no color occurs exactly once. With six neighbors, the three multiplicities must therefore be \(2,2,2\). \(\square\)

Let \(H=\overline G\). A \(3\)-coloring of \(G-v\) is a partition
\[
V(G)\setminus\{v\}=C_1\mathbin{\dot\cup}C_2\mathbin{\dot\cup}C_3
\]
into three cliques of \(H\). Lemma 2.1 translates to
\[
|N_H(v)\cap C_i|=|C_i|-2. \tag{2.1}
\]
In particular, every \(C_i\) has at least two vertices.

---

## 3. A clique obstruction in the complement

Suppose henceforth that \(G\) is \(6\)-regular of order \(n\), and put \(H=\overline G\). Then \(H\) is \((n-7)\)-regular.

> **Lemma 3.1.** Let \(Q\) be a clique of \(H\) of size \(s\ge2\), let
> \[
> R=V(H)\setminus Q,
> \]
> and for \(q\in Q\) set
> \[
> N_q=N_H(q)\cap R.
> \]
> Then every \(N_q\) has size
> \[
> d=n-s-6.
> \]
> Moreover:
>
> 1. \(d\ge2\), and hence \(s\le n-8\);
> 2. for distinct \(q,q'\in Q\),
>    \[
>    |N_q\cap N_{q'}|\le d-2; \tag{3.1}
>    \]
> 3. if \(s\ge5\), then \(d\ge4\), and hence \(s\le n-10\).

**Proof.**

The formula for \(d\) follows because every vertex of \(Q\) has \(s-1\) neighbors inside \(Q\) and total \(H\)-degree \(n-7\).

Fix \(q\in Q\), and take a clique partition \(C_1,C_2,C_3\) of \(H-q\). For one part \(C\), write
\[
a=|C\cap(Q\setminus\{q\})|,\qquad
b=|C\cap R|,\qquad
e=|C\cap N_q|.
\]
Since \(q\) is adjacent in \(H\) to all \(a\) vertices of \(C\cap Q\), equation (2.1) gives
\[
a+e=(a+b)-2,
\]
and hence
\[
b=e+2. \tag{3.2}
\]
Thus every part contains at least two vertices of \(R\).

Let \(q'\in Q\setminus\{q\}\), and suppose \(q'\in C\). Since \(C\) is a clique, all \(b\) vertices of \(C\cap R\) belong to \(N_{q'}\). Hence \(b\le d\), proving \(d\ge2\).

Furthermore, inside \(C\cap R\), exactly \(e=b-2\) vertices belong to \(N_q\). Outside \(C\cap R\), the set \(N_{q'}\) has only \(d-b\) vertices. Therefore
\[
|N_q\cap N_{q'}|
   \le (b-2)+(d-b)
   =d-2,
\]
which proves (3.1).

Finally suppose \(s\ge5\). For fixed \(q\), the \(s-1\ge4\) vertices of \(Q\setminus\{q\}\) lie in three parts, so two of them, say \(q',q''\), lie in the same part. That part contains at least two vertices of \(R\), all belonging to both \(N_{q'}\) and \(N_{q''}\). Thus
\[
|N_{q'}\cap N_{q''}|\ge2.
\]
Applying (3.1) to \(q',q''\) gives \(2\le d-2\), so \(d\ge4\). \(\square\)

---

## 4. Excluding all orders below \(15\)

Every \(H-v\) is the union of three clique parts satisfying (2.1).

### 4.1 Orders at most \(11\)

By Lemma 3.1, every clique of size at least two has size at most \(n-8\). Therefore
\[
n-1=|V(H-v)|\le 3(n-8).
\]
This implies
\[
n\ge12.
\]

### 4.2 Order \(12\)

Here Lemma 3.1 gives \(\omega(H)\le4\). Since \(H-v\) has \(11\) vertices partitioned into three cliques, \(H\) contains a \(K_4\); fix one,
\[
Q=\{q_1,q_2,q_3,q_4\}.
\]
For this clique,
\[
d=12-4-6=2.
\]
Thus the four external neighborhoods \(N_{q_i}\) are pairwise disjoint by (3.1).

Fix \(q_1\) and a clique partition of \(H-q_1\). Each of \(q_2,q_3,q_4\) lies in a part containing at least two vertices of \(R=V(H)\setminus Q\). Since each \(q_i\) has only two neighbors in \(R\), a part containing \(q_i\) contains exactly the two vertices of \(N_{q_i}\).

If \(q_2,q_3,q_4\) occupied three distinct parts, those parts would contain only
\[
2+2+2=6
\]
vertices of \(R\), whereas \(|R|=8\). Hence two of \(q_2,q_3,q_4\) share a part. The two \(R\)-vertices in that part then lie in both corresponding external neighborhoods, contradicting their disjointness.

Therefore \(n\ne12\).

### 4.3 Order \(13\)

Again \(\omega(H)\le4\): a clique of size at least five would, by Lemma 3.1, have size at most \(n-10=3\).

Thus every clique partition of \(H-v\), which has \(12\) vertices, consists of three \(K_4\)'s. Fix a \(K_4\)
\[
Q=\{q_1,q_2,q_3,q_4\}.
\]
Now
\[
d=13-4-6=3,
\]
so by (3.1),
\[
|N_{q_i}\cap N_{q_j}|\le1 \qquad(i\ne j). \tag{4.1}
\]

Fix \(q_1\) and partition \(H-q_1\) into three \(K_4\)'s. No two of \(q_2,q_3,q_4\) can lie in the same part: that part contains at least two vertices of \(R\), which would give an intersection of size at least two in violation of (4.1). Hence \(q_2,q_3,q_4\) lie in distinct parts.

There are nine vertices in \(R\). Each of the three parts contains between two and three vertices of \(R\), so each contains exactly three. The \(R\)-part containing \(q_i\) must therefore equal \(N_{q_i}\). Consequently,
\[
N_{q_2},N_{q_3},N_{q_4}
\]
are pairwise disjoint. Equation (3.2) gives
\[
|N_{q_1}\cap N_{q_i}|=3-2=1
\qquad (i=2,3,4). \tag{4.2}
\]

Now apply the same conclusion with \(q_2\) in place of \(q_1\). It says that
\[
N_{q_1},N_{q_3},N_{q_4}
\]
are pairwise disjoint, contradicting \(|N_{q_1}\cap N_{q_3}|=1\) from (4.2).

Therefore \(n\ne13\).

### 4.4 Order \(14\)

If \(H\) had a clique of size \(s\ge5\), Lemma 3.1 would give
\[
s\le n-10=4,
\]
a contradiction. Thus \(\omega(H)\le4\).

But \(H-v\) has \(13\) vertices and cannot be partitioned into three cliques of size at most four. Hence \(n\ne14\).

Combining the four cases proves the theorem:
\[
\boxed{|V(G)|\ge15.}
\]

---

## 5. The first surviving order

Suppose \(n=15\). Lemma 3.1 excludes cliques of size at least six, while every \(H-v\) has \(14\) vertices covered by three cliques. Therefore
\[
\omega(H)=5,
\]
and every such partition has sizes
\[
5,5,4.
\]

For a \(K_5\), say \(Q\), every vertex of \(Q\) has
\[
d=15-5-6=4
\]
neighbors outside \(Q\). Lemma 3.1 yields
\[
|N_q\cap N_{q'}|\le2
\qquad(q\ne q').
\]
In a partition of \(H-q\), four vertices of \(Q\setminus\{q\}\) occupy three parts, so two share a part. The \(R\)-portion of that part has at least two vertices, and hence the two corresponding external neighborhoods intersect in exactly two vertices.

These conditions are not themselves contradictory. For example, if ten abstract outside vertices are partitioned into pairs
\[
X_0,\ldots,X_4,
\]
then the set system
\[
N_i=X_i\cup X_{i+1}\qquad(\text{indices mod }5)
\]
has all pairwise intersections of size at most two and realizes the local intersection pattern forced by deleting vertices of a hypothetical \(K_5\). Additional clique adjacencies and the deletion conditions for the outside vertices remain to be enforced.

Thus the argument genuinely stops at order \(15\).

---

## 6. Sanity check: a close order-\(13\) example

The no-critical-edge hypothesis is essential. On \(\mathbb Z_{13}\), let \(G\) join vertices whose cyclic distance is \(4,5\), or \(6\). This graph is \(6\)-regular and \(4\)-vertex-critical:

- its independence number is \(4\), so \(\chi(G)\ge4\);
- after deleting \(0\), the sets
  \[
  \{1,2,3,4\},\quad
  \{5,6,7,8\},\quad
  \{9,10,11,12\}
  \]
  are independent, and rotations handle every deleted vertex.

However, the edge \(0\,4\) is critical: after deleting it, vertex \(0\) can be placed into the first displayed color class. Thus this graph does not contradict the order-\(13\) exclusion above.

---

## 7. Gap

The original existence problem remains open after this analysis. A resolution would require either:

1. constructing a graph of order at least \(15\) satisfying all deletion-coloring conditions and proving that every edge deletion remains \(4\)-chromatic; or
2. extending the complement-clique argument, beginning with the \(K_5\) and \(5,5,4\) structure forced at order \(15\).

No computation was used in the lower-bound proof.