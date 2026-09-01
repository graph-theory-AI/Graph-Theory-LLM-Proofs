```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The question is not a truth-valued conjecture; I give a canonical obstruction normal form, concrete special cases, and a sharp Sigma^0_2 complexity barrier for arbitrary hereditary classes.",
  "would_publish": false,
  "caveats": "The obstruction criterion is formal rather than structural, and the complexity results depend on the chosen membership-bit or algorithmic presentation."
}
```

## 1. Statement and interpretation

All graphs below are finite and simple. A hereditary class \(\mathcal C\) is polynomially \(\chi\)-bounded if there is a polynomial \(p\) such that
\[
\chi(G)\le p(\omega(G))
\qquad\text{for every }G\in\mathcal C.
\]

The displayed question is an open-ended classification programme, not a proposition with a truth value. In particular, there is no proposed characterization to prove or disprove. The results below give:

1. an exact, but formal, forbidden-induced-subgraph normal form;
2. structural information about the canonical obstructions;
3. elementary positive and negative results for finitely forbidden classes;
4. a sharp descriptive-complexity classification for unrestricted hereditary classes;
5. an undecidability result even when class membership is decidable.

None of these is the intended structural classification.

---

## 2. A canonical obstruction normal form

For integers \(A,d\ge 1\), define
\[
\mathcal B_{A,d}
 =
 \left\{
 G:\chi(H)\le A\omega(H)^d
 \text{ for every induced subgraph }H\text{ of }G
 \right\}.
\]

### Theorem 2.1

A hereditary class \(\mathcal C\) is polynomially \(\chi\)-bounded if and only if
\[
\mathcal C\subseteq \mathcal B_{A,d}
\]
for some integers \(A,d\ge1\).

#### Proof

If \(\mathcal C\) has a polynomial binding function \(p\), then for positive integers \(x\) there are integers \(A,d\ge1\) such that
\[
p(x)\le Ax^d.
\]
For example, one may take \(d\) at least the degree of \(p\) and \(A\) larger than the sum of the absolute values of its coefficients.

If \(G\in\mathcal C\) and \(H\) is induced in \(G\), heredity gives \(H\in\mathcal C\), and hence
\[
\chi(H)\le p(\omega(H))\le A\omega(H)^d.
\]
Thus \(G\in\mathcal B_{A,d}\).

Conversely, if \(\mathcal C\subseteq\mathcal B_{A,d}\), taking \(H=G\) gives
\[
\chi(G)\le A\omega(G)^d
\]
for every \(G\in\mathcal C\). ∎

Thus the polynomially \(\chi\)-bounded hereditary classes form the downward closure, under class inclusion, of the countable family
\[
\{\mathcal B_{A,d}:A,d\ge1\}.
\]

### Canonical minimal obstructions

Let \(\mathcal O_{A,d}\) be the family of graphs \(Q\) such that
\[
\chi(Q)>A\omega(Q)^d,
\]
but
\[
\chi(H)\le A\omega(H)^d
\]
for every proper induced subgraph \(H\) of \(Q\).

Then
\[
\mathcal B_{A,d}=\operatorname{Forb}_{\mathrm{ind}}(\mathcal O_{A,d}).
\]

Indeed, if a graph is not in \(\mathcal B_{A,d}\), choose an induced subgraph of minimum order violating the inequality; it belongs to \(\mathcal O_{A,d}\). The converse is immediate.

These canonical obstructions have significant elementary structure.

### Proposition 2.2

Every \(Q\in\mathcal O_{A,d}\) is:

1. vertex-critical;
2. of minimum degree at least \(\chi(Q)-1\);
3. connected;
4. co-connected, meaning that \(\overline Q\) is connected.

Moreover, \(\mathcal O_{A,d}\) is an induced-subgraph antichain.

#### Proof

For every \(v\in V(Q)\),
\[
\chi(Q-v)
 \le A\omega(Q-v)^d
 \le A\omega(Q)^d
 <\chi(Q).
\]
Deleting one vertex decreases chromatic number by at most one, so
\[
\chi(Q-v)=\chi(Q)-1.
\]
Thus \(Q\) is vertex-critical. If some vertex had degree at most \(\chi(Q)-2\), a \((\chi(Q)-1)\)-coloring of \(Q-v\) would leave a color unused on \(N(v)\), allowing the coloring to be extended to \(Q\). Hence
\[
\delta(Q)\ge\chi(Q)-1.
\]

