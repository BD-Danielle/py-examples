# ch11_4.py
from fractions import Fraction

x = Fraction(5, 6)
p1 = x**3               # 不出現 5 的機率
p2 = 1 - p1             # 出現 1 次 5 的機率

print(f'連擲 3 次骰子, 不出現 5    的機率 : {float(p1):.4f}')
print(f'連擲 3 次骰子, 出現 1 次 5 的機率 : {float(p2):.4f}')




