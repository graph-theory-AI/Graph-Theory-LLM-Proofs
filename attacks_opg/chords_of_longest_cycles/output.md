```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A switching argument gives |C| <= floor((3k^2-2k)/4) and k >= 5 for any counterexample, where k counts the components outside C.",
  "would_publish": false,
  "caveats": "The full conjecture is not resolved; the novelty of this self-contained bound has not been checked."
}
```

## Partial result

All graphs below are finite and simple. Write \(c(G)\) for the circumference of \(G\).

**Theorem.** Let \(G\) have minimum degree at least three, and suppose that a longest cycle \(C\) is chordless. Put
\[
c=|V(C)|,\qquad k=\operatorname{comp}(G-V(C)).
\]
Then
\[
\boxed{\quad c\le \binom{k}{2}+\left\lfloor\frac{k^2}{4}\right\rfloor
=\left\lfloor\frac{3k^2-2k}{4}\right\rfloor.\quad} \tag{1}
\]
If \(G\) is 3-connected, then additionally
\[
\boxed{k\ge 5.} \tag{2}
\]

One consequence is a near-Hamiltonian special case:

**Corollary.** If \(G\) has \(n\) vertices, minimum degree at least three, and
\[
c(G)>n-\frac{\sqrt{12n+1}-1}{3},
\tag{3}
\]
then every longest cycle of \(G\) has a chord.

Another consequence is that the conjecture holds for 3-connected graphs with independence number at most four.

The argument below is self-contained. I make no claim that these bounds are new.

## 1. Two elementary cycle switches

Suppose throughout the proof that \(C\) is a chordless longest cycle. Orient \(C\), and denote the successor of \(v\) by \(v^+\).

Let the components of \(G-V(C)\) be \(H_1,\dots,H_k\), and put
\[
A_i=N_G(V(H_i))\cap V(C),\qquad
S(v)=\{i:v\in A_i\}.
\]
Because \(C\) is chordless and \(\delta(G)\ge3\), every vertex of \(C\) has a neighbor outside \(C\). Thus \(S(v)\ne\varnothing\).

Any two distinct vertices of \(A_i\) can be joined by a path whose internal vertices lie in \(H_i\). Such a path has at least two edges.

### First switch: consecutive attachments are forbidden

For every \(v\in V(C)\),
\[
S(v)\cap S(v^+)=\varnothing. \tag{4}
\]
Otherwise, a path through a common component replaces the edge \(vv^+\), producing a longer cycle.

### Second switch: an ordered pair of components occurs at most once

For distinct \(i,j\), there is at most one oriented edge \(vv^+\) of \(C\) satisfying
\[
i\in S(v),\qquad j\in S(v^+). \tag{5}
\]

Indeed, suppose that \(xx^+\) and \(yy^+\) are two such edges. By (4), their four endpoints are distinct. Choose paths
\[
Q_i:x\longrightarrow y,\qquad
Q_j:x^+\longrightarrow y^+
\]
with interiors in \(H_i,H_j\), respectively. These paths are internally disjoint.

Delete \(xx^+\) and \(yy^+\). The remaining two paths of \(C\), together with \(Q_i,Q_j\), form one cycle: traverse \(Q_i\) from \(x\) to \(y\), follow \(C\) backwards to \(x^+\), traverse \(Q_j\) to \(y^+\), and follow \(C\) forwards to \(x\). This cycle contains every vertex of \(C\) and at least two additional vertices, a contradiction.

## 2. The transition digraph

Choose, arbitrarily, one component adjacent to each cycle vertex:
\[
f(v)\in S(v).
\]
Construct a digraph \(D\) on \(\{1,\dots,k\}\) by inserting the arc
\[
f(v)\longrightarrow f(v^+)
\]
for every oriented edge \(vv^+\) of \(C\).

By (4), there are no loops. By the second switch, no arc is repeated. Consequently,
\[
|A(D)|=c. \tag{6}
\]

Let \(B\) be the undirected graph on \(\{1,\dots,k\}\) in which \(ij\) is an edge precisely when **both** \(i\to j\) and \(j\to i\) belong to \(D\).

The key additional restriction is:

**Lemma.** \(B\) is triangle-free.

### A three-edge switching observation

Consider three selected edges of \(C\), whose unordered endpoint-color pairs occur in the circular order
\[
ab,\quad bc,\quad ca.
\]
Call their orientations *forward* when they are, respectively,
\[
a\to b,\quad b\to c,\quad c\to a,
\]
and *backward* otherwise.

If at least two selected edges are backward, a longer cycle can be constructed.

To see this, delete the three selected edges. Between two successive selected edges, the endpoints of the remaining \(C\)-path have the same color exactly when those two selected edges are both forward. With at least two backward edges, this never happens.

Thus each of the three remaining paths has differently colored endpoints. Each of \(a,b,c\) occurs exactly twice among the six endpoints. It follows that, viewed just by endpoint colors, the three remaining paths form a triangle on \(a,b,c\).

Join the two endpoints of each color through its corresponding component \(H_a,H_b,H_c\). The three connecting paths have mutually disjoint interiors and are disjoint from \(C\). Their union with the three remaining \(C\)-paths is one cycle containing all of \(C\) and at least three new vertices.

This also verifies that no degeneracy from adjacent selected edges is possible in this case: a single-vertex remaining path would have equal endpoint colors.

### Proof that \(B\) is triangle-free

Suppose instead that \(a,b,c\) form a triangle in \(B\). The six arcs
\[
p=ab,\quad q=bc,\quad r=ca,\qquad
\bar p=ba,\quad \bar q=cb,\quad \bar r=ac
\]
then correspond to six distinct edges of \(C\), hence to six distinct circular positions.

