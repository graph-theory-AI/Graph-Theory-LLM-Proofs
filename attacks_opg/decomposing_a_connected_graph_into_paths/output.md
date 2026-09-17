```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove Gallai's bound, with additional endpoint control, for connected graphs whose blocks are cliques or cycles.",
  "would_publish": false,
  "caveats": "This does not settle arbitrary connected graphs; no novelty is claimed for the special case."
}
```

# A self-contained partial result

Write \(p(G)\) for the minimum number of nontrivial simple paths whose edge sets partition \(E(G)\). Paths may share vertices, but not edges.

Because the number of paths is integral, the conjectured bound is
\[
p(G)\le \left\lceil\frac{|V(G)|}{2}\right\rceil.
\]
The tightness explanation in the quoted entry should concern **paths**, not cycles: for \(n\ge2\),
\[
p(K_n)\ge
\left\lceil\frac{\binom n2}{n-1}\right\rceil
=\left\lceil\frac n2\right\rceil.
\]

I prove the following restricted theorem independently of the literature claims in the prompt.

**Theorem.** Let \(G\) be a connected graph on \(n\) vertices such that every block is a complete graph or a simple cycle, with bridges regarded as \(K_2\)-blocks. Then
\[
p(G)\le \left\lceil\frac n2\right\rceil.
\]
More strongly, unless \(G\) is an odd complete graph of order at least three,
\[
p(G)\le \left\lfloor\frac n2\right\rfloor.
\]

The proof gives a prescribed-endpoint statement that makes the behavior at cutvertices explicit. No novelty claim is intended.

## 1. Endpoint-controlled decompositions of complete graphs

For a path decomposition \(\mathcal P\), let \(e_{\mathcal P}(v)\) be the number of its paths having \(v\) as an endpoint.

**Lemma 1.**

1. \(K_{2k}\) has a decomposition into \(k\) Hamilton paths, with every vertex an endpoint exactly once.
2. Given any set \(S\subseteq V(K_{2k+1})\) of size \(k+1\), there is a decomposition into \(k+1\) paths satisfying
   \[
   e_{\mathcal P}(v)=
   \begin{cases}
   2,&v\in S,\\
   0,&v\notin S.
   \end{cases}
   \]

**Proof.** First construct a Hamilton-cycle decomposition of \(K_{2k+1}\), using vertices
\[
\{\infty\}\cup\mathbb Z_{2k}.
\]
For \(i=0,\ldots,k-1\), define
\[
C_i=(\infty,x_0,x_1,\ldots,x_{2k-1},\infty),
\]
where, modulo \(2k\),
\[
x_{2j}=i+j,\qquad x_{2j+1}=i-j-1
\quad(0\le j\le k-1).
\]

Each \(C_i\) is Hamiltonian. Its finite-vertex edges consist precisely of the unordered pairs of distinct residues whose sums are \(2i-1\) or \(2i\) modulo \(2k\): there are \(k\) pairs of the first kind and \(k-1\) of the second. Its two edges at \(\infty\) lead to \(i\) and \(i-k\). Consequently, the \(C_i\) partition all edges of \(K_{2k+1}\).

Deleting \(\infty\) from every \(C_i\) gives \(k\) Hamilton paths decomposing \(K_{2k}\). Their endpoint pairs are
\[
\{i,i-k\},\qquad 0\le i\le k-1,
\]
so every finite vertex is an endpoint exactly once. This proves the first assertion.

For the second, consider the path
\[
R=(\infty,0,1,\ldots,k-1).
\]
Its edge \(\infty0\) belongs to \(C_0\), and, for \(1\le i\le k-1\), its edge \((i-1)i\) belongs to \(C_i\). Thus \(R\) contains exactly one edge from each \(C_i\).

Removing that edge from each \(C_i\) leaves \(k\) Hamilton paths. Together with \(R\), they decompose \(K_{2k+1}\).

Every vertex lies in the \(k\) Hamilton paths, and exactly the vertices
\[
S_0=\{\infty,0,\ldots,k-1\}
\]
also lie in \(R\). For any decomposition into nontrivial paths,
\[
e_{\mathcal P}(v)
=2\,|\{P\in\mathcal P:v\in V(P)\}|-d_G(v).
\]
Since \(K_{2k+1}\) is \(2k\)-regular, the endpoint counts are two on \(S_0\) and zero elsewhere. Relabeling the complete graph sends \(S_0\) to any prescribed \(S\). \(\square\)

We also use the elementary cycle analogue:

**Observation.** If \(C\) is a simple cycle and \(S\subseteq V(C)\) has at least two vertices, cutting \(C\) at the vertices of \(S\) gives \(|S|\) nontrivial paths. Every vertex of \(S\) is an endpoint twice, and all other vertices are endpoints zero times.

