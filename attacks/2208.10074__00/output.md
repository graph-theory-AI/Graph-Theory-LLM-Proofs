```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "The literal tree-depth formulation is false: square grids force the tree-depth factor to be \u03a9(log log n) when the clique factor has size O(\u221an).",
  "would_publish": false,
  "caveats": "The supplied source abstract states bounded tree-width, not bounded tree-depth; the actual tree-width conjecture is not addressed here."
}
```

# Statement under consideration

Interpreting the catalog statement literally, it asserts:

> If a hereditary class \(\mathcal G\) has balanced separators of order \(O(n^{1-\epsilon})\), then there are constants \(t,C\) such that every \(n\)-vertex \(G\in\mathcal G\) is a subgraph of
> \[
> H\boxtimes K_m,
> \qquad \operatorname{td}(H)\le t,\qquad m\le Cn^{1-\epsilon}.
> \]

This is false, already for planar graphs with \(\epsilon=\tfrac12\).

In fact, the following stronger lower bound holds.

## Theorem

For every constant \(C>0\), if the \(N\times N\) grid \(Q_N\) is a subgraph of
\[
H\boxtimes K_m,\qquad m\le CN,
\]
then
\[
\operatorname{td}(H)\ge \log_2\log N-O_C(1).
\]
In particular, \(\operatorname{td}(H)\) cannot be bounded independently of \(N\).

Since \(Q_N\) has \(n=N^2\) vertices, this says that a clique factor of order \(O(\sqrt n)\) forces tree-depth \(\Omega(\log\log n)\).

# 1. A necessary coloring condition

Recall that \(\operatorname{td}(H)\le t\) means that there is a rooted forest \(F\) of height \(t\) such that \(H\) is a subgraph of the closure of \(F\), where two vertices are adjacent in the closure when one is an ancestor of the other.

Suppose
\[
G\subseteq H\boxtimes K_m.
\]
Project each vertex of \(G\) to its \(H\)-coordinate:
\[
\pi:V(G)\longrightarrow V(H).
\]
Every fiber of \(\pi\) has size at most \(m\). Moreover, if \(uv\in E(G)\), then either \(\pi(u)=\pi(v)\) or \(\pi(u)\pi(v)\in E(H)\).

Color each \(v\in V(G)\) by the depth in \(F\) of \(\pi(v)\). This uses at most \(t\) colors.

### Lemma 1

For every nonempty connected vertex set \(X\subseteq V(G)\), some color occurs on \(X\) between \(1\) and \(m\) times.

### Proof

The projection \(\pi(X)\) is connected in \(H\), after repetitions are suppressed. A connected vertex set in the closure of a rooted forest has a unique vertex of minimum depth.

Indeed, choose a minimum-depth vertex \(x\) and follow any path in the closure starting at \(x\). Inductively, every vertex on the path is a descendant of \(x\): if \(x\) is an ancestor of the current vertex and the next vertex is comparable with the current one, then the next vertex is either also a descendant of \(x\), or is a strict ancestor of \(x\), the latter contradicting minimality. Thus \(x\) is the unique minimum-depth vertex.

Consequently, all vertices of \(X\) having the minimum color project to one vertex of \(H\). There are at most \(m\) such vertices. \(\square\)

Thus an embedding into \(H\boxtimes K_m\) with \(\operatorname{td}(H)\le t\) gives a \(t\)-coloring in which every connected set has a color appearing at most \(m\) times.

# 2. An isoperimetric lemma for the square lattice

For a finite \(A\subseteq\mathbb Z^2\), let \(p(A)\) denote its edge perimeter: the number of lattice edges with exactly one endpoint in \(A\).

### Lemma 2

For every nonempty finite \(A\subseteq\mathbb Z^2\),
\[
p(A)\ge 4\sqrt{|A|}.
\]

### Proof

Let \(r\) and \(c\) be the numbers of rows and columns meeting \(A\). Every occupied row contributes at least two horizontal boundary edges, and every occupied column contributes at least two vertical boundary edges. Hence
\[
p(A)\ge 2r+2c\ge 4\sqrt{rc}\ge4\sqrt{|A|}.
\]
\(\square\)

We also need a fragmentation consequence.

### Lemma 3

Let \(A\subseteq\mathbb Z^2\) be finite and connected, and let \(R\subseteq A\). If \(A_1,\dots,A_k\) are the components of \(A-R\), then
\[
\sum_{j=1}^k p(A_j)\le p(A)+4|R|.
\]
Consequently, if \(M=\max_j|A_j|\), then
\[
M\ge
\left(
 \frac{4(|A|-|R|)}{p(A)+4|R|}
\right)^2.
\]

### Proof

Every boundary edge of a component \(A_j\) either was already a boundary edge of \(A\), or has its other endpoint in \(R\). There are at most \(4|R|\) edges of the second type, proving the perimeter inequality.

