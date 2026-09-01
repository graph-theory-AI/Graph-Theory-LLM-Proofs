```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact minimum remains open, but every failure has s at least 3 and t at least 4 after normalization, and every witness contains a critical core on at least s+t+3 vertices.",
  "would_publish": false,
  "caveats": "The upper bound s+t at most 96 is taken from the supplied 2025 catalog entry and was not independently audited here."
}
```

# Mathematical writeup

## 1. Formalization

By symmetry, assume throughout that
\[
1\le s\le t.
\]
Let \(W(s,t)\) denote the assertion that every graph with no \(K_{s,t}\)-minor is \((s+t-1)\)-choosable, and define
\[
M=\min\{s+t:W(s,t)\text{ fails}\}.
\]
Steiner's construction shows that this set is nonempty. According to the supplied catalog, Vanderbush's construction for \((s,t)=(48,48)\) gives
\[
M\le 96,
\]
although that construction is not reproduced or independently checked here.

I prove the following rigorous lower bounds.

### Proposition
1. \(W(1,t)\) and \(W(2,t)\) hold for every \(t\).
2. \(W(3,3)\) holds.
3. Consequently, every failure satisfies
   \[
   s\ge3,\qquad t\ge4,\qquad s+t\ge7.
   \]
4. If \(G\) witnesses a failure of \(W(s,t)\), then \(G\) contains an induced subgraph \(H\) such that
   \[
   \delta(H)\ge s+t-1
   \quad\text{and}\quad
   |V(H)|\ge s+t+3.
   \]

Thus, accepting the reported \((48,48)\) construction,
\[
7\le M\le96.
\]

The first parameter pair not eliminated here is \((3,4)\).

---

## 2. The cases \(s=1\) and \(s=2\)

### 2.1. The case \(s=1\)

If \(G\) has a vertex of degree at least \(t\), then it contains \(K_{1,t}\) as a subgraph. Hence every \(K_{1,t}\)-minor-free graph satisfies
\[
\Delta(G)\le t-1.
\]
Greedy list coloring therefore shows that \(G\) is \(t\)-choosable, which is exactly the asserted bound
\[
s+t-1=t.
\]

### 2.2. The case \(s=2\)

We use the established edge-density theorem for \(K_{2,t}\)-minors:

> If \(F\) is a nonempty simple graph with no \(K_{2,t}\)-minor, then
> \[
> |E(F)|\le \frac{t+1}{2}\bigl(|V(F)|-1\bigr).
> \]

This is the theorem of Chudnovsky, Reed and Seymour, *The edge-density for \(K_{2,t}\) minors*, J. Combin. Theory Ser. B 101 (2011), 18–46.

Every subgraph \(F\subseteq G\) is also \(K_{2,t}\)-minor-free, and hence
\[
\frac{2|E(F)|}{|V(F)|}
 \le (t+1)\frac{|V(F)|-1}{|V(F)|}
 <t+1.
\]
Thus \(F\) has a vertex of degree at most \(t\). It follows that \(G\) is \(t\)-degenerate and consequently \((t+1)\)-choosable. Since
\[
s+t-1=t+1
\]
when \(s=2\), this proves \(W(2,t)\) for every \(t\).

---

## 3. The case \((s,t)=(3,3)\)

We use two standard results.

1. The Wagner-type structure theorem for \(K_{3,3}\)-minor-free graphs: every such graph is a subgraph of a graph obtained by clique-sums of order at most two from planar graphs and copies of \(K_5\).
2. Thomassen's strengthened planar \(5\)-list-coloring theorem: if an edge on the outer face of a plane graph is properly precolored, all other outer-face vertices have lists of size at least three, and all interior vertices have lists of size at least five, then the precoloring extends.

It remains to check that the pieces can be colored successively across adhesions of size at most two.

### Planar pieces

Let \(P\) be planar and let \(S\) be a precolored clique of order at most two.

