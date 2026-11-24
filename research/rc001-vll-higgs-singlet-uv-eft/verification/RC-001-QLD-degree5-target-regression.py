#!/usr/bin/env python3
"""Independent regression of the corrected QLD degree-five expansion core.

The numerator coefficients and reduce_graph algorithm are taken from the
production source
RC-001-QLD-hard-expansion-numerator-audit.py (Git blob
e0562fe1f2f7980b8d681f713b016b74d28b1390).

This regression checks the shifted-denominator Taylor factors, the scalar
external-degree selection, and the d-dimensional angular-pairing structure
counts. It deliberately does not repeat the radial master integrations,
soft-region integration, or hard-soft matching in the production script.
"""
import sympy as sp

d = sp.symbols('d')
k2, kq, kp, kpp = sp.symbols('k2 kq kp kpp')
p2, q2, pp2, pq, ppdotp = sp.symbols('p2 q2 pp2 pq ppdotp')

# Exact numerator coefficients from the current producer source.
NL = {'k': k2 + 2*kp + pq, 'p': -(k2 + kq), 'q': k2 + kp}
NE = {'k': k2 - sp.Symbol('M2') - ppdotp, 'p': k2 + kpp, 'pp': k2 + kp}
DOT = {
    ('p','p'): p2, ('q','q'): q2, ('pp','pp'): pp2,
    ('p','q'): pq, ('q','p'): pq,
    ('p','pp'): ppdotp, ('pp','p'): ppdotp,
}

def pairings(labels):
    labels = tuple(labels)
    if not labels:
        return {sp.Integer(1): 1}
    out = {}
    first = labels[0]
    for j in range(1, len(labels)):
        second = labels[j]
        rest = labels[1:j] + labels[j+1:]
        dot = DOT[(first, second)]
        for product, mult in pairings(rest).items():
            term = sp.expand(dot * product)
            out[term] = out.get(term, 0) + mult
    return out

def angular_denominator(r):
    return d * sp.prod(d + 2*j for j in range(1, r))

def reduce_graph(kind, component, numerator):
    if kind == 'L':
        vectors = ['q', 'p']
        kvars = [kq, kp]
        shifts = [2*kq + q2, 2*kp + p2]
        base_a, base_b = 2, 1
    else:
        vectors = ['p', 'pp']
        kvars = [kp, kpp]
        shifts = [2*kp + p2, 2*kpp + pp2]
        base_a, base_b = 1, 2
    target = 5 if component == 'k' else 4
    result = {}
    poly_vars = [k2, *kvars, p2, q2, pp2, pq, ppdotp]
    retained = 0
    for n in range(target + 1):
        for m in range(target + 1 - n):
            polynomial = (-1)**(n+m) * sp.expand(shifts[0]**n * shifts[1]**m * numerator)
            poly = sp.Poly(polynomial, *poly_vars, domain='EX')
            for mon, coeff in poly.terms():
                ex = dict(zip(poly_vars, mon))
                degree = ex[kvars[0]] + ex[kvars[1]] + 2*sum(
                    ex[s] for s in [p2, q2, pp2, pq, ppdotp]
                )
                if degree != target:
                    continue
                retained += 1
                labels = [vectors[0]]*ex[kvars[0]] + [vectors[1]]*ex[kvars[1]]
                scalar = coeff
                for sym in [p2, q2, pp2, pq, ppdotp]:
                    scalar *= sym**ex[sym]
                if kind == 'L':
                    a, b = base_a + n, base_b + m
                else:
                    a, b = base_a, base_b + n + m
                if component == 'k':
                    if len(labels) % 2 != 1:
                        continue
                    r = (len(labels) + 1)//2
                    den = angular_denominator(r)
                    for i, vec in enumerate(labels):
                        rest = labels[:i] + labels[i+1:]
                        for product, mult in pairings(rest).items():
                            key = (vec, a, b, ex[k2] + r)
                            result[key] = result.get(key, 0) + 2*scalar*mult*product/den
                else:
                    if len(labels) % 2:
                        continue
                    r = len(labels)//2
                    den = angular_denominator(r) if r else 1
                    product = sum(mult*term for term, mult in pairings(tuple(labels)).items())
                    key = (component, a, b, ex[k2] + r)
                    result[key] = result.get(key, 0) + 2*scalar*product/den
    return ({key: sp.factor(value) for key, value in result.items() if value != 0}, retained)

L = {c: reduce_graph('L', c, n) for c, n in NL.items()}
E = {c: reduce_graph('E', c, n) for c, n in NE.items()}
counts = {
    'L': {c: len(L[c][0]) for c in NL},
    'E': {c: len(E[c][0]) for c in NE},
}
raw = {
    'L': {c: L[c][1] for c in NL},
    'E': {c: E[c][1] for c in NE},
}
assert counts['L'] == {'k': 31, 'p': 12, 'q': 12}
assert counts['E'] == {'k': 14, 'p': 3, 'pp': 3}
assert raw['L'] == {'k': 42, 'p': 22, 'q': 22}
assert raw['E'] == {'k': 48, 'p': 22, 'pp': 22}
print('CURRENT SOURCE REDUCTION STRUCTURES')
print('Light:', counts['L'])
print('Heavy:', counts['E'])
print('RETAINED TERM INSTANCES BEFORE ANGULAR PAIRING (not unique after Taylor-order combination)')
print('Light:', raw['L'])
print('Heavy:', raw['E'])
print('PASS: explicit-vector components selected at scalar degree 4; free k^mu at degree 5.')
print('PASS: light graph expands both (k+q)^2 and (k+p)^2+M^2 denominators.')
print('PASS: heavy graph expands both (k+p)^2+M^2 and (k+p\')^2+M^2 denominators.')
