```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The implication holds for every graph when 2≤k≤6, and for every k when every chordless cycle has length at most nine.",
  "would_publish": false,
  "caveats": "The general case for arbitrary graphs and k≥7 remains unresolved; novelty relative to the full source paper has not been independently checked."
}
```

# Partial results

I use exactly the adjacency specified in the question: consecutive flows may differ by an arbitrary nonzero flow supported on one cycle.

The lifting and connected-fibre arguments in the previous attempt are valid under this definition; I reproduce their proofs below. The new ingredient is a **divisor-increment lemma**: a modular cycle move whose increment divides \(k\) can always be simulated between integer lifts, even when that particular modular edge has no directly adjacent lifts. In particular, this handles the missing increment \(3\) for \(k=6\).

I also strengthen the short-cycle result, and then use chords to obtain the following.

## Theorem

Let \(G\) be a finite graph. Reduction modulo \(k\) induces a bijection between the connected components of
\[
\mathcal F(G,k)
\quad\text{and}\quad
\mathcal F(G,\mathbb Z_k)
\]
in each of the following cases:

1. \(2\le k\le 6\), with no restriction on \(G\);
2. \(k\ge2\) is arbitrary, and every chordless cycle of \(G\) has length at most \(9\);
3. \(k\in\{7,8\}\), and every chordless cycle of \(G\) has length at most \(21\).

Consequently, the implication in the question holds in these cases.

Here a chord joins two nonconsecutive vertices of a cycle. For simple graphs, chordless cycles are precisely induced cycles.

The theorem does **not** assert that either reconfiguration graph is always connected. It asserts that their component partitions correspond under reduction.

---

# 1. Definitions and connected fibres

Fix an orientation of \(G\), and let
\[
(\partial x)(v)=
\sum_{e\in\delta^+(v)}x(e)-\sum_{e\in\delta^-(v)}x(e).
\]

An integer nowhere-zero \(k\)-flow is an integral circulation \(f\) satisfying
\[
1\le |f(e)|\le k-1
\qquad(e\in E(G)).
\]
A nowhere-zero \(\mathbb Z_k\)-flow is a circulation over \(\mathbb Z_k\) with every coordinate nonzero.

For a cyclically oriented cycle \(C\), write \(\chi_C\) for its signed incidence vector. Adjacent integer flows differ by \(t\chi_C\), for some nonzero integer \(t\); adjacent modular flows differ by \(a\chi_C\), for some nonzero \(a\in\mathbb Z_k\).

## Lemma 1.1: existence of bounded integer lifts

Every nowhere-zero \(\mathbb Z_k\)-flow has a nowhere-zero integer \(k\)-flow lifting it.

**Proof.**
Let \(\varphi\) be a modular flow, and let
\[
p(e)\in\{1,\ldots,k-1\}
\]
be its standard representatives. Set
\[
h=\frac{\partial p}{k}\in\mathbb Z^{V(G)}.
\]
The bounded-flow polytope
\[
P=\{q\in[0,1]^{E(G)}:\partial q=h\}
\]
is nonempty, since it contains \(p/k\). Integrality of bounded network flows gives an integral point \(q\in P\). Equivalently, this follows from total unimodularity of the incidence matrix.

Then
\[
f=p-kq
\]
is a circulation, and each \(f(e)\) is either \(p(e)\) or \(p(e)-k\). Thus \(f\) is a nowhere-zero integer \(k\)-flow lifting \(\varphi\). \(\square\)

The same argument lifts a modular flow that has zero coordinates: apply the lemma to its nonzero support, and put zero on the remaining edges.

## Lemma 1.2: each reduction fibre is connected

For every modular flow \(\varphi\), the subgraph induced by its integer lifts is connected.

**Proof.**
With \(p,h\) as above, the lifts are precisely
\[
p-kq,\qquad
q\in\{0,1\}^{E(G)},\quad \partial q=h.
\]
For two such vectors \(q,q'\), the difference \(q'-q\) is an integral circulation with coordinates in \(\{-1,0,1\}\). Orient its support according to its signs. This is an Eulerian directed graph, so it decomposes into edge-disjoint directed cycles.

Adding these signed cycle vectors to \(q\), one at a time, keeps every coordinate in \(\{0,1\}\) and keeps its boundary equal to \(h\). On the integer-flow side, each step is a cycle move with increment \(k\) or \(-k\). \(\square\)

Reduction sends an integer reconfiguration edge to either a modular reconfiguration edge or a single vertex. Thus the preceding lemmas have the following useful consequence:

