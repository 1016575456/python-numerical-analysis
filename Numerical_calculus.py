import numpy as np
import sympy
from math import *


def Cotes_coefficient(n):
    C = [0 for i in range(n + 1)]
    t = sympy.symbols('t')
    for i in range(n + 1):
        f = 1
        for k in range(n + 1):
            if k != i:
                f *= t - k
        Integral_item = sympy.integrate(f, (t, 0, n))
        C[i] = 1 / n * (-1) ** (n - i) / (factorial(i) * factorial(n - i)) * Integral_item
    return C


def Cotes(a, b, f, n):
    I = 0
    X = np.linspace(a, b, n + 1)
    f_x = [f.subs('x', i) for i in X]
    C = Cotes_coefficient(n)
    for k in range(n + 1):
        I += C[k] * f_x[k]
    I *= b - a
    return I


def composite_integration(a, b, f, n, method):
    if method == "T_n":
        T_n = 0
        h = np.linspace(a, b, n + 1)
        for i in range(n):
            T_n += Cotes(h[i], h[i + 1], f, 1)
        return T_n
    elif method == "S_n":
        S_n = 0
        h = np.linspace(a, b, n + 1)
        for i in range(n):
            S_n += Cotes(h[i], h[i + 1], f, 2)
        return S_n


def Legendpo(n):
    x = sympy.symbols('x')
    lengendre_po, solution = [1, x], []
    for i in range(2, n + 1):
        pn = ((2 * i - 1) * x * lengendre_po[i - 1] - (i - 1) * lengendre_po[i - 2]) / i
        lengendre_po.append(pn)
    X_k = list(sympy.solve(sympy.Eq(lengendre_po[-1], 0), x))
    AK = [sympy.symbols('A' * i) for i in range(1, n + 1)]
    f = [x ** j for j in range(n)]
    for each in f:
        determine = 0
        for k in range(n):
            determine += AK[k] * each.subs(x, X_k[k])
        solution.append(determine)
    res = [sympy.integrate(x ** j, (x, -1, 1)) for j in range(n)]
    equation = list(np.array(solution) - np.array(res))
    A_k = list(sympy.linsolve(equation, AK))
    return [X_k, A_k]


def Gauss_legendre(a, b, f, n):
    x = sympy.symbols('x')
    result = 0
    node, coef = Legendpo(n)
    for i in range(n):
        result += (b - a) / 2 * f.subs(x, (b - a) / 2 * node[i] + (a + b) / 2) * coef[0][i]
    return result


def Error_analysis(exact, value):
    return abs(exact - value)


