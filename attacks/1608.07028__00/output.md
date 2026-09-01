```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The exact asymptotic order remains open, but for every k at least 3 a binary-sum colouring of K_{2^k-2} has no rainbow cycle longer than 2^k-4, so the worst-case deficit is at least 2 on an infinite subsequence.",
  "would_publish": false,
  "caveats": "This only improves the constant obstruction on a subsequence and does not distinguish a bounded deficit from a growing one; novelty relative to all literature is not asserted."
}
```

## Formal statement

For a proper edge-colouring \(\chi\) of \(K_n\), let
\[
L(\chi)=\max\{|V(C)|: C\text{ is a rainbow cycle under }\chi\},
\]
and define
\[
\ell^*(n)=\min_{\chi} L(\chi),\qquad
\Delta(n)=n-\ell^*(n).
\]
Thus \(\Delta(n)\) is the nonnegative deficit. The bound quoted in the prompt from Balogh–Molla gives
\[
\Delta(n)=O(\sqrt n\log n).
\]

The usual lower obstruction is \(\Delta(n)\ge 1\) for even \(n\): a one-factorization of \(K_n\) uses only \(n-1\) colours and hence has no rainbow Hamilton cycle. The following strengthens this constant obstruction on infinitely many orders.

## Proposition

For every integer \(k\ge 3\),
\[
\ell^*(2^k-2)\le 2^k-4.
\]
Equivalently,
\[
\Delta(2^k-2)\ge 2.
\]

### Construction

Set \(N=2^k\) and let
\[
G=\mathbb F_2^k.
\]
Fix \(a\in G\setminus\{0\}\), and take the vertex set
\[
V=G\setminus\{0,a\},
\]
so \(|V|=N-2\). Colour the edge \(xy\) by
\[
\chi(xy)=x+y,
\]
where addition is in \(G\).

This is proper: for fixed \(x\), the equality
\[
\chi(xy)=\chi(xz)
\]
implies \(x+y=x+z\), hence \(y=z\). Moreover, no edge receives colour \(0\).

### Cycle invariant

Let
\[
C=v_1v_2\cdots v_rv_1
\]
be any cycle. The sum of its edge colours is
\[
\sum_{i=1}^r \chi(v_iv_{i+1})
 =\sum_{i=1}^r(v_i+v_{i+1})
 =2\sum_{i=1}^r v_i
 =0,
\]
where indices are cyclic and the last equality uses characteristic two.

Consequently, the set of colours of every rainbow cycle is a set of distinct nonzero vectors whose sum is zero.

On the other hand,
\[
\sum_{x\in G\setminus\{0\}}x=0.
\]
Indeed, in each coordinate exactly \(2^{k-1}\) vectors have coordinate \(1\), and \(2^{k-1}\) is even for \(k\ge2\).

Suppose first that there were a rainbow cycle of length \(N-2\). Its colours would form an \((N-2)\)-element subset \(D\) of the \((N-1)\)-element set \(G\setminus\{0\}\). Thus its complement would be a singleton \(\{d\}\), and
\[
\sum_{x\in D}x
 =\sum_{x\in G\setminus\{0\}}x+d
 =d\ne0,
\]
contradicting the cycle invariant.

Similarly, a rainbow cycle of length \(N-3\) would omit exactly two distinct nonzero vectors \(d,e\). Its colour sum would then be
\[
d+e\ne0,
\]
again contradicting the invariant.

Our graph has \(n=N-2\) vertices, so it contains no rainbow cycle of length \(n\) or \(n-1\). Hence every rainbow cycle has length at most
\[
n-2=N-4,
\]
proving the proposition.

## The obstruction is not merely a shortage of colours

In fact, all \(N-1=n+1\) nonzero vectors occur as colours.

For \(d=a\), any \(x\notin\{0,a\}\) gives an edge \(x(x+a)\) inside \(V\) of colour \(a\). For \(d\ne a\), choose
\[
x\notin\{0,a,d,a+d\},
\]
which is possible because \(N\ge8\). Then \(x,x+d\in V\), and their edge has colour \(d\).

Thus the construction has more colours than vertices, but nevertheless has neither a rainbow Hamilton cycle nor a rainbow cycle omitting just one vertex.

## Small explicit instance

For \(k=3\), identify \(G\) with the binary integers \(0,\dots,7\), delete \(0\) and \(1\), and colour \(xy\) by bitwise XOR. This gives a proper colouring of \(K_6\) with no rainbow \(C_5\) or \(C_6\).

It does contain the rainbow \(4\)-cycle
\[
4,5,7,3,4,
\]
whose colours are respectively
\[
1,2,4,7.
\]
Hence the longest rainbow cycle in this particular colouring is exactly \(4=6-2\).

## Limit of the argument and remaining gap

The XOR invariant alone cannot exclude a cycle of length \(N-4\): the complement of its colour set would have size three, and distinct nonzero vectors can sum to zero, for example
\[
x+y+(x+y)=0.
\]
Thus this method naturally stops at deficit \(2\).

Relative to the bounds stated in the prompt, we now have the precise additional obstruction
\[
\Delta(2^k-2)\ge2
\]
for every \(k\ge3\), while universally
\[
\Delta(n)=O(\sqrt n\log n).
\]
This does not determine whether \(\Delta(n)\) is bounded, tends to infinity along some sequence, or has order near \(\sqrt n\) up to logarithmic factors. The principal open problem therefore remains unresolved.