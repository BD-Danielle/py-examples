# ch33_4.py
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import numpy as np

# 生成顧客資料
np.random.seed(1)
age = np.random.randint(20, 70, 100)            #年齡從20到70之間隨機數
income = np.random.randint(20000, 100000, 100)  #收入從20000到100000之間隨機數
customers = np.array(list(zip(age, income)))

# 進行凝聚性分群
Z = linkage(customers, method='ward')

# 繪製樹狀圖
plt.figure(figsize=(10, 5))
dendrogram(Z, leaf_rotation=90, leaf_font_size=8)
plt.show()



