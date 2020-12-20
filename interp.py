import sympy
from math import pi
import numpy as np


def Lagrange_interp(X, Y, z):
    """拉格朗日插值多项式"""
    x = sympy.symbols('x')
    L, n = 0, len(X)
    for i in range(n):
        l = 1
        for j in range(n):
            if i != j:
                l *= (x - X[j]) / (X[i] - X[j])
        L += l * Y[i]
    return L.subs(x, z)


def Newton_interp(X, Y, x):
    """计算x点的插值"""
    sum = Y[0]
    temp = np.zeros((len(X), len(X)))
    # 将第一行赋值
    for i in range(0, len(X)):
        temp[i, 0] = Y[i]
    temp_sum = 1
    for i in range(1, len(X)):
        print(sum)
        # x的多项式
        temp_sum = temp_sum * (x - X[i - 1])
        # 计算均差
        for j in range(i, len(X)):
            temp[j, i] = (temp[j, i - 1] - temp[j - 1, i - 1]) / (X[j] - X[j - i])
        sum += temp_sum * temp[i, i]

    return sum


def get_diff_table(X, Y):
    '''得到插商表'''
    n = len(X)
    diff_table = np.zeros([n, n])

    for i in range(0, n):
        diff_table[i][0] = Y[i]

    for j in range(1, n):
        for i in range(j, n):
            diff_table[i][j] = (diff_table[i][j - 1] - diff_table[i - 1][j - 1])/ (X[i] - X[i - j])

    return diff_table

