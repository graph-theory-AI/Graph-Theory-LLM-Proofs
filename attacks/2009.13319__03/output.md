```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the intended independent-pair notation, I exhibit a four-tournament jointly heroic family with bound two and derive a canonical necessary condition for every heroic family, but do not classify all minimal subfamilies.",
  "would_publish": false,
  "caveats": "Literally using a directed edge instead of an independent pair makes the problem trivial; the four-pattern family is not proved inclusion-minimal."
}
```

## 1. Notational issue and reduction to tournaments

Write \(\overline{K_2}\) for two nonadjacent vertices and \(\overleftrightarrow{K_2}\) for a digon. The intended base set must be
\[
\{\overline{K_2},\overleftrightarrow{K_2}\}.
\]
Indeed, a loopless digraph has neither of these as an induced subdigraph exactly when every pair of vertices is joined by exactly one arc; that is, the digraph is a tournament. Consequently,
\[
\{\overline{K_2},\overleftrightarrow{K_2}\}\cup\mathcal H
\quad\text{is heroic}
\]
if and only if the class of \(\mathcal H\)-free tournaments has bounded dichromatic number. For tournaments, the dichromatic number is the minimum number of transitive subtournaments partitioning the vertex set.

If the displayed \(\overrightarrow{K_2}\) is interpreted literally as a single directed edge, then avoiding both \(\overrightarrow{K_2}\) and \(\overleftrightarrow{K_2}\) forces an edgeless digraph. The base pair is then already heroic with bound \(1\), and no nonempty extension can be inclusion-minimal. Everything below addresses the evidently intended \(\overline{K_2}\) formulation.

Call a finite family of tournaments jointly heroic if its simultaneous exclusion gives bounded tournament dichromatic number.

---

## 2. Tournament operations and two standard facts

For tournaments \(A,B,C\), let
\[
\Delta(A,B,C)
\]
be their cyclic composition: all arcs go from \(A\) to \(B\), from \(B\) to \(C\), and from \(C\) to \(A\). Let \(C_3\) denote the directed triangle and \(T_r\) the transitive tournament of order \(r\).

A module of a tournament \(T\) is a vertex set \(M\) such that every vertex outside \(M\) either dominates all of \(M\) or is dominated by all of \(M\). A tournament is prime if it has no nontrivial module.

I use two standard structural results.

1. **Prime reduction.** Every prime tournament of order at least five contains a prime tournament of order five. There are three prime tournaments of order five, up to isomorphism; denote their set by
   \[
   \mathcal P_5.
   \]
   This is the usual prime-subtournament lemma. One proof starts with an induced \(C_3\) and uses the standard one-or-two-vertex extension lemma for prime tournaments; since there is no prime tournament of order four, the first extension has order five.

2. **The hero structure theorem.** In the formulation relevant here, heroes are generated from \(K_1\) by ordered sums and by cyclic compositions having one singleton part, one transitive part, and one recursively heroic part, with both cyclic orientations allowed. In particular:
   - a prime hero with at least three vertices is \(C_3\);
   - every prime tournament on five vertices is a nonhero;
   - \(\Delta(C_3,C_3,K_1)\) is a nonhero.

The second item is the single-tournament characterization referred to in the question.

---

## 3. A finite forbidden basis for the class of hero tournaments

The following useful consequence explains the small patterns that appear below. Define
\[
A_6=\Delta(T_2,T_2,T_2),\qquad
B_7=\Delta(C_3,C_3,K_1),
\]
of orders \(6\) and \(7\), respectively, and put
\[
\mathcal B=\mathcal P_5\cup\{A_6,B_7\}.
\]

### Proposition 3.1
A tournament is a hero if and only if it contains no member of \(\mathcal B\) as an induced subtournament.

Moreover, every hero tournament is \(2\)-colorable.

### Proof

Heroicity is hereditary under taking induced subtournaments: if \(J\) is induced in a hero \(H\), then every \(J\)-free tournament is also \(H\)-free. Thus \(J\) is a hero.

Each member of \(\mathcal B\) is a nonhero:

- every member of \(\mathcal P_5\) is prime and is not \(C_3\);
- \(A_6\) has cyclic modular decomposition with all three maximal bags of order two, so it has no singleton bag of the kind required by the hero structure theorem;
- \(B_7\) has two nontransitive \(C_3\)-bags besides its singleton bag, whereas the hero construction requires one of the other bags to be transitive.

