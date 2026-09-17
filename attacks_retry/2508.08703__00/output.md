```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every 6-regular (4,1)-graph has at least 16 vertices, and an order-16 example would necessarily have independence number 5.",
  "would_publish": false,
  "caveats": "Existence at order 16 or larger remains unresolved; the novelty of these bounds relative to the full source paper has not been checked."
}
```

# A stronger order bound

I prove the following partial result.

> **Theorem.** Let \(G\) be a \(6\)-regular, \(4\)-vertex-critical graph with no critical edge. Then
> \[
> |V(G)|\ge 16.
> \]
> If \(|V(G)|=16\), then \(\alpha(G)=5\), and every proper \(3\)-coloring of every \(G-v\) has three color classes of size \(5\).

The key improvement over the supplied attempt is an exclusion of order \(15\). Its suggested “cycle of pairs” configuration is indeed forced; vertex-criticality at vertices outside the initial independent set then rules it out.

All arguments below are self-contained. Graphs are finite and simple. Write
\[
N(S)=\bigcup_{s\in S}N_G(s).
\]

## 1. Balance in every deletion coloring

> **Lemma 1.** For every \(v\in V(G)\), every proper \(3\)-coloring of \(G-v\) has exactly two neighbors of \(v\) in each color class.

**Proof.** Every color must occur on \(N(v)\), or the coloring extends to \(G\).

If a color occurs on exactly one neighbor \(x\) of \(v\), giving \(v\) that color produces a proper \(3\)-coloring of \(G-vx\). Thus \(vx\) would be critical. Each color therefore occurs at least twice on \(N(v)\). Since \(d(v)=6\), all three multiplicities equal two. \(\square\)

This is the balance observation from the previous attempt, verified directly.

## 2. Expansion of small independent sets

We first record two consequences that streamline the exclusion of orders below \(15\).

> **Lemma 2.**
> 1. If \(x,y\) are distinct nonadjacent vertices, then
>    \[
>    |N(x)\cap N(y)|\le4,\qquad |N(x)\cup N(y)|\ge8.
>    \]
> 2. If \(S\) is an independent set of size four, then
>    \[
>    |N(S)|\ge10.
>    \]

**Proof.**

For the first assertion, take a \(3\)-coloring of \(G-x\). The color class containing \(y\) contains two neighbors of \(x\), by Lemma 1. Neither is adjacent to \(y\). Hence
\[
|N(x)\setminus N(y)|\ge2.
\]
Both vertices have degree six, giving the stated bounds.

For the second assertion, let
\[
S=\{s_1,s_2,s_3,s_4\},\qquad R=N(S),\qquad r=|R|.
\]
The first assertion gives \(r\ge8\). Suppose \(r\le9\), and put
\[
F_i=R\setminus N(s_i).
\]
Then
\[
|F_i|=r-6,\qquad |F_i\cap F_j|\le r-8\le1\quad(i\ne j). \tag{2.1}
\]

Fix \(i\), and color \(G-s_i\) with three colors. Each color class contains at least two vertices of \(R\), because it contains two neighbors of \(s_i\). A class containing \(s_j\), for \(j\ne i\), has its \(R\)-portion contained in \(F_j\).

Consequently, two vertices of \(S\setminus\{s_i\}\) cannot share a color: their class would have at least two vertices in \(F_j\cap F_k\), contradicting (2.1). Thus the other three vertices of \(S\) occupy the three different classes. It follows that
\[
r\le 3(r-6).
\]
This already rules out \(r=8\).

If \(r=9\), equality holds. The three \(R\)-portions are exactly the three sets \(F_j\) with \(j\ne i\), so those sets are pairwise disjoint. Varying \(i\) shows that all four \(F_j\)'s are pairwise disjoint. But they are four sets of size three in a set of size nine, a contradiction. \(\square\)

### Consequence: \(n\ge15\)

Put \(n=|V(G)|\) and \(\alpha=\alpha(G)\).

