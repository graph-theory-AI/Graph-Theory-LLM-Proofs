```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for every k at least 4 and for all 3-uniform H outside a sharply characterized null-pair/full-pair class, whose unique four-vertex member is also settled explicitly.",
  "would_publish": false,
  "caveats": "The remaining case is k=3 on at least five vertices with a disjoint null pair and full pair; perturbations are assumed nonempty and vertex-locally finite."
}
```

# Mathematical writeup

## 1. Interpretation and results

Write \(G\triangle D\) for the hypergraph obtained by toggling every \(k\)-set in \(D\). I use the intended definition that

\[
D\neq\varnothing,\qquad
|\{d\in D:v\in d\}|<\infty\quad\text{for every vertex }v.
\]

The empty perturbation must be excluded because the required \(G\) is itself \(H\)-free.

For a \(k\)-uniform hypergraph \(H\), let its 2-shadow \(\partial_2H\) be the graph on \(V(H)\) given by

\[
xy\in E(\partial_2H)
 \quad\Longleftrightarrow\quad
\text{some edge of }H\text{ contains }\{x,y\}.
\]

The main partial result is the following.

### Theorem A
Let \(H\) be a finite \(k\)-uniform hypergraph with an edge and a nonedge. If either \(\partial_2H\) or \(\partial_2\overline H\) is complete, then there is a countably infinite \(H\)-free \(k\)-graph \(G\) such that every nonempty locally finite perturbation of \(G\) contains an induced copy of \(H\).

Consequently:

1. the conjecture is true for every \(k\geq 4\);
2. for \(k=3\), it is true unless \(H\) has both
   - a **null pair** \(P\), contained in no edge of \(H\), and
   - a disjoint **full pair** \(Q\), contained in no nonedge of \(H\);
3. the only four-vertex 3-graph omitted by Theorem A is the 3-graph with exactly two edges, and this case also has an explicit construction.

Thus the only cases left open by this argument are 3-uniform \(H\) on at least five vertices having a disjoint null pair and full pair.

---

## 2. The free-amalgamation lemma

### Lemma 2.1
Suppose \(\partial_2H\) is complete. Then the class \(\mathcal K_H\) of finite induced-\(H\)-free \(k\)-graphs has free amalgamation.

#### Proof

Let \(A,B\in\mathcal K_H\) have a common induced subhypergraph \(C\). Their free amalgam \(F=A\oplus_C B\) has vertex set \(V(A)\cup_CV(B)\), and its edges are precisely the edges inherited from \(A\) or \(B\). In particular, no edge of \(F\) contains both a vertex of \(A\setminus C\) and a vertex of \(B\setminus C\).

Suppose that \(F\) contained an induced copy of \(H\) meeting both \(A\setminus C\) and \(B\setminus C\). Choose corresponding vertices \(x,y\in V(H)\) whose images lie on opposite sides. Since \(\partial_2H\) is complete, some edge of \(H\) contains \(x\) and \(y\). Its image would be an edge of \(F\) meeting both exclusive sides, contrary to the definition of the free amalgam. Thus every induced \(H\) in \(F\) would lie entirely in \(A\) or entirely in \(B\), which is impossible. ∎

It follows by the standard Fraïssé construction—or directly by repeatedly carrying out all finite extension requirements—that there is a countably infinite \(H\)-free \(k\)-graph \(U\) with the following extension property:

> If \(A\subseteq B\) are finite \(H\)-free \(k\)-graphs and \(\phi:A\to U\) is an induced embedding, then \(\phi\) extends to an induced embedding \(B\to U\).

The class has arbitrarily large members, for example empty hypergraphs, since \(H\) has an edge; hence \(U\) is infinite.

We shall also use the following consequence.

### Lemma 2.2
For every one-vertex extension \(A\subseteq B=A\cup\{b\}\) in \(\mathcal K_H\), every induced embedding \(A\to U\) has arbitrarily many distinct extensions realizing the role of \(b\).

#### Proof

Freely amalgamate \(N\) copies of \(B\) over their common copy of \(A\). By Lemma 2.1 the resulting finite hypergraph is still \(H\)-free. Embedding this amalgam into \(U\) over \(A\) gives \(N\) distinct realizations of \(b\). ∎

---

## 3. Robustness under locally finite perturbations

We now prove Theorem A when \(\partial_2H\) is complete.

