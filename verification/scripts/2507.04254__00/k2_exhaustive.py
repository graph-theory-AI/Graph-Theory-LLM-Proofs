"""Exhaustive check of chi'_2(G_2) for the writeup's construction at k=2.

G_2 has 7 vertices and 8 edges. A modular 2-edge-colouring: in each colour
class every nonzero degree is odd (== 1 mod 2).

Writeup's lemma predicts chi'_2(G_2) >= ceil(7*2/6) = 3.
We verify by brute force over ALL colourings:
  m=1: 1 colouring, m=2: 2^8 = 256, m=3: 3^8 = 6561.
Also verify, inside every valid 3-colouring, the lemma's internal claims:
  t(v) = k = 2 for every vertex; x_c == y_c (mod 2); u_c - v_c == |X|-|Y| (mod 2);
  sum_c (u_c+v_c) = n(m-k).
"""
import itertools

k = 2
X = [("x", i) for i in range(4)]
H = [("h", 0)]
L = [("l", 0), ("l", 1)]
S = {0}
edges = []
for h in H:
    for x in X:
        edges.append((h, x))
for x in X:
    for l in L:
        if (l[1] - (x[1] % k)) % k in S:
            edges.append((x, l))
V = X + H + L
assert len(edges) == 8

def valid(col, m):
    for v in V:
        for c in range(m):
            d = sum(1 for e, ce in zip(edges, col) if ce == c and v in e)
            if d != 0 and d % k != 1 % k:
                return False
    return True

def count_valid(m):
    good = []
    for col in itertools.product(range(m), repeat=len(edges)):
        if valid(col, m):
            good.append(col)
    return good

print("m=1 valid colourings:", len(count_valid(1)))
print("m=2 valid colourings:", len(count_valid(2)))
good3 = count_valid(3)
print("m=3 valid colourings:", len(good3))
assert len(count_valid(1)) == 0 and len(count_valid(2)) == 0
assert len(good3) > 0
print("=> chi'_2(G_2) = 3 = ceil(7k/6); lemma bound confirmed exhaustively")

# lemma internals on every valid 3-colouring
m = 3
nX, nY = len(X), len(H) + len(L)
n = nX + nY
for col in good3:
    for v in V:
        t = len({c for e, c in zip(edges, col) if v in e})
        assert t == k, (v, t)
    tot = 0
    for c in range(m):
        xc = len({e[0] if e[0][0] == "x" else e[1] for e, ce in zip(edges, col) if ce == c})
        yc = len({e[0] if e[0][0] != "x" else e[1] for e, ce in zip(edges, col) if ce == c})
        assert (xc - yc) % k == 0, (c, xc, yc)
        uc, vc = nX - xc, nY - yc
        assert (uc - vc - (nX - nY)) % k == 0
        tot += uc + vc
    assert tot == n * (m - k), (tot, n * (m - k))
print("lemma internal identities hold in all", len(good3), "valid 3-colourings")
