```json
{
  "verdict": "already_resolved",
  "confidence": "medium",
  "one_line": "Assuming the catalog's stated 2026 result is accurate, polynomial-time recognition puts weightability in P and hence in NP, while independently weightability is equivalent to admitting a 0–1 edge set meeting every directed cycle exactly once.",
  "would_publish": false,
  "caveats": "The cited 2026 preprint and its bit-model algorithm were not independently checked, and its construction operations are not reproduced here."
}
```

## 1. Statement and interpretation

For a finite digraph \(D=(V,E)\), let
\[
L_{\mathrm{wt}}
 =\left\{\langle D\rangle:
 \exists w\in\mathbb R^E\ \text{such that } \sum_{e\in E(C)}w(e)=1
 \text{ for every directed simple cycle }C\right\}.
\]

There are two related readings of the question:

1. **Formal complexity reading:** Is \(L_{\mathrm{wt}}\in\mathrm{NP}\)?
2. **Structural reading:** Is there a sound and complete generative construction whose derivations are polynomially verifiable?

The supplied catalog metadata reports a later result giving both hierarchical constructions and a polynomial-time recognition algorithm. The latter alone settles the formal complexity question.

Indeed, if \(A\) is a deterministic polynomial-time algorithm deciding weightability, define an NP verifier by
\[
V(D,y)=
\begin{cases}
A(D),&y=\epsilon,\\
\text{reject},&y\ne\epsilon.
\end{cases}
\]
Thus
\[
L_{\mathrm{wt}}\in\mathrm P\subseteq\mathrm{NP}.
\]
No separate positive certificate is required. Consequently, uncertainty about whether the reported construction itself has polynomially bounded derivations does not affect the formal NP conclusion.

The two structural assertions reported in the prompt also compose formally: if every weightable digraph is constructed from planar weightable digraphs, and every planar weightable digraph is constructed from circular digraphs, then substituting the latter derivations into the former gives a construction from circular digraphs for every weightable digraph. I cannot check soundness, completeness, or the exact operations without the full follow-up paper.

## 2. A self-contained discrete characterization

The following removes any issue concerning irrational or large rational weights.

### Theorem

For a finite loopless digraph \(D\), the following are equivalent.

1. \(D\) is weightable over \(\mathbb R\).
2. There is a set \(F\subseteq E(D)\) such that
   \[
   |F\cap E(C)|=1
   \]
   for every directed cycle \(C\).
3. In every strongly connected component containing a cycle, there is a linear order of its vertices in which every directed cycle has exactly one backward edge.

Thus every weightable digraph has a valid weighting taking only the values \(0\) and \(1\).

Loops, if allowed, can be treated separately: every loop is itself a cycle and must receive weight \(1\).

### Proof

It suffices to work separately in the strongly connected components, since every directed cycle is contained in one strongly connected component. Edges between distinct components may be given weight \(0\).

Let \(S\) be strongly connected and let \(c:E(S)\to\mathbb R\) satisfy
\[
c(C)=1
\]
for every directed cycle \(C\).

#### Step 1: \(c\) is cohomologous to an integer weighting

Let
\[
L=\{z\in\mathbb Z^{E(S)}:Bz=0\}
\]
be the lattice of integral circulations, where \(B\) is the incidence matrix.

Every arc of \(S\) lies on a directed cycle. For each arc \(e\), choose such a cycle \(C_e\), and put
\[
q=\sum_{e\in E(S)}\chi_{C_e}.
\]
Then \(q\in L\) and every coordinate of \(q\) is positive.

For any \(z\in L\), choose \(N\) sufficiently large that \(z+Nq\ge 0\). Both \(z+Nq\) and \(Nq\) are nonnegative integral circulations. Every nonnegative integral circulation decomposes into incidence vectors of directed simple cycles. Hence
\[
c\cdot(z+Nq)\in\mathbb Z,\qquad c\cdot Nq\in\mathbb Z,
\]
because \(c\) has value \(1\) on each directed cycle. Therefore
\[
c\cdot z\in\mathbb Z \qquad\text{for all }z\in L. \tag{1}
\]

Choose a spanning tree \(T\) of the underlying undirected graph of \(S\). Adding a vertex potential does not change cycle sums: for \(p:V(S)\to\mathbb R\), define
\[
c^p(uv)=c(uv)+p(u)-p(v).
\]
Choose \(p\) so that \(c^p(e)=0\) for every tree edge \(e\in T\).

