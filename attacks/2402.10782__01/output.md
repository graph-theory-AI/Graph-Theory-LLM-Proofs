```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The maximum-degree-1 case is polynomial-time solvable—more generally, maximum-degree-d FAS is FPT in d—while the path case reduces to excluding undirected cycles from a maximum-degree-2 backedge graph and is not resolved here.",
  "would_publish": false,
  "caveats": "The dynamic program safely merges histories for degree constraints but not for the connectivity information needed to recognize linear forests."
}
```

# Mathematical writeup

## 1. Definitions and results

Let \(T\) be a tournament on \(n\) vertices. For an ordering
\[
\pi=(v_1,\ldots,v_n),
\]
let \(B_\pi\) be its set of backward arcs:
\[
B_\pi=\{v_jv_i\in A(T):i<j\}.
\]
We identify \(B_\pi\) with its underlying undirected graph when discussing degrees and cycles.

I prove the following.

### Theorem 1
For every integer \(d\geq 1\), one can decide in time
\[
2^{O(d)}n^{O(1)}
\]
whether a tournament has a feedback arc set whose underlying graph has maximum degree at most \(d\).

In particular, the \(\mathcal C\)-FAS problem is in \(\mathrm P\) when \(\mathcal C\) is the class of graphs of maximum degree at most \(1\).

For paths, I establish the exact reformulation:

### Proposition 2
A tournament has a path-FAS if and only if it has an ordering \(\pi\) for which \(B_\pi\) is a linear forest, i.e. an acyclic graph of maximum degree at most \(2\).

Thus Theorem 1 with \(d=2\) gives the degree part, but not the necessary acyclicity condition. I do not settle the complexity of this remaining problem.

---

## 2. From feedback arc sets to backward-edge orderings

The following elementary equivalence is fundamental.

### Lemma 3
For any \(d\geq 0\), the following are equivalent:

1. \(T\) has a feedback arc set \(F\) with \(\Delta(\underline F)\leq d\);
2. \(T\) has an ordering \(\pi\) with \(\Delta(B_\pi)\leq d\).

#### Proof
Suppose first that \(F\) is such a feedback arc set. Choose a topological ordering \(\pi\) of \(T-F\). Every backward arc in \(\pi\) must belong to \(F\), since an arc outside \(F\) remains in \(T-F\) and must point forward in a topological ordering. Thus
\[
B_\pi\subseteq F,
\]
and consequently \(\Delta(B_\pi)\leq d\).

Conversely, if \(\Delta(B_\pi)\leq d\), deleting \(B_\pi\) leaves every arc pointing forward in \(\pi\), so \(B_\pi\) is itself a feedback arc set of maximum degree at most \(d\). ∎

---

## 3. Score localization

Write \(s(v)=d_T^+(v)\), and define the score-center
\[
a(v)=n-s(v).
\]

Suppose \(v=v_i\) is in position \(i\) of an ordering \(\pi\). Let
\[
L(v)=|\{j<i:v\to v_j\}|
\]
be the number of backward arcs from \(v\) to its left, and let
\[
R(v)=|\{j>i:v_j\to v\}|
\]
be the number of backward arcs from its right into \(v\). Then
\[
d_{B_\pi}(v)=L(v)+R(v).
\]
Moreover,
\[
s(v)=L(v)+(n-i-R(v))
     =n-i+L(v)-R(v).
\]
Therefore
\[
a(v)=n-s(v)=i-L(v)+R(v),
\]
and hence
\[
|i-a(v)|\leq L(v)+R(v)=d_{B_\pi}(v).
\]

Consequently, in every ordering with \(\Delta(B_\pi)\leq d\), vertex \(v\) must occur in the interval
\[
I_v=[\ell(v),r(v)]
   =[\,\max\{1,a(v)-d\},\min\{n,a(v)+d\}\,].
\tag{1}
\]

This confines every vertex to at most \(2d+1\) possible positions.

---

## 4. The dynamic program

