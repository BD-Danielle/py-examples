# ch6_1.py
from sympy import Symbol, solve
                                
x = Symbol('x')                     # 定義公式中使用的變數
y = Symbol('y')                     # 定義公式中使用的變數
eq1 = 8 - 0.6 * x - y               # 公式 1
eq2 = 17.5 - 2.5 * x - y            # 公式 2
ans = solve((eq1, eq2))
print(f'x = {int(ans[x])}')
print(f'y = {int(ans[y])}')

z = 50 * int(ans[x]) + 50 * int(ans[y])
print(f'最大獲利 = {z} 萬')








