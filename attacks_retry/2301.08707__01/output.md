```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I obtain a 12n²/δ rainbow path cover when the minimum degree δ is positive, and a 19n cover for every split graph, but not the unrestricted linear bound.",
  "would_publish": false,
  "caveats": "Finite simple graphs; connector edges may be reused between paths; novelty has not been checked."
}
```

# 1. Statements of the partial results

All graphs below are finite and simple, and all paths are simple. Fix a proper edge-coloring \(\phi\) of \(G\). For \(F\subseteq E(G)\), let
\[
\rho_G(F)
\]
be the minimum number of rainbow paths **in \(G\)** covering \(F\). Such paths may use edges outside \(F\). Write \(\rho(G)=\rho_G(E(G))\).

The main partial results are the following.

### Theorem 1: positive relative minimum degree

Let \(G\) have \(n\) vertices, \(m\) edges, and minimum degree \(\delta>0\). Then
\[
\boxed{\displaystyle
\rho(G)\le
\frac{5n^2}{\delta}+2n+
\left\lceil 2n\log\!\left(\frac{24m}{\delta^2}\right)\right\rceil
\le \frac{12n^2}{\delta}.}
\]

Consequently, for every fixed \(\alpha>0\),
\[
\delta(G)\ge \alpha n
\quad\Longrightarrow\quad
\rho(G)\le \frac{12}{\alpha}n.
\]

This requires neither positive codegree nor connectivity. In particular, at the Dirac boundary,
\[
\delta(G)\ge n/2 \quad\Longrightarrow\quad \rho(G)\le24n.
\]

### Theorem 2: a dense vertex-cover core

Suppose \(X\) is a vertex cover of \(G\), with
\[
|X|=h,\qquad d=\delta(G[X])>0.
\]
Then
\[
\boxed{\displaystyle \rho(G)\le \frac{18nh}{d}.}
\]

Thus a vertex cover inducing a graph of fixed positive relative minimum degree suffices, even if vertices outside the cover have arbitrarily small degrees.

### Corollary 3: split graphs

Every properly edge-colored split graph on \(n\) vertices has a rainbow path cover of size at most
\[
\boxed{19n.}
\]

The unrestricted conjecture is not resolved. The new ingredient is a short-connector merging lemma, followed by an **extraction-and-repair** argument. I independently verify below the extraction and conflict-graph ingredients also appearing in the supplied attempt.

---

# 2. Three elementary tools

Throughout, logarithms are natural.

## 2.1. Rainbow-path extraction

**Lemma 2.1.** A properly edge-colored graph with at most \(n\) vertices and \(M>0\) edges contains a rainbow path of length at least \(M/(2n)\).

**Proof.** Repeatedly delete vertices of current degree less than \(M/n\), keeping this threshold fixed. Not all vertices can be deleted: otherwise, counting each edge when its first endpoint is deleted would give
\[
M< n\frac Mn=M.
\]
The remaining nonempty subgraph \(H\) therefore satisfies
\[
\delta(H)\ge M/n.
\]

In \(H\), greedily extend a rainbow path at one endpoint until this is impossible. Suppose the resulting path has length \(\ell\), with terminal endpoint \(v\). Every edge incident with \(v\) either has its other endpoint on the path or has a color already used by the path. Simplicity bounds the first category by \(\ell\); properness bounds the second by \(\ell\). Hence
\[
M/n\le d_H(v)\le2\ell.
\]
This proves the assertion. \(\square\)

An immediate useful consequence is the following threshold version.

**Extraction consequence.** Starting from \(m>0\) edges, for every real \(\tau>0\), one can remove at most
\[
T_\tau=\left\lceil2n\log^+(m/\tau)\right\rceil
\]
edge-disjoint rainbow paths so that at most \(\tau\) edges remain, where
\(\log^+x=\max\{0,\log x\}\).

Indeed, while edges remain, Lemma 2.1 gives
\[
M_{t+1}\le \left(1-\frac1{2n}\right)M_t,
\]
and therefore \(M_t\le m e^{-t/(2n)}\). If the graph becomes empty earlier, we simply stop.

Taking \(\tau=2n\) and covering the remaining edges individually also verifies the general baseline
\[
\rho(G)\le
2n+\left\lceil2n\log^+\!\left(\frac{m}{2n}\right)\right\rceil
=O(n\log n).
\]

## 2.2. Partitioning into compatible pieces

Call a collection of paths **globally rainbow** if all edges in their union have distinct colors.

**Lemma 2.2.**
1. Every edge set of \(G\) can be partitioned into at most \(5n/2\) rainbow matchings.
2. Every edge-disjoint collection of rainbow paths of length at most two can be partitioned into at most \(4n\) classes, each consisting of vertex-disjoint paths whose union is globally rainbow.

**Proof.**

