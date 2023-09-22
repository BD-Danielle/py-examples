# ch11_11.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

sides = 6
# 建立 10000 個 1-6(含) 的整數隨機數 
dice = np.random.randint(1,sides+1,size=10000)  # 建立隨機數
    
h = plt.hist(dice, sides)                       # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.xlabel('點數')
plt.ylabel('頻率(出現次數)')
plt.title('測試10000次')
plt.show()
    





