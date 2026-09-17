Attack the following open graph-theory problem.

Catalog id: switching_reconstruction_of_digraphs
Source: OpenProblemGarden (importance: Medium ✭✭)
Subject: Graph Theory
Catalog page: https://graph-theory-ai.github.io/graph-conjectures/op/switching_reconstruction_of_digraphs/
Original entry: http://www.openproblemgarden.org/op/switching_reconstruction_of_digraphs
Problem attributed to: Bondy, J. Adrian, Mercier, Fabien (posted 2013-03-07)

=== Problem statement (OpenProblemGarden) ===
Title: Switching reconstruction of digraphs
Question Are there any switching-nonreconstructible digraphs on twelve or more vertices?

=== Discussion / context (OpenProblemGarden) ===
To switch a vertex of a digraph is to reverse all the arcs incident to it. The digraph so obtained is called a switching of the digraph. The collection of switchings of a digraph $ D $ is called the switching deck of $ D $ . A digraph is switching-reconstructible if every digraph with the same deck as $ D $ is isomorphic to $ D $ . The problem is a directed analogue of switching reconstruction of graphs in which one complements the edges at a vertex, instead of reversing each of its incident arcs. Bondy and Mercier proved an analogue to Stanley's result for switching reconstruction of graphs. They proved that a digraph on $ n $ vertices is switching-reconstructible if $ n \not\equiv 0 (\mod 4) $ . They also proved many other common results for both switching reconstructions. One significant difference between the directed and undirected problems is that there exist switching-nonreconstructible directed graphs on eight vertices, while Stanley's conjecture that every simple graph on five or more vertices is switching-reconstructible.

=== References listed by OpenProblemGarden ===
- *[BM] J. A. Bondy and F. Mercier. Switching reconstruction of digraphs. J. Graph Theory 67(2011), no. 4, 332-348.

=== Catalog page (statement + literature review) ===
Switching reconstruction of digraphs — Graph-theory open problems

 
 Status
 partial
 medium confidence
 

 McKay and Schweitzer (2014) made meaningful progress by showing that there are exactly 44 switching-nonreconstructible oriented graphs whose underlying undirected graphs have maximum degree at most 2, and by determining the complete family of switching-stable oriented graphs; the largest known nonreconstructible examples still have only 8 vertices. The original question — whether switching-nonreconstructible digraphs on 12 or more vertices exist — remains open.

 Cited literature (1)

 
 
 
partial Switching Reconstruction of Digraphs
 (2014)
 

 
 Brendan D. McKay, Pascal Schweitzer · Journal of Graph Theory · arXiv:1308.0675

Proved that there are exactly 44 switching-nonreconstructible oriented graphs whose underlying graphs have maximum degree at most 2, and determined all switching-stable oriented graphs, without resolving existence of nonreconstructible digraphs on 12 or more vertices.
 

 

 Reviewer notes. The McKay–Schweitzer paper was submitted to arXiv on 2013-08-03 (after the OPG posting date 2013-03-07) and published in J. Graph Theory 76 (2014) 279–296. I could not determine from the abstract alone whether any of their 44 nonreconstructible examples lie on 12+ vertices, but search summaries consistently state that 'the largest known nonreconstructible oriented graphs have 8 vertices'. A related paper 'The r-switching-stable graphs' appeared on ScienceDirect (pii S0166218X18306565, likely 2018–2019) but returned HTTP 403, so it was not verified and is not cited. The Bondy–Mercier result that digraphs with n ≢ 0 (mod 4) are switching-reconstructible means n = 12 (≡ 0 mod 4) is the smallest open case.

 
 Auto-reviewed 2026-05-08 with claude-sonnet-4-6 (worker 05) (web search enabled).
 

Question. Are there any switching-nonreconstructible digraphs on twelve or more vertices?

Discussion

To switch a vertex of a digraph is to reverse all the arcs incident to it. The digraph so obtained is called a switching of the digraph. The collection of switchings of a digraph $ D $ is called the switching deck of $ D $ . A digraph is switching-reconstructible if every digraph with the same deck as $ D $ is isomorphic to $ D $ . The problem is a directed analogue of switching reconstruction of graphs in which one complements the edges at a vertex, instead of reversing each of its incident arcs. Bondy and Mercier proved an analogue to Stanley's result for switching reconstruction of graphs. They proved that a digraph on $ n $ vertices is switching-reconstructible if $ n \not\equiv 0 (\mod 4) $ . They also proved many other common results for both switching reconstructions. One significant difference between the directed and undirected problems is that there exist switching-nonreconstructible directed graphs on eight vertices, while Stanley's conjecture that every simple graph on five or more vertices is switching-reconstructible.

