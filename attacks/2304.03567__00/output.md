```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Under the source's apparent n^2-density normalization, a bidirected depth-two ternary tree gives r_t <= 2/9, and 2/9 is the exact asymptotic value for symmetric strongly connected digraphs.",
  "would_publish": false,
  "caveats": "The global lower bound remains 1/9; the catalog is ambiguous about normalization, and the full paper may already contain the 2/9 upper bound."
}
```

## 1. Formalization

For a total order \(\prec\) of \(V(D)\), let \(D_\prec\) consist of the arcs \(xy\in A(D)\) with \(x\prec y\). Write
\[
f(D,\prec)=\bigl|\{\{x,y\}:x\prec y\text{ and }y\text{ is reachable from }x\text{ in }D_\prec\}\bigr|
\]
and
\[
F(D)=\max_\prec f(D,\prec).
\]

The numerical lower bound \(r_t\ge 1/9\) quoted in the catalog appears to use the extremal-density convention
\[
r_t=\liminf_{n\to\infty}\ \min_{\substack{|V(D)|=n\\D\text{ strong}}}\frac{F(D)}{n^2},
\]
or an equivalent formulation allowing an \(o(n^2)\) error.

I prove:

> **Partial theorem.**
> 1. There is a family of strongly connected digraphs \(D_m\), with \(n=3m+4\), such that
>    \[
>    F(D_m)=2m^2+O(m).
>    \]
>    Consequently,
>    \[
>    r_t\le \frac29.
>    \]
> 2. Every symmetric strongly connected digraph \(D\) on \(n\) vertices satisfies
>    \[
>    F(D)\ge \frac{2(n-1)^2}{9}.
>    \]
>    Thus \(2/9\) is the exact asymptotic extremal density within the class of symmetric strongly connected digraphs, or more generally digraphs containing a bidirected spanning tree.

Combined with the source-paper bound, this leaves
\[
\boxed{\frac19\le r_t\le\frac29}.
\]

If normalization is instead by \(\binom n2\), all asymptotic constants in this writeup should be multiplied by \(2\); the symmetric-class value is then \(4/9\).

---

## 2. Orders and orientations of bidirected trees

Let \(\overleftrightarrow{T}\) denote the digraph obtained from an undirected tree \(T\) by replacing every edge \(xy\) with both arcs \(xy\) and \(yx\).

A vertex order \(\prec\) selects exactly one forward arc on every edge of \(T\), namely the arc from the earlier endpoint to the later endpoint. Thus \(D_\prec\) is an orientation of \(T\). Since a tree has a unique undirected path between every two vertices, two vertices are forward connected exactly when this unique path is consistently directed.

Conversely, every orientation of a tree is acyclic and hence has a topological ordering inducing it. Therefore FCPP on a bidirected tree is exactly the problem of orienting the tree so as to maximize the number of directed paths with distinct endpoints.

---

## 3. A \(2/9\) upper-bound construction

Let \(T_m\) be the following undirected tree:

- one root \(r\);
- three branch vertices \(c_1,c_2,c_3\), each adjacent to \(r\);
- for each \(i\), a set \(L_i\) of \(m\) leaves adjacent to \(c_i\).

Let \(D_m=\overleftrightarrow{T_m}\). It is strongly connected and has
\[
n=3m+4
\]
vertices.

Fix any vertex order and orient each tree edge forward. Let
\[
I=\{i:c_i\to r\},\qquad O=\{1,2,3\}\setminus I.
\]

For \(i\in I\), let \(k_i\) be the number of leaves in \(L_i\) whose edge is directed toward \(c_i\). These are precisely the leaves in branch \(i\) that can reach \(r\).

For \(i\in O\), let \(k_i\) be the number of leaves in \(L_i\) whose edge is directed away from \(c_i\). These are precisely the leaves in branch \(i\) reachable from \(r\).

### Counting leaf-leaf pairs

Within branch \(i\), a directed path between two leaves must have the form
\[
\ell\to c_i\to\ell'.
\]
Its number is
\[
k_i(m-k_i),
\]
regardless of whether \(i\in I\) or \(i\in O\).

Between distinct branches, the unique path passes through \(r\). Such a path is directed precisely from an \(I\)-branch toward an \(O\)-branch, giving
\[
\left(\sum_{i\in I}k_i\right)
\left(\sum_{j\in O}k_j\right)
\]
pairs.

Hence the total number \(Q\) of forward-connected pairs whose two endpoints are leaves is
\[
Q=\sum_{i=1}^3 k_i(m-k_i)
 +\left(\sum_{i\in I}k_i\right)
  \left(\sum_{j\in O}k_j\right).
\tag{1}
\]