## 2. Gluing at a cutvertex

Suppose \(G_1\) and \(G_2\) meet in exactly one vertex \(x\). Let \(\mathcal P_i\) be path decompositions, and put
\[
a_i=e_{\mathcal P_i}(x).
\]
For any integer \(t\le\min(a_1,a_2)\), choose \(t\) distinct endpoint paths from each side and concatenate them in pairs at \(x\).

Every concatenation is a simple path: its two constituent paths have no common vertex other than \(x\). The resulting decomposition of \(G_1\cup G_2\) has
\[
|\mathcal P_1|+|\mathcal P_2|-t
\]
paths and
\[
a_1+a_2-2t
\]
endpoints at \(x\). Endpoint counts at other vertices are unchanged.

This observation will also be applied successively to branches attached at different vertices of one block.

## 3. The rooted bound

The main ingredient is stronger than the unrooted theorem.

**Lemma 2.** Let \(G\) belong to the class in the theorem, let \(n\ge2\), and fix \(x\in V(G)\). Define
\[
a_G(x)=
\begin{cases}
1,&d_G(x)\text{ is odd},\\
2,&d_G(x)\text{ is even}.
\end{cases}
\]
Then \(G\) has a path decomposition \(\mathcal P\) such that
\[
e_{\mathcal P}(x)=a_G(x)
\]
and
\[
|\mathcal P|
\le
\left\lfloor\frac{n+a_G(x)-1}{2}\right\rfloor.
\tag{1}
\]

In particular, an odd-degree prescribed vertex can be made an endpoint exactly once using at most \(\lfloor n/2\rfloor\) paths.

**Proof.** Induct on the number of blocks. Write
\[
b(n,a)=\left\lfloor\frac{n+a-1}{2}\right\rfloor.
\]

### Case 1: \(x\) is a cutvertex

Split \(G\) into two nontrivial unions of branches \(G_1,G_2\), meeting only at \(x\). Put
\[
n_i=|V(G_i)|,\qquad a_i=a_{G_i}(x),\qquad a=a_G(x).
\]
Then \(n=n_1+n_2-1\).

By induction, \(G_i\) has a decomposition with at most \(b(n_i,a_i)\) paths and exactly \(a_i\) endpoints at \(x\). Set
\[
t=\frac{a_1+a_2-a}{2}.
\]
The three possibilities are
\[
(a_1,a_2,a,t)=(1,1,2,0),\ (1,2,1,1),\ (2,2,2,1),
\]
up to interchanging the two sides. Thus the gluing observation applies. It leaves exactly \(a\) endpoints at \(x\), and the path count is at most
\[
\begin{aligned}
b(n_1,a_1)+b(n_2,a_2)-t
&\le
\left\lfloor
\frac{n_1+n_2+a_1+a_2-2}{2}
\right\rfloor-t\\
&=
\left\lfloor\frac{n+a-1}{2}\right\rfloor.
\end{aligned}
\]

### Case 2: \(x\) is not a cutvertex

Let \(B\) be the unique block containing \(x\), and put \(r=|V(B)|\).

The block-cutvertex tree describes \(G\) as \(B\), together with rooted graphs \(H_u\) attached at vertices \(u\in V(B)\setminus\{x\}\). Each nontrivial \(H_u\) meets \(B\) only at \(u\), and different attached graphs have disjoint vertex sets outside \(B\).

For a nontrivial \(H_u\), induction gives a decomposition with \(q_u\) paths and
\[
a_u\in\{1,2\}
\]
endpoints at \(u\), satisfying
\[
2q_u\le |V(H_u)|-1+a_u.
\tag{2}
\]
If there is no attachment at \(u\), set \(q_u=a_u=0\) and regard \(H_u\) as the single vertex \(u\).

Let
\[
W=\sum_{u\ne x}\bigl(|V(H_u)|-1\bigr),
\qquad
A=\sum_{u\ne x}a_u.
\]
Then
\[
n=r+W,\qquad 2\sum_{u\ne x}q_u\le W+A.
\tag{3}
\]

We now choose a decomposition of \(B\), and join its endpoint paths to those in the attachments.

#### Case 2a: \(B=K_{2k}\)

Use Lemma 1 to decompose \(B\) into \(k\) paths, with one endpoint at every vertex. At each nontrivial attachment, perform one join.

If there are \(h\) nontrivial attachments, then \(A\le2h\). The resulting number \(q\) of paths satisfies
\[
2q
\le 2k+W+A-2h
\le n.
\]
There is exactly one endpoint at \(x\). Since \(d_G(x)=2k-1\), this proves (1).

#### Case 2b: \(B=K_{2k+1}\)

Choose \(k\) vertices \(T\subseteq V(B)\setminus\{x\}\) having the largest values of \(a_u\), including zero values when necessary. Because \(T\) consists of half of these \(2k\) vertices,
\[
M:=\sum_{u\in T}a_u\ge \frac A2.
\]