Select one position from each pair
\[
\{p,\bar p\},\qquad \{q,\bar q\},\qquad \{r,\bar r\}.
\]
The three-edge observation gives the following necessary condition for avoiding a longer cycle:

- if a majority of the selected positions are unbarred, their circular order must be \(p\)-type, \(q\)-type, \(r\)-type;
- if a majority are barred, their circular order must be \(p\)-type, \(r\)-type, \(q\)-type.

For the second assertion, note that in the reversed order of the three unordered color pairs, the barred orientations are the forward ones.

These conditions cannot be realized by six circular positions. Here is an explicit verification.

The all-unbarred choice forces the circular order \(p,q,r\). Write \((x,y)\) for the open oriented circular arc from position \(x\) to position \(y\). The choices with exactly one barred position force
\[
\bar p\in(r,q),\qquad
\bar q\in(p,r),\qquad
\bar r\in(q,p). \tag{7}
\]

The choice \(p,\bar q,\bar r\) has a barred majority, so, starting at \(p\), position \(\bar r\) must occur before \(\bar q\). Combined with (7), this forces the linear order
\[
q,\ \bar r,\ \bar q,\ r
\]
between \(p\) and its next occurrence.

But \(\bar p\in(r,q)\). Therefore the circular order of
\(\bar p,q,\bar r\) is
\[
\bar p,\ q,\ \bar r.
\]
This contradicts its barred majority, which requires the opposite order. The lemma follows.

## 3. Counting the transitions

Let \(b=|E(B)|\). Each unordered pair of components contributes at most one arc to \(D\), plus one additional arc if it is an edge of \(B\). Hence
\[
c=|A(D)|\le \binom{k}{2}+b. \tag{8}
\]

Since \(B\) is triangle-free,
\[
b\le \left\lfloor\frac{k^2}{4}\right\rfloor.
\]
For completeness, this bound follows directly from
\[
d_B(u)+d_B(v)\le k\qquad(uv\in E(B))
\]
and
\[
\frac{4b^2}{k}
\le \sum_v d_B(v)^2
=\sum_{uv\in E(B)}\bigl(d_B(u)+d_B(v)\bigr)
\le kb.
\]
The case \(b=0\) is immediate; otherwise division gives the bound.

Combining this with (8) proves (1).

Notice that 3-connectivity was not used: the argument only required longestness and a neighbor outside \(C\) at every cycle vertex.

## 4. Why 3-connectivity forces at least five components

Now assume \(G\) is 3-connected. Every outside component has at least three attachment vertices:
\[
|A_i|\ge3. \tag{9}
\]
Otherwise deleting at most two attachment vertices separates \(H_i\) from a surviving vertex of \(C\).

For fixed \(i\), consider the sets
\[
S(v^+)\qquad(v\in A_i).
\]
They are nonempty, exclude \(i\), and are pairwise disjoint. Indeed, a common element \(j\) in two of these sets would repeat the ordered pair \(i\to j\), contrary to the second switch. Consequently,
\[
|A_i|\le k-1. \tag{10}
\]
Equations (9)–(10) already exclude \(k\le3\).

Suppose \(k=4\). Then every \(A_i\) has exactly three vertices. For each fixed \(i\), the three nonempty, pairwise disjoint sets \(S(v^+)\), \(v\in A_i\), lie in a three-element set. All three must therefore be singletons.

Every cycle vertex is the successor of a vertex belonging to some \(A_i\). Thus every \(S(v)\) is a singleton, and the four attachment sets partition \(V(C)\). It follows that
\[
c=\sum_{i=1}^4|A_i|=12.
\]
But (1) gives
\[
c\le \binom42+\left\lfloor\frac{4^2}{4}\right\rfloor=10,
\]
a contradiction. This proves \(k\ge5\).

## 5. Consequences

### A circumference threshold

Put \(r=n-c\). Since \(k\le r\), (1) implies
\[
c\le \left\lfloor\frac{3r^2-2r}{4}\right\rfloor,
\]
and therefore
\[
4n\le 3r^2+2r.
\]
Solving for \(r\ge0\) gives the necessary condition
\[
\boxed{\quad
n-|C|\ge
\left\lceil\frac{\sqrt{12n+1}-1}{3}\right\rceil
\quad} \tag{11}
\]
for a chordless longest cycle in a graph of minimum degree at least three. This proves corollary (3).

Asymptotically, the argument rules out a chordless longest cycle whose deficit is less than
\[
\frac{2}{\sqrt3}\sqrt n-\frac13+O(n^{-1/2}).
\]

### Small independence number

If \(G\) were a counterexample with a chordless longest cycle \(C\), (2) would give at least five components of \(G-V(C)\). Choosing one vertex from each gives an independent set of size at least five. Hence:

\[
\boxed{\text{Every 3-connected graph with }\alpha(G)\le4
\text{ satisfies the conjecture.}}
\]

Likewise, every longest cycle whose deletion leaves at most four components has a chord.

## What remains unresolved

The argument excludes counterexamples with few outside components or with circumference sufficiently close to the order. It does **not** eliminate the region
\[
k\ge5,\qquad
c\le\left\lfloor\frac{3k^2-2k}{4}\right\rfloor.
\]
These restrictions are numerically compatible with arbitrarily large parameters—for example, \(c=3k\) is not excluded for any \(k\ge5\).

I have neither constructed a counterexample in that region nor proved that one cannot exist. The full conjecture is therefore not resolved here, and the literature novelty of the partial bounds remains unchecked.