Hence no hero contains a member of \(\mathcal B\).

Conversely, let \(T\) be \(\mathcal B\)-free, and induct on \(|V(T)|\).

- If \(T\) is not strongly connected, its strong components are linearly ordered. Each component is \(\mathcal B\)-free and hence a hero by induction, so their ordered sum is a hero.
- Suppose \(T\) is strongly connected. If \(T\) is prime, then the prime-reduction lemma shows that either \(T=C_3\), or \(T\) contains a member of \(\mathcal P_5\). Thus the prime case gives \(T=C_3\).
- Otherwise modular decomposition gives
  \[
  T=\Delta(T_1,T_2,T_3).
  \]
  Each \(T_i\) is a hero by induction. Since \(T\) is \(A_6\)-free, at least one \(T_i\) is a singleton: if all three had at least two vertices, selecting two vertices from each would induce \(A_6\). Suppose \(T_3=K_1\). Since \(T\) is \(B_7\)-free, at least one of \(T_1,T_2\) is transitive: otherwise each contains a \(C_3\), and these two triangles together with the singleton induce \(B_7\). The hero structure theorem now shows that \(T\) is a hero.

Finally, the recursive hero construction preserves \(2\)-colorability. Ordered sums can reuse the same two colors. If
\[
T=\Delta(H,T_r,K_1)
\]
and \(H=H_1\cup H_2\) is partitioned into two transitive sets, then, according to the cyclic order, one may use
\[
H_1\cup T_r,\qquad H_2\cup K_1
\]
as two transitive color classes. The reverse orientation is analogous. Thus every hero is \(2\)-colorable. \(\square\)

This proposition concerns which individual tournaments are heroes. It does not characterize jointly heroic families: notably, one of the five basis obstructions can be allowed while bounded colorability persists, as follows.

---

## 4. A four-tournament jointly heroic family of nonheroes

Let
\[
\mathcal Q=\mathcal P_5\cup\{B_7\}.
\]
Since \(\mathcal P_5\) consists of three isomorphism types, \(\mathcal Q\) has four members.

### Theorem 4.1
Every \(\mathcal Q\)-free tournament is \(2\)-colorable. Hence
\[
\{\overline{K_2},\overleftrightarrow{K_2}\}\cup\mathcal Q
\]
is heroic, with bound \(2\).

All four members of \(\mathcal Q\) are nonheroes.

### Proof

Let \(T\) be \(\mathcal Q\)-free. We induct on \(|V(T)|\).

If \(T\) is not strongly connected, its strong components are linearly ordered. By induction each is \(2\)-colorable, and the same two colors can be reused across the ordered components.

Suppose \(T\) is strongly connected.

If \(T\) is prime, then the prime-reduction lemma and \(\mathcal P_5\)-freeness imply \(T=C_3\), which is \(2\)-colorable.

Otherwise modular decomposition gives
\[
T=\Delta(T_1,T_2,T_3).
\]
Each \(T_i\) is \(\mathcal Q\)-free and hence \(2\)-colorable by induction.

At most one \(T_i\) is nontransitive. Indeed, if two bags were nontransitive, each would contain a directed triangle; choosing those two triangles and one vertex from the third bag would induce
\[
\Delta(C_3,C_3,K_1)=B_7.
\]

Suppose, after cyclic relabelling, that only \(T_1\) may be nontransitive. Write
\[
V(T_1)=X_1\cup X_2
\]
with \(X_1,X_2\) transitive. Since \(T_2,T_3\) are themselves transitive, the two sets
\[
X_1\cup V(T_2),\qquad X_2\cup V(T_3)
\]
are transitive: each uses only two bags of the cyclic composition, and all arcs between those bags go in one direction. They therefore give a \(2\)-coloring of \(T\).

The members of \(\mathcal P_5\) and \(B_7\) are nonheroes by the hero structure theorem, as noted above. \(\square\)

The bound \(2\) is sharp because \(C_3\) is \(\mathcal Q\)-free.

---

## 5. A canonical unbounded sequence and a necessary condition

