# ch31_6.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# 創建一個簡單的12個二維數據點的資料集
X = np.array([[32, 3.5], [18, 0.9], [80, 15], [41, 4.8],
                 [25, 1.3], [55, 13],[70, 14.5], [33, 4.1],
                 [20, 1.9], [23, 1.7], [66, 12], [40, 3.8]])

# 設定K值
K = 3

# 使用scikit-learn的KMeans方法進行分群
kmeans = KMeans(n_clusters=K, random_state=42)
kmeans.fit(X)

# 獲得分群標籤和分群中心
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 創建一個DataFrame來存儲身長、體重和分類結果
df = pd.DataFrame(X, columns=['身長', '體重'])

# 將標籤加入DataFrame
df['分類'] = labels

# 將結果儲存為CSV檔案
df.to_csv('fish_classification.csv', index=False, encoding='cp950')

# 繪製結果
plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*')
plt.title("無監督學習 - 捕獲魚的分類",fontsize=16)
plt.xlabel("身長")
plt.ylabel("體重")
plt.show()







