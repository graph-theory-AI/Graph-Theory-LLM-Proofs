```json
{
  "verdict": "already_resolved",
  "confidence": "high",
  "one_line": "A theorem of Alecu, Bonnet, Bureo Villafana, and Trotignon implies that every proper hereditary candidate obstruction family fails, so the only universal hereditary core is the tautological class of all graphs.",
  "would_publish": false,
  "caveats": "Question 1.1 is open-ended; the negative resolution concerns the universal hereditary-core formulation, while restricted-class structure theory remains open."
}
```

## 1. Precise formulation

All graphs below are finite and simple. Write \(H\leq_i G\) when \(H\) is isomorphic to an induced subgraph of \(G\), and set
\[
\operatorname{Forb}_i(H)=\{G:H\not\leq_i G\}.
\]
For a graph class \(\mathcal C\), write
\[
\operatorname{tw}(\mathcal C)=\sup_{G\in\mathcal C}\operatorname{tw}(G).
\]

Question 1.1 is not literally a proposition: “unavoidable” and “large” require quantifiers. The natural Grid-Theorem-style formulation is the following.

A family \(\mathcal A\) is an **induced treewidth detector** if
\[
\tag{D}
\forall k\ \exists N(k)\ \forall G,\qquad
\operatorname{tw}(G)\geq N(k)
\Longrightarrow
\exists F\leq_i G
\quad
\bigl(F\in\mathcal A,\ \operatorname{tw}(F)\geq k\bigr).
\]
Thus large treewidth forces an induced member of \(\mathcal A\) having large treewidth.

For hereditary classes, an equivalent class-level objective is a **universal hereditary core**: a hereditary class \(\mathcal U\) such that for every hereditary class \(\mathcal C\),
\[
\tag{UC}
\operatorname{tw}(\mathcal C)=\infty
\Longrightarrow
\operatorname{tw}(\mathcal C\cap\mathcal U)=\infty.
\]
Because \(\mathcal C\) is hereditary, every induced subgraph extracted from a member of \(\mathcal C\) remains in \(\mathcal C\). This is the formalization under which a single hereditary family would play the role of the walls in the Grid Minor Theorem.

## 2. The later theorem

Theorem 1.1 of Alecu, Bonnet, Bureo Villafana, and Trotignon, *Every Graph is Essential to Large Treewidth*, arXiv:2502.14775, states:

> **Essential-graph theorem.** For every finite graph \(H\), there exists a hereditary weakly sparse class \(\mathcal C_H\) such that
> \[
> \operatorname{tw}(\mathcal C_H)=\infty
> \]
> but
> \[
> \operatorname{tw}\bigl(\mathcal C_H\cap\operatorname{Forb}_i(H)\bigr)<\infty.
> \]

Equivalently, there is an integer \(b_H\) such that every \(H\)-free graph in \(\mathcal C_H\) has treewidth at most \(b_H\), while \(\mathcal C_H\) itself contains graphs of arbitrarily large treewidth.

The weak sparsity of \(\mathcal C_H\) is not needed for the deduction below, but shows that the phenomenon is not caused merely by dense graphs.

## 3. No proper hereditary universal core

### Corollary

A hereditary class \(\mathcal U\) satisfies (UC) if and only if \(\mathcal U\) is the class of all finite graphs.

### Proof

The class of all graphs plainly satisfies (UC).

Conversely, suppose that \(\mathcal U\) is proper and hereditary. Choose a graph
\[
H\notin\mathcal U.
\]
Since \(\mathcal U\) is hereditary, no graph in \(\mathcal U\) can contain \(H\) as an induced subgraph: otherwise heredity would imply \(H\in\mathcal U\). Hence
\[
\mathcal U\subseteq\operatorname{Forb}_i(H).
\]

