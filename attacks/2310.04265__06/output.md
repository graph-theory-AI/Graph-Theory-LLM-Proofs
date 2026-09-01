```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds, with an exponential chi-bound, whenever the ordered matching is noncrossing, with isolated vertices allowed.",
  "would_publish": false,
  "caveats": "The crossing two-edge pattern with edges 13 and 24 is not covered, and no claim of literature priority is made."
}
```

# 1. Statement of the partial result

All graphs below are finite and simple. Containment is understood as induced ordered-subgraph containment, as appropriate for the backedge-graph application.

For edges \(ab\) and \(cd\), with \(a\prec b\) and \(c\prec d\), say that they **cross** if
\[
a\prec c\prec b\prec d
\quad\text{or}\quad
c\prec a\prec d\prec b.
\]
An ordered graph of maximum degree at most \(1\) is a **noncrossing ordered matching** if no two of its edges cross. Isolated vertices are allowed.

## Theorem

Let \(M\) be a noncrossing ordered graph with \(\Delta(M)\le 1\). Then the class of \(M\)-free ordered graphs is \(\chi\)-bounded. In fact, for every such \(M\) there is a constant \(C_M\) such that every \(M\)-free ordered graph \(G\) satisfies
\[
\chi(G)\le C_M^{\omega(G)}.
\]

The proof uses two closure operations for ordered \(\chi\)-binding graphs.

# 2. Two closure operations

For ordered graphs \(A,B\), let \(A\oplus B\) denote their **ordered anticomplete sum**: every vertex of \(A\) precedes every vertex of \(B\), and there are no edges between the two parts.

For an ordered graph \(H\), let \(W(H)\) be obtained by adding vertices \(\ell,r\) such that
\[
\ell\prec V(H)\prec r,
\]
adding the edge \(\ell r\), and adding no edges from \(\{\ell,r\}\) to \(H\). Thus \(W(H)\) wraps \(H\) inside an isolated outer edge.

We prove that \(\chi\)-binding ordered graphs are closed under both operations.

Throughout, bounds are taken for graphs of clique number at most \(w\), and may be assumed nondecreasing in \(w\).

## Lemma 2.1: ordered anticomplete sums

If \(A\) and \(B\) are \(\chi\)-binding ordered graphs, then \(A\oplus B\) is \(\chi\)-binding.

### Proof

Let \(a_w,b_w\) be \(\chi\)-bounds for \(A\)-free and \(B\)-free ordered graphs, respectively, and put \(a=|V(A)|\). Write \(M=A\oplus B\).

We define a bound \(c_w\) recursively. Set \(c_1=1\), and for \(w\ge2\), set
\[
c_w=a_w+b_w+a\,c_{w-1}+1.
\]

Suppose, inductively on \(w\), that \(G\) is \(M\)-free, \(\omega(G)\le w\), and
\[
\chi(G)\ge a_w+b_w+a\,c_{w-1}+2.
\]
Set
\[
p=a_w+1,\qquad q=b_w+a\,c_{w-1}+1.
\]
Since \(\chi(G)\ge p+q\), there are consecutive ordered intervals \(X\prec Y\) with
\[
\chi(G[X])=p,\qquad \chi(G[Y])\ge q.
\]
Indeed, take the shortest initial interval having chromatic number \(p\); adding one vertex changes chromatic number by at most one, and
\[
\chi(G)\le \chi(G[X])+\chi(G[Y]).
\]

Since \(\chi(G[X])>a_w\), the interval \(X\) contains an induced ordered copy \(S\) of \(A\).

Let
\[
D=\{y\in Y:y\text{ has a neighbor in }S\}.
\]
For each \(s\in S\), the graph \(G[N(s)\cap Y]\) is \(M\)-free and has clique number at most \(w-1\). By induction,
\[
\chi(G[N(s)\cap Y])\le c_{w-1}.
\]
Consequently,
\[
\chi(G[D])\le a\,c_{w-1}.
\]
It follows that
\[
\chi(G[Y\setminus D])
 \ge \chi(G[Y])-\chi(G[D])
 \ge b_w+1.
\]
Thus \(Y\setminus D\) contains an induced ordered copy of \(B\). It is anticomplete to \(S\), and all its vertices follow \(S\), producing \(A\oplus B\), a contradiction.

Hence \(\chi(G)\le c_w\). ∎

## Lemma 2.2: bounded chromatic edge-spans

Let \(G\) be an ordered graph such that, for every edge \(xy\), \(x\prec y\),
\[
\chi\bigl(G[\{z:x\prec z\prec y\}]\bigr)\le t.
\]
Then
\[
\chi(G)\le 2(t+1).
\]

### Proof

Partition the order greedily into consecutive intervals
\[
V_1\prec V_2\prec\cdots\prec V_s
\]
such that every nonfinal interval has chromatic number exactly \(t+1\), while the final interval has chromatic number at most \(t+1\). This is done by repeatedly taking the shortest initial segment of chromatic number \(t+1\).

There cannot be an edge from \(V_i\) to \(V_j\) when \(j\ge i+2\). Indeed, its open ordered interval would contain all of \(V_{i+1}\), which has chromatic number \(t+1\), contrary to the hypothesis.

