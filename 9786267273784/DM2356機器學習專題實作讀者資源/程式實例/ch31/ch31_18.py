# ch31_18.py
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('wine_reviews.csv')

# 只選擇 'points' 和 'price' 這兩個特徵
selected_features = ['points', 'price']
X = data[selected_features]

# 資料預處理 - 缺失值填充
X = X.fillna(X.mean())

# 定義 K-means 模型，設定我們要分成3個群集
kmeans = KMeans(n_clusters=3, random_state=0)

# 使用 K-means 模型進行訓練
kmeans.fit(X)

# 將分群結果儲存到 'value' 特徵中
data['value'] = kmeans.labels_

# 儲存 'points', 'price', 'value' 到 CSV 文件中
data[selected_features + ['value']].to_csv('wine_report.csv', index=False)

# 畫出散點圖和群集的中心
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.scatter(X['points'], X['price'], c=data['value'])
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            c='red', marker='*')
plt.xlabel('評分')
plt.ylabel('價格')
plt.title('葡萄酒評價 評分 vs 價格')
plt.show()
