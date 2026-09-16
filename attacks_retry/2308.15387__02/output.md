```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A dual-matching argument proves M(r,s) >= ceil(((168 - 24 sqrt(2))/47)(s+1) - 6) for s >= 14, and also gives rounded r-dependent lower bounds.",
  "would_publish": false,
  "caveats": "The exact minimum remains undetermined in general; no claim of literature novelty or best-known status is made, and isolated vertices are permitted."
}
```

## 1. Results obtained

Write
\[
M(r,s)=\min\left\{|\mathcal H|:
\mathcal H\subseteq\binom{[r]}s
\text{ is intersecting and }\tau(\mathcal H)=s\right\}.
\]
The ground set may contain isolated vertices.

The main result below is an improvement of the asymptotic linear lower bound derived in the supplied attempt. It does not depend on that attempt’s nontrivial small-\(s\) assertions.

Put
\[
\eta=\frac{5+6\sqrt2}{47}=0.286920880\ldots,
\qquad
c=4(1-\eta)=\frac{168-24\sqrt2}{47}
=2.852316478\ldots.
\]

### Theorem 1
For every \(r\ge 2s-1\) and \(s\ge14\),
\[
\boxed{\displaystyle
M(r,s)\ge
\left\lceil c(s+1)-6\right\rceil.}
\tag{1}
\]
In particular,
\[
M(r,s)\ge (2.852316478\ldots-o(1))s
\]
uniformly in \(r\).

I also give:

* a fully specified rounded lower-bound recursion incorporating \(r\);
* the exact boundary value
  \[
  M(2s-1,s)=\binom{2s-1}{s};
  \tag{2}
  \]
* an elementary projective-plane construction showing that, when \(s-1\) is a prime power,
  \[
  M(r,s)\le s^2-3s+6
  \qquad\text{for }r\ge s^2-s+1.
  \tag{3}
  \]

No assertion is made that these bounds improve the published literature.

---

## 2. An incidence-dual matching lemma

The key point is to improve on covering edges solely by greedy choices and arbitrary pairing.

Let \(\mathcal F=\{F_1,\dots,F_n\}\) be an intersecting \(s\)-uniform hypergraph in which every vertex has degree at most three. For each nonisolated ground-set vertex \(x\), form the dual block
\[
B_x=\{i:x\in F_i\}\subseteq[n].
\]
Blocks are counted with multiplicity: different ground-set vertices can induce identical blocks.

Every block has size one, two, or three; every point \(i\in[n]\) belongs to exactly \(s\) blocks; and every pair of points belongs to at least one block.

Let \(b_j\) be the number of blocks of size \(j\), and let
\[
\lambda_{ij}=|\{x:\{i,j\}\subseteq B_x\}|.
\]
Define the total repeated-pair count
\[
E=\sum_{i<j}(\lambda_{ij}-1)\ge0.
\]
Since
\[
ns=b_1+2b_2+3b_3,
\qquad
\binom n2+E=b_2+3b_3,
\]
we have
\[
D:=ns-\binom n2=b_1+b_2+E.
\tag{4}
\]

Choose a maximum matching of three-element dual blocks. Let its size be \(\nu\), let \(W\) be the union of its blocks, and put
\[
U=[n]\setminus W,\qquad u=|U|=n-3\nu.
\]

### Lemma 2
If \(u\ge12\), then
\[
\boxed{\displaystyle
\binom u2\le \frac{\nu u}{2}+D.}
\tag{5}
\]

#### Proof

There is no three-element block contained in \(U\), by maximality of the matching. Consequently, every pair of \(U\) is covered either by a two-element block contained in \(U\), or by a three-element block meeting \(U\) in exactly two points.

Let \(\alpha\) count the latter blocks. Then
\[
\binom u2\le b_2+\alpha.
\tag{6}
\]

For each \(a\in W\), define a multigraph \(L_a\) on \(U\): an edge \(xy\) represents a dual block \(\{a,x,y\}\).

If \(\{a,b,d\}\) is one of the matched triples, no edge of \(L_a\) can be disjoint from an edge of \(L_b\). Otherwise, those two triples would replace \(\{a,b,d\}\), increasing the matching size. The same holds for the other two pairs of labels.

