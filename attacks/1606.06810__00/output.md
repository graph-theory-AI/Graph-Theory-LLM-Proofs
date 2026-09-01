```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured formula holds for all t when n is at most t+2, for all n when t is at most 4, and for every (t-2)-degenerate instance.",
  "would_publish": false,
  "caveats": "The minimum-degree core for t at least 5 and n at least t+3 remains unresolved; no counterexample to the conjectured bound is found."
}
```

# Mathematical writeup

## 1. Statement and convention

Write \(c(G)\) for the number of cliques of \(G\), including the empty clique. This convention is forced by the stated lower-bound construction: if \(S\) is a clique of order \(t-2\) and \(X\) is an independent set of order \(n-t+2\), with every edge between \(S\) and \(X\), then

\[
c(G)=2^{t-2}(|X|+1)=2^{t-2}(n-t+3).
\]

Let

\[
B_t(n):=2^{t-2}(n-t+3).
\]

Every branch vertex of a weak \(K_t\)-immersion has degree at least \(t-1\), since the \(t-1\) paths incident with it must start with distinct edges. In the construction above, every vertex of \(X\) has degree \(t-2\), leaving only \(t-2\) possible branch vertices. Thus the construction contains no weak \(K_t\)-immersion.

The general conjecture remains open here. I prove the following partial results.

### Partial theorem

For finite simple graphs:

1. If \(G\) is \((t-2)\)-degenerate, then \(c(G)\le B_t(n)\), without needing any immersion hypothesis.
2. Consequently, the conjecture holds for all chordal graphs.
3. The conjecture holds for every \(n\ge t-2\) when \(t\le4\).
4. The conjecture holds for every \(t\ge2\) whenever
   \[
   t-2\le n\le t+2.
   \]

The fourth assertion is the main additional finite-range result.

---

## 2. Clique recurrence and the degeneracy bound

For every vertex \(v\),

\[
c(G)=c(G-v)+c(G[N_G(v)]).
\tag{2.1}
\]

Indeed, cliques not containing \(v\) are counted by \(c(G-v)\), while cliques containing \(v\) are obtained by adjoining \(v\) to an arbitrary clique of \(G[N(v)]\).

### Lemma 2.1
If \(G\) is \(d\)-degenerate and \(n\ge d\), then

\[
c(G)\le 2^d(n-d+1).
\tag{2.2}
\]

#### Proof
Repeatedly delete a vertex of current degree at most \(d\), stopping when \(d\) vertices remain. At each deletion, (2.1) shows that at most \(2^d\) cliques are lost. The remaining graph has at most \(2^d\) cliques. Therefore

\[
c(G)\le (n-d)2^d+2^d=2^d(n-d+1).
\]

For \(d=0\), the same argument stops at the empty graph. \(\square\)

Taking \(d=t-2\) gives exactly

\[
2^{t-2}(n-(t-2)+1)=B_t(n).
\]

In particular, if at most \(t-1\) vertices of \(G\) have degree at least \(t-1\), then \(G\) is \((t-2)\)-degenerate: every subgraph either contains a vertex whose original degree is at most \(t-2\), or has at most \(t-1\) vertices.

### Core reduction

Repeatedly delete vertices of current degree at most \(t-2\), and let \(H\) be the remaining \((t-1)\)-core, of order \(h\). Then

\[
c(G)\le c(H)+(n-h)2^{t-2}.
\tag{2.3}
\]

Consequently, if \(G\) violates the conjectured bound, then

\[
c(H)>B_t(h).
\]

Thus any counterexample contains a counterexample of minimum degree at least \(t-1\).

Moreover, if \(G\) is a counterexample of minimum order, then for every \(v\),

\[
c(G[N(v)])>B_t(n)-B_t(n-1)=2^{t-2}.
\tag{2.4}
\]

This is stronger than merely \(\deg(v)\ge t-1\), but I do not know how to turn (2.4) into a general immersion.

