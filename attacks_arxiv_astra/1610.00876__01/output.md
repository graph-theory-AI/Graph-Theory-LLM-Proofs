```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A replication-and-thinning argument proves the conjecture for a class containing every oriented double star, but does not resolve it for arbitrary oriented trees.",
  "would_publish": false,
  "caveats": "Uses the in-arborescence theorem supplied in the question; novelty of this consequence has not been verified."
}
```

## 1. The partial result

All digraphs below are finite, nonempty, loopless, and have no parallel arcs; opposite arcs are allowed. Subdivisions replace arcs by consistently directed paths with pairwise disjoint interiors.

I use the following established result quoted in the question:

> **Known in-arborescence theorem.** Every in-arborescence is \(\delta^+\)-maderian.

The following extension can be proved from it.

### Theorem
Let \(A\) be an in-arborescence rooted at \(r\), and let
\[
u_1,\ldots,u_k
\]
be its immediate predecessors: the vertices for which \(u_i r\in E(A)\). Construct an oriented tree \(T\) by:

1. attaching \(q_i\ge 0\) new outgoing leaves to each \(u_i\); and
2. identifying \(r\) with the root of an arbitrary out-arborescence \(B\), otherwise disjoint from \(A\) and the new leaves.

Then \(T\) is \(\delta^+\)-maderian.

Thus the extra outgoing leaves may be attached to **all the immediate predecessors of the root**, not merely to one of them. The incoming subtrees below these predecessors can be arbitrary in-arborescences.

In particular:

> **Corollary.** Every orientation of a double star—and hence every oriented tree of diameter at most three—is \(\delta^+\)-maderian.

I do not claim that these consequences are new.

### A bound in terms of known forcing numbers

Define
\[
g(N)=\max\left\{
\mathrm{mader}_{\delta^+}(C):
C\text{ is an in-arborescence with }|C|\le N
\right\}.
\]
The quoted theorem implies that \(g(N)\) is finite.

Put
\[
b=|B|,\qquad Q=\sum_{i=1}^k q_i.
\]
When \(k\ge1\), the proof gives
\[
\mathrm{mader}_{\delta^+}(T)
\le
\max\{g(N),\,2(b+Q)\},
\tag{1}
\]
where
\[
N=
1+(b-1+8k)
\left(1+(Q+1)(|A|-k-1)\right).
\tag{2}
\]
This is an explicit reduction to established in-arborescence forcing numbers, not a claimed sharp numerical bound.

If \(k=0\), then \(A=\{r\}\) and \(T=B\), so the ordinary greedy bound \(b-1\) applies.

## 2. A thinning lemma for disjoint paths

The obstacle is that a branch vertex may have many out-neighbors on other paths of a subdivision. The following lemma lets us retain several paths while controlling this obstruction simultaneously.

### Lemma
Let \(P_1,\ldots,P_m\) be directed paths in a digraph \(D\), with respective initial vertices \(x_1,\ldots,x_m\), sharing a common last vertex \(r\) and otherwise vertex-disjoint. Suppose
\[
|N_D^+(x_i)\cap V(P_i)|\le1
\qquad(1\le i\le m).
\tag{3}
\]
If \(m\ge8k\), there is a set \(J\subseteq\{1,\ldots,m\}\) of size \(k\) such that, for every \(i\in J\),
\[
\left|
N_D^+(x_i)\cap\bigcup_{j\in J}V(P_j)
\right|
\le 1+\frac{d_D^+(x_i)}2.
\tag{4}
\]

#### Proof
Write \(d_i=d_D^+(x_i)\), which is positive since \(P_i\) has positive length. Independently select each index with probability \(1/4\), obtaining a random set \(J_0\).

For a fixed \(i\), define
\[
W_i=
\sum_{\substack{j\in J_0\\j\ne i}}
\left|N_D^+(x_i)\cap\bigl(V(P_j)\setminus\{r\}\bigr)\right|.
\]
Because the sets \(V(P_j)\setminus\{r\}\) are pairwise disjoint,
\[
\mathbb E[W_i\mid i\in J_0]\le \frac{d_i}{4}.
\]
Consequently,
\[
\Pr\left(W_i>\frac{d_i}{2}\,\middle|\,i\in J_0\right)\le\frac12.
\]
Call \(i\) good if \(i\in J_0\) and \(W_i\le d_i/2\). Each index is good with probability at least \(1/8\), so some outcome has at least \(m/8\ge k\) good indices.

Choose any \(k\) of them as \(J\). Deleting other indices cannot increase \(W_i\). Combining its bound with (3), and counting the common vertex \(r\) as part of \(P_i\), proves (4). \(\square\)

## 3. Proof of the theorem

Assume \(k\ge1\).

### 3.1. Constructing a sufficiently redundant in-arborescence

For each \(i\), let \(A_i\) be the component of \(A-r\) containing \(u_i\), rooted at \(u_i\). Thus \(A\) consists of the rooted trees \(A_i\), the root \(r\), and the arcs \(u_i r\).

Form an in-arborescence \(A^\star\) by taking disjoint copies of
\[
A_1,\ldots,A_k
\]
and identifying their roots. It contains each \(A_i\) as a rooted subdigraph, and
\[
|A^\star|-1
=
\sum_{i=1}^k(|A_i|-1)
=
|A|-k-1.
\tag{5}
\]

Set
\[
M=b-1+8k.
\]
Construct an auxiliary in-arborescence \(F\), rooted at \(\rho\), as follows:

