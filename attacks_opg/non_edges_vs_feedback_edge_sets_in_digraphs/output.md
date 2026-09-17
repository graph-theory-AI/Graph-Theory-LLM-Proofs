```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "If deleting one vertex makes G acyclic, then the sharp stronger bound gamma(G) >= 2 beta(G) + binom(beta(G),2) holds.",
  "would_publish": false,
  "caveats": "This does not resolve the unrestricted conjecture, and novelty of the special-case estimate is not claimed."
}
```

## 1. A sharp restricted-class result

Write a *feedback vertex* for a vertex belonging to every directed cycle.

**Theorem.** Let \(G\) be a simple digraph with no directed cycles of length at most three. Suppose that \(G-v\) is acyclic for some vertex \(v\). Then
\[
\boxed{\gamma(G)\ \ge\ 2\beta(G)+\binom{\beta(G)}2.}
\tag{1}
\]
This bound is attained for every nonnegative integer value of \(\beta(G)\).

In particular, the conjectured inequality holds in this class. The stronger estimate can also be written as
\[
\beta(G)\le
\left\lfloor\frac{\sqrt{8\gamma(G)+9}-3}{2}\right\rfloor.
\tag{2}
\]

The proof gives an exact refinement when the number of nonneighbors of the feedback vertex is prescribed.

## 2. Proof of the theorem

Put
\[
H=G-v,\qquad
A=N^+(v),\qquad B=N^-(v),\qquad
C=V(G)\setminus(\{v\}\cup A\cup B).
\]
Because digons are forbidden, these sets partition \(V(H)\). Because directed triangles are forbidden,
\[
\text{there is no arc from \(A\) to \(B\).}
\tag{3}
\]

Let \(k=\beta(G)\). The case \(k=0\) is immediate, so assume \(k\ge1\).

### 2.1. A flow representation of the feedback edge number

Construct a network with vertex set \(V(H)\cup\{s,t\}\). Retain every arc of \(H\), replace each arc \(v\to a\) by \(s\to a\), and replace each arc \(b\to v\) by \(b\to t\). Give every arc capacity one.

Every directed cycle of \(G\) contains \(v\), since \(H\) is acyclic. Consequently, under the natural correspondence between arcs of \(G\) and network arcs:

- every directed cycle of \(G\) gives an \(s\)-\(t\) path;
- every \(s\)-\(t\) path gives a directed cycle of \(G\);
- an arc set is a feedback edge set precisely when its corresponding network arcs disconnect \(s\) from \(t\).

Thus the minimum \(s\)-\(t\) cut has size \(k\). By integral max-flow–min-cut, there are \(k\) pairwise arc-disjoint \(s\)-\(t\) paths.

Removing their first and last arcs gives directed paths
\[
P_i:a_i\longrightarrow b_i
\quad (1\le i\le k)
\]
in \(H\), where \(a_i\in A\), \(b_i\in B\). The vertices \(a_1,\ldots,a_k\) are distinct, and so are \(b_1,\ldots,b_k\), because the arcs incident with \(s\) and \(t\) have capacity one.

Every \(P_i\) meets \(C\). Indeed, a path starting in \(A\), ending in \(B\), and avoiding \(C\) must contain an arc from \(A\) to \(B\), contrary to (3).

Choose a vertex
\[
x_i\in V(P_i)\cap C
\]
for each \(i\). For \(x\in C\), let
\[
r_x=|\{i:x_i=x\}|,
\qquad\text{so that}\qquad
\sum_{x\in C}r_x=k.
\tag{4}
\]

### 2.2. Forced nonedges between path endpoints

We count nonedges among the \(k^2\) distinct unordered pairs
\[
\{a_i,b_j\},\qquad 1\le i,j\le k.
\]
They are distinct because the \(a_i\)'s and \(b_j\)'s are separately distinct and \(A\cap B=\varnothing\).

**First, every \(\{a_i,b_i\}\) is a nonedge.**  
The arc \(a_i\to b_i\) is forbidden by (3), while \(b_i\to a_i\), together with \(P_i\), would create a directed cycle in \(H\).

**Second, for \(i\ne j\), at least one of**
\[
\{a_i,b_j\},\qquad \{a_j,b_i\}
\tag{5}
\]
**is a nonedge.**  
If both pairs were adjacent, (3) would force the arcs
\[
b_j\to a_i,\qquad b_i\to a_j.
\]
Together with \(P_i\) and \(P_j\), these arcs give a directed closed walk in \(H\), hence a directed cycle—a contradiction.

**Third, if \(x_i=x_j\), both pairs in (5) are nonedges.**  
The prefix of \(P_i\) ending at \(x_i\), followed by the suffix of \(P_j\) starting there, shows that \(a_i\) reaches \(b_j\) in \(H\). Thus \(b_j\to a_i\) would create a directed cycle in \(H\); the opposite arc is forbidden by (3). Interchanging \(i,j\) proves the other nonedge.

Let \(\gamma(A,B)\) denote the number of nonedges with one endpoint in \(A\) and the other in \(B\). These three observations give
\[
\gamma(A,B)
\ge
k+\binom{k}{2}+\sum_{x\in C}\binom{r_x}{2}.
\tag{6}
\]
Here the first term counts diagonal pairs; the second supplies one nonedge for each pair of distinct paths; and the last supplies the additional nonedge when their chosen vertices coincide.

### 2.3. Completing the count

The \(|C|\) nonedges \(\{v,x\}\), \(x\in C\), are disjoint from those counted in (6). Therefore
\[
\gamma(G)\ge
|C|+k+\binom{k}{2}+\sum_{x\in C}\binom{r_x}{2}.
\tag{7}
\]

