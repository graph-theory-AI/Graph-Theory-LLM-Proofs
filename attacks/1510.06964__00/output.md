```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For every 3-colour-compatible triangular torus, all nonsurjective 5-colourings lie in one Kempe class; this proves validity for all such tori of order at most 15 and, by a further argument, for the 18-vertex tori T_{3,6} and T_{6,3}.",
  "would_publish": false,
  "caveats": "Larger surjective colourings and periods that destroy the natural tripartition remain unresolved; the precise hypotheses of arXiv:2206.13126 were not independently checked here."
}
```

# 1. Model and statement of the partial result

Let
\[
T_\Lambda=\operatorname{Cay}\bigl(\mathbb Z^2/\Lambda,
 \{\pm(1,0),\pm(0,1),\pm(1,1)\}\bigr),
\]
where the quotient is assumed to be a simple cellular triangulation of the torus. Thus \(T_\Lambda\) is 6-regular, with
\[
|E(T_\Lambda)|=3|V(T_\Lambda)|.
\]

The natural 3-colouring of the infinite triangular lattice is
\[
\tau(x,y)=x+y\pmod 3.
\]
It descends to \(T_\Lambda\) precisely when
\[
\Lambda\subseteq\ker \tau.
\]
For the rectangular torus
\[
T_{m,n}=T_{\langle(m,0),(0,n)\rangle},
\]
this means \(3\mid m\) and \(3\mid n\). Write the three canonical independent sets as
\[
P_0,P_1,P_2.
\]
Every vertex has exactly three neighbours in each of the other two parts.

Let \(\mathcal K_0\) denote the Kempe class containing the canonical 3-colourings, regarded as 5-colourings.

We prove the following.

**Partial theorem.** Let \(T=T_\Lambda\) be a 3-colour-compatible triangular torus.

1. Every proper 5-colouring that omits a colour belongs to \(\mathcal K_0\).
2. More generally, a colouring belongs to \(\mathcal K_0\) if:
   - some colour occurs only in one canonical part; or
   - some canonical part omits at least two colours; or
   - some colour class has size at most \(2\); or
   - all but exactly one vertex of some colour lie in one canonical part.
3. Consequently, all 5-colourings of \(T\) are Kempe equivalent when \(|V(T)|\le 15\).
4. The same conclusion holds for \(T_{3,6}\) and \(T_{6,3}\).

Thus, in particular, the fifth colour joins all of the distinct \(q=4\) Kempe sectors on every 3-colour-compatible triangular torus. The unresolved issue is whether every surjective 5-colouring on a larger torus can be brought into this class.

# 2. A bipartite collapse lemma

We first record an elementary lemma.

**Lemma 2.1.** Let \(H\) be bipartite with fixed bipartition \(X\cup Y\). Every proper colouring of \(H\) with a palette containing two distinct colours \(p,q\) is Kempe equivalent to the colouring that assigns \(p\) to all of \(X\) and \(q\) to all of \(Y\).

**Proof.**
For each colour \(r\ne p\), consider every component of \(H[p,r]\).

A nontrivial connected component has two bipartitions:

- the restriction of \(X\cup Y\);
- the two colour classes \(p\) and \(r\).

Hence either its \(X\)-vertices all have colour \(p\), or its \(X\)-vertices all have colour \(r\). Swap precisely the components of the second kind. Isolated \(X\)-vertices of colour \(r\) are swapped individually. After doing this for every \(r\ne p\), all vertices of \(X\) have colour \(p\).

Now every vertex of \(Y\) can be recoloured individually to \(q\): its neighbours all have colour \(p\), and \(q\ne p\). Each such recolouring is a singleton Kempe change. ∎

# 3. A large explicit Kempe basin

## 3.1. A colour confined to one canonical part

**Lemma 3.1.** If a colour \(a\) occurs only in one canonical part, say \(P_0\), then the colouring belongs to \(\mathcal K_0\).

This includes the case in which \(a\) is unused.

**Proof.**
For every vertex \(v\in P_0\) not currently coloured \(a\), the \(\{a,\alpha(v)\}\)-component containing \(v\) is a singleton: all \(a\)-coloured vertices lie in \(P_0\), and \(P_0\) is independent. Recolour these vertices one at a time. We reach a colouring in which all of \(P_0\) has colour \(a\).

