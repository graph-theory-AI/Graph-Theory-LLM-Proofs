```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains unsettled, but it reduces to a sparse-core statement, bounded-substitution-width subfamilies satisfy Erdős–Hajnal, and Paley-17 substitutions show that any possible exponent is at most log(3)/log(17).",
  "would_publish": false,
  "caveats": "The key sparse-core estimate is reduced to but not proved, and no counterexample is obtained."
}
```

# Mathematical writeup

## 1. Statement and notation

Let
\[
\mathcal C=\operatorname{Forb}_{\mathrm{ind}}(C_8,\overline{C_8})
\]
and write
\[
h(G)=\max\{\alpha(G),\omega(G)\}.
\]
The problem asks whether there is \(c>0\) such that
\[
h(G)\ge |G|^c
\qquad\text{for every }G\in\mathcal C.
\]

I do not resolve this. I give:

1. a substitution construction showing that any valid exponent satisfies
   \[
   c\le \frac{\log 3}{\log 17}\approx 0.387762;
   \]
2. an Erdős–Hajnal theorem for every bounded-substitution-width subfamily;
3. a reduction of the full conjecture to a fixed-density sparse case, together with the precise form a counterexample sequence would have to take.

---

## 2. Substitution closure

A set \(M\subseteq V(H)\) is a module if every vertex outside \(M\) is either complete or anticomplete to \(M\). A graph is prime if its only modules are the singletons and the whole vertex set.

### Lemma 2.1
For every \(n\ge 5\), the cycle \(C_n\) is prime. Consequently, \(\overline{C_n}\) is prime.

#### Proof
Let \(M\) be a nontrivial module of \(C_n\).

If \(M\) contains adjacent vertices \(u,v\), let \(w\) be the other neighbor of \(u\). Then \(w\) is adjacent to \(u\) and not to \(v\). Hence \(w\in M\), since otherwise \(w\) distinguishes two vertices of \(M\). Repeating this around the cycle gives \(M=V(C_n)\).

Thus a proper module must be stable. Let \(u,v\in M\), \(u\ne v\), and let \(x,y\) be the two neighbors of \(u\). Both \(x,y\notin M\). Since each is adjacent to \(u\), modularity forces both \(x\) and \(y\) to be adjacent to every vertex of \(M\), in particular to \(v\). But in \(C_n\), for \(n\ge5\), the two neighbors of \(u\) have \(u\) as their unique common neighbor. Hence \(v=u\), a contradiction.

Finally, a set is a module in a graph if and only if it is a module in its complement. ∎

For a graph \(A\) and graphs \((B_a:a\in V(A))\), let
\[
A(B_a:a\in V(A))
\]
denote their substitution: each \(a\) is replaced by \(B_a\), and two distinct bags are complete or anticomplete according as their corresponding vertices are adjacent or nonadjacent in \(A\).

### Lemma 2.2
Let \(H\) be prime. If \(A\) and every \(B_a\) are induced-\(H\)-free, then \(A(B_a:a\in V(A))\) is induced-\(H\)-free.

#### Proof
Suppose an induced copy \(X\) of \(H\) occurs in the substitution. Its intersection with each bag is a module of \(G[X]\cong H\). Since \(H\) is prime, if \(X\) meets more than one bag, it meets every bag in at most one vertex. Projection to the skeleton \(A\) then gives an induced copy of \(H\) in \(A\). If \(X\) meets only one bag, that bag contains \(H\). Both alternatives are impossible. ∎

Applying this to both \(C_8\) and \(\overline{C_8}\) gives:

### Corollary 2.3
The class \(\mathcal C\) is closed under substitution.

---

## 3. A Paley-17 obstruction to large exponents

Let \(P\) be the Paley graph on \(\mathbb Z_{17}\): distinct \(x,y\) are adjacent when \(x-y\) is a quadratic residue modulo \(17\). The nonzero quadratic residues are
\[
Q=\{1,2,4,8,9,13,15,16\}.
\]

Because \(3\notin Q\), multiplication by \(3\) maps residues to nonresidues and is an isomorphism \(P\to\overline P\). Thus \(P\) is self-complementary.

### Lemma 3.1
\[
\alpha(P)=\omega(P)=3.
\]

#### Proof
It suffices to prove that \(P\) has no \(K_4\). By translation, a hypothetical \(K_4\) can be assumed to contain \(0\). Its other three vertices would form a triangle in the graph induced by \(Q=N_P(0)\).

The neighborhoods within \(Q\) are:
\[
\begin{array}{c|c}
q&N_{P[Q]}(q)\\ \hline
1&\{2,9,16\}\\
2&\{1,4,15\}\\
4&\{2,8,13\}\\
8&\{4,9,16\}\\
9&\{1,8,13\}\\
13&\{4,9,15\}\\
15&\{2,13,16\}\\
16&\{1,8,15\}.
\end{array}
\]
In every row, the displayed three vertices are pairwise nonadjacent, so \(P[Q]\) is triangle-free. Hence \(\omega(P)\le3\). On the other hand, \(\{0,1,2\}\) is a triangle, so \(\omega(P)=3\).

