```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture holds for every translation-invariant bipartite digraph over a finite abelian group, including all abelian circulant-type examples.",
  "would_publish": false,
  "caveats": "The argument uses translation invariance essentially and gives no proof for arbitrary bipartite digraphs."
}
```

## 1. Statement of the partial result

Let \(\Gamma\) be a finite abelian group of order \(n\), written additively, and let \(A=\{a_x:x\in\Gamma\}\) and \(B=\{b_x:x\in\Gamma\}\) be two copies of \(\Gamma\). Given nonempty subsets \(S,T\subseteq\Gamma\), define the bipartite digraph
\[
G(\Gamma;S,T)
\]
by
\[
a_x\longrightarrow b_{x+s}\quad(s\in S),\qquad
b_y\longrightarrow a_{y+t}\quad(t\in T).
\]
Thus every vertex of \(A\) has out-degree \(|S|\), and every vertex of \(B\) has out-degree \(|T|\).

### Theorem
For every integer \(k\geq 1\), if
\[
k|T|+|S|>|\Gamma|,
\]
then \(G(\Gamma;S,T)\) contains a directed cycle of length at most \(2k\).

Consequently, Conjecture 1.5 is valid for every bipartite digraph admitting a regular abelian group action on each part, with the action preserving all arcs.

The proof uses only the finite abelian form of Kneser’s sumset theorem.

---

## 2. Two additive lemmas

We use the following formulation of Kneser’s theorem. If \(X,Y\) are nonempty subsets of a finite abelian group and
\[
H=\{h:X+Y+h=X+Y\},
\]
then
\[
|X+Y|\geq |X+H|+|Y+H|-|H|.
\tag{2.1}
\]

### Lemma 2.1: Unique-representation sumset bound
Suppose \(X,Y\subseteq\Gamma\), and some element of \(X+Y\) has a unique representation as \(x+y\), with \(x\in X\) and \(y\in Y\). Then
\[
|X+Y|\geq |X|+|Y|-1.
\tag{2.2}
\]

#### Proof
Translate \(X,Y\) so that the uniquely represented element is \(0=0+0\). Thus
\[
X\cap(-Y)=\{0\}.
\tag{2.3}
\]

Let \(H\) be the stabilizer of \(X+Y\), let \(h=|H|\), and let \(r\) and \(q\) be the numbers of \(H\)-cosets meeting \(X\) and \(-Y\), respectively. By Kneser,
\[
|X+Y|\geq (r+q-1)h.
\tag{2.4}
\]

Both collections of cosets contain \(H\). In every common \(H\)-coset other than \(H\), the portions of \(X\) and \(-Y\) are disjoint. In \(H\), they intersect only in \(0\). Hence
\[
|X|+|Y|\leq (r+q-1)h+1.
\]
Combining this with (2.4) proves (2.2). \(\square\)

### Lemma 2.2: Cayley girth bound
Let \(U\subseteq\Gamma\setminus\{0\}\), with \(d=|U|\). In the directed Cayley graph
\[
D=\operatorname{Cay}(\Gamma,U),\qquad x\longrightarrow x+u\quad(u\in U),
\]
if there is no directed cycle of length at most \(k\), then
\[
1+kd\leq |\Gamma|.
\tag{2.5}
\]
Equivalently, if \(kd\geq|\Gamma|\), then \(D\) has a directed cycle of length at most \(k\).

#### Proof
Put \(W=U\cup\{0\}\), and for \(i\geq0\) define
\[
X_i=iW=\underbrace{W+\cdots+W}_{i\text{ summands}},
\qquad X_0=\{0\}.
\]
Thus \(X_i\) consists of the vertices reachable from \(0\) by a directed walk of length at most \(i\).

For \(0\leq i\leq k-1\),
\[
X_i\cap(-W)=\{0\}.
\tag{2.6}
\]
Indeed, if \(-u\in X_i\) for some \(u\in U\), then a representation of \(-u\) by at most \(i\) elements of \(U\), followed by the step \(u\), gives a positive-length closed directed walk of length at most \(i+1\leq k\). Every closed directed walk contains a directed cycle no longer than itself, contrary to the hypothesis.

Thus \(0\) has a unique representation in \(X_i+W\). Lemma 2.1 gives
\[
|X_{i+1}|=|X_i+W|
 \geq |X_i|+|W|-1
 =|X_i|+d.
\]
Induction yields
\[
|X_k|\geq 1+kd.
\]
Since \(X_k\subseteq\Gamma\), inequality (2.5) follows. \(\square\)

### Lemma 2.3: The relevant sumset estimate
If \(S,T\) are nonempty subsets of a finite abelian group \(\Gamma\) of order \(n\), and
\[
k|T|+|S|>n,
\tag{2.7}
\]
then
\[
k|S+T|\geq n.
\tag{2.8}
\]

