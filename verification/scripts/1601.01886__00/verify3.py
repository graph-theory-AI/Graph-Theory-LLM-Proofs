#!/usr/bin/env python3
"""
Third verification pass for attack 1601.01886__00: certified pathwidth of
R_h and D_h for larger h, without any pathwidth search.

Upper bounds: an explicit path-decomposition of R_h of width ceil(h/2) (resp.
of D_h of width ceil((h+1)/2)) is CONSTRUCTED following the writeup's Lemma 1
converse gluing, and then VALIDATED by an independent checker that verifies,
from first principles, the three path-decomposition axioms:
  (i) every vertex occurs in a non-empty contiguous interval of bags,
  (ii) every edge is contained in some bag,
  (iii) the width (max bag size - 1) equals the claimed value.

Lower bounds: the concrete combinatorial content of the standard 3-branch
lower-bound certificate is checked on the graph itself:
  in R_h (h>=2), deleting the branch vertex x_{h-1} of one top copy leaves
  >= 3 components each fully containing a canonical copy of R_{h-2};
  in D_h (h>=1), deleting x_h of one copy of R_h leaves >= 3 components each
  fully containing a canonical copy of R_{h-1}.
Combined with the easy direction of the Ellis-Sudborough-Turner criterion
(if some vertex has >= 3 branches of pathwidth >= k-1 then pw >= k) and
subgraph-monotonicity of pathwidth, this certifies
  pw(R_h) >= 1 + pw(R_{h-2}) and pw(D_h) >= 1 + pw(R_{h-1}),
grounded at the machine-verified base cases pw(R_0)=0, pw(R_1)=1.
"""
import sys
from math import ceil
sys.setrecursionlimit(1000000)
import itertools

# ------------------------------------------------------------- build with meta
def build_R_meta(h, counter=None, adj=None):
    """Build R_h; return (adj, meta) where meta is a nested record:
       {'h': j, 'root': r, 'x': x or None, 'verts': frozenset,
        'children': [meta, meta]}"""
    if counter is None:
        counter = itertools.count()
        adj = {}
    def newv():
        v = next(counter); adj[v] = set(); return v
    def add(u, v): adj[u].add(v); adj[v].add(u)
    def rec(j):
        if j == 0:
            r = newv()
            return {'h': 0, 'root': r, 'x': None, 'verts': frozenset([r]),
                    'children': []}
        m1 = rec(j - 1)
        m2 = rec(j - 1)
        x = newv(); r = newv()
        add(r, x); add(x, m1['root']); add(x, m2['root'])
        return {'h': j, 'root': r, 'x': x,
                'verts': m1['verts'] | m2['verts'] | {x, r},
                'children': [m1, m2]}
    meta = rec(h)
    return adj, meta, counter

def build_D_meta(h):
    counter = itertools.count()
    adj = {}
    adj1, m1, counter = build_R_meta(h, counter, adj)
    adj2, m2, counter = build_R_meta(h, counter, adj)
    adj[m1['root']].add(m2['root']); adj[m2['root']].add(m1['root'])
    return adj, m1, m2

# ------------------------------------------- explicit path-decomposition (UB)
def descend(meta):
    """Descending path inside R_j starting at its root: r_j, x_j, r_{j-1}, ...
    Returns (path_vertex_list, hangers) where hangers is a list of
    (attach_vertex_on_path, sub_meta_of_hanging_R_i)."""
    path, hangers = [], []
    m = meta
    while True:
        path.append(m['root'])
        if m['h'] == 0:
            return path, hangers
        path.append(m['x'])
        c1, c2 = m['children']
        hangers.append((m['x'], c2))   # the other child hangs at x
        m = c1

def pd_of_meta(meta):
    """Path decomposition (list of bags) of a standalone R_h, width ceil(h/2)."""
    h = meta['h']
    if h == 0:
        return [frozenset([meta['root']])]
    if h == 1:
        c1, c2 = meta['children']
        x, r = meta['x'], meta['root']
        return [frozenset([c1['root'], x]), frozenset([x, r]),
                frozenset([x, c2['root']])]
    c1, c2 = meta['children']
    p1, h1 = descend(c1)
    p2, h2 = descend(c2)
    # global path: reverse(p1) + [x_h] + p2 ; r_h hangs at x_h
    path = list(reversed(p1)) + [meta['x']] + p2
    hang = {}
    for (a, sm) in h1 + h2:
        hang.setdefault(a, []).append(sm)
    hang.setdefault(meta['x'], []).append(
        {'h': 0, 'root': meta['root'], 'x': None,
         'verts': frozenset([meta['root']]), 'children': []})
    return glue(path, hang)

