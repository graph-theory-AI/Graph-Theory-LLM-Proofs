"""Brute-force verification for referee report on 2108.00991__00.

Counts unlabeled monochromatic copies of P_k (path on k vertices) in explicit
2-colorings of K_{r(P_k)}, r(P_k) = k + floor(k/2) - 1 (Gerencser-Gyarfas).

Checks:
  1. The paper's extremal colorings chi(a0+1,b0) and chi(a0,b0+1) (two blue
     cliques A,B; red complete bipartite between) give exactly k!/2 mono P_k
     for even k, and chi(a0,b0+1) gives (k-1)/4*(k-1)! for odd k.
  2. The writeup's perturbed colorings:
     even k=2l: on K_{3l-1}, A (2l) u B (l-1); blue = cross + one edge xy in A;
       red = rest.  Claim: red = (2l)!/2 - (2l-1)!, blue = l*(2l-2)!.
     odd k=2l+1: on K_{3l}, W (2l) u Z (l-1) u {v}; red = K_W + K_Z + uv;
       blue = rest.  Claim: red = (2l-1)!, blue = l*(2l)!/2 - (2l)!/2.
"""
import itertools, math
from math import factorial


def count_mono_paths(n, k, red):
    """red: set of frozensets {i,j} that are red; all other edges blue.
    Returns (n_red, n_blue) counts of unlabeled monochromatic P_k copies."""
    nr = nb = 0
    for perm in itertools.permutations(range(n), k):
        if perm[0] > perm[-1]:
            continue  # kill reversal symmetry (endpoints distinct)
        colors = set()
        for a, b in zip(perm, perm[1:]):
            colors.add(frozenset((a, b)) in red)
            if len(colors) > 1:
                break
        if len(colors) == 1:
            if colors.pop():
                nr += 1
            else:
                nb += 1
    return nr, nb


def chi(a, b):
    """Paper's coloring chi(a,b): A={0..a-1}, B={a..a+b-1} blue cliques,
    cross edges red. Returns (n, red_set)."""
    n = a + b
    red = set()
    for i in range(a):
        for j in range(a, n):
            red.add(frozenset((i, j)))
    return n, red


def writeup_even(l):
    """K_{3l-1}: A={0..2l-1}, B={2l..3l-2}. Blue: cross + {0,1}. Red: rest."""
    n = 3 * l - 1
    A = range(2 * l)
    red = set()
    for i in range(n):
        for j in range(i + 1, n):
            e = frozenset((i, j))
            in_A = i < 2 * l and j < 2 * l
            in_B = i >= 2 * l and j >= 2 * l
            if (in_A or in_B) and e != frozenset((0, 1)):
                red.add(e)
    return n, red


def writeup_odd(l):
    """K_{3l}: W={0..2l-1}, Z={2l..3l-2}, v=3l-1, u=0.
    Red: K_W, K_Z, uv. Blue: rest."""
    n = 3 * l
    v = n - 1
    red = set()
    for i in range(n):
        for j in range(i + 1, n):
            in_W = i < 2 * l and j < 2 * l
            in_Z = 2 * l <= i < v and 2 * l <= j < v
            if in_W or in_Z:
                red.add(frozenset((i, j)))
    red.add(frozenset((0, v)))
    return n, red


def r_path(k):
    return k + k // 2 - 1


def check_even(k):
    l = k // 2
    assert r_path(k) == 3 * l - 1
    conj = factorial(k) // 2
    print(f"--- even k={k} (l={l}), r(P_k)={r_path(k)}, conjectured m={conj}")
    for (a, b), name in [((k, l - 1), "chi(a0+1,b0)"), ((k - 1, l), "chi(a0,b0+1)")]:
        n, red = chi(a, b)
        nr, nb = count_mono_paths(n, k, red)
        print(f"  {name}=chi({a},{b}): red={nr} blue={nb} total={nr+nb}"
              f"  (paper claims total {conj}) {'OK' if nr+nb==conj else 'MISMATCH'}")
    n, red = writeup_even(l)
    nr, nb = count_mono_paths(n, k, red)
    cr = factorial(2 * l) // 2 - factorial(2 * l - 1)
    cb = l * factorial(2 * l - 2)
    print(f"  writeup coloring: red={nr} (claim {cr}) blue={nb} (claim {cb})"
          f" total={nr+nb} vs conjectured {conj}"
          f" -> {'BEATS conjecture' if nr+nb < conj else 'does NOT beat'}")


def check_odd(k):
    l = (k - 1) // 2
    assert r_path(k) == 3 * l
    conj = (k - 1) * factorial(k - 1) // 4
    print(f"--- odd k={k} (l={l}), r(P_k)={r_path(k)}, conjectured m={conj}")
    n, red = chi(k - 1, l)  # chi(a0, b0+1)
    nr, nb = count_mono_paths(n, k, red)
    print(f"  chi(a0,b0+1)=chi({k-1},{l}): red={nr} blue={nb} total={nr+nb}"
          f"  (paper claims total {conj}) {'OK' if nr+nb==conj else 'MISMATCH'}")
    n, red = writeup_odd(l)
    nr, nb = count_mono_paths(n, k, red)
    cr = factorial(2 * l - 1)
    cb = l * factorial(2 * l) // 2 - factorial(2 * l) // 2
    print(f"  writeup coloring: red={nr} (claim {cr}) blue={nb} (claim {cb})"
          f" total={nr+nb} vs conjectured {conj}"
          f" -> {'BEATS conjecture' if nr+nb < conj else 'does NOT beat'}")


if __name__ == "__main__":
    check_even(4)
    check_odd(5)
    check_even(6)
    check_odd(7)
    check_even(8)
