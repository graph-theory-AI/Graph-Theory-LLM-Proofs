```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For n=7, cr(M_{7,1})=6, whereas the proposed formula gives 8; in fact the values for t=1,2,3 are 6,4,3 rather than 8,7,6.",
  "would_publish": false,
  "caveats": "This concerns the ordinary topological crossing number stated; an intended restriction to even n or to geodesic drawings would be a different conjecture."
}
```

# Disproof

We prove the following exact small-order result.

\[
\operatorname{cr}(M_{7,1})=6,\qquad
\operatorname{cr}(M_{7,2})=4,\qquad
\operatorname{cr}(M_{7,3})=3.
\]

Since the conjectured values are respectively \(8,7,6\), every positive value of \(t\) for \(n=7\) is a counterexample.

## 1. A basic lower bound

For every simple graph \(G\) with \(n\ge 3\) vertices and \(m\) edges,

\[
\operatorname{cr}(G)\ge m-(3n-6).
\tag{1}
\]

Indeed, from a drawing with \(c\) crossings, delete one of the two participating edges at each crossing. At most \(c\) distinct edges are deleted, and the remaining graph is planar. Hence

\[
m-c\le 3n-6.
\]

For \(M_{7,t}\), which has \(21-t\) edges, this gives

\[
\operatorname{cr}(M_{7,t})\ge 6-t.
\tag{2}
\]

In particular,

\[
\operatorname{cr}(M_{7,2})\ge4,\qquad
\operatorname{cr}(M_{7,3})\ge3.
\]

## 2. Explicit drawings

Work on the sphere. Let

\[
O=K_{2,2,2}
\]

with its three independent parts denoted

\[
\{a_1,b_1\},\quad \{a_2,b_2\},\quad \{a_3,b_3\}.
\]

Thus \(O\) is the octahedral graph. Use its standard spherical embedding, in which every triangle

\[
x_1x_2x_3,\qquad x_i\in\{a_i,b_i\},
\]

is a face.

### A three-crossing drawing of \(M_{7,3}\)

Let \(F=a_1a_2a_3\), and place a new vertex \(z\) inside \(F\).

Draw \(za_1,za_2,za_3\) inside \(F\). For each \(\{i,j,\ell\}=\{1,2,3\}\), draw \(zb_i\) so that it:

1. travels inside \(F\) to an interior point of \(a_ja_\ell\);
2. crosses \(a_ja_\ell\) once;
3. continues inside the adjacent face \(b_i a_j a_\ell\) to \(b_i\).

The six arcs in \(F\) can be chosen internally disjoint, apart from their common endpoint \(z\), and the portions outside \(F\) lie in three different faces. Thus the only crossings are

\[
zb_1\mathbin{\times}a_2a_3,\qquad
zb_2\mathbin{\times}a_1a_3,\qquad
zb_3\mathbin{\times}a_1a_2.
\]

The resulting graph contains every edge of \(K_7\) except

\[
a_1b_1,\quad a_2b_2,\quad a_3b_3.
\]

It is therefore \(M_{7,3}\), drawn with three crossings. Together with (2),

\[
\operatorname{cr}(M_{7,3})=3.
\tag{3}
\]

### A four-crossing drawing of \(M_{7,2}\)

Add the edge \(a_1b_1\) as follows. Route it through the face \(a_1b_2b_3\), cross the edge \(b_2b_3\) once, and then continue through the face

\[
B=b_1b_2b_3
\]

to \(b_1\). These faces were not used internally by the edges incident with \(z\), so this creates exactly one further crossing.

The resulting graph is \(M_{7,2}\), with four crossings. By (2),

\[
\operatorname{cr}(M_{7,2})=4.
\tag{4}
\]

### A six-crossing drawing of \(M_{7,1}\)

Now add \(a_2b_2\). Route it through the face \(b_1a_2b_3\), cross \(b_1b_3\) once, and continue through \(B=b_1b_2b_3\) to \(b_2\).

Inside \(B\), draw the portions of \(a_1b_1\) and \(a_2b_2\) with exactly one mutual crossing. This is possible—and in fact forced if both portions remain in \(B\)—because their four boundary endpoints alternate around \(\partial B\).

Thus the complete crossing list consists of:

- the original three crossings involving the edges incident with \(z\);
- \(a_1b_1\mathbin{\times}b_2b_3\);
- \(a_2b_2\mathbin{\times}b_1b_3\);
- \(a_1b_1\mathbin{\times}a_2b_2\).

Hence

\[
\operatorname{cr}(M_{7,1})\le6.
\tag{5}
\]

To prove the matching lower bound, take a good drawing of \(M_{7,1}\) with \(c\) crossings. For each vertex \(v\), let \(c_v\) be the number of crossings remaining after deleting \(v\). Every crossing has four distinct endpoint vertices, so it survives exactly three of the seven vertex deletions. Consequently,

\[
\sum_v c_v=3c.
\tag{6}
\]

Deleting either endpoint of the unique missing edge leaves \(K_6\), which has at least

\[
15-(3\cdot6-6)=3
\]

crossings by (1). Deleting any of the other five vertices leaves \(K_6-e\), which has at least

\[
14-(3\cdot6-6)=2
\]

crossings. Therefore

\[
3c=\sum_v c_v\ge 2\cdot3+5\cdot2=16,
\]

and hence \(c\ge6\). Combining this with (5),

\[
\operatorname{cr}(M_{7,1})=6.
\tag{7}
\]

## 3. Contradiction with the proposed formula

For \(n=7\),

\[
k=\left\lfloor\frac72\right\rfloor=3
\]

and

\[
H(7)=\frac14(3)(3)(2)(2)=9.
\]

The proposed formula becomes

\[
H(7)-\frac12t(k-1)(k-2)
=9-\frac12t(2)(1)
=9-t.
\]

Thus it predicts

\[
\begin{array}{c|ccc}
t&1&2&3\\ \hline
\text{conjectured}&8&7&6\\
\text{actual}&6&4&3.
\end{array}
\]

In particular, \(M_{7,1}=K_7-e\) alone is an explicit counterexample.

## 4. An infinite family of counterexamples from the supplied upper bound

The failure is not merely a small-order exception. Use the upper-bound construction quoted in the question for \(M_{2k,k}\). It gives a good drawing with at most

\[
\begin{aligned}
C_k
&=H(2k)-\frac12k(k-1)(k-2)\\
&=\frac14k(k-1)(k-2)(k-3)
\end{aligned}
\]

crossings.

Deleting any vertex from \(M_{2k,k}\) leaves \(M_{2k-1,k-1}\). Every crossing survives exactly \(2k-4\) of the \(2k\) vertex deletions. Hence one deletion has at most

\[
A_k=\frac{2k-4}{2k}C_k
=\frac14 (k-1)(k-2)^2(k-3)
\]

crossings. Therefore

\[
\operatorname{cr}(M_{2k-1,k-1})\le A_k.
\tag{8}
\]

On the other hand, the conjectured value for this graph is

\[
Q_k
=\frac14(k-1)^2(k-2)^2
-\frac12(k-1)(k-2)(k-3).
\]

A direct subtraction gives

\[
Q_k-A_k=\frac12(k-1)(k-2)>0
\]

for every \(k\ge3\). Thus the upper-bound construction in the source itself, followed by vertex deletion, yields infinitely many odd-order counterexamples at maximum matching size.

## Scope

There is no gap in the disproof for the ordinary topological crossing number and the statement as extracted. A modified conjecture restricted, for example, to even \(n\), or to geodesic/rectilinear drawings, is not settled by the explicit \(n=7\) argument and would require a separate formulation.