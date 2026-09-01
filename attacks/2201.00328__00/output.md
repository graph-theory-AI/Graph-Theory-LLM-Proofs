```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjectured bound holds when the labeled-speed coefficient is strictly below 2 and also for every edge-monotone or coedge-monotone factorial hereditary family.",
  "would_publish": false,
  "caveats": "The general case with arbitrary constant in 2^{O(n log n)} remains open; the arguments use labeled speed."
}
```

# Partial results toward the question

Throughout, graphs are finite and simple, and \(\log=\log_2\). I use the standard labeled speed
\[
f(n)=|\{G\in\mathcal F:V(G)=[n]\}|.
\]
An implicit representation means an adjacency-labeling scheme with a decoder depending only on \(\mathcal F\), not on the particular graph.

The full \(O(\sqrt n\log n)\) assertion is not proved below. I establish:

1. a quantitative upper bound in terms of the leading constant in the factorial speed;
2. the desired bound for all factorial classes that are monotone under edge deletion or edge addition;
3. an \(O(\sqrt n\log^3 n)\) bound at one natural critical speed threshold.

## 1. A quantitative bound from the speed coefficient

Define
\[
\rho(\mathcal F)
 =\limsup_{n\to\infty}
   \frac{\log f(n)}{n\log n}.
\]

### Theorem 1

Let \(\mathcal F\) be hereditary and suppose \(\rho(\mathcal F)<\infty\). For every real
\[
d>\max\{1,\rho(\mathcal F)\},
\]
the class \(\mathcal F\) admits an implicit representation of size
\[
O_{\mathcal F,d}\!\left(n^{1-1/d}\log^2 n\right).
\]

Consequently, if
\[
\rho(\mathcal F)<2,
\]
then \(\mathcal F\) admits labels of size \(O(\sqrt n\log n)\).

The proof has two ingredients.

### Lemma 1: factorial speed bounds simultaneous neighborhood traces

Suppose that, for all sufficiently large \(m\),
\[
f(m)\le m^{am}.
\]
For every \(d>\max\{1,a\}\), there is a constant \(C=C(\mathcal F,d)\) such that for every \(G\in\mathcal F\), every \(S\subseteq V(G)\) of size \(k\), and all sufficiently large \(k\),
\[
\left|\{N_G(v)\cap S:v\in V(G)\}\right|\le Ck^d.
\]

#### Proof

It is enough first to count vertices outside \(S\). Let
\[
q=\left|\{N_G(v)\cap S:v\in V(G)\setminus S\}\right|,
\]
and choose \(q\) vertices having pairwise distinct traces on \(S\).

Fix \(\varepsilon>0\) sufficiently small that
\[
1+\varepsilon<d,\qquad a(1+\varepsilon)<d.
\]
Put
\[
r=\lceil k^{1+\varepsilon}\rceil.
\]

If \(q<2r\), then \(q=O(k^{1+\varepsilon})=O(k^d)\). Suppose therefore that \(q\ge2r\).

Order the vertices of \(S\) as \(s_1,\dots,s_k\). For every ordered \(r\)-tuple of distinct trace representatives \(v_1,\dots,v_r\), take the induced graph on
\[
S\cup\{v_1,\dots,v_r\}
\]
and label \(s_i\) by \(i\) and \(v_j\) by \(k+j\). Distinct ordered tuples produce distinct labeled graphs: if they first differ at coordinate \(j\), the two vertices in that coordinate have different traces on the fixed labeled set \(S\).

By heredity,
\[
f(k+r)\ge(q)_r\ge(q/2)^r.
\]
Therefore
\[
(q/2)^r
 \le (k+r)^{a(k+r)},
\]
and hence
\[
q\le 2(k+r)^{a(k+r)/r}.
\]
Now
\[
\frac{k+r}{r}\longrightarrow1,
\qquad
\frac{\log(k+r)}{\log k}\longrightarrow1+\varepsilon.
\]
It follows that
\[
\limsup_{k\to\infty}\frac{\log q}{\log k}
 \le a(1+\varepsilon)<d.
\]
Thus \(q=O(k^d)\). The at most \(k\) vertices lying in \(S\) add only \(k=O(k^d)\) further traces. ∎

### Lemma 2: polynomial trace growth gives approximate-neighborhood representatives

Suppose a graph \(H\) on \(m\) vertices satisfies
\[
\left|\{N_H(v)\cap S:v\in V(H)\}\right|
 \le C\max\{1,|S|^d\}
\tag{1}
\]
for every \(S\subseteq V(H)\), where \(d>1\).

There is a constant \(K=K(C,d)\) and, for all sufficiently large \(m\), a set \(R\subseteq V(H)\) with
\[
|R|\le \frac m2
\]
such that every \(v\in V(H)\) has some \(p(v)\in R\) satisfying
\[
|N_H(v)\mathbin{\triangle}N_H(p(v))|
 \le K m^{1-1/d}\log m.
\tag{2}
\]

