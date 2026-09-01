```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A p-fold-cover bound proves the conjecture in the low-cover-defect regime and imposes strong necessary conditions on any counterexample, but does not settle the remaining cases.",
  "would_publish": false,
  "caveats": "Assumes a finite hypergraph with r>=2 and positive matching number; the literal empty-hypergraph case is false, and large cover-defect instances remain open."
}
```

# 1. Statement and conventions

Let \(\mathcal H\) be a finite \(r\)-partite \(r\)-uniform hypergraph, and write
\[
n=\nu(\mathcal H).
\]
For \(S\subseteq V(\mathcal H)\), let \(\mathcal H-S\) denote the hypergraph obtained by deleting \(S\) and all incident edges.

I interpret the conjecture for \(n>0\). Literally, if \(\mathcal H\) has no edges, then \(\nu(\mathcal H)=0\) cannot be reduced by a positive integer, so the statement needs this standard nontriviality assumption.

Only \(k\le n\) can be a witness. Set
\[
m=\min\{n,r-1\}.
\]

Define the \(k\)-th matching-blocker number
\[
b_k(\mathcal H)=
\min\bigl\{|S|:\nu(\mathcal H-S)\le n-k\bigr\},
\qquad 1\le k\le n.
\]
The conjecture is equivalent to
\[
b_k(\mathcal H)\le k(r-1)
\]
for some \(1\le k\le m\).

There is no distinction here between “at most” and “exactly” \(k(r-1)\) vertices. Indeed, if a set of size at most \(k(r-1)\) works, it can be padded: a maximum matching supplies \(rn\ge rk>k(r-1)\) vertices, and further deletions cannot increase the matching number.

# 2. Two elementary blocker identities

For \(t\ge1\), let \(\mathcal U_t(\mathcal H)\) be the hypergraph on \(V(\mathcal H)\) whose edges are the unions
\[
\bigcup_{e\in M}e
\]
over all \(t\)-edge matchings \(M\) of \(\mathcal H\).

Then
\[
\boxed{\quad b_k(\mathcal H)
=\tau\bigl(\mathcal U_{n-k+1}(\mathcal H)\bigr).\quad}
\]

Indeed, \(S\) reduces the matching number to at most \(n-k\) precisely when it intersects the union of every \((n-k+1)\)-matching.

There is also the universal bound
\[
\boxed{\quad b_k(\mathcal H)\le rk.\quad}
\]
To see this, choose any \(k\)-matching \(Q\) and delete its \(rk\) vertices. If an \((n-k+1)\)-matching remained, it would be disjoint from \(Q\), producing a matching of size \(n+1\).

Thus the conjecture asks whether, for some \(k\le r-1\), one can improve the trivial bound \(rk\) by exactly \(k\).

For \(k=n\),
\[
b_n(\mathcal H)=\tau(\mathcal H),
\]
since reducing the matching number to zero means deleting a vertex cover.

# 3. A \(p\)-fold-cover lemma

For \(1\le p\le r\), call \(C\subseteq V(\mathcal H)\) a \(p\)-cover if
\[
|C\cap e|\ge p\qquad\text{for every }e\in E(\mathcal H).
\]
Let
\[
\tau_p(\mathcal H)=\min\{|C|:C\text{ is a }p\text{-cover}\}.
\]
Thus \(\tau_1=\tau\). Since a maximum matching has \(n\) disjoint edges,
\[
\tau_p(\mathcal H)\ge pn.
\]

## Lemma

For \(1\le p\le r-1\) and \(1\le k\le n\),
\[
\boxed{\quad
b_k(\mathcal H)\le
\tau_p(\mathcal H)-p(n-k)
=
\bigl(\tau_p(\mathcal H)-pn\bigr)+pk.
\quad}
\]

### Proof

Let \(C\) be a minimum \(p\)-cover, of size \(c=\tau_p(\mathcal H)\). Since \(c\ge pn\), choose a subset \(C_0\subseteq C\) of size
\[
|C_0|=p(n-k),
\]
and delete
\[
S=C\setminus C_0.
\]
Every edge surviving in \(\mathcal H-S\) originally contained at least \(p\) vertices of \(C\), and none of these can lie in \(S\). Hence every surviving edge contains at least \(p\) vertices of \(C_0\).

A matching of size \(\ell\) in \(\mathcal H-S\) therefore uses at least \(p\ell\) distinct vertices of \(C_0\), so
\[
p\ell\le |C_0|=p(n-k).
\]
Thus \(\ell\le n-k\), as required. The number deleted is
\[
|S|=c-p(n-k).
\]
\(\square\)