#### Proof
Let \(H\) be the stabilizer of \(S+T\), let \(h=|H|\), and write
\[
\sigma=\frac{|S+H|}{h},\qquad
\tau=\frac{|T+H|}{h},\qquad
m=\frac{n}{h}.
\]
Since \(|S|\leq \sigma h\) and \(|T|\leq\tau h\), condition (2.7) implies
\[
k\tau+\sigma>m.
\]
All quantities are integers, so
\[
k\tau+\sigma\geq m+1.
\tag{2.9}
\]

Kneser’s theorem gives
\[
\frac{|S+T|}{h}\geq \sigma+\tau-1.
\]
Therefore
\[
\begin{aligned}
k\frac{|S+T|}{h}
&\geq k(\sigma+\tau-1)\\
&=(k\tau+\sigma)+(k-1)\sigma-k\\
&\geq (m+1)+(k-1)-k\\
&=m,
\end{aligned}
\]
where \(\sigma\geq1\) was used. Multiplying by \(h\) proves (2.8). \(\square\)

---

## 3. Proof of the partial theorem

Set
\[
U=S+T.
\]
A two-edge directed walk
\[
a_x\longrightarrow b_{x+s}\longrightarrow a_{x+s+t}
\]
corresponds to the Cayley step
\[
x\longrightarrow x+(s+t)
\]
in \(\operatorname{Cay}(\Gamma,U)\).

If \(0\in U\), there are \(s\in S,t\in T\) with \(s+t=0\), and
\[
a_x\longrightarrow b_{x+s}\longrightarrow a_x
\]
is a directed \(2\)-cycle. We may therefore assume \(0\notin U\).

By Lemma 2.3,
\[
k|U|\geq n.
\]
Lemma 2.2 now gives a directed cycle of length \(\ell\leq k\) in
\(\operatorname{Cay}(\Gamma,U)\). For each of its increments \(u_i\in U\), choose a decomposition
\[
u_i=s_i+t_i,\qquad s_i\in S,\ t_i\in T.
\]
Replacing every Cayley step by the corresponding two-edge walk in \(G(\Gamma;S,T)\) produces a directed closed walk of length \(2\ell\leq2k\). Every directed closed walk contains a directed cycle no longer than itself. Hence \(G(\Gamma;S,T)\) has girth at most \(2k\). \(\square\)

If this graph satisfies the original degree hypotheses, then
\[
|S|\geq\beta n,\qquad |T|\geq\alpha n,
\]
and therefore
\[
k|T|+|S|\geq n(k\alpha+\beta)>n,
\]
so the theorem applies.

---

## 4. Sharpness inside this class

Take
\[
\Gamma=\mathbb Z_{k+1},\qquad S=\{0\},\qquad T=\{1\}.
\]
Then
\[
a_x\to b_x\to a_{x+1},
\]
and the whole graph is one directed cycle of length \(2(k+1)\). Moreover,
\[
k|T|+|S|=k+1=|\Gamma|.
\]
Thus the strict inequality in the partial theorem is sharp.

---

## 5. Why this does not settle the general conjecture

For a general bipartite digraph, one can form the two-step auxiliary digraph on \(A\):
\[
a\longrightarrow a'
\quad\Longleftrightarrow\quad
a\to b\to a'\ \text{for some }b\in B.
\]
Under the absence of short cycles, every vertex of this auxiliary digraph has at least \(\alpha|A|\) out-neighbors. However, the \(\beta|B|\) different choices of the intermediate vertex \(b\) need not enlarge their union: their out-neighborhoods in \(A\) may almost completely coincide. In the abelian bi-Cayley case this union is exactly the sumset \(S+T\), and Kneser’s theorem supplies the missing expansion. No analogous estimate holds for arbitrary set systems.

There is also a precise Caccetta–Häggkvist obstruction. Given any loopless digraph \(D\) on \(n\) vertices with minimum out-degree \(d\), construct a bipartite digraph by
\[
a_v\to b_v,\qquad
b_v\to a_w\ \Longleftrightarrow\ v\to w\text{ in }D.
\]
Then
\[
\beta=\frac1n,\qquad \alpha=\frac dn,
\]
and
\[
k\alpha+\beta>1
\quad\Longleftrightarrow\quad
kd\geq n.
\]
Moreover, directed cycles of length \(\ell\) in \(D\) correspond exactly to directed cycles of length \(2\ell\) in the bipartite graph. Thus even the very restricted case in which every \(A\)-vertex has one prescribed out-neighbor contains the ordinary Caccetta–Häggkvist problem.

Accordingly, the argument above is a complete proof for the abelian translation-invariant case, but it does not overcome the non-homogeneous neighborhood-overlap issue in the full conjecture.