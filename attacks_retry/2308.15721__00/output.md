```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The corrected conjecture holds for C5, all stars, and all K_{2,t}; its defective equality also holds for every complete bipartite target.",
  "would_publish": false,
  "caveats": "Uses the ordinary-minor defective theorem quoted in the prompt; novelty is not claimed, and the general conjecture remains open."
}
```

## 1. Statement being attacked

I use the corrected source statement quoted in the supplied referee report:
\[
\chi_\Delta(\mathcal G_H^{\mathrm{odd}})
=\overline{\operatorname{td}}(H)-1,
\qquad
\chi_\star(\mathcal G_H^{\mathrm{odd}})
\le 2\overline{\operatorname{td}}(H)-2.
\tag{C}
\]
The catalog’s reconstructed equality for \(\chi_\star\) is not this conjecture. The previous claw calculation is consistent with (C), so I discard its claimed disproof.

Here are two partial results. I do not know whether these special cases are already explicitly recorded in the literature.

### Theorem A: complete bipartite targets

For integers \(1\le s\le t\),
\[
\boxed{\chi_\Delta(\mathcal G_{K_{s,t}}^{\mathrm{odd}})=s}
\]
and
\[
\boxed{\chi_\star(\mathcal G_{K_{s,t}}^{\mathrm{odd}})\le 2^s.}
\]
For \(t\ge2\), the latter colouring can have clustering
\[
2^{s-1}(t-1).
\]

Since \(\overline{\operatorname{td}}(K_{s,t})=s+1\), both assertions of (C) follow when \(s\le2\). For general \(s\), this proves the defective assertion and improves the supplied exponential clustered bound for these targets.

### Theorem B: a non-bipartite target

\[
\boxed{
\chi_\Delta(\mathcal G_{C_5}^{\mathrm{odd}})
=
\chi_\star(\mathcal G_{C_5}^{\mathrm{odd}})
=3.
}
\]
Indeed, every odd-\(C_5\)-minor-free graph has a \(3\)-colouring with clustering \(2\).

Since \(\overline{\operatorname{td}}(C_5)=4\), this proves both assertions of (C) for \(C_5\), with a stronger clustered bound.

All graphs below are finite and simple. In an odd model, branch trees are properly \(2\)-coloured, and each required edge between branch trees has equally coloured endpoints.

---

## 2. A parity-selection lemma

Write \(\mathcal G_F\) for the class excluding \(F\) as an ordinary minor.

**Lemma 1.** Let \(s,t\ge1\), and put
\[
N=2^{s-1}(t-1)+1.
\]
Every graph with an ordinary \(K_{s,N}\)-minor has an odd \(K_{s,t}\)-minor. Consequently,
\[
\mathcal G_{K_{s,t}}
\subseteq
\mathcal G_{K_{s,t}}^{\mathrm{odd}}
\subseteq
\mathcal G_{K_{s,N}}.
\tag{1}
\]

**Proof.**
Take an ordinary model with branch trees
\[
A_1,\dots,A_s,\qquad B_1,\dots,B_N.
\]
For every \(i,j\), choose one model edge
\[
e_{ij}=u_{ij}v_{ij},
\qquad
u_{ij}\in A_i,\quad v_{ij}\in B_j.
\]

Properly \(2\)-colour each branch tree independently, using colours in \(\mathbb F_2\). Let these colourings be \(a_i\) and \(b_j\), and define
\[
p_{ij}=a_i(u_{ij})+b_j(v_{ij}).
\]
Associate with \(B_j\) the signature
\[
\sigma_j=(p_{2j}+p_{1j},\dots,p_{sj}+p_{1j})
\in\mathbb F_2^{s-1}.
\]
There are \(2^{s-1}\) possible signatures, so at least \(t\) of the \(B_j\)'s have a common signature \(\sigma\). Retain those branch trees.

