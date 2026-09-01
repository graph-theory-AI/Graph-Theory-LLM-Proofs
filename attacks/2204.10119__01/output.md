```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "An explicit 28-vertex 4-clique amalgam of two apex graphs is K6-minor-free and has degrees only 6, 7, and 8.",
  "would_publish": false,
  "caveats": "This addresses the unrestricted finite-simple-graph statement; the counterexample has a 4-clique separator."
}
```

# Counterexample

We construct a simple connected graph \(G\) on \(28\) vertices with degree sequence
\[
6^{22},7^4,8^2
\]
and no \(K_6\) minor.

## Two elementary lemmas

### Lemma 1: Apex graphs are \(K_6\)-minor-free

If \(Q-z\) is planar for some vertex \(z\), then \(Q\) has no \(K_6\) minor.

#### Proof

Suppose \(B_1,\dots,B_6\) are branch sets of a \(K_6\)-minor model in \(Q\).

If no branch set contains \(z\), the whole model lies in the planar graph \(Q-z\), impossible. Otherwise, say \(z\in B_1\). Then \(B_2,\dots,B_6\) are five pairwise adjacent, vertex-disjoint connected subgraphs of \(Q-z\), giving a \(K_5\) minor in the planar graph \(Q-z\), again impossible. \(\square\)

### Lemma 2: A 4-clique amalgam preserves \(K_6\)-minor-freeness

Let \(Q=Q_1\cup Q_2\), where
\[
S=V(Q_1)\cap V(Q_2)
\]
is a clique of size at most four, and there are no edges between
\(V(Q_1)\setminus S\) and \(V(Q_2)\setminus S\). If both \(Q_1\) and \(Q_2\) are \(K_6\)-minor-free, then so is \(Q\).

#### Proof

Suppose \(B_1,\ldots,B_6\) form a \(K_6\)-minor model in \(Q\). Since the branch sets are disjoint and \(|S|\leq 4\), at least two branch sets avoid \(S\). Every connected branch set avoiding \(S\) lies entirely on one side of the separation. Moreover, all branch sets avoiding \(S\) must lie on the same side, since branch sets in opposite sides would have no edge between them. Assume this side is \(Q_1\).

For every branch set \(B_i\), put
\[
B_i'=B_i\cap V(Q_1).
\]
If \(B_i\) avoids \(S\), then \(B_i'=B_i\). If \(B_i\) meets \(S\), then \(B_i'\) is nonempty and can be made connected using edges of the clique \(S\): all components of \(B_i\cap (V(Q_1)\setminus S)\) attach to \(B_i\cap S\), and \(B_i\cap S\) is a clique.

Pairwise adjacency is preserved. If one branch set avoids \(S\), any edge from it to another branch set lies in \(Q_1\). If both branch sets meet \(S\), their disjoint intersections with the clique \(S\) are adjacent. Thus \(B_1',\dots,B_6'\) give a \(K_6\)-minor model in \(Q_1\), a contradiction. \(\square\)

## Construction of one building block

Let \(I\) be the icosahedral graph with its standard planar triangulation. Choose an edge \(ab\). Its two incident triangular faces are
\[
abc\quad\text{and}\quad abd,
\]
where \(c\neq d\). Let
\[
W=V(I)\setminus\{a,b,c,d\};
\]
thus \(|W|=8\).

For complete combinatorial specificity, one may take the usual model
\[
V(I)=\{N,S\}\cup\{A_i,B_i: i\in\mathbb Z_5\},
\]
with edges, for every \(i\in\mathbb Z_5\),
\[
NA_i,\quad SB_i,\quad A_iA_{i+1},\quad B_iB_{i+1},
\quad A_iB_i,\quad A_{i+1}B_i.
\]
Take
\[
a=A_0,\qquad b=A_1,\qquad c=N,\qquad d=B_0.
\]

Perform the following planar operations.

1. Insert a vertex \(u\) into the face \(abc\), adjacent to \(a,b,c\).
2. Insert a vertex \(v\) into the face \(abd\), adjacent to \(a,b,d\).
3. The edge \(ab\) is now incident with the faces \(abu\) and \(abv\). Flip this edge: delete \(ab\) and add \(uv\).
4. The resulting graph has a facial triangle \(auv\). Insert a vertex \(x\) into this face, adjacent to \(a,u,v\).

Call the resulting planar triangulation \(T\). Then
\[
S_0=\{x,u,v,a\}
\]
induces a \(K_4\).

Finally, add a new vertex \(z\) adjacent precisely to the eight vertices in \(W\). Call the resulting graph \(P\). Since \(P-z=T\) is planar, Lemma 1 shows that \(P\) is \(K_6\)-minor-free.

### Degree calculation in \(P\)

Initially every vertex of \(I\) has degree five.

After the two face insertions and the flip:

- \(u\) and \(v\) have degree \(4\);
- \(a,b,c,d\) have degree \(6\);
- every vertex in \(W\) still has degree \(5\).

Inserting \(x\) into \(auv\) gives
\[
d_T(x)=3,\qquad d_T(u)=d_T(v)=5,\qquad d_T(a)=7.
\]
Joining \(z\) to \(W\) raises every vertex of \(W\) from degree five to degree six and gives \(d_P(z)=8\). Thus:

\[
\begin{array}{c|c|c}
\text{vertices} & \text{number} & \text{degree in }P\\ \hline
W & 8 & 6\\
b,c,d & 3 & 6\\
z & 1 & 8\\
x & 1 & 3\\
u,v & 2 & 5\\
a & 1 & 7
\end{array}
\]

In particular, every vertex outside the distinguished \(K_4=S_0\) has degree six or eight, while the degrees on \(S_0\), in the order \(x,u,v,a\), are
\[
(3,5,5,7).
\]

## Amalgamating two copies

Take two disjoint copies \(P_1,P_2\), with distinguished cliques
\[
S_i=\{x_i,u_i,v_i,a_i\}.
\]
Identify the two \(K_4\)'s according to
\[
x_1=a_2,\qquad
a_1=x_2,\qquad
u_1=u_2,\qquad
v_1=v_2.
\]
Let the resulting simple graph be \(G\).

For a vertex obtained by identifying \(s\in S_1\) with \(t\in S_2\), its degree is
\[
d_G(s=t)=d_{P_1}(s)+d_{P_2}(t)-3,
\]
because the three edges from the vertex to the remainder of the common \(K_4\) were counted in both pieces.

Consequently, the four identified vertices have degrees
\[
3+7-3=7,\qquad
7+3-3=7,\qquad
5+5-3=7,\qquad
5+5-3=7.
\]
Every vertex outside the common \(K_4\) keeps its original degree. Hence \(G\) has:

- \(22\) vertices of degree \(6\);
- \(4\) vertices of degree \(7\);
- \(2\) vertices of degree \(8\).

Thus
\[
|V(G)|=28,\qquad |E(G)|=88,\qquad
\delta(G)=6,\qquad \Delta(G)=8.
\]

Each \(P_i\) is \(K_6\)-minor-free, and \(G\) is their amalgam over a clique of order four. Lemma 2 therefore implies that \(G\) has no \(K_6\) minor.

# Conclusion

The constructed graph \(G\) is a non-null simple connected graph satisfying
\[
6\leq d_G(v)\leq 8\qquad\text{for every }v\in V(G),
\]
but \(G\) has no \(K_6\) minor. Therefore the conjecture, as extracted, is false.

There is no computational component or unresolved case in the argument. The construction does exploit a \(4\)-clique separator, so it does not settle any strengthened version imposing \(5\)-connectivity.