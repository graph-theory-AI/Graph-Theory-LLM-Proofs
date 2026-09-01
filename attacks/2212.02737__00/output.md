```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "The literal question is answered by the published array criterion: the H-free class is clean exactly when H-free n-arrays exist for only finitely many n.",
  "would_publish": false,
  "caveats": "This is not a direct finite structural classification of the forbidden family, and no new proof of the deep array theorem is given here."
}
```

# Mathematical writeup

## 1. Formulation

Write \(J\leq_{\mathrm{ind}}G\) when \(J\) is isomorphic to an induced subgraph of \(G\), and put
\[
\mathcal C_{\mathcal H}
 =\operatorname{Forb}_{\mathrm{ind}}(\mathcal H)
 =\{G: H\not\leq_{\mathrm{ind}}G\text{ for every }H\in\mathcal H\}.
\]

The question asks which finite families \(\mathcal H\) have the property that \(\mathcal C_{\mathcal H}\) is clean, with cleanliness defined as in the prompt.

There are two readings:

1. A literal necessary-and-sufficient characterization.
2. A finite, intrinsic structural characterization analogous to the singleton result “\(H\) is a subdivided star forest.”

The first has been resolved; the second is not supplied by the known theorem.

## 2. The published exact characterization

For each \(n\), let \(\mathscr A_n\) denote the class of \(n\)-arrays in the sense of Alecu–Chudnovsky–Hajebi–Spirkl, and define
\[
S(\mathcal H)
 =\{n\in\mathbb N:\text{there exists an \(n\)-array whose underlying graph lies in }
 \mathcal C_{\mathcal H}\}.
\]

Theorem 1.4 of their paper *Induced subgraphs and tree decompositions XIII. Basic obstructions in \(\mathcal H\)-free graphs for finite \(\mathcal H\)*, arXiv:2311.05066, published in *Advances in Combinatorics*, states:

\[
\boxed{
\mathcal C_{\mathcal H}\text{ is clean}
\quad\Longleftrightarrow\quad
S(\mathcal H)\text{ is finite}.
}
\]

Equivalently,
\[
\mathcal C_{\mathcal H}\text{ is clean}
\quad\Longleftrightarrow\quad
\exists N\ \forall n\geq N\ \forall A\in\mathscr A_n\
\exists H\in\mathcal H\text{ such that }H\leq_{\mathrm{ind}}A.
\]

This theorem has exactly the hypotheses of the question—namely, \(\mathcal H\) is finite—and uses the same notion of cleanliness. Thus it settles the literal question without reducing it to an unproved conjecture.

I am invoking the published theorem rather than reproducing its substantial proof. The prompt does not provide the full definition of an \(n\)-array, so I do not attempt to reconstruct it from memory.

## 3. Elementary structural consequences

The array theorem is exact but asymptotic. Some direct consequences in terms of the forbidden graphs themselves can nevertheless be recorded.

### Lemma 3.1: Cleanliness is inherited by subclasses

If \(\mathcal D\subseteq\mathcal C\) and \(\mathcal C\) is clean, then \(\mathcal D\) is clean.

#### Proof

For each \(t\), use the same bound \(w_{\mathcal C}(t)\). Every graph in \(\mathcal D\) is also in \(\mathcal C\), so the defining conclusion for cleanliness remains valid. \(\square\)

### Lemma 3.2: Redundant forbidden graphs may be deleted

If \(H_1,H_2\in\mathcal H\) and \(H_1\leq_{\mathrm{ind}}H_2\), then \(H_2\) is redundant:
\[
\operatorname{Forb}_{\mathrm{ind}}(\mathcal H)
 =
\operatorname{Forb}_{\mathrm{ind}}(\mathcal H\setminus\{H_2\}).
\]

Indeed, any induced copy of \(H_2\) contains an induced copy of \(H_1\).

Consequently, if \(\min_{\mathrm{ind}}(\mathcal H)\) is the set of induced-subgraph-minimal members of \(\mathcal H\), then
\[
\mathcal C_{\mathcal H}
 =\mathcal C_{\min_{\mathrm{ind}}(\mathcal H)}.
\]
Thus the genuinely collective cases occur when the reduced forbidden family is an induced-subgraph antichain.

