```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The coefficient is exactly 1 for flow-critical graphs whose vertices of degree at least four induce at most 3|A|/2+O(1) edges, including graphs with boundedly many noncubic vertices, while any global obstruction to alpha=1 must have a dense noncubic core.",
  "would_publish": false,
  "caveats": "The global interval remains 1 <= alpha <= 5/2 because the density of the noncubic core is not controlled."
}
```

# 1. Statement of the partial result

Interpret \(O(1)\) as a universal additive constant independent of both \(G\) and \(g(G)\).

For a nontrivial \(\mathbb Z_3\)-flow-critical graph \(G\), let
\[
D=\{v\in V(G):d_G(v)=3\},\qquad
A=V(G)\setminus D,
\]
and put \(a=|A|\) and \(e_A=|E(G[A])|\). After discarding isolated vertices, all vertices in \(A\) have degree at least four.

The main elementary estimate obtained here is
\[
\boxed{\quad
|E(G)|\le \frac52|V(G)|+g(G)+e_A-\frac32a-2.
\quad} \tag{1}
\]

Consequently:

1. If a class of \(\mathbb Z_3\)-flow-critical graphs satisfies
   \[
   e(G[A])\le \frac32|A|+C
   \]
   for a fixed constant \(C\), then every graph in the class satisfies
   \[
   |E(G)|\le \frac52|V(G)|+g(G)+C-2.
   \]
   Thus the genus coefficient is at most \(1\) in this class.

2. In particular, the coefficient is exactly \(1\) for the class in which \(G[A]\) has average degree at most \(3\), for example when \(G[A]\) is subcubic.

3. For each fixed \(k\ge 3\), the coefficient is exactly \(1\) among \(\mathbb Z_3\)-flow-critical graphs having at most \(k\) noncubic vertices.

The lower bound in these statements is supplied by \(K^+_{3,t}\), whose three vertices on the small side are the only noncubic vertices.

This does not settle the unrestricted problem: the term
\[
e(G[A])-\frac32|A|
\]
is not presently controlled.

# 2. Elementary facts about flow-critical graphs

We regard a \(\mathbb Z_3\)-flow as an element of the kernel of an oriented incidence matrix over \(\mathbb Z_3\), with every edge value in
\(\mathbb Z_3^\ast=\{\pm1\}\).

## Lemma 2.1: deletion and contraction are equivalent here

If \(G\) has no nowhere-zero \(\mathbb Z_3\)-flow and \(G/e\) has one, then \(G-e\) has a nowhere-zero \(\mathbb Z_3\)-flow.

### Proof

Let \(e=uv\), oriented from \(u\) to \(v\), and lift a nowhere-zero flow of \(G/e\) to the edges of \(G-e\). Let the resulting imbalances at \(u,v\) be \(b_u,b_v\). Balance at the contracted vertex gives
\[
b_u+b_v=0.
\]
There is a unique value \(x_e\in\mathbb Z_3\) which balances both \(u\) and \(v\). If \(x_e\ne0\), this produces a nowhere-zero flow of \(G\), contrary to the hypothesis. Hence \(x_e=0\), so \(b_u=b_v=0\), and the lifted assignment is a nowhere-zero flow of \(G-e\). \(\square\)

Conversely, a flow of \(G-e\) remains a flow after \(u\) and \(v\) are identified. Thus a nonflowable graph is contraction-critical exactly when every edge deletion is flowable.

## Lemma 2.2: nontrivial critical graphs are simple and have minimum degree at least three

Apart from the one-edge degenerate case, a \(\mathbb Z_3\)-flow-critical graph, after isolated vertices are removed, is simple and has minimum degree at least three.

### Proof

A loop cannot occur: a flow after deleting or contracting the loop could be extended by assigning the loop any nonzero value.

Suppose \(e,f\) are parallel, oriented in the same direction. Take a nowhere-zero flow \(x\) on \(G-e\), and write \(x_f=c\ne0\). Replace the value of \(f\) by \(-c\) and assign \(e\) the value \(-c\). Since
\[
(-c)+(-c)=-2c=c\qquad\text{in }\mathbb Z_3,
\]
the total incidence contribution of the parallel pair is unchanged. This gives a nowhere-zero flow of \(G\), a contradiction.

If a vertex has degree two with incident edges \(e,f\), then \(G-e\) cannot have a nowhere-zero flow, because conservation at that vertex forces the value on \(f\) to be zero. A degree-one vertex similarly contradicts flowability after deleting any other edge. \(\square\)