> To show that reduction induces a bijection on components, it suffices to show that the endpoints of every modular reconfiguration edge have integer lifts in the same integer component.

The lifts at successive stages need not be the same lifts: Lemma 1.2 lets us connect any two choices within a fibre.

---

# 2. An exact criterion for directly lifting one edge

Suppose
\[
\psi=\varphi+a\chi_C,
\qquad 1\le a\le k-1,
\]
is a modular reconfiguration edge. Orient \(C\) cyclically, and let \(p\) represent \(\varphi\) as above.

Since \(\psi\) is nowhere-zero, no edge of \(C\) has \(p(e)=k-a\). Partition \(C\) into
\[
H=\{e\in C:p(e)>k-a\},
\qquad
L=\{e\in C:p(e)<k-a\}.
\]

Consider the two systems
\[
\tag{A}
\partial q=h,\qquad q\in\{0,1\}^{E(G)},\qquad q(e)=1\quad(e\in H),
\]
and
\[
\tag{B}
\partial q=h,\qquad q\in\{0,1\}^{E(G)},\qquad q(e)=0\quad(e\in L).
\]

## Proposition 2.1

The modular edge \(\varphi\psi\) has directly adjacent integer lifts if and only if at least one of (A) and (B) is feasible.

**Proof.**
If (A) is feasible, put \(f=p-kq\). Then
\[
f+a\chi_C
\]
is a valid integer \(k\)-flow lifting \(\psi\). On an edge of \(H\), forcing \(q(e)=1\) makes the new value
\[
p(e)-k+a\in\{1,\ldots,a-1\}.
\]
On an edge of \(L\), either choice of \(q(e)\) gives a valid new value.

Similarly, a solution to (B) makes
\[
f+(a-k)\chi_C
\]
a valid adjacent lift.

Conversely, adjacent lifts must differ by \(t\chi_C\), where
\[
t\equiv a\pmod k,\qquad |t|\le 2k-2.
\]
The only possibilities are
\[
a,\quad a-k,
\quad\text{and possibly }a+k,\ a-2k.
\]
The increment \(a\) forces \(q=1\) on \(H\), and \(a-k\) forces \(q=0\) on \(L\).

If \(t=a+k\), every edge of \(C\) must start at its negative representative and finish at \(p(e)+a\). Consequently \(H=\varnothing\), so (A) is unconstrained and feasible. Likewise, \(t=a-2k\) forces \(L=\varnothing\), making (B) feasible. \(\square\)

The bounded-flow cut criterion gives equivalent formulations:
\[
\tag{2.1}
\text{(A) is feasible}\quad\Longleftrightarrow\quad
h(X)\ge |H\cap\delta^+(X)|-|\delta^-(X)|
\quad\text{for every }X\subseteq V(G),
\]
and
\[
\tag{2.2}
\text{(B) is feasible}\quad\Longleftrightarrow\quad
h(X)\le |\delta^+(X)\setminus L|
\quad\text{for every }X\subseteq V(G).
\]
These criteria apply first to real bounded flows; integrality then gives \(0\)-\(1\) solutions. In particular, direct-edge liftability is decidable by bounded-flow feasibility computations.

## Lemma 2.2: increments \(\pm1,\pm2\) lift directly

Every valid modular cycle move with increment in
\[
\{1,2,k-2,k-1\}
\]
has directly adjacent integer lifts.

**Proof.**
For \(a=1\), the set \(H\) is empty, so (A) is feasible.

For \(a=2\), the only possible elements of \(H\) have \(p(e)=k-1\). The vector
\[
q^*=\frac{p+\chi_C}{k}
\]
belongs to \([0,1]^{E(G)}\), has boundary \(h\), and equals \(1\) on \(H\). Thus it is a fractional witness for (A), and bounded-flow integrality supplies the required integral witness.

Reversing a move handles increments \(-1,-2\). \(\square\)

This already proves component correspondence for \(2\le k\le5\).

---

# 3. Divisor increments can always be bypassed

The next result concerns paths between lifts, not necessarily direct lifting of the given modular edge.

## Lemma 3.1: divisor-increment lemma

Let \(d\) be a positive proper divisor of \(k\). If two nowhere-zero \(\mathbb Z_k\)-flows differ by
\[
d\chi_C
\]
on a cycle, then their integer lifts belong to the same component of \(\mathcal F(G,k)\).

The same holds for increment \(-d\).

### Proof

The case \(d=1\) follows from Lemma 2.2. Suppose \(d\ge2\), and write
\[
k=dm.
\]

