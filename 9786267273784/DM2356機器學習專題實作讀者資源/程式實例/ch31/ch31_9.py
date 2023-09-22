# ch31_9.py
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

# 生成簡單的資料
X = np.array([[1, 2], [1, 4], [1, 0],
             [4, 2], [4, 4], [4, 0]])

# 真實的標籤
true_labels = np.array([0, 0, 0, 1, 1, 1])

# 使用K-means進行分群
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# 獲得分群標籤
predicted_labels = kmeans.labels_

# 計算調整蘭德(ARI)
ari = adjusted_rand_score(true_labels, predicted_labels)
print(f"調整蘭德(ARI)係數 : {ari}")