Leave the colouring of \(A_1\) unchanged. For \(i\ge2\), flip the colouring of \(A_i\) by \(\sigma_i\). Flip the colouring of each retained \(B_j\) by \(p_{1j}\). For every retained model edge, its new endpoint-colour difference is
\[
p_{ij}+\sigma_i+p_{1j}=0,
\]
where \(\sigma_1:=0\). All required model edges are therefore monochromatic, while all branch-tree colourings remain proper. This is an odd \(K_{s,t}\)-model.

The second inclusion in (1) is the contrapositive. The first holds because every odd minor is an ordinary minor. \(\square\)

The explicit parity argument is essential: an arbitrary ordinary model need not itself be an odd model.

---

## 3. Proof of Theorem A

### 3.1. The defective equality

For \(1\le s\le q\),
\[
\overline{\operatorname{td}}(K_{s,q})=s+1.
\tag{2}
\]

For the upper bound, put the \(s\) vertices of the smaller part on a rooted chain and make every vertex of the other part a child of its last vertex.

For the lower bound, \(K_{s,q}\) has a \(K_{s+1}\)-minor: use branch sets
\[
\{a_i,b_i\}\quad(1\le i<s),\qquad
\{a_s\},\qquad
\{b_s\}.
\]
They are pairwise adjacent. Ordinary tree-depth is minor-monotone, equals \(s+1\) on \(K_{s+1}\), and agrees with connected tree-depth on connected graphs. This proves (2).

The only non-elementary input in this part is the established ordinary-minor theorem quoted in the question:
\[
\chi_\Delta(\mathcal G_F)
=\overline{\operatorname{td}}(F)-1.
\tag{3}
\]
For \(N=2^{s-1}(t-1)+1\), we have \(N\ge t\ge s\). Applying (3) to both ends of (1), and using (2), gives
\[
s
=\chi_\Delta(\mathcal G_{K_{s,t}})
\le
\chi_\Delta(\mathcal G_{K_{s,t}}^{\mathrm{odd}})
\le
\chi_\Delta(\mathcal G_{K_{s,N}})
=s.
\]
Thus the defective equality follows.

### 3.2. An elementary clustered bound for ordinary complete bipartite minors

**Lemma 2.** For integers \(a\ge1\) and \(b\ge2\), every \(K_{a,b}\)-minor-free graph has a \(2^a\)-colouring with clustering at most \(b-1\).

**Proof.**
Proceed by induction on \(a\), treating connected components independently.

For \(a=1\), choose a root and its breadth-first layers
\[
L_0,L_1,\dots.
\]
For \(i\ge1\), the vertices in earlier layers induce a connected subgraph adjacent to every vertex of \(L_i\). If \(|L_i|\ge b\), contracting that earlier subgraph and retaining \(b\) vertices of \(L_i\) gives a \(K_{1,b}\)-minor. Hence every layer has at most \(b-1\) vertices.

Colour by layer parity. Edges join vertices in the same layer or in consecutive layers, so every monochromatic component lies in one layer and has at most \(b-1\) vertices.

Now let \(a\ge2\). Each layer \(L_i\) is \(K_{a-1,b}\)-minor-free. Indeed, a model of \(K_{a-1,b}\) inside \(L_i\), together with the connected union of earlier layers as one additional branch set, would give a \(K_{a,b}\)-model: the additional branch set has an edge to each of the \(b\) right-hand branch sets. The root layer cannot contain such a model.

By induction, colour each layer with \(2^{a-1}\) colours and clustering \(b-1\). Use disjoint palettes for even and odd layers. Again every monochromatic component stays inside one layer. This uses \(2^a\) colours. \(\square\)

Apply Lemma 2 with
\[
a=s,\qquad b=N=2^{s-1}(t-1)+1,
\]
and use (1). For \(t\ge2\), this gives \(2^s\) colours and clustering
\[
N-1=2^{s-1}(t-1).
\]
When \(s=t=1\), the excluded target is an edge, so the class consists of edgeless graphs and one colour with clustering \(1\) suffices.