Set
\[
e_a=\sum_{x\in U}\max\{d_{L_a}(x)-1,0\}.
\]
Deleting at most \(e_a\) edges from \(L_a\) leaves a matching \(P_a\). Indeed, repeatedly deleting an edge incident with a vertex of degree at least two decreases the displayed excess by at least one.

For a matched triple \(\{a,b,d\}\), the matchings \(P_a,P_b,P_d\) are pairwise cross-intersecting. If one contains at least three edges, the other two must be empty. If all have size at most two, their total size is at most six. Since \(u\ge12\), in either case
\[
|P_a|+|P_b|+|P_d|\le \frac u2.
\]
Summing over the \(\nu\) matched triples gives
\[
\alpha=\sum_{a\in W}|L_a|
\le \frac{\nu u}{2}+\sum_{a\in W}e_a.
\tag{7}
\]

For \(a\in W\) and \(x\in U\), the degree \(d_{L_a}(x)\) is at most \(\lambda_{ax}\). Thus
\[
\sum_{a\in W}e_a
\le
\sum_{\substack{a\in W\\x\in U}}(\lambda_{ax}-1)
\le E.
\]
Combining this with (4), (6), and (7) proves (5). ∎

---

## 3. A general transversal bound

We prove a statement slightly more general than Theorem 1.

### Proposition 3
Let \(\mathcal H\) be any intersecting \(s\)-uniform hypergraph with \(m\) edges. Define
\[
K_s=
\max\left\{
\eta(s+1)+\frac12,\,
\frac{s}{6}+\frac{29}{12}
\right\}.
\]
Then
\[
\boxed{\displaystyle
\tau(\mathcal H)\le \frac m4+K_s.}
\tag{8}
\]
For \(s\ge14\),
\[
K_s=\eta(s+1)+\frac12.
\tag{9}
\]

#### Proof

Repeatedly choose a vertex incident with at least four remaining edges, and delete all edges incident with it. Suppose \(t\) vertices have been chosen when this process stops, and \(n\) edges remain. Then
\[
4t\le m-n.
\tag{10}
\]

If \(n=0\), the assertion follows immediately. Otherwise the residual family satisfies the hypotheses of Section 2. Moreover,
\[
n\le2s+1:
\tag{11}
\]
a fixed residual edge has \(s\) vertices, each meeting at most two other residual edges.

Use the notation \(\nu,u\) from Section 2. The \(\nu\) ground-set vertices corresponding to the matched triples hit \(3\nu\) residual edges. The remaining \(u\) edges can be hit using at most \(\lceil u/2\rceil\) vertices: pair the edges and choose a point in each pairwise intersection.

Consequently,
\[
\tau(\mathcal H)
\le t+\nu+\left\lceil\frac u2\right\rceil
=t+\left\lceil\frac{n-\nu}{2}\right\rceil.
\tag{12}
\]

### Case 1: \(u\le11\)

Using \(\nu=(n-u)/3\) and (10),
\[
\begin{aligned}
\tau(\mathcal H)
&\le \frac{m-n}{4}+\frac{n-u}{3}
       +\left\lceil\frac u2\right\rceil\\
&=\frac m4+\frac n{12}
  +\left(\left\lceil\frac u2\right\rceil-\frac u3\right).
\end{aligned}
\]
For integers \(0\le u\le11\), the bracket is at most \(7/3\). By (11),
\[
\tau(\mathcal H)
\le \frac m4+\frac s6+\frac{29}{12}.
\tag{13}
\]

### Case 2: \(u\ge12\)

Lemma 2 gives
\[
u(u-1)\le \nu u+2ns-n(n-1).
\]
Since \(u\le n\),
\[
u(u-\nu)\le 2(s+1)n-n^2.
\]
Substituting \(u=n-3\nu\), we obtain
\[
12\nu^2-7n\nu+2n^2-2(s+1)n\le0.
\]
Therefore
\[
\nu\ge
\frac{7n-\sqrt{96(s+1)n-47n^2}}{24}.
\tag{14}
\]

Equations (10), (12), and (14) imply
\[
\tau(\mathcal H)
\le
\frac m4+
\frac{5n+\sqrt{96(s+1)n-47n^2}}{48}
+\frac12.
\tag{15}
\]

