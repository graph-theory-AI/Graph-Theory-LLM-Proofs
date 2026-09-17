```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A self-contained proof establishes the conjecture for vertex-transitive digraphs and their nonuniform independent blow-ups, with an optimal order bound for the blow-ups.",
  "would_publish": false,
  "caveats": "No novelty is claimed; arbitrary digraphs and the general triangle case remain unresolved by this argument."
}
```

## 1. Statement of the partial result

I do not obtain a general proof or counterexample. The result below verifies a symmetry-based special case and extends it to a class of nonregular digraphs. No literature claims are needed for the proof.

Digraphs here have no loops or parallel arcs; opposite arcs are permitted. Write \(g(D)\) for directed girth. Positive minimum outdegree ensures that \(g(D)\) is finite.

For positive integers \(n,r\), the conjectured inequality is equivalently
\[
g(D)\le \left\lceil\frac nr\right\rceil
\quad\Longleftrightarrow\quad
n\ge r\bigl(g(D)-1\bigr)+1.
\]

An **independent blow-up** of a digraph \(Q\) replaces each vertex \(x\) by a nonempty independent set \(W_x\), and replaces every arc \(x\to y\) by all arcs from \(W_x\) to \(W_y\).

**Theorem.** Let \(Q\) be a finite vertex-transitive digraph of outdegree \(d\ge1\), and let \(D\) be any independent blow-up of \(Q\). Put
\[
n=|V(D)|,\qquad r=\delta^+(D),\qquad g=g(D).
\]
Then
\[
\boxed{\ n\ge r(g-1)+\left\lceil\frac rd\right\rceil.\ }
\tag{1}
\]
In particular, \(D\) satisfies Caccetta–Häggkvist.

Moreover, for every choice of integers
\[
d\ge1,\qquad r\ge d,\qquad g\ge2,
\]
there is such a blow-up attaining equality in (1).

The proof first establishes the vertex-transitive case using an elementary finite-group lemma.

## 2. A product-set lemma

For subsets \(A,B\) of a group, write \(AB=\{ab:a\in A,b\in B\}\).

**Lemma.** Let \(A,B\) be subsets of a finite group with identity \(e\). Suppose \(e\in A\cap B\), and the only solution to
\[
ab=e,\qquad a\in A,\ b\in B,
\]
is \(a=b=e\). Then
\[
|AB|\ge |A|+|B|-1.
\tag{2}
\]

**Proof.** Put \(C=AB\). Among pairs \((X,Y)\) satisfying

- \(e\in X\cap Y\);
- \(XY\subseteq C\);
- \(xy=e\), with \(x\in X,y\in Y\), implies \(x=y=e\),

choose one maximizing \(|X|+|Y|\), and, subject to that, maximizing \(|X|\). Such a pair exists, since \((A,B)\) is eligible and the group is finite.

Suppose some \(t\ne e\) belongs to \(X\cap Y\). The uniqueness condition gives
\[
t^{-1}\notin X\cup Y.
\]
Define
\[
\begin{aligned}
X_+&=X\cup Xt,&\qquad Y_-&=Y\cap t^{-1}Y,\\
X_-&=X\cap Xt^{-1},&\qquad Y_+&=Y\cup tY.
\end{aligned}
\]

Both new pairs contain \(e\) in each set. Also
\[
X_+Y_-\subseteq XY,\qquad X_-Y_+\subseteq XY.
\]
For example, \(tY_-\subseteq Y\) and \(X_-t\subseteq X\).

Both pairs preserve the unique representation of \(e\). For the first pair, a new representation would have the form
\[
e=(xt)y=x(ty),
\qquad x\in X,\ y\in Y_-.
\]
Since \(ty\in Y\), uniqueness for \((X,Y)\) forces \(x=e\) and \(y=t^{-1}\), contradicting \(t^{-1}\notin Y\). For the second pair, a new representation
\[
e=x(ty)=(xt)y,
\qquad x\in X_-,\ y\in Y,
\]
would similarly force \(x=t^{-1}\notin X\).

Let
\[
\alpha=|Xt\setminus X|,\qquad \beta=|tY\setminus Y|.
\]
Then
\[
\begin{aligned}
|X_+|+|Y_-|&=|X|+|Y|+\alpha-\beta,\\
|X_-|+|Y_+|&=|X|+|Y|-\alpha+\beta.
\end{aligned}
\]
Maximality of \(|X|+|Y|\) forces \(\alpha=\beta\).

