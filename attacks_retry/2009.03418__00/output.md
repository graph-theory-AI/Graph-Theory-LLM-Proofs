```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For the intended even-order conjecture, I prove the cases n=6,8, derive unconditional general lower bounds, and establish the sharp lower bound for a natural class of drawings.",
  "would_publish": false,
  "caveats": "The general even-order conjecture remains unresolved here; novelty and best-known status of these partial results have not been checked."
}
```

# Partial results for the even-order conjecture

## 1. Scope and conclusions

I use the intended scope identified in the supplied referee report:
\[
n=2k,\qquad k\ge 3,\qquad 0\le t\le k.
\]
Thus I discard the previous attempt’s claim of a disproof. Its odd-order examples do not refute this version. Odd-order graphs below are used only as auxiliary subgraphs, and their required lower bounds are proved.

Write
\[
C_{n,t}:=\operatorname{cr}(M_{n,t})
\]
and
\[
U_{k,t}
:=H(2k)-t\binom{k-1}{2}
=\frac{(k-1)(k-2)}4\bigl(k(k-1)-2t\bigr).
\]
The construction supplied in the question establishes
\[
C_{2k,t}\le U_{k,t}.
\tag{1}
\]
I take that established upper bound as an input.

The results proved below are:

1. **All cases with \(n=6,8\):**
   \[
   C_{6,t}=3-t\quad(0\le t\le3),
   \qquad
   C_{8,t}=18-3t\quad(0\le t\le4).
   \tag{2}
   \]

2. **An unconditional matching-sensitive lower bound:** for \(n\ge8\),
   \[
   C_{n,t}\ge
   \left\lceil
   \frac9{35}\binom n4
   -\frac{t(n-2)(n-3)}{10}
   \right\rceil .
   \tag{3}
   \]
   Two lower-bound recurrences give additional improvements, including
   \[
   C_{10,5}\ge27,\qquad C_{12,6}\ge77.
   \tag{4}
   \]

3. **The conjectured lower bound for a topological drawing class:** it holds whenever, after deleting a suitable perfect matching extending the missing matching, every crossing has endpoints in four distinct matching pairs. No geodesic assumption is needed.

These are self-contained partial results, not a claim of new literature progress.

---

## 2. Two general lower-bound recurrences

We use good drawings: edges are simple arcs, adjacent edges do not cross, independent edges cross at most once, and no three edges cross at one point. A crossing-minimal drawing may be assumed good.

### 2.1. Euler’s bound and vertex deletion

For every simple graph with \(n\ge3\) vertices and \(m\) edges,
\[
\operatorname{cr}(G)\ge m-3n+6.
\tag{5}
\]
Indeed, deleting at most one edge for each crossing leaves a planar graph.

We will also use the following consequence:

> **Euler equality observation.** If a drawing has exactly \(m-3n+6\) crossings, every edge is crossed at most once.

If an edge had \(r\ge2\) crossings, deleting it would leave a drawing with
\[
m-1\text{ edges and at most }m-3n+6-r<m-1-3n+6
\]
crossings, contradicting (5).

Let \(D\) be a good drawing of \(M_{n,t}\), with \(c\) crossings. Each crossing survives exactly \(n-4\) vertex deletions. Deleting an endpoint of a missing edge leaves \(M_{n-1,t-1}\), while deleting one of the other vertices leaves \(M_{n-1,t}\). Hence
\[
\boxed{
C_{n,t}\ge
\left\lceil
\frac{2tC_{n-1,t-1}+(n-2t)C_{n-1,t}}{n-4}
\right\rceil .
}
\tag{D}
\]
Terms with zero coefficient are omitted; thus no out-of-range crossing number is needed when \(n=2t\).

### 2.2. Completing one missing edge

Here is a second recurrence, obtained by routing a missing edge along a two-edge path.

For a good drawing \(D\), let \(q_D(e)\) be the number of crossings on edge \(e\), and put
\[
R_D(v):=\sum_{e\ni v}q_D(e).
\]
Because adjacent edges do not cross,
\[
R_D(v)=c(D)-c(D-v).
\tag{6}
\]

Suppose \(uv\) is a missing edge of \(M_{n,t}\). Every other vertex \(w\) is adjacent to both \(u\) and \(v\). Draw \(uv\) close to the path \(u w v\). Along its two edge segments, this introduces at most
\[
q_D(uw)+q_D(vw)
\]
crossings.

Inside a sufficiently small disk about \(w\), the new arc can use either of the two sectors between \(wu\) and \(wv\). The numbers of other incident edges in these sectors sum to \(\deg(w)-2\). Choosing the smaller sector costs at most
\[
\left\lfloor\frac{\deg(w)-2}{2}\right\rfloor
\]
additional crossings. Thus \(uv\) can be inserted at a cost at most
\[
q_D(uw)+q_D(vw)
+\left\lfloor\frac{\deg(w)-2}{2}\right\rfloor .
\tag{7}
\]
Any nongood features of the resulting drawing can subsequently be removed without increasing its crossing count.

