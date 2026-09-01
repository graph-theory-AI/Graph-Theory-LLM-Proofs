```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conclusion holds for every target graph in bounded-biclique host classes, and any bounded-clique counterexample must have arbitrarily large induced bicliques in each sufficiently high-chromatic induced subgraph.",
  "would_publish": false,
  "caveats": "The key input is a known Kühn–Osthus theorem; unrestricted biclique-rich bounded-clique graphs remain untreated."
}
```

# Mathematical writeup

## 1. Statement and notation

All graphs below are finite and simple. For a graph \(H\) and integer \(\ell\ge 0\), let \(H^{[\ell]}\) be the graph obtained by subdividing every edge of \(H\) exactly \(\ell\) times.

An induced subdivision of \(H^{[\ell]}\) is automatically an induced \((\ge \ell)\)-subdivision of \(H\): concatenate the paths replacing the \(\ell+1\) edges corresponding to each original edge of \(H\).

I do not resolve the unrestricted forest-of-lanterns conjecture. I prove a biclique-free special case, derive a necessary structural property of every possible counterexample, and rule out the ordinary shift graphs as a natural counterexample family.

---

## 2. Established input: the Kühn–Osthus theorem

I use the following published theorem of Kühn and Osthus, from *Induced subdivisions in \(K_{s,s}\)-free graphs of large average degree*.

**Kühn–Osthus theorem.**  
For every finite graph \(F\) and integer \(s\ge 2\), there exists \(d=d(F,s)\) such that every graph of average degree at least \(d\) contains either

1. \(K_{s,s}\) as a not necessarily induced subgraph, or
2. an induced subdivision of \(F\).

This is a theorem, not an additional conjectural assumption.

---

## 3. Pervasiveness in bounded-biclique classes

### Theorem 3.1

For every finite graph \(H\) and integers \(\ell\ge 0\), \(s\ge 2\), there exists \(c=c(H,\ell,s)\) such that every \(K_{s,s}\)-subgraph-free graph \(G\) with
\[
\chi(G)>c
\]
contains an induced \((\ge \ell)\)-subdivision of \(H\).

In particular, no bound on \(\omega(G)\) is needed.

### Proof

Put \(F=H^{[\ell]}\), and let \(d=d(F,s)\) be supplied by the Kühn–Osthus theorem. Set
\[
c=\lceil d\rceil+1.
\]

Suppose that \(G\) is \(K_{s,s}\)-subgraph-free and \(\chi(G)>c\). Let \(k=\chi(G)\), and choose an induced subgraph \(J\subseteq G\) minimal subject to \(\chi(J)=k\). Then \(J\) is vertex-critical, so
\[
\delta(J)\ge k-1.
\]
Indeed, if some \(v\in V(J)\) had degree at most \(k-2\), a \((k-1)\)-coloring of \(J-v\) could be extended to \(v\).

Consequently,
\[
\overline d(J)\ge k-1>d.
\]
The graph \(J\) remains \(K_{s,s}\)-subgraph-free. The Kühn–Osthus theorem therefore gives an induced subdivision of \(F\) in \(J\). Since \(J\) is an induced subgraph of \(G\), this subdivision is induced in \(G\) as well. Interpreting it as a subdivision of \(H\), every original edge of \(H\) has at least \(\ell\) subdivision vertices. ∎

### Consequences

1. **Every graph is pervasive in any class with uniformly bounded biclique number.**  
   If a class excludes some fixed \(K_{s,s}\) as a subgraph, Theorem 3.1 applies to every target \(H\), not merely forests of lanterns.

2. **The conclusion holds for hosts of girth at least five.**  
   Such graphs contain no \(K_{2,2}\) subgraph, so one may take \(s=2\).

3. **This is not subsumed by the controlled-class result in the source paper.**  
   For every fixed radius \(\rho\), there are graphs of arbitrarily large chromatic number and girth greater than \(2\rho+1\). Every \(\rho\)-ball in such a graph is a forest and hence has chromatic number at most two. Thus the class of graphs of girth at least five is not \(\rho\)-controlled for any fixed \(\rho\).

---

## 4. A biclique-or-target dichotomy

The preceding argument yields a useful necessary condition for any counterexample.

### Theorem 4.1

Fix a finite graph \(H\), integers \(\ell\ge0\), \(\nu\ge2\), and \(t\ge1\). There exists \(C=C(H,\ell,\nu,t)\) such that every graph \(G\) satisfying
\[
\omega(G)\le \nu,\qquad \chi(G)>C
\]
contains either

- an induced \((\ge\ell)\)-subdivision of \(H\), or
- an induced \(K_{t,t}\).

### Proof

Let
\[
s=R(\nu,t),
\]
where \(R(\nu,t)\) is the ordinary Ramsey number, and put \(F=H^{[\ell]}\). Apply the same critical-subgraph argument with the Kühn–Osthus threshold \(d(F,s)\).

If the resulting critical induced subgraph contains an induced subdivision of \(F\), the first outcome holds. Otherwise it contains a \(K_{s,s}\) as a subgraph, with sides \(A,B\).

