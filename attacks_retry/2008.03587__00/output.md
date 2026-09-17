```json
{
  "verdict": "disproved",
  "confidence": "high",
  "one_line": "A 59-vertex cactus requires at least three zombies, but adding one leaf produces a graph requiring exactly two.",
  "would_publish": true,
  "caveats": "Uses the standard compulsory-move rules, with zombies moving before the survivor; no computational or literature-status claim is made."
}
```

# A counterexample

Zombies choose their initial positions first, followed by the survivor. On each turn, every zombie must move along an edge decreasing its distance to the survivor; the survivor then moves to a neighbor or stays. Capture occurs upon coincidence.

The counterexample is a cactus consisting of three cycles attached to a path. The proof below is entirely analytic.

## 1. Construction

Start with the path
\[
v_0v_1\cdots v_{10}.
\]
Attach, using otherwise disjoint vertices,

- a cycle \(A\) of length \(25\) at \(v_0\);
- a cycle \(B\) of length \(17\) at \(v_2\);
- a cycle \(C\) of length \(9\) at \(v_4\).

There are no other edges. Call the resulting graph \(G\). Thus
\[
|V(G)|=11+24+16+8=59.
\]

Let \(H\) be obtained by adding a single new vertex \(v_{11}\), adjacent only to \(v_{10}\). I will prove
\[
z(G)\ge 3
\qquad\text{and}\qquad
z(H)=2.
\]

Here and below, each cycle includes its attachment vertex.

---

## 2. A certificate for perpetual rotation around an odd cycle

Let \(Q\) contain a cycle of length
\[
n=2h+1,\qquad h\ge2,
\]
attached to the rest of \(Q\) only at its vertex \(0\). Choose an orientation and label its vertices by \(\mathbb Z_n\) in that orientation.

For a zombie’s initial position \(x\), define its **phase**
\[
p(x)=
\begin{cases}
x, & x\text{ lies on the cycle, using its cyclic coordinate};\\[2mm]
-d_Q(x,0)\pmod n, & x\text{ lies outside the cycle}.
\end{cases}
\]

### Rotation lemma

If there is a coordinate \(q\) such that
\[
q-p(x_i)\pmod n\in\{2,3,\ldots,h\}
\tag{1}
\]
for every zombie \(i\), then the survivor can evade forever by starting at \(q\) and moving one step in the chosen orientation every turn.

In particular, two zombies can be evaded this way whenever
\[
\|p(x_1)-p(x_2)\|_n\le h-2,
\tag{2}
\]
where \(\|a\|_n\) denotes cyclic distance to \(0\) modulo \(n\).

### Proof

First consider a zombie initially on the cycle. Condition (1) puts it a forward distance between \(2\) and \(h\) behind the survivor. Its unique shortest route is in the survivor’s direction. After the zombie and survivor each move, this forward distance is unchanged.

Now consider a zombie outside the cycle, initially at distance \(D\) from the attachment vertex. While the survivor stays on the cycle, every shortest route from that zombie to the survivor passes through \(0\). Consequently, the zombie decreases its distance to \(0\) on every move and reaches \(0\) on its \(D\)-th move.

Immediately before that landing move, the survivor is at
\[
q+D-1 \pmod n.
\]
Writing \(e=q+D\pmod n\), condition (1) gives \(2\le e\le h\). Thus the survivor is not at \(0\) when the zombie lands. After the survivor’s response, the forward gap is \(e\), again between \(2\) and \(h\), and remains constant thereafter.

For the final assertion, two residues can satisfy (1) simultaneously exactly when their difference has a representative in
\[
[-(h-2),h-2],
\]
because this is the set of differences of two integers in \(\{2,\ldots,h\}\). ∎

For reference, the sufficient bounds in (2) are
\[
\begin{array}{c|c|c}
\text{Cycle length}&h&h-2\\ \hline
25&12&10\\
17&8&6\\
9&4&2
\end{array}
\]

---

