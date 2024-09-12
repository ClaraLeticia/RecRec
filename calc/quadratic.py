from math import sqrt

def quadratic(a, b, c )-> dict:
    b = b/a
    c = c/a
    d = b**2 - 4 * a * c
    r1 = (-b + sqrt(d)) / 2 * a
    r2 = (-b - sqrt(d)) / 2 * a
    return {'r1':r1, 'r2': r2, 'd': d }
    

def greaterThanZero(a,b,d) -> dict:
    r1 = (-b + sqrt(d)) / 2 * a
    r2 = (-b - sqrt(d)) / 2 * a
    return {'r1':r1, 'r2': r2, 'html': 'greater.html', 'd': d }

def equalZero(a,b,d) -> dict:
    r1 = (-b + sqrt(d)) / 2 * a
    r2 = (-b - sqrt(d)) / 2 * a
    return {'r1':r1, 'r2': r2, 'html': 'equal.html' }

