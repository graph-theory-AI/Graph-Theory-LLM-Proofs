```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For fixed k and c, I prove polynomial-time solvability on graphs with no induced cycle longer than c, including chordal bipartite graphs.",
  "would_publish": false,
  "caveats": "The unrestricted k>=3 question remains unresolved here; the novelty of this bounded-chordality special case has not been checked."
}
```

# 1. Partial result

All graphs below are finite, simple, and undirected, and path length means number of edges.

I prove the following special case.

**Theorem 1.** Fix integers \(k\ge 1\) and \(c\ge 3\). On graphs having no induced cycle of length greater than \(c\), one can decide whether there is an induced \(uv\)-path of length at least
\[
d_G(u,v)+k
\]
in time
\[
n^{\,k+\lfloor(c-2)/2\rfloor+O(1)}.
\]
The algorithm also returns such a path when one exists.

In particular, this gives polynomial-time algorithms for every fixed \(k\) on chordal bipartite graphs: their induced cycles all have length at most four.

The proof uses and re-establishes the previous attempt’s first-crossing observation. The new ingredient is that **a large decrease in BFS height along an induced path starting at \(u\) forces a long induced cycle**. This permits a finite-memory search without assuming uniqueness of shortest paths.

The unrestricted question is not settled. Section 5 gives an explicit obstruction to removing the bounded-return hypothesis from this argument.

We may immediately answer no if \(u,v\) are disconnected. If \(u=v\), the only simple \(uv\)-path has length zero, so again the answer is no. Henceforth assume \(u\ne v\), and restrict \(G\) to their component. Put
\[
h(x)=d_G(u,x),\qquad d=h(v).
\]

# 2. Delay and first crossing

For a path
\[
Q=(q_0=u,q_1,\ldots,q_t),
\]
define
\[
\delta_Q(i)=i-h(q_i).
\]
Adjacent vertices have heights differing by at most one, so
\[
\delta_Q(i+1)-\delta_Q(i)
=1+h(q_i)-h(q_{i+1})\in\{0,1,2\}.
\tag{1}
\]
Thus delay is nonnegative and nondecreasing.

Suppose an induced \(uv\)-path \(P\) has length at least \(d+k\). Let \(t\) be its first index with delay at least \(k\). Then
\[
\delta_P(i)<k\quad(i<t),
\qquad
\delta_P(t)\in\{k,k+1\}.
\tag{2}
\]
Call \(P[0,t]\) its **first-crossing prefix**.

Conversely, suppose an induced path \(Q\) from \(u\) to \(x\) has endpoint delay at least \(k\), and it has an induced extension to \(v\). That extension has length at least
\[
|E(Q)|+d_G(x,v)
\ge h(x)+k+d_G(x,v)
\ge d+k.
\tag{3}
\]

The task is therefore to find a first-crossing prefix that has a clean continuation to \(v\). The difficulty in general is that the continuation must avoid neighbors of the entire prefix. Under a bounded-return condition, only a bounded-size tail of the prefix matters.

# 3. Deep returns force long induced cycles

We first establish the structural bound used by the algorithm.

**Lemma 2 — An arch forces a hole.**  
Let
\[
Q=(a=q_0,q_1,\ldots,q_s=b)
\]
be an induced path of length \(s\ge2\), with
\[
h(a)=h(b)=r,\qquad h(q_i)>r\quad(0<i<s).
\]
Then \(G\) contains an induced cycle of length at least \(s+2\).

**Proof.**
The endpoints are distinct, so \(r\ge1\). The ball
\[
B_{r-1}=\{z:h(z)\le r-1\}
\]
is connected, and both \(a\) and \(b\) have neighbors in it. Choose a shortest \(ab\)-path \(R\) in
\[
G[B_{r-1}\cup\{a,b\}].
\]
It is induced. Since \(a,b\) are nonadjacent, \(R\) has length at least two.

Every internal vertex of \(Q\) has height at least \(r+1\), while every internal vertex of \(R\) has height at most \(r-1\). Consequently, there are no edges between the interiors of the two paths. Their interiors are also disjoint. Because both paths are induced, their union is an induced cycle, of length at least \(s+2\). ∎

**Lemma 3 — Bounded return in bounded-chordality graphs.**  
Suppose every induced cycle of \(G\) has length at most \(c\), and set
\[
b=\left\lfloor\frac{c-2}{2}\right\rfloor.
\]
For every induced path
\[
P=(p_0=u,p_1,\ldots,p_m)
\]
and every \(i<j\),
\[
h(p_i)-h(p_j)\le b.
\tag{4}
\]

**Proof.**
Only a positive difference needs consideration. Put
\[
r=h(p_j),\qquad s=h(p_i)-r>0.
\]
Because the path starts at height zero, there is an occurrence of height \(r\) before \(p_i\). Let \(p_a\) be the last such occurrence before \(p_i\), and let \(p_z\) be the first occurrence of height \(r\) after \(p_i\). The latter exists because of \(p_j\).

