```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for inversion-number-one tournaments, the cyclic C5, and a broad class controlled by a 3-vertex-strong module-free strong component.",
  "would_publish": false,
  "caveats": "The general low-connectivity and decomposable cases remain open; perturbations are assumed nonempty."
}
```

# 1. Statement and conventions

For tournaments \(S,S'\) on the same vertex set, let the **change graph**
\[
D=D(S,S')
\]
be the undirected graph whose edges are the pairs whose orientation is reversed between \(S\) and \(S'\). I interpret “locally finite perturbation” as meaning that \(D\) is locally finite and nonempty. The nonempty condition is necessary, since \(S\) itself is required to be \(T\)-free.

I do not prove the full conjecture. I prove three self-contained partial results:

1. the conjecture for every tournament whose minimum number of backward edges in a linear ordering is one;
2. the conjecture for the cyclic tournament \(C_5\), and more generally for a class described by a \(C_3\)-lexicographic decomposition;
3. the conjecture for every tournament that remains strongly connected after deleting at most two vertices and has no proper transitive homogeneous set. This extends to targets having such a tournament as a suitable strong component.

A recurring elementary observation is the following.

## Clean-transversal lemma

Let \(D\) be a locally finite graph, let \(A\) be finite, and let \(W_1,\dots,W_k\) be infinite pairwise disjoint sets. Then one can choose \(w_i\in W_i\) such that no edge of \(D\) joins two vertices of
\[
A\cup\{w_1,\dots,w_k\},
\]
apart from edges already lying wholly inside \(A\).

Indeed, choose the \(w_i\) successively. At each step only finitely many vertices are forbidden, since every previously selected vertex has finite degree in \(D\).

This is the mechanism that upgrades partite one-edge witnesses to robustness under arbitrary locally finite perturbations.

---

# 2. Tournaments one edge away from transitive

For a finite tournament \(T\), define
\[
\iota(T)=\min_{\prec}\left|\{(v,u):u\prec v\text{ and }v\to u\text{ in }T\}\right|,
\]
where the minimum is over all linear orders of \(V(T)\). Thus \(\iota(T)\) is the minimum number of arcs which must be reversed to make \(T\) transitive.

## Theorem 2.1

If \(T\) is nontransitive and \(\iota(T)=1\), then the conjecture holds for \(T\).

### Proof

Choose an ordering
\[
t_1\prec t_2\prec\cdots\prec t_n
\]
of \(T\) in which the unique backward arc is
\[
t_j\to t_i,\qquad i<j.
\]
Let \(S\) be the transitive tournament on \(\mathbb Q\), oriented by
\[
x\to y\quad\Longleftrightarrow\quad x<y.
\]
It is clearly \(T\)-free.

Let \(S'\) be a nontrivial locally finite perturbation, with change graph \(D\). Choose a changed pair \(x<y\). Thus \(x\to y\) in \(S\) and \(y\to x\) in \(S'\).

Map \(t_i\) to \(x\) and \(t_j\) to \(y\). For every other \(k\), choose an infinite open interval \(I_k\) such that:

- the intervals \(I_1,\dots,I_{i-1}\) occur in increasing order below \(x\);
- \(I_{i+1},\dots,I_{j-1}\) occur in increasing order between \(x\) and \(y\);
- \(I_{j+1},\dots,I_n\) occur in increasing order above \(y\).

Choose one point \(x_k\in I_k\) from each interval using the clean-transversal lemma with fixed set \(\{x,y\}\). Hence the only changed pair among the selected vertices is \(xy\).

In the inherited rational order, all selected arcs are forward except \(y\to x\). Consequently they induce \(T\) in \(S'\). ∎

The construction is exact in the following sense.

## Proposition 2.2

The dense transitive tournament on \(\mathbb Q\) has the required property for a nontransitive tournament \(T\) if and only if \(\iota(T)=1\).

### Proof

Sufficiency is Theorem 2.1. Conversely, reverse only one arc of the transitive tournament. Every finite subtournament of the result has at most one backward arc in the inherited order. Thus any nontransitive tournament appearing after such a perturbation has inversion number exactly one. ∎

This covers \(C_3\), every nontransitive tournament on four vertices, and many larger tournaments.

---

# 3. A lexicographic construction and the cyclic \(C_5\)

Let \(C_3\) be the directed cycle \(0\to1\to2\to0\). Define a countable tournament \(S_\triangle\) as follows. Its vertices are the eventually-zero sequences
\[
x=(x_0,x_1,\dots)\in\{0,1,2\}^{\mathbb N}.
\]
For distinct \(x,y\), let \(k\) be their first differing coordinate and put
\[
x\to y\text{ in }S_\triangle
\quad\Longleftrightarrow\quad
x_k\to y_k\text{ in }C_3.
\]
This is the countable infinite lexicographic power of \(C_3\).

A tournament is **prime** if it has no homogeneous set of size between \(2\) and \(|T|-1\).

## Proposition 3.1

Let \(T\) be a prime tournament of order greater than three. Suppose there is an arc \(e\) of \(T\) such that, after reversing \(e\), the resulting tournament \(T^e\) has a homogeneous partition
\[
V(T)=V_0\cup V_1\cup V_2
\]
with:

1. quotient tournament \(C_3\);
2. every \(T^e[V_i]\) transitive;
3. the endpoints of \(e\) lying in distinct parts.

Then \(S_\triangle\) is \(T\)-free and every nontrivial locally finite perturbation of \(S_\triangle\) contains \(T\).

### Proof

First, \(S_\triangle\) is \(T\)-free. Suppose a copy \(X\cong T\) existed. Consider the first coordinate at which the sequences in \(X\) are not all equal. Partition \(X\) according to their symbols at that coordinate. Every part is homogeneous in \(X\). Since \(T\) is prime, every nonempty part must be a singleton. There are at most three parts, contradicting \(|T|>3\).

Now let \(S'\) be a locally finite nontrivial perturbation, and choose a changed arc \(x\to y\) of \(S_\triangle\). At the first coordinate where \(x\) and \(y\) differ, they lie in two child cylinders corresponding to an arc of \(C_3\). Since \(C_3\) is arc-transitive, identify these cylinders with the two parts of \(T^e\) containing the endpoints of the reversed arc; identify the third cylinder with the remaining part.

Inside any cylinder of \(S_\triangle\), one can realize an arbitrary finite transitive tournament with any specified vertex represented by a prescribed point such as \(x\) or \(y\). Moreover, the remaining roles can be represented by infinite subcylinders so that every transversal gives the same transitive ordering. To see this, choose distinct later coordinates at which the role sequences first diverge from the prescribed point. A role intended to precede the prescribed point takes the symbol which beats its symbol at that coordinate; a role intended to follow it takes the symbol which it beats. Ordering the divergence coordinates appropriately gives the desired linear order.

Thus there are infinite candidate sets for all vertices of \(T^e\) other than the two endpoints, and every transversal together with \(x,y\) induces \(T^e\) in \(S_\triangle\). Apply the clean-transversal lemma to avoid all changed pairs except \(xy\). Reversing \(xy\) then changes \(T^e\) into \(T\). ∎

## Corollary 3.2: the cyclic \(C_5\)

The conjecture holds for the regular cyclic tournament \(C_5\).

### Proof

Label \(C_5\) by \(\mathbb Z_5\), with
\[
i\to j\quad\Longleftrightarrow\quad j-i\pmod 5\in\{1,2\}.
\]
Reverse the arc \(0\to2\). In the resulting tournament, the partition
\[
A=\{2,3\},\qquad B=\{4,0\},\qquad C=\{1\}
\]
has
\[
A\to B\to C\to A,
\]
with internal orders
\[
2\to3,\qquad 4\to0.
\]
The reversed arc is \(2\to0\), whose endpoints lie in distinct parts.

It remains only to note that \(C_5\) is prime. One quick verification uses regularity. If \(M\) were a nontrivial module, every vertex of \(M\) would have the same number of outneighbours outside \(M\), hence \(C_5[M]\) would be regular. Thus \(|M|\) would be odd, leaving only \(|M|=3\). But then one of the two outside vertices would dominate all three vertices of \(M\), giving it outdegree at least three, contrary to regular outdegree two. Proposition 3.1 applies. ∎

This case is not covered by Theorem 2.1: \(C_5\) is not one edge away from a transitive tournament.

---

# 4. A two-vertex amalgamation construction

The next construction covers a broad high-connectivity class.

Call a tournament \(U\) **3-vertex-strong** here if
\[
U-X\text{ is strongly connected for every }X\subseteq V(U),\ |X|\le 2.
\]

## Lemma 4.1: two-vertex amalgamation

Let \(U\) be 3-vertex-strong. Let \(A\) and \(B\) be \(U\)-free tournaments with
\[
V(A)\cap V(B)=\{x,y\},
\]
and suppose they agree on the arc \(xy\). Orient every remaining cross-pair uniformly, say
\[
B\setminus\{x,y\}\ \longrightarrow\ A\setminus\{x,y\}.
\]
Then the resulting tournament is \(U\)-free.

### Proof

Suppose \(W\cong U\). Put
\[
P=W\cap(B\setminus\{x,y\}),\quad
Q=W\cap(A\setminus\{x,y\}),\quad
R=W\cap\{x,y\}.
\]
If both \(P\) and \(Q\) are nonempty, then every arc between them is directed from \(P\) to \(Q\). Hence \(W-R\) is not strongly connected. But \(|R|\le2\), contradicting the 3-vertex-strong property of \(U\).

Thus \(P=\varnothing\) or \(Q=\varnothing\), so \(W\) lies wholly in \(A\) or wholly in \(B\), also impossible. ∎

For an arc \(e=uv\) of \(U\), write \(U^e\) for the tournament obtained by reversing \(e\). Define the **partite fan** \(F(U,e)\) by replacing every vertex of \(U^e\) other than \(u,v\) by a countably infinite transitive block, while retaining \(u,v\) as singleton blocks.

## Theorem 4.2: fan criterion

Suppose:

1. \(U\) is 3-vertex-strong;
2. for some arc \(e\), the partite fan \(F(U,e)\) is \(U\)-free.

Then there is a countably infinite \(U\)-free tournament such that every nontrivial locally finite perturbation contains \(U\).

### Proof

Start with a two-vertex tournament \(S_0\). Given a countable \(U\)-free tournament \(S_m\), enumerate its arcs. For each arc \(x\to y\), attach a fresh copy of \(F(U,e)\), identifying the reversed orientation of \(e\) in \(U^e\) with \(x\to y\). Orient all pairs from the fresh vertices to all old vertices other than \(x,y\) in one uniform direction.

Attach these fans one at a time. Lemma 4.1 shows after every attachment that the tournament remains \(U\)-free. The countable union remains \(U\)-free, since any finite copy of \(U\) would occur at a finite stage. Call the resulting tournament \(S_{m+1}\), and put
\[
S=\bigcup_{m<\omega}S_m.
\]
Every arc of \(S\) eventually receives such a fan.

Let \(S'\) be a nontrivial locally finite perturbation and choose a changed arc \(x\to y\) of \(S\). Consider the fan attached to \(xy\). Each of the other vertex roles of \(U^e\) has an infinite transitive block, and every transversal gives \(U^e\) with the reversed arc represented by \(xy\). By the clean-transversal lemma, choose a transversal on which no other pair was changed. In \(S'\), the reversal of \(xy\) converts this copy of \(U^e\) into \(U\). ∎

There is a convenient structural condition implying the fan hypothesis.

## Lemma 4.3

Every nontransitive finite tournament \(U\) has an arc \(e\) such that \(U^e\not\cong U\).

### Proof

Let \(d(v)\) be the outdegree of \(v\). If reversing an arc \(u\to v\) produced an isomorphic tournament, invariance of the sum of squared outdegrees would give
\[
0=(d(u)-1)^2+(d(v)+1)^2-d(u)^2-d(v)^2
  =2(d(v)-d(u)+1),
\]
so \(d(u)=d(v)+1\).

If every arc reversal preserved the isomorphism type, this equality would hold on every arc. On a directed triangle
\[
u\to v\to w\to u
\]
it would imply
\[
d(u)=d(v)+1,\quad d(v)=d(w)+1,\quad d(w)=d(u)+1,
\]
a contradiction. Every nontransitive tournament contains a directed triangle. ∎

## Corollary 4.4

Suppose \(U\) is 3-vertex-strong and has no proper nontrivial homogeneous set inducing a transitive tournament. Then the conjecture holds for \(U\). In particular, it holds whenever \(U\) is both prime and 3-vertex-strong.

### Proof

Choose \(e\) with \(U^e\not\cong U\) by Lemma 4.3. I claim \(F(U,e)\) is \(U\)-free.

Suppose a copy of \(U\) occurred in \(F(U,e)\). Its intersection with each quotient block would be a homogeneous transitive set in that copy. By hypothesis, each occupied block must therefore contain exactly one vertex, unless the whole copy lies in one block. The latter is impossible because the blocks are transitive and \(U\) is not.

Thus the copy uses one vertex from each of the \(|U|\) quotient blocks, and hence induces \(U^e\), contradicting \(U^e\not\cong U\). Apply Theorem 4.2. ∎

---

# 5. Extension through a strong component

The preceding construction also handles some non-strong targets.

## Theorem 5.1

Let \(T\) be a nontransitive tournament with a strong component \(U\) such that:

1. \(U-X\) is strongly connected whenever \(|X|\le2\);
2. \(U\) has no proper nontrivial transitive homogeneous set;
3. no other strong component of \(T\) contains an induced copy of \(U\).

Then the conjecture holds for \(T\).

In particular, condition 3 is automatic if \(U\) is the unique largest strong component of \(T\).

### Proof

Choose an arc \(e\) of \(U\) such that \(U^e\not\cong U\). Starting from \(T^e\), replace every vertex other than the endpoints of \(e\) by a countably infinite transitive block. Call the resulting tournament \(P\).

I claim that \(P\) is \(U\)-free. The strong components of \(T\) are linearly ordered, and this ordering remains valid after reversing the internal arc \(e\). Since \(U\) is strongly connected, a copy of \(U\) in \(P\) would have to lie inside the blow-up of a single strong component.

Inside such a blow-up, the intersection with each transitive block is a transitive homogeneous set in \(U\). By condition 2, a copy of \(U\) must therefore use at most one vertex from every block. In the distinguished component this would give \(U\cong U^e\), impossible. In any other component it would give an induced copy of \(U\) in that component, contrary to condition 3.

Now run the construction of Theorem 4.2, attaching a copy of \(P\) over every arc rather than merely \(F(U,e)\). Lemma 4.1, applied with forbidden tournament \(U\), ensures that the resulting countable tournament \(S\) remains \(U\)-free, and therefore \(T\)-free.

After a locally finite perturbation, select a changed arc and a clean transversal in its attached copy of \(P\). Reversing the distinguished arc converts the induced \(T^e\) into \(T\). ∎

---

# 6. A concrete high-connectivity example: cyclic \(C_7\)

Let \(C_7\) have vertex set \(\mathbb Z_7\), with
\[
i\to j\quad\Longleftrightarrow\quad j-i\pmod 7\in\{1,2,3\}.
\]

It satisfies the hypotheses of Corollary 4.4.

First, deleting at most two vertices leaves a strongly connected tournament. List the surviving vertices in cyclic order. The gap between consecutive survivors is at most three, so every consecutive pair is oriented forward around the circle. Hence the survivors contain a directed Hamilton cycle.

Second, \(C_7\) is prime. Every vertex has outdegree three. If \(M\) were a module, all vertices of \(M\) would have the same external outdegree, so \(C_7[M]\) would be regular. Thus \(|M|\) is odd, leaving only \(|M|=3\) or \(5\).

- If \(|M|=5\), one outside vertex must dominate all five vertices of \(M\), contradicting outdegree three.
- If \(|M|=3\), the three vertices induce a directed triangle and exactly two outside vertices dominate \(M\). Each of those already has three outneighbours in \(M\), so each would have to lose to the other, impossible.

Therefore the conjecture holds for \(C_7\). This is genuinely outside the inversion-number-one class.

More generally, Theorem 5.1 applies whenever \(C_7\) is a unique largest strong component of the target.

---

# 7. Finite recognition of the fan condition

Although \(F(U,e)\) is infinite, whether it contains \(U\) is decidable by a finite brute-force test.

Let \(B=U^e\), with the endpoints of \(e\) designated as singleton blocks. Then \(U\) embeds in \(F(U,e)\) if and only if there is a map
\[
f:V(U)\to V(B)
\]
such that:

1. the inverse image of either designated endpoint has size at most one;
2. every fiber \(f^{-1}(b)\) induces a transitive tournament;
3. whenever \(f(x)\ne f(y)\), the orientation of \(xy\) in \(U\) agrees with the orientation of \(f(x)f(y)\) in \(B\).

Thus one can test every arc \(e\) by enumerating the \(n^n\) maps \(f\), where \(n=|U|\). This gives a completely specified \(O(n^n\operatorname{poly}(n))\) test for the hypothesis of Theorem 4.2. I have not run this enumeration and claim no additional computational cases.

---

# 8. Remaining gap

These results do not exhaust all nontransitive tournaments. The main untreated region consists of low-connectivity tournaments with nontrivial modular structure. For example,
\[
C_3[C_3,1,1],
\]
the tournament obtained by replacing one vertex of a directed triangle by another directed triangle, is not covered:

- it has inversion number at least two;
- it is not prime;
- it is not 3-vertex-strong.

The two-vertex amalgamation proof fails precisely because the two common endpoints can separate an unintended copy of the forbidden tournament. The \(C_3\)-lexicographic proof, on the other hand, relies on primeness to exclude pre-existing copies. A new idea is needed to reconcile these two phenomena.

Thus there is no complete proof or counterexample here, but the conjecture is established for several infinite classes, including both cyclic \(C_5\) and cyclic \(C_7\).