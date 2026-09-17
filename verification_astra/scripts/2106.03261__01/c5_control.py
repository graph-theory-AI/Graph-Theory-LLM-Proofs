"""Sanity control: does the writeup's trick 'prove too much'?

C5 IS countable (Conlon-Fox-Sudakov-Zhao, [7]).  We build the exact analogue of
the writeup's host for F = C5: 5 classes by x mod 5, edges y+y'+xx' = c_rs with
c_rs = 1 on one C5 edge and 0 elsewhere, and count canonical C5 copies exactly
(by multiplying the five bipartite blocks).  If the trick were universal it would
give 0 copies here too, contradicting a proved theorem.
"""
import sys
import numpy as np

def run(q, twist=True, k=5):
    T = [np.array([x for x in range(q) if x % k == r], dtype=np.int64) for r in range(k)]
    V = [[(int(x), int(y)) for x in T[r] for y in range(q)] for r in range(k)]
    idx = [{v: i for i, v in enumerate(V[r])} for r in range(k)]
    blocks = []
    for r in range(k):
        s = (r + 1) % k
        c = 1 if (twist and r == k - 1) else 0
        B = np.zeros((len(V[r]), len(V[s])), dtype=np.float64)
        for i, (x, y) in enumerate(V[r]):
            for xp in T[s]:
                yp = (c - y - x * int(xp)) % q
                B[i, idx[s][(int(xp), int(yp))]] = 1.0
        blocks.append(B)
    M = blocks[0]
    for r in range(1, k):
        M = M @ blocks[r]
    cnt = float(np.trace(M))
    bench = np.prod([len(V[r]) for r in range(k)]) * (1.0 / q) ** k
    return cnt, bench, [len(V[r]) for r in range(k)]

for q in [int(a) for a in sys.argv[1:]] or [31, 61, 101]:
    for tw in (True, False):
        cnt, bench, sizes = run(q, tw)
        print(f"q={q:4d} twisted={tw!s:5s}  canonical C5 copies = {cnt:12.0f}   "
              f"random benchmark prod|V_r| p^5 = {bench:12.1f}   ratio = {cnt/bench:6.3f}   |V_r|={sizes}")
