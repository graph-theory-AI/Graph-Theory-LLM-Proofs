```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open, but it holds for tournaments admitting a homogeneous partition into at most n^{9/16+o(1)} transitive blocks.",
  "would_publish": false,
  "caveats": "The homogeneous-block hypothesis is restrictive; there is no improved exponent for arbitrary tournaments, and the literature novelty of the composition lemma was not checked."
}
```

## 1. Statement and notation

For a tournament \(T\), let
\[
f(T)=\max\{\chi(H):H\subseteq T\text{ is a directed-acyclic subgraph}\},
\]
where chromatic number is taken in the underlying undirected graph.

The conjecture asks whether every \(n\)-vertex tournament satisfies
\[
f(T)\ge n^{3/4-o(1)}.
\]

I do not prove this in general. The main partial result is the following.

### Partial theorem

Suppose that an \(n\)-vertex tournament \(T\) has a partition
\[
V(T)=V_1\sqcup\cdots\sqcup V_r
\]
such that:

1. each \(T[V_i]\) is transitive;
2. for every \(i\ne j\), all arcs between \(V_i\) and \(V_j\) have the same direction.

Thus \(T\) is a substitution of transitive tournaments into the vertices of an \(r\)-vertex quotient tournament. Then, for every fixed \(\eta>0\), there is \(c_\eta>0\) such that
\[
f(T)\ge c_\eta\,\frac{n}{r^{4/9+\eta}}. \tag{1}
\]
Consequently, if
\[
r\le n^{9/16+o(1)},
\]
then
\[
f(T)\ge n^{3/4-o(1)}.
\]

The exponent \(9/16\) comes from the established universal exponent \(5/9\) in the source paper.

---

## 2. Ordering reformulation

For a linear order \(\pi\) of \(V(T)\), define the agreement graph \(A_\pi(T)\) by
\[
uv\in E(A_\pi(T))
\quad\Longleftrightarrow\quad
\text{the tournament arc between \(u,v\) points from the earlier to the later vertex in \(\pi\)}.
\]

Then
\[
f(T)=\max_\pi \chi(A_\pi(T)). \tag{2}
\]

Indeed, all arcs represented by \(A_\pi(T)\) point forward in \(\pi\), so they form an acyclic subgraph. Conversely, if \(D\subseteq T\) is acyclic, take a topological order \(\pi\) of \(D\). Then the underlying graph of \(D\) is a subgraph of \(A_\pi(T)\), and hence
\[
\chi(D)\le \chi(A_\pi(T)).
\]

Also, if \(\pi^{\mathrm{rev}}\) is the reverse order, then
\[
A_{\pi^{\mathrm{rev}}}(T)=\overline{A_\pi(T)}. \tag{3}
\]

---

## 3. Fractional chromatic tools

Define the fractional analogue
\[
\phi(T)=\max_\pi \chi_f(A_\pi(T)).
\]

For every \(N\)-vertex graph \(G\),
\[
\chi_f(G)\le \chi(G)\le (\log N+2)\chi_f(G). \tag{4}
\]

For completeness, the second inequality follows by randomized rounding of an optimal fractional coloring. If the total fractional weight is \(\tau=\chi_f(G)\), sample
\[
m=\left\lceil \tau(\log N+1)\right\rceil
\]
independent sets according to the normalized fractional coloring. Each vertex remains uncovered with probability at most \(e^{-m/\tau}<1/(eN)\), so the expected number of uncovered vertices is less than one. Hence some sample covers every vertex; assigning each vertex to one sampled independent set containing it gives a proper coloring with at most \(m\le(\log N+2)\tau\) colors.

Applying (4) to agreement graphs gives
\[
\frac{f(T)}{\log |T|+2}\le \phi(T)\le f(T). \tag{5}
\]

Thus the theorem from the source paper implies
\[
\phi(R)\ge |R|^{5/9-o(1)} \tag{6}
\]
for every tournament \(R\). Equivalently, for every fixed \(\eta>0\), there is \(c_\eta>0\) such that
\[
\phi(R)\ge c_\eta |R|^{5/9-\eta} \tag{7}
\]
for every finite tournament \(R\). The constant can be adjusted to cover the finitely many small orders.

### Graph-substitution lemma

