```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove a sharp k=3 special case for line digraphs of Eulerian digraphs, via a stronger constructive strong-decomposition theorem.",
  "would_publish": false,
  "caveats": "The unrestricted conjecture remains unresolved here; novelty of the special-case construction has not been checked."
}
```

# A sharp special case: line digraphs of Eulerian digraphs

I do not obtain a universal constant for arbitrary digraphs. Instead, I take a different route from the supplied blow-up argument and prove the conjecture, sharply with \(k=3\), for **line digraphs of strongly connected Eulerian digraphs**.

The positive result is stronger than a good-pair theorem: it constructs arc-disjoint strongly connected spanning subdigraphs, one of which is a Hamilton cycle. The sharpness example has six vertices and arises from a simple Eulerian digraph.

## 1. Statement

For a loopless digraph \(H\), its **line digraph** \(L(H)\) has vertex set \(A(H)\), with an arc \(ef\) precisely when the head of \(e\) is the tail of \(f\). Thus arcs of \(L(H)\) represent consecutive transitions between arcs of \(H\).

Call \(H\) Eulerian here if
\[
d_H^+(x)=d_H^-(x)
\qquad(x\in V(H)).
\]

### Theorem
Let \(q\ge 1\), and let \(H\) be a finite, loopless, strongly connected Eulerian digraph satisfying
\[
d_H^+(x)=d_H^-(x)\ge 2q-1
\qquad(x\in V(H)).
\]
Then \(L(H)\) contains \(q\) pairwise arc-disjoint strongly connected spanning subdigraphs. Moreover:

- one can be chosen to be a Hamilton cycle;
- each of the other \(q-1\) can be chosen to have in-degree and out-degree exactly \(2\) at every vertex.

The proof also permits parallel arcs in the auxiliary digraph \(H\), although the sharpness example below needs none.

### Corollary
Let \(D=L(H)\), where \(H\) is loopless, strongly connected and Eulerian. If \(D\) is \(3\)-arc-strong, then for every prescribed \(u,v\in V(D)\), it contains an out-branching rooted at \(u\) and an arc-disjoint in-branching rooted at \(v\).

In fact, the out-branching can be chosen to be a Hamilton path starting at \(u\).

The constant \(3\) is best possible for this class, even when \(H\) is simple.

## 2. Proof of the decomposition theorem

Write
\[
d(x)=d_H^+(x)=d_H^-(x).
\]

Because \(H\) is strongly connected and Eulerian, it has a closed directed Euler tour. Read this tour cyclically. Its consecutive arcs give a Hamilton cycle \(C\) in \(L(H)\).

At a fixed vertex \(x\in V(H)\), label the incoming arcs
\[
e_{x,0},e_{x,1},\ldots,e_{x,d(x)-1}.
\]
Label the outgoing arcs
\[
f_{x,0},f_{x,1},\ldots,f_{x,d(x)-1}
\]
so that the Euler tour uses the transition
\[
e_{x,i}f_{x,i}.
\]
This is possible because the Euler tour pairs the incoming and outgoing arcs at \(x\) bijectively.

For \(s\in\mathbb Z_{d(x)}\), let
\[
M_x(s)=
\left\{
e_{x,i}f_{x,i+s}:i\in\mathbb Z_{d(x)}
\right\}.
\]
All these transitions are arcs of \(L(H)\). For fixed \(x\), the sets \(M_x(s)\) are pairwise disjoint, and
\[
A(C)=\bigcup_{x\in V(H)}M_x(0).
\]

For each \(j=1,\ldots,q-1\), define a spanning subdigraph \(F_j\) of \(L(H)\) by
\[
A(F_j)=
\bigcup_{x\in V(H)}
\bigl(M_x(2j-1)\cup M_x(2j)\bigr).
\]

Since \(d(x)\ge 2q-1\), the offsets
\[
0,1,\ldots,2q-2
\]
are distinct modulo \(d(x)\). Also, every transition in \(L(H)\) occurs at a unique vertex of \(H\). Consequently,
\[
C,F_1,\ldots,F_{q-1}
\]
are pairwise arc-disjoint.