For the first assertion, construct a conflict graph on the given edges: two edges conflict if they share a vertex or have the same color. If \(\mu\) is the largest color-class size and \(\Delta\) the maximum degree of the given edge set, its maximum conflict degree is at most
\[
2\Delta+\mu-3.
\]
A greedy coloring consequently uses at most
\[
2\Delta+\mu-2\le 2(n-1)+\lfloor n/2\rfloor-2\le 5n/2
\]
classes. These classes are rainbow matchings.

For the second assertion, make the given paths the vertices of a conflict graph, again joining pieces that share a vertex or a color. Because the pieces are edge-disjoint, the number containing any specified vertex \(v\) is at most \(d_G(v)\le n-1\). The number containing any specified color is at most \(\lfloor n/2\rfloor\), since a color class is a matching.

A piece uses at most three vertices and two colors. Its conflict degree is therefore less than \(4n\), so greedy coloring uses at most \(4n\) classes. \(\square\)

## 2.3. Short-connector merging

This is the main additional lemma.

**Lemma 2.3.** Let \(X\subseteq V(G)\), with \(|X|=h\) and
\[
\delta(G[X])\ge d>0.
\]
Let \(L\in\{1,2\}\). Suppose \(\mathcal Q\) consists of \(k\) vertex-disjoint paths such that:

- each path has length at most \(L\);
- both endpoints of each path belong to \(X\);
- all internal vertices of these initial paths lie outside \(X\);
- their union is globally rainbow.

If
\[
k\le \frac{d}{2(L+5)},
\]
then all edges of \(\mathcal Q\) can be covered by at most
\[
\frac{2h}{d}
\]
rainbow paths.

For \(L=1\), the smallness condition is \(k\le d/12\); for \(L=2\), it is \(k\le d/14\).

**Proof.** Start with the paths in \(\mathcal Q\). Maintain a vertex-disjoint, globally rainbow collection of paths, all with endpoints in \(X\).

Whenever possible, merge two current paths using a two-edge connector
\[
xwy,
\]
where \(x,y\) are endpoints of different current paths, \(w\in X\) is outside every current path, and both connector colors are unused by the entire current collection. The two connector colors are distinct because their edges meet at \(w\) and the coloring is proper.

Every merge preserves all the maintained properties. After \(r\) merges, the number of used vertices in \(X\) is at most
\[
2k+r,
\]
and the number of used colors is at most
\[
Lk+2r.
\]
Their sum is at most
\[
(L+2)k+3r\le (L+5)k.
\]

Stop when no such merge is available, and let \(t\) be the number of remaining paths. Choose one endpoint \(x_i\in X\) from each path. Let \(U\) be the used vertices in \(X\), and let \(C\) be the used colors. Define
\[
A_i=\{w\in X\setminus U:\ x_iw\in E(G),\ \phi(x_iw)\notin C\}.
\]
Properness gives
\[
|A_i|
\ge d-|U|-|C|
\ge d-(L+5)k
\ge d/2.
\]

The sets \(A_i\) are pairwise disjoint. Indeed, a vertex in \(A_i\cap A_j\) would supply an admissible two-edge connector between two different current paths.

Consequently,
\[
t\,d/2\le \sum_{i=1}^t|A_i|\le h,
\]
which proves \(t\le2h/d\). Every initial edge has been retained throughout. \(\square\)

A singleton batch can always be kept unchanged, even if its size does not satisfy the displayed smallness condition: \(1\le2h/d\), since \(d\le h-1\).

---

# 3. Proof of Theorem 1

The important distinction is that, after extracting some paths, we repair the remaining edge set using connectors from the **original** graph. Thus the connector graph retains minimum degree \(\delta\).

## 3.1. A repair bound

Fix any \(F\subseteq E(G)\), and put \(M=|F|\). By Lemma 2.2, partition \(F\) into at most \(5n/2\) rainbow matchings.

Set
\[
s=\max\{1,\lfloor\delta/12\rfloor\}.
\]
For every \(\delta>0\),
\[
s\ge\delta/24.
\]
Split each matching into batches of size at most \(s\). The number of batches is at most
\[
\frac{5n}{2}+\frac{M}{s}
\le \frac{5n}{2}+\frac{24M}{\delta}.
\]

Each batch is either a singleton or satisfies Lemma 2.3 with \(X=V(G)\) and \(L=1\). It can therefore be covered by at most \(2n/\delta\) rainbow paths in \(G\). Hence
\[
\boxed{\displaystyle
\rho_G(F)\le
\frac{5n^2}{\delta}
+\frac{48Mn}{\delta^2}.}
\tag{3.1}
\]

Paths belonging to different batches may reuse connector edges; this is permitted for a cover.

## 3.2. Extract first, repair second

Apply the extraction consequence with
\[
\tau=\frac{\delta^2}{24}.
\]
Since \(m\ge n\delta/2\),
\[
\frac{24m}{\delta^2}\ge\frac{12n}{\delta}>1.
\]
Thus at most
\[
T=\left\lceil2n\log\!\left(\frac{24m}{\delta^2}\right)\right\rceil
\]
rainbow paths leave a residual edge set \(F\) of size at most \(\delta^2/24\).

