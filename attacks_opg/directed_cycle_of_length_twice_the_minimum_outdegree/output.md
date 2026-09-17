```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the self-contained bound min(2k,k+4) for the length of a directed path, establishing the conjecture for k≤4.",
  "would_publish": false,
  "caveats": "The general case remains unresolved here; no novelty claim or independent verification of the supplied literature is made."
}
```

## Statement of the partial result

All graphs below are finite and nonempty. An **oriented graph** has no loops or antiparallel pair of arcs. Paths and cycles are simple, and their lengths count arcs.

I prove:

**Theorem.** Every oriented graph of minimum outdegree at least \(k\) contains a directed path of length at least
\[
\boxed{\min\{2k,k+4\}.}
\]

Consequently, the conjecture holds for \(k\le 4\). The theorem also gives lengths \(9\) and \(10\) when \(k=5\) and \(k=6\), respectively.

This is an additive bound, not an improvement on the asymptotic \(3k/2\) bound reported in the prompt. I do not claim that these small-degree cases or this bound are new.

## 1. Two consequences of a short longest path

Fix an oriented graph \(D\) with minimum outdegree at least \(k\), and let \(L\) be its maximum directed-path length. Throughout this section assume
\[
L<2k.
\]

### Lemma 1: A longest path cannot close into a cycle

There is no directed cycle of length \(L+1\).

**Proof.** Suppose \(C\) were such a cycle. If a vertex \(u\in C\) had an out-neighbor outside \(C\), traversing all of \(C\), starting at the successor of \(u\) and ending at \(u\), and then taking that outgoing arc would give a path of length \(L+1\).

Thus \(V(C)\) is out-closed. Since \(D[C]\) is oriented,
\[
k(L+1)
\le \sum_{v\in C}d^+(v)
=|E(D[C])|
\le \binom{L+1}{2}.
\]
This implies \(L\ge 2k\), a contradiction. \(\square\)

### Lemma 2: A cycle as long as a longest path forces a stronger bound

If \(D\) contains a directed cycle of length \(L\), then
\[
\boxed{2L\ge 3k+3.}
\]

**Proof.** Let \(C\) be a directed cycle with \(L\) vertices. Write \(s(u)\) for the successor of \(u\) on \(C\), and put
\[
A=\{u\in V(C):N^+(u)\setminus V(C)\ne\varnothing\},
\qquad
X=N^+(V(C))\setminus V(C).
\]

For every \(x\in X\), choose \(u\in C\) with \(u\to x\). Traversing \(C\) from \(s(u)\) to \(u\), and then taking \(u\to x\), gives a longest path. Therefore
\[
N^+(x)\subseteq V(C). \tag{1}
\]

We claim that
\[
N^+(x)\cap s(A)=\varnothing
\qquad\text{for every }x\in X. \tag{2}
\]
Indeed, suppose \(x\to s(u)\) with \(u\in A\), and choose \(z\in X\) with \(u\to z\). If \(x\ne z\), then
\[
x,s(u),\ldots,u,z
\]
is a path of length \(L+1\). If \(x=z\), the same arcs form a cycle of length \(L+1\), contrary to Lemma 1. This proves (2).

The set \(A\) is nonempty: otherwise \(C\) would be out-closed, forcing \(L\ge2k+1\) by the same arc count as above. It is proper, since \(A=V(C)\) would make (1)–(2) give \(d^+(x)=0\) for every \(x\in X\).

Set
\[
a=|A|,\qquad B=V(C)\setminus A,\qquad b=|B|=L-a.
\]
Because \(A\) is a nonempty proper subset of a cyclic order, there is a vertex
\[
u\in A\setminus s(A).
\]
Choose \(z\in X\) with \(u\to z\). By (1)–(2), every out-neighbor of \(z\) belongs to \(V(C)\setminus s(A)\). Moreover, \(z\not\to u\), since \(D\) is oriented. Hence
\[
k\le d^+(z)\le L-a-1,
\]
so
\[
a\le L-k-1. \tag{3}
\]

Every vertex of \(B\) has all its out-neighbors in \(C\). Also, the cycle \(C\) has at least one arc from \(A\) to \(B\), so there are at most \(ab-1\) arcs from \(B\) to \(A\). Consequently,
\[
kb
\le |E(D[B])|+|E(B,A)|
\le \binom b2+ab-1.
\]
In particular,
\[
k<\frac{b-1}{2}+a=\frac{L+a-1}{2}.
\]
Since the quantities are integral,
\[
a\ge 2k-L+2. \tag{4}
\]
Combining (3) and (4) gives
\[
2k-L+2\le L-k-1,
\]
which is exactly \(2L\ge3k+3\). \(\square\)

## 2. Excluding the two shortest remaining possibilities

We now prove the theorem. The case \(k=0\) is immediate, so assume \(k\ge1\). If \(L\ge2k\), there is nothing to prove. Thus assume
\[
L<2k.
\]

Let
\[
P=(p_0,p_1,\ldots,p_L)
\]
be a longest directed path. Every out-neighbor of \(p_L\) lies on \(P\). Lemma 1 excludes \(p_L\to p_0\), and orientation excludes \(p_L\to p_{L-1}\). Therefore
\[
N^+(p_L)\subseteq\{p_1,\ldots,p_{L-2}\},
\]
giving
\[
L\ge k+2. \tag{5}
\]

