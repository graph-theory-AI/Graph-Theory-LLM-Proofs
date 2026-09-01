```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A dual-layer argument gives an explicit asymptotic upper bound g(n) at most log n plus gamma minus log 2 plus O(n^-2), and a separate classification gives g(n)=1 for n at most 5 and g(6)=7/6.",
  "would_publish": false,
  "caveats": "The asymptotic bounds still differ by a factor of order (log log n)^3, and the reported Steiner lower bound is not reproved here."
}
```

# Mathematical writeup

## 1. Formulation and partial results

Write
\[
\rho(G)=\max_{\varnothing\neq S\subseteq V(G)}
\frac{|S|}{\alpha(G[S])}.
\]
This is equivalent to maximizing over all subgraphs: replacing a subgraph on \(S\) by \(G[S]\) can only decrease its independence number.

The pointwise smallest function in the problem is therefore
\[
g(n)=\max_{|V(G)|=n}\frac{\chi_f(G)}{\rho(G)}.
\]
The maximum exists because there are finitely many graphs on \(n\) vertices.

I prove the following.

### Theorem 1: a parametric harmonic upper bound

Let \(G\) have \(n\) vertices and let \(r=\rho(G)\). Then
\[
\chi_f(G)\leq \sum_{k=1}^{n}\frac{1}{\lceil k/r\rceil}.
\tag{1}
\]
Consequently, defining
\[
\Phi(t)=\int_0^t\frac{dx}{\lceil x\rceil}
      =H_{\lfloor t\rfloor}
       +\frac{t-\lfloor t\rfloor}{\lfloor t\rfloor+1},
\tag{2}
\]
with \(H_0=0\), one has
\[
\boxed{\frac{\chi_f(G)}{\rho(G)}
       \leq \Phi\!\left(\frac{n}{\rho(G)}\right).}
\tag{3}
\]
In particular,
\[
\chi_f(G)\leq \rho(G)H_{\alpha(G)}.
\tag{4}
\]

Using the Strong Perfect Graph Theorem to exclude spanning odd holes and antiholes when the ratio is greater than \(1\), this gives, for \(m\geq3\),
\[
\boxed{g(2m)\leq H_m-\frac1{2m-1},}
\tag{5}
\]
and
\[
\boxed{g(2m+1)\leq H_m-\frac1{m(2m-1)}.}
\tag{6}
\]
Thus, with natural logarithms,
\[
\boxed{g(n)\leq \log n+\gamma-\log 2+O(n^{-2}).}
\tag{7}
\]

This only sharpens the explicit constant in the known logarithmic upper bound; it does not close the multiplicative polylogarithmic gap.

### Theorem 2: exact initial values

\[
\boxed{g(n)=1\quad(1\leq n\leq5),\qquad g(6)=\frac76.}
\tag{8}
\]
Consequently, by adding isolated vertices,
\[
g(n)\geq\frac76\qquad(n\geq6).
\]

---

## 2. Basic fractional-coloring facts

The dual linear program for the fractional chromatic number is
\[
\chi_f(G)=
\max\left\{
\sum_{v\in V(G)}y_v:
y_v\geq0,\ 
\sum_{v\in I}y_v\leq1
\text{ for every independent set }I
\right\}.
\tag{9}
\]

Also,
\[
\rho(G)\leq \chi_f(G).
\tag{10}
\]
Indeed, for any \(S\subseteq V(G)\),
\[
\chi_f(G)\geq \chi_f(G[S])
\geq \frac{|S|}{\alpha(G[S])}.
\]

If \(G\) is perfect, then
\[
\rho(G)\leq\chi_f(G)\leq\chi(G)=\omega(G)\leq\rho(G),
\]
so
\[
\chi_f(G)=\rho(G)=\omega(G).
\tag{11}
\]

---

## 3. Proof of the harmonic upper bound