Consequently, the conjecture holds whenever there are \(p,k\) with
\[
\boxed{\quad
\tau_p(\mathcal H)-pn
\le k(r-1-p),
\qquad
1\le p\le r-1,\quad 1\le k\le m.
\quad}
\]

This is a verifiable sufficient condition, not merely an asymptotic one.

# 4. The ordinary cover-defect consequence

Taking \(p=1\) gives the particularly simple bound
\[
\boxed{\quad b_k(\mathcal H)\le \tau(\mathcal H)-n+k.\quad}
\]

Hence, if
\[
\tau(\mathcal H)-n\le k(r-2),
\]
then \(k\) is a witness. In particular:

\[
\boxed{\quad
\tau(\mathcal H)-\nu(\mathcal H)
\le (r-2)\min\{\nu(\mathcal H),r-1\}
\quad\Longrightarrow\quad
\mathcal H\text{ satisfies the conjecture}.
\quad}
\]

Some special cases are:

- If \(\tau=\nu\), then \(b_1\le1\), so the original Lovász conclusion holds after padding to \(r-1\) vertices.
- More generally, if
  \[
  \tau\le \nu+r-2,
  \]
  then \(k=1\) works.
- If \(\nu\le r-1\) and \(\mathcal H\) satisfies Ryser’s bound
  \[
  \tau\le(r-1)\nu,
  \]
  then \(k=\nu\) works.

The last assertion is only a conditional result for an individual hypergraph; it does not assume Ryser’s conjecture in unresolved ranks.

# 5. Necessary conditions for a counterexample

Suppose \(\mathcal H\) is a counterexample to the proposed conjecture. Applying the \(p\)-cover lemma with \(k=m\) shows that, for every \(1\le p\le r-1\),
\[
\boxed{\quad
\tau_p(\mathcal H)
\ge
pn+m(r-1-p)+1.
\quad}
\]

In particular,
\[
\boxed{\quad
\tau(\mathcal H)
\ge
n+(r-2)m+1.
\quad}
\]

This has two useful forms.

### If \(n\le r-1\)

Then \(m=n\), so any counterexample must satisfy
\[
\tau(\mathcal H)\ge (r-1)n+1.
\]
Thus any counterexample with matching number at most \(r-1\) is necessarily also a counterexample to Ryser’s inequality.

### If \(n\ge r-1\)

Then
\[
\tau(\mathcal H)\ge
n+(r-1)(r-2)+1.
\]

Moreover, let \(V_i^+\) denote the vertices in the \(i\)-th part that belong to at least one edge. Each \(V_i^+\) is a vertex cover, and hence every counterexample satisfies
\[
|V_i^+|\ge
n+(r-2)m+1
\]
for every part \(i\).

These restrictions are unaffected by adding or removing isolated vertices.

# 6. Consequences for \(r=2\) and \(r=3\)

## Rank \(2\)

For a bipartite graph, Kőnig’s theorem gives \(\tau=\nu\). The ordinary cover bound gives
\[
b_1\le1.
\]
After padding, one obtains the required one vertex, since \(r-1=1\). Thus the conjecture holds for \(r=2\).

## Rank \(3\)

Here \(k\in\{1,2\}\). The ordinary cover bound specializes to
\[
b_1\le\tau-\nu+1,\qquad
b_2\le\tau-\nu+2.
\]
Therefore:

- If \(\tau\le\nu+1\), the original Lovász conclusion holds with \(k=1\).
- If \(\nu\ge2\) and \(\tau\le\nu+2\), then \(k=2\) works.

There is also the \(p=2\) certificate:
\[
b_2\le\tau_2-2(\nu-2).
\]
Thus, if
\[
\tau_2=2\nu,
\]
then \(b_2\le4\).

Using the known \(r=3\) case of Ryser’s conjecture,
\[
\tau\le2\nu,
\]
one obtains the following unconditional reduction.

## Proposition for \(r=3\)

Every \(3\)-partite \(3\)-uniform hypergraph with
\[
\nu(\mathcal H)\le2
\]
satisfies the conjecture.

Any \(r=3\) counterexample must satisfy
\[
\boxed{
\nu\ge3,\qquad
\nu+3\le\tau\le2\nu,\qquad
\tau_2\ge2\nu+1,
}
\]
and every active vertex class has size at least \(\nu+3\).