- If \(|S|=2\), then \(S\) is an edge. Choose an embedding with that edge on the outer face and apply Thomassen's extension theorem.
- If \(|S|=1\), say \(S=\{x\}\), choose a neighbor \(y\) of \(x\), give \(y\) any color from its five-element list different from the color of \(x\), and apply the precolored-edge theorem. Isolated components are colored separately.
- If \(S=\varnothing\), this is ordinary planar \(5\)-choosability.

Thus every proper precoloring of an adhesion clique of order at most two extends over a planar piece.

### \(K_5\) pieces

Suppose a clique \(S\subseteq K_5\), with \(|S|\le2\), has already been properly colored. Remove the colors used on \(S\) from the lists of the remaining vertices. There are \(5-|S|\) remaining vertices, each with a list of size at least \(5-|S|\). Hall's theorem gives distinct representatives, hence an extension to the entire \(K_5\).

### Gluing

Root the clique-sum decomposition at one piece, color the root, and traverse the decomposition tree. Each new piece meets the already colored part in a clique of order at most two, and the preceding extension arguments apply. Retaining any adhesion edges deleted in the original clique-sum only produces a supergraph, so coloring that supergraph suffices.

Therefore every \(K_{3,3}\)-minor-free graph is \(5\)-choosable. Since
\[
3+3-1=5,
\]
\(W(3,3)\) holds.

It follows that, after assuming \(s\le t\), any counterexample must satisfy
\[
s\ge3,\qquad t\ge4.
\]
In particular,
\[
M\ge7.
\]

---

## 4. A critical-core and order reduction

Let
\[
r=s+t,\qquad k=r-1=s+t-1.
\]
Suppose \(G\) is not \(k\)-choosable. Choose an uncolorable list assignment \(L\) with all lists of size exactly \(k\), and choose an induced subgraph \(H\subseteq G\) minimal subject to not being \(L\)-colorable.

For every \(v\in V(H)\), the graph \(H-v\) is \(L\)-colorable. If
\[
d_H(v)\le k-1,
\]
then after coloring \(H-v\), at most \(k-1\) colors from the \(k\)-element list \(L(v)\) are forbidden, so \(v\) can be colored. This contradiction proves
\[
\delta(H)\ge k=r-1.
\]

I next show that \(H\) cannot have only \(r\), \(r+1\), or \(r+2\) vertices.

### Lemma
Let \(H\) be a graph with
\[
\delta(H)\ge r-1,\qquad |V(H)|=r+q,
\]
where \(0\le q\le2\). Then \(H\) contains \(K_{s,t}\) as a subgraph.

#### Proof

Let \(F=\overline H\). For every vertex,
\[
d_F(v)=|V(H)|-1-d_H(v)
 \le (r+q-1)-(r-1)=q.
\]
Thus \(\Delta(F)\le q\).

We claim that \(F\) has a set \(A\) of \(s\) vertices with
\[
|N_F(A)\setminus A|\le q.
\]

- For \(q=0\), \(F\) is edgeless and any \(s\)-set works.
- For \(q=1\), every component of \(F\) is an isolated vertex or an edge. Take whole components until \(s\) vertices have nearly been selected, and if necessary take one endpoint of one final edge. The external neighborhood has size at most one.
- For \(q=2\), every component is a path or a cycle. Again take whole components until one further component must be used, and take a consecutive segment of that path or cycle of the required size. Only the two endpoints can have neighbors outside the segment.

Since \(n=r+q=s+t+q\),
\[
|V(H)\setminus(A\cup N_F(A))|
 \ge s+t+q-s-q=t.
\]
Choose a \(t\)-set \(B\) in this difference. There are no \(F\)-edges between \(A\) and \(B\), so every possible edge between \(A\) and \(B\) belongs to \(H\). Hence \(H[A\cup B]\) contains \(K_{s,t}\). ∎

Since the critical core \(H\) is still \(K_{s,t}\)-minor-free, the lemma gives
\[
|V(H)|\ge r+3=s+t+3.
\]