Moreover, \(\alpha>0\): otherwise \(Xt=X\), so \(e\in Xt\) would imply \(t^{-1}\in X\). Consequently, \((X_+,Y_-)\) has the same total size but a larger first set, contradicting the secondary maximality.

Thus \(X\cap Y=\{e\}\). Since \(e\in X\cap Y\),
\[
X\cup Y\subseteq XY\subseteq C.
\]
It follows that
\[
|AB|=|C|
\ge |X|+|Y|-1
\ge |A|+|B|-1.
\]
This proves the lemma. \(\square\)

## 3. Cayley digraphs satisfy the conjecture

Let \(F\) be a finite group of order \(M\), and let
\[
S\subseteq F\setminus\{e\},\qquad |S|=s\ge1.
\]
Consider the Cayley digraph with arcs
\[
x\longrightarrow xt\qquad(t\in S).
\]
Let its girth be \(\gamma\), and put \(B=\{e\}\cup S\).

For \(1\le j\le\gamma-1\), the product \(B^{j-1}B\) has a unique representation of \(e\). Indeed, if
\[
ab=e,\qquad a\in B^{j-1},\ b\in B,
\]
and \(b\ne e\), expressing \(a\) as a product of \(j-1\) elements of \(B\) and deleting identity factors produces a nonempty word in \(S\), of length at most \(j\), whose product is \(e\).

That word gives a directed closed walk of length at most \(j<\gamma\). Every nonempty directed closed walk contains a directed cycle of no greater length, a contradiction.

Applying (2) successively therefore gives
\[
|B^j|\ge |B^{j-1}|+s,
\]
and hence
\[
M\ge |B^{\gamma-1}|\ge 1+(\gamma-1)s.
\]
Equivalently,
\[
\gamma\le \left\lceil\frac Ms\right\rceil.
\tag{3}
\]

## 4. Passing from Cayley digraphs to vertex-transitive digraphs

Let \(Q\) be vertex-transitive, with \(m\) vertices and outdegree \(d\ge1\). Fix \(v\in V(Q)\), and let
\[
F=\operatorname{Aut}(Q),\qquad
h=|\operatorname{Stab}_F(v)|.
\]
By orbit–stabilizer,
\[
|F|=mh.
\]

Set
\[
S=\{\sigma\in F:v\to \sigma(v)\text{ is an arc of }Q\}.
\]
Each outneighbor of \(v\) has exactly \(h\) preimages, so
\[
|S|=dh.
\]
Also \(e\notin S\), since \(Q\) is loopless.

There is a digraph homomorphism from \(\operatorname{Cay}(F,S)\) to \(Q\), namely
\[
\pi(\alpha)=\alpha(v).
\]
Indeed, an arc \(\alpha\to\alpha\sigma\) projects to the arc
\[
\alpha(v)\to\alpha(\sigma(v)).
\]

A directed cycle in the Cayley digraph projects to a directed closed walk in \(Q\), and thus contains a directed cycle in \(Q\) of no greater length. By (3),
\[
g(Q)
\le \left\lceil\frac{|F|}{|S|}\right\rceil
=\left\lceil\frac md\right\rceil.
\]
In the integer order formulation,
\[
\boxed{\ m\ge d\bigl(g(Q)-1\bigr)+1.\ }
\tag{4}
\]

This proves the vertex-transitive case without assuming another conjecture.

## 5. Nonuniform independent blow-ups

Write
\[
w_x=|W_x|\ge1,\qquad n=\sum_x w_x.
\]
Every vertex in \(W_x\) has outdegree
\[
R_x=\sum_{y\in N_Q^+(x)}w_y.
\]
Since every part is nonempty, \(R_x\ge r\) for every \(x\).

Vertex-transitivity makes the indegrees of \(Q\) constant. Equality of total indegree and total outdegree shows that this constant is also \(d\). Consequently,
\[
mr
\le \sum_x R_x
=\sum_y d_Q^-(y)w_y
=dn.
\tag{5}
\]

Also,
\[
g(D)=g(Q).
\tag{6}
\]
One direction follows by projecting a cycle of \(D\) to a closed walk in \(Q\). For the other, choose one vertex from each part corresponding to a shortest cycle of \(Q\); the chosen vertices form a cycle of the same length in \(D\).

