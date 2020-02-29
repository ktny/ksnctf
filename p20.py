from __future__ import with_statement
import decimal

def pi(prec):
    with decimal.localcontext() as ctx:
        ctx.prec = prec+2
        lasts = 0
        t = decimal.Decimal(3)
        s = 3
        n = 1
        na = 0
        d = 0
        da = 24
        while s != lasts:
            lasts = s
            n += na
            na += 8
            d += da
            da += 32
            t = (t * n) / d
            s += t
    return s

def is_prime(n: int):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for p in range(3, int(n**0.5)+1, 2):
        if n % p == 0:
            return False
    return True

PI = str(pi(100))
for i in range(2, 100):
    a = int(PI[i:i+10])
    if is_prime(a):
        print(i, 'FLAG_Q20_{}'.format(a))
        exit()