If \(Q\) were disconnected, then each component \(Q_i\) would be a proper induced subgraph and therefore satisfy the inequality. Since
\[
\chi(Q)=\max_i\chi(Q_i),\qquad
\omega(Q)=\max_i\omega(Q_i),
\]
the graph \(Q\) would also satisfy the inequality, a contradiction.

If \(\overline Q\) were disconnected, then \(Q\) would be the complete join of proper induced subgraphs \(Q_1,\dots,Q_s\). Consequently,
\[
\chi(Q)=\sum_i\chi(Q_i),\qquad
\omega(Q)=\sum_i\omega(Q_i).
\]
Using \(d\ge1\),
\[
\chi(Q)
 \le A\sum_i\omega(Q_i)^d
 \le A\left(\sum_i\omega(Q_i)\right)^d
 =A\omega(Q)^d,
\]
again a contradiction.

Finally, one member of \(\mathcal O_{A,d}\) cannot be a proper induced subgraph of another, since every proper induced subgraph of a member satisfies the inequality. ∎

Let \(\mathcal F_{\mathcal C}\) denote the minimal forbidden induced subgraphs for a hereditary class \(\mathcal C\). The preceding observations give the exact criterion
\[
\boxed{
\mathcal C\text{ is polynomially }\chi\text{-bounded}
\iff
\exists A,d\ \forall Q\in\mathcal O_{A,d}\ 
\exists F\in\mathcal F_{\mathcal C}\text{ with }F\le_{\mathrm{ind}} Q.
}
\]
This is logically complete, but circular: the families \(\mathcal O_{A,d}\) are themselves defined using the desired chromatic inequality.

For comparison, \(\mathcal B_{1,1}\) is precisely the class of perfect graphs. In that case, identifying \(\mathcal O_{1,1}\) as the odd holes and odd antiholes is the content of the Strong Perfect Graph Theorem. Thus even the first envelope is highly nontrivial structurally.

---

## 3. Concrete finitely forbidden special cases

We first record the standard high-girth lemma in a form needed below.

### Lemma 3.1

For every \(g,q\ge3\), there is a graph of girth greater than \(g\) and chromatic number greater than \(q\).

#### Proof

Take the binomial random graph \(G(n,p)\), where
\[
p=n^{-1+1/(2g)}.
\]
Let \(X\) be the number of cycles of lengths between \(3\) and \(g\). Then
\[
\mathbb E X
 \le \sum_{\ell=3}^{g}\frac{n^\ell p^\ell}{2\ell}
 =O_g(n^{1/2}).
\]
Thus, with probability tending to one, \(X<n/4\).

Put \(m=\lceil n/(2q)\rceil\). The probability of an independent set of order \(m\) is at most
\[
\binom nm(1-p)^{\binom m2}
 \le
 \exp\left(
 m\log\frac{en}{m}-p\binom m2
 \right)
 =o(1),
\]
because the positive term is \(O(n)\), while the negative term has order
\(n^{1+1/(2g)}\).

Hence, for sufficiently large \(n\), there is a graph with fewer than \(n/4\) short cycles and independence number less than \(m\). Delete one vertex from each cycle of length at most \(g\). The remaining graph \(H\) has more than \(3n/4\) vertices, girth greater than \(g\), and \(\alpha(H)<m\). Therefore
\[
\chi(H)\ge\frac{|V(H)|}{\alpha(H)}
 >
 \frac{3n/4}{n/(2q)+1}
 >q
\]
for sufficiently large \(n\). ∎

By taking an induced subgraph minimal subject to having chromatic number at least \(r\), one obtains the following useful strengthening:

> For every \(g\) and \(r\ge3\), there is a graph of girth greater than \(g\) and chromatic number exactly \(r\).

Indeed, vertex-minimality and the fact that deletion changes chromatic number by at most one force equality.

### Proposition 3.2: a necessary condition for finite forbidden lists

Let \(F_1,\dots,F_s\) be graphs, each containing a cycle. Then
\[
\operatorname{Forb}_{\mathrm{ind}}(F_1,\dots,F_s)
\]
is not \(\chi\)-bounded.

#### Proof

Choose \(g>\max_i |V(F_i)|\). By Lemma 3.1 there are graphs of girth greater than \(g\) and arbitrarily large chromatic number. Such graphs are triangle-free, so their clique number is at most two.

They cannot contain any \(F_i\), even as a non-induced subgraph: an occurrence of \(F_i\) would contain a cycle of length at most \(|V(F_i)|<g\). Thus they belong to the displayed hereditary class. ∎

