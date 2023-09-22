# ch18_1.py
from sympy import Symbol, solve

a = Symbol('a')
b = Symbol('b')
eq1 = -a + b -2
eq2 = a + b - 4
ans = solve((eq1, eq2))
print(f'a = {ans[a]}')
print(f'b = {ans[b]}')







