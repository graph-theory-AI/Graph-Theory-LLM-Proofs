```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A rigidity lemma gives R_l(K_r,2) >= (r-1)^2+2, improving the earlier elementary bound by one, but the proposed equality remains unresolved.",
  "would_publish": false,
  "caveats": "The partial result is self-contained; its novelty and whether stronger lower bounds are known have not been checked."
}
```

# A rigidity lemma and an improved elementary lower bound

Let \(R_\ell(K_r,2)\) be the least \(n\) for which there exists an assignment of two-element lists to \(E(K_n)\) admitting no coloring without a monochromatic \(K_r\).

I do not settle
\[
R_\ell(K_r,2)=R(K_r,2)
\qquad(r>3).
\]
The result below strengthens the previous attempt’s elementary lower bound to
\[
\boxed{R_\ell(K_r,2)\ge (r-1)^2+2.}
\]
In particular,
\[
\boxed{11\le R_\ell(K_4,2)\le18.}
\]

The main point is a sharp structural statement about a stronger coloring requirement:

> **Rigidity theorem.** Let \(q\ge2\), and let \(L\) assign a two-element list to every edge of \(K_{q^2+1}\). There exists an \(L\)-coloring in which every color class is \(q\)-partite if and only if \(L\) is nonconstant.

Here the \(q\)-partitions may depend on the actual color.

I use and reprove the vertex-labeling idea from the earlier attempt. Its palette-compression and QBF claims are not needed.

## 1. A multipartite coloring certificate

Let \(\mathcal C\) be the finite set of colors appearing in the lists. For each \(c\in\mathcal C\), seek a labeling
\[
\lambda_c:V(K_n)\longrightarrow[q]
\]
such that, whenever \(L(uv)=\{a,b\}\),
\[
\lambda_a(u)\ne\lambda_a(v)
\quad\text{or}\quad
\lambda_b(u)\ne\lambda_b(v). \tag{1}
\]

Such labelings give the desired coloring immediately: color \(uv\) by a candidate \(c\in L(uv)\) whose labels differ. Every edge assigned \(c\) then joins distinct fibers of \(\lambda_c\). Thus its color class is \(q\)-partite.

### The elementary extension step

Suppose labels have already been assigned at \(k\) vertices, and we wish to label a new vertex \(x\). Choose all \(\lambda_c(x)\), \(c\in\mathcal C\), independently and uniformly from \([q]\).

For an earlier vertex \(y\), write \(L(xy)=\{a,b\}\). The event that (1) fails on \(xy\) is
\[
B_y=\{\lambda_a(x)=\lambda_a(y),\ 
       \lambda_b(x)=\lambda_b(y)\},
\]
and
\[
\Pr(B_y)=q^{-2}.
\]
Consequently, if \(k\le q^2-1\), then
\[
\Pr\Bigl(\bigcup_y B_y\Bigr)
\le \frac{k}{q^2}<1.
\]
The labeling therefore extends.

This proves the earlier bound for \(n\le q^2\). To handle one additional vertex, we arrange a positive overlap between two of the final bad events.

## 2. Proof of the rigidity theorem

### Nonconstant assignments admit the certificate

Set \(n=q^2+1\), and suppose \(L\) is nonconstant. There are three distinct vertices \(u,v,w\) such that
\[
P:=L(vu)\ne L(vw)=:Q. \tag{2}
\]
Indeed, if every vertex had the same list on all its incident edges, completeness would force all edge lists to be identical.

Since \(P,Q\) are distinct two-element sets,
\[
|P\cap Q|\le1.
\]
The list \(L(uw)\) has two elements, so we can choose
\[
d\in L(uw)\setminus(P\cap Q). \tag{3}
\]

First label \(u,w\) as follows:
\[
\lambda_c(u)=1\qquad(c\in\mathcal C),
\]
and
\[
\lambda_c(w)=
\begin{cases}
2,&c=d,\\
1,&c\ne d.
\end{cases}
\]
This is possible because \(q\ge2\).

The edge \(uw\) satisfies (1), using color \(d\). Moreover,
\[
\lambda_c(u)=\lambda_c(w)
\qquad(c\in P\cap Q). \tag{4}
\]

Now label every vertex other than \(v\), starting with the already labeled \(u,w\). Each new vertex has at most \(q^2-1\) earlier vertices, so the elementary extension step applies.

It remains to label \(v\). Choose its labels independently and uniformly. There are exactly \(q^2\) bad events \(B_y\), each of probability \(q^{-2}\). Crucially, \(B_u\) and \(B_w\) are compatible: by (4), they prescribe the same values on their shared coordinates. Thus
\[
\Pr(B_u\cap B_w)=q^{-|P\cup Q|}>0.
\]
Using this overlap,
\[
\begin{aligned}
\Pr\Bigl(\bigcup_{y\ne v}B_y\Bigr)
&\le \sum_{y\ne v}\Pr(B_y)-\Pr(B_u\cap B_w)\\
&=1-q^{-|P\cup Q|}\\
&<1.
\end{aligned}
\]
Hence some choice of labels at \(v\) satisfies every remaining edge constraint.