Among the \(n-2\) choices of \(w\), exactly \(2(t-1)\) vertices have degree \(n-2\), and \(n-2t\) have degree \(n-1\). Define
\[
s_{n,t}:=
2(t-1)\left\lfloor\frac{n-4}{2}\right\rfloor
+(n-2t)\left\lfloor\frac{n-3}{2}\right\rfloor .
\tag{8}
\]
Averaging (7), some insertion has cost at most
\[
\left\lfloor
\frac{R_D(u)+R_D(v)+s_{n,t}}{n-2}
\right\rfloor .
\tag{9}
\]

Take \(D\) crossing-minimal, with \(c=C_{n,t}\), and let
\[
A=C_{n-1,t-1}.
\]
Both \(D-u\) and \(D-v\) draw \(M_{n-1,t-1}\), so (6) gives
\[
R_D(u),R_D(v)\le c-A.
\]
Completing \(uv\) produces \(M_{n,t-1}\). Consequently,
\[
C_{n,t-1}
\le c+\frac{2(c-A)+s_{n,t}}{n-2},
\]
and therefore
\[
\boxed{
C_{n,t}\ge
\left\lceil
\frac{(n-2)C_{n,t-1}+2C_{n-1,t-1}-s_{n,t}}{n}
\right\rceil .
}
\tag{I}
\]

For the intended even-order problem, \(n=2k\), this simplifies because
\[
s_{2k,t}=(2k-2)(k-2),
\]
independently of \(t\).

Both recurrences are unconditional inequalities involving actual crossing numbers. Their applications below use only lower bounds proved here.

---

## 3. Exact verification for \(n=6,8\)

### 3.1. A fact about extremal 1-planar drawings

We need the following elementary lemma.

> **Lemma.** A simple graph on \(n\ge3\) vertices having a good drawing in which every edge is crossed at most once has at most \(4n-8\) edges. If it has exactly \(4n-8\) edges, every vertex has even degree.

**Proof.** Let the drawing have \(c\) crossings and \(m\) edges. Its planarization has \(n+c\) vertices and \(m+2c\) edges, so
\[
m\le3n+c-6.
\tag{10}
\]
Retain only the segments between crossing points and original vertices. They form a simple planar bipartite graph with \(n+c\) vertices and \(4c\) edges. Thus
\[
4c\le2(n+c)-4,
\]
giving \(c\le n-2\). Together with (10), this gives \(m\le4n-8\).

If \(m=4n-8\), equality holds throughout: \(c=n-2\), and the planarization is a triangulation with \(4c\) faces. No planarization edge joins two crossing vertices, because every original edge has at most one crossing. Each crossing vertex is incident with four triangular faces, and every face therefore contains exactly one crossing vertex.

Around an original vertex, its neighbors in the planarization consequently alternate between original vertices and crossing vertices. Its degree is even. ∎

### 3.2. The necessary lower bound for \(K_7\)

We also use the parity fact
\[
c(D)\equiv\binom m4\pmod2
\tag{11}
\]
for every good drawing \(D\) of \(K_m\) with \(m\) odd.

For completeness, this parity can be proved by changing edge routes one at a time. Replacing an arc \(uv\), modulo \(2\), produces a closed curve \(Z\). If \(\epsilon(x)\) denotes its mod-\(2\) winding number at another vertex \(x\), the crossing parity with an independent edge \(xy\) changes by \(\epsilon(x)+\epsilon(y)\). Summing over the complete graph on the other \(m-2\) vertices gives
\[
(m-3)\sum_x\epsilon(x)=0\pmod2.
\]
Thus the total independent-crossing parity is invariant. Evaluate it on a drawing homeomorphic to a convex straight-line drawing, which has \(\binom m4\) crossings.

Now every drawing of \(K_6\) has at least \(3\) crossings by (5). Vertex deletion in a good drawing of \(K_7\) gives
\[
3c\ge7\cdot3,
\]
so \(c\ge7\). By (11), \(c\) is odd.

Suppose \(c=7\). Since \(K_7\) has \(21>4\cdot7-8\) edges, some edge has at least two crossings. Deleting it leaves \(K_7-e\) with at most five crossings. Euler’s bound gives at least five, so this drawing attains Euler equality and is 1-planar.

But \(K_7-e\) has \(20=4\cdot7-8\) edges and has two vertices of degree \(5\), contrary to the lemma. Thus
\[
C_{7,0}\ge9.
\tag{12}
\]

