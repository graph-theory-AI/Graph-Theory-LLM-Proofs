```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The unquantified asymptotic conjecture remains open, but there is a nearest-integral-above-threshold finite failure R(3;12,7)=6>A_2(12,7)+1=5, alongside infinite Plotkin-tight families where equality holds.",
  "would_publish": false,
  "caveats": "“Sufficiently close” is not quantified; the finite counterexample does not refute an eventual r→∞ formulation."
}
```

# Mathematical writeup

## 1. Reformulation

I use the standard convention that \(A_q(r,s)\) is the maximum size of a \(q\)-ary code of length \(r\) and minimum Hamming distance at least \(s\).

Given an \(s\)-set-coloring of \(K_N\) from the palette \([r]\), let \(G_i\) be the graph consisting of the edges receiving color \(i\). The coloring is bad—meaning it has no \(K_{q+1}\) whose edges share a color—if and only if every \(G_i\) is \(K_{q+1}\)-free. Moreover,

\[
\sum_{i=1}^r e(G_i)=s\binom N2.
\]

Writing \(t_q(N)=\operatorname{ex}(N,K_{q+1})\), Turán's theorem therefore gives the necessary condition

\[
s\binom N2\le r\,t_q(N). \tag{1}
\]

A \(q\)-ary code gives the usual lower-bound construction: in coordinate \(i\), pairs of words with different symbols form a complete \(q\)-partite graph. Thus

\[
R(q+1;r,s)\ge A_q(r,s)+1.
\]

Conversely, if every \(G_i\) in a bad coloring happens to be \(q\)-colorable, choose a proper \(q\)-coloring of each \(G_i\). The resulting \(q\)-ary words have pairwise distance at least \(s\). Hence any strict inequality \(R-1>A_q\) must use at least one \(K_{q+1}\)-free graph of chromatic number greater than \(q\).

---

## 2. A finite counterexample at the nearest integral point above threshold

### Theorem

\[
A_2(12,7)=4
\qquad\text{and}\qquad
R(3;12,7)=6.
\]

Consequently,

\[
R(3;12,7)=6>A_2(12,7)+1=5.
\]

Here \(s-r/2=1\), so for the even length \(r=12\), this is the nearest possible integral value strictly above the zero-rate threshold.

### Proof that \(A_2(12,7)=4\)

Four codewords exist: repeat each coordinate four times in the binary code

\[
\{000,011,101,110\}.
\]

This gives length \(12\) and all pairwise distances \(8\), so \(A_2(12,7)\ge4\).

Suppose that five binary words of length \(12\) had pairwise distance at least \(7\). Let \(S\) be the sum of their ten pairwise distances. In any coordinate, if \(a\) of the five words contain \(1\), that coordinate contributes

\[
a(5-a)\le 6
\]

to \(S\). Hence \(S\le 12\cdot6=72\).

Partition the five words according to the parity of their Hamming weights. A pair in the same parity class has even distance, hence distance at least \(8\). The minimum possible number of same-parity pairs is

\[
\binom22+\binom32=4.
\]

Therefore

\[
S\ge 10\cdot7+4=74,
\]

a contradiction. Thus \(A_2(12,7)\le4\).

### A bad coloring of \(K_5\)

Let the vertex set be \(V=\{1,\dots,5\}\).

For each two-element subset \(X\subset V\), take one color whose color graph is the complete bipartite cut

\[
K_{X,V\setminus X}.
\]

There are ten such colors. A fixed edge \(uv\) crosses exactly six of these cuts: the two-element set \(X\) must contain exactly one of \(u,v\).

Take two further colors whose color graphs are a \(5\)-cycle \(C_5\) and its complement, which is another \(5\)-cycle. These two cycles partition \(E(K_5)\). Thus every edge belongs to exactly

\[
6+1=7
\]

of the twelve color graphs.

All twelve color graphs are triangle-free, so there is no triangle whose three edges share a color. Therefore

\[
R(3;12,7)\ge6. \tag{2}
\]

### No bad coloring of \(K_6\)

Suppose \(G_1,\dots,G_{12}\) are triangle-free graphs on six vertices and every edge lies in exactly seven of them. Then

\[
\sum_{i=1}^{12}e(G_i)=7\binom62=105. \tag{3}
\]

By Mantel's theorem, \(e(G_i)\le9\).

A non-bipartite triangle-free graph on six vertices has at most seven edges: it contains a \(5\)-cycle, and the sixth vertex has at most two neighbors on that cycle. Consequently, there can be at most one non-bipartite \(G_i\), since two such graphs would give

\[
\sum_i e(G_i)\le 2\cdot7+10\cdot9=104,
\]

contrary to (3).

If all twelve \(G_i\) are bipartite, choose a bipartition for each. The six vertices then give six binary words of length \(12\), and every pair differs in at least the seven coordinates corresponding to the graphs containing that edge. This contradicts \(A_2(12,7)=4\).

It remains to rule out exactly one non-bipartite graph, say \(H=G_{12}\). Let \(h=e(H)\le7\). Choose bipartitions of the other eleven graphs and let \(x_v\in\{0,1\}^{11}\) be the word assigned to vertex \(v\). Then

\[
d(x_u,x_v)\ge
\begin{cases}
6,&uv\in E(H),\\
7,&uv\notin E(H).
\end{cases} \tag{4}
\]

Let \(S\) be the sum of the fifteen pairwise distances. Every binary coordinate separates at most \(3\cdot3=9\) pairs, so

\[
S\le 11\cdot9=99. \tag{5}
\]

The baseline in (4) sums to \(105-h\). Thus the total excess over that baseline is at most

