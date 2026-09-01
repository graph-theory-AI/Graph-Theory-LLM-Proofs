```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unrestricted question is not settled, but exact polynomial solvability is proved for chordal graphs and n^(2k+O(1)) solvability when every vertex has a unique shortest path from u.",
  "would_publish": false,
  "caveats": "The general k>=3 case remains; the novelty of the chordal special case has not been checked against the full literature."
}
```

## 1. Statement and scope

Let \(G\) be a finite simple undirected graph, and let \(u\ne v\) be in the same component. Write

\[
\mu_G(u,v)=\max\{|E(P)|:P\text{ is an induced }uv\text{-path}\}.
\]

The question is whether, for each fixed \(k\), one can decide in polynomial time whether

\[
\mu_G(u,v)\ge d_G(u,v)+k.
\]

I do not resolve this for arbitrary graphs. I prove:

1. an exact normal form for a potential witness;
2. an \(n^{2k+O(1)}\)-time algorithm when every vertex has a unique shortest path from \(u\);
3. a polynomial-time algorithm computing \(\mu_G(u,v)\) exactly when \(G\) is chordal, even when \(k\) is part of the input.

---

## 2. A general first-crossing normal form

Put \(h(x)=d_G(u,x)\). For a path

\[
Q=(q_0=u,q_1,\ldots,q_t)
\]

define the delay of its \(i\)-th vertex by

\[
\delta_Q(i)=i-h(q_i).
\]

Since adjacent vertices have \(h\)-values differing by at most one,

\[
\delta_Q(i+1)-\delta_Q(i)
 =1-\bigl(h(q_{i+1})-h(q_i)\bigr)\in\{0,1,2\}.
\]

Thus delay is nondecreasing. An edge directed along \(Q\) contributes

\[
c(q_iq_{i+1})
=
\begin{cases}
0,&h(q_{i+1})=h(q_i)+1,\\
1,&h(q_{i+1})=h(q_i),\\
2,&h(q_{i+1})=h(q_i)-1.
\end{cases}
\]

Call edges of positive contribution nonforward.

For an induced path \(Q\) ending at \(x=q_t\), let

\[
S=V(Q)\setminus\{x\},
\qquad
H(Q)=G\bigl[(V(G)\setminus N_G[S])\cup\{x\}\bigr].
\]

The vertex \(x\) is explicitly restored because it is adjacent to its predecessor in \(Q\).

### Lemma 2.1: clean extension

Suppose \(Q\) is an induced \(u x\)-path and \(v\notin V(Q)\setminus\{x\}\). There is an induced \(uv\)-path beginning with \(Q\) if and only if \(x\) and \(v\) are in the same component of \(H(Q)\).

#### Proof

If an induced \(uv\)-path begins with \(Q\), every later vertex other than \(x\) is distinct from and nonadjacent to every vertex of \(S\). Hence its suffix lies in \(H(Q)\).

Conversely, take a shortest \(xv\)-path \(R\) in \(H(Q)\). It is induced. Every vertex of \(R-\{x\}\) is nonadjacent to every vertex of \(S\), so concatenating \(Q\) and \(R\) creates no cross-chord. Thus the concatenation is an induced \(uv\)-path. ∎

### Proposition 2.2: first-crossing form

There is an induced \(uv\)-path of length at least \(d_G(u,v)+k\) if and only if there is an induced path

\[
Q=(q_0=u,\ldots,q_t=x)
\]

such that:

1. \(v\notin V(Q)\setminus\{x\}\);
2. \(\delta_Q(i)<k\) for every \(i<t\);
3. \(\delta_Q(t)\in\{k,k+1\}\);
4. \(x\) and \(v\) are in the same component of \(H(Q)\).

Moreover, \(Q\) contains at most \(k\) nonforward edges.

#### Proof

Let \(P=(p_0=u,\ldots,p_m=v)\) be qualifying. Then