Every color class of every \(G-v\) contains at least two vertices. For such a class \(C\), an independent pair in \(C\) has at least eight neighbors, all outside \(C\). Thus
\[
|C|\le n-8.
\]
Summing over the three classes gives
\[
n-1\le3(n-8),
\]
so \(n\ge12\). In particular, a deletion coloring has a class of size at least four, and hence \(\alpha\ge4\).

A maximum independent set contains an independent four-set. By Lemma 2 its neighborhood has at least ten vertices, all outside the maximum independent set. Therefore
\[
\alpha\le n-10.
\]
Since \(n-1\le3\alpha\), we obtain
\[
n-1\le3(n-10),
\]
and hence \(n\ge15\).

## 3. An eight-neighbor independent triple forces a large independent set

The next lemma is the additional structural ingredient.

> **Lemma 3.** If \(T=\{t_1,t_2,t_3\}\) is independent and
> \[
> |N(T)|=8,
> \]
> then \(\alpha(G)\ge7\).
>
> Consequently, if \(\alpha(G)\le6\), every independent triple \(T\) satisfies
> \[
> |N(T)|\ge9. \tag{3.1}
> \]

**Proof.** Put \(O=N(T)\), so \(|O|=8\), and define
\[
P_i=O\setminus N(t_i).
\]
Each \(P_i\) has size two. By Lemma 2, the union of the neighborhoods of any two vertices of \(T\) already has size at least eight, and hence equals \(O\). Therefore the three pairs \(P_1,P_2,P_3\) are pairwise disjoint. Let
\[
Z=O\setminus(P_1\cup P_2\cup P_3);
\]
then \(|Z|=2\).

Fix \(i\), and take a \(3\)-coloring of \(G-t_i\). For \(j\ne i\), the class containing \(t_j\):

- has its \(O\)-portion contained in \(P_j\); and
- contains two neighbors of \(t_i\).

