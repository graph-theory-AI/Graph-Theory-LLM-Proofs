"""Section 4: the explicit proper 4-colouring of O (including boundary directions).
Exact integer arithmetic: lines are primitive integer vectors; adjacency iff dot product 0."""
import itertools, math
from fractions import Fraction

def canon(v):
    """The writeup's representative rule, applied to a primitive integer direction."""
    x, y, z = v
    if z < 0 or (z == 0 and (y < 0 or (y == 0 and x < 0))):
        x, y, z = -x, -y, -z
    return (x, y, z)

def colour(v):
    x, y, z = canon(v)
    if (x, y) == (0, 0):
        return 2            # the pole [e3] gets the third colour (index 2)
    ang = math.atan2(y, x) % (2*math.pi)
    q = int(ang // (math.pi/2))
    # guard against float boundary error using exact sign tests
    if y == 0 and x > 0: q = 0
    elif x == 0 and y > 0: q = 1
    elif y == 0 and x < 0: q = 2
    elif x == 0 and y < 0: q = 3
    return q

def primitive(v):
    g = math.gcd(math.gcd(abs(v[0]), abs(v[1])), abs(v[2]))
    return (v[0]//g, v[1]//g, v[2]//g)

N = 6
lines = {}
for v in itertools.product(range(-N, N+1), repeat=3):
    if v == (0, 0, 0): continue
    lines[canon(primitive(v))] = None
V = sorted(lines)
print(f"lines with primitive integer direction, sup-norm <= {N}: {len(V)}")
col = {v: colour(v) for v in V}
bad = 0; edges = 0
for u, w in itertools.combinations(V, 2):
    if u[0]*w[0] + u[1]*w[1] + u[2]*w[2] == 0:
        edges += 1
        if col[u] == col[w]:
            bad += 1
            if bad < 5: print("  MONOCHROMATIC EDGE", u, w, col[u])
print(f"orthogonal pairs: {edges};  monochromatic edges: {bad}")
print("colour class sizes:", {c: sum(1 for v in V if col[v] == c) for c in range(4)})
# targeted boundary stress: equatorial lines and the pole
eq = [v for v in V if v[2] == 0]
print("equatorial lines:", len(eq), " their colours:", sorted(set(col[v] for v in eq)),
      "(writeup claims colour 2 is never used on the equator)")
pole = (0, 0, 1)
print("pole colour:", col[pole],
      " neighbours of the pole are exactly the equatorial lines:",
      all((v[2] == 0) == (v[0]*0+v[1]*0+v[2]*1 == 0) for v in V))
# random real directions too
import numpy as np
rng = np.random.default_rng(7)
def colour_real(u):
    x, y, z = u
    if z < 0 or (z == 0 and (y < 0 or (y == 0 and x < 0))): x, y, z = -x, -y, -z
    if x == 0 and y == 0: return 2
    return int((math.atan2(y, x) % (2*math.pi)) // (math.pi/2))
bad2 = 0
for _ in range(200000):
    u = rng.normal(size=3); u /= np.linalg.norm(u)
    # build a genuinely perpendicular partner
    w = rng.normal(size=3); w = w - np.dot(w, u)*u; w /= np.linalg.norm(w)
    if colour_real(u) == colour_real(w): bad2 += 1
print("random perpendicular pairs of real lines tested: 200000, monochromatic:", bad2)
