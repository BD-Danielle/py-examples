# ch4_2.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號
                                
a = Symbol('a')                 # 定義公式中使用的變數
b = Symbol('b')                 # 定義公式中使用的變數
eq1 = 600*a + b                 # 方程式 1
eq2 = 1000*a + b - 12           # 方程式 2
ans = solve((eq1, eq2))
print(f'a = {ans[a]}')
print(f'b = {ans[b]}')

pt_x1 = 600                             
pt_y1 = ans[a] * pt_x1 + ans[b]     # 計算x=600時的y值
pt_x2 = 1000
pt_y2 = ans[a] * pt_x2 + ans[b]     # 計算x=1000時的y值

x = np.linspace(0, 2500, 250)
y = ans[a] * x + ans[b]
plt.plot(x, y)                          # 繪函數直線
plt.plot(pt_x1, pt_y1, '-o')            # 繪點 P1
plt.text(pt_x1+60, pt_y1-2, 'P1')       # 輸出文字P1
plt.plot(pt_x2, pt_y2, '-o')            # 繪點 P2
plt.text(pt_x2+60, pt_y2-2, 'P2')       # 輸出文字P2
plt.xlabel("來客數")
plt.ylabel("利潤")
plt.grid()                              # 加格線
plt.show()






