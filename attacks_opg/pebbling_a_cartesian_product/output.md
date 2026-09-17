```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A connectivity-sensitive bound gives an explicit range of complete factors for which Graham’s inequality holds, but does not resolve arbitrary Cartesian products.",
  "would_publish": false,
  "caveats": "The partial bounds are proved below; their novelty relative to the complete-factor literature has not been verified."
}
```

# A quantitative partial result for complete factors

I do not obtain a proof or counterexample for arbitrary factors. I can prove the following explicit bound, including a range in which the product has pebbling number equal to its order. I do not assert that these quantitative bounds are new.

All graphs below are finite, simple, and connected. Write \(\kappa(G)\) for vertex connectivity, with \(\kappa(K_m)=m-1\). Factors consisting of one vertex cause no difficulty.

## Theorem

Let \(G\) have order \(m\ge 2\), vertex connectivity \(k\), and pebbling number \(p=p(G)\). For every \(n\ge 3\),
\[
\boxed{
p(G\Box K_n)
\le
\max\left\{
mn+p-m,\;
2p-1+(m-k)(n-1)
\right\}.
}
\tag{1}
\]
For \(n\ge 4\), the stronger bound
\[
\boxed{
p(G\Box K_n)
\le
\max\left\{
mn,\;
2p-1+(m-k)(n-1)
\right\}
}
\tag{2}
\]
holds.

Consequently, Graham’s inequality holds for \(G\Box K_n\) whenever
\[
\boxed{
n\ge
\max\left\{
3,\;
2+\left\lceil
\frac{m-k-1}{p-m+k}
\right\rceil
\right\}.
}
\tag{3}
\]

The proof uses only connectivity, parity counting, and legal pebbling moves.

## 1. A dense-configuration lemma

For a configuration \(D\) on \(G\), define its **pair count**
\[
B(D)=\sum_{v\in V(G)}
\left\lfloor\frac{D(v)}2\right\rfloor .
\]

We will repeatedly use the following elementary observation: a pair can be moved along a path whose internal vertices are occupied. After a move reaches an occupied vertex, that vertex has at least two pebbles, so the next move is possible.

**Lemma.** Suppose \(D\) has at most \(k-1\) empty vertices. If \(D\) cannot place two pebbles at a specified vertex \(r\), then
\[
|D|\le m+1.
\]

**Proof.** Let \(Z\) be the set of empty vertices.

If \(r\notin Z\), then \(G-Z\) is connected. Any vertex containing a pair could send a pebble to \(r\) along an occupied path, giving \(r\) two pebbles. Thus every vertex has at most one pebble, and \(|D|\le m\).

Suppose \(r\in Z\). Delete \(Z\setminus\{r\}\). At most \(k-2\) vertices are deleted, so the resulting graph \(F\) is 2-connected. Every vertex of \(F\) other than \(r\) is occupied.

If \(B(D)\ge2\), there are two possibilities.

* Some vertex \(u\) has at least four pebbles. Two internally vertex-disjoint \(u\)-\(r\) paths allow two separate deliveries to \(r\).
* Two distinct vertices \(u,v\) each have a pair. A two-fan from \(r\) to \(\{u,v\}\), supplied by Menger’s theorem, again allows two separate deliveries.

In both cases, the paths’ internal vertices supply the single pebbles needed to propagate the pairs. Hence \(B(D)\le1\). Since \(r\) is empty, this implies
\[
|D|\le (m-1)+2=m+1.
\]
\(\square\)

## 2. Set-up in the product

Fix a target \((r,0)\), and let \(q=p(G,r)\) be the rooted pebbling number of \(G\) at \(r\). In particular,
\[
m\le q\le p.
\]

Index the \(G\)-fibers of \(G\Box K_n\) by \(0,\ldots,n-1\). Suppose \(C\) is an unsolvable configuration for \((r,0)\), of size
\[
N\ge mn.
\]

For fiber \(i\), let
\[
\begin{aligned}
a_i&=\sum_v C(v,i),\\
b_i&=\sum_v\left\lfloor\frac{C(v,i)}2\right\rfloor,\\
o_i&=\bigl|\{v:C(v,i)\text{ is odd}\}\bigr|,\\
z_i&=\bigl|\{v:C(v,i)=0\}\bigr|.
\end{aligned}
\]
Thus \(a_i=2b_i+o_i\). Put
\[
Q=\sum_i b_i.
\]

Sending every available pair from each nonzero fiber directly into fiber \(0\) produces
\[
S=a_0+\sum_{i\ne0}b_i
  =Q+b_0+o_0
\]
pebbles in the target fiber. These are legal moves because each row is a clique. Unsolvability therefore gives
\[
S\le q-1.
\tag{4}
\]
Also,
\[
N=2S-a_0+\sum_{i\ne0}o_i.
\tag{5}
\]

### An unsolvable configuration has many empty vertices

Let \(z=\sum_i z_i\). I claim that
\[
z\ge n+1.
\tag{6}
\]

