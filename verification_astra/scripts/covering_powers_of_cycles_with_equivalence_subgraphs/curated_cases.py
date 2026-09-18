#!/usr/bin/env python3
"""Exact eq(C_n^k) on a curated list of cases, with per-case reporting.

Also cross-checks against:
  * the writeup's exact formula r+1 = ceil(log2(k+1)) + 1 when (k+1) | n,
  * the writeup's bounds r+1 <= eq <= 2r+1 for n >= 2k+2,
  * Douglas West's REGS page claim "eq(C_n^k) = k+1 when k+1 divides n".
"""
import sys
from brute_force_eq import eq_value

CASES = [
    (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1),
    (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2),
    (8, 3), (9, 3), (10, 3), (11, 3), (12, 3),
    (10, 4), (11, 4), (12, 4), (13, 4),
    (12, 5), (13, 5),
    (14, 6),
]

print(f"{'n':>3} {'k':>3} {'eq':>3} {'r+1':>4} {'2r+1':>5} {'k+1':>4} {'(k+1)|n':>8}  verdict")
bad = []
for (n, k) in CASES:
    s, = (k + 1,)
    r = max(1, (s - 1).bit_length())
    try:
        t, ne, npart, nsets = eq_value(n, k)
    except MemoryError:
        print(f"{n:3d} {k:3d}  -- memory")
        continue
    div = (n % s == 0)
    notes = []
    if t < r + 1:
        notes.append("BELOW writeup lower bound")
    if t > 2 * r + 1:
        notes.append("ABOVE writeup upper bound")
    if div and t != r + 1:
        notes.append("writeup exact formula FAILS")
    if div and t != k + 1:
        notes.append("West REGS claim eq=k+1 FAILS")
    if notes:
        bad.append((n, k, t, notes))
    print(f"{n:3d} {k:3d} {t:3d} {r+1:4d} {2*r+1:5d} {k+1:4d} {int(div):8d}  "
          f"{'; '.join(notes) if notes else 'consistent with writeup'}", flush=True)

print()
print("cases inconsistent with the writeup:",
      [b for b in bad if any('writeup' in x for x in b[3])] or "NONE")
print("divisible cases refuting West's eq=k+1:",
      [(b[0], b[1], b[2]) for b in bad if any('West' in x for x in b[3])] or "NONE")
