```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The implication holds for every graph when 2≤k≤5, and for every k when all cycles have length at most three, but the general case remains open.",
  "would_publish": false,
  "caveats": "This uses the standard adjacency notion that consecutive flows may differ by an arbitrary nonzero flow supported on one cycle; for k≥6 a modular edge need not lift directly."
}
```

# 1. Statement of the partial result

Fix an orientation of \(G\). I use the standard signed formulation:

- an integer nowhere-zero \(k\)-flow is \(f\in\mathbb Z^{E(G)}\) with
  \[
  \partial f=0,\qquad 1\le |f(e)|\le k-1;
  \]
- a nowhere-zero \(\mathbb Z_k\)-flow is \(\bar f\in\mathbb Z_k^{E(G)}\) with
  \[
  \partial \bar f=0,\qquad \bar f(e)\ne0;
  \]
- two flows are adjacent if their difference is a nonzero flow supported on the edge set of one cycle.

The following is proved below.

**Theorem A.** Let \(G\) be any graph.

1. If \(2\le k\le5\) and \(\mathcal F(G,\mathbb Z_k)\) is connected, then \(\mathcal F(G,k)\) is connected.
2. More generally, for arbitrary \(k\), the conclusion holds if \(\mathcal F(G,\mathbb Z_k)\) has a connected spanning subgraph in which every cycle move has increment
   \[
   \pm1\quad\text{or}\quad\pm2\pmod k.
   \]
3. Consequently, the conclusion holds for every \(k\) when every cycle of \(G\) has length at most three.

Thus, in particular, the stated conjecture is settled affirmatively for \(k=4\), and in fact also for \(k=5\).

I also give an exact feasible-circulation criterion for when an individual modular reconfiguration edge lifts to an integer reconfiguration edge. An explicit \(k=6\) example shows that not every modular edge lifts, so direct edge-by-edge path lifting cannot prove the full conjecture.

# 2. Integral lifts and connected fibers

Let \(\partial\) be the oriented incidence operator, with
\[
(\partial x)(v)=\sum_{e\in\delta^+(v)}x(e)-\sum_{e\in\delta^-(v)}x(e).
\]

## Lemma 2.1: every modular flow has an integer lift

**Lemma.** Every nowhere-zero \(\mathbb Z_k\)-flow has an integer nowhere-zero \(k\)-flow lifting it.

**Proof.**
Let \(\bar f\) be a nowhere-zero \(\mathbb Z_k\)-flow, and let
\[
p(e)\in\{1,\dots,k-1\}
\]
be the standard integer representative of \(\bar f(e)\). Since \(\partial\bar f=0\),
\[
h:=\frac1k\partial p
\]
is an integral vector.

Consider
\[
P=\{q\in[0,1]^{E(G)}:\partial q=h\}.
\]
It is nonempty because \(p/k\in P\). The incidence matrix is totally unimodular, so \(P\) has an integral point \(q\in\{0,1\}^{E(G)}\). Then
\[
f:=p-kq
\]
satisfies
\[
\partial f=\partial p-k\partial q=0.
\]
Moreover, each coordinate of \(f\) is either \(p(e)\) or \(p(e)-k\), hence lies in
\[
\{1,\dots,k-1\}\cup\{-(k-1),\dots,-1\}.
\]
Thus \(f\) is an integer nowhere-zero \(k\)-flow lifting \(\bar f\). \(\square\)

## Lemma 2.2: each reduction fiber is connected

Let
\[
\pi:\mathcal F(G,k)\longrightarrow \mathcal F(G,\mathbb Z_k)
\]
be reduction modulo \(k\).

**Lemma.** For every modular flow \(\bar f\), the subgraph induced by \(\pi^{-1}(\bar f)\) is connected.

**Proof.**
Using the notation above, every lift has the form
\[
f=p-kq,\qquad q\in\{0,1\}^{E(G)},\quad \partial q=h.
\]
Let
\[
f=p-kq,\qquad f'=p-kq'
\]
be two lifts. Then
\[
z:=q'-q
\]
is an integral circulation whose coordinates lie in \(\{-1,0,1\}\).

Orient every edge in \(\operatorname{supp}(z)\) according to the sign of \(z(e)\). The resulting directed subgraph is Eulerian and hence decomposes into directed cycles
\[
z=\chi_{C_1}+\cdots+\chi_{C_r},
\]
conformally: no edge is used against the sign of \(z\). Starting from \(q\), add these cycle vectors one at a time. Every intermediate vector remains \(0\)-\(1\), has boundary \(h\), and therefore corresponds to an integer \(k\)-flow.

