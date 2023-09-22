# ch34_4_2.py
import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

# 讀取資料
data = pd.read_csv('Mall_Customers.csv')

# 選擇 'Annual Income' 和 'Spending Score' 作為特徵
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# 標準化數據
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 建立 DBSCAN 物件並進行擬合
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan.fit(X)

# 獲取每個點的群集標籤
labels = dbscan.labels_
print(labels)

# 將標籤添加到原始數據集中
data['cluster'] = labels

# 儲存帶有標籤的資料到CSV
data.to_csv('Mall_labels34_4_2.csv', index=False)

# 定義一個顏色映射：將 -1 映射為紅色，其他的分為多種顏色
colors = ['black' if x == -1 else 'C{}'.format(x) for x in labels]

# 繪製分群結果
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'],
            c=colors)
plt.title('DBSCAN 分析購物數據 eps=0.3, min_samples=5')
plt.xlabel('年收入 Annual Income (k$)')
plt.ylabel('消費力 Spending Score (1-100)')
plt.show()