The graph \(T-P_0\) is bipartite with parts \(P_1,P_2\), and it uses only the other four colours. By Lemma 2.1 it can be Kempe-collapsed to two colours, without changing \(P_0\). We have therefore reached a canonical 3-colouring. ∎

An immediate consequence is important.

**Corollary 3.2.** All nonsurjective proper 5-colourings of a 3-colour-compatible triangular torus lie in one Kempe class.

In particular, all proper 4-colourings, including those separated by the usual \(q=4\) topological obstruction, become equivalent when the fifth colour is allowed.

## 3.2. Two colours absent from one part

**Lemma 3.3.** If a canonical part, say \(P_0\), contains no vertex of either colour \(a\) or colour \(b\), then the colouring belongs to \(\mathcal K_0\).

**Proof.**
The graph induced by colours \(a,b\) lies in the bipartite graph \(T-P_0\), with parts \(P_1,P_2\). In each nontrivial \(\{a,b\}\)-component, orient the two colours so that \(a\) lies on \(P_1\) and \(b\) on \(P_2\). Isolated vertices can likewise be assigned the appropriate one of \(a,b\) by a singleton switch.

After these changes, colour \(a\) is confined to \(P_1\). Lemma 3.1 applies. ∎

Thus every colouring outside \(\mathcal K_0\) must use at least four colours on each canonical part.

## 3.3. One outlying vertex

**Lemma 3.4.** Suppose all vertices of colour \(a\), except exactly one vertex \(x\in P_0\), lie in \(P_1\). Then the colouring belongs to \(\mathcal K_0\).

**Proof.**
If some colour \(b\ne a\) is absent from \(N(x)\), recolour \(x\) to \(b\) by a singleton Kempe change. Colour \(a\) is then confined to \(P_1\).

Otherwise all four other colours occur in \(N(x)\). The vertex \(x\) has three neighbours in \(P_1\) and three in \(P_2\). Let \(S_i\) be the set of colours appearing on its neighbours in \(P_i\). Then
\[
S_1\cup S_2=[5]\setminus\{a\},
\qquad |S_1|,|S_2|\le 3.
\]
Consequently \(S_1\nsubseteq S_2\). Choose
\[
b\in S_1\setminus S_2.
\]
All \(b\)-neighbours of \(x\) lie in \(P_1\).

The \(\{a,b\}\)-component containing \(x\) is now a star centred at \(x\): its \(b\)-vertices lie in \(P_1\), and they cannot be adjacent to any of the other \(a\)-vertices, which also lie in \(P_1\). Swapping this component replaces \(x\) by colour \(b\) and moves colour \(a\) only onto vertices of \(P_1\). Lemma 3.1 applies. ∎

Consequently:

- every colour class of size \(0\) or \(1\) is harmless;
- a colour class of size \(2\) is either contained in one part or has one vertex outside the part containing the other;
- a colour class of size \(3\) is harmless unless it has exactly one vertex in each canonical part.

# 4. Tori of order at most 15

**Theorem 4.1.** If \(T\) is a 3-colour-compatible triangular torus with \(|V(T)|\le 15\), then all proper 5-colourings of \(T\) are Kempe equivalent.

**Proof.**
Let \(\alpha\) be a proper 5-colouring.

If it omits a colour, use Corollary 3.2. If \(|V(T)|\le14\) and all five colours occur, some colour class has size at most \(2\), so Lemmas 3.1 and 3.4 apply.

It remains to consider \(|V(T)|=15\). If some colour class has size at most \(2\), we are done. Otherwise all five colour classes have size exactly \(3\).

If one of these classes is not distributed as one vertex in each \(P_i\), its distribution is either \(3+0+0\) or \(2+1+0\); Lemma 3.1 or Lemma 3.4 applies. We may therefore suppose that every colour occurs exactly once in each canonical part.

Fix two colours \(a,b\), and let \(C\) be a component of \(T[a,b]\). Write
\[
x_i=|C\cap\alpha^{-1}(a)\cap P_i|,
\qquad
y_i=|C\cap\alpha^{-1}(b)\cap P_i|.
\]
If \(\sum_i x_i\ne\sum_i y_i\), swapping \(C\) leaves one of the two colour classes with size at most \(2\), putting the colouring in \(\mathcal K_0\).

If the totals are equal but \((x_0,x_1,x_2)\ne(y_0,y_1,y_2)\), then after the swap one of the two size-3 colour classes is no longer distributed \(1+1+1\), and again Lemma 3.1 or 3.4 applies.