\[
\delta_P(m)=m-d_G(u,v)\ge k.
\]

Choose the first \(t\) with \(\delta_P(t)\ge k\), and put \(Q=P[p_0,p_t]\). Delay increases by at most two, so

\[
k\le \delta_Q(t)\le k+1.
\]

The original suffix of \(P\) witnesses connectivity in \(H(Q)\).

Conversely, by Lemma 2.1, extend \(Q\) using a shortest \(xv\)-path \(R\) in \(H(Q)\). If \(x=v\), \(Q\) itself has length at least \(d_G(u,v)+k\). Otherwise,

\[
\begin{aligned}
|E(Q)|+|E(R)|
&=h(x)+\delta_Q(t)+|E(R)|\\
&\ge h(x)+k+d_G(x,v)\\
&\ge d_G(u,v)+k.
\end{aligned}
\]

Finally, the first crossing occurs on a nonforward edge. Before the last such edge, the accumulated positive contribution is at most \(k-1\), and every nonforward edge contributes at least one. Hence there are at most \(k\) of them. ∎

This proposition reduces the problem to finding an almost \(h\)-increasing induced path whose closed neighborhood does not separate its endpoint from \(v\). The long increasing pieces are the unresolved difficulty.

---

## 3. Polynomial time when all \(u\)-geodesics are unique

Call the instance \(u\)-geodetic if every vertex in the component of \(u\) has a unique shortest path from \(u\). Equivalently, every \(x\ne u\) has exactly one neighbor \(p(x)\) with

\[
h(p(x))=h(x)-1.
\]

Indeed, such a neighbor always exists, and uniqueness of the predecessor is equivalent by induction to uniqueness of the \(u x\)-geodesic.

### Theorem 3.1

On \(u\)-geodetic instances, the fixed-\(k\) problem can be solved in time

\[
(2|E(G)|)^k n^{O(1)}=n^{2k+O(1)}.
\]

#### Algorithm

List all oriented nonforward edges \(ab\), namely those satisfying \(h(b)\le h(a)\). Give \(ab\) cost

\[
c(ab)=1-(h(b)-h(a))\in\{1,2\}.
\]

For each \(1\le r\le k\), enumerate ordered sequences

\[
e_j=a_jb_j,\qquad j=1,\ldots,r,
\]

of oriented nonforward edges satisfying

\[
\sum_{j<r}c(e_j)<k
\quad\text{and}\quad
\sum_{j\le r}c(e_j)\ge k.
\]

Such a sequence is intended to be the complete list of nonforward edges in a first-crossing prefix.

The intervening forward segments are uniquely determined:

- the segment from \(u\) to \(a_1\) is the unique \(u a_1\)-geodesic;
- for \(1\le j<r\), an \(h\)-increasing path from \(b_j\) to \(a_{j+1}\), if it exists, is found by following parent pointers backward from \(a_{j+1}\) down to level \(h(b_j)\). It exists precisely when this reaches \(b_j\).

Concatenate these segments and the \(e_j\)'s, ending at \(x=b_r\). Reject unless the resulting walk is a simple induced path, contains \(v\) only possibly as \(x\), and has the prescribed first crossing. Finally, construct \(H(Q)\) and test whether \(x\) and \(v\) are connected.

#### Correctness

If the algorithm accepts, Proposition 2.2 supplies a qualifying induced \(uv\)-path.

Conversely, let a qualifying path exist and take its first-crossing prefix \(Q\) from Proposition 2.2. It has at most \(k\) nonforward edges. Between successive nonforward edges, every edge raises the \(h\)-level by one. In a \(u\)-geodetic graph, every such increasing segment is uniquely determined by its endpoints. Therefore, when the algorithm enumerates the ordered list of nonforward edges of \(Q\), it reconstructs \(Q\) exactly and accepts.

There are at most \(2m\) oriented nonforward edges and at most \(k\) are guessed. Each candidate is checked in polynomial time, proving the claimed bound. ∎