### 3.3. Auxiliary seven-vertex bounds

Euler’s bound gives
\[
C_{6,t}\ge3-t,\qquad 0\le t\le3.
\tag{13}
\]
It also gives
\[
C_{7,2}\ge4,\qquad C_{7,3}\ge3.
\tag{14}
\]

For \(M_{7,1}\), deleting either endpoint of the missing edge leaves \(K_6\); the other five deletions leave \(M_{6,1}\). Hence
\[
3C_{7,1}\ge2\cdot3+5\cdot2=16,
\]
and
\[
C_{7,1}\ge6.
\tag{15}
\]

Thus the auxiliary lower bounds needed are
\[
(C_{7,0},C_{7,1},C_{7,2},C_{7,3})
\ge(9,6,4,3).
\tag{16}
\]
This rechecks, rather than merely adopts, the useful lower-bound part of the previous attempt.

### 3.4. All eight-vertex cases

Deleting vertices from \(K_8\) and using (12) gives
\[
4C_{8,0}\ge8\cdot9,
\qquad\text{so}\qquad C_{8,0}\ge18.
\tag{17}
\]

For \(n=8\), equation (8) gives \(s_{8,t}=12\). Apply recurrence (I) successively, using (16):
\[
\begin{array}{c|c|c|c}
t&C_{8,t-1}\text{ lower bound}&C_{7,t-1}\text{ lower bound}
& C_{8,t}\text{ lower bound}\\ \hline
1&18&9&\left\lceil(6\cdot18+2\cdot9-12)/8\right\rceil=15\\
2&15&6&\left\lceil(6\cdot15+2\cdot6-12)/8\right\rceil=12\\
3&12&4&\left\lceil(6\cdot12+2\cdot4-12)/8\right\rceil=9\\
4&9&3&\left\lceil(6\cdot9+2\cdot3-12)/8\right\rceil=6
\end{array}
\tag{18}
\]

The supplied upper bound (1) is \(3-t\) for \(n=6\), and \(18-3t\) for \(n=8\). Combining it with (13), (17), and (18) proves
\[
\boxed{
\begin{aligned}
(C_{6,0},C_{6,1},C_{6,2},C_{6,3})&=(3,2,1,0),\\
(C_{8,0},C_{8,1},C_{8,2},C_{8,3},C_{8,4})&=(18,15,12,9,6).
\end{aligned}}
\tag{19}
\]

---

## 4. Unconditional bounds at larger orders

### 4.1. Averaging over eight vertices

Let \(D\) be a good drawing of \(M_{n,t}\), \(n\ge8\), with \(c\) crossings. For each eight-vertex set \(S\), let \(t_S\) be the number of missing matching edges with both endpoints in \(S\). By (19),
\[
c(D[S])\ge18-3t_S.
\]

Every crossing survives in exactly \(\binom{n-4}{4}\) such subdrawings. Also,
\[
\sum_{|S|=8}t_S=t\binom{n-2}{6}.
\]
Consequently,
\[
\binom{n-4}{4}c
\ge18\binom n8-3t\binom{n-2}{6}.
\]
Using
\[
\frac{\binom n8}{\binom{n-4}{4}}=\frac1{70}\binom n4,
\qquad
\frac{\binom{n-2}{6}}{\binom{n-4}{4}}
=\frac{(n-2)(n-3)}{30},
\]
we obtain
\[
\boxed{
C_{n,t}\ge
\left\lceil
\frac9{35}\binom n4
-\frac{t(n-2)(n-3)}{10}
\right\rceil .
}
\tag{20}
\]

In particular, for a perfect missing matching and \(k\ge4\),
\[
C_{2k,k}\ge
\left\lceil
\frac{k(k-1)(2k-3)(6k-17)}{70}
\right\rceil .
\tag{21}
\]

### 4.2. Integer recurrence improvements

The recurrences retain rounding information lost in a single averaging step. Repeated application of (D) to the exact eight-vertex values gives
\[
\begin{aligned}
(C_{9,2},C_{9,3},C_{9,4})&\ge(24,20,16),\\
(C_{10,3},C_{10,4},C_{10,5})&\ge(38,32,27).
\end{aligned}
\tag{22}
\]
For example,
\[
C_{9,4}\ge
\left\lceil\frac{8\cdot9+6}{5}\right\rceil=16,
\qquad
C_{10,5}\ge
\left\lceil\frac{10\cdot16}{6}\right\rceil=27.
\]

