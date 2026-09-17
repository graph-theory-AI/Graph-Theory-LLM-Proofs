```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "The Δ+2 bound holds even for total list colouring when Δ≥9 and mad(G)<16Δ/(2Δ+9), by a self-contained reducibility and discharging argument.",
  "would_publish": false,
  "caveats": "No claim of novelty; the sparsity hypothesis is substantial, and the unrestricted conjecture is not settled."
}
```

## 1. Scope and partial result

I work with finite simple graphs. I do not obtain a proof of the unrestricted Total Colouring Conjecture. Instead, I prove a sparse-case result, including its list-colouring version, without invoking external colouring theorems. I do not assert that this special-case result is new.

Define the **maximum average degree**
\[
\operatorname{mad}(G)=
\max_{\substack{H\subseteq G\\ |V(H)|>0}}
\frac{2|E(H)|}{|V(H)|}.
\]
A total list colouring chooses the colour of each vertex and edge from its prescribed list, subject to the usual total-colouring constraints. Write \(\chi''_\ell(G)\) for the least \(k\) such that every assignment of lists of size at least \(k\) admits a total colouring.

### Theorem
Let \(D\ge 9\) be an integer and put
\[
a_D=\frac{16D}{2D+9}
    =8-\frac{72}{2D+9}.
\]
If
\[
\Delta(G)\le D
\qquad\text{and}\qquad
\operatorname{mad}(G)<a_D,
\]
then
\[
\boxed{\chi''_\ell(G)\le D+2.}
\]

In particular:

- If \(\Delta(G)\ge14\) and \(\operatorname{mad}(G)\le6\), then the Total Colouring Conjecture holds for \(G\), even with arbitrary lists of size \(\Delta(G)+2\).
- If \(\Delta(G)\ge32\) and \(\operatorname{mad}(G)\le7\), the same conclusion holds.

The proof gives a lower bound on the average degree of a hypothetical minimal obstruction.

## 2. Minimal-obstruction reductions

Fix \(D\) and an assignment \(L\) of lists of size at least \(D+2\). Suppose \(G\) has no total colouring from \(L\), and choose \(G\) minimal under taking subgraphs, with the lists restricted to the remaining vertices and edges. Thus every proper subgraph is colourable from its restricted lists.

Throughout, \(d(v)\) means degree in this minimal obstruction, and \(\Delta(G)\le D\). The reductions in this section are valid whenever \(D\ge5\).

### Lemma 1: A degree-sum restriction
For every edge \(uv\), if
\[
2d(u)\le D+1,
\]
then
\[
d(u)+d(v)\ge D+3.
\]

#### Proof
Suppose instead that \(d(u)+d(v)\le D+2\).

Colour \(G-uv\) by minimality, and then uncolour \(u\). For the edge \(uv\), the coloured conflicting objects are:

- the \(d(u)-1\) other edges at \(u\);
- the \(d(v)-1\) other edges at \(v\);
- the vertex \(v\).

They forbid at most
\[
d(u)+d(v)-1\le D+1
\]
colours. Hence \(uv\) can be coloured from its list.

Now colour \(u\). Its neighbours and incident edges forbid at most
\[
2d(u)\le D+1
\]
colours, so its list also contains an available colour. This restores all constraints, including the vertex-adjacency constraint across \(uv\), and contradicts the choice of \(G\). ∎

An isolated vertex is immediately reducible. Lemma 1 also excludes degrees one and two: for an edge incident with such a vertex, its hypotheses hold and the degree sum is at most \(D+2\). Consequently,
\[
\delta(G)\ge3.
\]

Moreover, when \(d(u)=3\), Lemma 1 gives
\[
3+d(v)\ge D+3
\]
for every neighbour \(v\). Therefore:

\[
\boxed{\text{Every degree-three vertex has only degree-\(D\) neighbours.}}
\]

### Lemma 2: The degree-\(3\)/degree-\(D\) incidence graph is a forest

Let \(B\) be the bipartite graph with parts
\[
V_3=\{v:d(v)=3\},
\qquad
V_D=\{v:d(v)=D\},
\]
containing all edges of \(G\) between these sets. Then \(B\) is a forest.

#### An elementary list-colouring fact
An even cycle can be edge-coloured from arbitrary lists of size at least two.

