```json
{
  "verdict": "ill_posed",
  "confidence": "high",
  "one_line": "The catalog item is a research direction rather than a proposition, since “near-extremal,” “large piece,” and “based on a projective plane” have no specified quantitative meanings.",
  "would_publish": false,
  "caveats": "The auxiliary results below require linearity and balanced part sizes and do not settle an additive-stability formulation."
}
```

# Mathematical writeup

## 1. Status of the stated problem

Let \(H\) be an \(r\)-partite \(r\)-uniform hypergraph with parts
\[
V_1,\dots,V_r,
\]
so every edge contains exactly one vertex from each part. It is intersecting if every two edges meet, and \(\tau(H)\) is its minimum vertex-cover size.

The extracted statement is not a mathematical proposition with a truth value. At least the following data are missing.

1. **Meaning of near-extremal.** Natural inequivalent possibilities include
   \[
   \tau(H)\ge r-C,\qquad \tau(H)\ge (1-\varepsilon)r,
   \qquad\text{or}\qquad \tau(H)=r-1.
   \]
   The first is the scale suggested by the source paper; the second admits substantially more examples.

2. **Meaning and scale of a large piece.** This could mean:
   - an exact subhypergraph isomorphic to a truncated projective plane;
   - such a subhypergraph on \(\Omega(r)\) parts;
   - a projective-plane restriction of unbounded order;
   - edit-distance \(o(|E(H)|)\) from a plane construction;
   - a union or gluing of several plane fragments.

   These conditions are not equivalent.

3. **Meaning of “based on” a projective plane.** This is partly a statement about how an object was discovered, not an isomorphism-invariant property. A construction can have both geometric and non-geometric descriptions.

4. **Normalization.** Adding arbitrarily many isolated vertices to every part preserves intersection and \(\tau(H)\), but destroys any assertion that a positive proportion of all vertices lies in a geometric piece.

Thus neither a proof nor a counterexample to the prose statement is possible without first selecting a formalization. The rest of the writeup gives rigorous reformulations and partial structural results.

---

## 2. Exact reformulation as a system of partitions

Let \(X=E(H)\). For each vertex \(v\), define
\[
B_v=\{e\in X:v\in e\}.
\]
For each part \(V_i\), the nonempty sets
\[
\mathcal P_i=\{B_v:v\in V_i,\ B_v\ne\varnothing\}
\]
form a partition of \(X\), since every hyperedge uses exactly one vertex of \(V_i\).

Under this translation:

- \(H\) is intersecting precisely when every pair of elements of \(X\) lies together in a cell of at least one partition \(\mathcal P_i\).
- \(H\) is linear precisely when every pair of elements of \(X\) lies together in exactly one such cell.
- A vertex cover of \(H\) is a collection of cells whose union is \(X\).

Thus the problem can be viewed as asking for pair-covering systems of \(r\) partitions whose block-cover number is close to \(r\).

### Resolvable Steiner designs

This gives a broad exact construction.

**Proposition 2.1.**  
Suppose \((X,\mathcal B)\) is a resolvable Steiner \(2\)-design with parameters \(2\!-\!(v,k,1)\). Then there is a linear intersecting \(r\)-partite \(r\)-uniform hypergraph \(H\) satisfying
\[
r=\frac{v-1}{k-1},
\qquad
\tau(H)=\frac vk.
\]

**Proof.**
The blocks are partitioned into parallel classes, each of which partitions \(X\). Make one hypergraph part for each parallel class, with the blocks in that class as its vertices. For every point \(x\in X\), form the hyperedge consisting of the unique block from each parallel class containing \(x\).

Every two points lie in a unique design block, so every two hyperedges meet in exactly one vertex. Hence the resulting hypergraph is linear and intersecting.

A hypergraph vertex corresponds to a \(k\)-set in \(X\). Therefore fewer than \(v/k\) vertices cannot cover all \(v\) point-hyperedges. Conversely, the \(v/k\) blocks of one parallel class cover all points. Hence \(\tau(H)=v/k\). Finally, the number of parallel classes equals the replication number \((v-1)/(k-1)\). ∎

The deficit in this construction is
\[
r-\tau(H)
 =\frac{v-1}{k-1}-\frac vk
 =\frac{v-k}{k(k-1)}.
\]
Consequently, obtaining exact fixed deficit \(C\) within this model amounts to finding resolvable designs with
\[
v=k\bigl(1+C(k-1)\bigr),
\qquad
r=Ck+1,
\qquad
\tau(H)=r-C.
\]
For \(C=1\), these are precisely the parameters of an affine plane of order \(k\). For \(C\ge2\), this is a concrete design-theoretic route to alternative constructions, but no non-geometric infinite family is proved here.

---

## 3. Why different natural interpretations give different answers

### 3.1 Exact full-rank containment is already false

Let \(T_q\) be the truncation of a projective plane of order \(q\) at a point. It has

\[
r=q+1,\qquad |E(T_q)|=q^2,\qquad d(v)=q,\qquad \tau(T_q)=q=r-1.
\]