### Excluding \(L=k+2\)

If \(L=k+2\), equality of the available number of vertices forces
\[
N^+(p_L)=\{p_1,\ldots,p_k\}.
\]
In particular, \(p_L\to p_1\), so \(p_1,\ldots,p_L\) form a cycle of length \(L\).

Lemma 2 then gives
\[
2(k+2)\ge3k+3,
\]
or \(k\le1\). But \(k+2=L<2k\) implies \(k\ge3\), a contradiction. Thus
\[
L\ge k+3. \tag{6}
\]

### Excluding \(L=k+3\)

Suppose now that \(L=k+3\). Since \(L<2k\), we have \(k\ge4\).

Lemma 2 shows that there is no cycle of length \(L\), because such a cycle would imply
\[
2k+6\ge3k+3,
\]
or \(k\le3\).

It follows that **every** longest path
\[
Q=(q_0,q_1,\ldots,q_L)
\]
has the exact endpoint neighborhood
\[
\boxed{N^+(q_L)=\{q_2,\ldots,q_{L-2}\}.} \tag{7}
\]
Indeed, an arc to \(q_0\) would create a cycle of length \(L+1\), an arc to \(q_1\) would create a cycle of length \(L\), and an arc to \(q_{L-1}\) is prohibited by orientation. The remaining set has exactly \(L-3=k\) vertices.

Write one longest path as
\[
(p_0,p_1,b_1,\ldots,b_k,r,x).
\]
By (7),
\[
N^+(x)=B:=\{b_1,\ldots,b_k\}.
\]

Let
\[
S=B\cup\{r,x\}.
\]
The vertex \(b_k\) receives arcs from both \(b_{k-1}\) and \(x\). As \(|S|=k+2\), it has at most \(k-1\) out-neighbors in \(S\). Hence there is an arc
\[
b_k\to y,\qquad y\notin S.
\]
The sequence
\[
Q=(r,x,b_1,\ldots,b_k,y)
\]
is a path of length \(L-1\). There are two cases.

#### Case 1: \(y\) has an out-neighbor \(z\notin V(Q)\)

Appending \(z\) to \(Q\) gives a longest path. Equation (7) yields
\[
N^+(z)=B.
\]
Now consider
\[
R=(y,z,b_3,\ldots,b_k,r,x,b_1,b_2).
\]
Every indicated arc exists, all vertices are distinct, and \(R\) has length \(L\).

In \(R\), the vertex \(x\) occupies position \(L-2=k+1\). Applying (7) to its endpoint \(b_2\) forces \(b_2\to x\). But \(x\to b_2\), a contradiction.

#### Case 2: \(N^+(y)\subseteq V(Q)\)

The arc \(y\to r\) would close \(Q\) into a cycle of length \(L\), which is impossible. Also, \(y\not\to b_k\), because \(b_k\to y\). The degree condition therefore forces
\[
N^+(y)=\{x,b_1,\ldots,b_{k-1}\}. \tag{8}
\]

The vertex \(b_{k-1}\) receives arcs from the three distinct vertices
\[
x,\quad y,\quad b_{k-2}.
\]
It consequently has at most \(k-1\) out-neighbors in \(V(Q)\), which has \(k+3\) vertices. Choose
\[
b_{k-1}\to z,\qquad z\notin V(Q).
\]
Then
\[
R=(r,x,b_k,y,b_1,\ldots,b_{k-1},z)
\]
is a longest path. Equation (7), applied to \(R\), gives \(z\to b_k\).

Using this arc and (8), we obtain the directed cycle
\[
x,b_1,\ldots,b_{k-1},z,b_k,y,x.
\]
It has \(k+3=L\) vertices, again a contradiction.

Both cases are impossible. Thus \(L\ne k+3\).

Together with (5)–(6), this proves that whenever \(L<2k\), necessarily
\[
L\ge k+4.
\]
Equivalently,
\[
L\ge\min\{2k,k+4\},
\]
completing the proof. \(\square\)

## 3. Consequences and the remaining gap

For \(0\le k\le4\),
\[
\min\{2k,k+4\}=2k,
\]
so the conjecture is established in those cases.

The target \(2k\) is sharp: on the vertices \(\mathbb Z/(2k+1)\mathbb Z\), orient \(i\to i+j\) for \(1\le j\le k\). This regular tournament has minimum outdegree \(k\), and its order prevents a path longer than \(2k\).

The first degree not settled by the argument is \(k=5\): it guarantees length \(9\), rather than \(10\). The proof’s limitation is precise:

- At \(k=5,L=9\), Lemma 2 permits an \(L\)-cycle, since \(2L=3k+3\).
- More generally, at \(L=k+4\), even excluding cycles of lengths \(L\) and \(L+1\) leaves \(k+1\) possible internal out-neighbors for a longest-path endpoint. The exact neighborhood identity (7), essential to both reroutings, is no longer forced.

No argument above excludes those configurations, and no counterexample to the full conjecture is constructed.