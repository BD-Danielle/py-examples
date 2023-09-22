# ch33_6.py
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('seeds_dataset.txt', sep='\t', header=None)

# 去除最右邊的分類特徵
data_without_class = data.iloc[:, :-1]

# 使用Scipy模組的linkage函數來獲得聚類的樹狀圖(Hierarchical tree)
linked = linkage(data_without_class, 'ward')

# 繪製樹狀圖
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending',
           show_leaf_counts=True)
plt.show()

