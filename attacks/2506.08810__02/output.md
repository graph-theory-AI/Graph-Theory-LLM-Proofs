```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A safe-amalgamation construction works for every tournament that remains strongly connected after deleting any two vertices, hence for asymptotically almost every labeled tournament, while explicit Paley tournaments give finite hosts for the transitive tournaments T4, T5, and T6.",
  "would_publish": false,
  "caveats": "This is not a full characterization; low-connectivity targets and transitive T_h for h at least 7 remain unresolved here."
}
```

# 1. Conventions and reformulation

I assume throughout that \(|H|\geq 3\) and that the host has at least two vertices. Otherwise a one-vertex tournament would satisfy the arc-reversal condition vacuously, contrary to the intended convention in the source discussion.

For an arc \(e\) of a tournament \(H\), let \(H^e\) denote the tournament obtained by reversing \(e\).

A basic observation will be used repeatedly.

**Observation.** Let \(G\) be \(H\)-free, and let \(uv\) be an arc of \(G\). If reversing \(uv\) creates a copy of \(H\) on a vertex set \(S\), then \(u,v\in S\), and before the reversal \(G[S]\) is isomorphic to \(H^e\) for some arc \(e\) of \(H\), with \(uv\) corresponding to the reversed arc.

Indeed, a copy not containing both \(u\) and \(v\) would already have existed in \(G\).

# 2. A broad sufficient condition

Call \(H\) **2-deletion-strong** if
\[
H-X\text{ is strongly connected for every }X\subseteq V(H),\quad |X|\leq 2.
\]

The following gives countably infinite solutions for all such targets.

## Theorem 1

Let \(H\) be a finite 2-deletion-strong tournament. Then there is a countably infinite \(H\)-free tournament \(G\) with the stronger property that reversing any nonempty finite set of arcs of \(G\) creates a copy of \(H\).

In particular, reversing any single arc creates \(H\).

### Step 1: Some arc reversal of \(H\) is not isomorphic to \(H\)

We first need the following elementary lemma.

**Lemma 2.** Every tournament \(H\) on at least three vertices has an arc \(e\) such that \(H^e\not\cong H\).

**Proof.** Suppose instead that every one-arc reversal of \(H\) is isomorphic to \(H\). This property is inherited by every tournament isomorphic to \(H\). Hence, starting from a labeled copy of \(H\), every tournament obtainable by a sequence of arc reversals is isomorphic to \(H\).

But the graph whose vertices are all labeled tournaments on a fixed \(n\)-element set, with adjacency given by one-arc reversal, is a hypercube and therefore connected. Thus all \(n\)-vertex tournaments would be mutually isomorphic. This is false for \(n\geq 3\), since there are both transitive and nontransitive tournaments. ∎

Fix such an arc \(e=ab\), where \(a\to b\) in \(H\), and put
\[
F=H^e.
\]
Then \(F\) is \(H\)-free: it has exactly \(|H|\) vertices, and \(F\not\cong H\).

### Step 2: The one-step amalgamation

Let \(C\) be a finite \(H\)-free tournament and let \(u\to v\) be an arc of \(C\). Attach a fresh rooted copy of \(F\), identifying its reversed root arc \(b\to a\) with \(u\to v\), namely \(b\mapsto u\) and \(a\mapsto v\).

Let
\[
W=V(F)\setminus\{a,b\},\qquad
Z=V(C)\setminus\{u,v\}.
\]
Orient every previously unspecified cross-arc from \(W\) to \(Z\):
\[
W\Rightarrow Z.
\]
Call the resulting tournament \(D\).

**Lemma 3.** The tournament \(D\) is \(H\)-free.

**Proof.** Both \(C\) and the attached copy of \(F\) are \(H\)-free. Thus any copy \(K\cong H\) in \(D\) would have to use at least one vertex of \(W\) and at least one vertex of \(Z\).

