```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I give constructive strong-immersion proofs for clique blow-ups of C5 and all their iterated Mycielski graphs.",
  "would_publish": false,
  "caveats": "This does not resolve arbitrary graphs; novelty of these special-case and closure results is not claimed."
}
```

## 1. Scope and conventions

I use the standard intended split operation: the edges \(uv,vw\) are replaced by \(uw\). The occurrence of \(vw\) as the new edge in the supplied discussion appears to be a typo.

An immersion of \(K_t\) consists of distinct **branch vertices** and pairwise edge-disjoint paths joining every pair of branch vertices. It is **strong** if no branch vertex is internal to one of these paths. All the special-case constructions below are strong immersions.

I work with finite simple graphs. For the conjecture, parallel edges can be discarded without changing the chromatic number, so proving it for simple graphs suffices for loopless multigraphs.

Write \(\iota_s(G)\) for the largest order of a complete graph strongly immersed in \(G\). I prove:

1. Every graph obtained by replacing the vertices of \(C_5\) by nonempty cliques satisfies
   \[
   \chi(G)\le \iota_s(G).
   \]
2. The property \(\chi(G)\le\iota_s(G)\) is preserved by the Mycielski construction. In fact,
   \[
   \iota_s(\mu(G))\ge \iota_s(G)+1
   \]
   for every nonempty finite simple graph \(G\).
3. These yield explicit families of unbounded chromatic number. The starting family includes graphs for which the analogous subdivision statement fails.

These are self-contained partial results, not asserted to be new.

---

## 2. Clique blow-ups of a five-cycle

For positive integers \(a_0,\ldots,a_4\), let
\[
H=H(a_0,\ldots,a_4)
\]
have disjoint cliques \(V_0,\ldots,V_4\), where \(|V_i|=a_i\). Put all edges between \(V_i\) and \(V_{i+1}\), with indices modulo \(5\), and no edges between other distinct parts.

Set
\[
N=\sum_{i=0}^4a_i,
\qquad
\omega=\max_i(a_i+a_{i+1}).
\]
The latter is precisely \(\omega(H)\).

### Theorem 1
For every such \(H\),
\[
\boxed{\quad
\chi(H)\le \max\{\omega,N-\omega\}\le \iota_s(H).
\quad}
\]

### 2.1. The coloring bound

Relabel cyclically so that \(V_0\cup V_1\) is a clique of order \(\omega\). Write
\[
(a,b,c,d,e)=(a_0,a_1,a_2,a_3,a_4),
\qquad q=a+b=\omega,
\qquad r=c+d+e.
\]
Maximality of \(q\) gives
\[
c\le a,\qquad e\le b.
\]

Consider a bipartite graph with sides
\[
Q=V_0\cup V_1,\qquad R=V_2\cup V_3\cup V_4,
\]
where two vertices are adjacent exactly when they are **nonadjacent in \(H\)**. Thus:

- vertices in \(V_2\) have neighborhood \(V_0\);
- vertices in \(V_4\) have neighborhood \(V_1\);
- vertices in \(V_3\) have neighborhood \(Q\).

If \(r\le q\), Hall’s condition holds for a matching saturating \(R\): the only restricted neighborhoods are \(V_0\) and \(V_1\), and the necessary inequalities are \(c\le a\), \(e\le b\), and \(r\le q\). Color each matched pair with one color and each unmatched vertex of \(Q\) with its own color. This uses \(q\) colors.

If \(r\ge q\), Hall’s condition holds for a matching saturating \(Q\), because
\[
c+d=r-e\ge q-e\ge a,
\qquad
d+e=r-c\ge q-c\ge b,
\]
and \(r\ge q\). Coloring matched pairs and unmatched vertices of \(R\) now uses \(r\) colors.

Consequently,
\[
\chi(H)\le \max\{q,r\}=\max\{\omega,N-\omega\}.
\]

### 2.2. The immersion construction

For this construction, relabel so that
\[
a_0=\max_i a_i.
\]
Put
\[
p=\min(a_4,a_2),\qquad r=\min(a_1,a_3).
\]
Choose vertices
\[
X=\{x_1,\ldots,x_p\}\subseteq V_4,\qquad
Y=\{y_1,\ldots,y_r\}\subseteq V_1,
\]
and relay vertices
\[
U=\{u_1,\ldots,u_p\}\subseteq V_2,\qquad
W=\{w_1,\ldots,w_r\}\subseteq V_3.
\]

Take \(V_0\cup X\cup Y\) as the branch set. Every pair of branch vertices is adjacent except pairs \(x_i,y_j\). For those pairs use
\[
x_i\,w_j\,u_i\,y_j.
\]

