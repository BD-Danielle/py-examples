# ch33_1.py
import numpy as np
from scipy.cluster.hierarchy import linkage

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