Remove from \(K\) whichever of the two root vertices \(u,v\) it contains. At most two vertices have been removed. The remaining tournament still has nonempty parts in \(W\) and \(Z\), with every cross-arc directed from the former to the latter. Hence it is not strongly connected.

On the other hand, it is isomorphic to \(H-X\) for some \(X\subseteq V(H)\) with \(|X|\leq 2\), which is strongly connected by hypothesis. This is a contradiction. ∎

After reversing the root arc \(u\to v\), the attached copy of \(F\) becomes a copy of \(H\).

### Step 3: The countable construction

Start with a two-vertex tournament. Whenever an arc first appears, assign it a serial number. In round \(r\), for each existing arc of serial number at most \(r\), attach one fresh rooted copy of \(F\) by the operation above. Attach the copies sequentially within the round.

Every intermediate tournament is finite and \(H\)-free by Lemma 3. Let \(G\) be their union. Then:

- \(G\) is countably infinite;
- \(G\) is \(H\)-free, since any finite copy of \(H\) would already occur at a finite stage;
- every arc receives infinitely many witnesses \(F\), with pairwise disjoint sets of non-root vertices.

Now let \(\mathcal R\) be a finite nonempty set of arcs to be reversed, and choose \(uv\in\mathcal R\). Among the infinitely many witnesses rooted at \(uv\), only finitely many contain another arc of \(\mathcal R\): the fresh vertex sets of these witnesses are pairwise disjoint. Choose an uncontaminated witness. On its vertex set, the only changed arc is \(uv\), so it has become \(H\). This proves Theorem 1. ∎

# 3. A sharper finite sufficient criterion

The strong-connectivity hypothesis can be weakened to an explicit rooted condition.

Fix \(e\) with \(F=H^e\not\cong H\), and let \(A\) be the two endpoints of \(e\) in \(F\). Say that this rooted reversal is **left-safe** if there do not exist

\[
V(H)=P\mathbin{\dot\cup}Q\mathbin{\dot\cup}R,
\]
with \(P,Q\neq\varnothing\), \(|R|\leq 2\), together with an embedding
\[
\psi:H[P\cup R]\hookrightarrow F
\]
such that

\[
P\Rightarrow Q,\qquad
\psi(P)\subseteq V(F)\setminus A,\qquad
\psi(R)\subseteq A.
\]

The same construction as above, orienting the new non-root vertices toward all old non-root vertices, proves:

**Proposition 4.** If \(H\) has a left-safe rooted reversal, then it admits a countably infinite \(H\)-free host which remains \(H\)-creating after every nonempty finite set of arc reversals.

There is a symmetric right-safe version, using the opposite orientation between old and new vertices.

This is a finite, decidable sufficient test: one can enumerate all partitions \(P,Q,R\) and all relevant embeddings into \(H^e\). Theorem 1 follows because if \(H-R\) is strongly connected, it cannot have a nontrivial directed cut \(P\Rightarrow Q\).

# 4. Almost every tournament is covered

Theorem 1 applies asymptotically to almost every labeled tournament.

## Corollary 5

As \(n\to\infty\), the proportion of labeled \(n\)-vertex tournaments \(H\) admitting a countably infinite host as in Theorem 1 tends to \(1\).

**Proof.** Let \(p_m\) be the probability that a uniformly random labeled \(m\)-vertex tournament is not strongly connected. A non-strong tournament has a nonempty proper set \(A\) such that
\[
A\Rightarrow V\setminus A.
\]
For fixed \(|A|=a\), this event has probability \(2^{-a(m-a)}\). Thus
\[
p_m\leq
\sum_{a=1}^{m-1}\binom ma 2^{-a(m-a)}.
\]
For large \(m\),
\[
p_m
 \leq
2\sum_{a=1}^{\lfloor m/2\rfloor}
   \left(m2^{-m/2}\right)^a
 \leq 4m2^{-m/2}.
\]

