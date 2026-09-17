```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "A sharp vertex-cover bound proves the conjecture whenever the vertex-cover number is at most Delta + 1.",
  "would_publish": false,
  "caveats": "The general conjecture is not resolved; novelty of the auxiliary bound has not been checked."
}
```

## Partial result: a sharp vertex-cover bound

I obtain a special case of the conjecture, together with an auxiliary upper bound and its equality characterization. The argument is self-contained apart from Hall’s marriage theorem.

Throughout, graphs are finite and simple, and \(\Delta\ge 1\). Write \(\tau(G)\) for the minimum vertex-cover size, and let \(G^\circ\) be obtained by deleting isolated vertices. The edgeless case has strong chromatic number \(1\); the expression \(2\Delta\) requires the usual positive-degree convention.

### Theorem

Let \(G\) have maximum degree \(\Delta\ge1\), and put \(s=\tau(G)\).

1. \(G\) is strongly \(r\)-colorable for every \(r\ge \Delta+s\).
2. If \(G^\circ\) is not complete bipartite, then \(G\) is also strongly \((\Delta+s-1)\)-colorable.
3. If \(G^\circ\) is complete bipartite, then
   \[
   \chi_S(G)=\Delta+s.
   \]

Consequently,
\[
\boxed{\tau(G)\le \Delta+1\quad\Longrightarrow\quad
G\text{ is strongly }2\Delta\text{-colorable}.}
\]

Thus any counterexample to the conjecture must satisfy
\[
\tau(G)\ge \Delta+2.
\]

## 1. An extension lemma

Let \(C\) be a vertex cover and let \(I=V(G)\setminus C\), so \(I\) is independent. Fix a partition \(\mathcal P\) into parts of size at most \(r\).

Suppose that \(C\) has already been colored properly from \([r]\), with distinct colors on \(C\cap B\) for every \(B\in\mathcal P\). Let \(k\) be the number of colors used on \(C\).

For \(x\in I\cap B\), its permissible colors are
\[
L_B(x)=[r]\setminus
\bigl(\{\text{colors on }C\cap B\}
       \cup\{\text{colors on }N_G(x)\cap C\}\bigr).
\]

Because \(I\) is independent, it suffices to find a system of distinct representatives for these lists separately in each part.

**Lemma.** The precoloring extends if:

- \(r-k\ge\Delta\); and
- for every part \(B\) and every color \(a\) not already used on \(C\cap B\), at most \(\Delta\) vertices of \(I\cap B\) have a neighbor in \(C\) colored \(a\).

**Proof.** Fix \(B\), and let \(T_B\) be the colors on \(C\cap B\). Consider a nonempty set \(X\subseteq I\cap B\).

If \(|X|\le\Delta\), every list contains all \(r-k\ge\Delta\) colors unused on \(C\), so Hall’s inequality holds.

If \(|X|>\Delta\), every color outside \(T_B\) is permissible at some vertex of \(X\): otherwise that color would be forbidden by neighbors at more than \(\Delta\) vertices of \(I\cap B\). Therefore
\[
\bigcup_{x\in X}L_B(x)=[r]\setminus T_B.
\]
The cover vertices have distinct colors within \(B\), so
\[
\left|\bigcup_{x\in X}L_B(x)\right|
=r-|C\cap B|
\ge |I\cap B|
\ge |X|.
\]
Hall’s theorem applies. Doing this for every part gives the required coloring. \(\square\)

## 2. The bound \(\Delta+s\)

Choose a vertex cover \(C\) of size \(s\). If \(r\ge\Delta+s\), color all vertices of \(C\) differently.

There are at least \(\Delta\) colors unused on \(C\). Each used color occurs on a single cover vertex and hence is forbidden by neighbors at at most \(\Delta\) vertices in any part. The extension lemma applies.

This proves assertion 1.

## 3. Saving one color outside the complete-bipartite case

Set
\[
r=s+\Delta-1.
\]
Since \(\Delta\ge1\), we can again color \(C\) injectively. Denote this coloring by \(\phi\).

Fix an arbitrary partition into parts of size at most \(r\), and form the lists above. If Hall’s condition holds in every part, we are finished. Otherwise, some part \(B\) contains a nonempty set \(X\subseteq I\cap B\) such that
\[
\left|\bigcup_{x\in X}L_B(x)\right|<|X|.
\]

We identify the structure forced by this failure.

### Every deficient set has size exactly \(\Delta\)

All lists contain the \(r-s=\Delta-1\) colors unused on \(C\). Hence
\[
|X|\ge\Delta.
\]

On the other hand, if \(|X|>\Delta\), no cover vertex can be adjacent to all of \(X\). Because cover colors are distinct, every color not used on \(C\cap B\) would occur in the union of the lists. As in the lemma, Hall’s inequality would then hold.

Thus
\[
|X|=\Delta.
\]