For \(0\leq i\leq n\), let
\[
D_i=\{v:r(v)\leq i\}
\]
be the vertices that must have appeared among the first \(i\) positions, and let
\[
X_i=\{v:\ell(v)\leq i<r(v)\}.
\]
Every interval-respecting prefix \(S\) of size \(i\) has the form
\[
S=D_i\cup Y,\qquad Y\subseteq X_i.
\tag{2}
\]

### Boundary-size bound

If a complete interval-respecting ordering exists, then
\[
|X_i|\leq 4d
\tag{3}
\]
for every \(1\leq i<n\).

Indeed, for \(v\in X_i\),
\[
\ell(v)\leq i<r(v)
\]
implies
\[
i-d<a(v)\leq i+d.
\]
Thus every interval \(I_v\), for \(v\in X_i\), lies inside
\[
[i-2d+1,i+2d],
\]
which contains at most \(4d\) positions. Since the intervals must receive distinct positions, more than \(4d\) such vertices is impossible. We may therefore reject immediately if (3) fails. Otherwise there are at most \(2^{4d}\) possible sets \(Y\) at each layer.

### Transition

A state at layer \(i\) is a reachable set
\[
S=D_i\cup Y,\qquad Y\subseteq X_i,\qquad |S|=i.
\]

For \(v\notin S\), consider placing \(v\) in position \(i+1\). Its total backward degree in every completion of this prefix is already determined:
\[
\beta(v,S)
 =
 |\{u\in S:v\to u\}|
 +
 |\{w\notin S\cup\{v\}:w\to v\}|.
\tag{4}
\]
The first term counts its backward arcs to earlier vertices; the second counts its backward arcs from later vertices. Crucially, (4) depends only on the set \(S\), not on the internal order of \(S\) or the future order.

We allow the transition \(S\to S\cup\{v\}\) precisely when:

1. \(i+1\in I_v\);
2. \(\beta(v,S)\leq d\);
3. \(D_{i+1}\subseteq S\cup\{v\}\).

The new state is represented as
\[
Y'=(S\cup\{v\})\setminus D_{i+1}\subseteq X_{i+1}.
\]

### Correctness

Inductively, a state \(S\) at layer \(i\) is reachable exactly when there is an ordering of \(S\) in the first \(i\) positions respecting all intervals, such that every already placed vertex has backward degree at most \(d\) in every completion with the remaining vertices later.

The induction step follows from (4). At layer \(n\), every vertex has been checked, so the reconstructed ordering satisfies \(\Delta(B_\pi)\leq d\).

Conversely, any ordering with \(\Delta(B_\pi)\leq d\) respects (1), and its successive prefixes follow permitted transitions. Thus the dynamic program accepts exactly the desired tournaments.

There are at most \(2^{4d}\) states per layer. Even with naive \(O(n)\) evaluation of (4) and \(O(n)\) candidate choices per state, the running time is
\[
O(2^{4d}n^3).
\]
This proves Theorem 1.

### Corollary 4
The \(\mathcal C\)-FAS problem for graphs of maximum degree at most \(1\) is in \(\mathrm P\).

Take \(d=1\) in Theorem 1 and use Lemma 3. The algorithm also constructs the matching-FAS by recovering the ordering and returning \(B_\pi\).

---

## 5. Exact reformulation of the path case

A linear forest is a disjoint union of paths and isolated vertices.

### Proof of Proposition 2

Suppose \(F\) is a path-FAS, and let \(\pi\) be a topological ordering of \(T-F\). As in Lemma 3,
\[
B_\pi\subseteq F.
\]
Every subgraph of a path is a linear forest, so \(B_\pi\) is acyclic and has maximum degree at most \(2\).

Conversely, suppose \(B_\pi\) is a linear forest. Since the underlying graph of a tournament is complete, one may concatenate all path components of \(B_\pi\), inserting isolated vertices as singleton components, to obtain a Hamiltonian undirected path \(P\) containing every edge of \(B_\pi\). Let \(F\) consist of the tournament arcs corresponding to the edges of \(P\). Then
\[
B_\pi\subseteq F.
\]
Since \(T-B_\pi\) is acyclic, its subdigraph \(T-F\) is also acyclic. Thus \(F\) is a path-FAS. ∎

