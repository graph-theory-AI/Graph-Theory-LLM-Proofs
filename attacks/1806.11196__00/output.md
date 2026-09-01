```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I do not settle the polynomial-time conjecture, but I prove a deterministic n^{O_t(sqrt(n))}-time algorithm for List-3-Coloring on P_t-free graphs.",
  "would_publish": false,
  "caveats": "The cases t >= 8 remain unresolved in polynomial time, and I have not checked whether this elementary subexponential bound is already in the literature."
}
```

## 1. Statement and scope

Let \(P_t\) denote the path on \(t\) vertices. The question asks whether, for every fixed \(t\), 3-Coloring is polynomial-time solvable on \(P_t\)-free graphs.

I do not prove or disprove this. In particular, the argument below does not give a polynomial-time algorithm for \(t=8\). It does give the following unconditional complexity bound, in the stronger list setting.

### Theorem

For every fixed \(t\ge 3\), List-3-Coloring on \(n\)-vertex \(P_t\)-free graphs can be solved deterministically in

\[
n^{O_t(\sqrt n)}
   =2^{O_t(\sqrt n\log n)}
   =2^{o(n)}
\]

time and polynomial space.

More generally, for every integer \(D\ge 8\), the running time is

\[
n^{O(n/D+tD)}.
\]

Thus the first open case \(t=8\) admits an \(n^{O(\sqrt n)}\)-time algorithm, also for arbitrary lists contained in \(\{1,2,3\}\).

The proof has two ingredients: bounded-size balanced separators in bounded-degree \(P_t\)-free graphs, and a list-color branching argument in which all but at most one branch at a high-degree vertex make substantial progress.

---

## 2. A balanced closed-neighborhood separator

For a vertex set \(X\), write \(N[X]\) for its closed neighborhood.

### Lemma 2.1

Let \(H\) be a connected \(P_t\)-free graph on \(m\) vertices. There is an induced path \(Q\) on at most \(t-1\) vertices such that every component of

\[
H-N_H[V(Q)]
\]

has at most \(m/2\) vertices.

Consequently, if \(\Delta(H)<D\), then \(H\) has a balanced separator of size at most

\[
(t-1)D.
\]

#### Proof

Choose a vertex \(v_1\), and put \(Q_i=v_1\cdots v_i\). Suppose inductively that \(Q_i\) is induced.

If every component of \(H-N[Q_i]\) has at most \(m/2\) vertices, stop. Otherwise, there is a unique component \(C_i\) with more than \(m/2\) vertices.

For \(i=1\), connectedness of \(H\) implies that some vertex \(v_2\in N(v_1)\) has a neighbor in \(C_1\).

For \(i\ge 2\), the component \(C_i\) is contained in \(C_{i-1}\): indeed, \(H-N[Q_i]\) is an induced subgraph of \(H-N[Q_{i-1}]\), and a component containing more than \(m/2\) vertices must lie in the unique previous component of that size.

By construction, \(v_i\) has a neighbor in \(C_{i-1}\). Since \(C_{i-1}\) is connected and \(C_i\) is a component of \(C_{i-1}-N[v_i]\), there is a vertex

\[
v_{i+1}\in C_{i-1}\cap N(v_i)
\]

having a neighbor in \(C_i\). Moreover,

\[
C_{i-1}\subseteq H-N[Q_{i-1}],
\]

so \(v_{i+1}\) has no neighbor among \(v_1,\ldots,v_{i-1}\). Hence \(Q_{i+1}\) is again an induced path.

If this process did not stop by \(i=t-1\), it would construct an induced path \(v_1\cdots v_t\), contrary to \(P_t\)-freeness. Therefore it stops with \(|Q|\le t-1\).

If \(\Delta(H)<D\), then every closed neighborhood has size at most \(D\), and therefore

\[
|N[Q]|
 \le \sum_{v\in Q}|N[v]|
 \le (t-1)D.
\]

The construction is algorithmic: each step only requires computing components and scanning their boundary. ∎

---

## 3. Solving the bounded-degree residual instances

### Lemma 3.1

For fixed \(t\) and \(D\), List-3-Coloring on \(P_t\)-free graphs of maximum degree less than \(D\) can be solved in

\[
n^{O(tD)}
\]

time and polynomial space.

#### Proof

It suffices to handle a connected instance \(H\) on \(m\) vertices; disconnected components can be solved independently.

Apply Lemma 2.1 and let

\[
S=N_H[V(Q)],\qquad |S|\le s_0:=(t-1)D.
\]

Enumerate every assignment of colors to \(S\) that respects the lists and is proper on \(H[S]\). There are at most \(3^{s_0}\) assignments.

For each such assignment:

1. delete from every outside list the colors used by its neighbors in \(S\);
2. reject the assignment if some list becomes empty;
3. repeatedly propagate singleton lists;
4. solve the resulting components independently.

Every remaining component is contained in a component of \(H-S\), and hence has at most \(m/2\) vertices. Deleting vertices does not increase maximum degree and preserves \(P_t\)-freeness.

For completeness, let \(F(m)\) denote the worst running time. Apart from polynomial overhead,

\[
F(m)
 \le 3^{s_0}\max
 \left\{
   \sum_i F(m_i):
   m_i\le m/2,\ \sum_i m_i\le m
 \right\}.
\]

For every \(p\ge1\),

\[
\sum_i m_i^p
 \le \left(\frac m2\right)^{p-1}\sum_i m_i
 \le \frac{m^p}{2^{p-1}}.
\]

Choosing

\[
p\ge s_0\log_2 3+O(1)
\]

makes \(3^{s_0}2^{1-p}<1\), and a standard induction gives