In fact, the same argument shows that a nontrivial critical graph is 3-edge-connected: if \(\{e,f\}\) is a 2-edge-cut, then \(f\) is a bridge of \(G-e\).

# 3. The noncubic-core inequality

We use the standard Euler-genus bound for a simple bipartite graph \(H\) on \(N\ge3\) vertices:
\[
|E(H)|\le 2N-4+2g(H). \tag{2}
\]

## Proposition 3.1

Let \(G\) be a simple graph of minimum degree at least three. Put
\[
D=\{v:d_G(v)=3\},\qquad A=V(G)\setminus D.
\]
Then
\[
|E(G)|\le \frac52|V(G)|+g(G)
   +|E(G[A])|-\frac32|A|-2.
\]

### Proof

Write
\[
d=|D|,\qquad a=|A|,
\]
and let \(e_D,e_{AD},e_A\) denote the numbers of edges inside \(D\), between \(A\) and \(D\), and inside \(A\), respectively.

Summing degrees over \(D\) gives
\[
3d=2e_D+e_{AD}. \tag{3}
\]
The spanning subgraph consisting only of the \(A\)-\(D\) edges is simple and bipartite. It embeds in every surface in which \(G\) embeds, so (2) gives
\[
e_{AD}\le 2(a+d)-4+2g(G). \tag{4}
\]
Combining (3) and (4),
\[
3d-2e_D\le 2a+2d-4+2g(G),
\]
and hence
\[
d-2e_D\le 2a-4+2g(G). \tag{5}
\]

On the other hand,
\[
|E(G)|=e_A+e_D+e_{AD}
      =e_A+3d-e_D.
\]
Therefore
\[
\begin{aligned}
|E(G)|-\frac52(a+d)
 &=e_A+\frac12d-e_D-\frac52a\\
 &=e_A+\frac12(d-2e_D)-\frac52a\\
 &\le e_A+a-2+g(G)-\frac52a\\
 &=g(G)+e_A-\frac32a-2,
\end{aligned}
\]
which is the claimed inequality. \(\square\)

The estimate is purely topological once simplicity and minimum degree three are known.

# 4. Exact coefficient for sparse noncubic cores

## Corollary 4.1

Suppose a class \(\mathcal C\) of \(\mathbb Z_3\)-flow-critical graphs has a uniform constant \(C\) such that
\[
|E(G[A])|\le \frac32|A|+C
\]
for every \(G\in\mathcal C\). Then
\[
|E(G)|\le \frac52|V(G)|+g(G)+C-2.
\]

In particular, coefficient \(1\) suffices whenever the graph induced by the noncubic vertices has average degree at most three.

## Corollary 4.2

For every fixed \(k\ge3\), let \(\mathcal C_k\) be the class of \(\mathbb Z_3\)-flow-critical graphs with at most \(k\) noncubic vertices. Then the smallest genus coefficient for \(\mathcal C_k\) is exactly \(1\).

### Proof

For \(G\in\mathcal C_k\), simplicity gives
\[
e_A\le \binom{k}{2}.
\]
Thus Proposition 3.1 gives a bound with genus coefficient \(1\) and an additive constant depending only on \(k\).

For the reverse inequality, take
\[
G_t=K^+_{3,t}.
\]
It has
\[
|V(G_t)|=t+3,\qquad |E(G_t)|=3t+1,
\qquad
g(G_t)=\left\lceil\frac{t-2}{2}\right\rceil.
\]
For \(t\ge4\), exactly the three vertices on the small side are noncubic, and the graph they induce consists of one edge. Hence \(G_t\in\mathcal C_k\) for every \(k\ge3\). Moreover,
\[
\frac{|E(G_t)|-\frac52|V(G_t)|}{g(G_t)}
=
\frac{(t-13)/2}{\lceil(t-2)/2\rceil}
\longrightarrow 1.
\]
No coefficient smaller than \(1\) can therefore hold with a bounded additive term. \(\square\)

For even \(t\), Proposition 3.1 is in fact attained with equality by \(K^+_{3,t}\).

## Verification of flow-criticality of \(K^+_{3,t}\)

Let the small side be \(\{x,y,z\}\), let \(B=\{b_1,\dots,b_t\}\), and add the edge \(xy\). Orient all \(B\)-to-\(\{x,y,z\}\) edges toward the small side and orient \(xy\) from \(x\) to \(y\).