Indeed, any part of \(q\) vertices is a cover, while \(q-1\) vertices cover at most \(q(q-1)<q^2\) edges.

Delete \(s\) hyperedges, where \(1\le s\le q-1\), and call the result \(H\). Then
\[
|E(H)|=q^2-s>q(q-1),
\]
and all vertex degrees are at most \(q\). Hence \(q-1\) vertices cover at most \(q(q-1)\) edges, so
\[
\tau(H)=q=r-1.
\]
However, \(H\) cannot contain a full copy of \(T_q\), simply because it has fewer than \(q^2\) edges.

Thus the formal assertion

> every \(r\)-partite intersecting \(H\) with \(\tau(H)=r-1\) contains a full truncated plane of rank \(r\)

is false. On the other hand, this example is at edit distance only \(s\) from a projective-plane construction, so it is not a counterexample to an edit-distance interpretation of “large piece.”

### 3.2 Relative near-extremality does not force a plane piece on \(\Omega(r)\) parts

Fix \(d\ge3\) and a prime power \(q\). Let \(X=\mathbb F_q^d\). For every one-dimensional subspace \(D\le\mathbb F_q^d\), partition \(X\) into the affine lines parallel to \(D\). Apply Proposition 2.1 to the affine lines.

There are
\[
r=\frac{q^d-1}{q-1}=q^{d-1}+q^{d-2}+\cdots+1
\]
directions, and each parallel class contains \(q^{d-1}\) lines. The associated hypergraph has
\[
\tau(H)=q^{d-1}.
\]
Indeed, every hypergraph vertex lies in exactly \(q\) point-hyperedges, so fewer than \(q^{d-1}\) vertices cannot cover the \(q^d\) edges, while one whole part does cover them.

Therefore, for fixed \(d\) and \(q\to\infty\),
\[
\frac{\tau(H)}r
 =\frac{q^{d-1}}{q^{d-1}+q^{d-2}+\cdots+1}
 \longrightarrow 1.
\]

Nevertheless, a truncated projective plane of order \(a\) has \(a^2\) hyperedges. Since the affine-space hypergraph has only \(q^d\) hyperedges, any exact truncated-plane subhypergraph must satisfy
\[
a^2\le q^d,
\qquad\text{so}\qquad
a\le q^{d/2}.
\]
Its rank is therefore at most \(q^{d/2}+1\), whereas the ambient rank is at least \(q^{d-1}\). For \(d\ge3\),
\[
\frac{q^{d/2}+1}{r}\longrightarrow0.
\]

Hence the following plausible formalization is false:

> If \(\tau(H)/r\to1\), then \(H\) contains a full truncated projective plane on \(\Omega(r)\) parts.

This does not address the additive condition \(\tau(H)\ge r-C\), since here
\[
r-\tau(H)=q^{d-2}+\cdots+1.
\]
Moreover, the construction itself comes from finite affine geometry and contains projective-plane restrictions of order \(q\). It therefore illustrates the ambiguity of “large” and “based on,” rather than resolving the source question.

---

## 4. A projective-plane characterization in the balanced linear equality case

The following gives a precise setting in which projective-plane structure is forced.

**Theorem 4.1.**  
Let \(q\ge2\), and let \(H\) be a linear intersecting \((q+1)\)-partite, \((q+1)\)-uniform hypergraph. Suppose every part has at most \(q\) vertices. Then
\[
|E(H)|\le q^2.
\]
If equality holds, then \(H\) is the truncation of a projective plane of order \(q\). In particular,
\[
\tau(H)=q.
\]

**Proof.**
Add isolated vertices so that every part has exactly \(q\) vertices. Let \(m=|E(H)|\) and \(d(v)\) denote vertex degrees.

Since \(H\) is both intersecting and linear, every two distinct hyperedges meet in exactly one vertex. Therefore
\[
\binom m2=\sum_v\binom{d(v)}2.
\]
For every part \(V_i\),
\[
\sum_{v\in V_i}d(v)=m.
\]
By Cauchy–Schwarz,
\[
\sum_{v\in V_i}d(v)^2\ge\frac{m^2}{q}.
\]
Summing over the \(q+1\) parts gives
\[
m(m-1)
 =\sum_v\bigl(d(v)^2-d(v)\bigr)
 \ge (q+1)\left(\frac{m^2}{q}-m\right).
\]
For \(m>0\), rearrangement yields
\[
m\le q^2.
\]

Suppose \(m=q^2\). Equality must hold in every Cauchy–Schwarz inequality, so every vertex has degree \(q\).

Each hyperedge realizes \(\binom{q+1}{2}\) pairs of vertices from distinct parts. No such vertex pair can occur in two hyperedges, by linearity. Since
\[
q^2\binom{q+1}{2}
\]
is exactly the total number of pairs of vertices from distinct parts, every such pair lies in a unique hyperedge.

Add a new point \(\infty\), and regard the following as lines:

