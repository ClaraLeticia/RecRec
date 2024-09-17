from math import atan, sqrt, degrees
from operator import neg

def quadratic(a, b, c )-> dict:
    b = b/a
    c = c/a
    print(a, b, c, b**2 - 4 * a * c)
    d = b**2 - 4 * a * c
    if d >= 0:   
        r1 = (-b + sqrt(d)) / 2 * a
        r2 = (-b - sqrt(d)) / 2 * a
        p = None
        alpha = None
    else:
        r1 = complex(-b / (2 * a), sqrt(abs(d)) / (2 * a))
        r2 = complex(-b / (2 * a), neg(sqrt(abs(d)) / (2 * a)))

        p = round(sqrt(pow(sqrt(abs(d)) / (2 * a), 2) + pow((-b / (2 * a)), 2)))
        alpha = round(degrees(atan((sqrt(abs(d)) / (2 * a)) / (-b / (2 * a)))))
    return {'r1': round(r1,2), 'r2': round(r2,2), 'delta': d, 'p': p, 'alpha':alpha}