---

## 3. Chordal graphs and the cases \(t\le4\)

### Chordal graphs

If a chordal graph \(G\) has no \(K_t\)-immersion, then in particular it has no \(K_t\) subgraph, so \(\omega(G)\le t-1\). A perfect elimination ordering has at most \(t-2\) later neighbors at every vertex. Hence \(G\) is \((t-2)\)-degenerate, and Lemma 2.1 proves the conjectured bound.

The lower-bound split graph is chordal, so the bound is sharp within this class.

### The case \(t=2\)

A graph with no \(K_2\)-immersion is edgeless. Hence

\[
c(G)=n+1=B_2(n).
\]

### The case \(t=3\)

A graph contains a weak \(K_3\)-immersion if and only if it contains a cycle. One direction follows by choosing three vertices on a cycle. Conversely, the three edge-disjoint paths of a \(K_3\)-immersion concatenate to a closed trail, which contains a cycle.

Thus \(K_3\)-immersion-free graphs are forests. Such a graph has at most \(n-1\) edges and no larger clique, so

\[
c(G)\le 1+n+(n-1)=2n=B_3(n).
\]

### The case \(t=4\)

I use two standard elementary facts:

- every \(K_4\)-minor model can be converted into a subdivision of \(K_4\), because \(K_4\) has maximum degree three;
- every \(K_4\)-minor-free graph is \(2\)-degenerate.

For the first fact, in each branch set of a minor model, take a minimal tree connecting the at most three attachment vertices. Its three arms meet at a single median vertex, producing a subdivision model. The second fact is the usual characterization of \(K_4\)-minor-free graphs as partial \(2\)-trees.

Therefore, if \(G\) has no weak \(K_4\)-immersion, it has no \(K_4\) subdivision and hence no \(K_4\) minor. It is consequently \(2\)-degenerate. Lemma 2.1 yields

\[
c(G)\le 4(n-1)=B_4(n).
\]

This proves the conjecture for all \(n\) when \(t\le4\).

---

## 4. A dense-complement routing lemma

The following lemma is used to settle \(n=t+2\).

### Lemma 4.1
Let \(H\) be a graph on \(N\ge4\) vertices with \(\Delta(H)\le2\). If \(H\) has at most one odd-cycle component, then \(\overline H\) contains a strong immersion of \(K_{N-2}\).

#### Proof

Since \(\Delta(H)\le2\), every component of \(H\) is a path or a cycle; isolated vertices are regarded as paths of order one.

We first describe a routing certificate. Choose two vertices \(x,y\), and put

\[
B=V(H)\setminus\{x,y\}.
\]

The vertices of \(B\) will be the branch vertices. For every incidence \((v,e)\), where \(e\in E(H[B])\) is incident with \(v\), assign one of the labels \(x,y\), subject to:

1. the assigned label \(z\) is not adjacent to \(v\) in \(H\);
2. the two incidences at a degree-two vertex of \(H[B]\) receive different labels;
3. on all but at most one edge of \(H[B]\), the labels at its two ends agree;
4. if one edge has different labels at its ends, then \(xy\notin E(H)\).

Such an assignment gives an immersion in \(G=\overline H\). Namely, a missing branch edge \(uv\in E(H[B])\) is routed as

\[
u-z-v
\]

if both incidences have label \(z\), and as

\[
u-x-y-v
\]

or \(u-y-x-v\) if the labels differ. All branch pairs that are adjacent in \(G[B]\) use their edge directly.

Condition 2 ensures that no edge from a branch vertex to \(x\) or \(y\) is repeated. There is at most one use of \(xy\), and direct branch edges are disjoint from all the other routing edges. Thus these paths form a strong immersion.

It remains to choose \(x,y\) and the labels. On a path, alternating the two labels satisfies condition 2. If labels are prescribed at both ends, either the alternating assignment works or one edge must be made exceptional. An even cycle has an alternating assignment with no exceptional edge, while an odd cycle requires one.

