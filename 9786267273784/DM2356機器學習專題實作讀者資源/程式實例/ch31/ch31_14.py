# ch31_14.py
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 讀取資料
data = pd.read_csv('Mall_Customers.csv')

# 選擇 'Annual Income' 和 'Spending Score' 作為特徵
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# 假設我們要將數據分成 5 個群集
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

# 獲取每個點的群集標籤
labels = kmeans.labels_

# 將標籤添加到原始數據集中
data['cluster'] = labels

# 儲存帶有標籤的資料到CSV
data.to_csv('Mall_Customers_labels.csv', index=False)

# 繪製分群結果
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.scatter(data['Annual Income (k$)'], data['Spending Score (1-100)'],
            c=data['cluster'])
plt.title('購物中心客戶群集 Clusters of customers')
plt.xlabel('年收入 Annual Income (k$)')
plt.ylabel('消費力 Spending Score (1-100)')
plt.show()