On the flow side, each step changes the flow by
\[
-k\chi_{C_i},
\]
which is supported on a cycle. Hence it is an allowed reconfiguration move. \(\square\)

It is useful to define a graph \(\Lambda(G,k)\) on the vertex set of \(\mathcal F(G,\mathbb Z_k)\): two distinct modular flows are adjacent in \(\Lambda(G,k)\) if some integer lift of one is adjacent to some integer lift of the other.

The preceding lemma immediately gives:

**Corollary 2.3.**
\[
\mathcal F(G,k)\text{ is connected}\quad\Longleftrightarrow\quad \Lambda(G,k)\text{ is connected}.
\]

Thus the conjecture asks whether connectivity of the full modular reconfiguration graph forces connectivity after deleting all modular edges that do not lift.

# 3. Exact criterion for lifting one modular cycle move

Suppose \(\bar f,\bar g\) are adjacent modular flows. Orient their witnessing cycle \(C\) cyclically. Their difference is then
\[
\bar g-\bar f=a\chi_C
\]
for some \(a\in\{1,\dots,k-1\}\).

Reorient the reference orientation on \(C\), if necessary, so all edges of \(C\) point cyclically. Let \(p(e)\in\{1,\dots,k-1\}\) represent \(\bar f(e)\), and put
\[
h=\frac1k\partial p.
\]
Since \(\bar g\) is nowhere-zero,
\[
p(e)+a\ne k\qquad(e\in C).
\]
Partition \(C\) into
\[
H=\{e\in C:p(e)+a>k\},\qquad
L=\{e\in C:p(e)+a<k\}.
\]

Consider the following two constrained circulation systems:
\[
\tag{A}
\partial q=h,\qquad q\in\{0,1\}^{E(G)},\qquad q(e)=1\quad(e\in H),
\]
and
\[
\tag{B}
\partial q=h,\qquad q\in\{0,1\}^{E(G)},\qquad q(e)=0\quad(e\in L).
\]

**Proposition 3.1.** The modular edge \(\bar f\bar g\) belongs to \(\Lambda(G,k)\) if and only if at least one of (A) and (B) is feasible.

**Proof.**

If (A) has a solution, let \(f=p-kq\). Then
\[
f'=f+a\chi_C
\]
is an integer \(k\)-flow. Indeed:

- for \(e\in H\), necessarily \(q(e)=1\), and
  \[
  f'(e)=p(e)-k+a=p(e)+a-k\in\{1,\dots,a-1\};
  \]
- for \(e\in L\), either
  \[
  p(e)\mapsto p(e)+a
  \]
  or
  \[
  p(e)-k\mapsto p(e)+a-k,
  \]
  and both values remain nonzero and have absolute value at most \(k-1\).

