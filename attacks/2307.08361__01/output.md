```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The conjecture remains open; cubic bounds hold for sidewise almost-regular bipartite graphs, and unconditionally h4(G) is at least D^(1/3)/(32 ceil(log2(1+4 Delta/D))).",
  "would_publish": false,
  "caveats": "The bounds still depend on degree spread or order and do not cover graphs with arbitrarily many widely separated degree scales."
}
```

## 1. Statement and interpretation

All graphs below are finite and simple. I interpret “subgraph” as an arbitrary, not necessarily induced, subgraph; the arguments delete edges.

For a graph \(G\), define
\[
h_4(G)=\max\{\overline d(H):H\subseteq G,\ H\text{ is }C_4\text{-free}\}.
\]
The conjecture is equivalent, up to constants, to asking whether there are absolute \(c,\alpha>0\) such that
\[
h_4(G)\ge c\,\overline d(G)^\alpha
\]
for every graph of sufficiently large average degree.

I do not prove such an order- and degree-independent estimate. I prove the following partial bounds.

## 2. Partial results

Let \(G\) have \(n\ge2\) vertices, average degree \(D>0\), and maximum degree \(\Delta\). Put
\[
L(G)=\left\lceil \log_2\left(1+\frac{4\Delta}{D}\right)\right\rceil .
\]

Then
\[
\boxed{
h_4(G)\ge
\max\left\{
\frac{3D}{4\Delta^{2/3}},
\frac{D^{1/3}}{32L(G)},
\frac{D}{256\sqrt n}
\right\}.
}
\tag{1}
\]

There is also a stronger cubic conclusion for bipartite graphs with controlled degrees on each side.

### Sidewise almost-regular case

