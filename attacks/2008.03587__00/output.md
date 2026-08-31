```json
{
  "verdict": "partial",
  "confidence": "high",
  "one_line": "Pendant extensions satisfy a useful sandwich, preserve the zombie number whenever z(G)≤2 or z(G)=c(G), and any counterexample must exploit a genuinely mixed active/delayed initial configuration.",
  "would_publish": false,
  "caveats": "The central mixed-delay case remains unresolved; the argument assumes finite connected graphs and the standard rule that the survivor may stay put."
}
```

# Mathematical writeup

## 1. Conventions and statement

I use the standard deterministic-zombie rules from the source paper:

- Zombies choose their initial vertices, then the survivor chooses theirs.
- In each round, every zombie moves first and must traverse an edge that decreases its distance to the current survivor by one.
- The survivor then may stay or move to a neighbor.
- Capture occurs as soon as a zombie and the survivor occupy the same vertex.

All graphs are finite, connected, and nonempty.

Let \(H\) be obtained from \(G\) by successively adding degree-one vertices. The vertices outside \(G\) induce rooted trees, each attached to a unique root in \(G\). Let

\[
\rho:V(H)\longrightarrow V(G)
\]

map every vertex in such a tree to its root and fix every vertex of \(G\).

The following gives a partial answer.

### Theorem

Let \(H\) be any pendant-forest extension of \(G\).

1. \[
   z(H)\le z(G).
   \]

2. If \(z(G)>1\), then \(z(H)>1\). Consequently,
   \[
   z(H)=z(G)\qquad\text{whenever }z(G)\le 2.
   \]

3. The ordinary cop number is unchanged:
   \[
   c(H)=c(G).
   \]
   Hence
   \[
   z(H)=z(G)
   \qquad\text{whenever }z(G)=c(G).
   \]

4. Define \(z_{\mathrm{pass}}(G)\) to be the minimum number of zombies needed when each zombie is additionally allowed to stay put on any turn. Then
   \[
   c(G)=c(H)\le z_{\mathrm{pass}}(G)\le z(H)\le z(G).
   \]
   Thus the conjecture holds for every graph satisfying
   \(z_{\mathrm{pass}}(G)=z(G)\).

5. The conjecture is exactly a question about unequal initial release times. More precisely, define \(z_{\mathrm{rel}}(G)\) by allowing zombie \(i\) to choose a root \(r_i\in V(G)\) and a finite delay \(d_i\), during which it travels down a private formal path and reaches \(r_i\) only after \(d_i\) zombie moves. Then
   \[
   z_{\mathrm{rel}}(G)
   =
   \min\{z(H):H\text{ is a pendant-forest extension of }G\},
   \]
   and
   \[
   z_{\mathrm{pass}}(G)\le z_{\mathrm{rel}}(G)\le z(G).
   \]

In particular, equal delays cannot help. Any strict counterexample must use at least two distinct release times.

---

## 2. Pendant extensions cannot increase \(z\)

Let \(k=z(G)\), and place the \(k\) zombies in \(G\) according to a winning strategy on \(G\).

Suppose the survivor is at \(s\in V(H)\), with \(r=\rho(s)\). For every zombie \(u\in V(G)\),

\[
d_H(u,s)=d_G(u,r)+d_H(r,s).
\]