For any \(S>0\) and any real \(x\) for which the square root is defined,
\[
\frac{5x+\sqrt{96Sx-47x^2}}{48}\le\eta S.
\tag{16}
\]
To check this, write \(y=x-48S/47\), so that
\[
96Sx-47x^2=\frac{2304S^2}{47}-47y^2.
\]
Cauchy–Schwarz gives
\[
\begin{aligned}
5x+\sqrt{96Sx-47x^2}
&=\frac{240S}{47}
  +5y+\sqrt{\frac{2304S^2}{47}-47y^2}\\
&\le \frac{240S}{47}+\frac{288\sqrt2\,S}{47}\\
&=48\eta S.
\end{aligned}
\]
Taking \(S=s+1\) in (15) proves
\[
\tau(\mathcal H)
\le \frac m4+\eta(s+1)+\frac12.
\tag{17}
\]

Together, the two cases prove (8).

Finally, \(\eta>1/6\), and at \(s=14\),
\[
\eta(s+1)+\frac12-
\left(\frac s6+\frac{29}{12}\right)
=15\eta-\frac{17}{4}>0.
\]
The difference increases with \(s\), proving (9). ∎

### Deduction of Theorem 1

If \(\tau(\mathcal H)=s\) and \(s\ge14\), Proposition 3 yields
\[
s\le \frac m4+\eta(s+1)+\frac12.
\]
Hence
\[
m\ge4s-4\eta(s+1)-2
=c(s+1)-6.
\]
Taking the integer ceiling proves (1).

Every case in this argument is covered, including the possibility that the initial greedy process deletes all edges.

---

## 4. Rounded lower bounds that incorporate \(r\)

The preceding argument is independent of \(r\). It can be combined with local counting and integer greedy bounds.

### 4.1. An integer greedy bound

For fixed \(s\), define
\[
a_s(1)=1,
\qquad
a_s(k)=a_s(k-1)+1+
\left\lceil\frac{a_s(k-1)}{s-1}\right\rceil
\quad(k\ge2).
\tag{18}
\]

Then every intersecting \(s\)-uniform family with transversal number at least \(k\) has at least \(a_s(k)\) edges.

To prove this, let the family have \(m\) edges and fix one edge \(A\). Intersectingness gives
\[
\sum_{x\in A}(d(x)-1)\ge m-1.
\]
Thus some vertex has degree at least
\[
1+\left\lceil\frac{m-1}{s}\right\rceil.
\]
Deleting its incident edges leaves a family with transversal number at least \(k-1\), and with at most
\[
\left\lfloor\frac{(s-1)(m-1)}s\right\rfloor
\]
edges. Induction and rearrangement give exactly (18).

Combine this with Proposition 3 by setting
\[
L_s(k)=
\max\left\{
a_s(k),\,
\left\lceil4k-4K_s\right\rceil
\right\}.
\tag{19}
\]
Thus
\[
\tau(\mathcal F)\ge k
\quad\Longrightarrow\quad
|\mathcal F|\ge L_s(k)
\tag{20}
\]
for every intersecting \(s\)-uniform family \(\mathcal F\).

### 4.2. The ground-set recursion

For the given \(r,s\), define integers
\[
b_{s-1}=1
\]
and, successively for \(t=s-2,\dots,0\),
\[
\boxed{\displaystyle
b_t=
\max\left\{
L_s(s-t),\,
\left\lceil
\frac{r-t}{r-s-t}\,b_{t+1}
\right\rceil
\right\}.}
\tag{21}
\]
Then
\[
\boxed{M(r,s)\ge b_0.}
\tag{22}
\]

Here is the proof. For \(T\subseteq[r]\), let
\[
q(T)=|\{F\in\mathcal H:F\cap T=\varnothing\}|.
\]
If \(|T|=t<s\), the family of edges avoiding \(T\) has transversal number at least \(s-t\); otherwise a cover of that family, together with \(T\), would cover \(\mathcal H\) with fewer than \(s\) vertices. Therefore
\[
q(T)\ge L_s(s-t).
\tag{23}
\]

Also,
\[
\sum_{x\notin T}q(T\cup\{x\})
=(r-s-t)q(T).
\tag{24}
\]
Indeed, each edge avoiding \(T\) also avoids exactly \(r-s-t\) possible choices of \(x\).

Starting from \(q(T)\ge1\) for \(|T|=s-1\), equations (23)–(24) prove inductively that \(q(T)\ge b_t\) whenever \(|T|=t\). Taking \(T=\varnothing\) proves (22).

