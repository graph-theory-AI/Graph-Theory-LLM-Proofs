```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Both bounds hold under explicit partition/codegree conditions, and direct proofs verify the unrestricted cases n ≤ 3 and n ≤ 4, respectively.",
  "would_publish": false,
  "caveats": "Neither full conjecture is settled; no improvement to the best unrestricted asymptotic bounds or literature novelty is claimed."
}
```

# 1. Results and scope

Write
\[
t_4(n)=\frac12n^2(5n-3),
\qquad
t_5(n)=n^2(n-1).
\]

I prove three partial results:

1. A comparison inequality for the first conjecture relative to its cyclic three-part construction. In particular, the conjecture holds when a balanced three-partition has **no reverse-cyclic edges**, even if edges within the parts are allowed. A quantitative loss term in this result is sharp.
2. A comparison inequality for the second conjecture. In particular, the conjecture holds if there is a balanced bipartition for which every pair has at most \(n/3\) neighbors within its own part.
3. Elementary unrestricted verifications for \(3n\le 9\) in the first conjecture and \(2n\le 8\) in the second.

The arguments are independent of the previous attempt’s one-vertex extension theorem. The small-order starting bounds used below are proved again.

## Reference constructions

For disjoint \(A,B,C\), each of size \(n\), let \(\mathcal T_n\) contain all triples of types
\[
ABC,\qquad AAB,\qquad BBC,\qquad CCA.
\]
Then
\[
e(\mathcal T_n)=n^3+3n\binom n2=t_4(n).
\]

It is \(K_4^{(3)}\)-free. A four-set with three vertices in one part contains an absent monochromatic triple. For distributions \(2+2\) and \(2+1+1\), at least one triple has the omitted orientation between the relevant parts.

For disjoint \(A,B\), each of size \(n\), let \(\mathcal B_n\) contain all triples meeting both parts. Then
\[
e(\mathcal B_n)=2n\binom n2=t_5(n).
\]
It is \(K_5^{(3)}\)-free because every five vertices have three in one part.

# 2. A local comparison theorem for \(K_4^{(3)}\)

Fix a balanced partition \(V(H)=A\cup B\cup C\), and use the cyclic orientation
\[
A\longrightarrow B\longrightarrow C\longrightarrow A.
\]

Let
\[
\mathcal P=E(H)\setminus E(\mathcal T_n)
\]
be the added triples, and divide the missing template triples into
\[
\begin{aligned}
\mathcal D_0&=\{f\in E(\mathcal T_n)\setminus E(H):f\text{ has type }ABC\},\\
\mathcal D_1&=\{f\in E(\mathcal T_n)\setminus E(H):
 f\text{ has type }AAB,BBC,\text{ or }CCA\}.
\end{aligned}
\]
Put \(d_i=|\mathcal D_i|\).

For a pair \(uv\), define
\[
d_{\mathcal P}(uv)=|\{f\in\mathcal P:\{u,v\}\subseteq f\}|.
\]
Let
\[
\mu=\max_{\substack{u,v\text{ in}\\\text{the same part}}}d_{\mathcal P}(uv),
\qquad
\lambda=\max_{\substack{u,v\text{ in}\\\text{different parts}}}d_{\mathcal P}(uv),
\]
with an empty maximum interpreted as zero.

**Proposition 1.** If \(H\) is \(K_4^{(3)}\)-free, then
\[
\boxed{
e(H)\le t_4(n)
-\left(1-\frac{3\lambda}{n}\right)d_0
-\left(1-\frac{\mu}{n}\right)d_1.
}
\tag{1}
\]
Consequently, the first conjectured bound holds whenever
\[
\mu\le n,\qquad 3\lambda\le n.
\tag{2}
\]

### Proof

Every added triple has one of the types
\[
AAA,\ BBB,\ CCC,\ AAC,\ ABB,\ BCC.
\]

For every \(f\in\mathcal P\), there are exactly \(n\) four-sets \(Q\supset f\) in which \(f\) is the only triple outside the template:

- If \(f\subseteq A\), choose the fourth vertex in \(B\).
- If \(f\) has type \(AAC\), choose the fourth vertex in \(B\).
- Use the cyclic analogues for the other types.

Call these the witnesses of \(f\). Since \(f\in E(H)\) and \(H\) is \(K_4^{(3)}\)-free, every witness contains a member of \(\mathcal D_0\cup\mathcal D_1\).

We count how many witnesses a missing template triple can meet.