Thus, in any colouring outside \(\mathcal K_0\), every bichromatic component must satisfy
\[
x_i=y_i\qquad(i=0,1,2). \tag{4.1}
\]
Since there is only one \(a\)-vertex and one \(b\)-vertex in each \(P_i\), condition (4.1) says that a component contains either both of these vertices or neither. A connected component cannot contain just the two vertices in one canonical part, because that part is independent. Therefore every component accounts for at least two of the three canonical parts. The three parts cannot be partitioned into two or more subsets of size at least two. Hence \(T[a,b]\) is connected.

This holds for every one of the ten colour pairs. Each connected bichromatic graph has six vertices and hence at least five edges. Therefore
\[
|E(T)|\ge 10\cdot5=50.
\]
But \(T\) is 6-regular on 15 vertices, so
\[
|E(T)|=45,
\]
a contradiction. ∎

# 5. Structure at order 18

The same reasoning gives a useful narrowing at the next order.

Suppose \(\alpha\notin\mathcal K_0\) on an 18-vertex torus. Then:

1. every colour class has size at least \(3\);
2. every size-3 colour class has one vertex in each canonical part;
3. for any two size-3 colours \(a,b\), the graph \(T[a,b]\) is connected;
4. every vertex in a size-3 class has a neighbour in each of the other four colours—otherwise a singleton Kempe change reduces that class to size \(2\).

Since the six possible type-pairs
\[
(a,P_i),\ (b,P_i)\qquad(i=0,1,2)
\]
form a 6-cycle of allowable adjacencies, a connected graph \(T[a,b]\) is either a spanning path or the whole 6-cycle. In particular,
\[
5\le e_{ab}\le6. \tag{5.1}
\]

The possible colour-class size patterns are
\[
(6,3,3,3,3),\qquad
(5,4,3,3,3),\qquad
(4,4,4,3,3).
\]

The first two are impossible outside \(\mathcal K_0\).

For \((6,3,3,3,3)\), let \(L\) be the size-6 class and \(S\) the four small colours. Degree counting gives
\[
72
 =2\sum_{\{a,b\}\subset S}e_{ab}
   +\sum_{a\in S}e_{aL}
 \ge 2\binom42 5+4\cdot3
 =72.
\]
Thus equality holds, in particular \(e_{aL}=3\) for each \(a\in S\).

But \(L\) is an independent set of size \(18/3=6\), attaining the maximum possible size. Counting incidences with triangular faces shows that every face contains exactly one \(L\)-vertex. Around every vertex outside \(L\), the \(L\)-neighbours therefore alternate around the six-neighbour cycle, so every such vertex has exactly three \(L\)-neighbours. Hence \(e_{aL}=9\), a contradiction.

For \((5,4,3,3,3)\), let \(X,Y\) have sizes \(4,5\), and let \(S\) be the three size-3 colours. Put
\[
R=\sum_{\{a,b\}\subset S}(e_{ab}-5),\quad
P=\sum_{a\in S}(e_{aX}-3),\quad
Q=\sum_{a\in S}(e_{aY}-3).
\]
All three quantities are nonnegative. Summing degrees over the three small classes gives
\[
2R+P+Q=6.
\]
The degree equations for \(X\) and \(Y\) give
\[
e_{XY}=15-P=21-Q,
\]
so \(Q-P=6\). Therefore \(R=P=0\), \(Q=6\), and
\[
e_{XY}=15.
\]
However, a vertex has at most three neighbours of any one colour, since its neighbours contain a 6-cycle. Hence
\[
e_{XY}\le 3|X|=12,
\]
a contradiction.

Thus an exceptional 18-vertex colouring would necessarily have class sizes
\[
(4,4,4,3,3). \tag{5.2}
\]

# 6. The \(T_{3,6}\) torus

We now rule out the remaining pattern (5.2) for \(T_{3,6}\).

Regard \(T_{3,6}\) as six cyclic rows
\[
R_0,\ldots,R_5,
\]
each of which is a triangle on positions \(x\in\mathbb Z_3\). Between \(R_y\) and \(R_{y+1}\), a vertex at position \(x\) is adjacent to positions \(x\) and \(x+1\). Thus two equal-coloured vertices in consecutive rows must occur at positions
\[
x,\quad x-1. \tag{6.1}
\]
Their canonical part \(x+y\pmod3\) is therefore constant along a consecutive run.

