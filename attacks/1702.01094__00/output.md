```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is sharp for s at most 3; I also prove the s=4 case for odd-hole-free graphs, give quantitative lower bounds, and derive a separator criterion and fixed-s recognition algorithm.",
  "would_publish": false,
  "caveats": "Colouring is interpreted as proper; the unrestricted problem remains open for s at least 4."
}
```

# 1. Interpretation and summary

I use the standard meaning from Scott–Seymour: a “colouring” is a proper vertex-colouring, although it need not be optimal. If arbitrary vertex-labellings were allowed, the statement would be false for every \(s\ge 2\): take triangle-free graphs of arbitrarily large chromatic number and colour every vertex identically.

A hole is an induced cycle of length at least four. For fixed \(s,\kappa\), write \(c^*(s,\kappa)\) for the least integer \(c\), if it exists, such that every graph \(G\) with
\[
\omega(G)\le \kappa,\qquad \chi(G)>c
\]
has, in every proper colouring, a hole with \(s\) consecutive vertices of pairwise distinct colours.

The main conclusions below are:

1. \(\boxed{c^*(s,\kappa)=\kappa}\) for \(s=1,2,3\).
2. For \(s=4\), the same sharp bound holds within the class of odd-hole-free graphs.
3. For \(\kappa\ge2\),
   \[
   c^*(4,\kappa)\ge \kappa+1,
   \]
   if \(c^*(4,\kappa)\) exists.
4. For \(s\ge5\), writing \(\kappa=2t+r\) with \(r\in\{0,1\}\),
   \[
   c^*(s,\kappa)\ge t(s-1)+r.
   \]
5. A rainbow induced \(s\)-vertex path can be closed into the desired hole exactly when its endpoints remain connected after deleting the closed neighbourhood of its internal vertices. This gives a useful separator reduction and a polynomial-time recognition algorithm for fixed \(s\).

The general problem for \(s\ge4\), including the triangle-free \(s=4\) case, is not resolved.

---

# 2. The cases \(s\le 3\)

## Theorem 2.1

Let \(G\) be a graph and let \(\phi\) be any proper colouring of \(G\). If
\[
\chi(G)>\omega(G),
\]
then \(G\) has a hole containing three consecutive vertices with pairwise distinct colours.

Consequently, for every positive \(\kappa\),
\[
c^*(1,\kappa)=c^*(2,\kappa)=c^*(3,\kappa)=\kappa.
\]

### Proof

The cases \(s=1,2\) are immediate once \(G\) contains a hole: a singleton is rainbow, and two consecutive vertices of a hole receive different colours in a proper colouring. If \(G\) had no hole, it would be chordal and therefore perfect, contrary to \(\chi(G)>\omega(G)\).

It remains to treat \(s=3\). Suppose, to the contrary, that no hole has a rainbow set of three consecutive vertices.

Let
\[
H=v_0v_1\cdots v_{n-1}v_0
\]
be any hole. Since the colouring is proper,
\[
\phi(v_i)\ne\phi(v_{i+1}),\qquad
\phi(v_{i+1})\ne\phi(v_{i+2}).
\]
Thus, if \(v_i,v_{i+1},v_{i+2}\) are not rainbow, necessarily
\[
\phi(v_i)=\phi(v_{i+2}). \tag{2.1}
\]

In particular, \(G\) has no odd hole: on an odd hole, repeatedly applying (2.1) makes all vertices have the same colour, since \(2\) generates the cyclic group \(\mathbb Z_n\) when \(n\) is odd. This contradicts properness.

We next show that \(G\) has no odd antihole. An antihole of length five is itself a \(5\)-hole, already excluded. Let therefore
\[
A=\overline{C_n},\qquad n\ge7\text{ odd},
\]
be an induced odd antihole, with vertices \(v_0,\ldots,v_{n-1}\) indexed so that the only nonedges of \(A\) are \(v_iv_{i+1}\).

For every \(i\), the four vertices
\[
v_i,\ v_{i+1},\ v_{i+3},\ v_{i+4}
\]
induce a \(C_4\) in \(A\): its two nonedges are
\[
v_iv_{i+1}\quad\text{and}\quad v_{i+3}v_{i+4}.
\]
On a properly coloured \(C_4\) with no rainbow consecutive triple, opposite vertices must receive the same colour. Hence
\[
\phi(v_i)=\phi(v_{i+1})
\]
for every \(i\). This is impossible because, for example, \(v_i\) and \(v_{i+2}\) are adjacent in \(A\).