Put
\[
C_B=C\cap B,\qquad t=|C_B|,
\]
and define
\[
Q=\{c\in C\setminus B:X\subseteq N_G(c)\}.
\]
Injectivity of \(\phi\) gives the exact identity
\[
\bigcup_{x\in X}L_B(x)
=[r]\setminus\bigl(\phi(C_B)\cup\phi(Q)\bigr).
\]
Writing \(q=|Q|\), Hall failure yields
\[
r-t-q\le\Delta-1.
\]
Substituting \(r=s+\Delta-1\), we obtain
\[
t+q\ge s.
\]
But \(C_B\) and \(Q\) are disjoint subsets of \(C\), so equality must hold:
\[
t+q=s,\qquad Q=C\setminus B.
\]

Moreover, \(Q\ne\varnothing\). Otherwise \(C\subseteq B\), and
\[
|B|\ge |C|+|X|=s+\Delta=r+1,
\]
contrary to the part-size bound.

Every \(c\in Q\) has all \(\Delta\) vertices of \(X\) as neighbors. The maximum-degree condition therefore forces
\[
N_G(c)=X. \tag{1}
\]

### A deficient part without a cover vertex forces the exception

If \(C_B=\varnothing\), then \(Q=C\). By (1), every cover vertex has neighborhood exactly \(X\).

Since \(I\) is independent, it follows that all edges of \(G\) are precisely the edges between \(C\) and \(X\). Every vertex outside \(C\cup X\) is isolated. Thus
\[
G^\circ=K_{s,\Delta}.
\]

Under the hypothesis that \(G^\circ\) is not complete bipartite, this case is impossible. Hence \(C_B\ne\varnothing\).

### One color identification repairs the extension problem

Choose
\[
c\in Q,\qquad u\in C_B.
\]
By (1), \(c\) has no neighbors outside \(X\subseteq I\cap B\). In particular, \(c\) and \(u\) are nonadjacent.

Change the color of \(c\) to the color of \(u\), leaving all other cover colors unchanged.

This remains a proper coloring of \(G[C]\). It also remains injective on every \(C\cap D\): the only repeated-color pair is \(c,u\), and these vertices lie in different partition parts.

The new cover coloring uses \(s-1\) colors, leaving
\[
r-(s-1)=\Delta
\]
unused colors. We check the extension lemma.

Every unmerged color occurs on a single cover vertex, so it excludes at most \(\Delta\) vertices in any part. For the merged color:

- in \(B\), it is already used on \(u\in C_B\), so the lemma imposes no neighborhood condition on it there;
- in every other part \(D\ne B\), vertex \(c\) has no neighbors, by (1). Thus the merged color is forbidden by neighbors only through \(u\), at at most \(\Delta\) vertices of \(I\cap D\).

All conditions of the extension lemma hold. Therefore the coloring extends.

This proves assertion 2. Every larger integer \(r\) is already covered by assertion 1.

## 4. The exceptional graphs and sharpness

Suppose
\[
G^\circ=K_{a,b},\qquad 1\le a\le b.
\]
Then \(\Delta=b\) and \(\tau(G)=a\). Assertion 1 gives
\[
\chi_S(G)\le a+b.
\]

For the reverse inequality, let \(r<a+b\).

- If \(r\ge b\), take the two bipartition classes as partition parts. Vertices within each class must have distinct colors, and every vertex in one class is adjacent to every vertex in the other. Thus all \(a+b\) nonisolated vertices require different colors.
- If \(r<b\), put \(r\) vertices from the class of size \(b\) into one part, and put a vertex from the other class into a singleton part. These vertices require \(r+1\) colors.

All remaining vertices can be placed in singleton parts. Hence \(G\) is not strongly \(r\)-colorable for any \(r<a+b\), proving
\[
\chi_S(G)=a+b=\Delta+\tau(G).
\]

In particular, \(K_{\Delta,\Delta}\) demonstrates that the conjectured factor \(2\) cannot be improved.

## 5. Consequences for the conjecture

If \(s\le\Delta\), assertion 1 applies directly at \(r=2\Delta\).

If \(s=\Delta+1\), then \(G^\circ\) cannot be complete bipartite: a complete bipartite graph always has vertex-cover number at most its maximum degree. Assertion 2 therefore gives
\[
r=\Delta+s-1=2\Delta.
\]

There is also a strict improvement within the smaller-cover range:
\[
\tau(G)\le\Delta,\quad G^\circ\ne K_{\Delta,\Delta}
\quad\Longrightarrow\quad
G\text{ is strongly }(2\Delta-1)\text{-colorable}.
\]
Indeed, use assertion 1 when \(s<\Delta\), and assertion 2 when \(s=\Delta\).

The proof is constructive once a suitable vertex cover is supplied. It uses bipartite matching for the lists, and in the improved-bound case needs at most one identification of two cover colors.

## What remains unresolved

The argument does not establish strong \(2\Delta\)-colorability when
\[
\tau(G)\ge\Delta+2.
\]
Already at \(\tau(G)=\Delta+2\), its general upper bound is \(2\Delta+1\), rather than \(2\Delta\). The vertex-cover number can be arbitrarily large while \(\Delta\) stays fixed, so this does not settle the difficult sparse regime.

The hypothesis concerns the **global** vertex-cover number. The proof does not give a componentwise extension: prescribed partition parts may meet many different components.

Thus this is a proved special case and an auxiliary extremal characterization, not a proof of the unrestricted strong-colorability conjecture.