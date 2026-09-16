```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured girth bound holds sharply for graphs that become bipartite after deleting at most two vertices, even without planarity.",
  "would_publish": false,
  "caveats": "The unrestricted planar conjecture is not resolved; no novelty claim is made for this special case."
}
```

## A sharp two-vertex-transversal case

Write \(\operatorname{og}(G)\) for the odd girth of \(G\), with value \(\infty\) when \(G\) is bipartite. An **odd-cycle transversal** is a vertex set whose deletion leaves a bipartite graph.

The following restricted version admits a complete proof.

**Theorem.** Let \(k\ge 1\), and let \(G\) be a finite simple graph. If
\[
\operatorname{og}(G)\ge 4k+1
\]
and \(G\) has an odd-cycle transversal of size at most two, then
\[
G\longrightarrow C_{2k+1}.
\]

Consequently, the conjecture holds for all planar graphs with an odd-cycle transversal of size at most two. In fact, planarity is unnecessary in this case. The girth threshold \(4k\) is sharp even within this subclass.

### 1. An integer-valued extension lemma

**Lemma.** Let \(B\) be a bipartite graph with bipartition \(X_0,X_1\), and let \(T\subseteq V(B)\). Suppose prescribed integers \(h(t)\), \(t\in T\), satisfy:

1. \(h(t)\equiv i\pmod 2\) whenever \(t\in X_i\);
2. for terminals in the same component,
   \[
   |h(s)-h(t)|\le d_B(s,t).
   \]

Then \(h\) extends to all vertices of \(B\) so that
\[
|h(x)-h(y)|=1
\qquad\text{for every }xy\in E(B).
\]

**Proof.** In a component containing terminals, define
\[
h(v)=\min_{t\in T\text{ in that component}}
       \bigl(h(t)+d_B(t,v)\bigr).
\]
The distance inequalities imply that this agrees with every prescribed value.

For adjacent vertices \(x,y\), the triangle inequality gives
\[
|h(x)-h(y)|\le 1.
\]
Moreover, every quantity in the minimum defining \(h(v)\) has parity \(i\) when \(v\in X_i\). Thus adjacent vertices receive integers of opposite parity, and their difference has absolute value exactly one.

In a component without terminals, assign \(0\) on \(X_0\) and \(1\) on \(X_1\). \(\square\)

We also use the elementary fact that every odd closed walk contains an odd cycle of no greater length.

### 2. Splitting the two exceptional vertices

Set
\[
m=2k+1.
\]
The odd-girth hypothesis becomes
\[
\operatorname{og}(G)\ge 2m-1.
\]

Graphs on at most one vertex are immediate. Otherwise, enlarge the transversal if necessary to two distinct vertices \(a,b\), so that
\[
H=G-\{a,b\}
\]
is bipartite. Fix a bipartition \(V_0,V_1\) of \(H\).

Construct a bipartite graph \(B\) by replacing \(a,b\) with
\[
a^0,a^1,b^0,b^1.
\]
Its two parts are
\[
X_i=V_i\cup\{a^i,b^i\},\qquad i=0,1.
\]
Retain all edges of \(H\). If \(x\in V_i\), replace an edge \(ax\) by \(a^{1-i}x\), and similarly for edges incident with \(b\). If \(ab\in E(G)\), add both
\[
a^0b^1,\qquad a^1b^0.
\]

There is a natural projection \(\pi:B\to G\), identifying the two copies of each exceptional vertex. Every walk in \(B\) projects to a walk of the same length in \(G\).

We will prescribe integer values at the four exceptional copies and apply the lemma. The values will satisfy
\[
h(a^0)\equiv h(a^1)\pmod m,\qquad
h(b^0)\equiv h(b^1)\pmod m.
\]
Reduction modulo \(m\) will therefore descend to a homomorphism \(G\to C_m\), where the vertices of \(C_m\) are \(\mathbb Z_m\) and adjacency means difference \(\pm1\).

First observe that every path from \(a^0\) to \(a^1\) projects to an odd closed walk in \(G\). Hence, whenever the distance is finite,
\[
d_B(a^0,a^1)\ge 2m-1.
\]
Likewise,
\[
d_B(b^0,b^1)\ge 2m-1. \tag{1}
\]

### 3. Choosing the terminal values

There are two cases.

