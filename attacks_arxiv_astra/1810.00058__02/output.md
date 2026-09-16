```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "I prove the conjecture for linear forests and establish necessary exponent bounds, including s ≥ 2 whenever H contains a triangle.",
  "would_publish": false,
  "caveats": "No general proof or counterexample is obtained, and no novelty or optimality is claimed for these partial results."
}
```

## 1. Results obtained

For disjoint vertex sets \(A,B\), write \(e(A,B)\) for the number of edges between them. Thus a \(c\)-sparse pair satisfies
\[
e(A,B)\le c|A||B|.
\]
The positive result below assumes \(\Delta(G)\le \varepsilon |G|\); the negative constructions satisfy the strict inequality, so either convention for “\(\varepsilon\)-bounded” is covered.

I establish the following partial results.

### A. Necessary bounds on the exponent

Define
\[
\beta(H)=
\max\left(
\{0\}\cup
\left\{
\frac{e(J)-v(J)+1}{v(J)-2}:
J\subseteq H,\ v(J)\ge3
\right\}
\right),
\]
where \(J\subseteq H\) means an ordinary, not necessarily induced, subgraph.

If the conjecture holds for \(H\) with parameters \(\varepsilon,s>0\), then
\[
\boxed{s\ge \beta(H).}
\]
In addition, if \(H\) contains a triangle, then
\[
\boxed{s\ge2.}
\]

For example, for \(r\ge3\), any admissible exponent for \(H=K_r\) must satisfy
\[
s\ge \max\left\{2,\frac{r-1}{2}\right\}.
\]
For a cycle \(C_\ell\), the first bound gives \(s\ge1/(\ell-2)\).

These are obstructions to particular exponents, **not counterexamples to the conjecture**, which is allowed to choose a larger exponent depending on \(H\).

### B. A positive special case

If \(H\) is a linear forest with \(h\ge2\) vertices and \(r\) components, put
\[
k=h+r-1.
\]
Then the conjecture holds with
\[
\boxed{\varepsilon=\frac1{8k},\qquad s=1.}
\]
In fact, under these hypotheses there are anticomplete sets \(A,B\) with
\[
|A|,|B|\ge \frac{|G|}{4},
\]
so any positive \(s\) works with this \(\varepsilon\).

The proofs follow.

---

## 2. A general exponent obstruction by random edge alteration

Suppose
\[
0<s<\beta(H).
\]
Fix \(\varepsilon>0\). We may assume \(\varepsilon\le1/4\): decreasing \(\varepsilon\) preserves any asserted instance of the conjecture.

Choose \(J\subseteq H\), with \(h=v(J)\ge3\) and \(m=e(J)\), such that
\[
s<\frac{m-h+1}{h-2}.
\]
Equivalently,
\[
\frac{h-2}{m-1}<\frac1{s+1}.
\]
Choose
\[
\frac{h-2}{m-1}<\alpha<\frac1{s+1},
\qquad p=N^{-\alpha}.
\]
Let \(F\) be the binomial random graph \(G(N,p)\).

### Uniform lower density in \(F\)

With probability tending to one,
\[
\Delta(F)\le2Np,
\]
because \(Np\) grows as a positive power of \(N\).

Also, with probability tending to one, every two disjoint sets satisfying
\[
|A|\ge \frac{\varepsilon}{2}4^{-s}p^sN,
\qquad
|B|\ge \frac{\varepsilon}{2}N
\tag{1}
\]
satisfy
\[
e_F(A,B)\ge\frac p2|A||B|.
\tag{2}
\]

Indeed, for fixed disjoint \(A,B\), the usual binomial lower-tail estimate gives
\[
\Pr\left(e_F(A,B)<\frac p2|A||B|\right)
\le \exp\left(-\frac{p|A||B|}{8}\right).
\]
There are at most \(3^N\) ordered disjoint pairs. Under (1),
\[
p|A||B|=\Omega_{\varepsilon,s}(N^2p^{s+1}),
\]
and
\[
Np^{s+1}=N^{1-\alpha(s+1)}\longrightarrow\infty.
\]
Consequently, the union bound proves (2) simultaneously for all such pairs.

### Removing all copies of \(J\)

Let \(D\) be the set of edges of \(F\) that belong to at least one ordinary copy of \(J\). If \(Y\) counts labelled copies of \(J\), then
\[
|D|\le mY,
\qquad
\mathbb E Y\le N^hp^m.
\]

Set \(\eta=\varepsilon/16\), and let
\[
X=\{v:\deg_D(v)>\eta Np\}.
\]
Then
\[
|X|\le \frac{2|D|}{\eta Np},
\]
so
\[
\mathbb E|X|
\le \frac{2m}{\eta}N^{h-1}p^{m-1}
=\frac{2m}{\eta}N\bigl(N^{h-2}p^{m-1}\bigr)
=o(N).
\]
The last equality follows from \(\alpha>(h-2)/(m-1)\).