## 3. Two zombies do not suffice on \(G\)

Consider any two initial zombie positions \(x,y\).

Every vertex outside \(A\) has distance at most \(10\) from \(v_0\). Indeed:

- the path ends at \(v_{10}\);
- a vertex of \(B\) is at distance at most \(2+8=10\) from \(v_0\);
- a vertex of \(C\) is at distance at most \(4+4=8\) from \(v_0\).

We distinguish all three possibilities for membership in \(A\).

### Case 1: Both zombies start outside \(A\)

Put
\[
D_x=d_G(x,v_0),\qquad D_y=d_G(y,v_0).
\]
Both numbers lie in \(\{1,\ldots,10\}\), so
\[
|D_x-D_y|\le9.
\]

Their phases on \(A\) are \(-D_x,-D_y\) modulo \(25\). Their cyclic separation is therefore at most \(9\), which is below the rotation lemma’s bound \(10\). The survivor can rotate around \(A\) forever.

### Case 2: Both zombies start in \(A\)

Let
\[
a=d_G(x,v_0),\qquad b=d_G(y,v_0),\qquad
\delta=|a-b|.
\]
Since \(A\) has length \(25\),
\[
0\le\delta\le12.
\]

The zombies’ distances to \(v_2\) are \(a+2,b+2\), and their distances to \(v_4\) are \(a+4,b+4\). Thus their phase separation is represented by \(\delta\) on both \(B\) and \(C\).

If
\[
\delta\in\{0,1,\ldots,6,11,12\},
\]
then
\[
\|\delta\|_{17}\le6,
\]
so the survivor can rotate around \(B\).

Otherwise \(\delta\in\{7,8,9,10\}\), and then
\[
\|\delta\|_9\le2.
\]
The survivor can instead rotate around \(C\).

### Case 3: Exactly one zombie starts in \(A\)

Suppose \(x\in A\) and \(y\notin A\). Put
\[
t=d_G(x,v_0)\in\{0,\ldots,12\},
\qquad
D=d_G(y,v_0)\in\{1,\ldots,10\}.
\]

Orient \(A\) so that \(x\) has coordinate \(-t\pmod{25}\). The two phases on \(A\) are then \(-t,-D\), whose difference is represented by
\[
D-t\in[-11,10].
\]

Except when
\[
(D,t)=(1,12),
\]
we have \(|D-t|\le10\), and the rotation lemma gives perpetual evasion on \(A\).

In the exceptional case, \(y=v_1\), since this is the only vertex outside \(A\) at distance \(1\) from \(v_0\). The distances of the zombies to the attachment vertex \(v_2\) of \(B\) are
\[
d_G(x,v_2)=12+2=14,
\qquad
d_G(y,v_2)=1.
\]
Their phase difference on \(B\) is \(13\) modulo \(17\), with cyclic distance
\[
\|13\|_{17}=4\le6.
\]
The survivor can rotate around \(B\).

These cases cover every pair of initial positions. Therefore
\[
\boxed{z(G)\ge3.}
\]

---

## 4. A delayed pair that captures on a pendant cycle

The following observation supplies the winning strategy on \(H\).

### Capture lemma

Suppose a cycle of length \(2d+3\), with \(d\ge1\), is attached to the rest of a graph only at its root \(r\). Suppose, immediately before a zombie turn,

- one zombie is at \(r\);
- another zombie is outside the cycle at distance \(d\) from \(r\);
- the survivor is on the cycle.

Then these two zombies can force capture.

### Proof

Label the root \(0\). Choose the orientation in which the survivor’s initial coordinate \(p\) satisfies
\[
1\le p\le d+1.
\]
If \(p=1\), the root zombie captures immediately. Assume otherwise.

The root zombie follows the survivor in this orientation. Consider a play avoiding capture, including capture on the following zombie turn. After \(t\) complete rounds, write the first zombie’s coordinate as \(t\) and the survivor’s unwrapped coordinate as \(u_t\).