This completes Theorem A.

### Extension to some non-complete bipartite targets

Suppose \(H\) has a bipartition with side sizes \(s\le t\) and
\[
\overline{\operatorname{td}}(H)=s+1.
\]
Since \(H\) is a subgraph of \(K_{s,t}\),
\[
\mathcal G_H^{\mathrm{odd}}
\subseteq
\mathcal G_{K_{s,t}}^{\mathrm{odd}}.
\]
The ordinary-minor lower bound and Theorem A therefore give
\[
\chi_\Delta(\mathcal G_H^{\mathrm{odd}})=s,
\qquad
\chi_\star(\mathcal G_H^{\mathrm{odd}})\le2^s.
\]
In particular, both conjectured bounds hold for all such targets with \(s\le2\). This includes every target of connected tree-depth \(2\), since such a graph is a subgraph of a star.

---

## 4. Odd cycle minors

To prove Theorem B, first identify the excluded configurations exactly.

**Lemma 3.** For \(m\ge3\), a graph has an odd \(C_m\)-minor if and only if it contains a cycle of length \(\ell\ge m\) with
\[
\ell\equiv m\pmod2.
\]

**Proof.**
Given an odd \(C_m\)-model, retain its branch trees and exactly one model edge for each cycle edge. Their union is connected and unicyclic. Its unique cycle uses all \(m\) model edges, together with one internal path in each branch tree.

Along the unique cycle, model edges preserve the witness colour and internal tree edges change it. The total number of internal tree edges is therefore even. Consequently the cycle has length at least \(m\) and the same parity as \(m\).

Conversely, suppose a cycle has length \(\ell\ge m\) with \(\ell-m\) even. Take \(m-1\) consecutive vertices as singleton branch trees, and take the remaining path as the last branch tree. That path has \(\ell-m\) edges, an even number. Colour all singleton branches \(0\), and properly colour the path with both endpoints \(0\). All model edges are monochromatic. \(\square\)

Thus
\[
G\in\mathcal G_{C_5}^{\mathrm{odd}}
\quad\Longleftrightarrow\quad
G\text{ has no odd cycle of length at least }5.
\tag{4}
\]

---

## 5. Structure of graphs with no long odd cycle

Let \(B_m\) be the *book graph* with adjacent vertices \(a,b\) and independent vertices \(x_1,\dots,x_m\), each adjacent to both \(a\) and \(b\).

**Lemma 4.** A \(2\)-connected non-bipartite graph with no odd cycle of length at least \(5\) is either \(K_4\) or a book \(B_m\).

**Proof.**
We use the following elementary observation. If \(J\) is a non-spanning subgraph of a \(2\)-connected graph \(G\), with at least two vertices, then some component of \(G-V(J)\) has two distinct neighbours in \(J\). Otherwise a single attachment vertex would be a cutvertex. Consequently there is a path with distinct endpoints in \(J\), at least one internal vertex, and all internal vertices outside \(J\). Call it a \(J\)-ear.

First suppose \(G\) contains a \(K_4\). If this \(K_4\) is not spanning, take an ear of length \(r\ge2\). Between its endpoints, the \(K_4\) contains paths of lengths \(2\) and \(3\). One of their unions with the ear is an odd cycle of length at least \(5\), a contradiction. Hence \(G=K_4\).

Now suppose \(G\) is \(K_4\)-free. Since it is non-bipartite, it contains an odd cycle, necessarily a triangle.

An ear of a triangle can only have length \(2\): an even length at least \(4\), together with the triangle edge between its endpoints, gives a forbidden odd cycle; an odd length at least \(3\), together with the other two triangle edges, does likewise. Thus, unless \(G\) is the triangle itself, the first ear produces a book \(B_2\).

Suppose a book \(B_m\), \(m\ge2\), has been obtained.