Thus, with probability tending to one, \(|X|\le N/2\). Choose a realization satisfying this, the maximum-degree bound, and (2). Delete all edges in \(D\), and then delete the vertices in \(X\). Call the resulting graph \(G\), and write \(n=|G|\). We have
\[
n\ge N/2.
\]

The graph \(G\) contains no ordinary copy of \(J\), hence no induced copy of \(H\). Moreover,
\[
\Delta(G)\le2Np\le4pn<\varepsilon n
\]
for sufficiently large \(N\).

### No pair of the required size

Set
\[
c=\frac p4.
\]
Suppose disjoint \(A,B\subseteq V(G)\) satisfy
\[
|A|\ge\varepsilon c^s n,\qquad |B|\ge\varepsilon n.
\]
They satisfy (1). Each vertex of \(A\) is incident with at most \(\eta Np\) deleted edges, so
\[
\begin{aligned}
e_G(A,B)
&\ge \frac p2|A||B|-\eta Np|A|\\
&\ge \left(\frac12-\frac{2\eta}{\varepsilon}\right)p|A||B|\\
&=\frac{3p}{8}|A||B|\\
&>c|A||B|.
\end{aligned}
\]
Thus \(G\) has no \(c\)-sparse pair of the required sizes.

This works for every fixed \(\varepsilon>0\), proving
\[
s\ge\beta(H)
\]
for any admissible exponent.

---

## 3. An explicit triangle-free obstruction giving \(s\ge2\)

The following algebraic family gives a stronger obstruction whenever \(H\) contains a triangle.

### Construction

Let \(q=2^k\ge8\), let \(F=\mathbb F_q\), and let
\[
\operatorname{Tr}:F\longrightarrow\mathbb F_2
\]
be the absolute trace.

Define
\[
S=
\left\{
(x,tx,tx^2):
t\in F^\times,\ 
\operatorname{Tr}(t^2x)=1
\right\}
\subseteq F^3.
\]
Let \(G_q\) be the Cayley graph of the additive group \(F^3\) with connection set \(S\).

The trace condition implies \(x\ne0\), so \(0\notin S\). Since the characteristic is two, \(S=-S\), and the graph is simple and undirected. Different parameter pairs give different elements of \(S\). For each nonzero \(t\), exactly \(q/2\) choices of \(x\) satisfy the trace condition. Therefore
\[
n_q=q^3,\qquad d_q=\frac{q(q-1)}2.
\tag{3}
\]

### Triangle-freeness

A triangle would give \(s_1,s_2,s_3\in S\) with
\[
s_1+s_2=s_3.
\]
Write
\[
s_1=(x,tx,tx^2),\quad
s_2=(y,uy,uy^2),\quad
s_3=(x+y,v(x+y),v(x+y)^2).
\]
Here \(x,y,x+y\) are nonzero.

The second-coordinate equation, multiplied by \(x+y\), and the third-coordinate equation imply
\[
xy(t+u)=0.
\]
Thus \(t=u\), and the second-coordinate equation then gives \(v=t\). But
\[
\operatorname{Tr}(t^2(x+y))
=
\operatorname{Tr}(t^2x)+\operatorname{Tr}(t^2y)
=1+1=0,
\]
contrary to \(s_3\in S\). Hence \(G_q\) is triangle-free.

### Eigenvalue estimate

The additive characters of \(F^3\) are
\[
\chi_{a,b,c}(u,v,w)
=(-1)^{\operatorname{Tr}(au+bv+cw)}.
\]
They form an eigenbasis for this Cayley graph.

Using
\[
\operatorname{Tr}(ct\,x^2)
=\operatorname{Tr}\bigl((ct)^{q/2}x\bigr),
\]
put
\[
L_t=a+bt+(ct)^{q/2}.
\]
Character orthogonality gives
\[
\sum_{\operatorname{Tr}(t^2x)=1}
(-1)^{\operatorname{Tr}(L_tx)}
=
\frac q2
\left(\mathbf 1_{L_t=0}-\mathbf 1_{L_t=t^2}\right).
\]
Therefore the corresponding eigenvalue is
\[
\theta_{a,b,c}=\frac q2(N_0-N_1),
\]
where \(N_0,N_1\) count nonzero \(t\) satisfying \(L_t=0\) and \(L_t=t^2\), respectively.

For \((a,b,c)\ne(0,0,0)\), squaring \(L_t=0\) gives the nonzero polynomial equation
\[
b^2t^2+ct+a^2=0,
\]
so \(N_0\le2\). Squaring \(L_t=t^2\) gives
\[
t^4+b^2t^2+ct+a^2=0,
\]
so \(N_1\le4\). Consequently every nontrivial eigenvalue satisfies
\[
|\theta_{a,b,c}|\le2q.
\tag{4}
\]

### Excluding \(c\)-sparse pairs

Put
\[
p_q=\frac{d_q}{n_q}=\frac{q-1}{2q^2},
\qquad
c_q=\frac{p_q}{2}.
\]
From (4), the expander-mixing estimate gives, for disjoint nonempty \(A,B\),
\[
\frac{e(A,B)}{|A||B|}
\ge p_q-\frac{2q}{\sqrt{|A||B|}}.
\tag{5}
\]