It remains to prove that every \(F_j\) is strongly connected.

### 2.1 Every \(F_j\) is balanced

Consider a vertex \(e=xy\) of \(L(H)\), meaning an arc \(xy\) of \(H\).

At \(y\), the arc \(e\) is one of the incoming arcs. Each of the two selected matchings supplies exactly one outgoing transition from \(e\). Therefore
\[
d_{F_j}^+(e)=2.
\]

At \(x\), the arc \(e\) is one of the outgoing arcs. Each selected matching supplies exactly one incoming transition to \(e\). Therefore
\[
d_{F_j}^-(e)=2.
\]

Thus \(F_j\) is balanced at every vertex.

### 2.2 Every \(F_j\) is weakly connected

Fix \(x\), and put \(s=2j-1\). The transitions of \(F_j\) at \(x\) are
\[
e_{x,i}f_{x,i+s},
\qquad
e_{x,i}f_{x,i+s+1}.
\]

Ignoring directions, these transitions connect
\[
e_{x,i}
\;-\;
f_{x,i+s}
\;-\;
e_{x,i-1}.
\]
Hence all the incoming arcs at \(x\), viewed as vertices of \(L(H)\), lie in one weak component of \(F_j\). Every outgoing arc at \(x\) is adjacent to one of them. Thus:

> All arcs of \(H\) incident with \(x\), viewed as vertices of \(F_j\), lie in one weak component.

The underlying undirected graph of \(H\) is connected. The preceding observation therefore propagates along its edges and shows that all vertices of \(F_j\) lie in one weak component.

### 2.3 Balanced and weakly connected implies strong

For completeness, a finite weakly connected digraph in which every vertex has equal in-degree and out-degree is strongly connected.

Indeed, if its condensation had more than one vertex, choose a source strong component \(X\). No arc enters \(X\), and balance gives
\[
|\delta^+(X)|=|\delta^-(X)|=0.
\]
This contradicts weak connectivity.

Applying this to \(F_j\) proves that every \(F_j\) is strongly connected, completing the theorem. \(\square\)

### Deriving the corollary

For an arc \(xy\) of \(H\),
\[
d_{L(H)}^+(xy)=d_H^+(y),
\qquad
d_{L(H)}^-(xy)=d_H^-(x).
\]
Since \(H\) is strongly connected, every vertex occurs as the head and tail of an arc. Thus \(3\)-arc-connectivity of \(L(H)\) implies
\[
d_H^+(x)=d_H^-(x)\ge3
\qquad(x\in V(H)).
\]

Apply the theorem with \(q=2\), obtaining an arc-disjoint Hamilton cycle \(C\) and strong spanning subdigraph \(F_1\).

Delete from \(C\) the arc entering the prescribed \(u\). This leaves a Hamilton out-path rooted at \(u\). Inside \(F_1\), take an in-branching rooted at the prescribed \(v\). For example, choose at each vertex other than \(v\) an arc that decreases its directed distance to \(v\).

The resulting branchings are arc-disjoint. This also covers \(u=v\). \(\square\)

## 3. A six-vertex sharpness example with a simple Eulerian base

Let
\[
H=\overleftrightarrow{K_3}
\]
on vertices \(0,1,2\). Label its six arcs by
\[
a=01,\quad b=12,\quad c=20,\qquad
x=10,\quad y=21,\quad z=02.
\]

Then \(D=L(H)\) has outgoing neighborhoods
\[
\begin{aligned}
N_D^+(a)=N_D^+(y)&=\{b,x\},\\
N_D^+(b)=N_D^+(z)&=\{c,y\},\\
N_D^+(c)=N_D^+(x)&=\{a,z\}.
\end{aligned}
\]
Every vertex has in-degree and out-degree \(2\).

I show that \(D\) is \(2\)-arc-strong but has no good pair with out-root \(a\) and in-root \(c\).

### 3.1 Arc-connectivity is exactly \(2\)