Next,
\[
C_{11,4}\ge
\left\lceil\frac{8\cdot38+3\cdot32}{7}\right\rceil
=58.
\tag{23}
\]
For \(n=11,t=5\), equation (8) gives
\[
s_{11,5}=8\cdot3+1\cdot4=28.
\]
Recurrence (I) therefore yields
\[
C_{11,5}\ge
\left\lceil\frac{9\cdot58+2\cdot32-28}{11}\right\rceil
=51.
\tag{24}
\]
Finally,
\[
C_{12,6}\ge
\left\lceil\frac{12\cdot51}{8}\right\rceil=77.
\tag{25}
\]

Thus these arguments, together with the supplied construction, give
\[
27\le C_{10,5}\le30,
\qquad
77\le C_{12,6}\le90.
\tag{26}
\]
These intervals describe the limitations of the present argument, not a claim about the best published bounds.

---

## 5. A sharp lower bound for pair-clean drawings

The following result isolates a natural setting in which the full proposed lower bound follows by elementary counting.

### Definition

Extend the \(t\) missing edges to a perfect matching
\[
P=\{a_i b_i:1\le i\le k\}
\]
on the \(2k\) vertices, and put
\[
B:=K_{2k}-P.
\]
Thus \(M_{2k,t}\) consists of \(B\) together with \(k-t\) edges of \(P\).

Call a drawing **pair-clean with respect to \(P\)** if every crossing between two edges of \(B\) has its four endpoints in four distinct pairs of \(P\).

Equivalently, restricting the drawing of \(B\) to any three pairs gives a crossing-free drawing of \(K_{2,2,2}\).

### Theorem

Every good drawing of \(M_{2k,t}\) that is pair-clean with respect to some such \(P\) has at least
\[
U_{k,t}
=6\binom k4+(k-t)\binom{k-1}{2}
\tag{27}
\]
crossings.

**Proof.**

First count crossings between edges of \(B\). Restrict to any four pairs. The resulting graph is \(M_{8,4}\), with \(24\) edges, so even Euler’s bound alone gives at least
\[
24-(3\cdot8-6)=6
\]
crossings.

By pair-cleanness, each crossing between edges of \(B\) belongs to exactly one four-pair restriction. Therefore
\[
c(B)\ge6\binom k4.
\tag{28}
\]

Now let \(a_i b_i\) be one of the \(k-t\) present edges of \(P\). Choose two other pair indices \(j,\ell\). On these six vertices, retain the octahedral graph
\[
B[\{a_i,b_i,a_j,b_j,a_\ell,b_\ell\}]
\]
and the single added edge \(a_i b_i\).

This six-vertex graph has \(13\) edges, so it has at least one crossing by (5). The octahedral part is drawn without crossings by pair-cleanness. Hence the added edge must cross an edge of that octahedron.

Since adjacent edges do not cross, the crossed base edge has one endpoint in pair \(j\) and one in pair \(\ell\). Thus different unordered choices \(\{j,\ell\}\) require different crossings of \(a_i b_i\) with \(B\). Consequently,
\[
q_D(a_i b_i,B)\ge\binom{k-1}{2}.
\tag{29}
\]

Summing (29) over the \(k-t\) present matching edges, and allowing any crossings between those matching edges themselves, gives
\[
c(D)\ge6\binom k4+(k-t)\binom{k-1}{2}.
\]
Finally,
\[
6\binom k4+(k-t)\binom{k-1}{2}
=H(2k)-t\binom{k-1}{2}.
\]
This proves the theorem. ∎

This class includes the antipodally organized geodesic constructions motivating the question, but the proof uses no metric geometry.

---

## 6. The remaining gap

Pair-cleanness cannot simply be assumed for an arbitrary crossing-minimal drawing.

To see precisely where the counting argument fails without it, let \(x_j\) count crossings between edges of \(B\) whose endpoints meet exactly \(j\) pairs of \(P\), for \(j=2,3,4\). For \(k\ge4\), averaging over four-pair restrictions gives only
\[
x_4+(k-3)x_3+\binom{k-2}{2}x_2
\ge6\binom k4.
\tag{30}
\]
The desired quantity is \(x_2+x_3+x_4\). Crossings supported on two or three pairs are overcounted in (30).

Such crossings genuinely can occur: in a convex drawing with cyclic order
\[
a_i,b_i,a_j,b_j
\]
on four selected vertices, the base edges \(a_i a_j\) and \(b_i b_j\) cross, using only two matching pairs. Moreover, once a three-pair octahedral subdrawing already has a crossing, Euler’s bound for that octahedron plus an added matching edge no longer forces an additional crossing on the added edge.

I have not proved a crossing-nonincreasing transformation that eliminates these obstructions, nor a compensating inequality strong enough to handle them. Accordingly, the sharp drawing-class theorem is not a proof of the unrestricted conjecture.

**Conclusion:** the even-order conjecture is verified here for \(n=6,8\), and the recurrences and bounds above are rigorous partial results. No complete proof or even-order counterexample is obtained.