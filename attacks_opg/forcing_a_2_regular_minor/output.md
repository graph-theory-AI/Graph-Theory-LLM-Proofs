```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The stated conjecture was proved by Csóka, Lo, Norin, Wu, and Yepremyan in their 2017 paper, The extremal function for disconnected minors.",
  "would_publish": false,
  "caveats": "This identifies and explains the published resolution; it is not an independent reproof of its main theorem."
}
```

## 1. Statement and published resolution

Work with finite simple undirected graphs. A nonempty 2-regular graph has the form
\[
H=C_{\ell_1}\,\dot\cup\cdots\dot\cup C_{\ell_r},
\qquad
\ell_i\ge 3,\qquad
t=\sum_{i=1}^r\ell_i.
\]

The conjecture in the question is already a theorem. The relevant reference is:

> Endre Csóka, Irene Lo, Sergey Norin, Hehui Wu, and Liana Yepremyan,  
> **The extremal function for disconnected minors**,  
> *Journal of Combinatorial Theory, Series B* **126** (2017), 162–174.  
> DOI: **10.1016/j.jctb.2017.04.005**; arXiv: **1509.01185**.

Their published resolution gives, in the form needed here:

**Theorem (Csóka–Lo–Norin–Wu–Yepremyan).**  
For every 2-regular graph \(H\) on \(t\) vertices, every nonempty graph \(G\) with
\[
\frac{2|E(G)|}{|V(G)|}\ge \frac43t-2
\]
contains \(H\) as a minor.

Thus the catalog’s “solved” designation is the appropriate one. The conclusion is exact, including the stated threshold; it is not merely an asymptotic \( (\frac43+o(1))t \) result.

I invoke this published theorem rather than claim a new proof. Below are self-contained explanations of its cycle-packing interpretation and of the sharpness example.

## 2. Equivalent cycle-packing formulation

For the above graph \(H\), the following are equivalent:

1. \(G\) contains \(H\) as a minor.
2. \(G\) contains pairwise vertex-disjoint cycles \(Q_1,\ldots,Q_r\) satisfying
   \[
   |V(Q_i)|\ge \ell_i \qquad (1\le i\le r).
   \]

**Proof.** If the cycles exist, delete unwanted vertices and edges, then contract edges of each \(Q_i\) until it has exactly \(\ell_i\) vertices. This produces \(H\).

Conversely, take a minor model of \(H\). For the component \(C_{\ell_i}\), denote its branch sets in cyclic order by
\[
B_{i,1},\ldots,B_{i,\ell_i}.
\]
Choose one edge between each pair of consecutive branch sets. Within each branch set, connect the endpoints of its two chosen incident edges by a simple path; that path may have length zero. These paths and chosen edges form a cycle visiting all \(\ell_i\) branch sets, so its length is at least \(\ell_i\). Models of different components have disjoint branch sets, hence the resulting cycles are vertex-disjoint. \(\square\)

Consequently, the theorem guarantees disjoint cycles meeting any prescribed list of minimum lengths whose sum is \(t\).

## 3. Sharpness when \(t\) is divisible by three

Let
\[
t=3k,\qquad H=kC_3,
\]
and consider
\[
G_N=K_{2k-1,N}.
\]
Write \(A\) for the bipartition class of size \(2k-1\).

Every cycle in a simple bipartite graph has length at least four and uses at least two vertices from each bipartition class. Thus \(k\) vertex-disjoint cycles in \(G_N\) would require at least \(2k\) distinct vertices of \(A\), which is impossible. By the equivalence above, \(G_N\) has no \(kC_3\)-minor.

Nevertheless,
\[
\begin{aligned}
\overline d(G_N)
&=\frac{2(2k-1)N}{N+2k-1}\\
&=4k-2-\frac{2(2k-1)^2}{N+2k-1}\\
&\longrightarrow 4k-2
=\frac43t-2.
\end{aligned}
\]
Therefore, for every \(\varepsilon>0\), some \(G_N\) has no \(H\)-minor despite satisfying
\[
\overline d(G_N)>\frac43t-2-\varepsilon.
\]

This proves that the threshold cannot be lowered when \(t=3k\). It does **not** establish optimality for every individual 2-regular \(H\), or for every value of \(t\). Also, the examples approach the threshold strictly from below, so they do not contradict the theorem’s “at least” formulation.

## 4. Scope of this answer

The main forcing assertion is supplied by the cited published theorem; its nontrivial proof is not reproduced here. The minor/cycle-packing equivalence and sharpness argument above are proved directly. Accordingly, this is an explanation of an existing resolution, not a new research proof or a reduction to another conjecture.