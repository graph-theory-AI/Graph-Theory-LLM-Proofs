#!/usr/bin/env python3
"""SAT check (via kissat) that T_n admits no ordering with triangle-free
backedge graph (i.e. omega->(T_n) >= 3), and that T_n - 0 does admit one.

Encoding: boolean p[u][v] for u < v (vertex labels): "u precedes v".
Transitivity clauses over all ordered triples. For each unordered pair {u,v}
the backedge-graph edge is present iff the head of the arc precedes the tail:
if arc v->u in T then edge iff (u precedes v). For each vertex triple, one
clause forbidding all three edges simultaneously. UNSAT <=> every ordering's
backedge graph has a triangle <=> omega-> >= 3.
"""
import itertools, subprocess, sys, tempfile, os

def make_T(n):
    q = 2 * n + 1
    S = set(range(1, n)) | {n + 1}
    return q, S

def prec_lit(var, u, v):
    """literal for 'u precedes v'"""
    return var[(u, v)] if (u, v) in var else -var[(v, u)]

def edge_lit(var, q, S, u, v):
    """literal for 'edge {u,v} present in backedge graph'.
    Arc v->u  iff (u - v) mod q in S; then edge iff u precedes v."""
    if (u - v) % q in S:      # arc v -> u
        return prec_lit(var, u, v)
    else:                     # arc u -> v
        return prec_lit(var, v, u)

def build_cnf(verts, q, S):
    var = {}
    cnt = 0
    for u, v in itertools.combinations(verts, 2):
        cnt += 1
        var[(u, v)] = cnt
    clauses = []
    for a, b, c in itertools.permutations(verts, 3):
        if a < c:  # avoid duplicating (a,b,c)/(c,b,a) symmetric clauses
            clauses.append([-prec_lit(var, a, b), -prec_lit(var, b, c),
                            prec_lit(var, a, c)])
    for a, b, c in itertools.combinations(verts, 3):
        clauses.append([-edge_lit(var, q, S, a, b),
                        -edge_lit(var, q, S, a, c),
                        -edge_lit(var, q, S, b, c)])
    return cnt, clauses

def run_kissat(cnt, clauses):
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', delete=False) as f:
        f.write(f"p cnf {cnt} {len(clauses)}\n")
        for cl in clauses:
            f.write(' '.join(map(str, cl)) + ' 0\n')
        path = f.name
    try:
        r = subprocess.run(['kissat', '-q', path], capture_output=True, text=True)
        out = r.stdout
        if 's UNSATISFIABLE' in out:
            return 'UNSAT'
        if 's SATISFIABLE' in out:
            return 'SAT'
        return 'UNKNOWN:' + out[:200]
    finally:
        os.unlink(path)

def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for n in range(lo, hi + 1):
        q, S = make_T(n)
        full = run_kissat(*build_cnf(range(q), q, S))
        dele = run_kissat(*build_cnf(range(1, q), q, S))
        verdict_full = 'omega>=3' if full == 'UNSAT' else ('omega<=2 (!!)' if full == 'SAT' else full)
        verdict_del = 'omega<=2' if dele == 'SAT' else ('omega>=3 (!!)' if dele == 'UNSAT' else dele)
        print(f"n={n} (q={q}): T_n -> {full} [{verdict_full}], "
              f"T_n - 0 -> {dele} [{verdict_del}]", flush=True)
        assert full == 'UNSAT' and dele == 'SAT', f"CLAIM FAILS at n={n}"
    print(f"SAT check passes for n={lo}..{hi}: every ordering of T_n has a "
          "backedge triangle; T_n - 0 has a triangle-free ordering.")

if __name__ == '__main__':
    main()