Thus \(G\) has neither an odd hole nor an odd antihole. By the Strong Perfect Graph Theorem, \(G\) is perfect, contradicting \(\chi(G)>\omega(G)\).

Therefore a rainbow consecutive triple exists.

Finally, if \(\omega(G)\le\kappa\) and \(\chi(G)>\kappa\), then \(\chi(G)>\omega(G)\), so \(c=\kappa\) suffices. It is sharp because \(K_\kappa\) has chromatic number \(\kappa\) and no hole. ∎

For \(\kappa=2\), this gives the particularly sharp statement that every non-bipartite triangle-free graph, under every proper colouring, has an odd hole with a rainbow consecutive triple.

---

# 3. A special \(s=4\) result

The following antihole observation is useful.

## Lemma 3.1

Let \(n\ge7\) be odd. Every proper colouring of the odd antihole \(\overline{C_n}\) contains a fully rainbow induced \(C_4\).

### Proof

Write the vertices as \(v_0,\ldots,v_{n-1}\), where \(v_i v_{i+1}\) are precisely the nonedges of the antihole. Call the cycle edge \(v_iv_{i+1}\) of the underlying \(C_n\):

- monochromatic if \(\phi(v_i)=\phi(v_{i+1})\);
- bichromatic otherwise.

Two consecutive underlying cycle edges cannot both be monochromatic, since that would give
\[
\phi(v_i)=\phi(v_{i+1})=\phi(v_{i+2}),
\]
while \(v_i\) and \(v_{i+2}\) are adjacent in the antihole. Hence at most \((n-1)/2\) underlying cycle edges are monochromatic, and at least
\[
\frac{n+1}{2}\ge4
\]
are bichromatic.

Among at least four edges of \(C_n\), \(n\ge7\), there are two, say
\[
e_i=v_iv_{i+1},\qquad e_j=v_jv_{j+1},
\]
which are separated by at least two unused cycle edges in both cyclic directions. Equivalently, none of the four cross-pairs is consecutive on the underlying \(C_n\). Therefore the four endpoints induce a \(K_{2,2}=C_4\) in the antihole, with \(e_i,e_j\) as its two nonedges.

The endpoints within each of \(e_i,e_j\) have different colours because both edges are bichromatic. Every cross-pair is adjacent in the antihole and hence also has different colours. Thus all four colours are distinct. ∎

## Corollary 3.2

Let \(G\) be odd-hole-free. If \(\chi(G)>\omega(G)\), then every proper colouring of \(G\) has a fully rainbow \(C_4\).

In particular, among odd-hole-free graphs with \(\omega(G)\le\kappa\), the sharp \(s=4\) cutoff is \(c=\kappa\).

### Proof

By the Strong Perfect Graph Theorem, a graph with \(\chi(G)>\omega(G)\) contains an odd hole or an odd antihole. The former is excluded. An odd antihole of length five is a \(C_5\), also excluded, so the antihole has length at least seven. Apply Lemma 3.1. ∎

This does not settle \(s=4\) in general: a counterexample to the general statement may contain odd holes, and an odd hole can of course be coloured with only three colours.

---

# 4. Quantitative lower bounds

These examples show that any positive answer must have substantial dependence on both \(s\) and \(\kappa\).

## 4.1 The case \(s=4\)

For every \(\kappa\ge2\), let
\[
G=K_{\kappa-2}\vee C_5,
\]
where \(\vee\) denotes the complete join.

Then
\[
\omega(G)=(\kappa-2)+2=\kappa,\qquad
\chi(G)=(\kappa-2)+3=\kappa+1.
\]
Colour the \(C_5\) with three colours and use new colours on the clique.

Every hole is contained in the \(C_5\): a vertex of the joined clique is adjacent to every other vertex and therefore cannot lie on an induced cycle of length at least four. Since the \(C_5\) uses only three colours, no four consecutive vertices are rainbow. Hence
\[
\boxed{c^*(4,\kappa)\ge\kappa+1.}
\]

Thus the exact \(s=3\) threshold cannot extend unchanged to \(s=4\).