Let \(D\neq\varnothing\) be locally finite, and choose a changed \(k\)-set \(e\in D\).

### Case 1: \(e\notin E(U)\)

Choose an edge \(q\in E(H)\), and let

\[
B=H-q.
\]

Then \(B\) is \(H\)-free: it has exactly \(|V(H)|\) vertices but one fewer edge than \(H\), so it cannot be isomorphic to \(H\). Moreover, \(B[q]\) agrees with \(U[e]\), both being nonedges.

### Case 2: \(e\in E(U)\)

Choose a nonedge \(q\notin E(H)\), and let

\[
B=H+q.
\]

Again \(B\) is \(H\)-free, now having one more edge than \(H\), and \(B[q]\) agrees with \(U[e]\), both being edges.

In either case, toggling \(q\) in \(B\) gives \(H\). We must embed \(B\) over \(q\mapsto e\) while avoiding all other changes in \(D\).

Order the vertices of \(B\setminus q\) as \(b_1,\dots,b_r\), and build an induced embedding one vertex at a time. Suppose that the current image is the finite set \(S_i\), initially \(S_0=e\). Define

\[
N_D(S_i)=\bigcup\{d\in D:d\cap S_i\neq\varnothing\}.
\]

This is finite: every vertex of \(S_i\) belongs to only finitely many members of \(D\).

By Lemma 2.2 there are arbitrarily many choices for the image of \(b_{i+1}\) that realize the required one-vertex extension. Choose one outside \(N_D(S_i)\). If \(x\) is this new vertex, no member of \(D\) newly contained in \(S_i\cup\{x\}\) can use \(x\): such a member would contain another vertex of \(S_i\), forcing \(x\in N_D(S_i)\). Consequently,

\[
D\cap [S_i\cup\{x\}]^k
 =
D\cap [S_i]^k.
\]

Starting from \(D\cap[e]^k=\{e\}\), induction yields a final embedding \(\phi:B\to U\) with image \(S\) satisfying

\[
D\cap[S]^k=\{e\}.
\]

Thus \((U\triangle D)[S]\) is obtained from \(B\) by toggling precisely \(q\), and hence is an induced copy of \(H\).

This proves Theorem A when \(\partial_2H\) is complete.

If instead \(\partial_2\overline H\) is complete, apply the result to \(\overline H\), obtaining a robust \(\overline H\)-free hypergraph \(U\), and put \(G=\overline U\). Since

\[
\overline{U\triangle D}=\overline U\triangle D,
\]

an induced \(\overline H\) in \(U\triangle D\) corresponds to an induced \(H\) in \(G\triangle D\). This completes the proof of Theorem A. ∎

---

## 4. Why this proves every uniformity \(k\geq4\)

### Proposition 4.1
If \(k\geq4\), then for every finite \(k\)-graph \(H\), either \(\partial_2H\) or \(\partial_2\overline H\) is complete.

#### Proof

Suppose neither is complete. Then there is a pair \(P\) contained in no edge of \(H\), and a pair \(Q\) contained in no edge of \(\overline H\). Equivalently, every \(k\)-set containing \(Q\) is an edge of \(H\).

Since \(k\geq4\), we have \(|P\cup Q|\leq4\leq k\). The hypothesis that \(H\) has both an edge and a nonedge implies \(|V(H)|\geq k+1\), so choose a \(k\)-set \(T\) containing \(P\cup Q\). Because \(P\subseteq T\), the set \(T\) is a nonedge of \(H\); because \(Q\subseteq T\), it is an edge of \(H\), a contradiction. ∎

Combining Proposition 4.1 with Theorem A proves the original conjecture in full for every \(k\geq4\).

---

## 5. Reduction of the 3-uniform case

For a 3-graph, call a pair \(P\)

- **null** if every triple containing \(P\) is a nonedge;
- **full** if every triple containing \(P\) is an edge.

If neither \(\partial_2H\) nor \(\partial_2\overline H\) is complete, then \(H\) has a null pair \(P\) and a full pair \(Q\). They must be disjoint: if they intersect, a triple containing \(P\cup Q\) would be both an edge and a nonedge.

Conversely, the existence of disjoint such pairs shows that both shadows are incomplete. Therefore Theorem A settles precisely those 3-graphs having no disjoint null pair and full pair.