Bibliography

★ [BM]
 J. A. Bondy and F. Mercier. Switching reconstruction of digraphs. J. Graph Theory 67(2011), no. 4, 332-348.

========================================================================

=== A PREVIOUS, UNVERIFIED ATTEMPT ===
The problem above was already attacked by `gpt-6-astra`, which reported verdict `partial` at high confidence. That attempt is reproduced below.

Treat it as a lead, not as an authority: it is unverified, it may be wrong in ways neither model noticed, and its framing may be the reason it stalled. Check anything you reuse, and say so if you discard it. Your task is the original problem, not a critique of this attempt. If you can finish what it started, do that; if a different route is better, take it.

--- previous attempt ---
```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove an exponential orbit-size obstruction for connected counterexamples and exclude all switchings of transitive tournaments on at least twelve vertices.",
  "would_publish": false,
  "caveats": "The unrestricted existence question is not settled; novelty relative to the listed references has not been checked, and no exhaustive computation was performed."
}
```

## 1. The partial result

The switching deck is understood as a **multiset of isomorphism types**, with one card for each vertex.

I allow antiparallel pairs of arcs, though they play no role in switching. For a digraph \(D\), let \(G\) be the undirected graph whose edges are the pairs carrying **exactly one** arc of \(D\). Thus, for an oriented graph, \(G\) is its ordinary underlying graph. Write \(n=|V(D)|\), and let \(c\) be the number of components of \(G\), including isolated vertices.

For \(S\subseteq V(D)\), write \(D^S\) for the result of switching every vertex in \(S\). Let
\[
\mathcal C(D)=\{D^S:S\subseteq V(D)\}
\]
be the labelled switching class. Define
\[
\Gamma(D)=\{\pi\in\operatorname{Sym}(V(D)):\pi\mathcal C(D)=\mathcal C(D)\}.
\]
This group acts on the labelled digraphs in \(\mathcal C(D)\). Its orbit on \(D\) has size
\[
r(D):=\bigl|\{F\in\mathcal C(D):F\cong D\}\bigr|
      =\frac{|\Gamma(D)|}{|\operatorname{Aut}(D)|}.
\]

### Proposition
Suppose \(D\) and \(E\) are nonisomorphic digraphs with the same switching deck. After relabelling \(E\), they belong to the same switching class. Moreover,
\[
n\equiv0\pmod4
\]
and
\[
\boxed{\quad r(D),r(E)\ \ge\ 2^{\,n/2-c-1}.\quad} \tag{1}
\]

In particular, when \(G\) is connected,
\[
r(D),r(E)\ge 2^{\,n/2-2}. \tag{2}
\]

At \(n=12\), every member of a connected counterexample pair must therefore have **at least sixteen distinct labelled copies within its switching class**.

Since \(\Gamma(D)\leq\operatorname{Aut}(G)\), an immediate consequence is:

> Every orientation of a connected twelve-vertex graph with at most fifteen automorphisms is switching-reconstructible.

A different consequence, which applies despite the enormous automorphism group of the underlying complete graph, is:

### Corollary
Every tournament obtained by switching an arbitrary subset of vertices of a transitive tournament on at least twelve vertices is switching-reconstructible.

I prove both statements below.

---

## 2. Equal decks give a zero-eigenfunction of a cube

### 2.1. Putting the two digraphs in one switching class

If the decks of \(D\) and \(E\) agree, there are vertices \(u,v\) and an isomorphism
\[
D^{\{u\}}\cong E^{\{v\}}.
\]
Use this isomorphism to identify the vertex sets. Then
\[
E=D^{\{u\}\triangle\{v\}}.
\]
Thus \(E\in\mathcal C(D)\). In the nonisomorphic case the two identified vertices are distinct.

### 2.2. The switching cube

Use sign vectors \(x\in\{-1,1\}^{V(D)}\) to describe switching: let \(D^x\) reverse an asymmetric arc \(uv\) precisely when \(x_ux_v=-1\).

Two vectors \(x,y\) produce the same labelled digraph if and only if \(x_uy_u\) is constant on each component of \(G\). Consequently, every labelled member of \(\mathcal C(D)\) has exactly \(2^c\) sign-vector representations.

Partition the cube into sets \(U_i\), one for each isomorphism type occurring in \(\mathcal C(D)\):
\[
U_i=\{x:D^x\text{ has isomorphism type }i\}.
\]
Write \(N_i=|U_i|\).

