```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A local fractional-cover parameter at most 2 guarantees an abundant element in a specified member, and an explicit construction shows this threshold is sharp.",
  "would_publish": false,
  "caveats": "This does not resolve Frankl's conjecture or improve the general abundance bound; novelty of these partial results is not claimed."
}
```

# A sharp local criterion

I do not obtain a proof or a counterexample to Frankl’s conjecture. The partial result below gives:

- a sufficient condition expressed as a small linear program;
- a special case described by the intersection graph of a generating family;
- explicit examples showing that the sufficient condition has an exact threshold.

All arguments are self-contained.

## 1. A fractional-cover certificate

Let \(\mathcal F\) be a finite union-closed family, and write
\[
m=|\mathcal F|,
\qquad
d(x)=|\{B\in\mathcal F:x\in B\}|.
\]
Call \(x\) **abundant** if \(d(x)\ge m/2\).

For a nonempty \(A\in\mathcal F\), define its family of nonempty traces
\[
\mathcal T_A=\{A\cap B:B\in\mathcal F,\ A\cap B\ne\varnothing\}.
\]
Define the fractional transversal number
\[
\tau_A^*=
\min\left\{
\sum_{a\in A}w_a:
w_a\ge0,\quad
\sum_{a\in T}w_a\ge1\ \text{for every }T\in\mathcal T_A
\right\}.
\]
This minimum exists: assigning weight \(1\) to every element is feasible, and weights greater than \(1\) can be truncated to \(1\).

### Theorem 1
If some nonempty \(A\in\mathcal F\) satisfies \(\tau_A^*\le2\), then an element of \(A\) is abundant.

### Proof

Choose feasible weights of total weight
\[
W=\sum_{a\in A}w_a\le2.
\]
Because \(A\in\mathcal T_A\), we have \(W\ge1\).

Partition \(\mathcal F\) into
\[
\begin{aligned}
\mathcal D&=\{B:B\cap A=\varnothing\},\\
\mathcal C&=\{B:A\subseteq B\},\\
\mathcal R&=\mathcal F\setminus(\mathcal D\cup\mathcal C).
\end{aligned}
\]
Put \(p=|\mathcal D|\), \(q=|\mathcal C|\), and \(t=|\mathcal R|\), so \(m=p+q+t\).

Union-closure gives a map
\[
\mathcal D\longrightarrow\mathcal C,\qquad B\longmapsto A\cup B.
\]
It is injective, since \(B\cap A=\varnothing\). Hence \(q\ge p\).

Every member of \(\mathcal R\) has a nonempty trace and therefore trace weight at least \(1\). Consequently,
\[
\begin{aligned}
\sum_{a\in A}w_a d(a)
&=\sum_{B\in\mathcal F}\sum_{a\in A\cap B}w_a\\
&\ge Wq+t\\
&=\frac{Wm}{2}
  +\frac W2(q-p)
  +\left(1-\frac W2\right)t\\
&\ge\frac{Wm}{2}.
\end{aligned}
\]
A weighted average of the frequencies is thus at least \(m/2\), so some positively weighted element is abundant. \(\square\)

### Equality when \(\tau_A^*<2\)

The proof also gives a rigidity statement. If \(\tau_A^*<2\) and no element of \(A\) occurs in more than half the members, then
\[
q=p,\qquad t=0.
\]
The injection above is therefore a bijection, and
\[
\mathcal F
=
\mathcal D\ \cup\ \{A\cup B:B\in\mathcal D\}.
\]
Thus \(A\) is a free binary block: every member either avoids \(A\) or contains all of \(A\), and every element of \(A\) occurs in exactly half the family.

### Two immediate consequences

1. **Large-trace condition.** If every \(B\in\mathcal F\) satisfies
   \[
   B\cap A=\varnothing
   \quad\text{or}\quad
   |B\cap A|\ge |A|/2,
   \]
   then \(A\) contains an abundant element. Use \(w_a=2/|A|\).

2. **A one- or two-element member suffices.** If \(1\le |A|\le2\), assign weight \(1\) to every element of \(A\).

## 2. A graph-theoretic special case

Suppose \(\mathcal H\) is a family of nonempty sets and
\[
\mathcal F=\left\{\bigcup\mathcal S:\mathcal S\subseteq\mathcal H\right\}.
\]
Define the **generator intersection graph** to have vertex set \(\mathcal H\), with distinct generators adjacent when they intersect.

### Corollary 2
If this graph has a vertex of degree at most two, then Frankl’s conjecture holds for \(\mathcal F\).

### Proof

Let \(A\in\mathcal H\) meet at most two other generators.

- If it meets none, choose any \(a\in A\).
- If it meets one generator \(H_1\), choose \(a\in A\cap H_1\).
- If it meets two generators \(H_1,H_2\), choose
  \[
  a\in A\cap H_1,\qquad b\in A\cap H_2.
  \]

The resulting set of at most two chosen points meets every generator that intersects \(A\), including \(A\) itself.

Any union of generators that intersects \(A\) contains an intersecting generator, and hence contains a chosen point. Giving the chosen points weight \(1\) therefore proves \(\tau_A^*\le2\). Apply Theorem 1. \(\square\)

In particular, this covers generating families whose intersection graph is a forest or, more generally, is \(2\)-degenerate.

The covering constraints can be checked on the generators rather than on the potentially exponentially larger union closure.

## 3. The threshold \(2\) is sharp for the local conclusion

Theorem 1 cannot be strengthened by replacing \(2\) with any larger constant while still guaranteeing an abundant element **inside the specified member \(A\)**.

