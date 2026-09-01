```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For clique-bounded parameters, (CC) forces boundedness in terms of the list chromatic number of the complement; this yields an explicit obstruction, an exact co-matching subclass dichotomy, and an undecidability result.",
  "would_publish": false,
  "caveats": "No sufficient condition or full characterization is obtained; the construction uses induced-subgraph heredity and the paper's island definition of col."
}
```

# 1. Definitions and scope

I use the definitions from the source paper. Thus \(f\) is induced-hereditary and componentwise:
\[
f(H)\le f(G)\quad\text{for every induced subgraph }H\subseteq G,
\qquad
f(G)=\max_{C\in\operatorname{comp}(G)}f(C).
\]

An \(L\)-coloring is an \((f,p)\)-coloring if every color class \(X\) satisfies \(f(G[X])\le p\). The corresponding list parameter is \(\chi^\ell_{f,p}\).

A nonempty \(S\subseteq V(H)\) is an \((f,p,k)\)-island if
\[
f(H[S])\le p
\quad\text{and}\quad
|N_H(v)\setminus S|<k\quad\text{for every }v\in S.
\]
Then \(\operatorname{col}_{f,p}(G)\le k\) means that every induced subgraph of \(G\) has such an island. Any alternative convention using “at most \(k\)” merely changes the constants below by one.

The original problem asks for a complete characterization. I obtain a necessary condition for the important case in which \(f\) is bounded on cliques, together with an exact characterization of a concrete subclass.

# 2. A replication lemma for joins

For a nonempty graph \(A\), write \(A^{\vee m}\) for the complete join of \(m\) vertex-disjoint copies of \(A\).

## Lemma 2.1

Let \(k\ge1\), \(m=2k+1\), and \(G=A^{\vee m}\). Every \(k\)-island \(S\) of \(G\) contains all vertices of at least one copy of \(A\).

### Proof

Let the copies be \(A_1,\dots,A_m\), and put
\[
X=V(G)\setminus S,\qquad X_i=X\cap V(A_i).
\]

If \(S\) meets only one block, say \(A_i\), then every vertex of \(S\) is adjacent to all vertices in the other \(m-1\) blocks. Its external degree is therefore at least
\[
(m-1)|V(A)|\ge 2k,
\]
contrary to \(S\) being a \(k\)-island.

Thus \(S\) meets two distinct blocks, say \(A_i\) and \(A_j\). Choose
\(u\in S\cap V(A_i)\) and \(v\in S\cap V(A_j)\). Since all edges between distinct blocks are present,
\[
\sum_{\ell\ne i}|X_\ell|<k,
\qquad
\sum_{\ell\ne j}|X_\ell|<k.
\]
Adding these inequalities gives
\[
|X_i|+|X_j|+2\sum_{\ell\notin\{i,j\}}|X_\ell|<2k,
\]
and hence \(|X|<2k\). Consequently \(X\) meets fewer than \(2k\) of the \(2k+1\) blocks. At least one block is entirely contained in \(S\). ∎

# 3. A necessary condition for clique-bounded parameters

Let \(\operatorname{ch}(H)\) denote the ordinary list chromatic number of \(H\), and define
\[
d_f(s)=
\sup\bigl\{
f(\overline H): \operatorname{ch}(H)\le s
\bigr\}.
\]

## Theorem 3.1 — Complement-choice obstruction

Suppose
\[
c:=\sup_{n\ge1} f(K_n)<\infty.
\]
If \(f\) satisfies property (CC), then
\[
d_f(s)<\infty
\qquad\text{for every }s\ge1.
\tag{1}
\]

Equivalently, for clique-bounded parameters satisfying (CC), \(f(G)\) is bounded by a function of \(\operatorname{ch}(\overline G)\).

### Proof

Suppose instead that \(d_f(s)=\infty\) for some fixed \(s\). We show that (CC) fails for the fixed pair \(p=c\) and this value of \(s\).

Let \(q,k\) be arbitrary proposed values for \(p',s'\). Choose a graph \(H\) such that
\[
\operatorname{ch}(H)\le s
\quad\text{and}\quad
f(\overline H)>q.
\]
Set
\[
m=2k+1,\qquad
G=\overline{mH}=(\overline H)^{\vee m},
\]
where \(mH\) denotes the disjoint union of \(m\) copies of \(H\).

We first prove
\[
\chi^\ell_{f,c}(G)\le s.
\]
Take any list assignment of size \(s\) on \(V(G)=V(mH)\). Since
\[
\operatorname{ch}(mH)=\operatorname{ch}(H)\le s,
\]
there is a proper list-coloring of \(mH\). Every color class is independent in \(mH\), and therefore is a clique in its complement \(G\). By the definition of \(c\), each color class has \(f\)-value at most \(c\). This is an \((f,c)\)-list-coloring of \(G\).

On the other hand, \(G\) has no \((f,q,k)\)-island. Indeed, if \(S\) were one, Lemma 2.1, applied with \(A=\overline H\), would imply that \(S\) contains an entire copy of \(\overline H\). By heredity,
\[
f(G[S])\ge f(\overline H)>q,
\]
a contradiction.

Thus
\[
\operatorname{col}_{f,q}(G)>k
\]
although \(\chi^\ell_{f,c}(G)\le s\). Since \(q,k\) were arbitrary, (CC) fails. ∎

## Consequences

For every clique-bounded parameter satisfying (CC):

1. **Bounded complement degree controls \(f\):**
   since \(\operatorname{ch}(H)\le\Delta(H)+1\),
   \[
   f(G)\le d_f\bigl(\Delta(\overline G)+1\bigr).
   \]