For a random \(n\)-vertex tournament, a union bound over all deleted sets of size at most two gives failure probability at most
\[
\sum_{s=0}^{2}\binom ns p_{n-s}
   =O\!\left(n^3 2^{-n/2}\right)=o(1).
\]
Hence almost every labeled tournament is 2-deletion-strong, and Theorem 1 applies. ∎

# 5. Targets one reversal away from a transitive tournament

There is another infinite family not covered by the connectivity theorem.

## Proposition 6

Suppose \(H\) is nontransitive and \(H^e\cong T_h\) for some arc \(e\) of \(H\). Then the transitive tournament on \(\mathbb Q\) is an \(H\)-free arc-reversal-saturated tournament. It also creates \(H\) after every nonempty finite set of arc reversals.

**Proof.** Orient \(\mathbb Q\) by
\[
x\to y\quad\Longleftrightarrow\quad x<y.
\]
It is \(H\)-free because every finite subtournament is transitive.

Fix an arc \(x\to y\), so \(x<y\). In the transitive order on \(H^e\), suppose the endpoints of the distinguished arc occupy positions \(i<j\). Choose:

- \(i-1\) rational numbers below \(x\);
- \(j-i-1\) rational numbers strictly between \(x\) and \(y\);
- \(h-j\) rational numbers above \(y\).

Together with \(x,y\), these vertices induce \(H^e\), rooted at \(x\to y\). Reversing \(x\to y\) produces \(H\).

For a finite set of reversed arcs, select any one changed arc \(x\to y\) and choose all supplementary rational points away from the finite set of endpoints of the other changed arcs. Then no other selected arc has been changed. ∎

For \(H=C_3\), this recovers the rational-order example. It also explains the finite obstruction: every finite \(C_3\)-free tournament is transitive, and reversing an arc between consecutive elements merely swaps two adjacent elements and remains transitive.

# 6. Transitive targets

Let \(T_h\) denote the transitive tournament on \(h\) vertices.

## 6.1 No infinite host

**Proposition 7.** No infinite tournament is \(T_h\)-free.

**Proof.** Enumerate an infinite tournament and color each unordered pair according to whether its arc agrees with or opposes the enumeration order. Infinite Ramsey gives an infinite monochromatic subset, which is transitive. ∎

Thus the problem for \(T_h\) is necessarily finite.

There are also useful necessary conditions. If \(G\) is a finite \(T_h\)-free saturated tournament, then:

1. its largest transitive subtournament has order exactly \(h-1\);
2. every vertex lies in a copy of \(T_{h-1}\);
3. every arc lies in a directed triangle;
4. consequently \(G\) is strongly connected.

For example, a witness for an arc is \(T_h\) with one nonadjacent arc reversed. Deleting either endpoint gives a \(T_{h-1}\). The endpoints cannot have been adjacent in the transitive order, since reversing an adjacent pair leaves a transitive tournament; hence an intermediate vertex forms a directed triangle with the exceptional arc.

## 6.2 Explicit finite hosts for \(T_3,T_4,T_5,T_6\)

For \(q\in\{3,7,11,19\}\), let \(P_q\) be the quadratic-residue tournament on \(\mathbb Z_q\):
\[
x\to y\quad\Longleftrightarrow\quad y-x\in R_q,
\]
where
\[
\begin{aligned}
R_3&=\{1\},\\
R_7&=\{1,2,4\},\\
R_{11}&=\{1,3,4,5,9\},\\
R_{19}&=\{1,4,5,6,7,9,11,16,17\}.
\end{aligned}
\]

Translations and multiplication by a nonzero quadratic residue are automorphisms. In particular, these tournaments are arc-transitive.

### \(P_7\) is \(T_4\)-free

The outneighborhood of \(0\) is \(\{1,2,4\}\), which induces
\[
1\to2\to4\to1.
\]
A transitive four-set would have a source whose other three vertices induce \(T_3\), which is impossible.

After reversing \(0\to1\), the vertices
\[
1,3,5,0
\]
occur in transitive order. Hence every arc reversal creates \(T_4\).

### \(P_{11}\) is \(T_5\)-free