Let \(y\) be an optimal solution of the dual program (9), and order the vertices so that
\[
y_1\geq y_2\geq\cdots\geq y_n.
\]
Let \(S_k=\{v_1,\ldots,v_k\}\). Since \(r=\rho(G)\),
\[
\alpha(G[S_k])\geq \frac{k}{r}.
\]
As the independence number is integral,
\[
\alpha(G[S_k])\geq \left\lceil\frac{k}{r}\right\rceil.
\]
Choose an independent set \(I_k\subseteq S_k\) of this size. Every vertex in \(I_k\) has dual weight at least \(y_k\), and hence dual feasibility gives
\[
1\geq \sum_{v\in I_k}y_v
  \geq \left\lceil\frac{k}{r}\right\rceil y_k.
\]
Therefore
\[
y_k\leq\frac1{\lceil k/r\rceil}.
\]
Summing over \(k\) proves (1).

For the integral estimate, put
\[
f(x)=\frac1{\lceil x\rceil}\qquad(x>0).
\]
This is nonincreasing. Taking \(h=1/r\), for each \(k\),
\[
h f(kh)\leq \int_{(k-1)h}^{kh}f(x)\,dx.
\]
Thus
\[
\frac1r\sum_{k=1}^n\frac1{\lceil k/r\rceil}
=h\sum_{k=1}^n f(kh)
\leq \int_0^{n/r}f(x)\,dx
=\Phi(n/r).
\]
Together with (1), this proves (3).

Finally, the full vertex set gives
\[
r\geq \frac{n}{\alpha(G)},
\]
so \(n/r\leq\alpha(G)\). Since \(\Phi\) is increasing and
\(\Phi(a)=H_a\) for every positive integer \(a\), (4) follows.

---

## 4. A pointwise upper bound for \(g(n)\)

Suppose first that
\[
\frac{\chi_f(G)}{\rho(G)}>1.
\]
Then \(G\) is not perfect. By the Strong Perfect Graph Theorem, \(G\) contains an induced odd hole or odd antihole.

Moreover, such an obstruction cannot use every vertex of \(G\). If it did, then \(G\) itself would be an odd cycle or the complement of an odd cycle. Both are vertex-transitive, and for a vertex-transitive graph
\[
\chi_f(G)=\frac{|V(G)|}{\alpha(G)};
\]
the full vertex set then witnesses \(\rho(G)=\chi_f(G)\), contrary to the strict inequality.

Let \(n\in\{2m,2m+1\}\), with \(m\geq3\). A proper odd hole or antihole has at most \(2m-1\) vertices.

If it is an odd hole of order \(2s+1\), then \(s\leq m-1\) and
\[
\rho(G)\geq\frac{2s+1}{s}
          =2+\frac1s
          \geq 2+\frac1{m-1}
          =\frac{2m-1}{m-1}.
\tag{12}
\]
If it is an odd antihole, its independence number is \(2\), so its Hall ratio is at least \(5/2\), which is again at least
\[
\frac{2m-1}{m-1}
\]
for \(m\geq3\). Hence in all cases
\[
r:=\rho(G)\geq r_m:=\frac{2m-1}{m-1}.
\tag{13}
\]

Because \(\Phi\) is increasing, Theorem 1 now yields
\[
\frac{\chi_f(G)}{\rho(G)}
\leq \Phi\!\left(\frac{n}{r_m}\right).
\]

### Even order

For \(n=2m\),
\[
\frac{n}{r_m}
=\frac{2m(m-1)}{2m-1}
=(m-1)+\frac{m-1}{2m-1}.
\]
Therefore
\[
\Phi(n/r_m)
=H_{m-1}+\frac{m-1}{m(2m-1)}
=H_m-\frac1{2m-1}.
\]
This proves (5).

### Odd order

For \(n=2m+1\),
\[
\frac{n}{r_m}
=\frac{(2m+1)(m-1)}{2m-1}
=(m-1)+\frac{2(m-1)}{2m-1}.
\]
Consequently,
\[
\Phi(n/r_m)
=H_{m-1}+\frac{2(m-1)}{m(2m-1)}
=H_m-\frac1{m(2m-1)}.
\]
This proves (6).

