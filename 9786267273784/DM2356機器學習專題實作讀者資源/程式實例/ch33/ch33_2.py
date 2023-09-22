# ch33_2.py
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# 定義一組簡單的二維數據點
data = np.array([[1, 2], 
                 [1, 4], 
                 [1, 0], 
                 [4, 2], 
                 [4, 4], 
                 [4, 0],
                 [10, 2],
                 [10, 4]])

# 進行凝聚性分群
linked = linkage(data, 'single')

# 繪製樹狀圖
plt.figure(figsize=(10, 7))
dendrogram(linked,                          # linkage()輸出
           orientation='top',               # 樹狀方向
           labels=range(0, 8),              # 原節點標記 0 ~ 7
           distance_sort='descending',      # 分支往下排序
           show_leaf_counts=True)           # 顯示葉節點數量
plt.show()



