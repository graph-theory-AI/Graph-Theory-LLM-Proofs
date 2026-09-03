#!/usr/bin/env python3
"""Verify f_{6,5}(9) = 8 (paper convention: length of a path = number of vertices).

f_{6,5}(9) = min over 6-edge-colorings chi of the transitive tournament on
v1 < ... < v9 of the number of vertices in the longest directed path whose
edges use at most 5 colors (i.e. avoid at least one color).

Directed paths in the transitive tournament = increasing vertex subsequences.

UPPER BOUND (f <= 8): exhibit a coloring with no color-avoiding 9-vertex path.
The only 9-vertex path is v1...v9; if its consecutive-edge word contains all
6 colors, that path is not color-avoiding, so p(chi) <= 8. The writeup's word
1,2,3,4,5,6,1,2 works. (Machine-checked trivially below.)

LOWER BOUND (f >= 8): show that EVERY coloring admits an 8-vertex
color-avoiding path. An 8-vertex path omits exactly one v_k and uses:
  - consecutive edges a_i = chi(v_i v_{i+1}) except the ones incident to v_k,
  - plus, if 2<=k<=8, the single chord v_{k-1} v_{k+1}.
Whether such a path avoids a color depends only on the word a_1..a_8 and the
chord colors. We machine-verify the following CHORD-INDEPENDENT sufficient
condition for every word a in [6]^8 (6^8 = 1679616 words):

  (A) set(a_2..a_8) != [6]                (delete v_1: no chord used), or
  (B) set(a_1..a_7) != [6]                (delete v_9: no chord used), or
  (C) some k in 2..8: the multiset a minus positions k-1,k misses >= 2 colors
      (then whatever single color the chord has, >= 1 color is still missing).

If every word satisfies A, B or C, then every coloring of the transitive
9-tournament (regardless of chord/other colors) has an 8-vertex
color-avoiding path, i.e. f_{6,5}(9) >= 8. This covers ALL colorings because
paths on >= 8 vertices use no edges other than the a_i and the 2-chords.
"""
import itertools
from collections import Counter

COLORS = set(range(1, 7))

# ---------- upper bound ----------
word = [1, 2, 3, 4, 5, 6, 1, 2]
assert set(word) == COLORS
print("upper bound: word 1,2,3,4,5,6,1,2 gives all 6 colors on the unique")
print("9-vertex path, so that coloring has p(chi) <= 8  =>  f_{6,5}(9) <= 8")

# ---------- lower bound ----------
bad_words = 0
checked = 0
for a in itertools.product(range(1, 7), repeat=8):
    checked += 1
    # (A) delete v1 -> edges a_2..a_8
    if set(a[1:]) != COLORS:
        continue
    # (B) delete v9 -> edges a_1..a_7
    if set(a[:7]) != COLORS:
        continue
    # (C) delete v_k, k=2..8 -> remove a_{k-1}, a_k (0-based: a[k-2], a[k-1])
    cnt = Counter(a)
    ok = False
    for k in range(2, 9):
        c = cnt.copy()
        c[a[k - 2]] -= 1
        c[a[k - 1]] -= 1
        missing = sum(1 for col in COLORS if c[col] <= 0)
        if missing >= 2:
            ok = True
            break
    if not ok:
        bad_words += 1
        if bad_words <= 10:
            print("word with no chord-independent color-avoiding 8-path:", a)

print(f"checked {checked} words; words failing A/B/C: {bad_words}")
if bad_words == 0:
    print("LOWER BOUND VERIFIED: every 6-coloring of the transitive 9-vertex")
    print("tournament has a color-avoiding 8-vertex path  =>  f_{6,5}(9) >= 8")
    print("CONCLUSION: f_{6,5}(9) = 8")
else:
    print("chord-independent criterion insufficient; deeper analysis needed")
