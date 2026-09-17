"""Check the retry writeup's geometric odd-walk lemma.

Lemma: a,b,c in R^3 linearly independent => the subgraph of O induced by all
lines contained in P_a u P_b u P_c is non-bipartite.

Proof under test: build the walk E^n F with E = J_a^2 J_b^2, F = J_a J_c J_b,
x0 a real eigenvector of E^n F.  Verify:
  (i) the matrix formulas (2) for E and F,
  (ii) every consecutive pair of the walk is a genuine edge of O
       (nonzero, perpendicular, distinct lines),
  (iii) every line of the walk lies in P_a u P_b u P_c,
  (iv) the walk is closed and of odd length 3+4n.
"""
import numpy as np, itertools, sys

rng = np.random.default_rng(20260917)

def J(d, x):
    return np.cross(d, x)

def normalize_frame(a, b, c):
    """Rotate so a=(0,0,1), b=(s,0,t) with s>0,0<t<1; return (s,t,u,v,w) and rotation R."""
    a = a/np.linalg.norm(a); b = b/np.linalg.norm(b); c = c/np.linalg.norm(c)
    if np.dot(a, b) < 0: b = -b
    e3 = a
    # component of b orthogonal to a
    bp = b - np.dot(b, a)*a
    e1 = bp/np.linalg.norm(bp)
    e2 = np.cross(e3, e1)
    R = np.vstack([e1, e2, e3])   # rows = new basis; R @ v gives coords
    A, B, C = R@a, R@b, R@c
    return A, B, C, R

def build_walk(a, b, c, nmax=4000):
    A, B, C, R = normalize_frame(a, b, c)
    s, t = B[0], B[2]
    u, v, w = C
    assert abs(A[0]) < 1e-12 and abs(A[1]) < 1e-12 and abs(A[2]-1) < 1e-12
    assert abs(B[1]) < 1e-12 and s > 0 and 0 < t < 1, (A, B)
    # claimed matrices
    E = np.array([[t**2, 0.0], [0.0, 1.0]])
    F = np.array([[0.0, s*u + t*w], [-t*w, s*v]])
    # verify them against the actual operators on P_a (= span(e1,e2) in new frame)
    for basis in ([1.0, 0.0], [0.0, 1.0]):
        x = np.array([basis[0], basis[1], 0.0])
        Ex = J(A, J(A, J(B, J(B, x))))
        Fx = J(A, J(C, J(B, x)))
        assert np.allclose(Ex[:2], E@np.array(basis)) and abs(Ex[2]) < 1e-12, (Ex, E@np.array(basis))
        assert np.allclose(Fx[:2], F@np.array(basis)) and abs(Fx[2]) < 1e-12, (Fx, F@np.array(basis))
    # least n with positive discriminant, computed in closed form (Delta_n -> (sv)^2 > 0)
    import math
    K = 4*t*w*(s*u + t*w)
    n = 0 if K <= 0 else max(0, math.ceil(math.log((s*v)**2/K)/(2*math.log(t))))
    if n > nmax:
        raise ValueError(f"n={n} exceeds cap {nmax} (a,b nearly parallel: t={t:.9f})")
    M = np.linalg.matrix_power(E, n) @ F
    disc = (s*v)**2 - 4*(t**(2*n))*t*w*(s*u + t*w)
    assert abs(disc - ((M[0,0]+M[1,1])**2 - 4*np.linalg.det(M))) < 1e-8*max(1, abs(disc)), "formula (3) wrong"
    assert disc > 0, "discriminant not positive"
    assert abs(np.linalg.det(M)) > 0, "E^n F singular"
    evals, evecs = np.linalg.eig(M)
    assert np.all(np.abs(evals.imag) < 1e-9), evals
    k = int(np.argmax(np.abs(evals.real)))
    lam = evals[k].real
    assert abs(lam) > 1e-9
    x0 = evecs[:, k].real
    x0 = x0/np.linalg.norm(x0)
    # now build the explicit walk in the ORIGINAL frame
    Rt = R.T
    x = Rt @ np.array([x0[0], x0[1], 0.0])
    a1, b1, c1 = Rt@A, Rt@B, Rt@C
    walk = [x]
    ops = [b1, c1, a1] + n*[b1, b1, a1, a1]   # F then n copies of E
    for d in ops:
        x = J(d, x)
        walk.append(x)
    return walk, a1, b1, c1, n, lam

