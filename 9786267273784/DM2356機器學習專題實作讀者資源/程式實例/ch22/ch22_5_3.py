# ch22_5_3.py
from sklearn.datasets import make_blobs
from sklearn.preprocessing import RobustScaler
import matplotlib.pyplot as plt

# 生成數據集
X, y = make_blobs(n_samples=200,n_features=2,centers=2,random_state=0)

# RobustScaler 縮放數據之間
X_sta = RobustScaler().fit_transform(X)

# 建立子圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# 繪製數據集
axs[0].scatter(X[:, 0], X[:, 1], c=y)
axs[0].set_title('一般數據集')
axs[0].grid()

# 繪製 RobustScaler 縮放數據
axs[1].scatter(X_sta[:, 0], X_sta[:, 1], c=y)
axs[1].set_title('RobustScaler 縮放數據')
axs[1].grid()

plt.show()                                 



