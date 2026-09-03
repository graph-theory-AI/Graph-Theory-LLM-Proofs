#!/usr/bin/env python3
"""Verify the explicit drawings claimed in attacks/2009.03418__00/output.md.

The writeup draws the octahedron O = K_{2,2,2} (parts {a_i,b_i}) planarly,
adds an apex z inside face a1a2a3, and routes z-b_i, a1b1, a2b2 as described,
claiming drawings of M_{7,3}, M_{7,2}, M_{7,1} with 3, 4, 6 crossings.

We realize the drawing with explicit rational polyline arcs (outer face =
b1b2b3 in the plane, which is face B on the sphere) and count all proper
pairwise crossings exactly (Fraction arithmetic). Any degenerate contact
(collinear overlap, touch at a non-shared endpoint, crossing at a polyline
breakpoint) is reported as a FAILURE of the encoding.
"""
from fractions import Fraction as F
from itertools import combinations

# ---------- exact segment intersection ----------

def seg_int(p, q, r, s):
    """Classify intersection of segments pq and rs (exact rational).
    Returns (kind, point) where kind in {'none','proper','touch','overlap'}."""
    def sub(u, v):
        return (u[0] - v[0], u[1] - v[1])
    def cross(u, v):
        return u[0] * v[1] - u[1] * v[0]
    d1, d2 = sub(q, p), sub(s, r)
    denom = cross(d1, d2)
    diff = sub(r, p)
    if denom == 0:
        if cross(diff, d1) != 0:
            return ('none', None)
        # collinear: check 1-D overlap
        def dot(u, v):
            return u[0] * v[0] + u[1] * v[1]
        L = dot(d1, d1)
        t0, t1 = F(dot(diff, d1), L), F(dot(sub(s, p), d1), L)
        lo, hi = min(t0, t1), max(t0, t1)
        if hi < 0 or lo > 1:
            return ('none', None)
        if hi == 0 or lo == 1:
            return ('touch', None)  # touch at an endpoint, collinear
        return ('overlap', None)
    t = F(cross(diff, d2), denom)
    u = F(cross(diff, d1), denom)
    if 0 <= t <= 1 and 0 <= u <= 1:
        pt = (p[0] + t * d1[0], p[1] + t * d1[1])
        if 0 < t < 1 and 0 < u < 1:
            return ('proper', pt)
        return ('touch', pt)
    return ('none', None)


# ---------- coordinates (all rational) ----------
P = {
    'b1': (F(0), F(10)), 'b2': (F(-10), F(-6)), 'b3': (F(10), F(-6)),
    'a1': (F(0), F(-3)), 'a2': (F(3), F(2)),   'a3': (F(-3), F(2)),
    'z':  (F(1, 5), F(1, 3)),
}

def pl(*names_or_pts):
    out = []
    for x in names_or_pts:
        if isinstance(x, str):
            out.append(P[x])
        else:
            out.append((F(x[0]), F(x[1])))
    return out

# Octahedron edges (straight lines): all pairs except a_i b_i.
octa = ['a1a2', 'a1a3', 'a2a3', 'b1b2', 'b1b3', 'b2b3',
        'a1b2', 'a1b3', 'a2b1', 'a2b3', 'a3b1', 'a3b2']
E = {}
for name in octa:
    u, v = name[:2], name[2:]
    E[name] = pl(u, v)

# Apex edges. za_i straight inside face a1a2a3.
E['za1'] = pl('z', 'a1')
E['za2'] = pl('z', 'a2')
E['za3'] = pl('z', 'a3')
# zb1: straight up, crossing a2a3 at (0,2), through face b1a2a3 to b1.
E['zb1'] = pl('z', 'b1')
# zb2: crosses a1a3, continues in face b2a1a3 to b2 (waypoint just past a1a3).
E['zb2'] = pl('z', (-2, F(-9, 10)), 'b2')
# zb3: mirror image.
E['zb3'] = pl('z', (2, F(-9, 10)), 'b3')
# a1b1: down through face a1b2b3, cross b2b3 at (0,-6), around outside
# (= interior of sphere-face B = b1b2b3, the outer face here) to b1.
E['a1b1'] = pl('a1', (0, -8), (16, -8), (16, 13), 'b1')
# a2b2: through face b1a2b3, cross b1b3 at (5,2), around the outside to b2,
# crossing a1b1's outer portion exactly once (at (16,2)).
E['a2b2'] = pl('a2', (7, F(3, 2)), (20, 2), (20, 18), (-20, 18), (-20, -7), 'b2')

def endpoints(name):
    if name.startswith('z'):
        return {'z', name[1:]}
    return {name[:2], name[2:]}

