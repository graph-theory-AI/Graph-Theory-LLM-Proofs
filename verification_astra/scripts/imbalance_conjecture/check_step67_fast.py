from math import comb
F = lambda b,l: comb(l,2) - (b-1)*l
bad7=bad6=0; ex6=[]
for D in range(4, 121):
    for k in range(2, D):
        b=D-k
        for t in range(0, k+1):
            r=b+t
            mx=max(F(b,l) for l in range(0,r+1))
            if mx != max(0, comb(t+1,2)-comb(b,2)): bad7+=1
            if mx > (k-1)*t:
                bad6+=1
                if len(ex6)<5: ex6.append((D,k,b,t,mx,(k-1)*t))
print("D=4..120: (7) violations", bad7, " (6) violations", bad6, ex6)
low=[]
for D in (2,3):
    for k in range(2,D):
        b=D-k
        for t in range(0,k+1):
            mx=max(F(b,l) for l in range(0,b+t+1))
            if mx>(k-1)*t: low.append((D,k,b,t,mx,(k-1)*t))
print("D<=3 (excluded regime) (6) violations:", low)
