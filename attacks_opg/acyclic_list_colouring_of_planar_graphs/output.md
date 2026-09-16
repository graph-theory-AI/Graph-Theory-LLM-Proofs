```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Every graph with maximum average degree less than 10/3 is acyclically 5-choosable, but the unrestricted planar conjecture is not resolved here.",
  "would_publish": false,
  "caveats": "The sparse-graph result below is proved self-containedly; no claim of novelty is made, and its literature status has not been checked."
}
```

# 1. Statement of the partial result

An **acyclic colouring** is a proper vertex colouring with no bichromatic cycle. A graph is **acyclically 5-choosable** if every assignment of lists of at least five colours admits an acyclic colouring from those lists.

Write
\[
\operatorname{mad}(G)=
\max_{\varnothing\ne H\subseteq G}\frac{2|E(H)|}{|V(H)|}.
\]

I prove the following special case, independently of planarity.

**Theorem.** Every finite simple graph \(G\) satisfying
\[
\operatorname{mad}(G)<\frac{10}{3}
\]
is acyclically 5-choosable.

Consequently, the conjecture holds for planar graphs satisfying this density restriction, including every planar graph of girth at least five. The density restriction also allows triangles and 4-cycles; it is not simply a forbidden-cycle hypothesis.

This is not advertised as a new sparse-colouring theorem. The contribution here is a complete, self-contained argument and an explicit account of where it stops short of the planar conjecture.

# 2. Extension tools

We may trim every list to size exactly five.

## 2.1. Adding a vertex with two coloured neighbours

Suppose \(H\) is acyclically coloured, and a new vertex \(z\) has two neighbours \(x,y\) in \(H\).

If \(x,y\) have different colours, every colour for \(z\) avoiding those two colours is safe.

If they both have colour \(a\), a colour \(b\ne a\) is unsafe precisely when \(H\) contains an \(a,b\)-coloured \(x\)-\(y\) path. Every such colour \(b\) occurs on a neighbour of \(x\), so the number of unsafe colours other than \(a\) is at most \(d_H(x)\).

In particular:

* if \(d_G(x)\le3\), and \(z\) is an uncoloured neighbour of \(x\), at least two colours remain available for \(z\);
* if \(d_G(x)\le4\), at least one remains.

Here and below, “available” in such a statement includes both properness and acyclicity.

## 2.2. Restoring degree-two neighbours

The following observation will handle most reductions.

Let \(S\) be a set of vertices, and let \(T\) be the set of degree-two vertices adjacent to \(S\). Assume that \(T\) is independent. Suppose \(G-T\) has already been acyclically coloured, including \(S\), and that any vertex of \(T\) whose two ends lie in \(S\) has differently coloured ends.

For \(v\in S\), call \(z\in T\), with other neighbour \(w\notin S\), **active at \(v\)** when
\[
\phi(w)=\phi(v).
\]
Let \(r(v)\) be the number of distinct colours on the neighbours of \(v\) outside \(T\).

It suffices to colour the active vertices at \(v\):

1. with pairwise distinct colours; and
2. avoiding \(\phi(v)\) and all colours on \(N(v)\setminus T\).

Each active vertex has at least \(4-r(v)\) colours after these exclusions. Thus this can be done whenever
\[
\#\{\text{vertices active at }v\}\le 4-r(v). \tag{1}
\]

Every remaining vertex of \(T\) has differently coloured ends and can receive any colour avoiding its ends.

To verify acyclicity, a bichromatic cycle through a degree-two vertex must have equally coloured ends at that vertex. Thus it cannot use any of the latter, inactive vertices. If it uses a vertex active at \(v\), its other edge at \(v\) cannot go to a direct neighbour of \(v\), by condition 2, or to another active vertex, by condition 1. This is a contradiction.

## 2.3. Two adjacent new vertices

Suppose two adjacent vertices \(u,v\) are added to an acyclically coloured graph \(H\). Let \(P,Q\) be the sets of colours on their respective neighbours in \(H\).

Suppose \(p\in L(u)\) and \(q\in L(v)\) are individually safe when adding just their respective vertex to \(H\). Then colouring \(u,v\) with \(p,q\) is safe provided
\[
p\ne q
\quad\text{and}\quad
\neg(p\in Q\ \text{and}\ q\in P). \tag{2}
\]

Indeed, a new bichromatic cycle containing both vertices would have colour set \(\{p,q\}\). Each of \(u,v\) would have a neighbour on that cycle in \(H\), forcing \(q\in P\) and \(p\in Q\).