We have constructed (1) on all of \(K_{q^2+1}\), and therefore an \(L\)-coloring with every color class \(q\)-partite.

### Constant assignments do not admit the certificate

Suppose instead that
\[
L(e)=\{a,b\}
\qquad\text{for every edge }e.
\]
Assume an \(L\)-coloring has both color classes \(q\)-partite. Choose proper vertex labelings
\[
\lambda_a,\lambda_b:V(K_{q^2+1})\longrightarrow[q]
\]
of the two color-class graphs.

The map
\[
v\longmapsto\bigl(\lambda_a(v),\lambda_b(v)\bigr)
\]
must be injective. Otherwise, for two distinct vertices \(u,v\), their edge—whether colored \(a\) or \(b\)—would violate the corresponding proper labeling.

But \([q]^2\) has only \(q^2\) elements, fewer than the \(q^2+1\) vertices. This contradiction proves the converse. ∎

## 3. Consequence for list Ramsey numbers

### Corollary
For every \(r\ge3\),
\[
R_\ell(K_r,2)\ge(r-1)^2+2.
\]

### Proof

Put \(q=r-1\), and consider any two-list assignment on \(K_{q^2+1}\).

If the assignment is nonconstant, the rigidity theorem gives a coloring with every color class \(q\)-partite, and hence with no monochromatic \(K_{q+1}\).

It remains to handle constant lists. For completeness, the following explicit ordinary two-coloring works on \(q^2+1\) vertices.

Partition the vertex set into
\[
B_1,\ldots,B_{q-2},W,
\]
where
\[
|B_i|=q,\qquad |W|=2q+1.
\]
For \(q=2\), there are no \(B_i\).

Color:

- all edges inside each \(B_i\) red;
- all edges between distinct parts blue;
- inside \(W\), the edges of a cycle \(C_{2q+1}\) blue and all other edges red.

A red clique is contained in one part. Inside \(B_i\) it has size at most \(q\); inside \(W\), it is an independent set of \(C_{2q+1}\), also of size at most \(q\).

A blue clique contains at most one vertex from each \(B_i\) and at most two vertices from \(W\), because \(C_{2q+1}\) is triangle-free. Its size is therefore at most
\[
(q-2)+2=q.
\]
Thus this coloring has no monochromatic \(K_{q+1}\), and it can be used with the two colors in the constant list.

Every two-list assignment on \(K_{q^2+1}\) is consequently colorable without a monochromatic \(K_{q+1}\), proving the bound. ∎

For \(r=3\), this recovers
\[
R_\ell(K_3,2)=6.
\]
For \(r=4\), using the classical value \(R(K_4,2)=18\), it gives
\[
11\le R_\ell(K_4,2)\le18.
\]

## 4. The construction can be made deterministic

The labeling proof does not require an exhaustive search over all vectors in \([q]^{\mathcal C}\).

At an intermediate vertex, let \(X\) be the number of violated incident constraints. Initially,
\[
\mathbb E X<1.
\]
Assign the color coordinates one at a time, always choosing a value that does not increase the conditional expectation. At the end, \(X\) is a nonnegative integer smaller than \(1\), so \(X=0\).

At the final vertex \(v\), use instead
\[
Y=X-\mathbf 1_{B_u\cap B_w}.
\]
Pointwise, \(Y\) is a nonnegative integer and
\[
Y=0\quad\Longleftrightarrow\quad X=0:
\]
if \(B_u\cap B_w\) occurs, then \(X\ge2\). Furthermore,
\[
\mathbb E Y=1-q^{-|P\cup Q|}<1.
\]
Conditional expectations therefore find valid labels here as well. Each expectation is a sum of explicitly computable cylinder-event probabilities, so this gives a polynomial-time construction in the input size.

No computational experiment is being claimed.

## 5. What remains unresolved

This improves the earlier attempt’s elementary lower bound by one vertex and completely classifies failure of the stronger multipartite certificate on \(K_{(r-1)^2+1}\). It does **not** classify bad list Ramsey assignments.

In particular, the argument cannot simply be iterated. On \(q^2+2\) vertices, a nonconstant assignment may contain a constant-list \(K_{q^2+1}\). The rigidity theorem’s converse then rules out any coloring with every color class \(q\)-partite. That is an obstruction to this certificate, not necessarily to avoiding \(K_{q+1}\).

For \(r=4\), equality still requires proving that **every** two-list assignment on \(K_{17}\) is colorable without a monochromatic \(K_4\), or finding an explicit bad assignment on at most seventeen vertices. Neither is established here.