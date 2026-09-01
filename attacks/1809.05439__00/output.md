```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "Under Theorem 5's triangle-free-planar quantifiers, a 23-vertex graph formed from two subdivided 5-wheels gives an explicit counterexample.",
  "would_publish": false,
  "caveats": "The counterexample has 4-cycles, so it does not resolve a stronger variant restricted to girth at least five."
}
```

# Statement attacked

I interpret the informal conjecture using the quantifiers of Theorem 5:

> For every triangle-free planar graph \(G\) and every \(x\in V(G)\), there is a set-coloring
> \[
> \varphi:V(G)\to 2^{[9]}
> \]
> such that adjacent vertices receive disjoint sets, every vertex receives at least three colors, and \(|\varphi(x)|=5\).

This statement is false.

## The tight wheel gadget

Let \(H\) be the graph with vertices
\[
\{x\}\cup\{u_i,v_i:i\in\mathbb Z_5\}
\]
and edges
\[
xu_i,\qquad u_iv_i,\qquad v_iv_{i+1}
\quad (i\in\mathbb Z_5).
\]
Thus \(H\) is obtained from the wheel with rim \(v_0v_1\cdots v_4v_0\) by subdividing every spoke once, with hub \(x\).

We first record the equality case behind the known \(5/9\) upper bound.

### Lemma

Suppose \(H\) has a set-coloring from \([9]\) in which \(|\varphi(x)|=5\) and all other vertices receive at least three colors. Put
\[
P=\varphi(x),\qquad Q=[9]\setminus P,
\]
so \(|P|=5\) and \(|Q|=4\). Then, for every \(i\),

1. \(\varphi(u_i)=Q\setminus\{q_i\}\) for a unique \(q_i\in Q\);
2. \(q_i\in\varphi(v_i)\);
3. \(q_i\ne q_{i+1}\).

Consequently,
\[
\varphi(u_i)\cup\varphi(u_{i+1})=Q.
\]

### Proof

Count color incidences only on
\[
S=\{u_i,v_i:i\in\mathbb Z_5\}.
\]

For a color \(p\in P\), none of the \(u_i\) can receive \(p\), since each \(u_i\) is adjacent to \(x\). Among the \(v_i\), which induce a \(5\)-cycle, at most two can receive \(p\). Thus every \(p\in P\) occurs at most twice on \(S\).

For a color \(q\in Q\), its color class is independent. The five edges \(u_iv_i\) are pairwise vertex-disjoint, so such a color occurs on at most one endpoint of each of these edges, hence at most five times on \(S\).

Therefore
\[
\sum_{w\in S}|\varphi(w)|
 \le 5\cdot2+4\cdot5=30.
\]
On the other hand, \(|S|=10\) and every vertex of \(S\) receives at least three colors, so the same sum is at least \(30\). Equality holds throughout.

In particular, every \(u_i\) receives exactly three colors. Since it is adjacent to \(x\), all these colors lie in \(Q\). Hence
\[
\varphi(u_i)=Q\setminus\{q_i\}
\]
for a unique \(q_i\in Q\).

Moreover, every color of \(Q\) occurs exactly five times on \(S\). The color \(q_i\) is absent from \(u_i\), and an independent color class contains at most one endpoint of every edge \(u_kv_k\). To occur five times, it must therefore occur on exactly one endpoint of every such edge. In particular,
\[
q_i\in\varphi(v_i).
\]
Since \(v_i v_{i+1}\) is an edge, their assigned sets are disjoint, so \(q_i\ne q_{i+1}\). The final assertion follows immediately. \(\square\)

# Counterexample

Take two copies \(H^1,H^2\) of \(H\), identifying only their hubs \(x\). Denote their other vertices by
\[
u_i^j,v_i^j,\qquad i\in\mathbb Z_5,\ j\in\{1,2\}.
\]

For each \(j\), add a vertex \(z_j\) adjacent to \(u_0^j\) and \(u_1^j\). Finally add the edge
\[
z_1z_2.
\]
Call the resulting graph \(G\). It has \(23\) vertices and \(35\) edges.

## Planarity and triangle-freeness

In the standard embedding of \(H^j\),
\[
x\,u_0^j\,v_0^j\,v_1^j\,u_1^j\,x
\]
bounds a face. Place \(z_j\) in this face and join it to \(u_0^j,u_1^j\). The resulting block has an embedding with
\[
x\,u_0^j\,z_j\,u_1^j\,x
\]
on its outer face.

Place the two blocks in disjoint disks meeting only at \(x\), with \(z_1,z_2\) on the common outer face, and draw \(z_1z_2\) in that face. Hence \(G\) is planar.

Each original \(H^j\) is triangle-free. The neighbors of \(z_j\) are \(u_0^j,u_1^j,z_{3-j}\), and no two of these are adjacent. Thus no triangle is introduced. Notice that
\[
x u_0^j z_j u_1^j x
\]
is a \(4\)-cycle, so \(G\) is triangle-free but does not have girth five.

## Nonexistence of the conjectured coloring

Suppose, for contradiction, that \(G\) has the proposed set-coloring. Let
\[
P=\varphi(x),\qquad Q=[9]\setminus P.
\]

Apply the lemma separately to each copy \(H^j\). There are distinct colors
\[
q_0^j,q_1^j\in Q
\]
such that
\[
\varphi(u_0^j)=Q\setminus\{q_0^j\},
\qquad
\varphi(u_1^j)=Q\setminus\{q_1^j\}.
\]
Because \(q_0^j\ne q_1^j\),
\[
\varphi(u_0^j)\cup\varphi(u_1^j)=Q.
\]

The vertex \(z_j\) is adjacent to both \(u_0^j\) and \(u_1^j\), so it cannot receive any color from \(Q\). Therefore
\[
\varphi(z_j)\subseteq P.
\]
Since every vertex receives at least three colors,
\[
|\varphi(z_1)|\ge3,\qquad |\varphi(z_2)|\ge3.
\]
But \(z_1z_2\in E(G)\), so these two subsets of the five-element set \(P\) must be disjoint. This is impossible, since two disjoint subsets of \(P\) cannot both have size at least three.

Thus \(G\) admits no such coloring, disproving the conjecture for triangle-free planar graphs.

# Scope

The construction relies on the \(4\)-cycles
\[
x u_0^j z_j u_1^j x.
\]
Accordingly, it does not disprove the analogous statement restricted to planar graphs of girth at least five. Under the quantifiers of Theorem 5—arbitrary triangle-free planar graphs—the counterexample is complete.