Define tournaments \(X_r\) recursively by
\[
X_1=C_3,\qquad
X_{r+1}=\Delta(X_r,X_r,K_1).
\]

### Lemma 5.1
For every \(r\ge 1\):

1. \(X_r\) has no prime induced subtournament of order at least four;
2. \(\vec\chi(X_r)=r+1\).

### Proof

For the first assertion, consider a prime induced subtournament \(P\) of
\[
X_{r+1}=\Delta(A,B,\{z\}),
\qquad A,B\simeq X_r.
\]
If \(P\) meets a top-level bag, say \(A\), in at least two vertices and also has a vertex outside \(A\), then \(P\cap A\) is a nontrivial module of \(P\). Thus a prime subtournament crossing the top-level bags uses at most one vertex from each bag and consequently has order at most three. A larger prime subtournament must lie wholly inside \(A\) or \(B\), and induction applies.

For the chromatic number, let \(q=\vec\chi(X_r)\). Using optimal \(q\)-colorings of the two copies of \(X_r\), with corresponding colors reused across the two bags, and assigning a new color to the singleton gives
\[
\vec\chi(X_{r+1})\le q+1.
\]

Conversely, suppose \(X_{r+1}\) had a \(q\)-coloring. Each of the two copies of \(X_r\) requires all \(q\) colors, so every color occurs in both copies. If the singleton \(z\) receives color \(c\), choose color-\(c\) vertices \(a\in A\) and \(b\in B\). Then
\[
a\to b\to z\to a
\]
is a monochromatic directed triangle, a contradiction. Hence
\[
\vec\chi(X_{r+1})=q+1.
\]
Since \(\vec\chi(C_3)=2\), the result follows. \(\square\)

### Consequences

1. **No family consisting solely of prime tournaments of order at least five is jointly heroic.**  
   Every \(X_r\) avoids all such tournaments, while \(\vec\chi(X_r)\to\infty\).

2. **Every finite jointly heroic family \(\mathcal H\) must meet the induced age of \((X_r)\):**
   \[
   \exists H\in\mathcal H,\ \exists r\quad H\le_{\mathrm{ind}}X_r.
   \]
   Otherwise the entire unbounded sequence would be \(\mathcal H\)-free.

3. In particular, a minimal jointly heroic family of at least two tournaments must contain a decomposable nonhero; a family of prime nonheroes cannot work.

4. Any jointly heroic subfamily of \(\mathcal Q\) must contain \(B_7\), because a subfamily of \(\mathcal P_5\) alone is avoided by every \(X_r\).

---

## 6. A concrete finite reduction for minimal families

Since \(\mathcal Q\) is jointly heroic and finite, it contains an inclusion-minimal jointly heroic subfamily \(\mathcal Q_0\).

No singleton subfamily is heroic because all members of \(\mathcal Q\) are nonheroes. By Lemma 5.1, \(\mathcal Q_0\) must contain \(B_7\). Therefore
\[
\mathcal Q_0=\{B_7\}\cup\mathcal S
\]
for some nonempty \(\mathcal S\subseteq\mathcal P_5\), and
\[
2\le |\mathcal Q_0|\le 4.
\]

Thus there exists a genuinely multi-tournament minimal heroic family among the seven candidates
\[
\{B_7\}\cup\mathcal S,
\qquad \varnothing\ne\mathcal S\subseteq\mathcal P_5.
\]

What is not settled here is which of the six proper choices of \(\mathcal S\) are jointly heroic. In particular, I have not proved that the displayed four-member family \(\mathcal Q\) itself is inclusion-minimal. Resolving those seven finite cases would be a sharply defined first subproblem, but it would still not classify minimal families containing larger tournaments.

## 7. Remaining gap

The full requested characterization remains open in this writeup. The established partial information is:

- every minimal family with at least two members consists entirely of nonheroes;
- it must contain a tournament induced in some \(X_r\), hence cannot consist only of prime tournaments;
- the four explicit nonheroes \(\mathcal P_5\cup\{\Delta(C_3,C_3,K_1)\}\) are jointly heroic with optimal bound \(2\);
- consequently, some minimal jointly heroic family has between two and four members and is contained in that explicit four-element set.

No sufficiency criterion for arbitrary finite families, and no classification of all their minimal members, is proved here.