### Theorem 3
For every integer \(k\ge1\), there are a finite union-closed family \(\mathcal F_k\) and a member \(A\in\mathcal F_k\) such that
\[
|A|=2k+1,\qquad
\tau_A^*=2+\frac1k,
\]
but
\[
d(a)=\frac{|\mathcal F_k|-1}{2}
\qquad\text{for every }a\in A.
\]

Moreover, every nonempty trace on \(A\) has size at least \(k\). Thus even allowing nonempty intersections to fall just one-half below \(|A|/2\) can invalidate the local conclusion.

### Construction

Take a set \(A\) of size \(2k+1\), and let
\[
\mathcal B=\binom{A}{k+1},\qquad r=|\mathcal B|.
\]
For each \(B\in\mathcal B\), introduce a distinct new marker \(z_B\). Put
\[
M=\{z_B:B\in\mathcal B\},\qquad V_B=M\setminus\{z_B\}.
\]

On \(A\), define
\[
\mathcal L_B=\{\varnothing,B,A\}\cup\binom{B}{k}
\]
and
\[
\mathcal T=\{\varnothing\}\cup\{S\subseteq A:|S|\ge k\}.
\]
Now set
\[
\boxed{
\mathcal F_k=
\{\varnothing,A\}
\;\cup\!
\bigcup_{B\in\mathcal B}
\{V_B\cup S:S\in\mathcal L_B\}
\;\cup\;
\{M\cup S:S\in\mathcal T\}.
}
\]

### Union-closure

Each \(\mathcal L_B\) is union-closed: two distinct \(k\)-subsets of the \((k+1)\)-set \(B\) have union \(B\). The family \(\mathcal T\) is also union-closed and contains every \(\mathcal L_B\).

There are three remaining types of unions to check.

- Two sets from the same \(V_B\)-layer remain in that layer.
- For distinct \(B,C\),
  \[
  V_B\cup V_C=M.
  \]
  Their union therefore lies in the \(M\)-layer, since its \(A\)-trace belongs to \(\mathcal T\).
- Union with the bottom member \(A\) replaces the trace by \(A\), which is allowed in every layer. Union with \(\varnothing\) changes nothing.

Unions involving the \(M\)-layer stay in that layer. This covers all cases.

### The fractional transversal number

Every nonempty trace on \(A\) has size at least \(k\). Moreover, every \(k\)-subset \(S\subseteq A\) occurs as a trace: choose \(B\in\binom{A}{k+1}\) containing \(S\), and use \(V_B\cup S\).

Weights \(w_a=1/k\) therefore give
\[
\tau_A^*\le\frac{2k+1}{k}.
\]
Conversely, summing the covering constraints over all \(k\)-subsets gives
\[
\binom{2k}{k-1}\sum_{a\in A}w_a
\ge
\binom{2k+1}{k}.
\]
Hence
\[
\tau_A^*=\frac{2k+1}{k}=2+\frac1k.
\]

### Exact frequencies

Write
\[
s=\binom{2k}{k},\qquad
u=\binom{2k}{k-1},
\]
and put
\[
Q=|\mathcal T|
  =1+\sum_{j=k}^{2k+1}\binom{2k+1}{j},
\qquad
D=\sum_{j=k-1}^{2k}\binom{2k}{j}.
\]
The layers in the construction are disjoint, and \(|\mathcal L_B|=k+4\). Thus
\[
m:=|\mathcal F_k|=2+(k+4)r+Q.
\]

Fix \(a\in A\). Exactly \(s\) members of \(\mathcal B\) contain \(a\). In such a layer, \(a\) occurs in \(k+2\) members of \(\mathcal L_B\); in every other layer, it occurs only in the trace \(A\). It occurs in \(D\) members of the top layer. Therefore
\[
d(a)=1+r+(k+1)s+D.
\]

Pascal’s identity gives
\[
r=s+u,\qquad
(k+1)u=ks,\qquad
2D-Q=u-1.
\]
Consequently,
\[
\begin{aligned}
2d(a)-m
&=2(k+1)s-(k+2)r+(2D-Q)\\
&=ks-(k+1)u-1\\
&=-1.
\end{aligned}
\]
This proves the claimed frequency formula. \(\square\)

These families are **not counterexamples to Frankl’s conjecture**. A marker \(z_B\) is absent only from the two bottom sets and its own \(k+4\)-set layer, so
\[
d(z_B)=m-k-6>\frac m2.
\]
For \(k=1\), the construction has \(25\) sets on six elements: the three selected elements occur \(12\) times each, while the three markers occur \(18\) times each.

Since \(2+1/k\) approaches \(2\), no constant larger than \(2\) can replace the threshold in Theorem 1.

## 4. Scope and remaining gap

The criterion is sufficient, not necessary. In fact, it can fail for **every** nonempty member of a family that easily satisfies Frankl’s conjecture.

For example, take
\[
\mathcal G=\{\varnothing\}\cup\{S\subseteq[7]:|S|\ge3\}.
\]
This is union-closed, has \(100\) members, and every element occurs \(57\) times.

For a member \(A\) of size \(a\), its nonempty traces are exactly the subsets of \(A\) of size at least
\[
q_a=\max(1,a-4).
\]
The same averaging argument used above gives
\[
\tau_A^*=\frac{a}{q_a}.
\]
For \(a=3,4,5,6,7\), these values are respectively
\[
3,\quad4,\quad5,\quad3,\quad\frac73,
\]
all greater than \(2\).

Thus one cannot finish the conjecture merely by asserting that every union-closed family has a member certified by Theorem 1: that assertion is false. The partial results establish a genuine special case and a sharp limitation of this local method, but leave the unrestricted conjecture unresolved.