from math import sqrt

def quadratic(a, b, c )-> dict:
    b = b/a
    c = c/a
    print(a, b, c, b**2 - 4 * a * c)
    d = b**2 - 4 * a * c
    r1 = (-b + sqrt(d)) / 2 * a
    r2 = (-b - sqrt(d)) / 2 * a
    return {'r1':r1, 'r2': r2, 'delta': d }