To see this, restrict each list to two colours. If all lists are identical, alternate their two colours. Otherwise, two cyclically consecutive lists differ. Number the cycle edges \(e_1,\ldots,e_r\) so that
\[
L(e_1)\ne L(e_r),
\]
and choose \(c\in L(e_1)\setminus L(e_r)\). Colour \(e_1\) with \(c\), then colour \(e_2,\ldots,e_r\) greedily. At the last edge, the colour on \(e_1\) is not in its list, so avoiding its predecessor is sufficient.

#### Proof of Lemma 2
Suppose \(B\) contains a cycle \(C\). It is even, alternating between degree-three and degree-\(D\) vertices.

Colour \(G-E(C)\) by minimality. Uncolour all degree-three vertices on \(C\), while leaving everything else coloured.

For a cycle edge \(uv\), where \(d(u)=3\) and \(d(v)=D\), the coloured conflicting objects consist of:

- the one off-cycle edge at \(u\);
- the \(D-2\) off-cycle edges at \(v\);
- the vertex \(v\).

Thus at most \(D\) colours are forbidden, leaving at least two available colours in \(L(uv)\). By the elementary fact above, all edges of \(C\) can be coloured from their available lists.

Finally, recolour the degree-three vertices on \(C\). Each has at most six forbidden colours from its neighbours and incident edges, whereas its list has at least \(D+2\ge7\) colours. These vertices are independent, because every degree-three vertex has only degree-\(D\) neighbours.

This completes a total colouring of \(G\), a contradiction. ∎

### A useful assignment from the forest

Every degree-three vertex has degree exactly three in \(B\). Root each nontrivial component of \(B\) at a degree-\(D\) vertex.

Every degree-three vertex then has one parent and two children, both of degree \(D\). Assign these two children to that degree-three vertex. This gives:

> Each degree-three vertex is assigned two distinct degree-\(D\) neighbours, and each degree-\(D\) vertex is assigned to at most one degree-three vertex.

This bounded assignment is the key improvement over treating each low-degree edge independently.

## 3. Discharging proof of the theorem

Now assume \(D\ge9\), and write
\[
a=a_D=\frac{16D}{2D+9}.
\]
The following inequalities will be used:
\[
4<a<8,\qquad
a\le\frac{D+2}{2},\qquad
a\le\frac{8(D-1)}{D+3}.                    \tag{1}
\]
For completeness, the last two follow from
\[
\frac{D+2}{2}-a
=
\frac{2D^2-19D+18}{2(2D+9)}
=
\frac{(D-9)(2D-1)+9}{2(2D+9)}>0
\]
and
\[
\frac{8(D-1)}{D+3}-a
=
\frac{8(D-9)}{(D+3)(2D+9)}\ge0.
\]

Call a vertex **low** if its degree is less than \(a\).

If \(u\) is low, integrality and (1) give
\[
2d(u)<2a\le D+2
\quad\Longrightarrow\quad
2d(u)\le D+1.
\]
Lemma 1 therefore implies, for every neighbour \(v\),
\[
d(u)+d(v)\ge D+3.                         \tag{2}
\]
In particular, every neighbour of a low vertex has degree greater than \(a\). Hence low vertices are independent.

### Discharging rules

Give each vertex initial charge \(d(v)\), and set
\[
q=\frac{a-4}{4}>0.
\]

Make the following transfers:

1. Each degree-three vertex receives \(q\) from each of its three neighbours.
2. Each degree-three vertex receives an additional \(a/8\) from each of its two assigned degree-\(D\) neighbours.
3. Each low vertex of degree \(i\ge4\) receives
   \[
   \frac{a-i}{i}
   \]
   from each neighbour.

There are no other transfers. All donors are non-low vertices.

We verify that every vertex finishes with charge at least \(a\).

### Case 1: Degree three

Its final charge is
\[
3+3q+2\frac a8
=
3+\frac{3(a-4)}4+\frac a4
=a.
\]

### Case 2: Low degree \(i\ge4\)

Its final charge is
\[
i+i\frac{a-i}{i}=a.
\]

### Case 3: Degree \(D\)

