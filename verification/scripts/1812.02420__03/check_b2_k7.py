#!/usr/bin/env python3
"""Exhaustive check of the writeup's b=2 construction for k=7:
all 2^21-1 nonempty families F of 2-subsets of [7] must satisfy
D[F] acyclic <=> intersection(F) nonempty.  Bitmask implementation."""
import itertools

k = 7
elems = list(range(1, k+1))
pos = {e: i for i, e in enumerate(elems)}
Bs = [frozenset(p) for p in itertools.combinations(elems, 2)]
n = len(Bs)  # 21
idx = {B: i for i, B in enumerate(Bs)}

out = [0]*n           # out-neighbor bitmask
elemmask = [0]*n      # element bitmask
for i, B in enumerate(Bs):
    for e in B:
        elemmask[i] |= 1 << (e-1)
for A, B in itertools.combinations(Bs, 2):
    i, j = idx[A], idx[B]
    if not (A & B):
        out[i] |= 1 << j
        out[j] |= 1 << i
    else:
        (x,) = A & B
        (a,) = A - {x}
        (c,) = B - {x}
        if (pos[a]-pos[x]) % k < (pos[c]-pos[x]) % k:
            out[i] |= 1 << j
        else:
            out[j] |= 1 << i

def cyclic(S):
    T = S
    while T:
        removable = 0
        R = T
        while R:
            v = (R & -R).bit_length() - 1
            R &= R - 1
            if out[v] & T == 0:
                removable |= 1 << v
        if not removable:
            return True
        T &= ~removable
    return False

viol = 0
FULL = (1 << 7) - 1
for S in range(1, 1 << n):
    inter = FULL
    R = S
    while R and inter:
        v = (R & -R).bit_length() - 1
        R &= R - 1
        inter &= elemmask[v]
    if cyclic(S) == (inter != 0):
        viol += 1
        if viol <= 5:
            print("VIOLATION at family mask", S)
print(f"k=7, b=2: checked {2**n - 1} families, violations: {viol}")
assert viol == 0
print("OK")