Therefore the path problem is precisely:

> Does \(T\) have an ordering whose backward graph is an acyclic graph of maximum degree at most \(2\)?

Theorem 1 decides the same question without “acyclic.”

---

## 6. The degree-\(2\) relaxation is genuinely insufficient

Here is an explicit family showing that one cannot simply run the \(d=2\) algorithm and hope to remove cycles afterward.

Let \(T\) have vertices \(1,\ldots,31\). Start with the transitive tournament
\[
i\to j\quad\text{whenever }i<j,
\]
and reverse precisely the four edges
\[
\{1,21\},\quad \{21,11\},\quad \{11,31\},\quad \{31,1\}.
\]
These four edges form the undirected cycle
\[
1-21-11-31-1.
\]

In the natural ordering \(1,\ldots,31\), these are exactly the backward edges. Hence \(T\) has a feedback arc set of maximum degree \(2\).

I claim that \(T\) has no path-FAS. Reversing the four cycle edges changes every vertex's transitive-tournament outdegree by at most \(2\). Consequently its score-center satisfies
\[
|a(v)-v|\leq 2.
\]
If an ordering \(\pi\) had \(\Delta(B_\pi)\leq2\), score localization would give
\[
|\operatorname{pos}_\pi(v)-a(v)|\leq2,
\]
and therefore
\[
|\operatorname{pos}_\pi(v)-v|\leq4.
\]
The endpoints of each reversed cycle edge differ by at least \(10\), so their relative order cannot change under displacements of at most \(4\). Thus all four reversed edges remain backward in every such ordering. Hence every backward graph of maximum degree at most \(2\) contains the displayed \(4\)-cycle and cannot be a linear forest. Proposition 2 now excludes a path-FAS.

---

## 7. A separating example

The path and matching cases are not equivalent. Let \(T_5\) be the cyclic tournament on \(\mathbb Z_5\), where
\[
i\to j \quad\Longleftrightarrow\quad j-i\pmod 5\in\{1,2\}.
\]
Every vertex has outdegree \(2\), so \(a(v)=3\) for all \(v\). If a matching-FAS existed, score localization with \(d=1\) would force all five vertices into positions \(2,3,4\), which is impossible.

On the other hand, in the ordering
\[
(0,1,2,3,4)
\]
the backward edges are
\[
\{0,3\},\ \{0,4\},\ \{1,4\},
\]
which form the path
\[
3-0-4-1
\]
together with the isolated vertex \(2\). Thus the backward graph is a linear forest, and Proposition 2 gives a path-FAS.

---

## 8. A limited polynomial-time subcase for paths

Using the \(d=2\) intervals \(I_v=[\ell(v),r(v)]\), define \(H\) to consist of every edge that is forced backward solely by disjoint intervals. For example, if
\[
r(u)<\ell(v)
\]
and \(T\) contains \(v\to u\), put \(uv\in H\).

Let \(Q\) contain \(H\), together with every pair \(uv\) whose intervals are not strictly separated. Then every interval-respecting ordering satisfies
\[
H\subseteq B_\pi\subseteq Q.
\]

Consequently:

- if \(H\) contains a cycle, there is no path-FAS;
- if \(Q\) is a forest, the \(d=2\) dynamic program decides the path problem exactly, because every accepted \(B_\pi\subseteq Q\) is automatically acyclic.

This covers a polynomially recognizable subclass but not the general case.

---

## 9. Remaining gap

For maximum-degree constraints, histories reaching the same prefix set \(S\) can be merged because the feasibility of placing the next vertex depends only on \(S\), via (4).

For the path case this merging is not sound: two orderings of the same prefix set may produce different connectivity among earlier backward edges. A later backward edge can close a cycle in one history but not the other. Long forced backward edges can create an unbounded number of simultaneously relevant components even though each score interval has constant width. Thus retaining only the constant-size interval frontier does not retain enough information to test acyclicity.

Accordingly, the maximum-degree-\(1\) question is resolved in polynomial time, but the general path case remains open in this writeup.