The same argument works more generally whenever all relevant \(h\)-increasing paths can be enumerated in polynomially bounded total number.

---

## 4. Exact polynomial algorithm for chordal graphs

The following result does not require \(k\) to be fixed.

### Theorem 4.1

If \(G\) is chordal, then \(\mu_G(u,v)\) can be computed in polynomial time. A direct implementation runs in \(O(n^5)\) time.

The proof uses the standard clique-tree representation of chordal graphs. Let \(T\) be a clique tree whose nodes are the maximal cliques of \(G\). For each graph vertex \(x\), let

\[
A_x=\{K\in V(T):x\in K\}.
\]

Then \(A_x\) is a subtree of \(T\), and for distinct \(x,y\),

\[
xy\in E(G)\quad\Longleftrightarrow\quad A_x\cap A_y\ne\varnothing.
\]

### Lemma 4.2: restriction to a clique-tree path is interval

Let \(R\) be a path in \(T\), and put

\[
X_R=\{x\in V(G):A_x\cap R\ne\varnothing\}.
\]

Then \(G[X_R]\) is an interval graph, represented by the intervals \(A_x\cap R\).

#### Proof

The trace \(A_x\cap R\) is empty or a subpath of \(R\). It remains to show that, for \(x,y\in X_R\),

\[
A_x\cap A_y\ne\varnothing
\quad\Longleftrightarrow\quad
(A_x\cap R)\cap(A_y\cap R)\ne\varnothing.
\]

Only the forward implication needs proof. Choose \(z\in A_x\cap A_y\). If \(z\in R\), there is nothing to prove. Otherwise, the component of \(T-V(R)\) containing \(z\) has a unique attachment \(p\) to \(R\). Since \(A_x\) is connected and contains both \(z\) and a vertex of \(R\), it contains \(p\). The same holds for \(A_y\). Thus \(p\in A_x\cap A_y\cap R\). ∎

### Lemma 4.3: every induced path is captured by one such interval subgraph

Let

\[
P=(p_0,p_1,\ldots,p_s)
\]

be an induced path in \(G\), with \(s\ge2\). There is a path \(R\) in the clique tree \(T\) such that \(p_i\in X_R\) for every \(i\).

#### Proof

Set \(B_i=A_{p_i}\). Consecutive subtrees \(B_i,B_{i+1}\) intersect, while nonconsecutive ones are disjoint because \(P\) is induced.

Choose

\[
a\in B_0\cap B_1,\qquad
b\in B_{s-1}\cap B_s,
\]

and let \(R\) be the unique \(ab\)-path in \(T\).

Fix \(1\le i\le s-1\), and define

\[
L_i=\bigcup_{j<i}B_j,\qquad
U_i=\bigcup_{j>i}B_j.
\]

Both are connected subtrees of \(T\), and they are disjoint because every \(B_j\) in the first union is nonconsecutive to every \(B_h\) in the second. The subtree \(B_i\) meets both \(L_i\) and \(U_i\). Consequently, \(B_i\) contains the unique bridge in \(T\) between \(L_i\) and \(U_i\). Since \(a\in L_i\) and \(b\in U_i\), the path \(R\) also contains this bridge. Hence \(B_i\cap R\ne\varnothing\). The endpoint subtrees contain \(a\) and \(b\), respectively. ∎

It remains to optimize induced paths in an interval graph.

### Lemma 4.4: longest induced path with fixed endpoints in an interval graph

Given an interval representation \(I_x=[\ell_x,r_x]\), a longest induced \(uv\)-path can be found in \(O(n^3)\) time.

#### Proof

Consider an induced path \(x_0,x_1,\ldots,x_t\) with \(t\ge2\). Since \(x_i\) and \(x_{i+2}\) are nonadjacent, their intervals are disjoint. If

\[
r_{x_0}<\ell_{x_2},
\]