Combining (4)–(6),
\[
n\ge \frac{mr}{d}
\ge r(g-1)+\frac rd.
\]
Since \(n-r(g-1)\) is an integer, this yields
\[
n\ge r(g-1)+\left\lceil\frac rd\right\rceil,
\]
proving (1).

In particular, \(\lceil r/d\rceil\ge1\), so
\[
g(D)\le \left\lceil\frac nr\right\rceil.
\]
Proving the assertion for \(r=\delta^+(D)\) also proves it for every smaller prescribed outdegree lower bound.

## 6. Equality constructions

Fix integers \(d\ge1\), \(r\ge d\), and \(\ell\ge2\). Put
\[
m=d(\ell-1)+1.
\]
Let \(Q\) have vertex set \(\mathbb Z_m\) and arcs
\[
i\longrightarrow i+s\pmod m,\qquad 1\le s\le d.
\]
This is vertex-transitive of outdegree \(d\).

Its girth is exactly \(\ell\). A closed walk of length at most \(\ell-1\) would have a positive total increment at most
\[
d(\ell-1)=m-1,
\]
so could not return modulo \(m\). Conversely, \(\ell-1\) increments equal to \(d\), followed by one increment equal to \(1\), give a simple directed cycle of length \(\ell\).

Set
\[
N=\left\lceil\frac{mr}{d}\right\rceil
=r(\ell-1)+\left\lceil\frac rd\right\rceil.
\]
Define periodic integer weights by
\[
w_i=
\left\lfloor\frac{(i+1)N}{m}\right\rfloor
-\left\lfloor\frac{iN}{m}\right\rfloor.
\]
They satisfy \(w_{i+m}=w_i\), sum to \(N\) over one period, and are positive because \(N/m\ge r/d\ge1\).

In the corresponding blow-up, the outdegree associated with part \(i\) is
\[
R_i
=\sum_{s=1}^d w_{i+s}
=\left\lfloor\frac{(i+d+1)N}{m}\right\rfloor
-\left\lfloor\frac{(i+1)N}{m}\right\rfloor
\ge \left\lfloor\frac{dN}{m}\right\rfloor.
\]
The definition of \(N\), together with \(d<m\), gives
\[
r\le \frac{dN}{m}<r+\frac dm<r+1.
\]
Thus every \(R_i\ge r\). Their average is \(dN/m<r+1\), so at least one equals \(r\). Hence the minimum outdegree is exactly \(r\).

The blow-up has girth \(\ell\) and order
\[
N=r(\ell-1)+\left\lceil\frac rd\right\rceil.
\]
Therefore the strengthened bound is attained for every feasible triple \(d,r,\ell\) above.

## 7. The unresolved step in the general problem

The essential input is the uniform group structure. Minimum outdegree alone does not justify replacing the product-set argument by uniform growth of directed out-balls.

Here is an explicit obstruction to that tempting extension. It is **not** a counterexample to Caccetta–Häggkvist.

Construct a digraph on
\[
\{x,a_0,a_1,a_2,a_3\}\ \sqcup\ \mathbb Z_{13}
\]
as follows:

- On \(\mathbb Z_{13}\), take all arcs \(z\to z+s\) for \(s=1,2,3,4\), except delete \(3\to7\).
- Add \(3\to x\).
- Add \(x\to a_i\) for all \(i\).
- Add \(a_i\to a_{i+1\bmod4}\) and \(a_i\to0,1,2\).

Every vertex has outdegree exactly \(4\). The retained step-\(1\) arcs on \(\mathbb Z_{13}\), together with \(3\to x\to a_i\to0\), show strong connectivity.

The girth is \(4\):

- The \(a_i\) form a directed \(4\)-cycle.
- There are no cycles of length at most \(3\) inside \(\mathbb Z_{13}\), since three allowed positive increments total at most \(12\).
- Any cycle crossing between the parts must contain \(3\to x\to a_i\), and \(a_i\to3\) is absent, so such a cycle has length at least \(4\).

Nevertheless, the set of vertices reachable from \(x\) in at most two steps is exactly
\[
\{x,a_0,a_1,a_2,a_3,0,1,2\},
\]
of size
\[
8<1+2\delta^+(D)=9.
\]
Thus even strong connectivity, constant outdegree, and the absence of directed triangles do not give the universal local expansion suggested by the Cayley proof.

The missing step is a valid global replacement for the group-based expansion argument in arbitrary digraphs. None is supplied here; the unrestricted conjecture, including its general triangle case, is not settled by this partial result.