def check(a, b, c, verbose=False):
    walk, a1, b1, c1, n, lam = build_walk(a, b, c)
    L = len(walk) - 1
    assert L == 3 + 4*n, (L, n)
    assert L % 2 == 1
    # (ii) edges
    for i in range(L):
        p, q = walk[i], walk[i+1]
        assert np.linalg.norm(p) > 1e-9 and np.linalg.norm(q) > 1e-9, "zero vector in walk"
        assert abs(np.dot(p, q)) < 1e-7*np.linalg.norm(p)*np.linalg.norm(q), "not perpendicular"
    # (iii) containment in P_a u P_b u P_c
    for p in walk:
        pn = p/np.linalg.norm(p)
        ok = min(abs(np.dot(pn, a1/np.linalg.norm(a1))),
                 abs(np.dot(pn, b1/np.linalg.norm(b1))),
                 abs(np.dot(pn, c1/np.linalg.norm(c1)))) < 1e-7
        assert ok, "line escapes P_a u P_b u P_c"
    # (iv) closed as LINES
    p0 = walk[0]/np.linalg.norm(walk[0]); pE = walk[-1]/np.linalg.norm(walk[-1])
    assert np.linalg.norm(np.cross(p0, pE)) < 1e-7, "walk not closed"
    if verbose:
        print(f"  n={n} length={L} lambda={lam:.6g} closed OK")
    return n, L

bad = 0
skipped = 0
lengths = {}
for trial in range(4000):
    a, b, c = rng.normal(size=(3, 3))
    if abs(np.linalg.det(np.vstack([a, b, c]))) < 1e-3: continue
    if min(abs(np.dot(a,b)), abs(np.dot(a,c)), abs(np.dot(b,c))) < 1e-3: continue
    try:
        n, L = check(a, b, c)
        lengths[L] = lengths.get(L, 0) + 1
    except AssertionError as e:
        bad += 1
        print("FAIL", a, b, c, e)
    except ValueError as e:
        skipped += 1
print("random generic triples tested:", sum(lengths.values()), " failures =", bad,
      " skipped (n above cap) =", skipped)
print("walk-length histogram:", dict(sorted(lengths.items())))

# near-degenerate cases: a,b almost perpendicular, c almost in span(a,b)
print("\nstress: near-degenerate but still generic triples")
bad = 0; worst = 0; skipped2 = 0; done = 0
for trial in range(400):
    a = rng.normal(size=3); a /= np.linalg.norm(a)
    # b nearly perpendicular to a
    eps = 10.0**rng.uniform(-3, -1)
    e = rng.normal(size=3); e -= np.dot(e,a)*a; e /= np.linalg.norm(e)
    b = a + eps*e; b /= np.linalg.norm(b)          # a,b nearly PARALLEL: t -> 1
    c = rng.normal(size=3); c /= np.linalg.norm(c)
    if min(abs(np.dot(a,c)), abs(np.dot(b,c))) < 1e-3: continue
    if abs(np.linalg.det(np.vstack([a,b,c]))) < 1e-9: continue
    try:
        n, L = check(a, b, c); worst = max(worst, L)
    except AssertionError as ex:
        bad += 1; print("FAIL", eps, ex)
    except ValueError:
        skipped2 += 1
    else:
        done += 1
print("near-parallel a,b: tested", done, " failures =", bad, " skipped (n above cap) =", skipped2, " max walk length =", worst)
