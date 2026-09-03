#!/usr/bin/env python3
"""Definition sanity check: brute-force exact M_k(n) for tiny k, n.

M_k(n) = least m such that there are integer shifts s_d with
s_d + B_d subset of {1,...,m} (B_d = {d,2d,...,nd}, d = 1..k) and the shifted
copies pairwise disjoint.  (Paper, Sec. 1 and Sec. 4.)

Checks the CRT-style reasoning: for k = 2, hulls of B_1 (full block of n
consecutive integers) and B_2 cannot interleave, so M_2(n) = n + (2n-1) = 3n-1.
"""
from itertools import product

def brute_Mk(k, n, m_max=200):
    prog = {d: [i * d for i in range(1, n + 1)] for d in range(1, k + 1)}
    hull = {d: (n - 1) * d for d in range(1, k + 1)}
    for m in range(max(hull.values()) + 1, m_max + 1):
        # shifts: s_d + d >= 1 and s_d + nd <= m  =>  s_d in [1-d, m-nd]
        ranges = [range(1 - d, m - n * d + 1) for d in range(1, k + 1)]
        for shifts in product(*ranges):
            sets = []
            ok = True
            for d, s in zip(range(1, k + 1), shifts):
                S = set(x + s for x in prog[d])
                for T in sets:
                    if S & T:
                        ok = False
                        break
                if not ok:
                    break
                sets.append(S)
            if ok:
                return m
    return None

def main():
    print("k=2:")
    for n in range(2, 8):
        m = brute_Mk(2, n)
        print(f"  M_2({n}) = {m}   (3n-1 = {3*n-1})  {'OK' if m == 3*n-1 else 'MISMATCH'}")
    print("k=3:")
    for n in range(2, 6):
        m = brute_Mk(3, n)
        print(f"  M_3({n}) = {m}")

if __name__ == "__main__":
    main()