Apply the essential-graph theorem to \(H\). It gives a hereditary class \(\mathcal C_H\) with unbounded treewidth but
\[
\operatorname{tw}\bigl(\mathcal C_H\cap\operatorname{Forb}_i(H)\bigr)<\infty.
\]
Since \(\mathcal U\subseteq\operatorname{Forb}_i(H)\),
\[
\mathcal C_H\cap\mathcal U
\subseteq
\mathcal C_H\cap\operatorname{Forb}_i(H),
\]
and therefore
\[
\operatorname{tw}(\mathcal C_H\cap\mathcal U)<\infty.
\]
Thus \(\mathcal C_H\) violates (UC). Hence no proper hereditary \(\mathcal U\) is universal. ∎

This covers every proper hereditary candidate, not merely finite lists of the previously known basic and non-basic obstruction types.

## 4. Consequence for arbitrary proposed obstruction families

For an arbitrary, not necessarily hereditary family \(\mathcal A\), define its induced closure by
\[
\downarrow_i\mathcal A
=
\{H:\text{there exists }A\in\mathcal A\text{ with }H\leq_i A\}.
\]

### Proposition

If \(\downarrow_i\mathcal A\) is a proper class, then \(\mathcal A\) does not satisfy the detector property (D).

### Proof

Choose
\[
H\notin\downarrow_i\mathcal A.
\]
Consequently, every member of \(\mathcal A\) is \(H\)-free.

Let \(\mathcal C_H\) and \(b_H\) be supplied by the essential-graph theorem. Set \(k=b_H+1\). For every integer \(N\), unboundedness of \(\operatorname{tw}(\mathcal C_H)\) gives a graph \(G\in\mathcal C_H\) with
\[
\operatorname{tw}(G)\geq N.
\]
If \(F\leq_i G\) and \(F\in\mathcal A\), then heredity of \(\mathcal C_H\) gives \(F\in\mathcal C_H\), while the choice of \(H\) gives \(F\in\operatorname{Forb}_i(H)\). Therefore
\[
\operatorname{tw}(F)\leq b_H<k.
\]
Thus arbitrarily large-treewidth members of \(\mathcal C_H\) contain no induced member of \(\mathcal A\) having treewidth at least \(k\). Property (D) fails. ∎

Hence every induced treewidth detector must satisfy
\[
\downarrow_i\mathcal A=\{\text{all finite graphs}\}.
\]
In particular, if \(\mathcal A\) is hereditary, then \(\mathcal A\) itself must be the class of all graphs.

The hereditary qualification is essential. For example, the proper nonhereditary family of all connected graphs satisfies (D): a connected component of \(G\) is induced, and some component has treewidth \(\operatorname{tw}(G)\). Its induced closure is nevertheless all graphs. Thus the later theorem does not say that literally every proper, nonhereditary family fails; it says that any successful family must already encode every finite graph through induced subgraphs.

## 5. Literal fixed-graph interpretation

If “unavoidable” instead means a single fixed graph \(H\) appearing induced in every graph of sufficiently large treewidth, the answer is elementary and different:

- \(K_1\) is unavoidable in every nonempty graph.
- \(K_2\) is unavoidable once treewidth is at least \(1\).
- Every noncomplete \(H\) is avoided by arbitrarily large complete graphs.
- Every complete \(H=K_r\) with \(r\geq3\) is avoided by the graphs \(K_{n,n}\), whose treewidth is unbounded.

Thus, apart from the empty graph convention, only \(K_1\) and \(K_2\) are individually unavoidable. The CHS programme plainly concerns parameterized obstruction families rather than this literal interpretation.

## 6. Scope and gaps

The consequence is therefore precise:

> There is no nontrivial proper hereditary induced-subgraph analogue of the universal grid family. For every omitted graph \(H\), a tailored hereditary weakly sparse class \(\mathcal C_H\) witnesses the failure.

This does not invalidate structural theorems for specifically restricted hereditary classes, nor does it provide a finite description of all context-dependent mechanisms producing large treewidth. Those remain meaningful research problems.

The only imported ingredient is the essential-graph theorem from arXiv:2502.14775; its layered-wheel construction is not reproduced here. Conditional on that published theorem statement, the deductions above are complete. They are not new enough to warrant publication.