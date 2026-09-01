```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "After correcting the malformed asymptotic statement, I recover the missing residue formula, prove the standard adaptive lower bound, and verify the conjectured exponent as optimal for a broad single-core fan strategy class, but unrestricted multicore adaptivity remains open.",
  "would_publish": false,
  "caveats": "I interpret the catalog's 2^{o(m)} as p^{o(1)} in the fixed-m, p-to-zero limit; the restricted-strategy result does not prove the conjecture."
}
```

# 1. Corrected statement

The displayed factor \(2^{o(m)}\) is not meaningful in the setting described, where \(m\) is fixed and \(p\to0\). The intended form of Conjecture 9 is

\[
f(K_m,p)=p^{-\tau_m+o(1)},\qquad
\tau_m=\frac{2m}{3}-c_m .
\]

The case formula consistent with the source construction is

\[
c_m=
\begin{cases}
\dfrac{m}{2m-3},&m\equiv0\pmod 3,\\[6pt]
\dfrac23,&m\equiv1\pmod 3,\\[6pt]
\dfrac{2m+5}{6m-12},&m\equiv2\pmod 3.
\end{cases}
\]

Thus, writing \(m=3k+r\),

\[
\tau_m=
\begin{cases}
2k-\dfrac{k}{2k-1},&m=3k,\\[7pt]
2k,&m=3k+1,\\[7pt]
2k+1-\dfrac1{2k},&m=3k+2.
\end{cases}
\]

For example,

\[
\begin{array}{c|c|c}
m&c_m&\tau_m\\ \hline
4&2/3&2\\
5&5/6&5/2\\
6&2/3&10/3\\
7&2/3&4\\
8&7/12&19/4\\
9&3/5&27/5
\end{array}
\]

The cases \(m=4,5\) agree with the stated resolved cases.

Throughout, algorithms may be randomized, but make at most \(q\) queries. If the definition uses expected query count, truncation at a constant multiple of the expectation changes only the required success probability by a constant and does not affect any exponent below.

# 2. A general adaptive lower bound

The following useful bound is fully adaptive.

## Lemma 1: exploration bound

Let \(H\) be a fixed connected graph with \(v\) vertices and \(e\) edges. Every adaptive algorithm making at most \(q\) edge queries satisfies

\[
\Pr(\text{a queried positive copy of }H\text{ is found})
 \le C_H q^{v-1}p^e
\]

for a constant \(C_H\) depending only on \(H\).

### Proof

It suffices to consider a deterministic algorithm, conditioning on its internal randomness. Repeated queries can be deleted.

Consider a successful transcript and a particular found copy of \(H\). Order the \(e\) edges of this copy by their query times. Scan this order and retain an edge whenever it joins two different components of the previously retained edges. Since \(H\) is connected, the retained edges form a spanning tree and there are exactly \(v-1\) of them.

A witness scheme records:

1. the ordering of the \(e\) abstract edges of \(H\);
2. the query times of the \(v-1\) retained tree edges;
3. the finitely many orientation choices needed when a retained edge first identifies one or two vertices of the copy.

There are at most \(C_Hq^{v-1}\) such schemes.

Fix one scheme. Delete from a successful transcript the \(e\) positive answers belonging to the target copy. The remaining \(q-e\) answers determine the original transcript uniquely:

- at a prescribed tree-edge time, insert a positive answer and use the queried endpoints to extend the partial embedding;
- once both endpoints of a non-tree edge have been identified, its query is recognizable and its positive answer is inserted;
- every other query consumes the next undeleted answer.

The greedy spanning-tree choice is important here: a target edge queried before its endpoints had already been connected would itself be a retained tree edge, so no unrecorded target edge can be hidden among the deleted data.

Consequently, for a fixed scheme the total probability of all compatible successful transcripts is at most

\[
p^e\sum_{z\in\{0,1\}^{q-e}}p^{|z|}(1-p)^{q-e-|z|}
=p^e.
\]

Summing over the at most \(C_Hq^{v-1}\) schemes proves the lemma. \(\square\)

For \(H=K_m\), where \(e=\binom m2\), this gives

\[
f(K_m,p)=\Omega_m\!\left(p^{-m/2}\right).
\]

Indeed,

\[
\frac{e}{m-1}=\frac m2.
\]