- Between its two hub vertices there are paths of lengths \(1\) and \(2\). Thus an ear between the hubs must have length \(2\), adding one new page.
- Between any other pair of distinct vertices there are paths of lengths \(2\) and \(3\). Hence an ear of length at least \(2\) between such a pair would create an odd cycle of length at least \(5\), regardless of its parity.

Therefore every subsequent ear adds a page to the same book. Since \(G\) is \(K_4\)-free, there are no edges between pages. Repeatedly taking ears until all vertices are included proves that \(G\) is a book. \(\square\)

It follows that every block of a graph satisfying (4) is bipartite, a book, or \(K_4\). Bridges and isolated vertices cause no difficulty.

---

## 6. Proof of Theorem B

### 6.1. Three colours with clustering two

Root the block decomposition of each connected component at an arbitrary vertex. Process its blocks outwards. When processing a block \(Q\), its parent vertex \(x\) is already coloured.

Give every vertex of \(Q-x\) one of the other two colours. This can be done with clustering at most \(2\):

- If \(Q\) is bipartite, properly \(2\)-colour \(Q-x\).
- If \(Q\) is a book and \(x\) is a hub, then \(Q-x\) is a star.
- If \(Q\) is a book and \(x\) is a page, colour both hubs alike and all other pages with the other colour. The only non-singleton monochromatic component is the hub edge.
- If \(Q=K_4\), then \(Q-x=K_3\), which has a \(2\)-colouring with clustering \(2\).

Crucially, no new vertex in \(Q\) receives the colour of \(x\). Thus no monochromatic component can grow through \(x\) from the previously processed graph into \(Q-x\). Continuing through the block decomposition produces a \(3\)-colouring of the whole graph with clustering \(2\). Therefore
\[
\chi_\star(\mathcal G_{C_5}^{\mathrm{odd}})\le3.
\tag{5}
\]

### 6.2. Two colours cannot have uniformly bounded defect

For each integer \(d\ge0\), construct \(F_d\) as follows:

- take a vertex \(r\);
- take \(d+1\) disjoint stars, each with \(d+1\) leaves;
- join \(r\) to every vertex of every star.

Every block is a book. Thus every cycle has length \(3\) or \(4\), and Lemma 3 shows that
\[
F_d\in\mathcal G_{C_5}^{\mathrm{odd}}.
\]

Suppose \(F_d\) had a \(2\)-colouring with defect at most \(d\). Say \(r\) is red. Since \(r\) is universal, at most \(d\) other vertices are red. There are \(d+1\) disjoint star vertex sets, so one of them is entirely blue. Its centre then has \(d+1\) blue neighbours, a contradiction.

Hence no uniform defect bound works with two colours:
\[
\chi_\Delta(\mathcal G_{C_5}^{\mathrm{odd}})\ge3.
\tag{6}
\]
Combining (5), (6), and \(\chi_\Delta\le\chi_\star\) gives
\[
\chi_\Delta(\mathcal G_{C_5}^{\mathrm{odd}})
=
\chi_\star(\mathcal G_{C_5}^{\mathrm{odd}})
=3.
\]

Finally, deleting any vertex of \(C_5\) leaves \(P_4\), whose tree-depth is \(3\). The tree-depth deletion recurrence therefore gives
\[
\overline{\operatorname{td}}(C_5)=4.
\]
Thus both parts of (C) hold for this target.

---

## 7. What remains unresolved

These arguments leave substantial gaps:

- For \(K_{s,t}\) with \(s\ge3\), the clustered argument gives \(2^s\), not the conjectured \(2s\).
- The parity-selection lemma exploits the complete bipartite structure; it does not prove the defective equality for arbitrary non-bipartite targets.
- The \(C_5\) argument relies on a special block classification that does not extend directly to longer excluded odd cycles.

Thus the general source conjecture remains unresolved. The contribution here is a collection of fully proved special cases and an explicit target-specific clustered bound, not a claimed disproof or complete solution.