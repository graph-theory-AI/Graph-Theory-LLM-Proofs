"""Referee verification for attack 1710.11281__02.

Claims checked numerically on the round sphere of radius rho = 1/(4*pi):

 (A) intrinsic diameter = pi*rho = 1/4 < 1/2, and every pair of points is
     within distance 1/4  =>  radius-1/2 capture is trivial (holds at t=0).
 (B) the antipodal map A(x) = -x is an isometry with constant displacement
     d(x, A(x)) = 1/4 for all x.
 (C) delayed-shadowing: for ANY 1-Lipschitz cop path C and tau = 1/8, the
     robber path R(t) = A(C(0)) for t <= tau, R(t) = A(C(t-tau)) for t >= tau
     is 1-Lipschitz and satisfies d(C(t), R(t)) >= 1/4 - 1/8 = 1/8 for all t.
     We test it against several cop behaviours, including a greedy pursuer
     that reacts to the robber's actual position (i.e. a closed-loop cop),
     and against random 1-Lipschitz cop paths.

Geodesic distance on the sphere of radius rho embedded in R^3:
    d(x, y) = rho * arccos(<x, y> / rho^2).
All motion is discretized with step dt; each step moves along the great
circle by arc length <= dt (so paths are 1-Lipschitz up to discretization).
"""

import numpy as np

rng = np.random.default_rng(20260902)

RHO = 1.0 / (4.0 * np.pi)   # sphere radius
D = np.pi * RHO             # intrinsic diameter = 1/4
TAU = D / 2.0               # delay = 1/8
DT = 1e-3                   # time step
T_END = 20.0                # simulate 20 time units (>> tau)


def gdist(x, y):
    c = np.dot(x, y) / RHO**2
    return RHO * np.arccos(np.clip(c, -1.0, 1.0))


def rand_point():
    v = rng.normal(size=3)
    return RHO * v / np.linalg.norm(v)


def step_towards(x, target, arclen):
    """Move from x towards target along the great circle by <= arclen."""
    d = gdist(x, target)
    if d < 1e-15:
        return x.copy()
    t = min(1.0, arclen / d)
    # slerp on the sphere
    ang = d / RHO
    a = np.sin((1 - t) * ang) / np.sin(ang)
    b = np.sin(t * ang) / np.sin(ang)
    p = a * x + b * target
    return RHO * p / np.linalg.norm(p)


def step_random(x, arclen):
    """Move from x in a uniformly random tangent direction by arclen."""
    v = rng.normal(size=3)
    v -= (np.dot(v, x) / np.dot(x, x)) * x
    n = np.linalg.norm(v)
    if n < 1e-15:
        return x.copy()
    v /= n
    ang = arclen / RHO
    p = np.cos(ang) * x + np.sin(ang) * RHO * v
    return RHO * p / np.linalg.norm(p)


def antipode(x):
    return -x


def run_game(cop_policy, label):
    """cop_policy(cop_pos, robber_pos, t) -> new cop_pos (must move <= DT)."""
    n_steps = int(round(T_END / DT))
    delay_steps = int(round(TAU / DT))
    C = rand_point()
    cop_hist = [C.copy()]
    R = antipode(cop_hist[0])           # robber starts at A(C(0))
    min_dist = gdist(C, R)
    max_cop_step = 0.0
    max_rob_step = 0.0
    for i in range(1, n_steps + 1):
        C_new = cop_policy(C, R, i * DT)
        max_cop_step = max(max_cop_step, gdist(C, C_new))
        C = C_new
        cop_hist.append(C.copy())
        # robber: R(t) = A(C(t - tau)) for t >= tau, else A(C(0))
        j = max(0, i - delay_steps)
        R_new = antipode(cop_hist[j])
        max_rob_step = max(max_rob_step, gdist(R, R_new))
        R = R_new
        min_dist = min(min_dist, gdist(C, R))
    print(f"  {label:34s} min d(C,R) = {min_dist:.6f}  "
          f"(bound {D - TAU:.6f}); max cop step {max_cop_step:.2e}, "
          f"max robber step {max_rob_step:.2e} (dt={DT:.0e})")
    return min_dist, max_rob_step