Moreover, on the four vertices \(P\cup Q\), the two triples containing \(P\) are nonedges and the two triples containing \(Q\) are edges. Thus every remaining \(H\) contains an induced four-vertex 3-graph with exactly two edges.

When \(|V(H)|=4\), this determines \(H\) completely. The following construction settles that case.

---

## 6. The two-edge 3-graph on four vertices

Let \(F\) denote the 3-uniform hypergraph on four vertices having exactly two edges. All such 3-graphs are isomorphic.

Let

\[
V=\left\{x\in\{0,1\}^{\mathbb N}:
x\text{ has finite support}\right\}.
\]

This set is countably infinite. For three distinct sequences \(x,y,z\), let

\[
\ell(x,y,z)
 =
\min\{i:x_i,y_i,z_i\text{ are not all equal}\}.
\]

Declare \(\{x,y,z\}\) to be an edge exactly when \(\ell(x,y,z)\) is odd. Call the resulting 3-graph \(G\).

### Lemma 6.1
The 3-graph \(G\) is induced-\(F\)-free.

#### Proof

Take four vertices and let \(n\) be the first coordinate at which their bits are not all equal.

If the split at coordinate \(n\) is \(2+2\), every triple meets both bit classes, so all four triples have status \(n\bmod2\). The induced edge count is therefore \(0\) or \(4\).

If the split is \(1+3\), the three triples containing the singleton have status \(n\bmod2\), while the triple inside the class of size three has some status \(q\in\{0,1\}\). The total edge count is therefore either \(q\in\{0,1\}\) or \(3+q\in\{3,4\}\).

In no case is the edge count two. ∎

### Lemma 6.2
Every nonempty locally finite perturbation of \(G\) contains an induced \(F\).

#### Proof

Let \(D\neq\varnothing\) be locally finite, and choose \(e=\{a,b,c\}\in D\). Put \(n=\ell(a,b,c)\). At coordinate \(n\), two of the sequences have the same bit; call them \(a,b\), and call \(c\) the minority sequence.

Choose \(w\) such that:

1. \(w\) agrees with \(a,b,c\) before coordinate \(n\);
2. \(w_n\) is the majority bit shared by \(a,b\);
3. \(\ell(a,b,w)=n+1\).

Condition 3 can always be arranged: if \(a\) and \(b\) differ at \(n+1\), it is automatic; otherwise choose \(w_{n+1}\) opposite to their common bit. There are infinitely many possible finite-support tails, hence infinitely many such \(w\).

For every such \(w\),

\[
\ell(a,b,c)=\ell(a,c,w)=\ell(b,c,w)=n,
\qquad
\ell(a,b,w)=n+1.
\]

Hence, before perturbation, the four-set \(\{a,b,c,w\}\) has:

- exactly one edge if \(n\) is even, namely \(abw\);
- exactly three edges if \(n\) is odd, namely \(abc,acw,bcw\).

In the first case \(e=abc\) is a nonedge and its toggle raises the count from one to two. In the second case \(e\) is an edge and its toggle lowers the count from three to two.

It remains to choose \(w\) so no other triple in this four-set is changed. Every other triple in the four-set meets \(e\), and local finiteness implies that only finitely many changed triples meet one of \(a,b,c\). Thus only finitely many of the infinitely many candidate \(w\)'s are spoiled. For an unspoiled choice, \(G\triangle D\) induces exactly two edges on \(\{a,b,c,w\}\), hence an induced \(F\). ∎

Thus all 3-uniform hypergraphs on four vertices having both an edge and a nonedge satisfy the conjecture.

---

## 7. Remaining gap

The only unresolved class after these arguments consists of 3-uniform \(H\) with at least five vertices possessing a null pair \(P\) and a disjoint full pair \(Q\).

The free-amalgamation method genuinely fails there. If \(P=\{u,v\}\) is null, then the free amalgam of \(H-u\) and \(H-v\) over \(H-\{u,v\}\) reconstructs \(H\): all triples containing both \(u\) and \(v\) are absent, exactly as required. Thus the age of finite \(H\)-free 3-graphs need not have free amalgamation. Dually, the full pair obstructs the complementary free-amalgamation construction.

The alternating binary construction above handles the minimal four-vertex obstruction, but it does not automatically extend to larger \(H\): a larger exceptional \(H\) can contain several induced two-edge four-sets not all involving the hyperedge changed by a perturbation.

Therefore this is a substantial partial resolution, not a proof of the full \(k=3\) case.