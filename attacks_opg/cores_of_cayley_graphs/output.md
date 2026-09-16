```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For M = Z/4Z, the Cayley graph C4 has core K2, which cannot be a Cayley graph on any direct power of M.",
  "would_publish": false,
  "caveats": "This disproves the literal fixed-base direct-power formulation, not the cubelike conjecture or the version allowing a different abelian group."
}
```

## 1. The fixed-base formulation has a counterexample

Use the standard convention that \(\operatorname{Cay}(G,S)\) has vertex set **all of \(G\)**. The assertion as written would require that, for each fixed abelian group \(M\),
\[
X=\operatorname{Cay}(M^n,S)
\quad\Longrightarrow\quad
\operatorname{core}(X)\cong\operatorname{Cay}(M^r,T)
\]
for some nonnegative integer \(r\).

Take
\[
M=\mathbb Z/4\mathbb Z,\qquad S=\{1,3\}.
\]
Then
\[
X=\operatorname{Cay}(M,S)
\]
is the four-cycle
\[
0-1-2-3-0.
\]

### Its core is \(K_2\)

The vertices \(\{0,1\}\) induce an edge. Define
\[
\rho:V(X)\longrightarrow\{0,1\},
\qquad
\rho(0)=\rho(2)=0,\quad
\rho(1)=\rho(3)=1.
\]
Every edge of \(X\) joins an even residue to an odd residue, so \(\rho\) is a graph homomorphism. It fixes \(0\) and \(1\), making it a retraction onto this induced \(K_2\).

Moreover, \(K_2\) is a core: a homomorphism of a loopless graph cannot identify the endpoints of an edge, so every endomorphism of \(K_2\) is an automorphism. Consequently,
\[
\operatorname{core}(X)\cong K_2.
\]

### This core cannot be a Cayley graph on a power of \(M\)

Every Cayley graph on \(M^r\) has
\[
|M^r|=4^r
\]
vertices. There is no nonnegative integer \(r\) satisfying \(4^r=2\). Thus \(K_2\) is not a Cayley graph on any direct power of this fixed \(M\).

This is a counterexample to the literal statement, already with a connected graph on four vertices.

## 2. The obstruction applies to every finite abelian group of composite order

The example is not specific to the cyclic group of order four.

**Proposition.** Let \(M\) be a finite abelian group of composite order. There is a connected Cayley graph on \(M\) whose core is not a Cayley graph on any direct power of \(M\).

**Proof.** Choose a maximal proper subgroup \(H<M\). Because \(M\) is finite abelian,
\[
M/H\cong\mathbb Z/p\mathbb Z
\]
for some prime \(p\). Put
\[
S=M\setminus H.
\]
This set excludes \(0\) and is closed under negation, so it defines a simple undirected Cayley graph.

Two vertices \(x,y\in M\) are adjacent precisely when
\[
y-x\notin H,
\]
equivalently, when they belong to different cosets of \(H\). Hence \(\operatorname{Cay}(M,S)\) is a complete \(p\)-partite graph with parts of size \(|H|\).

Choose one representative from each coset. These representatives induce \(K_p\), and sending every vertex to its coset representative is a retraction onto that clique. Since \(K_p\) is a core, the graph has core \(K_p\).

But \(p<|M|\), since \(|M|\) is composite. Therefore
\[
p\ne |M|^r
\qquad\text{for every integer }r\ge 0,
\]
so this core cannot be a Cayley graph on any direct power of \(M\). \(\square\)

Thus a nontrivial finite abelian group satisfying the literal universal assertion would necessarily have **prime order**.

## 3. Scope and the intended open question

There is an important distinction between the supplied fixed-base formulation and the substantive cubelike question.

- The example does **not** refute the assertion that the core of an abelian Cayley graph is a Cayley graph on *some abelian group*: \(K_2\) is Cayley on \(\mathbb Z/2\mathbb Z\).
- It does **not** refute the cubelike conjecture: both \(C_4\) and \(K_2\) are Cayley graphs on powers of \(\mathbb Z/2\mathbb Z\).
- It does refute the requirement that the core be Cayley on a direct power of the **same arbitrary fixed group** \(M\).

There is no gap in the counterexample under the ordinary definition of a Cayley graph. However, if the intended formulation permits a subgroup or quotient of a power of \(M\), or permits changing the abelian group, then this argument does not settle that formulation. The supplied wording therefore needs that distinction before its claimed open status can be applied.