* introduce \(M\) vertices \(x_1,\ldots,x_M\), with arcs \(x_j\rho\);
* at each \(x_j\), attach \(Q+1\) copies of \(A^\star\), identifying their roots with \(x_j\).

All these copies are otherwise disjoint. By (5),
\[
|F|
=
1+M\left(1+(Q+1)(|A|-k-1)\right)
=N.
\]

Let \(D\) satisfy
\[
\delta^+(D)\ge \max\{g(N),\,2(b+Q)\}.
\tag{6}
\]
It contains a subdivision \(S\) of \(F\). Choose such a subdivision with the minimum possible number of vertices. Write \(r,x_1,\ldots,x_M\) for the images of the corresponding branch vertices, and let \(P_j\) be the directed path representing \(x_j\rho\).

Minimality gives
\[
|N_D^+(x_j)\cap V(P_j)|=1.
\tag{7}
\]
Indeed, an arc from \(x_j\) to any vertex of \(P_j\) other than its successor would shorten \(P_j\). Its removed vertices are internal vertices of the path representing a single arc of \(F\), so this would still be a subdivision of \(F\).

For each \(j\), call the union of \(P_j-r\) and all the copies of \(A^\star\) attached at \(x_j\) the \(j\)-th **petal**. These petals are pairwise vertex-disjoint.

### 3.2. Embedding the outgoing part at the root

Since \(\delta^+(D)\ge b-1\), greedily embed a copy \(B_0\) of \(B\) rooted at \(r\). This is possible at every prescribed root: order the vertices of the out-arborescence with parents before children, and always choose an unused out-neighbor.

The set
\[
V(B_0)\setminus\{r\}
\]
has \(b-1\) vertices, so it intersects at most \(b-1\) petals. At least
\[
M-(b-1)=8k
\]
petals are therefore disjoint from \(B_0-r\). Call them clean.

Apply the thinning lemma to the paths belonging to clean petals, using (7). Retain \(k\) of them and relabel their initial vertices and paths as
\[
v_1,\ldots,v_k,\qquad R_1,\ldots,R_k.
\]
For each \(i\), writing \(d_i=d_D^+(v_i)\), we have
\[
\left|
N_D^+(v_i)\cap\bigcup_{j=1}^k V(R_j)
\right|
\le 1+\frac{d_i}{2}.
\tag{8}
\]

### 3.3. Choosing all the new outgoing leaves

Let
\[
W=V(B_0)\cup\bigcup_{j=1}^k V(R_j).
\]
Because \(r\) already belongs to the union of the paths, (8) gives
\[
\begin{aligned}
|N_D^+(v_i)\setminus W|
&\ge d_i-\left(1+\frac{d_i}{2}+b-1\right)\\
&=\frac{d_i}{2}-b\\
&\ge Q,
\end{aligned}
\tag{9}
\]
where the last inequality follows from (6).

We can consequently choose pairwise disjoint sets
\[
Z_i\subseteq N_D^+(v_i)\setminus W,
\qquad |Z_i|=q_i.
\tag{10}
\]
For example, choose them successively: each available set initially has at least \(Q\) vertices, and only \(Q\) choices are required in total.

Put
\[
Z=\bigcup_{i=1}^k Z_i,
\qquad |Z|=Q.
\]

### 3.4. Recovering the incoming subtrees

At each selected \(v_i\), the subdivision \(S\) supplies \(Q+1\) rooted subdivisions of \(A^\star\). They share only \(v_i\), and their petal is clean.

The set \(Z\) avoids \(v_i\), by (10), and can intersect at most \(Q\) of these copies. Hence at least one copy avoids \(Z\). It also avoids \(B_0\), since the petal is clean. In that copy, retain a rooted subdivision of \(A_i\), possible because \(A_i\) is a rooted subdigraph of \(A^\star\).

Now take the union of:

* these selected subdivisions of \(A_i\);
* the paths \(R_i\), joining their roots \(v_i\) to \(r\);
* \(B_0\);
* the arcs \(v_i z\) for \(z\in Z_i\).

This is a subdivision of \(T\). The pieces inherited from \(S\) have precisely the required intersections; \(B_0\) avoids the selected petals away from \(r\); and the newly chosen leaves avoid every retained piece.

This proves (1). The argument permits \(Q=0\), singleton \(A_i\), and singleton \(B\). Together with the previously handled case \(k=0\), all cases of the theorem are covered. \(\square\)

## 4. Why this includes every oriented double star

Let the central edge of an oriented double star be directed \(u\to r\).

Take \(A\) to consist of:

* the central arc \(u\to r\);
* all incoming leaf-arcs at \(u\);
* all incoming leaf-arcs at \(r\).

This is an in-arborescence rooted at \(r\). Take \(B\) to be the out-star consisting of \(r\) and its outgoing leaves. The only remaining arcs are the outgoing leaf-arcs at \(u\), and \(u\) is an immediate predecessor of \(r\) in \(A\).

The theorem applies. Degenerate double stars include stars; the one-vertex tree is trivial.

## 5. What remains missing

The proof does **not** permit outgoing leaves to be attached at arbitrary depths of \(A\).

Its crucial feature is the availability of many disjoint, interchangeable petals whose connecting paths meet only at \(r\). Thinning can discard petals responsible for excessive forbidden out-neighborhoods.

For attachments deeper in an in-arborescence, the relevant paths to the root are nested and share compulsory ancestor segments. A vertex may have many out-neighbors on such a segment, but discarding that segment would destroy other required parts of the target. Neither the thinning lemma nor the spare-copy argument above resolves that situation.

Thus this gives a proved special case, including all oriented double stars, but no proof or counterexample for Conjecture 4 in full.