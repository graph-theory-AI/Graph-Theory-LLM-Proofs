```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every hypothetical counterexample has a crossing K4 and at least six degree-five noncrossing vertices, yielding an exact curvature inequality and proving the strengthened degree-at-least-six case.",
  "would_publish": false,
  "caveats": "The sharp degree-five case remains open, and these elementary structural reductions may overlap with the source paper."
}
```

## 1. Statement of the partial result

All graphs below are finite and simple, and a separating triangle means a triangle \(T\) for which \(G-V(T)\) is disconnected.

Let the unique crossing be between the independent edges \(ac\) and \(bd\), with their four ends occurring around the crossing in the order
\[
a,b,c,d.
\]
Put \(A=\{a,b,c,d\}\).

### Theorem
Suppose \(G\) has no separating triangle, is not \(4\)-colorable, and every vertex outside \(A\) has degree at least five. Then:

1. \(G[A]\cong K_4\).
2. \(B:=G-A\) is connected, and every vertex of \(A\) has a neighbor in \(B\).
3. In a suitable plane embedding, \(B\) lies inside the cycle
   \[
   C=abcd,
   \]
   while the crossed edges \(ac,bd\) lie on the other side of \(C\).
4. If
   \[
   k=|V(B)|,\qquad e=|E(B)|,\qquad t=|E(A,B)|,
   \]
   and \(r\) is the length of the outer facial walk of \(B\), then \(r\ge4\) and
   \[
   \sum_{v\in V(B)}(6-d_G(v))\ge 6. \tag{1}
   \]
   More precisely,
   \[
   \sum_{v\in V(B)}(6-d_G(v))
   =r+2+\delta_B+\delta_H, \tag{2}
   \]
   where
   \[
   \delta_B=3k-3-r-e\ge0,\qquad
   \delta_H=3k+1-e-t\ge0.
   \]
5. Consequently, if \(n_5\) denotes the number of degree-five vertices in \(B\), then
   \[
   n_5\ge 6+\sum_{\substack{v\in B\\d_G(v)\ge7}}(d_G(v)-6). \tag{3}
   \]
6. The inherited plane embedding of \(B\) has at least six bounded triangular faces.

In particular, the following strengthening of the conjecture is proved.

### Corollary
If every vertex not incident with the crossed edges has degree at least six, then \(G\) is \(4\)-colorable.

More generally, under the degree-at-least-five hypothesis, \(G\) is \(4\)-colorable whenever
\[
\sum_{v\notin A}d_G(v)>6|V(G)\setminus A|-6.
\]

## 2. The crossing endpoints induce \(K_4\)

Let \(x\) be the artificial vertex obtained by planarizing the crossing. Thus the crossed edges become the paths
\[
a-x-c,\qquad b-x-d.
\]

Suppose, for example, that \(ab\notin E(G)\). In the planarization, contract the two edges \(ax\) and \(xb\). The resulting plane multigraph is precisely the graph obtained from \(G\) by identifying \(a\) and \(b\), up to deletion of parallel edges. There is no loop because \(ab\notin E(G)\).

By the Four Color Theorem, this quotient has a proper \(4\)-coloring. Lifting the coloring back to \(G\) and assigning \(a\) and \(b\) the color of the identified vertex gives a proper coloring of \(G\): the edges \(ac\) and \(bd\) become edges from the identified vertex to \(c\) and \(d\), respectively, so both remain properly colored.

Hence \(ab\) must be present. The same argument applies to
\[
bc,\quad cd,\quad da.
\]
Together with the crossed edges \(ac,bd\), these are all six edges on \(A\), so
\[
G[A]\cong K_4. \tag{4}
\]

This argument does not use the degree or separating-triangle hypotheses.

## 3. Consequences of having no separating triangle

For \(u\in A\), the set \(A\setminus\{u\}\) induces a triangle. Let \(K\) be a component of \(G-A\). If \(K\) had no neighbor at \(u\), then in
\[
G-(A\setminus\{u\})
\]
the component \(K\) would be disconnected from \(u\). Thus \(A\setminus\{u\}\) would be a separating triangle. Therefore every component of \(G-A\) has a neighbor at every vertex of \(A\).

Consider now the planarization of the drawing restricted to the crossing \(K_4\). It is a plane wheel with center \(x\), rim \(abcd\), four triangular faces incident with \(x\), and one face bounded by \(abcd\). A component of \(G-A\) must lie in one face of this wheel. Since it is adjacent to all four vertices of \(A\), it cannot lie in one of the triangular faces, whose only genuine vertices from \(G\) are two consecutive members of \(A\). Hence every component lies in the face bounded by \(abcd\).

There cannot be two such components. Indeed, if \(K_1,K_2\) were distinct, then \(K_1\), being adjacent to \(a,c\), would contain an \(a\)-to-\(c\) arc with interior in \(K_1\). Similarly \(K_2\) would give a \(b\)-to-\(d\) arc. Two disjoint arcs in a disk cannot join alternating boundary pairs \(a,c\) and \(b,d\). Therefore
\[
B=G-A
\]
is connected.