Let \(H\) be a graph on \([r]\), and let \(G_1,\ldots,G_r\) be graphs. Write
\[
H(G_1,\ldots,G_r)
\]
for the graph obtained by replacing vertex \(i\) by \(G_i\), putting all possible edges between \(G_i,G_j\) when \(ij\in E(H)\), and no edges between them otherwise.

If
\[
\chi_f(G_i)\ge w\qquad\text{for every }i,
\]
then
\[
\chi_f\bigl(H(G_1,\ldots,G_r)\bigr)\ge w\chi_f(H). \tag{8}
\]

To prove this, use the dual formulation
\[
\chi_f(G)=
\max\left\{
\sum_{v\in V(G)}x_v:
x_v\ge0,\ 
\sum_{v\in I}x_v\le1\ \text{for every independent set }I
\right\}. \tag{9}
\]
Let \(y_i\) be an optimal dual solution for \(H\), and let \(x^i_v\) be an optimal dual solution for \(G_i\). Assign
\[
z_v=y_i x^i_v \qquad(v\in V(G_i)).
\]
If \(S\) is independent in \(H(G_1,\ldots,G_r)\), then the indices of the blocks met by \(S\) form an independent set of \(H\), and \(S\cap V(G_i)\) is independent in \(G_i\). Therefore
\[
\sum_{v\in S}z_v
\le \sum_{i:\,S\cap V(G_i)\ne\varnothing}y_i
\le1.
\]
Its objective value is at least
\[
\sum_i y_i w=w\chi_f(H),
\]
proving (8).

---

## 4. A general tournament-composition inequality

Let
\[
T=Q(T_1,\ldots,T_r)
\]
be a tournament substitution: between \(T_i\) and \(T_j\), all arcs have the direction of the quotient arc \(ij\) in \(Q\).

### Proposition

