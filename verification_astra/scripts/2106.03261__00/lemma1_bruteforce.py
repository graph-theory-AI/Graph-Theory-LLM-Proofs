"""Independent numeric check of Lemma 1 (writeup attacks_retry/2106.03261__00).

Claim: in PG(2,K), char K odd, B nondegenerate symmetric.  If ten pairwise distinct
points A0..A4,B0..B4 are placed on the Petersen graph so that all 14 edges except
a3b3 are orthogonal pairs, and A0,A1 are nonisotropic, then A3 _|_ B3 as well.

Here we enumerate the configuration directly over F_q for several q and for a
RANDOM (not necessarily diagonal) nondegenerate symmetric form, i.e. we do not
reuse the writeup's normalisation.
"""
import itertools, random, sys

def run(q, form=None, seed=0, fixA0A1_all=False):
    rnd = random.Random(seed)
    F = range(q)
    def norm(P):  # projective normalisation
        for c in P:
            if c % q:
                inv = pow(c % q, q-2, q)
                return tuple((x*inv) % q for x in P)
        return None
    pts = []
    seen = set()
    for P in itertools.product(F, repeat=3):
        if P == (0,0,0): continue
        n = norm(P)
        if n not in seen:
            seen.add(n); pts.append(n)
    assert len(pts) == q*q+q+1
    if form is None:
        while True:
            a,b,c,d,e,f = [rnd.randrange(q) for _ in range(6)]
            M = [[a,b,c],[b,d,e],[c,e,f]]
            det = (a*(d*f-e*e) - b*(b*f-e*c) + c*(b*e-d*c)) % q
            if det: break
    else:
        M = form
    def bil(P,Q):
        return sum(M[i][j]*P[i]*Q[j] for i in range(3) for j in range(3)) % q
    def pol(P):
        return tuple(sum(M[i][j]*P[j] for j in range(3)) % q for i in range(3))
    def cross(u,v):
        return norm(((u[1]*v[2]-u[2]*v[1]) % q, (u[2]*v[0]-u[0]*v[2]) % q,
                     (u[0]*v[1]-u[1]*v[0]) % q))
    polar = {P: [Q for Q in pts if bil(P,Q)==0] for P in pts}
    nonis = [P for P in pts if bil(P,P)!=0]
    tested = nontrivial = viol = 0
    a0list = nonis if fixA0A1_all else nonis[:2]
    for A0 in a0list:
        for A1 in polar[A0]:
            if A1==A0 or bil(A1,A1)==0: continue
            for A2 in polar[A1]:
                for A4 in polar[A0]:
                    for B0 in polar[A0]:
                        for B1 in polar[A1]:
                            S = {A0,A1,A2,A4,B0,B1}
                            if len(S)<6: continue
                            if A2==A4 or B0==B1 or B0==A2 or B1==A4: continue
                            A3 = cross(pol(A2),pol(A4))
                            B3 = cross(pol(B0),pol(B1))
                            B2 = cross(pol(B0),pol(A2))
                            B4 = cross(pol(B1),pol(A4))
                            if len({A0,A1,A2,A3,A4,B0,B1,B2,B3,B4})<10: continue
                            tested += 1
                            lhs = bil(A3,B3); rhs = bil(B2,B4)
                            if rhs==0:
                                nontrivial += 1
                                if lhs!=0: viol += 1
                            # also record the stronger identity (equal up to the
                            # specific representatives chosen)
                            if (lhs==0) != (rhs==0):
                                viol += 1
    return dict(q=q, M=M, tested=tested, with_b2b4_orth=nontrivial, violations=viol)

if __name__ == '__main__':
    for q in (5,7,11,13):
        for seed in (1,2):
            r = run(q, seed=seed)
            print(f"q={q} seed={seed} form={r['M']}")
            print(f"   full 10-point configs enumerated (A0,A1 from 2 base points): {r['tested']}"
                  f"; of these with B2 _|_ B4: {r['with_b2b4_orth']}"
                  f"; VIOLATIONS of 'B2_|_B4 => A3_|_B3': {r['violations']}")
