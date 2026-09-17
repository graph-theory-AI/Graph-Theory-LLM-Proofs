```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained list-colouring argument proves the Δ+2 bound when mad(G)<10/3 and Δ≥24, and more generally in a parameterized sparse range approaching mad(G)<11/3.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; novelty of this sparse-graph result is not claimed."
}
```

# A sparse-graph partial result

Write \(a'(G)\) for the acyclic chromatic index. The conjecture asks whether
\[
a'(G)\le \Delta(G)+2
\]
for every simple graph.

I do not prove this in general or find a counterexample. I set aside the previous prime-order factorization approach and instead obtain a local-extension argument for sparse graphs. Nothing from the previous attempt is assumed below.

The argument works for **lists**: each edge may have its own set of permitted colours. No claim of novelty or improvement over the current literature is made.

For a finite graph, put
\[
\operatorname{mad}(G)=
\max_{\substack{H\subseteq G\\V(H)\ne\varnothing}}
\frac{2|E(H)|}{|V(H)|}.
\]

## Theorem

Let \(t,D\) be integers satisfying
\[
t\ge 10,\qquad D\ge 3t-6.
\]
If \(G\) is a finite simple graph with
\[
\Delta(G)\le D,
\qquad
\operatorname{mad}(G)<\rho_t:=\frac{11t}{3(t+1)},
\]
then every assignment of lists of at least \(D+2\) colours to its edges admits a proper acyclic edge-colouring from those lists.

In particular:

1. If \(\Delta\ge24\) and \(\operatorname{mad}(G)<10/3\), then \(a'(G)\le\Delta+2\), even with arbitrary lists of size \(\Delta+2\).
2. This applies to every planar graph of girth at least five and maximum degree at least \(24\).
3. For every fixed \(\varepsilon>0\), the list version of the conjectured bound holds when
   \[
   \operatorname{mad}(G)\le \frac{11}{3}-\varepsilon
   \]
   and \(\Delta\) is sufficiently large in terms of \(\varepsilon\).

The proof follows.

# 1. A necessary inequality in a minimal counterexample

Fix \(D\) and an edge-list assignment of size \(D+2\). Suppose that a graph is not acyclically colourable from these lists, and choose an edge-minimal uncolourable subgraph \(H\), discarding isolated vertices.

Write \(d(v)=d_H(v)\). Every proper subgraph of \(H\) is colourable from its inherited lists.

First,
\[
\delta(H)\ge2.
\]
Indeed, after deleting a pendant edge, at most \(D-1\) colours are forbidden at its other endpoint, and adding the pendant edge cannot create a cycle.

We next show that every vertex \(x\) satisfies
\[
\boxed{\quad
\sum_{z\in N_H(x)}d(z)\ge D+d(x)+2.
\quad} \tag{1}
\]

Choose an edge \(xy\), and acyclically colour \(H-xy\). Let \(S_x,S_y\) be the sets of colours appearing at \(x,y\).

A colour available at both endpoints can become invalid only by creating a bichromatic cycle through \(xy\). If that cycle uses colours \(a,c\), with \(a\) assigned to \(xy\), then \(c\in S_x\cap S_y\). Let \(xz_c\) be the edge of colour \(c\) at \(x\). Necessarily \(a\) occurs at \(z_c\) on an edge other than \(xz_c\).

Consequently, the number of colours forbidden either by properness or by this necessary condition for a bichromatic cycle is at most
\[
\begin{aligned}
|S_x\cup S_y|
+\sum_{c\in S_x\cap S_y}(d(z_c)-1)
&=
d(x)+d(y)-2
+\sum_{c\in S_x\cap S_y}(d(z_c)-2)\\
&\le
d(x)+d(y)-2
+\sum_{z\in N(x)\setminus\{y\}}(d(z)-2)\\
&=
\sum_{z\in N(x)}d(z)-d(x).
\end{aligned}
\]
The inequality uses \(\delta(H)\ge2\).

If the last expression were at most \(D+1\), some colour in the list of \(xy\) would extend the colouring. This proves (1).

# 2. A reducible configuration with many degree-two neighbours

The next lemma supplies more than the preceding counting argument.

## Lemma

Let \(J\) have maximum degree at most \(D\), with edge lists of size at least \(D+2\). Suppose that a vertex \(v\) has degree \(d\), at least \(d-1\) of its neighbours have degree two, and
\[
D\ge2d-3.
\]
Then every acyclic list edge-colouring of \(J-v\) extends to \(J\).

### Proof

Name the neighbours
\[
u_1,\ldots,u_{d-1},w,
\]
where each \(u_i\) has degree two.

In the given colouring of \(J-v\), let \(b_i\) be the colour of the remaining edge at \(u_i\), and put
\[
B=\{b_1,\ldots,b_{d-1}\}.
\]
Let \(S(w)\) be the colours appearing at \(w\).

Choose
\[
c\in L(vw)\setminus S(w).
\]
There are at least three such choices, although only one is needed. We will colour \(vw\) with \(c\).

Call \(i\) **triggered** if \(b_i=c\).

For a triggered index \(i\), let \(F_i\) be the set of colours \(a\) for which the coloured graph \(J-v\) contains an alternating \((a,c)\)-path joining \(w\) to \(u_i\). These are exactly the potential obstructions to assigning \(a\) to \(vu_i\) after assigning \(c\) to \(vw\).

We have
\[
F_i\subseteq S(w),
\]
and the sets \(F_i\), over triggered indices, are pairwise disjoint. To see this, fix \(a\). In the subgraph on colours \(a,c\), the vertex \(w\) has degree one because \(c\notin S(w)\). Its component is a path and can have at most one other endpoint \(u_i\). Thus
\[
\sum_{i\text{ triggered}}|F_i|\le |S(w)|\le D-1. \tag{2}
\]

We now define sets of permitted choices for the edges \(vu_i\):

- For a non-triggered \(i\), use
  \[
  R_i=L(vu_i)\setminus(B\cup\{c\}).
  \]
- For a triggered \(i\), use
  \[
  R_i=
  \bigl((L(vu_i)\setminus B)\setminus F_i\bigr)
  \ \cup\
  \bigl(L(vu_i)\setminus(S(w)\cup\{c\})\bigr).
  \]

Every colour in every \(R_i\) differs from \(c\) and \(b_i\). For triggered \(i\), it also avoids \(F_i\).

We claim that the family \(R_1,\ldots,R_{d-1}\) has distinct representatives.

For non-triggered \(i\),
\[
|R_i|\ge D+2-d\ge d-1. \tag{3}
\]
For triggered \(i\), the second set in its definition has size at least two.

Therefore Hall’s condition is immediate for a singleton, or for any set of indices containing a non-triggered index. It remains to consider a set \(I\) of \(s\ge2\) triggered indices.

Suppose, contrary to Hall’s condition, that
\[
\left|\bigcup_{i\in I}R_i\right|\le s-1.
\]
Since
\[
|L(vu_i)\setminus B|\ge D+3-d,
\]
at least \(D+4-d-s\) colours of \(L(vu_i)\setminus B\) must belong to \(F_i\). By (2),
\[
D-1\ge s(D+4-d-s).
\]
But, for \(2\le s\le d-1\),
\[
\begin{aligned}
s(D+4-d-s)-(D-1)
={}&(s-1)(D-2d+3)\\
&+(s-2)(d-1-s)+2
\ge2,
\end{aligned}
\]
a contradiction. Hall’s theorem gives distinct choices \(a_i\in R_i\).

Colour \(vu_i\) with \(a_i\), and \(vw\) with \(c\). The colouring is proper. Any newly created bichromatic cycle must pass through \(v\).

There are two possibilities.

- **It uses \(vu_i,vu_j\).** Necessarily
  \[
  b_i=a_j,\qquad b_j=a_i.
  \]
  If one index is triggered, this would require some \(a_j=c\), which is excluded. If neither is triggered, both \(a_i,a_j\) lie outside \(B\), again impossible.

- **It uses \(vw,vu_i\).** Necessarily \(b_i=c\), so \(i\) is triggered. The rest of the cycle would be an alternating \((a_i,c)\)-path from \(w\) to \(u_i\), contradicting \(a_i\notin F_i\).

Thus the extension is acyclic. \(\square\)

Applied to the minimal counterexample \(H\), the lemma implies
\[
\boxed{\quad
D\ge2d(v)-3
\ \Longrightarrow\
v\text{ has at most }d(v)-2\text{ degree-two neighbours}.
\quad} \tag{4}
\]

# 3. Structural consequences

We now prove the theorem. Suppose that its hypotheses hold but that some list assignment is uncolourable, and take the minimal counterexample \(H\) above.

Call a vertex **big** if its degree is at least \(t\), and **small** otherwise.

Every small vertex of degree \(d\ge4\) has at most \(d-2\) degree-two neighbours: indeed,
\[
D\ge3t-6\ge2d-3,
\]
so (4) applies.

The inequality (1) gives the following further facts.

### Degree two

Every degree-two vertex has both neighbours of degree at least four. Otherwise their degree sum would be at most \(D+3\), whereas (1) requires at least \(D+4\).

It also has a big neighbour: two small neighbours have degree sum at most \(2t-2\), less than
\[
D+4\ge3t-2.
\]

### Degree three

Every degree-three vertex has a big neighbour. Otherwise its neighbour-degree sum would be at most \(3t-3\), less than
\[
D+5\ge3t-1.
\]

### Small vertices without big neighbours

Such vertices satisfy:

\[
\begin{array}{c|c}
\text{degree}&\text{maximum number of degree-two neighbours}\\ \hline
4&0\\
5&2\\
6&3
\end{array} \tag{5}
\]

Here are the checks. If a degree-four vertex has a degree-two neighbour and no big neighbour, its neighbour-degree sum is at most
\[
2+3(t-1)=3t-1<D+6.
\]
If a degree-five vertex has at least three degree-two neighbours and no big neighbour, that sum is at most
\[
6+2(t-1)=2t+4<D+7.
\]
If a degree-six vertex has at least four degree-two neighbours and no big neighbour, it is at most
\[
8+2(t-1)=2t+6<D+8.
\]
All three contradict (1), using \(D\ge3t-6\) and \(t\ge10\).

# 4. Discharging

Set
\[
\rho=\frac{11t}{3(t+1)},\qquad
\beta=1-\frac{\rho}{t}.
\]
The useful identities and inequalities are
\[
\rho=\beta+\frac83,\qquad
\beta\ge\frac23,\qquad
\rho<\frac{11}{3}.
\]

Give each vertex initial charge equal to its degree, and make these transfers:

1. Each big vertex sends \(\beta\) to each small neighbour.
2. Each small vertex of degree at least four sends \(2/3\) to each degree-two neighbour.

We verify that every vertex finishes with charge at least \(\rho\).

### Big vertices

A big vertex of degree \(d\) sends at most \(d\beta\), so retains at least
\[
d(1-\beta)=d\frac{\rho}{t}\ge\rho.
\]

### Degree-two vertices

Such a vertex has a big neighbour and its other neighbour has degree at least four. It receives \(\beta\) from the first, and at least \(2/3\) from the other: either the other is small and rule 2 applies, or it is big and sends \(\beta\ge2/3\).

Its final charge is at least
\[
2+\beta+\frac23=\rho.
\]

### Degree-three vertices

These have a big neighbour and no degree-two neighbour. Their final charge is at least
\[
3+\beta=\rho+\frac13.
\]

### Small vertices of degree \(d\ge4\) with a big neighbour

By (4), they have at most \(d-2\) degree-two neighbours. Their final charge is at least
\[
d+\beta-\frac23(d-2)
=\beta+\frac{d+4}{3}
\ge\beta+\frac83=\rho.
\]

### Small vertices without a big neighbour

Using (5), their final charges are at least

- \(4\), if \(d=4\);
- \(5-\frac23\cdot2=\frac{11}{3}\), if \(d=5\);
- \(6-\frac23\cdot3=4\), if \(d=6\).

For \(d\ge7\), equation (4) gives a final charge of at least
\[
d-\frac23(d-2)=\frac{d+4}{3}\ge\frac{11}{3}.
\]

Thus every case has final charge at least \(\rho\). Charge is conserved, so
\[
2|E(H)|\ge \rho |V(H)|.
\]
This contradicts
\[
\operatorname{mad}(H)\le\operatorname{mad}(G)<\rho.
\]
The theorem follows. \(\square\)

# 5. Consequences and the remaining gap

Taking \(t=10\) gives
\[
\rho_{10}=\frac{10}{3},
\qquad
D\ge24.
\]
Hence
\[
\boxed{\;
\Delta\ge24,\quad \operatorname{mad}(G)<\frac{10}{3}
\quad\Longrightarrow\quad
a'(G)\le\Delta+2,
\;}
\]
including the list version.

For planar graphs of girth at least five, Euler’s formula gives
\[
\operatorname{mad}(G)<\frac{10}{3}.
\]
Indeed, every subgraph has the same girth restriction; cyclic connected components satisfy the usual planar girth bound, and forest components have average degree below two. This proves the stated planar corollary.

More generally, for \(\Delta\ge24\), take
\[
t=\left\lfloor\frac{\Delta+6}{3}\right\rfloor.
\]
The sufficient maximum-average-degree threshold is then
\[
\frac{11}{3}
-\frac{11}{3\left(\left\lfloor(\Delta+6)/3\right\rfloor+1\right)},
\]
which tends to \(11/3\) as \(\Delta\to\infty\).

The unresolved gap is substantial: arbitrary graphs need not satisfy any such sparsity condition. For example, a \(\Delta\)-regular graph has maximum average degree \(\Delta\), and the discharging contradiction above says nothing about it. The argument therefore establishes a precise sparse-graph special case, not the universal \(\Delta+2\) conjecture.