We choose \(x,y\) as follows.

- If \(H\) has at least two path components, choose an endvertex from each of two such components. The selected path components leave paths with at most one prescribed end label, so they need no exceptional edge. All even cycles alternate, and the possible unique odd cycle uses one exceptional edge. Since \(x,y\) lie in distinct components, \(xy\notin E(H)\).
- If \(H\) has exactly one path component and at least one cycle, choose \(x\) at an end of the path. If an odd cycle exists, choose \(y\) on that cycle; otherwise choose \(y\) on any cycle. Deleting a vertex from an odd cycle leaves a path whose two forced end labels are compatible, while deleting a vertex from an even cycle creates exactly one parity defect. Again \(x,y\) lie in different components.
- If all components are cycles and there is an odd cycle together with another cycle, choose \(x\) on the odd cycle and \(y\) on another, necessarily even, cycle. The first creates no defect and the second creates one.
- If all components are even cycles, choose two vertices at distance two on one cycle. The intervening vertex becomes isolated, and the other resulting path has compatible forced end labels.
- If \(H\) is a single path, choose its two endvertices. The remaining path has at most one parity defect, and the two ends are nonadjacent because \(N\ge4\).
- If \(H\) is a single cycle, choose two vertices at distance two. For an even cycle there is no defect, and for an odd cycle there is one. In the latter case the selected vertices are nonadjacent in \(H\).

In every case there is at most one exceptional edge, and whenever it exists \(xy\notin E(H)\). This supplies the required routing certificate. \(\square\)

---

## 5. Exact result for \(t-2\le n\le t+2\)

### Theorem 5.1
For every \(t\ge2\) and every

\[
t-2\le n\le t+2,
\]

every \(n\)-vertex graph with no weak \(K_t\)-immersion has at most \(B_t(n)\) cliques.

#### Proof

Put \(d=t-2\).

### Case \(n=t-2\)

There are at most \(2^{t-2}\) vertex subsets, and

\[
B_t(t-2)=2^{t-2}.
\]

Equality is attained by \(K_{t-2}\).

### Case \(n=t-1\)

Again the complete graph is allowed, since there are too few branch vertices. Thus

\[
c(G)\le2^{t-1}=B_t(t-1).
\]

### Case \(n=t\)

A \(K_t\)-immersion on exactly \(t\) host vertices uses \(\binom t2\) edge-disjoint nontrivial paths, and therefore at least \(\binom t2\) host edges. Thus every proper subgraph of \(K_t\) has no \(K_t\)-immersion.

Every forbidden graph has a nonedge \(xy\). A clique cannot contain both \(x\) and \(y\), so

\[
c(G)\le 2^t-2^{t-2}=3\cdot2^{t-2}=B_t(t).
\]

Equality is attained by \(K_t-xy\).

### Case \(n=t+1\)

Suppose first that \(G\) has a vertex \(v\) with \(\deg(v)\le t-2\). By (2.1) and the preceding case,

\[
c(G)\le B_t(t)+2^{t-2}
     =4\cdot2^{t-2}
     =B_t(t+1).
\]

It remains to show that a \(K_t\)-immersion-free graph must have such a vertex. Suppose instead that \(\delta(G)\ge t-1\), and let \(H=\overline G\). Since \(n=t+1\),

\[
\Delta(H)\le (n-1)-(t-1)=1.
\]

Thus \(H\) is a matching together with isolated vertices.

If \(H\) is empty, \(G\) contains \(K_t\). Otherwise choose one endpoint \(x\) of a matching edge \(xy\), and take \(V(G)\setminus\{x\}\) as the \(t\) branch vertices. Every remaining missing branch edge \(uv\) is another edge of the matching and can be routed as

\[
u-x-v.
\]

These paths are edge-disjoint, and all other branch pairs use their direct edges. This is a strong \(K_t\)-immersion, a contradiction.