Self-complementarity gives \(\alpha(P)=\omega(P)=3\). ∎

An induced \(C_8\) contains a stable set of four alternating vertices, while an induced \(\overline{C_8}\) contains a clique of four. Therefore:

### Corollary 3.2
The Paley graph \(P\) belongs to \(\mathcal C\).

Let \(P^{[k]}\) be the \(k\)-fold lexicographic power of \(P\). By Corollary 2.3,
\[
P^{[k]}\in\mathcal C.
\]
Clique and stability numbers multiply under lexicographic products, so
\[
|P^{[k]}|=17^k,\qquad
\alpha(P^{[k]})=\omega(P^{[k]})=3^k.
\]
Consequently,
\[
h(P^{[k]})=|P^{[k]}|^{\log_{17}3}.
\]

### Proposition 3.3
If \(\mathcal C\) has the Erdős–Hajnal property with exponent \(c\), then
\[
c\le \log_{17}3\approx0.387762.
\]

This does not disprove the conjecture: the construction itself still has a positive homogeneous-set exponent.

More generally, for every \(B\in\mathcal C\), substitution with \(B[\overline B]\) gives the bound
\[
c\le
\frac{\log\bigl(\alpha(B)\omega(B)\bigr)}
     {2\log |B|}.
\]
Indeed, \(B[\overline B]\in\mathcal C\), and both its clique and stability numbers equal \(\alpha(B)\omega(B)\).

---

## 4. A positive result for bounded substitution width

Define the substitution width of a graph to be at most \(m\) if it can be constructed from one-vertex graphs using substitutions whose skeletons have at most \(m\) vertices. Arbitrarily large complete or edgeless decomposition nodes may be made binary.

### Proposition 4.1
Let \(m\ge2\). Every \(n\)-vertex graph of substitution width at most \(m\) satisfies
\[
h(G)\ge n^{c_m},
\qquad
c_m=\frac{\log 2}{2\log m}.
\]

#### Proof
Set
\[
p(G)=\alpha(G)\omega(G),\qquad
\beta=\log_m2.
\]
We prove by induction on a substitution construction that
\[
p(G)\ge |G|^\beta.
\]

Suppose
\[
G=A(G_1,\ldots,G_q),\qquad 2\le q\le m,
\]
and write
\[
\alpha_i=\alpha(G_i),\quad
\omega_i=\omega(G_i),\quad
p_i=\alpha_i\omega_i,\quad
n_i=|G_i|.
\]

For any two distinct bags \(i,j\), one has
\[
p(G)\ge p_i+p_j.
\]
Indeed, if \(ij\in E(A)\), then
\[
\omega(G)\ge\omega_i+\omega_j,\qquad
\alpha(G)\ge\max\{\alpha_i,\alpha_j\}.
\]
Assuming \(\alpha_i\ge\alpha_j\),
\[
p(G)\ge\alpha_i(\omega_i+\omega_j)
      \ge p_i+p_j.
\]
The nonadjacent case is complementary: stable sets combine, and one uses the larger of \(\omega_i,\omega_j\).

Order the bag sizes as \(n_1\ge n_2\ge\cdots\). By induction,
\[
p(G)\ge p_1+p_2\ge n_1^\beta+n_2^\beta.
\]
Put \(n=\sum_i n_i\) and \(x=n_1/n\). Then \(x\ge1/m\), and
\[
n_2\ge \frac{n-n_1}{m-1}.
\]
Therefore
\[
n_1^\beta+n_2^\beta
\ge n^\beta\left(
x^\beta+\left(\frac{1-x}{m-1}\right)^\beta
\right).
\]
The expression in parentheses is a concave function of \(x\in[1/m,1]\). At both endpoints it equals \(1\), since \(m^\beta=2\). It is therefore at least \(1\) throughout the interval. Thus \(p(G)\ge n^\beta\).

Finally,
\[
h(G)\ge\sqrt{\alpha(G)\omega(G)}
      \ge n^{\beta/2}.
\]
∎

### Consequence
For each fixed \(m\), the members of \(\mathcal C\) of substitution width at most \(m\) have the Erdős–Hajnal property. In particular, for \(m=17\),
\[
h(G)\ge |G|^{\log 2/(2\log17)}
       \approx |G|^{0.1223}.
\]

Combining this with substitution closure gives an infinite special case: the substitution closure of any finite collection of \(\{C_8,\overline{C_8}\}\)-free graphs has the Erdős–Hajnal property.

This cannot settle the full question by itself: \(\mathcal C\) contains prime graphs of unbounded order, for example the paths \(P_t\), \(t\ge4\).

---

## 5. Reduction to a sparse core

I use the standard induced-density theorem of Rödl in the following form:

> For every fixed graph \(H\) and every \(\rho>0\), there is \(\delta>0\) such that every induced-\(H\)-free graph \(G\) has a set \(X\), \(|X|\ge\delta|G|\), for which either \(G[X]\) or \(\overline{G[X]}\) has edge density at most \(\rho\).