Fix \(\varepsilon>0\) and \(0<s<2\). If
\[
|A|\ge\varepsilon c_q^s n_q,
\qquad
|B|\ge\varepsilon n_q,
\]
then the error term in (5) is at most
\[
\frac{2q}{\varepsilon c_q^{s/2}q^3}
=\frac{2}{\varepsilon q^2c_q^{s/2}}
=o(c_q).
\]
Indeed, \(c_q\sim1/(4q)\), and the ratio of this error to \(c_q\) is
\[
O_{\varepsilon,s}(q^{s/2-1})\longrightarrow0.
\]
For sufficiently large \(q\), therefore,
\[
\frac{e(A,B)}{|A||B|}>p_q-c_q=c_q.
\]
No pair of the stipulated sizes is \(c_q\)-sparse.

At the same time,
\[
\frac{\Delta(G_q)}{n_q}=p_q\longrightarrow0,
\]
so \(G_q\) is \(\varepsilon\)-bounded for sufficiently large \(q\). Since it is triangle-free, it is \(H\)-free for every \(H\) containing a triangle.

Thus every admissible exponent for such an \(H\) satisfies \(s\ge2\).

---

## 4. Positive result for linear forests

We first prove an induced-path separator lemma.

### Lemma

If \(G\) is \(P_k\)-free, where \(k\ge2\), then there is a possibly empty induced path \(P\), with at most \(k-1\) vertices, such that every component of
\[
G-N[P]
\]
has at most \(|G|/2\) vertices.

#### Proof

If every component of \(G\) already has at most \(|G|/2\) vertices, take \(P\) empty.

Otherwise let \(C_0\) be the unique larger component and choose \(v_1\in C_0\). Grow an induced path \(v_1,\ldots,v_i\), continuing whenever
\[
G-N[\{v_1,\ldots,v_i\}]
\]
has a component \(C_i\) of size greater than \(|G|/2\).

For the first extension, connectivity of \(C_0\) gives a vertex \(v_2\in N(v_1)\cap C_0\) adjacent to \(C_1\).

For subsequent extensions, the large components are nested:
\[
C_i\subseteq C_{i-1}.
\]
The previous choice ensures that \(v_i\) has a neighbour in \(C_{i-1}\). Since \(C_{i-1}\) is connected, there is a vertex
\[
v_{i+1}\in N(v_i)\cap C_{i-1}
\]
adjacent to \(C_i\). Membership in \(C_{i-1}\) ensures that \(v_{i+1}\) is nonadjacent to \(v_1,\ldots,v_{i-1}\). Thus the path remains induced.

If this process did not stop with at most \(k-1\) vertices, it would construct an induced \(P_k\), a contradiction. ∎

### Proposition

If \(G\) is \(P_k\)-free, \(n=|G|>1\), and
\[
\Delta(G)\le \frac{n}{8k},
\]
then \(G\) has anticomplete sets \(A,B\) with
\[
|A|,|B|\ge n/4.
\]

#### Proof

If \(\Delta(G)=0\), split the vertex set as evenly as possible.

Otherwise apply the lemma and set \(S=N[P]\). Since \(\Delta(G)\ge1\),
\[
|S|
\le(k-1)(\Delta(G)+1)
\le2(k-1)\Delta(G)
\le\frac{k-1}{4k}n
<\frac n4.
\]
Thus \(G-S\) has more than \(3n/4\) vertices, and all its components have size at most \(n/2\).

If one component has size between \(n/4\) and \(n/2\), take it as \(A\), and take all other components as \(B\). Otherwise, accumulate components until their union first has size at least \(n/4\). This union has size less than \(n/2\); take it as \(A\) and all remaining components as \(B\).

In either case, \(A,B\) are anticomplete and both have size at least \(n/4\). ∎

### Application to linear forests

Let \(H\) be a linear forest with \(h\ge2\) vertices and \(r\) components. By inserting one unused vertex between successive path components, \(H\) is an induced subgraph of
\[
P_{h+r-1}.
\]
Consequently, every \(H\)-free graph is \(P_{h+r-1}\)-free.

Set \(k=h+r-1\) and \(\varepsilon=1/(8k)\). The proposition gives anticomplete \(A,B\) of sizes at least \(n/4\). For every \(c\in[0,1]\) and every \(s>0\),
\[
|A|\ge\varepsilon c^s n,\qquad |B|\ge\varepsilon n.
\]
This proves the asserted special case, including \(c=0\). Graphs \(H\) with at most one vertex are vacuous under the hypothesis \(|G|>1\).

---

## 5. Remaining gap

The positive argument depends on induced paths giving small balanced separators. It does not provide the required polynomial \(c\)-dependence for arbitrary forbidden induced subgraphs.

The constructions show that the exponent cannot be chosen independently of \(H\), and that even \(H=K_3\) requires \(s\ge2\). But every bound established here is finite for fixed \(H\), so none contradicts the original existential statement. A general proof or a counterexample remains beyond these arguments.