```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "For every n at least 3, an explicit circulant tournament on 2n+1 vertices is 3-clique-critical, giving unbounded minimal witnesses already for k=3.",
  "would_publish": true,
  "caveats": "The proof is self-contained under the stated definition; literature priority beyond the supplied sources has not been checked."
}
```

# Statement

Write \(\overrightarrow{\omega}(T)\) for the minimum, over all linear orders \(\prec\) of \(V(T)\), of the clique number of the corresponding backedge graph \(T^\prec\).

The proposed function \(\ell\) does not exist. In fact, there are \(3\)-\(\overrightarrow{\omega}\)-critical tournaments of arbitrarily large order.

More precisely:

> **Theorem.** For every integer \(n\ge 3\), there is a tournament \(T_n\) on \(2n+1\) vertices such that
> \[
> \overrightarrow{\omega}(T_n)=3,
> \]
> while every proper subtournament \(A\subsetneq T_n\) satisfies
> \[
> \overrightarrow{\omega}(A)\le 2.
> \]

This immediately answers Question 5.9 negatively by taking \(k=3\).

## 1. The construction

Fix \(n\ge3\), put \(q=2n+1\), and work in the cyclic group \(\mathbb Z_q\). Let
\[
S_n=\{1,2,\ldots,n-1,n+1\}\subseteq \mathbb Z_q.
\]
Define \(T_n\) on vertex set \(\mathbb Z_q\) by
\[
x\longrightarrow y
\quad\Longleftrightarrow\quad
y-x\in S_n.
\]

This is indeed a tournament. Namely,
\[
-S_n=\{n,n+2,n+3,\ldots,2n\},
\]
and therefore
\[
S_n\cap(-S_n)=\varnothing,\qquad
S_n\cup(-S_n)=\mathbb Z_q\setminus\{0\}.
\]
Translations of \(\mathbb Z_q\) are automorphisms of \(T_n\).

## 2. A last-vertex obstruction

We first record a simple observation.

> **Lemma.** If every vertex \(v\) of a tournament \(T\) dominates a directed triangle, then
> \[
> \overrightarrow{\omega}(T)\ge3.
> \]

**Proof.**
Consider an arbitrary ordering of \(V(T)\), and let \(v\) be its last vertex. By hypothesis, there are \(a,b,c\in N^+(v)\) inducing a directed triangle. In every linear ordering of \(a,b,c\), at least one of their three arcs is a backedge, say the edge \(ab\) belongs to the backedge graph. Since \(v\) is last and \(v\to a,v\to b\), both \(va\) and \(vb\) are also backedges. Hence \(v,a,b\) form a triangle in the backedge graph. This holds for every ordering. \(\square\)

For every \(x\in\mathbb Z_q\), the three vertices
\[
x+1,\qquad x+2,\qquad x+n+1
\]
are all dominated by \(x\), since \(1,2,n+1\in S_n\). Moreover,
\[
x+1\to x+2,
\]
because the difference is \(1\);
\[
x+2\to x+n+1,
\]
because the difference is \(n-1\); and
\[
x+n+1\to x+1,
\]
because
\[
(x+1)-(x+n+1)\equiv n+1\pmod q.
\]
Thus they induce a directed triangle. The lemma gives
\[
\overrightarrow{\omega}(T_n)\ge3.
\]

## 3. The natural backedge graph has one triangle

Consider the natural order
\[
0\prec1\prec\cdots\prec2n.
\]
For \(0\le i<j\le2n\), put \(d=j-i\). The pair \(ij\) is a backedge precisely when \(j\to i\), equivalently when
\[
i-j\equiv q-d\in S_n.
\]
This occurs exactly when
\[
d=n
\quad\text{or}\quad
n+2\le d\le2n.
\]
Thus the edge set of the backedge graph is
\[
ij\in E(T_n^\prec)
\quad\Longleftrightarrow\quad
j-i\in D_n,
\qquad
D_n:=\{n\}\cup\{n+2,\ldots,2n\}.
\]

We now determine its triangles. Suppose \(i<j<k\) form a triangle, and write
\[
a=j-i,\qquad b=k-j.
\]
Since both \(ij\) and \(jk\) are edges, \(a,b\in D_n\), and hence \(a,b\ge n\). On the other hand,
\[
a+b=k-i\le2n.
\]
Consequently \(a=b=n\). It follows that
\[
k=i+2n,
\]
so necessarily \(i=0\), \(j=n\), and \(k=2n\).

Conversely, the distances among \(0,n,2n\) are \(n,n,2n\), all belonging to \(D_n\). Therefore the natural backedge graph has exactly one triangle:
\[
\{0,n,2n\}.
\]
In particular, its clique number is \(3\), and hence
\[
\overrightarrow{\omega}(T_n)\le3.
\]
Together with the previous lower bound,
\[
\boxed{\overrightarrow{\omega}(T_n)=3.}
\]

## 4. Criticality

Delete the vertex \(0\). Restricting the natural order to
\[
1\prec2\prec\cdots\prec2n
\]
deletes the unique triangle \(\{0,n,2n\}\) from the backedge graph. The resulting backedge graph is triangle-free. Hence
\[
\overrightarrow{\omega}(T_n-0)\le2.
\]

Translations are automorphisms of \(T_n\), so \(T_n-v\cong T_n-0\) for every vertex \(v\). Therefore
\[
\overrightarrow{\omega}(T_n-v)\le2
\qquad\text{for every }v\in V(T_n).
\]

The parameter \(\overrightarrow{\omega}\) is monotone under taking subtournaments: restricting any ordering of a tournament to a vertex subset gives the induced backedge graph on that subset. Consequently, if \(A\subsetneq T_n\), choose \(v\notin V(A)\); then
\[
\overrightarrow{\omega}(A)
\le \overrightarrow{\omega}(T_n-v)
\le2.
\]
Thus \(T_n\) is induced-subtournament-minimal with \(\overrightarrow{\omega}\ge3\).

## 5. Disproof of Question 5.9

Suppose that the requested function \(\ell\) existed. Choose \(n\ge3\) such that
\[
2n+1>\ell(3).
\]
The tournament \(T_n\) satisfies
\[
\overrightarrow{\omega}(T_n)=3.
\]
But every proper subtournament has clique number at most \(2\). Therefore the only subtournament \(A\subseteq T_n\) with
\[
\overrightarrow{\omega}(A)\ge3
\]
is \(A=T_n\) itself, whose order is \(2n+1>\ell(3)\). This contradicts the defining property of \(\ell\).

Hence no such function exists.

# Conclusion

Question 5.9 has a negative answer, already for \(k=3\). The tournaments
\[
T_n=\operatorname{Cay}\!\left(\mathbb Z_{2n+1},
\{1,\ldots,n-1,n+1\}\right),\qquad n\ge3,
\]
form an infinite family of \(3\)-\(\overrightarrow{\omega}\)-critical tournaments. There are no remaining cases or conditional steps in the argument.