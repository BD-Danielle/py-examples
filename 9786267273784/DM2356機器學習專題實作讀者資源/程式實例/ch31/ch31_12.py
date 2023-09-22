# ch31_12.py
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 創建一個有300個點的數據集
X, y = make_blobs(n_samples=300, centers=4, random_state=1)

silhouette_scores = []      # 初始化空串列來存儲輪廓分數

# 我們在此選擇在2到10群集數檢查輪廓分數
for n_cluster in range(2, 11):
    silhouette_scores.append(
        silhouette_score(X, KMeans(n_clusters = n_cluster).fit_predict(X)))

# 繪製每個n_clusters的輪廓分數
k = [2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.bar(k, silhouette_scores)
plt.xlabel('Number of clusters', fontsize = 10)
plt.ylabel('Silhouette Score', fontsize = 10)
plt.show()


