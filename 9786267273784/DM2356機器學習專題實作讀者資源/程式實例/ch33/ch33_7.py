# ch33_7.py
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pandas as pd

# 定義列名稱
column_names = ['面積','周長','粗造度','長度',
                '寬度','不對稱係數','長度比', '分類']

# 讀取數據並加上列名稱
data = pd.read_csv('seeds_dataset.txt', sep='\t', header=None,
                   names=column_names)

# 複製原始數據, 刪除 '分類' 特徵, 防止影響後續操作
data_without_class = data.copy()
data_without_class = data_without_class.drop('分類', axis=1)

# 使用凝聚型分群
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean',
                                  linkage='ward')
labels = cluster.fit_predict(data_without_class)
labels += 1                         # 分群從 1 開始

# 將分群結果新增到原始數據中
data['我的分群'] = labels

# 將數據寫回csv檔案
data.to_csv('seeds_classification.csv', index=False, encoding='cp950')

# 使用Scipy模組的linkage函數來獲得聚類的樹狀圖(Hierarchical tree)
linked = linkage(data, 'ward')

# 繪製樹狀圖
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending',
           show_leaf_counts=True)
plt.show()