If \(g=\{a,a',b\}\in\mathcal D_1\), of type \(AAB\), then a witness containing \(g\) has its added triple containing \(\{a,a'\}\). Thus \(g\) lies in exactly
\[
d_{\mathcal P}(aa')
\]
witnesses. The same holds cyclically.

If \(g=\{a,b,c\}\in\mathcal D_0\), then its witnesses are obtained by adding a second vertex in one of the three parts. Their number is
\[
d_{\mathcal P}(ab)+d_{\mathcal P}(bc)+d_{\mathcal P}(ca).
\]

Every witness has a unique triple outside the template, so there is no ambiguity in this counting. Covering all \(n|\mathcal P|\) witnesses gives
\[
n|\mathcal P|
\le
\sum_{g\in\mathcal D_1}d_{\mathcal P}(\text{within-part pair of }g)
+
\sum_{\{a,b,c\}\in\mathcal D_0}
\bigl(d_{\mathcal P}(ab)+d_{\mathcal P}(bc)+d_{\mathcal P}(ca)\bigr).
\]
Hence
\[
n|\mathcal P|\le \mu d_1+3\lambda d_0.
\]
Substitute this into
\[
e(H)=t_4(n)+|\mathcal P|-d_0-d_1
\]
to obtain (1). \(\square\)

## 2.1. A sharp special case allowing monochromatic edges

Call the types \(AAC,ABB,BCC\) **reverse-cyclic**.

**Corollary 2.** Suppose \(n\ge2\), \(H\) is \(K_4^{(3)}\)-free, and it has a balanced partition \(A,B,C\) with no reverse-cyclic edges. Then
\[
\boxed{
e(H)\le t_4(n)-d_0-\frac{2}{n}d_1\le t_4(n).
}
\tag{3}
\]
Equality in the conjectured bound forces \(H=\mathcal T_n\) for this partition.

**Proof.** All added triples are monochromatic. Therefore
\[
\lambda=0,\qquad \mu\le n-2.
\]
Apply Proposition 1. If \(e(H)=t_4(n)\), then (3) forces \(d_0=d_1=0\), and the witness inequality then forces \(\mathcal P=\varnothing\). \(\square\)

This is not merely the case \(H\subseteq\mathcal T_n\): arbitrary monochromatic edges are permitted, subject to \(K_4^{(3)}\)-freeness.

### Sharpness of the coefficient \(2/n\)

For \(n\ge3\), choose distinct \(a_1,a_2\in A\). Starting from \(\mathcal T_n\),

- delete all \(n\) triples \(a_1a_2b\), \(b\in B\);
- add all \(n-2\) triples \(a_1a_2a\), \(a\in A\setminus\{a_1,a_2\}\).

The resulting hypergraph is \(K_4^{(3)}\)-free. Any newly created \(K_4^{(3)}\) would contain an added triple \(a_1a_2a\). Its fourth vertex cannot lie:

- in \(A\), because some monochromatic triple not containing \(a_1a_2\) is absent;
- in \(B\), because \(a_1a_2b\) was deleted;
- in \(C\), because the required reverse-cyclic triples are absent.

Here \(d_0=0,d_1=n\), and
\[
e(H)=t_4(n)-2.
\]
Thus equality holds in (3), proving that its coefficient \(2/n\) cannot be increased uniformly.

# 3. A local comparison theorem for \(K_5^{(3)}\)

Fix a balanced bipartition \(V(H)=A\cup B\). Let
\[
\mathcal P_A=E(H)\cap\binom A3,\qquad
\mathcal P_B=E(H)\cap\binom B3
\]
be the monochromatic edges. Let \(\mathcal D_{21}\) and \(\mathcal D_{12}\) be the missing crossing triples of types \(AAB\) and \(ABB\), respectively, and write
\[
d_{21}=|\mathcal D_{21}|,\qquad d_{12}=|\mathcal D_{12}|.
\]

Define the internal maximum codegrees
\[
\Delta_A=\max_{\{a,a'\}\in\binom A2}d_{\mathcal P_A}(aa'),
\qquad
\Delta_B=\max_{\{b,b'\}\in\binom B2}d_{\mathcal P_B}(bb').
\]

**Proposition 3.** If \(n\ge2\) and \(H\) is \(K_5^{(3)}\)-free, then
\[
\boxed{
\begin{aligned}
e(H)\le t_5(n)
&-\left(1-\frac{2\Delta_A+\Delta_B}{n}\right)d_{21}\\
&-\left(1-\frac{\Delta_A+2\Delta_B}{n}\right)d_{12}.
\end{aligned}
}
\tag{4}
\]
In particular, the second conjectured bound holds if
\[
2\Delta_A+\Delta_B\le n,
\qquad
\Delta_A+2\Delta_B\le n.
\tag{5}
\]
A simpler sufficient condition is
\[
\max(\Delta_A,\Delta_B)\le \frac n3.
\tag{6}
\]

### Proof

For every \(f\in\mathcal P_A\) and every pair \(R\in\binom B2\), the five-set \(f\cup R\) has exactly one monochromatic triple, namely \(f\). Therefore it contains a missing crossing triple. The analogous statement holds with \(A,B\) interchanged.

There are
\[
\binom n2\bigl(|\mathcal P_A|+|\mathcal P_B|\bigr)
\]
such witnesses.

Consider a missing crossing triple \(g=\{a,a',b\}\in\mathcal D_{21}\).

- Witnesses arising from \(\mathcal P_A\) are counted by
  \[
  (n-1)d_{\mathcal P_A}(aa'):
  \]
  choose a monochromatic edge containing \(aa'\), then the other vertex of its opposite-side pair.
- Witnesses arising from \(\mathcal P_B\) are counted by
  \[
  \deg_{\mathcal P_B}(b).
  \]

Moreover,
\[
2\deg_{\mathcal P_B}(b)
=\sum_{b'\ne b}d_{\mathcal P_B}(bb')
\le(n-1)\Delta_B.
\]
Thus \(g\) belongs to at most
\[
(n-1)\left(\Delta_A+\frac{\Delta_B}{2}\right)
\]
witnesses.

Similarly, each member of \(\mathcal D_{12}\) belongs to at most
\[
(n-1)\left(\Delta_B+\frac{\Delta_A}{2}\right)
\]
witnesses. Covering all witnesses gives
\[
\begin{aligned}
\binom n2\bigl(|\mathcal P_A|+|\mathcal P_B|\bigr)
\le (n-1)\biggl[
&\left(\Delta_A+\frac{\Delta_B}{2}\right)d_{21}\\
+&\left(\Delta_B+\frac{\Delta_A}{2}\right)d_{12}
\biggr].
\end{aligned}
\]
After division,
\[
|\mathcal P_A|+|\mathcal P_B|
\le
\frac{2\Delta_A+\Delta_B}{n}d_{21}
+
\frac{\Delta_A+2\Delta_B}{n}d_{12}.
\]
Now use
\[
e(H)=t_5(n)+|\mathcal P_A|+|\mathcal P_B|-d_{21}-d_{12}.
\]
This proves (4). \(\square\)

### Quantitative consequence

If
\[
\max(\Delta_A,\Delta_B)\le (1-\varepsilon)\frac n3
\qquad(0<\varepsilon\le1),
\]
then
\[
e(H)\le t_5(n)-\varepsilon(d_{21}+d_{12}).
\tag{7}
\]
In particular, equality in the conjectured edge bound forces \(H=\mathcal B_n\) for that partition.

# 4. Unrestricted small cases

These checks use only complements and deletion counting.

For a 3-graph \(H\), let
\[
F=\binom{V(H)}3\setminus E(H).
\]
Then \(H\) is \(K_t^{(3)}\)-free precisely when every \(t\)-set contains an edge of \(F\).

If \(F\) has \(N\) vertices and \(m\) edges, then
\[
\sum_{v\in V(F)} e(F-v)=(N-3)m.
\tag{8}
\]
Consequently, a lower bound \(L\) on the number of edges in every qualifying \((N-1)\)-vertex system gives
\[
m\ge \left\lceil\frac{NL}{N-3}\right\rceil.
\tag{9}
\]

## 4.1. First conjecture: \(n\le3\)

Here every four-set must contain an edge of \(F\).

On five vertices, there are five four-sets, and each triple lies in two of them. Hence \(e(F)\ge3\). By (9), on six vertices,
\[
e(F)\ge6.
\]

We need the following equality information.

**Lemma 4.** A six-vertex system \(F\) with six edges meeting every four-set is 3-regular and has maximum codegree at most two.

**Proof.** Every deletion has at least three edges, so every vertex has degree at most three. The degree sum is \(18\), forcing every degree to equal three.

Suppose \(d_F(uv)=3\). All edges containing \(u\) then also contain \(v\). Let \(W=V(F)\setminus\{u,v\}\). For each \(S\in\binom W3\), the four-set \(S\cup\{u\}\) must contain an edge, and that edge can only be \(S\). Thus all four triples on \(W\) are edges. Together with the three edges containing \(uv\), this gives at least seven edges, a contradiction. \(\square\)

On seven vertices, (9) initially gives \(e(F)\ge11\). Suppose equality holds. Every degree is at most five, and the degree sum is \(33\), so the degree sequence is either
\[
(5,5,5,5,5,5,3)
\quad\text{or}\quad
(5,5,5,5,5,4,4).
\tag{10}
\]

For every degree-five vertex \(v\), \(F-v\) has six edges and is 3-regular by Lemma 4. Therefore, for \(u\ne v\),
\[
d_F(uv)=\deg_F(u)-3.
\tag{11}
\]

In the first case of (10), the degree-three vertex has codegree zero with every other vertex, impossible.

In the second case, let \(u,w\) be the two degree-four vertices. Equation (11) gives codegree one between \(u\) and each of the five degree-five vertices. Hence
\[
d_F(uw)=2\deg_F(u)-5=3.
\]
Only three degree-five vertices occur as third vertices in these three edges. Choose a degree-five vertex \(v\) outside them. Then \(F-v\) still has codegree three at \(uw\), contradicting Lemma 4.

Thus every seven-vertex system has at least twelve edges. Repeated application of (9) now gives
\[
e(F)\ge20\quad(N=8),\qquad
e(F)\ge30\quad(N=9).
\]
Consequently,
\[
e(H)\le\binom93-30=54=t_4(3).
\]
The six-vertex bound is
\[
e(H)\le\binom63-6=14=t_4(2),
\]
and \(n=1\) is immediate. The constructions \(\mathcal T_n\) attain these bounds.

## 4.2. Second conjecture: \(n\le4\)

Now every five-set must contain an edge of \(F\).

On six vertices, at least two edges are necessary. If there are exactly two, they must be disjoint: otherwise a vertex in their intersection could be deleted, leaving an uncovered five-set. Thus every two-edge extremal system on six vertices is 1-regular.

On seven vertices, (9) gives \(e(F)\ge4\). Suppose \(e(F)=4\). Every degree is at most two, and the degree sum is twelve. The degree sequence is therefore either
\[
(2,2,2,2,2,2,0)
\quad\text{or}\quad
(2,2,2,2,2,1,1).
\tag{12}
\]

For any degree-two vertex \(v\), the deletion \(F-v\) consists of two disjoint triples. Hence
\[
d_F(uv)=\deg_F(u)-1
\qquad(u\ne v).
\tag{13}
\]

The first case of (12) gives a negative codegree in (13), impossible.

In the second case, a degree-one vertex has codegree zero with every degree-two vertex. Its unique edge would therefore have to lie entirely among the two degree-one vertices, also impossible.

Thus every seven-vertex system has at least five edges. On eight vertices, (9) yields
\[
e(F)\ge\frac{8\cdot5}{5}=8,
\]
and consequently
\[
e(H)\le\binom83-8=48=t_5(4).
\]
The six-vertex bound is \(20-2=18=t_5(3)\); \(n=1,2\) are immediate. Again, \(\mathcal B_n\) attains all these bounds.

# 5. The remaining gap

The comparison inequalities do not supply the required partitions or control all violations of their codegree conditions.

The second condition is genuinely restrictive, even among familiar \(K_5^{(3)}\)-free examples. Consider the complete crossing 3-graph with parts of sizes \(n-1,n+1\), where \(n\ge5\). In any balanced repartition, some new part contains vertices from both original parts. A pair chosen from different original parts has all the other \(n-2\) vertices of that new part as internal neighbors. Thus one of \(\Delta_A,\Delta_B\) is at least \(n-2\), violating (5). Nevertheless, this hypergraph has only
\[
(n^2-1)(n-1)=t_5(n)-(n-1)
\]
edges.

So one cannot finish the second conjecture merely by asserting that every \(K_5^{(3)}\)-free hypergraph admits a partition satisfying Proposition 3. Likewise, Proposition 1 leaves high-codegree reverse-cyclic configurations untreated.

The established progress is therefore limited to the stated restricted classes, the sharp loss term in Corollary 2, and the unrestricted small-order verifications. Neither general Turán conjecture is proved or disproved here.