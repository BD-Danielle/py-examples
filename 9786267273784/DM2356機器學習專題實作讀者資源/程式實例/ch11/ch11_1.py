# ch11_1.py
import random           # 導入模組random

min = 1
max = 6
target = 5
n = 10000
counter = 0
for i in range(n):
    if target == random.randint(min, max):
        counter += 1
print(f'經過 {n} 次, 得到 {counter} 次 {target}')
P = counter / n
print(f'機率 P = {P}')






        