The outneighborhood of \(0\) is \(R_{11}\). Within this set the outneighborhoods are
\[
\begin{array}{c|c}
1&\{4,5\}\\
3&\{1,4\}\\
4&\{5,9\}\\
5&\{3,9\}\\
9&\{1,3\}.
\end{array}
\]
Thus no vertex of \(P_{11}[R_{11}]\) can be the source of a transitive four-set. Hence \(R_{11}\) contains no \(T_4\), and \(P_{11}\) contains no \(T_5\).

After reversing \(0\to1\), the sequence
\[
8,1,2,6,0
\]
is transitive. Arc-transitivity now shows that reversing any arc creates \(T_5\).

### \(P_{19}\) is \(T_6\)-free

Let \(R=R_{19}=N^+(0)\). The outneighbors of \(1\) within \(R\) are
\[
B=\{5,6,7,17\}.
\]
This four-set is not transitive, since
\[
5\to6\to17\to5.
\]

For every \(r\in R\), multiplication by \(r^{-1}\) maps the outneighborhood of \(r\) within \(R\) isomorphically onto \(B\). Therefore every vertex of \(P_{19}[R]\) has exactly four outneighbors there, and those four do not induce \(T_4\). It follows that \(R\) contains no \(T_5\): the source of such a \(T_5\) would have its four remaining vertices equal to its entire outneighborhood, which is nontransitive. Consequently \(P_{19}\) contains no \(T_6\).

After reversing \(0\to1\), the sequence
\[
14,1,12,2,18,0
\]
is transitive. Indeed, all forward differences are in \(R_{19}\), except \(0-1\), whose direction is supplied by the reversal. Thus every arc reversal creates \(T_6\).

Finally, \(P_3=C_3\) is the familiar finite host for \(T_3\).

We have therefore proved:

**Proposition 8.** The transitive tournaments \(T_h\) admit finite nonvacuous arc-reversal-saturated hosts for
\[
h=3,4,5,6.
\]

I do not have a construction covering all \(h\geq7\).

# 7. Exact finite SAT formulation

For computational investigation, finite hosts can be searched for without any ambiguity.

Fix \(H\) on \([h]\) and a proposed host order \(N\). For each \(1\leq i<j\leq N\), introduce a variable \(x_{ij}\), interpreted as \(i\to j\). Let \(L(i,j)\) be the corresponding literal asserting \(i\to j\).

For every injection \(\phi:V(H)\hookrightarrow[N]\), add the \(H\)-freeness clause
\[
\bigvee_{a\to b\in A(H)}
 \neg L(\phi(a),\phi(b)).
\]

For each unordered host pair \(p=\{u,v\}\), and every injection \(\phi\) together with an arc \(a\to b\) of \(H\) satisfying
\[
\{\phi(a),\phi(b)\}=p,
\]
introduce a witness variable \(y_{p,\phi,a b}\). Add implications
\[
y_{p,\phi,a b}\Longrightarrow
 \neg L(\phi(a),\phi(b))
\]
and, for every other arc \(c\to d\) of \(H\),
\[
y_{p,\phi,a b}\Longrightarrow
 L(\phi(c),\phi(d)).
\]
Finally add
\[
\bigvee_{\phi,a b} y_{p,\phi,a b}
\]
for every host pair \(p\).

A satisfying assignment is exactly an \(N\)-vertex \(H\)-free tournament in which every arc reversal creates \(H\). This gives a reproducible route for investigating the remaining small targets.

# 8. What remains open in this attack

The arguments above do not give the requested full characterization. In particular:

- the safe-amalgamation theorem does not cover tournaments having a vertex cut of size at most two, unless they pass the sharper rooted test;
- targets not one reversal away from a transitive tournament and failing that safety test remain untreated;
- for transitive targets, infinite hosts are impossible, and the finite existence question remains unresolved here for \(T_h\) with \(h\geq7\);
- the rooted safety condition is only sufficient, not necessary, since a host may use much more complicated amalgamations than the one-way construction above.