Since every vertex of \(B\) is complete to \(A\), the set \(A\) cannot contain a clique of size \(\nu\): such a clique together with any vertex of \(B\) would give a \(K_{\nu+1}\). Thus
\[
\omega(G[A])\le \nu-1.
\]
Since \(|A|=R(\nu,t)\), Ramsey's theorem gives a stable set \(A'\subseteq A\) of size \(t\). Similarly, \(B\) contains a stable set \(B'\) of size \(t\). All edges between \(A'\) and \(B'\) are present, so
\[
G[A'\cup B']\cong K_{t,t}.
\]
∎

### Necessary structure of a counterexample

Suppose the conjecture fails for some \(H,\nu,\ell\), witnessed by graphs \(G_i\) with
\[
\omega(G_i)\le\nu,\qquad \chi(G_i)\longrightarrow\infty,
\]
and with no induced \((\ge\ell)\)-subdivision of \(H\). Then, for every fixed \(t\), all sufficiently high-chromatic \(G_i\) contain an induced \(K_{t,t}\).

More strongly, there is a constant \(C_t\) such that every induced subgraph \(J\subseteq G_i\) with \(\chi(J)>C_t\) contains an induced \(K_{t,t}\). This follows because \(J\) also avoids the target subdivision and has clique number at most \(\nu\).

Thus a counterexample cannot come from:

- bounded-codegree constructions;
- \(K_{s,s}\)-subgraph-free constructions;
- high-girth constructions.

It must exploit recursively arranged large bicliques. This is a substantial obstacle: an induced \(K_{t,t}\) itself has chromatic number two and generally does not contain a prescribed lantern subdivision, so the dichotomy does not finish the conjecture.

---

## 5. The ordinary shift graphs are not counterexamples

Since shift graphs are triangle-free, have unbounded chromatic number, and contain large induced bicliques, they are a natural family to test.

Let \(S_n\) have vertex set
\[
\{(i,j):1\le i<j\le n\},
\]
where \((i,j)\) and \((k,l)\) are adjacent exactly when \(j=k\) or \(l=i\).

### Basic properties

The graphs \(S_n\) are triangle-free. Orient each edge as
\[
(i,j)\longrightarrow (j,k)\qquad(i<j<k).
\]
This orientation is acyclic. A source in an oriented triangle would have two out-neighbors \((j,k)\) and \((j,l)\), but these two vertices are nonadjacent.

They have unbounded chromatic number. If \(\gamma\) is a proper coloring with \(r\) colors, define
\[
X_i=\{\gamma(i,j):j>i\}.
\]
For \(i<j\), the color \(\gamma(i,j)\) belongs to \(X_i\) but not to \(X_j\), since any \((j,k)\) of the same color would be adjacent to \((i,j)\). Hence the \(X_i\) are all distinct, so
\[
n\le 2^r,\qquad \chi(S_n)\ge \lceil\log_2 n\rceil.
\]

Nevertheless, they contain every prescribed long subdivision.

### Proposition 5.1

For every finite graph \(H\) and every \(\ell\ge0\), there exists \(N=N(H,\ell)\) such that \(S_N\), and hence every \(S_n\) with \(n\ge N\), contains an induced \((\ge\ell)\)-subdivision of \(H\).

### Proof

Choose
\[
q=\max\left\{1,\left\lceil\frac{\ell-1}{2}\right\rceil\right\},
\]
so \(2q+1\ge\ell\).

Construct a directed acyclic graph \(D\) as follows.

- For every \(v\in V(H)\), introduce vertices \(a_v,b_v\) and the arc
  \[
  a_v\to b_v.
  \]
- For every edge \(e=uv\), introduce vertices \(d_e,f_e\) and the arc
  \[
  d_e\to f_e.
  \]
- For each incidence \(v\in e\), add a directed path of length \(q\) from \(b_v\) to \(d_e\), with all its internal vertices private to that incidence.

All arcs point through successive layers, so \(D\) is acyclic.

Define the arc graph \(A(D)\) to have one vertex for each arc of \(D\), with two arcs adjacent when the head of one is the tail of the other.

For each \(v\in V(H)\), use the arc \(a_v\to b_v\) as the branch vertex representing \(v\). For an edge \(e=uv\), the corresponding path in \(A(D)\) consists of:

1. the branch arc \(a_u\to b_u\);
2. the \(q\) arcs on the \(u\)-to-\(d_e\) incidence path;
3. the central arc \(d_e\to f_e\);
4. the \(q\) arcs on the \(v\)-to-\(d_e\) incidence path, in reverse order;
5. the branch arc \(a_v\to b_v\).

This path has exactly \(2q+1\) internal vertices.

There are no unwanted adjacencies. At each \(b_v\), exactly one arc enters and the first arc of every incident path leaves, producing precisely the required star at the branch vertex. At each \(d_e\), two arcs enter and the central arc leaves, producing precisely the two required path adjacencies. Every other internal vertex has one entering and one leaving arc. Hence
\[
A(D)
\]
is exactly the uniform \((2q+1)\)-subdivision of \(H\).

Finally, choose a topological ordering of \(V(D)\) and identify its vertices with \(1,\dots,N\). Each arc \(x\to y\) of \(D\) then corresponds to the shift-graph vertex \((x,y)\). Two selected vertices are adjacent in \(S_N\) exactly when the corresponding arcs are consecutive in \(D\). Therefore \(A(D)\) is an induced subgraph of \(S_N\).

One may take explicitly
\[
N=2|V(H)|+2q|E(H)|.
\]
Thus the full shift-graph sequence cannot disprove the conjecture. ∎

---

## 6. Remaining gap

The unrestricted problem is concentrated in bounded-clique graphs with arbitrarily large induced bicliques. The Kühn–Osthus theorem gives no information about how such a biclique is attached to the high-chromatic part of the graph. In particular:

- its two sides may both have very small chromatic number;
- repeatedly finding bicliques need not produce induced paths linking them in the pattern required by a lantern;
- arbitrary attachments create chords that can destroy a proposed induced subdivision.

The shift-graph construction shows that biclique richness alone is not an obstruction: those graphs contain every fixed long subdivision. What is missing is a structural theorem for all biclique-rich, bounded-clique graphs, or an explicit recursively constructed family arranging its bicliques so as to exclude one particular forest of lanterns.

Accordingly, no proof or counterexample to the full conjecture is claimed.