The density conclusion can be changed to a maximum-degree conclusion by discarding at most half the vertices.

### Proposition 5.1 — sparse-core equivalence
The original conjecture is equivalent to the following assertion:

> There exist \(\eta,a>0\) such that every \(m\)-vertex graph \(J\in\mathcal C\) satisfying
> \[
> \Delta(J)\le\eta m
> \]
> has
> \[
> h(J)\ge m^a.
> \]

#### Proof
The forward implication is immediate.

Conversely, apply Rödl's theorem with \(H=C_8\) and density parameter \(\rho=\eta/4\). Since \(G\in\mathcal C\), there is \(X\), of size at least \(\delta|G|\), such that one of
\[
L=G[X],\qquad L=\overline{G[X]}
\]
has at most \(\rho\binom{|X|}{2}\) edges. In the second case \(L\) is still \(C_8\)-free because \(G\) is \(\overline{C_8}\)-free. In either case \(L\in\mathcal C\).

Delete the vertices of degree greater than \(2\rho|X|\). Fewer than \(|X|/2\) vertices are deleted. The remaining graph \(J\) has
\[
|J|\ge |X|/2\ge \delta|G|/2
\]
and
\[
\Delta(J)\le 2\rho|X|\le4\rho|J|=\eta|J|.
\]
By the sparse assertion,
\[
h(G)\ge h(J)\ge |J|^a
      \ge (\delta|G|/2)^a.
\]
Reducing the exponent slightly absorbs the fixed multiplicative constant. ∎

Thus an especially useful sufficient statement would be:

> There are \(\eta,a>0\) such that every induced-\(C_8\)-free graph \(J\), without assuming \(\overline{C_8}\)-freeness, with \(\Delta(J)\le\eta|J|\), has \(h(J)\ge |J|^a\).

This stronger one-sided sparse statement would settle the problem, but I do not prove it.

---

## 6. Sparse regimes that can be handled

Two elementary regimes illustrate what remains.

### Polynomially sublinear maximum degree
If
\[
\Delta(J)\le |J|^{1-\gamma},
\]
then greedy coloring gives
\[
\alpha(J)\ge\frac{|J|}{\Delta(J)+1}
           =\Omega(|J|^\gamma).
\]
Hence the difficult sparse case has maximum degree \(m^{1-o(1)}\), despite being at most a small fixed fraction of \(m\).

### No ordinary \(C_8\)
If \(J\) has no \(C_8\) even as a non-induced subgraph, the standard even-cycle extremal bound gives
\[
e(J)=O(|J|^{5/4}).
\]
Consequently, by the Caro–Wei bound,
\[
\alpha(J)
\ge \frac{|J|^2}{2e(J)+|J|}
=\Omega(|J|^{3/4}).
\]

In particular, if an induced-\(C_8\)-free graph has girth at least six, it has no ordinary \(C_8\): any chord of an 8-cycle creates a cycle of length \(3\), \(4\), or \(5\), so every 8-cycle would be induced. Thus this high-girth subcase has a homogeneous set of order \(\Omega(n^{3/4})\).

---

## 7. Necessary shape of a counterexample sequence

Suppose the conjecture fails. Applying Proposition 5.1 with sparsity parameters tending to zero yields a sequence \(J_k\in\mathcal C\), with \(m_k=|J_k|\to\infty\), such that
\[
h(J_k)=m_k^{o(1)},\qquad
\Delta(J_k)=o(m_k).
\]
The Caro–Wei inequality
\[
\alpha(J_k)\ge
\frac{m_k}{\overline d(J_k)+1}
\]
then forces
\[
\overline d(J_k)=m_k^{1-o(1)}.
\]

Thus a genuine counterexample would have to resemble a sparse pseudorandom graph in the narrow sense
\[
m^{1-o(1)}
\le \overline d(J)
\le \Delta(J)
=o(m),
\]
while avoiding both induced \(C_8\) and induced \(\overline{C_8}\) and having no polynomial clique or stable set.

The ordinary \(C_8\)-extremal theorem is ineffective here: such a graph has far more than \(m^{5/4}\) edges, so it necessarily contains many ordinary 8-cycles. Every one of those cycles must have chords. Controlling the concentration of those chords—without already producing a polynomial clique or stable set—is the unresolved step.

## 8. Conclusion and gap

The conjecture is not proved or disproved here. The main concrete conclusions are:

\[
\boxed{c\le\log_{17}3\approx0.387762}
\]
for any possible Erdős–Hajnal exponent;

\[
\boxed{h(G)\ge |G|^{\log 2/(2\log m)}}
\]
for every bounded-substitution-width-\(m\) subfamily; and the full problem is equivalent to its fixed-density sparse subcase.

A complete proof still requires a polynomial homogeneous-set bound in induced-\(C_8\)-free, fixed-density sparse graphs, or some different structural decomposition that covers prime graphs of unbounded order.