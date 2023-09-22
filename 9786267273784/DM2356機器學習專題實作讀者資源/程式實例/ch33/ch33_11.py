# ch33_11.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import numpy as np

data = pd.read_csv('oldfaithful.csv')

# 將特徵進行標準化
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# 進行凝聚性分群
cluster = AgglomerativeClustering(n_clusters=2)
data['class'] = cluster.fit_predict(data_scaled)

# 將結果寫入新的CSV文件
data.to_csv('oldfaithful_with_class.csv', index=False)

# 繪製散點圖，不同顏色表示不同的分群
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
colors = ['blue', 'green']
for i in range(2):
    plt.scatter(data[data['class'] == i]['Eruptions'], 
                data[data['class'] == i]['Waiting'], 
                c=colors[i])

plt.xlabel('爆發持續時間Eruptions(分鐘)')
plt.ylabel('等待時間Waiting(分鐘)')
plt.title('老實泉Old Faithful Geyser data')
plt.show()
