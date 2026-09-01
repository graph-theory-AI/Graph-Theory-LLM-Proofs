```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The full conjecture remains open, but it reduces exactly to trees, isolated components preserve polynomial chi-boundedness quantitatively, and a substitution construction forces every P6-free polynomial bound to have exponent at least log_2(16/5).",
  "would_publish": false,
  "caveats": "No polynomial upper bound for P6-free graphs is obtained, and the reported 2025 P5 result is used only conditionally."
}
```

## 1. Statement and status

All graphs below are finite and simple, and “\(H\)-free” means having no induced copy of \(H\).

> **Polynomial Gyárfás–Sumner conjecture.**  
> For every forest \(H\), there are constants \(C_H,d_H\) such that every \(H\)-free graph \(G\) satisfies
> \[
> \chi(G)\le C_H\omega(G)^{d_H}.
> \]

I do not prove or disprove this conjecture. I give:

1. an exact reduction from forests to trees;
2. a quantitative closure theorem for adding isolated vertices;
3. a self-contained polynomial bound for stars and stars plus isolated vertices;
4. the standard exponential component/path recurrences, with the precise point where polynomiality is lost;
5. an explicit sequence of \(P_6\)-free graphs showing that any \(P_6\)-free polynomial bound must have exponent at least
   \[
   \log_2(16/5)=1.678071\ldots.
   \]

The last construction in particular rules out any linear \(\chi\)-bound for \(P_6\)-free graphs.

---

## 2. The universal forest conjecture is exactly the tree conjecture

We first record the relevant monotonicity.

### Lemma 2.1
If \(H\) is an induced subgraph of \(J\), and \(J\) is good, then \(H\) is good, with the same polynomial bound.

#### Proof
Every induced copy of \(J\) contains an induced copy of \(H\). Hence every \(H\)-free graph is \(J\)-free. ∎

### Proposition 2.2
The following assertions are equivalent:

1. every forest is good;
2. every tree is good.

Moreover, if a forest \(H\) is not good, then there is a tree \(T\) on at most \(|V(H)|+1\) vertices that is not good.

#### Proof
Only \(2\Rightarrow1\) needs proof. Let \(H\) have components \(H_1,\dots,H_c\). If \(c=1\), it is already a tree. Otherwise choose \(u_i\in V(H_i)\), add one new vertex \(x\), and add the edges
\[
xu_1,\dots,xu_c.
\]
The resulting graph \(T\) is connected and has
\[
\sum_i(|V(H_i)|-1)+c=|V(H)|=|V(T)|-1
\]
edges, so \(T\) is a tree. Deleting \(x\) from \(T\) leaves \(H\) as an induced subgraph. Thus goodness of \(T\) implies goodness of \(H\) by Lemma 2.1.

The final assertion is the contrapositive. ∎

Thus the universal conjecture for forests is not genuinely stronger than its restriction to connected forests. This does not resolve the local question “if each component of a particular forest is good, must their disjoint union be good?”: the connected tree constructed above need not belong to any presently known good family.

---

## 3. Adding isolated vertices preserves polynomial \(\chi\)-boundedness

This operation admits a clean additive recurrence, unlike adding a nontrivial component.

### Theorem 3.1
Let \(F\) be any fixed graph. Suppose every \(F\)-free graph \(G\) satisfies
\[
\chi(G)\le p(\omega(G)),
\]
where \(p\) is nondecreasing and \(p(w)\ge1\) for \(w\ge1\).

For \(k\ge0\), put
\[
H_k=F\sqcup kK_1.
\]
Define \(p_0=p\), \(p_k(0)=0\), and, for \(w\ge1\),
\[
p_k(w)=p_k(w-1)+p_{k-1}(w).
\]
Then every \(H_k\)-free graph \(G\) satisfies
\[
\chi(G)\le p_k(\omega(G)).
\]

In particular, if \(p(w)\le Cw^d\), then
\[
\chi(G)\le C\omega(G)^{d+k}
\]
for every \(H_k\)-free graph \(G\), after harmless adjustment of \(C\).

#### Proof
Induct first on \(k\), and for fixed \(k\) on \(w=\omega(G)\). The case \(k=0\) is the hypothesis.

Let \(k\ge1\), \(w\ge1\), and choose \(v\in V(G)\). Set
\[
A=V(G)\setminus N[v],\qquad B=N(v).
\]
If \(G[A]\) contained \(H_{k-1}\), then adding the vertex \(v\), which is anticomplete to \(A\), would produce an induced copy of \(H_k\). Thus \(G[A]\) is \(H_{k-1}\)-free, and hence
\[
\chi(G[A]\cup\{v\})=\max\{\chi(G[A]),1\}\le p_{k-1}(w).
\]