#### Proof

Put
\[
t=K m^{1-1/d}\log m.
\]
Let \(R\) be a maximal collection of vertices whose neighborhoods are pairwise at symmetric-difference distance greater than \(t\). Maximality immediately gives (2).

It remains to bound \(|R|\). Choose, with replacement, a random sequence of
\[
s=\left\lceil\frac{4m\log m}{t}\right\rceil
\]
vertices. If \(u,v\in R\) are distinct, then the probability that the sample misses
\(N(u)\triangle N(v)\) is at most
\[
\left(1-\frac tm\right)^s
 \le \exp(-st/m)
 \le m^{-4}.
\]
There are fewer than \(m^2\) pairs, so with positive probability the sample distinguishes all members of \(R\). Removing repeated sample points, there is therefore a set \(S\) of size at most \(s\) on which all neighborhoods of vertices of \(R\) have distinct traces.

By (1),
\[
|R|\le Cs^d.
\]
For sufficiently large \(m\),
\[
s\le \frac{5}{K}m^{1/d}.
\]
Choosing \(K\) so that \(C(5/K)^d\le1/2\) gives \(|R|\le m/2\). ∎

### Lemma 3: recursive labeling from approximate representatives

Under the hypothesis of Lemma 2, \(H\) admits labels of length
\[
O\!\left(m^{1-1/d}\log^2 m\right).
\]

#### Proof

Give the vertices distinct global identifiers using \(\lceil\log m\rceil\) bits. Choose \(R\) and \(p(v)\) as in Lemma 2 and define
\[
D_v=N_H(v)\mathbin{\triangle}N_H(p(v)).
\]
Thus
\[
|D_v|\le t=O(m^{1-1/d}\log m).
\]

The label of \(v\) contains:

- the identifier of \(v\);
- the identifier of \(p(v)\);
- the list of identifiers in \(D_v\);
- recursively, the label of \(p(v)\) in the induced graph \(H[R]\).

Given labels of distinct \(v,w\), let \(b\) be the recursively decoded adjacency between \(p(v)\) and \(p(w)\), with \(b=0\) if they are the same vertex. Then
\[
\mathbf 1_{vw\in E(H)}
 =
 b
 \oplus \mathbf 1_{w\in D_v}
 \oplus \mathbf 1_{p(v)\in D_w}.
\tag{3}
\]
Indeed,
\[
A(v,w)=A(p(v),w)\oplus\mathbf 1_{w\in D_v},
\]
while symmetry and the definition of \(D_w\) give
\[
A(p(v),w)
 =A(p(v),p(w))\oplus\mathbf 1_{p(v)\in D_w}.
\]

At each recursive step the number of vertices is at least halved. Writing
\[
\alpha=1-\frac1d>0,
\]
the label-length recurrence is
\[
L(m)\le L(m/2)+O(m^\alpha\log m\log n)+O(\log n),
\]
where global identifiers use \(\log n\) bits. Consequently,
\[
L(n)
 =O\!\left(
   \log n\sum_{i\ge0}(n/2^i)^\alpha\log(n/2^i)
  \right)
 =O(n^\alpha\log^2 n).
\]
For bounded-size terminal graphs, the whole adjacency matrix can be encoded using a class-dependent constant number of bits. Standard headers and padding add only \(O(\log^2 n)\) bits. ∎

### Proof of Theorem 1

Choose
\[
\rho(\mathcal F)<a<d.
\]
For sufficiently large \(m\), \(f(m)\le m^{am}\). Lemma 1 supplies the trace bound (1) for every graph in \(\mathcal F\), and heredity ensures that it remains available at every recursive induced subgraph. Lemmas 2 and 3 now give
\[
L(n)=O(n^{1-1/d}\log^2 n).
\]

If \(\rho(\mathcal F)<2\), choose \(d\) with
\[
\max\{1,\rho(\mathcal F)\}<d<2.
\]
Then \(\alpha=1-1/d<1/2\), and hence
\[
n^\alpha\log^2 n
 =O(\sqrt n\log n),
\]
because \(\log n=O(n^{1/2-\alpha})\). ∎

## 2. A boundary estimate at coefficient \(2\)

The strict inequality \(\rho(\mathcal F)<2\) in Theorem 1 is not merely a cosmetic artifact of choosing \(d\). At the exact coefficient \(2\), the same counting argument gives an additional polylogarithmic factor.

### Proposition 4

Suppose
\[
f(m)\le 2^{Bm}m^{2m}
\]
for all sufficiently large \(m\), for some constant \(B\). Then \(\mathcal F\) admits labels of size
\[
O(\sqrt n\log^3 n).
\]

#### Proof