2. **Join powers are bounded:** for every fixed graph \(A\),
   \[
   \sup_{m\ge1} f(A^{\vee m})<\infty,
   \]
   because
   \[
   A^{\vee m}=\overline{m\overline A}
   \quad\text{and}\quad
   \operatorname{ch}(m\overline A)=\operatorname{ch}(\overline A).
   \]

3. In particular, if \(J_n=K_{2n}-nK_2\), the complement of a perfect matching, then
   \[
   \sup_n f(J_n)<\infty.
   \tag{2}
   \]

Thus unbounded growth on co-matchings is a simple certificate for failure of (CC), provided \(f\) is bounded on cliques.

# 4. An explicit hereditary connected parameter failing (CC)

Define
\[
\mu(G)=
\begin{cases}
0,&G=\varnothing,\\[2mm]
\displaystyle
\max_{C\in\operatorname{comp}(G)}
\bigl(1+\nu(\overline C)\bigr),&G\ne\varnothing,
\end{cases}
\]
where \(\nu\) denotes matching number.

## Proposition 4.1

The parameter \(\mu\) is induced-hereditary and componentwise, and it does not satisfy (CC).

### Proof

Componentwise behavior is built into the definition. If \(F\) is an induced subgraph of \(G\), each component \(D\) of \(F\) is contained in a component \(C\) of \(G\). Every matching in \(\overline D\) is also a matching in \(\overline C\), so
\[
\nu(\overline D)\le\nu(\overline C).
\]
Hence \(\mu(F)\le\mu(G)\).

For every clique,
\[
\mu(K_n)=1.
\]
On the other hand, for \(n\ge2\), the graph
\[
J_n=K_{2n}-nK_2
\]
is connected and satisfies
\[
\mu(J_n)=1+\nu(nK_2)=n+1.
\]
Since \(J_n=\overline{nK_2}\) and \(\operatorname{ch}(nK_2)=2\), Theorem 3.1 applies with \(c=1\) and \(s=2\), proving failure of (CC). ∎

There is also a direct list-coloring description. Given arbitrary lists of size two on \(J_n\), color the two endpoints of each missing matching edge differently; this is always possible. Each color class then contains at most one endpoint of every missing edge and hence induces a clique. Thus
\[
\chi^\ell_{\mu,1}(J_n)\le2,
\]
while \(\operatorname{col}_{\mu,q}(J_n)\) is unbounded for every fixed \(q\).

# 5. An exactly characterized subclass

Let \(h:\mathbb N_{\ge1}\to\mathbb N_{\ge1}\) be nondecreasing, with \(h(1)=1\), and define
\[
f_h=h\circ\mu.
\]
Equivalently,
\[
f_h(G)=
\max_{C\in\operatorname{comp}(G)}
h\bigl(1+\nu(\overline C)\bigr).
\]

## Theorem 5.1

The parameter \(f_h\) satisfies (CC) if and only if \(h\) is bounded.

### Proof

If \(h\) is bounded by \(B\), then \(f_h(G)\le B\) for every graph. Hence
\[
\operatorname{col}_{f_h,B}(G)\le1
\]
for every \(G\): in every induced subgraph, take the entire vertex set as the island. Thus (CC) holds.

If \(h\) is unbounded, then
\[
f_h(K_n)=h(1)=1,
\]
whereas
\[
f_h(J_n)=h(n+1)
\]
is unbounded. Theorem 3.1 again shows that (CC) fails. ∎

This gives a complete characterization on a nontrivial, uniformly defined family of hereditary connected parameters.

# 6. Effective complexity

Suppose a graph parameter is presented by a program which, on every finite graph, outputs its value, with heredity and componentwise behavior promised.

The preceding subclass already makes recognition of (CC) algorithmically intractable.

Let \(W_e\) be the \(e\)-th computably enumerable set, and let \(W_{e,r}\) be the elements enumerated during the first \(r\) computation stages. Define
\[
h_e(r)=
\max\bigl(\{1\}\cup(W_{e,r}\cap\{1,\dots,r\})\bigr).
\]
Then \(h_e\) is total, computable, nondecreasing, satisfies \(h_e(1)=1\), and \(h_e(r)\le r\). Moreover,
\[
h_e\text{ is bounded}
\quad\Longleftrightarrow\quad
W_e\text{ is finite}.
\]
Therefore, by Theorem 5.1,
\[
f_{h_e}\text{ satisfies (CC)}
\quad\Longleftrightarrow\quad
W_e\text{ is finite}.
\]

Since the index set of finite computably enumerable sets is \(\Sigma^0_2\)-complete, recognition of (CC), even on this restricted family, is \(\Sigma^0_2\)-hard and is neither decidable nor semidecidable; its complement is not semidecidable either.

For comparison, relative to a total evaluation oracle for \(f\), (CC) has the syntactic upper bound
\[
\forall p,s\;\exists p',s'\;\forall G\;R(f,p,s,p',s',G),
\]
where \(R\) is decidable on finite graphs. Indeed, generalized list-colorability and the island condition can both be checked by finite exhaustive search. Thus unrestricted (CC) lies at the \(\Pi^0_3\) level in this promised-oracle formulation.

# 7. What remains open

The main unresolved point is sufficiency. For clique-bounded \(f\), I proved the necessary condition
\[
\forall s\quad
\sup\{f(\overline H):\operatorname{ch}(H)\le s\}<\infty,
\]
but I do not know whether this condition, perhaps together with one of the source paper’s sufficient hypotheses, characterizes (CC).

The argument also says nothing decisive about the important branch where \(f(K_n)\) is unbounded, which includes parameters such as component order and maximum degree. Finally, the undecidability result applies to unrestricted program-presented parameters; it does not preclude a satisfactory characterization for natural monotone or minor-monotone parameters.