This lower bound matches the conjectured exponent exactly only for \(m=4,5\):

\[
\tau_4=2,\qquad \tau_5=\frac52.
\]

For the first open case it gives only

\[
p^{-3+o(1)}
 \le f(K_6,p)
 \le p^{-10/3+o(1)}.
\]

Thus the ordinary exploration/certificate argument alone cannot settle \(K_6\).

# 3. Nonadaptive complexity

For comparison, the nonadaptive problem is completely elementary.

## Proposition 2

If all queries must be fixed before any answers are seen, then

\[
f_{\mathrm{na}}(K_m,p)=\Theta_m\!\left(p^{-(m-1)}\right).
\]

### Proof

Let \(Q\) be the deterministic query graph with \(q\) edges and adjacency matrix \(A\). The number of copies of \(K_m\) in \(Q\) is at most

\[
\frac{\operatorname{tr}(A^m)}{m!}
\le \frac{\sum_i|\lambda_i(A)|^m}{m!}
\le \frac{(2q)^{m/2}}{m!},
\]

because \(\sum_i\lambda_i(A)^2=2q\). Hence a union bound gives

\[
\Pr(K_m\text{ found})
 \le C_m q^{m/2}p^{\binom m2}.
\]

Constant success probability therefore requires

\[
q=\Omega_m\!\left(p^{-2\binom m2/m}\right)
=\Omega_m\!\left(p^{-(m-1)}\right).
\]

Conversely, query every edge on \(N=Cp^{-(m-1)/2}\) vertices. A standard second-moment calculation shows that \(G(N,p)\) contains \(K_m\) with probability bounded away from zero for sufficiently large \(C=C(m)\). This uses \(\Theta(p^{-(m-1)})\) queries. \(\square\)

The conjecture is therefore specifically about the additional power of fully interleaved adaptivity.

# 4. A natural “single-core fan” class

The source upper-bound exponents for \(m\ge6\) can be recovered from the following architecture.

Choose integers \(s\ge0\) and \(b\ge2\) satisfying

\[
s+b+1=m.
\]

A single-core fan strategy does the following:

1. Find and commit to a positive core \(R\cong K_s\).
2. Produce two disjoint sets \(A,B\) of common neighbors of \(R\), with
   \[
   |A|=p^{-x+o(1)},\qquad |B|=p^{-y+o(1)}.
   \]
3. Query every edge between \(A\) and \(B\).
4. For every \(a\in A\), query all pairs in its positive neighborhood
   \[
   N_B(a)=\{z\in B:az\text{ is positive}\}.
   \]
5. Succeed if some \(N_B(a)\) contains a positive \(K_b\).

Then \(R\cup\{a\}\cup K_b\) is a \(K_m\).

## Resource calculation

Obtaining \(p^{-x}\) common neighbors of an \(s\)-clique costs exponent \(s+x\), and similarly \(s+y\) for \(B\). The complete \(A\)-\(B\) batch costs exponent \(x+y\).

Moreover,

\[
\mathbb E\sum_{a\in A}\binom{|N_B(a)|}{2}
 =p^{-x-2y+2+o(1)},
\]

so the final pair-query stage costs exponent \(x+2y-2\).

Thus the total exponent is

\[
T=\max\{s+x,\ s+y,\ x+y,\ x+2y-2\}.
\tag{1}
\]

The expected number of successful configurations \((a,S)\), where
\(a\in A\), \(S\in\binom Bb\), is

\[
p^{-x-by+o(1)}p^{\,b+\binom b2}
 =p^{\binom{b+1}{2}-x-by+o(1)}.
\]

A necessary exponent-level condition for success is therefore

\[
x+by\ge \binom{b+1}{2}.
\tag{2}
\]

For the parameter choices below, the corresponding weighted clique count is balanced. Indeed, two configurations with the same \(A\)-vertex and \(j\) common \(B\)-vertices contribute a normalized overlap term of order

\[
p^{\,x+jy-\binom{j+1}{2}},
\]

while configurations with distinct \(A\)-vertices and \(j\) common \(B\)-vertices contribute

\[
p^{\,jy-\binom j2}.
\]

The displayed parameter choices make these exponents nonnegative, and strictly positive for every proper nontrivial overlap. Adding an arbitrarily small exponent slack and applying the second-moment method therefore gives constant success probability.