All internal vertices of \(P[a,z]\) have height greater than \(r\). This subpath reaches height \(r+s\) and returns to height \(r\), so it has length at least \(2s\). Lemma 2 gives an induced cycle of length at least \(2s+2\). Therefore
\[
2s+2\le c,
\]
which proves \(s\le b\). ∎

For example, in a chordal graph \(c=3\), so every induced path starting at \(u\) has nondecreasing \(u\)-distance. When \(c=4\) or \(5\), its height can never decrease by more than one, even over a long subpath.

# 4. A finite-memory algorithm for bounded-return witnesses

The following algorithmic statement applies to arbitrary graphs.

Fix \(b\ge0\). Call a qualifying induced \(uv\)-path **\(b\)-shallow** if, writing \(t\) for its first-crossing index,
\[
h(p_j)\ge h(p_t)-b\qquad(t\le j\le |E(P)|).
\tag{5}
\]

**Theorem 4.** For fixed \(k,b\), the existence of a \(b\)-shallow qualifying induced \(uv\)-path can be decided in time
\[
n^{\,k+b+O(1)}.
\]
The algorithm is exact for this witness condition on arbitrary graphs.

## 4.1. Why bounded memory suffices

Set
\[
M=k+b+3.
\]

Consider a first-crossing prefix
\[
Q=(q_0=u,\ldots,q_t=x).
\]
Its endpoint delay is at most \(k+1\). If a vertex \(q_i\) lies before the last \(M\) vertices of \(Q\), then \(i\le t-M\), and hence
\[
\begin{aligned}
h(q_i)
&=i-\delta_Q(i)\\
&\le t-M\\
&=h(x)+\delta_Q(t)-M\\
&\le h(x)-b-2.
\end{aligned}
\tag{6}
\]
Therefore every forgotten vertex is nonadjacent to every vertex of height at least \(h(x)-b\).

This proves that a continuation satisfying (5) can interact only with the last \(M\) vertices of the prefix.