Also, one may restrict the search to incidence-connected hypergraphs. Matching numbers are additive over incidence components, and a witness contained in one component is automatically a witness for the whole hypergraph. Thus every nonempty component of a counterexample would itself have to be a counterexample and, in rank \(3\), have matching number at least \(3\).

# 7. Application to line hypergraphs of regular edge-coloured graphs

Let \(G\) be an \(r\)-regular graph with a proper \(r\)-edge-colouring. Define its line hypergraph \(\mathcal L(G)\) as follows:

- \(V(\mathcal L(G))=E(G)\);
- the \(r\) colour classes are the vertex parts;
- for each \(v\in V(G)\), the incident edge set \(\delta_G(v)\) is a hyperedge.

Then
\[
\nu(\mathcal L(G))=\alpha(G),
\]
because two hyperedges \(\delta_G(u),\delta_G(v)\) are disjoint exactly when \(u\) and \(v\) are nonadjacent.

A vertex cover of \(\mathcal L(G)\) is an edge cover of \(G\). Each colour class is a perfect matching, so if \(N=|V(G)|\),
\[
\tau(\mathcal L(G))=\frac N2.
\]

More generally, a \(p\)-cover of \(\mathcal L(G)\) is a set of graph edges having degree at least \(p\) at every graph vertex. The union of any \(p\) colour classes has \(pN/2\) edges, while the degree sum gives the matching lower bound. Hence
\[
\tau_p(\mathcal L(G))=\frac{pN}{2}.
\]

Writing
\[
d=\frac N2-\alpha(G),
\]
the \(p\)-cover criterion becomes
\[
pd\le k(r-1-p).
\]
Among these inequalities, \(p=1\) is the strongest. Therefore:

\[
\boxed{\quad
\frac{|V(G)|}{2}-\alpha(G)
\le
(r-2)\min\{\alpha(G),r-1\}
\quad\Longrightarrow\quad
\mathcal L(G)\text{ satisfies the conjecture}.
\quad}
\]

For cubic \(G\), this proves the weakened conjecture whenever
\[
\frac{|V(G)|}{2}-\alpha(G)\le2
\]
and \(\alpha(G)\ge2\). A line-hypergraph counterexample in the cubic case would necessarily have independence deficit at least \(3\). This criterion does not appear sufficient for the Biggs–Smith example and therefore does not subsume the source paper’s separate verification.

# 8. Exact finite-instance formulation

The blocker reformulation gives a completely specified computational test.

First compute \(n=\nu(\mathcal H)\) by the integer program
\[
\begin{aligned}
\text{maximize }&\sum_{e\in E(\mathcal H)}x_e,\\
\text{subject to }&
\sum_{e\ni v}x_e\le1
\quad(v\in V(\mathcal H)),\\
&x_e\in\{0,1\}.
\end{aligned}
\]

For each \(1\le k\le m\), put \(t=n-k+1\), enumerate all \(t\)-edge matchings \(M\), and solve
\[
\begin{aligned}
\text{minimize }&\sum_{v\in V(\mathcal H)}y_v,\\
\text{subject to }&
\sum_{v\in\bigcup_{e\in M}e}y_v\ge1
\quad\text{for every \(t\)-matching }M,\\
&y_v\in\{0,1\}.
\end{aligned}
\]
Its optimum is exactly \(b_k(\mathcal H)\). The conjecture holds for the instance precisely when one of these optima is at most \(k(r-1)\).

Likewise, the sufficient certificates above can be checked by
\[
\begin{aligned}
\tau_p(\mathcal H)=\text{minimize }&\sum_v y_v,\\
\text{subject to }&
\sum_{v\in e}y_v\ge p
\quad(e\in E(\mathcal H)),\\
&y_v\in\{0,1\}.
\end{aligned}
\]

No computational experiments are claimed here.

# 9. Remaining gap

The argument does not resolve hypergraphs with large \(p\)-cover defects. In the first unresolved rank \(r=3\), it leaves precisely the regime
\[
\nu\ge3,\qquad \tau-\nu\ge3,\qquad \tau_2-2\nu\ge1.
\]
The known counterexamples to Lovász’s original \(k=1\) assertion naturally lie outside the smallest cover-defect range, so a genuinely new matching-exchange or blocker argument would be needed there.

Thus the intended nonempty conjecture remains open, but any counterexample must satisfy the explicit hierarchy of \(p\)-cover obstructions above.