Hence the low-degree vertex exists and the desired bound follows.

### Case \(n=t+2\)

If \(G\) has a vertex \(v\) of degree at most \(t-2\), then the \(n=t+1\) case and (2.1) give

\[
c(G)\le B_t(t+1)+2^{t-2}
     =5\cdot2^{t-2}
     =B_t(t+2).
\]

Assume now that \(\delta(G)\ge t-1\), and put \(H=\overline G\). Then

\[
\Delta(H)\le (t+1)-(t-1)=2.
\]

If \(H\) has at most one odd-cycle component, Lemma 4.1 gives a strong immersion of

\[
K_{n-2}=K_t
\]

in \(G\), contrary to the hypothesis. Hence \(H\) has at least two odd-cycle components.

Cliques of \(G\) are independent sets of \(H\). If \(C\) is an odd cycle, then

\[
i(C)\le 2^{|C|-1}.
\tag{5.1}
\]

For \(C_3\), this is equality. Every longer odd cycle contains a four-vertex path, which has eight independent sets, giving

\[
i(C)\le 8\cdot2^{|C|-4}=2^{|C|-1}.
\]

Since independent-set counts multiply over components, two odd-cycle components imply

\[
c(G)=i(H)\le 2^{n-2}
             =4\cdot2^{t-2}
             <5\cdot2^{t-2}=B_t(t+2).
\]

This completes every case. The standard split construction attains equality throughout the range. \(\square\)

---

## 6. Minimum degree alone does not settle the conjecture

The core reduction cannot be completed by asserting that every graph of minimum degree at least \(t-1\) contains a weak \(K_t\)-immersion.

For \(q\ge4\), let \(G_q\) be the complete \(q\)-partite graph with every part of order three. Set

\[
n=3q,\qquad t=n-2=3q-2.
\]

Every vertex has degree

\[
n-3=t-1.
\]

Nevertheless, \(G_q\) has no weak \(K_t\)-immersion.

Indeed, suppose such an immersion existed. There would be \(t=n-2\) branch vertices and two nonbranch vertices \(x,y\). Since every branch vertex has degree exactly \(t-1\), its incident immersion paths exhaust all its incident edges. Consequently:

- no branch vertex can occur internally on another immersion path;
- every edge joining two branch vertices must be the direct path for that branch pair.

Call a part full if all three of its vertices are branch vertices. Within a full part, the three missing branch pairs form a triangle. Each of its three vertices must use its edges to \(x\) and \(y\), one for each of its two missing partners. A triangle cannot be properly edge-coloured with the two labels \(x,y\); therefore at least one of its three paths must use the edge \(xy\). Thus at most one full part can be routed if \(xy\in E(G_q)\), and none can be routed if \(xy\notin E(G_q)\).

If \(x,y\) lie in distinct parts, there are \(q-2\ge2\) full parts and only one edge \(xy\). If they lie in the same part, there are \(q-1\) full parts and \(xy\notin E(G_q)\). Both are impossible.

This family has

\[
c(G_q)=4^q,
\]

while the conjectured bound is

\[
B_t(n)=5\cdot2^{3q-4}.
\]

Thus it is far below the conjectured extremal count, but it demonstrates that the remaining minimum-degree core is a genuine issue rather than a removable technicality.

---

## 7. Remaining gap

A hypothetical minimum-order counterexample must now satisfy all of the following:

- \(t\ge5\);
- \(n\ge t+3\);
- \(\delta(G)\ge t-1\);
- for every vertex \(v\),
  \[
  c(G[N(v)])>2^{t-2}.
  \]

The explicit multipartite family above shows that minimum degree \(t-1\) by itself does not force the required immersion. The unresolved task is therefore to exploit the much stronger neighborhood clique condition, or otherwise control the clique contribution of such minimum-degree immersion-free cores.

No argument given here covers that general case, and no counterexample to the stated clique bound has been obtained.