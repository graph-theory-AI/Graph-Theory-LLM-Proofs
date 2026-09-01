```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture is proved here for every threshold graph, with the explicit exponent d=2|H|-1, via a closure theorem for adjoining universal or isolated vertices.",
  "would_publish": false,
  "caveats": "The argument does not handle general prime graphs, and the reported converse implication from Erdős-Hajnal to virality is not reproved."
}
```

# Mathematical writeup

## 1. Statement and conventions

Let \(H\) be a fixed nonempty finite simple graph with \(h=|H|\). A set \(X\subseteq V(G)\) is called \(\varepsilon\)-restricted if either
\[
\Delta(G[X])\leq \varepsilon |X|
\]
or
\[
\Delta(\overline{G}[X])\leq \varepsilon |X|.
\]

The conjecture asserts that some \(d>0\) satisfies: for every \(0<\varepsilon<1/2\), if
\[
\operatorname{ind}_H(G)\leq (\varepsilon^d |G|)^h,
\]
then \(G\) has an \(\varepsilon\)-restricted set of order at least \(\varepsilon^d|G|\).

I count induced copies by their vertex sets. If \(\operatorname{ind}_H\) instead denotes labelled induced embeddings, all lower bounds below remain valid, since every induced \(H\)-set supports at least one embedding.

## 2. Elementary observations

### 2.1 Complementation

If \(H\) is viral with exponent \(d\), then \(\overline H\) is viral with the same exponent. Indeed,
\[
\operatorname{ind}_{\overline H}(G)=\operatorname{ind}_{H}(\overline G),
\]
and a set is \(\varepsilon\)-restricted in \(G\) if and only if it is \(\varepsilon\)-restricted in \(\overline G\).

### 2.2 Larger exponents remain valid