For every fixed \(\eta>0\), there is \(c'_\eta>0\) such that
\[
\phi(T)\ge
c'_\eta r^{-4/9-\eta}
\sum_{i=1}^r \phi(T_i). \tag{10}
\]

#### Proof

Put \(w_i=\phi(T_i)\) and relabel so that
\[
w_1\ge w_2\ge\cdots\ge w_r.
\]
For each \(q\), consider the subtournament consisting of \(T_1,\ldots,T_q\), whose quotient is \(Q_q=Q[\{1,\ldots,q\}]\).

Choose orders inside the \(T_i\) attaining \(w_i\), and an order of \(Q_q\) attaining \(\phi(Q_q)\). Concatenating the block orders produces an agreement graph which is a graph substitution. By (8),
\[
\phi(T)\ge w_q\phi(Q_q).
\]
Using (7),
\[
\phi(T)\ge c_\eta w_q q^{5/9-\eta}. \tag{11}
\]
Writing \(M=\phi(T)\), this gives
\[
w_q\le c_\eta^{-1}M q^{-5/9+\eta}.
\]
Hence
\[
\sum_{q=1}^r w_q
\le c_\eta^{-1}M\sum_{q=1}^r q^{-5/9+\eta}
\le C_\eta M r^{4/9+\eta}.
\]
Rearranging proves (10). ∎

---

## 5. Proof of the partial theorem

Under the hypotheses of the partial theorem, \(T=Q(T_1,\ldots,T_r)\) where each \(T_i\) is transitive of order
\[
s_i=|V_i|.
\]
Ordering a transitive tournament in its arc direction makes its agreement graph complete, so
\[
\phi(T_i)=s_i.
\]
Therefore
\[
\sum_{i=1}^r\phi(T_i)=\sum_{i=1}^r s_i=n.
\]
Applying (10) and using \(f(T)\ge\phi(T)\) gives
\[
f(T)\ge c_\eta n r^{-4/9-\eta},
\]
which is (1).

Now suppose
\[
r\le n^{9/16+o(1)}.
\]
For fixed \(\eta>0\),
\[
f(T)
\ge n^{\,1-(4/9+\eta)(9/16+o(1))}
= n^{\,3/4-(9/16)\eta-o(1)}.
\]
Since \(\eta>0\) can be chosen arbitrarily small, this yields
\[
f(T)\ge n^{3/4-o(1)}.
\]

### A source-free companion estimate

Under the same homogeneous transitive-block hypotheses, one also has the exact elementary bound
\[
f(T)\ge \left(\sum_{i=1}^r s_i^2\right)^{1/2}
\ge \frac{n}{\sqrt r}. \tag{12}
\]

To see this, choose any order of the quotient and let \(H\) be its agreement graph. Ordering every block internally in its transitive direction gives the graph
\[
H(K_{s_1},\ldots,K_{s_r}).
\]
Reversing only the order of the blocks gives
\[
\overline H(K_{s_1},\ldots,K_{s_r}).
\]

Let
\[
L=\max\left\{\sum_{i\in I}s_i:I\text{ independent in }H\right\}.
\]
In the first graph, assigning dual weight \(s_i/L\) to every vertex in block \(i\) is feasible in (9), giving fractional chromatic number at least
\[
\frac{\sum_i s_i^2}{L}.
\]
For an \(H\)-independent set \(I\) of weight \(L\), the union of the corresponding blocks is a clique of size \(L\) in the second graph. Thus the second graph has chromatic number at least \(L\). One of the two orders consequently gives at least
\[
\max\left\{L,\frac{\sum_i s_i^2}{L}\right\}
\ge \left(\sum_i s_i^2\right)^{1/2}.
\]
Cauchy–Schwarz gives the last inequality in (12). This alone proves the conjectured exponent when \(r\le n^{1/2+o(1)}\); the source theorem improves the range to \(r\le n^{9/16+o(1)}\).

---

## 6. Other rigorous sufficient conditions

Two elementary inequalities further delimit what a counterexample would have to look like.

### 6.1 Largest transitive subtournament

Let \(\tau(T)\) be the largest order of a transitive subtournament of \(T\). Then
\[
f(T)\ge \max\left\{\tau(T),\frac{n}{\tau(T)}\right\}. \tag{13}
\]

The first term follows by ordering a largest transitive subtournament in its arc direction, producing a clique.

For the second, an independent set in any agreement graph \(A_\pi(T)\) has every tournament arc pointing backwards relative to \(\pi\), and hence induces a transitive tournament. Thus
\[
\alpha(A_\pi(T))\le\tau(T),
\]
and so
\[
\chi(A_\pi(T))\ge\frac{n}{\tau(T)}.
\]

Consequently, the conjecture already holds if either
\[
\tau(T)\le n^{1/4+o(1)}
\quad\text{or}\quad
\tau(T)\ge n^{3/4-o(1)}.
\]
If, for some fixed \(\delta>0\),
\[
f(T)\le n^{3/4-\delta},
\]
then necessarily
\[
n^{1/4+\delta}\le\tau(T)\le n^{3/4-\delta}. \tag{14}
\]

### 6.2 Distance from a transitive tournament

Let \(b(T)\) be the minimum number of backward arcs in a linear order of \(T\). Then
\[
f(T)\ge \frac{n^2}{n+2b(T)}. \tag{15}
\]

Choose an order attaining \(b(T)\), and properly color its agreement graph with \(k\) color classes of sizes \(a_1,\ldots,a_k\). Every pair inside a color class is a backward arc. Hence
\[
b(T)\ge \sum_{i=1}^k\binom{a_i}{2}
=\frac12\left(\sum_i a_i^2-n\right)
\ge\frac12\left(\frac{n^2}{k}-n\right),
\]
which rearranges to (15).

Thus the conjecture holds whenever
\[
b(T)\le n^{5/4+o(1)}.
\]
A fixed-exponent counterexample as in (14) would have to satisfy
\[
b(T)\ge \frac12\left(n^{5/4+\delta}-n\right). \tag{16}
\]

The same argument applies to every induced subtournament \(S\):
\[
f(T)\ge \frac{|S|^2}{|S|+2b(T[S])}. \tag{17}
\]

---

## 7. Remaining gap

The homogeneous-block theorem does not address arbitrary partitions into transitive subtournaments: uniform orientation between distinct blocks is essential to make the agreement graph a graph substitution. In particular, a tournament with no nontrivial homogeneous modules is not improved upon by this argument. Taking all blocks to be singletons gives \(r=n\), and (1) merely recovers
\[
f(T)\ge n^{5/9-o(1)},
\]
the known source-paper bound.

Thus an unresolved tournament may simultaneously have:

- no useful coarse partition into transitive homogeneous modules;
- transitive-subtournament number in the intermediate range (14);
- feedback-arc number at least the scale in (16).

The argument therefore supplies a structural special case and composition inequality, but neither proves nor disproves Conjecture 4.1.