The same estimate makes it possible to generate the prefixes using bounded memory. Suppose the current prefix ends at time \(t\), has delay below \(k\), and a candidate next vertex \(y\) gives new delay \(\delta'\le k+1\). A forgotten vertex has index \(i\le t-M\), so
\[
h(y)-h(q_i)
=(t+1-i)-(\delta'-\delta_Q(i))
\ge M+1-(k+1)
=b+3.
\tag{7}
\]
Thus \(y\) cannot equal or be adjacent to any forgotten vertex.

## 4.2. States and transitions

A state consists of:

- the current delay \(\delta\);
- an ordered tuple \(\tau\) containing the last at most \(M\) vertices of the prefix.

If \(x\) is the last vertex of \(\tau\), the prefix length is determined by the state:
\[
t=h(x)+\delta.
\tag{8}
\]
Thus no additional length coordinate is needed.

There are two kinds of states:

- **open states:** \(0\le\delta<k\);
- **crossing states:** \(\delta\in\{k,k+1\}\).

Initialize the state \((0,(u))\).

From an open state ending at \(x\), consider each neighbor \(y\) of \(x\). Set
\[
\delta'=\delta+1+h(x)-h(y).
\]
Require that:

1. \(y\) does not occur in \(\tau\);
2. \(y\) is nonadjacent to every vertex of \(\tau\) other than \(x\).

Append \(y\) to \(\tau\), truncating to its last \(M\) vertices if necessary.

A state ending at \(v\) is never expanded. If its delay is below \(k\), discard it. Crossing states are tested as described below and are never expanded.

Every transition increases the determined length \(t\) by one, so states can be processed in increasing \(t\). Lengths exceeding \(n-1\) may be discarded.

Equation (7) shows that checking the retained tuple is sufficient to preserve simplicity and inducedness. It also shows why merging states with the same \((\delta,\tau)\) is legitimate: forgotten vertices cannot affect a later transition before first crossing.

## 4.3. Testing a crossing state

Let a crossing state end at \(x\). Let
\[
A=V(\tau)\setminus\{x\},
\qquad
F_x=\{z:h(z)\ge h(x)-b\}.
\]
For a vertex set \(A\), write \(N_G[A]\) for its closed neighborhood.

Construct
\[
H_x
=
G\left[(F_x\setminus N_G[A])\cup\{x\}\right].
\tag{9}
\]
Accept precisely when \(x\) and \(v\) are connected in \(H_x\). In particular, if \(x=v\), the test succeeds.

The vertex \(x\) is explicitly restored because it is adjacent to its predecessor in the prefix.

## 4.4. Correctness

### Soundness

Every reachable state has an induced prefix realizing it: this follows inductively from the local checks and equation (7). Moreover, \(v\) cannot occur internally in a represented prefix.

Suppose a crossing state accepts, and recover a realizing prefix \(Q\) ending at \(x\). Take a shortest \(xv\)-path \(R\) in \(H_x\).

The path \(R\) is induced. Its vertices other than \(x\) are distinct from and nonadjacent to every vertex of \(A\). By equation (6), they are also distinct from and nonadjacent to every forgotten vertex of \(Q\). Consequently, concatenating \(Q\) and \(R\) gives an induced \(uv\)-path.

Its length is at least \(d+k\) by (3). Its first crossing occurs at \(x\), and all vertices of \(R\) have height at least \(h(x)-b\), so it is \(b\)-shallow.

### Completeness

Let \(P\) be a \(b\)-shallow qualifying induced \(uv\)-path, and let \(Q=P[0,t]\) be its first-crossing prefix.

Following \(Q\) produces legal state transitions: its delay is below \(k\) before \(t\), and lies in \(\{k,k+1\}\) at \(t\). Thus its crossing state is reached.

Write \(x=p_t\). By shallowness, the suffix \(P[t,m]\) lies in \(F_x\). Because \(P\) is induced, every vertex of this suffix other than \(x\) avoids \(N_G[A]\). Hence the suffix lies in \(H_x\), and the connectivity test accepts.

This proves Theorem 4. ∎

## 4.5. Running time and completion of Theorem 1

For \(n\ge2\), the number of states is at most
\[
(k+2)\sum_{r=1}^{M}n^r=O((k+2)n^M).
\]
Each open state has at most \(n\) candidate transitions, with \(O(M)\) work per transition using an adjacency matrix. Each crossing state requires one neighborhood-deletion and connectivity computation, taking \(O(Mn+n^2)\) time.

A conservative bound is therefore
\[
O\!\left((k+2)M\,n^{M+2}\right)
=
O\!\left((k+2)(k+b+3)n^{k+b+5}\right).
\tag{10}
\]

Now assume every induced cycle has length at most \(c\), and choose
\[
b=\left\lfloor\frac{c-2}{2}\right\rfloor.
\]
Lemma 3 says that every qualifying path is \(b\)-shallow. Theorem 4 therefore decides the original threshold question on this graph class, proving Theorem 1.

The graph-class restriction is a promise for this running-time statement. Outside it, the procedure remains sound, but a negative answer need not exclude a deep-return witness.

# 5. Why this does not settle the unrestricted question

The bounded-return hypothesis cannot simply be dropped. The following family exhibits arbitrarily deep necessary returns for \(k\ge3\), even though every vertex lies on a shortest \(uv\)-path.

Fix \(r\ge3\), and put \(D=r+4\). Start with three internally disjoint \(uv\)-paths of length \(D\):
\[
A=(u,a_1,\ldots,a_{D-1},v),
\]
and similarly \(B\) and \(C\). Add exactly two cross-edges:
\[
a_{r+2}b_{r+1},
\qquad
b_2c_3.
\tag{11}
\]

Assign level \(i\) to \(a_i,b_i,c_i\), level zero to \(u\), and level \(D\) to \(v\). Every edge joins consecutive levels. Consequently,
\[
d(u,v)=D,\qquad
h(a_i)=h(b_i)=h(c_i)=i,
\]
and all three original rails are shortest \(uv\)-paths.

A simple \(uv\)-path can use zero, one, or both cross-edges. Its possible excesses over \(D\) are:
\[
\begin{array}{c|c}
\text{Number of cross-edges used}&\text{Possible excesses}\\ \hline
0&0\\
1&0,\ 2\\
2&2,\ 2r
\end{array}
\tag{12}
\]
To see completeness of this list, a path using both cross-edges must start on \(A\) and end on \(C\), or start on \(C\) and end on \(A\); the intervening part of \(B\) is then forced. All other choices use at most one cross-edge.

The long route is
\[
u\,A\,a_{r+2}
-b_{r+1}\,B^{-}\,b_2
-c_3\,C\,v.
\tag{13}
\]
It is induced and has length \(D+2r\). Geodesic induced paths and induced paths of excess two also exist. Thus the set of attainable induced-path excesses is exactly
\[
\{0,2,2r\}.
\tag{14}
\]

Now fix \(k\ge3\), and write
\[
q=\left\lceil\frac{k}{2}\right\rceil.
\]
For sufficiently large \(r\), the only qualifying path is (13). Its first crossing occurs after its \(q\)-th height-decreasing edge, at
\[
b_{r+2-q}.
\]
The suffix subsequently reaches \(b_2\), so its first-crossing return depth is
\[
(r+2-q)-2=r-q.
\tag{15}
\]
This is arbitrarily large.

Therefore:

- no constant return bound depending only on \(k\) can be assumed;
- merely checking excesses in a fixed bounded interval above \(k\) is insufficient, even when every vertex lies on a shortest \(uv\)-path;
- using a general \(k=1\) algorithm as a black box may reveal only an excess-two path and need not expose the long witness.

This family is **not a hardness result**. It identifies the part not handled by the finite-memory argument: qualifying paths whose first-crossing prefix must be followed by an arbitrarily deep return. I do not have a polynomial algorithm or a fixed-\(k\) hardness reduction for that unrestricted case.