Applying (3.1) to this residual set gives
\[
\rho_G(F)\le \frac{5n^2}{\delta}+2n.
\]
Together with the extracted paths, this proves the first bound in Theorem 1.

For the simpler bound, write \(x=n/\delta\). Using \(m\le n^2/2\), \(\log 12<5/2\), and \(\log x\le x-1\), we obtain
\[
\begin{aligned}
\rho(G)
&\le 5nx+2n+2n\log(12x^2)+1\\
&\le 9nx+3n+1\\
&\le 12nx.
\end{aligned}
\]
The last inequality holds because \(n\ge2\) and \(\delta\le n-1\), which imply \(3n+1\le3n^2/\delta\). Therefore
\[
\rho(G)\le12n^2/\delta.
\]
This proves Theorem 1. \(\square\)

---

# 4. Dense vertex-cover cores

We now prove Theorem 2. Let \(X\) be a vertex cover, with \(|X|=h\) and
\[
d=\delta(G[X])>0.
\]
In particular, \(h\ge2\), and \(V(G)\setminus X\) is independent.

## 4.1. Repairing an arbitrary residual edge set

Fix \(F\subseteq E(G)\), with \(|F|=M\).

For each \(v\notin X\), pair its incident edges of \(F\) arbitrarily. Each pair forms a rainbow two-edge path with endpoints in \(X\) and internal vertex \(v\). At most one edge is left unpaired at each such vertex; cover these unpaired edges individually, using at most \(n-h\) paths.

Regard each edge of \(F\cap E(G[X])\) as a one-edge path. We now have an edge-disjoint collection of at most \(M\) rainbow paths of length one or two, all with endpoints in \(X\), and with internal vertices outside \(X\).

By Lemma 2.2, partition these pieces into at most \(4n\) vertex-disjoint, globally rainbow classes. Set
\[
s=\max\{1,\lfloor d/14\rfloor\}\ge d/28,
\]
and split the classes into batches of size at most \(s\). There are at most
\[
4n+\frac{28M}{d}
\]
batches.

Lemma 2.3 with \(L=2\), together with the singleton observation, covers each batch by at most \(2h/d\) paths. Consequently,
\[
\boxed{\displaystyle
\rho_G(F)\le
n-h+\frac{8nh}{d}+\frac{56Mh}{d^2}.}
\tag{4.1}
\]

## 4.2. Extraction and repair

Choose the threshold
\[
\tau=\frac{nd^2}{28h}.
\]
After at most
\[
T=\left\lceil2n\log^+\!\left(\frac{28mh}{nd^2}\right)\right\rceil
\]
extracted rainbow paths, at most \(\tau\) edges remain. Equation (4.1) covers those remaining edges with at most
\[
3n-h+\frac{8nh}{d}
\]
additional paths.

Put \(x=h/d\). Because \(X\) is a vertex cover, \(m\le hn\), and hence
\[
\log^+\!\left(\frac{28mh}{nd^2}\right)
\le\log(28x^2).
\]
Using \(\log28<7/2\) and \(\log x\le x-1\),
\[
T\le 4nx+3n+1.
\]
It follows that
\[
\begin{aligned}
\rho(G)
&\le 3n-h+8nx+T\\
&\le12nx+6n-h+1\\
&\le18nx,
\end{aligned}
\]
where the last step uses \(h\ge2\) and \(x\ge1\). Thus
\[
\rho(G)\le18nh/d.
\]
This proves Theorem 2. \(\square\)

## 4.3. Split graphs

Suppose \(G\) has a partition into a clique \(X\) and an independent set, and put \(h=|X|\).

If \(h\le18\), then
\[
m\le hn\le18n,
\]
so single-edge paths suffice.

If \(h\ge19\), then \(d=\delta(G[X])=h-1\), and Theorem 2 gives
\[
\rho(G)\le18n\frac{h}{h-1}\le19n.
\]
This covers every case and proves Corollary 3. \(\square\)

---

# 5. What remains unresolved

These arguments establish linear covers in two regimes not requiring the supplied attempt’s positive-codegree hypothesis:

- every graph with minimum degree at least a fixed positive fraction of its order;
- every graph with a vertex cover inducing such a dense core, including all split graphs.

The proofs are constructive: peeling, greedy path extension, greedy conflict-graph coloring, and searching for two-edge connectors all take polynomial time. No longest-path oracle or computational verification is required.

The gap to the original conjecture is still substantial. The factors
\[
n/\delta(G)\qquad\text{and}\qquad h/\delta(G[X])
\]
can be unbounded, and an arbitrary graph need not have a dense vertex-cover core. For unrestricted graphs, the extraction argument above still supplies only an \(O(n\log n)\) bound. Nothing here shows that the logarithmic loss is necessary, and no counterexample to a universal linear bound is produced.

Finally, these are **cover** arguments, not linear-size decomposition arguments: reusing original edges as connectors is essential to retaining the degree conditions during the repair stage. I make no claim that these partial results are new in the literature.