then inductively

\[
r_{x_i}<\ell_{x_{i+2}}
\qquad(0\le i\le t-2).
\]

Indeed, suppose \(r_{x_i}<\ell_{x_{i+2}}\). If \(I_{x_{i+3}}\) lay to the left of \(I_{x_{i+1}}\), then consecutive intersections would give

\[
\ell_{x_{i+2}}
\le r_{x_{i+3}}
<\ell_{x_{i+1}}
\le r_{x_i}
<\ell_{x_{i+2}},
\]

a contradiction. Thus the path continues consistently to the right. The alternative is the reflected leftward orientation.

For the rightward orientation, construct a directed graph whose states are ordered adjacent pairs \((a,b)\). Put an arc

\[
(a,b)\longrightarrow(b,c)
\]

when \(bc\in E(G)\) and

\[
r_a<\ell_c.
\]

This state graph is acyclic: because \(I_b\) and \(I_c\) intersect,

\[
r_a<\ell_c\le r_b.
\]

Thus the value \(r\) of the first state coordinate strictly increases along every arc.

Initialize the state \((u,b)\) with value \(1\) for every neighbor \(b\) of \(u\), and perform longest-path dynamic programming in the state DAG. A transition adds one edge. The local inequalities ensure that every generated sequence is induced: when \(c\) is appended, it is disjoint from the vertex two positions back, and the right endpoints of all earlier vertices are smaller still. Conversely, every rightward induced path gives exactly such a state sequence.

Taking the maximum label of a state \((a,v)\) gives the longest rightward induced \(uv\)-path. Reflecting all intervals gives the leftward case. There are \(O(n^2)\) states and \(O(n^3)\) possible transitions. ∎

### Completion of Theorem 4.1

A chordal graph has at most \(n\) maximal cliques. Enumerate every path \(R\) in the clique tree by enumerating its two endpoints. For each of the \(O(n^2)\) choices:

1. form the interval representation \(A_x\cap R\) for all \(x\in X_R\);
2. if \(u,v\in X_R\), apply Lemma 4.4.

Every path found is induced in \(G\), since \(G[X_R]\) is an induced subgraph. Conversely, by Lemma 4.3, every induced \(uv\)-path of length at least two is contained in one of the interval subgraphs considered. Paths of length zero or one are handled separately. Hence the maximum returned is exactly \(\mu_G(u,v)\).

There are \(O(n^2)\) clique-tree paths and the interval routine costs \(O(n^3)\) per path, giving \(O(n^5)\) time. After computing \(d_G(u,v)\) by BFS, one simply compares

\[
\mu_G(u,v)\ge d_G(u,v)+k.
\]

---

## 5. A general brute-force bound and the remaining gap

The clean-extension lemma also gives a fully specified arbitrary-graph algorithm whose exponent depends on \(d_G(u,v)\). Let

\[
L=d_G(u,v)+k.
\]

If \(L>n-1\), the answer is no. Otherwise enumerate every induced path

\[
Q=(u=q_0,\ldots,q_{L-1}=x)
\]

of length \(L-1\), with \(v\notin V(Q)\), and test connectivity of \(x\) and \(v\) in \(H(Q)\). A qualifying path supplies such a prefix, and any successful prefix extends to a path of length at least \(L\). This gives an exact

\[
n^{d_G(u,v)+k+O(1)}
\]

algorithm, polynomial when \(d_G(u,v)\) is bounded, but not for fixed \(k\) alone.

The first-crossing proposition shows precisely what remains in the general case: only \(k\) nonforward edges need be guessed, but the intervening \(h\)-increasing paths can have exponentially many choices. Moreover, whether a choice works depends on the closed neighborhood of every vertex on those long segments through the residual graph \(H(Q)\); the endpoints of the segments do not contain enough information. I do not have a polynomial-size representative family for these choices, nor an NP-hardness construction for fixed \(k\ge3\).