At each \(b_i\), three nonzero elements of \(\mathbb Z_3\) sum to zero only when they are all equal. Thus a putative flow assigns a sign \(s_i\in\{\pm1\}\) to all three edges incident with \(b_i\). If \(S=\sum_i s_i\), balance at \(z\) gives \(S=0\), while balance at \(x\) then forces the value on \(xy\) to be zero. Hence no nowhere-zero flow exists.

After deleting \(xy\), choose the \(s_i\)'s with sum zero. After deleting an incidence edge at \(b_1\), assign opposite values to the two remaining edges at \(b_1\). The other \(t-1\) signs can be chosen with any prescribed sum in \(\mathbb Z_3\), since \(t-1\ge2\), and the value on \(xy\) can then be selected to balance \(x,y,z\). Thus every edge deletion is flowable, and Lemma 2.1 gives contraction-criticality.

# 5. A further restriction on the cubic part

There is a useful structural observation which rules out nonbipartite cubic parts in any dense example.

## Proposition 5.1

Let \(G\) be a nontrivial \(\mathbb Z_3\)-flow-critical graph and let \(D\) be its set of degree-three vertices. If \(G[D]\) is nonbipartite, then
\[
|E(G)|\le 2|V(G)|.
\]

### Proof

For every edge \(e=uv\), the graph \(G-e\) has a nowhere-zero \(\mathbb Z_3\)-flow. Reverse edges carrying value \(-1\), so that every edge has value \(1\). At any degree-three vertex not incident with \(e\), the flow equation says
\[
d^+(v)-d^-(v)\equiv0\pmod3.
\]
Thus \(d^+(v)\in\{0,3\}\): every such vertex is a source or a sink. Adjacent degree-three vertices must consequently receive opposite source/sink labels. Hence
\[
G[D\setminus\{u,v\}]
\]
is bipartite for every edge \(uv\).

Let \(C\) be an odd cycle in \(G[D]\). If an edge \(uv\) had neither endpoint on \(C\), then \(C\) would remain in \(G[D\setminus\{u,v\}]\), a contradiction. Therefore every edge of \(G\) has an endpoint on \(C\).

Every vertex of \(C\) has degree three, with two incident edges already used by \(C\). Thus the \(c=|V(C)|\) vertices of \(C\) have only \(c\) remaining incidence slots. Since every noncycle edge uses at least one such slot,
\[
|E(G)|\le c+c=2c\le2|V(G)|.
\]
\(\square\)

Thus every graph relevant to the genus coefficient near the \(5|V|/2\) baseline has \(G[D]\) bipartite.

# 6. Equivalent face formulation

Let \(G\) have a cellular embedding of minimum Euler genus \(g=g(G)\), with \(f\) faces. Euler's formula gives
\[
|V(G)|-|E(G)|+f=2-g.
\]
Consequently,
\[
|E(G)|-\frac52|V(G)|-g
=f-\frac32|V(G)|-2. \tag{6}
\]

Hence the conjectural value \(\alpha=1\) is equivalent to the following statement:

> Every minimum-genus cellular embedding of a \(\mathbb Z_3\)-flow-critical graph has at most
> \[
> \frac32|V(G)|+O(1)
> \]
> faces.

The cancellation of the genus in (6) helps explain why coefficient \(1\) is natural. The family \(K^+_{3,t}\) asymptotically attains this face count.

# 7. What remains open

From Proposition 3.1,
\[
|E(G)|-\frac52|V(G)|-g(G)
\le
|E(G[A])|-\frac32|A|-2. \tag{7}
\]
Therefore, if a sequence were to force a coefficient at least \(1+\varepsilon\), then necessarily
\[
|E(G[A])|-\frac32|A|
\ge \varepsilon g(G)+O(1).
\]
Together with Proposition 5.1, any such sequence must have:

1. a bipartite graph induced by its cubic vertices; and
2. a noncubic core whose edge excess over \(3|A|/2\) is linear in the genus.

General topology alone cannot control this core term: even planar graphs can have vertex-induced subgraphs much denser than \(3|A|/2\). A complete proof of \(\alpha=1\) would therefore need an additional use of flow-criticality that either bounds this dense core or shows that its planar portions contribute nonpositively to the critical potential. No such argument is established here, so the global range remains
\[
1\le\alpha\le\frac52.
\]