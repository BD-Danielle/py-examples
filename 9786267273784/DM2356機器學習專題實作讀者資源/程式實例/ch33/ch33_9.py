# ch33_9.py
import pandas as pd
import matplotlib.pyplot as plt

# 讀取CSV文件
data = pd.read_csv('oldfaithful.csv')

# 創建散點圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.scatter(data['Eruptions'], data['Waiting'])
plt.xlabel('爆發持續時間Eruptions(分鐘)')
plt.ylabel('等待時間Waiting(分鐘)')
plt.title('老實泉Old Faithful Geyser data')
plt.grid(True)
plt.show()




