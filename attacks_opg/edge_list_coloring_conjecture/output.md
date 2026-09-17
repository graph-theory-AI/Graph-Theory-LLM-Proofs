```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture for graphs made bipartite by deleting one parallel class, and for multigraphs whose blocks are bipartite or multicycles.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved, and no novelty is claimed for these special cases."
}
```

## 1. Precise partial result

All graphs below are finite and loopless; parallel edges are allowed. Write \(\chi'_\ell(G)\) for the list chromatic index.

A **multicycle** is obtained from a simple cycle by replacing each edge with a nonempty parallel class. For block terminology, take the blocks of the underlying simple graph and restore all parallel edges; bridge blocks are included.

**Theorem.** The equality
\[
\chi'_\ell(G)=\chi'(G)
\]
holds in each of the following cases:

1. There are distinct vertices \(u,v\) such that deleting the entire parallel class \(E_G(u,v)\) makes \(G\) bipartite.
2. Every block of \(G\) is either bipartite or a multicycle.

The second case includes all multigraphs whose underlying simple graph is a cactus, with arbitrary edge multiplicities and arbitrarily many odd cycles.

The proof uses the stable-matching/kernel method underlying the bipartite case. The additional ingredient is a rooted list-coloring extension lemma: it makes the block argument valid despite the fact that list colorings cannot generally be glued by permuting their colors.

## 2. Two kernel lemmas

We allow a digraph to have both arcs \(xy\) and \(yx\), but no repeated arcs or loops. Its outdegree counts distinct outneighbors.

A **kernel** of a digraph \(D\) is an independent set \(K\) such that every vertex outside \(K\) has an arc directed to a vertex of \(K\). The digraph is **kernel-perfect** if every induced subdigraph has a kernel.

### Lemma 1: Kernel list-coloring lemma

Let \(D\) be a kernel-perfect digraph whose underlying undirected graph is \(J\). If
\[
|L(x)|\ge d_D^+(x)+1
\qquad(x\in V(J)),
\]
then \(J\) has an \(L\)-coloring.

**Proof.** Induct on \(|V(J)|\). Choose a color \(a\) appearing in a list, and put
\[
S=\{x:a\in L(x)\}.
\]
Take a kernel \(K\) of \(D[S]\), and color every vertex of \(K\) with \(a\). This is proper because \(K\) is independent.

Delete \(K\), and delete \(a\) from the remaining lists. If \(x\in S\setminus K\), its list loses one color, but it has an outgoing arc to \(K\), so its outdegree also decreases by at least one. Other lists do not shrink. Thus every remaining list still has size at least the new outdegree plus one.

The remaining induced digraph is kernel-perfect, so induction completes the coloring. \(\square\)

### Lemma 2: Bipartite preference digraphs

Let \(H\) be a bipartite multigraph with bipartition \(X,Y\). At each vertex, place its incident edges in a strict preference order. Form a digraph on \(E(H)\) by adding
\[
e\longrightarrow f
\]
whenever \(e,f\) share an endpoint that prefers \(f\) to \(e\). Retain both arcs when the endpoints give opposite preferences.

This digraph is kernel-perfect.

**Proof.** First find a kernel of the whole digraph.

Run the following proposal procedure. An unmatched vertex of \(X\) proposes along its incident edges in preference order. Each vertex of \(Y\) keeps its most preferred proposal so far and rejects the others. Stop when no unmatched vertex of \(X\) has an untried edge. The procedure terminates because each edge is proposed at most once. The retained edges form a matching \(M\).

Consider \(e=xy\notin M\). If \(x\) never proposed along \(e\), then it finishes matched along an edge it prefers to \(e\). Otherwise \(e\) was eventually rejected, and \(y\) finishes matched along an edge it prefers to \(e\). In either case, \(e\) has an arc to an edge of \(M\). Thus \(M\) is a kernel.

The same argument applies after restricting to any subset of edges. Proposals are along individual edges, so parallel edges cause no difficulty. \(\square\)

## 3. A rooted extension lemma

Here is the main useful strengthening.

**Lemma 3.** Let \(F\) be a loopless multigraph, let \(r\in V(F)\), and let \(k,t\) be nonnegative integers satisfying
\[
k\ge \chi'(F),
\qquad
k\ge d_F(r)+t.
\]
Assume either:

- \(F\) is bipartite; or
- there is a nonempty parallel class \(B=E_F(r,s)\) such that \(F-B\) has a bipartition \(X,Y\) with \(r,s\in X\).

Let every edge of \(F\) have a list of at least \(k\) colors, and let \(C\) be any set of \(t\) forbidden colors. Then \(F\) has a proper list edge-coloring in which no edge incident with \(r\) receives a color in \(C\).

The edgeless case is immediate, so assume \(F\) has an edge.

### Auxiliary ordinary coloring

In the bipartite case, put \(B=\varnothing\), set \(q=0\), and choose a bipartition \(X,Y\) with \(r\in X\). Otherwise put \(q=|B|\), using the bipartition in the hypothesis.

Temporarily add \(t\) parallel edges from \(r\) to a new vertex \(z\); call this dummy class \(Q\). There is a proper \(k\)-edge-coloring of \(F+Q\): start with one of \(F\), and assign the dummy edges distinct colors unused at \(r\). This is possible because
\[
k-d_F(r)\ge t.
\]

The edges in \(B\cup Q\) all meet \(r\), so their colors are distinct. Relabel the \(k\) colors so that
\[
c(B)=\{1,\ldots,q\},
\qquad
c(Q)=\{q+1,\ldots,q+t\}.
\]
The numerical coloring \(c\) is only auxiliary; its labels need not belong to the given lists.

### The digraph

Construct a digraph \(D\) on \(E(F)\):

- at a vertex of \(X\), direct an arc from the edge with larger numerical color to the one with smaller numerical color;
- at a vertex of \(Y\), direct an arc from the edge with smaller numerical color to the one with larger numerical color.

Coalesce repeated arcs, but retain opposite arcs. The underlying undirected graph is the line graph of \(F\).

We claim that
\[
d_D^+(e)\le
\begin{cases}
k-t-1,& e\text{ is incident with }r,\\
k-1,& e\text{ is not incident with }r.
\end{cases}
\tag{1}
\]

For a crossing edge \(e=xy\in E(F)\setminus B\), where \(x\in X\), \(y\in Y\), and \(c(e)=j\), its outgoing neighbors arise from lower-colored edges at \(x\) and higher-colored edges at \(y\). Hence
\[
d_D^+(e)\le (j-1)+(k-j)=k-1.
\]

If \(x=r\), then \(j>q+t\). All \(t\) dummy colors are smaller than \(j\), and none occurs on an edge of \(F\) incident with \(r\). Consequently,
\[
d_D^+(e)\le (j-1-t)+(k-j)=k-t-1.
\]

Finally, suppose \(e\in B\) and \(c(e)=i\). Every crossing edge incident with either endpoint of \(B\) has color greater than \(q\), since all colors \(1,\ldots,q\) already occur there on \(B\). Both endpoints lie in \(X\). Thus \(e\)'s outgoing neighbors are exactly the \(i-1\) lower-colored edges of \(B\). Therefore
\[
d_D^+(e)=i-1\le q-1\le k-t-1,
\]
where the last inequality follows from \(q+t\le d_F(r)+t\le k\). This proves (1).

### Kernel-perfection

Take any \(S\subseteq E(F)\).

If \(S\cap B=\varnothing\), then \(D[S]\) is a bipartite preference digraph and has a kernel by Lemma 2.

Otherwise, let \(e\) be the lowest-colored edge in \(S\cap B\). Every neighbor of \(e\) in \(D[S]\) has an arc directed to \(e\):

- other selected edges of \(B\) have larger colors;
- crossing edges at its endpoints have colors greater than \(q\).

Thus \(e\) is a sink. Moreover, it is adjacent to every other edge of \(B\).

Delete \(e\) and all its neighbors from \(S\), leaving \(T\). Then \(T\cap B=\varnothing\), so \(D[T]\) has a kernel \(K\) by Lemma 2. Now
\[
K\cup\{e\}
\]
is a kernel of \(D[S]\): deleted neighbors point to \(e\), and vertices in \(T\setminus K\) point to \(K\).

Therefore \(D\) is kernel-perfect.

### Applying the lists

Define
\[
L^*(e)=
\begin{cases}
L(e)\setminus C,& e\text{ is incident with }r,\\
L(e),&\text{otherwise}.
\end{cases}
\]
By (1),
\[
|L^*(e)|\ge d_D^+(e)+1
\]
for every edge. Lemma 1 gives the desired coloring. \(\square\)

## 4. Proof of the two special cases

The inequality
\[
\chi'(G)\le \chi'_\ell(G)
\]
always holds, by assigning the same palette to every edge. It therefore suffices to prove the reverse inequality.

Put \(k=\chi'(G)\), and consider an arbitrary assignment of lists of size at least \(k\). The edgeless case is trivial.

### Case 1: One parallel-class deletion makes \(G\) bipartite

Let
\[
B=E_G(u,v),\qquad H=G-B,
\]
where \(H\) is bipartite. Choose a bipartition of \(H\).

If \(u,v\) lie in opposite parts, then \(G\) itself is bipartite, so apply the bipartite case of Lemma 3 with \(t=0\).

If they lie in the same part, name that part \(X\) and apply the second case of Lemma 3 with
\[
F=G,\qquad r=u,\qquad t=0.
\]
Its degree condition holds because \(k\ge\Delta(G)\).

Thus every \(k\)-list assignment is colorable.

### Case 2: Bipartite and multicycle blocks

First observe that every allowed block \(F\) satisfies a hypothesis of Lemma 3 for **every** choice of root \(r\in V(F)\).

- If \(F\) is bipartite, use the first hypothesis.
- If \(F\) is an odd multicycle, choose either parallel class \(B\) incident with \(r\). Deleting \(B\) leaves a multipath whose underlying path has even length. Its two endpoints therefore lie in the same part of a bipartition, as required by the second hypothesis.
- Even multicycles are already bipartite.

Root the block-cutvertex tree of each nontrivial connected component, and process its blocks away from the root.

For the first block, apply Lemma 3 with \(t=0\). Now suppose a new block \(F\) meets the previously processed blocks at its parent cutvertex \(r\). No other vertex of \(F\) is incident with a previously colored edge.

Let \(C\) be the colors already used at \(r\), and put \(t=|C|\). Those colors are distinct because the coloring constructed so far is proper. Also,
\[
d_F(r)+t\le d_G(r)\le k,
\qquad
\chi'(F)\le \chi'(G)=k.
\]
Lemma 3 colors \(F\) from its original lists while avoiding \(C\) at \(r\). Hence this extends the existing proper coloring.

Continuing through the block-cutvertex trees colors every edge. Therefore
\[
\chi'_\ell(G)\le k=\chi'(G),
\]
completing the proof of both cases. \(\square\)

## 5. What remains unresolved

The argument does **not** establish the unrestricted conjecture.

Its crucial feature is that the exceptional parallel class can be assigned the lowest auxiliary colors. Every induced subdigraph containing an exceptional edge then has an appropriate sink, reducing the kernel problem to a bipartite graph.

With several interacting exceptional classes inside one non-bipartite block, that sink argument is unavailable. An arbitrary preference digraph can contain a directed odd cycle with no kernel; an outdegree bound alone does not suffice. The block extension argument separates difficulties at cutvertices, but does not handle general non-bipartite \(2\)-connected blocks.

Thus the writeup supplies exact, non-bipartite special cases and a rooted extension property, but neither a general proof nor a counterexample.