If \(H\) is viral with exponent \(d\), it is viral with every \(d'\geq d\). This follows from
\[
\varepsilon^{d'}\leq \varepsilon^d
\qquad (0<\varepsilon<1).
\]

## 3. Closure under adjoining a universal or isolated vertex

### Lemma

Let \(F\) be a graph on \(k\geq1\) vertices that is viral with exponent \(d>0\). Let \(H\) be obtained from \(F\) by adjoining one new vertex that is either adjacent to every vertex of \(F\), or adjacent to no vertex of \(F\). Then \(H\) is viral with exponent
\[
D=d+2.
\]

### Proof

Fix \(0<\varepsilon<1/2\), let \(n=|G|\), and suppose
\[
\operatorname{ind}_{H}(G)\leq
(\varepsilon^{D}n)^{k+1}.
\]
Set
\[
\rho=\varepsilon^{D}.
\]
Assume for a contradiction that \(G\) has no \(\varepsilon\)-restricted set of size at least \(\rho n\).

If \(\rho n\leq1\), then any singleton is an \(\varepsilon\)-restricted set of size at least \(\rho n\). Thus
\[
\rho n>1.
\]
Since \(D=d+2>2\) and \(\varepsilon<1/2\), this in particular gives \(n>4\).

Let
\[
r=\left\lfloor \frac n2\right\rfloor .
\]
We construct vertices \(v_1,\dots,v_r\). Before choosing \(v_i\), let
\[
S_i=V(G)\setminus\{v_1,\dots,v_{i-1}\}.
\]
Then \(|S_i|>n/2\). Also \(\rho<1/4\), so \(|S_i|\geq\rho n\). Hence \(S_i\) is not \(\varepsilon\)-restricted, and therefore
\[
\Delta(G[S_i])>\varepsilon |S_i|
\quad\text{and}\quad
\Delta(\overline G[S_i])>\varepsilon |S_i|.
\]

If the new vertex of \(H\) is universal over \(F\), choose \(v_i\in S_i\) with
\[
\deg_{G[S_i]}(v_i)>\varepsilon |S_i|,
\]
and let \(A_i=N_{G[S_i]}(v_i)\).

If the new vertex is isolated from \(F\), choose \(v_i\in S_i\) with
\[
\deg_{\overline G[S_i]}(v_i)>\varepsilon |S_i|,
\]
and let \(A_i\) be the set of nonneighbors of \(v_i\) in \(S_i\setminus\{v_i\}\).

In either case, writing \(a_i=|A_i|\),
\[
a_i>\varepsilon |S_i|>\frac{\varepsilon n}{2}. \tag{1}
\]

We claim that
\[
\operatorname{ind}_F(G[A_i])>
(\varepsilon^d a_i)^k. \tag{2}
\]
Otherwise, virality of \(F\) would give an \(\varepsilon\)-restricted set \(Y\subseteq A_i\) with
\[
|Y|\geq \varepsilon^d a_i
  >\frac12\varepsilon^{d+1}n
  >\varepsilon^{d+2}n
  =\rho n,
\]
where the penultimate inequality uses \(\varepsilon<1/2\). This contradicts the assumed absence of such a set in \(G\). Thus (2) holds.

Every induced copy of \(F\) in \(A_i\), together with \(v_i\), induces a copy of \(H\). These copies are distinct for different \(i\): a copy produced at step \(i\) contains \(v_i\), whereas every copy produced at a later step lies in \(S_{i+1}\), which no longer contains \(v_i\). Consequently,
\[
\begin{aligned}
\operatorname{ind}_H(G)
&\geq \sum_{i=1}^{r}\operatorname{ind}_F(G[A_i])\\
&> r\,\varepsilon^{dk}\left(\frac{\varepsilon n}{2}\right)^k\\
&\geq \frac{1}{3\cdot 2^k}\,
   \varepsilon^{k(d+1)}n^{k+1},
\end{aligned}
\]
using \(r\geq n/3\).

On the other hand,
\[
(\varepsilon^D n)^{k+1}
=
\varepsilon^{k(d+1)}
\varepsilon^{d+k+2}n^{k+1}.
\]
Because \(0<\varepsilon<1/2\),
\[
\varepsilon^{d+k+2}
<
2^{-(d+k+2)}
<
\frac{1}{3\cdot 2^k};
\]
the last inequality is equivalent to \(2^{d+2}>3\), which holds since \(d>0\). Therefore
\[
\operatorname{ind}_H(G)>
(\varepsilon^D n)^{k+1},
\]
contrary to the hypothesis. This proves the lemma. \(\square\)

### Corollary

If \(F\) is viral with exponent \(d\), and \(H\) is obtained from \(F\) by a sequence of \(t\) additions, each new vertex being universal or isolated relative to the graph constructed so far, then \(H\) is viral with exponent
\[
d+2t.
\]

## 4. Threshold graphs

Recall that a threshold graph is obtained from \(K_1\) by repeatedly adjoining either a universal vertex or an isolated vertex.

### Theorem

Every threshold graph \(H\) is viral. More precisely, if \(h=|H|\), then Conjecture 1.8 holds for \(H\) with
\[
d=2h-1.
\]

### Proof

The graph \(K_1\) is viral with exponent \(1\): for every nonempty \(G\),
\[
\operatorname{ind}_{K_1}(G)=|G|>\varepsilon |G|,
\]
so the premise of the viral implication never holds. The empty ambient graph is harmless.

Starting with exponent \(1\), apply the preceding lemma for each of the \(h-1\) universal/isolated vertex additions. The resulting exponent is
\[
1+2(h-1)=2h-1.
\]
\(\square\)

In particular, every graph on at most three vertices is threshold, so the conjecture holds for all such \(H\); the above bound gives \(d=5\) when \(|H|=3\).

## 5. Why the universal statement remains out of reach

The following direction of the reported equivalence is short and self-contained.

### Proposition

If \(H\) is viral with exponent \(d\), then \(H\) has the Erdős–Hajnal property. One may take Erdős–Hajnal exponent
\[
c=\frac{1}{2(d+1)}.
\]

### Proof

Let \(G\) be an \(H\)-free graph on \(n\) vertices. Put
\[
a=\frac1{d+1}.
\]
For \(n\geq 2^{2/a}\), take
\[
\varepsilon=n^{-a}<\frac12.
\]
Since \(\operatorname{ind}_H(G)=0\), virality gives an \(\varepsilon\)-restricted set \(X\) with
\[
m:=|X|\geq \varepsilon^d n=n^a.
\]

If \(\Delta(G[X])\leq\varepsilon m\), the greedy bound gives
\[
\alpha(G[X])
\geq \frac{m}{\varepsilon m+1}
=\frac{1}{\varepsilon+1/m}
\geq \frac{1}{2\varepsilon}
=\frac12 n^a
\geq n^{a/2}.
\]
If instead \(\Delta(\overline G[X])\leq\varepsilon m\), the same argument in the complement gives a clique of order at least \(n^{a/2}\).

For \(2\leq n<2^{2/a}\), every pair of vertices is either a clique or a stable set, and
\[
n^{a/2}<2.
\]
The case \(n=1\) is immediate. Thus \(H\) has the Erdős–Hajnal property with exponent \(a/2\). \(\square\)

The supplied literature record attributes the converse—Erdős–Hajnal implies virality—to Bucić, Fox, and Pham. I have not reconstructed that direction here. Accepting the reported theorem, the full conjecture is equivalent to the full Erdős–Hajnal conjecture.

## 6. Remaining gap

The closure lemma only applies when \(H\) has a vertex that is universal or isolated relative to the remaining graph. Consequently it proves the conjecture for threshold graphs and, more generally, for graphs obtained by such extensions from any already-viral core. It does not address genuinely prime graphs, where no such elimination is possible. No proof or counterexample for arbitrary \(H\) is obtained.