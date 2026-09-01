```json
{
  "verdict": "proved",
  "confidence": "high",
  "one_line": "For every k >= 1, an explicit tree has pathwidth k and minimum part-counting path-partition height 2k, so the factor 2 is sharp.",
  "would_publish": false,
  "caveats": "This uses the usual quotient-tree definition; if height counts quotient edges, the exact sharp value is 2k-1 rather than 2k."
}
```

## 1. Statement and conventions

A **path-partition** \(\mathcal P\) of a tree \(T\) is a partition of \(V(T)\) into sets inducing paths. Contracting every part gives a quotient tree \(T/\mathcal P\).

To make the height convention explicit, define
\[
\lambda(T):=
 \min_{\mathcal P,\;R\in\mathcal P}
 \max_{P\in\mathcal P} d_{T/\mathcal P}(R,P).
\]
Thus \(\lambda(T)\) is the minimum possible height when the root has depth \(0\). If height is instead the number of parts on a root-to-leaf chain, as in the usual formulation around Lemma 4, then
\[
H(T)=\lambda(T)+1.
\]

I prove the following exact result.

### Theorem
For every integer \(k\ge 1\):

1. every tree \(T\) of pathwidth at most \(k\) satisfies
   \[
   \lambda(T)\le 2k-1;
   \]
2. there is a tree \(T_k\) with
   \[
   \operatorname{pw}(T_k)=k,
   \qquad
   \lambda(T_k)=2k-1.
   \]

Consequently, in the convention counting the root part, \(H(T_k)=2k\). Thus the bound in Lemma 4 is attained exactly, and the factor \(2\) is unavoidable.

---

## 2. A path-removal characterization of tree pathwidth

We use the standard convention that the width of a path-decomposition is one less than its largest bag size.

### Lemma 1
For a tree \(T\) and \(k\ge1\),
\[
\operatorname{pw}(T)\le k
\]
if and only if there is a path \(P\subseteq T\) such that every component of \(T-V(P)\) has pathwidth at most \(k-1\).

#### Proof

Suppose first that \((B_1,\dots,B_m)\) is a path-decomposition of \(T\) of width at most \(k\). Choose \(u\in B_1\) and \(v\in B_m\), and let \(P\) be the unique \(u\)-\(v\) path in \(T\).

For each vertex \(x\), the set
\[
I_x:=\{i:x\in B_i\}
\]
is an interval. If \(xy\in E(T)\), then \(I_x\cap I_y\ne\varnothing\). Hence the union of the intervals \(I_x\), over \(x\in V(P)\), is an interval containing both \(1\) and \(m\). It therefore contains every index \(i\). Thus every bag \(B_i\) meets \(P\).

Deleting \(V(P)\) from every bag leaves a path-decomposition of \(T-V(P)\) in which every bag has size at most \(k\). Each component consequently has pathwidth at most \(k-1\).

Conversely, suppose \(P=p_1\cdots p_t\) has the stated property. Every component \(C\) of \(T-V(P)\) has a unique attachment vertex \(p_i\) on \(P\). Take a width-\((k-1)\) path-decomposition of \(C\), add \(p_i\) to all its bags, and concatenate these decompositions in the order \(p_1,\dots,p_t\), inserting bags \(\{p_i,p_{i+1}\}\) where needed. This gives a width-\(k\) path-decomposition of \(T\). ∎

---

## 3. The exact universal upper bound

It is useful first to prove a rooted version. For \(r\in V(T)\), let \(\lambda(T,r)\) be the minimum quotient edge-height when the quotient is rooted at the part containing \(r\).

### Lemma 2
For every rooted tree \((T,r)\),
\[
\lambda(T,r)\le 2\operatorname{pw}(T).
\]

#### Proof

Induct on \(k=\operatorname{pw}(T)\). The case \(k=0\) is immediate.

Choose, by Lemma 1, a path \(P\) such that every component of \(T-V(P)\) has pathwidth at most \(k-1\).

If \(r\in V(P)\), use \(P\) as the root part. Root each component partition at its attachment vertex and apply induction. This gives height at most
\[
1+2(k-1)=2k-1.
\]

Now suppose \(r\notin V(P)\). Let \(Q\) be the path from \(r\) to \(P\), meeting \(P\) first at \(x\). The tree \(P\cup Q\) has at most three arms at \(x\). It can be partitioned into at most two paths as follows:

- one path \(P_0\), containing \(Q\) and one side of \(P-x\), contains \(r\);
- the other side of \(P-x\), if nonempty, is a second path \(P_1\), adjacent to \(P_0\).

Every component of \(T-(P\cup Q)\) is a subtree of a component of \(T-P\), and hence has pathwidth at most \(k-1\). Root its partition at its attachment vertex. Components attached to \(P_0\) have depth at most
\[
1+2(k-1)=2k-1,
\]
while those attached to \(P_1\) have depth at most
\[
2+2(k-1)=2k.
\]
Thus \(\lambda(T,r)\le2k\). ∎

### Corollary 3
If \(T\) has pathwidth \(k\ge1\), then
\[
\lambda(T)\le2k-1.
\]

#### Proof

Choose a path \(P\) from Lemma 1 and use \(P\) as the root part. Every component \(C\) of \(T-P\) has pathwidth at most \(k-1\). Applying Lemma 2 to \(C\), rooted at its attachment vertex, gives global depth at most
\[
1+2(k-1)=2k-1.
\]
∎

Thus, if height counts parts rather than quotient edges, Corollary 3 is precisely the bound \(2k\).

---

## 4. The extremal family

Define rooted trees \((R_h,r_h)\) recursively.

- \(R_0\) consists of the single vertex \(r_0\).
- For \(h\ge1\), take two disjoint copies of \(R_{h-1}\), with designated roots \(s_1,s_2\), add two new vertices \(r_h,x_h\), and add the three edges
  \[
  r_hx_h,\qquad x_hs_1,\qquad x_hs_2.
  \]
  The designated root is \(r_h\).

Thus \(r_h\) is a leaf and \(x_h\) is a branching vertex:

\[
r_h - x_h
\begin{cases}
-\,R_{h-1},\\[-2mm]
-\,R_{h-1}.
\end{cases}
\]

Finally, let \(D_h\) be obtained from two disjoint copies of \(R_h\) by adding an edge between their designated roots.

The orders are
\[
|R_h|=3\cdot2^h-2,
\qquad
|D_h|=6\cdot2^h-4.
\]

---

## 5. Pathwidth of the construction

### Lemma 4
For every \(h\ge0\),
\[
\operatorname{pw}(R_h)=\left\lceil\frac h2\right\rceil .
\]

#### Proof

The cases \(h=0,1\) are immediate.

For the upper bound, in each of the two top copies of \(R_{h-1}\), choose a path beginning at its designated root and recursively continuing through one child at every branching vertex. Join these two paths through \(x_h\). The resulting path \(P\) has the property that every component of \(R_h-P\) is either isolated or contained in a copy \(R_j\) with \(j\le h-2\). Lemma 1 and induction give
\[
\operatorname{pw}(R_h)
 \le 1+\operatorname{pw}(R_{h-2})
 =1+\left\lceil\frac{h-2}{2}\right\rceil
 =\left\lceil\frac h2\right\rceil .
\]

For the reverse inequality, consider any path \(P\subseteq R_h\).

- If \(P\) does not meet both top copies of \(R_{h-1}\), one of them is untouched.
- If \(P\) meets both, it passes through \(x_h\). On entering either top copy through its designated root, the path has already used the edge toward \(x_h\). At the next branching vertex it can enter at most one of the two copies of \(R_{h-2}\). Hence an entire \(R_{h-2}\) remains untouched.

Thus every path deletion leaves a component containing \(R_{h-2}\). Applying Lemma 1 to an optimal-width decomposition gives
\[
\operatorname{pw}(R_h)
 \ge 1+\operatorname{pw}(R_{h-2})
 =\left\lceil\frac h2\right\rceil .
\]
∎

### Lemma 5
For every \(h\ge0\),
\[
\operatorname{pw}(D_h)
 =1+\operatorname{pw}(R_{h-1})
 =\left\lceil\frac{h+1}{2}\right\rceil ,
\]
with the natural interpretation for \(h=0\).

#### Proof

For the upper bound, take in each copy of \(R_h\) a path from its designated root recursively down through one child at each branching vertex. Join the two paths by the edge between the designated roots. Deleting this path leaves only copies \(R_j\) with \(j\le h-1\). Hence
\[
\operatorname{pw}(D_h)
 \le1+\operatorname{pw}(R_{h-1}).
\]

For the lower bound, every path in \(D_h\) leaves an intact copy of \(R_{h-1}\):