The standard expansion
\[
H_m=\log m+\gamma+\frac1{2m}+O(m^{-2})
\]
then gives (7) in both parity cases.

---

## 5. Exact determination for at most six vertices

### Orders at most five

By the Strong Perfect Graph Theorem, every graph on at most five vertices is perfect unless it is \(C_5\) itself, up to isomorphism.

Perfect graphs satisfy \(\chi_f=\rho\) by (11). For \(C_5\),
\[
\alpha(C_5)=2,\qquad
\rho(C_5)=\frac52.
\]
Assigning weight \(1/2\) to each of the five independent pairs of \(C_5\) gives a fractional coloring of total weight \(5/2\), so
\[
\chi_f(C_5)=\frac52=\rho(C_5).
\]
Hence
\[
g(n)=1\qquad(1\leq n\leq5).
\]

### Upper bound at order six

Let \(G\) have six vertices. If it is perfect, its ratio is \(1\). Otherwise, the Strong Perfect Graph Theorem implies that it contains an induced \(5\)-cycle \(C\). Let \(x\) be the remaining vertex and put
\[
A=N_G(x)\cap V(C).
\]

If \(A\) is independent in \(C_5\), then \(|A|\leq2\), and there is a vertex \(z\in V(C)\) adjacent in \(C\) to every vertex of \(A\). Mapping \(C\) identically to itself and mapping \(x\) to \(z\) gives a graph homomorphism
\[
G\longrightarrow C_5.
\]
Fractional chromatic number is homomorphism-monotone, so
\[
\chi_f(G)\leq\chi_f(C_5)=\frac52.
\]
Since \(G\) contains an induced \(C_5\), equality holds, and then
\[
\rho(G)=\chi_f(G)=\frac52.
\]

If \(A\) is not independent, it contains two consecutive vertices of \(C\). Together with \(x\), these form a triangle, so
\[
\rho(G)\geq3.
\]
Coloring \(x\) separately from an optimal fractional coloring of \(C_5\) gives
\[
\chi_f(G)\leq \chi_f(C_5)+1=\frac72.
\]
Thus
\[
\frac{\chi_f(G)}{\rho(G)}
\leq \frac{7/2}{3}
=\frac76.
\tag{14}
\]

### Sharpness at order six

Let
\[
W=K_1\vee C_5,
\]
the wheel with a \(5\)-cycle as rim. Fractional chromatic number is additive under joins, since every independent set of a join lies entirely in one side. Therefore
\[
\chi_f(W)=\chi_f(K_1)+\chi_f(C_5)
=1+\frac52=\frac72.
\]

Also \(\rho(W)=3\). The whole graph has independence number \(2\), giving ratio \(6/2=3\), and a direct check shows no vertex subset has larger ratio:

- without the center, the ratio is at most \(\rho(C_5)=5/2\);
- with the center and two adjacent rim vertices, one obtains a triangle and ratio \(3\);
- all larger subsets have independence number at least \(2\).

Hence
\[
\frac{\chi_f(W)}{\rho(W)}
=\frac{7/2}{3}
=\frac76.
\]
Together with (14), this proves
\[
g(6)=\frac76.
\]

Adding isolated vertices does not change either \(\chi_f\) or \(\rho\), so \(g(n)\geq7/6\) for every \(n\geq6\).

---

## 6. Remaining gap

The supplied catalog reports the asymptotic lower bound
\[
g(n)=\Omega\!\left(\frac{\log n}{(\log\log n)^3}\right)
\]
from Steiner's work. Combining that reported result with (7) gives
\[
\Omega\!\left(\frac{\log n}{(\log\log n)^3}\right)
\leq g(n)
\leq \log n+\gamma-\log2+O(n^{-2}).
\]

Thus the exponent of \(\log n\) is essentially settled, but the bounds still differ by a factor of order \((\log\log n)^3\), not merely by a constant. The arguments above do not remove that factor and do not determine \(g(n)\) beyond \(n=6\).