Therefore, any move \(u\to u'\) satisfying

\[
d_G(u',r)=d_G(u,r)-1
\]

also satisfies

\[
d_H(u',s)=d_H(u,s)-1.
\]

The zombies can consequently play their winning strategy in \(G\) against the projected survivor \(\rho(s)\). A survivor move inside an attached tree projects to a pass at its root, and a move along an edge of \(G\) projects to the same edge, so the projected survivor trajectory is legal.

Eventually the simulated strategy places some zombie at \(\rho(s)\). If \(s=\rho(s)\), this is an actual capture. Otherwise the survivor lies in the rooted tree attached there. The zombie at the root then follows the unique path toward the survivor. The survivor cannot pass through that zombie to return to \(G\). After each zombie move, the component of the tree still available to the survivor strictly shrinks, so capture occurs in finitely many rounds.

Thus

\[
z(H)\le z(G).
\]

---

## 3. A single zombie never benefits from pendant starting positions

Assume \(z(G)>1\), and consider an arbitrary starting vertex \(y\in V(H)\) for one zombie. Let

\[
r=\rho(y),\qquad d=d_H(y,r).
\]

Since one zombie starting at \(r\) does not win on \(G\), there is a survivor starting vertex \(s\in V(G)\) and an evasion strategy against that zombie.

Necessarily

\[
d_G(r,s)\ge 2,
\]

because a zombie at distance zero or one captures on its first move.

The survivor now starts at \(s\) in \(H\) and stays there during the first \(d\) rounds. Since the survivor is in \(G\), the zombie at \(y\) is forced to follow the unique path toward \(r\). After \(d\) zombie moves it reaches \(r\). The survivor stays once more after that landing move. At the start of the next zombie phase, the state is exactly the original losing state \((r,s)\) in \(G\), and the survivor switches to their winning strategy there.

Therefore no one-zombie starting vertex wins on \(H\). Hence

\[
z(G)>1\implies z(H)>1.
\]

Combining this with \(z(H)\le z(G)\) gives

\[
z(H)=z(G)
\quad\text{for }z(G)\in\{1,2\}.
\]

---

## 4. The cop-number criterion

The graph \(G\) is a retract of \(H\) in the pursuit-game sense: projecting an edge of an attached tree either collapses it to its root or maps it to an edge of \(G\).

A cop strategy on \(G\) extends to \(H\) by projecting the robber to \(G\), and after reaching the root of the robber’s tree, chasing down that tree. Thus

\[
c(H)\le c(G).
\]

Conversely, play a virtual winning cop strategy in \(H\) against a robber constrained to \(G\), and project every virtual cop through \(\rho\). A virtual cop move projects to either an edge move or a pass, both legal for an ordinary cop. If the virtual cop captures the robber in \(G\), its projection captures as well. Thus

\[
c(G)\le c(H).
\]

Therefore

\[
c(H)=c(G).
\]

Since every zombie strategy is a legal cop strategy,

\[
c(X)\le z(X)
\]

for every graph \(X\). Hence, if \(z(G)=c(G)\),

\[
z(G)=c(G)=c(H)\le z(H)\le z(G),
\]

so equality holds throughout.

Thus a counterexample must have a strict cop/zombie gap:

\[
c(G)<z(G).
\]

---

## 5. Zombies allowed to pass

Define \(z_{\mathrm{pass}}(G)\) as the minimum number of zombies needed if, on each zombie turn, every zombie may either

- stay where it is, or
- make an ordinary distance-decreasing zombie move.

This is a stronger pursuer than an ordinary zombie but weaker than an unrestricted cop, so

\[
c(G)\le z_{\mathrm{pass}}(G)\le z(G).
\]

I claim that

\[
z_{\mathrm{pass}}(G)\le z(H).
\]

Indeed, suppose \(k<z_{\mathrm{pass}}(G)\), and let \(k\) zombies be placed arbitrarily in \(H\). Project their starting positions to \(G\), and let the survivor remain in \(G\).

While an actual zombie is outside \(G\), its unique shortest path toward the survivor goes toward its root, and its projection stays at that root. Once the zombie is in \(G\), its projected move is an ordinary distance-decreasing move in \(G\). Thus every projected actual trajectory is a legal pass-zombie trajectory.

By the definition of \(z_{\mathrm{pass}}(G)\), the survivor has a strategy in \(G\) evading these projected zombies. An actual capture in \(G\) would give a projected capture, so the same strategy evades the zombies in \(H\).

Therefore

\[
c(G)=c(H)\le z_{\mathrm{pass}}(G)\le z(H)\le z(G).
\]

This proves the conjecture for any graph for which permitting arbitrary passes does not lower the zombie number.

---

## 6. Exact reformulation by release times

Define a release-time zombie game on \(G\) as follows. Before the survivor chooses a start, zombie \(i\) selects

\[
(r_i,d_i)\in V(G)\times\mathbb N_0.
\]

For \(d_i>0\), regard the zombie as traveling along a private path of length \(d_i\) whose endpoint in \(G\) is \(r_i\). It reaches \(r_i\) on its \(d_i\)-th move and makes its first ordinary move inside \(G\) on the following zombie turn. Let \(z_{\mathrm{rel}}(G)\) be the minimum number of such zombies required.

### Proposition

\[
z_{\mathrm{rel}}(G)
=
\min\{z(H):H\text{ is a pendant-forest extension of }G\}.
\]

### Proof

If \(H\) has a winning placement \(y_1,\dots,y_k\), constrain the survivor to \(G\). For each \(i\), let

\[
r_i=\rho(y_i),\qquad d_i=d_H(y_i,r_i).
\]

Until zombie \(i\) reaches \(r_i\), its route is forced. Thus the play restricted to \(G\) is exactly a release-time game with data \((r_i,d_i)\). Hence

\[
z_{\mathrm{rel}}(G)\le z(H).
\]

Conversely, suppose \(k\) release-time zombies win on \(G\), with data \((r_i,d_i)\). Attach a private pendant path of length \(d_i\) at \(r_i\), and start zombie \(i\) at its outer endpoint. Against a survivor whose projection remains in \(G\), these paths realize precisely the prescribed release times.

If the survivor starts in or enters one of the private paths, use the projected release-time strategy. When the projected strategy reaches the corresponding root, the zombie there separates the survivor from \(G\) and catches them along the finite path. Therefore the same \(k\) zombies win the constructed extension.

This proves the equality.

Consequently, the original conjecture is equivalent to

\[
z_{\mathrm{rel}}(G)=z(G)
\qquad\text{for every }G.
\]

### Equal release times do not help

Suppose all \(k\) zombies have the same delay \(d\), with roots \(r_1,\dots,r_k\), and \(k<z(G)\). The ordinary starting configuration \((r_1,\dots,r_k)\) is not globally winning, so choose a survivor start \(s\) and an evasion strategy against it. Again \(d_G(r_i,s)\ge2\) for every \(i\).

The survivor stays at \(s\) until all zombies have reached their roots and then stays once after their landing move. The resulting state is exactly the ordinary losing state with roots \(r_i\), so the survivor can evade indefinitely.

Thus only unequal release times can matter.

---

## 7. Necessary shape of a counterexample

It is enough to consider the addition of one leaf. Indeed, in any sequence

\[
G=G_0\subseteq G_1\subseteq\cdots\subseteq G_m=G',
\]

where each \(G_i\) is obtained from \(G_{i-1}\) by one leaf addition, the zombie numbers are nonincreasing. If \(z(G')<z(G)\), some individual step is strict.

Let \(H=G+x\), where \(x\) is a new leaf adjacent to \(v\), and suppose

\[
z(H)=k<z(G).
\]

Then every winning \(k\)-zombie initial placement in \(H\) must satisfy:

1. At least one zombie starts at \(x\).  
   Otherwise all zombies start in \(G\), and against a survivor remaining in \(G\) no shortest zombie move uses \(x\). The same placement and strategy would win on \(G\).

2. At least one zombie starts in \(G\).  
   If all \(k\) zombies start at \(x\), they all have the same one-round delay and the same root \(v\), which cannot improve on an ordinary \(k\)-zombie configuration by the equal-delay argument.

3. Necessarily
   \[
   k\ge2,\qquad z(G)\ge3,\qquad c(G)<z(G).
   \]

Thus the unresolved core is quite specific: a mixture of zombies active immediately in \(G\) and zombies receiving exactly one initial pass at the support \(v\).

---

## 8. Exact finite-state search protocol

For completeness, the conjecture can be checked exhaustively on finite graphs by the following attractor computation.

For a graph \(Q\) and fixed \(k\), use ordered zombie tuples

\[
\mathbf x=(x_1,\dots,x_k).
\]

A state \((\mathbf x,s)\) is taken immediately before a zombie move. Let

\[
M_i(x_i,s)=
\{y\sim x_i:d_Q(y,s)=d_Q(x_i,s)-1\}.
\]

Initialize \(W\) with all capture states, namely those with \(x_i=s\) for some \(i\). Repeatedly add a state \((\mathbf x,s)\) to \(W\) if there is a simultaneous zombie move

\[
\mathbf y\in\prod_{i=1}^k M_i(x_i,s)
\]

such that either some \(y_i=s\), or, for every survivor response \(t\in N_Q[s]\),

\[
t\in\{y_1,\dots,y_k\}
\quad\text{or}\quad
(\mathbf y,t)\in W.
\]

Iterate to the least fixed point. Since this is a finite reachability game, the resulting \(W\) is exactly the set of zombie-winning states.

An initial tuple \(\mathbf x\) is globally winning precisely when

\[
(\mathbf x,s)\in W
\qquad\text{for every }s\in V(Q).
\]

Thus \(z(Q)\) is obtained by testing \(k=1,\dots,|V(Q)|\). To search for a counterexample, enumerate connected graphs \(G\), each support \(v\in V(G)\), form \(G+x\) with \(xv\) pendant, and compare the two computed values.

I have not executed such an enumeration here, so no small-order computational claim is being made.

---

## 9. Remaining gap

The arguments above do not handle the decisive implication:

> If a mixed collection of active zombies and one-round-delayed zombies wins from every survivor start, must some ordinary initial placement of the same number of zombies also win?

The projection method replaces pendant zombies by zombies allowed to pass, but allowing passes is strictly more permissive than the original rule and does not give a reverse simulation. Conversely, moving a delayed zombie immediately toward the current survivor can commit it to a geodesic branch before the survivor moves; there is no evident monotonicity saying that this earlier move is always beneficial.

Accordingly, this does not prove or disprove the full conjecture. It isolates the only remaining mechanism and proves invariance in the cases \(z(G)\le2\), \(z(G)=c(G)\), and more generally \(z_{\mathrm{pass}}(G)=z(G)\).