## 4.2 The case \(s\ge5\)

We use two elementary facts about joins.

1. Chromatic number and clique number are additive under joins:
   \[
   \chi(G_1\vee G_2)=\chi(G_1)+\chi(G_2),\qquad
   \omega(G_1\vee G_2)=\omega(G_1)+\omega(G_2).
   \]
2. Every hole of length at least five in a join is contained in one factor.

For the second assertion, suppose an induced cycle \(C\) of length \(\ell\ge5\) meets two join factors. If a vertex \(x\) of one factor has vertices of \(C\) outside its factor, then \(x\) is adjacent to all of them, so there can be at most two such vertices. Thus its factor contributes at least \(\ell-2\ge3\) vertices of \(C\). A vertex of another factor is adjacent to all these three vertices, contradicting its degree two within an induced cycle.

For every \(q\ge2\), there exists a triangle-free graph \(H_q\) with
\[
\chi(H_q)=q,\qquad \omega(H_q)=2.
\]
This follows, for instance, by iterating the Mycielski construction starting from \(K_2\). The construction preserves triangle-freeness and increases chromatic number by exactly one.

Now let \(s\ge5\), write
\[
\kappa=2t+r,\qquad r\in\{0,1\},
\]
and let
\[
G=\underbrace{H_{s-1}\vee\cdots\vee H_{s-1}}_{t\text{ copies}}\vee K_r.
\]
Then
\[
\omega(G)=2t+r=\kappa
\]
and
\[
\chi(G)=t(s-1)+r.
\]

Colour each \(H_{s-1}\) with \(s-1\) colours, using disjoint palettes for different join factors. Any hole with at least \(s\ge5\) vertices is contained in one \(H_{s-1}\), where only \(s-1\) colours occur. Thus no such hole has \(s\) consecutive rainbow vertices. Therefore
\[
\boxed{c^*(s,\kappa)\ge (s-1)\left\lfloor\frac{\kappa}{2}\right\rfloor
      +(\kappa\bmod 2),\qquad s\ge5.}
\]

For example, already at \(\kappa=2\), any forcing cutoff must be at least \(s-1\).

---

# 5. Exact path-closing criterion

The source theorem guarantees long induced rainbow paths. The precise obstruction to closing such a path into a hole is the following separator.

## Lemma 5.1

Let
\[
P=p_1-p_2-\cdots-p_s
\]
be an induced path, with \(s\ge3\), and put
\[
I=\{p_2,\ldots,p_{s-1}\},\qquad
D_P=N[I]\setminus\{p_1,p_s\}.
\]
Then \(P\) occurs as a proper consecutive segment of a hole if and only if \(p_1\) and \(p_s\) lie in the same component of \(G-D_P\).

Here “proper segment” means that the hole has at least \(s+1\) vertices. A fully rainbow hole of length exactly \(s\) must be considered separately.

### Proof

If a hole contains \(P\) as a proper consecutive segment, its complementary \(p_1\)-\(p_s\) arc has no internal vertex adjacent to any vertex of \(I\), since such an edge would be a chord. Thus that arc lies in \(G-D_P\).

Conversely, suppose \(p_1,p_s\) are connected in \(G-D_P\), and let \(Q\) be a shortest \(p_1\)-\(p_s\) path there. The internal vertices of \(Q\) are anticomplete to \(I\). The path \(Q\) is induced, and shortestness ensures that neither endpoint has an edge to a nonconsecutive internal vertex of \(Q\). Since \(P\) is induced, \(P\cup Q\) is therefore an induced cycle containing \(P\) consecutively. ∎

Thus, in a graph with no desired hole, every induced rainbow \(P_s\) has its endpoints separated by \(D_P\).

## Corollary 5.2: a chromatic-connectivity special case

Define
\[
\ell(G)=\max_{v\in V(G)}\chi(G[N(v)])
\]
and
\[
\lambda_\chi(G)=
\min\{\chi(G[S]):\text{ some two vertices of }G-S
\text{ lie in different components}\},
\]
with \(\lambda_\chi(G)=\infty\) if no such separator exists.