Apart from the additional assigned-neighbour payment, a degree-\(D\) vertex sends at most \(q\) along each incident edge. Indeed, the payment to a degree-three neighbour is \(q\), while the payment to a low neighbour of degree \(i\ge4\) satisfies
\[
\frac{a-i}{i}
=\frac ai-1
\le\frac a4-1=q.
\]

The forest assignment permits at most one additional payment of \(a/8\). Its final charge is therefore at least
\[
D-Dq-\frac a8
=
2D-\frac{(2D+1)a}{8}
=a,
\]
where the last equality uses
\[
a=\frac{16D}{2D+9}.
\]

### Case 4: Non-low degree \(d<D\)

Such a vertex has no degree-three neighbours, since those have only degree-\(D\) neighbours. It makes no assigned-neighbour payment.

If it has no low neighbour, it sends nothing and retains charge \(d\ge a\).

Otherwise, put
\[
m=D+3-d.
\]
Because \(d\le D-1\),
\[
m\ge4.
\]
By (2), every low neighbour has degree \(i\ge m\). The existence of such a neighbour also gives \(m<a\).

The payment along any incident edge is consequently at most
\[
\frac am-1.
\]
Thus the final charge is at least
\[
d-d\left(\frac am-1\right)
=
2d-\frac{da}{m}.                          \tag{3}
\]

We claim that this is at least \(a\). Since
\[
d+m=D+3
\quad\text{and}\quad
4\le m<a\le\frac{D+2}{2},
\]
the function \(x(D+3-x)\) is increasing on the relevant interval. Hence
\[
\frac{2dm}{d+m}
=
\frac{2m(D+3-m)}{D+3}
\ge
\frac{8(D-1)}{D+3}
\ge a,
\]
using (1). Rearranging gives
\[
2d-\frac{da}{m}\ge a,
\]
as required for (3).

### Conclusion

Every vertex finishes with charge at least \(a\). Charge is conserved, so
\[
2|E(G)|=\sum_{v\in V(G)}d(v)\ge a|V(G)|.
\]
Thus every minimal obstruction has average degree at least \(a\).

If the original graph has maximum average degree less than \(a\), none of its subgraphs can be such an obstruction. Therefore every assignment of lists of size \(D+2\) is colourable, proving
\[
\chi''_\ell(G)\le D+2.
\]
This completes the theorem. ∎

Taking \(D=\Delta(G)\), the ordinary total chromatic number satisfies
\[
\Delta(G)+1\le\chi''(G)\le\chi''_\ell(G)\le\Delta(G)+2.
\]
The lower bound follows from a maximum-degree vertex together with its incident edges.

## 4. A simpler sparse consequence, including maximum degree six

The preliminary reductions also yield the following statement.

### Corollary
If \(D\ge5\), \(\Delta(G)\le D\), and
\[
\operatorname{mad}(G)<4,
\]
then
\[
\chi''_\ell(G)\le D+2.
\]

#### Proof
Take a minimal obstruction. By Section 2, it has minimum degree at least three and admits the forest assignment described there.

Start with charge \(d(v)\). Each assigned degree-\(D\) vertex sends \(1/2\) to the degree-three vertex to which it is assigned.

Every degree-three vertex receives two such payments and finishes with charge \(4\). Every degree-\(D\) vertex sends at most \(1/2\), retaining at least
\[
D-\frac12\ge\frac92>4.
\]
Every remaining vertex has degree at least four and sends nothing. Thus the obstruction has average degree at least four, contradicting the maximum-average-degree hypothesis. ∎

For example, this proves total \(8\)-choosability for triangle-free planar graphs of maximum degree six: Euler’s formula gives maximum average degree less than four for every finite simple triangle-free planar graph.

## 5. What remains unresolved

The special-case arguments above are complete, but they do not eliminate dense minimal obstructions.

Their precise conclusion is a necessary density condition:
\[
\text{a minimal obstruction with maximum degree at most \(D\ge9\)}
\quad\Longrightarrow\quad
\overline d(G)\ge\frac{16D}{2D+9}.
\]
That threshold approaches eight, whereas the average degree of a \(D\)-regular graph is \(D\). Thus the density contradiction gives no leverage on the unrestricted regular case, among many others.

Accordingly, this is a proved sparse-case result—not a proof of Behzad’s conjecture and not a claimed improvement over the verified literature.