This is a lower-bound recursion, not a claimed formula for the optimum.

---

## 5. The complementary covering bound and exact boundary

For completeness, the elementary complement reduction is re-proved here.

Because an edge of an intersecting \(s\)-uniform hypergraph is itself a transversal, the condition \(\tau(\mathcal H)=s\) is equivalent to saying that every \((s-1)\)-set avoids at least one edge.

Counting pairs \((T,F)\) with
\[
|T|=s-1,\qquad F\in\mathcal H,\qquad T\cap F=\varnothing
\]
gives
\[
|\mathcal H|\binom{r-s}{s-1}\ge\binom r{s-1}.
\]
Thus
\[
M(r,s)\ge
\left\lceil
\frac{\binom r{s-1}}{\binom{r-s}{s-1}}
\right\rceil.
\tag{25}
\]

When \(r=2s-1\), each \((s-1)\)-set \(T\) has exactly one disjoint \(s\)-set, namely \([r]\setminus T\). Every such \(s\)-set must therefore be an edge. This proves
\[
M(2s-1,s)=\binom{2s-1}{s}.
\]

Conversely, the complete \(s\)-uniform hypergraph on a fixed \(2s-1\)-subset is intersecting and has transversal number \(s\). Padding with isolated vertices gives the general upper bound
\[
M(r,s)\le\binom{2s-1}{s}.
\tag{26}
\]

---

## 6. A projective-plane upper bound

Here is a modest strengthening of the projective-plane construction in the supplied attempt.

### Proposition 4
Suppose \(q=s-1\ge2\) is a prime power. Then
\[
M(r,s)\le q^2-q+4=s^2-3s+6
\qquad
\text{whenever }r\ge q^2+q+1.
\]

#### Proof

Use the projective plane over \(\mathbb F_q\), which has
\[
N=q^2+q+1
\]
points and lines, with \(q+1\) points per line.

Choose distinct points \(P,Q\), and let \(L=PQ\). Delete:

* \(q-1\) lines through \(P\), none equal to \(L\);
* \(q-2\) lines through \(Q\), none equal to \(L\).

Call the deleted set \(\mathcal D\). Then
\[
|\mathcal D|=2q-3.
\]
No point lies on \(q\) deleted lines. For \(q\ge3\), points other than \(P,Q\) lie on at most two deleted lines, while \(P,Q\) lie on at most \(q-1\). For \(q=2\), only one line is deleted.

The remaining lines form an intersecting \((q+1)\)-uniform hypergraph with
\[
N-(2q-3)=q^2-q+4
\]
edges. We show that no \(q\) points cover them.

Let \(T\) be a set of \(q\) points.

**If \(T\) is collinear:** its line has one further point \(R\). Exactly the \(q\) lines through \(R\), other than that line, avoid \(T\). They cannot all belong to \(\mathcal D\), because no \(q\) deleted lines are concurrent.

**If \(T\) is not collinear:** choose a line containing exactly \(k\) points of \(T\), where
\[
2\le k\le q-1.
\]
The lines through those \(k\) points number \(kq+1\). Each of the remaining \(q-k\) points adds at most \(q+1-k\) further lines. Thus the number of lines meeting \(T\) is at most
\[
kq+1+(q-k)(q+1-k)
=q^2+1-(q-k)(k-1).
\]
At least
\[
q+(q-k)(k-1)\ge2q-2
\]
lines avoid \(T\). Since only \(2q-3\) lines were deleted, at least one avoiding line remains.

Therefore no \(q\)-set is a transversal. Any remaining line is a transversal of size \(q+1\), so the covering number is exactly \(q+1=s\). ∎

---

## 7. What remains unresolved

The main progress is the transversal inequality in Proposition 3, giving the coefficient
\[
\frac{168-24\sqrt2}{47}=2.852316478\ldots
\]
in the unrestricted linear lower bound, together with the rounded \(r\)-dependent refinement.

This does **not** determine \(M(r,s)\) generally. In particular, it does not close the gap between linear lower bounds and the quadratic projective-plane upper bounds, nor does it determine the minimum for arbitrary fixed \(r,s\).

The argument uses no computational assertions and no unverified literature citations. The pairing and complement observations reused from the supplied attempt were proved explicitly above; its asserted exact \(s=4\) table is not a premise of this writeup.