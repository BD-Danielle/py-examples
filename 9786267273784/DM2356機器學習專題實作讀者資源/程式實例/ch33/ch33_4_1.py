# ch33_4_1.py
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import numpy as np

# 生成顧客資料
np.random.seed(1)
age = np.random.randint(20, 70, 100)            #年齡從20到70之間隨機數
income = np.random.randint(20000, 100000, 100)  #收入從20000到100000之間隨機數
customers = np.array(list(zip(age, income)))

# 使用凝聚性分群方法, 設定回傳 3 個群集 
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean',
                                  linkage='ward')
cluster.fit_predict(customers)

# 繪製圖形
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.scatter(customers[:,0], customers[:,1], c=cluster.labels_, cmap='viridis')
plt.xlabel('年齡')
plt.ylabel('收入')
plt.show()