- all hyperedges of \(H\);
- the \(q+1\) sets \(V_i\cup\{\infty\}\).

Two vertices in the same part lie on their part-line; two vertices in distinct parts lie on a unique hyperedge; and \(\infty\) lies with every vertex on a unique part-line. Dually, any two of these lines meet in exactly one point. Every line has \(q+1\) points. This is a projective plane of order \(q\), and \(H\) consists precisely of the lines not through \(\infty\), with the lines through \(\infty\) defining the parts.

Finally, one part is a cover of size \(q\). Since every vertex has degree \(q\), any \(q-1\) vertices cover at most \(q(q-1)<q^2\) edges. Thus \(\tau(H)=q\). ∎

### Quantitative degree stability

The same counting gives an exact defect identity.

**Proposition 4.2.**  
Under the hypotheses of Theorem 4.1, pad each part to size \(q\), write
\[
|E(H)|=q^2-s,
\]
and put \(a_v=q-d(v)\). Then
\[
\sum_{v\in V_i}a_v=s
\quad\text{for every part }V_i,
\]
and
\[
\sum_v a_v^2=s(q+s).
\]
If \(0\le s\le q\), all but at most
\[
\frac{s(s-1)}2
\]
parts have exactly \(s\) vertices of degree \(q-1\) and \(q-s\) vertices of degree \(q\).

**Proof.**
The pair-counting identity gives
\[
\sum_v d(v)^2=m^2+qm.
\]
Substituting \(m=q^2-s\) into
\[
\sum_v(q-d(v))^2
\]
gives \(s(q+s)\). Also, in every part,
\[
\sum_{v\in V_i}(q-d(v))=q^2-m=s.
\]

For a part \(V_i\), define
\[
E_i=\sum_{v\in V_i}\bigl(a_v^2-a_v\bigr)
   =\sum_{v\in V_i}a_v(a_v-1).
\]
Since \(a_v\) is integral, every summand is a nonnegative even integer. Moreover,
\[
\sum_i E_i
 =s(q+s)-(q+1)s
 =s(s-1).
\]
Thus at most \(s(s-1)/2\) parts have \(E_i>0\). If \(E_i=0\), every \(a_v\in\{0,1\}\), and their sum is \(s\), giving the stated degree sequence. ∎

### The one-missing-edge case is completely rigid

**Corollary 4.3.**  
If \(H\) satisfies the hypotheses of Theorem 4.1 and has \(q^2-1\) edges, then there is a unique transversal edge whose addition turns \(H\) into a truncated projective plane of order \(q\). Moreover, \(\tau(H)=q\).

**Proof.**
Set \(s=1\) in Proposition 4.2. In each part \(V_i\), there is a unique vertex \(u_i\) of degree \(q-1\); every other vertex has degree \(q\).

For two distinct parts \(V_i,V_j\), the \(q^2-1\) hyperedges realize \(q^2-1\) distinct pairs from \(V_i\times V_j\). The unique omitted pair must be \((u_i,u_j)\). Consequently, no existing edge contains two of the vertices \(u_i\).

Let
\[
e^\ast=\{u_i:1\le i\le q+1\}.
\]
Every existing edge meets \(e^\ast\) at most once, while
\[
\sum_{e\in E(H)}|e\cap e^\ast|
 =\sum_i d(u_i)
 =(q+1)(q-1)
 =q^2-1
 =|E(H)|.
\]
Hence every existing edge meets \(e^\ast\) exactly once. Adding \(e^\ast\) preserves linearity and intersection and produces \(q^2\) edges. Theorem 4.1 now reconstructs a projective plane.

All degrees in \(H\) are at most \(q\), so \(q-1\) vertices cover fewer than \(q^2-1\) edges, while one part of size \(q\) is a cover. Thus \(\tau(H)=q\). ∎

This is a genuine, albeit narrow, stability result: in the balanced linear model, one missing hyperedge is forced to be a missing line of a projective-plane truncation. For fixed larger \(s\), Proposition 4.2 gives strong degree stability but does not prove that the missing edges can be coherently completed.

---

## 5. Remaining gaps

The results above do not resolve the intended source problem.

1. The hypothesis \(\tau(H)\ge r-C\) alone does not imply linearity, balanced part sizes, or edge count close to \((r-1)^2\).
2. Theorem 4.1 and Corollary 4.3 concern edge-density equality or near-equality, not covering-number stability in general.
3. The affine-space construction only treats relative near-extremality and is itself geometric.
4. Proposition 2.1 identifies a precise design-theoretic route to fixed additive deficit, but no infinite non-projective family is constructed here.
5. Most importantly, no formal definition of a projective-plane “piece” or of being “based on” such a plane is supplied.

A viable formal version would need to fix a constant \(C\), remove isolated vertices, specify whether linearity is assumed, and define a plane piece by an explicit embedding or edit-distance condition together with a quantitative lower bound on its order. Without these choices, the catalog item remains a legitimate research programme but not an adjudicable conjecture.