Let \(B\) be bipartite with parts \(A,B'\), \(m\) edges, and no isolated vertices. Write
\[
x=\frac{m}{|A|},\qquad y=\frac{m}{|B'|}
\]
for the two side-average degrees. Suppose
\[
d(v)\le Kx\quad(v\in A),\qquad
d(w)\le Ky\quad(w\in B')
\tag{2}
\]
for some \(K\ge1\). Then
\[
\boxed{
h_4(B)\ge \frac{3}{16K^{2/3}}\,\overline d(B)^{1/3}.
}
\tag{3}
\]

In particular, every biregular bipartite graph of average degree \(D\) contains a \(C_4\)-free subgraph of average degree at least
\[
\frac{3}{16}D^{1/3}.
\tag{4}
\]
Thus, for this class, average degree
\[
\left(\frac{16k}{3}\right)^3
\]
suffices.

More generally, (3) applies if all degrees on one side lie in \([r,Kr]\) and all degrees on the other side lie in \([s,Ks]\), with no restriction on the ratio \(r/s\).

## 3. Random alteration

We first record a standard self-contained alteration estimate.

### Lemma 1

If \(F\) has average degree \(d\) and maximum degree \(\Delta_F\ge1\), then
\[
h_4(F)\ge \frac{3d}{4\Delta_F^{2/3}}.
\tag{5}
\]

#### Proof

Let \(m=e(F)\), and let \(N_4(F)\) be the number of copies of \(C_4\). A fixed edge \(uv\) lies in at most
\[
(d(u)-1)(d(v)-1)\le(\Delta_F-1)^2
\]
copies of \(C_4\). Counting edge-cycle incidences gives
\[
4N_4(F)\le m(\Delta_F-1)^2\le m\Delta_F^2.
\tag{6}
\]

Retain each edge independently with probability
\[
q=\Delta_F^{-2/3}.
\]
The expected number of retained edges is \(qm\), while the expected number of retained copies of \(C_4\) is \(q^4N_4(F)\). From the sampled graph, delete one edge from each surviving \(C_4\). This removes at most one edge per surviving cycle and leaves a \(C_4\)-free graph. Its expected number of edges is at least
\[
qm-q^4N_4(F)
 \ge qm-\frac14q^4m\Delta_F^2
 =\frac34qm.
\]
Therefore some outcome has average degree at least
\[
\frac34q\,d=\frac{3d}{4\Delta_F^{2/3}}.
\]
Removing isolated vertices can only increase the average degree. \(\square\)

The first bound in (1) follows immediately. For example, if \(\Delta\le KD\), then
\[
h_4(G)\ge \frac{3}{4K^{2/3}}D^{1/3},
\]
so \(O(K^2k^3)\) average degree suffices.

## 4. Balancing an unbalanced bipartite graph

### Lemma 2

Under hypothesis (2),
\[
h_4(B)\ge \frac{3}{16K^{2/3}}\overline d(B)^{1/3}.
\]

#### Proof

Let \(a=|A|\), \(b=|B'|\). By interchanging the two sides, suppose \(x\ge y\), equivalently \(a\le b\). Set
\[
p=\frac{a}{b}=\frac{y}{x}.
\]
Select every vertex of \(B'\) independently with probability \(p\). Let \(Z\) be the number selected, so
\[
\mathbb E Z=pb=a.
\]

For \(u\in A\), let \(X_u\) be the number of selected neighbors of \(u\), with mean
\[
\mu_u=pd(u)\le pKx=Ky.
\]
Because there are no isolated vertices, \(y\ge1\). Put
\[
M=\lfloor 2Ky\rfloor,
\]
so \(M\ge Ky\ge\mu_u\).

After choosing the vertices of \(B'\), retain at most \(M\) selected edges at every vertex \(u\in A\). Let \(Y\) be the resulting number of edges. For every nonnegative integer \(z\),
\[
\min\{z,M\}\ge z-\frac{\binom z2}{M}.
\tag{7}
\]
Indeed, this is immediate for \(z\le M\), while for \(z\ge M\) the right-hand side is at most \(M\).

Since \(X_u\) is binomial,
\[
\mathbb E\binom{X_u}{2}\le\frac{\mu_u^2}{2}.
\]
Consequently,
\[
\mathbb E\min\{X_u,M\}
 \ge \mu_u-\frac{\mu_u^2}{2M}
 \ge\frac{\mu_u}{2}.
\]
Summing over \(A\),
\[
\mathbb EY\ge\frac12\sum_{u\in A}\mu_u
 =\frac12pm
 =\frac12ay.
\tag{8}
\]

It follows that
\[
\mathbb E\left[Y-\frac y4(a+Z)\right]\ge0.
\]
Hence some outcome satisfies
\[
Y\ge\frac y4(a+Z).
\]
The corresponding bipartite graph \(F\) has
\[
\overline d(F)=\frac{2Y}{a+Z}\ge\frac y2
\tag{9}
\]
and
\[
\Delta(F)\le 2Ky.
\tag{10}
\]

Moreover,
\[
\overline d(B)=\frac{2xy}{x+y},
\]
and \(x\ge y\) implies \(y\ge \overline d(B)/2\). Applying Lemma 1 to \(F\), we obtain
\[
\begin{aligned}
h_4(B)
&\ge \frac34\frac{y/2}{(2Ky)^{2/3}}\\
&=\frac{3y^{1/3}}{8(2K)^{2/3}}\\
&\ge \frac{3}{16K^{2/3}}\overline d(B)^{1/3}.
\end{aligned}
\]
\(\square\)

This lemma is useful because it handles arbitrarily unbalanced biregular graphs: the two typical degrees may differ by an arbitrarily large factor.

## 5. A logarithmic degree-spread bound

We now prove the middle estimate in (1).

Choose a bipartite spanning subgraph \(G_0\subseteq G\) with at least half the edges. Thus
\[
d_0:=\overline d(G_0)\ge \frac D2.
\]

Iteratively delete vertices of degree less than \(d_0/2\). Deleting such a vertex cannot decrease the current average degree, and the process leaves a nonempty bipartite graph \(G_1\) satisfying
\[
\delta(G_1)\ge \delta_0:=\frac{d_0}{2}\ge\frac D4,
\qquad
\overline d(G_1)\ge d_0\ge\frac D2.
\tag{11}
\]

Set
\[
\ell=\left\lceil\log_2\left(1+\frac{\Delta}{\delta_0}\right)\right\rceil
 \le L(G).
\tag{12}
\]
Let the bipartition of \(G_1\) be \(X\cup Y\). Partition both sides into dyadic degree classes
\[
X_i=\{v\in X:\delta_0 2^{i-1}\le d(v)<\delta_0 2^i\},
\]
and similarly \(Y_j\), for \(1\le i,j\le\ell\).

Write
\[
e_{ij}=e(X_i,Y_j),\qquad
R_i=\sum_j e_{ij},\qquad
C_j=\sum_i e_{ij}.
\]
Call a cell \((i,j)\) row-good if
\[
e_{ij}\ge\frac{R_i}{3\ell}
\]
and column-good if
\[
e_{ij}\ge\frac{C_j}{3\ell}.
\]

In each row, the total number of edges in cells that are not row-good is less than \(R_i/3\). Hence more than two-thirds of all edges lie in row-good cells. The analogous statement holds for column-good cells. Therefore more than one-third of all edges of \(G_1\) lie in cells that are both row-good and column-good.

Let \(m_1=e(G_1)\) and \(n_1=v(G_1)\). Also,
\[
\sum_{i,j}\bigl(|X_i|+|Y_j|\bigr)=\ell n_1.
\]
It follows by weighted averaging that some doubly good cell \((i,j)\), with \(a=|X_i|\), \(b=|Y_j|\), and \(e=e_{ij}\), satisfies
\[
\frac{2e}{a+b}\ge \frac{\overline d(G_1)}{3\ell}
 \ge\frac{D}{6\ell}.
\tag{13}
\]

Let \(P=G_1[X_i,Y_j]\). Since the cell is row-good,
\[
\frac ea\ge \frac{R_i}{3\ell a}
 \ge\frac{\delta_0 2^{i-1}}{3\ell}.
\]
On the other hand, every vertex of \(X_i\) has degree in \(P\) less than \(\delta_0 2^i\). Thus
\[
\Delta(P[X_i])\le 6\ell\frac ea.
\tag{14}
\]
Similarly,
\[
\Delta(P[Y_j])\le 6\ell\frac eb.
\tag{15}
\]
Deleting isolated vertices only increases the side-average degrees, so Lemma 2 applies to \(P\) with \(K=6\ell\). Using (13),
\[
\begin{aligned}
h_4(G)
&\ge \frac{3}{16(6\ell)^{2/3}}
   \left(\frac{D}{6\ell}\right)^{1/3}\\
&=\frac{D^{1/3}}{32\ell}\\
&\ge\frac{D^{1/3}}{32L(G)}.
\end{aligned}
\]
This proves the second estimate in (1).

## 6. A dense-order estimate

For completeness, there is also a useful bound depending on the number of vertices.

### Lemma 3

Every \(n\)-vertex graph of average degree \(D\) contains a \(C_4\)-free subgraph of average degree at least
\[
\frac{D}{256\sqrt n}.
\tag{16}
\]

#### Proof

For \(n\ge64\), choose a power of two \(q\) satisfying
\[
\frac{\sqrt n}{8}<q\le\frac{\sqrt n}{4}.
\]
The incidence graph of the projective plane over \(\mathbb F_q\) is \(C_4\)-free: two distinct points lie on a unique line. It has
\[
2(q^2+q+1)
\]
vertices and
\[
(q+1)(q^2+q+1)\ge q^3>\frac{n^{3/2}}{512}
\]
edges. Its order is at most
\[
\frac n8+\frac{\sqrt n}{2}+2\le n,
\]
so by adding isolated vertices we obtain a \(C_4\)-free graph \(Q\) on exactly \(n\) vertices with at least \(n^{3/2}/512\) edges.

Randomly identify \(V(G)\) with \(V(Q)\), and retain an edge of \(G\) exactly when its image is an edge of \(Q\). The retained graph is \(C_4\)-free, and every edge is retained with probability at least
\[
\frac{n^{3/2}/512}{\binom n2}\ge\frac1{256\sqrt n}.
\]
The expected retained average degree is therefore at least \(D/(256\sqrt n)\).

For \(n<64\), a single edge has average degree \(1\), which is more than the right-hand side whenever \(D>0\). \(\square\)

In particular, if \(n\le CD\), then
\[
h_4(G)\ge\frac{\sqrt D}{256\sqrt C},
\]
so a quadratic bound suffices for such dense graphs.

## 7. Consequences and obstruction profile

The estimates give polynomial bounds in several substantial special cases.

1. **Polynomial maximum degree.**  
   If \(\Delta\le D^A\) for fixed \(A\), then
   \[
   h_4(G)=\Omega_A\left(\frac{D^{1/3}}{\log(D+2)}\right).
   \]
   Thus a threshold
   \[
   O_A\!\left(k^3\log^3(k+2)\right),
   \]
   and hence certainly a polynomial threshold such as \(O_A(k^4)\), suffices.

2. **Subexponential degree spread.**  
   If, for some fixed \(\varepsilon>0\),
   \[
   L(G)\le D^{1/3-\varepsilon},
   \]
   then
   \[
   h_4(G)\ge\frac{D^\varepsilon}{32}.
   \]
   Hence \((32k)^{1/\varepsilon}\) suffices within this class.

3. **Sidewise almost-regular bipartite graphs.**  
   Under (2), average degree
   \[
   \left(\frac{16}{3}\right)^3K^2k^3
   \]
   suffices, independently of the ratio between the two side-average degrees.

There is also a precise necessary profile for any putative family defeating all power-law estimates. If
\[
h_4(G)<D^\eta
\]
for \(0<\eta<1/3\), then (1) implies
\[
\Delta>
\left(\frac34\right)^{3/2}D^{\frac32(1-\eta)}
\tag{17}
\]
and
\[
L(G)>\frac{D^{1/3-\eta}}{32}.
\tag{18}
\]
In particular,
\[
\log_2\left(1+\frac{4\Delta}{D}\right)
 \ge \frac{D^{1/3-\eta}}{32}-1.
\tag{19}
\]
Thus any diagonal sequence with
\[
h_4(G)=D^{o(1)}
\]
must satisfy
\[
\log \Delta\ge D^{1/3-o(1)}
\quad\text{and hence}\quad
|V(G)|\ge 2^{D^{1/3-o(1)}}.
\tag{20}
\]

## 8. Remaining gap

The logarithmic loss in the degree-bucketing argument is harmless when the maximum degree is at most polynomial, or even moderately subexponential, in the average degree. It is uncontrolled in general: a graph may have edges spread across arbitrarily many widely separated degree scales. Lemma 2 balances one pair of scales, including arbitrarily unbalanced biregular pairs, but does not combine all scales without a factor depending on their number.

Consequently, none of the estimates above gives a positive power of \(D\) for completely unrestricted graphs. They neither prove nor disprove the requested polynomial \(p(k)\), and they do not improve the quoted unrestricted \(k^{Ck^2}\) threshold. The arguments are elementary and self-contained; I have not verified whether these particular formulations already occur in the literature, so I make no novelty claim.