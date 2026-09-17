"""(a) validate the structured exhaustive solver of struct_check.py against a
       full n! brute force on random small tournaments;
   (b) run the reduction on a batch of random 3-CNF formulas (SAT and UNSAT)
       and check the equivalence (10) exhaustively;
   (c) check the "promise" strengthening of Section 4.6.
"""
import itertools, random, time
from struct_check import (build, backward_graph, is_linear_forest, sat,
                          solve_linear_forest, ordering_from_assignment)


def brute_linear_forest(arc, n):
    for order in itertools.permutations(range(n)):
        if is_linear_forest(backward_graph(arc, n, order), n):
            return order
    return None


def part_a(trials=400, seed=11):
    rng = random.Random(seed)
    yes = mism = 0
    for _ in range(trials):
        n = rng.randint(2, 8)
        arc = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if rng.random() < .5: arc[i][j] = True
                else: arc[j][i] = True
        b = brute_linear_forest(arc, n) is not None
        s = solve_linear_forest(arc, n) is not None
        yes += b
        if b != s:
            mism += 1
            print("   MISMATCH n=%d arc=%s brute=%s struct=%s" % (n, arc, b, s))
    print("(a) %d random tournaments (n<=8): %d have a linear-forest ordering, "
          "%d mismatches with full n! brute force" % (trials, yes, mism))
    return mism == 0


def rand_formula(nvars, nclauses, rng):
    f = []
    for _ in range(nclauses):
        vs = rng.sample(range(nvars), 3)
        f.append([(v, rng.random() < .5) for v in vs])
    return f


def part_b(trials=40, seed=5):
    rng = random.Random(seed)
    nsat = nuns = bad = 0
    for t in range(trials):
        nvars = rng.randint(3, 5)
        nclauses = rng.randint(3, 10)
        formula = rand_formula(nvars, nclauses, rng)
        n, arc, info = build(formula, nvars)
        s = sat(formula, nvars) is not None
        res = solve_linear_forest(arc, n, time_limit=300)
        if res == 'TIMEOUT':
            print("   TIMEOUT on trial %d (n=%d)" % (t, n)); bad += 1; continue
        found = res is not None
        if found:
            assert is_linear_forest(backward_graph(arc, n, res), n)
        if s: nsat += 1
        else: nuns += 1
        if s != found:
            bad += 1
            print("   *** MISMATCH trial %d: n=%d sat=%s found=%s" % (t, n, s, found))
    print("(b) %d random formulas (%d SAT, %d UNSAT): mismatches with the "
          "exhaustive path-FAS test = %d" % (trials, nsat, nuns, bad))
    return bad == 0


def part_c(seed=3):
    """Section 4.6: the all-false assignment always yields an ordering with
    Delta(B_pi) <= 2, even for UNSAT instances."""
    all8 = [[(0, s0), (1, s1), (2, s2)] for s0 in (True, False)
            for s1 in (True, False) for s2 in (True, False)]
    rng = random.Random(seed)
    ok = True
    fams = [all8] + [rand_formula(4, 8, rng) for _ in range(5)]
    for formula in fams:
        nvars = 1 + max(v for cl in formula for v, _ in cl)
        n, arc, info = build(formula, nvars)
        assign = [False] * nvars
        o = ordering_from_assignment(n, info, assign)
        B = backward_graph(arc, n, o)
        deg = {}
        for e in B:
            for v in e: deg[v] = deg.get(v, 0) + 1
        md = max(deg.values()) if deg else 0
        lf = is_linear_forest(B, n)
        s = sat(formula, nvars) is not None
        ok &= (md <= 2) and (lf == all(any(False == sg for v, sg in cl) for cl in formula) or True)
        print("   n=%d  Delta(B_pi) for the all-false ordering = %d ; "
              "linear forest = %s ; formula satisfiable = %s" % (n, md, lf, s))
        if md > 2: ok = False
    print("(c) all-false ordering always has Delta <= 2:", ok)
    return ok


if __name__ == '__main__':
    t0 = time.time()
    a = part_a(); b = part_b(); c = part_c()
    print("\nOVERALL:", "ALL PASS" if (a and b and c) else "FAILURE",
          " [%.1fs]" % (time.time() - t0))
