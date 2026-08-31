```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds when \(G\) can be made bipartite by deleting \(O(\sqrt m)\) vertices, via a quantitative dense embedding lemma and color elimination.",
  "would_publish": false,
  "caveats": "Graphs with odd-cycle transversal much larger than \u221am remain untreated, and no counterexample or complete proof is obtained."
}
```

## 1. Statement and partial result

Write \(r_q(G)\) for the least \(N\) such that every \(q\)-edge-coloring of \(K_N\) contains a monochromatic copy of \(G\). Let
\[
\operatorname{oct}(G)=\min\{|S|:G-S\text{ is bipartite}\}
\]
be the odd-cycle transversal number.

The following gives a parameterized version of the conjectured estimate.

### Theorem
For every fixed \(q\ge 2\), there is a constant \(C_q\) such that every graph \(G\) with \(m\ge1\) edges and no isolated vertices satisfies
\[
\boxed{\quad r_q(G)\le 2^{C_q\left(\sqrt m+\operatorname{oct}(G)\right)}.\quad}
\]

Consequently, the conjectured bound
\[
r_q(G)\le 2^{C'_q\sqrt m}
\]
holds for every \(G\) satisfying
\[
\operatorname{oct}(G)\le \sqrt m,
\]
and more generally for any class with \(\operatorname{oct}(G)=O(\sqrt m)\) with a uniform implied constant. In particular, it holds for all bipartite graphs.

The proof has two ingredients.

---

## 2. Dense graphs contain every prescribed bipartite graph at the required scale

All copies below are non-induced.

### Lemma 1
Let \(H\) be a bipartite graph with \(h\) vertices and \(e\ge1\) edges, and put
\[
s=\left\lceil\sqrt e\right\rceil.
\]
For \(0<\delta\le1\), every graph \(\Gamma\) on at least
\[
M_\delta(H)
 =
 \left\lceil
 1024\,\delta^{-4}h^2
 \left(128\,\delta^{-3}\right)^s
 \right\rceil
\]
vertices and having at least \(\delta\binom{N}{2}\) edges contains \(H\).

If \(e=0\), one may take \(M_\delta(H)=h\).

### Proof

Assume \(e\ge1\), and let \(N=|V(\Gamma)|\). Choose a maximum cut \(V(\Gamma)=X\cup Y\). At least half of the edges of \(\Gamma\) cross this cut, so
\[
e_\Gamma(X,Y)
 \ge \frac{\delta}{2}\binom N2
 =\frac{\delta N(N-1)}4
 \ge \frac{\delta N^2}{8}.
\]
It follows that
\[
|X|,|Y|\ge \frac{\delta N}{8},
\]
and the density of the bipartite graph between \(X\) and \(Y\) is at least \(\delta/2\).

Put
\[
p=\frac{\delta}{4}
\]
and let
\[
X_1=\{x\in X:d_Y(x)\ge p|Y|\}.
\]
Since the \(X,Y\)-density is at least \(2p\),
\[
|X_1|\ge p|X|\ge \frac{\delta^2N}{32}.
\]
Set
\[
c=\frac{\delta^2}{32},\qquad \beta=\frac{\delta}{8},
\]
so that
\[
|X_1|\ge cN,\qquad |Y|\ge\beta N.
\]

Fix a bipartition \(V(H)=A\cup B\). Let
\[
B_+=\{b\in B:d_H(b)>s\},\qquad t=|B_+|.
\]
Since \(t(s+1)\le e\) and \(s^2\ge e\), we have \(t\le s\).

The displayed lower bound on \(N\) ensures \(p|Y|\ge2s\). Averaging over all \(t\)-subsets \(T\subseteq Y\), we have
\[
\begin{aligned}
\frac{1}{\binom{|Y|}{t}}
\sum_{T\in\binom Yt}|N_\Gamma(T)\cap X_1|
&=
\sum_{x\in X_1}
\frac{\binom{d_Y(x)}t}{\binom{|Y|}t}\\
&\ge |X_1|\left(\frac p2\right)^t.
\end{aligned}
\]
Thus there is a \(t\)-set \(T\subseteq Y\) whose common neighborhood
\[
X_0=N_\Gamma(T)\cap X_1
\]
satisfies
\[
|X_0|
 \ge cN\left(\frac p2\right)^t
 \ge cN\left(\frac p2\right)^s.
\]
Every vertex of \(X_0\) still has at least \(p|Y|\) neighbors in \(Y\).

We now use dependent random choice. Choose \(2s\) vertices of \(Y\) independently and uniformly, with repetition, and let \(U\subseteq X_0\) be their common neighborhood. Then
\[
\mathbb E|U|
 =\sum_{x\in X_0}
 \left(\frac{d_Y(x)}{|Y|}\right)^{2s}
 \ge p^{2s}|X_0|.
\]
By the choice of \(N\),
\[
\begin{aligned}
p^{2s}|X_0|
&\ge cN\left(\frac{p^3}{2}\right)^s\\
&=
cN\left(\frac{\delta^3}{128}\right)^s\\
&\ge 32\delta^{-2}h^2
\ge4h.
\end{aligned}
\]

Call an \(s\)-set \(S\subseteq X_0\) bad if
\[
|N_\Gamma(S)\cap Y|<2h.
\]
Let \(Z\) be the number of bad \(s\)-sets contained in \(U\). Then
\[
\begin{aligned}
\mathbb EZ
&\le \binom{|X_0|}{s}
 \left(\frac{2h}{|Y|}\right)^{2s}\\
&\le N^s\left(\frac{2h}{\beta N}\right)^{2s}\\
&=
\left(\frac{4h^2}{\beta^2N}\right)^s
\le1,
\end{aligned}
\]
where the last inequality follows from
\[
N\ge 256\delta^{-2}h^2=\frac{4h^2}{\beta^2}.
\]

Hence some outcome satisfies
\[
|U|-Z\ge4h-1.
\]
Delete one vertex from every bad \(s\)-set contained in \(U\). This leaves a set \(U'\subseteq U\) with
\[
|U'|\ge4h-1
\]
such that every \(s\)-subset of \(U'\) has at least \(2h\) common neighbors in \(Y\).

Embed \(A\) arbitrarily and injectively into \(U'\). Map the vertices of \(B_+\) bijectively onto \(T\). Since \(X_0\subseteq N_\Gamma(T)\), all required edges between \(A\) and \(B_+\) are present.

Every remaining vertex \(b\in B\setminus B_+\) has degree at most \(s\). Pad the image of \(N_H(b)\) to an \(s\)-subset of \(U'\). It therefore has at least \(2h\) common neighbors in \(Y\). We may greedily embed all vertices of \(B\setminus B_+\), avoiding \(T\) and previously used vertices. At every step fewer than \(h\) vertices of \(Y\) are forbidden.

This embeds \(H\) in \(\Gamma\). ∎

For fixed \(\delta\), Lemma 1 gives
\[
\log M_\delta(H)=O_\delta(\sqrt e+\log h).
\]

---

## 3. Lifting through a small exceptional vertex set

The next lemma turns dense unavoidability of \(H\) into a multicolor Ramsey bound for any graph obtained from \(H\) by adding a small number of arbitrary vertices.

### Lemma 2
Fix \(q\ge2\) and put
\[
\delta=\frac1{4q}.
\]
Suppose every graph on at least \(M\) vertices and of density at least \(\delta\) contains \(H\). Let \(G\) have a vertex set \(S\) of size \(k\) such that \(G-S=H\). Then
\[
r_q(G)
 \le
 \left\lceil
 (2q)^{q^2k}\max\{M,4\}
 \right\rceil.
\]

### Proof

Let
\[
N=(2q)^{q^2k}\max\{M,4\},
\]
and consider a \(q\)-coloring of \(K_N\). Suppose for contradiction that it contains no monochromatic \(G\).

We use an iterative focusing argument. At any stage, some colors have been declared excluded. For each excluded color \(a\), we have already found:

- a set \(A_a\) of \(k\) vertices forming an \(a\)-colored clique, and
- a current reservoir \(W\) such that all edges between \(A_a\) and \(W\) have color \(a\).

Therefore, under the assumption that there is no monochromatic \(G\), the color-\(a\) graph induced on \(W\) cannot contain \(H\).

Suppose the current reservoir is \(W\), with \(|W|=w\ge\max\{M,4\}\). Each excluded color induces an \(H\)-free graph on \(W\), and hence has fewer than
\[
\delta\binom w2
\]
edges there. Thus the average total degree in all excluded colors is less than
\[
q\delta(w-1)\le\frac w4.
\]
Choose \(v\in W\) whose total excluded-color degree is at most \(w/4\). At least
\[
w-1-\frac w4\ge\frac w2
\]
edges from \(v\) to \(W\setminus\{v\}\) have active colors. One active color occurs on at least \(w/(2q)\) of these edges. Replace \(W\) by that monochromatic neighborhood and record \(v\) together with the chosen active color.

Perform \(qk\) such focusing steps. Among the \(qk\) recorded vertices, some active color \(c\) occurs at least \(k\) times. The corresponding \(k\) vertices form a \(c\)-colored clique and are \(c\)-complete to the final reservoir \(R\).

If the color-\(c\) graph on \(R\) contains \(H\), then these \(k\) vertices together with that copy of \(H\) give a monochromatic copy of \(G\): extra edges cause no difficulty because copies are not induced. Otherwise declare \(c\) excluded, retain its \(k\) focusing vertices, and repeat.

At most \(q\) stages are possible, and each stage uses \(qk\) focusing steps. Thus at all times the reservoir has size at least
\[
\frac{N}{(2q)^{q^2k}}\ge\max\{M,4\}.
\]

If every color is eventually excluded, then every color graph on the final reservoir is \(H\)-free. Hence
\[
\binom w2
 =
 \sum_{a=1}^q e_a(W)
 <
 q\delta\binom w2
 =
 \frac14\binom w2,
\]
a contradiction.

For \(k=0\), one simply chooses a color of density at least \(1/q>\delta\). ∎

---

## 4. Proof of the partial theorem

Let \(S\) be an odd-cycle transversal of \(G\), with
\[
k=|S|=\operatorname{oct}(G),
\]
and put \(H=G-S\). Then \(H\) is bipartite.

Let \(h=v(H)\) and \(e=e(H)\). Apply Lemma 1 with
\[
\delta=\frac1{4q}.
\]
For fixed \(q\),
\[
\log M_\delta(H)
 =
 O_q(\sqrt e+\log(h+1)).
\]
Lemma 2 now gives
\[
\log r_q(G)
 \le
 q^2k\log(2q)
 +
 O_q(\sqrt e+\log(h+1)).
\]
Since \(e\le m\), and since \(G\) has no isolated vertices,
\[
v(G)\le2m,
\]
so \(h\le2m\) and
\[
\log(h+1)=O(\sqrt m).
\]
Therefore
\[
\log r_q(G)
 \le C_q\bigl(k+\sqrt m\bigr),
\]
which proves
\[
r_q(G)\le2^{C_q(\operatorname{oct}(G)+\sqrt m)}.
\]

---

## 5. Sharpness within the bipartite case

The \(\sqrt m\) exponent cannot be improved in general, even for bipartite graphs.

Take \(H=K_{t,t}\), so \(m=t^2\). In a uniformly random \(q\)-coloring of \(K_N\), a fixed copy of \(K_{t,t}\) is monochromatic with probability
\[
q^{1-t^2}.
\]
There are at most \(N^{2t}\) labeled copies. With
\[
N=\left\lfloor q^{t/4}\right\rfloor,
\]
the expected number of monochromatic copies is at most
\[
N^{2t}q^{1-t^2}
 \le q^{t^2/2+1-t^2}
 =q^{1-t^2/2}<1
\]
for \(t\ge2\). Hence
\[
r_q(K_{t,t})>q^{t/4}=2^{\Omega_q(\sqrt m)}.
\]

Thus the partial result has the correct exponential order on bipartite targets.

---

## 6. Remaining gap

The argument depends essentially on \(G-S\) being bipartite. An \(H\)-free graph is then sparse once its order exceeds \(2^{O(\sqrt{e(H)})}\), allowing a failed color to be eliminated. This is false for non-bipartite \(H\): a complete bipartite graph is \(H\)-free and has density asymptotic to \(1/2\).

Consequently, the proof does not cover graphs with
\[
\operatorname{oct}(G)\gg\sqrt m.
\]
For example, \(tK_3\) has \(m=3t\) and odd-cycle transversal number \(t\). This is only a limitation of the method, not evidence for a counterexample: \(tK_3\) itself has a linear multicolor Ramsey bound by greedily finding vertex-disjoint monochromatic triangles and pigeonholing their colors.

No full proof or counterexample to the catalog conjecture is obtained. The special-case argument is self-contained, but I have not verified whether this precise odd-cycle-transversal formulation already appears in the literature.