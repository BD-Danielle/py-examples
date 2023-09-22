# ch31_7.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 建立 300 個點, n_features=2, centers=3
X, y = make_blobs(n_samples=300, n_features=2, centers=3,
                  random_state=10)
                                  
kmeans = KMeans(n_clusters=3)           # k-mean方法建立 3 個群集中心
kmeans.fit(X)                           # 將數據帶入物件, 做群集分析

# 印出WCSS
print(f"WCSS : {kmeans.inertia_}")

plt.rcParams["font.family"] = ["Microsoft JhengHei"]    # 微軟正黑體
plt.rcParams["axes.unicode_minus"] = False              # 可以顯示負號
# 繪圓點, 圓點用黑色外框, 使用標籤 labels_ 區別顏色, 
plt.scatter(X[:,0], X[:,1], marker="o", c=kmeans.labels_)
# 用紅色標記群集中心
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            marker="*", color="red")
plt.title("無監督學習",fontsize=16)
plt.show()














