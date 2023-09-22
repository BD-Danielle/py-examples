# ch33_1_1.py
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
print(linked)
# 繪製樹狀圖
plt.figure(figsize=(10, 7))
dendrogram(linked, 
           orientation='top',
           labels=range(1, 9),
           distance_sort='descending',
           show_leaf_counts=True)
plt.show()



