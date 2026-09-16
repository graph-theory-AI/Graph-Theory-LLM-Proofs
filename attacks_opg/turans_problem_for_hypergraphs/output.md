```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The K5^(3) bound, with equality characterized, holds whenever deleting one vertex makes the hypergraph 2-colorable.",
  "would_publish": false,
  "caveats": "Restricted-class result only; neither full conjecture is settled, and novelty is not claimed."
}
```

## 1. A sharp restricted case of the second conjecture

Call a 3-uniform hypergraph **2-colorable** if its vertex set has a partition into two classes, neither containing an edge. This is weak hypergraph coloring: an edge need only meet both classes.

For disjoint sets \(A,B\), let \(\mathcal B(A,B)\) contain all triples meeting both sets. Writing \(a=|A|\) and \(b=|B|\), its edge count is
\[
t(a,b)=\binom a2b+a\binom b2=\frac{ab(a+b-2)}2.
\]
It is \(K_5^{(3)}\)-free, since every five vertices include three in one part. Thus \(\mathcal B(n,n)\) has the conjectured number \(n^2(n-1)\) of edges.

Here is the partial result.

**Theorem.** Let \(H\) be a \(K_5^{(3)}\)-free 3-uniform hypergraph on \(2n\) vertices. Suppose there is a vertex \(v\) such that \(H-v\) is 2-colorable. Then
\[
e(H)\le n^2(n-1).
\]
Equality holds if and only if \(H\) is isomorphic to \(\mathcal B(n,n)\).

The hypothesis does **not** require \(H-v\) to contain every crossing triple. Nor is any restriction imposed in advance on the link of \(v\).

### 1.1. An auxiliary graph lemma

**Lemma.** Let \(G\) be an ordinary graph with vertex partition \(A\cup B\), where \(a=|A|\le b=|B|\). Suppose no four vertices comprising two from each part induce a complete graph. Then
\[
e(G)\le ab+\binom b2.
\]
If \(b>a\), equality holds only when \(A\) is independent, \(B\) is complete, and all \(A\)-\(B\) pairs are edges.

**Proof.** The case \(a=0\) is immediate. Take a maximum matching of size \(k\) in the bipartite graph consisting of the \(A\)-\(B\) edges of \(G\). Write its edges as
\[
a_1b_1,\ldots,a_kb_k,
\]
and let \(A_0,B_0\) be the unmatched vertices. Let \(q\) be the total number of nonedges of \(G\).

We count three disjoint categories of nonedges.

1. For every two matching edges, their four endpoints cannot form a \(K_4\). The two matching edges are present, so there is a nonedge between the two matched pairs. Different pairs of matching edges give distinct such nonedges. This contributes at least
   \[
   \binom k2.
   \]

2. Every pair in \(A_0\times B_0\) is a nonedge, contributing
   \[
   (a-k)(b-k).
   \]

3. For each \(i\), either all pairs between \(b_i\) and \(A_0\) are nonedges, or all pairs between \(a_i\) and \(B_0\) are nonedges. Otherwise the matching has an augmenting path of length three. Since \(a\le b\), this contributes at least \(a-k\) nonedges for each \(i\).

Consequently,
\[
q\ge \binom k2+(a-k)(b-k)+k(a-k)
=\binom k2+b(a-k).
\]
Moreover,
\[
\binom k2+b(a-k)-\binom a2
=\frac{(a-k)(2b-a-k+1)}2\ge0.
\]
Thus \(q\ge\binom a2\), giving
\[
e(G)\le\binom{a+b}{2}-\binom a2
=ab+\binom b2.
\]

Now suppose \(b>a\) and equality holds. The displayed inequalities force \(k=a\). The nonedges counted between matched pairs already number at least \(\binom a2=q\), so every unmatched vertex of \(B\) is adjacent to every other vertex of \(G\).

Choose an unmatched \(b_0\in B\). For each matched \(b_i\), replace the matching edge \(a_ib_i\) by \(a_ib_0\). Applying the same equality argument to this matching shows that \(b_i\), now unmatched, is also adjacent to every other vertex. Hence every vertex of \(B\) is universal.

It follows that \(A\) is independent: otherwise an edge of \(G[A]\), together with two vertices of \(B\), gives the forbidden \(K_4\). This proves the equality characterization. \(\square\)

### 1.2. Proof of the hypergraph bound

The case \(n=1\) is trivial. Assume \(n\ge2\).

Choose a 2-coloring
\[
V(H)\setminus\{v\}=A\cup B,
\qquad a=|A|\le b=|B|,
\qquad a+b=2n-1.
\]
Let
\[
D=E(\mathcal B(A,B))\setminus E(H-v),
\qquad d=|D|.
\]
Thus
\[
e(H-v)=t(a,b)-d.
\]

Let \(L\) be the ordinary link graph of \(v\):
\[
xy\in E(L)\quad\Longleftrightarrow\quad vxy\in E(H).
\]