# 5. Optimality inside the fan class

## Proposition 3

For \(m=4\) and every \(m\ge6\), the minimum exponent \(T\) over all single-core fan strategies is exactly the conjectured exponent \(\tau_m\).

### Lower bound inside the class

Put

\[
C=\binom{b+1}{2}.
\]

From (1), \(x,y\le T-s\). Together with (2),

\[
C\le x+by\le (b+1)(T-s),
\]

so

\[
T\ge s+\frac b2.
\tag{3}
\]

Also \(x+2y\le T+2\). Since \(x\ge0\),

\[
C\le x+by
 =\frac b2(x+2y)-\left(\frac b2-1\right)x
 \le \frac b2(T+2),
\]

which yields

\[
T\ge b-1.
\tag{4}
\]

Finally, using \(y\le T-s\),

\[
\begin{aligned}
C
 &\le x+by\\
 &=(x+2y)+(b-2)y\\
 &\le T+2+(b-2)(T-s).
\end{aligned}
\]

Hence

\[
T\ge
\frac{C+(b-2)s-2}{b-1}.
\tag{5}
\]

Since \(s=m-b-1\), inequalities (3) and (4) already force \(b\) to be one of the integers nearest \(2m/3\); inequality (5) gives the correction term.

### Case \(m=3k\)

If \(b\le2k-1\), (3) gives

\[
T\ge 3k-1-\frac b2\ge 2k-\frac12.
\]

If \(b\ge2k+1\), (4) gives \(T\ge2k\). Thus only \(b=2k\), \(s=k-1\), can be optimal. Inequality (5) gives

\[
T\ge 2k-\frac{k}{2k-1}.
\]

Equality is attained with

\[
x=\frac{k}{2k-1},
\qquad
y=k+\frac12-\frac1{4k-2}.
\]

Thus

\[
T=2k-\frac{k}{2k-1}
=\frac{2m}{3}-\frac{m}{2m-3}.
\]

### Case \(m=3k+1\)

If \(b\le2k\), (3) gives \(T\ge2k\); if \(b\ge2k+1\), (4) gives the same bound. It is attained by

\[
s=k-1,\qquad b=2k+1,\qquad x=0,\qquad y=k+1.
\]

Hence

\[
T=2k=\frac{2m}{3}-\frac23.
\]

This includes \(m=4\).

### Case \(m=3k+2\), \(k\ge2\)

If \(b\le2k\), (3) gives \(T\ge2k+1\); if \(b\ge2k+2\), (4) gives \(T\ge2k+1\). Therefore the only possible optimum has

\[
b=2k+1,\qquad s=k.
\]

Inequality (5) becomes

\[
T\ge2k+1-\frac1{2k}.
\]

It is attained with

\[
x=\frac{2k+1}{2k},
\qquad
y=k+1-\frac1{2k}.
\]

Consequently,

\[
T=2k+1-\frac1{2k}
=\frac{2m}{3}-\frac{2m+5}{6m-12}.
\]

This proves the proposition. \(\square\)

For \(m=5\), this particular fan class has a worse optimum; the source's sharp \(p^{-5/2+o(1)}\) construction uses a different small-clique architecture. Thus \(K_5\) is genuinely exceptional in this optimization.

# 6. What remains open

The preceding calculation shows that merely changing

- the core size,
- the sizes of the center and leaf pools, or
- the balance between qualification, cross queries, and internal queries

cannot improve the conjectured exponent within the principal fan architecture.

It does not give a lower bound for an unrestricted adaptive algorithm. Such an algorithm may simultaneously maintain many possible cores, and a single queried edge can contribute to the common neighborhoods of many of them. It can also use positive internal edges to decide retrospectively which core and which pool to continue. In that setting:

- the eventual core is not fixed independently of the pool;
- the pool is not selected independently of its internal edges;
- summing query costs separately over candidate cores can overcount by a polynomial factor.

This “multicore sharing” is exactly what the restricted LP does not control.

The first unresolved case is therefore still

\[
\boxed{f(K_6,p)\stackrel{?}=p^{-10/3+o(1)}}.
\]

The arguments here give only

\[
p^{-3+o(1)}
\le f(K_6,p)
\le p^{-10/3+o(1)}.
\]

No complete proof or counterexample for unrestricted adaptive algorithms is obtained.