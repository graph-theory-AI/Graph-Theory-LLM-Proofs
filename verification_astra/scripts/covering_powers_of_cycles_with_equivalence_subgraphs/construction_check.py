#!/usr/bin/env python3
"""Verify the writeup's explicit equivalence covers of C_n^k.

Section 2: for n = m*s with s = k+1, m >= 2, a cover with r+1 = ceil(log2 s)+1 layers.
Section 3: for arbitrary n >= 2s, a cover with 2r+1 layers.

We check, independently of the writeup's prose:
  (a) every part of every layer is a clique of C_n^k,
  (b) the parts of a layer are pairwise disjoint (so the layer is an equivalence subgraph),
  (c) the union of the layers covers every edge of C_n^k.
"""
import itertools
import sys


def cyc_dist(a, b, n):
    d = (a - b) % n
    return min(d, n - d)


def edges_cycle_power(n, k):
    E = set()
    for u in range(n):
        for v in range(u + 1, n):
            if 1 <= cyc_dist(u, v, n) <= k:
                E.add((u, v))
    return E


def bits(x, r):
    return tuple((x >> (r - 1 - i)) & 1 for i in range(r))


def I(h, p, eps, s, r):
    """{x in [0,s) : first h-1 bits = p, bit h = eps}, h in 1..r."""
    out = []
    for x in range(s):
        b = bits(x, r)
        if b[: h - 1] == tuple(p) and b[h - 1] == eps:
            out.append(x)
    return out


def cover_divisible(n, k):
    """Section 2 construction. Requires (k+1) | n and n/(k+1) >= 2."""
    s = k + 1
    r = max(1, (s - 1).bit_length())  # ceil(log2 s) for s>=2
    assert n % s == 0
    m = n // s
    v = lambda i, x: (i % m) * s + x

    layers = []
    layers.append([[v(i, x) for x in range(s)] for i in range(m)])  # H_0
    for h in range(1, r + 1):
        parts = []
        for i in range(m):
            for p in itertools.product((0, 1), repeat=h - 1):
                Q = [v(i, x) for x in I(h, p, 1, s, r)] + [
                    v(i + 1, y) for y in I(h, p, 0, s, r)
                ]
                if len(Q) >= 2:
                    parts.append(Q)
        layers.append(parts)
    return layers, r


def cover_general(n, k):
    """Section 3 construction: path-power cover (r+1 layers) + wrap cover (r layers)."""
    s = k + 1
    r = max(1, (s - 1).bit_length())
    assert n >= 2 * s
    nb = (n + s - 1) // s  # number of blocks, last possibly short
    block = [list(range(i * s, min((i + 1) * s, n))) for i in range(nb)]

    layers = [[b[:] for b in block if len(b) >= 2]]  # H_0
    for h in range(1, r + 1):
        parts = []
        for i in range(nb - 1):  # consecutive pairs only, no wrap
            for p in itertools.product((0, 1), repeat=h - 1):
                Q = [block[i][x] for x in I(h, p, 1, s, r) if x < len(block[i])] + [
                    block[i + 1][y] for y in I(h, p, 0, s, r) if y < len(block[i + 1])
                ]
                if len(Q) >= 2:
                    parts.append(Q)
        if parts:
            layers.append(parts)
    # wrap layers
    A = [n - s + x for x in range(s)]
    B = [y for y in range(s)]
    for h in range(1, r + 1):
        parts = []
        for p in itertools.product((0, 1), repeat=h - 1):
            Q = [A[x] for x in I(h, p, 1, s, r)] + [B[y] for y in I(h, p, 0, s, r)]
            if len(Q) >= 2:
                parts.append(Q)
        if parts:
            layers.append(parts)
    return layers, r


def check(n, k, layers, label):
    E = edges_cycle_power(n, k)
    covered = set()
    for li, parts in enumerate(layers):
        seen = set()
        for Q in parts:
            if len(set(Q)) != len(Q):
                return f"FAIL {label} n={n} k={k}: repeated vertex in part {Q}"
            for a in Q:
                if a in seen:
                    return f"FAIL {label} n={n} k={k}: layer {li} parts not disjoint at {a}"
                seen.add(a)
            for a, b in itertools.combinations(sorted(Q), 2):
                if (a, b) not in E:
                    return (f"FAIL {label} n={n} k={k}: layer {li} part {Q} not a clique "
                            f"({a},{b}) dist {cyc_dist(a,b,n)}")
                covered.add((a, b))
    if covered != E:
        return f"FAIL {label} n={n} k={k}: {len(E - covered)} edges uncovered, e.g. {sorted(E-covered)[:5]}"
    return None


def main():
    bad = 0
    print("== Section 2 (s | n) ==")
    print(f"{'n':>5} {'k':>4} {'s':>4} {'r':>3} {'layers':>7} {'r+1':>5}  status")
    for k in range(1, 33):
        s = k + 1
        for m in range(2, 6):
            n = m * s
            if n > 200:
                continue
            layers, r = cover_divisible(n, k)
            msg = check(n, k, layers, "S2")
            ok = "OK" if msg is None else msg
            if msg:
                bad += 1
            if k in (1, 2, 3, 4, 7, 8, 15, 16, 31) and m in (2, 3):
                print(f"{n:5d} {k:4d} {s:4d} {r:3d} {len(layers):7d} {r+1:5d}  {ok}")
            elif msg:
                print(f"{n:5d} {k:4d} {s:4d} {r:3d} {len(layers):7d} {r+1:5d}  {ok}")
            assert len(layers) == r + 1, (n, k, len(layers), r)

    print()
    print("== Section 3 (arbitrary n >= 2k+2) ==")
    worst = {}
    for k in range(1, 17):
        s = k + 1
        r = max(1, (s - 1).bit_length())
        for n in range(2 * s, min(2 * s + 40, 130)):
            layers, r = cover_general(n, k)
            msg = check(n, k, layers, "S3")
            if msg:
                bad += 1
                print(msg)
            worst[k] = max(worst.get(k, 0), len(layers))
        print(f"k={k:3d} s={s:3d} r={r:2d} max layers used = {worst[k]:2d}  (bound 2r+1 = {2*r+1})")
        assert worst[k] <= 2 * r + 1

    print()
    print("FAILURES:", bad)
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