Thus distinct odd-indexed intervals are pairwise anticomplete, and so are distinct even-indexed intervals. The odd intervals can be colored using one palette of \(t+1\) colors and the even intervals with another such palette. Hence
\[
\chi(G)\le 2(t+1).
\]
∎

## Lemma 2.3: wrapping by an isolated edge

If \(H\) is \(\chi\)-binding, then \(W(H)\) is \(\chi\)-binding.

### Proof

Let \(h_w\) be a \(\chi\)-bound for \(H\)-free ordered graphs, and let \(M=W(H)\). Define \(c_1=1\), and for \(w\ge2\), set
\[
c_w=4c_{w-1}+2h_w+2.
\]

Let \(G\) be \(M\)-free with \(\omega(G)\le w\). Fix an edge \(xy\), where \(x\prec y\), and define
\[
I(x,y)=\{z:x\prec z\prec y\},
\]
and
\[
Z=\{z\in I(x,y):zx,zy\notin E(G)\}.
\]
The ordered graph \(G[Z]\) is \(H\)-free: otherwise an induced copy of \(H\) in \(Z\), together with \(x,y\), would induce \(W(H)\). Therefore
\[
\chi(G[Z])\le h_w.
\]

Every vertex of \(I(x,y)\setminus Z\) belongs to \(N(x)\cup N(y)\). Both neighborhood graphs are \(M\)-free and have clique number at most \(w-1\). By induction,
\[
\chi(G[N(x)\cap I(x,y)])\le c_{w-1},
\]
and similarly for \(y\). Consequently,
\[
\chi(G[I(x,y)])\le h_w+2c_{w-1}.
\]

Lemma 2.2, with \(t=h_w+2c_{w-1}\), now gives
\[
\chi(G)\le 2(h_w+2c_{w-1}+1)=c_w.
\]
Thus \(W(H)\) is \(\chi\)-binding. ∎

For \(H=\varnothing\), \(W(H)=K_2\), which is trivially \(\chi\)-binding, since a \(K_2\)-free graph is edgeless.

# 3. Noncrossing ordered matchings

We now prove the theorem by induction on \(|V(M)|\).

Let \(v\) be the first vertex of a nonempty noncrossing ordered matching \(M\).

- If \(v\) is isolated, then
  \[
  M=K_1\oplus (M-v).
  \]
  The smaller matching \(M-v\) is noncrossing, so Lemma 2.1 applies.

- Suppose \(v\) is matched to \(u\). Let \(H\) consist of the vertices strictly between \(v\) and \(u\), and let \(K\) consist of the vertices following \(u\).

  There is no edge between \(H\) and \(K\). Indeed, an edge \(xy\) with
  \[
  v\prec x\prec u\prec y
  \]
  would cross the edge \(vu\). Since \(M\) has maximum degree at most \(1\), neither \(v\) nor \(u\) has any other incident edge. Therefore
  \[
  M=W(H)\oplus K.
  \]
  Both \(H\) and \(K\) are smaller noncrossing ordered matchings. By induction they are \(\chi\)-binding; Lemma 2.3 gives that \(W(H)\) is \(\chi\)-binding, and Lemma 2.1 then gives the result for \(M\).

This covers every noncrossing ordered matching, including arbitrary isolated vertices.

# 4. Quantitative bound

The preceding proof gives explicit recurrences:

- For \(M=A\oplus B\),
  \[
  f_M(1)=1,\qquad
  f_M(w)=f_A(w)+f_B(w)+|V(A)|f_M(w-1)+1.
  \]

- For \(M=W(H)\),
  \[
  f_M(1)=1,\qquad
  f_M(w)=4f_M(w-1)+2f_H(w)+2.
  \]

These recurrences preserve exponential dependence on \(w\). For example, a coarse uniform choice is
\[
f_M(w)\le \left(16\cdot 8^{|V(M)|}\right)^w
\]
for every noncrossing ordered matching \(M\).

For the two noncrossing two-edge patterns, the recurrences give more concrete bounds:

- If \(M\) has edges \(12\) and \(34\), then \(M=K_2\oplus K_2\), and one may take
  \[
  f_M(w)=2^{w+1}-3.
  \]

- If \(M\) has edges \(14\) and \(23\), then \(M=W(K_2)\), and one may take
  \[
  f_M(w)=\frac{7\cdot4^{w-1}-4}{3}.
  \]

# 5. Remaining gap

The smallest matching not covered is the crossing ordered matching
\[
1\prec2\prec3\prec4,\qquad E(M)=\{13,24\}.
\]
It is neither an ordered anticomplete sum of smaller nonempty patterns nor a wrapping \(W(H)\).

For an edge \(xz\) in a graph avoiding this crossing pattern, one can infer that the common antineighbors of \(x,z\) lying between \(x,z\) are anticomplete to the common antineighbors lying after \(z\). However, unlike in Lemma 2.3, this does not bound the chromatic number of the entire open interval between the endpoints of an edge. Thus the edge-span decomposition used above does not extend to this pattern.

Accordingly, the argument proves the conjecture for all noncrossing ordered matchings but leaves crossing matchings, beginning with \(\{13,24\}\), unresolved.