For every missing crossing triple \(f\in D\), let \(p(f)\) be its unique pair lying entirely within one color class. Delete all these pairs from \(L\), obtaining
\[
L'=L-\{p(f):f\in D\}.
\]
At most \(d\) edges have been deleted, so
\[
e(L')\ge e(L)-d. \tag{1}
\]

**Claim.** \(L'\) contains no \(K_4\) with two vertices in \(A\) and two in \(B\).

Suppose such a four-set \(Q\) existed. Every triple of \(Q\) is crossing. If some \(f\in\binom Q3\) belonged to \(D\), then \(p(f)\) would be a pair of \(Q\) absent from \(L'\), a contradiction. Therefore all four triples of \(Q\) belong to \(H\).

All six pairs of \(Q\) also belong to \(L\). Hence all ten triples on \(Q\cup\{v\}\) belong to \(H\), producing a \(K_5^{(3)}\). This proves the claim.

The graph lemma and (1) now give
\[
e(L)\le ab+\binom b2+d.
\]
Therefore
\[
\begin{aligned}
e(H)
&=t(a,b)-d+e(L)\\
&\le t(a,b)+ab+\binom b2\\
&=t(a+1,b)\\
&=(n-1)(a+1)b\\
&\le (n-1)n^2,
\end{aligned}
\]
where the final inequality uses \((a+1)+b=2n\). This proves the bound.

### 1.3. Equality

Suppose
\[
e(H)=n^2(n-1).
\]
Equality in the product bound gives
\[
a=n-1,\qquad b=n.
\]
Every preceding inequality must also be an equality. In particular,
\[
e(L')=ab+\binom b2,
\qquad
e(L)-e(L')=d.
\]
The second equality implies that the pairs \(p(f)\), \(f\in D\), are all distinct and all belong to \(L\).

Because \(b>a\), the graph lemma shows that \(L'\) consists precisely of all \(A\)-\(B\) pairs and all pairs within \(B\).

There cannot be a missing crossing triple with two vertices in \(B\): its pair within \(B\) would have been deleted from \(L'\). Thus every member of \(D\) has two vertices in \(A\).

If \(D\ne\varnothing\), choose
\[
f=\{a_1,a_2,b_0\}\in D.
\]
Then \(a_1a_2\in E(L)\). Distinctness of the pairs \(p(f)\) implies that \(f\) is the only member of \(D\) containing the pair \(a_1a_2\).

The existence of \(a_1,a_2\) gives \(n\ge3\), so choose distinct \(b_1,b_2\in B\setminus\{b_0\}\). All four triples on
\[
Q=\{a_1,a_2,b_1,b_2\}
\]
belong to \(H\):

- \(a_1a_2b_1\) and \(a_1a_2b_2\) are present by the uniqueness just established;
- \(a_1b_1b_2\) and \(a_2b_1b_2\) are present because no missing crossing triple has two vertices in \(B\).

All six pairs of \(Q\) belong to \(L\): five belong to \(L'\), and the sixth is \(a_1a_2\). This again gives a \(K_5^{(3)}\) on \(Q\cup\{v\}\), a contradiction.

Therefore \(D=\varnothing\), and
\[
H=\mathcal B(A\cup\{v\},B)\cong\mathcal B(n,n).
\]
The converse follows from the construction. \(\square\)

## 2. Small exact cases of the unrestricted conjectures

These are elementary checks, not claims of new numerical Turán values.

### First conjecture: \(n\le2\)

The case \(n=1\) is immediate.

First consider a \(K_4^{(3)}\)-free 3-graph on five vertices. Each of its five four-subsets must contain a missing triple. Each missing triple lies in exactly two four-subsets. Hence there are at least three missing triples, and therefore at most
\[
\binom53-3=7
\]
edges.

Now let \(H\) have six vertices and be \(K_4^{(3)}\)-free. Every five-vertex induced subgraph has at most seven edges, and every edge lies in exactly three five-subsets. Thus
\[
3e(H)
=\sum_{S\in\binom{V(H)}5}e(H[S])
\le6\cdot7,
\]
so
\[
e(H)\le14=\frac12\cdot2^2(5\cdot2-3).
\]

The cyclic three-part construction with parts of size two has \(8+6=14\) edges. Its four-sets have distributions \(2+2\) or \(2+1+1\), and in either case the omitted orientation of a doubled part supplies a missing triple. Thus the bound is attained.

### Second conjecture: \(n\le3\)

The cases \(n=1,2\) follow from the total number of possible triples.

For \(n=3\), take any vertex \(v\). The five-vertex hypergraph \(H-v\) is \(K_5^{(3)}\)-free, so it has a missing triple \(T\). The partition
\[
T,\qquad V(H-v)\setminus T
\]
is a 2-coloring: the first class is a nonedge, and the second has only two vertices. The theorem therefore applies and gives
\[
e(H)\le18.
\]
Equality is attained precisely by \(\mathcal B(3,3)\).

## 3. What remains uncovered

The coloring hypothesis in the main theorem is genuinely additional.

For an explicit example, let
\[
F=K_6^{(3)}\setminus\{123,145,246\}.
\]
This is \(K_5^{(3)}\)-free: the three omitted triples have empty common intersection, so every five-subset contains at least one of them.

However, \(F\) is not 2-colorable:

- it has no independent four-set, since such a set would require four missing triples;
- a \(3+3\) coloring would require two disjoint missing triples, whereas the three listed missing triples are pairwise intersecting.

Consequently, the disjoint union of two copies of \(F\) is \(K_5^{(3)}\)-free and remains non-2-colorable after deletion of any single vertex. It lies outside the theorem’s scope. It is far below the conjectured edge bound and is not a counterexample.

Thus the argument proves a sharp extension theorem around the proposed two-part construction, but it does not control arbitrary \(K_5^{(3)}\)-free hypergraphs. For the first conjecture, only the small cases above are established here. Neither unrestricted conjecture, nor any improvement to its general upper bounds, is claimed.