Let \(q_{ij}\) be the number of single-coordinate flips taking a fixed point of \(U_i\) into \(U_j\). This is well-defined: isomorphic digraphs have the same switching deck. Thus the row \((q_{ij})_j\) is precisely the deck of type \(i\), recorded by multiplicities.

Counting cube edges between two parts gives
\[
N_iq_{ij}=N_jq_{ji}. \tag{3}
\]

Let \(A\) and \(B\) be the parts corresponding to \(D\) and \(E\). Equal decks mean
\[
q_{Aj}=q_{Bj}\qquad\text{for every }j.
\]

Define the real function
\[
f(x)=\frac{\mathbf 1_A(x)}{|A|}
     -\frac{\mathbf 1_B(x)}{|B|}.
\]
The normalization matters: the two parts need not have the same size.

Let \(T\) be the adjacency operator of the \(n\)-cube:
\[
(Tf)(x)=\sum_{v\in V(D)}f(x^{(v)}),
\]
where \(x^{(v)}\) flips coordinate \(v\). For \(x\in U_j\), equation (3) gives
\[
(Tf)(x)
=\frac{q_{jA}}{|A|}-\frac{q_{jB}}{|B|}
=\frac{q_{Aj}-q_{Bj}}{N_j}
=0. \tag{4}
\]
Hence \(f\neq0\) is a zero-eigenfunction of the cube.

In fact, this argument is reversible: for two distinct isomorphism-type parts, the normalized difference above lies in \(\ker T\) if and only if their switching decks agree.

### 2.3. Fourier consequences

For \(S\subseteq V(D)\), put
\[
\chi_S(x)=\prod_{v\in S}x_v.
\]
These characters form a basis, and
\[
T\chi_S=(n-2|S|)\chi_S.
\]
Therefore (4) implies that \(n\) is even and that the Fourier expansion of \(f\) is supported entirely on
\[
|S|=n/2. \tag{5}
\]

Also, \(D^x=D^{-x}\), so \(f(x)=f(-x)\). Hence all odd-degree Fourier coefficients vanish. Together with (5), this forces \(n/2\) to be even:
\[
n\equiv0\pmod4.
\]
This recovers the congruence obstruction stated in the question.

Writing \(d=n/2\), we additionally have
\[
\sum_x f(x)\chi_S(x)=0
\qquad\text{whenever }|S|<d. \tag{6}
\]

The useful next step is to turn these vanishing moments into a lower bound on **each** sign-support of \(f\), not merely their union.

---

## 3. A signed-support lemma

### Lemma
Let \(h:\{-1,1\}^m\to\mathbb R\) be nonzero. Suppose \(1\le d\le m\) and
\[
\sum_x h(x)\chi_S(x)=0
\qquad\text{for every }|S|<d.
\]
Then
\[
|\{x:h(x)>0\}|\ge 2^{d-1},
\qquad
|\{x:h(x)<0\}|\ge 2^{d-1}. \tag{7}
\]

### Proof

We induct on \(d\).

For \(d=1\), the hypothesis includes \(\sum_x h(x)=0\). A nonzero function of mean zero has both signs, proving the assertion.

Now suppose \(d\ge2\). First, \(h\) cannot be positive at just one point \(p\). Indeed, the linear polynomial
\[
\ell_p(x)=\sum_{i=1}^m(1-p_ix_i)
\]
is zero at \(p\) and strictly positive everywhere else. If \(p\) were the only positive point, then
\[
\sum_x h(x)\ell_p(x)<0,
\]
contrary to the vanishing of the constant and degree-one moments.

Thus two positive points differ in some coordinate \(j\). Both restrictions
\[
h_+=h|_{x_j=1},
\qquad
h_-=h|_{x_j=-1}
\]
have positive points. For \(S\subseteq[m]\setminus\{j\}\) with \(|S|<d-1\),
\[
\sum h_\pm\chi_S
=\frac12\left(\sum h\chi_S
       \pm\sum h\chi_{S\cup\{j\}}\right)
=0.
\]
The induction hypothesis gives at least \(2^{d-2}\) positive points in each restriction. This proves the positive-support bound. Apply the same argument to \(-h\) for the negative-support bound. \(\square\)

### Completion of the proposition

Apply the lemma to \(f\) using (6). Its positive and negative supports are exactly \(A\) and \(B\), so
\[
|A|,|B|\ge 2^{n/2-1}.
\]
Every labelled digraph has \(2^c\) sign-vector representations. Consequently,
\[
|A|=2^c r(D),\qquad |B|=2^c r(E),
\]
and division gives (1).