#### Case I: Every odd \(a\)-\(b\) walk has length at least \(m\)

This includes the possibility that no such walk exists. Prescribe
\[
h(a^0)=h(b^0)=0,\qquad
h(a^1)=h(b^1)=m.
\]

These values have the required bipartition parities because \(m\) is odd.

Pairs of terminals in the same part have equal values. For terminals in opposite parts, the prescribed difference is \(m\). Their distance is at least \(m\): for copies of the same original vertex this follows from (1), and for copies of different vertices it follows from the assumption of this case.

Thus all conditions of the extension lemma hold.

#### Case II: There is an odd \(a\)-\(b\) walk of length less than \(m\)

Fix such a walk \(W\), of length \(r\). Since \(r,m\) are odd,
\[
r\le m-2.
\]

Every even \(a\)-\(b\) walk \(Q\), concatenated with the reverse of \(W\), gives an odd closed walk. Therefore
\[
|Q|+r\ge 2m-1,
\]
and consequently
\[
|Q|\ge m+1. \tag{2}
\]

Now prescribe
\[
h(a^0)=0,\qquad h(a^1)=m,\qquad
h(b^0)=m-1,\qquad h(b^1)=-1.
\]
Again, the parities agree with the bipartition. We check all terminal pairs:

- The two copies of either original vertex have value difference \(m\), permitted by (1).
- The pairs \(a^0,b^0\) and \(a^1,b^1\) have value differences \(m-1\) and \(m+1\), respectively. Every path joining either pair projects to an even \(a\)-\(b\) walk, so (2) supplies the required distance bounds.
- The pairs \(a^0,b^1\) and \(a^1,b^0\) have value difference \(1\), which is at most their distance whenever connected.

Thus the extension lemma applies in this case as well.

### 4. Obtaining the homomorphism

In either case, extend \(h\) over \(B\). Every edge of \(B\) has endpoint values differing by exactly one.

The two copies of \(a\) have the same residue modulo \(m\). The same is true for \(b\): in Case II, for example,
\[
m-1\equiv -1\pmod m.
\]
Hence \(h\bmod m\) descends through \(\pi\) to a well-defined map
\[
f:V(G)\to\mathbb Z_m.
\]
Every original edge is represented by an edge of \(B\), so its endpoint residues differ by \(\pm1\). Therefore \(f\) is a homomorphism to \(C_m\). This proves the theorem. \(\square\)

The proof is constructive: once the deletion pair is supplied, the case distinction and the extension can be implemented using shortest-path searches.

## Sharpness within this subclass

The family \(H_k\) supplied in the question already belongs to the subclass just proved.

Let its rim be a cycle of length \(4k-1\), and join a hub \(u\) to each rim vertex by internally disjoint paths of length \(2k-1\).

- It is planar, being a subdivision of a wheel.
- A cycle avoiding \(u\) is the rim. A cycle containing \(u\) consists of two spokes and a nonempty rim arc, so its length is at least
  \[
  2(2k-1)+1=4k-1.
  \]
  Thus its girth and odd girth are both \(4k-1\).
- Deleting \(u\) and any one rim vertex leaves a forest. In particular, its odd-cycle transversal number is at most two.

For completeness, suppose \(H_k\to C_{2k+1}\), and let the hub map to \(c\). No rim vertex can map to \(c\): its spoke would then map to an odd closed walk of length
\[
2k-1<2k+1
\]
in \(C_{2k+1}\), which is impossible. The odd rim would therefore map into
\[
C_{2k+1}-c,
\]
a bipartite graph, another impossibility.

Thus lowering the ordinary-girth threshold from \(4k\) to \(4k-1\) fails even for planar graphs that become forests after deleting two vertices. Equivalently, the theorem’s odd-girth threshold \(4k+1\) cannot be lowered to the preceding odd value \(4k-1\).

## What remains unresolved

This proves a sharp special case, not the full conjecture. In particular, any counterexample to the stated planar conjecture must have odd-cycle transversal number at least three.

Planarity and large girth do not guarantee a two-vertex transversal: arbitrarily many disjoint long odd cycles can be joined by bridges while preserving planarity and girth. The argument above does not handle unrestricted odd-cycle transversals and yields no improvement to the general planar girth bounds quoted in the question. I make no claim that this restricted theorem is new.