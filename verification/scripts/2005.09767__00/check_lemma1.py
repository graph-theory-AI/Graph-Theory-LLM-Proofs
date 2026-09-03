"""Independent check of Lemma 1 (footprint bound) of the writeup for 2005.09767__00.

Lemma 1: if P in F_q[X_1..X_r] induces a nonzero function on F_q^r and deg P <= d,
then #{x : P(x) != 0} >= q^{max(r - d/(q-1), 0)}.

We test it on polynomials already reduced (individual degrees <= q-1), taking d =
the exact total degree of the reduced polynomial (the strongest form used by the
writeup after reduction mod X_i^q - X_i).

- Exhaustive over all reduced polynomials for (q=2, r=2), (q=3, r=2), (q=2, r=3).
- Randomized (100000 trials) for (q=3, r=3), (q=5, r=2), (q=7, r=2), (q=7, r=1).
"""
import itertools
import random

def support_and_degree(q, r, coeffs):
    """coeffs: dict exponent-tuple -> coeff (mod q). Returns (support size, total degree)."""
    deg = max((sum(e) for e, c in coeffs.items() if c % q), default=-1)
    if deg == -1:
        return 0, -1  # zero polynomial
    supp = 0
    for x in itertools.product(range(q), repeat=r):
        val = 0
        for e, c in coeffs.items():
            t = c
            for xi, ei in zip(x, e):
                t = t * pow(xi, ei, q) if ei else t
            val = (val + t) % q
        if val % q:
            supp += 1
    return supp, deg

def bound(q, r, d):
    expo = max(r - d / (q - 1), 0.0)
    return q ** expo

def run_exhaustive(q, r):
    exps = list(itertools.product(range(q), repeat=r))  # individual degrees <= q-1
    n_fail = n_checked = 0
    worst = None
    for coeff_vec in itertools.product(range(q), repeat=len(exps)):
        coeffs = {e: c for e, c in zip(exps, coeff_vec) if c}
        if not coeffs:
            continue
        supp, deg = support_and_degree(q, r, coeffs)
        # reduced nonzero polynomial with individual degrees <= q-1 induces a
        # nonzero function, so supp >= 1 automatically; check the bound
        n_checked += 1
        b = bound(q, r, deg)
        if supp + 1e-9 < b:
            n_fail += 1
            worst = (coeffs, supp, deg, b)
    print(f"exhaustive q={q} r={r}: checked {n_checked} nonzero reduced polys, "
          f"failures={n_fail}" + (f" worst={worst}" if worst else ""))
    return n_fail

def run_random(q, r, trials, seed):
    rng = random.Random(seed)
    exps = list(itertools.product(range(q), repeat=r))
    n_fail = 0
    min_ratio = float("inf")
    for _ in range(trials):
        # random sparse-ish reduced polynomial
        k = rng.randint(1, min(6, len(exps)))
        coeffs = {}
        for e in rng.sample(exps, k):
            coeffs[e] = rng.randint(1, q - 1)
        supp, deg = support_and_degree(q, r, coeffs)
        if deg == -1:
            continue
        b = bound(q, r, deg)
        min_ratio = min(min_ratio, supp / b)
        if supp + 1e-9 < b:
            n_fail += 1
            print("FAIL", q, r, coeffs, supp, deg, b)
    print(f"random q={q} r={r} trials={trials}: failures={n_fail}, "
          f"min support/bound ratio={min_ratio:.4f}")
    return n_fail

if __name__ == "__main__":
    total = 0
    total += run_exhaustive(2, 2)
    total += run_exhaustive(2, 3)
    total += run_exhaustive(3, 2)
    total += run_random(3, 3, 100000, 1)
    total += run_random(5, 2, 100000, 2)
    total += run_random(7, 1, 100000, 3)
    total += run_random(7, 2, 50000, 4)
    # also products of random linear factors (the shape used in the writeup)
    rng = random.Random(5)
    fails = 0
    for trial in range(2000):
        q = rng.choice([3, 5, 7])
        r = rng.randint(1, 2)
        mfac = rng.randint(1, 3 * (q - 1))
        # multiply out product of linear factors symbolically mod (X_i^q - X_i)
        # represent poly as dict over exponent tuples with entries < q each
        poly = {tuple([0] * r): 1}
        for _ in range(mfac):
            lin = {tuple([0] * r): rng.randrange(q)}
            for i in range(r):
                e = [0] * r; e[i] = 1
                lin[tuple(e)] = rng.randrange(q)
            new = {}
            for e1, c1 in poly.items():
                for e2, c2 in lin.items():
                    e = tuple(a + b for a, b in zip(e1, e2))
                    new[e] = (new.get(e, 0) + c1 * c2) % q
            poly = {e: c for e, c in new.items() if c}
        # reduce exponents mod x^q = x (for x != 0 ... proper reduction: X^q -> X)
        red = {}
        for e, c in poly.items():
            ee = []
            for a in e:
                while a >= q:
                    a = a - (q - 1)   # X^q = X  => exponent a -> a-(q-1) for a>=q
                ee.append(a)
            ee = tuple(ee)
            red[ee] = (red.get(ee, 0) + c) % q
        red = {e: c for e, c in red.items() if c}
        if not red:
            continue
        supp, deg = support_and_degree(q, r, red)
        if supp == 0:
            continue  # zero function (can't happen for reduced nonzero poly)
        b = bound(q, r, deg)
        if supp + 1e-9 < b:
            fails += 1
            print("FAIL-linprod", q, r, red, supp, deg, b)
    print(f"random products of linear factors: failures={fails}")
    total += fails
    print("TOTAL FAILURES:", total)