Let \(s\ge4\). Suppose \(\omega(G)\le\kappa\), and suppose
\[
\lambda_\chi(G)>(s-2)\ell(G).
\]
If \(\chi(G)\) is large enough to invoke the Scott–Seymour rainbow induced-path theorem for \((s,\kappa)\), then every proper colouring of \(G\) has the desired hole.

### Proof

The rainbow-path theorem gives an induced rainbow path \(P=p_1-\cdots-p_s\). For \(s\ge4\), each vertex of the internal path \(I\) has a neighbour in \(I\), and hence
\[
D_P\subseteq\bigcup_{i=2}^{s-1}N(p_i).
\]
Consequently,
\[
\chi(G[D_P])
 \le \sum_{i=2}^{s-1}\chi(G[N(p_i)])
 \le (s-2)\ell(G).
\]
By the assumption on \(\lambda_\chi(G)\), \(D_P\) cannot separate \(p_1\) from \(p_s\). Lemma 5.1 closes \(P\) into a hole. ∎

For triangle-free graphs, every neighbourhood is stable, so \(\ell(G)\le1\). Hence:

\[
\boxed{\lambda_\chi(G)>s-2}
\]
is sufficient, together with sufficiently large chromatic number, in the triangle-free case.

There is also an inductive consequence. If the conjecture were already known for clique number \(\kappa-1\), with cutoff \(B\), then any counterexample of clique number at most \(\kappa\) would satisfy
\[
\chi(G[N(v)])\le B
\]
for every vertex \(v\). Every rainbow \(P_s\) in such a counterexample would therefore produce a separator of chromatic number at most \((s-2)B\).

This does not finish the induction. Repeated decomposition along low-chromatic cutsets can accumulate chromatic number. Iterated Mycielski graphs illustrate the difficulty: each new Mycielskian has a stable cutset separating the new apex from the previous graph, while the chromatic number still grows at every iteration.

---

# 6. Fixed-\(s\) recognition algorithm

For a graph with a specified vertex-colouring and fixed \(s\), existence of the required hole can be decided in polynomial time.

Enumerate all ordered \(s\)-tuples of distinct vertices.

1. Check whether the tuple induces a fully rainbow \(C_s\). This handles holes of length exactly \(s\).
2. Check whether it induces a rainbow path
   \[
   p_1-\cdots-p_s.
   \]
   If so, construct
   \[
   D_P=N[\{p_2,\ldots,p_{s-1}\}]\setminus\{p_1,p_s\}
   \]
   and test by breadth-first search whether \(p_1,p_s\) are connected in \(G-D_P\).
3. If they are connected, a shortest such path, together with \(P\), gives the desired hole by Lemma 5.1.

If a target hole has length \(s\), step 1 finds it. If it has length greater than \(s\), any rainbow \(s\)-window is an induced \(P_s\), and its complementary arc certifies connectivity in step 2. Thus the algorithm is complete.

With an adjacency matrix for constant-time tuple checks, the naive running time is
\[
O\!\left(n^s(n+m)\right),
\]
which is polynomial for every fixed \(s\).

For exhaustive small-order searches for bad colourings, one can instead use Boolean variables \(x_{uv}\) meaning “\(u\) and \(v\) have the same colour,” impose equivalence-relation clauses, impose \(\neg x_{uv}\) for every edge \(uv\), and for every cyclic \(s\)-window \(W\) of every hole impose
\[
\bigvee_{\{u,v\}\subseteq W}x_{uv}.
\]
A satisfying assignment is exactly a proper colouring with no rainbow \(s\)-window. I have not run this enumeration, so no small-order computational claim is made here.

---

# 7. Remaining gap

The unrestricted conjecture remains unresolved for \(s\ge4\).

The main obstruction exposed by Lemma 5.1 is precise: the rainbow-path theorem supplies the desired local segment, but in a counterexample the closed neighbourhood of its internal vertices separates its endpoints. In triangle-free graphs this separator is \((s-2)\)-colourable, but high chromatic number alone does not presently rule out recursive accumulation across such stable or low-chromatic separators.

For \(s=4\), the Strong Perfect Graph Theorem only reduces a possible counterexample to the odd-hole side: odd antiholes already force fully rainbow \(C_4\)'s, while odd holes themselves admit three-colourings and therefore need not contain a rainbow block of four. No argument above controls how many such odd-hole pieces can interact in a high-chromatic bounded-clique graph.