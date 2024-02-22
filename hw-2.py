#The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical approximation of 1 / π

import math

#定義ziqi為遞迴式
def ziqi(n):
    if n == 0:
        return 1
    else:
        recurse = ziqi(n-1)
        result = n * recurse
        return result

#定義estimate_pi為預估值
def estimate_pi():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = ziqi(4*k) * (1103 + 26390*k)
        den = ziqi(k)**4 * 396**(4*k)
        term = factor * num / den
        total += term
        
        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total

print(estimate_pi())
print(math.pi)