Let
\[
\psi=\varphi+d\chi_C,
\qquad
\rho=\varphi\bmod d=\psi\bmod d.
\]
Set
\[
H=\{e:\rho(e)\ne0\},\qquad M=E(G)\setminus H.
\]

By Lemma 1.1, \(\rho\) has an integer \(d\)-flow lift \(s\) on \(H\). Extend \(s\) by zero on \(M\), and reorient the edges of \(H\) so that
\[
1\le s(e)\le d-1\qquad(e\in H).
\]
Because \(s\) is a positive circulation on \(H\), every connected component of this oriented subgraph is strongly connected.

We first identify a family of directly liftable moves.

### Step 1: cycles directed on \(H\) are safe

Let \(\eta\) be any nowhere-zero \(\mathbb Z_k\)-flow reducing to \(\rho\) modulo \(d\). Suppose \(D\) is a cycle that follows the orientation of \(s\) on every edge of \(D\cap H\), and that
\[
\eta+d\chi_D
\]
is nowhere-zero.

Orient \(D\) cyclically. This does not reverse any edge of \(H\); it may reorient edges of \(M\), on which \(s=0\).

Let \(p\) be the standard representatives of \(\eta\). We can write
\[
p(e)=s(e)+d\,b(e)\quad(e\in H),
\qquad b(e)\in\{0,\ldots,m-1\},
\]
and
\[
p(e)=d\,b(e)\quad(e\in M),
\qquad b(e)\in\{1,\ldots,m-1\}.
\]
Thus
\[
q^0=\frac{p-s}{k}
\]
has boundary \(\partial p/k\).

Consider
\[
q^*=q^0+\frac1m\chi_D.
\]
On \(D\cap H\), this changes \(b(e)/m\) to \((b(e)+1)/m\), which lies in \([0,1]\).

On \(D\cap M\), validity of the modular move excludes \(b(e)=m-1\), so again \(q^*(e)\in[0,1]\). All other coordinates are unchanged.

Moreover, an edge of \(D\) satisfying \(p(e)+d>k\) must lie in \(H\) and have \(b(e)=m-1\). On every such edge, \(q^*(e)=1\).

Therefore \(q^*\) is a fractional witness for system (A) in Proposition 2.1. Integrality shows that the move on \(D\) lifts directly.

### Step 2: directed cycles generate all modular circulations on \(H\)

For later use, every \(\mathbb Z_m\)-circulation on \(H\) is a sum, modulo \(m\), of directed cycle vectors in the orientation of \(s\).

Indeed, lift such a modular circulation to an integral circulation \(z\) on \(H\). For a sufficiently large integer \(N\),
\[
z+Nm\,s
\]
is nonnegative on every edge of \(H\). It is an integral circulation, so it decomposes into directed cycles. Its reduction modulo \(m\) is the original modular circulation.

Consequently, any change supported on \(H\) that is a multiple of \(d\) can be effected by a sequence of moves \(+d\chi_D\) on directed cycles of \(H\). Every intermediate flow remains nonzero on \(H\), because its reduction modulo \(d\) is \(\rho\). By Step 1, all these moves lift directly.

### Step 3: reroute the original cycle through \(H\)

If \(C\subseteq H\), Step 2 already connects \(\varphi\) to \(\psi\).

Otherwise, retain each edge of \(C\cap M\), with its cyclic direction. Replace each intervening subpath of \(C\) lying in \(H\) by a directed path in \(H\) with the same endpoints. Such paths exist because the relevant components of \(H\) are strongly connected.

The result is a directed closed walk \(W\). It uses each edge of \(C\cap M\) exactly once, uses no other edge of \(M\), and may repeat edges of \(H\).

Decompose \(W\) into directed simple cycles, and apply increment \(d\) along these cycles one at a time.

- On \(M\), each affected edge changes exactly once, from its value in \(\varphi\) to its value in \(\psi\); hence it never becomes zero.
- On \(H\), the reduction modulo \(d\) remains nonzero, so no value becomes zero.
- Each cycle follows the fixed orientation on \(H\), so Step 1 directly lifts every move.

Let the resulting modular flow be \(\varphi^*\). It agrees with \(\psi\) on \(M\), and
\[
\psi-\varphi^*
\]
is supported on \(H\), is divisible by \(d\), and is a circulation. Step 2 connects \(\varphi^*\) to \(\psi\) through directly liftable moves.

Finally, connectedness of each integer fibre allows these directly lifted moves to be concatenated into an integer reconfiguration path. Reversing a path handles increment \(-d\). \(\square\)

## Consequence for \(k=6\)