Consequently, if a class defined by finitely many forbidden induced subgraphs is \(\chi\)-bounded, at least one graph in the forbidden list must be a forest. This is only a necessary condition.

### Proposition 3.3: induced-star-free classes

For every fixed \(t\ge1\), the class of \(K_{1,t}\)-free graphs is polynomially \(\chi\)-bounded. More precisely,
\[
\chi(G)\le
\binom{\omega(G)+t-2}{t-1}.
\]

#### Proof

Let \(w=\omega(G)\). For each vertex \(v\), the graph \(G[N(v)]\) has:

- no independent set of order \(t\), since that would give an induced \(K_{1,t}\) with center \(v\);
- no clique of order \(w\), since together with \(v\) it would give a clique of order \(w+1\).

Therefore
\[
\deg(v)<R(w,t).
\]
The standard Ramsey recurrence gives
\[
R(w,t)\le\binom{w+t-2}{t-1}.
\]
Greedy coloring now yields
\[
\chi(G)\le\Delta(G)+1
 \le R(w,t)
 \le\binom{w+t-2}{t-1}.
\]
∎

In particular, every hereditary class forbidding a fixed stable set \(I_t\) is polynomially \(\chi\)-bounded, since an \(I_t\)-free graph is also \(K_{1,t}\)-free.

---

## 4. Sharp descriptive complexity

There is a natural topology on the collection of hereditary classes. Let \(\mathcal G\) be the countable set of isomorphism classes of finite graphs, and identify a graph class with a point of
\[
2^{\mathcal G},
\]
using one membership bit for each finite graph. The hereditary classes form a closed subspace \(\mathfrak H\).

Let \(\mathfrak P\subseteq\mathfrak H\) be the set of polynomially \(\chi\)-bounded hereditary classes.

### Theorem 4.1

In the membership-bit topology, \(\mathfrak P\) is a complete \(F_\sigma\), equivalently complete \(\boldsymbol\Sigma^0_2\), subset of \(\mathfrak H\).

#### Upper bound

For fixed \(A,d\), let
\[
\mathfrak P_{A,d}
 =
 \left\{
 \mathcal C\in\mathfrak H:
 \chi(G)\le A\omega(G)^d\text{ for all }G\in\mathcal C
 \right\}.
\]
This is closed: it is the intersection, over all graphs \(G\) violating the inequality, of the clopen condition \(G\notin\mathcal C\). By Theorem 2.1,
\[
\mathfrak P=\bigcup_{A,d\ge1}\mathfrak P_{A,d}.
\]
Thus \(\mathfrak P\) is \(F_\sigma\).

#### Hardness

For \(x\in\mathbb N^{\mathbb N}\), put
\[
r_x(n)=\max_{0\le j\le n}x(j)
\]
and define
\[
\mathcal C_x
 =
 \left\{
 G:
 \chi(H)\le 2+r_x(|V(H)|)
 \text{ for every induced }H\le_{\mathrm{ind}}G
 \right\}.
\]

This class is hereditary. Moreover, the map
\[
x\longmapsto\mathcal C_x
\]
is continuous: whether a fixed graph \(G\) of order \(n\) belongs to \(\mathcal C_x\) depends only on \(x(0),\dots,x(n)\).

If \(x\) is bounded, say \(x(n)\le K\), then every \(G\in\mathcal C_x\) satisfies
\[
\chi(G)\le K+2,
\]
so \(\mathcal C_x\) is polynomially \(\chi\)-bounded.

Suppose \(x\) is unbounded. For every \(k\), choose \(N\ge3\) with \(r_x(N)\ge k\). Choose a graph \(G\) of girth greater than \(N\) and chromatic number exactly \(k+2\). For every induced \(H\le_{\mathrm{ind}}G\):

- if \(|V(H)|\le N\), then \(H\) is a forest, so \(\chi(H)\le2\);
- if \(|V(H)|>N\), then
  \[
  \chi(H)\le k+2\le 2+r_x(|V(H)|).
  \]

Thus \(G\in\mathcal C_x\). These graphs have clique number two and unbounded chromatic number, so \(\mathcal C_x\) is not even \(\chi\)-bounded.