The graph \(G[B]\) remains \(H_k\)-free, and
\[
\omega(G[B])\le w-1,
\]
since every clique in \(B\), together with \(v\), is a larger clique in \(G\). Therefore the induction on \(w\) gives
\[
\chi(G[B])\le p_k(w-1).
\]
Using disjoint palettes for \(A\cup\{v\}\) and \(B\),
\[
\chi(G)\le p_{k-1}(w)+p_k(w-1)=p_k(w).
\]

Finally,
\[
p_k(w)=\sum_{i=1}^w p_{k-1}(i).
\]
If inductively \(p_{k-1}(i)\le Ci^{d+k-1}\), then
\[
p_k(w)\le \sum_{i=1}^w Ci^{d+k-1}\le Cw^{d+k}.
\]
∎

Consequently, a minimum-order counterexample forest, if one exists, has no isolated component.

### Corollary 3.2: stars plus isolates

Let \(S_t=K_{1,t}\), where \(t\ge2\). Every \(S_t\)-free graph \(G\), with \(w=\omega(G)\), satisfies
\[
\chi(G)\le \binom{w+t-2}{t-1}.
\]
Consequently,
\[
S_t\sqcup kK_1
\]
is good for every fixed \(t,k\), with a bound of order
\[
O_{t,k}\bigl(\omega^{t-1+k}\bigr).
\]

#### Proof
For every \(v\in V(G)\), the graph \(G[N(v)]\) has no stable set of size \(t\), since such a stable set together with \(v\) would induce \(S_t\). It also has no clique of size \(w\), since that clique together with \(v\) would have size \(w+1\). The elementary Ramsey bound gives
\[
|N(v)|<R(w,t)\le \binom{w+t-2}{t-1}.
\]
Thus
\[
\Delta(G)+1\le \binom{w+t-2}{t-1},
\]
and greedy coloring gives the stated bound. Apply Theorem 3.1 for the isolated vertices. ∎

---

## 4. Why the straightforward component induction is exponential

The standard decomposition does prove ordinary \(\chi\)-boundedness under disjoint union, but it loses polynomiality.

### Proposition 4.1
Suppose \(F\)-free graphs are \(\chi\)-bounded by \(p_F\), and \(J\)-free graphs by \(p_J\). Let
\[
H=F\sqcup J,\qquad r=|V(F)|.
\]
Then \(H\)-free graphs are \(\chi\)-bounded by a function satisfying
\[
q(w)\le
\max\left\{
p_F(w),\,
p_J(w)+r+r q(w-1)
\right\}.
\]

#### Proof
Let \(G\) be \(H\)-free with clique number \(w\). If \(G\) is \(F\)-free, use \(p_F(w)\). Otherwise fix an induced copy \(X\cong F\).

Let \(A\) be the set of vertices outside \(X\) anticomplete to \(X\). Then \(G[A]\) is \(J\)-free, since a copy of \(J\) in \(A\), together with \(X\), would induce \(F\sqcup J\).

Every remaining vertex outside \(X\) has a neighbor in \(X\). Assign each such vertex to one chosen neighbor \(x\in X\), obtaining \(r\) parts \(R_x\subseteq N(x)\). Each \(G[R_x]\) is \(H\)-free and has clique number at most \(w-1\). Therefore
\[
\chi(G)\le p_J(w)+|X|+\sum_{x\in X}q(w-1),
\]
which is the claimed recurrence. ∎

If \(p_F,p_J\) are polynomial and \(r\ge2\), this recurrence gives only an exponential upper bound \(O(r^w)\). For \(r=1\), the coefficient of the recursive term is one, and discrete summation produces a polynomial; that is exactly the isolated-vertex situation of Theorem 3.1.

This recurrence is only a limitation of the proof. It is not a superpolynomial lower bound.

---

## 5. An elementary exponential bound for induced-path-free graphs

For comparison, here is a self-contained form of the classical path argument.

### Proposition 5.1
For every \(t\ge3\), every \(P_t\)-free graph \(G\) satisfies
\[
\chi(G)\le (t-1)^{\omega(G)-1}.
\]

#### Proof
Induct on \(w=\omega(G)\). The case \(w=1\) is immediate. Let
\[
a=(t-1)^{w-2},
\]
and suppose, for a contradiction, that a connected \(P_t\)-free graph \(G\) has
\[
\chi(G)>(t-1)a.
\]

Choose \(v_1\in V(G)\). A component \(C_1\) of \(G-v_1\) satisfies
\[
\chi(C_1)=\chi(G-v_1)\ge\chi(G)-1\ge(t-1)a.
\]
Since \(G\) is connected, \(v_1\) has a neighbor in \(C_1\).

We construct an induced path \(v_1,\dots,v_i\) and a connected set \(C_i\) such that:

- \(C_i\) is anticomplete to \(v_1,\dots,v_{i-1}\);
- \(v_i\) has a neighbor in \(C_i\);
- \(\chi(C_i)\ge(t-i)a\).