Thus its \(O\)-portion is exactly \(P_j\). The other two vertices of \(T\) have different colors, because their \(P\)-sets are disjoint. The third class therefore has \(O\)-portion
\[
P_i\cup Z.
\]
It follows, for each \(i\), that \(P_i\cup Z\) is independent. In particular, writing \(Z=\{z,z'\}\), the vertices \(z,z'\) are nonadjacent, and neither has a neighbor in \(P_1\cup P_2\cup P_3\).

Now color \(G-z\) with three colors. Both \(z\) and \(z'\) are adjacent to every vertex of \(T\). Hence no vertex of \(T\) has the color of \(z'\). Also, by balance at \(z\), all three vertices of \(T\) cannot have the same color. They therefore split \(2+1\) between the other two colors.

Suppose \(t_j,t_k\) share a color and \(t_i\) has the other color. No vertex of \(P_1\cup P_2\cup P_3\) can share the color of \(t_j,t_k\), since \(P_j\cap P_k=\varnothing\). Only vertices of \(P_i\) can share the color of \(t_i\). Consequently, all four vertices of \(P_j\cup P_k\) have the color of \(z'\).

This color class already contains \(z'\) and those four vertices. None is a neighbor of \(z\). By Lemma 1, the class additionally contains two neighbors of \(z\). Its size is therefore at least seven.

Finally, Lemma 2 gives \(|N(T)|\ge8\) for any independent triple. If \(\alpha(G)\le6\), the equality case just excluded cannot occur, proving (3.1). \(\square\)

## 4. Excluding order \(15\)

Assume for contradiction that \(n=15\). The preceding bounds give
\[
5=\left\lceil\frac{14}{3}\right\rceil\le\alpha(G)\le15-10=5.
\]
Thus
\[
\alpha(G)=5, \tag{4.1}
\]
and every deletion coloring has class sizes \(5,5,4\).

Fix an independent set \(Q\) of size five, put
\[
R=V(G)\setminus Q,
\]
and, for \(q\in Q\), define
\[
F_q=R\setminus N_G(q).
\]
Equivalently, \(F_q\) is the external neighborhood of \(q\) in \(H=\overline G\). Since \(|R|=10\),
\[
|F_q|=4. \tag{4.2}
\]
Lemma 2 gives
\[
|F_q\cap F_{q'}|\le2 \qquad(q\ne q'), \tag{4.3}
\]
and Lemma 3, together with (4.1), gives
\[
|F_q\cap F_{q'}\cap F_{q''}|\le1
\quad\text{for distinct }q,q',q''\in Q. \tag{4.4}
\]

### 4.1 Every deletion in \(Q\) has a prescribed pattern

Fix \(q\in Q\), and consider a \(3\)-coloring of \(G-q\).

Each class contains at least two vertices of \(R\). By (4.4), no class contains three vertices of \(Q\setminus\{q\}\). The distribution of those four vertices among the classes is therefore either
\[
(2,1,1)\quad\text{or}\quad(2,2,0).
\]

A class containing two vertices of \(Q\) has its \(R\)-portion contained in the intersection of the corresponding \(F\)-sets. By (4.3), this portion has exactly two vertices. Such a class therefore has size four. The pattern \((2,2,0)\) would give two classes of size four, contrary to the required sizes \(5,5,4\).

Thus the pattern is always \((2,1,1)\). Denote the singleton vertices by \(a,b\) and the paired vertices by \(c,d\). The \(R\)-portions of the two size-five classes are exactly \(F_a,F_b\), while the size-four class has \(R\)-portion
\[
X=R\setminus(F_a\cup F_b)=F_c\cap F_d.
\]
In particular,
\[
F_a\cap F_b=\varnothing,\qquad |X|=2. \tag{4.5}
\]

Balance at the deleted vertex \(q\) now gives
\[
F_q\subseteq F_a\cup F_b,\qquad
|F_q\cap F_a|=|F_q\cap F_b|=2. \tag{4.6}
\]

These conclusions hold for every \(q\in Q\), with the roles of \(a,b,c,d\) depending on \(q\).

### 4.2 The cycle of pairs is forced

For \(x\in R\), let
\[
m(x)=|\{q\in Q:x\in F_q\}|.
\]
A single partition in (4.5) shows that every vertex of \(R\) belongs to at least one \(F_q\). Equation (4.6), applied to that \(q\), shows that it belongs to at least one further \(F\)-set. Hence \(m(x)\ge2\) for every \(x\in R\).

But
\[
\sum_{x\in R}m(x)=\sum_{q\in Q}|F_q|=5\cdot4=20=2|R|.
\]
Therefore
\[
m(x)=2\qquad(x\in R). \tag{4.7}
\]

Construct a loopless multigraph \(M\) on vertex set \(Q\), with one edge for each \(x\in R\), joining the two vertices whose \(F\)-sets contain \(x\). Each vertex of \(M\) has degree four. By (4.6), each vertex has exactly two distinct neighbors, joined to it by two parallel edges each.

The underlying simple graph is consequently a \(2\)-regular graph on five vertices, necessarily a \(5\)-cycle. Label its vertices cyclically as \(q_0,\ldots,q_4\). There is a partition
\[
R=X_0\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}X_4,\qquad |X_i|=2,
\]
such that
\[
F_{q_i}=X_{i-1}\cup X_i \qquad(i\pmod5). \tag{4.8}
\]

Moreover, each \(F_{q_i}\) is independent in \(G\): it appears as the \(R\)-portion of a size-five color class when a neighboring vertex of the underlying cycle is deleted.

### 4.3 The complement has only six cliques of size five

Work now in \(H=\overline G\). It is \(8\)-regular. By (4.7), every vertex of \(R\) has exactly two neighbors in \(Q\), so \(H[R]\) is \(6\)-regular.

Equation (4.8) and the independence of every \(F_{q_i}\) imply that \(H[R]\) contains:

- the edge inside each pair \(X_i\); and
- all edges between each pair of cyclically consecutive \(X_i\)'s.

This spanning graph is \(5\)-regular. The remaining edges of \(H[R]\) therefore form a perfect matching, joining vertices in nonconsecutive pairs \(X_i\).

It follows that
\[
\omega(H[R])\le4. \tag{4.9}
\]
Indeed, a clique meeting only pairwise consecutive parts has at most four vertices. Otherwise, choose clique vertices \(x\in X_i\) and \(y\in X_j\) from nonconsecutive parts. Their edge belongs to the additional matching. Every further clique vertex must therefore be adjacent to both through the original spanning graph, and hence must lie in the unique part whose index is adjacent to both \(i\) and \(j\) on the \(5\)-cycle. That part has only two vertices.

We can now list all \(K_5\)'s of \(H\):

- \(Q\) itself; and
- the five sets
  \[
  \{q_i\}\cup F_{q_i},\qquad i=0,\ldots,4.
  \]

To check completeness of the list, (4.9) excludes a \(K_5\) contained in \(R\). A clique containing a vertex of \(R\) contains at most two vertices of \(Q\), by (4.7). If it contains two, their common neighborhood in \(R\) has size at most two, so its total size is at most four. If it contains exactly one \(q_i\), its four remaining vertices must be all of \(F_{q_i}\).

### 4.4 Deleting a vertex of \(R\) is impossible

Choose \(r\in R\). A \(3\)-coloring of \(G-r\) would partition \(H-r\) into cliques of sizes \(5,5,4\).

One of the size-five cliques cannot be \(Q\), since every other \(K_5\) of \(H\) intersects \(Q\). Thus both size-five cliques are of the form
\[
\{q_i\}\cup F_{q_i}.
\]
Together they use two vertices of \(Q\) and eight vertices of \(R\). The remaining size-four clique would consequently consist of three vertices of \(Q\) and one vertex of \(R\).

That is impossible: every vertex of \(R\) has only two neighbors in \(Q\) in \(H\).

This contradiction excludes \(n=15\). Combined with the earlier bound, it proves
\[
\boxed{|V(G)|\ge16}.
\]

## 5. Necessary structure at order \(16\)

Suppose now that \(n=16\). The general bounds give
\[
5\le\alpha(G)\le6.
\]

Assume \(\alpha(G)=6\), and choose an independent set \(Q\) of size six. Again put \(R=V(G)\setminus Q\), so \(|R|=10\), and
\[
F_q=R\setminus N(q).
\]
As before,
\[
|F_q|=4,\qquad |F_q\cap F_{q'}|\le2.
\]
Since \(\alpha(G)\le6\), Lemma 3 also gives
\[
|F_q\cap F_{q'}\cap F_{q''}|\le1.
\]

Fix \(q\in Q\), and color \(G-q\). Every class has at least two vertices of \(R\), so no class can contain three vertices of \(Q\setminus\{q\}\). The other five vertices of \(Q\) must therefore be distributed as \((2,2,1)\).

The two classes containing pairs of \(Q\)-vertices each contain at most two vertices of \(R\). The class containing a singleton of \(Q\) contains at most four vertices of \(R\). Thus the three classes cover at most
\[
2+2+4=8
\]
vertices of \(R\), although \(|R|=10\). This contradiction proves \(\alpha(G)=5\).

Every coloring of \(G-v\) consequently has three classes \(A_1,A_2,A_3\), each of size five. There is a further useful numerical constraint. If \(e_{ij}\) counts edges between \(A_i\) and \(A_j\), regularity and balance give
\[
e_{ij}+e_{ik}=6\cdot5-2=28.
\]
Solving these three equations yields
\[
e_{12}=e_{13}=e_{23}=14.
\]

Thus an order-\(16\) example would have, for every deleted vertex:

- three independent color classes of size five;
- exactly two neighbors of the deleted vertex in each class; and
- exactly fourteen edges between each pair of classes.

## 6. What remains unresolved

This does **not** answer the existence question. It excludes all orders at most \(15\) and reduces order \(16\) to the independence-number-five case described above.

No computational enumeration has been performed or claimed. In particular, the order-\(16\) conditions have not been shown inconsistent, and no construction satisfying them is supplied.