These paths are edge-disjoint:

- edges \(x_iw_j\) are distinct for distinct \((i,j)\);
- edges \(w_ju_i\) are distinct for distinct \((i,j)\);
- edges \(u_iy_j\) are distinct for distinct \((i,j)\);
- the three types lie between different pairs of parts.

Their internal vertices lie outside the branch set. Together with the direct edges for all other branch pairs, they give a strong immersion of
\[
K_f,\qquad f=a_0+\min(a_4,a_2)+\min(a_1,a_3).
\]

Moreover,
\[
N-f
=\max(a_1,a_3)+\max(a_2,a_4).
\]
Expanding the two maxima gives one of
\[
a_1+a_2,\quad a_3+a_2,\quad a_3+a_4,\quad a_1+a_4.
\]
The first three are at most \(\omega\). The last is also at most \(\omega\), since
\[
a_1+a_4\le a_1+a_0\le\omega.
\]
Therefore \(f\ge N-\omega\).

Since \(H\) also contains a clique of order \(\omega\),
\[
\iota_s(H)\ge \max\{\omega,f\}
\ge\max\{\omega,N-\omega\}.
\]
This proves Theorem 1. \(\square\)

---

## 3. An exact subfamily where subdivisions are insufficient

Let
\[
H_s=C_5[K_s]=H(s,s,s,s,s).
\]
For this family the relevant parameters can be determined exactly:
\[
\boxed{
\chi(H_s)=\left\lceil\frac{5s}{2}\right\rceil,
\qquad
\iota_s(H_s)=\iota(H_s)=3s,
\qquad
\tau(H_s)=2s+1,
}
\]
where \(\iota\) denotes the weak clique-immersion number and \(\tau\) the largest order of a subdivided complete graph.

### Chromatic number

Every independent set has size at most two, giving
\[
\chi(H_s)\ge\left\lceil\frac{5s}{2}\right\rceil.
\]

For \(s=2h\), assign \(h\) distinct colors to each of the five nonadjacent pairs of parts, using each such color once in each part of its pair. Every part belongs to two such pairs, so this colors all \(2h\) vertices per part with \(5h\) colors.

For \(s=2h+1\), do the same on \(2h\) vertices per part and color the remaining induced \(C_5\) with three additional colors. This attains the lower bound.

### Immersion number

Theorem 1 gives a strong \(K_{3s}\)-immersion. Every vertex of \(H_s\) has degree \(3s-1\), while a branch vertex of any \(K_t\)-immersion requires at least \(t-1\) incident edges. Hence no weak immersion has order greater than \(3s\).

### Subdivision number

First, \(H_s\) contains a subdivision of \(K_{2s+1}\). Take all vertices of \(V_0\cup V_1\) and one vertex \(z\in V_2\) as branches. The only missing adjacencies are between \(z\) and \(V_0\). Route these through \(V_3,V_4\), using one distinct vertex from each of those two parts for each path.

For the upper bound, use the following elementary separator observation. If a subdivision of \(K_k\) has branch vertices on both sides of a vertex separator \(S\), let:

- \(p,q\ge1\) be the numbers of branches on its two sides;
- \(c\) be the number of branches in \(S\).

The \(pq\) paths between branches on opposite sides must use distinct internal vertices of \(S\). Therefore
\[
|S|\ge c+pq
=k-1+(p-1)(q-1)\ge k-1.
\]

Suppose now that \(H_s\) contained a subdivision of \(K_k\) with \(k\ge2s+2\). If branches occur in two nonadjacent parts \(V_i,V_j\), deleting
\[
V_{i-1}\cup V_{i+1}
\]
separates those branches. This separator has size \(2s<k-1\), a contradiction.

Thus all branch-bearing parts must be pairwise adjacent on \(C_5\). There are at most two such parts, containing at most \(2s\) vertices—again a contradiction. Hence \(\tau(H_s)=2s+1\).

In particular,
\[
H_3=C_5[K_3]
\]
is an explicit \(15\)-vertex graph with
\[
\chi(H_3)=8,\qquad \iota_s(H_3)=9,\qquad \tau(H_3)=7.
\]
Thus this special case genuinely uses immersion rather than proving a subdivision statement.

---

## 4. Mycielski closure

The Mycielski graph \(\mu(G)\) has:

- the original vertices and edges of \(G\);
- one shadow \(v'\) for each \(v\in V(G)\);
- edges \(uv'\) and \(vu'\) for every \(uv\in E(G)\);
- a new apex \(z\), adjacent to every shadow.

There are no edges between shadows.

The main technical point is that an arbitrary immersion model need not initially have branch vertices with distinct neighbors. The following lemma repairs precisely that issue.

### Lemma 2: distinct-neighbor normal form
If a finite simple graph \(G\) strongly immerses \(K_t\), where \(t\ge2\), it has such a model with branch set \(B\) admitting an injective map
\[
f:B\longrightarrow V(G),
\qquad bf(b)\in E(G)\quad(b\in B).
\]
The images need not lie outside \(B\).

#### Proof

Start with a strong immersion model having branch set \(B\). Each \(b\in B\) has degree at least \(t-1\).

Apply Hall’s theorem to the bipartite graph between a left copy of \(B\) and a right copy of \(V(G)\), with adjacency inherited from \(G\). If Hall’s condition holds, we are done.

Otherwise some nonempty \(S\subseteq B\) satisfies
\[
|N_G(S)|<|S|.
\]
Since every vertex of \(S\) has at least \(t-1\) neighbors,
\[
t-1\le |N_G(S)|<|S|\le t.
\]
Thus
\[
S=B,\qquad |N_G(B)|=t-1.
\]
Writing \(R=N_G(B)\), every \(b\in B\) has neighborhood exactly \(R\). Also \(B\cap R=\varnothing\), since otherwise a vertex in the intersection would have to be its own neighbor.

Consequently, \(G\) contains a \(K_{t,t-1}\) with sides \(B,R\).

Put \(m=t-1\), and label
\[
B=\{a_*\}\cup\{a_0,\ldots,a_{m-1}\},
\qquad R=\{r_0,\ldots,r_{m-1}\}.
\]
Construct a new model with branches \(\{a_*\}\cup R\):

- use the direct edge \(a_*r_i\);
- for \(i<j\), use
  \[
  r_i\,a_{\,i+j\pmod m}\,r_j.
  \]

At a fixed \(r_i\), different \(j\)'s give different relay vertices, so these paths are edge-disjoint. All their internal vertices lie outside the new branch set.

Finally, define
\[
f(a_*)=r_0,\qquad f(r_i)=a_i.
\]
This is injective and assigns a neighbor to every branch vertex. The construction also covers \(m=1\), when there are no pairs \(i<j\). \(\square\)

### Theorem 3
For every nonempty finite simple graph \(G\),
\[
\boxed{\iota_s(\mu(G))\ge \iota_s(G)+1.}
\]

#### Proof

Let \(G\) strongly immerse \(K_t\).

If \(t=1\), the apex-shadow edge in \(\mu(G)\) gives a strong \(K_2\)-immersion.

For \(t\ge2\), choose the model and injective neighbor map \(f\) from Lemma 2. Retain the old model on the original vertices, add \(z\) as a new branch, and for each old branch \(b\) use
\[
b\,f(b)'\,z.
\]

Injectivity of \(f\) makes these new paths internally vertex-disjoint. They use only edges incident with shadows, whereas the old model uses only original edges. Hence all paths are edge-disjoint, and no branch is internal to a path. \(\square\)

The same argument also proves the corresponding statement for weak immersions.

### Chromatic number

For completeness,
\[
\chi(\mu(G))=\chi(G)+1.
\]
The upper bound colors each shadow like its original and gives the apex a new color.

Conversely, suppose \(\mu(G)\) has a proper \(q\)-coloring and the apex has color \(q\). No shadow has color \(q\). Recolor every original vertex of color \(q\) with the color of its shadow, leaving the other original colors unchanged. This properly colors \(G\) with \(q-1\) colors: on an edge with one recolored endpoint, the required inequality follows from the corresponding shadow-original edge.

Thus Theorem 3 proves closure of the conjectured inequality under \(\mu\).

---

## 5. Consequences and the remaining gap

Combining Theorems 1 and 3, every graph
\[
\mu^r\!\left(H(a_0,\ldots,a_4)\right),
\qquad r\ge0,\quad a_i\ge1,
\]
strongly immerses a complete graph of order equal to its chromatic number.

For the uniform family,
\[
\chi\!\left(\mu^r(H_s)\right)
=r+\left\lceil\frac{5s}{2}\right\rceil,
\qquad
\iota_s\!\left(\mu^r(H_s)\right)\ge r+3s.
\]
Its order is
\[
2^r(5s+1)-1.
\]
For example, starting with \(H_3\) gives graphs of chromatic number \(8+r\) with strong \(K_{9+r}\)-immersions.

**The unresolved step is entirely general:** nothing above shows that an arbitrary chromatic-critical graph is a clique blow-up of \(C_5\), a Mycielski graph, or reducible to one by immersion-preserving operations. The constructions therefore establish a precise special class and a closure theorem, but neither a proof nor a counterexample to the full conjecture.