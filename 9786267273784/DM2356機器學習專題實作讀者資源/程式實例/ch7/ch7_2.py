# ch7_2.py
from sympy import *

x = Symbol('x')
f = Symbol('f')
# 2 個實數根
f = x**2 - 2*x - 8
root = solve(f)
print(f"有 2 個實數根 : {root}")

# 1 個實數根
f = x**2 - 2*x + 1
root = solve(f)
print(f"有 1 個實數根 : {root}")

# 沒有實數根
f = x**2 + x + 1
root = solve(f)
print(f"沒有個實數根  : {root}")