- if it does not cross between the two copies of \(R_h\), the other copy is essentially untouched;
- if it does cross, then in each \(R_h\) it enters from the designated root and can continue through at most one of the two top \(R_{h-1}\) branches.

Lemma 1 now gives the reverse inequality. ∎

---

## 6. Minimum path-partition height

Given a path-partition \(\mathcal P\) of a tree \(T\), let
\[
F:=\bigcup_{P\in\mathcal P}E(T[P])
\]
be the set of edges internal to parts. Since every part is a path,
\[
\deg_F(v)\le2\qquad\text{for every }v.
\]

Moreover, for vertices \(u,v\), the quotient distance between their parts equals the number of edges outside \(F\) on the unique \(u\)-\(v\) path:
\[
d_{T/\mathcal P}([u],[v])
 =
 \bigl|E(uTv)\setminus F\bigr|.
\tag{1}
\]
Indeed, a connected part cannot meet a tree path in two disjoint intervals.

### Lemma 6: one cut per level
Let \(F\subseteq E(R_h)\) satisfy \(\deg_F(v)\le2\) for every vertex. There is a leaf \(\ell\) of \(R_h\) such that the \(r_h\)-\(\ell\) path contains at least \(h\) edges outside \(F\).

#### Proof

Induct on \(h\). The case \(h=0\) is immediate.

At the top of \(R_h\), consider the edge \(r_hx_h\).

- If \(r_hx_h\notin F\), it supplies one edge outside \(F\); continue into either copy of \(R_{h-1}\) and use induction.
- If \(r_hx_h\in F\), then, since \(\deg_F(x_h)\le2\), at least one of the two edges from \(x_h\) to the child roots is outside \(F\). Continue into that child and use induction.

This yields one new edge outside \(F\), plus at least \(h-1\) below it. ∎

### Lemma 7
For every \(h\ge0\),
\[
\lambda(D_h)=h.
\]

#### Lower bound

Take any path-partition \(\mathcal P\) of \(D_h\) and its internal edge set \(F\). Apply Lemma 6 independently in the left and right copies of \(R_h\). This gives leaves \(\ell_L,\ell_R\) such that each root-to-leaf segment contains at least \(h\) edges outside \(F\).

Consequently, the \(\ell_L\)-\(\ell_R\) path contains at least \(2h\) edges outside \(F\). By (1), the quotient tree has diameter at least \(2h\).

For any rooting of that quotient, at least one endpoint of this diameter is at distance at least \(h\) from the root. Therefore every path-partition has edge-height at least \(h\):
\[
\lambda(D_h)\ge h.
\]

#### Upper bound

We recursively construct a path-partition of \(R_h\), rooted at a part containing \(r_h\), of edge-height \(h\), with the root part a path from \(r_h\) to a leaf.

For \(h=0\), this is trivial. For \(h\ge1\), choose one child copy of \(R_{h-1}\), merge its recursively chosen root path with
\[
r_hx_h
\quad\text{and}\quad
x_hs_1.
\]
This gives a path from \(r_h\) to a leaf. Partition the other child recursively. Its root part is adjacent to the new root part, so the resulting edge-height is at most \(h\).

Perform this construction in both copies of \(R_h\) forming \(D_h\), and merge their two root paths using the edge between the designated roots. Their union is one path. Rooting the quotient at this merged part gives edge-height at most \(h\).

Hence \(\lambda(D_h)\le h\), completing the proof. ∎

---

## 7. Sharpness of the factor \(2\)

Set
\[
T_k:=D_{2k-1}.
\]
By Lemma 5,
\[
\operatorname{pw}(T_k)
 =\left\lceil\frac{2k}{2}\right\rceil
 =k.
\]
By Lemma 7,
\[
\lambda(T_k)=2k-1.
\]

Therefore, if height counts the number of quotient vertices on a root-to-leaf chain,
\[
H(T_k)=\lambda(T_k)+1=2k.
\]

Thus Lemma 4 is exactly sharp in that convention. If height instead counts quotient edges, then the exact extremal upper bound is \(2k-1\), attained by the same family; in particular, no multiplicative constant smaller than \(2\) is possible.

## Gaps and status

There is no mathematical gap under the standard definition of path-partition as a vertex partition into paths whose contraction is rooted. The extracted prompt omits the source’s precise height normalization, which is why both normalizations were stated explicitly. I have not independently checked the novelty of this construction against the full post-2016 literature or the typeset source definitions, so I would not submit it before those checks.