The forward gap
\[
g_t=u_t-t
\]
cannot increase: on a survivor move it changes by \(0,-1\), or \(-2\), accounting for the preceding zombie move. A gap at most \(1\) results in immediate or next-turn capture. Hence, while evasion continues,
\[
2\le g_t\le p\le d+1.
\tag{3}
\]
These bounds also ensure that the first zombie’s move in the chosen direction is always its unique shortest-path move.

For \(0\le t\le d\), (3) gives
\[
0<u_t\le t+d+1\le2d+1<2d+3.
\]
Thus the survivor cannot reach the attachment vertex during these rounds and cannot leave the cycle.

The outside zombie consequently reaches the root after exactly \(d\) moves. After the survivor’s response on that round,
\[
d+2\le u_d\le2d+1.
\]
The zombies are now at coordinates \(d\) and \(0\). They bracket the survivor on the arc from \(d\) forward to \(0\), and the two distances along that arc are
\[
u_d-d\le d+1,
\qquad
2d+3-u_d\le d+1.
\]
Both are shortest-path distances.

The zombies now move inward along this arc. Each of these two distances is nonincreasing after a complete round, so the inward moves remain legal. The occupied endpoints prevent escape through the root, and the intervening arc loses two edges on every zombie turn. Capture follows. ∎

---

## 5. Two zombies win on \(H\)

Place the zombies at
\[
v_0\quad\text{and}\quad v_{11}.
\]

Project every vertex of an attached cycle to its attachment vertex on the path
\[
P=v_0v_1\cdots v_{11}.
\]

Until a zombie reaches the attachment vertex of the cycle currently containing the survivor, both zombies move along \(P\) toward the survivor’s projection. These are legal shortest-path moves.

The survivor cannot cross an occupied path vertex. Consequently, unless capture or such a cycle-root contact occurs, the two zombies’ positions after \(t\) moves are
\[
v_t,\qquad v_{11-t},
\]
and the survivor’s projection remains strictly between them. This shrinking interval cannot support evasion indefinitely.

It remains to handle the first cycle-root contact. All attachment indices are \(0,2,4\), so this first contact is made by the zombie coming from \(v_0\). If the relevant root is \(v_r\), the contact occurs after \(r\) zombie moves, with positions
\[
v_r,\qquad v_{11-r}.
\]
The distance of the second zombie from the root is
\[
d=11-2r.
\]

The three possibilities are
\[
\begin{array}{c|c|c}
r&d&\text{Length of the attached cycle}\\ \hline
0&11&25=2\cdot11+3\\
2&7&17=2\cdot7+3\\
4&3&9=2\cdot3+3
\end{array}
\]

If the survivor is actually at the root, it is captured. Otherwise it lies inside that cycle and cannot leave through the occupied root on its ensuing response. The capture lemma therefore applies in every case.

Thus
\[
z(H)\le2.
\]

Conversely, one zombie can always be evaded on \(A\): in the rotation lemma, a single phase can always be accommodated by choosing \(q=p+2\pmod{25}\). This applies whether the zombie starts inside or outside \(A\). Hence
\[
\boxed{z(H)=2.}
\]

---

## 6. Conclusion

The explicitly constructed graphs satisfy
\[
\boxed{z(H)=2<3\le z(G),}
\]
although \(H\) is obtained from \(G\) by adding just the leaf \(v_{11}\) adjacent to \(v_{10}\).

Thus **zombie number is not invariant under leaf attachment**, even for cactus graphs.

The mechanism is precisely an initial-delay advantage: the new leaf delays the rear zombie by one move, making its arrival gap at each of the three cycle roots large enough to approach the survivor from the opposite direction. The lower-bound argument shows that no alternative pair of starting vertices in \(G\) can achieve a global win.

Every pair of starting positions in \(G\) and every survivor start in \(H\) is covered above. Determining the exact value of \(z(G)\) beyond \(z(G)\ge3\) is unnecessary for the counterexample.