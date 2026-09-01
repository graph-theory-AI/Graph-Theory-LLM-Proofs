```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "For fixed ℓ≥4, long-hole detection admits an O(n^ℓ) combinatorial algorithm and an n^{ℓ-3+ω+o(1)} algorithm using fast Boolean matrix multiplication, but no analogous improvement is obtained for long odd holes.",
  "would_publish": false,
  "caveats": "This is only an additive exponent saving for long holes; “substantially” is undefined, the odd case remains open, and literature priority has not been checked."
}
```

## Precise partial result

Let \(n=|V(G)|\), and let \(\ell\ge 4\) be fixed. Write \(T_{\mathrm{BMM}}(n)\) for the time required to multiply two \(n\times n\) Boolean matrices.

### Theorem

There is a deterministic algorithm deciding whether \(G\) contains a hole of length at least \(\ell\) in time

\[
O_\ell\!\left(n^{\ell-3}\bigl(T_{\mathrm{BMM}}(n)+n^2\bigr)\right).
\]

Consequently:

1. using naive Boolean multiplication, the running time is
   \[
   O_\ell(n^\ell);
   \]
2. if \(\omega\) denotes the matrix-multiplication exponent, the running time is
   \[
   O_{\ell,\varepsilon}\bigl(n^{\ell-3+\omega+\varepsilon}\bigr)
   \quad\text{for every }\varepsilon>0,
   \]
   or \(n^{\ell-3+\omega+o(1)}\) in the usual algebraic-RAM notation.

This improves the stated \(O(n^{\ell+1})\) bound, although it does not change the linear dependence on \(\ell\) in the exponent.

## Algorithm

Set

\[
r=\ell-3.
\]

Enumerate every ordered induced path

\[
X=(x_1,x_2,\ldots,x_r).
\]

For \(r=1\), this simply means enumerating one vertex.

For a fixed \(X\), define

\[
A_X=\{a\in V(G)\setminus X : a \text{ is anticomplete to }X\}.
\]

Define the possible left and right endpoints by

\[
L_X=\{u\notin X: ux_1\in E(G),\ ux_i\notin E(G)\text{ for }2\le i\le r\},
\]

and

\[
R_X=\{v\notin X: vx_r\in E(G),\ vx_i\notin E(G)\text{ for }1\le i<r\}.
\]

Thus, for \(u\in L_X\), \(v\in R_X\), with \(u\ne v\) and \(uv\notin E(G)\), the sequence

\[
P=u-x_1-\cdots-x_r-v
\]

is an induced path of length

\[
r+1=\ell-2.
\]

Compute the connected components

\[
K_1,\ldots,K_s
\]

of \(G[A_X]\). Form the \(n\times s\) Boolean matrix \(B_X\) given by

\[
B_X(z,j)=1
\quad\Longleftrightarrow\quad
z\text{ has a neighbor in }K_j.
\]

Compute

\[
M_X=B_XB_X^{\mathsf T}
\]

over the Boolean semiring. Then \(M_X(u,v)=1\) precisely when \(u\) and \(v\) both have a neighbor in some common component of \(G[A_X]\).

The algorithm accepts if, for some \(X\), there are \(u\in L_X\) and \(v\in R_X\) such that

\[
u\ne v,\qquad uv\notin E(G),\qquad M_X(u,v)=1.
\]

## Correctness

### Acceptance produces a long hole

Suppose the criterion holds for \(X,u,v\), and let \(K\) be a component of \(G[A_X]\) adjacent to both \(u\) and \(v\).

The graph \(G[K\cup\{u,v\}]\) contains a \(u\)-\(v\) path. Let \(Q\) be a shortest such path. Since \(uv\notin E(G)\), \(Q\) has at least two edges. Moreover, every shortest path is induced.

The path

\[
P=u-x_1-\cdots-x_r-v
\]

is induced by the definitions of \(L_X,R_X\) and the assumption \(uv\notin E(G)\). Every internal vertex of \(Q\) belongs to \(A_X\), so it is anticomplete to \(X\). Thus there are no chords between the interiors of \(P\) and \(Q\). Chords incident with \(u\) or \(v\) inside \(Q\) are excluded because \(Q\) is a shortest path.

Hence \(P\cup Q\) is an induced cycle. Its length is at least

\[
|E(P)|+|E(Q)|\ge (\ell-2)+2=\ell.
\]

