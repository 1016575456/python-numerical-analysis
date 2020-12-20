import sympy
import numpy as np
import random

def Dichotomy(a, b, f, R):
    x = sympy.symbols('x')
    f_a, f_b = f.subs(x, a), f.subs(x, b)
    if abs(b-a) < R:
        return (a + b) / 2
    if (f.subs(x, (a + b) / 2) > 0 and f_a > f_b) or (f.subs(x, (a + b) / 2) < 0 and f_a < f_b):
        return Dichotomy((a + b) / 2, b, f, R)
    elif (f.subs(x, (a + b) / 2) > 0 and f_a < f_b) or (f.subs(x, (a + b) / 2) < 0 and f_a > f_b):
        return Dichotomy(a, (a + b) / 2, f, R)


def Newton_itera(a,b,f,R):
    x = sympy.symbols('x')
    X_k = [random.uniform(a,b),"x2"]
    X_k[-1] = float(X_k[-2] - f.subs(x,X_k[-2])/(sympy.diff(f,x).subs(x,X_k[-2])))
    while(abs(X_k[-1]-X_k[-2])>=R):
        x_k = float(X_k[-1] - f.subs(x,X_k[-1])/(sympy.diff(f,x).subs(x,X_k[-1])))
        X_k.append(x_k)
    return X_k