def greedy_cop(C, R, t):
    return step_towards(C, R, DT)


def make_random_cop():
    state = {"target": rand_point()}

    def policy(C, R, t):
        if gdist(C, state["target"]) < 2 * DT:
            state["target"] = rand_point()
        return step_towards(C, state["target"], DT)

    return policy


def make_drunk_cop():
    def policy(C, R, t):
        return step_random(C, DT)
    return policy


def anticipating_cop(C, R, t):
    # cop heads for the antipode of its own position at full speed:
    # tries to "meet" the robber where the robber is going.
    return step_towards(C, antipode(C), DT)


def still_cop(C, R, t):
    return C.copy()


print("=== (A) diameter / trivial capture check ===")
print(f"rho = 1/(4 pi) = {RHO:.6f}, intrinsic diameter pi*rho = {D:.6f}")
assert abs(D - 0.25) < 1e-12
worst = 0.0
for _ in range(200000):
    x, y = rand_point(), rand_point()
    worst = max(worst, gdist(x, y))
print(f"max distance over 200000 random pairs = {worst:.6f}  (must be <= 0.25 < 0.5)")
assert worst <= 0.25 + 1e-9

print("\n=== (B) antipodal map: isometry with constant displacement ===")
disp = [gdist(x, antipode(x)) for x in (rand_point() for _ in range(10000))]
print(f"d(x, A(x)) over 10000 random x: min {min(disp):.9f}, max {max(disp):.9f}")
assert max(abs(v - 0.25) for v in disp) < 1e-6  # arccos loses ~1e-8 near -1
iso_err = 0.0
for _ in range(10000):
    x, y = rand_point(), rand_point()
    iso_err = max(iso_err, abs(gdist(x, y) - gdist(antipode(x), antipode(y))))
print(f"max |d(x,y) - d(Ax,Ay)| over 10000 random pairs = {iso_err:.2e}")
assert iso_err < 1e-6

print("\n=== (C) delayed shadowing vs several cop behaviours ===")
print(f"tau = {TAU:.6f}, claimed lower bound D - tau = {D - TAU:.6f}")
results = []
results.append(run_game(greedy_cop, "greedy pursuit (closed-loop)"))
results.append(run_game(anticipating_cop, "runs to own antipode"))
results.append(run_game(still_cop, "stationary cop"))
for k in range(3):
    results.append(run_game(make_random_cop(), f"random-waypoint cop #{k+1}"))
for k in range(2):
    results.append(run_game(make_drunk_cop(), f"random-walk cop #{k+1}"))

bound = D - TAU
tol = 2 * DT  # discretization tolerance
ok = all(m >= bound - tol for m, _ in results)
lip_ok = all(s <= DT + 1e-12 for _, s in results)
print(f"\nAll runs respect min distance >= {bound:.6f} - O(dt): {ok}")
print(f"Robber discretized path is 1-Lipschitz (steps <= dt): {lip_ok}")

print("\n=== extra: exact-lemma spot check on random Lipschitz cop paths ===")
# direct check of d(C(t), A(C(t - tau))) >= D - d(C(t), C(t-tau)) >= D - tau
worst_gap = np.inf
for trial in range(20):
    n = 4000
    C = rand_point()
    hist = [C]
    for _ in range(n):
        C = step_random(C, DT)
        hist.append(C)
    ds = int(round(TAU / DT))
    for i in range(ds, n + 1):
        lhs = gdist(hist[i], antipode(hist[i - ds]))
        worst_gap = min(worst_gap, lhs - (D - gdist(hist[i], hist[i - ds])))
print(f"min over 20 random paths of  d(C(t),A(C(t-tau))) - (D - d(C(t),C(t-tau)))"
      f" = {worst_gap:.3e}  (triangle ineq. => must be >= ~0)")
assert worst_gap > -1e-9
print("\nALL CHECKS PASSED")