For the first remaining pair \((3,4)\), any witness therefore has a critical induced subgraph satisfying
\[
\delta(H)\ge6,\qquad |V(H)|\ge10.
\]

---

## 5. Tight non-counterexamples

The conjectured list bound cannot be reduced even for parameter pairs where it holds. Let
\[
J_{s,t}(m)=K_{s-1}\vee (mK_t),
\]
where \(mK_t\) denotes \(m\) disjoint copies of \(K_t\), and \(\vee\) is the graph join.

Each set consisting of the \(K_{s-1}\) core and one \(K_t\) lobe induces a clique of order
\[
(s-1)+t=s+t-1.
\]
Thus
\[
\chi_\ell(J_{s,t}(m))\ge s+t-1.
\]

On the other hand, every lobe vertex has degree exactly
\[
(s-1)+(t-1)=s+t-2.
\]
Every nonempty subgraph containing a lobe vertex therefore has a vertex of degree at most \(s+t-2\), while a subgraph contained in the core has even smaller minimum degree. Hence \(J_{s,t}(m)\) is \((s+t-2)\)-degenerate and
\[
\chi_\ell(J_{s,t}(m))=s+t-1.
\]

It remains to verify that \(J_{s,t}(m)\) has no \(K_{s,t}\)-minor. Let \(C\) be its core, of order \(s-1\). Suppose there were a \(K_{s,t}\)-model. At most \(s-1\) branch sets meet \(C\). Removing the corresponding vertices from the target \(K_{s,t}\) leaves a connected graph, because
\[
\kappa(K_{s,t})=s.
\]
All remaining branch sets must consequently lie in one lobe, since distinct lobes have no edges between them. Branch sets meeting \(C\) may then be trimmed to their intersections with \(C\), because every core vertex is adjacent to the entire chosen lobe. This would place all \(s+t\) nonempty branch sets inside the \(s+t-1\) vertices consisting of \(C\) and one lobe, an impossibility.

Therefore \(J_{s,t}(m)\) is \(K_{s,t}\)-minor-free and has list chromatic number exactly \(s+t-1\).

For \((s,t)=(3,4)\), these graphs have average degree tending to
\[
t+2s-3=7,
\]
despite being \(5\)-degenerate. Thus a simple global edge bound forcing average degree below \(6\) cannot establish the \((3,4)\) case; a structural or critical-subgraph argument would be needed.

---

## 6. A completely finite bounded-order search

For fixed \((s,t)\) and an order bound \(N\), the following exhaustive computation would be conclusive up to \(N\).

Set \(k=s+t-1\). For each \(n\) with
\[
s+t+3\le n\le N,
\]
enumerate simple graphs \(H\) satisfying \(\delta(H)\ge k\).

1. **Minor test.**  
   Enumerate assignments of each vertex to either “unused” or one of \(s+t\) labeled branch sets. Retain assignments in which every branch set is nonempty and connected and every required pair of opposite branch sets has an edge between them. This exactly tests for a \(K_{s,t}\)-model.

2. **List-coloring test.**  
   It suffices to enumerate assignments of \(k\)-element lists from a palette of \(kn\) colors. Indeed, the union of \(n\) lists of size \(k\) has at most \(kn\) colors, which may be renamed. For each assignment, test whether a proper list coloring exists.

This is far too large as a naive computation, but it is a fully finite certification procedure and the critical-core reduction removes all graphs of order at most \(s+t+2\). I have not run this computation. Moreover, without an a priori upper bound on the order of a witness, failure to find one up to \(N\) would not settle \(W(s,t)\).

---

## 7. Remaining gap

The exact smallest pair is not determined. The present argument leaves \((3,4)\) as the first possible pair and, taking the supplied 2025 construction as correct, gives only
\[
7\le M\le96.
\]

The lower bound uses known results for \(K_{2,t}\)-minor density, the Wagner decomposition, and planar \(5\)-choosability; the new elementary component here is mainly the \(s+t+3\) critical-core order reduction and the explicit formulation of the bounded-order search. This is not enough for a publishable resolution.