Deleting the crossed edges now gives a plane graph
\[
H:=G-\{ac,bd\}
\]
whose outer face can be chosen to be the \(4\)-cycle \(C=abcd\), with \(B\) in the bounded disk.

## 4. The counting identity

Let
\[
k=|V(B)|,\qquad e=|E(B)|,\qquad t=|E(A,B)|.
\]
Since \(H\) consists of \(B\), the \(t\) attachment edges, and the four edges of \(C\),
\[
|E(H)|=e+t+4.
\]

A simple plane graph with \(k+4\) vertices and an outer face of length four has at most
\[
3(k+4)-7=3k+5
\]
edges. Hence
\[
e+t\le 3k+1. \tag{5}
\]

All edges incident with a vertex of \(B\) either lie in \(B\) or join \(B\) to \(A\). Therefore
\[
\sum_{v\in B}d_G(v)=2e+t. \tag{6}
\]
The degree hypothesis gives
\[
2e+t\ge5k.
\]
Together with (5), this implies
\[
e\ge2k-1. \tag{7}
\]
In particular \(k\ge5\).

All four vertices of \(A\) lie in the same face of the inherited embedding of \(B\). Designate this face as the outer face, and let its facial-walk length be \(r\). Since \(B\) contains a cycle, \(r\ge3\). If \(r=3\), the outer facial walk is a triangle \(T\). Since \(k>3\), some vertex of \(B\) lies on the other side of \(T\) from \(A\), and \(G-V(T)\) is disconnected. This is forbidden. Thus
\[
r\ge4. \tag{8}
\]

Euler's formula, with facial-walk lengths counted with multiplicity, gives
\[
e\le3k-3-r. \tag{9}
\]
Define the two nonnegative deficiencies
\[
\delta_B=3k-3-r-e
\]
and
\[
\delta_H=3k+1-e-t.
\]
Using (6),
\[
\begin{aligned}
\sum_{v\in B}(6-d_G(v))
 &=6k-(2e+t)\\
 &=(3k-3-r-e)+(3k+1-e-t)+(r+2)\\
 &=\delta_B+\delta_H+r+2.
\end{aligned}
\]
By (8), this proves
\[
\sum_{v\in B}(6-d_G(v))\ge6.
\]

Since all degrees in \(B\) are at least five,
\[
\sum_{v\in B}(6-d_G(v))
=n_5-\sum_{\substack{v\in B\\d_G(v)\ge7}}(d_G(v)-6),
\]
which proves (3).

In particular, a hypothetical counterexample has at least six degree-five vertices outside the crossing.

## 5. At least six facial triangles in \(B\)

Let \(q\) be the number of bounded faces of \(B\) whose facial walk has length three. The number of bounded faces is
\[
F=e-k+1.
\]
Every other bounded face has length at least four, so
\[
2e-r\ge 3q+4(F-q)=4F-q.
\]
Consequently
\[
q\ge4F-(2e-r)=2e-4k+4+r.
\]
Using \(e\ge2k-1\),
\[
q\ge r+2\ge6.
\]
Because \(B\) is simple and \(k\ge5\), each such facial walk is a genuine triangle.

This also yields two further solved subclasses: a counterexample cannot have \(B\) triangle-free, and it cannot have \(B\) outerplanar, since an outerplanar \(B\) would satisfy \(e\le2k-3\), contradicting (7).

## 6. Proof of the degree-six corollary

If every vertex of \(B\) had degree at least six, then
\[
\sum_{v\in B}(6-d_G(v))\le0,
\]
contradicting (1). Thus the conjecture is true with “degree at least five” replaced by “degree at least six.”

Equivalently, any non-\(4\)-colorable graph in the stated class satisfies the sharper degree-sum bound
\[
\sum_{v\notin A}d_G(v)\le6|V(G)\setminus A|-6.
\]

## 7. Boundary-coloring formulation and remaining gap

Once \(G[A]=K_4\), a \(4\)-coloring of \(G\) is equivalent to a coloring of the plane graph
\[
H=G-\{ac,bd\}
\]
in which the outer cycle \(abcd\) receives four distinct colors. Indeed, its consecutive vertices are already adjacent in \(H\), and the two deleted diagonals require the two opposite pairs also to receive different colors.

Thus the unresolved sharp case is a rainbow precoloring-extension problem for a plane graph with outer \(4\)-cycle. The identity above shows exactly why elementary Euler counting stops at degree five: a counterexample can pay the unavoidable six units of curvature with six or more degree-five vertices. A proof of the full conjecture needs a coloring or reducibility argument for those degree-five configurations; the present argument supplies no such reduction. I have also not established that these structural lemmas are new relative to the 51-page source paper.