Repeat Lemma 1, but take
\[
r=\lceil k\log k\rceil.
\]
If \(q<2r\), then \(q=O(k\log k)\). Otherwise,
\[
(q/2)^r\le 2^{B(k+r)}(k+r)^{2(k+r)}.
\]
Since \(r\sim k\log k\), this implies
\[
q=O(k^2\log^2 k).
\]
Thus the trace bound is
\[
\pi(k)=O(k^2\log^2 k).
\]

In Lemma 2, take
\[
t=K\sqrt m\,\log^2 m.
\]
Then the separating sample has size
\[
s=O\!\left(\frac{\sqrt m}{\log m}\right),
\]
and consequently
\[
\pi(s)=O(s^2\log^2s)=O(m/K^2).
\]
For sufficiently large \(K\), the representative set again has size at most \(m/2\).

Each difference list has \(O(\sqrt m\log^2m)\) identifiers, each of length \(O(\log n)\). Summing over the recursive levels gives
\[
O(\sqrt n\log^3 n).
\]
∎

This misses the requested bound by two logarithmic factors, but it identifies a concrete critical regime for the elementary trace-compression method.

## 3. Sparse graphs and monotone hereditary classes

The following direct labeling lemma reaches exactly the requested order.

### Lemma 5: graphs with \(M\) edges

Every \(n\)-vertex graph with at most \(M\) edges admits labels of length
\[
O\!\left(\sqrt{M\log(n+1)}+\log n\right),
\]
with a decoder common to all such graphs.

#### Proof

Set
\[
\tau=\max\left\{1,\left\lceil\sqrt{\frac{M}{\log(n+1)}}\right\rceil\right\}.
\]
Call a vertex low if its degree is at most \(\tau\), and high otherwise.

A low vertex stores its identifier and the identifiers of all its neighbors. This costs
\[
O(\tau\log n)
\]
bits.

Let \(h\) be the number of high vertices. Since their degree sum is at most \(2M\),
\[
h\le\frac{2M}{\tau}.
\]
Assign the high vertices ranks \(1,\dots,h\). Fix an orientation of \(K_h\) with maximum outdegree at most \(\lceil h/2\rceil\). Each high vertex stores one adjacency bit for every potential high neighbor to which its prescribed arc is directed. Thus high-high adjacency costs \(O(h)\) bits per high vertex, plus \(O(\log n)\) bits for identifiers and ranks.

For a queried pair:

- if at least one endpoint is low, inspect the low endpoint's neighbor list;
- if both are high, inspect the bit stored according to the fixed orientation.

The maximum label length is therefore
\[
O\!\left(\tau\log n+\frac M\tau+\log n\right)
 =O\!\left(\sqrt{M\log(n+1)}+\log n\right).
\]
∎

### Corollary 6: edge-monotone factorial classes

Suppose \(\mathcal F\) is closed under deletion of edges as well as vertices, and
\[
f(n)\le2^{C n\log n}.
\]
Then \(\mathcal F\) admits labels of size
\[
O_{\mathcal F}(\sqrt n\log n).
\]

#### Proof

If \(G\in\mathcal F_n\) has \(m\) edges, then all its \(2^m\) spanning subgraphs belong to \(\mathcal F_n\). Hence
\[
2^m\le f(n)\le2^{C n\log n},
\]
so
\[
m\le Cn\log n.
\]
Applying Lemma 5 with \(M=Cn\log n\) gives
\[
O(\sqrt{n\log n\cdot\log n})
 =O(\sqrt n\log n).
\]
∎

The same conclusion holds for classes closed under edge addition, by applying the lemma to graph complements. More generally, the proof covers any class in which every graph has either \(O(n\log n)\) edges or \(O(n\log n)\) nonedges. It also covers graphs differing in \(O(n\log n)\) pairs from a fixed finite blow-up template: encode the template color of each vertex and apply Lemma 5 to the exception graph.

## 4. What remains unresolved

The original hypothesis only says that \(\rho(\mathcal F)\) is finite; it need not be less than \(2\). For \(\rho(\mathcal F)\ge2\), Theorem 1 gives only
\[
O\!\left(n^{1-1/d}\log^2 n\right)
\qquad(d>\rho(\mathcal F)),
\]
whose exponent may exceed \(1/2\).

The monotone argument cannot be transferred directly to an arbitrary hereditary class: from \(G\in\mathcal F\), one may delete vertices but not arbitrary edges, so a graph with many edges does not generate \(2^{e(G)}\) members of \(\mathcal F_n\). Dense factorial classes may instead owe their small speed to a structured adjacency relation rather than to sparsity.

Thus the unresolved part is to exploit that structured relation uniformly when the trace exponent is greater than \(2\). The recursive representative construction then permits too many pairwise distant neighborhoods, and simply listing their differences costs more than \(O(\sqrt n\log n)\). No argument above rules out a counterexample, and no full proof of the catalogued question is claimed.