For \(i\le t-2\), the graph \(G[N(v_i)\cap C_i]\) has clique number at most \(w-1\), so by induction it has chromatic number at most \(a\). Hence
\[
\chi(C_i\setminus N(v_i))
   \ge \chi(C_i)-a
   \ge (t-i-1)a.
\]
Choose a component \(C_{i+1}\) of \(C_i\setminus N(v_i)\) with maximum chromatic number. Connectivity of \(C_i\) yields a vertex
\[
v_{i+1}\in N(v_i)\cap C_i
\]
having a neighbor in \(C_{i+1}\). The invariants are preserved, and the path remains induced.

After \(t-2\) such steps, \(v_1,\dots,v_{t-1}\) is an induced path and \(v_{t-1}\) has a neighbor \(v_t\in C_{t-1}\). This gives an induced \(P_t\), a contradiction. ∎

For \(P_6\) this gives
\[
\chi(G)\le 5^{\omega(G)-1},
\]
which is \(\chi\)-boundedness but not polynomial \(\chi\)-boundedness.

---

## 6. A polynomial lower bound for the \(P_6\)-free problem

We now give an explicit construction showing that a prospective polynomial bound for \(P_6\)-free graphs cannot have degree one.

### Theorem 6.1
There is a sequence \((G_k)_{k\ge1}\) of \(P_6\)-free graphs such that
\[
|V(G_k)|=16^k,\qquad
\alpha(G_k)=5^k,\qquad
\omega(G_k)=2^k.
\]
Consequently,
\[
\chi(G_k)\ge \left(\frac{16}{5}\right)^k
 =\omega(G_k)^{\log_2(16/5)}.
\]
Thus any bound of the form
\[
\chi(G)\le C\omega(G)^d
\]
valid for all \(P_6\)-free graphs must satisfy
\[
d\ge\log_2(16/5)=1.678071\ldots.
\]

The same conclusion holds for every forbidden forest \(H\) containing an induced \(P_6\).

### Proof

#### Step 1: a 16-vertex \(P_6\)-free graph

Let \(C\) have as vertices the even-cardinality subsets of \([5]\), with
\[
A\sim B\quad\Longleftrightarrow\quad |A\triangle B|=4.
\]
This is the usual Clebsch graph.

It is triangle-free: if \(A\sim B\sim D\), then both \(A\triangle B\) and \(B\triangle D\) are 4-subsets of a 5-set. If they are distinct, their symmetric difference has size \(2\); if equal, then \(A=D\). In neither case is \(|A\triangle D|=4\). Since \(C\) has edges, \(\omega(C)=2\).

We next show \(\alpha(C)=5\). Write
\[
M_i=[5]\setminus\{i\}.
\]
The five vertices \(M_1,\dots,M_5\) are pairwise nonadjacent, so \(\alpha(C)\ge5\).

For the reverse inequality, note:

- two 2-subsets are adjacent exactly when they are disjoint;
- \(M_i\) is adjacent to a 2-subset \(A\) exactly when \(i\in A\);
- all \(M_i\) are adjacent to \(\varnothing\).

If an independent set contains \(\varnothing\), it contains no \(M_i\), and its 2-subsets are pairwise intersecting. A pairwise intersecting family of 2-subsets of \([5]\) has size at most \(4\), giving total size at most \(5\).

If it does not contain \(\varnothing\), let
\[
R=\{i:M_i\text{ is in the independent set}\},\qquad r=|R|.
\]
Every included 2-subset lies in \([5]\setminus R\), and the included 2-subsets are pairwise intersecting. The maximum possible totals for \(r=0,\dots,5\) are respectively
\[
4,\ 4,\ 5,\ 4,\ 4,\ 5.
\]
Thus again the total is at most \(5\), proving \(\alpha(C)=5\).

It remains to prove that \(C\) is \(P_6\)-free. Suppose
\[
A_1-A_2-A_3-A_4-A_5-A_6
\]
were an induced \(P_6\). Symmetric difference with \(A_1\) is an automorphism, so assume \(A_1=\varnothing\). Permuting the coordinates, we may assume
\[
A_2=M_5=\{1,2,3,4\}.
\]
The neighbors of \(M_5\), other than \(\varnothing\), are the pairs \(\{i,5\}\); hence assume
\[
A_3=\{1,5\}.
\]
The neighbors of \(\{1,5\}\) that are nonadjacent to \(\varnothing\) and \(M_5\) are
\[
\{2,3\},\ \{2,4\},\ \{3,4\}.
\]
By symmetry,
\[
A_4=\{2,3\}.
\]
A neighbor of \(\{2,3\}\) nonadjacent to \(\varnothing\) is one of
\[
\{1,4\},\ \{1,5\},\ \{4,5\}.
\]
Nonadjacency to \(M_5\) excludes the pairs containing \(5\), so
\[
A_5=\{1,4\}.
\]
Finally, a neighbor of \(\{1,4\}\) nonadjacent to \(\varnothing\) is one of
\[
\{2,3\},\ \{2,5\},\ \{3,5\}.
\]
The first repeats \(A_4\), while the other two are adjacent to \(M_5=A_2\), creating a chord. This is impossible. Therefore \(C\) is \(P_6\)-free.