# 3. A minimum counterexample and its local structure

Assume the theorem is false. Choose a counterexample \((G,L)\) with as few vertices as possible. Every vertex-deleted subgraph can therefore be acyclically coloured from its restricted lists.

All reductions below use vertex deletion only. In particular, they preserve the maximum-average-degree hypothesis.

Put
\[
t(v)=|\{x\in N(v):d(x)=2\}|,\qquad s(v)=d(v)-t(v).
\]
Call neighbours not of degree two **direct neighbours**.

## 3.1. Basic degree restrictions

There is no vertex of degree at most one.

There is also no degree-two vertex with a neighbour of degree at most four: delete the degree-two vertex and use Section 2.1. Therefore
\[
\text{every degree-two vertex has two neighbours of degree at least five.} \tag{3}
\]
In particular, degree-two vertices form an independent set.

Next, there is no degree-three vertex whose neighbour degrees are \(3,3,\le4\).

To see this, delete such a vertex \(v\).

* If its neighbours have three distinct colours, extend immediately.
* If exactly two neighbours have the same colour, one of that pair has degree at most three. At most two colours are unsafe because of a bichromatic path, in addition to the two neighbour colours.
* If all three neighbours have the same colour \(a\), their total degree in \(G-v\) is at most
  \[
  2+2+3=7.
  \]
  Every unsafe colour \(b\ne a\) must occur at two of these neighbour incidences. Consequently there are at most \(\lfloor7/2\rfloor=3\) such colours.

In each case, at most four colours are forbidden.

A degree-three vertex thus has zero, one, or two degree-three neighbours. Call these **types \(0,1,2\)**, respectively. A type-2 vertex has its remaining neighbour of degree at least five.

## 3.2. One centre and its degree-two neighbours

The following configurations are reducible:

\[
\begin{array}{ll}
\text{(a)}&d(v)\le9,\quad s(v)\le1;\\
\text{(b)}&s(v)=2,\quad t(v)\le7,\quad
          \text{one direct neighbour has degree at most three};\\
\text{(c)}&s(v)=2,\quad t(v)\le3,\quad
          \text{one direct neighbour has degree at most four}.
\end{array} \tag{4}
\]

Delete \(v\) and its degree-two neighbours, and colour the remainder.

For (a), at least four colours remain for \(v\). Among at most nine far-end colours of its degree-two neighbours, some available colour occurs at most twice. Choose it. Since \(r(v)\le1\), inequality (1) holds.

For (b), if the two direct-neighbour colours differ, at least three colours remain for \(v\); one occurs on at most two of the at most seven far ends. Here \(r(v)=2\). If the direct-neighbour colours agree, Section 2.1 leaves at least two safe colours for \(v\); one occurs on at most three far ends, and \(r(v)=1\).

For (c), different direct-neighbour colours again cause no difficulty. If they agree, Section 2.1 leaves at least one safe colour, and all three degree-two neighbours can be active because \(r(v)=1\).

Define
\[
\mathcal A=\{v:d(v)=5,\ t(v)=3\}.
\]
By (4c), both direct neighbours of every vertex in \(\mathcal A\) have degree at least five.

Also, (4a) gives
\[
\begin{array}{c|ccccc}
d(v)&5&6&7&8&9\\ \hline
t(v)\text{ is at most}&3&4&5&6&7.
\end{array} \tag{5}
\]
By (4b), vertices with \((d,t)=(6,4)\) or \((7,5)\) have no degree-three neighbour.

## 3.3. A three-direct-neighbour reduction

The following configuration is reducible:

* \(s(v)=3\) and \(t(v)\le3\);
* one direct neighbour \(x\) has degree three and has another degree-three neighbour;
* one of the other two direct neighbours of \(v\) has degree three.

Delete \(v,x\), and all degree-two neighbours of \(v\). The latter have their other ends in the coloured remainder, by (3).

Let \(P\) be the colour set on the two remaining direct neighbours of \(v\), and \(Q\) the colour set on the two remaining neighbours of \(x\). Let \(X,Y\) be the colours individually safe for \(v,x\), respectively. Section 2.1 gives
\[
|X|\ge
\begin{cases}
2,&|P|=1,\\
3,&|P|=2,
\end{cases}
\qquad
|Y|\ge
\begin{cases}
2,&|Q|=1,\\
3,&|Q|=2.
\end{cases} \tag{6}
\]

