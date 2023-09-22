# ch33_10.py
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler

# 讀取CSV文件
data = pd.read_csv('oldfaithful.csv')

# 將特徵進行標準化
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# 進行凝聚性分群
Z = linkage(data_scaled, method='ward')

# 繪製樹狀圖
plt.figure(figsize=(10, 5))
dendrogram(Z, leaf_rotation=90, leaf_font_size=8)
plt.show()


