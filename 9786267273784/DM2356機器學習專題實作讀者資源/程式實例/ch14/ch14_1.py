# ch14_1.py
import numpy as np

n = np.linspace(1.1, 10, 90)        # 建立1.1-10的陣列
count = 0                           # 用於計算每5筆輸出換行
for i in n:
    count += 1
    print(f'{i:2.1f} = {np.log10(i):4.3f}', end='    ')
    if count % 5 == 0:              # 每5筆輸出就換行
        print()