Thus \(f,f'\) are adjacent lifts.

Similarly, if (B) has a solution, then
\[
f'=f+(a-k)\chi_C
\]
is a valid adjacent lift. The condition \(q(e)=0\) on \(L\) is exactly what prevents values there from falling below \(-(k-1)\).

Conversely, suppose adjacent integer lifts differ by \(t\chi_C\). Then
\[
t\equiv a\pmod k,\qquad |t|\le2(k-1).
\]
The relevant possibilities are \(a\), \(a-k\), and possibly \(a+k\) or \(a-2k\).

- If \(t=a\), boundedness forces \(q(e)=1\) on \(H\), giving (A).
- If \(t=a-k\), boundedness forces \(q(e)=0\) on \(L\), giving (B).
- If \(t=a+k\), then necessarily \(H=\varnothing\); in that case (A) is just the unconstrained lifting system and is feasible.
- If \(t=a-2k\), then necessarily \(L=\varnothing\); in that case (B) is feasible.

Thus (A) or (B) is necessary. \(\square\)

These conditions are polynomial-time checkable. Indeed, by the bounded-circulation criterion, (A) is feasible exactly when
\[
\tag{3.1}
h(X)\ge |H\cap\delta^+(X)|-|\delta^-(X)|
\qquad\text{for every }X\subseteq V(G),
\]
while (B) is feasible exactly when
\[
\tag{3.2}
h(X)\le |\delta^+(X)\setminus L|
\qquad\text{for every }X\subseteq V(G).
\]
The complementary inequalities follow by replacing \(X\) with \(V(G)\setminus X\). Integrality follows from total unimodularity.

# 4. Moves of size \(\pm1\) and \(\pm2\) always lift

**Lemma 4.1.** If
\[
a\in\{1,2,k-2,k-1\},
\]
then every modular cycle move with increment \(a\) belongs to \(\Lambda(G,k)\).

**Proof.**

### Case \(a=1\)

Since the target is nowhere-zero, no edge of \(C\) has \(p(e)=k-1\). Hence \(H=\varnothing\), and (A) is the unconstrained lifting system, which is feasible by Lemma 2.1.

### Case \(a=2\)

Now \(p(e)=k-2\) is excluded on \(C\), and therefore
\[
H=\{e\in C:p(e)=k-1\}.
\]
We verify (3.1).

For \(X\subseteq V(G)\),
\[
\begin{aligned}
&k\Big(h(X)-|H\cap\delta^+(X)|+|\delta^-(X)|\Big)\\
&\quad =
\sum_{e\in\delta^+(X)\setminus H}p(e)
+\sum_{e\in\delta^+(X)\cap H}(p(e)-k)
+\sum_{e\in\delta^-(X)}(k-p(e)).
\end{aligned}
\]
Every negative term comes from \(H\cap\delta^+(X)\), and each such term equals \(-1\). Every edge of \(C\) entering \(X\) contributes at least \(1\) to the last sum. Since \(C\) is cyclically oriented,
\[
|C\cap\delta^+(X)|=|C\cap\delta^-(X)|.
\]
In particular,
\[
|C\cap\delta^-(X)|\ge |H\cap\delta^+(X)|.
\]
Thus the displayed expression is nonnegative, proving (3.1). Hence (A) is feasible.

### Case \(a=k-1\)

The target being nowhere-zero excludes \(p(e)=1\), so \(L=\varnothing\). Thus (B) is the unconstrained lifting system.

### Case \(a=k-2\)

Here \(p(e)=2\) is excluded and
\[
L=\{e\in C:p(e)=1\}.
\]
For every \(X\subseteq V(G)\),
\[
\begin{aligned}
&k\Big(|\delta^+(X)\setminus L|-h(X)\Big)\\
&\quad =
\sum_{e\in\delta^+(X)\setminus L}(k-p(e))
-\sum_{e\in\delta^+(X)\cap L}p(e)
+\sum_{e\in\delta^-(X)}p(e).
\end{aligned}
\]
Each negative term equals \(-1\), and each edge of \(C\) entering \(X\) contributes at least \(1\) to the final sum. Again the numbers of edges of \(C\) entering and leaving \(X\) are equal, so the expression is nonnegative. This is (3.2), proving feasibility of (B). \(\square\)

Therefore the subgraph of \(\mathcal F(G,\mathbb Z_k)\) consisting of moves by \(\pm1,\pm2\) is contained in \(\Lambda(G,k)\).

## Proof of Theorem A for \(k\le5\)

For \(2\le k\le5\), every nonzero element of \(\mathbb Z_k\) belongs to
\[
\{1,2,k-2,k-1\}.
\]
Hence every modular reconfiguration edge lifts. Thus
\[
\Lambda(G,k)=\mathcal F(G,\mathbb Z_k).
\]
If the latter is connected, so is \(\Lambda(G,k)\), and Corollary 2.3 gives connectivity of \(\mathcal F(G,k)\). \(\square\)

# 5. A graph class valid for all \(k\)

For a fixed modular flow \(\bar f\) and cyclically oriented cycle \(C\), consider all shifts
\[
\bar f+s\chi_C,\qquad s\in\mathbb Z_k.
\]
Such a shift is nowhere-zero precisely when
\[
s\notin F_C:=\{-\bar f(e):e\in C\}.
\]
Thus the admissible shifts form \(\mathbb Z_k\setminus F_C\).

Let \(Q_k\) be the Cayley graph on \(\mathbb Z_k\) with steps \(\pm1,\pm2\). If at most three vertices are deleted from \(Q_k\), the remaining graph is connected. For \(k\le5\) this is immediate. For \(k\ge6\), a disconnection around the cyclic order would require at least two separating gaps, each containing at least two consecutive deleted vertices; hence at least four deleted vertices.

Consequently, if \(|C|\le3\), then \(|F_C|\le3\), and any modular move on \(C\) can be replaced by a sequence of nowhere-zero modular moves on the same cycle, each having increment \(\pm1\) or \(\pm2\). Lemma 4.1 lifts all those moves.

This proves:

**Corollary 5.1.** For every \(k\), if every cycle of \(G\) has length at most three and \(\mathcal F(G,\mathbb Z_k)\) is connected, then \(\mathcal F(G,k)\) is connected.

# 6. Why direct edge lifting fails from \(k=6\) onward

The following explicit example shows that Proposition 3.1 can fail for both systems (A) and (B).

Let \(k=6\). Take vertices
\[
u_i,b_i,v_i,c_i\qquad (i=1,\dots,6),
\]
with indices cyclically interpreted. Let the main directed cycle be
\[
u_i\longrightarrow b_i\longrightarrow v_i\longrightarrow c_i\longrightarrow u_{i+1},
\]
with modular values respectively
\[
4,\quad5,\quad2,\quad1.
\]
Add:

- an arc \(u_i\to v_i\) of value \(3\), for every \(i\);
- arcs \(b_6\to b_i\) of value \(1\), for \(1\le i\le5\);
- arcs \(c_i\to c_6\) of value \(1\), for \(1\le i\le5\).

Call this assignment \(\bar f\). Its boundary is divisible by \(6\):

- at each \(u_i\), the integer boundary is \(4+3-1=6\);
- at each \(v_i\), it is \(2-5-3=-6\);
- at \(b_i\), \(i\le5\), it is \(5-4-1=0\), while at \(b_6\) it is \(6\);
- at \(c_i\), \(i\le5\), it is \(1+1-2=0\), while at \(c_6\) it is \(-6\).

Thus \(\bar f\) is a nowhere-zero \(\mathbb Z_6\)-flow.

Let \(C\) be the main \(24\)-cycle and put
\[
\bar g=\bar f+3\chi_C.
\]
On \(C\), the values become
\[
1,\quad2,\quad5,\quad4,
\]
so \(\bar g\) is also nowhere-zero and \(\bar f,\bar g\) are adjacent.

For this move, \(a=3\), and
\[
H=\{e\in C:p(e)\in\{4,5\}\},\qquad
L=\{e\in C:p(e)\in\{1,2\}\}.
\]

Let
\[
X=V(G)\setminus\{b_1,\dots,b_6\}.
\]
The six arcs \(u_i\to b_i\), of value \(4\), leave \(X\), while the six arcs \(b_i\to v_i\), of value \(5\), enter \(X\). No added arc crosses this cut. Hence
\[
h(X)=\frac{6\cdot4-6\cdot5}{6}=-1.
\]
But
\[
|H\cap\delta^+(X)|-|\delta^-(X)|=6-6=0.
\]
Thus (3.1) fails, so system (A) is infeasible.

Likewise, let
\[
Y=V(G)\setminus\{c_1,\dots,c_6\}.
\]
The six arcs \(v_i\to c_i\), of value \(2\), leave \(Y\), and the six arcs \(c_i\to u_{i+1}\), of value \(1\), enter \(Y\). Hence
\[
h(Y)=\frac{6\cdot2-6\cdot1}{6}=1.
\]
Every arc leaving \(Y\) belongs to \(L\), so
\[
|\delta^+(Y)\setminus L|=0.
\]
Thus (3.2) fails, and system (B) is infeasible.

By Proposition 3.1, this modular reconfiguration edge has no integer reconfiguration edge above it.

This does **not** disprove the conjecture: an integer path might project to a modular detour through other flows. I have not proved that either reconfiguration graph of this example is globally connected or disconnected.

# 7. Remaining gap

The general conjecture is now reduced to the following precise statement:

> If \(\mathcal F(G,\mathbb Z_k)\) is connected, must its spanning subgraph \(\Lambda(G,k)\), consisting of the modular edges satisfying one of the two constrained circulation systems (A) and (B), also be connected?

For \(k\le5\), every edge belongs to \(\Lambda(G,k)\). Starting at \(k=6\), the explicit construction above shows that individual edges can be absent. Therefore a full proof must show that every non-liftable modular edge can be bypassed globally, or a counterexample must make such an edge essential to modular connectivity. Neither is established here.