def glue(path, hang):
    """Lemma 1 converse gluing: concatenate along `path`, inserting the
    recursive decompositions of hanging pieces with the attach vertex added."""
    bags = []
    for i, p in enumerate(path):
        bags.append(frozenset([p]))   # ensure p occurs even with no hangers
        for sm in hang.get(p, []):
            for b in pd_of_meta(sm):
                bags.append(b | {p})
        if i + 1 < len(path):
            bags.append(frozenset([p, path[i + 1]]))
    return bags

def pd_of_D(h, m1, m2):
    p1, h1 = descend(m1)
    p2, h2 = descend(m2)
    path = list(reversed(p1)) + p2   # joined by the root-root edge
    hang = {}
    for (a, sm) in h1 + h2:
        hang.setdefault(a, []).append(sm)
    return glue(path, hang)

def check_pd(adj, bags, claimed_width):
    """First-principles validation of a path decomposition."""
    occ = {}
    for i, b in enumerate(bags):
        for v in b:
            occ.setdefault(v, []).append(i)
    assert set(occ) == set(adj), "vertex missing from decomposition"
    for v, ids in occ.items():
        assert ids == list(range(ids[0], ids[-1] + 1)), f"interval broken for {v}"
    for u in adj:
        for v in adj[u]:
            if u < v:
                assert any(u in b and v in b for b in bags), f"edge {u},{v} uncovered"
    w = max(len(b) for b in bags) - 1
    assert w == claimed_width, f"width {w} != claimed {claimed_width}"
    return w

# ----------------------------------------------------- 3-branch LB certificate
def components(adj, vset):
    seen, out = set(), []
    for s in vset:
        if s in seen: continue
        stack, comp = [s], set()
        seen.add(s)
        while stack:
            v = stack.pop(); comp.add(v)
            for u in adj[v]:
                if u in vset and u not in seen:
                    seen.add(u); stack.append(u)
        out.append(comp)
    return out

def all_copies(meta, level, acc=None):
    if acc is None: acc = []
    if meta['h'] == level:
        acc.append(meta['verts'])
        return acc
    for c in meta['children']:
        all_copies(c, level, acc)
    return acc

def check_lb_R(adj, meta):
    """Verify the concrete 3-branch facts for pw(R_h) >= 1 + pw(R_{h-2})."""
    h = meta['h']
    assert h >= 2
    x = meta['children'][0]['x']        # x_{h-1} of the first top copy
    targets = all_copies(meta, h - 2)
    comps = components(adj if isinstance(adj, dict) else adj,
                       meta['verts'] - {x})
    good = sum(1 for c in comps if any(t <= c for t in targets))
    assert good >= 3, f"R_{h}: only {good} branches at x_(h-1) contain an R_{h-2}"
    return good

def check_lb_D(adj, m1, m2, h):
    assert h >= 1
    x = m1['x']                          # x_h of the left copy
    targets = all_copies(m1, h - 1) + all_copies(m2, h - 1)
    vall = m1['verts'] | m2['verts']
    comps = components(adj, vall - {x})
    good = sum(1 for c in comps if any(t <= c for t in targets))
    assert good >= 3, f"D_{h}: only {good} branches at x_h contain an R_{h-1}"
    return good

# ----------------------------------------------------------------------- main
def main():
    print("== certified pathwidth: UB by validated explicit decomposition,")
    print("   LB by concrete 3-branch certificate ==")
    print("-- R_h --")
    lbchain = {0: 0, 1: 1}  # machine-checkable bases: R_0 single vertex, R_1 = K_{1,3}
    for h in range(0, 12):
        adj, meta, _ = build_R_meta(h)
        k = ceil(h / 2)
        bags = pd_of_meta(meta)
        check_pd(adj, bags, k if h > 0 else 0)
        lbnote = ""
        if h >= 2:
            g = check_lb_R(adj, meta)
            lbnote = (f"; LB cert: x_(h-1) has {g}>=3 branches each containing an"
                      f" R_{h-2} => pw >= 1+pw(R_{h-2})")
        print(f"  R_{h} (n={len(adj)}): valid path-decomposition of width {k}{lbnote}")
    print("  => with pw(R_0)=0, pw(R_1)=1: pw(R_h) = ceil(h/2) for all h <= 11")
    print("-- D_h --")
    for h in range(0, 11):
        adj, m1, m2 = build_D_meta(h)
        k = ceil((h + 1) / 2)
        bags = pd_of_D(h, m1, m2)
        check_pd(adj, bags, k)
        lbnote = ""
        if h >= 1:
            g = check_lb_D(adj, m1, m2, h)
            lbnote = (f"; LB cert: x_h has {g}>=3 branches each containing an"
                      f" R_{h-1} => pw >= 1+pw(R_{h-1})")
        print(f"  D_{h} (n={len(adj)}): valid path-decomposition of width {k}{lbnote}")
    print("  => pw(D_h) = ceil((h+1)/2) for all h <= 10;"
          " in particular pw(D_(2k-1)) = k for k = 1..5")
    print("VERIFY3: ALL CHECKS PASSED")

if __name__ == "__main__":
    main()