The arcs of \(D\) partition into the Hamilton cycle
\[
C_0=a\,b\,c\,z\,y\,x\,a
\]
and the two vertex-disjoint directed cycles
\[
Q_1=a\,x\,z\,c\,a,
\qquad
Q_2=b\,y\,b.
\]

Let \(X\subset V(D)\) be nonempty and proper. The Hamilton cycle contributes at least one arc to \(\delta_D^+(X)\).

If \(Q_1\cup Q_2\) contributes an outgoing arc, then
\[
|\delta_D^+(X)|\ge2.
\]
Otherwise \(X\) must be the vertex set of \(Q_1\) or the vertex set of \(Q_2\). In either case, \(C_0\) contributes exactly two outgoing arcs.

Hence every nontrivial outgoing cut has size at least \(2\). Since every vertex has out-degree \(2\), the arc-connectivity is exactly \(2\).

### 3.2 No good \((a,c)\)-pair

Suppose that \(T\) is an out-branching rooted at \(a\), and \(S\) is an arc-disjoint in-branching rooted at \(c\).

For every vertex \(w\ne c\), the in-branching \(S\) uses one outgoing arc of \(w\). Since \(d_D^+(w)=2\),
\[
d_T^+(w)\le1\qquad(w\ne c).
\]

At \(c\), the arc \(ca\) cannot belong to \(T\), because \(a\) is its root. Thus
\[
d_T^+(c)\le1
\]
as well.

An out-branching with maximum out-degree at most one is a Hamilton path starting at its root. The Hamilton paths in \(D\) starting at \(a\) are exactly the following three:

\[
\begin{array}{c|c}
\text{Hamilton path }T
&
\text{closed directed cycle in }D-A(T)
\\ \hline
a\,x\,z\,y\,b\,c & a\,b\,y\,x\,a\\
a\,b\,c\,z\,y\,x & b\,y\,b\\
a\,b\,y\,x\,z\,c & a\,x\,a
\end{array}
\]

Here is an exhaustive check of the path list. If the first arc is \(ax\), then \(xz\) is forced; choosing \(zc\) would terminate prematurely, so the remainder is forced as \(zybc\). If the first arc is \(ab\), the next arc is either \(bc\) or \(by\), and each gives the corresponding forced continuation displayed above.

In each row, every vertex of the displayed residual cycle has exactly its cycle arc as its remaining outgoing arc. Its vertex set therefore has no outgoing arc in \(D-A(T)\). None of these closed sets contains \(c\).

Consequently, \(D-A(T)\) cannot contain an in-branching rooted at \(c\), contradicting the existence of \(S\).

Thus \(D\) has no good \((a,c)\)-pair. \(\square\)

This proves both:

- \(3\) is sharp for the line-digraph special case;
- any universal constant in the original prescribed-root conjecture must satisfy \(k\ge3\).

### Why this does not contradict unspecified-root results

The graph does have good pairs with other roots. For instance, the two arc-disjoint Hamilton paths
\[
a\,x\,z\,y\,b\,c
\qquad\text{and}\qquad
z\,c\,a\,b\,y\,x
\]
form an out-branching rooted at \(a\) and an in-branching rooted at \(x\).

Indeed, the underlying graph consists of two triangles joined by a matching, so \(\alpha(D)=2\). This example therefore also illustrates why an unspecified-root existence theorem for independence number two must not be read as a theorem for every prescribed root pair.

## 4. Scope and remaining gap

The positive construction depends on two specific features:

1. an Euler tour of the auxiliary digraph gives a Hamilton cycle of its line digraph;
2. at each auxiliary vertex, **all** transitions from incoming arcs to outgoing arcs are available, allowing the consecutive-shift matchings.

High arc-connectivity of an arbitrary digraph does not itself provide this structure.

Nor can the result be projected from \(L(H)\) back to \(H\): arc-disjoint transitions in a line digraph can involve the same original arc of \(H\). In particular, this does **not** prove the conjecture for arbitrary Eulerian digraphs themselves.

Thus the unrestricted conjecture is not settled here. The established partial result is a self-contained, constructive, sharp \(k=3\) theorem for Eulerian-base line digraphs, with the stronger \(q\)-subdigraph decomposition above.