Thus it is a long hole.

### Every long hole is found

Conversely, let \(C\) be an induced cycle of length at least \(\ell\). Choose \(\ell-2\) consecutive edges of \(C\), and write the resulting path as

\[
u-x_1-\cdots-x_r-v,
\qquad r=\ell-3.
\]

Let \(Q\) be the complementary \(u\)-\(v\) path on \(C\). Since \(|C|\ge\ell\), \(Q\) has at least two edges.

Because \(C\) is induced:

- \(X=(x_1,\ldots,x_r)\) is an induced path;
- \(u\in L_X\) and \(v\in R_X\);
- \(u\ne v\) and \(uv\notin E(G)\);
- every internal vertex of \(Q\) is anticomplete to \(X\).

Therefore all internal vertices of \(Q\) lie in one component \(K\) of \(G[A_X]\), and \(K\) has neighbors in both \(u\) and \(v\). Thus \(M_X(u,v)=1\), and the algorithm accepts.

This proves the theorem.

## Running time

There are at most \(n^{\ell-3}\) ordered choices for \(X\). For each choice:

- testing whether \(X\) is induced takes \(O_\ell(1)\) time with an adjacency matrix;
- constructing \(A_X,L_X,R_X\) takes \(O_\ell(n)\);
- finding the components of \(G[A_X]\) and constructing \(B_X\) takes \(O(n^2)\);
- computing \(B_XB_X^{\mathsf T}\) takes \(T_{\mathrm{BMM}}(n)\);
- inspecting all endpoint pairs takes \(O(n^2)\).

This gives the asserted bound. The naive \(O(n^3)\) Boolean product yields \(O(n^\ell)\). For the algebraic bound, one may multiply over a field of characteristic greater than \(n\); every entry is then a count between \(0\) and \(n\), so it is nonzero exactly when the corresponding Boolean product entry is one.

The fixed-\(X\) completion problem is naturally a tripartite triangle problem: its three parts are \(L_X\), \(R_X\), and the components of \(G[A_X]\), with an \(L_XR_X\)-edge representing a nonedge of \(G\). This explains the Boolean-matrix-multiplication term.

## Why this does not extend directly to odd holes

The path \(P\) above has length \(\ell-2\). To obtain an odd hole, the complementary path \(Q\) must have prescribed parity:

\[
|E(Q)|\not\equiv \ell-2 \pmod 2.
\]

Connectivity of a component does not provide an induced path of a prescribed parity. Even the existence of an ordinary simple path of the correct parity is insufficient, because a shortest path subject to a parity condition need not be induced.

Here is a concrete obstruction. Let \(P\) be an induced \(u\)-\(v\) path of length \(d=\ell-2\).

- If \(d\) is even, add vertices \(a,b\) and edges
  \[
  ua,\ ab,\ ub,\ bv.
  \]
  The path \(u-a-b-v\) has the required odd parity, but it has chord \(ub\). The only induced route through this gadget is \(u-b-v\), of even length.

- If \(d\) is odd, subdivide \(bv\) once, replacing it by \(b-c-v\). The required even path
  \[
  u-a-b-c-v
  \]
  again has chord \(ub\), while the induced shortcut \(u-b-c-v\) has odd length.

Take all gadget vertices anticomplete to the interior of \(P\). In either case, the shortcut together with \(P\) is an even long hole; the route of the parity needed for an odd cycle is chorded. The only induced odd cycle introduced by the gadget is the triangle \(uab\), not an odd hole. Thus merely augmenting the component test with parity reachability would give a false positive.

Accordingly, the argument above gives no improvement to the \(O(n^{20\ell+40})\) long odd-hole algorithm. Handling the interaction between parity and chords remains the substantive unresolved part.

## Status and gaps

The proved result is an unconditional exponent reduction for ordinary long-hole detection:

\[
O(n^{\ell+1})
\quad\longrightarrow\quad
O(n^\ell)
\quad\text{or}\quad
n^{\ell-3+\omega+o(1)}.
\]

It remains \(n^{\Theta(\ell)}\), so it does not answer interpretations of “substantially improved” that ask for a smaller coefficient of \(\ell\), an \(n^{o(\ell)}\) algorithm, or fixed-parameter tractability. The long odd-hole running time is not improved here. No claim of literature novelty or optimality is made.