\[
F(m)\le m^{O(s_0)}=m^{O(tD)}.
\]

Correctness follows because every coloring restricts to one enumerated coloring of \(S\), while for a fixed coloring of \(S\), the components of \(H-S\) are independent. The recursion can be traversed depth first, using polynomial space. ∎

Equivalently, the separator proof gives a tree decomposition of width \(O(tD\log n)\), leading to the same bound by dynamic programming.

---

## 4. Branching on high-degree vertices

We now consider a list instance \((H,L)\), where \(L(v)\subseteq\{1,2,3\}\).

Repeatedly apply the forced-color rule:

- if \(L(v)=\varnothing\), reject;
- if \(L(v)=\{c\}\), assign \(v\) color \(c\), remove \(v\), and delete \(c\) from the lists of all its neighbors.

After this propagation, every remaining list has size two or three. The residual graph is always an induced subgraph of the original graph and is therefore still \(P_t\)-free.

Define the potential

\[
\Phi(H,L)=\sum_{u\in V(H)}(|L(u)|-1).
\]

Thus a two-element list contributes \(1\), a three-element list contributes \(2\), and initially \(\Phi\le 2n\).

Let \(v\) have degree \(d\). For each \(c\in L(v)\), put

\[
f_c=\bigl|\{u\in N(v):c\in L(u)\}\bigr|.
\]

Assigning \(v\) color \(c\) removes \(v\) and deletes \(c\) from each of these \(f_c\) neighboring lists. Therefore, in every surviving branch,

\[
\Phi-\Phi_c\ge |L(v)|-1+f_c.
\tag{1}
\]

### Lemma 4.1

At a vertex \(v\) of degree \(d\), all but at most one of the color branches satisfy

\[
f_c\ge d/2.
\]

#### Proof

If \(|L(v)|=3\), then

\[
\sum_{c=1}^3 f_c
  =\sum_{u\in N(v)}|L(u)|
  \ge 2d.
\]

Order the frequencies as \(f_1\le f_2\le f_3\). Since \(f_3\le d\), the inequality \(f_2<d/2\) would imply

\[
f_1+f_2+f_3<d/2+d/2+d=2d,
\]

a contradiction. Thus the two largest frequencies are at least \(d/2\).

If \(L(v)=\{a,b\}\), every neighboring list has size at least two in a three-color universe, and hence intersects \(\{a,b\}\). Consequently,

\[
f_a+f_b\ge d,
\]

so the larger of \(f_a,f_b\) is at least \(d/2\). ∎

At every branch node, designate one least-frequent color as the **default** branch. Every other branch is called **heavy**. Lemma 4.1 and (1) show that if \(d\ge D\), every heavy branch decreases \(\Phi\) by at least \(D/2\).

Since \(\Phi\le2n\), every root-to-leaf path contains at most

\[
K:=\left\lfloor\frac{4n}{D}\right\rfloor
\]

heavy branches. There is at most one default child and at most two heavy children at every branching node. Also, every branch assigns and removes at least one vertex, so the branching depth is at most \(n\).

A root-to-leaf path is determined by its length, the at most \(K\) positions at which it uses a heavy branch, and one of at most two labels for each heavy branch. Hence the number of leaves is at most

\[
(n+1)\sum_{k=0}^{K}\binom nk2^k
   =n^{O(n/D)}.
\tag{2}
\]

This estimate remains valid if some branches immediately fail. The argument is special to three colors: after singleton propagation, any two remaining lists intersect.

---

## 5. The complete subexponential algorithm

Fix \(D\ge8\). At every recursive state:

1. perform singleton propagation;
2. if the residual maximum degree is less than \(D\), invoke the bounded-degree algorithm from Lemma 3.1;
3. otherwise choose a vertex \(v\) of degree at least \(D\), and branch over all colors in \(L(v)\).

Correctness is immediate by induction:

- singleton propagation is forced;
- every coloring chooses exactly one branch color at \(v\);
- the bounded-degree solver exhaustively considers the balanced separator colors and then solves independent components.

By (2), the high-degree branching phase has at most \(n^{O(n/D)}\) leaves. At each leaf, Lemma 3.1 takes \(n^{O(tD)}\) time. Polynomial work at internal nodes is absorbed, giving

\[
T(n,t,D)=n^{O(n/D+tD)}.
\]

Taking \(D=\lceil\sqrt n\rceil\) yields

\[
T(n,t)=n^{O_t(\sqrt n)}
      =2^{O_t(\sqrt n\log n)}.
\]

Since \(\sqrt n\log n=o(n)\), this is genuinely subexponential.

The result applies to ordinary 3-Coloring by taking \(L(v)=\{1,2,3\}\) for every vertex. If the \(P_t\)-free condition is not supplied as a promise, it can be checked in \(n^{O(t)}\) time by enumerating ordered \(t\)-tuples.

---

## 6. Consequences and remaining gap

For \(t=8\), the argument gives

\[
\text{List-3-Coloring on \(P_8\)-free graphs}
 \in n^{O(\sqrt n)}.
\]

It also gives polynomial time whenever the maximum degree is bounded by a constant, via Lemma 3.1.

This does not answer the catalog question. Within this framework the exponent is controlled by

\[
\frac nD+tD,
\]

whose minimum is of order \(\sqrt{tn}\), not a constant. A polynomial algorithm would require a substantially stronger treatment of at least one of:

1. the sequence of low-frequency/default branches at high-degree vertices; or
2. the enumeration of all colorings of the \(O(tD)\)-vertex balanced separators.

No counterexample or NP-hardness result for any fixed \(t\) is obtained. I also have not verified whether the subexponential bound above has already appeared in the literature, so I make no novelty claim.