\[
99-(105-h)=h-6\le1. \tag{6}
\]

Partition the six words by the parity of their weights. For an edge of \(H\), the baseline distance in (4) is even; if its endpoints have different parities, its distance is at least \(7\), contributing an excess of at least one. For a nonedge of \(H\), the baseline is odd; if its endpoints have the same parity, its distance is at least \(8\), again contributing an excess of at least one.

It follows from (6) that \(H\) differs in at most one pair from the union of the two cliques induced by the parity classes. But every partition of six vertices has either:

- a class of size at least four, in which case deleting at most one edge from its clique leaves a triangle; or
- two classes of size three, in which case there are two disjoint triangles and one edge change cannot destroy both.

Thus \(H\) contains a triangle, a contradiction. Therefore no bad coloring exists on \(K_6\), proving

\[
R(3;12,7)\le6.
\]

Together with (2), this establishes \(R(3;12,7)=6\).

---

## 3. Infinite families where the conjectured equality is exact

The preceding exception does not mean equality is rare. There is an elementary infinite family approaching the zero-rate threshold from above.

### Proposition

Let \(q\ge2\), \(a\ge2\), and \(M=qa\). Define

\[
r_0=\frac{M!}{(a!)^q}
\]

and

\[
s_0=q(q-1)\frac{(M-2)!}{(a-1)!^2(a!)^{q-2}}.
\]

Then for every positive integer \(\lambda\),

\[
A_q(\lambda r_0,\lambda s_0)=M
\]

and

\[
R(q+1;\lambda r_0,\lambda s_0)=M+1.
\]

### Construction

Index the coordinates by all maps

\[
f:[M]\longrightarrow[q]
\]

whose \(q\) fibers all have size \(a\). For each \(v\in[M]\), define the codeword

\[
x_v=(f(v))_f.
\]

For distinct \(u,v\), the probability over a uniformly chosen balanced map that \(f(u)\ne f(v)\) is

\[
\frac{M-a}{M-1}
 =\frac{(q-1)a}{qa-1}.
\]

Thus every pair of codewords has distance exactly \(s_0\), and

\[
\frac{s_0}{r_0}
 =\frac{(q-1)a}{qa-1}
 =\frac{t_q(M)}{\binom M2}. \tag{7}
\]

Repeating every coordinate \(\lambda\) times gives the asserted code of size \(M\).

For \(M=qa\),

\[
\frac{t_q(M+1)}{\binom{M+1}{2}}
 =\frac{(q-1)(qa+2)}{q(qa+1)}.
\]

A direct calculation gives

\[
\frac{(q-1)a}{qa-1}
-
\frac{(q-1)(qa+2)}{q(qa+1)}
=
\frac{2(q-1)}
 {q(qa-1)(qa+1)}
>0. \tag{8}
\]

Hence a bad coloring on \(M+1\) vertices would violate the Turán inequality (1). The same calculation also rules out a code of size \(M+1\). Therefore both maxima are exactly \(M\).

The relative distance in (7) satisfies

\[
\frac{s_0}{r_0}
=
1-\frac1q+\frac{q-1}{q(M-1)},
\]

so these examples approach the threshold \(1-1/q\).

### Economical prime-power version

If \(q\) is a prime power and \(m\ge2\), the \(q\)-ary simplex code has parameters

\[
M=q^m,\qquad
r=\frac{q^m-1}{q-1},\qquad
s=q^{m-1}.
\]

It meets (7), so

\[
A_q(r,s)=q^m,
\qquad
R(q+1;r,s)=q^m+1.
\]

Moreover,

\[
q s-(q-1)r=1,
\]

the smallest possible positive integral excess above the threshold. Thus equality holds for infinitely many parameters at the arithmetically closest possible distance above the threshold.

---

## 4. A general sufficient condition for equality

For completeness, define

\[
\gamma_q(N)
=
t_q(N)-
\max\{e(H): H\text{ is }K_{q+1}\text{-free and }\chi(H)>q\},
\]

with \(\gamma_q(N)=\infty\) if no such graph exists.

If a bad coloring on \(N\) vertices exists, its total Turán deficit is

\[
\Delta_q(N)
=
r\,t_q(N)-s\binom N2.
\]

If

\[
0\le \Delta_q(N)<\gamma_q(N), \tag{9}
\]

then every color graph must be \(q\)-colorable. Choosing a proper \(q\)-coloring for each color graph produces a \(q\)-ary code of size \(N\) and minimum distance at least \(s\).

Consequently, if \(N=A_q(r,s)+1\) satisfies either \(\Delta_q(N)<0\) or (9), then

\[
R(q+1;r,s)=A_q(r,s)+1.
\]

This isolates the obstruction: a strict gap can only occur when the available total Turán deficit is large enough to support one or more non-\(q\)-colorable \(K_{q+1}\)-free color graphs. The two \(C_5\)'s in the \((q,r,s)=(2,12,7)\) example are exactly such obstructions.

---

## 5. Remaining gap

The source statement does not specify what “sufficiently close” means. The counterexample above refutes an unqualified all-parameter interpretation and shows that even the nearest integral value above the threshold can fail at small length. It does **not** rule out a statement of the form:

\[
\exists \eta(q)>0,\ r_0(q)
\quad
\forall r\ge r_0(q),\qquad
0<s/r-(1-1/q)<\eta(q)
\Longrightarrow
R(q+1;r,s)=A_q(r,s)+1,
\]

nor a formulation involving \(q s-(q-1)r=o(r)\). The infinite Plotkin-tight family proves equality only on sparse parameter sequences. Controlling compatible families of non-\(q\)-colorable near-Turán graphs in all remaining parameters is the unresolved step.