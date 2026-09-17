"""Sanity test of the exact predicate harness: a configuration that IS degenerate
must be detected.  Even polygon h=6 + center: v0, o, v3 are collinear."""
import sympy as sp, itertools
from verify import build, orient, sgn, proper_cross
P = build(6, [(0,0)])
bad = [t for t in itertools.combinations(range(7),3) if orient(P,*t)==0]
print("h=6 (EVEN) + center, collinear triples detected:", bad)
assert bad, "harness failed to detect known degeneracy"
print("orient(v0,o,v3) =", orient(P,0,6,3), "(must be 0)")
# odd h=5: no antipodal pair, so no degeneracy
P5 = build(5, [(0,0)])
bad5 = [t for t in itertools.combinations(range(6),3) if orient(P5,*t)==0]
print("h=5 (ODD) + center, collinear triples:", bad5)
# sanity: a crossing that is only an endpoint touch must NOT count as proper
print("proper_cross(v0v2, v0v3) (share endpoint) =", proper_cross(P5,0,2,0,3), "(must be False)")
print("proper_cross(v0v2, v1v3) =", proper_cross(P5,0,2,1,3), "(must be True)")