Apply Lemma 1 with endpoint set
\[
S=\{x\}\cup T.
\]
This gives \(k+1\) paths in \(B\), with two endpoints at each vertex of \(S\).

For each \(u\in T\), perform \(a_u\) joins to the attachment at \(u\). This is possible since \(a_u\le2\). Consequently,
\[
2q
\le 2k+2+W+A-2M
\le n+1.
\]
Exactly two endpoints remain at \(x\), and \(d_G(x)=2k\). Again (1) follows.

#### Case 2c: \(B\) is a cycle

Here \(d_G(x)=2\), so we need two endpoints at \(x\) and at most \(\lceil n/2\rceil\) paths.

Let \(h_1\) and \(h_2\) be the numbers of vertices \(u\ne x\) with \(a_u=1\) and \(a_u=2\), respectively.

* If \(h_2\ge1\), cut the cycle at \(x\) and at all vertices with \(a_u=2\). This produces \(h_2+1\) paths in \(B\). Perform two joins at each such attachment. Using (3),
  \[
  \begin{aligned}
  2q
  &\le 2(h_2+1)+W+(h_1+2h_2)-4h_2\\
  &=W+h_1+2
  \le n+1.
  \end{aligned}
  \]

* If \(h_2=0\) and \(h_1\ge1\), cut the cycle at \(x\) and at one vertex with \(a_u=1\), and perform one join there. Then
  \[
  2q\le4+W+h_1-2
      =W+h_1+2
      \le n+1.
  \]

* If \(h_1=h_2=0\), there are no attachments. Cutting the cycle at \(x\) and any other vertex gives two paths, and
  \[
  2\le\left\lceil\frac r2\right\rceil
  \qquad(r\ge3).
  \]

In every case exactly two endpoints remain at \(x\).

All joins above preserve simplicity by the gluing observation. The cases exhaust the possibilities and complete the induction. \(\square\)

## 4. Finishing the unrooted theorem

Lemma 2 immediately gives
\[
p(G)\le\left\lceil\frac n2\right\rceil.
\]

Suppose now that \(G\) has a cutvertex \(x\). Split it into nontrivial rooted graphs \(G_1,G_2\) meeting only at \(x\), and obtain the decompositions from Lemma 2. Write their root endpoint counts as \(a_1,a_2\in\{1,2\}\).

This time perform
\[
s=\min(a_1,a_2)
\]
joins. With \(n=n_1+n_2-1\), the resulting path count is at most
\[
\begin{aligned}
b(n_1,a_1)+b(n_2,a_2)-s
&\le
\left\lfloor
\frac{n+|a_1-a_2|-1}{2}
\right\rfloor\\
&\le \left\lfloor\frac n2\right\rfloor,
\end{aligned}
\tag{4}
\]
because \(|a_1-a_2|\le1\).

If \(G\) has no cutvertex and \(n\ge2\), it consists of one block:

* An even complete graph has the required \(\lfloor n/2\rfloor\)-path decomposition by Lemma 1.
* A cycle of length at least four decomposes into two paths, and \(2\le\lfloor n/2\rfloor\).
* An odd complete graph has path number exactly \((n+1)/2\), by Lemma 1 and the edge-count lower bound.
* The triangle is already covered by the preceding item.

Finally, the single-vertex graph has an empty decomposition. This proves the theorem.

### Two consequences

First, (4) gives a slightly stronger bound whenever \(G\) has an **even-degree cutvertex**. In that case \(a_1=a_2\), so
\[
p(G)\le \left\lfloor\frac{n-1}{2}\right\rfloor.
\]

Second, consider any graph formed by identifying one vertex from each of at least two cliques, each of order at least two, into a common vertex \(v\). Then
\[
\boxed{p(G)=\left\lfloor\frac n2\right\rfloor.}
\]
The upper bound is the theorem. For the lower bound, \(d(v)=n-1\), and a simple path uses at most two edges incident with \(v\).

## 5. Scope and obstruction to extending the proof

The argument is complete for the stated class. It does **not** establish Gallai's conjecture for unrestricted blocks.

Indeed, the rooted strengthening itself is false for arbitrary graphs. Take \(K_5-e\), and choose as root an endpoint of the missing edge. This root has odd degree, so extending Lemma 2 to arbitrary graphs would assert a decomposition into
\[
\left\lfloor\frac52\right\rfloor=2
\]
paths. But \(K_5-e\) has nine edges, while two simple paths on five vertices contain at most eight edges.

Thus the endpoint invariant used here cannot simply be imposed on arbitrary 2-connected blocks. That is a concrete limitation of this approach—not a counterexample to Gallai's original bound, which allows three paths on five vertices.