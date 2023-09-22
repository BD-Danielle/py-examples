# ch11_2.py
import matplotlib.pyplot as plt
from random import randint

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

min = 1
max = 6                                 # 骰子有幾面
times = 10000                           # 擲骰子次數

dice = [0] * 7                          # 建立擲骰子的串列
for i in range(times):
    data = randint(min, max)
    dice[data] += 1
    
del dice[0]                             # 刪除索引0資料
    
for i, c in enumerate(dice, 1):
    print(f'{i} = {c} 次')
    
x = [i for i in range(1, max+1)]        # 長條圖x軸座標
width = 0.35                            # 長條圖寬度
plt.bar(x, dice, width, color='g')      # 繪製長條圖
plt.xlabel('骰子數字')
plt.ylabel('頻率(出現次數)')
plt.title('擲骰子 10000 次')
plt.show()