For each non-tree arc \(e\), let \(z_e\in L\) be the signed fundamental circulation consisting of \(e\) and the tree path joining its endpoints, with coefficient \(1\) on \(e\). Since all tree-edge weights under \(c^p\) vanish,
\[
c^p(e)=c^p\cdot z_e=c\cdot z_e\in\mathbb Z
\]
by (1). Therefore \(c^p\) is integer-valued on every arc.

#### Step 2: Make the integer weighting nonnegative

Every directed cycle has \(c^p\)-weight \(1\), so there is no negative directed cycle. Add an auxiliary source with zero-cost arcs to every vertex and let \(d(v)\) be the shortest-path distance to \(v\) under \(c^p\). These distances are finite integers.

For an arc \(uv\), define the reduced weight
\[
r(uv)=c^p(uv)+d(u)-d(v).
\]
The shortest-path inequalities give \(r(uv)\ge0\). Moreover, \(r\) differs from \(c^p\) by a potential, so every directed cycle still has weight \(1\).

Every arc \(e\) of a strongly connected digraph lies on a directed simple cycle \(C_e\). Hence
\[
0\le r(e)\le r(C_e)=1.
\]
Since \(r(e)\) is an integer,
\[
r(e)\in\{0,1\}.
\]

Let
\[
F=\{e:r(e)=1\}.
\]
For every directed cycle \(C\),
\[
1=r(C)=|F\cap E(C)|.
\]
This proves \(1\Rightarrow2\). The implication \(2\Rightarrow1\) follows immediately by assigning weight \(1\) to \(F\) and \(0\) elsewhere.

#### Step 3: Ordering formulation

Assume \(F\) meets every directed cycle exactly once. Then \(S-F\) is acyclic, so take a topological order of \(S-F\).

Every \(f=uv\in F\) lies on a directed cycle. Since \(f\) is the unique member of \(F\) on that cycle, deleting \(f\) leaves a directed \(v\)-to-\(u\) path in \(S-F\). Thus \(v\) precedes \(u\), so \(f\) is backward in the topological order. All edges outside \(F\) are forward. Therefore every directed cycle has exactly one backward edge.

Conversely, assigning weight \(1\) to the backward edges and \(0\) to the forward edges proves weightability whenever such an order exists. This proves the theorem. ∎

## 3. What this does and does not give algorithmically

The theorem gives a particularly concrete reformulation:

> A digraph is weightable exactly when it has an **exact feedback arc set**—an edge set meeting every directed cycle exactly once.

It also shows that the use of arbitrary real weights creates no bit-complexity problem: a positive instance always has a binary weighting.

However, the set \(F\) alone is not automatically a conventional NP certificate. Given \(F\),

- checking that every cycle meets \(F\) at least once is easy: test that \(D-F\) is acyclic;
- checking that no directed simple cycle contains two or more edges of \(F\) remains a universal condition.

Thus the binary normalization by itself does not prove membership in NP. This is precisely where a polynomial recognition algorithm or a polynomially verifiable structural decomposition is needed.

For completeness, nonweightability has an elementary short certificate. Let \(A\) be the matrix whose rows are the incidence vectors of directed cycles. Weightability is the feasibility of
\[
Aw=\mathbf 1.
\]
If this system is infeasible, some subsystem of at most \(m+1\) equations is already infeasible, where \(m=|E(D)|\). Therefore one can list at most \(m+1\) directed cycles and verify by rational Gaussian elimination that their equations are inconsistent. This recovers the co-NP side without enumerating all cycles.

## 4. Status and remaining gap

Taking the catalog’s report at face value, the later polynomial-time recognition theorem gives
\[
L_{\mathrm{wt}}\in\mathrm P\subseteq\mathrm{NP},
\]
so the formal NP-characterization question is already answered affirmatively. The reported pair of hierarchical constructions appears also to answer the structural version.

What is not supplied here is a verification of that later theorem: I have not inspected the preprint, its construction rules, or whether “polynomial-time” is proved in the standard Turing bit model. Without that external result, the self-contained contribution above is only a reduction to exact cycle transversals, not a complete NP characterization.