### Proposition 3.3: Two direct tests

Let \(\mathsf{SSF}\) be the class of subdivided star forests.

1. If \(\mathcal H\cap\mathsf{SSF}\neq\varnothing\), then \(\mathcal C_{\mathcal H}\) is clean.
2. If there is a graph \(J\notin\mathsf{SSF}\) such that
   \[
   J\leq_{\mathrm{ind}}H\qquad\text{for every }H\in\mathcal H,
   \]
   then \(\mathcal C_{\mathcal H}\) is not clean.

#### Proof

For the first assertion, choose \(F\in\mathcal H\cap\mathsf{SSF}\). Then
\[
\mathcal C_{\mathcal H}\subseteq\operatorname{Forb}_{\mathrm{ind}}(F).
\]
The singleton theorem from Part VII says that \(\operatorname{Forb}_{\mathrm{ind}}(F)\) is clean. Lemma 3.1 gives the result.

For the second assertion, every \(J\)-free graph is \(\mathcal H\)-free: if a \(J\)-free graph contained some \(H\in\mathcal H\), transitivity of induced containment would give an induced copy of \(J\). Hence
\[
\operatorname{Forb}_{\mathrm{ind}}(J)\subseteq\mathcal C_{\mathcal H}.
\]
Since \(J\) is not a subdivided star forest, the singleton theorem says that \(\operatorname{Forb}_{\mathrm{ind}}(J)\) is not clean. If \(\mathcal C_{\mathcal H}\) were clean, Lemma 3.1 would force its subclass \(\operatorname{Forb}_{\mathrm{ind}}(J)\) to be clean, a contradiction. \(\square\)

Thus a necessary condition for cleanliness is
\[
\bigcap_{H\in\mathcal H}
 \{J:J\leq_{\mathrm{ind}}H\}
 \subseteq \mathsf{SSF}.
\]
This is a finite, effectively checkable necessary condition, though it is not sufficient.

### Corollary 3.4: Families with a least forbidden graph

Suppose there is \(H_0\in\mathcal H\) such that
\[
H_0\leq_{\mathrm{ind}}H\qquad\text{for every }H\in\mathcal H.
\]
Then
\[
\mathcal C_{\mathcal H}
 =\operatorname{Forb}_{\mathrm{ind}}(H_0),
\]
and hence
\[
\boxed{
\mathcal C_{\mathcal H}\text{ is clean}
\quad\Longleftrightarrow\quad
H_0\text{ is a subdivided star forest}.
}
\]

In particular, this completely handles finite families that are chains under induced-subgraph containment.

## 4. Why a simpler memberwise criterion cannot work

The example in the prompt,
\[
\mathcal H=\{D,K_3\},
\]
where \(D\) is the six-vertex double star with two adjacent degree-three vertices, shows that
\[
\mathcal H\cap\mathsf{SSF}=\varnothing
\]
does not imply non-cleanliness. Neither \(D\) nor \(K_3\) is a subdivided star forest, yet their joint forbidden class is clean.

The common-induced-subgraph obstruction above also does not settle this example. Any graph induced in both \(D\) and \(K_3\) is among the empty graph, \(K_1\), and \(K_2\), all of which are subdivided star forests. Thus the cleanliness is genuinely caused by interaction between incomparable forbidden graphs.

## 5. Remaining gap under the stronger interpretation

The array theorem is a complete mathematical characterization, but it does not by itself give:

- a finite list of allowed forms for the members of \(\mathcal H\);
- a criterion comparable in simplicity to the singleton subdivided-star-forest theorem;
- an explicit decision algorithm or complexity bound for testing a finite input family;
- a bound \(N=N(\mathcal H)\) whose existence can be checked from elementary invariants of the forbidden graphs.

The supplied literature review also mentions “tasselled” families, but does not state enough of that result to justify claiming a simpler equivalence here.

Accordingly, the literal question is already resolved by the published array theorem. If “for which families” is intended to demand an intrinsic finite structural description, then the present answer is only partial: the elementary tests above handle nested families and provide a common-induced-obstruction criterion, but they do not classify induced-antichain families such as \(\{D,K_3\}\).