For every nonnegative integer \(r\),
\[
1+\binom r2-r=\frac{(r-1)(r-2)}2\ge0.
\]
Using (4), we obtain
\[
|C|+\sum_{x\in C}\binom{r_x}{2}\ge k.
\]
Substitution into (7) proves
\[
\gamma(G)\ge 2k+\binom{k}{2},
\]
as required. \(\square\)

## 3. Sharpness

For \(k\ge1\), take vertices
\[
v,\quad a_1,c_1,b_1,\quad a_2,c_2,b_2,\quad\ldots,\quad a_k,c_k,b_k.
\]

On the vertices other than \(v\), use the displayed linear order. Add every forward arc except
\[
a_i\to b_j\qquad (i\le j),
\]
whose endpoint pairs are left nonadjacent. Finally, add
\[
v\to a_i,\qquad b_i\to v
\]
for every \(i\), and leave every pair \(\{v,c_i\}\) nonadjacent.

The resulting digraph \(G_k\) has the following properties.

- \(G_k-v\) is acyclic, since all its arcs point forward.
- A directed triangle containing \(v\) would require an arc from some \(a_i\) to some \(b_j\); no such arc exists. Hence \(G_k\) satisfies the forbidden-cycle assumptions.
- The only nonedges are the \(k\) pairs \(\{v,c_i\}\) and the \(\binom{k+1}{2}\) pairs \(\{a_i,b_j\}\) with \(i\le j\). Thus
  \[
  \gamma(G_k)=k+\binom{k+1}{2}
  =2k+\binom{k}{2}.
  \]
- The \(k\) directed cycles
  \[
  v\to a_i\to c_i\to b_i\to v
  \]
  are pairwise arc-disjoint, so \(\beta(G_k)\ge k\).
- Deleting the \(k\) arcs \(v\to a_i\) makes the graph acyclic, so \(\beta(G_k)\le k\).

Therefore
\[
\beta(G_k)=k,\qquad
\gamma(G_k)=2k+\binom{k}{2}.
\]
For \(k=0\), a single vertex gives equality.

## 4. Exact refinement with a prescribed number of nonneighbors

The preceding argument determines more than (1). Suppose
\[
c=|C|\ge1,\qquad k=qc+s,\qquad 0\le s<c.
\]
Equation (7) gives
\[
\gamma(G)\ge \binom{k+1}{2}+c+\sum_{x\in C}\binom{r_x}{2}.
\]
Among nonnegative integer \(r_x\) summing to \(k\), the last sum is minimized when their values differ by at most one. Consequently,
\[
\boxed{
\gamma(G)\ge
\binom{k+1}{2}+c
+(c-s)\binom q2+s\binom{q+1}{2}.
}
\tag{8}
\]

This too is sharp for every \(k\ge0\) and \(c\ge1\).

To see this, choose nonnegative integers \(r_1,\ldots,r_c\) summing to \(k\), with \(s\) of them equal to \(q+1\) and the others equal to \(q\). Take vertices \(v,z_1,\ldots,z_c\), together with sets \(A_i,B_i\) of size \(r_i\). Order the vertices other than \(v\) as
\[
A_1,z_1,B_1,\ A_2,z_2,B_2,\ \ldots,\ A_c,z_c,B_c.
\]
Add all forward arcs except those from a vertex in
\(A=\bigcup_i A_i\) to a vertex in \(B=\bigcup_i B_i\). Add all arcs \(v\to A\) and \(B\to v\), and no arcs between \(v\) and the \(z_i\)'s.

The same triangle argument applies. Pairing \(A_i\) bijectively with \(B_i\) produces \(k\) arc-disjoint directed four-cycles through \(v,z_i\); deleting all \(k\) arcs leaving \(v\) destroys every cycle. Hence \(\beta=k\).

The number of nonedges is exactly
\[
c+\sum_{i\le j}r_i r_j
=
c+\frac{k^2+\sum_i r_i^2}{2}
=
\binom{k+1}{2}+c+\sum_i\binom{r_i}{2},
\]
which is the right-hand side of (8).

Thus (8) is an exact extremal bound, not merely an estimate from the proof.

## 5. Consequence for strongly connected components

**Corollary.** The conjecture holds whenever every strongly connected component can be made acyclic by deleting at most one vertex.

Indeed, if the strongly connected components are \(G_1,\ldots,G_m\), then every directed cycle lies in one component, and therefore
\[
\beta(G)=\sum_i\beta(G_i).
\]
Also,
\[
\gamma(G)\ge\sum_i\gamma(G_i).
\]
Applying the theorem componentwise gives the stronger conclusion
\[
\gamma(G)\ge
2\beta(G)+\sum_i\binom{\beta(G_i)}2.
\tag{9}
\]

In particular, any counterexample to the original conjecture must have a strongly connected component in which no single vertex meets every directed cycle.

## 6. Scope and the remaining gap

The basic one-feedback-vertex case is also implied by the two-clique result reported in the supplied context: complete \(G-v\) according to a topological ordering, except never add an arc from \(A\) to \(B\). The resulting triangle-free digraph is the union of the two cliques
\[
A\cup\{v\},\qquad B\cup C.
\]
Thus I do not claim a new class for which the original inequality is known. The quantitative content of this attack is the sharp quadratic strengthening (1) and the exact refinement (8).

Two essential steps do not extend to arbitrary digraphs:

1. Splitting one vertex gives a minimum-cut formulation only because every directed cycle contains that vertex.
2. The endpoint count excludes a reverse arc whenever there is a directed path in \(G-v\). Without acyclicity of \(G-v\), that reverse arc may create a long directed cycle, which is allowed.

Neither obstruction is removed here. The unrestricted Chudnovsky–Seymour–Sullivan inequality is therefore **not proved or disproved by this argument**.