Indeed, \(C(r,0)=0\), and \(N\ge mn\) guarantees that some vertex has a pair. If \(z\le n\), delete all empty vertices other than the target. At most \(n-1\) vertices have been deleted, so some \(G\)-fiber is untouched. The remaining product graph is connected: every remaining vertex has an edge to its corresponding vertex in that untouched fiber.

There is consequently a path from a pair-containing vertex to the target whose internal vertices are occupied. Propagating the pair along this path solves the configuration, a contradiction.

Now let
\[
E=\sum_x\max\{C(x)-1,0\}.
\]
We have
\[
N=mn-z+E,\qquad E\le2Q.
\]
Since \(N\ge mn\), equation (6) implies
\[
Q\ge\left\lceil\frac{n+1}{2}\right\rceil.
\tag{7}
\]
In particular, \(Q\ge2\) for \(n\ge3\), and \(Q\ge3\) for \(n\ge4\).

## 3. Restrictions on a nearly occupied fiber

Fix \(j\ne0\) with \(z_j<k\). Send every available pair from every other fiber into fiber \(j\). Its resulting size is
\[
a_j+Q-b_j.
\]
Its set of empty vertices can only shrink.

This resulting configuration cannot place two pebbles at \((r,j)\), since one subsequent move would solve the original target \((r,0)\). The lemma therefore gives
\[
a_j+Q-b_j\le m+1.
\tag{8}
\]

Since \(a_j-b_j\ge m-z_j\), and \(a_j-b_j=b_j+o_j\), we obtain
\[
Q\le z_j+1,
\qquad
o_j\le m+1-Q.
\tag{9}
\]

These inequalities yield a useful dichotomy.

### Case A: \(Q\ge k+1\)

The first inequality in (9) rules out \(z_j<k\) for every \(j\ne0\). Thus each nonzero fiber has at least \(k\) empty vertices, giving
\[
\sum_{j\ne0}o_j\le(m-k)(n-1).
\]
Equations (4) and (5) now imply
\[
N\le 2q-2+(m-k)(n-1).
\tag{10}
\]

### Case B: \(Q\le k\)

For every \(j\ne0\),
\[
o_j\le m+1-Q.
\tag{11}
\]
For \(z_j<k\), this follows from (9). Otherwise,
\[
o_j\le m-k\le m+1-Q.
\]

Equation (4) gives
\[
o_0\le q-1-Q-b_0.
\]
Hence
\[
\begin{aligned}
N
&=2Q+o_0+\sum_{j\ne0}o_j\\
&\le 2Q+q-1-Q-b_0+(n-1)(m+1-Q)\\
&=mn+(q-m)-(n-2)(Q-1)-b_0.
\end{aligned}
\]
For \(n\ge3\), equation (7) yields
\[
N\le mn+(q-m)-1.
\tag{12}
\]

Combining (10) and (12), and including configurations of size below \(mn\), proves the rooted bound
\[
p(G\Box K_n,(r,0))
\le
\max\{mn+q-m,\;2q-1+(m-k)(n-1)\}.
\]
Taking the maximum over \(r\) proves (1).

## 4. Improvement when \(n\ge4\)

In Case B, use the simpler estimate \(o_0\le m-1\), since the target is empty. Together with (11), this gives
\[
\begin{aligned}
N
&\le 2Q+(m-1)+(n-1)(m+1-Q)\\
&=mn+n-2-(n-3)Q.
\end{aligned}
\]
For \(n\ge4\), equation (7) gives \(Q\ge3\), so
\[
N\le mn+7-2n\le mn-1.
\]
This contradicts \(N\ge mn\). Thus Case B cannot occur, and (10) proves (2).

## 5. Consequences for Graham’s inequality

Let \(d=p-m\ge0\). The first term in (1) satisfies
\[
mn+d\le pn.
\]
The second term is at most \(pn\) precisely when
\[
n(d+k)\ge 2p-m+k-1
             =2(d+k)+(m-k-1).
\]
This proves (3), using \(p(K_n)=n\).

There are also exact-value consequences.

* If \(G\) is **Class 0**, meaning \(p(G)=m\), then
  \[
  p(G\Box K_n)=mn
  \quad\text{whenever}\quad
  n\ge3,\qquad k(n-1)\ge m-1.
  \]
* For arbitrary \(G\), equation (2) gives
  \[
  p(G\Box K_n)=mn
  \quad\text{whenever}\quad
  n\ge4,\qquad k(n-1)\ge2p-m-1.
  \]

In both statements, the matching lower bound \(mn\) comes from placing one pebble at every vertex except the target: there is no legal move.

## What remains unresolved

The proof depends essentially on the complete factor. It repeatedly transfers every available pair into a chosen fiber using one move per pair. For a general second factor, those transfers need not be available, and routing them changes both their cost and the occupancy information used above.

Thus this argument establishes only a quantitative complete-factor result. It neither proves Graham’s conjecture for arbitrary factors nor produces a counterexample, and it makes no determination of the Lemke-graph square.