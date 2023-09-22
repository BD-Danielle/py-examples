# ch7_10.py
from sympy import Symbol, solve

a = Symbol('a')                 # 定義公式中使用的變數
b = Symbol('b')                 # 定義公式中使用的變數
c = Symbol('c')                 # 定義公式中使用的變數

eq1 = a + b + c - 500           # 第100次公式
eq2 = 4*a + 2*b + c - 1000      # 第200次公式
eq3 = 9*a + 3*b + c - 2000      # 第300次公式
ans = solve((eq1, eq2, eq3))
print(f'a = {ans[a]}')
print(f'b = {ans[b]}')
print(f'c = {ans[c]}')










