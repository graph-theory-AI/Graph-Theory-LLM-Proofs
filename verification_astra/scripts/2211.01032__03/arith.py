"""Re-derive the closed forms (13),(14),(15) and the final constant."""
import math
G = 0.5772156649015329
print(f"{'n':>7} {'series(13) exact':>17} {'ln n-3/2':>10} {'factor(14)':>11} {'1/2':>5} "
      f"{'prod':>9} {'(1/2)ln n-3/4':>14} {'bound(2)':>9} {'(1/2)lnn+1+g/2':>15} {'total bound':>12} {'ln n+1/4+g/2':>13}")
for n in (50, 100, 200, 1000, 10**4, 10**6, 10**9):
    q = 1 - 1.0 / (n - 2)
    ser = sum(q ** (k - 2) / k for k in range(3, 20000000)) if n <= 1000 else None
    cf = q ** -2 * (-math.log(1 - q) - q - q * q / 2)
    if ser is not None:
        assert abs(ser - cf) < 1e-9 * max(1, cf), (ser, cf)
    R = math.ceil(4 * math.log2(n)); D = n - 2 - R
    fac = (n - 1) * (n - 2) / (2.0 * D * D)
    Hn2 = sum(1.0 / j for j in range(1, n - 1)) if n <= 10**6 else math.log(n - 2) + G + 1/(2*(n-2))
    tot = 1 + Hn2 / 2 + fac * cf + 1.0 / n
    print(f"{n:7d} {cf:17.6f} {math.log(n)-1.5:10.6f} {fac:11.6f} {0.5:5.2f} "
          f"{fac*cf:9.6f} {0.5*math.log(n)-0.75:14.6f} {1+Hn2/2:9.6f} "
          f"{0.5*math.log(n)+1+G/2:15.6f} {tot:12.6f} {math.log(n)+0.25+G/2:13.6f}")