By Lemma 2,
\[
4\sqrt{|A_j|}\le p(A_j).
\]
Therefore
\[
\begin{aligned}
|A|-|R|
 &=\sum_j |A_j|\\
 &\le \sqrt M\sum_j\sqrt{|A_j|}\\
 &\le \frac{\sqrt M}{4}\sum_j p(A_j)\\
 &\le \frac{\sqrt M}{4}\bigl(p(A)+4|R|\bigr).
\end{aligned}
\]
Rearranging proves the claimed lower bound on \(M\). \(\square\)

# 3. Fixedly many colors do not suffice

Fix \(C>0\) and an integer \(t\). Suppose, for contradiction, that \(Q_N\) has a \(t\)-coloring such that every nonempty connected set has a color occurring at most \(CN\) times.

Set
\[
A_0=V(Q_N).
\]
Then
\[
|A_0|=N^2,\qquad p(A_0)=4N.
\]

Inductively, suppose \(A_i\) is nonempty and connected. By the coloring property, there is a color appearing on \(A_i\) at most \(CN\) times. Let \(R_i\) be all vertices of that color in \(A_i\), and choose \(A_{i+1}\) to be a largest component of \(A_i-R_i\).

Define constants
\[
a_0=1,\qquad b_0=4,
\]
and recursively
\[
b_{i+1}=b_i+4C,\qquad
a_{i+1}=\left(\frac{2a_i}{b_i+4C}\right)^2.
\]
For fixed \(C,t\), all \(a_i\) are positive constants.

We claim that, for sufficiently large \(N\),
\[
|A_i|\ge a_iN^2,\qquad p(A_i)\le b_iN
\]
for every \(0\le i\le t\).

The assertion is true for \(i=0\). If it holds for \(i\), choose \(N\) sufficiently large that
\[
CN\le \frac{a_iN^2}{2}.
\]
Then
\[
|A_i|-|R_i|\ge \frac{a_iN^2}{2}.
\]
Lemma 3 gives
\[
\begin{aligned}
|A_{i+1}|
&\ge
\left(
 \frac{4(a_iN^2/2)}
      {(b_i+4C)N}
\right)^2\\
&=a_{i+1}N^2.
\end{aligned}
\]
It also gives
\[
p(A_{i+1})\le p(A_i)+4|R_i|
              \le(b_i+4C)N
              =b_{i+1}N.
\]
This proves the induction.

At every step, the color removed from \(A_i\) is absent from all later \(A_j\), so the colors removed in successive steps are distinct. After \(t\) steps, all \(t\) colors have been removed. Thus \(A_t\) should be empty. But the induction gives
\[
|A_t|\ge a_tN^2>0,
\]
a contradiction.

Therefore, for every fixed \(C,t\), sufficiently large square grids admit no such coloring. By Lemma 1, they cannot be subgraphs of \(H\boxtimes K_{CN}\) with \(\operatorname{td}(H)\le t\).

## Quantitative form

Here
\[
b_i=4+4Ci,\qquad
a_{i+1}=\frac{a_i^2}{4(1+C(i+1))^2}.
\]
Writing \(L_i=-\log a_i\),
\[
L_{i+1}
 =2L_i+\log4+2\log(1+C(i+1)).
\]
Thus, for some finite constant \(K_C\),
\[
L_i\le K_C2^i,
\qquad\text{so}\qquad
a_i\ge \exp(-K_C2^i).
\]
The preceding iteration therefore works for all
\[
i\le \log_2\log N-O_C(1),
\]
which proves
\[
\operatorname{td}(H)=\Omega_C(\log\log N).
\]

# 4. Counterexample to the catalog statement

Let \(\mathcal P\) be the class of planar graphs.

- \(\mathcal P\) is hereditary.
- By the planar separator theorem, every \(n\)-vertex planar graph has a balanced separator of size \(O(\sqrt n)\). Thus the hypothesis holds with \(\epsilon=\tfrac12\).
- The class contains every square grid \(Q_N\), with \(n=N^2\).
- The theorem above shows that if
  \[
  Q_N\subseteq H\boxtimes K_{O(\sqrt n)}
            =H\boxtimes K_{O(N)},
  \]
  then \(\operatorname{td}(H)\) is unbounded, indeed \(\Omega(\log\log n)\).

Hence the literal bounded-tree-depth conjecture is false.

# 5. Textual discrepancy with the source

The final paragraph of the supplied source abstract says **bounded tree-width**, not bounded tree-depth:

> “…a subgraph of the strong product of a graph \(H\) with bounded tree-width and a complete graph of size \(O(n^{1-\epsilon})\).”

That formulation is not refuted by the argument above. The depth-coloring lemma fundamentally uses bounded tree-depth and has no analogue with a bounded number of colors for bounded tree-width. Thus the apparent open problem is a catalog extraction error: the bounded-tree-depth version is false, while the bounded-treewidth version is a different conjecture and remains untouched by this writeup.