# ch12_2.py
import matplotlib.pyplot as plt
import math 
def probability(k):
    num = (math.factorial(n))/(math.factorial(n-k)*math.factorial(k))
    pro = num * success**k * (1-success)**(n-k)
    return pro

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
  
n = 10                                      # 銷售次數  
success = 0.35                              # 銷售成功機率
fail = 1 - success                          # 銷售失敗機率
p = []                                      # 儲存成功機率

for k in range(0,n+1):
    if k == 0:
        p.append(fail**n)                   # 連續n次失敗機率
        continue
    if k == n:
        p.append(success**n)                # 連續n次成功機率
        continue
    p.append(probability(k))                # 計算其他次成功機率

for i in range(len(p)):
    print(f'銷售 {i} 單位成功機率 {p[i]*100}%')
        
x = [i for i in range(0, n+1)]              # 長條圖x軸座標
width = 0.35                                # 長條圖寬度
plt.xticks(x)
plt.bar(x, p, width, color='g')             # 繪製長條圖
plt.ylabel('機率')
plt.xlabel('銷售單位:100')
plt.title('二項式分佈')
plt.show()