Put \(k=3-|P|\). Exclude from \(X\) any colour appearing at least \(k+1\) times among the far ends of the degree-two neighbours of \(v\). Since there are at most three such ends, at most one colour is excluded. The resulting set \(X'\) satisfies
\[
|X'|\ge1\quad\text{if }|P|=1,
\qquad
|X'|\ge2\quad\text{if }|P|=2. \tag{7}
\]

We can choose \(p\in X'\), \(q\in Y\) satisfying (2):

* If \(|P|=1\), take any \(p\in X'\). When \(p\notin Q\), choose \(q\ne p\). When \(p\in Q\), we have \(p\notin Y\), and can choose \(q\in Y\setminus P\).
* If \(|P|=2\) and \(|Q|=1\), choose \(p\in X'\setminus Q\), then \(q\ne p\).
* If \(|P|=|Q|=2\), choose \(q\in Y\setminus P\), then \(p\ne q\).

The colouring of the two centres is acyclic. At \(v\), there are at most \(k\) active degree-two neighbours and at most \(|P|+1\) direct-neighbour colours, so (1) applies.

Two useful consequences are:

1. type-2 degree-three vertices form an independent set;
2. if \((d(v),t(v))\) is \((5,2)\) or \((6,3)\), and \(v\) has at least two degree-three neighbours, then all its degree-three neighbours have type \(0\).

For consequence 1, apply the reduction to two adjacent type-2 vertices, with \(t(v)=0\). Consequence 2 follows by choosing a non-type-0 neighbour as \(x\).

## 3.4. Two adjacent centres with two direct neighbours each

There cannot be adjacent vertices \(u,v\) each having exactly two direct neighbours and at most five degree-two neighbours.

Delete the two centres and all their degree-two neighbours. Let \(a,b\) be the colours on their respective remaining direct neighbours.

For each centre, exclude \(a,b\), and also exclude any colour occurring at least three times on its external far ends. At most one colour is excluded for the latter reason. Thus each centre retains at least two colours, and they can receive distinct colours.

Section 2.3 gives acyclicity on the centres and the old graph. Each centre has at most two active degree-two neighbours and at most two direct-neighbour colours. Degree-two vertices between the centres have differently coloured ends. Section 2.2 completes the extension.

Consequently:
\[
\mathcal A\text{ is independent, and no vertex in }\mathcal A
\text{ is adjacent to a vertex with }(d,t)=(6,4). \tag{8}
\]

## 3.5. An edge from a \((5,2)\)-vertex to \(\mathcal A\)

Suppose \(d(u)=5,t(u)=2\), and \(u\) has a degree-three neighbour. Then \(u\) has no neighbour in \(\mathcal A\).

For otherwise, let \(v\in\mathcal A\) be adjacent to \(u\). Delete \(u,v\) and all their degree-two neighbours. Let \(P\) be the colours on the two remaining direct neighbours of \(u\); one of those neighbours has degree three. Let \(c\) be the colour on the other direct neighbour of \(v\).

The individually safe set \(X\) for \(u\) has size at least two if \(|P|=1\), and at least three if \(|P|=2\). In the latter case, exclude a colour if it occurs on both external far ends at \(u\). This leaves a set \(X'\) of size at least two.

Choose the colour \(q\) for \(v\) avoiding:

* \(c\);
* the colours in \(P\);
* a colour occurring on all three external far ends at \(v\), if there is one.

At most four colours are excluded, so this is possible. Choose \(p\in X'\setminus\{q\}\).

Since \(q\notin P\), condition (2) holds. At \(v\), at most two degree-two neighbours are active. At \(u\), at most two are active if \(|P|=1\), and at most one if \(|P|=2\). These are precisely the bounds needed in (1).

Thus
\[
d(u)=5,\ t(u)=2,\ N(u)\cap V_3\ne\varnothing
\quad\Longrightarrow\quad N(u)\cap\mathcal A=\varnothing. \tag{9}
\]

## 3.6. A \((5,1)\)-vertex with three type-2 neighbours

A vertex \(v\) with \(d(v)=5,t(v)=1\) has at most two type-2 degree-three neighbours.

Suppose otherwise, and choose three such neighbours \(x_1,x_2,x_3\). They are independent by Section 3.3. Let \(a\) be the remaining direct neighbour of \(v\), and let \(z,w\) be its degree-two neighbour and the other neighbour of \(z\).

Delete \(v,z,x_1,x_2,x_3\), and colour the remainder. For each \(i\), let \(P_i\) be the colour set on the two remaining neighbours of \(x_i\). Both of those vertices have degree three, and \(|P_i|\in\{1,2\}\).

There are at least three possible colours for \(v\) after excluding \(\phi(a),\phi(w)\). We claim that one such colour \(p\) satisfies:

* \(p\) belongs to at most two of \(P_1,P_2,P_3\);
* if it belongs to two, those two sets are not both singletons.

There are at most two colours failing these conditions. Indeed, if two singleton sets coincide, their common colour is the only possible failing colour. Otherwise the failing colours lie in \(P_1\cap P_2\cap P_3\), a set of size at most two.

Fix such a \(p\), and call \(x_i\) active when \(p\in P_i\).

Now colour the \(x_i\) successively, maintaining acyclicity. At every step, Section 2.1 leaves at least two available colours if \(|P_i|=1\), and at least three if \(|P_i|=2\).

Colour the active vertices first, requiring their colours to be distinct and to avoid \(\phi(a)\). If there are two, colour a singleton-set vertex first, if present. The second then has \(|P_i|=2\), and its at least three available colours suffice to avoid \(\phi(a)\) and the first active colour. The colour \(p\) is already excluded by properness at active vertices.

Colour each inactive \(x_i\) while also avoiding \(p\); at least one colour remains.

Add \(v\) with colour \(p\). A bichromatic cycle through \(v\) using an edge \(vx_i\) would require \(x_i\) to be active. But the active colours are distinct and avoid \(\phi(a)\), so no such cycle exists. Finally, \(z\) has differently coloured ends and can be restored safely.

## 3.7. A \((5,2)\)-vertex with three neighbours in \(\mathcal A\)

A vertex \(u\) with \(d(u)=5,t(u)=2\) has at most two neighbours in \(\mathcal A\).

Suppose its three direct neighbours \(v_1,v_2,v_3\) all belong to \(\mathcal A\). They are independent by (8). Let \(a_i\) be the other direct neighbour of \(v_i\).

Delete
\[
S=\{u,v_1,v_2,v_3\}
\]
and all degree-two vertices adjacent to \(S\), and colour the remainder.

Choose a colour \(p\) for \(u\) avoiding:

* \(\phi(a_1),\phi(a_2),\phi(a_3)\);
* a colour occurring on both external far ends at \(u\), if there is one.

At most four colours are excluded.

Form an auxiliary graph \(F\) on \(v_1,v_2,v_3\), joining two vertices when they have a common degree-two neighbour in \(G\).

For each \(v_i\), exclude \(p,\phi(a_i)\). If \(v_i\) is isolated in \(F\), also exclude a colour occurring on all three of its external far ends, if there is one.

A nonisolated vertex of \(F\) has at most two external far ends, and retains at least three colours. An isolated vertex retains at least two. Since \(F\) has three vertices, it can be properly coloured from these lists.

All degree-two vertices with both ends in \(S\) now have differently coloured ends. The colouring before restoring them is acyclic: any cycle meeting \(S\) contains a path \(u v_i a_i\), whose three colours are distinct.

There is at most one active degree-two neighbour at \(u\), and at most two at each \(v_i\). Since \(r(u)\le3\) and \(r(v_i)\le2\), Section 2.2 finishes the extension.

# 4. Discharging

Give every vertex initial charge \(d(v)\). Transfer charge as follows.

1. Every degree-two vertex receives \(2/3\) from each neighbour.
2. A degree-three vertex receives from each neighbour of degree at least four:
   \[
   \begin{cases}
   1/9,&\text{if it has type }0,\\
   1/6,&\text{if it has type }1,\\
   1/3,&\text{if it has type }2.
   \end{cases}
   \]
3. Every vertex in \(\mathcal A\) receives \(1/6\) from each of its two direct neighbours.

I verify that every final charge is at least \(10/3\).

## 4.1. Degrees two, three, and four

A degree-two vertex finishes with
\[
2+2(2/3)=10/3.
\]

A degree-three vertex receives exactly \(1/3\), because it has respectively three, two, or one higher-degree neighbours.

A degree-four vertex has no degree-two neighbour, no type-2 degree-three neighbour, and no neighbour in \(\mathcal A\). It therefore sends at most \(4/6\), finishing with at least
\[
4-\frac46=\frac{10}{3}.
\]

## 4.2. Vertices in \(\mathcal A\)

Such a vertex sends \(3(2/3)=2\), receives \(2(1/6)=1/3\), and makes no other payments. Its final charge is
\[
5-2+\frac13=\frac{10}{3}.
\]

## 4.3. Other degree-five vertices

They have \(t\le2\).

* If \(t=0\), total outgoing charge is at most \(5/3\).
* If \(t=1\), Section 3.6 allows at most two type-2 neighbours. Thus total outgoing charge is at most
  \[
  \frac23+2\left(\frac13\right)+2\left(\frac16\right)=\frac53.
  \]
* Suppose \(t=2\), and let \(m\) count degree-three neighbours.
  * If \(m\ge2\), all are type \(0\), by Section 3.3, and there is no neighbour in \(\mathcal A\), by (9). Total outgoing charge is at most
    \[
    \frac43+\frac39=\frac53.
    \]
  * If \(m=1\), there is again no neighbour in \(\mathcal A\), so outgoing charge is at most \(4/3+1/3=5/3\).
  * If \(m=0\), Section 3.7 allows at most two neighbours in \(\mathcal A\), so outgoing charge is at most \(4/3+2/6=5/3\).

Every degree-five vertex therefore finishes with at least \(10/3\).

## 4.4. Degree-six vertices

Here \(t\le4\).

If \(t\le2\), outgoing charge is at most
\[
\frac{2t}{3}+\frac{6-t}{3}
=\frac{6+t}{3}\le\frac83.
\]

If \(t=3\), the degree-two payments total \(2\). Among the three direct neighbours:

* if at least two have degree three, they all have type \(0\); their payments, together with any payment to \(\mathcal A\), total at most
  \[
  \max\left\{\frac39,\frac29+\frac16\right\}\le\frac23;
  \]
* if at most one has degree three, the total is at most
  \[
  \frac13+2\left(\frac16\right)=\frac23.
  \]

If \(t=4\), the other neighbours are neither degree-three vertices nor members of \(\mathcal A\), by (4b) and (8). Outgoing charge is exactly \(8/3\).

Thus every degree-six vertex finishes with at least \(6-8/3=10/3\).

## 4.5. Larger degrees

For a vertex of degree \(d\), with \(t\) degree-two neighbours, the general outgoing bound is
\[
\frac{2t}{3}+\frac{d-t}{3}=\frac{d+t}{3}. \tag{10}
\]

* For \(d=7,t\le4\), this is at most \(11/3\).
* For \(d=7,t=5\), the two direct neighbours do not have degree three. Hence outgoing charge is at most
  \[
  \frac{10}{3}+\frac26=\frac{11}{3}.
  \]
* For \(d=8\), we have \(t\le6\), and (10) is at most \(14/3\).
* For \(d=9\), we have \(t\le7\), and (10) is at most \(16/3\).
* For \(d\ge10\), every neighbour receives at most \(2/3\), leaving charge at least \(d/3\ge10/3\).

Every vertex finishes with charge at least \(10/3\). Since charge is conserved,
\[
\frac{2|E(G)|}{|V(G)|}\ge\frac{10}{3},
\]
contrary to \(\operatorname{mad}(G)<10/3\).

This proves the theorem. \(\square\)

# 5. Planar consequences and the remaining gap

For a planar graph of girth at least five, Euler's inequality, applied to its subgraphs, gives
\[
\operatorname{mad}(G)<\frac{10}{3}.
\]
Forest components satisfy an even stronger bound. Hence the theorem proves acyclic 5-choosability for that planar class.

It does **not** improve the unrestricted planar bound of seven quoted in the question.

There is a useful distinction between the sparse argument above and the unresolved planar case. A minimum-order counterexample to the full planar conjecture would have minimum degree at least four. Indeed, if \(d(v)\le3\), delete \(v\) and join its neighbours pairwise. This can be done planarly—the degree-three operation is the planar \(Y\)-to-\(\Delta\) replacement. Minimality gives an acyclic list colouring of the smaller graph. The neighbours of \(v\) then have distinct colours, so \(v\) can be restored without creating a bichromatic cycle.

Thus a minimum planar counterexample, if one exists, lies precisely beyond the low-degree regime controlled by the density argument. Planarity permits substantial degree-four and degree-five cores, including triangulations, and none of the reductions proved here eliminates all such cores.

**Conclusion.** The sparse theorem is complete. The assertion that **every planar graph is acyclically 5-choosable** remains unproved and undisproved by this argument.