Every nonzero increment in \(\mathbb Z_6\) is one of
\[
\pm1,\quad \pm2,\quad 3.
\]
The first four lift directly, and \(3\mid6\), so Lemma 3.1 handles the remaining increment.

This proves component correspondence for \(k=6\), completing part 1 of the theorem.

In particular, the direct-lifting obstruction at \(k=6\) in the previous attempt is not a component obstruction: the divisor lemma guarantees a detour between the corresponding fibres.

---

# 4. A lower bound on the length of a non-liftable cycle move

We next strengthen the previous attempt’s short-cycle result.

## Proposition 4.1

Suppose a modular move with increment \(a\), where \(1\le a\le k-1\), has no directly adjacent integer lifts. Then
\[
3\le a\le k-3
\]
and, with the partition \(C=H\sqcup L\) from Section 2,
\[
\tag{4.1}
|H|\ge 2\left\lceil\frac{k}{a-2}\right\rceil,
\qquad
|L|\ge 2\left\lceil\frac{k}{k-a-2}\right\rceil.
\]
In particular,
\[
\tag{4.2}
|C|\ge
2\left\lceil\frac{k}{a-2}\right\rceil+
2\left\lceil\frac{k}{k-a-2}\right\rceil.
\]

**Proof.**
Lemma 2.2 gives the asserted range of \(a\).

Since (A) is infeasible, some \(X\subseteq V(G)\) violates (2.1). For this \(X\), define
\[
E_X=k\left(h(X)-|H\cap\delta^+(X)|+|\delta^-(X)|\right).
\]
Then \(E_X\le-k\), because the expression in parentheses is an integer. Expanding,
\[
E_X=
\sum_{\delta^+(X)\setminus H}p(e)
+\sum_{\delta^+(X)\cap H}(p(e)-k)
+\sum_{\delta^-(X)}(k-p(e)).
\]

All terms from edges outside \(C\) are nonnegative. Because \(C\) is cyclically oriented, it has equally many edges entering and leaving \(X\). Pair those outgoing and incoming cycle edges arbitrarily.

For a pair consisting of an outgoing \(H\)-edge and an incoming \(H\)-edge, the contribution is
\[
p(e_{\rm out})-p(e_{\rm in})\ge -(a-2).
\]
Every other type of pair has nonnegative contribution:

- outgoing \(H\), incoming \(L\): at least \(2\);
- outgoing \(L\), incoming \(H\): at least \(2\);
- outgoing \(L\), incoming \(L\): positive.

There are at most \(\lfloor |H|/2\rfloor\) pairs of the first type. Hence
\[
E_X\ge -(a-2)\left\lfloor\frac{|H|}{2}\right\rfloor.
\]
Combining this with \(E_X\le-k\) gives the first inequality in (4.1).

Similarly, infeasibility of (B) supplies a cut \(Y\) for which
\[
\begin{aligned}
&k\left(|\delta^+(Y)\setminus L|-h(Y)\right)\\
&\qquad=
\sum_{\delta^+(Y)\setminus L}(k-p(e))
-\sum_{\delta^+(Y)\cap L}p(e)
+\sum_{\delta^-(Y)}p(e)
\le-k.
\end{aligned}
\]
Pairing outgoing and incoming cycle edges now shows that only an \(L,L\) pair can contribute negatively, and its contribution is at least \(-(k-a-2)\). This proves the second inequality. \(\square\)

## Corollary 4.2

Every modular cycle move supported on a cycle of length at most \(9\) lifts directly, for every \(k\).

**Proof.**
For a non-liftable move, put
\[
x=a-2,\qquad y=k-a-2.
\]
These are positive and satisfy \(x+y=k-4\). Therefore
\[
\frac{k}{x}+\frac{k}{y}
\ge \frac{4k}{k-4}>4.
\]
The sum of the two ceilings in (4.2) is consequently at least \(5\), giving \(|C|\ge10\). \(\square\)

For particular \(k\), (4.2) is stronger. For example:

- for \(k=7\), the only increments not covered by Lemma 2.2 are \(3,4\), and (4.2) gives \(|C|\ge22\);
- for \(k=8\), increment \(4\) is handled by Lemma 3.1, while increments \(3,5\) have the same lower bound \(22\).

---

# 5. Chords reduce the remaining moves to shorter cycles

## Lemma 5.1

Suppose a modular cycle move has increment \(a\), with
\[
2a\ne0\pmod k,
\]
and its cycle \(C\) has a chord. Then it can be replaced by two valid modular moves on strictly shorter cycles, both with increment \(a\) under suitable orientations.