If \(I=\varnothing\) or \(I=\{1,2,3\}\), then
\[
Q\le 3\frac{m^2}{4}<2m^2.
\]

It remains to consider \(|I|=1\); the case \(|I|=2\) is symmetric. Write \(x\) for the variable on the unique \(I\)-branch and \(y,z\) for those on the two \(O\)-branches. Then
\[
Q=x(m-x)+y(m-y)+z(m-z)+x(y+z).
\]
For fixed \(x\),
\[
y(m-y)+xy
=-\left(y-\frac{m+x}{2}\right)^2+\frac{(m+x)^2}{4},
\]
and similarly for \(z\). Therefore
\[
\begin{aligned}
Q
&\le x(m-x)+\frac{(m+x)^2}{2}\\
&=\frac{m^2}{2}+2mx-\frac{x^2}{2}\\
&\le 2m^2,
\end{aligned}
\]
since the last expression is increasing for \(0\le x\le m\), and its value at \(x=m\) is \(2m^2\).

Thus every order satisfies
\[
Q\le 2m^2.
\tag{2}
\]

There are only four non-leaf vertices. The number of unordered pairs having at least one non-leaf endpoint is at most
\[
4(3m)+\binom42=12m+6.
\]
Consequently,
\[
F(D_m)\le 2m^2+12m+6.
\tag{3}
\]

Conversely, order the vertices so that
\[
L_1\prec c_1\prec r\prec c_2,c_3\prec L_2\cup L_3,
\]
with each \(c_i\) before all leaves in \(L_i\). Then every leaf in \(L_1\) reaches every leaf in \(L_2\cup L_3\), yielding \(2m^2\) pairs. Hence
\[
2m^2\le F(D_m)\le 2m^2+O(m).
\]

Since \(n=3m+4\),
\[
\lim_{m\to\infty}\frac{F(D_m)}{n^2}=\frac29.
\]
This proves the global upper bound \(r_t\le2/9\).

---

## 4. Matching lower bound for symmetric digraphs

Call a digraph symmetric if \(xy\in A(D)\) implies \(yx\in A(D)\). Let \(D\) be a connected symmetric digraph on \(n\) vertices. Choose any spanning tree \(T\) of its underlying graph, and let \(v\) be a centroid of \(T\). Thus every component of \(T-v\) has at most \(n/2\) vertices.

Put \(S=n-1\), and let the component sizes of \(T-v\) be
\[
s_1,\dots,s_q,\qquad \sum_i s_i=S.
\]

For \(n\ge4\), each \(s_i\le n/2=(S+1)/2\le2S/3\). There is a subcollection of these components whose total size \(A\) lies in
\[
\frac S3\le A\le\frac{2S}{3}.
\tag{4}
\]
Indeed:

- if some \(s_i\in[S/3,2S/3]\), take that component;
- otherwise all \(s_i<S/3\), and greedily add components until the sum first reaches \(S/3\); the resulting sum is less than \(2S/3\).

Let \(B=S-A\). Then both \(A,B\ge S/3\), and
\[
AB=A(S-A)\ge \frac{2S^2}{9}.
\tag{5}
\]

Orient all edges in the components contributing to \(A\) toward \(v\), and orient all edges in the remaining components away from \(v\). This is an orientation of a tree, so it has a topological ordering. Because all tree edges occur in both directions in \(D\), this topological ordering realizes the prescribed oriented edges as forward arcs.

Every vertex in the \(A\)-side reaches \(v\), and \(v\) reaches every vertex in the \(B\)-side. Thus every one of the \(AB\) cross pairs is forward connected. By (5),
\[
F(D)\ge AB\ge\frac{2(n-1)^2}{9}.
\]

The construction \(D_m\) from the previous section is itself symmetric and satisfies
\[
F(D_m)=\left(\frac29+o(1)\right)|V(D_m)|^2.
\]
Therefore the asymptotic extremal constant for symmetric strongly connected digraphs is exactly
\[
\boxed{\frac29}.
\]

The proof only uses a bidirected spanning tree, so the same lower bound holds whenever \(D\) contains one.

---

## 5. What remains open

The centroid argument cannot be transferred directly to arbitrary strong digraphs: it prescribes independently whether each spanning-tree edge points toward or away from the centroid, while a general digraph need not contain both orientations of those edges.

Thus the argument does not improve the global lower bound \(1/9\). Subject to the normalization above, the remaining interval is
\[
\frac19\le r_t\le\frac29.
\]

Finally, if “best approximation ratio” is meant literally as the best polynomial-time ratio \( \mathrm{ALG}/\mathrm{OPT}\), rather than the extremal density \(F(D)/n^2\), then the catalog statement is insufficiently precise: the construction above is an extremal upper bound, not an approximation-hardness result.