import sympy as sp


def dot(a, b):
    eta = (1, -1, -1, -1)
    return sp.expand(sum(eta[i] * a[i] * b[i] for i in range(4)))


def test_rfg_current_projection_identity():
    k = sp.symbols("k0:4", real=True)
    q = sp.symbols("q0:4", real=True)
    jl = sp.symbols("jl0:4", real=True)
    jr = sp.symbols("jr0:4", real=True)
    kq = tuple(k[i] + q[i] for i in range(4))
    lhs = (
        dot(jl, k) * dot(jr, k)
        - dot(jl, kq) * dot(jr, kq)
    ) / (dot(k, k) * dot(kq, kq))
    rhs = -(
        dot(jl, k) * dot(jr, q)
        + dot(jl, q) * dot(jr, k)
        + dot(jl, q) * dot(jr, q)
    ) / (dot(k, k) * dot(kq, kq))
    assert sp.simplify(lhs-rhs) == 0


def test_rfg_sufficient_transversality_condition():
    X, Y, U, V = sp.symbols("X Y U V")
    numerator = X*Y - (X+U)*(Y+V)
    assert sp.simplify(numerator.subs({X: 0, Y: -V})) == 0


def test_rfg_generic_rational_point_is_nonzero():
    k = (3, 2, 0, 0)
    q = (1, 0, 1, 0)
    jl = (1, 0, 0, 0)
    jr = (0, 1, 0, 0)
    kq = tuple(k[i]+q[i] for i in range(4))
    value = (
        dot(jl, k)*dot(jr, k)-dot(jl, kq)*dot(jr, kq)
    )/(dot(k, k)*dot(kq, kq))
    assert value == sp.Rational(2, 55)