Assume for contradiction that \(\alpha\notin\mathcal K_0\). Let \(a,b\) be the two size-3 colours.

Each of \(a,b\) has one vertex in each canonical part. By (6.1), it cannot occur in consecutive rows. Hence each occupies either all even rows or all odd rows. Since \(T[a,b]\) is connected, they cannot occupy the same parity of rows: in that case \(T[a,b]\) would be three disjoint same-row edges. Thus \(a\) and \(b\) occupy opposite row parities, and each row contains exactly one of them.

Let the size-4 colours be \(X,Y,Z\). Each occurs in four of the six rows. If its two omitted rows are adjacent, its four occurrences form one consecutive run and lie in a single canonical part. If the omitted rows are at cyclic distance two, its occurrences form runs of lengths \(3\) and \(1\), giving either a confined class or a \(3+1\) class. Both possibilities lie in \(\mathcal K_0\).

Therefore the two omitted rows for each of \(X,Y,Z\) must be opposite. Since every row contains exactly two of these three colours, after relabelling we may assume
\[
\begin{aligned}
X&\text{ is absent from }R_0,R_3,\\
Y&\text{ is absent from }R_1,R_4,\\
Z&\text{ is absent from }R_2,R_5.
\end{aligned}
\]
The unique large colour common to \(R_y,R_{y+1}\) is consequently, cyclically,
\[
Z,X,Y,Z,X,Y.
\]

Let \(u_y\in\mathbb Z_3\) be the position in \(R_y\) of this common colour. By (6.1), its position in \(R_{y+1}\) is \(u_y-1\). In row \(R_y\), the incoming common colour has position \(u_{y-1}-1\). These are the two large-colour positions, so they are distinct:
\[
u_y-u_{y-1}\in\{0,1\}\pmod3.
\]
Set
\[
d_y=u_y-u_{y-1}\in\{0,1\}.
\]

Let \(p_y\) be the position of the small colour \(a\) or \(b\) in \(R_y\). Since the three positions sum to \(0\) modulo \(3\),
\[
p_y=1-u_y-u_{y-1}.
\]
The small vertices in \(R_y,R_{y+1}\) fail to be adjacent precisely when
\[
p_{y+1}=p_y-1,
\]
which is equivalent to
\[
d_y+d_{y+1}=1.
\]
Thus a missing edge of \(T[a,b]\) corresponds exactly to a transition in the cyclic binary word
\[
d_0d_1\cdots d_5.
\]

But \(T[a,b]\) is connected on its six alternating row vertices, so at most one of the six possible consecutive-row edges is missing. A cyclic binary word has an even number of transitions. Hence it has no transitions, and all \(d_y\) are equal.

If all \(d_y=0\), then \(u_{y+3}=u_y\). If all \(d_y=1\), then also
\[
u_{y+3}=u_y+3=u_y\pmod3.
\]
In either case, the two length-2 runs of each of \(X,Y,Z\) lie in the same canonical part. That size-4 colour is therefore confined to one part, contrary to \(\alpha\notin\mathcal K_0\).

This contradiction proves:

**Theorem 6.1.** All proper 5-colourings of \(T_{3,6}\), and hence also of the isomorphic \(T_{6,3}\), are Kempe equivalent. ∎

# 7. What remains open

For a 3-colour-compatible torus, any counterexample Kempe class must consist entirely of surjective colourings satisfying all of the following:

- every colour class has size at least \(3\);
- every canonical part contains at least four colours;
- no colour is confined to one canonical part;
- no colour has all but one of its vertices in a single canonical part;
- every size-3 colour is a transversal of the three canonical parts;
- every two size-3 colours induce a connected spanning path or cycle on their six vertices.

The first standard rectangular cases are now settled:
\[
T_{3,3},\qquad T_{3,6},\qquad T_{6,3}.
\]
The argument does not settle \(T_{3,9}\), \(T_{6,6}\), larger tori, or periodic quotients on which the natural 3-colouring does not descend.

Finally, the supplied description of Salas–Sokal, arXiv:2206.13126, does not state its additional structural hypotheses. Six-regularity and Eulerianity alone are not enough to verify those hypotheses. I have therefore not treated that preprint as an established resolution of the precise family considered here.