For completeness, the orbit formula defining \(r(D)\) follows because the stabilizer of \(D\) in \(\Gamma(D)\) is exactly \(\operatorname{Aut}(D)\). Also, \(\Gamma(D)\le\operatorname{Aut}(G)\), since switching does not change which pairs carry exactly one arc.

Thus a connected nonreconstructible \(D\) must satisfy the stronger symmetry requirement
\[
|\Gamma(D)|
\ \ge\
2^{n/2-2}\,|\operatorname{Aut}(D)|. \tag{8}
\]

---

## 4. Application: switchings of transitive tournaments

Let \(T_n\) be the transitive tournament labelled so that
\[
i\longrightarrow j\quad\Longleftrightarrow\quad i<j.
\]

I claim that, for \(n\ge3\),
\[
\Gamma(T_n)\cong C_n, \tag{9}
\]
acting as the rotations of the cyclic order \(1,2,\ldots,n\).

To see this, define
\[
a_{ij}=
\begin{cases}
1,&i\to j,\\
-1,&j\to i.
\end{cases}
\]
For distinct vertices, the triple product
\[
a_{ij}a_{jk}a_{ki}
\]
is switching-invariant: a switch at one of the three vertices changes exactly two factors.

For \(T_n\), this product is \(-1\) precisely when \((i,j,k)\) occurs in the positive cyclic order associated with \(1,2,\ldots,n\). Therefore every element of \(\Gamma(T_n)\) preserves that cyclic order. Its only preserving permutations are the \(n\) rotations.

Conversely, the rotation
\[
\rho=(1\,2\,\cdots\,n)
\]
satisfies
\[
\rho(T_n)=T_n^{\{1\}}.
\]
Thus every rotation preserves the switching class, proving (9).

Now let \(D\in\mathcal C(T_n)\). Since \(D\) and \(T_n\) have the same switching class,
\[
\Gamma(D)=\Gamma(T_n),
\qquad\text{so}\qquad
r(D)\le n. \tag{10}
\]

If \(D\) were nonreconstructible, the proposition would require \(4\mid n\) and
\[
r(D)\ge 2^{n/2-2}.
\]
But for every multiple of four with \(n\ge12\),
\[
2^{n/2-2}>n.
\]
This contradicts (10), proving the corollary.

This illustrates why \(\Gamma(D)\), rather than merely the automorphism group of the underlying graph, is the relevant symmetry parameter: here the underlying graph is \(K_n\), but the switching-class symmetry group has only \(n\) elements.

---

## 5. A precise computational reduction at twelve vertices

The proposition gives the following exhaustive procedure for a **fixed connected underlying graph** \(G\) on twelve vertices.

1. **Discard small automorphism groups.**  
   If \(|\operatorname{Aut}(G)|<16\), no orientation of \(G\) is a counterexample.

2. **Enumerate labelled switching classes.**  
   Fix a spanning tree and prescribe its edge directions. Every switching class has exactly one orientation with those prescribed tree directions. Thus, if \(G\) has \(m\) edges, enumerate the \(2^{m-11}\) assignments on the remaining edges.

3. **Compute \(\Gamma(D)\) for each class.**  
   For each \(\pi\in\operatorname{Aut}(G)\), compare \(D\) with \(\pi D\). If \(\delta_{uv}\in\mathbb F_2\) records whether their directions on \(uv\) disagree, test whether
   \[
   s_u+s_v=\delta_{uv}\pmod2
   \]
   is solvable. This can be done by propagating values along the spanning tree and checking the remaining edges.

4. **Form the isomorphism-type orbits.**  
   The switching class has \(2^{11}=2048\) labelled members. Partition them into \(\Gamma(D)\)-orbits.

5. **Compare deck rows only for sufficiently large orbits.**  
   An orbit of size less than sixteen cannot be a member of a counterexample pair. For each remaining orbit, compute its twelve card types with multiplicity and compare the resulting rows.

There are at most \(2048/16=128\) eligible orbit rows in any one switching class. Equal distinct rows give an explicit counterexample; absence of such rows certifies that class.

No such enumeration is claimed here. The number of underlying graphs and switching classes still makes this far from a completed twelve-vertex search.

## 6. What remains unresolved

The argument excludes small switching-isomorphism orbits, but it does not control the possible equal-deck pairs between **large** orbits. Highly symmetric switching classes can easily survive the bound.

Thus the original question is **not answered here**. The established progress is the necessary bound (1), its connected twelve-vertex threshold of sixteen, and the reconstruction result for the entire switching class of every sufficiently large transitive tournament. I have not compared these derivations against the full listed references, so I make no claim that these partial results are new.