It follows that
\[
\mathcal C_x\in\mathfrak P
\quad\Longleftrightarrow\quad
x\text{ is bounded}.
\]
The set of bounded sequences
\[
\{x:\exists K\ \forall n,\ x(n)\le K\}
\]
is a standard complete \(F_\sigma\) set. Hence \(\mathfrak P\) is \(F_\sigma\)-hard and therefore \(F_\sigma\)-complete. ∎

For completeness, the hardness of bounded sequences can be seen directly. If \(A=\bigcup_k F_k\) is any \(F_\sigma\) subset of Baire space, with the closed sets \(F_k\) increasing, define \(b_y(n)\) to be the least \(k\le n\) such that the length-\(n\) cylinder around \(y\) meets \(F_k\), using \(n+1\) if no such \(k\) exists. Then \(y\mapsto b_y\) is continuous, and \(b_y\) is bounded exactly when \(y\in A\).

Thus the existential choice of polynomial followed by a universal quantification over graphs is not merely an artifact of the definition: in this unrestricted coding, it gives the sharp first nontrivial Borel complexity.

---

## 5. Effective undecidability

The same construction gives an algorithmic obstruction.

### Corollary 5.1

There is no algorithm which, given a code for a total membership algorithm promised to recognize a hereditary class, always decides whether that class is polynomially \(\chi\)-bounded.

More precisely, this promise-index problem is \(\Sigma^0_2\)-hard.

#### Proof

Let \(W_e\) be the \(e\)-th computably enumerable set, and let
\[
s_e(n)=|\{\text{distinct elements enumerated into }W_e
\text{ during the first }n\text{ stages}\}|.
\]
Define
\[
\mathcal C_e
 =
 \left\{
 G:
 \chi(H)\le2+s_e(|V(H)|)
 \text{ for every induced }H\le_{\mathrm{ind}}G
 \right\}.
\]

Membership is decidable uniformly in \(e\): enumerate the finitely many induced subgraphs of \(G\), compute their chromatic numbers by exhaustive search, and simulate the enumeration of \(W_e\) for the required finite numbers of stages. The class is hereditary by definition.

If \(W_e\) is finite, then \(s_e\) is bounded, and \(\mathcal C_e\) has bounded chromatic number. If \(W_e\) is infinite, then \(s_e\) is unbounded, and the high-girth argument from Theorem 4.1 shows that \(\mathcal C_e\) is not \(\chi\)-bounded. Hence
\[
\mathcal C_e\text{ is polynomially }\chi\text{-bounded}
\quad\Longleftrightarrow\quad
W_e\text{ is finite}.
\]
The index set of finite computably enumerable sets is \(\Sigma^0_2\)-complete.

For plain undecidability, given a machine \(M\), enumerate one new integer at each stage until \(M\) halts. The resulting set is finite exactly when \(M\) halts, so the proposed decision algorithm would decide the halting problem. ∎

There is also no terminating membership-oracle test using only finitely many graph-membership queries. Run such a test on the class of all finite graphs, which is not \(\chi\)-bounded. It makes finitely many queries, all answered “yes”; let \(N\) be the largest queried order. The hereditary class of all graphs of order at most \(N\) gives the same transcript but has bounded chromatic number.

Using the premise from the question that a \(\chi\)-bounded non-polynomial hereditary class \(\mathcal D\) exists, the same argument works even under the promise of \(\chi\)-boundedness: replace \(\mathcal D\) by
\[
\mathcal D_{\le N}=\{G\in\mathcal D:|V(G)|\le N\}.
\]
This agrees with \(\mathcal D\) on all queried graphs but is polynomially \(\chi\)-bounded.

---

## 6. Gaps and conclusion

The substantive classification remains open.

- The obstruction criterion in Section 2 is exact but circular: it uses chromatic inequalities to define the obstruction families.
- The \(F_\sigma\)-completeness and undecidability results apply to arbitrary hereditary classes under very general presentations. They do not rule out useful structure theorems for finitely forbidden, geometrically defined, or otherwise natural classes.
- The effective hardness construction distinguishes bounded-chromatic classes from classes that are not even \(\chi\)-bounded; it does not classify the polynomial/non-polynomial boundary inside effectively presented \(\chi\)-bounded classes.
- For finite forbidden lists, the arguments prove that at least one forbidden graph must be a forest for \(\chi\)-boundedness, and give explicit polynomial bounds when a forbidden graph is an induced star or stable set. They do not settle general forbidden forests.

Thus there is no proof or disproof of the original open-ended question here, but there is a precise obstruction normal form and a sharp complexity barrier showing why no unrestricted finite or algorithmic classification can exist.