def crossings(edge_names):
    """Return list of proper crossings between non-adjacent edges; assert no
    degeneracies anywhere (including polyline breakpoints and touches)."""
    found = []
    problems = []
    for e1, e2 in combinations(edge_names, 2):
        shared = endpoints(e1) & endpoints(e2)
        pts = []
        for i in range(len(E[e1]) - 1):
            for j in range(len(E[e2]) - 1):
                kind, pt = seg_int(E[e1][i], E[e1][i + 1], E[e2][j], E[e2][j + 1])
                if kind == 'none':
                    continue
                if kind == 'overlap':
                    problems.append((e1, e2, 'collinear overlap'))
                elif kind == 'touch':
                    # allowed only if the touch point is a shared graph vertex
                    ok = any(pt == P[v] for v in shared) if pt else False
                    if not ok:
                        problems.append((e1, e2, f'degenerate touch at {pt}'))
                else:
                    pts.append(pt)
        # de-duplicate touches at a shared vertex counted from both incident segments
        uniq = set(pts)
        if len(uniq) != len(pts):
            problems.append((e1, e2, 'repeated crossing point'))
        for pt in uniq:
            if shared:
                problems.append((e1, e2, f'ADJACENT edges cross at {pt}'))
            else:
                found.append((tuple(sorted((e1, e2))), pt))
        if len(uniq) > 1:
            problems.append((e1, e2, f'{len(uniq)} mutual crossings (not a good drawing)'))
    return found, problems

def report(tag, edge_names, expected_count, expected_pairs=None):
    found, problems = crossings(edge_names)
    print(f'--- {tag}: {len(edge_names)} edges ---')
    for (pair, pt) in sorted(found):
        print(f'  crossing {pair[0]} x {pair[1]} at ({float(pt[0]):.3f},{float(pt[1]):.3f})')
    for pr in problems:
        print(f'  PROBLEM: {pr}')
    ok = (len(found) == expected_count) and not problems
    if expected_pairs is not None:
        got_pairs = sorted(p for p, _ in found)
        ok = ok and got_pairs == sorted(expected_pairs)
    print(f'  crossings = {len(found)} (expected {expected_count})  ->',
          'OK' if ok else 'FAILURE')
    return ok

all_ok = True
# 0) octahedron alone must be planar (0 crossings)
all_ok &= report('octahedron K_{2,2,2}', octa, 0)
# 1) M_{7,3}: octahedron + z-edges, claimed 3 crossings
m73 = octa + ['za1', 'za2', 'za3', 'zb1', 'zb2', 'zb3']
all_ok &= report('M_{7,3} drawing', m73, 3,
                 expected_pairs=[('a2a3', 'zb1'), ('a1a3', 'zb2'), ('a1a2', 'zb3')])
# 2) M_{7,2}: add a1b1, claimed 4 crossings
m72 = m73 + ['a1b1']
all_ok &= report('M_{7,2} drawing', m72, 4,
                 expected_pairs=[('a2a3', 'zb1'), ('a1a3', 'zb2'), ('a1a2', 'zb3'),
                                 ('a1b1', 'b2b3')])
# 3) M_{7,1}: add a2b2, claimed 6 crossings
m71 = m72 + ['a2b2']
all_ok &= report('M_{7,1} drawing', m71, 6,
                 expected_pairs=[('a2a3', 'zb1'), ('a1a3', 'zb2'), ('a1a2', 'zb3'),
                                 ('a1b1', 'b2b3'), ('a2b2', 'b1b3'), ('a1b1', 'a2b2')])

# 4) sanity: edge sets really are K_7 minus the right matchings
V = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'z']
K7 = {frozenset(p) for p in combinations(V, 2)}
def eset(names):
    return {frozenset(endpoints(n)) for n in names}
missing73 = K7 - eset(m73)
missing72 = K7 - eset(m72)
missing71 = K7 - eset(m71)
print('missing edges M_{7,3}:', sorted(tuple(sorted(e)) for e in missing73))
print('missing edges M_{7,2}:', sorted(tuple(sorted(e)) for e in missing72))
print('missing edges M_{7,1}:', sorted(tuple(sorted(e)) for e in missing71))
assert missing73 == {frozenset({'a1', 'b1'}), frozenset({'a2', 'b2'}), frozenset({'a3', 'b3'})}
assert missing72 == {frozenset({'a2', 'b2'}), frozenset({'a3', 'b3'})}
assert missing71 == {frozenset({'a3', 'b3'})}
print('edge-set checks OK (matchings of sizes 3, 2, 1 removed)')

# 5) verify the straight-line octahedron drawing has the claimed facial
#    structure implicitly: planarity certified by 0 crossings above, and the
#    drawing is connected/spanning by construction.
print()
print('ALL CHECKS PASSED' if all_ok else 'SOME CHECK FAILED')