**Proof.**
Let \(C_1,C_2\) be the two cycles formed by the chord, oriented so that
\[
\chi_C=\chi_{C_1}+\chi_{C_2}.
\]
Their directions on the chord are opposite.

There are two possible orders in which to apply the moves \(a\chi_{C_1}\) and \(a\chi_{C_2}\). If the current chord value, in one fixed orientation, is \(b\), the intermediate chord value is respectively
\[
b+a\quad\text{or}\quad b-a.
\]
Both could be zero only if \(2a=0\), contrary to the hypothesis. Thus at least one order keeps the chord nonzero.

Every other edge in the intermediate flow has either its initial value or its final value, so is also nonzero. Both cycles are strictly shorter than \(C\). \(\square\)

The only nonzero increment excluded from this lemma is \(a=k/2\), when \(k\) is even. That increment divides \(k\), so Lemma 3.1 already handles it on every cycle.

Now induct on the length of a cycle witnessing a modular move.

- If it is chordless and has length at most \(9\), Corollary 4.2 lifts the move directly.
- If it has a chord and the increment is not a half-turn, Lemma 5.1 reduces it to shorter cycles.
- A half-turn is handled by Lemma 3.1.

This proves part 2 of the theorem. Using the \(22\)-edge lower bounds noted above proves part 3 in exactly the same way.

---

# 6. The nine-edge direct-lifting bound is sharp

The following example shows that Corollary 4.2 cannot be improved from \(9\) to \(10\) as a statement about **direct** lifting. It is not a counterexample to the original conjecture.

Take \(k=24\). Let the main directed cycle be
\[
x_1y_1x_2y_2x_3y_3x_4y_4x_5y_5x_1.
\]
Assign values to its two edges in each block as follows:
\[
\begin{array}{c|cc}
i & x_i\to y_i & y_i\to x_{i+1}\\ \hline
1,2 &11&23\\
3,4,5&9&1
\end{array}
\]
with indices on the \(x_i\) interpreted cyclically.

Add the following arcs and values:
\[
\begin{array}{c|c}
\text{arc}&\text{value}\\ \hline
y_2\to y_1&12\\
y_3\to y_5&8\\
y_4\to y_5&8\\
x_2\to x_1&12\\
x_3\to x_1&14\\
x_1\to x_4&8\\
x_1\to x_5&8
\end{array}
\]

Call this assignment \(p\). Its integer boundary is zero at every vertex except
\[
(\partial p)(y_2)=24,\qquad
(\partial p)(y_5)=-24.
\]
Thus \(p\) defines a nowhere-zero \(\mathbb Z_{24}\)-flow \(\varphi\).

Let \(C\) be the main \(10\)-cycle and set
\[
\psi=\varphi+14\chi_C.
\]
The main-cycle values change as
\[
(11,23)\longmapsto(1,13),\qquad
(9,1)\longmapsto(23,15),
\]
so \(\psi\) is nowhere-zero.

Here \(H\) consists of the four edges with values \(11,23\), and \(L\) consists of the six edges with values \(9,1\).

For
\[
X=V(G)\setminus\{y_1,y_2\},
\]
the outgoing cut values sum to \(22\), and the incoming values sum to \(46\). Hence
\[
h(X)=-1,
\]
whereas
\[
|H\cap\delta^+(X)|-|\delta^-(X)|=2-2=0.
\]
Thus (A) is infeasible.

For
\[
Y=V(G)\setminus\{y_3,y_4,y_5\},
\]
the outgoing cut values sum to \(27\), and the incoming values sum to \(3\). Thus
\[
h(Y)=1,
\qquad
|\delta^+(Y)\setminus L|=0,
\]
so (B) is infeasible as well.

Proposition 2.1 shows that \(\varphi\psi\) has no directly adjacent integer lifts.

Nevertheless, this graph has only ten vertices and seventeen edges, and every \(10\)-cycle is chorded. Hence all its chordless cycles have length at most \(9\). The theorem above therefore guarantees that the fibres of \(\varphi\) and \(\psi\) are connected by an integer path. This illustrates precisely the distinction between direct lifting and path simulation.

---

# 7. What remains unresolved

The results prove the requested implication for all graphs through \(k=6\), and for the stated chordless-cycle classes for every \(k\).

They do not settle arbitrary graphs beginning with \(k=7\). For example, increment \(3\) in \(\mathbb Z_7\) is neither one of \(\pm1,\pm2\) nor a divisor increment, and the short-cycle argument only controls it on cycles of length at most \(21\). The chord argument does not address long chordless cycles.

No complete proof or counterexample for that remaining regime is established here.