#### Step 2: substitution preserves \(P_6\)-freeness

For graphs \(A,B\), let \(A[B]\) denote their lexicographic product: every vertex of \(A\) is replaced by a copy of \(B\), and two copies are completely joined exactly when their corresponding vertices are adjacent in \(A\).

The path \(P_n\), for \(n\ge4\), has no nontrivial homogeneous set. Indeed, if \(S\) were such a set, connectedness gives a vertex outside \(S\) adjacent to all of \(S\). Since vertices of a path have degree at most two, \(|S|=2\); the two vertices are the two neighbors of a common path vertex. As \(n\ge4\), another path vertex distinguishes them, a contradiction.

Consequently, if both \(A\) and \(B\) are \(P_6\)-free, then \(A[B]\) is \(P_6\)-free. An induced \(P_6\) meeting a substitution module in at least two but fewer than six vertices would give a nontrivial homogeneous set in the \(P_6\). Thus it either lies inside one module, giving a \(P_6\) in \(B\), or uses at most one vertex from each module, giving a \(P_6\) in \(A\).

Define
\[
G_1=C,\qquad G_{k+1}=C[G_k].
\]
Inductively, every \(G_k\) is \(P_6\)-free.

#### Step 3: parameters

For lexicographic products,
\[
\omega(A[B])=\omega(A)\omega(B),\qquad
\alpha(A[B])=\alpha(A)\alpha(B).
\]
Therefore
\[
|V(G_k)|=16^k,\qquad
\omega(G_k)=2^k,\qquad
\alpha(G_k)=5^k.
\]
Every color class has at most \(5^k\) vertices, so
\[
\chi(G_k)\ge \frac{16^k}{5^k}=\left(\frac{16}{5}\right)^k.
\]
Since \(\omega(G_k)=2^k\), this is
\[
\chi(G_k)\ge\omega(G_k)^{\log_2(16/5)}.
\]

If \(H\) contains an induced \(P_6\), then every \(P_6\)-free graph is \(H\)-free, so the same lower bound applies to the class of \(H\)-free graphs. ∎

### Amplification consequence

More generally, let \(B\) be any \(P_6\)-free graph with \(\omega(B)\ge2\). Its iterated lexicographic powers are \(P_6\)-free and satisfy
\[
\frac{|V(B^{[k]})|}{\alpha(B^{[k]})}
 =\left(\frac{|V(B)|}{\alpha(B)}\right)^k,
 \qquad
\omega(B^{[k]})=\omega(B)^k.
\]
Therefore a polynomial bound \(C\omega^d\) would force the constant-free necessary inequality
\[
\frac{|V(B)|}{\alpha(B)}\le \omega(B)^d
\]
for every finite \(P_6\)-free graph \(B\). The Clebsch graph gives the ratio \(16/5\) at clique number \(2\).

This provides a finite computational route to stronger lower bounds: search \(P_6\)-free graphs \(B\) maximizing
\[
\frac{\log(|V(B)|/\alpha(B))}{\log\omega(B)}.
\]
No such computation is claimed here.

---

## 7. Consequence of the reported \(P_5\) result

The supplied catalog reports that arXiv:2512.24907 proves that \(P_5\) is good. I have not independently checked that manuscript, so the following is conditional on the reported theorem.

The 2023 source paper proves that
\[
F\text{ good}\quad\Longrightarrow\quad F\sqcup P_4\text{ good}.
\]
Hence, if \(P_5\) is good, then
\[
P_5\sqcup rP_4\sqcup kK_1
\]
is good for all fixed \(r,k\). By Lemma 2.1, every linear forest with at most one component isomorphic to \(P_5\) and all other components of order at most four is then good.

This still does not cover \(P_6\), \(2P_5\), or general forests.

---

## 8. Remaining gaps

1. The principal missing case exposed here is a polynomial upper bound for \(P_6\)-free graphs. The elementary upper bound above is exponential in \(\omega\).
2. The Clebsch substitution family is not a counterexample: its chromatic number grows only as a fixed power of its clique number.
3. The naive component recurrence has several recursive branches of clique number \(w-1\); this creates an exponential recurrence. A proof of the conjecture needs additional structure that combines these branches rather than coloring them with separate palettes.
4. Although the universal forest conjecture is equivalent to the tree version, knowing that the individual components of one forest are good still does not imply, by the arguments here, that their disjoint union is good.